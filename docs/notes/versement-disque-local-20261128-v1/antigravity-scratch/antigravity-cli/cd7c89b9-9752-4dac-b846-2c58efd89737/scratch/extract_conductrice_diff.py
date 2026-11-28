import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
OUT = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\b8-staging\conductrice-diff")
OUT.mkdir(parents=True, exist_ok=True)

mb = subprocess.check_output(
    ["git", "-C", str(REPO), "merge-base", "main", "origin/barreau8/conductrice-lecture-sondes-v1"],
    text=True,
).strip()
files = subprocess.check_output(
    ["git", "-C", str(REPO), "diff", "--name-only", mb, "origin/barreau8/conductrice-lecture-sondes-v1"],
    text=True,
).splitlines()
print(f"DIFF_FILES ({len(files)}):")
for f in files:
    print(" ", f)
    p = OUT / Path(f).name
    blob = subprocess.check_output(["git", "-C", str(REPO), "show", f"origin/barreau8/conductrice-lecture-sondes-v1:{f}"])
    p.write_bytes(blob)
