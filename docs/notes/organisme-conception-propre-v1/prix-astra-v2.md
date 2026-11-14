# Prix de `gpt-6-astra`, lu sur la page officielle d'OpenAI — v2

Remplace pour la lecture `lecture-classement-v3/prix-astra-v1.md` (`839a3e6c…`, « prix non lu »), qui reste en place (R12). Relevé par la session mère le 14 novembre 2026 (R-2676), commande lancée à 08:45:38Z (`date -u`).

## Source
- Adresse demandée : `https://platform.openai.com/docs/pricing`, redirigée vers `https://developers.openai.com/api/docs/pricing` ; statut 200 ; 599 534 octets. Copie versée et scellée : `docs/sources/tarifs-openai-v1/developers-openai-com-api-docs-pricing-2026-11-14.html` (`099c9496f75ffe6f08a57f30b007c5abf79f6eb26ecba5ddecf50ffdf4ec8028`). L'autre adresse, `https://openai.com/api/pricing/`, a répondu 403.
- Réseau : l'environnement de la session est en accès non restreint ; l'échec du développeur (`ENOTFOUND`) venait de l'outil de lecture de pages, pas d'une règle du réseau. **Aucun changement d'environnement n'a été fait** (l'approbation prévue par R-2676 n'a pas eu à être demandée).

## Valeurs (USD par million de jetons ; tableau « Flagship models », contexte « Short : ≤ 272K input tokens », sélecteur coché par défaut)
| Palier | Entrée | Entrée en cache | Sortie |
|---|---|---|---|
| Standard | 10,00 | 1,00 | 50,00 |
| Flex / Batch | 5,00 | 0,50 | 25,00 |
| Fast | 20,00 | 2,00 | 100,00 |
| Ultrafast | 60,00 | 6,00 | 300,00 |

Lues deux fois : dans le texte rendu du tableau et dans les données de la page (composant `TextTokenPricingTables`, paliers `standard`, `batch`, `fast`, `ultrafast`, ligne `gpt-6-astra`). Les corps de la lecture (≈ 15 000 à 51 000 jetons d'entrée) sont sous le seuil de 272 000 : le contexte « Short » s'applique. Le barème « supposé » du dépôt (10 / 50) est donc **égal** au prix standard publié.

## Devis recalculé (formules de `lecture-classement-v3/devis-lecture-astra-v1.md`, § 2 et 3 ; entrée en cache comptée au prix plein, borne haute)
| | Standard (10 / 50) | Flex (5 / 25) |
|---|---|---|
| Un appel, attendu (effort `medium`) | 1,00 USD | 0,50 USD |
| Un appel, pire cas | 2,15 USD | 1,07 USD |
| 18 appels, attendu (`medium`) | 17,28 USD | 8,64 USD |
| 18 appels, attendu (`low`) | 8,68 USD | 4,34 USD |
| 18 appels, pire cas (borné par la garde) | 38,50 USD | 19,25 USD |
| Plafond pour que les 18 appels passent (`medium`) | 18,46 USD | 9,23 USD |

Rappels : reste de la ligne GO-2026-11-13-06 : 14,21 USD (plafond 21) ; reste de la réserve du lecteur : 2,74 USD. En standard et effort `medium`, la lecture complète ne tient pas dans la ligne ; en Flex, elle y tient. L'outil v3 n'envoie que le palier par défaut (aucun champ `service_tier`) : le palier Flex demande une version neuve de l'outil, contre-lue. Le palier Flex peut être plus lent et refuser un appel faute de ressources : sous la règle « arrêt au premier écart », un refus arrête la lecture.
