import subprocess, json, hashlib

GIT_DIR = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\.git"

def git_bytes(*args):
    r = subprocess.run(["git", f"--git-dir={GIT_DIR}", *args], capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode("utf-8", errors="replace")

def git(*args):
    rc, out, err = git_bytes(*args)
    return rc, out.decode("utf-8", errors="replace"), err

print("=== 1. ALL REFS MATCHING iib/voie/passe/barreau8/etalonnage/sondes ===")
rc, out, _ = git("show-ref")
for line in out.splitlines():
    if any(k in line.lower() for k in ("iib", "voie", "passe", "barreau8", "etalonnage", "sondes", "explo", "oracle")):
        print(" ", line)

print("\n=== 2. TRACES OF IIB IN 3326499e ===")
rc, out, _ = git("ls-tree", "-r", "--name-only", "3326499e666c6b2a3670feda6ee5e15ed055170a", "traces")
for f in out.splitlines():
    if "iib" in f.lower() or "20261123" in f or "20261122" in f:
        print(" ", f)
        if not f.endswith(".sha256"):
            rc2, txt, _ = git("show", f"3326499e666c6b2a3670feda6ee5e15ed055170a:{f}")
            print(f"--- {f} ({len(txt)} chars) ---")
            print(txt[:4000])

print("\n=== 3. ETALONNAGE MANIFESTE & RESUME & BRANCHES IN 192a429e ===")
for p in [
    "runs/20261122-202132-iib-reel/manifeste.json",
    "diag/20261122-202132-iib-reel/resume.json",
    "diag/20261122-202132-iib-reel/branches-iib-v5.json",
    "diag/20261122-202132-iib-reel/vitesse-premier-lot-iib-v5.json",
]:
    rc2, b, err = git_bytes("show", f"192a429e67b93e9a89d273ba5a4b5c0c61d139f1:{p}")
    if rc2 == 0:
        d = json.loads(b.decode("utf-8"))
        compact = {k: v for k, v in d.items() if k not in ("graines", "empreintes", "config", "lignes")}
        print(f"\n192a429e:{p} (sha={hashlib.sha256(b).hexdigest()}):")
        print(json.dumps(compact, indent=2, ensure_ascii=False)[:2500])
    else:
        print(f"\n192a429e:{p} ERR: {err.strip()}")

print("\n=== 4. COMMIT 192a429e MESSAGE & CONFIG COURSE ===")
rc, out, _ = git("show", "-s", "--format=%H%n%aI%n%cI%n%B", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1")
print(out)

rc, out, _ = git("diff-tree", "--no-commit-id", "--name-only", "-r", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1")
for f in out.splitlines():
    if "config" in f or "designation" in f or "manifeste" in f or "resume" in f or "ordre" in f:
        print("  changed in 192a429e:", f)

print("\n=== 5. CHECK COMMIT 0ee74d3f AND 2580b334 FILE CONTENTS/DIFFS ===")
for c in ["0ee74d3fb755c1bd33ed5ab956e2831a043cec1a", "2580b334de8275d6c5bcb73e1861bd23f700395c", "97c23cad9862668dfb59b8d619c90f33971e4c0f"]:
    rc, out, _ = git("show", "--stat", "--format=%H %cI %s", c)
    print(out)

print("\n=== 6. CHECK TRACE-GARDES-PASSE ON DISK OR WT ===")
import pathlib
for base in [
    pathlib.Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail"),
]:
    for m in base.rglob("*trace-gardes-passe*"):
        print("  found on disk:", m)
    for m in base.rglob("*designation*iib*"):
        print("  found on disk:", m)
