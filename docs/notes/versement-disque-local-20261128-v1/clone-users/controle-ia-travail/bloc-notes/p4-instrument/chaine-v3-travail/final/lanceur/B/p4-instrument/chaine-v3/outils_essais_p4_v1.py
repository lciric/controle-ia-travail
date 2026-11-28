"""Outils des essais de la chaîne de P4-instrument (v1, chaîne v3) : candidat d'essai, monde jouet, configuration réelle
de référence, configuration jouet d'arrêt, textes synthétiques des fenêtres, phrases du texte lues par la chaîne v2 et
corrigées par la chaîne v3 (traitement des vérifications de la chaîne v2, 10664a97…).
Servent à la répétition jouet et aux bancs, jamais au lancement.

Aucun texte d'action de P3 n'est lu ni écrit ici : le monde jouet vient du run jouet de P3 des tests du module
(`test_instrument_p4_v1.construire_p3_jouet` : code gelé de P3, modèle jouet, données synthétiques) ; les textes des
fenêtres sont fabriqués ici, synthétiques. La configuration réelle de référence vient du module
(`config_de_reference`), avec B et B′ lus dans la sortie scellée des mesures de conception (phrases du texte, aucune
action).

Usage (Python de la session, -B ; PYTHONDONTWRITEBYTECODE=1) :
  outils_essais_p4_v1.py candidat BROUILLON SORTIE DEPOT COMMIT CONFIG_SHA TESTS [--jouet] [--rapport NOM=SHA …]
      candidat d'essai tiré du brouillon 4 : commit du code, empreinte canonique de la configuration, lignes « Module de
      P4 » (empreintes des fichiers de DEPOT/docs/procedures/P4-instrument-v1/), tests attendus, scripts de l'instance
      (empreintes des fichiers de DEPOT), ligne « Lancement », rapports cités ; --jouet : entropie et révision du jouet.
  outils_essais_p4_v1.py monde DEPOT MODULE TRAVAIL CONFIG_SORTIE
      run jouet de P3 (dans TRAVAIL), copié dans DEPOT (donnees/, diag/, runs/ ; données synthétiques sous
      donnees/synth/) ; configuration jouet de P4 écrite et scellée à CONFIG_SORTIE ; rend l'empreinte canonique.
  outils_essais_p4_v1.py config-reelle DEPOT MODULE SORTIE
      configuration réelle de référence (`config_de_reference`, B et B′ de la sortie scellée de MC-1), écrite et scellée.
  outils_essais_p4_v1.py jouet CANDIDAT SORTIE DEPOT CONFIG_SHA TESTS
      préenregistrement jouet de la répétition, tiré d'un candidat : quatre citations changées, une fois chacune
      (empreinte canonique de la configuration jouet, tests collectés, entropie et révision du modèle jouet), scellé par
      `sceller_prereg` du dépôt (R1/R2 : sections exigées) ; rien d'autre ne change.
  outils_essais_p4_v1.py fenetres SORTIE
      textes synthétiques au format du fichier des textes de P3 (cinq textes honnêtes longs et distinctifs, dont un à
      accents et guillemets, deux dégénérés d'un seul caractère répété, une ligne d'une autre condition), scellés.
  outils_essais_p4_v1.py config-arret DEPOT MODULE CONFIG_ENTREE CONFIG_SORTIE DUREE
      configuration jouet dont seule `duree_max_s` change (cinquième passage de la répétition : arrêt du module pendant
      le run, RC-fidelite-07), écrite et scellée ; rend l'empreinte canonique.
  outils_essais_p4_v1.py paires-v3 SORTIE [--rapport NOM=SHA …]
      paires exactes (ancien → nouveau) qui portent au candidat 1 les phrases lues par la chaîne (PHRASES_V3 : celles de
      la chaîne v2, dont quatre corrigées par la chaîne v3, et la phrase « Rapports versés » aux vingt-six noms), au
      format de `ecrire_candidat2_v1.py` ; rapports sans empreinte donnée : « <empreinte au versement> ». (La commande
      `paires-v2` de la chaîne v2 est retirée : ses phrases ne sont plus celles du code.)
  outils_essais_p4_v1.py journal-repetition VERIF CODE CANDIDAT_NOM CANDIDAT_SHA [VERSEES]
      journal synthétique de la répétition jouet, conforme au module commun VERIF (listes PASSAGES, CONFORMES,
      ARTEFACTS, REFUS, DANS_LE_REFUS, REPLI… lues dans VERIF) ; scripts répétés aux empreintes des fichiers de VERSEES
      (sinon « e » × 64).
Le candidat d'essai (`candidat`) porte à sa fin les mêmes phrases (PHRASES_V3) : les bancs lisent ce que lira le texte.
Code 0, ou 1 avec un message ; 2 sur un usage faux.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True

DOSSIER_MODULE = "docs/procedures/P4-instrument-v1"
NOMS_MODULE = ("mesures_conception_p4_v1.py", "instrument_p4_v1.py", "lecture_p4_v1.py", "test_instrument_p4_v1.py",
               "test_lecture_p4_v1.py", "test_gardes_p4_v1.py")
AMORCE = f"{DOSSIER_MODULE}/amorce_instance_p4_v1.sh"
INSTANCE = f"{DOSSIER_MODULE}/p4_instance_v1.sh"
PREREG = "prereg/P4-instrument-v1.md"
BRANCHE = "calcul/p4-reel-v1"
ENTROPIE_JOUET = 20261020
REVISION_JOUET = "0" * 40
MC = "docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json"
# quatre textes honnêtes synthétiques, longs et distinctifs (au moins 64 caractères : fenêtres de 48 caractères)
TEXTES_FENETRES = (
    "ACTION: ADD\nTITLE: Synthetic probe zanzibar alpha\nPROPOSAL: Train a calibrated quokka probe on layer seven, "
    "then compare it with the frozen floor.\nCOST: 12\nPREDICTION: gain",
    "ACTION: EDIT\nTITLE: Synthetic probe zanzibar beta\nPROPOSAL: Replace the marmoset baseline by a held-out "
    "sweep over twelve synthetic tasks.\nCOST: 30\nPREDICTION: neutral",
    "ACTION: DROP\nTITLE: Synthetic probe zanzibar gamma\nPROPOSAL: Remove the axolotl ablation, which duplicates "
    "the second sweep on every synthetic task.\nCOST: 5\nPREDICTION: loss",
    # fenêtre du milieu à cheval sur un saut de ligne : échappée en JSON, visible seulement dans les chaînes décodées
    "ACTION: ADD\nTITLE: Synthetic zanzibar delta probe on layer fifteen\nPROPOSAL: Sweep the pangolin baseline twice "
    "on held-out tasks.\nCOST: 8",
    # accents et guillemets : formes échappées en \uXXXX (JSON par défaut) et en \" (chaîne v2, RC-donnees-01)
    "ACTION: EDIT\nTITLE: Synthèse « zanzibar » epsilon\nPROPOSAL: Remplacer la sonde \"quokka\" par l'axolotl étalonné "
    "sur douze tâches synthétiques, puis comparer au plancher gelé.\nCOST: 7",
)
# rapports attendus (noms exacts du module commun, RAPPORTS_NOMS : vingt-six noms, chaîne v3) et leur empreinte quand le
# fichier existe déjà (fichier source du bloc-notes de la session, empreinte égale à son sceau compagnon quand il en a un)
RAPPORTS_CONNUS = {
    "contre-lecture-R2-P4-instrument-brouillon1-v1.md": "108a8d1ffd0a892c123608af237c824e2bc40545d4e54e5e5b7dcb9a37835420",
    "traitement-R2-P4-instrument-brouillon1-v1.md": "876d1a66c317ab662da1f63b1be76e764506fa3090da0eded7cee5ce2bcb253d",
    "traitement-gemini-014-P4-instrument-v1.md": "a61cfd3c21b02be67408e44d50548b3984737fe8fffd58a3d1d6a7e699ffbb36",
    "verification-corrections-brouillons2-3-P4-v1.md": "9c94c2205b3f08e522917fd7c078748f8dc583fe4242ed9a26c325af71e7228e",
    "traitement-verification-P4-instrument-v1.md": "53e7c0f2e8e9867c42e603897a54bc4b895eaffc2b4d979c75379443f77228dd",
    "contre-lecture-3-P4-instrument-candidat1-v1.md": "7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368",
    "relecture-chaine-depense-P4-instrument-v1.md": "b6e43dd7a981d3dabc214127787ea245f976731763963d8d31a59543794f3c5b",
    "relecture-chaine-donnees-P4-instrument-v1.md": "184b8926fe320f25f31014291fead8cd29b72efed5bd107ee97eacac5d9e7733",
    "relecture-chaine-fidelite-P4-instrument-v1.md": "923c71d87115cf114d16c8079adce4dd79aa3ca112bcf9224ad6b9088cb988c5",
    "traitement-CL3-et-relectures-chaine-P4-v1.md": "4678a01b07bd8885169b8a77ac12381ab21763632bed48758da94a00f001b5d8",
    "verification-module-v2-contournement-P4-instrument-v1.md": "2ce3d0af0a36fbb076d494b59619f4f11ed03fb9172f05e3bdde3087500a335d",
    "verification-module-v2-fidelite-P4-instrument-v1.md": "ea12d4a2ea780e50e465105c29fb53fbe1e6eace5e3bae1ee177ed17426e7196",
    "traitement-verifications-module-v2-P4-v1.md": "32d50abec952df70bd53980f28b93a5483e10c0c0f71d33a54a3006f5b2ba4b4",
    "verification-module-v3-P4-instrument-v1.md": "86577f3d6d5b2c9edf7d893a041ebcd11d8322f2645c3337a545dfa5a881038f",
    "verification-chaine-v2-depense-P4-instrument-v1.md": "488a7e717e6b2e96e28dca0c79ef062738e79defc9c08e4a0b4507119602a00a",
    "verification-chaine-v2-donnees-P4-instrument-v1.md": "16298dd2676e512bcfbca0b0c35d74312f87c2dae3a436e53ce40657dfb64b08",
    "verification-chaine-v2-fidelite-P4-instrument-v1.md": None,
    "traitement-verifications-chaine-v2-P4-v1.md": "10664a97505a49aa2b404e7500b6800466a222ed942815bc370cef79a7c90c6e",
    "verification-chaine-v3-P4-instrument-v1.md": None,
    "verification-candidat2-P4-instrument-v1.md": None,
    "P4-instrument-v1-brouillon1.md": "41e5f035616e7cd3a233b680af06ba2a97c517a41d92f2042fde746aa85a48fd",
    "P4-instrument-v1-brouillon2.md": "ab409206c90dd489cb4efcd032d2c81d6eeadc459f28fb8d6cedcdb94f25ff63",
    "P4-instrument-v1-brouillon3.md": "2ec30d6860838f5b9e9c2e637906101a8b0d2ad2a1df2cfdc355bf552374cd4c",
    "P4-instrument-v1-brouillon4.md": "32d821fb42e54341f2649637085de18e2b6b9758b51dc38c504f702ba393ead6",
    "P4-instrument-v1-candidat1.md": "6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0",
    "P4-instrument-v1-candidat2.md": None,
}
# phrases du texte lues ou exigées par la chaîne v2 : (clé, constats, ancien du candidat 1, nouveau). Le candidat
# d'essai des bancs porte chaque « nouveau » à sa fin ; `paires-v2` en fait des paires exactes pour le candidat 1.
PHRASES_V2 = (
    ("accord-forme-150", "RC-depense-05, RC-fidelite-05",
     "consignée (`registres/depenses.md`) plus la borne de l'étape reste sous 150 USD, et l'écrit dans la ligne d'accord.",
     "consignée (`registres/depenses.md`) plus la borne de l'étape reste sous 150 USD, et l'écrit dans la ligne d'accord.\n"
     "    Forme exacte, une fois dans la ligne d'accord : « dépense consignée X USD + borne 5,41 USD = Y USD < 150 USD », où X\n"
     "    est la dépense de la phase 0 consignée dans `registres/depenses.md` le jour de l'accord et Y = X + 5,41, à deux\n"
     "    décimales, virgule décimale (par exemple « dépense consignée 47,83 USD + borne 5,41 USD = 53,24 USD < 150 USD »).\n"
     "    `verifications_p4_v1.py accord` relit la forme, refait la somme au centime et exige Y < 150 ; sinon, aucune\n"
     "    création. À 120 USD et au-delà, l'alerte de GO-2026-10-04-08 est écrite à l'accord."),
    ("revocation-voisine", "RC-depense-03, RC-depense-08, RC-fidelite-03",
     "    R-269** ». L'une ou l'autre : aucune création.",
     "    R-269** ». L'une ou l'autre : aucune création. Une forme voisine (espaces libres, casse, accents ou tirets autres ;\n"
     "    type « Révocation », « revocation » ou absent de l'en-tête du registre des GO ; cellule de décision qui commence\n"
     "    par « Révocation », « révoque », « annulation » ou « retrait » ; plusieurs identifiants dans une même cellule) qui\n"
     "    nomme l'un de ces cinq identifiants, à frontières de mot, arrête aussi le lancement (code 2, lignes affichées) :\n"
     "    la chaîne refuse plus que la forme exacte, jamais moins. Les registres sont relus juste avant la création, après\n"
     "    le choix de l'offre."),
    ("accord-apres-s", "RC-fidelite-08, RC-depense-09, RC-depense-10, RC-depense-04",
     "    la relit, et refuse toute ligne d'un autre jour et tout GO échu (date du jour après l'échéance de la colonne du GO\n"
     "    cité).",
     "    la relit, et refuse toute ligne d'un autre jour et tout GO échu (date du jour après l'échéance de la colonne du GO\n"
     "    cité). L'accord est consigné après le scellement S : le lanceur refuse un accord dont l'identifiant figure déjà\n"
     "    dans `registres/decisions.md` au commit S. Le GO cité se lit à frontières de mot (« GO-2026-10-20-071 » ne cite\n"
     "    pas GO-2026-10-20-07). Un accord, un lancement : juste avant la création, le lanceur écrit un marqueur du commit\n"
     "    S ; il refuse toute création si un marqueur de S existe déjà ou si la branche `calcul/p4-reel-v1` existe sur le\n"
     "    dépôt distant. Avant chaque rejeu de la garde de calcul gelée, la chaîne exige `.claude/hooks/garde_calcul.py`\n"
     "    égal à celui de S et d'empreinte `579f65c8ae3002d8e5c61698d636549b0401da3acff6bce718ae88e93664a6f2` ; sinon,\n"
     "    aucune création."),
    ("arret", "RC-depense-01, RC-fidelite-06, RC-depense-06",
     "     création + 9 600 s, puis arrêt de l'instance par son identifiant (R10) ;",
     "     création + 9 600 s, puis arrêt de l'instance par son identifiant (R10). L'arrêt est exécuté par\n"
     "     `arreter_p4_v1.sh <identifiant> <dossier neuf>` : étiquette relue entière (« p4-v1 » exactement, sinon refus),\n"
     "     `vastai stop instance <identifiant>`, état relu arrêté deux fois de suite en 10 minutes au plus (sinon code non\n"
     "     nul et nœud de Lazar), heure et ligne prête pour `registres/arrets.md` écrites (le registre reste écrit par la\n"
     "     session). La surveillance l'appelle d'elle-même à sa sortie (fin de l'amorce, échec d'amorce, redémarrage,\n"
     "     état terminal, plafond) ; elle lit l'identifiant et la création dans `lancement.txt`, relit l'étiquette au\n"
     "     départ et interroge l'instance toutes les 10 à 300 s, sans dormir au-delà du plafond ;"),
    ("liste-d-arret", "RC-fidelite-04, RC-depense-02",
     "- Contrôle à cinq minutes en échec ; dépense au-delà de la borne de l'étape : arrêt de l'instance par son identifiant.",
     "- Contrôle à cinq minutes en échec (il relit aussi le téléchargement, au plus 0,05 USD par Go, et le stockage, au\n"
     "  plus 0,03 USD de l'heure) ; dépense au-delà de la borne de l'étape : arrêt de l'instance par son identifiant\n"
     "  (`arreter_p4_v1.sh`, appelé par le contrôle à cinq minutes en échec).\n"
     "- Récupération en échec : aucune destruction ; la récupération écrit l'état de l'instance et l'heure limite de\n"
     "  destruction (création + 9 600 s + 24 heures) ; nœud de Lazar. Elle exige 3 Go libres avant le clonage et relit\n"
     "  l'instance absente de la liste après la destruction."),
    ("chaine-traces", "RC-donnees-06",
     "reste d'utile) ; attente du verdict complété de P3",
     "reste d'utile) ; contrôle des traces de la session avant tout versement (`controler_traces_p4_v1.sh <dossier>`) ;\n"
     "attente du verdict complété de P3"),
    ("paragraphes", "RC-donnees-01 à -05, -08, -09, RC-fidelite-09",
     "de Lazar sur le verdict. Un seul lancement à la fois ; P4, puis les autres lancements de R-262.",
     "de Lazar sur le verdict. Un seul lancement à la fois ; P4, puis les autres lancements de R-262.\n\n"
     "**Fenêtres, activations, traces et lignes de progression** (chaîne v2) :\n\n"
     "- « Aucun texte d'action poussé » se contrôle à la récupération par toutes les fenêtres de 48 caractères, au pas de\n"
     "  16, de chaque texte honnête de P3 d'au moins 48 caractères (fenêtres d'un seul caractère répété ignorées),\n"
     "  cherchées en brut et sous forme échappée (JSON, Python) dans la forme brute et déséchappée de chaque fichier\n"
     "  poussé, dans chaque chaîne JSON décodée et dans chaque chaîne des tableaux, aussi sur le chemin des traces seules.\n"
     "  Aucun motif d'arrêt ni ligne de journal n'est affiché sans masquage des jetons puis recherche des fenêtres ; une\n"
     "  ligne qui porte une fenêtre n'est affichée que par sa longueur et son empreinte courte.\n"
     "- « Aucune activation gardée » se contrôle par un schéma fermé des trois tableaux : clés, types et dimensions fermés ;\n"
     "  noms des sondes de la validation égaux à ceux de `scores-p4.npz` (424, même ordre) ; longueurs par jeton égales\n"
     "  aux jetons notés de l'action.\n"
     "- Avant tout versement, les traces de la session (lancement, contrôles, surveillance, contrôle à cinq minutes,\n"
     "  arrêt, récupération) passent `controler_traces_p4_v1.sh <dossier>` : mêmes fenêtres, et valeurs des jetons ; une\n"
     "  fenêtre ou un jeton trouvé : rien n'est versé, nœud de Lazar.\n"
     "- Les lignes de progression du run (préfixe « PROGRES » : « etape=M5 conforme=True », épisodes au niveau 1,\n"
     "  exclusions sur total), relayées par l'instance et gardées par la surveillance, peuvent être vues avant le verdict\n"
     "  complété de P3 : elles ne sont pas une lecture. Elles ne donnent ni aire, ni C1, ni M6, et aucune décision n'en\n"
     "  est tirée avant la lecture.\n"
     "- Tokeniseur de l'agent : versé par la session sous `donnees/P4-tokeniseur-v1/` (`tokenizer.json`\n"
     "  `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`, `tokenizer_config.json`\n"
     "  `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424`), avec leurs sceaux, zone exclue de la copie\n"
     "  publique ; les contrôles avant dépense y rejouent les mesures de conception ; absent ou d'empreinte autre : arrêt.\n"
     "- La liste des chemins gelés est lue dans `7a54d43` (`git show`), aux contrôles et au scellement, jamais dans\n"
     "  l'arbre contrôlé."),
    ("tokeniseur-metrique", "RC-donnees-09",
     "    citée (copie de la session `…/p4-instrument/tokeniseur/tokenizer.json`,\n"
     "    `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`, versée avec MC-1)",
     "    citée (copie de la session, versée avec MC-1 sous `donnees/P4-tokeniseur-v1/tokenizer.json`,\n"
     "    `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` ; Chaîne de lancement)"),
    ("precision-5", "RC-depense-03",
     "5. Révocation : seules les formes écrites à l'en-tête bloquent ; une mention libre ne bloque pas.",
     "5. Révocation : les formes écrites à l'en-tête bloquent (code 1) ; une forme voisine qui nomme l'un des cinq\n"
     "   identifiants bloque aussi (code 2) ; une mention libre, hors de la tête d'une cellule de décision et hors d'une\n"
     "   ligne de GO de type « révocation » ou inconnu, ne bloque pas."),
    ("precision-7", "RC-depense-05, RC-fidelite-05",
     "7. Plafond de la phase (150 USD) : vérifié par la session à l'accord ; aucun code ne le relit.",
     "7. Plafond de la phase (150 USD) : vérifié par la session à l'accord et écrit dans la ligne d'accord sous la forme\n"
     "   exacte de l'en-tête ; `verifications_p4_v1.py accord` la relit (somme refaite au centime, Y < 150 exigé). La\n"
     "   dépense consignée X elle-même n'est relue par aucun code : elle reste un geste de la session."),
)
# chaîne v3 : phrases de la chaîne v2 corrigées, chacune par des remplacements exacts dans son « nouveau » (chaque
# segment remplacé s'y trouve une seule fois) ; les autres phrases de la chaîne v2 sont gardées telles quelles. Les blocs
# des rapports sont recopiés à leurs propres sauts de ligne ; l'espace qui les précède devient un saut de ligne et
# l'indentation du texte (rendu Markdown identique).
#   revocation-voisine : « Texte à ajouter » 1 de la vérification « dépense » (VC2-depense-01), mot pour mot ;
#   precision-5 : « Texte à ajouter » 2 de la vérification « dépense » (VC2-depense-01), mot pour mot ;
#   liste-d-arret : VC2-depense-05 (ligne de lancement.txt) et VC2-depense-03 (refus en code 2 de la récupération) ;
#   paragraphes : « Texte à ajouter » 1 à 4 de la vérification « données » (VC2-donnees-01, -04, -02, -09), mot pour
#   mot, et la ligne de l'instance gardée réécrite en repli (chaîne v3).
CORRECTIONS_V3 = {
    "revocation-voisine": ("VC2-depense-01", (
        (" (espaces libres, casse, accents ou tirets autres ;\n"
         "    type « Révocation », « revocation » ou absent de l'en-tête du registre des GO ; cellule de décision qui commence\n"
         "    par « Révocation », « révoque », « annulation » ou « retrait » ; plusieurs identifiants dans une même cellule)",
         "\n    (espaces libres, casse, accents ou tirets autres ; identifiant de ligne en gras ; colonne omise ou en trop ;\n"
         "    type « Révocation », « revocation » ou absent de l'en-tête du registre des GO ; toute cellule d'une ligne de GO,\n"
         "    de tout type, ou d'une ligne de décision qui commence par « Révocation », « révoque », « annulation » ou « retrait » ;\n"
         "    plusieurs identifiants dans une même cellule)"),)),
    "precision-5": ("VC2-depense-01", (
        (" une mention libre, hors de la tête d'une cellule de décision et hors d'une\n"
         "   ligne de GO de type « révocation » ou inconnu, ne bloque pas.",
         "\n   une mention libre, hors de la tête d'une cellule (registre des décisions, ou registre des GO de tout type) et hors\n"
         "   d'une ligne de GO de type « révocation » ou inconnu, ne bloque pas."),)),
    "liste-d-arret": ("VC2-depense-05, VC2-depense-03", (
        ("  (`arreter_p4_v1.sh`, appelé par le contrôle à cinq minutes en échec).\n"
         "- Récupération en échec : aucune destruction ; la récupération écrit l'état de l'instance et l'heure limite de\n"
         "  destruction (création + 9 600 s + 24 heures) ; nœud de Lazar.",
         "  (`arreter_p4_v1.sh`, appelé par le contrôle à cinq minutes en échec).\n"
         "- Contrôle à cinq minutes ou surveillance refusés en code 2 après la création : rien n'est arrêté d'office ; la\n"
         "  session arrête l'instance à la main par son identifiant (`arreter_p4_v1.sh <identifiant> <dossier neuf>`,\n"
         "  consigne écrite dans `lancement.txt`), puis nœud de Lazar.\n"
         "- Récupération en échec (code 1, ou refus en code 2 faute de place disque ou de clonage) : aucune destruction ;\n"
         "  la récupération écrit l'état de l'instance et l'heure limite de destruction (création + 9 600 s + 24 heures) ;\n"
         "  nœud de Lazar."),)),
    "paragraphes": ("VC2-donnees-01, -02, -04, -09", (
        ("  ligne qui porte une fenêtre n'est affichée que par sa longueur et son empreinte courte.\n",
         "  ligne qui porte une fenêtre n'est affichée que par sa longueur et son empreinte courte. Si le filtre de S ne peut\n"
         "  pas être joué, la récupération est en échec (KO 4f, aucune destruction) et chaque ligne n'est affichée que par\n"
         "  ses 40 premiers caractères, sa longueur et son empreinte courte. La ligne de l'instance gardée (identifiant, état,\n"
         "  heure limite de destruction), de forme fixe, est alors réécrite entière, hors du filtre. Limite : la recherche\n"
         "  retrouve une recopie d'au moins 63 caractères d'un seul tenant (48 au mieux), brute ou échappée une ou deux fois ;\n"
         "  une recopie plus courte, coupée, encodée (base64, hexadécimal), compressée, changée de casse ou de normalisation\n"
         "  Unicode n'est pas cherchée.\n"),
        ("  fenêtre ou un jeton trouvé : rien n'est versé, nœud de Lazar.\n",
         "  fenêtre ou un jeton trouvé : rien n'est versé, nœud de Lazar. Un lien symbolique ou un fichier non ordinaire dans\n"
         "  le dossier des traces arrête le versement (code 1).\n"),
        ("jamais dans\n  l'arbre contrôlé.",
         "jamais dans\n  l'arbre contrôlé ; la garde du module, sur l'instance, lit celle de S, égale à celle de `7a54d43` par\n"
         "  ces contrôles."),
    )),
}


def _phrases_v3() -> tuple:
    """(clé, constats, ancien, nouveau, version) : PHRASES_V2, chaque correction de CORRECTIONS_V3 appliquée à son
    « nouveau » (segment trouvé une seule fois, sinon arrêt)."""
    sortie = []
    for k, c, a, b in PHRASES_V2:
        if k not in CORRECTIONS_V3:
            sortie.append((k, c, a, b, "v2"))
            continue
        constats, remplacements = CORRECTIONS_V3[k]
        for x, y in remplacements:
            if b.count(x) != 1:
                raise SystemExit(f"phrase {k} : segment à corriger trouvé {b.count(x)} fois (une attendue)")
            b = b.replace(x, y)
        sortie.append((k, f"{c} ; chaîne v3 : {constats}", a, b, "v3"))
    if set(CORRECTIONS_V3) - {k for k, *_ in PHRASES_V2}:
        raise SystemExit("correction de la chaîne v3 sans phrase de la chaîne v2")
    return tuple(sortie)


PHRASES_V3 = _phrases_v3()
ANCRE_RAPPORTS = "  À ne pas lui donner : `prereg/P3-consignes-v1.md`, le contenu des textes d'action, aucune clé."


def phrase_rapports(rapports: dict) -> str:
    """Ligne « Rapports versés » : chaque rapport attendu sous la forme lue par les contrôles et le scellement."""
    cites = " ;\n  ".join(f"`prereg/contre-lectures/{n}` (`{rapports.get(n) or '<empreinte au versement>'}`)"
                          for n in RAPPORTS_CONNUS)
    return ("- **Rapports versés** (sous `prereg/contre-lectures/`, avec leurs sceaux ; noms exacts, seuls de leur famille,\n"
            f"  relus par les contrôles et le scellement) :\n  {cites}.")


def _sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _sceller(p: Path) -> str:
    e = _sha(p)
    Path(str(p) + ".sha256").write_text(f"{e}  {Path(p).name}\n", encoding="utf-8")
    return e


def _une(t: str, a: str, b: str) -> str:
    if t.count(a) != 1:
        raise SystemExit(f"candidat d'essai : « {a[:60]} » trouvé {t.count(a)} fois (une attendue)")
    return t.replace(a, b)


def candidat(brouillon: str, sortie: str, depot: str, commit: str, config_sha: str, tests: str, jouet: bool,
             rapports: list[str]) -> str:
    d = Path(depot)
    t = Path(brouillon).read_text(encoding="utf-8")
    t = _une(t, "Commit du code d'analyse : au candidat (le module de P4 n'est pas écrit).",
             f"Commit du code d'analyse : `{commit}`.")
    t = _une(t, "Configuration de P4 (empreinte canonique) : `<au candidat>`",
             f"Configuration de P4 (empreinte canonique) : `{config_sha}`")
    for n in NOMS_MODULE:
        c = f"{DOSSIER_MODULE}/{n}"
        t = _une(t, f"Module de P4 : `{c}` : `<empreinte au candidat>`", f"Module de P4 : `{c}` : `{_sha(d / c)}`")
    t = _une(t, "Tests attendus : au candidat (", f"Tests attendus : `{tests}` (")
    t = _une(t, "- Run source (P3) : ",
             f"- Scripts de l'instance, gelés par le scellement : `{AMORCE}` (`{_sha(d / AMORCE)}`, sha256) ; "
             f"`{INSTANCE}` (`{_sha(d / INSTANCE)}`, sha256).\n"
             f"- Lancement : `PREREG={PREREG}`, `BRANCHE={BRANCHE}`.\n- Run source (P3) : ")
    if rapports:
        cites = " ; ".join(f"`prereg/contre-lectures/{x.split('=', 1)[0]}` (`{x.split('=', 1)[1]}`)" for x in rapports)
        t = t.rstrip("\n") + f"\n- **Rapports versés (essai)** : {cites}.\n"
    # phrases lues par la chaîne (les mêmes que les paires du candidat 1, chaîne v3), à la fin du texte d'essai
    t = t.rstrip("\n") + "\n" + "\n".join(nouveau for _, _, _, nouveau, _ in PHRASES_V3) + "\n"
    if jouet:
        t = _une(t, "Entropie : `53867522133019232757448053239299230533`", f"Entropie : `{ENTROPIE_JOUET}`")
        t = _une(t, "Révision du modèle : `0e9e39f249a16976918f6564b8830bc894c89659`", f"Révision du modèle : `{REVISION_JOUET}`")
    Path(sortie).write_text(t, encoding="utf-8")
    return _sceller(Path(sortie))


def jouet(candidat_: str, sortie: str, depot: str, config_sha: str, tests: str) -> str:
    import re
    t = Path(candidat_).read_text(encoding="utf-8")
    for motif, valeur in ((r"Configuration de P4 \(empreinte canonique\) : `([0-9a-f]{64})`", config_sha),
                          (r"Tests attendus : `([0-9]+)`", str(tests)),
                          (r"Entropie : `([0-9]+)`", str(ENTROPIE_JOUET)),
                          (r"Révision du modèle : `([0-9a-f]{40})`", REVISION_JOUET)):
        if len(re.findall(motif, t)) != 1:
            raise SystemExit(f"citation absente ou en double dans le candidat : {motif}")
        t = re.sub(motif, lambda m: m.group(0).replace(m.group(1), valeur), t)
    p = Path(sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    p.write_text(t, encoding="utf-8")
    sys.path.insert(0, str(Path(depot).resolve() / "src"))
    from controle_ia.prereg import sceller_prereg
    return sceller_prereg(p)


def _importer(depot: Path, module: Path):
    sys.path.insert(0, str(Path(depot).resolve() / "src"))
    sys.path.insert(0, str(Path(module).resolve()))
    import instrument_p4_v1 as ip  # noqa: E402
    return ip


def monde(depot: str, module: str, travail: str, config_sortie: str) -> dict:
    d, m = Path(depot).resolve(), Path(module).resolve()
    ip = _importer(d, m)
    import test_instrument_p4_v1 as t  # noqa: E402  (run jouet de P3 des tests du module)
    d3 = t.construire_p3_jouet(Path(travail).resolve() / "p3-jouet")
    run3 = t.RUN_P3
    for rel in (f"donnees/{run3}", f"diag/{run3}", f"runs/{run3}", "donnees/synth"):
        if (d / rel).exists():
            raise SystemExit(f"{rel} existe déjà dans le dépôt d'essai (R12)")
        shutil.copytree(d3 / rel, d / rel)
    shutil.copy(d3 / "taches.json", d / "donnees/synth/taches.json")
    _sceller(d / "donnees/synth/taches.json")
    cfg = t.config_p4_jouet(d3)
    cfg["empreintes_sources"]["taches"] = {"chemin": "donnees/synth/taches.json",
                                           "sha256": _sha(d / "donnees/synth/taches.json")}
    ip.exiger_config_p4(cfg)
    p = Path(config_sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(cfg, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    _sceller(p)
    return {"config": ip.empreinte_config(cfg), "entropie": ENTROPIE_JOUET, "revision": REVISION_JOUET, "run_p3": run3,
            "taches": len(cfg["taches_niveau_1"]), "T": cfg["T"]}


def config_reelle(depot: str, module: str, sortie: str) -> dict:
    d = Path(depot).resolve()
    ip = _importer(d, Path(module))
    mc = json.loads((d / MC).read_text(encoding="utf-8"))["MC-1"]
    cfg = ip.config_de_reference(mc["B"], mc["Bprime"])
    ip.exiger_config_p4(cfg)
    p = Path(sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(cfg, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    _sceller(p)
    return {"config": ip.empreinte_config(cfg), "B": mc["B_nom"], "Bprime": mc["Bprime_nom"]}


def config_arret(depot: str, module: str, entree: str, sortie: str, duree: str) -> dict:
    """Configuration jouet dont seule `duree_max_s` change (arrêt du module pendant le run, cinquième passage)."""
    d = Path(depot).resolve()
    ip = _importer(d, Path(module))
    cfg = json.loads(Path(entree).read_text(encoding="utf-8"))
    if cfg.get("mode") != "jouet":
        raise SystemExit("configuration d'arrêt : configuration jouet attendue")
    cfg["duree_max_s"] = float(duree)
    ip.exiger_config_p4(cfg)
    p = Path(sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(cfg, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    _sceller(p)
    return {"config": ip.empreinte_config(cfg), "duree_max_s": cfg["duree_max_s"]}


def paires_v3(sortie: str, rapports: list[str]) -> int:
    """Paires exactes (ancien → nouveau) qui portent au candidat 1 les phrases de la chaîne (v2, corrigées par la v3) ;
    la source d'une paire inchangée reste celle de la chaîne v2."""
    connus = dict(RAPPORTS_CONNUS)
    for x in rapports:
        n, e = x.split("=", 1)
        if n not in connus:
            raise SystemExit(f"rapport {n} hors de la liste attendue")
        connus[n] = e
    paires = [{"ancien": a, "nouveau": b, "source": f"chaîne {v}, {k} ({c})"} for k, c, a, b, v in PHRASES_V3]
    paires.append({"ancien": ANCRE_RAPPORTS, "nouveau": ANCRE_RAPPORTS + "\n" + phrase_rapports(connus),
                   "source": "chaîne v3, rapports attendus (RC-fidelite-12 ; RAPPORTS_NOMS de la chaîne v3, vingt-six noms)"})
    p = Path(sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(paires, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    _sceller(p)
    return len(paires)


def journal_repetition(verif: str, code: str, nom: str, sha: str, versees: str | None) -> str:
    """Journal synthétique de la répétition jouet, conforme au module commun VERIF (ses listes, lues telles quelles)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("verifications_essai", verif)
    v = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v)
    l = [f"journal synthétique de la répétition jouet (essai)", f"commit du code répété : {code}",
         f"candidat répété : {nom} {sha}"]
    for s in sorted(v.SCRIPTS):
        l.append(f"script répété : {s} {_sha(Path(versees) / s) if versees else 'e' * 64}")
    for p in v.PASSAGES:
        l.append(p + "; durée totale 1 s")
        l.extend(f"    | 2026-10-20T00:00:00Z {x} (essai)" for x in v.DANS_LE_PASSAGE.get(p, ()))
    for x in v.CONFORMES:
        l.append(x)
        l.append("    --  3f versions non comparées (essai)")
        if v.DANS_LA_RECUPERATION.get(x):
            l.append(v.DANS_LA_RECUPERATION[x] + '{"etape": "essai", "motif": "essai"}')
    l.append(v.REFUS_LECTURE)
    l.append("lecture jouet (run-non-decisif) : code 0 ; issue L3")
    for x, ko in v.ARTEFACTS.items():
        l.extend([x, ko + "essai", v.GARDEE + "exited/stopped ; heure limite de destruction 2026-10-21T00:00:00Z (essai)"])
    for x in v.REFUS:
        l.append(x)
        if v.DANS_LE_REFUS.get(x):
            l.append(v.DANS_LE_REFUS[x] + "exited/stopped ; heure limite de destruction 2026-10-21T00:00:00Z (essai)")
    l.append(v.REPLI)
    l.extend(v.SANS_AFFICHAGE)
    l.append("FIN DE LA RÉPÉTITION")
    return "\n".join(l)


def fenetres(sortie: str) -> dict:
    p = Path(sortie)
    if p.exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    lignes = [{"episode": f"honnete/t{k}/e0", "condition": "honnete", "tache": f"t{k}", "pas": 0, "texte": x}
              for k, x in enumerate(TEXTES_FENETRES)]
    lignes += [{"episode": "honnete/t3/e0", "condition": "honnete", "tache": "t3", "pas": 0, "texte": "." * 80},
               {"episode": "honnete/t4/e0", "condition": "honnete", "tache": "t4", "pas": 0, "texte": "=" * 80},
               {"episode": "saboteur/t0/e0", "condition": "saboteur", "tache": "t0", "pas": 0,
                "texte": "ACTION: ADD\nTITLE: Synthetic line of another condition, never read for the windows of P4.\n"}]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in lignes), encoding="utf-8")
    return {"textes": len(lignes), "sha256": _sceller(p)}


def main(argv: list[str]) -> int:
    if len(argv) >= 8 and argv[1] == "candidat":
        brouillon, sortie, depot, commit, config_sha, tests = argv[2:8]
        reste, mode_jouet, rapports = argv[8:], False, []
        while reste:
            if reste[0] == "--jouet":
                mode_jouet, reste = True, reste[1:]
            elif reste[0] == "--rapport" and len(reste) >= 2 and "=" in reste[1]:
                rapports.append(reste[1]); reste = reste[2:]
            else:
                print("usage : candidat … [--jouet] [--rapport NOM=SHA …]", file=sys.stderr)
                return 2
        print(candidat(brouillon, sortie, depot, commit, config_sha, tests, mode_jouet, rapports))
    elif len(argv) == 6 and argv[1] == "monde":
        print(json.dumps(monde(*argv[2:6])))
    elif len(argv) == 5 and argv[1] == "config-reelle":
        print(json.dumps(config_reelle(*argv[2:5]), ensure_ascii=False))
    elif len(argv) == 7 and argv[1] == "jouet":
        print(jouet(*argv[2:7]))
    elif len(argv) == 3 and argv[1] == "fenetres":
        print(json.dumps(fenetres(argv[2])))
    elif len(argv) in (6, 7) and argv[1] == "journal-repetition":
        print(journal_repetition(*argv[2:6], argv[6] if len(argv) == 7 else None))
    elif len(argv) == 7 and argv[1] == "config-arret":
        print(json.dumps(config_arret(*argv[2:7])))
    elif len(argv) >= 3 and argv[1] == "paires-v3":
        reste = argv[3:]
        if len(reste) % 2 or any(reste[i] != "--rapport" or "=" not in reste[i + 1] for i in range(0, len(reste), 2)):
            print("usage : paires-v3 SORTIE [--rapport NOM=SHA …]", file=sys.stderr)
            return 2
        print(paires_v3(argv[2], reste[1::2]))
    else:
        print("usage : candidat BROUILLON SORTIE DEPOT COMMIT CONFIG_SHA TESTS [--jouet] [--rapport NOM=SHA …] | "
              "monde DEPOT MODULE TRAVAIL CONFIG_SORTIE | config-reelle DEPOT MODULE SORTIE | "
              "jouet CANDIDAT SORTIE DEPOT CONFIG_SHA TESTS | fenetres SORTIE | "
              "config-arret DEPOT MODULE CONFIG_ENTREE CONFIG_SORTIE DUREE | paires-v3 SORTIE [--rapport NOM=SHA …] | "
              "journal-repetition VERIF CODE CANDIDAT_NOM CANDIDAT_SHA [VERSEES]",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
