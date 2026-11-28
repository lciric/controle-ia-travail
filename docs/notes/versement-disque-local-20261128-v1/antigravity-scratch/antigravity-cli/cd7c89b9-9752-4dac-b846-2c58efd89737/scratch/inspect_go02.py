import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT = SCRATCH / "wt-main-push"

for reg in ("go.md", "depenses.md", "arrets.md", "decisions.md"):
    p = WT / "registres" / reg
    if p.exists():
        txt = p.read_text(encoding="utf-8", errors="replace")
        matches = [line for line in txt.splitlines() if any(k in line for k in ("GO-2026-11-24-02", "177425658", "epreuve-plantee", "sondes-v2"))]
        print(f"\n=== {reg} ({len(matches)} lines) ===")
        for line in matches[-30:]:
            print(line[:380])

for ref in ("origin/main", "origin/sondes-v2/code-v2"):
    r = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", ref], capture_output=True, text=True, encoding="utf-8")
    files = [f for f in r.stdout.splitlines() if any(k in f for k in ("sondes-v2", "sondes_v2", "monde_plante", "epreuve-plantee", "diagnostics-prealables-sondes"))]
    print(f"\n=== FILES IN {ref} ({len(files)}) ===")
    for f in files:
        print(" ", f)

r_br = subprocess.run(["git", "-C", str(REPO), "branch", "-r"], capture_output=True, text=True, encoding="utf-8")
brs = [b.strip() for b in r_br.stdout.splitlines() if any(k in b for k in ("sondes", "epreuve", "plante"))]
print(f"\n=== REMOTE BRANCHES ({len(brs)}) ===")
for b in brs:
    print(" ", b)
