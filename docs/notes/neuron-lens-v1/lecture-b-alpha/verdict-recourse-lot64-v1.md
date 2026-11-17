# Verdict de la recourse de la tranche B-alpha de « Neuron Lens » (lots 16 et 64 sur A100 SXM4 40 Go) — v1

Lecteur neuf (sous-agent ; n'a ecrit ni le texte gele, ni le code, ni les commandes, ni la course, ni le premier verdict).
Course `20261117-015632-neuron-lens-b-alpha`, branche `calcul/neuron-lens-b-alpha-v6`, tete `ea814779`. Ecrit le 2026-11-17.
Criteres appliques tels qu'ecrits au texte gele v6 (`34b88243`) et a l'addendum v3 (`5f05f5bc`).
Experience **hors du programme** : rien ici n'entre dans T0.7, T0.8, G0, G1 ni P3b sans noeud de Lazar.

## Verdict, en mots simples

- **Verdict de B-7 de la recourse (lot 64, A100) : « autre » (couche par couche).**
  La seule condition manquee est la couche 15 (`r_med` = 0,3117 pour un plafond de 0,25). La condition
  « >= 0,50 aux couches 26 a 29 » tient largement (0,81 a 0,85). Meme issue qu'a la troisieme course (RTX 4090, lot 16 :
  couche 15 a 0,3097). Ce verdict **remplace** celui de la troisieme course pour B-7 (addendum v3, paragraphe 3).
- **Fait critique : toutes les valeurs sont identiques entre le lot 16 et le lot 64.** Les deux
  empreintes `causal.sha256` sont les memes (`7c1b5de9`). La mesure au lot 64 a produit un fichier identique au bit
  pres a celle du lot 16. La comparaison (c) est zero partout, la comparaison (a) aussi. **B-7 ne depend pas du lot**.
- **B-7 ne depend pas du materiel** (meme verdict « autre » sur A100 et RTX 4090, memes couches manquantes).
- **Aucune divergence de B-2 ni de B-3 entre l'A100 et la RTX 4090** : memes verdicts (B-2 « autre », B-3 « reproduit »),
  memes couches manquantes.
- Mes verdicts, calcules sans le code de la course, **sont les memes que les siens** aux deux series
  (`7228cf99` lot 16 ; `bb66eebf` lot 64).

## Pieces et empreintes (huit premiers caracteres ; toutes verifiees par leur compagnon)

| piece | chemin | empreinte |
|---|---|---|
| texte gele v6 | `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (branche `prep/neuron-lens-v1`) | `34b88243` |
| addendum v3 | `docs/notes/neuron-lens-v1/addendum-texte-gele-v6-recourse-b7-a100-v3.md` (branche `prep/neuron-lens-v1`) | `5f05f5bc` |
| premier verdict (troisieme course) | `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` | `ca06acb1` |
| resume de `score`, lot 16 | `diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json` | `bd57d519` |
| resume de `score`, lot 64 | `diag/…/causal_lens_lot64_llama-3.1-8b-instruct.json` | `bd57d519` |
| n et poles ecartes, lot 16 | `diag/…/b-alpha-grandeurs.json` | `6465f3da` |
| n et poles ecartes, lot 64 | `diag/…/b-alpha-grandeurs-lot64.json` | `1a36d8a8` |
| grandeurs par pole, lot 16 | `diag/…/grandeurs-par-pole-b-alpha-v1.json` | `6cce8f72` |
| grandeurs par pole, lot 64 | `diag/…/grandeurs-par-pole-b-alpha-lot64-v1.json` | `6cce8f72` |
| controles de B0 | `diag/…/b-alpha-b0.json` | `e79aa88e` |
| fumee | `diag/…/b-alpha-fumee.json` | `203e68ac` |
| etape `measure`, lot 16 | `diag/…/b-alpha-measure.json` | `47327c23` |
| etape `measure`, lot 64 | `diag/…/b-alpha-measure-lot64.json` | `a61dbbd1` |
| bascule lot 64 | `diag/…/b-alpha-bascule-lot64.json` | `1af3aaf0` |
| verdicts de la course, lot 16 | `diag/…/b-alpha-verdicts.json` | `7228cf99` |
| verdicts de la course, lot 64 | `diag/…/b-alpha-verdicts-lot64.json` | `bb66eebf` |
| resume troisieme course (RTX) | `diag/20261115-120622-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json` (branche `calcul/neuron-lens-b-alpha-v3`) | `904a512a` |
| grandeurs troisieme course | `diag/20261115-120622-…/b-alpha-grandeurs.json` (branche `calcul/neuron-lens-b-alpha-v3`) | `c8fe14b7` |
| grandeurs par pole troisieme course | `diag/20261115-120622-…/grandeurs-par-pole-b-alpha-v1.json` (branche `calcul/neuron-lens-b-alpha-v3`) | `28d20e41` |
| mon plan de lecture (scelle avant tout resultat) | `…/lecture-b-alpha/plan-de-lecture-recourse-lot64-v1.md` | `acd96c84` |
| mon calcul : programme | `…/lecture-b-alpha/calcul_verdicts_recourse_lot64_v1.py` | `4f7d93e9` |
| mon calcul : sortie | `…/lecture-b-alpha/calcul-verdicts-recourse-lot64-v1.json` | `3bfaf735` |

Empreintes : les 26 pieces a compagnon de `diag/20261117-015632-neuron-lens-b-alpha/` sont conformes. Les 10 journaux
`journaux/*.log` **n'ont pas de compagnon** (lus tels quels). Les trois pieces de la troisieme course (branche
`calcul/neuron-lens-b-alpha-v3`) sont conformes a leurs compagnons et commencent par les empreintes acceptees par le
premier verdict (`904a512a`, `c8fe14b7`, `28d20e41`).

Dans la suite, sauf mention : chiffres du resume de `score` (lot 64 = lot 16 : `bd57d519`), repris dans ma sortie
(`3bfaf735`) ; intervalles a 95 % : les miens, 2 000 reechantillonnages, `SeedSequence(entropy=20261117)`.

## 1. Chaine en defaut : aucune (aux deux series)

| condition | constat | marge | source |
|---|---|---|---|
| (a) temoin hors de +/-0,10, couches 0 a 27, 4 cibles x 4 lentilles | aucune | plus grand \|`control_med`\| : 0,0680 (« steer 4x », J, couche 11) | `bd57d519` ; `3bfaf735` |
| (b) plus de 32 poles ecartes pour effet nul, « steer 1x », couches 0 a 27 | aucune | 0 pole ecarte a toute couche | `6465f3da` ; `1a36d8a8` |
| (c) cas sains, couches 28 a 30 | tenus | logits : 0,8520 ; 0,8700 ; 0,8970 (plancher 0,80) ; `npR` : 0,9676 ; 0,9719 ; 0,9803 (plancher 0,85) | `bd57d519` |
| (d) essais et fumee | tenus | `essais_ok` lu des resultats scelles de B0, B.3 et fumee (correction v5 du lanceur) ; fumee code 0 | `e79aa88e` ; `203e68ac` |
| (e) repli sur les logits | aucun | plus petit \|`r_med`(lentille) - `r_med`(logits)\|, couches 0 a 23 : 0,0019 (`npJpp`, couche 1) pour un plancher de 0,001 | `bd57d519` |

La condition (d) est effective dans le code du lanceur v5 : `essais_ok` est lu des resultats scelles, non ecrit en dur
(changement declare a l'addendum v3, paragraphe 2, point 3).

## 2. Lisibilite

n = 64 a chacune des 32 couches et pour chacune des quatre cibles, aux deux series (`6465f3da`, `1a36d8a8`) : toutes les
couches sont lisibles (n >= 48), aucune bande n'est « partielle ».

## 3. B-2 — lentille `npR`, « steer 1x » (valeurs A100, identiques aux deux lots)

| couche | `r_med` | seuil | `pass` | seuil | `control_med` |
|---|---|---|---|---|---|
| 8 | **0,4089** | 0,40 | **0,7500** | 0,90 | +0,0021 |
| 9 | 0,4335 | 0,40 | 0,9219 | 0,90 | -0,0107 |
| 10 | 0,4777 | 0,40 | **0,8750** | 0,90 | +0,0150 |
| 11 | 0,4764 | 0,40 | 0,9375 | 0,90 | +0,0026 |
| 12 | 0,5775 | 0,40 | 0,9688 | 0,90 | -0,0196 |
| 13 | 0,6349 | 0,40 | 1,0000 | 0,90 | +0,0147 |
| 14 | 0,7107 | 0,40 | 0,9688 | 0,90 | -0,0025 |
| 15 | 0,7918 | 0,40 | 1,0000 | 0,90 | -0,0109 |
| 16 | 0,8186 | 0,60 | 1,0000 | 0,90 | -0,0056 |
| 17 | 0,8614 | 0,60 | 1,0000 | 0,90 | +0,0009 |
| 18 | 0,8798 | 0,60 | 1,0000 | 0,90 | +0,0007 |
| 19 | 0,8983 | 0,60 | 1,0000 | 0,90 | -0,0015 |
| 20 | 0,9093 | 0,60 | 1,0000 | 0,90 | -0,0090 |
| 21 | 0,9246 | 0,60 | 1,0000 | 0,90 | +0,0014 |
| 22 | 0,9336 | 0,60 | 1,0000 | 0,90 | -0,0026 |
| 23 | 0,9411 | 0,60 | 1,0000 | 0,90 | -0,0114 |
| 24 | 0,9481 | 0,85 | 1,0000 | 0,90 | -0,0093 |
| 25 | 0,9529 | 0,85 | 1,0000 | 0,90 | -0,0007 |
| 26 | 0,9580 | 0,85 | 1,0000 | 0,90 | -0,0074 |
| 27 | 0,9609 | 0,85 | 1,0000 | 0,90 | -0,0068 |

- « Reproduit » : **non** — deux conditions manquees (en gras) : `pass` a la couche 8 (0,7500 = 48/64 pour 0,90) et a la
  couche 10 (0,8750 = 56/64 pour 0,90). `r_med` a la couche 8 (0,4089) passe le seuil de 0,40 (a la difference de la RTX,
  0,3883 ; c'est l'unique point ou la valeur d'une couche passe un seuil de r_med sur une carte et pas sur l'autre).
- Temoin (couches 0 a 27) : aucune couche hors de +/-0,05 ; plus grand |`control_med`| 0,0196 (couche 12).
- « Non reproduit » : **non** — aucune couche 16 a 27 avec `pass` < 0,50, aucune couche 16 a 23 avec `r_med` < 0,30.
- Donc **« autre »**, ce que le code de la course ecrit « partiel ».

## 4. B-3 — `r_med`(`npR`) - `r_med`(logits), « steer 1x », couches 4 a 15

| couche | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ecart | 0,2091 | 0,2396 | 0,2916 | 0,2960 | 0,3125 | 0,2935 | 0,3151 | 0,3136 | 0,3748 | 0,3258 | 0,3211 | 0,2824 |

- « Reproduit » : **oui** — ecart >= +0,20 aux 12 couches. Ecart minimal a la couche 4 : 0,2091 (0,0091 au-dessus du seuil).
- A comparer a la troisieme course (RTX) : ecart minimal 0,2085 (couche 4 aussi, ecart au seuil de 0,0085). L'A100
  devance la RTX de 0,0006 a cette couche ; les deux passent.

## 5. B-4 — rapportee, non decisive (couches 4 a 23, « steer 1x »)

- `r_med`(`npR`) - `r_med`(`J`) : de -0,0851 (couche 12) a +0,0068 (couche 4) ; positif a **1 couche sur 20**.
- `r_med`(`npR`) - `r_med`(`npJpp`) : de +0,0325 (couche 20) a +0,1513 (couche 8) ; positif aux 20 couches.
- Meme constat que la troisieme course : J lit le pilotage un peu mieux que R a presque toutes les couches ;
  R devance J++ partout.

## 6. B-7 — « ablate win », lentille `npR` (valeurs A100, identiques aux deux lots)

| couche | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `r_med` | -0,0029 | 0,0248 | 0,0065 | 0,0531 | 0,0763 | 0,0439 | 0,0670 | 0,0821 | 0,0504 | 0,0664 | 0,0281 | 0,0994 | 0,1108 | 0,1701 | 0,1861 | **0,3117** |

| couche | 26 | 27 | 28 | 29 |
|---|---|---|---|---|
| `r_med` | 0,8126 | 0,8423 | 0,8108 | 0,8468 |

- « Reproduit » : **non** — la condition « < 0,25 a chaque couche 0 a 15 » manque a la seule couche 15 (0,3117, a 0,0617
  du plafond de 0,25). La condition « >= 0,50 aux couches 26 a 29 » tient largement.
- « Non reproduit » : **non** — aucune couche 8 a 15 a 0,40 ou plus (par le haut) ; aucune couche 26 a 29 sous 0,30
  (par le bas).
- Donc **« autre » : couche par couche.** La course ecrit « partiel » — meme issue, libelle different (comme au
  premier verdict).

## 7. Audits de symetrie geles (R4)

- **« Trop beau »** : **non declenche** aux deux series — aucune couche 0 a 7 avec `r_med` >= 0,95 (maximum 0,3808 aux
  deux series) ; aucun `control_med` ecrit egal a 0 aux couches 0 a 27 (le plus proche : 0,0002 a la couche 18, « steer 1x »,
  logits).
- **« Tout negatif »** : **non declenche** (B-3 est « reproduit », B-2 n'est pas « non reproduit »).
- L'audit a la graine 1 n'a donc pas ete joue ; les fichiers `seed1` ne sont pas presents dans la course.
- **B-7 « par le haut »** : non requis (ni lot 16 ni lot 64 ne rendent « non reproduit par le haut »).

## 8. Controle de serie (lu avant les comparaisons)

| controle | attendu | constate | source |
|---|---|---|---|
| `measure` lot 16 : `resultat.lot` | 16 | 16 | `47327c23` |
| `measure` lot 64 : `resultat.lot` | 64 | 64 | `a61dbbd1` |
| bascule : `deplaces[…].sha256` = `measure` lot 16 `causal.sha256` | egal | egal | `1af3aaf0`, `47327c23` |
| `causal.sha256` lot 16 | — | `7c1b5de9…` | `47327c23` |
| `causal.sha256` lot 64 | — | `7c1b5de9…` | `a61dbbd1` |
| les deux `causal.sha256` | differentes si l'ablation depend du lot | **identiques** | reserve |
| `meta` lot 16 = `meta` lot 64 | egaux | egaux | `bd57d519` |
| `meta` conformes aux defauts geles | 32 par couche, 16 contextes, 64 jetons, doses 1 et 4, fenetre 8, 8 premiers documents | conformes | `bd57d519` |
| resume lot 16 `sha256` = resume lot 64 `sha256` | — | **identiques** (`bd57d519`) | reserve |
| grandeurs par pole lot 16 `sha256` = lot 64 `sha256` | — | **identiques** (`6cce8f72`) | reserve |

**Reserve** : les deux empreintes `causal.sha256` sont identiques (`7c1b5de955fca525a7d2c9af7c39cb57ce9c051178ef103e82b3188d84cb3ce6`).
Le fichier de mesure au lot 64 est identique au bit pres a celui du lot 16. Par consequent les deux resumes de
`score`, les deux fichiers de grandeurs et les deux fichiers de grandeurs par pole sont aussi identiques. Les deux
series ne sont pas deux mesures d'ablation distinctes : elles sont la meme mesure, lue deux fois. L'ecart de lot
n'existe pas dans les donnees. Les comparaisons (c) et (a) ci-dessous sont mecaniquement nulles. Je ne conclus pas sur
la cause (la mesure du lot de contexte n'affecte peut-etre pas l'ablation telle qu'elle est codee ; ou le code de
bascule n'a pas fonctionne comme prevu) : je le rapporte.

## 9. Comparaison (c) — cas sain de determinisme (A100, lot 64 contre lot 16)

max |delta `r_med`| (pilotage, « steer 1x » et « steer 4x », 4 lentilles, couches 0 a 31) : **0,0** (256 valeurs).
max |delta `pass`| : 0,0. max |delta `control_med`| : 0,0.
Couches 0 a 27 : idem, 0,0. Le seuil de reserve de 0,01 de l'addendum n'est **pas atteint**.

Ceci est mecanique : les deux resumes de `score` sont le meme fichier (paragraphe 8).

## 10. Comparaison (a) — effet du lot, meme carte (A100, lot 64 contre lot 16)

max |delta `r_med`| (ablation, « ablate win » et « ablate pos », 4 lentilles, couches 0 a 31) : **0,0** (256 valeurs).
Meme chose par pole : delta `r`(pole) = 0,0 partout (mediane 0, extremes 0 a chaque couche).

Ceci est mecanique : meme reserve qu'au paragraphe 8. L'effet du lot sur l'ablation n'est **pas mesurable** par cette
recourse ; les deux series sont le meme calcul.

## 11. Comparaison (b) — effet du materiel, meme lot (A100 lot 16 contre RTX 4090 lot 16)

Sources de la troisieme course : branche `calcul/neuron-lens-b-alpha-v3`, course `20261115-120622-neuron-lens-b-alpha`.
Empreintes verifiees : `904a512a`, `c8fe14b7`, `28d20e41` (celles du premier verdict).

| cible | lentille | max \|delta `r_med`\| | couche | A100 | RTX |
|---|---|---|---|---|---|
| steer 1x | logit | 0,0091 | 1 | 0,0411 | 0,0320 |
| steer 1x | J | 0,0212 | 5 | 0,3396 | 0,3184 |
| steer 1x | npJpp | 0,0213 | 1 | 0,0084 | 0,0297 |
| steer 1x | npR | 0,0206 | 8 | 0,4089 | 0,3883 |
| steer 4x | logit | 0,0028 | 7 | 0,0709 | 0,0737 |
| steer 4x | J | 0,0062 | 4 | 0,2096 | 0,2158 |
| steer 4x | npJpp | 0,0087 | 3 | 0,0735 | 0,0822 |
| steer 4x | npR | 0,0114 | 2 | 0,1722 | 0,1836 |
| ablate win | logit | 0,0126 | 12 | 0,0627 | 0,0501 |
| ablate win | J | **0,0296** | 6 | 0,0480 | 0,0776 |
| ablate win | npJpp | 0,0249 | 4 | 0,0586 | 0,0337 |
| ablate win | npR | 0,0294 | 7 | 0,0821 | 0,0527 |
| ablate pos | logit | 0,0112 | 25 | 0,7201 | 0,7089 |
| ablate pos | J | 0,0142 | 3 | 0,0188 | 0,0330 |
| ablate pos | npJpp | 0,0212 | 6 | 0,0469 | 0,0681 |
| ablate pos | npR | 0,0226 | 2 | 0,0187 | -0,0039 |

max |delta `r_med`| global : **0,0296** (« ablate win », J, couche 6). L'effet du materiel est un ordre de grandeur
au-dessus de l'effet du lot (qui est 0), mais il reste petit (< 0,03).

**Couches qui decident de B-7** (« ablate win », `npR`) :

| couche | A100 | RTX | delta | seuil |
|---|---|---|---|---|
| 0 | -0,0029 | -0,0091 | +0,0062 | < 0,25 |
| 1 | 0,0248 | 0,0122 | +0,0126 | < 0,25 |
| 2 | 0,0065 | 0,0062 | +0,0003 | < 0,25 |
| 3 | 0,0531 | 0,0542 | -0,0011 | < 0,25 |
| 4 | 0,0763 | 0,0565 | +0,0198 | < 0,25 |
| 5 | 0,0439 | 0,0434 | +0,0005 | < 0,25 |
| 6 | 0,0670 | 0,0666 | +0,0004 | < 0,25 |
| 7 | 0,0821 | 0,0527 | +0,0294 | < 0,25 |
| 8 | 0,0504 | 0,0670 | -0,0166 | < 0,25 |
| 9 | 0,0664 | 0,0628 | +0,0036 | < 0,25 |
| 10 | 0,0281 | 0,0493 | -0,0212 | < 0,25 |
| 11 | 0,0994 | 0,1002 | -0,0008 | < 0,25 |
| 12 | 0,1108 | 0,1137 | -0,0029 | < 0,25 |
| 13 | 0,1701 | 0,1646 | +0,0055 | < 0,25 |
| 14 | 0,1861 | 0,1847 | +0,0014 | < 0,25 |
| 15 | 0,3117 | 0,3097 | +0,0020 | < 0,25 |
| 26 | 0,8126 | 0,8053 | +0,0073 | >= 0,50 |
| 27 | 0,8423 | 0,8384 | +0,0039 | >= 0,50 |
| 28 | 0,8108 | 0,8111 | -0,0003 | >= 0,50 |
| 29 | 0,8468 | 0,8450 | +0,0018 | >= 0,50 |

La couche 15 (decisive) vaut 0,3117 sur A100 et 0,3097 sur RTX (delta +0,0020) : les deux sont au-dessus de 0,25,
meme verdict « autre ». Le plus grand |delta| aux couches 0 a 15 est 0,0294 (couche 7) ; la plus petite marge au seuil
de 0,25 est 0,0617 (couche 15, A100) : la marge est deux fois plus grande que le plus grand ecart du materiel.

**Couches de B-2 proches d'un seuil** (`npR`, « steer 1x ») :
- Couche 8 : A100 `r_med` = 0,4089 (passe >= 0,40), RTX `r_med` = 0,3883 (echoue). C'est le seul point ou `r_med`
  change de cote par rapport au seuil entre les deux cartes. Mais `pass` echoue aux deux cartes (A100 : 0,7500 ; RTX :
  0,7656 ; seuil 0,90), et B-2 reste « autre » aux deux cartes.

## 12. Phrases de conclusion (addendum v3, paragraphe 3)

| mesure | B-7 | B-2 | B-3 | reproduction |
|---|---|---|---|---|
| troisieme course (RTX 4090, lot 16) | autre (couche 15 : 0,3097) | autre | reproduit (ecart min 0,2085) | partiel |
| recourse A100, lot 16 | autre (couche 15 : 0,3117) | autre | reproduit (ecart min 0,2091) | partiel |
| recourse A100, lot 64 | autre (couche 15 : 0,3117) | autre | reproduit (ecart min 0,2091) | partiel |

- **B-7 ne depend pas du lot** : meme verdict, memes valeurs (paragraphes 8 a 10).
- **B-7 ne depend pas du materiel** : meme verdict (« autre »), meme couche manquante (15), marge au seuil (0,06)
  superieure au plus grand ecart du materiel (0,03).
- **Aucune divergence de B-2** entre A100 et RTX : meme verdict (« autre »), memes couches manquantes (8 et 10 sur `pass`).
  La seule difference est que `r_med` a la couche 8 passe 0,40 sur A100 (0,4089) et pas sur RTX (0,3883), mais `pass`
  echoue aux deux.
- **Aucune divergence de B-3** : meme verdict (« reproduit »), ecart minimal a la couche 4 aux deux cartes (0,2091
  A100 ; 0,2085 RTX ; les deux au-dessus de 0,20).

## 13. Mes verdicts contre ceux de la course

| | course lot 16 (`7228cf99`) | course lot 64 (`bb66eebf`) | lecteur lot 16 (`3bfaf735`) | lecteur lot 64 (`3bfaf735`) | accord |
|---|---|---|---|---|---|
| chaine en defaut | aucune | aucune | aucune | aucune | oui |
| audits requis | aucun | aucun | aucun | aucun | oui |
| B-2 | « partiel » | « partiel » | « autre » (= partiel) | « autre » (= partiel) | oui |
| B-3 | « reproduit », 0,2091 | « reproduit », 0,2091 | « reproduit », 0,2091 | « reproduit », 0,2091 | oui |
| B-7 | « partiel » | « partiel » | « autre », couche par couche | « autre », couche par couche | oui (libelle different) |
| reproduction | « partiel » | « partiel » | « partiel » | « partiel » | oui |

Mon recalcul de `r_med` et `control_med` a partir des r par pole est identique au resume de `score` a une unite de la
quatrieme decimale (fidelite declaree par le programme de la course et verifiee par le mien).

## 14. Reserves et constats

1. **Les deux series sont le meme calcul** (reserve, paragraphe 8). L'effet du lot sur l'ablation n'est pas mesure par
   cette recourse. L'ecart de lot declare a la troisieme course (R-2901) n'est pas leve par des donnees differentes ;
   il est leve par un lot qui ne change pas le fichier de sortie. Que le lot 64 soit « le defaut publie » est vrai, mais
   les donnees de la recourse ne montrent pas que l'ablation y serait differente. La question « un ecart de lot est-il
   un ecart au texte gele » (premier verdict, paragraphe 8) n'est toujours pas tranchee par la mesure.

2. **Reserve 1 du plan : meme tirage de poles**. Aucune option `--seed` dans les journaux de `measure`, aucun fichier
   `seed1` dans la course. Les sequences de poles sont identiques entre les deux series et avec la troisieme course
   (meme `random.Random(0)` tire par le code). Cette reserve ne change rien au verdict (memes neurones evalues aux
   memes invites ; ce n'est pas une reproduction independante).

3. **B-2 couche 8, `r_med` de part et d'autre du seuil de 0,40** entre les cartes (A100 : 0,4089 ; RTX : 0,3883).
   C'est un ecart de materiel, pas de lot. `pass` echoue aux deux : le verdict de B-2 ne change pas. Mais la valeur
   est proche du seuil et cote d'un cote different selon la carte ; pour un moniteur, la lecture « npR predit le
   pilotage a partir de la couche 8 » tient sur A100 (par `r_med`) et pas sur RTX.

4. **B-3 couche 4 : marge fragile** (0,0091 au-dessus de 0,20 sur A100, 0,0085 sur RTX). Le verdict « reproduit »
   tient a cette marge aux deux cartes. L'ecart entre cartes (0,0006) est un dixieme de la marge.

5. **Pas de journaux compagnons** : les 10 fichiers `journaux/*.log` n'ont pas de `.sha256` (meme constat que le
   premier verdict).

6. **Condition (d)** : effective dans le code du lanceur v5, lue des resultats scelles (addendum v3, paragraphe 2,
   point 3). Verifiee sur `b-alpha-b0.json` et `b-alpha-fumee.json`.

7. **n = 64 partout, 0 pole ecarte** aux deux series et aux quatre cibles (meme constat que le premier verdict ;
   reserve de proprete signee).

## 15. Ce que je n'ai pas fait

Aucune machine, aucun appel payant, aucun commit ; rien lu sous `donnees/` ni `docs/verdicts/` ; aucun `diag/` ni
`runs/` sur la branche `main` ; aucune autre branche que `prep/neuron-lens-v1`, `calcul/neuron-lens-b-alpha-v6` et
`calcul/neuron-lens-b-alpha-v3` ; aucun arbitrage d'ambiguite ; aucune relance de serie. Verdict a soumettre a Lazar ;
il n'ouvre ni ne ferme aucune porte du programme.
