"""Tests for dynamique_gradient_evasion_v1 (guards tested on a sound case and on an artefact)."""
import math
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dynamique_gradient_evasion_v1 as m  # noqa: E402

P = np.array([0.85, 0.14, 0.01]); BETA = np.array([1.0, 0.05, 0.75])


def test_closed_form_matches_integration():
    for op in ("none", "A", "B"):
        r = m.effective_rewards(op, 1.0, BETA, 2.5, 3.0)
        assert np.max(np.abs(m.npg_closed_form(P, r, 3.0, 2.0)[0] - m.npg_integrate(P, r, 3.0, 2.0, 1e-3))) < 1e-10


def test_closed_form_detects_wrong_path():  # artefact: a wrong lambda(t) must be caught by the same comparison
    r = m.effective_rewards("B", 1.0, BETA, 2.5, 3.0)
    wrong = m.softmax(np.log(P) + 2.0 * r)  # lambda*eta replaced by t (no KL saturation)
    assert np.max(np.abs(wrong - m.npg_integrate(P, r, 3.0, 2.0, 1e-3))) > 1e-3


def test_fixed_point_is_gibbs():
    r = m.effective_rewards("A", 1.0, BETA, 0.0, 3.0)
    far = m.npg_closed_form(P, r, 3.0, 300.0)[0]
    assert np.allclose(far, m.softmax(np.log(P) + 3.0 * r), atol=1e-12)
    assert np.allclose(m.softmax(np.log(P) + 3.0 * r), BETA * P * np.exp(3.0 * np.array([0, 1, 1])) / np.sum(BETA * P * np.exp(3.0 * np.array([0, 1, 1]))))


def test_dominance_time_formula_and_infinite_case():
    t = m.dominance_time(0.01, 0.85, 1.0, 0.0, 8.0)
    assert math.isfinite(t)
    pi = m.npg_closed_form(P, np.array([0.0, 1.0, 1.0]), 8.0, [t - 1e-6, t + 1e-6])
    assert pi[0, 2] < pi[0, 0] and pi[1, 2] > pi[1, 0]
    assert m.dominance_time(0.01, 0.85, 0.3, 0.0, 3.0) == float("inf")  # eta*d <= log(p_h/p_f)


def test_rft_compounding_exact_and_threshold():
    R = np.array([0.0, 1.0, 1.0])
    tr = m.rft_rounds(P, BETA, R, lambda r: np.exp(0.2 * r), 30)
    slope = 0.2 - math.log(1 / 0.75)
    assert slope < 0
    assert np.all(tr[:, 2] < tr[:, 0])
    assert m.rft_dominance_round(0.01, 0.85, 0.75, 1.0, math.exp(0.2)) is None
    k = m.rft_dominance_round(0.01, 0.85, 0.75, 1.0, math.exp(0.5))
    tr = m.rft_rounds(P, BETA, R, lambda r: np.exp(0.5 * r), k)
    assert tr[k, 2] > tr[k, 0] and tr[k - 1, 2] <= tr[k - 1, 0]


def test_discard_pg_lower_bound():
    R = np.array([0.0, 1.0, 1.0])
    _, traj = m.discard_pg_integrate(P, BETA, R, 10.0, 1e-3, record=50)
    for t, pi in traj:
        assert math.log(pi[2] / pi[0]) >= math.log(P[2] / P[0]) + 0.75 * t - 1e-9


def test_two_channel_equilibria_and_types():
    eqs = m.two_channel_equilibria(m.BASE_2CH)
    assert [e["type"] for e in eqs] == ["stable", "saddle", "stable"]
    for e in eqs:
        gu, gw = m.two_channel_field(e["u"], e["w"], m.BASE_2CH)
        assert abs(gu) < 1e-8 and abs(gw) < 1e-8
    assert eqs[2]["J"] > eqs[0]["J"]  # stealth node is the global optimum ...
    u, w, _ = m.two_channel_flow(m.BASE_2CH["u0"], m.BASE_2CH["w0"], m.BASE_2CH, 200.0, 0.01)
    assert m.sigmoid(u) < 0.01 and m.sigmoid(w) < 0.05  # ... yet the base model flows to the honest node


def test_certificate_sound_case_and_artefact():
    par = dict(m.BASE_2CH, kappa=0.25, C=1.0, eta=8.0)
    ok, ubar = m.order_interval_certificate(par)
    assert ok
    u, w, tr = m.two_channel_flow(par["u0"], par["w0"], par, 100.0, 0.01, record=10)
    assert all(a <= ubar + 1e-9 and b <= par["w0"] + 1e-9 for _, a, b in tr)
    bad = dict(m.BASE_2CH, kappa=0.05, C=0.0, eta=20.0)  # artefact: stealth reachable -> certificate must fail
    assert not m.order_interval_certificate(bad)[0]
    u, w, _ = m.two_channel_flow(bad["u0"], bad["w0"], bad, 400.0, 0.02)
    assert m.sigmoid(u) > 0.5 and m.sigmoid(w) > 0.5


def test_guards_fire():
    with pytest.raises(m.GuardError):
        m.effective_rewards("A", 1.0, np.array([1.0, 0.0, 0.5]), 0.0, 1.0)
    with pytest.raises(m.GuardError):
        m.logit(np.array([0.0]))
    with pytest.raises(m.GuardError):
        m.two_channel_stochastic(m.BASE_2CH, 1, 1, 0.1, m.child_rng("t"))
    with pytest.raises(m.GuardError):
        m.check_probability_vector([0.5, 0.6])
    m.check_probability_vector([0.5, 0.5])


def test_stochastic_unbiased_large_batch_tracks_meanfield():
    par = dict(m.BASE_2CH, eta=20.0, C=0.1)
    q, s = m.two_channel_stochastic(par, 256, 8000, 0.5, m.child_rng("t2"))
    assert q > 0.9 and s > 0.9


def test_seeds_reproducible():
    a = m.child_rng("x").random(3); b = m.child_rng("x").random(3); c = m.child_rng("y").random(3)
    assert np.array_equal(a, b) and not np.array_equal(a, c)
