"""Tests for experience_jouet_decouplage_sonde_v1 (sound case and artefact for each guard)."""
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import experience_jouet_decouplage_sonde_v1 as m  # noqa: E402


def test_auc_basic_and_ties():
    assert m.auc([2, 3], [0, 1]) == 1.0 and m.auc([0, 1], [2, 3]) == 0.0
    assert m.auc([1, 1], [1, 1]) == 0.5


def test_stein_shift_matches_and_orthogonal_is_zero():
    r = m.selection_gaussian(m.child_rng("t-sel"), 400000, True)
    for k in ("aligned", "sigma_orthogonal", "random"):
        assert r[k]["abs_diff"] < 6 * r[k]["mc_se"] + 1e-12
    assert abs(r["sigma_orthogonal"]["stein_prediction"]) < 1e-12
    # artefact: the non-Gaussian counterexample must show a large shift despite ~zero covariance
    c = r["nongaussian_counterexample"]
    assert abs(c["shift_mc"]) > 20 * c["mc_se"] and abs(c["cov_z_s"]) < 0.02


def _setup(kind, placement):
    rng = m.child_rng("t-net")
    xc, xh, M0 = m.make_task(rng, 600)
    W, U, w, a, b = m.heads(m.child_rng(f"t-h-{kind}-{placement}"), M0, xc, xh, kind, placement)
    return xc, xh, M0, W, U, w, a, b


def test_disjoint_exact_invariance_relu():
    xc, xh, M0, W, U, w, a, b = _setup("relu", "disjoint")
    log, _, _ = m.train(xc, xh, M0, W, U, w, a, b, "relu", 150, lr=0.5)
    assert log[-1]["max_abs_probe_change"] == 0.0
    assert log[-1]["filter_catch_rate_cheat"] < log[0]["filter_catch_rate_cheat"]  # the filter is being evaded


def test_orthogonal_linear_invariant_relu_moves():
    xc, xh, M0, W, U, w, a, b = _setup("linear", "orthogonal_shared")
    assert np.linalg.norm(W @ w) < 1e-12
    log, _, _ = m.train(xc, xh, M0, W, U, w, a, b, "linear", 150, lr=0.5)
    assert log[-1]["max_abs_probe_change"] < 1e-9
    xc, xh, M0, W, U, w, a, b = _setup("relu", "orthogonal_shared")
    log, _, _ = m.train(xc, xh, M0, W, U, w, a, b, "relu", 150, lr=0.5)
    assert log[-1]["max_abs_probe_change"] > 1e-4


def test_trainable_head_recruits_probe():
    xc, xh, M0, W, U, w, a, b = _setup("relu", "disjoint")
    log, _, _ = m.train(xc, xh, M0, W, U, w, a, b, "relu", 150, lr=0.5, train_head=True, head_lr=0.5)
    assert log[0]["coupling_norm_Ww"] == 0.0 and log[-1]["coupling_norm_Ww"] > 1e-3


def test_guards():
    with pytest.raises(m.GuardError):
        _setup("relu", "nonsense")
