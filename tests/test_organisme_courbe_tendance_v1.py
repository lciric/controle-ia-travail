"""Essais du test exact de tendance (règle R5 : un cas sain et un artefact)."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_courbe.tendance_v1 import TableTendance, puissance


def test_valeurs_p_extremes_et_somme_des_poids():
    t = TableTendance([3, 3, 3], [0, 1, 2])
    # aucune issue n'est plus extrême que « tous les succès à la plus forte dose » : p minimale pour ce total
    p_haut = t.valeur_p(np.array([0, 0, 3]))
    p_bas = t.valeur_p(np.array([3, 0, 0]))
    assert p_haut < p_bas == pytest.approx(1.0)
    # total nul : une seule issue, p = 1
    assert t.valeur_p(np.array([0, 0, 0])) == pytest.approx(1.0)


def test_niveau_sous_le_nul_ne_depasse_pas_alpha():
    # cas sain : sous une probabilité égale à toutes les doses, le taux de rejet reste sous alpha (test exact, prudent)
    t = TableTendance([8] * 5, [0, 1, 2, 3, 4])
    r = puissance(t, [0.3] * 5, 0.05, 20000, np.random.default_rng(3))
    assert r["rejet"] <= 0.05 + 0.006


def test_puissance_forte_sous_une_tendance_nette():
    t = TableTendance([8] * 5, [0, 1, 2, 3, 4])
    r = puissance(t, [0.0, 0.2, 0.5, 0.7, 0.8], 0.05, 5000, np.random.default_rng(4))
    assert r["rejet"] > 0.9


def test_artefact_tendance_inversee_ne_rejette_pas():
    # artefact : une probabilité qui décroît avec la dose ne doit presque jamais être lue comme une hausse
    t = TableTendance([8] * 5, [0, 1, 2, 3, 4])
    r = puissance(t, [0.8, 0.7, 0.5, 0.2, 0.0], 0.05, 5000, np.random.default_rng(5))
    assert r["rejet"] < 0.001


def test_gardes():
    with pytest.raises(GardeArret):
        TableTendance([3], [0])
    with pytest.raises(GardeArret):
        TableTendance([3, 3], [1, 1])
    t = TableTendance([2, 2], [0, 1])
    with pytest.raises(GardeArret):
        t.valeur_p(np.array([3, 0]))
    with pytest.raises(GardeArret):
        puissance(t, [0.5], 0.05, 10, np.random.default_rng(0))
