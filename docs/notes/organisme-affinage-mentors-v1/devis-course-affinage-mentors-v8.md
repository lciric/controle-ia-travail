# Devis de la course d'affinage des idées des mentors — v8 : Carbon avec sa pensée (non engagé)

- Écrit le 2026-11-18T21:43:20Z (`date -u +%FT%TZ`) par le modèle L', correctif v8 demandé par la mère. **Version 8** (R12) : les devis v1 à v6b restent en place ; le devis v6b (`devis-course-affinage-mentors-v6b.md`, `2326666d11529c59799205de6014ca94bdc8c9b0ac0d1139eacb281579ebb129`) est la base ; seul le poste de **Carbon** change. Même composition déclarée (deux Claude, Argon, Astra, Carbon ; pas de Kimi), même plafond d'arrêt (150 USD), même ligne de GO (GO-2026-11-18-14). Aucun appel ; aucun réseau.
- Pourquoi : la course d'auto-conception v4 a montré que Carbon pense en lot bien au-delà du budget de pensée demandé (diagnostic `docs/notes/organisme-auto-conception-v1/course-v2/diagnostic-erreurs-carbon-astra-course-v4-v1.md` sur `lot/compte-organisme-v1`, `510312b105c62ad01a1d45ab9078dfc04333ce3bc2322b98695fa48c4daa8aec`, § 2 : 17 454, 18 823 et 20 696 jetons de pensée, sortie 2 202 à 3 410 jetons). Le devis v6 comptait tout proposeur hors Claude à 0,276 USD par appel (0,400484 au pire appel) : ce prix ne contient pas une telle pensée.

## 1. Réglages de Carbon retenus en v8, et pire cas d'un appel

Commande `commande_gemini_lot_v1.py` (`9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75`, épinglée, inchangée) : prix plein 8,3 et 41,5 USD par million (bornes hautes de R-3271), facteur du lot 0,5, **provision de pensée 28 672**, **sortie maximale 16 384**, sortie minimale 4 096, délai de lot **1 620 s**, relevé toutes les 30 s, **délai de requête 60 s**.

Garde avant envoi de la commande (l. 167-173), au prix plein, sous le plafond de session d'un proposeur de l'affinage (**1,50 USD**, configuration v6) ; entrée gardée = caractères de la consigne servie / 3 × 1,05 (calcul du lanceur v8, `controler_pire_cas_carbon`, sur les seize fils réels) :

| consigne servie | caractères | entrée gardée (jetons) | sortie demandée par la commande | pire cas minimal (sortie 4 096) | **pire cas d'un appel, prix plein** | même pire cas au prix du lot |
|---|---|---|---|---|---|---|
| fil le plus long | 7 478 | 2 618 | 6 948 | 1,3816 | **1,499959** | 0,749980 |
| fil le plus court | 4 250 | 1 488 | 7 174 | 1,3722 | **1,499959** | 0,749980 |

- **Pire cas d'un appel de Carbon : 1,50 USD au plus (1,499959)**, sous le plafond par appel de l'affinage (1,50) par construction de la garde de la commande ; 0,75 USD au prix du lot si la pensée reste sous la provision. Sur tout échec après la création du lot (codes 3, 5, 6, 7), la commande rend ce pire cas au prix plein, que l'orchestrateur compte.
- **La provision de 32 768 jetons demandée ne tient pas** sous 1,50 USD : (4 096 + 32 768) × 41,5 / 10⁶ = 1,5299 USD avant même l'entrée (1,5516 avec l'entrée la plus longue) ; la commande refuserait **chaque** appel (code 4, rien envoyé) et Carbon serait absente de fait. 28 672 (28 × 1 024) laisse 6 948 jetons de sortie demandée sur le fil le plus long, 2,0 fois la plus forte sortie observée (3 410), avec une marge de pensée de 28 672 / 20 696 = 1,385 ; 30 720 aurait donné 1,48 de marge de pensée mais 4 900 jetons de sortie (1,44 fois) : choix du développeur, à trancher autrement par la mère si elle le veut (une version suivante).
- La sortie maximale de 16 384 n'est jamais atteinte : la commande la ramène à ce que le plafond paie (6 948 à 7 174 jetons).

## 2. Prix estimé d'un appel de Carbon

Hypothèse déclarée, non mesurée sur l'affinage : pensée 20 000 jetons (plus forte pensée observée, arrondie), sortie 3 500 (plus forte sortie observée, arrondie), entrée 2 618 (fil le plus long, borne haute) ; prix du lot :

(2 618 × 8,3 + (20 000 + 3 500) × 41,5) / 10⁶ × 0,5 = **0,4985 USD par appel** (au lieu de 0,276).

Haut par appel : **1,50 USD** (pire cas compté par la commande sur un échec après la création du lot), au lieu de 0,400484.

## 3. Totaux (composition déclarée, cinq espèces)

| poste | estimation | haut |
|---|---|---|
| proposeurs | 24,70 (21,14 + 16 × 0,2225) | 59,21 (41,62 + 16 × 1,099516) |
| aiguilleur (première espèce Claude) | 4,96 | 21,12 |
| juges (première espèce Claude et Argon) | 11,47 | 31,24 |
| sous-total | **41,136** | 111,57 |
| marge de 10 % | 4,11 | 11,16 |
| **total** | **45,25** | **122,73** |

- **Estimation : 45,25 USD** (41,14 sans marge) ; **haut : 122,73 USD** ; majoré de 25 % : 56,56 et **153,41**. Le haut majoré dépasse 150 : il suppose les seize appels de Carbon échoués au pire cas en plus de tous les hauts des autres postes ; le plafond d'arrêt de 150 USD coupe alors une étape (« non mesuré (budget) ») et la course s'arrête proprement. Rien n'est changé au plafond.
- **Pire cas de la course : 150 USD** (plafond d'arrêt, S17 de la configuration, tenu par l'orchestrateur ; borne par les plafonds de session : 352 USD, au-dessus).
- Base de l'écart au devis du manifeste de fin (lanceur v8, `devis_estimation`) : **41,136 USD** sans marge pour les cinq espèces déclarées (37,576 en v7).

## 4. Part au pire par clé (règle R-3237, inchangée)

| clé (nom de variable) | relais, rôles | estimation (marge comprise) | haut | **part au pire** |
|---|---|---|---|---|
| `RR_ANTHROPIC_API_KEY_MINUIT` | Claude : deux proposeurs, aiguilleur, premier juge | 20,65 | 74,62 | **150,00** (plafond d'arrêt) |
| `GEMINI_API_KEY`, partagée par **Argon et Carbon** | Argon : proposeur, second juge ; Carbon : proposeur | 10,97 + 8,77 = **19,74** | 14,66 + 26,40 = **41,06** | **174,00** (150 + 24) |
| clé d'OpenAI, **injectée par le secret de réseau** (nom déclaré `OPENAI_API_KEY`) | Astra : proposeur | 4,86 | 7,05 | **24,00** (16 × 1,50) |
| clé de Kimi | — | — | — | non déclarée (R-3279) |

- Carbon : 16 × 0,4985 × 1,1 = 8,77 ; 16 × 1,50 × 1,1 = 26,40. Part au pire de Carbon **inchangée : 24 USD** (16 appels × 1,50, plafond de session), ce que le lanceur v8 vérifie aussi par la garde du pire cas de la commande. Somme des estimations par clé : 20,65 + 19,74 + 4,86 = 45,25.
- Clé d'OpenAI : le relais d'Astra lit `OPENAI_API_KEY` dans son environnement au démarrage, posée par la session d'exécution depuis le secret de réseau ; ni la valeur ni le secret ne sont lus ici. Les clés de Google et d'OpenAI restent « non lisibles » sous la dispense R-3237 ; Minuit est lue (ou comptée au prix relevé : 200 USD déclarés moins la dépense antérieure, qui comprend la dépense réelle de la course d'auto-conception v4).
- La sonde commune d'Astra du jour (au plus 0,05 USD, appel réel trivial, R-3273) est en sus, sur la clé d'OpenAI, hors du plafond de la course.

## 5. Plafond demandé

**150 USD**, plafond d'arrêt de toute la course, **inchangé** (GO-2026-11-18-14, R-3215) : aucune ligne de GO neuve n'est demandée. Le plafond par appel d'un proposeur (1,50 USD, configuration v6 épinglée) est inchangé ; c'est lui qui interdit la provision de 32 768 jetons (§ 1).

## 6. Ce qui n'est pas établi

- Le prix estimé de Carbon repose sur trois lots d'une autre course (entrées de 29 000 à 41 000 jetons) ; la pensée sur les consignes de l'affinage (2 600 jetons au plus) n'est pas mesurée.
- Si le fournisseur compte la pensée dans `maxOutputTokens` (documentation non lue, aucun réseau), une sortie demandée de 6 948 jetons couperait la réponse (`MAX_TOKENS`, code 5) dès que la pensée dépasse environ 3 500 jetons ; aucun réglage sous 1,50 USD ne tient alors avec cette commande : seul un plafond par appel relevé pour Carbon (configuration neuve) le permettrait (rapport du développeur v8, points ouverts).
- Le diagnostic donne « ≈ 1,1 à 1,3 USD » pour les trois lots refusés de la course d'auto-conception : c'est la formule de la commande (`c0`, l. 211) au prix plein (1,14 à 1,26 USD sur ses compteurs) ; au facteur du lot 0,5 de l'affinage, ces lots auraient coûté 0,57 à 0,63 USD. Le facteur passé dans cette autre course n'est pas relu ici ; le présent devis compte la pensée au prix du lot (estimation) et le pire cas au prix plein (haut).
