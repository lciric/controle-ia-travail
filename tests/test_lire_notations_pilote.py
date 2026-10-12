"""Lecture des notations refaites du pilote de T0.5 (N-021) : équivalence avec `analyser` (mêmes notations, lues dans le
dossier du pilote ou dans un run distinct), gardes (cas sain et artefact, R5), juge échu."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.environnements import lire_notations_pilote as lnp
from controle_ia.environnements import lire_pilote as lp
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, verifier_resultat
from test_lire_pilote import ANALYSE, ENTROPIE, REEL, RUN, _jusqu_a_l_analyse

NOTATIONS = "20261012-200000-t05-notations-jouet"
LECTURE = "20261012-210000-t05-lecture-juges-jouet"


@pytest.fixture(autouse=True)
def _code_du_vrai_depot(monkeypatch):
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)


def _depot(tmp_path_factory, nom):
    d = tmp_path_factory.mktemp(nom)
    for args in (("init", "-q", "-b", "main"), ("config", "user.email", "t@example.invalid"),
                 ("config", "user.name", "t")):
        subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True)
    (d / "README").write_text("x\n")
    committer(d)
    return d


def _modules_notations(depot: Path) -> None:
    for m in lnp.MODULES_NOTATIONS:
        (depot / m).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REEL / m, depot / m)


def _notations_de(depot: Path, juge: str) -> list[dict]:
    return json.loads((depot / "diag" / RUN / f"notations-{juge}-decisives.json").read_text())["resultat"]["notations"]


def _run_des_notations(depot: Path, notations: dict, run_pilote: str = RUN) -> None:
    _modules_notations(depot)
    committer(depot)
    chemin, _ = creer_manifeste(depot, NOTATIONS, {"run_pilote": run_pilote}, ["x"], entropie=ENTROPIE)
    for j, n in notations.items():
        ecrire_resultat(depot, chemin, f"notations-{j}-decisives", {"notations": n})
    committer(depot)


def _pilote_complet_et_pilote_arrete(tmp_path_factory):
    """A : pilote arrêté pendant les notations de D (décisives écrites dans son dossier), lu par `analyser`. B : le même
    pilote arrêté pendant les notations décisives du 8B, première analyse faite (juges en nœud)."""
    a, ta = _depot(tmp_path_factory, "a"), tmp_path_factory.mktemp("travail-a")
    _jusqu_a_l_analyse(a, ta, etapes="descriptives")
    lecture_a = lp.analyser(a, RUN, ANALYSE, a / "taches.json")
    committer(a)
    b, tb = _depot(tmp_path_factory, "b"), tmp_path_factory.mktemp("travail-b")
    _jusqu_a_l_analyse(b, tb, etapes="decisives-8B")
    lecture_b = lp.analyser(b, RUN, ANALYSE, b / "taches.json")
    committer(b)
    assert all(lecture_b["juges"][j]["plan_b"] == "nœud" for j in ("8B", "3B"))
    return a, lecture_a, b, lecture_b


def test_equivalence_avec_analyser(tmp_path_factory):
    a, lecture_a, b, lecture_b = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b, {j: _notations_de(a, j) for j in ("8B", "3B")})
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    s = lp._serialisable
    assert s(lecture["juges"]) == s(lecture_a["juges"])
    assert s(lecture["difference_appariee"]) == s(lecture_a["difference_appariee"])
    assert all(lecture["predictions"][k] == lecture_a["predictions"][k] for k in ("P2", "P3"))
    assert lecture["relectures_audit"] == lecture_a["relectures_audit"]
    assert lecture_a["juges"]["8B"]["decomposition_concluante"]                       # cas non trivial
    assert all(lecture["predictions"][k] == lecture_b["predictions"][k] for k in lnp.PREDICTIONS_DE_LA_PREMIERE_LECTURE)
    r = verifier_resultat(b, b / "diag" / LECTURE / "lecture-juges.json")
    assert r["resultat"]["run_notations"] == NOTATIONS and r["resultat"]["arbre_propre"]
    assert not list((b / "diag" / RUN).glob("notations-*"))                          # dossier du pilote intact


def test_juge_echu_lu_en_noeud(tmp_path_factory):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b, {"8B": _notations_de(a, "8B")})
    lecture = lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    assert lecture["juges"]["8B"]["decomposition_concluante"] and lecture["juges"]["3B"]["plan_b"] == "nœud"
    assert lecture["predictions"]["P3"] == "non concluant"


def test_gardes_cas_sain_et_artefacts(tmp_path_factory, monkeypatch):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    n8, n3 = _notations_de(a, "8B"), _notations_de(a, "3B")
    # artefact : une notation désalignée (empreinte de l'ensemble noté)
    altere = [dict(n8[0], ensemble_sha256="0" * 64)] + n8[1:]
    _run_des_notations(b, {"8B": altere, "3B": n3})
    with pytest.raises(GardeArret, match="désalignement"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    assert not (b / "runs" / LECTURE).exists()


def test_gardes_de_rattachement_et_de_modules(tmp_path_factory, monkeypatch):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    # artefact : le dossier du pilote porte déjà des notations décisives (pilote A)
    _run_des_notations(a, {j: _notations_de(a, j) for j in ("8B", "3B")})
    with pytest.raises(GardeArret, match="porte des notations décisives"):
        lnp.lire_notations(a, RUN, NOTATIONS, ANALYSE, a / "taches.json", LECTURE)
    # artefact : run des notations rattaché à un autre pilote
    _run_des_notations(b, {j: _notations_de(a, j) for j in ("8B", "3B")}, run_pilote="20261010-120001-autre")
    with pytest.raises(GardeArret, match="rattaché au pilote"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)


def test_modules_modifies_et_predictions_divergentes(tmp_path_factory, monkeypatch):
    a, _, b, _ = _pilote_complet_et_pilote_arrete(tmp_path_factory)
    _run_des_notations(b, {j: _notations_de(a, j) for j in ("8B", "3B")})
    # artefact : module des notations modifié après le commit du run des notations
    m = b / lnp.MODULES_NOTATIONS[1]
    texte = m.read_text()
    m.write_text(texte + "\n# modifié\n")
    with pytest.raises(GardeArret, match="modules des notations modifiés"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE, autoriser_depot_sale=True)
    m.write_text(texte)
    # artefact : module de lecture gelé modifié (garde gelée d'`_ouvrir_analyse`)
    g = b / lp.MODULES_LECTURE[1]
    texte_g = g.read_text()
    g.write_text(texte_g + "\n# modifié\n")
    with pytest.raises(GardeArret, match="modules de lecture modifiés"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE, autoriser_depot_sale=True)
    g.write_text(texte_g)
    # artefact : une prédiction de la première lecture qui ne se retrouve pas
    vraie = lnp.predictions
    monkeypatch.setattr(lnp, "predictions", lambda *x: {**vraie(*x), "P1": "inventée"})
    with pytest.raises(GardeArret, match="recalculées ≠ celles de la première lecture"):
        lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)
    monkeypatch.setattr(lnp, "predictions", vraie)
    assert not (b / "runs" / LECTURE).exists()
    lnp.lire_notations(b, RUN, NOTATIONS, ANALYSE, b / "taches.json", LECTURE)          # cas sain
