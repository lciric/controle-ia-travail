# Devis — course d'auto-conception de l'organisme d'idéation — v2b : composition déclarée (Astra et Carbon, sans Kimi)

- Auteur : session du compte organisme (modèle I), 18 novembre 2026. Version 2b (R12 ; le devis v2, `devis-course-auto-conception-v2.md`, `fa39c545f71bb614cdc317c420c5b4c4d3fd47ed8435d0adace510d3a6233d85`, reste en place). **Rien n'a été lancé.**
- Ce qui change : la composition déclarée, sur le mot du directeur (18 novembre, vers 10:50Z) — **deux espèces Claude + Argon + Astra + Carbon** (Kimi non déclaré, R-3273). Prix, hypothèses, plafond d'arrêt (**90 USD**) et épreuve des témoins (**5 USD**) inchangés.
- Chiffres lus dans la sortie du calcul du devis v2, sans nouveau calcul de jetons : `calcul-devis-course-auto-conception-v2.json` (`91f5cf8f147689eb2fa9ff9db8b6e3b91b15496174e03f07a66d691676c2db2b`), clé `totaux["prop-argon+prop-astra+prop-carbon+prop-claude-1+prop-claude-2"]` et `especes` ; parts par clé sommées ici à la main.

## 1. Total de la composition déclarée

| | appels (proposeurs / aiguilleur / juges) | proposeurs | aiguilleur | juges | **total** |
|---|---|---|---|---|---|
| estimation | 55 / 110 / 220 | 28,32 | 3,41 | 7,89 | **39,62 USD** |
| haut | 55 / 220 / 440 | 53,31 | 20,46 | 47,32 | **121,10 USD** |

C'est la ligne « + Astra + Carbon » du devis v2 (§ 2), qui devient la composition déclarée. Au haut, 121,10 > 90 : le plafond d'arrêt coupe (une étape protégée qui ne tient pas sous son plafond n'est pas lancée : « non mesurée (budget) », issue rapportée) — inchangé, dit au devis v2.

## 2. Part par clé

| relais (clé) | estimation | haut | part au pire (règle du lanceur v2) |
|---|---|---|---|
| Claude (`RR_ANTHROPIC_API_KEY_RIGAUD`) : deux proposeurs, aiguilleur, juge 1 | 2,7901 + 6,9753 + 3,41 + 110 × 0,037 = **17,25 USD** | 5,2526 + 13,1316 + 20,46 + 220 × 0,037 × 3 = **63,26 USD** | 90 USD |
| Argon : proposeur, juge 2 | 5,7895 + 110 × 0,0347 = **9,61 USD** | 10,8992 + 220 × 0,0347 × 3 = **33,80 USD** | 90 USD |
| Astra (`OPENAI_API_KEY`) | 6,98 USD | 13,13 USD | 33 USD (11 × 3 USD de plafond de session ; relais de course à 34) |
| Carbon (`«CLE_CARBON»`) | 5,79 USD | 10,90 USD | 33 USD |

Somme : 17,25 + 9,61 + 6,98 + 5,79 = 39,62 (estimation) ; 63,26 + 33,80 + 13,13 + 10,90 = 121,10 (haut).

**Clé Claude, reste net** : inchangé (devis v2, § 4) : ≈ 104 USD avant l'épreuve des témoins, au-dessus de la part au pire de 90 ; l'estimation de la clé passe de 14,25 (composition par défaut) à 17,25.

**Si Carbon emploie la même variable de clé qu'Argon** : la clé porte Argon et Carbon (estimation 15,40, haut 44,70). Le lanceur v2 calcule la part au pire **par fournisseur** (`parts_au_pire`, l. 1178-1197) et ne la somme pas par nom de clé (le lanceur v6 de l'affinage le fait) ; une clé illisible sous la dispense de la mère n'est confrontée à aucune part. La somme des parts (90 + 33 = 123 USD) est donc écrite ici pour la mère seulement ; elle n'est gardée par aucun programme.

## 3. Relais Gemini et épreuve

Argon : au pire 11 + 11 × 5 × 4 = **231 appels** — `--max-appels 280` (inchangé). Carbon : 11 lots au pire, `--max-lots 15`. Épreuve des témoins inchangée (estimation 1,13 USD, haut 3,39, plafond 5).

## 4. Total demandé

Course 90 USD + épreuve 5 USD = **95 USD au plus** (inchangé) ; **attendu ≈ 40,75 USD** (39,62 + 1,13), au lieu de ≈ 23,5 pour la composition par défaut. La sonde d'Astra (au plus 0,05 USD, signalée) est en sus, sur `OPENAI_API_KEY`.
