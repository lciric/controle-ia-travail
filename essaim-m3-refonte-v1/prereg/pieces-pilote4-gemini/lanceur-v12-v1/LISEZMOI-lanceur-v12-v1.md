# LISEZMOI — lanceur v12 des deux courses à question de la v6.2.1, batterie v14, série v15 — v1

Écrit par le sous-agent qui a dérivé le lanceur v11 et la batterie v13 (brief `lanceur-v11-v1/`), sur le brief de conv-audit du
26 octobre 2026 (message de coordination, puis précision : un seul texte pour les deux courses), le @@HEURE@@ (heure lue sur
`date -u` dans la commande qui a écrit ce fichier). Sources lues : le lanceur v11 (`21854b79…`), la batterie v13 (`7b0a9bb0…`), le
texte `prereg/courses-question-gemini-v6-2-v1.md` (brouillon de conv-audit, non scellé), `sceller_courses_question_v6.py`, le code
du noyau (`essaim_m3/noyau/appels.py`, `boucle.py`, `bac_a_sable.py`, `serveur.py`, `question.py`, `archive.py`) et les conventions
du collisionneur v2.5 (`collisionneur_v2.py`, `213b52ef…`, `statut_reponse` et `REFUS_GEMINI`), le code de la v6.2.1 au commit
`7ea32705…` (`mitose_spectrale.py`, `principal.py`, `CONCEPTION.md` : rôles des castes), les cinq fichiers servis au commit
`eb03bad5` (empreintes et tailles seulement, contenu non lu), le journal d'appels poussé de g001 de la course M du pilote 4
(`pilotes/pilote4-gemini-v6-2-v1`, rôles et statuts seulement, aucun score), les copies d'essai d'hier et `lancer-serie-v14.sh`.
Ni clé lue, ni script de la relève exécuté, ni poussée, ni commit ; `python3 -I` partout ; `git` : `fetch` du commit `eb03bad5`
dans les deux copies d'essai (seule action demandée), `show`/`cat-file`/`log`/`grep`/`merge-base` en lecture.

## Réserve à lire avant tout lancement réel : la garde « refus-question » telle que spécifiée arrêterait la course sur un refus de tâche

La garde arrête la course au premier appel dont le rôle est l'un des cinq rôles des castes de la question
(`monoculture_analytique`, `monoculture_croisee`, `sonde_orthogonale_onsager`, `critique_adversariale_limites`,
`arbitre_synthese_contradictoire`) et dont le statut est REFUS (ou dont `fin` est une raison d'arrêt de sûreté). Or, dans la
v6.2.1, `monoculture_analytique` est aussi la caste qui résout les tâches de la banque (`planifier_castes`, `mitose_spectrale.py`,
indice 0 ; avec 160 appels pour ≈ 121 tâches, chaque tâche n'a que cette caste), et `monoculture_croisee` et
`sonde_orthogonale_onsager` le seraient avec plus d'appels par tâche. Seuls `critique_adversariale_limites` et
`arbitre_synthese_contradictoire` sont propres à la question (les tâches utilisent `arbitre_contradictoire_<k>`). Les appels de la
question sont, en g001, les cinq derniers appels (après l'appel `moissonneur_formulation_requetes` de la moisson sur la question),
et rien dans le journal ne les distingue d'un appel de tâche de même rôle (même étape `organisme`, même `max_tokens` 8192,
empreinte de consigne imprévisible).

Fait : dans le journal réel de g001 de la course M du pilote 4 (129 appels), cinq appels de tâche `monoculture_analytique` ont le
statut REFUS (`refusal`, 0 caractère : `organisme-0029`, `0046`, `0056`, `0111`, `0121`), avant les appels de la question
(`0125` à `0129`) ; l'arbitre de la question (`0129`, `arbitre_synthese_contradictoire`) a lui aussi été refusé. g000, g002, g003 et
c001 portent aussi des refus de tâche (8, 5, 8, 1). **Avec la liste spécifiée, la garde aurait tué la course M à `organisme-0029`
(04:06 UTC), au quart de g001, sur un refus de tâche, avant toute question.** Les deux courses à venir, sur la même banque et le
même organisme, y sont exposées de la même façon. Le lanceur v12 applique la liste spécifiée (variable `ROLES_QUESTION`, une
ligne), et la batterie le constate (`garde-refus-question-monoculture-analytique` : un REFUS `monoculture_analytique` arrête la
course). Décision attendue de conv-audit ou de Lazar, options :
- (a) restreindre `ROLES_QUESTION` aux rôles propres à la question (`critique_adversariale_limites`,
  `arbitre_synthese_contradictoire`, et, aux bornes actuelles, `monoculture_croisee`, `sonde_orthogonale_onsager`) : un seul
  remplacement exact ; mais un refus de la question par la caste 1 (`monoculture_analytique`) ne serait pas vu, et la question
  serait reposée à la caste 2 ;
- (b) garder les cinq rôles mais ne les considérer qu'après le premier appel `moissonneur_formulation_requetes` de g001 (début
  du bloc de la question dans la v6.2.1) : mécanique, mais lié au code de cet organisme, et sans effet si cette moisson n'a pas
  lieu ;
- (c) reconnaître un appel « qui porte la question » par sa consigne (`appels/<id>.prompt.txt` du dossier du noyau contient le
  texte servi) : le critère fidèle, mais le lanceur lirait les consignes de la course (hors du journal), ce que ses règles
  interdisent aujourd'hui ;
- (d) laisser tel quel, en acceptant qu'un refus de tâche en g001 ferme la course (fermeture sûre, livrable perdu).
Recommandation : (b) avec (a) en repli, après avis de conv-audit ; aucune de ces options n'a été appliquée.

## Fait

1. `deriver_lanceur_question_v12.py` : dérive `lancer_courses_question_v12.sh` (962 lignes) de `lancer_pilote4_gemini_v11.sh`
   (938 lignes, `21854b79…`) par 29 remplacements exacts (28 à 1 occurrence, `setsid env -i` à 2) et le retrait du bloc de la
   porte « course v6.2 précédente » (83 lignes, ancre vérifiée par son empreinte `2ff1cfec…`), puis 58 contrôles de présence ou
   d'absence. Écart : `diff-lanceur-v11-vers-v12.txt` (`diff -u`, 515 lignes). `bash -n` : conforme. Changements :
   - clés `maieutique` (nom `course-maieutique-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2-maieutique`, enfant 0, question
     `1d29fbec…`, sans annexe) et `audit` (`course-audit-gemini-v6-2-v1`, `gemini-organisme-v6-2-audit`, enfant 1, question
     `dd2c1016…`, trois annexes) ; `v6-2` et `v6-2-s` refusées dans le `case`, en réel comme en simulation ; même organisme ;
   - `GO_ID` lu de l'environnement juste après `COURSE` (forme `GO-AAAA-MM-JJ-NN` exigée), jamais fixé ; la ligne `GO_ID=GO-2026-10-25-02`
     retirée ; messages et commentaires du registre au GO de la course ;
   - étape 2 : `TEXTE` et `TEXTE_SHA256` à la place de `PREREG` et `PREREG_SHA256` ; ligne `graine de la course <clé> = <N>` lue et
     recalculée (enfant `INDICE_GRAINE`) ; la ligne de l'autre course exigée (`^ *graine de la course <autre> = [0-9]+$`), non utilisée ;
     note « texte : … (enfant k), ligne de la course <autre> présente (non utilisée) » ;
   - étape 3 : question de base présente au commit (`cat-file -e`) et d'empreinte juste, chaque annexe aussi ; `question.md` composé
     par `composer_question` (question, puis pour chaque annexe `\n---\n\n# Annexe k — <chemin> (sha256 <empreinte>)\n\n` et son
     contenu) ; empreinte du composé recalculée depuis le dépôt à chaque segment et comparée au fichier ; `SHA_QUESTION` reste celle
     de la question de base (ligne de GO, note « question (clé) : sha256 … ; annexes (3, commit eb03bad5…) : … ») ; ligne nouvelle
     `- question servie : question.md, sha256 <composé>, <N> caractères` (N = caractères UTF-8, comme le manifeste du noyau) ;
     artefacts d'essai `question` (fichier servi altéré), `question-base` (empreinte attendue à 0), `annexe` (empreinte de
     l'annexe 1 à 0), `annexe-absente` (chemin de l'annexe 1 inexistant) ;
   - porte « course v6.2 précédente » retirée (`PRECEDENTE_V62` sans effet, `LANCEUR_V62_*`, `EMP_V62`, contrôle de la graine v6-2 et
     part « empreintes de la v6.2 » de la ligne de dépense retirés) ; porte « course M de référence » et chaîne de `grep` de la
     ligne de GO inchangées ; `PERMIS_APRES_CODE` permet `prereg/courses-question-gemini-v6-2-v[0-9]+.md(.sha256)?` et ses
     contre-lectures ;
   - garde « refus-question » (étape 7 bis) : le noyau est lancé sous `setsid` (groupe de processus propre, relu dans `/proc`) ;
     veilleur `garde_refus_question` lancé après le minuteur, qui lit toutes les 2 s, dès que la course est en cours (même critère
     que le minuteur), `<espace attendu>/travail/<lignée>/g001.noyau/journal-appels.jsonl` (lignes complètes seulement, champs
     `role`, `statut`, `fin`), `ESSAI_JOURNAL_GARDE` à la place en simulation ; au premier appel conforme au critère : marqueur
     `garde-refus-question-v1.json`, `tuer_noyau` (TERM au groupe du noyau, KILL après 5 s, puis KILL des sessions de ses enfants
     directs relevés par `pgrep -P`, par PID), ligne `- arrêt par la garde refus-question : appel <id>, rôle <rôle>, statut
     <statut>, fin <fin> (<heure UTC>) ; course fermée sans reprise`, pièce JSON (appel sans texte, heure, PID tués, listes) ;
     après `wait`, le lanceur saute les branches « fin de segment » et ferme la course (étape 8a) ; `permis_re` et les compagnons
     couvrent la pièce ; liste close des raisons de sûreté : `refusal SAFETY PROHIBITED_CONTENT BLOCKLIST SPII RECITATION
     IMAGE_SAFETY BLOCAGE_PROMPT` (toutes les raisons qui valent REFUS dans `statut_reponse`) ; sans arrêt, note « garde
     refus-question : aucun arrêt ; veilleur arrêté par son PID » ; `ESSAI_JOURNAL_GARDE` interdite en réel.
2. `deriver_essais_question_v14.py` : dérive `essais_lanceur_question_v14.sh` (731 lignes) de `essais_lanceur_pilote4_v13.sh`
   (701 lignes, `7b0a9bb0…`) : 17 blocs réécrits ou retirés par ancre vérifiée par empreinte, 7 remplacements exacts ciblés, 16
   remplacements globaux comptés sur le texte restant (noms, clés, graines, texte, GO ; les noms et le GO d'hier gardés dans
   `go-autre-id`, `dep-absente` et `dep-ancienne-forme` sont protégés par des jetons), 43 contrôles. Écart (non demandé) :
   `diff-essais-v13-vers-v14.txt`. `bash -n` : conforme. Cas : v13 = 240 ; v14 = @@N_V14@@ (voir la série).
3. Série v15 : `lancer-serie-v15.sh` (copie de `lancer-serie-v14.sh` ; lanceur et batterie lus dans le worktree, non committés ;
   copies d'essai d'hier à la tête `2688148`, le commit `eb03bad5` récupéré dans `depot` et dans la copie sous `/root` par
   `git fetch origin refs/remotes/origin/main` — `main` du clone local ne le porte pas, sa référence `origin/main` oui) :
   @@SERIE@@. Journal : `essais-lanceur-question-v15.log`, heures `essais-lanceur-question-v15.heures.txt`.

## Choix faits seul (une ligne chacun)

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
  seulement), l'heure, les PID, les deux listes ; poussée avec son compagnon.
- `cas` de la batterie : `COURSE=audit` entraîne `GO_ID=GO-2026-10-26-04` et la pièce de dépense `td-sain-audit.json` ; course par
  défaut `maieutique` (GO 05) ; la clé `v6-2-s` d'hier est devenue `maieutique`, `v6-2` est devenue `audit` (les deux courses
  saines, les segments, la fermeture CLORE=1 et le mutant tournent sur `audit`, avec les annexes ; la seconde course saine, la
  garde et les cas par défaut sur `maieutique`).
- Les lignes de GO d'essai suivent la forme de la ligne d'extension du texte v1 (`ligne_go`), les lignes de dépense la forme
  `| date | nom | GO | 75 USD au pire cas | empreintes de M <16> |` ; « ancienne forme refusée » = les lignes du pilote 4 (noms et
  GO d'hier, part « de v6.2 ») ne consignent pas ces courses.
- Les artefacts de la garde portent sur `arbitre_synthese_contradictoire` (REFUS), `critique_adversariale_limites`
  (MODELE_NON_CONFORME avec `fin` SAFETY : le critère sur `fin`) et `monoculture_analytique` (REFUS : le comportement spécifié,
  à reconsidérer, voir la réserve) ; le cas sain porte un REFUS sur `inducteur_entrainement` ; un cas « ligne incomplète » vérifie
  qu'une ligne sans fin de ligne n'est jamais lue.
- Les cas réels de l'étape (0) courent sur `maieutique` (et un sur `audit`) sans `PRECEDENTE_V62` : la porte est bien absente.
- Les copies d'essai gardent leur tête d'hier (`2688148`) : seuls les objets du commit `eb03bad5` sont nécessaires au lanceur ;
  le texte des courses n'est pas dans les copies (les textes d'essai sont synthétiques).

## Ce qui reste, ou n'a pas été vérifié

- La réserve ci-dessus (rôles de la garde) : décision à prendre avant le lancement réel.
- La garde n'a été essayée qu'avec des journaux synthétiques et sur le noyau simulé (tué en c001 ou g000 : g001 n'y est jamais
  archivée) ; sur un journal réel de g001, seule la lecture « aucun arrêt » a tourné (courses saines, journal vivant réel lu).
- Le lanceur v12 n'a pas tourné en réel ; `setsid`, `pgrep -P` et `/proc/<pid>/stat` sont ceux de ce conteneur.
- La tête de la copie de lancement de session-depot (texte v1, § Plan) doit ne différer de `8e5e2f7b` que par les chemins permis :
  le texte des courses et ses contre-lectures le sont désormais ; le reste de cette tête n'a pas été vérifié ici.
- Le lanceur v12 n'a pas été exécuté sur le vrai texte scellé (aucun : le texte v1 est un brouillon sans graines).
- La contre-lecture 9 et le scellement (`sceller_courses_question_v6.py`) ne sont pas de ce brief.

## Empreintes

@@EMPREINTES@@
