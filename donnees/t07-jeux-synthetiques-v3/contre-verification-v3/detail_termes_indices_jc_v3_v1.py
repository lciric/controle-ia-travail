#!/usr/bin/env python3
"""Lot 2, étape 3 : détail par terme des indices I1, I2 et I3 du lecteur (information seulement ; la règle de décision est
celle du décompte, sur l'expression entière) — v1. Même règle que le précédent : expression sans casse, présente dans un
seul membre, membre gonflé ; part = compte / 320.
Usage : python -I -B detail_termes_indices_jc_v3_v1.py <J-C> <décompte JSON> <sortie JSON à créer>"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

JC, DEC, SORTIE = (Path(a) for a in sys.argv[1:4])
assert hashlib.sha256(JC.read_bytes()).hexdigest() == "99b4f1b25daa84f16b6c8c8dec06fede52ec7538f085d95b09e7e20bec627447"
paires: dict = {}
for l in JC.read_text(encoding="utf-8").splitlines():
    r = json.loads(l)
    paires.setdefault((r["tache"], r["paire"]), {})[r["etiquette"]] = r
P = list(paires.values())
dec = json.loads(DEC.read_text(encoding="utf-8"))
out = {"outil_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "indices": {}}
for ind in dec["indices_de_surface"]:
    if ind["id"] not in ("I1", "I2", "I3"):
        continue
    m = re.fullmatch(r"(\w+: \.\*)\\b\((.*)\)\\b", ind["regle"])
    tete, termes = m.group(1), m.group(2).split("|")
    lignes = {}
    for t in termes:
        rx = re.compile(rf"{tete}\b({t})\b", re.I)
        g = h = sens = 0
        for v in P:
            a, b = bool(rx.search(v[0]["reponse"])), bool(rx.search(v[1]["reponse"]))
            g += b
            h += a
            sens += b and not a
        lignes[t] = {"gonfle": g, "honnete": h, "gonfle_seul": sens}
    # l'expression sans chaque terme, tour à tour (sensibilité de la règle entière)
    sans = {}
    for t in termes:
        reste = "|".join(x for x in termes if x != t)
        rx = re.compile(rf"{tete}\b({reste})\b", re.I)
        sans[t] = sum(1 for v in P if bool(rx.search(v[1]["reponse"])) and not rx.search(v[0]["reponse"]))
    out["indices"][ind["id"]] = {"par_terme": lignes, "expression_sans_ce_terme_dans_le_sens": sans}
with open(SORTIE, "x", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
for k, v in out["indices"].items():
    print(k, {t: (x["gonfle_seul"], x["gonfle"], x["honnete"]) for t, x in v["par_terme"].items()})
    print("  sans:", v["expression_sans_ce_terme_dans_le_sens"])
