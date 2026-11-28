"""Vérifie que les lignes d'énoncé de HC1, HC2, HC2b, HC3 du brouillon 6 sont présentes, égales, dans le brouillon 7 — v1.
Usage : python3 -B -I enonces_b6_b7_v1.py B6 B7"""
import sys
b6 = open(sys.argv[1], encoding="utf-8").read().splitlines()
b7 = set(open(sys.argv[2], encoding="utf-8").read().splitlines())
debuts = ("  - un moniteur génératif de contrôle", "  - g et ĉ sont estimés", "- **HC2, robustesse**",
          "- **HC2b, trahison par les activations**", "  - **cité comme acquis**", "  - **revendiqué, composante 1**",
          "  - **revendiqué, composante 2**", "**Pièces revendiquées**")
ok = True
for d in debuts:
    l6 = [l for l in b6 if l.startswith(d)]
    assert len(l6) == 1, d
    present = l6[0] in b7
    ok &= present
    print(f"{d.strip()[:45]:45s} : ligne égale au brouillon 6 : {present}")
print("énoncés inchangés :", ok)
