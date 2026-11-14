"""Essais (R5) du suivi sans secret v2 : champs filtrés, sortie contenant un secret refusée (brut, encodé pour une adresse, base 64
seul et en en-tête, à tout alignement), champ gardé portant le secret refusé, variable exigée absente = refus, forme inattendue
signalée, absence prouvée seulement sur une liste lue sans erreur, sortie de création réduite, outil introuvable."""
import base64
import io
import json
from urllib.parse import quote

import pytest

from controle_ia.neuron_lens import suivi_vast_v2 as sv

JETON = "ghp_factice0123456789ABCDEFabcdef"
ENV = {"CONTROLE_IA_GITHUB_TOKEN_2": JETON}


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
    sv.main(["instance", "7"], appel=appel_factice, env=ENV, sortie=vus.append)
    sv.main(["instances"], appel=appel_factice, env=ENV, sortie=vus.append)
    assert JETON not in "".join(vus) and '"dph_total": 0.42' in vus[0] and "extra_env" not in vus[1]


def test_variable_exigee_absente_refus():
    vus = []
    with pytest.raises(SystemExit, match="absente"):
        sv.main(["logs", "7"], appel=appel_factice, env={"GH_TOKEN": JETON}, sortie=vus.append)
    with pytest.raises(SystemExit, match="absente"):
        sv.main(["logs", "7"], appel=appel_factice, env={"CONTROLE_IA_GITHUB_TOKEN_2": "court"}, sortie=vus.append)
    assert vus == []
    sv.main(["logs", "7"], appel=appel_factice, env=ENV, sortie=vus.append)  # cas sain
    assert vus == ["AMORCE ok\n"]


@pytest.mark.parametrize("prefixe", ["", "a", "ab", "abc", "Authorization: Basic "])
@pytest.mark.parametrize("forme", ["brut", "adresse", "b64", "b64_entete"])
def test_formes_encodees_refusees(prefixe, forme):
    charge = {"brut": JETON.encode(), "adresse": JETON.encode(), "b64": JETON.encode(),
              "b64_entete": b"x-access-token:" + JETON.encode()}[forme]
    if forme in ("b64", "b64_entete"):
        fuite = base64.b64encode(prefixe.encode() + charge + b"\nsuite").decode()
    elif forme == "adresse":
        fuite = prefixe + "https://x-access-token:" + quote(JETON, safe="") + "@github.com"
    else:
        fuite = prefixe + JETON + " suite"
    vus = []
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["logs", "7"], appel=lambda *a: (0, f"trace {fuite}\n", ""), env=ENV, sortie=vus.append)
    assert vus == []


def test_formes_ne_refusent_pas_un_texte_sain():
    sec = sv.valeurs_secretes(ENV)
    assert all(len(f) >= sv.MIN_FORME for f in sec)
    sain = "AMORCE 2026-11-14T00:00:00Z pousse : essais passes ; " + base64.b64encode(b"x-access-token:autre-jeton-0123456789").decode()
    assert sv.balayer(sain, sec) == sain


def test_champ_garde_portant_le_secret_refuse():
    vus = []
    app = lambda *a: (0, json.dumps({"id": 7, "label": f"etiquette {JETON}", "status_msg": "ok"}), "")
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["instance", "7"], appel=app, env=ENV, sortie=vus.append)
    app2 = lambda *a: (0, json.dumps([{"id": 7, "status_msg": f"erreur {JETON}"}]), "")
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["instances"], appel=app2, env=ENV, sortie=vus.append)
    assert vus == []


def test_instance_absente_erreur_ou_forme_inattendue():
    assert sv.instance(7, appel=lambda *a: (0, "{}", "")) == {"absente": True}
    assert "erreur" in sv.instance(7, appel=lambda *a: (1, "", "Error: instance 7 not found"))
    assert "forme inattendue" in sv.instance(7, appel=lambda *a: (0, json.dumps({"instances": {"id": 7}}), ""))["erreur"]
    assert "illisible" in sv.instance(7, appel=lambda *a: (0, "pas du json", ""))["erreur"]
    assert sv.instances(appel=lambda *a: (0, json.dumps({"instances": [{"id": 3}]}), "")) == [{"id": 3}]
    assert "forme inattendue" in sv.instances(appel=lambda *a: (0, json.dumps({"x": 1}), ""))["erreur"]


def test_absence_prouvee_seulement_sans_erreur():
    vus = []
    assert sv.main(["absente", "8"], appel=appel_factice, env=ENV, sortie=vus.append) == 0  # cas sain : 8 n'est pas listée
    assert sv.main(["absente", "7"], appel=appel_factice, env=ENV, sortie=vus.append) == 1  # présente
    assert sv.main(["absente", "8"], appel=lambda *a: (1, "", "Error: 401"), env=ENV, sortie=vus.append) == 1  # erreur ≠ absence
    assert sv.main(["absente", "8"], appel=lambda *a: (0, '{"x": 1}', ""), env=ENV, sortie=vus.append) == 1  # forme inattendue
    assert "NON prouvée" in vus[2] and "PRÉSENTE" in vus[1]


def test_creation_reduite_et_balayee():
    vus = []
    entree = io.StringIO(json.dumps({"success": True, "new_contract": 123, "env": {"GH_TOKEN": JETON}}))
    sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append, entree=entree)
    assert json.loads(vus[0]) == {"success": True, "new_contract": 123}
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append, entree=io.StringIO(f"Error: bad env {JETON}"))
    sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append, entree=io.StringIO("Error: no such offer"))
    assert "no such offer" in vus[-1] and len(vus) == 2


def test_outil_introuvable(monkeypatch):
    monkeypatch.setenv("VASTAI_OUTIL", "/inexistant/vastai")
    assert sv.instance(7) == {"erreur": "outil introuvable : /inexistant/vastai"}
    assert "NON prouvée" in sv.absente(7)[1]
