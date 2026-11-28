import subprocess, json, hashlib, pathlib, os, re

GIT = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\.git"
REPO = pathlib.Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
ENV = {"GIT_TERMINAL_PROMPT": "0", "PATH": os.environ.get("PATH", "")}

def git_bytes(*args):
    r = subprocess.run(["git", f"--git-dir={GIT}", *args], capture_output=True, env=ENV)
    return r.returncode, r.stdout, r.stderr.decode("utf-8", errors="replace")

def git(*args):
    rc, b, err = git_bytes(*args)
    return rc, b.decode("utf-8", errors="replace"), err

print("=== 1. VERIFY SHAS OF RULE AND ORDER ===")
rc, b, err = git_bytes("show", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1:brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1.md")
print("conception in 192a429e:", rc, hashlib.sha256(b).hexdigest() if rc == 0 else err)
p_ord = REPO / "brouillons/ii-b-saboteur-budget-v5/additif-course-v1/additif-ordre-course-voie-A-v1.md"
print("ordre on disk:", hashlib.sha256(p_ord.read_bytes()).hexdigest())

print("\n=== 2. SEARCH origin/barreau8/cote-expose-pieces-lecture-v1 FOR TIMESTAMPS / DESIGNATION / D-15 ===")
rc, files, _ = git("ls-tree", "-r", "--name-only", "origin/barreau8/cote-expose-pieces-lecture-v1", "docs/notes/barreau8-cote-expose-pieces-lecture-v1")
rx = re.compile(r"8cac7bbd|78045af7|22:12|D-15|attestation-course|13:27:38|20:29:04|04:41:|11:24:|designation-iib", re.I)
for f in files.splitlines():
    if f.endswith((".md", ".json", ".py")):
        rc2, txt, _ = git("show", f"origin/barreau8/cote-expose-pieces-lecture-v1:{f}")
        for i, l in enumerate(txt.splitlines(), 1):
            if rx.search(l):
                print(f"  {f}:L{i}: {l[:220]}")

print("\n=== 3. SEARCH SMALL TARGETED DIRS ON MAIN ===")
for sub in [
    "docs/notes/additif-sondes-barreau8-scellement-v1",
    "docs/notes/rejeu-activations-saboteur-voie-a-v1",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1",
    "docs/notes/barreau8-cote-moniteurs-sorties-v1",
]:
    d = REPO / sub
    if not d.exists():
        continue
    for p in d.rglob("*"):
        if p.is_file() and p.suffix in (".md", ".json", ".txt"):
            txt = p.read_text(encoding="utf-8", errors="ignore")
            for i, l in enumerate(txt.splitlines(), 1):
                if rx.search(l):
                    print(f"  {p.relative_to(REPO)}:L{i}: {l[:220]}")

print("\n=== 4. CHECK TIMESTAMPS INSIDE 192a429e ETALONNAGE & 3326499e COURSE FILES ===")
rc, log_192, _ = git("log", "-n", "5", "--format=%H %cI %s", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1")
print("log 192a429e:\n", log_192)
for p in ["diag/20261122-202132-iib-reel/etalonnage-oracles-iib-v5.json", "diag/20261122-202132-iib-reel/graines-etalonnage-iib-v5.json"]:
    rc, b, _ = git_bytes("show", f"192a429e67b93e9a89d273ba5a4b5c0c61d139f1:{p}")
    if rc == 0:
        d = json.loads(b.decode("utf-8"))
        print(f"{p} top keys:", list(d.keys())[:20])
        for k in list(d.keys()):
            if any(t in k.lower() for t in ("date", "heure", "instant", "cree", "debut", "fin", "utc")):
                print(f"  {k}: {d[k]}")

print("\n=== 5. CHECK IF etalonnage-iib-v5 OR lots HAVE TIMESTAMPS IN 192a429e ===")
rc, b, _ = git_bytes("show", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1:donnees/20261122-202132-iib-reel/lots/lot-001-etalonnage-honnete.json")
if rc == 0:
    d = json.loads(b.decode("utf-8"))
    print("lot-001 keys:", list(d.keys()))
rc, b, _ = git_bytes("show", "3326499e666c6b2a3670feda6ee5e15ed055170a:diag/20261122-202132-iib-reel/evaluation/ids-evaluation-H.json")
if rc == 0:
    d = json.loads(b.decode("utf-8"))
    print("ids-evaluation-H keys:", list(d.keys()))
rc, b, _ = git_bytes("show", "3326499e666c6b2a3670feda6ee5e15ed055170a:diag/20261122-202132-iib-reel/evaluation-iib-v5.json")
if rc == 0:
    d = json.loads(b.decode("utf-8"))
    print("evaluation-iib-v5 keys:", list(d.keys()))
