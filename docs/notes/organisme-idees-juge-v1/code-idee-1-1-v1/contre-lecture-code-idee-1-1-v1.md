# Contre-lecture du code de l'idée 1.1 (R2) — contre le préenregistrement scellé `prereg/organisme-idee-1-1-poids-du-nul-v2.md` (`3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff`), version 1

- Auteur : contre-lecteur neuf, sous-agent de la session mère ; je n'ai écrit ni le texte, ni la preuve, ni le code, ni le rapport du développeur, ni aucune de leurs contre-lectures.
- Date (UTC) : 2026-11-15, de 22:58 à 23:09 (`date -u`) ; dépôt lu sur `main`, tête `3c015999`, arbre propre au début et à la fin ; aucun fichier existant modifié, aucun commit, aucune poussée, aucun appel réseau ni payant.
- **Pas lancés** : le jeu, l'étape 0, la lecture, la répétition miniature du lanceur. Aucun résultat lu ; rien ouvert sous `diag/`, `runs/`, `donnees/`.
- Pièces lues : le texte scellé en entier (empreinte recalculée, égale) ; la preuve v3 (hypothèses P1 à P6, H7′, lemme 4 et son exigence de code) ; le rapport du développeur (`c970a897…`, égal à son compagnon) et ses trois différentiels (égaux à leurs compagnons) ; les douze modules, les trois scripts, les cinq fichiers d'essais ; dans les copies tierces : `nul_v9.py` (`7ae450df…`, recalculée), `selection_pari.py` (`proba`, `Cache`, `tirer_categorie`), les trois fichiers de la course « projection » (empreintes recalculées, égales au texte) ; le « Banc B v2 » du préenregistrement de l'idée 1.2.

## 0. Verdict

**Jouable après corrections.** Le banc, les bras, les gardes du jeu et l'ordre du gel suivent le texte ; je n'ai trouvé aucun défaut dans le calcul des richesses ni dans la garde P4. Les trois majeurs touchent le **verrouillage autour du jeu** (lecture et étape 0), pas le jeu lui-même : aucun ne demande de changer le banc. Deux écarts de forme au texte sont à faire trancher (section 9).

- Majeurs : 3 (M1 à M3). Mineurs : 11 (m1 à m11).
- Essais rejoués : **117 passés sur 117**, 124 s, un processus (section 7).
- Les corrections changent des fichiers gelés : noms neufs (R12), essais rejoués, différentiel relu, étape 0 lancée **après** elles.

## 1. Correspondance texte → code

Conforme, vérifié ligne à ligne :

- **30 lignes**, indices 0 à 29 dans l'ordre du texte (`banc_idee_1_1_v1.py`, l. 76 à 93) ; Q1 à Q7 et V1 à V5 égales au « Banc B v2 » ; Q8 (600 pas, poids à six décimales, renormalisés), Q9a, Q9b, Hs, Hm, Hg, Hn, H7 égales au tableau du texte (l. 248 à 330).
- **J8, J9, La, Ld** : bibliothèque standard, marginale d'entraînement, membres par `membres_archive_v8`, `membres_archive_v9`, et le nul limité ; engagement par l'appel écrit au texte, argument pour argument (l. 560). **Différentiel du nul limité rejoué par moi** (`diff -u`) : égal au fichier joint, à l'alignement de deux lignes vides près ; il ne porte que les quatre changements déclarés. Solveur et constantes intacts.
- **J9⁺** : champ `atteinte` (l. 777). **J9-D40, J9-D** : engagement jumeau à T₄₀, règle en réunion (l. 1040 à 1046), domination gardée. **J9-Dc** : l'indice de la coupe est juste (nombre de valeurs distinctes ≤ c parmi les t premières, face aux seuils « −∞ puis chaque valeur » de `_coupes`). **Je juge la copie sûre** : chaque borne par coupe est un certificat valide quel que soit l'état de convergence (commentaire et code de `maximiser_par_lots`) ; une coupe élaguée garde une borne plus lâche, donc une lecture plus prudente.
- **J9-P, La-P** : richesse = minimum de W^reste et du terme projeté ; familles = linéaire, sous-population, chaque valeur distincte du plan (liste vérifiée à chaque répétition, l. 1077) ; 300 pas puis 150 pas ; pari plein ; seconde écriture du terme (l. 1059). Les égalités de z dans un bloc sont traitées juste.
- **A1, A2** : corps recopiés, pas de 0,05, A2 lu à 200. **Lignes H** : J9-P-nu, refus, gel ; J9, J9-D40, J9-D sur Hs, Hm, Hg, Hn ; rien d'autre sur H7 ; trois quantités de Hn ; témoin exact.
- **Principale** : I parmi les 15 lignes V seulement, écrites deux fois ; seuil 0,02 ; I recalculé dans chaque rééchantillon ; rééchantillon à moins de 2 lignes écarté et compté ; quantiles 0,833 % et 99,167 % ; ordre « nuisible, regagne, ne regagne pas, partiel » ; ρ⁺ avec I⁺ ; le moins favorable retenu.
- **Holm à 61**, dans chaque sens ; **34 fatales** (22 + 12) ; 7 copies ; 32 de taille : comptes gardés par `exiger_comptes_du_texte`. Dents à 0,5 et à 0,05. Seuils de l'annexe A éprouvés par essai.
- **Règle de réduction** : cinq crans dans l'ordre, chacun entier ; jamais sur les 61 cellules ni sur les primaires ; rejouée par `lire_addendum`. **48 heures** comptées du premier départ, vérifiées à chaque répétition et dans l'attente du parent.
- **Graines** : `SeedSequence(entropy=racine, spawn_key=…)`, racine = entier de l'empreinte du texte ; `(i_ligne, r, 0)`, `(i_ligne, r, 1)`, `(99, b)`. Les essais prolongent les clés : `(98, r, 0|1)`, `(97, k, …, 0|1)`. Lecture admissible (il faut deux flux par répétition), **non déclarée au rapport** : à inscrire à l'addendum (m9).

## 2. Liste d'arrêt, essai sain et artefact (R5), replis silencieux

Chaque ligne de la liste a un arrêt dans le code, un cas sain et un artefact ; le tableau du développeur (section 3 de son rapport) est exact. Les `except` larges du banc de mutations ferment tous du côté du blocage (cas sain en erreur = manqué ; détecteur en erreur = mutation survivante).

Replis trouvés, tous mineurs, aucun n'est actif sur le banc tel qu'il est :

- **m1** — `lecture_idee_1_1_v1.py`, l. 90 : `rec["J9-D"].get("quantite_fatale", -math.inf)`. Une quantité fatale absente passerait pour « aucun dépassement ». À remplacer par un arrêt.
- **m2** — `execution_idee_1_1_v1.py`, l. 268 et 269 : `res0.get("resultat", res0)` et `corps0.get("bloquants")`. Un fichier d'étape 0 sans la clé `bloquants` est accepté. Clés à exiger.
- **m3** — `banc_idee_1_1_v1.py`, l. 937 et 993 : `np.maximum(…, cm.PLANCHER)` au numérateur gelé et à celui de H7. Inactif (le juge plafonne déjà à 10⁻¹², la carte H7 aussi), mais une probabilité nulle serait masquée au lieu d'arrêter ; `probas_finies` (l. 197) ne vérifie pas la stricte positivité.

## 3. Garde P4

Conforme sous ses deux formes.

- **Gel** : `carte_gelee_bloc` (l. 649) appelle `proba` avec `list(passe)`, de longueur exactement 25·b, jamais le `Cache` ; `FluxFrais.passe` refuse tout autre nombre de blocs tirés. La même loi gelée sert à la projection, au certificat et au numérateur de W^reste. Pour Hg, la fenêtre se vide après cinq pas dans le bloc : c'est ce que le texte et le lemme 4 annoncent. Pour H7, la carte gelée est le monde lui-même (excès du bloc non lu).
- **Journal** : carte sans mémoire, les huit empreintes sont dans l'enregistrement avant la création du générateur des issues (l. 583, 634 à 636) ; sous gel, l'empreinte du bloc b est écrite avant `tirer_bloc(b)` (l. 641 à 644) ; `valeurs_e` revérifie l'empreinte avant d'employer la projection.
- **Mêmes issues** : un flux par répétition, huit appels `random(25)` sur toutes les lignes, quels que soient les bras ; chaque bras reçoit un dictionnaire lié à son empreinte ; des issues différentes arrêtent.
- **Refus** : comptée « refusée », jamais promue ; « nu » interdit hors des cinq lignes H.

## 4. Lecture

Les critères qui portent un verdict sont appliqués sans choix. Mais :

- **M1 (majeur) — la lecture peut se lancer avec un code modifié après le jeu.** `scripts/lire_idee_1_1_v1.py`, l. 39 à 55 : le script exige le préenregistrement scellé, le manifeste et la sortie scellée, mais **ne relit pas l'addendum** et ne compare l'empreinte d'aucun fichier gelé. `lecture_idee_1_1_v1.py` pourrait être changé après le scellement de la sortie sans qu'aucune garde ne lève. Correction : lire `m["config"]["addendum"]` (chemin, empreinte), vérifier l'empreinte, appeler `X.lire_addendum` (qui vérifie chaque fichier gelé), refuser sinon ; essai sain et artefact.
- **M3 (majeur) — la lecture gelée ne calcule pas tout ce que la « Métrique » gèle**, ce qui laisserait des choix après lecture :
  - gains secondaires **contre J9⁺** : `lire_gain` a le paramètre `plus`, jamais appelé avec (l. 339 à 341) ;
  - ρ **par strate** (« structure sur une partition du bras », « hors des partitions du bras ») : absent ; l'appartenance de chaque ligne V à une strate, par bras, doit être écrite en code avant le jeu ;
  - **intervalles** de la décomposition du prix (l. 388) : estimations ponctuelles seules ;
  - test de **McNemar** par ligne, intervalle bilatéral des taux de cellule (l. 280), log W médian par cellule : absents.
  Aucun de ces éléments ne porte un verdict ; tous sont écrits au texte comme rapportés.
- **m4** — l. 366 à 373 : « trou atteint par la grammaire », « non éprouvée » et « nécessaire » sont rendus comme un seul verdict, avec une priorité que le texte n'écrit pas ; le libellé de la l. 373 dit « non tenue » pour un cas qui peut être « non jugeable ». Rendre les trois lectures à part (les composantes sont déjà dans la sortie).
- **m5** — l. 423 : la part des écarts résiduels > 2·10⁻³ est comptée sur J9 seul (question 9).
- **m6** — l. 223 à 229 : pour un secondaire réduit, I est recalculé sur les seules premières répétitions (seuil de 0,02 à n = 500). Le texte ne tranche pas entre cela et le I des 1 000. Sans effet si aucune réduction 5 n'est appliquée ; à déclarer.
- **m7** — l. 455 et 471 à 475 : P5 n'a pas son état « partielle » ; P12 est évaluée sur ses chiffres et non sur ses réfutations écrites (question 8).

## 5. Script de jeu

Conforme : `exiger_prereg_scelle` et égalité à `3ffe1739…`, arbre propre, addendum exigé et vérifié (fichiers gelés, bloc programme, règle rejouée), copies, essais, mutations, un manifeste par run, départ scellé, tranches scellées, `sortie.json` scellé, arrêt consigné sur toute exception, aucune lecture.

- **M2 (majeur) — le fichier d'étape 0 n'est pas lié au code gelé.** `execution_idee_1_1_v1.py`, l. 264 à 275 : `lire_addendum` vérifie le scellé du fichier d'étape 0 et l'absence de bloquants, mais ne compare pas son champ `fichiers_geles` (écrit par `scripts/etape0_idee_1_1_v1.py`, l. 71) aux empreintes de l'addendum. Une étape 0 passée sur un code antérieur (par exemple avant les corrections de ce rapport) ouvrirait le jeu d'un code différent : préalable 1, E0 à ED, critères de H7 et de Hn, chronométrage vaudraient pour un autre code. Correction : exiger l'égalité, fichier par fichier, et l'empreinte du texte ; essai sain et artefact.
- **m8** — `scripts/jouer_idee_1_1_v1.py`, l. 105 : `exiger_depot_propre` est appelé aussi en reprise. Or `runs/<run>/` et `diag/…/<run>/` sont alors des fichiers non suivis (`git status --untracked-files=all`) : **la reprise est refusée** tant que la sortie partielle n'est pas committée. Elle ferme du bon côté, mais la reprise annoncée ne marche pas telle quelle. À corriger (tolérer les seuls fichiers du run repris) ou à documenter.

## 6. Étape 0

- **Préalable 1** : complet dans le code. (a) seize noms, liste égale au texte ; (b) E9 ; (c) vue hors du dépôt, chaque fichier vérifié avant et après recopie puis après le rejeu, interpréteur fils isolé, essais joués un à un ; un essai sauté, en échec ou non importable bloque ; une classe attendue absente bloque ; un rejeu filtré n'est jamais le préalable.
- **Essais d'égalité** : E0 à 10⁻¹², 100 répétitions, clés `(98, r)` ; E9 par `sans_morceaux`, valeur pour valeur ; EP à 10⁻⁹ sur chaque log e et sur le minimum ; ED à 2·10⁻³.
- **Mutations** : les dix-huit du texte y sont ; dix-sept dans `jouer_banc`, la dix-huitième (« garde P4 retirée ») par le compte de H7 : mort à 20 sur 200, cas sain à 2, Hn sous gel bloquant à 3. Raisons de mort attendues vérifiées par message.
- **Chronométrage** : 20 répétitions × 30 lignes, gel par bloc compris, temps seuls ; D = somme / p ; la strate est comptée dans la base à 1 000 répétitions (majorant).
- **m10** — `etape0_idee_1_1_v1.py`, l. 51 : `essai_projection_cas_v1.py` n'est vérifié que contre son compagnon ; son empreinte est à citer à l'addendum.
- **m11** — le lanceur rejoue les dix-sept mutations (l. 131) mais pas le compte de H7 ni de Hn : couvert si M2 est corrigé ; à dire à l'addendum.

## 7. Essais rejoués

Un processus, `OMP_NUM_THREADS=1`, `nice -n 10`, sans variable `GIT_*`, sans cache : **117 passés, 0 échec, 124,25 s** (23:03:54 à 23:05:59 UTC). Par fichier : projection 22, gardes 30, banc 41, lecture 16, exécution 8. Arbre propre après.

## 8. Les questions du développeur (sa section 5 en compte neuf, pas huit)

| n° | objet | avis | raison |
|---|---|---|---|
| 1 | forme scindée de `_blocs_projection` | **lecture admissible** | le texte exige à la fois la reprise de l'optimiseur et qu'aucune issue du bloc n'atteigne la projection ; il fixe pour EP une tolérance de 10⁻⁹, qui suppose un module distinct. Différentiel lu : mêmes opérations, même ordre, mêmes pas ; lot d'un bloc sous gel égal au lot de huit (essai) |
| 2 | J9-Dc par un second appel au solveur | **lecture admissible** ; voir écart E3 | le jumeau reste « évalué par le code du v9 » ; J9-Dc est descriptif. Mais « sans coût de plus » devient faux dans ce montage |
| 3 | richesses calculées fonction par fonction | **admissible sur le fond ; écart de lettre E2** | le texte demande des grandeurs que `evaluer_v9` ne rend pas (valeur atteinte, valeur par membre, trajectoire non arrondie pour les gardes à 10⁻⁶). Mêmes fonctions, même ordre, gardes rejouées. Mais le jeu n'appelle jamais `evaluer_v2` ni `evaluer_v9`, que le texte nomme |
| 4 | huit lectures de texte | **admissibles** | ordre des lignes V : seule lecture naturelle ; uniformes d'entraînement tirés avant le plan : imposé par Q8 ; E0 : essai d'égalité, l'archive A0 ne sert qu'au nul ; table du membre de la copie : fixée avant le jeu, juste ligne par ligne ; La-P « comme J9-P » : le texte l'écrit et dit que tout autre réglage est un écart ; coût du processus retenu, strate recalculée (les autres membres ne dépendent pas des membres log-linéaires) : descriptifs ; A2 à 200 : conforme |
| 5 | comptes non écrits | **admissibles**, à inscrire à l'addendum | le texte ne fixe aucun de ces comptes ; `commun` n'a pas de constructeur de mondes, `cas` le fournit avec les pièces de `commun` (m10) |
| 6 | Hn sous gel : « l'un ou l'autre » | **admissible, et égale au texte** | le terme sur toutes les familles est un minimum qui contient la famille linéaire : il ne peut pas promouvoir sans elle ; la condition ajoutée ne bloque jamais seule |
| 7 | aucun essai réécrit | **admissible** (plus strict) | un échec bloque ; « aucune réécriture ne remplace un essai d'origine rejouable ». À vérifier au rejeu officiel : pourquoi les sept essais de `GrainesEtPreenregistrement` passent dans la vue, alors que le texte les attendait non rejouables |
| 8 | P12, « Hn environ 0,10 » non évaluable | **admissible** ; correction m7 conseillée | le texte écrit sa réfutation (borne basse ≤ 0,05) : la partie est évaluable par elle |
| 9 | écart résiduel compté sur J9 seul | **lecture trop étroite, sans écart de protocole** ; correction m5 | « des évaluations » couvre La et Ld ; valeurs déjà enregistrées, ligne seulement rapportée |

## 9. Écarts au texte scellé (réservés au directeur)

- **E1 — ordre des étapes, non déclaré.** Le texte place les essais d'égalité E0, E9, EP, ED à l'étape 2, après l'addendum et les contrôles, avant le jeu. Le code les joue à l'étape 0 seulement ; le lanceur ne les rejoue pas. Sans effet si M2 est corrigé (mêmes graines, même code, résultat déterministe). Deux sorties : faire rejouer les quatre essais par le lanceur (environ dix minutes ; alors plus d'écart), ou faire acter l'ordre.
- **E2 — lettre de « Proximité avec le vrai juge ».** J8 et J9 ne sont pas évalués par `evaluer_v2` et `evaluer_v9` dans le jeu, mais par leurs fonctions internes ; l'égalité à six décimales n'est éprouvée que par les essais et par E9 (deux répétitions par ligne). Je le tiens pour admissible sur le fond ; c'est la plus fragile des lectures déclarées.
- **E3 — phrase descriptive contredite.** « Sans coût de plus : les bornes par coupe sont déjà calculées » (bras 5, J9-Dc) est faux dans le montage strict : un second appel au solveur, chronométré dans le groupe du jumeau. Aucun critère n'en dépend.

Je n'ai trouvé aucun écart sur une hypothèse, une métrique à verdict, un seuil, une graine du jeu ou la liste d'arrêt.

## 10. Corrections demandées avant le jeu

1. M1 — `scripts/lire_idee_1_1_v1.py`, l. 39 à 55.
2. M2 — `execution_idee_1_1_v1.py`, l. 264 à 275 (et m2, l. 268 et 269).
3. M3 — `lecture_idee_1_1_v1.py`, l. 339 à 341, l. 280, l. 378 à 394, et les strates de ρ.
4. Mineurs : m1 (lecture, l. 90) ; m3 (banc, l. 937, 993) ; m4 (lecture, l. 366 à 373) ; m5 (l. 423) ; m6 (l. 223 à 229, à déclarer) ; m7 (l. 455, 471 à 475) ; m8 (lanceur, l. 105) ; m9, m10, m11 (addendum).
5. E1 à E3 : à porter à la mère, pour le directeur.

## 11. Ce que je n'ai pas vérifié

Le rejeu des essais d'origine du v9 (non lancé) ; l'étape 0 et ses comptes ; les durées ; la preuve (hors de ma mission) ; le code de `lois_v1.py` et de `juge_v1.py`, déjà contre-lus pour l'idée 1.2 ; la reprise après un vrai arrêt de machine ; l'égalité bit à bit de la forme scindée au-delà des essais (10⁻⁹).

## 12. Incidents de ma main

Aucun fichier existant modifié. Un seul fichier créé : ce rapport et son compagnon. Un fichier de travail hors du dépôt (journal des essais, dossier temporaire de la session). Aucune variable d'environnement affichée.
