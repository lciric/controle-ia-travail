#!/usr/bin/env python3
"""Applique à la consigne v5 la correction du tour 3 de la contre-lecture de la v3 (m1, trois couples) et les décisions de la
mère (R-2992 et tâche de la mère : rédacteur de la v3 → v4 du modèle A ; pièce de dépense du point 4 ; sommet final de la branche
de sortie ; ce que le lecteur rend aux cribles), et écrit la v6.

Usage : python appliquer-corrections-consigne-lecteur-issue-pilote-v14-v6.py HEURE_UTC
(HEURE_UTC : sortie de `date -u +%Y-%m-%dT%H:%M:%SZ`, lue juste avant l'écriture et le scellement).

Vérifie l'empreinte de la v5 et du rapport, que chaque « ancien » figure exactement une fois,
et refuse d'écraser la cible (ouverture en mode « x »).
"""
import hashlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v5.md")
SOURCE_SHA256 = "05f4f32598e62aaad4cd81f5697c5d0a3eaea43eeb39e387208cbc2fe28e6fbd"
RAPPORT = os.path.join(ICI, "contre-lecture-consigne-lecteur-issue-pilote-v14-v3-tour3-v1.md")
RAPPORT_SHA256 = "d0019ab6291256ee96bcd21f1e894448b42a768cdd828769cd7e52ed19790bb8"
CIBLE = os.path.join(ICI, "consigne-lecteur-issue-pilote-v14-v6.md")


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


TOUR3 = (
    "\n"
    "### Tour 3 de la v3\n"
    "\n"
    "- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-v3-tour3-v1.md` (même dossier), empreinte\n"
    "  `d0019ab6291256ee96bcd21f1e894448b42a768cdd828769cd7e52ed19790bb8` (égale à son compagnon) ; verdict « corrections » (aucune\n"
    "  majeure, une mineure) ; pièce lue : la v5, `05f4f32598e62aaad4cd81f5697c5d0a3eaea43eeb39e387208cbc2fe28e6fbd`.\n"
    "- **Application** : par le rédacteur des corrections (modèle A), qui n'a pas écrit le texte scellé ni le code, par le programme\n"
    "  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v6.py` (même dossier) : empreintes de la v5 et du rapport vérifiées,\n"
    "  chaque « ancien » présent une seule fois, cible jamais écrasée. Noms des pièces citées revérifiés présents dans la copie de\n"
    "  sortie (noms et tailles seulement, aucune pièce de la copie ouverte). Pièce de dépense relue sur le commit `2f7acc1d` de\n"
    "  `lot/compte-organisme-v1` : empreinte recalculée égale à `53c72308…` et à son compagnon ; seuls les noms de ses clés lus\n"
    "  (`machine`, `autres`, `proposeurs`, `pi1_sous_la_ligne`, `pi2_sous_la_ligne`…), aucune valeur. Champs `corps.appels`\n"
    "  (`repondu`, `sans_carte`, `tronque`, `echec`) et `corps.temoin_positif` relus sur `mesure_pilote_v4.py` (`676d5f37…`) :\n"
    "  `temoin_positif` n'existe pas quand l'issue est P-0 ; `duree_s` des appels du relevé, `debut_utc` et `fin_utc` du manifeste\n"
    "  relus sur les pièces de la répétition locale du commit `2d35cafa`, non sur les pièces réelles.\n"
    "- **Réponse point par point** :\n"
    "  - m1 (provenance du rédacteur, deux puces « Application » et la réponse m1 du tour 2 de la v3) : appliquée mot pour mot,\n"
    "    trois couples. La mère a confirmé que la passe v3 → v4 a été appliquée par un rédacteur du modèle A (vérifié dans les\n"
    "    journaux, R-2992, points 0 et 4) : le couple 1 vaut donc tel quel, et « n'a écrit ni la consigne », faux pour le modèle A,\n"
    "    auteur de la consigne, est retiré des deux puces.\n"
    "  - Décisions de la mère portées dans le corps, en plus du rapport (point 3 des « Points pour la mère » de ce rapport et des\n"
    "    précédents) : (a) pièces, point 4 : la sortie du programme de dépense est nommée, `depense-pilote-v14-v1.json`\n"
    "    (`53c72308…`, commit `2f7acc1d` de `lot/compte-organisme-v1`), déjà produite et scellée par le compte organisme (R-2983) ;\n"
    "    les arguments `--machine` et `--autre` y sont recopiés (champs `machine` et `autres`), d'où « avec lesquels il a été joué » ;\n"
    "    (b) pièces, point 2 : sommet final de la branche de sortie `69275b74` (R-2981) ; (c) « Ce qu'il rend » : section « Pour les\n"
    "    cribles » (comptes d'appels répondus, tronqués et en échec, durées, coûts, seul champ du témoin positif). Pour (c), deux\n"
    "    précisions de ce rédacteur, sans rien ajouter à la liste de la mère : où se lit chaque chose (noms de champs ci-dessus), et\n"
    "    que faire si un champ manque (P-0) ou si un arrêt interdit de lire la sortie de mesure, pour que la section ne contredise\n"
    "    pas le point 0.\n"
    "  - Remarques facultatives F1 à F3 : non appliquées (non exigées).\n"
    "  - Non touchée : la puce « Application » du tour 1 (« rédacteur neuf (modèle C) »), que ni ce rapport ni les décisions\n"
    "    transmises ne nomment ; R-2992 (point 0) dit fausses les mentions « lettre C » des rédacteurs lancés au modèle A : à la\n"
    "    mère de dire si celle-ci en est une.\n"
)


def couples(heure):
    return [
        # en-tête : titre
        ("# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v5\n",
         "# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v6\n"),
        # en-tête : version
        ("Version 5, 2026-11-16T14:38:53Z (`date -u`, lue juste avant l'écriture et le scellement) : correction du tour 2 de la "
         "contre-lecture de la v3 appliquée (section « Contre-lecture », en fin de pièce) ; la v4 (`de826db5…`), la v3 (`f06f46b3…`), "
         "la v2 (`0e12acbd…`) et la v1 (`5189c442…`) restent intactes dans ce dossier.",
         f"Version 6, {heure} (`date -u`, lue juste avant l'écriture et le scellement) : correction du tour 3 de la contre-lecture "
         "de la v3 et décisions de la mère (R-2992) appliquées (section « Contre-lecture », en fin de pièce) ; la v5 (`05f4f325…`), "
         "la v4 (`de826db5…`), la v3 (`f06f46b3…`), la v2 (`0e12acbd…`) et la v1 (`5189c442…`) restent intactes dans ce dossier."),
        # décision de la mère : sommet final de la branche de sortie (R-2981)
        ("à son sommet\n   final (`etape=fini` dans `etat.txt`) ;",
         "à son sommet\n   final `69275b74` (`etape=fini` dans `etat.txt` ; R-2981) ;"),
        # décision de la mère : pièce de dépense du point 4, déjà produite et scellée par le compte organisme
        ("Le lecteur reçoit sa **sortie JSON scellée** (nom donné par la mère) et les arguments `--machine` (prix horaire, heures de "
         "création et de destruction) et `--autre` tels que la mère les a donnés ; il les rapporte sans pouvoir les vérifier.",
         "Le lecteur reçoit sa **sortie JSON scellée**, déjà produite et scellée par le compte organisme : "
         "`docs/notes/organisme-multi-generations-v1/pilote-v1/lecture-depense-pilote-v14-compte-organisme/depense-pilote-v14-v1.json` "
         "(`53c72308bb30adcce5602ad18b47f2e7325a22a295264c143ed52ff46f349ce2`, avec son compagnon, commit `2f7acc1d` de "
         "`lot/compte-organisme-v1`) ; les arguments `--machine` (prix horaire, heures de création et de destruction) et `--autre` "
         "avec lesquels il a été joué y sont recopiés (champs `machine` et `autres`) ; il les rapporte sans pouvoir les vérifier."),
        # décision de la mère : ce que le lecteur rend aux cribles (renvoi dans la liste du verdict)
        ("audit R4 (déclenché ou non, fait ou non fait), les phrases du point 6, nœuds de Lazar appelés. Le verdict",
         "audit R4 (déclenché ou non, fait ou non fait), les phrases du point 6, nœuds de Lazar appelés, la section « Pour les "
         "cribles » ci-dessous. Le verdict"),
        # décision de la mère : ce que le lecteur rend aux cribles (paragraphe)
        ("ne recopie aucune réponse\nbrute.\n\n## Contre-lecture\n",
         "ne recopie aucune réponse\nbrute.\n\n"
         "**Pour les cribles** (décision de la mère, R-2992 : devis des cribles refaits d'après le coût réel du pilote) : une section à "
         "part du verdict, intitulée « Pour les cribles », qui porte seulement les comptes d'appels répondus, tronqués et en échec "
         "(`repondu`, `tronque` et `echec` de `corps.appels` de la sortie de mesure), les durées (`duree_s` de chaque appel du relevé ; "
         "`debut_utc` et `fin_utc` du manifeste), les coûts (la dépense rapprochée du point 4) et le seul champ "
         "`corps.temoin_positif` de la sortie de mesure, recopié tel quel (écrit « absent » si l'issue est P-0 : la sortie ne le "
         "calcule pas) ; rien d'autre de la sortie de mesure ni de la lecture. Après un arrêt aux points 0 à 2, la sortie de mesure "
         "n'est pas lue au-delà de ce que permet le point 0 : la section ne porte que les durées et les coûts, le reste écrit "
         "« non lu (arrêt) ».\n\n"
         "## Contre-lecture\n"),
        # m1, couple 1 (puce « Application » du tour 1 de la v3)
        ("par un rédacteur neuf (modèle à confirmer par la mère : « modèle C » écrit ici par ce rédacteur, « modèle A » selon le "
         "contre-lecteur du tour 2 de la v3), qui n'a écrit ni la consigne, ni le texte scellé, ni le code, par le programme",
         "par le rédacteur des corrections (modèle A), qui n'a pas écrit le texte scellé ni le code, par le programme"),
        # m1, couple 2 (puce « Application » du tour 2 de la v3, deux lignes devenues une)
        ("- **Application** : par un rédacteur neuf (modèle à confirmer par la mère : sa tâche le dit « modèle C » et dit aussi que\n"
         "  les corrections sont écrites par le modèle A), qui n'a écrit ni la consigne, ni le texte scellé, ni le code, par le programme",
         "- **Application** : par le rédacteur des corrections (modèle A), qui n'a pas écrit le texte scellé ni le code, par le programme"),
        # m1, couple 3 (réponse m1 du tour 2 de la v3, cinq lignes) ; sous-section du tour 3 ajoutée en fin de pièce
        ("  - m1 (puce « Application » du tour 1 de la v3, modèle du rédacteur) : appliquée **avec une adaptation**. Ni « modèle A »\n"
         "    (couple du rapport, qui tombe si la mère confirme C) ni la variante « le rédacteur des corrections (modèle A) » (si la mère\n"
         "    confirme A) ne sont écrits : la mère n'a confirmé ni l'un ni l'autre, et la tâche de ce rédacteur ne tranche pas (elle le\n"
         "    dit « modèle C » et dit que les corrections sont écrites par le modèle A). La lettre « modèle C » n'est donc plus affirmée\n"
         "    seule : la puce dit les deux lectures et renvoie à la mère (point 1 du rapport). Le reste de la puce est inchangé.\n"
         "  - Remarques facultatives F1 à F3 : non appliquées (non exigées).\n",
         "  - m1 (puce « Application » du tour 1 de la v3, modèle du rédacteur) : appliquée avec la variante du rapport (« le rédacteur "
         "des corrections (modèle A) »), la mère ayant confirmé que les corrections sont écrites par le modèle A ; le reste de la puce "
         "est inchangé.\n"
         "  - Remarques facultatives F1 à F3 : non appliquées (non exigées).\n" + TOUR3),
    ]


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", sys.argv[1]):
        sys.exit("usage : appliquer-corrections-consigne-lecteur-issue-pilote-v14-v6.py AAAA-MM-JJTHH:MM:SSZ")
    if sha256(SOURCE) != SOURCE_SHA256:
        sys.exit(f"empreinte de la v5 inattendue : {sha256(SOURCE)}")
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
