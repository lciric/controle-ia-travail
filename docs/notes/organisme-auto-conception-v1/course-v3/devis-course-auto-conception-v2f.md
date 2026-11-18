# Devis — course d'auto-conception de l'organisme d'idéation — v2f : tentative neuve, Carbon à pensée 28 672 et sortie 32 768

- Auteur : développeur unique de la tentative neuve (modèle L′), 18 novembre 2026. Version 2f (R12 ; le devis v2e, `devis-course-auto-conception-v2e.md`, `c643830e…`, reste en place). **Rien n'a été lancé** ; aucun appel, aucune dépense.
- Ce qui change depuis la v2e : le seul réglage de Carbon (la pensée compte dans `maxOutputTokens`, documentation du fournisseur lue par la session principale ; additif v2f) : `--provision-pensee-jetons 28672 --max-sortie-jetons 32768 --delai-s 1620 --delai-requete-s 60`. L'estimation ne change pas (elle repose sur l'usage réel des lots, non sur les réglages) ; seul le pire cas d'un appel de Carbon change.
- Chiffres lus dans la sortie scellée du calcul : `course-v3/calcul-devis-course-auto-conception-v2f.json`, sha256 `5dc32255031322c6da058f3942808a973c8d4f70c21bd9a870daec85e633b9e2`, écrite par `course-v3/calcul-devis-course-auto-conception-v2f.py` (scellé). Base : coûts réels de la course v4 (manifeste de fin `2625234c786a7fc50c926325c1a9efc8a8e9b74146a59205bf8a31c6e2c5fd7f`), usage des quatre lots de Carbon (diagnostic `510312b1…`, § 2), épreuve v4 (`980e8888…`), calcul du devis v2 (`91f5cf8f…`) pour l'aiguillage et les juges.

## 1. Total (inchangé depuis la v2e)

| | estimation | au pire |
|---|---|---|
| course (proposition 47,26 ; aiguillage 3,41 ; juges 7,89) | **58,55 USD** | **90 USD** (plafond d'arrêt) |
| épreuve des témoins du jour (v6) | 1,20 | 5 USD (ligne à part) |
| sonde d'Astra du jour | ≤ 0,05 | 0,05 |
| **total** | **59,81 USD** (59,807539) | **95,05 USD** |

Les ≈ 45 USD attendus sont le coût de la v4, arrêtée après l'étape « proposition ». **La ligne de GO de la course porte exactement 90 USD** (exigé à l'identique par l'orchestrateur, `verifier_go_v55`, et par le lanceur) ; l'épreuve, 5 USD.

## 2. Carbon : pire cas d'un appel, calculé comme la commande le calcule

La commande ajoute sortie et provision : pire = entrée gardée × 8,3 / 10⁶ + (`maxOutputTokens` + provision) × 41,5 / 10⁶, et réduit d'elle-même `maxOutputTokens` pour tenir le plafond de session (3 USD). Sur la plus grande entrée servie (136 622 octets) :

| compte des jetons d'entrée | entrée gardée | `maxOutputTokens` retenu | pire cas | sortie retenue ≥ 24 500 ? |
|---|---|---|---|---|
| caractères / 3 (règle de la commande) | 47 818 | **32 768** | **2,946649 USD** | oui |
| octets / 2 (borne prudente du lanceur v6) | 71 727 | **29 271** | **2,999969 USD** | oui |

Sous le plafond de 3 USD par appel dans les deux cas. La sortie retenue (où la pensée **et** la réponse doivent tenir) reste au-dessus de 24 500 jetons (pensée la plus forte observée 20 696 + ≈ 3 500 de réponse) ; la pensée de 28 672 au plus laisse au moins 4 096 jetons de réponse dans 32 768. 11 appels au pire : **33,00 USD** (part au pire du relais de Carbon calculée par le lanceur : 33 USD, inchangée). Estimation par appel inchangée : 0,994890 USD (usage réel moyen), 10,94 USD pour 11.

## 3. Points inchangés depuis la v2e

- **Clé Claude** : reste net estimé au départ 124 − 33,27 − 18 = **72,73 USD ≤ 90** → code 3 aux chiffres de la pièce v2 ; il faut un crédit déclaré > 141,27 USD, des réserves revues ou une autre clé.
- **Seuil des juges** : cumul après l'aiguillage ≤ 60 USD (estimation 50,67).
- Part par clé : Claude ≈ 32,27 (+ ≈ 1,00 d'épreuve) ; Gemini (Argon et Carbon) ≈ 18,98 (+ ≈ 0,20) ; Astra ≈ 7,31 (+ ≤ 0,05).
- Aucune reprise d'Astra ; délai de Carbon borné par le délai fixe de 1 800 s de l'orchestrateur (durée au pire de la commande 1 770 s).
