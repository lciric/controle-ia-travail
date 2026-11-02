scellable après corrections — liste exacte : B-2 (reconduit), B-L1, B-L2, puis I-A à I-E (section « Ce qui reste bloquant ») ; le texte précède le code, donc le scellement attend de toute façon le commit final, ses empreintes, la configuration et « Tests attendus » (sept « À REMPLIR »).

# Vérification anticipée du brouillon 2 de l'addendum de relance v2 de R1 (« rejeu à graine ») et du module « lot fidèle » — v1

- Lecteur : sous-agent neuf (règle R2), auteur d'aucune pièce ; même lecteur que la vérification du brouillon 1
  (`verification-addendum-r1-v2-brouillon1-v1.md`, `dd7157e1…`), dont les numéros C-1 à C-9, R-01 à R-18, B-, I-, m-
  sont repris.
- Date : 2 novembre 2026, ≈ 10:26–10:55 UTC (heure relevée par `date -u`).
- Pièces (empreintes vérifiées par `git show … | sha256sum`) : texte brouillon 2 `076a6b57:prereg/R1-addendum-relance-v2.md`
  (`d4617ea837cd81accc4dc8e26d6d1be2015f1f10eaecad2258b3e54c9eb48c89`, 494 lignes) ; lot fidèle
  `99022f43:src/controle_ia/runs_nuit/resolution_graine_lot_v1.py` (`9acdd228…`, 858 lignes) et
  `99022f43:tests/test_resolution_graine_lot_v1.py` (`4645f9bc…`, 375 lignes ; `git diff --stat 21a6e583 99022f43 --
  src tests scripts` : ces deux fichiers seuls) ; `06887bdd:src/controle_ia/runs_nuit/rejeu_activations_v3.py`
  (`0581cf9a…`, hors de ce texte, non lu en détail) ; n° 267 (`95951c2d…`) ; `generer_lot` et `jouer_episodes` de
  `97dd8290:src/controle_ia/harnais/episode.py`, `Crochets` de `harnais/activations.py`, `cloture` de
  `harnais/formats.py`, `plan_p3` et `jouer_p3` de `premier_test_ia/run.py`, `reconstruire_episode` de
  `rejeu_activations_v1.py`.
- Abréviations : « A2 » = texte brouillon 2 ; « LOT » = module du lot ; « TL » = ses essais ; « l. » = ligne de
  `git show <commit>:<chemin> | cat -n`.

## 1. Sort de mes corrections C-1 à C-9 et couples R-01 à R-18

| N° | État dans A2 | Où, et jugement |
|---|---|---|
| C-1 (durée par épisode, résultat écrit quand même, délais) | **appliqué dans le texte** | l. 190-191 (consigné dès terminé), 196-199 (causes « durée », « non traité »), 234-236 (600 s, 2 400 s, 900 s, 3 600 s), 296-298, 390-393 (délais = budget + 5 min ; 30 + 45 + 45 + 65 + 10 = 195 < 200, vérifié), 467-473. Cohérent. Code : à venir (VG-01), essais exigés l. 408-410. |
| C-2 (unité de `balayages_max` ; nombre de U+FFFD des 7 et des 147) | **absent** | l. 233 reconduit mot pour mot « 64 balayages du vocabulaire par épisode pour les octets que recouvre un U+FFFD » ; l. 211 compte les balayages (VG-07) sans en changer l'unité ; aucun nombre de U+FFFD par épisode. Le code de base compte un balayage à chaque pas où un U+FFFD est dans les 128 caractères suivants (essai du brouillon 1 : 3 U+FFFD → 90 > 64). **B-2 reconduit.** |
| C-3 (validation non bloquante, cinq conditions) | **appliqué pour (1), (2), (4) ; absent pour (3) et (5)** | (1) règle à trois lignes l. 424-426, réserve écrite au résultat l. 259 ; essai exigé l. 410 ; (2) l. 341-342 (`exiger_validation` sans condition de lecture) ; (4) l. 431 « sans réserve de validation ni de lot » ; (3) la classe de la validation n'est pas recopiée dans le résultat de la résolution ni dans la table v3 (rien ne l'écrit) ; (5) l'interdit R3 « une seule exécution de chaque étape sous ce texte » n'est pas écrit (l. 168-169 ne parle que des prédictions). |
| C-4 (`torch.version.cuda`, filtres d'offre, retrait de `datacenter=true` déclaré et soumis à Lazar) | **partiel** | l. 215 (versions au résultat), 320-322 (réserves), 323-325 (retrait du filtre déclaré et consigné). **Absent** : l'exposition du clone du dépôt privé et des deux jetons (GitHub en écriture, Hugging Face) à un hôte hors centre de données, et sa soumission à Lazar (compte et dépôt distant : nœud, pas routine) ; les filtres restants (pilote compatible CUDA 13.0, débit, fiabilité, prix plafond). |
| C-5 (accord pour les non résolus ; accord attendu sous graine indépendante = p_k ; pas informatifs) | **absent** | l. 202-204 reconduit la définition ; le code de base ne calcule pas l'accord d'un épisode non résolu (`acc_v` nul, RG l. 1085) ; aucune mesure « attendu sous graine indépendante » ni « pas informatifs ». La formule inexacte de l. 167 (« probabilité du jeton le plus probable, typiquement 0,6 à 0,85 ») est reconduite. I-2 et I-4 ouverts. |
| C-6 (R-06 à R-09) | **partiel** | R-06 appliqué autrement et acceptable (G2, l. 126 : liste à Lazar, sort fixé dans l'addendum v3, décision de Lazar pour toute cause autre que U+FFFD). R-07 absent (HG-3 l. 148-150 inchangé). R-08 partiel (l. 299-301 : « le seul cas qui peut être déclaré non inversible … selon Critères » ✓ ; unité des balayages et mot « budget » absents). R-09 partiel (l. 431 : condition « sans réserve de validation ni de lot » ✓, autres causes → nœud ✓ ; la parenthèse fausse « le texte stocké n'est pas l'image exacte des jetons » et le nom de cause « cas non simple » restent). |
| C-7 (le texte décrit le calcul du choix contraint du code scellé) | **appliqué autrement, acceptable** | l. 306-311 : p en float32 sur processeur, puis choix contraint en double à partir de ce p (variante de la décision n° 4 du n° 262, que j'avais acceptée) ; le n° 267 dit « le code sera aligné sur le texte » : à vérifier par la contre-lecture sur le commit final (RG l. 437-443 part encore des logits). La mesure 2·10⁻⁷ nat n'est pas citée (mineur). |
| C-8 (essais ajoutés) | **appliqué pour l'essentiel** | l. 407-413 : repli itératif, paires en validation, budget épuisé, durée de l'étape, validation sous les seuils → résolution quand même, contrôle croisé à trois valeurs, balayages comptés, table v3 scellée et fusion, validation du lot, gardes avancées, CUDA → réserve. **Manquent** : citation de la configuration (`CONFIG_CITEE`, deux libellés), texte attendu de l'ouverture, unité des balayages (C-2). |
| C-9 (P-G3 : chemin et empreinte, ou retrait) | **absent** | l. 180-182 inchangé (« essais du code de base ») ; les essais tournent en float32 (TG l. 105). I-6 ouvert. |
| R-01 (règle de lecture à trois classes) | **appliqué autrement, partiel** | l. 424-426 : trois lignes (validées ; accord sous un seuil → réserve « graines ou précision », tout non résolu = nœud ; moins de 147 avec accord bon → fragilité). Conséquences ✓ (l. 425, 431). Sans « pas informatifs », sans « accord attendu sous graine indépendante », sans l'interdit R3. |
| R-02 (P-G1) | **absent** | l. 164-169 : formule du « jeton le plus probable » reconduite ; réfutation réécrite sans « réserve ». |
| R-03 (étape 0 : mesure) | **appliqué** | l. 332-336. |
| R-04 (étape 1 : ordre, sans condition de lecture) | **appliqué sauf l'ordre** | l. 341-342 ✓ ; les 3 de C-6 restent en fin de liste (l. 247-249) : devenu mineur avec la consignation par épisode (m-5). |
| R-05 (formulation de l'aveugle) | **absent** | l. 329-332 identique au brouillon 1 (m-1 : dit plus que le code). |
| R-10 (lectures de la validation) | **appliqué autrement, acceptable** | l. 425-426. |
| R-11 (contrôle croisé à trois valeurs ; garde de l'étape table) | **appliqué pour la lecture** (l. 343-345, 432-433) ; **absent** pour la garde « étape table sans contrôle croisé conforme » (l. 461-465 ne la cite pas). |
| R-12 (durée) | **appliqué** | l. 234-236, 296-298, 390-393. m-7 (vie de l'instance hors amorce dans le pire cas) absent. |
| R-13 (point (ii) précision) | **appliqué autrement, acceptable** | l. 306-311 (voir C-7). |
| R-14 (carte, CUDA, `datacenter`, exposition, filtres) | **partiel** | voir C-4 : la réserve ✓, le retrait déclaré ✓ ; l'exposition du dépôt et des jetons et la décision de Lazar **absentes** ; filtres absents. |
| R-15 (P-G3 provenance) | **absent** | voir C-9. |
| R-16 (liste d'arrêt) | **appliqué** | l. 461-462, 467-470 ; moins la garde de l'étape table (R-11). |
| R-17 (`combinaisons_max_validation` = 136) | **appliqué** | l. 230-232. |
| R-18 / m-6 (écart d'ordre des modes déclaré) | **absent** | l. 25-26 présente le lot comme « accepté au n° 352 ; il est ici l'étape 1 bis » : le n° 352 l'acceptait **en premier**, la passe forcée en repli ; l'inversion n'est pas déclarée comme écart, ni motivée. |

Sort des bloquants du brouillon 1 : **B-1 levé** (C-1) ; **B-2 reconduit** ; **B-3 levé** pour l'essentiel (règle écrite, validation non bloquante), restes en I-A et I-B.

## 2. Le lot fidèle (`99022f43`)

**(a) « Recopie `generer_lot` appel pour appel » : tient**, à l'opération de tirage près et à un arrêt anticipé déclaré.
Comparaison ligne à ligne avec `97dd8290:harnais/episode.py` l. 89-137 :
- forme du lot : `ids` rempli à gauche de `pad_id`, `masque`, `positions = (masque.cumsum − 1).clamp(0)` (LOT l. 233-238 =
  P3 l. 95-100) ;
- préremplissage : `modele(input_ids, attention_mask, position_ids, use_cache=True, logits_to_keep=1)` (LOT l. 192-196 =
  P3 l. 107-108) ; `suivante = positions[:, -1:] + 1` (LOT l. 246 = P3 l. 109, décalage 0) ;
- par pas : `sortie.logits[:, -1].to("cpu", torch.float32)` (LOT l. 205-207 = P3 l. 111) ; `jetons = full(pad)` ; lignes
  inactives ignorées (LOT l. 252-255 = P3 l. 112-115) ; arrêt d'une ligne à son premier jeton de `fins` (LOT l. 267 = P3
  l. 124) ; `if not any(actives) or pas == max_nouveaux − 1: break` (LOT l. 270 = P3 l. 126) ; `masque = cat(…)`, puis
  `modele(input_ids=jetons, attention_mask=masque, position_ids=suivante, past_key_values=…, use_cache=True,
  logits_to_keep=1)`, `suivante += 1` (LOT l. 274-277 = P3 l. 128-133) ;
- tirage : P3 `multinomial(softmax(logits[r] / T), 1, generator)` (l. 121) ; LOT, ligne cible : `p = softmax(logits / T)` en
  float32 sur processeur, `R = p / Q[s]`, argmax sur les candidats triés, premier maximum (`ChoixCible.choisir`, l. 120-145 ;
  garde « (V,) float32 sur processeur » l. 117-119) — l'opération de P3 restreinte aux candidats, équivalence
  `multinomial = argmax(p / q)` revérifiée au lancement (l. 684) ; autres lignes : jetons forcés (l. 261-264) ;
- différences déclarées : arrêt des passes dès que la cible est finie (l. 272-273, docstring l. 23-24 : sans effet sur
  les logits déjà calculés de la cible, juste) ; lignes forcées arrêtées aussi à `longueurs[r]` (l. 267) ;
- contexte des lignes : `trs[b] = contextes[b] + nvs[b] + fmt.cloture(debuts[b], nvs[b])`, journal des **textes
  stockés** (LOT l. 377-379 = P3 `jouer_episodes` l. 250-255) : les observations suivantes sont exactes ;
- P3 générait parfois sous `Crochets` (lignes de l'échantillon d'équivalence, `jouer_p3` l. 251-258) : les crochets ne
  font que lire (`detach().to("cpu"…).copy()`, `activations.py` l. 26-30), sans effet numérique ;
- plan des lots : `plan_p3` (un épisode par tâche et par condition, conditions entremêlées, lots consécutifs de `lot`)
  reconstruit et vérifié contre l'ordre des textes (LOT l. 485-505 ; essai TL l. 227-246, passé ici).

**(b) Les lignes voisines « approchées » peuvent-elles changer les logits de la cible ?** Par les valeurs, non : les lignes
d'un lot sont indépendantes (remplissage à gauche masqué, positions explicites, cache par ligne). Par la **forme** du lot,
oui : la longueur remplie L (plus long contexte du lot à ce pas) et la taille B entrent dans l'ordre des réductions ; l'essai
TL l. 150-165 le montre (une ligne voisine allongée de 40 jetons change les bits de la cible dès le deuxième pas), et le
module le déclare (docstring l. 9-11). Or la forme n'est **pas** exacte pour une ligne approchée :
- `forcee` (LOT l. 301-304) tronque ou complète par `pad_id` la reconstruction de base `notes + [fin par défaut]`
  (`reconstruire_episode` l. 126-130) à `jetons[t]` : pour toute action **non conforme en longueur** (c'est la définition
  d'une ligne approchée), le dernier jeton forcé est un jeton canonique (troncature) ou `pad_id` (complément), jamais la fin
  par défaut `c[0]` ;
- `FormatChat.cloture` (`formats.py` l. 91-93) rend `c[1:]` si le dernier jeton est `c[0]`, sinon `c` entier : le contexte
  de la ligne approchée aux actions suivantes est donc **un jeton plus long** que celui de P3 (dont l'action finissait par
  `c[0]` dans le cas courant), systématiquement, à chaque action non conforme ; l'écart inverse (−1) survient si la vraie
  fin de P3 n'était pas `c[0]` (rare : 1 épisode sur 22 dans la table v1). Le module le dit à demi (docstring l. 32-33 :
  « à un jeton de clôture près ») ; **le texte dit le contraire** (A2 l. 153-154 : « ne changent pas la forme du lot, donc
  pas les logits des autres lignes » ; l. 356 : « longueur forcée exacte »). Effet : dès qu'une ligne approchée est la
  plus longue du lot à un pas, L diffère de celui de P3 et HG-4 ne tient plus pour ce pas. Les lots 0 et 24 ont 2 et 3
  lignes approchées (A2 l. 351-352).
- L'essai TL l. 127-144 ne couvre pas ce cas : la ligne approchée y est la plus longue **en jetons générés**, pas
  nécessairement en contexte ; `logits_conformes` y est vrai par chance de forme. L'essai des 7 lignes (l. 172-173)
  n'affirme rien sur `logits_conformes`.
- **Correction de code, simple** : pour une ligne approchée avec `a_fin = 1`, forcer `notes[:jetons_notes]` complété à
  `jetons_notes`, **puis la fin par défaut à la dernière place** (la clôture redevient `c[1:]` comme chez P3, sauf vraie fin
  non par défaut) ; et **mesurer** après coup, par pas, si la longueur remplie est fixée par une ligne approchée
  (`plans[t]["longueurs_contextes"]`, l. 376, et `lot[].source` suffisent) : « pas où L est fixé par une ligne approchée »
  = 0 ⇒ forme exacte prouvée pour la cible. Essai R5 : ligne approchée la plus longue du lot → mêmes bits après
  correction ; même ligne avec un jeton de contexte en plus → bits différents déclarés.

**(c) L'essai « égal au bit près » est-il sur le chemin de l'instance ?** Non, et le texte le dit (HG-4, l. 155-156) : la
référence et le rejeu sont calculés dans le même processus, sur processeur, en **float32** (modèle minuscule chargé
`dtype=torch.float32`, TG l. 105), sans carte, sans `sdpa` CUDA ni bfloat16. L'essai prouve la **recopie de la suite
d'appels** (mêmes formes, mêmes passes, mêmes conversions : TL l. 86-102, nombre de passes égal à celui du harnais l. 98),
non la reproductibilité au bit sur A100 en bfloat16, qui dépend des noyaux déterministes de `regler_determinisme`
(TF32 coupé, algorithmes déterministes) et de la même version de torch/cuDNN : c'est ce que mesure l'accord des lignes
voisines (P-G4), à condition qu'il soit codé (ci-dessous).

**(d) Écarts entre A2 et le code du lot au commit `99022f43`** (le n° 267 annonce des corrections ; à vérifier au commit
final) :
1. **Cibles du lot** : A2 l. 237-239 et 349 (« pris parmi les 4 non résolus de la table v2 ; un épisode de C-6 non résolu
   à l'étape 1 n'est pas une cible ») ; le code prend **tous** les non résolus de l'étape 1 (`episodes_de_l_etape`, LOT
   l. 628-637), un épisode de C-6 compris. À restreindre dans le code (sinon le texte ment), ou à écrire tel quel.
2. **Validation du lot** : A2 l. 240-242 et 359-360 (« mesurée sur les lignes résolues des mêmes lots, sans passe de plus,
   sans seuil ») : **non codée**. Le code a une étape `validation-lot` à part avec seuil et condition « atteint » (LOT
   l. 602-613, 778-786), que le texte supprime. Pour mesurer l'accord des lignes forcées il faut, par ligne voisine et par
   pas joué, `softmax(logits[r]) / q_r` avec les tirages du générateur de **cette** ligne (une graine par action, comme
   P3) : `generer_lot_fidele` ne calcule rien pour les lignes forcées (l. 261-264). Essai R5 à écrire : lignes exactes →
   accord 1 exactement sur processeur ; graine fausse sur une voisine → accord ≈ Σ p² ; c'est la seule preuve de HG-4 sur
   la carte.
3. **Repli** : A2 l. 358 (« le repli itératif ci-dessus ») ; le code du lot a le repli à deux bascules du brouillon 1
   (LOT l. 444-473), avec le défaut VG-02.
4. **Budget par épisode (900 s)** : non codé (l'échéance de l'étape lève `GardeArret` et arrête tout, LOT l. 115-116,
   698-699) ; résultat consigné par épisode : non codé (tout est écrit à la fin, l. 753-783).
5. **Fusion du lot dans la table v3** : non codée (A2 l. 371-372 le dit).
6. `ChoixCible` : `ecart` et `marge` calculés depuis les valeurs float32 de p / q (l. 124-125, 157-158), non depuis les
   logits : cohérent avec « l'opération même de P3 », bien.

**(e) Essais rejoués ici** (copie du bloc-notes au commit `21a6e583` + les deux fichiers de `99022f43`, `.venv` gelé, réseau
coupé) : `PYTHONPATH=src nice -n 10 python -m pytest -q -p no:cacheprovider tests/test_resolution_graine_lot_v1.py -rs` →
**`3 passed, 6 skipped in 94.62s`** (code 0). Passés : plan des lots, gardes de configuration, **bout en bout jouet**
(validation-lot, résolution-lot, lignes `resolution_v1` revérifiées par l'empreinte, identifiants faux refusés). Sautés,
motif « tokeniseur de Llama 3.1 introuvable » : logits au bit, cas sain 8 et 4, lignes approchées, lot recomposé, graine
fausse et texte altéré, repli. Les « 9 essais » du n° 267 sont donc attestés pour 3 ici ; les 6 autres restent à la charge
du vérificateur neuf ou de l'instance.

## 3. Points neufs du brouillon 2 : chiffrés, écrits d'avance, essayés (R5) ?

| Point neuf | Chiffré | Écrit | Essayé (cas sain + artefact) |
|---|---|---|---|
| Repli itératif à deux niveaux (l. 287-295) | oui (16, 2, 136) | oui, règle claire ; « l'ordre exact est celui du code » : à comparer par la contre-lecture | non codé ; essai exigé l. 408 (« seconde erreur dans une autre action ») ✓ annoncé |
| Budgets 600 / 900 s, étapes 2 400 / 3 600 s, délais, plafond 200 min (l. 234-236, 390-393) | oui, cohérents | oui | non codé ; essais exigés l. 409 ✓ |
| Consignation par épisode (l. 190-191) | — | oui | non codé ; à essayer : coupure (TERM) après k épisodes → résultat partiel scellé, k épisodes présents (absent de la liste l. 407-413) |
| Lot fidèle, étape 1 bis (l. 347-363) | oui (16 combinaisons, 900 s, 3 600 s, lots 0/5/14/24) | oui | code `99022f43` : 9 essais (3 passés ici, 6 sautés) ; **manquent** : validation du lot (2.d.2), ligne approchée fixant L (2.b), budget du lot, cible restreinte aux 4 |
| HG-4 et P-G4 (l. 151-156, 183-186) | oui (0,999 prédit ; 0,99 lu) | oui | la partie « lignes approchées sans effet sur la forme » est **fausse** (2.b) ; la mesure de P-G4 n'est pas codée |
| Contrôle croisé à trois valeurs (l. 343-345, 432-433) | — | oui | non codé ; essai exigé l. 410 ✓ |
| Gardes avancées VG-04 (sceaux de toutes les pièces avant l'installation, agent = manifeste de P3, noyau « defaut » seul) (l. 442-453) | — | oui | non codé ; essai exigé l. 412-413 ✓ |
| CUDA, pilote, cuDNN → réserve (l. 320-322, 468-469) | — | oui | essai exigé l. 413 ✓ |
| Table v3 scellée, fusion du lot (l. 365-373) | — | oui | non codé ; essai exigé l. 411 ✓ |
| Volumes et durée de P3 (l. 111, 271-272) | oui | oui | R6 : aucun chemin ni empreinte pour le script qui a compté 4 143 855 jetons et 309 797 pas (mineur) |
| Pire cas 4,1 USD (l. 393) | 200 min × 1,22 | oui | le taux est celui des offres du jour, non un plafond de filtre : écrire le prix plafond du filtre de location (mineur) |

## 4. Ce qui reste bloquant pour le scellement (liste exacte)

- **B-2 (reconduit)** — unité de `balayages_max` et nombre de U+FFFD par épisode (7 et 147) ; A2 l. 211, 233, 299-301,
  431 ; code RG l. 292, 428-433 et LOT l. 133-138 (même compte). Tant que l'unité est « pas à moins de 128 caractères d'un
  U+FFFD », un épisode à trois U+FFFD est déclaré « non inversible » sans avoir rien balayé.
- **B-L1** — HG-4 et l. 153-154, 356 affirment une propriété fausse des lignes approchées (clôture : +1 jeton de contexte
  après chaque action non conforme, 2.b). Correction minimale : texte (déclarer l'écart de forme, et la mesure « pas où L
  est fixé par une ligne approchée ») ; correction recommandée : code (`forcee` avec la fin par défaut en dernière place)
  et essai R5 ; sans elle, P-G4 et HG-4 sont indécidables sur les lots 0 et 24.
- **B-L2** — texte et code du lot ne décrivent pas la même chose sur trois points (2.d.1 à 2.d.3 : cibles restreintes
  aux 4, validation du lot sans étape ni seuil, repli itératif) et la mesure qui fonde le seuil de lecture 0,99 (accord
  des lignes voisines) n'existe pas ; à aligner au commit final, chaque point avec son essai.
- **I-A** — C-3 (5) : écrire l'interdit R3 « une seule exécution de chaque étape sous ce texte ; toute reprise (réglages,
  lot) sous un texte neuf ».
- **I-B** — C-3 (3) : la classe de la validation (et la réserve du lot) recopiée dans le résultat de la résolution, du lot
  et dans la table v3 (sinon une table bâtie sous réserve se lit comme les autres).
- **I-C** — C-4 / R-14 : exposition du dépôt privé et des jetons hors centre de données : déclarée et soumise à Lazar ;
  filtres d'offre écrits (pilote compatible CUDA 13.0, débit, fiabilité, prix plafond).
- **I-D** — C-5 / I-2 / I-4 : accord calculé aussi pour les non résolus ; « accord attendu sous graine indépendante »
  (moyenne de p_k) et « pas informatifs » écrits au résultat ; formule de l. 167 corrigée.
- **I-E** — C-9 / I-6 : P-G3, chemin et empreinte des mesures en bfloat16, ou retrait des chiffres.
- Mineurs reconduits : m-1 (R-05), m-6 (R-18), m-7, garde de l'étape table (R-11), parenthèse fausse de l. 431,
  « cas non simple » → « budget de balayages dépassé », essais manquants de C-8 (citation de la configuration sous ses
  deux libellés, texte attendu de l'ouverture, coupure après k épisodes), R6 des volumes, prix plafond.

## 5. Couples « remplacer / par » restants (A2, brouillon 2)

**R2-01 — l. 153-154 (HG-4).**
Remplacer : « les lignes voisines approchées (découpage canonique à longueur forcée exacte) ne changent pas la forme du
lot, donc pas les logits des autres lignes. »
Par : « les lignes voisines approchées ont le nombre exact de jetons générés par action, et la fin par défaut à la
dernière place quand P3 a compté une fin ; leur contexte ne diffère de celui de P3 que si la vraie fin de P3 n'était pas
la fin par défaut (un jeton) ; les logits de la cible ne dépendent des autres lignes que par la forme du lot (taille et
longueur remplie) ; le nombre de pas où la longueur remplie est fixée par une ligne approchée est mesuré et rapporté
(0 = forme exacte prouvée pour la cible). »

**R2-02 — l. 356.**
Remplacer : « approchées (découpage canonique à longueur forcée exacte, jeton de fin par défaut ; **déclarées et
comptées**, lot déclaré « approché ») »
Par : « approchées (découpage canonique tronqué ou complété au nombre de jetons notés, puis la fin par défaut si P3 a
compté une fin ; **déclarées et comptées**, lot déclaré « approché » ; pas où elles fixent la longueur remplie comptés) »

**R2-03 — l. 233.**
Remplacer : « `balayages_max` = **64** balayages du vocabulaire par épisode pour les octets que recouvre un U+FFFD ; »
Par : « `balayages_max` = **N** par U+FFFD (unité : pas où la recherche de candidats couvre des octets inconnus, c'est-à-dire
où `commencant_par` est appelé avec un ensemble non vide, et non tout pas à moins de 128 caractères d'un U+FFFD) ; nombre
de U+FFFD par épisode, pour les 7 et les 147 : … (processeur, textes seuls, chemin et empreinte) ; »

**R2-04 — l. 431, parenthèse.**
Remplacer : « Cause « caractère de remplacement : cas non simple », sans réserve de validation ni de lot = **non inversible
déclaré** (le texte stocké n'est pas l'image exacte des jetons) »
Par : « Cause « caractère de remplacement : budget de balayages dépassé », sans réserve de validation ni de lot = **non
inversible déclaré par la méthode** (budget de recherche épuisé, non preuve d'impossibilité : le jeton de P3 reste dans
l'ensemble contraint à chaque pas) »

**R2-05 — l. 237-239 (cibles du lot), ajout.**
Après « (au plus 4 ; un épisode de C-6 non résolu à l'étape 1 n'est pas une cible, son entrée de C-6 est déjà prouvée par
l'empreinte) », ajouter : « — restriction appliquée par le code (`episodes_de_l_etape`, étape `resolution-lot` : les non
résolus de l'étape 1 **intersectés** avec les entrées `non_resolu` de la table v2), essayée (un épisode de C-6 non résolu
demandé au lot → refusé, cause écrite) ».

**R2-06 — l. 359-360 (validation du lot).**
Remplacer : « accord du choix non contraint de chaque ligne forcée avec son jeton connu, aux pas joués ; **sans arrêt**. »
Par : « accord du choix non contraint de chaque ligne forcée avec son jeton connu, aux pas joués, calculé pendant les mêmes
passes avec les tirages exponentiels du générateur de **cette** ligne (une graine par action, dérivée comme pour la
cible) ; moyenne et par ligne ; **sans arrêt** ; essais : lignes exactes → accord 1 exactement sur processeur ; graine
fausse sur une ligne voisine → accord qui tombe vers Σ p² ; »

**R2-07 — l. 168-169 (R3) et liste d'arrêt, ajout.**
Après « (R3 : rien n'est relancé pour les atteindre). » ajouter : « **Une seule exécution de chaque étape (0, 1, 1 bis, 2)
sous ce texte** ; toute reprise avec d'autres réglages, un autre plan de lot ou un autre code relève d'un texte neuf,
scellé et contre-lu. »

**R2-08 — l. 259, ajout.**
Après « rien ne s'arrête. » ajouter : « La lecture de la validation (« validées », « réserve graines ou précision »,
« fragilité ») et celle du lot (« fidèle », « réserve lot non fidèle ») sont **recopiées** dans le résultat de la
résolution, dans celui du lot et dans la table v3 (clé `lecture_validation`), pour que la table porte sa réserve. »

**R2-09 — l. 167.**
Remplacer : « (une graine fausse ferait tomber cet accord vers la probabilité du jeton le plus probable, typiquement 0,6 à
0,85) »
Par : « (sous une graine indépendante, l'accord attendu à chaque pas est la probabilité p_k du jeton connu sous la passe,
en espérance Σ p² : cette valeur est calculée sur les mêmes passes et rapportée (`accord_attendu_graine_independante`),
avec l'accord sur les pas informatifs, où le jeton connu n'est pas l'argmax des logits) »

**R2-10 — l. 323-325 (location).**
Remplacer : « **ce seul critère est retiré**, et ce retrait est consigné au journal et au résultat (déclaré). »
Par : « **ce seul critère est retiré**, et ce retrait est consigné au journal et au résultat (déclaré) ; **conséquence
déclarée** : l'hôte, non vérifié comme centre de données, reçoit le clone du dépôt de travail privé et les deux jetons
(GitHub à grain fin en écriture sur ce seul dépôt, Hugging Face en lecture) — nœud « compte, dépôt distant » soumis à
Lazar : … ; les autres filtres restent : A100-SXM4-80GB, pilote compatible CUDA 13.0, débit descendant ≥ …, fiabilité ≥ …,
prix ≤ … USD/h (ce plafond entre dans le pire cas). »

**R2-11 — l. 25-26 (ordre des modes).**
Remplacer : « il est ici l'**étape 1 bis** (« lot fidèle »). »
Par : « il est ici l'**étape 1 bis** (« lot fidèle »), **après** la passe forcée : écart déclaré à l'ordre accepté au
n° 352 (lot en premier) ; raison : la passe forcée coûte moins d'une minute par épisode et résout la majorité des cas ; le
lot, 3 à 5 minutes par essai, ne sert qu'aux restes ; l'arbitre (empreinte) est le même. »

**R2-12 — l. 180-182 (P-G3).**
Remplacer : « Mesure sur le modèle minuscule en bfloat16 (essais du code de base) : »
Par : « Mesure sur le modèle minuscule en bfloat16 (script `…`, sortie `…`, empreintes ; les essais du code tournent en
float32) : » — ou retirer les trois chiffres.

**R2-13 — l. 329-332 (aveugle).** Le couple R-05 du brouillon 1, inchangé.

**R2-14 — l. 461-465 (chaîne des étapes), ajout.** « ; étape table sans contrôle croisé « conforme » dans le résultat de
l'étape 1 ».

**R2-15 — l. 407-413 (essais exigés), ajout.** « ; citation de la configuration sous ses deux libellés (texte sans l'un
d'eux → arrêt) ; texte attendu de l'ouverture (absent → arrêt) ; coupure (TERM) après k épisodes → résultat partiel scellé
avec k épisodes ; ligne approchée la plus longue du lot → mêmes bits que la ligne exacte après correction de `forcee` ».

## Annexe — ce que j'ai fait et pas fait

- Lecture par `git show` seulement ; essais du lot rejoués dans la copie du bloc-notes
  (`/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/copie-21a6e583/`, les deux fichiers de
  `99022f43` copiés à l'octet, empreintes `9acdd228…` et `4645f9bc…` revérifiées), sortie `pytest-lot.txt` du bloc-notes.
- Aucun `git fetch`, `checkout`, `switch`, `worktree`, `stash`, `reset` ; aucun commit, aucun `.sha256`, aucun fichier
  existant modifié ; rien sous `donnees/` ; aucun appel de réseau (cache Hugging Face coupé) ni de modèle ; `nice -n 10`.
  Un seul fichier neuf : celui-ci, à sceller par la session.
