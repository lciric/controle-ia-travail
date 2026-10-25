# Préenregistrement — pilote descriptif : l'organisme écrit par Gemini (v4), seul, sur la banque scellée `confrontation-v1`, avec une question ouverte posée à la génération 1 — v3

Remplace la v2 (`pilote-gemini-organisme-v4-question-v2.md`,
`4b89795cd571c5246a2a0de7c2aaace3a3431784d3ffe6a7f48859efa1a800e5`, gardée, R12), vérifiée par la contre-lecture 4
(« scellable après corrections », 8 constats PG4-01 à PG4-08, traités en fin de texte), qui remplaçait la v1
(`pilote-gemini-organisme-v4-question-v1.md`, `6ef156778a5f6315cdd201919585250fce33afd227ec0e95fff3d028b11ed038`),
contre-lue (contre-lecture 3 : « scellable après corrections », 16 constats PG3-01 à PG3-16), et les brouillons
`pilote-gemini-organisme-v3-v1.md` (`3eaf72751c9055bfcbcb3151acde814d5e1bea5a2d029fa03cf9f06edd57fecf`) et
`pilote-gemini-organisme-v3-v2.md` (`5b956645e87ad829fe6db5c14b99f2c3a3c4ccaefcd66252d0a07f4dbb5e65ae`), jamais scellés,
dont les contre-lectures 1 et 2 sont traitées ici. Décisions de Lazar (heure de Paris) : 24 octobre, 23:52 — « (a) Oui,
pilote descriptif préenregistré d'une page, sous ton GO « préparatifs » (≤ 200 USD jusqu'à lundi) … : go » ; 25 octobre,
00:55 — objet **v4** de l'organisme de Gemini avec la question ouverte « réécrire sa structure ou apprendre dedans »
posée **à la génération 1 seulement** (option (b), recommandée) : « go » ; 00:59 — « lance le pilote cette nuit à la
suite du scellement, tu as mon accord anticipé » ; 01:45 — moissonneur : (b), « goooo » (ce pilote tel quel, sans
moisson ; une v5 de Gemini avec moissonneur et un second pilote plus tard). But : voir ce que donne **déjà**, sur les deux
familles de tâches réelles, l'organisme conçu par Gemini (code figé, mémoire spectrale transmise) ; répéter la chaîne
réelle (espèces réelles, banque réelle, noyau isolé) avec statuts et coûts ; et recueillir, comme **matériau** pour le
dessin des régimes de budget du noyau, la réponse de son essaim à une question ouverte, posée avant qu'il ait vu quoi que
ce soit de notre part. **Aucune hypothèse n'est testée** ; tout est rapporté. Rien d'opposable (R7) ; aucune lecture de
résultat avant scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4).

- Auteur : lignée conv-audit. Date : 2026-10-25, 00:43 UTC (heure lue sur `date -u` ; les heures de Paris citées sont
  celles des messages de Lazar). Lanceur : lignée session-depot (clés), **dans son conteneur** (root, `unshare`
  disponible ; aucune instance payante : le pilote n'a besoin d'aucune carte), au moyen du script
  `prereg/pieces-pilote-gemini-v4/lancer_pilote_gemini_v4_question_v3.sh` (`322275c06d2ad88e13ffe1d4fbd77d1e610bddeebef447d38c45b7630ffeb680` ; remplace la v2,
  `d0293ad4dd14dc3400ebd2c2ceab07375a3fbf9c4b683fd36d8bba94e0153794`, gardée), qui exécute le plan § 1 et § 3 pas à pas
  et refuse, avec sa raison consignée, à chaque écart (la vérification du statut de l'appel de contrôle et celle du reste
  sur la ligne du GO sont du lanceur, consignées ; le script contrôle la présence de leurs pièces) ; processus consigné par son PID dans `LANCEMENT.md`, arrêt par PID
  (R10).
- **Objet** : `gemini-organisme-v4` — branche `outils/gemini-organisme-v4`, commit
  `b64bb3e4c0ae8fd500d09de939ff5a48dc7aec10`, dossier `outils/gemini-organisme-v4/organisme/`, **16 fichiers**, sans
  `memoire_isvd.json` ni `etat_generation_precedente.json` ni `__pycache__` (liste : `EMPREINTES-organisme-v1.txt` de la
  branche), empreinte d'arbre `c5ada33581fd7675f2cec5331d9a9a50ff80271b543c22eef80a64882730c1b9` calculée par
  `boucle.empreinte_arbre` (chemins relatifs triés + empreinte de chaque fichier), la même que le noyau consigne au
  manifeste (`organismes_imposes.*.empreinte_arbre`). Famille nominale `gemini` (N-040 (3)). Lignée imposée unique,
  **sans phase de conception** (`--rondes-conception-max 0` ; son code se recopie), **G = 2** générations notées (g0, g1 :
  la seconde reçoit `memoire_isvd.json` et l'historique de la première ; `--relances-max 1` : si le successeur de g0 est
  invalide, g1 relance g0 et c'est consigné). Déclaration (R1) : la v4 a été écrite par Gemini (relais de Lazar, 25
  octobre 00:44 Paris) **sans connaître le texte de la question** (la demande ne décrivait que la primitive) ; ses
  fichiers v3 sont au contenu identique à ceux de l'arbre v3
  (`3e6fe2e96d6133ab0bfae39009133897d335966d25e5dd48832d6a5d88dc6ba7`, dossier `outils/gemini-organisme-v3/organisme` au
  commit `320cd34eafac8a5d4b6f571ee782a6cef457e43d`), aux fins de ligne finales et à une marque d'ordre d'octets près ;
  ses ajouts ne touchent que la question ouverte ; sans question, son flux est celui de la v3 ; les corrections v1 et v2
  de la v3 (`CORRECTIONS-v1.md`, `-v2.md`, R-345, R-353 ; mesures d'entrée dans
  `outils/gemini-organisme-v2/demonstration-v1-v2.txt`, branche `outils/gemini-organisme-v2`, commit
  `b4c3774ff72b99abf11475ada35b4efc072be633`, `710d24554cfa686bf06fcf6b27f33952651c3646c3338d50add66c1c8b68aee7`) ont été
  faites par session-depot avant tout run réel, sur des simulations sans score réel ; aucune correction ne vient d'un
  résultat réel. Ses 20 essais passent en isolation (`outils/gemini-organisme-v4/LISEZMOI-v1.md`). **Simulation avec la
  question réelle** : le script de lancement, en mode simulation (appels factices, aucun modèle réel), sous un code
  identique à `cec6dce` (tête `5aca4aaf61f5d7c426f04b5d45754d0687fa4471`), avec la question `d967b212…` servie à g001 :
  deux générations `OK`, cinq castes planifiées, `reponse-question.md` archivé ; pièces
  `prereg/pieces-pilote-gemini-v4/simulation-lanceur-v2/` — `LANCEMENT-simulation-v1.md`
  (`0bf93757bc099366f6172d6dc513e8b9cb11d3dc4a3b155e3b40485de52ac94a`), `extrait-mecanique-simulation-v1.json`
  (`39241a6a10b79adeea5813aa371bed68153a3272fd06859368542559f4f430ff`), `reponse-question-g001-simulation-v1.md`
  (`7aa87221f46f4d0bb412c1f9cf38beaa75abcf755bac444aacb2c36c9cd7f8fd`), `A-POUSSER-simulation-v1.txt`
  (`9a2186ecf02c9f9030f29b635cc73d7789d210d9cfa420cf67b5b8e1ff0e2789`). Les textes de cette réponse sont ceux des doubles
  de simulation : ils ne disent rien de ce que diront les modèles réels.
- **Question ouverte** : `question-reecriture-vs-apprentissage-organismes-v1.md`, branche `canal/conv-audit-n04`, commit
  `003995208431e825605bab9c4c1894b7508ad6ab`, `d967b212082315c7b4fa1c42ab1b5d551b3bc1d3c4a98cdeb58eccd58b5b9441`
  (2 702 caractères) : un en-tête pour l'organisme, puis le corps de la question posée au collisionneur
  (`question-reecriture-vs-apprentissage-v1.md`, `89d8c3db754f8ff6c39cedf139ddfe35b8d4d6288bdc7a6eb60697f3a8e2229d`),
  identique sauf la phrase d'introduction des points, tournée sans « Je veux » ; sans aucune réponse ni matériau de notre
  part. Posée par le noyau (`--question-ouverte … --question-ouverte-aux g001`, contrat § 7) à la **seule génération 1** :
  la délibération n'entre dans aucune mémoire transmise à une génération notée ultérieure (il n'y en a pas), et g0 → g1
  reste « code figé, mémoire transmise ». À g0, `contexte["question_ouverte"]` vaut null.
- **Banque** : `essaim-m3-refonte-v1/banque/banque-confrontation-v1.json`,
  `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc` (80 / 60 / 60 : `banque/LISEZMOI-v3.md`,
  `66855d2ab0d89d6fdea9bd85ff41005c7aa16c5f9e7f55cdc0c4fbff7f0299af`) ; étiquettes des traces vérifiées par paires,
  10 paires sur 10 (`banque/verification-etiquettes-paires-v1/LISEZMOI-v2.md`,
  `d9761e6f3920d586347903c9ee0425adfba2d928e29df9b71e1e2d7cc4341b97`). Références de surface (`LISEZMOI-v3.md`) :
  `test_final` conscience d'évaluation 0,69, contrôle de délégation 0,50 ; `test` 0,75 et 0,58 (colonnes du tableau,
  jamais comparées). Vérifiée par `sha256sum` avant le départ (le champ `sha256_banque` du manifeste est l'empreinte
  d'un vidage JSON trié, pas celle du fichier).
- **Mission** : `essaim-m3-refonte-v1/MISSION-v1.md`, `bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e`,
  vérifiée par `sha256sum` avant le départ.
- **Code** : commit **`cec6dce3b1e2d4c1514f63914face859e8a59d97`** de `outils/essaim-m3-gradient-v1-travail` (tête réunie
  des deux lignées : contient `4967734a62a0b10c3b5cd6360e21924f015053fd`, correctif de la faille des liens — essais
  `test_fichiers_lecture_et_copie_sans_lien`, `test_depot_ne_suit_aucun_lien_de_l_organisme`,
  `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau` — ; CE3-04 à CE3-07, CE3-11, CE3-12 de session-depot ; la
  primitive `question_ouverte` — essais `test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts`,
  `test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score` ; l'outil
  `essaim_m3/outils/extrait_mecanique.py` — essai `test_extrait_mecanique_sain_puis_artefacts`) ; 114 essais. Le lanceur
  part d'une copie du dépôt dont `essaim-m3-refonte-v1/essaim_m3/` et `essaim-m3-refonte-v1/tests/` sont identiques à
  ceux de `cec6dce`, au commit (`git diff --quiet cec6dce HEAD -- …`) **et dans l'arbre de travail**
  (`git diff --quiet cec6dce -- …`, `git status --porcelain -- …` vide hors `__pycache__`) : les commits postérieurs
  n'ajoutent que ce texte et ses pièces ; la tête de session-depot (vivier de conception, CE3-17) n'est **pas** ce code ;
  tout autre code vaut nouvelle version de ce texte. Le champ `commit` du manifeste sera la tête de la copie du lanceur,
  non `cec6dce` ; c'est l'identité du code qui fait foi. Empreinte du code du noyau : `boucle.empreinte_arbre(essaim_m3/noyau)`
  sans `__pycache__` = `68494279ec42fc13366f83cc67c502c67ed6dcf97f0678bb568aaae8010772fb` (calculée sur `git archive
  cec6dce`) ; le champ `sha256_code_noyau` du manifeste hache **tout** fichier présent sous `essaim_m3/noyau`, bytecode
  compris (défaut signalé à session-depot) — d'où, au plan § 1, le nettoyage et `PYTHONDONTWRITEBYTECODE=1`. Empreintes des
  fichiers du noyau et des pièces : `prereg/pieces-pilote-gemini-v4/EMPREINTES-pilote-gemini-v4-question-v3.txt`
  (+ `.sha256`), écrit au scellement.
- **Espèces servies** : `especes()` rend la liste triée du noyau, `["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5",
  "GEMINI_ARGON"]` (`serveur.py`, `sorted(ESPECES)`). Règles de l'organisme (`mitose_spectrale.py`) : pour les tâches, la
  caste primaire et l'inducteur prennent la **première** espèce ; avec 120 tâches servies et 160 appels, il planifie
  **une** caste (`budget_par_tache` = (160 − 6) // 120 = 1) : **toutes ses réponses aux tâches viendront de Fable**. Pour la
  question (g1, après les tâches), `planifier_castes_question_ouverte` planifie `min(appels restants, 5)` castes dans
  l'ordre des espèces : **5 castes planifiées** attendues (Fable, Opus, Argon, Fable, puis l'arbitre Opus) ; le nombre de
  contributions peut être moindre (troncature, refus, garde de temps : voir Bornes). Dit d'avance, rapporté (appels par
  espèce et par rôle). Un refus d'une espèce sur la question (`REFUS`) est un échec compté par l'organisme et consigné ;
  **aucune reformulation, aucun second essai** (règle de Lazar sur les refus de filtre). Clés : `ANTHROPIC_API_KEY` ; la
  clé Gemini **passée au noyau sous le nom `GEMINI_API_KEY`** (`cli.lancer` l'exige), prise dans `GEMINI_API_KEY_2` (la
  clé n° 2) si elle est définie, sinon dans `GEMINI_API_KEY` ; le script consigne le nom de la variable source, jamais
  la valeur ;
  `ANTHROPIC_BASE_URL` retirée de l'environnement du run ; `BRAVE_API_KEY` inutile (`recherches_max` 0 ; l'organisme
  n'appelle ni `rechercher` ni `telecharger`).
- **Bornes** : par génération `appels_max` 160, `usd_max` 20, `temps_max_s` **1 800** (le brouillon v3-v2 disait 1 200 ;
  porté à 1 800 **pour réduire le risque** que la question, traitée après les 120 tâches, soit coupée par la garde interne
  des 75 % du temps de l'organisme ; ce risque demeure : la bascule en parallèle de l'organisme ne réserve rien à la
  question, et à latence moyenne d'un peu moins de 11 s par appel les tâches finissent près de 1 350 s ; une contribution
  à 1 200 jetons, ou l'arbitre à 1 500, peut aussi revenir `TRONQUE`, texte vide ; ces cas donnent le texte d'abstention ou
  le texte minimal de l'organisme, avec `reponse` vrai, rapportés tels quels, critère 2 ; sans effet sur le pire cas en
  dollars), `recherches_max` 0, `telechargements_max` 0, `entrainements_max` 0, aucun `--traits` ; `--plafond-total`
  **40 USD** ; `--isoler-reseau`, isolation d'utilisateur (noyau en root), `--decalage-uid 0` (aucune autre course ne
  tourne dans ce conteneur pendant le pilote ; s'il en tourne une, le pilote attend) ; `--parallele-max 8` ;
  `--relances-max 1` ; `--max-tokens-appel 4096` (rabat au-dessus de 4 096 seulement : l'organisme demande 640 par tâche,
  1 024 pour l'induction, 512 par vérification, 1 200 par caste de la question, 1 500 pour l'arbitre — sans effet, dit pour
  la forme).
- **Service des tâches** : en génération notée, le noyau sert `test` et `test_final` **mêlés** (120 tâches, sans
  distinction, ordre tiré par la graine de la génération) ; l'organisme fait 1 appel d'induction (8 exemples stratifiés
  de `train`), 2 appels de vérification, puis 1 appel par tâche : ≈ 123 appels par génération ; à g1, jusqu'à 5 appels de
  plus pour la question : ≈ 128, sous 160 ; pire cas en dollars tenu par le noyau : 20 USD par génération (réservation
  au `max_tokens` demandé), 40 la course.
- **Devis au pire cas** : 2 × 20 = **40 USD** (aucun amorçage : lignée imposée). Ordre de grandeur attendu, **non
  opposable** : ≈ 10 à 14 USD la course, dont ≈ 0,35 USD au plus pour la question
  (`prereg/pieces-pilote-gemini-v4/devis-attendu-pilote-gemini-v4-v1.json`,
  `e01db1499e6a5815633224a44131a56dd2b595412bfca218ea30895ae1eb2767` : longueurs des 120 textes servis de la banque,
  tarifs du collisionneur lus par `appels.modele_de` — Fable et Argon 10 USD par million de jetons d'entrée et 50 en
  sortie, Opus 4 et 20 —, convention du collisionneur de 3 caractères par jeton d'entrée (`cv.cout_pire_cas`), 300 à
  640 jetons de sortie par tâche). Sous **GO-2026-10-24-07** (« préparatifs », type calcul, 200 USD, échéance 2026-10-26 ;
  `registres/go.md` sur `main`, `02ae701e06841d6a01323ae8d8c20e4488009847`), **étendu au pilote par les décisions de
  Lazar de 23:52, 00:55 et 00:59** : avant le lancement, **deux écritures et une vérification** — session-depot inscrit
  l'extension dans `registres/go.md` (une ligne qui commence par `| GO-2026-10-24-07 |` et porte, **sur cette même
  ligne**, le type calcul et le nom `pilote-gemini-organisme-v4-question-v1`), consigne le lancement dans
  `registres/depenses.md` (une ligne qui nomme `pilote-gemini-organisme-v4-question-v1` et `GO-2026-10-24-07` ; 40 USD
  au pire cas, imputé à GO-2026-10-24-07 seul), et vérifie que le **reste disponible sur la ligne est ≥ 40 USD** (après ce qui y est
  déjà imputé : appels de contrôle, collisionneur, lot 3 au-delà de GO-06, sonde d'hôte) ; sans elles, le pilote ne part
  pas (vérification du lanceur, consignée dans `LANCEMENT.md` ; ce n'est pas une garde du noyau).

## Hypothèse

Aucune (pilote descriptif). Ce qui est rapporté : (1) mécanique — statut d'exécution de chaque génération (`OK`,
`EXCEPTION`, `DELAI_DEPASSE`, `SANS_STATUT`, `STATUT_ILLISIBLE`, `ISOLATION_INDISPONIBLE`, `INVALIDE_MODELE`,
`ANOMALIE_NOYAU`, `CREDIT_EPUISE`), appels par espèce et par rôle, statuts des appels (`OK`, `TRONQUE`, `VIDE`, `REFUS`,
`ANOMALIE`, `ECHEC_API`, `PLAFOND`, `ARRET_NOYAU`, `MODELE_NON_CONFORME` ; `TRONQUE` est attendu comme mode d'échec le plus
probable : réponse JSON en fin de texte et 640 jetons), coût réel contre plafond, durées, castes planifiées (tâches et
question), taille de `memoire_isvd.json`, relance éventuelle, empreinte de l'archive de l'organisme
(`empreinte_organisme`, archive tar, consignée par le noyau) à g0 et g1 — l'identité du code de g1 avec celui de g0 est
vérifiée après le moment du plan § 3, par `boucle.empreinte_arbre` des fichiers de code extraits des deux archives (sans
`memoire_isvd.json` ni `etat_generation_precedente.json`) ; en cas de relance, g1 tourne l'organisme de g0 —, éléments
écartés par le dépôt, nombre total de réponses valides (`n_reponses_test`, lisible dès la fin ; leur part par famille
reste avec les scores) ; (2) la **réponse à la question ouverte** : si elle a été lue (`reponse` vrai ou faux, raison),
ses octets et son empreinte, le texte **tel quel** et sa structure mécanique (sections présentes, bloc ORGANISATION :
appels, castes, votes et confiances déclarés par l'organisme) ; (3) scores — exactitude équilibrée par famille sur `test`
et sur `test_final`, aux générations 0 et 1, dans une table où figurent aussi les références de surface ; calibration
(Brier borné, erreur de calibration) ; part de tâches sans réponse valide par famille. **Aucune différence n'est
calculée ni nommée** (ni g1 − g0, ni score − référence) ; **la réponse à la question n'est ni notée ni jugée** : c'est du
matériau pour le dessin du noyau, rapporté avec sa provenance.

## Prédiction chiffrée et signe attendu

Aucune prédiction ; aucun signe attendu. Rien n'est écrit sur ce que « devrait » donner cet organisme, ni sur ce que sa
réponse « devrait » dire.

## Métrique

Exactitude équilibrée par famille ((sensibilité + spécificité) / 2), juge du noyau (`taches.evaluer`), une tâche sans
réponse valide comptée comme une erreur ; calibration par `taches.calibration` (10 classes ; sans réponse : q = 1, faux).
Scores de `test` rendus à l'organisme dans `historique` ; score de `test_final` jamais rendu, **calculé par le noyau en fin
de génération** (`juge/score-final.json`), lu par personne avant le moment fixé au plan § 3. La question ouverte n'a
aucune métrique : la primitive ne produit aucun score (le score est calculé avant la lecture de la réponse ; essai :
courbes et scores finaux identiques avec et sans question,
`test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`).

## Seuil

Aucun seuil de lecture (descriptif). Seuils de **garde** : plafond 40 USD pour la course, 20 par génération ; 1 800 s par
génération ; un appel `MODELE_NON_CONFORME` invalide la génération et arrête la lignée ; un HTTP 402 (`CREDIT_EPUISE`)
invalide la génération et arrête la course ; un journal d'appels absent après des appels (`ANOMALIE_NOYAU`) invalide la
génération (mêmes gardes que les préenregistrements principaux).

## Plan d'analyse

1. **Une seule course** (R3). Une course **part dès que son manifeste est écrit** ; après, jamais de seconde course,
   quelle que soit l'issue. Avant (tout refus ou toute exception avant le manifeste : codes 1 à 7 de la commande ; aucun
   manifeste, aucun appel, aucun score), un refus consigné peut être suivi d'une nouvelle tentative de la même commande,
   dans un nouveau dossier (`…-tentative2`, R12), après correction de l'environnement, jamais de ce texte ; le noyau a pu
   créer des dossiers vides (`course/`, son espace) : le script vérifie qu'ils ne contiennent aucun fichier ordinaire et
   que la sortie standard est vide, et les laisse tels quels (ils ne bloquent pas la tentative suivante) ; sinon il les
   ferme dans `refus-avant-manifeste-v1.tar.gz`, jamais lu, réserve consignée. En mode réel, le script refuse toute
   variable d'essai (`PILOTE_RACINE`, `SUFFIXE_ESSAI`, `REGISTRE_GO_SOURCE`, `DEPENSES_SOURCE`, `ESSAI_*`), et refuse de
   partir si une autre course du noyau tourne dans le conteneur (détection, aucun arrêt) ; il consigne le dossier du pilote
   et la source des registres (`origin/main`). Dossier du pilote :
   `PILOTE` = chemin absolu de `essaim-m3-refonte-v1/pilotes/pilote-gemini-organisme-v4-question-v1/` dans la copie du
   dépôt du lanceur (nouveau, vide au départ). Étapes, toutes faites par le script, chacune consignée dans
   `$PILOTE/LANCEMENT.md` : (i) code identique à `cec6dce` (commit et arbre de travail), `4967734a…` ancêtre ; banque et
   mission par `sha256sum` ; (ii) préenregistrement scellé (empreinte donnée, compagnon conforme, graine écrite dedans,
   aucun marqueur) ; (iii) `$PILOTE/outils/gemini-organisme-v4/organisme/` = `git archive b64bb3e…
   outils/gemini-organisme-v4/organisme` (`boucle.empreinte_arbre` = `c5ada335…`, 16 fichiers) ; `$PILOTE/question.md` =
   `git show 00399520…:brouillons/canal-reprise-releve-v1/envois/question-reecriture-vs-apprentissage-organismes-v1.md`
   (`d967b212…`) ; (iv) `$PILOTE/registre-go.md` = `registres/go.md` de `origin/main` après l'inscription de l'extension ;
   dépense consignée dans `origin/main:registres/depenses.md` ; reste déclaré ≥ 40 USD ; (v) résultat de l'appel de
   contrôle par espèce joint (statut `OK` exigé et vérifié par l'outil de session-depot ; le script vérifie que la pièce
   existe et n'est pas vide) ; (vi) **essais en root**, dans ce conteneur,
   depuis `essaim-m3-refonte-v1/` : `PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider --junitxml
   $PILOTE/essais-v1.xml` (désélections éventuelles nommées dans `PYTEST_ARGS`, consignées) ; exigés : aucun échec,
   aucun saut sauf `test_sources_reelles_de_moisson_si_reseau` (réseau), passés + sautés + désélectionnés = 114, et chacun
   des essais cités dans la liste d'arrêt passé ici ; (vii) depuis `essaim-m3-refonte-v1/`, `find essaim_m3 tests -name
   __pycache__ -prune -exec rm -rf {} +`, puis `boucle.empreinte_arbre(essaim_m3/noyau)` sous `python -B` =
   `68494279…` ; (viii) en root, `PYTHONDONTWRITEBYTECODE=1`, clés exportées, `ANTHROPIC_BASE_URL` retirée de
   l'environnement du run, depuis `essaim-m3-refonte-v1/` :
   `python -m essaim_m3 lancer --reel --go GO-2026-10-24-07 --registre-go "$PILOTE/registre-go.md" --taches
   banque/banque-confrontation-v1.json --mission MISSION-v1.md --sortie "$PILOTE/course" --generations 2 --graine
   10826196869519811464 --especes --appels-max 160 --usd-par-generation 20 --temps-max 1800 --max-tokens-appel 4096
   --recherches-max 0 --telechargements-max 0 --entrainements-max 0 --rondes-conception-max 0 --parallele-max 8
   --relances-max 1 --isoler-reseau --plafond-total 40 --decalage-uid 0 --question-ouverte "$PILOTE/question.md"
   --question-ouverte-aux g001 --organisme-impose "gemini-organisme-v4=$PILOTE/outils/gemini-organisme-v4/organisme@gemini"
   > "$PILOTE/ferme/sortie-standard-lanceur.txt" 2> "$PILOTE/sortie-erreur-lanceur.txt"`
   (`--especes` vide : aucune lignée auto-écrite — `cli._imposes_et_especes`, `Noyau(especes_amorcage=[])` ; essai en ligne
   de commande dans `test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score` ; les trois
   espèces restent servies à l'organisme imposé). `LANCEMENT.md` consigne aussi : tête de la copie, hôte, PID, `date -u`
   de départ et de fin, code de retour. Un fichier `STOP` dans `$PILOTE/course/` n'est posé que pour un incident
   technique (panne, coût anormal lu dans le journal des appels), consigné ; jamais au vu d'un score.
2. **Graine (R9)** : entropie E = 68205334246963107241479293944300770716 tirée au scellement par `secrets.randbits(128)` ; graine de course =
   `int(numpy.random.SeedSequence(E).generate_state(1, dtype=numpy.uint64)[0])` = 10826196869519811464 ; le manifeste de run
   consigne cette graine (`entropie_seed_sequence`), la version de numpy, `sha256_code_noyau` et `commit` (la tête de la
   copie du lanceur) ; E n'est consignée qu'ici.
3. **Moment de la lecture des scores (R1)** — ce qui est exécutable, fichier par fichier. Les fichiers du noyau mêlent
   statuts et scores (`resume.json`, `index.jsonl`, `evenements.jsonl`, `rapport-v1.json`), et `cli.lancer` imprime les
   scores `test` et `test_final` sur la **sortie standard** en fin de course (`cli.py`, `print` de `courbes` et
   `scores_finaux`). Donc : la **sortie standard** va dans `$PILOTE/ferme/` (fermé, jamais lu, jamais poussé en clair) ;
   la **sortie d'erreur** va dans `$PILOTE/sortie-erreur-lanceur.txt`, **lisible** : le noyau n'y écrit que des refus et des messages
   d'avant le manifeste (`refus : …`, « mode réel non demandé », « espèce inconnue ») et, en cas d'exception, la trace
   Python (lignes de code et message de l'exception : coûts, chemins, jamais un score) ; vérifié par recherche de tous les
   `print` vers la sortie d'erreur dans tout `essaim_m3/noyau/`, `essaim_m3/__main__.py` et l'outil d'extraction au commit
   cité, et dans le collisionneur (`collisionneur_v2.py`, qui n'y écrit que dans sa propre commande, jamais appelée par le
   noyau) ; ni `logging` ni `warnings` dans ces fichiers. **Pendant la course**, le lanceur ne consulte que le journal des appels
   de la génération en cours, par son chemin exact,
   `<espace>/travail/gemini-organisme-v4/gNNN.noyau/journal-appels.jsonl` (statuts, espèces, coûts par appel, cumul ;
   aucun score), où `<espace>` est la racine de la course ou `/var/tmp/essaim-m3/<16 premiers caractères de
   sha256(chemin absolu de la course)>` (`bac_a_sable.espace_organismes` ; consigné au manifeste, `espace_organismes`) ;
   ni la liste de ce dossier ni `gNNN.noyau/appels/` (textes bruts des réponses aux tâches). **Dès la fin**, sont lisibles
   et seulement eux : (a) `$PILOTE/extrait-mecanique-v1.json`, produit par `python -m essaim_m3.outils.extrait_mecanique
   --course "$PILOTE/course" --sortie "$PILOTE/extrait-mecanique-v1.json"` (listes closes de champs pour les résumés,
   l'exécution, le journal de l'organisme et le rapport ; filtre par motifs de noms de clés pour le manifeste et les
   événements, sûr au commit cité ; garde finale sur les noms de clés ; essai sain et artefacts) ; (b) la réponse,
   `course/archive/gemini-organisme-v4/g001/reponse-question.md`, recopiée par commande en
   `$PILOTE/reponse-question-g001.md`, avec un vrai compagnon de la copie (`.sha256`) et le compagnon d'origine gardé en
   `.sha256-archive` ; (c) les journaux d'appels archivés, `course/archive/gemini-organisme-v4/gNNN/journal-appels.jsonl`,
   recopiés par commande en `$PILOTE/journal-appels-gNNN.jsonl`, compagnons de même forme (un journal absent ou non
   ordinaire est consigné) ; (d) `$PILOTE/sortie-erreur-lanceur.txt`, `$PILOTE/LANCEMENT.md`, `$PILOTE/essais-v1.*` ;
   (e) les entrées poussées en clair : `question.md`, `registre-go.md`, le résultat de l'appel de contrôle,
   `outils/gemini-organisme-v4/organisme/`, `.gitignore`, `A-POUSSER-v1.txt` et les fichiers d'empreintes.
   **Canal latéral dit et accepté** : l'extrait liste les fichiers de travail avec leur taille ; la taille de
   `contexte.json` de g001 dépend de la longueur d'écriture du score `test` de g0 dans `historique` (quelques bits sur ce
   score) ; **personne ne la calcule ni ne la met en rapport avec quoi que ce soit** avant le moment ci-dessous. **Ce que la réponse (b) peut contenir** : jamais une vérité de `test` ni
   de `test_final`, ni un score du juge — l'organisme ne reçoit pas ces vérités ; il reçoit à g1 le score `test` de g0
   (dans `historique`, sa vue `g000/resume.json` et `contexte.json`), mais le code de la v4 ne passe `historique` qu'à
   `planifier_castes_question_ouverte`, qui n'en tire que la pression d'exploration (nombre de castes), et ni les
   consignes des castes ni le fichier écrit n'en contiennent rien (`principal.py`, `_traiter_question_ouverte` ;
   `mitose_spectrale.py`, `planifier_castes_question_ouverte`). **Exposition dite et acceptée** : le « résumé transmis aux
   castes » (bloc ORGANISATION) et le corps des contributions peuvent citer jusqu'à 4 exemplaires de la mémoire
   spectrale (≤ 220 caractères chacun), qui peuvent être une **vérité d'entraînement** (trace de vérification
   `[famille] verite=…`) ou le début du raisonnement de g0 sur une tâche de `test` ou de `test_final`, avec l'étiquette
   choisie ; **personne ne les confronte aux vérités de la banque** avant le moment ci-dessous. **Jusqu'au scellement de
   la v4 de l'étape 1**, et jusqu'à ce qu'il soit inscrit que la v8 de la confrontation ne change ni la table de lecture
   de H-E1, ni les seuils, ni les règles de lecture de la v7 (`74487a41fe29b4ad0e5688df9fb9fda815725cdd7521ee2a327694b2fa4ddf61`),
   **personne ne lit**, notamment : la sortie standard, `rapport-v1.json`, `evenements.jsonl`, `archive/index.jsonl`, les
   `resume.json`, les `juge/`, `banque.json`, `lignees/`, `archive/*/gNNN/organisme.tar.gz` (qui porte
   `etat_generation_precedente.json`, avec l'étiquette donnée à chaque tâche de test), `archive/*/gNNN/travail/` (dont
   `noyau/appels/`), et dans `<espace>` :
   `archive_vue/`, `travail/*/gNNN/` (réponses de l'organisme, `contexte.json`, `journal_generation.json`) et
   `gNNN.noyau/appels/`. **Fermeture mécanique** : le script fait de `course/`, `ferme/` (sortie standard) et `<espace>`
   une seule archive `$PILOTE/ferme.tar.gz` (+ `.sha256`), **sans l'ouvrir** ; il vérifie que le nombre d'entrées de
   l'archive égale celui des fichiers et dossiers sur disque (hors sockets), puis **retire les copies ouvertes** ; si la
   vérification échoue, les copies restent dans le conteneur, jamais lues ni poussées, et c'est une réserve consignée.
   **Poussé en clair**, et seulement : les fichiers de `$PILOTE/A-POUSSER-v1.txt`, liste **fermée par noms** écrite par le
   script (`.gitignore`, `LANCEMENT.md` et compagnon, `sortie-erreur-lanceur.txt` et compagnon, `essais-v1.xml`,
   `essais-v1.txt`, `extrait-mecanique-v1.json` et compagnon, `reponse-question-g001.md` et ses compagnons,
   `journal-appels-gNNN.jsonl` et leurs compagnons, `question.md`, `registre-go.md`, le résultat de l'appel de contrôle,
   `outils/gemini-organisme-v4/organisme/`, `ferme.tar.gz` ou `refus-avant-manifeste-v1.tar.gz` et compagnon,
   `A-POUSSER-v1.txt` et compagnon, `EMPREINTES-pilote-v1.txt` et compagnon ; tout autre fichier du dossier est consigné
   et n'est pas poussé), sur une branche `pilotes/gemini-organisme-v4-question-v1`, jamais `main` ; `course/` et `ferme/`
   ne sont jamais ajoutés au dépôt (`$PILOTE/.gitignore`, écrit avant la course). Tout changement des règles de lecture de la v7
   rouvrirait R1 pour ce pilote (nouvelle version de ce texte avant toute lecture). Déclaration : aucun score de ce
   pilote ne motive aucun changement des préenregistrements principaux ; leur scellement citera les empreintes de
   `ferme.tar.gz` et de `EMPREINTES-pilote-v1.txt` pour le montrer.
4. **Lecture** : après le moment du point 3, ouverture de `ferme.tar.gz` : `rapport-v1.json`, `evenements.jsonl`,
   `resume.json` des deux générations, `juge/` ; tableau rapporté : famille × génération × {score `test`, score
   `test_final`, référence de surface, Brier, part sans réponse}, plus appels par espèce, par rôle et par statut, coûts,
   durées, castes, taille de mémoire, empreintes des archives et identité du code de g1, relance, éléments écartés ; la
   réponse à la question, telle quelle, avec sa structure mécanique. Rédigé par conv-audit, relu par session-depot ; aucune
   lecture de verdict (R13 sans objet : ce n'est pas une porte).
5. **Ce que ce pilote ne dit pas** (écrit d'avance) : rien sur H-E1, H-G1 ni sur les organismes auto-écrits ; rien sur
   « l'intelligence » de la conception de Gemini (un organisme, une graine, deux générations, deux familles, une seule
   espèce appelée pour les tâches) ; ses scores sont des points, pas des estimations ; ils n'entrent dans aucun critère
   des préenregistrements principaux ; la réponse à la question est l'avis d'un essaim d'une conception, à une graine,
   dans ≈ 37 appels restants, sans moisson : un matériau parmi d'autres (réponses du collisionneur, des organismes
   auto-écrits à venir, d'une v5 de Gemini avec moissonneur), jamais une consigne au noyau ni aux organismes.

## Critères de lecture gelés

1. Score d'une famille > 0,95 ou < 0,30 sur `test` ou sur `test_final`, à l'une des générations ; ou part de tâches sans
   réponse de 100 % pour une famille ; ou plus de 20 % d'appels hors `OK` à une génération ; ou une génération en statut
   autre que `OK` → **audit de symétrie (R4)** avant tout rapport, **sans relance** (fuite, étiquettes, indice de
   surface, panne, troncature, isolation), par un **sous-agent neuf** lancé par conv-audit, qui n'a ni écrit ce texte ni
   lu les scores avant l'audit ; rapport scellé dans `prereg/contre-lectures/`. Les déclencheurs mécaniques (statuts,
   part d'appels hors `OK`) se lisent dès la fin dans l'extrait ; un audit qui doit lire un fichier fermé (point 3) se
   fait **après** le moment du point 3 ; d'ici là, son matériau se limite aux fichiers lisibles (a)–(d).
2. Question : (i) g1 n'a pas tourné (lignée arrêtée à g0 : `INVALIDE_MODELE`, `ANOMALIE_NOYAU`, `CREDIT_EPUISE` ; course
   arrêtée : `STOP`, plafond) → « question non posée : g1 n'a pas tourné », avec la raison lue dans l'extrait ;
   (ii) `reponse` faux avec `probleme` autre que « absent » (lien, taille, fichier non ordinaire) → rapporté comme refus du
   noyau, avec la raison ; (iii) `reponse` faux et « absent » → « l'organisme n'a pas écrit de réponse », rapporté ;
   (iv) réponse lue d'une génération g1 invalidée → texte rapporté tel quel, avec la mention « réponse d'une génération
   invalidée (statut …) » ; (v) réponse lue → texte rapporté tel quel, y compris quand c'est le texte d'abstention ou le
   texte minimal de l'organisme (délibération coupée ou vide).
3. Sinon → **rapporté tel quel** : le tableau, les statuts, les coûts, la réponse, et la phrase « pilote descriptif, un
   organisme, une graine, deux générations, une espèce appelée pour les tâches, une question posée une fois ».
Lectures interdites — dans la prose du rapport (la citation de la question et de la réponse n'est pas visée) : tout verbe
de comparaison (« bat », « dépasse », « reste sous », « fait mieux / moins bien ») entre un score et une référence, un
autre score ou 0,5 ; tout adjectif sur un score ; toute différence calculée (g1 − g0, score − référence) ; toute
extrapolation aux organismes auto-écrits ou à Gemini ; toute mention de « apprentissage » ou de « mémoire qui marche » à
propos des scores ou de la mémoire de cet organisme ; tout jugement de la réponse à la question (« bonne », « profonde »,
« fausse », « meilleure que le collisionneur ») ; **toute mise en rapport de la réponse avec les scores**. Les nombres et
les références que contient la réponse (confiances, capacité spectrale, références « à vérifier ») sont rapportés comme
**dires de l'essaim, non vérifiés** (R7) ; une référence n'entre dans aucun texte avant vérification sur PDF empreinté,
page citée.

## Liste d'arrêt

| condition | effet | garde ou vérification |
|---|---|---|
| une course déjà partie (manifeste écrit) dans un dossier du pilote, quelle que soit la tentative ; dossier de la tentative existant | le pilote ne part pas (R3, R12) | script de lancement, consigné |
| code différent de celui de `cec6dce3…` (commit ou arbre de travail), fichier non suivi dans `essaim_m3/` ou `tests/`, `4967734a…` non ancêtre, empreinte du noyau nettoyé ≠ `68494279…`, banque ≠ `f1387a20…`, mission ≠ `bd2c6a15…` | le pilote ne part pas | script (`git diff --quiet`, `git status --porcelain`, `git merge-base --is-ancestor`, `python -B` + `boucle.empreinte_arbre`, `sha256sum`), consigné ; le `sha256_code_noyau` du manifeste est rapporté de l'extrait (égal attendu) |
| préenregistrement d'empreinte autre, compagnon absent, graine non écrite, marqueur restant | le pilote ne part pas | script, consigné |
| `boucle.empreinte_arbre($PILOTE/outils/gemini-organisme-v4/organisme) ≠ c5ada335…`, `sha256($PILOTE/question.md) ≠ d967b212…`, ou 16 fichiers non retrouvés | le pilote ne part pas | script, consigné ; le manifeste reconsigne l'empreinte d'arbre et l'empreinte de la question |
| GO-2026-10-24-07 non étendu au pilote dans `registres/go.md`, lancement non consigné dans `registres/depenses.md`, reste sur la ligne < 40 USD | le pilote ne part pas | vérification du lanceur (le script lit les deux registres d'`origin/main` et le reste déclaré), consignée |
| un échec d'essai, un saut autre que celui de l'essai réseau, un total ≠ 114, un essai cité ci-dessous non passé dans ce conteneur | le pilote ne part pas | script (rapport JUnit), consigné |
| GO absent ou d'un autre type, registre absent, collisionneur d'empreinte inattendue, `ANTHROPIC_BASE_URL` définie, isolation réseau indisponible, noyau non root, clés absentes | refus de lancer (avant le manifeste : tentative suivante permise) | gardes du noyau : `boucle.Noyau.__init__` (GO, collisionneur, registre, root, `--isoler-reseau`, `unshare -n`), `cli.lancer` (clés, `ANTHROPIC_BASE_URL`, root) ; essais discriminants `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url`, `test_bac_a_sable_isolation_reseau_refusee_si_indisponible` ; clés absentes et non root : refusés d'abord par le script (essayés) et par `cli.lancer` (codes 4, 5) ; collisionneur inattendu et isolation : sans essai discriminant au commit cité, vérifiés après départ par `manifeste.collisionneur_conforme` et `manifeste.isolation` de l'extrait, consignés |
| `--question-ouverte` sans `--question-ouverte-aux`, question absente, cible mal formée ; question vide | refus avant tout lancement | `cli._question_ouverte`, essai `test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score` ; question vide : `test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts` |
| appel de contrôle d'une espèce en échec (crédit, clé, en-tête, modèle servi) | la course ne part pas | outil de session-depot (essais sain et artefact) ; le script exige sa pièce présente et non vide (essayé) |
| variable d'essai définie en mode réel ; autre course du noyau en cours dans le conteneur | le pilote ne part pas (il attend) | script (essayés) |
| plafond de 40 USD (course) ou de 20 USD (génération) | `PLAFOND` rendu, génération rapportée, course arrêtée au plafond total | `test_appels_paralleles_plafond_tenu_au_pire_cas`, `test_organisme_gourmand_recoit_plafond_sans_exception` ; arrêt au plafond total : `boucle.Noyau._doit_arreter`, `test_ce312_doit_arreter_et_raison_juste` |
| 1 800 s par génération | génération arrêtée (`DELAI_DEPASSE`), statut rapporté ; garde interne de l'organisme : aucun nouvel appel après 75 % du temps, consigné dans son journal | `test_bac_a_sable_exception_et_delai` ; `principal.py` (`PART_TEMPS_APPELS`) |
| modèle servi non conforme | génération `INVALIDE_MODELE`, lignée arrêtée | `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee` |
| crédit d'un fournisseur épuisé (HTTP 402) | génération `CREDIT_EPUISE` invalidée, course arrêtée, aucune relance | `test_ce305_credit_epuise_arrete_la_course` |
| journal des appels absent après des appels | génération `ANOMALIE_NOYAU` invalidée | détection : `test_ce307_anomalie_journal_absent` ; invalidation : code de `boucle.executer_generation` |
| successeur invalide à g0 | g1 = relance de g0, consignée ; invalide à g1 : course finie | `test_relance_puis_reprise_remet_le_compteur_a_zero` |
| liens, tubes ou fichiers spéciaux posés par l'organisme (dont sous le nom `reponse-question.md`) | écartés et consignés ; lectures sans lien, bornées — sauf `statut_execution.json` et `erreurs.txt`, lus par `bac_a_sable.executer` sans garde de lien (signalé à session-depot ; le code de la v4 n'en pose pas) ; réponse refusée consignée | essais du correctif (en-tête), `test_question_ouverte_posee_…` (artefact du lien) |
| fichier `STOP` (incident technique seulement) | arrêt à la fin de la génération, consigné | `test_fichier_stop_arrete_la_boucle` |
| lecture hors des sorties par l'organisme, écriture dans la vue, processus détaché | refus par le système | `test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus` (exécuté en root, exigé passé) |
| archive fermée incomplète (code de `tar` non nul, ou nombre d'entrées ≠ disque) | copies ouvertes gardées, jamais lues ni poussées ; réserve consignée | script |
| arrêt humain du processus | par PID consigné dans `LANCEMENT.md` (R10) | lanceur |

Essais cités (chacun exigé passé dans le conteneur du lancement) : `test_fichiers_lecture_et_copie_sans_lien`,
`test_depot_ne_suit_aucun_lien_de_l_organisme`, `test_organisme_poseur_de_liens_ne_voit_rien_du_noyau`,
`test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts`,
`test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score`,
`test_extrait_mecanique_sain_puis_artefacts`, `test_mode_reel_refuse_sans_go`, `test_mode_reel_refuse_anthropic_base_url`,
`test_bac_a_sable_isolation_reseau_refusee_si_indisponible`, `test_appels_paralleles_plafond_tenu_au_pire_cas`,
`test_organisme_gourmand_recoit_plafond_sans_exception`, `test_ce312_doit_arreter_et_raison_juste`,
`test_bac_a_sable_exception_et_delai`, `test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee`,
`test_ce305_credit_epuise_arrete_la_course`, `test_ce307_anomalie_journal_absent`,
`test_relance_puis_reprise_remet_le_compteur_a_zero`, `test_fichier_stop_arrete_la_boucle`,
`test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus`. Le script de lancement v3 a été essayé en simulation (pièces
`prereg/pieces-pilote-gemini-v4/simulation-lanceur-v3/` : `LANCEMENT-simulation-v1.md`,
`415e1f85a1e312994841d8a66ae833401ffc1bc26066509e8851abdc0569adfa`, cas sain avec désélection de l'essai réseau —
113 passés, 1 désélectionné, 19 essais cités passés —, deux générations, réponse archivée, archive fermée de 1 429
entrées égale au disque, copies retirées ; `extrait-mecanique-simulation-v1.json`,
`9ab3011c5a675d38e4577025b6b78e361086198309a81bba462a932846750c08` ; `reponse-question-g001-simulation-v1.md`,
`e2dad0abbbff2f3683d2b9c08510b246f82f6eb52fc679c980496ff23a75aa34` ; `A-POUSSER-simulation-v1.txt`,
`9f53a76f42c9ff181fc9b4242179966353b1180e6f8bd8d8aad755e14f7fcc72`) et sur 34 artefacts, chacun refusé ou traité avec sa
raison (`essais-lanceur-v3-v1.log`, `e9edfa7794e15ef81f405e615f21b86f66c19098979bedfae13ab9b7c30fbc2e` ; le programme
d'essai : `essais_lanceur_v3.sh`, `6f4a162a1ef9380c37ca4c6c49796b35d47cc18eb8dc2089059b4044f7228403`) : variable d'essai
en mode réel ; clés absentes ; mode réel hors root ; autre course en cours ; course déjà partie ; dossier existant ;
commit absent ; code de tête différent (la tête de session-depot) ; arbre de travail modifié ; fichier non suivi ;
banque ; mission ; préenregistrement d'autre empreinte, sans compagnon, sans la graine, avec un marqueur ; organisme
altéré ; fichier de l'organisme manquant ; question altérée ; ligne du GO sans « calcul » ; « calcul » et nom sur deux
lignes ; dépense non consignée ; reste < 40 USD ; appel de contrôle vide ; essai en échec, saut non permis d'un essai cité
et total ≠ 114 (rapport JUnit modifié) ; bytecode réintroduit ; refus du noyau après création de `course/` (famille
inconnue : rien de fermé, dossiers vides laissés), puis tentative 2 acceptée, puis tentative 3 refusée ; archive fermée
incomplète (copies gardées, rien de `course/` poussé) ; espace hors de `/var/tmp/essaim-m3` (réserve consignée) ; fichier
imprévu (consigné, non poussé). Gardes du script restées sans artefact : l'ancêtre `4967734a…` (aucun commit utile ne
l'omet) ; le cas d'un refus avant le manifeste qui laisserait des fichiers ordinaires (aucune voie connue du noyau n'en
écrit avant le manifeste) ; la sortie de `tar` en erreur (simulée seulement par l'archive incomplète).

## Traitement des constats de la contre-lecture 3 (PG3-01 à PG3-16)

| constat | traitement dans ce texte |
|---|---|
| PG3-01 (majeur) sortie du lanceur avec les scores, hors de l'enveloppe, poussée en clair | sorties séparées : sortie standard dans `ferme/`, archivée fermée avec `course/` et `<espace>`, copies retirées après vérification ; sortie d'erreur lisible (aucun score : `print` du noyau vérifiés) ; liste close de ce qui est poussé ; `course/` et `ferme/` jamais ajoutés (plan § 3) |
| PG3-02 `<espace>` et copies du conteneur ; chemin du journal (c) | emplacements interdits nommés (`archive_vue/`, `travail/*/gNNN/`, `gNNN.noyau/appels/`, `archive/*/gNNN/travail/`, `banque.json`) ; journal lu par son chemin exact seulement ; journaux archivés recopiés par commande et lus en copie ; `<espace>` archivé fermé puis retiré (plan § 3) |
| PG3-03 exposition de la réponse | énoncé exact : jamais une vérité de `test` ou de `test_final` ni un score ; des vérités d'entraînement et des débuts de raisonnement sur `test` ou `test_final` peuvent y figurer ; l'argument complet (score `test` reçu à g1, écarté par le code de la v4) |
| PG3-04 1 800 s ; « attendu 5 » | « pour réduire le risque » ; coupure et troncature dites d'avance, texte d'abstention ou minimal rapporté tel quel (critère 2 (v)) ; « 5 castes planifiées », contributions possiblement moindres |
| PG3-05 cas de la question ; moment de l'audit | critère 2 (i) g1 non tournée, (iv) g1 invalidée ; critère 1 : audit sur fichiers fermés après le moment du § 3, sinon matériau (a)–(d) |
| PG3-06 lectures interdites et réponse | interdits bornés à la prose du rapport (citation non visée) ; nombres et références de la réponse rapportés comme dires non vérifiés (R7) ; mise en rapport de la réponse avec les scores interdite |
| PG3-07 refus avant tout appel | « une course part dès que son manifeste est écrit » ; tentative suivante permise avant, dans un nouveau dossier ; jamais après (plan § 1, liste d'arrêt, script) |
| PG3-08 simulation citée d'une pièce contraire | simulation du script avec la question réelle `d967b212…`, sous un code identique à `cec6dce`, pièces et empreintes citées ; textes de simulation dits sans valeur |
| PG3-09 banque, mission, arbre de travail | `sha256sum` de la banque et de la mission, `git diff --quiet cec6dce -- …`, `git status --porcelain` ; ligne d'arrêt ; `sha256_banque` du manifeste dit « vidage JSON trié » |
| PG3-10 essais sautés | essais en root ; aucun saut sauf l'essai réseau ; total 114 ; essais cités exigés passés ; ligne d'arrêt |
| PG3-11 « listes closes » | « listes closes pour résumés, exécution, journal de l'organisme et rapport ; filtre par motifs pour le manifeste et les événements, sûr au commit cité » |
| PG3-12 corps de la question | « identique sauf la phrase d'introduction des points, tournée sans « Je veux » » |
| PG3-13 `EXCEPTION` | ajouté aux statuts d'exécution |
| PG3-14 verdict sans marqueur ; marqueurs comme noms | contre-lecture 3 inscrite entière (verdict, empreintes, traitement ci-dessus) ; toute correction de plus = nouvelle version ; champs du scellement nommés sans doubles chevrons |
| PG3-15 portée des essais | `test_ce307…` : détection seule, invalidation par le code ; question vide : essai du module ; `--especes` vide : essai en ligne de commande ; gardes sans essai discriminant : vérification après départ par l'extrait |
| PG3-16 précisions | `b4c3774…` et `3e6fe2e9…` en entier avec chemin ; convention du collisionneur ; répertoire de `find` dit ; `commit` du manifeste = tête de la copie ; `--decalage-uid 0` sans alternative ; « dossier du pilote » ; « deux écritures et une vérification » ; `LANCEMENT.md` avec compagnon ; empreinte de l'archive tar, identité du code de g1 vérifiée après le moment ; `n_reponses_test` lisible dès la fin |
| observation hors préenregistrement (`statut_execution.json`, `erreurs.txt` lus sans garde de lien) | dite dans la liste d'arrêt ; transmise à session-depot |

## Traitement des constats de la contre-lecture 4 (PG4-01 à PG4-08)

| constat | traitement dans ce texte et dans le script v3 |
|---|---|
| PG4-01 refus au code 7 → `ferme.tar.gz` → tentative suivante refusée | rien n'est fermé sans manifeste ; dossiers vides vérifiés sans fichier et laissés, sinon `refus-avant-manifeste-v1.tar.gz` ; essayé : refus du noyau après création de `course/` (famille inconnue), puis tentative 2 acceptée, puis tentative 3 refusée (plan § 1) |
| PG4-02 variables de simulation actives en réel | refusées en mode réel avant tout ; dossier du pilote et source des registres consignés ; motif de recherche des courses parties étendu à tout dossier `…-v1*` ; essayé |
| PG4-03 canal latéral par la taille de `contexte.json` | déclaré au plan § 3 (« personne ne la calcule ni ne la met en rapport ») ; outil inchangé (code cité) |
| PG4-04 gardes du script sans artefact ; désélection non montrée | artefacts ajoutés (liste au-dessus de cette table) ; cas sain avec désélection de l'essai réseau joint ; gardes restées sans artefact nommées |
| PG4-05 (i) appel de contrôle ; (ii) ligne du GO ; (iii) clé Gemini ; (iv) journal absent ; (v) ligne de `depenses.md` | (i) note du script : présence et non-vide seulement, statut par l'outil de session-depot ; (ii) type et nom exigés sur une même ligne (essayé : deux lignes séparées refusées) ; (iii) variable source consignée ; (iv) consigné ; (v) décrite au Devis |
| PG4-06 compagnons des copies ; `A-POUSSER-v1.txt` | vrais `.sha256` des copies, compagnons d'origine en `.sha256-archive` ; `A-POUSSER-v1.txt` avec compagnon et dans `EMPREINTES-pilote-v1.txt` |
| PG4-07 liste par exclusion ; `course/` dans l'arbre de travail | liste fermée par noms, fichiers imprévus consignés et non poussés ; `.gitignore` (`course/`, `ferme/`) écrit avant la course |
| PG4-08 (i) entrées en clair ; (ii) `lignees/`, `organisme.tar.gz` ; (iii) codes 1 à 7, messages de la sortie d'erreur ; (iv) clés et manifeste ; (v) autre course | (i) ajoutées en (e) ; (ii) nommées, « notamment » ; (iii) « tout refus ou toute exception avant le manifeste », messages nommés ; (iv) clés : script et `cli.lancer` ; manifeste : collisionneur et isolation ; (v) détection par le script, consignée |

## Traitement des constats des contre-lectures 1 et 2

Repris de la v1 (table « Traitement des constats de la contre-lecture 2 (PG2-01 à PG2-09) et des constats « traités en
partie » de la contre-lecture 1 », jugée par la contre-lecture 3 : 8 traités, PG2-01 en partie ; PG-06 et PG-12 en partie ;
aucun non traité). Les parts restantes sont traitées ici : PG2-01 et PG-06 par PG3-01 et PG3-02 ; PG-12 par PG3-08 et
PG3-16. Les autres lignes de cette table valent telles quelles.

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf (`claude-fable-5-1`, lancé par conv-audit, 24 octobre 2026, 21:54:52–22:06:48
  UTC) ; brouillon relu `prereg/pilote-gemini-organisme-v3-v1.md`,
  `3eaf72751c9055bfcbcb3151acde814d5e1bea5a2d029fa03cf9f06edd57fecf` ; rapport
  `prereg/contre-lectures/pilote-gemini-organisme-v3-v1-cl1.md`,
  `445a42489093cd84a02a86819d1039529417270565c4526d6134f201915a3807` ; verdict « scellable après corrections » (18
  constats PG-01 à PG-18).
- **Contre-lecture 2** — sous-agent neuf (`claude-fable-5-1`, lancé par conv-audit, 24 octobre 2026, 22:14:15–22:27:23
  UTC) ; brouillon relu `prereg/pilote-gemini-organisme-v3-v2.md`,
  `5b956645e87ad829fe6db5c14b99f2c3a3c4ccaefcd66252d0a07f4dbb5e65ae` ; rapport
  `prereg/contre-lectures/pilote-gemini-organisme-v3-v2-cl2.md`,
  `240788fca480a6d9e15c7693249d85fdadd4d8b87859d416f012c87fedb5f596` ; verdict « scellable après corrections (v3) » (9
  constats PG2-01 à PG2-09).
- **Contre-lecture 3** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 24 octobre 2026, 23:26:36–23:53:29
  UTC), qui n'a écrit aucune pièce ; brouillon relu `prereg/pilote-gemini-organisme-v4-question-v1.md`,
  `6ef156778a5f6315cdd201919585250fce33afd227ec0e95fff3d028b11ed038` ; rapport
  `prereg/contre-lectures/pilote-gemini-organisme-v4-question-v1-cl3.md`,
  `928463e0688bb89335c3fb63da8e53ed2f19a7800b0fcdfbd18a92585cd938d5` ; verdict « scellable après corrections » (16
  constats PG3-01 à PG3-16 ; traités ci-dessus).
- **Contre-lecture 4** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 25 octobre 2026, 00:10:57–00:29:37
  UTC), qui n'a écrit aucune pièce, a vérifié sur la v2 et sur le script v2 le traitement des 16 constats de la
  contre-lecture 3 ; brouillon relu `prereg/pilote-gemini-organisme-v4-question-v2.md`,
  `4b89795cd571c5246a2a0de7c2aaace3a3431784d3ffe6a7f48859efa1a800e5` ; rapport
  `prereg/contre-lectures/pilote-gemini-organisme-v4-question-v2-cl4.md`, `891a2fcb96f2efab8345f2af1c5aba76dcfa7a9bc719aa18c74840e84b18215a` ; verdict « scellable après
  corrections » (15 constats traités, PG3-07 en partie ; 8 constats nouveaux PG4-01 à PG4-08, 4 mineurs et 4 de forme ;
  traités ci-dessus). **Signalé (R2)** : les corrections de cette v3 n'ont pas été relues par un cinquième sous-agent ;
  elles sont essayées par le script en simulation (pièces `simulation-lanceur-v3/`). Champs remplis au scellement, et eux
  seuls : l'entropie et la graine (plan § 2 et § 1), l'empreinte du fichier d'empreintes des pièces : `prereg/pieces-pilote-gemini-v4/EMPREINTES-pilote-gemini-v4-question-v3.txt`, `145e58aa35abca681b4b2752e8717d3b473a3eb9ee316683c39d9a06dd4ee840`.
