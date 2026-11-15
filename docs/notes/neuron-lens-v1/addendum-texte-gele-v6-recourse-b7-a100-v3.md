# Addendum au texte gelé v6 — recourse de la lecture contre ablation (B-7) de la tranche B-α, sur une A100 SXM4 40 Go, aux lots 16 et 64 — v3

v3 = v2 (`addendum-texte-gele-v6-recourse-b7-a100-v2.md`, `92f16b97…`, archivée, jamais jouée) avec la majeure M1 et les mineures 1, 2 et
4 de la seconde contre-lecture (`contre-lectures/contre-lecture-commande-b-alpha-v7-v1.md`) : **critère de l'audit de B-7 « par le haut »
fixé avant la course** ; changements marqués « (v3) ». Aucun code changé (lanceur v5, amorce v7).

v2 = v1 (`addendum-texte-gele-v6-recourse-b7-a100-v1.md`, `11671826…`, archivée, jamais jouée) corrigée selon la contre-lecture neuve de
la commande v6 (`contre-lectures/contre-lecture-commande-b-alpha-v6-v1.md` : bloquantes B1 et B2, majeures M1 et M2, mineures 8 à 11, 15,
16) ; changements marqués « (v2) ». Lanceur v5 (`b_alpha_lancer_v5.py`), amorce v7.

Écrit par la fille « Neuron Lens » le 2026-11-17 (v1 ≈ 00:40 UTC ; v2 ≈ 01:40 UTC ; v3 ≈ 02:10 UTC), sur GO-2026-11-17-03 (« b puis c », R-3046) et GO-2026-11-17-04 (mot
de Lazar transmis par la mère : carte **A100 SXM4 40 Go** sous la ligne GO-2026-11-14-06 ; l'ablation jouée **deux fois sur la même
carte, au lot 16 puis au lot 64** ; la comparaison « A100 lot 16 contre RTX 4090 lot 16 » rapporte l'effet du matériel). Il **ajoute** au
texte gelé `texte-gele-volet-a-et-b-alpha-v6.md` (`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`), qui n'est pas
modifié ; il ne change **aucun seuil, aucune métrique, aucun critère de lecture** de B-2, B-3, B-4 ni B-7. Il déclare deux écarts et fixe
comment lire les deux séries. **Aucune lecture de résultat de la recourse n'a eu lieu** : la course n'est pas partie.

## 1. Pourquoi
La troisième course de B-α (instance 60783204, 2026-11-15, verdict R-2915 « partielle », `lecture-b-alpha/verdict-b-alpha-v1.md`
`ca06acb1…`) a joué l'ablation avec `--ctx-batch 16` au lieu du défaut publié 64 (écart de lot déclaré, R-2901 ;
`devis-b-alpha/memoire-measure-b-alpha-v1.md` `423d7955…`). Le lot 64 ne tient **très probablement** pas dans une RTX 4090 (marge estimée ≈ 0,04 GiB, non établi ;
`devis-b-alpha/memoire-ablation-lot64-rtx4090-v1.md` `b67f90a9…`). La recourse lève l'écart de lot sur une carte qui le permet.

## 2. Écarts déclarés
1. **Carte** : A100 SXM4 40 Go au lieu d'une RTX 4090 (ligne GO-2026-11-14-06 ; mot de Lazar, GO-2026-11-17-04). Contrôlé sur la
   machine par l'amorce v7 (`CARTE_ATTENDUE=A100-SXM4-40GB` : nom lu par `nvidia-smi` **avant** l'installation, puis par `torch` ; autre
   carte ou nom illisible : code 11 avant toute course ; essayé à blanc sur un cas sain et quatre artefacts (v2)). Mémoire : 39 936 ou
   40 960 Mio selon l'offre (≈ 39,0 à 40,0 GiB) (v2) ; pic estimé de l'ablation au lot 64 ≈ 23,5 GiB (note `b67f90a9…`, § 2) ; **marge ≈ 15,5 GiB** (estimée, non mesurée).
2. **Second lot** : la chaîne entière est jouée comme à la troisième course (`measure --ctx-batch 16`, puis `score`, grandeurs,
   verdicts, audits R4 requis) ; **ensuite**, sur la même machine et les mêmes tables de la passe complète, les fichiers de `measure` du
   lot 16 sont mis de côté sous un nom distinct (empreinte vérifiée égale à celle de `measure`), et `measure --ctx-batch 64` (le défaut
   publié, l. 379 de la copie) est rejoué, puis `score` (étiquette `lot64`), grandeurs, verdicts et audit « trop beau » s'il est requis
   par la seconde série (lanceur `b_alpha_lancer_v5`). `measure` refait pilotage **et** ablation : le pilotage n'a pas de
   lot de contexte (`cond_batch` inchangé), il est donc **le même calcul** aux deux séries.
   Aucun autre paramètre de mesure n'est passé (contrôlé par programme, essai de l'environnement v3).
3. **Changement de code déclaré (v2)** : `essais_ok`, en dur à `True` dans le lanceur v3 de la troisième course (constat du lecteur,
   `constats-a-porter-b-alpha-v1.md`), est lu des résultats scellés de B0, de B.3 et de la fumée : la condition (d) de « chaîne en défaut »
   du texte gelé devient effective ; elle ne l'était pas en troisième course.

## 3. Lecture des deux séries (fixée avant la course)
- **Verdict de B-7 de la recourse** : celui de la **seconde série (A100, lot 64)**, par les seuils inchangés du texte gelé v6
  (« Seuil », tableau B ; « Critères de lecture gelés », B-7). C'est la mesure que la recourse vient chercher. (v2) Il **remplace**, comme
  lecture de B-7 pour un moniteur, celui de la troisième course (RTX 4090, lot 16), qui est rapporté à côté avec son écart de lot ; il
  n'est **pas** un verdict de reproduction. **Aucun verdict de B-7 de la recourse** si la seconde série n'a pas de verdict de mesure
  (« chaîne en défaut ») ou n'est pas jouée (échec par mémoire, arrêt dur, perte de machine) : la série A100 au lot 16 **ne le remplace
  pas** ; la lecture de B-7 reste alors celle de la troisième course, avec son écart de lot, et la recourse est rapportée « sans verdict
  de B-7 ». Une issue « autre » de B-7 au lot 64 se lit couche par couche, comme au texte gelé.
- **Verdicts de B-2, B-3 et de la reproduction** : calculés aux deux séries par le même code des verdicts ; ils sont **rapportés**
  avec le verdict R-2915 de la troisième course, **qui reste le verdict de B-α** sauf mot de Lazar. Tout désaccord de verdict de B-2 ou
  B-3 entre l'A100 et la RTX 4090 est une **divergence non résolue**, portée à la mère, sans arbitrage par la fille ni par le lecteur.
- **Comparaisons rapportées, sans critère** (le lecteur les calcule à partir des grandeurs par pôle et des résumés de `score`) :
  (a) **effet du lot**, même carte : A100 lot 64 contre A100 lot 16, `r_med` d'« ablate win » et d'« ablate pos » par couche et par
  lentille, et l'écart maximal ; (b) **effet du matériel**, même lot : A100 lot 16 contre RTX 4090 lot 16 (troisième course, branche
  `calcul/neuron-lens-b-alpha-v3`, course `20261115-120622-neuron-lens-b-alpha`), les quatre cibles et les quatre lentilles ;
  (c) **cas sain de déterminisme** : les cibles de pilotage (« steer 1x », « steer 4x ») de la série lot 64 contre la série lot 16 sur
  l'A100 ; elles doivent coïncider (même calcul) ; l'écart maximal |Δ `r_med`| est rapporté ; au-delà de 0,01 (seuil **choisi ici**, non
  sourcé : un dixième du plus petit écart de seuil du tableau B, 0,40 contre 0,30) il est rapporté comme **réserve** sur la stabilité de la
  mesure, et les écarts (a) de même ordre ou moindres sont rapportés « dans le bruit de la mesure » ; ni cette réserve ni (a) ni (b)
  ne changent un verdict (v2).
- Si le verdict de B-7 diffère entre (A100, lot 16) et (A100, lot 64), la lecture dit « B-7 dépend du lot » ; s'il diffère entre (A100,
  lot 16) et (RTX 4090, lot 16), « B-7 dépend du matériel » ; les deux peuvent être vraies. Aucune de ces phrases n'est un verdict de
  reproduction.

## 4. Audits (R4), inchangés dans leur forme
(v2) **B-7 « non reproduit » par le haut** (texte gelé : « audit R4 avant toute lecture ») : le texte gelé n'écrit pas sa procédure ; la
seule procédure R4 écrite pour B-α est celle de « trop beau » (témoin bien apparié, pilotage de norme non nulle, `measure` à la graine
1) ; **elle est jouée** dans la même série, sur la même machine (lanceur v5 ; la v3 de la troisième course et la v4 perdaient ce motif) ;
(v3) **Critère, fixé avant la course** : l'audit de B-7 « par le haut » d'une série **tient** si, ensemble, (1) le témoin est bien apparié
(`temoin_bien_apparie` vrai dans le résultat de l'audit), (2) le pilotage a une norme non nulle (`pilotage_norme_non_nulle` > 0 pour
« steer 1x » et « steer 4x »), (3) le **verdict de B-7 recalculé à la graine 1** de la même série et au même lot — par le code des
verdicts (`verdicts_b_alpha_v3`, seuils inchangés), sur le résumé de `score` de l'audit (`causal_lens_seed1_…` ou `causal_lens_seed1-lot64_…`,
versé) et les n des grandeurs de la graine 1 (versées) — est lui aussi « non reproduit » **par le haut**. Le calcul (3) est fait par le
lecteur neuf, sans code ni location en plus. **S'il tient** : B-7 de la série est rapporté « non reproduit par le haut, confirmé à la
graine 1 » : lecture valable en contexte plus tôt que publié (texte gelé, critères de B-7). **S'il ne tient pas** : « non reproduit par le
haut, non confirmé à la graine 1 » : **aucune** lecture « par le haut », B-7 de la série est rapporté sans lecture pour un moniteur. Ni
l'un ni l'autre n'est un verdict de reproduction. Le lanceur s'arrête sur tout motif d'audit qu'il ne connaît pas (garde, R5 ; en marche
normale, les trois motifs du code des verdicts sont connus).
« Trop beau » évalué à chaque série sur ses propres valeurs (graine 1 au même lot que la série) ; son déclencheur lit le pilotage, le même
calcul aux deux séries : s'il est requis, il l'est en principe aux deux ; (v3) le motif B-7 « par le haut », lui, lit l'ablation, qui
diffère entre les lots : l'audit peut donc être requis à une seule série ; **un ou deux** audits « trop beau » au total ; « tout négatif » si l'une des séries le
déclenche (B-2 et B-3 « non reproduit ») ; son champ `lecture` reste une **lecture proposée**, aucun verdict après lui sans la décision
de Lazar. Le lecteur neuf lit sur un plan scellé avant toute ouverture des résultats.

## 5. Ajouts à la liste d'arrêt
| condition | action |
|---|---|
| carte lue autre qu'une A100 SXM4 40 Go (code 11 de l'amorce) | destruction immédiate, rapport ; aucune autre carte sans mot de Lazar |
| ablation au lot 64 en échec par mémoire | les résultats du lot 16 sont déjà poussés ; destruction, rapport ; aucune relance sans mot de la mère |
| fichier de `measure` du lot 16 changé avant la bascule, ou cible de la bascule déjà présente | arrêt du lanceur (codé), rapport |
| (v2) toute autre série de B-7 (autre carte, autre lot, autre graine, nouvelle location), **quel que soit le résultat** | interdite sans décision de Lazar (R3) |
| (v2) perte de la machine, arrêt dur ou minuterie avant la fin de la seconde série | rien n'est relancé ; rapport « sans verdict de B-7 » (§ 3) ; mot de la mère |
| dépense de cette course à 60 % de son plafond (5,10 USD ; 7,2 USD sur la ligne) | compte rendu à la mère ; à 90 % (7,65 USD ; ≈ 9,75 USD sur la ligne), arrêt dur et destruction vérifiée |

## 6. Ce qui n'est pas couvert (déclaré)
- La marge de mémoire de l'A100 au lot 64 est estimée (§ 2), non mesurée.
- Les deux séries partagent la passe complète, le corpus et la machine : elles ne sont pas deux reproductions indépendantes.
- La recourse ne lève pas l'effet du matériel sur la référence publiée (carte des auteurs non nommée par leurs fichiers : non vérifié
  ici) ; les auteurs notent que les effets faibles dépendent du matériel (cité au devis v2, § 2, niveau citation).
- (v2) La chaîne n'a jamais tourné sur l'architecture de l'A100 (bf16 pris en charge ; versions épinglées inchangées) : non essayé.
- (v2) Les fichiers bruts de `measure` (`-causal.pt`, `-causal-lot16.pt`, ≈ 2 GiB chacun pour Llama, `devis-b-alpha/memoire-measure-b-alpha-v1.md` § 3 ; v3) dépassent la limite de fichier de l'hébergeur
  de code : ils restent sur l'instance et sont **perdus à la destruction** ; seuls leurs empreintes, les résumés de `score` et les
  grandeurs par pôle sont versés.
- La v1 a été contre-lue avec la commande v6, la v2 avec la commande v7 (rapports cités en tête) ; les retouches de la v3 sont soumises
  au même contre-lecteur.
