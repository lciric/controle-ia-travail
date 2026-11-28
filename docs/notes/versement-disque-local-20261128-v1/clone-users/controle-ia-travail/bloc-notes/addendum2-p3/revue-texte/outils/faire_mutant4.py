import shutil, sys
from pathlib import Path
base = Path(sys.argv[1]); src = (base / "copie" / "audit_verdict_p3_v1.py").read_text(encoding="utf-8")
avant = "abs(aire - ref[0]) > TOLERANCE_AIRE or abs(q - ref[1]) > TOLERANCE_AIRE:"
apres = "abs(aire - ref[0]) > TOLERANCE_AIRE:"
assert src.count(avant) == 1
d = base / "mutants" / "M4-garde7-quantile-plancher"
shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
(d / "audit_verdict_p3_v1.py").write_text(src.replace(avant, apres), encoding="utf-8")
shutil.copy(base / "copie" / "test_audit_verdict_p3_v1.py", d)
print("écrit", d)
