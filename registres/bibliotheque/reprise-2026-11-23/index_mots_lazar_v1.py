"""Index des mots de Lazar du 23 novembre tirés de registres/go.md (classe C, bibliothécaire). Usage : python -I index_mots_lazar_v1.py GO.md
Sort une ligne Markdown par GO du 23 : identifiant, heure, nature, mot cité (premières citations entre guillemets), pièce ou chantier touché (début de la description après le mot), plafond."""
import re, sys
for l in open(sys.argv[1], encoding="utf-8"):
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) < 5 or not c[0].startswith("GO-2026-11-23-"): continue
    t = c[3]
    h = re.search(r"2026-11-23T(\d\d:\d\d(?::\d\d)?)Z", t); h = h.group(1) if h else "?"
    q = re.findall(r"«\s*(.*?)\s*»", t)
    mot = " / ".join(q)[:420] if q else "(sans citation dans la ligne)"
    reste = re.sub(r"«.*?»", "«…»", t)
    print(f"| {c[0]} | {h} | {c[2]} | « {mot.replace('|','/')} » | {reste.strip(' —-:;')[:380].replace('|','/')} | {c[4]} |")
