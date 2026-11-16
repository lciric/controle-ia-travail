#!/usr/bin/env python3
"""Applique à la consigne v4 la correction du tour 2 de la contre-lecture de la v3 (m1) et écrit la v5.

Usage : python appliquer-corrections-consigne-lecteur-issue-pilote-v14-v5.py HEURE_UTC
(HEURE_UTC : sortie de `date -u +%Y-%m-%dT%H:%M:%SZ`, lue juste avant l'écriture et le scellement).

Vérifie l'empreinte de la v4 et du rapport, que chaque « ancien » figure exactement une fois,
et refuse d'écraser la cible (ouverture en mode « x »).
"""
import hashlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v4.md")
SOURCE_SHA256 = "de826db5953ec86123ffca204c5b0c488098043298d5b15bc39563025781f8e4"
RAPPORT = os.path.join(ICI, "contre-lecture-consigne-lecteur-issue-pilote-v14-v3-tour2-v1.md")
RAPPORT_SHA256 = "98332a7459f6d0ada90441fc57d07b76d3a5051c579de356aa58a556fea177c2"
CIBLE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v5.md")


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def couples(heure):
    return [
        # en-tête : titre
        ("# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v4\n",
         "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v5\n"),
        # en-tête : version
        ("Version 4, 2026-11-16T14:33:58Z (`date -u`, lue juste avant l'écriture et le scellement) : corrections du tour 1 de la "
         "contre-lecture de la v3 appliquées (section « Contre-lecture », en fin de pièce) ; la v3 (`f06f46b3…`), la v2 (`0e12acbd…`) "
         "et la v1 (`5189c442…`) restent intactes dans ce dossier.",
         f"Version 5, {heure} (`date -u`, lue juste avant l'écriture et le scellement) : correction du tour 2 de la contre-lecture "
         "de la v3 appliquée (section « Contre-lecture », en fin de pièce) ; la v4 (`de826db5…`), la v3 (`f06f46b3…`), la v2 "
         "(`0e12acbd…`) et la v1 (`5189c442…`) restent intactes dans ce dossier."),
        # m1 (puce « Application » du tour 1 de la v3), adaptée : aucune lettre de modèle affirmée sans confirmation de la mère
        ("par un rédacteur neuf (modèle C), qui n'a écrit ni la consigne",
         "par un rédacteur neuf (modèle à confirmer par la mère : « modèle C » écrit ici par ce rédacteur, « modèle A » selon le "
         "contre-lecteur du tour 2 de la v3), qui n'a écrit ni la consigne"),
        # section « Contre-lecture » : sous-section du tour 2 de la v3, ajoutée après la dernière puce du tour 1 de la v3
        ("    est laissée telle quelle, comme au tour 2 : elle relève des points pour la mère.\n",
         "    est laissée telle quelle, comme au tour 2 : elle relève des points pour la mère.\n"
         "\n"
         "### Tour 2 de la v3\n"
         "\n"
         "- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-v3-tour2-v1.md` (même dossier), empreinte\n"
         f"  `{RAPPORT_SHA256}` (égale à son compagnon) ; verdict « corrections » (aucune\n"
         "  majeure, une mineure) ; pièce lue : la v4, `de826db5953ec86123ffca204c5b0c488098043298d5b15bc39563025781f8e4`.\n"
         "- **Application** : par un rédacteur neuf (modèle à confirmer par la mère : sa tâche le dit « modèle C » et dit aussi que\n"
         "  les corrections sont écrites par le modèle A), qui n'a écrit ni la consigne, ni le texte scellé, ni le code, par le programme\n"
         "  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v5.py` (même dossier) : empreintes de la v4 et du rapport vérifiées,\n"
         "  chaque « ancien » présent une seule fois, cible jamais écrasée. `diff` v3 → v4 relu : les trois corrections du tour 1 de la v3\n"
         "  et la sous-section « Tour 1 de la v3 » y sont appliquées fidèlement, rien d'autre. Noms des pièces citées revérifiés présents\n"
         "  dans la copie de sortie (noms et tailles seulement, aucune pièce de la copie ouverte).\n"
         "- **Réponse point par point** :\n"
         "  - m1 (puce « Application » du tour 1 de la v3, modèle du rédacteur) : appliquée **avec une adaptation**. Ni « modèle A »\n"
         "    (couple du rapport, qui tombe si la mère confirme C) ni la variante « le rédacteur des corrections (modèle A) » (si la mère\n"
         "    confirme A) ne sont écrits : la mère n'a confirmé ni l'un ni l'autre, et la tâche de ce rédacteur ne tranche pas (elle le\n"
         "    dit « modèle C » et dit que les corrections sont écrites par le modèle A). La lettre « modèle C » n'est donc plus affirmée\n"
         "    seule : la puce dit les deux lectures et renvoie à la mère (point 1 du rapport). Le reste de la puce est inchangé.\n"
         "  - Remarques facultatives F1 à F3 : non appliquées (non exigées).\n"),
    ]


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", sys.argv[1]):
        sys.exit("usage : appliquer-corrections-consigne-lecteur-issue-pilote-v14-v5.py AAAA-MM-JJTHH:MM:SSZ")
    if sha256(SOURCE) != SOURCE_SHA256:
        sys.exit(f"empreinte de la v4 inattendue : {sha256(SOURCE)}")
    if sha256(RAPPORT) != RAPPORT_SHA256:
        sys.exit(f"empreinte du rapport inattendue : {sha256(RAPPORT)}")
    if os.path.exists(CIBLE):
        sys.exit(f"cible déjà présente, jamais écrasée : {CIBLE}")
    with open(SOURCE, encoding="utf-8") as f:
        texte = f.read()
    for i, (ancien, nouveau) in enumerate(couples(sys.argv[1]), 1):
        n = texte.count(ancien)
        if n != 1:
            sys.exit(f"couple {i} : « ancien » présent {n} fois (1 attendu)")
        texte = texte.replace(ancien, nouveau, 1)
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(f"écrit : {CIBLE}")


if __name__ == "__main__":
    main()
