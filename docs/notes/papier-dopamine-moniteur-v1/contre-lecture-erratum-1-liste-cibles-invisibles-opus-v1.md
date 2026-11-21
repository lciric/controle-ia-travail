# Contre-lecture de l'erratum 1 de la liste figée des cibles invisibles — v1 (2026-11-21T18:51:51Z, `date -u`)

Classe B (instrument). Contre-lecteur neuf : Claude Opus 5.5, qui n'a écrit aucune des pièces. Accord visé : GO-2026-11-21-69. Rien committé, rien poussé.

## Verdict : à corriger

Le fond tient : la garde lit de nouveau, les 43 lignes et les deux faux lecteurs sont justes et chacun vient d'un fichier versé et sans changement local. Aucun fichier illégitime n'est blanchi. L'essai neuf passe (41 sur 41) et attrape toutes les mutations que j'ai jouées. L'essai v3 n'a pas bougé. Il reste trois petites corrections, à faire par erratum, avant le versement. La première touche à une provenance donnée pour vérifiée alors qu'elle est fausse.

## Pièces lues (empreintes recalculées, toutes égales à leurs compagnons)

| pièce | empreinte |
|---|---|
| `tests/liste_cibles_invisibles_v4.json` | `e6724709bb11c58cc56e4058bd8111846b2c433921613a2cc2c0f2f123f4a5f8` |
| `tests/test_cibles_invisibles_v4.py` | `b93959b67fc77d1d6d1fc8815c0d8c2274f73c368e2ba063aada6ebab6997351` |
| `docs/notes/papier-dopamine-moniteur-v1/erratum-1-liste-cibles-invisibles-v3.md` | `694c1337ddda058261edb051dbc27074c69597022502c6aa5349a272621479b4` |
| `tests/test_cibles_invisibles_v3.py` (inchangé) | `93a6df4343f876cad58c01933d2636e65858bc8d55a99285edd4125cb5d504a9` |

Arbre de lecture : tête `2b04bc736d3e` de `main`. Aucun fichier de `src/` n'a changé entre `e6fbe03a` (arbre examiné par l'erratum) et cette tête (`git diff --stat` vide).

## Corrections demandées

**C-1 (provenance fausse, bloquante pour le versement).** Pour `controle_ia/dopamine_exploratoire/modele_v1.py`, le champ `commit` de la liste vaut `b1b29073ecebdf974a327a150193ffaa5ea74c22`, et la ligne 17 de la note porte « commit b1b29073 ». Or `git rev-parse b1b29073:src/…/modele_v1.py` donne `bd248bb4…`, et l'objet git de l'arbre de travail est `c0d0f58e…`. La vérification que la note donne pour commune (« objet git … égal à celui du commit nommé ») est **fausse** pour ce fichier. Le fichier a été modifié après `b1b29073`, par `0c907a7d` (13:19Z). Les commits `d6cde6667b789d165c672991608388a36e4a098f` (tête nommée par R-4571), `a52731b9` (fusion) et `e6fbe03a` portent bien l'objet `c0d0f58e…`. L'empreinte de 64 signes du fichier est juste, et le fichier est légitime. Correction : écrire `d6cde6667b789d165c672991608388a36e4a098f` dans le champ `commit` de la liste et dans la ligne 17, puis resceller la liste. Les 15 autres fichiers sont justes : objet git égal à celui du commit nommé, empreinte égale, fichier suivi et propre.

**C-2 (réserve 6 inexacte).** La note dit que la liste et la note ne sont pas exclues de git. Elles le sont : `.git/info/exclude`, ligne 90 pour la note et ligne 92 pour la liste, plus la ligne 87 pour l'essai. Les trois motifs se terminent par `*`, ce qui couvre aussi les compagnons. Les trois pièces et leurs compagnons ne sont pas suivis. Correction : rectifier la réserve et verser explicitement les six fichiers (ajout forcé), faute de quoi le versement les laisse de côté sans rien dire.

**C-3 (détail).** La docstring de l'essai v4 (ligne 4) parle de « quarante constructeurs d'invite ». La liste et la note en comptent 43. Correction par erratum, ou dans la version suivante de l'essai.

## Ce qui a été vérifié

1. **Chaque ligne ajoutée contre sa source.** Les 43 entrées ont été comptées par catégorie : 28 lignes de données, 7 environnements sur `tache_de` (dont 2 couvertes par un collecteur), 4 rendus d'environnements reçus, 3 textes fixes et 1 gabarit, soit 43. Elles concordent ligne à ligne avec la note. J'ai relu le code de toutes les lignes qui ne sont pas des lignes de données :
   - `tirer_famille` : l'environnement du saboteur est bien bâti par `environnement("saboteur", tache_de(t), …)`.
   - `membres_de_famille`, `evaluer_membre`, les deux appels de `relecture_v1._executer`, `rebatir_episodes`, `debut_d_episode` et `etat_impose_v1.rejouer_episode` : la tâche passe chaque fois par `tache_de` sur une simple recherche par identifiant.
   - Les quatre rendus ne lisent que des environnements reçus en paramètre.
   - `charger` et `formation_v1._executer` ouvrent la conversation de contrôle sur `("agent", None)`.
   - `DecoupeurHF.gabarit` rend deux textes reçus.
   - Les deux faux lecteurs se ramènent à `a = config["adaptateur"]` puis `tuple(a["cibles"])`.

   Les lignes de registre citées existent et disent ce que la note leur fait dire : R-2336, R-2338, R-4147, R-3618, R-4571, R-2751, R-2780, R-4596 et R-4650 au registre des décisions, CODE-FORMATION-B5F et CODE-LECTURE-B5F au registre propre du barreau 5. Les 76 lignes et les 12 lecteurs repris du v3 sont égaux au v3 ; l'essai le vérifie et je l'ai relancé.
2. **Aucun fichier illégitime blanchi.** Les 16 fichiers sont suivis par git, sans modification locale, et chacun a une ligne de registre. Il n'y a aucun fichier non suivi sous `src/`. Le seul écart trouvé est C-1, qui ne touche pas à la légitimité du fichier.
3. **Essai neuf relancé.** Commande : `PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_cibles_invisibles_v4.py --basetemp=<bloc-notes>`. Résultat : 41 passés. L'essai v3, relancé de la même façon, donne 2 échecs (les deux inventaires) et 19 passés, comme la note l'annonce.
4. **Mutations jouées sur des copies dans le bloc-notes.** La liste mutée est rescellée à chaque fois, pour que l'échec ne vienne pas du sceau. Les deux cas sains passent : la liste réécrite sans changement (41 passés) et une copie entière du code (41 passés).

   | mutation | échecs | essai qui la prend (hors empreinte) |
   |---|---|---|
   | ligne `evaluer_membre` retirée | 2 | inventaire des constructeurs |
   | faux lecteur de la relecture retiré | 3 | lecteurs de la clé `cibles` |
   | catégorie de `rejouer_episode` changée | 2 | preuve « environnement sur tache_de » |
   | ligne fantôme ajoutée | 5 | registre à jour |
   | une ligne reprise du v3 réécrite | 1 | « reprend le v3 sans rien changer » |
   | empreinte d'un fichier source changée | 1 | fichiers examinés inchangés |
   | source d'une ligne inventée | 1 | ajouts sourcés |
   | code : cibles ajoutées à la première observation de la passe de recalcul | 4 | collecteur à marqueur de la passe |
   | code : tâche entière passée à l'environnement dans `evaluer_membre` | 2 | preuve par l'arbre syntaxique |
   | code : cibles glissées dans la tâche du saboteur instruit | 5 | collecteur à marqueur du tirage |
   | code : cibles glissées dans l'argument de `tache_de` d'une fonction exemptée | 4 | lecteurs de la clé `cibles` (pas la preuve par `tache_de`) |

   Pour les copies du code, `docs/` a dû être relié par un lien symbolique : sans lui, les collecteurs échouent faute de l'index des invites. C'est un faux échec, que j'ai écarté avant de lire les mutations.
5. **Ancien essai intact.** Son empreinte est égale à son compagnon et à celle que la note annonce, et `git diff HEAD` sur le fichier est vide.

## Remarques, sans correction exigée

- La preuve « environnement sur tache_de » admet n'importe quel argument écrit `tache_de(...)`. Une tâche enrichie de ses cibles avant `tache_de` lui échappe. Dans ma mutation, c'est l'inventaire des lecteurs de la clé `cibles` qui l'a prise, parce que la clé y était écrite en toutes lettres. Une clé bâtie dynamiquement échapperait aux deux. Cette limite vient du v3 et la réserve 4 de la note l'approche. Dans le code actuel, j'ai vérifié à la lecture que les arguments sont de simples recherches.
- L'essai vérifie la forme du champ `commit` (40 signes hexadécimaux), pas l'égalité des objets git. Un essai de cette égalité, sauté quand le commit manque d'un historique tronqué, aurait pris C-1.
- La note dit que `cc9ab8eb` n'est pas un ancêtre de la tête. C'est exact, mais le dépôt est à historique tronqué. R-4596 parle d'un versement « sur main, commit cc9ab8eb », alors que le commit ancêtre qui porte les lanceurs est `25236c16` (message « versement de la liste v3 sur main … R-4596 »), et les objets y sont égaux. Rien à corriger dans la liste ; c'est le registre qui est ambigu.

## Écarts à la consigne

Aucune commande de liste hors du bloc-notes. Commandes git sur des chemins nommés seulement (`rev-parse`, `hash-object`, `ls-files --error-unmatch`, `check-ignore`, `status` et `diff` par chemin). Le fichier `epreuve_verite_plantee_v1.py` est du code : je n'en ai lu que l'empreinte et la provenance, aucune vérité ni aucun rendu. Je n'ai ouvert aucun fichier interdit et lu aucun résultat.
