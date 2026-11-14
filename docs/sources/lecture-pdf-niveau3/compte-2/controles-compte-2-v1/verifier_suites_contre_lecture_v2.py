"""Vérifie que chaque constat attendu a une entrée et une seule « corrigé » ou « réserve maintenue » dans une table.
La première cellule d'une ligne commence par l'identifiant (lettre, ou lettre suivie de chiffres : A, B1, M14),
éventuellement en gras, suivi d'un blanc, d'un tiret, d'une barre ou de la fin de cellule.
Usage : python3 -I verifier_suites_contre_lecture_v2.py <rapport.md> <identifiants séparés par des virgules>
Exemple : ... synthese.md B1,B2,B3,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12,M13,M14"""
import re, sys
texte = open(sys.argv[1], encoding="utf-8").read()
attendus = [x.strip() for x in sys.argv[2].split(",") if x.strip()]
trouve = {}
for ligne in texte.splitlines():
    m = re.match(r"\|\s*\**([A-Z]\d{0,2})\**(?=[\s*|—-])", ligne)
    if not m: continue
    cellules = [c.strip().strip("*").strip() for c in ligne.strip().strip("|").split("|")]
    dec = [c for c in cellules if c in ("corrigé", "réserve maintenue")]
    if dec: trouve.setdefault(m.group(1), []).append(dec[0])
ko = 0
for l in attendus:
    v = trouve.get(l, [])
    if len(v) == 1: print(f"{l} : {v[0]}")
    else: ko += 1; print(f"ÉCHEC {l} : {v or 'aucune entrée'}")
print(f"constats : {len(attendus)} ; avec une entrée : {len(attendus)-ko} ; échecs : {ko}")
sys.exit(1 if ko else 0)
