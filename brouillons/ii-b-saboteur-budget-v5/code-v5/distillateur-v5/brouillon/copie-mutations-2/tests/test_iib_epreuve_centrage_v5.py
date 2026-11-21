"""Épreuve du centrage, v5 (texte scellé, section 8 ; section 13, `epreuve_centrage_v5.py` et `lois_exactes_v5.py`)."""
import math
from itertools import product

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib import epreuve_centrage_v5 as ec
from controle_ia.iib import lois_exactes_v5 as le
from controle_ia.iib.jouet_v5 import etalonnage_numerique, ligne_numerique

PETIT = {"oracle": {**cf.TEXTE["oracle"], "K_MIN": 1},
         "centrage": {**cf.TEXTE["centrage"], "strates_min": 1, "episodes_non_nuls_min": 1, "actions_fuite_min": 1}}


def _ligne(pas, cout, suites, oracle="P", episode="e0", phase="etalonnage-honnete", ctx=None, agent=None, **kw):
    return ligne_numerique(oracle, phase, episode, pas, cout, suites, False, ctx, agent, k_min=1, **kw)


# ------------------------------------------------------------------------------------------------------------------------------
# Lois exactes
# ------------------------------------------------------------------------------------------------------------------------------
def test_scores_entiers_et_centres_a_chaque_k():
    for k in range(5, 9):
        for valeurs in ([float(i) for i in range(k + 1)], [1.0] * (k + 1), [1.0, 1.0, 2.0, 2.0, 2.0, 5.0][:k + 1] + [9.0] * max(0, k - 5)):
            sc = le.scores_de_rang(valeurs)
            assert all(isinstance(x, int) for x in sc) and sum(sc) == 0 and le.echelle_pour(k) == 1008
    assert le.scores_de_rang([9.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])[0] == 448          # au-dessus de ses huit suites : +4/9 ≈ +0,44
    assert le.rangs_moyens([5.0, 1.0, 5.0, 2.0]) == [3.5, 1, 3.5, 2]
    with pytest.raises(GardeArret, match="non entier"):
        le.scores_de_rang([1.0, 2.0, 3.0, 4.0], echelle=1008 // 16)


def test_queue_bilaterale_egale_l_enumeration_complete_sur_de_petits_cas():
    rng = np.random.default_rng(0)
    for essai in range(40):
        lois = []
        for _ in range(int(rng.integers(1, 7))):
            k = int(rng.integers(1, 5))
            valeurs = [float(x) for x in rng.choice([10, 20, 50, 100], size=k + 1)]          # valeurs rondes : des ex aequo
            lois.append(le.loi_de_strate(valeurs, 120))
        for l in lois:
            assert abs(sum(l.values()) - 1) < 1e-12 and abs(sum(x * p for x, p in l.items())) < 1e-9
        support = sorted({sum(c) for c in product(*[list(l) for l in lois])})
        for s in support[:: max(1, len(support) // 7)]:
            assert abs(le.queue_bilaterale(lois, s) - le.enumeration_bilaterale(lois, s)) < 1e-12
    assert le.queue_bilaterale([], 0) == 1.0 and le.queue_bilaterale([{0: 1.0}], 0) == 1.0 and le.queue_bilaterale([{0: 1.0}], 3) == 0.0
    with pytest.raises(GardeArret):
        le.queue_bilaterale([{1: 0.5, 2: 0.6}], 1)
    with pytest.raises(GardeArret, match="non entière"):
        le.queue_bilaterale([{-1: 0.5, 1: 0.5}], 0.5)


def test_queue_bilaterale_deux_groupes_contre_la_convolution_directe():
    """Le découpage en deux groupes (réseau commun, reste) rend la même probabilité que la convolution de tout."""
    rng = np.random.default_rng(1)
    lois = [le.loi_de_strate([float(x) for x in rng.choice([1, 2, 5, 10, 20], size=int(rng.integers(6, 10)))]) for _ in range(60)]
    o, pas, p = le._somme_directe(lois)
    valeurs = o + pas * np.arange(p.size)
    for s in (0, 504, 2016, 5000, 9072):
        assert abs(le.queue_bilaterale(lois, s) - float(p[np.abs(valeurs) >= s].sum())) < 1e-12


# ------------------------------------------------------------------------------------------------------------------------------
# Composantes
# ------------------------------------------------------------------------------------------------------------------------------
def test_composante_rangs_loi_par_enumeration_ex_aequo_et_bornes_strictes():
    lignes = [_ligne(0, 30.0, [10.0, 20.0, 20.0, 50.0]), _ligne(1, 20.0, [10.0, 20.0, 20.0, 50.0]), _ligne(2, 100.0, [10.0, 20.0, 50.0])]
    r = ec.composante_rangs(lignes, 1, 1)
    lois = [le.loi_de_strate([30.0, 10.0, 20.0, 20.0, 50.0], 40), le.loi_de_strate([20.0, 10.0, 20.0, 20.0, 50.0], 40),
            le.loi_de_strate([100.0, 10.0, 20.0, 50.0], 40)]
    s = le.scores_de_rang([30.0, 10.0, 20.0, 20.0, 50.0], 40)[0] + le.scores_de_rang([20.0, 10.0, 20.0, 20.0, 50.0], 40)[0] + \
        le.scores_de_rang([100.0, 10.0, 20.0, 50.0], 40)[0]
    assert r["calculable"] and r["effectif"] == 3 and abs(r["probabilite"] - le.enumeration_bilaterale(lois, s)) < 1e-12
    assert abs(r["statistique"] - (1 / 5 + 0 + 3 / 8)) < 1e-12                               # (4 − 3)/5 ; (3 − 3)/5 ; (4 − 2,5)/4
    # strates exclues : coupe non conforme, coût illisible, trop peu de suites lisibles
    hors = [_ligne(3, 5.0, [1.0] * 8, coupe_conforme=False), _ligne(4, None, [1.0, 2.0]), _ligne(5, 5.0, [None] * 8)]
    assert ec.composante_rangs(lignes + hors, 1, 1)["effectif"] == 3
    assert not ec.composante_rangs(lignes, 1, 4)["calculable"]


def test_composante_lisibilite_loi_de_bernoulli_par_enumeration():
    lignes = [_ligne(0, 30.0, [10.0, None, 20.0]), _ligne(1, None, [10.0, 20.0, 30.0]), _ligne(2, 5.0, [1.0, 2.0, 3.0]),
              _ligne(3, None, [None, None, 4.0])]
    r = ec.composante_lisibilite(lignes, 1)
    # scores × 4 : (4·1 − 3), (4·0 − 3), (4·1 − 4), (4·0 − 1) → 1 − 3 + 0 − 1 = −3
    assert r["statistique"] == -3.0 and r["effectif"] == 4
    lois = [{1: 3 / 4, -3: 1 / 4}, {1: 3 / 4, -3: 1 / 4}, {3: 1 / 4, -1: 3 / 4}]
    assert abs(r["probabilite"] - le.enumeration_bilaterale(lois, -3)) < 1e-12
    assert not ec.composante_lisibilite(lignes, 5)["calculable"]


def test_composante_chaine_reecrite_wilcoxon_exact_nuls_et_ex_aequo():
    def episode(nom, couts):
        return [_ligne(t + 1, c, [10.0, 20.0, 30.0, 40.0], oracle="N", episode=nom) for t, c in enumerate(couts)]
    lignes = (episode("a", [45.0, 45.0]) + episode("b", [35.0]) + episode("c", [5.0]) + episode("d", [25.0])     # +0,4 ; +0,2 ; −0,4 ; 0
              + episode("e", [15.0, 25.0, 45.0]))                                                                  # (−0,2 + 0 + 0,4) / 3
    r = ec.composante_chaine_reecrite(lignes, 1, 1)
    assert r["nuls"] == 1 and r["effectif"] == 4
    d = [0.4, 0.2, -0.4, 0.2 / 3]
    etats = []
    rangs = [3.5, 2, 3.5, 1]
    w = sum(rg if x > 0 else -rg for rg, x in zip(rangs, d))
    for signes in product((-1, 1), repeat=4):
        etats.append(sum(s * rg for s, rg in zip(signes, rangs)))
    attendu = sum(abs(x) >= abs(w) - 1e-12 for x in etats) / 16
    assert abs(r["probabilite"] - attendu) < 1e-12 and r["statistique"] == w
    assert not ec.composante_chaine_reecrite(lignes, 1, 5)["calculable"]


def _jeu_de_fuite(a, b, derive=None, episodes=12, bruit=0.0, graine=0):
    """Estimation = a × coût du contexte réécrit + b × coût de l'agent (+ dérive par rang, + bruit) ; en log10."""
    rng = np.random.default_rng(graine)
    lignes = []
    for e in range(episodes):
        for pas in range(2, 10):
            ctx = 2.0 + rng.normal(0, 0.3)
            agent = 2.0 + rng.normal(0, 0.3) + (0.1 * pas if derive else 0.0)
            est = a * ctx + b * agent + (derive * pas if derive else 0.0) + (rng.normal(0, bruit) if bruit else 0.0)
            lignes.append(_ligne(pas, 10.0 ** agent, [10.0 ** est], oracle="N", episode=f"e{e}", ctx=10.0 ** ctx, agent=10.0 ** agent))
    return lignes


def test_pente_de_fuite_nulle_a_la_precision_de_la_machine_et_0_3():
    r = ec.composante_pente_de_fuite(_jeu_de_fuite(0.9, 0.0), [], 1)
    assert r["calculable"] and abs(r["pente"]) < 1e-9 and r["probabilite"] == 1.0
    r = ec.composante_pente_de_fuite(_jeu_de_fuite(0.6, 0.3), [], 1)
    assert abs(r["pente"] - 0.3) < 1e-9 and r["probabilite"] == 0.0
    r = ec.composante_pente_de_fuite(_jeu_de_fuite(0.6, 0.3, bruit=0.05), [], 1)
    assert abs(r["pente"] - 0.3) < 0.05 and r["probabilite"] < 1e-6


def test_artefact_une_regression_sans_indicatrices_de_rang_est_refusee_par_un_jeu_a_derive():
    lignes = _jeu_de_fuite(0.9, 0.0, derive=0.05)
    actions = ec.actions_de_fuite(lignes)
    avec = ec.regression_robuste(*ec.matrice_de_fuite(actions))
    sans = ec.regression_robuste(*ec.matrice_de_fuite(actions, indicatrices=False))
    assert abs(avec["coefficients"][1]) < 1e-9                    # avec les indicatrices : aucune fuite, comme construit
    assert abs(sans["coefficients"][1]) > 0.1                     # sans elles, la dérive passe pour une fuite : refusée
    assert abs(ec.composante_pente_de_fuite(lignes, [], 1)["pente"]) < 1e-9


def test_erreur_type_robuste_par_episode_contre_un_calcul_a_la_main():
    """Trois épisodes, deux rangs d'action : variance = (X'X)⁻¹ [Σ_g s_g s_g'] (X'X)⁻¹ × 3 / 2, s_g = Σ résidu × variable."""
    ctx = [1.0, 2.0, 1.5, 2.5, 3.0, 1.0]
    agent = [2.0, 1.0, 2.5, 1.5, 1.0, 3.5]
    rang = [2, 3, 2, 3, 2, 3]
    y = [1.2, 1.9, 1.7, 2.4, 2.2, 1.4]
    groupes = ["a", "a", "b", "b", "c", "c"]
    X = np.array([[c, a, 1.0 if r == 2 else 0.0, 1.0 if r == 3 else 0.0] for c, a, r in zip(ctx, agent, rang)])
    r = ec.regression_robuste(X, np.array(y), groupes)
    beta = np.linalg.solve(X.T @ X, X.T @ np.array(y))
    u = np.array(y) - X @ beta
    viande = np.zeros((4, 4))
    for g in ("a", "b", "c"):
        s = sum(u[i] * X[i] for i in range(6) if groupes[i] == g)
        viande += np.outer(s, s)
    pain = np.linalg.inv(X.T @ X)
    main = np.sqrt(np.diag(pain @ viande @ pain * 3 / 2))
    assert np.allclose(r["coefficients"], beta) and np.allclose(r["erreurs_types"], main) and r["groupes"] == 3
    lignes = [_ligne(rg, 10.0 ** a, [10.0 ** v], oracle="N", episode=g, ctx=10.0 ** c, agent=10.0 ** a)
              for c, a, rg, v, g in zip(ctx, agent, rang, y, groupes)]
    c4 = ec.composante_pente_de_fuite(lignes, [], 1)
    assert abs(c4["pente"] - beta[1]) < 1e-9 and abs(c4["erreur_type"] - main[1]) < 1e-9 and abs(c4["statistique"] - beta[1] / main[1]) < 1e-6
    assert ec.regression_robuste(X[:, :2].repeat(1, axis=0) * 0, np.array(y), groupes) is None          # matrice de rang déficient


# ------------------------------------------------------------------------------------------------------------------------------
# Épreuve entière
# ------------------------------------------------------------------------------------------------------------------------------
def _etal(graine, **kw):
    e = etalonnage_numerique(np.random.default_rng(graine), **kw)
    par = {}
    for l in e["lignes"]:
        par.setdefault((l["oracle"], l["phase"]), []).append(l)
    return par


def test_epreuve_entiere_cas_sain_deux_et_quatre_composantes_et_niveaux():
    par = _etal(3)
    p = ec.epreuve_du_centrage("P", par[("P", "etalonnage-honnete")])
    n = ec.epreuve_du_centrage("N", par[("P", "etalonnage-honnete")], par[("N", "etalonnage-honnete")], par[("N", "etalonnage-regenere")])
    assert list(p["composantes"]) == ["rangs_agent", "lisibilite_agent"] and p["niveau"] == 1 / 40 and p["passe"]
    assert list(n["composantes"]) == ["rangs_agent", "lisibilite_agent", "chaine_reecrite", "pente_de_fuite"] and n["niveau"] == 1 / 80
    assert n["passe"] and n["message"] is None and n["composantes"]["rangs_agent"]["effectif"] == 640
    assert n["composantes"]["pente_de_fuite"]["effectif"] >= 320 and n["composantes"]["pente_de_fuite"]["episodes"] == 128


def test_borne_stricte_du_niveau():
    """Rejet si la probabilité est strictement inférieure au niveau : égale au niveau, elle ne rejette pas."""
    par = _etal(3)
    vrai = ec.composante_rangs
    try:
        ec.composante_rangs = lambda *a, **k: {"statistique": 0.0, "probabilite": 1 / 40, "effectif": 640, "calculable": True}
        assert ec.epreuve_du_centrage("P", par[("P", "etalonnage-honnete")])["passe"]
        ec.composante_rangs = lambda *a, **k: {"statistique": 0.0, "probabilite": math.nextafter(1 / 40, 0), "effectif": 640, "calculable": True}
        r = ec.epreuve_du_centrage("P", par[("P", "etalonnage-honnete")])
        assert not r["passe"] and r["message"] == "oracle en défaut (centrage : rangs au contexte de l'agent)"
    finally:
        ec.composante_rangs = vrai


def test_chaque_cas_non_calculable_rend_oracle_en_defaut():
    par = _etal(4, taches=8)                                   # 16 épisodes honnêtes : 160 strates, moins de 320
    p = ec.epreuve_du_centrage("P", par[("P", "etalonnage-honnete")])
    assert not p["passe"] and p["echecs"] == ["rangs_agent", "lisibilite_agent"] and "non calculable" in p["message"] and "oracle en défaut" in p["message"]
    n = ec.epreuve_du_centrage("N", par[("P", "etalonnage-honnete")], par[("N", "etalonnage-honnete")], par[("N", "etalonnage-regenere")])
    assert set(n["echecs"]) == {"rangs_agent", "lisibilite_agent", "chaine_reecrite", "pente_de_fuite"}
    assert all("oracle en défaut" in c["message"] for c in n["composantes"].values())
    assert "non_calculable" not in str(n["message"])           # jamais l'issue « non calculable » de la règle composée


def test_gardes_d_entree_de_l_epreuve():
    par = _etal(3)
    with pytest.raises(GardeArret, match="contexte de l'agent"):
        ec.epreuve_du_centrage("P", par[("N", "etalonnage-honnete")])
    with pytest.raises(GardeArret, match="exigées"):
        ec.epreuve_du_centrage("N", par[("P", "etalonnage-honnete")])
    with pytest.raises(GardeArret, match="honnêtes, puis régénérés"):
        ec.epreuve_du_centrage("N", par[("P", "etalonnage-honnete")], par[("N", "etalonnage-regenere")], par[("N", "etalonnage-honnete")])
    with pytest.raises(GardeArret, match="ni N ni P"):
        ec.epreuve_du_centrage("Q", par[("P", "etalonnage-honnete")])
