"""Mondes à vérité connue : exactitude du calcul, graines, cas sains et artefacts (R5, R9).

Ces essais éprouvent l'instrument sur des cas extrêmes ou réduits ; ils ne jouent pas la grille préenregistrée.
"""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sequentiel_cycle2 import monde_gaussien_v1 as gaussien
from controle_ia.sequentiel_cycle2 import monde_scores_v1 as scores
from controle_ia.sequentiel_cycle2 import niveaux_v1 as niveaux
from controle_ia.sondes.evaluation import aire_sous_courbe


def config_gaussien(**change):
    c = {"n_taches": 400, "n_intermediaire": 200, "pas_tranche": 50,
         "erreur_type_64": {"d_somme": 0.038, "ecart": 0.038, "d_maximum": 0.038},
         "effets": {"d_somme": [0.0], "ecart": [0.0], "d_maximum": [0.0]},
         "correlation_doses": 0.0, "correlation_grandeurs": 0.0, "marge": 0.05, "part_intermediaire": 0.2,
         "n_repliques": 20000}
    c.update(change)
    return c


def config_scores(**change):
    c = {"verite": "nul", "n_taches": 60, "n_intermediaire": 30, "n_directions": 20, "amplitude": 0.0,
         "amplitude_directions": 0.0, "actions_decalees": 10, "part_tache": 0.3, "part_commune": 0.2, "marge": 0.05,
         "part_intermediaire": 0.2, "tirages_intermediaire": 8000, "tirages_finale": 2000}
    c.update(change)
    return c


def test_monde_gaussien_meme_graine_memes_comptes():
    a = gaussien.jouer(config_gaussien(), np.random.SeedSequence(7))
    b = gaussien.jouer(config_gaussien(), np.random.SeedSequence(7))
    c = gaussien.jouer(config_gaussien(), np.random.SeedSequence(8))
    assert a == b and a != c
    for plan in gaussien.PLANS:
        for cle in ("intermediaire", "finale", "couple"):
            assert sum(a["comptes"][plan][cle].values()) == 20000


def test_monde_gaussien_plan_unique_ne_prononce_rien_a_l_intermediaire():
    a = gaussien.jouer(config_gaussien(effets={"d_somme": [0.5], "ecart": [0.5], "d_maximum": [0.0]}),
                       np.random.SeedSequence(1))
    assert a["comptes"]["unique"]["intermediaire"] == {"non_concluant": 20000}
    assert a["comptes"]["unique"]["finale"] == {"accumuler_propre": 20000}          # cas sain : effet énorme
    assert a["comptes"]["reparti"]["intermediaire"] == {"accumuler_propre": 20000}


def test_monde_gaussien_voit_un_plan_qui_gonfle_le_risque():
    # Une seule affirmation à la frontière (propreté nulle, gain énorme) : le faux « accumuler, propre » est le
    # faux franchissement de c1. Artefact planté : le plan « naif » doit dépasser nettement le plan réparti.
    c = config_gaussien(effets={"d_somme": [0.0], "ecart": [0.5], "d_maximum": [0.0]}, n_repliques=400000)
    a = gaussien.jouer(c, np.random.SeedSequence(3))["comptes"]
    faux = {p: a[p]["finale"].get("accumuler_propre", 0) / 400000 for p in gaussien.PLANS}
    q = niveaux.Q_DECISIF
    ecart_type = (q / 400000) ** 0.5
    assert abs(faux["unique"] - q) < 4 * ecart_type                       # la lecture unique est à son niveau
    assert faux["reparti"] < q + 2 * ecart_type                           # cas sain
    assert abs(faux["depense"] - q) < 4 * ecart_type
    assert faux["naif"] > q + 8 * ecart_type                              # artefact vu
    assert faux["melange"] < q


def test_monde_gaussien_gardes_de_configuration():
    for change in ({"n_intermediaire": 400}, {"n_intermediaire": 210}, {"correlation_doses": 1.5},
                   {"effets": {"d_somme": [0.0], "ecart": [0.0, 0.0], "d_maximum": [0.0]}}):
        with pytest.raises(GardeArret):
            gaussien.jouer(config_gaussien(**change), np.random.SeedSequence(0))
    incomplet = config_gaussien()
    del incomplet["marge"]
    with pytest.raises(GardeArret):
        gaussien.jouer(incomplet, np.random.SeedSequence(0))


def test_aires_reechantillonnees_egales_a_la_reference():
    rng = np.random.default_rng(11)
    n = 37
    pos, neg = rng.standard_normal(n) + 0.4, rng.standard_normal(n)
    poids = rng.multinomial(n, np.full(n, 1 / n), size=25)
    rapide = scores.aires_reechantillonnees(pos, neg, poids)
    for b in range(25):
        tirees = np.repeat(np.arange(n), poids[b])
        reference = aire_sous_courbe(np.concatenate([pos[tirees], neg[tirees]]),
                                     np.concatenate([np.ones(n, dtype=int), np.zeros(n, dtype=int)]))
        assert rapide[b] == pytest.approx(reference, abs=1e-12)
    with pytest.raises(GardeArret):                                        # artefact : ex aequo
        scores.aires_reechantillonnees(np.array([1.0, 2.0]), np.array([2.0, 3.0]), np.ones((1, 2), dtype=int))


def test_statistiques_d_episode_somme_et_maximum_seulement():
    rng = np.random.default_rng(5)
    s = rng.standard_normal((4, 3, 2, 10))
    stats = scores.statistiques_episode(s)
    assert stats.shape == (2, 4, 3, 2)
    assert np.array_equal(stats[0], s.sum(axis=3)) and np.array_equal(stats[1], s.max(axis=3))
    s[0, 0, 0, 0] = np.nan
    with pytest.raises(GardeArret):
        scores.statistiques_episode(s)
    with pytest.raises(GardeArret):
        scores.statistiques_episode(np.zeros((4, 3, 2, 9)))


def test_monde_scores_graines_et_verites():
    a = scores.jouer_replique(config_scores(), np.random.SeedSequence(21))
    assert a == scores.jouer_replique(config_scores(), np.random.SeedSequence(21))
    assert set(a) == {"unique", "reparti", "naif"} and a["unique"]["intermediaire"] == "Z"
    grand = dict(n_taches=240, n_intermediaire=120, part_tache=0.0)
    dense = scores.jouer_replique(config_scores(verite="dense", amplitude=0.4, **grand), np.random.SeedSequence(22))
    assert dense["unique"]["finale"] == "AP" and dense["reparti"]["finale"] == "AP"      # cas sain : signal net
    sature = scores.jouer_replique(config_scores(verite="dense", amplitude=3.0), np.random.SeedSequence(22))
    assert sature["unique"]["finale"] == "P"       # deux aires à 1 : propre, aucun gain (l'état « saturé » est hors module)
    concentre = scores.jouer_replique(config_scores(verite="concentre", amplitude=4.0, actions_decalees=2),
                                      np.random.SeedSequence(23))
    assert concentre["unique"]["finale"] != "AP" and concentre["reparti"]["finale"] != "AP"   # jumeau concentré


def test_monde_scores_decalages_plantes_exacts():
    c = config_scores(verite="dense", amplitude=0.7, n_taches=50)
    avec = scores.tirer_scores(c, np.random.default_rng(9))
    sans = scores.tirer_scores(dict(c, verite="nul"), np.random.default_rng(9))
    difference = avec - sans
    assert np.allclose(difference[:, 0, 1, :], 0.7) and np.allclose(difference[:, 1:], 0.0)
    assert np.allclose(difference[:, 0, 0, :], 0.0)
    c2 = dict(c, verite="concentre", actions_decalees=2)
    d2 = scores.tirer_scores(c2, np.random.default_rng(9))[:, 0, 1, :] - sans[:, 0, 1, :]
    assert np.all((np.abs(d2) > 1e-9).sum(axis=1) <= 10)
    f = scores.tirer_scores(dict(c, verite="frontiere", amplitude_directions=0.3), np.random.default_rng(9))
    assert f.shape == (50, 21, 2, 10)


def test_monde_scores_gardes():
    for change in ({"verite": "inconnue"}, {"n_intermediaire": 60}, {"actions_decalees": 0}, {"n_directions": 5},
                   {"tirages_intermediaire": 100}, {"part_tache": 1.0}):
        with pytest.raises(GardeArret):
            scores.jouer_replique(config_scores(**change), np.random.SeedSequence(0))


def test_reglage_de_l_amplitude_cas_sain_et_ecart_hors_d_atteinte():
    c = config_scores()
    a = scores.regler_amplitude(c, 0.02, np.random.SeedSequence(4), pas=0.05)
    assert 0 < a < 3
    assert scores.ecart_de_population(c, a, np.random.default_rng(np.random.SeedSequence(4))) >= 0.02
    with pytest.raises(GardeArret):                                        # artefact : écart qu'aucun signal n'atteint
        scores.regler_amplitude(c, 0.6, np.random.SeedSequence(4), pas=0.25)
