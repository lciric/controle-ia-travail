#!/usr/bin/env python3
"""Mesure en jetons (tokeniseur conforme, copie hors de l'arbre) des deux membres d'une paire, réponse entière et texte avant COST.
Usage : mesure_jetons_v1.py TOKENIZER.json FICHIER.jsonl PAIRE [JEU]  → écarts relatifs ; seuil du script officiel 0,15 ; cible ≤ 0,12."""
import json, sys
from tokenizers import Tokenizer
tk = Tokenizer.from_file(sys.argv[1]); f = sys.argv[2]; p = int(sys.argv[3]); jeu = sys.argv[4] if len(sys.argv) > 4 else None
rs = [json.loads(l) for l in open(f)]
rs = [r for r in rs if r["paire"] == p and r["etiquette"] in (0, 1) and (jeu is None or r["jeu"] == jeu)]
n = {}
for r in rs:
    rep = r["reponse"]; av = rep[:rep.find("\nCOST:") + 1]
    n[r["etiquette"]] = (len(tk.encode(rep, add_special_tokens=False).ids), len(tk.encode(av, add_special_tokens=False).ids))
for i, nom in ((0, "entière"), (1, "avant COST")):
    a, b = n[0][i], n[1][i]
    print(f"{nom}: étiquette 0 = {a}, étiquette 1 = {b}, écart relatif = {abs(a-b)/max(a,b):.3f}")
