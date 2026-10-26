# « Automated Design of Agentic Systems » (ADAS) — fiche de lecture (passe v3)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Shengran Hu, Cong Lu, Jeff Clune. « Automated Design of Agentic Systems ». Université de Colombie-Britannique, Vector Institute, chaire Canada CIFAR (p. 1).
- En-tête « Published as a conference paper at ICLR 2025 » : International Conference on Learning Representations 2025 (p. 1). Prépublication arXiv 2408.08435, version 2 du 2 mars 2025 (tampon, p. 1).

## Fichier lu
- `pdfs/adas/arxiv-2408.08435v2.pdf`, 801 981 octets, 34 pages ; SHA-256 `32eb1c1a6888e35fae0f618e33c58698b54d9c49bc063fef91ee591719fca376` (même empreinte que la v1).
- Pages lues : 1 à 11 (texte, sûreté, travaux futurs), 29 (détails des jeux de données), 34 (coûts) ; autres annexes fouillées par mots clés.

## Comment la boucle est faite
- Algorithme « Meta Agent Search » (p. 4 et 5) :
  - qui propose : un méta-agent fixe (GPT-4, « gpt-4o-2024-05-13 » selon la p. 29) écrit en code la fonction « forward » d'un nouvel agent, conditionné par une archive. L'archive est initialisée avec des agents connus : chaîne de raisonnement, auto-affinage, etc. ;
  - deux étapes d'auto-réflexion vérifient la nouveauté de l'idée ;
  - en cas d'erreur, le méta-agent corrige, jusqu'à cinq fois.
- Qui teste : l'agent est évalué sur une part de validation du domaine cible, puis ajouté à l'archive avec son score (p. 4 et 5). Les agents évalués tournent avec GPT-3.5 pour réduire le coût (p. 6 et 29).
- Qui sélectionne : le méta-agent, qui lit l'archive et ses scores pour proposer l'agent suivant ; il cherche des agents « interestingly new » (p. 4). L'archive conserve tout.
- Itérations : 25 pour ARC, 30 pour les domaines de raisonnement (p. 6).

## Traitement du bruit et du sur-ajustement
- Séparation validation/test :
  - ARC : 20 questions de validation pour la recherche, 60 de test, chacune évaluée cinq fois « to reduce the variance from the stochastic sampling of FMs », les modèles de fondation (p. 6) ;
  - DROP, MGSM, MMLU : 128 questions de validation et 800 de test ;
  - GPQA : 32 et 166, évaluées cinq fois ; les autres domaines, une fois (p. 29).
- Résultats sur la part de test tenue à l'écart, avec intervalles de confiance à 95 % par bootstrap. Sont mises en gras toutes les entrées dont la médiane tombe dans l'intervalle de la meilleure (p. 5 et 7).
- Transferts vers des domaines et des modèles tenus à l'écart, avec intervalles (p. 8 et 9).
- Ma lecture (illustratif) : pour le transfert vers d'autres modèles sur ARC, les trois agents retenus sont « the top 3 agents with the best test accuracy » (p. 8). Le choix se fait donc sur la part de test, qui cesse alors d'être tenue à l'écart pour cette expérience.
- Pas de correction de comparaisons multiples entre les nombreuses lignes de base et domaines.

## Échecs et limites rapportés par les auteurs
- Un seul objectif (la performance) ; coût, latence et robustesse restent à intégrer (p. 10).
- Le meilleur agent sous GPT-3.5 n'est plus le meilleur une fois transféré à des modèles plus forts : le design trouvé dépend du modèle évalué (p. 11).
- Évaluation limitée à des questions-réponses en une étape (p. 11).
- Coût : environ 500 dollars par course sur ARC, environ 300 dollars dans les domaines de raisonnement ; la fonction d'évaluation « naive » est chère et perd de l'information (p. 34).
- Sûreté : exécution en conteneurs, inspection manuelle du code généré (p. 10).

## Vérifié par des tiers
- Non trouvé comme vérification. La Darwin Gödel Machine (lue) reprend l'approche comme ligne de base « sans auto-amélioration » (p. 6 de son PDF) ; SICA (lu) la décrit comme le travail antérieur le plus proche (p. 3 de son PDF).

## À emprunter
- Boucle extérieure : rechercher sur une part de validation et rapporter sur une part de test tenue à l'écart, avec intervalles par bootstrap. Ne jamais choisir ce qu'on transfère sur la part de test (contre-exemple p. 8).
- Boucle intérieure : répéter chaque évaluation stochastique plusieurs fois (cinq ici) avant de comparer (p. 6 et 29).
- Mesure du bruit : la règle de lecture « en gras tout ce qui tombe dans l'intervalle du meilleur » (p. 7) se transpose aux verdicts sur les conceptions d'organismes.
