# Contre-lecture du greffon des échecs connus — v1

**Verdict : Conforme**, avec deux réserves mineures (R-A : un module d'essais sauté en bloc échappe au contrôle de ligne fantôme ; R-B : l'option `--runxfail` neutralise l'échec attendu strict). Aucune des trois questions de la mère n'est cassée dans l'usage normal.

- Contre-lecteur neuf, hostile, aveugle aux autres relectures. Pièces lues : `tests/greffon_echecs_connus_v1.py`, `tests/echecs-connus-v1.txt` et son compagnon, `tests/conftest.py` (différentiel contre `origin/main` : une seule ligne d'import ajoutée), branche `lot/compte-organisme-v1`, commit `5e26d5dd1`.
- Empreintes vérifiées sur le dépôt réel : `sha256sum -c` rend OK pour `echecs-connus-v1.txt` (`c73a3310…47c1`) et pour `greffon_echecs_connus_v1.py`.
- Travail sur copie partielle (`git archive HEAD tests src scripts pyproject.toml`) dans `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-greffon/` : `copie/` intacte, `copie-m/` pour les artefacts. Suite entière jamais jouée.
- Conséquence de la copie partielle : le dossier `docs/` manque, donc beaucoup d'essais des fichiers `test_cibles_invisibles_v*.py` échouent dans la copie pour une cause étrangère (index d'invites absent). C'est utile : ces échecs non listés restent des échecs, ce qui prouve la non-exemption. Les deux essais listés de chaque fichier échouent dans la copie pour la raison même que dit la liste (constructeurs d'invite non examinés ; lecteurs de `cibles` non admis), constatée dans la sortie sous `--runxfail`.

## Les trois questions

| Question | Résultat | Pas visé et preuve |
|---|---|---|
| 1. N'exempte que les quatre identifiants exacts, sans effet de bord | **Tenu** | Passages 1, 2, 3, 9, 10 de la chaîne ci-dessous |
| 2. Échoue s'il manque un essai nommé ou si un exempté passe | **Tenu** (usage normal), deux réserves | Passages 4 à 8 ; réserves R-A (passage 13) et R-B (passage 14) |
| 3. Ne touche rien d'autre | **Tenu** | Passages 11 et 12 ; recherche de crochets (passage 12) |

## Relevé de méthode

### Chaîne de raisonnement

Commande de base de tous les passages (sauf indication) : `env -C <copie> TMPDIR=<mon dossier> PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider …`. Le `pyproject.toml` fixe `pythonpath = ["src", "tests"]`, donc l'import du greffon dans `conftest.py` marche sans `PYTHONPATH` et en mode d'import par défaut.

1. Les quatre essais listés, joués ensemble (`tests/test_cibles_invisibles_v1.py tests/test_cibles_invisibles_v2.py`, `copie/`) : quatre `XFAIL`, exactement les quatre identifiants de la liste ; 24 `FAILED` voisins non listés restent en échec (24 failed, 14 passed, 4 xfailed). Le greffon n'exempte donc pas par fichier.
2. Même nom dans un autre fichier : `tests/test_cibles_invisibles_v3.py` porte les deux mêmes noms d'essai. Joué avec `-k "inventaire_tout or ne_lit_la_cle or scellement"` : les deux essais du v3 `PASSED`, non marqués ; seuls v1 et v2 `XFAIL` (`-k test_inventaire_tout_constructeur_d_invite_est_examine` sur v1, v2, v3 : 2 xfailed, 1 passed). L'exemption porte sur le chemin complet, pas sur le nom.
3. Collecte restreinte `fichier::essai` : `tests/test_cibles_invisibles_v1.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles` seul : 1 `XFAIL`, aucune erreur sur les trois autres lignes (fichier ou essai non collecté : non jugé, par conception, ligne 14 du greffon).
4. Altération de la liste sans resceller (`copie-m/`) : code 4, `liste des échecs connus refusée … empreinte b804bccbd2e0… ≠ scellée c73a3310ce52…`, aucun essai joué, même sur un fichier étranger à la liste.
5. Essai exempté qui passe (ligne `tests/test_scellement.py::test_sain_sceller_puis_verifier`, resscellée) : `1 failed, 6 passed`, message `[XPASS(strict)] échec connu`. Code 1.
6. Ligne fantôme, essai renommé, fichier joué avec `fichier::essai` restreint, puis avec `-k absent` : code 4, `aucun essai collecté de ce nom`. La re-collecte du module (lignes 62 à 70, 86 à 89 du greffon) voit les essais que la restriction a écartés. Même ligne fantôme, mais seul un autre fichier joué (`tests/test_manifeste.py`) : 11 passés, non jugée (conception documentée).
7. Fichier absent (`tests/test_absent_v9.py::test_x`) : code 4, `fichier absent`, refus même quand le fichier n'est pas joué (le test d'existence est global, ligne 84).
8. Caractère de motif (`…::test_artefact_*`) : code 4, `caractère de motif`. Identifiant de classe seule (`tests/test_garde_refus_question_v2.py::TestCasSain`) : code 4, aucun essai de ce nom (un nœud classe n'est pas un `pytest.Item`). Ligne mal formée (quatre champs) : refus `trois champs non vides`.
9. Classe, méthode exacte (`…::TestCasSain::test_accepte`, v2), jouée avec le v1 qui a aussi une classe `TestCasSain` : un seul `FAILED` (le `XPASS(strict)` de la méthode du v2), les 11 autres passent, y compris les huit de `TestCasSain` du v1.
10. Essai paramétré, exemption d'un seul paramètre (`…test_aucune_invite_ne_porte_les_cibles[agent_p3]`) : `1 xfailed`, les 5 autres paramètres `FAILED`. Ni préfixe ni nom sans crochets ne sont acceptés.
11. Deux fichiers hors liste joués avec et sans la ligne d'import (`tests/test_scellement.py`, `tests/test_manifeste.py`, `tests/test_prereg.py`, `tests/test_cibles_invisibles_v3.py`, plus 19 essais du v1 hors liste ; 68 essais retenus par `-k`) : mêmes résultats par essai, avec la ligne (`copie/`) comme sans (`copie-m/`, ligne retirée) : 24 failed, 44 passed, 2 deselected, même ordre. Le greffon voit les deux essais listés avant la sélection `-k` (il passe en premier) et n'y change rien.
12. Crochets : `grep` de `pytest_collection_modifyitems|pytest_collection_finish|pytest_runtest_makereport|pytest_configure` sur `tests/`, `src/`, `scripts/` : seuls `tests/greffon_echecs_connus_v1.py` et la ligne d'import de `tests/conftest.py`. Un seul `conftest.py` dans le dépôt. `conftest.py` ne définit que des fixtures (`depot`, `_signal_term_efface`), aucune n'est masquée. Le greffon s'enregistre en plus des crochets des greffons de pytest (pluggy appelle toutes les implémentations ; `tryfirst` seulement l'ordre).
13. Réserve R-A, module sauté en bloc : `pytest.skip(…, allow_module_level=True)` ajouté en tête de `copie-m/tests/test_cibles_invisibles_v2.py` : `1 skipped`, aucune erreur du greffon, alors que deux lignes de la liste désignent ce fichier. Le module saute avant toute collecte d'essai, il n'entre pas dans `modules`, donc ses lignes ne sont pas jugées (le greffon ne le dit pas : sa docstring ne promet que « fichier absent » et « essai renommé »). Visible comme un saut dans le résumé, jamais comme un échec.
14. Réserve R-B, `--runxfail` : avec la ligne P1 (essai qui passe), `--runxfail` rend `7 passed` : l'échec attendu strict est désarmé. Les deux essais listés du v1 joués avec `--runxfail` : `2 failed` (non masqués : le côté sûr tient). Il faut passer l'option à la main ; ce n'est pas le défaut.
15. Aucune de ces expériences n'a dépendu d'une lecture de résultat de la mère ni d'une clé ; aucune dépense, aucun appel externe.

### Objets de contrôle

Mécanisme éprouvé : le greffon (liste scellée, exemption stricte, refus de lignes fantômes).

- Objet où la conclusion « le greffon ne ferait rien d'illégitime » est fausse par construction : une ligne qui désigne un essai sain (`test_sain_sceller_puis_verifier`), une ligne fantôme, une ligne de fichier absent, un motif, une classe seule, une liste altérée. Prédit d'avance : refus ou échec dans chaque cas. Rendu : refus code 4 (altération, fantôme, absent, motif, classe seule, mal formée) ou échec code 1 (essai sain exempté) ; tous conformes à la prédiction.
- Objet où c'est vrai par construction : les quatre lignes de la liste telle que livrée, sur des essais qui échouent réellement ; le v3 (mêmes noms, essais sains) ; trois fichiers sains. Prédit : quatre `XFAIL` ; v3 inchangé ; résultats identiques avec et sans l'import. Rendu : conforme.
- Prédictions écrites avant chaque passage ; résultats après. Un écart de ma part : un premier jeu de la ligne « classe seule » avait quatre champs (faute de ma manipulation de la liste), refusé pour mise en forme et non pour la raison visée ; je l'ai refait proprement (passage 8).
- Artefacts à moi, six, tous prédits : (a) liste altérée sans resceller, (b) essai sain exempté, (c) ligne fantôme sous collecte restreinte, (d) fichier absent, (e) motif, classe seule, paramètre unique, méthode de classe exacte, (f) module sauté en bloc, plus (g) `--runxfail`. Cassés par mon attaque (au sens où le greffon ne réagit pas) : (f) et (g) seulement.

### Premier pas non justifié

Le passage 11, pour la partie « aucun changement de résultat » : je l'ai établi sur 68 essais choisis, non sur la suite entière, que je n'ai pas le droit de jouer ; le raisonnement qui généralise est le passage 12 (pas d'autre crochet) et la lecture du code (le greffon ne marque que les identifiants de la liste). Ce qui le justifierait pleinement : une passe complète de la suite avec et sans la ligne, comparée essai par essai (la mère l'a faite : « 90 passés et 4 échecs attendus », message de commit, non rejoué ici).

### Mode d'échec affecté

Trois questions de la mère, rendues ci-dessus : (1) tenu, (2) tenu avec réserves R-A et R-B, (3) tenu. Pas visé de chaque question : passages 2, 9 et 10 ; 4 à 8, 13 et 14 ; 11 et 12.

### Trouvaille de côté

- Le compagnon de la liste garantit l'intégrité, pas l'autorité : qui réécrit la liste et son compagnon d'un coup (comme je l'ai fait en copie) étend l'exemption sans bruit. La garde de revue du dépôt (`verifier-arbre`, relecture de la mère) est le seul rempart ; cela n'est pas un défaut du greffon.
- Le greffon, lui, n'a pas de compagnon vérifié à l'exécution (le `.sha256` existe et est correct, mais seul `verifier-arbre` le lit).
- Je n'ai pas vérifié si `tests/` est dans `DOSSIERS_SCELLES` ; non poursuivi.

### Évaluateur et conseil

Ce qui juge mon produit : mes artefacts prédits et la sortie de pytest. Les témoins sont la liste livrée (quatre échecs réels), le v3 et trois fichiers sains. Mon produit pourrait paraître bon sans le mériter parce que la copie partielle n'a pas `docs/` : les essais listés échouent dans la copie pour les motifs écrits, mais je n'ai pas joué les quatre dans le dépôt complet avec `git`. Conseil de correction, non bloquant : (R-A) refuser une ligne dont le fichier est présent sur disque, joué, mais dont le module n'a produit aucun essai collecté (saut ou rapport de collecte sans essai) ; (R-B) soit un `pytest_configure` du greffon qui refuse `--runxfail`, soit le dire dans la docstring. Le verdict de porte reste à un sous-agent neuf et à Lazar.
