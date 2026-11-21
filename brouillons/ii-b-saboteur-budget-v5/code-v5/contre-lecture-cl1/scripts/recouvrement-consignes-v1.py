"""Recherche, par programme, de fragments des consignes privées dans les correctifs 0004 à 0006 (code, essais, configuration,
messages de commit). N'imprime AUCUN texte de consigne : seulement des comptes, et les numéros de ligne du correctif concerné.
n-grammes de 5 mots normalisés ; on retire ceux qui figurent dans le texte scellé de la conception et dans les deux mandats
(textes publics du dépôt), qui ne sont donc pas propres aux consignes. Appel : python3 -I ce_script.py RACINE"""
import re, sys, glob, os
R = sys.argv[1]
def mots(t): return re.findall(r"[a-zà-ÿ0-9]+", t.lower())
def ngr(t, n=5):
    m = mots(t); return {" ".join(m[i:i+n]) for i in range(len(m)-n+1)}
cons = sorted(glob.glob(R + "/brouillons/ii-b-saboteur-budget-v5/consignes-v5/consigne*-v*.md")) + \
       [R + "/brouillons/ii-b-saboteur-budget-v1/consigne-privee-maitre-ii-b-v1-brouillon2.md", R + "/prereg/P3-consignes-v1.md"]
public = set()
for p in [R + "/brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1.md",
          R + "/registres/iib-reconception/mandat-developpeur-code-organisme-retenu-v5-v1.md",
          R + "/registres/iib-reconception/mandat-contre-lecteur-code-organisme-retenu-v5-v1.md"]:
    public |= ngr(open(p, encoding="utf-8").read())
patchs = sorted(glob.glob(R + "/brouillons/ii-b-saboteur-budget-v5/code-v5/correctifs/000[456]-*.patch"))
lignes = []
for p in patchs:
    for i, l in enumerate(open(p, encoding="utf-8", errors="replace").read().split("\n"), 1):
        if l.startswith("+") or not l.startswith(("-", " ", "@", "diff", "index")):
            lignes.append((os.path.basename(p)[:4], i, ngr(l)))
for c in cons:
    g = ngr(open(c, encoding="utf-8").read()) - public
    touchees = [(n, i, len(s & g)) for n, i, s in lignes if s & g]
    print(f"{os.path.basename(c)} : {len(g)} n-grammes propres ; lignes de correctif touchées : {len(touchees)}"
          + (" ; " + ", ".join(f"{n}:{i}({k})" for n, i, k in touchees[:40]) if touchees else ""))
