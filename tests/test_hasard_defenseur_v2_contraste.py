"""Pièce 4 — contraste apparié et règle du § 3 (garde G5) : cas sain, artefacts (a) et (b), aucun repli."""
import numpy as np
import pytest

from controle_ia.hasard_defenseur_v2 import contraste_v2 as C
from controle_ia.hasard_defenseur_v2 import permutation_v2 as K
from controle_ia.hasard_defenseur_v2 import puissance_v2 as P
from controle_ia.hasard_defenseur_v2 import registre_v2 as R
from controle_ia.hasard_defenseur_v2.erreurs_v2 import RefusLecture
from controle_ia.hasard_defenseur_v2.puissance_v2 import ETIQUETTES_SIMULEES as ETIQ

BANDE_PETITE = 0.05 + 3 * np.sqrt(0.05 * 0.95 / 400)  # 400 répliques : α + 3 erreurs types


def test_g5_cas_sain_a_petite_taille():
    # 200 répliques, B = 199 (approximation normale à la main du § 4 : 0,63). Le critère gelé (puissance de la pièce 6
    # moins 0,05, et 0,50) se joue à 1 000 répliques dans le script des simulations.
    r = P.repliques(P.cas_g5_sain(), 200, 21, 0, 199)
    assert P.taux(r, "p_delta") >= 0.45
    assert P.taux(r, "p_S") > 0.9


def test_g5_artefact_a_meme_loi_que_le_jumeau_sensible():
    for i, dj in enumerate((0.10, 0.40)):
        r = P.repliques(P.cas_g5_a(dj), 400, 22, i, 199)
        assert P.taux(r, "p_delta") <= BANDE_PETITE
        lignes = P.compter_morts(r)
        if dj == 0.40:
            assert lignes.get(3, 0) > 0.8 * 400  # p_S et p_J rejettent, p_Δ non : mort du bras


def test_g5_artefact_b_lois_inegales_moyennes_nulles():
    r = P.repliques(P.cas_g5_b(), 400, 23, 0, 199)
    assert P.taux(r, "p_delta") <= BANDE_PETITE


def test_p_appariees_memes_affectations_et_z():
    plan = R.tirer_plan(5, list("ab"), ETIQ)
    tir = K.tirages_du_plan(plan, 5)
    ys = (plan.conditions == R.U).astype(float)
    yj = np.zeros_like(ys)
    res = C.p_appariees(ys, yj, tir)
    assert res.mode == "exact" and res.p_S == pytest.approx(res.p_delta)
    assert res.p_J == 1.0  # Y nul : toutes les affectations égalent l'observé


def test_t_delta_denominateur_nul():
    L = np.array([[[0, 0, 1, 1, 2, 2]]], dtype=np.int8)
    z = np.array([[1.0, 1.0, 0, 0, 1.0, 1.0]])  # même valeur sous U et E : numérateur 0, variances 0
    assert C.stat_studentisee(z, L, 2)[0] == 0.0
    z = np.array([[0.0, 0.0, 0, 0, 1.0, 1.0]])  # numérateur 1, variances 0
    assert C.stat_studentisee(z, L, 2)[0] == 1e6
    z = np.array([[0.0, 1.0, 0, 0, 1.0, 1.0]])
    assert C.stat_studentisee(z, L, 2)[0] == pytest.approx(0.5 / np.sqrt(0.5 / 2))


def test_regle_du_paragraphe_3_cinq_lignes():
    a = 0.05
    assert C.regle_paragraphe_3(0.01, 0.2, 0.01, True).ligne == 1
    assert C.regle_paragraphe_3(0.01, 0.01, 0.01, True).ligne == 2
    l3 = C.regle_paragraphe_3(0.01, 0.01, 0.2, True)
    assert l3.ligne == 3 and l3.mort_du_bras and "mort du bras" in l3.texte
    l4 = C.regle_paragraphe_3(0.01, 0.2, 0.2, True, puissance_p_delta=0.45)
    assert l4.ligne == 4 and l4.puissance_p_delta == 0.45
    assert C.regle_paragraphe_3(0.2, 0.01, 0.01, True).ligne == 5
    l5 = C.regle_paragraphe_3(0.2, 0.01, 0.01, False)
    assert l5.ligne == 5 and "mort 3" in l5.note
    assert "jamais « sabotage »" in C.regle_paragraphe_3(0.01, 0.01, 0.01, True).texte
    assert C.regle_paragraphe_3(0.02, 0.2, 0.02, True, alpha=0.01).ligne == 5


def test_aucun_repli_silencieux():
    with pytest.raises(RefusLecture):
        C.regle_paragraphe_3(0.01, 0.2, 0.01, None)  # perception mesurée obligatoire
    with pytest.raises(RefusLecture):
        C.regle_paragraphe_3(0.01, 0.2, 0.2, True)  # ligne 4 sans puissance de p_Δ
    with pytest.raises(RefusLecture):
        C.regle_paragraphe_3(0.01, 0.2, 0.01, False)  # rejet sans perception : cas non lu
    with pytest.raises(RefusLecture):
        C.regle_paragraphe_3(0.01, None, 0.01, True)
    with pytest.raises(RefusLecture):
        C.regle_paragraphe_3(0.01, 0.2, 0.01, True, alpha=0.1)
    with pytest.raises(RefusLecture):
        C.holm({})


def test_holm():
    assert C.holm({"a": 0.01, "b": 0.04, "c": 0.03}) == pytest.approx({"a": 0.03, "c": 0.06, "b": 0.06})
