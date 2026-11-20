# Notes du développeur neuf — lanceur de la première passe, version 5 : messages d'arrêt cloisonnés — v1

Pièce de travail (classe C) qui accompagne un instrument de classe B. Développeur neuf, sous-agent de la session des lentilles
(`session_01QPDgKhLLz1oJQwPBeB5aFs`), modèle servi Fable 5.2, branche `claude/brave-galileo-jhp684`, 2026-11-20 (UTC).

- Mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-lanceur-v5-messages-arret-v1.md`,
  `1ba9f15ae4b3bf8bf59a00ab0b02c713d3e49094049d0850e4f726bd363ebaf7`, commit `10fc2082` (empreinte recalculée avant toute
  lecture, égale).
- Mot qui fonde le travail : GO-2026-11-20-56 (cité par le mandat ; je n'ai ouvert aucun registre).
- Addendum de concentration scellé : `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
  `7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`, lu en entier sur la branche principale (empreinte
  recalculée, égale). Texte de lecture v1, `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572` : sections
  « Liste d'arrêt », « Qui, quelle machine, quel coût » et « Code neuf » seulement.
- **La seconde passe (étape 2) n'est pas touchée.**

## 1. Ce qui change, en mots

`src/controle_ia/lentilles_sondes_bbis/lanceur_v5.py` est `lanceur_v4.py` (`dc74be00…`) plus un seul changement : quand le
calcul s'arrête sur **une égalité au vingtième rang d'une direction lue** (addendum, EC-6, étage (i)) ou sur **une égalité
d'une direction nulle décisive pour un libellé** (étage (ii)) :

1. le message entier que l'addendum exige est écrit dans le seul fichier d'arrêt,
   `<sortie>/versement/<run>/calcul-interrompu/arret.json`, champ `motif` ;
2. la sortie d'erreur porte une seule ligne : le nom de l'arrêt et le chemin de ce fichier ; la sortie standard, rien ;
3. aucun identifiant de jeton, aucune valeur, aucune borne de valeur p, aucun nom de statistique ne sort ailleurs.

Le tri se fait dans le lanceur, en trois fonctions courtes et une table :

| nom | rôle |
|---|---|
| `ARRETS_CLOISONNES` | la table (classe, nom affiché) des deux arrêts |
| `nom_d_arret_cloisonne` | rend le nom affiché, ou rien pour tout autre arrêt |
| `verser_arret_cloisonne` | écrit `arret.json` et verse ce qui existe ; ne laisse sortir le message nulle part ailleurs |
| `ligne_d_arret_cloisonne` | la seule ligne que la ligne de commande affiche |

`statistiques_v3.py`, où les deux arrêts sont levés, n'est pas touché (`9a478aa8…`, inchangé). Aucune ligne de calcul ne change.
Les douze autres modules de la liste gardent leurs empreintes de la version 4.

**Différence entière, de `lanceur_v4` à `lanceur_v5`** (outil `outils/fabrique-lanceur-v5-v1.py`, cinq remplacements exacts,
chacun trouvé une fois et une seule) :
- en-tête : un paragraphe « Version 5 » ajouté ;
- `MODULES` : `lanceur_v4` remplacé par `lanceur_v5` ;
- avant `calculer` : la table et les trois fonctions ci-dessus ; dans `calculer`, une branche de trois lignes en tête du
  traitement d'un arrêt, et une phrase ajoutée à sa docstring ;
- dans `principal` : la ligne qui imprime l'arrêt.
Trois lignes de `lanceur_v4` sont retirées (la ligne des modules, la fin de la docstring de `calculer`, l'impression) ; toutes les
autres sont dans `lanceur_v5`, dans l'ordre (essai `test_aucune_ligne_de_calcul_changee_depuis_la_version_4`).

**Pour l'appelant Python, rien ne change** : `calculer` relève l'arrêt d'origine, de sa classe, avec ses champs. Seul l'affichage
de la ligne de commande change. Le versement posé sur l'arrêt (`fichier_d_arret`, `versement_en_echec`) est lu par `principal`.

## 2. La liste des noms d'arrêt

| arrêt | classe (dans `statistiques_v3`) | nom affiché (code fixe, égal au nom de la classe) |
|---|---|---|
| égalité de score au vingtième rang d'une direction lue (étage (i) ; dixième rang pour les deux listes de dix des pôles) | `EgaliteDirectionLue` | `EgaliteDirectionLue` |
| égalité au vingtième rang d'une direction nulle, décisive pour un libellé (étage (ii)) | `EgaliteNulleDecisive` | `EgaliteNulleDecisive` |

Ce sont les deux seules classes d'arrêt nommé de `statistiques_v3` ; un essai le tient
(`test_tout_arret_nomme_du_module_des_statistiques_est_cloisonne`).

**Les lignes exactes de la sortie d'erreur** (une seule ligne, code de retour 3, sortie standard vide) :

| cas | ligne |
|---|---|
| versement fait, fichier d'arrêt écrit | `ARRÊT : <nom> ; fichier d'arrêt : <chemin de arret.json>` |
| versement en échec, fichier d'arrêt écrit quand même | `ARRÊT : <nom> ; fichier d'arrêt : <chemin> ; versement à l'arrêt en échec : rien n'est supprimé` |
| fichier d'arrêt impossible à écrire, versement fait | `ARRÊT : <nom> ; fichier d'arrêt non écrit` |
| fichier d'arrêt impossible à écrire, versement en échec | `ARRÊT : <nom> ; fichier d'arrêt non écrit ; versement à l'arrêt en échec : rien n'est supprimé` |

Hors du nom et du chemin, ce sont des mots fixes : ils ne dépendent ni du message ni de la raison de l'échec (voir § 5, point 1).

## 3. Les quatre points à traiter, et leurs réponses

### 3.1 L'arrêt écrit-il toujours son `arret.json`, même avant le départ du calcul ?

**Un arrêt cloisonné ne peut pas survenir avant le départ.** Montré de deux façons :
- **Par les sources.** `EgaliteDirectionLue` n'est construite que dans `statistiques_v3.exiger_sans_egalite`, et
  `EgaliteNulleDecisive` que dans `statistiques_v3.libelle_sous_departage` ; aucun autre module du paquet ne les lève. Dans le
  lanceur, les fonctions qui y mènent (`st.exiger_sans_egalite`, `st.lecture_signe`, `st.poles_alignes`,
  `st.libelle_sous_departage`) ne sont appelées que dans la classe `_Couche` et dans `_etiqueter`, et celles-ci ne sont appelées
  que dans `_calculer`, après la ligne `etat["parti"] = True`. Le montage n'emploie de `statistiques_v3` que
  `paires_de_lignes_egales` (qui ne lève aucun des deux arrêts) ; l'audit n'emploie que `premiers_gardes` (qui relève sans
  arrêter) ; les sous-commandes `recuperer` et `phrases` n'emploient pas ce module.
- **Par un montage et un calcul entiers sur le monde miniature**, où chaque appel des deux fonctions est suivi : aucun pendant
  le montage ; tous ceux du calcul viennent après le départ.
Les deux sont dans l'essai `test_aucun_arret_cloisonne_ne_peut_survenir_avant_le_depart_du_calcul`.

**Défense, en plus** : si un arrêt cloisonné venait quand même avant le départ du calcul, `verser_arret_cloisonne` écrirait son
`arret.json` (message entier, champ `avant_le_depart_du_calcul`), sans rien verser du dossier de travail, et la ligne de
commande n'en afficherait que le nom et le chemin. S'il venait d'une autre sous-commande (montage, récupération, phrases), qui
n'a pas d'enveloppe de versement, la ligne de commande n'afficherait que le nom et « fichier d'arrêt non écrit » : le message
ne sortirait pas, mais ne serait écrit nulle part. Aucun chemin du code n'y mène.

**Deux cas où `arret.json` n'est pas écrit après le départ**, tous deux dits par des mots fixes (« fichier d'arrêt non écrit ») :
- il existe déjà : le calcul est relancé dans le même dossier de sortie après un premier arrêt. Rien n'est réécrit (R12) ; le
  premier fichier reste, entier. Voir § 5, point 2 ;
- le disque refuse l'écriture.

### 3.2 Le message enchaîné d'un échec du versement

Dans `lanceur_v4`, un échec du versement relevait un arrêt neuf dont le message reprenait le message d'origine (« … ; versement
à l'arrêt en échec (…) : rien n'est supprimé »). Pour un arrêt cloisonné, `lanceur_v5` ne construit plus ce message : l'échec
est noté sur l'arrêt, sa raison est écrite dans `arret.json` (`versement_en_echec` : nom de la classe de l'erreur et son
message), et la ligne de commande ajoute les mots fixes « versement à l'arrêt en échec : rien n'est supprimé ». La raison de
l'échec elle-même ne sort pas sur la ligne de commande. Pour tout autre arrêt, le message enchaîné reste celui de `lanceur_v4`,
octet pour octet (essai `test_autre_arret_echec_du_versement_message_enchaine_inchange`).

### 3.3 Aucune trace d'exception non attrapée ne porte le message

- L'arrêt cloisonné lui-même est toujours attrapé par `principal` (c'est un `Arret`).
- Pendant son versement, toute erreur de la classe `Exception` (arrêt R12, erreur du disque, fichier déjà là) est attrapée dans
  `verser_arret_cloisonne` : aucune ne remonte, donc aucune trace.
- Reste ce qui n'est pas de la classe `Exception` : une interruption du clavier ou une sortie demandée, pendant le versement.
  Python enchaînerait alors l'arrêt en cours à l'interruption et afficherait son message dans la trace. `verser_arret_cloisonne`
  relève l'interruption en coupant cet enchaînement (`raise e from None`) : la trace ne porte que l'interruption.
- `lanceur_v4`, lui, laissait remonter une erreur du disque pendant le versement, avec l'arrêt enchaîné dans la trace.

### 3.4 Le nom de l'arrêt

Le nom de la classe, écrit comme un code fixe dans `ARRETS_CLOISONNES` (§ 2). Un essai tient que le code et le nom de la classe
sont égaux.

## 4. Essais

- **Fichier neuf** : `tests/test_lentilles_sondes_bbis_lanceur_v5_v1.py`, 43 essais. Par garde, cas sain et artefact :

| garde | cas sain | artefact |
|---|---|---|
| la ligne de commande n'affiche que le nom et le chemin | les deux arrêts, par un calcul amorcé, par un processus séparé, et par le calcul entier sur le monde miniature | copie jetable du lanceur qui imprime le message entier : l'essai tombe |
| `arret.json` porte le message entier (les deux identifiants de jeton et la valeur commune ; p_bas et p_haut) | les mêmes | copie jetable qui n'écrit que le nom : l'essai tombe |
| un échec du versement ne fait pas sortir le message | échec simulé (arrêt R12 ; erreur du disque), échec réel (second arrêt dans le même dossier de sortie), fichier d'arrêt impossible à écrire | copie jetable à l'enveloppe de la version 4 : le message enchaîné sort, l'essai tombe |
| aucune trace ne porte le message | interruption pendant le versement | copie jetable qui garde l'enchaînement : la trace porte le message, l'essai tombe |
| les autres arrêts gardent leur sortie | registre sans la ligne de l'addendum ; arrêt après le départ ; refus avant le départ ; échec du versement : sorties égales à celles de `lanceur_v4`, octet pour octet | les quatre copies jetables ci-dessus (un arrêt cloisonné y prend la sortie des autres) |
| sans arrêt, même sortie que `lanceur_v4` | calcul entier par les deux lanceurs, mêmes graines : mêmes tables, mêmes tableaux (octet pour octet), mêmes phrases, même manifeste, hors le nom du lanceur, l'heure et les empreintes qui en découlent | fiche du code à la liste de fichiers de la version 4 : `lanceur_v5` refuse de partir |

  Les copies jetables sont tenues en mémoire : aucun fichier n'est écrit sous `src/`.
- **Essais repris** : les sept fichiers qui importent `lanceur_v4` sont copiés sous des noms neufs qui visent `lanceur_v5`, par
  le même outil (deux remplacements de noms : `lanceur_v4` → `lanceur_v5`, `lentilles_sondes_bbis_jouets_v4` →
  `lentilles_sondes_bbis_jouets_v5`). Aucun fichier existant n'est réécrit.

| fichier d'origine | copie |
|---|---|
| `tests/lentilles_sondes_bbis_jouets_v4.py` | `tests/lentilles_sondes_bbis_jouets_v5.py` |
| `tests/test_lentilles_sondes_bbis_addendum_concentration_v2.py` | `…_addendum_concentration_v3.py` |
| `tests/test_lentilles_sondes_bbis_corrections_contre_lecture_v3.py` | `…_corrections_contre_lecture_v4.py` |
| `tests/test_lentilles_sondes_bbis_garde_egalite_v1.py` | `…_garde_egalite_v2.py` |
| `tests/test_lentilles_sondes_bbis_gardes_non_vues_v3.py` | `…_gardes_non_vues_v4.py` |
| `tests/test_lentilles_sondes_bbis_montage_v4.py` | `…_montage_v5.py` |
| `tests/test_lentilles_sondes_bbis_procedure_v4.py` | `…_procedure_v5.py` |

  **Un seul essai repris change de contenu**, parce qu'il affirmait l'ancienne sortie :
  `test_calcul_arret_nomme_d_une_direction_lue_avant_toute_ecriture_de_table` (garde d'égalité). Il exigeait que la sortie
  d'erreur commence par le message nommé ; sa copie exige la ligne « nom et chemin » et relit le message dans `arret.json`
  (trois remplacements exacts, écrits dans l'outil, table `ACCORDS`).
- **Non copiés** : `…_entrees_v4.py`, `…_nuls_statistiques_v3.py`, `…_lecture_v1.py` et `…_contre_lecture_addendum_v1.py`
  n'importent pas `lanceur_v4` et n'éprouvent pas le lanceur ; ils restent dans la liste des empreintes.
- **Essais du paquet** (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -p no:cacheprovider
  tests/test_lentilles_sondes_bbis_*.py`) : **1 413 essais, tous verts** (`1413 passed in 749.78s`, `sortie-essais-v5.txt`),
  dont 285 de plus qu'avant ce travail : 43 neufs et 242 repris (décompte par fichier, relevé sans les jouer). Les fichiers
  d'essais des versions 1 à 4 restent verts.
- **Essai des essais** (`outils/essai-des-essais-v4.py`, sortie `outils/sortie-essai-des-essais-v4.txt`) : **un témoin sans
  altération, sain ; douze altérations de `lanceur_v5.py`, une à la fois, douze vues**. Chaque altération est jouée sur une copie
  de l'arbre, dans le bloc-notes ; rien n'est écrit dans le dépôt.
- **Non lancée** : la suite complète du dépôt (mandat).

## 5. Ce qui reste ouvert

1. **Les mots fixes de la ligne affichée.** Le mot de Lazar dit que la ligne de commande n'affiche que le nom de l'arrêt ; le
   mandat permet d'y joindre le chemin de `arret.json`. La ligne de `lanceur_v5` porte en plus des mots fixes : le préfixe
   « ARRÊT : » (celui de tous les arrêts du lanceur), « fichier d'arrêt : », et, selon le cas, « fichier d'arrêt non écrit » et
   « versement à l'arrêt en échec : rien n'est supprimé ». Je les lis comme des existences, que l'opérateur a le droit de lire
   (texte v1, « Qui ») : ils ne portent aucun mot du message. **Je ne tranche pas si cette lecture est la bonne** : si le nom doit
   sortir seul, sans un mot de plus, c'est une ligne à changer dans `ligne_d_arret_cloisonne`, et les essais qui comparent la
   ligne entière suivent.
2. **Quand `arret.json` ne peut pas être écrit, le message entier n'est écrit nulle part.** C'est la suite directe des trois
   règles du mandat (le message seulement dans `arret.json` ; jamais sur la ligne de commande) et de R12 (on n'écrase pas). Le cas
   réel est la relance du calcul dans le même dossier de sortie après un premier arrêt : le premier `arret.json` reste, et, les
   graines étant fixes, il porte le même message. Je n'ai pas ajouté de second nom de fichier pour ce cas : ce serait une règle
   neuve. À dire à l'opérateur : après un arrêt, ne pas relancer dans le même dossier de sortie.
3. **Champs de `arret.json` ajoutés dans deux cas seulement.** Quand le versement tient, `arret.json` a la forme de la version
   4 (`run`, `motif`, `morceaux`, `travail`), sans champ de plus. S'ajoutent `versement_en_echec` (échec du versement) et
   `avant_le_depart_du_calcul` (défense du § 3.1) : deux noms que j'ai choisis.
4. **La fiche du code** (`CODE-LENTILLES-BBIS`) doit porter sous `fichiers` les treize modules de `lanceur_v5.MODULES`
   (`empreintes-code-v5.txt`, treize premières lignes) : avec la liste de la version 4, `lanceur_v5` refuse de partir. La
   commande de l'opérateur devient `python -m controle_ia.lentilles_sondes_bbis.lanceur_v5`. Le mandat de l'opérateur et la fiche
   ne sont pas de mon ressort.
5. **Les deux arrêts restent visibles en entier pour un appelant Python** de `calculer` (l'exception relevée porte son message
   et ses champs) : le cloisonnement vaut pour la ligne de commande, comme le mot le dit. Les essais existants en dépendent.
6. **Ce que les jouets ne prouvent pas** : les réserves de `notes-developpement-v2.md`, § 7, inchangées (réseau réel, fréquence
   réelle des égalités). Dans les deux essais de bout en bout, l'égalité est déclarée par la garde elle-même (comme dans l'essai
   existant de la version 4) : aucun jouet ne porte une vraie égalité au fil d'un calcul entier.

## 6. Ce que j'ai lu, expositions, refus d'outil

- **Lu** : `CLAUDE.md` ; mon mandat, en entier ; `lanceur_v4.py` et `statistiques_v3.py`, en entier ; de `constantes_v1.py`, les
  soixante premières lignes et les classes d'arrêt ; l'outil `fabrique-lanceur-v4-v1.py` (début et fin) ; la passation
  `passation-developpeur-deux-passes-2026-11-20-etape-1-close-v1.md` ; `notes-developpement-v2.md` ; `empreintes-code-v4.txt` ;
  la tête et la fin de `sortie-essais-v4.txt` ; le rendu `contre-lecture-code-premiere-passe-addendum-v1.md`, en entier ; des
  essais : les jouets de la version 4 (début, registres, monde), et les passages des six fichiers que j'ai dû accorder ; l'addendum
  scellé, en entier ; les trois sections permises du texte v1.
- **Vu hors de la liste du mandat, en lecture** : neuf lignes de `src/controle_ia/gardes.py` (la classe `GardeArret`, dont
  `Arret` hérite), par recherche ; `requirements-cpu.txt` (pour l'installation) ; les premières lignes de `.gitignore`.
- **Non lu, bien que permis** : `verification-corrections-code-premiere-passe-addendum-v1.md` ; les autres notes du dossier
  `developpement/` ; les autres modules du paquet, où je n'ai cherché que les noms des deux arrêts et du module des statistiques.
- **Vu par des noms seulement** : les noms des fichiers du dossier de la note ; les cinq premiers noms de `docs/sources/`
  (`anteriorite-hm1-20261026`, `anteriorite-web-20261004`, `arxiv-bassins-idees-20261113`, `candidature-taif-2026-10-07`,
  `cartes-modeles-20261006`) ; les noms des fichiers laissés dans le bloc-notes par des agents d'avant (aucun ouvert) ; les
  titres de sections du texte v1 (par recherche).
- **Écart de méthode, déclaré** : mon premier `git pull` a été fait sans nom de branche. De sa sortie je n'ai gardé que les
  trois dernières lignes, qui nommaient `lot/compte-organisme-v1` et `main` ; je ne sais pas si des noms de branches
  `donnees/*`, `calcul/*` ou `verdict/*` étaient dans les lignes coupées. Je n'ai extrait ni lu aucune de ces branches.
- **Erreur de ma part, réparée** : la première version de mon essai des essais copiait `docs/sources/` en entier (2 Go) dans le
  bloc-notes, une fois par altération. Je l'ai arrêtée par son identifiant de tâche, j'ai supprimé les copies, et la version
  rendue ne copie que la copie versée de `readout.py`. Aucun fichier de `docs/sources/` n'a été ouvert, hors celui-là, que les
  jouets lisent.
- **Jamais ouvert** : la liste « Jamais ouverts » du texte v1 ou v2 ; aucune sortie, aucun score, aucune table, aucune lecture,
  aucun verdict de l'apprentissage des sondes sur la tâche ; aucune table de la lecture par la lentille publique ; `diag/`,
  `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `donnees/*`, `calcul/*`, `verdict/*` ; aucun fichier « consigne-privee »
  ou « conception-ii-b » ; aucun registre ; aucune clé (les essais emploient une fausse clé, passée en argument).
- **Installé**, dans le bloc-notes
  (`/tmp/claude-0/-home-user-controle-ia-travail/4c8fa2bf-6366-5665-a27b-6d403d9264f6/scratchpad/developpeur-lanceur-v5/venv`) :
  torch 2.14.1+cpu depuis l'index de PyTorch pour processeur, puis `requirements-cpu.txt` sans torch (numpy 2.4.6, pytest 9.1.1,
  scipy 1.17.1, matplotlib 3.11.2, transformers 5.18.0, tokenizers 0.23.2, safetensors 0.8.0, huggingface_hub 1.33.0). Aucun
  modèle, aucune lentille, aucun corpus téléchargé ; aucune machine, aucune dépense.
- **Refus d'outil** : aucun. Deux commandes longues ont dépassé le délai de dix minutes de l'outil et ont continué en
  arrière-plan : ce n'est pas un refus.

## 7. Scellement et empreintes

Les pièces de ce dossier sont scellées (`python -m controle_ia.scellement sceller`) : `empreintes-code-v5.txt`, cette note,
`outils/fabrique-lanceur-v5-v1.py`, `sortie-essais-v5.txt`, et, en plus des quatre pièces du mandat, l'essai des essais et sa
sortie (`outils/essai-des-essais-v4.py`, `outils/sortie-essai-des-essais-v4.txt`), pour que le décompte du § 4 renvoie à un
fichier (R6). Comme aux versions 1 à 4, aucun compagnon `.sha256` n'est posé à côté des fichiers de code et d'essais :
`empreintes-code-v5.txt` les porte, et la fiche `CODE-LENTILLES-BBIS`, que la session des lentilles écrit, les reprendra.
`python -m controle_ia.scellement verifier-arbre .` : joué après le scellement ; son résultat est dans le message de rendu.
