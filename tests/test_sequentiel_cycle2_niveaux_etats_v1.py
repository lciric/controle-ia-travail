"""Niveaux des lectures et états : cas sains et artefacts (R5)."""
import itertools
import math

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sequentiel_cycle2 import etats_v1 as etats
from controle_ia.sequentiel_cycle2 import niveaux_v1 as niveaux


def test_repartition_somme_exacte_et_gardes():
    for q in (niveaux.Q_DECISIF, niveaux.Q_EQUIVALENCE):
        for part in (0.1, 0.2, 0.5):
            q_i, q_f = niveaux.repartir(q, part)
            assert q_i > 0 and q_f > 0 and q_i + q_f == pytest.approx(q, abs=0, rel=1e-15)
    for mauvais in (0.0, 1.0, -0.1, 1.5, 1):
        with pytest.raises(GardeArret):
            niveaux.repartir(niveaux.Q_DECISIF, mauvais)
    for mauvais in (0.0, 0.5, 1.0, -1.0):
        with pytest.raises(GardeArret):
            niveaux.repartir(mauvais, 0.2)


def test_tirages_minimaux():
    assert niveaux.tirages_minimaux(0.003125) == 8000
    assert niveaux.tirages_minimaux(0.000625) == 40000
    assert niveaux.tirages_minimaux(0.0025) == 10000


def test_frontiere_a_depense_retrouve_les_valeurs_publiees():
    # Lan et DeMets, dépense de type O'Brien-Fleming, deux lectures égales, niveau unilatéral 0,025 :
    # valeurs tabulées 2,963 et 1,969 (tables des plans séquentiels par groupes).
    z1, z2 = niveaux.bornes_depense(0.025, 0.5)
    assert z1 == pytest.approx(2.963, abs=2e-3) and z2 == pytest.approx(1.969, abs=2e-3)
    assert niveaux.risque_deux_lectures(z1, z2, 0.5) == pytest.approx(0.025, abs=1e-6)


def test_frontiere_a_depense_tient_le_niveau_du_brouillon_3_et_le_plan_naif_non():
    q = niveaux.Q_DECISIF
    for fraction in (1 / 3, 0.5, 0.75):
        z1, z2 = niveaux.bornes_depense(q, fraction)
        assert niveaux.risque_deux_lectures(z1, z2, fraction) == pytest.approx(q, rel=1e-4)
        z = niveaux.z_de(q)
        assert niveaux.risque_deux_lectures(z, z, fraction) > 1.3 * q      # artefact : deux lectures sans correction
        zi, zf = (niveaux.z_de(x) for x in niveaux.repartir(q, 0.2))
        assert niveaux.risque_deux_lectures(zi, zf, fraction) <= q         # cas sain : borne d'union


def test_frontiere_du_melange_au_dessus_de_la_lecture_unique():
    q = niveaux.Q_DECISIF
    for n in (50, 200, 400, 600):
        assert niveaux.frontiere_melange(n, q, 0.03) > niveaux.z_de(q)
    with pytest.raises(GardeArret):
        niveaux.frontiere_melange(0, q, 0.03)


def test_enumeration_des_etats_de_dose_aucun_trou():
    vus = set()
    for valeurs in itertools.product((False, True), repeat=6):
        aff = dict(zip(etats.AFFIRMATIONS, valeurs))
        e = etats.etat_dose(aff)
        assert e in etats.ETATS_DOSE
        vus.add(e)
        vect = etats.etats_dose_vect({a: np.array([v]) for a, v in aff.items()})
        assert etats.ETATS_DOSE[int(vect[0])] == e
    assert vus == set(etats.ETATS_DOSE)
    faux = dict.fromkeys(etats.AFFIRMATIONS, False)
    assert etats.etat_dose(dict(faux, c1=True, c2=True)) == "AP"
    assert etats.etat_dose(dict(faux, c3=True, c4=True)) == "M"
    assert etats.etat_dose(dict(faux, c1=True, c6=True)) == "P"
    assert etats.etat_dose(dict(faux, c2=True)) == "G"
    assert etats.etat_dose(dict(faux, c5=True, c6=True)) == "R"
    assert etats.etat_dose(dict(faux, c5=True)) == "Z"
    assert etats.etat_dose(dict(faux, c3=True)) == "Z"


def test_enumeration_des_etats_de_cycle_et_version_vectorisee():
    vus = set()
    for combinaison in itertools.product(etats.ETATS_DOSE, repeat=4):
        e = etats.etat_cycle(list(combinaison))
        vus.add(e)
        codes = np.array([[etats.ETATS_DOSE.index(x) for x in combinaison]])
        assert etats.ETATS_CYCLE[int(etats.etats_cycle_vect(codes)[0])] == e
    assert vus == set(etats.ETATS_CYCLE)
    assert etats.etat_cycle(["AP", "M", "Z", "Z"]) == "partage"
    assert etats.etat_cycle(["R", "R", "R", "R"]) == "rien_de_propre"
    assert etats.etat_cycle(["R", "R", "R", "R"], signal_plante_reconnu=False) == "non_concluant"
    assert etats.etat_cycle(["R", "R", "R", "Z"]) == "non_concluant"
    assert etats.etat_cycle(["C", "Z", "Z", "Z"]) == "non_concluant"
    with pytest.raises(GardeArret):
        etats.etat_cycle(["AP", "inconnu"])
    with pytest.raises(GardeArret):
        etats.etat_cycle([])


def test_cumul_entre_lectures():
    faux = dict.fromkeys(etats.AFFIRMATIONS, False)
    inter, finale = dict(faux, c1=True), dict(faux, c2=True)
    assert etats.etat_dose(inter) == "P" and etats.etat_dose(finale) == "G"
    assert etats.etat_dose(etats.cumuler(inter, finale)) == "AP"          # acquis à deux lectures différentes
    assert etats.etat_dose(etats.cumuler(dict(faux, c2=True), dict(faux, c3=True, c4=True))) == "C"   # contradiction
    with pytest.raises(GardeArret):
        etats.cumuler({"c1": True}, finale)
    with pytest.raises(GardeArret):
        etats.etat_dose(dict(faux, c1=1))
    assert math.isfinite(niveaux.z_de(niveaux.Q_DECISIF))
