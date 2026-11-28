"""Essai : sous RQ-17, ordre réel d'exécution de pytest pour la sélection « après les autres tests du témoin » de
`rejouer_rq17_vcb2.py`, et répétabilité de son issue (trois processus neufs), comparée au test lancé seul (trois
processus neufs). Copie `wY`, effacée après usage par l'appelant."""
import shutil
import subprocess
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import muter_vcb2 as M  # noqa: E402

(_, module, ancien, nouveau, _, _), = [m for m in M.MUTANTS if m[0] == "RQ-17"]
w = M.ICI / "wY"
M.preparer(w)
cible = w / module
t = (M.CLONE / module).read_text(encoding="utf-8")
assert t.count(ancien) == 1
cible.write_text(t.replace(ancien, nouveau, 1), encoding="utf-8")
T = "tests/test_plan_b_requalifier.py::"
conf, imp, graine = (T + x for x in ("test_temoin_configuration_remplacee_cas_sain_et_artefact",
                                     "test_temoin_impossible_et_pannes_propagees",
                                     "test_temoin_graine_posee_avant_chaque_appel"))
env = {**os.environ, "PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(M.ICI / "tmp")}
try:
    for nom, tests in (("trois tests (conf, impossible, graine)", [conf, imp, graine]),) * 3 + (("conf seul", [conf]),) * 3:
        p = subprocess.run(["nice", "-n", "19", M.PY, "-B", "-m", "pytest", "-v", "-p", "no:cacheprovider",
                            f"--basetemp={w / 'bt'}", *tests], cwd=w, env=env, capture_output=True, text=True)
        ordre = [x.split("::")[1].split(" ")[0] + " " + x.split(" ")[-2] if " " in x else x
                 for x in p.stdout.splitlines() if x.startswith("tests/") and ("PASSED" in x or "FAILED" in x)]
        print(f"{nom} : {[x for x in p.stdout.splitlines() if x.strip()][-1]}")
        for x in ordre:
            print("   ", x)
finally:
    shutil.copy(M.CLONE / module, cible)
    assert cible.read_bytes() == (M.CLONE / module).read_bytes()
