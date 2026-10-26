# LISEZMOI — lanceur v12 des deux courses à question de la v6.2.1, batterie v14, séries v15, v16 et v17 — v1

Écrit par le sous-agent qui a dérivé le lanceur v11 et la batterie v13 (brief `lanceur-v11-v1/`), sur le brief de conv-audit du
26 octobre 2026 (message de coordination, trois précisions : un seul texte pour les deux courses ; les annexes en bloc de
paramètres ; la question « audit » v2 à `9417652a` avec une seule annexe à remplir ; puis deux décisions : la règle de la garde
« refus-question », le noyau attendu `9beee10b` à la borne de 100 000 caractères ; enfin les paramètres définitifs de la course
« audit », R-518 : question v3 et annexe réelle au commit `ad23e9ae` de `main` ; puis R-519 : la course « audit » ne part pas —
refus d'un modèle au collisionneur sur la partie 3 du rapport, condition de GO-04 non remplie — sa clé et ses paramètres restent
dans le lanceur et la batterie, inutilisés jusqu'à une décision de Lazar ; ce qui fait partir la course « maieutique » est
fini), le 26 octobre 2026 à 14:13 UTC (heure lue sur `date -u` dans la
commande qui a écrit ce fichier). Sources lues : le lanceur v11 (`21854b79…`), la batterie v13 (`7b0a9bb0…`), le texte
`prereg/courses-question-gemini-v6-2-v1.md` (brouillon de conv-audit, non scellé), `sceller_courses_question_v6.py`, le code du
noyau (`essaim_m3/noyau/appels.py`, `boucle.py`, `bac_a_sable.py`, `serveur.py`, `question.py` aux commits `8e5e2f7b` et
`9beee10b`, `archive.py`) et les conventions du collisionneur v2.5 (`collisionneur_v2.py`, `213b52ef…`, `statut_reponse` et
`REFUS_GEMINI`), le code de la v6.2.1 au commit `7ea32705…` (`mitose_spectrale.py`, `principal.py`, `CONCEPTION.md` : rôles des
castes), les questions aux commits `eb03bad5`, `9417652a` et `ad23e9ae` (v3 : 3 430 caractères) et l'annexe définitive
(`docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md` à `ad23e9ae` : empreinte et taille seulement, 37 563
octets, 36 024 caractères, contenu non lu ; les trois annexes initiales de même), le journal d'appels poussé de g001 de la course M du pilote 4 (branche `pilotes/pilote4-gemini-v6-2-v1`,
`pilote4-gemini-v6-2-v1-tentative2/journal-appels-g001.jsonl`, `fec0cb82…`, 129 appels : rôles, statuts et raisons d'arrêt
seulement, aucun score ni texte), les copies d'essai d'hier et `lancer-serie-v14.sh`. Ni clé lue, ni script de la relève exécuté,
ni poussée ; `python3 -I` partout ; `git` : `fetch` des commits des questions, de la branche `outils/pilote4-gemini-travail`
puis de `main` à `ad23e9ae` dans les deux copies d'essai, `checkout --detach 9beee10b` dans ces copies, `show`/`cat-file`/`log`/`grep`/`merge-base`/`archive`
en lecture ; commit des pièces finales sur la branche (permis par conv-audit après la série v16), aucune poussée.

## Réserve levée : la règle de la garde « refus-question »

Constat (brief initial) : la garde devait arrêter la course au premier appel refusé de l'un des cinq rôles des castes de la
question (`monoculture_analytique`, `monoculture_croisee`, `sonde_orthogonale_onsager`, `critique_adversariale_limites`,
`arbitre_synthese_contradictoire`). Or `monoculture_analytique` est aussi la caste qui résout les tâches de la banque
(`planifier_castes`, `mitose_spectrale.py`, indice 0 ; une caste par tâche sous les bornes du pilote 4), et rien dans le journal
ne distingue un appel de tâche d'un appel de question de même rôle. Dans le journal réel de g001 de la course M du pilote 4
(129 appels), 120 appels de tâche `monoculture_analytique` précèdent la question, cinq en REFUS (`organisme-0029`, `0046`, `0056`,
`0111`, `0121`) ; puis `organisme-0124` `moissonneur_formulation_requetes` (la moisson sur la question), puis les cinq castes de la
question (`0125` `monoculture_analytique`, `0126` `monoculture_croisee`, `0127` `sonde_orthogonale_onsager`, `0128`
`critique_adversariale_limites`, `0129` `arbitre_synthese_contradictoire`, en REFUS). La liste initiale aurait tué la course M à
`organisme-0029`, sur un refus de tâche.

Règle retenue par conv-audit (26 octobre 2026), appliquée par le lanceur v12 (étape 7 bis, paramètres `ROLES_QUESTION_PROPRES`,
`ROLE_TACHES_ET_QUESTION`, `PREFIXE_MOISSONNEUR`, `APPELS_TACHES_MAX`, une ligne chacun) : dans g001, un appel est « refusé » si
son statut est REFUS ou si `fin` porte une raison d'arrêt de sûreté (`FINS_SURETE`, liste close) ; (a) un appel refusé de l'un des
quatre rôles propres à la question (`monoculture_croisee`, `sonde_orthogonale_onsager`, `critique_adversariale_limites`,
`arbitre_synthese_contradictoire`) arrête toujours ; (b) un appel refusé de `monoculture_analytique` arrête seulement s'il vient
après le premier appel de rôle `moissonneur_*` de g001, ou s'il est au-delà du 120e appel de ce rôle en g001 (le 121e est une
caste de la question) ; sinon rien. La règle qui a joué est écrite au LANCEMENT.md (ligne « garde refus-question : règle « … » »)
et dans la pièce `garde-refus-question-v1.json` (`regle`, `rang_role_taches`, `premier_moissonneur`). Sur le journal réel de la
course M, la règle ne s'arrête qu'à `organisme-0129` (l'arbitre de la question, refusé) : la batterie le rejoue (motif réel,
suites « rôle statut fin » vérifiées par empreinte, `6d2ad200…` pour les 124 premiers appels, `7f79273d…` pour les 129).

## Fait

1. `deriver_lanceur_question_v12.py` : dérive `lancer_courses_question_v12.sh` (1047 lignes) de `lancer_pilote4_gemini_v11.sh`
   (938 lignes, `21854b79…`) par 41 remplacements exacts comptés (40 à 1 occurrence, `setsid env -i` à 2) et le retrait du bloc de
   la porte « course v6.2 précédente » (83 lignes, ancre vérifiée par son empreinte `2ff1cfec…`), puis 101 contrôles de présence
   ou d'absence comptés. Écart : `diff-lanceur-v11-vers-v12.txt` (`diff -u`, 653 lignes). `bash -n` : conforme. Changements :
   - bloc de paramètres en tête (après `refus_tot`) : `QUESTION_MAIEUTIQUE_COMMIT|CHEMIN|SHA` (`eb03bad5`, `1d29fbec…`),
     `QUESTION_AUDIT_COMMIT|CHEMIN|SHA` (**définitifs, R-518** : `ad23e9ae…`, `question-audit-controle-organismes-v3.md`,
     `998960b8…` ; la v1 `dd2c1016…` et la v2 `ec3abf28…` ne servent plus), quatre emplacements d'annexe
     `ANNEXE_k_COMMIT|CHEMIN|SHA` : l'annexe 1 remplie (`ad23e9ae…`,
     `docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md`, `c1237687…`), les emplacements 2 à 4 vides ; un
     emplacement vide n'est pas servi, un emplacement à moitié rempli est un refus ; les annexes servies sont numérotées dans
     l'ordre ; changer une question ou une annexe = trois lignes, l'empreinte du lanceur change ; puis le **noyau attendu** :
     `NOYAU_COMMIT=9beee10b…` (le code de la copie — essaim_m3, tests, collisionneur — doit lui être identique, lui-même ancêtre
     de HEAD, commits postérieurs limités aux chemins permis ; `COMMIT_CODE` le reprend), `NOYAU_EMPREINTE_PROPRE=192b2128…`
     (empreinte de l'arbre `essaim_m3/noyau` sans bytecode à ce commit, recalculée ici par `git archive` et la fonction du noyau ;
     `61ddd638…` au commit `8e5e2f7b`, retrouvée par la même méthode ; `CODE_NOYAU_PROPRE` la reprend) et
     `QUESTION_CARACTERES_MAX=100000` (vérifiée égale à `CARACTERES_MAX_QUESTION` de `question.py` du code attendu, importé depuis
     la copie : paramètre et noyau vont ensemble) ; messages et notes nomment `${NOYAU_COMMIT:0:8}` ;
   - clés `maieutique` (nom `course-maieutique-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2-maieutique`, enfant 0, sans annexe)
     et `audit` (`course-audit-gemini-v6-2-v1`, `gemini-organisme-v6-2-audit`, enfant 1, emplacements 1 à 4) ; `v6-2` et `v6-2-s`
     refusées dans le `case`, en réel comme en simulation ; même organisme ;
   - `GO_ID` lu de l'environnement juste après `COURSE` (forme `GO-AAAA-MM-JJ-NN` exigée), jamais fixé ; la ligne `GO_ID=GO-2026-10-25-02`
     retirée ; messages et commentaires du registre au GO de la course ;
   - étape 2 : `TEXTE` et `TEXTE_SHA256` à la place de `PREREG` et `PREREG_SHA256` ; ligne `graine de la course <clé> = <N>` lue et
     recalculée (enfant `INDICE_GRAINE`) ; la ligne de l'autre course exigée (`^ *graine de la course <autre> = [0-9]+$`), non utilisée ;
     note « texte : … (enfant k), ligne de la course <autre> présente (non utilisée) » ;
   - étape 3 : question de base présente au commit (`cat-file -e`) et d'empreinte juste ; chaque annexe servie : commit présent,
     chemin présent au commit, empreinte juste ; `question.md` composé par `composer_question` (question, puis pour chaque annexe
     servie `\n---\n\n# Annexe k — <chemin> (sha256 <empreinte>)\n\n` et son contenu) ; empreinte du composé recalculée depuis le
     dépôt à chaque segment et comparée au fichier ; **borne du noyau** : la question servie doit faire au plus
     `QUESTION_CARACTERES_MAX` caractères (100 000 au noyau `9beee10b` ; 20 000 jusqu'au `8e5e2f7b`), sinon refus avant tout
     appel ; `SHA_QUESTION` reste celle de la question de base (ligne de GO, note « question (clé) : sha256 … (<fichier>, commit …) ;
     annexes servies : n ; annexe k : chemin commit sha ») ; ligne nouvelle `- question servie : question.md, sha256 <composé>, <N>
     caractères` (N = caractères UTF-8, comme le manifeste du noyau) ; RÉSERVE consignée si la course « audit » part sans aucune
     annexe ; en simulation, `ESSAI_ANNEXE_1_COMMIT`, `ESSAI_ANNEXE_1_CHEMIN`, `ESSAI_ANNEXE_1_SHA` (ensemble, interdites en réel)
     remplacent l'annexe 1 ; artefacts d'essai `question` (fichier servi altéré), `question-base` (empreinte attendue à 0),
     `question-v1` et `question-v2` (chemins des v1 et v2 de la question « audit » : empreinte autre), `annexe` (empreinte de
     l'annexe 1 à 0), `annexe-absente` (chemin de l'annexe 1 inexistant), `annexe-vide` (emplacement 1 vidé : la RÉSERVE) ;
   - porte « course v6.2 précédente » retirée (`PRECEDENTE_V62` sans effet, `LANCEUR_V62_*`, `EMP_V62`, contrôle de la graine v6-2 et
     part « empreintes de la v6.2 » de la ligne de dépense retirés) ; porte « course M de référence » et chaîne de `grep` de la
     ligne de GO inchangées ; `PERMIS_APRES_CODE` permet `prereg/courses-question-gemini-v6-2-v[0-9]+.md(.sha256)?` et ses
     contre-lectures ;
   - garde « refus-question » (étape 7 bis) : le noyau est lancé sous `setsid` (groupe de processus propre, relu dans `/proc`) ;
     veilleur `garde_refus_question` lancé après le minuteur, qui lit toutes les 2 s, dès que la course est en cours (même critère
     que le minuteur), `<espace attendu>/travail/<lignée>/g001.noyau/journal-appels.jsonl` (lignes complètes seulement, champs
     `id`, `role`, `statut`, `fin`), `ESSAI_JOURNAL_GARDE` à la place en simulation ; règle ci-dessus ; au premier appel qui la
     déclenche : marqueur `garde-refus-question-v1.json`, `tuer_noyau` (TERM au groupe du noyau, KILL après 5 s, puis KILL des
     sessions de ses enfants directs relevés par `pgrep -P`, par PID), ligne `- arrêt par la garde refus-question : appel <id>,
     rôle <rôle>, statut <statut>, fin <fin> (<heure UTC>) ; course fermée sans reprise`, ligne « garde refus-question : règle
     « … » ; noyau … tué … », pièce JSON (appel sans texte, règle, heure, PID tués, paramètres) ; après `wait`, le lanceur saute les
     branches « fin de segment » et ferme la course (étape 8a) ; `permis_re` et les compagnons couvrent la pièce ; liste close des
     raisons de sûreté : `refusal SAFETY PROHIBITED_CONTENT BLOCKLIST SPII RECITATION IMAGE_SAFETY BLOCAGE_PROMPT` (toutes les
     raisons qui valent REFUS dans `statut_reponse`) ; sans arrêt, note « garde refus-question : aucun arrêt ; veilleur arrêté par
     son PID » ; `ESSAI_JOURNAL_GARDE` interdite en réel.
2. `deriver_essais_question_v14.py` : dérive `essais_lanceur_question_v14.sh` (822 lignes) de `essais_lanceur_pilote4_v13.sh`
   (701 lignes, `7b0a9bb0…`) : 18 blocs réécrits ou retirés par ancre vérifiée par empreinte, 9 remplacements exacts ciblés, 19
   remplacements globaux comptés sur le texte restant (noms, clés, graines, texte, GO, noyau attendu ; les noms et le GO d'hier
   gardés dans `go-autre-id`, `dep-absente` et `dep-ancienne-forme` sont protégés par des jetons), 78 contrôles. Écart (non
   demandé) : `diff-essais-v13-vers-v14.txt` (873 lignes). `bash -n` : conforme. Cas : v13 = 240 ; v14 = 372 (voir la
   série v16). Deux annexes synthétiques sont committées dans la copie `depot` au début de la série, puis retirées de sa tête
   (`reset --hard HEAD~1`, objets lisibles par `git show`) : `annexe-essai-v1.md` (l'annexe de la course « audit » saine) et
   `annexe-longue-v1.md` (100 029 caractères : le refus « question servie > 100000 »), toutes deux sous
   `essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/`. Les lignes de GO d'essai (`ligne_go`) citent `noyau 9beee10b`.
   Paramètres définitifs : la course « audit » saine (`sain-audit`) tourne **sans variable d'essai d'annexe**, sur la question v3
   et l'annexe réelle du commit `ad23e9ae` (récupéré dans les copies par `git fetch origin main`) ; la batterie recompose la
   question servie depuis le dépôt (v3, séparateur, titre, annexe) et la compare au fichier et au journal, et **vérifie la taille
   servie : 39 617 caractères ≤ 100 000** (3 430 + 163 + 36 024 ; `sain-audit-taille-servie-sous-la-borne`, `-relevee`) ;
   `annexe-empreinte-fausse` (annexe réelle, empreinte `01234567…` : refus « empreinte de l'annexe 1 … ≠ », aucun dossier
   `course/`, aucun manifeste : refus avant tout appel) ; `question-v2-refusee`, `go-question-v2-refuse-audit` ;
   `audit-sans-annexe-reserve` par l'artefact `annexe-vide` (question servie = la v3 seule, 3 430 caractères). Garde :
   journaux synthétiques par `journal_garde FICHIER MOTIF…` (`ROLE[:STATUT[:FIN]][*N]`) ; cas sans arrêt
   `garde-refus-question-sain` (REFUS sur `inducteur_entrainement`), `-ligne-incomplete`, `-tache-refusee` (REFUS
   `monoculture_analytique` au rang 3, sans moissonneur), `-rang-120` (120e appel en REFUS, sans moissonneur), `-moissonneur-refuse`,
   `-motif-reel-m-avant-question` (les 124 premiers appels réels : cinq REFUS de tâche, aucun arrêt) ; cas d'arrêt (`garde_artefact` :
   ligne, règle, pièce et compagnon poussés, g001 jamais archivée, arrêt sous 10 s, SEGMENT=2 refusé) `-artefact` (arbitre REFUS),
   `-fin-surete` (`critique_adversariale_limites`, MODELE_NON_CONFORME, `fin` SAFETY), `-critique-sans-moissonneur`,
   `-apres-moissonneur` (10 tâches, moissonneur, REFUS `monoculture_analytique` : règle « après le premier appel moissonneur_* »),
   `-rang-121` (121e appel `monoculture_analytique` en REFUS, sans moissonneur : règle « au rang 121 > 120 »),
   `-premiere-caste-apres-moissonneur` (les 124 appels réels puis la première caste de la question en REFUS, `organisme-0125`),
   `-motif-reel-m-complet` (les 129 appels réels : arrêt à `organisme-0129`, l'arbitre).
3. Série v15 (batterie v14 d'avant les deux décisions, sur le lanceur v12 d'avant, copies à la tête `2688148` avec les commits
   `eb03bad5` et `9417652a`) : quatre lancements le 26 octobre 2026 (heures UTC, `date -u`) : (1) 12:07:28 à 12:10:46, refus de la
   course M de référence (`test_sources_reelles_de_moisson_si_reseau` du noyau en échec : arXiv a répondu « HTTP Error 429: Too Many
   Requests » ; 46 sur 276 cas ; journal `essais-lanceur-question-v15-essai-rate-arxiv-429.log`) ; (2) 12:22:55, course « audit »
   saine refusée par le noyau (`refus : question ouverte : question de 93075 caractères > 20000` : les trois annexes initiales ;
   série arrêtée à la main, journal `…-essai-rate-annexes-93075-caracteres.log`) ; (3) 12:39:53 à 12:51:23, 285 sur 287 : la
   batterie passait l'annexe synthétique à deux cas réels de la course « audit », refusés pour variable d'essai en mode réel
   (journal `…-essai-rate-annexe-reel.log` ; `cas` corrigé : annexe synthétique hors du mode réel seulement) ; (4) 12:52:28 à
   13:04:06, 287 sur 287 (journal `essais-lanceur-question-v15.log`, heures `essais-lanceur-question-v15.heures.txt`). Le lanceur
   et la batterie de cette série ont été remplacés par les versions finales (mêmes noms) après les deux décisions.
4. Série v16 (lanceur v12 et batterie v14 après les deux décisions, encore sur la question « audit » v2 et l'annexe synthétique ;
   `lancer-serie-v16.sh`, copie de `lancer-serie-v15.sh` ; copies d'essai portées à la tête `9beee10b` par `git fetch origin
   outils/pilote4-gemini-travail` puis `checkout --detach`) : deux lancements le 26 octobre 2026 (heures UTC, `date -u`) : (1) 13:29:52 à 13:42:26, 360 sur 367 — les sept échecs
   sont le vérificateur `-noyau-tue` des sept cas d'arrêt, qui attendait l'ancienne ligne « garde refus-question : noyau … »
   (la ligne porte désormais la règle avant le noyau tué) ; tout le reste conforme, dont les quatorze cas de la règle
   (journal `essais-lanceur-question-v16-essai-rate-attendu-noyau-tue.log` ; vérificateur corrigé dans le dériveur) ;
   (2) 13:42:46 à 13:55:29, 367 sur 367 (journal `essais-lanceur-question-v16.log`, heures `essais-lanceur-question-v16.heures.txt`).
   Le lanceur et la batterie de cette série ont ensuite reçu les paramètres définitifs de la course « audit » (mêmes noms).
5. Série v17 (lanceur v12 et batterie v14 finaux, paramètres définitifs de la course « audit » ; `lancer-serie-v17.sh`, copie de
   `lancer-serie-v16.sh` ; le commit `ad23e9ae` de `main` récupéré dans les copies, leur tête inchangée à `9beee10b`) : un lancement le 26 octobre 2026, 14:00:55 à 14:13:42 UTC (`date -u`), **372 sur 372 cas conformes** (« tout
   conforme »). Journal : `essais-lanceur-question-v17.log`, heures `essais-lanceur-question-v17.heures.txt`.

## Choix faits seul (une ligne chacun)

- Règle (b) de la garde : le critère « refusé » (statut REFUS ou `fin` de sûreté) est le même pour `monoculture_analytique` que
  pour les rôles propres ; « après le premier appel `moissonneur_*` » se lit dans l'ordre des lignes du journal (le journal est
  écrit à la fin de chaque appel) ; le moissonneur lui-même refusé ne compte pas (il n'est pas une caste de la question) ; quand
  les deux conditions de (b) valent, la règle consignée est « après le premier appel moissonneur_* ».
- Le noyau attendu est un bloc de trois paramètres (commit, empreinte de l'arbre, borne) : changer de noyau = trois lignes, et le
  lanceur vérifie lui-même que la borne paramétrée est celle du code (`question.CARACTERES_MAX_QUESTION`, importé depuis la copie).
- Séparateurs des annexes : une ligne vide avant `---` et après, et après le titre (sans la ligne vide, `---` sous une ligne de
  texte serait lue comme un soulignement de titre en Markdown) ; la batterie recompose le fichier indépendamment et compare.
- `N caractères` = longueur du texte décodé en UTF-8 (celle que le manifeste du noyau consigne), pas les octets.
- Le noyau est lancé sous `setsid` pour que la garde puisse tuer son groupe sans toucher au lanceur ; conséquence : tuer le groupe
  du lanceur ne tue plus le noyau (R10 veut de toute façon un arrêt par PID, consigné) ; le groupe est relu dans `/proc` au moment
  de tuer, avec repli sur le PID seul s'il n'est pas le sien.
- Les enfants directs du noyau (organisme en bac à sable, chacun dans sa propre session par `os.setsid()` dans `bac_a_sable.py`)
  sont tués par leurs sessions, par PID relevé avant le TERM : le noyau tué par TERM (pas de gestionnaire de signal dans
  `boucle.py`) ne les nettoierait pas.
- Le veilleur n'agit que si la course est en cours (manifeste écrit ; reprise consignée au segment K ≥ 2) : un arrêt avant le
  manifeste ferait prendre la branche « aucune course partie ».
- Le marqueur est écrit avant de tuer ; si la garde se déclenche alors que la course finit d'elle-même, la ligne d'arrêt est écrite
  et la fermeture est la même (course finie, sans reprise).
- La pièce `garde-refus-question-v1.json` contient l'enregistrement du journal sans texte (le journal n'en porte pas : empreintes
  seulement), la règle, l'heure, les PID, les paramètres de la garde ; poussée avec son compagnon.
- Le motif réel de la course M est embarqué dans la batterie sous forme compacte (suite des rôles, statuts et raisons d'arrêt des
  129 appels, aucun autre champ) et vérifié à chaque série par l'empreinte de la suite « rôle statut fin », relevée sur le journal
  réel poussé (`fec0cb82…`) : les copies d'essai n'ont pas besoin de la branche des pilotes.
- `cas` de la batterie : `COURSE=audit` entraîne `GO_ID=GO-2026-10-26-04`, la pièce de dépense `td-sain-audit.json` et, hors du
  mode réel seulement (les variables d'essai y sont interdites), l'annexe synthétique (`ESSAI_ANNEXE_1_*`, que le cas peut
  redéfinir ou vider) ; course par défaut `maieutique` (GO 05) ; les clés `v6-2-s` et `v6-2` d'hier sont devenues `maieutique`
  (la première course saine avec les essais du noyau, les segments, la fermeture CLORE=1, le mutant, la garde et les cas par
  défaut) ; la seconde course saine, les artefacts de question et d'annexe et les cas de registre doublés tournent sur `audit`.
- La question servie de la course « audit » saine est recomposée par la batterie elle-même (question v2 extraite du commit
  `9417652a`, séparateur, titre, annexe synthétique) et comparée à `question.md` et à la ligne « question servie » du journal.
- Les lignes de GO d'essai suivent la forme de la ligne d'extension du texte v1 (`ligne_go`, `noyau 9beee10b`), les lignes de
  dépense la forme `| date | nom | GO | 75 USD au pire cas | empreintes de M <16> |` ; « ancienne forme refusée » = les lignes du
  pilote 4 (noms et GO d'hier, part « de v6.2 ») ne consignent pas ces courses.
- Les cas réels de l'étape (0) courent sur `maieutique` (et un sur `audit`) sans `PRECEDENTE_V62` : la porte est bien absente.
- Les copies d'essai sont à la tête `9beee10b` (le noyau attendu, sans commit postérieur) : la course M de référence court sur
  `depot-m`, inchangée ; le texte des courses n'est pas dans les copies (les textes d'essai sont synthétiques).

## Ce qui reste, ou n'a pas été vérifié

- **La course « audit » ne part pas (R-519)** : rien n'est lancé ; sa clé, ses paramètres (question v3, annexe) et ses cas d'essai
  restent en place, inutilisés, jusqu'à une décision de Lazar. La course « maieutique » ne dépend d'aucun d'eux : clé
  `maieutique`, GO-2026-10-26-05, question `1d29fbec…` à `eb03bad5`, sans annexe (les artefacts d'annexe sont sans effet sur
  elle : `annexe-artefacts-sans-effet-maieutique`) ; sa copie de lancement doit porter `eb03bad5` (et `ad23e9ae` n'est exigé
  que de la course « audit » : le lanceur ne vérifie que les commits de la course lancée).
- Les paramètres de la course « audit » sont définitifs (R-518) ; la copie de lancement doit porter le commit `ad23e9ae` de
  `main` (`git fetch origin main` avant la course : le lanceur refuse « commit … absent du dépôt (git fetch) » sinon). Si une
  question ou l'annexe change encore : trois lignes du bloc de paramètres, l'empreinte du lanceur change, `lancer-serie-v17.sh`
  rejoue la batterie v14 sans dérivation (attendu : 372 sur 372 ; `sain-audit-taille-servie-relevee` attend 39 617
  caractères et est à ajuster) ; la taille servie doit rester ≤ 100 000 caractères (titre d'annexe : 95 + longueur du chemin).
- Le texte v1 des courses cite encore `noyau 8e5e2f7b` dans ses lignes d'extension de GO et sa table (à mettre à `9beee10b` par
  conv-audit) ; le lanceur ne lit pas le commit du noyau dans la ligne de GO (il exige `calcul`, l'empreinte de la question,
  celle de l'organisme et celle du texte).
- `GO_ID` n'est pas fixé par le lanceur ; les lignes de GO (`GO-2026-10-26-05` maieutique, `GO-2026-10-26-04` audit) sont celles du
  brief, utilisées dans les cas d'essai et les messages ; le lanceur accepte tout identifiant de la forme `GO-AAAA-MM-JJ-NN` qui a sa
  ligne « calcul » au registre avec l'empreinte de la question de la course et celle du texte.
- La garde n'a été essayée qu'avec des journaux synthétiques (dont le motif réel de la course M) et sur le noyau simulé (tué en
  c001 ou g000 : g001 n'y est jamais archivée) ; sur un journal réel de g001, seule la lecture « aucun arrêt » a tourné (courses
  saines, journal vivant réel lu).
- Le lanceur v12 n'a pas tourné en réel ; `setsid`, `pgrep -P` et `/proc/<pid>/stat` sont ceux de ce conteneur.
- La tête de la copie de lancement de session-depot (texte v1, § Plan) doit ne différer de `9beee10b` que par les chemins permis :
  le texte des courses et ses contre-lectures le sont ; le reste de cette tête n'a pas été vérifié ici.
- Le lanceur v12 n'a pas été exécuté sur le vrai texte scellé (aucun : le texte v1 est un brouillon sans graines).
- La contre-lecture 9 et le scellement (`sceller_courses_question_v6.py`) ne sont pas de ce brief.

## Empreintes

- `lancer_courses_question_v12.sh` : `ee6ceb5cf39b3334d8d93fb3ab2c81de1c5247882562c28587c679d29b5f1687`
- `deriver_lanceur_question_v12.py` : `b08b85193619d021fd57e14e88852488ebab4c74bd73b3ea97586e513169592a`
- `diff-lanceur-v11-vers-v12.txt` : `e42423c7efb3cfce70f46d4d6bfa7f9168828e7a202e69762527b95ebaac91cd`
- `essais_lanceur_question_v14.sh` : `59944102f4473ff9a11ccd4001266fea0f51bcf20a1a86a99b64f28f3b0ce42f`
- `deriver_essais_question_v14.py` : `a8b6eff54c1e105452e171152a5ebf80724076b59b66739035b7a010f0a9262e`
- `diff-essais-v13-vers-v14.txt` : `66490079c9496fae02e41ac773e1bc3879fb440f6e0a131dcd67ae761477a59b`
- `essais-lanceur-question-v17.log` : `eb2739f1c186ba85471fba34ec71db559bab49572ffbee0c20a6e02cace7f1a0`
- `essais-lanceur-question-v17.heures.txt` : `a1bc52eee15ee3f6d23ff9d9d7ec6fccbbabfd43eac9f381713c904d03d3f0ae`
- `essais-lanceur-question-v16.log` : `e469db547ed577c0fe17d426f433bee23666e61729a88d642c2a3e6dd4f102ad`
- `essais-lanceur-question-v16.heures.txt` : `981b44ed89b3e7e66bc54b5a844d08bb5ad4387c5f9b36849b6a1161d59d1568`
- `essais-lanceur-question-v16-essai-rate-attendu-noyau-tue.log` : `1436d85be5597bf872c35f0bcb4a036709329620a380f806029520ab8cf6e3fb`
- `essais-lanceur-question-v15.log` : `913043447d7d9ea06c325d9f38d348598391bccc6efdc18c4cd58bc2b79f3087`
- `essais-lanceur-question-v15.heures.txt` : `83ddd3c38aa0514b3aa1cf257d6c3ffbae46e05f4b8998b2590e16133d353641`
- `essais-lanceur-question-v15-essai-rate-arxiv-429.log` : `273268037cb60ea8569d0fbf49ec9ab439646be4c42761bc2bdf4ac733610799`
- `essais-lanceur-question-v15-essai-rate-annexes-93075-caracteres.log` : `1b386eb6852692a3b76815e6f5bc8f35d53a03c885923def8fc2d26676216321`
- `essais-lanceur-question-v15-essai-rate-annexe-reel.log` : `771fb23440099ca5c8e0bbd2ec506704d15e1d2246f90bdd04df4bc1f8516a33`
- scripts des séries, hors dépôt (copie d'essai) : `/var/tmp/batterie-v13-v1/lancer-serie-v17.sh` `897349570b6aa8ab…` ; `/var/tmp/batterie-v13-v1/lancer-serie-v16.sh` `45bafb78220ee350…` ; `/var/tmp/batterie-v13-v1/lancer-serie-v15.sh` `8ab81ae9943aa9d6…`
- `lanceur-v12-v1/LISEZMOI-lanceur-v12-v1.md` : voir son compagnon `.sha256` (écrit après ce fichier).
