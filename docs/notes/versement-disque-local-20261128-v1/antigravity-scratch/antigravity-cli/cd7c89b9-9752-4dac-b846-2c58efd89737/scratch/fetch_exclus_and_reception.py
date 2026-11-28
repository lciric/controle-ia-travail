import hashlib
import os
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

def git_run(*args, binary=False):
    cmd = ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", *args]
    return subprocess.run(cmd, env=env, capture_output=True, text=not binary, timeout=120)

for b in ("barreau8/cote-expose-pieces-lecture-v1", "reception/barreau8-sortie-garde-v1"):
    p = git_run("fetch", "origin", f"refs/heads/{b}:refs/remotes/origin/{b}")
    print(f"FETCH {b}: rc={p.returncode}")

# Check liste-exclus on barreau8/cote-expose-pieces-lecture-v1
ls1 = git_run("ls-tree", "-r", "--name-only", "origin/barreau8/cote-expose-pieces-lecture-v1").stdout.splitlines()
for f in ls1:
    if "exclus" in f or "barreau8-cote-expose" in f:
        blob = git_run("show", f"origin/barreau8/cote-expose-pieces-lecture-v1:{f}", binary=True).stdout
        print(f"EXPOSE_BRANCH: {f} size={len(blob)} sha={hashlib.sha256(blob).hexdigest()}")

# Check reception branch (names + SHA only, NEVER content!)
ls2 = git_run("ls-tree", "-r", "--name-only", "origin/reception/barreau8-sortie-garde-v1").stdout.splitlines()
head2 = git_run("rev-parse", "origin/reception/barreau8-sortie-garde-v1").stdout.strip()
print(f"RECEPTION_HEAD: {head2}")
for f in ls2:
    blob = git_run("show", f"origin/reception/barreau8-sortie-garde-v1:{f}", binary=True).stdout
    print(f"RECEPTION_BRANCH: {f} size={len(blob)} sha={hashlib.sha256(blob).hexdigest()}")
