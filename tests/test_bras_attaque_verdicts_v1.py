import numpy as np
import pytest

from controle_ia.bras_attaque import verdicts_v1 as v
from controle_ia.bras_attaque import puissance_seuil_v1 as p
from controle_ia.gardes import GardeArret


def test_verdicts_somment_a_un_et_cas_extremes():
    r = v.verdicts_exacts(100, 100, 0.1, 0.1, 0.10)
    assert abs(sum(r.values()) - 1.0) < 1e-9
    assert r["casse"] < 0.01
    fort = v.verdicts_exacts(100, 100, 0.9, 0.05, 0.10)
    assert fort["casse"] > 0.99
    moyen = v.verdicts_exacts(100, 100, 0.40, 0.05, 0.10)
    assert moyen["entame"] > 0.9


def test_verdicts_contre_simulation():
    rng = np.random.default_rng(np.random.SeedSequence(21))
    m, eb, en, d = 60, 0.3, 0.15, 0.10
    xb = rng.binomial(m, eb, 40000)
    xn = rng.binomial(m, en, 40000)
    bas_b, haut_b = p.clopper_pearson(xb, m, 0.95)
    _, haut_n = p.clopper_pearson(xn, m, 0.95)
    hausse = bas_b > haut_n
    resiste = ~hausse & (haut_b <= xn / m + d + 1e-12)
    exact = v.verdicts_exacts(m, m, eb, en, d)
    assert abs(np.mean(resiste) - exact["resiste"]) < 0.01
    assert abs(np.mean(hausse & (2 * xb < m)) - exact["entame"]) < 0.01


def test_temoin_exact_valeurs_de_la_contre_lecture():
    assert abs(v.temoin_faille_exact(50, 0.6, 0.1)["constitue_et_casse"] - 0.94) < 0.01
    assert abs(v.temoin_faille_exact(50, 0.8, 0.3)["constitue_et_casse"] - 0.78) < 0.01
    pire, _ = v.fausse_cassure_pire(50)
    assert pire < 0.005


def test_nul_exact_proche_de_la_simulation():
    rng = np.random.default_rng(np.random.SeedSequence(22))
    exact = v.nul_sensibilite_exacte(1000, 10, 500, 5.0, 0.99)
    simule = p.puissance_nul(1000, 10, 500, 5.0, 0.99, 40000, rng)
    assert abs(exact - simule) < 0.01
    assert v.nul_sensibilite_exacte(1000, 10, 500, 1.0, 0.99) < 0.01


def test_dommage_honnete_valeurs_de_la_contre_lecture():
    assert abs(v.dommage_honnete_chute(500, 0.005) - 0.24) < 0.02
    assert abs(v.dommage_honnete_chute(500, 0.01) - 0.74) < 0.02


def test_rang_voit_une_baisse_que_le_decompte_ne_voit_pas():
    rng = np.random.default_rng(np.random.SeedSequence(23))
    assert v.puissance_rang_binormal(1000, 500, -0.27, 0.01, 0.05, 300, rng) > 0.8
    assert v.puissance_rang_binormal(1000, 500, 0.0, 0.01, 0.05, 300, rng) < 0.05


def test_garde_entrees_invalides():
    with pytest.raises(GardeArret):
        v.verdicts_exacts(10, 10, 1.5, 0.1, 0.1)
