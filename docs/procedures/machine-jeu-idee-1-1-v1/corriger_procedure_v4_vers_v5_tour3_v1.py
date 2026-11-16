#!/usr/bin/env python3
"""Applique à procedure-machine-jeu-idee-1-1-v4.md les couples du tour 2 (point 4) et du tour 3 (M1'', m1'') : v5 neuve.

Usage : python3 -I corriger_procedure_v4_vers_v5_tour3_v1.py SOURCE CIBLE HEURE_UTC LONGUEUR_LIGNE OCTETS_COMMANDE
- SOURCE : la procédure v4, dont l'empreinte doit être EMPREINTE_SOURCE ;
- CIBLE : la procédure v5, fichier neuf (jamais écrasé, R12) ;
- HEURE_UTC : `date -u +%FT%TZ` au moment du scellement ;
- LONGUEUR_LIGNE, OCTETS_COMMANDE : longueur de la ligne de création et taille de la sortie de `commande`, relevées dans la
  répétition v2 dont la sortie est gardée (`sortie-repetition-machine-jeu-idee-1-1-v2.txt`, ligne « longueur de la ligne »).
Les empreintes des pièces v2 sont lues sur disque, à côté de la source, et doivent être égales à leurs compagnons.
Le nombre de cas de la répétition v2 est lu dans sa sortie gardée (« répétition : N cas, 0 écart(s) »), qui doit dire 0 écart.
Chaque « ancien » doit figurer exactement le nombre de fois indiqué (1 par défaut) au moment de son couple.
"""
import hashlib
import os
import re
import sys

EMPREINTE_SOURCE = "996c8a5cbe9d7cacba32124118dff30af8eb47ebf431a9c72925a7619687b24f"
NOM_TOUR3 = "contre-lecture-machine-jeu-idee-1-1-tour3-v1.md"
PIECES = ["lancer_jeu_idee_1_1_machine_v2.sh", "garde_machine_jeu_idee_1_1_v1.py", "amorce_jeu_idee_1_1_v2.sh",
          "repetition_machine_jeu_idee_1_1_v2.sh", "jeu_factice_idee_1_1_v1.py", "sortie-repetition-machine-jeu-idee-1-1-v2.txt",
          "devis-machine-jeu-idee-1-1-v2.md", "rapport-machine-jeu-idee-1-1-v2.md", NOM_TOUR3, "corriger_procedure_v4_vers_v5_tour3_v1.py"]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    if len(sys.argv) != 6:
        print(__doc__)
        return 2
    src, cible, heure, longueur, octets = sys.argv[1:]
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure) or not longueur.isdigit() or not octets.isdigit():
        print("REFUS : heure, longueur ou octets illisibles")
        return 2
    if sha(src) != EMPREINTE_SOURCE:
        print("REFUS : empreinte de la source ≠ v4")
        return 2
    ici = os.path.dirname(os.path.abspath(src))
    E = {}
    for n in PIECES:
        p = os.path.join(ici, n)
        c = open(p + ".sha256", encoding="utf-8").read()
        E[n] = sha(p)
        if c != f"{E[n]}  {n}\n":
            print(f"REFUS : compagnon de {n} faux ou absent")
            return 2
    sortie = open(os.path.join(ici, "sortie-repetition-machine-jeu-idee-1-1-v2.txt"), encoding="utf-8").read()
    m = re.search(r"^répétition : (\d+) cas, 0 écart\(s\)", sortie, re.M)
    if not m or f"longueur de la ligne : {longueur} " not in sortie:
        print("REFUS : sortie de la répétition v2 sans « 0 écart » ou sans la longueur donnée")
        return 2
    ncas = m.group(1)
    L = int(longueur)
    moitie = L - 6000
    oct_arrondi = f"{round(int(octets), -2):,}".replace(",", " ")
    lg_arrondi = f"{round(L, -2):,}".replace(",", " ")
    lg_exact = f"{L:,}".replace(",", " ")
    COUPLES = [
        ("titre", 1,
         "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v4",
         "# Procédure de la machine louée du jeu relancé de l'idée 1.1 — v5"),
        ("décision (en tête)", 1,
         "écrit et contre-lu (ordre de grandeur 1 à 3 USD), citant ce mot, avec une procédure de machine contre-lue ») ; R-3014.",
         "écrit et contre-lu (ordre de grandeur 1 à 3 USD), citant ce mot, avec une procédure de machine contre-lue ») ; R-3014 ;\n"
         "  GO-2026-11-16-10 (écart D7 accepté, R-3016) ; minuterie de 49 h 45 acceptée par la mère (R-3026)."),
        ("tour 2 point 4, couple 1 et lanceur (liste des pièces)", 1,
         "  `lancer_jeu_idee_1_1_machine_v1.sh` (côté session), `garde_machine_jeu_idee_1_1_v1.py` (gardes qu'il appelle),\n"
         "  `amorce_jeu_idee_1_1_v1.sh` (côté machine), `repetition_machine_jeu_idee_1_1_v1.sh` et `jeu_factice_idee_1_1_v1.py`\n"
         "  (répétition locale), ",
         f"  `lancer_jeu_idee_1_1_machine_v2.sh` (côté session, `{E['lancer_jeu_idee_1_1_machine_v2.sh']}`),\n"
         f"  `garde_machine_jeu_idee_1_1_v1.py` (gardes qu'il appelle, inchangées, `{E['garde_machine_jeu_idee_1_1_v1.py']}`),\n"
         f"  `amorce_jeu_idee_1_1_v2.sh` (côté machine, `{E['amorce_jeu_idee_1_1_v2.sh']}`),\n"
         f"  `repetition_machine_jeu_idee_1_1_v2.sh` (`{E['repetition_machine_jeu_idee_1_1_v2.sh']}`) et\n"
         f"  `jeu_factice_idee_1_1_v1.py` (inchangé, `{E['jeu_factice_idee_1_1_v1.py']}`) (répétition locale),\n  "),
        ("tour 2 point 4, couple 2 (sortie de la répétition)", 1,
         "`sortie-repetition-machine-jeu-idee-1-1-v1.txt` (sortie gardée : 110 cas, 0 écart),\n",
         f"`sortie-repetition-machine-jeu-idee-1-1-v2.txt` (sortie gardée : {ncas} cas, 0 écart :\n"
         f"  les 110 cas de la v1 et ceux de la reprise ; `{E['sortie-repetition-machine-jeu-idee-1-1-v2.txt']}`),\n"),
        ("tour 2 point 4, couple 3 (devis, rapport)", 1,
         "  `devis-machine-jeu-idee-1-1-v1.md`, `rapport-machine-jeu-idee-1-1-v1.md`, et cette procédure.",
         f"  `devis-machine-jeu-idee-1-1-v2.md` (`{E['devis-machine-jeu-idee-1-1-v2.md']}`),\n"
         f"  `rapport-machine-jeu-idee-1-1-v2.md` (`{E['rapport-machine-jeu-idee-1-1-v2.md']}`), et cette procédure.\n"
         "  Les pièces v1 du même dossier (lanceur, amorce, répétition et sa sortie, devis, rapport) et les procédures v1 à v4\n"
         "  restent archivées sans modification (R12) ; elles ne partent pas au feu."),
        ("tour 3, M1'' point 4, cinquième couple (statut)", 1,
         "contre-lue aux tours 1 (`contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`) et 2\n"
         "  (`contre-lecture-machine-jeu-idee-1-1-tour2-v1.md`), corrections du tour 1 en v3, corrections du tour 2 qui portent sur\n"
         "  cette pièce en v4 ; ne part pas au feu sans l'amorce v2, le devis v2, le rapport v2, la version suivante de cette\n"
         "  procédure qui les nomme et un tour 3 rendu `scellable` (§ 6) ;",
         "contre-lue aux tours 1 (`contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`), 2\n"
         "  (`contre-lecture-machine-jeu-idee-1-1-tour2-v1.md`) et 3 (`contre-lecture-machine-jeu-idee-1-1-tour3-v1.md`), corrections\n"
         "  du tour 1 en v3, du tour 2 en v4, des tours 2 (point 4) et 3 en v5, avec les pièces v2 qu'elle nomme (amorce, lanceur,\n"
         "  répétition, devis, rapport) ; ne part pas au feu sans un tour 4 rendu `scellable` (§ 6) ;"),
        ("version", 1,
         "- **Version** : v4, scellée à 2026-11-16T21:50:41Z (`date -u`) ; suit la v3 (`e91a9020…`) ; changements de la v3 à la v4 : corrections\n"
         "  de la contre-lecture du tour 2 qui portent sur cette pièce (§ 6).",
         f"- **Version** : v5, scellée à {heure} (`date -u`) ; suit la v4 (`996c8a5c…`) ; changements de la v4 à la v5 : couples du\n"
         "  tour 2 (point 4) et du tour 3 (M1'', m1''), pièces v2 nommées avec leurs empreintes, et les changements de rédaction\n"
         "  déclarés au § 6 (tour 3). La v4 (2026-11-16T21:50:41Z) suivait la v3 (`e91a9020…`) par les corrections du tour 2 qui\n"
         "  portaient sur cette pièce."),
        ("§ 1, pas 7 (reprise de l'amorce v2, dite exactement)", 1,
         "la machine restant vivante (aucun « stopped » tant que les sorties ne sont pas poussées) ;",
         "la machine restant vivante (aucun « stopped » tant que les sorties ne sont pas poussées et que l'échéance − 20 minutes\n"
         "   n'est pas atteinte ; chaque reprise manquée est journalisée, et le journal poussé si possible ; reprises épuisées :\n"
         "   arrêt en code 4 « après reprises », sorties intactes sur le disque de la machine arrêtée, que la minuterie détruit à\n"
         "   l'échéance) ;"),
        ("§ 1, codes de fin", 1,
         "compagnon faux, poussée des sorties impossible).",
         "compagnon faux, poussée des sorties impossible après reprises)."),
        ("§ 2, point 2 (part de l'écart D7, P2 du tour 1)", 1,
         "plus aucune question de la mère sur D7 ; le feu cite GO-2026-11-16-10 en toutes lettres.",
         "plus aucune question de la mère sur D7 ; le feu cite GO-2026-11-16-10 en toutes lettres.\n"
         "   **Part de l'écart D7, déclarée** (P2 du tour 1) : les poussées de la machine vers la branche de sortie pendant le jeu\n"
         "   (journal et `etat.txt` chaque heure, hors du processus du jeu), à sa fin (sorties) et leurs reprises (§ 1 pas 7, § 5)."),
        ("tour 3, m1'' (§ 2, point 3)", 1,
         "3. Contre-lecture de cette procédure, de l'amorce et du devis par un lecteur neuf (R2), tour 3 rendu `scellable`.",
         "3. Contre-lecture de cette procédure, de l'amorce, du lanceur, de la répétition et du devis par un lecteur neuf (R2),\n"
         "   tour 4 rendu `scellable`."),
        ("§ 2, point 5 (le feu cite la part de l'écart D7)", 1,
         "la ligne jouée par l'outil du loueur à son chemin complet (déjà dans la ligne imprimée).",
         "la ligne jouée par l'outil du loueur à son chemin complet (déjà dans la ligne imprimée) ; il cite aussi, comme part de\n"
         "   l'écart D7 (GO-2026-11-16-10), les poussées de la machine pendant et après le jeu, reprises comprises (§ 5)."),
        ("§ 3, L3 (longueur de la ligne de l'amorce v2)", 1,
         "la ligne fait ≈ 11 900 caractères (répétition : 11 911), lue en **deux\n  morceaux de 6 000**",
         f"la ligne fait ≈ {lg_arrondi} caractères (répétition v2 : {lg_exact}), lue en **deux\n"
         f"  morceaux** (6 000, puis {moitie})"),
        ("gestes : lanceur v2 (dix appels « $W/… »)", 10,
         "$W/lancer_jeu_idee_1_1_machine_v1.sh",
         "$W/lancer_jeu_idee_1_1_machine_v2.sh"),
        ("geste 5 : lanceur v2", 1,
         "lancer_jeu_idee_1_1_machine_v1.sh commande $R",
         "lancer_jeu_idee_1_1_machine_v2.sh commande $R"),
        ("geste 5 : taille de la sortie", 1,
         "`code 0`, **2** lignes, ≈ 12 100 octets,",
         f"`code 0`, **2** lignes, ≈ {oct_arrondi} octets,"),
        ("tour 2 point 4, couple 4 (geste 6)", 1,
         "> /root/amorce_jeu_idee_1_1_v1.sh && bash /root/amorce_jeu_idee_1_1_v1.sh",
         "> /root/amorce_jeu_idee_1_1_v2.sh && bash /root/amorce_jeu_idee_1_1_v2.sh"),
        ("geste 13 (reprise, puis destruction par la minuterie)", 1,
         "nœud de la mère, qui décide de la copie depuis la machine vivante avant l'échéance)",
         "nœud de la mère, qui décide de la copie depuis la machine vivante avant l'échéance ; la machine reprend seule la poussée\n"
         "    toutes les 5 minutes jusqu'à l'échéance − 20 minutes, puis s'arrête en code 4 « après reprises » ; sa minuterie la\n"
         "    détruit à l'échéance quoi qu'il arrive, disque compris : la décision se prend avant ; cette procédure n'écrit aucune\n"
         "    commande de copie depuis la machine)"),
        ("§ 5 (reprises comprises dans la part de l'écart D7)", 1,
         "ces poussées et celle des sorties à la fin sont déclarées comme part de l'écart D7 (texte scellé l. 629), que le feu cite en toutes lettres.",
         "ces poussées, celle des sorties à la fin et ses reprises (amorce v2 : toutes les 5 minutes, jusqu'à 20 minutes avant\n"
         "  l'échéance) sont déclarées comme part de l'écart D7 (texte scellé l. 629 ; P2 du tour 1), que le feu cite en toutes\n"
         "  lettres."),
        ("§ 6, tour 1 : « cette version » (v3)", 1,
         "le pas 7 et le geste 13 de\n    cette version décrivent la reprise",
         "le pas 7 et le geste 13 de\n    la v3 décrivent la reprise"),
        ("tour 3, M1'' point 4, phrase « Cette version ne part donc pas … » (réponse au tour 1)", 1,
         "pas. Cette version ne part donc pas au feu avec l'amorce v1 : il faut",
         "pas. La v3 ne partait donc pas au feu avec l'amorce v1 (dépendance levée en v5 : réponse au tour 3) : il faut"),
        ("§ 6, tour 2 : « Cette version » (v4)", 1,
         "- **Cette version** : v4, écrite par un rédacteur neuf",
         "- **Version v4** : écrite par un rédacteur neuf"),
        ("tour 3, M1'' point 4, phrase « Cette version ne part donc pas … » (réponse au tour 2)", 1,
         "La phrase\n    « Cette version ne part donc pas au feu avec l'amorce v1 » est donc gardée : elle vaut pour la v4.",
         "La phrase de la\n    réponse au tour 1 sur l'amorce v1 est donc gardée : elle vaut pour la v4 (levée en v5 : réponse au tour 3)."),
    ]
    t = open(src, encoding="utf-8").read()
    for nom, n, ancien, nouveau in COUPLES:
        k = t.count(ancien)
        if k != n:
            print(f"REFUS : couple « {nom} » : ancien trouvé {k} fois, {n} attendu(s)")
            return 2
        t = t.replace(ancien, nouveau)
        print(f"appliqué : {nom} ({n})")
    E3 = sha(os.path.join(ici, NOM_TOUR3))
    t = t.rstrip("\n") + "\n" + TOUR3.format(E3=E3, ncas=ncas, **{k.replace("-", "_").replace(".", "_"): v for k, v in E.items()}) + "\n"
    with open(cible, "x", encoding="utf-8") as f:
        f.write(t)
    print(f"écrit : {cible} ; {sha(cible)}")
    return 0


TOUR3 = """
**Tour 3** (corrections en v5) :

- **Rapport** : `contre-lecture-machine-jeu-idee-1-1-tour3-v1.md` (même dossier), empreinte `{E3}`, lecteur neuf (R2) ;
  verdict `corrections` (une majeure, M1'', en quatre points ; une mineure, m1'' ; remarques facultatives).
- **Cette version** : v5, écrite par un rédacteur neuf (modèle A, qui n'a écrit aucune pièce v1 ni les versions v1 à v4),
  au moyen du programme de couples `corriger_procedure_v4_vers_v5_tour3_v1.py` (même dossier,
  `{corriger_procedure_v4_vers_v5_tour3_v1_py}`), depuis la v4 `996c8a5cbe9d7cacba32124118dff30af8eb47ebf431a9c72925a7619687b24f`,
  après les pièces v2 qu'elle nomme.
- **Pièces v2 livrées** (fichiers neufs, R12, chacun avec son compagnon) :
  - `amorce_jeu_idee_1_1_v2.sh` `{amorce_jeu_idee_1_1_v2_sh}` : l'amorce v1 plus la reprise de la poussée des sorties
    (couples 1 et 2 du tour 1, forme fixée par l'auteur : fonction `reprise_sorties`, pause de 5 × `PAUSE` = 300 s,
    jusqu'à `MARGE_TERM` = 1 200 s avant l'échéance ; chaque reprise manquée journalisée et le journal poussé si possible ;
    reprises épuisées : `arret … après reprises … 4`) ; rien d'autre ne change que les commentaires d'en-tête ;
  - `lancer_jeu_idee_1_1_machine_v2.sh` `{lancer_jeu_idee_1_1_machine_v2_sh}` : le lanceur v1 dont l'amorce nommée est la v2
    (chemin du fichier, nom écrit sur la machine, motif de `controle-ligne`) ; la garde v1 ne nomme pas l'amorce : inchangée ;
  - `repetition_machine_jeu_idee_1_1_v2.sh` `{repetition_machine_jeu_idee_1_1_v2_sh}` et sa sortie gardée
    `sortie-repetition-machine-jeu-idee-1-1-v2.txt` `{sortie_repetition_machine_jeu_idee_1_1_v2_txt}` : **{ncas} cas, 0 écart** ;
    les 110 cas de la v1 et, par un crochet « pre-receive » du dépôt jouet qui refuse les poussées portant des sorties sur
    deux branches, la poussée refusée trois fois puis acceptée (machine vivante, sorties poussées égales à l'octet, aucun
    « stopped » avant) et la poussée jamais acceptée (reprises journalisées, arrêt en code 4 à l'échéance − `MARGE_TERM`,
    « stopped » après l'arrêt seulement, destruction à l'échéance, sorties intactes sur le disque) ; jeu factice v1 inchangé ;
  - `devis-machine-jeu-idee-1-1-v2.md` `{devis_machine_jeu_idee_1_1_v2_md}` : couples 5, 11, 16 et 17 du tour 1 ;
  - `rapport-machine-jeu-idee-1-1-v2.md` `{rapport_machine_jeu_idee_1_1_v2_md}` : D7 tranché (GO-2026-11-16-10), addendum de
    relance scellé (R-3017), minuterie acceptée (R-3026).
- **Réponse point par point** :
  - **M1'', points 1 à 3** : livrés (ci-dessus).
  - **M1'', point 4** (couples du tour 2, point 4) : les quatre couples appliqués (liste des pièces, en tête ; geste 6),
    les « nouveaux » portant les noms v2 et leurs empreintes ; le passage du statut supprimé (remplacé par la condition du
    tour 4) ; la phrase « Cette version ne part donc pas au feu avec l'amorce v1 » réécrite dans ses deux places (réponses aux
    tours 1 et 2, au passé, levée en v5). Les dix appels « `$W/lancer_jeu_idee_1_1_machine_v1.sh` » des gestes et celui du
    geste 5 nomment le lanceur v2.
  - **m1''** : appliqué (§ 2, point 3 : « tour 4 rendu `scellable` » ; le statut dit la même condition).
- **Changements de rédaction en plus des couples, déclarés** : en tête, « Décision » cite GO-2026-11-16-10 et R-3026 ;
  § 1 pas 7 et codes de fin disent exactement ce que fait l'amorce v2 (« stopped » après épuisement des reprises seulement,
  destruction par la minuterie à l'échéance) ; § 2 points 2 et 5 et § 5 déclarent comme part de l'écart D7 les poussées du
  journal et des sorties pendant et après le jeu, reprises comprises (P2 du tour 1) ; § 3 L3 et geste 5 : longueur de la
  ligne et taille de la sortie de `commande` relevées dans la répétition v2 ; geste 13 : la minuterie détruit la machine à
  l'échéance, disque compris, et aucune commande de copie depuis la machine n'est écrite ; § 6 : « cette version » des
  réponses aux tours 1 et 2 nommée v3 et v4.
- **Restes ouverts déclarés** (aucun ne relève du texte des gestes ; la mère les tient) :
  - F2 du tour 1 (geste 8 : `head -c 400 reponse-creation.json` pourrait afficher une clé ; noms seulement préférables) et
    F4 (geste 9 : un `None` à la place du prix est une forme à relire, non un prix à punir de destruction) : facultatives,
    toujours ouvertes ;
  - rappel programmé de la mère à l'échéance (49 h 45 après l'impression), même si tout va bien (P3 : la destruction par la
    machine elle-même n'a jamais été vue en vrai) ;
  - permission de la ligne neuve (forme `( umask 077; … > fichier )`) par Lazar avant de lancer (P4) ;
  - renouvellement du jeton `CONTROLE_IA_GITHUB_TOKEN_2` après la preuve de destruction (P5 ; nœud de Lazar : compte) ;
  - ligne de GO de type « calcul » à inscrire (périmètre « idée 1.1 », `3.5 USD`, échéance 2026-11-22 au plus tôt, devis v2
    § 1 ; P6) ;
  - `COMMIT` à relire au feu (la tête de `main` bouge ; P6) ; dossier à commiter ; fichiers parasites `/s.txt` et
    `/commande-coupee.txt` à effacer par une personne (R-3026) ;
  - réserves neuves de la rédaction v2, pour le tour 4 (rapport v2, § 5) : une poussée refusée par la garde de poussée
    (chemin hors des sorties, fichier de plus de 94 Mo) est reprise comme une panne ; une copie partielle des sorties n'est
    pas refaite par la reprise ; trafic montant des reprises dans le cas extrême (devis v2, § 4).
- **Rien d'autre ne change** de la v4 à la v5 : en tête (titre, décision, liste des pièces, statut, version), les couples
  ci-dessus et cette section."""


if __name__ == "__main__":
    raise SystemExit(main())
