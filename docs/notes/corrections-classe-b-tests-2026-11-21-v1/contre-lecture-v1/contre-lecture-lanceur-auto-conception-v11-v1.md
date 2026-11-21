# Contre-lecture du lanceur d'auto-conception v11 (filtre « programme à épingler ») — v1

**Verdict : Conforme**, avec deux réserves consignées (pas de blocage) : la v11 ne pose aucune exigence sur l'interpréteur lui-même (parité exacte avec la v10 sous `/usr/`, voir B1) ; l'essai à blanc éteint n'a pas pu être joué dans ma copie partielle (sauté, voir C3).

Nature : contre-lecture de classe B, un seul mode d'échec par ligne, lecteur neuf, hostile. Aucune écriture hors de mon dossier ; ni commit, ni fournisseur, ni clé, ni dépense ; l'environnement du conteneur n'a pas été affiché.

## Quatre lignes

| # | Question | Tenu / cassé | Le passage visé | Preuve |
|---|---|---|---|---|
| 1 | La v11 diffère-t-elle de la v10 sur autre chose que le filtre, les noms de version et le message « tentative déjà lancée » ? | **Tenu** (sous réserve de lecture : les « noms de version » sont plus nombreux que les trois cités, tous des noms) | `diff` complet, lignes 2 à 21 (chaîne de documentation), 361, 468 à 469, 483 à 488, 1033, 1142, 1982, 2943 de la v10 | A1 |
| 2 | Le filtre relâche-t-il quelque chose de non prévu ? | **Tenu** : aucun relâchement au-delà de l'exemption écrite ; deux propriétés notées (B1, B2) | `scripts/lancer_course_auto_conception_v11.py` lignes 2002 à 2004 | B, sept artefacts prédits d'avance, 7 sur 7 comme prédits |
| 3 | La correction est-elle prouvée sous `.venv` ? | **Tenu** : 12 passés, 1 sauté sous `.venv/bin/python` et sous `/usr/local/bin/python3` | fichier d'essais v11, depuis une copie partielle | C |
| 4 | Les essais sont-ils mérités (filtre v10 remis) ? | **Tenu** : 6 essais rougissent sous `.venv`, 5 sous l'interpréteur système ; détail ci-dessous | filtre v10 remis dans la v11 | D |

Empreintes lues : v10 `f4196ec5…a07a` (`scripts/lancer_course_auto_conception_v10.py`) ; v11 `fbc60aa7…3f09` ; essais v11 `909dd23f…a944` (les deux égales à leur compagnon `.sha256` dans `docs/notes/corrections-classe-b-tests-2026-11-21-v1/`).

## Relevé de méthode

### Chaîne de raisonnement

**A. Différentiel (ligne 1).**
1. `diff` de `/home/user/controle-ia-travail/scripts/lancer_course_auto_conception_v10.py` (`f4196ec5…a07a`) contre `docs/notes/corrections-classe-b-tests-2026-11-21-v1/scripts/lancer_course_auto_conception_v11.py` (`fbc60aa7…3f09`), joué par moi, sans l'essai de l'auteur : 10 blocs de différences, et rien d'autre (ligne 1, le shebang, et la fin de fichier ne figurent pas dans le différentiel).
2. Bloc `2c2,21` : la ligne 2 de la chaîne de documentation est remplacée et 19 lignes de texte sont ajoutées dans la chaîne ; le texte de la v10 suit, intact. La chaîne de documentation du module n'est lue par aucun code : `grep -n "__doc__"` ne trouve que `decouper_matiere.__doc__` (ligne 920 de la v11), qui est celle d'une fonction.
3. Blocs `361c380`, `468,469c487,488` : `VERSION`, `DOSSIER_SORTIES`, `SUFFIXE_RUN` en v11 (noms).
4. Blocs `483c502,503` et `488c508` : le suffixe de la v10 s'ajoute à `SUFFIXES_DEJA_LANCEE` et son dossier de sortie à `SORTIES_AUTRES_VERSIONS` (noms ; effet : la v10 est comptée parmi les versions déjà lancées).
5. Bloc `1033c1053` : le message « tentative v11 déjà lancée » (cité par l'énoncé). Bloc `1142c1162` : l'en-tête du registre dérivé (nom). Bloc `2943c2965` : le nom du dossier d'alerte de crédit, `…-v10` devenu `…-v11` (nom).
6. Bloc `1982c2002,2004` : le filtre. C'est le seul changement de logique.
7. Réserve de lecture : les « noms propres de version » du texte de la question sont en réalité sept sites (pas 3) ; tous sont des chaînes de nom, aucun n'est une condition. Le lecteur de l'auteur en liste neuf dans `CHANGEES` (essais, lignes 202 à 226) ; mon différentiel retrouve les mêmes neuf lignes retirées et ajoutées.

**B. Le filtre (ligne 2).**
8. Texte lu (v11, lignes 2002 à 2004) : `interpretes = {sys.executable, os.path.realpath(sys.executable)}`, puis `fichiers` écarte en plus tout élément `x in interpretes` (égalité de chaîne) ; la suite (`not fichiers or any(sha256_fichier(x) not in permis …)`) est inchangée.
9. Conséquences lues du texte, avant épreuve : (i) l'exemption est une égalité de chaîne, pas une identité de fichier : un autre chemin vers le même binaire reste à épingler ; (ii) elle ne dépend pas de la position dans la commande ; (iii) `fichiers` vide reste refusé ; (iv) elle s'applique à Astra et à Carbon (même bloc) ; (v) elle suit `sys.executable`, quel que soit ce fichier.
10. Sept artefacts à moi, écrits et prédits avant de jouer (`copie/tests/test_artefacts_contre_lecteur.py`, en tête du fichier : P1 à P7). Résultat : voir « Objets de contrôle » ; 7 sur 7 comme prédit, sous `.venv/bin/python` et sous `/usr/local/bin/python3`.
11. P1 montre le seul point où la v11 laisse passer ce que la v10 refusait en dehors du cas visé : commande `[lien-hors-usr, "-I", "-c", "code non épinglé", script-épinglé, …]` acceptée par la v11. La v10 l'accepte déjà avec un interpréteur sous `/usr/` (`/usr/local/bin/python3`, rejoué dans le même essai) : parité, pas un relâchement nouveau. Le défaut vient de ce que le filtre exige qu'un fichier de la commande soit épinglé, non que ce soit l'argument de programme de l'interpréteur ; il préexiste.

**C. Preuve sous `.venv` (ligne 3).**
12. Copie partielle sous `…/contre-lecteur-v11/copie/` : `scripts/` (v10 et v11), `tests/` (essais v11, `conftest.py`), `pyproject.toml`, `src/` (copie du dépôt), et la pièce que le filtre lit : `docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json` (empreinte vérifiée par l'essai lui-même, `_fixe()`).
13. `PYTHONPATH=src TMPDIR=…/contre-lecteur-v11/tmp /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_lancer_course_auto_conception_v11.py -rs` : **12 passés, 1 sauté**. Même commande avec `/usr/local/bin/python3` : **12 passés, 1 sauté**.
14. Sous `.venv`, `sys.executable` est le vrai lien `.venv/bin/python` (hors `/usr/`, `readlink -f` : `/usr/local/bin/python3.13`) : `test_cas_sain_interprete_reel` joue donc sans simulation le cas du tri ; sous l'interpréteur système, il joue le chemin `/usr/…`. Les quatre autres essais du filtre posent un lien simulé dans le dossier d'essai et disent la même chose sous les deux interpréteurs.
15. Le seul essai sauté est `test_essai_a_blanc_eteint_v11` : la copie n'est pas un dépôt git (`git show refs/remotes/origin/main:…matiere-premiere-v3.md` échoue). Je ne l'ai ni forcé ni contourné. Il n'est pas dans le périmètre du filtre. Réserve C3.

**D. Essais mérités (ligne 4).**
16. Copie `copie-mut/` : dans la v11, les trois lignes du filtre sont remplacées par la ligne exacte de la v10 (une seule ligne `fichiers = [...]`). Mêmes essais, mêmes commandes.
17. Sous `.venv` : **6 rougissent** sur 12 + 1 sauté. Sous `/usr/local/bin/python3` : **5 rougissent** (`test_cas_sain_interprete_reel` passe, car l'interpréteur est sous `/usr/`). Tableau à la rubrique « Évaluateur et conseil ».
18. Contre-mutation (relâcher trop) : remplacer l'exemption par `not os.path.samefile(x, sys.executable)` (tous les liens vers le même fichier écartés). Sous `/usr/local/bin/python3`, 5 essais rougissent : le seul essai de l'auteur qui tue cette variante est `test_artefact_autre_lien_vers_le_meme_interprete` ; mes P3 et P6 la tuent aussi (voir plus bas).

### Objets de contrôle

Mécanisme éprouvé : le filtre « programme à épingler » corrigé.

- **Objet où la conclusion « ce programme est non épinglé et doit être refusé » est vraie par construction** : un second fichier du dossier d'essai (`evil.py`, `autre.py`), un script d'empreinte absente de la pièce, une copie de l'interpréteur à un autre chemin, un autre lien vers le même binaire, une commande sans aucun fichier épinglé. Prédit : refus « programme non épinglé ».
- **Objet où la conclusion est fausse par construction** (le programme est l'interpréteur courant, qui ne doit pas être épinglé) : `sys.executable`, sa cible résolue, un lien hors `/usr/` simulé. Prédit : acceptation.
- Résultat de mes sept artefacts (prédictions écrites dans l'en-tête de `copie/tests/test_artefacts_contre_lecteur.py`) :

| Artefact | Prédit | Rendu | Sous les deux interpréteurs |
|---|---|---|---|
| P1 `[lien, -I, -c, code, script épinglé]` | accepté (parité v10 sous `/usr/`) | accepté ; v10 sous `/usr/local/bin/python3` accepte la même forme ; v10 avec le lien hors `/usr/` refuse | oui |
| P2 copie des octets de l'interpréteur à un autre chemin, devant un script épinglé | refusé | refusé | oui |
| P3 chemin du lien écrit avec `/../bin/python` (même fichier, `samefile` vrai) | refusé | refusé | oui |
| P4 programme non épinglé en tête, lien courant en argument | refusé | refusé | oui |
| P5 `sys.executable` posé sur un fichier quelconque non épinglé | accepté (l'exemption suit `sys.executable`, non l'identité du binaire) | accepté | oui |
| P6 maillon intermédiaire de la chaîne de liens (`venv/bin/python3` quand `sys.executable` est `venv/bin/python`) | refusé ; et le lien courant lui-même accepté (contraste) | refusé ; contraste accepté | oui |
| P7 copie de l'interpréteur en tête, lien courant en argument | refusé | refusé | oui |

Le lien vers lui, sa copie et sa cible résolue sont donc traités ainsi : sa cible résolue et lui seul passent ; un lien, un maillon, une copie ou un chemin écrit autrement restent à épingler (et ne passent que s'ils le sont).

### Premier pas non justifié

Pas 9 (v) et pas 11, portée : la correction suppose que `sys.executable`, dans le processus du lanceur, est le binaire qui exécutera la commande d'Astra ou de Carbon. Rien dans le lanceur ne le fait respecter : une commande `[autre-fichier, …]` où `autre-fichier` serait `sys.executable` d'une autre machine ne se rencontre pas, mais P5 montre que l'exemption ne vérifie aucune propriété du fichier. Ce qui le justifierait : une mention écrite, dans la pièce de départ, que l'interpréteur du lanceur est celui de la commande, ou une exigence que `b["commande"][0]` soit cet interpréteur. Je ne la tiens pas pour un défaut de la v11 (le motif est celui du tri : l'interpréteur prescrit par `CLAUDE.md`), je la signale.

### Trouvaille de côté

- B1 : aucune exigence sur l'interpréteur, et le trou `-c` : tant qu'un fichier épinglé figure ailleurs dans la commande, un `-c` ou un `-m` non épinglé passe (P1). Préexistant sous `/usr/` en v10, nouveau seulement pour un interpréteur hors `/usr/`. Pas un défaut de la correction ; à noter pour qui reprendra le filtre.
- B2 : l'exemption est positionnelle-agnostique et s'applique à Astra et Carbon ; `fichiers` pour Carbon sert ensuite à lire les `.sh` (ligne 2016) : l'interpréteur n'y est jamais lu, ce qui est le comportement voulu.
- Portée de la correction (hors ma question) : le tri compte 240 essais touchés (230 pour les lanceurs d'auto-conception v1 à v9 selon sa table, 10 pour l'affinage et les déclarés), qui chargent le lanceur de leur propre version. La v11 ne corrige que le lanceur v11 ; ces essais continuent de rougir sous `.venv`. Seul un correctif sur les lanceurs anciens (règle R12 : nouvelle version, non réécrite) ou sur les essais le change. Non poursuivi.

### Évaluateur et conseil

Ce qui juge la correction : le fichier d'essais v11 (12 essais joués, 1 sauté). Témoins : l'essai sain sous interpréteur réel (vrai `.venv/bin/python` en production du cas), le contraste « la v10 refuse le même cas » (`test_v10_refuse_le_meme_cas`, le seul essai qui charge la v10 côte à côte), et les artefacts de refus. Par où elle obtiendrait un bon jugement sans le mériter : le cas « sain » est écrit avec un script épinglé par son empreinte dans une pièce d'essai que l'auteur fabrique (`_depart`), donc l'essai ne montre pas que la pièce de départ réelle de la mère épingle bien un script et non l'interpréteur ; et deux des essais qui rougissent à la mutation (ci-dessous) rougissent pour une raison de texte, non de comportement.

Mutation « filtre v10 remis » (`copie-mut/`, même fichier d'essais) : essais qui rougissent, chacun avec son passage et sa preuve.

| Essai | Rougit ? | Pourquoi (preuve) |
|---|---|---|
| `test_cas_sain_interprete_reel` | sous `.venv` seulement | `.venv/bin/python` est hors `/usr/` : il entre dans `fichiers`, son empreinte n'est pas dans la pièce : refus « programme non épinglé » (sous `/usr/local/bin/python3` : passe, c'est le chemin `/usr/`) |
| `test_cas_sain_interprete_lien_hors_usr` | oui, les deux | lien hors `/usr/` : même refus |
| `test_cas_sain_cible_resolue_de_l_interprete` | oui, les deux | copie hors `/usr/` : même refus |
| `test_artefact_commande_sans_programme` | oui, les deux | « DID NOT RAISE » : dans cet essai, la pièce de départ épingle l'interpréteur lui-même ; avec le filtre v10, il compte comme programme épinglé et la commande `-c` passe ; avec la v11, `fichiers` est vide et la commande est refusée. L'essai distingue donc bien les deux filtres, mais par l'épinglage de l'interpréteur, non par « aucun programme » en général |
| `test_mutation_filtre_v10_remis_attrape` | oui, les deux | cassé par texte : `assert source.count(FILTRE_V11) == 1` échoue (0), parce que ma mutation est sur disque ; il ne joue pas son comportement. Il ne prouve que dans sa propre mutation en mémoire, qui passe sur la v11 intacte |
| `test_le_reste_de_la_v10_inchange` | oui, les deux | cassé par texte : `retirees != CHANGEES["retirees"]` (le filtre v10 n'est plus une ligne retirée). C'est son rôle : il garde le différentiel |

Ne rougissent pas (attendu : ce sont des refus qui tiennent avec les deux filtres, ou des noms) : `test_v10_refuse_le_meme_cas` (charge la v10), `test_artefact_autre_programme_non_epingle`, `test_artefact_autre_lien_vers_le_meme_interprete`, `test_artefact_script_non_epingle`, `test_noms_propres_v11`, `test_documentation_garde_le_texte_de_la_v10`, et l'essai sauté. Sur ces refus, mérités en sens inverse (relâcher trop) : la variante `samefile` fait rougir `test_artefact_autre_lien_vers_le_meme_interprete`, ce qui montre qu'il peut échouer ; `test_artefact_autre_programme_non_epingle` et `test_artefact_script_non_epingle` ne rougissent pas à `samefile` (ce n'est pas ce qu'ils gardent).

Décompte : 4 essais de comportement rougissent sous `.venv` (les trois sains et l'essai sans programme) ; 3 sous l'interpréteur système (le sain réel passe) ; 2 essais de texte rougissent dans les deux cas.

## Réserves

- **B1** : voir « Trouvaille de côté ». Parité avec la v10 sous `/usr/`, nouvelle seulement pour l'interpréteur hors `/usr/`.
- **C3** : l'essai à blanc éteint n'a pas été joué (copie sans dépôt git). À jouer par qui a la référence de `main`.
- **D** : `test_artefact_commande_sans_programme` tient par l'épinglage de l'interpréteur dans la pièce d'essai, pas par « aucun fichier » ; le nom promet un peu plus que ce qu'il garde. Non bloquant.
- Aucun identifiant de modèle dans cette pièce. Pièces à moi : `copie/tests/test_artefacts_contre_lecteur.py`, `copie-mut/` (mutations).
