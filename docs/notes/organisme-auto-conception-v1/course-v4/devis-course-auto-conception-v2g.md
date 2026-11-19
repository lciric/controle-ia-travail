# Devis — course d'auto-conception de l'organisme d'idéation — v2g : Carbon synchrone sans troncature, plafonds relevés, clé Minuit

- Auteur : développeur unique de la version (modèle L′), 19 novembre 2026. Version 2g (R12 ; le devis v2f, `course-v3/devis-course-auto-conception-v2f.md`, `7a8ef9d4…`, reste en place). **Rien n'a été lancé** ; aucun appel, aucune dépense.
- Fondement : mots de Lazar « go (a) » (Carbon par la commande synchrone d'Argon, éprouvé d'abord par un appel réel sur le plus grand lot, puis course), « augmente le plafond » (6 USD par appel des proposeurs ; 120 USD d'arrêt), « enlève la troncature pour Carbon », « Clé Minuit (Recommandé) » ; mère R-3613 (« (a) si la clé Minuit a du crédit, sinon (b) » → (a) : clé vérifiée active le 19 novembre à 06:37:04Z, appel minimal, HTTP 200, 0,000108 USD) et R-3616 (réservation de Minuit levée pour cette course ; crédit 200 USD, dépense antérieure inscrite 0). Additif `course-v4/additif-preenregistrement-course-auto-conception-v2g.md` (`2b0d3e7a553c60c013f81c37f6150c27285e80377219920495fba8a8816bb867`).
- Chiffres lus dans la sortie scellée du calcul : `course-v4/calcul-devis-course-auto-conception-v2g.json`, sha256 `b01678ad8db9790fcef5f0ae5debb542f0ee5c36d772c5f8953f85bc1a821be5`, écrite par `course-v4/calcul-devis-course-auto-conception-v2g.py` (`bf1e8a04466eb7a4da64d30342f4f2aabd0e446dace1bad53b7c0efc46c1152f`). Bases : coûts réels de la course v6 (manifeste de fin `3ed8cc61…`) pour Opus, Fable, Argon, Astra ; usage des lots de Carbon de la v4 (diagnostic `510312b1…`) et pensée de la v6 (journal v62, PO-178) ; garde de la commande refaite par le lanceur v7 (`b10b2d18…`) sur la plus grande entrée servie ; aiguillage et juges : calcul du devis v2 (`91f5cf8f…`) ; épreuve : coût réel de l'épreuve v6 (`fe787c62…`).

## 1. Total

| | estimation | haut | au pire |
|---|---|---|---|
| proposition (Opus 7,42 ; Fable 17,30 ; Argon 4,18 ; Astra 4,80 ; Carbon 10,94) | 44,64 | 53,95 (Carbon 20,26) | plafond dur 110 |
| aiguillage | 3,41 | 20,46 | |
| juges | 7,89 | 47,32 | |
| **course** | **55,94 USD** | 121,74 (brut, au-delà du plafond) | **120 USD** (plafond d'arrêt) |
| épreuve des témoins du jour (v7) | 1,18 | | 5 USD (ligne à part) |
| **sonde réelle de Carbon** (un appel, plus grand lot) | 1,86 | | **6 USD** (ligne à part ; pire cas par la garde 5,82) |
| sonde d'Astra du jour | ≤ 0,05 | | 0,05 |
| **total** | **59,03 USD** (59,027543) | | **131,05 USD** |

**La ligne de GO de la course porte exactement 120 USD** (l'orchestrateur exige l'égalité : `montant_requis` = S17 de la configuration v3 ; le lanceur v7 aussi) ; l'épreuve, 5 USD ; la sonde de Carbon, **6 USD**, périmètre « sonde » et « Carbon » (le programme de sonde l'exige). Estimation proche de la v2f (59,81) : le relèvement des plafonds ne change pas l'usage attendu ; il change le pire.

## 2. Carbon : réglage retenu, pire cas d'un appel

Réglage figé par l'enveloppe `appel-carbon-synchrone-v1.sh` (`b380be0b…`) : `--max-sortie-jetons 65536` (le maximum de la commande, `MAX_SORTIE_JETONS_DEFAUT`, `commande_argon_v3d.py` l. 348 ; aucune autre source dans le dépôt ni dans l'orchestrateur), `--sans-config-pensee` (budget de pensée non fixé : défaut du fournisseur), `--provision-pensee-jetons 65536` (≥ la sortie), prix 8,3 / 41,5, 3 caractères par jeton, marge 5 %, délai 1 680 s, arrêt dur 1 720 + 20 s.

La commande compte la provision **en plus** de la sortie : pire = entrée gardée × 8,3 / 10⁶ + (sortie + provision) × 41,5 / 10⁶. Sur la plus grande entrée servie (lot 1, 136 265 octets, 130 101 caractères) :

| compte des jetons d'entrée | entrée gardée | sortie retenue | pire cas d'un appel | plafond qui tiendrait la sortie maximale |
|---|---|---|---|---|
| **caractères / 3, compte de la commande** | 45 536 | **65 536** (aucune réduction) | **5,817437 USD ≤ 6** | 5,82 |
| octets / 2, borne prudente (si countTokens dépassait car. / 3) | 71 540 | 64 734 (réduite) | 5,999987 | **6,04** |

Onze appels au pire : 63,99 USD (part au pire du relais de Carbon, règle du lanceur : 11 × 6 = 66 USD). Estimation par appel 0,99 USD (usage de la v4) ; haut 1,84 USD (pensée de 32 765 et réponse de 3 410 jetons, comme en v6). **Pour Lazar** : le plafond de 6 USD tient la sortie maximale au compte de la commande ; si l'on veut qu'il la tienne aussi à la borne prudente, il faut **6,04 USD par appel** (non pris ; la sonde relève le compte réel de l'entrée, `entree_jetons_comptee`, et le lanceur exige que la sortie demandée par la sonde soit 65 536).

## 3. Seuils internes (règle d'A1, `pole/budget_v56.py`) et plafonds d'étape souples

| | v6 (S17 90) | v7 (S17 120) |
|---|---|---|
| plafond dur de la proposition au lancement : max(45 ; S17 − 0 − 10) | 80 | **110** |
| aiguillage lancé si le cumul ≤ S17 − 15 | 75 | **105** |
| juges lancés si le cumul ≤ S17 − 30 | 60 | **90** |

- **À l'estimation** : cumul après la proposition 44,64, avant les juges 48,05 → tout est lancé (plafonds durs : aiguillage 68,36, juges 71,95).
- **Au haut** : 53,95 puis 74,41 → tout est lancé (juges 45,59).
- **Si Carbon atteignait son pire cas aux onze appels** (les autres au réel de la v6) : cumul 97,69 après la proposition, aiguillage lancé (plafond dur 15,31), cumul avant les juges jusqu'à 113 > 90 → **l'étape « juges » serait non mesurée (budget, C13)**. Le seuil se franchit dès que Carbon dépasse ≈ 52,9 USD sur onze appels (≈ 4,81 par appel) avec l'aiguillage estimé, ou ≈ 35,8 USD (≈ 3,26 par appel) avec l'aiguillage au haut. Aucun seuil ne bloque à l'estimation ni au haut ; la marge dépend de la pensée réelle de Carbon (mesurée par la sonde).
- Plafonds de session inchangés : juge 0,60, aiguilleur 0,25.

## 4. Parts au pire par clé, crédits

| clé | part au pire (règle du lanceur) | crédit, reste |
|---|---|---|
| **Claude, `RR_ANTHROPIC_API_KEY_MINUIT`** (relais de l'aiguilleur et d'un juge) | **120 USD** | crédit déclaré 200 (R-3228, mère R-3616) ; dépense antérieure 0 + 0,000108 (vérification) + épreuve v7 (≈ 0,97) ; réserves vides → reste net ≈ **199,03 > 120** (et ≥ un cinquième) : départ admis ; reste au pire après la course ≈ 79,03 |
| Gemini, `GEMINI_API_KEY` (Argon tient un juge ; Carbon 11 × 6) | 120 USD | illisible, sous la dispense de la mère (R-3237) |
| OpenAI, `OPENAI_API_KEY` (Astra) | 66 USD (11 × 6) | illisible, sous dispense |

Réserve de la mère (R-3616) : la variable Minuit est commune à l'environnement par défaut ; un usage non inscrit d'une autre session n'est pas exclu ; le relevé de facturation de Lazar fait foi. La clé Rigaud est refusée par le lanceur v7.

## 5. Points inchangés

Aucune reprise d'Astra ; part d'Astra au pire relevée par le seul plafond de session (11 × 6 = 66) ; relais d'Astra à régler en conséquence (commandes v2g : `--plafond-usd 67`). Plafond de l'épreuve 5 USD. Bornes des relais Gemini : Argon 464 (2 × 231 + 2), Carbon 24 (2 × 11 + 2) au moins.
