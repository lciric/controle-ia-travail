# Identifiants de Google (Gemini hors concepteurs) pour le juge des deux ancres — relevé documentaire — v1

Relevé fait le 2026-11-20 par un agent de lecture web de la session de relance (`session_01QPDgKgkCezLtWTAC6NJ7ok`), pour le choix 3 (b) de Lazar (seul un identifiant figé est admis ; pièce `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-cinq-choix-lecteur-bras-a-2026-11-20-v1.md`, 93cbc6f4c78d00c5b91ca29e5b300bef345cd7aa46c89db2be6bff95a46d5beb) et l'option (c) posée à Lazar. Pages lues par un outil qui résume ; provenance par transcription, non opposable (R7). Aucune clé, aucun appel, aucune dépense. Les adresses `ai.google.dev` et `cloud.google.com` redirigent vers `aistudio.google.com/docs/...` et `docs.cloud.google.com/...`.

## Règle de nommage de Google (https://aistudio.google.com/docs/models, « Model version name patterns »)
- **Stable** : « Points to a specific stable model. Stable models usually don't change. » (« usually » : pas une garantie d'immutabilité).
- **Latest** (alias) : « This alias will get hot-swapped with every new release of a specific model variation. » ; « A 2-week notice will be provided through email before the version behind latest is changed. »
- **Preview** : dépréciée avec au moins deux semaines de préavis. **Experimental** : non stable.
- Vertex AI (https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) : « While retirement timelines may be extended, they won't be moved to an earlier date than what is listed. »
- Non trouvé : une règle qui dise qu'un nom stable ne change jamais ; des identifiants numérotés pour ces modèles.

## `gemini-4-neon`
- Fiche (https://aistudio.google.com/docs/models/gemini-4-neon) : « Stable: `gemini-4-neon` ». Sortie le 18 novembre 2026 ; « No shutdown date announced » (https://aistudio.google.com/docs/deprecations). Absent des tables de Vertex AI.
- Prix (https://aistudio.google.com/docs/pricing), offre payante seulement : 3 USD en entrée, 15 USD en sortie (raisonnement compris) par million de jetons.
- Raisonnement (https://aistudio.google.com/docs/whats-new-gemini-4-neon) : « It supports four thinking levels: `low`, `medium`, `high` (default), and `xhigh`. » ; température et échantillonnage ignorés.

## `gemini-4-hydrogen`
- Fiche : « Stable: `gemini-4-hydrogen` ». Sortie le 12 novembre 2026 ; aucune date de retrait. Sur Vertex AI, rangé parmi les « Models available for shorter availability periods » : « Short-term availability models remain active until a replacement model is released and a retirement date is announced. »
- Prix : 1,5 USD et 7,5 USD par million de jetons ; offre gratuite avec « Used to improve our products: Yes ».

## Lecture de la session
Google range `gemini-4-neon` dans une catégorie « stable » écrite, distincte de ses alias, ce qu'OpenAI ne fait pas pour `gpt-6.2-sol` (`docs/notes/relance-organismes-discrets-v1/juge-des-ancres-identifiant-openai-v1.md`). La garantie reste plus faible que chez Mistral (« Silent updates: No ») : « usually don't change ». `gemini-4-hydrogen` est donné pour une disponibilité courte. Neon est le plus proche du choix 3 (b) parmi les modèles hors concepteurs et hors familles des lecteurs.
