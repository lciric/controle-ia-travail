# Verdict du lecteur neuf — essai d'invariance au lot de l'ablation de `measure` (audit R4) — v1

**Issue : « identité 16/64 établie, invariance non établie ».** Les cinq témoins tiennent aux trois couches ; les 64 tâches du lot 64
sont identiques au bit près au lot 16 aux couches 0, 15 et 26 ; le lot 1 (0 sur 64) et le lot 7 (56 sur 64) diffèrent. Mon calcul et la
lecture par programme concordent sur l'issue et sur chaque témoin.

## Pièces et empreintes
| pièce | chemin | sha256 |
|---|---|---|
| préenregistrement (consigne) | `docs/notes/neuron-lens-v1/audit-invariance-lot/preenregistrement-audit-invariance-lot-v3.md` | `bbf2c95b7a471c46218b349e05739c3affd57d6cdca4ce71c4abbb0e819205ad` |
| sa contre-lecture | `docs/notes/neuron-lens-v1/audit-invariance-lot/contre-lecture-audit-invariance-lot-v3.md` | `a27f1d04603d505583f56b9af08bac05118c3f38d7d5fdc2a9586c76ab8c5687` (vérifiée, OK) |
| ma déclaration (2026-11-17T10:35:31Z, avant toute lecture de résultat) | `docs/notes/neuron-lens-v1/audit-invariance-lot/declaration-lecteur-audit-invariance-v1.md` | `76e7b41a1a898c621ef87ec5fb36f4b7c74d2a6b3bdf0b07ebaf268837d8283c` |
| mon script | `docs/notes/neuron-lens-v1/audit-invariance-lot/calcul_issue_audit_invariance_v1.py` | `2766c6d8fcd395d2937489510262812d1c534bbd78686801613bd22acfd9be86` |
| mon résultat | `docs/notes/neuron-lens-v1/audit-invariance-lot/calcul-issue-audit-invariance-v1.json` | `1a7012fb8458ba6da49c58b72de8c2e88b8ebc2ffa03e8c87b91e3df5db95dc7` |
| manifeste | `runs/20261117-095647-neuron-lens-audit-invariance/manifeste.json` | `a42a8c9c87fadab7f6f67677136645e34e14a3697852fef5835afa7a59350fc6` |
| détail brut | `diag/20261117-095647-neuron-lens-audit-invariance/audit-invariance-lot-v3.json` | `d97fbd77436ccfe4c40e4006db271fcb9c61858f3caa8726d1b7d86f52e033d9` |
| résultat de l'étape | `diag/20261117-095647-neuron-lens-audit-invariance/b-alpha-audit-invariance.json` | `d2162e8b2beba012da6f740b0fc253a9e9e31dc6d949b88b229c1b93174b9741` |

Identifiant de course lu dans `run-id-audit-invariance-v1.txt` : `20261117-095647-neuron-lens-audit-invariance`.

## 1. Empreintes
- Manifeste : compagnon OK ; `manifeste_sha256` du résultat de l'étape = empreinte du manifeste.
- `diag/<run>/` : les cinq JSON de premier niveau et les quatre fichiers de `references/` se vérifient par leurs compagnons (OK).
  `journaux/telecharger-tokeniseur.log` n'a pas de compagnon (`bc26ed57…`, suivi par git au commit `80a07358`) : réserve 2.
- Préenregistrement versé : `resultat.preenregistrement` = chemin v3 et `bbf2c95b…205ad`, identique au § 0. Le même fichier, au commit
  `37b2157c` de la machine (manifeste), a la même empreinte ; le module `audit_invariance_lot_v3.py` y a l'empreinte `4b14404c…` du
  module du commit `80a07358`.
- Carte relevée : « NVIDIA A100-SXM4-40GB » ; la condition d'arrêt du § 4 n'est pas déclenchée. Graine : `SeedSequence(20261117)`,
  versée au résultat et au détail (`entropie`).

## 2. Mon calcul (script autonome, bibliothèque standard, sans le module de l'essai)
| couche | C1 formes 16 ≠ 64 | C2 tâche 0 change, 63/63 autres identiques | C3 rejeu lot 16 | C3b rejeu lot 64 | C4 non nulles (≥ 58/64) |
|---|---|---|---|---|---|
| 0 | oui | oui | 64/64 | 64/64 | 64/64 |
| 15 | oui | oui | 64/64 | 64/64 | 64/64 |
| 26 | oui | oui | 64/64 | 64/64 | 64/64 |

Tâches identiques au lot 16 (au bit près ; en demi-précision ; écart maximal en valeur absolue) :
| couche | lot 64 | lot 1 | lot 7 |
|---|---|---|---|
| 0 | 64/64 ; 64/64 ; 0 | 0/64 ; 0/64 ; 0,7293 | 56/64 ; 56/64 ; 0,3235 |
| 15 | 64/64 ; 64/64 ; 0 | 0/64 ; 0/64 ; 0,5491 | 56/64 ; 56/64 ; 0,3054 |
| 26 | 64/64 ; 64/64 ; 0 | 0/64 ; 0/64 ; 0,3497 | 56/64 ; 56/64 ; 0,3480 |

Contrôles non décisifs de mon script : les formes de passes versées coïncident, à chaque lot et à chaque couche, avec celles qu'on attend
des longueurs versées (tâches dans l'ordre, 2 × paquet lignes, largeur = plus longue séquence du paquet) : lot 16, 4 passes (32 × 240 à
253) ; lot 64, une passe 128 × 253 ; lot 7, 10 passes ; lot 1, 58 formes distinctes. « Identique » ⇔ « écart nul » partout. Les 64
empreintes du lot 16 sont distinctes à chaque couche. Aucune anomalie (64 tâches, lots 16, 64, 1, 7, longueurs dans [24, 256]).

Application du § 4 : témoins tenus ; lot 64 identique aux trois couches ; lots 1 et 7 différents → **« identité 16/64 établie, invariance
non établie »**.

## 3. Comparaison à la lecture par programme et au code
- `lecture_par_programme` : C1 à C4 vrais, `lot64_identique_au_lot16` vrai, `lots_1_et_7_identiques` faux, même issue. **Aucun
  désaccord.**
- Code (`lire_issue`, l. 160-183) : même règle que le § 4 ; seuil C4 `≥ 0,9 × 64` (soit 58), identique au mien. Deux notes sans effet
  ici : le champ `lots_1_et_7_identiques` vaut en fait « lot 64 **et** lots 1 et 7 identiques » (nom plus étroit que son contenu) ; C2 et C4
  sont lus au seul lot 16, ce que le § 3 permet.

## 4. Rapporté sans critère
- Écarts maximaux par lot et par couche : tableau du § 2 (lot 64 : 0 partout ; lot 1 : 0,73 / 0,55 / 0,35 ; lot 7 : 0,32 / 0,31 / 0,35).
- Demi-précision : mêmes comptes qu'au bit près, à chaque lot et à chaque couche (l'arrondi ne rattrape aucune tâche).
- Produit matriciel bf16 (2 lignes contre 128 lignes, 2 premières lignes) : **non identique**, écart maximal 1,0.
- Versions et attention : torch 2.14.1+cu130, CUDA 13.0, cuDNN 92400, transformers 5.18.0, attention `sdpa` ; épinglage du
  préenregistrement respecté (torch 2.14.1, transformers 5.18.0). Durée de l'étape 103,4 s (échéance 0,3 h attendue, 1,0 h au pire ;
  pas de dépassement).
- Carte : NVIDIA A100-SXM4-40GB.

## 5. Ce que l'issue entraîne pour la recourse de B-7 (§ 4)
Explication (A) soutenue **pour les lots 16 et 64 seulement** : sur cette carte et ces versions, ce calcul rend la même chose au bit près
aux lots 16 et 64, donc l'identité observée dans la recourse est **attendue** ; l'invariance au lot **n'est pas générale** (lots 1 et 7
différents) ; rapporté. La clause « série au lot 64 suspecte » ne s'applique qu'à l'issue « réfutée » : elle ne joue pas. Le § 6 reste :
l'essai ne prouve pas que la course a fait exactement ce calcul (vraies tâches, code voisin), et la carte n'est pas forcément la machine
de la course. Remarque du lecteur, hors § 4 : les séries 16 et 64 de la recourse ne sont donc pas deux mesures indépendantes, mais une
même mesure vue deux fois.

## Réserves
1. Le détail ne verse les empreintes par tâche que pour le lot 16 ; lots 64, 1, 7 et rejeux sont versés en comptes. Mon calcul est
   indépendant pour la règle de lecture, non pour la comparaison des tenseurs, faite sur la machine. On ne peut pas dire quelles 8 tâches du
   lot 7 diffèrent (par exemple la dernière passe de 2 lignes, de la forme du lot 1, ou non).
2. `journaux/telecharger-tokeniseur.log` sans empreinte compagnon (R6) ; aucun journal de l'étape `audit-invariance` n'est versé sous `diag/`.
3. Le manifeste est celui de B-α (préenregistrement `texte-gele-volet-a-et-b-alpha-v6.md`, graines 20261114), comme le § 3 le déclare ;
   la graine de l'essai n'est que dans le résultat de l'étape et le détail.
4. R4, symétrie : l'identité 16/64 est propre (écart nul, 3 × 64 tâches), mais l'instrument voit des écarts ailleurs (lots 1 et 7, C2,
   produit bf16) ; je n'y vois pas de propreté suspecte. L'ampleur des écarts au lot 1 (jusqu'à 0,73 en différence de log-softmax) est
   rapportée sans critère.
