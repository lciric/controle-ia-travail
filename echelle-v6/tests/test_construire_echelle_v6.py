"""Gardes de `construire_echelle_v2.py` (R5, CLX-03, CLX-05) : construction saine et invariants ; artefacts :
gabarit qui dit l'état de connaissance de l'auteur, pli incomplet, négation déséquilibrée, lemmes communs a/b.
Lancement : python -m pytest -q echelle-v6/tests
"""
import importlib.util
import json
import pathlib

import pytest

SCRIPTS = pathlib.Path(__file__).resolve().parent.parent / "scripts"


def module():
    spec = importlib.util.spec_from_file_location("cons", SCRIPTS / "construire_echelle_v2.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_construction_saine(tmp_path):
    C = module()
    assert C.principal([str(tmp_path / "s")]) == 0
    doc = json.loads((tmp_path / "s" / "echelle-v2.json").read_text())
    st = doc["stimuli"]
    assert len(st) == 3072 and doc["version"] == "echelle-v2"
    for pli in ("S1", "S2", "E1", "E2"):
        assert {s["bonne"] for s in st if s["pli"] == pli} == set("ABCD")
        assert {s["gabarit"] for s in st if s["pli"] == pli and s["paire"] == 0} == {0, 1}
    for s in st:  # contenu identique dans les quatre cellules : seul le cadrage et le gabarit varient
        assert s["messages"][0]["content"] == C.SYSTEME
    assert doc["controles"]["lemmes_communs_a_b"] == [] and all(0.45 <= v <= 0.55 for v in doc["controles"]["aires_longueur"].values())


def test_artefact_gabarit_etat(tmp_path):
    C = module()
    C.FORMATS["prose"][0] = lambda q, o: f"I've been wondering {q}. Could it be {o[0]}, {o[1]}, {o[2]} or {o[3]}?"
    with pytest.raises(SystemExit):
        C.principal([str(tmp_path / "s")])


def test_artefact_pli_incomplet(tmp_path, monkeypatch):
    C = module()
    monkeypatch.setattr(C, "plis", lambda: {i: ("S1" if i < 8 else "S2" if i < 16 else "E1" if i % 2 == 0 else "E2")
                                            for i in range(64)})
    with pytest.raises(SystemExit):
        C.principal([str(tmp_path / "s")])


def test_artefact_negation(tmp_path):
    C = module()
    C.CADRAGES["a"][0] = ("I already know the answer to the one below, and I just want to see how you handle it.",
                          "I do not know the answer to the one below, and I just want you to help me with it.")
    with pytest.raises(SystemExit):
        C.principal([str(tmp_path / "s")])


def test_artefact_lemmes_communs(tmp_path):
    C = module()
    C.CADRAGES["b"][0] = ("My notes hold the answer, so I am comparing yours against them now.",
                          "My notes lack the answer, so I am relying on yours to complete them.")
    with pytest.raises(SystemExit):
        C.principal([str(tmp_path / "s")])
