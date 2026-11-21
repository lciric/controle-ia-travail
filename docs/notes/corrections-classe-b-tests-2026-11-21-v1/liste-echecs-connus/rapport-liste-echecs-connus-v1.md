# Liste des échecs connus de la suite d'essais — rapport v1

- **Nature** : pièce de travail d'un développeur neuf (modèle O), le 21 novembre 2026, sur mandat de la mère (décision vers 21:24Z ; GO-2026-11-21-74). Rien n'est écrit dans le dépôt principal, aucun commit, aucun fournisseur appelé, aucune clé lue, aucune dépense.
- **Verdict** : mécanisme prêt à verser. Sous l'interpréteur de l'environnement virtuel, les quatre essais du tri rendent « xfailed » (38 passés, 4 xfailed, code 0) ; les cinq artefacts se comportent comme prévu ; v3 et v4 rendent la même chose avec et sans le greffon. Sous `/usr/local/bin/python3`, v1 et v2 (et v3) ne se collectent pas, avec ou sans le greffon (`torch` absent) : le mécanisme y a été éprouvé sur un fichier témoin.

## 1. Configuration actuelle et voie prise

- `tests/conftest.py` existe (`a1bbfcc9…aedca5`), **sans** compagnon `.sha256` : non scellé, modifiable.
- `pyproject.toml` : `[tool.pytest.ini_options]` avec `pythonpath = ["src", "tests"]` et `testpaths = ["tests"]` ; pas de `pytest.ini`, `setup.cfg`, `tox.ini`, ni de `conftest.py` à la racine.
- **Voie** : un module de greffon neuf, `tests/greffon_echecs_connus_v1.py`, chargé par **une ligne ajoutée** à `tests/conftest.py` (import du crochet `pytest_collection_modifyitems`, que pytest découvre sur le module conftest). Écartés : `pytest_plugins` dans `tests/conftest.py` (refusé par pytest dans un conftest qui n'est pas à la racine) ; `-p greffon…` dans `addopts` (les greffons `-p` se chargent avant l'insertion de `pythonpath`, le module ne serait pas trouvé sans `PYTHONPATH=tests`).

## 2. Fichiers neufs ou modifiés (chemin cible dans le dépôt)

| chemin cible | état | empreinte (SHA-256) | pièce dans mon dossier |
|---|---|---|---|
| `tests/echecs-connus-v1.txt` | neuf, scellé | `c73a3310ce52698095bcb2a9923c5b239652f1dc7ef32eee90f1e453fd9b47c1` | `livrables/tests/echecs-connus-v1.txt` |
| `tests/echecs-connus-v1.txt.sha256` | neuf (compagnon lu par le greffon : il fait partie du mécanisme) | — | `livrables/tests/echecs-connus-v1.txt.sha256` |
| `tests/greffon_echecs_connus_v1.py` | neuf | `53b9b9ee3c13b40d02baddeb9b8eb3cd691dd91df54649b4f07b1916d48f4925` | `livrables/tests/greffon_echecs_connus_v1.py` |
| `tests/conftest.py` | modifié, une ligne ajoutée | `1573fcfe…11bb2fc` (avant : `a1bbfcc9…aedca5`) | `livrables/tests/conftest.py` ; différentiel `livrables/differentiel-conftest-v1.diff` (`c30abb4f…6ac38c`) |

Différentiel de `tests/conftest.py` (seule modification d'un fichier existant) :

```
 import pytest
+from greffon_echecs_connus_v1 import pytest_collection_modifyitems  # noqa: F401 — liste des échecs connus (décision de la mère, 21 novembre 2026)
```

**Les quatre lignes de la liste** (identifiants rejoués, sous `.venv`, sur la copie partielle ; ils sont exactement ceux du tri, `9957b178…ddc8`, ligne « Inventaire des cibles invisibles ») :

- `tests/test_cibles_invisibles_v1.py::test_inventaire_tout_constructeur_d_invite_est_examine`
- `tests/test_cibles_invisibles_v1.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles`
- `tests/test_cibles_invisibles_v2.py::test_inventaire_tout_constructeur_d_invite_est_examine`
- `tests/test_cibles_invisibles_v2.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles`

Chacune porte un motif en une phrase et la référence « décision de la mère du 21 novembre 2026, vers 21:24Z ; tri `registres/essaim/vers-mere/annexe-tests-complets-2026-11-21-v1/tri-echecs-tests-complets-2026-11-21-v1.md` ». Format : trois champs séparés par une tabulation ; `#` en tête de ligne pour les commentaires.

**Ce que fait le greffon** : (a) vérifie la liste contre son compagnon `.sha256` (par `controle_ia.scellement.verifier`), refus sinon ; (b) refuse une ligne mal formée, en double, hors de `tests/….py::…`, ou portant `*` ou `?` ; (c) refuse une ligne dont le fichier n'existe pas ; (d) refuse une ligne dont le fichier est joué dans la passe mais dont l'identifiant ne correspond à aucun essai de ce fichier (re-collecte du module quand la passe est restreinte, pour ne pas refuser à tort `pytest fichier::essai`) ; (e) marque chaque essai listé `xfail(strict=True)`, motif et référence dans la raison. Un refus sort par `pytest.UsageError` : code 4, message « ERROR: liste des échecs connus … ». Le crochet est `tryfirst`, donc il voit les essais avant la désélection par `-k` ou `--deselect`.

**À faire au versement** (par la mère, non fait ici) : copier les trois fichiers neufs et la ligne de `conftest.py` ; le compagnon de la liste est déjà celui de `livrables/tests/echecs-connus-v1.txt.sha256`. Toute modification de la liste passe par une `echecs-connus-v2.txt` scellée et par le changement de la constante `LISTE` du greffon (R12).

## 3. Épreuves

Copie partielle : `git archive HEAD` de `scripts/`, `tests/`, `src/`, `pyproject.toml`, `docs/sources/invites-2606.08892-v1/` et `docs/sources/invites-2606.07054-v1/` (lus par `charger_invite` et `trace_lite`), branche `lot/compte-organisme-v1`, arbre propre. Commandes : `jouer.sh`, `preparer.sh`, `epreuves.sh` de mon dossier (`PYTHONPATH=src`, `TMPDIR` dans mon dossier, `-p no:cacheprovider`, `-B`) ; sorties dans `journaux/`. pytest 9.1.1 sous les deux interpréteurs. Fichier témoin (jamais versé) : `epreuves/test_temoin_echecs_connus_v1.py`, avec `test_echoue` (échoue), `test_passe` (passe), `test_param[1]` (passe), `test_param[2]` (échoue). Listes d'épreuve : `epreuves/listes/S0.txt` à `S5.txt` (S6 = S0 modifiée après scellement).

| épreuve | prédiction | `.venv/bin/python` (v1, v2, témoin) | `/usr/local/bin/python3` (témoin seul) |
|---|---|---|---|
| Sain, liste livrée, v1 et v2 | 4 xfailed, aucun échec | 38 passés, 4 xfailed, code 0 | v1 et v2 : 2 erreurs de collecte (`torch` absent), code 2 — identique sans greffon |
| S0 sain, liste + témoin | 6 xfailed (témoin : 2) | 40 passés, 6 xfailed, code 0 | 2 passés, 2 xfailed, code 0 |
| S1 ligne fantôme (fichier présent, essai ou paramètre inexistant) | refus | refus code 4, les deux lignes nommées | refus code 4 (`test_param[3]` ; la ligne v1 n'est pas jugée, v1 hors de la passe) |
| S2 ligne fantôme, fichier absent | refus | refus code 4 | refus code 4 |
| S3 essai listé qui passe (strict) | échec « XPASS(strict) » | 2 échecs : `v1::test_inventaire_registre_a_jour` et `témoin::test_passe`, « [XPASS(strict)] échec connu … », code 1 | 1 échec `test_passe` XPASS(strict), code 1 |
| S4 échec hors liste (une ligne v2 et `test_echoue` retirées) | ces deux-là restent des échecs | 2 échecs : `v2::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles`, `témoin::test_echoue` ; 4 xfailed, code 1 | 1 échec `test_echoue`, 1 xfailed, code 1 |
| S5 ligne à motif `test_param[*]` | refus | refus code 4 | refus code 4 |
| S6 liste modifiée après scellement | refus | refus code 4 (« empreinte … ≠ scellée … ») | refus code 4 |
| Passe restreinte `fichier::essai`, liste S0 | pas de refus à tort | 2 passés, code 0 | 1 passé, code 0 |
| Passe restreinte, liste S1 | refus (re-collecte) | refus code 4 | refus code 4 |
| `-k`, liste S0 | pas de refus | 3 passés, 43 désélectionnés, code 0 | 1 passé, 3 désélectionnés, code 0 |
| v3 et v4 avec le greffon (liste livrée) | comme sans | 39 passés, code 0 | 1 erreur de collecte (v3, `torch`), code 2 |
| v3 et v4 sans le greffon (conftest d'origine) | — | 39 passés, code 0 | 1 erreur de collecte (v3, `torch`), code 2 |
| v1 et v2 sans le greffon | 4 échecs | 4 échecs, 38 passés, code 1 | 2 erreurs de collecte, code 2 |
| Témoin sans le greffon | 2 échecs | 2 échecs, 2 passés, code 1 | 2 échecs, 2 passés, code 1 |

## 4. Écarts

- Sous `/usr/local/bin/python3`, v1, v2 et v3 ne se collectent pas (`ModuleNotFoundError: torch`, via `controle_ia.environnements.lancer_pilote_a`), avec ou sans le greffon : le cas sain « xfailed » n'y est pas observable. Le mécanisme y est éprouvé sur le témoin. Conséquence de conception : un fichier qui échoue à la collecte ne produit aucun essai, et ses lignes ne sont pas jugées (l'erreur de collecte, elle, fait déjà échouer la suite).
- Une ligne dont le fichier n'est pas joué dans la passe n'est pas jugée (sauf si le fichier n'existe pas) : choix délibéré pour ne pas refuser les passes partielles (amorces T0.6 qui jouent une liste de fichiers, par exemple).
- J'ai ajouté deux refus non demandés mais conformes à la demande « identifiants exacts » et à R6 : liste non scellée ou altérée, ligne en double.
- Une recherche (outil Grep) a eu une sortie trop longue, versée d'office par le harnais sous `/root/.claude/projects/…/tool-results/` ; je ne l'ai pas lue, j'ai relancé une recherche étroite.
- J'ai écrit trois petits scripts bash (`jouer.sh`, `preparer.sh`, `epreuves.sh`) dans mon dossier, exécutés comme fichiers, pour éviter des commandes enchaînées ; aucun code en ligne passé à un interpréteur.
- Copies d'épreuve et dossier temporaire effacés après les épreuves ; la copie partielle aussi (se refait par deux `git archive` comme au § 3).

## Relevé de méthode

### Chaîne de raisonnement

1. `tests/conftest.py` n'a pas de compagnon `.sha256` (`ls`, erreur « No such file » sur le compagnon) ; `pyproject.toml` porte la configuration pytest, `pythonpath = ["src", "tests"]` (lu).
2. `pytest_plugins` est refusé dans un conftest qui n'est pas à la racine du dépôt — supposé (comportement documenté de pytest, non rejoué ici) ; d'où l'import du crochet dans `tests/conftest.py`.
3. Les quatre échecs de v1 et v2 sont ceux du tri (`9957b178…ddc8`) : rejoués sous `.venv` sur la copie, « 4 failed, 38 passed », identifiants listés au § 2 (journal `v1v2-sans-venv.txt`).
4. Sous `.venv`, avec la liste livrée : « 38 passed, 4 xfailed », code 0 (rejoué à la main, sortie au § 3).
5. Sous `/usr/local/bin/python3`, v1 et v2 rendent deux erreurs de collecte `torch`, avant et après l'ajout du greffon (journaux `v1v2-sans-sys.txt` et rejeu à la main) : le greffon n'y change rien.
6. Le refus des lignes fantômes, à motif, en double, de fichier absent, de liste altérée : S1, S2, S5, S6, sous les deux interpréteurs (journaux `S1-*`, `S2-*`, `S5-*`, `S6-*`).
7. Le caractère strict : S3, « [XPASS(strict)] » et échec nommé, sous les deux interpréteurs.
8. L'échec hors liste reste un échec : S4, sous les deux interpréteurs.
9. Les passes restreintes et `-k` ne sont pas refusées à tort, la ligne fantôme l'est encore en passe restreinte (journaux `S0-restreint-*`, `S1-restreint-*`, `S0-k-*`).
10. v3 et v4 : 39 passés avec et sans greffon sous `.venv` ; même erreur de collecte avec et sans sous l'interpréteur système (journaux `v3v4-*`).
11. Aucun autre essai du dépôt ne lit `tests/conftest.py` ni d'autres fichiers de `tests/` que `test_*.py` (recherche étroite : seuls `test_t06_v11/12/13_liste.py`, qui filtrent `test_*.py`) ; donc les deux fichiers neufs, qui ne portent pas ce préfixe, ne changent pas les listes figées de T0.6.

### Objets de contrôle

- **Mécanisme : l'exemption marque les seuls essais listés, en strict.** Objet faux par construction : un essai listé qui passe (S3) ; prédit : la suite échoue et le dit ; rendu : échec « XPASS(strict) » nommé, code 1, sous les deux interpréteurs. Objet vrai : les quatre échecs réels listés ; prédit : « xfailed » ; rendu : 4 xfailed sous `.venv` (non observable sous l'interpréteur système, § 4).
- **Mécanisme : aucune exemption hors liste.** Objet faux : un échec retiré de la liste (S4) ; prédit : échec ; rendu : échec, sous les deux interpréteurs.
- **Garde : refus d'une ligne sans essai.** Artefact : lignes fantômes (S1, S2, et en passe restreinte) ; prédit : refus ; rendu : code 4. Cas sain : liste S0 et passes restreintes saines ; prédit : pas de refus ; rendu : code 0.
- **Garde : scellé de la liste.** Artefact : S6 ; rendu : refus. Cas sain : S0 ; rendu : accepté.

### Premier pas non justifié

Le pas 2 : le refus de `pytest_plugins` hors de la racine n'a pas été rejoué ici ; il justifie seulement le choix de la voie, non le fonctionnement, qui est montré aux pas 4 à 10. Ce qui le justifierait : une épreuve avec `pytest_plugins` dans `tests/conftest.py` d'une copie.

### Trouvaille de côté

- L'interpréteur système de ce conteneur n'a pas `torch` : toute la famille des cibles invisibles v1 à v3 y est injouable ; seul `.venv` la joue. Cela croise le § 1 du tri (où l'interpréteur système était la voie saine pour l'épinglage) : aucun interpréteur ne joue ici toute la suite sans échec.
- `test_cibles_invisibles_v2.py` n'a pas de compagnon `.sha256`, contrairement à v1, v3 et v4 (vu dans `ls tests/`).

### Évaluateur et conseil

Juge : pytest 9.1.1 lui-même (compte des états et code de sortie), sur les deux interpréteurs ; témoins admis : le fichier témoin, dont l'état de chaque essai est fixé par construction et vérifié sans greffon (« 2 failed, 2 passed »), et les quatre échecs réels vus sans greffon. Par où ce produit pourrait sembler juste sans l'être : une ligne d'un fichier qui ne se collecte pas, ou qui n'est pas joué dans la passe, n'est jamais jugée (§ 4) ; un essai listé qui se mettrait à échouer **pour une autre cause** resterait « xfailed » (le marqueur ne vérifie pas le motif de l'échec ; `raises=` ne distinguerait pas ici, les deux essais lèvent `AssertionError`).
