#!/usr/bin/env python3
"""Extrait de calcul-devis-essaim-v1.json les totaux par ligne (pilote, confirmatoire, instruments, inédites) et par poste,
pour la note du devis. Usage : python3 -I -B extraire_lignes_devis_v1.py DEVIS.json"""
import json
import sys

d = json.load(open(sys.argv[1], encoding="utf-8"))
for esp in ("claude-1", "kimi", "fable-5-2", "claude-2"):
    for r in ("bas", "attendu", "haut"):
        for mode in ("estimation", "pire"):
            x = d["devis_par_espece"][esp][r][mode]["par_ligne"]
            print(esp, r, mode, {l: (v["total_usd"], v["perimetre_section_D_sans_tests_usd"]) for l, v in x.items()})
x = d["devis_par_espece"]["claude-1"]["attendu"]["estimation"]["par_ligne"]["confirmatoire"]["lignes"]
print("postes claude-1 attendu estimation confirmatoire", json.dumps(x, ensure_ascii=False))
x = d["devis_par_espece"]["claude-1"]["attendu"]["pire"]["par_ligne"]["confirmatoire"]["lignes"]
print("postes claude-1 attendu pire confirmatoire", json.dumps(x, ensure_ascii=False))
