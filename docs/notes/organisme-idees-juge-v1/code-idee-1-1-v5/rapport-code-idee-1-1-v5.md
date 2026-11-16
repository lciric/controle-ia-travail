# Rapport du développeur — code de l'idée 1.1, version 5 (complément de la copie du v9 dans la vue ; étape 0 v4 du 16 novembre, R-2976, `etape0-idee-1-1-v4.json`, `c6c34fd0…`)

- Auteur : le développeur des versions 1 à 4.
- Date (UTC) : 2026-11-16, de 12:40 à 13:10 environ. Tête de départ : `16484e48`.
- **Ce que je n'ai pas fait** :
  - aucun fichier existant modifié (R12) ;
  - aucun commit, aucun appel réseau, aucun appel payant ;
  - ni étape 0 en vraie grandeur, ni jeu, ni lecture ;
  - rien sous `diag/`, `runs/` ni `donnees/`.
- **Ce que j'ai lancé** : seulement le préalable 1 (c), sur une vue neuve de mon bloc-notes, et les essais v5. Tout a tourné sur un processus, `nice -n 10`.
- Toutes mes tâches d'arrière-plan sont terminées.

## 1. Relevé statique des imports (avant d'ajouter le module)

J'ai relevé, par analyse syntaxique, la fermeture transitive à partir de quatre racines :
- `essais/test_nul_v9.py` ;
- les trois bancs `demonstrations/banc_tricheurs_v9.py`, `…_v8.py` et `…_v7.py`, que les fichiers chargent par `importlib`.

Le relevé porte sur tous les nœuds `import` et `from … import`, **imports paresseux compris** (dans les fonctions). Il recense aussi chaque appel `spec_from_file_location`, `_charger`, `import_module`, `open` et `os.path.join` qui porte un littéral. Les fichiers sont pris dans la vue, avec et sans le module versé.

- **Fichiers atteints** (23 avec le module) :
  - les trois bancs ;
  - `essais/test_nul_v9.py` ;
  - dans `pole` : `__init__`, `adaptateurs`, `attaque_goodhart_v2`, `caviardage`, `controles_pari`, `cycle`, `fiche`, `garde_outils`, `memoire`, `monde_banque`, `monde_noyau`, `nul_filles_v2`, `nul_v8`, `nul_v9`, `outils`, `relais`, `relais_reel`, `selection_pari`, `simulation`.
  
  Tous sont présents dans la vue.
- **Manques sans le module** :
  - `pole.attaque_goodhart_v2`, importé à `essais/test_nul_v9.py`, l. 406. C'est exactement le manque de l'étape 0.
  - Un faux positif : `from . import __version__` dans `pole/outils.py`, l. 160. `__version__` est un nom défini dans `pole/__init__.py` (l. 30), pas un module.
- **Manques avec le module** : aucun, à part ce faux positif.
- **Chargements de fichiers**, tous résolus dans la vue :
  - `_charger("banc_tricheurs_v9.py")` dans l'essai ;
  - `banc_tricheurs_v8.py`, chargé par le banc v9 (l. 68) et par `attaque_goodhart_v2` (l. 152 et 153) ;
  - `banc_tricheurs_v7.py`, chargé par le banc v8 (l. 88).
- **Chemins lus hors de la vue** : `RACINE/prereg/…`, à savoir `preenregistrement-validation-nul-v9-brouillon1.md` (essai, l. 612) et `preenregistrement-validation-nul-v8-v2.md` (banc v8, l. 108).
  - Ces fichiers sont absents de la vue. Les essais qui les nomment les attendent absents ou les fabriquent dans un dossier temporaire.
  - Ils passaient déjà à l'étape 0 v4, et passent au rejeu ci-dessous.
  - Les autres chemins littéraux sont des sorties écrites dans des dossiers temporaires, sous le `TMPDIR` de la vue.

Le script du relevé et ses deux sorties sont dans le bloc-notes, hors du dépôt : `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/releve_imports.py`, `…/releve.json`, `…/releve--sans-attaque.json`.

## 2. Préalable 1 (c) rejoué seul (vue v2, dossier neuf du bloc-notes)

`etape0_idee_1_1_v5.rejeu_essais_v9` a joué la vue `…/scratchpad/rejeu-v5/travail/vue-v9` : 58 fichiers, empreinte de la liste `96107ec2…`. Chaque fichier y est vérifié par empreinte avant et après la recopie, puis après le rejeu. L'interpréteur fils est lancé en `-I -B`, avec son dossier courant et son `TMPDIR` dans la vue.

**37 essais d'origine sur 37 passent**, en 43 s. Classement : « route première passée ». Aucun bloquant, aucun essai à défaut, aucune classe manquante.

Le résultat est dans `…/scratchpad/rejeu-v5/resultat.json`. C'est un rejeu de développeur et non le préalable officiel, qui reste celui de l'étape 0 v5.

## 3. Code v5 (même méthode : couples déclarés, essai d'égalité au différentiel près)

- **Les couples** sont dans `code-idee-1-1-v5/couples-v4-vers-v5.json` : 10 fichiers, dont `vue_v9_v2.py`, dérivé de `vue_v9_v1.py`.
  - Chaque couple déclare son nombre exact d'occurrences `n`, ce qui permet les remplacements de noms répétés, comme le nom du script dans le lanceur.
  - L'essai neuf `test_…differentiel_v5.py` vérifie que chaque source est intacte et que chaque cible lui est égale octet pour octet, au différentiel près.
- **`vue_v9_v2.py`** :
  - `pole/attaque_goodhart_v2.py` (`3c9de8b8…`) et `PROVENANCE-complement-v3.md` (`a4a62a88…`) entrent dans `EMPREINTES_V9` ;
  - le module est donc vérifié avec la copie (contre son empreinte et son compagnon), puis versé dans la vue ;
  - la constante `COMPLEMENT_V3` porte le chemin, l'empreinte et la provenance.
- **Cascade de noms** pour tout ce qui importe la vue :
  - modules : `etape0_idee_1_1_v5`, `execution_idee_1_1_v5` ;
  - scripts : `jouer`, `lire` et `etape0`, en `_v5` ;
  - essais : `banc`, `bout_en_bout`, `execution` et `gardes`, en `_v5`.
- **Modules inchangés et toujours employés** : `banc_idee_1_1_v2`, `lecture_idee_1_1_v4`, `mutations_idee_1_1_v4`, ainsi que les modules v1 de la projection, du juge et des lois.
- **Lanceur et exécution** :
  - le nom du run est `idee-1-1-poids-du-nul-v5`, et un run antérieur, de la v1 à la v5, est refusé ;
  - `version_lanceur` vaut 5 ;
  - `FICHIERS_GELES` compte 46 fichiers, sans doublon et tous présents : les modules en usage, les sources v4 du différentiel avec `vue_v9_v1`, le JSON v5 et les essais ;
  - le lanceur rejoue 7 essais : les 5 essais v5, plus `lecture_v4` et `projection_v4`, dont les modules ne changent pas.
- **Fermeture dynamique des imports** des trois scripts v5 : aucun fichier hors de `FICHIERS_GELES`, aucun module touché d'une version antérieure importé.
- **Fichier d'étape 0 v5** : il s'écrit sous `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v5/etape0-v1/etape0-idee-1-1-v5.json`.
- **Bloc d'addendum** : `declarations_v5()` ajoute `complement_copie_v9` (chemin, empreinte, provenance et son empreinte). Sa remarque dit que **le texte scellé ne citait, comme compléments de la copie `a41b7b5`, que les bancs v7, v8 et v9**, et que l'essai d'origine importe aussi `pole.attaque_goodhart_v2`, versé par la mère (R-2976) et vérifié par empreinte.

| fichier | sha256 |
|---|---|
| `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v5/couples-v4-vers-v5.json` | `61008bafa5b51cd98feb991be10f489541e4e48206df8d9e52167c08f5356ac1` |
| `scripts/etape0_idee_1_1_v5.py` | `ffa5255195efa82278f842b9d6f0ffb2383ec36389921bec14101a0c807186d9` |
| `scripts/jouer_idee_1_1_v5.py` | `c116a4bf943dc5e2f34f157080fc5ab7b3942e37033ad82ace7606066d27f0c8` |
| `scripts/lire_idee_1_1_v5.py` | `398b922af1d2c57e2ec2bfb3ffe167bd6c704665c3d441562aba80ff3f082b05` |
| `src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v5.py` | `54d6a7dd7ae3b25dde2fdeab7e0e48420e1f4147a36f4084691f3646dfc309d4` |
| `src/controle_ia/organisme_idees_juge/execution_idee_1_1_v5.py` | `8542a484bacf37e496f059cea6f5a83db28ed8ecfe8746c1d347560348a763a6` |
| `src/controle_ia/organisme_idees_juge/vue_v9_v2.py` | `bab7b6453cc11b8618b70fd6be55ddaf362fffe3cafe7e79a1f4eddeaf1d225e` |
| `tests/test_organisme_idees_juge_idee_1_1_banc_v5.py` | `2fc13778709c86c710be22e8160ece0b374c28196c446e9d028f40fd765ace89` |
| `tests/test_organisme_idees_juge_idee_1_1_bout_en_bout_v5.py` | `4245f8d4c8e271df6d45cd8e0d7a1179039471760c91a7b9d85272eca890e1bc` |
| `tests/test_organisme_idees_juge_idee_1_1_differentiel_v5.py` | `af450e5cf8b27d18c1d21cd58700256e0877acda8cd58c6639521e62540b9e41` |
| `tests/test_organisme_idees_juge_idee_1_1_execution_v5.py` | `ae6ef7134ab994a78508a03c2f29f0baa02c6dabd7f93eb6318ea14049f63070` |
| `tests/test_organisme_idees_juge_idee_1_1_gardes_v5.py` | `09d40fbb21ed859fe3b232ee33975709a91edd4b50892fc01ce10e407ec05df1` |

## 4. Essais

- Fichiers joués : les 4 essais v5 et l'essai d'égalité v5, sur un processus, `nice -n 10`, `OMP_NUM_THREADS=1`, sans variable `GIT_*`.
- Résultat : **102 passés sur 102**, en 5 min 14.

| fichier | essais |
|---|---|
| banc | 44 |
| bout en bout | 5 |
| exécution | 8, dont le banc des 17 mutations, toutes tuées, et leurs cas sains passés |
| gardes | 34, dont l'essai neuf de la vue v2 (complément listé, vérifié, refusé s'il est altéré) |
| égalité | 11 |

Les essais `lecture_v4` (49) et `projection_v4` (22) ne sont pas rejoués ici : leurs fichiers et leurs modules n'ont pas changé depuis le passage complet de la v4.

## 5. Étape 0, version 5 (à lancer par la mère, après relecture du différentiel v4 → v5 et commit)

```
cd /home/user/controle-ia-travail && .venv/bin/python -I -B scripts/etape0_idee_1_1_v5.py --travail /tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/etape0-travail-v5 --processus 2
```

- La commande imprime le bloc programme avec toutes les déclarations, complément de la copie compris.
- Les lignes d'empreintes s'obtiennent par `--lister-empreintes`.
- Ensuite :
  - jeu : `scripts/jouer_idee_1_1_v5.py --addendum CHEMIN` ;
  - lecture : `scripts/lire_idee_1_1_v5.py diag/organisme-idees-juge-v1/<RUN_ID>`.
- E2 et E3 sont inchangés, toujours au directeur.

## 6. Non éprouvé

- L'étape 0 v5 en vraie grandeur, avec le préalable 1 (c) officiel.
- Le jeu.
- La lecture d'une vraie sortie de jeu.
- La reprise après un vrai arrêt de machine.
- La relecture du différentiel v4 → v5 par un sous-agent neuf.
