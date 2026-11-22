"""Essais de la voie abonnement v1 : faux appelants, aucun réseau. L'essai central compare, cellule par cellule, les
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
CHEMIN = Path(os.environ.get("VOIE_MODULE") or ICI / "voie_abonnement_v1.py")
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


def sessions(voie, dossier, modele_servi=None):
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
        assert voie.recueillir(dossier, k.name, t, f"session_faux_{n}", modele_servi or fiche["modele"]) == 0
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
        code = voie.lancer_moteur(nom, "branche-essai", argv_moteur(nom, tmp, dossier), v=v, appelants=faux.table())
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
                                  appelants=faux.table())
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
                                               tmp_path / "seq"), v=v, mod=mod, appelants=faux.table())
    assert code == voie.CODE_USAGE and faux.appels == []


# ---------- gardes ----------

def premiere_vague(env, tmp_path, nom="v8p"):
    voie = charger_voie()
    v = moteur(voie, nom)
    bloquer(env, v)
    d = tmp_path / "run"
    assert voie.lancer_moteur(nom, "b", argv_moteur(nom, tmp_path, d), v=v, appelants=Faux(v).table()) == v.CODE_PORTE
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
        voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-opus-5-5")  # kit de Fable
    assert voie.recueil(d, "E3-T1-conception-A") is None
    assert voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2") == 0  # cas sain


def test_recueil_vide_refuse(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    t = tmp_path / "r.md"
    t.write_text("  \n", encoding="utf-8")
    with pytest.raises(SystemExit):
        voie.recueillir(d, "E3-T1-conception-A", t, "s", "claude-fable-5-2")
    assert voie.recueil(d, "E3-T1-conception-A") is None


def test_reponse_alteree_refusee(env, tmp_path):
    voie, d = premiere_vague(env, tmp_path)
    assert sessions(voie, d) == 2
    f = d / "abonnement" / "reponses" / "E3-T1-conception-A.md"
    f.write_text(f.read_text(encoding="utf-8") + "ajout", encoding="utf-8")
    with pytest.raises(ValueError):
        voie.recueil(d, "E3-T1-conception-A")


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
    code = voie.lancer_moteur("v8p", "b", argv_moteur("v8p", tmp_path, d), v=v, appelants=faux.table())
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
    voie_obj = voie.Voie(v, "b")
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
