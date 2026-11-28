import pathlib
import re
import sys

print("Python:", sys.version)
root = pathlib.Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
pat = re.compile(r"CONTAINER_ID|VAST_CONTAINERLABEL|console\.vast\.ai|VAST_INSTANCE|58936096")
for p in sorted(root.rglob("*")):
    if ".git" in p.parts or not p.is_file() or p.suffix not in (".py", ".sh", ".md", ".json"):
        continue
    try:
        txt = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for i, line in enumerate(txt.splitlines(), 1):
        if pat.search(line):
            print(f"{p.relative_to(root)}:{i}: {line.strip()[:140]}")
