# copie de la logique de src/controle_ia/prereg.py (problemes), sans importer le depot
import re, sys
SECTIONS = ("Hypothèse","Prédiction chiffrée et signe attendu","Métrique","Seuil","Plan d'analyse","Critères de lecture gelés","Liste d'arrêt","Contre-lecture")
MARQUEUR = "À REMPLIR"
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPREINTE = re.compile(r"\b[0-9a-f]{64}\b")
ENTREE = re.compile(r"^\s*-?\s*\**Contre-lecture (\d+)\**", re.M)
def sections(texte):
    m = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    return {t.strip(): c.strip() for t, c in zip(m[1::2], m[2::2])}
texte = open(sys.argv[1], encoding="utf-8").read()
s = sections(texte)
print("sections:", list(s))
sortie = []
for nom in SECTIONS:
    if nom not in s: sortie.append("absente " + nom)
    elif not s[nom] or MARQUEUR in s[nom]: sortie.append("vide " + nom)
if MARQUEUR in texte: sortie.append("marqueur hors sections")
cl = s.get("Contre-lecture")
if cl:
    ent = list(ENTREE.finditer(cl))
    print("entrees:", [e.group(1) for e in ent])
    if not ent and len(set(EMPREINTE.findall(cl))) < 2: sortie.append("cl sans 2 empreintes")
    for k, e in enumerate(ent):
        fin = ent[k+1].start() if k+1 < len(ent) else len(cl)
        n = len(set(EMPREINTE.findall(cl[e.start():fin])))
        print("entree", e.group(1), "empreintes:", n)
        if n < 2: sortie.append("entree sans 2 empreintes")
r = sorted(set(GABARIT.findall(texte)))
if r: sortie.append("gabarit " + ",".join(r))
print("problemes:", sortie)
for nom in SECTIONS:
    print(f"{nom}: {len(s.get(nom,''))} caracteres")
