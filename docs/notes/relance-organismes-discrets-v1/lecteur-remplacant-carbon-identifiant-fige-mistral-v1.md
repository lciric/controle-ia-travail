# Identifiant figé de Mistral Large 4 — relevé documentaire — v1

Relevé fait le 2026-11-20 par un agent de lecture web de la session de relance (`session_01QPDgKgkCezLtWTAC6NJ7ok`), pour le choix 3 (b) de Lazar (seul un identifiant figé est admis ; pièce `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-cinq-choix-lecteur-bras-a-2026-11-20-v1.md`, 93cbc6f4c78d00c5b91ca29e5b300bef345cd7aa46c89db2be6bff95a46d5beb). Pages lues par un outil qui résume ; provenance par transcription, non opposable comme un PDF empreinté (R7). Aucune clé, aucun appel d'API, aucune dépense.

## Constat
- **Règle de nommage** (https://docs.mistral.ai/inference/model-lifecycle) : identifiants au format `model-name-major-minor` ; trois formes : `model-name-latest` (dernière version toutes générations), `model-name-major` (dernière version mineure d'une génération), `model-name-major-minor` (« Fixed major and minor version »). Avertissement : « Using an alias may expose you to silent updates in model behavior and pricing. » Tableau du cycle de vie : stade GA, « Silent updates: No ». **Non trouvé** : une phrase qui dise que les poids ne changent jamais.
- **`mistral-large-4-0`** (https://docs.mistral.ai/models/mistral-large-4-0) : étiquette « GA », date affichée « November 5, 2026 », version « v26.10 ». L'identifiant n'apparaît que dans l'adresse de la page (pas de champ « identifiant d'API ») ; un texte « mistral-large-4+2 » figure sur la page sans explication, non interprété.
- **Retrait** : aucune date de retrait de Large 4 (https://docs.mistral.ai/models/overview) ; préavis de 6 mois en GA ; après retrait, réponse 404.
- **Identifiant plus précis** (daté, par exemple `-2610`) : non trouvé.
- **Non vérifié** : l'identifiant n'a pas été essayé contre l'API.

## Lecture de la session
`mistral-large-4-0` est un identifiant de la forme « version majeure et mineure fixées », que Mistral oppose à ses alias, en disponibilité générale, sans mise à jour silencieuse annoncée. Il satisfait le choix 3 (b) au sens de la documentation, sous trois réserves à écrire au texte : (1) aucune garantie écrite sur les poids ; (2) la version servie est relevée par programme à chaque appel (texte, 3.4) ; (3) l'identifiant accepté par l'API se constate au premier appel de l'essai (vérification de la clé avant la file).
