# Répétition de la mesure du plancher d'essais de la course de l'étape B bis (apprentissage des sondes sur la tâche, T0.7), sous Python 3.11 et sous Python 3.13 — v1

- **Auteur** : sous-agent lancé par la session mère. Je n'ai écrit ni l'amorce, ni le lanceur, ni leurs essais, ni l'addendum,
  ni aucune des contre-lectures et de l'arbitrage lus.
- **Date (UTC, `date -u`)** : 2026-11-18, de 05:12Z à 05:30Z environ.
- **Nature** : **répétition**, à la tête du moment. Ce n'est pas la mesure définitive, que l'arbitrage exige au commit exact de la
  course, quand l'addendum scellé et inscrit y sera (arbitrage, correction B.2).
- **Pièces lues en entier avant d'agir** : R-3160, R-3170 (point 8), R-3185 et R-3188 (`registres/decisions.md`) ; l'arbitrage
  `arbitrage-contre-lecture-amorce-v6-v1.md` (`688abea5965a872b646148538f979be9dfd90d687c8eb73185eb092bcac150e3`, conforme à son
  compagnon) ; les quatre contre-lectures qu'il arbitre (gardes, conformité, machine, adverse ; compagnons conformes) ; la
  sous-commande `essais-du-commit` du lanceur (`scripts/lancer_bbis_v6.sh`, l. 62-85 et 170-186).
- **Ce que fait la sous-commande** (lu avant de la jouer) : elle reconstruit, dans le dossier donné, l'arbre que l'amorce
  extrairait au commit. C'est un dépôt jetable adossé aux objets du dépôt local, sans réseau et sans rien écrire dans le dépôt.
  Elle joue ensuite, depuis cet arbre, la ligne d'essais de l'amorce (`pytest … tests/test_t07bbis_*.py`) avec l'interpréteur
  `PYTHON_BBIS`, et compare le compte au plancher `MIN_ESSAIS` de l'amorce. Elle n'appelle ni le loueur, ni le dépôt distant, ni
  aucune clé.
- **Cloisonnement tenu** :
  - rien d'ouvert sous `diag/`, `runs/` ni `donnees/` ; aucune branche de données ni de calcul ;
  - aucun résultat de 7a, de 7b, de T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis ;
  - les seules sorties lues sont celles des essais de la chaîne, qui ne portent que sur des données fabriquées.
- **Sans** dépense, appel au loueur ou à l'hébergeur, clé lue, commit ni poussée. Le seul réseau employé est celui des paquets
  (PyPI).

## Verdict : prêt pour la mesure définitive, à une condition

Au même commit, les deux interpréteurs donnent :

- le code 0 ;
- **exactement 151 passés et 25 sautés**, sans aucun échec ;
- les mêmes 516 fichiers sur l'arbre, dont la liste a l'empreinte
  `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0`. C'est la même empreinte que la preuve du développeur
  (`brouillons/T0.7-etape-B-bis-v1/preuve-amorce-v6-v1/fichiers-de-l-arbre-extrait-candidat.txt`, compagnon conforme).

Les mêmes 25 essais sautent, pour les mêmes motifs, dans le même ordre. L'environnement 3.11 est prêt et peut servir tel quel à
la mesure définitive.

**La condition** : à la mesure définitive et au feu version 4, `PYTHON_BBIS` doit être un **chemin absolu**. Avec le chemin
relatif `.venv/bin/python`, celui qu'écrit l'arbitrage (« Ce qui doit aller au feu version 4 », point 1), `essais-du-commit`
rend un faux refus. Le nom du dossier de mesure est alors consommé (règle R12). Le détail est au § 3.

## 1. Commit mesuré et chaîne

- **Commit** : `244c4f7a72b732a09052e932655809b583586c2f`, tête de `main` à 05:13Z (commité le 2026-11-18T05:12:58Z,
  « registres : essai E5 clos (0,26 USD), suite arrêtée par défaut ; pièces de N-071 versées (R-3189) »). Il ne porte pas
  encore l'addendum scellé : ce **n'est pas** le commit de la course.
- **Même commit pour les deux mesures** : il a été fixé une fois, avant la première (`git rev-parse HEAD` relevé à 05:13Z). La
  tête a bougé ensuite, mais les deux mesures portent ce commit.
- **Chaîne à ce commit et sur le disque** : amorce version 6
  `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5`, lanceur version 6
  `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7`. Ce sont les empreintes arbitrées, sur 64 caractères.
- **Contrôle complémentaire** (geste B.4 de l'arbitrage, répété ici) : la commande
  `git diff --quiet 05cd22aa 244c4f7a -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'`
  rend le code 0. Le code hors de la fiche n'a pas bougé depuis le commit de la fiche.

## 2. Environnement Python 3.11

- **Création** : `/usr/bin/python3.11 -m venv /tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/venv-py311-bbis`
  (Python 3.11.18, pip 24.0).
- **Installation**, depuis la racine du dépôt :
  `…/venv-py311-bbis/bin/python -m pip install --no-cache-dir --report <rapport> -r requirements-cpu.txt -r requirements-donnees.txt`.
  Code 0, en 1 min 9 s.
- **torch** : `requirements-cpu.txt` ne prévoit pas de roue réservée au processeur. Son commentaire dit que l'index de PyTorch
  réservé au processeur est inaccessible, et il fige `torch==2.14.1` depuis PyPI. J'ai donc installé ce que le fichier prévoit :
  la roue PyPI `torch-2.14.1-cp311-cp311-manylinux_2_28_x86_64.whl`
  (`305a61f61f35f128579f299c5bd33d475f6a01c6307336139632e30856c4854d`). Elle embarque les bibliothèques des cartes (`2.14.1+cu130`).
  C'est la même construction que dans `.venv` et que celle que `requirements-gpu.txt` installe sur la machine. L'environnement
  occupe 5,8 Go.
- **Manifeste** : versions et empreintes des 71 roues installées, données par l'index et consignées par `pip --report`.
  - Dans le bloc-notes : `…/scratchpad/venv-py311-bbis-manifeste.txt`.
  - Copie versée : `repetition-mesure-plancher-v1/manifeste-environnement-py311-v1.txt`
    (`69e52dcd6af360cf799eabac5450e2e853a4221d094b9f4f551c42fe14914c07`).
  - Rapport brut de pip : `…/scratchpad/venv-py311-bbis-travail/rapport-pip.json`
    (`433e5d38e3340208f3ee44f5f337b57c976b522d3915e612cab4c061c030ca2f`).
- **Versions des paquets qui comptent, égales des deux côtés** :

  | paquet | version |
  |---|---|
  | torch | 2.14.1+cu130 (CUDA 13.0) |
  | numpy | 2.4.6 |
  | scipy | 1.17.1 |
  | pytest | 9.1.1 |
  | transformers | 5.18.0 |
  | tokenizers | 0.23.2 |
  | safetensors | 0.8.0 |
  | huggingface_hub | 1.33.0 |
  | matplotlib | 3.11.2 |

## 3. Commandes exactes et comptes

Toutes les commandes ont été jouées depuis `/home/user/controle-ia-travail`, avec `C=244c4f7a72b732a09052e932655809b583586c2f`
et `S=/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad`.

| mesure | commande | début et fin (UTC) | code | ligne de compte | fichiers | empreinte de la liste |
|---|---|---|---|---|---|---|
| Python 3.11 | `PYTHON_BBIS=$S/venv-py311-bbis/bin/python bash scripts/lancer_bbis_v6.sh essais-du-commit /home/user/controle-ia-travail $C $S/mesure-py311-repetition-v1` | 05:14:39 → 05:21:21 | **0** | « 151 passed, 25 skipped in 399.98s » | 516 | `d48e74d3…49edc0` |
| Python 3.13, chemin relatif (consigne) | `PYTHON_BBIS=.venv/bin/python bash scripts/lancer_bbis_v6.sh essais-du-commit /home/user/controle-ia-travail $C $S/mesure-py313-repetition-v1` | 05:21:31 → 05:21:31 | **2** (pytest : 127) | vide | 516 | `d48e74d3…49edc0` |
| Python 3.13, chemin absolu | `PYTHON_BBIS=/home/user/controle-ia-travail/.venv/bin/python bash scripts/lancer_bbis_v6.sh essais-du-commit /home/user/controle-ia-travail $C $S/mesure-py313-repetition-v2` | 05:21:44 → 05:23:54 | **0** | « 151 passed, 25 skipped, 4 warnings in 128.06s » | 516 | `d48e74d3…49edc0` |

**Pourquoi le chemin relatif échoue** :

- Le lanceur entre dans l'arbre reconstruit avant d'appeler l'interpréteur (`scripts/lancer_bbis_v6.sh`, l. 180 :
  `( cd "$DOS/depot" && … "$PY" -m pytest … )`).
- Un `PYTHON_BBIS` relatif y est donc introuvable. La sortie d'erreur dit : « scripts/lancer_bbis_v6.sh: line 180:
  .venv/bin/python: No such file or directory ».
- Le refus est du côté sûr : « essais en échec », rien ne passe. Mais c'est un faux refus, et il consomme le nom du dossier.
- La sous-commande `commande` n'entre dans aucun dossier avant d'appeler `"$PY"` (l. 92, 126, 146). Elle supporte donc le
  chemin relatif depuis la racine. Pour éviter le piège, il vaut mieux poser un chemin absolu partout.

**Ce qu'il faudrait** (aucun code de la course n'est à changer) :

- écrire au feu version 4 et à la consigne de la mesure définitive `PYTHON_BBIS=/home/user/controle-ia-travail/.venv/bin/python`
  pour Python 3.13 ;
- écrire `PYTHON_BBIS=/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/venv-py311-bbis/bin/python`
  pour Python 3.11 ;
- prévoir un nom de dossier neuf par essai (règle R12).

Je n'ai pas cherché pourquoi la contre-lecture « machine » rapporte un succès avec `.venv/bin/python`. Je constate seulement
l'échec ici, depuis la racine du dépôt.

**Sorties versées** (dossier `docs/notes/prealables-course-etape-b-bis-v1/repetition-mesure-plancher-v1/`, chacune scellée) :

| fichier | empreinte |
|---|---|
| `sortie-lanceur-py311-v1.txt` | `b922a3244073df29f58edf650a2511ecf3b7d028599abe38552d3742a8e25a5f` |
| `essais-py311-v1.txt` | `5ae80f2f0eac58fb1834fdc487cfdd2863938acfa590ce158125c622af11b619` |
| `fichiers-de-l-arbre-py311-v1.txt` | `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0` |
| `sortie-lanceur-py313-chemin-relatif-v1.txt` | `8ff82414202664af0def6c5f1624f9f4135d679518ed536d62529fdcef9d95ca` |
| `essais-err-py313-chemin-relatif-v1.txt` | `178fbd7732b7511f5dbb492f81ea9a1a155af0b13b45892d192621e7843da730` |
| `sortie-lanceur-py313-v2.txt` | `97ceacda5911c27c7e7f790ba4be31ffeaef0094327006e066fbd1921fafa908` |
| `essais-py313-v2.txt` | `d7047bc161781e17f4b76a5f163f02766815de50d9dd0afc0a51de7cf98b13c4` |
| `fichiers-de-l-arbre-py313-v2.txt` | `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0` |
| `paquets-installes-py311-v1.txt` | `66d379d01de6e8d4a5688d89446864c0380f2e6aa191ecaa769792737c77aa37` |
| `paquets-installes-py313-v1.txt` | `d11ff2947cdec64075009299000e0b295471a747bf9bd097aeedf45c74e0a83a` |

Les sorties d'erreur des deux mesures réussies sont vides (`e3b0c442…`). Les arbres jetables (`depot/`) et les dossiers
temporaires des essais ont été effacés. Les trois dossiers de mesure du bloc-notes ne gardent plus que `essais.txt`,
`essais.err` et `fichiers-de-l-arbre.txt`.

## 4. Différences entre 3.11 et 3.13

- **Issues des essais : aucune différence.**
  - Les lignes de progression de pytest sont identiques caractère pour caractère. Chaque position est le même essai, dans le même
    ordre de collecte, avec la même issue.
  - Les 25 lignes `SKIPPED` sont identiques entre 3.11 et 3.13. Elles sont aussi identiques à la preuve du développeur
    (`essais-arbre-extrait-candidat.txt`, compagnon conforme) :
    - 17 « chaîne de T0.6 absente de ce clone » : bout en bout ×8, contrôle v2 ×1, contrôle v3 ×1, état imposé ×6, second
      addendum l. 488 ×1 ;
    - 7 « code de la pièce absent de cet arbre (instance : extraction partielle) » : lien « mots et coût » ;
    - 1 « fabrique factice de la pièce absente de cet arbre ».
  - Aucun essai n'échoue. Aucun ne saute sous un interpréteur et pas sous l'autre.
  - Les fichiers d'essais de la course ne contiennent aucun saut qui dépende de la version de Python (recherche de
    `version_info`, `skipif`, `importorskip` et `pytest.skip(` au commit : seuls les motifs ci-dessus).
- **Avertissements** :
  - Sous 3.13, il y a 4 avertissements, tous du même essai
    (`tests/test_t07bbis_epreuve_niveau_v1.py::test_petit_jeu_deterministe_et_independant_des_processus`) :
    `DeprecationWarning` de `multiprocessing/popen_fork.py`, « process is multi-threaded, use of fork() may lead to deadlocks ».
  - Cet avertissement n'existe qu'à partir de Python 3.12 ; sous 3.11, il n'y en a aucun.
  - L'essai passe sous les deux. La machine (image `python:3.11-bookworm`) est du côté sans avertissement.
- **Durée** : 399,98 s sous 3.11, contre 128,06 s sous 3.13. **Incident déclaré** : de 05:15Z à 05:20Z environ, une boucle
  d'attente que j'avais mal écrite a tourné à vide sur un cœur pendant la mesure 3.11. Elle explique au moins une partie de
  l'écart. Je ne l'ai pas isolée et je ne conclus rien sur la vitesse comparée. Les autres mesures déjà faites sous 3.13 vont de
  128 s à 640 s selon la charge (contre-lectures et preuve du développeur).
- **Paquets** : `requirements-cpu.txt` ne fige pas les dépendances transitives. Le diff des deux listes installées donne :

  | paquet | 3.11 | 3.13 (`.venv`) | remarque |
  |---|---|---|---|
  | contourpy | 1.3.3 | 1.4.0 | |
  | networkx | 3.6.1 | 3.7 | |
  | regex | 2026.11.18 | 2026.11.15 | celle de 3.11 est parue le jour même |
  | pip | 24.0 | 26.2.2 | |
  | setuptools | 79.0.1 | 84.2.1 | |
  | pypandoc_binary | 1.17 | absent | `.venv` n'a pas reçu `requirements-donnees.txt` ; aucun essai de la course ne l'appelle |

  Ces écarts n'ont changé aucune issue.

## 5. Réserves

1. **Répétition seulement.** Le commit `244c4f7a` ne porte pas l'addendum scellé. La mesure définitive reste à faire au commit
   exact de la course (arbitrage, B.1 et B.2), sous les deux interpréteurs, avec des noms de dossier neufs, sorties scellées.
2. **Marge nulle, inchangée** : 151 passés pour un plancher de 151. Un essai de plus ou de moins sur la machine arrête la course.
3. **Ce que cette mesure ne couvre pas sur la machine** :
   - L'image installe `requirements-gpu.txt` au moment de la course. Les dépendances transitives non figées y seront résolues de
     nouveau : `regex` a paru le jour même ici.
   - Le Python 3.11 de l'image n'est pas forcément 3.11.18.
   - Rien n'a tourné sur une carte : `torch.cuda.is_available()` est faux ici, et aucun essai de la course ne demande la carte
     sans garde (contre-lectures « machine » et « adverse »).
4. **Faux refus au chemin relatif** (§ 3) : à porter au feu version 4. L'arbitrage y écrit `.venv/bin/python`.
5. **Incident de calcul de l'auteur** (§ 4, durée) : déclaré. Sans effet sur les comptes.
6. **Disque** : l'environnement 3.11 occupe 5,8 Go dans le bloc-notes. Il reste 8,6 Go libres à 05:28Z, contre 15 Go avant
   l'installation. L'environnement est gardé pour la mesure définitive. Si la place manque, il se recrée en 1 min 9 s à
   partir du manifeste, avec les mêmes versions directes. Les versions transitives seraient résolues de nouveau.
