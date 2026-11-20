"""Essais de la garde de `lignee_reconnue` — v1. Cas sains et artefacts (R5), sans aucune donnée.

Lancement : `.venv/bin/python -B -m pytest -q -p no:cacheprovider docs/notes/organisme-auto-conception-v9-mere/juge-selection-manifeste-v1/essais_garde_lignee_reconnue_v1.py`
"""
import importlib.util
import json
from pathlib import Path

import pytest

_ICI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("garde", _ICI / "garde_lignee_reconnue_v1.py")
g = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(g)

FAM = {"prop-opus": "F", "prop-fable": "F", "prop-argon": "A", "prop-astra": "S", "prop-carbon": "C"}
PERMIS = set(FAM)


def _lecture(cartes, veto, lignee="prop-fable"):
    return {"lecteur": "F", "lignee": lignee, "independance": "x", "cartes": cartes, "veto": veto}


def test_sain():
    l = _lecture([{"id": "c1", "lignee_reconnue": "prop-opus", "raisons": {"E": "TEXTE"}},
                  {"id": "c2", "lignee_reconnue": "aucune"}],
                 [{"id": "c1", "prediction": "p", "decision": "d", "lignee_reconnue": "prop-carbon"}])
    r = g.controler(l, PERMIS)
    assert r["issue"] == "conforme" and r["nombre_de_refus"] == 0
    assert "TEXTE" not in json.dumps(r)


def test_artefact_graphie_carte():
    l = _lecture([{"id": "c1", "lignee_reconnue": "Opus"}, {"id": "c2", "lignee_reconnue": "prop-opus "}], [])
    r = g.controler(l, PERMIS)
    assert r["issue"] == "refusee" and r["refus"]["cartes"] == ["c1", "c2"]
    assert "Opus" not in json.dumps(r["refus"])


def test_artefact_graphie_veto():
    l = _lecture([{"id": "c1", "lignee_reconnue": "aucune"}],
                 [{"id": "c1", "prediction": "p", "decision": "d", "lignee_reconnue": "Aucune"}])
    r = g.controler(l, PERMIS)
    assert r["refus"]["veto"] == ["c1"] and r["issue"] == "refusee"


def test_artefact_valeur_absente_ou_non_textuelle():
    l = _lecture([{"id": "c1"}, {"id": "c2", "lignee_reconnue": None}, {"id": "c3", "lignee_reconnue": 3}], [])
    assert g.controler(l, PERMIS)["refus"]["cartes"] == ["c1", "c2", "c3"]


def test_artefact_lignee_du_lecteur():
    r = g.controler(_lecture([{"id": "c1", "lignee_reconnue": "aucune"}], [], lignee="fable"), PERMIS)
    assert r["refus"]["lignee_du_lecteur"] is True and r["issue"] == "refusee"


def test_artefact_identifiant_absent():
    r = g.controler(_lecture([{"lignee_reconnue": "aucune"}], []), PERMIS)
    assert r["entrees_sans_identifiant"] == 1 and r["issue"] == "refusee"


def test_artefact_lecture_mal_formee():
    with pytest.raises(g.Malforme):
        g.controler({"lignee": "prop-opus", "cartes": {}}, PERMIS)
    with pytest.raises(g.Malforme):
        g.controler(_lecture(["pas un objet"], []), PERMIS)


def test_manifeste_sain_et_artefacts():
    assert g.permis_depuis_manifeste({"familles": FAM}) == PERMIS
    with pytest.raises(g.Malforme):
        g.permis_depuis_manifeste({"familles": {}})
    with pytest.raises(g.Malforme):
        g.permis_depuis_manifeste({"familles": {"aucune": "X"}})


def test_principal_codes(tmp_path):
    m = tmp_path / "m.json"
    m.write_text(json.dumps({"familles": FAM}))
    bon = tmp_path / "l.json"
    bon.write_text(json.dumps(_lecture([{"id": "c1", "lignee_reconnue": "prop-argon"}], [])))
    mauvais = tmp_path / "l2.json"
    mauvais.write_text(json.dumps(_lecture([{"id": "c1", "lignee_reconnue": "argon"}], [])))
    casse = tmp_path / "l3.json"
    casse.write_text("{pas du json")
    s = tmp_path / "s.json"
    assert g.principal(["--manifeste", str(m), "--lecture", str(bon), "--sortie", str(s)]) == 0
    assert g.principal(["--manifeste", str(m), "--lecture", str(mauvais), "--sortie", str(s)]) == 1
    assert g.principal(["--manifeste", str(m), "--lecture", str(casse), "--sortie", str(s)]) == 2
    assert json.loads(s.read_text())["issue"] == "mal_formee"
