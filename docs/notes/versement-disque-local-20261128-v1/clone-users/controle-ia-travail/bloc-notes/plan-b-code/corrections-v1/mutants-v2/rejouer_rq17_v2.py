"""RQ-17 (graine du témoin non posée) rejoué contre le test neuf `test_temoin_graine_posee_avant_chaque_appel` :
seul, puis après les deux autres tests du témoin (autre état du générateur global). Il doit échouer les deux fois,
sur l'assertion de l'espion (raison écrite), quel que soit l'état laissé par les tests précédents. Copie `wR`,
effacée après usage (`rm -r`)."""
import shutil
import subprocess
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import muter_v2 as M  # noqa: E402
(_, module, ancien, nouveau, _, _), = [m for m in M.MUTANTS if m[0] == "RQ-17"]
w = M.ICI / "wR"
M.preparer(w)
cible = w / module
t = (M.CLONE / module).read_text(encoding="utf-8")
assert t.count(ancien) == 1
cible.write_text(t.replace(ancien, nouveau, 1), encoding="utf-8")
try:
    seul = "tests/test_plan_b_requalifier.py::test_temoin_graine_posee_avant_chaque_appel"
    for nom, tests in (("seul", [seul]), ("après les tests du témoin", [
            "tests/test_plan_b_requalifier.py::test_temoin_configuration_remplacee_cas_sain_et_artefact",
            "tests/test_plan_b_requalifier.py::test_temoin_impossible_et_pannes_propagees", seul])):
        p = M.pytest(w, tests, x=False)
        lignes = p.stdout.splitlines()
        print(f"--- RQ-17, {nom} : {[x for x in lignes if x.strip()][-1]}")
        print("\n".join(x for x in lignes if x.startswith("E ") or x.startswith("FAILED"))[:1500])
finally:
    shutil.copy(M.CLONE / module, cible)
    assert cible.read_bytes() == (M.CLONE / module).read_bytes()
