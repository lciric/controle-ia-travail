import hashlib
import os
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
STAGE = SCRATCH / "b8-staging"
D8_DST = STAGE / "donnees" / "20261114-001352-t07-lecture-reel"
MAND_DST = STAGE / "conductrice"

env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

def git_run(*args, timeout=300, binary=False):
    cmd = ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", *args]
    return subprocess.run(cmd, env=env, capture_output=True, text=not binary, timeout=timeout)

# 1. Fetch the 3 branches (no checkout, pure objects)
branches = [
    "donnees/t07-etape-a-v1",
    "donnees/passe-activations-voie-a-v1",
    "barreau8/conductrice-lecture-sondes-v1",
]
for b in branches:
    p = git_run("fetch", "origin", f"refs/heads/{b}:refs/remotes/origin/{b}", timeout=300)
    print(f"FETCH {b}: rc={p.returncode} {(p.stderr or '').strip()[:150]}")
    assert p.returncode == 0, f"Fetch failed for {b}: {p.stderr}"

# 2. Inspect tree of conductrice branch & extract non-cloisonne planning/mandate/prep docs into scratch/b8-staging/conductrice
MAND_DST.mkdir(parents=True, exist_ok=True)
p_ls_c = git_run("ls-tree", "-r", "--name-only", "origin/barreau8/conductrice-lecture-sondes-v1")
cond_files = [f for f in p_ls_c.stdout.splitlines() if f.strip()]
print(f"CONDUCTRICE_FILES ({len(cond_files)}):")
for f in cond_files:
    if any(k in f for k in ("conductrice", "mandat", "preparer", "exclus", "qui-a-lu")):
        print("  ", f)
        blob = git_run("show", f"origin/barreau8/conductrice-lecture-sondes-v1:{f}", binary=True).stdout
        out_p = MAND_DST / Path(f).name
        out_p.write_bytes(blob)

# 3. Inspect filenames (ONLY names, NEVER content!) on passe-activations-voie-a-v1
p_ls_p = git_run("ls-tree", "-r", "--name-only", "origin/donnees/passe-activations-voie-a-v1")
passe_files = [f for f in p_ls_p.stdout.splitlines() if f.strip()]
print(f"PASSE_FILES ({len(passe_files)}):")
for f in passe_files:
    if "versement/" in f or "livraison/" in f or "bordereau" in f:
        print("  ", f)

# 4. Stage D-8 probe files from origin/donnees/t07-etape-a-v1 (binary only, verify exact SHA-256!)
D8_DST.mkdir(parents=True, exist_ok=True)
p_ls_t = git_run("ls-tree", "-r", "--name-only", "origin/donnees/t07-etape-a-v1")
t07_files = [f for f in p_ls_t.stdout.splitlines() if "20261114-001352-t07-lecture-reel" in f]
print(f"T07_D8_FILES ({len(t07_files)}):")
for f in t07_files:
    print("  ", f)

# Extract planchers-figees-t07.npz (+ .sha256)
pl_rel = "donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz"
pl_bytes = git_run("show", f"origin/donnees/t07-etape-a-v1:{pl_rel}", binary=True).stdout
(D8_DST / "planchers-figees-t07.npz").write_bytes(pl_bytes)
pl_sha = hashlib.sha256(pl_bytes).hexdigest()
(D8_DST / "planchers-figees-t07.npz.sha256").write_text(f"{pl_sha}  planchers-figees-t07.npz\n", encoding="utf-8", newline="\n")
print(f"STAGED planchers-figees-t07.npz size={len(pl_bytes)} sha={pl_sha}")

# Reassemble sondes-neuves-t07.npz from chunks 000..008
chunks = sorted(f for f in t07_files if "sondes-neuves-t07.npz.morceau-" in f and not f.endswith(".sha256"))
print("SONDES_NEUVES_CHUNKS:", len(chunks))
h_sn = hashlib.sha256()
total_sz = 0
sn_path = D8_DST / "sondes-neuves-t07.npz"
with sn_path.open("wb") as out_f:
    for c in chunks:
        b = git_run("show", f"origin/donnees/t07-etape-a-v1:{c}", binary=True).stdout
        out_f.write(b)
        h_sn.update(b)
        total_sz += len(b)
sn_sha = h_sn.hexdigest()
(D8_DST / "sondes-neuves-t07.npz.sha256").write_text(f"{sn_sha}  sondes-neuves-t07.npz\n", encoding="utf-8", newline="\n")
print(f"STAGED sondes-neuves-t07.npz size={total_sz} sha={sn_sha}")
assert sn_sha == "374ad47346ae40d5a4d350724d0d19b5961724066dd7fdfaaf0adf1c3a4cbb79", f"SHA mismatch: {sn_sha}"

# Also locate sondes-figees-legeres.npz in repo
for p in REPO.rglob("sondes-figees-legeres.npz"):
    print("FOUND_LEGERES:", p, hashlib.sha256(p.read_bytes()).hexdigest())
