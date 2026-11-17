# Addendum au texte gelé v6 — recourse de la lecture contre ablation (B-7) de la tranche B-α, sur une A100 SXM4 40 Go, aux lots 16 et 64 — v1

Écrit par la fille « Neuron Lens » le 2026-11-17 (≈ 00:40 UTC), sur GO-2026-11-17-03 (« b puis c », R-3046) et GO-2026-11-17-04 (mot
de Lazar transmis par la mère : carte **A100 SXM4 40 Go** sous la ligne GO-2026-11-14-06 ; l'ablation jouée **deux fois sur la même
carte, au lot 16 puis au lot 64** ; la comparaison « A100 lot 16 contre RTX 4090 lot 16 » rapporte l'effet du matériel). Il **ajoute** au
texte gelé `texte-gele-volet-a-et-b-alpha-v6.md` (`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`), qui n'est pas
modifié ; il ne change **aucun seuil, aucune métrique, aucun critère de lecture** de B-2, B-3, B-4 ni B-7. Il déclare deux écarts et fixe
comment lire les deux séries. **Aucune lecture de résultat de la recourse n'a eu lieu** : la course n'est pas partie.

## 1. Pourquoi
La troisième course de B-α (instance 60783204, 2026-11-15, verdict R-2915 « partielle », `lecture-b-alpha/verdict-b-alpha-v1.md`
`ca06acb1…`) a joué l'ablation avec `--ctx-batch 16` au lieu du défaut publié 64 (écart de lot déclaré, R-2901 ;
`devis-b-alpha/memoire-measure-b-alpha-v1.md` `423d7955…`). Le lot 64 ne tient pas dans une RTX 4090 (marge ≈ 0,04 GiB,
`devis-b-alpha/memoire-ablation-lot64-rtx4090-v1.md` `b67f90a9…`). La recourse lève l'écart de lot sur une carte qui le permet.

## 2. Écarts déclarés
1. **Carte** : A100 SXM4 40 Go au lieu d'une RTX 4090 (ligne GO-2026-11-14-06 ; mot de Lazar, GO-2026-11-17-04). Contrôlé sur la
   machine par l'amorce v6 (`CARTE_ATTENDUE=A100-SXM4-40GB` : nom lu par `torch`, sinon code 11 avant toute course). Mémoire : 39 936 Mio
   (≈ 39,0 GiB) ; pic estimé de l'ablation au lot 64 ≈ 23,5 GiB (note `b67f90a9…`, § 2) ; **marge ≈ 15,5 GiB** (estimée, non mesurée).
2. **Second lot** : la chaîne entière est jouée comme à la troisième course (`measure --ctx-batch 16`, puis `score`, grandeurs,
   verdicts, audits R4 requis) ; **ensuite**, sur la même machine et les mêmes tables de la passe complète, les fichiers de `measure` du
   lot 16 sont mis de côté sous un nom distinct (empreinte vérifiée égale à celle de `measure`), et `measure --ctx-batch 64` (le défaut
   publié, l. 379 de la copie) est rejoué, puis `score` (étiquette `lot64`), grandeurs, verdicts et audit « trop beau » s'il est requis
   par la seconde série (lanceur `b_alpha_lancer_v4`, `c598b787…`). `measure` refait pilotage **et** ablation : le pilotage n'a pas de
   lot de contexte (`cond_batch` inchangé), il est donc **le même calcul** aux deux séries.
   Aucun autre paramètre de mesure n'est passé (contrôlé par programme, essai de l'environnement v3).

## 3. Lecture des deux séries (fixée avant la course)
- **Verdict de B-7 de la recourse** : celui de la **seconde série (A100, lot 64)**, par les seuils inchangés du texte gelé v6
  (« Seuil », tableau B ; « Critères de lecture gelés », B-7). C'est la mesure que la recourse vient chercher.
- **Verdicts de B-2, B-3 et de la reproduction** : calculés aux deux séries par le même code des verdicts ; ils sont **rapportés**
  avec le verdict R-2915 de la troisième course, **qui reste le verdict de B-α** sauf mot de Lazar. Tout désaccord de verdict de B-2 ou
  B-3 entre l'A100 et la RTX 4090 est une **divergence non résolue**, portée à la mère, sans arbitrage par la fille ni par le lecteur.
- **Comparaisons rapportées, sans critère** (le lecteur les calcule à partir des grandeurs par pôle et des résumés de `score`) :
  (a) **effet du lot**, même carte : A100 lot 64 contre A100 lot 16, `r_med` d'« ablate win » et d'« ablate pos » par couche et par
  lentille, et l'écart maximal ; (b) **effet du matériel**, même lot : A100 lot 16 contre RTX 4090 lot 16 (troisième course, branche
  `calcul/neuron-lens-b-alpha-v3`, course `20261115-120622-neuron-lens-b-alpha`), les quatre cibles et les quatre lentilles ;
  (c) **cas sain de déterminisme** : les cibles de pilotage (« steer 1x », « steer 4x ») de la série lot 64 contre la série lot 16 sur
  l'A100 ; elles doivent coïncider (même calcul) ; un écart au-delà du bruit numérique du bf16 (|Δ `r_med`| > 0,01 à une couche) est
  **rapporté comme réserve** sur la stabilité de la mesure, et toute comparaison (a) d'un ordre de grandeur égal ou inférieur est lue en
  conséquence.
- Si le verdict de B-7 diffère entre (A100, lot 16) et (A100, lot 64), la lecture dit « B-7 dépend du lot » ; s'il diffère entre (A100,
  lot 16) et (RTX 4090, lot 16), « B-7 dépend du matériel » ; les deux peuvent être vraies. Aucune de ces phrases n'est un verdict de
  reproduction.

## 4. Audits (R4), inchangés dans leur forme
« Trop beau » évalué à chaque série sur ses propres valeurs (graine 1 au même lot que la série) ; « tout négatif » si l'une des séries le
déclenche (B-2 et B-3 « non reproduit ») ; son champ `lecture` reste une **lecture proposée**, aucun verdict après lui sans la décision
de Lazar. Le lecteur neuf lit sur un plan scellé avant toute ouverture des résultats.

## 5. Ajouts à la liste d'arrêt
| condition | action |
|---|---|
| carte lue autre qu'une A100 SXM4 40 Go (code 11 de l'amorce) | destruction immédiate, rapport ; aucune autre carte sans mot de Lazar |
| ablation au lot 64 en échec par mémoire | les résultats du lot 16 sont déjà poussés ; destruction, rapport ; aucune relance sans mot de la mère |
| fichier de `measure` du lot 16 changé avant la bascule, ou cible de la bascule déjà présente | arrêt du lanceur (codé), rapport |
| dépense de cette course à 60 % de son plafond (5,10 USD ; 7,2 USD sur la ligne) | compte rendu à la mère ; à 90 % (7,65 USD ; ≈ 9,75 USD sur la ligne), arrêt dur et destruction vérifiée |

## 6. Ce qui n'est pas couvert (déclaré)
- La marge de mémoire de l'A100 au lot 64 est estimée (§ 2), non mesurée.
- Les deux séries partagent la passe complète, le corpus et la machine : elles ne sont pas deux reproductions indépendantes.
- La recourse ne lève pas l'effet du matériel sur la référence publiée (carte des auteurs non nommée par leurs fichiers : non vérifié
  ici) ; les auteurs notent que les effets faibles dépendent du matériel (cité au devis v2, § 2, niveau citation).
- Aucune contre-lecture de cet addendum n'est faite par la fille ; elle est demandée à la mère (R2).
