# Devis de la course d'affinage des idées des mentors — v9 : plafond par appel des proposeurs à 3,00 USD (non engagé)

- Écrit le 2026-11-18T22:11:35Z (`date -u +%FT%TZ`) par le modèle L', correctif v9 demandé par la session principale (option 1 (c) du rapport du développeur v8, décidée sous l'autonomie de Lazar). **Version 9** (R12) : les devis v1 à v8 restent en place ; base : devis v8 (`devis-course-affinage-mentors-v8.md`, `91171ea56e0c3b9eb6486a5f8d0444f1017cdf4a00b5f4e5c5b3f540529aa97f`) et v6b. Même composition (deux Claude, Argon, Astra, Carbon ; pas de Kimi), même plafond d'arrêt (150 USD), même ligne de GO (GO-2026-11-18-14). Aucun appel ; aucun réseau.
- Ce qui change : configuration v9 (`course-v9/configuration-course-affinage-mentors-v9.json`), **plafond de session des proposeurs 3,00 USD** (1,50 en v6) ; Carbon à sortie maximale **32 768** et provision **28 672**. Raison : la documentation du fournisseur (lue par la session principale) compte la pensée dans la sortie maximale ; sous 1,50 USD la commande de Carbon n'aurait demandé qu'environ 7 000 jetons, pensée comprise, contre 20 696 jetons de pensée observés (diagnostic `510312b1…`).

## 1. Carbon : réglages, sortie retenue et pire cas d'un appel

Commande `commande_gemini_lot_v1.py` (`9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75`, épinglée, inchangée) : prix plein 8,3 et 41,5 USD par million, facteur du lot 0,5, **sortie maximale 32 768**, sortie minimale 4 096, **provision 28 672**, délai de lot 1 620 s, relevé toutes les 30 s, délai de requête 60 s (durée maximale 1 770 s, sous les 1 800 s de l'orchestrateur épinglé).

Garde avant envoi de la commande (l. 167-173), au prix plein, sous **3,00 USD** ; entrée gardée = caractères de la consigne servie / 3 × 1,05 (calcul du lanceur v9 sur les seize fils ; recoupé en jouant hors réseau la vraie commande de `main`, essai `test_v9_arithmetique_recoupee_avec_la_vraie_commande_de_carbon`) :

| consigne servie | caractères | entrée gardée | **sortie retenue (demandée au fournisseur)** | pire cas minimal | **pire cas d'un appel, prix plein** | au prix du lot |
|---|---|---|---|---|---|---|
| fil le plus long | 7 478 | 2 618 | **32 768** | 1,3816 | **2,571489** | 1,285745 |
| fil le plus court | 4 250 | 1 488 | **32 768** | 1,3722 | **2,562110** | 1,281055 |

- **Sortie retenue : 32 768 jetons ≥ 24 500** (plus forte pensée observée 20 696 + plus forte réponse observée 3 410 = 24 106, arrondi) sur toutes les entrées : le lanceur v9 le vérifie et refuse sinon.
- **Pire cas d'un appel de Carbon : 2,5715 USD au prix plein**, sous 3,00 ; c'est aussi ce que la commande rend sur un échec après la création du lot (codes 3, 5, 6, 7). Si la pensée compte dans la sortie maximale (documentation), la facture réelle d'un appel ne dépasse pas l'entrée + 32 768 jetons de sortie : 1,38 USD au prix plein, 0,69 au prix du lot ; la provision est alors une réserve de la garde.
- Une pensée au-delà de 28 672 jetons rend le code 7 (réponse refusée, pire cas compté) ; si pensée et réponse dépassent ensemble 32 768 jetons, la réponse est coupée (code 5).

## 2. Prix par appel

- Carbon, estimation : **0,4985 USD** (inchangée depuis la v8 : pensée 20 000, réponse 3 500, entrée 2 618, prix du lot) ; haut : **2,5715** (pire cas compté par la commande sur un échec).
- Claude, Argon, Astra : prix estimés et hauts du devis v6 inchangés (ils viennent des jetons, non du plafond). Le plafond relevé élargit seulement ce qu'un appel **peut** coûter : Astra demande 32 768 jetons au plus, pire cas d'un appel 1,73 USD par la formule de sa commande (corps de 8 011 octets au plus) ; un proposeur Claude a un budget de session de 3,00 ; Argon remplit son plafond selon sa propre garde.

## 3. Totaux (composition déclarée, cinq espèces)

| poste | estimation | haut |
|---|---|---|
| proposeurs | 24,70 | 76,36 (59,21 + 16 × (2,5715 − 1,50)) |
| aiguilleur (première espèce Claude) | 4,96 | 21,12 |
| juges (première espèce Claude et Argon) | 11,47 | 31,24 |
| sous-total | **41,136** | 128,72 |
| marge de 10 % | 4,11 | 12,87 |
| **total** | **45,25** | **141,59** |

- **Estimation : 45,25 USD** (41,14 sans marge, inchangée depuis la v8) ; **haut : 141,59 USD** ; majoré de 25 % : 56,56 et 176,98.
- **Pire cas de la course : 150 USD** (plafond d'arrêt, S17, tenu par l'orchestrateur ; borne par les plafonds de session : 80 × 3,00 + 160 × 0,25 + 320 × 0,60 = 472 USD, au-dessus).
- **Plafond dur de l'étape « proposition » : 60 USD** (configuration, inchangé). Le haut de la proposition (76,36) le dépasse : dans ce régime (Carbon échouant à chaque appel au pire cas, A3 ne l'arrêtant pas), l'orchestrateur coupe l'étape (« non mesuré (budget) »), et la course s'arrête proprement en l'écrivant. A3 arrête Carbon après trois échecs consécutifs, ce qui rend ce régime peu probable ; il n'est pas exclu.
- Base de l'écart au devis du manifeste de fin : 41,136 USD sans marge (inchangée).

## 4. Part au pire par clé (règle R-3237 : 16 × plafond de session pour un relais de proposeur seul ; 150 pour un relais qui tient l'aiguilleur ou un juge)

| clé (nom de variable) | relais, rôles | estimation (marge comprise) | haut | **part au pire v9** | v8 |
|---|---|---|---|---|---|
| `RR_ANTHROPIC_API_KEY_MINUIT` | Claude : deux proposeurs, aiguilleur, premier juge | 20,65 | 74,62 | **150,00** | 150 |
| `GEMINI_API_KEY`, partagée par **Argon et Carbon** | Argon : proposeur, second juge ; Carbon : proposeur | 10,97 + 8,77 = **19,74** | 14,66 + 45,26 = **59,92** | **198,00** (150 + 16 × 3,00) | 174 |
| clé d'OpenAI, **injectée par le secret de réseau** (nom déclaré `OPENAI_API_KEY`) | Astra : proposeur | 4,86 | 7,05 | **48,00** (16 × 3,00) | 24 |
| clé de Kimi | — | — | — | non déclarée | — |

- **Une part dépasse ce que la ligne permet** : la clé de Google, **198 USD**, au-dessus du plafond de la ligne GO-2026-11-18-14 (150 USD). Ce n'est pas une dépense possible de la course : la part au pire est la somme des bornes de deux relais, et la dépense réelle de toute la course, toutes clés comprises, reste bornée par le plafond d'arrêt de 150 USD (déjà vrai en v7 et v8 : 174). La clé part sous la dispense R-3237 (solde illisible) : la part n'est confrontée à aucun reste lu ; si son solde devenait lisible, le lanceur exigerait un reste au-dessus de 198 USD. Les parts d'Astra (48) et de Minuit (150) tiennent dans la ligne.
- Relais d'Astra lancé à `--plafond-usd 48` exactement (le lanceur exige l'égalité avec sa part) ; ce plafond n'ajoute aucune dépense possible au-delà de ce que seize appels à 1,73 USD au plus peuvent coûter (27,66).
- Somme des estimations par clé : 20,65 + 19,74 + 4,86 = 45,25.
- La sonde commune d'Astra du jour (au plus 0,05 USD, appel réel trivial, R-3273) est en sus, sur la clé d'OpenAI, hors du plafond de la course.

## 5. Plafond demandé

**150 USD**, plafond d'arrêt de toute la course, **inchangé** (GO-2026-11-18-14) : aucune ligne de GO neuve n'est demandée. Le plafond par appel des proposeurs passe à 3,00 USD (configuration v9) ; il ne change aucune borne de la course entière.

## 6. Ce qui n'est pas établi

- La pensée de Carbon sur les consignes de l'affinage (2 600 jetons d'entrée au plus) n'est pas mesurée ; l'estimation repose sur trois lots d'une autre course.
- Lecture de la documentation du fournisseur faite par la session principale, non par ce devis (aucun réseau). Une note du dépôt (`commande_argon_v3d.py`, l. 260-261) dit avoir constaté, sur un appel synchrone d'Argon, que l'interface ne comptait pas les pensées dans la sortie maximale : les réglages v9 tiennent dans les deux lectures (32 768 ≥ 24 500 et provision 28 672 ≥ 1,25 × 20 696).
- Le coût réel des sessions Claude, d'Argon et d'Astra sous un plafond de 3,00 n'est pas mesuré : leurs estimations sont celles du devis v6.
