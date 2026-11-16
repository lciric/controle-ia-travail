#!/usr/bin/env python3
"""Applique à procedure-machine-jeu-idee-1-1-v3.md les corrections du tour 2 qui portent sur cette pièce (v4 neuve).

Usage : python3 -I corriger_procedure_v3_vers_v4_tour2_v1.py SOURCE CIBLE HEURE_UTC
- SOURCE : la procédure v3, dont l'empreinte doit être EMPREINTE_SOURCE ;
- CIBLE : la procédure v4, fichier neuf (jamais écrasé, R12) ;
- HEURE_UTC : `date -u +%FT%TZ` au moment du scellement.
Rapport appliqué : contre-lecture-machine-jeu-idee-1-1-tour2-v1.md (empreinte EMPREINTE_RAPPORT, vérifiée si le fichier
est à côté de la source). Couples appliqués : m1', m2', m3' ; en tête (titre, statut, version) ; section « Contre-lecture ».
Non appliqués (motifs au § 6 de la v4) : M1' points 1 à 3 (autres pièces) et point 4 (pièces neuves encore absentes).
Chaque « ancien » doit figurer exactement une fois dans la source et au moment de son couple.
"""
import hashlib
import os
import re
import sys

EMPREINTE_SOURCE = "e91a9020cf35e320af99ccbd61ac37fdf591854a895b7efbc15f66070a98465c"
EMPREINTE_RAPPORT = "c977ac7e7f5640dd76ad957febe8cdfdc5a7e1bf3077abbacb13dc183e264de7"
NOM_RAPPORT = "contre-lecture-machine-jeu-idee-1-1-tour2-v1.md"

COUPLES = [
    ("titre",
     "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v3",
     "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v4"),
    ("statut",
     "contre-lue au tour 1 (`contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`), corrections de ce tour en v3 ;",
     "contre-lue aux tours 1 (`contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`) et 2\n"
     "  (`contre-lecture-machine-jeu-idee-1-1-tour2-v1.md`), corrections du tour 1 en v3, corrections du tour 2 qui portent sur\n"
     "  cette pièce en v4 ; ne part pas au feu sans l'amorce v2, le devis v2, le rapport v2, la version suivante de cette\n"
     "  procédure qui les nomme et un tour 3 rendu `scellable` (§ 6) ;"),
    ("version",
     "- **Version** : v3, scellée à 2026-11-16T21:42:18Z (`date -u`) ; suit la v1 (`0d674c39…`) ; changements : corrections de la\n"
     "  contre-lecture du tour 1 (§ 6). La v2 (`ce23095a…`, même dossier, même rédacteur) citait au § 6 une tête de `main`\n"
     "  périmée au moment de son scellement ; seul ce fait et la numérotation changent de la v2 à la v3.",
     "- **Version** : v4, scellée à {HEURE} (`date -u`) ; suit la v3 (`e91a9020…`) ; changements de la v3 à la v4 : corrections\n"
     "  de la contre-lecture du tour 2 qui portent sur cette pièce (§ 6). La v3 suivait la v1 (`0d674c39…`) par les corrections\n"
     "  du tour 1 ; la v2 (`ce23095a…`) citait au § 6 une tête de `main` périmée."),
    ("m1' (§ 2, point 1)",
     "ancêtre de la tête de `main` à 21:3xZ",
     "ancêtre de la tête de `main` lue à 21:47Z : `396c4a0c…`"),
    ("m2' (§ 2, point 3)",
     "Contre-lecture de cette procédure et du devis par un lecteur neuf (R2), corrections faites.",
     "Contre-lecture de cette procédure, de l'amorce et du devis par un lecteur neuf (R2), tour 3 rendu `scellable`."),
    ("m3' (geste 13)",
     "(§ 2, « Après le jeu ») : `git -C $R archive",
     "(§ 2, « Après le jeu ») : `test ! -e $R/runs/<run> && test ! -e $R/diag/organisme-idees-juge-v1/<run> && git -C $R archive"),
    ("§ 6, tour 1 (titre du bloc)",
     "## 6. Contre-lecture\n\n- **Rapport** : `contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`",
     "## 6. Contre-lecture\n\n**Tour 1** (corrections en v3) :\n\n- **Rapport** : `contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`"),
    ("§ 6, tour 1 (version v3)",
     "- **Cette version** : v3, écrite",
     "- **Version v3** : écrite"),
    ("§ 6, tour 1 (fin) et tour 2",
     "- **Rien d'autre ne change** par rapport à la v1 : en tête (titre, statut, version), les couples ci-dessus et cette section.\n",
     "- **Rien d'autre ne change** de la v1 à la v3 : en tête (titre, statut, version), les couples ci-dessus et cette section.\n"
     "\n"
     "**Tour 2** (corrections en v4) :\n"
     "\n"
     "- **Rapport** : `contre-lecture-machine-jeu-idee-1-1-tour2-v1.md` (même dossier), empreinte\n"
     "  `c977ac7e7f5640dd76ad957febe8cdfdc5a7e1bf3077abbacb13dc183e264de7`, lecteur neuf (R2) ; verdict `corrections` (une\n"
     "  majeure, M1', en quatre points ; trois mineures, m1' à m3' ; remarques facultatives).\n"
     "- **Cette version** : v4, écrite par un rédacteur neuf au moyen du programme de couples\n"
     "  `corriger_procedure_v3_vers_v4_tour2_v1.py` (même dossier), depuis la v3\n"
     "  `e91a9020cf35e320af99ccbd61ac37fdf591854a895b7efbc15f66070a98465c`.\n"
     "- **Réponse point par point** :\n"
     "  - **M1', points 1 à 3** (amorce v2 portant la reprise, avec ses deux cas de répétition ; devis v2 portant les couples 5,\n"
     "    11, 16 et 17 du tour 1 ; rapport v2 qui ne présente plus D7 comme ouvert) : hors de cette pièce, non appliqués ici ;\n"
     "    à livrer par l'auteur de ces pièces (fichiers neufs, R12). Fait relevé pour lui : le lanceur v1 nomme l'amorce par son\n"
     "    chemin (`AMORCE=\"$ICI/amorce_jeu_idee_1_1_v1.sh\"`) et `controle-ligne` cherche `/root/amorce_jeu_idee_1_1_v1.sh` dans\n"
     "    la ligne : une amorce v2 demande donc un lanceur v2.\n"
     "  - **M1', point 4** (couples qui nomment les pièces neuves) : **non appliqué, refus motivé**. Au scellement de cette\n"
     "    version, ni `amorce_jeu_idee_1_1_v2.sh`, ni `devis-machine-jeu-idee-1-1-v2.md`, ni `rapport-machine-jeu-idee-1-1-v2.md`,\n"
     "    ni une sortie de répétition de l'amorce v2 n'existent dans le dossier (vérifié sur disque) : les appliquer ferait nommer\n"
     "    à la liste des pièces et au geste 6 des fichiers absents ; le « nouveau » du deuxième couple (nom et nombre de cas de\n"
     "    cette sortie) n'est pas encore défini ; le cinquième se conditionne lui-même à la levée de la dépendance. La phrase\n"
     "    « Cette version ne part donc pas au feu avec l'amorce v1 » est donc gardée : elle vaut pour la v4. Ces couples\n"
     "    reviennent à la version suivante de cette procédure, écrite après les pièces neuves, puis au tour 3.\n"
     "  - **m1'** : appliqué (§ 2, point 1) ; fait recoupé en lecture seule : `14a0dfc5…` ancêtre de la référence locale\n"
     "    `origin/main` `396c4a0c…` (la tête bouge : `COMMIT` se relit au feu).\n"
     "  - **m2'** : appliqué (§ 2, point 3).\n"
     "  - **m3'** : appliqué (geste 13) : les deux `test ! -e` en tête de la commande de recopie.\n"
     "  - **Remarques facultatives** (F2 et F4 du tour 1 ; surcoût de la reprise au devis) : non appliquées, aucune n'est\n"
     "    exigée ; la seconde porte sur le devis.\n"
     "  - **Points pour la mère** : hors du texte de la procédure ; rien n'y change ici.\n"
     "- **Rien d'autre ne change** de la v3 à la v4 : en tête (titre, statut, version), les couples m1', m2', m3' et cette\n"
     "  section.\n"),
]


def main() -> int:
    if len(sys.argv) != 4:
        print("REFUS : usage SOURCE CIBLE HEURE_UTC")
        return 2
    source, cible, heure = sys.argv[1:]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        print("REFUS : heure illisible")
        return 2
    if os.path.exists(cible):
        print(f"REFUS : {cible} existe déjà (R12, jamais écrasé)")
        return 2
    rapport = os.path.join(os.path.dirname(os.path.abspath(source)), NOM_RAPPORT)
    if os.path.exists(rapport):
        er = hashlib.sha256(open(rapport, "rb").read()).hexdigest()
        if er != EMPREINTE_RAPPORT:
            print(f"REFUS : empreinte du rapport {er} ≠ {EMPREINTE_RAPPORT}")
            return 2
    brut = open(source, "rb").read()
    e = hashlib.sha256(brut).hexdigest()
    if e != EMPREINTE_SOURCE:
        print(f"REFUS : empreinte de la source {e} ≠ {EMPREINTE_SOURCE}")
        return 2
    texte = brut.decode("utf-8")
    for nom, ancien, _ in COUPLES:
        if texte.count(ancien) != 1:
            print(f"REFUS : {nom} : « ancien » trouvé {texte.count(ancien)} fois dans la source (1 exigée)")
            return 2
    for nom, ancien, nouveau in COUPLES:
        if texte.count(ancien) != 1:
            print(f"REFUS : {nom} : « ancien » trouvé {texte.count(ancien)} fois au moment de son couple")
            return 2
        texte = texte.replace(ancien, nouveau.replace("{HEURE}", heure), 1)
        print(f"appliqué : {nom}")
    try:
        with open(cible, "x", encoding="utf-8") as f:
            f.write(texte)
    except FileExistsError:
        print(f"REFUS : {cible} existe déjà (R12, jamais écrasé)")
        return 2
    print(f"écrit : {cible} ({len(COUPLES)} couples) ; sha256 {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
