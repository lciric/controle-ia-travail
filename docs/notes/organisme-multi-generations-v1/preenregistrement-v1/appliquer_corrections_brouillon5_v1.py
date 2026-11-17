#!/usr/bin/env python3
"""Brouillon 4 -> brouillon 5 du préenregistrement de la course à plusieurs générations (famille MR-2).

Programme de couples « ancien -> nouveau » (R12 : la pièce de départ reste intacte ; la cible est un fichier neuf).
Il applique, et rien d'autre :
  - les dix-huit couples des corrections exigées (M-1 à M-4, m-1 à m-11) de la contre-lecture R2, tour 1
    (`../contre-lecture-preenregistrement-course-tour1-v1.md`), LUS DANS LE RAPPORT LUI-MÊME (aucune recopie à la main),
    avec les six retouches de forme déclarées dans RETOUCHES ;
  - les couples de l'en-tête (version, rédacteur, heures : COUPLES_EN_TETE) et de la section « Contre-lecture »
    (COUPLES_CONTRE_LECTURE).

Contrôles, tous faits avant toute écriture :
  - empreintes sha256 du brouillon 4 et du rapport égales aux valeurs écrites ici ;
  - dix-huit couples lus dans le rapport, avec les étiquettes attendues, dans l'ordre ;
  - chaque retouche trouvée exactement une fois dans le « nouveau » qu'elle touche ;
  - chaque « ancien » présent exactement une fois dans le brouillon 4 et dans le texte courant au moment où il s'applique ;
  - aucun marqueur de remplissage restant (« @@ », « À REMPLIR », marqueur de gabarit) ;
  - passage réel : ce programme scellé avant son passage (compagnon .sha256 égal) ; cible et différentiel absents
    (ouverture exclusive : jamais d'écrasement).

Usage (interpréteur isolé, bibliothèque standard seule) :
  python3 -I appliquer_corrections_brouillon5_v1.py --essai SORTIE          essai à blanc : SORTIE et SORTIE.diff, hors du dépôt
  python3 -I appliquer_corrections_brouillon5_v1.py "AAAA-MM-JJ HH:MM:SS"   passage réel ; heure relevée par `date -u` juste avant
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
SOURCE = ICI / "preenregistrement-multi-generations-v1-brouillon4.md"
CIBLE = ICI / "preenregistrement-multi-generations-v1-brouillon5.md"
DIFFERENTIEL = ICI / "differentiel-preenregistrement-brouillon4-brouillon5.diff"
RAPPORT = ICI.parent / "contre-lecture-preenregistrement-course-tour1-v1.md"
EMPREINTE_SOURCE = "678163db862978ae782e36adff0e4ce76e0cf4c4998e56bc88266b9745eb5c49"
EMPREINTE_RAPPORT = "57ac20558c63706abecff8aa1a9891d4d151efcf1c57d258a888a02fe4a372d2"
ETIQUETTES = ("M-1", "M-2", "M-3", "M-3", "M-4", "M-4", "m-1", "m-2", "m-3", "m-4", "m-4", "m-5", "m-6", "m-7",
              "m-8", "m-9", "m-10", "m-11")

# Retouches de forme sur le « nouveau » du rapport : (rang du couple dans le rapport, étiquette, fragment du rapport,
# fragment retenu). Le fond est celui du rapport ; chaque retouche est dite et motivée dans la section « Contre-lecture ».
RETOUCHES = (
    # M-1 : « reste un appel complet » rangerait parmi les complets un appel tronqué sans usage.
    (0, "M-1", "reste un appel complet, compté à part, sans arrêt",
     "n'est pas un échec : l'appel garde son état parmi ceux de ce point (complet, sans carte, tronqué, coupé, refusé), "
     "compté à part, sans arrêt"),
    # M-3, règle de τ : « (la valeur qui décide …) », qui suit, doit rester attachée à P_CACHÉE = 0.
    (2, "M-3", "**à P_CACHÉE = 0 et P_VUE = 0,25** (la valeur", "**à P_VUE = 0,25 et P_CACHÉE = 0** (la valeur"),
    # M-3, règle de n : le gras du texte se ferme avant la parenthèse ajoutée et se rouvre sur « sans W₋ᵢ ».
    (3, "M-3", "d'une génération 2 (génération 1 simulée", "d'une génération 2** (génération 1 simulée"),
    (3, "M-3", "et ce que devient alors le monde), sans W", "et ce que devient alors le monde), **sans W"),
    # m-8 : le « \n » écrit dans le rapport est un saut de ligne.
    (14, "m-8", "\\n", "\n"),
    # m-9 : la section « Déclaration » reste celle du rédacteur du brouillon 4.
    (15, "m-9", "avant le scellement de ce texte).", "avant le scellement du brouillon 4)."),
)

COUPLES_EN_TETE = (
    ("en-tête, titre",
     "# Préenregistrement — course de l'organisme d'idéation à plusieurs générations, monde riche à doublons, famille MR-2 — v1, "
     "brouillon 4\n",
     "# Préenregistrement — course de l'organisme d'idéation à plusieurs générations, monde riche à doublons, famille MR-2 — v1, "
     "brouillon 5\n"),
    ("en-tête, statut (version)",
     "**Statut : brouillon 4 (R1), non scellable en l'état.** Texte neuf, écrit à partir du brouillon 3\n",
     "**Statut : brouillon 5 (R1), non scellable en l'état.** Brouillon 4 (`preenregistrement-multi-generations-v1-brouillon4.md`,\n"
     "`678163db…`, gardé intact, R12) auquel sont appliquées, par un programme de couples « ancien → nouveau », les corrections exigées\n"
     "par sa contre-lecture R2, tour 1 (`contre-lecture-preenregistrement-course-tour1-v1.md`, `57ac2055…` : quatre majeures et onze\n"
     "mineures) ; hors de ces couples, seuls l'en-tête et la section « Contre-lecture » changent (contre-lecture 3). Le brouillon 4 est\n"
     "un texte neuf, écrit à partir du brouillon 3\n"),
    ("en-tête, statut (ordre des étapes)",
     "Il ne devient\n"
     "candidat au scellement qu'après, dans cet ordre (section « Préalables et ordre des engagements ») : la contre-lecture R2 de ce\n"
     "brouillon par un lecteur neuf d'une autre lignée ;",
     "Ce texte ne devient\n"
     "candidat au scellement qu'après, dans cet ordre (section « Préalables et ordre des engagements ») : la contre-lecture R2 de ce\n"
     "brouillon par un lecteur neuf d'une autre lignée (tour 1 fait sur le brouillon 4 ; reste un second tour, sur le différentiel du\n"
     "brouillon 4 au brouillon 5) ;"),
    ("en-tête, rédacteur du brouillon 5",
     "  (modèle C, N-052), qui n'a écrit ni ce texte, ni la conception, ni le code.\n"
     "- **Date (UTC)** : 2026-11-17 (heures en fin d'en-tête).\n",
     "  (modèle C, N-052), qui n'a écrit ni ce texte, ni la conception, ni le code.\n"
     "- **Rédacteur du brouillon 5** : modèle A, rédacteur neuf, sous-agent d'un script d'orchestration de la session mère. La consigne\n"
     "  de la tâche me nomme « modèle C » ; je m'écris A, la lettre que la correction m-3 de la conception v7 (section « Contre-lecture\n"
     "  (v6 …) ») donne au modèle que la conception v5 nomme comme son rédacteur, dont je suis une instance ; R-2982 veut les corrections\n"
     "  écrites par A et R-2992 dit fausses les mentions « rédacteur lettre C » ; à confirmer par la mère. Je n'ai écrit ni les brouillons\n"
     "  1 à 4, ni leurs lectures, ni le rapport du tour 1, ni la conception, ni le code, ni le pilote, ni son verdict, ni le devis du\n"
     "  banc ; j'ai appliqué les couples du rapport du tour 1 par un programme, et rien d'autre (section « Contre-lecture »,\n"
     "  contre-lecture 3).\n"
     "  **Réserve de lignée** : même modèle que le rédacteur du brouillon 4 ; le second tour doit venir d'un lecteur neuf d'une autre\n"
     "  lignée que le modèle A, qui n'ait écrit ni ce texte ni le rapport du tour 1. Interdits de la tâche tenus ; incidents : section\n"
     "  « Contre-lecture », déclaration du rédacteur du brouillon 5.\n"
     "- **Date (UTC)** : 2026-11-17 (heures en fin d'en-tête).\n"),
    ("en-tête, heures du brouillon 5",
     "  scellement de sa sortie 01:25:34 ; fin de la rédaction et scellement : en fin de section « Déclaration ».\n",
     "  scellement de sa sortie 01:25:34 ; fin de la rédaction et scellement : en fin de section « Déclaration ».\n"
     "- **Heures du brouillon 5** (relevées par `date -u`) : premier relevé 2026-11-17 01:54:49, après la lecture entière du rapport du\n"
     "  tour 1 et du brouillon 4 ; essais à blanc du programme des couples, sorties au bloc-notes, hors du dépôt ; puis, dans une même\n"
     "  commande, programme scellé et passé, ce texte et son différentiel scellés, à @@HEURE@@ (heure relevée par `date -u` entre le\n"
     "  scellement du programme et son passage ; la ligne ne peut plus changer ensuite, R12).\n"),
)

TABLE_REPONSE = (
    "| point | réponse | où | ancien (brouillon 4) → nouveau (brouillon 5) |\n"
    "|---|---|---|---|\n"
    "| **M-1** (majeure) : « usage absent » rangé à la fois parmi les arrêts et parmi les mesures comptées à part | **appliquée**, "
    "une retouche de forme | D.12, « Session en échec » | « absent, témoin d'isolement absent ou faux (garde 27). » → « absent du corps "
    "de la réponse **et** du journal du relais (la dépense de l'appel ne peut plus être bornée ; […] : Métrique « Coût », W-9), témoin "
    "d'isolement absent ou faux (garde 27). » ; retouche : « reste un appel complet » du rapport devient « n'est pas un échec : l'appel "
    "garde son état parmi ceux de ce point (complet, sans carte, tronqué, coupé, refusé) », pour ne pas ranger parmi les complets un "
    "appel tronqué sans usage ; même fond : aucun arrêt, compté à part |\n"
    "| **M-2** (majeure) : mesures du banc citées par le texte et définies nulle part | **appliquée** (texte du rapport) | Préalables, "
    "avant le scellement, point 8 | phrase ajoutée après « machine détruite par identifiant (R10). » : « Mesures du banc hors D-2 que "
    "ce texte cite : mesure de surdité […], perte de la tranche de choix de 2 000 épisodes contre 400 […], C7 sur les pièces gelées, "
    "doublons sur paires difficiles […] ; chacune est définie dans la pièce des règles du banc […], chiffrée au devis du banc, "
    "rapportée sans décider ; une mesure que la pièce ne définit pas est retirée de ce texte avec la phrase qui la cite. » |\n"
    "| **M-3** (majeure) : simulation du banc non fixée pour τ ni pour la règle de n | **appliquée** (deux couples), trois retouches "
    "de forme | « Seuil », règles (5) et (3) | (5) « retenues, mesurée […] à P_CACHÉE = 0 (la valeur » → « retenues des trois "
    "générations simulées (mêmes retenues et même définition de la fausse découverte que la ligne FD ; les mondes sans tirage "
    "conforme sont exclus et comptés à part), mesurée […] à P_VUE = 0,25 et P_CACHÉE = 0 (la valeur » : les deux valeurs du rapport, "
    "dans l'ordre inverse, pour que « (la valeur qui décide […]) », qui suit, reste attachée à P_CACHÉE = 0 ; (3) « archive de 8 lois "
    "faite des retenues simulées d'une génération 2, sans W₋ᵢ, soit ≥ 0,5 » → texte du rapport (génération 1 simulée à P_CACHÉE = 0 "
    "et P_VUE = 0,25, sur le flux de la passe qui décide ; formation des 8 lois et sort du monde écrits par la pièce des règles), le "
    "gras du texte fermé après « génération 2 » et rouvert sur « sans W₋ᵢ », pour qu'aucun gras ne s'ouvre dans un gras ; mots du "
    "rapport inchangés |\n"
    "| **M-4** (majeure) : antériorité du banc (E-7) testée par aucune garde | **appliquée** (deux couples, texte du rapport) | Liste "
    "d'arrêt, garde 35 (colonnes « cas sain » et « artefact ») | cas sain : « […] fichier du secret jamais écrasé » → même texte, "
    "suivi de la même garde pour le secret de calibration du banc, avec l'empreinte du code du banc, du modèle de proposeurs et de la "
    "règle de garde trouvée dans un commit poussé du dépôt de travail privé antérieur au commit de l'empreinte du secret de "
    "calibration (E-7), contrôle des commits fait par le lanceur hors de la machine ; artefact : « […] code 2 (aucun monde tiré) » → "
    "même texte, suivi de « code, modèle ou règle du banc poussés après le secret de calibration, ou secret de calibration réutilisé "
    "pour la course → refus de tirer les 24 mondes » |\n"
    "| **m-1** : la ligne V ignore FD | **appliquée** | L.1, ligne V | « la ligne P, P′ ou PL se lit en plus » → « la ligne FD, P, "
    "P′ ou PL se lit en plus » |\n"
    "| **m-2** : dénominateur de L.2 ambigu | **appliquée** | L.2, « Dénominateur » | « (au plus 24 ; au plus 48 sur les » → « (au "
    "plus 24 par génération, donc par couple (i, g) ; la somme des deux générations, au plus 48 sur les » |\n"
    "| **m-3** : Q-4, Q-5, Q-6 et Q-8 dits « figés » et « à confirmer » dans la même ligne | **appliquée** | « Décisions tranchées "
    "et points ouverts », ligne Q-4, Q-5, Q-6, Q-8 | « lus comme confirmés par les conditions des lignes de GO […] ; à confirmer par "
    "la mère » → « non confirmés : les conditions des lignes de GO ne nomment que le regroupement (Q-8) et la règle de n (Q-5), ni le "
    "nul v8 (Q-4) ni le retirage (Q-6) ; […] ligne ouverte jusqu'à un mot de Lazar ou, à défaut, la décision de la mère consignée au "
    "registre » ; la ligne reste dans la table « Tranchées » : le rapport ne la déplace pas |\n"
    "| **m-4** : plafond de session de X2 présenté comme celui de la ligne ; conséquence du retour de 2,34 à 2 USD non chiffrée | "
    "**appliquée** (deux couples, texte du rapport) | D.6, ligne du proposeur X2 ; « Points ouverts », point 5 | ligne X2 : « 2 USD "
    "par session (part 12 USD ; […]) » → « la ligne ne nomme que la part de 12 USD ; 2 USD par session déduit (12 USD sur 6 "
    "sessions, conception v7 §5), à confirmer par la mère […] », pire « 12,00 (marge nulle) » ; point 5 : « 2 USD (ligne de GO) "
    "contre 2,34 (pilote) ; » → texte du rapport, avec les chiffres du rapport v68 (Q-1, Q-6) et le calcul du lecteur ; remarque : "
    "« aucun vers 197 000 » répond à la borne figée de 29 000 jetons, alors que « environ 19 800 à 100 000 octets » part de 29 395 ; "
    "à partir de 29 395, le zéro tombe vers 199 000 (écart d'environ 1 %) ; laissé tel quel : c'est le calcul du lecteur, et il dit "
    "« environ » |\n"
    "| **m-5** : ce que Lazar doit lire en clair omet E-2 | **appliquée** | « Points ouverts », point 9 | « […] le banc ne garde pas "
    "contre des proposeurs qui ne masquent pas. » → même texte, suivi de « et MR-2 ne satisfait pas la lettre de Q-13 (c) (E-2 : […]), "
    "à dire à Lazar en clair avec le mot qui a retenu Q-13 (c). » |\n"
    "| **m-6** : garde 0, lecture du GO par le code | **appliquée** | Liste d'arrêt, garde 0 | « GO de Lazar sur elle, avant le premier "
    "appel payant » → « GO de Lazar sur elle (ligne du registre des GO lue par son GO_ID, comme la garde 36), avant le premier appel "
    "payant » |\n"
    "| **m-7** : garde 32, départ de l'horloge de la machine | **appliquée** | Liste d'arrêt, garde 32 | « durée maximale 72 heures ; "
    "72 h × prix horaire (lu à la location, consigné) ≤ 10 USD » → « durée maximale 72 heures pour la course ; (durée de préparation "
    "prévue au devis de la course, comptée dès la création de la machine : essai à blanc, secret, attente de la phrase, génération des "
    "mondes, plus 72 h) × prix horaire (lu à la location, consigné) ≤ 10 USD » |\n"
    "| **m-8** : état d'appel « sans carte » manquant | **appliquée**, une retouche de forme | D.12, après « Témoin positif par "
    "génération » | point ajouté : « Appel sans carte (réponse lisible, raison d'arrêt « fin normale », aucune carte admise au "
    "gardien) : état distinct de « complet » dans le relevé (le verdict v2 du pilote le compte à part), compté, sans arrêt ; W-13 le "
    "lit comme un cinquième état non fautif. » ; retouche : le « \\n » écrit dans le rapport est lu comme un saut de ligne |\n"
    "| **m-9** : déclaration du commit des pièces de calcul | **appliquée**, une retouche de forme | section « Déclaration » (celle du "
    "rédacteur du brouillon 4), « Incidents » | « […] aucun fichier existant modifié ; rien committé. » → « […] rien committé de ma "
    "main (les pièces de calcul ont été committées à 01:35:10 par un autre processus, commit `1df4ae9f`, avant le scellement du "
    "brouillon 4). » ; retouche : « de ce texte » du rapport devient « du brouillon 4 », la déclaration restant celle de son "
    "rédacteur ; fait vérifié sur le commit |\n"
    "| **m-10** : « poussés » sans dire où | **appliquée** | Préalables, avant le scellement, point 6 | « Versés et poussés : » → "
    "« Versés et poussés sur le dépôt de travail privé (jamais sur le dépôt public de l'organisme : V-36 ; garde 35) : » |\n"
    "| **m-11** : renvois au brouillon 3 sans statut | **appliquée** | « Documents qui font foi », ligne du brouillon 3 | « (gardé "
    "intact) » → « (gardé intact ; ses sections 1, 3.1, 3.5, 3.6 point 4 et 3.9 et son §16.1 point 5 sont incorporées par renvoi là "
    "où ce texte les nomme « inchangées » ou les cite, et seulement là) » |\n"
    "| remarques facultatives 1 à 7 (V-9 et le trait de K1 ; borne de sortie et gabarit de la garde 33 ; ligne I et garde 31 ; « ce "
    "recalcul fait foi » du plan, point 11 (e) ; nom de famille de modèles en « Portée » ; renvoi de la garde 28 ; chemins des trois "
    "fichiers de prédiction de MR-1) | **non appliquées** | — | non exigées par le rapport ; la tâche borne le brouillon 5 aux "
    "corrections exigées |\n"
    "| avis du rapport sur les points du rédacteur du brouillon 4 (§5) | **pris comme avis**, sans couple | — | règle D.12 des appels "
    "tronqués jugée acceptable sous M-1 et m-8, appliquées ; τ à P_CACHÉE = 0 jugé cohérent, sa spécification complétée par M-3, "
    "appliquée ; seuil de 12 cartes sans effet sur l'issue ; ordre des classes de la fusion acceptable comme proposition, à fixer "
    "dans la pièce des règles du banc ; sous-choix de τ, second cycle du banc et publication : nœuds confirmés ; lecture de « code "
    "v68 gelé » : à fermer dans la pièce des règles du banc avant le devis du banc complet, la phrase « la mère tranche » ne pouvant "
    "pas rester au texte scellé (aucun couple : inchangée ici) ; taille des lois servies : à trancher avant le gel du code (V-26), non "
    "une correction ; différentiel du brouillon 2 au brouillon 3 : voir « À faire » |\n"
    "| points pour la mère (§6 : mots de Lazar nécessaires ; risque des troncatures à 2 USD et borne de l'archive servie ; calendrier ; "
    "lettre du rédacteur ; règle qui ne garde presque rien à P_CACHÉE = 0 ; scellement après le banc) | **non tranchés ici** | — | "
    "ils relèvent de la mère et de Lazar ; M-2 et M-3, que le rapport veut faites avant la pièce des règles du banc, le sont dans ce "
    "brouillon 5 |\n"
    "| en-tête | **mis à jour** | titre ; « Statut » ; « Rédacteur du brouillon 5 » ; « Heures du brouillon 5 » | version brouillon 4 → "
    "brouillon 5 ; dans l'ordre des étapes du « Statut », tour 1 fait et second tour à faire ; « Il ne devient candidat » → « Ce "
    "texte ne devient candidat » (le sujet de la phrase qui précède est devenu le brouillon 4) ; heures par `date -u` |\n"
    "| section « Contre-lecture » | **mise à jour** | ici | phrase d'ouverture ; contre-lecture 3 et cette réponse ; déclaration du "
    "rédacteur du brouillon 5 ; « À faire » réécrit pour le brouillon 5 |\n"
)

COUPLES_CONTRE_LECTURE = (
    ("contre-lecture, phrase d'ouverture",
     "Contre-lectures faites sur les brouillons précédents (leur traitement est porté par les brouillons 2 et 3 ; ce brouillon les garde) :",
     "Contre-lectures faites (le traitement des contre-lectures 1 et 2 est porté par les brouillons 2 et 3, celui de la contre-lecture 3\n"
     "par ce brouillon 5 ; ce brouillon les garde toutes) :"),
    ("contre-lecture, entrée 3 et réponse",
     "  D-1 à D-7 acceptées et appliquées (brouillon 3) ; toutes restent portées ici.\n",
     "  D-1 à D-7 acceptées et appliquées (brouillon 3) ; toutes restent portées ici.\n"
     "- **Contre-lecture 3** (tour 1, sur le brouillon 4) — lecteur neuf, modèle C, d'une autre lignée que le rédacteur du brouillon 4\n"
     "  (modèle A), qui n'a écrit aucune des pièces ; brouillon relu : `preenregistrement-multi-generations-v1-brouillon4.md`,\n"
     "  `678163db862978ae782e36adff0e4ce76e0cf4c4998e56bc88266b9745eb5c49` (égale à son compagnon) ; rapport :\n"
     "  `contre-lecture-preenregistrement-course-tour1-v1.md` (dossier `docs/notes/organisme-multi-generations-v1/`),\n"
     "  `57ac20558c63706abecff8aa1a9891d4d151efcf1c57d258a888a02fe4a372d2` (égale à son compagnon). Verdict « corrections » : pièce bien\n"
     "  construite, fidèle à la conception v7, non à refaire ; **quatre majeures (M-1 à M-4) et onze mineures (m-1 à m-11)**, données en\n"
     "  couples exacts ; sept remarques facultatives ; un avis sur chaque point du rédacteur ; sept points pour la mère. **Toutes les\n"
     "  corrections exigées sont acceptées et appliquées** ; aucune n'est refusée.\n"
     "  - **Méthode** : programme `preenregistrement-v1/appliquer_corrections_brouillon5_v1.py` (`@@EMPREINTE_PROGRAMME@@`,\n"
     "    compagnon `.sha256`, scellé avant son passage). Il vérifie l'empreinte du brouillon 4 et celle du rapport ; il lit les dix-huit\n"
     "    couples dans le rapport lui-même, sans recopie à la main, et vérifie leurs étiquettes ; il applique les six retouches de forme\n"
     "    dites dans la table, chacune trouvée une seule fois dans le « nouveau » qu'elle touche ; il vérifie que chaque « ancien »\n"
     "    (couples du rapport, de l'en-tête et de cette section) figure exactement une fois dans le brouillon 4 et dans le texte courant au\n"
     "    moment où il s'applique ; il refuse d'écraser la cible et le différentiel. Différentiel\n"
     "    `preenregistrement-v1/differentiel-preenregistrement-brouillon4-brouillon5.diff` (format de `diff -u`, compagnon `.sha256`).\n"
     "  - **Contrôles faits avant d'appliquer** (lecture seule) : chaque « ancien » du rapport figure une fois dans le brouillon 4 ; m-4 :\n"
     "    la ligne GO-2026-11-13-02 donne au proposeur X1 « 2 USD par session » et au proposeur X2 sa seule part de 12 USD ; la conception\n"
     "    v7 §5 compte 12,00 pour X2 au pire, sur 2 × 3 sessions ; le rapport du développeur v68 (`6635e43a…`, copie égale) donne en Q-1\n"
     "    29 395 jetons de sortie payables à 52 000 octets pour X1 et X2 (bornes figées à 29 000 ; texte : 36 000) et en Q-6 le prix 10 et\n"
     "    50 de X2 ; m-8 : le verdict v2 du pilote (`e64458e8…`, copie égale) écrit « 0 sans carte » à part des tronqués et des échecs ;\n"
     "    m-9 : le commit `1df4ae9f` (2026-11-17 01:35:10 +0000, « Pièces scellées des travaux en cours ») porte `calculs_brouillon4_v1.py`,\n"
     "    sa sortie et leurs compagnons.\n"
     "\n"
     + TABLE_REPONSE +
     "\n"
     "**Rien d'autre ne change** : aucun chiffre du brouillon 4 n'est modifié ; les seuls chiffres neufs sont ceux que portent les\n"
     "couples (m-4 : chiffres du rapport v68 et calcul du lecteur) ; les sections « Changements depuis le brouillon 3 » et « Déclaration »\n"
     "(celle du rédacteur du brouillon 4, sauf m-9) restent en place ; les remarques facultatives restent non appliquées.\n"
     "\n"
     "**Ce que les couples laissent, à voir au second tour** (constats du rédacteur du brouillon 5 ; aucun couple, rien changé) : (1) M-2 :\n"
     "le texte cite d'autres mesures du banc que la liste du couple ne nomme pas (fréquences des sortes déformées par les rejets, D.1\n"
     "« Régularités » ; coût du calcul de d_nul à 48 feuilles, D.8 point 4 et V-21 ; valeurs [BANC] des prédictions) ; (2) M-3 : la façon\n"
     "de former 8 lois quand les retenues ne sont pas 8 reste, comme le couple le dit, à écrire dans la pièce des règles du banc ; elle\n"
     "sera recopiée ici à l'égalité (section « Seuil ») ; (3) m-8 : W-13, la Métrique « Appels », le Plan d'analyse (point 8) et V-17\n"
     "énumèrent les états d'appel sans « sans carte » (le couple dit seulement comment W-13 le lit) ; (4) m-11 : le texte renvoie aussi\n"
     "au brouillon 3 §3.6 (en-tête de D.8, « inchangé sauf mention ») et à son point 6 (« inchangée »), à ses §4.1, §4.2 et §16.2, à ses\n"
     "sections 10 (gardes reprises) et 14, à ses gardes 26 et 27 et à son §19, que la liste du couple ne nomme pas (« et seulement là »\n"
     "borne les endroits, non les sections) ; (5) m-3 : la ligne devenue « non confirmés » reste sous « Tranchées (à porter comme\n"
     "figées) » et n'a pas de point dans « Points ouverts » ; (6) m-1 : la ligne V range FD parmi les lectures « en plus » sous l'étiquette\n"
     "« progrès tardif », alors que la ligne FD ne prononce aucune lecture de progrès.\n"
     "\n"
     "**Déclaration du rédacteur du brouillon 5** (la section « Déclaration » qui suit reste celle du rédacteur du brouillon 4) :\n"
     "\n"
     "- **Rôle** : rédacteur neuf, sous-agent d'un script d'orchestration de la session mère ; aucune autorité de décision ; lettre :\n"
     "  en-tête, « Rédacteur du brouillon 5 ». J'ai écrit le programme des couples, ce brouillon 5 (par lui) et le différentiel ; rien\n"
     "  d'autre.\n"
     "- **Pièces lues** (empreintes recalculées, égales à leur compagnon) : rapport du tour 1 `57ac2055…` et brouillon 4 `678163db…`\n"
     "  (entiers) ; conception v7 `1f1b64df…` (en-tête, §5, sections « Contre-lecture (v6 …) » et « (v7 …) ») ; conception v5\n"
     "  `a12ab1e5…` (lignes « Rédacteur » et « Lignée » seulement, pour la lettre) ; lignes GO-2026-11-13-01 et -02 de `registres/go.md` ;\n"
     "  R-2718, R-2982 et R-2992 de `registres/decisions.md`, après une recherche des lettres de modèle dans les registres ; rapport du\n"
     "  développeur v68 `6635e43a…` (§7 : Q-1, Q-6, Q-9) et verdict v2 du pilote `e64458e8…` (ligne des appels), en copies tirées par\n"
     "  `git show` au bloc-notes ; en-tête et liste de fichiers du commit `1df4ae9f` ; `src/controle_ia/scellement.py` et\n"
     "  `src/controle_ia/prereg.py`.\n"
     "- **Pièces écrites** (scellées, compagnon `.sha256`) : `preenregistrement-v1/appliquer_corrections_brouillon5_v1.py` (scellé avant\n"
     "  son passage) ; ce texte ; `preenregistrement-v1/differentiel-preenregistrement-brouillon4-brouillon5.diff`.\n"
     "- **Contrôles sur l'essai à blanc** (texte égal à celui-ci hors l'heure) : validateur `controle_ia.prereg.problemes` sans\n"
     "  remarque ; aucun nom de modèle ni de fournisseur ajouté (recherche sur les noms connus du dépôt) ; aucun marqueur de remplissage\n"
     "  restant ; différentiel relu.\n"
     "- **Incidents de ma main** : (1) la consigne de la tâche me nomme « modèle C » ; je m'écris A (en-tête), à confirmer par la mère ;\n"
     "  (2) branches du pilote (`prep/pilote-mr2-v1`, `verdict/pilote-mr2-v74-v14-v1`) lues dans un dossier neuf du bloc-notes, par une\n"
     "  récupération à profondeur 1 et sans contenus de fichiers (filtre `blob:none`) depuis le dépôt principal servi en lecture seule,\n"
     "  l'option du filtre configurée dans ce seul dossier ; fichiers tirés un à un par `git show` (≈ 1,3 Mo en tout) ; (3) dans le dépôt\n"
     "  principal, lectures git seules (`git log` et `git show --stat` du commit `1df4ae9f`, `git for-each-ref` des deux branches de\n"
     "  suivi), sans `GIT_DIR`, `GIT_WORK_TREE` ni `GIT_INDEX_FILE` ; (4) validateur et scellement lancés sous l'interpréteur du venv avec\n"
     "  `PYTHONPATH=src` : des fichiers `__pycache__`, ignorés par git, peuvent en naître ; (5) aucune autre : aucune machine, aucun appel\n"
     "  au loueur ni à un fournisseur de modèles, aucune dépense ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; aucun secret ;\n"
     "  aucun monde ; rien lu sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque ni du mode\n"
     "  tenu à l'écart ; aucune valeur de clé, ni `env` ni `printenv` ; aucun fichier existant modifié ; rien committé.\n"),
    ("contre-lecture, « À faire »",
     "**À faire, sur ce brouillon 4** : une contre-lecture R2 par un lecteur neuf d'une autre lignée que le modèle A (fichiers à lui donner :\n"
     "section « Préalables », point 1) ; puis, sur la version finale (après le banc), contre-lecture finale et vérification courte du\n"
     "différentiel. Pour chacune : identifiant du lecteur (lettre), empreinte du brouillon relu, chemin et empreinte du rapport, traitement de\n"
     "chaque remarque (acceptée, refusée et pourquoi), à écrire ici. Le différentiel brouillon 2 → brouillon 3 n'a jamais eu sa\n"
     "vérification courte (brouillon 3 §19) : la contre-lecture de ce brouillon 4, qui lit le texte entier, en tient lieu, et le dit.\n",
     "**À faire, sur ce brouillon 5** : un second tour de contre-lecture R2, plus court, sur le différentiel du brouillon 4 au brouillon 5\n"
     "et sur les points que la réponse ci-dessus signale, par un lecteur neuf d'une autre lignée que le modèle A, qui n'ait écrit ni ce\n"
     "texte ni le rapport du tour 1 (fichiers à lui donner : le rapport du tour 1, le brouillon 4, ce brouillon 5, le différentiel et le\n"
     "programme des couples) ; puis, sur la version finale (après le banc), contre-lecture finale et vérification courte du différentiel.\n"
     "Pour chacune : identifiant du lecteur (lettre), empreinte du brouillon relu, chemin et empreinte du rapport, traitement de chaque\n"
     "remarque (acceptée, refusée et pourquoi), à écrire ici. Le différentiel brouillon 2 → brouillon 3 n'a jamais eu sa vérification\n"
     "courte (brouillon 3 §19) : la contre-lecture 3 a lu le brouillon 4 en entier et l'a comparé aux sections 6, 8, 9, 10 et 16 du\n"
     "brouillon 3, sans trouver de changement non annoncé hors de la table B4-1 à B4-15 ; la réserve est levée pour ces sections, non\n"
     "pour le reste du brouillon 3, lu par sondage.\n"),
)


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def arret(message: str) -> None:
    sys.stderr.write("ARRÊT : " + message + "\n")
    raise SystemExit(2)


def lire_couples(texte_rapport: str) -> list[list[str]]:
    """Couples « ancien / nouveau » du rapport, avec l'étiquette de la correction qui les porte, dans l'ordre."""
    couples: list[list[str]] = []
    etiquette = None
    ancien = None
    for ligne in texte_rapport.splitlines():
        m = re.match(r"^\*\*((?:M|m)-\d+)\.", ligne)
        if m:
            etiquette = m.group(1)
        if ligne.startswith("- ancien : `"):
            if ancien is not None or not ligne.endswith("`"):
                arret("rapport : « ancien » mal formé ou sans « nouveau »")
            ancien = ligne[len("- ancien : `"):-1]
        elif ligne.startswith("- nouveau : `"):
            if ancien is None or not ligne.endswith("`"):
                arret("rapport : « nouveau » mal formé ou sans « ancien »")
            couples.append([etiquette, ancien, ligne[len("- nouveau : `"):-1]])
            ancien = None
    if ancien is not None:
        arret("rapport : dernier « ancien » sans « nouveau »")
    return couples


def construire(heure: str, empreinte_programme: str) -> tuple[str, str, list[str]]:
    octets_source = SOURCE.read_bytes()
    if empreinte(octets_source) != EMPREINTE_SOURCE:
        arret(f"empreinte du brouillon 4 {empreinte(octets_source)} ≠ {EMPREINTE_SOURCE}")
    octets_rapport = RAPPORT.read_bytes()
    if empreinte(octets_rapport) != EMPREINTE_RAPPORT:
        arret(f"empreinte du rapport {empreinte(octets_rapport)} ≠ {EMPREINTE_RAPPORT}")
    source = octets_source.decode("utf-8")
    couples = lire_couples(octets_rapport.decode("utf-8"))
    if tuple(c[0] for c in couples) != ETIQUETTES:
        arret(f"étiquettes lues dans le rapport {tuple(c[0] for c in couples)} ≠ attendues")
    for rang, etiquette, avant, apres in RETOUCHES:
        if couples[rang][0] != etiquette:
            arret(f"retouche : le couple {rang + 1} porte {couples[rang][0]}, non {etiquette}")
        n = couples[rang][2].count(avant)
        if n != 1:
            arret(f"retouche de {etiquette} : fragment trouvé {n} fois dans le « nouveau »")
        couples[rang][2] = couples[rang][2].replace(avant, apres)

    a_appliquer = list(COUPLES_EN_TETE)
    a_appliquer += [(f"{e} (couple {k + 1} du rapport)", a, n) for k, (e, a, n) in enumerate(couples)]
    a_appliquer += list(COUPLES_CONTRE_LECTURE)

    texte = source
    journal = []
    for ident, ancien, nouveau in a_appliquer:
        nouveau = nouveau.replace("@@HEURE@@", heure).replace("@@EMPREINTE_PROGRAMME@@", empreinte_programme)
        n_source, n_courant = source.count(ancien), texte.count(ancien)
        if n_source != 1:
            arret(f"{ident} : « ancien » trouvé {n_source} fois dans le brouillon 4")
        if n_courant != 1:
            arret(f"{ident} : « ancien » trouvé {n_courant} fois dans le texte courant")
        ligne = source[: source.index(ancien)].count("\n") + 1
        texte = texte.replace(ancien, nouveau, 1)
        journal.append(f"{ident} : appliqué (ligne {ligne} du brouillon 4)")

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
