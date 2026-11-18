# Devis de la course d'affinage des idées des mentors — v6b : composition déclarée (Astra et Carbon, sans Kimi) (non engagé)

- Écrit le 18 novembre 2026 par la session du compte organisme (modèle I). **Version 6b** (R12) : le devis v6 (`devis-course-affinage-mentors-v6.md`, `48dfd571d3f9a2042a363ccb7c35da30ab6b924fc443ae83139d0f75880dddaa`) reste en place ; mêmes prix, mêmes hypothèses, même plafond d'arrêt (150 USD), même ligne de GO. Seule la **composition déclarée** change, sur le mot du directeur (18 novembre, vers 10:50Z) et R-3279 : **deux espèces Claude + Argon + Astra + Carbon** ; Kimi non déclaré.
- Aucun appel ; chiffres tirés du devis v6 (§ 1 et § 3), recalculés à la main ci-dessous.

## 1. Totaux

La composition déclarée a **cinq** espèces de proposeurs, comme la colonne « sans Carbon » du devis v6 (deux Claude, Argon, Kimi, Astra) : 80 appels de proposeur, 160 cartes, 160 aiguillages, 320 jugements (560 appels). Le devis v6 compte **tout** proposeur hors Claude au même prix par appel (0,276 USD en moyenne, 0,400484 au pire appel ; § 1) : remplacer Kimi par Carbon ne change donc aucun total.

| poste | estimation | haut |
|---|---|---|
| proposeurs | 21,14 | 41,62 |
| aiguilleur (première espèce Claude) | 4,96 | 21,12 |
| juges (première espèce Claude et Argon) | 11,47 | 31,24 |
| sous-total | 37,58 | 93,98 |
| marge de 10 % | 3,76 | 9,40 |
| **total** | **41,33** | **103,38** |

Plafond d'arrêt 150 USD inchangé ; haut majoré de 25 % : 129,23, sous 150.

## 2. Part au pire par clé (règle du lanceur v6, inchangée)

| clé (nom de variable) | relais, rôles | estimation (marge comprise) | haut | **part au pire** |
|---|---|---|---|---|
| `RR_ANTHROPIC_API_KEY_MINUIT` | Claude : deux proposeurs, aiguilleur, premier juge | 20,65 | 74,62 | **150,00** |
| `GEMINI_API_KEY`, partagée par Argon et Carbon | Argon : proposeur, second juge ; Carbon : proposeur | 10,97 + 4,86 = **15,83** | 14,66 + 7,05 = **21,71** | **174,00** (150 + 24) |
| `OPENAI_API_KEY` | Astra : proposeur | 4,86 | 7,05 | **24,00** (16 × 1,50) |
| clé de Kimi | — | — | — | non déclarée (R-3279) |

Calcul (devis v6, § 1) : Carbon et Astra, 16 appels × 0,276 × 1,1 = 4,86 ; 16 × 0,400484 × 1,1 = 7,05. Argon : (16 × 0,276 + 160 × 0,0347) × 1,1 = 10,96 (10,97 au devis v6, arrondi des moyennes) ; (16 × 0,400484 + 160 × 0,04326) × 1,1 = 14,66. Minuit : colonne « sans Carbon » du devis v6 (cinq espèces), inchangée. Somme des estimations par clé : 20,65 + 15,83 + 4,86 = 41,34 (41,33 au total, arrondis).

## 3. Ce qui change par rapport au devis v6

- Le total de la composition déclarée est celui de la colonne « cinq espèces » (41,33 / 103,38), non celui de la colonne « avec Carbon » (49,81 / 121,95, six espèces avec Kimi).
- `GEMINI_API_KEY` : estimation 15,83 et haut 21,71 (au lieu de 17,05 et 23,23 avec six espèces) ; part au pire **174** inchangée.
- La clé de Kimi n'est pas confrontée (non déclarée).
- La sonde d'Astra (au plus 0,05 USD, appel réel trivial, signalé) est en sus, sur `OPENAI_API_KEY`, hors du plafond de la course.
