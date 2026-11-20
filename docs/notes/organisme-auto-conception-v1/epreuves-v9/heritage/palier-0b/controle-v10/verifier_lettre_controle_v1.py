#!/usr/bin/env python3
"""Compare les textes « Ancien » / « Neuf » des § 8 et § 9 du contrôle de la v9 aux entrées du JSON v9 -> v10.

Usage : python3 -B verifier_lettre_controle_v1.py CONTROLE JSON V9 V10
Règle d'extraction (celle du contrôle) : la ligne entière qui suit « Ancien : » ou « Neuf : »,
hors des accents graves de bord quand il y en a (un de chaque côté).
Ne lit que les lignes qui suivent le titre « ## 8. » ; s'arrête au titre « ## 10. ».
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
    controle, js, v9, v10 = sys.argv[1:5]
    lignes = open(controle, encoding="utf-8").read().split("\n")
    dedans = False
    paires = []
    courant = None
    motif = re.compile(r"^\s*- (Ancien|Neuf) : (.*)$")
    for ligne in lignes:
        if ligne.startswith("## 8."):
            dedans = True
            continue
        if ligne.startswith("## 10."):
            break
        if not dedans:
            continue
        m = motif.match(ligne)
        if not m:
            continue
        texte = bord(m.group(2))
        if m.group(1) == "Ancien":
            courant = texte
        else:
            paires.append((courant, texte))
            courant = None
    remplacements = json.load(open(js, encoding="utf-8"))
    t9 = open(v9, encoding="utf-8").read()
    t10 = open(v10, encoding="utf-8").read()
    print(f"paires extraites : {len(paires)}")
    for i, (a, n) in enumerate(paires, 1):
        rangs = [k for k, r in enumerate(remplacements, 1) if r["ancien"] == a]
        egal = [k for k in rangs if remplacements[k - 1]["neuf"] == n]
        print(f"paire {i} : ancien {a[:50]!r}… | rang(s) ancien {rangs} | neuf égal à l'octet aux rangs {egal} | "
              f"ancien dans v9 {t9.count(a)} fois, dans v10 {t10.count(a)} fois | "
              f"neuf dans v9 {t9.count(n)} fois, dans v10 {t10.count(n)} fois")


if __name__ == "__main__":
    main()
