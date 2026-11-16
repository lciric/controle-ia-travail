#!/usr/bin/env python3
"""Applique à la consigne v3 les corrections du tour 1 de sa contre-lecture (m1, m2, m3) et écrit la v4.

Usage : python appliquer-corrections-consigne-lecteur-issue-pilote-v14-v4.py HEURE_UTC
(HEURE_UTC : sortie de `date -u +%Y-%m-%dT%H:%M:%SZ`, lue juste avant l'écriture et le scellement).

Vérifie l'empreinte de la v3 et du rapport, que chaque « ancien » figure exactement une fois,
et refuse d'écraser la cible (ouverture en mode « x »).
"""
import hashlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v3.md")
SOURCE_SHA256 = "f06f46b31944f88b62ea2de08b8b95d06ce92fd906b52e2856c10479942034c8"
RAPPORT = os.path.join(ICI, "contre-lecture-consigne-lecteur-issue-pilote-v14-v3-tour1-v1.md")
RAPPORT_SHA256 = "27269e9275f2fb094c5e4b4f88e182974d96a1bb49f3485426af94797253af4c"
CIBLE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v4.md")


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def couples(heure):
    return [
        # en-tête : titre
        ("# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v3\n",
         "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v4\n"),
        # en-tête : version
        ("Version 3, 2026-11-16T14:17:29Z (`date -u`, à l'écriture, avant le scellement) : corrections du tour 2 de sa contre-lecture "
         "appliquées (section « Contre-lecture », en fin de pièce) ; la v2 (`0e12acbd…`) et la v1 (`5189c442…`) restent intactes dans ce dossier.",
         f"Version 4, {heure} (`date -u`, lue juste avant l'écriture et le scellement) : corrections du tour 1 de la contre-lecture de la v3 "
         "appliquées (section « Contre-lecture », en fin de pièce) ; la v3 (`f06f46b3…`), la v2 (`0e12acbd…`) et la v1 (`5189c442…`) "
         "restent intactes dans ce dossier."),
        # m1 (point 6)
        ("les taux d'erreur du texte (section « Prédiction chiffrée et signe attendu » : course refusée",
         "tous les taux d'erreur du texte (section « Prédiction chiffrée et signe attendu », dont : course refusée"),
        # m2 (point 0)
        ("aucun appel au-dessus de son pire cas, aucune part atteinte. Tout",
         "aucun appel au-dessus de son pire cas (`journal_au_dessus_du_pire_cas` à 0 pour chaque proposeur) et aucune part atteinte "
         "(le coût du relevé et celui des journaux de chaque proposeur strictement inférieurs à sa part, même si `sous_la_part` est vrai ; "
         "la machine, de même, strictement sous 3 USD). Tout"),
        # m3 (point 7)
        ("sans `numpy` (version 1.25 au moins), le tirage est écrit « non fait », avec sa cause),",
         "sans `numpy` (version 1.25 au moins), le tirage est écrit « non fait », avec sa cause ; la version de `numpy` employée et, "
         "pour chaque appel, les indices tirés sont écrits au rapport, pour que la mère puisse rejouer le tirage),"),
        # section « Contre-lecture » : sous-section du tour 1 de la v3, ajoutée après la dernière puce du tour 2
        ("  - Remarques facultatives F1 à F5 : non appliquées (non exigées).\n",
         "  - Remarques facultatives F1 à F5 : non appliquées (non exigées).\n"
         "\n"
         "### Tour 1 de la v3\n"
         "\n"
         "- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-v3-tour1-v1.md` (même dossier), empreinte\n"
         f"  `{RAPPORT_SHA256}` (égale à son compagnon) ; verdict « corrections » (aucune\n"
         "  majeure, trois mineures) ; pièce lue : la v3, `f06f46b31944f88b62ea2de08b8b95d06ce92fd906b52e2856c10479942034c8`.\n"
         "- **Application** : par un rédacteur neuf (modèle C), qui n'a écrit ni la consigne, ni le texte scellé, ni le code, par le programme\n"
         "  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v4.py` (même dossier) : empreintes de la v3 et du rapport vérifiées,\n"
         "  chaque « ancien » présent une seule fois, cible jamais écrasée. `diff` v2 → v3 relu : les corrections du tour 2 y sont appliquées\n"
         "  fidèlement, avec les adaptations déclarées. Noms des pièces citées revérifiés présents dans la copie de sortie (noms et tailles\n"
         "  seulement, aucune pièce de la copie ouverte). Champs `journal_au_dessus_du_pire_cas`, `sous_la_part` (comparaison `≤` à la part)\n"
         "  et `MACHINE = 3.0` relus sur `depense_pilote_v14_v1.py` (`9866e611…`) ; « Dépense d'un fournisseur atteignant sa part → arrêt »\n"
         "  et la version de `numpy` du bloc gelé relues dans le texte scellé (`8aa33014…`).\n"
         "- **Réponse point par point** :\n"
         "  - m1 (point 6, liste de taux non exhaustive) : appliquée mot pour mot.\n"
         "  - m2 (point 0, champs du pire cas et part atteinte au sens strict) : appliquée mot pour mot.\n"
         "  - m3 (point 7, version de `numpy` et indices tirés écrits au rapport) : appliquée mot pour mot.\n"
         "  - Remarques facultatives F1 à F3 : non appliquées (non exigées) ; F3 (mention « modèle C » de la puce « Application » du tour 1)\n"
         "    est laissée telle quelle, comme au tour 2 : elle relève des points pour la mère.\n"),
    ]


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", sys.argv[1]):
        sys.exit("usage : appliquer-corrections-consigne-lecteur-issue-pilote-v14-v4.py AAAA-MM-JJTHH:MM:SSZ")
    if sha256(SOURCE) != SOURCE_SHA256:
        sys.exit(f"empreinte de la v3 inattendue : {sha256(SOURCE)}")
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
