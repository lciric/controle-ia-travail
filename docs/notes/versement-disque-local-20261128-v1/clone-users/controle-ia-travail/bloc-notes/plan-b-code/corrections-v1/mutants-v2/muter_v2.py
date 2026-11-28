"""Pilote des mutants rejoués après les corrections VCB (repris de celui de la vérification des corrections ; trois
différences : la base est le clone, jamais écrit ; `pyproject.toml` est copié, pas lié ; témoin intégré).
Usage : python muter_v2.py <id du travailleur> <n travailleurs> [ids…]   |   python muter_v2.py temoin
Chaque travailleur a son dossier `wN` : copies de `src/`, `tests/` et `pyproject.toml` ; liens vers les autres entrées
du clone (sans `.git`). Pour chaque mutant : module restauré depuis le clone, une seule substitution, tests ciblés
(-x), module restauré. Sortie : une ligne JSON par mutant dans `resultats-wN.jsonl`. Les dossiers `wN` sont
effacés après usage (`rm -r` : les liens seuls, jamais leurs cibles dans le clone)."""
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
CLONE = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/plan-b-code/depot")
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
TESTS_PLAN_B = ["tests/test_plan_b_rubrique_simplifiee.py", "tests/test_plan_b_juges_simplifies.py",
                "tests/test_plan_b_requalifier.py", "tests/test_plan_b_lecteur.py", "tests/test_plan_b_integration.py"]
sys.path.insert(0, str(ICI))
from liste_mutants_v2 import MUTANTS  # noqa: E402


def preparer(w: Path) -> None:
    if w.exists():
        return
    w.mkdir()
    for x in CLONE.iterdir():
        if x.name == ".git":
            continue
        if x.name in ("src", "tests", "pyproject.toml"):
            (shutil.copytree if x.is_dir() else shutil.copy2)(x, w / x.name)
        else:
            (w / x.name).symlink_to(x)


def pytest(w: Path, tests: list[str], x: bool = True) -> subprocess.CompletedProcess:
    (ICI / "tmp").mkdir(exist_ok=True)
    return subprocess.run(["nice", "-n", "19", PY, "-B", "-m", "pytest", "-q", *(["-x"] if x else []),
                           "-p", "no:cacheprovider", f"--basetemp={w / 'bt'}", *tests], cwd=w,
                          env={**os.environ, "PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1",
                               "TMPDIR": str(ICI / "tmp")}, capture_output=True, text=True, timeout=3000)


def temoin() -> None:
    w = ICI / "wT"
    preparer(w)
    t0 = time.time()
    p = pytest(w, TESTS_PLAN_B, x=False)
    fin = [x for x in p.stdout.splitlines() if x.strip()][-1:] or [""]
    r = {"temoin": "copie non mutée", "code": p.returncode, "fin": fin[0], "duree_s": round(time.time() - t0, 1)}
    (ICI / "journal-temoin.txt").write_text(p.stdout[-3000:] + "\n" + json.dumps(r, ensure_ascii=False) + "\n",
                                            encoding="utf-8")
    print(json.dumps(r, ensure_ascii=False), flush=True)


def main():
    if sys.argv[1] == "temoin":
        return temoin()
    k, n = int(sys.argv[1]), int(sys.argv[2])
    choisis = set(sys.argv[3:])
    w = ICI / f"w{k}"
    preparer(w)
    sortie = ICI / f"resultats-w{k}.jsonl"
    for i, (ident, module, ancien, nouveau, tests, quoi) in enumerate(MUTANTS):
        if (choisis and ident not in choisis) or (not choisis and i % n != k):
            continue
        cible = w / module
        shutil.copy(CLONE / module, cible)
        texte = cible.read_text(encoding="utf-8")
        occ = texte.count(ancien)
        if occ != 1:
            r = {"id": ident, "statut": f"ancien texte trouvé {occ} fois", "quoi": quoi}
        else:
            cible.write_text(texte.replace(ancien, nouveau, 1), encoding="utf-8")
            t0 = time.time()
            p = pytest(w, tests)
            fin = [x for x in p.stdout.splitlines() if x.strip()][-1:] or [""]
            echec = [x for x in p.stdout.splitlines() if x.startswith("FAILED") or x.startswith("ERROR")][:2]
            r = {"id": ident, "statut": "survit" if p.returncode == 0 else "tué", "code": p.returncode,
                 "fin": fin[0], "premier_echec": echec, "duree_s": round(time.time() - t0, 1), "quoi": quoi}
        shutil.copy(CLONE / module, cible)
        assert cible.read_bytes() == (CLONE / module).read_bytes()
        with sortie.open("a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(json.dumps(r, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
