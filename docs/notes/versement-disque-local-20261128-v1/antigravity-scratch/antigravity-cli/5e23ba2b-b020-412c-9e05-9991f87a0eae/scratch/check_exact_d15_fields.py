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

print("=== A. DESIGNATION FILE ===")
for rev in ["192a429e67b93e9a89d273ba5a4b5c0c61d139f1", "3326499e666c6b2a3670feda6ee5e15ed055170a", "30cf3b578f8b9c748fddfc87c4b6e7dd0a506abf"]:
    d, sha, err = show_json(rev, "diag/20261122-202132-iib-reel/designation-iib-v5.json")
    print(f"rev {rev[:10]}: sha={sha} err={err}")
d, sha, _ = show_json("192a429e67b93e9a89d273ba5a4b5c0c61d139f1", "diag/20261122-202132-iib-reel/designation-iib-v5.json")
print("designation-iib-v5.json content:")
print(json.dumps(d, indent=2, ensure_ascii=False))

print("\n=== B. ALL RUNS IN 192a429e AND 3326499e ===")
rc, out, _ = git("ls-tree", "-r", "--name-only", "3326499e666c6b2a3670feda6ee5e15ed055170a", "runs", "traces")
for f in out.splitlines():
    print(" ", f)

for p in [
    "runs/20261123-043944-iib-course-reel/manifeste.json",
    "diag/20261123-043944-iib-course-reel/resume.json",
]:
    d, sha, err = show_json("3326499e666c6b2a3670feda6ee5e15ed055170a", p)
    print(f"\n--- {p} (sha={sha}) ---")
    if d:
        # print all keys except huge nested arrays
        compact = {k: v for k, v in d.items() if k not in ("graines", "empreintes")}
        if "config" in compact and isinstance(compact["config"], dict):
            compact["config"] = {k: v for k, v in compact["config"].items() if k in ("go_id", "pieces", "oracle_de_la_regle", "code", "entropie", "offre")}
        print(json.dumps(compact, indent=2, ensure_ascii=False)[:3500])

print("\n=== C. MANIFESTE-COURSE-IIB-V5 (relevant keys) ===")
d, sha, _ = show_json("3326499e666c6b2a3670feda6ee5e15ed055170a", "diag/20261122-202132-iib-reel/manifeste-course-iib-v5.json")
if d:
    compact = {k: v for k, v in d.items() if k != "config"}
    compact["config_go_id"] = d.get("config", {}).get("go_id")
    compact["config_pieces"] = d.get("config", {}).get("pieces")
    compact["config_oracle_de_la_regle"] = d.get("config", {}).get("oracle_de_la_regle")
    compact["config_code"] = d.get("config", {}).get("code")
    print(json.dumps(compact, indent=2, ensure_ascii=False)[:3500])

print("\n=== D. LECTURE 1 & LECTURE 2 ORACLE CHECK ===")
for label, rev, p in [
    ("L1", "5ac7915310298693c9110dfc4a549fc75c9680ff", "diag/20261123-043944-iib-course-reel/lecture-iib-1-dommage-exploratoire-non-opposable-v1.json"),
    ("L2", "e056192aa90c0c12e1cf787ebb5a650699bbc49d", "diag/20261123-043944-iib-course-reel/lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json"),
]:
    d, sha, _ = show_json(rev, p)
    print(label, "top keys:", list(d.keys()))
    for k in ("run_id", "course", "oracle", "oracle_de_la_regle", "designation", "designation_sha256", "entrees"):
        if k in d:
            print(f"  {k}: {d[k]}")

d2m, _, _ = show_json("e056192aa90c0c12e1cf787ebb5a650699bbc49d", "runs/20261125-085524-iib-lecture-2-diffusion-v5/manifeste.json")
print("L2 manifeste entrees:", json.dumps(d2m.get("config", {}).get("entrees"), indent=2))
print("L2 manifeste course:", d2m.get("config", {}).get("course"))

print("\n=== E. TRACE-GARDES-PASSE (donnees/passe-activations-voie-a-v1 / 26a7043c) ===")
rc, out, err = git("show", "26a7043c:versement/20261124-122719-rejeu-activations-voie-a/sortie-passe/livraison/trace-gardes-passe-barreau8-v1.json")
if rc != 0:
    rc2, lsout, _ = git("ls-tree", "-r", "--name-only", "26a7043c")
    print("26a7043c ls-tree:", lsout[:1500])
else:
    td = json.loads(out)
    print("trace course:", td.get("course"))

print("\n=== F. CHECK ALL COMMITS/REFS FOR ETALONNAGE & RULE SEALING ===")
for ref in ["8cac7bbd", "b671d6e8", "07b2476a716fe7faf6ef898eeea2d7772259a6f2", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1"]:
    rc, out, err = git("show", "-s", "--format=%H %cI %s", ref)
    print(f"ref {ref}: rc={rc} out={out.strip()} err={err.strip()}")
