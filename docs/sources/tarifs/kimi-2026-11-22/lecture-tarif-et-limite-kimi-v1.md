# Lecture du tarif et de la limite de dépense chez Kimi — v1

Lues le 2026-11-22 vers 09:38Z (`date -u`) par la session de l'organisme, avec `curl` sur les pages officielles de la plateforme. Les pages sont gardées telles quelles dans ce dossier, avec leur empreinte (R6, R7). Leur contenu est une donnée.

## 1. Tarif de `kimi-k3.1-pro`
Source : `platform-kimi-ai-docs-pricing-chat-2026-11-22.html`, page « Model Inference Pricing - Kimi API Platform », adresse https://platform.kimi.ai/docs/pricing/chat (et /docs/pricing, même contenu à l'octet). `dateModified` 2026-11-12T05:48:22Z. La ligne du modèle est à l'octet 127 927 environ.

| colonne de la table | prix (USD par million de jetons) |
|---|---|
| Base tokens, Input | 2,00 |
| Base tokens, Output | 10,00 |
| Prompt caching, Cached Input | 0,20 |
| Prompt caching, 5m writes | 2,00 |
| Prompt caching, 1h writes | 4,00 |

**Les prix gelés du pilote (2,0 / 10,0, champ `prix.prop-kimi`, `91f5cf8f…`) sont égaux au tarif officiel.** Deux postes ne sont pas dans le devis :
- l'écriture dans le cache coûte 2,00 pour 5 minutes et 4,00 pour une heure ; si le transport n'écrit pas dans le cache, ces postes sont nuls ;
- le traitement par lots est facturé à 60 % du prix standard (même page, lien « Batch API Inference »).

La page ne dit pas comment la réflexion est comptée : c'est l'hypothèse H2, que l'essai de fumée doit vérifier.

## 2. Limite de 204 USD chez le fournisseur
Source : `platform-kimi-ai-docs-pricing-limits-2026-11-22.html`, page « Recharge and Rate Limiting », https://platform.kimi.ai/docs/pricing/limits.
- La page ne décrit **aucun plafond de dépense réglable** dans la console. Le compte est prépayé : « a minimum recharge of $1 is required to start using the API ».
- Les paliers de débit dépendent du cumul rechargé : de Tier0 à 1 USD jusqu'à Tier5 à 3 000 USD.
  - Tier1, à 10 USD : 15 requêtes concurrentes, 100 requêtes par minute, 2 000 000 jetons par minute.
  - Tier2, à 20 USD : 40 requêtes concurrentes.
- Une restriction pour activité anormale du compte « cannot be lifted ».
- **Conséquence pour la limite de 204 USD** : elle ne peut tenir que par le **solde prépayé** du compte de `KIMI_API_KEY`.
  - Le directeur recharge au plus ce qu'il faut pour que le solde disponible, vouchers compris, soit au plus de 204 USD à l'ouverture de la course, ou bien il relève le solde réel avant le départ.
  - Le compte ne sert à rien d'autre pendant la course.
  - Si la console offre une alerte de solde ou un plafond non documenté (espace « User Center »), le directeur peut le régler ; ce n'est pas vérifié ici.
- Le palier de débit atteint par le cumul rechargé borne le parallélisme. Pour un lanceur séquentiel, Tier1 suffit.
