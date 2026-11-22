"""Pièce 3 — monde planté (trois organismes) : taux retrouvés à la graine ; graine partagée entre tâches refusée."""
import dataclasses

import numpy as np
import pytest

from controle_ia.hasard_defenseur_v1 import monde_v1 as M
from controle_ia.hasard_defenseur_v1 import registre_v1 as R
from controle_ia.hasard_defenseur_v1.erreurs_v1 import RefusGraine, RefusPlan
from controle_ia.hasard_defenseur_v1.puissance_v1 import ETIQUETTES_SIMULEES as ETIQ

ENT_R, ENT_M = 31415, 27182


def _plan(n_t=1500):
    return R.tirer_plan(ENT_R, [f"t{i}" for i in range(n_t)], ETIQ, nb_mots_agent=M.NB_MOTS_MONDE)


@pytest.fixture(scope="module")
def plan():
    return _plan()


def _p(**kw):
    base = dict(p0=0.10, rho=0.0, delta=0.15, r=0.5, delta_J=0.10)
    base.update(kw)
    return M.ParametresMonde(**base)


def test_taux_retrouves_a_la_graine(plan):
    m = M.simuler_monde(plan, ENT_M, _p())
    c = plan.conditions
    se = np.sqrt(0.25 * 0.75 / 3000)
    assert m.Y["saboteur"][c == R.U].mean() == pytest.approx(0.10 + 0.5 * 0.15, abs=4 * se)
    assert m.Y["saboteur"][c == R.E].mean() == pytest.approx(0.10, abs=4 * se)
    assert m.Y["jumeau_insensible"][c == R.U].mean() == pytest.approx(0.10, abs=4 * se)
    assert m.Y["jumeau_sensible"][c == R.U].mean() == pytest.approx(0.20, abs=4 * se)
    assert m.Y["jumeau_sensible"][c == R.D].mean() == pytest.approx(0.10, abs=4 * se)
    assert m.percu[c == R.U].mean() == pytest.approx(0.5, abs=0.03) and not m.percu[c != R.U].any()
    assert m.sonde["saboteur"][c == R.U].mean() == pytest.approx(0.5, abs=0.06)
    assert m.sonde["jumeau_insensible"][c == R.U].mean() == pytest.approx(0.0, abs=0.06)
    assert m.trait["jumeau_sensible"][c == R.U].mean() == pytest.approx(0.5, abs=0.04)
    assert m.trait["jumeau_insensible"][c == R.U].mean() == pytest.approx(0.2, abs=0.04)
    # même graine : mêmes issues
    m2 = M.simuler_monde(plan, ENT_M, _p())
    assert all(np.array_equal(m.Y[o], m2.Y[o]) for o in M.ORGANISMES)


def test_correlation_intra_tache_plantee():
    p_t = M.taux_taches(ENT_M, np.arange(4000), 0.10, 0.3)
    assert p_t.mean() == pytest.approx(0.10, abs=0.01)
    # corrélation intra-tâche d'une Bernoulli de taux Bêta : var(p_t) / (p0 (1 − p0))
    assert p_t.var() / (0.1 * 0.9) == pytest.approx(0.3, abs=0.04)
    assert np.all(M.taux_taches(ENT_M, np.arange(10), 0.10, 0.0) == 0.10)


def test_artefact_graine_partagee_entre_taches_refusee(plan):
    petit = _plan(4)
    with pytest.raises(RefusGraine):
        M.simuler_monde(dataclasses.replace(petit, numeros=np.array([0, 1, 1, 3])), ENT_M, _p())
    graines = [list(l) for l in petit.graines]
    graines[2][0] = graines[0][0]
    with pytest.raises(RefusGraine):
        M.simuler_monde(dataclasses.replace(petit, graines=graines), ENT_M, _p())
    with pytest.raises(RefusGraine):
        R.verifier_plan_structure(dataclasses.replace(petit, graines=graines))


def test_aucun_repli_silencieux():
    petit = R.tirer_plan(ENT_R, ["a", "b"], ETIQ)  # sans mots d'agent
    with pytest.raises(RefusGraine):
        M.simuler_monde(petit, ENT_M, _p())
    with pytest.raises(RefusPlan):
        M.simuler_monde(_plan(2), ENT_M, _p(delta=1.5))
    with pytest.raises(RefusPlan):
        M.simuler_monde(_plan(2), ENT_M, _p(rho=1.0))
    with pytest.raises(RefusGraine):
        M.simuler_monde(_plan(2), None, _p())


def test_graines_cles_distinctes_monde_agent_conditions(plan):
    # p_t par la clé (3, t) de l'entropie du monde
    a, b = 0.1 * (1 / 0.3 - 1), 0.9 * (1 / 0.3 - 1)
    ref = [np.random.default_rng(np.random.SeedSequence(ENT_M, spawn_key=(3, t))).beta(a, b) for t in range(5)]
    assert np.allclose(M.taux_taches(ENT_M, np.arange(5), 0.10, 0.3), ref)
    # changer l'entropie du monde ne change ni les conditions ni le hasard de l'agent
    m1 = M.simuler_monde(plan, ENT_M, _p(rho=0.3))
    m2 = M.simuler_monde(plan, ENT_M + 1, _p(rho=0.3))
    assert not np.allclose(m1.p_t, m2.p_t)
    assert np.array_equal(m1.percu, m2.percu)
    # uniformes indépendantes entre organismes ; variante « uniformes communes » à part
    u = M.uniformes(plan.mots_agent)
    assert abs(np.corrcoef(u[..., M.MOT_DOMMAGE["saboteur"]].ravel(), u[..., M.MOT_DOMMAGE["jumeau_sensible"]].ravel())[0, 1]) < 0.03
    mc = M.simuler_monde(plan, ENT_M, _p(uniformes_communes=True, delta=0.0, r=1.0, delta_J=0.0))
    assert np.array_equal(mc.Y["saboteur"], mc.Y["jumeau_insensible"])
    mi = M.simuler_monde(plan, ENT_M, _p(delta=0.0, r=1.0, delta_J=0.0))
    assert not np.array_equal(mi.Y["saboteur"], mi.Y["jumeau_insensible"])
