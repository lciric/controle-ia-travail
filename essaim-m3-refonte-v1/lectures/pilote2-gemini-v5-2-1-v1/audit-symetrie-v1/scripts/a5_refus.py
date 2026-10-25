"""Audit de symétrie, pilote 2 — appels hors OK : à quelles tâches de test correspondent-ils ? Lecture seule.
Usage : python3 -I a5_refus.py RACINE_ESPACE_TRAVAIL (M ou S)"""
import json, sys, pathlib, collections
b = json.load(open("/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/banque/banque-confrontation-v1.json"))
tests = b["test"] + b["test_final"]
R = pathlib.Path(sys.argv[1])
for g in ("g000", "g001"):
    lignes = [json.loads(l) for l in (R / f"{g}.noyau" / "journal-appels.jsonl").read_text().splitlines() if l.strip()]
    if g == "g000":
        print("clés du journal :", sorted(lignes[0].keys()))
    hors = [l for l in lignes if l.get("statut") != "OK"]
    items = collections.Counter()
    for l in hors:
        ida = str(l.get("id_appel") or l.get("id") or "")
        p = R / f"{g}.noyau" / "appels" / f"{ida}.prompt.txt"
        if not p.exists():
            cands = sorted((R / f"{g}.noyau" / "appels").glob(f"*{ida}*.prompt.txt"))
            p = cands[0] if cands else None
        txt = p.read_text(encoding="utf-8", errors="replace") if p else ""
        trouve = [t["id"] for t in tests if t["texte"][:300] in txt]
        items[(l.get("statut"), l.get("role"), tuple(trouve))] += 1
    print(g, "appels hors OK :", len(hors), "->", dict(items))
