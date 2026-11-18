# Mesures définitives au commit de la course de l'étape B bis (apprentissage des sondes sur la tâche, T0.7) : plancher d'essais sous Python 3.13 et 3.11, code hors de la fiche, empreintes de la chaîne — v1

- **Auteur** : sous-agent lancé par la session mère. Je n'ai écrit ni l'amorce, ni le lanceur, ni leurs essais, ni aucun brouillon
  de l'addendum, ni aucune contre-lecture, ni l'arbitrage, ni la répétition de la mesure du plancher.
- **Date (UTC, `date -u`)** : 2026-11-18, de 05:47Z à 05:56Z environ.
- **Gestes faits** : B.2 (plancher au commit exact, deux fois), B.4 (code hors de la fiche) et la partie hors loueur de B.3
  (empreintes de la chaîne, ligne d'inscription, compagnon de l'addendum), tels que les écrit l'arbitrage des quatre
  contre-lectures (`arbitrage-contre-lecture-amorce-v6-v1.md`, `688abea5965a872b646148538f979be9dfd90d687c8eb73185eb092bcac150e3`,
  section B). Non fait ici, parce qu'il demande la commande imprimée au feu : le décodage du base64 de la commande de création
  (troisième tiret de B.3).
- **Commit de la course, fixé une fois par la mère** : `438a9c5257bdc4fa65f25c42cc89753a049b4586` (« Étape B bis : troisième
  addendum d'écart accordé, scellé et inscrit (R-3191) »). Il porte le troisième addendum scellé
  (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md`, `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872`) et
  sa ligne `ADDENDUM-ECART-3-BBIS`. Toutes les mesures portent ce commit, et lui seul.
- **Pièces lues avant d'agir** : R-3188 et R-3191 (`registres/decisions.md`) ; l'arbitrage (section B et « Ce qui doit aller au
  feu version 4 ») ; le troisième addendum scellé (compagnon conforme) ; le projet de feu version 3 et sa contre-lecture
  (compagnons conformes) ; la répétition de la mesure du plancher (`repetition-mesure-plancher-py311-py313-v1.md`, compagnon
  conforme) ; la sous-commande `essais-du-commit` du lanceur au commit.
- **Cloisonnement tenu** : rien d'ouvert sous `diag/`, `runs/` ni `donnees/` ; aucune branche de données ni de calcul ; aucun
  résultat de 7a, de 7b, de T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis. Les seules sorties lues
  sont celles des essais de la chaîne, qui ne portent que sur des données fabriquées. Aucune dépense, aucun appel au loueur ni à
  l'hébergeur, aucune clé lue ni affichée, aucun commit, aucune poussée.

## Verdict : tout conforme

Chaque exigence de la consigne est tenue au commit `438a9c5257bdc4fa65f25c42cc89753a049b4586`, sans aucun écart :

| exigence | Python 3.13 | Python 3.11 |
|---|---|---|
| code de retour du lanceur | **0** | **0** |
| ligne de compte | « 151 passed, 25 skipped, 4 warnings » | « 151 passed, 25 skipped » |
| exactement 151 passés et 25 sautés | oui | oui |
| fichiers sur l'arbre extrait | **516** | **516** |
| empreinte de la liste des fichiers | `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0` | `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0` |
| sortie d'erreur des essais | vide | vide |

| geste | résultat |
|---|---|
| B.4, `git diff --quiet 05cd22aa 438a9c52… -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'` | code **0** ; liste des fichiers différents vide |
| B.4, fichiers réutilisés de la l. 19 du texte scellé | **11 sur 11 conformes** au commit de la course (et égaux au commit de la fiche `05cd22aa`) |
| B.4, `git ls-tree --name-only` de la racine | mêmes **35 entrées** aux deux commits ; `diff` vide, code 0 |
| B.3, amorce v6 au commit | `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5`, égale en entier au § 6 de l'addendum |
| B.3, lanceur v6 au commit | `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7`, égal en entier au § 6 de l'addendum |
| B.3, ligne `ADDENDUM-ECART-3-BBIS` au registre voisin | présente **une fois** (l. 9 de `registres/t07-etape-b-bis-v1-addenda-v1.md` au commit), chemin et empreinte `e5604cbd…` entiers |
| B.3, addendum conforme à son compagnon | `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872` des deux côtés |

Une remarque hors des critères écrits, qui n'est pas un écart, est au § 4.

## 1. Plancher d'essais au commit exact (geste B.2)

Les deux commandes ont été jouées depuis `/home/user/controle-ia-travail`, avec `PYTHON_BBIS` donné par chemin absolu (condition
de la répétition, § 3 de celle-ci) et un dossier de mesure neuf chaque fois (aucun nom réutilisé) :

| mesure | commande | début → fin (UTC) | code | ligne de compte |
|---|---|---|---|---|
| Python 3.13.18 | `PYTHON_BBIS=/home/user/controle-ia-travail/.venv/bin/python bash scripts/lancer_bbis_v6.sh essais-du-commit /home/user/controle-ia-travail 438a9c5257bdc4fa65f25c42cc89753a049b4586 /tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/mesure-definitive-py313-v1` | 05:47:46 → 05:50:13 | **0** | « 151 passed, 25 skipped, 4 warnings in 144.78s » |
| Python 3.11.18 | `PYTHON_BBIS=/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/venv-py311-bbis/bin/python bash scripts/lancer_bbis_v6.sh essais-du-commit /home/user/controle-ia-travail 438a9c5257bdc4fa65f25c42cc89753a049b4586 /tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/mesure-definitive-py311-v1` | 05:50:29 → 05:52:54 | **0** | « 151 passed, 25 skipped in 143.24s » |

Les deux fois, le lanceur écrit « 151 passés ≥ 151 : le plancher de l'amorce serait franchi ». Plancher lu dans l'amorce : 151.

**Comparaisons** :

- Les 25 lignes `SKIPPED` sont identiques entre 3.13 et 3.11, et identiques à celles de la répétition sous 3.11
  (`repetition-mesure-plancher-v1/essais-py311-v1.txt`). Les lignes de progression de pytest sont identiques entre les deux
  interpréteurs.
- Les 4 avertissements sous 3.13 sont ceux que la répétition décrit (essai de l'épreuve de niveau, `fork()` dans un processus à
  plusieurs fils, avertissement qui n'existe qu'à partir de Python 3.12) ; aucun sous 3.11.
- Paquets : `torch==2.14.1`, `numpy==2.4.6`, `scipy==1.17.1`, `pytest==9.1.1`, `transformers==5.18.0` des deux côtés
  (`environnements-paquets-py313-py311-v1.txt`). L'environnement 3.11 est celui de la répétition, gardé tel quel.

**Chaîne jouée depuis le disque** : la sous-commande lit l'amorce sur le disque (`$ICI/amorce_bbis_v6.sh`), et l'arbre extrait
est reconstruit au commit à partir des objets du dépôt. La branche `main` a avancé pendant la mesure : tête `ccac0bd9…` au départ
de la mesure 3.13, `07cd2286…` au départ de la mesure 3.11, `450a6651…` à la fin, `478111c2…` à 05:55Z, tous postérieurs au
commit de la course. Les empreintes de l'amorce et du lanceur sur le disque ont été relevées avant chaque mesure et après la
seconde : toujours `26f954e9…dbbb5` et `3224ce14…344b7`, sur 64 caractères ; et `git diff --quiet 438a9c52… HEAD --
scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh` rend le code 0. Les scripts joués sont donc à l'octet ceux du commit de la
course.

## 2. Code hors de la fiche (geste B.4)

- `git diff --quiet 05cd22aa 438a9c5257bdc4fa65f25c42cc89753a049b4586 -- src requirements-gpu.txt pyproject.toml tests/conftest.py
  'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'` : **code 0** (attendu 0). Contrôle complémentaire par `--name-only` : aucun
  fichier.
- Texte scellé au commit : `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb`, égal à son compagnon. Sa l. 19
  porte onze empreintes de 64 caractères ; les onze fichiers (`src/controle_ia/sondes/familles.py`, `evaluation.py`,
  `temoins.py` ; `src/controle_ia/t07/repli_recalcul_v1.py`, `repli_v1.py`, `plancher_v2.py`, `plancher_v3.py`,
  `lecture_v4.py`, `criteres_v1.py` ; `src/controle_ia/t06/test_croise.py` ; `src/controle_ia/organismes/lora.py`) ont, au commit
  de la course, exactement l'empreinte de la l. 19 : **11 sur 11**. Le programme vérifie aussi que sa liste reprend toutes les
  empreintes de la l. 19 et elles seules.
- `git ls-tree --name-only` de la racine : 35 entrées à `05cd22aa`, 35 entrées au commit de la course, `diff` vide (code 0).

## 3. Empreintes de la chaîne et inscription de l'addendum (geste B.3, partie hors loueur)

- `git show 438a9c52…:scripts/amorce_bbis_v6.sh | sha256sum` → `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` ;
  § 6 de l'addendum (lu au même commit, une seule ligne) : la même, sur 64 caractères ; compagnon `.sha256` au commit : la même.
- `git show 438a9c52…:scripts/lancer_bbis_v6.sh | sha256sum` → `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7` ;
  § 6 : la même ; compagnon : la même.
- En plus, les essais de la chaîne, `tests/test_chaine_bbis_v6_v1.py` :
  `f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca`, égale au § 6 et au compagnon.
- Registre voisin au commit : la clé `ADDENDUM-ECART-3-BBIS` y figure **une fois** (une ligne), l. 9, datée 2026-11-18T05:46:36Z,
  avec le chemin `prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md` et l'empreinte entière `e5604cbd…07872`.
- Addendum au commit : `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872`, égal à son compagnon au commit (et au
  fichier sur le disque, `sha256sum -c` conforme).

## 4. Remarque hors des critères écrits (pas un écart)

Au-delà des noms, j'ai comparé le contenu des fichiers de la racine, que l'amorce extrait par le motif `/*`. Un seul diffère
entre `05cd22aa` et le commit de la course : `CLAUDE.md` (3 lignes : liste des décisions, échéance de la porte décalée à
décembre, règle de nommage étendue). Aucun fichier de `src/controle_ia/t07bbis/`, aucun essai `tests/test_t07bbis_*` et
l'amorce ne le lisent ; seuls deux modules hors de la course le citent (`harnais/validation_reelle.py`, pour l'exclure ;
`runs_nuit/rejeu_activations_v1.py`, en commentaire). Le critère écrit de B.4 ne compare que les noms, qui sont égaux : je le
consigne pour que le feu le sache, sans le compter comme écart.

## 5. Sorties brutes versées

Dossier `docs/notes/prealables-course-etape-b-bis-v1/mesures-definitives-commit-course-v1/`, un fichier par commande, chacun scellé
par son compagnon `.sha256` :

| fichier | empreinte |
|---|---|
| `commande-1-essais-du-commit-py313-sortie-lanceur.txt` (commande, heures, sortie, code) | `35805d014b504c3e6c88d39eb41e20b6897d6e5f1eedde4b1c897ed65449f3e7` |
| `commande-1-essais-du-commit-py313-essais.txt` | `f6b483ef0e18f050d73aaaea99b2a9247ab4302a5eadcfcffcbd9c434ced35bc` |
| `commande-1-essais-du-commit-py313-essais-err.txt` (vide) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `commande-1-essais-du-commit-py313-fichiers-de-l-arbre.txt` | `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0` |
| `commande-2-essais-du-commit-py311-sortie-lanceur.txt` | `acc5c4abe1b2de06c4bd79801d2dbe51339146e455d61e4fc3c726024dd0964c` |
| `commande-2-essais-du-commit-py311-essais.txt` | `762e561a244ad6a295c6461af94e9417c94ac1e833ddeb982ac1539beffa1f49` |
| `commande-2-essais-du-commit-py311-essais-err.txt` (vide) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `commande-2-essais-du-commit-py311-fichiers-de-l-arbre.txt` | `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0` |
| `commande-3-geste-b4-git-diff-quiet-code-hors-fiche.txt` | `bce8326b86e8bfede07dc8bec63902be7f7c8917b42116fdb16cd2e3a7fad697` |
| `commande-4-geste-b4-empreintes-l19-texte-scelle.txt` | `f2b4d3c9ef8e60f026a239c63a33bbacf19fb2d739fe7fb0bdc7eb3e42a8e130` |
| `commande-5-geste-b4-ls-tree-racine-05cd22aa-et-commit-course.txt` | `b37b2d0f6abf57a9698adaf426a8b41064fe7ee40a25069c603c629469e83199` |
| `commande-6-geste-b3-empreintes-chaine-v6-au-commit.txt` | `25bbbbd40e0b1a9b9d10a784b1e3d07976df41e2be5fa4fa66f993ca74c33de5` |
| `commande-7-geste-b3-ligne-addendum-ecart-3-registre-voisin.txt` | `7e352de624efdc55a085df2077468c6e3d0163e8d7cc9bc2c18f2eb48d84c6c3` |
| `commande-8-geste-b3-addendum-conforme-a-son-compagnon.txt` | `6ccd117866c4780da038581783bac8c7d7d5e290dd9426c802cda3b556263059` |
| `environnements-paquets-py313-py311-v1.txt` | `7d535c8c76682b295cdb62bdfe80b79114cbf09aa3d473fb1372bb7f20931a52` |
| `programme-gestes-b3-b4-v1.sh` (programme qui a produit les commandes 3 à 8, lecture seule du dépôt) | `7a859ea14d8768004a332149789c26cfba6341788d754ccc4422fdcaf150a5a8` |

Les dossiers de mesure du bloc-notes (arbres jetables `depot/` et dossiers temporaires des essais) sont effacés en rendant ;
l'environnement 3.11 est gardé.

## 6. Réserves

1. **Marge nulle, inchangée** : 151 passés pour un plancher de 151.
2. **Ce que ces mesures ne couvrent pas sur la machine** (repris de la répétition et de l'addendum, § 4) : Python 3.11 de l'image
   peut différer de 3.11.18 ; les dépendances transitives de `requirements-gpu.txt` seront résolues de nouveau ; rien n'a tourné
   sur une carte ; la sortie de 7b n'est pas apportée dans l'arbre reconstruit.
3. **Reste au feu, hors de cette tâche** : le décodage du base64 de la commande imprimée et sa comparaison à `26f954e9…dbbb5`
   (troisième tiret de B.3), et la reprise des mêmes comparaisons d'empreintes dans le shell de lancement juste avant la création.
