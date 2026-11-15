# Code qui joue le préenregistrement de l'idée 1.2 — rapport du développeur — v1

- Auteur : développeur neuf, sous-agent de la session mère ; je n'ai écrit ni le préenregistrement (v1 à v4), ni ses
  contre-lectures, ni la vérification courte, ni les deux contrôles de différentiel, ni le banc B v1, ni la preuve, ni le juge.
- Date (UTC) : 2026-11-15, de 09:50 à 10:45 environ (`date -u`). Dépôt lu sur `main`, tête `b9cf34fd`. **Aucun commit,
  aucune poussée, aucun appel réseau ni payant ; le run réel n'a pas été lancé** ; aucun `diag/` existant lu ; rien écrit sous
  `donnees/`, `docs/verdicts/`, ni dans `docs/notes/organisme-idees-juge-v1/correction-poids-v1/`.
- Texte joué : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
  (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`, `exiger_prereg_scelle` conforme), ci-dessous **[T]**,
  lignes citées « l. n » ; contrôle final `docs/notes/organisme-idees-juge-v1/controle-differentiel-prereg-tirages-repartis-v4-v1.md`
  (`a22c627d958c6ef3aff14b703a20bfa85fb9f82c2e187587da997961ba287d43`), observations O1 à O6 ; registre R-2886.
- Juge réel : copie `94bfd92` (`docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/`), **importée** (jamais
  lancée comme programme), empreintes vérifiées à chaque chargement ; la copie du nul v9 (`copie-nul-v9-a41b7b5/`) **n'est pas
  employée** : l'idée 1.2 ne juge que sous le nul v8 ([T] l. 154, 325).

## Verdict

Le code qui joue [T] est écrit, sans le jouer : 109 essais verts (sur 109), 18 mutations sur 18 tuées pour la raison
attendue (dont « valeur e lue au maximum » par la lecture (3) sur le jeu synthétique de 20 000 générations), répétition
miniature de bout en bout conforme (10 générations, racine d'essai). **Durée estimée du run réel : 3 à 5,5 h sur deux
processus d'une machine libre, environ 7 h sous la charge observée ici ; sous la borne de 24 h**, mais trois à six fois le
temps processeur que le Coût du texte laissait attendre. **Deux écarts au texte scellé (nœuds)** : lieu du code (`src/` au lieu de `docs/notes/…/code-v1/`) ; lois du
monde jouet du jeu synthétique tirées par génération (lecture de « graines (97, g) »), à confirmer. Le reste est conforme ou
relève de lectures du texte dites plus bas, à soumettre à la contre-lecture du code.

## Fichiers (tous neufs, tous scellés par compagnon `.sha256`)

| fichier | lignes | empreinte sha256 |
|---|---|---|
| `src/controle_ia/organisme_idees_juge/__init__.py` | 22 | `c29258ab0069320bbba33d3cdf8b652ba1ce254298b348e2c68ac03e83e6414e` |
| `src/controle_ia/organisme_idees_juge/juge_v1.py` | 126 | `853595cb44260eaaf16bf003f7a7b8155a3785e08c424573fcdaf40a6d1c487e` |
| `src/controle_ia/organisme_idees_juge/lois_v1.py` | 353 | `bf7e1f3e6cdbbebed681cf115e6d7e8031e670ffb14d82910d707a09f5b0e1fb` |
| `src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py` | 495 | `9cb63ff12d6198b3acd0ec979e798fe41268b2a50a8d90600614fd01284d65b9` |
| `src/controle_ia/organisme_idees_juge/oracle_v1.py` | 79 | `34b6d356be3d717c7f0ab44711d4e1ee38926d6db6be4cd2a3a9684514db4350` |
| `src/controle_ia/organisme_idees_juge/rejeu_v1.py` | 317 | `a1a08ef78c87ba8ffaa4147d53854dd4c17e6a70ec5b265cb406a858a49d1086` |
| `src/controle_ia/organisme_idees_juge/synthetique_v1.py` | 154 | `febe203ab27796ba573accea6e6fea5692bc2c776191254408ab07d3cc9815d7` |
| `src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v1.py` | 399 | `9c25699e280d9179d6c9a541711921a4861b8a129fe434de559b1a51526d4638` |
| `src/controle_ia/organisme_idees_juge/mutations_v1.py` | 253 | `77a74bf7f1e6fdc2fcb08267de90d16845e8b30b1c55762613e77f35a60bf15c` |
| `src/controle_ia/organisme_idees_juge/execution_v1.py` | 283 | `d6da7373efca00b538407794bcd832f3f84970412e6200e49715d23455731747` |
| `scripts/jouer_idee_1_2_v1.py` | 230 | `a2a059b298ffc01b2746f32892f6390e46763ba88c665f2d840a56dc7801f640` |
| `scripts/lire_idee_1_2_v1.py` | 55 | `0382ed81c0d65f83505b9790c8dbc48e5ab3d295ad038e639f6e1c2bded87a86` |
| `tests/test_organisme_idees_juge_lois_v1.py` | 140 | `7c0b30aea0bbc1529a2d1400aa2c11bcb83dfd467c3c65a0b2d7f395d0f385e2` |
| `tests/test_organisme_idees_juge_banc_v1.py` | 223 | `565d4217d8bf4fd8c8ab9ab78d91b78313179a43f8b73c94c6031b592d8b1273` |
| `tests/test_organisme_idees_juge_rejeu_v1.py` | 149 | `faf94968a189e82f125dbef1b432f9e04870996af0b88493fe758993d782f7fd` |
| `tests/test_organisme_idees_juge_lecture_v1.py` | 196 | `3606348964a9b00dd817ad6d442f76216b99817fb21843e20face9b37983c27a` |
| `tests/test_organisme_idees_juge_mutations_v1.py` | 61 | `14dfd455c963bf4ec84903e11cf4504a65dc2c9c8cecfcad50dbcb8c35fe2eb3` |
| `tests/test_organisme_idees_juge_execution_v1.py` | 235 | `7e0f1bfb4dbc7c237ea0d6e783c1bb25ae110ce8553c15c65769743760998482` |

Lignes prêtes pour l'addendum d'empreintes (format `sha256sum`, rendues par `--lister-empreintes`) :

```
c29258ab0069320bbba33d3cdf8b652ba1ce254298b348e2c68ac03e83e6414e  src/controle_ia/organisme_idees_juge/__init__.py
853595cb44260eaaf16bf003f7a7b8155a3785e08c424573fcdaf40a6d1c487e  src/controle_ia/organisme_idees_juge/juge_v1.py
bf7e1f3e6cdbbebed681cf115e6d7e8031e670ffb14d82910d707a09f5b0e1fb  src/controle_ia/organisme_idees_juge/lois_v1.py
9cb63ff12d6198b3acd0ec979e798fe41268b2a50a8d90600614fd01284d65b9  src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py
34b6d356be3d717c7f0ab44711d4e1ee38926d6db6be4cd2a3a9684514db4350  src/controle_ia/organisme_idees_juge/oracle_v1.py
a1a08ef78c87ba8ffaa4147d53854dd4c17e6a70ec5b265cb406a858a49d1086  src/controle_ia/organisme_idees_juge/rejeu_v1.py
febe203ab27796ba573accea6e6fea5692bc2c776191254408ab07d3cc9815d7  src/controle_ia/organisme_idees_juge/synthetique_v1.py
9c25699e280d9179d6c9a541711921a4861b8a129fe434de559b1a51526d4638  src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v1.py
77a74bf7f1e6fdc2fcb08267de90d16845e8b30b1c55762613e77f35a60bf15c  src/controle_ia/organisme_idees_juge/mutations_v1.py
d6da7373efca00b538407794bcd832f3f84970412e6200e49715d23455731747  src/controle_ia/organisme_idees_juge/execution_v1.py
a2a059b298ffc01b2746f32892f6390e46763ba88c665f2d840a56dc7801f640  scripts/jouer_idee_1_2_v1.py
0382ed81c0d65f83505b9790c8dbc48e5ab3d295ad038e639f6e1c2bded87a86  scripts/lire_idee_1_2_v1.py
7c0b30aea0bbc1529a2d1400aa2c11bcb83dfd467c3c65a0b2d7f395d0f385e2  tests/test_organisme_idees_juge_lois_v1.py
565d4217d8bf4fd8c8ab9ab78d91b78313179a43f8b73c94c6031b592d8b1273  tests/test_organisme_idees_juge_banc_v1.py
faf94968a189e82f125dbef1b432f9e04870996af0b88493fe758993d782f7fd  tests/test_organisme_idees_juge_rejeu_v1.py
3606348964a9b00dd817ad6d442f76216b99817fb21843e20face9b37983c27a  tests/test_organisme_idees_juge_lecture_v1.py
14dfd455c963bf4ec84903e11cf4504a65dc2c9c8cecfcad50dbcb8c35fe2eb3  tests/test_organisme_idees_juge_mutations_v1.py
7e0f1bfb4dbc7c237ea0d6e783c1bb25ae110ce8553c15c65769743760998482  tests/test_organisme_idees_juge_execution_v1.py
```

## Ce que fait chaque module

- `juge_v1.py` : vérifie la liste d'empreintes de la copie (`0153e02d…`, égale à [T] l. 44-45, et à son compagnon), puis
  chacun des dix modules chargés (`__init__`, `outils`, `caviardage`, `fiche`, `selection_pari`, `cycle`, `memoire`, `nul_v8`,
  `nul_filles_v2`, `controles_pari`) et les cinq fichiers que [T] cite par empreinte entière (l. 45-50, `a_blanc_v59` compris,
  jamais importé) ; interdit l'écriture de code compilé (rien sous `docs/`) ; vérifie que chaque module `pole.*` chargé vient
  de la copie. Tout écart : `GardeArret`.
- `lois_v1.py` : constructeurs de la grammaire du juge (softmax aléatoire, `si_sinon`, `par_sous_population`, `melange`,
  `transformee`), composantes V1 à V5 (`Composante.loi(force)`, direction bruitée), coupures, seuils décentrés, poids de
  Dirichlet, doublons ; **évaluateur vectorisé** `probas_np` (mêmes opérations que `selection_pari.proba`, essai : écart
  ≤ 10⁻¹²) servant **seulement** à l'oracle (20 000 instances) et à la règle du cosinus ; cosinus de [T] l. 399-400.
- `banc_tirages_repartis_v1.py` (nom de [T] l. 460) : banc B v2 — graines (`racine_de`, `generateur` par
  `SeedSequence(entropy=racine, spawn_key=clé)`), archive A2, mondes T et N, cartes T et N, échantillon de l'oracle,
  `Generation` (machine à états construite → engagements → gelée → tirée → évaluée, avec les gardes du gel et du flux propre),
  montage du juge (bibliothèque comme `juger_carte`, `construire_engagement_v2` « ordre_naturel », 32 instants, `evaluer_v2`),
  `EvaluationFiltree` (seule la trajectoire est lisible), rapport exact Λ (famille N), domination, essai E1, liste des 50 cartes
  de E1.
- `oracle_v1.py` : table de l'oracle d'une génération ([T] l. 285-291) : membres ordinaires par
  `selection_pari.trajectoire_membre`, membres ajustés par `nul_filles_v2.valeurs_ajustees` à l'instant 20 000 (marge de
  certificat comprise), cache vectorisé de même interface que `selection_pari.Cache` ; gain, classes ; gardes : avant toute
  issue fraîche, échantillon retiré de sa graine `(f, g, 2000)` et comparé.
- `rejeu_v1.py` : les sept bras ([T] l. 430-447) sur les trajectoires calculées une fois ; `Vue` (garde d'accès), `Budget`
  (garde des tirages) ; valeur e (règle (vi)) ; e-BH du juge (`cycle.appliquer_multiplicite`, m_fixe = 24), **recoupée** par
  une seconde écriture de e-BH et de la valeur e ; **vérificateur indépendant** (écriture par tableaux) qui refait chaque
  allocation à partir des trajectoires, des positions et de la graine du placebo ; garde « m = 24 ».
- `synthetique_v1.py` : jeu d'essai synthétique de la réserve (a) ([T] l. 306-316) : monde jouet du programme `01c648a0…`,
  graines `(97, g)`, lecture sans allocation par la fonction même du rejeu, moyenne et borne basse percentile
  (10 000 rééchantillons `(99, b)`), mutation « maximum de la trajectoire ».
- `lire_banc_tirages_repartis_v1.py` (nom de [T] l. 461) : lecture gelée ; charge la sortie seulement scellée et rattachée à un
  seul manifeste ; apparie oracle et jeu (mêmes cartes, oracle scellé au rejeu) ; étages 1, 1 bis, 2, 3, 4, 5 dans l'ordre de
  [T] l. 486-493 ; prédictions Q1 à Q9 (rapportées) ; éléments de l'audit R4 (le code ne prononce rien) ; écrit
  `lecture-gelee-v1.json` scellé.
- `mutations_v1.py` : banc de mutations de l'étape 0 (section « Banc de mutations » ci-dessous).
- `execution_v1.py` : enchaînement des étapes 2 à 5 de [T] l. 469-474 (E1, oracle scellé, jeu, sortie scellée), deux
  processus au plus (`multiprocessing`, bifurcation), gardes de durée (24 h) et de réseau, `arret.json` scellé sur tout arrêt,
  vérification de l'addendum d'empreintes, liste des fichiers gelés.
- `scripts/jouer_idee_1_2_v1.py` : lanceur (`python -I -B`), modes « jeu décisif » et « répétition miniature », et
  `--lister-empreintes` (lignes prêtes pour l'addendum). `scripts/lire_idee_1_2_v1.py` : lecture gelée d'un run décisif
  (racine lue au manifeste ; n'affiche que le chemin et l'empreinte de la lecture).

## Correspondance avec le texte scellé

| [T] | exigence | code |
|---|---|---|
| l. 279-281 | B = 4 800 ; A, P, P′, F-arrêt, G ≤ B ; F = B ; F125 = 6 000 ; entraînement hors compte | `rejeu_v1.BUDGET_BLOCS`, `BUDGET125_BLOCS`, `Budget`, `jouer_bras` (deux gardes : dépassement ; blocs non comptés) |
| l. 282-284 | promotion par `appliquer_multiplicite`, m_fixe = 24, α = 0,05 ; valeur e tronquée, arrêtée à m/α | `rejeu_v1.promotions_ebh`, `log_valeur_e`, recoupement dans `jouer_bras` |
| l. 285-291 | oracle avant le jeu, 20 000 instances `(f, g, 2000)`, nul v8 ajusté à 20 000, gain, quatre classes, table scellée avec la sortie | `banc.echantillon_oracle`, `oracle_v1.table_oracle`, `classe` ; `execution_v1.executer` scelle `oracle.json` avant le rejeu |
| l. 292-298 | couverture (Clopper-Pearson), différences appariées (percentile, 10 000), McNemar, FP par sorte, partiellement vraies, erreurs de décision | `lire_….lecture_famille_T`, `Reechantillonneur`, `clopper_pearson`, `mcnemar_exact` |
| l. 299-305 | validité, quatre lectures ; jugées sur 500, rapportées par monde (250) | `lire_….lecture_validite` (par bras, par monde, domination recalculée, 49 intervalles, G parmi les sept bras) |
| l. 306-318 | réserve (a) : jeu synthétique 20 000, sans allocation, maximum sur 32 instants, borne basse percentile 10 000 ; réserve (b) : fuite d'instants vue seulement par la garde d'accès | `synthetique_v1.epreuve_mutation_maximum` ; `rejeu_v1.Vue.lire` et la mutation « la règle lit un instant non révélé » |
| l. 319-321 | consommation, économie, tirages reçus par sorte et classe, parts arrêtées bas, haut, plafond ; par cellule et réunis | `lecture_famille_T` (`tirages`, `tirages_recus`, `cellules`) |
| l. 325-327 | blocs de 25, instants fins de blocs, plafond 800 ; arrêt bas log W < log(1/20) à t ≥ 50 ; arrêt haut log W ≥ log(m/α) | `banc.INSTANTS`, `rejeu_v1.SEUIL_BAS`, `arretee_bas` (indice ≥ 1), `SEUIL_HAUT`, `arretee_haut` |
| l. 328-330 | tenue ≤ 13, non tenue ≥ 39 sur 500 (sept bras) | `seuils_validite` (recalcul du script de l'annexe B ; garde : 13 et 39 exigés pour 500) |
| l. 331-338 | domination à tout instant ; borne basse > 1 dans l'un des 49 intervalles ; six sortes ; par monde : audit, non verdict | `lecture_validite` (`defauts_etage_1`, `audit_ecrit_requis_par_monde` ; garde : 49 intervalles exigés pour 500) |
| l. 339-342 | principale dans l'ordre nuisible, gain, pas de gain, non tranché | `lire_….lire`, étage 3 |
| l. 343-346 | qualifications, quatrième issue, A − P′ rapporté | `lire`, étage 4 |
| l. 347-349 | zone utile C_F ∈ ]0,05 ; 0,95[ | `lire`, étage 2 |
| l. 358-364 | espace, instances arrondies, softmax aléatoire, archive A2, coupures \|s\| ≥ 0,3 | `banc.tirer_instances_np`, `lois.softmax_aleatoire`, `banc.construire_archive`, `lois.coupure_archive` |
| l. 366-381 | lignes Q1, V1 à V5 | `lois.melange_archive`, `lois.Composante`, `tirer_composante`, `seuil_decentre` |
| l. 388-389 | dix cellules, cellule g mod 10 | `lois.CELLULES`, `cellule` |
| l. 391-405 | famille T : 6 porteuses, 6 copies de la classe, 4 copies par morceaux, 6 fausses (règle du cosinus, plafond 1 000, V4 : six sous la règle), 2 nulles | `banc.cartes_T`, `fausse_construite` |
| l. 407-423 | famille N : M₀ (g < 250), M₀′ (g ≥ 250, base parmi S1 et S2) ; 8 voisines, 8 membres exacts, 8 autres (fausses : règle du cosinus contre la composante de la cellule) | `banc.construire_monde`, `cartes_N` |
| l. 425-428 | plan de 800, entraînement sur 100, 800 issues, flux propre ; richesses calculées une fois par `evaluer_v2` ; bras rejouant les mêmes trajectoires | `Generation.preparer_engagements`, `tirer_frais`, `evaluer` ; `execution_v1._tache_jeu` ; `rejeu_v1.rejouer_generation` |
| l. 430-447 | bras F, F-arrêt, A, P, P′, F125, G | `rejeu_v1.bras_*`, `BRAS` |
| l. 449-456 | graines (racine, clés, issues fraîches après le gel, 1001, 1000, 2000, (99, b), (97, g)) ; manifeste | `banc.racine_de`, `generateur` ; `Generation` ; `rejeu_v1.generateur_placebo` ; `Reechantillonneur` ; `synthetique_v1` ; lanceur : `creer_manifeste` (configuration et empreinte, versions, commit ; clés écrites dans la configuration) |
| l. 460-467 | code sous noms neufs, essais (R5 par ligne de la liste d'arrêt), banc de mutations, contre-lecture du code, addendum | modules `*_v1.py` ; essais ; `mutations_v1` ; contre-lecture et addendum : **à faire** (pas mon rôle) ; `--lister-empreintes` prépare l'addendum |
| l. 468 | contrôles avant jeu | lanceur `jeu_decisif` : préenregistrement, arbre propre, sortie absente, addendum, copie du juge, essais (`lancer_essais`), mutations (`MU.banc` avec la racine du texte) |
| l. 469-471 | E1 sur 50 cartes, 32 instants, deux égalités ; sinon arrêt | `banc.essai_E1_carte`, `CARTES_E1`, `executer` (arrêt avant l'oracle) |
| l. 472 | oracle scellé avant le rejeu | `executer` : `oracle.json` scellé, vérifié au départ et à la fin du rejeu ; chaque génération jouée porte l'empreinte de l'oracle |
| l. 473 | 1 250 générations, `nice -n 10`, deux processus au plus | `generations_du_texte`, `abaisser_priorite` (`os.nice(10)`), `_carte` (≤ 2), une file de calcul par processus |
| l. 474 | sortie scellée avant toute lecture, sous `diag/organisme-idees-juge-v1/` | `diag/organisme-idees-juge-v1/<run>/` : `controles-avant-jeu.json`, `oracle.json`, `jeu.json`, `journal.json` (ou `arret.json`) |
| l. 475 | lecture gelée, puis lecteur neuf, audit R4 | `scripts/lire_idee_1_2_v1.py` ; lecteur neuf et audit : à venir |
| l. 486-493 | étages 1 à 5 | `lire` |
| l. 495-500 | audit de symétrie : éléments | `indicateurs_audit` (« trop propre », « tout négatif », porteuses arrêtées bas, partiellement vraies promues, cellules) |
| l. 504-515 | liste d'arrêt | section « Essais » ci-dessous |

## O1 à O6 (contrôle final), portés dans le code

- **O1** : le repli au plafond (« la carte de plus petit cosinus est gardée et signalée ») est la même fonction
  `banc.fausse_construite` pour les familles T et N ; le drapeau `plafond_atteint` et le nombre de tirages sont écrits dans la
  construction de chaque carte (`oracle.json`, champ `construction`).
- **O2** : en famille N, la référence du cosinus est la porteuse construite à force × 1 (dose de la cellule) : `cartes_N`
  passe `p_porteuse = probas(comp.loi(1.0))` ; essai `test_fausses_construites_regle_du_cosinus`.
- **O3** : le jeu synthétique **garde** le plafond de log e à 50 de la mutation X2 (`synthetique_v1.PLAFOND_LOG_E`), pour la
  lecture saine et la lecture mutée ; il ne peut que baisser la moyenne (échec du côté sûr). La lecture (3) du jeu réel n'a
  **aucun** plafond.
- **O4** : seuls les 49 intervalles comptent : `lecture_validite` ne calcule pour le critère que 7 (par bras) + 42 (six sortes
  × sept bras) intervalles, et exige 49 quand la famille N compte 500 générations.
- **O5** : 10 000 rééchantillons pour la lecture (3) comme partout (`REECHANTILLONS = 10_000`).
- **O6** : cosmétique, sans effet sur le code.

## Lectures du texte faites par le code (à contre-lire ; aucune ne touche un seuil)

1. Ordre des tirages dans chaque générateur : archive S1, S2, U1 à U4, jA, s_A, s_B ; monde : paramètres de la composante
   (j, puis c, puis u ; Δ ; N) ; oracle : instances (traits puis sous-populations) puis uniformes ; plan : 800 instances, puis
   100 instances d'entraînement, puis 100 uniformes (le texte dit « son plan, son entraînement et les issues
   d'entraînement » ; `juger_carte` tire l'entraînement avant le plan, sans effet sur la loi).
2. Famille N : la composante de la cellule (deux porteuses construites, référence des deux fausses) est tirée par le
   générateur du monde `(0, g, 24)`, après les paramètres du monde (le texte ne donne pas de clé propre).
3. Cellules : V1 à V5 dans l'ordre, dose basse puis haute (cellule 0 : V1 0,25 ; … ; 9 : V5 0,8).
4. « Mélange des lois d'archive » = construction de la ligne Q1 (S1 à S4 et l'uniforme fixe, Dirichlet(1, …, 1) à cinq
   poids, arrondis à 10⁻⁶ et renormalisés), comme la v1 de [T] l'écrivait (« ligne Q1 de [BANC] »).
5. Lois construites arrondies à six décimales à leur création ; puissance et inclinaison arrondies à six décimales.
6. Direction bruitée : bruit gaussien de norme 0,3 fois celle de la direction (centré par colonne pour Δ, centré pour u),
   puis renormalisation à la norme d'origine ; pour V4, la direction est le vecteur des neuf paramètres de la loi neuve N.
7. Doublon : chaque nombre du champ « poids » de chaque loi softmax de M, plus 0,01·N(0, 1) ; biais inchangés.
8. « Composante de même type tirée indépendamment » : tous les paramètres aléatoires du type sont retirés (j, c, u, Δ, N) ;
   pour V5, la condition reste la coupure de l'archive.
9. Copie par morceaux « au signe d'un trait (S2, S1) » : trait j tiré uniforme par la graine de construction de la carte.
10. Membres exacts pour Q2 et l'étage 1 : les 8 « membres exacts » de N **et** les 6 « copies de la classe » de T (Q2 dit
    « dans aucune famille ») : du côté prudent.
11. Oracle : la marginale d'entraînement, propre à chaque carte, n'entre pas (le meilleur membre est le même pour les
    24 cartes, [T] l. 521 ; la marginale ajustée domine toute loi fixe de la marginale). Probabilités par instance calculées par
    l'évaluateur vectorisé, servies aux routines du juge (écart ≤ 10⁻¹² à `selection_pari.proba`, écart ≤ 10⁻⁸ entre les deux
    caches sur les membres du nul, essais).
12. Issues fraîches et d'entraînement : uniformes du générateur numpy de la clé, issue par `selection_pari.tirer_categorie`
    sur `selection_pari.proba` (fonctions du juge).
13. Bras G : les deux premiers blocs sont donnés sans condition (comme la règle gloutonne du programme `01c648a0…`) ;
    égalité de log W courante : plus petite position. Bras P : la carte est tirée par `rng.integers` parmi les éligibles
    rangées par position. Bras P′ : tours à la suite des tours de la phase 1 (numérotation continuée), ordre des positions
    décalé du numéro du tour, sur l'ensemble élargi.
14. Essai E1 : les 50 cartes sont les 24 de T g = 0, les 24 de N g = 0 et les deux premières de T g = 1 (chaque sorte
    couverte) ; remplacement déterministe y → (y + 1) mod 3 au-delà de t (comme l'annexe B de [BANC-v1]) : aucune clé neuve.
15. Intervalle percentile : quantiles 2,5 % et 97,5 % (`numpy.quantile`, interpolation linéaire) ; même rééchantillon b pour
    toutes les statistiques d'un même ensemble de générations.
16. Hors de la zone utile : étages 3 et 4 non lus ; prédictions rapportées avec la mention « sans valeur de verdict ».
17. « Deux processus au plus » : deux processus de calcul (le processus parent attend, sans calcul).
18. Banc de mutations : les scénarios de code (bras, gel, flux, oracle) emploient une **racine d'essai** fixe ; seul le jeu
    synthétique emploie, au jeu réel, la racine du texte avec les clés `(97, g)` comme [T] le demande.

## Écarts au texte scellé (chacun est un nœud)

- **E-1, lieu du code** : [T] l. 460-461 nomme `docs/notes/organisme-idees-juge-v1/code-v1/banc_tirages_repartis_v1.py` et
  `lire_banc_tirages_repartis_v1.py`. Sur la demande de la mère, le code est sous
  `src/controle_ia/organisme_idees_juge/`, avec ces deux noms et sept modules voisins, et les lanceurs sous `scripts/` (les
  habitudes du dépôt interdisent d'exécuter depuis `docs/`). Enjeu : traçabilité seule, aucun calcul ne change.
  Recommandation (confiance 0,8) : l'addendum d'empreintes déclare ce lieu et liste les 18 fichiers par empreinte ; à défaut,
  copie octet pour octet sous `code-v1/` comme pièce, jamais exécutée.
- **E-2, monde jouet du jeu synthétique** : [T] l. 309-312 dit « construit comme l'essai de [CL] » et « graines (97, g) » ; le
  programme `01c648a0…` tire les lois (S1, S2, P, Q) **une fois**. Le code tire, pour chaque génération g, ses lois **et** ses
  issues de la graine `(97, g)` (la seule clé que le texte donne). Enjeu : la mise à mort de la mutation se lit sur un
  mélange de mondes jouets au lieu d'un seul. Avec une racine d'essai (pas celle du texte) : lecture saine, moyenne 0,444,
  intervalle [0,398 ; 0,497] ; lecture mutée, moyenne 2,536, borne basse 2,364 > 1 (tuée) — sur un seul monde, la contre-
  lecture avait 2,618 ± 0,225. Options : (a) garder (chaque génération porte sa graine, recommandation, confiance 0,6) ;
  (b) lois tirées une fois, d'une clé que le texte ne donne pas (écart plus large). Ce point est peut-être une simple lecture
  plutôt qu'un écart ; je le classe en nœud par prudence.
- **Coût (non un écart de critère, à signaler)** : [T] l. 519-524 compte 0,12 à 0,20 s par évaluation (mesure de [BANC-v1],
  annexe B, sur une archive à **deux** lois et 7 membres). Avec l'archive A2 (quatre lois, 17 membres, dont l'ajustement
  linéaire à sept colonnes recalculé à 32 instants), j'ai mesuré 0,5 à 1,7 s par évaluation à 800 tirages (temps
  processeur ≈ 0,55 à 1,1 s selon la génération). La borne dure de 24 h (liste d'arrêt) n'est pas menacée (section « Durée »).

## Essais

Suite concernée : **109 essais, tous verts** — 108 en 373 s passés par `lancer_essais` (le chemin même du contrôle avant jeu du lanceur), puis le fichier d'enchaînement rejoué seul après l'ajout d'un dix-septième essai (17 sur 17, 178 s). Essais d'infrastructure du dépôt touchés par le lanceur (`test_manifeste`, `test_scellement`,
`test_prereg`, `test_run_factice`) : 30 sur 30, verts.

| fichier | essais | objet |
|---|---|---|
| `test_organisme_idees_juge_lois_v1.py` | 9 | évaluateur vectorisé = juge réel (≤ 10⁻¹², toutes les formes du banc) ; refus d'un type hors du banc ; tirage par inversion = `tirer_categorie` ; cosinus ; coupures et seuils ; composantes valides par `valider_loi`, V4 de signe opposé refusé ; direction bruitée ; doublons ; cellules ; Dirichlet |
| `test_organisme_idees_juge_banc_v1.py` | 14 | copie du juge (saine ; altérée : refus) ; racine et clés ; archive A2 ; composition, validité, déterminisme ; règle du cosinus (O1, O2) ; ordre du gel ; flux propre ; oracle avant les issues fraîches ; caches égaux ; évaluation filtrée = `evaluer_v2` ; montage = `juger_carte` (analyse syntaxique) ; Λ et domination ; E1 (sain, fuite) ; 50 cartes de E1 |
| `test_organisme_idees_juge_rejeu_v1.py` | 50 | garde d'accès ; budget ; ordre des tours ; arrêts bas et haut ; bras sur trajectoires d'essai ; vérificateur indépendant et propriétés (P et P′ ≥ A) sur 40 jeux tirés au hasard ; placebo reproductible ; valeur e et e-BH = juge (200 cas) ; garde m ; garde du budget ; G |
| `test_organisme_idees_juge_lecture_v1.py` | 14 | seuils de l'annexe B (13/39 ; 13/38 ; 4/23) ; cas sain ; chaque défaut de l'étage 1 (membre exact N et T, domination, non tenue, borne basse) ; étage 1 bis et audit par monde ; ordre de la principale ; qualifications ; zone utile ; lecture refusée avant scellement ; appariement ; run incomplet |
| `test_organisme_idees_juge_mutations_v1.py` | 5 | banc complet (synthétique 20 000 générations, 10 000 rééchantillons, racine d'essai) ; artefact de `exiger_toutes_tuees` ; lot = génération par génération ; mutation tuée pour une autre raison = survivante |
| `test_organisme_idees_juge_execution_v1.py` | 17 | durée ; réseau ; écriture scellée ; addendum ; enchaînement (oracle scellé avant le rejeu, phases dans l'ordre) ; oracle altéré ; arrêt consigné ; E1 en échec ; processus ; lanceur : préenregistrement altéré, arbre sale, sortie existante, addendum absent ; miniature hors du dépôt et racine distincte ; lecteur ; `lancer_essais` (code ≠ 0 refusé) |

**Liste d'arrêt de [T] (l. 504-515), chaque garde sur un cas sain et un artefact (R5)** :

| ligne | garde | cas sain | artefact |
|---|---|---|---|
| fichier gelé ≠ addendum ; essai qui échoue ; mutation qui survit | `verifier_addendum` ; `lancer_essais` ; `exiger_toutes_tuees` | addendum scellé conforme ; suite verte ; banc tout tué | addendum non scellé, fichier absent ou modifié ; code de sortie ≠ 0 simulé : refus ; mutation survivante |
| E1 : préfixe non égal | `essai_E1_carte`, `executer` | carte réelle à 25, 400, 800 | évaluation qui lit les issues au-delà de t ; E1 en échec : arrêt avant l'oracle |
| issue fraîche avant le gel ou lue par la construction | `Generation` | chaîne dans l'ordre | tirage avant gel ; flux ouvert avant la construction ou pendant ; engagement modifié après le gel |
| règle qui lit au-delà des tirages donnés | `Vue.lire` | lecture des révélés | lecture de l'instant suivant (mutation sur G) |
| tirages > B ou > 6 000 | `Budget`, `jouer_bras` | A = 4 800, F125 = 6 000 | A sans budget ; F125 à 11 blocs ; blocs non comptés |
| domination franchie | `domination`, étage 1 | carte « monde » : W ≤ Λ | valeur au-dessus de Λ : « garantie mise en défaut », le run va à son terme (aucun arrêt dans le jeu) |
| exception, log W non fini | `EvaluationFiltree`, `consigner_arret` | trajectoire finie | valeur infinie ; exception en cours de jeu : `arret.json` scellé, pas de `jeu.json` |
| durée murale > 24 h | `GardeDuree` | 9 s sur 10 | 11 s sur 10 |
| lecture avant scellement ; oracle après le rejeu | `charger_sortie` ; `executer` | sortie scellée lue | sortie non scellée refusée ; oracle altéré au départ du rejeu : pas de `jeu.json` |
| dépense, appel de modèle | `installer_garde_reseau` | aucun appel | connexion refusée |

## Banc de mutations (étape 0)

Toutes tuées pour la raison attendue (répétition miniature et essai complet ; message de la garde cité au rapport du banc) :

| mutation | tuée par |
|---|---|
| la règle lit un instant non révélé (G lit le bloc suivant) | garde d'accès (« instant non révélé ») |
| budget dépassé (A ignore le budget restant) | garde du budget (« tirages donnés > budget ») |
| garde du budget contournée (blocs révélés sans être comptés) | recompte (« garde du budget contournée ») |
| arrêt bas avant 50 tirages | vérificateur indépendant (« allocation non conforme ») |
| plafond ignoré | `Vue.reveler` (« plafond de 800 ») |
| hasard du placebo tiré des issues | vérificateur indépendant (graine `(f, g, 1000)`) |
| m compté après coup | garde m (« m compté après coup ») |
| flux d'issues partagé entre deux cartes | registre des flux (« partagé ») |
| issues fraîches tirées avant le gel | machine à états (« avant le gel ») |
| issues fraîches passées à la fonction qui bâtit un engagement | registre des flux au gel (« issue fraîche tirée avant le gel ») |
| valeur e lue au maximum de la trajectoire | **lecture (3) sur le jeu synthétique** (borne basse > 1 ; raison exigée par [T]) ; en plus, recoupement avec la valeur e du juge dans le rejeu |
| F lu sur `promue`, `t_promotion`, `log_richesse_max`, `log_richesse_arretee` (quatre) | évaluation filtrée (« champ … interdit ») |
| oracle calculé sur les issues jugées (deux formes) | garde d'ordre de l'oracle ; provenance de l'échantillon |

Jeu synthétique complet (20 000 générations, 10 000 rééchantillons, racine d'essai) : lecture saine moyenne 0,444
[0,398 ; 0,497] ; lecture mutée moyenne 2,536, borne basse 2,364 : **tuée**. Aucune domination franchie dans le monde jouet.
Durée : environ 2 min. Au jeu réel, le lanceur rejoue ce banc avec la racine du texte (`(97, g)`), avant le manifeste.

## Répétition miniature

Commande : `python -I -B scripts/jouer_idee_1_2_v1.py --miniature --sortie <bloc-notes>/miniature-v2 --n-T 5 --n-N 5
--processus 2 --synthetique 1000 --reechantillons-synthetiques 1000 --reechantillons-lecture 1000` ; racine d'essai
`sha256("repetition miniature, idee 1.2, v1 …")`, distincte de celle du texte (garde : refus de la racine du texte) ; sortie
hors du dépôt. Générations : T 0 à 4, N 0, 1, 2, 250, 251 (les deux mondes). Contrôles réduits : banc de mutations (18 sur
18 tuées, synthétique de 1 000 générations), E1 sur deux cartes (T g = 0 porteuse, N g = 0 membre exact ; 32 instants ; aucun
échec). Puis oracle scellé, jeu, sortie scellée, lecture gelée (1 000 rééchantillons) : cinq fichiers scellés, tous vérifiés.
**Je n'ai lu de la lecture que la liste de ses clés** (aucun chiffre de couverture, de promotion ni d'étage : ce serait un
pilote). Aucune fausse construite au plafond du cosinus dans ces dix générations (construction). Durée murale : 255 s.
Premier passage : un **défaut trouvé** par la répétition (E1 à t = 800 itérait sur l'évaluation filtrée) ; la garde a arrêté
proprement (`arret.json` scellé, ni oracle ni jeu) ; corrigé (`trajectoire_de`), essai ajouté (instant 800).

Mesures (machine à 4 cœurs **chargée par d'autres processus**, charge moyenne ≈ 11) :
- jeu (24 évaluations, Λ, sept bras et vérificateur) : 12,9 à 54,9 s par génération et par processus (moyenne 33,1) ; avec
  deux processus, 17,3 s murales par génération ;
- oracle : 3,7 s par génération et par processus (2,0 s murales à deux processus) ;
- E1 : 49,9 s par carte ;
- temps processeur propre, un processus (même charge) : jeu 20 à 27 s, oracle 1,4 à 2,8 s par génération ; les 24
  évaluations du juge en font l'essentiel (EM de l'ajustement linéaire, `nul_filles_v2._lineaire`).

## Durée estimée du run réel

- Contrôles avant jeu : essais ≈ 5 à 8 min ; banc de mutations complet ≈ 2 à 3 min.
- E1 : 50 cartes × ≈ 40 à 50 s, sur deux processus : ≈ 17 à 21 min.
- Oracle : 1 250 × 1,5 à 3 s de processeur, sur deux processus : ≈ 15 à 30 min.
- Jeu : 1 250 × 13 à 27 s de processeur, sur deux processus : ≈ 2,3 à 4,7 h.
- **Total : ≈ 3 à 5,5 h sur deux processus d'une machine libre ; ≈ 7 h sous une charge comme celle d'aujourd'hui** (17,3 s
  murales par génération mesurées). Sous la borne de 24 h, sans marge à craindre. Temps processeur total ≈ 5 à 10 h d'un cœur, quand le registre (R-2886)
  annonçait 1,5 à 2,5 h d'un cœur : trois à six fois plus.

## Ce qui reste non éprouvé

- Le run réel (racine du texte, 1 250 générations) ; l'essai E1 sur les 50 cartes réelles ; le banc de mutations avec la
  racine du texte ; le chemin `lancer_essais` est éprouvé (la suite ci-dessus est passée par lui), pas l'enchaînement complet du
  mode décisif (il exige un arbre propre, donc un commit, et l'addendum).
- La tenue numérique des ajustements du nul sur 1 250 générations (une exception arrête le run : `arret.json`, relance
  seulement sous un texte ou un addendum neuf) ; la fréquence du repli au plafond du cosinus sur tout le banc (aucun sur dix
  générations d'essai ; V4 n'y figure pas, il n'est vu que par les essais sur la cellule 6).
- La lecture gelée sur 500 et 750 générations réelles (éprouvée sur des sorties fabriquées et sur la miniature).
- Contre-lecture du code par un autre modèle et addendum d'empreintes scellé : à faire avant tout jeu ([T] l. 467).

## Ce que je n'ai pas fait

Aucun jeu du préenregistrement ; aucune lecture de résultat (la miniature et les essais emploient des racines d'essai, et je
n'ai pas lu les chiffres de la lecture miniature) ; aucun commit ; aucune modification d'un fichier existant du dépôt.
Sorties jetables, hors du dépôt : `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/miniature-v2/`
(répétition conforme) et `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/miniature-v1-arret-E1/`
(premier passage, arrêt de E1).
