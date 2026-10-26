# « Agent Laboratory: Using LLM Agents as Research Assistants » — fiche de lecture (passe v3)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum. « Agent Laboratory: Using LLM Agents as Research Assistants ». AMD, Université Johns Hopkins, École polytechnique fédérale de Zurich (p. 1).
- Prépublication arXiv 2501.04227, version 2 du 17 juin 2025, catégorie interaction humain-machine (tampon, p. 1) ; en-tête daté 2025-6-18. Lieu : aucun indiqué sur le PDF.

## Fichier lu
- `pdfs/agent-laboratory/arxiv-2501.04227v2.pdf`, 3 644 380 octets, 84 pages ; SHA-256 `67b9543ae1d8e3ad86a65e2a436ddbd12700d7c8f4a66c5b4c2a6fccc1674d75` (même empreinte que la v1).
- Pages lues : 1 à 20 (texte, évaluations, limites, modes d'échec) ; annexes fouillées par mots clés.

## Comment la boucle est faite
- Qui propose : l'humain fournit l'idée de recherche et des notes. Une chaîne d'agents spécialisés conduit la revue de littérature, l'expérimentation et la rédaction du rapport (p. 1 et 4 à 8). En mode « co-pilote », l'humain donne son avis à chaque étape (p. 1 et 10).
- Qui teste : l'outil « mle-solver » (p. 6 et 7) :
  - il garde une liste des programmes les mieux notés et les modifie par édition de lignes ou remplacement complet ;
  - un programme qui échoue à l'exécution est réparé jusqu'à trois fois, puis abandonné (p. 6) ;
  - un programme qui s'exécute reçoit un score entre 0 et 1 d'un « LLM reward model » (modèle de récompense tenu par un grand modèle de langue), juge interne qui estime l'adéquation au plan de recherche, au vu du plan, du code et de sa sortie (p. 6 et 7).
- Qui sélectionne : ce même juge. Avant chaque commande, un programme est tiré au hasard dans la collection des mieux notés ; chaque pas fait N modifications en parallèle, et la meilleure remplace le programme le moins bien noté de la collection (p. 6 et 7).
- La rédaction passe par un « paper-solver », puis une relecture notée par des relecteurs automatiques de style NeurIPS, la conférence Neural Information Processing Systems (p. 8 à 10).
- Mémoire : la collection des programmes les mieux notés et les réflexions écrites après chaque essai, réussi ou non (p. 7).

## Traitement du bruit et du sur-ajustement
- Le juge interne (« reward model ») n'est validé contre aucune vérité de terrain dans les pages lues.
- Les relecteurs automatiques reprennent le système de The AI Scientist. Le texte cite sa validation sur 500 articles de la conférence International Conference on Learning Representations 2022 : 65 % d'exactitude contre 66 % pour les humains, score F1 de 0,57 contre 0,49 « after calibration » (p. 9).
- Relecteurs automatiques contre relecteurs humains sur les rapports produits : 6,1 sur 10 contre 3,8 en moyenne générale, « automated scores significantly overestimating quality » (p. 2 ; aussi p. 12).
- Sur un sous-ensemble de 10 défis MLE-Bench (p. 18 et 19) :
  - le score interne est remplacé par un score sur une part de développement, 20 % tirés au hasard des données d'entraînement ;
  - le meilleur code est évalué sur le vrai jeu de test de Kaggle.

  Les autres méthodes sont moyennées sur « several runs » en excluant leurs soumissions invalides (p. 19). Nombre de courses de « mle-solver » : non trouvé dans les pages lues.
- Résultats : 4 médailles pour « mle-solver », contre 2 pour OpenHands, 2 pour AIDE et 0 pour MLAB ; au-dessus de la médiane humaine sur 6 défis sur 10 (p. 19). Aucun intervalle ni test trouvé pour ces comparaisons.

## Échecs et limites rapportés par les auteurs
- Auto-évaluation peu fiable (p. 19) : le texte rapporte des scores d'accord plus bas pour les modèles que pour les relecteurs humains (53,3 % contre 56,1 %) et les rattache à Lu et al. (2024b), c'est-à-dire The AI Scientist d'après la même page. Ces deux chiffres ne figurent pas dans le PDF de The AI Scientist lu ici (recherche par mots clés) : source exacte à vérifier.
- Hallucinations de résultats expérimentaux dans certains rapports, surtout avec les modèles les moins bons comme gpt-4o (p. 20).
- Modes d'échec (p. 20) :
  - expériences à 0 % d'exactitude pour toutes les méthodes, que l'agent ne corrige pas ;
  - appels à `exit()` qui arrêtent tout le processus, détectés et retirés à la main ;
  - commandes système lancées sur la machine hôte (`subprocess.run`) ; rien de problématique observé, des garde-fous sont demandés ;
  - boucles sur la commande de résumé pendant la revue de littérature ;
  - jusqu'à 100 essais avant qu'une recherche d'articles rende un résultat, d'où une limite fixée à 5.
- Coût : 2,33 dollars par article avec gpt-4o (p. 3 et 17) ; 84 % de baisse revendiquée face aux méthodes autonomes antérieures (p. 1).

## Vérifié par des tiers
- Non trouvé. « The AI Scientist v2 » (lu) le cite comme travail concurrent (p. 14 de son PDF), sans le vérifier.

## À emprunter
- Boucle extérieure : l'écart de 2,3 points sur 10 entre juge automatique et juges humains (p. 12) rappelle qu'un juge interne doit être calibré contre un juge externe avant de servir de critère.
- Boucle intérieure : remplacer un juge interne par un score mesuré sur une part de développement séparée quand c'est possible (p. 18).
- Mesure du bruit : ne pas comparer des moyennes qui excluent les échecs des autres sans les exclure des siennes (p. 19) ; compter les échecs dans le dénominateur.
