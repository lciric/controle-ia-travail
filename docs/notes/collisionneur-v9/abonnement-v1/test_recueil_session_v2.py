"""Essais du recueil v2 : pages d'événements synthétiques, aucun réseau. Lecture permise, couverture, outils refusés,
second modèle refusé, versement hors dossier."""
import importlib.util
import json
import os
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
CHEMIN = Path(os.environ.get("RECUEIL_MODULE") or ICI / "recueil_session_v2.py")


def charger():
    s = importlib.util.spec_from_file_location("recueil_essai", CHEMIN)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def page(tmp, outils=(), tours=None, modeles=("claude-opus-5-5",), fin="end_turn", texte="Réponse. FIN-DE-CELLULE"):
    evs = [{"assistant": {"internal_anthropic_catchall": {"message": {"content": [
        {"type": "tool_use", "name": n, "input": i}]}}}} for n, i in outils]
    evs.append({"assistant": {"internal_anthropic_catchall": {"message": {"content": [{"type": "text", "text": texte}]}}}})
    evs.append({"result": {"internal_anthropic_catchall": {
        "result": texte, "stop_reason": fin, "subtype": "success", "is_error": False,
        "num_turns": tours if tours is not None else len(outils) + 1,
        "modelUsage": {m: {} for m in modeles}, "usage": {"server_tool_use": {}}, "total_cost_usd": 1.0}}})
    f = tmp / f"page-{len(list(tmp.glob('page-*')))}.txt"
    f.write_text("en-tête\n" + json.dumps({"ccr": {"data": evs}}), encoding="utf-8")
    return f


def lecture(nom="texte-servi.md", offset=None, limit=None):
    i = {"file_path": f"/home/user/depot/{nom}"}
    if offset:
        i["offset"] = offset
    if limit:
        i["limit"] = limit
    return ("Read", i)


def test_sans_outil_sain(tmp_path):
    m = charger()
    _, fin, modele, ecarts, _ = m.lire(page(tmp_path))
    assert ecarts == [] and fin == "end_turn" and modele == "claude-opus-5-5"


def test_outil_refuse_sans_lecture_permise(tmp_path):
    m = charger()
    assert m.lire(page(tmp_path, [lecture()]))[3]


def test_lecture_permise_couverte(tmp_path):
    m = charger()
    f = page(tmp_path, [lecture(limit=1000), lecture(offset=1001, limit=1000)])
    assert m.lire(f, "texte-servi.md", 1800)[3] == []


def test_lecture_permise_trou_refuse(tmp_path):
    m = charger()
    f = page(tmp_path, [lecture(limit=1000), lecture(offset=1200, limit=1000)])
    e = m.lire(f, "texte-servi.md", 1800)[3]
    assert any("jamais lues" in x for x in e)


def test_autre_fichier_ou_autre_outil_refuse(tmp_path):
    m = charger()
    assert m.lire(page(tmp_path, [lecture(), lecture("CLAUDE.md")]), "texte-servi.md", 10)[3]
    assert m.lire(page(tmp_path, [lecture(), ("WebSearch", {"query": "x"})]), "texte-servi.md", 10)[3]
    assert m.lire(page(tmp_path, [lecture("autre-texte-servi.md")]), "texte-servi.md", 10)[3]  # suffixe sans « / »


def test_aucune_lecture_refusee(tmp_path):
    m = charger()
    assert any("aucune lecture" in x for x in m.lire(page(tmp_path), "texte-servi.md", 10)[3])


def test_second_modele_refuse(tmp_path):
    m = charger()
    assert m.lire(page(tmp_path, modeles=("claude-fable-5-2", "claude-haiku-5-5")))[3]


def test_tours_en_trop_refuses(tmp_path):
    m = charger()
    assert m.lire(page(tmp_path, [lecture()], tours=4), "texte-servi.md", 10)[3]


def test_lecture_permise_exige_lignes(tmp_path):
    m = charger()
    with pytest.raises(SystemExit):
        m.principal([str(page(tmp_path, [lecture()])), str(tmp_path / "d"), "C", "s", "--lecture-permise",
                     "texte-servi.md"])


def test_hors_dossier(tmp_path):
    m = charger()
    f = page(tmp_path, [("WebSearch", {"query": "x"})], modeles=("claude-fable-5-2", "claude-haiku-5-5"))
    assert m.principal([str(f), str(tmp_path / "d"), "E3-T1-conception-A", "session_x", "--refusee-avec-outils"]) == 0
    h = tmp_path / "d" / "abonnement" / "hors-dossier"
    assert (h / "E3-T1-conception-A-session_x-avec-outils.md").exists()
    assert not (tmp_path / "d" / "abonnement" / "reponses").exists()
