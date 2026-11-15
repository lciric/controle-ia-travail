# Verdict de la tranche B-α de « Neuron Lens » (Llama 3.1 8B Instruct, lentilles publiques de Neuronpedia) — v1

Lecteur neuf (sous-agent ; n'a écrit ni le texte gelé, ni le code, ni les commandes, ni la course, ni le verdict du volet A).
Course `20261115-120622-neuron-lens-b-alpha`, branche `prep/neuron-lens-v1`, tête `7f29cf08`. Écrit le 2026-11-15 après 14:20 UTC.
Critères appliqués tels qu'écrits au texte gelé v6 (`docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`, `34b88243`).
Expérience **hors du programme** : rien ici n'entre dans T0.7, T0.8, G0, G1 ni P3b sans nœud de Lazar.

## Verdict, en mots simples

- **Reproduction (B-2 et B-3) : « partiel ».** Aucune chaîne en défaut, aucun audit de symétrie gelé déclenché.
  - **B-3 : « reproduit ».** Dans la première moitié du réseau (couches 4 à 15), la lentille R publique devance la lentille des logits
    d'au moins 0,20 à chaque couche — de justesse à la couche 4 (0,2085 pour un seuil de 0,20).
  - **B-2 : ni « reproduit » ni « non reproduit » (« autre »).** La lecture R prédit bien l'effet du pilotage à partir de la couche 11
    et très bien au-delà de la couche 15, mais trois conditions manquent en bas de la bande : `r_med` à la couche 8 (0,3883 pour 0,40),
    `pass` à la couche 8 (0,7656 pour 0,90) et à la couche 10 (0,8750 pour 0,90). Le témoin tient partout.
- **B-4 (rapportée, non décisive)** : la lentille R publique est **en dessous** de la lentille J publique à 19 couches sur 20
  (écart de −0,103 à +0,025, couches 4 à 23) et au-dessus de J++ aux 20 couches (+0,032 à +0,153). Le signe prédit (« positif et petit »)
  n'est pas retrouvé face à J.
- **B-7 : ni « reproduit » ni « non reproduit » (« autre », à lire couche par couche).** Ce qu'une activation isolée fait en contexte
  est mal prédit des couches 0 à 14 (`r_med` ≤ 0,185) et bien prédit des couches 26 à 29 (≥ 0,805) ; la seule condition manquée est la
  couche 15 (0,3097 pour un plafond de 0,25). La lecture devient valable un peu plus tôt que le texte ne le prévoyait, pas assez pour un
  « non reproduit par le haut ».
- Mes verdicts, calculés sans le code de la course, **sont les mêmes que les siens** (`b-alpha-verdicts.json`, `c4eb22fa`).

Suites écrites au texte : « partiel » se rapporte mesure par mesure ; il ne suspend pas B-β (seule une chaîne en défaut le ferait).
Un « reproduit » de B-3 dit que la lentille lit ce qu'une direction pousse en moyenne, pas qu'elle nomme le concept d'une invite.

## Pièces et empreintes (huit premiers caractères ; toutes vérifiées par leur compagnon)

| pièce | chemin | empreinte |
|---|---|---|
| texte gelé v6 | `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b88243` |
| journal de la course v3 | `docs/notes/neuron-lens-v1/journal-course-b-alpha-v3.md` | `edd37d37` |
| manifeste du run | `runs/20261115-120622-neuron-lens-b-alpha/manifeste.json` | `fd692571` |
| résumé écrit par `score` | `diag/20261115-120622-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json` | `904a512a` |
| n et pôles écartés | `diag/…/b-alpha-grandeurs.json` | `c8fe14b7` |
| grandeurs par pôle | `diag/…/grandeurs-par-pole-b-alpha-v1.json` | `28d20e41` |
| contrôles de B0 | `diag/…/b-alpha-b0.json` | `7eef2e31` |
| code des verdicts rejoué (B.3) | `diag/…/b-alpha-b3.json` | `2db5a9e3` |
| fumée | `diag/…/b-alpha-fumee.json` | `4ecfc52b` |
| addendum, partie 2 | `diag/…/addendum-partie2-b-alpha-v1.md` ; `diag/…/b-alpha-partie2.json` | `5a55f96a` ; `45bb5b32` |
| étape `measure` | `diag/…/b-alpha-measure.json` | `9a1ca972` |
| verdicts de la course | `diag/…/b-alpha-verdicts.json` | `c4eb22fa` |
| copie du code publié de la mesure | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/scripts-checks-causal_lens.py.txt` | `befb7018` |
| mon plan de lecture (scellé avant tout résultat) | `docs/notes/neuron-lens-v1/lecture-b-alpha/plan-de-lecture-v1.md` | `5a799918` |
| mon calcul : programme, sortie | `…/lecture-b-alpha/calcul_verdicts_b_alpha_v1.py` ; `…/calcul-verdicts-b-alpha-v1.json` | `18d82258` ; `6f0b9078` |
| mon complément : programme, sortie | `…/lecture-b-alpha/complement_lecture_b_alpha_v1.py` ; `…/complement-lecture-b-alpha-v1.json` | `1bdfc421` ; `998a8485` |

Empreintes : les 21 pièces à compagnon de `diag/20261115-120622-neuron-lens-b-alpha/` et le manifeste sont conformes. Les huit journaux
`journaux/*.log` **n'ont pas de compagnon** (je les ai lus tels quels ; `measure.log` : `59798e36`). L'empreinte du résumé de `score` et
celle du fichier `-causal.pt` (`7615933b`, non versé : 2,1 Go) se recoupent entre `b-alpha-score.json`, `b-alpha-measure.json` et les
grandeurs par pôle.

Dans la suite, sauf mention : chiffres du résumé de `score` (`904a512a`), repris dans ma sortie (`6f0b9078`, clé `tableau`) ; intervalles
à 95 % : les miens, 2 000 rééchantillonnages des pôles, `SeedSequence(entropy=20261115)` (`6f0b9078`, clé `intervalles_95`) ; valeurs
non arrondies : `998a8485`.

## 1. Chaîne en défaut : aucune

| condition | constat | marge | source |
|---|---|---|---|
| (a) témoin hors de ±0,10, couches 0 à 27, 4 cibles × 4 lentilles | aucune | plus grand \|`control_med`\| : 0,0694 (« steer 4x », J, couche 11) ; par cible : 0,0437 (« steer 1x »), 0,0347 (« ablate pos »), 0,0240 (« ablate win ») | `904a512a` ; `6f0b9078` |
| (b) plus de 32 pôles écartés pour effet nul, « steer 1x », couches 0 à 27 | aucune | 0 pôle écarté à toute couche | `c8fe14b7` |
| (c) cas sains, couches 28 à 30 | tenus | logits : 0,8445 ; 0,8649 ; 0,8976 (plancher 0,80) ; `npR` : 0,9675 ; 0,9718 ; 0,9799 (plancher 0,85) | `904a512a` |
| (d) essais et fumée | tenus | correctif (1) 7 passés ; correctif (2) 13 passés ; graine 8 ; crochets 4 ; aucun sauté ; fumée code 0 | `7eef2e31` ; `4ecfc52b` |
| (e) repli sur les logits | aucun | plus petit \|`r_med`(lentille) − `r_med`(logits)\|, couches 0 à 23 : 0,0023 (`npJpp`, couche 1) pour un plancher de 0,001 ; aucune matrice identité aux couches 0 à 27 ; 31 couches `0..30` pour `J`, `npJpp`, `npR` | `904a512a` ; `7eef2e31` |
| code des verdicts de la course (B.3) | 35 essais passés, avant et après la passe | — | `7eef2e31` ; `2db5a9e3` |
| partie 2 de l'addendum | « Écarts : aucun » ; empreintes des trois lentilles égales à celles du texte (`d5300a15`, `8bd04f48`, `a63a1588`) | — | `5a55f96a` |

Marge la plus mince : (e) à la couche 1 pour `npJpp` (0,0297 contre 0,0320 pour les logits : écart 0,0023, à 0,0013 du plancher). Les deux
valeurs sont proches de zéro à cette couche ; je le signale, ce n'est pas un défaut selon la règle.

## 2. Lisibilité

n = 64 à chacune des 32 couches et pour chacune des quatre cibles (`c8fe14b7`) : toutes les couches sont lisibles (n ≥ 48), aucune bande
n'est « partielle ». n est celui que le code de la course a recalculé depuis `-causal.pt` ; je ne peux pas le refaire (fichier non versé),
mais je retrouve 64 pôles retenus par couche, cible et lentille dans les grandeurs par pôle (`28d20e41`).

## 3. B-2 — lentille `npR`, « steer 1x »

| couche | `r_med` | intervalle | seuil | `pass` | seuil | `control_med` |
|---|---|---|---|---|---|---|
| 8 | **0,3883** | [0,334 ; 0,427] | 0,40 | **0,7656** | 0,90 | +0,0026 |
| 9 | 0,4178 | [0,395 ; 0,458] | 0,40 | 0,9062 | 0,90 | −0,0062 |
| 10 | 0,4813 | [0,456 ; 0,504] | 0,40 | **0,8750** | 0,90 | +0,0186 |
| 11 | 0,4708 | [0,444 ; 0,506] | 0,40 | 0,9531 | 0,90 | −0,0007 |
| 12 | 0,5611 | [0,514 ; 0,603] | 0,40 | 0,9688 | 0,90 | −0,0074 |
| 13 | 0,6412 | [0,620 ; 0,656] | 0,40 | 1,0000 | 0,90 | +0,0177 |
| 14 | 0,7137 | [0,687 ; 0,723] | 0,40 | 0,9688 | 0,90 | −0,0063 |
| 15 | 0,7933 | [0,785 ; 0,801] | 0,40 | 1,0000 | 0,90 | −0,0103 |
| 16 | 0,8188 | [0,808 ; 0,826] | 0,60 | 1,0000 | 0,90 | −0,0041 |
| 17 | 0,8606 | [0,852 ; 0,868] | 0,60 | 1,0000 | 0,90 | +0,0016 |
| 18 | 0,8800 | [0,875 ; 0,886] | 0,60 | 1,0000 | 0,90 | +0,0002 |
| 19 | 0,8987 | [0,895 ; 0,901] | 0,60 | 1,0000 | 0,90 | −0,0027 |
| 20 | 0,9095 | [0,907 ; 0,914] | 0,60 | 1,0000 | 0,90 | −0,0086 |
| 21 | 0,9247 | [0,923 ; 0,926] | 0,60 | 1,0000 | 0,90 | +0,0008 |
| 22 | 0,9337 | [0,932 ; 0,935] | 0,60 | 1,0000 | 0,90 | −0,0026 |
| 23 | 0,9411 | [0,939 ; 0,943] | 0,60 | 1,0000 | 0,90 | −0,0117 |
| 24 | 0,9486 | [0,947 ; 0,950] | 0,85 | 1,0000 | 0,90 | −0,0092 |
| 25 | 0,9528 | [0,952 ; 0,954] | 0,85 | 1,0000 | 0,90 | −0,0006 |
| 26 | 0,9582 | [0,956 ; 0,959] | 0,85 | 1,0000 | 0,90 | −0,0058 |
| 27 | 0,9609 | [0,960 ; 0,962] | 0,85 | 1,0000 | 0,90 | −0,0067 |

- « Reproduit » : **non** — trois conditions manquées (en gras), toutes aux couches 8 et 10. `pass` vaut 49/64 à la couche 8 et
  56/64 à la couche 10 ; il en fallait 58 (`998a8485`).
- Témoin (couches 0 à 27) : aucune couche hors de ±0,05 ; plus grand |`control_med`| 0,0249 (couche 1). Les deux lectures de mon plan
  (toutes couches, couches lisibles) coïncident, toutes les couches étant lisibles.
- « Non reproduit » : **non** — aucune couche 16 à 27 avec `pass` < 0,50, aucune couche 16 à 23 avec `r_med` < 0,30.
- Donc **« autre »**, ce que le tableau des critères gelés range sous « partiel, mesure par mesure ».
- Près du seuil : `r_med` de la couche 8 vaut 0,388313 non arrondi ; son intervalle contient 0,40. Avec une médiane ordinaire (moyenne des
  deux valeurs centrales) au lieu de celle de `score` (la plus basse des deux), il vaudrait 0,399799, toujours sous 0,40 (`998a8485`). Les
  deux manques de `pass` ne tiennent pas à un pôle près du centile commun (0,292589) : le pôle le plus proche en est à 0,006 (couche 8) et
  0,006 (couche 10), et il manque 9 et 2 pôles.
- Pour repère, hors critère : couches 0 à 7, `r_med` de 0,1475 à 0,3808 ; « steer 4x », `npR` : 0,1459 à 0,9792 sur les couches 0 à 30,
  même allure.

## 4. B-3 — `r_med`(`npR`) − `r_med`(logits), « steer 1x », couches 4 à 15

| couche | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| écart | 0,2085 | 0,2350 | 0,2992 | 0,2987 | 0,2896 | 0,2818 | 0,3210 | 0,3049 | 0,3533 | 0,3329 | 0,3246 | 0,2817 |
| intervalle, bas | 0,189 | 0,194 | 0,251 | 0,259 | 0,239 | 0,261 | 0,296 | 0,275 | 0,297 | 0,310 | 0,297 | 0,270 |
| intervalle, haut | 0,240 | 0,291 | 0,352 | 0,332 | 0,333 | 0,326 | 0,354 | 0,339 | 0,403 | 0,343 | 0,348 | 0,297 |

- « Reproduit » : **oui** — écart ≥ +0,20 aux 12 couches. « Non reproduit » : non (aucun écart ≤ 0).
- Marge mince à la couche 4 : 0,2085 (0,208473 non arrondi ; 0,209411 avec une médiane ordinaire), soit 0,0085 au-dessus du seuil ;
  l'intervalle [0,189 ; 0,240] contient 0,20, et celui de la couche 5 aussi [0,194 ; 0,291]. Le texte décide sur la valeur ponctuelle :
  le verdict est « reproduit », mais il ne tient qu'à cette marge à la couche 4.
- Les écarts observés (+0,21 à +0,35) sont en dessous des écarts publiés pour Qwen3-8B que cite le texte (+0,352 à +0,425, niveau du
  texte gelé, que je n'ai pas revérifié sur le fichier de référence).

## 5. B-4 — rapportée, non décisive (couches 4 à 23, « steer 1x »)

- `r_med`(`npR`) − `r_med`(`J`) : de −0,1027 (couche 12) à +0,0250 (couche 4) ; positif à **1 couche sur 20** (la couche 4).
- `r_med`(`npR`) − `r_med`(`npJpp`) : de +0,0320 (couche 20) à +0,1529 (couche 13) ; positif aux 20 couches.
- La prédiction (« positif et petit, +0,026 à +0,131 publiés ») n'est pas retrouvée face à la lentille J publique : J lit le pilotage
  un peu mieux que R à presque toutes les couches. Le texte ne dit pas à laquelle des deux différences la prédiction s'attache
  (**ambiguïté, non arbitrée**) ; je rapporte les deux.

## 6. B-7 — « ablate win », lentille `npR`

| couche | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `r_med` | −0,0091 | 0,0122 | 0,0062 | 0,0542 | 0,0565 | 0,0434 | 0,0666 | 0,0527 | 0,0670 | 0,0628 | 0,0493 | 0,1002 | 0,1137 | 0,1646 | 0,1847 | **0,3097** |

| couche | 26 | 27 | 28 | 29 |
|---|---|---|---|---|
| `r_med` | 0,8053 | 0,8384 | 0,8111 | 0,8450 |
| intervalle | [0,789 ; 0,817] | [0,817 ; 0,856] | [0,753 ; 0,860] | [0,825 ; 0,867] |

- « Reproduit » : **non** — la condition « < 0,25 à chaque couche 0 à 15 » manque à la seule couche 15 (0,3097 ; intervalle
  [0,277 ; 0,333], entièrement au-dessus de 0,25 ; 47 pôles sur 64 ont r ≥ 0,25). La condition « ≥ 0,50 aux couches 26 à 29 » tient
  largement.
- « Non reproduit » : **non** — aucune couche 8 à 15 à 0,40 ou plus (par le haut) ; aucune couche 26 à 29 sous 0,30 (par le bas).
- Donc **« autre » : couche par couche.** La course écrit « partiel » pour B-7 ; le texte n'emploie pas ce mot pour B-7 (il dit « autre :
  couche par couche ») — même issue, libellé différent.
- Couche par couche : lecture basse (≤ 0,185) des couches 0 à 14 ; montée à partir de 15 (0,31), 0,50 atteint vers la couche 19-20
  (0,4976 puis 0,5169), 0,69 à la couche 23, ≥ 0,75 dès la couche 24. Pour un moniteur : avant la couche 15, l'étiquette d'un neurone
  décrit une poussée moyenne et ne dit pas ce qu'une activation donnée fait dans un épisode ; cela vaut pour les quatre lentilles (à la
  couche 15 : logits 0,2151, J 0,2964, J++ 0,2801, R 0,3097 ; à la couche 26 : 0,7243 ; 0,8062 ; 0,7177 ; 0,8053).
- Le témoin de cette cible reste petit (|`control_med`| ≤ 0,0240).

## 7. Audits de symétrie gelés (R4)

- « Trop beau » : **non déclenché** — aucune couche 0 à 7 avec `r_med` ≥ 0,95 (maximum 0,3808) ; aucun `control_med` écrit égal à 0
  aux couches 0 à 27 (le plus proche : 0,0002 à la couche 18).
- « Tout négatif » : **non déclenché** (B-3 est « reproduit », B-2 n'est pas « non reproduit »).
- L'audit à la graine 1 n'a donc pas été joué ; aucune pièce de cet audit n'existe dans la course.

## 8. Écart de lot `measure --ctx-batch 16` (défaut publié : 64)

- Déclaré au journal (`edd37d37`) et à la décision R-2901 (`registres/decisions.md`, ligne 2861) ; visible dans la ligne de commande de
  `journaux/measure.log` (`59798e36`, **sans compagnon**) et dans la constante du lanceur v3 (`44bba9c0`, empreinte au manifeste). Le
  résumé de `score` et le manifeste ne le consignent pas (`meta` : 32 par couche, 16 contextes, 64 jetons, 8 premiers documents, fenêtre 8 —
  les quatre défauts gelés sont bien ceux du texte).
- D'après la copie du code publié (`befb7018`, lignes 216-217), `--ctx-batch` n'est lu que dans la boucle d'**ablation** ; le pilotage
  emploie `--cond-batch`, resté à son défaut. **B-2, B-3 et B-4 (« steer 1x ») ne sont donc pas touchés** par l'écart. Sont touchés :
  B-7 (« ablate win »), « ablate pos », et la condition (a) pour ces deux cibles.
- Nature de l'effet : le lot change le nombre de lignes par passe et la longueur de remplissage ; la ligne propre et la ligne ablatée
  d'un même contexte restent dans la même passe (lignes 219 à 244). L'effet attendu est donc un bruit numérique de la demi-précision.
  **Je ne peux pas le mesurer** : aucune course à lot 64 n'existe pour l'ablation (elle a épuisé la mémoire, R-2901).
- Sensibilité des verdicts : la seule condition de B-7 qui décide (couche 15) est à 0,06 de son seuil, intervalle entièrement du même
  côté ; les couches 26 à 29 sont à 0,31 ou plus du leur ; aucune couche 8 à 15 n'est à moins de 0,09 du seuil de « non reproduit par le
  haut ». Un bruit numérique ne peut pas, raisonnablement, changer l'issue de B-7 ni la condition (a). Savoir si un écart de lot est ou non
  un écart au texte gelé a été tranché par la mère (R-2901) ; **je ne l'arbitre pas**.

## 9. Mes verdicts contre ceux de la course

| | course (`c4eb22fa`) | lecteur (`6f0b9078`) | accord |
|---|---|---|---|
| chaîne en défaut | aucune | aucune | oui |
| audits requis | aucun | aucun | oui |
| B-2 | « partiel » | « autre » (= partiel) | oui |
| B-3 | « reproduit », écart minimal 0,2085 | « reproduit », 0,2085 | oui |
| B-4 | 40 valeurs | les mêmes 40 valeurs | oui |
| B-7 | « partiel » | « autre », couche par couche | oui (libellé différent) |
| reproduction | « partiel » | « partiel » | oui |

Mon recalcul de `r_med` et `control_med` à partir des r par pôle égale le résumé de `score` à 0,00005 près ; `pass` recalculé avec le
centile commun écrit par la course est identique partout (`998a8485`). (Dans `6f0b9078`, mon propre recalcul du centile, fait sur des r
arrondis à 6 décimales, déplace un pôle sur 64 à une couche : écart de 1/64 dû à l'arrondi, sans rôle dans les verdicts, qui lisent le
résumé de `score`.) Intervalles de la course et les miens (graines différentes) : écart de borne de 0,008 au plus pour `npR`, « steer 1x ».

## 10. Écarts, ambiguïtés et constats — non arbitrés

1. **Ce que je savais avant de sceller mon plan** : le journal, que la consigne fait lire d'abord, écrit « aucun audit R4 requis »,
   « aucun défaut (e) », « partie 2 sans écart ». Déclaré au plan (`5a799918`). Je ne connaissais aucune valeur ni aucun verdict de mesure.
2. **Intervalles** : le texte demande des intervalles « rapportés » ; la course n'en écrit que pour « steer 1x » (logits et `npR`), aucun
   pour « ablate win » (B-7) ni pour l'écart de B-3. Les miens comblent ce manque ; ils ne décident de rien.
3. **Lecture des `config.yaml` et `CREDIT.md`** : le texte la place à B0, sur la machine ; elle a été faite avant le feu
   (`docs/notes/neuron-lens-v1/devis-b-alpha/lecture-config-credit-neuronpedia-v1.md`, que je n'ai pas relue) et l'addendum n'en porte que
   les empreintes git. Les nombres de documents d'ajustement (461 ; 64) restent donc au niveau citation pour moi.
4. **`essais_ok=True` écrit en dur** à l'appel du verdict dans le lanceur v3 (`b_alpha_lancer_v3.py`, ligne 769, `44bba9c0`) : la
   condition (d) n'est pas relue par le code des verdicts au moment du verdict (le lanceur est censé s'arrêter plus tôt). Je l'ai vérifiée
   moi-même sur `b-alpha-b0.json` et `b-alpha-fumee.json`.
5. **Journaux sans compagnon** (`journaux/*.log`, huit fichiers) ; champ « instance » vide dans l'addendum de la partie 2.
6. **Fumée** : `--docs 64` donne « 256 documents » (64 par tranche, quatre tranches) ; code 0.
7. **Médiane** : `r_med` est la médiane de `score` (`torch.median` : la plus basse des deux valeurs centrales pour 64 pôles), pas la
   médiane ordinaire. Aucun verdict ne change entre les deux (§§ 3, 4, 6), mais la couche 8 de B-2 passe de 0,3883 à 0,3998.
8. **B-4** : prédiction « positif et petit » sans dire contre quelle lentille (§ 5).
9. **B-7** : libellé « partiel » de la course contre « autre : couche par couche » du texte (§ 6).
10. J'ai vu, sans les étudier, les lignes 215 à 234 du code des verdicts de la course (`controle_lentille` : 31 couches, identité à
    10⁻⁶ près aux couches 0 à 27) en cherchant d'où venaient les champs « arrêts » et « défauts » de B0 ; mon calcul n'en reprend rien.
11. Je n'ai pas rouvert la référence publiée de Qwen3-8B : les valeurs « publiées » citées ici sont celles du texte gelé.

## 11. Réserves de symétrie (un résultat trop propre se signale, dans les deux sens)

Aucun des deux déclencheurs gelés ne se déclenche. Je signale en plus, sans en tirer de verdict :

1. **Aucun pôle écarté, n = 64 partout** (32 couches × 4 cibles ; `c8fe14b7`). Le texte rappelle que la référence de Qwen3-8B a des
   dénominateurs de 59, 57, 62, 61 aux couches 1 à 4. Zéro pôle sans contexte et zéro effet nul sur 2 048 pôles est propre ; cela peut
   tenir au modèle et au corpus (64 000 documents), mais je ne peux pas le contrôler sans `-causal.pt`. Les « tirs » et doses par pôle
   sont versés (`28d20e41`) : un contrôle par un tiers est possible (tirs tous strictement positifs ?).
2. **Haut de la bande très propre** : `pass` = 1,0000 à 14 des 20 couches 8 à 27 ; `r_med` de 0,9486 à 0,9609 aux couches 24 à 27 avec
   des intervalles de largeur 0,002 à 0,003. C'est l'allure attendue (toute lentille approche 1 en fin de réseau), et le témoin reste
   près de zéro ; rien d'anormal relevé, mais c'est du côté « beau ».
3. **Centile commun du témoin élevé pour les lentilles** : 0,2926 pour `npR`, 0,3356 pour `J`, 0,2631 pour `npJpp`, contre 0,0710 pour
   les logits (« steer 1x », `28d20e41`). La médiane du témoin est petite, mais une part des pôles appariés à la lecture d'un autre
   neurone corrèle à 0,3 ou plus : indice d'une composante commune aux lectures par lentille (le « mode commun » que le texte nomme en
   (a) sans qu'il atteigne le seuil). Les deux manques de `pass` de B-2 dépendent de ce centile.
4. **Ablation mieux lue que prévu** : la prédiction de B-7 (« < 0,25 sur 0 à 15 ») manque à la couche 15, et les couches 26 à 29 sont à
   0,81-0,85, au-dessus de ce que le texte cite pour la référence (couche 26 de Qwen3-8B : 0,54). C'est un écart du côté positif, sur la
   seule cible touchée par l'écart de lot ; il ne déclenche ni l'audit « trop beau » (qui ne porte que sur « steer 1x ») ni le « non
   reproduit par le haut ». Je le signale pour qu'il ne soit pas lu comme une confirmation sans contrôle.
5. **Du côté négatif** : B-2 manque aux deux couches les plus basses de sa bande, là où les seuils, convertis en profondeur, sont
   les plus exigeants par rapport au publié (0,54 à 0,71 fois, selon le texte) ; et la lentille R publique est sous la lentille J
   publique (B-4). Le texte prévoit qu'un résultat en retrait « ne conclut pas sur la chaîne » (64 documents d'ajustement, autre corpus,
   autre code) : B-β tranche.
6. **B-3 tient à 0,0085** à la couche 4 (§ 4) : « reproduit » sur la valeur ponctuelle, fragile au sens de l'intervalle.
7. Couche 31 : `J`, `npJpp`, `npR` identiques aux logits, et « ablate win » identique à « ablate pos » (0,9988) — attendu (pas de
   lentille à la couche 31 ; une ablation à la dernière couche n'agit qu'à sa position) ; ces valeurs n'entrent dans aucun verdict.

## 12. Ce que je n'ai pas fait

Aucun modèle chargé, aucune machine, aucun appel payant, aucun commit ; rien lu sous `donnees/` ni `docs/verdicts/`, aucun autre `diag/`
ni `runs/`, aucune autre branche. Je n'ai pas recalculé n ni les corrélations depuis les activations (fichier non versé) : mes verdicts
reposent sur le résumé écrit par `score` et sur les r par pôle écrits par le code de la course, dont la garde de fidélité à `score` est
déclarée passée (`28d20e41`, champ `fidelite_a_score`). Verdict à soumettre à Lazar ; il n'ouvre ni ne ferme aucune porte du programme.
