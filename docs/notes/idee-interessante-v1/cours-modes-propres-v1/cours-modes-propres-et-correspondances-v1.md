---
title: "Cours accéléré : les modes d'un graphe et les correspondances entre graphes"
---

Classe C, note pédagogique de la session mère, 24 novembre 2026, sur la demande de Lazar. Les références sont à vérifier sur PDF avant toute citation dans une pièce du programme (R7).

## 0. L'idée en une phrase

Un mode est une façon de vibrer propre à une structure. Les modes d'un graphe forment un système de coordonnées que le graphe se donne lui-même. Une bonne correspondance entre deux graphes envoie chaque mode de l'un sur le mode de même « fréquence » de l'autre.

## 1. Avec les mains : la corde

Une corde tendue, fixée aux deux bouts, a des façons naturelles de vibrer : le fondamental (un seul ventre), puis deux ventres avec un nœud au milieu, puis trois ventres, et ainsi de suite. Deux faits suffisent.

- Toute forme de la corde, même biscornue, est une somme de ces formes de base, chacune avec un poids. Les poids sont les coordonnées de la forme : c'est la série de Fourier.
- Chaque forme de base a sa note. Plus elle a de ventres, plus elle ondule vite, plus la note est aiguë.

Un mode, c'est cela : une forme qui, laissée à elle-même, garde sa forme et ne fait que changer d'amplitude.

## 2. De la corde au graphe (version rigoureuse)

Remplaçons la corde par n perles reliées par des ressorts : c'est un graphe en ligne. Une « forme » devient une liste de n nombres `x_1, …, x_n`, un par nœud. On l'appelle un signal sur le graphe.

Pour un graphe quelconque, avec des nœuds i et des liens pondérés `w_ij ≥ 0`, on définit le laplacien `L = D − W`. Ici, W est la matrice des poids, et D la matrice diagonale des degrés, `d_i = Σ_j w_ij`. Une seule formule à retenir :

`xᵀ L x = Σ sur les liens (i,j) de w_ij (x_i − x_j)²`

Le membre de droite est l'énergie du signal. Elle est petite quand le signal varie peu d'un nœud à ses voisins, et grande quand il saute d'un lien à l'autre.

Sur la ligne de perles, `(L x)_i = 2 x_i − x_(i−1) − x_(i+1)`. C'est la dérivée seconde discrète, au signe près : le laplacien du graphe est la version discrète de l'opérateur qui gouverne la corde.

**Base d'harmoniques, définition.** L est symétrique et positive, car l'énergie n'est jamais négative. Par le théorème spectral, il existe une base orthonormée de signaux `v_1, …, v_n` et des nombres `0 = λ_1 ≤ λ_2 ≤ … ≤ λ_n` tels que `L v_k = λ_k v_k`.

- Les `v_k` sont les modes propres, les harmoniques du graphe.
- `λ_k` joue le rôle du carré de la fréquence.
- « Orthonormée » veut dire deux choses. Chaque mode est de norme 1. Deux modes différents sont orthogonaux, `Σ_i v_j(i) v_k(i) = 0` : ils sont indépendants, aucun n'est une combinaison des autres.

**Vérification sur l'anneau.** Pour n perles disposées en cercle, les modes sont exactement `cos(2πkj/n)` et `sin(2πkj/n)`, avec `λ_k = 2 − 2 cos(2πk/n)`, à peu près `(2πk/n)²` pour les petits k. Ce sont les modes de Fourier : sur l'anneau, la transformée de Fourier d'un graphe est la transformée de Fourier ordinaire.

**Ce qu'est un mode sur un graphe quelconque** (principe du minimax de Courant et Fischer) :

- `v_1` est le signal d'énergie minimale : c'est la constante, d'énergie nulle, si le graphe est d'un seul tenant.
- `v_2` est le signal d'énergie minimale parmi ceux qui sont orthogonaux à la constante, c'est-à-dire de somme nulle. Il doit être positif quelque part et négatif ailleurs. Pour garder une énergie basse, il ne change de signe qu'à travers peu de liens. Il coupe donc le graphe le long de sa coupure la plus faible, en deux régions peu reliées entre elles (Fiedler 1973 ; l'inégalité de Cheeger rend ce lien précis).
- `v_3` est la meilleure coupure suivante, indépendante de la première, et ainsi de suite.
- Les derniers modes oscillent d'un voisin à l'autre : ils décrivent du détail, ou du bruit.

**Les coordonnées d'un concept.** On garde les m premiers modes non constants et on donne au nœud i la liste `(v_2(i), v_3(i), …, v_(m+1)(i))`. C'est le plongement spectral (« Laplacian eigenmaps », Belkin et Niyogi 2003). Deux concepts reliés par de nombreux chemins courts reçoivent des coordonnées proches, parce que les modes lents varient peu à travers un lien.

**Ce qu'il faut en retenir :**

- une dimension, c'est un mode `v_k`, c'est-à-dire une manière indépendante dont le domaine se partage : une ligne de faille ;
- la coordonnée k du concept i dit de quel côté de la faille k il se trouve, et à quelle profondeur ;
- c'est une propriété du graphe entier, pas du concept. Ajoutez des liens loin de i : les failles bougent, et la coordonnée de i change sans que i ait changé. C'est comme « être dans la moitié est » d'un réseau ferré, qui dépend de toutes les lignes.

## 3. Deux graphes, une correspondance, la matrice C (version rigoureuse)

Le graphe A a pour modes `a_1, a_2, …`, et le graphe B a pour modes `b_1, b_2, …`. Une correspondance φ envoie les nœuds de A sur ceux de B.

Pour simplifier, prenons-la bijective, avec n nœuds de chaque côté. Elle transporte un signal x sur A en un signal `P x` sur B : en φ(i), on met la valeur que x avait en i. P est une matrice de permutation.

Transportons le mode `a_j` de A. `P a_j` est un signal sur B, qu'on écrit dans la base des modes de B :

`P a_j = Σ_k C_kj b_k`, avec `C_kj = ⟨b_k, P a_j⟩`

La matrice C est la correspondance φ écrite dans les deux bases d'harmoniques. Sa case (k, j) dit combien du mode j de A atterrit sur le mode k de B.

**Pourquoi C est diagonale quand φ conserve la structure.** « φ conserve la structure » veut dire que chaque lien de A devient un lien de B de même poids. Autrement dit, `P L_A = L_B P` : φ commute avec le laplacien. Notons `Λ_A` et `Λ_B` les matrices diagonales des fréquences. Alors :

`Λ_B C − C Λ_A = 0`

Preuve en une ligne :

- d'un côté, la case (k, j) de `Λ_B C − C Λ_A` vaut `b_kᵀ (L_B P − P L_A) a_j`, qui est nul ;
- de l'autre, cette même case vaut `C_kj (λ_k^B − λ_j^A)` ;
- donc `C_kj = 0` dès que les deux fréquences diffèrent : C ne relie que des modes de même fréquence.

Si toutes les fréquences sont distinctes, C est diagonale, avec ±1 sur la diagonale : un mode transporté est le mode de même rang, au signe près. Si une fréquence se répète, parce que le graphe a des symétries, C est diagonale par blocs.

**Version approchée, la seule utile en pratique.** Si φ conserve presque la structure, posons `ε = ‖L_B P − P L_A‖`. Alors :

`|C_kj| ≤ ε / |λ_k^B − λ_j^A|`

Les cases qui relient des fréquences très différentes sont minuscules. Seules celles qui relient des fréquences voisines peuvent être grandes : C est concentrée sur une bande autour de la diagonale. C'est le cœur des « applications fonctionnelles » en géométrie des formes (Ovsjanikov et al. 2012) : on y cherche justement une C qui commute avec les laplaciens.

**Deux limites, honnêtement :**

- des modes de fréquences très proches se mélangent facilement : on compare alors des groupes de modes, pas des modes isolés ;
- nos graphes de concepts ont des liens typés et orientés, que le laplacien simple ne voit pas. Il faut des versions par type de relation, ou des laplaciens faits pour les graphes orientés. C'est un chantier, pas un acquis.

## 4. À la manière d'un physicien

Chaque graphe est un tambour fait de masses reliées par des ressorts. Ses modes sont ses façons propres de vibrer, chacune avec sa note.

Si deux tambours ont la même forme et qu'on a bien posé l'un sur l'autre, un mode pur de A, reporté sur B, est encore un mode pur de B, à la même note. Il ne « bave » sur aucune autre note : c'est la diagonale.

Si l'alignement est faux, comme une peau collée de travers, une note pure de A devient un accord de plusieurs notes de B : des cases hors de la diagonale.

La question de Kac (1966), « peut-on entendre la forme d'un tambour ? », dit que les notes sont presque une empreinte de la forme. Presque seulement : il existe des tambours différents, et des graphes différents, qui sonnent pareil.

## 5. Avec les mains, pour nos domaines

Les modes d'un domaine sont ses lignes de faille, rangées par importance : la grande coupure en deux, puis la suivante, et ainsi de suite. La matrice C est la table de correspondance des failles.

- Une bonne analogie envoie la grande faille de A sur la grande faille de B, la deuxième sur la deuxième : la table est diagonale.
- Une mauvaise analogie envoie une faille de A à cheval sur plusieurs failles de B : la table est brouillée.

**La « dimension cachée ».** Une analogie partielle a une table propre sur certaines lignes seulement. Supposons qu'une ligne propre corresponde à une petite faille, qui n'a rien de spécial ni dans A ni dans B. Elle est alors invisible de chaque côté, et seule la correspondance révèle que c'est la même faille.

C'est l'idée de l'analyse des corrélations canoniques (Hotelling 1936). Prenons deux micros dans une pièce bruyante : chacun est dominé par son bruit local, mais, une fois les deux enregistrements alignés dans le temps, ce qu'ils partagent ressort. Ici, l'alignement, c'est φ. C'est une interprétation à tester, pas un théorème.

## Références (à vérifier sur PDF)

- Belkin, M. et Niyogi, P. (2003), « Laplacian eigenmaps for dimensionality reduction and data representation », *Neural Computation*.
- Fiedler, M. (1973), « Algebraic connectivity of graphs », *Czechoslovak Mathematical Journal*.
- Hotelling, H. (1936), « Relations between two sets of variates », *Biometrika*.
- Kac, M. (1966), « Can one hear the shape of a drum? », *American Mathematical Monthly*.
- Ovsjanikov, M. et al. (2012), « Functional maps: a flexible representation of maps between shapes », *ACM Transactions on Graphics*.
