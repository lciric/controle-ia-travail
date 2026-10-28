# Fiche — Kramár, Engels, Wang, Chughtai, Shah, Nanda et Conmy, *Building Production-Ready Probes For Gemini* (Google DeepMind ; arXiv 2601.11516v4, 10 février 2026) — v1

- **Source déjà tenue par le programme** : `pdf-main/2601.11516v4.pdf`, SHA-256
  `c4a36db54c9d679a718a0e35b9cad09fa628d81f6174bb6e1d8c6b26a063d8bf` (contrôlée le 2026-10-26 à 11:25 UTC, conforme à
  `provenance-niveau2-lot2-v1.md`) ; non retéléchargée.
- **Pages lues** : 1–2, 31 (extraits).
- **Chez session-depot** : **non** (citée seulement comme « le programme cite 2601.11516 » en D3).

## Ce que la source établit sur des modes d'échec

1. **Les sondes sont fragiles au décalage de distribution de production** : des sondes entraînées sur des contextes
   courts ne généralisent pas aux entrées longues ; entraîner directement sur des contextes longs multiplie le coût
   d'entraînement par plus d'un ordre de grandeur pour un résultat semblable (p. 2).
2. **La généralisation large exige architecture et diversité des données** : les nouvelles architectures règlent la
   longueur de contexte, mais il faut aussi entraîner sur des distributions variées (conversations à plusieurs tours,
   contextes longs, équipe rouge adaptative) (p. 1).
3. **Politique aléatoire et attaque au meilleur de n** : une politique de décision randomisée peut être indésirable en
   sécurité, car un attaquant peut répéter ses requêtes jusqu'à obtenir une réponse favorable ; les auteurs gardent des
   politiques déterministes (annexe, p. 31).

## Conditions

- Mésusage cyber-offensif ; sondes sur Gemini 2.5 Flash ; entrées de l'utilisateur (pas des actions d'agent).

## Ce qu'elle ne dit pas

- Rien sur la tromperie ou le sabotage d'un agent ; rien sur l'agrégation séquentielle.

## Ce que ça touche chez nous (avis)

- Sondes de l'environnement (a) : des épisodes longs et multi-tours sont exactement le décalage qui casse les sondes
  entraînées sur des textes courts (recettes publiées, section 7) ; la porte G0 doit mesurer les sondes sur la
  longueur réelle des épisodes.
- Invariant « seuils stochastiques » (section 9) : un audit randomisé est une surface d'attaque au meilleur de n si
  l'agent peut retenter ; à rapprocher de S6 chez session-depot.

## Phrase citée

« Overall, probes are indeed a cost-effective misuse mitigation, but there is a key problem: they are also fragile to
distribution shifts. » (p. 2)
