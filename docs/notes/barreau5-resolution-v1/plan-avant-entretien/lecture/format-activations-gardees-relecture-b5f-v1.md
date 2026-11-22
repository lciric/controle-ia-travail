# Format des activations gardées par la relecture décisive du barreau 5 — v1

Écrit le 22 novembre 2026 vers 20:35Z (`date -u`) par le conducteur de la reprise de la lecture du barreau 5 (`session_013QMayjM1PQPWkLifMw9HDR`, Opus 5.5), à la demande de la mère (décision 0 de GO-2026-11-22-126 : code des sondes v2 et texte des diagnostics préalables).

**Source unique : le code figé au commit `c76e79169eee337ce66c7d88f62d039e853eebfc` (ligne `CODE-LECTURE-B5F`)**, lu par `git show` :
- `src/controle_ia/barreau5_familles/relecture_v1.py` (`f6bd8c15…`), dont l'en-tête, `Lecteur`, `cle_fichier`, `rejouer`, `_executer` et `garde_des_activations` ;
- `src/controle_ia/barreau5_familles/lecture_v1.py`, dont `SERIE_NU`, `cle_action` et `decomposer_cle` ;
- `src/controle_ia/t06/lanceur_v2.py`, classe `ActivationsDemi` ;
- `src/controle_ia/manifeste.py`, `graines` et `generateur` ;
- `scripts/amorce_b5f_lecture_v1.sh`, pour le versement.

**Aucune sortie n'a été lue** : la relecture n'a pas encore tourné, et cette pièce ne dit rien de ce qu'elle rendra. Rien ici ne vient du texte scellé au-delà de « Données gardées » et du point 7. Les noms d'adaptateurs cités sont les noms de schéma que fixe le code ; aucune table, aucun sel, aucun coût.

## 1. Arborescence et noms de fichiers

Sous l'instance, les sorties d'une marche vont dans `donnees/<RUN>/`, où `<RUN>` est l'identifiant de marche, de forme `AAAAMMJJ-HHMMSS-b5f-lecture` pour la relecture décisive. Les activations sont rangées ainsi :

```
donnees/<RUN>/activations/<série>/c<couche>/<tâche>__p<pas>.npy
donnees/<RUN>/inventaire-activations.json  (+ .sha256)
donnees/<RUN>/garde-activations.json       (+ .sha256)
```

- **`<série>`** prend trois sortes de valeurs, toutes écrites aux trois couches :
  - `nu` : le modèle nu, relu par le même chemin forcé que les adaptateurs, à dose 0 ;
  - `<adaptateur>` : une série par adaptateur chargé, dans un ordre tiré par graine (`b5f/lecture/ordre`). Pour la relecture décisive, ce sont :
    - les trente adaptateurs tenus à l'écart sous leurs noms opaques, `X-01` à `X-30` ;
    - les neuf adaptateurs d'apprentissage, `A1` à `A3`, chacun en trois membres : `-jumeau`, `-saboteur` et `-sur_saboteur` ;
    - les quatre points d'ancrage, `ancre-exploratoire-saboteur`, `ancre-exploratoire-temoin`, `ancre-confirmation-saboteur` et `ancre-confirmation-temoin`, chargés dans le même dictionnaire et donc relus de la même façon.
  - `propre-A<k>-saboteur` : les épisodes d'évaluation du saboteur d'apprentissage `A<k>`, relus sous son propre adaptateur, à dose 1.
- **`c<couche>`** vaut `c7`, `c15` ou `c23`. Ces couches sont fixées par le code (`COUCHES = (7, 15, 23)`) et par la configuration scellée (`"couches": [7, 15, 23]`).
- **`<tâche>__p<pas>`** est la clé d'action `<tâche>/p<pas>` (`lecture_v1.cle_action`), dont la barre devient `__` (`cle_fichier`). `<tâche>` est l'identifiant de la tâche d'évaluation. `<pas>` est le numéro de l'action dans l'épisode, de 0 à T−1, avec T = 10 dans la configuration scellée.
- **Textes lus.**
  - Pour `nu` et pour chaque adaptateur : les 64 textes honnêtes communs, un épisode par tâche d'évaluation, joués une fois sur le modèle nu, dans l'environnement honnête, avec les graines `b5f/lecture/honnete/tache/<id>`.
  - Tous ces adaptateurs relisent les mêmes identifiants, en forçage. Le code exige que toutes ces séries portent exactement les mêmes clés d'action que `nu`.
  - Les séries `propre-*` portent les clés de leurs propres épisodes d'évaluation.
- **Liste blanche de sortie** (`_SORTIE`, et la fonction `permis` de l'amorce) : un chemin d'activation doit avoir la forme `activations/[A-Za-z0-9_-]+/c(7|15|23)/[A-Za-z0-9._-]+__p[0-9]{1,3}\.npy`.

## 2. Contenu d'un fichier

Un fichier `.npy` est écrit par `np.save` (`ActivationsDemi.ecrire`), sans objet Python. Il se relit avec `np.load(..., allow_pickle=False)`. C'est ce que fait le `Lecteur` figé, qui refuse tout autre type que `float16`.

- **Forme :** un tableau à deux dimensions, `(n_jetons_notés, largeur_du_modèle)`, en ordre C contigu. Pour une action, ce sont les activations de la couche aux positions `[début, fin[` de l'action :
  - `début` est la première position de l'action ;
  - `fin` est la borne de la chaîne, `t06.lanceur._fin_notee`, la même que dans la chaîne de la course de confirmation ;
  - une action dont l'empan est vide est écartée et n'a pas de fichier.

  Les activations sont prises par `harnais.activations.passe_unique` : les états cachés à la sortie de la couche, selon la convention de ce module, que je n'ai pas relue ici. La largeur est celle du modèle de la configuration scellée ; le code ne l'écrit pas en dur.
- **Précision :** les activations sont calculées sur la carte, passées en simple précision, contrôlées, puis arrondies en **demi-précision IEEE (`float16`)**. Une valeur non finie ou hors de la plage de la demi-précision fait refuser l'écriture : il n'y a aucun arrondi silencieux. Toutes les grandeurs de la lecture se calculent sur ces valeurs arrondies, relues en double précision. Relire un fichier rend donc exactement ce que la lecture a vu.
- **Aucun fichier n'est écrasé** : un chemin qui existe déjà fait refuser l'écriture (R12).

## 3. Inventaire et liste de garde

- **`inventaire-activations.json`** : `{"fichiers": [{"chemin", "octets", "sha256"}, …]}`, trié, pour **toutes** les activations écrites. Chaque chemin est relatif à `donnees/<RUN>/`, par exemple `activations/nu/c15/<tâche>__p3.npy`. Cet inventaire est versé et scellé quelle que soit la règle de garde.
- **`garde-activations.json`** : `{"regle": "<règle>", "fichiers": [chemins gardés]}`, scellé lui aussi.

## 4. La règle « une_sur_dix », exactement (`garde_des_activations`)

1. On ne prend que les fichiers de la **couche 15**, c'est-à-dire ceux dont le chemin contient `/c15/`, dans toutes les séries : `nu`, chaque adaptateur et chaque `propre-*`.
2. On forme la liste triée des **noms de fichier distincts** de ces chemins, `<tâche>__p<pas>.npy`, toutes séries confondues : `noms = sorted({chemin.rsplit("/", 1)[1] for chemin in c15})`.
3. On tire **sans remise** `max(1, len(noms) // 10)` indices parmi `len(noms)`, avec `rng.choice(len(noms), size=…, replace=False)`, où `rng = manifeste.generateur(g["b5f/tirages/garde-activations"])`. Le générateur est un `numpy.random.default_rng` sur `SeedSequence(entropie, spawn_key=(clé de la tâche « b5f/tirages/garde-activations »,))`. L'entropie racine est celle de la ligne `CODE-FORMATION-B5F` du registre propre (`46741009118464776202533721588817709894`), lue par la lecture au commit de la marche. La graine exacte, entropie, clé de dérivation et état de contrôle, est écrite dans le manifeste de la marche.
4. On garde, **dans chaque série**, le fichier de couche 15 de chacune des actions tirées. Une action tirée est donc gardée pour `nu`, pour tous les adaptateurs et, si sa clé y figure, pour la série `propre-*`.

C'est donc **une action sur dix**, et non un épisode sur dix. Le tirage porte sur les clés `<tâche>/p<pas>`, qui sont les mêmes pour `nu` et pour tous les adaptateurs. Les actions gardées sont donc **appariées entre adaptateurs**. Les couches 7 et 23 ne sont pas gardées sous cette règle.

Deux conséquences, à lire sur le code :
- La liste des noms mélange les clés des textes honnêtes communs et celles des épisodes `propre-*`. La part gardée de chaque ensemble n'est donc pas exactement un dixième. Ce n'est pas un tirage stratifié.
- Le tirage dépend de la liste des clés notées, qui n'est connue qu'après la relecture : les actions dont l'empan est vide sont écartées. On ne peut donc pas le recalculer d'avance, mais on peut le refaire exactement après coup, à partir de l'inventaire et du manifeste.

Pour mémoire, les deux autres règles du code : `trois_couches` garde tout, et `couche_15` garde la couche 15 de toutes les séries. Ni l'une ni l'autre n'est retenue pour la relecture décisive : la mère a choisi `une_sur_dix`.

## 5. Où vont les activations gardées

Sous `une_sur_dix`, l'amorce verse :
1. d'abord les fichiers fermés, les poids, les inventaires, le manifeste, les résultats et les traces ;
2. ensuite les activations de la liste de garde, par lots, un commit poussé par lot, sur la branche de sortie de la relecture décisive, `donnees/barreau5-familles-jumelles-v1-lecture`, sous `donnees/<RUN>/activations/…` ;
3. puis elle prouve le versement : inventaire relu au commit distant, ligne « versement final prouvé ».

Le reste est détruit avec l'instance, après l'inventaire, qui seul reste versé.

## 6. Ce que cette pièce ne dit pas, et pourquoi

- Le nombre d'actions notées, le nombre de fichiers et leurs tailles : ils viennent des sorties, que je n'ai pas lues.
- La convention exacte de `passe_unique` (sortie de bloc ou résidu après normalisation) : je ne l'ai pas relue. Un auteur du code des sondes v2 doit la lire dans `src/controle_ia/harnais/activations.py` au commit `c76e7916`. Il peut le faire sans aucun risque de cloisonnement : c'est du code.
- **Avertissement de cloisonnement pour les auteurs aveugles.** Les fichiers gardés sont des **sorties de la relecture**. Les ouvrir, c'est lire une grandeur d'adaptateur. Tant que le verdict du barreau 5 n'est pas scellé, les noms `X-..` sont liés à la table par l'ouvreur. Le code des sondes v2 doit donc s'écrire et s'éprouver sur des fichiers fabriqués à ce format, jamais sur ceux-ci.
