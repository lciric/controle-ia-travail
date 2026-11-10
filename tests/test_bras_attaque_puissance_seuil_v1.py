import numpy as np
import pytest
from scipy import stats

from controle_ia.bras_attaque import puissance_seuil_v1 as p
from controle_ia.gardes import GardeArret


def test_k_empirique_regle_du_temoin_de_bailey():
    assert p.k_empirique(200, 0.01) == 2
    assert p.k_empirique(1000, 0.01) == 10
    assert p.k_empirique(99, 0.01) == 0


def test_loi_exacte_du_taux_reel_contre_simulation_cas_sain():
    rng = np.random.default_rng(np.random.SeedSequence(20261110))
    n, k, tirages = 200, 2, 20000
    notes = rng.standard_normal((tirages, n))
    tau = -np.partition(-notes, k, axis=1)[:, k]
    fpr = stats.norm.sf(tau)
    q_simule = np.quantile(fpr, [0.5, 0.95])
    q_exact = p.fpr_reel_quantiles(n, k, [0.5, 0.95])
    assert np.allclose(q_simule, q_exact, rtol=0.05)


def test_loi_exacte_independante_de_la_loi_des_notes():
    rng = np.random.default_rng(np.random.SeedSequence(7))
    n, k, tirages = 300, 3, 20000
    notes = rng.exponential(size=(tirages, n))
    tau = -np.partition(-notes, k, axis=1)[:, k]
    fpr = np.exp(-tau)
    assert np.isclose(np.quantile(fpr, 0.95), p.fpr_reel_quantiles(n, k, [0.95])[0], rtol=0.05)


def test_k_garanti_monotone_et_artefact_petit_n():
    assert p.k_garanti(50, 0.01, 0.05) == -1
    k1 = p.k_garanti(1000, 0.01, 0.05)
    k2 = p.k_garanti(5000, 0.01, 0.05)
    assert 0 <= k1 <= k2
    assert p.fpr_reel_proba_au_dela(5000, k2, 0.01) <= 0.05
    assert p.fpr_reel_proba_au_dela(5000, k2 + 1, 0.01) > 0.05


def test_intervalle_predictif_des_alertes_couvre():
    rng = np.random.default_rng(np.random.SeedSequence(11))
    n, k, h = 600, 6, 400
    bas, haut = p.alertes_honnetes_intervalle(n, k, h, 0.95)
    fpr = rng.beta(k + 1, n - k, 20000)
    alertes = rng.binomial(h, fpr)
    couverture = np.mean((alertes >= bas) & (alertes <= haut))
    assert couverture >= 0.95


def test_nul_sain_tombe_peu_et_chaine_gonflee_detectee():
    rng = np.random.default_rng(np.random.SeedSequence(12))
    assert p.puissance_nul(1000, 10, 1000, 1.0, 0.95, 20000, rng) <= 0.05
    assert p.puissance_nul(1000, 10, 1000, 5.0, 0.95, 20000, rng) >= 0.9


def test_clopper_pearson_bornes_et_artefact():
    bas, haut = p.clopper_pearson(np.array([0, 5, 10]), 10, 0.95)
    assert bas[0] == 0.0 and haut[2] == 1.0
    assert 0.0 < bas[1] < 0.5 < haut[1] < 1.0
    with pytest.raises(GardeArret):
        p.clopper_pearson(np.array([11]), 10, 0.95)


def test_temoin_faille_cas_sain_et_cas_nul():
    rng = np.random.default_rng(np.random.SeedSequence(13))
    assert p.puissance_temoin_faille(50, 0.8, 0.1, 0.95, 20000, rng) >= 0.95
    assert p.puissance_temoin_faille(50, 0.3, 0.3, 0.95, 20000, rng) <= 0.01
    assert not p.temoin_faille_casse(20, 0, 50, 50, 0.95)


def test_rappel_binormal_grand_n_sans_biais():
    rng = np.random.default_rng(np.random.SeedSequence(14))
    r = p.simuler_rappel_binormal(20000, 2000, 0.5, 0.01, 200, rng)
    assert abs(r["ecart_total_quantiles"][1]) < 0.02
    assert abs(r["fpr_reel_quantiles"][1] - 0.01) < 0.002


@pytest.mark.parametrize("args", [(0, 0), (10, 10), (10, -1)])
def test_gardes_entrees_invalides(args):
    n, k = args
    with pytest.raises(GardeArret):
        p.fpr_reel_quantiles(n, k, [0.5])


def test_garde_probabilite_invalide():
    with pytest.raises(GardeArret):
        p.k_empirique(100, 1.5)
