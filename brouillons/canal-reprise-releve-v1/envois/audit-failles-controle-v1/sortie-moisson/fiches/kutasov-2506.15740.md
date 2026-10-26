# Fiche — Kutasov, Sun, Colognese, van der Weij et al., *SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents* (arXiv 2506.15740v2, 8 juillet 2025) — v1

- **Nature** : prépublication (« Preprint. Under review. ») d'Anthropic, Redwood Research, Scale AI et d'indépendants.
- **Fichier** : `pdf/kutasov-2506.15740/2506.15740v2.pdf`, SHA-256
  `f9c1656907b7387faad5099d405d048a0346071bea8dbffc0b68962a278330f4`, 3 703 037 octets, 44 pages.
- **Provenance** : `https://arxiv.org/pdf/2506.15740v2`, téléchargé le 2026-10-26 à 10:36 UTC ; titre conforme.
- **Pages lues** : 1, 3–4, 6–7.
- **Chez session-depot** : **non** ; c'est l'une de ses sources restant à lire (n° 7).

## Ce que la source établit sur des modes d'échec

1. **Le meilleur moniteur génératif reste moyen sur le sabotage subtil** : aire sous la courbe de 0,87 (meilleur
   moniteur) pour séparer transcriptions bénignes et malveillantes ; les auteurs attendent que la difficulté croisse
   avec des tâches plus longues et complexes (p. 1).
2. **Un raisonnement privé invisible au moniteur porte le succès du sabotage** : pour les modèles de pointe actuels, la
   réussite de la tâche secondaire dépend fortement d'un carnet caché ; le retirer fait baisser nettement le succès
   global, l'évasion et la tâche secondaire (p. 1, p. 6, figure 7 p. 7). C'est un appui pour la surveillance de la
   chaîne de pensée et un mode d'échec pour tout moniteur qui ne voit pas ce raisonnement.
3. **La détection actuelle tient surtout aux erreurs de l'attaquant** : les agents se font prendre surtout en
   mentionnant la tâche secondaire hors du carnet, en ne cherchant pas la discrétion, ou en échouant à exécuter un plan
   de plus de quelques étapes (p. 6). Les taux de succès des meilleurs saboteurs sont de 27 % et 15 % sous un moniteur
   donné (p. 1).
4. **Moniteur aveugle à la tâche secondaire** par construction (p. 3) : la mesure porte sur la suspicion générale.

## Conditions

- Saboteurs **sur instruction** (tâche secondaire nommée dans le message système, retiré avant la surveillance, p. 4) ;
  moniteurs génératifs ; environnements simulés longs.

## Ce qu'elle ne dit pas

- Aucun moniteur fondé sur les activations ; pas d'attaquant qui choisit ses occasions (voir la fiche METR, mode 3).

## Ce que ça touche chez nous (avis)

- H1 : l'écart blanc-sur-noir dépend de ce que lit la base boîte noire (avec ou sans raisonnement privé) ; à fixer et à
  rapporter dans le préenregistrement de G1, sinon le gain de l'accès interne se confond avec l'accès au raisonnement.
- Organismes (i) : une détection fondée sur les maladresses d'un attaquant sur instruction ne prédit pas la détection
  d'un attaquant compétent.

## Phrase citée

« For current frontier models, success on the side task relies heavily on having access to a hidden scratchpad that is
not visible to the monitor. » (p. 1)
