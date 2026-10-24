# Contre-lecture 1 — préenregistrement « pilote descriptif : l'organisme écrit par Gemini (v3), seul, sur la banque scellée `confrontation-v1` — v1 »

- **Contre-lecteur** : sous-agent neuf, modèle Claude Fable 5.1 (`claude-fable-5-1`). Je n'ai écrit aucune pièce du programme ; je n'ai lu que les dix fichiers nommés dans la consigne ; ni git, ni réseau, ni recherche dans le système de fichiers, ni script exécuté (seulement `date -u`, `sha256sum` et la création du dossier du rapport).
- **Début (UTC)** : 2026-10-24 21:54:52. **Fin (UTC)** : 2026-10-24 22:06:48 (heure lue juste avant l'écriture de ce rapport).
- **Empreinte SHA-256 du brouillon relu** (`pieces/pilote-gemini-organisme-v3-v1.md`, calculée par `sha256sum`) : `3eaf72751c9055bfcbcb3151acde814d5e1bea5a2d029fa03cf9f06edd57fecf`.
- **Verdict** : **scellable après corrections** (version 2, règle R12). Le préenregistrement est bien celui d'un pilote descriptif (aucune hypothèse, aucune prédiction, aucun signe visé, audit symétrique prévu) ; mais sa commande ne part pas telle qu'écrite (une option inexistante), plusieurs énoncés sur le comportement de l'organisme sont inexacts d'après son code, et les gardes de lecture laissent trois ouvertures (relance ou arrêt sur un score, comparaison implicite à la référence de surface, lecture des scores avant le scellement des préenregistrements principaux).
- **Décompte** : 18 constats — 1 bloquant (PG-01), 8 majeurs (PG-02 à PG-09), 7 mineurs (PG-10 à PG-16), 2 de forme (PG-17, PG-18). Plus deux observations hors préenregistrement.

## Ce qui a été vérifié et tient

- Les huit sections exigées par le validateur sont présentes et non vides (`validateur-prereg.py` l. 16-25) ; aucun marqueur « À REMPLIR » ni gabarit `<<…>>`.
- Banque : empreinte `f1387a20…` (préenregistrement l. 16) = `banque-LISEZMOI-v3.md` l. 24 ; partition 80 / 60 / 60 = LISEZMOI l. 27 ; références de surface 0,69 / 0,50 (`test_final`) et 0,75 / 0,58 (`test`) = LISEZMOI l. 46-47.
- Espèces (l. 21) = `contrat.ESPECES_DISPONIBLES` (`contrat.py` l. 14). `ANTHROPIC_BASE_URL` absente = refus du noyau sinon (`cli.py` l. 190-192). Isolation d'utilisateur = le noyau exige d'être root pour cela (`cli.py` l. 193-195).
- Options de la commande (plan § 1, l. 62-65) existantes dans `cli.py` l. 289-333, **sauf une** (PG-01). `--especes` sans valeur donne `[]` (`nargs="*"`, l. 299) et passe le contrôle des noms d'espèces (l. 335-338). `--organisme-impose NOM=CHEMIN@FAMILLE` (l. 304-305, 50-65) : forme respectée, famille `gemini` admise. `--rondes-conception-max` absent → défaut 0 (l. 316) : « sans phase de conception » tient.
- Métrique (l. 50-52) = `taches.evaluer` (exactitude équilibrée (sensibilité + spécificité) / 2, non-réponse comptée comme erreur, `taches.py` l. 202-229) et `taches.calibration` (10 classes, sans réponse q = 1 faux, l. 163-199).
- Organisme : `principal.py` et `mitose_spectrale.py` n'appellent que `appeler`, `especes()` et `budget()` (l. 50, 77, 435) ; ni `rechercher`, ni `telecharger`, ni `entrainer`, ni `predire` : `recherches_max` 0 et `entrainements_max` 0 sont sans effet sur lui. Le code se recopie dans `successeur/organisme/` (`_propager_successeur`, l. 254-273) : « son code se recopie » tient. `max_tokens` demandés : 640 (tâches, l. 321 et 354), 1 024 (induction, l. 452), 512 (vérifications, l. 470) ; une induction et `N_VERIFICATIONS = 2` vérifications (l. 22-23, 446-484).
- Heures : décision 23:52 Paris = 21:52 UTC (Paris est à UTC+2 le 24 octobre 2026, le changement d'heure tombe le 25) ; rédaction 21:54 UTC : cohérent.
- R7 : aucun chiffre d'état de l'art ; sans objet. R3 : aucun signe visé dans le texte. R4 : le critère 1 déclenche le même audit pour un score trop haut et trop bas.

## Constats

### PG-01 — bloquant — l'option `--max-tokens-appel` n'existe pas
- **Où** : Bornes, l. 25-26 (`max_tokens_appel` 4 096) ; Plan d'analyse § 1, l. 64 (`--max-tokens-appel 4096`).
- **Ce qui est** : `cli.py` l. 289-333 ne déclare aucune option de ce nom (ni pour `simuler` ni pour `lancer`) ; `argparse` refuse une option inconnue : la commande du plan, telle qu'écrite, ne part pas. Le 4 096 vient du contrat § 3 (`contrat.py` l. 55-57) : c'est le défaut que le noyau prend pour compter le pire cas d'un appel **sans** `max_tokens` ; ce n'est ni une option ni un plafond. Cet organisme passe toujours un `max_tokens` (640, 1 024, 512) : le défaut ne sert jamais.
- **Correction** : retirer l'option de la commande et la ligne « `max_tokens_appel` 4 096 » des bornes ; écrire à la place « `max_tokens` demandés par l'organisme : 640 (tâches, `principal.py` l. 321, 354), 1 024 (induction, l. 452), 512 (vérifications, l. 470) ; pire cas du noyau compté sur le `max_tokens` demandé (contrat § 3) ».

### PG-02 — majeur — « un appel par tâche » n'est vrai que dans un des deux cas ; le service de `test_final` n'est pas écrit
- **Où** : Devis, l. 28-29 (« un appel de ≤ 640 jetons par tâche ») ; Hypothèse (2), l. 38 ; Métrique, l. 52.
- **Ce qui est** : `planifier_castes_par_mitose` (`mitose_spectrale.py` l. 58-72) calcule, avec `appels_restants` = 160 : réserve = min(6, 160 // 4) = 6 ; appels pour test = 154 ; budget par tâche = 154 // n_tâches ; castes = min(budget par tâche, min(5, 3 espèces + pression 1)). La pression vaut 1 aux deux générations (il faut ≥ 2 entrées d'historique, l. 67-70 ; g1 n'en a qu'une). Donc : si l'organisme reçoit **60** tâches (`test` seul), budget par tâche = 2 → **2 castes** ; et `_traiter_tache` appelle toutes les castes pour chaque tâche dès que `len(castes) > 1` (`principal.py` l. 337-339 : `besoin_arbitrage` est vrai, la condition 0,78 est sans effet) → **2 appels par tâche** (castes `monoculture_analytique` et `monoculture_croisee`, deux espèces). Si l'organisme reçoit **120** tâches (`test` et `test_final` mêlés), budget par tâche = 1 → 1 caste → 1 appel par tâche. Dans les deux cas ≈ 123 appels par génération (3 d'entraînement + 120), sous `appels_max` 160. Le préenregistrement ne dit pas comment `test_final` est servi à l'organisme ; or ce point décide du nombre de castes, des espèces appelées et du coût. `boucle.py` n'est pas dans les pièces : **non vérifiable ici**. Si `test_final` n'était pas dans `taches_test`, aucune réponse n'existerait pour lui et la « part sans réponse de 100 % » du critère 1 se déclencherait par construction.
- **Correction** : écrire le mode de service de `test_final` (mêlé à `taches_test` sans marque, ou non ; citer la ligne de `boucle.py` ou le test) et le nombre de tâches reçu par l'organisme ; en déduire explicitement « 1 caste, 1 appel par tâche » ou « 2 castes, 2 appels par tâche » et ≈ 123 appels par génération ; corriger le devis attendu en conséquence (voir aussi PG-12).

### PG-03 — majeur — l'ordre de `especes()` choisit les castes ; « famille nominale gemini » ne dit pas quelles espèces répondent
- **Où** : Espèces servies, l. 21-22 (« l'organisme choisit ses castes parmi `especes()` ; aucune n'est choisie pour lui ») ; Objet, l. 13 (« famille nominale `gemini` »).
- **Ce qui est** : la caste `idx` prend `especes[idx % len(especes)]` (`mitose_spectrale.py` l. 76) : la **première** espèce de la liste rendue par le noyau est la caste primaire, l'inducteur (`principal.py` l. 447) et le calibrateur (l. 468) ; la deuxième est la caste croisée. Si la liste est dans l'ordre de `contrat.ESPECES_DISPONIBLES` (`contrat.py` l. 14 ; l'ordre réellement servi est dans `boucle.py`, **non vérifiable ici**), la caste 1 est `CLAUDE_FABLE_5_1`, la caste 2 `CLAUDE_OPUS_5_5`, et `GEMINI_ARGON` n'est appelée par aucune caste (au plus 2 castes ici, PG-02). L'ordre est donc un choix du noyau, pas de l'organisme, et « l'organisme de Gemini » pourrait ne faire répondre que des modèles d'Anthropic.
- **Correction** : inscrire l'ordre de la liste servie par `especes()` (ligne de code ou test) ; le rapporter avec le nombre d'appels par espèce (déjà prévu, l. 36) ; remplacer « aucune n'est choisie pour lui » par « l'ordre de la liste servie par le noyau fixe la caste primaire » ; ajouter dans « Ce que ce pilote ne dit pas » : « "organisme de Gemini" désigne le code, pas les modèles appelés ».

### PG-04 — majeur — statuts rapportés incomplets : `TRONQUE`, `VIDE`, `ANOMALIE` manquent
- **Où** : Hypothèse (1), l. 36.
- **Ce qui est** : le contrat § 3 (`contrat.py` l. 50-52) connaît huit statuts ; le préenregistrement n'en rapporte que cinq. `TRONQUE` est le mode d'échec le plus probable de cet organisme : `max_tokens` 640 pour une réponse qui doit d'abord exposer les faits puis finir par un objet JSON (`principal.py` l. 246-250), et le noyau rend `texte` vide sur `TRONQUE` ; l'organisme ne compte alors pas l'appel (l. 81) et la tâche peut rester sans réponse. Un rapport « mécanique » qui omet ce statut manquerait l'information principale.
- **Correction** : rapporter les huit statuts du contrat, par espèce et par génération, plus `echecs_par_statut`, `erreurs` et `bascule_parallele_a_la_tache` du `journal_generation.json` de l'organisme (`principal.py` l. 576-595), à côté des journaux du noyau.

### PG-05 — majeur — rien n'interdit une seconde course, un `STOP` ou une lecture pendant la course sur la foi d'un score
- **Où** : Plan § 1, l. 62 (« Une course ») ; Liste d'arrêt, l. 97 (fichier `STOP`) ; Métrique, l. 52 (« lu une fois »).
- **Ce qui est** : le préenregistrement ne dit pas ce qui se passe si la course échoue en partie (pannes d'interface, plafond) ni qui peut écrire `STOP` et pour quelle raison. Une relance avec une autre graine « parce que g0 a mal tourné », ou un `STOP` écrit après avoir vu le score de g0 dans `evenements.jsonl`, serait un run choisi sur résultat (R3) et une lecture avant la fin (l. 52).
- **Correction** : ajouter aux critères gelés et à la liste d'arrêt : « une seule course sous ce préenregistrement ; toute seconde course est un préenregistrement v2 qui cite ce qui a déjà été lu ; `STOP` et l'arrêt par PID (R10) ne sont permis que pour une raison mécanique écrite d'avance (dépense, clé compromise, ordre de Lazar), jamais pour un score ; aucun score n'est lu pendant la course (ni `evenements.jsonl`, ni l'archive, ni la sortie standard) ; une course au statut autre que `OK` est rapportée telle quelle, sans relance ».

### PG-06 — majeur — « préenregistrements principaux déjà écrits » ≠ scellés : fuite des scores réels vers eux
- **Où** : Plan § 4, l. 76-77 ; Métrique, l. 52.
- **Ce qui est** : le pilote lit des scores réels sur `test` et `test_final` de la banque même qui doit servir la confrontation (`banque-LISEZMOI-v3.md` l. 5-6). Si les préenregistrements principaux sont écrits mais non scellés quand ces scores sont lus, leurs auteurs auront vu des résultats réels avant scellement (R1 des principaux), et rien ici ne l'interdit. Le pilote a par ailleurs un but mécanique légitime (statuts, coûts, l. 6-7) dont les enseignements doivent pouvoir servir ; le texte ne distingue pas ce que le pilote peut informer de ce qu'il ne peut pas.
- **Correction** : « les scores du pilote (`test` et `test_final`) ne sont lus qu'après le scellement des préenregistrements principaux, dont les empreintes sont citées dans le rapport du pilote ; la mécanique (statuts, nombre d'appels, coûts, durées) peut être lue avant et peut motiver des changements de bornes dans des préenregistrements non scellés, consignés comme décisions ; aucun score ne motive aucun changement ».

### PG-07 — majeur — lectures interdites trop lâches : référence de surface, 0,5, adjectifs, écart nommé
- **Où** : Critères gelés, l. 85-86 (« bat / ne bat pas … ») ; Banque, l. 17-18 et Hypothèse (2), l. 39 (« à côté des références de surface ») ; Hypothèse (3), l. 40 (« l'écart g1 − g0 »).
- **Ce qui est** : les points de suspension laissent ouverte la comparaison à la référence de surface et à 0,5 ; or le LISEZMOI (l. 49-51) dit que tout score d'organisme « se lit contre cette référence » : mettre la colonne à côté des scores sans règle de prose invite la phrase « au-dessus / en dessous de la référence », qui ferait du pilote une preuve. Rapporter un « écart g1 − g0 » comme quantité nommée invite de même la lecture d'un apprentissage, que la l. 86 interdit.
- **Correction** : compléter la liste : « aucune phrase comparant un score du pilote à la référence de surface, à 0,5, à une autre génération ou à un autre organisme ; la référence est une colonne du tableau sans commentaire ; aucun adjectif (bon, faible, prometteur, décevant) ; aucune phrase sur ce que l'organisme "détecte" ou "comprend" ». Rapporter les scores de g0 et de g1 ; ne pas calculer d'écart nommé (ou, s'il est gardé, le faire suivre de la phrase gelée l. 84).

### PG-08 — majeur — correctif des liens symboliques : « essais » manuels, commit inconnu, pas de test nommé (R5)
- **Où** : Code, l. 19-20 ; Liste d'arrêt, l. 92.
- **Ce qui est** : la première ligne de la liste d'arrêt fonde le départ du pilote sur un correctif dont le commit n'est pas encore écrit (« inscrits au scellement ») et dont la garde est vérifiée par des « essais de session-depot », non par un test de la suite. R5 demande une garde testée sur un cas sain et sur un artefact, sans repli silencieux ; les autres lignes de la liste citent un test nommé, celle-ci non. La validation du successeur refuse bien les liens symboliques dans l'arbre (`contrat.py` l. 238-240), mais la faille visée (lecture par lien dans le bac à sable) est ailleurs : **non vérifiable ici**.
- **Correction** : nommer le test automatisé qui couvre les trois artefacts cités (lien vers un fichier 0600, vers `/proc/self/environ`, tube nommé) et le cas sain ; écrire « le pilote ne part pas tant que ce test n'est pas dans la suite et vert » ; citer le commit complet (40 caractères) et l'empreinte de l'arbre du noyau dans la version scellée.

### PG-09 — majeur — `--especes` vide : lecture cohérente avec `cli.py`, mais non vérifiable au-delà
- **Où** : Plan § 1, l. 66 ; Espèces servies, l. 21-22 ; Devis, l. 28 (« aucun amorçage »).
- **Ce qui est** : `--especes` sans valeur donne `[]` (`cli.py` l. 299) ; `_imposes_et_especes` rend `[]` et le commentaire de la l. 82 confirme que `[]` veut dire « aucune espèce n'amorce » ; `lancer` appelle pourtant `noyau.amorcer()` (l. 231) et c'est `boucle.Noyau` (absent des pièces) qui décide si `[]` ouvre une lignée auto-écrite et si `especes()` rend bien les trois espèces à la lignée imposée. **Non vérifiable ici.** Si la lecture était fausse : soit des lignées d'amorçage non prévues (dépense jusqu'au plafond, pilote qui n'est plus « l'organisme seul »), soit `especes()` vide → aucune caste (`mitose_spectrale.py` l. 54-56) → 100 % sans réponse.
- **Correction** : citer le test (ou la ligne de `boucle.py`) qui montre les deux faits ; à défaut, consigner dans `EMPREINTES-pilote-v1.txt` un essai `simuler` de la commande exacte (sans `--reel`, `--go`, `--registre-go`, `--taches`) dont la sortie `lignees` ne montre que la lignée imposée avec `impose` vrai (`cli.py` l. 108).

### PG-10 — mineur — GO « préparatifs » : identifiant et type non écrits
- **Où** : Devis, l. 29-31 ; Plan § 1, l. 62 (`--go <GO préparatifs> --registre-go <extrait>`) ; Liste d'arrêt, l. 93.
- **Ce qui est** : `--registre-go` attend « la ligne du GO (type « calcul ») » (`cli.py` l. 332) et la liste d'arrêt prévoit « GO d'un autre type → refus ». Le préenregistrement nomme un GO « préparatifs » sans son identifiant `GO-AAAA-MM-JJ-NN`, sans son type, et le « 200 USD jusqu'à lundi » n'est rattaché à aucune ligne du registre. Le refus serait sûr, mais le plan ne partirait pas.
- **Correction** : inscrire l'identifiant, le type tel que le noyau l'exige, le montant et la fin de validité du GO dans la version scellée ; écrire que l'extrait passé à `--registre-go` contient cette ligne.

### PG-11 — mineur — relance sur successeur invalide et empreinte de l'arbre de g1
- **Où** : Objet, l. 14-15 (« la seconde reçoit la mémoire `memoire_isvd.json` ») ; Bornes, l. 27 (`--relances-max 1`).
- **Ce qui est** : si le successeur de g0 est invalide (`valider_organisme`, `contrat.py` l. 234-268), g1 est une relance de g0 (contrat § 6, l. 131-135) : même code, sans `memoire_isvd.json` transmis (hors ce que `charger_connaissances_archive` lit dans l'archive). Par ailleurs l'arbre de g1 diffère de `3e6fe2e9…` par `memoire_isvd.json` et `etat_generation_precedente.json` (`principal.py` l. 265-272).
- **Correction** : « si le successeur de g0 est invalide, g1 est une relance ; le rapport le dit et ne parle d'aucune transmission » ; rapporter l'empreinte de l'arbre `organisme/` de g1 à côté de celle de g0.

### PG-12 — mineur — chiffres sans chemin ni empreinte (R6)
- **Où** : l. 12 (`320cd34`), l. 17 (« 10 sur 10 »), l. 17-18 (références de surface), l. 29 (« ≈ 10 à 15 »), l. 31 (« 136,63 »).
- **Ce qui est** : « étiquettes vérifiées par paires (10 sur 10) » n'a ni chemin ni empreinte, et le LISEZMOI-v3 (l. 58-59) dit cette vérification « à faire, sur 20 traces » : **non vérifiable ici**. « 136,63 » (répétition générale) n'a aucune référence. Les références de surface renvoient au LISEZMOI-v3 sans son empreinte. Le devis attendu « ≈ 10 à 15 » repose sur un nombre d'appels inexact (PG-02) et sur un tarif non cité. Le commit est donné en 7 caractères.
- **Correction** : chemin + empreinte du rapport de vérification des étiquettes (ou retirer la phrase) ; retirer 136,63 ou renvoyer à la ligne du registre des dépenses ; empreinte du LISEZMOI-v3 ; devis attendu recalculé (≈ 123 appels par génération, 1 ou 2 castes, textes ≤ 20 000 caractères) avec le tarif cité, ou marqué « ordre de grandeur, non opposable » ; commit en 40 caractères.

### PG-13 — mineur — entrées non figées : mission, chemins, fichier d'empreintes
- **Où** : Plan § 1, l. 62-65 (`<banque>`, `<pilote>`, `<…>/organisme`, `<extrait>`) ; Code, l. 20 (`EMPREINTES-pilote-v1.txt` sans chemin).
- **Ce qui est** : la commande ne passe pas `--mission` ; le noyau lit alors `MISSION-v1.md` à la racine du dépôt (`cli.py` l. 22, 26), et cette mission entre dans le prompt d'induction de l'organisme (`principal.py` l. 219) : c'est une entrée du run, sans empreinte. Les chemins de sortie et de banque ne sont pas écrits ; le fichier d'empreintes n'a ni chemin ni compagnon `.sha256`.
- **Correction** : fixer chaque chemin dans la version scellée (sortie versionnée, R12 : par exemple `runs/pilote-gemini-organisme-v3-v1/`) ; ajouter `--mission` explicite ou l'empreinte de `MISSION-v1.md` dans `EMPREINTES-pilote-v1.txt` ; donner le chemin de ce fichier et son `.sha256`.

### PG-14 — mineur — critère 1 limité à `test_final` ; auditeur non nommé
- **Où** : Critères gelés, l. 81-82.
- **Ce qui est** : les scores de `test` sont lus aussi (l. 38) mais ne déclenchent aucun audit ; l'audit ne dit pas qui le fait ni qu'il n'autorise aucune relance. Les bornes 0,95 et 0,30 ne sont pas symétriques autour de 0,5 (observation seulement ; je ne propose aucun autre chiffre).
- **Correction** : mêmes déclencheurs sur `test` ; « audit fait par un sous-agent neuf, sur les journaux, les étiquettes, les textes et les indices de surface ; sans relance ; son rapport est joint ».

### PG-15 — mineur — liste d'arrêt : temps, successeur invalide, arrêt par PID et lieu d'exécution absents
- **Où** : Liste d'arrêt, l. 90-98.
- **Ce qui est** : rien sur `temps_max_s` 1 200 (l'organisme cesse d'appeler à 75 % du temps, `principal.py` l. 24, 39-45, 527-528 : effet, tâches sans réponse) ; rien sur la relance puis l'arrêt de lignée sur successeur invalide (contrat § 6) ; rien sur l'arrêt d'urgence par PID (R10) ni sur le lieu d'exécution (aucune instance payante ? sinon identifiant et GO).
- **Correction** : trois lignes dans le tableau, chacune avec sa garde ou son test.

### PG-16 — mineur — pièces absentes de la contre-lecture (R2) et déclaration R1 sur les corrections
- **Où** : consigne et Contre-lecture, l. 102-103 (« brouillon relu : ce fichier ») ; Hypothèse (1), l. 37 (« taille de la mémoire transmise ») ; l. 8 (« aucune lecture de résultat avant scellement »).
- **Ce qui est** : je n'ai pas eu `memoire_isvd.py` (importé `principal.py` l. 12-16 ; il lit l'archive et fait la mémoire dont la taille est rapportée), ni `boucle.py` / `appels.py` (service des espèces, plafond, vue de l'archive, `test_final`), ni les tests cités l. 93-98, ni `CORRECTIONS-v1.md`. **Non vérifiables ici** : que `memoire_isvd.py` n'appelle pas `noyau_client` ; que la vue de l'archive servie à g1 ne porte ni vérité ni score `test_final` (le contrat § 2, l. 33-35, dit « leur score » sans préciser) ; que les corrections C-01 à C-10 de l'organisme n'ont pas été faites en le faisant tourner sur `confrontation-v1` ou ses sources.
- **Correction** : ajouter ces pièces à la contre-lecture 2 ; inscrire dans le préenregistrement : « l'organisme n'a jamais tourné sur `confrontation-v1` ni sur ses sources ; ses corrections ont été faites sur … (chemin, empreinte) » et « la vue de l'archive ne porte ni vérité ni score `test_final` (test …) ».

### PG-17 — forme — ce qui manque pour que le validateur passe, et comment lui faire tenir les champs à remplir
- **Où** : Contre-lecture, l. 102-106 ; placeholders `<…>` l. 62-65 ; titre l. 1.
- **Ce qui est** : l'entrée « Contre-lecture 1 » est reconnue (`ENTREE`, validateur l. 29) mais ne contient aucune empreinte : `problemes()` rend « contre-lecture 1 sans ses deux empreintes » (l. 53-56) et `sceller_prereg` lève `GardeArret`. Les gabarits `<GO préparatifs>`, `<extrait>`, `<banque>`, `<pilote>`, `<graine>`, `<…>` ne sont pas détectés par `GABARIT` (`<<[A-Z0-9_]+>>`, l. 27) : le validateur laisserait sceller un texte à trous. Le titre porte « (À CONTRE-LIRE) ».
- **Correction** : inscrire l'empreinte du brouillon relu (`3eaf72751c9055bfcbcb3151acde814d5e1bea5a2d029fa03cf9f06edd57fecf`) et celle de ce rapport ; écrire les trous en `<<GO_PREPARATIFS>>`, `<<CHEMIN_BANQUE>>`… pour que le validateur refuse tant qu'ils restent ; lister en une ligne les champs remplis au scellement (commit et empreintes du noyau, entropie E et graine, GO, chemins, empreinte du rapport, titre) pour que la différence brouillon → scellé soit vérifiable ; retirer « (À CONTRE-LIRE) » du titre de la version scellée.

### PG-18 — forme — graine : source d'entropie, manifeste de run, place dans le texte (R9)
- **Où** : Plan § 2, l. 68-69 ; Contre-lecture, l. 105.
- **Ce qui est** : E est tirée par `secrets.randbits(128)` puis passée à `SeedSequence(E)` ; le dépôt tire l'entropie par `numpy.random.SeedSequence()` (LISEZMOI-v3 l. 21-23). Les deux voies passent par `SeedSequence` ; mais R9 demande un manifeste par run (configuration et empreinte, versions, graines, commit) que le préenregistrement ne nomme pas, et E est à inscrire dans la section « Contre-lecture », qui sert à R2.
- **Correction** : « E et la graine dérivée inscrites au plan § 2 et dans le manifeste du run (chemin), avec la version de numpy et le commit » ; `--graine` reçoit l'entier dérivé (`cli.py` l. 298, `type=int`).

## Observations hors préenregistrement (à transmettre, sans effet sur le verdict)

- `cli.py` l. 6 (« refuse de tourner en tant que root sans accord explicite ») contredit le code l. 193-195, qui **exige** root : la docstring est fausse, le lanceur doit savoir qu'il faut être root.
- `gemini-principal.py` l. 19 dit « Version 2 » alors que `VERSION = "organisme-gemini-m3-v3"` (l. 21) : incohérence de commentaire dans l'arbre scellé.

## Réponses aux cinq points de la consigne

1. R1, R3, R4, R6, R7, R9 : R3 et R7 tenus ; R4 prévu (PG-14 pour l'étendre à `test`) ; R1 tenu pour le pilote mais ouvert vers les préenregistrements principaux (PG-06) et sur l'origine des corrections (PG-16) ; R6 : plusieurs chiffres sans chemin (PG-12) ; R9 : manifeste non nommé (PG-18).
2. Bornes et code : une option inexistante (PG-01) ; `--especes` vide et `--organisme-impose` conformes à `cli.py` ; `especes()` et `budget()` appelés par l'organisme comme dit ; 1 ou 2 appels par tâche selon le service de `test_final` (PG-02), ≈ 123 appels par génération, sous 160. Le pire cas de 40 USD tient par le noyau (`usd_max` 20 × 2 générations, `--plafond-total` 40, pire cas au `max_tokens` demandé, contrat § 3), sous réserve de PG-09 et du test cité l. 95, **non vérifiables ici** ; les appels de contrôle sont hors des 40 USD, ce que le texte dit.
3. Strictesse des lectures : insuffisante sur trois points (PG-05, PG-06, PG-07).
4. Fuite ou lecture de `test_final` : aucune par conception dans le texte ; deux ouvertures de procédure (PG-05, PG-06) ; vue de l'archive non vérifiable (PG-16).
5. Validateur : deux empreintes à inscrire dans « Contre-lecture 1 » (PG-17) ; le reste passe.

## Compte rendu

Préenregistrement de pilote descriptif bien construit (aucune hypothèse, aucun signe, audit symétrique), mais non scellable tel quel : une option de commande inexistante (`--max-tokens-appel`), le nombre d'appels par tâche et les espèces appelées dépendent du service de `test_final` et de l'ordre de `especes()`, non écrits, et trois gardes de lecture manquent (une seule course, scores lus après le scellement des principaux, aucune comparaison à la référence de surface).
Verdict : scellable après corrections, en v2 ; empreinte du brouillon relu `3eaf72751c9055bfcbcb3151acde814d5e1bea5a2d029fa03cf9f06edd57fecf` ; 18 constats (1 bloquant, 8 majeurs, 7 mineurs, 2 de forme).
Non vérifiable ici faute de pièces : `boucle.py`, `appels.py`, `memoire_isvd.py`, les tests cités, `CORRECTIONS-v1.md`, le rapport de vérification des étiquettes.
