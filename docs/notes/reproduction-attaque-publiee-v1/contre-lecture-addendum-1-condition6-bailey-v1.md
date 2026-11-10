# Contre-lecture de l'addendum 1 (condition de lancement 6) du témoin de Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le texte scellé, ni l'addendum, ni le code, ni les essais, ni la liste
  des lectures, ni aucun des rapports de relecture cités. Date : `date -u` = Tue Nov 10 17:46:42 UTC 2026 (fin des
  vérifications).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, tête `e8cd8d99`, arbre propre
  avant ce rapport (le seul écart à `99b59d33` est l'addendum). `origin/main` relevé à `09ede09f` (par
  `git fetch --depth=400 origin +refs/heads/main:refs/remotes/origin/main`) ; `origin/claude/upbeat-cray-dmauvv` relevé
  à `55433bf0` (même forme de `git fetch`, refspec explicite). Aucune autre requête réseau.
- Pièce relue : `prereg/temoin-attaque-publiee-bailey-v1-addendum-1-condition6.md`
  (`daf2ef9dbcf90c4c742c3c255f740a85d8ac5804408826d80b53a8830d4fb2c0`), en entier.
- Pièces de contrôle (SHA-256 sur disque) :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), l. 360-391 (liste d'arrêt, conditions de lancement) ;
  - liste des lectures v7 `lectures-addendum-condition6-v7.md` (`9f03ad70bd2ba60c06b1c5f04d802b1147abbf79c3b1873ef2589c5fd131bcd3`), en entier ; `diff` avec la v6 (`2b0923e3…`) ;
  - décisions : `registres/passations/2026-11-10-1240-decision-lazar-noeud5-lecture-b2.md` (`2f3e8e3a0bbb37543b9cada3f019eb77d700acb734c0f75638332e7f4871f2a2`), `…-1657-decision-lazar-lectures-et-pilote.md` (`d4f21aa5849ed49c34ab3f4c4ff8c50a16de998eced1bf71d8a785f1cfebd932`), `…-1118-decision-lazar-go-autonome-bailey.md` (`5ae71cf3…`), `…-1204-decision-lazar-modele-location-d2.md` (`85d95700…`), `…-1216-decision-lazar-autonomie-totale.md` (`0821cb81…`), en entier ; passations d'étape `…-1231-attaquant-informe-successeur-etape.md` (`ee3fb47c…`, l. 20-40) et `…-1434-attaquant-informe-successeur-etape.md` (`54e56860…`, l. 1-50) ;
  - session-dépôt, sur `origin/claude/upbeat-cray-dmauvv` : `registres/passations/2026-11-10-1310-decision-lazar-addendum2-manifeste.md` (`52990ef0e4906744cb99707a1181bfd293bd2141887eaa83dced42336f9d3b7e`) et `…-1654-erratum-heure-addendum2.md` ;
  - `prereg/bras-attaque-regle-v1-addendum-2.md` (`73c8de015fe77619658d35a0ff59be513988092a9feb4d8720d36a810876adbc`, compagnon conforme), l. 1-35 ; contre-lecture `contre-lecture-addendum-2-regle-bras-v1.md` (`8bf0cecc…`), § 3 ;
  - registre des GO : `git show origin/main:registres/go.md` (l. 300-303) et `git show cbc9c5ce:registres/go.md` ;
  - rapports de relecture du code : en-têtes et verdicts de `relecture-lignes-touchees-code-condition6-v7/-v8-bailey-v1.md`, `controle-correction-c1-lanceur-v9-bailey-v1.md` (§ 5-6) ; `relecture-differentiel-analyse-v2-bailey-v1.md` (`8895a5a7…`, verdict, D-1 à D-12) ; `contre-lecture-code-analyse-bailey-v1.md` (`151eee65…`, « À préciser ») ; `relecture-differentiel-code-condition6-v2-bailey-v1.md` (`4f079ece…`, en-tête) ; empreinte et compagnon de chacun des onze rapports cités ;
  - code au commit `99b59d33` : empreintes des sept modules et des deux fichiers d'essais ; `lanceur_v9.py` (constantes l. 118-136, `CHEMINS_ARCHIVE` par import, l. 251-280, 627, 809-812, 1023-1107) ; `instance_v8.py` (l. 73, 102-107, 140-165) ; `analyse_v3.py` (l. 1-45, 387-390, 459-471) ; `conventions_v3.py` (l. 33-34, 59) ; `tests/test_temoin_bailey_condition6_v3.py` (l. 830-850) ;
  - manifeste `versions-figees-temoin-bailey-v1.json` (`e21bccf6eb99c9255f0069be7af2fe5d729bde9ab05db56811ccef1eddee06f9`) : clés `python`, `versions` (nombre), `git`, `revisions_…`, `acces_jeton_hugging_face`.
- Non lu : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`,
  `registres/etat.md`, `registres/decisions.md` ; tout résultat, note ou seuil de sonde ou de moniteur du programme ;
  tout résultat d'attaque contre le juge de l'organisme ; le corps des rapports de relecture du code hors en-têtes,
  verdicts et points cités ; le devis v4 ; le reste des modules. Aucune clé. Pas de `vastai`. Aucun refus de classifieur.
- Outils : `git` (`show`, `log -S`, `diff`, `cat-file`, `fetch` à refspec explicite), `sha256sum`, `grep`, `sed`, `diff` ;
  `python3` (import de `lanceur_v9` pour lire `CHEMINS_ARCHIVE`, lecture du manifeste JSON) ; `pytest` (venv du dépôt,
  `PYTHONPATH=src`, sans `TEMOIN_BAILEY_CLONE`) sur `tests/test_temoin_bailey_condition6_v9.py` et
  `tests/test_temoin_bailey_analyse_v3.py` : **91 passés** (55 + 36), aucun sauté. (Un premier passage sans
  `PYTHONPATH=src` fait échouer `test_remarque_veilleur_recolte_jamais_signale`, dont le veilleur est un sous-processus
  qui importe le paquet : effet de mon environnement, pas du code.) Aucune modification du dépôt hors de ce rapport.

## 1. Verdict

**Scellable après corrections** (C-1 à C-9 ci-dessous, texte exact au § 6 ; aucune ne touche au code ni ne demande un
mot de Lazar). Les empreintes, le commit, les rapports, les lectures et les états des conditions de lancement sont
exacts pour l'essentiel ; aucun résultat ; aucun écart au texte scellé qui ne soit acté. Trois points de fond :
(C-1) la liste de l'archive envoyée sur l'instance est fausse ; (C-3) une limite de relecture d'`analyse_v3` n'est
pas déclarée ; (C-4) des conventions que deux rapports demandent d'écrire « dans l'addendum » n'y sont pas.

## 2. Empreintes, commit, rapports (point 1 de la demande)

- `99b59d3366f98c9c837ff280009191c50dc126da` existe, daté 2026-11-10 17:36:45 UTC, contenu dans la branche locale et
  dans `origin/claude/compassionate-meitner-d4ryyk`.
- Les sept SHA-256 de modules égalent `git show 99b59d33:src/controle_ia/temoin_bailey/<module> | sha256sum` :
  `lanceur_v9` `324dee5a…`, `instance_v8` `7e4c2dc8…`, `lecture_v8` `1657a492…`, `execution_v3` `279f1f4f…`,
  `journaliseur_v3` `9f75407c…`, `conventions_v3` `51c2fa26…`, `analyse_v3` `c28c6821…` : **tous conformes**.
  L'essai `test_temoin_bailey_condition6_v9.py` : `43736f05…`, conforme. L'essai `test_temoin_bailey_analyse_v3.py`
  n'a pas d'empreinte dans l'addendum (`8cca01f18b61f81fc805dc3c89847e997db66c05609f644a08a5929b3f440d47` au commit) :
  à ajouter (R6, C-2).
- Le seul écart entre `99b59d33` et la tête est l'addendum lui-même : le code n'a pas bougé depuis le commit cité.
- **`CHEMINS_ARCHIVE`** (`lanceur_v9`, par import) = `controle_ia/__init__.py`, `gardes.py`, `scellement.py`,
  `temoin_bailey/__init__.py`, `analyse_v3.py`, `conventions_v3.py`, `execution_v3.py`, `journaliseur_v3.py`,
  `lecture_v8.py`, `instance_v8.py`. L'addendum dit « Seuls ces fichiers de `src/` [les sept du tableau] partent sur
  l'instance (`lanceur_v9.CHEMINS_ARCHIVE`), avec le paquet `controle_ia` (`__init__`, `gardes`, `scellement`) » :
  **faux sur deux points** : `lanceur_v9.py` ne part pas (il tourne sur le poste local) ; `temoin_bailey/__init__.py`
  part et n'est pas nommé. La lecture 21 de la v7 donne la bonne liste. **C-1.**
- Onze rapports cités : chacun existe dans `docs/notes/reproduction-attaque-publiee-v1/`, son empreinte commence par le
  préfixe cité et son compagnon `.sha256` est égal. Les abréviations « `…-v3-bailey-v1.md` » et « `…-v5-…` » se
  résolvent sans ambiguïté (`relecture-differentiel-code-condition6-v3-bailey-v1.md`,
  `relecture-lignes-touchees-code-condition6-v5-bailey-v1.md`). Verdicts vérifiés : v7 « conforme » ; v8 « C-1
  bloquante » ; contrôle de C-1 : « code et essais conformes ; L-1 à L-3 », et L-1 à L-3 sont repris mot pour mot dans
  la v7 des lectures (`diff` v6 → v7 : bannière, ligne « Rapport appliqué », en-tête « Code », lecture 26, conclusion ;
  rien d'autre).
- Liste des lectures v7 : existe, `9f03ad70…` en entier, compagnon conforme.
- Code public `9c1f4b1a…` / arbre `c7cf686c…` : égaux à `conventions_v3.COMMIT_PUBLIC` / `ARBRE_PUBLIC`.
- Manifeste `e21bccf6…` : Python 3.11, 166 versions, 3 dépôts git, révisions `8afb486c…`, `4bd893d3…`, `9cf48e52…` :
  conformes (« publiés avant le 11 février 2025 » non vérifié ici).
- **« Essai sauté »** : aucun essai des deux fichiers cités n'est sauté (91 passés, `-rs` vide). L'essai d'import de
  `Llama3SoftPrompted` est `tests/test_temoin_bailey_condition6_v3.py::test_essai_manquant_7_import_llama3_soft_prompted`
  (l. 842-849), hors des fichiers cités. **C-2.**
- **Relecture d'`analyse_v3`** : la v3 applique D-1 à D-11 de `8895a5a7…`. Le seul relecteur du différentiel v2 → v3
  (`4f079ece…`, l. 29) écrit : « `analyse_v3.py` hors des fonctions nommées (les points D-3 à D-11 n'ont pas été relus
  point par point : hors demande) ». Les relecteurs suivants n'ont lu d'`analyse_v3` que `validite`, `garde_fin_de_run`,
  `nombre_de_tours`, `garde_nombre_de_tours`. Aucun rapport ne confirme D-3 à D-11 (dont D-4, `verdict` et l'audit ;
  D-6, comptes entiers ; D-7, essais R5 rétablis ; D-10, rang de `Evaluation`). L'addendum présente la chaîne comme
  complète. Pas un défaut constaté du code : une limite de la contre-lecture, à déclarer (R4 : rien de silencieux).
  **C-3** ; un contrôle court de D-3 à D-11 par un sous-agent neuf est recommandé, non exigé.
- **Conventions demandées pour l'addendum** : `151eee65…` (P-1, P-2, P-6) et `8895a5a7…` (D-9) demandent d'écrire
  **dans l'addendum** : P1 et P2 toujours calculées deux fois et « dépend des égalités » = « issues différentes » ; les
  deux conventions du rééchantillonnage (bénignes tirées avant les nuisibles, `integers(0, 200, size=(tirages, 200))` ;
  `numpy.percentile` en interpolation linéaire) ; la conversion de t en heures. `analyse_v3.py` l. 24-36 les écrit
  sous le titre « Conventions écrites ici pour l'addendum de la condition 6 » ; ni l'addendum ni la liste v7 ne les
  reprennent. **C-4.**

## 3. Fidélité aux actes de Lazar et à la liste v7 (point 2)

- « go c, go lecture B − 2 » : verbatim exact ; note `2f3e8e3a…` ; lectures 1 à 3 : exact. L'heure « ≈ 12:32 UTC » est
  juste (erratum de la passation `…-1434-…`, `54e56860…`, l. 8-9 ; la note de décision porte 12:40 par erreur), mais la
  source n'est pas citée. **C-5.**
- « go lectures, et la correction du pilote » : verbatim exact ; note `d4f21aa5…` ; lectures 4, 6, 7, 8, 13, 16, 24, 25,
  26, 31, 36 : exactement la liste de la note ; correction du pilote : exact.
- Résumé des « principales » lectures, comparé ligne à ligne à la v7 :
  - « B − 2 » (lectures 1 à 4, 24) : fidèle (3 600 s, B − 0,5, au plus tard à l'échéance, B − 1) ;
  - « Ligne de GO » : fidèle aux lectures 6 et 7 ; « texte lu sur `origin/main` » est la lecture **30**, **déclarée**,
    non actée ;
  - « Mémoire vive » (lecture 8) : fidèle ;
  - « Écart acté (lecture 16) » : fidèle ; il omet les exceptions de la lecture (« sauf "sonde orientée" tombée,
    dépense ou échéance du GO ») ; « relance selon la liste d'arrêt » les couvre, mais l'énoncé gagne à les nommer ;
  - « Ligne coupée (lecture 36) » : fidèle à (a), (d), (f) et à C-1 ;
  - « Appariement (lecture 10) » : fidèle, mais la lecture 10 est **déclarée**, non actée, et figure sous le titre
    « Lectures de lignes scellées, actées par Lazar ».
  Aucune lecture n'est ajoutée ni changée sur le fond ; deux lectures déclarées sont présentées sous un titre
  « actées ». **C-5.**
- Risques déclarés (§ 3) : conformes aux lectures 22, 32, 36. La lecture 22 dit en plus quand faire l'inventaire
  (« à chaque reprise de session et au plus tard à l'échéance du GO ») : omis. **C-8.**

## 4. Conditions de lancement (point 3)

| # | Affirmation de l'addendum | Constat |
|---|---|---|
| 1 | rempli (`fb6c2f34…`) | Exact. |
| 2 | `GO-2026-11-10-10`, `main`, `cbc9c5ce`, l. 300 ; B = 75 ; devis `f9c8c66e…` ; 30 novembre (22:59:59 UTC) ; A100 80 Go ; rempli sous réserve de la licence écrite | `cbc9c5ce` (2026-11-10 12:06:00 UTC) est le commit qui inscrit la ligne (`git log -S`), à la l. 300 ; la ligne est **identique** sur `origin/main` `09ede09f`, toujours l. 300 ; aucune révocation ne la vise ; `GO-2026-11-10-11` ne remplace que la part « organisme ». B, devis, échéance, carte : exacts. Mais la ligne exige « licence levée par écrit » parmi ses « conditions toutes exigées » : tant que la preuve manque, la ligne ne vaut pas pour ce run ; « rempli, sous réserve » est trop favorable. **C-6.** |
| 3 | « oui » 12:03 ; inscription sur `main` attendue | Verbatim et heure exacts (`85d95700…`). La note lit la condition 3 « remplie » ; la passation de 14:34 exige l'inscription sur `main` avant toute instance (la mère n'inscrit pas sur un mot relayé). L'addendum ne dit pas l'état. **C-6.** |
| 4 | « go autonome Bailey ils sont ok » ≈ 11:18 ; preuve écrite à verser | Verbatim exact (`5ae71cf3…`). La condition 4 du texte (« le mot de Lazar ») est remplie ; la preuve écrite est exigée par N-061 et par la ligne de GO. L'état n'est pas dit en un mot. **C-6.** |
| 5 | rempli — addendum 2 `73c8de01…`, commit `46a664ea` ; F-001, « go (b) », pas encore déposé | Exact : empreinte et compagnon conformes ; `46a664ea` du 10 novembre 12:36:01 UTC (« condition de lancement 5 de Bailey remplie ») ; option (c) de la note `2f3e8e3a…`. F-001 et « go (b) pour l'addendum 2 » sont dans la note de la session-dépôt `…-1310-decision-lazar-addendum2-manifeste.md` (`52990ef0…`, branche `claude/upbeat-cray-dmauvv`, heure corrigée à ≈ 16:53 UTC par `…-1654-erratum-…`) : non citée dans l'addendum (R6). **C-7.** Cette note porte une réserve : « une course du bras qui en dépend avant le dépôt le dira dans son préenregistrement » ; l'addendum la dit (« n'est daté que par son commit »). |
| 6 | rempli par cet addendum | Après C-1 à C-4 et scellement. |
| 7 | attendu | Exact. |
| 8 | « go location », autonomie totale ; `vastai` 1.11.0 (`--label`) ; jeton HF ; tokeniseur ; ordre de lancement | « go location » (`85d95700…`) et autonomie totale (`0821cb81…`) : exacts. Jeton HF vérifié : passation `…-1231-…` l. 30 et manifeste (`acces_jeton_hugging_face` : HTTP 200, ≈ 12:25 UTC). Tokeniseur et `--label` : passation `…-1434-…` l. 21 (« Établi »). **Sources non citées**, alors que la liste v7, qui « fait partie de cet addendum », porte encore les lectures 23 et 35 « à établir avant l'instance ». La lecture 35 demande aussi le champ `label` de `show instances --raw`, que la passation n'établit pas. `lanceur_v9` exige `GO_ID` dans l'environnement (l. 1098) : l'ordre doit le porter. **C-8.** |

## 5. Écarts, résultats, promesses tenues par le code (point 4)

- Aucun résultat. Seul écart au texte scellé : la lecture 16, actée comme écart par le mot de 16:57 ; la lecture 5
  (plus stricte) et les déclarées ne changent aucune issue en faveur d'un signe.
- Affirmations vérifiées par `grep` :
  - marge de 3 600 s : `MARGE_TRANSFERT_S = 3600.0` (`lanceur_v9` l. 126, `instance_v8` l. 73) ;
  - B − 2 : `analyse_v3.garde_depense` (`d ≥ b − 2`, l. 388), appelée par `instance_v8.verifier_budget` ;
    `lanceur_v9` l. 904-910, 1028, 1107 ;
  - seuil local B − 1 : `SEUIL_LOCAL_USD = 1.0` (l. 127), appliqué l. 1023 ; contrainte
    `marge_secours < seuil_local < 2` l. 1096 ;
  - secours B − 0,5 : `MARGE_SECOURS_USD = 0.5` (l. 125) ;
  - 128 × 10⁹ octets : `conventions_v3.MEMOIRE_VIVE_MIN_OCTETS = 128 * 10 ** 9` (l. 59) ; minimum de `MemTotal` × 1 024
    et de `memory.max` (`instance_v8` l. 140-157) ;
  - Paris : `FUSEAU_ECHEANCE = "Europe/Paris"` (l. 302) ;
  - `--label` : `PREFIXE_ETIQUETTE` (l. 134), `args += ["--label", etiquette]` (l. 169) ;
  - B lu sous « (B = » et texte lu sur `origin/main` : `texte_go_main` (l. 251-260), refus d'un texte différent
    (l. 1090) ;
  - `DEPOT_URL` : l. 118, porté par `ordre_de_lancement` (l. 809-812).
- Promesse implicite : l'instance reçoit `git archive` de `man["commit_code"]` (l. 627, 1105). Rien dans le code
  n'oblige ce commit à être `99b59d33`, ni la conduite locale à tourner sur les empreintes du tableau. L'addendum
  donne le commit ; il doit dire que le lancement le passe. **C-9** (précision).
- En-tête : « ≈ 17:45 UTC » ; le fichier date de 17:37:39 UTC (`stat`) et il est committé à 17:37:58 (`e8cd8d99`).
  Même classe d'erreur que la C1 de l'addendum 2. **C-9.** (En passant, hors objet : la bannière v7 de la liste des
  lectures porte « ≈ 17:40 UTC » alors que la v7 est dans le commit `99b59d33` de 17:36:45 ; pièce scellée, à ne pas
  réécrire, à signaler seulement.)
- Hors objet, à la prochaine version du code : la docstring d'`analyse_v3` (l. 18) renvoie à `lecture_v1.py` pour les
  grandeurs rapportées ; le module courant est `lecture_v8`.

## 6. Corrections exactes

- **C-1** (§ 1, l. 24-25) : remplacer « Seuls ces fichiers de `src/` partent sur l'instance (`lanceur_v9.CHEMINS_ARCHIVE`),
  avec le paquet `controle_ia` (`__init__`, `gardes`, `scellement`). » par « Partent sur l'instance, par une archive
  `git archive` du commit ci-dessus, les seuls fichiers de `lanceur_v9.CHEMINS_ARCHIVE` : `src/controle_ia/__init__.py`,
  `gardes.py`, `scellement.py`, `src/controle_ia/temoin_bailey/__init__.py` et les six modules du tableau autres que
  `lanceur_v9.py`, qui tourne sur le poste local (lecture 21). »
- **C-2** (§ 1, l. 28-32) : remplacer « et `tests/test_temoin_bailey_analyse_v3.py` (36 passés) » par « et
  `tests/test_temoin_bailey_analyse_v3.py` (36 passés,
  `8cca01f18b61f81fc805dc3c89847e997db66c05609f644a08a5929b3f440d47`) » ; et remplacer « l'import de la classe
  `Llama3SoftPrompted` (essai sauté) » par « l'import de la classe `Llama3SoftPrompted`
  (`tests/test_temoin_bailey_condition6_v3.py::test_essai_manquant_7_import_llama3_soft_prompted`, sauté hors de
  l'instance ; aucun essai des deux fichiers ci-dessus n'est sauté) ».
- **C-3** (§ 1, à la fin du paragraphe « Contre-lecture (R2) ») : ajouter « Limite déclarée : le différentiel
  `analyse_v2` → `analyse_v3` (corrections D-1 à D-11 de `8895a5a7…`) a été relu par `4f079ece…` pour D-1, D-2 et les
  fonctions `validite`, `verdict`, `garde_fin_de_run` seulement ; « les points D-3 à D-11 n'ont pas été relus point par
  point » (`4f079ece…`, en-tête) ; les relectures suivantes n'ont lu d'`analyse_v3` que `validite`, `garde_fin_de_run`,
  `nombre_de_tours` et `garde_nombre_de_tours`. » — et, si la session le choisit, un contrôle court de D-3 à D-11 par un
  sous-agent neuf, cité ici avant le scellement.
- **C-4** (nouvelle sous-section à la fin du § 2, « Conventions de l'analyse ») : « Demandées pour cet addendum par
  `151eee65…` (P-1, P-2, P-6) et `8895a5a7…` (D-9), écrites dans `analyse_v3.py` l. 24-36 au commit ci-dessus :
  P1 et P2 sont toujours calculées deux fois, égalités à τ non signalées (note > τ) puis signalées (note ≥ τ) ;
  « dépend des égalités » veut dire « issues différentes » ; R_std(0) est « sensible » si ses deux issues diffèrent ;
  la médiane d'un nombre pair de comptes se compare en entiers (somme des deux valeurs centrales ≥ 2 × 180).
  Rééchantillonnage : un seul générateur, `numpy.random.default_rng(enfant « rééchantillonnage »)` ; tours e = 0, …,
  K′ − 1 en ordre croissant et, dans chaque tour, R_att(e), R_def(e) (absent au dernier tour, sans tirage), R_std(e) ;
  aucun autre tirage ; dans chaque appel, indices des bénignes tirés avant ceux des nuisibles
  (`integers(0, 200, size=(tirages, 200))`) ; percentiles de `numpy.percentile` (interpolation linéaire, valeur
  possiblement non entière). Les mentions de l'audit se lisent sur la définition de base de R_att ; le recalcul de
  l'audit ne réemploie ni `seuil` ni `evaluer`. Règle du nombre de tours : t en secondes, c en dollars par heure,
  K = ⌊72 000 (B − R − D) / (23 c t)⌋ ; H ≤ 0 : arrêt. »
- **C-5** (§ 2) : remplacer « (`registres/passations/2026-11-10-1240-decision-lazar-noeud5-lecture-b2.md`, `2f3e8e3a…` ;
  le mot est de ≈ 12:32 UTC) » par « (`registres/passations/2026-11-10-1240-decision-lazar-noeud5-lecture-b2.md`,
  `2f3e8e3a…` ; le mot est de ≈ 12:32 UTC, erratum de la passation `2026-11-10-1434-attaquant-informe-successeur-etape.md`,
  `54e56860…`) » ; remplacer « Les principales : » par « Les principales (actées, sauf mention « déclarée ») : » ; dans la
  puce « Ligne de GO », remplacer « texte lu sur `origin/main` ; » par « texte lu sur `origin/main` (lecture 30,
  déclarée) ; » ; dans la puce « Écart acté (lecture 16) », après « (relance selon la liste d'arrêt) », insérer « , sauf
  « sonde orientée » tombée, dépense ou échéance du GO » ; remplacer « **Appariement** (lecture 10) » par
  « **Appariement** (lecture 10, déclarée) ».
- **C-6** (§ 4) : condition 2, remplacer « **Rempli**, sous réserve de la licence écrite que la ligne exige. » par
  « Ligne inchangée sur `origin/main` `09ede09f` (`GO-2026-11-10-11` ne remplace que la part « organisme »).
  **Non remplie pour ce run tant que la licence écrite que la ligne exige n'est pas versée** (condition 4). » ;
  condition 3, remplacer « **Inscription sur `main` attendue** » par « Mot : rempli. **Inscription sur `main`
  attendue avant toute instance** » ; condition 4, avant « **preuve écrite des auteurs** », insérer « mot : rempli ; ».
- **C-7** (§ 4, condition 5) : remplacer « (file de la session-dépôt, F-001, mot de Lazar « go (b) »), pas encore
  déposé. » par « (file de la session-dépôt, F-001, mot de Lazar « go (b) pour l'addendum 2 », ≈ 16:53 UTC :
  `registres/passations/2026-11-10-1310-decision-lazar-addendum2-manifeste.md`, `52990ef0…`, et son erratum
  `…-1654-erratum-heure-addendum2.md`, branche `claude/upbeat-cray-dmauvv`), pas encore déposé. »
- **C-8** (§ 4, condition 8) : remplacer « Vast.ai joignable, `vastai` 1.11.0 (`--label` présent) ; jeton Hugging Face
  avec accès aux deux modèles à accès contrôlé (Llama-3-8B-Instruct, `google/gemma-2b`, base de l'adaptateur du juge) ;
  tokeniseur présent dans le dépôt de l'adaptateur. L'ordre de lancement cite le GO, B, le taux relevé et
  `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`. » par « Vast.ai joignable, `vastai` 1.11.0, option
  `--label` présente et tokeniseur présent dans le dépôt de l'adaptateur (établis : passation
  `2026-11-10-1434-attaquant-informe-successeur-etape.md`, `54e56860…`, l. 21 ; ils lèvent les « à établir » des
  lectures 23 et 35 de la liste v7, sauf le champ `label` de `vastai show instances --raw`, à vérifier avant la
  création) ; jeton Hugging Face avec accès aux deux modèles à accès contrôlé (Llama-3-8B-Instruct, `google/gemma-2b`,
  base de l'adaptateur du juge ; HTTP 200, ≈ 12:25 UTC, manifeste `e21bccf6…` et passation `…-1231-…`, `ee3fb47c…`).
  L'ordre de lancement cite le GO, `GO_ID` (exigé dans l'environnement par la conduite), B, le taux relevé,
  l'étiquette de l'instance et `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`. » ; et au § 3, puce
  « Poste local éteint », remplacer « inventaire par l'étiquette unique de l'instance (`--label`) et arrêt par
  identifiant (R10). » par « inventaire par l'étiquette unique de l'instance (`--label`), à chaque reprise de session et
  au plus tard à l'échéance du GO, et arrêt par identifiant (R10). »
- **C-9** : l. 3, remplacer « ≈ 17:45 UTC » par « ≈ 17:37 UTC » (ou l'heure `date -u` du scellement, dite comme
  telle) ; au § 1, après « **Commit du code : `99b59d33…`** (…), branche ci-dessus. », ajouter « Le lancement passe ce
  commit comme `commit_code` (archive envoyée sur l'instance) et la conduite locale tourne sur un arbre où les sept
  modules ont les empreintes ci-dessous. »

Après C-1 à C-9 : scellable, sans nouvelle contre-lecture de l'addendum (contrôle par `diff` suffisant).
