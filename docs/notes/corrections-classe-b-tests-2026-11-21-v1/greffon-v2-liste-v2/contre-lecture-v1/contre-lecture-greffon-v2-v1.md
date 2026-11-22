# Contre-lecture du greffon des échecs connus v2 et de sa liste v2 (relecteur neuf, hostile, aveugle)

**Verdict : Conforme avec réserves.** Chaque garde revendiquée est rouge sur son artefact et verte sur son cas sain ; le greffon n'exempte que les 14 identifiants exacts listés. Trois réserves, aucune ne permet d'exempter ou masquer un essai hors liste : (R1) la garde R-A ne couvre que le « sauté en bloc », pas le « fichier joué sans aucun essai collecté » ; (R2) un marqueur `xfail` non strict propre à un essai listé neutralise le strict du greffon ; (R3) la liste n'est scellée que par un compagnon voisin, que rien d'extérieur ne fixe.

## Table des cas
Outil : `outils/epreuves.py` (essais synthétiques, un bac par cas) ; sortie complète : `tables/cas.tsv`. Code 4 = erreur d'usage de pytest (refus), 0 = vert, 1 = échec.

| Cas | Attendu | Rendu | Fichier d'essai |
|---|---|---|---|
| 1a ligne fantôme (faux) / 1b ligne vraie (vrai) | 4 / 0 | 4 / 0 | tests/test_a.py |
| 2a liste altérée après scellement (faux) / 2b intacte (vrai) | 4 / 0 | 4 / 0 | idem |
| 2d compagnon absent | 4 | 4 | idem |
| 3a doublon (faux) / 3b sans doublon (vrai) | 4 / 0 | 4 / 0 | idem |
| 4a fichier absent (faux) / 4b présent (vrai) | 4 / 0 | 4 / 0 | idem |
| 5a exempté qui passe (strict, faux) / 5b exempté qui échoue (vrai) | 1 / 0 | 1 / 0 | idem |
| 6a module sauté en bloc par `pytest.skip`, ligne listée (R-A, faux) | 4 | 4 | test_skipbloc.py |
| 6c idem par `importorskip` | 4 | 4 | test_importorskip.py |
| 6b même module sauté, non listé (vrai) | 0 | 0 | test_skipbloc.py |
| 6f / 6g R-A par dossier, par fichier seul | 4 / 4 | 4 / 4 | idem |
| 7a `--runxfail` (R-B, faux) / 7b sans (vrai) | 4 / 0 | 4 / 0 | test_a.py |
| 7c `PYTEST_ADDOPTS=--runxfail` ; 7d `--runxfail` sans essai collecté | 4 / 4 | 4 / 4 | idem |
| 8a `-k` désélectionne l'essai listé ; 8b `--deselect` | 0 / 0 (essai non joué, rien d'exempté de plus) | 0 / 0 | idem |
| 8c, 8d ligne fantôme + `-k` ou `--deselect` | 4 / 4 | 4 / 4 | idem |
| 9a passe ne collectant pas le fichier listé | 0 (non jugé, voulu) | 0 | test_b.py seul |
| 9b idem avec ligne fantôme | 0 (non jugé) | 0 | idem |
| 9c / 9d passe par identifiant d'un autre essai du fichier (ligne vraie / fantôme) | 0 / 4 | 0 / 4 | test_a.py::test_ok |
| 9e `--collect-only`, ligne fantôme | 4 | 4 | idem |
| 10a essai non listé qui échoue (`test_ko2`), voisin d'un listé | 1 | 1 | idem |
| 10b préfixe sans paramètre (`test_p` pour `test_p[1]`) | 4 | 4 | idem |
| 10g motif `*` ; 10h chemin hors `tests/` | 4 / 4 | 4 / 4 | idem |
| 2c liste ET compagnon altérés ensemble | (refus espéré, non promis) | 0, 2 xfailed | idem |
| **6d** fichier joué, aucun essai collecté (non sauté), ligne listée | 4 si même principe que R-A | **0**, ligne non jugée | test_vide.py |
| **6e** module marqué `skip` (`pytestmark`), ligne listée | non promis | 0, non signalé | test_marque_skip.py |
| **10e** essai listé qui passe, portant son propre `xfail(strict=False)` | 1 | **0** (1 xpassed) | test_xfail_propre.py |

Arbre réel (lecture seule, `outils/lance.sh`) : v11 + cibles v1 + v2 → 41 passed, 14 xfailed, aucun XPASS, code 0 ; mêmes fichiers avec `--runxfail` → code 4, message R-B. Comparaison par programme (`outils/comm_ids.sh`, `tables/ids-*.txt`) : les 10 identifiants v11 de la liste = les 10 `FAILED` v11 de `echecs-avec.txt` (0 en plus, 0 en moins) ; les 4 lignes v1 recopiées à l'identique (lignes entières).

Comparaison « sans la ligne » (`outils/compar.sh`, `tables/real-*.res`, `real-diff.txt`) : 7 fichiers réels (test_manifeste, test_prereg, test_scellement, test_garde_calcul, test_garde_google_v1, test_garde_refus_question_v1, test_run_factice) plus test_cibles_invisibles v1 et v2, dans deux copies à arbres identiques (copie sans `scripts/`, d'où 36 erreurs et 25 échecs, identiques dans les deux) : avec la ligne 25 failed, 110 passed, 1 skipped, 4 xfailed ; sans la ligne 29 failed, 110 passed, 1 skipped. La différence ligne à ligne est exactement les 4 essais cibles_invisibles listés (XFAIL contre FAILED) ; rien d'autre ne bouge.

## Trouvailles
- **R1 (réserve, bas).** Une ligne dont le fichier est joué mais où aucun essai n'est collecté (cas 6d : fichier sans fonction d'essai, ou essais conditionnels absents) n'est pas jugée : `modules` est bâti sur les essais présents. Même principe que R-A, non couvert ; effet : ligne périmée silencieuse, aucun essai masqué.
- **R2 (réserve, bas).** Le `xfail(strict=True)` du greffon est ajouté après les marqueurs de l'essai ; un `xfail` propre non strict est lu en premier, et un XPASS passe en code 0 (cas 10e). Ne touche que les identifiants listés.
- **R3 (réserve).** Liste et compagnon se changent ensemble sans refus (cas 2c) ; seule la revue du dépôt le retient. De même `tests/conftest.py` n'a pas de compagnon `.sha256` dans l'arbre (il en a un dans les pièces pour main). Même limite qu'en v1.
- De côté : la v1 (greffon et liste) reste dans l'arbre mais n'est plus chargée ; v11 ne se collecte pas sans `scripts/` (erreur de collecte, hors greffon).

## Relevé de méthode

**Chaîne de raisonnement.**
1. Pièces lues : `tests/greffon_echecs_connus_v2.py` (530c2d88e7a343d3…, empreinte recalculée identique à son compagnon), `tests/echecs-connus-v2.txt` (44b298298f70d5c7…, idem), `tests/conftest.py` (5fc78c9e5f487487…, sans compagnon dans l'arbre).
2. `diff` v1→v2 du greffon : ajouts seuls (ensemble `_SAUTES_EN_BLOC`, crochet `pytest_collectreport`, refus `runxfail`, branche `sautes`) ; `diff` des listes : 10 lignes v11 ajoutées, 4 lignes v1 intactes ; `git diff tests/conftest.py` : une ligne d'import. Conforme à ce qui est prétendu.
3. Comparaison par programme `comm` : 10 = 10, voir ci-dessus (`outils/comm_ids.sh`).
4. Seuls les identifiants exacts de `entrees` reçoivent un marqueur (lecture du code, `par_id[identifiant]`) ; confirmé par 10a et 10b (voisins et préfixes non exemptés) et par la comparaison « sans la ligne » (différence = 4 ids).
5. Chaque garde jouée sur objet faux et objet vrai (tableau) ; code et message rejoués.
6. Cas limites : 6d, 6e, 10e, 2c, voir trouvailles.

**Objets de contrôle.** Pour chaque garde : objet faux = artefact (ligne fantôme, liste altérée, doublon, fichier absent, exempté qui passe, module sauté listé, `--runxfail`), prévu rouge ; objet vrai = cas sain (ligne vraie, liste intacte, etc.), prévu vert. Rendu conforme dans les 14 couples du tableau. Pour R-A le contrôle vrai supplémentaire est 6b (même module sauté, non listé : vert). Aucun mécanisme n'a réussi là où sa conclusion était fausse, sauf aux cas 6d et 10e, signalés comme réserves.

**Premier pas non justifié.** Pas 5 pour la combinaison de plusieurs plugins ou `xdist` : non éprouvée (je n'ai joué qu'un processus) ; une passe `-n` pourrait répartir `_SAUTES_EN_BLOC` entre travailleurs. Ce qui le justifierait : une passe xdist sur un module sauté listé.

**Mode d'échec affecté.** Tenu, avec réserves R1 à R3. Pas visé : 5 (les gardes) ; preuve : `tables/cas.tsv`, `tables/real-diff.txt`. Le greffon ne peut ni exempter ni masquer autre chose que les 14 identifiants (pas 4 et comparaison « sans la ligne »).

**Trouvaille de côté.** Voir ci-dessus, trois lignes ; rien poursuivi. Je n'ai pas lu le rapport de l'auteur ni le relevé de la contre-lecture interrompue.

**Évaluateur et conseil.** Juge : pytest lui-même (code de sortie) sur mes essais synthétiques écrits avant les rendus, avec codes attendus fixés d'avance dans `epreuves.py`. Admission du juge : paires faux/vrai du tableau. Ce qui pourrait donner un bon jugement sans le mériter : mes essais synthétiques n'emploient ni l'environnement réel du dépôt (git, `scripts/`) ni plusieurs plugins ; deux attentes marquées « ? » (2c, 6d) l'étaient parce que je ne savais pas d'avance.

## Écarts à ma consigne
Aucun refus rencontré. Cas 6d/6e/10f relancés après avoir corrigé mes propres arguments d'essai (premiers rendus pollués par des échecs de `test_a.py`) ; les copies `bac/` et `bac-sans/` sont retirées.
