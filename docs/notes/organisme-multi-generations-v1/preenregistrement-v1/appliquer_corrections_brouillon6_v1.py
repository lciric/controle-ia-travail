#!/usr/bin/env python3
"""Brouillon 5 -> brouillon 6 du préenregistrement de la course à plusieurs générations (famille MR-2).

Programme de couples « ancien -> nouveau » (R12 : la pièce de départ reste intacte ; la cible est un fichier neuf).
Il applique, et rien d'autre :
  - les douze couples des corrections exigées (m-12 à m-17) de la contre-lecture R2, tour 2
    (`../contre-lecture-preenregistrement-course-tour2-v1.md`), LUS DANS LE RAPPORT LUI-MÊME (aucune recopie à la main),
    avec la retouche de forme déclarée dans RETOUCHES (m-16 : colonne « où » de la ligne des marqueurs) ;
  - les couples de l'en-tête (version, rédacteur, heures : COUPLES_EN_TETE) et de la section « Contre-lecture »
    (COUPLES_CONTRE_LECTURE).

Contrôles, tous faits avant toute écriture :
  - empreintes sha256 du brouillon 5 et du rapport égales aux valeurs écrites ici ;
  - douze couples lus dans le rapport, avec les étiquettes attendues, dans l'ordre ; un champ écrit sur plusieurs lignes
    (le « nouveau » du premier couple de m-16) est lu jusqu'à son accent grave de fin, et aucun accent grave n'est permis à
    l'intérieur d'un champ ;
  - chaque fragment de retouche trouvé exactement une fois dans le champ du couple qu'il touche ;
  - chaque « ancien » présent exactement une fois dans le brouillon 5 et dans le texte courant au moment où il s'applique ;
  - aucun marqueur de remplissage restant (« @@ », « À REMPLIR », marqueur de gabarit) ;
  - passage réel : ce programme scellé avant son passage (compagnon .sha256 égal) ; cible et différentiel absents
    (ouverture exclusive : jamais d'écrasement).

Usage (interpréteur isolé, bibliothèque standard seule) :
  python3 -I appliquer_corrections_brouillon6_v1.py --essai SORTIE          essai à blanc : SORTIE et SORTIE.diff, hors du dépôt
  python3 -I appliquer_corrections_brouillon6_v1.py "AAAA-MM-JJ HH:MM:SS"   passage réel ; heure relevée par `date -u` juste avant
"""
from __future__ import annotations

import difflib
import hashlib
import re
import sys
from pathlib import Path

PROGRAMME = Path(__file__).resolve()
ICI = PROGRAMME.parent
RACINE_DEPOT = ICI.parents[3]
SOURCE = ICI / "preenregistrement-multi-generations-v1-brouillon5.md"
CIBLE = ICI / "preenregistrement-multi-generations-v1-brouillon6.md"
DIFFERENTIEL = ICI / "differentiel-preenregistrement-brouillon5-brouillon6.diff"
RAPPORT = ICI.parent / "contre-lecture-preenregistrement-course-tour2-v1.md"
EMPREINTE_SOURCE = "7100a978335893ffd3d0ae9ec142622361869621e8496be138b3f1d782f907f8"
EMPREINTE_RAPPORT = "d067513c1a505ef85e9219c90e8dd2a0decbd58865b1bf66210ef72b4acc936e"
ETIQUETTES = ("m-12", "m-12", "m-12", "m-12", "m-12", "m-12", "m-13", "m-14", "m-15", "m-16", "m-16", "m-17")
DEBUT_ANCIEN = "- ancien : `"
DEBUT_NOUVEAU = "- nouveau : `"

# Retouches de forme sur un champ d'un couple du rapport : (rang du couple dans le rapport, étiquette, champ (1 : ancien,
# 2 : nouveau), fragment du rapport, fragment retenu). Le fond est celui du rapport ; la retouche est dite et motivée dans la
# section « Contre-lecture ».
RETOUCHES = (
    # m-16, second couple : la colonne « où » de la même ligne des marqueurs reçoit « Décisions », section qui porte la ligne
    # Q-4 … Q-8 de la table « Tranchées » et le point 11 neuf ; l'« ancien » et le « nouveau » sont prolongés de cette cellule,
    # le reste de la ligne inchangé.
    (10, "m-16", 1, "taille des lois servies |", "taille des lois servies | Seuil ; À vérifier sur le code |"),
    (10, "m-16", 2, "non confirmés |", "non confirmés | Seuil ; À vérifier sur le code ; Décisions |"),
)

COUPLES_EN_TETE = (
    ("en-tête, titre",
     "# Préenregistrement — course de l'organisme d'idéation à plusieurs générations, monde riche à doublons, famille MR-2 — v1, "
     "brouillon 5\n",
     "# Préenregistrement — course de l'organisme d'idéation à plusieurs générations, monde riche à doublons, famille MR-2 — v1, "
     "brouillon 6\n"),
    ("en-tête, statut (version)",
     "**Statut : brouillon 5 (R1), non scellable en l'état.** Brouillon 4 (`preenregistrement-multi-generations-v1-brouillon4.md`,\n"
     "`678163db…`, gardé intact, R12) auquel sont appliquées, par un programme de couples « ancien → nouveau », les corrections exigées\n"
     "par sa contre-lecture R2, tour 1 (`contre-lecture-preenregistrement-course-tour1-v1.md`, `57ac2055…` : quatre majeures et onze\n"
     "mineures) ; hors de ces couples, seuls l'en-tête et la section « Contre-lecture » changent (contre-lecture 3). Le brouillon 4 est\n",
     "**Statut : brouillon 6 (R1), non scellable en l'état.** Brouillon 5 (`preenregistrement-multi-generations-v1-brouillon5.md`,\n"
     "`7100a978…`, gardé intact, R12) auquel sont appliquées, par un programme de couples « ancien → nouveau », les corrections exigées\n"
     "par sa contre-lecture R2, tour 2 (`contre-lecture-preenregistrement-course-tour2-v1.md`, `d067513c…` : aucune majeure, six\n"
     "mineures) ; hors de ces couples, seuls l'en-tête et la section « Contre-lecture » changent (contre-lecture 4). Le brouillon 5 est\n"
     "lui-même le brouillon 4 (`preenregistrement-multi-generations-v1-brouillon4.md`, `678163db…`, gardé intact, R12) corrigé de la\n"
     "même façon selon sa contre-lecture R2, tour 1 (`contre-lecture-preenregistrement-course-tour1-v1.md`, `57ac2055…` : quatre\n"
     "majeures et onze mineures ; contre-lecture 3). Le brouillon 4 est\n"),
    ("en-tête, statut (ordre des étapes)",
     "(tour 1 fait sur le brouillon 4 ; reste un second tour, sur le différentiel du\n"
     "brouillon 4 au brouillon 5) ;",
     "(tour 1 fait sur le brouillon 4 ; tour 2 fait sur le brouillon 5 ; reste la vérification\n"
     "courte du différentiel du brouillon 5 au brouillon 6) ;"),
    ("en-tête, rédacteur du brouillon 6",
     "  « Contre-lecture », déclaration du rédacteur du brouillon 5.\n"
     "- **Date (UTC)** : 2026-11-17 (heures en fin d'en-tête).\n",
     "  « Contre-lecture », déclaration du rédacteur du brouillon 5.\n"
     "- **Rédacteur du brouillon 6** : modèle A, rédacteur neuf, sous-agent d'un script d'orchestration de la session mère. La consigne\n"
     "  de la tâche me nomme « modèle C » ; je m'écris A pour la même raison que le rédacteur du brouillon 5 : la table de la correction\n"
     "  m-3 de la conception v7 (section « Contre-lecture (v6 …) ») donne la lettre A au modèle que la conception v5 nomme comme son\n"
     "  rédacteur, dont je suis une instance ; R-2982 veut les corrections écrites par A et R-2992 dit fausses les mentions « rédacteur\n"
     "  lettre C » ; à confirmer par la mère. Je n'ai écrit ni les brouillons 1 à 5, ni leurs lectures, ni les rapports des tours 1 et\n"
     "  2, ni la conception, ni le code, ni le pilote, ni son verdict, ni le devis du banc ; j'ai appliqué les couples du rapport du\n"
     "  tour 2 par un programme, et rien d'autre (section « Contre-lecture », contre-lecture 4).\n"
     "  **Réserve de lignée** : même modèle que les rédacteurs des brouillons 4 et 5 ; la vérification courte du différentiel du\n"
     "  brouillon 5 au brouillon 6 doit venir d'un lecteur d'une autre lignée que le modèle A, qui n'ait écrit ni ce texte ni le\n"
     "  programme des couples. Interdits de la tâche tenus ; incidents : section « Contre-lecture », déclaration du rédacteur du\n"
     "  brouillon 6.\n"
     "- **Date (UTC)** : 2026-11-17 (heures en fin d'en-tête).\n"),
    ("en-tête, heures du brouillon 6",
     "  scellement du programme et son passage ; la ligne ne peut plus changer ensuite, R12).\n"
     "- **Interdits tenus** :",
     "  scellement du programme et son passage ; la ligne ne peut plus changer ensuite, R12).\n"
     "- **Heures du brouillon 6** (relevées par `date -u`) : premier relevé 2026-11-17 02:18:01, à la vérification des empreintes du\n"
     "  rapport du tour 2 et du brouillon 5, avant leur lecture entière ; essais à blanc du programme des couples, sorties au\n"
     "  bloc-notes, hors du dépôt ; puis, dans une même commande, programme scellé et passé, ce texte et son différentiel scellés, à\n"
     "  @@HEURE@@ (heure relevée par `date -u` entre le scellement du programme et son passage ; la ligne ne peut plus changer\n"
     "  ensuite, R12).\n"
     "- **Interdits tenus** :"),
)

TABLE_REPONSE = (
    "| point | réponse | où | ancien (brouillon 5) → nouveau (brouillon 6) |\n"
    "|---|---|---|---|\n"
    "| **m-12** : l'état « sans carte » (couple m-8) absent des énumérations des états d'appel, et « cinquième » faux | "
    "**appliquée** (six couples, texte du rapport) | L.5, W-13 ; D.12, « Plafond de session atteint » (génération appauvrie) et "
    "« Appel sans carte » ; Métrique, « Appels » ; Plan d'analyse, point 8 ; V-17 | W-13 : « (complet, tronqué, coupé, refusé, "
    "échec) » → « (complet, sans carte, tronqué, coupé, refusé, échec) » ; D.12 : « W-13 le lit comme un cinquième état non "
    "fautif. » → « W-13 le lit comme un état non fautif de plus (cinq non fautifs, avec l'échec en sixième) ; ses cartes admises, "
    "zéro, entrent dans le compte de la « génération appauvrie » (« moins de 12 cartes admises » ci-dessus). », et « tronqués, "
    "coupés ou refusés d'une génération » → « tronqués, coupés, refusés ou sans carte d'une génération » ; Métrique et Plan "
    "d'analyse, point 8 : « complets, tronqués, » → « complets, sans carte, tronqués, » ; V-17 : « complet, tronqué, » → "
    "« complet, sans carte, tronqué, » |\n"
    "| **m-13** : « aucun vers 197 000 » faux de quelques pour cent (erreur du lecteur du tour 1) | **appliquée** (texte du "
    "rapport) | « Points ouverts », point 5 | « et aucun vers 197 000 : calcul du lecteur » → « et aucun vers 199 000 (200 000 à "
    "la borne exacte de 2 USD d'entrée au prix supposé) : calcul du lecteur du tour 1, refait au tour 2 » ; calcul refait "
    "(contrôles ci-dessus) ; la remarque du rédacteur du brouillon 5 sur m-4 (« laissé tel quel ») est close |\n"
    "| **m-14** : mondes sans tirage conforme dits « qu'au dénominateur » par la règle de n et « exclus et comptés à part » par "
    "celle de τ | **appliquée** (texte du rapport) | « Seuil », règle (3), parenthèse finale | « ne comptent qu'au dénominateur "
    "de la règle de garde.) » → « n'entrent que dans le dénominateur de la règle de garde, et sont comptés à part au rapport "
    "pour n et pour τ.) » |\n"
    "| **m-15** : « le code refuse de générer » sans dire qui contrôle les commits, alors que la machine ne porte aucun jeton du "
    "dépôt | **appliquée** (texte du rapport) | D.3, mondes de test, point 4 | « **Le code refuse de générer** si l'empreinte du "
    "secret » → « **Le code refuse de générer** (le contrôle des commits est fait par le lanceur hors de la machine, qui ne porte "
    "aucun jeton du dépôt, comme pour le secret de calibration, garde 35 ; la machine ne génère que sur l'ordre du lanceur) si "
    "l'empreinte du secret » |\n"
    "| **m-16** : Q-4, Q-6 et l'étendue de Q-5 et de Q-8, « non confirmés », sans point ouvert ni ligne de marqueur | "
    "**appliquée** (deux couples, texte du rapport), une retouche de forme | « Points ouverts », point 11 (neuf) ; « Marqueurs "
    "restants », ligne du sous-choix de τ | point 11 ajouté après le point 10 : « Q-4 (nul v8), Q-6 (retirage automatique) et "
    "l'étendue de Q-5 et de Q-8 : non confirmés par les conditions des lignes de GO (table « Tranchées ») ; mot de Lazar, ou, à "
    "défaut, décision de la mère consignée au registre, avant le scellement. » ; ligne des marqueurs : « […] ; taille des lois "
    "servies » → « […] ; taille des lois servies ; Q-4, Q-6 (et étendue de Q-5, Q-8) non confirmés » ; retouche : l'« ancien » et "
    "le « nouveau » du second couple sont prolongés de la cellule « où » de la même ligne, « Seuil ; À vérifier sur le code », "
    "qui devient « Seuil ; À vérifier sur le code ; Décisions » (section qui porte la ligne Q-4 … Q-8 et le point 11) ; le reste "
    "de la ligne est inchangé ; la ligne Q-4 … Q-8 reste dans la table « Tranchées » : le rapport ne la déplace pas |\n"
    "| **m-17** : deux mesures du banc citées par le texte et non nommées par la liste de M-2 | **appliquée** (texte du rapport) "
    "| « Préalables », avant le scellement, point 8 | « (brouillon 3 §16.1 point 5) ; » → « (brouillon 3 §16.1 point 5), "
    "fréquences des sortes déformées par les rejets (D.1 « Régularités »), coût du calcul de d_nul à 48 feuilles (D.8 point 4, "
    "V-21) ; » |\n"
    "| remarques facultatives 1 à 6 (retouche de M-1 ; nom de famille de modèles en « Portée » ; prix de X1 ; renvois au "
    "brouillon 3 que la liste de m-11 ne nomme pas ; étiquette « progrès tardif » de la ligne V ; points du rédacteur laissés à "
    "la mère) | **non appliquées** | — | non exigées par le rapport ; la tâche borne le brouillon 6 aux corrections exigées ; la "
    "4, que le rapport veut levée dans la version finale, est inscrite à « À faire » |\n"
    "| constats du rédacteur du brouillon 5 (« Ce que les couples laissent ») | **suivis par le rapport** ; aucun couple de plus | "
    "— | (1) → m-17 ; (3) → m-12 ; (5) → m-16 (point ajouté ; ligne non déplacée) ; (4) → remarque facultative 4 ; (6) → "
    "remarque facultative 5 ; (2) (formation des 8 lois) : reste à la pièce des règles du banc ; le paragraphe des constats reste "
    "tel quel |\n"
    "| ce que le rapport dit du rédacteur du brouillon 5 (§5) et points pour la mère (§6) | **pris comme constats ; non tranchés "
    "ici** | — | « rien d'autre ne change » au brouillon 5 : confirmé par le rapport ; réserve de lignée du brouillon 5 : levée "
    "par le tour 2, selon son lecteur (§6 point 3) ; lettre du rédacteur et filtre de récupération du brouillon 5 : à la mère ; "
    "mots de Lazar nécessaires (sous-choix de τ ; Q-4, Q-6 et l'étendue de Q-5 et de Q-8 ; lecture d'E-2 ; relèvement d'un "
    "plafond de session ; second cycle du banc ; publication), risque des troncatures à 2 USD, archive servie croissante et "
    "calendrier : à la mère et à Lazar ; l'erreur « 197 000 » (point 4) est reprise par m-13 ; la vérification courte (point 1) "
    "est inscrite à « À faire » |\n"
    "| en-tête | **mis à jour** | titre ; « Statut » ; « Rédacteur du brouillon 6 » ; « Heures du brouillon 6 » | version "
    "brouillon 5 → brouillon 6 ; le « Statut » décrit le brouillon 6, puis le brouillon 5 ; dans l'ordre des étapes, tours 1 et 2 "
    "faits, vérification courte à faire ; heures par `date -u` |\n"
    "| section « Contre-lecture » | **mise à jour** | ici | phrase d'ouverture ; contre-lecture 4 et cette réponse, après la "
    "déclaration du rédacteur du brouillon 5 ; constats et déclaration du rédacteur du brouillon 6 ; « À faire » réécrit pour le "
    "brouillon 6 |\n"
)

COUPLES_CONTRE_LECTURE = (
    ("contre-lecture, phrase d'ouverture",
     "Contre-lectures faites (le traitement des contre-lectures 1 et 2 est porté par les brouillons 2 et 3, celui de la contre-lecture 3\n"
     "par ce brouillon 5 ; ce brouillon les garde toutes) :",
     "Contre-lectures faites (le traitement des contre-lectures 1 et 2 est porté par les brouillons 2 et 3, celui de la contre-lecture 3\n"
     "par le brouillon 5, dont la réponse suit, celui de la contre-lecture 4 par ce brouillon 6, dont la réponse vient après la\n"
     "déclaration du rédacteur du brouillon 5 ; ce brouillon les garde toutes) :"),
    ("contre-lecture, entrée 4, réponse, déclaration et « À faire »",
     "**À faire, sur ce brouillon 5** : un second tour de contre-lecture R2, plus court, sur le différentiel du brouillon 4 au brouillon 5\n"
     "et sur les points que la réponse ci-dessus signale, par un lecteur neuf d'une autre lignée que le modèle A, qui n'ait écrit ni ce\n"
     "texte ni le rapport du tour 1 (fichiers à lui donner : le rapport du tour 1, le brouillon 4, ce brouillon 5, le différentiel et le\n"
     "programme des couples) ; puis, sur la version finale (après le banc), contre-lecture finale et vérification courte du différentiel.\n"
     "Pour chacune : identifiant du lecteur (lettre), empreinte du brouillon relu, chemin et empreinte du rapport, traitement de chaque\n"
     "remarque (acceptée, refusée et pourquoi), à écrire ici. Le différentiel brouillon 2 → brouillon 3 n'a jamais eu sa vérification\n"
     "courte (brouillon 3 §19) : la contre-lecture 3 a lu le brouillon 4 en entier et l'a comparé aux sections 6, 8, 9, 10 et 16 du\n"
     "brouillon 3, sans trouver de changement non annoncé hors de la table B4-1 à B4-15 ; la réserve est levée pour ces sections, non\n"
     "pour le reste du brouillon 3, lu par sondage.\n",
     "- **Contre-lecture 4** (tour 2, sur le brouillon 5) — lecteur neuf, modèle C, d'une autre lignée que le rédacteur du brouillon 5\n"
     "  (modèle A), qui n'a écrit aucune des pièces et a recontrôlé sur le brouillon 5 les couples du tour 1 ; brouillon relu :\n"
     "  `preenregistrement-multi-generations-v1-brouillon5.md`, `7100a978335893ffd3d0ae9ec142622361869621e8496be138b3f1d782f907f8` (égale\n"
     "  à son compagnon) ; rapport : `contre-lecture-preenregistrement-course-tour2-v1.md` (dossier\n"
     "  `docs/notes/organisme-multi-generations-v1/`), `d067513c1a505ef85e9219c90e8dd2a0decbd58865b1bf66210ef72b4acc936e` (égale à son\n"
     "  compagnon). Verdict « corrections » : les dix-huit couples du tour 1 appliqués fidèlement, retouches de forme déclarées\n"
     "  acceptées, rien d'autre dans le différentiel que l'en-tête et la section « Contre-lecture » ; **aucune majeure et six mineures\n"
     "  (m-12 à m-17)**, toutes de cohérence, données en douze couples exacts ; six remarques facultatives ; six points pour la mère.\n"
     "  **Toutes les corrections exigées sont acceptées et appliquées** ; aucune n'est refusée.\n"
     "  - **Méthode** : programme `preenregistrement-v1/appliquer_corrections_brouillon6_v1.py` (`@@EMPREINTE_PROGRAMME@@`,\n"
     "    compagnon `.sha256`, scellé avant son passage). Il vérifie l'empreinte du brouillon 5 et celle du rapport ; il lit les douze\n"
     "    couples dans le rapport lui-même, sans recopie à la main (le « nouveau » du premier couple de m-16, écrit sur deux lignes, est\n"
     "    lu jusqu'à son accent grave de fin), et vérifie leurs étiquettes ; il applique la retouche de forme dite dans la table (m-16),\n"
     "    chacun de ses deux fragments trouvé une seule fois dans le champ du couple qu'il touche ; il vérifie que chaque « ancien »\n"
     "    (couples du rapport, de l'en-tête et de cette section) figure exactement une fois dans le brouillon 5 et dans le texte courant\n"
     "    au moment où il s'applique ; il refuse d'écraser la cible et le différentiel. Différentiel\n"
     "    `preenregistrement-v1/differentiel-preenregistrement-brouillon5-brouillon6.diff` (format de `diff -u`, compagnon `.sha256`).\n"
     "  - **Contrôles faits avant d'appliquer** (lecture seule) : chaque « ancien » du rapport figure une fois dans le brouillon 5\n"
     "    (compté par le programme, à l'essai à blanc) ; m-12 : la liste donne cinq états non fautifs (complet, sans carte, tronqué,\n"
     "    coupé, refusé) et l'échec en sixième, et la règle de la « génération appauvrie » est bien au-dessus du point « Appel sans\n"
     "    carte » dans D.12 ; m-13, refait à la main au prix supposé (10 USD par million de jetons d'entrée, un jeton par octet au pire,\n"
     "    et 50 en sortie) : chaque octet d'entrée retire 0,2 jeton de sortie sous le plafond de 2 USD ; la sortie s'annule à\n"
     "    200 000 octets à la borne exacte et, en partant de 29 395 jetons à 52 000 octets, vers 52 000 + 29 395 / 0,2 ≈ 198 975 octets,\n"
     "    soit environ 199 000 ; m-14 : la règle (5) dit les mondes sans tirage conforme « exclus et comptés à part » ; m-15 : la\n"
     "    garde 35 dit le contrôle des commits « fait par le lanceur **hors de la machine** (la machine ne porte aucun jeton du dépôt) » ;\n"
     "    m-16 : le point 10 est le dernier des « Points ouverts » ; m-17 : D.1 « Régularités » écrit « fréquences déformées par les\n"
     "    rejets, mesurées au banc et déclarées », D.8 point 4 « le coût du calcul de d_nul (à mesurer au banc) » et V-21 « coût du calcul\n"
     "    à 48 feuilles mesuré ».\n"
     "\n"
     + TABLE_REPONSE +
     "\n"
     "**Rien d'autre ne change** : hors de m-13 (« 197 000 » devient « 199 000 », avec « 200 000 » à la borne exacte), aucun chiffre du\n"
     "brouillon 5 n'est modifié ; le corps ne reçoit que le texte des douze couples et de la retouche de m-16 ; les sections\n"
     "« Changements depuis le brouillon 3 » et « Déclaration » (celle du rédacteur du brouillon 4), la réponse à la contre-lecture 3,\n"
     "les constats et la déclaration du rédacteur du brouillon 5 restent en place, tels quels ; les remarques facultatives des tours 1\n"
     "et 2 restent non appliquées.\n"
     "\n"
     "**Ce que les couples laissent, à voir à la vérification courte** (constats du rédacteur du brouillon 6 ; aucun couple, rien\n"
     "changé) : (1) m-12 : trois endroits nomment encore les appels à zéro carte admise sans l'état « sans carte » : L.1, « En tête du\n"
     "rapport » (« appels tronqués, coupés au plafond ou refusés, par proposeur et génération ») ; A6 (« appels tronqués, coupés ou\n"
     "refusés, comptés par fournisseur et génération », avant toute lecture PL) ; le dernier paragraphe de la « Liste d'arrêt »\n"
     "(« Appels tronqués, coupés au plafond, refusés : jamais un arrêt (D.12) ») ; le rapport ne les vise pas, et un appel sans carte\n"
     "peut lui aussi faire un négatif par artefact (A6) ; (2) « Préalables », avant le scellement, point 1, décrit encore la\n"
     "contre-lecture « de ce brouillon 4 » et des corrections « portées dans un brouillon 5 », faites depuis (contre-lectures 3 et 4) :\n"
     "à mettre à jour dans la version finale.\n"
     "\n"
     "**Déclaration du rédacteur du brouillon 6** (la déclaration du rédacteur du brouillon 5, plus haut, et la section « Déclaration »\n"
     "qui suit, celle du rédacteur du brouillon 4, restent les leurs) :\n"
     "\n"
     "- **Rôle** : rédacteur neuf, sous-agent d'un script d'orchestration de la session mère ; aucune autorité de décision ; lettre :\n"
     "  en-tête, « Rédacteur du brouillon 6 ». J'ai écrit le programme des couples, ce brouillon 6 (par lui) et le différentiel ; rien\n"
     "  d'autre.\n"
     "- **Pièces lues** (empreintes recalculées, égales à leur compagnon) : rapport du tour 2 `d067513c…` et brouillon 5 `7100a978…`\n"
     "  (entiers) ; programme des couples du brouillon 5 `f87f0c90…` (entier, comme modèle du mien) ; pour la lettre, conception v7\n"
     "  `1f1b64df…` (lignes « Rédacteur » de l'en-tête ; lignes m-3 et C-1 des sections « Contre-lecture (v6 …) » et « (v7 …) »),\n"
     "  conception v5 `a12ab1e5…` (lignes « Rédacteur » et « Lignée »), R-2982 et R-2992 de `registres/decisions.md` ; lignes\n"
     "  GO-2026-11-13-01, GO-2026-11-13-02 et GO-2026-11-17-05 de `registres/go.md` (rien inscrit) ; `src/controle_ia/scellement.py`\n"
     "  et `src/controle_ia/prereg.py`. Empreintes seules recalculées : brouillon 4 `678163db…`, rapport du tour 1 `57ac2055…`,\n"
     "  différentiel du brouillon 4 au brouillon 5 `09bf66ca…`.\n"
     "- **Pièces écrites** (scellées, compagnon `.sha256`) : `preenregistrement-v1/appliquer_corrections_brouillon6_v1.py` (scellé avant\n"
     "  son passage) ; ce texte ; `preenregistrement-v1/differentiel-preenregistrement-brouillon5-brouillon6.diff`.\n"
     "- **Contrôles sur l'essai à blanc** (texte égal à celui-ci hors l'heure) : validateur `controle_ia.prereg.problemes` sans\n"
     "  remarque ; aucun nom de modèle ni de fournisseur ajouté (recherche sur les noms connus du dépôt) ; aucun marqueur de remplissage\n"
     "  restant ; différentiel relu.\n"
     "- **Incidents de ma main** : (1) la consigne de la tâche me nomme « modèle C » ; je m'écris A (en-tête), à confirmer par la mère ;\n"
     "  (2) la recherche des lignes R-2982 et R-2992 a affiché en passant le début des lignes R-2983 (dépense inscrite du pilote) et\n"
     "  R-3054 du registre des décisions, et R-2982 elle-même nomme des travaux d'autres lignes (dont B bis) : rien n'en est tiré ni\n"
     "  recopié ; (3) validateur et scellement lancés sous l'interpréteur du venv avec `PYTHONPATH=src` : des fichiers `__pycache__`,\n"
     "  ignorés par git, peuvent en naître ; (4) aucune autre : aucune machine, aucun appel au loueur ni à un fournisseur de modèles,\n"
     "  aucune dépense ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; aucune branche du pilote récupérée (ni son code ni\n"
     "  son verdict relus pour ce brouillon) ; aucun secret ; aucun monde ; rien lu sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b,\n"
     "  T0.6, T0.7, B bis, P3-bis, du bras d'attaque ni du mode tenu à l'écart ; aucune valeur de clé, ni `env` ni `printenv` ; dans le\n"
     "  dépôt principal, lectures git seules (`git status`, `git log`), sans `GIT_DIR`, `GIT_WORK_TREE` ni `GIT_INDEX_FILE` ; aucun\n"
     "  fichier existant modifié ; rien committé de ma main.\n"
     "\n"
     "**À faire, sur ce brouillon 6** : la vérification courte du différentiel du brouillon 5 au brouillon 6 (couples, retouche de m-16,\n"
     "en-tête, section « Contre-lecture » ; rapport du tour 2, §6 point 1), par un lecteur d'une autre lignée que le modèle A, qui n'ait\n"
     "écrit ni ce texte ni le programme des couples (fichiers à lui donner : le rapport du tour 2, le brouillon 5, ce brouillon 6, le\n"
     "différentiel et le programme des couples) ; puis, sur la version finale (après le banc), contre-lecture finale et vérification\n"
     "courte du différentiel, la version finale levant aussi la remarque facultative 4 du tour 2 (liste exhaustive des renvois au\n"
     "brouillon 3, ou leur recopie). Pour chacune : identifiant du lecteur (lettre), empreinte du brouillon relu, chemin et empreinte\n"
     "du rapport, traitement de chaque remarque (acceptée, refusée et pourquoi), à écrire ici. Le différentiel brouillon 2 → brouillon 3\n"
     "n'a jamais eu sa vérification courte (brouillon 3 §19) : la contre-lecture 3 a lu le brouillon 4 en entier et l'a comparé aux\n"
     "sections 6, 8, 9, 10 et 16 du brouillon 3, sans trouver de changement non annoncé hors de la table B4-1 à B4-15 ; la réserve est\n"
     "levée pour ces sections, non pour le reste du brouillon 3, lu par sondage.\n"),
)


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def arret(message: str) -> None:
    sys.stderr.write("ARRÊT : " + message + "\n")
    raise SystemExit(2)


def lire_champ(lignes: list[str], i: int, debut: str) -> tuple[str, int]:
    """Corps d'un champ « ancien » ou « nouveau » commencé à la ligne i, lu jusqu'à son accent grave de fin.

    Renvoie le corps (lignes jointes par un saut de ligne, sans l'accent grave de fin) et le rang de sa dernière ligne.
    """
    morceaux = [lignes[i][len(debut):]]
    j = i
    while not morceaux[-1].endswith("`"):
        j += 1
        if j >= len(lignes) or not lignes[j].strip() or lignes[j].startswith((DEBUT_ANCIEN, DEBUT_NOUVEAU)):
            arret(f"rapport : champ commencé à la ligne {i + 1} sans accent grave de fin")
        morceaux.append(lignes[j])
    corps = "\n".join(morceaux)[:-1]
    if not corps or "`" in corps:
        arret(f"rapport : champ de la ligne {i + 1} vide ou portant un accent grave à l'intérieur")
    return corps, j


def lire_couples(texte_rapport: str) -> list[list[str]]:
    """Couples « ancien / nouveau » du rapport, avec l'étiquette de la correction qui les porte, dans l'ordre."""
    lignes = texte_rapport.splitlines()
    couples: list[list[str]] = []
    etiquette = None
    ancien = None
    i = 0
    while i < len(lignes):
        ligne = lignes[i]
        m = re.match(r"^\*\*((?:M|m)-\d+)\.", ligne)
        if m:
            etiquette = m.group(1)
        if ligne.startswith(DEBUT_ANCIEN):
            if ancien is not None:
                arret(f"rapport : « ancien » de la ligne {i + 1} sans « nouveau » avant lui")
            ancien, i = lire_champ(lignes, i, DEBUT_ANCIEN)
        elif ligne.startswith(DEBUT_NOUVEAU):
            if ancien is None:
                arret(f"rapport : « nouveau » de la ligne {i + 1} sans « ancien »")
            nouveau, i = lire_champ(lignes, i, DEBUT_NOUVEAU)
            couples.append([etiquette, ancien, nouveau])
            ancien = None
        i += 1
    if ancien is not None:
        arret("rapport : dernier « ancien » sans « nouveau »")
    return couples


def construire(heure: str, empreinte_programme: str) -> tuple[str, str, list[str]]:
    octets_source = SOURCE.read_bytes()
    if empreinte(octets_source) != EMPREINTE_SOURCE:
        arret(f"empreinte du brouillon 5 {empreinte(octets_source)} ≠ {EMPREINTE_SOURCE}")
    octets_rapport = RAPPORT.read_bytes()
    if empreinte(octets_rapport) != EMPREINTE_RAPPORT:
        arret(f"empreinte du rapport {empreinte(octets_rapport)} ≠ {EMPREINTE_RAPPORT}")
    source = octets_source.decode("utf-8")
    couples = lire_couples(octets_rapport.decode("utf-8"))
    if tuple(c[0] for c in couples) != ETIQUETTES:
        arret(f"étiquettes lues dans le rapport {tuple(c[0] for c in couples)} ≠ attendues")
    for rang, etiquette, champ, avant, apres in RETOUCHES:
        if couples[rang][0] != etiquette:
            arret(f"retouche : le couple {rang + 1} porte {couples[rang][0]}, non {etiquette}")
        n = couples[rang][champ].count(avant)
        if n != 1:
            arret(f"retouche de {etiquette} : fragment trouvé {n} fois dans le champ {champ} du couple {rang + 1}")
        couples[rang][champ] = couples[rang][champ].replace(avant, apres)

    a_appliquer = list(COUPLES_EN_TETE)
    a_appliquer += [(f"{e} (couple {k + 1} du rapport)", a, n) for k, (e, a, n) in enumerate(couples)]
    a_appliquer += list(COUPLES_CONTRE_LECTURE)

    texte = source
    journal = []
    for ident, ancien, nouveau in a_appliquer:
        nouveau = nouveau.replace("@@HEURE@@", heure).replace("@@EMPREINTE_PROGRAMME@@", empreinte_programme)
        n_source, n_courant = source.count(ancien), texte.count(ancien)
        if n_source != 1:
            arret(f"{ident} : « ancien » trouvé {n_source} fois dans le brouillon 5")
        if n_courant != 1:
            arret(f"{ident} : « ancien » trouvé {n_courant} fois dans le texte courant")
        ligne = source[: source.index(ancien)].count("\n") + 1
        texte = texte.replace(ancien, nouveau, 1)
        journal.append(f"{ident} : appliqué (ligne {ligne} du brouillon 5)")

    for marque in ("@@", "À REMPLIR"):
        if marque in texte:
            arret(f"marqueur « {marque} » restant dans le texte neuf")
    if re.search(r"<<[A-Z0-9_]+>>", texte):
        arret("marqueur de gabarit restant dans le texte neuf")
    differentiel = "".join(difflib.unified_diff(
        source.splitlines(keepends=True), texte.splitlines(keepends=True),
        fromfile="preenregistrement-v1/" + SOURCE.name, tofile="preenregistrement-v1/" + CIBLE.name, n=3))
    return texte, differentiel, journal


def ecrire_exclusif(chemin: Path, contenu: str) -> None:
    with open(chemin, "x", encoding="utf-8", newline="") as f:
        f.write(contenu)


def main(argv: list[str]) -> int:
    empreinte_programme = empreinte(PROGRAMME.read_bytes())
    if len(argv) == 2 and argv[0] == "--essai":
        sortie = Path(argv[1]).resolve()
        if RACINE_DEPOT == sortie or RACINE_DEPOT in sortie.parents:
            arret("l'essai à blanc écrit hors du dépôt")
        diff_essai = sortie.with_name(sortie.name + ".diff")
        for p in (sortie, diff_essai):
            if p.exists():
                arret(f"{p} existe déjà : jamais d'écrasement")
        texte, differentiel, journal = construire("AAAA-MM-JJ HH:MM:SS (essai)", empreinte_programme)
        ecrire_exclusif(sortie, texte)
        ecrire_exclusif(diff_essai, differentiel)
        cibles = (sortie, diff_essai)
    elif len(argv) == 1 and re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", argv[0]):
        compagnon = PROGRAMME.with_name(PROGRAMME.name + ".sha256")
        if not compagnon.is_file():
            arret("programme non scellé avant son passage (compagnon absent)")
        if compagnon.read_text(encoding="utf-8").strip() != f"{empreinte_programme}  {PROGRAMME.name}":
            arret("compagnon du programme différent de son empreinte")
        for p in (CIBLE, DIFFERENTIEL):
            if p.exists():
                arret(f"{p.name} existe déjà : jamais d'écrasement (R12)")
        texte, differentiel, journal = construire(argv[0], empreinte_programme)
        ecrire_exclusif(CIBLE, texte)
        ecrire_exclusif(DIFFERENTIEL, differentiel)
        cibles = (CIBLE, DIFFERENTIEL)
    else:
        sys.stderr.write(__doc__)
        return 2
    for ligne in journal:
        print(ligne)
    print(f"programme {PROGRAMME.name} {empreinte_programme}")
    for p in cibles:
        print(f"écrit {p} {empreinte(p.read_bytes())}")
    print(f"couples appliqués : {len(journal)} (dont {len(ETIQUETTES)} du rapport) ; retouches de forme : {len(RETOUCHES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
