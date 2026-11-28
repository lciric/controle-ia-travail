import subprocess, json, hashlib

GIT_DIR = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\.git"

def git(*args):
    r = subprocess.run(["git", f"--git-dir={GIT_DIR}", *args], capture_output=True, text=True, encoding="utf-8", errors="replace", env={"GIT_TERMINAL_PROMPT": "0", "PATH": subprocess.os.environ.get("PATH", "")})
    return r.returncode, r.stdout, r.stderr

print("=== 1. FULL journal.txt EVALUATION / DISTILLATION / FIN FROM 3326499e ===")
rc, out, _ = git("show", "3326499e666c6b2a3670feda6ee5e15ed055170a:traces/iib-20261123-132033-c3YM/journal.txt")
for line in out.splitlines():
    if any(k in line.lower() for k in ("evaluation", "distillation", "tours finis", "fin de la course", "debut", "engagee", "tour=1 ", "tour 001", "tour=20", "tour 020", "phase=fin", "oracle")):
        print(" ", line)

print("\n=== 2. CHECK ALL COMMITS REACHABLE FROM origin/barreau8/cote-expose-pieces-lecture-v1 ===")
rc, out, _ = git("log", "-n", "10", "--stat", "origin/barreau8/cote-expose-pieces-lecture-v1")
print(out[:2500])

print("\n=== 3. CHECK origin/barreau8/conductrice-lecture-sondes-v1 ===")
rc, out, _ = git("log", "-n", "10", "--stat", "origin/barreau8/conductrice-lecture-sondes-v1")
print(out[:2500])

print("\n=== 4. CHECK designation-iib-v5.json AND ITS COMMIT / CONFIG COURSE ===")
rc, out, _ = git("show", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1:docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-voie-a-course-v1.json")
if rc == 0:
    d = json.loads(out)
    print("config-course oracle_de_la_regle:", json.dumps(d.get("oracle_de_la_regle"), indent=2))
    print("config-course go_id:", d.get("go_id"))
    print("config-course pieces:", json.dumps(d.get("pieces"), indent=2))

print("\n=== 5. CHECK IF etats-evaluation-iib-v5.json HAS TIMESTAMPS ===")
rc, out, _ = git("show", "3326499e666c6b2a3670feda6ee5e15ed055170a:diag/20261122-202132-iib-reel/etats-evaluation-iib-v5.json")
if rc == 0:
    print(out[:1500])

print("\n=== 6. CHECK designation_v5.py IN 192a429e ===")
rc, out, _ = git("show", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1:src/controle_ia/iib/designation_v5.py")
if rc == 0:
    print("designation_v5.py len:", len(out))
    for i, l in enumerate(out.splitlines(), 1):
        if any(k in l.lower() for k in ("heure", "date", "instant", "utc", "designation-iib", "scell", "conception", "regle")):
            print(f"  L{i}: {l}")
