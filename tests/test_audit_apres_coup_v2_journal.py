"""Essais de `audit_apres_coup_v2.journal` (rang 2) : ajout seul ; réécriture refusée ; probabilité absente refusée."""
import numpy as np
import pytest

from controle_ia.audit_apres_coup_v2.journal import Journal, heures
from controle_ia.gardes import GardeArret


def _lot(n, debut=0, pi=0.5, u=None):
    e = np.arange(debut, debut + n)
    h = heures(e)
    u = np.linspace(0, 0.99, n) if u is None else u
    pi = np.full(n, pi)
    aud = u < pi
    return dict(episode=e, enjeu=np.ones(n), h_enjeu=h["h_enjeu"], h_debut=h["h_debut"], h_fin=h["h_fin"],
                score=np.zeros(n), g_force=np.zeros(n, bool), h_score=h["h_score"], part_plancher=pi,
                part_enjeu=np.zeros(n), part_soupcon=np.zeros(n), pi=pi, ecrete=np.zeros(n, bool), u_piece=u,
                h_piece=h["h_piece"], audite=aud, source=np.where(aud, 1, 0))


def test_ajout_seul_et_verification():
    j = Journal()
    j.ajouter_episodes(**_lot(10))
    j.ajouter_episodes(**_lot(5, debut=10))
    a = np.flatnonzero(j.colonne("audite"))
    j.ajouter_verdicts(episode=a, verdict=np.ones(len(a)), h_verdict=8 * a + 5)
    assert len(j) == 15
    assert j.verifier() == j.empreinte()


def test_artefact_reecriture_refusee():
    j = Journal()
    j.ajouter_episodes(**_lot(10))
    with pytest.raises(GardeArret, match="réécriture"):
        j.reecrire(3, pi=0.1)
    with pytest.raises(ValueError):
        j.colonne("pi")[3] = 0.1  # colonne en lecture seule
    # modification par-dessous l'interface : détectée par l'empreinte chaînée
    base = j._ep["pi"][0]
    base.setflags(write=True)
    base[3] = 0.1
    with pytest.raises(GardeArret, match="modifié"):
        j.verifier()


def test_artefact_second_verdict_refuse():
    j = Journal()
    j.ajouter_episodes(**_lot(10))
    j.ajouter_verdicts(episode=[0], verdict=[1], h_verdict=[5])
    with pytest.raises(GardeArret):
        j.ajouter_verdicts(episode=[0], verdict=[0], h_verdict=[13])


def test_artefact_probabilite_absente_refusee():
    lot = _lot(4)
    lot["pi"] = np.array([0.5, np.nan, 0.5, 0.5])
    with pytest.raises(GardeArret, match="absente"):
        Journal().ajouter_episodes(**lot)
    lot = _lot(4)
    del lot["pi"]
    with pytest.raises(GardeArret, match="absentes"):
        Journal().ajouter_episodes(**lot)


def test_mutation_audite_qui_ne_suit_pas_U_inferieur_a_pi():
    lot = _lot(4)
    k = int(np.flatnonzero(~lot["audite"])[0])
    lot["audite"] = lot["audite"].copy()
    lot["audite"][k] = True
    lot["source"] = np.where(lot["audite"], 1, 0)
    with pytest.raises(GardeArret, match="« audité » ne suit pas U_i < π_i"):
        Journal().ajouter_episodes(**lot)


def test_artefact_source_plancher_pour_U_au_dessus_de_pi_min():
    """I-5 : π = 0,5 dont plancher 0,1 et soupçon 0,4 ; un audité de U ≥ 0,1 étiqueté « plancher » est refusé."""
    lot = _lot(6)
    lot["part_plancher"] = np.full(6, 0.1)
    lot["part_soupcon"] = np.full(6, 0.4)
    lot["source"] = np.where(lot["audite"], 1, 0)
    with pytest.raises(GardeArret, match="source incohérente avec U_i et les parts"):
        Journal().ajouter_episodes(**lot)
    lot["source"] = np.where(~lot["audite"], 0, np.where(lot["u_piece"] < 0.1, 1, 3))
    Journal().ajouter_episodes(**lot)  # cas sain


def test_artefact_pi_different_de_la_somme_des_parts():
    lot = _lot(4)
    lot["part_soupcon"] = np.full(4, 0.1)
    with pytest.raises(GardeArret, match="somme des trois parts"):
        Journal().ajouter_episodes(**lot)


def test_artefact_horloge_et_ordre():
    lot = _lot(4)
    lot["h_piece"] = lot["h_fin"]  # pièce tirée à la fin, non après
    with pytest.raises(GardeArret):
        Journal().ajouter_episodes(**lot)
    with pytest.raises(GardeArret):
        Journal().ajouter_episodes(**_lot(4, debut=3))
    j = Journal()
    j.ajouter_episodes(**_lot(4))
    with pytest.raises(GardeArret, match="antérieure"):
        j.ajouter_verdicts(episode=[0], verdict=[1], h_verdict=[3])


def test_journal_non_chaine_refuse_la_verification():
    j = Journal(chaine=False)
    j.ajouter_episodes(**_lot(3))
    with pytest.raises(GardeArret, match="non chaîné"):
        j.verifier()
