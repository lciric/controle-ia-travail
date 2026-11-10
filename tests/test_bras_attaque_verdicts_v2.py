"""Essais de `bras_attaque.verdicts_v2` : un cas sain et un artefact par fonction (règle R5)."""
import numpy as np
import pytest

from controle_ia.bras_attaque import verdicts_v2 as v2
from controle_ia.bras_attaque.verdicts_v1 import fausse_cassure_pire
from controle_ia.gardes import GardeArret


def test_fausse_hausse_pire_petite_et_croissante_avec_les_naifs():
    p_egal, e_egal = v2.fausse_hausse_pire(100, 100, grille=51)
    p_inegal, _ = v2.fausse_hausse_pire(100, 1000, grille=51)
    assert 0.0 < p_egal < 0.01 and 0.0 <= e_egal <= 1.0
    assert p_inegal > p_egal  # des naïfs plus nombreux resserrent leur borne haute : la fausse hausse devient plus facile
    # la cellule ordinaire n'a pas la condition de constitution du témoin : son pire cas est au moins celui du témoin
    assert p_egal >= fausse_cassure_pire(100, grille=51)[0] - 1e-12


def test_fausse_hausse_pire_refuse_un_bras_vide():
    with pytest.raises(GardeArret):
        v2.fausse_hausse_pire(0, 100)


def test_resiste_sous_hausse_cas_extremes():
    assert v2.resiste_sous_hausse(200, 200, 0.1, 0.0) > 0.9
    assert v2.resiste_sous_hausse(200, 200, 0.1, 0.5) < 1e-6
    with pytest.raises(GardeArret):
        v2.resiste_sous_hausse(100, 100, 0.8, 0.3)


def test_resiste_sous_hausse_pire_rend_un_point_de_la_grille():
    naifs = np.linspace(0, 0.5, 11)
    p, e = v2.resiste_sous_hausse_pire(100, 100, 0.10, naifs)
    assert 0.0 <= p <= 1.0 and e in naifs


def test_sans_objet_course_saine():
    assert v2.sans_objet_course_saine(1.0, 0.0, 5) == 0.0
    assert v2.sans_objet_course_saine(0.98, 0.01, 1) == pytest.approx(1 - 0.98 * 0.99)
    with pytest.raises(GardeArret):
        v2.sans_objet_course_saine(0.98, 0.01, 0)


def test_nul_echec_course_saine_petit():
    r = v2.nul_echec_course_saine(1000, 1000, 5, 200, np.random.default_rng(1))
    assert 0.0 <= r["decompte"] <= 0.0101 and r["rang"] <= 0.02
    with pytest.raises(GardeArret):
        v2.nul_echec_course_saine(1000, 1000, 0, 10, np.random.default_rng(1))


def test_fpr_notes_entieres_departage_rend_la_loi_exacte():
    # cas sain : avec départage, la probabilité que le taux réel dépasse 2 % suit la loi exacte (erreur de simulation)
    probas = np.array([0.30, 0.25, 0.18, 0.12, 0.07, 0.04, 0.02, 0.01, 0.005, 0.003, 0.002])
    r = v2.fpr_notes_entieres(200, 2, probas, 0.02, 3000, np.random.default_rng(7))
    assert abs(r["avec_departage"] - r["loi_exacte"]) < 0.03
    # artefact : sans départage, les ex aequo au seuil éloignent du résultat exact
    assert abs(r["sans_departage"] - r["loi_exacte"]) > 0.05


def test_fpr_notes_entieres_refuse_une_loi_invalide():
    with pytest.raises(GardeArret):
        v2.fpr_notes_entieres(200, 2, np.array([0.5, 0.6]), 0.02, 10, np.random.default_rng(0))
