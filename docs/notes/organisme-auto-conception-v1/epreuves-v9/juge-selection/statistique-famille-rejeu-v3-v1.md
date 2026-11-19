# Statistique de famille du rejeu à blanc v3 des critères de sélection, course v9 — v1

- **Auteur** : modèle L′, neuf ; je n'ai écrit ni les critères v3, ni aucune lecture, ni aucune carte. Mandat de la mère (R-3883), d'après la recommandation 4 de l'audit de symétrie `audit-symetrie-rejeu-v2-v1.md` (sha256 `ff814fc980925ea4304c2a784c20e41378fc11d92b2b08d3eb835a71451d4673`). Écrit le 2026-11-19 (`date -u` : 2026-11-19T14:45:21Z). Hors ligne, processeur seul, aucune dépense, aucun appel de modèle.
- **Scellé avant l'ouverture des lectures v3.** Ce texte et son programme fixent la statistique, ses entrées et sa règle de lecture. Ils ne se changent pas après lecture d'une sélection v3 ; une version nouvelle prend un nom nouveau (règle R12).
- **Ce texte ne choisit rien et ne revendique rien.** Il dit quand la famille des lecteurs est plus, ou moins, présente qu'à sa part de base. Un signal déclenche l'audit de la règle R4 ; il ne décide de rien sur aucune carte.

## 0. Pièces lues, et ce qui ne l'a pas été

| pièce | ce que j'en ai lu | sha256 |
|---|---|---|
| `…/juge-selection/audit-symetrie-rejeu-v2-v1.md` | en entier | `ff814fc980925ea4304c2a784c20e41378fc11d92b2b08d3eb835a71451d4673` |
| `…/juge-selection/audit_symetrie_rejeu_v2_v1.py` | en entier (structures, graines, test de permutation) | `52cabc0df8d079991f0a95dd39788291de5b0995a5bffc380bbfa2415190e5c0` |
| `…/juge-selection/selections-rejeu-a-blanc-criteres-v2-lecteur-f-v1.json` | clés et types seulement | `e42b5f05d0f9b2c8423fc0d005e5d5c414c1023208e049201074ecf91ec69fc6` |
| `…/juge-selection/selections-rejeu-a-blanc-criteres-v2-lecteur-o-v1.json` | clés et types seulement | `8bd435b98f1b81abf3a4e201977b2b1bf9a72cbe464dfb9127243d1a93e0b7d3` |
| `…/juge-selection/rejeu-a-blanc-criteres-v2-lecteur-o-v1.md` | en-tête et titres (format des sélections) | `209243b73e34c0aaac5ca2b1ef77c972d855eb09804db7d4f01390d16b13674f` |
| `…/juge-selection/criteres-choix-cartes-v9-v3.md` | § 0 à § 11 (définitions des listes, du veto, des voies) ; aucune modification | `1ce419031644eac6060378ed283bdd2966477d6d444fa54637f8866b4ee01b6e` |
| `docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json` (configuration de la course v9) | `especes` : étiquettes des proposeurs | `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8` |
| code de l'orchestrateur, commit `a41b7b50` (celui de la configuration v5), `orchestrator/pole/course2_v54.py` | la ligne qui écrit l'espèce dans `meta` ; l'écriture de `fiches.json` (`course2_v56.py`) | `ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342` |

**Non lus** : `fiches.json` (ni ouvert, ni passé au programme : seuls ses clés et son empreinte, `ba65c411…`, viennent de l'audit et du code de l'orchestrateur), le champ `meta` de toute carte, toute carte, toute sélection v3, `diag/`, `donnees/`, le bras d'attaque, les archives de réponses, la conservation des réponses, `.claude/`, le coffre. Le programme n'a tourné que sur des données synthétiques (§ 8).

**Structure d'un enregistrement de `fiches.json`** (audit, § 1 ; code de l'orchestrateur, `course2_v56.py` : `{f["ident"]: {"contenu", "empreinte", "meta"}}`). L'espèce est écrite dans `meta`, clé `proposeur`, par `f["meta"]["proposeur"] = p["etiquette"]` (`course2_v54.py`). Les étiquettes de la configuration v5 sont `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra`, `prop-carbon` (et `prop-kimi`, absente de la v9). **Réserve** : je ne l'ai pas vérifié sur le fichier, que je n'ouvre pas. Si la clé manque ou porte une autre valeur, le programme ne devine rien : une étiquette hors table est un refus ; une clé absente est comptée « sans espèce » et rend toute lecture non concluante (§ 5).

## 1. Objet

Rendre exécutable la recommandation 4 de l'audit : la part de la **famille des lecteurs** parmi les cartes à la note maximale, dans le nombre visé et au veto, comparée à sa part de base, avec un test de permutation de l'étiquette d'espèce stratifié par voie. Elle est rapportée **pour chaque lecteur v3 et pour l'assemblage**. La couverture est complète : l'espèce de chacune des 94 cartes est lue par programme, après le dépôt des lectures, au lieu des 62 étiquetées de l'audit.

## 2. Entrées

1. **Cartes** : `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json`, sha256 `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`. Le programme refuse tout autre fichier, sauf en mode d'essai synthétique ; la sortie porte alors « sans valeur ».
2. **Une sélection par ensemble**, aux noms fixés ici :
   - `F` : la lecture du lecteur F ;
   - `O` : celle du lecteur O ;
   - `programme` : celle du lecteur par programme ;
   - `assemblage` : l'assemblage par programme.

   Les chemins et les empreintes sont passés en argument ; les noms de fichiers restent à paramétrer. Deux ensembles peuvent venir du même fichier. Un ensemble absent est rapporté « sans objet ».
3. **Une correspondance**, écrite par la mère **après le dépôt des lectures et avant de lancer ce programme**, scellée, empreinte passée en argument. C'est un JSON `{"piece", "ecrite_utc", "ensembles": {NOM: {…}}}`. Elle ne nomme que des **clés** des fichiers de sélection, jamais un identifiant de carte. Pour chaque ensemble :
   - `cartes` : pointeur (« a/b/c ») vers la liste des enregistrements par carte, ou vers un objet `{identifiant: enregistrement}` ;
   - `id` : clé de l'identifiant dans un enregistrement (null pour un objet) ;
   - `voie` : clé de la voie ; une valeur nulle dit « non notée » ;
   - `note` : clé de la note définie au § 3 ; une valeur nulle dit « non notée » ;
   - `exclue` (facultatif) : clé booléenne, ou liste des cas d'exclusion ;
   - `nombre_vise`, `veto` : null, ou `{"liste": pointeur, "id": clé}`, ou `{"liste": pointeur}` (liste d'identifiants), ou `{"drapeau": clé booléenne}`.

   Toute autre clé est refusée. Une clé exigée qui manque dans un enregistrement est un refus, jamais une carte « non notée » en silence.

   Exemple sur le format de la sélection v2 du lecteur O, à titre d'illustration seulement : `{"cartes": "cartes_notees", "id": "id", "voie": "voie", "note": "total", "exclue": "excl", "nombre_vise": {"liste": "variantes/A/retenues"}, "veto": {"liste": "veto_declare/liste", "id": "id"}}`.
4. **Ce que le programme lit des cartes** : la seule clé `meta` → `proposeur`, et les identifiants (clés de premier niveau). Preuve par le code :
   - une seule fonction touche aux enregistrements, `extraire_especes`, et n'y fait que deux accès : `rec["meta"]` puis `meta["proposeur"]` ;
   - tout autre chemin est refusé (`CHEMIN_ESPECE` constant) ;
   - l'objet entier est supprimé (`del fiches`) aussitôt l'extraction faite.

   Le décodage du JSON parcourt le fichier entier : c'est inévitable, mais aucune autre valeur n'est ensuite lue. Un essai à enregistrements espions le vérifie (§ 8). La sortie ne porte **que des comptes** : ni espèce par carte, ni identifiant, ni texte.
5. **Empreintes** : toutes les entrées (cartes, correspondance, sélections) sont vérifiées **avant toute lecture**. Un écart à l'empreinte passée est un refus, et rien n'est calculé.

## 3. Définitions

- **Lignées** : Opus, Fable, Argon, Astra, Carbon (étiquettes `prop-…` du § 0). **Famille des lecteurs** : Opus et Fable. Les deux lecteurs v3 sont de ces lignées (critères v3, § 1).
- **Population d'un ensemble** : les cartes **notées** de cet ensemble, c'est-à-dire non exclues, avec une voie et une note.
- **Note** : celle qui fait la première clé du rang dans la pièce, critères v3, § 10.
  - Pour une lecture seule, la note fine de ce lecteur, sur les items qu'il garde. Si la pièce n'en porte pas, la note qui fait son rang, écrite comme telle dans la correspondance.
  - Pour l'assemblage, la note fine sommée.
  - Pour le lecteur par programme, la note qu'il rend (D, s'il ne rend que D).
- **Les trois listes** :
  - **note maximale** : les cartes de la population dont la note égale la plus haute **observée** dans l'ensemble (à 10⁻⁹ près) ;
  - **nombre visé** : les cartes porteuses des lignes du nombre visé ;
  - **veto** : les listes de veto **telles que déposées**, avant le retrait par lignée du § 8 des critères v3, titulaires seulement, sans les suppléantes. Pour l'assemblage, la réunion des listes des titulaires.

  Un identifiant en double est retiré et compté. Une carte de liste hors de la population est comptée « hors population » et sortie du test. Un identifiant inconnu des 94 est un refus.
- **Strate** : la voie de la carte dans l'ensemble (I, P, N, ou ce que rend le lecteur par programme). Une carte que l'assemblage met dans deux voies forme la strate « I|P » (voies triées, jointes).
- **Statistique**, pour une liste L de n cartes, dont k de la famille :
  - part p_L = k / n ;
  - base sur 94 = cartes de la famille / cartes d'espèce connue des 94 (attendu : 37 / 94) ;
  - base parmi les notées = part de la famille dans la population ;
  - écarts p_L − base, pour chacune des deux bases.
- **Test** : permutation de l'étiquette de famille **à l'intérieur de chaque voie** de la population, **20 000 permutations**. Les effectifs de la famille par voie restent ceux observés, à chaque permutation.
  - Statistique de test : T = k − E, où E = Σ_v n_v · F_v / N_v est l'attendu stratifié. Ici n_v est le nombre de cartes de la liste dans la voie v, F_v le nombre de cartes de la famille dans la voie v, N_v l'effectif de la voie.
  - p bilatérale = (1 + #{|T*| ≥ |T|}) / 20 001 ; les deux p unilatérales sont rapportées.
  - La permutation garde la base fixe : le même p vaut donc pour les deux bases.
- **Contrôle exact** : la loi exacte de k sous le même nul, qui est la convolution des lois hypergéométriques par voie. Elle donne la p exacte bilatérale, avec le même critère, et la **p minimale atteignable**, la plus petite p que les effectifs permettent.
- **Graines (règle R9)** : `numpy.random.SeedSequence(int(sha256(b"statistique-famille-rejeu-v3-v1"), 16))`, soit l'entropie 925961801580951929512497721206609076062388465257187361765833090784703907333. `spawn(4)` ; l'enfant k sert l'ensemble k dans l'ordre F, O, programme, assemblage, quels que soient les ensembles présents. `Generator(PCG64(enfant))` ; un `permuted` par voie, voies triées. numpy 1.25 au moins (vérifié par le programme). La sortie porte l'entropie, la version de numpy, l'empreinte du programme et celles des entrées.
- **Par lignée** (Opus, Fable, Argon, Astra, Carbon) : dans chaque liste, le nombre, la part, les deux parts de base et les deux écarts. **Descriptif, sans test**, et sans place dans la règle de lecture.

## 4. Ce qui est rapporté

Pour chaque ensemble :
- les cartes de la sélection, les non notées, la population et sa famille ;
- les deux bases ;
- la valeur de la note maximale ;
- la population et sa famille par voie.

Pour chaque liste :
- n déposé, doublons retirés, hors population ;
- n, k et la part ;
- les deux écarts, l'attendu stratifié et T ;
- la répartition par voie ;
- les trois p de permutation, la p exacte et la p minimale atteignable ;
- le descriptif par lignée ;
- la lecture du § 5.

Comptes globaux : par lignée sur les 94, cartes sans espèce, conformité aux totaux de la pièce `especes-et-originalite-cartes-v9-v1.md` (`2af9e67f…`, § (a) : Opus 22, Fable 15, Argon 21, Astra 20, Carbon 16).

## 5. Règle de lecture, écrite d'avance

1. **Non concluant**, avant tout test, si l'une de ces conditions est vraie :
   - les comptes par lignée des 94 cartes diffèrent de la pièce `2af9e67f…` (le champ lu n'est peut-être pas l'espèce) ;
   - une carte de la population ou de la liste est sans espèce ;
   - la liste compte moins de 3 cartes dans la population ;
   - la famille est absente de la population, ou seule ;
   - la liste est la population entière ;
   - la p minimale atteignable dépasse 0,05 : les effectifs ne permettent pas de voir un écart.

   Une liste non concluante ne se lit ni « présent » ni « absent ».
2. **Correction** : de Holm, au seuil de 0,05, sur l'ensemble des tests restants (au plus 4 ensembles × 3 listes). Elle s'applique aux p de permutation, et séparément aux p exactes.
3. **Signal présent** : la p de permutation et la p exacte sont toutes deux ≤ 0,05 après Holm. Le sens est rapporté : famille des lecteurs sur-représentée (T > 0) ou sous-représentée (T < 0).
4. **Absent** : les deux sont > 0,05 après Holm. Une p de permutation brute ≤ 0,05 est signalée comme indice, sans autre effet.
5. **Non concluant** aussi quand la permutation et le calcul exact tombent de part et d'autre du seuil après Holm.
6. **Ce qu'un signal présent fait** : il déclenche l'audit de la règle R4, **dans un sens comme dans l'autre**, avec le même soin. Il ne décide de rien sur aucune carte, ne change aucune liste, aucun rang, aucun veto, et ne fonde **aucune revendication**. Un signal « absent » ne vaut pas preuve d'absence de préférence.
7. Le seuil de 0,05, le minimum de 3 cartes et la correction de Holm sont des choix de conception, à confirmer par la mère. Ils ne sont tirés d'aucune source.

## 6. Ce que cette statistique ne dit pas

- **Elle ne mesure pas un biais.** Elle n'a aucune référence de qualité extérieure aux lecteurs : un écart peut venir de ce que les cartes d'une famille seraient meilleures selon les critères. C'est la réserve du § 12 des critères v3 sur la matrice juge × auteur, qui se lit à auteur fixe et juge changé.
- **Elle ne sépare pas la préférence pour soi d'une manière d'écrire** propre à la famille, que les critères récompenseraient. Elle ne sépare pas non plus la reconnaissance du style de la préférence. Deux lecteurs d'une même famille ne le peuvent pas (audit, § 7) ; le lecteur par programme sert de témoin sans famille, non d'arbitre.
- **Elle ne dit rien de la lignée** au-delà du descriptif : aucun test par lignée, effectifs trop petits.
- **Le veto** se compare ici à la population des notées, non aux « cartes non retenues ». Le § 8 des critères v3 demande cette autre mesure, la part de sa propre lignée, au programme d'assemblage. Les deux ne se remplacent pas.
- **Rien hors de la v9.** Une course, et des lecteurs qui ont lu les rejeux v2. Les listes ne sont pas indépendantes entre ensembles : l'assemblage dérive de F et O. Holm le tolère, mais les verdicts ne s'additionnent pas.
- **Elle ne remplace pas** la mesure de reconnaissance déclarée (audit, recommandation 5), ni le masquage du style (recommandation 3).

## 7. Commande exacte que la mère lancera

Après le dépôt et le scellement des trois lectures v3 et de l'assemblage, puis l'écriture et le scellement de la correspondance (§ 2, point 3), depuis la racine du dépôt :

```
D=docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection
(cd $D && sha256sum -c statistique_famille_rejeu_v3_v1.py.sha256 statistique-famille-rejeu-v3-v1.md.sha256)
FICHES=archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json
/usr/local/bin/python3 -B -I $D/statistique_famille_rejeu_v3_v1.py \
  --fiches "$FICHES" --sha-fiches ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481 \
  --correspondance $D/<CORRESPONDANCE>.json --sha-correspondance <SHA_CORRESPONDANCE> \
  --selection F $D/<SELECTIONS_F>.json <SHA_F> \
  --selection O $D/<SELECTIONS_O>.json <SHA_O> \
  --selection programme $D/<SELECTIONS_PROGRAMME>.json <SHA_PROGRAMME> \
  --selection assemblage $D/<ASSEMBLAGE>.json <SHA_ASSEMBLAGE> \
  --sortie $D/statistique-famille-rejeu-v3-sortie-v1.json \
  --resume $D/statistique-famille-rejeu-v3-resume-v1.md
```

- Les `<…>` sont les noms des fichiers déposés et leurs empreintes, recopiées de leurs compagnons `.sha256`.
- Le programme écrit la sortie et le résumé avec leurs compagnons `.sha256` et refuse d'écraser (R12).
- Il rend le code 2 et le motif sur tout refus, sans rien écrire.
- Il imprime les verdicts.
- Ne pas passer `--essai-synthetique` sur la vraie course.

## 8. Essais (données synthétiques seulement)

`tests/test_statistique_famille_rejeu_v3_v1.py` fabrique 94 cartes inventées, avec les totaux par lignée de la pièce. La famille est répartie 10/20, 20/50 et 7/24 dans les voies I, P et N. Les cartes portent des champs `contenu` et `meta` à valeurs sentinelles. **29 essais, 29 passés** ; sortie : `statistique-famille-rejeu-v3-essais-sortie-v1.txt`.
- **Cas sain** : listes à la part exacte de la famille dans chaque voie, donc T = 0, p = 1 et verdict « absent ». Un nul aléatoire donne p > 0,05 sur les trois listes.
- **Artefact** : un signal est planté dans les deux sens (famille seule, puis hors famille seule, à la note maximale, au nombre visé et au veto). Il donne p < 0,01 en permutation comme en exact, « signal présent » et le bon sens ; le lecteur par programme, au format objet, aussi.
- **Refus d'empreinte** : sur une sélection (code 2, rien d'écrit), sur des cartes modifiées après le calcul de l'empreinte, sur des cartes qui ne sont pas celles de la v9 hors mode d'essai, et sur une empreinte illisible.
- **Refus de lire un autre champ** :
  - `contenu.titre`, `meta.fournisseur`, `meta`, un chemin trop long et `empreinte` sont refusés ;
  - un enregistrement espion montre que seules les clés `meta` et `proposeur` sont touchées, sans aucun parcours ;
  - une étiquette hors table est refusée ; une espèce absente est comptée ;
  - la sortie ne contient ni texte sentinelle, ni identifiant.
- **Stratification exacte** : à chacune de 5 000 permutations, l'effectif de la famille et le multiensemble des étiquettes sont gardés dans chaque voie. Les étiquettes bougent bien dans la voie. Une liste prise dans une voie reste dans le support hypergéométrique. Permutation et exact concordent à 0,01 près. Sous le nul, sur 200 jeux, la part de p ≤ 0,05 reste ≤ 0,10.
- **Divers** : petits effectifs « non concluant » (liste de 2 ; 3 cartes de famille dans la voie I, p minimale 0,21) ; totaux non conformes, donc tout « non concluant » ; Holm ; reproductibilité ; refus d'écraser ; quatre correspondances refusées ; identifiant inconnu refusé.

## 9. Fichiers

| fichier | rôle |
|---|---|
| `statistique-famille-rejeu-v3-v1.md` | ce texte |
| `statistique_famille_rejeu_v3_v1.py` | le programme (empreinte au compagnon `.sha256`) |
| `tests/test_statistique_famille_rejeu_v3_v1.py` | les essais synthétiques |
| `statistique-famille-rejeu-v3-essais-sortie-v1.txt` | la sortie des essais |
