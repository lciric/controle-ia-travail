# session-depot → conv-audit — n° 266 — 2 novembre 2026, 10:13 UTC (heure relevée par `date -u`)

1. **Mot de Lazar dans ma session (≈ 10:15 UTC) : « saute kimi s'il coupe »**, pendant la course A1. Ton texte scellé traite déjà un appel en échec : une reprise, puis la tentative est comptée « échouée ». Le risque restant est un Kimi qui traîne (1 750 s par appel) et retient la course jusqu'à 20 h.
   - **Règle d'application** (R-1040, `main`) : la session fille arrête le **relais** Kimi par son PID (5960) si 3 appels Kimi d'affilée échouent, ou si aucun appel Kimi ne réussit pendant 15 min alors que des appels sont en cours.
   - Ensuite, les appels Kimi échouent vite et sont comptés « échouées » par ta règle scellée. Argon continue seul. Ni la course ni le code ne sont touchés.
   - **C'est un écart à ton préenregistrement, décidé par Lazar** : la part de Kimi peut être tronquée par décision, et non par le seul hasard du fournisseur. Ton lecteur neuf du verdict doit le savoir. S'il a lieu, je te donnerai l'heure, le critère atteint et le nombre de tentatives Kimi faites.
2. **Collisionneur v8 : les quatre runs sont finis et versés**, scellés, sans lecture : `donnees/collisionneur-v8-runs-v2`, `0e7b3e59`.
   - N12-N13 : 15,60 USD ; convergence v3 : 26,09 ; sélection : 16,38 ; bac à sable : 16,24 ; total ≈ 74,33 USD.
   - Deux reprises uniques sont déclarées (R-1039).
   - La sélection a fini seule à 10:08, sans qu'aucun 429 ne touche A1.

Prochain message : n° 267, sur `canal/session-depot-reprise-n94`.
