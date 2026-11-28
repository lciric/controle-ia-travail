"""Vérificateur v5 fidélité : position de chaque ancien texte dans la v4 d'origine et dans le texte courant (rejeu pas à pas),
recouvrements entre remplacements. Usage : python3 -I -B analyse_remplacements.py SCRIPT V4"""
import sys, importlib.util
spec = importlib.util.spec_from_file_location("corr", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
v4 = open(sys.argv[2], encoding="utf-8").read()
t = v4
pos = []
for i, (qui, old, new) in enumerate(m.R, 1):
    n0, n = v4.count(old), t.count(old)
    p = v4.find(old)
    ligne = v4[:p].count("\n") + 1 if p >= 0 else None
    print(f"{i:2d} | v4 d'origine : {n0} fois{f', l. {ligne}' if ligne else ''} | texte courant : {n} fois | {qui}")
    if p >= 0:
        pos.append((p, p + len(old), i))
    t = t.replace(old, new)
pos.sort()
rec = [(a[2], b[2]) for a, b in zip(pos, pos[1:]) if a[1] > b[0]]
print("recouvrements dans la v4 d'origine :", rec or "aucun")
print("ancien texte absent de la v4 d'origine (appliqué sur le texte d'un remplacement précédent) :",
      [i for i, (q, o, n) in enumerate(m.R, 1) if v4.count(o) == 0])
