import hashlib
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")

reg_dir = REPO / "registres"
print("QUI_A_LU_QUOI_FILES:")
for p in sorted(reg_dir.glob("qui-a-lu-quoi*")):
    if p.is_file() and not p.name.endswith(".sha256"):
        print(f"  {p.name} sha={hashlib.sha256(p.read_bytes()).hexdigest()}")
    elif p.is_dir():
        print(f"  DIR {p.name}:")
        for sub in sorted(p.iterdir()):
            if sub.is_file() and not sub.name.endswith(".sha256"):
                print(f"    {sub.name} sha={hashlib.sha256(sub.read_bytes()).hexdigest()}")

for dname in ("docs/notes/barreau8-cote-expose-pieces-lecture-v1", "docs/notes/barreau8-cote-moniteurs-entrees-v1", "registres"):
    d = REPO / dname
    if d.exists():
        for p in sorted(d.glob("*exclus*")):
            if p.is_file() and not p.name.endswith(".sha256"):
                print(f"  EXCLUS {dname}/{p.name} sha={hashlib.sha256(p.read_bytes()).hexdigest()}")
