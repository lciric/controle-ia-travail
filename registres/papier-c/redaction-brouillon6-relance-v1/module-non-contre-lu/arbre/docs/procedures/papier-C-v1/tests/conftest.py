"""Essais du module du papier C (v1) : chemins et configuration communs.

Lancement (cible nommée, jamais la suite complète du dépôt) :
    PYTHONPATH=src:docs/procedures/papier-C-v1 python -m pytest -q docs/procedures/papier-C-v1/tests
Données : simulées par ces essais seulement ; aucun résultat d'expérience n'est lu.
"""
import copy
import json
import sys
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
MODULE = ICI.parent
RACINE = MODULE.parents[2]
for chemin in (str(MODULE), str(ICI)):
    if chemin not in sys.path:
        sys.path.insert(0, chemin)


def chemin_de_la_configuration() -> Path:
    """La configuration scellée si elle existe, sinon le brouillon 5 relu."""
    scellee = RACINE / "prereg" / "papier-C-config-v1.json"
    return scellee if scellee.is_file() else RACINE / "brouillons" / "papier-C-config-v1-brouillon5.json"


@pytest.fixture(scope="session")
def configuration_brute() -> dict:
    return json.loads(chemin_de_la_configuration().read_text(encoding="utf-8"))


@pytest.fixture()
def cfg(configuration_brute) -> dict:
    return copy.deepcopy(configuration_brute)


def remplir_pour_le_scellement(cfg: dict) -> dict:
    """Copie de la configuration avec les champs du scellement remplis de valeurs factices (essais seulement)."""
    c = copy.deepcopy(cfg)
    c["version"], c["statut"] = "papier-C-config-v1", "scellé (factice, essais)"
    c["graines"]["racine"] = "123456789012345678901234567890"
    for k, j in enumerate(c["juges"]):
        j["revision"] = f"{k:040x}"
    c["partage_taches"]["sha256_source"] = "a" * 64
    c["controlabilite"]["concept"] = "concept factice"
    c["controlabilite"]["consignes"]["pense"] = "consigne factice A"
    c["controlabilite"]["consignes"]["ne_pense_pas"] = "consigne factice B"
    c["controlabilite"]["banc"].update(version="v-factice", licence="licence factice", sha256="b" * 64)
    return c


@pytest.fixture()
def cfg_scellee(cfg) -> dict:
    return remplir_pour_le_scellement(cfg)
