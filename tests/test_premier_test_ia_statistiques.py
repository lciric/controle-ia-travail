"""Statistiques de la lecture du premier test (i-a) : cas sains et artefacts de chaque garde (R5)."""
import math

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia.statistiques import (accumulation, cout_de_tache, cout_lisible, detection,
                                                      effet_cout_apparie)


def test_cout_lisible():
    assert cout_lisible(3) and cout_lisible(0.5)
    for c in (None, 0, -1.0, float("nan"), float("inf"), True, "3"):
        assert not cout_lisible(c)


def test_cout_de_tache():
    r = cout_de_tache([10.0, 1000.0, None, 0])
    assert math.isclose(r["valeur"], 2.0) and r["lisibles"] == 2 and r["illisibles"] == 2 and r["nuls"] == 1
    assert cout_de_tache([None, float("nan")])["valeur"] is None


def _couts(n_taches, facteur, rng):
    base = {t: list(10 ** rng.normal(1.0, 0.5, size=10)) for t in range(n_taches)}
    return base, {t: [c * facteur for c in v] for t, v in base.items()}


def test_effet_cout_sain_et_nul():
    rng = np.random.default_rng(1)
    honnete, saboteur = _couts(60, 3.0, rng)
    r = effet_cout_apparie(saboteur, honnete, np.random.default_rng(2), n_tirages=2000)
    assert math.isclose(r["effet"], math.log10(3.0), rel_tol=1e-9) and r["bas"] > 0
    # artefact : aucune différence, mais du bruit propre à chaque condition ; l'intervalle contient 0
    autre = {t: list(10 ** rng.normal(1.0, 0.5, size=10)) for t in range(60)}
    r0 = effet_cout_apparie(autre, honnete, np.random.default_rng(3), n_tirages=2000)
    assert r0["bas"] < 0 < r0["haut"]


def test_effet_cout_taches_exclues_et_gardes():
    rng = np.random.default_rng(4)
    honnete, saboteur = _couts(5, 3.0, rng)
    saboteur[2] = [None] * 10
    r = effet_cout_apparie(saboteur, honnete, np.random.default_rng(5), n_tirages=100)
    assert r["taches_exclues"] == [2] and r["n_taches"] == 4 and r["actions_illisibles_a"] == 10
    with pytest.raises(GardeArret):
        effet_cout_apparie({0: [1.0]}, {1: [1.0]}, np.random.default_rng(0))
    with pytest.raises(GardeArret):
        effet_cout_apparie({0: [None], 1: [1.0]}, {0: [1.0], 1: [1.0]}, np.random.default_rng(0))
    with pytest.raises(GardeArret):
        effet_cout_apparie(saboteur, honnete, 7)


def _jeu(n_taches, decalage, rng, n_plancher=50):
    cond, tache, s = [], [], []
    for t in range(n_taches):
        for c, d in (("honnete", 0.0), ("saboteur", decalage), ("temoin", 0.0)):
            for _ in range(10):
                cond.append(c)
                tache.append(t)
                s.append(rng.normal(d, 1.0))
    s = np.array(s)
    return s, rng.normal(size=(s.size, n_plancher)), np.array(cond), np.array(tache)


def test_detection_saine_et_artefact():
    rng = np.random.default_rng(6)
    s, p, c, t = _jeu(30, 1.5, rng)
    r = detection(s, p, c, t, "saboteur", "honnete", 500, 7)
    assert r["au_dessus_du_plancher"] and r["aire"] > 0.8 and r["n_positifs"] == r["n_negatifs"] == 300
    r2 = detection(s, p, c, t, "temoin", "honnete", 500, 8)
    assert not r2["au_dessus_du_plancher"]


def test_detection_gardes():
    rng = np.random.default_rng(9)
    s, p, c, t = _jeu(4, 1.0, rng)
    with pytest.raises(GardeArret):
        detection(s, p, c, t, "saboteur", "saboteur", 10, 0)
    with pytest.raises(GardeArret):
        detection(s, p[:-1], c, t, "saboteur", "honnete", 10, 0)
    s2 = s.copy()
    s2[0] = np.nan
    with pytest.raises(GardeArret):
        detection(s2, p, c, t, "saboteur", "honnete", 10, 0)
    p2 = p.copy()
    p2[3, 1] = np.inf
    with pytest.raises(GardeArret):
        detection(s, p2, c, t, "saboteur", "honnete", 10, 0)
    with pytest.raises(GardeArret):
        detection(s, p, c, t, "saboteur", "absent", 10, 0)


def test_accumulation_somme_contre_maximum():
    rng = np.random.default_rng(10)
    cond, ep, s = [], [], []
    for e in range(60):
        for c, d in (("honnete", 0.0), ("saboteur", 0.8)):
            for _ in range(10):
                cond.append(c)
                ep.append(f"{c}-{e}")
                s.append(rng.normal(d, 1.0))
    r = accumulation(np.array(s), np.array(cond), np.array(ep))
    assert r["episodes"] == {"honnete": 60, "saboteur": 60}
    assert r["somme"]["faux_positifs_observes"] <= 0.01 and r["maximum"]["faux_positifs_observes"] <= 0.01
    # un faible décalage diffus s'accumule : la somme rappelle davantage que le maximum
    assert r["somme"]["rappel"] > r["maximum"]["rappel"]


def test_accumulation_gardes():
    with pytest.raises(GardeArret):
        accumulation(np.ones(4), np.array(["honnete"] * 2 + ["saboteur"] * 2), np.array(["a", "a", "b", "b"]))
    with pytest.raises(GardeArret):
        accumulation(np.array([0.0, 1.0, 2.0, 3.0]), np.array(["honnete", "honnete", "saboteur", "saboteur"]),
                     np.array(["a", "a", "a", "a"]))
    with pytest.raises(GardeArret):
        accumulation(np.array([0.0, 1.0]), np.array(["honnete", "honnete"]), np.array(["a", "a"]))
