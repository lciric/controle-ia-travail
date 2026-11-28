import subprocess, json, pathlib, re

GIT_DIR = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\.git"

def git(*args):
    r = subprocess.run(["git", f"--git-dir={GIT_DIR}", *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, r.stdout, r.stderr

print("=== RELEVANT BRANCHES ===")
rc, out, _ = git("branch", "-a")
for line in out.splitlines():
    if re.search(r"iib|barreau8|passe|voie-a|etalonnage|sondes|oracle|saboteur", line, re.I):
        print(" ", line.strip())

print("\n=== COMMIT 30cf3b578f8b9c748fddfc87c4b6e7dd0a506abf (barreau8/lectures-v5-executees-v1) ===")
rc, out, _ = git("log", "-n", "10", "--stat", "30cf3b578f8b9c748fddfc87c4b6e7dd0a506abf")
print(out[:6000])

print("\n=== REMOTE barreau8/cote-expose-pieces-lecture-v1 ===")
rc, out, _ = git("log", "-n", "10", "--stat", "origin/barreau8/cote-expose-pieces-lecture-v1")
print(out[:4000])

print("\n=== COMMIT 192a429e67b93e9a89d273ba5a4b5c0c61d139f1 (launch commit) ===")
rc, out, _ = git("show", "--stat", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1")
print(out[:4000])

print("\n=== COMMIT 3326499e666c6b2a3670feda6ee5e15ed055170a (essai/iib-explo-v8) LOG ===")
rc, out, _ = git("log", "--format=%H %cI %s", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1..3326499e666c6b2a3670feda6ee5e15ed055170a")
print(out[:6000])
