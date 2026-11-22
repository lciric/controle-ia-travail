"""Essais (R5) de l'amorce de T0.8 (`scripts/amorce_instance_t08_v1.sh`), artefacts du clonage : un fichier interdit présent sur
l'instance arrête avant tout calcul (dans la branche d'entrée : garde précoce, avant l'installation ; dans les objets git du code :
garde du code `entrees_v1.exiger_instance_sans_interdits`, avant les essais et la course) ; une branche d'entrée déplacée depuis
les contrôles arrête. Le cas sain est l'essai de bout en bout (`scripts/essai_jouet_chaine_t08_v1.py`, joué deux fois, rapport).
Hors de la liste figée de la machine (ces essais construisent un dépôt par `git archive` du dépôt courant)."""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("essai_chaine_t08", RACINE / "scripts" / "essai_jouet_chaine_t08_v1.py")
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)


@pytest.mark.parametrize("cas", ["interdit_dans_entree", "interdit_dans_code", "entree_deplacee"])
def test_amorce_artefacts_du_clonage(tmp_path, cas):
    d = tmp_path / "essai"
    m = E.construire(d, "20261122-120000", 12345, interdit_code=cas == "interdit_dans_code",
                     interdit_entree=cas == "interdit_dans_entree")
    sup = {"ENTREE_COMMIT": "0" * 40} if cas == "entree_deplacee" else {}
    r = E.jouer(d, m, "artefact", sup)
    sortie = (d / "amorce-sortie.txt").read_text(encoding="utf-8")
    assert r["code"] != 0 and not r["fin_normale"], sortie[-2000:]
    assert "refus" in (r["detruire"] or ""), sortie[-2000:]
    assert "run : " not in sortie and "suite ciblée" not in sortie, sortie[-2000:]              # ni essais ni course
    if cas == "interdit_dans_entree":
        assert "fichier interdit présent sur l'instance après le clonage" in sortie and "lecture-sondes-t06.json" in sortie
        assert "installation" not in sortie
    elif cas == "interdit_dans_code":
        assert "gardes avant tout calcul" in sortie and "objet git diag/20261004-104156-harnais-factice/resume.json" in sortie
    else:
        assert "branche d'entrée" in sortie and "≠ commit des contrôles" in sortie
