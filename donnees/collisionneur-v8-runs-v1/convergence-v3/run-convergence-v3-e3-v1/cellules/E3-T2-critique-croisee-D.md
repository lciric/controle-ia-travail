Le PDF de Bailey, le pilote JSON complet et les 432 entrées `resultats` ne sont pas servis ; je n’en déduis rien.  

**Point de mesure commun — VÉRIFIÉ dans le code.** Pour une défense \(p\), la valeur calculée \(V\) est le minimum de détections obtenues par deux attaques approchées, sur échantillons finis. Ce n’est pas \(S(p)=\inf_{\theta\in\Theta_\delta}u(p,\theta)\). Si \(\eta_p=|V(p)-S(p)|\) inclut erreur d’optimisation et erreur Monte-Carlo, un contraste estimé \(\Delta\) entre \(p\) et \(p'\) cesse d’être jugeable lorsque
\[
|\Delta|\lesssim \eta_p+\eta_{p'}+\text{incertitude d’échantillonnage du contraste}.
\]
L’appariement peut réduire la variance, mais ne supprime pas ce problème. Toutes les propositions utilisent par endroits \(V\) comme si l’attaque était un oracle certifié.

## Sur la proposition A

**(a) Défauts de méthode.** La déduction centrale — équilibre mixte, donc une suite de moniteurs purs ne peut se stabiliser — exige un jeu figé, des meilleures réponses exactes et une classe de déploiement inchangée. Même sous ces conditions, elle n’implique ni périodicité, ni retours angulaires au-delà du hasard. Le caractère non pur de B est **RAPPORTÉ** pour des poids issus du jeu restreint final ; cela ne démontre pas que tous les équilibres accessibles à la trajectoire de A sont mixtes.

Le Duel 1 ne sépare pas les facteurs causaux. `A_q` change la distribution d’entraînement, `A_moy` change le déploiement et la paramétrisation, `A_pire` change l’objectif ; les moniteurs de B changent encore la trajectoire et la distribution adverse. Le maximum sur \(X\), choisi après observation, ajoute un biais de sélection. Surtout, plafond de classe et mauvaise règle de mise à jour peuvent être vrais simultanément : les deux hypothèses ne sont pas exclusives. Il faudrait un plan factoriel croisant séparément objectif d’entraînement, classe du moniteur, déploiement pur ou mixte et réponse adverse, à budget constant.

Le Duel 2 ne teste pas directement « dynamique contre géométrie ». Permuter huit déplacements teste leur non-échangeabilité dans une réalisation, pas la cause des retours. Le second test sur les poids des moniteurs change d’espace, d’unité et de loi nulle. Retirer le départ déterministe modifie aussi l’attaquant et les données d’entraînement. Dans le Duel 3, comparer A, son mélange déployé et un attaquant jouant contre l’historique confond à nouveau apprentissage et déploiement. Enfin, réduire les unités ou augmenter \(K\) dans le Duel 5 change le jeu ; une pureté moins fréquente n’isole pas l’effet du tirage.

**(b) Conditions de perte de puissance ou de non-jugement.**

- **I1** compare deux moyennes de quatre tours. Il perd sa puissance si la détection sature tôt à un plafond, mais aussi si les oscillations se compensent dans les deux fenêtres : une trajectoire périodique peut produire \(I1\approx0\) sans convergence.
- **I3 contre 0,7345** suppose des déplacements échangeables, avec continuité et gestion des égalités compatible avec la nulle simulée. Sous une loi adaptive \(Q_{\theta_{t+1}\mid w_t}\), cette échangeabilité n’a pas de raison de tenir. Avec un optimiseur produisant quelques modes discrets ou de nombreuses égalités, la nulle gaussienne est invalide dans les deux sens. À huit tours, I3 ne peut pas identifier une orbite périodique longue.
- **NashConv restreint** n’est comparable entre \(T=8\) et \(T=16\) que si le jeu, les classes et la convention de profil moyen sont explicitement conservés. Un petit gap restreint ne certifie pas un petit gap dans le jeu continu.
- Pour le jeu fictif, si la seule borne disponible sur le taux est \(r_T\), un seuil de décision inférieur à \(r_T\) ne peut pas réfuter la convergence asymptotique à horizon fini.

**(c) Contrôles négatifs indispensables.** Sans eux, les duels ne discriminent pas leurs mécanismes :

1. `A̅` construit sur des copies exactes d’un même moniteur, qui doit rester fonctionnellement identique au moniteur unique, et un bras gelé sans réentraînement.
2. Deux lois synthétiques de géométrie connue : mélange réellement séparable par un moniteur pur, et mélange dont l’enveloppe convexe empêche cette séparation, à marginales comparables.
3. Trajectoires entièrement fabriquées : périodique, convergente, i.i.d. unimodale et i.i.d. multimodale, soumises au même I1/I3 ; plus une trajectoire produite par l’optimiseur seul, moniteur gelé.
4. Matrices à selle pure, à équilibre intérieur et à cycle connu, ainsi qu’une matrice à ligne strictement dominante pour le test de pureté.

## Sur la proposition B

**(a) Défauts de méthode.** Dans l’expérience 1, une grille de \(10^4\) ou \(10^5\) points n’est pas un attaquant exhaustif dans \(\Theta_\delta\), continu et de dimension élevée. Elle peut être plus faible que SLSQP sur certains bassins et plus forte sur d’autres. Une disparition d’I3 peut donc provenir d’un changement de loi des déplacements, pas de la suppression d’un artefact du solveur. Les moniteurs ne peuvent pas non plus rester identiques si leurs trajectoires d’entraînement changent.

L’expérience 2 commet une erreur logique : un NashConv supérieur à un seuil à \(T=8\) ne réfute pas une hypothèse de convergence asymptotique sans borne de vitesse. Il faut en outre évaluer les politiques empiriques moyennes, pas le dernier moniteur pur. Le contrôle Matching Pennies valide seulement un cas fini exact.

L’expérience 3 appelle « exploitabilité » l’écart entre valeur du jeu restreint et \(V(B)\). C’est au plus une partie côté attaquant du gap, estimée avec des réponses approchées ; elle peut décroître pendant que l’autre partie augmente. Les jeux restreints à \(T=16,32,64\) ne forment pas nécessairement une échelle de métrique commune.

Dans l’expérience 4, plusieurs \(\lambda\) sont explorés sans contrôle de la sélection, tandis que recalibration et changement d’objectif varient ensemble. Dans l’expérience 5, augmenter \(T\) modifie simultanément horizon, nombre d’attaques et matrice ; les seuils de part pure à \(T=32\) ne séparent pas capacité intrinsèque et effet d’horizon.

**(b) Conditions mesurables.**

- Si l’erreur de meilleure réponse adverse dépasse l’écart de détection entre deux défenses, leur classement par \(V\) est non identifiable. Il faut faire croître le budget d’attaque jusqu’à stabilisation du contraste, sur échantillon frais.
- Pour toute convergence annoncée à \(T\) fini, le critère est impuissant si la borne théorique ou le taux de référence \(r_T\) reste supérieur au seuil retenu.
- Le classement de pureté devient fragile lorsque les gains de la matrice estimée ont une erreur comparable aux seuils \(10^{-6}\) ou \(10^{-9}\). Si une ligne domine les autres avec marge \(\eta\), et que l’erreur maximale sur les gains est inférieure à \(\eta/2\), la pureté est au contraire certifiable. Si \(v_{\rm mix}-v_{\rm pur}\) est inférieur à l’incertitude de la matrice, la non-pureté fonctionnelle est non jugeable.
- Pour la régularisation, si la variation de \(V\) est du même ordre que l’erreur d’attaque ou que l’effet de recalibration, « cycle brisé sans perte » n’est pas tranchable.

**(c) Contrôles négatifs indispensables.** Il faut un cycle artificiel planté dans un jeu sans cycle dynamique et un cycle de jeu persistant sous plusieurs optimiseurs ; un jeu fini où les deux composantes du gap sont calculées exactement ; un témoin à régularisation fictive et budget de calcul identique, en plus de \(\lambda=0\) ; enfin, pour le solveur, matrices à ligne dominante, lignes dupliquées rendant l’équilibre non unique, et équilibre intérieur connu. Le seul contrôle B linéaire non pur ne valide aucune de ces distinctions.

## Sur la proposition C

**(a) Défauts de méthode.** La formalisation distingue correctement le jeu en population du jeu effectivement optimisé, mais les expériences réintroduisent ensuite des preuves par construction. Les écarts **RAPPORTÉS** \(C1-A\) et \(D-A\) ne prouvent pas l’explication géométrique : C1 change le déploiement, D change la classe, et tous deux diffèrent de A par leurs trajectoires et leurs distributions d’entraînement.

L’expérience 1 oppose capacité et myopie sans factorisation. Une bonne performance sur les attaques d’entraînement n’établit pas qu’un moniteur pur minimise la perte de pire cas sur leur mélange ; une variante bilatérale peut également modifier la difficulté de l’attaque et la qualité des données. Il manque le croisement réponse adverse au dernier moniteur ou à l’historique × déploiement pur ou mixte, à oracles et budgets identiques.

L’expérience `C3p_support` ne teste pas proprement « randomisation contre dilution ». Elle change à la fois le support, les poids effectivement utilisés, la calibration et l’agrégation déterministe. Comparer un mélange échantillonné à un « ou » non pondéré sur son seul support ne suffit pas : il faut aussi une agrégation déterministe pondérée, à support et moniteurs identiques.

Enfin, la condition \(m<K T\) ne garantit aucun équilibre non pur. Le nombre d’unités du maxout ne contrôle ni le rang de la matrice de gains ni le support de Nash. Une ligne peut dominer toutes les autres pour \(m=2\) comme pour \(m=9\). L’argument invoquant Carathéodory ou le rang pour imposer un support d’au moins deux moniteurs est donc faux ; la condition C5.1 ne rend pas Q2 posable par construction.

**(b) Conditions de validité statistique.**

- Pour le test de capacité, il faut comparer \(\min_{t\le T}H\) ou le minimum sur une banque tenue à l’écart, pas seulement la moyenne d’entraînement. Si deux classes atteignent la même perte empirique mais diffèrent sous la loi mélange des \(Q_\theta\), le critère proposé n’a pas de pouvoir.
- Pour randomisation contre agrégation, soient \(u_i(\theta)\) les détections des moniteurs du support. Le contraste pertinent oppose \(\inf_\theta\sum_i p_i u_i(\theta)\) à \(\inf_\theta u_{\rm ag}(\theta)\). Si, sous toutes les \(Q_\theta\), les scores sont affinements équivalents ou les événements de détection quasi coïncidents, les deux défenses peuvent être fonctionnellement identiques : l’expérience ne mesure alors aucun effet de randomisation. Si les détections sont disjointes ou fortement dépendantes, l’effet peut au contraire changer de signe ; il faut rapporter ces régimes, pas un signe universel.
- Q2 n’est tranchable que si le jeu de comparaison possède une marge estimable \(v_{\rm mix}-v_{\rm pur}\), ou si l’hypothèse porte explicitement sur l’absence de marge. Si cette différence est inférieure aux erreurs de gains et d’attaque, pureté et avantage du mélange sont non jugeables.
- Le taux de retours conserve les mêmes limites d’échangeabilité, de discrétisation et de courte fenêtre que chez A.

**(c) Contrôles négatifs indispensables.**

1. Couples de lois à géométrie certifiée : mélange séparable par hyperplan et mélange dont l’enveloppe convexe contient l’origine, avec calibration identique ; une seule attaque facile ne suffit pas.
2. Pour `C3p_support` : invariance aux moniteurs dupliqués ou de poids nul, égalité au bit sur les tâches pures, et comparaison à une agrégation déterministe **pondérée** sur le même support.
3. Plan factoriel complet pour attaquant myope/bilatéral et défense pure/mixte, avec même banque d’évaluation tenue à l’écart.
4. Pour Q2 : reproduction au bit à \(m=1\), matrice à ligne dominante et matrice à équilibre intérieur certifié. Sans ces contrôles, une part pure faible prouve seulement que le solveur n’a pas renvoyé de sommet pur, pas que le tirage possède un avantage causal.

## Sur la proposition E

**(a) Défauts de méthode.** La proposition nomme correctement les trois objets — dernier profil, profil moyen et jeu restreint — mais ses expériences ne les maintiennent pas toujours au même niveau. Un gap exact sur un jeu fini ne devient pas un gap du jeu continu par simple changement de vocabulaire.

Dans « plafond de classe ou bibliothèque incomplète », l’absence de gain d’une extension peut signifier que l’extension est faible, mal optimisée ou mal calibrée. Elle ne distingue donc pas plafond de classe et procédure insuffisante. Un gain positif réfute seulement le plafond allégué pour cette batterie.

Le plan causal réutilise une même banque pour choisir pondérations et objectifs, puis ouvrir la boucle : sans banque de développement séparée de la banque finale, l’intervention peut être adaptée à l’évaluation. Les contrôles à coefficient nul ou stratégies dupliquées vérifient l’implémentation, pas l’absence de cette fuite. Enfin, \(v_{\rm mix}>v_{\rm pur}\) établit un avantage possible du mélange **dans la matrice restreinte**, pas l’avantage de la procédure B′ sur D, dont les historiques d’entraînement diffèrent.

**(b) Conditions de non-jugement.** Avec deux réponses approchées, l’écart calculé ne borne le gap global que d’un côté ; un petit gap local ne certifie rien lorsque l’erreur résiduelle d’optimisation est supérieure au seuil. Pour une extension, un gain inférieur à la somme des erreurs d’attaque, de calibration et d’échantillonnage est compatible aussi bien avec l’absence que la présence d’un effet. De même, si l’erreur sur \(G\) dépasse la moitié de \(v_{\rm mix}-v_{\rm pur}\), le critère de posabilité perd sa puissance. Agréger plusieurs tâches reste une autre expérience si la défense ne connaît pas la tâche au moment de fixer ses poids ; la disponibilité effective de cette information doit faire partie de la loi du jeu, pas d’une note interprétative.

**(c) Contrôles négatifs indispensables.** Il faut des jeux à gap global connu, dont un profil convergent à I3 faible et un profil cyclique à gap mesuré ; une extension positive plantée dont le gain est connu, ainsi qu’une extension dupliquée à gain nul ; des interventions fictives à budget égal et une banque finale jamais utilisée pour le réglage ; enfin, pour \(v_{\rm mix}-v_{\rm pur}\), une matrice à selle pure, une matrice intérieure exacte et des stratégies dupliquées. Sans ces contrôles, les critères proposés restent incapables de distinguer absence d’effet, instrument insuffisant et mauvaise estimation de l’attaque.

FIN-DE-CELLULE