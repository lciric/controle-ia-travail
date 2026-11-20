#!/usr/bin/env python3
"""Verifie que chaque correction du contre-lecteur figure mot pour mot dans le jeu du redacteur, et que
le texte de la contre-lecture 4 du § 8 du rapport est porte mot pour mot. N'ecrit rien.
Usage : python3 -B comparer_corrections_v5_v1.py MES_K1_K4.json MES_K5_K9.json SON_PREREG.json SON_DEVIS.json RAPPORT.md
"""
import json
import sys


def charger(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def main(a):
    if len(a) != 6:
        sys.stderr.write("usage : 5 chemins\n")
        return 2
    mes = [("prereg", x) for x in charger(a[1])] + [("devis", x) for x in charger(a[2])]
    siens = {"prereg": charger(a[3]), "devis": charger(a[4])}
    for i, (cible, k) in enumerate(mes, 1):
        print("K%d" % i, cible, "porte mot pour mot :", k in siens[cible])
    with open(a[5], encoding="utf-8") as f:
        rapport = f.read()
    debut = rapport.rindex("« - **Contre-lecture 4**") + 2  # la derniere : la premiere est l'ancre
    borne = "(à écrire par la mère). »"
    fin = rapport.index(borne, debut) + len(borne) - 2
    texte = rapport[debut:fin]
    neuf_cl4 = [x["neuf"] for x in siens["prereg"] if x["ancien"].startswith("- **Contre-lecture 4**")]
    print("contre-lecture 4 portee mot pour mot :", len(neuf_cl4) == 1 and neuf_cl4[0] == texte)
    autres = [x for x in siens["prereg"] if ("prereg", x) not in mes] + [x for x in siens["devis"] if ("devis", x) not in mes]
    print("remplacements hors K1 a K9 :", len(autres))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
