# Contre-lecture, tour 1, de l'addendum de relance de l'idée 1.2 (brouillon 1) — v1

- **Pièce relue** : `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon1.md`
  (`26aa0713419ecff1cbb2cd4240e17dfdc0aea9902e66e4f2c9020560ed50fdd3`), égale à son compagnon ; première contre-lecture,
  lecture entière (541 lignes) ; inchangée à la fin de ma lecture. Ci-dessous « la pièce » ; **[T]** et **[AE]** comme
  dans la pièce (`bdabf2bc…790e` et `1b96cf06…beee`, tous deux égaux à leurs compagnons).
- **Contre-lecteur** : lecteur neuf (R2), sous-agent de la session mère, lancé pour cette seule contre-lecture. Je n'ai
  écrit ni la pièce, ni [T], ni [AE], ni le code, ni aucune pièce de l'idée 1.2. R-2973 annonce un auteur « du modèle A »
  et « un lecteur du modèle B » : je ne peux attester moi-même ni la lettre de mon modèle, ni qu'il diffère de celui de
  l'auteur ; la mère l'inscrit (§ 6, point 9).
- **Dates (UTC, `date -u`)** : 2026-11-16, de 12:16:44Z à 12:55:27Z.
- **Dépôt** : `main`, tête `96958c4c` à mon arrivée, `1332acb3` au rejeu de l'annexe A de la pièce, `60eee4e5` à la
  fin (la mère a versé pendant ma lecture) ; les 34 fichiers gelés sont restés égaux (annexe B, [B1]). Aucun commit,
  aucune poussée, aucun fichier existant modifié de ma main.
- **Lu** : la pièce en entier ; [AE] en entier ; [T] l. 1-60 et l. 425-672 (graines, étapes, critères de lecture, liste
  d'arrêt, coût, écarts, contre-lectures, annexes), le reste par recherche de mots (addendum, relance, invalide,
  24 heures) ; en entier : `scripts/jouer_idee_1_2_v2.py`, `scripts/lire_idee_1_2_v2.py`, et, sous
  `src/controle_ia/`, `organisme_idees_juge/execution_v2.py`, `execution_v1.py`, `banc_tirages_repartis_v1.py`,
  `juge_v1.py`, `oracle_v1.py`, `oracle_v2.py`, `lire_banc_tirages_repartis_v2.py`, `mutations_v2.py`, `manifeste.py`,
  `gardes.py`, `scellement.py`, `prereg.py` ; en partie : `mutations_v1.py` (l. 20-135), `rejeu_v1.py` (l. 195-317) ; par
  recherche des sources de hasard et d'horloge seulement : `lois_v1.py`, `synthetique_v1.py`,
  `verificateur_texte_v2.py`, `lire_banc_tirages_repartis_v1.py` et les dix modules de la copie du juge que charge
  `juge_v1.py` ; `registres/decisions.md`, lignes R-2951, R-2964, R-2973, R-1103, R-1105, R-1463, R-2910, R-2851 ;
  `registres/go.md`, en-tête et ligne GO-2026-11-16-01.
- **Non fait** : aucun fichier du run invalide ouvert (leurs octets ne sont passés que par `sha256sum -c`) ; ni jeu, ni
  essais, ni `pytest` ; aucun appel réseau ; rien écrit dans `/home/user/jeu-idee-1-2-copie`, ni sous `diag/`, `runs/`,
  `donnees/` du dépôt principal.
- **Verdict : « corrections »** — 2 majeures, 11 mineures (17 couples exigés), et 3 couples facultatifs. **La conception
  n'est pas en cause.**

## 1. Verdict

1. **Le fond tient.** La qualification « run invalide » sous [T] l. 512 est la bonne lecture ; les preuves de l'annexe A
   se rejouent à l'identique ; « mêmes tirages » est confirmé par le code (aucune seconde chance sur un autre tirage,
   R3) ; les conditions de la relance sont conformes à [T] et à [AE] ; l'argument « l'oracle invalide a le contenu de
   l'oracle neuf » est exact ; rien ne change un critère, un seuil, une graine ni le plan. **La lecture (iv) de la mère
   est juste : la relance n'est pas un écart et ne demande pas de mot nouveau du directeur** (§ 2, point 7).
2. **Deux corrections majeures.** (M1) La consigne d'opérateur du § 5 prescrit une attente « avec le plus long délai que
   permet le harnais » : c'est le contraire de la décision (vi) de la mère, et c'est la forme que les heures des
   fichiers de la nuit montrent avant la perte du conteneur (deux sorties de tâches de fond à deux heures d'écart, la
   seconde non suivie d'une autre ; annexe B, [B3]). (M2) La décision (v) — jeu relancé en même temps que le jeu de
   l'idée 1.1 — manque, avec ses conséquences sur la durée et sur la borne de 24 heures.
3. **Onze corrections mineures** : les décisions (i), (ii) et (iv) à écrire comme décisions ; l'instant de l'arrêt
   (≈ 04:36Z d'après les journaux de la session, non 06:13Z) ; le nombre de reprises du conteneur (trois au moins) ; un
   incident de l'auteur à déclarer (verrou d'index posé dans la copie par son `git status`) ; la présence de l'addendum
   dans la copie neuve, que rien ne contrôle ; l'espace disque (0,86 Go libre à 12:39Z) ; une phrase trop forte ; la
   section « Contre-lecture ».

## 2. Les huit points à vérifier

### (1) Cause et qualification « run invalide » — conforme ; deux précisions

- **Lettre.** [T] l. 512 : « exception, log W non fini | arrêt du run ; aucune lecture partielle ; relance seulement sous
  un texte ou un addendum neuf (R5) ». [T] l. 513 (durée murale > 24 h) et l. 514 (lecture avant scellement, oracle
  calculé après le rejeu) ne décrivent pas ce cas. La pièce a raison : [T] n'a pas de ligne propre à un arrêt venu de
  l'extérieur, et les mots « run invalide » viennent de [AE] l. 114-115, qui les pose sur [T] l. 512.
- **La ligne 512 est la bonne**, pour quatre raisons : (a) c'est la ligne des fins anormales en cours de marche
  (« exception »), quand les lignes 513 et 514 visent deux causes précises qui ne sont pas celle-ci ; (b) [AE]
  l. 111-115 range déjà sous elle un arrêt provoqué du dehors (TERM de l'opérateur au parent), avec les mots « run
  invalide » ; (c) le code lui-même attache cette règle à tout arrêt (`execution_v1.py` l. 271) et refuse
  toute relance en présence d'une sortie antérieure avec les mêmes mots, quelle qu'en soit la cause (lanceur l. 74) ;
  (d) des deux lectures possibles — « aucune ligne ne s'applique, relance libre » et « l. 512, relance sous addendum,
  aucune lecture » — c'est la plus stricte. Le mot « la plus prudente » de la pièce est acceptable ; « la plus proche,
  lue du côté le plus strict » serait plus exact (couple facultatif f3).
- **Un addendum, non un texte neuf : c'est ce qui garde les tirages.** La racine est l'entier de l'empreinte « du texte
  qui fera foi » ([T] l. 451 ; `banc_tirages_repartis_v1.py` l. 37 et 61-64). Un texte neuf aurait une autre empreinte,
  donc d'autres tirages : la voie de l'addendum est aussi la bonne au regard de R3 (couple facultatif f2).
- **Précision 1 — l'instant de l'arrêt.** La cause déclarée (reprise du conteneur pendant une période d'inactivité de
  la session) est cohérente avec tout ce que j'ai relevé, mais le redémarrage de ≈ 06:13Z est celui de la reprise de la
  session, non l'instant de l'arrêt. D'après les seules heures de modification des fichiers (aucun ouvert ; annexe B,
  [B3]) : dernière sortie de tâche de fond de la session à 04:31:41Z ; dernières écritures des journaux de la session à
  04:36:02Z ; puis plus rien sur tout le disque avant 06:13:16Z. Le conteneur s'est donc très probablement arrêté vers
  04:36Z, et le jeu avec lui : ≈ 4 h 06 min après son lancement, non 5 h 43 min comme le compte le point 4 du § 2. La conclusion de la
  pièce (« le jeu n'avait vraisemblablement pas fini ») en sort renforcée ; son chiffre est à corriger (m4). La
  qualification n'en dépend pas, comme la pièce le dit.
- **Précision 2 — une phrase trop forte.** « Aucune garde de la liste d'arrêt ne l'a arrêté » ne se prouve pas : le
  point 4 du même § 2 admet que l'état sur disque n'exclut pas le parent bloqué de [AE] l. 106-115, cas où une garde a
  joué sans pouvoir écrire. Ce qui est établi : aucun arrêt n'est consigné, ni `arret.json`, ni ligne au journal (m9).

### (2) Les preuves — confirmées

- **Rejeu du programme de l'annexe A.** Programme et sortie extraits de la pièce, octet pour octet : empreintes égales
  à celles que la pièce cite (`02d193c5…a8de`, `a634334f…8214`) et à celles des deux fichiers d'origine dans le dossier
  de travail de l'auteur. Rejoué le 2026-11-16 à 12:21:47Z, dans un sous-dossier neuf à moi du bloc-notes, par
  `python3 -I -B`, avec `GIT_OPTIONAL_LOCKS=0` (voir l'incident ci-dessous). **Sortie égale à celle de la pièce, à cinq
  lignes près** : les deux heures, la tête de `main`, la durée de marche de la machine, les deux empreintes des
  registres à la tête nouvelle (annexe A).
- **Les 34 empreintes gelées** : 34 sur 34 égales sur l'arbre du dépôt, sur les objets de `main` et sur l'arbre de la
  copie ; empreinte du bloc `b6e724a4…39d2`, égale ; aucune différence entre `2753ecf2` et `main` sur ces chemins.
  Contrôle indépendant, par `sha256sum -c` sur la liste extraite de [AE], refait à 12:39:18Z sur la tête `9f55173c` : 34
  conformes dans le dépôt, 34 conformes dans la copie (annexe B, [B1]).
- **Les trois fichiers du run invalide**, vérifiés par `sha256sum -c` depuis leur dossier, sans être ouverts : trois
  fois « OK » ; tailles et heures égales au tableau du § 2 de la pièce (9 489, 10 076 et 13 505 894 octets ; 00:38:05,
  00:53:28, 01:22:37). **Absents** : `jeu.json`, `journal.json`, `arret.json`, `lecture-gelee-v2.json`. Journal du
  lanceur : 0 octet (annexe B, [B2]).
- **Incident de l'auteur, à déclarer dans la pièce (m7).** Le `git status` de son programme, joué dans la copie sans
  `--no-optional-locks`, y a posé puis retiré un verrou d'index : le dossier `.git` de la copie porte l'heure de
  modification 12:06:35.456Z, celle de son programme. L'index lui-même n'a pas changé (4 218 874 octets, 00:29:54.087Z),
  ni l'arbre de travail. Mon rejeu, sans verrou facultatif, a laissé ce dossier à la même heure (vérifié avant et
  après). Sans conséquence sur les trois fichiers ; mais la condition du § 6 (« ni modifiée ») doit dire comment on
  joue une commande git de lecture dans la copie.
- **« Par élimination »** (interpréteur du run invalide) : l'argument tient. Le lanceur tourne en mode isolé (`-I`) et
  importe scipy ; outre les interpréteurs du système que l'auteur a relevés, je n'ai trouvé sur la machine que deux
  environnements Python (celui du dépôt et `vastai-env` ; recherche bornée, annexe B, [B5]), et seul celui du dépôt
  porte scipy et pytest.

### (3) « Mêmes tirages » — confirmé par le code

- **Ce qui fait les graines** : la racine est `int(EMPREINTE_PREREG, 16)`, constante du code gelé égale à l'empreinte
  de [T] (`banc_tirages_repartis_v1.py` l. 37, 61-64 ; lanceur l. 145 ; l'égalité du fichier de [T] à cette constante
  est exigée au départ, lanceur l. 59-63 et 133) ; chaque générateur est
  `SeedSequence(entropy=racine, spawn_key=clé)` (banc l. 67-70), les clés étant faites des seuls entiers famille,
  génération, carte et numéro de flux (banc l. 83, 107, 144, 191, 240, 370, 394, 418-420 ; `rejeu_v1.py` l. 210-211 et
  297 ; `synthetique_v1.py` l. 59 et 130 ; rééchantillonnage `(99, b)`).
- **Ce qui dépend du run et n'entre dans aucune graine** : le nom du run (lanceur l. 132) et l'empreinte du manifeste ne
  servent qu'à l'en-tête des sorties (`execution_v1.py` l. 96) ; l'heure de départ ne sert qu'à la garde des 24 heures
  (`debut`, `execution_v2.py` l. 109, 142) et aux durées consignées ; l'empreinte de l'oracle scellé est recopiée dans
  la sortie, sans plus (`execution_v1.py` l. 148-170) ; le commit et l'addendum ne vont qu'au manifeste et aux
  contrôles (lanceur l. 142-154) ; le PID n'est lu nulle part ; l'identifiant d'un engagement est
  `idee12-f{f}-g{g}-c{i}` (banc l. 402), sans nom de run. Le champ `graines` du manifeste dérive de la même racine et
  d'un nom de tâche fixe (`manifeste.py` l. 37-48) ; il n'alimente aucun tirage.
- **Copie du juge** : ses tirages viennent de graines dérivées par empreinte ou de constantes (`nul_v8.py` l. 156) ; le
  seul hasard libre que j'y ai trouvé (`cycle.py` l. 392, tirage du noyau secret) est dans le constructeur du cycle réel,
  que le banc n'appelle pas : il n'emploie de `cycle` que `instants_reguliers` et `appliquer_multiplicite`, et évalue
  sous le plan « ordre_naturel », sans graine de noyau (banc l. 304-306, 336-337). Aucun parcours d'ensemble dont l'ordre
  dépendrait du hachage, ni dans le banc ni dans ces modules ; `imap` rend les résultats dans l'ordre des tâches
  (`execution_v2.py` l. 91), donc indépendamment du nombre de processus.
- **Banc de mutations** : racines d'essai fixes (`mutations_v1.py` l. 27, 33, 58, 119) et, pour le jeu synthétique, la
  racine du texte sous les clés `(97, g)` et `(99, b)`.
- **Conséquence pour R3** : la relance refait les mêmes tirages ; elle n'offre aucune seconde chance sur un autre
  tirage, et le moment du lancement ne peut rien changer. Confirmé.
- **Limite, que la pièce ne dit pas** (couple facultatif f1) : « au bit près » demande aussi le même processeur (numpy
  choisit ses noyaux de calcul selon lui) ; la machine a été reprise trois fois depuis le run invalide. Les graines n'en
  dépendent pas ; seule l'égalité du dernier bit de calculs flottants en dépendrait. Processeur relevé à 12:50Z : le
  même modèle que dans [AE] § 5 (annexe B, [B5]).

### (4) Conditions de la relance — conformes ; deux manques

- **Mêmes fichiers gelés** : oui (point 2) ; le lanceur refait le contrôle (l. 139).
- **Copie propre neuve** : oui ; l'ancienne serait refusée deux fois (arbre non propre, l. 134 ; sortie antérieure,
  l. 135). `main` ne porte aucun chemin suivi sous `runs/` ou `diag/organisme-idees-juge-v1/` au nom de ce jeu
  (vérifié) : une copie de `main` passera la garde de la ligne 135. Les dix fichiers d'essais gelés ne parcourent pas
  `prereg/` (recherche) : le fichier neuf sous `prereg/` ne change pas leur issue.
- **Commit noté, PID noté** : oui (4.4, 4.5).
- **Commande** : exacte ; nommer l'interpréteur par son chemin est une précision, non un écart (le manifeste consigne de
  toute façon la chaîne fixe de la ligne 154 du lanceur).
- **`--addendum`** : le lanceur lit le fichier que nomme l'argument (l. 138-139), en consigne chemin et empreinte
  (l. 142-143, 150), et rien d'autre. **Il refuserait l'addendum de relance** : la pièce ne porte aucune ligne au
  format lu (compté : 0), les 34 fichiers seraient « absents de la liste », `GardeArret` à la ligne 139, avant les
  essais (l. 144). Ce refus tient au contenu seul : le lanceur accepterait tout fichier scellé qui porterait les 34
  lignes. La version scellée doit donc garder zéro ligne de cette forme ; mes couples n'en ajoutent pas (annexe C) ; à
  recompter après le remplissage de « Contre-lecture ».
- **Contrôle des versions** (décision (iii)) : présent (4.2) ; commande rejouée telle quelle à 12:50Z :
  `3.13.18 2.4.6 1.17.1` (annexe B, [B5]).
- **Borne de 24 heures par run** : conforme au code (garde créée au départ du lanceur, l. 130 ; limite
  `execution_v1.py` l. 29).
- **Manque 1 (m8)** : rien ne contrôle que la copie neuve porte bien l'addendum de relance ; le lien entre le run et
  l'addendum n'est que le commit. Une vérification d'une ligne avant le lancement ferme la boucle.
- **Manque 2 (m11)** : l'espace disque. Une copie propre occupe ≈ 2,8 Go ; à 12:39Z le disque n'avait que 0,86 Go
  libre (98 % de ≈ 39 Go), et 7,7 Go à 12:46Z après l'effacement de dossiers de travail par la session (annexe B,
  [B4]). Un disque plein en cours de jeu lèverait une exception : un second run invalide.

### (5) Consigne d'opérateur neuve et seconde interruption — une majeure, une mineure

- **M1.** Le § 5 demande une attente « avec le plus long délai que permet le harnais ». La décision (vi) dit
  l'inverse : une attente qui se termine d'elle-même avant la limite de l'outil, réarmée à chaque fin. Les heures des
  fichiers appuient la mère : deux sorties de tâches de fond de 10 octets à 02:31:14Z et à 04:31:41Z, à deux heures
  d'écart, puis aucune tâche de fond ; journaux de la session arrêtés à 04:36:02Z, quatre minutes après (annexe B,
  [B3]). Lecture, que la mère confirme sur son propre journal : deux attentes menées à la limite de l'outil, la seconde
  non réarmée. Le reste de la consigne est bon (qui la tient ; ni rappel ni relève ne la remplacent ; un sous-agent fini
  ne la tient pas ; ce que la consigne n'exclut pas). L'exemple du couple M1 est éprouvé sur cette machine : code 124
  quand l'attente expire, code 0 quand le processus guetté finit (annexe B, [B5]).
- **m5.** Le constat est à compléter : trois reprises au moins depuis le lancement (≈ 06:13Z, ≈ 07:09Z, ≈ 11:24Z), et
  ce qu'est devenue l'attente n'est pas « non consigné » : les heures des fichiers le disent.
- **Seconde interruption** : la règle est bonne (run invalide, aucune lecture, un addendum de relance de plus, mêmes
  tirages, chaque run invalide rapporté). Elle n'ouvre aucune relance d'avance, chaque relance demandant son propre
  addendum. Remarque facultative F6.

### (6) Fichiers du run invalide — l'argument tient ; la voie (a) protège la lecture gelée

- **Le contenu de l'oracle.** `oracle.json` est `{run_id, manifeste_sha256, resultat: {generations: [tables]}}`
  (`execution_v1.py` l. 96 ; `execution_v2.py` l. 163-164). Chaque table vient de `Generation(racine, famille, g)` et de
  `oracle_v2.table_oracle` : génération, effectif, empreinte de l'échantillon, meilleur membre, valeurs des membres,
  gain et classe de chaque carte, résumé de la construction, membres à la borne triviale — tout cela fonction de la
  racine seule — plus `duree_s`. **Hors du nom du run, de l'empreinte du manifeste et des durées, l'oracle invalide a
  bien le contenu de l'oracle neuf** (sous la réserve du dernier bit, point 3). L'ouvrir avant la lecture gelée du run
  neuf reviendrait à lire le run neuf avant le scellement de sa sortie ([T] l. 514).
- **La voie (a) protège-t-elle ?** Oui, tant que la règle « personne ne les ouvre » est tenue : hors du dépôt, les
  fichiers ne sont sur aucune branche, aucun outil du dépôt ne les parcourt (la vérification de l'arbre ne lit que le
  dépôt principal), et le lecteur gelé refuse ce run avant de rien charger (pas de `journal.json`). La voie (b) les
  exposerait sur le dépôt distant avant le prononcé. La décision (ii) est fondée.
- **Ce que la pesée de la pièce ne dit pas (m11-b)** : la voie (a) retient l'ancienne copie entière, ≈ 2,8 Go, sur un
  disque de ≈ 39 Go qui était plein à 98 % pendant ma lecture.
- **À écrire** : la décision (ii) comme décision (m3) ; trois reprises et non deux (m6) ; la règle des commandes git
  dans la copie (m7-b).

### (7) Rien ne change ; la relance demande-t-elle un mot du directeur ? — non

- **Rien ne change** un critère, un seuil, une graine, une étape ni une ligne de la liste d'arrêt de [T], ni un fichier
  gelé, une empreinte, un écart ou une réserve de [AE]. Ce que la pièce ajoute est du côté strict : une qualification,
  une interdiction de lecture, un contrôle des versions qui peut seulement empêcher un lancement, une consigne
  d'opérateur, le sort de fichiers. La phrase de préséance du § 1 (« [T] puis [AE] l'emportent ») est bonne.
- **La lecture (iv) de la mère est juste.** (a) Aucune dépense : processeur seul, travail de routine dans la hiérarchie
  de décision. (b) Les seuls écarts au texte, E-1 et E-2, sont acceptés par la ligne GO-2026-11-16-01, point 4, qui
  ordonne aussi le « jeu sur processeur » ; son échéance est le 2026-11-22. (c) La relance sous un addendum neuf est le
  chemin que [T] l. 512 écrit lui-même : suivre un texte scellé n'est pas s'en écarter. (d) [T] ne demande pas de GO
  neuf. Le précédent d'A1-v3 (R-1103, R-1463 : « texte nouveau et GO nouveau ») tenait au texte scellé de cette
  course-là et à sa dépense ; il ne se transpose pas. (e) Rien n'a été lu, et les tirages sont les mêmes.
- **Nuance à écrire** (elle est dans le couple m2) : ranger un arrêt venu de l'extérieur sous [T] l. 512 est une lecture
  du texte, faite du côté le plus strict, non un écart ; [AE] § 3 a consigné de la même façon des lectures du texte sans
  mot du directeur. Lazar la trouve au registre et dans le rapport du run neuf.
- **La concurrence avec l'idée 1.1** n'est pas un écart non plus : [T] l. 473 borne les processus de ce jeu, et [AE]
  § 5 décrivait une machine partagée ; la durée attendue n'est pas un critère, seule la borne de 24 heures en est un
  ([AE] l. 138-139 le dit du coût écrit au texte).

### (8) Empreintes, identifiants de modèle, section « Contre-lecture »

- **Empreintes citées**, toutes vérifiées par `sha256sum` : [T] ; [AE] ; `registres/decisions.md` et `registres/go.md`
  aux objets de la tête `d4b81652` (`7025e985…b3c3`, `b46dcde2…b98a`) ; les trois fichiers du run invalide ; le bloc
  des 34 lignes ; la liste de la copie du juge (`0153e02d…32df`) ; le programme et la sortie de l'annexe A ; les commits
  `d4b81652…3805` et `2753ecf2…8cc8` existent et sont ceux que dit la pièce. Lignes citées de [T], de [AE], du code et
  des registres : exactes (rejeu de l'annexe A, sections [6] à [8], et lecture).
- **Identifiants de modèle** : aucun dans la pièce (recherche sans casse).
- **Section « Contre-lecture »** : « À REMPLIR » ; texte proposé au couple m10.

## 3. Les six décisions de la mère dans la pièce

| décision | dans la pièce | correction |
|---|---|---|
| (i) nom `…-addendum-relance-v1.md`, « v2 » de R-2964 erreur de plume | nom présent (l. 16) ; mais « à confirmer par elle » (l. 18) | m1 |
| (ii) voie (a) jusqu'au prononcé du run neuf | écrite comme recommandation (confiance 0,65) avec une variante | m3 (trois couples) |
| (iii) contrôle des versions gardé | présent (4.2, troisième puce) | aucune |
| (iv) pas de mot nouveau du directeur | laissé ouvert (« s'il faut le lui redemander, la mère en juge ») | m2 |
| (v) jeu relancé en même temps que le jeu de l'idée 1.1 | **absente** | **M2** |
| (vi) attente qui finit d'elle-même avant la limite de l'outil, réarmée à chaque fin | **forme contraire** (« le plus long délai que permet le harnais ») | **M1** |

## 4. Corrections exigées — couples « ancien → nouveau »

Chaque « ancien » est le texte exact de la pièce entre les deux lignes de clôture, retours à la ligne et espaces de
début de ligne compris ; il figure **une seule fois** dans la pièce, et les couples ne se chevauchent pas (contrôle par
programme, annexe C). Les couples s'appliquent dans n'importe quel ordre. Deux « nouveau » portent des mots à remplacer
par la mère : m10 (empreinte du rapport, traitement) ; m5 porte une lecture que la mère confirme ou corrige avant le
scellement (§ 6, point 2).

**M1** (majeure) — § 5, « Consigne » (décision (vi) de la mère) ; lignes 194 à 198 de la pièce.

Ancien :

```text
elle arme une attente en arrière-plan suivie par le harnais, qui
  rend la main à la fin du parent (par exemple `tail --pid=<PID> -f /dev/null`, avec le plus long délai que permet le
  harnais), et la réarme dans le tour même où elle rend la main, tant que le parent vit. Ni un rappel programmé ni une
  relève périodique ne la remplacent ; un sous-agent qui a fini ne la tient pas. L'attente ne cesse qu'après la fin du
  parent (`journal.json` ou `arret.json` écrit, ou parent disparu).
```

Nouveau :

```text
elle arme une attente en arrière-plan suivie par le harnais, qui
  **se termine d'elle-même avant la limite de durée de l'outil**, que le parent ait fini ou non (par exemple
  `timeout <secondes> tail --pid=<PID> -f /dev/null`, la durée choisie sous cette limite : code 0, le parent a fini ;
  code 124, l'attente a expiré), et **la réarme à chaque fin**, dans le tour même où elle rend la main, tant que le
  parent vit. L'attente n'est jamais laissée jusqu'à la limite de l'outil, qui l'arrêterait ; faute de tâche active, le
  conteneur peut être repris (constat). Ni un rappel programmé ni une relève périodique ne la remplacent ; un sous-agent
  qui a fini ne la tient pas. La suite des attentes ne cesse qu'après la fin du parent (`journal.json` ou `arret.json`
  écrit, ou parent disparu).
```

**M2** (majeure) — paragraphe 4.10 neuf, inséré avant le titre du § 5 (décision (v) de la mère) ; lignes 184 à 184 de la pièce.

Ancien :

```text
## 5. Consigne d'opérateur neuve : une tâche active pendant tout le jeu
```

Nouveau :

```text
**4.10 Machine partagée avec le jeu de l'idée 1.1 (décision de la mère).** Le run neuf tournera en même temps que le jeu
de l'idée 1.1, sur la même machine à 4 processeurs logiques : deux processus de calcul pour l'idée 1.2 (4.6), trois au
plus pour l'idée 1.1 (son texte scellé, étape 3), tous à `nice -n 10`. [T] ne l'interdit pas (l. 473 : deux processus au
plus pour ce jeu) et [AE] § 5 décrivait déjà une machine partagée et chargée : ce n'est ni un écart ni un critère.
Conséquences :

- **tirages et calculs** : aucune ; ni la charge ni le nombre de processus n'entrent dans une graine (4.2) ; seules
  changent les durées consignées dans les sorties ;
- **durée** : jusqu'à cinq processus de calcul de même priorité pour quatre processeurs logiques, soit 4/5 d'un
  processeur chacun au mieux ; chaque phase de calcul prend alors au moins 1,25 fois sa durée sur machine libre (total
  ≈ 3 à 5,5 h selon [AE] l. 137, soit ≈ 3,75 à 6,9 h au moins). La durée dans cette configuration n'a pas été mesurée ; repère :
  ≈ 6 à 7,5 h sous la charge plus forte du jour des mesures de [AE] (charge moyenne de 10 à 13, l. 130-137) ;
- **borne de 24 heures** ([T] l. 513) : inchangée, comptée depuis le lancement du run neuf (4.7) ; sur le repère de
  7,5 h, la marge reste de trois fois environ. Si la borne était franchie, la garde arrêterait le run ([T] l. 513 :
  arrêt, run invalide), sans aucune lecture ;
- **consigne du fils oisif** ([AE] l. 111-115) : elle se lit avec ces durées ; TERM au parent, par son PID, seulement si
  `journal.json` n'est pas écrit à la durée attendue **et** si les processus du run n'emploient plus le processeur ;
- **ordre** : le run neuf ne part pas pendant l'étape 0 de l'idée 1.1, dont le chronométrage est sensible à la charge
  (R-2964 : relance après elle).

## 5. Consigne d'opérateur neuve : une tâche active pendant tout le jeu
```

**m1** (mineure) — en-tête, « Statut et lieu » (décision (i) de la mère) ; lignes 17 à 18 de la pièce.

Ancien :

```text
R-2964 l'annonce comme « addendum de relance v2 » : second addendum de [T], il est le premier de
  relance, d'où `-relance-v1` dans le nom retenu par la mère (R12) ; à confirmer par elle.
```

Nouveau :

```text
R-2964 l'annonçait comme « addendum de relance v2 » : erreur de plume de la mère, reconnue par
  elle ; second addendum de [T], il est le premier de relance, d'où `-relance-v1` (R12), **nom confirmé par la mère**.
```

**m2** (mineure) — § 4.9 (décision (iv) de la mère) ; lignes 180 à 182 de la pièce.

Ancien :

```text
Le mot de Lazar qui fait lancer ce jeu
(GO-2026-11-16-01, point 4) porte sur le jeu, que la relance rejoue à l'identique ; s'il faut le lui redemander, la mère
en juge. Le moment du lancement relève de la mère (R-2964 : relance après l'étape 0 de l'idée 1.1).
```

Nouveau :

```text
**La relance ne demande pas de mot nouveau
de Lazar (décision de la mère)** : elle ne dépense rien ; les seuls écarts au texte, E-1 et E-2, sont acceptés
(GO-2026-11-16-01, point 4 : « écarts E-1 et E-2 acceptés, jeu sur processeur à lancer », échéance 2026-11-22) ; la
relance sous un addendum neuf est ce que [T] l. 512 prescrit, et [T] ne demande pas de GO neuf (à la différence du texte
scellé d'A1-v3, course à dépense : R-1103) ; cet addendum ne déclare aucun écart. Ranger l'arrêt venu de l'extérieur
sous [T] l. 512 est une lecture du texte, faite du côté le plus strict (§ 2) ; Lazar la trouve au registre (R-2964,
R-2973) et dans le rapport du run neuf (4.8). Le moment du lancement relève de la mère (R-2964 : relance après l'étape 0
de l'idée 1.1 ; 4.10).
```

**m3-a** (mineure) — § 6, première ligne (décision (ii) de la mère) ; lignes 207 à 207 de la pièce.

Ancien :

```text
Trois fichiers, leurs compagnons (§ 2) et le journal vide. Deux voies.
```

Nouveau :

```text
Trois fichiers, leurs compagnons (§ 2) et le journal vide. Deux voies ont été pesées ; **la mère a retenu la
voie (a)** (R-2973) : fichiers laissés scellés et non lus dans la copie jusqu'au prononcé du run neuf.
```

**m3-b** (mineure) — § 6, « Recommandation » (décision (ii) de la mère) ; lignes 230 à 230 de la pièce.

Ancien :

```text
**Recommandation : (a)**, confiance 0,65.
```

Nouveau :

```text
**Décision de la mère : voie (a)** (R-2973), sur la recommandation du rédacteur (confiance 0,65).
```

**m3-c** (mineure) — § 6, « Variante acceptable » (décision (ii) de la mère) ; lignes 235 à 236 de la pièce.

Ancien :

```text
**Variante acceptable** : (a) jusqu'au prononcé du run neuf, puis (b) si la mère veut une trace durable ; le risque de
contamination est alors nul, et la règle « personne ne les ouvre » demeure.
```

Nouveau :

```text
**Après le prononcé du run neuf**, la voie (b) reste ouverte si la mère veut une trace durable : le risque de
contamination est alors nul, et la règle « personne ne les ouvre » demeure.
```

**m4** (mineure) — § 2, point 4 (instant de l'arrêt) ; lignes 80 à 81 de la pièce.

Ancien :

```text
À 06:13Z, environ 5 h 43 min s'étaient écoulées depuis le lancement, moins que la durée totale attendue sous charge
   (6 à 7,5 h, [AE] l. 137) : le jeu n'avait vraisemblablement pas fini.
```

Nouveau :

```text
Le redémarrage de ≈ 06:13Z est celui de la reprise de la session : il ne borne l'instant de l'arrêt que par le haut.
   D'après les seules heures de modification des fichiers de la machine (aucun n'est ouvert ; contre-lecture du tour 1,
   annexe B), la dernière sortie de tâche de fond de la session est écrite à 04:31:41Z, les journaux de la session
   s'arrêtent à 04:36:02Z, et plus rien n'est écrit sur le disque avant 06:13:16Z : le conteneur s'est très
   probablement arrêté vers 04:36Z, ≈ 4 h 06 min après le lancement ; la phase « jeu » durait alors depuis ≈ 3 h 13 min
   (4 h 50 min si l'arrêt n'était venu qu'à 06:13Z), pour 2,3 à 4,7 h attendues sur machine libre et davantage sous
   charge ([AE] l. 136-137). Le jeu n'avait vraisemblablement pas fini ; l'état sur disque ne permet pas de l'affirmer.
```

**m5** (mineure) — § 5, « Constat » (redémarrages, sort de l'attente) ; lignes 187 à 190 de la pièce.

Ancien :

```text
Le conteneur de ce jeu a redémarré vers
  06:13Z (R-2964), puis de nouveau vers 11:24:01Z (annexe A, [5] ; cause de ce second redémarrage non établie ici). Au
  lancement, la surveillance était tenue par une attente en arrière-plan de la mère (R-2951) ; ce qu'elle était devenue
  à 06:13Z n'est pas consigné.
```

Nouveau :

```text
Le conteneur de ce jeu a redémarré vers
  06:13Z (R-2964) et vers 11:24Z (annexe A, [5]) ; d'après les noms et les heures des journaux de la session (non
  ouverts ; contre-lecture du tour 1, annexe B), la session a tourné du 15 novembre 20:13:13Z au 16 novembre 04:36:02Z,
  de 06:13:17Z à 06:37:47Z, de 07:09:55Z à 07:14:53Z, puis depuis 11:24:08Z : trois reprises au moins depuis le
  lancement (causes de celles de 07:09Z et de 11:24Z non établies ici). Au lancement, la surveillance était tenue par
  une attente en arrière-plan de la mère (R-2951) ; d'après les heures et les tailles des sorties de tâches de fond de
  la session (non ouvertes), deux sorties de 10 octets sont écrites à 02:31:14Z et à 04:31:41Z, à deux heures d'écart,
  et aucune tâche de fond n'est armée ensuite (lecture : deux attentes menées jusqu'à la limite de l'outil, la seconde
  non réarmée) ; les journaux de la session s'arrêtent quatre minutes plus tard, à 04:36:02Z. Une session sans tâche
  active peut donc perdre son conteneur en quelques minutes.
```

**m6** (mineure) — § 6, voie (a), « Contre » (nombre de redémarrages) ; lignes 215 à 215 de la pièce.

Ancien :

```text
ils ont survécu à deux redémarrages (06:13Z, 11:24Z), mais
```

Nouveau :

```text
ils ont survécu à trois redémarrages au moins (≈ 06:13Z, ≈ 07:09Z, ≈ 11:24Z ; § 5), mais
```

**m7-a** (mineure) — § 3, deuxième puce (incident du verrou d'index, à déclarer) ; lignes 94 à 95 de la pièce.

Ancien :

```text
Rien d'autre n'a été ouvert ; rien n'a été lu ni
  écrit sous `diag/` ou `runs/` du dépôt principal.
```

Nouveau :

```text
Rien d'autre n'a été ouvert ; rien n'a été lu ni
  écrit sous `diag/` ou `runs/` du dépôt principal. **Incident déclaré** : le `git status` du programme de l'annexe A,
  joué dans la copie sans `--no-optional-locks`, y a posé puis retiré un verrou d'index à 12:06:35Z (heure de
  modification du dossier `.git` de la copie) ; l'index (4 218 874 octets, 00:29:54Z) et l'arbre de travail n'ont pas
  changé. Tout rejeu de ce programme se fait avec `GIT_OPTIONAL_LOCKS=0` (rejeu du contre-lecteur à 12:21:47Z : même
  sortie, dossier `.git` inchangé).
```

**m7-b** (mineure) — § 6, « Conditions » (commandes git dans la copie) ; lignes 232 à 233 de la pièce.

Ancien :

```text
ni modifiée (aucune
commande git qui écrit, aucun lancement) jusqu'au prononcé du run neuf ;
```

Nouveau :

```text
ni modifiée (aucune
commande git qui écrit, aucun lancement ; toute commande git de lecture y est jouée avec `--no-optional-locks` ou
`GIT_OPTIONAL_LOCKS=0`, pour ne poser aucun verrou d'index) jusqu'au prononcé du run neuf ;
```

**m8** (mineure) — § 4.4 (présence de l'addendum dans la copie neuve ; relevés consignés) ; lignes 153 à 153 de la pièce.

Ancien :

```text
Le commit est noté au registre avant le lancement ; le manifeste le consigne.
```

Nouveau :

```text
Avant le lancement, l'opérateur vérifie dans la copie neuve que cet addendum y est, égal à son
compagnon (`sha256sum -c` depuis `prereg/`) : le lanceur ne le contrôle pas (4.6). Le commit, l'empreinte de cet
addendum, la sortie du contrôle des versions (4.2) et l'espace libre sont notés au registre avant le lancement ; le
manifeste consigne le commit.
```

**m9** (mineure) — § 2, « Qualification », dernière phrase ; lignes 86 à 87 de la pièce.

Ancien :

```text
Aucune garde de la liste d'arrêt ne l'a arrêté : la relance n'est ni
une reprise après un défaut, ni une seconde tentative après un essai échoué.
```

Nouveau :

```text
Aucun arrêt par une garde n'est consigné (ni `arret.json`, ni ligne au
journal du lanceur) ; le seul cas que l'état sur disque n'exclut pas est celui du parent bloqué de [AE] l. 106-115
(point 4). La relance n'est ni une reprise après un défaut constaté, ni une seconde tentative après un essai échoué :
aucun résultat n'a été lu (§ 3) et les tirages sont les mêmes (§ 4.2).
```

**m10** (mineure) — section « Contre-lecture » ; lignes 240 à 241 de la pièce.

Ancien :

```text
À REMPLIR — par un lecteur neuf, qui n'a écrit ni ce brouillon ni aucune pièce de l'idée 1.2 : texte relu (chemin et
empreinte entière), rapport (chemin et empreinte entière), verdict, traitement de chaque remarque.
```

Nouveau :

```text
- **Contre-lecture 1** (R2) — lecteur neuf, sous-agent de la session mère (lettre du modèle : inscrite par la mère), qui
  n'a écrit ni ce brouillon ni aucune pièce de l'idée 1.2 ; texte relu : brouillon 1,
  `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon1.md`,
  `26aa0713419ecff1cbb2cd4240e17dfdc0aea9902e66e4f2c9020560ed50fdd3` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-relance-idee-1-2-tour1-v1.md` (empreinte entière : celle
  de son compagnon, recopiée ici par la mère) ; programme de l'annexe A rejoué le 2026-11-16 à 12:21:47Z sur la tête
  `1332acb3` de `main` : même sortie, aux heures, à la tête et aux empreintes des registres près. Verdict :
  « corrections » (2 majeures, 11 mineures). **Traitement** : écrit par la mère, remarque par remarque.
```

**m11-a** (mineure) — § 4.4, alinéa neuf à la suite (espace disque) ; lignes 154 à 154 de la pièce.

Ancien :

```text
Journal sous un nom neuf (proposé : `/home/user/jeu-idee-1-2-relance-v1.log`), jamais l'ancien (R12).
```

Nouveau :

```text
Journal sous un nom neuf (proposé : `/home/user/jeu-idee-1-2-relance-v1.log`), jamais l'ancien (R12).

**Espace disque (précaution d'opérateur, neuve).** Une copie neuve occupe ≈ 2,8 Go (arbre de travail ; les objets git
sont liés, non recopiés) et l'ancienne copie reste en place (§ 6) ; le disque offert à la session (≈ 39 Go) est passé
par ≈ 0,86 Go libre le 2026-11-16 à 12:39Z, puis ≈ 7,7 Go à 12:46Z, des dossiers de travail ayant été effacés
entre-temps (`df` ; contre-lecture du tour 1, annexe B). Avant de créer la copie, l'opérateur relève et consigne
l'espace libre ; s'il faut de la place, il la libère **ailleurs que dans `/home/user/jeu-idee-1-2-copie`** ; pas de
lancement si, la copie faite, il reste moins de 1 Go libre : un disque plein en cours de jeu lèverait une exception,
donc un run invalide de plus ([T] l. 512). Ce seuil est une précaution, non un critère.
```

**m11-b** (mineure) — § 6, voie (a), « Contre » (coût en disque, absent de la pesée) ; lignes 218 à 218 de la pièce.

Ancien :

```text
une commande git qui écrit, jouée par erreur dans la copie, pourrait les y porter.
```

Nouveau :

```text
une commande git qui écrit, jouée par erreur dans la copie, pourrait les y porter ; la copie
  entière reste en place : ≈ 2,8 Go d'arbre de travail retenus sur un disque de ≈ 39 Go (4.4).
```

## 5. Remarques facultatives

Trois couples prêts, que la mère prend ou laisse :

**f1** (facultative) — § 4.2, troisième puce (limite du « bit près ») ; lignes 138 à 139 de la pièce.

Ancien :

```text
non sur
  les lois tirées).
```

Nouveau :

```text
non sur
  les lois tirées) ;
- **limite déclarée** : numpy choisit ses noyaux de calcul selon le processeur ; sur un autre modèle de processeur, le
  dernier bit de certains calculs flottants pourrait changer ; les graines, elles, ne dépendent que de [T]. Processeur
  relevé le 2026-11-16 à 12:50Z : Intel Xeon à 2,10 GHz, 4 processeurs logiques, comme [AE] § 5 ; celui du run invalide
  n'est consigné nulle part ailleurs. « Au bit près » s'entend sous cette réserve ; « mêmes graines, mêmes tirages » n'en
  dépend pas.
```

**f2** (facultative) — § 4.2 (pourquoi un addendum et non un texte neuf) ; lignes 121 à 121 de la pièce.

Ancien :

```text
la même pour tout run de [T] ;
```

Nouveau :

```text
la même pour tout run de [T] (un texte neuf, d'une autre empreinte, aurait changé la racine, donc
les tirages : c'est l'addendum qui les garde) ;
```

**f3** (facultative) — § 2, « Qualification » (mot plus exact) ; lignes 84 à 84 de la pièce.

Ancien :

```text
la ligne la plus prudente, [T] l. 512 :
```

Nouveau :

```text
la ligne la plus proche, lue du côté le plus strict, [T] l. 512 :
```

Sans couple :

- **F4 — une preuve directe de « mêmes tirages », après le prononcé.** Une comparaison par programme des deux oracles,
  qui n'afficherait qu'un verdict d'égalité hors nom du run, empreinte du manifeste et durées, prouverait par le fait
  ce que le § 4.2 établit par le code. La pièce l'interdit pour toujours (§ 3 : « ni avant ni après » ; 4.2 : « comparer
  leurs contenus est interdit ») et fait de toute exception un nœud de Lazar. Si la mère veut cette preuve, c'est
  maintenant qu'il faut l'écrire comme permise après le prononcé, ou la demander à Lazar ; sinon elle sera un écart.
- **F5 — deux chaînes d'attentes décalées.** La nuit du run, quatre minutes ont suffi entre la fin de la dernière tâche
  et l'arrêt de la session. Deux attentes armées avec un décalage (la fin de l'une tombe au milieu de l'autre) laissent
  une tâche active même si un réarmement manque, et donnent une seconde occasion de réarmer.
- **F6 — portée de « seconde interruption ».** Dire que la règle vise un arrêt venu de l'extérieur, sans `arret.json` ;
  un arrêt consigné par le lanceur relève de [T] l. 512 avec sa cause à établir d'abord (R4, R5), et, si le code doit
  changer, d'un autre addendum d'empreintes. Après une seconde interruption, la question d'une machine qui ne dépende
  pas de la session se poserait : une dépense, donc un devis et un GO ; à porter alors à Lazar comme réserve.
- **F7 — essais bornés en temps.** Deux essais gelés portent une borne de temps (`tests/test_organisme_idees_juge_execution_v2.py`
  l. 61 et 68 : 30 s et 15 s). Sous la charge de deux jeux, un échec donnerait « pas de jeu » ([T] l. 506) avant tout
  manifeste : aucun run n'existerait ; la cause serait à établir et à consigner avant toute nouvelle tentative, jamais
  un essai rejoué jusqu'à ce qu'il passe. Risque faible (les mêmes essais ont passé sous une charge moyenne de 10 à 13,
  [AE] § 5 et § 6).
- **F8 — la règle « personne n'ouvre » est plus stricte que [T] pour le manifeste**, qui ne porte aucun résultat
  (`manifeste.py` l. 98-111). Acceptable ; à savoir si un jour la mère veut y lire les versions du run invalide.
- **F9 — en-tête.** Ajouter à la recopie sous `prereg/` une ligne « corrections après contre-lecture » (date, tête de
  `main`), puisque l'en-tête dit le dépôt lu à la tête `d4b81652`.
- **F10 — registres.** R-2964 porte « addendum de relance v2 » : une ligne neuve le corrige (les registres ne se
  réécrivent pas). `registres/arrets.md` n'a aucune ligne pour ce jeu tué par l'infrastructure ; le précédent R-1103
  en avait inscrit une.

## 6. Points pour la mère

1. **Lecture (iv) : juste.** La relance n'est pas un écart ; pas de mot nouveau du directeur. À écrire dans la pièce avec
   ses raisons et sa nuance (m2).
2. **Consigne (vi) : la pièce dit le contraire** (M1). Les heures des fichiers te donnent raison ; je n'ai ouvert aucun
   de ces fichiers, et ma lecture (« deux attentes menées à la limite de deux heures, la seconde non réarmée ; session
   arrêtée quatre minutes après ») est à confirmer sur ton propre journal avant de sceller le couple m5. Si tu la
   corriges, garde les heures, qui sont des faits.
3. **Instant de l'arrêt : ≈ 04:36Z, non 06:13Z** (m4). Le jeu a tourné ≈ 4 h 06 min. Trois reprises du conteneur depuis
   (m5, m6).
4. **Disque.** 0,86 Go libre à 12:39Z (98 % de ≈ 39 Go), 7,7 Go à 12:46Z après des effacements. À compter : la copie
   neuve de l'idée 1.2 (≈ 2,8 Go), l'ancienne, que la voie (a) retient jusqu'au prononcé (≈ 2,8 Go), la copie et les
   sorties du jeu de l'idée 1.1, les sorties recopiées dans le dépôt. Un disque plein en cours de jeu = une exception =
   un run invalide. Précaution au couple m11-a ; le seuil de 1 Go est une proposition, fixe le tien. **Variante de la
   voie (a), si la place manque** : garder en place les six fichiers du run invalide et effacer les seuls fichiers
   suivis de l'ancienne copie (recopie du commit `2753ecf2`, que git redonne) ; cela libère ≈ 2,8 Go mais change la
   condition « ni modifiée » du § 6 : ta décision, à écrire avant le scellement. Une seconde interruption retiendrait
   une copie de plus (§ 5 de la pièce : « ses fichiers suivent le § 6 »).
5. **Concurrence (v)** : à déclarer aussi, par symétrie, dans l'addendum de l'idée 1.1 (trois processus, borne de
   48 heures, durée exigée ≤ 32 heures « pour la charge des autres sessions »). Le run neuf ne part pas pendant une
   étape 0 de l'idée 1.1.
6. **Limite d'usage de la session** (précédent R-1463 : cinq heures) contre un jeu attendu entre ≈ 3,75 et 7,5 heures
   (couple M2) : la pièce la déclare parmi ce que la consigne n'exclut pas ; rien ne la couvre.
7. **Zéro ligne au format du lanceur** dans la version scellée : à recompter après le remplissage de « Contre-lecture »
   (`grep -cE '^[0-9a-f]{64}  \S+\s*$'` doit rendre 0), sans quoi le lanceur ne refuserait plus cet addendum passé par
   erreur.
8. **Incident de l'auteur** : verrou d'index posé puis retiré dans l'ancienne copie à 12:06:35Z ; index et arbre
   inchangés (m7).
9. **Lettre du modèle** : je ne peux pas l'attester ; inscris-la au couple m10. Si mon modèle était celui de l'auteur,
   la contre-lecture « par un autre modèle » de R-2851 ne serait pas tenue.
10. **Facultatif** : F4 (comparaison des deux oracles après le prononcé, à décider maintenant), F5 (deux chaînes
    d'attentes), F10 (registres).

## 7. Incidents et gestes de ma main

- **Deux `git status` dans le dépôt principal sans `--no-optional-locks`** (vers 12:16Z et 12:22Z) : verrou d'index
  facultatif, posé et retiré ; aucun effet relevé (l'index a été réécrit ensuite par les commits de la mère). Mes autres
  commandes git n'ont lu que des objets, les dernières avec `--no-optional-locks` ; dans la copie, les seules commandes
  git sont celles du rejeu, jouées sans verrou facultatif.
- **Parcours du disque, par les seules heures et tailles des fichiers** (`find`, `du`, à la priorité la plus basse) :
  `find` vers 12:25Z (quelques secondes) et à 12:33:36Z (5 s) ; `du` à 12:30:27Z (6 s), 12:30:43Z (1 s) et 12:35:18Z
  (1 s) ; `find` et `du` à 12:39:30Z et 12:39:48Z (≈ 1 s chacun). Une vingtaine de secondes d'un processeur en tout, sur
  une machine à quatre processeurs. **Une étape 0 de l'idée 1.1 tournait au début de ma lecture** (PID 612, un
  processus à la priorité 10 : vu à 12:21Z après 55 minutes de marche, absent à 12:29Z) : ont pu la croiser mon rejeu du
  programme de l'annexe A (12:21:47Z, une seconde, sept démarrages d'interpréteur), le premier `find` et le `sha256sum`
  des trois fichiers (12:27:20Z). Je tiens ces commandes pour légères ; si ce chronométrage se joue à la seconde, la mère
  le sait désormais. À partir de 12:46Z (un processus de calcul neuf à la priorité 10, que je n'ai pas identifié), plus
  aucun parcours du disque : seulement la commande du contrôle des versions (12:50:27Z), une liste d'objets git,
  l'épreuve d'une seconde de l'attente bornée (12:53:33Z), les petits programmes d'assemblage de ce rapport (quelques
  démarrages de l'interpréteur du système, moins d'une seconde chacun) et le scellement.
- **Empreintes de deux fichiers du dossier de travail de l'auteur** (son programme et sa sortie) calculées par
  `sha256sum`, pour les comparer à celles que cite la pièce ; rien d'autre n'y a été lu ni touché.
- **Noms, tailles et heures relevés, rien d'ouvert** : les sorties de tâches de fond de la session, les journaux de
  l'outil de la session et de son gestionnaire d'environnement (annexe B, [B3]). Ces fichiers ne sont pas à moi ; je
  n'en ai lu que ce que rend `ls`.
- **Fichiers du run invalide** : lus par `sha256sum -c` (trois passes : mon rejeu du programme de l'annexe A, puis deux
  fois à la main) ; leurs trois compagnons affichés une fois (une empreinte et un nom chacun). Rien d'autre.
- **Deux fichiers de travail à moi effacés de ma main**, dans mon sous-dossier du bloc-notes, pour ménager le disque :
  une liste d'heures de fichiers (16 Mo, `ce9680df…f83c`) et un extrait du registre à la tête `d4b81652` (3,5 Mo,
  `7025e985…b3c3`, l'objet de git). Aucun autre effacement ; aucun dossier d'un autre agent touché.
- **Commande du contrôle des versions du § 4.2** jouée une fois (lecture des métadonnées de trois paquets).
- **Rapport réassemblé avant le scellement** : les écritures précédentes de ce fichier (la première à 12:52:47Z),
  non scellées, ont été remplacées de ma main (retouches de forme, un exemple éprouvé en plus).
- **Rien d'autre** : aucun processus arrêté, aucun commit, aucune poussée, aucune valeur de clé lue, aucun appel réseau.

## Annexe A — rejeu du programme de l'annexe A de la pièce

Programme extrait de la pièce (`02d193c536eae1c534f2c2cffdefe1968587dbc7aac1fe45ff8b0987723ba8de`), joué tel quel le
2026-11-16 à 12:21:47Z par `GIT_OPTIONAL_LOCKS=0 python3 -I -B verifier_relance_idee_1_2_v1.py` ; code de sortie 0 ;
sortie d'erreur vide ; empreinte de la sortie :
`028f5b12d6b24ba5128ade5e203349127485c7be6c7c9e0ef016ad6958cd775b` ; 140 lignes comme celle de la pièce. Différences
avec la sortie recopiée dans la pièce (`diff`), en entier :

```text
1,2c1,2
< début (date -u) : 2026-11-16T12:06:35Z
< tête de main : d4b81652d936d6d3fd620cd4260d367a0fa83805
---
> début (date -u) : 2026-11-16T12:21:47Z
> tête de main : 1332acb3ddc7da197a224288473ed45a0432faae
41c41
< /proc/uptime : 2554 s à 2026-11-16T12:06:35+00:00 ; démarrage ≈ 2026-11-16T11:24:01+00:00
---
> /proc/uptime : 3467 s à 2026-11-16T12:21:48+00:00 ; démarrage ≈ 2026-11-16T11:24:01+00:00
130c130
< registres/decisions.md (objet de main d4b81652) : 7025e9857afd71a855a29aab3b1726865d3b246b148a3f5baaa6c54fdd05b3c3
---
> registres/decisions.md (objet de main 1332acb3) : 1a3b77ae2d95dc2e90b59d0ac8d41671dda962c5ed375a7686d8e1e38ec68c70
137c137
< registres/go.md (objet de main d4b81652) : b46dcde26612137d593100a135e698480034e0eef1f2a62c1d004bc71554b98a
---
> registres/go.md (objet de main 1332acb3) : 4bcec4a0408499477babb133f7184a159928ca2f35c5bc3188666e5a81264568
140c140
< fin (date -u) : 2026-11-16T12:06:36Z
---
> fin (date -u) : 2026-11-16T12:21:48Z
```

Dossier `.git` de la copie avant et après le rejeu : modification 2026-11-16 12:06:35.456176105 +0000 (inchangée) ;
index : 2026-11-16 00:29:54.086563935 +0000 (inchangé).

## Annexe B — relevés du contre-lecteur (commandes légères)

Dans les chemins, `<session>` est le dossier de la session sous `/tmp`, `<cache>` et `<projet>` ses dossiers de cache et
de projet ; le nom de l'outil de la session y est remplacé par `<outil>`. Hors du dépôt, je n'ai ouvert aucun fichier,
sauf les trois compagnons `.sha256` de la copie (une empreinte et un nom chacun). Les fichiers de ces relevés sont dans
mon sous-dossier du bloc-notes (éphémère) ; ils sont recopiés ici en entier.

**[B1] Les 34 fichiers gelés, par `sha256sum -c` sur la liste extraite de [AE]** (`grep -E '^[0-9a-f]{64}  \S+\s*$'`) :

```text
== [B1] 2026-11-16T12:39:18Z tête de main et fichiers gelés
9f55173c2a91a7bb01c44b249f4b9a0a1d1e67da
34
b6e724a48fa3a57a28819c052ed68fcbd7ce95302283c0fbb5416b2b6fc239d2
arbre du dépôt : 34 conformes (sha256sum -c)
git diff 2753ecf2 → HEAD sur les 34 chemins : aucune différence
arbre de la copie du run invalide : 34 conformes (sha256sum -c)
lignes au format du lanceur dans la pièce : 0
tail (GNU coreutils) 9.4
timeout (GNU coreutils) 9.4
chemins suivis sous runs/ et diag/organisme-idees-juge-v1/ au nom du jeu, à la tête b95014a8 : 0
```

**[B2] Les trois fichiers du run invalide** (`sha256sum -c` depuis leur dossier ; `stat` ; `test -e`) :

```text
== [B2] 2026-11-16T12:39:48Z fichiers du run invalide : sha256sum -c depuis leur dossier, noms, tailles, heures (rien d'ouvert)
manifeste.json: OK
controles-avant-jeu.json: OK
oracle.json: OK
9489 octets | modif 2026-11-16 00:38:05.061519248 +0000 | runs/20261116-002954-idee-1-2-tirages-repartis-v1/manifeste.json
10076 octets | modif 2026-11-16 00:53:28.547248521 +0000 | diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/controles-avant-jeu.json
13505894 octets | modif 2026-11-16 01:22:37.486751977 +0000 | diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/oracle.json
jeu.json : absent
journal.json : absent
arret.json : absent
lecture-gelee-v2.json : absent
0 octets | modif 2026-11-16 00:29:54.090804109 +0000 | /home/user/jeu-idee-1-2.log
dossier .git de la copie : modif 2026-11-16 12:06:35.456176105 +0000
index de la copie : 4218874 octets, modif 2026-11-16 00:29:54.086563935 +0000
```

**[B3] Chronologie de la nuit par les heures de modification** (`find / -xdev -type f -newermt … ! -newermt …` ; `ls`
sur les sorties de tâches de fond et sur les journaux ; aucun fichier ouvert) :

```text
== [B3] 2026-11-16T12:39:30Z heures de modification, sans rien ouvrir
-- fichiers modifiés sur tout le disque entre 03:31 et 06:15 (find / -xdev -type f -newermt … ! -newermt …) :
2026-11-16 04:31:41 10 <session>/tasks/bogxc3813.output
2026-11-16 04:36:02 286350 /tmp/environment-manager-3488510393.diag.log
2026-11-16 04:36:02 3506 <cache>/mcp-logs-<outil>-Docs/2026-11-15T20-13-13-295Z.jsonl
2026-11-16 04:36:02 516418 /tmp/<outil>-code-2556456768.diag.log
2026-11-16 04:36:02 5259 <cache>/mcp-logs-github/2026-11-15T20-13-13-295Z.jsonl
2026-11-16 04:36:02 8211 <cache>/mcp-logs-<outil>-code-remote/2026-11-15T20-13-13-295Z.jsonl
2026-11-16 06:13:16 144774 /root/.<outil>/backups/.<outil>.json.backup.1794809596694
2026-11-16 06:14:43 116301 <projet>/tool-results/mcp-<outil>-code-remote-list_events-1794809683371.txt
-- sorties de tâches de fond de la session, du 16 novembre de 00:25 à 06:25 (heure, octets) :
00:25:47 500;00:25:47 500;00:25:53 1528;00:29:45 219;00:29:47 219;00:32:01 130;00:35:51 28;00:36:26 130;00:38:24 623;00:39:04 130;00:43:42 22;00:46:31 70;00:47:11 130;00:47:11 2008;00:47:54 124;00:52:07 130;00:54:09 130;00:56:31 22;01:05:35 100;01:05:35 130;02:31:14 10;02:31:40 130;03:29:34 130;03:29:34 29;03:29:37 173;03:29:38 51;04:31:41 10;06:20:55 130;
-- journaux d'un connecteur de la session (nom = démarrage ; heure = dernière écriture) :
2026-11-15T07-16-18-827Z.jsonl -> 2026-11-15 19:44:47
2026-11-15T20-13-13-295Z.jsonl -> 2026-11-16 04:36:02
2026-11-16T06-13-17-323Z.jsonl -> 2026-11-16 06:37:47
2026-11-16T07-09-55-870Z.jsonl -> 2026-11-16 07:14:53
2026-11-16T11-24-08-278Z.jsonl -> 2026-11-16 11:24:13
-- journaux du gestionnaire d'environnement (heure de dernière écriture) :
2026-11-15 00:04:30 92692
2026-11-15 00:42:14 2092
2026-11-15 02:37:10 2097
2026-11-15 03:31:47 2505
2026-11-15 19:44:47 759709
2026-11-16 04:36:02 286350
2026-11-16 06:37:47 2373
2026-11-16 07:14:53 1960
2026-11-16 12:38:13 4296
-- /proc/uptime :
4530 s
2026-11-16T12:39:31Z
```

Lecture : la session a tourné du 15 novembre 20:13:13Z au 16 novembre 04:36:02Z ; sa dernière sortie de tâche de fond
est de 04:31:41Z, deux heures après la précédente de même taille (02:31:14Z) ; rien n'est écrit sur le disque entre
04:36:02Z et 06:13:16Z ; la session reprend à 06:13:17Z, s'arrête à 06:37:47Z, reprend à 07:09:55Z, s'arrête à
07:14:53Z, reprend à 11:24:08Z. Durées : 00:29:50Z → 04:36:02Z = 4 h 06 min 12 s ; 01:22:37Z → 04:36:02Z = 3 h 13 min
25 s ; 01:22:37Z → 06:13:00Z = 4 h 50 min 23 s. Compte par minute des fichiers modifiés sous `/home/user` et sous
`<session>` entre 03:30 et 06:18 (premier relevé, vers 12:25Z) : 03:30, 24 ; 04:31, 1 ; 06:15, 10 ; 06:16, 20 707 ;
06:17, 5 723 ; rien entre 03:31 et 04:30, ni entre 04:32 et 06:14.

**[B4] Disque, mémoire, charge** (`df`, `stat -f`, `du --exclude=.git`, `/proc`) :

```text
== [B4] 2026-11-16T12:39:48Z disque et mémoire
1M-blocks Used Avail Use%; 258020 38513 859 98%;
blocs de 4096 octets : total 66053021 ; libres 56193705 ; disponibles hors réserve 219672
rw,relatime,discard,no_prefetch_block_bitmaps,resv_strict,resuid=65534,resgid=65534
2822 Mo, arbre de travail sans .git : /home/user/jeu-idee-1-2-copie
2810 Mo, arbre de travail sans .git : /home/user/etape0-idee-1-1-copie
MemTotal: 16473776 kB;MemAvailable: 15299248 kB;
4
1.21 1.39 1.29 2/121 8025
== [B4 bis] 2026-11-16T12:46:02Z disque, après l'effacement de dossiers de travail par la session
1M-blocks Used Avail Use%; 258020 31661 7711 81%;
/home/user/controle-ia-travail/ /home/user/etape0-idee-1-1-copie-v5/ /home/user/jeu-idee-1-2-copie/ /home/user/lciric/ /home/user/pilote-mr2-v74-envoi-v12/ /home/user/pilote-mr2-v74-envoi-v13/ /home/user/pilote-mr2-v74-envoi-v14/ /home/user/pilote-mr2-v74-envoi/ /home/user/vastai-env/ 
uptime 4921 s
2.29 1.69 1.41 4/125 11001
  PID  NI %CPU     ELAPSED COMMAND
 1736  19 98.6       15:32 python
10919  10 98.3       00:08 python
```

Relevés d'espace libre pendant ma lecture (`df`, Mo) : 12:30:02Z, 857 ; 12:35:19Z, 845 ; 12:39:48Z, 859 ; 12:45:15Z,
9 411 ; 12:45:23Z, 8 787 ; 12:46:02Z, 7 711. Entre 12:39Z et 12:45Z ont disparu deux dossiers du bloc-notes (4 681 Mo
et 4 081 Mo à 12:35Z) et `/home/user/etape0-idee-1-1-copie` ; `/home/user/etape0-idee-1-1-copie-v5` est apparu. Je n'y
suis pour rien.

**[B5] Interpréteur et processeur** :

```text
== [B5] 2026-11-16T12:50:27Z interpréteur (commande du § 4.2 de la pièce, telle quelle) et processeur
3.13.18 2.4.6 1.17.1
model name : Intel(R) Xeon(R) Processor @ 2.10GHz
processeurs logiques : 4
jeux d'instructions (extrait) : fma avx2 avx512f 
environnements Python trouvés (pyvenv.cfg, profondeur 5 sous /home /opt /usr/local /root /srv /tmp, relevé de 12:24Z environ) : /home/user/vastai-env ; /home/user/controle-ia-travail/.venv
== [B5 bis] 2026-11-16T12:53:33Z exemple d'attente bornée du couple M1, éprouvé (GNU coreutils 9.4)
timeout 1 tail --pid=<interpréteur de commandes vivant> -f /dev/null  → code 124 (attente expirée)
timeout 5 tail --pid=<processus de 0,3 s> -f /dev/null  → code 0 (processus fini)
```

## Annexe C — contrôle des couples

Programme `couples_v1.py`, dans mon sous-dossier du bloc-notes
(`8d07d9cba6ba6ed3d59888ab1d7c6d93df3093236a8b3a3866e07e1df3dfad50`) : il découpe chaque « ancien » dans la pièce,
exige qu'il y figure une seule fois, qu'aucun couple n'en chevauche un autre, qu'aucun « nouveau » ne porte une ligne au
format du lanceur ni le marqueur « À REMPLIR », puis applique en mémoire les 17 couples exigés et recompte. Les blocs du
§ 4 et du § 5 sont écrits par ce programme, non recopiés à la main. Sortie
(`0361bb1e36a529f0707c0b72669f4147fb70ed1f97669f8fd65e517a2ac68471`), en entier :

```text
pièce : 26aa0713419ecff1cbb2cd4240e17dfdc0aea9902e66e4f2c9020560ed50fdd3
M1 (majeure) : ancien trouvé 1 fois, lignes 194 à 198, 488 caractères ; nouveau 796 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
M2 (majeure) : ancien trouvé 1 fois, lignes 184 à 184, 71 caractères ; nouveau 1869 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m1 (mineure) : ancien trouvé 1 fois, lignes 17 à 18, 187 caractères ; nouveau 213 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m2 (mineure) : ancien trouvé 1 fois, lignes 180 à 182, 259 caractères ; nouveau 767 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m3-a (mineure) : ancien trouvé 1 fois, lignes 207 à 207, 70 caractères ; nouveau 211 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m3-b (mineure) : ancien trouvé 1 fois, lignes 230 à 230, 41 caractères ; nouveau 97 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m3-c (mineure) : ancien trouvé 1 fois, lignes 235 à 236, 194 caractères ; nouveau 185 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m4 (mineure) : ancien trouvé 1 fois, lignes 80 à 81, 188 caractères ; nouveau 815 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m5 (mineure) : ancien trouvé 1 fois, lignes 187 à 190, 309 caractères ; nouveau 1038 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m6 (mineure) : ancien trouvé 1 fois, lignes 215 à 215, 58 caractères ; nouveau 88 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m7-a (mineure) : ancien trouvé 1 fois, lignes 94 à 95, 100 caractères ; nouveau 548 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m7-b (mineure) : ancien trouvé 1 fois, lignes 232 à 233, 92 caractères ; nouveau 225 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m8 (mineure) : ancien trouvé 1 fois, lignes 153 à 153, 77 caractères ; nouveau 353 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m9 (mineure) : ancien trouvé 1 fois, lignes 86 à 87, 145 caractères ; nouveau 374 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m10 (mineure) : ancien trouvé 1 fois, lignes 240 à 241, 215 caractères ; nouveau 818 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m11-a (mineure) : ancien trouvé 1 fois, lignes 154 à 154, 101 caractères ; nouveau 882 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
m11-b (mineure) : ancien trouvé 1 fois, lignes 218 à 218, 82 caractères ; nouveau 187 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
f1 (facultative) : ancien trouvé 1 fois, lignes 138 à 139, 27 caractères ; nouveau 522 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
f2 (facultative) : ancien trouvé 1 fois, lignes 121 à 121, 30 caractères ; nouveau 145 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
f3 (facultative) : ancien trouvé 1 fois, lignes 84 à 84, 39 caractères ; nouveau 65 caractères ; ligne au format du lanceur dans le nouveau : non ; marqueur à remplir : non
couples : 20 ; chevauchement : aucun
après application des couples exigés (en mémoire seulement) : lignes au format du lanceur : 0 ; « À REMPLIR » : 0 ; « à confirmer par elle » : 0 ; « plus long délai » : 0 ; « 4.10 » : 1 ; longueur : 53132
fragment écrit : fragment-couples-v1.md f8bd1876551baef61094d73a6015c06702792b92e0bd4194218260d0b4b853dc
```
