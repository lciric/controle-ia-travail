"""Essais de la pièce 7 — puissance : tables par simulation contre les formules."""
import math

import pytest

from controle_ia.devin_v2 import RefusDevin
from controle_ia.devin_v2.graines import graine_tache
from controle_ia.devin_v2.puissance import (confirmer_taille, constante_c, delta_min, episodes_pour,
                                            facteur_bonferroni, comparer_aux_formules, mort_1_declenche,
                                            mort_2_declenche, table_formules, taille_annoncee)

RACINE = 0xE703_7ED1_A0B4_28DB_8EBB_2A8D_6C4F_5C7F


def test_formules_redonnent_les_chiffres_de_la_specification():
    assert constante_c() == pytest.approx(2.4865, abs=1e-4)
    t = table_formules()
    assert [round(t["equilibre"][n], 3) for n in (400, 1000, 2000, 4000, 10000)] == [0.124, 0.079, 0.056, 0.039, 0.025]
    assert [round(t["audit_5"][n], 3) for n in (1000, 2000, 4000, 10000)] == [0.180, 0.128, 0.090, 0.057]
    assert round(facteur_bonferroni(15), 2) == 1.43 and round(facteur_bonferroni(17), 2) == 1.45
    assert round(facteur_bonferroni(30), 2) == 1.52 and round(facteur_bonferroni(34), 2) == 1.53
    # La spécification écrit 2 473 ((c / δ)² = 2 473,02, arrondi) ; l'entier qui atteint la
    # puissance est 2 474 (point laissé ouvert au rapport).
    assert round((constante_c() / 0.05) ** 2) == 2473 and episodes_pour(0.05) == 2474


def test_cas_sain_ecart_nul_aux_formules():
    lignes = comparer_aux_formules((2000,), 0.5, 1000, graine_tache(RACINE, "eq"))
    assert abs(lignes[2000]["puissance_simulee"] - 0.8) < 0.05
    lignes = comparer_aux_formules((2000,), 0.05, 1000, graine_tache(RACINE, "a5"))
    assert abs(lignes[2000]["puissance_simulee"] - 0.8) < 0.05


def test_artefact_ecart_qui_fait_redire_les_tailles():
    def formule_fausse(n, taux):  # oublie le taux d'audit
        return constante_c() / math.sqrt(n)
    with pytest.raises(RefusDevin, match="tailles à redire"):
        comparer_aux_formules((2000,), 0.05, 1000, graine_tache(RACINE, "faux"), formule=formule_fausse)


def test_tests_de_mort_1_et_2():
    assert not mort_1_declenche(72) and mort_1_declenche(73)
    assert mort_2_declenche(760) and not mort_2_declenche(761)
    with pytest.raises(RefusDevin):
        mort_1_declenche(10, repliques=100)


def test_taille_annoncee_puis_relevee_par_le_test_de_mort_2():
    grille = (0.02, 0.04, 0.06, 0.08)
    # Annonce sur ses graines : 0,04 passe 850 ; le test de mort 2, sur d'autres graines, le dément.
    annonce = {0.02: 500, 0.04: 860, 0.06: 950, 0.08: 999}
    mort = {0.04: 750, 0.06: 900, 0.08: 999}
    t = taille_annoncee(grille, lambda x, g: annonce[x], graine_tache(RACINE, "annonce"))
    assert t == 0.04
    r = confirmer_taille(grille, t, lambda x, g: mort[x], graine_tache(RACINE, "mort2"), graine_tache(RACINE, "annonce"))
    assert r["taille"] == 0.06 and r["declenchements"] == [{"taille": 0.04, "retrouvailles": 750}]


def test_aucun_repli():
    with pytest.raises(RefusDevin, match="aucune taille"):
        taille_annoncee((0.1, 0.2), lambda x, g: 10, graine_tache(RACINE, "x"))
    with pytest.raises(RefusDevin, match="croissante"):
        taille_annoncee((0.2, 0.1), lambda x, g: 999, graine_tache(RACINE, "x"))
    with pytest.raises(RefusDevin, match="distinctes"):
        confirmer_taille((0.1,), 0.1, lambda x, g: 999, graine_tache(RACINE, "m"), graine_tache(RACINE, "m"))
    with pytest.raises(RefusDevin, match="bout de la grille"):
        confirmer_taille((0.1, 0.2), 0.1, lambda x, g: 100, graine_tache(RACINE, "m"), graine_tache(RACINE, "a"))
    with pytest.raises(RefusDevin):
        delta_min(0)
