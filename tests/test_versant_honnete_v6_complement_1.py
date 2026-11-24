"""Complément 1 aux essais du code v6 du versant honnête (vérification Sonnet : borne haute de centre_min_actions non
éprouvée ; la mutation « <= 60 porté à 600 » survivait). Le code v6 n'est pas modifié."""
import pytest

from controle_ia import versant_honnete_v6 as vh
from controle_ia.gardes import GardeArret

SAIN = {"centre_statistique": "mediane", "centre_echelle": "log10", "centre_unite": "action",
        "centre_mediane_paire": "milieu", "centre_min_actions": 10}


def test_min_actions_bornes_hautes():
    assert vh.controler_reglages_centre(dict(SAIN, centre_min_actions=60))["centre_min_actions"] == 60   # cas sain : borne incluse
    for v in (61, 600):                                                                                 # artefacts
        with pytest.raises(GardeArret, match="hors domaine"):
            vh.controler_reglages_centre(dict(SAIN, centre_min_actions=v))
