# API de Mistral et de Google pour les essais d'admission — relevé documentaire — v1

Relevé fait le 2026-11-21 par un agent de lecture web de la session de relance (`session_01QPDgKgkCezLtWTAC6NJ7ok`), pour les corrections 1 à 3 et 8 de la contre-lecture du devis des essais d'admission (`docs/notes/relance-organismes-discrets-v1/contre-lecture-devis-essais-admission-brouillon1-v1.md`). Sources officielles ; citations courtes ; « [résumé] » = tiré du résumé de l'outil, non du texte exact ; provenance par transcription, non opposable (R7). Aucune clé, aucun appel, aucune dépense. Les adresses `ai.google.dev` redirigent vers `aistudio.google.com`.

## Mistral Large 4 (`mistral-large-4-0`), `POST /v1/chat/completions`
- **`max_tokens`** (https://docs.mistral.ai/api/) : « The maximum number of tokens to generate in the completion. » Raisonnement compris ou non : **non trouvé**.
- **Forme de la réponse** (https://docs.mistral.ai/capabilities/reasoning) : « `message.content` is a **list of chunks** instead of a plain string » ; morceau de pensée, puis « `TextChunk` (`type: "text"`): contains the final answer. » Texte jugé = concaténation des seuls morceaux `text`. Large 4 refuse `none`, `minimal`, `xhigh`, `max` ; `reasoning_effort` : `low`, `medium`, `high`, défaut `high`.
- **`usage`** : noms des champs **non trouvés** dans les pages lues (exemple vide ; schéma non atteint). Facturation du raisonnement au prix de sortie : **non trouvée** (« uses reasoning tokens »).
- **`finish_reason`** : seule valeur vue, `stop` ; les autres : **non trouvées**.
- **`model`** : champ présent, requis ; forme rendue pour Large 4 : **non trouvée**.
- **Flux** : `stream` possible ; la pensée est émise au fil de l'eau (« delta.content changes shape during the response ») ; délai du serveur : non trouvé.
- **Erreur « modèle inconnu »** : **non trouvée** ; le schéma donne 422 « Validation Error » pour le chat [résumé].
- **`temperature`** : recommandation générale « between 0.0 and 0.7 » ; effet sous raisonnement : non trouvé.
- **`GET /v1/models`** : objet `data` + `object: "list"` selon le schéma, tableau nu dans l'exemple (contradiction non résolue) ; champs `id`, `aliases`, `archived`…
- **Prix** (https://docs.mistral.ai/models/mistral-large-4-0 ; https://docs.mistral.ai/inference/pricing) : 0,7 USD en entrée, 0,07 en cache, 2,1 en sortie par million de jetons. Point d'accès européen : « billed at 1.1× standard list pricing » (https://docs.mistral.ai/inference/regional-inference) ; disponibilité de Large 4 sur ce point d'accès : non trouvée. La FAQ de https://mistral.ai/pricing cite « Mistral Large » à 0,5 et 1,5 USD : autre modèle, à ne pas employer. Recharge minimale et taxes : non trouvées.

## Gemini 4 Neon (`gemini-4-neon`), `generateContent`
- **`maxOutputTokens`** : les pages disent que la borne couvre pensée et réponse (« including thought tokens » ; « caps combined thinking and output tokens for a response », https://aistudio.google.com/docs/thinking, https://aistudio.google.com/docs/whats-new-gemini-4-neon), mais ces phrases visent `max_output_tokens` de l'API Interactions ; pour `generateContent`, confirmation directe non trouvée.
- **Réglage** : `generationConfig.thinkingConfig.thinkingLevel` [résumé] ; valeurs REST en majuscules `LOW`, `MEDIUM`, `HIGH`, `XHIGH` [résumé] ; Neon : `low`, `medium`, `high` (défaut), `xhigh` ; `minimal` rejeté.
- **`usageMetadata`** (https://aistudio.google.com/api-reference/generate-content) : `promptTokenCount`, `candidatesTokenCount`, `thoughtsTokenCount` (« Number of tokens of thoughts for thinking models »), `totalTokenCount`. Pensée facturée en sortie : « Output tokens, including thinking tokens: $15.00 per 1M tokens ».
- **Forme de la réponse** : « In the `generateContent` API, there are no dedicated thought blocks. » ; pensée non rendue sauf `includeThoughts` [résumé] ; extraction du texte final : non documentée (texte des parts, `includeThoughts` non envoyé).
- **`finishReason`** : `STOP`, `MAX_TOKENS`, `SAFETY`, `RECITATION`, `OTHER`, `MALFORMED_RESPONSE`, `CONTINUATION` (« reached the per-request token limit, but generation is not yet complete »), et d'autres.
- **`modelVersion`** : « The model version used to generate the response. » ; forme rendue pour Neon : non trouvée.
- **Délai** : « set HTTP client timeouts to at least 15 minutes » ; « Hard prompts can take several minutes. » Flux de la pensée en `generateContent` : non trouvé.
- **`temperature`** : « The server ignores in-range custom values if sent. » ; « Remove `temperature`, `top_p`, and `top_k` from requests. »
- **Erreur « modèle inconnu »** : non trouvée.
- **Prix** (https://aistudio.google.com/docs/pricing) : 3,00 USD en entrée, 15,00 en sortie (pensée comprise) ; « Gemini 4 Neon is not available on the Free tier. » Recharge minimale et taxes : non trouvées.
