"""Essais du rejeu des bras de l'idée 1.2 : gardes d'accès et de budget, règles des bras, valeur e, e-BH, vérificateur."""
import math
from unittest import mock

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B
from controle_ia.organisme_idees_juge import juge_v1
from controle_ia.organisme_idees_juge import mutations_v1 as MU
from controle_ia.organisme_idees_juge import rejeu_v1 as R

RAC = MU.RACINE_ESSAI


@pytest.fixture(scope="module")
def J():
    return juge_v1.charger()


def _ev(lw):
    return {i: B.EvaluationFiltree([round(float(v), 6) for v in t]) for i, t in enumerate(lw)}


def _hasard(graine, derive=-0.05, ecart=0.6):
    rng = np.random.default_rng(graine)
    return np.cumsum(rng.normal(derive, ecart, (24, 32)), axis=1)


def test_vue_garde_d_acces_cas_sain_et_artefact():
    v = R.Vue(list(range(32)))
    assert v.reveler() == 0 and v.lire(0) == 0 and v.courante() == 0
    with pytest.raises(GardeArret, match="non révélé"):
        v.lire(1)
    for _ in range(31):
        v.reveler()
    with pytest.raises(GardeArret, match="plafond"):
        v.reveler()
    with pytest.raises(GardeArret):
        R.Vue([0.0] * 31)


def test_budget_cas_sain_et_artefact():
    b = R.Budget(2)
    b.prendre(); b.prendre()
    assert b.reste == 0
    with pytest.raises(GardeArret, match="budget"):
        b.prendre()


def test_ordre_du_tour():
    pos = list(np.random.default_rng(1).permutation(24))
    o0, o1 = R.ordre_du_tour(pos, 0), R.ordre_du_tour(pos, 1)
    assert [pos[i] for i in o0] == list(range(24))
    assert o1 == o0[1:] + o0[:1]


def test_arrets_bas_seulement_apres_50_tirages_et_haut_des_25():
    v = R.Vue([-3.5, -1.0] + [0.0] * 30)
    v.reveler()
    assert not R.arretee_bas(v)          # sous 1/20 à 25 tirages seulement : pas d'arrêt
    v.reveler()
    assert not R.arretee_bas(v)
    w = R.Vue([-1.0, -3.5] + [0.0] * 30)
    w.reveler(); w.reveler()
    assert R.arretee_bas(w)
    h = R.Vue([R.SEUIL_HAUT] + [0.0] * 31)
    h.reveler()
    assert R.arretee_haut(h)


def test_bras_sur_trajectoires_d_essai(J):
    ev = MU.evaluations_essai()
    pos = MU.positions_essai()
    res = R.rejouer_generation(J, ev, pos, RAC, "N", 0)
    assert set(res) == set(R.BRAS_N)
    assert res["F"]["blocs"] == [8] * 24 and res["F"]["tirages"] == 4800
    assert res["F125"]["blocs"] == [10] * 24 and res["F125"]["tirages"] == 6000
    assert res["F-arret"]["blocs"][0] == 1 and res["F-arret"]["blocs"][1] == 2 and res["F-arret"]["blocs"][2] == 8
    assert res["A"]["blocs"][0] == 1 and res["A"]["arrets"][0] == "haut"
    assert max(res["A"]["blocs"]) == 32 and res["A"]["arrets"][res["A"]["blocs"].index(32)] == "plafond"
    for nom in ("F-arret", "A", "P", "P-prime", "G"):
        assert res[nom]["tirages"] <= 4800
    assert res["P"]["tirages"] >= res["A"]["tirages"]
    assert all(n >= 2 for n in res["G"]["blocs"])
    assert R.rejouer_generation(J, ev, pos, RAC, "T", 0).keys() == set(R.BRAS_T)


@pytest.mark.parametrize("graine", range(40))
def test_verificateur_independant_et_proprietes(J, graine):
    lw = _hasard(graine, derive=[-0.2, -0.05, 0.05, 0.2][graine % 4])
    ev = _ev(lw)
    pos = [int(p) for p in np.random.default_rng(100 + graine).permutation(24)]
    res = R.rejouer_generation(J, ev, pos, RAC, "N", graine)     # le vérificateur indépendant est joué à chaque bras
    assert res["P"]["tirages"] >= res["A"]["tirages"]            # P consomme au moins autant que A ([CL] m1)
    assert res["P-prime"]["tirages"] >= res["A"]["tirages"]
    for nom, r in res.items():
        for i in range(24):
            assert r["log_e"][i] == R.log_valeur_e(tuple(ev[i]["trajectoire_log_w"][:r["blocs"][i]]))


def test_placebo_reproductible_depuis_sa_graine(J):
    ev, pos = _ev(_hasard(3)), MU.positions_essai()
    a = R.jouer_bras(J, "P", ev, pos, RAC, 0, 7)
    b = R.jouer_bras(J, "P", ev, pos, RAC, 0, 7)
    assert a == b


def test_valeur_e_egale_au_juge_et_ebh_seconde_ecriture(J):
    rng = np.random.default_rng(4)
    for k in range(200):
        lw = np.cumsum(rng.normal(0.15 * (k % 3), 1.0, (24, 32)), axis=1).round(6)
        n = rng.integers(1, 33, 24)
        rev = [tuple(float(x) for x in lw[i, :n[i]]) for i in range(24)]
        promues, m, le_juge = R.promotions_ebh(J, rev)
        assert m == 24
        le = [R.log_valeur_e(r) for r in rev]
        assert all(abs(round(le[i], 6) - le_juge[i]) <= 1e-9 for i in range(24))
        assert R.ebh_independant(le) == promues


def test_garde_m_fixe_cas_sain_et_artefact(J):
    ev, pos = MU.evaluations_essai(), MU.positions_essai()
    R.jouer_bras(J, "A", ev, pos, RAC, 0, 0)
    vrai = R.promotions_ebh
    with mock.patch.object(R, "promotions_ebh", lambda JJ, rev: (vrai(JJ, rev)[0], 23, vrai(JJ, rev)[2])):
        with pytest.raises(GardeArret, match="m compté après coup"):
            R.jouer_bras(J, "A", ev, pos, RAC, 0, 0)


def test_garde_du_budget_dans_le_rejeu(J):
    ev, pos = MU.evaluations_lentes(), MU.positions_essai()
    assert R.jouer_bras(J, "A", ev, pos, RAC, 0, 0)["tirages"] == 4800
    with mock.patch.dict(R.BRAS, {"A": (MU._A_sans_budget, R.BUDGET_BLOCS)}):
        with pytest.raises(GardeArret, match="tirages donnés > budget"):
            R.jouer_bras(J, "A", ev, pos, RAC, 0, 0)
    with mock.patch.dict(R.BRAS, {"F125": (lambda v, p, b, rng=None: R.bras_F(v, p, b, blocs=11), R.BUDGET125_BLOCS)}):
        with pytest.raises(GardeArret, match="tirages donnés > budget \\(6000\\)"):
            R.jouer_bras(J, "F125", ev, pos, RAC, 0, 0)


def test_bras_G_glouton(J):
    lw = np.zeros((24, 32))
    lw[7] = np.linspace(0.1, 3.0, 32)        # la meilleure courante reçoit tous les blocs libres jusqu'au plafond
    lw[9] = np.linspace(0.05, 2.0, 32)
    res = R.jouer_bras(J, "G", _ev(lw), list(range(24)), RAC, 0, 0)
    assert res["blocs"][7] == 32 and res["blocs"][9] == 32
    assert sum(res["blocs"]) == 192
