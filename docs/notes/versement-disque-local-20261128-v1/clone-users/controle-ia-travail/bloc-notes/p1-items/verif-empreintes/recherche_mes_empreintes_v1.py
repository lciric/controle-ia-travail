# -*- coding: utf-8 -*-
"""Cherche, dans tous les fichiers texte des sources candidates, chacune de MES empreintes
(30 textes + 90 prompts, sha256 complet et prefixes de 16 caracteres). Lecture seule.
Exclut les fichiers interdits sans les ouvrir."""
import json, os, sys, collections
T = json.load(open(sys.argv[1], encoding="utf-8"))["mes_empreintes"]
cibles = {}
for x in T:
    for k, v in x.items():
        if k.startswith("sha256_"):
            cibles[v] = (x["item"], k)
pref = {v[:16]: c for v, c in cibles.items()}
RACINES = ["/home/user/archive-2026-09", "/home/user/p1-auto",
           "/home/user/sycophancy-construct-validity", "/home/user/lciric",
           "/home/user/cplt_run_2026-09-03", "/home/user/controle-ia-travail"]
EXCLUS = {".git", ".venv", "venv", "__pycache__", "node_modules"}
INTERDIT = {"/home/user/controle-ia-travail/prereg/P3-consignes-v1.md"}
SCRATCH = "/tmp/claude-0"
hits = collections.defaultdict(lambda: collections.Counter())
for r in RACINES:
    for d, ds, fs in os.walk(r):
        ds[:] = [x for x in ds if x not in EXCLUS]
        for f in fs:
            p = os.path.join(d, f)
            if p in INTERDIT or f.startswith("textes-actions-") or os.path.islink(p):
                continue
            if os.path.getsize(p) > 80_000_000 or f.endswith((".npz", ".pt", ".npy", ".pdf", ".png", ".ots")):
                continue
            try:
                s = open(p, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            if not any(c in s for c in "0123456789abcdef"):
                continue
            for v, c in cibles.items():
                if v in s:
                    hits[p][("complet",) + tuple(map(str, c))] += s.count(v)
            for v, c in pref.items():
                n = s.count(v) - s.count(next(k for k in cibles if k.startswith(v)))
                if n > 0:
                    hits[p][("prefixe16",) + tuple(map(str, c))] += n
for p in sorted(hits):
    kinds = collections.Counter()
    items = collections.defaultdict(set)
    for (forme, it, k), n in hits[p].items():
        kinds[(forme, k)] += n
        items[(forme, k)].add(int(it))
    print(p)
    for (forme, k), n in sorted(kinds.items()):
        print("    %-10s %-22s occurrences %5d  items distincts %2d" % (forme, k, n, len(items[(forme, k)])))
