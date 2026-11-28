import hashlib
import os
import re
import shutil
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT = SCRATCH / "wt-main-push"
SRC_DIR = SCRATCH / "lecture-sondes-v2-etalon"
DL = Path(r"C:\Users\lciri\Downloads")

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

# 1. Copy the 4 files to C:\Users\lciri\Downloads
rep_name = "rapport-resultats-sondes-v2-etalon-v1.md"
json_name = "synthese-partielle-r0-130-etalon-v1.json"

rep_h = sha256_file(SRC_DIR / rep_name)
json_h = sha256_file(SRC_DIR / json_name)

shutil.copy2(SRC_DIR / rep_name, DL / rep_name)
(DL / (rep_name + ".sha256")).write_bytes(f"{rep_h}  {rep_name}\n".encode("ascii"))
shutil.copy2(SRC_DIR / json_name, DL / json_name)
(DL / (json_name + ".sha256")).write_bytes(f"{json_h}  {json_name}\n".encode("ascii"))

assert sha256_file(DL / rep_name) == rep_h
assert sha256_file(DL / json_name) == json_h
print(f"DOWNLOADS_OK: {DL / rep_name} ({rep_h[:12]}...), {DL / json_name} ({json_h[:12]}...)")

# 2. Inspect GO-2026-11-24-02 in registres
for reg in ("go.md", "depenses.md", "arrets.md", "decisions.md"):
    p = WT / "registres" / reg
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="replace")
        matches = [line for line in txt.splitlines() if ("GO-2026-11-24-02" in line or "177425658" in line or "epreuve-plantee" in line or "sondes-v2" in line)]
        print(f"\n=== {reg} ({len(matches)} lines) ===")
        for line in matches[-25:]:
            print(line[:350])

# 3. Find all files related to sondes-v2 / epreuve-plantee on origin/main and origin/sondes-v2/code-v2
for ref in ("origin/main", "origin/sondes-v2/code-v2"):
    r = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", ref], capture_output=True, text=True, encoding="utf-8")
    files = [f for f in r.stdout.splitlines() if any(k in f for k in ("sondes-v2", "sondes_v2", "monde_plante", "epreuve-plantee", "diagnostics-prealables-sondes"))]
    print(f"\n=== FILES IN {ref} ({len(files)}) ===")
    for f in files:
        print(" ", f)

# 4. Also list remote branches matching sondes-v2 or epreuve
r_br = subprocess.run(["git", "-C", str(REPO), "branch", "-r"], capture_output=True, text=True, encoding="utf-8")
brs = [b.strip() for b in r_br.stdout.splitlines() if any(k in b for k in ("sondes", "epreuve", "plante"))]
print(f"\n=== REMOTE BRANCHES ({len(brs)}) ===")
for b in brs:
    print(" ", b)
