"""Garde de tous les essais du dépôt : aucun sous-processus d'un essai ne doit agir sur un dépôt réel par des variables git
héritées (incident du § 7 de `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon5-et-code-v2-v1.md` : `pytest` lancé
avec `GIT_DIR` pointé sur le dépôt principal, un essai à dépôt jouet y a écrit un commit, l'index et deux réglages ; décision de
la mère R-2919, point 7). Fichier neuf à la racine (R12 : aucun fichier existant modifié) ; il est lu par `pytest` avant
`tests/conftest.py` et avant tout module d'essais.

Retirées de `os.environ` dès l'import de ce fichier, donc pour toute la session et pour tous les sous-processus qui héritent de
l'environnement : `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_COMMON_DIR`, `GIT_OBJECT_DIRECTORY` ; remises à la fin de
la session. **Version restreinte** (réserve 1 de `etat-corrections-v3-en-cours-v1.md`, demande de la mère) : les `GIT_CONFIG*`
(réglages réseau de la session) et `GIT_ALTERNATE_OBJECT_DIRECTORIES` ne sont plus retirées. Preuve :
`tests/test_essais_git_propres_bbis_v2.py` (sous `GIT_DIR` pointé vers un dépôt jouet témoin, rien n'y bouge ; artefact : sans la
garde, le témoin bouge)."""
import os

import pytest

VARIABLES_GIT = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_OBJECT_DIRECTORY")


def variables_git_dangereuses(env) -> list:
    return sorted(k for k in env if k in VARIABLES_GIT)


def _retirer() -> dict:
    return {k: os.environ.pop(k) for k in variables_git_dangereuses(os.environ)}


_RETIREES = _retirer()


@pytest.fixture(scope="session", autouse=True)
def _environnement_git_propre():
    vues = _retirer()
    yield
    for k, v in {**_RETIREES, **vues}.items():
        os.environ.setdefault(k, v)
