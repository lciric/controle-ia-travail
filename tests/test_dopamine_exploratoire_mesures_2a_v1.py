"""Mesures de l'étape 2a (exploratoire) : chaque mesure sur un objet où sa conclusion est fausse et un où elle est vraie."""
import math

import numpy as np
import pytest

from controle_ia.dopamine_exploratoire import mesures_2a_v1 as m
from controle_ia.gardes import GardeArret


def _ar1(rng, n, rho):
    x = np.empty(n)
    x[0] = rng.standard_normal()
    for t in range(1, n):
        x[t] = rho * x[t - 1] + math.sqrt(1 - rho ** 2) * rng.standard_normal()
    return x


def test_correlation_pas_suivant_vraie_et_nulle():
    rng = np.random.default_rng(1)
    fort = m.correlation_pas_suivant([_ar1(rng, 400, 0.7) for _ in range(20)])
    nul = m.correlation_pas_suivant([rng.standard_normal(400) for _ in range(20)])
    assert abs(fort["rho"] - 0.7) < 0.05 and abs(nul["rho"]) < 0.05
    assert fort["couples"] == 20 * 399


def test_correlation_pas_suivant_gardes():
    with pytest.raises(GardeArret):
        m.correlation_pas_suivant([np.ones(1)])
    with pytest.raises(GardeArret):
        m.correlation_pas_suivant([np.ones(5), np.ones(5)])
    with pytest.raises(GardeArret):
        m.correlation_pas_suivant([np.array([1.0, np.nan, 2.0])])


def test_tailles_effectives():
    assert m.taille_effective_serie(100, 0.0) == 100
    assert m.taille_effective_serie(100, 0.5) == pytest.approx(100 / 3)
    assert m.taille_famille_ponderee([2, 2, 4]) == pytest.approx((4 + 4 + 16) / 8)
    assert m.taille_effective_familles([10] * 10, 0.0) == 100
    assert m.taille_effective_familles([10] * 10, -0.3) == 100          # ρ négatif compté 0
    assert m.taille_effective_familles([10] * 10, 0.1) == math.floor(100 / 1.9)
    assert m.taille_effective_familles([10] * 10, 1.0) == 10
    with pytest.raises(GardeArret):
        m.taille_effective_serie(100, 1.0)
    with pytest.raises(GardeArret):
        m.taille_effective_familles([0, 3], 0.1)


def test_seuil_et_indicatrice():
    s = np.arange(10.0)
    t = m.seuil_alerte(s, 0.2)
    assert t == 8.0 and m.indicatrice_alerte(s, t).sum() == 2
    assert m.indicatrice_alerte(np.arange(11.0), m.seuil_alerte(np.arange(11.0), 0.2)).sum() == 3   # ⌈2,2⌉
    with pytest.raises(GardeArret):
        m.seuil_alerte(s, 0.0)


def test_correlation_intra_famille_vraie_et_nulle():
    rng = np.random.default_rng(2)
    fam = np.repeat(np.arange(40), 10)
    groupe = np.repeat(rng.random(40) < 0.5, 10).astype(float)
    assert m.correlation_intra_famille(groupe, fam)["rho"] > 0.95          # tout est porté par la famille
    nul = m.correlation_intra_famille((rng.random(400) < 0.2).astype(float), fam)
    assert abs(nul["rho"]) < 0.06
    with pytest.raises(GardeArret):
        m.correlation_intra_famille(np.ones(4), np.zeros(4))


def test_correlation_alerte_par_famille_rend_taille_effective():
    rng = np.random.default_rng(3)
    fam = np.repeat(np.arange(30), 8)
    s = np.repeat(rng.standard_normal(30), 8) + 0.1 * rng.standard_normal(240)
    r = m.correlation_alerte_par_famille(s, fam)
    assert r["rho"] > 0.7 and r["taille_effective"] < 60 and abs(r["taux_alerte"] - 0.2) < 0.02


def test_taux_alerte_entre_lots_meme_loi_et_loi_deplacee():
    rng = np.random.default_rng(4)
    a = rng.standard_normal(2000)
    meme = m.taux_alerte_entre_lots(a, rng.standard_normal(2000))
    deplace = m.taux_alerte_entre_lots(a, rng.standard_normal(2000) + 1.0)
    assert meme["taux_vise_dans_l_intervalle"] and not deplace["taux_vise_dans_l_intervalle"]
    eff = m.taux_alerte_entre_lots(a, rng.standard_normal(2000), effectif_effectif_b=200)
    assert eff["effectif"] == 200 and eff["intervalle"][1] - eff["intervalle"][0] > 0.08
    with pytest.raises(GardeArret):
        m.taux_alerte_entre_lots(a, a, effectif_effectif_b=5000)


def test_intervalle_exact_bornes():
    assert m.intervalle_exact(0, 10)[0] == 0.0 and m.intervalle_exact(10, 10)[1] == 1.0
    b, h = m.intervalle_exact(20, 100)
    assert b < 0.2 < h
