"""Dérive le lanceur v12 des deux courses à question de la v6.2.1 (`lancer_courses_question_v12.sh`) du lanceur v11 du
quatrième pilote (`lancer_pilote4_gemini_v11.sh`, 21854b79…), par remplacements exacts au nombre attendu (texte
`courses-question-gemini-v6-2-v1.md`, table de correspondance ; ordre de Lazar, R-509 ; brief de conv-audit du 26 octobre
2026). Ce qui change, et rien d'autre :
1. clés `maieutique` et `audit` (les clés du pilote 4, `v6-2` et `v6-2-s`, sont refusées en réel comme en simulation) ; noms
   `course-maieutique-gemini-v6-2-v1` et `course-audit-gemini-v6-2-v1` ; lignées `gemini-organisme-v6-2-maieutique` et
   `gemini-organisme-v6-2-audit` ; même organisme, la v6.2.1 (`7ea32705…`, arbre `4f13647a…`, 26 fichiers) ; graines enfants
   0 (`maieutique`) et 1 (`audit`) d'un seul texte, dont le lanceur lit la ligne de sa clé et exige celle de l'autre sans
   l'utiliser (variables TEXTE et TEXTE_SHA256 à la place de PREREG et PREREG_SHA256) ; GO_ID lu de l'environnement (donné
   par session-depot : 05 pour `maieutique`, 04 pour `audit`), de la forme GO-AAAA-MM-JJ-NN ;
2. bloc de paramètres en tête du lanceur (une ligne par champ : un changement = le remplacement d'une ligne, vérifié par
   l'empreinte du lanceur) : questions de `main`, extraites et vérifiées — `maieutique` =
   `question-hypotheses-maieutique-organismes-v1.md` (commit `eb03bad5`, 1d29fbec…) ; `audit` =
   `question-audit-controle-organismes-v3.md` (commit `ad23e9ae`, 998960b8… ; paramètres définitifs de session-depot, R-518 ;
   la v1 dd2c1016… et la v2 ec3abf28… ne servent plus) — et, pour `audit`, jusqu'à quatre annexes (`ANNEXE_k_COMMIT`,
   `ANNEXE_k_CHEMIN`, `ANNEXE_k_SHA`) : l'annexe 1 est la transcription expurgée v2 du rapport consolidé
   (`docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md`, commit `ad23e9ae`, c1237687…, 37 563 octets),
   les emplacements 2 à 4 vides ; une annexe aux trois champs vides n'est pas servie, un emplacement à moitié rempli est un
   refus ; `question.md` =
   question, puis pour chaque annexe servie (numérotées dans l'ordre) une ligne `---`, un titre `# Annexe k — <chemin>
   (sha256 <empreinte>)` et son contenu (une ligne vide avant et après chaque séparateur et chaque titre) ; la question servie
   doit tenir dans la borne du noyau (paramètre QUESTION_CARACTERES_MAX, 100 000 caractères au noyau 9beee10b, vérifié égal à
   CARACTERES_MAX_QUESTION de `question.py` du code attendu) : refus sinon ;
   SHA_QUESTION reste celle de la question de base (ligne de GO, LANCEMENT.md) ; ligne nouvelle « question servie :
   question.md, sha256 …, N caractères » ; en simulation, ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN et ESSAI_ANNEXE_1_SHA
   (ensemble) remplacent l'annexe 1 (annexe synthétique de la batterie) ; artefacts d'essai `question` (fichier servi
   altéré), `question-base`, `question-v1`, `question-v2`, `annexe`, `annexe-absente`, `annexe-vide` (emplacement 1 vidé :
   la RÉSERVE « sans aucune annexe ») ;
3. porte « course v6.2 précédente » retirée (bloc 0 bis, variables LANCEUR_V62_*, EMP_V62, contrôle de la graine v6-2) ;
   PRECEDENTE_V62 sans effet ; porte « course M de référence » et chaîne de `grep` de la ligne de GO inchangées ; chemins
   permis après le code : le texte des courses à question et ses contre-lectures ;
4. garde « refus-question » : veilleur de fond lancé avec le noyau (lancé sous `setsid`, dans son propre groupe de
   processus), qui lit toutes les 2 s le journal d'appels vivant de g001 et, au premier appel d'un rôle des castes de la
   question en REFUS ou dont `fin` porte une raison d'arrêt de sûreté (liste close de `statut_reponse` et REFUS_GEMINI du
   collisionneur v2.5, chargé par le noyau), tue le noyau et ses enfants par PID, écrit la ligne « arrêt par la garde
   refus-question » et la pièce `garde-refus-question-v1.json` (poussée) : la course est fermée sans reprise ;
   ESSAI_JOURNAL_GARDE (simulation seulement) remplace le journal lu. Règle de conv-audit (26 octobre 2026, après le journal
   réel de g001 de la course M du pilote 4 : 120 appels de tâche `monoculture_analytique`, cinq en REFUS, avant la question) :
   (a) un appel refusé de l'un des quatre rôles propres à la question (`monoculture_croisee`, `sonde_orthogonale_onsager`,
   `critique_adversariale_limites`, `arbitre_synthese_contradictoire`) arrête toujours ; (b) un appel refusé de
   `monoculture_analytique` (qui sert aussi les tâches) arrête seulement s'il vient après le premier appel de rôle
   `moissonneur_*` de g001, ou s'il est au-delà du 120e appel de ce rôle en g001 (120 tâches servies, une caste par tâche :
   le 121e est une caste de la question) ; sinon rien ;
5. noyau attendu en paramètre (NOYAU_COMMIT = `9beee10b`, seul changement depuis `8e5e2f7b` : la borne de la question
   portée de 20 000 à 100 000 caractères, `question.py` ; NOYAU_EMPREINTE_PROPRE = empreinte de l'arbre essaim_m3/noyau sans
   bytecode à ce commit, 192b2128… ; QUESTION_CARACTERES_MAX = 100000) : le code de la copie (essaim_m3, tests, collisionneur)
   doit être identique à ce commit, lui-même ancêtre de HEAD, les commits postérieurs limités aux chemins permis.

Usage : python3 -I deriver_lanceur_question_v12.py LANCEUR_V11 SORTIE
Refuse si l'empreinte du lanceur v11 n'est pas 21854b79…, si une occurrence n'est pas au nombre attendu, si le bloc de la
porte retirée n'a pas l'empreinte attendue, si un reste interdit subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, re, sys

SHA_V11 = "21854b794de90d874b23def1685e306ceba80b32cd471de1dd8cf750ad01d0d7"
SHA_BLOC_PORTE = "2ff1cfecd7af37e97bc652a6bb76657b6faa0a64655afb50a7cc23b2291c6f03"   # bloc « 0 bis », 83 lignes, de la v11
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V11:
    sys.exit("refus : le lanceur source n'est pas la v11 21854b79…")
t = b.decode("utf-8")
Z64 = "0" * 64
remplacements = [
    # en-tête : objet, dérivation v12
    ("# Lanceur du quatrième pilote descriptif « organisme assisté de Gemini, la v6.2.1, seule, sur la question M puis sur la question S, sur la banque\n"
     "# `confrontation-v3` (identifiants opaques), quatre générations notées, 6 rondes de conception au plus avant g000 (l'organisme déclare lui-même la fin de sa conception, `fin_conception.json`), 3 USD au plus par ronde, question de la course (M, puis S) à g001 »,\n"
     "# une course en un ou plusieurs segments (COURSE=v6-2 sous le lanceur v10, puis COURSE=v6-2-s sous celui-ci ; SEGMENT=1, 2, …) — v11 : le lanceur v10\n",
     "# Lanceur des deux courses à question de la v6.2.1 (texte `courses-question-gemini-v6-2-v1.md`, ordre de Lazar, R-509) : « organisme assisté de Gemini, la v6.2.1, seule, sur la banque\n"
     "# `confrontation-v3` (identifiants opaques), quatre générations notées, 6 rondes de conception au plus avant g000 (l'organisme déclare lui-même la fin de sa conception, `fin_conception.json`), 3 USD au plus par ronde, question de la course (« maieutique », ou « audit » avec son annexe) à g001 »,\n"
     "# une course en un ou plusieurs segments (COURSE=maieutique, puis COURSE=audit ; SEGMENT=1, 2, …) — v12 : le lanceur v11\n"
     "# (21854b79…) par `deriver_lanceur_question_v12.py` (deux courses à question du même organisme, hors du pilote 4 : clés\n"
     "# `maieutique` et `audit`, noms `course-maieutique-gemini-v6-2-v1` et `course-audit-gemini-v6-2-v1`, lignées\n"
     "# `gemini-organisme-v6-2-maieutique` et `gemini-organisme-v6-2-audit`, graines enfants 0 et 1 d'un même texte ; questions\n"
     "# de `main` (« maieutique » à `eb03bad5`, « audit » v3 à `ad23e9ae`), la course « audit » servie avec son annexe (bloc de\n"
     "# paramètres en tête : la transcription expurgée v2 du rapport consolidé, même commit) dans `question.md` ; GO par course, donné\n"
     "# par session-depot (GO_ID) ; porte « course v6.2 précédente » retirée (rien n'est exigé des courses du pilote 4) ; les\n"
     "# clés `v6-2` et `v6-2-s` refusées ; garde « refus-question » (veilleur de fond sur le journal d'appels vivant de g001 : au\n"
     "# premier appel refusé d'un rôle propre à la question, ou de `monoculture_analytique` après le premier appel `moissonneur_*`\n"
     "# de g001 ou au-delà de son 120e appel, le noyau est tué et la course fermée sans reprise) ; noyau attendu en paramètre\n"
     "# (NOYAU_COMMIT 9beee10b : borne de la question 100 000 caractères) ; écart consigné dans `diff-lanceur-v11-vers-v12.txt`), la v11 dérivée du lanceur v10\n", 1),
    ("la porte « v6.2 précédente » (v9 ; dans l'ordre inverse jusqu'au v8)\n",
     "la porte « v6.2 précédente » (v9 ; dans l'ordre inverse jusqu'au v8 ; retirée en v12)\n", 1),
    ("# Objet des deux courses (M, puis S) : la v6.2.1, dossier `organisme/` — la v5.3 ne court pas (décision de Lazar, R-492), et la clé\n"
     "# `v6-2` ne sert plus qu'en simulation (la course M de ce pilote a tourné sous `lancer_pilote4_gemini_v10.sh`, R-490).\n",
     "# Objet des deux courses (« maieutique », puis « audit ») : la v6.2.1, dossier `organisme/` ; les clés du pilote 4 (`v6-2`, `v6-2-s`)\n"
     "# sont refusées en réel comme en simulation (ses courses M et S sont finies et fermées, R-494, R-498).\n", 1),
    ("# Texte : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md` (ou la version qui le remplace et cite ce\n"
     "# script) ; pièces : `prereg/pieces-pilote4-gemini/`.\n",
     "# Texte : `essaim-m3-refonte-v1/prereg/courses-question-gemini-v6-2-v1.md` (ou la version qui le remplace et cite ce\n"
     "# script) — un texte pour les deux courses, aux deux lignes « graine de la course maieutique = … » et « graine de la course\n"
     "# audit = … » (enfants 0 et 1 de son entropie, `sceller_courses_question_v6.py`) ; pièces : `prereg/pieces-pilote4-gemini/`.\n", 1),
    ("#   MODE=reel COURSE=v6-2-s DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO_USD=… \\\n"
     "#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=… CLE_ANTHROPIC=NOM CLE_GEMINI=NOM \\\n"
     "#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M> \\\n"
     "#       PRECEDENTE_V62=<dossier de la course M de ce pilote, pilote4-gemini-v6-2-v1[-tentativeN], dans la même copie> [SEGMENT=1] \\\n"
     "#       bash lancer_pilote4_gemini_v11.sh\n"
     "#   MODE=reel COURSE=v6-2 : refusée par ce lanceur (la course M de ce pilote a tourné sous le lanceur v10, R-490) ; MODE=simulation COURSE=v6-2 : permise\n",
     "#   MODE=reel COURSE=maieutique GO_ID=GO-2026-10-26-05 DEPOT=… PYTHON=… TEXTE=… TEXTE_SHA256=… GRAINE=… RESTE_GO_USD=… \\\n"
     "#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=… CLE_ANTHROPIC=NOM CLE_GEMINI=NOM \\\n"
     "#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M du second pilote> [SEGMENT=1] \\\n"
     "#       bash lancer_courses_question_v12.sh\n"
     "#   MODE=reel COURSE=audit GO_ID=GO-2026-10-26-04 … (même forme ; GO_ID est donné par session-depot, jamais fixé ici)\n"
     "#   COURSE=v6-2 ou COURSE=v6-2-s (clés du pilote 4) : refusées, en réel comme en simulation ; PRECEDENTE_V62 : sans effet (porte retirée)\n", 1),
    ("#   MODE=simulation : comme le lanceur v2 (variables d'essai inchangées)\n",
     "#   MODE=simulation : comme le lanceur v2 (variables d'essai inchangées ; en plus ESSAI_JOURNAL_GARDE=<journal synthétique lu par la garde refus-question> et\n"
     "#     ESSAI_ANNEXE_1_COMMIT=… ESSAI_ANNEXE_1_CHEMIN=… ESSAI_ANNEXE_1_SHA=…, ensemble : une annexe synthétique à la place de l'annexe 1)\n", 1),
    ("# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course (hors de son manifeste et de son état\n"
     "# de reprise, mécaniques) ou la sortie standard ; arrêter un\n"
     "# processus (R10 : PID consigné ; une course voisine est détectée, jamais arrêtée) ; écraser un dossier (R12) ; lancer\n",
     "# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course (hors de son manifeste, de son état\n"
     "# de reprise et, pour la garde refus-question, du journal d'appels vivant de g001 — rôle, statut, raison d'arrêt, jamais un\n"
     "# texte —, mécaniques) ou la sortie standard ; arrêter un\n"
     "# processus (R10 : PID consigné ; une course voisine est détectée, jamais arrêtée ; la garde refus-question tue le noyau de\n"
     "# cette course et ses enfants par leurs PID, consignés) ; écraser un dossier (R12) ; lancer\n", 1),
    # bloc de paramètres en tête : questions et annexes (une ligne par champ)
    ('refus_tot() { echo "REFUS : $*" >&2; exit 2; }   # refus avant que le dossier du pilote existe\n\n',
     'refus_tot() { echo "REFUS : $*" >&2; exit 2; }   # refus avant que le dossier du pilote existe\n\n'
     "# ---- Paramètres des questions et des annexes (texte v1 ; R-509, R-510, R-515, R-516) : une ligne par champ, changer un\n"
     "#      champ est le remplacement d'une ligne, vérifié par l'empreinte de ce lanceur. Annexes de la course « audit » : jusqu'à\n"
     "#      quatre emplacements (ANNEXE_k_COMMIT, ANNEXE_k_CHEMIN, ANNEXE_k_SHA) ; un emplacement aux trois champs vides n'est pas\n"
     "#      servi (les annexes servies sont numérotées dans l'ordre), un emplacement à moitié rempli est un refus ; l'annexe 1 est la\n"
     "#      transcription expurgée v2 du rapport consolidé (session-depot, R-518 : `main` à ad23e9ae, même commit que la question v3).\n"
     "#      La question servie (question, puis annexes) doit tenir dans la borne du noyau (QUESTION_CARACTERES_MAX ci-dessous,\n"
     "#      égale à CARACTERES_MAX_QUESTION de essaim_m3/noyau/question.py au noyau attendu), vérifiée à l'étape (3). En simulation, ESSAI_ANNEXE_1_COMMIT,\n"
     "#      ESSAI_ANNEXE_1_CHEMIN et ESSAI_ANNEXE_1_SHA (ensemble) remplacent l'annexe 1 (annexe synthétique de la batterie). ----\n"
     "QUESTION_MAIEUTIQUE_COMMIT=eb03bad56ece1e755afa5e264948d0c44416f6cc\n"
     "QUESTION_MAIEUTIQUE_CHEMIN=brouillons/questions-organismes-20261026-v1/question-hypotheses-maieutique-organismes-v1.md\n"
     "QUESTION_MAIEUTIQUE_SHA=1d29fbecd52b1dfc94410e117f786811067f86f3cce24c4c54bbe424e480e3a3\n"
     "QUESTION_AUDIT_COMMIT=ad23e9ae07588ed701a70b9b5f4bf379ca079953\n"
     "QUESTION_AUDIT_CHEMIN=brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v3.md\n"
     "QUESTION_AUDIT_SHA=998960b8d101d5013c498d6fcf225277ba17d20741825ad136381892c05cfd0e\n"
     "ANNEXE_1_COMMIT=ad23e9ae07588ed701a70b9b5f4bf379ca079953\n"
     "ANNEXE_1_CHEMIN=docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md\n"
     "ANNEXE_1_SHA=c1237687e98db14475336af690986bc08800a85e259d249de4940130245b1a64\n"
     "ANNEXE_2_COMMIT=\n"
     "ANNEXE_2_CHEMIN=\n"
     "ANNEXE_2_SHA=\n"
     "ANNEXE_3_COMMIT=\n"
     "ANNEXE_3_CHEMIN=\n"
     "ANNEXE_3_SHA=\n"
     "ANNEXE_4_COMMIT=\n"
     "ANNEXE_4_CHEMIN=\n"
     "ANNEXE_4_SHA=\n"
     "# ---- Noyau attendu (décision de conv-audit du 26 octobre 2026) : le commit du code (essaim_m3, tests, collisionneur) auquel\n"
     "#      HEAD de la copie doit être identique (lui-même ancêtre de HEAD, commits postérieurs limités aux chemins permis),\n"
     "#      l'empreinte de l'arbre essaim_m3/noyau sans bytecode à ce commit, et la borne de la question servie à ce commit\n"
     "#      (question.py, CARACTERES_MAX_QUESTION, vérifiée égale) : les trois lignes vont ensemble. 9beee10b = 8e5e2f7b plus la borne\n"
     "#      portée de 20 000 à 100 000 caractères (seul changement du noyau ; tests du noyau passés chez conv-audit). ----\n"
     "NOYAU_COMMIT=9beee10be4b66525a4ae98d69237abeb34ffbdac\n"
     "NOYAU_EMPREINTE_PROPRE=192b21283292df14b3e21cd454cb34bc213e8e49a8867a99243d28d9a4abc7d7\n"
     "QUESTION_CARACTERES_MAX=100000\n"
     "# ---- fin des paramètres ----\n\n", 1),
    # commit du code et empreinte du noyau : les paramètres
    ("COMMIT_CODE=8e5e2f7b8bde522e4b5ce0229a9da57e118d32f3\n", 'COMMIT_CODE="$NOYAU_COMMIT"   # paramètre en tête (noyau attendu)\n', 1),
    ("CODE_NOYAU_PROPRE=61ddd638d7a3b5519a7294fc04a75003e3d21da72b9cfdcf4dd07dc0341565a0\n", 'CODE_NOYAU_PROPRE="$NOYAU_EMPREINTE_PROPRE"   # paramètre en tête (noyau attendu)\n', 1),
    ("# 1. Code identique à 8e5e2f7b (commit et arbre de travail, collisionneur compris) ; commits postérieurs limités aux pièces\n",
     "# 1. Code identique au noyau attendu, NOYAU_COMMIT (commit et arbre de travail, collisionneur compris) ; commits postérieurs limités aux pièces\n", 1),
    ('refus "code de HEAD différent de 8e5e2f7b (essaim_m3, tests ou collisionneur)"', 'refus "code de HEAD différent de ${NOYAU_COMMIT:0:8} (essaim_m3, tests ou collisionneur)"', 1),
    ('refus "arbre de travail différent de 8e5e2f7b (essaim_m3, tests ou collisionneur)"', 'refus "arbre de travail différent de ${NOYAU_COMMIT:0:8} (essaim_m3, tests ou collisionneur)"', 1),
    ('refus "8e5e2f7b non ancêtre de HEAD"', 'refus "${NOYAU_COMMIT:0:8} non ancêtre de HEAD"', 1),
    ('refus "commits postérieurs à 8e5e2f7b hors des pièces du pilote : $(echo $hors_pieces)"', 'refus "commits postérieurs à ${NOYAU_COMMIT:0:8} hors des pièces du pilote : $(echo $hors_pieces)"', 1),
    ('note "- code : identique à 8e5e2f7b (commit et arbre de travail : essaim_m3, tests, collisionneur) ;', 'note "- code : identique à ${NOYAU_COMMIT:0:8} (noyau attendu ; commit et arbre de travail : essaim_m3, tests, collisionneur) ;', 1),
    ('refus "empreinte du noyau nettoyé $code_noyau ≠ 61ddd638…"', 'refus "empreinte du noyau nettoyé $code_noyau ≠ ${CODE_NOYAU_PROPRE:0:8}… (NOYAU_EMPREINTE_PROPRE)"', 1),
    # clé de course, GO
    ('COURSE="${COURSE:?COURSE=v6-2-s ou COURSE=v6-2}"\n',
     'COURSE="${COURSE:?COURSE=maieutique ou COURSE=audit}"\n'
     'GO_ID="${GO_ID:?GO_ID=identifiant du GO de la course, donné par session-depot (GO-2026-10-26-05 pour maieutique, GO-2026-10-26-04 pour audit) : le lanceur ne le fixe pas}"\n'
     '[[ "$GO_ID" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || refus_tot "GO_ID doit être de la forme GO-AAAA-MM-JJ-NN : « $GO_ID »"\n', 1),
    # questions par course, annexes, clés du pilote 4 refusées
    ("# Question par course (v11, R-492) : M v2 épurée (la même que celle de la course M du second pilote) pour `v6-2` ; S v2 (la\n"
     "#   question de la course S du second pilote) pour `v6-2-s` ; même organisme, la v6.2.1, pour les deux courses\n"
     'case "$COURSE" in\n'
     "  v6-2-s)\n"
     '    NOM="pilote4-gemini-v6-2-s-v1"; INDICE_GRAINE=0\n'
     "    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e\n"
     "    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d\n"
     "    N_FICHIERS_ORGANISME=26\n"
     '    LIGNEE="gemini-organisme-v6-2-s"\n'
     "    COMMIT_QUESTION=4772b525081342a6a30ba8823733aa5770a888a8\n"
     "    CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-apprendre-structure-entrainement-generations-organismes-v2.md\n"
     "    SHA_QUESTION=a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289;;\n"
     "  v6-2)\n"
     '    NOM="pilote4-gemini-v6-2-v1"; INDICE_GRAINE=1\n'
     "    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e\n"
     "    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d\n"
     "    N_FICHIERS_ORGANISME=26\n"
     '    LIGNEE="gemini-organisme-v6-2"\n'
     "    COMMIT_QUESTION=a15809b816b6c967b6c3cf21877e350bfe676dca\n"
     "    CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-gemini-maieutique-vs-coercition-organismes-v2.md\n"
     "    SHA_QUESTION=8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd;;\n"
     '  *) refus_tot "COURSE inconnue : $COURSE (v6-2-s ou v6-2)";;\n'
     "esac\n"
     "# v11 (R-492) : en réel, ce lanceur ne lance que la course S ; la course M de ce pilote (`v6-2`) a tourné sous le lanceur v10\n"
     "#   (R-490) ; en simulation, `v6-2` reste permise (la batterie en a besoin pour produire la course précédente)\n"
     'if [ "$MODE" = reel ] && [ "$COURSE" = v6-2 ]; then refus_tot "COURSE=v6-2 en mode réel : la course M a tourné sous le lanceur v10 (R-490) ; ce lanceur v11 ne lance en réel que v6-2-s (R-492)"; fi\n',
     "# Question par course (v12, R-509, R-510, R-515, R-516) : « maieutique » et « audit » (bloc de paramètres en tête) ; même\n"
     "#   organisme, la v6.2.1, pour les deux courses ; la course « audit » est servie avec les annexes remplies du bloc de\n"
     "#   paramètres (emplacements 1 à 4), composées dans question.md à l'étape (3) ; les clés du pilote 4 sont refusées\n"
     'case "$COURSE" in\n'
     "  maieutique)\n"
     '    NOM="course-maieutique-gemini-v6-2-v1"; INDICE_GRAINE=0\n'
     "    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e\n"
     "    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d\n"
     "    N_FICHIERS_ORGANISME=26\n"
     '    LIGNEE="gemini-organisme-v6-2-maieutique"\n'
     '    COMMIT_QUESTION="$QUESTION_MAIEUTIQUE_COMMIT"; CHEMIN_QUESTION="$QUESTION_MAIEUTIQUE_CHEMIN"; SHA_QUESTION="$QUESTION_MAIEUTIQUE_SHA"\n'
     '    ANNEXES="";;\n'
     "  audit)\n"
     '    NOM="course-audit-gemini-v6-2-v1"; INDICE_GRAINE=1\n'
     "    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e\n"
     "    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d\n"
     "    N_FICHIERS_ORGANISME=26\n"
     '    LIGNEE="gemini-organisme-v6-2-audit"\n'
     '    COMMIT_QUESTION="$QUESTION_AUDIT_COMMIT"; CHEMIN_QUESTION="$QUESTION_AUDIT_CHEMIN"; SHA_QUESTION="$QUESTION_AUDIT_SHA"\n'
     '    ANNEXES="1 2 3 4";;\n'
     '  v6-2|v6-2-s) refus_tot "COURSE=$COURSE : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)";;\n'
     '  *) refus_tot "COURSE inconnue : $COURSE (maieutique ou audit)";;\n'
     "esac\n"
     "# simulation : annexe 1 synthétique (R5, batterie) — les trois variables vont ensemble ; interdites en réel (liste des variables d'essai)\n"
     'if [ "$MODE" = simulation ] && { [ -n "${ESSAI_ANNEXE_1_COMMIT:-}" ] || [ -n "${ESSAI_ANNEXE_1_CHEMIN:-}" ] || [ -n "${ESSAI_ANNEXE_1_SHA:-}" ]; }; then\n'
     '  { [ -n "${ESSAI_ANNEXE_1_COMMIT:-}" ] && [ -n "${ESSAI_ANNEXE_1_CHEMIN:-}" ] && [ -n "${ESSAI_ANNEXE_1_SHA:-}" ]; } || refus_tot "ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN et ESSAI_ANNEXE_1_SHA vont ensemble"\n'
     '  ANNEXE_1_COMMIT="$ESSAI_ANNEXE_1_COMMIT"; ANNEXE_1_CHEMIN="$ESSAI_ANNEXE_1_CHEMIN"; ANNEXE_1_SHA="$ESSAI_ANNEXE_1_SHA"\n'
     "fi\n", 1),
    # variable d'essai de la garde, interdite en réel
    ("ESSAIM_M3_ESPACE ESSAI_ECHEANCE_STOP_S; do\n", "ESSAIM_M3_ESPACE ESSAI_ECHEANCE_STOP_S ESSAI_JOURNAL_GARDE ESSAI_ANNEXE_1_COMMIT ESSAI_ANNEXE_1_CHEMIN ESSAI_ANNEXE_1_SHA; do\n", 1),
    # GO par course
    ("GO_ID=GO-2026-10-25-02\n"
     "USD_GEN=30      # par génération (mêmes bornes que la course M ; décision (b) de Lazar, 25 octobre 10:17 Paris)\n"
     "USD_COURSE=75   # par course, tous segments compris (plafond total du noyau) ; deux courses : 150 USD au plus (décision de Lazar, 25 octobre, 20:23 Paris : 75 USD par course, GO-2026-10-25-02 à 185 USD au plus pour l'ensemble du GO ; la ligne d'extension est écrite par session-depot sur son mot direct)\n",
     "# GO_ID : lu en tête (un GO par course, donné par session-depot) ; bornes du pilote 4 (texte v1, table de correspondance)\n"
     "USD_GEN=30      # par génération (mêmes bornes que la course M ; décision (b) de Lazar, 25 octobre 10:17 Paris)\n"
     "USD_COURSE=75   # par course, tous segments compris (plafond total du noyau) ; chaque course sur son GO (GO-2026-10-26-05 ; GO-2026-10-26-04 partie (2) — mot direct de Lazar, R-509 ; la ligne d'extension est écrite par session-depot)\n", 1),
    # artefacts d'essai de la question servie
    ('[ "$ART" = commit ] && COMMIT_QUESTION=0123456789abcdef0123456789abcdef01234567\n',
     '[ "$ART" = commit ] && COMMIT_QUESTION=0123456789abcdef0123456789abcdef01234567\n'
     '[ "$ART" = question-base ] && SHA_QUESTION=' + Z64 + '\n'
     '[ "$ART" = question-v1 ] && CHEMIN_QUESTION=brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v1.md   # la v1 (dd2c1016…) ne sert plus : empreinte autre\n'
     '[ "$ART" = question-v2 ] && CHEMIN_QUESTION=brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v2.md   # la v2 (ec3abf28…) ne sert plus : empreinte autre\n'
     '[ "$ART" = annexe ] && ANNEXE_1_SHA=' + Z64 + '\n'
     '[ "$ART" = annexe-absente ] && ANNEXE_1_CHEMIN=docs/nulle-part-v1.md\n'
     '[ "$ART" = annexe-vide ] && ANNEXE_1_COMMIT= && ANNEXE_1_CHEMIN= && ANNEXE_1_SHA=   # emplacement 1 vidé : course « audit » sans annexe (RÉSERVE)\n', 1),
    # chemins permis après le code : le texte des courses à question et ses contre-lectures
    ("# Chemins que les commits postérieurs à 8e5e2f7b peuvent toucher : le texte du second pilote, ses pièces et ses\n"
     "# contre-lectures ; ce texte, ses pièces et ses contre-lectures ; dossier des pilotes\n",
     "# Chemins que les commits postérieurs au noyau attendu (NOYAU_COMMIT) peuvent toucher : le texte du second pilote, ses pièces et ses\n"
     "# contre-lectures ; les textes du pilote 4, leurs pièces et leurs contre-lectures ; le texte des courses à question et ses\n"
     "# contre-lectures (ses pièces sont sous pieces-pilote4-gemini/) ; dossier des pilotes\n", 1),
    ("|pilote4-gemini-organisme-v[0-9]+\\.md(\\.sha256)?|pieces-pilote4-gemini/.+|contre-lectures/pilote4-gemini-organisme-v[0-9]+-cl[0-9]+\\.md(\\.sha256)?)|banque/",
     "|pilote4-gemini-organisme-v[0-9]+\\.md(\\.sha256)?|courses-question-gemini-v6-2-v[0-9]+\\.md(\\.sha256)?|pieces-pilote4-gemini/.+|contre-lectures/pilote4-gemini-organisme-v[0-9]+-cl[0-9]+\\.md(\\.sha256)?|contre-lectures/courses-question-gemini-v6-2-v[0-9]+-cl[0-9]+\\.md(\\.sha256)?)|banque/", 1),
    # étape 2 : le texte (un texte pour les deux courses)
    ("# 2. Préenregistrement scellé (réel ; en simulation si PREREG est donné) ; graine recalculée depuis l'entropie\n"
     'if [ "$MODE" = reel ] || [ -n "${PREREG:-}" ]; then\n'
     '  PREREG="${PREREG:?PREREG=chemin du préenregistrement scellé}"; PREREG_SHA256="${PREREG_SHA256:?}"\n'
     '  [ "$(sha256sum "$PREREG" | cut -d\' \' -f1)" = "$PREREG_SHA256" ] || refus "empreinte du préenregistrement ≠ PREREG_SHA256"\n'
     '  [ -f "$PREREG.sha256" ] && [ "$(cut -d\' \' -f1 < "$PREREG.sha256")" = "$PREREG_SHA256" ] || refus "compagnon .sha256 du préenregistrement absent ou différent"\n'
     '  grep -q "graine de la course $COURSE = $GRAINE\\b" "$PREREG" || refus "la graine $GRAINE de la course $COURSE n\'est pas écrite dans le préenregistrement scellé"\n'
     '  if grep -q "<<[A-Z0-9_]*>>" "$PREREG"; then refus "marqueurs <<…>> restants : préenregistrement non scellé"; fi\n'
     '  grep -q "$SHA_LANCEUR" "$PREREG" || refus "le préenregistrement ne cite pas l\'empreinte de ce lanceur"\n'
     '  E_TEXTE="$(grep -Eo \'entropie E = [0-9]+\' "$PREREG" | head -1 | grep -Eo \'[0-9]+$\' || true)"\n'
     '  [ -n "$E_TEXTE" ] || refus "entropie E absente du préenregistrement"\n',
     "# 2. Texte scellé (réel ; en simulation si TEXTE est donné) : un texte pour les deux courses ; la graine de cette course est\n"
     "#    recalculée depuis l'entropie (enfant INDICE_GRAINE) ; la ligne de l'autre course doit exister (elle n'est pas utilisée)\n"
     'if [ "$MODE" = reel ] || [ -n "${TEXTE:-}" ]; then\n'
     '  TEXTE="${TEXTE:?TEXTE=chemin du texte scellé}"; TEXTE_SHA256="${TEXTE_SHA256:?}"\n'
     '  [ "$(sha256sum "$TEXTE" | cut -d\' \' -f1)" = "$TEXTE_SHA256" ] || refus "empreinte du texte ≠ TEXTE_SHA256"\n'
     '  [ -f "$TEXTE.sha256" ] && [ "$(cut -d\' \' -f1 < "$TEXTE.sha256")" = "$TEXTE_SHA256" ] || refus "compagnon .sha256 du texte absent ou différent"\n'
     '  grep -q "graine de la course $COURSE = $GRAINE\\b" "$TEXTE" || refus "la graine $GRAINE de la course $COURSE n\'est pas écrite dans le texte scellé"\n'
     '  AUTRE_COURSE=audit; [ "$COURSE" = audit ] && AUTRE_COURSE=maieutique\n'
     '  grep -Eq "^ *graine de la course $AUTRE_COURSE = [0-9]+\\$" "$TEXTE" || refus "la ligne « graine de la course $AUTRE_COURSE = … » est absente du texte (un texte pour les deux courses ; cette ligne n\'est pas utilisée ici)"\n'
     '  if grep -q "<<[A-Z0-9_]*>>" "$TEXTE"; then refus "marqueurs <<…>> restants : texte non scellé"; fi\n'
     '  grep -q "$SHA_LANCEUR" "$TEXTE" || refus "le texte ne cite pas l\'empreinte de ce lanceur"\n'
     '  E_TEXTE="$(grep -Eo \'entropie E = [0-9]+\' "$TEXTE" | head -1 | grep -Eo \'[0-9]+$\' || true)"\n'
     '  [ -n "$E_TEXTE" ] || refus "entropie E absente du texte"\n', 1),
    ('  if [ "$COURSE" = v6-2-s ] && [ -n "${GRAINE_V62_MANIFESTE:-}" ]; then\n'
     '    grep -Eq "^ *graine de la course v6-2 = ${GRAINE_V62_MANIFESTE}\\$" "$PREREG" || refus "la course v6.2 a tourné avec la graine $GRAINE_V62_MANIFESTE, qui n\'est pas la graine v6-2 du préenregistrement scellé"\n'
     '    note "- course v6.2 précédente : graine $GRAINE_V62_MANIFESTE = graine v6-2 du préenregistrement"\n'
     "  fi\n"
     '  note "- préenregistrement : $PREREG, sha256 $PREREG_SHA256 (compagnon conforme), graine $GRAINE de la course $COURSE écrite et recalculée depuis l\'entropie du texte, empreinte du lanceur citée"\n',
     '  note "- texte : $TEXTE, sha256 $TEXTE_SHA256 (compagnon conforme), graine $GRAINE de la course $COURSE écrite et recalculée depuis l\'entropie du texte (enfant $INDICE_GRAINE), ligne de la course $AUTRE_COURSE présente (non utilisée), empreinte du lanceur citée"\n', 1),
    # étape 3 : question servie (question de base, puis annexes), vérifiée à chaque segment
    ("# 3. Organisme de la course (la v6.2.1 pour les deux courses, dossier organisme/ seul) et question (par course), extraits des commits cités, vérifiés\n",
     "# 3. Organisme de la course (la v6.2.1 pour les deux courses, dossier organisme/ seul) et question servie (la question de base, puis, pour la course « audit », ses annexes), extraits des commits cités, vérifiés\n", 1),
    ('if [ "$SEGMENT" = 1 ]; then git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" > "$PILOTE/question.md"; else [ -f "$PILOTE/question.md" ] || refus "SEGMENT=$SEGMENT : question du segment 1 absente de $PILOTE"; fi\n'
     '[ "$ART" = question ] && printf \'\\n\' >> "$PILOTE/question.md"\n'
     '[ "$(sha256sum "$PILOTE/question.md" | cut -d\' \' -f1)" = "$SHA_QUESTION" ] || refus "empreinte de la question ≠ ${SHA_QUESTION:0:8}…"\n'
     'note "- organisme : $N_FICHIERS_ORGANISME fichiers, empreinte d\'arbre $ARBRE_ORGANISME ; question ($COURSE) : sha256 $SHA_QUESTION"\n',
     "# question de base présente au commit cité et d'empreinte juste ; annexes servies : les emplacements de la course dont les trois\n"
     "# champs sont remplis, dans l'ordre (un emplacement à moitié rempli est un refus), chacune présente à son commit et d'empreinte\n"
     "# juste ; la question servie (question.md) est leur composé, écrit au segment 1 et revérifié à chaque segment (empreinte du\n"
     "# composé recalculée depuis le dépôt) ; elle doit tenir dans la borne du noyau (QUESTION_CARACTERES_MAX, vérifiée égale à\n"
     "# CARACTERES_MAX_QUESTION de question.py du code attendu : 100 000 caractères au noyau 9beee10b)\n"
     'git -C "$DEPOT" cat-file -e "$COMMIT_QUESTION:$CHEMIN_QUESTION" 2>/dev/null || refus "question ($CHEMIN_QUESTION) absente du commit ${COMMIT_QUESTION:0:8}…"\n'
     '[ "$(git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" | sha256sum | cut -d\' \' -f1)" = "$SHA_QUESTION" ] || refus "empreinte de la question ≠ ${SHA_QUESTION:0:8}…"\n'
     "AN_COMMITS=(); AN_CHEMINS=(); AN_SHAS=(); n_annexes=0\n"
     "for k in $ANNEXES; do\n"
     '  vc="ANNEXE_${k}_COMMIT"; vp="ANNEXE_${k}_CHEMIN"; vs="ANNEXE_${k}_SHA"; c="${!vc}"; p="${!vp}"; s="${!vs}"\n'
     '  if [ -z "$c$p$s" ]; then continue; fi\n'
     '  { [ -n "$c" ] && [ -n "$p" ] && [ -n "$s" ]; } || refus "annexe $k : champs incomplets (ANNEXE_${k}_COMMIT, ANNEXE_${k}_CHEMIN et ANNEXE_${k}_SHA vont ensemble)"\n'
     '  git -C "$DEPOT" cat-file -e "$c^{commit}" 2>/dev/null || refus "annexe $k : commit $c absent du dépôt (git fetch)"\n'
     '  git -C "$DEPOT" cat-file -e "$c:$p" 2>/dev/null || refus "annexe $k ($p) absente du commit ${c:0:8}…"\n'
     '  [ "$(git -C "$DEPOT" show "$c:$p" | sha256sum | cut -d\' \' -f1)" = "$s" ] || refus "empreinte de l\'annexe $k ($p) ≠ ${s:0:8}…"\n'
     '  n_annexes=$((n_annexes + 1)); AN_COMMITS+=("$c"); AN_CHEMINS+=("$p"); AN_SHAS+=("$s")\n'
     "done\n"
     "composer_question() {  # la question servie : la question de base, puis, pour chaque annexe servie (numérotée dans l'ordre), une ligne ---, un titre et son contenu\n"
     '  git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION"\n'
     "  local i\n"
     '  for ((i = 0; i < n_annexes; i++)); do printf \'\\n---\\n\\n# Annexe %d — %s (sha256 %s)\\n\\n\' "$((i + 1))" "${AN_CHEMINS[i]}" "${AN_SHAS[i]}"; git -C "$DEPOT" show "${AN_COMMITS[i]}:${AN_CHEMINS[i]}"; done\n'
     "}\n"
     'SHA_QUESTION_SERVIE="$(composer_question | sha256sum | cut -d\' \' -f1)"\n'
     'if [ "$SEGMENT" = 1 ]; then composer_question > "$PILOTE/question.md"; else [ -f "$PILOTE/question.md" ] || refus "SEGMENT=$SEGMENT : question du segment 1 absente de $PILOTE"; fi\n'
     '[ "$ART" = question ] && printf \'\\n\' >> "$PILOTE/question.md"\n'
     '[ "$(sha256sum "$PILOTE/question.md" | cut -d\' \' -f1)" = "$SHA_QUESTION_SERVIE" ] || refus "empreinte de la question servie ≠ ${SHA_QUESTION_SERVIE:0:8}… (question.md altéré, ou composé autrement qu\'au segment 1)"\n'
     'N_CARACTERES_QUESTION="$("$PY" -I -c \'import sys; print(len(open(sys.argv[1], encoding="utf-8").read()))\' "$PILOTE/question.md")"\n'
     'BORNE_NOYAU="$(cd "$R" && env -u PYTHONPATH "$PY" -B -I -c \'import sys; sys.path.insert(0, "."); from essaim_m3.noyau import question; print(question.CARACTERES_MAX_QUESTION)\' 2>/dev/null || echo illisible)"\n'
     '[ "$BORNE_NOYAU" = "$QUESTION_CARACTERES_MAX" ] || refus "QUESTION_CARACTERES_MAX=$QUESTION_CARACTERES_MAX ≠ CARACTERES_MAX_QUESTION du noyau ($BORNE_NOYAU, essaim_m3/noyau/question.py) : paramètre et noyau attendu vont ensemble"\n'
     '[ "$N_CARACTERES_QUESTION" -le "$QUESTION_CARACTERES_MAX" ] || refus "question servie de $N_CARACTERES_QUESTION caractères > $QUESTION_CARACTERES_MAX (borne du noyau ${NOYAU_COMMIT:0:8}, essaim_m3/noyau/question.py, CARACTERES_MAX_QUESTION) : le noyau la refuserait avant tout appel"\n'
     'note "- organisme : $N_FICHIERS_ORGANISME fichiers, empreinte d\'arbre $ARBRE_ORGANISME ; question ($COURSE) : sha256 $SHA_QUESTION (${CHEMIN_QUESTION##*/}, commit ${COMMIT_QUESTION:0:8}…) ; annexes servies : $n_annexes$(for ((i = 0; i < n_annexes; i++)); do printf \' ; annexe %d : %s %s %s\' "$((i + 1))" "${AN_CHEMINS[i]}" "${AN_COMMITS[i]}" "${AN_SHAS[i]}"; done)"\n'
     'note "- question servie : question.md, sha256 $SHA_QUESTION_SERVIE, $N_CARACTERES_QUESTION caractères"\n'
     '[ "$COURSE" = audit ] && [ "$n_annexes" = 0 ] && note "- RÉSERVE : course « audit » sans aucune annexe servie (l\'annexe 1, transcription expurgée du rapport, est-elle remplie ?)"\n', 1),
    # étape 4 : GO de la course, texte, sans la part « empreintes de la v6.2 »
    ("# 4. Registre des GO : une ligne « | GO-2026-10-25-02 | » qui porte « calcul »",
     "# 4. Registre des GO : une ligne « | $GO_ID | » (le GO de la course) qui porte « calcul »", 1),
    ('  t16="${PREREG_SHA256:-}"; t16="${t16:0:16}"\n', '  t16="${TEXTE_SHA256:-}"; t16="${t16:0:16}"\n', 1),
    ('  if [ -n "$EMP_V62" ]; then\n'
     '    echo "$dep" | grep "$NOM" | grep "$GO_ID" | grep -q "${EMP_V62:0:16}" || refus "la ligne de dépense de la course S ne porte pas l\'empreinte des empreintes de v6.2 (${EMP_V62:0:16}…), écrite après la fin de v6.2"\n'
     "  fi\n", "", 1),
    # étape 7 : le noyau dans son propre groupe de processus (setsid), PID et groupe consignés
    ('  env -i "${ENV_NOYAU[@]}" \\\n', '  setsid env -i "${ENV_NOYAU[@]}" \\\n', 2),
    ("PID=$!\n"
     'note "- PID de la course : $PID (arrêt humain par ce PID seulement, R10 ; STOP dans course/ : arrêt avant la ronde ou la génération suivante, celle en cours finit)"\n',
     "PID=$!\n"
     "groupe_de() { sed 's/^.*) //' \"/proc/$1/stat\" 2>/dev/null | cut -d' ' -f3 || true; }   # groupe de processus d'un PID (champ pgrp de /proc)\n"
     'for i in 1 2 3 4 5; do PGID_NOYAU="$(groupe_de "$PID")"; [ "$PGID_NOYAU" = "$PID" ] && break; sleep 0.2; done   # setsid a pris effet dès que le groupe est le PID\n'
     'note "- PID de la course : $PID (session et groupe de processus propres, par setsid : groupe ${PGID_NOYAU:-illisible} ; arrêt humain par ce PID seulement, R10, ou par la garde refus-question ; STOP dans course/ : arrêt avant la ronde ou la génération suivante, celle en cours finit)"\n', 1),
    # 7 bis : la garde « refus-question », lancée après le minuteur
    ('note "- minuteur : PID $MINUTEUR ; échéance $(date -u -d "@$(( DEBUT_LANCEUR_S + ECHEANCE_STOP_S ))" +%Y-%m-%dT%H:%M:%SZ), $ECHEANCE_STOP_S s après le départ du lanceur ($(date -u -d "@$DEBUT_LANCEUR_S" +%Y-%m-%dT%H:%M:%SZ))"\n'
     'set +e; wait "$PID"; CODE=$?; set -e\n'
     'kill "$MINUTEUR" 2>/dev/null || true\n'
     'wait "$MINUTEUR" 2>/dev/null || true\n',
     'note "- minuteur : PID $MINUTEUR ; échéance $(date -u -d "@$(( DEBUT_LANCEUR_S + ECHEANCE_STOP_S ))" +%Y-%m-%dT%H:%M:%SZ), $ECHEANCE_STOP_S s après le départ du lanceur ($(date -u -d "@$DEBUT_LANCEUR_S" +%Y-%m-%dT%H:%M:%SZ))"\n'
     "# 7 bis. Garde « refus-question » (texte v1, § Liste d'arrêt ; consigne gelée R-484 à R-487 : une question refusée n'est jamais\n"
     "#   reposée sous d'autres rôles) : veilleur de fond, lancé avec le noyau et arrêté par son PID à la fin de la course. Dès que la\n"
     "#   course est en cours (même critère que le minuteur), il lit toutes les 2 s le journal d'appels vivant de l'unité g001 (dossier\n"
     "#   du noyau de la génération, dans l'espace des organismes : <espace>/travail/<lignée>/g001.noyau/journal-appels.jsonl ;\n"
     "#   lignes complètes seulement ; champs id, rôle, statut, fin — jamais un texte). Un appel est « refusé » si son statut est REFUS\n"
     "#   ou si son champ `fin` porte une raison d'arrêt de sûreté (liste close des conventions du noyau : `statut_reponse` et\n"
     "#   REFUS_GEMINI de collisionneur_v2.py, 213b52ef…, chargé par essaim_m3/noyau/appels.py — les raisons qui valent REFUS).\n"
     "#   Règle (conv-audit, 26 octobre 2026, après le journal réel de g001 de la course M du pilote 4 : 120 appels de tâche\n"
     "#   `monoculture_analytique`, cinq en REFUS, avant la question, qui vient après l'appel `moissonneur_formulation_requetes`) :\n"
     "#   (a) un appel refusé de l'un des quatre rôles propres à la question ouverte de la v6.2.1 (ROLES_QUESTION_PROPRES) arrête\n"
     "#   toujours ; (b) un appel refusé du rôle qui sert aussi les tâches de la banque (ROLE_TACHES_ET_QUESTION) arrête seulement\n"
     "#   s'il vient après le premier appel de rôle PREFIXE_MOISSONNEUR* de g001, ou s'il est au-delà du APPELS_TACHES_MAX-ième appel\n"
     "#   de ce rôle en g001 (120 tâches servies, une caste par tâche sous les bornes du pilote 4 : le 121e est une caste de la\n"
     "#   question) ; sinon rien (refus de tâche) ; un refus sur un autre rôle ne fait rien. Alors il écrit le marqueur\n"
     "#   garde-refus-question-v1.json, tue le noyau (son groupe de processus, puis les sessions de ses enfants directs : organisme\n"
     "#   en bac à sable, entraîneur — par PID, R10), écrit la ligne « arrêt par la garde refus-question » au LANCEMENT.md (la règle\n"
     "#   qui a joué à la ligne suivante et dans la pièce) : la course est fermée sans reprise (étape 8a : liste fermée poussée avec\n"
     "#   ce qui existe ; le noyau tué n'écrit pas l'archive de g001, son journal vivant reste dans l'espace, archivé dans\n"
     "#   ferme.tar.gz, jamais lu ; si ferme.tar.gz n'est pas écrite, les copies ouvertes restent dans ce conteneur, non poussées,\n"
     "#   et la réserve « ARCHIVE FERMÉE INCOMPLÈTE » est consignée). En simulation, ESSAI_JOURNAL_GARDE remplace le journal lu\n"
     "#   (R5 : cas sain, motif réel de la course M, artefacts).\n"
     'ROLES_QUESTION_PROPRES="monoculture_croisee sonde_orthogonale_onsager critique_adversariale_limites arbitre_synthese_contradictoire"\n'
     'ROLE_TACHES_ET_QUESTION=monoculture_analytique\n'
     'PREFIXE_MOISSONNEUR=moissonneur_\n'
     'APPELS_TACHES_MAX=120\n'
     'FINS_SURETE="refusal SAFETY PROHIBITED_CONTENT BLOCKLIST SPII RECITATION IMAGE_SAFETY BLOCAGE_PROMPT"\n'
     'JOURNAL_GARDE="$ESPACE_ATTENDU/travail/$LIGNEE/g001.noyau/journal-appels.jsonl"; JOURNAL_GARDE_ESSAI=""\n'
     'if [ "$MODE" = simulation ] && [ -n "${ESSAI_JOURNAL_GARDE:-}" ]; then JOURNAL_GARDE="$ESSAI_JOURNAL_GARDE"; JOURNAL_GARDE_ESSAI=" (ESSAI : journal synthétique)"; fi\n'
     'MARQUEUR_GARDE="$DS/garde-refus-question-v1.json"\n'
     "tuer_noyau() {  # le noyau par son groupe (ou par son PID si le groupe n'est pas le sien), puis les sessions de ses enfants directs, par PID (R10) ; rend les PID des enfants\n"
     "  local enfants p i pg\n"
     '  enfants="$(pgrep -P "$PID" 2>/dev/null | tr \'\\n\' \' \' || true)"; pg="$(groupe_de "$PID")"\n'
     '  if [ "$pg" = "$PID" ]; then kill -TERM -- "-$PID" 2>/dev/null || true; else kill -TERM "$PID" 2>/dev/null || true; fi\n'
     '  for i in 1 2 3 4 5; do kill -0 "$PID" 2>/dev/null || break; sleep 1; done\n'
     '  if [ "$pg" = "$PID" ]; then kill -KILL -- "-$PID" 2>/dev/null || true; else kill -KILL "$PID" 2>/dev/null || true; fi\n'
     '  for p in $enfants; do kill -KILL -- "-$p" 2>/dev/null || true; kill -KILL "$p" 2>/dev/null || true; done\n'
     '  echo "$enfants"\n'
     "}\n"
     "garde_refus_question() {\n"
     "  local verdict s heure enfants ID ROLE STATUT FIN REGLE\n"
     "  trap 'exit 0' TERM\n"
     '  while kill -0 "$PID" 2>/dev/null; do\n'
     '    if course_en_cours && [ -f "$JOURNAL_GARDE" ]; then\n'
     '      verdict="$("$PY" -I -c \'\n'
     "import json, sys\n"
     "chemin, propres, role_taches, prefixe, taches_max, fins = sys.argv[1], set(sys.argv[2].split()), sys.argv[3], sys.argv[4], int(sys.argv[5]), set(sys.argv[6].split())\n"
     "try:\n"
     '    lignes = open(chemin, encoding="utf-8", errors="replace").read().split("\\n")[:-1]\n'
     "except OSError:\n"
     "    sys.exit(0)\n"
     "rang, moissonneur = 0, None   # rang de l appel parmi ceux du rôle des tâches ; id du premier appel moissonneur_*\n"
     "for l in lignes:\n"
     "    try:\n"
     "        e = json.loads(l)\n"
     "    except Exception:\n"
     "        continue\n"
     "    if not isinstance(e, dict):\n"
     "        continue\n"
     '    role = e.get("role") if isinstance(e.get("role"), str) else ""\n'
     "    if moissonneur is None and role.startswith(prefixe):\n"
     '        moissonneur = e.get("id")\n'
     "    if role == role_taches:\n"
     "        rang += 1\n"
     '    if not (e.get("statut") == "REFUS" or e.get("fin") in fins):\n'
     "        continue\n"
     "    if role in propres:\n"
     '        regle = "rôle propre à la question"\n'
     "    elif role == role_taches and moissonneur is not None:\n"
     '        regle = f"{role_taches} après le premier appel {prefixe}* de g001 ({moissonneur})"\n'
     "    elif role == role_taches and rang > taches_max:\n"
     '        regle = f"{role_taches} au rang {rang} > {taches_max} (au-delà des tâches servies)"\n'
     "    else:\n"
     "        continue\n"
     '    v = {k: e.get(k) for k in ("id", "role", "statut", "fin", "espece", "etape", "categorie", "debut_utc", "fin_utc", "sha256_prompt")}\n'
     '    v.update({"regle": regle, "rang_role_taches": rang if role == role_taches else None, "premier_moissonneur": moissonneur})\n'
     "    print(json.dumps(v, ensure_ascii=False, sort_keys=True))\n"
     "    break\n"
     '\' "$JOURNAL_GARDE" "$ROLES_QUESTION_PROPRES" "$ROLE_TACHES_ET_QUESTION" "$PREFIXE_MOISSONNEUR" "$APPELS_TACHES_MAX" "$FINS_SURETE" 2>/dev/null || true)"\n'
     '      if [ -n "$verdict" ]; then\n'
     "        trap '' TERM\n"
     '        heure="$(date -u +%Y-%m-%dT%H:%M:%SZ)"\n'
     '        { printf \'%s\\n\' "$verdict" > "$MARQUEUR_GARDE.tmp" && mv "$MARQUEUR_GARDE.tmp" "$MARQUEUR_GARDE"; } || true\n'
     '        enfants="$(tuer_noyau)"\n'
     '        read -r ID ROLE STATUT FIN <<< "$("$PY" -I -c \'import json, sys; e = json.loads(sys.argv[1]); print(e.get("id"), e.get("role"), e.get("statut"), e.get("fin"))\' "$verdict" 2>/dev/null || echo "? ? ? ?")"\n'
     '        REGLE="$("$PY" -I -c \'import json, sys; print(json.loads(sys.argv[1]).get("regle", "?"))\' "$verdict" 2>/dev/null || echo "?")"\n'
     '        "$PY" -I -c \'import json, sys; json.dump({"appel": json.loads(sys.argv[1]), "heure_utc": sys.argv[2], "journal": sys.argv[3], "pid_noyau": int(sys.argv[4]), "groupe_noyau": sys.argv[5], "pid_enfants_tues": [int(p) for p in sys.argv[6].split()], "regle": json.loads(sys.argv[1]).get("regle"), "roles_question_propres": sys.argv[7].split(), "role_taches_et_question": sys.argv[8], "prefixe_moissonneur": sys.argv[9], "appels_taches_max": int(sys.argv[10]), "fins_surete": sys.argv[11].split()}, open(sys.argv[12], "w", encoding="utf-8"), ensure_ascii=False, indent=1)\' "$verdict" "$heure" "$JOURNAL_GARDE" "$PID" "$PGID_NOYAU" "$enfants" "$ROLES_QUESTION_PROPRES" "$ROLE_TACHES_ET_QUESTION" "$PREFIXE_MOISSONNEUR" "$APPELS_TACHES_MAX" "$FINS_SURETE" "$MARQUEUR_GARDE" 2>/dev/null || true\n'
     '        note "- arrêt par la garde refus-question : appel $ID, rôle $ROLE, statut $STATUT, fin $FIN ($heure) ; course fermée sans reprise"\n'
     '        note "- garde refus-question : règle « $REGLE » ; noyau $PID (groupe ${PGID_NOYAU:-illisible}) tué, enfants directs tués par PID :${enfants:+ $enfants}${enfants:- aucun} ; pièce $(basename "$MARQUEUR_GARDE") (appel, règle, heure, PID)"\n'
     "        exit 0\n"
     "      fi\n"
     "    fi\n"
     "    sleep 2 & s=$!\n"
     '    wait "$s" || true\n'
     "  done\n"
     "}\n"
     "garde_refus_question & GARDE=$!\n"
     'note "- garde refus-question : veilleur PID $GARDE ; journal vivant de g001 : $JOURNAL_GARDE$JOURNAL_GARDE_ESSAI, lu toutes les 2 s dès que la course est en cours ; rôles propres à la question : $ROLES_QUESTION_PROPRES ; $ROLE_TACHES_ET_QUESTION : refus après le premier appel ${PREFIXE_MOISSONNEUR}* de g001 ou au-delà du ${APPELS_TACHES_MAX}e appel de ce rôle ; raisons d\'arrêt de sûreté : $FINS_SURETE"\n'
     'set +e; wait "$PID"; CODE=$?; set -e\n'
     'kill "$MINUTEUR" 2>/dev/null || true\n'
     'wait "$MINUTEUR" 2>/dev/null || true\n'
     'GARDE_ARRET=""\n'
     'if [ -f "$MARQUEUR_GARDE" ]; then wait "$GARDE" 2>/dev/null || true; GARDE_ARRET=1\n'
     'else kill "$GARDE" 2>/dev/null || true; wait "$GARDE" 2>/dev/null || true; note "- garde refus-question : aucun arrêt ; veilleur arrêté par son PID ($GARDE) à la fin de la course"; fi\n', 1),
    ('  CODE=""\n  cd "$R"   # v6 : l\'étape 8a lance l\'extrait mécanique depuis le dépôt',
     '  CODE=""; GARDE_ARRET=""\n  cd "$R"   # v6 : l\'étape 8a lance l\'extrait mécanique depuis le dépôt', 1),
    # fin de segment : jamais après un arrêt par la garde (course fermée sans reprise)
    ('if [ -z "$CLORE" ] && [ "$SEGMENT" != 1 ] && [ "$CODE" = 9 ]; then\n',
     'if [ -z "$CLORE" ] && [ -z "$GARDE_ARRET" ] && [ "$SEGMENT" != 1 ] && [ "$CODE" = 9 ]; then\n', 1),
    ('if [ -z "$CLORE" ] && [ -f "$PILOTE/course/manifeste-run.json" ] && [ "$CODE" = 0 ] && [ "$(compter_etats)" = "$((N_ETATS_AVANT + 1))" ]; then\n',
     'if [ -z "$CLORE" ] && [ -z "$GARDE_ARRET" ] && [ -f "$PILOTE/course/manifeste-run.json" ] && [ "$CODE" = 0 ] && [ "$(compter_etats)" = "$((N_ETATS_AVANT + 1))" ]; then\n', 1),
    # liste fermée : la pièce de la garde, avec son compagnon
    ('for f in sortie-erreur-extrait.txt sortie-erreur-tar.txt; do [ -f "$PILOTE/$f" ] && (cd "$PILOTE" && sha256sum "$f" > "$f.sha256"); done\n',
     'for f in sortie-erreur-extrait.txt sortie-erreur-tar.txt; do [ -f "$PILOTE/$f" ] && (cd "$PILOTE" && sha256sum "$f" > "$f.sha256"); done\n'
     'for f in "$PILOTE"/garde-refus-question-v1.json "$PILOTE"/segment-*-t*/garde-refus-question-v1.json; do if [ -f "$f" ]; then (cd "$(dirname "$f")" && sha256sum garde-refus-question-v1.json > garde-refus-question-v1.json.sha256); fi; done\n', 1),
    ("|question\\.md|registre-go\\.md|test-depense-[^/]+|organisme/.+|",
     "|question\\.md|registre-go\\.md|test-depense-[^/]+|garde-refus-question-v1\\.json(\\.sha256)?|organisme/.+|", 1),
    ("|segment-[0-9]+-t[0-9]+/(registre-go\\.md|test-depense-[^/]+|essais-v1\\.(xml|txt)|sortie-erreur-lanceur\\.txt(\\.sha256)?))$'",
     "|segment-[0-9]+-t[0-9]+/(registre-go\\.md|test-depense-[^/]+|essais-v1\\.(xml|txt)|sortie-erreur-lanceur\\.txt(\\.sha256)?|garde-refus-question-v1\\.json(\\.sha256)?))$'", 1),
    ('echo "pilote fini : $PILOTE — à pousser',
     'echo "pilote fini${GARDE_ARRET:+ (arrêt par la garde refus-question : course fermée sans reprise)} : $PILOTE — à pousser', 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
# porte « course v6.2 précédente » (bloc 0 bis de la v11) : retirée en bloc, l'empreinte du bloc vérifiée
blocs = list(re.finditer(r"# 0 bis \(avant l'étape 0, pour que ses refus en réel soient essayables\)\. Course S .*?\n  note \"- course v6\.2 précédente : \$SV ; \$issue_v62 ; lanceur attendu [^\n]*\nfi\n\n", t, re.S))
if len(blocs) != 1:
    sys.exit(f"refus : {len(blocs)} bloc(s) de la porte 0 bis au lieu de 1")
bloc = blocs[0].group(0)
if hashlib.sha256(bloc.encode("utf-8")).hexdigest() != SHA_BLOC_PORTE:
    sys.exit("refus : le bloc de la porte 0 bis n'a pas l'empreinte attendue (2ff1cfec…)")
t = t.replace(bloc, "# 0 bis (v11 : porte « course v6.2 précédente ») retiré en v12 : rien n'est exigé des courses du pilote 4 (texte v1,\n"
                    "#       table de correspondance) ; PRECEDENTE_V62 est sans effet\n\n")
for motif, permis in (("v6-2-s", 7), ("v5.3", 0), ("v5-3-v6", 3), ("pilote4-gemini-v6-2-s-v1", 1), ("pilote4-gemini-v6-2-v1", 0),
                      ("PRECEDENTE_V62", 3), ("LANCEUR_V62", 0), ("EMP_V62", 0), ("GRAINE_V62_MANIFESTE", 0), ("PREREG_SHA256", 0), ('"$PREREG"', 0), ("$PREREG.", 0),
                      ("PREREG_M", 7), ("TEXTE_SHA256", 8), ("GO-2026-10-25-02", 0), ("GO-2026-10-26-05", 3), ("GO-2026-10-26-04", 3),
                      ("GO_ID=", 4), ("GO_ID", 24),
                      ("course-maieutique-gemini-v6-2-v1", 2), ("course-audit-gemini-v6-2-v1", 2),
                      ("gemini-organisme-v6-2-maieutique", 2), ("gemini-organisme-v6-2-audit", 2),
                      ("eb03bad56ece1e755afa5e264948d0c44416f6cc", 1), ("9417652a", 0), ("ad23e9ae07588ed701a70b9b5f4bf379ca079953", 2), ("ad23e9ae", 4),
                      ("1d29fbecd52b1dfc94410e117f786811067f86f3cce24c4c54bbe424e480e3a3", 1), ("ec3abf28", 1), ("998960b8d101d5013c498d6fcf225277ba17d20741825ad136381892c05cfd0e", 1),
                      ("c1237687e98db14475336af690986bc08800a85e259d249de4940130245b1a64", 1), ("transcription-expurgee-v2.md", 1), ("question-audit-controle-organismes-v3.md", 1), ("question-audit-controle-organismes-v2.md", 1), ("annexe-vide", 1), ("remplir", 0),
                      ("dd2c1016", 1), ("2fd63bad", 0), ("29b32f62", 0), ("2204256d", 0), ("question-audit-controle-organismes-v1.md", 1),
                      ("ANNEXE_1_COMMIT", 10), ("ANNEXE_4_SHA=", 1), ("QUESTION_AUDIT_", 6), ("QUESTION_MAIEUTIQUE_", 6), ("ESSAI_ANNEXE_1_", 21),
                      ("n_annexes", 7), ("AN_CHEMINS", 5), ("20000", 0), ("20 000", 1), ("100000", 1), ("100 000", 3), ("CARACTERES_MAX_QUESTION", 6), ("QUESTION_CARACTERES_MAX", 8), ("BORNE_NOYAU", 3),
                      ("NOYAU_COMMIT", 11), ("NOYAU_EMPREINTE_PROPRE", 3), ("9beee10be4b66525a4ae98d69237abeb34ffbdac", 1), ("9beee10b", 4), ("192b21283292df14b3e21cd454cb34bc213e8e49a8867a99243d28d9a4abc7d7", 1),
                      ("8e5e2f7b", 2), ("61ddd638", 0), ("COMMIT_CODE", 6), ("CODE_NOYAU_PROPRE", 3),
                      ("a54da93e", 0), ("8b1c7511", 0), ("4772b525", 0), ("a15809b8", 0),
                      ("7ea32705c5437d91ed071dd95fb3209bb0b0035e", 2), ("4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d", 2),
                      ("ANNEXES", 3), ("SHA_QUESTION_SERVIE", 4), ("composer_question", 3), ("N_CARACTERES_QUESTION", 4),
                      ("ROLES_QUESTION", 5), ("ROLES_QUESTION_PROPRES", 5), ("ROLE_TACHES_ET_QUESTION", 5), ("PREFIXE_MOISSONNEUR", 5), ("APPELS_TACHES_MAX", 5), ("FINS_SURETE", 4),
                      ("regle", 8), ("REGLE", 3), ("rang_role_taches", 1), ("premier_moissonneur", 1), ("moissonneur", 12), ("JOURNAL_GARDE", 14), ("MARQUEUR_GARDE", 7), ("GARDE_ARRET", 6), ("garde_refus_question", 2),
                      ("tuer_noyau", 2), ("PGID_NOYAU", 5), ("groupe_de", 3), ("setsid", 4), ("ESSAI_JOURNAL_GARDE", 5), ("garde-refus-question-v1", 8),
                      ("lancer_courses_question_v12.sh", 1), ("deriver_lanceur_question_v12.py", 1), ("diff-lanceur-v11-vers-v12.txt", 1),
                      ("courses-question-gemini-v6-2-v", 4), ("sceller_courses_question_v6.py", 1), ("lancer_pilote4_gemini_v11.sh", 0)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()}")
