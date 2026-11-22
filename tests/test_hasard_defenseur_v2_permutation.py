"""Pièce 2 — noyau de permutation stratifié (garde G1) : cas sain, artefact « unité fausse », aucun repli, graines."""
import itertools

import numpy as np
import pytest

from controle_ia.hasard_defenseur_v2 import permutation_v2 as K
from controle_ia.hasard_defenseur_v2 import puissance_v2 as P
from controle_ia.hasard_defenseur_v2 import registre_v2 as R
from controle_ia.hasard_defenseur_v2.erreurs_v2 import RefusPlan
from controle_ia.hasard_defenseur_v2.puissance_v2 import ETIQUETTES_SIMULEES as ETIQ

ENT = 987654321


def test_enumeration_exacte_egale_a_la_force_brute():
    plan = R.tirer_plan(ENT, ["a", "b"], ETIQ)
    y = np.array([[1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1]], dtype=float)
    tir = K.tirages_du_plan(plan, ENT)
    assert tir.mode == "exact" and tir.m == 90**2
    res = K.tester(y, tir)
    aff = sorted(set(itertools.permutations([0, 0, 1, 1, 2, 2])))

    def T(c0, c1):
        tot = 0.0
        for yy, c in ((y[0], c0), (y[1], c1)):
            c = np.array(c)
            tot += yy[c == 2].mean() - yy[c == 0].mean()
        return tot

    t_obs = T(plan.conditions[0], plan.conditions[1])
    brut = np.mean([T(a, b) >= t_obs - 1e-12 for a in aff for b in aff])
    assert res.p == pytest.approx(brut) and res.t_observe == pytest.approx(t_obs)


def test_seuil_enumeration_trois_taches_exact_quatre_tirees():
    assert K.nb_affectations_par_tache(2) == 90
    assert K.tirages(R.tirer_plan(ENT, list("abc"), ETIQ).conditions, 2, ENT).mode == "exact"
    assert K.tirages(R.tirer_plan(ENT, list("abcd"), ETIQ).conditions, 2, ENT).mode == "tirage"


@pytest.mark.parametrize("rho", [0.0, 0.8])
def test_g1_cas_sain_niveau_a_petite_taille(rho):
    # Taille réduite (300 répliques, 20 tâches, B = 199) : bande à α + 3 erreurs types. La bande gelée (0,061 sur 2 000
    # répliques, N = 300) est jouée par le script des simulations, pas ici.
    r = P.repliques(P.cas_g1(rho, N=120), 300, 11, 0, 199)
    t = P.taux(r, "p_J")
    assert t <= 0.05 + 3 * np.sqrt(0.05 * 0.95 / 300)
    if rho == 0.0:
        assert t >= 0.01


def test_g1_artefact_condition_par_tache_permutee_par_episode():
    # Condition tirée par tâche entière, ρ = 0,8 : le noyau refuse le plan ; une permutation naïve par épisode,
    # ignorant les tâches, rejette très au-dessus de α (démonstration du danger, écrite dans l'essai seulement).
    rng = np.random.default_rng(np.random.SeedSequence(5, spawn_key=(9,)))
    n_t, k = 30, 2
    cond_tache = np.repeat(np.array([0, 1, 2] * (n_t // 3)), 1)
    conditions = np.repeat(cond_tache[:, None], 3 * k, axis=1)
    with pytest.raises(RefusPlan):
        K.tirages(conditions, k, 1)
    rejets = 0
    for _ in range(200):
        c = rng.permutation(cond_tache)
        pt = rng.beta(0.1 * (1 / 0.8 - 1), 0.9 * (1 / 0.8 - 1), n_t)
        y = (rng.random((n_t, 3 * k)) < pt[:, None]).astype(float).ravel()
        lab = np.repeat(c, 3 * k)
        t_obs = y[lab == 2].mean() - y[lab == 0].mean()
        perm = np.array([rng.permutation(lab) for _ in range(199)])
        tb = np.array([y[p == 2].mean() - y[p == 0].mean() for p in perm])
        rejets += (1 + np.sum(tb >= t_obs)) / 200 <= 0.05
    assert rejets / 200 > 0.15


def test_g1_artefact_unite_declaree_differente_du_registre():
    plan = R.tirer_plan(ENT, list("abcde"), ETIQ)
    with pytest.raises(RefusPlan):
        K.tirages_du_plan(plan, ENT, unite="tache", bloc="tout")


def test_aucun_repli_silencieux():
    plan = R.tirer_plan(ENT, list("abcde"), ETIQ)
    tir = K.tirages_du_plan(plan, ENT)
    y = np.zeros(plan.conditions.shape)
    y[0, 0] = np.nan
    with pytest.raises(RefusPlan):
        K.tester(y, tir)
    with pytest.raises(RefusPlan):
        K.tirages_du_plan(plan, ENT, B=999)  # hors simulation
    with pytest.raises(RefusPlan):
        K.tester(np.zeros((4, 6)), tir)
    with pytest.raises(RefusPlan):
        K.p_valeur(1.0, np.zeros(10), "inconnu")


def test_graines_tirages_par_cle_2_reproductibles():
    plan = R.tirer_plan(ENT, list("abcde"), ETIQ)
    t1 = K.tirages_du_plan(plan, ENT, B=199, simulation=True)
    t2 = K.tirages_du_plan(plan, ENT, B=199, simulation=True)
    assert np.array_equal(t1.affectations, t2.affectations)
    rng = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(2,)))
    ref = rng.permuted(np.broadcast_to(plan.conditions, (199, 5, 6)).copy(), axis=2)
    assert np.array_equal(t1.affectations, ref)
    for b in range(5):  # chaque tirage reste un bloc complet par tâche
        assert all(np.bincount(t1.affectations[b, t], minlength=3).tolist() == [2, 2, 2] for t in range(5))


def test_statistique_omnibus():
    plan = R.tirer_plan(ENT, list("abcde"), ETIQ)
    tir = K.tirages_du_plan(plan, ENT)
    y = (plan.conditions == R.D).astype(float)  # dommage sous D seulement : T dirigée nulle, omnibus maximal
    assert K.stat_dirigee(y, tir.observe[None], 2)[0] == 0.0
    assert K.stat_omnibus(y, tir.observe[None], 2)[0] == 5.0
    assert K.tester(y, tir, K.stat_omnibus).p < 0.05
    with pytest.raises(RefusPlan):
        K.tirages(np.full((5, 6), 3), 2, ENT)
