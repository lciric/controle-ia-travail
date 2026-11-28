# -*- coding: utf-8 -*-
"""Balayage par empreinte (lecture seule) : retrouve sur disque les fichiers dont le sha256
commence par un prefixe cite par le projet precedent. Exclut les fichiers interdits
(prereg/P3-consignes-v1.md, textes-actions-*) SANS les ouvrir, et .git/.venv."""
import hashlib, os, sys, json
RACINES = ["/home/user/archive-2026-09", "/home/user/p1-auto",
           "/home/user/sycophancy-construct-validity", "/home/user/lciric",
           "/home/user/cplt_run_2026-09-03", "/home/user/controle-ia-travail"]
INTERDIT_CHEMIN = {"/home/user/controle-ia-travail/prereg/P3-consignes-v1.md"}
EXCLUS_DIR = {".git", ".venv", "venv", "__pycache__", "node_modules"}
CIBLES = dict(a.split("=", 1) for a in sys.argv[1:])
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()
trouve = {k: [] for k in CIBLES}
n = 0
for r in RACINES:
    for d, ds, fs in os.walk(r):
        ds[:] = [x for x in ds if x not in EXCLUS_DIR]
        for f in fs:
            p = os.path.join(d, f)
            if p in INTERDIT_CHEMIN or f.startswith("textes-actions-") or os.path.islink(p):
                continue
            try:
                h = sha(p)
            except OSError:
                continue
            n += 1
            for k, pre in CIBLES.items():
                if h.startswith(pre):
                    trouve[k].append((p, h))
print("fichiers haches :", n)
for k, v in trouve.items():
    print(f"{k:28s} {CIBLES[k]:16s} -> {len(v)}")
    for p, h in v:
        print("     ", h, p)
