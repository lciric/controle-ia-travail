# Devis — course d'auto-conception de l'organisme d'idéation — v2h : Argon et Carbon proposeurs sans troncature, 6,05 USD par appel

- Auteur : développeur unique de la version (modèle L′), 19 novembre 2026. Version 2h (R12 ; le devis v2g, `devis-course-auto-conception-v2g.md`, `0cd9b1bb…`, reste en place). **Rien n'a été lancé** ; aucun appel, aucune dépense.
- Fondement : mots de Lazar « go (a) », « augmente le plafond », « enlève la troncature pour Carbon », « Clé Minuit (Recommandé) », **« fais sauter la troncature pour argo aussi »** ; demande de la session principale (plafond par appel des proposeurs 6,05 USD) ; mère R-3613, R-3616. Additif `course-v4/additif-preenregistrement-course-auto-conception-v2h.md` (`be46d1366ff10670c6dd721628e463ea9c29b363b91d0f424f73b63589ca8c47`).
- Chiffres lus dans la sortie scellée du calcul : `course-v4/calcul-devis-course-auto-conception-v2h.json`, sha256 `9462478ddf2ed103b5f7651f6a353c80bb8afb1c50636eaa96f413a608befe3c`, écrite par `course-v4/calcul-devis-course-auto-conception-v2h.py` (`767e41daafca8fe6aa5eeed5bb0ebb4e4608d40589845ba481c7e634a0edd5b9`), qui charge le lanceur v8 (`0640e99f…`) pour refaire la garde de la commande.

## 1. Total

| | estimation | haut | au pire |
|---|---|---|---|
| proposition (Opus 7,42 ; Fable 17,30 ; Astra 4,80 ; **Argon 4,18** ; **Carbon 10,94**) | 44,64 | 70,03 (Argon et Carbon 20,26 chacun) | plafond dur 110 |
| aiguillage | 3,41 | 20,46 | |
| juges | 7,89 | 47,32 | |
| **course** | **55,94 USD** | 137,81 (brut, au-delà du plafond) | **120 USD** (plafond d'arrêt) |
| épreuve des témoins du jour (v8) | 1,18 | | 5 USD (ligne à part) |
| sonde réelle de Carbon (v1, plus grand lot) | 1,86 | | **6 USD** (ligne à part) |
| sonde d'Astra du jour | ≤ 0,05 | | 0,05 |
| **total** | **59,03 USD** | | **131,05 USD** |

La ligne de GO de la course porte **exactement 120 USD** (inchangé). Estimation inchangée depuis la v2g : faute de mesure d'Argon sans budget de pensée, son estimation reste son coût réel de la v6 (0,38 USD par appel) ; son haut suppose une pensée comme celle de Carbon en v6 (32 765 jetons, ≈ 1,84 USD par appel).

## 2. Argon et Carbon proposeurs : réglage, pire cas d'un appel (plafond 6,05 USD)

Même réglage pour les deux (enveloppes `appel-argon-sans-troncature-v1.sh`, branche proposeur, et `appel-carbon-synchrone-v1.sh`) : sortie 65 536 (maximum de la commande), budget de pensée non fixé, provision 65 536, prix 8,3 / 41,5, 3 caractères par jeton, marge 5 %, délai 1 680 s, timeout 1 720 + 20 s ; relais 8788 (Argon) et 8792 (Carbon). Plus grande entrée servie : lot 1, 136 265 octets, 130 101 caractères.

| compte des jetons d'entrée | entrée gardée | sortie retenue | pire cas d'un appel |
|---|---|---|---|
| caractères / 3 (compte de la commande) | 45 536 | **65 536** | 5,817437 USD |
| octets / 2 (borne prudente du lanceur) | 71 540 | **65 536** (sous 6,00 : 64 734) | **6,03327 USD ≤ 6,05** |

Le lanceur v8 exige la sortie maximale **aux deux comptes** (`pire_cas_sans_troncature`). Onze appels au pire : 66,37 USD chacun ; part au pire de Carbon (règle du lanceur) 11 × 6,05 = **66,55 USD**.

**Réglage actuel d'Argon (`appel-argon-v5.sh`, courses v4 et v6) et ce qui change** : délai 1 500 s, sortie 65 536 réduite par la garde (≈ 57 265 jetons sur le plus grand lot sous l'ancien plafond de 3 USD), provision et `thinkingBudget` 8 192 (pensée au-delà : code 7), 4 caractères par jeton, timeout 1 700 s → proposeur : budget retiré, provision 65 536, sortie 65 536 retenue, 3 caractères par jeton, délai 1 680 s, timeout 1 720 s.

**Argon juge** (réglage v5 gardé, plafond 0,60 USD) : la garde retient ≈ **5 560** jetons de sortie (consigne de juge et fiche de 9 000 caractères ; 5 875 pour 3 000 caractères) sous un `thinkingBudget` de 8 192 ; le même traitement « sans troncature » ne laisserait que ≈ 6 876 jetons de sortie **et** de pensée (code 7 au-delà) : gardé à la v5. Coût au pire d'un jugement : 0,60 USD (inchangé).

## 3. Seuils internes (règle d'A1) et plafonds d'étape souples

Inchangés dans leur forme (S17 120) : proposition, plafond dur 110 ; aiguillage lancé si cumul ≤ 105 ; juges si cumul ≤ 90.

| scénario | cumul après la proposition | cumul avant les juges | juges lancés ? |
|---|---|---|---|
| estimation | 44,64 | 48,05 | **oui** (plafond dur 71,95) |
| haut (Argon et Carbon à 1,84 par appel, aiguillage au haut) | 70,03 | **90,49** | **non** (> 90 : non mesurée, budget, C13) |
| Carbon au pire (Argon au réel v6) | 100,06 | 115,06 | non |
| Argon et Carbon au pire | 110 (plafond dur) | 110 | non (aiguillage non lancé non plus) |

**Les juges sont lancés tant qu'Argon et Carbon proposeurs coûtent ensemble au plus ≈ 57,07 USD sur onze cases (aiguillage estimé, 3,41) ou ≈ 40,02 USD (aiguillage au haut, 20,46)**. Le seuil interne **bloque donc au haut** : c'est le prix de la sortie sans troncature des deux espèces Gemini. Leviers possibles (décision de Lazar, non pris ici) : relever S17 (et la ligne de GO), ou le plafond de relais de l'étape « juges » (30 → plus), ou garder la troncature d'Argon.

## 4. Parts au pire par clé, crédits

| clé | part au pire | crédit, reste |
|---|---|---|
| Claude, `RR_ANTHROPIC_API_KEY_MINUIT` | **120 USD** | 200 déclarés (R-3228, R-3616) ; dépense antérieure 0,000108 + épreuve (≈ 0,97) ; réserves vides → reste net ≈ **199,03 > 120** ; ≈ 79,03 au pire après la course |
| Gemini, `GEMINI_API_KEY` (Argon tient un juge ; Carbon 11 × 6,05) | 120 USD | illisible, sous dispense (R-3237) |
| OpenAI, `OPENAI_API_KEY` (Astra 11 × 6,05) | **66,55 USD** | illisible, sous dispense ; relais d'Astra à `--plafond-usd 67` |

**Relais d'Argon** : bornes inchangées, 2 × 231 + 2 = **464** appels (proposeur et juge : countTokens puis generateContent par appel ; vérifié, `appels_relais_gemini_requis`, `controler_relais_argon` identique à la v7). Relais de Carbon ≥ 24.
