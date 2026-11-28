"""Énoncés de HC1, HC2, HC2b, HC3 (composantes 1 et 2, jusqu'au point final de l'énoncé) et « Pièces revendiquées » :
égaux entre les brouillons 3, 6 et 7 ? (« Pièces revendiquées », absent du brouillon 3, comparé entre 6 et 7) — v1. Usage : python3 -B -I enonces_b3_b6_b7_v1.py B3 B6 B7"""
import sys, re, hashlib
txt = [open(p, encoding="utf-8").read() for p in sys.argv[1:4]]
def extr(t, debut, fin=None):
    i = t.index(debut); j = t.index("\n", i) if fin is None else t.index(fin, i) + len(fin)
    return re.sub(r"\s+", " ", t[i:j])
CLES = [("HC1 ligne 1", "- un moniteur génératif de contrôle", None), ("HC1 ligne 2", "- g et ĉ sont estimés", None),
        ("HC2", "- **HC2, robustesse**", None), ("HC2b", "- **HC2b, trahison par les activations**", None),
        ("HC3 acquis", "- **cité comme acquis**", None), ("HC3 comp. 1", "- **revendiqué, composante 1**", None),
        ("HC3 comp. 2 (énoncé)", "- **revendiqué, composante 2**", "l'agent auteur."),
        ("Pièces revendiquées", "**Pièces revendiquées**", "(N-013).")]
ok = True
for nom, d, f in CLES:
    e = [extr(t, d, f) if d in t else None for t in txt]
    if e[0] is None:  # « Pièces revendiquées » n'existe pas au brouillon 3 (ajouté ensuite) : comparé entre 6 et 7
        e[0] = e[1]
    h = [hashlib.sha256(x.encode()).hexdigest()[:10] for x in e]
    egal = len(set(e)) == 1; ok &= egal
    print(f"{nom:22s} b3 {h[0]} b6 {h[1]} b7 {h[2]} égaux : {egal}")
print("énoncés inchangés depuis le brouillon 3 :", ok)
