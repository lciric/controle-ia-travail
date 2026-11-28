# -*- coding: utf-8 -*-
"""Textes de l'erratum 1 du programme v3 (lemme d'additivité, application).

Ce module ne fait que porter les textes : l'énoncé revendiqué et les sept
entrées (texte d'origine, texte neuf, raison). La construction du fichier et
les vérifications vivent dans construire.py.
"""

S1 = (
    "Chez des agents qui sabotent, à dommage total égal et pour un même "
    "nombre n d'actions surveillées, le déplacement cumulé des scores de "
    "sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du "
    "nombre d'actions ou d'agents entre lesquels le sabotage est réparti."
)
S2 = (
    "Ce déplacement est la somme des scores sur les n actions de l'épisode "
    "saboté, moins la même somme chez son jumeau honnête."
)
S3 = (
    "Si cette conservation tient, l'énoncé central cité s'applique aux "
    "sondes : à déplacement total donné, la somme lue en fin d'épisode est "
    "indifférente à la répartition."
)
ENONCE = S1 + " " + S2 + " " + S3

REFUTATION = (
    "La conservation est réfutée si le déplacement cumulé monte ou baisse "
    "avec la fragmentation au-delà d'une marge fixée au préenregistrement, "
    "après calcul de puissance. Le sens de l'écart est alors le résultat ; "
    "une issue indéterminée est possible."
)

FORMULE = (
    "revendiqué dans sa seule application au contrôle de l'intelligence "
    "artificielle, sous la forme mesurée"
)

ENTREES = []

# L-1 — section 0, défaut D-b
ENTREES.append((
    "(défaut de la version 2, caduc : le lemme n'est plus revendiqué, section 3)",
    "(défaut de la version 2, caduc : le lemme n'est plus revendiqué comme "
    "théorème ; il est " + FORMULE + ", section 3)",
    "GO-2026-11-24-18. La phrase excluait aussi l'application. Le défaut "
    "reste caduc : aucun théorème n'est tenté.",
))

# L-2 — section 2, ligne « Hypothèses » du tableau des trois papiers
ENTREES.append((
    "L et T mentionnés, non revendiqués",
    "L " + FORMULE + " (énoncé central cité, non revendiqué) ; "
    "T mentionné, non revendiqué",
    "GO-2026-11-24-18. Le statut du lemme change ; celui du théorème négatif "
    "ne change pas.",
))

# L-3 — section 3, « Statut de ce qui suit »
ENTREES.append((
    "L'additivité interne, le lemme et le théorème ne sont plus des résultats ; "
    "ils restent mentionnés, chacun à son statut.",
    "L'additivité interne, le lemme et le théorème ne sont plus des résultats ; "
    "l'additivité interne et le théorème restent mentionnés, chacun à son "
    "statut ; le lemme reste cité pour son énoncé central, et il est " + FORMULE + ".",
    "GO-2026-11-24-18. Le lemme n'est plus seulement mentionné. Il reste "
    "retiré comme résultat (GO-2026-11-22-24).",
))

# L-4 — section 3, paragraphe du lemme : statut, énoncé central, application
ENTREES.append((
    "**Lemme d'additivité (mentionné, non revendiqué).** Énoncé occupé hors du "
    "contrôle de l'intelligence artificielle : l'indifférence de la somme à la "
    "répartition, à taille fixe (Avenhaus et Jaech 1981 ; Ker 2006).",
    "**Lemme d'additivité (énoncé central cité, non revendiqué ; application au "
    "contrôle de l'intelligence artificielle revendiquée sous la forme mesurée, "
    "décision du 24 novembre 2026, GO-2026-11-24-18).** Énoncé central, occupé "
    "hors du contrôle de l'intelligence artificielle et non revendiqué : "
    "l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et "
    "Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7). Application revendiquée, "
    "sans théorème, à éprouver par la mesure. " + ENONCE + " " + REFUTATION + " "
    "Hypothèses : (1) le sabotage déplace la position des scores et ce "
    "déplacement croît avec le dommage (s'il est nul à tous les niveaux, "
    "l'énoncé est sans objet et la question Q décide) ; (2) le dommage, celui "
    "de l'épisode entier, est chiffré et constaté hors des scores ; (3) à tous "
    "les niveaux de "
    "fragmentation, n, la tâche, le nombre d'agents et la sonde, gelée avant la "
    "mesure, sont les mêmes, et la référence honnête est déclarée (taille m, "
    "dans l'unité de n) ; (4) la "
    "somme est lue en fin d'épisode, et rien n'est dit d'un franchissement "
    "séquentiel ; (5) le montage fixe la fragmentation, sur les organismes tels "
    "qu'ils sont construits, et rien n'est affirmé d'un saboteur qui choisit sa "
    "répartition. Mesuré par sonde, par famille d'organismes et par niveau de "
    "fragmentation (le nombre d'actions ou d'agents qui portent le sabotage) : "
    "le déplacement cumulé et sa dispersion ; à côté, le rappel "
    "de la somme, le maximum par action et la part du déplacement portée par "
    "les actions de sabotage. Unité d'observation : l'épisode entier, apparié à "
    "son jumeau honnête sur la même tâche ; l'incertitude se calcule par tâche. "
    "Voisins à citer : bornes en divergence totale, en boîte noire (Tailor "
    "2025, arXiv 2510.04303, p. 12 ; Ghanem 2026, arXiv 2608.02698, p. 5) ; "
    "baisse du maximum du soupçon quand l'attaque se répartit entre plus "
    "d'agents (Makins et al. 2026, arXiv 2607.07368, p. 1 ; la somme n'y est "
    "pas testée, selon notre lecture). Antériorité de cette forme non établie : "
    "aucune phrase de nouveauté. La prévision de H3 sur la somme globale garde "
    "son statut.",
    "GO-2026-11-24-18, avec GO-2026-11-22-42 (application au contrôle) et "
    "GO-2026-11-22-64 (forme mesurée : conservation du déplacement cumulé sous "
    "fragmentation). L'énoncé central reste cité, non revendiqué ; ses pages "
    "viennent de R-4767. Voisins à citer : R-4771.",
))

# L-5 — section 5, hypothèse L du papier A
ENTREES.append((
    "**L — lemme d'additivité** (mentionné, non revendiqué ; la note 0,75 est "
    "caduque). Section 3.",
    "**L — lemme d'additivité** (" + FORMULE + " ; énoncé central cité, non "
    "revendiqué ; la note 0,75 est caduque ; application non calibrée). "
    "Section 3.",
    "GO-2026-11-24-18. La note 0,75 reste caduque. L'application n'est pas "
    "calibrée : son antériorité n'est pas établie.",
))

# L-6 — section 10, tâches de la phase 0
ENTREES.append((
    "(tâche de la version 2, nom gardé ; les deux énoncés ne sont plus "
    "revendiqués, section 3)",
    "(tâche de la version 2, nom gardé ; les deux énoncés ne sont plus "
    "revendiqués comme théorèmes ; le lemme est " + FORMULE + " ; section 3)",
    "GO-2026-11-24-18. La phrase disait le lemme non revendiqué, sans réserve. "
    "La tâche et son nom ne changent pas.",
))

# L-7 — section 15, question du co-auteur
ENTREES.append((
    "sans objet pour le lemme, qui n'est plus revendiqué (section 3)",
    "sans objet pour le lemme, qui est " + FORMULE + " et sans théorème "
    "(section 3)",
    "GO-2026-11-24-18. La phrase excluait aussi l'application. La question "
    "reste sans objet : l'application est une mesure.",
))

LIEUX = [
    "section 0, défaut D-b",
    "section 2, tableau des trois papiers, ligne des hypothèses",
    "section 3, statut de ce qui suit",
    "section 3, paragraphe du lemme",
    "section 5, hypothèse L du papier A",
    "section 10, tâches de la phase 0",
    "section 15, question du co-auteur",
]
