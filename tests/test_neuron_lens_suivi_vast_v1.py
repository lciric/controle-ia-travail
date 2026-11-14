"""Essais (R5) du suivi sans secret : champs filtrés (le jeton de la configuration n'est pas restitué), sortie contenant un secret
refusée, instance absente, journaux balayés."""
import json

import pytest

from controle_ia.neuron_lens import suivi_vast_v1 as sv

JETON = "jeton-factice-0123456789"


def appel_factice(*args):
    if args[:2] == ("show", "instance"):
        return 0, json.dumps({"id": 7, "actual_status": "running", "dph_total": 0.42,
                              "extra_env": [["GH_TOKEN", JETON]], "onstart": "x"}), ""
    if args[:2] == ("show", "instances"):
        return 0, json.dumps([{"id": 7, "label": "neuron-lens-volet-a", "extra_env": {"GH_TOKEN": JETON}}]), ""
    if args[0] == "logs":
        return 0, "AMORCE ok\n", ""
    raise AssertionError(args)


def test_champs_filtres_sans_secret():
    vus = []
    sv.main(["instance", "7"], appel=appel_factice, env={"CONTROLE_IA_GITHUB_TOKEN_2": JETON}, sortie=vus.append)
    sv.main(["instances"], appel=appel_factice, env={"CONTROLE_IA_GITHUB_TOKEN_2": JETON}, sortie=vus.append)
    assert JETON not in "".join(vus) and '"dph_total": 0.42' in vus[0] and "extra_env" not in vus[1]


def test_sortie_avec_secret_refusee():
    vus = []
    with pytest.raises(SystemExit):
        sv.main(["logs", "7"], appel=lambda *a: (0, f"fuite {JETON}\n", ""), env={"GH_TOKEN": JETON}, sortie=vus.append)
    assert vus == []
    sv.main(["logs", "7"], appel=appel_factice, env={"GH_TOKEN": JETON}, sortie=vus.append)
    assert vus == ["AMORCE ok\n"]


def test_instance_absente_ou_erreur():
    assert sv.instance(7, appel=lambda *a: (0, "{}", "")) == {"absente": True}
    assert "erreur" in sv.instance(7, appel=lambda *a: (1, "", "Error: instance 7 not found"))
