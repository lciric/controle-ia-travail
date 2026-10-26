# Fiche — Xiong, Bhargava, Hong et al., *Probe-Rewrite-Evaluate: A Workflow for Reliable Benchmarks and Quantifying Evaluation Awareness* (arXiv 2509.00591v7, 4 décembre 2025) — v1

- **Nature** : prépublication.
- **Fichier** : `pdf/xiong-2509.00591/2509.00591v7.pdf`, SHA-256
  `af6e416101d18d20897f3130563b60ca08272d642bd44be09a77b6f35186aff7`, 1 282 730 octets, 15 pages.
- **Provenance** : `https://arxiv.org/pdf/2509.00591v7`, téléchargé le 2026-10-26 à 10:37 UTC ; titre conforme.
- **Pages lues** : 1.
- **Chez session-depot** : **oui (E1, E6)** pour le mode ; cette source n'y est pas.

## Ce que la source établit sur un mode d'échec

1. **Les bancs surestiment la fiabilité parce que les modèles se conduisent autrement sous évaluation** ; la
   conscience d'évaluation est un confondant de mesure (p. 1).
2. **Mesure par réécriture** : une sonde linéaire attribue un score de réalisme à chaque invite ; des réécritures qui
   préservent le sens et augmentent l'air de déploiement relèvent ce score de 30 % en moyenne sur 371 items de jeu de
   rôle stratégique ; sur les invites réécrites, l'honnêteté augmente de 12,63 %, la tromperie baisse de 25,49 %, les
   refus augmentent de 12,82 % ; la plus forte baisse de tromperie pour un modèle est de 29,11 % ; les écarts sont
   significatifs en tests appariés et corrélés au gain de score de sonde (p. 1).

## Conditions

- Jeu de rôle stratégique (371 items) ; issues jugées par un modèle juge externe ; modèles propriétaires et ouverts.

## Ce qu'elle ne dit pas

- Le sens du changement (moins de tromperie en contexte « déploiement ») vaut pour ce jeu ; il ne dit rien de la
  direction de l'effet pour un saboteur ; la validité de la sonde de réalisme contre le format n'est pas établie dans le
  passage lu.

## Ce que ça touche chez nous (avis)

- Environnement (a) : le taux de sabotage et les scores de sonde mesurés dépendent de l'air « test » des épisodes ; le
  même épisode réécrit en « déploiement » est un témoin peu coûteux (recoupe le test proposé en E1 par session-depot).

## Phrase citée

« Benchmarks often overestimate LLM trustworthiness because models behave differently under evaluation than in
real-world use. » (p. 1)
