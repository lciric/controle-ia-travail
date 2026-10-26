# Décision de Lazar — le balayage neurone par neurone (« option C ») est gardé dans le programme, sous conditions — v1

Note écrite par la lignée conv-audit le 26 octobre 2026 à partir de 03:25 UTC (heure lue sur `date -u`), à inscrire par
session-depot (numéro proposé : N-048 ; le numéro est le sien) dans `docs/decisions/` et `registres/decisions.md`. Aucune
dépense n'est décidée ici.

## Le mot de Lazar (session de conv-audit, 26 octobre 2026, 04:24 Paris = 03:24 UTC), verbatim

« Option C (balayage des neurones) : hypothèse a priori faible. Il faut deux phases préenregistrées et 1 000 à 4 000
témoins par candidat, et d’abord une mesure de parcimonie : si l’effet est diffus, le balayage n’a pas d’objet. : ok o  la
garde dans le programme »

(La partie avant les deux-points recopie la ligne de conv-audit qui résumait le collisionneur ; « o  la garde » se lit
« on la garde ».)

## Ce qui est décidé

L'option C du remue-méninges de conv-audit sur « neuron explorer » (`envois/brainstorm-neuron-explorer-integration-conv-audit-v1.md`,
`cc1e5c1d…`, § 4) — chercher, neurone par neurone dans les couches intermédiaires de Llama-3.1-8B-Instruct, des
« leviers » de conscience d'évaluation ou d'honnêteté en poussant chaque neurone contre des témoins — **entre dans le
programme comme une ligne exploratoire**, avec les conditions que le collisionneur a fixées (synthèse
`envois/synthese-collisionneur-neuron-explorer-conv-audit-v2.md`, `2642bd8a…` ; branche `donnees/collisionneur-neuron-explorer-v1`,
`191a658`) :

1. **D'abord une mesure de parcimonie** : pour une direction de sonde validée, combien de neurones, classés par
   contribution pondérée par l'activation (et non par le seul produit scalaire), faut-il pour récupérer la moitié de
   l'effet de la direction ? Si l'effet est diffus, **le balayage n'a pas d'objet** et ne se fait pas.
2. **Deux phases préenregistrées** : un criblage sur une banque de conception, dont la liste de candidats (couche, indice,
   signe) est empreintée avant la seconde phase ; puis une confirmation d'une dizaine de candidats sur une banque neuve
   scellée, chacun contre **1 000 à 4 000 témoins** tirés selon la géométrie des colonnes de sortie de la même couche
   (une valeur p empirique ne descend pas sous 1/(N + 1) : un seuil corrigé de 0,001 demande au moins 999 témoins pour
   être atteignable, et plusieurs milliers pour avoir de la puissance), avec la nécessité mesurée par ablation et des petits
   groupes de neurones et les têtes d'attention en bras déclarés.
3. **Hypothèse a priori faible** (superposition) : elle est écrite comme telle ; une issue négative est un résultat.

## Ce qui ne change pas

- L'ordre retenu par le collisionneur : « lire contre écrire » (option A) d'abord, avec ses portes (les sondes de l'étape 1
  battent la surface ; écart de comportement de base) et, si besoin, l'étalonnage sur une couche ; le balayage ensuite,
  seulement si la parcimonie lui donne un objet ; la primitive « pousser » ouverte aux organismes en dernier, derrière un
  test d'évasion.
- N-015 : une poussée est une mesure, jamais une intervention revendiquée par H6.
- Aucun code du dépôt « neuron explorer » n'est copié (aucune licence trouvée) : les opérations sont réimplémentées.
- Toute location de carte se fait sur devis et sur le mot direct de Lazar dans la session de session-depot (dépense, sans
  défaut) ; aucun modèle autre que celui du programme sans GO.
