import os, sys, stat, tarfile, re
sp, out = sys.argv[1], sys.argv[2]
racines = [("bloc-notes-session14", "."), ("reprise-20261020", "session16/reprise-20261020"),
           ("canal-gemini", "session16/canal-gemini"), ("voisins", "session16/voisins"),
           ("outils-archive", "session16/outils-archive"), ("tokeniseur-refait", "session16/tokeniseur-refait"), ("consignes-lancement-s16", "session16/consignes-lancement-s16")]
EXCL_DIRS = {"__pycache__", ".pytest_cache", "donnees", "diag", "runs", ".git", "node_modules", "pytest-of-root",
             "site-packages", "venv", ".venv"}
def interdit(nom):
    n = nom.lower()
    return (n.endswith(".pdf") or "textes-actions" in n or "p3-consignes" in n
            or n.endswith((".pyc", ".npz", ".safetensors", ".pt", ".bin")))
fichiers, ecartes = [], []
for src, dst in racines:
    base = os.path.join(sp, src)
    if not os.path.isdir(base):
        continue
    for d, sous, fs in os.walk(base):
        if os.path.lexists(os.path.join(d, ".git")):
            sous[:] = []; ecartes.append(("clone git", d)); continue
        sous[:] = [s for s in sous if s not in EXCL_DIRS and not os.path.islink(os.path.join(d, s))]
        for f in fs:
            p = os.path.join(d, f)
            st = os.lstat(p)
            if not stat.S_ISREG(st.st_mode):
                ecartes.append(("pas un fichier ordinaire", p)); continue
            if interdit(f):
                continue
            if st.st_size > 20_000_000:
                ecartes.append(("taille", p)); continue
            rel = os.path.relpath(p, base)
            fichiers.append((p, os.path.normpath(os.path.join(dst, rel))))
jet = re.compile(rb"(hf_[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-ant-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{30,})")
cles = [os.environ.get(k, "") for k in os.environ if any(m in k for m in ("KEY", "TOKEN", "SECRET"))]
cles = [c.encode() for c in cles if len(c) >= 12]
suspects = []
for p, a in fichiers:
    with open(p, "rb") as fh:
        b = fh.read()
    if jet.search(b) or any(c in b for c in cles):
        suspects.append(a)
print("fichiers :", len(fichiers), "; écartés :", len(ecartes), "; suspects de jeton :", len(suspects), flush=True)
for s in suspects[:30]:
    print("  SUSPECT", s)
if suspects:
    sys.exit(3)
nom = os.path.join(out, "bloc-notes-session16-2026-10-21.tar.gz")
with tarfile.open(nom, "w:gz") as t:
    for p, a in sorted(fichiers, key=lambda x: x[1]):
        t.add(p, arcname="./" + a, recursive=False)
with open(os.path.join(out, "bloc-notes-session16-2026-10-21-liste.txt"), "w") as fh:
    fh.write("\n".join("./" + a for _, a in sorted(fichiers, key=lambda x: x[1])) + "\n")
with open(os.path.join(out, "ecartes.txt"), "w") as fh:
    fh.write("\n".join(f"{r}\t{p}" for r, p in ecartes) + "\n")
print("archive", os.path.getsize(nom), "octets", flush=True)
