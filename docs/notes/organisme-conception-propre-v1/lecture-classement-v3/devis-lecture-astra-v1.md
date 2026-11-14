# Devis — lecture des fiches de la course « conception propre » par Astra (`gpt-6-astra`), outil v3 — v1

Développeur neuf, sous-agent de la session mère, 14 novembre 2026, vers 08:00 UTC (`date -u`). Ligne : GO-2026-11-13-06
(plafond 21 USD). **Aucun appel fait** ; ce devis précède tout appel (R-2662 : devis présenté à Lazar avant tout appel).

## Verdict

**Devis incomplet : le prix d'Astra n'a pas pu être lu** (`prix-astra-v1.md` : pages d'OpenAI hors des domaines de la
session). Les volumes de jetons sont chiffrés ci-dessous ; le coût est donné **en formule des deux prix**, puis illustré au
seul barème que le dépôt connaît, **10 / 50 USD par million, « SUPPOSÉ », jamais lu**. À ce barème, la lecture complète
coûterait **≈ 17,3 USD attendus** (effort `medium`), **au-dessus du reste de la ligne (14,21 USD)** et très au-dessus du
reste de la réserve du lecteur (2,74 USD). Le pire cas des 18 appels serait **≈ 38,5 USD** ; la garde de l'outil l'empêche
(arrêt avant tout appel qui pourrait dépasser le plafond), mais une lecture arrêtée en route est payée sans rien produire
(E2). Deux nœuds pour Lazar : **le prix**, et **la part de la ligne accordée au lecteur**.

## 1. Volumes (43 fiches : 23 réelles admissibles, 20 témoins ; R-2645)

Lots de 5 (`TAILLE_LOT`) : 9 lots par lecture (sept de 5, deux de 4), deux lectures, **18 appels** au plus (fixé d'avance,
`MAX_APPELS`). Corps de chaque appel : préambule fixe (consigne, question, faits, catalogue : 28 466 octets de texte, soit
≈ 8 900 jetons) puis le lot.

Estimations (méthode en § 4) :

| Par appel | Lot de 5 | Lot de 4 |
|---|---|---|
| Octets du corps (estimés) | ≈ 49 900 | ≈ 45 800 |
| Jetons d'entrée **attendus** (3,32 octets par jeton) | ≈ 15 000 | ≈ 13 800 |
| Jetons d'entrée **pire cas** (un jeton par octet, + 1 024) | ≈ 50 900 | ≈ 46 900 |
| Jetons de sortie attendus, effort `low` / `medium` / `high` (SUPPOSÉ) | 7 000 / **17 000** / 32 000 | 5 600 / 13 600 / 25 600 |
| Jetons de sortie **pire cas** (`max_completion_tokens`) | 32 768 | 32 768 |

| Deux lectures, 18 appels | Jetons d'entrée | Jetons de sortie |
|---|---|---|
| Attendu, effort `low` | ≈ 265 700 | ≈ 120 400 |
| **Attendu, effort `medium` (recommandé)** | **≈ 265 700** | **≈ 292 400** |
| Attendu, effort `high` | ≈ 265 700 | ≈ 550 400 (proche du plafond de chaque appel : risque de fin `length`) |
| **Pire cas** | **≈ 900 600** | **589 824** |

## 2. Coût, en formule (PE, PS : prix d'entrée et de sortie en USD par million de jetons)

| | Par appel (lot de 5) | 18 appels |
|---|---|---|
| Attendu, `low` | 0,0150 PE + 0,0070 PS | 0,2657 PE + 0,1204 PS |
| **Attendu, `medium`** | **0,0150 PE + 0,0170 PS** | **0,2657 PE + 0,2924 PS** |
| Attendu, `high` | 0,0150 PE + 0,0320 PS | 0,2657 PE + 0,5504 PS |
| **Pire cas** | **0,0509 PE + 0,0328 PS** | **0,9006 PE + 0,5898 PS** |

Les jetons d'entrée en cache sont comptés au prix d'entrée (borne haute). Le préambule (≈ 8 900 jetons), identique en tête
des 18 corps, pourrait être servi en cache par OpenAI pour 17 appels (≈ 150 700 jetons) : le coût réel serait alors un peu
plus bas ; ce n'est pas compté.

**Illustration au barème prudent du dépôt, 10 / 50 (SUPPOSÉ, non lu : ce n'est pas un prix)** :

| | Par appel | 18 appels |
|---|---|---|
| Attendu, `low` | ≈ 0,50 USD | ≈ 8,68 USD |
| **Attendu, `medium`** | **≈ 1,00 USD** | **≈ 17,28 USD** |
| Attendu, `high` | ≈ 1,75 USD | ≈ 30,18 USD |
| **Pire cas** | **≈ 2,15 USD** | **≈ 38,50 USD** (jamais atteint : la garde arrête avant le plafond) |

## 3. Comparaison avec la ligne GO-2026-11-13-06

- Plafond de la ligne : 21 USD. Déjà compté (`registres/depenses.md`) : course 5,534745 ; Kimi, première tentative
  0,498232 (au pire cas, réel attendu nul) ; Kimi, seconde tentative 0,758110 ; **cumul 6,791087 USD**. **Reste :
  14,208913 USD** (14,707145 si la console confirme que le 429 de Kimi n'a rien coûté). L'outil v3 refuse tout plafond
  au-dessus de 14,20 (`PLAFOND_ABSOLU_USD`).
- Réserve du lecteur prévue par le devis de la course (`devis-v1.md`, ligne « Lecteur de la règle ») : 4,0 USD ; déjà
  comptés 1,256342 ; **reste de la réserve : 2,743658 USD**. Toute lecture par Astra au-dessus de ce reste emprunte à la
  part non dépensée de la course (14,9 prévus, 5,53 dépensés) : **décision de Lazar** (nœud de dépense).
- Pour que la garde laisse passer **les 18 appels** dans le scénario attendu, il faut, au moment du dernier appel,
  dépense des 17 premiers + pire cas du 18e ≤ plafond, soit **0,3019 PE + 0,3089 PS ≤ plafond** (effort `medium`).
  Exemples, en supposant PE = PS / 5 (rapport du barème du dépôt, SUPPOSÉ) : plafond 14,20 → PS ≤ ≈ 38 ; plafond
  2,74 (reste de la réserve du lecteur) → PS ≤ ≈ 7,4. Au barème 10 / 50, il faudrait ≈ 18,5 USD : **la lecture
  complète ne tient pas dans la ligne** ; avec l'effort `low`, ≈ 10,4 USD, elle tiendrait dans le reste de la ligne, pas
  dans la réserve du lecteur.
- Un plafond plus bas que ce seuil n'est **pas** une économie : la lecture s'arrête en route, ce qui a été payé ne produit
  aucune désignation (E2), et la règle n'admet aucune relecture.

## 4. Méthode et hypothèses

- Octets : préambule mesuré par l'outil v3 sur les pièces épinglées ; octets moyens d'une fiche servie, **3 931**, tirés
  des tailles des envois scellés de la v1 (`lecture-g1-v1/envois/`, six messages, 338 066 octets de fiches pour deux
  lectures de 43 fiches ; tailles des fichiers seulement, contenu non ouvert) ; échappements JSON du corps : × 1,0338
  (mesuré sur les mêmes envois). Les lots réels varient autour de cette moyenne (fiches de 1 500 à plus de 3 700 octets).
- Jetons d'entrée attendus : 3,32 octets par jeton, mesuré sur Kimi (25 374 jetons pour 84 252 octets, journal de la
  seconde tentative) ; transposé à Astra (SUPPOSÉ ; un découpeur plus efficace en français donnerait moins de jetons).
- Sortie visible : ≈ 400 jetons par fiche (huit points, citations de 20 à 200 caractères) ; raisonnement par fiche
  (SUPPOSÉ, aucune mesure sur Astra) : 1 000 (`low`), 3 000 (`medium`), 6 000 (`high`). Repère : Kimi, à son effort par
  défaut, a passé plus de 2 180 jetons de raisonnement par fiche sans finir (R-2658).
- Règle de coût de l'outil : (entrée − cache) × PE + cache × prix du cache + sortie × PS + excédent de `total_tokens` au
  prix le plus haut ; `completion_tokens` compte le raisonnement (SUPPOSÉ, à vérifier sur la première réponse ; un
  raisonnement plus grand que la sortie est une incohérence comptée au pire cas).

## 5. Recommandation (confiance 0,6)

1. **Prix lu d'abord** (`prix-astra-v1.md`, deux voies) ; puis recalculer ce devis avec les vrais prix (formules du § 2).
2. **Effort `medium`**, plafond de sortie 32 768, lots de 5 (outil v3, tels quels).
3. **Plafond** : au moins 0,3019 PE + 0,3089 PS (§ 3), au plus 14,20 ; sinon ne pas lancer (ou effort `low`, après
   décision). La part au-delà de 2,74 USD est une décision de Lazar.
4. **Premier appel seul** (`envoyer --envois-max 1`), puis `bilan` : modèle servi exact, sens de `usage` (raisonnement
   compris dans la sortie), jetons réels d'entrée et de sortie ; la mère recalcule le devis avec ces mesures **avant** de
   laisser partir les 17 autres (même journal, même plafond). Coût de ce premier appel : 0,0150 PE + 0,0170 PS attendus,
   0,0509 PE + 0,0328 PS au pire (≈ 1,00 et ≈ 2,15 USD au barème 10 / 50).
5. Défaut sous 48 heures : aucun appel (dépense : nœud, jamais de défaut qui dépense).

Durée : 18 appels l'un après l'autre, de 5 à 15 minutes chacun (SUPPOSÉ ; Kimi : ≈ 17 minutes pour 15 fiches à
32 768 jetons de sortie), soit 1 h 30 à 4 h 30.
