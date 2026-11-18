# Vérification courte du code v3 du saboteur à budget (ii-b) — v1

> Vérification neuve (même famille, autre modèle que le développeur : Claude Opus 5.5 contre Claude Opus 4.6 ; N-052) d'un code de course **exploratoire, non opposable (R-522)**. Processeur seulement. Rien n'a été lancé sur une carte, rien n'a été dépensé, aucun modèle réel n'a été chargé, aucune clé n'a été lue. Seul appel réseau : `git fetch` des deux branches nommées par le mandat. Aucun fichier de `registres/`, `diag/`, `runs/`, `donnees/` ou `docs/verdicts/` du dépôt n'a été ouvert. Ni commit, ni poussée.

## 0. Identité

- Mandat : `docs/notes/barreau8-iib-v1/mandat-verification-courte-code-iib-v3-v1.md`, empreinte `abaad0e81c911ca9ac5ca8048627e872e70f3a3b2e709625b0162fe1265fe759`, vérifiée (compagnon égal).
- Branche vérifiée : `origin/prep/iib-code-v3`, tête `d88e3d947ec4f05958834e2746a800c854271a8f`, un seul commit au-dessus de `a3adf4128` (ancêtre de `origin/main`). Les commits v1 (`3baecee7`) et v2 (`7a1f5e39`) ne sont **pas** ancêtres de la tête. Le commit ajoute 35 fichiers (14 modules, 13 essais, 5 scripts et une liste, le rapport v2 et son compagnon).
- Arbre de travail à moi : `/home/user/iib-verif-v3`, supprimé à la fin.
- Rapport du développeur v2 : `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v2.md`, empreinte `6bb7073a40c5da5106c7ec10da12512eb570ab4f3edfd161c7f01320421d2908`, égale au compagnon et au mandat.
- Contre-lecture de référence : `docs/notes/barreau8-iib-v1/contre-lecture-code-iib-v2-v1.md` (`8e5078e9…`, vérifiée).
- Consigne privée : lue par `git show` dans un script seulement (empreinte `9f8bbdef…90c1`, égale à son compagnon) ; aucun extrait affiché ni recopié.
- **Je suis exclu de tout rôle de lecteur des sondes du barreau 8** (j'ai lu la consigne privée par programme).

## 1. Verdict

**Autorisable après corrections.**

Constats : **0 bloquant, 2 majeurs, 5 mineurs**.

Le bloquant CLV2-01 est levé **en substance** : aucun fragment ni motif réel de la consigne privée dans les 35 fichiers ajoutés ni dans le message du commit. Mais l'essai de non-fuite versé pour le garder est **inerte** : il ne refuse pas un motif réel planté (VC3-01). Les corrections CLV2-02 et CLV2-05 sont faites. CLV2-03 ne l'est qu'en partie (VC3-02). Les 406 essais passent. La répétition jouet est identique à l'octet.

## 2. Constats

| identifiant | gravité | où | constat | correction demandée |
|---|---|---|---|---|
| **VC3-01** essai de non-fuite inerte | **majeur** | `tests/test_iib_exclusion_v1.py:199-209` ; `:212-219` | (a) Essai sain : après `continue` (`:200`), tout le corps de la boucle (`:201-209`) est indenté **sous** ce `continue`, dans la branche des fichiers « consigne-privee ». C'est du code mort : aucun fichier n'est lu, aucun motif ni triplet n'est cherché. Épreuve faite : un motif réel (rang 1, 25 caractères) planté dans un fichier temporaire `scripts/piege_verif_iib_tmp.py` de mon arbre → l'essai **passe** (`1 passed`). Fichier retiré ensuite, arbre propre. (b) Essai artefact : il écrit le motif dans un fichier puis vérifie `motif in texte`. C'est une tautologie : il n'appelle pas la logique de l'essai sain. (c) Le périmètre de l'essai sain ne couvre ni les rapports de la branche, ni le message du commit, alors que la contre-lecture les demandait. Le rapport v2 (`:15`, `:52`) et le message du commit présentent cet essai comme la preuve de la non-fuite. | Désindenter le corps (`:201-209`) d'un niveau, hors du `if`. Faire de la recherche une fonction appelée par l'essai sain **et** par l'artefact, l'artefact plantant un motif réel et un triplet réel dans un fichier temporaire. Étendre l'essai aux rapports `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-*` (hors fichiers de consigne). Écrire des messages sans le motif (voir VC3-05). |
| **VC3-02** gardes neuves encore sans artefact (CLV2-03 en partie) | **majeur** | `tests/test_iib_consigne_invisible_v1.py` (inchangé depuis la v2) ; `tests/test_iib_lanceur_v1.py:325-341` ; `tests/test_iib_configuration_v1.py:163-176` ; `src/controle_ia/iib/session_v1.py:76-84` | Faits, avec artefact : sorties par tour (3 essais), identifiants incohérents (09), non-convergence (04), base décisive (03, 7 cas), base modifiée pendant la distillation (10), bornes de prix (4 cas). Encore sans artefact : (06) indication plantée aux pas 1 à 9 de l'évaluation, hors maître. Le fichier d'essai n'a pas changé et l'artefact de la ligne 141-142 reste sans portée. (11) clé `condition` des sorties d'évaluation : essai sain seulement. (12) part des épisodes honnêtes acceptés : essai sain seulement, et `echelle_h_cohen` n'est vérifiée nulle part. (13) aucune des autres bornes de l'offre (cœurs, mémoire vive, volume de téléchargement, mémoire de la carte, prix et nom de la carte) n'a d'artefact. Garde neuve de la ligne de création de 7b (`MOTIF_LIGNE_CREATION_7B`, §4-14) : aucun artefact (une ligne sans identifiant d'instance → refus). R5. | Un artefact par garde nommée ci-dessus. Le modèle de l'annexe B de la contre-lecture v2 (espion des contextes, neuf bornes) peut être repris. |
| VC3-03 rapport v2 encore infidèle par endroits | mineur | `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v2.md:15`, `:22`, `:33`, `:34`, `:51`, `:52` | (a) Il présente l'essai de non-fuite comme une vérification, alors qu'il est inerte (VC3-01). (b) Il présente CLV2-03 comme traité, sans dire que 06, 11, 12 et 13 (hors prix) restent sans artefact. (c) Il donne CLV2-11 pour corrigé, ce qui est faux (VC3-04). (d) Il dit que l'essai de §4-12(a) « vérifie la structure » : la clé neuve n'y est pas vérifiée. (e) Il annonce 54 fichiers comparés : j'en compte 48 avec l'entropie 20261118, car le rapport ne donne pas son entropie. CLV2-05 est corrigé pour l'essentiel : chaque essai cité existe (16 noms vérifiés), et le diff v2 → v3 correspond aux changements décrits. | Version 3 du rapport (nom neuf, R12) après VC3-01 et VC3-02, avec l'entropie de la répétition. |
| VC3-04 paire commune aux consignes factice et réelle toujours présente (CLV2-11 non levé) | mineur | `src/controle_ia/iib/jouet_v1.py:36` | Les lignes 36 et 37 ont changé, mais les mots remplacés ne sont pas ceux de la paire commune. La même paire de deux mots (longueurs 7 et 4) et la même sous-chaîne de 13 caractères restent sur la ligne 36. Je l'ai vérifié par programme, sans affichage. Ce constat reste sous le seuil de trois mots. | Remplacer ces deux mots par des mots inventés. Vérifier par programme (longueurs seulement). |
| VC3-05 messages d'échec qui porteraient un motif réel | mineur | `tests/test_iib_exclusion_v1.py:71`, `:116` ; et `:203` une fois VC3-01 corrigé | Si l'essai échoue, `assert …, motif` (`:116`) écrit le motif réel dans la sortie. `ValueError(f"exemple fabriqué {exemple!r} …")` (`:71`) y écrit un exemple tiré du motif. La réécriture des assertions par `pytest` afficherait aussi le motif et le texte du fichier pour `assert motif not in texte`. L'amorce rejoue la suite sur l'instance et garde sa sortie (`scripts/amorce_instance_iib_v1.sh:384`, fichier `tests.txt`). | Messages avec le rang et la longueur seulement. Pour la non-fuite, utiliser `assert not trouve, message` sur un booléen calculé à part. |
| VC3-06 forme de la ligne de création de 7b choisie par le développeur | mineur | `src/controle_ia/iib/session_v1.py:76` | La contre-lecture demandait la forme exacte de la ligne du registre, fournie par la mère. Le motif `7b.*\binstance\s+\d+` est une forme inventée par le développeur. Il est sans artefact (VC3-02). | La mère fixe la forme de sa ligne. Le motif et un artefact suivent. |
| VC3-07 restes de CLV2-06 | mineur | `src/controle_ia/iib/lecture_v1.py:296` ; `:212-235` | Le seuil est maintenant dans `FIXES_PAR_LE_CODE`, et les itérations et le gradient sont écrits par pli : c'est fait. Restent deux points. `code.get("facteur_seuil_non_convergence", 100)` est un repli par défaut ; il est sans effet en mode réel, où la configuration doit égaler `FIXES_PAR_LE_CODE` (`configuration_v1.py:296-297`), mais c'est un repli silencieux de forme. Le gradient retenu est encore celui d'avant le dernier pas. | Lire la clé sans défaut. Recalculer le gradient après le dernier pas, ou l'écrire dans la conception. |

## 3. Corrections déclarées → état constaté

| constat de la contre-lecture v2 | déclaré | constaté |
|---|---|---|
| CLV2-01 fragments | corrigé | **levé en substance** (§ 5.1). Exemples fabriqués à l'exécution par `_exemple_depuis_motif` (analyseur d'expressions), aucun dictionnaire d'exemples. Essai de non-fuite **inerte** (VC3-01). |
| CLV2-02 sorties tour par tour | corrigé | **corrigé**. `lanceur_v1.py:308` écrit l'oracle, les identifiants et les textes à la fin de chaque tour (`…-tour<r>`). Les fichiers d'évaluation ne portent que l'évaluation (`:405`). Les trois artefacts existent et passent (arrêt pendant le tour 2, épreuve E-O6, arrêt M). |
| CLV2-03 artefacts des gardes neuves | corrigé | **en partie** (VC3-02) |
| CLV2-04 portage de la base (A) | décision laissée | **non tranché**. En-tête en partie mis à jour (une ligne). Seuil de non-convergence ajouté aux réglages. Voir § 6. |
| CLV2-05 rapport fidèle | corrigé | **pour l'essentiel** (VC3-03) |
| CLV2-06 seuil en dur | corrigé | **en grande partie** (VC3-07) |
| CLV2-07 bornes de prix | corrigé | **corrigé** (0,08 et 0,05, constantes nommées, 4 artefacts). L'empreinte de la liste ciblée n'est pas recoupée dans le code Python. Seule l'amorce l'écrit en dur (`amorce_instance_iib_v1.sh:370`, égale à l'empreinte réelle `847676ef…e3b6`). |
| CLV2-08 fichiers par phase, R12 | corrigé | **corrigé** (phases sans cumul, vérification d'existence ajoutée pour les identifiants et les textes). Le § 7 de l'ordre reste à compléter (§ 6). |
| CLV2-09 imports transitifs | non fait | non fait, déclaré |
| CLV2-10 essais de la lecture (2) et des tours | non fait | non fait, déclaré (`tests/test_iib_tours_v1.py` inchangé) |
| CLV2-11 paire commune | corrigé | **non levé** (VC3-04) |
| § 4-12(a) échelle | corrigé | ajouté à `taux_fin`, donc écrit dans `acceptation-iib.json` (`tours_v1.py:186-190`). Clé non vérifiée par un essai. |
| § 4-14 ligne de 7b | corrigé | garde ajoutée, forme non fournie par la mère, sans artefact (VC3-06) |
| § 4-17(c) clés de graine | corrigé | **corrigé** : `iib/lecture-2/tirages_aire` et `iib/lecture-2/tirages_taux` sont dérivées au manifeste (`lanceur_v1.py:126`) et employées séparément (`lecture_v1.py:307`, `:339`) |

## 4. Essais rejoués

`cd /home/user/iib-verif-v3 && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider --basetemp=/tmp/iib-verif-v3-tmp -rsx $(cat scripts/tests-cibles-iib-v1.txt)`

Dernière ligne : **`406 passed in 415.73s (0:06:55)`**, de 19:02:31Z à 19:09:29Z, aucun saut. La liste ciblée compte 13 fichiers et porte l'empreinte `847676eff87f20c8aa5d7b1a1b401a7dd025c71c57d190ec0ba9c306f397e3b6`, inchangée. Le dossier de travail a été supprimé.

Le jetoniseur jouet par caractères tourne ici. Le jetoniseur réel n'est éprouvé par aucun essai.

**Répétition jouet**, dans un dépôt jetable de mon bloc-notes : `preparer` (entropie 20261118, configuration `b9e9ab9b…c43f`), commit, `jouer 20261118-191500-iib-jouet-a`, commit, `jouer 20261118-191501-iib-jouet-b`, commit, `comparer`. Résultat : **`48 fichiers comparés, 0 différent(s)`**, code 0. Les deux jeux donnent 7 acceptés en 2 tours. Fichiers par phase présents (étalonnage, tour 1, tour 2, évaluation), sans fichier cumulatif des tours. Ces sorties sont factices ; je les ai supprimées.

**Graines (R9)** : toutes les sources d'aléa du paquet viennent du manifeste (`manifeste.generateur`, `numpy.random.SeedSequence` à `spawn_key`). Les graines par suite du modèle jouet (`modele_v1.py:149`, `:195`, `:229`) sont reçues de `graines_des_actions(generateur(…))` (`lanceur_v1.py:198`). Le diff v2 → v3 n'ajoute aucune source d'aléa. Il sépare la clé double de la lecture (2).

**Moyenne ou médiane sur les jetons** : aucune. Le diff v2 → v3 n'en ajoute aucune. Les moyennes et médianes portent sur des actions, des tâches ou des tirages. Le paquet n'a aucune sonde et n'écrit aucun fichier de sonde.

## 5. Recherche des fragments de la consigne privée

### 5.1 Méthode et résultat

Le script hors dépôt (`fragments_arbre.py`, dans mon bloc-notes) dérive de l'annexe A de la contre-lecture v2. Il lit la consigne par `git show origin/lot/compte-4-v1:…` et vérifie son empreinte contre le compagnon. Il la découpe par `iib/consigne_v1` de la v3 : consigne de 95 mots, indication de 12 mots, 9 motifs. Il n'affiche que des comptes, des longueurs, des rangs et des chemins.

Le script parcourt **tout l'arbre** de la tête, soit 28 802 fichiers :
- 1 873 fichiers sous `diag/`, `runs/`, `donnees/` et `docs/verdicts/` sont exclus par le cloisonnement. Le commit v3 n'y ajoute rien : ses 35 fichiers sont tous hors de ces dossiers.
- 926 fichiers non textuels ou non UTF-8 sont sautés (documents PDF, archives, tableaux binaires). Aucun n'est ajouté par la v3.
- 26 003 fichiers textuels sont examinés.

Pour chaque fichier et pour le message du commit, le script cherche :
- les triplets de mots communs avec la consigne et avec l'indication ;
- les motifs réels à la lettre, avec et sans la casse ;
- les motifs réels qui trouvent quelque chose.

Pour les 35 fichiers ajoutés, le message du commit et tout fichier avec une alerte, il cherche aussi la plus longue suite de mots commune et la plus longue sous-chaîne commune en caractères.

**Fichiers ajoutés par la v3 et message du commit** : triplets **0** partout ; motifs réels à la lettre : **aucun** ; motifs qui trouvent : **aucun** ; plus longue suite : 2 mots, sur `jouet_v1.py`, `lecture_v1.py`, `tests/test_iib_lanceur_v1.py`, `tests/test_iib_oracle_v1.py` et `tests/test_iib_tours_v1.py`, ailleurs au plus 1 ; plus longue sous-chaîne : 13 caractères (`jouet_v1.py:36`, VC3-04), ailleurs au plus 9. Les motifs `iib:01` et `iib:05` de CLV2-01 n'apparaissent à la lettre dans **aucun** fichier de l'arbre, hors des deux fichiers de consigne eux-mêmes.

**Validation de la méthode.** Le cas sain est l'ensemble des 35 fichiers ajoutés : aucun triplet, aucun motif. L'artefact est la consigne elle-même, présente dans l'arbre : la méthode y trouve 93 triplets de la consigne, 10 de l'indication et les 9 motifs à la lettre.

### 5.2 Fichiers hérités de `main` (hors du commit v3), à signaler à la mère

Mêmes objets que sur `main` ; ils ne sont pas de la responsabilité du code v3.
- Les deux fichiers de consigne privée eux-mêmes (brouillons 1 et 2, mêmes objets sur `main`, la v3 et le lot) sont dans l'arbre de la branche. Quiconque lit la branche peut les lire.
- Trois fichiers de la conception de (ii-b) sur `main` portent à la lettre des motifs réels de rangs 2, 7 et 8 :
  - `brouillons/ii-b-saboteur-budget-v1/contre-lecture-ii-b-v1-cl1.md` ;
  - `brouillons/ii-b-saboteur-budget-v1/couples-contre-lecture-ii-b-v1-cl1.json` ;
  - `brouillons/ii-b-saboteur-budget-v1/journal-redaction-ii-b-v1.md`, rang 7 seulement.
- Ces trois rangs se trouvent aussi dans des fichiers plus anciens sans rapport avec (ii-b). Le rang 7 est dans les consignes de P3 et de P3-bis, le rang 2 dans des notes de financement, le rang 8 dans une source. Ils ne sont donc pas propres à (ii-b).
- La consigne partage une suite de 12 mots avec les consignes de P3 (héritage commun), dans les fichiers de P3 et dans les essais de P3-bis.
- À trancher par la mère pour la copie expurgée et pour le cloisonnement du lecteur des sondes. Ce n'est pas un défaut du code v3.

## 6. Ce qui reste avant la course

1. **Code** : VC3-01 et VC3-02 à corriger, puis VC3-03 à VC3-07. Ensuite, un contrôle court par un lecteur qui n'est pas le développeur : rejouer l'artefact de non-fuite, la recherche par programme et la suite ciblée. Le commit propre qui en sort sera celui que citeront `COMMIT_CODE_IIB` et `EMPREINTES_CODE_IIB`.
2. **Nœud CLV2-04 : réglages du portage de la base textuelle dans la lecture (2), à décider avant la course.** Ils sont lus dans la configuration du manifeste (`lecture_v1.py:360`) et doivent figurer dans `FIXES_PAR_LE_CODE` (`configuration_v1.py:57-59`) avant la course. Je les nomme sans les fixer.
   - (a) **Le choix lui-même** : portage complet de la base (A) de T0.8, ou forme hybride actuelle déclarée dans la conception.
   - (b) **La liste exacte des traits** de la base « traits » (`lecture_v1.py:251-264`). Aujourd'hui : coût normalisé, coût brut, indicateur d'illisible, unité, log10(1 + longueur), `valide` et formes du champ.
   - (c) **L'unité de longueur** : caractères (aujourd'hui, `:192`) ou jetons. Si ce sont des jetons : quel jetoniseur et à quelle révision figée.
   - (d) **Garder ou retirer `valide`**, qui vaut exactement 1 − `illisible` (`:256`).
   - (e) **La règle « sans centre »** : nombre minimal de coûts lisibles pour qu'une tâche ait un centre, et traitement d'une tâche sans centre (exclusion, ou valeur neutre). Aujourd'hui, la valeur est 0 sans seuil (`_normaliser`, `:206-209`).
   - (f) **Le centrage** : statistique (médiane aujourd'hui) ; ensemble des conditions mises en commun (les quatre conditions aujourd'hui) ; calcul sur toutes les actions ou par pli d'apprentissage.
   - (g) **La méthode d'ajustement et ses réglages** :
     - méthode de Newton aujourd'hui, ou celle de la base (A) ;
     - régularisation L2 (λ = 1) ;
     - nombre maximal d'itérations (100) ;
     - tolérance (10⁻¹⁰) et critère d'arrêt (sur le pas aujourd'hui) ;
     - facteur du seuil de non-convergence (100) ;
     - gradient lu avant ou après le dernier pas (VC3-07).
   - (h) **Le vocabulaire de la base « mots et coût »** : motif des mots, taille (1 000), présence binaire. Déjà écrits ; à confirmer dans la même décision.
   - (i) **Suites communes aux deux options** : en-tête du module mis à jour, car les traits décrits aux lignes 17-18 ne sont plus ceux du code ; essais du portage (aire 1 si le coût sépare, voisine de 0,5 sans signal, centre inchangé par permutation des étiquettes, tâche sans centre).
3. **CLV2-09** (espion au niveau des fonctions, course et lectures, artefact) et **CLV2-10** (deux cas de la lecture (2), deux parties du constat 16) : non faits. Le développeur les dit non bloquants ; la mère tranche s'ils précèdent la course.
4. **§ 4-08** : borne basse bilatérale à 95 % (quantile 0,025), à écrire dans la conception et l'ordre scellés. Aucun code.
5. **§ 4-18** : écrire au § 4 de l'ordre que le commit cité doit contenir la ligne de GO inscrite. Aucun code.
6. **Ordre exploratoire** (brouillon 2, non scellé) :
   - les 30 marqueurs à remplir par la mère ;
   - le § 7 à compléter des fichiers par phase et par tour (`oracle-iib-<phase>.json`, `ids-actions-iib-<phase>.npz`, `textes-actions-iib-<phase>.jsonl`, où la phase vaut étalonnage, tour r ou évaluation), en plus des fichiers combinés ;
   - la forme de la ligne de création de 7b (VC3-06) ;
   - la place des épreuves de l'oracle ;
   - une contre-lecture neuve, puis le scellement.
7. **Devis** : une version neuve (R12) aux dates à jour, la variante de plafond tranchée, puis l'inscription.
8. **Épreuves de l'oracle en réel** : elles n'ont tourné que sur le jouet. La mère tranche si la phase A de la course suffit ou s'il faut une passe préalable, avec sa dépense et son devis. Les longueurs de la consigne au jetoniseur réel (`<<LONGUEURS_CONSIGNE_IIB>>`) en dépendent.
9. **Essais qui dépendent de `tokenizers` et du jetoniseur réel sur carte** : ils n'ont jamais été exécutés. Il s'agit de la coupe du préfixe, des jetons à cheval, de l'arrêt au saut de ligne, du cache dupliqué en demi-précision, de la mémoire de la distillation et du débit du jumeau. Recommandation : un essai sur processeur avec les seuls fichiers du jetoniseur réel à la révision figée, sans modèle, si cela ne coûte rien ; sinon une réserve écrite dans l'ordre.
10. **Décision CLV2-01 (4) sur le distant** : la branche `origin/prep/iib-code-v2`, qui porte encore les deux motifs réels, existe toujours sur le dépôt distant. Il faut la retirer, ou la déclarer gelée et exclue de la copie publique. C'est un nœud de Lazar s'il touche le distant.

## 7. Lectures hors de ce mandat, limites

- **Lectures hors de la liste du mandat** : `git ls-tree` et `git rev-parse` sur `main` et `origin/main`, pour les ancêtres et les objets des fichiers de consigne (noms et empreintes d'objets seulement). Un diff v2 → v3 sur les seuls fichiers de `src/` et la liste de ses fichiers. Je n'ai pas affiché le diff de `tests/test_iib_exclusion_v1.py`, qui porterait les motifs de la v2. Les noms des fichiers hérités qui portent une alerte (§ 5.2), affichés par mon script, sans leur contenu.
- **Exécutés sans lecture de leur code** : `t06.session`, `premier_test_ia.conditions.blocs_cites`, `manifeste`, par les essais et la répétition jouet.
- **Non lus** : la base (A) de T0.8 (CLV2-04 est nommé d'après la contre-lecture v2 et le code), l'ordre, le devis, la conception, les registres, et aucun fichier de `diag/`, `runs/`, `donnees/` ou `docs/verdicts/` du dépôt.
- **Limites** :
  - La recherche compte des triplets, des suites, des sous-chaînes et des motifs. Une paraphrase lointaine lui échappe.
  - La sous-chaîne en caractères n'est calculée que pour les fichiers ajoutés et les fichiers en alerte.
  - Les modules inchangés depuis la v2 n'ont pas été relus ligne à ligne.
  - La routine de reprise du dépôt n'a pas été jouée (c'est le rôle de la session mère), et aucune instance n'a été inventoriée.
- **Refus** : aucun.
