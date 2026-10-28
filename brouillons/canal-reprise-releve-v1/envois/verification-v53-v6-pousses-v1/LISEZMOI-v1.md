# Organismes v5.3 et v6 poussés par Gemini : vérification en isolation (v1)

Écrit le 25 octobre 2026 (vers 15 h UTC) par un sous-agent de vérification. Aucune commande git, aucun accès réseau,
aucun sous-agent. Seuls ont été exécutés les essais des deux organismes et les deux outils d'essai
(`invariance_v1.py`, `verrous_imbriques_v1.py`), en isolation. Tout le reste est de la lecture : `diff`, `sha256sum`,
et des analyses de l'arbre syntaxique faites par mes outils (`outils-v1/`, lancés avec `python -I`), qui lisent les
fichiers sans jamais les exécuter. Rien n'a été écrit hors de `/var/tmp/verification-v53-v6-pousses-v1/`. Les
empreintes de tous les journaux et différences cités sont dans `EMPREINTES-v1.txt`.

## Verdict

- **v5.3 poussée** (`4ecba58`, 22 fichiers, `6251ab21…`). Même code que la reconstitution : les arbres syntaxiques sont
  identiques, seuls des docstrings et des commentaires ont disparu. 39 essais passés, 0 échec. Relevés identiques sous
  les graines de hachage 0, 1 et 2, cette fois vraiment appliquées. 0 appel imbriqué sous `_VERROU`. Gardes C-01 à C-13
  présentes. **Aucune des neuf réserves de la reconstitution n'est levée.**
- **v6 poussée** (`7cd7508`, 24 fichiers, `940c59c3…`). 43 essais passés, 0 échec. Relevés stables d'une graine à
  l'autre. 0 appel imbriqué. Gardes présentes, aucune réserve levée. **Mais il y a un défaut bloquant.** Toute mutation
  acceptée écrit pour le successeur un `politique_endogene.py` qui ne peut pas s'importer : `ast` n'y est pas importé,
  et le filtre interdit justement de l'importer. Or le noyau ne contrôle que la syntaxe : il laisse passer ce
  successeur. S'y ajoutent quatre problèmes :
  - le filtre de propreté accepte des règles non propres, et ne borne ni le niveau ni l'échelle du score ;
  - le code candidat s'exécute sans borne de temps ;
  - 3 des 4 fonctions réécrites ne sont jamais appelées ;
  - la récompense interne change même sans mutation, ce que Gemini n'annonce pas.

## 1. Provenance

| objet | chemin | empreinte d'arbre (`boucle.empreinte_arbre`) | fichiers |
|---|---|---|---|
| v5.3 poussée | `/var/tmp/verif-pousses-v53-v6/v53/organisme/` | `6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753` (conforme) | 22 |
| v6 poussée | `/var/tmp/verif-pousses-v53-v6/v6/organisme/` | `940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a` (conforme) | 24 |
| reconstitution v5.3 | `/var/tmp/reconstitution-v5-3-v1/organisme/` | `a119fa0f6f1e7ca5884acf66c90b74ca165af4012b257cc6a9643de0496fec55` (conforme) | 22 |
| base v5.2.1 | `/var/tmp/verif-v521/o/organisme/` | `fec005c6626b3d1aa960702e4322b44ade3b902157dd84eae8e658b70e4f43f4` (conforme) | 21 |

- **Rapport de livraison de Gemini** : `/mnt/user-data/attachments/3a0c40e9-…/44e7245a-attachment.txt`, 9 053 octets,
  109 lignes, sha256 `5792fc8820b13c987d4a883b14a9292dd58d83c2968c258356c35e76bb9d4f04`. Lu comme une donnée.
- **Outils**, mêmes empreintes que pour la reconstitution :
  - `invariance_v1.py` : `1fe2609c5ff7ab83…` ;
  - `verrous_imbriques_v1.py` : `404d66c237971cd8…`.
- **Interpréteur** : `/opt/venv-essaim-sim-v1/bin/python`, Python 3.13.17, pytest 9.1.1.
- **Noyau**, lu sans modification : `/home/claude/noyau-cles/essaim-m3-refonte-v1/`.

## 2. Méthode

- **Copies d'essai.** Chaque copie est faite à part par `cp -a`, puis passée à `nobody` par `chown -R` :
  `essais-v1/pytest-<v>/organisme` et `essais-v1/invariance-<v>-<cas>-s<graine>/organisme`. J'ai recontrôlé leurs
  empreintes avant les essais et après : elles sont inchangées.
- **Commande** : `unshare -n sudo -u nobody env -i PATH=/usr/bin:/bin HOME=<dossier> LANG=C.UTF-8
  TMPDIR=<dossier>/tmp PYTHONDONTWRITEBYTECODE=1 [PYTHONHASHSEED=n] /opt/venv-essaim-sim-v1/bin/python -P -s -B …`.
- **Graine de hachage** (`verification-v1/sonde-graine-hachage-v1.log`). Sous `-P -s -B`, chaque graine donne deux fois
  la même valeur de `hash("a")` :

  | graine | valeur de `hash("a")`, deux lancements |
  |---|---|
  | 0 | `4644417185603328019`, deux fois |
  | 1 | `-3012895188637184397`, deux fois |
  | 2 | `6352457989142756797`, deux fois |

  Témoin : sous `-I`, la graine 0 donne deux valeurs différentes, car `-I` fait ignorer la variable.
- **Réseau** : coupé. Une connexion tentée dans l'espace de noms est refusée (`OSError` 101, réseau injoignable).
- **Écritures.** pytest a mis ses dossiers temporaires sous `essais-v1/pytest-<v>/tmp/`. Aucun fichier de `nobody` n'a
  été écrit ailleurs : une recherche `find -newer -user nobody` sur `/tmp`, `/var/tmp`, `/home`, `/root`, `/opt/venv…`
  et `/mnt/user-data` revient vide. Les dossiers `/tmp/pytest-of-nobody/pytest-0` à `pytest-11` sont plus anciens que
  cette vérification (dernier à 14:32, heure de la machine, avant le début à 14:47).

## 3. Fichiers et différences (résultat 1)

Les inventaires sont dans `verification-v1/inventaire-*-v1.txt`, et les empreintes fichier par fichier dans
`verification-v1/sha256-fichiers-*-v1.txt`.

| comparaison | ajoutés | changés | inchangés |
|---|---|---|---|
| base v5.2.1 → v5.3 poussée | `tests/test_emprunts_v5_3.py` | `CONCEPTION.md`, `manifeste.json`, `memoire_isvd.py`, `principal.py` | 17 |
| base v5.2.1 → v6 poussée | `politique_endogene.py`, `tests/test_auto_architecte_v6.py`, `tests/test_emprunts_v5_3.py` | les mêmes 4 | 17 |
| v5.3 poussée → v6 poussée | `politique_endogene.py`, `tests/test_auto_architecte_v6.py` | `manifeste.json`, `principal.py` | 20, dont `CONCEPTION.md` et `memoire_isvd.py` |
| reconstitution → v5.3 poussée | — | `memoire_isvd.py`, `principal.py`, `tests/test_emprunts_v5_3.py` | 19 |

Les 34 essais hérités de la v5.2.1 sont inchangés octet pour octet (les 7 fichiers `tests/` de la base).

Différences unifiées, dans `verification-v1/diff-<comparaison>-<fichier>-v1.txt` :

| comparaison | fichier | lignes ajoutées | lignes retirées |
|---|---|---|---|
| base → v5.3 | `CONCEPTION.md` | 18 | 1 |
| base → v5.3 | `manifeste.json` | 4 | 4 |
| base → v5.3 | `memoire_isvd.py` | 115 | 7 |
| base → v5.3 | `principal.py` | 257 | 26 |
| base → v5.3 | test ajouté | 215 | — |
| base → v6 | `principal.py` | 405 | 30 |
| v5.3 → v6 | `manifeste.json` | 3 | 3 |
| v5.3 → v6 | `principal.py` | 149 | 5 |

Les fichiers `diff-base-v521-vers-v6-poussee-*` donnent aussi les autres fichiers changés depuis la base.

**v5.3 poussée contre la reconstitution** (`verification-v1/comparaison-ast-reconstitution-vers-v53-poussee-v1.txt`).
Ce qui change, fichier par fichier :
- **`memoire_isvd.py`** : 11 lignes retirées, toutes des docstrings et des commentaires. 12 165 octets deviennent
  11 121.
- **`principal.py`** : 25 lignes retirées et 3 lignes raccourcies, toutes des docstrings et des commentaires.
  85 296 octets deviennent 82 879. Parmi les commentaires retirés figurent ceux qui renvoyaient à C-12 (deux fois) et
  à C-13 (en-tête, `_sanitiser_donnee_externe` et docstring de `_bloc_moisson_borne`). Le code de ces gardes reste en
  place, et `CORRECTIONS-v3.md` et `CORRECTIONS-v4.md` sont inchangés.
- **Arbres syntaxiques** : docstrings retirées, ils sont identiques pour les deux modules.
- **`tests/test_emprunts_v5_3.py`** : la docstring et des commentaires sont retirés, et une boucle de `predire` (faux
  noyau) est réécrite en compréhension de dictionnaire. L'effet est le même : 0,94 pour `te_clair`, 0,52 sinon.
- **Effet sur les réserves** : aucun. Le code jugé par la reconstitution est celui qui a été poussé. Sa réserve 3
  (hypothèses de la reconstitution, branche poussée à comparer) est donc close : le code est identique.

**v6 contre la v5.3 poussée.** `principal.py` change par cinq points :
- `import politique_endogene`, au niveau du module (l. 22), et `VERSION` ;
- `_calculer_score_bregman_tsallis` (l. 888-896) appelle `politique_endogene.recompense_interne`, avec un repli
  silencieux sur l'ancienne formule ;
- une nouvelle fonction, `_synthetiser_mutation_politique_endogene` (l. 899-1013) ;
- `_propager_successeur` (l. 1454-1473) écrit le fichier muté ;
- `executer` appelle la mutation (l. 1870-1879) et ajoute la clé `mutation_politique_endogene` (l. 2015-2017).

Ailleurs, par analyse syntaxique, 35 fonctions sont inchangées (`verification-v1/fonctions-ast-base-v53-v6-v1.txt`),
de même que `memoire_isvd.py`. **`CONCEPTION.md` n'est pas modifié par la v6** : il ne mentionne nulle part
`politique_endogene` ni l'auto-réécriture.

## 4. Essais en isolation (résultat 2)

Commande : `python -m pytest -q -p no:cacheprovider organisme/tests`, lancée depuis `essais-v1/pytest-<v>/`.

| version | résultat | code de sortie | journal |
|---|---|---|---|
| v5.3 poussée | `39 passed in 4.56s` | 0 | `verification-v1/pytest-v53-poussee-v1.log` |
| v6 poussée | `43 passed in 4.68s` | 0 | `verification-v1/pytest-v6-poussee-v1.log` |

Le détail essai par essai (`-v`) est dans `pytest-<v>-poussee-detail-v1.log`. On y trouve :
- 11 essais dans `test_corrections_v1.py`, 3 dans `_v2`, 1 dans `_v3` et 5 dans `_v4` ;
- 8 dans `test_moissonneur_v5.py`, 3 dans `test_organisme.py`, 3 dans `test_question_ouverte_v4.py` ;
- 5 dans `test_emprunts_v5_3.py`, et en v6, 4 dans `test_auto_architecte_v6.py`.

Les essais de garde `test_c01` à `test_c13` passent tous ; C-09 est couverte par
`test_c08_confiance_non_finie_et_c09_json_imbrique`. Les nombres sont conformes à l'annonce : 39 et 43.

Une remarque sur le rapport de Gemini : il donne deux durées pour une même exécution, 9,36 s dans l'en-tête et 6,43 s
dans la ligne de pytest (8,8 s et 6,65 s pour la v6). L'en-tête n'est donc pas une sortie brute de pytest.

## 5. Reproductibilité à graine de hachage fixe (résultat 3)

`invariance_v1.py`, cas B et D, `PYTHONHASHSEED` = 0, 1 et 2. Journal : `verification-v1/invariance-v53-v6-poussees-v1.log`.
Relevés : `verification-v1/releve-invariance-<v>-<cas>-s<n>-v1.json`.

| version | cas | appels `appeler` | `budget()` / `especes()` | recherches / téléchargements | sha256 des 3 relevés |
|---|---|---|---|---|---|
| v5.3 | B | 28 | 46 / 1 | 0 / 0 | `e5927040eaee2f2e…`, identique pour les trois |
| v5.3 | D | 29 | 53 / 1 | 2 / 1 | `d85e7d3e40d750a7…`, identique pour les trois |
| v6 | B | 28 | 46 / 1 | 0 / 0 | `84f355fc619269fa…`, identique pour les trois |
| v6 | D | 29 | 53 / 1 | 2 / 1 | `d26a36c8d6089ce0…`, identique pour les trois |

- **v5.3.** Ses relevés sont identiques à ceux de la reconstitution (`e5927040…` et `d85e7d3e…`). L'invariance tient
  donc sous des graines vraiment fixées, ce qui lève la réserve 1 (graine) de la reconstitution.
- **Successeurs** (`verification-v1/successeurs-invariance-v1.txt`). L'outil écarte `successeur/organisme/` de son
  relevé ; je l'ai donc empreinté à part. Il est identique d'une graine à l'autre :
  - v5.3 : B `180d9b8f…`, D `5f9f98cd…` ;
  - v6 : B `ff89e1d2…`, D `5fc81d0e…`.

  En v6, `politique_endogene.py` y est recopié tel quel (`55f0d0b7…`) : l'outil ne déclenche aucune mutation, car
  l'historique n'a qu'une entrée et la phase n'est pas « conception ».
- **v6 contre v5.3** (`verification-v1/comparaison-invariance-v53-vers-v6-v1.txt`,
  `differences-fichiers-v53-vers-v6-invariance-v1.txt`).
  - Identiques : les consignes, une à une par empreinte, les rôles, les comptes de `budget()` et d'`especes()`, les
    recherches et téléchargements, `reponses_test.json` et `reponse-question.md`.
  - Différents :
    - `journal_generation.json` : version, et la clé `mutation_politique_endogene` ;
    - `memoire_isvd.json` : Sigma, U et les exemplaires, soit 228 valeurs en B et 232 en D ;
    - `metrique_proposee.json` : `valeur` passe de **0,231448 à 0,195747**, en B comme en D.

  La cause : la récompense interne n'est plus la même formule (§ 9.7). À la lecture, les consignes de la génération
  suivante différeront aussi, car elles contiennent le résumé de cette mémoire. Ce point n'a pas été exécuté : l'outil
  ne fait qu'une génération.

## 6. Verrous (résultat 4)

Journal : `verification-v1/verrous-imbriques-v53-v6-v1.log`.

- **`verrous_imbriques_v1.py` sur `principal.py`** : **0 appel imbriqué**, en v5.3 comme en v6. Six fonctions prennent
  `_VERROU` : `_consigner_erreur`, `_enregistrer_appel`, `_enregistrer_recherche`, `_enregistrer_telechargement`,
  `_entrainer_et_predire_sondes_traits`, `_faut_basculer`. Sur `memoire_isvd.py`, `mitose_spectrale.py` et
  `politique_endogene.py`, aucune fonction ne prend `_VERROU`. `politique_endogene.py` ne cite « threading » que dans
  sa liste de noms interdits (l. 62).
- **Mon complément** (`outils-v1/verrous_transitifs_v1.py`, `verification-v1/verrous-transitifs-v53-v6-v1.txt`). L'outil
  ne voit que les appels directs ; j'ai donc suivi aussi les chaînes d'appels internes au module. Résultat : **0 appel
  imbriqué, chaînes comprises**, et aucun `acquire` ni `release` explicite. En v6, la fonction
  `_synthetiser_mutation_politique_endogene` prend le verrou par `_enregistrer_appel`, jamais en le tenant déjà.

## 7. Gardes C-01 à C-13 (résultat 5)

Constats faits d'après le code et l'analyse syntaxique (`verification-v1/fonctions-ast-base-v53-v6-v1.txt`,
`c01-octets-v53-v6-v1.txt`). Les lignes de la v6 sont entre parenthèses.

| garde | v5.3 poussée | v6 poussée |
|---|---|---|
| C-01 | Aucun `.py` ni `.json` n'a de marque d'ordre d'octets ni de retour chariot. `CONCEPTION.md` garde ses caractères de contrôle hérités (2 retours chariot isolés, 4 tabulations, sonnerie, retour arrière, saut de page) : C-01 laisse les `.md` tels quels. | idem, `politique_endogene.py` compris |
| C-02, C-09 | `_parser_decision_tache` (l. 613) et `_extraire_json_candidat` (l. 578) sont inchangées. | inchangées (l. 614, l. 579) |
| C-03 | Les étiquettes sont lues dans chaque tâche (l. 1390). La sonde prend `etiquettes[0]` et `etiquettes[1]` de la tâche (l. 1412). | idem (l. 1520, l. 1542) |
| C-04 | `_selection_stratifiee` (l. 895) est inchangée ; elle passe à 4 vérifications en conception seulement (l. 1644). | idem (l. 1016, l. 1775) |
| C-05 | `_ecrire_reponses` et `_temps_ok` sont inchangées. Les écritures de fin restent dans le `finally` (l. 1743). | Idem (`finally` l. 1885). **Faiblesse nouvelle** : l'`exec` du candidat (`politique_endogene.py`, l. 132) et ses 14 évaluations (l. 69-70) n'ont aucune borne de temps. Ils tournent dans le `try` d'`executer`, avant le `finally`. Une boucle sans fin bloquerait la génération jusqu'au délai du bac à sable : mémoire, métrique, journal et successeur ne seraient pas écrits. Les réponses déjà écrites tâche par tâche restent. |
| C-06 | Les nouveaux compteurs sont tenus sous verrou (l. 524, 534). `_faut_basculer` est inchangée. | idem (l. 525, 535) |
| C-07 | `charger_connaissances_archive` est inchangée. Quelques replis silencieux nouveaux, déjà relevés par la reconstitution : `memoire_isvd.py` l. 107 ; `principal.py` l. 544-548. | Les mêmes, plus deux nouveaux : l. 891-896, où toute exception de `recompense_interne` fait revenir en silence à l'ancienne formule, et l. 958-959, où des paramètres illisibles prennent des défauts en silence. Le rejet d'une mutation, lui, est consigné (l. 1010). |
| C-08 | `_confiance_finie` est inchangée ; les probabilités de `predire` y passent (l. 560). | idem (l. 561) |
| C-10, C-11 | Le dossier `metrique/` est identique à la base. | idem |
| C-12 | 0 appel imbriqué, chaînes comprises (§ 6). | idem |
| C-13 | `OUVERTURE_MOISSON` et `FERMETURE_MOISSON` sont présentes (l. 24-25). `_bloc_moisson_borne` (l. 914) et `_sanitiser_donnee_externe` sont inchangées, avec `replace("===", "= =")` (l. 252). Les 5 essais de `test_corrections_v4.py` passent. Seuls les commentaires qui citaient C-13 ont été retirés. | idem (l. 25-26, l. 1035, l. 253) |

## 8. Les neuf réserves de la reconstitution (résultat 6)

Ce sont les points 1 à 9 du § 11 de `/var/tmp/reconstitution-v5-3-v1/LISEZMOI-v1.md`. Les lignes de la v6 sont entre
parenthèses. Les lignes de `memoire_isvd.py` sont les mêmes dans les deux versions, puisque le fichier est identique.

| n° | réserve | v5.3 poussée | v6 poussée |
|---|---|---|---|
| 1 | « Sans traits, flux identique à la v5.2.1 » est faux | **Non levée.** La consigne vaut « entre 4 et n » avec n = max(4, min(10, recherches)) (l. 716, 720). Un `budget()` s'ajoute si des traits sont servis (l. 472). Côté mémoire : `memoire_isvd.py` l. 178-180, 212-214 et 280-285. | **Non levée** (l. 717, 721, 473), et aggravée : même sans mutation, la récompense interne change, donc la mémoire et la métrique aussi (§ 5). |
| 2 | Perte de la sonde non propre (Brier + 0,08 × Tsallis) | **Non levée** (l. 44-49, employée l. 511) | **Non levée** (l. 45-50, l. 512). `politique_endogene.code_objectif_sonde()` rend une perte propre, mais elle n'est jamais appelée (§ 9.7). |
| 3 | Vote de la sonde dès une exactitude de 0,60, quelle que soit la marge | **Non levée** (l. 1410-1416) | **Non levée** (l. 1540-1546) |
| 4 | « La sonde incertaine force l'arbitrage » : sans effet | **Non levée** (l. 1454-1456) | **Non levée** (l. 1584-1586). Les seuils de `seuils_routage()` ne sont pas lus : 0,32, 0,18, 0,78 et 0,35 restent écrits en dur. |
| 5 | La garde d'exactitude porte sur l'exactitude d'entraînement | **Non levée** (l. 547, l. 1410) | **Non levée** (l. 548, l. 1540) |
| 6 | Journal d'ablations : il faut Δ > 0,005 pour « CONFIRME », pas Δ > 0 | **Non levée** (`memoire_isvd.py` l. 138-143) | **Non levée** (fichier identique) |
| 7 | « Multi-familles » détecté par mots-clés, bonus appliqué deux fois | **Non levée.** `memoire_isvd.py` : détection l. 81-85, poids × 1,15 l. 178-180, `energie_proj` × 1,15 l. 212-214. | **Non levée.** `ponderer_trace_memoire` ajoute un troisième jeu de mots-clés, mais elle n'est jamais appelée. |
| 8 | Rondes de conception comptées à partir de 0, alors que le noyau compte de 1 à R (`boucle.py` l. 850, 589, 619) | **Non levée** (l. 1800-1803) | **Non levée** (l. 1942-1945) |
| 9 | Paramètre `erreurs` annoncé, absent du code | **Non levée** (signature l. 460) | **Non levée** (l. 461) |

Une amélioration partielle en v6 : la récompense interne `recompense_interne`, combinaison de Brier (0,80) et du score
logarithmique borné (0,20), est maintenant strictement propre (§ 9.6). La v5.3 gardait la formule héritée, qui pousse
vers les extrêmes. Mais la v6 la garde comme repli silencieux (l. 891-896).

Les autres réserves de la reconstitution :
- **§ 12, réserve 1 (graine)** : levée (§ 5).
- **§ 12, réserve 2 (écritures dans `/tmp`)** : évitée ici grâce à `TMPDIR`.
- **§ 12, réserve 4 (caractères de contrôle)** : toujours là, dans `CONCEPTION.md`.
- **§ 12, réserve 6 (replis silencieux)** : toujours là, et la v6 en ajoute deux (§ 7, C-07).

## 9. Spécifique à la v6 : l'auto-réécriture de `politique_endogene.py` (résultat 7)

### 9.1. Déclenchement (`principal.py` l. 907-921)

La mutation est tentée dans trois cas :
- en phase « conception », à chaque ronde ;
- si `contexte["autoriser_mutation_code"]` est vrai, clé que Gemini n'annonce pas ;
- à partir de la génération 1, en cas de « stagnation », c'est-à-dire quand les deux derniers scores du noyau dans
  `historique` diffèrent de 0,01 au plus, baisse comprise.

Dans tous les cas, `_peut_appeler` doit être vrai : budget restant et garde de temps (l. 205-207). La mutation coûte
alors un appel de plus, de rôle `architecte_mutation_endogene`, plafonné à 8 192 jetons.

### 9.2. Ce que le code exécute

1. **Appel au modèle** (l. 923-941). La consigne contient Sigma et les deux dernières entrées du journal d'ablations,
   soit des nombres et des chaînes fixes : aucun texte moissonné.
2. **Deux chemins pour obtenir le candidat**, le premier prioritaire :
   - *code brut* : si la réponse contient un bloc ```` ``` ```` avec `def recompense_interne`, ce texte du modèle
     devient le candidat tel quel (l. 947-949) ;
   - *gabarit* : sinon, tout objet JSON lisible, même sans les clés attendues, remplit un gabarit fixe (l. 951-1002).
     Le nom est assaini (l. 953), les nombres sont bornés (l. 955-957), et des défauts silencieux s'appliquent
     (l. 958-959).
3. **Validation** par `politique_endogene.verifier_et_valider_code_politique` (l. 1008). Elle analyse le texte
   (`ast.parse`, l. 101), le filtre, puis le compile (`compile`, l. 130) et l'exécute (`exec`, l. 132) dans le
   processus de l'organisme, avec des fonctions intégrées réduites (l. 122-127). Elle teste ensuite les quatre fonctions
   (l. 136-155).
4. **Écriture** (l. 1465-1473) de `dossier_travail/successeur/organisme/politique_endogene.py`, à l'intérieur du dossier
   de travail : le candidat, suivi de tout ce qui vient après le premier marqueur `# ====…` du fichier courant, c'est-à-
   dire le vérificateur. **Le fichier écrit n'est jamais validé en entier** : seul le candidat l'est.
5. **Chargement par le successeur** : il n'y a ni `importlib` ni `exec` dans `principal.py`. Le successeur charge le
   module par l'`import politique_endogene` ordinaire de son `principal.py` (l. 22) quand le noyau le lance. Le module
   tourne alors avec les fonctions intégrées complètes.

### 9.3. Défaut bloquant : un successeur muté ne s'importe pas

- **Le constat.** Le gabarit, et tout candidat validé, commencent par `import math` seul : le filtre refuse tout autre
  import (l. 108-111) et tout `ImportFrom` (l. 58). L'`import ast` du fichier d'origine se trouve avant le marqueur
  (l. 4) ; il est donc remplacé par le candidat. Or le vérificateur recopié emploie `ast` dès le niveau du module, dans
  `NOEUDS_INTERDITS = (ast.ImportFrom, …)`.
- **La preuve, statique.** Les deux successeurs mutés produits par les essais v6 eux-mêmes ont été analysés
  (`outils-v1/noms_non_lies_v1.py`, `verification-v1/noms-non-lies-successeur-v6-v1.txt`). Ce sont
  `…/test_v6_auto_reecriture_effect0/travail_v6_mut/…` et `…/test_v5_3_phase_conception_ecr0/conception_c000/…`, ce
  dernier produit par l'essai de conception v5.3 tournant sur la v6. Résultat : seul import `math`, nom `ast` non lié
  à la ligne 48. Différence avec l'original : `verification-v1/diff-politique-originale-vers-successeur-essai-v6-mut-v1.txt`.
- **La conséquence.** `NameError` à l'import de `politique_endogene`, donc à l'import de `principal` dans le
  successeur : il ne peut pas tourner. Aucune mutation validée ne peut corriger cela, puisque le filtre interdit
  d'importer `ast`. Je ne l'ai pas exécuté, par respect de la règle, mais l'analyse statique suffit : c'est une
  référence de niveau module à un nom jamais lié.
- **Pourquoi l'essai ne le voit pas.** `test_v6_auto_reecriture_effective_dans_successeur_sous_stagnation` ne fait que
  chercher des chaînes dans le texte du fichier (l. 69-72). Il ne l'importe jamais.
- **Pourquoi le noyau ne le voit pas.** `contrat.valider_organisme` ne fait que `compile` chaque `.py`
  (`contrat.py` l. 293-297). Le successeur est donc déclaré valide.
- **Effet probable** (d'après `boucle.py` l. 771-795 et le contrat, l. 142-156 ; non exécuté). En conception, le
  successeur muté devient l'organisme de la ronde suivante, ou `g000-concu` si la ronde a déclaré sa fin. Or la v6
  tente la mutation à chaque ronde de conception, et la réussit dès que la réponse contient un objet JSON. La lignée
  risque donc d'entrer en génération 0 avec un organisme qui ne s'importe pas. En génération, la même chose se produit
  à chaque « stagnation ».

### 9.4. Le filtre de l'arbre syntaxique (`politique_endogene.py` l. 58-63, 96-115)

**Interdit**
- Les nœuds `ImportFrom`, `Global`, `Nonlocal`, `AsyncFunctionDef`, `Await` et `Yield`.
- Tout `import` autre que `math`.
- 24 noms : `eval`, `exec`, `compile`, `open`, `__import__`, `getattr`, `setattr`, `delattr`, `globals`, `locals`,
  `vars`, `input`, `breakpoint`, `exit`, `quit`, `os`, `sys`, `subprocess`, `socket`, `shutil`, `pathlib`, `threading`,
  `multiprocessing`, `ctypes`.
- Tout attribut dont le nom commence par `__`.
- Un code de moins de 50 caractères utiles, ou de plus de 25 000.

**Pendant la validation seulement**, les fonctions intégrées sont réduites à 18, plus un `__import__` qui ne rend que
`math` (l. 117-127).

**Autorisé**, parce que c'est une liste noire : tout le reste. En particulier :
- les boucles `while` et `for`, et la récursion ;
- `lambda`, les classes, les compréhensions, `try` / `raise`, `with`, `del` ;
- l'affectation d'attributs, y compris ceux du module `math` réel, qui est passé dans l'espace d'exécution (l. 127) et
  partagé par tout le processus ;
- les noms à double souligné, à l'exception de `__import__` : seuls les *attributs* en `__` sont filtrés.

### 9.5. Ce qu'un code engendré peut faire

| capacité | constat |
|---|---|
| Lire ou écrire hors du dossier de travail | Aucun moyen direct : `open`, `os`, `pathlib`, `shutil` et `sys` sont interdits par leur nom, et seul `math` peut s'importer. Mais la liste noire a des manques de principe (§ 9.4). Dans le successeur, le module s'importe avec les fonctions intégrées complètes, et le fichier final n'est pas validé en entier. **Je ne peux pas conclure que c'est impossible.** Je n'ai pas cherché de contournement, et rien n'a été exécuté en ce sens. La seule barrière sûre reste le bac à sable du noyau (utilisateur dédié, réseau coupé). La seule écriture du mécanisme est faite par `principal.py`, dans le dossier de travail (l. 1473). |
| Ouvrir le réseau | Aucun moyen direct (`socket` interdit, aucun import autre que `math`). Même réserve de principe. Le réseau reste coupé par le noyau. |
| Lancer un processus | Aucun moyen direct (`subprocess` et `os` interdits). Même réserve de principe. |
| Prendre un verrou | Non. `threading` est interdit, et `_VERROU` vit dans `principal`, que le module n'importe pas. |
| Boucler sans fin | **Oui.** `while True` et une récursion sans fin passent le filtre. L'`exec` de validation (l. 132) et les 14 évaluations (l. 69-70) n'ont aucune borne, ni de temps ni de mémoire. La génération bloque avant le `finally` (§ 7, C-05). Dans un successeur qui s'importerait, le code de niveau module tournerait aussi à l'import. |
| Changer le score qu'il rend | **Oui.** Le `recompense_interne` du successeur est le code engendré. Il fixe le poids des traces (l. 1797-1800), donc la mémoire, et `score_interne_moyen` (l. 1935-1938). Celui-ci décide la fin de la conception (seuils 0,78 et 0,65, l. 1943-1944) et la `valeur` de la métrique proposée (l. 1960). Le filtre de propreté ne contraint ni le niveau ni l'échelle (§ 9.6). Il ne contrôle pas non plus un comportement qui changerait d'un appel à l'autre, ni hors des 7 points de la grille. Le score externe du noyau n'est pas calculé à partir de cette récompense, mais la déclaration de fin de conception l'est. |

### 9.6. Le filtre de « propreté stricte » (`politique_endogene.py` l. 66-93)

**Ce qu'il fait** : une grille de 7 valeurs de q (0,05 ; 0,15 ; 0,30 ; 0,50 ; 0,70 ; 0,85 ; 0,95).
1. Les valeurs doivent être finies et comprises entre −10 et 10.
2. R(1, q) doit croître strictement, et R(0, q) décroître strictement, d'au moins 1e-5 par pas.
3. Pour les 5 valeurs intérieures de p seulement, q = p doit battre les 6 autres points de la grille d'au moins 1e-5.

**Est-ce correct ?** Non. Ce sont des conditions *nécessaires*, vérifiées en quelques points, pas une preuve que
l'unique optimum est q = p :
- rien n'est contrôlé entre les points de la grille, ni aux extrémités p = 0,05 et p = 0,95 ;
- toute règle qui coïncide avec une règle propre sur ces 14 valeurs passe, quelle que soit sa forme ailleurs ;
- la propreté est invariante par a·R + b avec a > 0 : le niveau et l'échelle sont libres, alors que l'organisme compare
  ce score à des seuils absolus ;
- les marges absolues de 1e-5 rejettent à tort une règle propre de petite échelle.

**Essai** (`outils-v1/proprete_regles_v1.py`, `verification-v1/proprete-regles-v1.txt`). C'est **ma transcription** du
contrôle, d'après la lecture des lignes 66 à 93 ; le code de Gemini n'est ni importé ni exécuté. Elle est comparée à
l'optimum vrai de l'espérance, calculé sur une grille fine de pas 1e-4.

| règle | verdict du filtre | optimum vrai q* pour p = 0,70 / 0,90 | propre ? |
|---|---|---|---|
| Brier, 1 − (y − q)² | accepte | 0,700 / 0,900 | oui |
| logarithmique bornée (q borné à [1e-4, 1 − 1e-4]) | accepte | 0,700 / 0,900 | oui |
| v6 initiale : 1 − (0,80 Brier + 0,20 log) | accepte | 0,700 / 0,900 | oui |
| gabarit v6, poids de Brier 0,55 ou 0,95 | accepte | 0,700 / 0,900 | oui |
| constante 0,99 | rejette (monotonie) | — | non |
| linéaire : q si y = 1, 1 − q sinon | rejette (propreté, p = 0,15) | 0,9999 / 0,9999 | non |
| v5.3 interne : 1 − Brier + 0,1 Tsallis (repli de la v6, l. 891-896) | rejette | 0,740 / 0,9999 | non, sur-confiante |
| perte de sonde v5.3 prise comme récompense | rejette | 0,731 / 0,9999 | non, sur-confiante |
| sur-confiante légère : 1 − Brier + 0,10 (q − ½)² | **accepte** | **0,722 / 0,944** | **non** |
| sur-confiante forte : 1 − Brier + 0,30 (q − ½)² | rejette | 0,786 / 0,9999 | non |
| Brier décalée : 1,5 − (y − q)² | **accepte** | 0,700 / 0,900 | oui, niveau + 0,5 |
| Brier dilatée : 5 (1 − (y − q)²) | **accepte** | 0,700 / 0,900 | oui, échelle × 5 |
| Brier réduite : 1e-5 (1 − (y − q)²) | **rejette** (marges absolues) | 0,700 / 0,900 | oui |

**Effet sur les seuils.** Prenons une vérification juste à une confiance de 0,85 et une fausse à 0,70. Le score
interne moyen vaut 0,744 avec Brier, et 1,244 avec la même règle décalée de 0,5, que le filtre accepte. Le seuil de
fin de conception, 0,78, est alors franchi sans aucun changement de calibration.

**Ce que le filtre accepte et rejette, en résumé.**
- *Il rejette* : les règles constantes, linéaires, ou fortement sur-confiantes. La formule interne de la v5.3 est
  rejetée, alors que la v6 la garde comme repli.
- *Il accepte* : les règles propres usuelles, une sur-confiance légère (écart de l'optimum jusqu'à 0,05), et toute
  transformation affine croissante.

Par le chemin du gabarit, la règle est toujours propre : c'est une combinaison positive de Brier et du logarithme.
Mais `poids_brier`, choisi par le modèle, y change le niveau du score : 0,552 avec un poids de 0,55, contre 0,722 avec
0,95, sur le même exemple.

### 9.7. Ce qui ne sert à rien, et ce qui n'est pas annoncé

- **Trois fonctions sur quatre ne sont jamais appelées.** `principal.py` n'appelle que `recompense_interne` (l. 890)
  et le vérificateur (l. 1008). `code_objectif_sonde`, `ponderer_trace_memoire` et `seuils_routage` sont réécrites et
  testées, mais jamais utilisées :
  - la sonde garde `CODE_OBJECTIF_SONDE_BREGMAN_TSALLIS` (l. 512) ;
  - le routage garde ses seuils écrits en dur (l. 1540-1586).

  Dans le gabarit, `EXPOSANT_ALPHA` n'entre dans aucun calcul, et `SEUIL_CASTE1` ne sert qu'à `seuils_routage`. Seul
  `poids_brier` agit.
- **La récompense interne change même sans mutation** (non annoncé). `_calculer_score_bregman_tsallis` (l. 888-896)
  passe de « 1 − Brier + 0,1 × Tsallis » à `politique_endogene.recompense_interne`. Effet mesuré au § 5 : métrique et
  mémoire différentes à la génération 1.
- **Écarts au rapport de Gemini.**
  - Il annonce un filtre qui « bloque tout reward hacking (récompense constante ou sur-confiante) ». C'est faux pour une
    sur-confiance légère, ainsi que pour le niveau et l'échelle du score (§ 9.6).
  - La clé `autoriser_mutation_code` n'est pas annoncée.
  - Les plages données dans la consigne (`alpha` de 1,15 à 1,85, `poids_brier` de 0,60 à 0,95) ne sont pas celles des
    bornes du code (1,10 à 1,95 ; 0,55 à 0,95).
  - `CONCEPTION.md` n'est pas mis à jour pour la v6.

## 10. Recherche de motifs (résultat 8)

Motifs : `subprocess`, `socket`, `urllib`, `requests`, `os.environ`, `getenv`, `os.system`, `__import__`, `eval(`,
`exec(`, `compile(`, `open(`, cherchés dans tous les fichiers d'`organisme/`. Journal :
`verification-v1/motifs-v53-v6-v1.txt`.

| version | fichier, ligne | motif | rôle |
|---|---|---|---|
| v5.3 et v6 | `tests/test_corrections_v1.py` l. 28, 33 | `socket` | Message `ConnectionError("socket du noyau fermé")` d'un faux noyau, pour l'essai de C-07. Aucun socket n'est utilisé. Fichier inchangé depuis la base. |
| v5.3 et v6 | `metrique/attaques.json` l. 55 | `urllib`, `open(` | Texte d'une attaque de sabotage : une trace d'actions d'un sous-agent, faite de chaînes, jamais exécutée. Fichier identique à la base. |
| v6 | `politique_endogene.py` l. 60, 62 | `__import__`, `subprocess`, `socket` | Entrées de la liste noire `NOMS_INTERDITS`. |
| v6 | `politique_endogene.py` l. 123 | `__import__` | Clé des fonctions intégrées réduites de la validation, liée à `_import_math_seul`, qui ne rend que `math`. |
| v6 | `politique_endogene.py` l. 130 | `compile(` | Compile l'arbre du code candidat écrit par le modèle. |
| v6 | `politique_endogene.py` l. 132 | `exec(` | **Exécute le code candidat dans le processus de l'organisme**, sans borne de temps (§ 9.2, § 9.5). |

`requests`, `os.environ`, `getenv`, `os.system` et `eval(` n'apparaissent nulle part. `principal.py` ne contient aucun
de ces motifs dans aucune des deux versions. Il lit et écrit `politique_endogene.py` par `read_text` et `write_text`
(l. 1466 et 1473).

## 11. Réserves de cette vérification

1. **Conclusions statiques.** Le défaut d'import (§ 9.3) est établi par analyse syntaxique de fichiers produits par les
   essais, sans les importer, puisque la règle interdit toute autre exécution. Les effets sur le noyau sont lus dans
   `boucle.py` et `contrat.py`, non exécutés.
2. **Propreté.** Mon essai porte sur ma transcription du contrôle, pas sur l'exécution du code de Gemini. Les verdicts
   « accepte » et « rejette » en dépendent.
3. **Couverture.** L'outil d'invariance ne déclenche ni les sondes (aucun trait) ni la mutation (historique d'une seule
   entrée). Ces chemins ne sont éprouvés que par les essais unitaires de Gemini, qui ne contrôlent ni l'économie
   d'appels de la sonde ni l'importabilité du successeur.
4. **Sûreté du filtre.** Je n'ai pas cherché de contournement. Les manques de principe relevés au § 9.4 suffisent à ne
   pas considérer l'auto-réécriture comme sûre. Il faudrait au minimum :
   - une liste blanche au lieu d'une liste noire ;
   - une validation du fichier entier ;
   - une exécution dans un processus à part, borné en temps et en mémoire ;
   - un contrôle d'import du successeur, côté noyau.

   C'est à toi de décider.
5. **Rapport de Gemini.** Il contient des durées incohérentes avec ses propres sorties (§ 4) et affirme des propriétés
   du filtre que le code n'a pas (§ 9.7).

## 12. Contenu de ce dossier

- `LISEZMOI-v1.md` : ce rapport ; `EMPREINTES-v1.txt` : sha256 de tous les journaux, différences, relevés et outils
  (contrôle : `sha256sum -c EMPREINTES-v1.txt` depuis ce dossier).
- `verification-v1/` : inventaires, empreintes par fichier, différences unifiées, journaux de pytest, d'invariance et
  de verrous, relevés, comparaisons, analyses.
- `outils-v1/` : mes quatre outils d'analyse statique et ma transcription du contrôle de propreté. Ils prennent leurs
  entrées en arguments et se lancent avec `python -I`.
- `essais-v1/` : les copies d'essai, propriété de `nobody`, avec leurs sorties. Elles ne figurent pas dans les
  empreintes, sauf les relevés recopiés dans `verification-v1/`.
- `livrable-verification-v53-v6-pousses-v1.zip` : tout ce qui précède, sauf `essais-v1/`.
