"""Essais du module des autres moniteurs et de la lecture commune du bras A, version 11. La version 11 ne change que
l'empreinte inscrite du programme de préparation des lectures (version 3) ; aucun calcul, aucune garde. Les essais de
la version 10 éprouvent tout le reste ; ceux-ci éprouvent que la différence est bien celle-là, et la production avec la
préparation v3 (cas sain) et v2 (artefact). La lecture commune de bout en bout avec la v11 est jouée par les essais du
lanceur (`tests/test_bras_a_v2_habilite_lanceur_discretion_v1.py`).

Essais ciblés :
    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_autres_moniteurs_v11.py
"""
from __future__ import annotations

import ast
import difflib
import hashlib
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v10 as A10
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v11 as A

RACINE = Path(__file__).resolve().parents[1]
PAQUET = RACINE / "src/controle_ia/organismes_discrets/bras_a_v2_habilite"
PREPARATION_V3 = "src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py"


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def test_la_seule_difference_avec_la_version_10():
    """Hors de l'en-tête (paragraphe « Version 11 »), seules les deux lignes de la préparation dans
    `PROGRAMMES_DE_PRODUCTION` diffèrent."""
    v10 = (PAQUET / "autres_moniteurs_v10.py").read_text(encoding="utf-8").splitlines()
    v11 = (PAQUET / "autres_moniteurs_v11.py").read_text(encoding="utf-8").splitlines()
    retirees = [l[1:] for l in difflib.unified_diff(v10, v11, lineterm="", n=0)
                if l.startswith("-") and not l.startswith("---")]
    ajoutees = [l[1:] for l in difflib.unified_diff(v10, v11, lineterm="", n=0)
                if l.startswith("+") and not l.startswith("+++")]
    assert retirees == ['                                 "preparation_des_lectures_v2.py",',
                        '                                 "6dfd2bfc6989bd8a90ec40648bda653f5f8383e157c3c521e6d9a488f582debd"),']
    entete = ajoutees[:-2]
    pleines = [l for l in entete if l]
    assert pleines[0].startswith("Version 11, pour le lanceur") and len(entete) - len(pleines) == 1
    entete_du_module = ast.get_docstring(ast.parse("\n".join(v11)), clean=False)
    assert all(l in entete_du_module.splitlines() for l in entete)          # ces lignes sont dans l'en-tête seul
    assert ajoutees[-2:] == ['                                 "preparation_des_lectures_v3.py",',
                             f'                                 "{_sha(RACINE / PREPARATION_V3)}"),']
    # le corps exécutable est le même à ces deux lignes près : mêmes fonctions, mêmes constantes
    noms = lambda m: sorted(n.name for n in ast.parse(m).body if isinstance(n, (ast.FunctionDef, ast.ClassDef)))  # noqa: E731
    assert noms("\n".join(v10)) == noms("\n".join(v11))


def test_programmes_de_production_preparation_v3():
    assert A.empreintes_des_programmes(RACINE) == {
        "moniteurs_a_modele_de_langue": A10.PROGRAMMES_DE_PRODUCTION["moniteurs_a_modele_de_langue"][1],
        "preparation_des_lectures": _sha(RACINE / PREPARATION_V3)}
    A.exiger_programmes(A.empreintes_des_programmes(RACINE))                             # cas sain
    with pytest.raises(GardeArret, match="≠ inscrites"):                                 # artefact : la préparation v2
        A.exiger_programmes({n: s for n, (_, s) in A10.PROGRAMMES_DE_PRODUCTION.items()})


def test_production_ecrite_avec_la_v11_lue_par_la_v11_seule(tmp_path):
    registre = tmp_path / "registre.md"
    registre.write_text(f"| {A.CLE_TABLE_B} | 2026-12-01T09:00:00Z | f | {'b' * 64} |\n"
                        f"| {A.CLE_ISSUE_DE_LA_BASE} | 2026-12-01T10:00:00Z | f | {'a' * 64} |\n", encoding="utf-8")
    lectures = [{"cle": f"{i:016x}", "score": float(i), "balise": A.ETATS_BALISE[0], "jointure": A.JOINTURES[0],
                 "masse_faible": False} for i in range(4)]
    e = A.ecrire_la_production(tmp_path / "p", A.JUGE, lectures, registre, "e" * 64, racine=RACINE)
    assert A.lire_la_production(e["manifeste"])["programmes"]["preparation_des_lectures"] == _sha(RACINE / PREPARATION_V3)
    with pytest.raises(GardeArret, match="≠ inscrites"):
        A10.lire_la_production(e["manifeste"])


IMPORTS_PERMIS = {"__future__", "argparse", "copy", "hashlib", "importlib.util", "json", "math", "re", "sys",
                  "unicodedata", "collections", "datetime", "pathlib", "numpy", "torch", "tokenizers", "jinja2",
                  "jinja2.sandbox"}
INTERNES_PERMIS = {"", "gardes", "scellement", "manifeste", "bases", "environnements.pilote_a",
                   "environnements.propositions", "harnais.modeles"}
CHARGEMENT_PAR_CHEMIN_PERMIS = {f"autres_moniteurs_v{k}.py" for k in range(1, 12)}


def violations(dossier: Path) -> list[str]:
    """Garde statique du paquet, celle des essais de la version 10, la liste des modules qui chargent la pièce source
    à son empreinte portant la version 11."""
    vues = []
    for chemin in sorted(dossier.glob("*.py")):
        source = chemin.read_text(encoding="utf-8")
        for n in ast.walk(ast.parse(source)):
            noms = [a.name for a in n.names] if isinstance(n, ast.Import) else \
                [("." * n.level) + (n.module or "")] if isinstance(n, ast.ImportFrom) else []
            for nom in noms:
                if not (nom[3:] in INTERNES_PERMIS if nom.startswith("...") else nom in IMPORTS_PERMIS):
                    vues.append(f"{chemin.name} importe {nom}")
        if "spec_from_file_location" in source and chemin.name not in CHARGEMENT_PAR_CHEMIN_PERMIS:
            vues.append(f"{chemin.name} charge un fichier par son chemin")
    return vues


def test_garde_statique_du_paquet_avec_la_version_11(tmp_path):
    assert violations(PAQUET) == []
    (tmp_path / "plante.py").write_text("import importlib.util\nimportlib.util.spec_from_file_location('x', 'y')\n",
                                        encoding="utf-8")
    assert violations(tmp_path) == ["plante.py charge un fichier par son chemin"]
