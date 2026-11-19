# -*- coding: utf-8 -*-
"""Barreau 5 : retouches de consolidation du candidat au scellement, employées par `fabrique-candidat-scellement-v1.py`.

Écrites par le rédacteur (Claude Fable 5.2). Elles s'appliquent au brouillon 5 après les 18 couples de l'erratum 1.
Rien d'autre que : titre et statut ; liste des documents ; les quatre mentions des marques levées ; le nom définitif.
`PROPOSITIONS` : couples que le rédacteur propose mais n'applique pas (le mandat disait « et rien d'autre ») ; le
programme vérifie seulement que leur « avant » se trouve une fois dans le candidat. Aucune donnée du programme.
"""
NOM = "barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1"
PLAN = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/"
CANDIDAT = "candidat au scellement, à copier à l'octet sous le nom définitif si la vérification le dit scellable tel quel"
E_B4 = "dbe66dc99332a1c40cbc6f6bceee7f9c7c49c741f0e99feaa7f7949609109256"
E_B5 = "6f7e20418c841c79d12f763c67ccfbd4e18c41bccc2a5ca626567ab3606dbfe2"
E_B5_ERRATUM = "a6c8f0bc6bbd52a2dfcce1d9ed32a44dcacd466aefbfa6bfe5eb2c9ca399924c"
E_DV5 = "9ba5db06f2070c2f85fbc34002f27f47aaa9df739c7fbb2ef939efedee85a306"
E_DV5_ERRATUM = "1c7f6f2236846fac14e3886c51aebf18256b88905875cf489da2a6ae3bc463ba"
E_ERRATUM = "8c3451a2e76823d4ae31789164ac6597b2d9b87e809b0e251c295cb8d14a2e40"
E_RAPPORT_V4 = "b7e2255500985badcd0c9e8a1fd9e33671d641fd5d252bc254cef79019e274c3"
E_VERIF_B4 = "a091eed230a10ddd3566187e213a736f764e04d105a58d0ef62f91f6ba1a9df4"

STATUT = (
    "- Statut : **" + CANDIDAT + ".** Nom définitif : `prereg/" + NOM + ".md` ; le code de formation refuse un nom qui contient « brouillon ». "
    "Ce candidat est le brouillon 5 (`" + E_B5 + "`) auquel sont appliqués les 18 couples de l'erratum 1 (`" + PLAN + "erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md`, `" + E_ERRATUM + "`), ce qui donne l'état d'empreinte `" + E_B5_ERRATUM + "`, puis les seules retouches de consolidation : titre, statut, liste des documents, quatre mentions des marques levées, nom définitif du devis. "
    "Tout ce qui le sépare du brouillon 4 vérifié (`" + E_B4 + "`) est énuméré dans `" + PLAN + "table-difference-candidat-scellement-v1.md`. "
    "Filiation : vérification du brouillon 4 (`" + E_VERIF_B4 + "`, « scellable après ces couples ») ; brouillon 3 (`525f338e7899e6a8f57b73fffef7f0eeef3d6a16eee0e7d6c2823cddb44c9e50`) et sa vérification (`a1b2250de628f90fb28253ded8e12ae6be88678f4915cced28c979197c02d19b`, constat bloquant V-B1) ; fiche de décision `" + PLAN + "fiche-decision-v-b1-lazar-v1.md` (`78cadfd2…`) ; couples du code (`couples-du-code-pour-brouillon4-v1.md`, `1e929542…`) ; vérification des corrections du code (`code-formation/verification-corrections-code-formation-v1.md`, `3517677f…`) ; rapport v4 du développeur des corrections du code (`b7e22555…`). "
    "Aucune phrase de ce texte n'attend plus un rapport sur le code : les marques du brouillon 4 sont levées. Le devis est un candidat lui aussi, à copier à l'octet sous le nom `" + PLAN + "devis-adaptateurs-tenus-a-l-ecart-v1.md`. Rien lancé sur carte, rien dépensé, rien commis.")

DOCUMENTS = (
    "  - rapport v4 du développeur des corrections du code de formation : `code-formation/rapport-developpeur-corrections-code-formation-v4.md`, `" + E_RAPPORT_V4 + "` ; erratum 1 au brouillon 5, qui lève sur ce rapport les marques du brouillon 4, écrit la règle des compteurs de dépense et range les treize points du rapport : `erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md`, `" + E_ERRATUM + "` ; `points-g-rapport-v4-ranges-v1.md`, `76e0e27e…` ;")

# (nom, avant, après) : chaque « avant » une fois, après l'erratum 1
RETOUCHES_TEXTE = [
    ("K-titre", "— v1 — brouillon 5", "— v1 — " + CANDIDAT),
    ("K-ce-qui-change",
     "(3) Les marques « [à confirmer par le rapport v4] » restent : le rapport v4 du développeur n'était pas scellé à l'écriture ; elles se lèvent par un erratum.",
     "(3) Les marques « à confirmer » du brouillon 4 sont levées par l'erratum 1 au brouillon 5, sur le rapport v4 du développeur des corrections du code ; cet erratum écrit aussi quel compteur de dépense compte la relance, et prend dans le texte les points du rapport qui le touchaient. Ce candidat est le brouillon 5 avec cet erratum."),
    ("K-risque",
     "- La vérification du différentiel de ce brouillon, et la levée des marques « [à confirmer par le rapport v4] » : le code exige le texte entier scellé.",
     "- La vérification de ce candidat (différentiel du brouillon 5, erratum 1, retouches de consolidation) : le code exige le texte entier scellé."),
    ("K-contre-lecture",
     "**Vérification du différentiel du brouillon 5 : en attente**, par le même contre-lecteur. Puis scellement sous le nom définitif, après la levée des marques « [à confirmer par le rapport v4] ».",
     "**Vérification de ce candidat : en attente**, par le même contre-lecteur. Elle porte sur le différentiel du brouillon 5, sur l'erratum 1 (`" + E_ERRATUM + "`) et sur les retouches de consolidation, tous énumérés dans `table-difference-candidat-scellement-v1.md`. S'il est dit scellable tel quel, ce candidat est copié à l'octet sous le nom définitif."),
]
PARTOUT_TEXTE = [("K-nom-du-devis", "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md", "devis-adaptateurs-tenus-a-l-ecart-v1.md", 2)]
LIGNES_TEXTE = [
    ("K-statut", "- Statut :", STATUT, False),
    ("K-documents", "  - code de formation : rapport v3", DOCUMENTS, True),
]

RETOUCHES_DEVIS = [
    ("K-devis-titre", "— v1 — brouillon 5\n", "— v1 — " + CANDIDAT + "\n"),
    ("K-devis-texte-chiffre",
     "- Texte qu'il chiffre : `prereg/" + NOM + "-brouillon5.md`, qui sera scellé sous le nom `prereg/" + NOM + ".md`.",
     "- **Candidat au scellement** : le devis du brouillon 5 (`" + E_DV5 + "`) avec les quatre couples de l'erratum 1 (`erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md`, `" + E_ERRATUM + "`), ce qui donne l'état d'empreinte `" + E_DV5_ERRATUM + "`, puis ces seules retouches : titre, cette puce, nom du texte chiffré. Aucun chiffre ne change. À copier à l'octet sous le nom `devis-adaptateurs-tenus-a-l-ecart-v1.md`.\n"
     "- Texte qu'il chiffre : `prereg/" + NOM + ".md`, nom définitif du candidat `prereg/" + NOM + "-candidat-scellement.md`."),
]

# couples proposés, NON appliqués : le mandat borne les retouches ; à la mère et au contre-lecteur de dire
PROPOSITIONS = [
    ("P-1", "le marqueur M-2 dit encore que le plafond, l'enveloppe et les nœuds 3 à 7 restent : oubli du brouillon 5, contredit par « Nœuds »",
     "M-2 : réponses de Lazar : 39 adaptateurs, voie (iii) et départ au plus tôt acquis ; restent le plafond, l'enveloppe de relance, et les nœuds 3 à 7, qui ont un défaut écrit (« Nœuds ») ;",
     "M-2 : fait : les réponses de Lazar sont écrites à la section « Nœuds » (`GO-2026-11-19-79`, `-82`, `-86` à `-88`) ; reste le nœud 8, après le verdict ;"),
    ("P-2", "le marqueur M-10 parle du différentiel du brouillon 5",
     "reste la vérification du différentiel du brouillon 5 ;",
     "reste la vérification du candidat au scellement ;"),
    ("P-3", "le titre de la section dit « à remplir avant le scellement », alors que le texte est copié à l'octet : les marqueurs encore ouverts (M-3, M-4, M-5, M-7) ne peuvent être remplis que par le registre",
     "## Marqueurs à remplir avant le scellement\n",
     "## Marqueurs (état au candidat ; ceux qui restent ouverts sont remplis par la ligne `SCELLEMENT-B5F` du registre propre, puisque ce texte est copié à l'octet)\n"),
    ("P-4", "le marqueur M-6 dit que, faute de rapprochement avant le scellement, « le texte scellé dit alors rapprochement non fait » : le texte doit donc le dire",
     "M-7 : nom de la session de formation et de la session de lecture ;",
     "M-6, état à l'écriture du candidat : rapprochement non fait ; ce plan garde sa propre règle ; M-7 : nom de la session de formation et de la session de lecture, écrits au registre propre à leur désignation ;"),
]
