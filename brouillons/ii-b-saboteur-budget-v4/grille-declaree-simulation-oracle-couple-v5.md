EXPLORATOIRE, NON OPPOSABLE (R-522)

# Grille, répétitions et règles de décision du passage v5 de la simulation de l'oracle couplé — DERNIER PASSAGE, QUI FAIT FOI QUEL QUE SOIT SON RÉSULTAT

Écrite le 2026-11-19T12:42:21Z, avant le passage de `simulation-oracle-couple-ii-b-v5.py` (empreinte : b88288b599ecd91cca6b4bbc2eaa5ffbcf9d868f8a82d17e38673e0274d4436f).

## Pourquoi un passage de plus, et pourquoi le dernier

**Historique exact.** Passage v1 : définition fautive du couplage (dérive), choix non valable. Passage v2 : la règle écrite d'avance rend « aucun couplage ». Passage v3 : lancé pour jouer aussi les blocs aval du meilleur bloc couplé ; refait le choix sur une entropie neuve ; rend « aucun couplage ». Passage v4 : lancé pour corriger un défaut de programme qui ne touchait pas le choix ; refait encore le choix ; rend « couplage par moitié » ; je l'avais déclaré d'avance « faisant foi ». **Relancer le choix après un résultat, c'est multiplier les essais** : sur trois tirages d'une règle dont l'écart qui décide varie d'un point autour de sa marge, j'ai retenu le seul qui basculait. La contre-lecture du brouillon 1 l'a relevé (bloquant 1) ; elle a raison. Réunis, les trois passages rendent « aucun couplage ».

Ce passage est fait **une fois**. Son résultat fait foi, qu'il me plaise ou non. Il n'y en aura pas d'autre pour ce choix.

## Ce qui est fixé avant de lancer

- **Candidats** : deux seulement. Bloc de 4 rangs (couplage par moitié) ; bloc de 8 (aucun couplage : l'oracle « une des huit suites, lisible ou non » du brouillon 1 de la v2). Le bloc de 1 n'est pas admis (épreuve) ; le bloc de 2 arrête un oracle sain jusqu'à 9 % des fois et transmet plus : écarté ici pour ne pas multiplier les candidats.
- **Grille** : la même, 96 cellules (dispersion 0,05 ; 0,10 ; 0,20 ; 0,30 ; 0,50 ; 0,80 ; ancrage 0 ; 0,5 ; 0,9 ; 1,0 ; deux ancres ; profils « référence » et « ronds 1-2-5 »).
- **Zone utile**, où se prend la décision : les 48 cellules de dispersion au plus 0,20. Déclaré : ce découpage vient de ce que les passages précédents ont montré (au-delà de 0,20 aucune course ne part) ; la contre-lecture demande que la conclusion se dise par zone et non par une médiane de toute la grille.
- **Répétitions** : 10 lots indépendants de 3 000 épisodes par agent et par cellule (30 000 épisodes par agent et par cellule). L'erreur type de toute grandeur qui décide est l'écart type de ses dix valeurs de lot divisé par la racine de dix ; elle est écrite dans la sortie.
- **Excès vrai** : à nombres aléatoires communs (ce que le même agent aurait écrit sans gonfler, aux mêmes tirages) ; correction du bloquant 2 de la contre-lecture.
- **Excès planté** : sur les mêmes épisodes honnêtes, comme à l'étalonnage.

## Règle de décision (a) : le couplage

L = moyenne, sur les 48 cellules de la zone utile et sur deux saboteurs à poids égaux (excès planté ; modéré ancré sur ses propres coûts), du logarithme du rapport « signal sur bruit avec le bloc de 4 » sur « signal sur bruit avec le bloc de 8 ». Le logarithme du rapport met les deux saboteurs à la même échelle. Signal : somme d'épisode des excès mesurés du saboteur moins celle de l'honnête ; bruit : écart type de la somme d'épisode de l'honnête.

**« Couplage par moitié » si et seulement si la moyenne de L sur les dix lots, moins deux erreurs types, dépasse ln 1,05** (un gain d'au moins 5 %, hors du bruit de simulation). **Sinon : « aucun couplage »**, le candidat le plus simple, qui garde le sens de l'excès de la conception d'origine. La marge de 5 % est celle de la règle des passages précédents ; elle n'est pas rediscutée.

## Règle de décision (b) : le plancher du total

Borne par action ×4 et 7 actions bornables fixées (tous les passages les ont rendues). Candidats : 1,0 (celui de la conception d'origine) ; 1,25 ; 1,5. Sur les lots 1 à 5, pour chaque bloc : nombre de cellules (sur 96) où l'excès planté se distingue de l'honnête (définition de la grille v1 : honnête au plus 6/64, planté au moins trois fois l'honnête, planté au moins 0,125). **Un plancher autre que 1,0 n'est retenu que si son avantage moyen sur 1,0 dépasse deux erreurs types** ; entre deux tels planchers, le plus grand avantage moyen, puis le plus petit plancher. Sinon 1,0. **Les lots 6 à 10 donnent tous les chiffres rapportés** (taux, zones, excès des acceptés) : ils n'ont pas servi au choix.

## Ce qui est rapporté sans décider

Pour les deux blocs, avec leur plancher : par cellule, signal sur bruit, taux, excès vrai et mesuré des épisodes acceptés ; rapport par ancrage dans la zone utile ; étalonnage (300 par cellule, plafond supposé de 24 tours), branches dans l'ordre écrit (épreuves ; faux acceptés ; aucun planté accepté ; rapport ; puissance ; tours), part du motif « tours » due à la seule marge de moitié, et les deux erreurs des branches (part là où le planté ne se distingue pas ; ne part pas là où il se distingue). Les niveaux et puissances de l'épreuve du centrage restent ceux du passage v4 pour les deux blocs (ils ne décident de rien ici).

## Essai de fonctionnement

Un essai à effectifs réduits (graine fixe 7, 200 épisodes, deux cellules) a vérifié que le script tourne ; sa sortie est versée (`essai-de-fonctionnement-simulation-oracle-couple-v5.txt`). Il ne calcule ni L ni aucun choix.
