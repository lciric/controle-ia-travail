"""Prolongement de la simulation scellee de la contre-lecture (variante V2, bruit asymetrique) a 4,3 et 4,5 ecarts types,
pour controler directement le « ≈ 4,3 ecarts types, ≈ 0,39 » de la correction m6.1 (une extrapolation dans le rapport).
Verificateur Claude Opus 5.5. Seules les definitions de fonctions du script de la contre-lecture sont chargees, par son
arbre syntaxique (module ast) ; sa campagne n'est pas executee. Memes tailles que lui (2 000 tirages, 4 000 vecteurs de
signes, 400 jeux par effet et par signe), meme entropie, cles de graine neuves (9, j, signe), distinctes des siennes.
Usage : python3 -B prolongement-v2-m6-verification-v1.py <script de la contre-lecture> <sortie .json>
"""
import ast
import json
import math
import sys

import numpy as np

source = open(sys.argv[1], encoding="utf-8").read()
arbre = ast.parse(source)
module = ast.Module(body=[n for n in arbre.body if isinstance(n, ast.FunctionDef)], type_ignores=[])
ENT = 119398714658723140935360634172411817158
espace = dict(np=np, math=math, T=32, K=10, B=2000, NS=4000, ENT=ENT)
exec(compile(module, sys.argv[1], "exec"), espace)
V2 = dict(part_texte=0.6, sd_ep=0.5, k_adapt=1.5, loi="asym")
SE = 0.09            # ecart type d'estimation de V2 dans la sortie scellee (« ecart_type_vrai »)
out = {"entropie": ENT, "ecart_type_V2": SE, "rep_effet": 400, "puissance_critere_double": {}}
for j, mult in enumerate((4.3, 4.5)):
    for sgn in (1, -1):
        r = espace["campagne"]((9, j, 1 if sgn > 0 else 0), V2, sgn * mult * SE, 400)
        cle = "dbl_haut" if sgn > 0 else "dbl_bas"
        out["puissance_critere_double"][f"{'+' if sgn > 0 else '-'}{mult}se_{sgn * mult * SE:+.3f}"] = round(r[cle] / 400, 3)
texte = json.dumps(out, indent=1, ensure_ascii=False)
print(texte)
open(sys.argv[2], "w", encoding="utf-8").write(texte + "\n")
