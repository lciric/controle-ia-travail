"""Statistiques de l'étude des formulations du contraste à témoin apparié : valeurs exactes et propriétés (v3 :
les essais de la v2 sur `statistiques_v3`, plus la garde appariée de N-055, D-S4, et l'e-valeur du minimum)."""
import numpy as np
import pytest
from scipy import stats

from controle_ia.formulation_g1 import statistiques_v3 as st
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


def test_pari_sur_grille_niveau_et_puissance():
    rng = np.random.default_rng(np.random.SeedSequence(15))
    nul = rng.choice([-1.0, 0.0, 1.0], p=[0.3, 0.4, 0.3], size=(4000, 300))
    assert st.pari_sur_grille(nul, 0.05).mean() <= 0.05 + 3 * (0.05 * 0.95 / 4000) ** 0.5
    assert st.pari_sur_grille(nul, 0.025).mean() <= 0.025 + 3 * (0.025 * 0.975 / 4000) ** 0.5
    effet = rng.choice([-1.0, 0.0, 1.0], p=[0.1, 0.4, 0.5], size=(500, 300))
    assert st.pari_sur_grille(effet, 0.025).mean() > 0.99
    assert st.pari_sur_grille(-effet, 0.025).sum() == 0
    assert st.pari_sur_grille(np.zeros((3, 50)), 0.025).sum() == 0


def test_pari_sur_grille_capital_a_la_main():
    # une seule mise 0,5, différences toutes égales à 1 : capital 1,5 puissance t ; 1/0,025 = 40 atteint à t = 10
    assert st.pari_sur_grille(np.ones((1, 9)), 0.025, grille=(0.5,)).tolist() == [False]
    assert st.pari_sur_grille(np.ones((1, 10)), 0.025, grille=(0.5,)).tolist() == [True]
    # rejet au maximum du capital : dix gains puis des pertes ne défont pas le rejet
    d = np.concatenate([np.ones((1, 10)), -np.ones((1, 30))], axis=1)
    assert st.pari_sur_grille(d, 0.025, grille=(0.5,)).tolist() == [True]
    assert st.GRILLE_MISES == (0.1, 0.3, 0.6, 0.9)


def test_pari_sur_grille_gardes():
    sain = np.zeros((2, 10))
    assert st.pari_sur_grille(sain, 0.05).shape == (2,)
    with pytest.raises(GardeArret):
        st.pari_sur_grille(np.full((2, 10), 1.5), 0.05)
    with pytest.raises(GardeArret):
        st.pari_sur_grille(sain, 0.7)
    for grille in ((), (0.0, 0.5), (0.5, 1.0)):
        with pytest.raises(GardeArret):
            st.pari_sur_grille(sain, 0.05, grille=grille)


def test_delta_de_garde_paliers_de_la_conception():
    assert [st.delta_de_garde(n) for n in (50, 149, 150, 299, 300, 600)] == [0.10, 0.10, 0.05, 0.05, 0.03, 0.03]
    with pytest.raises(GardeArret):
        st.delta_de_garde(1)


def test_pari_avec_garde_sain_et_artefact():
    rng = np.random.default_rng(np.random.SeedSequence(16))
    v = rng.choice([-1.0, 0.0, 1.0], p=[0.1, 0.4, 0.5], size=(300, 400))
    sain = rng.choice([-1 / 3, 0.0, 1 / 3], p=[0.02, 0.96, 0.02], size=(300, 400))      # aucune asymétrie d'alertes
    assert st.pari_avec_garde(v, sain, 0.03, 0.025).mean() > 0.95
    asymetrie = rng.choice([0.0, 1 / 3, 1.0], p=[0.6, 0.3, 0.1], size=(300, 400))        # écart moyen 0,2 : au-delà de δ
    assert st.pari_avec_garde(v, asymetrie, 0.03, 0.025).sum() == 0                     # la garde bloque le gain
    assert st.pari_sur_grille(v, 0.025).mean() > 0.99                                   # que le contraste seul promeut
    assert st.pari_avec_garde(-v, sain, 0.03, 0.025).sum() == 0                         # la garde ne promeut rien seule
    # la garde ne fait que retirer : jamais de rejet avec elle sans rejet du contraste seul
    assert not np.any(st.pari_avec_garde(v, sain, 0.03, 0.025) & ~st.pari_sur_grille(v, 0.025))


def test_pari_avec_garde_niveau_sur_chaque_membre_du_nul():
    rng = np.random.default_rng(np.random.SeedSequence(17))
    nul_contraste = rng.choice([-1.0, 0.0, 1.0], p=[0.3, 0.4, 0.3], size=(4000, 300))
    sain = np.zeros((4000, 300))
    assert st.pari_avec_garde(nul_contraste, sain, 0.05, 0.05).mean() <= 0.05 + 3 * (0.05 * 0.95 / 4000) ** 0.5
    effet = np.ones((4000, 300))
    frontiere_garde = rng.choice([-0.95, 0.05, 1.0], p=[0.2, 0.55, 0.25], size=(4000, 300))   # écart moyen = δ = 0,0875…
    delta = float(-0.95 * 0.2 + 0.05 * 0.55 + 1.0 * 0.25)
    assert st.pari_avec_garde(effet, frontiere_garde, delta, 0.05).mean() <= 0.05 + 3 * (0.05 * 0.95 / 4000) ** 0.5


def test_pari_avec_garde_minimum_au_meme_instant():
    # une seule mise 0,5 ; contraste : dix gains (richesse 57,7 ≥ 40) puis des pertes ; garde : ne monte qu'après
    v = np.concatenate([np.ones((1, 10)), -np.ones((1, 30))], axis=1)
    g_tardive = np.concatenate([np.full((1, 10), 0.5), np.full((1, 30), -1.0)], axis=1)
    assert st.pari_sur_grille(v, 0.025, grille=(0.5,)).tolist() == [True]
    assert st.pari_avec_garde(v, g_tardive, 0.5, 0.025, grille=(0.5,)).tolist() == [False]   # jamais ≥ 40 ensemble
    g_tot = np.full((1, 40), -1.0)                                                           # garde riche dès le début
    assert st.pari_avec_garde(v, g_tot, 0.5, 0.025, grille=(0.5,)).tolist() == [True]


def test_pari_avec_garde_gardes():
    sain = np.zeros((2, 10))
    assert st.pari_avec_garde(sain, sain, 0.05, 0.05).shape == (2,)
    with pytest.raises(GardeArret):
        st.pari_avec_garde(sain, np.zeros((2, 9)), 0.05, 0.05)
    with pytest.raises(GardeArret):
        st.pari_avec_garde(sain, np.full((2, 10), 1.5), 0.05, 0.05)
    for delta in (0.0, 1.0):
        with pytest.raises(GardeArret):
            st.pari_avec_garde(sain, sain, delta, 0.05)
    with pytest.raises(GardeArret):
        st.pari_avec_garde(sain, sain, 0.05, 0.05, grille=(1.0,))
