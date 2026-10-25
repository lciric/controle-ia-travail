# Contre-lecture 1 du préenregistrement du troisième pilote (Gemini v5.3 puis v6) — `pilote3-gemini-organisme-v5-3-v6-v1.md`

- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit ; auteur d'aucune pièce de ce pilote, ni de T2.
- **Date** : 25 octobre 2026, de 14:18:44 à ≈ 14:40 UTC (heures lues sur `date -u`).
- **Méthode** : lecture seule des fichiers listés, par leur chemin exact. Aucune recherche récursive, aucune commande git,
  aucun sous-agent. Aucun lanceur, essai ou code d'organisme exécuté. Commandes lancées : `date -u`, `sha256sum`, `wc`,
  `stat`, `sed -n` (lecture de lignes), `diff` et `cmp` entre les deux lanceurs, un calcul de jour de la semaine
  (`python3 -I`, module `datetime` seul), et des recherches de motifs limitées à un seul fichier listé à la fois.
- **Texte modifié pendant la contre-lecture.** Le fichier contre-lu a été réécrit à 14:18:46 UTC, deux secondes après
  le début. Ma première lecture portait peut-être sur la version précédente. Je l'ai relu en entier ensuite. Seul
  changement vu : l. 22–25, ajout de la réponse de Lazar de 15:18 (heure de Paris), « Recommandation : (a), confiance
  moyenne. : ok ». **Ce rapport porte sur la version `69a3cbff…`** (empreinte refaite à 14:36 UTC). Les numéros de ligne
  cités sont ceux de cette version.

## Fichiers lus (sha256)

| fichier | sha256 |
|---|---|
| `prereg/pilote3-gemini-organisme-v5-3-v6-v1.md` (texte contre-lu) | `69a3cbff81918664c34c452b7be538cf4d5556a79ecd9fd0ed88a257ff97beb1` |
| `prereg/pilote2-gemini-organisme-v5-2-v2.md` (T2) | `d294465429094e5099cb5facdad95e2b806aa8953640b57bcab99998396c066b` |
| `prereg/pieces-pilote3-gemini-v5-3-v6/lancer_pilote3_gemini_v5_3_v6_v1.sh` | `5a56d8546ac4f81a96acdfd1acfe09bbe3a8b8ca255976c70c7d06148ca87050` |
| `prereg/pieces-pilote3-gemini-v5-3-v6/diff-lanceur-v5-vers-pilote3-v1.txt` | `0121d1e934b1b13e63bd2a732b4b200ce06cf6aad17d268e4056579706a2c8fc` |
| `prereg/pieces-pilote2-gemini-v5-2/lancer_pilote2_gemini_v5_2_v5.sh` (lu en partie : l. 1–150 et 186–355) | `83f8b9cf8f3062dfc5e2c02094c602a2d582adf0cbcef292d5bdccd8f8d61b1b` |
| `prereg/pieces-pilote3-gemini-v5-3-v6/essais_lanceur_pilote3_v5_3_v6_v1.sh` | `f7cb5f762711746c0d91655ff062181f0d69660103dd8ebe4f7ef3d6fbc772e3` |
| `prereg/pieces-pilote3-gemini-v5-3-v6/verification-objets-v5-3-v6-v1/LISEZMOI-v1.md` | `acb2c3ae5c1a25f6efc41919ea137a628d8091b71523d2a7e67dfad84d184562` |
| `prereg/pieces-pilote3-gemini-v5-3-v6/sceller_pilote3_v1.py` | `54861a0f4b78a4b444ea1d007ae6db72576d74663879842acb27f5b2da5355c6` |
| `/var/tmp/verif-pousses-v53-v6/v6/organisme/principal.py` (l. 80–100, 718–730, 880–1019, 1440–1480, 1500–1600, 1630–1730, 1855–2017) | `7278e3f93f6ff5d2be26763657d074882a8a73c9905a0b5b6707c850718914c1` |
| `/var/tmp/verif-pousses-v53-v6/v53/organisme/memoire_isvd.py` (l. 60–288) | `9b8889d9d696caf73b3491370d28ae17e2880ef3b58d588fe46d1088b75feb86` |
| `/var/tmp/verif-pousses-v53-v6/v53/organisme/mitose_spectrale.py` (l. 50–129) | `dcba040c45d7936dfb8732bc5aa935052529ce2bf9963dacaa51dbc4f81ae492` |
| `essaim_m3/noyau/boucle.py` (l. 540–649, plus des recherches de motifs) | `218052dd2f30c99ad659932d7b3e90a9289854db63ee319119b5fe87e1a8020c` |
| `essaim_m3/noyau/contrat.py` (l. 1–160) | `06333cb397cfe548167fb456c8217dd7df5b7639ab8c39244c06ac0774442dd8` |

Les chemins sans racine sont sous `/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/`.

## Verdict

**Scellable après corrections** : 2 constats majeurs (la porte entre v5.3 et v6 ; la ligne du GO), 8 mineurs et
3 remarques.

## Vérifié et conforme

- **Empreintes citées.** Elles sont toutes égales à celles que j'ai calculées : T2 `d2944654…`, lanceur de T2 `83f8b9cf…`,
  lanceur du pilote 3 `5a56d854…`, écart `0121d1e9…`, rapport de vérification `acb2c3ae…`.
- **Écart au lanceur de T2.** Je l'ai recalculé par `diff` : il est identique octet pour octet à la pièce. Il ne touche
  que ce que le texte annonce : en-tête, courses, objets, GO, chemins permis, étape (0), messages. Les `COMMUNES` et la
  commande du noyau sont inchangés.
- **Objets.** Commits, empreintes d'arbre, nombres de fichiers (22 et 24), lignées et noms de course sont cohérents entre
  le texte, le lanceur, les essais et le rapport de vérification (§ 1 et § 3 du rapport).
- **Résumé de la vérification.** Il est fidèle au rapport : 39 et 43 essais passés ; 28 et 29 appels ; métrique
  0,231448 → 0,195747 ; neuf réserves ; défaut bloquant du § 9.3.
- **Renvois.** Tous les numéros de ligne de T2 cités par le texte sont justes : 58–85, 120–130, 146–315, 266–279,
  318–332, 339–345, 349–353, 357–403, 363–367, 412–482, 432–437, 451–456, 483–489, 490–498, 500–525 et 527–557.
- **Porte « M de référence »** (lanceur l. 193–272). C'est le même code Python que l'étape (0) de T2, avec les valeurs
  de M : nom et empreinte du lanceur, lignée, GO. S'y ajoutent l'empreinte de T2, vérifiée, et la graine M lue dans T2.
  Les quatre cas demandés sont traités :
  - M simulée : refusée en réel (essais `reel-reference-simulee`, `reel-reference-tentative-simulee`) ;
  - M d'un autre lanceur : refusée (`m-autre-lanceur`, `m-sous-lanceur-pilote3`) ;
  - M d'une autre graine : refusée (`m-graine-autre`) ;
  - M d'une autre copie : acceptée seulement si ses empreintes se vérifient, donc avec le même contenu (voir P3C1-11).

  Il y a 22 artefacts de M et 5 refus en mode réel. La M saine des essais est produite par le lanceur scellé de T2
  lui-même, avec le texte et la graine scellés.
- **Graines.** Le motif « graine de la course v5-3 = … » / « v6 = … » est celui que cherche le lanceur (l. 328). L'enfant
  0 va à v5.3 et l'enfant 1 à v6, dans le texte, le lanceur (l. 49, 55, 333) et le script de scellement (l. 37–43). Le
  script refuse s'il reste un marqueur autre que les siens : `<<APPELS_SIMULATION>>` et `<<ESSAIS_DU_LANCEUR>>` doivent
  donc être remplis avant lui (bonne garde).
- **Chemins de lignée.** Ils sont transposés par la variable `LIGNEE` (lanceur l. 53, 59, 597, 605). La liste de ce qui
  est poussé est inchangée.
- **Défaut bloquant de la v6 inerte : affirmation vérifiée à la lecture.** Le seul point non vérifié est l'absence de
  la clé dans tout le noyau (voir P3C1-06).
  - `principal.py` de la v6, l. 907–921 : la mutation n'est tentée que si la phase est « conception », si
    `autoriser_mutation_code` est vrai, ou si `generation >= 1` avec stagnation. La stagnation exige
    `len(historique) >= 2` et deux scores non nuls.
  - Le contexte construit par `boucle.py` (l. 617–633) porte `"phase": "generation"`. Avec `--rondes-conception-max 0`,
    aucune ronde n'a lieu (l. 850 et 871). L'historique vient de `self.archive.historique(lignee)` (l. 630), et le
    contrat (l. 47–51 et 152–154) n'y met que les générations passées : une seule entrée à g1, relance comprise. Le
    contexte n'a aucune clé `autoriser_mutation_code`, et ni `boucle.py` ni `contrat.py` n'en contient d'occurrence.
  - `verifier_et_valider_code_politique`, donc le code candidat sans borne, n'est appelé qu'à la l. 1008, derrière la
    garde de déclenchement.
  - Sans mutation, le successeur est une copie de l'organisme, plus la mémoire et l'état (l. 1454–1477).
- **Score de g0 recopié à g1 : affirmation vérifiée à la lecture.**
  - `memoire_isvd.py`, l. 101–113 : le score de g0 est écrit dans `score_noyau`.
  - Le retour arrière (l. 117) et le delta (l. 135) n'agissent qu'avec deux scores. Avec un seul, le statut vaut la
    constante « REFERENCE_G0 » (l. 144–145).
  - `mitose_spectrale.py`, l. 73–76 et 115–118 : la mitose exige aussi deux entrées à l'historique.
  - Le résumé de mémoire servi aux consignes de g1 est calculé au début de g1 (`principal.py` l. 1698), sur la mémoire
    écrite par g0 sous un historique vide. La mise à jour qui porte le score n'intervient qu'à la fin (l. 1908–1922),
    après les tâches, la question et l'appel de mutation. Aucun effet sur les consignes de g1 ne se lit dans le code.
  - Pour les tâches, une seule caste : `budget_par_tache` = (160 − 6) // 120 = 1, d'après `mitose_spectrale.py`
    l. 64–78. Pas d'arbitrage à une caste (`principal.py` l. 1586). La phrase du critère 3, « une espèce appelée pour
    les tâches », tient donc à la lecture.

## Constats

### P3C1-01 — majeur — La porte entre v5.3 et v6 n'est ni mécanique, ni la règle de T2, ni essayée

- **Lieu** : texte l. 84–89 et l. 242 ; table l. 49–50 ; lanceur l. 205–272 (l'étape (0) ne lit que M, pour les deux
  courses) ; T2, liste d'arrêt l. 546–548, 553–554 (« S ne part pas »).
- **Constat.** Pour que v6 parte, le texte se contente d'une lecture humaine du `LANCEMENT.md` de v5.3 : « code de
  retour : 0 » et archive fermée. C'est bien plus faible que la liste close « M saine » qu'appliquait T2 à la seconde
  course, alors que Lazar a écrit : « Mêmes règles de refus que pour M et S » (R-440). Quatre problèmes :
  - **Issues non vues.** Une v5.3 au code 0 avec g0 en `INVALIDE_MODELE`, g1 en `ANOMALIE_NOYAU`, plus de 20 % d'appels
    hors `OK` (panne d'environnement, le cas même de P52C1-02), aucun appel `OK` de Fable, un arrêt sur `STOP`, une fin
    « sans successeur valide » ou une génération invalidée laisserait partir v6, qui se perdrait de la même façon.
  - **Crédit épuisé invisible.** Le `LANCEMENT.md` ne porte ni les statuts des générations ni la raison de l'arrêt.
    Un « arrêt sur crédit épuisé » n'y est donc visible que si le noyau rend alors un code non nul, ce que je n'ai pas
    pu vérifier (`cli.py` est hors de ma liste).
  - **Renvoi ambigu.** La table ne dit pas ce que devient « S » dans les lignes de la liste d'arrêt de T2 (« S ne part
    pas »), reprises « ligne à ligne, pour chaque course » (l. 236). Lue avec S = v6, une `INVALIDE_MODELE` de v5.3
    arrête v6 ; lue avec la l. 84–89, qui prévaut en cas de conflit, elle ne l'arrête pas.
  - **Ordre non tenu, garde non essayée.** Rien n'empêche mécaniquement v6 de partir avant v5.3, et la garde n'a ni cas
    sain ni artefact (R5).
- **Correction.**
  - **(a), recommandé.** Écrire un lanceur v2 où, pour `COURSE=v6` (toujours en réel), une variable comme
    `PRECEDENTE_V53` pointe sur le dossier de v5.3. On lui applique la même liste close, paramétrée : nom et empreinte
    de ce lanceur, en-tête « pilote3-gemini-v5-3-maieutique-v1 (reel, tentative N) », « - course : v5-3 ; », lignée
    `gemini-organisme-v5-3`, `GO-2026-10-25-02`, graine v5-3 de ce texte. On y ajoute une ligne de dépense de v6 portant
    les 16 premiers caractères des empreintes de v5.3, puis un cas sain et des artefacts.
  - **(b), à défaut.** Écrire la liste close complète dans le texte, appliquée par session-depot à l'extrait de v5.3
    (fichier lisible (a)) et consignée.
  - **Dans les deux cas**, ajouter à la table la ligne : « S ne part pas » (liste d'arrêt de T2) se lit, pour une issue
    de v5.3, « v6 ne part pas ».

### P3C1-02 — majeur — La ligne du GO est mal décrite pour être écrite juste du premier coup

- **Lieu** : texte l. 26–36, 68–71, 199–200, 243 ; lanceur l. 355–367.
- **Constat.**
  - **Ce que dit le texte.** Il annonce « une seule ligne, de type calcul, portant l'empreinte de la question
    `8b1c7511`, celles des deux objets […], celle de ce texte scellé et celle du lanceur ». Or la ligne de R-440 existe
    déjà, sans aucune empreinte, et elle annonce « une ligne d'extension avant chaque course ».
  - **Ce que le lanceur exige.** Une ligne qui commence par `| GO-2026-10-25-02 |` et porte, sur la même ligne,
    « calcul », `8b1c7511` et les 8 premiers caractères de l'arbre de l'objet de la course : `6251ab21` ou `940c59c3`.
    Il ne lit ni l'empreinte du texte ni celle du lanceur.
  - **Ce qui manque.** Le texte ne cite pas R-440 et ne donne pas la forme exacte de la ligne (T2 la donnait, l. 288–291).
    Il ne dit pas non plus que cette ligne et la ligne de dépense doivent être poussées sur `main`, puis récupérées dans
    la copie du pilote 3 (`git fetch origin main`) avant chaque course : le lanceur lit `origin/main`.
  - **Conséquence.** Une ligne mal écrite fait refuser le lanceur après la création du dossier. Cela consomme la seule
    tentative permise sans Lazar (R-439).
- **Correction.** Citer R-440, puis donner les deux formes exactes, par exemple :
  - ligne d'extension du GO :
    `| GO-2026-10-25-02 | 2026-10-25 | calcul | extension : empreintes du pilote 3 publiées par « conv-audit » (R-440) — v5.3 4ecba58, arbre 6251ab219e86286e… ; v6 7cd7508, arbre 940c59c3dd58fdd5… ; question M v2 épurée 8b1c751174b3d24d… ; préenregistrement <empreinte> ; lanceur <empreinte> ; périmètre, plafond, échéance et conditions inchangés | 120 USD au plus pour les deux courses | 2026-10-31 | Lazar | R-… |`
  - ligne de dépense, une par course :
    `| 2026-10-25 | pilote3-gemini-v5-3-maieutique-v1 | GO-2026-10-25-02 | 60 USD au pire cas | après la fin de M ; empreintes de M <16 premiers caractères> |`

  Dire aussi que le manifeste consignera dans `registre_go` la première ligne de l'identifiant, celle de R-440, sans
  empreinte, et que le rapport le dira (transposition de P52C1-14). Enfin, ajouter à la condition « prêtes » (l. 68–71)
  la ligne d'extension poussée sur `main`.

### P3C1-03 — mineur — Deux lanceurs peuvent se chevaucher : la garde des voisines a une fenêtre

- **Lieu** : texte l. 62–67 et l. 246 ; lanceur l. 107–120 et 500.
- **Constat.**
  - **La fenêtre.** Le refus d'une voisine au décalage 900 ne voit qu'un processus `essaim_m3 lancer|simuler` en
    cours. Pendant la phase d'avant départ d'un autre lanceur (≈ 3 minutes d'essais `pytest` du noyau, qui tournent sous
    l'utilisateur 60900), ou pendant l'archivage final de M après la fin de son noyau, aucune voisine n'est vue.
  - **Premier risque : deux courses à la fois.** Deux lanceurs (pilote 3 et S, par exemple) peuvent passer leurs deux
    détections et partir ensemble, au même utilisateur 60900. L'isolation entre courses, qui repose sur des
    utilisateurs distincts, ne tient plus, et S s'en trouve touchée.
  - **Second risque : une tentative perdue.** Un lanceur du pilote 3 parti juste après le noyau de M est refusé à
    l'étape (0), faute d'`EMPREINTES-pilote-v1.txt`, et brûle la tentative unique de R-439.
  - T2 rangeait déjà « une voisine apparue entre les deux détections » parmi les gardes sans artefact. La chaîne compte
    désormais quatre courses, lancées sans Lazar.
- **Correction.** Écrire la règle de procédure : « un seul appel de lanceur à la fois dans le conteneur, second pilote
  compris ; session-depot ne lance un lanceur qu'après la fin de la commande de fond du précédent (pour la première
  course du pilote 3, après l'écriture des empreintes de M) ».

### P3C1-04 — mineur — R-439 n'est pas cité, et l'effet sur S d'un arrêt du pilote 3 n'est pas dit

- **Lieu** : texte l. 68–71, 84–89 et 244.
- **Constat.**
  - **R-439 absent.** Le texte renvoie à T2 (« sauf décision contraire de sa part consignée ») sans citer cette décision
    contraire, R-439 : une seule nouvelle tentative sans Lazar, après correction de l'environnement seulement, même
    commande, dossier « -tentative2 » ; pour tout autre refus, une M non saine, un arrêt en cours de course ou un
    dépassement, « tu t'arrêtes, tu consignes et tu attends mon retour ».
  - **Conflit sur S.** Lu à la lettre, R-439 fait qu'une v5.3 arrêtée en cours de course arrête toute la chaîne, v6 et
    S compris. Le texte, lui, n'arrête « que le pilote 3 » et laisse entendre que S part (« son lanceur ne dépend en
    rien de ce pilote », l. 70).
  - **Condition de Lazar non définie.** R-440 dit : « Si la vérification ou la contre-lecture les arrête, elles
    attendent mon retour. » Le texte ne dit pas ce que veut dire « la contre-lecture les arrête » : verdict « non
    scellable » seulement, ou aussi des constats majeurs traités sans seconde contre-lecture ?
  - **Condition « prêtes » incomplète.** Elle omet ce que le GO exige : les empreintes des objets, du texte scellé et
    contre-lu et du lanceur publiées par conv-audit sur le canal.
- **Correction.**
  - Citer R-439 pour chacune des deux courses.
  - Écrire, issue par issue (refus avant le manifeste, autre refus, arrêt en cours de course, v5.3 non saine), si S
    part encore. À défaut d'un mot de Lazar, la lecture littérale de R-439 suspend aussi S.
  - Définir « la contre-lecture les arrête » et compléter la condition « prêtes ».

### P3C1-05 — mineur — Un canal de lecture précoce nouveau : la taille de la mémoire de g1

- **Lieu** : texte l. 142–146 ; `memoire_isvd.py` l. 101–113, 228–234 et 249 ; `principal.py` de la v6 l. 1919–1922.
- **Constat.**
  - **Le mécanisme.** À g1, la v5.3 et la v6 écrivent `memoire_isvd.json` avec `score_noyau`, le score `test` de g0,
    au format `json.dumps`. La taille de ce fichier dépend donc de la longueur d'écriture du score.
  - **Pourquoi c'est un canal.** T2 rapporte la taille de `memoire_isvd.json` (l. 324). Si l'extrait mécanique la
    porte, elle est lisible dès la fin de la course. Je ne l'ai pas vérifié : l'outil d'extraction est hors de ma liste.
  - **Ce qui manque.** T2 déclarait le canal analogue de la taille de `contexte.json` (l. 428–432). Le texte ne déclare
    pas celui-ci.
  - **Citation.** L'affectation est à la l. 113, et non dans la plage l. 101–112 citée.
- **Correction.** Ajouter ce canal aux « canaux dits et acceptés », ou établir que l'extrait ne porte pas cette taille.
  Corriger la citation en l. 101–113.

### P3C1-06 — mineur — « Aucune occurrence dans `essaim_m3/` » n'est appuyée sur aucune pièce

- **Lieu** : texte l. 127.
- **Constat.** L'affirmation n'est rattachée à aucune pièce (R6). J'ai vérifié `boucle.py` et `contrat.py` seulement :
  aucune occurrence, et la construction du contexte (l. 617–633) n'a pas cette clé. Je n'ai pu vérifier ni
  `bac_a_sable.preparer` (qui reçoit le contexte), ni `archive.historique`, ni `cli.py`, ni le reste du noyau.
- **Correction.** Citer la recherche (commande, fichiers, résultat, empreinte du journal), ou restreindre l'affirmation
  à ce qui a été lu : « contexte construit en `boucle.py` l. 617–633, sans cette clé ».

### P3C1-07 — mineur — Deux faits de la vérification sont inexacts

- **Lieu** : texte l. 108–109 ; rapport l. 3–6 et l. 63–64.
- **Constat.**
  - **« Aucune exécution hors des essais de Gemini ».** Le rapport dit avoir aussi exécuté `invariance_v1.py`, qui fait
    tourner les organismes sous un faux noyau (cas B et D, trois graines), et `verrous_imbriques_v1.py`. Les relevés
    cités l. 113–114 viennent justement de ces exécutions.
  - **L'heure.** Le texte donne « ≈ 13:30–13:51 UTC ». Le rapport se date « vers 15 h UTC », heure impossible puisque
    postérieure au début de cette contre-lecture (14:18 UTC) : sans doute l'heure de Paris, qui est UTC+1 depuis ce
    25 octobre. Il dit aussi avoir commencé à 14:47 « heure de la machine ».
- **Correction.** Écrire les exécutions réelles (essais de Gemini et les deux outils d'essai, en isolation). Donner
  l'heure d'après une pièce horodatée, ou dire l'incohérence.

### P3C1-08 — mineur — Des passages de T2 propres à la v5.2.1 ne sont pas traités

- **Lieu** : texte l. 152–159 ; T2 l. 169–175, l. 263–265 et l. 437–446.
- **Constat.** Le texte écarte seulement « ce que T2 dit de la moisson ». Restent dans les plages incorporées par renvoi,
  sans traitement :
  - le service des tâches : g0 ≈ 123 appels et g1 ≈ 129 (l. 263–265), autre chose pour la v5.3 et la v6 ;
  - les espèces servies, avec `principal.py` l. 877 pour l'espèce qui formule les requêtes (l. 169–175) ; c'est la
    l. 1130 en v6 ;
  - les expositions du plan § 3, « dans la v5.2.1, ces documents entrent dans chaque consigne de tâche » (l. 437–446).
- **Correction.** Dire pour chacun de ces passages s'il est repris, revérifié sur la v5.3 et la v6, ou non transposé.
  Mon constat de lecture pour la v6 : une caste pour les tâches (voir plus haut) ; formulation par la première espèce
  servie (l. 1130).

### P3C1-09 — mineur — Le moment de lecture et l'escalier dépendent d'événements non bornés

- **Lieu** : texte l. 57, 58 et 208–212.
- **Constat.**
  - **La version 8 de la confrontation** doit citer les archives du pilote 3. Rien n'est dit pour deux cas : elle doit
    être scellée avant la fin du pilote 3 (par exemple, pilote 3 après S, ou arrêté entre v5.3 et v6) ; ou v6 ne part
    pas, et il n'y a qu'une archive.
  - **L'escalier.** Les courses « ne comptent dans l'escalier que si un de ses bras est exactement leur configuration ».
    Si ce préenregistrement est écrit après la lecture de leurs scores, le choix des bras peut en dépendre (R1).
- **Correction.** Écrire deux règles :
  - « sinon, une version suivante de la confrontation, scellée avant toute lecture des scores du pilote 3, cite ses
    archives avec la même déclaration ; avec une seule course, une archive » ;
  - « elles ne comptent dans l'escalier que si son préenregistrement, scellé avant toute lecture des scores du pilote 3,
    le dit ».

### P3C1-10 — mineur — Champs remplis après la contre-lecture et pièces non citées (R2, R5, R6)

- **Lieu** : texte l. 167, 250, 254–260 et 264–265.
- **Constat.**
  - **Champs non relus.** `<<APPELS_SIMULATION>>` et `<<ESSAIS_DU_LANCEUR>>` seront remplis après cette contre-lecture,
    donc sans contre-lecture (R2). Le texte ne le dit pas, contrairement à T2.
  - **Cas non refaits.** Le programme d'essais compte 83 cas et 11 vérifications, soit 94 contrôles. Il ne refait pas
    les gardes communes suivantes :
    - préenregistrement : compagnon absent, entropie absente ;
    - essais du noyau : `junit-saut` ;
    - test de dépense : vieilli ou modifié au départ, coût nul, modèle autre, jetons nuls, pièce illisible, heure sans
      fuseau ;
    - dépôt et code : dossier traversable, dépôt non caché, banque, mission, arbre modifié, fichier non suivi ou ignoré,
      bytecode ;
    - course : espace autre, voisines à 0, 700 et 300, `pytest` en cours.

    Elles valent par identité des lignes : l'écart, que j'ai vérifié, ne les touche pas. Il faut le dire (R5).
  - **Pièces sans empreinte.** Le § Pièces ne cite pas le script de scellement `sceller_pilote3_v1.py` (`54861a0f…`), ni
    l'empreinte du programme d'essais (`f7cb5f76…`) (R6).
- **Correction.** Dire dans le texte que les deux champs ne sont pas contre-lus. Dans le champ des essais, dire quels
  cas de T2 valent par identité des lignes et lesquels sont refaits. Citer les deux pièces avec leur empreinte.

### P3C1-11 — remarque — Porte « M de référence » : des précisions

- **Lieu** : texte l. 72–73 et 79–81 ; lanceur l. 210–213 et 268–270.
- **Constat.**
  - **Emplacement de M.** Le texte place `REFERENCE_M` « dans la copie de lancement du second pilote ». Le lanceur
    accepte tout dossier sous `/root` ou `/home` qui porte le bon nom. Une copie des fichiers poussés de M passe si ses
    empreintes se vérifient : c'est sans conséquence, le contenu étant le même.
  - **Branches non essayées.** `go_id` et `reel` du manifeste en mode réel (inaccessibles sans forger un en-tête
    « reel ») ; empreintes de M sans `LANCEMENT.md` ou sans extrait ; extrait illisible.
  - **Cas limite hérité de T2.** Une `entropie_seed_sequence` vide passerait le `grep` « = \b » de la l. 270.
- **Correction.** Aligner le texte sur le lanceur. Remplacer la recherche par une égalité exacte : la graine du
  manifeste, entière, égale à celle de T2.

### P3C1-12 — remarque — Formulations à préciser

- **Lieu** : texte l. 135, 139, 140–141, 144–145 et 245.
- **Constat.**
  - **Ligne d'arrêt l. 245.** « Aucun effet (le successeur de g1 ne tourne pas) » ne vaut que pour un appel fait à g1.
    À g0, cas impossible à la lecture, g1 ferait tourner un successeur qui ne s'importe pas.
  - **« Jamais à un organisme à l'exécution » (l. 140–141).** Les emprunts sont dans le code lui-même : requêtes de
    réserve envoyées à g0, `CONCEPTION.md`.
  - **Numéros de ligne sans version.** « `principal.py` l. 724 et 725 » et « l. 85–96 et 86–97 » ne disent pas de quelle
    version il s'agit : en v6, ce sont les l. 724–725 et 86–97 (`REQUETES_RESERVE_SCIENTIFIQUES`) ; en v5.3, une ligne
    plus haut.
  - **Mitose.** Les gardes sont aux l. 73 et 115 de `mitose_spectrale.py`.
- **Correction.**
  - Écrire « à g1 », et ajouter que, à g0, l'appel est rapporté et g1 jugée selon T2.
  - Écrire « jamais servies par le noyau ».
  - Nommer la version de chaque citation de ligne.

### P3C1-13 — remarque — Points non lus et garde de numpy

- **Lieu** : texte l. 13–14, 164 et 256 ; script de scellement l. 10–11 et 37–39.
- **Constat.**
  - **Non lus.** L'erratum des graines de hachage (`06c28c7a…`) et `deriver_lanceur_pilote3_v1.py` (`d431b45d…`) sont
    hors de ma liste. Le texte ne dit ni ce que change l'erratum pour le renvoi, ni s'il est scellé et contre-lu.
  - **numpy.** Le script de scellement ne vérifie pas numpy ≥ 1.25 (R9).
  - **Tests de dépense.** Le texte ne dit pas s'ils sont imputés à `GO-2026-10-25-02` et comptés dans le reste, comme
    R-407 le faisait pour GO-01. Sinon, la dépense totale peut dépasser 120 USD de quelques millièmes.
- **Correction.** Dire le statut de l'erratum et ce qu'il change. Ajouter le contrôle de version au script. Écrire
  l'imputation des tests de dépense.

## Non vérifié (hors de ma liste ou non exécutable)

- `bac_a_sable.py`, `archive.py`, `cli.py`, l'outil d'extraction et le reste de `essaim_m3/` : clés ajoutées au contexte,
  contenu exact de l'historique, code de retour du noyau sur un crédit épuisé, champs de l'extrait (taille de la mémoire).
- `politique_endogene.py` : code exécuté au niveau du module, à l'import.
- `principal.py` de la v5.3, et `CONCEPTION.md` des deux objets.
- Les commits, branches et poussées : aucune commande git.
- Le résultat de la batterie d'essais du lanceur, encore en cours.

## Décompte

13 constats : 2 majeurs (P3C1-01, P3C1-02), 8 mineurs (P3C1-03 à P3C1-10), 3 remarques (P3C1-11 à P3C1-13).

**Recommandation de procédure.** Si P3C1-01 est traité par un lanceur v2, ce lanceur et l'écart v1 → v2 devraient être
relus par un sous-agent neuf avant tout départ. Sinon, selon le mot de Lazar (« si la vérification ou la contre-lecture
les arrête, elles attendent mon retour »), les courses du pilote 3 passent après S, ou attendent Lazar.
