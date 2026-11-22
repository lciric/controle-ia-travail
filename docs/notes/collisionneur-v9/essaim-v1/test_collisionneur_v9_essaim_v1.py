"""Essais du collisionneur v9, mode essaim (v1). Faux appelants, aucun réseau : transport, transport des comptages et
connexions remplacés par des doublures qui lèvent une erreur ; chaque garde a un cas sain et un artefact (R5).

Lancement : PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/essaim-v1/test_collisionneur_v9_essaim_v1.py
(ESSAIM_MODULE=chemin d'une copie mutée : mêmes essais sur la copie, pour les mutations.)
"""
import importlib.util
import json
import os
import re
import shutil
import socket
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
CHEMIN = Path(os.environ.get("ESSAIM_MODULE") or ICI / "collisionneur_v9_essaim_v1.py")
QUESTION = ("Des agents de langue accomplissent de longues tâches. Quelle expérience trancherait entre deux "
            "hypothèses sur les moniteurs ? Donnez une question, une réponse réfutable et une expérience.\n")
FINS = {"anthropic": "end_turn", "gemini": "STOP", "openai": "stop"}


def reseau_interdit(*a, **k):
    raise AssertionError("appel réseau réel interdit dans les essais")


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
    """Doublure du transport des comptages (comme les essais de la v8d) : ⌊caractères / 2,5⌋."""

    def __init__(self):
        self.appels = []

    def __call__(self, requete, delai, locale=False):
        corps = json.loads(requete.data)
        url = requete.full_url
        self.appels.append(url)
        if url.endswith("/v1/messages/count_tokens"):
            texte, champ = corps["messages"][0]["content"], "input_tokens"
        elif url.endswith(":countTokens"):
            texte, champ = corps["contents"][0]["parts"][0]["text"], "totalTokens"
        elif url.endswith("/responses/input_tokens"):
            texte, champ = corps["input"], "input_tokens"
        else:
            raise AssertionError(url)
        return FauxFlux({champ: int(len(texte) / 2.5)})


def charger():
    spec = importlib.util.spec_from_file_location("essaim_essai", CHEMIN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def es(monkeypatch):
    mod = charger()
    v = mod.charger_v8d()
    monkeypatch.setattr(v, "TRANSPORT", reseau_interdit)
    v.TRANSPORT_COMPTE = FauxCompteur()
    monkeypatch.setattr(socket, "create_connection", reseau_interdit)
    monkeypatch.setattr(socket.socket, "connect", reseau_interdit)
    monkeypatch.setattr(v, "DORMIR", lambda s: None)
    monkeypatch.setenv("GEMINI_API_KEY", "cle-gemini-factice")
    monkeypatch.setenv("MA_CLE", "cle-anthropic-factice")
    monkeypatch.setenv("OPENAI_API_KEY_ESSAI", "cle-openai-factice")
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    monkeypatch.delenv("ANTHROPIC_WORKSPACE_ID", raising=False)
    return mod, v


def config(tmp, **sur):
    cfg = json.loads((ICI / "configuration-pilote-essaim-v1.json").read_text(encoding="utf-8"))
    cfg.update(enveloppe_usd=100.0, cycles=3)
    cfg.update(sur)
    p = tmp / f"configuration-{len(list(tmp.glob('configuration-*')))}.json"
    p.write_text(json.dumps(cfg, ensure_ascii=False), encoding="utf-8")
    return p


def phase(prompt):
    if "Temps de société, cycle" in prompt:
        return "cycle"
    if "Temps final : réponse finale privée" in prompt:
        return "finale"
    assert "Tour III.1" in prompt
    return "brouillon"


class Faux:
    """Faux appelant : répond selon le temps reconnu dans l'invite ; garde chaque invite. `special(n, m, prompt)` peut
    rendre un texte, une Reponse, ou lever une exception (coupure)."""

    def __init__(self, v, special=None, sortie=200, pensees=50):
        self.v, self.special, self.sortie, self.pensees = v, special, sortie, pensees
        self.invites, self.n = [], 0

    def texte(self, m, prompt):
        p = phase(prompt)
        jeton = f"SECRET{self.n}"
        if p == "brouillon":
            return f"Brouillon {jeton} avec des idées.\nFIN-DE-CELLULE"
        if p == "finale":  # une section balisée : une finale qui serait publiée paraîtrait dans les invites suivantes
            return (f"Réponse finale FINALE{self.n} privée.\n=== SALON ===\nTitre : FINALE{self.n}\nfin\n"
                    f"=== FIN SALON ===\nFIN-DE-CELLULE")
        morceaux = [f"=== SALON ===\nTitre : question {jeton}\nUne question courte sur les moniteurs.\n=== FIN SALON ===",
                    f"=== PREPUBLICATION ===\nTitre : texte {jeton}\n" + "mot " * 50 + "\n=== FIN PREPUBLICATION ==="]
        for cible in re.findall(r"<<<DÉBUT A-REVOIR (\S+) sha256=", prompt):
            morceaux.append(f"=== REVUE {cible} ===\nObjection vérifiable : le contrôle négatif manque.\n=== FIN REVUE ===")
        ids = re.findall(r"^- \[(\S+)\]", prompt, re.M)
        if ids:
            morceaux.append(f"=== OUVRIR ===\n{ids[0]}\n=== FIN OUVRIR ===")
        return "\n".join(morceaux) + "\nFIN-DE-CELLULE"

    def __call__(self, m, prompt, max_tokens):
        self.n += 1
        self.invites.append((m["espece"], prompt))
        t = None
        if self.special:
            t = self.special(self.n, m, prompt)
        if isinstance(t, self.v.Reponse):
            return t
        if t is None:
            t = self.texte(m, prompt)
        usage = {"entree": 100, "sortie": self.sortie}
        if m["fournisseur"] == "gemini":
            usage.update(reflexion=self.pensees, ecart_total=0)
        return self.v.Reponse(texte=t, modele_servi=m["id"], fin=FINS[m["fournisseur"]], usage=usage, usage_lu=True)

    def table(self):
        return {"anthropic": self, "gemini": self, "openai": self}


def lancer(mod, v, tmp, cfg, faux, nom="essaim", extra=()):
    q = tmp / "question.md"
    if not q.exists():
        q.write_text(QUESTION, encoding="utf-8")
    args = ["lancer", "--configuration", str(cfg), "--question", str(q), "--sortie", str(tmp / nom), "--plafond-usd",
            "50", "--ligne-usd", "50", "--cle-anthropic", "MA_CLE", "--cle-openai", "OPENAI_API_KEY_ESSAI", *extra]
    return mod.principal(args, appelants=faux.table(), v=v)


def journal(d):
    return [json.loads(l) for l in (d / "journal.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]


# ---------- chargement, tours ----------

def test_empreinte_v8d_controlee(es, tmp_path):
    mod, _ = es
    copie = tmp_path / "v8d.py"
    shutil.copy(mod.SCRIPT_V8D, copie)
    assert mod.charger_v8d(copie).VERSION == "collisionneur-v9-v8d"  # sain
    copie.write_text(copie.read_text(encoding="utf-8") + "\n# ajout\n", encoding="utf-8")
    with pytest.raises(SystemExit):  # artefact
        mod.charger_v8d(copie)


def test_tours_ajoutes_sans_changer_les_existants(es, tmp_path):
    mod, v = es
    avant = json.dumps(v.TOURS, sort_keys=True)
    cfg = mod.lire_configuration(v, config(tmp_path))
    mod.installer_tours(v, cfg)
    assert {t: v.TOURS[t] for t in json.loads(avant)} == json.loads(avant)
    v.fixer_composition(cfg["especes"])
    cid = v.id_cellule(mod.tour_cycle(2), "C")
    assert cid == "W1-C02-societe-C" and mod.decoupe_cid(v, cid) == ("W1-C02", "C")
    d = tmp_path / "d"
    assert v.cellule_valide(d, cid) is None and v.prochain_essai(d, cid) == 1
    v.ecrire_neuf(v.chemin_cellule(d, cid), "texte")
    assert v.cellule_valide(d, cid)[0] == "texte"
    for tour in mod.tours_essaim(cfg):  # garde v3 de Google sur les tours neufs, Argon et Carbon
        for l in ("C", "E"):
            m = v.MODELES[l]
            corps = v.demande_gemini(m, "x", m["max"])
            assert v.verifier_reglages_google(m["espece"], corps, m["provision"], mots=v.TOURS[tour]["mots"]) == []
    m = v.MODELES["E"]  # artefact : limite de mots trop haute pour Carbon
    assert v.verifier_reglages_google("carbon", v.demande_gemini(m, "x", m["max"]), m["provision"], mots=5000)
    v.TOURS["W0-T1"] = {"nom": "autre", "mots": 1}
    with pytest.raises(v.Arret):  # artefact : un tour existant n'est jamais réécrit
        mod.installer_tours(v, cfg)


def test_configuration_gardee(es, tmp_path):
    mod, v = es
    mod.lire_configuration(v, config(tmp_path))  # sain
    for sur in ({"repartition": {"temps0": 0.3, "temps1": 0.55, "temps2": 0.2}}, {"enveloppe_usd": None},
                {"pseudonymes": ["Claude"] + [f"Nom{c}" for c in "abcdef"]}, {"cycles": 0}, {"relecteurs": 5}):
        with pytest.raises(v.Arret):
            mod.lire_configuration(v, config(tmp_path, **sur))


def test_lancer_refuse_sans_enveloppe_avant_tout_appel(es, tmp_path):
    mod, v = es
    faux = Faux(v)
    assert lancer(mod, v, tmp_path, config(tmp_path, enveloppe_usd=None), faux) == v.CODE_USAGE
    assert faux.n == 0 and v.TRANSPORT_COMPTE.appels == []


# ---------- déroulé complet ----------

def test_deroule_complet(es, tmp_path):
    mod, v = es
    faux = Faux(v)
    assert lancer(mod, v, tmp_path, config(tmp_path), faux) == 0
    d = tmp_path / "essaim"
    assert faux.n == 5 * (1 + 3 + 1)
    tir = json.loads((d / "tirages.json").read_text(encoding="utf-8"))
    for l in v.LETTRES:
        for t in mod.tours_essaim(json.loads((d / "configuration.json").read_text(encoding="utf-8"))):
            assert v.cellule_valide(d, v.id_cellule(t, l))
    pubs = mod.publications(v, d)
    assert len(pubs) == 15 and all(p["anomalies_balisage"] == [] and p["refuses"] == [] for p in pubs.values())
    # ordre fixe : les rangs des publications suivent l'ordre tiré
    for k in (1, 2, 3):
        assert [p["lettre"] for p in sorted(pubs.values(), key=lambda p: p["rang"]) if p["cycle"] == k] == tir["ordre"]
    els = mod.elements(v, d)
    assert sum(e["genre"] == "REVUE" for e in els) == 2 * 5 * 2  # deux relecteurs par dépôt, cycles 1 et 2
    assert all(e["relecteurs"] == [] for e in els if e["genre"] == "PREPUBLICATION" and e["cycle"] == 3)
    assert [e for e in journal(d) if "injection" in e][0]["injection"] is None
    assert mod.verifier_essaim(v, d) == []
    # tout appel est passé par executer_cellule : un essai journalisé par appel, avec comptage
    assert len(v.essais_journal(d)) == faux.n == len(v.TRANSPORT_COMPTE.appels)


def test_chaque_appel_passe_par_executer_cellule(es, tmp_path, monkeypatch):
    mod, v = es
    dedans = []
    vrai = v.executer_cellule

    def enveloppe(*a, **k):
        dedans.append(True)
        try:
            return vrai(*a, **k)
        finally:
            dedans.pop()

    monkeypatch.setattr(v, "executer_cellule", enveloppe)
    faux = Faux(v, special=lambda n, m, p: (None if dedans else pytest.fail("appel hors d'executer_cellule")))
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=1), faux) == 0 and faux.n == 15


def test_pseudonymes_sans_fuite_de_nom_de_modele(es, tmp_path):
    mod, v = es
    faux = Faux(v)
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=2), faux) == 0
    d = tmp_path / "essaim"
    tir = json.loads((d / "tirages.json").read_text(encoding="utf-8"))
    ids = [v.MODELES[l]["id"] for l in v.LETTRES]
    for espece, prompt in faux.invites:
        assert not mod.MOTIF_NOMS_MODELES.search(prompt), espece
        assert not any(i in prompt for i in ids)
        assert not re.search(r"W\d-[A-Z]\d+-[a-z-]+-[A-Z]\b|proposition [A-E]\b|-[A-E]>>>", prompt)
        lettre = next(l for l in v.LETTRES if v.MODELES[l]["espece"] == espece)
        assert f"Ton pseudonyme est {tir['pseudonymes'][lettre]}." in prompt
    assert len(set(tir["pseudonymes"].values()) | {tir["pseudonyme_tiers"]}) == 6
    # tirés à chaque exécution : un autre dossier, d'autres tirages (même graine)
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=1), Faux(v), nom="essaim-bis") == 0
    tir2 = json.loads((tmp_path / "essaim-bis" / "tirages.json").read_text(encoding="utf-8"))
    assert (tir2["pseudonymes"], tir2["ordre"]) != (tir["pseudonymes"], tir["ordre"])


def test_garde_du_cadre_contre_les_noms(es, tmp_path, monkeypatch):
    mod, v = es
    monkeypatch.setattr(mod, "CONSIGNE_FINALE", mod.CONSIGNE_FINALE + " Comme Claude le ferait.")
    faux = Faux(v)
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=1), faux) == v.CODE_USAGE
    assert faux.n == 10  # brouillons et cycle faits ; aucune réponse finale envoyée
    assert not any(phase(p) == "finale" for _, p in faux.invites)


def test_relecteurs_jamais_auteurs(es, tmp_path):
    mod, v = es
    cfg = mod.lire_configuration(v, config(tmp_path))
    v.fixer_composition(cfg["especes"])
    tir = mod.tirer(v, cfg, 7, [1])
    vus = set()
    for k in range(1, 30):
        for a in v.LETTRES:
            r = mod.tirer_relecteurs(v, cfg, tir, k, a)
            assert a not in r and len(set(r)) == 2
            vus.add(tuple(r))
    assert len(vus) > 3  # le tirage varie
    assert mod.tirer_relecteurs(v, cfg, tir, 3, "B") == mod.tirer_relecteurs(v, cfg, tir, 3, "B")  # rejouable


def test_revues_sans_note(es, tmp_path):
    mod, v = es
    for sain in ("Objection : le contrôle manque.", "Le taux de 1/10 des cas est trop bas.", "Antériorité à vérifier."):
        assert not mod.MOTIF_NOTE.search(sain), sain
    for note in ("Note : 8/10", "Score : 4", "Verdict : accepter", "7/10 pour la clarté", "weak accept", "note de 3"):
        assert mod.MOTIF_NOTE.search(note), note
    premier = []

    def special(n, m, prompt):
        cibles = re.findall(r"<<<DÉBUT A-REVOIR (\S+) sha256=", prompt)
        if phase(prompt) == "cycle" and cibles and not premier:
            premier.append(cibles)
            return "\n".join([f"=== REVUE {cibles[0]} ===\nNote : 8/10, bon travail.\n=== FIN REVUE ==="]
                             + [f"=== REVUE {c} ===\nObjection vérifiable sur la métrique.\n=== FIN REVUE ==="
                                for c in cibles[1:]]) + "\nFIN-DE-CELLULE"
        return None

    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=2), Faux(v, special=special)) == 0
    d = tmp_path / "essaim"
    refus = [r for p in mod.publications(v, d).values() for r in p["refuses"]]
    assert [r["motif"] for r in refus] == ["revue avec note ou verdict"] and refus[0]["cible"] == premier[0][0]
    assert all(not mod.MOTIF_NOTE.search(mod.lire_element(v, d, e)) for e in mod.elements(v, d) if e["genre"] == "REVUE")
    assert mod.verifier_essaim(v, d) == []


def test_part_epuisee_sautee(es, tmp_path):
    mod, v = es
    # Fable : 100 jetons d'entrée à 10 et 200 de sortie à 50 USD par million = 0,011 USD par appel ; part du temps 1 :
    # enveloppe × 0,55 / 5. Enveloppe 0,15 : part 0,0165 ; Fable fait deux cycles (0,011 < 0,0165), saute le troisième.
    faux = Faux(v)
    assert lancer(mod, v, tmp_path, config(tmp_path, enveloppe_usd=0.15), faux) == 0
    d = tmp_path / "essaim"
    lettre = next(l for l in v.LETTRES if v.MODELES[l]["espece"] == "fable")
    sauts = mod.sauts(v, d)
    cid = v.id_cellule("W1-C03", lettre)
    assert cid in sauts and sauts[cid]["motif"] == "part épuisée" and sauts[cid]["depense_phase_usd"] >= 0.0165
    assert v.essais_journal(d, cid) == [] and v.cellule_valide(d, v.id_cellule("W2-T1", lettre))  # finale faite
    assert v.essais_journal(d, v.id_cellule("W1-C02", lettre))  # sain : sous la part, appelé
    assert lancer(mod, v, tmp_path, config(tmp_path, enveloppe_usd=0.15), Faux(v)) == 0  # même configuration : rien à refaire
    assert lancer(mod, v, tmp_path, config(tmp_path, enveloppe_usd=0.2), Faux(v)) == v.CODE_USAGE  # autre : refusée


def test_tous_epuises_arrete_la_societe(es, tmp_path):
    mod, v = es
    faux = Faux(v)
    assert lancer(mod, v, tmp_path, config(tmp_path, enveloppe_usd=0.0001), faux) == 0
    d = tmp_path / "essaim"
    assert [e["arret_societe"] for e in journal(d) if "arret_societe" in e] == [2]
    assert faux.n == 5 + 5 + 5  # brouillons, un cycle, finales ; jamais sur consensus, sur budget


def test_reprise_apres_coupure(es, tmp_path):
    mod, v = es
    coupe = Faux(v, special=lambda n, m, p: (_ for _ in ()).throw(ConnectionResetError("coupure")) if n == 8 else None)
    cfg = config(tmp_path)
    assert lancer(mod, v, tmp_path, cfg, coupe) == v.CODE_ECHEC
    d = tmp_path / "essaim"
    tirages = (d / "tirages.json").read_bytes()
    valides_avant = {p.name for p in (d / "cellules").glob("*.md")}
    invite_coupee = coupe.invites[-1][1]
    suite = Faux(v)
    assert lancer(mod, v, tmp_path, cfg, suite) == 0
    assert suite.n == 25 - 7 and suite.invites[0][1] == invite_coupee  # rien de valide renvoyé ; même invite
    assert (d / "tirages.json").read_bytes() == tirages
    assert valides_avant < {p.name for p in (d / "cellules").glob("*.md")}
    assert mod.verifier_essaim(v, d) == []


def test_reprise_entre_cellule_et_publication(es, tmp_path, monkeypatch):
    mod, v = es
    vrai, vu = mod.publier, []

    def casse(*a, **k):
        vu.append(1)
        if len(vu) == 3:
            raise v.Arret(v.CODE_ECHEC, "coupure simulée avant la publication")
        return vrai(*a, **k)

    monkeypatch.setattr(mod, "publier", casse)
    cfg = config(tmp_path, cycles=2)
    assert lancer(mod, v, tmp_path, cfg, Faux(v)) == v.CODE_ECHEC
    monkeypatch.setattr(mod, "publier", vrai)
    suite = Faux(v)
    assert lancer(mod, v, tmp_path, cfg, suite) == 0
    assert suite.n == 20 - 8  # la cellule écrite n'est pas renvoyée ; elle est publiée à la reprise
    assert mod.verifier_essaim(v, tmp_path / "essaim") == []


def test_reprise_refuse_une_invite_differente(es, tmp_path, monkeypatch):
    mod, v = es
    cfg = config(tmp_path, cycles=2)
    coupe = Faux(v, special=lambda n, m, p: (_ for _ in ()).throw(ConnectionResetError("x")) if n == 8 else None)
    assert lancer(mod, v, tmp_path, cfg, coupe) == v.CODE_ECHEC
    d = tmp_path / "essaim"
    with monkeypatch.context() as mp:  # artefact 1 : le cadre change entre deux lancements ; la cellule coupée ne part pas
        mp.setattr(mod, "CONSIGNE_CYCLE", mod.CONSIGNE_CYCLE + " Ajout.")
        suite = Faux(v)
        assert lancer(mod, v, tmp_path, cfg, suite) == v.CODE_USAGE and suite.n == 0
    el = mod.elements(v, d)[0]  # artefact : le tableau change entre deux lancements (sceau refait à la main)
    chemin = d / el["chemin"]
    for p in (chemin, Path(str(chemin) + ".sha256")):
        p.chmod(0o644)
    nouveau = "Titre : autre\nautre texte\n"
    chemin.write_text(nouveau, encoding="utf-8")
    Path(str(chemin) + ".sha256").write_text(f"{v.empreinte(nouveau)}  {chemin.name}\n", encoding="utf-8")
    suite = Faux(v)  # artefact 2 : le tableau change (sceau refait) : arrêt dès qu'un texte altéré est lu
    assert lancer(mod, v, tmp_path, cfg, suite) == v.CODE_USAGE
    assert any("salon-1" in x for x in mod.verifier_essaim(v, d))


def test_arret_code_10_transmis(es, tmp_path):
    mod, v = es
    faux = Faux(v, pensees=0)
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=1), faux) == v.CODE_PENSEES == 10
    d = tmp_path / "essaim"
    assert [e["statut"] for e in v.essais_journal(d)][-1] == "SANS_PENSEES"
    assert v.MODELES[[l for l in v.LETTRES if v.essais_journal(d, v.id_cellule("W0-T1", l))
                      and v.essais_journal(d, v.id_cellule("W0-T1", l))[-1]["statut"] == "SANS_PENSEES"][0]][
        "fournisseur"] == "gemini"


def test_injection_avec_et_sans_fichier(es, tmp_path):
    mod, v = es
    cfg = config(tmp_path, cycles=1)
    sans = Faux(v)
    assert lancer(mod, v, tmp_path, cfg, sans, nom="sans") == 0
    j = [e for e in journal(tmp_path / "sans") if "injection" in e]
    assert len(j) == 1 and j[0]["injection"] is None and "rien n'est injecté" in j[0]["motif"]
    tiers = json.loads((tmp_path / "sans" / "tirages.json").read_text(encoding="utf-8"))["pseudonyme_tiers"]
    assert not any(tiers in p for _, p in sans.invites)
    f = tmp_path / "erreurs.md"
    texte = "Titre : un résultat connu\nSelon Durand et al. (2019), le taux vaut 42 %.\n"
    v.ecrire_neuf(f, texte)
    avec = Faux(v)
    assert lancer(mod, v, tmp_path, cfg, avec, nom="avec", extra=("--erreurs-plantees", str(f))) == 0
    d = tmp_path / "avec"
    tir = json.loads((d / "tirages.json").read_text(encoding="utf-8"))
    inj = [e for e in journal(d) if "injection" in e][0]["injection"]
    assert inj["id"] == "salon-1" and inj["pseudonyme"] == tir["pseudonyme_tiers"] and inj["lettre"] == "tiers"
    cycle1 = [p for _, p in avec.invites if phase(p) == "cycle"]
    assert len(cycle1) == 5 and all(f"[salon-1] salon, {tir['pseudonyme_tiers']}, cycle 1" in p for p in cycle1)
    assert mod.verifier_essaim(v, d) == []
    # artefacts : fichier non scellé refusé ; reprise avec un autre fichier refusée
    g = tmp_path / "non-scelle.md"
    g.write_text(texte, encoding="utf-8")
    assert lancer(mod, v, tmp_path, cfg, Faux(v), nom="x", extra=("--erreurs-plantees", str(g))) == v.CODE_USAGE
    assert lancer(mod, v, tmp_path, cfg, Faux(v), nom="sans", extra=("--erreurs-plantees", str(f))) == v.CODE_USAGE


def test_finale_ne_voit_pas_les_autres(es, tmp_path):
    mod, v = es
    faux = Faux(v)
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=2), faux) == 0
    finales = [(i, p) for i, (_, p) in enumerate(faux.invites) if phase(p) == "finale"]
    assert len(finales) == 5
    for i, p in finales:
        assert "FINALE" not in p  # aucune réponse finale, même antérieure, dans une invite
    assert all("FINALE" not in p for _, p in faux.invites)


def test_sorties_mal_balisees(es, tmp_path):
    mod, v = es
    fait = []
    mal = ("Préambule hors section.\n=== SALON ===\nTitre : ouvert\njamais fermé\n"
           "=== INCONNU ===\n=== FIN REVUE ===\n"
           "=== SALON ===\nTitre : trop long\n" + "mot " * 200 + "\n=== FIN SALON ===\n"
           "=== SALON ===\nTitre : bon\nUn message correct.\n=== FIN SALON ===\n"
           "=== ERRATUM salon-99 ===\nsur rien\n=== FIN ERRATUM ===\n"
           "=== OUVRIR ===\nprepub-77, salon-1\n=== FIN OUVRIR ===\n"
           "=== PREPUBLICATION ===\nTitre : sans fin\ntexte\nFIN-DE-CELLULE")

    def special(n, m, prompt):
        if phase(prompt) == "cycle" and not fait:
            fait.append(n)
            return mal
        return None

    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=1), Faux(v, special=special)) == 0
    d = tmp_path / "essaim"
    p = sorted(mod.publications(v, d).values(), key=lambda p: p["rang"])[0]
    assert [e["titre"] for e in p["elements"]] == ["bon"]  # rien d'inventé : un seul élément publiable
    anomalies = " | ".join(a["anomalie"] for a in p["anomalies_balisage"])
    for attendu in ("SALON non fermée", "balise inconnue INCONNU", "fin de REVUE sans ouverture",
                    "PREPUBLICATION non fermée", "texte hors section"):
        assert attendu in anomalies
    motifs = sorted(r["motif"] for r in p["refuses"])
    assert motifs == ["204 mots > 150", "erratum sur un texte qui n'est pas le sien"]
    assert [o["id"] for o in p["ouvrir_refuses"]] == ["prepub-77"] and p["ouvrir"] == ["salon-1"]  # inconnu refusé
    assert mod.verifier_essaim(v, d) == []


def test_ouvertures_donnees_au_cycle_suivant(es, tmp_path):
    mod, v = es
    faux = Faux(v)
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=2), faux) == 0
    d = tmp_path / "essaim"
    pubs = sorted(mod.publications(v, d).values(), key=lambda p: p["rang"])
    for p in pubs:
        if p["cycle"] == 1 and p["ouvrir"]:
            suivante = mod.publications(v, d)[v.id_cellule("W1-C02", p["lettre"])]
            lec = [e for e in journal(d) if e.get("lecture") == v.id_cellule("W1-C02", p["lettre"])][0]
            assert {x["id"] for x in lec["textes"] if x["genre"] == "TEXTE"} == set(p["ouvrir"]) and suivante


def test_devis_sans_reseau(es, tmp_path, capsys):
    mod, v = es
    cfg = config(tmp_path, enveloppe_usd=None)
    q = tmp_path / "q.md"
    q.write_text(QUESTION, encoding="utf-8")
    assert mod.principal(["devis", "--configuration", str(cfg), "--question", str(q), "--enveloppe-usd", "15"], v=v) == 0
    sortie = capsys.readouterr().out
    assert "TOTAL" in sortie and "part par agent 0.7500" in sortie and v.TRANSPORT_COMPTE.appels == []


def test_enveloppe_du_dossier_isole(es, tmp_path, capsys):
    mod, v = es
    v.fixer_composition(["fable", "opus", "argon", "astra", "carbon"])
    d = tmp_path / "isole"
    v.sceller_composition(d)
    for t in v.ORDRE_ETAGE[3]:
        for l in v.LETTRES:
            cid = v.id_cellule(t, l)
            v.ecrire_neuf(v.chemin_cellule(d, cid), "texte")
            v.ajouter_journal(d, {"cellule": cid, "essai": 1, "statut": "OK", "espece": v.MODELES[l]["espece"],
                                  "cout_usd": 0.5})
    v.ajouter_journal(d, {"cellule": v.id_cellule("E3-T2", "A"), "essai": 2, "statut": "VIDE", "espece": "fable",
                          "cout_usd": 0.25})
    assert mod.principal(["enveloppe", str(d)], v=v) == 0
    assert "enveloppe_usd = 7.7500" in capsys.readouterr().out
    (d / "cellules" / f"{v.id_cellule('E3-T3', 'B')}.md").chmod(0o644)
    (d / "cellules" / f"{v.id_cellule('E3-T3', 'B')}.md").unlink()  # artefact : dossier incomplet
    assert mod.principal(["enveloppe", str(d)], v=v) == v.CODE_USAGE
    assert "incomplet" in capsys.readouterr().out


def test_bilan_et_verifier(es, tmp_path, capsys):
    mod, v = es
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=2), Faux(v)) == 0
    d = tmp_path / "essaim"
    capsys.readouterr()
    assert mod.principal(["bilan", str(d)], v=v) == 0
    sortie = capsys.readouterr().out
    lignes = [l for l in sortie.splitlines() if re.match(r"\| [A-E] \| \w+ \| \w+ \| temps", l)]
    assert len(lignes) == 15
    total = sum(float(l.split("|")[11]) for l in lignes)
    assert abs(total - v.depense(d)) < 1e-3
    assert mod.principal(["verifier", str(d)], v=v) == 0
    # artefacts : relecteurs réécrits au journal ; élément du tableau altéré
    texte = (d / "journal.jsonl").read_text(encoding="utf-8")
    pub = next(e for e in journal(d) if "publication" in e and e["elements"] and e["cycle"] == 1)
    pre = next(e for e in pub["elements"] if e["genre"] == "PREPUBLICATION")
    faux_rel = [pre["lettre"], pre["relecteurs"][0]]
    ligne = json.dumps(pub, ensure_ascii=False, sort_keys=True)
    pub2 = json.loads(ligne)
    next(e for e in pub2["elements"] if e["genre"] == "PREPUBLICATION")["relecteurs"] = faux_rel
    (d / "journal.jsonl").write_text(texte.replace(ligne, json.dumps(pub2, ensure_ascii=False, sort_keys=True)),
                                     encoding="utf-8")
    probl = mod.verifier_essaim(v, d)
    assert any("auteur compris" in x for x in probl) and any("différents du tirage" in x for x in probl)
    (d / "journal.jsonl").write_text(texte, encoding="utf-8")
    el = mod.elements(v, d)[0]
    (d / el["chemin"]).chmod(0o644)
    (d / el["chemin"]).write_text("altéré", encoding="utf-8")
    assert any("altéré" in x or "empreinte" in x for x in mod.verifier_essaim(v, d))


def test_tirages_relus_et_controles(es, tmp_path):
    mod, v = es
    cfg = config(tmp_path, cycles=1)
    assert lancer(mod, v, tmp_path, cfg, Faux(v)) == 0
    d = tmp_path / "essaim"
    assert lancer(mod, v, tmp_path, cfg, Faux(v)) == 0  # sain : relus, rien à refaire
    chemin = d / "tirages.json"
    tir = json.loads(chemin.read_text(encoding="utf-8"))
    tir["ordre"] = list(reversed(tir["ordre"]))  # artefact : ordre réécrit, sceau refait
    texte = json.dumps(tir, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    for p in (chemin, Path(str(chemin) + ".sha256")):
        p.chmod(0o644)
    chemin.write_text(texte, encoding="utf-8")
    Path(str(chemin) + ".sha256").write_text(f"{v.empreinte(texte)}  tirages.json\n", encoding="utf-8")
    assert lancer(mod, v, tmp_path, cfg, Faux(v)) == v.CODE_USAGE
    assert any("tirages" in x for x in mod.verifier_essaim(v, d))
