# Devis — T0.6, organisme (ii), dose–réponse et test croisé — v3 (suite ciblée à 67 minutes, bras B borné)

- Écrit le 2026-11-08 par la fille 10 (Claude Sonnet 5.5) sur demande de la session mère (~07:10Z). **Remplace le devis v2 pour la ligne d'engagement** (`docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v2.md`, qui reste tel quel, R12 ; il n'est ni sur `main` ni parmi les ancêtres de ce commit : branche `prep/t06-candidat8-v1`, commit `c99d41e`, empreinte `f6f6195c…`, R-1707). **Aucune dépense engagée par ce document ; aucun plafond changé** (GO-2026-11-02-28 : 200 USD ; GO-2026-11-07-02 : A100 SXM4 ≤ 1,30 USD/h d'abord, sinon H200 NVL ≤ 4,70 USD/h).
- **Ce qui change par rapport au v2** : (1) la durée de la suite d'essais est **mesurée** : « 1878 passed in 4009.60s (1:06:49) » sur l'A100 de 80 Go d'E3 bis (liste v1), contre ≈ 45 minutes estimées ; la liste v2 de la course a 1 914 essais, soit environ 2 % de plus : **67 min × 1,02 ≈ 68,3 min = 1,14 h** ; (2) la borne de l'annexe du bras B est comptée (≈ 5 800 s) ; (3) le reste est inchangé (heures de marche, prix, stockage 0,0417 mesuré, disque arrêté 72 h, téléchargement).

## Postes d'heures de carte (hors calcul du run, ce que le v2 appelait « divers ≈ 1 h »)

| poste | heures | source |
|---|---|---|
| installation (venv, `pip install`) | 0,10 | E3 bis : instance créée 05:47:22Z, suite lancée 05:51:30Z (le clonage, 61 s, et le matériel compris) |
| clonage réduit | 0,02 | E3 bis : `CLONAGE secondes=61` |
| **suite ciblée et figée (liste v2)** | **1,14** | 67 min mesurées × 1,02 (1 914 essais au lieu de 1 878) |
| bras B (nominal) | 0,33 | devis v2 : 20 minutes ; **borne 5 800 s = 1,61 h** (module 2 400 s + verrou 1 500 s + poussée 3 × 600 + 75 s) |
| fin de run, poussées, arrêt | 0,25 | estimation |
| **total « divers »** | **≈ 1,84** (v2 : ≈ 1,0) | |

Heures de marche : génération 3,57 ; évaluation 6,43 ; distillation 0,46 à 6,14 (devis v1/v2, débit de P3, H200 NVL supposée au même débit : **non mesuré**) ; divers 1,84 → **12,3 à 17,9 h** (v2 : 11,5 à 17,1).

## Attendu

| poste | A100 SXM4 (≤ 1,30 USD/h) | H200 NVL (≤ 4,70 USD/h, repli après les 12 recherches) |
|---|---|---|
| calcul | 12,3 h × 1,1083 à 17,9 h × 1,30 = **13,7 à 23,3 USD** | 12,3 h × 3,3617 à 17,9 h × 4,0417 = **41,5 à 72,5 USD** |
| disque arrêté jusqu'au verdict (72 h × 0,0417) | 3,0 | 3,0 |
| téléchargement | 1 à 2 | 1 à 2 |
| **attendu** | **≈ 18 à 28 USD** (v2 : 17 à 27) | **≈ 46 à 78 USD** (v2 : 43 à 74) |

Réserve sur le prix de la A100 : à E3 bis (8 novembre), la moins chère des A100 conformes valait **2,07 USD/h** (borne d'épreuve relevée à 2,10 par Lazar, R-1755) et la liste à ≤ 1,30 était **vide** à 05:34Z. La course garde la borne de 1,30 (GO-2026-11-07-02) : il est donc plausible que la fenêtre de trois heures s'épuise et que la course se joue sur la **H200 NVL**. Sur une A100 à 2,07 USD/h, le même run coûterait 12,3 × 2,07 = 25,5 à 17,9 × 2,07 = 37,1 USD de calcul ; la course ne le permet pas sans nouveau mot de Lazar.

## Pire cas (sous le plafond ; l'arrêt à 200 USD cumulés est la seule garde de dépense)
Hôte deux fois plus lent : 2 × 17,9 = **35,9 h** ; bras B à sa borne : 1,61 h.

| scénario | hypothèses | USD (prix constatés) | USD (à la borne de prix) |
|---|---|---|---|
| P1' hôte A100 deux fois plus lent | (35,9 + 1,61) h × 1,30 ; disque arrêté 72 h à 0,08 = 5,8 ; téléchargement 2 | **≈ 57** | ≈ 57 |
| P2' = P1' + une relance complète sur A100 (erreur de chaîne avant tout épisode d'évaluation) | + 22,2 h × 1,30 = 28,9 ; téléchargement 2 | **≈ 87** | ≈ 87 |
| P3' repli H200 NVL, hôte deux fois plus lent | (35,9 + 1,61) h × 4,0417 (prix constatés) ou × 4,70 (borne) ; disque 5,8 ; téléchargement 2 | **≈ 159** | **≈ 184** |
| P4' erreur de mémoire à la distillation sur A100 (9,1 h × 1,30 = 11,8 ; disque et téléchargement 2,3), puis course complète sur H200 NVL, hôte lent | 11,8 + 2,3 + calcul P3' + 5,8 + 2 | **≈ 173** | **≈ 198** |

**Le devis ne dépasse pas le plafond de 200 USD**, mais la marge est faible : **P4' à la borne de prix de 4,70 USD/h atteint ≈ 198 USD (marge ≈ 2 USD)** ; à 4,04 USD/h (prix constatés) 173 USD. **Ces pires cas supposent la H200 NVL au débit de l'A100 (réserve : non mesuré).** Avec les heures exactes (17,98 h et non 17,9), P4' à la borne vaut ≈ 198,5 USD (marge ≈ 1,5 USD) ; il dépasse 200 USD dès que la H200 NVL met 0,9 % de temps de plus que l'hôte A100 lent de P1' (P3' dès 8,9 %). La seule garde est alors l'arrêt par identifiant à 200 USD cumulés : l'instance serait détruite avant la fin du run, course perdue pour environ 200 USD. Recalcul : `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/scripts/recalcul_devis_v3_v1.py`. Au-delà de **180 USD** cumulés, toute relance reste un nœud de Lazar avant dépense (v1, v2) ; **rien n'est changé ici**.

## Hors devis
Inchangé (devis v2). Les recherches de la fenêtre (12, 0 USD) et la lecture à 0 USD par le code la veille ne coûtent rien. E2 (0,627), E3 (1,465) et E3 bis relèvent de GO-2026-11-06-01 et GO-2026-11-07-08 (8 USD cumulés), pas de ce devis.

## Ligne d'engagement révisée (`registres/depenses.md`, à écrire par la session mère au lancement)
« engagement : T0.6 organisme (ii), dose–réponse et test croisé (GO-2026-11-02-28, plafond 200 USD ; GO-2026-11-07-02) : lanceur `scripts/lancer_t06_v12.sh` (empreinte `<<EMPREINTES_CODE_T06>>`), commit `<<COMMIT_CODE_T06>>` ; préenregistrements de T0.6 et de T0.7 scellés (`<<EMPREINTE_PREREG_T07>>`) ; recherche d'une A100 SXM4 80 Go ≤ 1,30 USD/h toutes les 15 minutes pendant 3 heures (12 recherches, 0 USD), sans A100 conforme repli sur la H200 NVL ≤ 4,70 USD/h, ≥ 140 Go ; dans les deux cas ≥ 16 cœurs effectifs, ≥ 128 000 Mo de mémoire vive, disque ≥ 150 Go, fiabilité ≥ 0,98, CUDA ≥ 13,0, stockage ≤ 0,08 USD/h, téléchargement ≤ 0,05 USD/Go ; suite d'essais figée de 68 minutes ; **attendu ≈ 18 à 28 USD sur A100, ≈ 46 à 78 USD sur H200 NVL ; pire cas ≈ 173 USD aux prix constatés, ≈ 198 USD à la borne de 4,70 USD/h ; arrêt par identifiant à 200 USD cumulés** ; crédit Vast.ai relu à la création (recharge automatique, R-283) ».

## Réserves
Débit de la H200 NVL non mesuré (supposé égal à celui de la A100) ; bras B, amorce v10, lanceur v12 jamais joués sur une instance ; prix de la A100 du 8 novembre (2,07 USD/h) supérieur à la borne de la course ; durée de la suite mesurée sur la liste v1, 2 % de plus supposés pour la liste v2.
