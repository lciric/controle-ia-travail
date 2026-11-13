"""Vérifie que chaque constat attendu a une ligne « corrigé » ou « réserve maintenue » dans la table de suite.
Usage : python3 -I verifier_suites_contre_lecture.py <rapport.md> <lettres, ex. ABCDEFGH>"""
import re, sys
texte = open(sys.argv[1], encoding="utf-8").read()
attendus = list(sys.argv[2])
trouve = {}
for ligne in texte.splitlines():
    m = re.match(r"\|\s*\**([A-Z]\d{0,2})(?=[\s*|—-])", ligne)
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
