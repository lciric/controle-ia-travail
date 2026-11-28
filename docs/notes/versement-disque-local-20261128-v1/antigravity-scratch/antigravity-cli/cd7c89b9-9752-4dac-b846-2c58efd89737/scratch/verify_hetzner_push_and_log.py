import hashlib
import os
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

def git_run(*args, binary=False):
    return subprocess.run(
        ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", *args],
        env=env, capture_output=True, text=not binary, timeout=120,
    )

b = "calcul/sondes-v2-epreuve-plantee-v4"
pf = git_run("fetch", "origin", f"refs/heads/{b}:refs/remotes/origin/{b}")
print("FETCH_RC:", pf.returncode)
assert pf.returncode == 0, pf.stderr

plog = git_run("log", "-n", "5", "--format=%H %cI %s", f"origin/{b}")
print("COMMIT_LOG:")
print(plog.stdout.strip())

# Check diff files against parent / main (ONLY names, sizes, SHA-256 — NEVER open contents!)
pls = git_run("ls-tree", "-r", "-l", f"origin/{b}")
lines = pls.stdout.splitlines()
print(f"TOTAL_FILES_IN_TREE: {len(lines)}")
# Show ONLY files added relative to origin/sondes-v2/code-v2 (or diff-tree of HEAD commit)
pdiff = git_run("diff-tree", "--no-commit-id", "--name-status", "-r", f"origin/{b}")
print("HEAD_COMMIT_FILES:")
for ln in pdiff.stdout.splitlines()[:60]:
    print(" ", ln)
print("HEAD_COMMIT_FILE_COUNT:", len(pdiff.stdout.splitlines()))
