#!/usr/bin/env python3
"""Compare les paires « Ancien » / « Neuf » de mon contrôle aux JSON d'essai (cohérence de ma propre pièce).

Usage : python3 -B verifier_mes_textes_v1.py CONTROLE JSON1 [JSON2 ...]
Règle d'extraction : la ligne entière qui suit « Ancien : » ou « Neuf : », hors des accents graves de bord.
Contrôleur neuf, modèle O.
"""
import json
import re
import sys


def bord(t):
    if len(t) >= 2 and t[0] == "`" and t[-1] == "`":
        return t[1:-1]
    return t


def main():
    controle = sys.argv[1]
    motif = re.compile(r"^\s*- (Ancien|Neuf) : (.*)$")
    paires, courant = [], None
    for ligne in open(controle, encoding="utf-8").read().split("\n"):
        m = motif.match(ligne)
        if not m:
            continue
        if m.group(1) == "Ancien":
            courant = bord(m.group(2))
        else:
            paires.append((courant, bord(m.group(2))))
            courant = None
    entrees = []
    for js in sys.argv[2:]:
        entrees += [(r["ancien"], r["neuf"]) for r in json.load(open(js, encoding="utf-8"))]
    print(f"paires du contrôle : {len(paires)} ; entrées des JSON : {len(entrees)}")
    for i, p in enumerate(paires, 1):
        print(f"paire {i} : {'égale à une entrée' if p in entrees else 'ABSENTE DES JSON'} ; ancien {p[0][:40]!r}")
    for i, e in enumerate(entrees, 1):
        if e not in paires:
            print(f"entrée {i} des JSON absente du contrôle : {e[0][:40]!r}")


if __name__ == "__main__":
    main()
