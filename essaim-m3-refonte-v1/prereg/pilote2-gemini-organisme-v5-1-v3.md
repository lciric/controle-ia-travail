# Préenregistrement — second pilote descriptif : l'organisme écrit par Gemini (v5.1), seul, sur la banque scellée `confrontation-v1`, moisson ouverte, en deux courses avec une question ouverte posée à la génération 1 — v3

Remplace la v2 (`pilote2-gemini-organisme-v5-1-v2.md`, `0d718031733e4f27bb8593e8dab773acf175e7a7a909dd3b655a217a901b9241`,
gardée, R12), contre-lue (contre-lecture 2 : sous-agent neuf, 25 octobre 2026, 10:18–10:38 UTC, rapport
`prereg/contre-lectures/pilote2-gemini-organisme-v5-1-v2-cl2.md`,
`1b513a0eb8838f9eda9c960b5fddbf8ba9b46e1794e00ed1352cb7b0bba39903` ; verdict « scellable après corrections » ; 14 constats
de la contre-lecture 1 traités, dont 4 en partie ; 10 constats nouveaux P2C2-01 à P2C2-10, traités en fin de texte), qui
remplaçait la v1 (`pilote2-gemini-organisme-v5-1-v1.md`, `51d1b2246f1cb1c8104d5101963697af99b6d9102a15af86f67eba6660a3e75f`),
contre-lue (contre-lecture 1 : sous-agent neuf, 25 octobre 2026, 09:39–10:01 UTC, rapport
`prereg/contre-lectures/pilote2-gemini-organisme-v5-1-v1-cl1.md`,
`688b1e21f0a7972cc2e9982e557139ecd8929a4990926d50ec7b64a3497011a8` ; verdict « scellable après corrections » ; 14
constats P2C1-01 à P2C1-14). Second pilote après celui de l'objet v4
(`pilote-gemini-organisme-v4-question-v3.md`, `1c5b6f7db90caa1c5527f207fcc034163257459104f4d2b9a01d33df25eed79a`,
branche `outils/essaim-m3-gradient-v1-travail`, commit `2d01805a7c314ffd4ab72b46ea359dad483c298b`), parti le 25 octobre
à 07:49 UTC et arrêté sur le crédit épuisé (rapport mécanique v2 et audit de symétrie, branche `canal/conv-audit-n04`,
commit `7d1feec550e3d3bdaf963ecade2cf1558b73e53f` : `rapport-pilote-gemini-organisme-v4-question-v1-mecanique-v2.md`,
`7136f5b9…` ; `audit-symetrie-pilote-gemini-v4-question-v1.md`, `35ade113…`). Ce texte reprend le dessin du premier
(une lignée imposée, deux générations notées, question posée à g001 seulement, sortie fermée, lectures interdites) ; ce
qui change est dit à chaque section.

Décisions de Lazar (heure de Paris, 25 octobre 2026) : 01:45 — moissonneur : « (b) … goooo » (une v5 de Gemini avec
moissonneur et un second pilote plus tard) ; 09:07 — « (b) go » : question v2 « apprendre sa structure… » posée à g1 ;
09:26 — « (a) go » : la v5.1 de Gemini, sur les faits mécaniques transmis ; 09:51 — « (c) Les deux, en deux courses … :
les deux » ; 09:58 — la garde avant départ est un **test de dépense**, « car la recharge automatique est activée sur tous
les modèles API » ; 10:17 — plafonds, option (b) : « 30 par génération, 60 par course, 120 au pire pour les deux,
8 192 jetons … : go ». Mots directs de Lazar dans la session de session-depot (consignés sur `main`) : vers 09:13 UTC,
la recharge automatique est active sur toutes les clés, Anthropic et Gemini (R-404) ; vers 09:25 UTC, « je te donne par
anticipation mon go pilote 2 pour le moment venu » (ligne `GO-2026-10-25-01`, R-407) ; vers 09:44 UTC, « plafond du
GO-2026-10-25-01 porté à 120 USD » (R-409, ligne d'extension ; Lazar à conv-audit, 10:45 Paris : « c'est fait »).
Sources de moisson : Lazar, 11:37 Paris : « alors avec Brave, ne le retire pas » et « oui, et la clé est déjà versée dans
dépôt » (à la proposition « rendre la source web si la clé existe et que l'offre est gratuite ») : **la source « web »
(Brave) est servie**, clé tenue par session-depot et passée au noyau seul ; 11:43 Paris : clé OpenAlex demandée à son
adresse (« (a) … : go »), formulaire Semantic Scholar préparé (« ok »), ajout au noyau de ces clés et des sources Crossref,
DBLP, OpenReview et CORE après l'étape 1 (« oui d'accord ») — rien de cela ne touche ce pilote, dont le code est figé. But : voir ce que donne, sur les deux familles de
tâches réelles, l'organisme v5.1 (code figé, mémoire spectrale transmise, moisson documentaire servie par le noyau) ;
répéter la chaîne réelle après les corrections du premier pilote (crédit épuisé rendu en 400, plafonds de sortie, verrou,
refus) avec statuts et coûts ; recueillir, comme **matériau**, deux réponses de son essaim à deux questions ouvertes,
posées avant qu'il ait vu quoi que ce soit de notre part. **Aucune hypothèse n'est testée** ; tout est rapporté. Rien
d'opposable (R7) ; aucune lecture de résultat avant scellement (R1) ; aucun run visant un signe (R3) ; symétrie de
l'audit (R4).

- Auteur : lignée conv-audit. Date : 2026-10-25, 11:05 UTC (heure lue sur `date -u` ; les heures de Paris citées sont
  celles des messages de Lazar). Lanceur : lignée session-depot (clés), dans son conteneur (root, `unshare` disponible ;
  aucune instance payante), une course par appel du script `prereg/pieces-pilote2-gemini-v5-1/lancer_pilote2_gemini_v5_1_v4.sh`
  (empreinte au § Pièces ; remplace les v1 à v3, gardées), qui exécute le plan § 1 et § 3 pas à pas et refuse, avec
  sa raison consignée, à chaque écart ; processus consigné par son PID dans `LANCEMENT.md`, arrêt par PID (R10). Placé
  par session-depot avant les courses décisives de l'étape 1, dans le même conteneur (ligne `GO-2026-10-25-01`).
- **Deux courses**, dans cet ordre : **S** (`COURSE=structure`, nom `pilote2-gemini-v5-1-structure-v1`), puis **M**
  (`COURSE=maieutique`, nom `pilote2-gemini-v5-1-maieutique-v1`). Même objet, même code, même banque, mêmes bornes ;
  seules diffèrent la question et la graine. **M ne part que si S est « saine »**, définition close vérifiée par le
  script de M dans les pièces lisibles de S (variable `S_PILOTE` = dossier du pilote de S ; P2C1-01) : empreintes de S
  vérifiées (`EMPREINTES-pilote-v1.txt` et son compagnon) ; `LANCEMENT.md` de S écrit par ce même lanceur (même
  empreinte), pour la course S, avec « code de retour : 0 » et la ligne « archive fermée : ferme.tar.gz (… » (pas
  d'archive incomplète, aucun espace des organismes autre que l'espace attendu) ; extrait mécanique de S : exactement les
  générations 0 et 1 de la lignée, chacune au statut `OK`, non invalidée, sans anomalie du noyau ; aucune génération
  invalidée au rapport ; fin de la lignée « générations maximales » ; un seul arrêt de la course, « aucune lignée
  active ». **En réel, de plus** (P2C2-01) : S a tourné en réel (en-tête « (reel, tentative N) » de son `LANCEMENT.md`,
  `manifeste.reel` vrai), sous `GO-2026-10-25-01` (`manifeste.go_id`), avec la graine S du texte scellé
  (`manifeste.entropie_seed_sequence`), dans le dossier des pilotes de la copie de lancement, sous le nom
  `pilote2-gemini-v5-1-structure-v1` ou sa tentative ; les empreintes de S listent son `LANCEMENT.md` et son extrait ; et
  **la ligne de dépense de M**, écrite par session-depot **après la fin de S**, porte les 16 premiers caractères de
  l'empreinte de `EMPREINTES-pilote-v1.txt` de S. **Toute autre issue** (S simulée ou d'une autre graine, crédit
  épuisé, fichier `STOP`, modèle non conforme, isolation indisponible, exception du noyau après le manifeste, archive
  incomplète, espace autre, génération non tournée ou invalidée, g1 sans successeur valide, S non partie) : M ne part
  pas, refus consigné, et attend une nouvelle décision de Lazar. **Les plafonds ne bloquent pas M** (P2C2-02) : avec
  2 × 30 = 60, le plafond total ne peut être atteint qu'à la fin de g1 ; les refus d'appels au plafond d'une génération
  de S (`refus_noyau`) et la dépense de S sont consignés dans le `LANCEMENT.md` de M, pour information. **Procédure entre
  S et M** (P2C2-05) : la copie de lancement n'est jamais committée ; le dossier de S n'y est jamais modifié ; S est
  poussée depuis un autre arbre de travail (copie des fichiers de son `A-POUSSER-v1.txt`) ; le rapprochement de la
  dépense avec la console s'écrit dans `registres/depenses.md`, jamais dans le dossier de S.
- **Objet** : `gemini-organisme-v5-1` — branche `outils/gemini-organisme-v5-1`, commit
  `7f9cd2e5a8053dc45050e1b6316bf29ee0c62e0e`, dossier `outils/gemini-organisme-v5-1/organisme/`, **19 fichiers**, sans
  `memoire_isvd.json` ni `etat_generation_precedente.json` ni `__pycache__`, empreinte d'arbre
  `50ffcd7d8cd3af059f2b881f3e565a8ad5829d8d325c39b9535bed6e01a8e12c` par `boucle.empreinte_arbre`, celle que le noyau
  consigne au manifeste. Famille nominale `gemini`. Lignée imposée unique, **sans phase de conception**
  (`--rondes-conception-max 0`), **G = 2** générations notées (g0, g1 ; g1 reçoit `memoire_isvd.json` et l'historique de
  g0 ; `--relances-max 1`). Provenance (`outils/gemini-organisme-v5-1/LISEZMOI-v1.md`) : reçue de Lazar le 25 octobre à
  09:44 Paris (`livraison/recu-gemini-v5-1-v1.txt`, `49dc80c6…`), reconstituée sans exécuter le script de Gemini ; réponse
  à `DEMANDE-v5-1-faits-mecaniques-v1.md` (faits du premier pilote, **aucune valeur suggérée**) ; ses plafonds de sortie
  (16 384 ; 24 576 ; 8 192) sont les siens, rabattus par son code au `max_tokens_appel` du noyau. Correction faite par
  nous avant tout run réel, sur simulation sans score réel : C-12 (verrou non réentrant), reprise telle quelle par Gemini ;
  aucune correction ne vient d'un résultat réel. 27 essais passés en isolation ; suites d'appels identiques pour trois
  graines de hachage ; simulé sous le noyau `90595ffb` avec la question S et la moisson ouverte. **Déclarations** : le code
  de la v5.1 ne contient aucun texte des deux questions ; son code et sa documentation partagent du vocabulaire avec la
  question M (score « Bregman-Tsallis », vecteurs « de Koopman », mentions d'une expérience « pascalienne » que sa propre
  `CONCEPTION.md` dit sans pièce) ; la question M a été écrite par Gemini, concepteur de l'organisme.
- **Questions ouvertes** (posées par le noyau, `--question-ouverte … --question-ouverte-aux g001`, contrat § 7, à la
  **seule génération 1** ; à g0, `contexte["question_ouverte"]` vaut null) :
  - **S** : `question-apprendre-structure-entrainement-generations-organismes-v2.md`, branche `canal/conv-audit-n04`,
    commit `4772b525081342a6a30ba8823733aa5770a888a8`, `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289` :
    un en-tête pour l'organisme puis le corps de la question posée au collisionneur (« structure » v2, `6906a1d1…`),
    sans aucune de ses réponses ;
  - **M** : `question-gemini-maieutique-vs-coercition-organismes-v1.md`, même branche, commit
    `7d1feec550e3d3bdaf963ecade2cf1558b73e53f`, `9e1da26de7c7951e0c9a319b12b99faaad7252f86dc14b0d85479696b4cc6595` :
    notre en-tête, puis le texte de Gemini — lignes 2100 à 2104 de `livraison/recu-gemini-v5-1-v1.txt`, **chevrons de
    citation et retours chariot retirés**, octets inchangés sinon (empreinte du bloc seul
    `12a21131fea455f79915f1ccf5fccd228e9f84fbcb1d4c8f6b88bfab99fb8fa3`, P2C1-13) —, puis notre pied (identique à celui de
    S). Ce texte nomme des sujets qui ont déclenché un refus de filtre au premier tour du collisionneur : un refus est un
    échec compté par l'organisme, **jamais reformulé**.
- **Banque** : `essaim-m3-refonte-v1/banque/banque-confrontation-v1.json`,
  `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc` (80 / 60 / 60 ; `banque/LISEZMOI-v3.md`,
  `66855d2ab0d89d6fdea9bd85ff41005c7aa16c5f9e7f55cdc0c4fbff7f0299af`), inchangée depuis le premier pilote. **Mission** :
  `essaim-m3-refonte-v1/MISSION-v1.md`, `bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e`. Les deux
  vérifiées par `sha256sum` avant le départ.
- **Code** : commit **`5d1d4fdb0dbd9e4d481ec3f4270555f4006df749`** de `outils/essaim-m3-gradient-v2-travail` (tête de
  session-depot, 25 octobre 09:17 UTC : contient `4967734a…` (liens), `90595ffb…` (R-395 : crédit épuisé rendu en 400 ou
  en erreur de flux sous 200, arrêt de la course), `c66f529e…` (R-398 : la réflexion comprise dans `max_tokens`, dite
  au contrat), R-402 (types de blocs de chaque réponse au journal des appels ; appels qui ont réfléchi comptés par
  l'extrait) et CL5-01 / CL5-02 (dépôt caché, dossiers inscriptibles par tous rendus privés)). **140 essais** (123 dans
  `tests/test_noyau.py`, 17 dans `tests/test_outils.py`), tous passés dans un conteneur du même type (conv-audit, root,
  25 octobre, 09:22 UTC, 0 sauté, dont la recherche réelle sur arXiv). Le lanceur part d'une copie du dépôt dont
  `essaim-m3-refonte-v1/essaim_m3/`, `essaim-m3-refonte-v1/tests/` et `collisionneur-v2.5-banc-jev-travail/` sont
  identiques à ceux de `5d1d4fd`, au commit et dans l'arbre de travail ; **les commits postérieurs ne touchent que ce
  texte, ses pièces et ses contre-lectures** (vérifié par le script : `git diff --name-only 5d1d4fd HEAD` dans la liste
  permise) ; rien de non suivi ni de modifié sous `essaim-m3-refonte-v1/` et le collisionneur hors des dossiers de pilotes
  (un module posé à la racine masquerait sinon un module du noyau, P2C1-13) ; tout autre code vaut nouvelle version de ce
  texte. Le champ `commit` du manifeste sera la tête de la copie ; c'est l'identité du code qui fait foi. Empreinte du
  code du noyau : `boucle.empreinte_arbre(essaim_m3/noyau)` = `d5d0efcc4677dd9957db3f324101b58e9475642e8e05926407579f056f653836`
  (17 fichiers, calculée sur `git archive 5d1d4fd` ; la fonction écarte le bytecode depuis le constat n° 30 § 5, et le
  `sha256_code_noyau` du manifeste aussi) ; collisionneur `collisionneur_v2.py` =
  `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd`. Versions consignées dans `LANCEMENT.md` par le
  script : Python, numpy, la bibliothèque `anthropic` (exigée en réel) (P2C1-13).
- **Espèces servies** : `["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5", "GEMINI_ARGON"]`. Règles de l'organisme
  (`mitose_spectrale.py`) : pour les tâches, une caste (`budget_par_tache` = (160 − 6) // 120 = 1), la première espèce :
  **toutes les réponses aux tâches viendront de Fable** ; pour la question, `planifier_castes_question_ouverte` planifie
  min(appels restants, 5) castes dans l'ordre des espèces (Fable, Opus, Argon, Fable, arbitre Opus), appelées une à une
  après la fermeture de l'exécuteur des tâches ; la formulation des requêtes de moisson de g1 prend l'espèce de la première
  caste. Réflexion : les espèces Anthropic sont appelées par le collisionneur en réflexion adaptative à effort élevé,
  **comprise** dans `max_tokens` (R-398) ; chaque appel consigne ses types de blocs (R-402). Les clients du collisionneur
  reprennent une requête en échec (Anthropic jusqu'à 4 fois ; Gemini jusqu'à 4 fois, délai jusqu'à 1 200 s) : ces reprises
  ne sont pas des appels de l'organisme et ne sont pas comptées par le noyau (P2C1-05). Clés « selon GO-2026-10-24-04 » :
  la clé Anthropic prise dans la variable que nomme `CLE_ANTHROPIC` (défaut `ANTHROPIC_API_KEY`) et passée au noyau sous
  `ANTHROPIC_API_KEY` ; la clé Gemini dans la variable que nomme `CLE_GEMINI` (défaut `GEMINI_API_KEY_2`, sinon
  `GEMINI_API_KEY`) et passée sous `GEMINI_API_KEY` ; la clé Brave dans la variable que nomme `CLE_BRAVE` (défaut
  `BRAVE_API_KEY`), **exigée en réel**, passée sous `BRAVE_API_KEY` (source « web ») ; les noms des variables sont
  consignés, jamais les valeurs ; `ANTHROPIC_BASE_URL`, `PYTHONPATH`, `ESSAIM_M3_COLLISIONNEUR` et `ESSAIM_M3_ESPACE`
  retirées de l'environnement du run.
- **Moisson** (d'après le code `7f9cd2e`, P2C1-02) : `--recherches-max 6 --telechargements-max 3 --octets-max 40000000`
  par génération ; sources servies, dans l'ordre du noyau : `arxiv`, `openalex`, `semanticscholar` (sans clé) et `web`
  (Brave, clé du noyau ; `recherche.Rechercheur`), consignées au manifeste (`sources_moisson`, `cle_brave_presente`).
  L'organisme prend les sources à tour de rôle, dans cet ordre (`principal.py`, `sources_dispo[idx_q % len(sources_dispo)]`).
  À **g0** (pas de question), il appelle `_executer_moisson` sans appel de formulation (`autoriser_appel_formulation=False`) :
  trois requêtes fixes, donc **au plus 3 recherches** (arXiv, OpenAlex, Semantic Scholar : la source web n'est pas
  atteinte), et **au plus 2 téléchargements** ; un extrait de 350 caractères
  du corpus s'ajoute à la fin des règles induites, que la consigne de tâche coupe à 600 caractères : il n'y entre que si
  l'induction est courte. À **g1** (question posée), pas de moisson pour les tâches ; une moisson sur le sujet de la
  question (ses 600 premiers caractères) : un appel de formulation (2 à 4 requêtes), au plus 4 recherches (la quatrième,
  s'il y en a quatre, va à la source web : **au plus une recherche web par course**), au plus 2 téléchargements ; le bloc
  documentaire (au plus 8 notices et 2 extraits) préfixe les consignes des castes de la question. Constats d'avant (non
  opposables, conv-audit, conteneur du même type, 25 octobre, une requête chacune) : arXiv rend des notices ; l'interface
  de Brave répond (422 sans clé) ; OpenAlex rend 429 parce que, sans clé, ses requêtes comptent contre un budget gratuit
  quotidien partagé par toute l'adresse réseau de la machine, épuisé ce jour-là jusqu'à minuit UTC (message de l'interface,
  10:40 UTC) ; Semantic Scholar rend 429 (réserve commune des utilisateurs sans clé) ; le noyau `5d1d4fd` n'envoie aucune
  clé à ces deux sources : rien n'est corrigé pour ce pilote ; chaque statut est consigné par le noyau et rapporté par
  source. Coût de Brave : nul sur la parole de Lazar (offre gratuite) ; au plus deux requêtes web pour les deux courses. **Provenance des téléchargements** (P2C1-03) :
  le noyau rapporte (i) toute adresse https rendue par une recherche de la même génération (OpenAlex et Semantic Scholar
  rendent des liens d'éditeurs ; la source web, des liens de tout site), (ii) un identifiant arXiv, (iii) une adresse d'un hôte toujours permis
  (`moisson.HOTES_TOUJOURS_PERMIS` : arXiv, OpenAlex, Semantic Scholar, LessWrong, Alignment Forum) ; les redirections https
  sont suivies ; le texte est rendu à l'organisme comme donnée. **Réserve** : l'extraction du texte des documents (PDF)
  se fait dans le contexte du noyau, hors du bac à sable de l'organisme ; demande de durcissement transmise à
  session-depot (extraction sous un utilisateur non privilégié, environnement vide), sans effet sur ce pilote, dont le
  code est figé.
- **Bornes**, par course : par génération `appels_max` 160, `usd_max` **30**, `temps_max_s` **3 600** (le premier pilote
  avait 1 800 ; porté à 3 600 **pour réduire le risque** que la question, traitée après les 120 tâches, soit coupée par
  la garde interne des 75 % du temps de l'organisme ; la latence par appel, réflexion comprise, n'est pas connue ; sans
  effet sur le pire cas en dollars), `max_tokens_appel` **8 192**, `recherches_max` 6, `telechargements_max` 3,
  `entrainements_max` 0, aucun `--traits` ; `--plafond-total` **60 USD** ; `--isoler-reseau`, isolation d'utilisateur
  (noyau en root), **`--decalage-uid 900`** ; `--parallele-max 8` ; `--relances-max 1`.
- **Isolation** (CL5-01, P2C1-06) : le dossier du pilote est créé en 0700 à root, donc non traversable : l'espace des
  organismes va sous `/var/lib/essaim-m3/<16 premiers caractères de sha256(chemin absolu de la course)>`
  (`bac_a_sable.espace_organismes`), hors du dépôt ; le script calcule cet **espace attendu** avant le départ et le
  consigne ; c'est le seul espace archivé puis retiré. Le dépôt de la copie doit être sous `/root` ou `/home` (cachés par
  défaut aux organismes de toute course, la voisine comprise) et il est donné au noyau dans `ESSAIM_M3_CACHER` ; le script
  vérifie par `bac_a_sable.dossiers_a_cacher`, pour l'espace attendu, que le dépôt réel est caché. Entre courses, la
  protection tient aux utilisateurs distincts (décalage 900 : utilisateur 60900), aux modes 0700 et 0750 et aux espaces de
  noms (essais `test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course`, `test_cl5_01_banque_cachee_a_l_organisme`,
  `test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`, ce dernier sur deux organismes successifs, non
  simultanés). Course voisine : refus si elle tourne au décalage 900 ; **réserve consignée** si elle tourne au décalage 0,
  700 ou 800 (pendant les essais d'avant départ, ≈ 3 minutes, des processus d'essai du noyau tournent sous les
  utilisateurs 60000 et suivants, 60700–60701, 60800–60830 et 60900, P2C2-04) ; consignée sinon ; détection refaite juste
  avant le départ. Symétriquement, des essais du noyau lancés dans le conteneur **pendant** une de nos courses feraient
  tourner des processus sous l'utilisateur 60900 de ce pilote : session-depot n'en lance pas pendant nos courses ; le
  script consigne en réserve tout `pytest` présent au départ. Le champ
  `caches` des exécutions n'est pas copié par l'extrait : le recouvrement effectif du dépôt se vérifie après le moment
  de lecture, dans l'archive fermée.
- **Service des tâches** : en génération notée, le noyau sert `test` et `test_final` **mêlés** (120 tâches, ordre tiré
  par la graine de la génération) ; **g0 ≈ 123 appels** (1 induction, 2 vérifications, 120 tâches) ; g1 ≈ 123 appels de
  tâches puis jusqu'à 6 pour la question (1 formulation, 5 castes) : ≈ 129, sous 160.
- **Devis au pire cas** : 2 × 30 = 60 USD par course, **120 USD pour les deux**, plus les tests de dépense (≈ 0,002 USD
  par course au premier pilote). Ordre de grandeur attendu, **non opposable**
  (`prereg/pieces-pilote2-gemini-v5-1/devis-attendu-pilote2-v3.json`, script `devis_attendu_pilote2_v3.py` ; entrées : le
  journal des appels de g000 du premier pilote, `journal-appels-g000.jsonl`, branche
  `pilotes/gemini-organisme-v4-question-v1`, commit `84b880a75be152289b1dd9c715e75a25e381c6fb`,
  `c24d0e55edbc77b3740c04718adccccf1d3d51ae1045260349a867b52ba1ca90` — 2 195 jetons d'entrée en moyenne sur les appels
  de tâche facturés, d'un pilote aux règles induites vides ; ici jusqu'à 600 caractères de plus, effet faible —, les prix
  lus par `appels.modele_de`, Fable et Argon 10 USD par million de jetons d'entrée et 50 en sortie, Opus 4 et 20) : la
  sortie par appel, réflexion comprise, est **inconnue** ; ≈ 18 USD la course à 1 000 jetons de sortie par appel de tâche,
  ≈ 31 à 2 000, ≈ 44 à 3 000 ; la question de g1, dont les castes partent une à une, est servie entière au pire cas tant
  que Fable écrit au plus ≈ 4 100 jetons par tâche (seuil « un appel en vol » de la pièce) ; le dernier appel de tâche
  de g0 est refusé (`PLAFOND`) au-delà de ≈ 4 400 jetons (un en vol) ou ≈ 4 200 (huit en vol) — la contre-lecture 1
  trouvait ≈ 3 900 pour huit en vol : ordre de grandeur, qui dépend de la longueur des consignes. Sous
  **`GO-2026-10-25-01`** (`registres/go.md` sur `main`, commit `21121c1` : ligne R-407, « second pilote … deux courses
  (question v2 `a54da93e…` et question écrite par Gemini `9e1da26d…`) … telles que les définira leur préenregistrement
  scellé et contre-lu …, tests de dépense compris » ; extension R-409, **120 USD au plus pour les deux courses** ;
  échéance 2026-10-31). Avant chaque course, **deux écritures et une vérification** : la ligne du GO existe (le script
  exige une ligne `| GO-2026-10-25-01 |` qui porte, sur la même ligne, le type calcul et l'empreinte de la question de la
  course) ; session-depot consigne la course dans `registres/depenses.md` (une ligne qui nomme la course et
  `GO-2026-10-25-01` ; 60 USD au pire cas ; celle de M après la fin de S) et déclare au script le **reste disponible sur
  le GO, ≥ 60 USD** (après tout ce qui y est imputé, la course S comprise quand M part) ; sans elles, la course ne part
  pas.
- **Test de dépense** (décision de Lazar 09:58 ; P2C1-04) : la recharge automatique étant active (R-404), un appel de
  solde ne dirait rien ; à sa place, **un appel payant par espèce**, fait par l'outil d'appel de contrôle de session-depot
  au plus 15 minutes avant le départ de chaque course. **La réalité des appels est attestée par l'outil de session-depot ;
  le script vérifie la pièce** : pour chacune des trois espèces, `statut` `OK`, `modele_servi` conforme
  (`claude-fable-5-1`, `claude-opus-5-5`, `gemini-4-argon`), `cout_usd` > 0, jetons de sortie > 0 quand la pièce les donne,
  `go` = `GO-2026-10-25-01`, **heure de l'appel (`heure_utc`, avec fuseau) exigée en réel** ; âge ≤ 900 s par la date du
  fichier et par l'heure de chaque appel ; la vérification est **refaite juste avant le départ**, après les essais, et la
  pièce doit être restée identique (empreinte) depuis sa première lecture (P2C2-10). Aucun identifiant de requête n'est
  exigé : la pièce ne prouve pas à elle seule les appels. L'attestation
  de la recharge (R-404) est consignée telle quelle dans `LANCEMENT.md`. **Ce que le test ne garantit pas** : que la
  recharge suivra pendant la course (moyen de paiement, plafond mensuel éventuel) ; un arrêt sur crédit épuisé reste
  possible, il arrête la course (R-395) et M ne part pas. **Réserve dite** (P2C1-05) : la recharge automatique retire le
  plafond externe que formait le solde au premier pilote ; les plafonds du noyau (`--plafond-total`,
  `--usd-par-generation`, réservation au pire cas des appels en vol, `appels._reserver`) et l'arrêt sur crédit épuisé
  deviennent le seul frein — un frein **juste mais pas étanche** : un appel en échec est compté 0 USD même si une partie a
  été facturée, les reprises des clients ne sont pas comptées, l'entrée du pire cas est estimée à caractères ÷ 3, et la
  course voisine dépense sur le même compte et partage ses limites de débit ; la dépense du noyau (extrait) est consignée
  après chaque course et rapprochée de la console sur la parole de Lazar.

## Hypothèse

Aucune (pilote descriptif). Ce qui est rapporté, **par course** : (1) mécanique — statut d'exécution de chaque génération
(`OK`, `EXCEPTION`, `DELAI_DEPASSE`, `SANS_STATUT`, `STATUT_ILLISIBLE`, `ISOLATION_INDISPONIBLE`, `INVALIDE_MODELE`,
`ANOMALIE_NOYAU`, `CREDIT_EPUISE`), appels par espèce et par rôle, statuts des appels (`OK`, `TRONQUE`, `VIDE`, `REFUS`,
`ANOMALIE`, `ECHEC_API`, `PLAFOND`, `ARRET_NOYAU`, `MODELE_NON_CONFORME`), types de blocs par appel et appels qui ont
réfléchi par statut (R-402), jetons d'entrée et de sortie par appel (journal), coût réel contre plafond et dépense
rapprochée de la console, durées, recherches et téléchargements par source et par statut, castes planifiées (tâches et
question), taille de `memoire_isvd.json`, relance éventuelle, empreinte de l'archive de l'organisme à g0 et g1 (identité
du code de g1 avec celui de g0 vérifiée après le moment du plan § 3), éléments écartés par le dépôt, nombre total de
réponses valides (`n_reponses_test`) ; (2) la **réponse à la question ouverte** : si elle a été lue, ses octets et son
empreinte, le texte **tel quel** et sa structure mécanique (sections présentes, bloc ORGANISATION, documents moissonnés
cités) ; (3) scores — exactitude équilibrée par famille sur `test` et sur `test_final`, aux générations 0 et 1, dans une
table où figurent aussi les références de surface ; calibration (Brier borné, erreur de calibration) ; part de tâches sans
réponse valide par famille. **Aucune différence n'est calculée ni nommée** (ni g1 − g0, ni score − référence, ni S − M,
ni second pilote − premier) ; **les réponses ne sont ni notées, ni jugées, ni comparées entre elles** : c'est du matériau,
rapporté avec sa provenance.

## Prédiction chiffrée et signe attendu

Aucune prédiction ; aucun signe attendu. Rien n'est écrit sur ce que « devrait » donner cet organisme, ni sur ce que ses
réponses « devraient » dire, ni sur l'effet de la moisson ou des plafonds.

## Métrique

Exactitude équilibrée par famille ((sensibilité + spécificité) / 2), juge du noyau (`taches.evaluer`), une tâche sans
réponse valide comptée comme une erreur ; calibration par `taches.calibration` (10 classes ; sans réponse : q = 1, faux).
Scores de `test` rendus à l'organisme dans `historique` ; score de `test_final` jamais rendu, calculé par le noyau en fin
de génération (`juge/score-final.json`), lu par personne avant le moment fixé au plan § 3. La question ouverte n'a aucune
métrique (essai `test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`).

## Seuil

Aucun seuil de lecture (descriptif). Seuils de **garde** : plafond 60 USD par course, 30 par génération ; 3 600 s par
génération ; un appel `MODELE_NON_CONFORME` invalide la génération et arrête la lignée ; un crédit épuisé (HTTP 402, ou
« credit balance is too low » en 400 ou en erreur de flux sous 200 : `CREDIT_EPUISE`) invalide la génération et arrête la
course ; un journal d'appels absent après des appels (`ANOMALIE_NOYAU`) invalide la génération ; M ne part que si S est
saine (définition close ci-dessus).

## Plan d'analyse

1. **Une seule course de chaque nom** (R3), S puis M. Une course **part dès que son manifeste est écrit** ; après, jamais
   de seconde course de ce nom. Gardes (P2C2-06) : courses déjà parties cherchées dans tous les dossiers du nom, au début et
   juste avant le départ ; verrou `.verrou-<nom>` dans le dossier des pilotes (création atomique, retiré sur refus avant
   la course, gardé sinon) ; marqueur de départ du conteneur `/var/lib/essaim-m3/pilotes-partis/<nom>` posé de façon
   atomique juste avant le départ, jamais retiré une fois la course partie (retiré seulement si aucune course n'est partie) ;
   refus si la branche `pilotes/<nom>` existe déjà sur le dépôt distant (lecture impossible du dépôt distant : refus). Avant (tout refus ou toute exception avant le manifeste), une nouvelle tentative de la
   même commande est permise, dans un nouveau dossier (`…-tentative2`, R12), après correction de l'environnement, jamais
   de ce texte (dossiers vides laissés, sinon `refus-avant-manifeste-v1.tar.gz`, jamais lu). En mode réel, le script
   refuse toute variable d'essai et `ESSAIM_M3_ESPACE`, un dépôt hors de `/root` et de `/home`, une course voisine au
   décalage 900 ; il consigne les autres voisines (réserve aux décalages 0 et 800). Dossier du pilote :
   `PILOTE` = `essaim-m3-refonte-v1/pilotes/<nom de la course>/` dans la copie du dépôt (nouveau, créé en 0700). Étapes,
   toutes faites par le script, chacune consignée dans `$PILOTE/LANCEMENT.md` : (0) pour M seulement, S saine (liste
   close ci-dessus, `S_PILOTE` ; non défini : refus consigné) ; (i) code identique à `5d1d4fd` (commit et arbre de travail, `essaim_m3`, `tests`,
   collisionneur), commits postérieurs limités aux pièces du pilote, rien de non suivi ni d'ignoré (`git status
   --ignored`, P2C2-09) hors des dossiers de pilotes et des `__pycache__`,
   `4967734a…` et `90595ffb…` ancêtres, banque, mission et collisionneur par `sha256sum`, versions consignées (lues sans
   `-I`, comme le noyau tourne) ; (i bis)
   dossier du pilote « 700 0 », espace attendu calculé et consigné, dépôt caché vérifié ; (ii) préenregistrement scellé
   (empreinte donnée, compagnon conforme, graine de la course écrite et **recalculée depuis l'entropie** du texte, aucun
   marqueur, empreinte du lanceur citée ; pour M, graine de S au manifeste de S = graine S du texte) ; (iii) `$PILOTE/outils/gemini-organisme-v5-1/organisme/` =
   `git archive 7f9cd2e… outils/gemini-organisme-v5-1/organisme` (`50ffcd7d…`, 19 fichiers) ; `$PILOTE/question.md` =
   `git show <commit de la question>:<chemin>` (S : `a54da93e…` ; M : `9e1da26d…`) ; (iv) `$PILOTE/registre-go.md` =
   `registres/go.md` d'`origin/main` ; ligne du GO pour cette course ; dépense consignée dans
   `origin/main:registres/depenses.md` (pour M, avec l'empreinte des empreintes de S) ; reste déclaré ≥ 60 USD ; (v) test de dépense vérifié, copié en
   `test-depense-<nom>.json`, attestation consignée ; (vi) essais en root, depuis `essaim-m3-refonte-v1/`, environnement
   sans `PYTHONPATH`, `ESSAIM_M3_COLLISIONNEUR` ni `ESSAIM_M3_CACHER` : `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p
   no:cacheprovider --junitxml $PILOTE/essais-v1.xml` ; exigés : aucun échec, **aucun saut** (l'essai de recherche réelle
   sur arXiv compris), passés + désélectionnés = 140, et chacun des 28 essais cités passé ici ; (vii) nettoyage des
   `__pycache__`, puis `boucle.empreinte_arbre(essaim_m3/noyau)` = `d5d0efcc…` ; (vii bis) test de dépense **revérifié**
   (pièce inchangée depuis sa première lecture, âge ≤ 900 s au départ, sinon refus : le refaire, tentative suivante) ;
   voisines redétectées ; courses parties recherchées de nouveau ; marqueur de départ posé ; (viii) en root,
   `PYTHONDONTWRITEBYTECODE=1`, `ESSAIM_M3_CACHER=<dépôt>`, clés exportées sous leurs noms du noyau (`ANTHROPIC_API_KEY`,
   `GEMINI_API_KEY`, `BRAVE_API_KEY`), `ANTHROPIC_BASE_URL`, `ESSAIM_M3_ESPACE`, `PYTHONPATH` et `ESSAIM_M3_COLLISIONNEUR`
   retirées, depuis `essaim-m3-refonte-v1/` :
   `python -m essaim_m3 lancer --reel --go GO-2026-10-25-01 --registre-go "$PILOTE/registre-go.md" --taches
   banque/banque-confrontation-v1.json --mission MISSION-v1.md --sortie "$PILOTE/course" --generations 2 --graine <graine
   de la course> --especes --appels-max 160 --usd-par-generation 30 --temps-max 3600 --max-tokens-appel 8192
   --recherches-max 6 --telechargements-max 3 --octets-max 40000000 --entrainements-max 0 --rondes-conception-max 0
   --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 60 --decalage-uid 900 --question-ouverte
   "$PILOTE/question.md" --question-ouverte-aux g001 --organisme-impose
   "gemini-organisme-v5-1=$PILOTE/outils/gemini-organisme-v5-1/organisme@gemini" > "$PILOTE/ferme/sortie-standard-lanceur.txt"
   2> "$PILOTE/sortie-erreur-lanceur.txt"`. Un fichier `STOP` dans `$PILOTE/course/` n'est posé que pour un incident
   technique (panne, coût anormal lu dans le journal des appels), consigné ; jamais au vu d'un score.
2. **Graines (R9)** : entropie E = <<ENTROPIE>> tirée au scellement par `secrets.randbits(128)` ; deux enfants
   `numpy.random.SeedSequence(E).spawn(2)` ; graine de chaque course = `int(enfant.generate_state(1, dtype=numpy.uint64)[0])`,
   l'enfant 0 pour S, l'enfant 1 pour M (chaque égalité sur une seule ligne, lue et recalculée par le lanceur) :
   graine de la course structure = <<GRAINE_STRUCTURE>>
   graine de la course maieutique = <<GRAINE_MAIEUTIQUE>>
   Le manifeste de chaque run consigne sa graine, la version de numpy, `sha256_code_noyau` et `commit` ; E n'est
   consignée qu'ici.
3. **Moment de la lecture des scores (R1)** — fichier par fichier. La **sortie standard** (qui porte les scores,
   `cli.py`) va dans `$PILOTE/ferme/`, jamais lue. Sont lisibles comme sorties d'erreur, sans score (P2C1-12) :
   `sortie-erreur-lanceur.txt` (au commit cité, les 20 `print(…, file=sys.stderr)` de `cli.py`, tous « refus : … »,
   « mode réel non demandé » ou « espèce inconnue », les messages de `SystemExit` de `cli._organismes_imposes` et
   d'`argparse` avant le manifeste, et en cas d'exception la trace Python ; ni `logging` ni `warnings` dans le noyau),
   `sortie-erreur-extrait.txt` (l'outil d'extraction n'y écrit que « refus : … ») et `sortie-erreur-tar.txt` (messages de
   `tar`). **Pendant la course**, le lanceur ne consulte que le journal des appels de la génération en cours, par son
   chemin exact, `<espace attendu>/travail/gemini-organisme-v5-1/gNNN.noyau/journal-appels.jsonl` (statuts, espèces,
   coûts, types de blocs ; aucun score), l'espace attendu étant consigné dans `LANCEMENT.md` avant le départ ; ni la liste
   de ce dossier ni le reste de `gNNN.noyau/`. **Dès la fin**, sont lisibles et seulement eux : (a)
   `$PILOTE/extrait-mecanique-v1.json` (listes closes de champs ; comptes par statut des recherches par source et des
   téléchargements ; appels qui ont réfléchi par statut ; dépense du noyau ; jamais de score) ; (b) la réponse,
   recopiée en `$PILOTE/reponse-question-g001.md` (vrai compagnon de la copie, compagnon d'origine en `.sha256-archive`) ;
   (c) les journaux d'appels archivés, recopiés en `$PILOTE/journal-appels-gNNN.jsonl` ; (d) les trois sorties d'erreur,
   `LANCEMENT.md`, `essais-v1.*` ; (e) les entrées poussées en clair : `question.md`, `registre-go.md`,
   `test-depense-*.json`, `outils/gemini-organisme-v5-1/organisme/`, `.gitignore`, `A-POUSSER-v1.txt` et les fichiers
   d'empreintes. **Canaux dits et acceptés** (P2C1-07) : la taille de `contexte.json` de g001 dépend de la longueur
   d'écriture du score `test` de g0 ; l'organisme écrit lui-même des valeurs qui arrivent dans les pièces lisibles (noms et
   tailles de ses fichiers, `erreurs` de son journal, `role` de chaque appel, castes, bilan spectral, taille de sa réponse) ;
   personne ne les calcule ni ne les met en rapport avec quoi que ce soit avant le moment ci-dessous. **Le score de g0 n'a
   d'effet sur rien à g1** (P2C1-02) : le code de la v5.1 ne passe `historique` qu'à `planifier_castes_par_mitose` et à
   `planifier_castes_question_ouverte`, qui n'en lisent les scores que si `len(historique) >= 2`
   (`mitose_spectrale.py`) ; à g1, `historique` n'a qu'une entrée ; ni les consignes des castes, ni la formulation des
   requêtes, ni le fichier écrit n'en contiennent rien (`principal.py`, `_traiter_question_ouverte`, `_executer_moisson`).
   **Expositions dites et acceptées** : jamais une vérité de `test` ni de `test_final` n'est servie par le noyau ; mais
   le résumé de la mémoire spectrale (jusqu'à 4 exemplaires de ≤ 220 caractères : vérité d'entraînement ou début du
   raisonnement de g0 sur une tâche de `test` ou de `test_final`) entre dans les consignes des castes et de la formulation,
   et peut être cité dans la réponse ; la famille « conscience d'évaluation » de `test_final` vient d'un jeu public, les
   requêtes fixes de g0 visent ce sujet, et la garde de fuite du noyau ne met en quarantaine que les passages de 8 mots et
   plus recoupant les textes de test : des documents moissonnés peuvent en porter des fragments ; personne ne les confronte
   aux vérités de la banque avant le moment ci-dessous. **Deux documents distincts** (P2C2-08) : **jusqu'à ce que (i) le
   préenregistrement de l'étape 1 qui part (document de session-depot, version 8 ou suivante ; son chemin et son empreinte
   seront cités dans le rapport de lecture de ce pilote) soit scellé, et (ii) que soit inscrit, dans le texte de la version
   8 du préenregistrement de la confrontation (document de conv-audit, autre que le précédent), qu'il ne change ni la table
   de lecture de H-E1, ni les seuils, ni les règles de lecture de sa version 7 (brouillon
   `74487a41fe29b4ad0e5688df9fb9fda815725cdd7521ee2a327694b2fa4ddf61`)** (P2C1-08), personne ne lit, notamment : la
   sortie standard, `rapport-v1.json`, `evenements.jsonl`, `archive/index.jsonl`, les `resume.json`, les `juge/`,
   `banque.json`, `lignees/`, `archive/*/gNNN/organisme.tar.gz`, `archive/*/gNNN/travail/` (dont `noyau/appels/`,
   `corpus/`), et dans `<espace>` : `archive_vue/`, `travail/*/gNNN/`, `travail/*/gNNN.corpus/` et tout `gNNN.noyau/` hors
   du journal des appels (`appels/`, `journal-recherches.jsonl`, `recherches/*.brut`, `journal-fuite.jsonl`, P2C1-07).
   **Fermeture mécanique** : le script fait de `course/`, `ferme/` et de l'espace (s'il est l'espace attendu) une seule
   archive `$PILOTE/ferme.tar.gz` (+ `.sha256`), sans l'ouvrir, vérifie le nombre d'entrées contre le disque, puis retire
   les copies ouvertes (sinon réserve consignée ; un espace autre que l'espace attendu n'est ni archivé ni retiré, réserve).
   **Poussé en clair**, et seulement (liste fermée par noms, écrite par le script dans `A-POUSSER-v1.txt`, P2C1-14) :
   `.gitignore` ; `LANCEMENT.md` et son compagnon ; `sortie-erreur-lanceur.txt`, `sortie-erreur-extrait.txt`,
   `sortie-erreur-tar.txt` et leurs compagnons ; `essais-v1.xml`, `essais-v1.txt` ; `extrait-mecanique-v1.json` et son
   compagnon ; `reponse-question-g001.md`, son compagnon et son `.sha256-archive` ; `journal-appels-g000.jsonl`,
   `journal-appels-g001.jsonl`, leurs compagnons et leurs `.sha256-archive` ; `question.md` ; `registre-go.md` ;
   `test-depense-*.json` ; `outils/gemini-organisme-v5-1/organisme/` ; `ferme.tar.gz` ou `refus-avant-manifeste-v1.tar.gz`
   et son compagnon ; `A-POUSSER-v1.txt`, `EMPREINTES-pilote-v1.txt` et leurs compagnons ; tout autre fichier est consigné
   et n'est pas poussé ; sur une branche `pilotes/<nom de la course>`, jamais `main` ; `course/` et `ferme/` jamais
   ajoutés (`.gitignore` écrit avant la course). Tout changement des règles de lecture de la v7 rouvrirait R1 pour ce
   pilote. Déclaration : aucun score de ce pilote ne motive aucun changement des préenregistrements principaux ; la v8 de
   la confrontation citera les empreintes des deux `ferme.tar.gz` et des deux `EMPREINTES-pilote-v1.txt` pour le montrer.
4. **Lecture** : après le moment du point 3, ouverture des deux `ferme.tar.gz` ; par course, tableau rapporté : famille ×
   génération × {score `test`, score `test_final`, référence de surface, Brier, part sans réponse}, plus appels par
   espèce, par rôle et par statut, jetons, appels qui ont réfléchi, coûts et dépense rapprochée, durées, moisson par
   source et par statut, castes, taille de mémoire, empreintes des archives et identité du code de g1, relance, éléments
   écartés, recouvrement effectif du dépôt (champ `caches` des exécutions) ; les deux réponses, telles quelles, avec leur
   structure mécanique ; les deux courses dans deux tableaux distincts. Rédigé par conv-audit, relu par session-depot ;
   aucune lecture de verdict (R13 sans objet).
5. **Ce que ce pilote ne dit pas** (écrit d'avance) : rien sur H-E1, H-G1 ni sur les organismes auto-écrits ; rien sur
   « l'intelligence » de la conception de Gemini ; rien sur l'effet de la moisson, des plafonds ou de la question (aucun
   bras témoin) ; rien sur la valeur d'une question contre l'autre ; ses scores sont des points, pas des estimations, et
   n'entrent dans aucun critère des préenregistrements principaux ; chaque réponse est l'avis d'un essaim d'une
   conception, à une graine : un matériau parmi d'autres, jamais une consigne au noyau ni aux organismes, jamais servie à
   un organisme. La moisson réelle n'a jamais tourné de bout en bout avant ce pilote (seule la fonction de recherche
   arXiv est essayée en réel ; partout ailleurs, la source « simulation », P2C1-11).

## Critères de lecture gelés

1. Pour chaque course : score d'une famille > 0,95 ou < 0,30 sur `test` ou sur `test_final`, à l'une des générations ;
   ou part de tâches sans réponse de 100 % pour une famille ; ou plus de 20 % d'appels hors `OK` à une génération ; ou une
   génération en statut autre que `OK` ; ou aucune recherche `OK` à une génération où l'organisme en a demandé → **audit
   de symétrie (R4)** avant tout rapport, **sans relance**, par un **sous-agent neuf** lancé par conv-audit, qui n'a ni
   écrit ce texte ni lu les scores avant l'audit ; rapport scellé. Les déclencheurs mécaniques se lisent dès la fin dans
   l'extrait ; un audit qui doit lire un fichier fermé se fait après le moment du point 3 ; d'ici là, son matériau se
   limite aux fichiers lisibles (a)–(e).
2. Question, pour chaque course : (i) g1 n'a pas tourné → « question non posée : g1 n'a pas tourné », avec la raison lue
   dans l'extrait ; (ii) `reponse` faux avec `probleme` autre que « absent » → refus du noyau rapporté avec la raison ;
   (iii) `reponse` faux et « absent » → « l'organisme n'a pas écrit de réponse » ; (iv) réponse d'une génération g1
   invalidée → texte rapporté tel quel, avec la mention « réponse d'une génération invalidée (statut …) » ; (v) réponse
   lue → texte rapporté tel quel, y compris le texte d'abstention ou le texte minimal de l'organisme ; les appels de la
   question refusés par le plafond (`PLAFOND`) ou par un filtre (`REFUS`) sont comptés et dits.
3. Sinon → **rapporté tel quel** : les tableaux, les statuts, les coûts, les réponses, et la phrase « pilote descriptif,
   un organisme, deux courses à une graine chacune, deux générations, une espèce appelée pour les tâches, une question
   posée une fois par course ».
Lectures interdites — dans la prose du rapport (la citation des questions et des réponses n'est pas visée) : tout verbe
de comparaison (« bat », « dépasse », « reste sous », « fait mieux / moins bien ») entre un score et une référence, un
autre score, 0,5, l'autre course ou le premier pilote ; tout adjectif sur un score ; toute différence calculée ; toute
extrapolation aux organismes auto-écrits ou à Gemini ; toute mention de « apprentissage » ou de « mémoire qui marche » ;
tout jugement d'une réponse (« bonne », « profonde », « fausse », « meilleure que l'autre ou que le collisionneur ») ;
toute mise en rapport d'une réponse avec les scores ; tout lien de cause entre la moisson, les plafonds ou la question et
un score. Les nombres et les références que contient une réponse sont rapportés comme **dires de l'essaim, non vérifiés**
(R7) ; une référence n'entre dans aucun texte avant vérification sur PDF empreinté, page citée.

## Liste d'arrêt

| condition | effet | garde ou vérification |
|---|---|---|
| une course de ce nom déjà partie (manifeste écrit) dans un dossier du pilote, au début ou au départ ; marqueur de départ du conteneur ; verrou présent ; branche `pilotes/<nom>` déjà sur le dépôt distant ; dossier de la tentative existant | la course ne part pas (R3, R12) | script, consigné (essais `tentative-3`, `verrou-present`, `marqueur-present`) |
| **M : S non saine** (liste close : empreintes, lanceur, code de retour, archive, espace attendu, générations 0 et 1 `OK` non invalidées sans anomalie, aucune invalidée au rapport, fin « générations maximales », arrêt « aucune lignée active » ; en réel : S réelle, sous ce GO, graine S du texte, dans le dossier des pilotes ; ligne de dépense de M portant l'empreinte des empreintes de S) ; `S_PILOTE` absent ou non défini | M ne part pas ; décision de Lazar requise | script, étapes (0), (2), (4) (essais `sain-M` et les artefacts `m-…` et `reel-m-…`) |
| code différent de celui de `5d1d4fd` (commit ou arbre de travail, collisionneur compris), commit postérieur hors des pièces du pilote, fichier non suivi ou modifié sous `essaim-m3-refonte-v1` hors des dossiers de pilotes, `4967734a…` ou `90595ffb…` non ancêtre, noyau nettoyé ≠ `d5d0efcc…`, banque, mission ou collisionneur d'autre empreinte ; bibliothèque `anthropic` absente en réel | la course ne part pas | script, consigné ; `sha256_code_noyau` du manifeste rapporté de l'extrait |
| dossier du pilote autre que « 700 0 » ; dépôt hors de `/root` et `/home` en réel ; dépôt non caché pour l'espace attendu ; `ESSAIM_M3_ESPACE` définie en réel ; fichier ignoré (par exemple un `.pyc`) sous `essaim-m3-refonte-v1` hors des `__pycache__` | la course ne part pas | script (essayés) |
| préenregistrement d'empreinte autre, compagnon absent, graine de la course non écrite ou différente de celle que donne l'entropie, entropie absente, marqueur restant, empreinte du lanceur non citée | la course ne part pas | script (essayés) |
| organisme ≠ `50ffcd7d…` ou 19 fichiers non retrouvés ; question ≠ son empreinte | la course ne part pas | script ; le manifeste reconsigne l'empreinte d'arbre et celle de la question |
| aucune ligne `GO-2026-10-25-01` de type calcul portant l'empreinte de la question de la course ; course non consignée dans `registres/depenses.md` ; reste < 60 USD | la course ne part pas | vérification du lanceur, consignée (essayés) |
| test de dépense absent, vide, illisible, vieux de plus de 900 s (date du fichier ou heure d'un appel), une espèce non `OK`, modèle servi non conforme, coût nul, jetons de sortie nuls, autre GO, heure d'appel sans fuseau, heure absente en réel ; trop ancien ou modifié au départ ; attestation de la recharge vide en réel | la course ne part pas | script (essayés) |
| un échec d'essai, un saut quelconque (l'essai arXiv compris), un total ≠ 140, un essai cité non passé dans ce conteneur | la course ne part pas | script (rapport JUnit) |
| course du noyau en cours au décalage 900, au début ou juste avant le départ ; variable d'essai en réel ; clé Brave absente en réel | la course ne part pas (elle attend) | script (essayés) ; voisines aux décalages 0, 700 et 800, essais `pytest` présents au départ : réserve consignée ; autres voisines : consignées ; jamais arrêtées |
| GO absent ou d'un autre type, registre absent, collisionneur d'empreinte inattendue, `ANTHROPIC_BASE_URL` définie, isolation réseau indisponible, noyau non root, clés absentes | refus de lancer (avant le manifeste : tentative suivante permise) | gardes du noyau et du script ; essais `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url`, `test_bac_a_sable_isolation_reseau_refusee_si_indisponible` ; collisionneur et isolation vérifiés après départ par l'extrait |
| `--question-ouverte` sans `--question-ouverte-aux`, question absente, cible mal formée ; question vide | refus avant tout lancement | `cli._question_ouverte`, essais `test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`, `test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts` (P2C1-10) |
| plafond de 60 USD (course) ou de 30 USD (génération) | `PLAFOND` rendu, génération rapportée, course arrêtée au plafond total ; les plafonds ne bloquent pas M (P2C2-02) | `test_appels_paralleles_plafond_tenu_au_pire_cas`, `test_organisme_gourmand_recoit_plafond_sans_exception`, `test_ce312_doit_arreter_et_raison_juste` |
| 3 600 s par génération | `DELAI_DEPASSE` ; garde interne de l'organisme à 75 % du temps (code de l'organisme, `PART_TEMPS_APPELS`) | `test_bac_a_sable_exception_et_delai` ; cohérence du budget de temps avec la moisson : `test_ce311_garde_de_temps_compte_la_moisson` (P2C1-10) |
| modèle servi non conforme | `INVALIDE_MODELE`, lignée arrêtée ; M ne part pas | `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee` |
| crédit épuisé (402 ; « credit balance is too low » en 400 ou sous 200) | `CREDIT_EPUISE` invalidée, course arrêtée, aucune relance ; M ne part pas | `test_ce305_credit_epuise_arrete_la_course`, `test_r395_credit_epuise_rendu_en_400_arrete_la_course` (arrêt de la course) ; départ de M : étape (0) du script |
| journal des appels absent après des appels | `ANOMALIE_NOYAU` invalidée ; M ne part pas | `test_ce307_anomalie_journal_absent` |
| successeur invalide à g0 | g1 = relance de g0, consignée | `test_relance_puis_reprise_remet_le_compteur_a_zero` |
| liens, tubes ou fichiers spéciaux posés par l'organisme | écartés et consignés | `test_fichiers_lecture_et_copie_sans_lien`, `test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau` |
| lecture du dépôt ou de la banque par l'organisme ; voie commune entre courses | refus par le système | `test_cl5_01_banque_cachee_a_l_organisme`, `test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`, `test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course`, `test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus` |
| moisson : source injoignable, 429, document trop gros | statut consigné par le noyau, rapporté par source ; aucune relance | garde de code : `except Exception` de `Rechercheur.rechercher` et de `Telechargeur.telecharger`, plafonds d'octets ; essais `test_moisson_de_bout_en_bout_en_simulation`, `test_ce305_sources_moisson_au_manifeste_et_bras_apparie`, `test_sources_reelles_de_moisson_si_reseau` (aucun n'essaie un 429 ni un document trop gros, P2C1-10) |
| fichier `STOP` (incident technique seulement) | arrêt à la fin de la génération, consigné ; M ne part pas | `test_fichier_stop_arrete_la_boucle` |
| archive fermée incomplète ; espace du manifeste autre que l'espace attendu | copies gardées, jamais lues ni poussées ; réserve ; M ne part pas | script (essayés : `archive-incomplete`, `espace-autre`, `m-archive-incomplete`, `m-espace-autre`) |
| arrêt humain du processus | par PID consigné (R10) | lanceur |

Essais cités (28 ; chacun exigé passé dans le conteneur du lancement) : `test_fichiers_lecture_et_copie_sans_lien`,
`test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau`,
`test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts`,
`test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`,
`test_extrait_mecanique_sain_puis_artefacts`, `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url`,
`test_bac_a_sable_isolation_reseau_refusee_si_indisponible`, `test_appels_paralleles_plafond_tenu_au_pire_cas`,
`test_organisme_gourmand_recoit_plafond_sans_exception`, `test_ce312_doit_arreter_et_raison_juste`,
`test_bac_a_sable_exception_et_delai`, `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee`,
`test_ce305_credit_epuise_arrete_la_course`, `test_ce307_anomalie_journal_absent`,
`test_relance_puis_reprise_remet_le_compteur_a_zero`, `test_fichier_stop_arrete_la_boucle`,
`test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus`,
`test_r395_credit_epuise_rendu_en_400_arrete_la_course`, `test_cl5_01_banque_cachee_a_l_organisme`,
`test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous`,
`test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course`, `test_sources_reelles_de_moisson_si_reseau`,
`test_moisson_de_bout_en_bout_en_simulation`, `test_ce311_garde_de_temps_compte_la_moisson`,
`test_ce305_sources_moisson_au_manifeste_et_bras_apparie`,
`test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait`.

**Essais du lanceur v4** (R5 ; P2C1-11, P2C2-07) : conv-audit, 25 octobre, 10:52–10:57 UTC, root, conteneur du même type, copie du
dépôt à `5d1d4fd` (plus une seconde copie sous `/root` pour les refus du mode réel) ; **98 cas sur 98 conformes**
(`essais-lanceur-pilote2-v4.log`, `e3a4465ab8b95fadfe692cf0e6c299b2364bf33e2c2dac8394a09ebf8dd975e1` ; programme
`essais_lanceur_pilote2_v4.sh`, `7626d7193bbda59ea2af3dd89f553456ba6562a73c8823d22b482167d5cbee9c`). Cas sains : **S
complet** avec préenregistrement d'essai (graine recalculée depuis l'entropie), test de dépense avec heures d'appel
(exigées), essais du noyau exécutés (140 passés, 0 sauté, 28 cités passés), deux générations, réponse archivée, archive
fermée égale au disque, copies retirées, espace attendu sous `/var/lib/essaim-m3/`, utilisateur de l'organisme 60900,
marqueur de départ posé, verrou retiré ; **M** avec S pour course précédente (« S saine », graine de S égale à la graine
S du texte, ligne de dépense de M portant l'empreinte des empreintes de S), rapport JUnit de S repris ; M une seconde fois
jusqu'à l'archive. Artefacts : course M — ligne de dépense sans l'empreinte de S, S absente, empreintes de S altérées,
code de retour non nul, archive incomplète, autre lanceur, autre course, crédit épuisé à g1, modèle non conforme à g0,
anomalie du noyau, une seule génération, arrêt sur `STOP`, arrêt au plafond total (chemin de code gardé), génération
invalidée au rapport, fin de lignée « sans successeur valide », espace autre, graine de S autre, `S_PILOTE` non défini,
S hors du dossier des pilotes, S simulée (refus) ; mode réel — variable d'essai, `ESSAI_EXIGER_HEURE`, `ESSAIM_M3_ESPACE`,
clé Anthropic absente, nom de variable invalide, variable nommée absente, clé Gemini absente, variable Gemini nommée
absente, clé Brave absente, variable Brave nommée absente, attestation vide, dépôt hors de `/root` et `/home` (refus avant
tout appel) ; course ou mode inconnus ; voisine au décalage 900 (refus), à 300 (consignée), à 0, à 700 et sans décalage
(réserve consignée, course partie) ; `pytest` en cours (réserve) ; verrou présent, marqueur présent (refus) ; commit de la
question absent ; arbre modifié (noyau, collisionneur) ; fichier non suivi dans les essais et à la racine
d'`essaim-m3-refonte-v1`, fichier ignoré (`.pyc`) à la racine ; tête de code différente ; commit postérieur hors des
pièces (refus) et dans les pièces (course partie) ; banque ; mission ; dossier traversable ; dépôt non caché ;
préenregistrement d'autre empreinte, sans compagnon, sans la graine, graine de l'autre course, graine hors de
l'entropie, entropie absente, marqueur restant, lanceur non cité ; organisme altéré, fichier manquant ; question altérée ;
ligne du GO sans « calcul », sur deux lignes, d'une seule question, d'un autre GO ; dépense non consignée ; reste sous
60 ; test de dépense vide, vieux de 20 minutes, vieilli avant le départ, modifié avant le départ, statut `ECHEC_API`,
modèle autre, coût nul, autre GO, jetons de sortie nuls, JSON illisible, heure d'appel vieille de 20 minutes, heure sans
fuseau, heure absente alors qu'exigée ; essai en échec, saut de l'essai arXiv, total ≠ 140 ; bytecode sous le noyau
(traité : empreinte inchangée) ; refus du noyau après création de `course/`, puis tentative 2 partie, puis tentative 3
refusée (R3) ; archive incomplète ; espace du manifeste autre que l'espace attendu (réserve) ; fichier imprévu (consigné,
non poussé). Le dépôt d'essai est revenu propre à `5d1d4fd`. Pièces des cas sains : `simulation-lanceur-v4/`
(`LANCEMENT-simulation-structure-v4.md`, `dee1c1fe…` ; `LANCEMENT-simulation-maieutique-v4.md`, `b7f1127a…` ; extraits,
réponses et listes à pousser, chacun avec son `.sha256`) ; les textes de ces réponses sont ceux des doubles de
simulation ; sources « simulation » partout : la moisson réelle n'a jamais tourné de bout en bout (seule la fonction de
recherche arXiv est essayée en réel). Gardes restées sans artefact : la sortie de `tar` en erreur (simulée par l'archive
incomplète) ; un refus avant le manifeste qui laisserait des fichiers ordinaires ; une voisine apparue au décalage 900
entre les deux détections (même fonction) ; `anthropic` absente en réel (la copie d'essai n'a pas la bibliothèque :
consignée « absente » en simulation) ; la branche `pilotes/<nom>` déjà sur le dépôt distant (lecture du dépôt distant
non essayée) ; les corrections de cette v3 n'ont pas été relues par une troisième contre-lecture (signalé, R2) : elles
sont essayées par le lanceur en simulation.

## Pièces

`prereg/pieces-pilote2-gemini-v5-1/` : le lanceur `lancer_pilote2_gemini_v5_1_v4.sh` (`05e2fd0d818915393db769acf6e49c14ca21f58d9ad476cafde708b60e219c31`), ses essais
`essais_lanceur_pilote2_v4.sh` et leur journal `essais-lanceur-pilote2-v4.log`, les pièces des cas sains
`simulation-lanceur-v4/`, le devis `devis-attendu-pilote2-v3.json`
(`093a2d7082b40ffe97ec1c75350feeaf76723c83471b0566524fd9232ab0f54c` ; nombres identiques à la v2) et son script
`devis_attendu_pilote2_v3.py` (`851f38c8b56528b6c4e899a87e8d7844f0010366887c06348d1100791bb7dd79`), le script de
scellement `sceller_pilote2_v2.py` (`373beddc962ed3b577bd3a935fad8709d152a0381688656cdf2dafc7fe642f4f` ; la v1, gardée, attendait un marqueur de plus) ; les versions
antérieures (lanceurs v1 à v3, essais v1 à v3, devis v1 et v2) gardées ; chaque pièce a son `.sha256` ; fichier d'empreintes
`EMPREINTES-pilote2-gemini-v5-1-v3.txt` (+ `.sha256`) sous `pieces-pilote2-gemini-v5-1/`, écrit au scellement par le script de
scellement : <<EMPREINTE_PIECES>>.

## Traitement des constats de la contre-lecture 1 (P2C1-01 à P2C1-14)

| constat | traitement dans ce texte (v2, repris en v3) et dans le lanceur v3 (repris en v4) |
|---|---|
| P2C1-01 (majeur) départ de M sans garde | liste close de « S saine » écrite (§ Deux courses, Seuil, liste d'arrêt) ; étape (0) du script de M : empreintes de S vérifiées, `LANCEMENT.md` de S (même lanceur, course S, code 0, archive fermée), extrait de S (générations 0 et 1 `OK`, non invalidées, sans anomalie ; aucune invalidée au rapport ; fin « générations maximales » ; arrêt « aucune lignée active ») ; cas sain M et 12 artefacts ; ligne de dépense de M écrite après la fin de S |
| P2C1-02 moisson et appels contre le code | g0 sans formulation, ≤ 3 recherches, ≤ 2 téléchargements, ≈ 123 appels ; bloc ≤ 8 notices et 2 extraits ; extrait de 350 caractères coupé à 600 ; argument du § 3 remplacé (scores lus seulement si l'historique a deux entrées) |
| P2C1-03 provenance des téléchargements | provenance exacte (liens rendus par une recherche de la génération, identifiants arXiv, hôtes toujours permis ; redirections https suivies) ; réserve sur l'extraction hors bac à sable ; demande de durcissement à session-depot |
| P2C1-04 test de dépense | « réalité des appels attestée par l'outil, le script vérifie la pièce » ; `heure_utc` par espèce lue quand elle existe ; revérification juste avant le départ ; ce que le test ne garantit pas, dit |
| P2C1-05 frein non étanche | dit (appel en échec compté 0, reprises des clients, entrée estimée, voisine sur le même compte) ; dépense du noyau consignée et rapprochée de la console |
| P2C1-06 isolation et voisinage | protection réelle écrite (utilisateurs, modes, espaces de noms ; `test_ce306…` cité) ; réserve pour une voisine aux décalages 0 et 800 ; détection refaite avant le départ ; dépôt sous `/root` ou `/home` ; dépôt caché vérifié par `dossiers_a_cacher` ; `caches` vérifié après lecture |
| P2C1-07 lectures interdites et canaux | `gNNN.corpus/` et le reste de `gNNN.noyau/` nommés ; canaux écrits par l'organisme déclarés ; exposition par le jeu public dite ; espace attendu consigné avant le départ |
| P2C1-08 moment de lecture | documents nommés (préenregistrement de l'étape 1 qui part, cité au rapport ; inscription dans la v8 de la confrontation ; v7 dite brouillon) ; phrase « l'étape 1 est scellée avant le départ » retirée |
| P2C1-09 devis | pièce v2 : 123 appels à g0 ; seuils de g0 ajoutés (≈ 4 400 et ≈ 4 200 ; écart avec l'estimation de la contre-lecture dit) ; seul « un en vol » vaut pour la question |
| P2C1-10 attributions d'essais | `test_ce311…` réattribué ; garde de 75 % = code de l'organisme ; 429 et document trop gros : garde de code nommée, sans essai ; ligne des refus de `--question-ouverte` rétablie |
| P2C1-11 essais du lanceur | description exacte (cas sain S complet avec les essais du noyau, cas sain M, artefacts) ; moisson réelle jamais de bout en bout, dit (§ 5) |
| P2C1-12 sortie d'erreur | messages de `SystemExit` et d'`argparse` ajoutés ; sorties d'erreur de l'extraction et de `tar` gardées dans des fichiers lisibles, poussés |
| P2C1-13 intégrité | « chevrons et retours chariot retirés » ; versions consignées ; commits postérieurs et fichiers non suivis vérifiés ; seul l'espace attendu est retiré ; `PYTHONPATH` et `ESSAIM_M3_COLLISIONNEUR` retirées ; graines recalculées depuis l'entropie |
| P2C1-14 forme | « pour réduire le risque » ; liste close de ce qui est poussé écrite en noms |

## Traitement des constats de la contre-lecture 2 (P2C2-01 à P2C2-10, et constats de la contre-lecture 1 traités en partie)

| constat | traitement dans ce texte et dans le lanceur v4 |
|---|---|
| P2C2-01 (majeur) S de simulation acceptée | en réel : en-tête « (reel, tentative N) », `manifeste.reel`, `manifeste.go_id`, graine S du manifeste = graine S du texte (étape 2), `S_PILOTE` dans le dossier des pilotes et nommé comme S, empreintes listant `LANCEMENT.md` et l'extrait ; ligne de dépense de M portant l'empreinte des empreintes de S (étape 4) ; essais `reel-m-s-simulee`, `reel-m-s-hors-dossier`, `reel-m-sans-s`, `m-graine-s-autre`, `m-depense-sans-empreinte` |
| P2C2-02 plafonds | écrit : les plafonds ne bloquent pas M ; refus du noyau et dépense de S consignés chez M ; l'artefact `m-plafond-total` garde le chemin de code d'un arrêt au plafond, impossible avec 2 × 30 = 60 ; g1 sans successeur valide nommé comme bloquant |
| P2C2-03 espace autre chez S | refus de M (étape 0) ; essai `m-espace-autre` |
| P2C2-04 décalages des essais | 0, 700, 800 en réserve (900 refusé) ; utilisateurs nommés ; essais du noyau pendant nos courses : règle écrite, `pytest` au départ en réserve ; essais `voisine-decalage-700`, `essais-en-cours` |
| P2C2-05 pousser S avant M | procédure écrite (copie de lancement jamais committée, dossier de S jamais modifié, S poussée depuis un autre arbre, rapprochement dans `registres/depenses.md`) ; fichier d'empreintes du scellement sous `pieces-pilote2-gemini-v5-1/` |
| P2C2-06 R3 non atomique | verrou, marqueur de départ du conteneur, recherche refaite au départ, branche distante ; essais `verrou-present`, `marqueur-present` |
| P2C2-07 nombres | nombres repris du journal v4 ; script du devis v3 (usage, deux extraits) |
| P2C2-08 deux v8 | deux documents nommés, auteurs dits |
| P2C2-09 intégrité | versions lues sans `-I` depuis un dossier neutre ; `git status --ignored` (essai `ignore-racine`) ; `S_PILOTE` non défini : refus consigné |
| P2C2-10 test de dépense | pièce inchangée entre ses deux lectures (essai `td-modifie-avant-depart`) ; `heure_utc` avec fuseau exigée en réel (essais `td-heure-sans-fuseau`, `td-heure-absente-exigee`) |
| P2C1-01, P2C1-04, P2C1-06, P2C1-13 (en partie) | par P2C2-01, P2C2-10, P2C2-04, P2C2-09 ; aucun identifiant de requête exigé (dit) |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 25 octobre 2026, 09:39:29–10:01:23
  UTC), auteur d'aucune pièce ; brouillon relu `pilote2-gemini-organisme-v5-1-v1.md` (`51d1b224…`) et lanceur v1
  (`a26d508f…`) ; rapport `prereg/contre-lectures/pilote2-gemini-organisme-v5-1-v1-cl1.md`
  (`688b1e21f0a7972cc2e9982e557139ecd8929a4990926d50ec7b64a3497011a8`) ; verdict « scellable après corrections » (1
  majeur, 8 mineurs, 5 de forme ; traités ci-dessus).
- **Contre-lecture 2** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 25 octobre 2026, 10:18:21–10:38:11
  UTC), auteur d'aucune pièce ni de la contre-lecture 1 ; brouillon relu `pilote2-gemini-organisme-v5-1-v2.md`
  (`0d718031…`) et lanceur v3 (`bd1e0a2b…`) ; rapport `prereg/contre-lectures/pilote2-gemini-organisme-v5-1-v2-cl2.md`
  (`1b513a0eb8838f9eda9c960b5fddbf8ba9b46e1794e00ed1352cb7b0bba39903`) ; verdict « scellable après corrections » (1 majeur, 4
  mineurs, 5 de forme ; traités ci-dessus).
- **Corrections de cette v3** (contre-lecture 2) et lanceur v4 : essayés en simulation (98 cas), **non relus par une
  troisième contre-lecture** (signalé, R2 ; comme la v3 du premier pilote). Champs remplis au scellement, et eux seuls :
  l'entropie et les deux graines (plan § 2), l'empreinte du fichier d'empreintes des pièces (§ Pièces).
