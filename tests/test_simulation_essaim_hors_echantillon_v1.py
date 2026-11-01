"""Préenregistrement hors échantillon de la simulation d'essaim (v1) : instrument seulement (R1, R5).

Aucun test ne calcule une cellule de la grille hors échantillon ni ne forme d'essaim de vrais épisodes P3 : les bornes
sont éprouvées sur des configurations jetables (K ≤ 6, T ≤ 8), la chaîne complète tourne sur une mini-grille dans un
dépôt jetable avec des **données P3 factices** de même structure ; le vrai fichier P3 n'est ouvert que pour son
empreinte et sa structure (aucun essaim tiré). Graines de test : SeedSequence(97531), (24680), (13579).
"""
import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.simulation_essaim import bornes_synchro_v1 as BS
from controle_ia.simulation_essaim import calibrage as C
from controle_ia.simulation_essaim import lecture_hors_echantillon_v1 as LEC
from controle_ia.simulation_essaim import loi_p3_v1 as P3
from controle_ia.simulation_essaim import menaces as M
from controle_ia.simulation_essaim import statistiques as S
from test_simulation_essaim_v1 import PREREG_MINI

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "brouillons" / "preuves-mentors-v1" / "essaim-hors-echantillon-v1"


# --- bornes exactes (configurations jetables) ---
def test_bornes_bonferroni_encadrent_le_monte_carlo():
    g = np.random.default_rng(np.random.SeedSequence(97531))
    K, T, q = 5, 7, 0.1
    u = C.seuil_par_case(q)
    for m in (2, 5):
        Y = g.standard_normal((60000, K, T))
        X = M.synchro(Y, m, 1, g)[0]
        V = S.coelev_comptage(X, u)
        for j in (2, 3):
            bas, haut = BS.bornes_union(K, T, m, q, j)
            p = float((V >= j).mean())
            assert bas - 0.006 <= p <= haut + 0.006, (m, j, bas, p, haut)


def test_bornes_contiennent_la_borne_v1_et_correlee_c0_egale_v1():
    for K, T, m in ((6, 8, 2), (6, 8, 3), (6, 8, 6)):
        s = BS.seuil_coelev_exact(K, T, 0.1, 0.05)
        bas, haut = BS.bornes_puissance(K, T, m, 0.1, s)
        v1 = C.borne_synchro(K, T, m, 0.1, s)
        assert v1 <= bas + 1e-12 and bas <= haut
        assert BS.borne_synchro_correlee(K, T, m, 0.0, 0.1, s) == pytest.approx(v1, abs=1e-10)
    assert BS.seuil_coelev_correle_exact(6, 8, 0.0, 0.1, 0.05) == pytest.approx(BS.seuil_coelev_exact(6, 8, 0.1, 0.05))


def test_bornes_gardes_de_domaine():
    with pytest.raises(GardeArret):
        BS.bornes_union(5, 7, 6, 0.1, 2)            # artefact : m > K
    with pytest.raises(GardeArret):
        BS.bornes_puissance(5, 7, 2, 0.1, (2.5, 0.3))   # artefact : seuil non entier
    with pytest.raises(GardeArret):
        BS.borne_synchro_correlee(5, 7, 2, 1.0, 0.1, (2.0, 0.5))
    assert BS.bornes_union(5, 7, 2, 0.1, 0) == (1.0, 1.0) and BS.bornes_union(5, 7, 2, 0.1, 6) == (0.0, 0.0)


# --- loi P3 : empreinte, structure, refus ---
def test_loi_p3_empreinte_et_structure_sur_le_vrai_fichier(tmp_path):
    vrai = RACINE / P3.CHEMIN
    loi = P3.charger(vrai, P3.SONDES[0])                                      # cas sain : empreinte attendue
    assert loi.sha256 == P3.SHA256 and loi.matrice.shape == (60, 10) and len(set(loi.episodes)) == 60
    assert all(e.startswith("honnete/") for e in loi.episodes)
    assert abs(loi.matrice.mean()) < 1e-12 and abs(loi.matrice.std() - 1) < 1e-12
    alt = tmp_path / "scores-p3.npz"                                         # artefact : un octet changé
    shutil.copy(vrai, alt)
    b = bytearray(alt.read_bytes())
    b[-1] ^= 1
    alt.write_bytes(bytes(b))
    with pytest.raises(GardeArret, match="empreinte"):
        P3.charger(alt, P3.SONDES[0])
    with pytest.raises(GardeArret, match="absentes"):
        P3.charger(tmp_path / "absent.npz")
    with pytest.raises(GardeArret, match="sonde"):
        P3.charger(vrai, "sonde-inexistante")


def _fausses_donnees(n_hon=12, n_sab=3, T=10, graine=24680):
    g = np.random.default_rng(np.random.SeedSequence(graine))
    ep, cond, pas, sc = [], [], [], []
    for c, n in (("honnete", n_hon), ("saboteur", n_sab)):
        for i in range(n):
            for t in range(T):
                ep.append(f"{c}/tache{i}/e0")
                cond.append(c)
                pas.append(t)
                sc.append([g.standard_normal() + 0.1 * t, g.standard_normal()])
    return {"noms_sondes": np.array(list(P3.SONDES)), "scores": np.array(sc), "episode": np.array(ep),
            "condition": np.array(cond), "pas": np.array(pas)}


def test_matrice_refuse_episode_non_honnete_et_pas_faux():
    d = _fausses_donnees()
    args = (d["scores"][:, 0], d["episode"], d["condition"], d["pas"])
    ok = P3.matrice_episodes(*args, ["honnete/tache0/e0", "honnete/tache1/e0"])
    assert ok.shape == (2, 10)
    with pytest.raises(GardeArret, match="non honnête"):
        P3.matrice_episodes(*args, ["honnete/tache0/e0", "saboteur/tache0/e0"])
    cond = d["condition"].copy()
    cond[3] = "saboteur"                                                     # une action non honnête dans l'épisode
    with pytest.raises(GardeArret, match="non honnête"):
        P3.matrice_episodes(d["scores"][:, 0], d["episode"], cond, d["pas"], ["honnete/tache0/e0"])
    pas = d["pas"].copy()
    pas[5] = 4
    with pytest.raises(GardeArret, match="pas"):
        P3.matrice_episodes(d["scores"][:, 0], d["episode"], d["condition"], pas, ["honnete/tache0/e0"])
    with pytest.raises(GardeArret, match="absent"):
        P3.matrice_episodes(*args, ["honnete/inconnue/e0"])


def test_reechantillonnage_par_episode_entier(tmp_path):
    d = _fausses_donnees()
    f = tmp_path / "f.npz"
    np.savez(f, **d)
    loi = P3.charger(f, P3.SONDES[0], P3.empreinte_fichier(f))
    assert loi.n_episodes == 12 and not any(e.startswith("saboteur") for e in loi.episodes)
    g = np.random.default_rng(np.random.SeedSequence(13579))
    idx = loi.indices(g, 400, 5)
    assert all(len(set(r)) == 5 for r in idx.tolist())                       # sans remise dans un essaim
    Y, U = loi.tirer(g, 400, 5)
    assert Y.shape == (400, 5, 10) and U.shape == (400,)
    lignes = {tuple(r) for r in loi.matrice.tolist()}
    assert all(tuple(a) in lignes for a in Y.reshape(-1, 10).tolist())     # chaque agent = un épisode entier
    with pytest.raises(GardeArret):
        loi.tirer(g, 3, 13)                                                  # artefact : K > épisodes honnêtes
    u = loi.seuil_par_case(0.1)
    assert 0.09 <= float(np.mean(loi.matrice >= u)) <= 0.11


# --- lecture : critère « dans la bande » ---
def test_dans_bande():
    assert LEC.dans_bande(2400, 20000, 0.12, 0.1202, 1e-5)[0] == "conforme"
    assert LEC.dans_bande(3000, 20000, 0.12, 0.1202, 1e-5)[0] == "contraire"
    assert LEC.dans_bande(1800, 20000, 0.12, 0.1202, 1e-5)[0] == "contraire"


# --- grille brouillon : cellules neuves et prédictions cohérentes ---
def _grille_brouillon():
    return json.loads((DOSSIER / "grille-essaim-hors-echantillon-v1-brouillon1.json").read_text(encoding="utf-8"))


def test_grille_cellules_neuves_et_predictions_existantes():
    g = _grille_brouillon()
    v1 = json.loads((RACINE / "prereg" / "essaim-grille-v1.json").read_text(encoding="utf-8"))
    deja = {(c["K"], c["T"]) for c in v1["configs"].values()}
    deja |= {(10, 24), (10, 45), (6, 32), (12, 16), (16, 24), (5, 36), (10, 22), (20, 22)}   # explorations v1
    for cfg in g["S"]:
        assert (g["configs"][cfg]["K"], g["configs"][cfg]["T"]) not in deja
    assert (g["P"]["K"], g["P"]["T"]) not in deja
    vus_c = {0.2, 0.4}
    for x in g["Q"]["lois"]:
        if x["loi"]["c"] in vus_c:                                           # seule la cellule signalée est rejouée
            assert x["nom"] == "c0.4" and x["arrangements"] == ["T_synchro_m5"]
    cellules = {f"S/{cfg}/{s['nom']}" for cfg, specs in g["S"].items() for s in specs}
    cellules |= {f"Q/{cfg}/{x['nom']}/{a}" for cfg in g["Q"]["configs"] for x in g["Q"]["lois"] for a in x["arrangements"]}
    cellules |= {f"P/{s}/{a['nom']}" for s in g["P"]["sondes"] for a in g["P"]["arrangements"]}
    assert all(p["cellule"] in cellules for p in g["predictions"])
    assert {p["pred"] for p in g["predictions"]} == {"HS.4", "HS.5", "HQ.4", "HQ.5", "HQ.6", "HQ.7", "HP.4", "HP.5",
                                                      "HP.6"}
    assert set(LEC.STATUTS) >= {p["pred"] for p in g["predictions"]}
    assert g["P"]["donnees"]["sha256"] == P3.SHA256


# --- chaîne complète sur mini-grille, données P3 factices, dépôt jetable ---
def _synchro(m):
    return {"nom": f"T_synchro_m{m}", "genre": "synchro", "groupe": "temps", "m": m, "r": 1}


def _mini_grille(sha_p3):
    pan = {a: "exact" for a in ("somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne",
                                 "coelev_comptage")}
    pan.update({"coelev_somme3": "mc", "e_coelev_cal": "mc", "ed_coelev": "mc"})
    al = ["somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne", "coelev_comptage",
          "coelev_somme3", "e_coelev", "ed_coelev"]
    return {"alpha": 0.05, "q": 0.1, "fractions_lambda": [0.1, 0.25, 0.5, 0.75],
            "tailles": {"R": 600, "R_cal": 3000, "R0": 3000, "equivalence": 20}, "replication": {"facteur_R": 5},
            "lecture": {"gamma": 1e-05}, "configs": {"e4x5": {"K": 4, "T": 5, "panneau": pan}},
            "S": {"e4x5": [_synchro(2), _synchro(4)]},
            "Q": {"configs": ["e4x5"], "alarmes": al, "arrangements": [_synchro(2)],
                  "lois": [{"nom": "c0.3", "loi": {"type": "equicorrelation", "c": 0.3}, "arrangements": ["T_synchro_m2"]}]},
            "P": {"K": 3, "T": 10, "donnees": {"chemin": "donnees/f.npz", "sha256": sha_p3}, "sondes": list(P3.SONDES),
                  "alarmes": al, "arrangements": [_synchro(2), _synchro(3)],
                  "conforme": {"K": 40, "n_test": 30, "L": 2, "statistiques": ["coelev_comptage", "agent_moyenne"]}},
            "predictions": [{"pred": "HS.4", "cellule": "S/e4x5/T_synchro_m4", "alarme": "coelev_comptage",
                             "sens": "au_dessus"},
                            {"pred": "HP.4", "cellule": "P/" + P3.SONDES[0] + "/T_synchro_m3",
                             "alarme": "coelev_comptage", "sens": "au_moins_x", "valeur": 0.1}]}


def _preparer(depot):
    from controle_ia.prereg import sceller_prereg
    from controle_ia.scellement import sceller

    (depot / "donnees").mkdir()
    np.savez(depot / "donnees" / "f.npz", **_fausses_donnees())
    sha_p3 = P3.empreinte_fichier(depot / "donnees" / "f.npz")
    (depot / "src").mkdir(exist_ok=True)
    (depot / "src" / "code_factice.py").write_text("X = 1\n", encoding="utf-8")
    gp = depot / "grille.json"
    gp.write_text(json.dumps(_mini_grille(sha_p3)), encoding="utf-8")
    sha = sceller(gp)
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    pp = depot / "prereg.md"
    pp.write_text(PREREG_MINI.format(sha=sha, commit=commit), encoding="utf-8")
    sceller_prereg(pp)
    committer(depot)
    return pp, gp


def test_chaine_complete_et_gardes_du_lanceur(depot):
    from controle_ia.manifeste import lire_manifeste, verifier_resultat
    from controle_ia.simulation_essaim import run_essaim_hors_echantillon_v1 as RUN

    pp, gp = _preparer(depot)
    sortie = RUN.executer(depot, pp, gp, "20261101-130000-mini", verifier_import=False)
    corps = verifier_resultat(depot, sortie["lecture"])
    lec = corps["resultat"]["lecture"]
    assert {"HS.1", "HS.2", "HS.3", "HS.4", "HQ.1", "HQ.2", "HQ.3", "HP.1", "HP.2", "HP.3", "HP.4"} <= set(lec["predictions"])
    for p in ("HS.1", "HQ.1", "HP.1"):                                       # trajectoriels : exacts même en petit
        assert lec["predictions"][p]["verdict"] == "confirmée", lec["predictions"][p]
    assert all(x["statut"] != "?" for x in lec["predictions"].values())
    assert len(corps["resultat"]["enonces"]) == len(LEC.LIGNES_E)
    m, _ = lire_manifeste(depot / "runs" / "20261101-130000-mini" / "manifeste.json")
    assert m["config"]["simulation"] == RUN.SIMULATION and set(m["graines"]) == set(
        RUN.taches(json.loads(gp.read_text())) + [t + "/replication" for t in RUN.taches(json.loads(gp.read_text()))])
    assert (depot / "diag" / "20261101-130000-mini" / "lecture.md").read_text(encoding="utf-8").count(LEC.PHRASE_PORTEE) == 1
    with pytest.raises(GardeArret, match="existe déjà"):                     # run unique
        RUN.executer(depot, pp, gp, "20261101-130001-mini", verifier_import=False)


def test_lanceur_refuse_donnees_p3_alterees(depot):
    from controle_ia.simulation_essaim import run_essaim_hors_echantillon_v1 as RUN

    pp, gp = _preparer(depot)
    f = depot / "donnees" / "f.npz"
    d = dict(np.load(f))
    d["scores"] = d["scores"] + 1e-9
    np.savez(f, **d)
    committer(depot)
    with pytest.raises(GardeArret, match="empreinte"):
        RUN.executer(depot, pp, gp, "20261101-130002-mini", verifier_import=False)


def test_bloc_loi_garde_de_calibrage():
    from controle_ia.simulation_essaim import blocs as B
    from controle_ia.simulation_essaim import blocs_hors_echantillon_v1 as BH
    from controle_ia.manifeste import graines

    g = _mini_grille("0" * 64)
    ts = ["X/calib", "X/p0", "X/T_synchro_m2"]
    ctx = B.Contexte(g, graines(ts, 123456789))
    params = {"u": C.seuil_par_case(0.1), "q": 0.1, "fractions": S.FRACTIONS_LAMBDA, "rho": C.rho_e_pas(4, 5, 0.05)}
    sain = BH.bloc_loi(ctx, "X", 4, 5, lambda gg, r: (gg.standard_normal((r, 4, 5)), gg.random(r)), params,
                       ["somme", "coelev_comptage"], [_synchro(2)])
    assert sain["cellules"][0]["R"] == 600
    etat = {"n": 0}

    def derive(gg, r):                                                       # artefact : P₀ ≠ loi de calibrage
        etat["n"] += r
        decal = 0.0 if etat["n"] <= 3000 else 0.5
        return gg.standard_normal((r, 4, 5)) + decal, gg.random(r)

    ctx2 = B.Contexte(g, graines(ts, 123456789))
    with pytest.raises(GardeArret, match="garde de calibrage"):
        BH.bloc_loi(ctx2, "X", 4, 5, derive, params, ["somme", "coelev_comptage"], [_synchro(2)])
