"""Applique à la consigne v8 la correction du tour 1 de sa contre-lecture (v8 → v9).

Couples « ancien → nouveau » : chaque « ancien » doit figurer exactement une fois dans la v8 ;
l'empreinte de la v8 et celle du rapport sont vérifiées ; la cible n'est jamais écrasée (R12).
Usage : python appliquer-corrections-consigne-lecteur-issue-pilote-v14-v9.py HEURE_UTC
"""
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "consigne-lecteur-issue-pilote-v14-v8.md"
CIBLE = ICI / "consigne-lecteur-issue-pilote-v14-v9.md"
RAPPORT = ICI / "contre-lecture-consigne-lecteur-issue-pilote-v14-v8-tour1-v1.md"
EMPREINTE_SOURCE = "821153e2f959834c97192d4d0cf8ccac2548f7883d66c60dbcac15d575f667bb"
EMPREINTE_RAPPORT = "9734258f04c513eca0d0549bed2eb9d797dd946f70e626dd17e3f2f5fb85ae50"


def empreinte(chemin):
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def couples(heure):
    return [
        # En-tête : titre et version.
        (
            "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v8\n",
            "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v9\n",
        ),
        (
            "Version 8, 2026-11-16T15:43:30Z (`date -u`, lue juste avant l'écriture et le scellement) : un premier lecteur s'est arrêté au point 0 de la v7 sur un critère que la consigne ajoutait à la « Liste d'arrêt » du texte scellé (`appels_complets_illisibles` à 0) ; le texte fait foi, et le lecteur en applique la « Liste d'arrêt » et rien d'autre : les arrêts du point 0 absents de cette liste deviennent des contrôles rapportés (sous-section « Version 8 », en fin de pièce) ; rédacteur : un rédacteur neuf (modèle A), qui n'a écrit ni le texte scellé ni le code ; la v7 (`b9706280…`),",
            f"Version 9, {heure} (`date -u`, lue juste avant l'écriture et le scellement) : correction du tour 1 de la contre-lecture de la v8 appliquée (la part de la machine, absente de la « Liste d'arrêt », devient un contrôle rapporté ; section « Contre-lecture », sous-section « Tour 1 de la v8 », en fin de pièce) ; rédacteur des corrections : un rédacteur neuf (modèle C), qui n'a écrit ni la consigne, ni le texte scellé, ni le code ; la v8 (`821153e2…`), la v7 (`b9706280…`),",
        ),
        # C1, couple 1 (point 0).
        (
            "la machine, de même, strictement sous 3 USD)",
            "la machine, elle, rapportée contre ses 3 USD sans arrêt : elle n'est pas un fournisseur de la « Liste d'arrêt » ; un dépassement est écrit au rapport comme nœud de Lazar)",
        ),
        # C1, couple 2 (sous-section « Version 8 »).
        (
            "aucune part atteinte, machine comprise",
            "aucune part de fournisseur atteinte",
        ),
        # C1, couple 3 (sous-section « Version 8 »).
        (
            "(part de 3 USD de la ligne π2 du bloc gelé). La règle",
            "(la machine, 3 USD de la ligne π2 du bloc gelé, est rapportée sans arrêt). La règle",
        ),
        # C1, couple 4 (point 4).
        (
            "la machine contre 3 USD, comprise dans les 21,72 USD de π2)",
            "la machine contre 3 USD, comprise dans les 21,72 USD de π2, rapportée sans arrêt)",
        ),
        # Sous-section du tour 1 de la v8, ajoutée en fin de pièce.
        (
            "- **À faire avant la remise** : contre-lecture de la v8 par un sous-agent neuf (R2).\n",
            "- **À faire avant la remise** : contre-lecture de la v8 par un sous-agent neuf (R2).\n" + TOUR1_V8,
        ),
    ]


TOUR1_V8 = """
### Tour 1 de la v8

- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-v8-tour1-v1.md` (même dossier), empreinte
  `9734258f04c513eca0d0549bed2eb9d797dd946f70e626dd17e3f2f5fb85ae50` (égale à son compagnon) ; verdict « corrections » (une
  mineure exigée, deux remarques facultatives) ; pièce lue : la v8, `821153e2f959834c97192d4d0cf8ccac2548f7883d66c60dbcac15d575f667bb`.
- **Application** : par un rédacteur neuf des corrections (modèle C), qui n'a écrit ni la consigne, ni le texte scellé, ni le code,
  par le programme `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v9.py` (même dossier) : empreintes de la v8 et du
  rapport vérifiées, chaque « ancien » présent une seule fois, cible jamais écrasée. Aucune pièce de la sortie du pilote ouverte,
  ni le verdict du premier lecteur. Relus pour juger : la « Liste d'arrêt » du texte scellé (`8aa33014…`, branche
  `prep/pilote-mr2-compte-organisme-v1`, empreinte recalculée égale) : « Dépense d'un fournisseur atteignant sa part → arrêt »,
  et « fournisseur » n'y désigne que les fournisseurs des proposeurs et de leurs relais ; la ligne π2 du bloc gelé (parts
  `argon` 9,36, `astra` 9,36, machine 3,0) ; `depense_pilote_v14_v1.py` au commit `2f7acc1d` de `lot/compte-organisme-v1`
  (`MACHINE = 3.0` ; code 3 si `machine.sous_la_part` est faux, code du programme de dépense, non un arrêt du pilote).
- **Réponse point par point** :
  - C1 (part de la machine hors de la « Liste d'arrêt », quatre couples : point 0, deux dans la sous-section « Version 8 »,
    point 4) : appliquée mot pour mot.
  - Remarques facultatives R1 (règle « non fait = arrêt », extension assumée, à signaler à la mère) et R2 (« compte » du point 0) :
    non appliquées (non exigées).
- **À faire avant la remise** : contre-lecture de la v9 par un sous-agent neuf (R2).
"""


def main():
    if len(sys.argv) != 2:
        sys.exit("usage : HEURE_UTC")
    if CIBLE.exists():
        sys.exit(f"refus : {CIBLE.name} existe déjà")
    if empreinte(SOURCE) != EMPREINTE_SOURCE:
        sys.exit("refus : empreinte de la v8 inattendue")
    if empreinte(RAPPORT) != EMPREINTE_RAPPORT:
        sys.exit("refus : empreinte du rapport inattendue")
    texte = SOURCE.read_text(encoding="utf-8")
    for ancien, nouveau in couples(sys.argv[1]):
        n = texte.count(ancien)
        if n != 1:
            sys.exit(f"refus : « {ancien[:60]}… » figure {n} fois")
        texte = texte.replace(ancien, nouveau)
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(f"écrit : {CIBLE.name} {empreinte(CIBLE)}")


if __name__ == "__main__":
    main()
