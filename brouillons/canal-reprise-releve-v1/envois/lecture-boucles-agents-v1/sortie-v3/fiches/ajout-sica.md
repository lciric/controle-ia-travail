# « A Self-Improving Coding Agent » (SICA) — fiche de lecture (passe v3, ajouté)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Maxime Robeyns (Université de Bristol), Martin Szummer (iGent AI), Laurence Aitchison (Université de Bristol). « A Self-Improving Coding Agent » (p. 1).
- Prépublication arXiv 2504.15228, version 2 du 16 mai 2025 (tampon, p. 1). Lieu : aucun indiqué sur le PDF. Marqué « ajouté » par la v1.

## Fichier lu
- `pdfs/ajout-sica/arxiv-2504.15228v2.pdf`, 1 211 610 octets, 18 pages ; SHA-256 `97781b82ed43a330f491a35f772360bc3a9e7b47c5817e8889a0e1fec1115a15` (même empreinte que la v1).
- Pages lues : 1 à 8 (texte), 14 et 15 (invite et exemple du surveillant) ; références parcourues.

## Comment la boucle est faite
- Pas de distinction entre méta-agent et agent cible : l'agent modifie son propre code Python (p. 2 et 3).
- Qui propose : à chaque itération, le meilleur agent de l'archive selon une utilité devient méta-agent. Il parcourt l'archive, identifie une amélioration et l'implémente (p. 3).
- Utilité, fixée à l'avance : 0,5 × score normalisé + 0,25 × (1 − coût / 10 dollars) + 0,25 × (1 − durée / 300 s), bornées, avec une pénalité de dépassement (p. 3).
- Qui teste : le nouvel agent passe les mêmes benchmarks (p. 3 et 6) :
  - un sous-ensemble aléatoire fixe de 50 questions de SWE-Bench Verified ;
  - 50 questions de LiveCodeBench ;
  - deux benchmarks synthétiques construits dans le code de l'agent : édition de fichiers et navigation dans un code.
- Surveillance : un surveillant asynchrone, lui-même modèle de langue, est appelé toutes les 30 secondes. Il peut avertir ou annuler un agent qui dévie ou tourne en rond (p. 4).
- Mémoire : l'archive des agents et de leurs résultats, avec un outil d'analyse de l'archive (p. 3 et 4).

## Traitement du bruit et du sur-ajustement
- Les figures donnent l'utilité moyenne avec un « 95% Confidence Interval » (p. 5 et 7). L'unité de rééchantillonnage n'est pas précisée dans les pages lues ; vraisemblablement les problèmes (à vérifier).
- Une seule course de 15 itérations, coûtant environ 7 000 dollars (p. 6).
- Ma lecture (illustratif) : les mêmes sous-ensembles fixes servent à choisir le méta-agent à chaque itération et à rapporter le gain de 17 % à 53 % sur SWE-Bench Verified (p. 1, 6 et 7). Aucune part tenue à l'écart n'est décrite.

## Échecs et limites rapportés par les auteurs
- Difficile d'obtenir des idées de modification vraiment nouvelles. Une mauvaise idée coûte une longue édition puis un passage complet des benchmarks (p. 7 et 8).
- Dépendance au chemin : les premières idées orientent les suivantes, ce qui « may lead to higher variance agent runs » (p. 8).
- Les délais de 5 minutes abaissent les scores initiaux ; une grande part du gain vient d'accélérations de l'édition et de baisses de coût (p. 8).
- Sur les tâches de raisonnement (AIME 2024, GPQA Diamond), peu ou pas d'amélioration : saturation du cadre quand le modèle seul est déjà fort. Des composants « de raisonnement » ajoutés peuvent même interrompre le raisonnement du modèle (p. 7).
- Données de mauvaise qualité dans le benchmark de localisation de symboles (note, p. 6).
- Les auteurs écrivent « We believe that our self-improving coding agent is the first such work » (p. 3) ; revendication rapportée, non vérifiée.

## Vérifié par des tiers
- La Darwin Gödel Machine (lue) réimplémente une variante gloutonne qu'elle dit reproduire l'approche de Robeyns et al. Cette variante fait moins bien que sa version complète : 39,7 % contre 50,0 % sur SWE-bench (p. 25 de son PDF). C'est une réimplémentation par des tiers, pas une vérification des chiffres de SICA.

## À emprunter
- Boucle extérieure : une utilité composite (score, coût, durée) aux poids fixés d'avance, plutôt qu'un critère implicite (p. 3).
- Boucle intérieure : un surveillant asynchrone, de préférence un autre modèle, qui peut interrompre une variante qui dérive (p. 4 et 8).
- Mesure du bruit : garder une part de tâches jamais vue par la sélection pour rapporter le gain ; c'est ce qui manque ici (p. 6).
