# Proposition E — Critique croisée de méthode

**OBSERVÉ-NON-AUDITÉ — Pièces :** les quatre conceptions sont présentes et ne paraissent pas coupées. La formule exacte de la valeur e n’est pas fournie ; je n’en reconstruis pas la garantie.

**Statut des critiques : HYPOTHÈSE.** Les objections ci-dessous sont des analyses conditionnelles à tester, non des résultats expérimentaux. Les choix attribués aux propositions sont **RAPPORTÉS** par leurs textes.

**Notation proposée — HYPOTHÈSE :** \(P(dx)\) désigne la distribution des traits, \(p(y\mid x)\) la loi du monde, \(q,r\) des lois candidates, \(Q(dx)\) la distribution des sondes. Posons
\[
L_p(q)=\mathbb E_{Pp}\log q(Y\mid X),\qquad
G_{\mathcal N}(q)=L_p(q)-\sup_{r\in\mathcal N}L_p(r).
\]
Les seuils symboliques ci-dessous sont à préenregistrer ; aucune nouvelle valeur numérique empirique n’est avancée.

**Règle d’inférence proposée — HYPOTHÈSE :** pour chaque contrôle, opposer des hypothèses complémentaires sur un paramètre, par exemple \(H_A:\theta\leq\varepsilon\) contre \(H_B:\theta>\varepsilon\). Un intervalle entièrement d’un côté du seuil réfute statistiquement l’autre hypothèse, au risque préenregistré. Un intervalle traversant le seuil est **indécis**, pas une validation. L’absence d’échec observé ne réfute pas une probabilité d’échec positive arbitrairement petite.

## Sur la proposition A

### (a) Défauts de méthode

**HYPOTHÈSE — L’étalon oracle n’est pas dispensé de validation.** A définit la couverture par la baisse du gain sur une marginale après neutralisation d’une composante, puis qualifie cet instrument d’étalon. Or l’ablation modifie potentiellement simultanément la cible, sa marginale et la relation entre composantes. Une baisse du gain ne démontre donc pas que la candidate représentait la composante neutralisée. Le contrôle « composante absente » est nécessaire, mais insuffisant si l’absence est définie par la même décomposition utilisée pour construire l’instrument.

**HYPOTHÈSE — La détectabilité annoncée n’est pas celle mesurée.** Promouvoir la loi complète du monde ne démontre pas que chaque composante est détectable séparément. Un effet dominant peut porter toute la puissance. La calibration doit isoler le gain incrémental de chaque composante contre l’archive pertinente, notamment après enrichissement de celle-ci.

**HYPOTHÈSE — Le nul réduit change la définition opérationnelle d’une copie.** Archiver un représentant aléatoire n’autorise pas à retirer les autres lois du dispositif anticopie. Une sœur écartée peut être proche du représentant et néanmoins apporter un gain testable contre lui. Il faut distinguer compression de la vue, compression du comptage et compression du nul. Le succès de la première ne justifie pas la troisième.

**HYPOTHÈSE — Calibration circulaire et sélection aval.** Ajuster le seuil de distance pour prédire le refus du juge produit un instrument de proximité au **juge**, pas nécessairement de redondance probabiliste. Employer ensuite ce regroupement dans une mesure de composition des agents crée une dépendance indirecte à ce juge ; sa compatibilité avec N-053/N-058 doit être examinée, pas présumée.

**HYPOTHÈSE — Plusieurs duels n’opposent pas des causes exclusives.** Monde pauvre et proposeurs corrélés peuvent agir conjointement. Dans E4, gain utile et exploitation de recombinaisons peuvent augmenter ensemble ; aucune amélioration peut aussi survenir. Dans E5, épuisement dès la première génération et couverture complète sont compatibles avec plusieurs explications. Un contraste causal exige une manipulation appariée, pas seulement un seuil de couverture.

### (b) Conditions probabilistes de perte de puissance ou de non-jugabilité

**HYPOTHÈSE — Couverture par ablation.** Soit \(p_{-c}\) la loi après ablation et \(m_p(y)=\int p(y\mid x)P(dx)\). Le score proposé dépend de
\[
A_c(q)=
[L_p(q)-L_p(m_p)]
-
[L_{p_{-c}}(q)-L_{p_{-c}}(m_{p_{-c}})].
\]
Même si \(q\) ne dépend pas du trait associé à \(c\), \(A_c(q)\) peut être non nul si \(p_{-c}\) modifie la distribution de \(Y\). Le critère relatif devient instable lorsque \(L_p(q)-L_p(m_p)\) approche zéro. Il est non identifiable si deux paramétrisations de \(p\), égales \(P\)-presque sûrement, donnent des \(p_{-c}\) différents.

**HYPOTHÈSE — Distance et archivage.** Si \(Q(B)=0\), \(P(B)>0\) et \(q=r\) hors de \(B\), alors \(d_Q(q,r)=0\) malgré un écart de score sous \(Pp\). Même avec \(Q=P\), une faible distance Jensen-Shannon ne borne pas uniformément le regret logarithmique lorsque les probabilités candidates approchent zéro. La compression devient dangereuse dès que
\[
d_Q(q,r)\leq\tau
\quad\text{mais}\quad
G_{\mathcal N_{\mathrm{réduit}}}(q)>\delta.
\]

**HYPOTHÈSE — Détectabilité.** Pour un rapport de vraisemblance contre une loi fixe \(r\), posons
\[
Z=\log(q(Y\mid X)/r(Y\mid X)),\quad
\mu=\mathbb EZ,\quad \sigma^2=\operatorname{Var}(Z).
\]
Un seuil \(h\) ne se calibre pas avec \(n\mu\) seul : la dispersion \(\sqrt n\,\sigma\) compte. Si \(n\mu-h\) est petit devant cette dispersion, la puissance reste incertaine. Cette approximation ne s’étend pas sans justification à une valeur e contre un nul composite.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles requis :**

- Ablations de paramètres sans effet sur \(p\), et décompositions différentes donnant exactement le même \(p\) : la couverture ne doit pas changer arbitrairement.
- Candidates ignorant une composante dont l’ablation modifie néanmoins la marginale : mesure du taux de fausse couverture.
- Réinjection de **toutes les sœurs supprimées**, pas seulement des représentants, contre le nul réduit.
- Lois ne différant que sur une région de faible probabilité, avec comparaison des distances et des regrets logarithmiques.

Pour la compression, le duel pertinent est \(H_A\) : le taux de réadmission des sœurs reste sous la tolérance ; \(H_B\) : il la dépasse. Aucune réadmission observée ne suffit sans borne d’incertitude.

## Sur la proposition B

### (a) Défauts de méthode

**HYPOTHÈSE — Conservation des groupes vraie par construction.** Regrouper les fiches, garder un représentant par groupe, puis compter ces mêmes groupes peut afficher une conservation parfaite alors qu’une information probabiliste utile a disparu. L’évaluation doit porter sur une propriété indépendante du partitionnement ayant servi à supprimer les fiches.

**HYPOTHÈSE — Le maximum de valeurs e exige une procédure explicitée.** B choisit le représentant ayant la plus grande valeur e. Si ce maximum est traité comme une nouvelle valeur e avec multiplicité réduite, sa validité n’est pas acquise. Si toutes les fiches ont d’abord été testées avec la multiplicité initiale, le problème est différent : il reste à justifier la garantie revendiquée sur le sous-ensemble finalement retenu. « Post-traitement » ne suffit pas comme preuve.

**HYPOTHÈSE — Le contrôle K1-riche n’est pas un nul garanti.** Une loi utilisant tous les traits peut être mal spécifiée. Son inclusion dans l’archive n’implique pas qu’aucune candidate ne puisse la dépasser. Il faut un monde dont la loi conditionnelle appartient effectivement au nul.

**HYPOTHÈSE — Le nombre de groupes ne valide pas leur partition.** Retrouver le nombre attendu de groupes peut masquer une fusion erronée compensée par une séparation erronée. Les erreurs par paire et la perte de score doivent être mesurées.

**HYPOTHÈSE — Confusions de traitements.** Modifier le nombre d’appels, la température et les formulations ne permet pas d’attribuer le gain au seul nombre d’appels. Égalité du nombre de fiches ne signifie pas égalité du coût. Les agrégats de coût v67 ne permettent pas d’isoler le coût des appels de proposeurs.

**HYPOTHÈSE — Une recombinaison hors nul n’est pas nécessairement fausse.** Il faut séparer vérité prédictive, nouveauté relative à l’archive et validité du test. Le statut grammatical ne tranche aucune de ces propriétés.

### (b) Conditions probabilistes de perte de puissance ou de non-jugabilité

**HYPOTHÈSE — Distance moyenne.** Définissons
\[
d_1(q,r)=\mathbb E_P\sum_y|q(y\mid X)-r(y\mid X)|.
\]
Si les lois diffèrent seulement sur \(B\),
\[
d_1(q,r)=P(B)\,
\mathbb E[\|q-r\|_1\mid B].
\]
Une différence conditionnelle forte devient donc indiscernable au seuil fixé lorsque \(P(B)\) est faible. Avec \(M\) sondes indépendantes, la probabilité de ne jamais observer \(B\) vaut \((1-P(B))^M\).

**HYPOTHÈSE — Proximité moyenne contre score logarithmique.** Si \(p(y\mid x)>0\), \(q(y\mid x)\to0\) et \(r(y\mid x)\) reste positif, le regret de \(q\) peut diverger tandis que \(d_1(q,r)\) reste faible. Sans borne inférieure des probabilités, le seuil L1 ne garantit pas l’interchangeabilité pour le juge ou le test de mort.

**HYPOTHÈSE — Calibration du nombre de groupes.** Si \(\widehat{\mathcal C}\) et \(\mathcal C\) sont deux partitions, l’égalité
\[
|\widehat{\mathcal C}|=|\mathcal C|
\]
n’impose pas l’égalité des partitions. La corrélation de rang devient indéfinie si le nombre cible est constant entre mondes ; elle ne mesure pas non plus la calibration absolue.

**HYPOTHÈSE — Faux positifs.** L’estimateur \(V/R\) nécessite une convention lorsque \(R=0\). Un taux par fiche, une proportion de faux rejets parmi les rejets et une probabilité d’au moins un rejet ne sont pas le même paramètre.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles requis :**

- Monde où \(p\) est exactement un membre du nul, avec toute la procédure de sélection du maximum.
- Lots comportant simultanément une fausse fusion et une fausse séparation, afin de tromper volontairement le seul comptage.
- Lois proches en L1 mais très différentes en risque logarithmique, notamment sur événements rares.
- Rejeu des mêmes fiches archivées pour comparer les regroupeurs, sans nouveaux appels de modèles.
- Contrôle A/A à coût réellement mesuré pour les plans d’appels.

Le duel pour l’instrument doit porter sur un **taux d’erreur de partition** sous ou au-dessus d’une tolérance, pas sur la seule égalité du nombre de groupes.

## Sur la proposition C

### (a) Défauts de méthode

**HYPOTHÈSE — Le traitement M1 n’est pas identifié.** Quotas de formes, exclusion de traits et masquage d’archive changent simultanément la recherche autorisée et l’information disponible. Une hausse de copies peut provenir de l’ignorance de l’archive ; une baisse de découvertes, de l’exclusion d’un trait nécessaire. Il faut des ablations séparées avant attribution.

**HYPOTHÈSE — Préférence pour la simplicité non neutre.** Choisir le représentant avant les données protège contre une sélection sur les résultats du juge, mais ne protège pas contre la perte d’information. La complexité de la représentation n’est pas une mesure de proximité avec \(p\).

**HYPOTHÈSE — Définition spectrale incohérente.** Le texte annonce une entropie de Rényi d’ordre deux, puis fournit l’exponentielle de l’entropie de Shannon. Ces fonctionnelles ne sont pas interchangeables. Il faut en choisir une, démontrer les conditions sur le noyau et définir le cas de l’ensemble vide.

**HYPOTHÈSE — « Couverture causale » insuffisamment définie.** Ablater des traits dans une candidate ne définit pas une intervention sur le monde. Des traits corrélés peuvent se substituer prédictivement ; une loi conditionnelle plantée ne fournit pas, à elle seule, une structure causale identifiable.

**HYPOTHÈSE — Extension du nul et batterie ne coïncident pas.** Un nul ajouté sur une grille de seuils ne couvre pas automatiquement les produits, compositions ou coupures hors grille. Rejouer les attaques ayant guidé cette extension mesure l’ajustement à ces attaques, pas la couverture d’une classe indépendante.

**HYPOTHÈSE — Extrapolation multigénération invalide sans branches distinctes.** Un rejeu a posteriori de la première génération peut mesurer ses pertes immédiates. Il ne reconstitue pas les propositions suivantes, puisque les archives servies ont changé.

### (b) Conditions probabilistes de perte de puissance ou de non-jugabilité

**HYPOTHÈSE — Score spectral.** Pour utiliser \(-\sum_i\lambda_i\log\lambda_i\), il faut \(\lambda_i\geq0\) et \(\sum_i\lambda_i=1\). La procédure est non définie sans convention pour \(k=0\). Même avec un noyau admissible, changer les proportions de répétition de lois identiques peut changer le spectre sans changer l’ensemble des lois distinctes.

**HYPOTHÈSE — Quasi-uniformité.** Pour
\[
q_i(y\mid x)=u(y)+\epsilon v_i(y,x),
\qquad \sum_yv_i(y,x)=0,
\]
avec \(u(y)>0\), les divergences Jensen-Shannon sont d’ordre \(\epsilon^2\). Lorsque \(\epsilon\to0\), le nombre spectral tend vers celui d’un lot identique, même si les directions \(v_i\) diffèrent.

**HYPOTHÈSE — Ablation.** Si \(X_a=X_b\) presque sûrement, une dépendance à \(X_a\) et une dépendance à \(X_b\) peuvent donner exactement la même loi conditionnelle. Leur attribution séparée n’est pas identifiable sous \(P\).

**HYPOTHÈSE — Extension du nul.** Si \(q\in\mathcal N_{\mathrm{étendu}}\), alors \(G_{\mathcal N_{\mathrm{étendu}}}(q)\leq0\), même lorsque \(q=p\). Son absence de promotion n’est donc pas une perte de puissance pour une alternative au nul. Pour parler de puissance, imposer un gain strictement positif contre ce nul.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles requis :**

- Répétition déséquilibrée de lois identiques pour mesurer la sensibilité du score aux fréquences.
- Paramétrisations distinctes donnant exactement les mêmes distributions conditionnelles pour tester la couverture.
- Attaques hors grille et compositions non utilisées pour construire le nul.
- Comparaison archive complète/masquée sans quotas, puis quotas sans masquage.
- Contextes portant des nombres issus légitimement de l’archive, mais aussi fuites d’information sans constante numérique copiée.

Pour le scanner, le duel doit porter sur ses taux d’erreur dans une classe de fuites définie. Une réussite sur des constantes injectées ne réfute pas l’existence de fuites structurelles.

## Sur la proposition D

### (a) Défauts de méthode

**HYPOTHÈSE — \(D_u\) peut encore compter plusieurs variantes du même gain.** Plusieurs candidates éloignées entre elles peuvent toutes battre une bibliothèque faible en exploitant la même amélioration. Le contrôle oracle élimine certaines diversités inutiles, mais ne transforme pas automatiquement une distance prédictive en nombre d’apports indépendants.

**HYPOTHÈSE — Appariement incomplet des mondes.** Répartir un gain total constant entre plusieurs effets diminue potentiellement chaque gain individuel. L’expérience peut opposer un signal détectable à plusieurs signaux sous le seuil, plutôt qu’un monde pauvre à un monde riche.

**HYPOTHÈSE — Le maximum sur sondes ne garantit pas la protection des régions rares.** Il ne protège que les régions effectivement sondées. Inversement, un point sans masse sous la distribution cible peut séparer des lois sans conséquence prédictive opérationnelle.

**HYPOTHÈSE — Canonisation à préciser.** Renommer des variables liées purement notationnelles est différent de permuter les coordonnées observées. La canonisation ne doit pas confondre des lois dépendant de traits distincts.

**HYPOTHÈSE — Garantie du sous-ensemble et multiplicité.** Choisir les représentants avant les données est approprié pour éviter une sélection sur le juge, mais la procédure statistique modifiée doit être spécifiée. Les effets du regroupement et ceux d’un changement du nombre de tests doivent être évalués séparément.

**HYPOTHÈSE — Attribution limitée du paquet E2.** Son contraste peut évaluer un paquet complet ; il ne permet pas d’attribuer le résultat aux rôles, aux consignes ou à la présentation de l’archive. D prévoit des ablations ultérieures : elles restent nécessaires avant toute conclusion mécaniste.

### (b) Conditions probabilistes de perte de puissance ou de non-jugabilité

**HYPOTHÈSE — Utilité non indépendante.** Considérons \(q_i=q_\star+\epsilon v_i\), toutes admissibles, telles que
\[
G_{\mathcal N}(q_i)>\delta,\qquad d(q_i,q_j)>\tau,
\]
mais
\[
L_p(q_i)-L_p(q_\star)\leq0.
\]
Le comptage utile peut croître sans amélioration supplémentaire au-delà de \(q_\star\). Sa valeur dépend alors du seuil de séparation et de la faiblesse de \(\mathcal N\).

**HYPOTHÈSE — Moyenne et maximum empiriques.** Si les sondes évitent \(B\), les deux distances estimées sont nulles pour des lois égales hors de \(B\). Si \(P(B)=0\) mais qu’une sonde appartient à \(B\), le maximum peut être positif alors que les lois sont égales \(P\)-presque sûrement.

**HYPOTHÈSE — Répartition du gain.** À gain total \(\Delta\) fixé, les gains individuels \(\Delta_j\) peuvent satisfaire \(n\Delta_j<h\) pour chaque \(j\), alors que \(n\Delta>h\). L’appariement du gain total ne suffit donc pas à apparier les probabilités de détection.

**HYPOTHÈSE — Estimation oracle.** Si \(L_p(q)\) est estimé par simulation, les classifications proches de \(\delta\) sont instables lorsque l’erreur Monte-Carlo est comparable à \(|G_{\mathcal N}(q)-\delta|\). Une bibliothèque sélectionnée sur les mêmes simulations ajoute un biais de sélection.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles requis :**

- Lots de variantes distantes portant le même gain contre une bibliothèque faible.
- Réévaluation après ajout de \(q_\star\) à la bibliothèque, pour détecter les comptes sans apport incrémental.
- Différences concentrées hors sondes, et différences uniquement sur des ensembles de probabilité nulle.
- Mondes appariés sur les **puissances individuelles**, pas seulement sur le gain total.
- Permutations de coordonnées avec puis sans permutation correspondante de leur distribution.
- Simulations indépendantes pour construire la bibliothèque et estimer \(D_u\).

Le duel décisif pour \(D_u\) est : \(H_A\), son inflation sur les lots sans apport incrémental reste sous une tolérance ; \(H_B\), elle la dépasse. Sans ce contrôle, « utile » ne signifie toujours pas « distinct ».

FIN-DE-CELLULE