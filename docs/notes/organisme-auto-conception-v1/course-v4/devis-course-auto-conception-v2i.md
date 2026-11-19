# Devis — course d'auto-conception de l'organisme d'idéation — v2i : plafond d'arrêt 150 USD, seuils internes relevés d'autant, conservation des réponses brutes

- Auteur : développeur unique de la version (modèle L′), 19 novembre 2026. Version 2i (R12 ; le devis v2h, `devis-course-auto-conception-v2h.md`, `9462478d…` pour son calcul, reste en place). **Rien n'a été lancé** ; aucun appel, aucune dépense.
- Fondement : mot de Lazar (option choisie) **« Course à 150 USD (Recommandé) »** — « plafond d'arrêt de la course 120 → 150 USD (ligne de GO à 150 exactement), seuils internes relevés d'autant ; les juges passent aussi au haut. Clé Minuit (≈ 199 nets) le couvre. » ; règle de Lazar R-3661 (« il faut TOUJOURS récupérer ce qui est récupérable ») ; additif `course-v4/additif-preenregistrement-course-auto-conception-v2i.md` (`1433b6a98a0fce4fad74e79465b69acd0b5ebb797fe3f26890179de70015d71b`).
- Chiffres lus dans la sortie scellée du calcul : `course-v4/calcul-devis-course-auto-conception-v2i.json`, sha256 `1f43d53185ba4c93043e038c968c9a62245c2ae86f51c9754a3b42cd1a79743b`, écrite par `course-v4/calcul-devis-course-auto-conception-v2i.py` (`8120b61c5a9da40d8ae9ab983d0e7cf7e5b315e2933575d121e505d307d2402d`), qui charge le lanceur v9 (`1b47c1cf…`) et la vraie classe `BudgetV56` de l'orchestrateur épinglé (`pole/budget_v56.py`, `3a672ace…`, empreinte égale à celle que le lanceur épingle).

## 1. Total

Bases inchangées depuis le devis v2h (coûts réels de la course v6 ; Argon et Carbon proposeurs : estimation au réel v6 et aux lots v4, haut à la pensée de Carbon en v6, 1,841446 USD par appel ; aiguillage et juges du devis v2) : seul le plafond d'arrêt change.

| | estimation | haut | au pire |
|---|---|---|---|
| proposition (Opus 7,42 ; Fable 17,30 ; Astra 4,80 ; Argon 4,18 ; Carbon 10,94) | 44,64 | 70,03 | plafond dur **140** |
| aiguillage | 3,41 | 20,46 | |
| juges | 7,89 | 47,32 | |
| **course** | **55,94 USD** | **137,81 USD (≤ 150 : tout est lancé)** | **150 USD** (plafond d'arrêt) |
| épreuve des témoins du jour (v9) | 1,18 | | 5 USD (ligne à part) |
| sonde réelle de Carbon (v1, plus grand lot) | 1,86 | | 6 USD (ligne à part) |
| sonde d'Astra du jour | ≤ 0,05 | | 0,05 |
| conservation des réponses brutes (R-3661) | **0** (enveloppe locale, aucun appel) | | 0 |
| **total** | **59,03 USD** | | **161,05 USD** (150 + 5 + 6 + 0,05) |

La ligne de GO de la course porte **exactement 150 USD** (montant que l'orchestrateur exige : S17 de la configuration v5).

## 2. Seuils internes (règle d'A1), lus par la vraie classe `BudgetV56`

Configuration v5 (`3f662ee8…`) : S17 150 ; étapes protégées inchangées (plafonds de relais 45, 15, 30 ; attendus 19, 3, 7) ; étapes sacrifiables à 151 (retirées par construction). Les seuils montent **d'autant** (+ 30) : plafond dur de la proposition 110 → **140** ; aiguillage lancé si le cumul est au plus 105 → **135** ; juges si au plus 90 → **120**.

| scénario (configuration v5) | proposition (plafond dur) | aiguillage (cumul avant ; plafond dur) | juges (cumul avant ; plafond dur) | sous la v4 (S17 120) |
|---|---|---|---|---|
| estimation | 44,64 (140) | lancé (44,64 ; 98,35) | **lancés** (48,05 ; 101,94) | lancés |
| **haut** | 70,03 (140) | **lancé** (70,03 ; **72,96**) | **lancés** (90,49 ≤ 120 ; **59,50** ≥ 47,32) | **juges non lancés** (90,49 > 90) |
| Carbon au pire (Argon au réel v6), aiguillage au haut | 100,06 (140) | lancé (100,06 ; 42,93) | non lancés (120,52 > 120) | aiguillage non lancé |
| Argon et Carbon au pire | 162,25 > 140 : **coupée** (C13) | — | — | coupée |

La lecture du lanceur v9 (`lecture_a1`) est **d'accord** avec `BudgetV56` sur les quatre scénarios (états et plafonds durs, étape par étape ; champ `lanceur_et_budget_v56_d_accord`), et `garde_seuils_au_haut` accepte la v5 et refuse la v4. Au haut, la course coûterait ≈ 137,81 USD ≤ 150. **Les juges sont lancés tant que le cumul avant eux est au plus 120 USD**, c'est-à-dire tant qu'Argon et Carbon proposeurs coûtent ensemble au plus ≈ **87,07 USD** sur onze cases (aiguillage estimé, 3,41) ou ≈ **70,02 USD** (aiguillage au haut, 20,46). Note : la formule reprise du calcul v2h arrondit au plus proche (72,97 ; 59,51) ; l'orchestrateur arrondit au centime inférieur (72,96 ; 59,50) — les chiffres de l'orchestrateur font foi.

## 3. Parts au pire par clé, crédits

| clé | part au pire | crédit, reste |
|---|---|---|
| Claude, `RR_ANTHROPIC_API_KEY_MINUIT` | **150 USD** | 200 déclarés (R-3228, R-3616) ; dépense antérieure 0,000108 + épreuve (≈ 0,97) ; réserves vides → reste net ≈ **199,03 > 150** (et ≥ 40, un cinquième) ; ≈ **49,03** au pire après la course |
| Gemini, `GEMINI_API_KEY` (Argon tient un juge ; Carbon 11 × 6,05) | **150 USD** | illisible, sous dispense (R-3237) |
| OpenAI, `OPENAI_API_KEY` (Astra 11 × 6,05) | 66,55 USD | illisible, sous dispense ; relais d'Astra à `--plafond-usd 67` (inchangé) |

Relais Claude de la course : `--plafond-usd 150` (égal au plafond d'arrêt, exigé à l'identique). Relais d'Argon : 464 appels (inchangé) ; Carbon ≥ 24 (inchangé).

## 4. Rien d'autre ne change

Réglages d'Argon (proposeur sans troncature, juge v5) et de Carbon (synchrone, sans troncature) ; **6,05 USD** par appel des proposeurs (pire cas d'un appel 6,03327 USD à la borne prudente, 5,817437 au compte de la commande) ; composition ; clé Minuit ; juges ; épreuve (5 USD), sonde de Carbon (6 USD), sonde d'Astra (0,05 USD). La conservation des réponses brutes (enveloppe `scripts/enveloppe_conservation_reponses_v1.py`, `c7a3e0dd…`) et l'inventaire de fin ne coûtent rien (local, aucun appel) ; un échec d'écriture arrête l'appel (le coût déjà déclaré par la commande reste compté).
