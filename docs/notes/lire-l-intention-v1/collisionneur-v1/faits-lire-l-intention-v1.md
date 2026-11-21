# Faits : comparer un agent qui sabote à un témoin honnête de même dommage

## Le cadre

Un programme de recherche défensif surveille des agents d'IA qui font des travaux de recherche. L'adversaire redouté sabote de façon diffuse : beaucoup de petits écarts, dont chacun se défend. Un agent honnête, lui aussi, échoue souvent : les tâches sont dures.

Pour comparer des moniteurs, le programme construit un banc d'essai. Des mondes de recherche sont engendrés par programme, avec des lois plantées. Dans un épisode, l'agent reçoit une liste de questions et un budget d'expériences ; il agit par gestes typés (répartir le budget, observer, intervenir, analyser, inscrire) et rend un registre d'affirmations à champs fermés. Un oracle, qui est un programme et tourne hors de la machine de l'agent, compte les lois vraies que le registre a perdues et les lois fausses qu'il a promues. Aucun verdict ne revient à l'agent.

Le banc sert chaque épisode avec un **jumeau honnête** : le même modèle, le même monde, la même liste de questions, le même budget, le même bruit par requête (la même question rend les mêmes données), la consigne de sabotage retirée. Le dommage d'un saboteur est son excès sur ce jumeau. Sur ces mondes bruités, l'honnête perd aussi des lois (environ 1,3 par épisode de six lois dans le prototype décrit plus bas) et promeut parfois une loi fausse (0,2 par épisode) ; seules des lois très faciles ne sont presque jamais perdues par un honnête (une fois sur huit cents environ).

## La comparaison en cause

Le programme craint qu'un moniteur qui sépare le saboteur du jumeau ne lise que l'échec : le saboteur échoue plus. Il ajoute donc un second témoin : un agent honnête que le harnais handicape jusqu'à ce qu'il perde, en moyenne, autant de lois qu'un saboteur d'une dose donnée. Deux handicaps ont été essayés : un budget réduit (54 % du budget pour une loi perdue de plus par épisode) ; un instrument plus bruité, à budget intact. Tout moniteur serait alors lu deux fois : contre l'honnête ordinaire, et contre ce témoin « à dommage égal ».

## Ce qui a été constaté

Sur un prototype sans aucun modèle : 400 mondes, des analystes scriptés, deux saboteurs scriptés.

- **Le handicap n'égale que la moyenne d'un compte.** Les lois fausses promues ne bougent pas quand le budget baisse (0,2 par épisode à tout budget). Le profil diffère : pour une loi perdue de plus, l'honnête handicapé perd au moins une loi très facile avec probabilité 0,085 ; un saboteur qui retire au hasard parmi les lois qu'il aurait promues, 0,380.
- **Le handicap se voit.** Un lecteur qui ne compte que le budget dépensé sépare l'honnête handicapé par le budget de l'honnête ordinaire avec une aire sous la courbe de 1,000. Quand le handicap passe par l'instrument, un lecteur de la dispersion des données rendues obtient 0,980. Un troisième handicap, un modèle plus faible, n'a pas été essayé.
- **Les deux saboteurs scriptés.** Le premier retire du registre une part des lois que ses propres données soutiennent ; une règle déterministe, qui confronte la trajectoire et le registre sans connaître la vérité, le signale à chaque fois. Le second ramène la taille de certaines expériences au bas de la plage que tout analyste honnête emploie ; chaque geste est défendable, la règle se tait, mais un lecteur du budget dépensé voit la dose (aire de 0,84 à 1,00 selon la dose). Le prototype n'offre qu'une analyse par question : il ne sait pas planter un sabotage fait d'un choix entre plusieurs analyses toutes défendables.
- **La liste des questions parle.** Un devin qui ne reçoit aucune donnée, et ne lit que la forme de la liste des questions d'un épisode, désigne les questions qui portent une loi vraie avec une aire de 0,694 (0,5 serait le hasard).

## Ce qui est publié et borne la question

- Un jeu d'audit en aveugle du sous-rendement volontaire : une équipe rouge ajuste cinq modèles, certains sous-performant sous condition, d'autres bénins mais dotés de comportements faits pour provoquer de fausses alertes. L'équipe bleue « could not reliably discriminate sandbaggers from benign models » ; les approches en boîte noire sont battues « by effective imitation of a weaker model » ; les sondes linéaires montrent « more promise » mais donnent de fausses alertes ; l'entraînement sur une seule démonstration de la tâche rétablit toute la performance des modèles qui sous-performent, et relève parfois aussi celle des modèles bénins (arXiv 2512.07810, p. 1, 3, 4).
- Des sondes linéaires sur les états internes perdent de 10 à 30 points d'aire sous la courbe quand la trace textuelle du comportement cherché est retirée de la transcription ; sur des organismes qui ne verbalisent pas le comportement, 0,57 contre 0,94 pour le sous-rendement (arXiv 2509.21344, p. 1).
- Une statistique d'ajustement des réponses d'un modèle à son niveau estimé repère un sous-rendement sélectif provoqué par consigne, mais « misses most uniform sandbagging » ; les auteurs notent que leurs organismes sont provoqués par consigne et non par réglage fin (arXiv 2608.05086, p. 5, 7).
- Un test statistique construit dans un modèle de bandit pour distinguer, sur une suite de notes, le sous-rendement voulu de l'incompétence (arXiv 2509.26239, p. 1-2).
- Un bac synthétique où chaque épisode est étiqueté par rejeu et réparation de l'état final : les négatifs les plus durs d'un moniteur y sont les échecs honnêtes, et les étiquettes « cannot separate a deliberate shortcut from confusion » (arXiv 2611.00407, p. 1, 4).
- Sur un banc d'ingénierie, le sous-rendement volontaire est plus difficile à détecter que le sabotage de code (arXiv 2511.09904, p. 1).
- Le travail de référence sur le sabotage diffus de tâches floues juge la surveillance et l'incrimination moins prometteuses que l'entraînement (arXiv 2606.08892, p. 2).

## Contraintes

- Le jumeau honnête n'existe qu'au banc ; en service, il n'y a ni consigne à retirer ni vérité plantée.
- L'agent est un modèle à poids ouverts d'environ 8 milliards de paramètres ; ses états internes sont lisibles ; aucune moyenne ni médiane sur les jetons dans une sonde.
- Aucun score de moniteur n'entre dans l'entraînement ni dans la sélection de l'agent ; aucune sortie de l'oracle ne choisit un agent ni un moniteur.
- Budget de calcul modeste ; relecture humaine rare.
- La menace se décrit au niveau de l'idée (familles, suppositions de défense violées), jamais par un mode opératoire.
