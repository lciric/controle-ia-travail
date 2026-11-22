"""Compare, essai par essai, les issues de deux sorties `pytest -rA` (lignes « PASSED|FAILED|… identifiant »)."""
import re
import sys
from pathlib import Path

ISSUE = re.compile(r"^(PASSED|FAILED|ERROR|SKIPPED|XFAIL|XPASS) (tests/.+?)(?: - .*)?$")


def issues(p):
    d = {}
    for l in Path(p).read_text(encoding="utf-8").splitlines():
        m = ISSUE.match(l)
        if m:
            d[m.group(2)] = m.group(1)
    return d


a, b = issues(sys.argv[1]), issues(sys.argv[2])
diff = sorted(k for k in a.keys() | b.keys() if a.get(k) != b.get(k))
compte = {}
for v in a.values():
    compte[v] = compte.get(v, 0) + 1
print(f"essais : {len(a)} contre {len(b)} ; issues de la première sortie : {compte}")
print(f"différences : {len(diff)}")
for k in diff:
    print(f"  {k} : {a.get(k)} -> {b.get(k)}")
for k, v in sorted(a.items()):
    if v != "PASSED":
        print(f"  (non passé, identique) {k} : {v}" if b.get(k) == v else "")
sys.exit(1 if diff else 0)
