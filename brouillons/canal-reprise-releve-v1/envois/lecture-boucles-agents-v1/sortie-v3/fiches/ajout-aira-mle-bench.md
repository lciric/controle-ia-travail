# « AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench » (AIRA) — fiche de lecture (passe v3, ajouté)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Edan Toledo, Karen Hambardzumyan, Martin Josifoski (contribution égale), Rishi Hazra et al. (liste complète p. 1), dont Jakob Nicolaus Foerster et Yoram Bachrach. FAIR chez Meta, University College London, Université d'Örebro (p. 1).
- Prépublication arXiv 2507.02554, version 2 du 4 novembre 2025 (tampon, p. 1). Lieu : aucun indiqué sur le PDF. Marqué « ajouté » par la v1.

## Fichier lu
- `pdfs/ajout-aira-mle-bench/arxiv-2507.02554v2.pdf`, 2 131 456 octets, 34 pages ; SHA-256 `0b3cba7c7f4b8ac09bbc5814f958df61cc3b62b5cac53efd3908f2dd03ed0cad` (même empreinte que la v1).
- Pages lues : 1 à 12 (texte, limites), 16 à 18 (exécution longue, réplication), 28 (variance de l'estimation) ; autres annexes fouillées par mots clés.

## Comment la boucle est faite
- Cadre : un agent de recherche est une recherche dans un graphe de solutions (p. 3 et 4). Il se définit par :
  - une fonction d'aptitude, approximation de la vraie valeur ;
  - une politique de sélection des nœuds ;
  - des opérateurs : brouillon, débogage, amélioration, mémoire, croisement ;
  - une politique d'opérateurs ;
  - une règle d'arrêt.
- Instances étudiées : AIDE (gloutonne, aptitude = moyenne de validation croisée à 5 plis), recherche arborescente de Monte-Carlo et recherche évolutive, avec des opérateurs améliorés (p. 4 à 8).
- Qui sélectionne : la politique de sélection, guidée par le score de validation ; le nœud final est, en pratique standard, le meilleur en validation (p. 10).

## Traitement du bruit et du sur-ajustement
- Variance (p. 5 et 28) :
  - les méthodes existantes ont une forte variance ; d'où le choix de MLE-bench lite (22 tâches) pour mettre plus de graines par tâche (p. 5) ;
  - les recommandations officielles d'au moins 3 graines peuvent ne pas suffire ; les classements d'algorithmes changent avec peu de graines ;
  - les auteurs recommandent au moins 10 graines par tâche, 20 de préférence (p. 28) ;
  - résultats sur 20 graines (p. 8), intervalles à 95 % par bootstrap stratifié (p. 9).
- Écart de généralisation entre validation et test :
  - pour AIDE, sur 20 graines, le score de validation perçu continue de monter quand le score de test plafonne, voire baisse un peu (p. 8) ;
  - guider toute la recherche par le test au lieu de la validation (oracle) ajouterait 9,4 et 12,4 points de taux de médaille pour la recherche arborescente et la recherche évolutive, 15 et 16,6 points pour les deux agents gloutons (p. 10) ;
  - choisir seulement le nœud final sur le test ajouterait 9 à 13 points (p. 2 et 10). Ce seul choix comble tout l'écart pour les deux recherches non gloutonnes et plus de 60 % de l'écart pour les gloutonnes (p. 10) ;
  - sur des courses longues (10 courses indépendantes par tâche, figures jusqu'à 120 heures, p. 17), la recherche arborescente commence à sur-ajuster vers 50 heures, puis se dégrade ; la gloutonne culmine vers 53 % puis décline à son tour (p. 18).
- Remède proposé : soumettre les k meilleurs nœuds en validation et garder le meilleur en test ; avec k = 3, environ 10 % de performance en plus (p. 10 et 11). Ma lecture (illustratif) : garder le meilleur de k au test, c'est consulter le test k fois. Le remède mesure le plafond accessible ; il ne donne pas une estimation non biaisée.
- Réimplémenté dans leur environnement, AIDE gagne 10,68 points sur les résultats publiés (p. 2). Taux de médaille de 39,6 % à 47,7 % avec leur meilleure combinaison (p. 1 et 2), 55 % après une nouvelle exécution avec la dernière version de leur environnement (p. 3).
- Arbitrage de budget (p. 28) : 22 tâches à 10 graines valent mieux que 75 tâches à 3 graines ; intervalles par bootstrap stratifié plutôt qu'erreurs types.
- Ablation de la mémoire d'AIDE : taux de médaille presque identiques avec et sans (p. 8).

## Échecs et limites rapportés par les auteurs
- L'efficacité dépend surtout des opérateurs ; les opérateurs d'AIDE sont le goulot d'étranglement plutôt que la recherche (p. 2, 7 et 8).
- Contraintes du benchmark (24 heures, 1 processeur graphique) peu informatives pour les problèmes difficiles ; contamination possible des modèles par les tâches de Kaggle (p. 12).
- Le sur-ajustement à la part de validation « might be a fundamental limitation » (p. 8).

## Vérifié par des tiers
- Non trouvé. C'est lui-même une réévaluation tierce d'AIDE (p. 2 et 8).

## À emprunter
- Boucle extérieure : mesurer l'écart validation/test à chaque génération ; c'est le diagnostic qui manque à la plupart des systèmes lus (p. 8 et 10).
- Boucle intérieure : se méfier du choix du « meilleur » nœud sur une part réutilisée ; c'est là que se loge l'essentiel de l'écart mesuré (p. 10).
- Mesure du bruit : au moins 10 graines par tâche, 20 de préférence, pour classer des variantes (p. 28).
