# Usage des données envoyées à Google (Gemini) et à Mistral — relevé documentaire — v1

Relevé fait le 2026-11-20 par un agent de lecture web de la session de relance (`session_01QPDgKgkCezLtWTAC6NJ7ok`), pour la question de la condition d'envoi des textes (brouillon 41, note, question 1 ; vérification du 41). Pages lues par un outil qui résume ; citations courtes ; provenance par transcription, non opposable (R7). Aucune clé, aucun appel, aucune dépense.

## Google, API Gemini, offre payante (`gemini-4-neon`)
- **Entraînement : non sur l'offre payante.** https://aistudio.google.com/docs/pricing, « Gemini 4 Neon » : « Used to improve our products » = « No » (payant). https://aistudio.google.com/docs/terms, « Paid Services » : « When you use Paid Services, including, for example, the paid quota of the Gemini API, Google doesn't use your prompts » … « or responses to improve our products ». Est payant un accès par « a Cloud Project associated with an active billing account ». Aucun réglage à refuser ; le partage de « datasets » de journaux (https://aistudio.google.com/docs/logs-policy) « may be used to improve model quality » : option distincte, à ne pas activer. Le « Contributor Tier » ne vise pas Neon.
- **Conservation** : « Google logs prompts and responses for a limited period of time, solely for detecting and preventing violations » ; durée non trouvée. Journaux du projet : 55 jours au plus par défaut, réglables à 7, 14, 28 ou 55 jours ; activés par défaut pour certains appels.
- **Non-conservation** : non trouvée.
- **Région** : « This data may be stored transiently or cached in any country in which Google or its agents maintain facilities. » Aucun choix trouvé.

## Mistral, API, offre payante (`mistral-large-4-0`)
- **Entraînement** : https://legal.mistral.ai/terms/commercial-terms-of-service, 4.2 « Training » : « Mistral AI will not use Customer Data or Outputs to train its artificial intelligence models except » (exceptions : retours, modèles « Labs » ou « Preview », 4.3). https://help.mistral.ai/en/articles/455207-… : refus possible à tout moment, panneau d'administration, « Privacy », « Data usage for improving our services ». Réglage par défaut du bouton : non trouvé.
- **Conservation par défaut** : non trouvée (accord de traitement non lu).
- **Non-conservation** (https://docs.mistral.ai/admin/monitor-comply/zero-data-retention) : offerte sur l'usage à la demande pour les appels sans état, dont `/v1/chat/completions` ; sur demande, accordée « at our discretion » (https://help.mistral.ai/en/articles/347612-…).
- **Région** (https://docs.mistral.ai/inference/regional-inference) : point d'accès `api.eu.mistral.ai`, « Multiple data centers in EU and EFTA countries », facturé 1,1 fois le prix courant ; « Regional inference does not provide regional storage for all control-plane data ». Service de `mistral-large-4-0` sur ce point d'accès : non vérifié.
