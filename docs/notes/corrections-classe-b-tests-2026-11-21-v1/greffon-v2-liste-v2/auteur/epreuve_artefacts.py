"""Épreuve des artefacts du greffon v2 dans des bacs jetables (un par cas), sous le dossier de travail.

Chaque bac : pyproject (racine), tests/conftest.py et tests/greffon_echecs_connus_v{1,2}.py copiés octet pour octet
de l'arbre de travail, trois fichiers d'essais synthétiques, une liste scellée propre au cas.
Usage : python epreuve_artefacts.py ARBRE DOSSIER_SORTIES
"""
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

ARBRE = Path(sys.argv[1]).resolve()
SORTIES = Path(sys.argv[2]).resolve()
ICI = Path(__file__).resolve().parent
BACS = ICI / "bacs"
PY = "/home/user/controle-ia-travail/.venv/bin/python"
ENV = {**os.environ, "PYTHONPATH": str(ARBRE / "src")}

ESSAIS = {
    "test_echoue.py": "def test_a():\n    assert False\n\n\ndef test_b():\n    assert 1 == 2\n",
    "test_passe.py": "def test_ok():\n    assert True\n",
    "test_saute.py": ("import pytest\n\npytest.skip('sauté en bloc pour l\\'épreuve', allow_module_level=True)\n\n\n"
                      "def test_x():\n    assert False\n"),
}
REF = "épreuve\tbac"


def ligne(ident):
    return f"{ident}\t{REF}\n"


SAINES = [ligne("tests/test_echoue.py::test_a"), ligne("tests/test_echoue.py::test_b")]

# (nom, lignes de la liste, altération après scellement, arguments, version du greffon)
CAS = [
    ("10-sain", SAINES, None, [], 2),
    ("11-fantome", SAINES + [ligne("tests/test_echoue.py::test_z")], None, [], 2),
    ("12-liste-alteree", SAINES, "altere", [], 2),
    ("13-empreinte-absente", SAINES, "sans_empreinte", [], 2),
    ("14-doublon", SAINES + [SAINES[0]], None, [], 2),
    ("15-fichier-absent", SAINES + [ligne("tests/test_inexistant.py::test_a")], None, [], 2),
    ("16-exempte-qui-passe", SAINES + [ligne("tests/test_passe.py::test_ok")], None, [], 2),
    ("17-saute-en-bloc-liste", SAINES + [ligne("tests/test_saute.py::test_x")], None, [], 2),
    ("18-saute-en-bloc-liste-v1", SAINES + [ligne("tests/test_saute.py::test_x")], None, [], 1),
    ("19-saute-en-bloc-non-liste", SAINES, None, [], 2),
    ("20-saute-en-bloc-liste-fichier-non-joue", SAINES + [ligne("tests/test_saute.py::test_x")], None,
     ["tests/test_echoue.py"], 2),
    ("21-runxfail", SAINES, None, ["--runxfail"], 2),
    ("22-runxfail-v1", SAINES, None, ["--runxfail"], 1),
    ("23-motif", SAINES + [ligne("tests/test_echoue.py::test_*")], None, [], 2),
]


def empreinte(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def construire(nom, lignes, alteration, version):
    bac = BACS / nom
    if bac.exists():
        shutil.rmtree(str(BACS) + "/" + nom)  # chemin gardé : toujours sous BACS
    (bac / "tests").mkdir(parents=True)
    (bac / "pyproject.toml").write_text('[tool.pytest.ini_options]\npythonpath = ["tests"]\ntestpaths = ["tests"]\n')
    for f in ("greffon_echecs_connus_v1.py", "greffon_echecs_connus_v2.py"):
        shutil.copyfile(ARBRE / "tests" / f, bac / "tests" / f)
        assert empreinte(bac / "tests" / f) == empreinte(ARBRE / "tests" / f)
    conftest = (ARBRE / "tests/conftest.py").read_text(encoding="utf-8")
    if version == 1:  # même conftest, la seule ligne de chargement remise vers le v1
        lignes_c = conftest.splitlines(keepends=True)
        idx = [i for i, l in enumerate(lignes_c) if l.startswith("from greffon_echecs_connus_v2 import")]
        assert len(idx) == 1
        lignes_c[idx[0]] = ("from greffon_echecs_connus_v1 import pytest_collection_modifyitems  # noqa: F401 — "
                            "liste des échecs connus (décision de la mère, 21 novembre 2026)\n")
        conftest = "".join(lignes_c)
    (bac / "tests/conftest.py").write_text(conftest, encoding="utf-8")
    for f, texte in ESSAIS.items():
        (bac / "tests" / f).write_text(texte, encoding="utf-8")
    liste = bac / "tests" / f"echecs-connus-v{version}.txt"
    liste.write_text("# liste d'épreuve\n" + "".join(lignes), encoding="utf-8")
    r = subprocess.run([PY, "-m", "controle_ia.scellement", "sceller", str(liste)], env=ENV,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    if alteration == "altere":
        with liste.open("a", encoding="utf-8") as fh:
            fh.write(ligne("tests/test_passe.py::test_ok"))
    elif alteration == "sans_empreinte":
        Path(str(liste) + ".sha256").unlink()
    return bac


def main():
    SORTIES.mkdir(parents=True, exist_ok=True)
    resume = []
    for nom, lignes, alteration, args, version in CAS:
        bac = construire(nom, lignes, alteration, version)
        cmd = [PY, "-m", "pytest", "-rA", "-p", "no:cacheprovider", *args]
        r = subprocess.run(cmd, cwd=bac, env=ENV, capture_output=True, text=True)
        sortie = SORTIES / f"{nom}.txt"
        sortie.write_text(f"$ (cwd={bac}) {' '.join(cmd)}\ncode de sortie : {r.returncode}\n\n{r.stdout}\n--- stderr ---\n{r.stderr}",
                          encoding="utf-8")
        derniere = [l for l in (r.stdout + r.stderr).splitlines() if l.strip()]
        erreur = [l for l in derniere if l.startswith("ERROR:")]
        bilan = erreur[0] if erreur else (derniere[-1] if derniere else "")
        resume.append(f"{nom}\tcode={r.returncode}\t{bilan[:260]}")
    (SORTIES / "resume-artefacts.txt").write_text("\n".join(resume) + "\n", encoding="utf-8")
    print("\n".join(resume))


main()
