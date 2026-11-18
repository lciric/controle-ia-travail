"""Statistiques de l'étude des formulations du contraste à témoin apparié : valeurs exactes et propriétés."""
import numpy as np
import pytest
from scipy import stats

from controle_ia.formulation_g1 import statistiques_v1 as st
from controle_ia.gardes import GardeArret


def test_alertes_tolerees_arithmetique_publique():
    # Clopper-Pearson unilatéral à 95 %, borne strictement sous 5 % : arithmétique refaite par deux lecteurs de la décision
    assert [st.alertes_tolerees(n) for n in (150, 200, 300, 400)] == [2, 4, 8, 12]
    assert st.alertes_tolerees(10) == -1
    assert st.passage_garde_exact(200, 0.01) == pytest.approx(0.948, abs=5e-4)
    assert st.passage_garde_exact(300, 0.01) == pytest.approx(0.996, abs=5e-4)
    assert st.passage_garde_exact(300, 0.05) == pytest.approx(0.034, abs=5e-4)


def test_conjonction_independante():
    p = st.passage_garde_exact(200, 0.01)
    assert st.conjonction_independante([p] * 3) == pytest.approx(0.853, abs=1e-3)
    assert st.conjonction_independante([p] * 6) == pytest.approx(0.727, abs=1e-3)
    with pytest.raises(GardeArret):
        st.conjonction_independante([0.5, 1.2])


def test_seuils_sain_et_artefact():
    x = np.arange(300, dtype=float)[None, :].repeat(2, axis=0)
    s = st.seuils(x, 0.01)            # j = 3 : troisième plus grand score, 297
    assert list(s) == [297.0, 297.0]
    assert (x > s[:, None]).sum(axis=1).tolist() == [2, 2]
    with pytest.raises(GardeArret):   # 99 épisodes ne fixent aucun seuil à 1 %
        st.seuils(np.zeros((1, 99)), 0.01)
    with pytest.raises(GardeArret):
        st.seuils(np.zeros(300), 0.01)


def test_taux_reel_du_seuil_calibre():
    rng = np.random.default_rng(np.random.SeedSequence(11))
    s = st.seuils(rng.standard_normal((4000, 300)), 0.01)
    assert stats.norm.sf(s).mean() == pytest.approx(3 / 301, abs=4e-4)


def test_rappel_vrai():
    assert st.rappel_vrai(0.0, 0.01) == pytest.approx(0.01)
    assert st.rappel_vrai(stats.norm.isf(0.01), 0.01) == pytest.approx(0.5)


def test_pari_niveau_et_puissance():
    rng = np.random.default_rng(np.random.SeedSequence(12))
    nul = rng.choice([-1.0, 0.0, 1.0], p=[0.3, 0.4, 0.3], size=(4000, 300))
    assert st.pari_apparie_borne(nul, 0.05).mean() <= 0.05 + 3 * (0.05 * 0.95 / 4000) ** 0.5
    effet = rng.choice([-1.0, 0.0, 1.0], p=[0.1, 0.4, 0.5], size=(500, 300))
    assert st.pari_apparie_borne(effet, 0.025).mean() > 0.99
    contraire = -effet
    assert st.pari_apparie_borne(contraire, 0.025).sum() == 0
    assert st.pari_apparie_borne(np.zeros((3, 50)), 0.025).sum() == 0


def test_pari_garde_bornes():
    with pytest.raises(GardeArret):
        st.pari_apparie_borne(np.full((2, 10), 1.5), 0.05)
    with pytest.raises(GardeArret):
        st.pari_apparie_borne(np.array([[0.0, np.nan]]), 0.05)
    with pytest.raises(GardeArret):
        st.pari_apparie_borne(np.zeros((2, 10)), 0.7)
    assert st.pari_apparie_borne(np.ones((2, 10)), 0.05).shape == (2,)


def test_student_apparie():
    rng = np.random.default_rng(np.random.SeedSequence(13))
    nul = rng.normal(0, 0.3, size=(6000, 100)).clip(-1, 1)
    assert st.student_apparie(nul, 0.05).mean() == pytest.approx(0.05, abs=0.012)
    assert st.student_apparie(np.full((1, 10), 0.2), 0.05).tolist() == [True]     # écart-type nul, moyenne positive
    assert st.student_apparie(np.zeros((1, 10)), 0.05).tolist() == [False]


def test_borne_haute_par_taches_et_clopper_pearson():
    assert st.borne_haute_clopper_pearson(0, 300) == pytest.approx(1 - 0.05 ** (1 / 300))
    assert float(st.borne_haute_clopper_pearson(300, 300)) == 1.0
    with pytest.raises(GardeArret):
        st.borne_haute_clopper_pearson(301, 300)
    t = np.zeros((1, 50))
    assert st.borne_haute_par_taches(t)[0] == 0.0
    with pytest.raises(GardeArret):
        st.borne_haute_par_taches(np.zeros((1, 1)))


def test_reechantillonnage_par_blocs():
    rng = np.random.default_rng(np.random.SeedSequence(14))
    v = rng.normal(0.1, 0.2, size=(3, 200)).clip(-1, 1)
    idx = st.indices_blocs(rng, 3, 400, 200)
    moy = st.moyennes_reechantillonnees(v, idx)
    assert moy.shape == (3, 400)
    assert np.allclose(moy.mean(axis=1), v.mean(axis=1), atol=0.004)
    assert np.allclose(moy.std(axis=1), v.std(axis=1) / 200 ** 0.5, rtol=0.2)
    with pytest.raises(GardeArret):
        st.indices_blocs(rng, 3, 50, 200)
    with pytest.raises(GardeArret):
        st.moyennes_reechantillonnees(v[:, :100], idx)
