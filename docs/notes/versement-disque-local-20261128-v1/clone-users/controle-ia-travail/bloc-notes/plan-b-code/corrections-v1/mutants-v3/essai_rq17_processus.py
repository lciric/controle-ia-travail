"""Essai : sous RQ-17 (graine du témoin non posée), l'issue de `test_temoin_configuration_remplacee_cas_sain_et_artefact`
(égalité de deux appels « à graine égale ») varie-t-elle d'un processus à l'autre ? Le test est lancé seul, en premier
dans un processus neuf, six fois : PYTHONHASHSEED 0, 0, 1, 1, puis non fixé deux fois. Copie `wX`, effacée après usage
par l'appelant."""
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import muter_vcb2 as M  # noqa: E402

(_, module, ancien, nouveau, _, _), = [m for m in M.MUTANTS if m[0] == "RQ-17"]
w = M.ICI / "wX"
M.preparer(w)
cible = w / module
t = (M.CLONE / module).read_text(encoding="utf-8")
assert t.count(ancien) == 1
cible.write_text(t.replace(ancien, nouveau, 1), encoding="utf-8")
test = "tests/test_plan_b_requalifier.py::test_temoin_configuration_remplacee_cas_sain_et_artefact"
try:
    for graine in ("0", "0", "1", "1", None, None):
        env = {**os.environ, "PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(M.ICI / "tmp")}
        env.pop("PYTHONHASHSEED", None)
        if graine is not None:
            env["PYTHONHASHSEED"] = graine
        p = subprocess.run(["nice", "-n", "19", M.PY, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                            f"--basetemp={w / 'bt'}", test], cwd=w, env=env, capture_output=True, text=True)
        lignes = p.stdout.splitlines()
        diff = [x for x in lignes if "Differing items" in x or x.startswith("E         {'rangees'")]
        print(f"PYTHONHASHSEED={graine} : {[x for x in lignes if x.strip()][-1]}")
        for x in diff:
            print("   ", x[:400])
finally:
    shutil.copy(M.CLONE / module, cible)
    assert cible.read_bytes() == (M.CLONE / module).read_bytes()
