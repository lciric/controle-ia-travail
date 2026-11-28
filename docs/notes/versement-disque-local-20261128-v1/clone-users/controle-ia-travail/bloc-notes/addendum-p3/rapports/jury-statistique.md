# Jury statistique — implémentations de l'addendum de lecture complémentaire de P3 (v1)

Angle : justesse statistique. Points examinés : plancher conjoint tirage par tirage, fenêtres de même longueur, tranches
recalculées dans le tirage, aire intra-tâche, niveaux, cas dégénérés, graines et déterminisme.
Fond de référence : brouillon 1 du préenregistrement de l'addendum. Les constats RA-01 à RA-23 de la contre-lecture ont
été lus pour information.
Date : 2026-10-20.

## Verdict

- **Gagnant : candidat « b » (8,0 sur 10).** Le candidat « a » obtient 7,5. Le noyau de Gemini obtient 2,0.
- Le cœur statistique de « a » et de « b » est le même et il est juste. Sur la même source, la même lecture et les mêmes
  graines, les deux rendent des estimations ponctuelles égales pour A1 à A6. Les deux retrouvent mes deux calculs faits à
  la main.
- « b » l'emporte pour trois raisons :
  - ses artefacts de données exercent les vrais mécanismes (biais de longueur du maximum en A2 (b), plancher qui varie
    avec les tâches sur la sonde retenue en A1, trois artefacts de données en A4) ;
  - sa garde de concordance prouve que la lecture décisive a été calculée sur ce run source ;
  - il est le seul des deux à tenir « arrêt après le manifeste, écrit avec son motif ».
- « a » est meilleur sur quatre points, à greffer dans « b » :
  - la vraie règle de `lire_action` en A5 (RA-01) ;
  - une garde de l'issue qui peut vraiment échouer (RA-04) ;
  - aucun nombre non fini remplacé en silence ;
  - le décompte des fenêtres qui ne sont pas de même longueur.
- Défauts communs aux deux, à corriger dans la version retenue :
  - en A4 (b), une tâche tirée k fois pèse k² ;
  - en A4 (a), le nombre de tranches de chaque tirage n'est pas rapporté ;
  - aucune marge n'est rapportée pour la variabilité due au nombre fini de tirages, près des seuils.

## Ce que j'ai fait (tout dans `rapports/jury-statistique-travail/`)

Aucun fichier n'a été écrit hors de `rapports/`. Le dépôt de travail est propre (`git status` vide). Les dossiers des
candidats n'ont pas changé : je n'ai ajouté ni fichier de cache ni code compilé.

- Empreintes vérifiées. Celles de « b » sont égales aux empreintes annoncées :
  - module « b » : `8f2410f5…dc9` ; tests « b » : `7a3684e1…25` ;
  - module « a » : `dc232ac3…70d` ; tests « a » : `f54353de…11` ;
  - noyau de Gemini : `0ddbdab4…7b2`.
- Suites de tests, lancées avec `PYTHONDONTWRITEBYTECODE=1`, sans cache et avec un dossier temporaire dans
  `rapports/` :
  - « a » : 61 réussis en 108 s ;
  - « b » : 60 réussis en 297 s.
- Gemini : le module **ne se compile pas**. On obtient `IndentationError` à la ligne 332 (`     base = {` a cinq espaces).
  Pour le juger comme greffe, j'en ai fait une copie corrigée d'une seule espace :
  `gemini_copie/noyau_gemini_corrige_indentation.py`.
- Scripts du juge :
  - `v1_aires.py` : aires vectorisées des trois candidats contre le code gelé ;
  - `v2_plancher_conjoint_main.py` : calcul à la main n° 1 ;
  - `v3_fenetres_main.py` : calcul à la main n° 2 ;
  - `v4_intra_tache_et_tranches.py` : poids k² et tranches ex aequo ;
  - `v5_comparaison_et_determinisme.py` : mêmes données, « a » contre « b » ;
  - `v6_artefacts_croises.py` : artefacts de chaque candidat passés dans l'autre ;
  - `v7_a1_plancher.py` : variabilité due au nombre de tirages ;
  - `v8_garde_issue.py` : garde de l'issue et nombres non finis.

## Calculs refaits à la main

### 1. Plancher conjoint (A1), trois tâches, deux sondes de plancher, quatre tirages imposés

Données (score de la sonde s, plancher p1 et p2, étiquette y, tâche) :

- t0 : (0,9 ; 0,1 ; 0,5 ; 1) et (0,2 ; 0,3 ; 0,5 ; 0) ;
- t1 : (0,6 ; 0,8 ; 0,2 ; 1) et (0,6 ; 0,4 ; 0,9 ; 0) ;
- t2 : (0,3 ; 0,7 ; 0,6 ; 1) et (0,5 ; 0,6 ; 0,1 ; 0).

Valeurs observées :

- aire de la sonde : 6,5/9 = 0,7222 ;
- aires du plancher : 6/9 et 4,5/9 ;
- quantile 0,95 (interpolation linéaire) : Q = 0,5 + 0,95 × 0,1667 = 0,6583 ;
- écart observé : Δ_obs = 0,0639.

Tirages imposés :

| Tirage | Tâches tirées | A(b) | Aires du plancher | Q(b) | Δ(b) |
|---|---|---|---|---|---|
| b1 | t0, t0, t2 | 8/9 | 3/9 et 7/9 | 0,7556 | 0,1333 |
| b2 | t1 × 3 | 0,5 | 1 et 0 | 0,95 | −0,45 |
| b3 | t2, t1, t0 | — | — | — | 0,0639 |
| b4 | t0 × 3 | 1 | 0 et 0,5 | 0,475 | 0,525 |

Le tirage b3 retrouve exactement l'échantillon observé.

Intervalle à 50 % (pour la démonstration) : de −0,0646 à 0,2313.

- « a » (`plancher_conjoint`), « b » (`ecart_conjoint`) et Gemini corrigé rendent ces valeurs à 0 près.
- L'exemple montre aussi ce que G-02 vise. Au plancher figé, la borne basse de A (0,6667) dépasse Q_obs (0,6583) : le jeu
  est « au-dessus ». Au plancher conjoint, Δ_bas = −0,0646 ≤ 0 : la réserve A1 est levée.

### 2. Fenêtres de même longueur (A2 (b)), départs imposés

- **Action 0.** Scores (1, 5, 2, 3, 9, 4, 7). Le champ du coût va du jeton 4 au jeton 6 : c = 4, L = 2.
  - Coût = max(9, 4) = 9.
  - Départs possibles {0, 1, 2}. Fenêtres : 5, 5, 3.
  - Fenêtre juste avant le champ : 3.
- **Action 1.** c = 1, L = 4, donc c ≤ L : la fenêtre est tout le pré-coût, soit 8 (un seul jeton contre quatre).
- **Sonde à attention.** Somme pondérée par le softmax des logits restreints à la fenêtre.
  - Logits (0, 1, 2, 0, 3, −1, 0) : coût 8,9101 ; fenêtres 3,9242, 2,8068 et 2,1192.
  - Logits nuls sur l'action 1 : coût 2,5.

« a » (`_fenetres`) et « b » (`localisation`) rendent tous ces nombres à 1e-12 près. Le maximum ou le softmax est pris sur
l'empan ; aucune moyenne des jetons d'une action n'entre dans un score.

### 3. Aire intra-tâche (A4 (b)) : une tâche tirée deux fois pèse quatre fois

Données : tâche X (positif 0,9, négatif 0,1 : aire 1) et tâche Y (positif 0,2, négatif 0,8 : aire 0). Aire observée :
(1 + 0) / 2 = 0,5.

Tirage X, X, Y :

- **Code des trois candidats** (tranche commune aux copies) : (2·2·1 + 1·0) / (4 + 1) = **0,8**. « a », « b » et Gemini
  rendent tous 0,8.
- **Une tranche par copie** : (1 + 1 + 0) / 3 = **0,667**. C'est le poids k du tirage par blocs.

Effet mesuré sur douze tâches mixtes simulées (4 000 tirages) :

- tranche commune : écart type 0,113, intervalle à 95 % de 0,244 à 0,719 ;
- tranche par copie : écart type 0,082, intervalle à 95 % de 0,305 à 0,631.

L'intervalle est environ 38 % plus large avec la tranche commune. Les deux candidats lisent la réserve d'A4 (b) sur l'aire
ponctuelle, donc l'erreur ne touche que l'intervalle descriptif. Elle reste à corriger (RA-06).

## Comparaison point par point (angle statistique)

| Point | « a » | « b » |
|---|---|---|
| Plancher conjoint : A(b) et Q(b) sur le même multi-ensemble, Δ = A − Q, `np.quantile` comme la lecture | juste (vérifié à la main) | juste (vérifié à la main) |
| Niveaux A1 : 97,5 % pour saboteur contre honnête, 95 % sinon ; T1 et T4 à 95 % | oui | oui |
| Effectif minimal (10 de chaque côté), plus de 1 % de tirages dégénérés = échec | oui | oui |
| Fenêtres : départs uniformes dans {0, …, c − L}, R = 50, réplique b mod R | oui | oui |
| Cas c ≤ L (fenêtres plus courtes que le champ) | compté (`actions_pre_cout_entier`) | **non compté** |
| Estimateur observé d'A2 (b) | moyenne, minimum et maximum des différences d'aires sur les répliques | idem, plus l'aire moyenne des fenêtres |
| A2 (c), fenêtre juste avant | différence observée seulement | différence et intervalle (descriptif) |
| T4 aux tranches recalculées (`strates_quantiles` sur les coûts tirés), plancher sur les mêmes tranches | oui | oui |
| Nombre de tranches par tirage (RA-17) | non rapporté | non rapporté |
| A4 (b) : tâches tirées | seules les tâches mixtes | toutes les tâches de T1 (donne un sens à « 1 % sans paire ») |
| A4 (b) : intervalle | écart conjoint (plancher tiré aussi) | aire de la sonde seule |
| A4 (b) : poids k² | oui (défaut) | oui (défaut) |
| A4 (c) : référence géométrique | `10**mean(log10)` (égal à RA-22) | `cout_de_tache` (exactement RA-22) |
| Graines | `generateur` pour ses boucles, `graine_entiere` pour le code gelé ; clés `addendum/<analyse>/<sonde>/<objet>` | `default_rng(graine_entiere(…))` partout ; mêmes clés |
| Déterminisme octet pour octet (deux passages, mêmes données) | oui | oui |
| Entrées intactes (source, lecture, graines) | oui (vérifié par moi ; ses tests ne contrôlent que la lecture) | oui (testé) |
| Nombre non fini dans la sortie | arrêt (`_propre`) | **remplacé par None en silence** (`_vers_json`) |
| Unité de « plus de la moitié des analyses en échec » | entrées (analyse × sonde) entièrement en échec | analyses dont au moins une sous-analyse est en échec |
| A8, entropie normalisée d'une action d'un seul jeton | 0,0 en silence | None, et le nombre de ces actions est rapporté |

Comparaison sur les mêmes données (`_source(0)` avec textes, même lecture, union des graines, 200 tirages) :

- les estimations ponctuelles sont identiques dans A1 (sept jeux, deux sondes), A2 (a), A3, A4 (a), (b) et (c), A5
  (T2_propre) et A6 ;
- l'intervalle d'A2 (a) et celui de T2_propre sont identiques, parce que la clé et la graine sont les mêmes ;
- les intervalles d'A1 diffèrent de quelques millièmes, parce que les générateurs diffèrent ;
- aucune réserve chez l'un ni chez l'autre.

Artefacts croisés :

- les neuf artefacts de « a » passés dans « b » lèvent la même réserve ;
- les douze artefacts de « b » passés dans « a » lèvent la même réserve.

Une seule différence : sur l'artefact « plancher qui varie avec les tâches », « b » lève aussi la réserve sur P3-P4 et
sur T3, et « a » ne la lève pas. L'écart vient du générateur, pas du code. Avec 2 000 tirages, Δ_bas de saboteur contre
mention vaut −0,0007 chez « a » et +0,0027 chez « b ». Δ_bas de saboteur contre témoin vaut −0,0032 et −0,0008. Près de 0,
le signe de la borne basse dépend de la graine. Aucun des deux ne le signale. C'est à écrire comme réserve de lecture pour
le sous-agent du verdict (symétrie, R4).

## Tests par analyse (cas sain, artefact, cas dégénéré, verrou)

Les deux couvrent les quatre cas pour A1 à A9. A9 n'a pas de réserve possible : son artefact vérifie qu'aucune réserve
n'est levée. La qualité statistique des artefacts diffère.

- **A1.**
  - « a » : un artefact de données, une confusion par tâche de la mention partagée par ses sondes de plancher. Il vise T3.
  - « b » : un artefact de données, un plancher décalé par tâche. Il vise la sonde retenue, donc P3-P3, le cœur de G-02.
- **A2.**
  - « a » ne teste que le niveau (a).
  - « b » teste le niveau et le **biais de longueur du maximum**, avec des jetons aberrants : le pré-coût de 20 jetons est
    noyé plus souvent que le champ de 5 jetons. C'est le seul test qui montre que les fenêtres de même longueur font leur
    travail. « a » réussit cet artefact quand je le lui passe, mais ses propres tests ne le prouvent pas.
- **A3.** Les deux forcent la conformité de P3-P4 dans une copie de la lecture : c'est un artefact de lecture.
- **A4.**
  - « a » : tranches internes par un artefact de lecture (T4 forcé), confusion par un artefact de données.
  - « b » : trois artefacts de données (tranches, confusion, référence géométrique), plus un cas « peu de tâches mixtes »
    où l'intervalle n'est pas lu mais la comparaison au plancher est gardée.
- **A5 à A8.** Artefacts de données des deux côtés.

## Tests transverses

| Test | « a » | « b » |
|---|---|---|
| Déterminisme octet pour octet | oui | oui, et entrées intactes |
| Refus d'une autre entropie (fonction pure et lancement) | oui | oui (y compris la valeur True) |
| Issue inchangée, garde sur une copie altérée | oui. Garde réelle : l'issue est fixée avant les analyses, et une analyse qui modifie la lecture arrête (vérifié) | copie altérée testée. Mais la copie est faite à la fin et comparée à la même lecture : une analyse qui modifie l'issue en cours de route **passe** (vérifié : l'issue recopiée devient « organisme non établi » sans arrêt). RA-04 reste ouvert |
| Aucune moyenne sur les jetons (le score d'empan est le maximum) | oui | oui (maximum et softmax) |
| Aire vectorisée égale au code gelé à 1e-12, ex aequo compris | oui (mon contrôle : 400 cas, écart maximal 0 ; 1,1e-16 avec tranches) | oui (même contrôle) |
| Gardes R5 (cas sain et artefact) | source hors de forme, état introuvable, verrou interne, import, lecture non décisive, textes altérés, module non cité, nom du run | source, lecture (introuvable, non booléen, état inconnu, sondes principales autres, **aires incohérentes avec la source**, nombre de sondes de plancher), verrou, aires, textes, lecture d'un autre run ou d'une autre entropie, module hors de son chemin |
| Lancement de bout en bout | gardes d'avant le manifeste, passage scellé et rattaché, second passage refusé (clé : run source **et** lecture). **Pas d'arrêt écrit après le manifeste** | tout, y compris `arret-addendum-p3.json` scellé avec son motif. Second passage refusé sur le run source seul |

Aucun des deux ne lance le module par la vraie ligne de commande : les deux appellent `executer`, et `_main` n'est pas
testé.

## Noyau de Gemini (greffes seulement)

- Le fichier livré ne se compile pas. Avec une espace retirée, `aires_par_rangs`, `plancher_conjoint`,
  `t4_tranches_internes` et `t1_intra_tache` sont justes : mêmes nombres que mes calculs à la main, et égalité au code gelé
  à 1e-16.
- Défauts :
  - aucun effectif minimal ;
  - graine entière et non `SeedSequence` dérivée d'une clé ;
  - booléens `au_dessus_conjoint` et `au_dessus_du_plancher` dans la sortie (RA-05) ;
  - poids k² dans `t1_intra_tache` ;
  - import d'une fonction privée (`statistiques._tables`) ;
  - ni A5 à A9, ni verrou, ni garde, ni test.
- Seule greffe utile : `_verifier_params_bootstrap` (lignes 26 à 34). C'est une garde d'entrée : niveau dans ]0, 1[, au
  moins un tirage, quantile et part des tirages dégénérés dans leurs bornes.

## Greffes recommandées dans « b »

1. **Règle réelle de `lire_action` en A5.** Prendre `position_cout_lire_action`, `_vers_brut` et `_NETTOYAGE` de « a »
   (lignes 105 et 665 à 711), avec leur garde : la valeur lue doit égaler `lire_action(texte).champs["COST"]`.
   - « b » ne compare `bornes_champs` qu'à la règle « puce, dernière occurrence » que le brouillon prête à tort à
     `lire_action` (RA-01).
   - Exemple de cas manqué : « *COST: 30 », gras ouvert sans fermeture. `bornes_champs` le voit, `lire_action` ne le lit
     pas, et la règle du brouillon le voit aussi : « b » ne voit aucune divergence.
   - T2_propre doit exclure l'union des divergences, comme « a ».
2. **Issue fixée avant les analyses.** Reprendre de « a » le motif des lignes 1435 et 1455 à 1457 : `issue_canonique` est
   pris avant toute analyse, puis on vérifie après que la lecture n'a pas changé. Cela ferme RA-04.
3. **Aucun nombre non fini remplacé en silence.** Remplacer `_vers_json` par `_propre` de « a » (lignes 464 à 482).
4. **Second passage.** Dans `exiger_premier_passage`, un manifeste illisible doit arrêter (« a », lignes 1481 à 1490), au
   lieu de `continue`. Garder la clé de « b » (le run source seul, comme le brouillon).
5. **Fenêtres trop courtes.** Ajouter à la sortie d'A2 (b) le nombre d'actions où c ≤ L (« a », `pre_entier`).
6. **A4 (b), intervalle de l'écart conjoint.** Tirer aussi le plancher, comme « a » (`plancher_conjoint(...,
   strates=tache)`, lignes 1031 à 1037), après avoir corrigé le poids k².
7. **Lancement.** Ajouter la vérification du nom `AAAAMMJJ-HHMMSS-addendum-p3` et celle du run source décisif en mode réel
   (« a », lignes 68, 1497 et 1502 à 1504).
8. **Gemini.** Ajouter `_verifier_params_bootstrap` à l'entrée de `ecart_conjoint`, de `fenetres_meme_longueur` et de
   `contrastes`.

## Corrections communes, à faire dans la version retenue

- **A4 (b).** Dans chaque tirage, donner une tranche propre à chaque copie d'une tâche, par exemple la position dans le
  tirage. Une tâche tirée k fois doit peser k, pas k². Seulement là : pour les tranches de coût (A1 T4, A4 (a)), les copies
  doivent partager leur tranche, comme dans `detection_stratifiee`.
- **A4 (a).** Rapporter le nombre de tranches observé et sa distribution sur les tirages (minimum, maximum). Exemple
  vérifié : avec des coûts ex aequo, on observe 3 tranches sur 5, et entre 1 et 4 selon le tirage (RA-17).
- **Variabilité due au nombre de tirages.** Rapporter, pour chaque contrôle qui lève ou évite une réserve, la part des
  tirages où Δ ≤ 0. Le sous-agent du verdict pourra ainsi voir les réserves qui tiennent à quelques millièmes.
- **Booléens de la sortie.** Plusieurs booléens peuvent se lire comme des conclusions (RA-05) :
  - chez « a » : `etabli` de T2_propre, `au_dessus_du_plancher`, `aire_cout_bas_au_dessus` ;
  - chez « b » : `au_dessus_de_0_5`, `a_au_dessus_de_b`, `etabli`, `aire_cout_au_dessus`.

  Les renommer en « contrôle_… » ou les ranger sous `descriptif`.

## Durées (journaux des candidats, non refaits ici)

À la taille de P3 (2 400 actions, 430 sondes), avec 2 000 et 10 000 tirages :

- « a » : 438 s ;
- « b » : 332 s.

Les deux sont bien en dessous de l'estimation de RA-21 (de l'ordre d'une heure).
