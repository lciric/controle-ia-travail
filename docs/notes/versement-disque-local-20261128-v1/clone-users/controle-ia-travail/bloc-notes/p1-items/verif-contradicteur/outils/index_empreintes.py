# Index sha256 de tous les fichiers des arbres candidats (lecture seule).
# Exclut .git et, dans controle-ia-travail, prereg/P3-consignes-v1.md et tout textes-actions-*.
import hashlib, os, sys
RACINES = ["/home/user/archive-2026-09", "/home/user/p1-auto", "/home/user/sycophancy-construct-validity",
           "/home/user/lciric", "/home/user/cplt_run_2026-09-03", "/home/user/controle-ia-travail"]
INTERDIT = "/home/user/controle-ia-travail/prereg/P3-consignes-v1.md"
out = open(sys.argv[1], "w", encoding="utf-8")
n = 0
for r in RACINES:
    for d, ds, fs in os.walk(r):
        ds[:] = [x for x in ds if x not in (".git", ".venv", "__pycache__", "node_modules")]
        for f in fs:
            p = os.path.join(d, f)
            if p == INTERDIT or "textes-actions-" in f:
                continue
            if os.path.islink(p) or not os.path.isfile(p):
                continue
            h = hashlib.sha256()
            with open(p, "rb") as fh:
                for b in iter(lambda: fh.read(1 << 20), b""):
                    h.update(b)
            out.write(f"{h.hexdigest()}\t{os.path.getsize(p)}\t{p}\n")
            n += 1
out.close()
print(n)
