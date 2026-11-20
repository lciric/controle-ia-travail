#!/usr/bin/env python3
"""Contre-lecture du différentiel v8 -> v9 du palier 0b : T1 à T9 du contrôle de la v8 (§ 5) contre le JSON, à l'octet.

Usage : python3 -B verifier_t1_t9_v1.py CONTROLE_V8 JSON V8 V9

Règle d'extraction (contrôle de la v8, § 5, sous T1) : chaque texte est la ligne entière qui suit « - Ancien : » ou
« - Neuf : », hors des accents graves de bord quand il y en a. Bibliothèque standard seulement ; aucune graine, aucun tirage.
Contre-lecteur, modèle O.
"""
import json
import re
import sys


def extraire(chemin):
    t, courant = {}, None
    for ligne in open(chemin, encoding="utf-8").read().split("\n"):
        if ligne.startswith("## "):
            courant = None
            continue
        m = re.match(r"^\*\*(T[1-9]) ", ligne)
        if m:
            courant = m.group(1)
            t[courant] = {}
            continue
        if courant is None:
            continue
        for cle, prefixe in (("ancien", "- Ancien : "), ("neuf", "- Neuf : ")):
            if ligne.startswith(prefixe):
                s = ligne[len(prefixe):]
                if len(s) >= 2 and s.startswith("`") and s.endswith("`"):
                    s = s[1:-1]
                t[courant][cle] = s
    return t


def main(argv):
    controle, chemin_json, chemin_v8, chemin_v9 = argv
    t = extraire(controle)
    js = json.load(open(chemin_json, encoding="utf-8"))
    v8 = open(chemin_v8, encoding="utf-8").read()
    v9 = open(chemin_v9, encoding="utf-8").read()
    print(f"textes T extraits : {len(t)} ; remplacements du JSON : {len(js)}")
    pris = set()
    ok = True
    for k in sorted(t):
        a, n = t[k].get("ancien"), t[k].get("neuf")
        if a is None or n is None:
            print(f"{k} : ancien ou neuf manquant")
            ok = False
            continue
        rangs = [i + 1 for i, r in enumerate(js) if r["ancien"] == a and r["neuf"] == n]
        pris.update(rangs)
        bon = len(rangs) == 1 and v8.count(a) == 1 and v9.count(n) == 1
        ok = ok and bon
        print(f"{k} : rang(s) du JSON égaux à l'octet {rangs} ; ancien dans v8 {v8.count(a)} fois ; neuf dans v9 "
              f"{v9.count(n)} fois ; octets ancien {len(a.encode('utf-8'))}, neuf {len(n.encode('utf-8'))} ; "
              f"{'OK' if bon else 'ÉCART'}")
    autres = [i + 1 for i in range(len(js)) if i + 1 not in pris]
    print(f"rangs du JSON qui ne sont pas T1 à T9 : {autres} ({len(autres)})")
    print("VERDICT : " + ("T1 à T9 à l'octet" if ok and len(t) == 9 else "ÉCART"))
    return 0 if ok and len(t) == 9 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
