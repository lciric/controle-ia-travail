# Devis — course d'auto-conception de l'organisme d'idéation — v2

- Auteur : session du compte organisme (modèle I). Version 2 (R12 ; la v1, `devis-course-auto-conception-v1.md`, `50e7d2f1…`, reste en place). **Rien n'a été lancé.**
- Ce qui change depuis la v1 : composition par défaut **sans Kimi** (constat 1 de la contre-lecture de la v1 : une espèce déclarée qui échoue consomme la tentative ; Kimi seulement sur mot écrit de la mère) ; prix de Carbon donnés par la mère (R-3271 : bornes hautes 8,3 / 41,5 USD par million, commande par lot) ; reste net de la clé Claude (réserves de R-3271) ; `--max-appels` des relais Gemini ; entrées recalculées sur la consigne v2 (expurgée, quelques octets de moins). Plafond d'arrêt **inchangé : 90 USD** ; épreuve des témoins **inchangée : 5 USD**.
- Chiffres calculés par programme, sans appel : `calcul-devis-course-auto-conception-v2.py` (`110db726edcfdb76324fb042c4cce483864eb0285d10651a424cf2cd9b1e9b30`), sortie `calcul-devis-course-auto-conception-v2.json` (`91f5cf8f147689eb2fa9ff9db8b6e3b91b15496174e03f07a66d691676c2db2b`). Hypothèses et sources des prix inchangées (devis v1, § 3) ; Carbon : bornes hautes de la mère, prix plein, remise du lot non comptée.

## 1. Ce qui est servi

Inchangé : **tout** le catalogue v3, en onze lots découpés par ses propres titres ; v2 : nom du directeur et identifiants de session internes retirés par programme de tout texte servi (trois remplacements dans la consigne, trois dans la partie commune des lots, listés).

## 2. Totaux par composition

| composition | appels (proposeurs / aiguilleur / juges, estimation) | estimation | haut |
|---|---|---|---|
| **par défaut** : deux espèces Claude + Argon | 33 / 66 / 132 | **22,33 USD** | 69,95 USD |
| + Astra (sur mot écrit de la mère) | 44 / 88 / 176 | 31,57 USD | 96,64 USD |
| + Carbon (sur mot écrit de la mère) | 44 / 88 / 176 | 30,38 USD | 94,41 USD |
| + Astra + Carbon | 55 / 110 / 220 | 39,62 USD | 121,10 USD |
| + Kimi (sur mot écrit de la mère seulement) | 44 / 88 / 176 | 25,99 USD | 86,14 USD |
| toutes | 66 / 132 / 264 | 43,27 USD | 137,28 USD |

Au haut, les compositions avec Astra ou Carbon dépassent 90 USD : le plafond d'arrêt coupe (une étape protégée qui ne tient pas sous son plafond n'est pas lancée : « non mesurée (budget) », issue rapportée). Par appel de proposeur (estimation / haut) : Claude 1 0,254 / 0,478 ; Claude 2 0,634 / 1,194 ; Argon et Carbon 0,526 / 0,991 ; Astra 0,634 / 1,194 ; Kimi 0,127 / 0,239.

## 3. Plafond d'arrêt : 90 USD (inchangé)

Recommandation (confiance moyenne) : 90 USD. Il couvre le haut de la composition par défaut (69,95) avec une marge, et l'estimation de toute composition (au plus 43,27) deux fois. Plafonds de relais des étapes protégées : proposition 45, aiguillage 15, juges 30.

## 4. Part au pire par clé, reste net

| relais (clé) | estimation | haut | part au pire (règle du lanceur) |
|---|---|---|---|
| Claude (`RR_ANTHROPIC_API_KEY_RIGAUD`, R-3271) : deux proposeurs, aiguilleur, juge 1 | 14,25 USD (composition par défaut ; 15,75 avec une espèce de plus) | 45,30 USD (54,29) | 90 USD |
| Argon : proposeur, juge 2 | 8,08 USD (par défaut ; 8,84 avec une espèce de plus) | 24,64 USD (29,22) | 90 USD |
| Astra (si déclarée) | 6,98 USD | 13,13 USD | 33 USD (11 × plafond de session) |
| Carbon (si déclarée) | 5,79 USD | 10,90 USD | 33 USD |
| Kimi (si déclaré) | 1,40 USD | 2,63 USD | ≈ 4,8 USD, plus la réserve Moonshot de 15 USD ≤ 90 % du reste |

**Clé Claude, reste net** (constat 8) : crédit déclaré 124 USD − ≈ 2 USD déjà dépensés − réserves 9 (course Carbon en cours) et 9 (étape 3 d'E5) = **≈ 104 USD**, au-dessus de la part au pire (90) de ≈ 14 USD **avant** l'épreuve des témoins (au plus 5 sur la même clé : ≈ 0,75 attendu sur le relais Claude) ; le relevé du jour, fait après l'épreuve, doit donc lire un reste net > 90 ; sinon le lanceur arrête avant le départ (code 3) et écrit l'alerte pour la mère.

## 5. Relais Gemini

Argon (relais v2, port 8788) : au pire 11 + 11 × espèces actives × 4 appels — 143 par défaut, 231 avec Astra et Carbon, 275 avec toutes : **`--max-appels 280`**. Épreuve des témoins : 11 appels d'Argon, **`--max-appels 15`** (constat 10 : une marge de reprise ; « non conclue » reste un arrêt). Carbon (relais v4, port 8792, par lot) : 11 lots au pire.

## 6. Épreuve réelle des témoins (inchangée)

33 appels (22 sur le relais Claude, 11 sur Argon) ; estimation 1,13 USD, haut 3,39 USD, plafond 5 USD, ligne de GO à part.

## 7. Total demandé

Course 90 USD + épreuve 5 USD = **95 USD au plus** ; attendu ≈ 23,5 USD dans la composition par défaut, épreuve comprise (≈ 15,0 sur la clé Claude).
