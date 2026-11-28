# Notes d'intégration — code du plan B des juges (T0.5), v1

- Date : 2026-10-20 (UTC). Agent d'intégration (workflow `plan-b-code-v1`, phase « Intégration »), en routine sur processeur.
- Clone : `plan-b-code/depot`, branche locale `travail/plan-b-v1`, tête `cb14316` ; aucun commit, aucune poussée ; dépôt principal non touché ; aucun service payant, aucun modèle réel.
- Texte suivi : `plan-b-juges/T0.5-plan-B-juges-v1-brouillon3.md` (sha256 `8747ea81…`), notes de conception v1, décision R-225.

## Verdict

Le code des trois agents s'intègre : 281 tests du plan B passent, ainsi que 203 tests des modules gelés réutilisés. Une incohérence de fond a été trouvée et corrigée : **le lecteur ne lisait pas le format des fichiers qu'écrit le lanceur** (aucune clé commune hors des noms de fichiers). Le lecteur lit désormais le format du lanceur ; un test neuf le prouve sur les fichiers d'un vrai run jouet du lanceur. Aucun module gelé n'a changé ; aucun test n'a été affaibli.

## 1. Fichiers neufs (tous non suivis ; empreintes après intégration)

| fichier | lignes | sha256 | auteur | touché par l'intégration |
|---|---|---|---|---|
| `docs/sources/invites-plan-b-v1/invites/RS1.txt` (+ `.sha256`) | 58 | `b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7` | RS1 | non |
| `docs/sources/invites-plan-b-v1/index.json` (+ `.sha256`) | 32 | `c61df3db8efce13295f9ba0cd1fb005fe8a1ef235d6977eacf004926ceeb4bda` | RS1 | non |
| `docs/sources/invites-plan-b-v1/LISEZMOI.md` (+ `.sha256`) | 56 | `00e6011e40da28b616a110a914a7cf8f93a103f7c05637d2f1f593599b2fc49f` | RS1 | non |
| `src/controle_ia/environnements/rubrique_simplifiee.py` | 187 | `2859c2977592f03f741f59e1c85d3d19f9231f40cd590963134c8307b640bcfe` | RS1 | non |
| `src/controle_ia/environnements/juges_simplifies.py` | 176 | `01a4e0c448e92dec32a551e6f401c7e9109235e3d44e68f5a1ea1570744c8262` | juges+lanceur | non |
| `src/controle_ia/environnements/requalifier_juges.py` | 1 303 | `bf7184ba55fdedf301dc3083aefd75835de164e4c28885d4140a4b429ca14680` | juges+lanceur | docstring seulement (avant : `325b2219…`) |
| `src/controle_ia/environnements/lire_requalification.py` | 1 013 | `8f4f03bd50f3c61ea8fed8aed2f8962b2d091709f6eeff2558358fa47a1b5844` | lecteur | oui (avant : `bdc970f0…`) |
| `tests/test_plan_b_rubrique_simplifiee.py` | 372 | `b1fdb00c8a138366683406b9f6c5f19223ab38db6f9a61d90e8dc3d463232292` | RS1 | non |
| `tests/test_plan_b_juges_simplifies.py` | 229 | `403e1461def54354dbd06f6e5b926f5e046c396e2d49d63cb25719e68e609d50` | juges+lanceur | non |
| `tests/test_plan_b_requalifier.py` | 1 232 | `39c854a0508fc4abd042188d15dcf5c12b8dfe32243518b9d655368eaeca8e3d` | juges+lanceur | configuration réelle sortie dans `_config_reelle()` (avant : `53b4fd9b…`) |
| `tests/test_plan_b_lecteur.py` | 1 222 | `5c18feeb7ff0e7f05355e48295595f95d9a4e90db844c341e799cf900d260e68` | lecteur | oui (avant : `0a3e3d82…`) |
| `tests/test_plan_b_integration.py` | 137 | `399ed7ff6ee115f357acf1657df88905cfd8b4b78b92d3799d557ca8c7b8488e` | intégration | neuf |

Copies d'avant l'intégration (pour la relecture des différences) : `plan-b-code/integration/originaux/`.

## 2. Incohérence trouvée et corrigée : format des fichiers du run

Le lecteur avait été écrit en parallèle, sur un format inventé (le texte ne fixe que les noms des fichiers). Écarts constatés, lanceur → lecteur d'avant :

| fichier | le lanceur écrit | le lecteur lisait |
|---|---|---|
| `resume.json` / `arret.json` | `fichiers[<fichier>]` = « écrit », « en cours », « échu » (et `phases` par phase, deux fichiers par rejeu) | `phases[<fichier>].statut` |
| `notations-RS1-<J>-decisives.json` | `garde.rapports` : rapport de rangée aplati (`rapport_de_la_rangee`) avec `cle` | rapport brut de `jouer_episodes` (clé « 0,0 », `episode`) |
| `rejeu-<J>-demi.json` | rangée : `garde`, `jetons_generes`, `tronquee`, `reponse_sha256`, `reproduction` = booléens | `rapport` ; `reproduction` = valeurs |
| `rejeu-<J>-simple.json` | `reglages_relus` ; `repere.par_couche`, `repere.par_rangee` (liste) ; `ancrage.par_couche` ; `chemin.rangees` ; `d1.rangees` | `reglages_effectifs` ; `repere.global`, `par_rangee` (dictionnaire) ; `ancrage.max` ; `chemin` et `d1` en listes |
| `temoins.json` | `juges[<J>].appels[…]` (statut « fait » ou « témoin impossible ») et `taux_h4` | `[<J>].rangees` et `[<J>].impossible` |

Correction (le lecteur s'aligne sur le lanceur ; le lanceur, qui produit les données et dont les tests jouent un vrai run, garde son format) :
- `lire_requalification.py` : `rapport_de_jouer_episodes` remet le rapport d'une rangée sous la forme de `jouer_episodes` (aucune valeur recalculée ; clé absente : arrêt) ; le reste du lecteur appelle toujours les fonctions gelées sur cette forme. Statuts lus dans `fichiers` ; nom de fichier ou statut inconnu : arrêt (non lisible). Clés du rejeu et du témoin renommées comme ci-dessus.
- Gardes neuves de cohérence lanceur-lecteur, chacune avec cas sain et artefact : noms des juges du run égaux à ceux du lecteur (ils font les noms des fichiers et des clés) ; `CONSTANTES_CONFIG` étendu à `couverture_jetons`, `couverture_unite` et `controle_intervalles` (mêmes séparateurs que `rubrique_simplifiee`) ; lecture RS1 recalculée comparée aussi à `complete_sans_troncature` et `lecture_rs1` consignés ; reproduction recalculée égale à celle consignée par le lanceur ; taux H.4 du témoin consigné égal au taux recalculé ; `repere.par_rangee` en liste, sans doublon.
- `fichiers_de_phase(juges)` : noms des fichiers de phase, partagés par la constante `FICHIERS` et par le test d'intégration.
- `test_plan_b_lecteur.py` : les fichiers synthétiques sont faits au format du lanceur, par ses propres fonctions (`rapport_de_la_rangee`, `_rangee`, `reproduction`). Toutes les assertions d'avant sont gardées ; la garde « deux comparaisons dans un rapport », devenue impossible au format du lanceur, reste éprouvée sur `_comparaison` directement. +7 cas (artefacts neufs).
- `requalifier_juges.py` : docstring seulement. Ses fonctions de bilan ne sont **pas** partagées avec la lecture, contrairement à ce qu'elle disait ; elles sont décrites comme un second calcul, comparé à la lecture par `test_plan_b_integration.py`, avec l'écart NaN connu (question I-1).
- `test_plan_b_integration.py` (neuf, 4 tests) : constantes communes (modules gelés, commit, réglages, unité, séparateurs, clé « 0,0 », noms des fichiers) et configuration réelle du texte acceptée des deux côtés (artefacts : un seuil que le lanceur accepte et que le lecteur refuse) ; aller et retour du rapport de rangée ; fonctions pures égales des deux côtés sur une grille (règle k, queues binomiales, classement des dépassements) ; **le lecteur lit les fichiers d'un vrai run jouet du lanceur** (issue, sceaux, lecture RS1 recalculée, seuils de couverture, garde en ligne, deux paliers, contrôles négatif et positif, couverture, reproduction, témoin) et ses lectures égalent celles du second calcul du lanceur. Sur ce run jouet, sur cette machine : chemin « fidèle » (D1 vu, couverture atteinte au bord : 8 jetons générés, 7 positions générées comparées), production « non concluant », reproduction 4 rangées sur 4, garde en ligne sans rangée comparable (réponses RS1 courtes).

Imports croisés vérifiés : `requalifier_juges` → `juges_simplifies`, `rubrique_simplifiee` ; `lire_requalification` → `rubrique_simplifiee`, `juges_simplifies.CLE_ACTION`, `pilote_a.CLES_RAPPORT_GARDEES` ; clés des notations `juge-RS1-<J>/…` et graines de la lecture identiques des deux côtés ; commande de lecture du texte égale à l'interface du lecteur.

## 3. Tests

| fichier | fonctions | cas | avant l'intégration |
|---|---|---|---|
| `test_plan_b_rubrique_simplifiee.py` | 34 | 88 | 88 |
| `test_plan_b_juges_simplifies.py` | 10 | 12 | 12 |
| `test_plan_b_requalifier.py` | 37 | 71 | 71 |
| `test_plan_b_lecteur.py` | 33 | 106 | 99 |
| `test_plan_b_integration.py` | 4 | 4 | — |
| **total ajouté à la suite** | **118** | **281** | 270 |

Tests sensibles au matériel (docstring « SENSIBLE AU MATÉRIEL », signalés par l'agent du lanceur) : `test_garde_en_ligne_cas_sain_et_d1_sur_le_jouet`, `test_palier_du_chemin_et_d1_sur_le_jouet`, `test_repere_et_rapports_sur_le_jouet`, `test_tous_les_rapports_de_garde_et_lecture_du_run_jouet`. Le test d'intégration sur le run jouet ne l'est pas : il compare deux calculs sur les mêmes nombres.

## 4. Sorties de pytest

Commande : `cd plan-b-code/depot && PYTHONPATH=src <venv-gpu-neuf>/bin/python -B -m pytest -q -p no:cacheprovider <fichiers>`.

- (0) avant l'intégration, les 4 fichiers des agents : `270 passed in 97.51s (0:01:37)`.
- (1) tous les tests du plan B (`tests/test_plan_b_*.py`, 5 fichiers) : `281 passed in 101.68s (0:01:41)`.
- (2) `tests/test_rubrique*.py`, `tests/test_juges*.py`, `tests/test_invites*.py` : **aucun n'existe**. À leur place, les tests des modules gelés que le plan B réutilise et dont ses tests importent les aides (`rubrique`, `juges`, `invites`, `pilote_a`, `lire_pilote`, `lire_notations_pilote`, `noter_pilote_a`) : `tests/test_environnement_a.py tests/test_pilote_a.py tests/test_lire_pilote.py tests/test_lire_notations_pilote.py tests/test_noter_pilote_a.py` : `203 passed in 613.36s (0:10:13)`.
- (3) modules gelés : `git diff --stat HEAD -- src/controle_ia/environnements/rubrique.py src/controle_ia/environnements/juges.py src/controle_ia/harnais` : vide. `git diff --quiet c63d4f1 --` sur les 13 modules gelés : code 0. `git diff --quiet HEAD` (fichiers suivis) : code 0. `verifier-arbre .` : « arbre intact ». Sceaux de `RS1.txt`, `index.json`, `LISEZMOI.md` : OK. Aucun `__pycache__` ni `.pytest_cache` dans le clone.
- `git status --short` : les 10 entrées non suivies du tableau 1 (dont le dossier `docs/sources/invites-plan-b-v1/`).
- La suite complète (environ 30 minutes) n'a pas été lancée : le nombre « Tests attendus » reste à fixer au commit du code.

## 5. Écarts au texte et questions, par agent

Les retours structurés des trois agents ne m'ont pas été transmis (seulement leurs fichiers et un résumé de leurs contrôles). Ce qui suit est relevé dans leurs fichiers (docstrings, tests) et à la lecture du code contre le brouillon 3.

### Agent RS1 (points 1 et 2)
- R-225 appliqué : « , », « ; », « and », « ( » suivis d'un chiffre (signe permis) rendent l'occurrence invalide (« second nombre »), comptée à part des intervalles.
- **Limite constatée, signalée par l'agent** : un second nombre sans l'un des séparateurs (« 3 4 », « 3 vs 4 », « 3 (or 4) », « 3 & 4 ») n'est pas vu, et la fonction gelée lit 3 ; « 3 out of 4 » est lu 3. La phrase du texte « ne choisit jamais entre deux nombres » (« Métrique », l. 103) **n'est donc pas vraie** : le module ne la reprend pas ; le texte doit être corrigé par la session (R-225 dit qu'elle n'est gardée que si elle devient vraie). Un test fixe ce comportement.
- Limite écrite élargie par R-225 : une prose après une note qui commence par « ( » et un chiffre (« 4 (2 weak points) ») rend aussi l'occurrence invalide.
- `index.json` porte deux comptes de caractères (3 966 avec la fin de ligne finale, convention de l'index des invites de l'article ; 3 965 sans, compte du texte).
- Extraction faite sur le brouillon 3, hors du dépôt : à refaire sur l'annexe A du texte scellé (commande d'une ligne dans `LISEZMOI.md`).
- Garde ajoutée, hors du texte : `exiger_criteres_de_l_invite` (critères du code = titres et lignes de format de l'invite).

### Agent juges et lanceur (points 3 et 4)
- **Repère** : le texte nomme la fonction gelée `repere_precision` ; le lanceur ne l'appelle pas. Il calcule le repère (`repere_demi_simple`) avec les fonctions gelées `passe_unique` et `ecarts_par_jeton`, agrégées comme elle, rôles écrits (numérateur ‖a_demi − a_simple‖, dénominateur ‖a_simple‖) : appelée après la conversion, `repere_precision` passerait le modèle courant (simple précision) et prendrait pour référence, au dénominateur, la passe en demi-précision, rôles inversés. C'est le point nommé pour la relecture R2 (VC-15).
- **Citations du préenregistrement inventées** : le lanceur exige, dans le texte scellé, une ligne par citation avec ces intitulés exacts : « Configuration du plan B (empreinte canonique) », « Run du pilote requalifié », « Manifeste du pilote requalifié », « Épisodes du pilote requalifié », « Run des notations rejoué », « Manifeste des notations rejoué », « Résumé des notations rejoué », « Notations rejouées du juge 8B » et « … du juge 3B », « Invite RS1 », « Index de l'invite RS1 », plus les motifs gelés « Commit du code d'analyse », « Tâches du pilote », « Entropie ». Le brouillon 3 ne les porte pas encore.
- **Configuration** : clé `couverture_jetons` (`{"8B": 3072, "3B": 983}`) ajoutée, absente de la table « Configuration » du texte ; `controle_intervalles` prend la forme `{"actif", "separateurs_intervalle", "separateurs_second_nombre"}` : le texte ne liste que les séparateurs d'intervalle (R-225 à reporter).
- Échéances contrôlées aussi avant la conversion et le repère, avant l'ancrage et avant chaque rechargement du témoin (le texte : avant chaque lot et chaque appel du témoin) : plus strict, sans effet sur la borne de dépassement.
- Témoin : configuration effective relue par `_prepare_generation_config`, fonction privée de la bibliothèque (versions égales à celles du pilote, contrôlées) ; à surveiller si la version change.
- Une grandeur illisible (NaN) au palier du chemin y est classée « illisible » → « non concluant (contrôles) » ; signalé dans le code comme « question ouverte à la session » (question I-1).
- Fonctions de bilan pures (k(n − 1), classement, ancrage, couverture, queues, bilans de garde et de paliers) écrites aussi dans le lanceur : la docstring les disait partagées avec la lecture ; elles ne l'étaient pas (question I-2).

### Agent lecteur (point 5)
- Format des fichiers inventé, faute de texte : remplacé par celui du lanceur à l'intégration (section 2).
- NaN : « jamais sous un seuil » (convention gelée de T0.4, `_maximum`, `lire`) ; au palier du chemin, un écart NaN est donc « trop grand », lu « défaut (écart trop grand) » si l'ancrage le permet (question I-1).
- Table E : seule la condition (ii) du relancement s'établit dans la lecture ; (i), (iii), (iv) et (v) restent « sur les pièces » (journal, dépense, alerte, crédit).
- Mutants (hors du clone, `plan-b-code/mutants-lecteur/muter.py`) : 12, dont 11 tués par la suite ciblée, le 12e par `test_gardes_de_lecture_artefacts[lecture-rs1]`, exclu de son lancement. Non refait après l'intégration (rôle de la relecture R2, angle 3).

## 6. Questions de l'intégration (pour la session)

- **I-1 (règle de lecture, à fixer avant le scellement)** : écart NaN au palier du chemin. Lecteur, qui fait foi : « défaut (écart trop grand) » si R_S ≤ 1e-2/3 (convention de T0.4 : une valeur illisible n'est jamais conforme), donc « défaut du chemin » et requalification suspendue ; second calcul du lanceur : « non concluant (contrôles) ». La table C ne dit rien du NaN ; la table D le range parmi les déclencheurs « trop sale ». Options : (a) garder le lecteur (avantage : convention gelée de T0.4 ; inconvénient : un « défaut » non établi suspend la requalification) ; (b) écrire au texte « grandeur illisible → non concluant (contrôles), audit » et aligner le lecteur (avantage : un défaut doit être montré, la réserve 1 reste levable ; inconvénient : écart à la convention de T0.4). Recommandation : (b), confiance moyenne. Le test `test_second_calcul_du_lanceur_egal_a_la_lecture_sur_les_fonctions_pures` fixe l'écart actuel pour qu'il ne se perde pas.
- **I-2 (routine)** : garder le second calcul du lanceur, comparé au lecteur par le test d'intégration (recalcul indépendant, coût nul pendant le run), ou le retirer pour réduire la surface de relecture. Recommandation : le garder tel quel, docstring corrigée.
- **I-3 (scellement)** : écrire dans le texte les intitulés de citation exigés par le lanceur (section 5) et compléter la table « Configuration » (`couverture_jetons`, séparateurs de R-225, noms des juges 8B et 3B, que le lecteur exige désormais).
- **I-4 (scellement)** : corriger la phrase « ne choisit jamais entre deux nombres » (limite de R-225) et nommer, au « Plan d'analyse », l'emploi de `passe_unique` et `ecarts_par_jeton` à la place de `repere_precision`.

## 7. Points du texte que le code ne couvre pas encore

- **Point 6, chaîne de lancement** (hors de cette étape) : `scripts/amorce_instance_t05_planb.sh` et `scripts/planb_t05_instance.sh` (empreintes à fixer au candidat) ; `docs/procedures/planb-T0.5-v1/` : amorce et script de l'instance (`ETUDE=planb`, délai externe de 412 minutes, plafond de l'amorce de 462 minutes), lanceur qui prend l'offre conforme la moins chère et applique la règle de crédit sur 8,1 heures, contrôles avant dépense, surveillance (création plus 28 320 s), relevé cumulatif, récupération, scellement, répétition jouet, bancs ; copies versées et scellées. Avec elle, la liste d'arrêt « Avant l'installation », « Avant les tests » et « Tests » (dernière ligne « N passed… », N égal aux tests attendus), et « Dépense » (plafond de 13,6 USD, alerte à 120 USD).
- **Contrôles avant dépense** : R-067 sur le tokeniseur du 3B (notes de 0 à 5 en un seul jeton) ; longueurs réelles des contextes RS1 (le lanceur les consigne pendant le run, rien ne les mesure avant).
- **Causes d'un arrêt et relancement** (table E) : classement infrastructure, déterministe ou indéterminée (journal de l'instance, durée de mise en place contre 2 700 s), conditions (i), (iii), (iv), (v), branche `calcul/t05-planb-reel-v2` : à la récupération et à la session.
- **Scellement** : configuration `prereg/T0.5-plan-B-juges-config-v1.json` et son empreinte canonique ; entropie tirée au scellement ; citations (section 5) ; nombre « Tests attendus » (suite complète au commit du code) ; empreintes des scripts de l'instance ; réextraction de RS1 depuis l'annexe A scellée ; versement de l'archive (notes de conception, contre-lectures, vérifications, `travail/`).
- **Après le run** : audit R4 (relectures tirées, recalcul indépendant par un sous-agent neuf), verdict R13 : processus, non code.
- Mesure non faite ici : mutants sur le lanceur et sur le code d'intégration (relecture R2, angle 3).

## 8. Fichiers hors du clone

- `plan-b-code/integration/` : `originaux/` (copies d'avant l'intégration), sorties de pytest `pytest-avant.txt`, `pytest-plan-b-apres.txt`, `pytest-geles-apres.txt`.
- Des agents précédents : `essais-plan-b/` (`essai_d1.py`, `essai_bonus.py`, `essai_garde.py`), `mesure_jouet.py`, `plan-b-code/mutants-lecteur/muter.py`.
