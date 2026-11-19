# Notice — développeur habilité côté moniteurs du bras A : classifieur lexical, classifieur de surface, agrégateur séquentiel (lot 16) — version 4 du code

**En bref.**
- **Les versions 1 à 3 permutaient les étiquettes action par action.** La contre-lecture du texte neuf l'a relevé comme bloquant : quand les actions d'un même épisode se ressemblent, le moniteur « repère » à tort bien plus souvent que son niveau. La version 4 permute **par épisode**.
- Chaque permutation passe une garde. Chaque résultat porte en plus la valeur p qui entre dans la famille de Holm (1 si le moniteur n'est pas calculable).
- 46 essais passent. Chaque garde du module, retirée seule, fait échouer un essai : 30 sur 30.
- Les aires, la borne haute, l'aire conditionnelle, les plis, les clés de graine et la preuve d'ordre ne changent pas. Les valeurs p changent, par construction.
- Les versions 1 à 3 restent intactes : **aucune ne doit servir à une lecture décisive.**

Qui : développeur habilité côté moniteurs, session fille de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, le 19 novembre 2026. Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun résultat lu ; aucun poids chargé ; aucune dépense ; jamais la suite d'essais complète. Aucun outil refusé.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| module, version 4 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v4.py` | `230188224f8f73ccfbbb8f4efb602e861eb499c5d73a90f7dbd305623c963c8a` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v4.py` | `40769bc495cbcb0f4796ce5839a258c143b9ba7dbbcc5f59061ad17fddcd1d86` |

Commit `44e3f325` de la branche `claude/bras-a-habilite-developpeur-v1`.

```
PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_autres_moniteurs_v4.py
```
Dernière ligne : `46 passed` (près de deux minutes : l'essai du niveau pèse).

## 2. Le défaut, et sa correction

**Avant.** `_permuter`, recopiée du plancher gelé, échangeait les étiquettes entre toutes les actions d'une tâche. Pour les quatre moniteurs dont l'unité est l'action, cela tient les dix actions d'un épisode pour indépendantes. Elles ne le sont pas : elles viennent du même épisode, de la même condition. La loi de permutation était alors trop étroite, et la valeur p trop petite. L'agrégateur séquentiel, dont l'unité est l'épisode, n'était pas touché.

**Après.** Dans chaque tâche, pli par pli, les épisodes de la dose et de l'honnête échangent leurs étiquettes ; toutes les unités d'un épisode gardent la même étiquette permutée. Un épisode est repéré par sa condition et son rang. La règle vaut pour les cinq moniteurs, y compris quand des actions manquent dans un épisode : l'étiquette suit l'épisode. Les moniteurs appris sont toujours réappris à chaque permutation, sur ces étiquettes.

**Conséquence à écrire au texte.** Une tâche offre seize étiquettes à échanger (huit épisodes de la dose, huit de l'honnête), et non cent soixante. La valeur p est plus prudente ; sa plus petite valeur possible reste 1 ÷ 2 001.

## 3. Garde et essais

- **Garde** `exiger_etiquettes_par_episode`, appelée sur chaque permutation : toutes les unités d'un épisode portent la même étiquette, et chaque tâche garde son nombre d'épisodes étiquetés « dose ».
- **Artefacts** : une permutation action par action (celle de la version 3) est refusée ; une permutation qui change le nombre d'épisodes « dose » est refusée ; un espion montre que la permutation appelle la garde ; son refus arrête la lecture.
- **Essai de structure** : sur vingt permutations, chaque épisode a une seule étiquette et chaque tâche garde huit épisodes « dose » ; même chose quand des actions manquent.
- **Essai du niveau, sur simulation sans donnée.** Aucun effet de dose ; scores portés par l'épisode. Sur 60 simulations, au niveau 0,05 : la permutation par épisode « repère » dans 15 % des cas au plus ; la permutation action par action dans 25 % au moins, et plus du double. L'essai borne large, il ne mesure pas finement.

## 4. Valeur p pour la famille de Holm

Le module n'applique pas la correction de Holm : c'est l'instance d'analyse. Il rend, pour chaque moniteur et chaque dose, `valeur_p_pour_la_famille` : la valeur p haute quand le moniteur est calculable, **1 quand il ne l'est pas**. Si l'instance d'analyse prend ce champ aux trois doses de la famille, celle-ci reste à quinze tests. Cette prise est à vérifier de son côté.

## 5. Ce qui reste

- Vérification par le même contre-lecteur.
- Au texte : l'unité de la permutation (l'épisode) ; le champ de la famille.
- Case 13.1 : le module des cinq moniteurs à citer est la version 4.
