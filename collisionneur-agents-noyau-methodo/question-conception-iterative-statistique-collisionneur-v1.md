# Question de l'arbitre pour le collisionneur v2.5, étage III — une phase de conception itérative d'un système d'optimisation à base de modèles de langue : plan d'expérience, réutilisation adaptative d'un jeu d'évaluation, bruit entre graines, outils à plusieurs pas (v1)

Demande de Lazar du 26 octobre 2026 (vers 02:13, heure de Paris) : question distincte, posée sous la règle R-468. Une
seule tentative ; un refus est consigné tel quel. La réponse est du matériau pour une décision de Lazar, jamais une
consigne. Texte figé au départ.

## Le cadre

- Un **système d'optimisation** $\mathcal{O}$ : du code réécrit d'une itération à l'autre par des modèles de langue, qui
  classe des textes en deux familles de classification binaire et tourne dans un environnement isolé ; un hôte fixe lui
  sert les textes, appelle pour lui des modèles de langue (appels simples : une consigne, une réponse), borne temps, coût
  et recherches, et note ses réponses. Une **exécution** : jusqu'à 6 rondes de conception, puis 4 itérations notées ;
  $\mathcal{O}$ reçoit à chaque itération son score sur un jeu $D_{\mathrm{val}}$ ; un jeu $D_{\mathrm{final}}$ ne lui
  est jamais rendu.
- **Jeux** : 60 items par part (36 et 24 par famille) pour la conception ; un jeu neuf plus grand (≥ 96 items par part,
  une famille tenue à l'écart de la conception) est prévu pour la **confirmation**.
- **Règle de phase** : pendant la conception par essais-erreurs, les plans ne sont pas scellés d'avance, mais chaque
  texte est relu par un relecteur indépendant ; les scores de conception sont lus dès la fin d'une exécution ; les
  expériences de **confirmation** se font sur le jeu neuf, sous plan scellé, et déclarent que leurs auteurs ont lu les
  scores de conception.
- **Bruit** : à une exécution par variante, l'erreur type d'une exactitude vers 0,75 sur 36 items est
  $\sqrt{0{,}75 \cdot 0{,}25/36} \approx 0{,}07$ (≈ 0,09 sur 24) ; un écart de moins de 0,2 entre deux exécutions
  uniques reste dans le bruit, sans compter la variance entre graines, inconnue.
- **Quatre manières d'organiser les essais**, à comparer : (1) donner à $\mathcal{O}$, par l'hôte, des **agents à
  plusieurs pas avec outils** (exécution de code, recherche) au lieu d'appels simples ; (2) un **essai réel court et
  payant** avant chaque exécution, en plus des essais en simulation ; (3) des **relecteurs indépendants refont et
  éprouvent** les essais de l'hôte, sans dépense ; (4) **exécuter, lire, corriger, relancer**.

## Ce qui est demandé

Réponse argumentée, objets mathématiques nommés, hypothèses dites :

1. **Chacune des quatre manières** : ce qu'elle apporte à la question de fond (une complexité ajoutée à $\mathcal{O}$
   apporte-t-elle un gain au-delà du bruit ?), son coût, ses risques, l'ordre, les combinaisons, ce qui manque.
2. **Une conception itérative qui reste de la science** : journal de tous les essais (échecs compris), règle d'arrêt, un
   facteur à la fois ou plan factoriel, **analyse adaptative des données** (réutiliser les mêmes 60 items surapprend la
   conception : jeu réutilisable de type Thresholdout, budget de lectures, arrondi des scores, réserve intouchée), nombre
   d'itérations avant la confirmation, séparation exploration / confirmation et borne de la contamination de la
   confirmation par ce que ses auteurs ont lu.
3. **Séparer du bruit pendant la conception** : ce qu'une exécution par variante permet de conclure ou non ; répétitions
   minimales (graines, exécutions identiques), modèle de variance à deux niveaux (graines × items), intervalles appariés,
   références d'un classifieur trivial ; ce qui reste invisible sans répétition.
4. **Des agents à plusieurs pas servis par l'hôte** : ce qu'ils pourraient être (outils, bornes, journaux), leurs
   risques méthodologiques (canal d'information vers $D_{\mathrm{final}}$, coût non borné, non-reproductibilité), le dessin
   minimal et les essais de l'hôte qui doivent le précéder.
5. **Références** citables (titre, auteurs, année, « à vérifier ») : analyse exploratoire puis confirmatoire,
   réutilisation adaptative d'un jeu de test, bacs à sable pour agents outillés, variance entre graines ; aucune de
   mémoire incertaine.
6. **Comment départager** les voies, et ce qu'il faudrait savoir de plus.

Contraintes : réponse en français ; tout chiffre sans raisonnement explicite est « illustratif » ; plusieurs voies et ce
qui les départage, aucune présentée comme « la » réponse.
