"""Copie expurgée du dépôt (`scripts/depot_expurge.py`, R-104) : l'appariement des retraits ne traverse pas les
dossiers, et aucun fichier que le code charge n'est retiré (cas sain et artefact, R5)."""
from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("depot_expurge", RACINE / "scripts" / "depot_expurge.py")
de = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(de)


def test_appariement_par_segment():
    assert de.correspond("docs/sources/invites-2606.07054-v1/invites/B1.txt",
                         "docs/sources/invites-2606.07054-v1/invites/*.txt")
    assert not de.correspond("docs/sources/invites-2606.07054-v1/derivees/B1-env-a-v1.txt",
                             "docs/sources/invites-2606.07054-v1/*.txt")          # le défaut de la première version
    assert not de.correspond("docs/sources/invites-2606.07054-v1/verification.txt",
                             "docs/sources/invites-2606.07054-v1/invites/*.txt")  # nos vérifications restent
    assert de.correspond("donnees/run/sorties.tar", "donnees/**")
    assert not de.correspond("donnees-bis/x", "donnees/**")


def test_fichiers_charges_par_le_code_jamais_retires():
    suivis = subprocess.run(["git", "-C", str(RACINE), "ls-files"], capture_output=True, text=True,
                            check=True).stdout.split("\n")
    charges = [f for f in suivis if any(de.correspond(f, g) for g in de.GARDES)]
    assert len(charges) == 26                       # 18 invites et leur index ; 6 gabarits adaptés et leur index
    assert all(de.motif_de(f) is None for f in charges)


def test_retrait_d_un_fichier_charge_arrete(monkeypatch):
    monkeypatch.setattr(de, "RETRAITS", de.RETRAITS + [("docs/sources/invites-2606.07054-v1/derivees/*.txt", "x")])
    with pytest.raises(SystemExit, match="chargé par le code"):
        de.motif_de("docs/sources/invites-2606.07054-v1/derivees/B1-env-a-v1.txt")
