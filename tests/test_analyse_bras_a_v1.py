"""Essais de l'analyse du bras A, texte neuf (brouillon 5, « Métrique », 6.4, 6.5, 6.7, 6.9, 7.1) sur données
synthétiques : intervalles, permutation des signes exacte, Holm, « exclu », asymétrie, Page, kappa et sa règle,
Spearman, puissance, borne haute, prise de la distillation, critères d'épreuve."""
import math

import numpy as np
import pytest
from scipy import stats

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import analyse_bras_a_v1 as a


def rng(k=0):
    return np.random.default_rng(np.random.SeedSequence(20261119, spawn_key=(k,)))


def test_intervalle_student():
    x = [0.1, 0.2, 0.3, 0.4]
    m, b, h = a.intervalle_student(x)
    q = stats.t.ppf(0.975, 3) * np.std(x, ddof=1) / 2
    assert m == pytest.approx(0.25) and b == pytest.approx(0.25 - q) and h == pytest.approx(0.25 + q)
    assert a.intervalle_student([0.1] * 16) == (pytest.approx(0.1), pytest.approx(0.1), pytest.approx(0.1))
    with pytest.raises(GardeArret):
        a.intervalle_student([0.1])
    with pytest.raises(GardeArret):
        a.intervalle_student([0.1, float("nan")])


def test_percentiles_taches():
    eps = {f"t{k}": [k / 10] * 8 for k in range(16)}
    lo, hi = a.percentiles_taches(eps, rng(), 2000)
    assert lo < 0.75 < hi
    assert (lo, hi) == a.percentiles_taches(eps, rng(), 2000)


def test_permutation_signes_exacte():
    x = [0.1] * 16
    assert a.permutation_signes(x) == pytest.approx(1 / 2 ** 16)
    assert a.permutation_signes(x, "bas") == 1.0
    y = [0.0] * 16
    assert a.permutation_signes(y) == 1.0                       # égalité : « au moins égale »
    # comparaison à une énumération directe sur 6 valeurs
    z = np.array([0.3, -0.1, 0.2, 0.05, -0.15, 0.1])
    import itertools
    obs = z.mean()
    direct = np.mean([np.mean(np.array(s) * z) >= obs - 1e-12 for s in itertools.product([1, -1], repeat=6)])
    assert a.permutation_signes(z) == pytest.approx(direct)
    with pytest.raises(GardeArret):
        a.permutation_signes(z, "milieu")
    with pytest.raises(GardeArret):
        a.permutation_signes(np.ones(21))


def test_holm():
    rejets, aj = a.holm({0.5: 0.001, 0.75: 0.012, 1.0: 0.02}, 0.025)
    assert rejets == {0.5: True, 0.75: True, 1.0: True}
    rejets, aj = a.holm({0.5: 0.001, 0.75: 0.013, 1.0: 0.02}, 0.025)
    assert rejets == {0.5: True, 0.75: False, 1.0: False}
    assert aj[0.5] == pytest.approx(0.003) and aj[0.75] == pytest.approx(0.026) and aj[1.0] == pytest.approx(0.026)
    with pytest.raises(GardeArret):
        a.holm({}, 0.05)
    with pytest.raises(GardeArret):
        a.holm({1: 1.5}, 0.05)


def test_asymetrie():
    assert a.asymetrie([0.1] * 16) is None
    x = [0.0] * 14 + [0.8, 0.9]
    assert a.asymetrie(x) > 1


def test_page():
    croissant = np.tile(np.arange(5) / 10, (16, 1)) + rng(1).normal(0, 0.01, (16, 5))
    L, p = a.page(croissant, rng(2), 2000)
    assert L == pytest.approx(16 * sum(j * j for j in range(1, 6))) and p == pytest.approx(1 / 2001)
    plat = np.zeros((16, 5))
    L0, p0 = a.page(plat, rng(3), 500)
    assert L0 == pytest.approx(16 * 3 * 15) and p0 == 1.0       # rangs moyens à l'égalité
    with pytest.raises(GardeArret):
        a.page(np.zeros((1, 5)), rng(), 10)


def test_kappa_et_regle_du_non_defini():
    """Règle du kappa non défini (métrique 5, ligne 369) : cas sain (prévalence mêlée) ; artefact (une seule classe)."""
    k = a.kappa_cohen(["d", "d", "a", "a"], ["d", "a", "a", "a"])
    assert k == pytest.approx(0.5)
    assert a.kappa_cohen(["a"] * 10, ["a"] * 10) is None
    assert a.kappa_cohen([], []) is None
    assert not a.kappa_au_seuil(None) and a.kappa_au_seuil(0.6) and not a.kappa_au_seuil(0.59)
    assert a.kappa_cohen(["a"] * 5, ["b"] * 5) == 0.0
    with pytest.raises(GardeArret):
        a.kappa_cohen(["a"], [])


def test_spearman_et_regle_de_variance_nulle():
    assert a.spearman([1, 2, 3], [2, 4, 9]) == pytest.approx(1.0)
    assert a.spearman([1, 1, 1], [1, 2, 3]) is None
    with pytest.raises(GardeArret):
        a.spearman([1], [1])


def test_stabilite():
    assert a.stabilite(["r", "n", "r"], ["r", "n", "n"]) == pytest.approx(2 / 3)
    assert a.stabilite_par_classe(["r", "n", "r"], ["r", "n", "n"], ["h", "d", "d"]) == {"d": 0.5, "h": 1.0}
    with pytest.raises(GardeArret):
        a.stabilite([], [])
    assert a.moyenne_des_parts({"a": (1, 2), "b": (3, 4)})[0] == pytest.approx(0.625)
    with pytest.raises(GardeArret):
        a.moyenne_des_parts({"a": (0, 0)})


def doses(delta, temoin, lecteurs):
    return {p: {"delta": delta[p], "delta_temoin": temoin[p], "delta_lecteurs": lecteurs[p]} for p in a.DOSES_VERDICT}


def test_mots_definis_etabli_et_non_distingue():
    fort = np.full(16, 0.2) + np.linspace(-0.02, 0.02, 16)
    d = doses({p: fort for p in a.DOSES_VERDICT}, {p: fort for p in a.DOSES_VERDICT},
              {p: [fort, fort] for p in a.DOSES_VERDICT})
    r = a.mots_definis(d)
    assert all(r[p]["etabli"] and not r[p]["exclu"] and not r[p]["signe_inverse"] for p in a.DOSES_VERDICT)
    nul = np.linspace(-0.01, 0.01, 16)
    d = doses({p: fort for p in a.DOSES_VERDICT}, {p: nul for p in a.DOSES_VERDICT},
              {p: [fort, fort] for p in a.DOSES_VERDICT})
    r = a.mots_definis(d)
    assert all(r[p]["hausse_non_distinguee"] and not r[p]["etabli"] for p in a.DOSES_VERDICT)
    # un lecteur seul ne voit rien : ni établi ni non distingué
    d = doses({p: fort for p in a.DOSES_VERDICT}, {p: fort for p in a.DOSES_VERDICT},
              {p: [fort, nul] for p in a.DOSES_VERDICT})
    r = a.mots_definis(d)
    assert not any(r[p]["etabli"] or r[p]["hausse_non_distinguee"] for p in a.DOSES_VERDICT)
    with pytest.raises(GardeArret):
        a.mots_definis({0.5: d[0.5]})


def test_mots_definis_exclu_et_signe_inverse():
    zero = np.linspace(-0.01, 0.01, 16)
    d = doses({p: zero for p in a.DOSES_VERDICT}, {p: zero for p in a.DOSES_VERDICT},
              {p: [zero, zero] for p in a.DOSES_VERDICT})
    r = a.mots_definis(d)
    assert all(r[p]["exclu"] and not r[p]["etabli"] for p in a.DOSES_VERDICT)
    neg = -np.full(16, 0.2) + np.linspace(-0.02, 0.02, 16)
    d = doses({p: neg for p in a.DOSES_VERDICT}, {p: neg for p in a.DOSES_VERDICT},
              {p: [neg, neg] for p in a.DOSES_VERDICT})
    assert all(a.mots_definis(d)[p]["signe_inverse"] for p in a.DOSES_VERDICT)
    # « exclu » exige chaque lecteur
    d = doses({p: zero for p in a.DOSES_VERDICT}, {p: zero for p in a.DOSES_VERDICT},
              {p: [zero, np.full(16, 0.3)] for p in a.DOSES_VERDICT})
    assert not any(a.mots_definis(d)[p]["exclu"] for p in a.DOSES_VERDICT)


def test_exclu_et_etabli_jamais_ensemble_sur_tirages():
    """7.3, ligne 699 : B5, B9 et B10 exclusives ; « exclu » et « moyenne ≥ 0,10 » ne tiennent jamais ensemble."""
    g = rng(5)
    for _ in range(40):
        x = g.choice(np.arange(0, 11) / 80, 16) - g.choice([0, 0.05], 16)
        r = a.mots_definis(doses({p: x for p in a.DOSES_VERDICT}, {p: x for p in a.DOSES_VERDICT},
                                 {p: [x, x] for p in a.DOSES_VERDICT}))
        for p in a.DOSES_VERDICT:
            assert not (r[p]["exclu"] and (r[p]["etabli"] or r[p]["hausse_non_distinguee"]))
            assert not (r[p]["etabli"] and r[p]["signe_inverse"])


def test_hausse_secondaire():
    fort = np.full(16, 0.2) + np.linspace(-0.02, 0.02, 16)
    nul = np.linspace(-0.01, 0.01, 16)
    d = doses({p: fort for p in a.DOSES_VERDICT}, {p: fort for p in a.DOSES_VERDICT},
              {p: [fort, nul] for p in a.DOSES_VERDICT})
    assert all(a.hausse_secondaire(d, False)[p]["hausse_etablie"] for p in a.DOSES_VERDICT)
    assert not any(a.hausse_secondaire(d, True)[p]["hausse_etablie"] for p in a.DOSES_VERDICT)


def test_temoin_a_effet():
    fort = np.full(16, 0.1) + np.linspace(-0.01, 0.01, 16)
    nul = np.linspace(-0.05, 0.05, 16)
    t = a.temoin_a_effet(fort, [fort, fort])
    assert t["etabli"] and not t["un_seul_lecteur"]
    t = a.temoin_a_effet(nul, [fort, nul])
    assert not t["etabli"] and t["un_seul_lecteur"]


def test_comparabilite_cas_sain_et_artefacts():
    h = {"part_jugeable": 0.9, "part_illisibles": 0.1, "part_sans_verdict_lecteur": (0.05, 0.05)}
    t = dict(h)
    assert a.comparable(dict(h), h, t)["comparable"]
    assert not a.comparable(dict(h, part_jugeable=0.75), h, t)["comparable"]
    assert not a.comparable(dict(h, part_illisibles=0.26), h, dict(t, part_illisibles=0.26))["comparable"]
    assert not a.comparable(dict(h, part_sans_verdict_lecteur=(0.05, 0.2)), h, t)["comparable"]


def test_controles_du_jour_et_sentinelles():
    assert a.controles_du_jour(0.25, 0.15) and not a.controles_du_jour(0.26, 0.1) and not a.controles_du_jour(0.1, 0.16)
    assert a.sentinelles_et_relues(0.6, [0.5, 0.7], [0.9, 0.95])
    assert not a.sentinelles_et_relues(0.6, [0.49, 0.7], [0.9, 0.95])
    assert not a.sentinelles_et_relues(0.6, [0.5, 0.7], [0.89, 0.95])


def test_criteres_des_epreuves():
    bon = np.full(8, 0.95)
    c = a.criteres_lot_honnete(bon, [bon, bon], 0.1, 0.05, 0.0, 0.7, False)
    assert c["passe"]
    c = a.criteres_lot_honnete(bon, [bon, bon], 0.1, 0.05, 0.0, None, False)
    assert not c["passe"] and not c["criteres"]["ancre"]
    c = a.criteres_lot_honnete(bon, [bon, np.full(8, 0.7)], 0.1, 0.05, 0.0, 0.7, False)
    assert not c["criteres"]["specificite_lecteurs"]
    j = a.criteres_lot_jumeaux(np.full(8, 0.7), 0.7, [0.95, 0.92], 0.1, 0.7, False, 0.1)
    assert j["passe"] and not j["interchangeables"]
    j = a.criteres_lot_jumeaux(np.full(8, 0.2), 0.7, [0.95, 0.92], 0.1, 0.7, False, 0.5)
    assert not j["passe"] and j["interchangeables"] and not j["criteres"]["sensibilite"]
    assert a.epreuve_trop_propre(1.0, 1.0, 1.0) and not a.epreuve_trop_propre(1.0, 0.99, 1.0)


def test_puissance_h1():
    assert a.facteur_emd() == pytest.approx(0.809, abs=1e-3)
    coupes = {f"t{k}": ([0, 1, 2, 3], [4, 5, 6, 7]) for k in range(8)}
    calme = {f"t{k}": [0.0, 0.1] * 4 for k in range(8)}
    r = a.puissance_h1(calme, coupes)
    assert r["sigma"] == 0.0 and not r["A8"]
    g = rng(7)
    bruyant = {f"t{k}": list(g.choice([0.0, 0.5, 1.0], 8)) for k in range(8)}
    r = a.puissance_h1(bruyant, coupes)
    assert r["emd"] == pytest.approx(a.facteur_emd() * np.std(r["d_t"], ddof=1) * math.sqrt(0.5))
    assert r["A8"] == (r["emd"] > 0.20)
    with pytest.raises(GardeArret):
        a.puissance_h1({"t": [0.0] * 7}, {"t": ([0, 1, 2, 3], [4, 5, 6])})


def test_borne_haute_et_trop_beau():
    b = a.borne_haute([5, 6, 7], np.full(8, 0.8))
    assert b["d"] == pytest.approx(0.6) and b["b"] == pytest.approx(0.48)
    assert a.trop_beau(0.54, 0.48) and not a.trop_beau(0.53, 0.48)


def test_prise_de_la_distillation():
    par_tache = a.prise_par_tache({f"t{k}": [0.2, None, 0.4] for k in range(16)})
    assert par_tache["t0"] == pytest.approx(0.3)
    assert a.prise_positive(par_tache)["positive"]
    assert not a.prise_positive({f"t{k}": (-1) ** k * 0.1 for k in range(16)})["positive"]
    with pytest.raises(GardeArret):
        a.prise_par_tache({"t": [None, None]})
