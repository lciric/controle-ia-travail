#!/usr/bin/env python3
"""Imprime le résumé de soumissions par identifiant de forum, à partir des réponses brutes déjà journalisées.
Usage : lire_openreview.py LONGUEUR ID [ID...]"""
import sys, json, glob, re, datetime
n = int(sys.argv[1]); ids = sys.argv[2:]
vu = {}
for f in sorted(glob.glob("brut/*-openreview.json")):
    try: d = json.load(open(f, encoding="utf-8"))
    except Exception: continue
    for note in d.get("notes", []):
        k = note.get("forum") or note.get("id")
        if k in ids and k not in vu: vu[k] = note
for k in ids:
    note = vu.get(k)
    if not note: print("=====", k, ": absent des réponses brutes"); continue
    c = note.get("content", {})
    g = lambda key: (c.get(key, {}) or {}).get("value", "") if isinstance(c.get(key), dict) else (c.get(key) or "")
    t = (note.get("cdate") or 0) / 1000
    date = datetime.datetime.fromtimestamp(t, datetime.UTC).strftime("%Y-%m-%d") if t else "?"
    print("=====", k, "|", date, "|", g("venue"), "|", re.sub(r"\s+", " ", str(g("title"))))
    print("   mots-clés :", g("keywords"))
    print("   " + re.sub(r"\s+", " ", str(g("abstract")))[:n])
