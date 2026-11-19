# Vérification des corrections — bras A, côté moniteurs : moniteurs à modèle de langue v3, autres moniteurs v8, préparation des lectures v2, liste « sans interne » v8 — v1

**Conclusions, par pièce :**
- **Module des deux moniteurs à modèle de langue, version 3 : inscriptible.** Les corrections (a) et (b) sont faites comme je les ai écrites, avec leurs artefacts ; aucune lecture de score ne change. Banc : 76 mutations appliquées, 76 tuées, aucune survivante (la survivante de la version 2, la branche soudée non réencodable, est tuée).
- **Module des autres moniteurs, version 8 : pas encore : deux essais à ajouter, (i) et (j), sans changer le code** (partie 2). Les lettres (d), (f), (g), (h) sont faites comme je les ai écrites ; aucun calcul n'a changé depuis la version 7 (égalité à l'octet du fichier par unité) ; la permutation est un paramètre obligatoire, l'échange par paire est juste, ses deux gardes mordent et son essai de niveau tient ; la forme « rang » rend les mêmes aires. Mais deux mutations survivent au fichier entier et cachent un défaut que rien ne verrait :
  - **(i)** la lecture commune peut jouer la permutation libre tout en écrivant « échange par paire » dans ses réglages : aucun essai ne vérifie que la permutation demandée est celle qui est jouée ;
  - **(j)** des rangs pris sur toutes les doses à la fois, et non « pour son moniteur et sa dose », passent : l'essai des rangs ne porte que sur une dose.
  Les deux essais proposés sont écrits et éprouvés : sains sur la version 8, chacun tue sa mutation. Le module n'a pas à changer : la liste v8 resterait juste.
- **Préparation des lectures, version 2 : inscriptible.** Seul l'import change (module des moniteurs à modèle de langue, version 3). Banc rejoué : 27 mutations, 26 tuées ; la seule survivante est la garde redondante déjà relevée sur la version 1 (la demande est revérifiée à l'écriture).
- **Liste « sans interne » v8 : inscriptible.** Elle cite la version 8 (et la version 3, la préparation v2) pour tous les points des lots 14 et 16, porte mes corrections des points 10, 11, 24, 26, 27, 30, et aucun interne de moniteur.

Reste, hors du code : **la décision de fond sur la permutation** (libre par épisode ou échange par paire) est toujours à prendre par la mère et Lazar avant le scellement du texte ; les deux sont codées, justes et éprouvées. La réserve de cloisonnement sur les scores des moniteurs appris tient sous la forme « score » ; la forme « rang » l'atténue sans la lever (partie 5).

Qui : le même contre-lecteur que pour les pièces précédentes (Claude Opus 5.5 ; développeur : Claude Fable 5.2), lancé par la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, le 19 novembre 2026, de 14:20Z à 15:35Z.
- Pièces de classe B. Branche `claude/bras-a-habilite-developpeur-v1`, tête `e6a5d2b4`, code au commit `18f63f40`.
- Rien ouvert sous `diag/`, `runs/`, `donnees/` ni `docs/verdicts/`, ni aucun fichier « consigne-privee » ou « conception-ii-b ». Aucun résultat lu, aucun poids chargé, aucune dépense, rien commis, pas de suite complète.
- Tout est fait dans `opus-contre-lecture-bras-a/` du bloc-notes de la mère, dans un arbre propre tiré de `e6a5d2b4` (`arbre8/`) et deux copies pour les bancs (`arbre8m14/`, `arbre8m16/`). Chaque essai est joué avec `-p no:cacheprovider`, `--basetemp` et `TMPDIR` dans ce dossier.
- Refus d'outil : aucun.

Empreintes vérifiées à la tête `e6a5d2b4` :

| pièce | empreinte |
|---|---|
| `moniteurs_langue_v3.py` | `8e941d240bacb7ca889e68fe988bc2e6c7cd16968290dcee91893327baa620e8` |
| `autres_moniteurs_v8.py` | `61105129f58f5df590b033c183e7ab334f56a51cc03bb04e86ebdb52e6e53760` |
| `preparation_des_lectures_v2.py` | `6dfd2bfc6989bd8a90ec40648bda653f5f8383e157c3c521e6d9a488f582debd` |
| `pour-le-texte-du-bras-a-sans-interne-v8.md` | `6818d11dad154cbc1aaaaf7b3111cc86e0562846715f12195a2ad6f6f8fa4329` |

Les deux commits depuis `a32c4abb` n'ajoutent que des fichiers ; aucune version antérieure n'est touchée.

## 1. Les lettres (a), (b), (d), (f), (g), (h) : faites comme écrites

| lettre | ce qui est fait | essai | mutation |
|---|---|---|---|
| (a) spécification comparée à la table des moniteurs | `exiger_specification` (v3) : nom connu (chaîne, dans `MONITEURS`), cas du moniteur, puis jetons de fin égaux à ceux relevés quand ils le sont. C'est mon texte « après », à un détail près, sans effet : le contrôle de forme des jetons (liste non vide d'entiers) passe avant la comparaison | `test_specification_ecrite_a_la_main_comparee_a_la_table` : un seul jeton de fin, un jeton de trop, nom inconnu, nom non chaîne, mauvais cas, et sur le chemin où elle sert (`lire_avec_raisonnement` refuse le juge à un seul jeton) | 4 mutations, tuées |
| (b) balise soudée non réencodable | cinquième état `« écrite, soudée, non réencodable : imposée »`, dans `ETATS_IMPOSES` (règle de la balise absente) ; champ `jointure_de_la_coupe`, que l'imposition n'écrase pas ; compté par `compter` | `test_balise_soudee_non_reencodable_cinquieme_etat` (la coupe est remplacée par une coupe non réencodable sur le vrai tokeniseur) et `test_couper_non_reencodable_rend_vide_et_la_jointure_concatenee` (tokeniseur jouet) : état, score imposé, trace de la coupe, comptes, règle « anomalie » | 6 mutations neuves et la survivante de la v2, tuées |
| (d) ordre trié des identifiants opaques | `exiger_ordre_des_identifiants`, appelée à l'écriture (avant tout fichier) et à la lecture de la production | `test_production_hors_de_l_ordre_des_identifiants_refusee` : écriture refusée, rien d'écrit ; cas sain ; fichier réordonné, compagnons refaits, refusé à la lecture | 3 mutations (corps, appel à l'écriture, appel à la lecture), tuées |
| (f) valeur p de la famille | ligne ajoutée telle que je l'ai écrite : `assert r["valeur_p_pour_la_famille"] == r["valeur_p_haut"] != r["valeur_p_bas"]` | `test_permutations_perdues_comptees_et_deux_valeurs_p` | tuée (fichier entier : 1 failed) ; elle survivait en version 7 |
| (g) table tirée de l'entropie du bras, refusée de bout en bout | essai neuf : `lire_les_cinq` reçoit `tirer_la_table_opaque(cles, ENTROPIE)`, la refuse, et n'écrit rien | `test_table_a_entropie_du_bras_refusee_dans_la_lecture_commune` | tuée (fichier entier) ; elle survivait en version 7 |
| (h) forme fermée du manifeste de production | essai neuf : clé « condition » de plus, `engagement_de_la_table` retiré, et une liste au lieu d'un objet, tous refusés après un cas sain | `test_manifeste_de_production_a_forme_fermee` | tuée (essais visés) ; elle survivait en version 7 |

Liste fermée des états de la balise : la version 8 a les cinq états, et l'essai qui compare les deux listes passe.

## 2. Bancs de mutations rejoués

Méthode inchangée : une garde neutralisée ou un calcul altéré à la fois, sur une copie ; essais visés ; une survivante sur les essais visés est rejouée sur le fichier entier. Les copies sont restaurées et vérifiées à leurs empreintes (partie 6).

**Moniteurs à modèle de langue, version 3** (`mutations14v3.py`, sortie `banc14v3.txt`) : mon banc de la version 2 (67 mutations appliquées), plus 10 neuves sur (a) et (b) : nom connu, cas du moniteur, jetons de fin relevés (retirés, ou réduits à un sous-ensemble), cinquième état hors des imposés, cinquième état écrit comme une troncature, jointure de la coupe non gardée, écrasée par l'imposition, non comptée, cinquième état non compté. **76 appliquées, 76 tuées, aucune survivante.** Neuf ne s'appliquent pas, comme en version 2 : huit visaient des textes de la version 1, et la forme de la spécification de la version 2 est remplacée par les mutations (a).

**Autres moniteurs, version 8, et préparation des lectures, version 2** (`mutations16-v8.py`, sortie `banc16v8.txt`) : mon banc de la version 7 (17 mutations du module, 27 de la préparation ; la mutation décisive « permutation action par action » réécrite pour la branche libre), plus 29 neuves :
- (d) : corps de la garde, appel à l'écriture, appel à la lecture ;
- permutation sans défaut : corps de `exiger_permutation`, son appel par la lecture commune, son appel par les scores fixes ;
- échange par paire : jamais d'échange, toujours l'échange, chance de 0,3, épisode seul échangé aussi, échange sans retournement, un seul épisode de la paire retourné, paires formées sans le rang, paires formées par rang modulo 2 ;
- garde de la paire : ses trois conditions, son appel, son appel aussi pour la permutation libre ;
- câblage : la lecture commune passe toujours la permutation libre ; les deux réglages rendus (`permutation`, `unite_de_la_permutation`) ;
- forme « rang » : corps de `exiger_forme`, rang maximal des ex aequo, rangs sur les deux plis ensemble, rangs sur toutes les doses ensemble, forme « rang » écrite avec les scores, champs de la ligne écrite, interdiction d'écraser visant le fichier des scores quelle que soit la forme ;
- motif « tirages dégénérés » illisible.

**74 appliquées (47 sur le module, 27 sur la préparation), 68 tuées, 6 survivent au fichier entier** (`66 passed`) :
- **redondantes, sans défaut (4)** :
  - la garde de la ligne de score à la collecte, refaite à l'écriture du fichier (déjà relevée en version 7) ;
  - la garde de la demande dans `preparer`, refaite à l'écriture des demandes (déjà relevée en version 7) ;
  - l'appel de `exiger_permutation` dans `lire_scores_fixes` : la même garde est appelée par `_permuter`, avant tout calcul de valeur p, et la lecture commune l'appelle avant tout calcul ; l'essai la voit donc toujours ;
  - le contrôle des champs de chaque ligne dans `ecrire_les_scores` : les lignes y arrivent déjà fermées (la collecte est gardée ligne à ligne, et `rangs_dans_le_pli` construit les dix champs) ; c'est une seconde garde, qu'aucun chemin ne peut atteindre sans fausser le code.
- **avec défaut (2), corrections (i) et (j)** :
  - **la lecture commune passe toujours la permutation libre** (`a = (dose, plis, graines, registre, collecte, PERMUTATION_LIBRE, n_perm, n_tirages)`) : les 66 essais passent, car les réglages rendus nomment toujours la permutation demandée, et l'essai de bout en bout n'a pas de valeur p qui distingue les deux (avec 8 permutations sur les données factices, les valeurs p sont égales). Une erreur de câblage ferait donc lire la permutation libre sous le nom de l'échange par paire, sans que rien ne le voie ;
  - **rangs pris sur toutes les doses** (groupes par moniteur et pli seulement) : les 66 essais passent. Les aires ne changent pas (l'ordre dans un pli et une dose est gardé), mais le fichier ne dit plus ce que le texte promet (points 24 et 34 : « dans son pli, pour son moniteur et sa dose »), et les rangs mêlent les doses, pour un moniteur appris, des valeurs prises sous des modèles différents.

Les mutations sur ce que la version 8 ajoute de (d), de l'échange par paire, de la garde de la paire, des réglages rendus, de la forme et du motif des tirages sont toutes tuées ; (f), (g) et (h), qui survivaient en version 7, sont tuées.

**Correction (i), texte avant et après.** Avant : `test_lecture_commune_avec_l_echange_par_paire_et_les_rangs` ne vérifie que les réglages rendus. Après : un essai (ou ces lignes dans celui-ci, avec `monkeypatch`) qui enregistre la permutation reçue par `_permuter` pendant la lecture commune :
```python
def test_la_lecture_commune_joue_la_permutation_demandee(tmp_path, donnees, monkeypatch):
    vrai, appels = A._permuter, []
    monkeypatch.setattr(A, "_permuter", lambda rng, pp, permutation: appels.append(permutation) or vrai(rng, pp, permutation))
    for nom, mode in (("libre", LIBRE), ("paire", PAIRE)):
        appels.clear()
        registre, table, bn, juge, manifestes = _preparer(tmp_path / nom, donnees)
        _ouvrir_tout(registre, manifestes)
        A.lire_les_cinq(RACINE, registre, donnees["lignes"], donnees["conditions"], donnees["taches"], ENTROPIE,
                        manifestes[A.BOITE_NOIRE], manifestes[A.JUGE], tmp_path / nom / "table" / A.FICHIER_TABLE_OPAQUE,
                        "moyenne", mode, "score", tmp_path / nom / "unites", 3, 20)
        assert appels and set(appels) == {mode}
```

**Correction (j), texte avant et après.** Avant : `test_rangs_dans_le_pli_et_aire_d_une_restriction` forme les rangs sur une collecte d'une seule dose. Après : un essai sur une collecte de deux doses, où chaque groupe moniteur, dose et pli a ses propres rangs :
```python
def test_rangs_par_moniteur_dose_et_pli(piece, donnees):
    _, M = piece
    plis = A.plis_communs(M, donnees["taches"], donnees["graines"])
    unites, _ = A.unites_avec_scores(donnees["actions"], _scores(donnees["actions"], 0.5))
    collecte = []
    for dose in ("dose-0.50", "dose-1.00"):
        A.lire_scores_fixes(A.JUGE, M, unites, dose, plis, donnees["graines"], REGISTRE, collecte, LIBRE, 3, 20)
    rangs = A.rangs_dans_le_pli(collecte)
    groupes = {(x["moniteur"], x["dose"], x["pli"]) for x in collecte}
    assert len(groupes) == 4
    for g in groupes:
        s = np.array([x["score"] for x in collecte if (x["moniteur"], x["dose"], x["pli"]) == g])
        r = np.array([x["rang"] for x in rangs if (x["moniteur"], x["dose"], x["pli"]) == g])
        assert np.array_equal(r, np.array([(s < v).sum() + ((s == v).sum() + 1) / 2.0 for v in s]))
```
Je les ai éprouvés dans ma copie de banc, à côté du fichier d'essais de la version 8 : sains sur le module v8 (`68 passed`) ; sous la mutation « libre toujours », un seul essai échoue (`1 failed, 67 passed`), et c'est (i) : les 66 essais de la version 8 passent sous cette mutation, et (j) n'appelle pas la lecture commune ; sous la mutation « rangs sur toutes les doses », un seul échoue (`1 failed, 67 passed`), et c'est (j), pour la même raison. Le code n'a pas à changer ; une version 9 du fichier d'essais suffit. Après ces deux essais, je n'ai besoin que de leur dernière ligne pour dire « inscriptible ».

## 3. Aucun calcul de moniteur n'a changé depuis la version 7

Lu au diff : les fonctions d'aire, de borne, de collecte, de plis, de graines et de lecture des moniteurs ne changent pas ; la branche libre de `_permuter` est celle de la version 7, mot pour mot, sous une condition ; la seule addition sur le chemin de la permutation libre est `exiger_permutation`.

Rejoué (`scripts-moi/verif_v8.py`, données factices de la fabrique, juge sur un sous-échantillon, actions sans score, un épisode de dose sans aucune lecture) : la lecture commune de la version 7 et celle de la version 8 (« libre par épisode », « score ») sur les mêmes entrées.
- Les lectures des cinq moniteurs aux quatre doses : **aucun écart**, champ par champ (aires, plis, bornes, valeurs p, comptes) ;
- plis, statistiques de l'agrégateur, exclues, comptes des lectures : égaux ;
- **le fichier par unité est identique à l'octet.**

## 4. La permutation : paramètre obligatoire ; l'échange par paire est juste

**Sans défaut.** `permutation` est un argument positionnel de `lire_les_cinq`, de `lire_moniteur_appris` et de `lire_scores_fixes`, sans valeur par défaut ; `exiger_permutation` refuse tout ce qui n'est pas l'une des deux chaînes exactes (essai : `None`, vide, « par action », « libre », une liste ; et un appel sans l'argument lève `TypeError`). Je l'ai vérifié aussi sur `_permuter` (vide, « libre », casse changée, absente : refusées). Les réglages rendus nomment la permutation jouée et son unité.

**La forme « échange par paire »** (`_paires_de_la_tache`, `_permuter`) : dans chaque pli et chaque tâche, les unités sont groupées par rang d'épisode, puis par condition ; à chaque rang dont les deux épisodes sont là, les deux étiquettes sont retournées avec une chance sur deux (`rng.random() < 0.5`) ; un rang qui n'a qu'un épisode n'est pas touché. C'est l'option que j'avais écrite. Mon contrôle indépendant (`verif_v8.py`, 200 permutations à la dose ½, avec un épisode de dose sans aucune lecture) :
- une seule étiquette par épisode, et une de chaque sorte dans chaque paire complète : vrai partout ;
- part des paires échangées : **0,499** sur 25 400 ;
- l'épisode sans son pair garde son étiquette : vrai partout ;
- le nombre d'épisodes de la dose dans chaque tâche est donc conservé.

Le même rang d'épisode porte les mêmes graines dans les deux conditions : je l'avais vérifié au lanceur (clé `verification/tache/{id}/e{k}`, sans la condition) ; l'appariement que suit le code est donc celui du jeu.

**Ses deux gardes mordent.** `exiger_etiquettes_par_episode` (déjà là) et `exiger_etiquettes_par_paire` (neuve : plus de deux épisodes de même rang ; paire sans une étiquette de chaque sorte ; épisode seul changé). Chacune de ses trois conditions a son artefact dans `test_gardes_de_l_echange_par_paire` (et la permutation libre, qui défait les paires, est refusée par elle dans `test_echange_par_paire_structure`) ; son câblage (appelée pour la paire, pas pour la libre) est éprouvé. Au banc : les trois conditions de la garde de la paire, son appel, et son appel à tort pour la permutation libre : cinq mutations, toutes tuées ; huit mutations de l'échange lui-même (jamais, toujours, chance de 0,3, épisode seul échangé, sans retournement, un seul des deux retourné, paires sans le rang, paires par rang modulo 2) : toutes tuées.

**Son essai de niveau tient.** `test_niveau_et_puissance_des_deux_permutations_sur_des_paires` (40 essais, 99 permutations, effet commun à la paire) : sans effet, au plus 6 rejets à 5 % pour l'échange par paire ; avec un effet de 0,15, au moins 30 sur 40 pour l'échange par paire, et au moins 15 de moins pour la libre. Il passe. Je l'ai refait avec ma simulation (16 tâches, 8 rangs, 10 actions, écart-type de la paire 1), mais en appelant le `_permuter` du module : part des p ≤ 0,05

| | libre par épisode | échange par paire |
|---|---|---|
| sans effet | 0,00 | 0,05 |
| effet de 0,15 | 0,15 | 0,95 |

Ce sont les nombres de ma simulation de la version 7 (0,00 et 0,04 sans effet ; 0,08 et 0,95 avec effet), aux fluctuations près.

**Les aires et les bornes ne dépendent pas du choix.** Rejoué de bout en bout : sur les mêmes entrées, la lecture commune avec l'échange par paire rend, pour les cinq moniteurs aux quatre doses, les mêmes aires, plis, bornes hautes, effectifs et tirages que la permutation libre, et le même fichier par unité, à l'octet ; seules les valeurs p peuvent changer.

Une remarque sans conséquence sur le code : dans `test_lecture_commune_avec_l_echange_par_paire_et_les_rangs`, la comparaison des deux préparations se termine par `… or m == A.AGREGATEUR`, ce qui la rend vide pour l'agrégateur, et elle ne porte pas sur le juge ni le moniteur boîte noire. Mon contrôle ci-dessus montre l'égalité pour les cinq ; l'essai pourrait retirer cette exception. Ce n'est pas une condition.

## 5. La forme « rang » rend les mêmes aires que la forme « score »

`rangs_dans_le_pli` : rang moyen de l'unité dans son pli, pour son moniteur et sa dose (1 pour la plus petite valeur, les ex aequo partagent la moyenne). Le fichier `rangs-par-unite-moniteurs-bras-a.jsonl` a les neuf premiers champs de la forme « score », puis `rang`, et aucun champ `score`.

Rejoué (`verif_v8.py`) : sur les mêmes entrées, la forme « rang » et la forme « score »
- rendent les mêmes lectures (aires, bornes, valeurs p) ;
- ont les mêmes unités dans le même ordre ;
- donnent la même aire sur 120 comparaisons (chaque moniteur, chaque dose, chaque pli ; le pli entier et deux restrictions : honnêtes et épisodes pairs de la dose, honnêtes et trois premiers épisodes de la dose) : **écart maximal 0** ;
- et l'aire moyenne des deux plis recalculée sur les rangs est celle que rend la lecture, à 0 près.

C'est attendu : l'aire de Mann-Whitney ne dépend que de l'ordre dans le pli, et toute restriction garde l'ordre. L'interdiction d'écraser vise le fichier de la forme demandée, avant tout calcul (essai, et mutation tuée).

**Ce que la forme « rang » ne lève pas.** Le rang dans le pli garde l'ordre des scores d'un moniteur appris ; avec les textes d'action, l'ordre seul laisse encore approcher ses poids, moins finement que la valeur. La réserve de cloisonnement reste donc, en plus faible : le fichier n'est lu que par le programme de l'aire conditionnelle. La phrase du point 24 de la liste v8 le dit bien pour les deux formes.

## 6. La liste « sans interne » v8

Lue entière contre la v7 (`381036f2…`) et la v6 (`f3617a24…`).
- **Version citée.** Une table « Modules à citer », qui remplace celle de la v6 et l'en-tête de la v7, dit que pour tous les points des lots 14 et 16 les modules à citer sont : moniteurs à modèle de langue v3, autres moniteurs v8, préparation v2, au commit `18f63f40`, et l'extraction v2 et la vérification du tokeniseur v2 à leurs empreintes. **Les cinq empreintes sont justes à la tête `e6a5d2b4`** (je les ai recalculées). Elle dit que les versions 1 à 7 du module des autres moniteurs ne servent à aucune lecture décisive.
- **Mes corrections** (rapport `4bfa5eac…`, partie 5) :
  - point 24 : la fin que j'avais écrite, mot pour mot, et la variante « en rangs » ;
  - point 26 : mot pour mot, avec la ligne d'artefacts complétée du manifeste à clé de plus ou sans engagement ;
  - point 27 : laissé en attente de la décision de fond, avec les deux textes ; celui de l'échange par paire est le mien, complété de la paire incomplète et des deux gardes, ce qui est exact ;
  - point 30 : la phrase de (d), complétée de « à l'écriture comme à la lecture » et de son artefact ;
  - points 10 et 11 : cinq états, nommés ; la phrase de (a) ajoutée au point 11, avec ses artefacts ;
  - point 36 : ma phrase de la partie 4.5, reprise telle quelle.
- **Points neufs.** 33 (motif des tirages illisible : la lecture s'arrête) et 34 (format de la forme « rang ») : exacts, au code.
- **Aucun interne.** Ni seuil, ni trait, ni vocabulaire, ni poids, ni texte de consigne. Les seuls nombres sont des numéros de points et de sections, des empreintes, des dates, des comptes de méthode (dix champs, huit paires, 256 permutations, cinq états).
- Une phrase est vraie à cette tête et à revoir après ma pièce : « Les modules des lots 14 et 16 et la préparation attendent la vérification du contre-lecteur dans ces versions. »

## 7. Essais joués (dernières lignes)

- Moniteurs à modèle de langue, version 3 (avec le dossier du tokeniseur du juge) : `51 passed in 18.48s`.
- Autres moniteurs, version 8 : `66 passed in 883.35s (0:14:43)`.
- Préparation des lectures, version 2 : `8 passed in 4.84s`.

Programmes et sorties, dans `opus-contre-lecture-bras-a/` : bancs `mutations14v3.py` et `mutations16-v8.py`, sorties `banc14v3.txt` et `banc16v8.txt` ; contrôles `scripts-moi/verif_v8.py` (version 7 contre version 8, forme « rang », structure de l'échange par paire, niveau et puissance) et `scripts-moi/verif_v8b.py` (permutation libre contre échange par paire, de bout en bout).

Copies restaurées et vérifiées à leurs empreintes : `8e941d24…` (moniteurs à modèle de langue v3), `61105129…` (autres moniteurs v8), `6dfd2bfc…` (préparation v2), dans les deux copies des bancs. Le fichier d'essais où j'ai éprouvé (i) et (j) était dans ma copie de banc ; il est retiré.
