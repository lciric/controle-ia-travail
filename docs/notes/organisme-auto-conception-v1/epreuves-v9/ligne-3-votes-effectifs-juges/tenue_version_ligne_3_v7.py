# -*- coding: utf-8 -*-
"""Textes de tenue de version (version 6 -> version 7) de la ligne 3.

Ce module ne porte AUCUN texte des quatre corrections de la vérification de
la version 6 : ceux-là sont tirés de la vérification par `appliquer_v7.py`.
Il ne porte que la tenue de version (titre, statut, heures, mandat cité,
vérification citée comme faite, section de différentiel).
`{HEURE_FIN}` est rempli par le programme (heure relevée par `date -u`).
"""

E_V5 = "915fbe4b7ab17d83b9d39b92f21fd4cf4d52394d974b8b5b9c6e9e589d2fed12"
E_V6 = "b040d24cbef61a2a61ca724b097e6857d3465bba4d21f16d2cffc0241220ab94"
E_VERIF_V6 = "cbaf44de72b3dff7bd133be33a288a6a171776e72b94fc194f866faa05e8f9c1"
E_MANDAT_V7 = "70568050074f1ec4fc0be614317452b6d0bd8b7cdc815b6949e65c45c57234da"
E_DEVIS_V5 = "43bcb1c887de4f8e683510ceac5871ff4c07464f6dfe396480937567b8761c4f"
E_DEVIS_V6 = "34e87d90f8f3060f7eecd0abdce84721078cea6a97247f909e4cb4d0f2a6c26a"
COMMIT_DECISIONS = "79da594ce55fb0f9941be082b02f3a7c01136838"
E_DECISIONS = "8cd3e08cb59c290fe4b9990be54ce9abdb63f82f939139d2ee4e980b3b85a0a8"

ALLEGEMENT = (
    "(règle de l'allègement, classe A : contre-lecture, puis vérification des "
    "corrections par le même contre-lecteur ; ici par un agent neuf du même "
    "modèle, écart déclaré)"
)

# ---------------------------------------------------------------------------
# Préenregistrement : (nom, ancien, nouveau). Chaque ancien doit figurer une
# fois et une seule dans la version 6.
# ---------------------------------------------------------------------------
PREREG_TENUE = [
    (
        "titre",
        "étage 1 sur processeur, étage 2 payant — v6\n",
        "étage 1 sur processeur, étage 2 payant — v7\n",
    ),
    (
        "statut, tête",
        "**Statut : version 6, scellable par la mère après vérification du différentiel ; aucune dépense avant la ligne de GO.** "
        "Cette version remplace la version 5 (`preenregistrement-ligne-3-votes-effectifs-juges-v5.md`, `" + E_V5 + "`), "
        "gardée sans modification, comme les versions 4, 3, 2 et 1. "
        "Elle applique les quatre corrections du compte rendu du vérificateur arrêté de la version 5 (",
        "**Statut : version 7, scellable par la mère après vérification du différentiel ; aucune dépense avant la ligne de GO.** "
        "Cette version remplace la version 6 (`preenregistrement-ligne-3-votes-effectifs-juges-v6.md`, `" + E_V6 + "`), "
        "gardée sans modification, comme les versions 5, 4, 3, 2 et 1. "
        "Elle applique, à la lettre, les quatre corrections de la vérification de la version 6 "
        "(`verification-ligne-3-v6-v1.md`, même dossier, `" + E_VERIF_V6 + "`, verdict « scellable après corrections »), "
        "que la mère a acceptées : la liste fermée de ce que rend la garde de recouvrement, dite entière ; "
        "le repli mis sous la condition (4) ; le journal des rejeux absent ou illisible ; la provenance des mots de la mère. "
        "Elle n'ajoute que la tenue de version. "
        "Aucun montant, aucun appel, aucune hypothèse, aucune règle de lecture d'un verdict ne change. "
        "**Version 6** : elle remplaçait la version 5 (`preenregistrement-ligne-3-votes-effectifs-juges-v5.md`, `" + E_V5 + "`), "
        "gardée sans modification, comme les versions 4, 3, 2 et 1. "
        "Elle appliquait les quatre corrections du compte rendu du vérificateur arrêté de la version 5 (",
    ),
    (
        "statut, temps du verbe (1)",
        "), et écrit toutes les conditions de cloisonnement que la mère met à la garde de recouvrement (mots vers 15:39Z, 16:39Z et 16:44Z)",
        "), et écrivait toutes les conditions de cloisonnement que la mère met à la garde de recouvrement (mots vers 15:39Z, 16:39Z et 16:44Z)",
    ),
    (
        "statut, temps du verbe (2)",
        "Le travail est repris sur le mot de Lazar « go reprise, go recos » (GO-2026-11-19-81). "
        "Aucun montant, aucun appel, aucune hypothèse, aucune règle de lecture d'un verdict ne change. **Version 5**",
        "Le travail était repris sur le mot de Lazar « go reprise, go recos » (GO-2026-11-19-81). "
        "Elle ne changeait aucun montant, aucun appel, aucune hypothèse, aucune règle de lecture d'un verdict. **Version 5**",
    ),
    (
        "statut, différentiels visés",
        "le différentiel avec la version 5 est en fin de texte, et la vérification de la version 6 se fait sur lui ; "
        "comme la vérification de la version 5 n'a pas été écrite, elle se fait aussi sur le différentiel de la version 5 avec la version 4, gardé tel quel juste avant.",
        "le différentiel avec la version 6 est en fin de texte, et la vérification de la version 7 se fait sur lui seul ; "
        "la vérification de la version 6 s'est faite sur le différentiel de la version 6 avec la version 5 et, "
        "comme la vérification de la version 5 n'avait pas été écrite, sur celui de la version 5 avec la version 4, tous deux gardés tels quels juste avant.",
    ),
    (
        "en-tête, auteur",
        "Cette version 6 est écrite par un agent neuf du modèle F, qui n'a écrit aucune des versions 1 à 5 ; "
        "elle se vérifie sur son différentiel, par un agent du modèle O qui n'a écrit aucune version " + ALLEGEMENT + ".",
        "La version 6 a été écrite par un agent neuf du modèle F, qui n'avait écrit aucune des versions 1 à 5 ; "
        "elle a été vérifiée, sur ses deux différentiels, par un agent neuf du modèle O qui n'a écrit aucune des pièces lues "
        "(verdict « scellable après corrections », quatre corrections). "
        "Cette version 7 est écrite par un agent neuf du modèle F, qui n'a écrit aucune des versions 1 à 6 ; "
        "elle se vérifie sur son différentiel, par un agent du modèle O qui n'a écrit aucune version " + ALLEGEMENT + ".",
    ),
    (
        "en-tête, date",
        "version 6 entre 22:11 (première heure relevée) et 22:16.",
        "version 6 entre 22:11 (première heure relevée) et 22:16, "
        "version 7 entre 22:35 (première heure relevée) et {HEURE_FIN}.",
    ),
    (
        "en-tête, mandat de la version 6 (nom)",
        "- **Mandat du rédacteur de cette version 6** : même dossier,",
        "- **Mandat du rédacteur de la version 6** : même dossier,",
    ),
    (
        "en-tête, mandat de la version 7 (puce neuve)",
        "Ce mandat ne partait qu'au mot de reprise de Lazar : ce mot est donné (GO-2026-11-19-81).\n",
        "Ce mandat ne partait qu'au mot de reprise de Lazar : ce mot est donné (GO-2026-11-19-81).\n"
        "- **Mandat du rédacteur de cette version 7** : même dossier, `mandat-redacteur-ligne-3-v7-v1.md`, `" + E_MANDAT_V7 + "`. "
        "Donné par la session du compte de l'organisme sur GO-2026-11-19-81. "
        "Il limite cette version aux quatre corrections de la vérification de la version 6, appliquées à la lettre avec ses textes exacts, et à la tenue de version ; "
        "il garde l'interdit de toute commande sur un chemin sous `archives-reponses-modeles/`. "
        "La mère a accepté les quatre corrections (mot vers 22:28Z) : je n'ai lu ce mot que par la session du compte de l'organisme, qui me l'a rapporté en me donnant ce mandat ; je n'en ai pas lu d'autre source écrite.\n",
    ),
    (
        "en-tête, documents : vérification de la version 6 (puce neuve)",
        "elle se prend par le code de la banque, à sa contre-lecture (« Garde de recouvrement », (1) et (4)).\n",
        "elle se prend par le code de la banque, à sa contre-lecture (« Garde de recouvrement », (1) et (4)).\n"
        "  - vérification de la version 6 : `verification-ligne-3-v6-v1.md`, même dossier (branche), `" + E_VERIF_V6 + "`. "
        "Faite, par un agent neuf du modèle O, sur les deux différentiels (version 4 → version 5, version 5 → version 6) ; "
        "verdict « scellable après corrections », quatre corrections, toutes à ce texte ; le devis v6 y est jugé propre. "
        "**Pour écrire la version 7, le rédacteur n'a lancé aucune commande sur un chemin sous `archives-reponses-modeles/`** : ni ouverture, ni empreinte, ni liste, ni taille ; il n'a ouvert aucune carte. "
        "L'empreinte `ba65c411…` du fichier des cartes reste reprise des versions 1 à 5. "
        "Pour la correction 4, il a relu sur main `registres/decisions.md` au commit `" + COMMIT_DECISIONS + "` : "
        "l'empreinte `" + E_DECISIONS + "` est recalculée égale, et les lignes R-3917 (15:39:45Z) et R-3934 (16:44:40Z) y sont, avec le contenu que la correction leur prête.\n",
    ),
    (
        "en-tête, empreintes recalculées",
        "le fichier des cartes n'a pas été touché ; toutes les autres empreintes de cette liste sont reprises de la version 5.",
        "le fichier des cartes n'a pas été touché ; toutes les autres empreintes de cette liste sont reprises de la version 5. "
        "Pour la version 7, ont été recalculées : la version 6 du texte et du devis, le rapport du rédacteur de la version 6, "
        "la vérification de la version 6, les mandats des versions 6 et 7, et `registres/decisions.md` au commit de main nommé plus haut ; "
        "le fichier des cartes n'a pas été touché ; toutes les autres empreintes de cette liste sont reprises de la version 6.",
    ),
    (
        "en-tête, devis",
        "- Devis de l'étage payant : `devis-ligne-3-etage-payant-v6.md`, même dossier (",
        "- Devis de l'étage payant : `devis-ligne-3-etage-payant-v7.md`, même dossier "
        "(la vérification de la version 6 juge le devis v6 propre ; la version 7 du devis n'y change que le renvoi au fichier de ce préenregistrement, aucun chiffre ; ",
    ),
    (
        "en-tête, devis, temps du verbe",
        "la version 6 n'y change que des renvois : le nom de ce préenregistrement, le registre relu, le mandat).",
        "la version 6 n'y changeait que des renvois : le nom du préenregistrement, le registre relu, le mandat).",
    ),
    (
        "en-tête, non lus",
        "aucune pour la version 6, ni aucune commande sur le fichier des cartes).",
        "aucune pour la version 6, ni aucune commande sur le fichier des cartes ; de même pour la version 7).",
    ),
    (
        "garde de recouvrement, (4) : vérificateur nommé",
        "Le vérificateur de la version 6, lui, contrôle que les cinq conditions",
        "Le vérificateur de la version 6, puis celui de la version 7, eux, contrôlent que les cinq conditions",
    ),
    (
        "ordre des gestes, (1)",
        "vérification de cette version 6, sur son différentiel et sur celui de la version 5 ; (2)",
        "vérification de la version 6, sur son différentiel et sur celui de la version 5, faite ; "
        "vérification de cette version 7, sur son seul différentiel ; (2)",
    ),
    (
        "« Contre-lecture » : version 6 vérifiée, version 7 à vérifier",
        "**Version 6, à vérifier.** Par un agent neuf du modèle O qui n'a écrit aucune version.",
        "**Version 6 : vérification faite.** Par un agent neuf du modèle O, qui n'a écrit aucune des pièces lues : "
        "`verification-ligne-3-v6-v1.md`, même dossier, `" + E_VERIF_V6 + "`. "
        "Ce qu'elle dit : les deux différentiels lus par programme et à la main (version 4 → version 5, 24 morceaux ; version 5 → version 6, 16 morceaux), tous expliqués ; "
        "les neuf corrections de la vérification de la version 4 et les quatre du compte rendu arrêté, reprises à la lettre et justes ; "
        "l'écart déclaré à la liste d'arrêt, juste et nécessaire ; les ajouts du rédacteur de la version 6, gardés ; "
        "le calcul des prédictions rejoué, sorties égales à l'octet ; le registre relu sur main. "
        "Elle n'a lancé aucune commande sur un chemin sous `archives-reponses-modeles/` : l'empreinte `ba65c411…` et le compte de 94 du fichier des cartes ne sont pas vérifiés par elle. "
        "Verdict : « scellable après corrections », quatre corrections, toutes à ce texte ; les trois premières ferment des trous de la garde de recouvrement, la quatrième est de provenance ; le devis v6 est jugé propre. "
        "La mère a accepté les quatre corrections (mot vers 22:28Z, rapporté au rédacteur de la version 7 par la session du compte de l'organisme).\n"
        "\n"
        "**Traitement des quatre corrections de la vérification de la version 6.** "
        "Toutes sont appliquées à la lettre, sans écart : un programme tire les textes anciens et neufs de la vérification elle-même (§ 10), sans recopie à la main, "
        "et s'arrête si un texte ancien ne figure pas une fois et une seule dans la version 6. "
        "Aucune ne change le choix de Lazar, la grandeur mesurée, le plan de 504 appels, les montants ni le plafond.\n"
        "\n"
        "| n° | ce qu'elle demande | comment | où |\n"
        "|---|---|---|---|\n"
        "| 1 | la liste fermée de ce que rend la garde n'était pas dite entière en un seul lieu ; la cause du repli doit être nommée par une valeur fermée, non par un texte libre | "
        "fin de la liste du (3) remplacée par le texte donné : nombre de rejeux, nom de classe et lieu d'une exception, mention du repli et sa cause parmi les deux déclencheurs, puis les mots qui ferment la liste ; "
        "à l'annexe A, l'écart du repli est dit déclaré au manifeste et au rapport de la garde | « Garde de recouvrement », (3) ; annexe A |\n"
        "| 2 | lu à la lettre, le repli faisait tourner la garde sans que le contrôle du (4) soit passé | phrase donnée ajoutée à la fin de la puce « Repli » : sous le repli, la condition (4) vaut aussi, chemin du repli compris ; sinon ni garde ni repli | « Garde de recouvrement », puce « Repli » |\n"
        "| 3 | rien ne disait ce qui se passe si le journal des rejeux est absent ou illisible : le compte repartait de zéro, en silence (règle R5) | "
        "phrases données ajoutées au (5) : journal créé vide avant le premier passage, refus de tourner avant d'ouvrir le fichier s'il est absent ou illisible ; un artefact de plus à la liste d'arrêt | « Garde de recouvrement », (5) ; liste d'arrêt, « recouvrement » |\n"
        "| 4 | provenance des mots de la mère (règle R6) | à l'en-tête, texte donné : R-3917 et R-3934 cités, commit et empreinte de `registres/decisions.md` (relus et recalculés pour la version 7) ; "
        "au (4), la source de la confirmation de lecture devient le mandat de la version 6, point 2 | en-tête, mandat de la version 6 ; « Garde de recouvrement », (4) |\n"
        "\n"
        "**Hors vérification, ajouté par le rédacteur en version 7, à vérifier sur le différentiel** : la tenue de version seulement "
        "(titre ; statut ; auteur ; heures ; mandat de la version 7 cité ; vérification de la version 6 citée comme faite ; empreintes recalculées dites ; renvoi au devis v7 ; « non lus » ; "
        "vérificateur de la version 7 nommé au (4) ; ordre des gestes, (1) ; cette section ; le différentiel avec la version 6). Rien au fond. "
        "Le devis passe en version 7 pour un seul renvoi : il nomme ce préenregistrement par son fichier. "
        "Les deux lectures à confirmer par la mère, nommées plus haut, restent telles quelles : la vérification de la version 6 juge la première conforme au mot « rejeu » et à R-3934, et dit la question bien rendue à la mère.\n"
        "\n"
        "**Version 7, à vérifier.** Par un agent neuf du modèle O qui n'a écrit aucune version. "
        "**Interdit à écrire en tête de son mandat : aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`** ; "
        "aucune carte n'est à lui donner, et l'empreinte du fichier des cartes ne se vérifie pas par lui. "
        "Fichiers à lui donner : ce texte et son compagnon ; la version 6 ; la vérification de la version 6 ; le devis v7 et le devis v6 ; le mandat du rédacteur de la version 7 ; "
        "les lignes R-3917 et R-3934 de `registres/decisions.md` sur main. "
        "Points à lui demander : que chacun des textes neufs donnés au § 10 de la vérification de la version 6 est présent, à la lettre et à sa place ; "
        "chaque ligne de la table ci-dessus et du différentiel avec la version 6 ; que rien d'autre n'a changé depuis la version 6 que la tenue de version déclarée ; "
        "que le devis v7 ne change que le renvoi au fichier de ce préenregistrement.\n"
        "\n"
        "**Ce que la version 6 demandait à son vérificateur (gardé tel quel, pour mémoire ; vérification faite).** Par un agent neuf du modèle O qui n'a écrit aucune version.",
    ),
]

PREREG_FIN = (
    "\n"
    "## Différentiel avec la version 6\n"
    "\n"
    "Rien ne change dans : le choix de Lazar sur la ligne, les décisions de Lazar sur `fefca0bd94064` et `fa38f9faa24e0`, les deux décisions de GO-2026-11-19-77, "
    "la grandeur mesurée, les deux étages, les lois 1 à 4, les trois lois du lecteur de surface et le sens qui décide, la grille, le monde de puissance, les 100 témoins, "
    "le plan de 504 appels, les montants du devis, le plafond de 25 USD, les seuils, les critères de lecture gelés, la table de lecture de l'étage 2, "
    "les dix-neuf gardes (une ligne précisée : un artefact de plus), les treize réserves, la règle « aucune carte tranchée par un juge », les calculs versés et leurs sorties. "
    "Aucun appel de plus, aucune carte affichée, aucune commande sur le fichier des cartes. "
    "Les différentiels avec les versions 1 à 5, ci-dessus, sont gardés tels quels. "
    "« Correction n » renvoie à la vérification de la version 6, § 10 ; « mandat » renvoie au mandat du rédacteur de la version 7. "
    "Les lignes 10 à 13, 15 et 17, et la phrase de provenance de la ligne 5, sont les quatre corrections, à la lettre ; toutes les autres sont de la tenue de version.\n"
    "\n"
    "| n° | section | version 6 | version 7 | source |\n"
    "|---|---|---|---|---|\n"
    "| 1 | titre | « v6 » | « v7 » | règle R12 |\n"
    "| 2 | statut | version 6, remplace la version 5 | version 7, remplace la version 6 ; ce qu'elle applique ; la phrase de la version 6 gardée, mise au passé ; différentiel visé : celui-ci seul | mandat |\n"
    "| 3 | en-tête, auteur | version 6 et son vérificateur à venir | version 6 dite vérifiée ; version 7 et son vérificateur ; citation de la règle de l'allègement gardée à la lettre | mandat |\n"
    "| 4 | en-tête, date | jusqu'à la version 6 | heures de la version 7 ajoutées | mandat |\n"
    "| 5 | en-tête, mandats | « cette version 6 » ; le mandat dit seule source écrite des mots de la mère | « la version 6 » ; texte donné : R-3917 et R-3934 cités, commit et empreinte de `registres/decisions.md`, le mot de 16:39Z sans autre source ; mandat de la version 7 cité (puce neuve), mot d'acceptation de la mère rapporté | correction 4 ; mandat |\n"
    "| 6 | en-tête, documents | jusqu'au compte rendu du vérificateur arrêté | vérification de la version 6 citée comme faite (puce neuve) ; aucune commande sur le fichier des cartes pour la version 7 ; `registres/decisions.md` relu | mandat ; règle R6 |\n"
    "| 7 | en-tête, empreintes recalculées | jusqu'à la version 6 | celles de la version 7 dites | règle R6 |\n"
    "| 8 | en-tête, devis | devis v6 | devis v7 (un seul renvoi) ; la phrase de la version 6 mise au passé | mandat |\n"
    "| 9 | en-tête, non lus | « aucune pour la version 6 … » | « de même pour la version 7 » ajouté | mandat |\n"
    "| 10 | garde de recouvrement, (3) | liste finie à l'identifiant de chaque témoin refusé | texte donné : nombre de rejeux, nom de classe et lieu d'une exception, mention du repli et sa cause, liste dite close | correction 1 |\n"
    "| 11 | garde de recouvrement, (4) | confirmation de lecture sourcée par « mot vers 16:39Z » ; vérificateur de la version 6 | texte donné : sourcée par le mandat de la version 6, point 2, condition (4) ; vérificateurs des versions 6 et 7 | correction 4 ; mandat |\n"
    "| 12 | garde de recouvrement, (5) | — | texte donné : journal créé vide avant le premier passage ; absent ou illisible, refus de tourner avant d'ouvrir le fichier, mère saisie | correction 3 |\n"
    "| 13 | garde de recouvrement, repli | — | texte donné, en fin de puce : sous le repli, la condition (4) vaut aussi, chemin du repli compris | correction 2 |\n"
    "| 14 | ordre des gestes, (1) | vérification de la version 6 à faire | faite ; vérification de la version 7 à faire, sur son seul différentiel | mandat |\n"
    "| 15 | liste d'arrêt, « recouvrement » | — | texte donné : un artefact de plus (journal des rejeux absent ou illisible) | correction 3 |\n"
    "| 16 | « Contre-lecture » | version 6 à vérifier | vérification de la version 6 dite faite ; table des quatre corrections ; tenue de version nommée ; version 7 à vérifier, interdit en tête ; demande de la version 6 gardée pour mémoire | corrections 1 à 4 ; mandat |\n"
    "| 17 | annexe A, banque | « écart déclaré au manifeste » | texte donné : « écart déclaré au manifeste et au rapport de la garde » | correction 1 |\n"
    "| 18 | fin de texte | — | ce différentiel | mandat |\n"
    "| — | devis | v6 | v7 : aucun montant changé ; un seul renvoi (le fichier de ce préenregistrement) ; calcul du devis inchangé (version 3) | mandat |\n"
    "| — | calcul des prédictions | version 2 | inchangé, non rejoué pour la version 7 | — |\n"
)

# ---------------------------------------------------------------------------
# Devis : seulement le renvoi au fichier du préenregistrement (mandat).
# ---------------------------------------------------------------------------
DEVIS_TENUE = [
    (
        "titre",
        "devis de l'étage payant — v6\n",
        "devis de l'étage payant — v7\n",
    ),
    (
        "statut, renvoi",
        "**Statut : version 6, scellable par la mère après vérification du différentiel ; aucune dépense avant la ligne de GO.** "
        "Ce devis chiffre l'étage 2 du préenregistrement `preenregistrement-ligne-3-votes-effectifs-juges-v6.md` (même dossier). Il n'engage rien. "
        "Il remplace `devis-ligne-3-etage-payant-v5.md` (`" + E_DEVIS_V5 + "`), gardé sans modification, comme les versions 4 (",
        "**Statut : version 7, scellable par la mère après vérification du différentiel ; aucune dépense avant la ligne de GO.** "
        "Ce devis chiffre l'étage 2 du préenregistrement `preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (même dossier). Il n'engage rien. "
        "Il remplace `devis-ligne-3-etage-payant-v6.md` (`" + E_DEVIS_V6 + "`), gardé sans modification, comme les versions 5 (`" + E_DEVIS_V5 + "`), 4 (",
    ),
    (
        "statut, objet",
        "rien de cela ne touche un paragraphe chiffré de ce devis. Aucun chiffre, aucun appel, aucun calcul ne change. Différentiel en fin de texte.",
        "rien de cela ne touche un paragraphe chiffré de ce devis. Aucun chiffre, aucun appel, aucun calcul ne change. "
        "**La version 7** ne change qu'un renvoi : le fichier du préenregistrement, passé en version 7 pour les quatre corrections de sa vérification "
        "(`verification-ligne-3-v6-v1.md`, même dossier, `" + E_VERIF_V6 + "`, qui juge le devis v6 propre). Aucun chiffre, aucun appel, aucun calcul ne change. "
        "Différentiel en fin de texte.",
    ),
    (
        "§ 7, point 1",
        "1. Le préenregistrement (version 6) et ce devis,",
        "1. Le préenregistrement (version 7) et ce devis,",
    ),
]

DEVIS_FIN = (
    "\n"
    "## Différentiel avec la version 6\n"
    "\n"
    "Aucun montant, aucun nombre d'appels, aucun plafond, aucune table, aucun paragraphe chiffré ne change. "
    "Le calcul et sa sortie sont ceux des versions 4 à 6 (`calcul_devis_ligne_3_v3.py`, `calcul-devis-ligne-3-v3.json`), sans changement, non rejoués. "
    "Seul le renvoi au fichier du préenregistrement change ; la vérification de la version 6 juge le devis v6 propre.\n"
    "\n"
    "| n° | point | version 6 | version 7 | source |\n"
    "|---|---|---|---|---|\n"
    "| — | montants de la base | 16,52 ; 22,49 ; 44,38 USD | inchangés | — |\n"
    "| 1 | titre | « v6 » | « v7 » | règle R12 |\n"
    "| 2 | statut | version 6 ; préenregistrement v6 ; remplace le devis v5 | version 7 ; préenregistrement v7 ; remplace le devis v6, gardé | mandat du rédacteur de la version 7 |\n"
    "| 3 | statut, objet | ce que la version 6 change | une phrase de plus : la version 7 ne change qu'un renvoi | mandat |\n"
    "| 4 | § 7, point 1 | préenregistrement (version 6) | préenregistrement (version 7) | mandat |\n"
    "| 5 | fin de texte | — | ce différentiel | mandat |\n"
)
