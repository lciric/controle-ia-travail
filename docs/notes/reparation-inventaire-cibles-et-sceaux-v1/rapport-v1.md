# Réparation de l'inventaire des lecteurs de la référence cachée et de l'arbre des sceaux — rapport v1

- Auteur : Claude Opus 5.5, développeur neuf (pièce de classe B). Branche `reparation/inventaire-cibles-et-sceaux-main-v1`, tirée de `origin/main` à `f4db9f174`. Écrit le 2026-11-24 vers 18:40Z (`date -u`).
- Rien n'a été ouvert sous `coffre/`, `docs/verdicts/`, `diag/`, `donnees/`, `versement/`. Sous `runs/`, aucun contenu lu ni affiché : seulement l'historique git (commits, dates, auteurs, comptes de lignes) et des empreintes, tailles et un contrôle de préfixe calculés par programme (sortie booléenne).
- Aucun module de production modifié. Aucune dépense, aucune instance.

## Verdict

1. Les trois fonctions relevées par la garde de cloisonnement **ne lisent pas la référence cachée** : une homonymie (projections de l'adaptateur), une garde qui la nomme pour la refuser, une fabrique de tâches jouets qui en écrit des valeurs factices ; chacune a un texte scellé ou une décision nommée qui la fonde. Elles sont admises dans une **liste neuve v6** (`tests/liste_cibles_invisibles_v6.json`, essai `tests/test_cibles_invisibles_v6.py`), avec preuve par l'arbre syntaxique éprouvée sur des artefacts ; les listes v4 et v5, scellées, ne sont pas touchées.
2. Les deux essais en échec des v4 et v5 (`test_aucun_module_hors_mesures_ne_lit_la_cle_cibles`) **restent en échec** : ils lisent des listes scellées que R12 interdit de réécrire ; leur classement en échec connu est à trancher par la mère.
3. Arbre des sceaux : **18 problèmes sur `main`, 12 après réparation**. Six compagnons mal nommés corrigés (fichier inchangé depuis son scellement, vérifié par git). Un fichier modifié après scellement (`journal-etage3.txt`, une ligne ajoutée) et un fichier réécrit deux fois sous le même nom (`programme-questions-directeur-2026-11-24-v1.md`) sont décrits, non corrigés ; dix compagnons absents sont décrits, non créés.

## 1. Inventaire des lecteurs de la référence cachée

État sur `main` (`f4db9f174`) : `test_cibles_invisibles_v4.py` et `test_cibles_invisibles_v5.py`, chacun un échec, `test_aucun_module_hors_mesures_ne_lit_la_cle_cibles` (l'essai du v3 joué sous la liste complétée). Fonctions hors liste : `barreau8_moniteurs/passe_recalcul_v6.py::_table_en_specification`, `t08/fabrique_jouet_v1.py::taches_factices`, `t08/rendu_juges_v1.py::exiger_tache_projetee`. (La consigne annonçait trois échecs : il y en a deux, un par fichier d'essai, chacun nommant les trois fonctions.)

Pourquoi pas dans la liste v5 : elle est du 21 novembre (`4b507bb2a`) ; le code de T0.8 est entré sur `main` le 22 (`04b4edfad`), la passe de recalcul v6 le 24 (`3405f7afe`).

### 1.1 `passe_recalcul_v6.py::_table_en_specification` — homonyme, ne lit pas la référence

- (a) Lecture du code : la constante `"cibles"` n'apparaît qu'en clé du dictionnaire rendu, `"cibles": tuple(c["adaptateurs"]["projections"])`, où `c` est la table neuve des constantes reportées. `cibles` est le champ de forme de la spécification de la passe qui nomme les projections visées par l'adaptateur (`q_proj`, `k_proj`, `v_proj`, `o_proj`), passé ensuite à `injecter(..., cibles=spec.cibles)`. Aucune lecture d'une tâche ni de sa référence cachée dans cette fonction.
- (b) Fondement : additif 1 scellé, `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md` (`fc5b0610ed004ea4b1565e7a50567d7538b0f9e66b129c874c2f8c5bc2a4d8c2`, ligne SCELLEMENT-ADDITIF-1-SONDES-IIB de `registres/sondes-iib-v1.md`), table des constantes, ligne « `adaptateurs.projections` … report, RP-12 », et « Constantes de forme » ; additif 2 scellé (`8e930abadcdbb050e026771cb67f90bb47ebed63955b498364d0fa9c9f7eab5e`, M-4) ; code inscrit à la ligne CODE-PASSE-IIB (bordereau `registres/bordereau-code-passe-barreau8-v6.json`, `74736c499d9bd7568d0ebe93b0eccd73746fe0ab1697fa26f2371ef816d6e8db`, commit nommé `1f16e86e`, objet git égal ; R-5268). Précédent de décision : R-1941 (le lecteur de `cibles` de l'adaptateur des lanceurs de T0.6 admis parmi les lecteurs, « preuve, pas exemption », décision de routine de la mère) ; même homonymie admise aux listes v4 et v5 pour la formation et la relecture du barreau 5.
- Décision : **admise** (catégorie « homonyme de l'adaptateur »). Fichier à `f3228b4b25a5140b3b8fa8c7ac994a727d61f9d986b0539f8ea5956eb5fba30a`.

### 1.2 `t08/rendu_juges_v1.py::exiger_tache_projetee` — nomme la clé pour la refuser

- (a) Lecture du code : `if "cibles" in tache: raise GardeArret(...)` ; la fonction ne rend rien et ne lit aucune valeur de la tâche. Elle est appelée par `message_utilisateur` et `demandes_de_l_episode` avant tout rendu.
- (b) Fondement : texte scellé `prereg/T0.8-bases-boite-noire-v0-v3.md` (`72a2611b3eff8ef070ab6f12f1468213cb88a8f42729eb2e9edeea7fcb884918`, ligne SCELLEMENT-T08-V3 de `registres/scellements-v1.md`) : « Ce que voit chaque surveillant » (« Jamais donnés à un juge : les cibles semées de la tâche … N-060 v3 ») ; « Plan d'analyse », point 1 (« garde : un objet portant `cibles` passé au rendu est refusé ») et point 10 (« refus de `cibles` », éprouvé sur un cas sain et un artefact, R5). Code inscrit à la ligne CODE-T08-V3 (commit `6735dd2e`, pièce `docs/notes/t08-code-aligne-v1/empreintes-code-t08-6735dd2e-v1.md`, `7f8a7a92d0a45a892f157eb96613316a6eb04d73a3aa81ef7c83d05a7fc7519e`, qui porte ce fichier à l'empreinte actuelle ; objet git égal).
- Décision : **admise** (catégorie « nommée pour refuser »). Fichier à `aca5447b0096eea18092c1203131b2e285ffeb3ea09f5df880294e4b2c707a45`.

### 1.3 `t08/fabrique_jouet_v1.py::taches_factices` — écrit des cibles factices, ne lit rien

- (a) Lecture du code : la constante `"cibles"` est la clé d'un dictionnaire littéral de tâche jouet ; ses valeurs viennent du générateur de l'essai (`rng`) et d'une liste de mots fixes ; la fonction n'ouvre ni ne lit aucun fichier et écrit sous la racine d'essai donnée (`racine / "donnees" / "jouet-taches"`, racine neuve exigée par `essai_jouet_v1.fabriquer_entrees`). Appelée par l'essai jouet de T0.8 et des essais.
- (b) Fondement : même texte scellé de T0.8, « Plan d'analyse », point 10 (chaque garde éprouvée sur un cas sain et sur un artefact, « refus de `cibles` ») ; docstring du module (« tâches d'évaluation factices (64, avec `cibles` pour éprouver le refus du rendu des juges) ») ; même ligne CODE-T08-V3 et même pièce d'empreintes.
- Décision : **admise** (catégorie « fabrique jouet »). Fichier à `7ffe0c95743f247dc9185f2955561f20d7928df305fe3c4f537d10e7c167150c`.

Aucun des trois cas n'est une brèche de cloisonnement.

### 1.4 Ce qui a été fait, et pourquoi une v6

La liste admise vit dans `tests/liste_cibles_invisibles_v5.json`, scellée (compagnon ; la v5 vérifie aussi qu'elle ne diffère de la v4 que par sa correction). La réécrire violerait R12 et ferait échouer d'autres essais. Selon l'usage du dépôt (v3, puis v4 et v5 en erratum), j'ai ajouté une version neuve :

- `tests/liste_cibles_invisibles_v6.json` (`a7353b641567bca8ccd9b3ffb8bbc2f960ff67de072c41f35669e52f9bf82f56`, compagnon) : nomme la v5 à son empreinte (`37bcbb01…`), ajoute les trois fonctions, chacune avec catégorie, raison, source, textes à leur empreinte, commit et empreinte du fichier examiné. Statut écrit : « proposée, non adoptée ».
- `tests/test_cibles_invisibles_v6.py` (`59e4de05c3985701246470ebce5f30519b4b790921b2ed48293474a34ef97e4c`, compagnon), 13 essais : liste scellée ; v5 intacte ; ajouts neufs, sourcés, textes à leur empreinte ; fichiers examinés inchangés ; objets git égaux au commit nommé ; l'essai du v3 joué sous v5 plus v6 ; mutation (retirer une fonction la rend exactement hors liste) ; module planté qui lit `tache['cibles']` toujours vu (R5) ; une preuve par l'arbre syntaxique par catégorie, chacune admettant un cas sain et refusant de 4 à 5 artefacts (lecture `x["cibles"]`, `.get`, `if` sans `raise`, `not in`, lecture de fichier, valeur venue d'un argument) ; comportement de la garde du rendu (refus et cas sain).

Limite déclarée : la v6 rend la garde verte pour le code actuel, mais n'enlève pas les échecs des v4 et v5, qui lisent leurs listes scellées. La pièce est de classe B : contre-lecture par un autre modèle avant adoption.

## 2. Arbre des sceaux

`python -m controle_ia.scellement verifier-arbre .` sur `main` : **18 problèmes**. Les empreintes de lancement sont conformes (3 sur 3).

### 2.1 Compagnons mal nommés, corrigés (6)

Pour chacun : le compagnon porte un chemin au lieu du nom de base ; l'empreinte du compagnon égale celle du fichier ; fichier et compagnon créés dans le même commit, jamais modifiés depuis (une seule version git de chacun). Correction : compagnon réécrit à son chemin réglementaire (`FICHIER.sha256`), même empreinte, nom de base ; vérifié par programme avant écriture (empreinte actuelle = empreinte scellée).

| fichier | empreinte | commit unique (fichier et compagnon) |
|---|---|---|
| `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/contre-lecture-carbon-high-publication-v1.md` (nom inscrit : chemin absolu d'une machine Antigravity) | `ae7ab7d1…` | `fe9cf122`, 2026-11-24 05:01:50Z |
| `registres/passations/2026-11-23-2220-mere-antigravity-opus-reprise-et-mandats.md` | `535b3631…` | `0d4c1437`, 2026-11-23 22:20:47Z |
| `registres/passations/2026-11-23-2326-plan-entretien-f10.md` | `bf9fa72e…` | `b0449d85`, 2026-11-23 23:26:21Z |
| `registres/passations/2026-11-24-0920-mere-claude-code-016QhUrvi45g3jX5saFefVED.md` | `64e768e6…` | `9600f858`, 2026-11-24 09:20:26Z |
| `registres/passations/2026-11-24-1412-mere-016Qh-a-mere-01Qi7-questions-organisme.md` | `7037dfd3…` | `b8c73088`, 2026-11-24 14:12:23Z |
| `registres/passations/2026-11-24-1528-mere-016Qh-a-mere-01Qi7-partage-organisme.md` | `2d4e4dc7…` | `25a8fc21`, 2026-11-24 15:28:11Z |

(La consigne parlait de trois passations ; il y en a cinq, plus la contre-lecture de Carbon.)

### 2.2 Compagnon mal nommé, **non corrigé** : le fichier a changé depuis son premier scellement (1)

`docs/notes/idee-interessante-v1/programme-questions-directeur-2026-11-24-v1.md` : trois versions sous le même nom, chacune rescellée en réécrivant le compagnon (avec le chemin dans le nom) : `da447155` 15:31:13Z (`b7e39c88…`, 3 595 octets, R-5312) ; `e7ae9ad6` 16:04:14Z (`51f9326b…`, 4 237 octets, R-5323) ; `04ffcacf` 17:01:06Z (`d579b377…`, 4 695 octets, R-5332). Document tenu vivant sous un nom versionné : écart à R12. L'empreinte actuelle concorde avec le compagnon ; seul le nom inscrit est faux, mais la condition « inchangé depuis le scellement d'origine » ne tient pas : laissé à la mère.

### 2.3 Fichier modifié après scellement, **non corrigé** (1)

`runs/collisionneur-protocole-x-bancs-plantes-cinq-decisions-v1-20261122-131546/journal-etage3.txt` :
- scellé au commit `6350a767` (2026-11-24 09:18:33Z, « seconde tentative sur la clé de Luc, encore 401 … 0 USD », session `session_01Qi7Gr3Ggccg85kjmP654WC`) à `7125e2c3…`, 8 182 octets ;
- modifié au commit `74d789ce` (2026-11-24 09:27:54Z, « relance avec la clé du compte, cellule d'Opus 4.6 en cours (journal partiel) », session `session_01Qi7Gr4L1p9Jdu9GbxtU362`, Claude Opus 5.5) : 8 313 octets, `14d63074…`, **une ligne ajoutée en fin, aucune retirée** (131 octets ; l'ancienne version est un préfixe exact de l'actuelle, contrôle par programme) ; le compagnon n'a pas été mis à jour.
- Nature : journal d'une course de collisionneur en cours, scellé à une étape puis prolongé. Contenu non lu.

### 2.4 Compagnons absents, **non créés** (10 fichiers)

| fichier | historique | lecture |
|---|---|---|
| `docs/notes/attelage-plan-turing-v1/collisionneur-attelage-v1/consigne-test-neutralite-v1.txt` | une version, `efc7f0ac` 17:08:26Z (R-5336) | jamais scellé |
| `docs/notes/attelage-plan-turing-v1/collisionneur-attelage-v1/question-neutre-attelage-v1.md` | une version, même commit | jamais scellé |
| `docs/notes/rejeu-activations-saboteur-voie-a-v1/amorce-executante-v8/note-ordre-lancement-rejeu-voie-a-v2.md` | une version, `f99c1eed` 11:06:07Z | jamais scellé |
| `docs/notes/rejeu-activations-saboteur-voie-a-v1/amorce-executante-v8/ordre-lancement-rejeu-voie-a-v1.json` | trois versions (`3a835480`, `0580280d`, `8c6ac595`, 10:40 à 10:47Z) | brouillon jamais scellé ; l'ordre v2 voisin, lui, est scellé |
| `docs/notes/service-collisionneur-modes-v8-v1/calculs-v3/essais-artefacts-produire-version-servie-v1/d-sceau-faux.json` et `….sceau-faux-essai` | `dbafadaa`, `2d17946f` (23 nov.) | artefacts voulus d'un essai de faux sceau, exception déclarée (R-5161) |
| `runs/collisionneur-protocole-x-bancs-plantes-cinq-decisions-v1-20261122-131546/etat.md` | trois versions, 09:02 à 09:18Z | fichier d'état d'une course, jamais scellé |
| `runs/collisionneur-protocole-x-bancs-plantes-cinq-decisions-v1-20261122-131546/journal.jsonl` | trois versions, 09:02 à 09:18Z | journal d'une course, jamais scellé |
| `registres/passations/2026-11-24-1811-developpeur-cote-moniteurs-code-lecture-sondes-v6.md` | une version, `191f0721` 18:13:23Z (R-5350) | passation non scellée par son auteur |
| `registres/passations/index-passations-2026-11-23-v1.md` | 29 versions le 23 (06:30 à 08:12Z) | index tenu vivant, « scellé à sa passation » (R-5161), jamais scellé depuis |

Après réparation : **12 problèmes** = 10 compagnons absents + le compagnon mal nommé de 2.2 + l'empreinte différente de 2.3 (sur `main` : 18 = ces 12 + les 6 compagnons corrigés de 2.1).

## 3. Sorties des essais

Environnement : `.venv` de `requirements-cpu.txt`, `PYTHONPATH=src`, Python du conteneur, processeur.

```
# main, avant tout changement
$ pytest -q tests/test_cibles_invisibles_v4.py tests/test_cibles_invisibles_v5.py
FAILED tests/test_cibles_invisibles_v4.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles
FAILED tests/test_cibles_invisibles_v5.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles
2 failed, 84 passed, 4 xfailed in 41.98s

# après : v4, v5 et v6
$ pytest -q tests/test_cibles_invisibles_v4.py tests/test_cibles_invisibles_v5.py tests/test_cibles_invisibles_v6.py
FAILED tests/test_cibles_invisibles_v4.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles
FAILED tests/test_cibles_invisibles_v5.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles
2 failed, 97 passed, 4 xfailed in 53.44s
# (les 13 essais du v6 passent ; les 4 attendus en échec sont les inventaires figés des v4 et v5, R-5010)

$ pytest -q tests/test_cibles_invisibles_v6.py
13 passed in 17.83s

$ pytest -q tests/test_t08_cibles_invisibles_v1.py tests/test_scellement.py tests/test_comparer_echecs_attendus_v1.py \
    tests/test_cibles_invisibles_v1.py tests/test_cibles_invisibles_v2.py tests/test_cibles_invisibles_v3.py
88 passed, 6 xfailed in 50.62s

$ python -m controle_ia.scellement verifier-arbre .
main : 18 problème(s) ; après réparation : 12 problème(s) (liste en section 2)
```

Suite complète : **non lancée**. Elle compte environ 9 600 essais et dure plus d'une heure sur ce conteneur à quatre processeurs, sans `pytest-xdist` (R-3919, R-2776) : au-delà de la borne de 20 minutes de la consigne.

## 4. À trancher par la mère

1. Adoption de la liste v6 et de son essai, après contre-lecture par un autre modèle (pièce de classe B).
2. Les deux échecs `test_aucun_module_hors_mesures_ne_lit_la_cle_cibles` des v4 et v5 : les classer en échecs connus (liste d'échecs connus v5 et son greffon, comme R-5010 l'a fait pour les inventaires figés), ou les laisser visibles. Ils ne peuvent passer sans réécrire une liste scellée.
3. `programme-questions-directeur-2026-11-24-v1.md` réécrit deux fois sous le même nom (R12) : déclarer document vivant, ou le verser en versions nommées ; son compagnon reste mal nommé d'ici là.
4. `journal-etage3.txt` prolongé d'une ligne après scellement : déclarer les journaux de la course vivants jusqu'à sa fin, ou sceller une version neuve sous un nom neuf ; idem pour `etat.md` et `journal.jsonl` de la même course, jamais scellés.
5. Compagnons absents : passation `2026-11-24-1811` (à sceller par son auteur, CLAUDE.md, R14), index des passations du 23 (R-5161 promettait un scellement à la passation), deux pièces du collisionneur de l'attelage, la note v2 et le brouillon v1 de l'ordre du rejeu. Les artefacts `d-sceau-faux` sont déjà déclarés (R-5161).
