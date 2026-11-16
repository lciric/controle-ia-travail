# Vérification du différentiel v1 → v2 du code de l'idée 1.1 (R2) — contre le préenregistrement scellé `prereg/organisme-idee-1-1-poids-du-nul-v2.md` (`3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff`)

- Auteur : contre-lecteur neuf, sous-agent de la session mère. Je n'ai écrit ni le texte, ni le code v1 ou v2, ni le rapport du développeur, ni la contre-lecture du code v1.
- Date (UTC) : 2026-11-15, de 23:20 à 23:33 (`date -u`). Dépôt lu sur `main`, tête `02ed55f2`. Arbre propre au début et à la fin.
- Ce que je n'ai pas fait :
  - aucun fichier existant modifié, aucun commit, aucune poussée ;
  - aucun appel réseau ni payant ;
  - ni le jeu, ni l'étape 0, ni la lecture, ni la répétition miniature lancés ;
  - aucun résultat lu ; rien ouvert sous `diag/`, `runs/`, `donnees/`.
- Une seule exécution du banc, hors de tout jeu : 20 répétitions isolées (une par ligne) sous une **racine d'essai** propre à cette vérification, différente de celle du texte (vérifié), pour éprouver la lecture v2 sur des enregistrements réels (section 3). Rien n'a été écrit dans le dépôt.
- Pièces lues :
  - la contre-lecture du code v1 (`8def0cf5…`, empreinte recalculée, égale) ;
  - le rapport v2 (`a0376d5e…`, égal) et `couples-v1-vers-v2.json` (`17f06db0…`, égal) ;
  - les treize fichiers v2 et l'essai neuf du différentiel, avec leurs empreintes recalculées : toutes égales au rapport et aux compagnons ;
  - chaque `diff` v1 → v2 ;
  - dans le texte : « Prédiction chiffrée », « Métrique », « Seuil », « Plan d'analyse » (Banc, Bras, Cellules, Graines, Étapes), et la réponse de la contre-lecture à M1 ;
  - le « Banc B v2 » du préenregistrement de l'idée 1.2 (`bdabf2bc…`, recalculée), pour les lignes V1 à V5.

## 0. Verdict

**Corrections avant l'étape 0 : une majeure (N1) ; jouable ensuite, sans autre changement exigé.**

- **N1 (majeur)** : la lecture v2 s'arrête sur une erreur `KeyError` dès qu'elle reçoit un vrai enregistrement du banc. Les verdicts de la v1 seraient calculés, mais aucun `lecture.json` ne serait écrit. Après le jeu, la correction toucherait un fichier gelé : M1 refuserait alors la lecture, à juste titre, et il faudrait un écart au texte.
  - Fichier : `src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v2.py`, l. 593 à 602 et l. 619 et 620.
  - Essai manquant : `tests/test_organisme_idees_juge_idee_1_1_lecture_v2.py`, l. 67.
- Le reste du différentiel est conforme :
  - M1, M2 et m1 à m11 sont corrigés ou déclarés ;
  - E1 est levé ;
  - aucun verdict de la lecture v1 ne change ;
  - aucun écart nouveau au texte ;
  - aucun repli silencieux introduit.
- Mineurs nouveaux, à faire dans la même passe : n1 à n5 (section 7). Aucun ne demande de changer le banc.
- Essais rejoués : **259 passés sur 259** en 248,85 s, dans un seul processus (section 8).

## 1. Égalité v2 = v1 + différentiel déclaré

- **Rejeu indépendant de l'essai d'égalité**, par un script de ma main hors du dépôt : pour chacun des 13 fichiers,
  - le v1 est égal à son compagnon ;
  - chaque « ancien » est présent une seule fois ;
  - le v1, avec les couples appliqués dans l'ordre puis l'ajout de fin, est égal octet pour octet au v2.
  
  Les 13 fichiers sont **égaux**. L'essai du dépôt (14 cas) passe aussi.
- **Aucun fichier v1 n'a changé** depuis `3c015999`, le commit contre-lu : `git diff --stat 3c015999 HEAD` sur les fichiers v1 est vide. Aucun autre code n'a changé entre `3c015999` et `02ed55f2` : seulement les fichiers v2, les notes et `registres/decisions.md`.
- **Chaque `diff` relu**, sur son contenu et pas seulement sur sa forme. Le JSON ne déclare rien de plus que ce qui suit :
  - **banc** : docstring ; `probas_finies` exige `> 0` (l. 200 et 201) ; plancher retiré aux l. 938 et 994 ;
  - **mutations** : imports seulement ;
  - **étape 0** : imports ; `declarations` dans la sortie ; ajout de `essais_d_egalite`, `empreintes_ep` et `declarations` ;
  - **exécution** :
    - imports et nom du run, plus la liste `NOMS_RUN_DE_CE_JEU` ;
    - `FICHIERS_GELES` complété ; `ESSAIS` limité aux essais v2 ;
    - dans `lire_addendum`, les clés exigées (m2) et l'égalité fichier par fichier (M2) ;
    - ajout de `verifier_addendum_du_manifeste` (M1) et de `exiger_depot_propre_sauf_run` (m8) ;
  - **lecture** :
    - m1 (l. 92 à 94) ;
    - `lru_cache` sur `cp_bas_unilateral`, fonction pure sur des entiers : sans effet sur une valeur ;
    - m4, m5 et m7 ;
    - ajout de la partie M3 (l. 496 à 641) ;
  - **scripts** : imports ; reprise (m8) ; E1 dans le lanceur ; M1 et `lire_v2` dans `lire` ; sortie et déclarations dans l'étape 0 ;
  - **essais** : imports, et les essais neufs.

## 2. Corrections de la contre-lecture v1 : essai sain et artefact

« Artefact v1 » répond à la question : l'artefact échouerait-il, c'est-à-dire serait-il accepté, sans la correction ? Je l'ai vérifié par la logique du v1, et pour M2 par un rejeu de chaque raison d'arrêt.

| point | corrigé | essai sain | artefact v1 | remarque |
|---|---|---|---|---|
| M1 | oui : `lire_idee_1_1_v2.py`, l. 47, avant toute lecture | `test_m1_…` | oui : la fonction n'existe pas en v1, et le script v1 ne relit pas l'addendum | quatre artefacts : sans addendum ; autre empreinte ; autre programme ; fichier gelé modifié |
| M2 | oui : `lire_addendum`, l. 293 à 301 | `test_m2_…` | oui : le v1 accepte les six cas | j'ai rejoué chaque cas par un script : chacun s'arrête **pour sa raison** (message lu), et le cas sain est accepté. Comme `lire` appelle `lire_addendum`, le lien entre l'étape 0 et le code est aussi revérifié à la lecture |
| M3 | en partie : voir section 3 et **N1** | `test_lecture_v2_…`, `test_strates_…`, `test_mcnemar_exact` | oui | les essais ne passent que sur des enregistrements synthétiques qui ne ressemblent pas au banc (N1) |
| m1 | oui | `test_m1_quantite_fatale…` | oui | `MEMBRE_DE_LA_COPIE` couvre les sept lignes fatales (Q1 à Q5, Q9a, Q9b) : sur le banc réel, aucun arrêt n'est attendu |
| m2 | oui : les six clés sont exigées, et `jeu_permis is True` | dans `test_m2_…` | oui | |
| m3 | oui ; la stricte positivité vaut aussi pour `proba_carte` (l. 212), qui sert à toutes les cartes | `test_m3_…` | oui | la garde est plus large que les deux lignes de m3, mais elle ferme du côté de l'arrêt. Les lois de `lois_v1` sont plafonnées à 10⁻¹² puis renormalisées : rien ne devrait s'arrêter sur le banc, et l'étape 0 le montrera |
| m4 | oui : trois lectures à part, plus la liste des cellules « non tenues ou non jugeables » | essai de lecture (sain seulement) | — | la condition de « nécessaire » est celle du texte (dent sur H7 **et** gel tenu). Elle n'exclut plus le trou : c'est conforme |
| m5 | oui | `test_m5_…` | oui : le v1 compte zéro | |
| m6 | déclaré (`declaration_m6`) | — | — | |
| m7 | oui : P5 peut valoir « partielle » ; P12 est lue sur ses réfutations, partie par partie | essai faible (seulement « P5 ∈ {vrai, faux, partielle} ») | — | j'ai relu les cinq parties contre la colonne « ce qui la réfute » : elles sont exactes |
| m8 | oui | `test_m8_…` | oui | section 5 |
| m9, m10, m11 | déclarés dans `declarations()`, qui passent au bloc programme de l'addendum | `test_declarations_m9_m10` | — | |
| E1 | levé | `test_e1_…` | oui | section 4 |

**Verdicts de la lecture v1 : aucun n'a changé.** `lire_v2` commence par appeler `lire`, sans rien y changer d'autre que les points suivants :

- m1 : arrêt sur une clé absente ;
- m4 : forme de la sortie de la garde P4 (`verdict` remplacé par `lectures`). Aucun code ne lisait `garde_P4["verdict"]` (vérifié) ;
- m5 : un rapporté ;
- m7 : deux prédictions, et le calcul de « toutes vraies » qui sert à l'audit ;
- `lru_cache`.

L'étage 1 (taille, fatales, copies), l'étage 2 (dents), ρ, la principale, ρ⁺ et son ordre, La, Ld, les secondaires et `issue` ont un code identique.

## 3. M3 : grandeurs ajoutées contre la « Métrique »

| grandeur | texte | code v2 | avis |
|---|---|---|---|
| taux et intervalle bilatéral | « Clopper-Pearson, bilatéral à 95 % pour le rapport » | `cp_bilateral` : quantiles bêta 0,025 et 0,975, bornes 0 et 1 aux extrêmes | **exact** |
| McNemar | « test exact de McNemar par ligne (rapport) » pour Δ_{X,Y} | exact bilatéral, min(1 ; 2·F(min(n₁₀, n₀₁)))) ; 15 lignes V × 11 paires | formule exacte. **Lecture** : la liste des paires et la restriction aux lignes V. Il manque J9-D et J9-D40 contre J9⁺ (n3) |
| log W maximal et médian par cellule | « Mesures descriptives » | sur les répétitions, à partir du log W maximal de chacune ; pour J9-D, la quantité fatale | lecture admissible ; **plante sur A2 (N1)** |
| ρ par strate | « Rapportée aussi par strate : structure sur une partition du bras / hors des partitions du bras » | même formule de ρ ; I recalculé sur les 15 lignes V dans chaque rééchantillon, puis coupé à la strate ; graines `(99, b)` ; quantiles de Bonferroni | formule exacte. **Lecture** : un rééchantillon n'est écarté que s'il n'a **aucune** ligne informative dans la strate, alors que la principale en exige 2 (n2) |
| décomposition du prix, avec intervalles | « Avec les intervalles du rééchantillonnage » | 1 − ρ_La, ρ_La − ρ_Ld, ρ_Ld ; mêmes rééchantillons, appariés ; percentiles à 95 % | formule exacte. **Lecture** : le niveau de 95 %, que le texte ne donne pas. Les rééchantillons écartés ne sont pas comptés (n4) |
| gains secondaires contre J9⁺ | « rapportés contre J9⁺ de la même façon » | `lire_gain(…, plus=True)` : I⁺ par (J8, J9⁺) ; Y = J9⁺ quand Y = J9 ; quantiles à 95 % | **exact** ; « de la même façon » est lu juste |
| ρ⁺ | « ρ⁺_X = … ; mêmes quantiles de Bonferroni » | calculé pour J9-P seul (déjà en v1) | ρ⁺ de La et de Ld absent (n5, défaut déjà présent en v1, non relevé alors) |

**Tableau des strates.** C'est une **lecture** : le texte ne dit pas quelle ligne V appartient à quelle strate. Pour la vérifier, j'ai repris :

- les lignes V1 à V5 du « Banc B v2 » ;
- les classes du texte :
  - J9-P : la famille linéaire, la sous-population, et chaque coupure {z_j ≤ c} pour toute valeur c du plan ;
  - La : v8, plus les deux coupures de l'archive ;
  - Ld : La, plus la sous-population et le signe de chaque trait ;
  - v8 ne contient pas la sous-population, comme le montre la ligne Q3 du tableau des cellules ;
- la réponse à [CL] M1 : « aucune découverte posée sur une coupure de l'archive », d'où V5.

Les partitions de chaque ligne :

- V1 : effet global, sans partition ;
- V2 : signe z_j > 0 ;
- V3 : seuil décentré, à plus de 0,3 de la coupure de l'archive ;
- V4 : sous-population ;
- V5 : coupure A de l'archive.

On en tire exactement le tableau du développeur :

- J9-P : V2 à V5 sur une partition, V1 hors des partitions ;
- La : V5 sur, V1 à V4 hors ;
- Ld : V2, V4, V5 sur, V1 et V3 hors.

**C'est la seule lecture naturelle**, sous deux réserves de forme qui ne changent aucune case :

- pour V2 sous J9-P, la coupure au signe 0 n'est pas une valeur du plan. La coupure à la plus grande valeur négative induit pourtant la même partition des 200 instances : V2 est donc bien « sur une partition » ;
- les lois S3 et S4 de l'archive sont elles-mêmes par morceaux, mais sur les coupures A et B, qui sont déjà celles de La.

Une lecture qui ferait dépendre la strate des lois par morceau, et non de la partition, serait sans objet : aucune classe ne contient M sur les lignes V.

Un choix reste ouvert : le texte n'impose pas de limiter les strates aux trois primaires. C'est admissible, puisque la phrase suit la mention des primaires. Ce tableau, la règle « au moins une ligne » (n2) et le niveau de la décomposition sont à **inscrire à l'addendum** comme lectures déclarées, avant le jeu.

**N1, démontré.** J'ai joué une répétition de Q1 sous la racine d'essai, puis appelé `taux_des_cellules({"Q1": [rec]})` :

- l'appel s'arrête sur `KeyError: 'max'` à `lecture_idee_1_1_v2.py`, l. 620 → 602 → 92 à 99 (`log_w_max`, dernière ligne) ;
- la cause : le banc écrit `rec["A2"] = {"promue", "log_w_200"}` (banc, l. 892), sans champ `max` ;
- l'essai synthétique ne le voit pas, parce que `_rec` (essai de lecture, l. 67) donne un `max` à A2 ;
- A2 est joué sur toutes les lignes, et `taux_des_cellules` est appelé **avant** l'arrêt aux étages 1 et 2 : la lecture v2 tombe donc dans tous les cas ;
- l'erreur n'est pas une `GardeArret` : le script s'arrête sur une trace Python, sans message d'arrêt écrit.

J'ai ensuite contourné A2 dans mon seul script : `taux_des_cellules` et `lire_mcnemar` passent alors sur 19 lignes réelles (Q1, Q8, Hs, H7 et les 15 lignes V). **A2 est le seul défaut** de cette sorte que j'aie trouvé.

Correction proposée, à faire en v3 :

- `_lw_rep` rend `r["A2"]["log_w_200"]` pour A2, la valeur que le texte lit (« lu à 200 ») ;
- l'enregistrement synthétique `_rec` suit le banc : A2 sans champ `max` ;
- un essai neuf passe `taux_des_cellules`, `lire_mcnemar` et les rapportés sur des enregistrements produits par `jouer_repetition` (une répétition par ligne suffit ; environ 3 s par ligne).

## 4. E1 : lanceur v2

`scripts/jouer_idee_1_1_v2.py`, `jeu_decisif`. L'ordre est le suivant :

1. texte scellé ;
2. dépôt propre ;
3. addendum relu par `lire_addendum`, qui revérifie les fichiers gelés, l'étape 0 liée au code (M2) et la règle rejouée ;
4. copies vérifiées ;
5. vue chargée ;
6. puis, en départ neuf :
   - aucune sortie antérieure ;
   - essais v2 ;
   - dix-sept mutations ;
   - **`E0.essais_d_egalite`** (l. 142 et 143), qui joue E0, E9, EP et ED et lève une `GardeArret` si l'un d'eux échoue (l. 421 à 423 du module) ;
7. ensuite seulement : manifeste, départ scellé, jeu.

Les résultats sont écrits au manifeste (`controles_avant_jeu.essais_d_egalite`). C'est l'étape 2 du texte : **E1 est levé.**

L'essai `test_e1_…` éprouve l'arrêt (ED manqué), mais pas l'ordre dans le script. J'ai vérifié l'ordre en lisant le code.

En reprise, les quatre essais ne sont pas rejoués. Ils l'ont été au départ du même run : c'est admissible.

## 5. m8 : reprise

`exiger_depot_propre_sauf_run` (exécution, l. 327) lit `git status --porcelain --untracked-files=all`. Elle ne tolère que les chemins qui commencent par `runs/<run>/` ou par `diag/organisme-idees-juge-v1/<run>/`, avec la barre finale : un autre run au nom voisin n'est pas toléré.

L'essai couvre trois cas :

- sain ;
- un fichier étranger ;
- le dossier d'un autre run.

Le lanceur exige ensuite que l'identifiant finisse par `idee-1-1-poids-du-nul-v2` et que le manifeste et le départ scellé existent. Un identifiant forgé ne tolère rien de plus : les chemins de `git status` sont normalisés.

**Conforme : la reprise ne tolère que les dossiers du run repris.**

Remarque déjà présente en v1, que la v2 ne touche pas : la reprise ne compare pas l'empreinte de l'addendum passé à celle du manifeste. Seuls les processus et les réductions sont comparés. `lire_addendum` garantit pourtant que le code est celui de l'addendum passé, et M1 refusera à la lecture un addendum différent de celui du manifeste. Le défaut ferme donc du bon côté. Je le note sans le demander.

## 6. Écarts, replis, fermeture des imports

- **Écarts nouveaux au texte scellé : aucun.**
- **Replis silencieux introduits : aucun.** J'ai relu chaque `.get(` du différentiel :
  - `add.get("programme")` et `preenregistrement.get("sha256")` ferment en arrêt ;
  - `donnees[l][0].get("J9-D", {})` ne retire qu'un rapporté descriptif ; une répétition plus loin sans quantité fatale arrête ;
  - le retour anticipé de `lire_v2` quand les étages 1 ou 2 ne sont pas franchis est conforme au texte (« rien d'autre n'est lu »).
  
  Deux cas limites ne sont pas gardés : un quantile sur une liste vide dans `lire_rho_strate` et dans `lire_decomposition`, si tous les rééchantillons étaient écartés. L'appel s'arrêterait sur une erreur numpy, du côté de l'arrêt et sans valeur inventée, mais sans message propre (inclus dans n2 et n4).
- **Les scripts v2 n'importent aucun module v1 touché.** Je l'ai vérifié par une fermeture dynamique :
  - les trois scripts sont importés, puis `vue_v9_v1.charger()` ;
  - tous les modules chargés depuis le dépôt sont listés ;
  - aucun `*_idee_1_1_v1` n'en fait partie ;
  - hors de `.venv`, les seuls modules qui manquent à `FICHIERS_GELES` sont les copies tierces (`code-organisme-94bfd92/orchestrator/pole/*`, `copie-nul-v9-a41b7b5/…/nul_v9.py`). Ces copies sont gardées par `juge_v1.verifier_copie` et `vue_v9_v1.verifier_copie_v9`, appelés par le lanceur avant le jeu, comme en v1.
  
  **La liste des fichiers gelés couvre donc tout ce que le jeu et la lecture importent dans `src/` et `scripts/`.** Elle couvre aussi les fichiers v1 et le JSON des couples, sources de l'essai du différentiel.

## 7. Mineurs nouveaux (aucun ne porte un verdict)

- **n1** — `scripts/jouer_idee_1_1_v2.py`, l. 89 : `"version_lanceur": 1` reste écrit au manifeste par le lanceur v2. Le nom du script est déjà dans `commande`, mais le champ est faux. À passer à 2.
- **n2** — `lecture_idee_1_1_v2.py`, l. 540 : une strate garde un rééchantillon dès qu'il compte une ligne informative, alors que la principale en exige deux. Les deux règles sont admissibles, aucune n'est écrite au texte. À inscrire à l'addendum ; un message d'arrêt si tous les rééchantillons sont écartés.
- **n3** — l. 580 : `PAIRES_MCNEMAR` ne contient pas J9-D ni J9-D40 contre J9⁺, alors que leurs gains contre J9⁺ sont rapportés. À ajouter, ou à déclarer.
- **n4** — l. 549 à 575 : `lire_decomposition` ne compte pas les rééchantillons écartés, alors que ρ les compte. Le niveau de 95 % est à déclarer.
- **n5** — l. 330 (code de la v1, laissé tel quel en v2) : ρ⁺ n'est calculé que pour J9-P. Le texte définit ρ⁺_X avec « mêmes quantiles de Bonferroni », donc pour les trois primaires. À rapporter pour La et Ld **sans toucher au verdict**, par un appel à part dans `lire_v2` : le J9-P de `rho_plus` ne doit pas changer.
- Les essais de m4 et de m7 n'ont qu'un cas sain. Un artefact chacun serait utile (trou et dent manquée ensemble ; P5 à 2 lignes ; une partie de P12 réfutée).

## 8. Essais rejoués

- Conditions :
  - les 12 fichiers `tests/test_organisme_idees_juge_idee_1_1_*` (v1 et v2, différentiel compris) ;
  - un seul processus, `nice -n 10`, `OMP_NUM_THREADS=1` ;
  - les variables `GIT_*` retirées par leur nom, sans afficher aucune valeur ;
  - sans cache.
- **Résultat : 259 passés, 0 échec, 248,85 s**, de 23:24:13 à 23:28:23 UTC.
- C'est le compte du rapport : 117 essais v1 et 142 essais v2. L'arbre est propre après.
- À part, hors du dépôt : le rejeu de l'égalité (13 sur 13), les raisons d'arrêt de M2 (6 artefacts et le cas sain) et la démonstration de N1 (section 3).

## 9. Écarts au texte scellé (liste à jour, réservés au directeur)

- **E1 (ordre des étapes)** : **levé** par la v2 (section 4).
- **E2 (lettre de « Proximité avec le vrai juge »)** : **inchangé**. Le jeu appelle les fonctions internes, et non `evaluer_v2` ou `evaluer_v9`. L'égalité est éprouvée par les essais et par E9, rejoué désormais par le lanceur avant le jeu. Toujours à trancher.
- **E3 (« sans coût de plus », J9-Dc)** : **inchangé**. Toujours à trancher.
- Écart nouveau : **aucun**.
- Lectures déclarées, sans écart, à inscrire à l'addendum :
  - le tableau des strates (seule lecture naturelle) ;
  - les règles des strates (n2) ;
  - le niveau de 95 % de la décomposition ;
  - les paires de McNemar et leur restriction aux lignes V ;
  - m6, m9, m10, m11 ;
  - les comptes non écrits.

## 10. Avant l'étape 0

1. N1 : `lecture_idee_1_1_v2.py`, l. 593 à 602 (`_lw_rep` pour A2), avec un essai sur enregistrements réels ; `tests/test_organisme_idees_juge_idee_1_1_lecture_v2.py`, l. 67 (`_rec`).
2. n1 à n5 dans la même passe, au choix de la mère.
3. Noms neufs en v3 (R12), différentiel déclaré, essais rejoués, puis relecture du différentiel v2 → v3 par un sous-agent neuf. Ensuite seulement : l'étape 0, puis le jeu.

## 11. Incidents de ma main

- Aucun fichier existant modifié.
- Un seul fichier créé dans le dépôt : ce rapport et son compagnon.
- Des scripts de travail et le journal des essais sont dans le dossier temporaire de la session, hors du dépôt.
- Une exécution du banc sous une racine d'essai, déclarée en tête : elle ne lit et n'écrit aucun résultat du jeu.
- Aucune variable d'environnement affichée.
