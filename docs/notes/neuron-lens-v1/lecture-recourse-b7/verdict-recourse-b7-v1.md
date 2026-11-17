# Verdict de la recourse de la lecture contre ablation (B-7) de B-α, A100, lots 16 et 64 — v1

Lecteur neuf (sous-agent ; n'a écrit ni le texte gelé, ni l'addendum, ni le code, ni la commande, ni le plan de lecture).
Course `20261117-015632-neuron-lens-b-alpha` ; branche `prep/neuron-lens-v1`, commit `9fa259f0`. Écrit le 2026-11-17 après 09:02 UTC.
Expérience hors du programme : rien ici n'ouvre ni ne ferme une porte.

| pièce | chemin | empreinte |
|---|---|---|
| plan de lecture scellé (consigne) | `docs/notes/neuron-lens-v1/lecture-recourse-b7/plan-de-lecture-recourse-b7-v3.md` | `64e96bc302b6…` |
| sa contre-lecture | `…/lecture-recourse-b7/contre-lecture-plan-de-lecture-recourse-b7-v3.md` | `841c2992ecff…` |
| ma déclaration (étape 0, scellée 08:55:45Z, avant tout fichier de `diag/`) | `…/lecture-recourse-b7/declaration-lecteur-recourse-b7-v1.md` | `0d7c78471d30…` |
| mon calcul (scellé à 09:01Z, avant l'étape 5) | `…/lecture-recourse-b7/calcul_verdicts_recourse_b7_v1.py` | `58254aed12f1…` |
| sa sortie (étapes 4 et 6) | `…/lecture-recourse-b7/calcul-verdicts-recourse-b7-v1.json` | `2560e5978e7c…` |
| texte gelé v6 ; addendum v3 ; journal v5 ; contre-lecture de la commande v8 | `docs/notes/neuron-lens-v1/…` | `34b882437a9d…` ; `5f05f5bc5cae…` ; `3047ff1c1f73…` ; `a6b7a9ccf25e…` |
| manifeste | `runs/20261117-015632-neuron-lens-b-alpha/manifeste.json` | `69917256f534…` |
| résumés de `score`, lot 16 et lot 64 | `diag/20261117-015632-…/causal_lens_llama-3.1-8b-instruct.json`, `…/causal_lens_lot64_llama-3.1-8b-instruct.json` | **tous deux** `bd57d519a24e…` |
| grandeurs par pôle, lot 16 et lot 64 | `…/grandeurs-par-pole-b-alpha-v1.json`, `…-lot64-v1.json` | **toutes deux** `6cce8f72f27e…` |
| n et écartés | `…/b-alpha-grandeurs.json` ; `…/b-alpha-grandeurs-lot64.json` | `6465f3dadc01…` ; `1a36d8a8bae2…` |
| verdict R-2915 (troisième course, RTX 4090) | `origin/main:docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` | `ca06acb1550c…` |

Empreintes (étape 1) : les 29 fichiers à compagnon de `diag/20261117-015632-…` et le manifeste sont conformes ; les 10 journaux
`journaux/*.log` n'ont pas de compagnon (empreintes calculées dans ma sortie de travail ; `measure.log` `379d5425…`, `measure-lot64.log`
`1d8b0b02…`). Troisième course : 21 compagnons conformes.

## 1. Verdict en trois lignes

1. **B-7 de la recourse (A100, lot 64) : « autre », couche par couche** — lecture basse (< 0,25) aux couches 0 à 14, **0,3117 à la couche 15** (la seule condition manquée), ≥ 0,81 aux couches 26 à 29 ; ni « par le haut », ni « par le bas ». Il remplace, pour un moniteur, la lecture de la RTX 4090 (lot 16, « autre », couche 15 à 0,3097), même issue.
2. **B-2 « autre », B-3 « reproduit », reproduction « partiel », aux deux lots** ; mêmes verdicts que R-2915, **qui reste le verdict de B-α** ; aucune chaîne en défaut, aucun audit déclenché ni joué, aucun désaccord de fond avec le code de la course.
3. **Réserve majeure (trop propre)** : la série au lot 64 est **identique octet pour octet** à celle du lot 16 (même `-causal.pt` `7c1b5de9…`, même résumé, mêmes grandeurs) : l'effet du lot mesuré est exactement nul et le cas sain (c) est dégénéré ; je ne sais pas dire pourquoi, je le signale sans l'arbitrer.

## 2. Chaînes en défaut et audits, par série

Les deux séries ayant des entrées identiques, tout ce qui suit vaut pour le lot 16 **et** le lot 64 (vérifié séparément par le calcul).

| condition | constat | marge |
|---|---|---|
| (a) \|`control_med`\| > 0,10, couches 0 à 27, 4 cibles × 4 lentilles | aucune | max 0,0700 (« steer 4x », `J`, couche 11) |
| (b) plus de 32 pôles écartés pour **effet nul**, « steer 1x », 0 à 27 | aucune | motif séparé par la course (« effet nul », « sans contexte ») : 0 partout, toutes cibles |
| (c) logits « steer 1x » ≥ 0,80, `npR` ≥ 0,85, couches 28 à 30 | tenus | logits 0,8446 ; 0,8642 ; 0,8974 — `npR` 0,9672 ; 0,9719 ; 0,9798 |
| (d) correctifs (1) et (2), fumée | tenus | 7 passés, 13 passés, aucun sauté (`-rs`) ; graine 8, crochets 4 ; fumée code 0 (« smoke test done ») |
| (e) repli sur les logits, 0 à 23 ; identité à B0 | aucun | plus petit écart 0,0327 (`npJpp`, couche 1) ; 31 couches `0..30` pour `J`, `npJpp`, `npR`, défauts (e) vides |
| B.3 rejoué ; partie 2 | 35 passés, deux fois ; « Écarts : aucun » | — |

Étape 3 : `b-alpha-measure.json` lot 16, `b-alpha-measure-lot64.json` lot 64 ; la bascule a déplacé un fichier d'empreinte égale à celle de
`measure` (`7c1b5de9…`) : conforme.

**Audits** (étape 3 bis, constat par fichiers, avant le calcul) : aucun fichier d'audit présent (ni `b-alpha-audit-trop-beau*.json`, ni
`b-alpha-audit-tout-negatif.json`, ni résumés ou grandeurs de la graine 1) : **aucun audit joué**. Mon calcul n'en déclenche aucun, à
aucune série : « trop beau » non (`r_med` max couches 0 à 7 : 0,3771 ; aucun `control_med` écrit 0 aux couches 0 à 27) ; « tout
négatif » non ; « B-7 par le haut » non. La course écrit `audits_requis = []`, `motifs_audit = []`, `audit_b7_par_le_haut = false` aux
deux lots : **aucune divergence**. Le critère de l'audit de B-7 « par le haut » est sans objet.

## 3. B-2, B-3, B-4 et B-7, par série (lot 16 = lot 64)

Toutes les couches sont lisibles (n = 64 partout, 4 cibles ; n écrit par la course, non recalculable : `-causal.pt` non versé ; je
retrouve 64 pôles « retenus » par couche dans les grandeurs par pôle). Aucune bande partielle.

- **B-2 : « autre »** (la course écrit « partiel »). `r_med` tient à chaque couche (le plus juste : couche 8, 0,4089 pour 0,40) ;
  **`pass` manque aux couches 8 (0,7500) et 10 (0,8750)** pour 0,90 ; témoin : aucune couche hors de ±0,05 (toutes couches et couches
  lisibles : même lecture). « Non reproduit » : non (aucun `pass` < 0,50 en 16 à 27, aucun `r_med` < 0,30 en 16 à 23).
- **B-3 : « reproduit »** : écart ≥ 0,20 aux 12 couches 4 à 15 (de 0,2091 à la couche 4, marge 0,0091, à 0,3748 à la couche 12) ; aucun
  écart ≤ 0. Différence arrondie et différence flottante brute donnent le même côté.
- **B-4** (non décisive), couches 4 à 23 : `npR` − `J` de −0,0851 (couche 12) à +0,0068 (couche 4), positif à 1 couche sur 20 ;
  `npR` − `npJpp` de +0,0325 (couche 20) à +0,1513 (couche 8), positif aux 20. Mes 40 valeurs égalent celles de la course.
- **B-7 : « autre », couche par couche** (la course écrit « partiel ») — « ablate win », `npR` :

| couche | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `r_med` | −0,0029 | 0,0248 | 0,0065 | 0,0531 | 0,0763 | 0,0439 | 0,0670 | 0,0821 | 0,0504 | 0,0664 | 0,0281 | 0,0994 | 0,1108 | 0,1701 | 0,1861 | **0,3117** |

| couche | 26 | 27 | 28 | 29 |
|---|---|---|---|---|
| `r_med` | 0,8126 | 0,8423 | 0,8108 | 0,8468 |

  « Reproduit » : non, la seule condition manquée est « < 0,25 » à la couche 15. « Par le haut » : non (aucune couche 8 à 15 ≥ 0,40 ;
  max 0,3117). « Par le bas » : non (aucune couche 26 à 29 < 0,30). Couches 16 à 25, hors bandes : 0,2984 à 0,7759.
- **Verdict de reproduction de chaque série : « partiel »**, mesure par mesure (B-2 « autre », B-3 « reproduit »).

## 4. Verdict de B-7 de la recourse

**« Autre », couche par couche** (série au lot 64, sans chaîne en défaut, sans motif « par le haut ») : une activation isolée est mal
lue avant la couche 15 (`r_med` ≤ 0,1861 aux couches 0 à 14), la lecture monte à 0,31 à la couche 15, passe 0,50 vers la couche 19
(0,5072) et vaut 0,81 à 0,85 aux couches 26 à 29. Il remplace, comme lecture de B-7 pour un moniteur, celle de la troisième course
(RTX 4090, lot 16, R-2915 : « autre », couche 15 à 0,3097, couches 26 à 29 à 0,8053–0,8450), rapportée à côté avec son écart de lot.
Ce n'est pas un verdict de reproduction. Voir la réserve du § 6.1 : la série au lot 64 ne diffère pas, au bit près, de celle du lot 16.

Phrases du § 4 du plan : B-7 de l'A100 lot 16 (« autre ») = A100 lot 64 (« autre ») → **pas de « B-7 dépend du lot »** ; A100 lot 16
(« autre ») = RTX 4090 lot 16 (« autre », même couche manquée) → **pas de « B-7 dépend du matériel »**.

B-2 et B-3 : A100 (deux lots) et RTX 4090 donnent les mêmes verdicts (B-2 « autre », B-3 « reproduit », reproduction « partiel ») :
**aucune divergence** à porter. Les conditions manquées de B-2 diffèrent pourtant d'une carte à l'autre : la RTX 4090 manque aussi
`r_med` à la couche 8 (0,3883), l'A100 l'y tient (0,4089) ; `pass` manque aux couches 8 et 10 sur les deux. Mon recalcul de la
troisième course retrouve les verdicts de R-2915.

## 5. Comparaisons, sans critère (Δ en valeurs écrites, arrondies à 4 décimales)

- **(a) effet du lot** (lot 64 − lot 16, « ablate win » et « ablate pos », couches 0 à 30, 4 lentilles) : **Δ = 0 à chaque cellule** ;
  maximum 0 pour « ablate win » et 0 pour « ablate pos ».
- **(c) cas sain de déterminisme** (« steer 1x » et « steer 4x », lot 64 − lot 16) : **max |Δ| = 0** ; pas de réserve de stabilité
  au sens du plan (seuil 0,01). Par la règle du plan, le maximum de (a) par cible (0 et 0) est ≤ au maximum de (c) (0) : (a) est
  « dans le bruit de la mesure ». Ce constat est dégénéré (tout est nul) : § 6.1.
- **(b) effet du matériel** (A100 lot 16 − RTX 4090 lot 16, couches 0 à 30, 4 lentilles), écart maximal par cible :
  « steer 1x » 0,0213 (`npJpp`, couche 1) ; « steer 4x » 0,0114 (`npR`, couche 2) ; « ablate pos » 0,0226 (`npR`, couche 2) ;
  « ablate win » 0,0296 (`J`, couche 6 ; `npR` : 0,0294). Écarts cellule par cellule dans ma sortie (clé
  `comparaison_b_a100_lot16_moins_rtx4090_lot16`). Ambiguïté 7 : les empreintes des quatre tranches du corpus (partie 2) sont **égales**
  entre les deux courses ; (b) ne mêle donc pas le corpus au matériel (les deux courses partagent aussi le code, non vérifié ligne à ligne par moi).

## 6. Désaccords avec le code de la course, ambiguïtés, ce qui est trop propre

**Trop propre (signalé, sans verdict)**
1. **Lot 64 identique au lot 16, octet pour octet.** `measure --ctx-batch 64` (ligne de commande lue dans `journaux/measure-lot64.log`)
   a écrit un `-causal.pt` d'empreinte `7c1b5de9…`, celle du lot 16 ; d'où des résumés de `score` (`bd57d519…`) et des grandeurs par
   pôle (`6cce8f72…`) identiques, et des journaux écrits par `score` à côté des résumés (`causal_lens_*.log`) identiques (`f3b60958…`). Durées de l'ablation : 682 s (lot 16) et 687 s
   (lot 64). La copie du code publié lit bien `--ctx-batch` dans la boucle d'ablation (l. 216-217 de
   `scripts-checks-causal_lens.py.txt`) : le lot y change le nombre de lignes par passe et la longueur de remplissage. Dans le même temps,
   la carte change `r_med` jusqu'à 0,03 (comparaison (b)). Deux explications possibles, **non arbitrées** et que je ne peux pas
   départager (fichiers bruts perdus avec l'instance) : calcul invariant au lot, au bit près, sur cette carte et ces versions ; ou option
   sans effet dans le code qui a tourné. Conséquence : la recourse ne fournit pas une mesure de B-7 au lot 64 distincte de celle au lot 16
   de la même carte ; (a) et (c) ne mesurent rien qui se distingue.
2. **n constant à 64** (32 couches × 4 cibles × 2 séries), aucun pôle écarté — comme en troisième course ; non contrôlable sans `-causal.pt`.
3. Marges proches des seuils (aucune collée) : B-2 `r_med` couche 8 à +0,0089 ; B-3 couche 4 à +0,0091 ; B-2 `pass` couche 9 à +0,0219.
4. Valeurs égales entre couches voisines, près de zéro seulement : logits « steer 4x » couches 0 et 1 (0,0289) ; logits « ablate win »
   couches 1 et 2 (0,0064). Aucune lentille identique à une autre aux couches 0 à 30 ; aucun quartile `r_q25` = `r_q75` ; tableau des
   grandeurs par pôle égal au résumé de `score` (écart 0).

**Désaccords avec le code de la course** (`verdicts_b_alpha_v3.py`, `8f57088a…`, lu après mon calcul) : aucun de fond.
- Libellé : la course écrit « partiel » pour B-2 et B-7, le texte gelé « autre » (pour B-7 : « autre : couche par couche »).
- Lectures déclarées par le code, sans effet ici : « non reproduit » non jugé sur une bande partielle (aucune bande partielle) ;
  (b) jugé sur n < 32 tous motifs confondus au lieu du seul motif « effet nul » (0 écarté) ; témoin de B-2 sur les seules couches lisibles
  (toutes lisibles) ; `verdict()` rend B-7 vide en chaîne en défaut (pas de chaîne en défaut).
- `verdict_b7` : `par_le_haut = false`, `par_le_bas = false` aux deux lots, comme mon calcul.
- Intervalles de la course différents entre les deux séries malgré des entrées identiques (par ex. `npR`, « steer 1x », couche 0 :
  [0,0844 ; 0,2169] au lot 16, [0,0896 ; 0,2138] au lot 64) : tirages de rééchantillonnage différents ; ils ne décident de rien.

**Ambiguïtés du § 5 du plan** : 1 (témoin et couches non lisibles), 2 (bande partielle), 3 (bande sans couche lisible) : non rencontrées,
toutes les couches étant lisibles. 4 (arrondi) : aucun côté de seuil changé. 5 : motif « effet nul » séparé. 6 : couche 31 exclue de
tout. 7 : corpus égal (§ 5).

**Autres constats** : champ « instance » vide dans la partie 2 ; journaux sans compagnon. La contre-lecture du plan v3 notait un point
possible (n de la graine 1 en deux sources) : sans objet, aucun audit joué.

Aucun modèle chargé, aucune machine, aucun appel payant, aucun code du dépôt voisin exécuté, aucun autre `diag/` ni `runs/` lu, aucun
fichier existant modifié, aucun commit. Verdict à soumettre à Lazar.
