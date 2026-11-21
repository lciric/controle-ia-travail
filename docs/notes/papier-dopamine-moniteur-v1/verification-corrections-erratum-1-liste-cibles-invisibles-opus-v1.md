# Vérification des corrections de l'erratum 1 de la liste figée des cibles invisibles — v1 (2026-11-21T20:57:18Z, `date -u`)

Classe B (instrument). Vérificateur : Claude Opus 5.5, dans le rôle du contre-lecteur de `contre-lecture-erratum-1-liste-cibles-invisibles-opus-v1.md` (`4d2eed09…`), relue. Accord visé : GO-2026-11-21-69. Rien committé, rien poussé.

## Verdict : à corriger

Les trois corrections demandées sont faites et justes : le commit de la provenance (C-1), la réserve sur l'exclusion de git (C-2) et le compte de la docstring (C-3). Les trois remarques sans correction exigée ont reçu une réponse. La liste v5 est juste et ne change de la v4 que ce qu'elle dit. L'essai v5 passe sur le cas sain et échoue sur chaque artefact joué. Une correction reste à faire par erratum, dans l'essai neuf de l'égalité des objets git : il fait passer pour « historique tronqué » un commit qui existe mais ne porte pas encore le fichier. C'est le genre d'erreur que C-1 visait. Il reste aussi deux détails de texte. Rien de cela ne touche au contenu de la liste v5.

## Pièces vérifiées (empreintes recalculées, toutes égales à leurs compagnons)

| pièce | empreinte |
|---|---|
| `docs/notes/papier-dopamine-moniteur-v1/erratum-1-liste-cibles-invisibles-v3-v2.md` | `21bb82606976c5524abd676a5be157a6048d2c0c7bc23ec66622d5bb44e5c621` |
| `tests/liste_cibles_invisibles_v5.json` | `37bcbb01372114d373ab2ec3be011f211aeb96c2fa038aa39f2eb4a136234081` |
| `tests/test_cibles_invisibles_v5.py` | `28970e8609f9794273ecabd0998f38762a0b95defd4524084be9d93f1af39828` |
| `tests/liste_cibles_invisibles_v4.json` (intacte) | `e6724709bb11c58cc56e4058bd8111846b2c433921613a2cc2c0f2f123f4a5f8` |
| `tests/test_cibles_invisibles_v4.py` (intact) | `b93959b67fc77d1d6d1fc8815c0d8c2274f73c368e2ba063aada6ebab6997351` |
| `tests/test_cibles_invisibles_v3.py` (intact) | `93a6df4343f876cad58c01933d2636e65858bc8d55a99285edd4125cb5d504a9` |

## Remarque par remarque

| remarque de la contre-lecture | constat |
|---|---|
| C-1 : commit faux pour `dopamine_exploratoire/modele_v1.py` | **corrigée.** Le `commit` de la liste v5 vaut `d6cde6667b789d165c672991608388a36e4a098f`. `git rev-parse` donne `c0d0f58e…` à `d6cde666`, `e6fbe03a`, `6c4fd6e9` et à la tête. `git hash-object` du fichier donne la même valeur, et `b1b29073` donne toujours `bd248bb4…`. La ligne 17 de la note et le tableau des sources nomment `d6cde666`. Le registre des décisions nomme bien `d6cde666` à la ligne R-4571. Le `diff` de la v4 à la v5 ne touche qu'aux métadonnées, à la table des corrections et aux champs `commit` et `verification` de cette entrée. |
| C-2 : réserve 6 inexacte | **corrigée.** Les lignes 87, 90 et 92 de `.git/info/exclude` sont les bonnes. Les six fichiers de la v4 sont au commit `25986189` (2026-11-21T20:11:34Z). Les pièces v5 sont exclues aux lignes 133, 135 et 136 (`git check-ignore -v`), et la note les nomme une à une pour l'ajout forcé. |
| C-3 : « quarante » dans la docstring | **corrigée.** La docstring dit « quarante-trois », et un essai le compare à la liste. |
| sans correction exigée : argument libre de `tache_de` | **répondue.** `recherche_simple` exige un nom, ou un nom indicé par un nom ou une constante, sans mot-clé. Les arguments du code réel sont tous admis (`t`, `tache`, `ep["tache"]`, `par_id[i]`, `par_id[t]`, `par_tache[tache]`), ce qui concorde avec la réserve 4. La limite restante est écrite. |
| sans correction exigée : forme du commit seulement | **répondue, avec un défaut** (correction V-1 ci-dessous). |
| sans correction exigée : R-4596 ambigu | **répondue.** Renvoyée à la mère, comme il convenait. |

## Correction demandée

**V-1 (essai de l'égalité des objets git, par erratum).** `objets_git` (ligne 190 de l'essai v5) range dans `absents` tout échec de `git rev-parse COMMIT:chemin`. Deux cas y finissent ensemble :

- le commit manque à l'historique tronqué : un saut est légitime ;
- le commit existe mais ne porte pas le fichier, parce qu'il nomme un commit antérieur à sa création. C'est une provenance fausse.

Dans le second cas, l'essai se saute avec un motif faux (« commit nommé absent de l'historique local (tronqué) »). Artefact joué : `lanceur_v8.py` nommé au commit `25236c16`, qui existe dans l'historique et où ce fichier n'existe pas encore. L'essai de l'égalité se saute. Seul l'essai de comparaison à la v4 échoue, et seulement parce que cette liste-ci se compare à la v4. Correction : tester d'abord l'existence du commit (`git cat-file -e COMMIT^{commit}`) ; s'il existe et que le chemin n'y est pas, faire échouer l'essai ; ne sauter que si le commit manque. Il faut ajouter l'artefact « commit présent sans le fichier » à la garde, et le cas sain reste celui de la liste v5.

## Détails (erratum ou version suivante)

- **D-1.** La table d'en-tête de l'essai v5 dit « trois artefacts neufs » pour la preuve durcie. L'essai en porte quatre : l'indice composé `t[k][j]` est le quatrième. La note signale ce décalage pour la table de la liste v5, mais pas pour l'en-tête de l'essai.
- **D-2.** Pour la course sur la tête `6c4fd6e9`, la note parle de « 2 échecs : les deux essais d'inventaire ». Sur la tête que j'ai jouée, les deux échecs sont `test_inventaire_tout_constructeur_d_invite_est_examine` et `test_chaque_ligne_ajoutee_est_necessaire`, c'est-à-dire la mutation. `test_inventaire_registre_a_jour`, lui, passe. Il faut nommer les deux essais.

## Ce que j'ai rejoué

Toutes les courses ont été faites avec `PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider …`, chacune avec un `--basetemp` neuf dans mon bloc-notes.

1. **Cas sain sur l'arbre examiné.** La copie de l'arbre `e6fbe03a` par `git archive` a échoué : le disque est plein (moins de 2 Mo libres sur `/`), et j'ai supprimé ma copie partielle par son chemin écrit en entier. À la place, un greffon de mon bloc-notes (`arbre_examine2.py`) restreint le balayage de l'essai v3 aux fichiers de `src/controle_ia` présents dans `e6fbe03a`. Les modules plantés dans le dossier temporaire restent vus. Entre cet arbre et la tête, `src/` n'a reçu que des ajouts, sans aucune modification : `garde_google_v1` à `v3`, `cache_tokeniseur_v2`, `lanceur_v9`, plus `relecture_fable_api_v1.py`, non suivi et exclu. Résultat : **49 passés**. Les deux essais de l'égalité des objets sont joués et passent, puisque la course se fait dans le dépôt. Avec le même greffon, l'essai v4 donne 41 passés. L'essai v3 seul donne 2 échecs et 19 passés, comme avant.
2. **Tête réelle (`4814dc47e`).** Résultat : 47 passés et 2 échecs (voir D-2). Les échecs viennent de six fonctions hors de l'examen : les trois de `lentilles_sondes_bbis/lanceur_v9.py` (réserve 2) et trois de `controle_ia/relecture_fable_api_v1.py` (`_ligne_base`, `lire_entree`, `relire`). Ce dernier fichier est apparu après la correction, n'est pas suivi par git et est exclu (`.git/info/exclude`, ligne 138). La réserve 2 ne le nomme pas, puisqu'il lui est postérieur. Son examen revient à la mère, avec celui de `lanceur_v9`.
3. **Artefacts sur la liste**, joués en mémoire, sans fichier écrit, en appelant les fonctions d'essai de la v5. Le balayage est restreint comme au point 1. Le cas sain, la liste v5 telle quelle, passe sur les sept essais appelés.

   | artefact | essais qui échouent |
   |---|---|
   | commit faux de la v4 remis (C-1) | égalité des objets, garde de l'égalité, comparaison à la v4 |
   | commit inventé pour `lanceur_v8` | comparaison à la v4 (l'égalité se saute en le disant) |
   | `lanceur_v8` nommé à `25236c16`, commit présent, fichier absent | comparaison à la v4 seulement (l'égalité se saute à tort : V-1) |
   | ligne ajoutée retirée (`formation_v1.py::jouer_sans_activations`) | comparaison à la v4, compte de la docstring, mutation |
   | ligne retirée de la table des corrections | comparaison à la v4 |
   | seconde source changée en plus de la correction | comparaison à la v4 |
   | docstring revenue à « quarante » (C-3) | compte de la docstring |

4. **Preuve durcie sur le code réel**, avec la source lue en mémoire puis mutée, sans aucun fichier écrit. Les quatre modules de la raison « environnement sur tache_de » passent sains : 3, 2, 2 et 1 appels, aucun fautif. J'ai ensuite muté chaque argument de `tache_de` de quatre façons : tâche en dictionnaire enrichi, tâche passée par une fonction, mot-clé ajouté, indice composé. Toutes les mutations sont vues. La seule exception est l'indice constant ajouté à un nom simple (`tache[0]`), que la règle admet par construction. C'est la limite écrite, pas un défaut.

## Écarts à la consigne

Aucune commande de liste hors de mon bloc-notes. J'ai seulement utilisé `git ls-tree` sur `e6fbe03a` dans un programme, pour filtrer les noms, et `git ls-files -o -i` sur `src` pour trouver les fichiers exclus. Aucun fichier interdit n'a été ouvert, et aucun résultat ni aucune donnée n'a été lu. Le module de la fabrique de l'épreuve à vérité plantée n'a été ni ouvert ni muté. L'essai l'importe, comme il le fait dans le dépôt. La copie avortée par `git archive` portait des fichiers de code dont le nom contient « verite » ou « scores ». Elle a été supprimée sans qu'aucun ne soit ouvert.

## Versement

Cette note est exclue de git elle aussi (`.git/info/exclude`, ligne 134, motif `verification-corrections-erratum-1-*`). Elle se verse par ajout forcé, avec son compagnon `.sha256`. Le disque était plein pendant la vérification : il faut le signaler à la mère avant tout versement.
