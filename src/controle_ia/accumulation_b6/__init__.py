"""Barreau 6, forme faible (« accumuler bat le score action par action ») : code de lecture, marque `ACCB6`.

Texte joué : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-brouillon2.md` (sha256
`9f070e31734be21d753967e0df11ee2aae174906d170a36f27a45c52714494c3`), chemin visé au scellement `prereg/accumulation-barreau6-v1.md`.
Modules : `etats_v1` (états des couples et des jeux, séquence fixée), `phrases_v1` (phrases gelées), `garde_v1` (registre propre,
journal propre, garde d'ouverture, aiguillage G-1 à G-4), `lecture_v1` (entrées, épisodes, calculs, résultat scellé, commande).
Aucune fonction de T0.7 n'est modifiée ; celles qui sont appelées le sont telles quelles.
"""
