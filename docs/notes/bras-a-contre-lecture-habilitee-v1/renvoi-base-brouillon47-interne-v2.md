# Renvoi de la base, brouillon 47 — vérification habilitée — pièce interne — v2 (complément)

Écrit le 2026-11-22 par le même lecteur habilité (Claude Opus 5.5). Accès étendu par R-4910, puis à la section 6.9 sur le mot de la mère. La v1 (`renvoi-base-brouillon47-interne-v1.md`, `ced1626d…`) reste en vigueur, inchangée. La présente pièce ne fait que clore ses deux vérifications restées hors d'accès. Pièce interne, classe C.

**Texte lu** : brouillon 47, `f59f6b4ed2b1198c3781badf83692d593ed4ade0df5baa9f0e4ea8b1827a6cb9`, sections 6.9 (lignes 852 à 915) et 7.7 (lignes 1065 à 1075). **Document de la base** : `prereg/T0.8-base-A-mots-et-cout-v1.md`, `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d`, sur la branche principale. C'est le texte que le programme de la base nomme comme le sien (`TEXTE_BASE_A` de la pièce source) et qu'inscrit le registre des scellements (`SCELLEMENT-T08-BASE-A`, 2026-11-10T12:21:55Z).

## 1. R-BA2 et R-BA2b recopiées en 7.7 — vérifié

Comparaison par programme : le texte entre guillemets de premier niveau, guillemets internes compris, dans la 7.7 (« Son texte, à la lettre » et « Sa voisine R-BA2b ») contre la phrase gelée des lignes BA-L3 et BA-L3b du document de la base (table des lignes, lignes 133 et 134).
- **R-BA2 : égaux, caractère pour caractère** (221 caractères).
- **R-BA2b : égaux, caractère pour caractère** (122 caractères).

Les deux phrases du code de la base (`PHRASES_BA["BA-L3"]` et `PHRASES_BA["BA-L3b"]` de la pièce source, `9dbcc55c…`) se trouvent aussi, à la lettre, entre guillemets, dans le document de la base. La 7.7 dit encore « sans que j'aie ouvert ce document » et « le contenu de la réserve reste à vérifier par le lecteur habilité » : c'est fait ici. Le rédacteur peut retirer cette dernière phrase au profit d'un renvoi à cette vérification ; ce n'est pas une correction exigée.

## 2. Lettre de 6.9 sur l'unité de l'aire décisive et la classe honnête — vérifié

La 6.9 écrit : l'unité de l'aire est **l'action pour quatre moniteurs** (classifieur lexical, moniteur boîte noire par action, classifieur de surface, juge d'une autre lignée) et **l'épisode pour l'agrégateur séquentiel**. Elle précise que ce choix fixe l'unité de l'aire décisive (condition (b) de « ne repère pas », valeurs p). Pour l'aire conditionnelle, elle dit : « toutes les lignes d'étiquette 0 et les lignes d'étiquette 1 des épisodes retenus, par pli, puis la moyenne des deux plis ». Pour la permutation, elle dit que les actions d'un épisode gardent ensemble l'étiquette tirée pour lui.

Le code du module v11 rend exactement cela (v1, points 1 à 3) :
- unités d'action pour les quatre, d'épisode pour l'agrégateur ;
- aire égale à la moyenne des aires des deux plis (fonction gelée) ;
- toutes les unités honnêtes, à l'étiquette 0, écrites à chaque dose dans le fichier par unité ;
- permutation par épisode, avec l'échange dans chaque paire.

La réserve du point 2 de la v1 est levée.

## 3. Lignes du verdict de discrétion corrigées par la contre-lecture 10 — vérifié

Le différentiel du brouillon 46 au brouillon 47 (`difflib`, ligne à ligne) change les lignes 1, 3, 522, 551-552, 599, 772, 923, 973, 1008, 1194, 1201, 1228, 1454, 1462, 1464-1465, 1468, 1473-1474, 1485 et 2543. **Aucune ligne de 6.9, de 6.10, de 6.12, de la table C ni de 7.7 ne change.**

Les lignes changées que la v1 n'a pas vérifiées portent :
- sur les lecteurs et le juge des ancres (522, 551-552, 1194, 1465, 1485) ;
- sur l'instrument de l'appariement (599) ;
- sur le déclencheur d'un repli (772) ;
- sur la ligne A8 de la table A (1008) ;
- sur les cases « nœuds » et « familles » (1462, 1464).

Aucune ne nomme la discrétion, la table C, la base « mots et coût » ni la base (A). Elles ne touchent donc pas le verdict de discrétion. Les lignes qui le touchent (1201, 1473) sont vérifiées en v1.

## Verdict d'ensemble (v1 et v2 lues ensemble)

**Vérifié**, au défaut mineur près de la ligne 1471 (préparation citée en version 1), que la relance corrige au brouillon 48. Aucun défaut de code. Restent à relire, sur leurs seules lignes : la correction de la ligne 1471, et M-6 et M-7 après le mot de Lazar.

Cette pièce ne dépense rien et n'autorise rien.
