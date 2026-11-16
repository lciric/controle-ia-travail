"""Banc de mutations de l'idée 1.2 (étape 0 du texte scellé) : toutes tuées pour la raison attendue, la mutation
« valeur e lue au maximum » par la lecture (3) sur le jeu synthétique de 20 000 générations (racine d'essai)."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B
from controle_ia.organisme_idees_juge import mutations_v1 as MU
from controle_ia.organisme_idees_juge import synthetique_v1 as S


@pytest.fixture(scope="module")
def rapport():
    return MU.banc(MU.RACINE_ESSAI, S.GENERATIONS, S.REECHANTILLONS)


EXIGEES = ("la règle lit un instant non révélé", "budget dépassé", "arrêt bas avant 50 tirages", "plafond ignoré",
           "hasard du placebo tiré des issues", "m compté après coup", "flux d'issues partagé entre deux cartes",
           "issues fraîches tirées avant le gel", "issues fraîches passées à la fonction qui bâtit un engagement",
           "valeur e lue au maximum de la trajectoire (lecture (3), jeu synthétique)",
           "F lu sur le champ « promue » de l'évaluation à 800", "F lu sur le champ « t_promotion » de l'évaluation à 800",
           "F lu sur le champ « log_richesse_max » de l'évaluation à 800",
           "F lu sur le champ « log_richesse_arretee » de l'évaluation à 800",
           "oracle calculé sur les issues jugées (après le tirage des issues fraîches)")


def test_toutes_les_mutations_exigees_sont_tuees_pour_la_raison_attendue(rapport):
    for nom in EXIGEES:
        assert nom in rapport["mutations"], nom
    for nom, r in rapport["mutations"].items():
        assert r["tuee"], (nom, r)
    assert rapport["toutes_tuees"]
    MU.exiger_toutes_tuees(rapport)


def test_jeu_synthetique_de_20000_generations(rapport):
    ep = rapport["synthetique"]
    assert ep["generations"] == 20000 and ep["reechantillons"] == 10000 and ep["plafond_log_e"] == 50.0
    assert ep["mute"]["borne_basse"] > 1.0          # mutation tuée
    assert ep["sain"]["borne_haute"] < 1.0          # cas sain : la lecture correcte ne déclenche pas


def test_exiger_toutes_tuees_artefact(rapport):
    faux = {"mutations": dict(rapport["mutations"]), "synthetique": rapport["synthetique"]}
    faux["mutations"]["plafond ignoré"] = {"tuee": False, "raison": "aucun arrêt", "attendue": "plafond"}
    with pytest.raises(GardeArret, match="pas de jeu"):
        MU.exiger_toutes_tuees(faux)


def test_lot_synthetique_egal_a_l_ecriture_par_generation():
    lw_lot, lam_lot = S.trajectoires_lot(MU.RACINE_ESSAI, 0, 20)
    for g in range(20):
        lw, lam = S.trajectoires_generation(B.generateur(MU.RACINE_ESSAI, 97, g))
        assert np.allclose(lw, lw_lot[g], atol=1e-9, rtol=0) and np.allclose(lam, lam_lot[g], atol=1e-9, rtol=0)
        assert (lw <= lam + 1e-9).all()


def test_mutation_tuee_pour_une_autre_raison_compte_comme_survivante():
    assert not MU._tuee(lambda: (_ for _ in ()).throw(GardeArret("autre chose")), "raison attendue")["tuee"]
    assert not MU._tuee(lambda: None, "x")["tuee"]
    assert not MU._tuee(lambda: 1 / 0, "x")["tuee"]
