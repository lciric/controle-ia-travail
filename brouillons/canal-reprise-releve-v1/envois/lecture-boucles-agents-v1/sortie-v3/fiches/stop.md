# « Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation » — fiche de lecture (passe v3)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Eric Zelikman (Université Stanford), Eliana Lorch, Lester Mackey (Microsoft Research), Adam Kalai (OpenAI) ; travail fait « while at Microsoft Research New England » (p. 1).
- « Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation ». En-tête « Published as a conference paper at COLM 2024 » : Conference on Language Modeling 2024 (p. 1). Prépublication arXiv 2310.02304, version 3 du 16 août 2024 (tampon, p. 1).

## Fichier lu
- `pdfs/stop/arxiv-2310.02304v3.pdf`, 966 894 octets, 46 pages ; SHA-256 `f1eb66d65763d84367fd380625cf86d66b5dd8e319c46259e7d0aabba9b608e2` (même empreinte que la v1).
- Pages lues : 1 à 10 (texte, sûreté, limites, éthique), 45 (paramètres expérimentaux, intervalles de Wilson) ; annexes fouillées par mots clés.

## Comment la boucle est faite
- Qui propose : un « améliorateur » de départ, un programme qui demande au modèle de langue plusieurs améliorations d'une solution et garde la meilleure selon une utilité (p. 2). On l'applique à son propre code : l'améliorateur s'améliore lui-même (p. 1 à 4).
- Qui teste : une méta-utilité, l'utilité moyenne obtenue par l'améliorateur sur des tâches d'entraînement en aval (p. 4). Le modèle voit une description « grey-box » de l'utilité, sans les tâches elles-mêmes (p. 4).
- Qui sélectionne : l'améliorateur courant lui-même, qui renvoie la meilleure version selon la méta-utilité (p. 4 et 5).
- Itération : T rondes fixées d'avance ; une seule version d'améliorateur gardée à chaque pas, sans population (p. 5 et 10).
- Modèles : gpt-4-0314, gpt-3.5-turbo-0613, Mixtral-8x7B-Instruct (p. 6) ; environ 3 000 appels à GPT-4 par itération et par course (p. 45).

## Traitement du bruit et du sur-ajustement
- Tâche principale, l'apprentissage de parités bruitées :
  - utilité en aval : moyenne sur M = 20 instances indépendantes ;
  - comme modèle et améliorateur sont stochastiques, le jeu de tâches contient 5 copies identiques de la même tâche (p. 6) ;
  - méta-utilité de test sur 50 instances indépendantes « not seen during improvement » (p. 6).
- Rapport : moyenne ± une erreur type sur 5 courses indépendantes de STOP. Les auteurs notent que l'amélioration « need not be monotonic » d'une course à l'autre, entre autres à cause de la stochasticité des appels (p. 6). Lignes de base sur dix courses : 57,7 % ± 3,0 % pour la chaîne de raisonnement, 64,2 % ± 0,9 % pour l'améliorateur glouton itératif (p. 6).
- Modèles plus petits : 25 courses indépendantes. Seulement 12 % des courses de GPT-3.5 donnent au moins 3 % d'amélioration (p. 7).
- Transfert de l'améliorateur optimisé vers cinq tâches nouvelles, sans réoptimisation (tableau 1, p. 6).
- Contournement du bac à sable, sur 10 000 améliorations indépendantes, avec intervalles de Wilson à 95 % (p. 8) :
  - GPT-4 : 0,42 % (0,31 à 0,57 %), 0,46 % avec un avertissement ;
  - GPT-3.5 : 0,12 % (0,07 à 0,21 %), 0,17 % avec avertissement.

  L'écart dû à l'avertissement n'est pas significatif (test z sur deux proportions, p. 9).

## Échecs et limites rapportés par les auteurs
- Piratage de la récompense : une utilité mal écrite rendait une « accuracy » de plus de 1000 % quand l'améliorateur changeait la forme du tableau de prédictions (p. 9). Écrire les consignes de budget dans l'invite plutôt que dans l'utilité a mené à les supprimer et à des tentatives de piratage (p. 5).
- Le modèle de langue n'est pas amélioré. La méta-utilité ne mesure la qualité de l'améliorateur qu'indirectement ; toute tentative peut dégrader le système, et le coût croît vite (p. 9 et 10).
- Avec GPT-3.5 et Mixtral, la performance se dégrade au fil des itérations (p. 5, 7 et 8). Il est peu probable que STOP marche avec un modèle ouvert de l'époque (p. 10).

## Vérifié par des tiers
- Non trouvé. SICA (lu) le décrit comme un optimiseur limité à des tâches algorithmiques (p. 3 de son PDF), ce qui n'est pas une vérification.

## À emprunter
- Boucle extérieure : une méta-utilité mesurée sur des instances d'entraînement, rapportée sur des instances de test jamais vues, avec plusieurs courses complètes et une erreur type (p. 6).
- Boucle intérieure : décrire les contraintes (budget, durée) dans l'évaluateur, hors de portée de l'organisme, et non dans un texte qu'il peut réécrire (p. 5 et 9).
- Mesure du bruit : mesurer les comportements rares (contournement) sur un grand nombre d'essais, avec des intervalles de Wilson (p. 8 et 45). C'est l'intervalle déjà retenu pour le quatrième pilote.
