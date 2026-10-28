# « AlphaEvolve: A coding agent for scientific and algorithmic discovery » — fiche de lecture (passe v3)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii (contribution égale), Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, Matej Balog (contribution égale). « AlphaEvolve: A coding agent for scientific and algorithmic discovery ». Google DeepMind (p. 1).
- Livre blanc (« In this white paper », p. 1), prépublication arXiv 2506.13131, version 1 du 16 juin 2025 (tampon, p. 1). Pas de lieu avec comité de lecture indiqué.

## Fichier lu
- `pdfs/alphaevolve/arxiv-2506.13131v1.pdf`, 3 525 764 octets, 44 pages ; SHA-256 `f092c8cbd65da89951ee6496374da9a54963f9035758c25ac6e4625f506df9ad` (même empreinte que la v1).
- Pages lues : 1 à 21 (texte, ablations, travaux liés, limites) ; annexes (p. 22 à 44) fouillées par mots clés.

## Comment la boucle est faite
- Ce que fournit l'humain : un programme initial dont les blocs à faire évoluer sont balisés, et une fonction d'évaluation `evaluate` qui rend un ou plusieurs scores à maximiser (p. 4 et 5).
- Qui propose : un ensemble de modèles de langue, Gemini 2.0 Flash pour le débit et Gemini 2.0 Pro pour des suggestions plus rares et meilleures. Ils écrivent des modifications sous forme de différences (p. 7). L'invite combine :
  - un programme parent et des « inspirations » tirés de la base ;
  - le contexte fourni par l'humain ;
  - les résultats d'évaluation rendus ;
  - des méta-invites que le modèle fait lui-même évoluer (p. 5).
- Qui teste : des évaluateurs exécutent `evaluate` (p. 7).
- Qui sélectionne : une base évolutive inspirée de MAP-Elites et des modèles en îles, qui arbitre exploitation et diversité (p. 8). Une « cascade d'évaluation », appelée « hypothesis testing », soumet les candidats à des jeux de tests de difficulté croissante ; un candidat ne passe à l'étape suivante que s'il est prometteur (p. 7). Un modèle de langue peut noter des propriétés difficiles à mesurer (simplicité), comme score ou comme filtre (p. 7 et 8).
- Qui déclenche l'itération suivante : un contrôleur asynchrone optimisé pour le débit (p. 8).
- Mémoire : la base des programmes et de leurs résultats (p. 8).

## Traitement du bruit et du sur-ajustement
- Problèmes mathématiques : évaluation exacte, avec des constructions vérifiables (p. 4 et 5, p. 10 à 13).
- Décomposition de tenseurs : chaque programme est lancé sur plusieurs graines. Le score retient le meilleur rang atteint et la fraction des graines qui l'atteignent (p. 10). Les éléments sont arrondis aux entiers ou demi-entiers pour garantir l'exactitude (p. 10).
- Ordonnancement des centres de données :
  - évolution sur un simulateur nourri d'instantanés historiques ;
  - mesure sur « an unseen test dataset » de charges récentes ;
  - déploiement, puis mesures après déploiement : 0,7 % des ressources de calcul de la flotte récupérées en moyenne (p. 14).
- Noyau de multiplication de matrices : la moitié des formes d'entrée sert à l'entraînement, l'autre moitié à l'évaluation (p. 16). Résultat : 23 % d'accélération moyenne, 1 % de temps d'entraînement de Gemini en moins (p. 16).
- Code de compilateur pour l'attention : chaque modification est vérifiée sur des entrées aléatoires contre la référence. La version finale est confirmée correcte par des experts humains (p. 17).
- Ablations : trois courses indépendantes de graines différentes, avec l'écart type en ombre (p. 18). Chaque composant (évolution, contexte, méta-invites, évolution du fichier entier, gros modèles) y apporte un gain (p. 18).
- Pas de correction de comparaisons multiples ; pas d'intervalle sur les gains d'ingénierie dans les pages lues.

## Échecs et limites rapportés par les auteurs
- Il faut un évaluateur automatique ; les tâches qui demandent une expérimentation manuelle sont hors champ (p. 2 et 21). L'évaluation par un modèle de langue est possible mais « not a setting we have optimized for » (p. 21).
- Certains résultats ont été obtenus en ensemençant le programme initial avec des idées des chercheurs (p. 10).
- Les gains sur sa propre infrastructure sont « moderate », avec des boucles de rétroaction de l'ordre de mois (p. 21).

## Vérifié par des tiers
- Problèmes mathématiques proposés par des mathématiciens extérieurs (Javier Gomez Serrano, Terence Tao), qui ont aussi conseillé leur formulation (p. 13) : ce n'est pas une vérification. La réécriture d'un circuit est validée par les concepteurs de puces ; la même amélioration avait été « independently caught » par les outils de synthèse en aval (p. 16).
- ShinkaEvolve (lu) reprend le problème d'empilement de cercles et revérifie sa propre solution avec le code de vérification exact d'AlphaEvolve (p. 20 de son PDF).
- Correction par un tiers, rapportée par les auteurs (p. 39) : après la première version, Henry Cohn a signalé que son article avec Gonçalves (Inventiones mathematicae, 2019, référence [18], p. 24) obtenait déjà, par une approche voisine plus fine, une meilleure constante (0,3284) que la borne annoncée comme nouvelle (0,3523 → 0,3521, p. 12). En reprenant cette approche, les auteurs passent à 0,3216. Un record annoncé était donc battu depuis 2019 par un travail qu'ils n'avaient pas vu.

## À emprunter
- Boucle extérieure : une cascade d'évaluation à seuils écrits d'avance (tests bon marché d'abord, évaluation complète réservée aux candidats prometteurs) (p. 7).
- Boucle intérieure : faire porter le score sur plusieurs graines (meilleur résultat et fraction des graines qui l'atteignent) plutôt que sur une seule (p. 10).
- Mesure du bruit : séparer les entrées d'évolution et les entrées d'évaluation, puis confirmer après déploiement (p. 14 et 16).
