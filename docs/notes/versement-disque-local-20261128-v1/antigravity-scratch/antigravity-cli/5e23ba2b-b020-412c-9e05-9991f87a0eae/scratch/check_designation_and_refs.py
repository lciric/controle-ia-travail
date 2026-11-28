import subprocess, json, hashlib, pathlib

GIT_DIR = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\.git"
REPO = pathlib.Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")

def git(*args):
    r = subprocess.run(["git", f"--git-dir={GIT_DIR}", *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, r.stdout, r.stderr

print("=== 1. FULL journal.txt FROM 3326499e ===")
rc, out, _ = git("show", "3326499e666c6b2a3670feda6ee5e15ed055170a:traces/iib-20261123-132033-c3YM/journal.txt")
for line in out.splitlines():
    if any(k in line.lower() for k in ("evaluation", "distillation", "tours", "debut", "fin", "engagee", "tour=1 ", "tour 001", "tour=20", "tour 020", "oracle", "progres")):
        print(" ", line)

print("\n=== 2. ETALONNAGE MANIFESTE & RESUME IN 192a429e ===")
for p in ["runs/20261122-202132-iib-reel/manifeste.json", "diag/20261122-202132-iib-reel/resume.json"]:
    rc, out, _ = git("show", f"192a429e67b93e9a89d273ba5a4b5c0c61d139f1:{p}")
    d = json.loads(out)
    print(f"\n--- {p} ---")
    for k, v in d.items():
        if k not in ("graines", "config", "empreintes"):
            if k == "resultat" and isinstance(v, dict):
                print("  resultat (without empreintes):", json.dumps({rk: rv for rk, rv in v.items() if rk != "empreintes"}, indent=2, ensure_ascii=False))
            else:
                print(f"  {k}: {json.dumps(v, ensure_ascii=False)}")

print("\n=== 3. FILES ON origin/barreau8/cote-expose-pieces-lecture-v1 AND origin/barreau8/conductrice-lecture-sondes-v1 ===")
for ref in ["origin/barreau8/cote-expose-pieces-lecture-v1", "origin/barreau8/conductrice-lecture-sondes-v1"]:
    rc, out, _ = git("log", "-n", "10", "--stat", ref)
    print(f"\n--- {ref} ---")
    print(out[:2500])

print("\n=== 4. GREP docs/ AND registres/ FOR 78045af7, 8cac7bbd, 13:27:38, 8d839f33, 2026-11-22T22:1, c1dc5459 ===")
for pat in ["78045af7", "8cac7bbd", "8c66bac4", "13:27:38", "8d839f33", "2026-11-22T22:1", "c1dc5459", "attestation-course-et-oracle"]:
    print(f"\n-- grep {pat} --")
    for base in [REPO / "docs", REPO / "registres", REPO / "prereg", REPO / "brouillons"]:
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix in (".md", ".json", ".txt", ".py"):
                try:
                    txt = p.read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    continue
                if pat in txt:
                    for i, line in enumerate(txt.splitlines(), 1):
                        if pat in line:
                            print(f"  {p.relative_to(REPO)}:L{i}: {line[:220]}")
                            break

print("\n=== 5. CHECK IF etats-evaluation-iib-v5.json HAS TIMESTAMPS ===")
rc, out, _ = git("show", "3326499e666c6b2a3670feda6ee5e15ed055170a:diag/20261122-202132-iib-reel/etats-evaluation-iib-v5.json")
if rc == 0:
    print(out[:1500])

print("\n=== 6. CHECK designation_v5.py IN 192a429e ===")
rc, out, _ = git("ls-tree", "-r", "--name-only", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1", "src/controle_ia/iib", "scripts")
for f in out.splitlines():
    if "design" in f or "iib" in f:
        print(" ", f)
