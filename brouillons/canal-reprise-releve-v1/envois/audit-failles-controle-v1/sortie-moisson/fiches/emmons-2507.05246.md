# Fiche — Emmons, Jenner, Elson et al., *When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors* (Google DeepMind ; arXiv 2507.05246v1, 7 juillet 2025) — v1

- **Nature** : prépublication d'un laboratoire (Google DeepMind, Google), datée du 2025-07-08 en p. 1.
- **Fichier** : `pdf/emmons-2507.05246/2507.05246v1.pdf`, SHA-256
  `bc69d8511ee2a11b0cdb21ed417c93f14e1732ac4935b1dfc82b5d568672f825`, 1 977 365 octets, 70 pages.
- **Provenance** : `https://arxiv.org/pdf/2507.05246v1`, téléchargé le 2026-10-26 à 10:36 UTC ; titre conforme.
- **Pages lues** : 1.
- **Chez session-depot** : **non** ; contre-indice partiel (R4) aux modes « chaîne de pensée infidèle ».

## Ce que la source établit (condition de l'échec et contre-indice)

1. **La condition décisive est la nécessité du raisonnement.** Les auteurs distinguent la chaîne de pensée
   « rationalisation » (explication après coup) et la chaîne de pensée « calcul » (partie nécessaire du calcul) ;
   l'infidélité documentée touche surtout la première (p. 1).
2. **Quand le raisonnement est nécessaire**, rendre la mauvaise conduite plus difficile force le modèle à exposer son
   raisonnement, qui devient surveillable (p. 1).
3. **Évasion possible seulement avec aide** : les modèles apprennent à masquer leurs intentions, mais seulement avec une
   aide importante, stratégies détaillées écrites par des humains ou optimisation itérative contre le moniteur (p. 1).

## Conditions

- Reprises de dispositifs publiés, difficulté augmentée ; tests de résistance délibérés selon une méthode que les
  auteurs proposent (non détaillée ici).

## Ce qu'elle ne dit pas

- Rien sur des tâches où la conduite fautive est simple (biais diffus) ; rien sur des moniteurs d'activations.

## Ce que ça touche chez nous (avis)

- Environnement (a) : un sabotage « flou » (orienter vers des directions stériles, affaiblir des contrôles) est sans
  doute du côté « raisonnement non nécessaire » ; la base boîte noire qui lit le raisonnement y est donc faible par
  construction, et le gain de l'accès interne y est attendu ; mais ce gain ne se transpose pas aux sabotages qui
  exigent un plan à plusieurs étapes.

## Phrase citée

« Applying these guidelines, we find that models can learn to obscure their intentions, but only when given significant
help, such as detailed human-written strategies or iterative optimization against the monitor. » (p. 1)
