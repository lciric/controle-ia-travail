"""Épreuves du greffon v2 sur essais synthétiques, dans bac/sb/. Écrit tables/cas.tsv."""
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

D = Path("/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-greffon-v2-b")
BAC = D / "bac"
SB = BAC / "sb"
if SB.exists():
    shutil.rmtree(SB)
SB.mkdir()

CONFTEST = "from greffon_echecs_connus_v2 import pytest_collection_modifyitems, pytest_collectreport  # noqa\n"
TEST_A = '''import pytest

def test_ok():
    assert True

def test_ko():
    assert False

def test_ko2():
    assert False

@pytest.mark.parametrize("x", [1, 2])
def test_p(x):
    assert x == 3

class TestC:
    def test_m(self):
        assert False
'''
TEST_B = "def test_b():\n    assert True\n"
FILES = {
    "tests/test_a.py": TEST_A,
    "tests/test_b.py": TEST_B,
    "tests/test_skipbloc.py": 'import pytest\npytest.skip("bloc", allow_module_level=True)\n\ndef test_s():\n    assert False\n',
    "tests/test_importorskip.py": 'import pytest\npytest.importorskip("module_qui_n_existe_pas_xyz")\n\ndef test_s():\n    assert False\n',
    "tests/test_vide.py": "def helper():\n    return 1\n",
    "tests/test_marque_skip.py": 'import pytest\npytestmark = pytest.mark.skip(reason="x")\n\ndef test_s():\n    assert False\n',
    "tests/test_xfail_propre.py": 'import pytest\n\n@pytest.mark.xfail(strict=False)\ndef test_s():\n    assert True\n',
}


def ligne(i):
    return f"{i}\tmotif\tref"


def mk(name, lignes, files=None, seal=True, tamper_after=None, tamper_both=None, conftest=CONFTEST):
    r = SB / name
    (r / "tests").mkdir(parents=True)
    (r / "pyproject.toml").write_text('[tool.pytest.ini_options]\npythonpath = ["tests"]\ntestpaths = ["tests"]\n')
    (r / "tests/conftest.py").write_text(conftest)
    shutil.copy(BAC / "tests/greffon_echecs_connus_v2.py", r / "tests/greffon_echecs_connus_v2.py")
    for f, c in (files or FILES).items():
        (r / f).parent.mkdir(parents=True, exist_ok=True)
        (r / f).write_text(c)
    liste = r / "tests/echecs-connus-v2.txt"
    liste.write_text("# essai\n" + "\n".join(lignes) + "\n")
    if seal:
        h = hashlib.sha256(liste.read_bytes()).hexdigest()
        (r / "tests/echecs-connus-v2.txt.sha256").write_text(f"{h}  echecs-connus-v2.txt\n")
    if tamper_after:
        with liste.open("a") as fh:
            fh.write(tamper_after + "\n")
    if tamper_both:
        with liste.open("a") as fh:
            fh.write(tamper_both + "\n")
        h = hashlib.sha256(liste.read_bytes()).hexdigest()
        (r / "tests/echecs-connus-v2.txt.sha256").write_text(f"{h}  echecs-connus-v2.txt\n")
    return r


def run(r, args, env_extra=None):
    env = dict(os.environ)
    env.update(PYTHONDONTWRITEBYTECODE="1", PYTHONPATH=str(BAC / "src"), TMPDIR=str(D / "tables"))
    env.pop("PYTEST_ADDOPTS", None)
    if env_extra:
        env.update(env_extra)
    p = subprocess.run([sys.executable, "-m", "pytest", "-p", "no:cacheprovider", f"--rootdir={r}", "-q", "-rxX", *args],
                       cwd=r, env=env, capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip().splitlines()
    resume = " | ".join(l for l in out if ("passed" in l or "failed" in l or "xfailed" in l or "error" in l.lower()
                                            or "no tests ran" in l or "skipped" in l or "XPASS" in l or "refus" in l)
                        )[:300]
    return p.returncode, resume


T = "tests/test_a.py::"
rows = []


def cas(nom, attendu, r, args=(), env_extra=None):
    code, resume = run(r, list(args), env_extra)
    ok = "OK" if str(code) == str(attendu) else "ECART"
    rows.append((nom, attendu, code, ok, resume))
    print(nom, attendu, code, ok, flush=True)


# 1 ligne fantôme
cas("1a fantome (objet faux)", 4, mk("c1a", [ligne(T + "test_nope")]))
cas("1b sain (objet vrai)", 0, mk("c1b", [ligne(T + "test_ko")]), ["tests/test_a.py::test_ok", "tests/test_a.py::test_ko"])
# 2 liste altérée
cas("2a liste alteree apres scellement", 4, mk("c2a", [ligne(T + "test_ko")], tamper_after=ligne(T + "test_ko2")))
cas("2b liste scellee intacte", 0, mk("c2b", [ligne(T + "test_ko")]), ["tests/test_a.py::test_ok", "tests/test_a.py::test_ko"])
cas("2c liste ET compagnon alteres ensemble (objet: exemption elargie)", "0?", mk("c2c", [ligne(T + "test_ko")], tamper_both=ligne(T + "test_ko2")),
    ["tests/test_a.py::test_ko", "tests/test_a.py::test_ko2"])
cas("2d compagnon absent", 4, mk("c2d", [ligne(T + "test_ko")], seal=False))
# 3 doublon
cas("3a doublon", 4, mk("c3a", [ligne(T + "test_ko"), ligne(T + "test_ko")]))
cas("3b sans doublon", 0, mk("c3b", [ligne(T + "test_ko"), ligne(T + "test_ko2")]), ["tests/test_a.py::test_ko", "tests/test_a.py::test_ko2"])
# 4 fichier absent
cas("4a fichier absent", 4, mk("c4a", [ligne("tests/test_absent.py::test_x")]))
cas("4b fichier present", 0, mk("c4b", [ligne(T + "test_ko")]), ["tests/test_a.py::test_ko"])
# 5 exempté qui passe
cas("5a exempte qui passe (strict)", 1, mk("c5a", [ligne(T + "test_ok")]), ["tests/test_a.py"])
cas("5b exempte qui echoue", 0, mk("c5b", [ligne(T + "test_ko")]), ["tests/test_a.py::test_ko"])
# 6 module sauté en bloc
cas("6a skip bloc, ligne listee (R-A)", 4, mk("c6a", [ligne("tests/test_skipbloc.py::test_s")]))
cas("6b skip bloc, NON liste", 0, mk("c6b", [ligne(T + "test_ko")]), ["tests/test_skipbloc.py", "tests/test_b.py"])
cas("6c importorskip, ligne listee (R-A)", 4, mk("c6c", [ligne("tests/test_importorskip.py::test_s")]))
cas("6d module sans aucun essai collecte (non saute), ligne listee", "4?", mk("c6d", [ligne("tests/test_vide.py::test_x")]), ["tests/test_vide.py", "tests/test_b.py"])
cas("6e module marque skip (pytestmark), ligne listee", "?", mk("c6e", [ligne("tests/test_marque_skip.py::test_s")]), ["tests/test_marque_skip.py"])
cas("6f skip bloc ligne listee, run par dossier tests (defaut)", 4, mk("c6f", [ligne("tests/test_skipbloc.py::test_s")]), ["tests"])
cas("6g skip bloc ligne listee, run par argument fichier seul", 4, mk("c6g", [ligne("tests/test_skipbloc.py::test_s")]), ["tests/test_skipbloc.py"])
# 7 runxfail
cas("7a --runxfail (R-B)", 4, mk("c7a", [ligne(T + "test_ko")]), ["--runxfail"])
cas("7b sans --runxfail", 0, mk("c7b", [ligne(T + "test_ko")]), ["tests/test_a.py::test_ko"])
cas("7c PYTEST_ADDOPTS=--runxfail", 4, mk("c7c", [ligne(T + "test_ko")]), ["tests/test_a.py::test_ko"], {"PYTEST_ADDOPTS": "--runxfail"})
cas("7d --runxfail sans aucun essai collecte (-k absent)", 4, mk("c7d", [ligne(T + "test_ko")]), ["--runxfail", "-k", "zzz_rien"])
# 8 désélection
cas("8a -k deselectionne l'essai liste", "0", mk("c8a", [ligne(T + "test_ko")]), ["tests/test_a.py", "-k", "test_ok"])
cas("8b --deselect de l'essai liste", "0", mk("c8b", [ligne(T + "test_ko")]), ["tests/test_a.py", f"--deselect={T}test_ko", "-k", "test_ok"])
cas("8c fantome + -k qui deselectionne tout", 4, mk("c8c", [ligne(T + "test_nope")]), ["-k", "test_b"])
cas("8d fantome + --deselect", 4, mk("c8d", [ligne(T + "test_nope")]), [f"--deselect={T}test_ko"])
# 9 passe sans le fichier listé
cas("9a passe ne collectant pas le fichier liste", 0, mk("c9a", [ligne(T + "test_ko")]), ["tests/test_b.py"])
cas("9b fantome, passe ne collectant pas le fichier", "0", mk("c9b", [ligne(T + "test_nope")]), ["tests/test_b.py"])
cas("9c passe par identifiant d'un autre essai du fichier listé (ligne vraie)", 0, mk("c9c", [ligne(T + "test_ko")]), ["tests/test_a.py::test_ok"])
cas("9d idem, ligne fantome", 4, mk("c9d", [ligne(T + "test_nope")]), ["tests/test_a.py::test_ok"])
cas("9e --collect-only, ligne fantome", 4, mk("c9e", [ligne(T + "test_nope")]), ["--collect-only"])
# 10 autres
cas("10a essai non liste qui echoue reste un echec (test_ko2)", 1, mk("c10a", [ligne(T + "test_ko")]), ["tests/test_a.py::test_ko", "tests/test_a.py::test_ko2"])
cas("10b prefixe: liste test_p seul (parametre absent de l'id)", 4, mk("c10b", [ligne(T + "test_p")]))
cas("10c parametre exact test_p[1]", "1", mk("c10c", [ligne(T + "test_p[1]")]), ["tests/test_a.py::test_p"])
cas("10d methode de classe", 0, mk("c10d", [ligne(T + "TestC::test_m")]), ["tests/test_a.py::TestC"])
cas("10e xfail propre non strict sur essai liste qui passe", "1", mk("c10e", [ligne("tests/test_xfail_propre.py::test_s")]), ["tests/test_xfail_propre.py"])
cas("10f rootdir = tests/", "4?", mk("c10f", [ligne(T + "test_ko")]), ["--rootdir=" + str(SB / "c10f" / "tests"), "test_a.py::test_ko"])
# 10f est rejoué avec --rootdir réel ci-dessous
cas("10g ligne avec motif *", 4, mk("c10g", [ligne(T + "test_*")]))
cas("10h ligne hors tests/", 4, mk("c10h", [ligne("scripts/x.py::test_a")]))

with (D / "tables/cas.tsv").open("w") as fh:
    fh.write("cas\tattendu\trendu\tverdict\tresume\n")
    for r in rows:
        fh.write("\t".join(str(x) for x in r) + "\n")
