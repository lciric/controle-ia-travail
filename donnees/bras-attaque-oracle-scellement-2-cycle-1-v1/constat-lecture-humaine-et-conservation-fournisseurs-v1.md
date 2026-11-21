# Constat — lecture humaine possible et durée de conservation chez les fournisseurs des lecteurs — v1

- Classe C. Établi le 2026-11-21 vers 19:05 UTC par le monteur de l'oracle du cycle 1, à la demande de la mère (message de 19:00 UTC ; pièce de sécurité v9 du banc fermé, champ 18). **Aucun contenu de famille ni d'oracle.**
- Sources : pages publiques récupérées le 2026-11-21 vers 19:01 UTC (`curl`, sans compte), versées telles quelles dans `sources-conditions-fournisseurs-v1/`, avec leurs empreintes ci-dessous. Les citations sont recopiées mot pour mot du texte des pages.

| fournisseur | page | empreinte sha256 |
|---|---|---|
| | `ai.google.dev_gemini-api_docs_usage-policies.html` | `ad9f490ae1965a28…` |
| | `ai.google.dev_gemini-api_terms.html` | `b2c1aa502cceec13…` |
| | `docs.x.ai_docs_faq_security.html` | `e1bda7107d0d1fb2…` |
| | `openai.com_policies_services-agreement.html` | `1edd80fc1fe57fb1…` |
| | `platform.openai.com_docs_guides_your-data.html` | `361792f03668f4d4…` |

## Lecteur 1 — OpenAI (interface de programmation)

- **Lecture humaine possible : oui.** La page des données (`platform.openai.com/docs/guides/your-data`) ne dit pas « revue humaine » pour le régime par défaut ; elle le dit par contraste. Pour un régime spécial, accordé sur approbation, elle écrit : « such content will be excluded from human review unless required by applicable law ». Pour les clients en « Zero Data Retention » ou « Modified Abuse Monitoring », dans un cas de risque grave : « we may retain and human review customer content […] that our classifiers detect as potentially violating our Usage Policies ». J'en conclus que, dans le régime par défaut, le contenu signalé peut être lu par une personne.
- **Conservation : jusqu'à 30 jours par défaut** : « abuse monitoring logs are generated for all API feature usage and retained for up to 30 days, unless longer retention is required by law, or is reasonably necessary to protect our services or any third party from harm ». L'exclusion de ces journaux (« Zero Data Retention » ou « Modified Abuse Monitoring ») demande l'approbation préalable d'OpenAI.
- **Entraînement** : « not used to train or improve OpenAI models (unless you explicitly opt in) ».

## Lecteur 2 — Google Gemini (interface de programmation)

- Page datée : « Gemini API Additional Terms of Service — Effective March 23, 2026 ».
- **Service gratuit à exclure** : « human reviewers may read, annotate, and process your API input and output », et les contenus servent à améliorer les produits de Google. **Seul le service payant est admissible.**
- **Service payant, lecture humaine possible : oui.** La page « Abuse monitoring » dit : « When prompts or model outputs are flagged by safety filters and abuse detection systems […], authorized Google employees may assess the flagged content ». Elle dit aussi : « a project […] may be flagged for manual review by authorized Google personnel ».
- **Conservation : 55 jours** (service payant) : « Google retains the following data for fifty-five (55) days for the purposes of detecting and preventing violations of the Prohibited Use Policy » ; les conditions disent : « logs prompts and responses for a limited period of time, solely for detecting and preventing violations ».
- **Entraînement** (service payant) : « Google doesn't use your prompts […] or responses to improve our products ».

## Ancre et énoncés neutres — xAI (pour mémoire)

- **Conservation : 30 jours par défaut** : « all API requests and responses are stored on our servers (encrypted at rest) for 30 days for auditing purposes in the event of suspected abuse or misuse » (`docs.x.ai/docs/faq/security`). Une option « Zero Data Retention » est en libre-service pour l'administrateur d'une équipe.
- **Lecture humaine possible : non établi.** La page n'en dit rien. Les pages des conditions et de la politique de confidentialité de `x.ai` ont refusé la récupération automatique (403) : rien n'est versé d'elles.

## Conséquence, selon la règle de la mère

La règle est : « oui » ou « non établi » ⇒ ce lecteur ne lit pas, ou nœud à Lazar. Les deux lecteurs proposés répondent **oui**, et l'agent proposé pour l'ancre répond **non établi**. **Aucun des trois ne peut lire sans le mot de Lazar.**

Je ne connais aucun fournisseur hors Llama, Qwen, Mistral et Claude dont l'interface payante exclut toute lecture humaine par défaut. Les régimes sans conservation (OpenAI, xAI) ou à surveillance modifiée demandent une approbation ou un réglage du compte. Même accordés, ils laissent une revue possible dans les cas graves (OpenAI). **Nœud à porter à Lazar** :

- **Option 1** : accepter une lecture humaine possible, limitée aux contenus signalés, avec une conservation de 30 jours (OpenAI) et de 55 jours (Google), et l'inscrire en réserve dans la pièce de sécurité.
- **Option 2** : demander les régimes sans conservation (OpenAI « Zero Data Retention », xAI « Zero Data Retention »), ce qui demande une démarche de compte par Lazar.
- **Option 3** : des lecteurs locaux à poids ouverts, hors des familles exclues. Mais un modèle local peut entrer dans une base boîte noire de G1 (réserve 1 du réfutateur).

Ma recommandation : l'option 2 pour les deux lecteurs si elle est accordée à temps, sinon l'option 1. Confiance : moyenne.
