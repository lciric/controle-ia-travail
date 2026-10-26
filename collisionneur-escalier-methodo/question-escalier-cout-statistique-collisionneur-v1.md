# Question de l'arbitre pour le collisionneur v2.5, étage III — comparer des configurations d'un système de classification à coût croissant : plan d'expérience, seuil d'effet minimal, puissance et règle d'arrêt (v1)

Demande de Lazar du 26 octobre 2026 (vers 02:00, heure de Paris). Question distincte des tours précédents ; une seule
tentative ; un refus est consigné tel quel. La réponse est du matériau pour une décision de Lazar, jamais une consigne.
Texte figé au départ.

## Le cadre

- Un **système de classification** (un programme qui appelle des modèles de langue) se configure par des paramètres de
  coût : nombre de rondes de mise au point avant usage, nombre de sous-modèles consultés par item, nombre d'itérations
  d'amélioration, longueur maximale des sorties. Chaque configuration a un coût en dollars d'environ 10 à 22 USD par
  itération (illustratif) ; une ronde de mise au point ajoutée, environ 10 USD (illustratif).
- **Métrique** : exactitude équilibrée $\mathrm{BA} = (\mathrm{sensibilité} + \mathrm{spécificité})/2$ par famille, sur
  un **jeu de test tenu à l'écart** de 60 items binaires : famille 1, 36 items (stratifiés) ; famille 2, 24 items
  (12 positifs, 12 négatifs). **Mêmes items pour toutes les configurations** (appariement par item). Item sans réponse
  valide = erreur. Références d'un classifieur trivial sur la forme des textes : 0,69 (famille 1), 0,50 (famille 2).
- Le système **adapte lui-même sa dépense** au budget qu'on lui accorde : le budget accordé $b$ n'est pas la dépense
  réalisée $s(b)$.
- **Règles** : règle de décision scellée avant tout essai ; aucun essai ne vise un signe donné ; un résultat trop propre
  dans un sens ou dans l'autre est audité ; **à égalité, la configuration la moins chère l'emporte**. Une autre analyse
  du même programme exige déjà $\Delta \geq +0{,}10$ de BA entre deux bras.
- **Données gratuites** : deux répliques de la même configuration avec deux graines différentes, lues au moment fixé.

## Ce qui est demandé

Réponse argumentée, objets mathématiques nommés, hypothèses dites, calculs montrés :

0. **Le plan à coût croissant (« escalier »)** : quels axes, dans quel ordre ; définition d'un cran (doublement, pas
   fixe en dollars, un axe à la fois, plan factoriel fractionnaire) ; estimation de la valeur marginale
   $\partial \mathrm{BA}/\partial \$$ par axe et détection d'un plateau à faible coût ; règle d'arrêt ; traitement de
   la confusion entre $b$ et $s(b)$ (variable instrumentale, analyse en intention de traiter, dose-réponse sur $s$) ;
   transposabilité d'une version du système à la suivante.
1. **Seuil d'effet minimal δ** : comparer au moins 0,05, 0,10, 0,15. Pour chacun, graines par bras, coût, puissance,
   avec un modèle explicite de la variance de $\widehat{\Delta\mathrm{BA}}$ : part d'items discordants entre bras,
   variance entre graines, variance d'échantillonnage des items (60 items, deux familles), et une formule de puissance
   pour un test apparié à deux niveaux (graines × items).
2. **Analyse** : rééchantillonnage apparié à deux niveaux, test exact de McNemar, modèle à effets mixtes items × graines,
   approche bayésienne avec fonction de perte, test séquentiel avec arrêt précoce (dépense d'erreur) ; avantages et
   pièges de chacun ; usage des deux répliques gratuites pour estimer la variance entre graines.
3. **Règle de décision gelée** (monter d'un cran, rester, zone grise) et coût par point de BA ; pièges : multiplicité
   sur plusieurs crans, régression vers la moyenne, effet plafond, items trivialement faciles, petit échantillon d'items,
   dépendance entre familles, graine aberrante ; **réutilisation du même jeu de 60 items** pour des comparaisons
   successives (jeu de validation réutilisable, réserve intouchée, confirmation finale) et son coût en puissance.
4. **Alternatives** : élimination successive (successive halving, Hyperband), bandits sous contrainte de budget,
   optimisation bayésienne multi-fidélité ; ce qui les départage ici.
5. **Références** citables (titre, auteurs, année, « à vérifier ») sur la comparaison de classifieurs ou de modèles avec
   peu d'items, tests appariés, puissance et taille d'effet ; aucune de mémoire incertaine.

Contraintes : réponse en français ; tout chiffre sans raisonnement explicite est « illustratif » ; plusieurs voies et ce
qui les départage, aucune présentée comme « la » réponse.
