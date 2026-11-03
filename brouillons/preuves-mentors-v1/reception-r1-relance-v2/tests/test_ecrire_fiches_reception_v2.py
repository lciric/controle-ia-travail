"""Essais R5 du script `ecrire_fiches_reception_v2.py` (réception de la relance de R1 sur la table v3).

Mode « avant la récupération » : sur un dépôt git jetable (dossier temporaire de pytest, hors du dépôt de travail) où
sont copiés à l'octet, par `git show`, les vrais textes scellés (addendum v3, configuration v5, table v3 `ead8a668…`,
parent, code, nos analyses et nos pièces citées) : cas sain, puis un artefact par garde neuve.

Mode « après le versement » : sur un arbre synthétique aux formats du fournisseur (compagnons ; corps
`{"run_id", "manifeste_sha256", "resultat"}` ; manifeste à la clé `preenregistrement` et à la vraie configuration v5),
avec les attendus réels écrits par le mode « avant », dans une fiche scellée ici. Les `.npz` sont des octets
quelconques (le script ne les ouvre jamais) ; les empreintes des juges du bloc d'attendus sont remplacées par celles
des octets synthétiques (les vraies, `10838eea…` et `1ebbeff8…`, ne se fabriquent pas) ; le commit attendu est le vrai
commit de scellement. Les clés interdites (valeurs observées de P-R5, lectures de l'instrument) portent des
sentinelles qu'aucune sortie ne doit contenir.

Les fiches JSON écrites sont validées par les lecteurs des deux analyses (`entrees_v1.lire_fiche`,
`entrees_v3.lire_fiche_v3`, identiques aux commits cités a8b7fdb2 et 326601cf). Variable `SCRIPT_RECEPTION_V2` : chemin
d'un autre script à éprouver (banc de mutations, `banc_mutations_v2.py`)."""
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

sys.dont_write_bytecode = True
ICI = Path(__file__).resolve().parent
SCRIPT = Path(os.environ.get("SCRIPT_RECEPTION_V2") or ICI.parent / "ecrire_fiches_reception_v2.py").resolve()
DEPOT = ICI.parents[3]
SCELLEMENT = "139a81d37fbd2255aff8d27698f84b47b9433221"
REJEU = "20261103-120000-r1-rejeu-reel"
J3, J8 = "20261102-004328-r2-juge3b-reel", "20261102-005048-r2-juge8b-reel"
COMMIT_VERSEMENT = "a" * 40
ENV = {**os.environ, "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull, "GIT_TERMINAL_PROMPT": "0",
       "PYTHONDONTWRITEBYTECODE": "1"}
# sentinelles : valeurs des clés interdites (aucune ne doit sortir) ; nombres longs et réels, introuvables par hasard
SENTINELLES = {"fideles": 713579246, "notees": 824680135, "fideles_parmi_contextes_conformes": 935791357,
               "notees_contextes_conformes": 146802468, "egalite_exacte": 257913579, "ecart_max": 0.0314159265358,
               "ecart_mediane": 0.000271828182846, "part_fideles_parmi_notees": 0.86420975318642,
               "activations_identiques_au_bit": 368024680, "ecart_echantillon": 0.00141421356237,
               "ecart_negatif": 0.173205080756887, "hors_tolerance": 479135791}


def module():
    spec = importlib.util.spec_from_file_location("ecrire_fiches_reception_v2_essai", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M = module()


def git(d: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(d), *args], capture_output=True, env=ENV)
    assert r.returncode == 0, f"git {args} : {r.stderr.decode()}"
    return r.stdout.decode("utf-8", "replace")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def canon(config: dict) -> str:
    return hashlib.sha256(json.dumps(config, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def poser(p: Path, contenu) -> str:
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(contenu, (dict, list)):
        contenu = json.dumps(contenu, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if isinstance(contenu, str):
        p.write_text(contenu, encoding="utf-8")
    else:
        p.write_bytes(contenu)
    h = sha(p)
    Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


# ------------------------------------------------------------------ mode « avant la récupération »
@pytest.fixture(scope="session")
def pieces_reelles() -> dict:
    """Les vrais textes scellés et leurs compagnons, lus dans le dépôt de travail par `git show` (lecture seule)."""
    refs = {"scellement": SCELLEMENT, "principale": M.COMMIT_PRINCIPALE, "secondaire": M.COMMIT_SECONDAIRE, "tete": "HEAD"}
    out = {}
    for _, (ref, chemin, _, avec_compagnon, _) in M.PIECES.items():
        r = subprocess.run(["git", "-C", str(DEPOT), "show", f"{refs[ref]}:{chemin}"], capture_output=True, env=ENV)
        assert r.returncode == 0, f"pièce scellée {chemin} introuvable à {refs[ref]} (récupérer prep/r1-relance-v3) : R11"
        out[chemin] = r.stdout
        if avec_compagnon:
            out[chemin + ".sha256"] = subprocess.run(["git", "-C", str(DEPOT), "show", f"{refs[ref]}:{chemin}.sha256"],
                                                     capture_output=True, env=ENV, check=True).stdout
    return out


def resceller(contenu: dict, chemin: str) -> None:
    contenu[chemin + ".sha256"] = f"{hashlib.sha256(contenu[chemin]).hexdigest()}  {Path(chemin).name}\n".encode()


def depot_jetable(base: Path, pieces: dict, alterer=None) -> tuple:
    d = base / "depot"
    d.mkdir()
    git(d, "init", "-q")
    contenu = dict(pieces)
    if alterer:
        alterer(contenu)
    for chemin, b in contenu.items():
        p = d / chemin
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b)
    git(d, "add", "-A")
    git(d, "-c", "user.name=essai", "-c", "user.email=essai@invalid", "-c", "commit.gpgsign=false", "commit", "-qm", "copie")
    return d, git(d, "rev-parse", "HEAD").strip()


def lancer_avant(d: Path, commit: str, sortie: Path, *extra):
    return subprocess.run([sys.executable, "-I", str(SCRIPT), "avant-recuperation", "--depot", str(d),
                           "--commit-scellement", commit, "--commit-principale", commit, "--commit-secondaire", commit,
                           "--ref-tete", commit, "--sortie", str(sortie), "--qui", "essai", *extra],
                          capture_output=True, text=True, env=ENV)


def bloc(texte: str) -> dict:
    return json.loads(texte.split(M.DEBUT_BLOC, 1)[1].split(M.FIN_BLOC, 1)[0].strip()[len("```json"):-3])


GARDES_AVANT = ["recuperation", "config-table", "canonique", "table", "ligne-104", "attentes-texte", "piece", "compagnon"]


@pytest.fixture(scope="session")
def fiche_avant(tmp_path_factory, pieces_reelles) -> dict:
    base = tmp_path_factory.mktemp("avant")
    d, c = depot_jetable(base, pieces_reelles)
    sortie = base / "fiche.md"
    r = lancer_avant(d, c, sortie)
    assert r.returncode == 0, r.stderr
    return {"texte": sortie.read_text(encoding="utf-8"), "stdout": r.stdout, "commit": c, "chemin": sortie}


def test_avant_cas_sain_fiche_ecrite_attendus_reels(fiche_avant):
    texte, att = fiche_avant["texte"], bloc(fiche_avant["texte"])
    assert f"gardes passées : {', '.join(GARDES_AVANT)}" in fiche_avant["stdout"]
    assert f"**Gardes passées par le script** : {', '.join(GARDES_AVANT)}." in texte
    assert "aucune `calcul/…`" in texte and "Moment du scellement : avant toute récupération" in texte
    m, r = att["manifeste"], att["resultat"]
    assert att["format"] == "attendus-reception-r1-relance-v3-v1" and m["commit"] == fiche_avant["commit"]
    assert m["preenregistrement"] == {"chemin": "prereg/R1-addendum-relance-v3.md",
                                      "sha256": "88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4"}
    assert m["commande"] == "python -m controle_ia.runs_nuit.rejeu_activations_v3" and m["decisif"] is True
    assert m["config_sha256"] == "1cfb7fba9518ff81484153e0e9cc6dd974941b7d985775f026e61a80687627d4"
    assert m["table_tokenisation_sha256"] == r["tokenisation.table_sha256"] == \
        "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423"
    assert r["tokenisation.addendum"] == "prereg/R1-addendum-relance-v2.md" and m["entropie"] == M.ENTROPIE
    c = r["comptes"]
    assert (c["empreintes_p3.episodes"], c["empreintes_p3.trajectoires_identiques"], c["fidelite_toutes.actions"],
            c["fidelite_toutes.conformes_longueur"], c["fidelite_toutes.contextes_conformes"],
            c["tokenisation.trajectoires_identiques_base"], c["tokenisation.signales"],
            c["tokenisation.corrections_verifiees_au_chargement"]) == (240, 151, 2400, 2236, 1782, 129, 22, 22)
    assert c["tokenisation.par_methode_resolution"] == {"v1": 15, "v2": 3, "identifiants": 4, "aucune": 218}
    assert {k: v for k, v in c["tokenisation.corrections_par_methode"].items() if v} == \
        {"fins": 1, "une_paire": 12, "deux_paires": 2, "trois_paires": 1, "fenetre": 2, "identifiants": 4}
    assert c["tokenisation.episodes_non_resolus"] == [] and att["episodes_non_inversibles_declares"] == []
    assert att["juges"]["juge3b"]["sha256"].startswith("10838eea") and att["juges"]["juge8b"]["sha256"].startswith("1ebbeff8")
    assert att["N_A"].startswith("sans objet") and set(att["interdits"]) == set(M.INTERDITS)


def _texte(contenu: dict, chemin: str, avant: str, apres: str) -> None:
    t = contenu[chemin].decode("utf-8")
    assert t.count(avant) >= 1
    contenu[chemin] = t.replace(avant, apres, 1).encode("utf-8")


def _json(contenu: dict, chemin: str, f) -> None:
    d = json.loads(contenu[chemin])
    f(d)
    contenu[chemin] = json.dumps(d, indent=2, ensure_ascii=False).encode("utf-8")


ADD, CFG, TAB, MAN = M.ADDENDUM_V3, M.CONFIG_V5, M.TABLE_V3, "src/controle_ia/manifeste.py"
PRINC = "prereg/analyse-principale-r1-r2-v1.md"
ARTEFACTS_AVANT = [
    ("recuperation", "calcul", None, "update-ref refs/remotes/origin/calcul/r1-r2-reel-v1"),
    ("recuperation", "donnees", None, "update-ref refs/remotes/origin/donnees-x"),
    ("config-table", "table_tokenisation_sha256", lambda c: (_json(c, CFG, lambda d: d.update(
        table_tokenisation_sha256="5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2")), resceller(c, CFG)), None),
    ("canonique", "empreinte canonique", lambda c: (_json(c, CFG, lambda d: d.update(tolerance_fidelite=0.03)),
                                                    resceller(c, CFG)), None),
    ("table", "version 2", lambda c: (_json(c, TAB, lambda d: d.update(version=2)), resceller(c, TAB)), None),
    ("table", "non_resolu", lambda c: (_json(c, TAB, lambda d: d["comptes"].update(non_resolu=1)), resceller(c, TAB)), None),
    ("ligne-104", "l. 104", lambda c: _texte(c, MAN, '"preenregistrement": prereg_info,', '"addendum": prereg_info,'), None),
    ("attentes-texte", "`signales` = 22", lambda c: (_texte(c, ADD, "`signales` = 22,", "`signales` = 21,"),
                                                    resceller(c, ADD)), None),
    ("attentes-texte", "`addendum` =", lambda c: (_texte(c, ADD, "`addendum` =\n`prereg/R1-addendum-relance-v2.md` (E16)",
                                                         "`addendum` =\n`prereg/R1-addendum-relance-v3.md` (E16)"),
                                                  resceller(c, ADD)), None),
    ("piece", "principale", lambda c: (c.__setitem__(PRINC, c[PRINC] + b"\n"), resceller(c, PRINC)), None),
    ("compagnon", "sceau faux", lambda c: c.__setitem__(ADD + ".sha256", f"{'0' * 64}  {Path(ADD).name}\n".encode()), None),
]


@pytest.mark.parametrize("garde, fragment, alterer, refs", ARTEFACTS_AVANT,
                         ids=[f"{a[0]}-{i}" for i, a in enumerate(ARTEFACTS_AVANT)])
def test_avant_artefact_arrete_sans_fiche(tmp_path, pieces_reelles, garde, fragment, alterer, refs):
    d, c = depot_jetable(tmp_path, pieces_reelles, alterer)
    if refs:
        git(d, *refs.split(), "HEAD")
    sortie = tmp_path / "fiche.md"
    r = lancer_avant(d, c, sortie)
    assert r.returncode == 2 and f"ARRÊT [{garde}]" in r.stderr and fragment in r.stderr, r.stderr
    assert not sortie.exists()


def test_avant_commit_absent_et_fiche_existante(tmp_path, pieces_reelles):
    d, c = depot_jetable(tmp_path, pieces_reelles)
    sortie = tmp_path / "fiche.md"
    r = lancer_avant(d, "f" * 40, sortie)
    assert r.returncode == 2 and "ARRÊT [piece]" in r.stderr and "R11" in r.stderr and not sortie.exists()
    sortie.write_text("déjà là", encoding="utf-8")
    r = lancer_avant(d, c, sortie)
    assert r.returncode == 2 and "ARRÊT [R12]" in r.stderr and sortie.read_text(encoding="utf-8") == "déjà là"


# ------------------------------------------------------------------ mode « après le versement »
@pytest.fixture(scope="session")
def config_v5(pieces_reelles) -> dict:
    return json.loads(pieces_reelles[CFG])


@pytest.fixture(scope="session")
def att_base(fiche_avant) -> dict:
    return bloc(fiche_avant["texte"])


def resultat_sain(att: dict, fichiers: dict) -> dict:
    c, S = att["resultat"]["comptes"], SENTINELLES
    return {
        "fichiers_au_dessus_de_95_mo": {}, "verdict_fidelite": "conforme", "regle_repli_appliquee": False,
        "lecture": "principale", "textes_sha256": "ba05fa13" + "0" * 56, "fichiers": fichiers,
        "identite_sha256": "1f25adbd" + "0" * 56, "regle_empan": "empan noté par P3", "contexte": "forçage par l'enseignant",
        "couches": [7, 15, 23], "agregats": {"maximum": "production (harnais)"},
        "fidelite_echantillon": {"rangs": [3], "ecarts": [S["ecart_echantillon"]], "conformes": [True], "fautes": [],
                                 "tolerance": 0.02, "lecture": "conforme"},
        "controle_negatif": {"rangs": [3], "ecarts_consigne_fausse": [S["ecart_negatif"]], "hors_tolerance": S["hors_tolerance"],
                             "minimum": 18, "tolerance": 0.02, "lecture": "discriminant"},
        "empreintes_p3": {"episodes": c["empreintes_p3.episodes"], "trajectoires_identiques": c["empreintes_p3.trajectoires_identiques"],
                          "activations_identiques_au_bit": S["activations_identiques_au_bit"]},
        "fidelite_toutes": {"notees": S["notees"], "fideles": S["fideles"], "conformes_longueur": c["fidelite_toutes.conformes_longueur"],
                            "contextes_conformes": c["fidelite_toutes.contextes_conformes"], "actions": c["fidelite_toutes.actions"],
                            "fideles_parmi_contextes_conformes": S["fideles_parmi_contextes_conformes"],
                            "notees_contextes_conformes": S["notees_contextes_conformes"],
                            "egalite_exacte": S["egalite_exacte"], "ecart_max": S["ecart_max"], "ecart_mediane": S["ecart_mediane"]},
        "tokenisation": {"addendum": att["resultat"]["tokenisation.addendum"], "version_table": c["tokenisation.version_table"],
                         "table_sha256": att["resultat"]["tokenisation.table_sha256"],
                         "corrections_verifiees_au_chargement": c["tokenisation.corrections_verifiees_au_chargement"],
                         "trajectoires_identiques_base": c["tokenisation.trajectoires_identiques_base"],
                         "signales": c["tokenisation.signales"],
                         "corrections_par_methode": dict(c["tokenisation.corrections_par_methode"]),
                         "methodes_resolution": {"temoin/x/e0": {"methode_resolution": "aucune", "methode_table": None}},
                         "par_methode_resolution": dict(c["tokenisation.par_methode_resolution"]),
                         "episodes_non_resolus": [], "actions_non_resolues": 0, "fideles_parmi_non_resolues": 0,
                         "seuil_non_conformes": c["tokenisation.seuil_non_conformes"],
                         "part_fideles_parmi_notees": S["part_fideles_parmi_notees"], "p_r5_au_moins_90_pour_cent": True},
        "sondes_fidelite": ["G-7"], "sondes_legeres_sha256": "c" * 64, "reglages": {}, "duree_s": 812.4,
        "modele": {"modele": "meta-llama/Llama-3.1-8B-Instruct", "revision": "0e9e39f2"}, "empreintes_modele": {}}


def arbre_verse(racine: Path, att: dict, config: dict, rejeu=REJEU, arret=False, juges=("juge3b", "juge8b"),
                man=None, corps_patch=None) -> dict:
    m = {"run_id": rejeu, "cree_le": "2026-11-03T06:00:00+00:00", "commit": att["manifeste"]["commit"], "depot_propre": True,
         "decisif": True, "preenregistrement": dict(att["manifeste"]["preenregistrement"]), "config": copy.deepcopy(config),
         "config_sha256": canon(config), "versions": {"python": "3.11.2", "torch": "2.14.1"},
         "graines": {"fidelite": {"entropie": M.ENTROPIE, "spawn_key": ["1"], "etat_controle": [1, 2]},
                     "modele-jouet-inutilise": {"entropie": M.ENTROPIE, "spawn_key": ["2"], "etat_controle": [3, 4]}},
         "commande": att["manifeste"]["commande"], "reserves": []}
    if man:
        man(m)
    sha_m = poser(racine / "runs" / rejeu / "manifeste.json", m)
    if arret:
        corps = {"run_id": rejeu, "manifeste_sha256": sha_m, "resultat": {
            "etape": "vérification de la table", "motif": "GardeArret: table", "verdict_fidelite": "echec", "duree_s": 3.0,
            "partiel": {"controle_negatif": {"lecture": "non discriminant", "hors_tolerance": SENTINELLES["hors_tolerance"]},
                        "fidelite_echantillon": {"ecarts": [SENTINELLES["ecart_echantillon"]]}}}}
        nom = "arret.json"
    else:
        fichiers = {n: poser(racine / "donnees" / rejeu / n, os.urandom(2048) + n.encode())
                    for n in att["fichiers_rejeu"].values()}
        corps = {"run_id": rejeu, "manifeste_sha256": sha_m, "resultat": resultat_sain(att, fichiers)}
        nom = "rejeu-activations.json"
    if corps_patch:
        corps_patch(corps)
    poser(racine / "diag" / rejeu / nom, corps)
    shas = {}
    for cle in juges:
        run, fichier = att["juges"][cle]["run"], att["juges"][cle]["fichier"]
        sm = poser(racine / "runs" / run / "manifeste.json", {"run_id": run, "config": {"mode": "reel"}})
        shas[cle] = poser(racine / "donnees" / run / fichier, os.urandom(1024) + fichier.encode())
        poser(racine / "diag" / run / "juge-actions.json", {"run_id": run, "manifeste_sha256": sm, "resultat": {
            "fichier": fichier, "sha256": shas[cle], "invite_sha256": "44d48a28" + "0" * 56,
            "contexte": "énoncé de la tâche et action, sans consigne privée", "juge": {"modele": "Llama-3.2-3B-Instruct"}}})
    return shas


def fiche_scellee(dossier: Path, att: dict, sceller=True, avec_bloc=True, alterer_apres=False) -> tuple:
    corps = f"{M.DEBUT_BLOC}\n```json\n{json.dumps(att, indent=1, ensure_ascii=False, sort_keys=True)}\n```\n{M.FIN_BLOC}\n"
    p = dossier / "fiche-reception-essai-v1.md"
    p.write_text("# Fiche de réception (essai)\n\n" + (corps if avec_bloc else "sans bloc\n"), encoding="utf-8")
    h = sha(p)
    if sceller:
        Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    if alterer_apres:
        p.write_text(p.read_text(encoding="utf-8") + "ajout après scellement\n", encoding="utf-8")
    return p, h


def preparer(tmp_path, att_base, config_v5, rejeu=REJEU, arret=False, man=None, corps_patch=None, att_patch=None,
             juges=("juge3b", "juge8b"), **fiche_kw) -> tuple:
    racine = tmp_path / "arbre"
    racine.mkdir()
    att = copy.deepcopy(att_base)
    att["manifeste"]["commit"] = SCELLEMENT
    for cle, h in arbre_verse(racine, att, config_v5, rejeu, arret, juges, man, corps_patch).items():
        att["juges"][cle]["sha256"] = h
    if att_patch:
        att_patch(att)
    fiche, h = fiche_scellee(tmp_path, att, **fiche_kw)
    return racine, fiche, h


def lancer_apres(racine, fiche, h, *extra, rejeu=REJEU, juge3b=J3, juge8b=J8):
    return subprocess.run([sys.executable, "-I", str(SCRIPT), "apres-versement", "--racine", str(racine),
                           "--fiche-reception", str(fiche), "--fiche-reception-sha256", h, "--rejeu", rejeu,
                           "--juge3b", juge3b, "--juge8b", juge8b, "--qui", "essai", "--commit-versement",
                           COMMIT_VERSEMENT, *extra], capture_output=True, text=True, env=ENV)


FP, FS = "prereg/fiche-reception-principale-r1-r2-v1.json", "prereg/fiche-reception-blanche-noire-v3.json"
GARDES_APRES = ["fiche", "attendus", "nom-rejeu", "e21", "rattachement", "texte", "commande", "decisif", "configuration",
                "commit", "entropie", "table-comparee", "provenance", "comptes", "juges", "P-R5"]


def lecteurs(racine: Path) -> tuple:
    """Les lecteurs des deux analyses acceptent la forme des fiches (aucune donnée lue : `scellee=False`)."""
    from controle_ia.analyse_principale_r1_r2.entrees_v1 import lire_fiche
    from controle_ia.analyse_blanche_noire.entrees_v3 import lire_fiche_v3
    return lire_fiche(racine, FP, scellee=False)[0], lire_fiche_v3(racine, FS, scellee=False)[0]


def sorties(r, racine: Path) -> str:
    return r.stdout + r.stderr + "".join((racine / f).read_text(encoding="utf-8") for f in (FP, FS) if (racine / f).exists())


def test_apres_cas_sain_deux_fiches_validees_par_les_lecteurs(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 0, r.stderr
    fp, fs = lecteurs(racine)
    red = fp["redaction"]
    assert red["controles"] == GARDES_APRES and fs["redaction"]["controles"] == GARDES_APRES
    assert f"gardes passées : {', '.join(GARDES_APRES)}" in r.stdout
    assert fp["R1"]["moyenne"]["chemin"] == f"donnees/{REJEU}/activations-p3-rejeu-v1.npz"
    assert fp["R1"]["resultat"]["chemin"] == f"diag/{REJEU}/rejeu-activations.json" and fp["motif_R1"] is None
    assert fs["R1"]["manifeste"] == fp["R1"]["resultat"] and fs["R4"] is None and fs["redaction"]["manifeste_rejeu"]
    assert fs["R1"]["pointeurs"]["regle_repli"] == ["resultat", "regle_repli_appliquee"]
    assert red["addendum_v3"]["chemin"] == "prereg/R1-addendum-relance-v3.md" and red["addendum_v3"]["commit_scellement"] == SCELLEMENT
    assert red["provenance_table"]["valeur"] == "prereg/R1-addendum-relance-v2.md" and "addendum_v2" not in red
    assert red["fiche_reception"]["sha256"] == h and red["e21"] == {"reprise": False, "branche_source": "calcul/r1-relance-v3-reel-v1"}
    assert red["episodes_non_inversibles_declares"] == [] and red["N_A"].startswith("sans objet")
    assert set(red["cles_lues"]) == {".".join(c) for c in M.CHEMINS_LUS} and "valeurs_lues" not in red
    # analyse secondaire scellée, l. 24 : chemins, empreintes, pointeurs et motifs seulement ; aucun nombre
    assert M.nombres_dans(fp) == [] and M.nombres_dans(fs) == []
    # 3 manifestes + rejeu (3 npz + résultat) + 2 juges × (npz + résultat) = 11 fichiers confrontés à leur compagnon
    assert red["aucun_npz_ouvert"] is True and len(red["compagnons_verifies"]) == 11
    assert all(p.endswith(".json") for p in red["ce_qui_a_ete_ouvert"]) and len(red["ce_qui_a_ete_ouvert"]) == 4
    assert "sans consigne privée" in r.stdout


def test_apres_aucune_valeur_P_R5_ni_lecture_de_l_instrument_ne_sort(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 0, r.stderr
    texte = sorties(r, racine)
    fuites = [k for k, v in SENTINELLES.items() if json.dumps(v) in texte]
    assert not fuites, fuites
    assert not M.cles_interdites(json.loads((racine / FP).read_text(encoding="utf-8")))


def test_garde_P_R5_refuse_une_sortie_qui_porterait_une_cle_interdite():
    ctl = M.Controles()
    M.exiger_sans_fuite(ctl, {"redaction": {"cles_lues": ["resultat.tokenisation.table_sha256"], "aucun_npz_ouvert": True}})
    assert ctl.passees == ["P-R5"]
    for fuite in ({"a": {"fideles": "x"}}, {"a": [{"p_r5_au_moins_90_pour_cent": True}]}, {"controle_negatif": {}},
                  {"redaction": {"compte": 2236}}, {"redaction": {"part": [0.93]}}):
        with pytest.raises(M.Arret) as e:
            M.exiger_sans_fuite(M.Controles(), {"redaction": fuite})
        assert e.value.garde == "P-R5"


def test_filtre_ne_garde_que_les_chemins_nommes():
    doc = {"run_id": "r", "manifeste_sha256": "m", "resultat": {"a": 1, "b": {"c": 2, "fideles": 3}}}
    assert M.filtrer(doc, (("run_id",), ("resultat", "b", "c"))) == {"run_id": "r", "resultat.b.c": 2}
    with pytest.raises(M.Arret) as e:
        M.filtrer(doc, (("resultat", "absente"),))
    assert e.value.garde == "forme"


def _maj(chemin, valeur):
    def f(d):
        x = d
        for k in chemin[:-1]:
            x = x[k]
        x[chemin[-1]] = valeur
    return f


V2_SHA = "9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059"
T2_SHA = "5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2"


def _config_autre_table(m):
    m["config"]["table_tokenisation_sha256"] = T2_SHA
    m["config_sha256"] = canon(m["config"])


# (garde, fragment du message, arguments de `preparer`, arguments de `lancer_apres`)
ARTEFACTS_APRES = [
    ("fiche", "absente (R11", {}, {"fiche_absente": True}),
    ("fiche", "non scellée", {"sceller": False}, {}),
    ("fiche", "(modifiée)", {"alterer_apres": True}, {}),
    ("fiche", "envoyée au canal", {}, {"h": "f" * 64}),
    ("attendus", "bloc d'attendus", {"avec_bloc": False}, {}),
    ("attendus", "autre format", {"att_patch": _maj(["format"], "attendus-autre-v9")}, {}),
    ("nom-rejeu", "première course", {"rejeu": "20261102-002114-r1-rejeu-reel"}, {"rejeu": "20261102-002114-r1-rejeu-reel"}),
    ("nom-rejeu", "r1-rejeu-reel", {"rejeu": "20261103-120000-r1-rejeu-jouet"}, {"rejeu": "20261103-120000-r1-rejeu-jouet"}),
    ("e21", "égal au run lu", {}, {"extra": ["--course-arretee-e21", REJEU, "--arret-e21-sha256", "absent",
                                             "--annonce-e21", "n° 1", "--branche-source", "calcul/r1-relance-v3-reel-v2"]}),
    ("e21", "sans le message d'annonce", {}, {"extra": ["--course-arretee-e21", "20261103-100000-r1-rejeu-reel",
                                                         "--arret-e21-sha256", "absent",
                                                         "--branche-source", "calcul/r1-relance-v3-reel-v2"]}),
    ("e21", "64 hex", {}, {"extra": ["--course-arretee-e21", "20261103-100000-r1-rejeu-reel", "--arret-e21-sha256",
                                      "pas-une-empreinte", "--annonce-e21", "n° 1",
                                      "--branche-source", "calcul/r1-relance-v3-reel-v2"]}),
    ("e21", "branche source", {}, {"extra": ["--course-arretee-e21", "20261103-100000-r1-rejeu-reel",
                                              "--arret-e21-sha256", "absent", "--annonce-e21", "n° 1"]}),
    ("e21", "sans reprise E21", {}, {"extra": ["--annonce-e21", "n° 1"]}),
    ("rattachement", "manifeste : run_id", {"man": _maj(["run_id"], "20261103-120001-r1-rejeu-reel")}, {}),
    ("rattachement", "≠ run et manifeste versés", {"corps_patch": _maj(["manifeste_sha256"], "0" * 64)}, {}),
    ("rattachement", "arret.json : run_id ou manifeste", {"arret": True, "corps_patch": _maj(["manifeste_sha256"], "0" * 64)},
     {}),
    ("texte", "addendum-relance-v2", {"man": _maj(["preenregistrement"], {"chemin": "prereg/R1-addendum-relance-v2.md",
                                                                          "sha256": V2_SHA})}, {}),
    ("texte", "texte qui gouverne", {"man": _maj(["preenregistrement", "sha256"], V2_SHA)}, {}),
    ("commande", "rejeu_activations_v1", {"man": _maj(["commande"], "python -m controle_ia.runs_nuit.rejeu_activations_v1")}, {}),
    ("decisif", "decisif = False", {"man": _maj(["decisif"], False)}, {}),
    ("configuration", "table citée par la configuration", {"man": _config_autre_table}, {}),
    ("configuration", "≠ attendue", {"man": _maj(["config_sha256"], "2" * 64)}, {}),
    ("configuration", "recalcul canonique", {"man": _maj(["config", "tolerance_fidelite"], 0.03)}, {}),
    ("commit", "commit de scellement lancé", {"man": _maj(["commit"], "04bc323a50cfd31c07a69fa4fa688e1a9d4522b3")}, {}),
    ("commit", "arbre non propre", {"man": _maj(["depot_propre"], False)}, {}),
    ("entropie", "entropie", {"man": _maj(["graines", "fidelite", "entropie"], "1")}, {}),
    ("table-comparee", "autre table", {"corps_patch": _maj(["resultat", "tokenisation", "table_sha256"], T2_SHA)}, {}),
    ("provenance", "E16", {"corps_patch": _maj(["resultat", "tokenisation", "addendum"], "prereg/R1-addendum-relance-v3.md")}, {}),
    ("comptes", "empreintes_p3.trajectoires_identiques = 147",
     {"corps_patch": _maj(["resultat", "empreintes_p3", "trajectoires_identiques"], 147)}, {}),
    ("comptes", "episodes_non_resolus", {"corps_patch": _maj(["resultat", "tokenisation", "episodes_non_resolus"],
                                                             ["honnete/2602.00987v1/e0"])}, {}),
    ("comptes", "par_methode_resolution", {"corps_patch": _maj(["resultat", "tokenisation", "par_methode_resolution", "v1"], 14)}, {}),
    ("juges", "empreinte citée par l'addendum v3", {"att_patch": _maj(["juges", "juge3b", "sha256"], "1" * 64)}, {}),
    ("juges", "run cité par l'addendum v3", {"att_patch": _maj(["juges", "juge8b", "run"], "20261102-005049-r2-juge8b-reel")}, {}),
]


@pytest.mark.parametrize("garde, fragment, prep, lanc", ARTEFACTS_APRES,
                         ids=[f"{a[0]}-{i}" for i, a in enumerate(ARTEFACTS_APRES)])
def test_apres_artefact_arrete_sans_fiche(tmp_path, att_base, config_v5, garde, fragment, prep, lanc):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5, **prep)
    if lanc.get("fiche_absente"):
        fiche = fiche.with_name("fiche-reception-jamais-ecrite-v1.md")
    r = lancer_apres(racine, fiche, lanc.get("h", h), *lanc.get("extra", []), rejeu=lanc.get("rejeu", REJEU))
    assert r.returncode == 2 and f"ARRÊT [{garde}]" in r.stderr and fragment in r.stderr, r.stderr
    assert not (racine / "prereg").exists()


def test_apres_reprise_e21_notee(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    r = lancer_apres(racine, fiche, h, "--course-arretee-e21", "20261103-100000-r1-rejeu-reel", "--arret-e21-sha256",
                     "b" * 64, "--annonce-e21", "n° 300 (empreinte 1234…)", "--branche-source", "calcul/r1-relance-v3-reel-v2")
    assert r.returncode == 0, r.stderr
    fp, _ = lecteurs(racine)
    assert fp["redaction"]["e21"] == {"reprise": True, "course_arretee": "20261103-100000-r1-rejeu-reel",
                                      "arret_json_sha256": "b" * 64, "annonce": "n° 300 (empreinte 1234…)",
                                      "branche_source": "calcul/r1-relance-v3-reel-v2", "lue": False}


def test_bout_en_bout_fiche_du_mode_avant_scellee_puis_lue(tmp_path, fiche_avant, config_v5):
    """La fiche écrite par le mode « avant » (attendus réels, commit du dépôt jetable), scellée, gouverne le mode
    « après » ; juges absents (motif fermé), puisque leurs vraies empreintes ne se fabriquent pas."""
    fiche = tmp_path / "fiche-reception-r1-relance-v3-v1.md"
    fiche.write_text(fiche_avant["texte"], encoding="utf-8")
    h = sha(fiche)
    Path(str(fiche) + ".sha256").write_text(f"{h}  {fiche.name}\n", encoding="utf-8")
    racine = tmp_path / "arbre"
    racine.mkdir()
    arbre_verse(racine, bloc(fiche_avant["texte"]), config_v5, juges=())
    r = lancer_apres(racine, fiche, h, "--motif-R2", "sorties_non_livrees", "--preuve-R2", "essai", juge3b="absent",
                     juge8b="absent")
    assert r.returncode == 0, r.stderr
    fp, fs = lecteurs(racine)
    assert fp["R2"] is None and fp["motif_R2"] == "sorties_non_livrees" and fs["R2"] is None
    assert fp["redaction"]["fiche_reception"]["sha256"] == h


# ------------------------------------------------------------------ gardes de la v1, portées (formats inchangés)
def test_v1_juge_8b_absent_motif_ferme(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5, juges=("juge3b",))
    r = lancer_apres(racine, fiche, h, juge8b="absent")
    assert r.returncode == 0, r.stderr
    fp, _ = lecteurs(racine)
    assert fp["R2"]["juge8b"] is None and fp["R2"]["motif_juge8b"] == "non_livre"


def test_v1_rejeu_arrete_motif_ferme_rien_d_interdit_ne_sort(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5, arret=True)
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 0, r.stderr
    fp, fs = lecteurs(racine)
    assert fp["R1"] is None and fp["motif_R1"] == "rejeu_en_echec" and fs["R1"] is None and fs["motif_R1"] == "rejeu_en_echec"
    assert fp["redaction"]["notes"][0]["arret"]["chemin"] == f"diag/{REJEU}/arret.json"
    assert "texte" in fp["redaction"]["controles"] and "comptes" not in fp["redaction"]["controles"]
    texte = sorties(r, racine)
    assert not [k for k, v in SENTINELLES.items() if json.dumps(v) in texte]


def test_v1_artefact_fichier_manquant(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    p = racine / "donnees" / REJEU / "activations-p3-rejeu-v1-maximum.npz"
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 2 and "ARRÊT [fichiers]" in r.stderr and "absent" in r.stderr
    assert not (racine / "prereg").exists()


def test_v1_artefact_nom_inattendu(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    poser(racine / "donnees" / REJEU / "activations-p3-rejeu-v2.npz", b"x")
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 2 and "inattendu" in r.stderr


def test_v1_artefact_empreinte_fausse(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    p = racine / "donnees" / J3 / "scores-juge3b-p3-v1.npz"
    p.write_bytes(p.read_bytes() + b"!")
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 2 and "≠ compagnon" in r.stderr


def test_v1_artefact_empreinte_declaree_par_le_fournisseur_differente(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5, corps_patch=_maj(
        ["resultat", "fichiers", "activations-p3-rejeu-v1.npz"], "0" * 64))
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 2 and "déclarée par le fournisseur" in r.stderr


def test_v1_artefact_resultat_et_arret_tous_deux_presents(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    poser(racine / "diag" / REJEU / "arret.json", {"resultat": {"verdict_fidelite": "echec"}})
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 2 and "exactement un" in r.stderr


def test_v1_fiches_existantes_jamais_ecrasees(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    assert lancer_apres(racine, fiche, h).returncode == 0
    avant = (sha(racine / FP), sha(racine / FS))
    r = lancer_apres(racine, fiche, h)
    assert r.returncode == 2 and "ARRÊT [R12]" in r.stderr and (sha(racine / FP), sha(racine / FS)) == avant
    (racine / FP).unlink()
    r = lancer_apres(racine, fiche, h)       # la secondaire existe : rien n'est écrit, pas même la principale
    assert r.returncode == 2 and "ARRÊT [R12]" in r.stderr and not (racine / FP).exists()


def test_v1_parametres_hors_de_forme(tmp_path, att_base, config_v5):
    racine, fiche, h = preparer(tmp_path, att_base, config_v5)
    r = subprocess.run([sys.executable, "-I", str(SCRIPT), "apres-versement", "--racine", str(racine), "--fiche-reception",
                        str(fiche), "--fiche-reception-sha256", h, "--rejeu", REJEU, "--juge3b", J3, "--juge8b", J8,
                        "--qui", "x", "--commit-versement", "abc"], capture_output=True, text=True, env=ENV)
    assert r.returncode == 2 and "hors de forme" in r.stderr
    r = lancer_apres(racine, fiche, h, rejeu="pas-un-run")
    assert r.returncode == 2 and "format AAAAMMJJ" in r.stderr
