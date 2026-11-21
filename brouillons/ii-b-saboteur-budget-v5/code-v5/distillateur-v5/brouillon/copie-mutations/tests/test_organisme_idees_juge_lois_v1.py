"""Essais des lois du banc B v2 (idée 1.2) : évaluateur vectorisé égal au juge réel, constructeurs, composantes."""
import math
import random

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import juge_v1
from controle_ia.organisme_idees_juge import lois_v1 as L


@pytest.fixture(scope="module")
def J():
    return juge_v1.charger()


def _archive(rng):
    S1, S2, U1, U2, U3, U4 = (L.softmax_aleatoire(rng) for _ in range(6))
    jA = 0
    return {"S1": S1, "S2": S2, "S3": L.si_sinon_trait(jA, 0.42, U1, U2), "S4": L.si_sinon_trait(1, -0.55, U3, U4),
            "jA": jA, "sA": 0.42, "sB": -0.55, "cut": {0: 0.42, 1: -0.55}}


def _lois_variees(rng):
    a = _archive(rng)
    lois = [a["S1"], a["S3"], L.melange_archive(a, rng), L.tempere_incline(a["S4"], rng),
            L.par_sous_population(a["S1"], L.melange([a["S1"], a["S2"]], [0.7, 0.3])),
            {"type": "si_sinon", "condition": {"sous_population": 1}, "si": a["S2"], "sinon": a["S1"]},
            {"type": "transformee", "base": a["S2"], "melange_aveugle": {"lambda": 0.3, "probas": [1, 2, 3]},
             "puissance": 0.8, "inclinaison": [0.1, -0.2, 0.05],
             "oscillation": {"amplitude": 0.4, "frequence": 2.0, "trait": 1, "issue": 2, "phase": 0.3}},
            L.UNIFORME]
    for genre in L.TYPES:
        comp = L.tirer_composante(genre, L.DOSES[genre][1], a, rng)
        lois += [comp.loi(1.0), comp.loi(0.5), comp.bruitee(rng).loi(1.0)]
        if genre != "V4":
            lois.append(comp.loi(-1.0))
    return lois


def test_evaluateur_vectorise_egal_au_juge(J):
    rng = np.random.default_rng(3)
    inst = J.sp.tirer_instances(random.Random(4), 300, 2)
    Z = np.array([x["z"] for x in inst]); G = np.array([x["g"] for x in inst])
    for loi in _lois_variees(rng):
        J.sp.valider_loi(loi, 3, 2)
        P = L.probas_np(loi, Z, G)
        Pj = np.array([J.sp.proba(loi, x, [], t) for t, x in enumerate(inst)])
        assert np.max(np.abs(P - Pj)) <= 1e-12


def test_evaluateur_refuse_un_type_hors_du_banc():
    Z, G = np.zeros((2, 2)), np.zeros(2, int)
    with pytest.raises(GardeArret):
        L.probas_np({"type": "moyenne_glissante", "nombre_issues": 3, "fenetre": 5, "lissage": 0.5}, Z, G)
    with pytest.raises(GardeArret):
        L.probas_np({"type": "par_sous_population", "lois": {"0": L.UNIFORME}}, Z, np.array([0, 1]))


def test_tirage_par_inversion_egal_au_juge(J):
    rng = np.random.default_rng(8)
    P = rng.dirichlet(np.ones(3), size=500)
    u = rng.random(500)

    class U:
        def __init__(self, v): self.v = iter(v.tolist())
        def random(self): return next(self.v)
    src = U(u)
    attendu = [J.sp.tirer_categorie(src, list(p)) for p in P.tolist()]
    assert L.tirer_issues_np(P, u).tolist() == attendu


def test_cosinus():
    rng = np.random.default_rng(1)
    base = rng.dirichlet(np.ones(3), size=100)
    a = rng.dirichlet(np.ones(3), size=100)
    assert L.cosinus(a, a, base) == pytest.approx(1.0)
    assert L.cosinus(a, 2 * base - a, base) == pytest.approx(-1.0)
    with pytest.raises(GardeArret):
        L.cosinus(base, a, base)


def test_coupures_et_seuils():
    rng = np.random.default_rng(2)
    for _ in range(500):
        s = L.coupure_archive(rng)
        assert abs(s) >= 0.3 and -1 <= s <= 1 and round(s, 2) == s
        c = L.seuil_decentre(rng, s)
        assert 0.3 <= abs(c) <= 0.8 and abs(c - s) >= 0.3 and round(c, 2) == c


def test_composantes_lois_valides_et_V4_signe_oppose_refuse(J):
    rng = np.random.default_rng(5)
    a = _archive(rng)
    for genre in L.TYPES:
        for dose in L.DOSES[genre]:
            comp = L.tirer_composante(genre, dose, a, rng)
            for f in (1.0, 0.5, 1.5) + (() if genre == "V4" else (-1.0, -0.5)):
                J.sp.valider_loi(comp.loi(f), 3, 2)
    v4 = L.tirer_composante("V4", 0.2, a, rng)
    with pytest.raises(GardeArret):
        v4.loi(-1.0)


def test_direction_bruitee_garde_la_norme_et_doublon_ne_touche_que_les_poids():
    rng = np.random.default_rng(6)
    a = _archive(rng)
    for genre in ("V1", "V2", "V5"):
        comp = L.tirer_composante(genre, 0.4, a, rng)
        cle = "delta" if genre == "V1" else "u"
        b = comp.bruitee(rng)
        d0, d1 = comp.params[cle], b.params[cle]
        assert np.linalg.norm(d1) == pytest.approx(np.linalg.norm(d0))
        assert not np.allclose(d0, d1)
        if genre == "V1":
            assert np.allclose(d1.mean(axis=0), 0)
        else:
            assert d1.mean() == pytest.approx(0, abs=1e-12)
    m = L.tirer_composante("V2", 0.8, a, rng).loi(1.0)
    dbl = L.perturber_poids(m, rng)
    for x, y in zip(L.lois_de(m), L.lois_de(dbl)):
        assert x["biais"] == y["biais"]
        diff = np.abs(np.array(x["poids"]) - np.array(y["poids"]))
        assert 0 < diff.max() < 0.06


def test_cellules_du_texte():
    assert len(L.CELLULES) == 10
    assert [c[0] for c in L.CELLULES] == ["V1", "V1", "V2", "V2", "V3", "V3", "V4", "V4", "V5", "V5"]
    assert [c[2] for c in L.CELLULES] == [0.25, 0.5, 0.4, 0.8, 0.4, 0.8, 0.1, 0.2, 0.4, 0.8]
    assert [c[1] for c in L.CELLULES] == [0, 1] * 5
    assert L.cellule(13) == L.CELLULES[3]


def test_poids_dirichlet_somme_un():
    rng = np.random.default_rng(9)
    for _ in range(200):
        w = L.poids_dirichlet(rng, 5)
        assert abs(sum(w) - 1) <= 1e-9 and all(x >= 0 for x in w)
