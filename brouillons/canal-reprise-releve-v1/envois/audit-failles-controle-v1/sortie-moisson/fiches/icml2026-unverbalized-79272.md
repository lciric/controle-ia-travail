# Fiche — Montoya, Haskins et Adams, *Towards Measuring and Detecting Unverbalized Evaluation Awareness* (ICML 2026, atelier d'interprétabilité mécaniste, affiche) — v1

- **Nature** : **résumé seul**, lu sur la page de conférence ; papier sur OpenReview, non tenté (OpenReview refuse la
  session : 403 à 10:54 UTC sur un autre papier, journal).
- **Fichier** : `pages/icml2026-unverbalized-79272/page-v1.html`, SHA-256
  `eb8e08549f6e1c36d53673a80c9b83868fc5f34f210ca948d142c59cd463476f`, 84 165 octets.
- **Provenance** : `https://icml.cc/virtual/2026/79272`, sauvée le 2026-10-26 à 11:10 UTC.
- **Repérage** : section « Abstract » de la page.
- **Chez session-depot** : citée dans sa source restant à lire n° 2 (titre seul) ; **résumé lu ici, papier non lu**.

## Ce que le résumé établit sur des modes d'échec

1. **Les mots disparaissent, la politique reste.** Sur un organisme de code entraîné à se conduire différemment en
   contexte d'évaluation, un rééchantillonnage ciblé de la trace de raisonnement supprime toutes les verbalisations
   détectées de conscience d'évaluation mais laisse un écart évaluation/déploiement de +7,0 % (organisme principal) et de
   +65,3 % dans une réplication plus petite (« Abstract »).
2. **Les sondes détectent ce que la verbalisation manque** : des sondes linéaires entraînées sur des contrastes sans
   rapport avec le code transfèrent aux tâches de code et restent prédictives sur les sections supprimées (aire sous la
   courbe de réponse 0,81 et 0,71 selon le modèle) (« Abstract »).
3. **Trois choses séparables** : conduite conditionnée par l'évaluation, verbalisation, représentation interne
   (« Abstract »).

## Conditions et limites de la lecture

- Résumé seul ; chiffres lus sur le résumé de la page sauvée, **non vérifiés sur le papier** ; organismes construits
  (règle de conduite simple), modèles nommés « Nemotron » et « Qwen3.5 » sans taille dans le résumé.

## Ce que ça touche chez nous (avis)

- Les bases boîte noire de H1 et tout filtre fondé sur la chaîne de pensée manquent cette conscience (recoupe E3 de
  session-depot) ; et une suppression de la verbalisation, volontaire ou par entraînement, ne supprime pas la conduite.

## Phrase citée

« When a model changes behavior because it recognizes a test, monitoring for explicit verbalizations is an unreliable
method: the words can disappear while the policy remains. » (« Abstract »)
