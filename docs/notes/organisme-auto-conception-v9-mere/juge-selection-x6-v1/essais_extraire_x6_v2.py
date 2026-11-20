"""Essais du programme d'extraction du cas X6 — v2. Cas sains et artefacts (R5), sans aucune donnée.

Lancement : `.venv/bin/python -B -m pytest -q docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/essais_extraire_x6_v2.py`
"""
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

_ICI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("x6", _ICI / "extraire_x6_journal_aiguilleur_v2.py")
x6 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(x6)


def test_sain_liste_avec_id():
    d = {"entrees": [{"id": "c-01", "classe": "concret", "categorie": "TEXTE SECRET"},
                     {"id": "c-02", "classe": "a_corriger", "categorie": "x"},
                     {"id": "c-03", "classe": "concret", "categorie": "y"}]}
    r = x6.extraire(d)
    assert r["comptes_par_classe"] == {"a_corriger": 1, "concret": 2}
    assert r["identifiants_par_classe"]["concret"] == ["c-01", "c-03"]
    assert "TEXTE SECRET" not in json.dumps(r)
    assert r["doublons"] == []


def test_sain_id_par_cle_parente():
    d = {"c-01": {"classe": "niveau_methode", "categorie": "z"}, "c-02": {"classe": "concret"}}
    r = x6.extraire(d)
    assert r["source_identifiant"] == {"cle": 0, "parent": 2}
    assert r["identifiants_par_classe"] == {"concret": ["c-02"], "niveau_methode": ["c-01"]}


def test_sain_cle_ident():
    d = {"entrees": [{"ident": "f-07", "classe": "concret", "contenu": "TEXTE"}]}
    r = x6.extraire(d)
    assert r["identifiants_par_classe"] == {"concret": ["f-07"]}
    assert r["source_identifiant"] == {"cle": 1, "parent": 0}
    assert "TEXTE" not in json.dumps(r)


def test_artefact_ident_et_id_differents():
    with pytest.raises(x6.Arret) as e:
        x6.extraire([{"id": "c-01", "ident": "c-02", "classe": "concret"}])
    assert e.value.code == 4


def test_artefact_profondeur():
    d = {"classe": "concret", "id": "c-01"}
    for _ in range(x6.PROFONDEUR_MAX + 2):
        d = {"n": d}
    with pytest.raises(x6.Arret) as e:
        x6.extraire(d)
    assert e.value.code == 6


def test_sain_profondeur_juste_sous_la_borne():
    d = {"classe": "concret", "id": "c-01"}
    for _ in range(x6.PROFONDEUR_MAX - 1):
        d = {"n": d}
    assert x6.extraire(d)["comptes_par_classe"] == {"concret": 1}


def test_doublon_rapporte():
    d = [{"id": "c-01", "classe": "concret"}, {"id": "c-01", "classe": "concret"}]
    assert x6.extraire(d)["doublons"] == ["c-01"]


def test_artefact_aucune_classe():
    with pytest.raises(x6.Arret) as e:
        x6.extraire({"a": [{"verdict": "texte libre"}]})
    assert e.value.code == 3
    assert "texte libre" not in json.dumps(e.value.details)


def test_artefact_identifiant_absent():
    with pytest.raises(x6.Arret) as e:
        x6.extraire([{"classe": "concret"}])
    assert e.value.code == 4


def test_artefact_identifiant_texte_libre():
    with pytest.raises(x6.Arret) as e:
        x6.extraire([{"id": "une phrase entière avec des espaces", "classe": "concret"}])
    assert e.value.code == 4
    assert "phrase" not in json.dumps(e.value.details)


def test_artefact_identifiants_ambigus():
    with pytest.raises(x6.Arret) as e:
        x6.extraire([{"id": "c-01", "fiche_id": "c-02", "classe": "concret"}])
    assert e.value.code == 4


def test_artefact_classe_illisible():
    with pytest.raises(x6.Arret) as e:
        x6.extraire([{"id": "c-01", "classe": "Classe Libre !"}])
    assert e.value.code == 5
    assert "Libre" not in json.dumps(e.value.details)


def _depot(tmp_path, fichiers):
    d = tmp_path / "depot"
    d.mkdir()
    subprocess.run(["git", "init", "-q", str(d)], check=True)
    for nom, contenu in fichiers.items():
        p = d / nom
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(contenu, encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(d), "-c", "user.name=e", "-c", "user.email=e@e", "commit", "-q", "-m", "e"], check=True)
    tete = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
    return d, tete


SUF = "/generation-1/aiguillage/journal-aiguillage.json"


def test_principal_sain(tmp_path):
    d, c = _depot(tmp_path, {"a/x" + SUF: json.dumps([{"id": "c-01", "classe": "concret"}]),
                             "a/autre.json": "{}"})
    s = tmp_path / "s.json"
    assert x6.principal(["--depot", str(d), "--commit", c, "--suffixe", SUF, "--sortie", str(s)]) == 0
    r = json.loads(s.read_text())
    assert r["issue"] == "conforme" and r["fichiers_trouves"] == 1
    assert r["extraction"]["identifiants_par_classe"] == {"concret": ["c-01"]}
    assert len(r["sha256_journal"]) == 64


def test_principal_artefact_aucun_fichier(tmp_path):
    d, c = _depot(tmp_path, {"a/autre.json": "{}"})
    s = tmp_path / "s.json"
    assert x6.principal(["--depot", str(d), "--commit", c, "--suffixe", SUF, "--sortie", str(s)]) == 2
    r = json.loads(s.read_text())
    assert r["fichiers_trouves"] == 0 and "chemin" not in r


def test_principal_artefact_deux_fichiers(tmp_path):
    d, c = _depot(tmp_path, {"a/x" + SUF: "[]", "b/y" + SUF: "[]"})
    s = tmp_path / "s.json"
    assert x6.principal(["--depot", str(d), "--commit", c, "--suffixe", SUF, "--sortie", str(s)]) == 2
    assert "chemin" not in json.loads(s.read_text())


def test_principal_artefact_json_illisible(tmp_path):
    d, c = _depot(tmp_path, {"a/x" + SUF: "{pas du json"})
    s = tmp_path / "s.json"
    assert x6.principal(["--depot", str(d), "--commit", c, "--suffixe", SUF, "--sortie", str(s)]) == 6
