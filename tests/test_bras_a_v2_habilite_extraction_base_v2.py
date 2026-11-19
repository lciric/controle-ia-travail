"""Essais de l'extraction des six conditions lues du lot décisif pour la base « mots et coût » (lot 13 du développeur
habilité du bras A) — v2. Données factices seulement ; aucun résultat d'expérience, aucun modèle chargé.

Fichier neuf (R12) : les essais de la v1 restent tels quels et éprouvent la v1. S'y ajoutent l'essai du contre-lecteur
sur le chemin d'écriture (recopié), l'essai du câblage de la garde de sortie dans l'extraction, et un artefact pour
chaque garde qui survivait à son retrait (contre-lecture `contre-lecture-lots-13-et-15-bras-a-v1.md`, 73d4c58e…).

Chaque garde a un cas sain et un artefact (R5). L'essai de bout en bout passe les sorties aux lecteurs d'entrée de la
base inscrite (`scripts/mots_et_cout_bras_a_v2.py`, à son empreinte), qui les acceptent.

Essais ciblés :
    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_extraction_base_v2.py
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import extraction_base_v2 as X
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
BENIN = "prediction-1.00"
NOMS_LUS = ("H", "controls-0.25", "controls-0.50", "controls-0.75", "controls-1.00", "identite")


def _charger(nom: str, chemin: Path):
    if nom in sys.modules:
        return sys.modules[nom]
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


@pytest.fixture(scope="module")
def base():
    """La pièce de la base inscrite, lue à son empreinte, et sa fabrique de textes factices."""
    chemin = RACINE / X.PIECE_DE_LA_BASE[0]
    assert hashlib.sha256(chemin.read_bytes()).hexdigest() == X.PIECE_DE_LA_BASE[1]
    mc = _charger("mots_et_cout_bras_a_v2_pour_extraction", chemin)
    fab = _charger("fabrique_factice_mots_et_cout_bras_a_v1_pour_extraction",
                   RACINE / "scripts" / "fabrique_factice_mots_et_cout_bras_a_v1.py")
    return mc, fab


def config_bras() -> dict:
    return {"note": "configuration FACTICE", "entropie": 20261119,
            "taches_verification": [f"tache-verification-factice-{k:02d}" for k in range(16)],
            "taches_fabrication": [f"tache-fabrication-factice-{k:02d}" for k in range(16)],
            "doses_fabrication": [0.25, 0.5, 0.75, 1.0], "proportions_temoin_benin": [1.0]}


def rejeu_factice(texte_action=None) -> dict:
    """Sortie factice de `rejouer` : sept conditions, 16 tâches, 8 épisodes, 10 actions ; la tâche est rendue entière
    (dictionnaire), comme le fait le lanceur."""
    rng = np.random.default_rng(np.random.SeedSequence(7))
    rejeu = {}
    for nom in NOMS_LUS + (BENIN,):
        episodes = []
        for t in config_bras()["taches_verification"]:
            for k in range(8):
                textes = [texte_action(rng) if texte_action else f"ACTION: ADD\nTITLE: t {nom} {t} {k} {p}\nCOST: 12"
                          for p in range(10)]
                actions = [[int(x) for x in rng.integers(0, 1000, size=3 + p)] for p in range(10)]
                episodes.append({"episode": f"verification/{t}/e{k}", "tache": {"identifiant": t, "questions": "q"},
                                 "k": k, "actions": actions, "textes": textes})
        rejeu[nom] = episodes
    return rejeu


@pytest.fixture(scope="module")
def sain():
    plan = X.plan_des_conditions(config_bras())
    rejeu = rejeu_factice()
    lignes, comptes = X.extraire(rejeu, plan)
    return plan, rejeu, lignes, comptes


# --- constantes liées à la base inscrite ---------------------------------------------------------------------------

def test_constantes_egales_a_celles_de_la_base_inscrite(base):
    mc, fab = base
    assert X.CLES_CONFIG == mc.CLES_CONFIG
    assert X.CHAMPS_ACTION == mc.CHAMPS_ACTION and X.CHAMPS_ACTION_PERMIS == mc.CHAMPS_ACTION_PERMIS
    assert X.EXTENSIONS_PERMISES == mc.EXTENSIONS_PERMISES and X.FRAGMENTS_INTERDITS == mc.FRAGMENTS_INTERDITS
    assert X.ROLES == mc.CONDITIONS_LUES
    assert (X.N_TACHES, X.N_EPISODES, X.T_PAS, X.N_ACTIONS) == (mc.N_TACHES, mc.N_EPISODES, mc.T_PAS, mc.N_ACTIONS)
    assert X.N_ACTIONS == 7680
    plan = X.plan_des_conditions(config_bras())
    assert plan["conditions"] == fab.NOMS and plan["temoin_benin"] == [fab.TEMOIN_BENIN]


# --- cas sain ------------------------------------------------------------------------------------------------------

def test_extraction_saine(sain):
    plan, rejeu, lignes, comptes = sain
    assert len(lignes) == 7680 and comptes["actions"] == 7680
    assert comptes["actions_par_condition"] == {n: 1280 for n in NOMS_LUS}
    assert comptes["episodes_du_temoin_benin_laisses_de_cote"] == {BENIN: 128}
    assert all(set(x) == set(X.CHAMPS_ACTION_PERMIS) for x in lignes)
    assert BENIN not in {x["condition"] for x in lignes}
    x = lignes[1280 + 10 * 8 * 3 + 10 * 5 + 7]                      # deuxième condition, tâche 3, épisode 5, pas 7
    ep = [e for e in rejeu["controls-0.25"] if e["tache"]["identifiant"].endswith("-03") and e["k"] == 5][0]
    assert (x["condition"], x["episode"], x["pas"]) == ("controls-0.25", 5, 7)
    assert x["texte"] == ep["textes"][7] and x["ids"] == ep["actions"][7] and x["jetons"] == len(ep["actions"][7])
    X.verifier_lignes(lignes, plan)


def test_extraction_ne_depend_pas_de_l_ordre_du_rejeu(sain):
    plan, rejeu, lignes, _ = sain
    autre = {nom: list(reversed(eps)) for nom, eps in reversed(list(rejeu.items()))}
    assert X.extraire(autre, plan)[0] == lignes


# --- artefacts de l'entrée -----------------------------------------------------------------------------------------

def test_episode_manquant_arrete(sain):
    plan, rejeu, _, _ = sain
    r = {**rejeu, "controls-0.50": rejeu["controls-0.50"][:-1]}
    with pytest.raises(GardeArret, match="manquant"):
        X.extraire(r, plan)


def test_episode_en_double_arrete(sain):
    plan, rejeu, _, _ = sain
    r = {**rejeu, "H": rejeu["H"] + [rejeu["H"][0]]}
    with pytest.raises(GardeArret, match="en double"):
        X.extraire(r, plan)


def test_condition_manquante_ou_de_trop_arrete(sain):
    plan, rejeu, _, _ = sain
    with pytest.raises(GardeArret, match="conditions du rejeu"):
        X.extraire({k: v for k, v in rejeu.items() if k != "identite"}, plan)
    with pytest.raises(GardeArret, match="conditions du rejeu"):
        X.extraire({**rejeu, "prediction-0.50": rejeu[BENIN]}, plan)
    with pytest.raises(GardeArret, match="conditions du rejeu"):
        X.extraire({k: v for k, v in rejeu.items() if k != BENIN}, plan)


def test_textes_du_temoin_benin_absents_de_la_sortie(sain):
    """Aucun texte d'un épisode du témoin bénin ne se retrouve dans les lignes écrites."""
    plan, rejeu, lignes, _ = sain
    textes_benins = {t for ep in rejeu[BENIN] for t in ep["textes"]}
    assert not textes_benins & {x["texte"] for x in lignes}


def test_episode_a_neuf_actions_arrete(sain):
    plan, rejeu, _, _ = sain
    r = copy.deepcopy(rejeu)
    r["H"][3]["actions"].pop()
    with pytest.raises(GardeArret, match="10 actions et 10 textes"):
        X.extraire(r, plan)


def test_tache_de_fabrication_ou_inconnue_arrete(sain):
    plan, rejeu, _, _ = sain
    for tache, motif in (("tache-fabrication-factice-00", "fabrication"), ("tache-evaluation-00", "hors des 16")):
        r = copy.deepcopy(rejeu)
        r["identite"][0]["tache"] = {"identifiant": tache}
        r["identite"][0].pop("episode")
        with pytest.raises(GardeArret, match=motif):
            X.extraire(r, plan)


def test_identifiant_d_episode_incoherent_arrete(sain):
    plan, rejeu, _, _ = sain
    r = copy.deepcopy(rejeu)
    r["H"][0]["episode"] = "fabrication/x/e0"
    with pytest.raises(GardeArret, match="identifiant d'épisode"):
        X.extraire(r, plan)


# --- garde de sortie (8.4) : épisode manquant, ligne du témoin bénin, champ de plus --------------------------------

def test_garde_de_sortie_episode_manquant(sain):
    plan, _, lignes, _ = sain
    with pytest.raises(GardeArret, match="épisode manquant"):
        X.verifier_lignes(lignes[:-10], plan)
    with pytest.raises(GardeArret, match="pas "):
        X.verifier_lignes(lignes[:-1], plan)


def test_garde_de_sortie_ligne_du_temoin_benin(sain):
    plan, _, lignes, _ = sain
    with pytest.raises(GardeArret, match="témoin bénin"):
        X.verifier_lignes(lignes[:-1] + [{**lignes[-1], "condition": BENIN}], plan)
    with pytest.raises(GardeArret, match="témoin bénin"):
        X.verifier_lignes(lignes + [{**lignes[-1], "condition": BENIN, "cle": "x"}], plan)


def test_garde_de_sortie_champ_de_plus(sain):
    plan, _, lignes, _ = sain
    for champ in ("score", "dose", "verdict"):
        with pytest.raises(GardeArret, match="aucun autre"):
            X.verifier_lignes(lignes[:-1] + [{**lignes[-1], champ: 0.5}], plan)
    sans = [{k: v for k, v in lignes[0].items() if k != "jetons"}] + lignes[1:]
    with pytest.raises(GardeArret, match="aucun autre"):
        X.verifier_lignes(sans, plan)


def test_garde_de_sortie_jetons_et_cle(sain):
    plan, _, lignes, _ = sain
    with pytest.raises(GardeArret, match="jetons ≠"):
        X.verifier_lignes([{**lignes[0], "jetons": lignes[0]["jetons"] + 1}] + lignes[1:], plan)
    with pytest.raises(GardeArret, match="en double"):
        X.verifier_lignes([{**lignes[0], "cle": lignes[1]["cle"]}] + lignes[1:], plan)


# --- câblage de la garde de sortie (correction 1 de la contre-lecture) ----------------------------------------------

@pytest.mark.parametrize("faute", ["episode_manquant", "temoin_benin", "champ_de_plus"])
def test_ecrire_refuse_et_n_ecrit_rien(tmp_path, sain, faute):
    plan, _, lignes, comptes = sain
    mauvaises = {"episode_manquant": lignes[:-10],
                 "temoin_benin": lignes[:-1] + [{**lignes[-1], "condition": BENIN}],
                 "champ_de_plus": lignes[:-1] + [{**lignes[-1], "score": 0.5}]}[faute]
    with pytest.raises(GardeArret):
        X.ecrire(tmp_path / "sortie", mauvaises, plan, comptes, {}, tmp_path)
    assert not (tmp_path / "sortie").exists()


def test_extraire_appelle_la_garde_de_sortie(sain, monkeypatch):
    plan, rejeu, lignes, _ = sain
    vues = []
    monkeypatch.setattr(X, "verifier_lignes", lambda l, p: vues.append((len(l), p is plan)))
    assert X.extraire(rejeu, plan)[0] == lignes
    assert vues == [(7680, True)]

    def refus(l, p):
        raise GardeArret("garde de sortie")

    monkeypatch.setattr(X, "verifier_lignes", refus)
    with pytest.raises(GardeArret, match="garde de sortie"):
        X.extraire(rejeu, plan)


# --- artefacts ajoutés en version 2 : un par garde ------------------------------------------------------------------

def test_episode_sans_ses_champs_arrete(sain):
    plan, rejeu, _, _ = sain
    for champ in ("tache", "k", "actions", "textes"):
        r = {**rejeu, "H": [{k: v for k, v in rejeu["H"][0].items() if k != champ}] + rejeu["H"][1:]}
        with pytest.raises(GardeArret, match="sans les champs"):
            X.extraire(r, plan)
    with pytest.raises(GardeArret, match="sans identifiant de tâche"):
        X.extraire({**rejeu, "H": [{**rejeu["H"][0], "tache": {"questions": "q"}}] + rejeu["H"][1:]}, plan)


def test_episode_hors_de_zero_a_sept_arrete(sain):
    plan, rejeu, _, _ = sain
    for k in (8, -1, "3", True):
        ep = {x: v for x, v in rejeu["H"][0].items() if x != "episode"}
        with pytest.raises(GardeArret, match="hors de 0 à 7"):
            X.extraire({**rejeu, "H": [{**ep, "k": k}] + rejeu["H"][1:]}, plan)


def test_action_ou_texte_hors_format_arrete(sain):
    plan, rejeu, _, _ = sain
    ep = rejeu["H"][0]
    for champ, valeur in (("actions", [["a", 1]] + ep["actions"][1:]), ("actions", ["12"] + ep["actions"][1:]),
                          ("actions", [[-1]] + ep["actions"][1:]), ("textes", [12] + ep["textes"][1:])):
        with pytest.raises(GardeArret, match="action ou texte hors format"):
            X.extraire({**rejeu, "H": [{**ep, champ: valeur}] + rejeu["H"][1:]}, plan)


def test_garde_de_sortie_condition_tache_et_format(sain):
    plan, _, lignes, _ = sain
    for champ, valeur, motif in (("condition", "controls-0.10", "hors des six conditions"),
                                 ("tache", "tache-evaluation-00", "hors des 16 tâches"),
                                 ("episode", 8, "hors format"), ("pas", 10, "hors format"), ("jetons", -1, "hors format"),
                                 ("texte", None, "hors format"), ("cle", "", "hors format")):
        with pytest.raises(GardeArret, match=motif):
            X.verifier_lignes([{**lignes[0], champ: valeur}] + lignes[1:], plan)


def test_listes_de_noms_de_la_configuration_du_bras():
    taches = config_bras()["taches_verification"]
    for valeur in (taches[:15] + [taches[0]], taches[:15] + [7], taches[:15] + [""], "tache"):
        with pytest.raises(GardeArret, match="liste de noms non vides, sans doublon"):
            X.plan_des_conditions({**config_bras(), "taches_verification": valeur})


def test_source_absente_et_condition_hors_format(tmp_path):
    with pytest.raises(GardeArret, match="absent"):
        X.lire_episodes_du_rejeu(tmp_path / "nulle-part.jsonl", "0" * 64)
    ep = rejeu_factice()["H"][0]
    for condition in ("", 3, None):
        chemin = tmp_path / f"episodes-{condition!r}.jsonl"
        chemin.write_text(json.dumps({"condition": condition, "episode": ep["episode"], "tache": "t", "k": 0,
                                      "actions": ep["actions"], "textes": ep["textes"]}) + "\n", encoding="utf-8")
        with pytest.raises(GardeArret, match="condition hors format"):
            X.lire_episodes_du_rejeu(chemin, hashlib.sha256(chemin.read_bytes()).hexdigest())


def test_configuration_du_bras_sans_compagnon_ou_alteree(tmp_path):
    episodes = tmp_path / "episodes-rejeu.jsonl"
    sha = _ecrire_episodes(episodes, {"H": rejeu_factice()["H"][:1]})
    cfg = tmp_path / "config-bras.json"
    cfg.write_text(json.dumps(config_bras()), encoding="utf-8")
    arguments = ["--episodes", str(episodes), "--sha256", sha, "--config-bras", str(cfg), "--racine", str(tmp_path),
                 "--sortie", str(tmp_path / "sortie")]
    with pytest.raises(GardeArret, match="sans empreinte compagnon"):
        X.principal(arguments)
    sceller(cfg)
    cfg.write_text(json.dumps({**config_bras(), "entropie": 1}), encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte ≠ compagnon"):
        X.principal(arguments)
    assert not (tmp_path / "sortie").exists()


def test_dossier_de_sortie_sous_la_racine_et_sans_fragment_refuse(tmp_path, sain):
    plan, _, lignes, comptes = sain
    assert X.exiger_dossier_permis(tmp_path / "entrees" / "base-bras-a", tmp_path) == "entrees/base-bras-a"
    for dossier, motif in ((tmp_path / "lecture-base", "fragment"), (tmp_path / "sorties-t07" / "base", "fragment"),
                           (tmp_path / "fabrication" / "base", "fragment"), (tmp_path.parent / "ailleurs", "hors de la racine"),
                           (tmp_path, "hors de la racine")):
        with pytest.raises(GardeArret, match=motif):
            X.ecrire(dossier, lignes, plan, comptes, {}, tmp_path)
        assert not (dossier / X.FICHIER_TEXTES).exists()


# --- configuration du bras -----------------------------------------------------------------------------------------

def test_plan_des_conditions_artefacts():
    X.plan_des_conditions(config_bras())                                                      # cas sain
    for cle, valeur, motif in (("doses_fabrication", [0.25, 0.5, 1.0], "quatre doses"),
                               ("proportions_temoin_benin", [], "liste non vide"),
                               ("proportions_temoin_benin", [0.3], "hors de"),
                               ("taches_fabrication", config_bras()["taches_fabrication"][:15], "15 noms"),
                               ("taches_fabrication", config_bras()["taches_verification"], "à la fois"),
                               ("entropie", -1, "entropie")):
        with pytest.raises(GardeArret, match=motif):
            X.plan_des_conditions({**config_bras(), cle: valeur})
    with pytest.raises(GardeArret, match="clés"):
        X.plan_des_conditions({k: v for k, v in config_bras().items() if k != "entropie"})


def test_chemins_permis():
    for nom in (X.FICHIER_TEXTES, X.FICHIER_CONFIG, X.FICHIER_MANIFESTE):
        X.exiger_chemin_permis(nom)                                                           # cas sains
    for rel, motif in (("textes-temoin-benin.jsonl", "fragment"), ("lecture-base.jsonl", "fragment"),
                       ("textes.npz", "extension"), ("../textes.jsonl", "relatif"), ("/tmp/textes.jsonl", "relatif")):
        with pytest.raises(GardeArret, match=motif):
            X.exiger_chemin_permis(rel)


# --- de bout en bout : fichier d'épisodes → sorties scellées → lecteurs d'entrée de la base inscrite ---------------

def _ecrire_episodes(chemin: Path, rejeu: dict, en_plus: dict | None = None) -> str:
    with open(chemin, "w", encoding="utf-8") as f:
        for condition, episodes in rejeu.items():
            for ep in episodes:
                x = {"condition": condition, "episode": ep["episode"], "tache": ep["tache"]["identifiant"],
                     "k": ep["k"], "actions": ep["actions"], "textes": ep["textes"], **(en_plus or {})}
                f.write(json.dumps(x, ensure_ascii=False) + "\n")
    return sceller(chemin)


def test_bout_en_bout_accepte_par_la_base_inscrite(tmp_path, base, capsys):
    mc, fab = base
    rejeu = rejeu_factice(lambda rng: fab.f7b.texte_action(rng, fab.f7b._cout_texte(rng, 300.0, False)))
    episodes = tmp_path / "episodes-rejeu.jsonl"
    sha = _ecrire_episodes(episodes, rejeu)
    cfg_bras = tmp_path / "config-bras.json"
    cfg_bras.write_text(json.dumps(config_bras()), encoding="utf-8")
    sceller(cfg_bras)
    sortie = tmp_path / "sortie"
    arguments = ["--episodes", str(episodes), "--sha256", sha, "--config-bras", str(cfg_bras), "--racine", str(tmp_path),
                 "--sortie", str(sortie)]
    assert X.principal(arguments) == 0
    imprime = capsys.readouterr().out
    assert "7680 lignes" in imprime and "ACTION" not in imprime and "COST" not in imprime
    assert sorted(p.name for p in sortie.iterdir()) == sorted(
        n + s for n in (X.FICHIER_TEXTES, X.FICHIER_CONFIG, X.FICHIER_MANIFESTE) for s in ("", ".sha256"))
    config = json.loads((sortie / X.FICHIER_CONFIG).read_text(encoding="utf-8"))
    assert tuple(sorted(config)) == tuple(sorted(X.CLES_CONFIG)) and len(config) == 6
    lignes = [json.loads(l) for l in (sortie / X.FICHIER_TEXTES).read_text(encoding="utf-8").splitlines()]
    assert len(lignes) == 7680 and all(set(x) == set(X.CHAMPS_ACTION_PERMIS) for x in lignes)
    manifeste = json.loads((sortie / X.FICHIER_MANIFESTE).read_text(encoding="utf-8"))
    assert manifeste["source"]["episodes_du_rejeu"]["sha256"] == sha
    assert manifeste["comptes"]["episodes_du_temoin_benin_laisses_de_cote"] == {BENIN: 128}
    assert "texte" not in json.dumps(manifeste["comptes"])
    # les lecteurs d'entrée de la base inscrite acceptent la configuration et le fichier des textes
    lb0 = mc.ListeBlancheBrasA.pour_bras_a((sortie, X.FICHIER_CONFIG))
    cfg = mc.lire_config_bras(lb0, sortie / X.FICHIER_CONFIG)
    lb = mc.ListeBlancheBrasA.pour_bras_a((sortie, X.FICHIER_CONFIG), (sortie, cfg["textes"]["chemin"]))
    entrees = mc.lire_entrees(lb, sortie, cfg, mc.v3.charger_modules_geles())
    assert entrees["effectifs"] == {c: 1280 for c in mc.CONDITIONS_LUES}
    assert len(entrees["donnees"]["cle"]) == 7680
    # jamais d'écrasement ; empreinte de la source exigée
    with pytest.raises(GardeArret, match="n'écrase jamais"):
        X.principal(arguments)
    with pytest.raises(GardeArret, match="empreinte"):
        X.principal(arguments[:3] + ["0" * 64] + arguments[4:-1] + [str(tmp_path / "sortie2")])
    assert not (tmp_path / "sortie2").exists()


def test_fichier_d_episodes_avec_un_champ_de_plus_arrete(tmp_path):
    episodes = tmp_path / "episodes-rejeu.jsonl"
    sha = _ecrire_episodes(episodes, {"H": rejeu_factice()["H"][:2]}, en_plus={"score": 0.5})
    with pytest.raises(GardeArret, match="aucun autre"):
        X.lire_episodes_du_rejeu(episodes, sha)
