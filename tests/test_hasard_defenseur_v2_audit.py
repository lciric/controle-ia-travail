"""Pièce 7 — simulation d'audit et courbes (§ 5) : cas sain de la figure, pièce corrélée à la condition refusée."""
import numpy as np
import pytest

from controle_ia.hasard_defenseur_v2 import audit_v2 as A
from controle_ia.hasard_defenseur_v2 import monde_v2 as M
from controle_ia.hasard_defenseur_v2 import registre_v2 as R
from controle_ia.hasard_defenseur_v2.erreurs_v2 import RefusAudit
from controle_ia.hasard_defenseur_v2.puissance_v2 import ETIQUETTES_SIMULEES as ETIQ

PIECES = tuple(A.piece_independante(x, 1.0) for x in A.GRILLE_PIQ)


def test_formule_premier_ordre_du_paragraphe_5():
    # 20 sabotages attendus, πq = 0,03 : 0,45 (conditionnelle et uniforme) ; πq = 0,10 : 0,87
    for lam in (0.0, 1.0):
        s_c = A.strategie(lam, A.s_lecture("ii", lam, 300))
        assert A.detection_audit_formule(0.03, 1.0, s_c, 300) == pytest.approx(0.45, abs=0.01)
        assert A.detection_audit_formule(0.10, 1.0, s_c, 300) == pytest.approx(0.87, abs=0.01)


def test_regime_de_signature_une_seule_uniforme():
    plan = R.tirer_plan(1, [f"t{i}" for i in range(2000)], ETIQ, nb_mots_agent=M.NB_MOTS_MONDE)
    s_c = A.strategie(0.0, 0.2)
    y, marque = A.episode_signature(plan, np.full(2000, 0.10), s_c)
    assert np.all(y[marque] == 1.0)  # un dommage marqué est un dommage
    assert not marque[plan.conditions != R.U].any()
    assert y[plan.conditions == R.U].mean() == pytest.approx(0.30, abs=0.02)
    assert y[plan.conditions == R.E].mean() == pytest.approx(0.10, abs=0.015)


def test_cas_sain_de_la_figure_a_petite_taille():
    # 300 répliques à λ = 1 (bande à α + 3 erreurs types), 100 à λ = 0 (lecture ii) ; B = 199. Les seuils gelés
    # (0,061 et 0,93 sur 2 000 répliques, B = 999) se jouent dans le script des simulations.
    c1 = [A.point_courbe(300, 1.0, l, PIECES, 0.0, 31, j, 300, 199) for j, l in enumerate(("i", "ii"))]
    c0 = A.point_courbe(300, 0.0, "ii", PIECES, 0.0, 31, 2, 100, 199)
    for c in c1:
        assert c["permutation"] <= 0.05 + 3 * np.sqrt(0.05 * 0.95 / 300)
    assert c0["permutation"] >= 0.85
    for c in (*c1, c0):
        for p in c["pieces"]:
            assert p["union"] >= p["audit"]  # l'union est au moins l'audit, par construction
            se = np.sqrt(max(p["audit_formule"] * (1 - p["audit_formule"]), 0.01) / c["n_repliques"])
            assert p["audit"] == pytest.approx(p["audit_formule"], abs=4 * se + 0.02)


def test_artefact_piece_correlee_a_la_condition_refusee():
    correlee = A.PieceAudit((0.01, 0.01, 0.10), 1.0)
    with pytest.raises(RefusAudit):
        correlee.verifier()
    with pytest.raises(RefusAudit):
        A.point_courbe(300, 0.0, "ii", (correlee,), 0.0, 31, 0, 2, 99)


def test_aucun_repli_silencieux():
    with pytest.raises(RefusAudit):
        A.s_lecture("iii", 0.0, 300)
    with pytest.raises(RefusAudit):
        A.strategie(1.5, 0.2)
    with pytest.raises(RefusAudit):
        A.piece_independante(1.2, 1.0).verifier()
    with pytest.raises(RefusAudit):
        A.verdict_cas_sain([{"lambda": 0.5, "lecture": "i", "permutation": 0.3}])


def test_graines_audit_cle_distincte():
    plan = R.tirer_plan(9, [f"t{i}" for i in range(3)], ETIQ, nb_mots_agent=M.NB_MOTS_MONDE)
    a = A.tirer_audit(plan, 9)
    ref = np.random.default_rng(np.random.SeedSequence(9, spawn_key=(5, 1))).random((6, 2))
    assert np.array_equal(a[1], ref)
    assert np.array_equal(A.tirer_audit(plan, 9), a)
