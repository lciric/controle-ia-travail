"""Énoncés de HC1, HC2, HC2b, HC3 : chaque ligne d'énoncé du brouillon 3 (section « Hypothèse », lignes qui
commencent par « - **HC » et leurs sous-puces d'énoncé) est-elle présente mot pour mot aux brouillons 5 et 6 ?"""
import re, sys
b3, b5, b6 = (open(p, encoding="utf-8").read() for p in sys.argv[1:4])
def section(t):
    a = t.index("## Hypothèse"); b = t.index("## Prédiction", a)
    return t[a:b]
s3 = section(b3)
lignes = [l for l in s3.split("\n") if l.strip()]
for l in lignes:
    print(("B5 oui" if l in b5 else "B5 NON"), ("B6 oui" if l in b6 else "B6 NON"), "|", l[:110])
def piece_inutile(t):
    a = t.index("**Pièces revendiquées**"); b = t.index("**Hypothèses de travail**", a); return t[a:b]

