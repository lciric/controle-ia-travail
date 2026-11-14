# Vérification courte des corrections v2 (m-A) et v3 (destruction vérifiée) du code de l'étape B bis de T0.7 (modèle C), v1

**Déclaration** : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue ; rien ouvert sous `diag/`, `runs/`, `donnees/`, `essai/` ; aucune clé, aucun réseau, aucune machine ; le vrai outil `vastai` n'a jamais été appelé. Aucun refus de permission ni du classifieur.

- **Lecteur** : contre-lecteur neuf, « modèle C » ; n'a écrit ni le code ni les corrections. **Date (UTC, `date -u`)** : 2026-11-14, de 16:48 à 16:55.
- **Copie** : `/home/user/relecture-bbis-corrections-v2`, HEAD `36d555bda911c005fdbff51a92b3fdbe659d73f4` (vérifié). Code lu : différentiel `38c7203e..1db78884` (12 fichiers). Entre `1db78884` et HEAD : quatre fichiers de notes seulement (rapport v3, sortie des essais v3, leurs `.sha256`).
- **Rejoué** : `pytest -q -p no:cacheprovider tests/test_t07bbis_*.py` → **108 passés** en 2 min 51 s. Syntaxe `bash -n` des deux scripts : bonne. Empreintes des cinq fichiers de code = celles du rapport v3 § 5.
- **`MIN_ESSAIS=86`** : jugé d'après la sortie `essais-sortie-corrections-v3.txt` (extraction partielle simulée au commit `1db78884`, même procédure que la v1) : 86 passés + 22 sautés = 108, cohérent avec mon rejeu ; les 22 sautés sont de la même nature qu'avant (chaîne de T0.6, code de la pièce MC absents de l'extraction). 84 → 86 = les deux essais neufs (m-A, destruction) qui tournent sur l'instance. Non rejoué sur extraction (rien cloné).

## Verdict : **scellable avec mineurs**

Les changements font exactement ce qui est dit, avec cas sain et artefact (R5), et ne touchent ni règle de lecture, ni issue, ni seuil, ni graine, ni jeton.

## Une ligne par changement

1. **m-A, `amorce_bbis_v1.sh`** (`SORTIE_LIBRE`, `traces_sur_commit`) : conforme. Posé à 1 juste après le contrôle de l'étape 7, remis à 0 avec `BRANCHE_PRETE=1`. Un arrêt entre les deux copie les traces, construit dans un **index à part** (`GIT_INDEX_FILE`, `read-tree COMMIT`, `add --sparse -f traces/…`, `write-tree`, `commit-tree -p COMMIT`) et pousse ce commit sur la branche de sortie ; la tête, l'arbre et le commit local des entrées de 7b ne sont ni touchés ni poussés. Garde de taille (`SEUIL`) ; trois essais ; `SORTIE_LIBRE=0` d'abord (pas de récursion) ; identité git posée à la l. 117. Essai `test_arret_avant_la_marche_pousse_ses_traces_sans_le_commit_local` : sain (parent = COMMIT, arbre sans `runs/ diag/ donnees/`, commit local absent du distant par `cat-file -e`, tête et fichier modifié intacts) ; artefacts (avant l'étape 7 → rien poussé ; distant injoignable → « traces non poussées », code gardé ; branche prête → chemin ordinaire) ; ordre des marqueurs dans le texte vérifié.
2. **Texte d'aide de `marche_v1.py`** (m-C) : docstring seul (3 lignes), « complet : sonde finale, directions du plancher, sondes du nul, ENC ; interprétation 19 ». Aucun code.
3. **`detruire ID`, `lancer_bbis_v1.sh`** : imprime `GO_ID=… vastai destroy instance ID -y`, puis la ligne de vérification ; refuse non numérique et les cinq instances d'autres sessions (58936096, 58936099, 58936100, 60480302, 60599797 : liste vérifiée caractère par caractère dans `INSTANCES_D_AUTRES_SESSIONS`) ; aucune commande imprimée en cas de refus. Conforme.
4. **`verifier-destruction ID TEMOIN [LISTE]`** : lecture seule ; sans fichier, `vastai show instances --raw` (outil `VASTAI_BBIS` ou `vastai`) lu avec entrée nulle ; code non nul → « absence non prouvée », code 2 ; sinon `registre_bbis_v1 absence`. Jamais jugé par le code de la destruction. Conforme. Un ID vide passe le `case` de la couche shell (concaténation) mais est refusé en Python (`isdigit`) : sans conséquence.
5. **`exiger_absence`, `exiger_identifiant_a_detruire`, sous-commandes `identifiant` et `absence`, `registre_bbis_v1.py`** : preuve = liste lue (JSON valide, liste d'objets portant `id`, ou `{"instances": […]}`), témoin numérique ≠ ID **présent**, ID **absent** ; tout le reste → `GardeArret`. Échec fermé (liste vide → témoin absent → non prouvée). Les autres sessions restent permises comme témoins, refusées comme cibles (y compris dans `absence`). Conforme. Message de `garde_depense` : texte seul.
6. **Minuterie de l'amorce** : ne juge plus aucun code HTTP ; boucle `DELETE` toutes les 60 s tant que le processus vit ; après le 5e essai, un seul `PUT stopped`. Essai `test_minuterie_refait…` joue l'extrait réel avec un faux `curl` qui rend toujours 200 : 7 `DELETE`, 1 `PUT`, journal conforme, « return 0 » absent de l'extrait. Conforme. Échéance, jeton (`CONTAINER_API_KEY`), URL : inchangés.
7. **`fin_instance`** : texte du journal seul.
8. **`MIN_ESSAIS` 83 → 86** : voir plus haut (l'étape intermédiaire 84 de la v2 est écrite dans le commentaire).
9. **Essais** : `test_destruction_avec_y_et_absence_prouvee_contre_un_faux_outil` — faux `vastai` qui reproduit le défaut (sans `-y` : « Aborted. », code 0, rien détruit) : sain (ligne imprimée jouée telle quelle → détruit → « DESTRUCTION PROUVEE ») ; **cas du jour** (sans `-y` : code 0 mais code 2 à la vérification) ; artefacts (témoin absent, liste illisible, lecture en échec code 1, témoin = ID, liste sans `id`, forme `{"instances"}`, cinq autres sessions, `depense`). `tests/test_t07bbis_registre_v1.py` : attente de `detruire` mise à jour (5 lignes).
10. **Aucun changement de fond ailleurs** : le différentiel hors scripts, `registre_bbis_v1.py`, `marche_v1.py` (docstring) et tests est vide ; aucune ligne touchant graines, seuils de lecture, issues, coupure de 39,5 USD, jeton.

## Une ligne par hunk non expliqué

Aucun. Tous les hunks sont couverts par les points 1 à 9 ; entêtes de commentaires de l'amorce et de `registre_bbis_v1.py` = texte seul.

## Mineurs

- **m-D (minuterie : `stopped` coupe peut-être le processus)** : la demande « stopped » au 5e essai peut arrêter le conteneur, donc la minuterie, qui ne refera alors plus de `DELETE` ; c'est voulu (carte non facturée, stockage seul) mais la boucle « infinie » n'est infinie que tant que le conteneur tourne. La preuve reste celle de la session (déjà écrit au rapport v3 § 4). À savoir : une instance « stopped » non détruite reste facturée en stockage jusqu'à `detruire -y` + `verifier-destruction`.
- **m-E (témoin)** : sans autre instance du compte dans la liste, `verifier-destruction` ne peut jamais conclure (échec fermé) ; la mère doit avoir un témoin présent (par exemple une des cinq instances listées). Voulu ; à garder en tête, y compris pour la répétition à blanc.
- **m-F (forme de la liste réelle)** : la forme de `show instances --raw` n'est connue que par le faux outil ; réserve déjà écrite par le développeur (§ 4) ; l'échec est fermé (« illisible »), jamais un faux « prouvé ». À confirmer à la répétition à blanc.
- **m-G (liste d'autres sessions figée)** : au mot du 2026-11-14 ; déjà déclaré.
