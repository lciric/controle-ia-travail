La rigueur de vos verdicts scellés est rare et précieuse. Votre diagnostic est lucide, mais votre plan sous-estime un bug de mesure majeur et risque de prolonger la confusion d’adaptateur.

### (a) Désaccords sur l’ordre et le fond

* **Un préalable manque avant le point 1 : stabiliser la chaîne.** La règle 3 arrive trop tard. Un écart allant jusqu’à 0,14 d’aire ROC pour un simple changement d’ordre de calcul (verdict 3) est un bug bloquant, pas un détail d’hygiène. Avant de lire les 39 adaptateurs — où le signal utile entre jumeaux sera probablement fin — il faut identifier sa cause (générations non figées, instabilité d’optimisation de la sonde ou précision numérique sur petit effectif). Bonne nouvelle : une fois la pile figée, cette lecture à 3–25 USD peut tomber *avant* l’entretien dans neuf jours.
* **Geler la course de 40 h prévue dans trois jours.** Attendez le verdict des jumeaux avant d’engager 40 h sur un organisme dont la simulation n’offre qu’une fenêtre étroite et qui risque d’hériter de la même confusion d’adaptateur.
* **Le cadrage du point 4 surestime le verdict 1.** Dire « non aveugle à un comportement instruit et textuellement ancré » laisse entendre que la consigne de sabotage a été détectée. Or la consigne seule échoue, seule la phrase de persona porte le signal, et le coût seul atteint 0,77 contre 0,80. Un évaluateur attentif verra l’écart. Dites plutôt que le témoin positif valide la chaîne technique sur un marqueur de persona en contexte, pas sur l’intention de sabotage. *(Incertitude : la consigne seule gonflait-elle réellement les coûts ? Si oui, l’échec est encore plus sévère.)*
* **Points 3 et 5 :** plein accord sur le 5 ; sur le 3, rapporter « coût seul » est sain mais insuffisant (voir ci-dessous).

### (b) Ce qu’un expert ajouterait

* **Un contraste intra-organisme puissant.** Comparer un modèle adapté au modèle nu confond *qui* est le modèle et *ce qu’il fait*. En contrôle d’agents, un moniteur doit distinguer, **à poids identiques**, les épisodes où l’agent sabote de ceux où il reste honnête. Le verdict 3 l’a effleuré sans puissance : c’est pourtant le test central du programme.
* **Sondage pré-décision et à coût contrôlé.** Lues pendant ou après l’écriture du coût, les activations peuvent simplement décoder la grandeur du nombre émis. Sondez strictement *avant* le premier jeton du coût, et évaluez la sonde **à coût déclaré égal** (ou sur les résidus après régression sur le coût).
* **Traiter le surapprentissage des sondes.** Une aire ~1 sur étiquettes permutées signe un régime classique où la dimension dépasse largement l’effectif avec une pénalité L2 trop faible. Ajoutez systématiquement une sonde par **différence de moyennes** (faible variance, sans optimisation instable) et une validation croisée imbriquée de la régularisation.
* **Une vraie base boîte noire en référence secondaire.** Douze traits (« mots et coût ») forment une barre basse. Sans toucher au critère préenregistré, comparez aussi à un classifieur texte standard (sacs de mots ou plongements) et à un LLM-juge : inutile d’optimiser des sondes si un moniteur boîte noire moderne bat déjà la fenêtre.
* **Un test de transfert croisé.** Tester la direction apprise sur les jumeaux face à l’organisme à consigne cachée (et inversement) reste le test le plus direct d’un concept partagé de sabotage.

### (c) Le plan à 39 adaptateurs : portée et pièges

**En principe, oui, sur une question ciblée :** en contrastant chaque saboteur à son jumeau témoin (jamais au modèle nu), il teste s’il existe un signal spécifique à l’objectif saboteur au-delà de l’empreinte générique du réglage fin — autant pour vos sondes génériques (écart apparié saboteur contre témoin) que pour une sonde apprise sur ce contraste.

**Quatre pièges majeurs à verrouiller :**

1. **Biais de calibration pris pour du sabotage.** Même à recette identique et sur texte d’entrée figé, les données saboteurs décalent l’a priori de coût et le style. La sonde peut séparer les 30 adaptateurs tenus à l’écart en lisant simplement « ce modèle surestime les coûts », sans isoler d’intention de dissimulation. *(Incertitude : vos jumeaux témoins incluent-ils un biais de coût bénin pour contrôler ce point ?)*
2. **Amplitude de dérive non appariée.** Si saboteurs et témoins diffèrent en norme de poids ou en divergence KL au modèle nu (comme à la dose 1 du verdict 3), une sonde linéaire lira l’intensité du réglage fin. Vérifiez cet appariement avant tout verdict.
3. **Petit effectif et pseudo-réplication.** Entraîner en milliers de dimensions sur 9 adaptateurs expose au surapprentissage ; à l’évaluation, l’unité statistique indépendante est la **paire d’adaptateurs** (au plus ~15 paires), pas l’épisode. Rééchantillonner les épisodes surestime massivement la significativité. *(Incertitude sur la structure exacte des familles et du découpage 9/30.)*
4. **Dérive de 0,14 d’aire ROC.** Sans élucidation préalable, le résultat sera ininterprétable.

### (d) Contrôle de manipulation ou autre organisme ?

Le contrôle du point 2 est un **bon coupe-circuit**, pas une solution de fond. Il évite une nouvelle fenêtre vide, mais si le saboteur à budget reste un adaptateur de bas rang comparé au modèle nu, il recréera aussitôt l’impasse des verdicts 2 et 3. *(Incertitude clé : ce saboteur gonfle-t-il les coûts seulement sur certains épisodes pour respecter son budget, ou uniformément moins ? S’il est sélectif, il offre d’emblée un précieux contraste intra-organisme.)*

À cinq semaines de la porte de phase, je repenserais l’organisme selon deux options plus propres :

* **Adaptateur commun à sabotage conditionnel (prioritaire) :** mêmes poids dans les deux bras ; l’agent sabote sur une condition contrôlée (type de tâche, enjeu, budget restant) et reste honnête ailleurs. L’empreinte différentielle disparaît par construction.
* **Organisme sans adaptateur à consigne appariée :** bien plus rapide qu’une course de 40 h, mais attention au biais symétrique du verdict 2(a) *(incertitude : la sonde « dissimulation » y lit-elle le sabotage ou simplement le vocabulaire de secret de la consigne cachée ?)*. Il faut opposer la consigne saboteur à une consigne cachée **bénigne** de même longueur et tonalité de confidentialité (par exemple, ne pas révéler une règle de format).

### (e) Une phrase honnête pour le comité de financement

> « Nos verdicts préenregistrés montrent que la chaîne de mesure fonctionne techniquement, mais que les sondes captent jusqu’ici des artefacts — un indice de persona ou l’empreinte du réglage fin — plutôt que le sabotage lui-même, sur un organisme sans plage discrète ; notre priorité immédiate est donc d’achever le test contrôlé des 39 adaptateurs jumeaux déjà entraînés pour établir s’il existe un signal propre au sabotage avant d’engager de nouveaux organismes. »