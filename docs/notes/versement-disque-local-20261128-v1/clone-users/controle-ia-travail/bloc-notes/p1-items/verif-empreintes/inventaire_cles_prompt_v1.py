# -*- coding: utf-8 -*-
"""Inventaire (lecture seule) des cles d'empreinte de PROMPT/INVITE stockees dans les JSON
des sources candidates. Exclut les fichiers interdits sans les ouvrir."""
import json, os, re, sys, collections
RACINES = ["/home/user/archive-2026-09", "/home/user/p1-auto",
           "/home/user/sycophancy-construct-validity", "/home/user/lciric",
           "/home/user/cplt_run_2026-09-03"]
EXCLUS_DIR = {".git", ".venv", "venv", "__pycache__", "node_modules"}
MOTIF = re.compile(r"(prompt|invite|items_sha|entree)", re.I)
MOTIF_SHA = re.compile(r"(sha|empreinte)", re.I)
res = collections.defaultdict(collections.Counter)
def walk(o, f):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(k, str) and MOTIF.search(k) and MOTIF_SHA.search(k):
                res[f][k] += 1
            walk(v, f)
    elif isinstance(o, list):
        for x in o:
            walk(x, f)
    elif isinstance(o, str) and o.startswith("{'sha256_invite'"):
        res[f]["(chaine) sha256_invite"] += 1
for r in RACINES:
    for d, ds, fs in os.walk(r):
        ds[:] = [x for x in ds if x not in EXCLUS_DIR]
        for fn in fs:
            if not fn.endswith(".json") or fn.startswith("textes-actions-"):
                continue
            p = os.path.join(d, fn)
            try:
                if os.path.getsize(p) > 60_000_000:
                    continue
                o = json.load(open(p, encoding="utf-8"))
            except Exception:
                continue
            walk(o, p)
for f in sorted(res):
    print(f, dict(res[f]))
