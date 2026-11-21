"""Barreau 6, forme faible (« accumuler bat le score action par action ») : code de lecture, marque `ACCB6`.

Texte joué : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat2.md` (sha256
`0716d3d52fd60f76b51c921ef8284580d70ddc587d855cfbc12381c1667baee1` ; R-2278, VB6-5 ; le brouillon 2, `9f070e31…`, avant lui), chemin visé
au scellement `prereg/accumulation-barreau6-v1.md`.
Modules : `etats_v1` (états des couples et des jeux, séquence fixée), `phrases_v1` (phrases gelées), `garde_v1` (registre propre,
journal propre, garde d'ouverture, aiguillage G-1 à G-4), `lecture_v1` (entrées, épisodes, calculs, résultat scellé, commande),
`code_accb6_v1` (contrôle du code exécuté contre `CODE-ACCB6`).
Aucune fonction de T0.7 n'est modifiée ; celles qui sont appelées le sont telles quelles.
"""
