import subprocess, json, hashlib, re, pathlib

GIT_DIR = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\.git"
REPO = pathlib.Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")

def git_bytes(*args):
    r = subprocess.run(["git", f"--git-dir={GIT_DIR}", *args], capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode("utf-8", errors="replace")

def git(*args):
    rc, out, err = git_bytes(*args)
    return rc, out.decode("utf-8", errors="replace"), err

def show_text(rev, path):
    rc, b, err = git_bytes("show", f"{rev}:{path}")
    if rc != 0:
        return None, None, err.strip()
    return b.decode("utf-8", errors="replace"), hashlib.sha256(b).hexdigest(), ""

print("=== 1. TRACES IN 3326499e ===")
rc, out, _ = git("ls-tree", "-r", "--name-only", "3326499e666c6b2a3670feda6ee5e15ed055170a", "traces")
for f in out.splitlines():
    print(" ", f)
    if f.endswith(".txt") or f.endswith(".json") or f.endswith(".log"):
        txt, sha, _ = show_text("3326499e666c6b2a3670feda6ee5e15ed055170a", f)
        if txt and len(txt) < 15000:
            print(f"--- CONTENT {f} ---")
            print(txt)
        elif txt:
            print(f"--- HEAD/TAIL {f} (len={len(txt)}) ---")
            print("\n".join(txt.splitlines()[:25]))
            print("...")
            print("\n".join(txt.splitlines()[-25:]))

print("\n=== 2. ETALONNAGE FILES IN 192a429e ===")
for p in [
    "runs/20261122-202132-iib-reel/manifeste.json",
    "diag/20261122-202132-iib-reel/resume.json",
    "diag/20261122-202132-iib-reel/branches-iib-v5.json",
    "diag/20261122-202132-iib-reel/vitesse-premier-lot-iib-v5.json",
]:
    txt, sha, err = show_text("192a429e67b93e9a89d273ba5a4b5c0c61d139f1", p)
    print(f"\n--- 192a429e:{p} (sha={sha}, err={err}) ---")
    if txt:
        d = json.loads(txt)
        compact = {k: v for k, v in d.items() if k not in ("graines", "empreintes", "config", "lignes")}
        if "config" in d and isinstance(d["config"], dict):
            compact["config_go_id"] = d["config"].get("go_id")
            compact["config_pieces"] = d["config"].get("pieces")
        print(json.dumps(compact, indent=2, ensure_ascii=False)[:2500])

print("\n=== 3. CONFIG COURSE IN 192a429e ===")
rc, out, _ = git("ls-tree", "-r", "--name-only", "192a429e67b93e9a89d273ba5a4b5c0c61d139f1", "docs/notes/barreau8-iib-v1", "diag/20261122-202132-iib-reel")
for f in out.splitlines():
    if "config" in f or "designation" in f or "ordre" in f or "resume" in f or "manifeste" in f:
        rc2, b, _ = git_bytes("show", f"192a429e67b93e9a89d273ba5a4b5c0c61d139f1:{f}")
        sha = hashlib.sha256(b).hexdigest() if rc2 == 0 else None
        print(f"  {f}  sha={sha}")

print("\n=== 4. CHECK CONFIG COURSE CONTENT ===")
for f in out.splitlines():
    if "course" in f and f.endswith(".json") and "config" in f:
        txt, sha, _ = show_text("192a429e67b93e9a89d273ba5a4b5c0c61d139f1", f)
        d = json.loads(txt)
        print(f"File {f} (sha={sha}):")
        for k in ("go_id", "code", "oracle_de_la_regle", "pieces", "prefixe_graines"):
            print(f"  {k}: {json.dumps(d.get(k), ensure_ascii=False)}")

print("\n=== 5. GREP REPO FOR 78045af7, 8cac7bbd, 61875617, c1dc5459, designation-iib-v5 ===")
for pat in ["78045af7", "8cac7bbd", "designation-iib-v5", "13:27:38", "20:29:04", "04:41:59", "04:41:56", "11:24:13"]:
    print(f"\n-- grep {pat} in registres/ --")
    for p in (REPO / "registres").rglob("*.md"):
        txt = p.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(txt.splitlines(), 1):
            if pat in line:
                print(f"  {p.relative_to(REPO)}:L{i}: {line[:260]}")
