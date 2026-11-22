# Prix de gpt-6.2-astra relevé sur la page d'OpenAI

Relevé à 2026-11-22T14:14:09Z (`date -u`), sur le mot de la mère (14:13Z). Classe C. La page a été lue par un agent de lecture web, réponse HTTP 200. Ce relevé est une transcription : il n'est pas opposable au sens de R7 tant que la page n'est pas archivée avec son empreinte.

- **Adresse** : https://developers.openai.com/api/docs/models/gpt-6.2-astra , section « Pricing » > « Text tokens ».
- **Lignes citées mot pour mot** :
  - « | Input | $8 | 1M tokens | »
  - « | Cached input | $0.4 | 1M tokens | »
  - « | Cache writes | $10 | 1M tokens | » (rétention de 30 minutes)
  - « | Output | $40 | 1M tokens | »
- **Contexte** : « Prices are per 1M tokens. » « Batch costs 50% of Standard rates. »
- **Contexte long** : au-delà de 272K jetons d'entrée, « input and cache rates double and output costs 1.5 times the short-context rate for the full request ». Cela donne 16 USD en entrée et 60 USD en sortie pour toute la requête.

## Écart avec les moteurs
Les moteurs v8d, v8m et v8p appliquent à Astra le prix de gpt-6-astra : **10 USD par million en entrée et 50 en sortie**.
- **Sous 272K jetons d'entrée** : coûts et pires cas sont **surestimés** de 20 % (8 / 40 réels). La garde de dépense reste donc prudente.
- **Au-delà de 272K jetons d'entrée** : le coût est **sous-estimé** (16 / 60 réels contre 10 / 50). Aucune invite servie à Astra ne l'a atteint jusqu'ici : la plus grande, celle des critiques de l'essaim, fait environ 300 000 caractères, soit environ 120 000 jetons.
- La prochaine version contre-lue portera 8 / 40, et 16 / 60 au-delà de 272K jetons d'entrée.
