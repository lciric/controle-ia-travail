"""Greffon de la liste des échecs connus — v1.

Décision de la mère du 21 novembre 2026, vers 21:24Z : les essais de `tests/test_cibles_invisibles_v1.py` et
`tests/test_cibles_invisibles_v2.py` qui échouent ne sont ni retirés ni modifiés ; ils sont exemptés par une liste
documentée, que la suite lit : `tests/echecs-connus-v1.txt` (scellée, compagnon `.sha256`).

Ce que fait le greffon (chargé par une ligne de `tests/conftest.py`) :
- il vérifie la liste contre son empreinte compagnon et refuse la suite si elle manque ou diffère ;
- il refuse toute ligne mal formée, en double, ou qui porte un caractère de motif (`*`, `?`) : des identifiants
  exacts seulement, jamais d'expression ;
- il refuse toute ligne dont le fichier d'essais n'existe pas, et toute ligne dont le fichier est joué mais dont
  l'identifiant ne correspond à aucun essai de ce fichier (ligne fantôme) ; une ligne dont le fichier n'est pas
  joué dans cette passe n'est pas jugée ;
- il marque chaque essai listé « échec attendu » strict (`xfail(strict=True)`) : un essai listé qui passe fait
  échouer la suite (« XPASS(strict) ») ; un essai hors de la liste qui échoue reste un échec.
Aucune autre exemption.
"""
from __future__ import annotations

from pathlib import Path

import pytest

LISTE = Path(__file__).resolve().parent / "echecs-connus-v1.txt"
CARACTERES_DE_MOTIF = ("*", "?")


def lire_liste(chemin: Path = LISTE) -> dict[str, tuple[str, str]]:
    """{identifiant : (motif, référence)} ; lève `pytest.UsageError` sur toute irrégularité."""
    from controle_ia.gardes import GardeArret
    from controle_ia.scellement import verifier

    try:
        verifier(chemin)
    except GardeArret as e:
        raise pytest.UsageError(f"liste des échecs connus refusée : {e}") from None
    entrees: dict[str, tuple[str, str]] = {}
    problemes = []
    for numero, ligne in enumerate(chemin.read_text(encoding="utf-8").splitlines(), start=1):
        if not ligne.strip() or ligne.startswith("#"):
            continue
        champs = ligne.split("\t")
        if len(champs) != 3 or not all(c.strip() for c in champs):
            problemes.append(f"ligne {numero} : trois champs non vides séparés par une tabulation attendus")
            continue
        identifiant, motif, reference = (c.strip() for c in champs)
        fichier = identifiant.split("::", 1)[0]
        if ("::" not in identifiant or fichier.startswith("/") or not fichier.startswith("tests/")
                or not fichier.endswith(".py")):
            problemes.append(f"ligne {numero} : identifiant complet attendu (tests/….py::essai), lu {identifiant!r}")
        elif any(c in identifiant for c in CARACTERES_DE_MOTIF):
            problemes.append(f"ligne {numero} : caractère de motif dans {identifiant!r} (identifiants exacts seulement)")
        elif identifiant in entrees:
            problemes.append(f"ligne {numero} : {identifiant!r} en double")
        else:
            entrees[identifiant] = (motif, reference)
    if problemes:
        raise pytest.UsageError(f"liste des échecs connus refusée ({chemin.name}) : " + " ; ".join(problemes))
    return entrees


def _essais_du_fichier(noeud) -> set[str]:
    """Identifiants de tous les essais sous un nœud collecté (re-collecte, pour une passe restreinte)."""
    trouves = set()
    for enfant in noeud.collect():
        if isinstance(enfant, pytest.Item):
            trouves.add(enfant.nodeid)
        else:
            trouves |= _essais_du_fichier(enfant)
    return trouves


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(session, config, items):
    entrees = lire_liste()
    racine = Path(config.rootpath)
    par_id = {item.nodeid: item for item in items}
    modules = {}
    for item in items:
        modules.setdefault(item.nodeid.split("::", 1)[0], item.getparent(pytest.Module))
    fantomes = []
    for identifiant in entrees:
        fichier = identifiant.split("::", 1)[0]
        if not (racine / fichier).is_file():
            fantomes.append(f"{identifiant} (fichier absent)")
        elif fichier in modules and identifiant not in par_id:
            module = modules[fichier]
            if module is None or identifiant not in _essais_du_fichier(module):
                fantomes.append(f"{identifiant} (aucun essai collecté de ce nom)")
    if fantomes:
        raise pytest.UsageError(f"liste des échecs connus ({LISTE.name}) : ligne(s) sans essai : " + " ; ".join(fantomes))
    for identifiant, (motif, reference) in entrees.items():
        if identifiant in par_id:
            par_id[identifiant].add_marker(pytest.mark.xfail(
                reason=f"échec connu ({LISTE.name}) : {motif} [{reference}]", strict=True))
