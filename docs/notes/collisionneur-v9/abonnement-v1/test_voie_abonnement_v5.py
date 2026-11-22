"""Essais de la voie abonnement v5 : copie des essais de la v4 (effort « max » passé), plus les essais de la v5 en fin.

En-tête de la v4 :
Essais de la voie abonnement v4 : copie des essais de la v3, plus les essais de la v4 en fin.

En-tête de la v3 :
Essais de la voie abonnement v3 : copie des essais de la v2, plus les essais de la v3 en fin.

En-tête de la v2 :
Essais de la voie abonnement v2 : copie des essais de la v1, accordés (--fin), plus les essais des corrections en fin.

En-tête de la v1 :
Essais de la voie abonnement v1 : faux appelants, aucun réseau. L'essai central compare, cellule par cellule, les
invites servies et les cellules écrites d'un dossier joué tout par l'interface (doublures) et du même dossier joué par
la voie abonnement (kits, recueil, relance), sur le v8m, le v8p et l'essaim v7. Chaque garde : un cas sain et un
artefact (R5).

Lancement : PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/abonnement-v1/
(VOIE_MODULE=chemin d'une copie mutée : mêmes essais sur la copie.)
"""
import hashlib
import importlib.util
import json
import os
import re
import socket
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
CHEMIN = Path(os.environ.get("VOIE_MODULE") or ICI / "voie_abonnement_v5.py")
FINS = {"anthropic": "end_turn", "gemini": "STOP", "openai": "stop", "kimi": "stop"}
QUESTION = ("Des agents de langue accomplissent de longues tâches. Quelle expérience trancherait entre deux "
            "hypothèses sur les moniteurs ? Donnez une question, une réponse réfutable et une expérience.\n")
MOTIF_IDS = re.compile(r"^- ((?:salon|revue|erratum|prepub)-[0-9a-f]{6}(?:-v\d+)?) \(", re.M)


def reseau_interdit(*a, **k):
    raise AssertionError("appel réseau réel interdit dans les essais")


def charger_voie():
    spec = importlib.util.spec_from_file_location("voie_essai", CHEMIN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class FauxFlux:
    def __init__(self, corps):
        self.corps = corps

    def read(self, *a):
        return json.dumps(self.corps).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class FauxCompteur:
    def __init__(self):
        self.urls = []

    def __call__(self, requete, delai, locale=False):
        corps = json.loads(requete.data)
        url = requete.full_url
        self.urls.append(url)
        if url.endswith("/v1/messages/count_tokens"):
            texte, champ = corps["messages"][0]["content"], "input_tokens"
        elif url.endswith(":countTokens"):
            texte, champ = corps["contents"][0]["parts"][0]["text"], "totalTokens"
        elif url.endswith("/responses/input_tokens"):
            texte, champ = corps["input"], "input_tokens"
        else:
            raise AssertionError(url)
        return FauxFlux({champ: int(len(texte) / 2.5)})


def texte_de(prompt):
    """Réponse déterministe, fonction de l'invite seule (la même par l'interface et par l'abonnement)."""
    j = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:10]
    if re.search(r"^Cycle \d+ sur \d+\. Vous recevez", prompt, re.M):
        morceaux = [f"=== SALON question ===\nTitre : question {j}\nUne question courte.\n=== FIN SALON ===",
                    f"=== PREPUBLICATION ===\nTitre : texte {j}\n" + "mot " * 50 + "\n=== FIN PREPUBLICATION ==="]
        for cible in re.findall(r"<<<DÉBUT A-REVOIR (\S+) sha256=", prompt):
            morceaux.append(f"=== REVUE {cible} ===\nObjection : le contrôle négatif manque.\n=== FIN REVUE ===")
        ids = MOTIF_IDS.findall(prompt)
        if ids:
            morceaux.append(f"=== OUVRIR ===\n{ids[0]}\n=== FIN OUVRIR ===")
        return "\n".join(morceaux) + "\nFIN-DE-CELLULE"
    if "Temps final. Écris seul ta réponse" in prompt:
        return f"Réponse finale {j}.\n=== SALON question ===\nTitre : F{j}\nfin\n=== FIN SALON ===\nFIN-DE-CELLULE"
    return f"Proposition {j} avec des idées.\nFIN-DE-CELLULE"


class Faux:
    def __init__(self, v):
        self.v, self.appels = v, []

    def __call__(self, m, prompt, max_tokens):
        self.appels.append((m["fournisseur"], prompt))
        usage = {"entree": 100, "sortie": 200}
        if m["fournisseur"] == "gemini":
            usage.update(reflexion=10, ecart_total=0)
        return self.v.Reponse(texte=texte_de(prompt), modele_servi=m["id"], fin=FINS[m["fournisseur"]], usage=usage,
                              usage_lu=True)

    def table(self):
        return {f: self for f in FINS}


def bloquer(monkeypatch, v):
    monkeypatch.setattr(v, "TRANSPORT", reseau_interdit)
    v.TRANSPORT_COMPTE = FauxCompteur()
    monkeypatch.setattr(v, "DORMIR", lambda s: None)


@pytest.fixture
def env(monkeypatch):
    monkeypatch.setattr(socket, "create_connection", reseau_interdit)
    monkeypatch.setattr(socket.socket, "connect", reseau_interdit)
    monkeypatch.setenv("GEMINI_API_KEY", "cle-gemini-factice")
    monkeypatch.setenv("MA_CLE", "cle-anthropic-factice")
    monkeypatch.setenv("OPENAI_API_KEY", "cle-openai-factice")
    monkeypatch.setenv("OPENAI_API_KEY_ESSAI", "cle-openai-factice")
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    monkeypatch.delenv("ANTHROPIC_WORKSPACE_ID", raising=False)
    return monkeypatch


def journal(d):
    return [json.loads(l) for l in (Path(d) / "journal.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]


def sessions(voie, dossier, modele_servi=None, fin="end_turn"):
    """Joue les sessions filles des kits en attente : réponse déterministe, versée par « recueillir »."""
    base = Path(dossier) / "abonnement" / "kits"
    n = 0
    for k in sorted(base.iterdir()):
        if voie.recueil(dossier, k.name) is not None:
            continue
        fiche = json.loads((k / "fiche.json").read_text(encoding="utf-8"))
        servi = (k / "texte-servi.md").read_text(encoding="utf-8")
        assert hashlib.sha256(servi.encode("utf-8")).hexdigest() == fiche["sha256_texte_servi"]
        assert fiche["effort"] == "max" and fiche["outils"] == "aucun"
        t = Path(dossier).parent / f"rep-{k.name}.md"
        t.write_text(texte_de(servi), encoding="utf-8")
        assert voie.recueillir(dossier, k.name, t, f"session_faux_{n}", modele_servi or fiche["modele"], fin) == 0
        n += 1
    return n


def cellules(d):
    return {p.name: p.read_text(encoding="utf-8") for p in sorted((Path(d) / "cellules").glob("*.md"))}


def invites(d):
    return {(e["cellule"], e["essai"]): e["sha256_prompt"] for e in journal(d) if "cellule" in e and "essai" in e}


ARGV_MOTEUR = {
    "v8m": ["--fable", "--opus", "--argon", "--astra"],
    "v8p": ["--fable", "--opus", "--argon", "--astra", "--place-iii3", "fin"],
}


def argv_moteur(nom, tmp, dossier):
    q = tmp / "question.md"
    q.write_text(QUESTION, encoding="utf-8")
    return ["etage3", *ARGV_MOTEUR[nom], "--cle-anthropic", "MA_CLE", "--sortie", str(dossier), "--faits", str(q),
            "--question", str(q), "--plafond-usd", "60"]


def moteur(voie, nom):
    return voie.charger(*voie.MOTEURS[nom], f"moteur_{nom}_essai_{os.urandom(4).hex()}")


def jouer_abonnement(voie, nom, tmp, env, dossier, tours_max=8):
    vagues, codes = 0, []
    while True:
        v = moteur(voie, nom)
        bloquer(env, v)
        faux = Faux(v)
        code = voie.lancer_moteur(nom, "branche-essai", argv_moteur(nom, tmp, dossier), v=v, appelants=faux.table(), effort="max")
        assert not [a for a in faux.appels if a[0] == "anthropic"]  # jamais d'appel à Anthropic
        assert not [u for u in v.TRANSPORT_COMPTE.urls if "anthropic" in u]  # ni de comptage sur la clé
        codes.append(code)
        if code == 0:
            return vagues, codes, v
        assert code == v.CODE_PORTE
        vagues += 1
        assert sessions(voie, dossier) > 0
        assert vagues <= tours_max


@pytest.mark.parametrize("nom", ["v8m", "v8p"])
def test_moteur_meme_dossier_par_les_deux_voies(env, tmp_path, nom):
    voie = charger_voie()
    v = moteur(voie, nom)
    bloquer(env, v)
    ref = tmp_path / "interface"
    assert v.principal(argv_moteur(nom, tmp_path, ref), appelants=Faux(v).table()) == 0
    ab = tmp_path / "abonnement"
    vagues, codes, v2 = jouer_abonnement(voie, nom, tmp_path, env, ab)
    assert vagues == 3  # III.1, III.2, III.3 : une vague par tour
    assert cellules(ref) == cellules(ab)
    assert invites(ref) == invites(ab)
    lignes = [e for e in journal(ab) if "voie_abonnement" in e]
    claude = [e for e in v2.essais_journal(ab) if e["modele_demande"].startswith("claude-")]
    assert len(lignes) == len(claude) == 6
    assert all(e["cout_usd"] == 0 and e["id_reponse"] == "abonnement" and e["statut"] == "OK" for e in claude)
    assert all(e["effort_session"] == "max" and e["session"].startswith("session_faux_") for e in lignes)
    autres = [e for e in v2.essais_journal(ab) if not e["modele_demande"].startswith("claude-")]
    assert len(autres) == 6 and all(e["cout_usd"] > 0 for e in autres)
    assert v2.principal(["verifier", str(ab)]) == 0


def config_essaim(tmp, **sur):
    cfg = json.loads((ICI.parent / "essaim-v1" / "configuration-pilote-essaim-v7.json").read_text(encoding="utf-8"))
    cfg.update(references_usd={e: 20.0 for e in cfg["especes"]}, cycles=2, place_iii3="fin")
    cfg.update(sur)
    p = tmp / f"configuration-{len(list(tmp.glob('configuration-*')))}.json"
    p.write_text(json.dumps(cfg, ensure_ascii=False), encoding="utf-8")
    return p


def argv_essaim(tmp, cfg, dossier, extra=()):
    q = tmp / "question.md"
    q.write_text(QUESTION, encoding="utf-8")
    return ["lancer", "--configuration", str(cfg), "--question", str(q), "--sortie", str(dossier), "--plafond-usd",
            "80", "--ligne-usd", "80", "--cle-anthropic", "MA_CLE", "--cle-openai", "OPENAI_API_KEY_ESSAI", *extra]


def essaim(voie):
    mod = voie.charger(*voie.ESSAIM, f"essaim_essai_{os.urandom(4).hex()}")
    return mod, mod.charger_moteur()


def test_essaim_meme_dossier_par_les_deux_voies(env, tmp_path):
    voie = charger_voie()
    cfg = config_essaim(tmp_path)
    mod, v = essaim(voie)
    bloquer(env, v)
    ref = tmp_path / "interface" / "essaim"  # même nom de dossier : mêmes tirages (cle_dossier lit le nom)
    assert mod.principal(argv_essaim(tmp_path, cfg, ref), appelants=Faux(v).table(), v=v) == 0
    ab = tmp_path / "abonnement" / "essaim"
    vagues = 0
    while True:
        mod, v = essaim(voie)
        bloquer(env, v)
        faux = Faux(v)
        code = voie.lancer_essaim("branche-essai", argv_essaim(tmp_path, cfg, ab), v=v, mod=mod,
                                  appelants=faux.table(), effort="max")
        assert not [a for a in faux.appels if a[0] == "anthropic"]
        assert not [u for u in v.TRANSPORT_COMPTE.urls if "anthropic" in u]
        if code == 0:
            break
        assert code == voie.CODE_PORTE
        vagues += 1
        assert sessions(voie, ab) == 2  # Fable et Opus à chaque temps
        assert vagues <= 6
    assert vagues == 4  # temps 0, cycles 1 et 2, temps final
    assert cellules(ref) == cellules(ab)
    assert invites(ref) == invites(ab)
    assert mod.publications(v, ref).keys() == mod.publications(v, ab).keys()
    assert mod.verifier_essaim(v, ab) == []


def test_essaim_sequentiel_refuse(env, tmp_path):
    voie = charger_voie()
    mod, v = essaim(voie)
    bloquer(env, v)
    faux = Faux(v)
    code = voie.lancer_essaim("b", argv_essaim(tmp_path, config_essaim(tmp_path, ordre="sequentiel_retire"),
                                               tmp_path / "seq"), v=v, mod=mod, appelants=faux.table(), effort="max")
    assert code == voie.CODE_USAGE and faux.appels == []


# ---------- gardes ----------

def premiere_vague(env, tmp_path, nom="v8p"):
    voie = charger_voie()
    v = moteur(voie, nom)
    bloquer(env, v)
    d = tmp_path / "run"
    assert voie.lancer_moteur(nom, "b", argv_moteur(nom, tmp_path, d), v=v, appelants=Faux(v).table(), effort="max") == v.CODE_PORTE
    return voie, d


def test_kits_listes_puis_recueillis(env, tmp_path, capsys):
    voie, d = premiere_vague(env, tmp_path)
    capsys.readouterr()
    assert voie.kits_en_attente(d) == 0
    lignes = capsys.readouterr().out.strip().splitlines()
    assert [l.split("\t")[0] for l in lignes] == ["E3-T1-conception-A", "E3-T1-conception-B"]
    assert sessions(voie, d) == 2
    capsys.readouterr()
    assert voie.kits_en_attente(d) == 0 and capsys.readouterr().out == ""


def test_recueil_modele_different_refuse(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    t = tmp_path / "r.md"
    t.write_text("Réponse. FIN-DE-CELLULE", encoding="utf-8")
    with pytest.raises(SystemExit):
        voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-opus-5-5", "end_turn")  # kit de Fable
    assert voie.recueil(d, "E3-T1-conception-A") is None
    assert voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2", "end_turn") == 0  # cas sain


def test_recueil_vide_refuse(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    t = tmp_path / "r.md"
    t.write_text("  \n", encoding="utf-8")
    with pytest.raises(SystemExit):
        voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2", "end_turn")
    assert voie.recueil(d, "E3-T1-conception-A") is None


def test_reponse_alteree_refusee(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    assert sessions(voie, d) == 2
    f = d / "abonnement" / "reponses" / "E3-T1-conception-A.md"
    f.write_text(f.read_text(encoding="utf-8") + "ajout", encoding="utf-8")
    with pytest.raises(ValueError):
        voie.recueil(d, "E3-T1-conception-A")
    v = moteur(voie, "v8p")  # v2 : à la relance, arrêt nommé, pas une trace
    bloquer(env, v)
    assert voie.lancer_moteur("v8p", "b", argv_moteur("v8p", tmp_path, d), v=v, appelants=Faux(v).table(), effort="max") == 1


def test_texte_servi_change_arrete(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    assert sessions(voie, d) == 2
    j = d / "abonnement" / "reponses" / "E3-T1-conception-A.json"
    fiche = json.loads(j.read_text(encoding="utf-8"))
    fiche["sha256_texte_servi"] = "0" * 64
    texte = json.dumps(fiche, ensure_ascii=False, indent=1) + "\n"
    j.write_text(texte, encoding="utf-8")
    Path(str(j) + ".sha256").write_text(f"{hashlib.sha256(texte.encode()).hexdigest()}  {j.name}\n", encoding="utf-8")
    v = moteur(voie, "v8p")
    bloquer(env, v)
    faux = Faux(v)
    code = voie.lancer_moteur("v8p", "b", argv_moteur("v8p", tmp_path, d), v=v, appelants=faux.table(), effort="max")
    assert code == voie.CODE_USAGE
    assert not v.cellule_valide(d, "E3-T1-conception-A")


def test_deux_voies_ne_se_melent_pas(env, tmp_path):
    voie = charger_voie()
    v = moteur(voie, "v8p")
    bloquer(env, v)
    d = tmp_path / "run"
    faux = Faux(v)
    ref = Faux(v)
    # tour 1 joué par l'interface, puis la conception de Fable rendue invalide : la voie abonnement refuse de la reprendre
    v.fixer_composition(["fable", "opus", "argon", "astra"], nom_cle_anthropic="MA_CLE")
    lettre = next(l for l in v.LETTRES if v.MODELES[l]["espece"] == "fable")
    assert v.executer_cellule(str(d), "E3-T1", lettre, "mot " * 500, [], 50.0, ref.table()) == "OK"
    (d / "cellules" / "E3-T1-conception-A.md").unlink()
    voie_obj = voie.Voie(v, "b", "max")
    with pytest.raises(v.Arret) as e:
        voie_obj.executer(str(d), "E3-T1", lettre, "mot " * 500, [], 50.0, faux.table())
    assert e.value.code == voie.CODE_USAGE and faux.appels == []


def test_kit_jamais_ecrase(env, tmp_path):
    voie = charger_voie()
    p = tmp_path / "k" / "texte-servi.md"
    voie.ecrire_scelle(p, "un")
    assert voie.ecrire_scelle(p, "un") == hashlib.sha256(b"un").hexdigest()  # cas sain : même contenu
    with pytest.raises(ValueError):
        voie.ecrire_scelle(p, "deux")
    assert p.read_text(encoding="utf-8") == "un"


def test_moteur_altere_refuse(tmp_path):
    voie = charger_voie()
    copie = tmp_path / "m.py"
    copie.write_bytes(voie.MOTEURS["v8p"][0].read_bytes() + b"\n")
    with pytest.raises(SystemExit):
        voie.charger(copie, voie.MOTEURS["v8p"][1], "m_altere")


def test_appel_direct_a_anthropic_refuse():
    voie = charger_voie()
    with pytest.raises(AssertionError):
        voie.refuser_anthropic({}, "x", 1)


def test_fiche_de_recueil_alteree_sans_sceau_refusee(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    assert sessions(voie, d) == 2
    assert voie.recueil(d, "E3-T1-conception-A") is not None  # cas sain
    j = d / "abonnement" / "reponses" / "E3-T1-conception-A.json"
    j.write_text(j.read_text(encoding="utf-8").replace("session_faux_0", "session_autre"), encoding="utf-8")
    with pytest.raises(ValueError, match="sceau"):
        voie.recueil(d, "E3-T1-conception-A")


# ---------- v2 : corrections de la contre-lecture ----------

def test_v2_motif_interdit_aucun_kit(env, tmp_path):
    voie = charger_voie()
    v = moteur(voie, "v8p")
    bloquer(env, v)
    v.fixer_composition(["fable", "astra"], nom_cle_anthropic="MA_CLE")
    lettre = next(l for l in v.LETTRES if v.MODELES[l]["espece"] == "fable")
    d = tmp_path / "run"
    w = voie.Voie(v, "b", "max")
    sain = "mot " * 500
    assert w.executer(str(d), "E3-T1", lettre, sain, [], 50.0, Faux(v).table()) == "KIT"  # cas sain
    prompt = sain + " écrire à quelqu.un@exemple.fr " + sain  # motif « courriel »
    with pytest.raises(v.Arret) as e:
        w.executer(str(d), "E3-T2", lettre, prompt, [], 50.0, Faux(v).table())
    assert e.value.code == v.CODE_MOTIF
    assert not (d / "abonnement" / "kits" / v.id_cellule("E3-T2", lettre)).exists()


def test_v2_plafond_avant_kit(env, tmp_path):
    voie = charger_voie()
    v = moteur(voie, "v8p")
    bloquer(env, v)
    v.fixer_composition(["fable", "astra"], nom_cle_anthropic="MA_CLE")
    lettre = next(l for l in v.LETTRES if v.MODELES[l]["espece"] == "fable")
    d = tmp_path / "run"
    w = voie.Voie(v, "b", "max")
    with pytest.raises(v.Arret) as e:
        w.executer(str(d), "E3-T1", lettre, "mot " * 500, [], 0.01, Faux(v).table())
    assert e.value.code == v.CODE_PLAFOND
    assert not (d / "abonnement" / "kits").exists()
    assert w.executer(str(d), "E3-T1", lettre, "mot " * 500, [], 50.0, Faux(v).table()) == "KIT"  # cas sain


def test_v2_dossier_commence_par_l_interface_refuse(env, tmp_path):
    voie = charger_voie()
    v = moteur(voie, "v8p")
    bloquer(env, v)
    d = tmp_path / "run"
    argv = argv_moteur("v8p", tmp_path, d)
    faux = Faux(v)

    class Arret1:  # le tour 1 joué par l'interface, puis arrêt avant le tour 2
        def __init__(self):
            self.n = 0

        def __call__(self, m, prompt, max_tokens):
            self.n += 1
            if self.n > 4:
                return v.Reponse(echec="arrêt de l'essai", usage={"entree": 0, "sortie": 0})
            return faux(m, prompt, max_tokens)
    a = Arret1()
    assert v.principal(argv, appelants={f: a for f in FINS}) != 0
    assert all(v.cellule_valide(d, f"E3-T1-conception-{l}") for l in "ABCD")
    v2 = moteur(voie, "v8p")
    bloquer(env, v2)
    f2 = Faux(v2)
    assert voie.lancer_moteur("v8p", "b", argv, v=v2, appelants=f2.table(), effort="max") == 1
    assert not (d / "abonnement" / "kits").exists() and not [x for x in f2.appels if x[0] == "anthropic"]


@pytest.mark.parametrize("fin,statut", [("max_tokens", "TRONQUE"), ("refusal", "REFUS")])
def test_v2_fin_de_session_rendue_au_moteur(env, tmp_path, fin, statut):
    voie, d = premiere_vague(env, tmp_path)
    t = tmp_path / "r.md"
    t.write_text("Réponse coupée", encoding="utf-8")
    assert voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2", fin) == 0
    v = moteur(voie, "v8p")
    bloquer(env, v)
    assert voie.lancer_moteur("v8p", "b", argv_moteur("v8p", tmp_path, d), v=v, appelants=Faux(v).table(), effort="max") != 0
    assert not v.cellule_valide(d, "E3-T1-conception-A")
    assert v.essais_journal(d, "E3-T1-conception-A")[0]["statut"] == statut  # v3 : le premier essai (lecture unique)


def test_v2_fin_inconnue_refusee(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    t = tmp_path / "r.md"
    t.write_text("Réponse. FIN-DE-CELLULE", encoding="utf-8")
    with pytest.raises(SystemExit):
        voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2", "stop")
    assert voie.recueil(d, "E3-T1-conception-A") is None


@pytest.mark.parametrize("sur", [{"parts": "bloquantes"}, {"reserver_finales": True}])
def test_v2_essaim_parts_bloquantes_ou_reserve_refusees(env, tmp_path, sur):
    voie = charger_voie()
    mod, v = essaim(voie)
    bloquer(env, v)
    faux = Faux(v)
    code = voie.lancer_essaim("b", argv_essaim(tmp_path, config_essaim(tmp_path, **sur), tmp_path / "e"), v=v, mod=mod,
                              appelants=faux.table(), effort="max")
    assert code == voie.CODE_USAGE and faux.appels == []


def test_v2_sceau_orphelin_et_sceau_faux(tmp_path):
    voie = charger_voie()
    p = tmp_path / "a.md"
    Path(str(p) + ".sha256").write_text("0" * 64 + "  a.md\n", encoding="utf-8")
    with pytest.raises(ValueError, match="sans son fichier"):
        voie.ecrire_scelle(p, "un")
    assert not p.exists()
    q = tmp_path / "b.md"
    q.write_text("un", encoding="utf-8")
    Path(str(q) + ".sha256").write_text("0" * 64 + "  b.md\n", encoding="utf-8")
    with pytest.raises(ValueError):
        voie.ecrire_scelle(q, "un")


def test_v2_recueillir_en_ligne_de_commande_sans_trace(env, tmp_path, capsys):
    voie, d = premiere_vague(env, tmp_path)
    t = tmp_path / "r.md"
    t.write_text("Réponse. FIN-DE-CELLULE", encoding="utf-8")
    (d / "abonnement" / "kits" / "E3-T1-conception-A" / "fiche.json.sha256").unlink()
    code = voie.principal(["recueillir", str(d), "E3-T1-conception-A", "--texte", str(t), "--session", "s",
                           "--modele-servi", "claude-fable-5-2", "--fin", "end_turn"])
    assert code == 1 and "sceau" in capsys.readouterr().err


def test_v2_v8m_effort_max_equivalent_sans_rejeu(env, tmp_path):
    voie = charger_voie()
    v = moteur(voie, "v8m")
    bloquer(env, v)
    ref = tmp_path / "interface"
    a = argv_moteur("v8m", tmp_path, ref) + ["--effort-max"]
    assert v.principal(a, appelants=Faux(v).table()) == 0
    ab = tmp_path / "abonnement"
    while True:
        v2 = moteur(voie, "v8m")
        bloquer(env, v2)
        code = voie.lancer_moteur("v8m", "b", argv_moteur("v8m", tmp_path, ab) + ["--effort-max"], v=v2,
                                  appelants=Faux(v2).table(), effort="max")
        if code == 0:
            break
        assert code == v2.CODE_PORTE and sessions(voie, ab) > 0
    assert cellules(ref) == cellules(ab) and invites(ref) == invites(ab)
    assert not [e for e in journal(ab) if "rejeu_effort_xhigh_declare" in e or e.get("rejeu_effort_xhigh")]
    assert [e for e in journal(ab) if "voie_abonnement" in e]


# ---------- v3 ----------

def test_v3_tronque_un_seul_essai_sans_relance_fictive(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    t = tmp_path / "r.md"
    t.write_text("Réponse coupée", encoding="utf-8")
    assert voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2", "max_tokens") == 0
    v = moteur(voie, "v8p")
    bloquer(env, v)
    assert voie.lancer_moteur("v8p", "b", argv_moteur("v8p", tmp_path, d), v=v, appelants=Faux(v).table(), effort="max") != 0
    es = v.essais_journal(d, "E3-T1-conception-A")
    assert [e["statut"] for e in es] == ["TRONQUE", "ECHEC"]
    assert "relance impossible par la voie abonnement" in es[1]["echec"]
    assert all(e["cout_usd"] == 0 for e in es)


def test_v3_v8m_effort_max_vide_aucun_rejeu_declare(env, tmp_path):
    voie = charger_voie()
    v = moteur(voie, "v8m")
    bloquer(env, v)
    d = tmp_path / "run"
    a = argv_moteur("v8m", tmp_path, d) + ["--effort-max"]
    assert voie.lancer_moteur("v8m", "b", a, v=v, appelants=Faux(v).table(), effort="max") == v.CODE_PORTE
    t = tmp_path / "r.md"
    t.write_text("", encoding="utf-8")
    with pytest.raises(SystemExit):  # v3 : un vide coupé ne se verse pas
        voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2", "max_tokens")
    assert voie.recueil(d, "E3-T1-conception-A") is None
    assert voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2", "refusal") == 0  # un refus peut être vide
    v2 = moteur(voie, "v8m")
    bloquer(env, v2)
    assert voie.lancer_moteur("v8m", "b", a, v=v2, appelants=Faux(v2).table(), effort="max") != 0
    assert not [e for e in journal(d) if "rejeu_effort_xhigh_declare" in e]
    assert v2.statut_courant(d, "E3-T1-conception-A") == "REFUS"


@pytest.mark.parametrize("sur", [{"parts": "bloquantes"}, {"reserver_finales": True}, {"ordre": "sequentiel_retire"}])
def test_v3_essaim_refus_avant_toute_ecriture(env, tmp_path, sur):
    voie = charger_voie()
    mod, v = essaim(voie)
    bloquer(env, v)
    e = tmp_path / "e"
    assert voie.lancer_essaim("b", argv_essaim(tmp_path, config_essaim(tmp_path, **sur), e), v=v, mod=mod,
                              appelants=Faux(v).table(), effort="max") == voie.CODE_USAGE
    assert not e.exists()


def test_v3_erreur_du_moteur_hors_du_filet(env, tmp_path, monkeypatch):
    voie, d = premiere_vague(env, tmp_path)
    assert sessions(voie, d) == 2
    v = moteur(voie, "v8p")
    bloquer(env, v)
    w = voie.Voie(v, "b", "max")

    def casse(*a, **k):
        raise KeyError("erreur propre au moteur")
    w.original = casse
    lettre = next(l for l in v.LETTRES if v.MODELES[l]["espece"] == "fable") if v.LETTRES else None
    v.fixer_composition(["fable", "opus", "argon", "astra"], nom_cle_anthropic="MA_CLE")
    prompt = (d / "abonnement" / "kits" / "E3-T1-conception-A" / "texte-servi.md").read_text(encoding="utf-8")
    with pytest.raises(KeyError):
        w.executer(str(d), "E3-T1", "A", prompt, [], 50.0, Faux(v).table())


# ---------- v4 ----------

def test_v4_absence_acceptee_apres_tronque_puis_dossier_au_bout(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    t = tmp_path / "r.md"
    t.write_text("Réponse coupée", encoding="utf-8")
    assert voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2", "max_tokens") == 0
    t2 = tmp_path / "r2.md"
    servi = (d / "abonnement" / "kits" / "E3-T1-conception-B" / "texte-servi.md").read_text(encoding="utf-8")
    t2.write_text(texte_de(servi), encoding="utf-8")
    assert voie.recueillir(d, "E3-T1-conception-B", t2, "s2", "claude-opus-5-5", "end_turn") == 0
    v = moteur(voie, "v8p")
    bloquer(env, v)
    assert voie.lancer_moteur("v8p", "b", argv_moteur("v8p", tmp_path, d), v=v, appelants=Faux(v).table(), effort="max") != 0
    assert all(e["id_reponse"] == "abonnement" for e in v.essais_journal(d, "E3-T1-conception-A"))
    argv = argv_moteur("v8p", tmp_path, d) + ["--accepter-absence", "E3-T1-conception-A"]
    for _ in range(4):
        v = moteur(voie, "v8p")
        bloquer(env, v)
        code = voie.lancer_moteur("v8p", "b", argv, v=v, appelants=Faux(v).table(), effort="max")
        if code == 0:
            break
        assert code == v.CODE_PORTE, code  # jamais l'arrêt pour mélange (code 1)
        assert sessions(voie, d) > 0
    assert code == 0


def test_v4_configuration_forme_egal_et_illisible(env, tmp_path, capsys):
    voie = charger_voie()
    mod, v = essaim(voie)
    bloquer(env, v)
    e = tmp_path / "e"
    argv = argv_essaim(tmp_path, config_essaim(tmp_path, parts="bloquantes"), e)
    i = argv.index("--configuration")
    argv = argv[:i] + [f"--configuration={argv[i + 1]}"] + argv[i + 2:]
    assert voie.lancer_essaim("b", argv, v=v, mod=mod, appelants=Faux(v).table(), effort="max") == voie.CODE_USAGE
    assert not e.exists()
    mauvais = tmp_path / "mauvais.json"
    mauvais.write_text("{pas du json", encoding="utf-8")
    argv2 = argv_essaim(tmp_path, mauvais, tmp_path / "e2")
    assert voie.lancer_essaim("b", argv2, v=v, mod=mod, appelants=Faux(v).table(), effort="max") == voie.CODE_USAGE
    assert not (tmp_path / "e2").exists() and "illisible" in capsys.readouterr().err


# ---------- v5 ----------

def test_v5_effort_xhigh_dans_la_fiche_et_le_journal(env, tmp_path):
    voie = charger_voie()
    v = moteur(voie, "v8p")
    bloquer(env, v)
    d = tmp_path / "run"
    assert voie.lancer_moteur("v8p", "b", argv_moteur("v8p", tmp_path, d), v=v, appelants=Faux(v).table(),
                              effort="xhigh") == v.CODE_PORTE
    fiches = [json.loads((k / "fiche.json").read_text(encoding="utf-8")) for k in (d / "abonnement" / "kits").iterdir()]
    assert len(fiches) == 2 and all(f["effort"] == "xhigh" for f in fiches)


def test_v5_effort_absent_ou_hors_liste_refuse(env, tmp_path):
    voie = charger_voie()
    v = moteur(voie, "v8p")
    with pytest.raises(ValueError):
        voie.Voie(v, "b", "high")
    with pytest.raises(ValueError):
        voie.Voie(v, "b", None)
    with pytest.raises(SystemExit):
        voie.principal(["v8p", "--", "etage3"])  # --effort obligatoire
