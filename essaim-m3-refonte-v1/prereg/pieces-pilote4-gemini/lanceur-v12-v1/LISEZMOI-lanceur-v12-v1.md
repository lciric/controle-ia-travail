# LISEZMOI — lanceur v12 des deux courses à question de la v6.2.1, batterie v14, séries v15 et v16 — v1

Écrit par le sous-agent qui a dérivé le lanceur v11 et la batterie v13 (brief `lanceur-v11-v1/`), sur le brief de conv-audit du
26 octobre 2026 (message de coordination, trois précisions : un seul texte pour les deux courses ; les annexes en bloc de
paramètres ; la question « audit » v2 à `9417652a` avec une seule annexe à remplir ; puis deux décisions : la règle de la garde
« refus-question », le noyau attendu `9beee10b` à la borne de 100 000 caractères), le @@HEURE@@ (heure lue sur `date -u` dans la
commande qui a écrit ce fichier). Sources lues : le lanceur v11 (`21854b79…`), la batterie v13 (`7b0a9bb0…`), le texte
`prereg/courses-question-gemini-v6-2-v1.md` (brouillon de conv-audit, non scellé), `sceller_courses_question_v6.py`, le code du
noyau (`essaim_m3/noyau/appels.py`, `boucle.py`, `bac_a_sable.py`, `serveur.py`, `question.py` aux commits `8e5e2f7b` et
`9beee10b`, `archive.py`) et les conventions du collisionneur v2.5 (`collisionneur_v2.py`, `213b52ef…`, `statut_reponse` et
`REFUS_GEMINI`), le code de la v6.2.1 au commit `7ea32705…` (`mitose_spectrale.py`, `principal.py`, `CONCEPTION.md` : rôles des
castes), les questions aux commits `eb03bad5` et `9417652a` et les trois annexes initiales (empreintes et tailles seulement,
contenu non lu), le journal d'appels poussé de g001 de la course M du pilote 4 (branche `pilotes/pilote4-gemini-v6-2-v1`,
`pilote4-gemini-v6-2-v1-tentative2/journal-appels-g001.jsonl`, `fec0cb82…`, 129 appels : rôles, statuts et raisons d'arrêt
seulement, aucun score ni texte), les copies d'essai d'hier et `lancer-serie-v14.sh`. Ni clé lue, ni script de la relève exécuté,
ni poussée ; `python3 -I` partout ; `git` : `fetch` des commits des questions puis de la branche `outils/pilote4-gemini-travail`
dans les deux copies d'essai, `checkout --detach 9beee10b` dans ces copies, `show`/`cat-file`/`log`/`grep`/`merge-base`/`archive`
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

1. `deriver_lanceur_question_v12.py` : dérive `lancer_courses_question_v12.sh` (1045 lignes) de `lancer_pilote4_gemini_v11.sh`
   (938 lignes, `21854b79…`) par 41 remplacements exacts comptés (40 à 1 occurrence, `setsid env -i` à 2) et le retrait du bloc de
   la porte « course v6.2 précédente » (83 lignes, ancre vérifiée par son empreinte `2ff1cfec…`), puis 92 contrôles de présence
   ou d'absence comptés. Écart : `diff-lanceur-v11-vers-v12.txt` (`diff -u`, 651 lignes). `bash -n` : conforme. Changements :
   - bloc de paramètres en tête (après `refus_tot`) : `QUESTION_MAIEUTIQUE_COMMIT|CHEMIN|SHA` (`eb03bad5`, `1d29fbec…`),
     `QUESTION_AUDIT_COMMIT|CHEMIN|SHA` (`9417652a…`, `question-audit-controle-organismes-v2.md`, `ec3abf28…`), quatre
     emplacements d'annexe `ANNEXE_k_COMMIT|CHEMIN|SHA`, tous vides (l'annexe 1, transcription expurgée d'un rapport, est à remplir
     par session-depot : trois lignes à remplacer, l'empreinte du lanceur change) ; un emplacement vide n'est pas servi, un
     emplacement à moitié rempli est un refus ; les annexes servies sont numérotées dans l'ordre ; puis le **noyau attendu** :
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
     `question-v1` (chemin de la v1 de la question « audit » : empreinte autre), `annexe` (empreinte de l'annexe 1 à 0),
     `annexe-absente` (chemin de l'annexe 1 inexistant) ;
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
2. `deriver_essais_question_v14.py` : dérive `essais_lanceur_question_v14.sh` (809 lignes) de `essais_lanceur_pilote4_v13.sh`
   (701 lignes, `7b0a9bb0…`) : 18 blocs réécrits ou retirés par ancre vérifiée par empreinte, 9 remplacements exacts ciblés, 19
   remplacements globaux comptés sur le texte restant (noms, clés, graines, texte, GO, noyau attendu ; les noms et le GO d'hier
   gardés dans `go-autre-id`, `dep-absente` et `dep-ancienne-forme` sont protégés par des jetons), 58 contrôles. Écart (non
   demandé) : `diff-essais-v13-vers-v14.txt` (860 lignes). `bash -n` : conforme. Cas : v13 = 240 ; v14 = @@N_V14@@ (voir la
   série v16). Deux annexes synthétiques sont committées dans la copie `depot` au début de la série, puis retirées de sa tête
   (`reset --hard HEAD~1`, objets lisibles par `git show`) : `annexe-essai-v1.md` (l'annexe de la course « audit » saine) et
   `annexe-longue-v1.md` (100 029 caractères : le refus « question servie > 100000 »), toutes deux sous
   `essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/`. Les lignes de GO d'essai (`ligne_go`) citent `noyau 9beee10b`. Garde :
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
4. Série v16 (lanceur v12 et batterie v14 finaux ; `lancer-serie-v16.sh`, copie de `lancer-serie-v15.sh` ; copies d'essai portées
   à la tête `9beee10b` par `git fetch origin outils/pilote4-gemini-travail` puis `checkout --detach`) : @@SERIE16@@

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

- L'annexe 1 de la course « audit » (transcription expurgée d'un rapport) : trois lignes à remplir par session-depot
  (`ANNEXE_1_COMMIT`, `ANNEXE_1_CHEMIN`, `ANNEXE_1_SHA`), le commit poussé sur `main` avant la course ; **taille** : la question v2
  fait 3 196 caractères et le titre de l'annexe 95 + longueur du chemin, donc l'annexe tient au plus 96 709 − longueur du chemin
  caractères (UTF-8) sous la borne de 100 000, sinon le lanceur refuse avant tout appel. Après remplissage, l'empreinte du lanceur
  change : `lancer-serie-v16.sh` rejoue la batterie v14 sans dérivation (la batterie lit le lanceur qu'on lui donne) ; attendu :
  @@N_V14@@ sur @@N_V14@@, et un relevé des empreintes à refaire.
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

@@EMPREINTES@@
