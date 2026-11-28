import subprocess, json, hashlib, re

GIT_DIR = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\.git"

def git_bytes(*args):
    r = subprocess.run(["git", f"--git-dir={GIT_DIR}", *args], capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode("utf-8", errors="replace")

def git(*args):
    rc, out, err = git_bytes(*args)
    return rc, out.decode("utf-8", errors="replace"), err

def show_json(rev, path):
    rc, b, err = git_bytes("show", f"{rev}:{path}")
    if rc != 0:
        return None, None, err.strip()
    return json.loads(b.decode("utf-8")), hashlib.sha256(b).hexdigest(), ""

print("=== 1. LECTURES V5 EXECUTEES (30cf3b57) ===")
for c in ["5ac7915310298693c9110dfc4a549fc75c9680ff", "e056192aa90c0c12e1cf787ebb5a650699bbc49d", "30cf3b578f8b9c748fddfc87c4b6e7dd0a506abf"]:
    rc, out, _ = git("diff-tree", "--no-commit-id", "--name-only", "-r", c)
    print(f"Commit {c[:10]} files:")
    for f in out.splitlines():
        print("  ", f)

for rev, p in [
    ("5ac7915310298693c9110dfc4a549fc75c9680ff", "runs/20261125-052722-iib-lecture-1-dommage-v5/manifeste.json"),
]:
    d, sha, err = show_json(rev, p)
    print(f"\nManifeste L1 ({p}, sha={sha}):")
    print(json.dumps(d, indent=2, ensure_ascii=False)[:3000])

# Find L2 manifeste path
rc, out, _ = git("diff-tree", "--no-commit-id", "--name-only", "-r", "e056192aa90c0c12e1cf787ebb5a650699bbc49d")
l2_man = [f for f in out.splitlines() if f.endswith("manifeste.json")][0]
d, sha, err = show_json("e056192aa90c0c12e1cf787ebb5a650699bbc49d", l2_man)
print(f"\nManifeste L2 ({l2_man}, sha={sha}):")
print(json.dumps(d, indent=2, ensure_ascii=False)[:3000])

# Check top-level non-score metadata keys in L1 and L2 JSONs
for rev, p in [
    ("5ac7915310298693c9110dfc4a549fc75c9680ff", "diag/20261123-043944-iib-course-reel/lecture-iib-1-dommage-exploratoire-non-opposable-v1.json"),
    ("e056192aa90c0c12e1cf787ebb5a650699bbc49d", "diag/20261123-043944-iib-course-reel/lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json"),
]:
    d, sha, err = show_json(rev, p)
    if d:
        meta = {k: v for k, v in d.items() if k in ("run_id", "oracle", "oracle_de_la_regle", "designation", "source", "entrees", "course", "commit_lancement", "empreintes")}
        print(f"\nMeta of {p} (top keys={list(d.keys())}):")
        print(json.dumps(meta, indent=2, ensure_ascii=False)[:2000])

print("\n=== 2. COURSE LAUNCH COMMIT 192a429e & COURSE HEAD 3326499e ===")
rc, out, _ = git("ls-tree", "-r", "--name-only", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1", "diag", "runs", "docs/notes/barreau8-iib-v1")
print("Files in 192a429e (diag, runs, docs/notes/barreau8-iib-v1):")
for f in out.splitlines():
    if "lot-" not in f and "tour-" not in f:
        print("  ", f)

rc, out, _ = git("ls-tree", "-r", "--name-only", "3326499e666c6b2a3670feda6ee5e15ed055170a", "diag", "runs", "traces")
print("\nFiles in 3326499e (diag, runs, traces, filtered):")
for f in out.splitlines():
    if "lot-" not in f and "tour-" not in f:
        print("  ", f)

for p in [
    "runs/20261123-043944-iib-course-reel/manifeste.json",
    "diag/20261123-043944-iib-course-reel/resume.json",
    "diag/20261122-202132-iib-reel/manifeste-course-iib-v5.json",
    "diag/20261122-202132-iib-reel/course-engagee-iib-v5.json",
]:
    d, sha, err = show_json("3326499e666c6b2a3670feda6ee5e15ed055170a", p)
    print(f"\n3326499e:{p} (sha={sha}, err={err}):")
    if d:
        print(json.dumps(d, indent=2, ensure_ascii=False)[:2500])
