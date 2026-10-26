#!/usr/bin/env bash
# Lanceur des deux courses à question de la v6.2.1 (texte `courses-question-gemini-v6-2-v1.md`, ordre de Lazar, R-509) : « organisme assisté de Gemini, la v6.2.1, seule, sur la banque
# `confrontation-v3` (identifiants opaques), quatre générations notées, 6 rondes de conception au plus avant g000 (l'organisme déclare lui-même la fin de sa conception, `fin_conception.json`), 3 USD au plus par ronde, question de la course (« maieutique », ou « audit » avec son annexe) à g001 »,
# une course en un ou plusieurs segments (COURSE=maieutique, puis COURSE=audit ; SEGMENT=1, 2, …) — v12 : le lanceur v11
# (21854b79…) par `deriver_lanceur_question_v12.py` (deux courses à question du même organisme, hors du pilote 4 : clés
# `maieutique` et `audit`, noms `course-maieutique-gemini-v6-2-v1` et `course-audit-gemini-v6-2-v1`, lignées
# `gemini-organisme-v6-2-maieutique` et `gemini-organisme-v6-2-audit`, graines enfants 0 et 1 d'un même texte ; questions
# de `main` (« maieutique » à `eb03bad5`, « audit » v3 à `ad23e9ae`), la course « audit » servie avec son annexe (bloc de
# paramètres en tête : la transcription expurgée v2 du rapport consolidé, même commit) dans `question.md` ; GO par course, donné
# par session-depot (GO_ID) ; porte « course v6.2 précédente » retirée (rien n'est exigé des courses du pilote 4) ; les
# clés `v6-2` et `v6-2-s` refusées ; garde « refus-question » (veilleur de fond sur le journal d'appels vivant de g001 : au
# premier appel refusé d'un rôle propre à la question, ou de `monoculture_analytique` après le premier appel `moissonneur_*`
# de g001 ou au-delà de son 120e appel, le noyau est tué et la course fermée sans reprise) ; noyau attendu en paramètre
# (NOYAU_COMMIT 9beee10b : borne de la question 100 000 caractères) ; écart consigné dans `diff-lanceur-v11-vers-v12.txt`), la v11 dérivée du lanceur v10
# (0203f546…) par `deriver_lanceur_pilote4_v11.py` (seconde course : le même organisme, la v6.2.1, sur la question S, clé
# `v6-2-s`, nom `pilote4-gemini-v6-2-s-v1`, lignée `gemini-organisme-v6-2-s`, graine enfant 0 ; la question devient une
# constante par course ; en réel, ce lanceur refuse `v6-2` (la course M a tourné sous le lanceur v10, R-490) et la porte
# « course précédente » attend le lanceur v10 ; décision de Lazar du 26 octobre 2026, 04:13 UTC, R-492 ; écart consigné
# dans `diff-lanceur-pilote4-v10-vers-v11.txt`), la v10 dérivée du lanceur v9
# (6491c940…) par `deriver_lanceur_pilote4_v10.py` (objet de la course v6-2 : la v6.2.1, commit `7ea3270`, arbre
# `4f13647a…`, 26 fichiers — la v6.2 de Gemini corrigée par conv-audit, mot de Lazar du 26 octobre 2026, 00:27 Paris ;
# écart consigné dans `diff-lanceur-pilote4-v9-vers-v10.txt`), la v9 dérivée du lanceur v8
# (40685089…) par `deriver_lanceur_pilote4_v9.py` (ordre des courses inversé, décision de Lazar du 26 octobre 2026,
# 00:18 Paris, « je veux la v6.2 en premier » : la v6.2 d'abord, puis la seconde course après une v6.2 saine — porte « v6.2
# précédente », variable PRECEDENTE_V62 ; écart consigné dans `diff-lanceur-pilote4-v8-vers-v9.txt`), la v8 dérivée
# du lanceur v7 (cda96923…) par `deriver_lanceur_pilote4_v8.py` (objet de la seconde course : la v6.2 livrée par Gemini, commit
# `3bbb78c`, à la place de son premier commit `fedb065`, que le second, commité le 25 octobre 2026 à 22:57 UTC, remplace ;
# le lanceur v7 n'a jamais servi ; écart consigné dans `diff-lanceur-pilote4-v7-vers-v8.txt`), la v7 dérivée du lanceur v6
# (50f9c496…) par `deriver_lanceur_pilote4_v7.py` (objet de la seconde course : la v6.2 à la place de la v6.1, décision
# de Lazar du 25 octobre 2026, 23:54 Paris, « tout attendre la v6.2 »), la v6 dérivée du lanceur v5 (565f5205…) par `deriver_lanceur_pilote4_v6.py`
# (avec CLORE=1, l'extrait mécanique est lancé depuis le dépôt), la v5 dérivée du lanceur v4
# (f335440c…) par `deriver_lanceur_pilote4_v5.py` (reprise par segments du noyau 8e5e2f7b : une course arrêtée par le STOP
# du minuteur continue dans l'appel suivant ; archive fermée à la fin de la course ou sur CLORE=1 ; 75 USD par course ;
# minuteur à 3 400 s ; écart consigné dans `diff-lanceur-pilote4-v4-vers-v5.txt`), le v4 dérivé du v3 (73d318b9…) par
# `deriver_lanceur_pilote4_v4.py`, le v3 étant lui-même dérivé du lanceur v2 du pilote 3
# (`lancer_pilote3_gemini_v5_3_v6_v2.sh`, `add695a9…`) par `deriver_lanceur_pilote4_v3.py` (remplacements exacts ; écart
# consigné dans `diff-lanceur-pilote3-v2-vers-pilote4-v3.txt`). Ce qui change : les objets (v6.2 à la place de la v6) et
# les noms des courses ; la banque v3 (empreinte, chemin ; les chemins des banques v2 et v3 sont permis après le code) ;
# `--generations 4` ; les rondes de conception ; la porte « v6.2 précédente » (v9 ; dans l'ordre inverse jusqu'au v8 ; retirée en v12)
# attend les générations 0 à 3 ; la ligne de
# GO doit porter aussi les 16 premiers caractères de l'empreinte du texte scellé ; les journaux recopiés et poussés
# couvrent g000 à g003 et les rondes. Tout le reste (porte « M de référence » sur la course M du second pilote, gardes,
# environnement fermé, passerelle, essais du noyau, fermeture, liste fermée) est la ligne du lanceur v2.
# Objet des deux courses (« maieutique », puis « audit ») : la v6.2.1, dossier `organisme/` ; les clés du pilote 4 (`v6-2`, `v6-2-s`)
# sont refusées en réel comme en simulation (ses courses M et S sont finies et fermées, R-494, R-498).
# v6.2 = la v6.2.1 : branche `canal/conv-audit-organisme-v6-2-1`, commit `7ea3270`, arbre `4f13647a…`, 26 fichiers (la v6.2
# de Gemini, `3bbb78c`, corrigée par conv-audit : C-14 à C-17, `organisme/CORRECTIONS-v5.md`) ; lignées « assistées ».
# Les commits d'objets portent aussi l'arbre de la relève : seul `organisme/` en est extrait (`git archive <commit>
# organisme`) ; ils ne sont jamais extraits en entier ni empruntés comme arbre de travail.
# Texte : `essaim-m3-refonte-v1/prereg/courses-question-gemini-v6-2-v1.md` (ou la version qui le remplace et cite ce
# script) — un texte pour les deux courses, aux deux lignes « graine de la course maieutique = … » et « graine de la course
# audit = … » (enfants 0 et 1 de son entropie, `sceller_courses_question_v6.py`) ; pièces : `prereg/pieces-pilote4-gemini/`.
# Usage :
#   MODE=reel COURSE=maieutique GO_ID=GO-2026-10-26-05 DEPOT=… PYTHON=… TEXTE=… TEXTE_SHA256=… GRAINE=… RESTE_GO_USD=… \
#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=… CLE_ANTHROPIC=NOM CLE_GEMINI=NOM \
#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M du second pilote> [SEGMENT=1] \
#       bash lancer_courses_question_v12.sh
#   MODE=reel COURSE=audit GO_ID=GO-2026-10-26-04 … (même forme ; GO_ID est donné par session-depot, jamais fixé ici)
#   COURSE=v6-2 ou COURSE=v6-2-s (clés du pilote 4) : refusées, en réel comme en simulation ; PRECEDENTE_V62 : sans effet (porte retirée)
#   Reprise : la même commande (même COURSE, TENTATIVE, GRAINE, texte et références) avec SEGMENT=K, quand le LANCEMENT.md
#     dit « segment K−1 arrêté par STOP ; reprise attendue : SEGMENT=K » ; à chaque segment, un test de dépense frais
#     (APPEL_CONTROLE_FICHIER), une ligne de dépense nommant la course, le GO et « segment K », RESTE_GO_USD ≥ 75 USD moins
#     la dépense déjà faite par la course ; rien n'est committé dans la copie du dépôt entre deux segments (même HEAD)
#   Fermeture sans reprise (décision de Lazar) : SEGMENT=K CLORE=1 — aucun appel ; la course arrêtée est fermée et poussée
#     comme à sa fin
#   MODE=simulation : comme le lanceur v2 (variables d'essai inchangées ; en plus ESSAI_JOURNAL_GARDE=<journal synthétique lu par la garde refus-question> et
#     ESSAI_ANNEXE_1_COMMIT=… ESSAI_ANNEXE_1_CHEMIN=… ESSAI_ANNEXE_1_SHA=…, ensemble : une annexe synthétique à la place de l'annexe 1)
#
# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course (hors de son manifeste, de son état
# de reprise et, pour la garde refus-question, du journal d'appels vivant de g001 — rôle, statut, raison d'arrêt, jamais un
# texte —, mécaniques) ou la sortie standard ; arrêter un
# processus (R10 : PID consigné ; une course voisine est détectée, jamais arrêtée ; la garde refus-question tue le noyau de
# cette course et ses enfants par leurs PID, consignés) ; écraser un dossier (R12) ; lancer
# une seconde course de même nom (R3).
set -euo pipefail
set +x
DEBUT_LANCEUR_S="$(date +%s)"   # départ du lanceur : origine du minuteur (P4C1-02)
refus_tot() { echo "REFUS : $*" >&2; exit 2; }   # refus avant que le dossier du pilote existe

# ---- Paramètres des questions et des annexes (texte v1 ; R-509, R-510, R-515, R-516) : une ligne par champ, changer un
#      champ est le remplacement d'une ligne, vérifié par l'empreinte de ce lanceur. Annexes de la course « audit » : jusqu'à
#      quatre emplacements (ANNEXE_k_COMMIT, ANNEXE_k_CHEMIN, ANNEXE_k_SHA) ; un emplacement aux trois champs vides n'est pas
#      servi (les annexes servies sont numérotées dans l'ordre), un emplacement à moitié rempli est un refus ; l'annexe 1 est la
#      transcription expurgée v2 du rapport consolidé (session-depot, R-518 : `main` à ad23e9ae, même commit que la question v3).
#      La question servie (question, puis annexes) doit tenir dans la borne du noyau (QUESTION_CARACTERES_MAX ci-dessous,
#      égale à CARACTERES_MAX_QUESTION de essaim_m3/noyau/question.py au noyau attendu), vérifiée à l'étape (3). En simulation, ESSAI_ANNEXE_1_COMMIT,
#      ESSAI_ANNEXE_1_CHEMIN et ESSAI_ANNEXE_1_SHA (ensemble) remplacent l'annexe 1 (annexe synthétique de la batterie). ----
QUESTION_MAIEUTIQUE_COMMIT=eb03bad56ece1e755afa5e264948d0c44416f6cc
QUESTION_MAIEUTIQUE_CHEMIN=brouillons/questions-organismes-20261026-v1/question-hypotheses-maieutique-organismes-v1.md
QUESTION_MAIEUTIQUE_SHA=1d29fbecd52b1dfc94410e117f786811067f86f3cce24c4c54bbe424e480e3a3
QUESTION_AUDIT_COMMIT=ad23e9ae07588ed701a70b9b5f4bf379ca079953
QUESTION_AUDIT_CHEMIN=brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v3.md
QUESTION_AUDIT_SHA=998960b8d101d5013c498d6fcf225277ba17d20741825ad136381892c05cfd0e
ANNEXE_1_COMMIT=ad23e9ae07588ed701a70b9b5f4bf379ca079953
ANNEXE_1_CHEMIN=docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md
ANNEXE_1_SHA=c1237687e98db14475336af690986bc08800a85e259d249de4940130245b1a64
ANNEXE_2_COMMIT=
ANNEXE_2_CHEMIN=
ANNEXE_2_SHA=
ANNEXE_3_COMMIT=
ANNEXE_3_CHEMIN=
ANNEXE_3_SHA=
ANNEXE_4_COMMIT=
ANNEXE_4_CHEMIN=
ANNEXE_4_SHA=
# ---- Noyau attendu (décision de conv-audit du 26 octobre 2026) : le commit du code (essaim_m3, tests, collisionneur) auquel
#      HEAD de la copie doit être identique (lui-même ancêtre de HEAD, commits postérieurs limités aux chemins permis),
#      l'empreinte de l'arbre essaim_m3/noyau sans bytecode à ce commit, et la borne de la question servie à ce commit
#      (question.py, CARACTERES_MAX_QUESTION, vérifiée égale) : les trois lignes vont ensemble. 9beee10b = 8e5e2f7b plus la borne
#      portée de 20 000 à 100 000 caractères (seul changement du noyau ; tests du noyau passés chez conv-audit). ----
NOYAU_COMMIT=9beee10be4b66525a4ae98d69237abeb34ffbdac
NOYAU_EMPREINTE_PROPRE=192b21283292df14b3e21cd454cb34bc213e8e49a8867a99243d28d9a4abc7d7
QUESTION_CARACTERES_MAX=100000
# ---- fin des paramètres ----

MODE="${MODE:?MODE=reel ou MODE=simulation}"
[ "$MODE" = reel ] || [ "$MODE" = simulation ] || refus_tot "MODE inconnu : $MODE"
COURSE="${COURSE:?COURSE=maieutique ou COURSE=audit}"
GO_ID="${GO_ID:?GO_ID=identifiant du GO de la course, donné par session-depot (GO-2026-10-26-05 pour maieutique, GO-2026-10-26-04 pour audit) : le lanceur ne le fixe pas}"
[[ "$GO_ID" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || refus_tot "GO_ID doit être de la forme GO-AAAA-MM-JJ-NN : « $GO_ID »"
# Reprise par segments (décision de Lazar, 25 octobre 2026, 20:23 Paris) : SEGMENT=1 fait partir la course ; SEGMENT=K ≥ 2
#   continue la course arrêtée au segment K − 1 par le STOP du minuteur ; CLORE=1 (avec SEGMENT ≥ 2) la ferme sans reprise
SEGMENT="${SEGMENT:-1}"
case "$SEGMENT" in ''|*[!0-9]*|0*) refus_tot "SEGMENT doit être un entier ≥ 1, sans zéro en tête : « $SEGMENT »";; esac
CLORE="${CLORE:-}"
case "$CLORE" in ''|1) ;; *) refus_tot "CLORE vaut 1 ou rien : « $CLORE »";; esac
if [ -n "$CLORE" ] && [ "$SEGMENT" = 1 ]; then refus_tot "CLORE=1 ferme une course arrêtée entre deux segments : SEGMENT ≥ 2 exigé"; fi
# Question par course (v12, R-509, R-510, R-515, R-516) : « maieutique » et « audit » (bloc de paramètres en tête) ; même
#   organisme, la v6.2.1, pour les deux courses ; la course « audit » est servie avec les annexes remplies du bloc de
#   paramètres (emplacements 1 à 4), composées dans question.md à l'étape (3) ; les clés du pilote 4 sont refusées
case "$COURSE" in
  maieutique)
    NOM="course-maieutique-gemini-v6-2-v1"; INDICE_GRAINE=0
    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e
    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d
    N_FICHIERS_ORGANISME=26
    LIGNEE="gemini-organisme-v6-2-maieutique"
    COMMIT_QUESTION="$QUESTION_MAIEUTIQUE_COMMIT"; CHEMIN_QUESTION="$QUESTION_MAIEUTIQUE_CHEMIN"; SHA_QUESTION="$QUESTION_MAIEUTIQUE_SHA"
    ANNEXES="";;
  audit)
    NOM="course-audit-gemini-v6-2-v1"; INDICE_GRAINE=1
    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e
    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d
    N_FICHIERS_ORGANISME=26
    LIGNEE="gemini-organisme-v6-2-audit"
    COMMIT_QUESTION="$QUESTION_AUDIT_COMMIT"; CHEMIN_QUESTION="$QUESTION_AUDIT_CHEMIN"; SHA_QUESTION="$QUESTION_AUDIT_SHA"
    ANNEXES="1 2 3 4";;
  v6-2|v6-2-s) refus_tot "COURSE=$COURSE : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)";;
  *) refus_tot "COURSE inconnue : $COURSE (maieutique ou audit)";;
esac
# simulation : annexe 1 synthétique (R5, batterie) — les trois variables vont ensemble ; interdites en réel (liste des variables d'essai)
if [ "$MODE" = simulation ] && { [ -n "${ESSAI_ANNEXE_1_COMMIT:-}" ] || [ -n "${ESSAI_ANNEXE_1_CHEMIN:-}" ] || [ -n "${ESSAI_ANNEXE_1_SHA:-}" ]; }; then
  { [ -n "${ESSAI_ANNEXE_1_COMMIT:-}" ] && [ -n "${ESSAI_ANNEXE_1_CHEMIN:-}" ] && [ -n "${ESSAI_ANNEXE_1_SHA:-}" ]; } || refus_tot "ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN et ESSAI_ANNEXE_1_SHA vont ensemble"
  ANNEXE_1_COMMIT="$ESSAI_ANNEXE_1_COMMIT"; ANNEXE_1_CHEMIN="$ESSAI_ANNEXE_1_CHEMIN"; ANNEXE_1_SHA="$ESSAI_ANNEXE_1_SHA"
fi
PY="${PYTHON:-python3}"
ART="${ESSAI_ARTEFACT:-}"
SOURCE_GEMINI=""
SOURCE_ANTHROPIC=""
SOURCE_BRAVE=""
SOURCE_OPENALEX=""
SOURCE_S2=""
if [ "$MODE" = reel ]; then
  for v in PILOTE_RACINE SUFFIXE_ESSAI REGISTRE_GO_SOURCE DEPENSES_SOURCE ESSAI_ARTEFACT ESSAI_JUNIT_EXISTANT ESSAI_RESUME_EXISTANT ESSAI_EXIGER_HEURE ESSAI_PASSERELLE_PY ESSAIM_M3_ESPACE ESSAI_ECHEANCE_STOP_S ESSAI_JOURNAL_GARDE ESSAI_ANNEXE_1_COMMIT ESSAI_ANNEXE_1_CHEMIN ESSAI_ANNEXE_1_SHA; do
    [ -z "${!v:-}" ] || refus_tot "variable $v définie en mode réel (variable d'essai, ou espace des organismes déplacé)"
  done
  [ "$(id -u)" = 0 ] || refus_tot "le mode réel exige root (essais et course)"
  # P52C1-05 : clés des runs seulement (GO-2026-10-24-04 et R-411), toujours nommées
  NOMS_ANTHROPIC="RR_ANTHROPIC_API_KEY RR_ANTHROPIC_API_KEY_2 RR_ANTHROPIC_API_KEY_3 RR_ANTHROPIC_API_KEY_LUC"
  NOMS_GEMINI="GEMINI_API_KEY_2 GEMINI_API_KEY"
  [ -n "${CLE_ANTHROPIC:-}" ] || refus_tot "CLE_ANTHROPIC non défini : nom de la clé Anthropic des runs, parmi $NOMS_ANTHROPIC (GO-2026-10-24-04, R-411)"
  SOURCE_ANTHROPIC="$CLE_ANTHROPIC"
  [[ " $NOMS_ANTHROPIC " == *" $SOURCE_ANTHROPIC "* ]] || refus_tot "CLE_ANTHROPIC=$SOURCE_ANTHROPIC hors des clés des runs ($NOMS_ANTHROPIC)"
  [ -n "${!SOURCE_ANTHROPIC:-}" ] || refus_tot "clé Anthropic absente (variable $SOURCE_ANTHROPIC)"
  [ -n "${CLE_GEMINI:-}" ] || refus_tot "CLE_GEMINI non défini : nom de la clé Gemini des runs, parmi $NOMS_GEMINI (GO-2026-10-24-04, R-411)"
  SOURCE_GEMINI="$CLE_GEMINI"
  [[ " $NOMS_GEMINI " == *" $SOURCE_GEMINI "* ]] || refus_tot "CLE_GEMINI=$SOURCE_GEMINI hors des clés des runs ($NOMS_GEMINI)"
  [ -n "${!SOURCE_GEMINI:-}" ] || refus_tot "clé Gemini absente (variable $SOURCE_GEMINI)"
  SOURCE_BRAVE="${CLE_BRAVE:-BRAVE_API_KEY}"
  [[ "$SOURCE_BRAVE" =~ ^[A-Z][A-Z0-9_]*$ ]] || refus_tot "CLE_BRAVE doit être un nom de variable (lettres capitales, chiffres, _)"
  [ -n "${!SOURCE_BRAVE:-}" ] || refus_tot "clé Brave absente (variable $SOURCE_BRAVE) : la source « web » est servie à ce pilote"
  SOURCE_OPENALEX="${CLE_OPENALEX:-OPENALEX_API_KEY}"
  [[ "$SOURCE_OPENALEX" =~ ^[A-Z][A-Z0-9_]*$ ]] || refus_tot "CLE_OPENALEX doit être un nom de variable (lettres capitales, chiffres, _)"
  [ -n "${!SOURCE_OPENALEX:-}" ] || refus_tot "clé OpenAlex absente (variable $SOURCE_OPENALEX) : exigée (décision de Lazar, 12:11 Paris : clés avant le pilote)"
  SOURCE_S2="${CLE_S2:-SEMANTIC_SCHOLAR_API_KEY}"
  [[ "$SOURCE_S2" =~ ^[A-Z][A-Z0-9_]*$ ]] || refus_tot "CLE_S2 doit être un nom de variable (lettres capitales, chiffres, _)"
  [ -n "${!SOURCE_S2:-}" ] || refus_tot "clé Semantic Scholar absente (variable $SOURCE_S2) : exigée (Lazar, 12:24 Paris : les deux clés entrent dans le pilote)"
  [ -n "${RECHARGE_ATTESTEE:-}" ] || refus_tot "RECHARGE_ATTESTEE vide : l'attestation de Lazar (recharge automatique active, avec l'heure) est exigée"
fi
DECALAGE_UID=900
DECALAGES_DES_ESSAIS="0 700 800"   # les essais du noyau font tourner des processus aux décalages 0, 700, 800–830 et 900 (P2C1-06, P2C2-04)
# GO_ID : lu en tête (un GO par course, donné par session-depot) ; bornes du pilote 4 (texte v1, table de correspondance)
USD_GEN=30      # par génération (mêmes bornes que la course M ; décision (b) de Lazar, 25 octobre 10:17 Paris)
USD_COURSE=75   # par course, tous segments compris (plafond total du noyau) ; chaque course sur son GO (GO-2026-10-26-05 ; GO-2026-10-26-04 partie (2) — mot direct de Lazar, R-509 ; la ligne d'extension est écrite par session-depot)
# P4C1-02 et reprise par segments : minuteur. STOP posé dans course/ à ECHEANCE_STOP_S s du départ du lanceur si la course
#   tourne encore ; le noyau finit l'unité en cours (ronde de conception ou génération), écrit son état de reprise et
#   s'arrête ; le segment suivant continue. 3 400 s + la plus longue unité possible (2 400 s de génération + 900 s
#   d'attente des appels en vol, ATTENTE_FILS_S, + 60 s de dépôt) + 300 s de fermeture = 7 060 s, sous les 7 200 s de la
#   commande de fond de session-depot ; fixe en réel ; réglable en simulation (ESSAI_ECHEANCE_STOP_S)
ECHEANCE_STOP_S=3400
if [ "$MODE" = simulation ] && [ -n "${ESSAI_ECHEANCE_STOP_S:-}" ]; then
  case "$ESSAI_ECHEANCE_STOP_S" in *[!0-9]*) refus_tot "ESSAI_ECHEANCE_STOP_S doit être un entier (secondes)";; esac
  ECHEANCE_STOP_S="$ESSAI_ECHEANCE_STOP_S"
fi
AGE_MAX_TEST_DEPENSE=900

# Courses voisines : une course au décalage 900 → refus ; aux décalages des essais (0, 800) → réserve consignée ; autres
# → consignées (détection seulement, aucun arrêt). Une course sans --decalage-uid est au décalage 0 (défaut du noyau).
decalage_de() { local l="$1" d; d="$(echo "$l" | grep -Eo -- '--decalage-uid[= ][0-9]+' | grep -Eo '[0-9]+$' | tail -1)"; echo "${d:-0}"; }
voisines=""; reserve_voisines=""
detecter_voisines() {
  voisines=""; reserve_voisines=""
  local pid ligne d
  for pid in $(pgrep -f 'essaim_m3 (lancer|simuler)' || true); do
    ligne="$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null || true)"
    [ -n "$ligne" ] || continue
    d="$(decalage_de "$ligne")"
    if [ "$d" = "$DECALAGE_UID" ]; then return 1; fi
    voisines="$voisines $pid(décalage $d)"
    for e in $DECALAGES_DES_ESSAIS; do [ "$d" = "$e" ] && reserve_voisines="$reserve_voisines $pid(décalage $d)"; done
  done
  return 0
}
detecter_voisines || refus_tot "une course du noyau tourne déjà au décalage d'utilisateurs $DECALAGE_UID : le pilote attend"

DEPOT="$(cd "${DEPOT:?DEPOT=racine du dépôt}" && pwd -P)"
if [ "$MODE" = reel ]; then
  case "$DEPOT/" in /root/*|/home/*) ;; *) refus_tot "dépôt $DEPOT hors de /root et de /home : il ne serait pas caché aux organismes d'une course voisine (P2C1-06)";; esac
fi
R="$DEPOT/essaim-m3-refonte-v1"
GRAINE="${GRAINE:?GRAINE=graine de la course, écrite dans le préenregistrement scellé}"
RACINE_PILOTES="${PILOTE_RACINE:-$R/pilotes}"
TENTATIVE="${TENTATIVE:-1}"
case "$TENTATIVE" in ''|*[!0-9]*) refus_tot "TENTATIVE doit être un entier";; esac
if [ "$TENTATIVE" = 1 ]; then PILOTE="$RACINE_PILOTES/$NOM${SUFFIXE_ESSAI:-}"; else PILOTE="$RACINE_PILOTES/$NOM-tentative$TENTATIVE${SUFFIXE_ESSAI:-}"; fi

COMMIT_CODE="$NOYAU_COMMIT"   # paramètre en tête (noyau attendu)
COMMIT_LIENS=4967734a62a0b10c3b5cd6360e21924f015053fd
COMMIT_CREDIT=90595ffb53b30c65c66be807215a998998b701fc
[ "$ART" = commit ] && COMMIT_QUESTION=0123456789abcdef0123456789abcdef01234567
[ "$ART" = question-base ] && SHA_QUESTION=0000000000000000000000000000000000000000000000000000000000000000
[ "$ART" = question-v1 ] && CHEMIN_QUESTION=brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v1.md   # la v1 (dd2c1016…) ne sert plus : empreinte autre
[ "$ART" = question-v2 ] && CHEMIN_QUESTION=brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v2.md   # la v2 (ec3abf28…) ne sert plus : empreinte autre
[ "$ART" = annexe ] && ANNEXE_1_SHA=0000000000000000000000000000000000000000000000000000000000000000
[ "$ART" = annexe-absente ] && ANNEXE_1_CHEMIN=docs/nulle-part-v1.md
[ "$ART" = annexe-vide ] && ANNEXE_1_COMMIT= && ANNEXE_1_CHEMIN= && ANNEXE_1_SHA=   # emplacement 1 vidé : course « audit » sans annexe (RÉSERVE)
SHA_BANQUE=157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d
SHA_MISSION=bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e
SHA_COLLISIONNEUR=213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
[ "$ART" = banque ] && SHA_BANQUE=0000
[ "$ART" = mission ] && SHA_MISSION=0000
CODE_NOYAU_PROPRE="$NOYAU_EMPREINTE_PROPRE"   # paramètre en tête (noyau attendu)
N_ESSAIS=169
ESSAIS_CITES="test_fichiers_lecture_et_copie_sans_lien test_depot_ne_suit_aucun_lien_de_l_organisme test_organisme_poseur_de_liens_ne_voit_rien_du_noyau test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score test_extrait_mecanique_sain_puis_artefacts test_mode_reel_refuse_sans_go test_mode_reel_refuse_anthropic_base_url test_bac_a_sable_isolation_reseau_refusee_si_indisponible test_appels_paralleles_plafond_tenu_au_pire_cas test_organisme_gourmand_recoit_plafond_sans_exception test_ce312_doit_arreter_et_raison_juste test_bac_a_sable_exception_et_delai test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee test_ce305_credit_epuise_arrete_la_course test_ce307_anomalie_journal_absent test_relance_puis_reprise_remet_le_compteur_a_zero test_fichier_stop_arrete_la_boucle test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus test_r395_credit_epuise_rendu_en_400_arrete_la_course test_cl5_01_banque_cachee_a_l_organisme test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course test_sources_reelles_de_moisson_si_reseau test_moisson_de_bout_en_bout_en_simulation test_ce311_garde_de_temps_compte_la_moisson test_ce305_sources_moisson_au_manifeste_et_bras_apparie test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait test_r410_cles_openalex_et_s2_en_entete_jamais_dans_l_adresse test_course_continue_de_reference test_stop_en_conception_aucune_generation_notee_avant_la_reprise test_conception_arretee_jamais_suivie_de_generations_dans_le_meme_segment test_stop_pendant_la_derniere_unite_n_appelle_pas_de_segment test_stop_pose_pendant_une_unite_ne_l_interrompt_pas test_reprise_acceptee_puis_jamais_deux_fois_le_meme_etat test_reprise_refusee_sans_etat_et_sur_noyau_amorce test_reprise_refusee_stop_present test_reprise_refusee_etat_altere test_reprise_refusee_course_qui_a_bouge test_reprise_accepte_d_autres_chemins_pour_les_memes_pieces test_cli_simuler_reprendre_et_refus test_refus_reprise_des_arguments test_lancer_refuse_course_existante_sans_reprendre test_ronde_interrompue_continuee_sans_rejouer_ni_sauter[False] test_ronde_interrompue_continuee_sans_rejouer_ni_sauter[True]"
# Chemins que les commits postérieurs au noyau attendu (NOYAU_COMMIT) peuvent toucher : le texte du second pilote, ses pièces et ses
# contre-lectures ; les textes du pilote 4, leurs pièces et leurs contre-lectures ; le texte des courses à question et ses
# contre-lectures (ses pièces sont sous pieces-pilote4-gemini/) ; dossier des pilotes
PERMIS_APRES_CODE='^essaim-m3-refonte-v1/(prereg/(pilote2-gemini-organisme-v5-2-v[0-9]+\.md(\.sha256)?|pieces-pilote2-gemini-v5-2/.+|contre-lectures/pilote2-gemini-organisme-v5-2-v[0-9]+-cl[0-9]+\.md(\.sha256)?|pilote3-gemini-organisme-v5-3-v6-v[0-9]+\.md(\.sha256)?|pieces-pilote3-gemini-v5-3-v6/.+|contre-lectures/pilote3-gemini-organisme-v5-3-v6-v[0-9]+-cl[0-9]+\.md(\.sha256)?|pilote4-gemini-organisme-v[0-9]+\.md(\.sha256)?|courses-question-gemini-v6-2-v[0-9]+\.md(\.sha256)?|pieces-pilote4-gemini/.+|contre-lectures/pilote4-gemini-organisme-v[0-9]+-cl[0-9]+\.md(\.sha256)?|contre-lectures/courses-question-gemini-v6-2-v[0-9]+-cl[0-9]+\.md(\.sha256)?)|banque/(banque-confrontation-v2(-secret)?\.json(\.sha256)?|LISEZMOI-v4\.md(\.sha256)?|EMPREINTES-banque-v2-v1\.txt(\.sha256)?|construction-v2/.+|banque-confrontation-v3(-secret|-cle)?\.json(\.sha256)?|LISEZMOI-v[56]\.md(\.sha256)?|EMPREINTES-banque-v3-v[12]\.txt(\.sha256)?|construction-v3/.+|contre-lectures/.+))$'

# R3 : une course est partie dès que son manifeste est écrit ; aucune seconde course de ce nom, quel que soit le dossier,
#     la copie du dépôt (marqueur de départ du conteneur, branche poussée) ou le moment (verrou ; P2C2-06)
if [ "$MODE" = reel ]; then MARQUEURS=/var/lib/essaim-m3/pilotes-partis; else MARQUEURS="$RACINE_PILOTES/.partis"; fi
VERROU="$RACINE_PILOTES/.verrou-$NOM"
course_deja_partie() {
  local d
  for d in "$RACINE_PILOTES/$NOM"*; do
    [ -d "$d" ] || continue
    if [ -f "$d/course/manifeste-run.json" ] || [ -f "$d/ferme.tar.gz" ]; then echo "une course est déjà partie dans $d"; return 0; fi
  done
  [ -e "$MARQUEURS/$NOM" ] && { echo "marqueur de départ $MARQUEURS/$NOM présent"; return 0; }
  return 1
}
if [ "$SEGMENT" = 1 ]; then
  if raison_r3="$(course_deja_partie)"; then refus_tot "$raison_r3 (R3 : jamais de seconde course)"; fi
fi
if [ "$MODE" = reel ]; then  # rien n'est poussé avant la fermeture de la course, quel que soit le segment
  distante="$(git -C "$DEPOT" ls-remote --heads origin "pilotes/$NOM" 2>/dev/null)" || refus_tot "lecture du dépôt distant impossible (git ls-remote) : R3 non vérifiable, le pilote attend"
  [ -z "$distante" ] || refus_tot "la branche pilotes/$NOM existe déjà sur le dépôt distant (R3)"
fi
L="$PILOTE/LANCEMENT.md"
SHA_LANCEUR="$(sha256sum "$0" | cut -d' ' -f1)"
if [ "$SEGMENT" = 1 ]; then
  [ -e "$PILOTE" ] && refus_tot "$PILOTE existe déjà (R12 ; après un refus avant le manifeste : TENTATIVE=$((TENTATIVE + 1)))"
  mkdir -p "$RACINE_PILOTES"
  mkdir "$VERROU" 2>/dev/null || refus_tot "verrou $VERROU présent : un autre lanceur de cette course tourne, ou un lanceur s'est interrompu (examiner, puis retirer le verrou à la main)"
  mkdir -m 700 "$PILOTE"
  mkdir -m 700 "$PILOTE/ferme"
  printf 'course/\nferme/\n' > "$PILOTE/.gitignore"   # jamais ajoutés au dépôt, même par un `git add -A`
  VERROU_ACTIF="$VERROU"; DS="$PILOTE"; SUFFIXE_SEG=""
else
  # Reprise : la course de ce pilote (même TENTATIVE), partie au segment 1, arrêtée par le STOP du minuteur au segment
  # précédent, ni fermée ni poussée ; même lanceur, même HEAD ; un seul lanceur par segment (verrou du segment)
  { [ -d "$PILOTE" ] && [ -f "$L" ]; } || refus_tot "SEGMENT=$SEGMENT : $PILOTE ou son LANCEMENT.md absent (aucune course à reprendre ; même TENTATIVE qu'au segment 1)"
  if [ -e "$PILOTE/ferme.tar.gz" ]; then refus_tot "SEGMENT=$SEGMENT : la course de $PILOTE est déjà fermée"; fi
  [ -f "$PILOTE/course/manifeste-run.json" ] || refus_tot "SEGMENT=$SEGMENT : aucune course partie dans $PILOTE"
  [ -d "$VERROU" ] || refus_tot "SEGMENT=$SEGMENT : verrou $VERROU du segment 1 absent"
  { [ -f "$MARQUEURS/$NOM" ] && [ "$(cut -d' ' -f1 < "$MARQUEURS/$NOM")" = "$PILOTE" ]; } || refus_tot "SEGMENT=$SEGMENT : marqueur de départ $MARQUEURS/$NOM absent ou d'un autre dossier (R3)"
  for d in "$RACINE_PILOTES/$NOM"*; do
    if [ -d "$d" ] && [ "$d" != "$PILOTE" ] && { [ -f "$d/course/manifeste-run.json" ] || [ -f "$d/ferme.tar.gz" ]; }; then refus_tot "SEGMENT=$SEGMENT : une autre course de ce nom est partie dans $d (R3)"; fi
  done
  derniere_fin="$(grep -E '^- segment [0-9]+ arrêté par STOP ; reprise attendue : SEGMENT=[0-9]+$' "$L" | tail -1 || true)"
  [ "$derniere_fin" = "- segment $((SEGMENT - 1)) arrêté par STOP ; reprise attendue : SEGMENT=$SEGMENT" ] || refus_tot "SEGMENT=$SEGMENT : le LANCEMENT.md n'attend pas ce segment (dernière fin de segment : « ${derniere_fin:-aucune} »)"
  grep -Fxq -- "- lanceur : $(basename "$0"), sha256 $SHA_LANCEUR" "$L" || refus_tot "SEGMENT=$SEGMENT : ce lanceur ($(basename "$0"), ${SHA_LANCEUR:0:8}…) n'est pas celui du segment 1"
  head1="$(grep -E '^- dépôt : .* ; HEAD : [0-9a-f]{40} ' "$L" | head -1 | grep -Eo 'HEAD : [0-9a-f]{40}' | cut -c8- || true)"
  [ "$head1" = "$(git -C "$DEPOT" rev-parse HEAD)" ] || refus_tot "SEGMENT=$SEGMENT : HEAD du dépôt ≠ celui du segment 1 (${head1:-illisible}) : le noyau refuserait la reprise ; rien n'est committé dans cette copie entre deux segments"
  VERROU_ACTIF="$VERROU-segment$SEGMENT"
  mkdir "$VERROU_ACTIF" 2>/dev/null || refus_tot "verrou $VERROU_ACTIF présent : un autre lanceur de ce segment tourne, ou un lanceur s'est interrompu (examiner, puis retirer le verrou à la main)"
  essai_seg=1; while [ -e "$PILOTE/segment-$SEGMENT-t$essai_seg" ]; do essai_seg=$((essai_seg + 1)); done
  DS="$PILOTE/segment-$SEGMENT-t$essai_seg"; SUFFIXE_SEG="-segment-$SEGMENT-t$essai_seg"
  mkdir -m 700 "$DS"
fi
refus() { echo "REFUS : $*" >&2; echo "- refus : $* ($(date -u +%Y-%m-%dT%H:%M:%SZ)) ; verrou $VERROU_ACTIF retiré" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256); rmdir "$VERROU_ACTIF" 2>/dev/null || true; exit 2; }
note() { echo "$*" >> "$L"; }
trap 'c=$?; echo "ÉCHEC inattendu (code $c) à la ligne $LINENO : arrêt" >&2; echo "- échec inattendu (code $c) à la ligne $LINENO ($(date -u +%Y-%m-%dT%H:%M:%SZ)) ; verrou $VERROU_ACTIF laissé (à examiner)" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256) || true' ERR
if [ "$MODE" = reel ]; then SOURCE_REG="origin/main"; else SOURCE_REG="${REGISTRE_GO_SOURCE:-aucune (simulation)} ; dépenses : ${DEPENSES_SOURCE:-aucune (simulation)}"; fi
{
  if [ "$SEGMENT" = 1 ]; then
    echo "# Lancement du pilote $NOM ($MODE, tentative $TENTATIVE)"
  else
    echo
    echo "## Segment $SEGMENT, essai $essai_seg ($MODE, tentative $TENTATIVE)$(if [ -n "$CLORE" ]; then echo " — fermeture sans reprise (CLORE=1)"; fi)"
  fi
  echo
  echo "- début (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; hôte : $(hostname) ; utilisateur : $(id -u)"
  echo "- course : $COURSE ; dossier du pilote : $PILOTE (0700, à root)$(if [ "$SEGMENT" != 1 ]; then echo " ; pièces de ce segment : $(basename "$DS")/"; fi)"
  if [ "$SEGMENT" = 1 ]; then echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD) (c'est le « commit » que le manifeste consignera)"
  else echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD) (celui du segment 1, que le manifeste consigne)"; fi
  echo "- lanceur : $(basename "$0"), sha256 $SHA_LANCEUR"
  echo "- source des registres : $SOURCE_REG"
  if [ -n "$voisines" ]; then echo "- course(s) voisine(s) du noyau détectée(s) dans ce conteneur, à un autre décalage d'utilisateurs que $DECALAGE_UID :$voisines (détection seulement, rien n'est arrêté)"
  else echo "- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)"; fi
  [ -n "$reserve_voisines" ] && echo "- RÉSERVE : course(s) voisine(s) à un décalage des essais du noyau (0, 700, 800) :$reserve_voisines — pendant les essais d'avant départ (≈ 3 minutes), des processus d'essai tournent sous les utilisateurs 60000 et suivants, 60700–60701, 60800–60830 et 60900 et partagent ces utilisateurs avec elle(s)"
} >> "$L"
[ "$MODE" = simulation ] && [ -n "$ART" ] && note "- ESSAI : artefact « $ART » (simulation)"
# Reprise : l'état de reprise du segment précédent (dernier `course/reprise/etat-vN.json`) — compagnon, arrêt sur STOP,
#   numéro de segment ; seule la dépense déjà faite en est lue (rien d'autre de la course)
compter_etats() { local n=0 f; for f in "$PILOTE/course/reprise"/etat-v*.json; do if [ -f "$f" ]; then n=$((n + 1)); fi; done; echo "$n"; }
lire_etat_reprise() {  # lire_etat_reprise SEGMENT_ATTENDU → « nom sha dépense_faite reste_course » ; code 1 sinon
  "$PY" -I -c '
import hashlib, json, pathlib, sys
d, usd, seg = pathlib.Path(sys.argv[1]) / "reprise", float(sys.argv[2]), int(sys.argv[3])
etats = sorted(d.glob("etat-v*.json"), key=lambda p: int(p.stem.split("-v")[-1])) if d.is_dir() else []
if not etats: print("aucun état de reprise"); sys.exit(1)
p = etats[-1]
c = p.with_name(p.name + ".sha256")
sha = hashlib.sha256(p.read_bytes()).hexdigest()
if not c.is_file() or c.read_text(encoding="utf-8").split()[:1] != [sha]: print(p.name + " : compagnon absent ou différent"); sys.exit(1)
e = json.loads(p.read_text(encoding="utf-8"))
if e.get("raison_arret") != "fichier STOP": print(p.name + " : arrêt autre que STOP (%r)" % e.get("raison_arret")); sys.exit(1)
if e.get("segment") != seg: print(p.name + " : état du segment %r, attendu %d" % (e.get("segment"), seg)); sys.exit(1)
fait = float(e["depense_totale_usd"])
print("%s %s %.4f %.4f" % (p.name, sha, fait, max(0.0, usd - fait)))' "$PILOTE/course" "$USD_COURSE" "$1"
}
if [ "$SEGMENT" != 1 ]; then
  etat_reprise="$(lire_etat_reprise "$((SEGMENT - 1))")" || refus "SEGMENT=$SEGMENT : état de reprise du segment $((SEGMENT - 1)) non conforme ($etat_reprise)"
  read -r ETAT_NOM ETAT_SHA DEJA_USD DU_SEGMENT <<< "$etat_reprise"
  note "- état de reprise : $ETAT_NOM, sha256 $ETAT_SHA (compagnon conforme), arrêt sur STOP du segment $((SEGMENT - 1)) ; dépense de la course jusqu'ici $DEJA_USD USD ; reste au plus $DU_SEGMENT USD pour la course (plafond $USD_COURSE USD)"
fi

# 0 bis (v11 : porte « course v6.2 précédente ») retiré en v12 : rien n'est exigé des courses du pilote 4 (texte v1,
#       table de correspondance) ; PRECEDENTE_V62 est sans effet

# 0. Course M de référence : une course du pilote 4 ne part qu'après une course M du second pilote finie, fermée et
#    saine — liste close du lanceur du second pilote (P2C1-01, P52C1-02), appliquée telle quelle aux pièces lisibles de M,
#    avec le nom, l'empreinte et la lignée du lanceur et de l'objet de M ; graine de M lue dans le texte scellé du second
#    pilote ; la ligne de dépense de la course porte les 16 premiers caractères de l'empreinte des empreintes de M
#    (les noms EMP_S, GRAINE_S_MANIFESTE et issue_s sont ceux du lanceur source ; ils portent ici les valeurs de M)
EMP_S=""
LANCEUR_M_NOM=lancer_pilote2_gemini_v5_2_v5.sh
LANCEUR_M_SHA=83f8b9cf8f3062dfc5e2c02094c602a2d582adf0cbcef292d5bdccd8f8d61b1b
LIGNEE_M="gemini-organisme-v5-2-1"
GO_M=GO-2026-10-25-01
PREREG_M="$R/prereg/pilote2-gemini-organisme-v5-2-v2.md"
PREREG_M_SHA=d294465429094e5099cb5facdad95e2b806aa8953640b57bcab99998396c066b
if [ "$MODE" = reel ] || [ -n "${REFERENCE_M:-}" ]; then
  [ -n "${REFERENCE_M:-}" ] || refus "REFERENCE_M non défini : une course du pilote 4 ne part qu'après une course M saine (dossier du pilote de la course M)"
  SP="$REFERENCE_M"
  [ -d "$SP" ] || refus "REFERENCE_M $SP absent : une course du pilote 4 ne part qu'après M"
  SP="$(cd "$SP" && pwd -P)"
  if [ "$MODE" = reel ]; then
    case "$SP/" in /root/*|/home/*) ;; *) refus "REFERENCE_M $SP hors de /root et de /home";; esac
    [[ "$(basename "$SP")" =~ ^pilote2-gemini-v5-2-1-maieutique-v1(-tentative[0-9]+)?$ ]] || refus "REFERENCE_M $SP : nom autre que pilote2-gemini-v5-2-1-maieutique-v1[-tentativeN]"
  fi
  [ -f "$SP/EMPREINTES-pilote-v1.txt" ] && [ -f "$SP/EMPREINTES-pilote-v1.txt.sha256" ] || refus "empreintes de M absentes : une course du pilote 4 ne part qu'après une course M finie et fermée"
  (cd "$SP" && sha256sum -c --quiet EMPREINTES-pilote-v1.txt.sha256 && sha256sum -c --quiet EMPREINTES-pilote-v1.txt) > /dev/null 2>&1 || refus "empreintes de M non vérifiées (fichiers de M modifiés ou manquants)"
  for f in LANCEMENT.md extrait-mecanique-v1.json; do
    grep -Eq "^[0-9a-f]{64}  $f\$" "$SP/EMPREINTES-pilote-v1.txt" || refus "empreintes de M sans $f"
  done
  EMP_S="$(cut -d' ' -f1 < "$SP/EMPREINTES-pilote-v1.txt.sha256")"
  issue_s="$("$PY" -I -c '
import json, re, sys
sp, sha_lanceur, lignee, mode, go_id, nom_lanceur = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
pb = []
lan = open(sp + "/LANCEMENT.md", encoding="utf-8").read()
if not re.search(r"^- course : maieutique ;", lan, re.M): pb.append("ce n est pas la course M")
if mode == "reel" and not re.search(r"^# Lancement du pilote pilote2-gemini-v5-2-1-maieutique-v1 \(reel, tentative [0-9]+\)$", lan, re.M):
    pb.append("M n a pas tourné en réel")
if "≠ espace attendu" in lan: pb.append("espace des organismes de M autre que l espace attendu")
if not re.search(r"^- lanceur : " + re.escape(nom_lanceur) + r", sha256 " + sha_lanceur + r"$", lan, re.M): pb.append("M n a pas tourné sous ce lanceur")
if not re.search(r"code de retour : 0 ;", lan): pb.append("code de retour du noyau non nul ou absent")
if not re.search(r"^- archive fermée : ferme\.tar\.gz \(", lan, re.M) or "ARCHIVE FERMÉE INCOMPLÈTE" in lan: pb.append("archive fermée absente ou incomplète")
try:
    x = json.load(open(sp + "/extrait-mecanique-v1.json", encoding="utf-8"))
except Exception as e:
    print("extrait de M illisible : " + type(e).__name__); sys.exit(1)
gs = sorted((g for g in x.get("generations", []) if g.get("lignee") == lignee and not g.get("phase")), key=lambda g: g.get("generation", -1))
if [g.get("generation") for g in gs] != [0, 1]: pb.append("générations de M : " + str([g.get("generation") for g in gs]) + " au lieu de [0, 1]")
statuts_appels = []
for g in gs:
    if g.get("statut") != "OK" or g.get("invalide") or g.get("anomalie_noyau"):
        pb.append("g%03d : statut %r, invalide %r, anomalie %r" % (g.get("generation"), g.get("statut"), g.get("invalide"), g.get("anomalie_noyau")))
    a = g.get("appels") or {}
    ps = a.get("par_statut") or {}
    n = a.get("n") if isinstance(a.get("n"), int) else sum(v for v in ps.values() if isinstance(v, int))
    ok = ps.get("OK", 0) if isinstance(ps.get("OK", 0), int) else 0
    if not n:
        pb.append("g%03d : aucun appel au journal" % g.get("generation"))
    elif (n - ok) > 0.20 * n:
        pb.append("g%03d : %d appels hors OK sur %d (plus de 20 %%)" % (g.get("generation"), n - ok, n))
    fab = (((a.get("par_espece") or {}).get("CLAUDE_FABLE_5_1") or {}).get("par_statut") or {}).get("OK", 0)
    if not isinstance(fab, int) or fab < 1:
        pb.append("g%03d : aucun appel OK de CLAUDE_FABLE_5_1" % g.get("generation"))
    statuts_appels.append("g%03d %s" % (g.get("generation"), json.dumps(ps, ensure_ascii=False, sort_keys=True)))
m = x.get("manifeste") or {}
if mode == "reel":
    if m.get("reel") is not True: pb.append("manifeste de M : reel = %r" % m.get("reel"))
    if m.get("go_id") != go_id: pb.append("manifeste de M : go_id = %r" % m.get("go_id"))
r = x.get("rapport") or {}
if r.get("generations_invalidees"): pb.append("générations invalidées : " + str(r.get("generations_invalidees")))
fin = ((r.get("lignees") or {}).get(lignee) or {}).get("fin")
if fin != "générations maximales": pb.append("fin de la lignée : %r" % fin)
arrets = [e.get("raison") for e in x.get("evenements", []) if e.get("etape") == "arret"]
if arrets != ["aucune lignée active"]: pb.append("arrêt de la course : %r" % arrets)
if pb: print("; ".join(pb)); sys.exit(1)
refus_s = [g.get("refus_noyau") for g in gs]
print("M saine : g000 et g001 OK, au plus 20 %% d appels hors OK et au moins un appel OK de Fable à chacune (%s), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de M %s ; dépense du noyau %s USD ; refus du noyau par génération %s" % ("; ".join(statuts_appels), m.get("entropie_seed_sequence"), r.get("depense_totale_usd"), json.dumps(refus_s, ensure_ascii=False)))
' "$SP" "$LANCEUR_M_SHA" "$LIGNEE_M" "$MODE" "$GO_M" "$LANCEUR_M_NOM")" || refus "la course $COURSE ne part pas : issue de M hors de la liste saine ($issue_s) — décision de Lazar requise"
  GRAINE_S_MANIFESTE="$("$PY" -I -c 'import json, sys; print((json.load(open(sys.argv[1])).get("manifeste") or {}).get("entropie_seed_sequence"))' "$SP/extrait-mecanique-v1.json")"
  [ -f "$PREREG_M" ] && [ "$(sha256sum "$PREREG_M" | cut -d' ' -f1)" = "$PREREG_M_SHA" ] || refus "texte scellé du second pilote absent ou d'empreinte autre que d2944654… ($PREREG_M)"
  [[ "$GRAINE_S_MANIFESTE" =~ ^[0-9]+$ ]] || refus "graine de M au manifeste illisible ou vide ($GRAINE_S_MANIFESTE)"
  grep -Eq "^ *graine de la course maieutique = ${GRAINE_S_MANIFESTE}\$" "$PREREG_M" || refus "la course M a tourné avec la graine $GRAINE_S_MANIFESTE, qui n'est pas la graine M du texte scellé du second pilote"
  note "- course M de référence : $SP ; $issue_s ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 $EMP_S) ; graine $GRAINE_S_MANIFESTE = graine M du texte scellé du second pilote (d2944654…)"
fi

# 1. Code identique au noyau attendu, NOYAU_COMMIT (commit et arbre de travail, collisionneur compris) ; commits postérieurs limités aux pièces
#    du pilote ; rien de non suivi ni de modifié sous essaim-m3-refonte-v1 hors des dossiers de pilotes ; ancêtres ;
#    banque, mission, collisionneur
for c in "$COMMIT_CODE" "$COMMIT_LIENS" "$COMMIT_CREDIT" "$COMMIT_ORGANISME" "$COMMIT_QUESTION"; do
  git -C "$DEPOT" cat-file -e "$c^{commit}" 2>/dev/null || refus "commit $c absent du dépôt (git fetch)"
done
P="essaim-m3-refonte-v1/essaim_m3 essaim-m3-refonte-v1/tests collisionneur-v2.5-banc-jev-travail"
# shellcheck disable=SC2086
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" HEAD -- $P || refus "code de HEAD différent de ${NOYAU_COMMIT:0:8} (essaim_m3, tests ou collisionneur)"
# shellcheck disable=SC2086
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" -- $P || refus "arbre de travail différent de ${NOYAU_COMMIT:0:8} (essaim_m3, tests ou collisionneur)"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_CODE" HEAD || refus "${NOYAU_COMMIT:0:8} non ancêtre de HEAD"
hors_pieces="$(git -C "$DEPOT" diff --name-only "$COMMIT_CODE" HEAD | grep -Ev "$PERMIS_APRES_CODE" || true)"
[ -z "$hors_pieces" ] || refus "commits postérieurs à ${NOYAU_COMMIT:0:8} hors des pièces du pilote : $(echo $hors_pieces)"
rel_pilotes="$(realpath --relative-to="$DEPOT" "$RACINE_PILOTES" 2>/dev/null || echo "")"
inattendus="$(git -C "$DEPOT" status --porcelain --ignored --untracked-files=all -- essaim-m3-refonte-v1 collisionneur-v2.5-banc-jev-travail \
  | grep -v '__pycache__' | grep -v '/\.pytest_cache/' | { if [ -n "$rel_pilotes" ] && [ "${rel_pilotes#..}" = "$rel_pilotes" ]; then grep -v " $rel_pilotes/" ; else cat; fi; } || true)"
[ -z "$inattendus" ] || refus "fichiers non suivis ou modifiés sous essaim-m3-refonte-v1 ou le collisionneur : $(echo $inattendus)"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_LIENS" HEAD || refus "correctif des liens 4967734 non ancêtre de HEAD"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_CREDIT" HEAD || refus "R-395 (90595ffb, arrêt sur crédit épuisé en 400) non ancêtre de HEAD"
[ "$(sha256sum "$R/banque/banque-confrontation-v3.json" | cut -d' ' -f1)" = "$SHA_BANQUE" ] || refus "empreinte de la banque ≠ 157a2b45…"
[ "$(sha256sum "$R/MISSION-v1.md" | cut -d' ' -f1)" = "$SHA_MISSION" ] || refus "empreinte de la mission ≠ bd2c6a15…"
[ "$(sha256sum "$DEPOT/collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py" | cut -d' ' -f1)" = "$SHA_COLLISIONNEUR" ] || refus "empreinte du collisionneur ≠ 213b52ef…"
note "- code : identique à ${NOYAU_COMMIT:0:8} (noyau attendu ; commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque $SHA_BANQUE ; mission $SHA_MISSION ; collisionneur $SHA_COLLISIONNEUR"
versions="$(cd / && env -u PYTHONPATH "$PY" -c '
import importlib.metadata as m, platform
out = ["python " + platform.python_version()]
for p in ("numpy", "anthropic"):
    try: out.append(p + " " + m.version(p))
    except Exception: out.append(p + " absente")
print(" ; ".join(out))')"
note "- versions : $versions"
if [ "$MODE" = reel ]; then echo "$versions" | grep -q "anthropic absente" && refus "bibliothèque anthropic absente de l'interpréteur $PY"; fi

# 1 bis. Isolation : dossier du pilote non traversable par les autres → espace des organismes sous /var/lib/essaim-m3/,
#        hors du dépôt ; espace attendu calculé ; dépôt caché aux organismes (vérifié par la fonction du noyau)
[ "$ART" = traversable ] && chmod 711 "$PILOTE"
[ "$(stat -c '%a %u' "$PILOTE")" = "700 0" ] || refus "dossier du pilote $(stat -c '%a %u' "$PILOTE") au lieu de « 700 0 » : l'espace des organismes serait sous le dépôt"
ESPACE_ATTENDU="/var/lib/essaim-m3/$("$PY" -I -c 'import hashlib, pathlib, sys; print(hashlib.sha256(str(pathlib.Path(sys.argv[1]).resolve()).encode("utf-8")).hexdigest()[:16])' "$PILOTE/course")"
CACHER="$DEPOT"; [ "$ART" = cache ] && CACHER="/nulle-part-$$"
(cd "$R" && env -u PYTHONPATH ESSAIM_M3_CACHER="$CACHER" "$PY" -B -I -c '
import sys; sys.path.insert(0, ".")
from essaim_m3.noyau import bac_a_sable
import pathlib
caches = bac_a_sable.dossiers_a_cacher([sys.argv[1] + "/travail/x", sys.argv[1] + "/travail/x/noyau.sock"])
sys.exit(0 if str(pathlib.Path(sys.argv[2]).resolve()) in caches else 1)' "$ESPACE_ATTENDU" "$DEPOT") \
  || refus "le dépôt $DEPOT ne serait pas caché aux organismes (bac_a_sable.dossiers_a_cacher)"
note "- isolation : dossier du pilote 0700 à root ; espace attendu $ESPACE_ATTENDU ; dépôt $DEPOT caché aux organismes (vérifié par bac_a_sable.dossiers_a_cacher) ; ESSAIM_M3_ESPACE non définie"

# 2. Texte scellé (réel ; en simulation si TEXTE est donné) : un texte pour les deux courses ; la graine de cette course est
#    recalculée depuis l'entropie (enfant INDICE_GRAINE) ; la ligne de l'autre course doit exister (elle n'est pas utilisée)
if [ "$MODE" = reel ] || [ -n "${TEXTE:-}" ]; then
  TEXTE="${TEXTE:?TEXTE=chemin du texte scellé}"; TEXTE_SHA256="${TEXTE_SHA256:?}"
  [ "$(sha256sum "$TEXTE" | cut -d' ' -f1)" = "$TEXTE_SHA256" ] || refus "empreinte du texte ≠ TEXTE_SHA256"
  [ -f "$TEXTE.sha256" ] && [ "$(cut -d' ' -f1 < "$TEXTE.sha256")" = "$TEXTE_SHA256" ] || refus "compagnon .sha256 du texte absent ou différent"
  grep -q "graine de la course $COURSE = $GRAINE\b" "$TEXTE" || refus "la graine $GRAINE de la course $COURSE n'est pas écrite dans le texte scellé"
  AUTRE_COURSE=audit; [ "$COURSE" = audit ] && AUTRE_COURSE=maieutique
  grep -Eq "^ *graine de la course $AUTRE_COURSE = [0-9]+\$" "$TEXTE" || refus "la ligne « graine de la course $AUTRE_COURSE = … » est absente du texte (un texte pour les deux courses ; cette ligne n'est pas utilisée ici)"
  if grep -q "<<[A-Z0-9_]*>>" "$TEXTE"; then refus "marqueurs <<…>> restants : texte non scellé"; fi
  grep -q "$SHA_LANCEUR" "$TEXTE" || refus "le texte ne cite pas l'empreinte de ce lanceur"
  E_TEXTE="$(grep -Eo 'entropie E = [0-9]+' "$TEXTE" | head -1 | grep -Eo '[0-9]+$' || true)"
  [ -n "$E_TEXTE" ] || refus "entropie E absente du texte"
  g_calc="$("$PY" -I -c 'import sys, numpy; e, i = int(sys.argv[1]), int(sys.argv[2]); print(int(numpy.random.SeedSequence(e).spawn(2)[i].generate_state(1, dtype=numpy.uint64)[0]))' "$E_TEXTE" "$INDICE_GRAINE")"
  [ "$g_calc" = "$GRAINE" ] || refus "graine $GRAINE ≠ celle de SeedSequence(E).spawn(2)[$INDICE_GRAINE] = $g_calc"
  note "- texte : $TEXTE, sha256 $TEXTE_SHA256 (compagnon conforme), graine $GRAINE de la course $COURSE écrite et recalculée depuis l'entropie du texte (enfant $INDICE_GRAINE), ligne de la course $AUTRE_COURSE présente (non utilisée), empreinte du lanceur citée"
fi

# 3. Organisme de la course (la v6.2.1 pour les deux courses, dossier organisme/ seul) et question servie (la question de base, puis, pour la course « audit », ses annexes), extraits des commits cités, vérifiés
# reprise : l'organisme et la question extraits au segment 1, revérifiés ci-dessous, jamais réécrits
if [ "$SEGMENT" = 1 ]; then git -C "$DEPOT" archive "$COMMIT_ORGANISME" organisme | tar -x -C "$PILOTE"; else [ -d "$PILOTE/organisme" ] || refus "SEGMENT=$SEGMENT : organisme du segment 1 absent de $PILOTE"; fi
ORG="$PILOTE/organisme"
[ "$ART" = organisme ] && printf ' ' >> "$ORG/principal.py"
[ "$ART" = nombre ] && rm -f "$ORG/CONCEPTION.md"
n_fichiers="$(find "$ORG" -type f | wc -l)"
[ "$n_fichiers" = "$N_FICHIERS_ORGANISME" ] || refus "organisme : $n_fichiers fichiers au lieu de $N_FICHIERS_ORGANISME"
empreinte_arbre() { (cd "$R" && env -u PYTHONPATH "$PY" -B -I -c 'import pathlib, sys; sys.path.insert(0, "."); from essaim_m3.noyau import boucle; print(boucle.empreinte_arbre(pathlib.Path(sys.argv[1])))' "$1"); }
[ "$(empreinte_arbre "$ORG")" = "$ARBRE_ORGANISME" ] || refus "empreinte d'arbre de l'organisme ≠ ${ARBRE_ORGANISME:0:8}…"
# question de base présente au commit cité et d'empreinte juste ; annexes servies : les emplacements de la course dont les trois
# champs sont remplis, dans l'ordre (un emplacement à moitié rempli est un refus), chacune présente à son commit et d'empreinte
# juste ; la question servie (question.md) est leur composé, écrit au segment 1 et revérifié à chaque segment (empreinte du
# composé recalculée depuis le dépôt) ; elle doit tenir dans la borne du noyau (QUESTION_CARACTERES_MAX, vérifiée égale à
# CARACTERES_MAX_QUESTION de question.py du code attendu : 100 000 caractères au noyau 9beee10b)
git -C "$DEPOT" cat-file -e "$COMMIT_QUESTION:$CHEMIN_QUESTION" 2>/dev/null || refus "question ($CHEMIN_QUESTION) absente du commit ${COMMIT_QUESTION:0:8}…"
[ "$(git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" | sha256sum | cut -d' ' -f1)" = "$SHA_QUESTION" ] || refus "empreinte de la question ≠ ${SHA_QUESTION:0:8}…"
AN_COMMITS=(); AN_CHEMINS=(); AN_SHAS=(); n_annexes=0
for k in $ANNEXES; do
  vc="ANNEXE_${k}_COMMIT"; vp="ANNEXE_${k}_CHEMIN"; vs="ANNEXE_${k}_SHA"; c="${!vc}"; p="${!vp}"; s="${!vs}"
  if [ -z "$c$p$s" ]; then continue; fi
  { [ -n "$c" ] && [ -n "$p" ] && [ -n "$s" ]; } || refus "annexe $k : champs incomplets (ANNEXE_${k}_COMMIT, ANNEXE_${k}_CHEMIN et ANNEXE_${k}_SHA vont ensemble)"
  git -C "$DEPOT" cat-file -e "$c^{commit}" 2>/dev/null || refus "annexe $k : commit $c absent du dépôt (git fetch)"
  git -C "$DEPOT" cat-file -e "$c:$p" 2>/dev/null || refus "annexe $k ($p) absente du commit ${c:0:8}…"
  [ "$(git -C "$DEPOT" show "$c:$p" | sha256sum | cut -d' ' -f1)" = "$s" ] || refus "empreinte de l'annexe $k ($p) ≠ ${s:0:8}…"
  n_annexes=$((n_annexes + 1)); AN_COMMITS+=("$c"); AN_CHEMINS+=("$p"); AN_SHAS+=("$s")
done
composer_question() {  # la question servie : la question de base, puis, pour chaque annexe servie (numérotée dans l'ordre), une ligne ---, un titre et son contenu
  git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION"
  local i
  for ((i = 0; i < n_annexes; i++)); do printf '\n---\n\n# Annexe %d — %s (sha256 %s)\n\n' "$((i + 1))" "${AN_CHEMINS[i]}" "${AN_SHAS[i]}"; git -C "$DEPOT" show "${AN_COMMITS[i]}:${AN_CHEMINS[i]}"; done
}
SHA_QUESTION_SERVIE="$(composer_question | sha256sum | cut -d' ' -f1)"
if [ "$SEGMENT" = 1 ]; then composer_question > "$PILOTE/question.md"; else [ -f "$PILOTE/question.md" ] || refus "SEGMENT=$SEGMENT : question du segment 1 absente de $PILOTE"; fi
[ "$ART" = question ] && printf '\n' >> "$PILOTE/question.md"
[ "$(sha256sum "$PILOTE/question.md" | cut -d' ' -f1)" = "$SHA_QUESTION_SERVIE" ] || refus "empreinte de la question servie ≠ ${SHA_QUESTION_SERVIE:0:8}… (question.md altéré, ou composé autrement qu'au segment 1)"
N_CARACTERES_QUESTION="$("$PY" -I -c 'import sys; print(len(open(sys.argv[1], encoding="utf-8").read()))' "$PILOTE/question.md")"
BORNE_NOYAU="$(cd "$R" && env -u PYTHONPATH "$PY" -B -I -c 'import sys; sys.path.insert(0, "."); from essaim_m3.noyau import question; print(question.CARACTERES_MAX_QUESTION)' 2>/dev/null || echo illisible)"
[ "$BORNE_NOYAU" = "$QUESTION_CARACTERES_MAX" ] || refus "QUESTION_CARACTERES_MAX=$QUESTION_CARACTERES_MAX ≠ CARACTERES_MAX_QUESTION du noyau ($BORNE_NOYAU, essaim_m3/noyau/question.py) : paramètre et noyau attendu vont ensemble"
[ "$N_CARACTERES_QUESTION" -le "$QUESTION_CARACTERES_MAX" ] || refus "question servie de $N_CARACTERES_QUESTION caractères > $QUESTION_CARACTERES_MAX (borne du noyau ${NOYAU_COMMIT:0:8}, essaim_m3/noyau/question.py, CARACTERES_MAX_QUESTION) : le noyau la refuserait avant tout appel"
note "- organisme : $N_FICHIERS_ORGANISME fichiers, empreinte d'arbre $ARBRE_ORGANISME ; question ($COURSE) : sha256 $SHA_QUESTION (${CHEMIN_QUESTION##*/}, commit ${COMMIT_QUESTION:0:8}…) ; annexes servies : $n_annexes$(for ((i = 0; i < n_annexes; i++)); do printf ' ; annexe %d : %s %s %s' "$((i + 1))" "${AN_CHEMINS[i]}" "${AN_COMMITS[i]}" "${AN_SHAS[i]}"; done)"
note "- question servie : question.md, sha256 $SHA_QUESTION_SERVIE, $N_CARACTERES_QUESTION caractères"
[ "$COURSE" = audit ] && [ "$n_annexes" = 0 ] && note "- RÉSERVE : course « audit » sans aucune annexe servie (l'annexe 1, transcription expurgée du rapport, est-elle remplie ?)"

# CLORE=1 : ni registre, ni test de dépense, ni essais, ni course — la course arrêtée est fermée (étape 8a)
if [ -z "$CLORE" ]; then
# 4. Registre des GO : une ligne « | $GO_ID | » (le GO de la course) qui porte « calcul », l'empreinte (8 premiers caractères) de
#    la question et celle de l'objet de la course ; dépense consignée avant (une ligne nommant la course, le GO et
#    l'empreinte des empreintes de M) ; reste ≥ plafond de la course
if [ "$MODE" = reel ] || [ -n "${REGISTRE_GO_SOURCE:-}" ]; then
  if [ "$MODE" = reel ]; then git -C "$DEPOT" show origin/main:registres/go.md > "$DS/registre-go.md"; else cp "$REGISTRE_GO_SOURCE" "$DS/registre-go.md"; fi
  # pilote 4 : la ligne porte aussi les 16 premiers caractères de l'empreinte du texte scellé (toujours donné en réel)
  t16="${TEXTE_SHA256:-}"; t16="${t16:0:16}"
  ligne_go="$(grep "^| $GO_ID |" "$DS/registre-go.md" | grep 'calcul' | grep "${SHA_QUESTION:0:8}" | grep "${ARBRE_ORGANISME:0:8}" || true)"
  if [ -n "$t16" ]; then ligne_go="$(echo "$ligne_go" | grep "$t16" || true)"; fi
  [ -n "$ligne_go" ] \
    || refus "aucune ligne « | $GO_ID | » qui porte à la fois le type calcul, l'empreinte de la question ${SHA_QUESTION:0:8}…, l'empreinte de l'organisme ${ARBRE_ORGANISME:0:8}… et celle du texte scellé (${t16:-aucun texte donné en simulation}) (GO non inscrit pour cette course, cet objet et ce texte)"
  if [ "$MODE" = reel ]; then dep="$(git -C "$DEPOT" show origin/main:registres/depenses.md)"; else dep="$(cat "${DEPENSES_SOURCE:?DEPENSES_SOURCE en simulation avec REGISTRE_GO_SOURCE}")"; fi
  echo "$dep" | grep "$NOM" | grep -q "$GO_ID" || refus "lancement non consigné avant dans registres/depenses.md (une ligne nommant $NOM et $GO_ID)"
  if [ "$SEGMENT" != 1 ]; then
    echo "$dep" | grep "$NOM" | grep "$GO_ID" | grep -q "segment $SEGMENT\b" || refus "segment $SEGMENT non consigné avant dans registres/depenses.md (une ligne nommant $NOM, $GO_ID et « segment $SEGMENT »)"
  fi
  if [ -n "$EMP_S" ]; then
    echo "$dep" | grep "$NOM" | grep "$GO_ID" | grep -q "${EMP_S:0:16}" || refus "la ligne de dépense de la course $COURSE ne porte pas l'empreinte des empreintes de M (${EMP_S:0:16}…), écrite après la fin de M"
  fi
  reste="${RESTE_GO_USD:?RESTE_GO_USD=reste disponible sur $GO_ID avant cette course, en USD}"
  besoin="$USD_COURSE"; if [ "$SEGMENT" != 1 ]; then besoin="$DU_SEGMENT"; fi   # reprise : 75 USD moins la dépense déjà faite (état de reprise)
  "$PY" -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= float(sys.argv[2]) else 1)' "$reste" "$besoin" || refus "reste sur $GO_ID = $reste USD < $besoin"
  note "- registre : une ligne $GO_ID de type calcul portant l'empreinte de la question ($COURSE), celle de l'organisme (${ARBRE_ORGANISME:0:8}…) et celle du texte scellé (${t16:-aucun texte donné en simulation}) ; dépense consignée avant$(if [ "$SEGMENT" != 1 ]; then echo " (segment $SEGMENT)"; fi) ; reste déclaré $reste USD ≥ $besoin (vérification du lanceur)"
fi

# 5. Test de dépense (réel ; en simulation si le fichier est donné) : la pièce de l'outil de session-depot (un appel
#    payant par espèce) est lue et vérifiée ici ; la réalité des appels est attestée par l'outil, pas par ce script
EXIGER_HEURE=0; { [ "$MODE" = reel ] || [ -n "${ESSAI_EXIGER_HEURE:-}" ]; } && EXIGER_HEURE=1
verifier_test_depense() {  # verifier_test_depense FICHIER → verdict sur la sortie ; code 1 si non conforme
  "$PY" -I -c '
import datetime, json, os, sys, time
f, go_attendu, age_max, exiger_heure = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4] == "1"
nom_anthropic, nom_gemini = sys.argv[5], sys.argv[6]
attendus = {"CLAUDE_FABLE_5_1": "claude-fable-5-1", "CLAUDE_OPUS_5_5": "claude-opus-5-5", "GEMINI_ARGON": "gemini-4-argon"}
try:
    d = json.load(open(f, encoding="utf-8"))
except Exception as e:
    print(f"illisible : {type(e).__name__}"); sys.exit(1)
pb = []
maintenant = time.time()
age = maintenant - os.stat(f).st_mtime
if age > age_max: pb.append(f"âge du fichier {age:.0f} s > {age_max:.0f} s")
go = d.get("go")
if go != go_attendu: pb.append(f"go = {go!r} (attendu {go_attendu})")
esp = d.get("especes") or {}
couts = []
for e, m in attendus.items():
    r = esp.get(e) or {}
    st, ms, c = r.get("statut"), r.get("modele_servi"), r.get("cout_usd")
    if st != "OK": pb.append(f"{e} : statut {st!r}")
    if ms != m: pb.append(f"{e} : modèle servi {ms!r}")
    if not isinstance(c, (int, float)) or isinstance(c, bool) or c <= 0: pb.append(f"{e} : coût {c!r} (un appel payant est exigé)")
    js = r.get("jetons_sortie", (r.get("usage") or {}).get("sortie") if isinstance(r.get("usage"), dict) else None)
    if js is not None and (not isinstance(js, int) or isinstance(js, bool) or js <= 0): pb.append(f"{e} : jetons de sortie {js!r}")
    h = r.get("heure_utc")
    if h is None:
        if exiger_heure: pb.append(f"{e} : heure_utc absente (exigée en réel)")
    else:
        try:
            dt = datetime.datetime.fromisoformat(str(h).replace("Z", "+00:00"))
            if dt.tzinfo is None:
                pb.append(f"{e} : heure_utc sans fuseau {h!r}")
            else:
                t = dt.timestamp()
                if maintenant - t > age_max: pb.append(f"{e} : appel fait il y a {maintenant - t:.0f} s > {age_max:.0f} s")
        except Exception:
            pb.append(f"{e} : heure_utc illisible {h!r}")
    couts.append(f"{e} {c}")
noms = d.get("variables_cles")
note_noms = "noms des variables du test : absents de la pièce (réserve, P52C1-05)"
if isinstance(noms, dict):
    for cle, attendu in (("anthropic", nom_anthropic), ("gemini", nom_gemini)):
        if attendu and noms.get(cle) != attendu:
            pb.append(f"noms des variables du test : {cle} = {noms.get(cle)!r} (attendu {attendu})")
    note_noms = "noms des variables du test : " + ", ".join(f"{k} {v}" for k, v in sorted(noms.items()))
elif noms is not None:
    pb.append("variables_cles illisible")
if pb: print("; ".join(pb)); sys.exit(1)
print("trois espèces OK, modèles servis conformes, coûts " + ", ".join(couts) + f" USD, âge {age:.0f} s ; " + note_noms)
' "$1" "$GO_ID" "$AGE_MAX_TEST_DEPENSE" "$EXIGER_HEURE" "${CLE_ANTHROPIC:-}" "${CLE_GEMINI:-}"
}
TD=""
if [ "$MODE" = reel ] || [ -n "${APPEL_CONTROLE_FICHIER:-}" ]; then
  TD="${APPEL_CONTROLE_FICHIER:?APPEL_CONTROLE_FICHIER=résultat du test de dépense par espèce (JSON)}"
  [ "$ART" = appel ] && TD="$PILOTE/appel-vide.json" && : > "$TD"
  [ "$ART" = appel-vieux ] && touch -d '20 minutes ago' "$TD"
  [ -s "$TD" ] || refus "résultat du test de dépense absent ou vide : $TD"
  verdict="$(verifier_test_depense "$TD")" || refus "test de dépense non conforme : $verdict"
  SHA_TD="$(sha256sum "$TD" | cut -d' ' -f1)"
  cp "$TD" "$DS/test-depense-$(basename "$TD")"
  note "- test de dépense : $(basename "$TD"), sha256 $(sha256sum "$TD" | cut -d' ' -f1) — $verdict (réalité des appels attestée par l'outil de session-depot ; le script vérifie la pièce)"
  attest="$(printf '%s' "${RECHARGE_ATTESTEE:-}" | tr -d '\n\r' | cut -c1-300)"
  [ -n "$attest" ] && note "- recharge automatique attestée : « $attest »"
fi

# 6. Essais (en root en réel), puis code sans bytecode et empreinte du noyau
if [ "$MODE" = simulation ] && [ -n "${ESSAI_JUNIT_EXISTANT:-}" ]; then
  cp "$ESSAI_JUNIT_EXISTANT" "$DS/essais-v1.xml"; resultat="${ESSAI_RESUME_EXISTANT:?}"
  note "- ESSAI : rapport JUnit repris de $ESSAI_JUNIT_EXISTANT (simulation)"
else
  resultat="$( (cd "$R" && env -u PYTHONPATH -u ESSAIM_M3_COLLISIONNEUR -u ESSAIM_M3_CACHER PYTHONDONTWRITEBYTECODE=1 "$PY" -m pytest -q -p no:cacheprovider --junitxml "$DS/essais-v1.xml" ${PYTEST_ARGS:-} 2>&1) | tail -1 || true)"
fi
if [ "$ART" = junit-echec ] || [ "$ART" = junit-saut ] || [ "$ART" = junit-total ]; then
  "$PY" -I -c '
import sys, xml.etree.ElementTree as ET
a, f = sys.argv[1], sys.argv[2]
t = ET.parse(f); cas = list(t.getroot().iter("testcase"))
if a == "junit-echec": ET.SubElement(cas[0], "failure", message="artefact")
elif a == "junit-saut": ET.SubElement([c for c in cas if c.get("name") == "test_sources_reelles_de_moisson_si_reseau"][0], "skipped", message="artefact")
else:
    for s in t.getroot().iter("testsuite"):
        for c in list(s.findall("testcase"))[:3]: s.remove(c)
t.write(f)' "$ART" "$DS/essais-v1.xml"
fi
"$PY" -I -c '
import re, sys, xml.etree.ElementTree as ET
resume, junit, cites, total_attendu = sys.argv[1], sys.argv[2], set(sys.argv[3].split()), int(sys.argv[4])
n = {k: int(v) for v, k in re.findall(r"(\d+) (passed|failed|errors?|skipped|deselected|xfailed|xpassed)", resume)}
try:
    cas = list(ET.parse(junit).getroot().iter("testcase"))
except Exception as e:
    print(f"rapport JUnit illisible : {e}"); sys.exit(1)
etat = {}
for c in cas:
    e = "passe"
    for enfant in c:
        if enfant.tag in ("failure", "error"): e = "echec"
        elif enfant.tag == "skipped" and e != "echec": e = "saute"
    etat[c.get("name")] = e
echecs = sorted(k for k, v in etat.items() if v == "echec")
sautes = sorted(k for k, v in etat.items() if v == "saute")
manquants = sorted(cites - {k for k, v in etat.items() if v == "passe"})
d = n.get("deselected", 0)
total = len(etat) + d
problemes = []
if echecs: problemes.append(f"échecs : {echecs}")
if sautes: problemes.append(f"sauts (aucun permis) : {sautes}")
if manquants: problemes.append(f"essais cités non passés ici : {manquants}")
if total != total_attendu: problemes.append(f"{total} essais au lieu de {total_attendu}")
print("; ".join(problemes) if problemes else f"{len(etat)} passés, 0 sauté, {d} désélectionnés")
sys.exit(1 if problemes else 0)' "$resultat" "$DS/essais-v1.xml" "$ESSAIS_CITES" "$N_ESSAIS" > "$DS/essais-v1.txt" || refus "essais : $(cat "$DS/essais-v1.txt") (résumé : « $resultat »)"
note "- essais : $(cat "$DS/essais-v1.txt") ; arguments : « ${PYTEST_ARGS:-aucun} » ; les $(echo $ESSAIS_CITES | wc -w) essais cités ont passé ici (dont la recherche réelle sur arXiv)"
find "$R/essaim_m3" "$R/tests" "$DEPOT/collisionneur-v2.5-banc-jev-travail" -name __pycache__ -prune -exec rm -rf {} +
[ "$ART" = bytecode ] && mkdir -p "$R/essaim_m3/noyau/__pycache__" && printf x > "$R/essaim_m3/noyau/__pycache__/x.pyc"
code_noyau="$(empreinte_arbre "$R/essaim_m3/noyau")"
[ "$code_noyau" = "$CODE_NOYAU_PROPRE" ] || refus "empreinte du noyau nettoyé $code_noyau ≠ ${CODE_NOYAU_PROPRE:0:8}… (NOYAU_EMPREINTE_PROPRE)"
note "- noyau sans bytecode : empreinte $code_noyau (la fonction écarte le bytecode depuis le constat n° 30 § 5)"

# 6 bis. Juste avant le départ : test de dépense revérifié (âge ≤ 15 min au départ) ; voisines redétectées
if [ -n "$TD" ]; then
  [ "$ART" = appel-vieillit ] && touch -d '20 minutes ago' "$TD"
  [ "$ART" = appel-modifie ] && printf ' ' >> "$TD"
  [ "$(sha256sum "$TD" | cut -d' ' -f1)" = "$SHA_TD" ] || refus "la pièce du test de dépense a changé depuis sa première lecture : refaire le test, puis TENTATIVE=$((TENTATIVE + 1))"
  verdict2="$(verifier_test_depense "$TD")" || refus "test de dépense trop ancien ou non conforme au départ ($verdict2) : le refaire, puis TENTATIVE=$((TENTATIVE + 1))"
  note "- test de dépense revérifié au départ : $verdict2"
fi
detecter_voisines || refus "une course du noyau tourne au décalage $DECALAGE_UID au moment du départ : le pilote attend"
note "- voisines au départ :${voisines:- aucune}"
if [ "$SEGMENT" = 1 ]; then if raison_r3="$(course_deja_partie)"; then refus "$raison_r3 (R3, au départ)"; fi; fi
essais_en_cours="$(pgrep -f 'pytest' 2>/dev/null | tr '\n' ' ' || true)"
[ -n "$essais_en_cours" ] && note "- RÉSERVE : des essais (pytest) tournent dans le conteneur au départ (PID $essais_en_cours) : ceux du noyau font tourner des processus sous l'utilisateur 60900 de ce pilote"
# 6 ter. Environnement du noyau : vide (env -i), sauf la liste ci-dessous ; les variables d'infrastructure réseau du
#        conteneur (passerelle de sortie et certificats) passent quand elles sont définies ; les clés en réel seulement.
#        Puis la passerelle de sortie est vérifiée sous cet environnement, sans clé (P52C1-04) : `httpx` (client de la
#        bibliothèque `anthropic`) vers l'interface d'Anthropic, `urllib` avec le contexte du collisionneur vers celle de
#        Gemini ; un statut HTTP quelconque suffit (401, 403 sans clé) ; sinon refus avant le manifeste.
INFRA_RESEAU="HTTPS_PROXY https_proxy HTTP_PROXY http_proxy NO_PROXY no_proxy SSL_CERT_FILE SSL_CERT_DIR REQUESTS_CA_BUNDLE CURL_CA_BUNDLE GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"
ENV_BASE=(PATH="$PATH" HOME="${HOME:-/root}" LANG="${LANG:-C.UTF-8}" PYTHONDONTWRITEBYTECODE=1 ESSAIM_M3_CACHER="$DEPOT")
for v in $INFRA_RESEAU; do [ -n "${!v:-}" ] && ENV_BASE+=("$v=${!v}"); done
PY_PASSERELLE=""
if [ "$MODE" = reel ]; then PY_PASSERELLE="$PY"; elif [ -n "${ESSAI_PASSERELLE_PY:-}" ]; then PY_PASSERELLE="$ESSAI_PASSERELLE_PY"; fi
if [ -n "$PY_PASSERELLE" ]; then
  passerelle="$(cd / && env -i "${ENV_BASE[@]}" "$PY_PASSERELLE" -I -c '
import os, ssl, sys, urllib.error, urllib.request
r = []
try:
    import httpx
    s = httpx.get("https://api.anthropic.com/v1/models", timeout=30).status_code
    r.append("httpx %s, api.anthropic.com : statut %d" % (httpx.__version__, s))
except Exception as e:
    print("httpx, api.anthropic.com : %s : %s" % (type(e).__name__, str(e)[:120])); sys.exit(1)
ca = os.environ.get("SSL_CERT_FILE")
ctx = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
try:
    urllib.request.urlopen("https://generativelanguage.googleapis.com/v1beta/models", context=ctx, timeout=30)
    r.append("urllib, generativelanguage.googleapis.com : statut 200")
except urllib.error.HTTPError as e:
    r.append("urllib, generativelanguage.googleapis.com : statut %d" % e.code)
except Exception as e:
    print("urllib, generativelanguage.googleapis.com : %s : %s" % (type(e).__name__, str(e)[:120])); sys.exit(1)
print(" ; ".join(r))
' 2>&1)" || refus "passerelle de sortie injoignable sous l'environnement du noyau : $passerelle"
  note "- passerelle de sortie, sous l'environnement du noyau sans clé : $passerelle"
fi
ENV_NOYAU=("${ENV_BASE[@]}")
if [ "$MODE" = reel ]; then
  ENV_NOYAU+=(ANTHROPIC_API_KEY="${!SOURCE_ANTHROPIC}" GEMINI_API_KEY="${!SOURCE_GEMINI}" BRAVE_API_KEY="${!SOURCE_BRAVE}"
              OPENALEX_API_KEY="${!SOURCE_OPENALEX}" SEMANTIC_SCHOLAR_API_KEY="${!SOURCE_S2}")
fi
noms_env=""; for a in "${ENV_NOYAU[@]}"; do noms_env+="${a%%=*} "; done
note "- environnement du noyau (noms seulement, valeurs jamais écrites) : ${noms_env}."
if [ "$SEGMENT" = 1 ]; then
  mkdir -p "$MARQUEURS"
  ( set -o noclobber; printf '%s %s\n' "$PILOTE" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$MARQUEURS/$NOM" ) 2>/dev/null || refus "marqueur de départ $MARQUEURS/$NOM déjà posé (R3)"
  note "- marqueur de départ : $MARQUEURS/$NOM (R3 ; jamais retiré)"
else
  note "- marqueur de départ : $MARQUEURS/$NOM, posé au segment 1 pour ce dossier (R3 ; jamais retiré)"
fi

# 7. La course : sortie standard fermée (elle porte les scores), sortie d'erreur lisible ; PID consigné
FAMILLE=gemini; [ "$ART" = famille ] && FAMILLE=inconnue
COMMUNES=(--sortie "$PILOTE/course" --generations 4 --graine "$GRAINE" --especes --appels-max 160 --usd-par-generation "$USD_GEN"
          --temps-max 2400 --max-tokens-appel 8192 --recherches-max 6 --telechargements-max 3 --octets-max 40000000
          --entrainements-max 0 --rondes-conception-max 6 --usd-max-conception 3 --temps-max-conception 900 --parallele-max 8 --relances-max 1 --isoler-reseau
          --plafond-total "$USD_COURSE" --decalage-uid "$DECALAGE_UID"
          --question-ouverte "$PILOTE/question.md" --question-ouverte-aux g001
          --organisme-impose "$LIGNEE=$ORG@$FAMILLE")
if [ "$SEGMENT" != 1 ]; then COMMUNES+=(--reprendre); fi   # reprise : le noyau continue la course de --sortie (état scellé, mêmes paramètres)
SORTIE_FERMEE="$PILOTE/ferme/sortie-standard-lanceur$SUFFIXE_SEG.txt"
ERREURS="$DS/sortie-erreur-lanceur.txt"
cd "$R"
N_ETATS_AVANT="$(compter_etats)"
N_EV_AVANT=0
if [ "$SEGMENT" != 1 ]; then
  N_EV_AVANT="$(wc -l < "$PILOTE/course/evenements.jsonl")"
  if [ -f "$PILOTE/course/STOP" ]; then rm -f "$PILOTE/course/STOP"; note "- STOP du segment $((SEGMENT - 1)) retiré de course/ (reprise)"; fi
fi
if [ "$MODE" = reel ]; then
  note "- clés : présentes (valeurs jamais lues ni écrites) ; Anthropic : variable $SOURCE_ANTHROPIC → ANTHROPIC_API_KEY ; Gemini : $SOURCE_GEMINI → GEMINI_API_KEY ; Brave : $SOURCE_BRAVE → BRAVE_API_KEY (source « web ») ; OpenAlex : $SOURCE_OPENALEX → OPENALEX_API_KEY ; Semantic Scholar : $SOURCE_S2 → SEMANTIC_SCHOLAR_API_KEY ; rien d'autre de l'environnement du lanceur (ni jeton Hugging Face, Vast, OSF, GitHub, ni ANTHROPIC_BASE_URL, PYTHONPATH, ESSAIM_M3_ESPACE, ESSAIM_M3_COLLISIONNEUR)"
  note "- départ (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)$(if [ "$SEGMENT" != 1 ]; then echo " ; segment $SEGMENT, reprise de la course"; fi)"
  setsid env -i "${ENV_NOYAU[@]}" \
    "$PY" -m essaim_m3 lancer --reel --go "$GO_ID" --registre-go "$DS/registre-go.md" \
      --taches banque/banque-confrontation-v3.json --mission MISSION-v1.md "${COMMUNES[@]}" \
      > "$SORTIE_FERMEE" 2> "$ERREURS" &
else
  note "- départ de la simulation (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)$(if [ "$SEGMENT" != 1 ]; then echo " ; segment $SEGMENT, reprise de la course"; fi)"
  setsid env -i "${ENV_NOYAU[@]}" \
    "$PY" -m essaim_m3 simuler "${COMMUNES[@]}" --n-train 80 --n-test 60 --n-final 60 \
      > "$SORTIE_FERMEE" 2> "$ERREURS" &
fi
PID=$!
groupe_de() { sed 's/^.*) //' "/proc/$1/stat" 2>/dev/null | cut -d' ' -f3 || true; }   # groupe de processus d'un PID (champ pgrp de /proc)
for i in 1 2 3 4 5; do PGID_NOYAU="$(groupe_de "$PID")"; [ "$PGID_NOYAU" = "$PID" ] && break; sleep 0.2; done   # setsid a pris effet dès que le groupe est le PID
note "- PID de la course : $PID (session et groupe de processus propres, par setsid : groupe ${PGID_NOYAU:-illisible} ; arrêt humain par ce PID seulement, R10, ou par la garde refus-question ; STOP dans course/ : arrêt avant la ronde ou la génération suivante, celle en cours finit)"
# P4C1-02 : minuteur, lancé en fond et arrêté par son PID dès la fin du processus de la course (R10). À l'échéance, si la
#   course tourne encore (segment 1 : manifeste écrit ; segment K ≥ 2 : reprise consignée par le noyau), il pose STOP dans
#   course/ (le noyau le lit avant chaque ronde et chaque génération, `_doit_arreter`) ; le noyau finit l'unité en cours,
#   écrit son état de reprise et rend 0 : fin du segment, la course reste ouverte et le segment suivant la continue ;
#   si plus aucune unité ne restait, la course a fini et se ferme (étape 8a).
course_en_cours() {  # segment 1 : manifeste écrit ; segment K ≥ 2 : reprise consignée par le noyau (sinon STOP la ferait refuser)
  if [ "$SEGMENT" = 1 ]; then [ -f "$PILOTE/course/manifeste-run.json" ]; else [ "$(wc -l < "$PILOTE/course/evenements.jsonl")" -gt "$N_EV_AVANT" ]; fi
}
minuteur() {
  local fin=$(( DEBUT_LANCEUR_S + ECHEANCE_STOP_S )) s
  trap 'exit 0' TERM
  while kill -0 "$PID" 2>/dev/null; do
    if course_en_cours && [ "$(date +%s)" -ge "$fin" ]; then
      : > "$PILOTE/course/STOP"
      note "- minuteur : STOP posé dans course/ à $(date -u +%Y-%m-%dT%H:%M:%SZ) ($ECHEANCE_STOP_S s après le départ du lanceur) : la course s'arrête avant la ronde ou la génération suivante ; état de reprise attendu"
      exit 0
    fi
    sleep 1 & s=$!
    wait "$s" || true
  done
}
minuteur & MINUTEUR=$!
note "- minuteur : PID $MINUTEUR ; échéance $(date -u -d "@$(( DEBUT_LANCEUR_S + ECHEANCE_STOP_S ))" +%Y-%m-%dT%H:%M:%SZ), $ECHEANCE_STOP_S s après le départ du lanceur ($(date -u -d "@$DEBUT_LANCEUR_S" +%Y-%m-%dT%H:%M:%SZ))"
# 7 bis. Garde « refus-question » (texte v1, § Liste d'arrêt ; consigne gelée R-484 à R-487 : une question refusée n'est jamais
#   reposée sous d'autres rôles) : veilleur de fond, lancé avec le noyau et arrêté par son PID à la fin de la course. Dès que la
#   course est en cours (même critère que le minuteur), il lit toutes les 2 s le journal d'appels vivant de l'unité g001 (dossier
#   du noyau de la génération, dans l'espace des organismes : <espace>/travail/<lignée>/g001.noyau/journal-appels.jsonl ;
#   lignes complètes seulement ; champs id, rôle, statut, fin — jamais un texte). Un appel est « refusé » si son statut est REFUS
#   ou si son champ `fin` porte une raison d'arrêt de sûreté (liste close des conventions du noyau : `statut_reponse` et
#   REFUS_GEMINI de collisionneur_v2.py, 213b52ef…, chargé par essaim_m3/noyau/appels.py — les raisons qui valent REFUS).
#   Règle (conv-audit, 26 octobre 2026, après le journal réel de g001 de la course M du pilote 4 : 120 appels de tâche
#   `monoculture_analytique`, cinq en REFUS, avant la question, qui vient après l'appel `moissonneur_formulation_requetes`) :
#   (a) un appel refusé de l'un des quatre rôles propres à la question ouverte de la v6.2.1 (ROLES_QUESTION_PROPRES) arrête
#   toujours ; (b) un appel refusé du rôle qui sert aussi les tâches de la banque (ROLE_TACHES_ET_QUESTION) arrête seulement
#   s'il vient après le premier appel de rôle PREFIXE_MOISSONNEUR* de g001, ou s'il est au-delà du APPELS_TACHES_MAX-ième appel
#   de ce rôle en g001 (120 tâches servies, une caste par tâche sous les bornes du pilote 4 : le 121e est une caste de la
#   question) ; sinon rien (refus de tâche) ; un refus sur un autre rôle ne fait rien. Alors il écrit le marqueur
#   garde-refus-question-v1.json, tue le noyau (son groupe de processus, puis les sessions de ses enfants directs : organisme
#   en bac à sable, entraîneur — par PID, R10), écrit la ligne « arrêt par la garde refus-question » au LANCEMENT.md (la règle
#   qui a joué à la ligne suivante et dans la pièce) : la course est fermée sans reprise (étape 8a : liste fermée poussée avec
#   ce qui existe ; le noyau tué n'écrit pas l'archive de g001, son journal vivant reste dans l'espace, archivé dans
#   ferme.tar.gz, jamais lu ; si ferme.tar.gz n'est pas écrite, les copies ouvertes restent dans ce conteneur, non poussées,
#   et la réserve « ARCHIVE FERMÉE INCOMPLÈTE » est consignée). En simulation, ESSAI_JOURNAL_GARDE remplace le journal lu
#   (R5 : cas sain, motif réel de la course M, artefacts).
ROLES_QUESTION_PROPRES="monoculture_croisee sonde_orthogonale_onsager critique_adversariale_limites arbitre_synthese_contradictoire"
ROLE_TACHES_ET_QUESTION=monoculture_analytique
PREFIXE_MOISSONNEUR=moissonneur_
APPELS_TACHES_MAX=120
FINS_SURETE="refusal SAFETY PROHIBITED_CONTENT BLOCKLIST SPII RECITATION IMAGE_SAFETY BLOCAGE_PROMPT"
JOURNAL_GARDE="$ESPACE_ATTENDU/travail/$LIGNEE/g001.noyau/journal-appels.jsonl"; JOURNAL_GARDE_ESSAI=""
if [ "$MODE" = simulation ] && [ -n "${ESSAI_JOURNAL_GARDE:-}" ]; then JOURNAL_GARDE="$ESSAI_JOURNAL_GARDE"; JOURNAL_GARDE_ESSAI=" (ESSAI : journal synthétique)"; fi
MARQUEUR_GARDE="$DS/garde-refus-question-v1.json"
tuer_noyau() {  # le noyau par son groupe (ou par son PID si le groupe n'est pas le sien), puis les sessions de ses enfants directs, par PID (R10) ; rend les PID des enfants
  local enfants p i pg
  enfants="$(pgrep -P "$PID" 2>/dev/null | tr '\n' ' ' || true)"; pg="$(groupe_de "$PID")"
  if [ "$pg" = "$PID" ]; then kill -TERM -- "-$PID" 2>/dev/null || true; else kill -TERM "$PID" 2>/dev/null || true; fi
  for i in 1 2 3 4 5; do kill -0 "$PID" 2>/dev/null || break; sleep 1; done
  if [ "$pg" = "$PID" ]; then kill -KILL -- "-$PID" 2>/dev/null || true; else kill -KILL "$PID" 2>/dev/null || true; fi
  for p in $enfants; do kill -KILL -- "-$p" 2>/dev/null || true; kill -KILL "$p" 2>/dev/null || true; done
  echo "$enfants"
}
garde_refus_question() {
  local verdict s heure enfants ID ROLE STATUT FIN REGLE
  trap 'exit 0' TERM
  while kill -0 "$PID" 2>/dev/null; do
    if course_en_cours && [ -f "$JOURNAL_GARDE" ]; then
      verdict="$("$PY" -I -c '
import json, sys
chemin, propres, role_taches, prefixe, taches_max, fins = sys.argv[1], set(sys.argv[2].split()), sys.argv[3], sys.argv[4], int(sys.argv[5]), set(sys.argv[6].split())
try:
    lignes = open(chemin, encoding="utf-8", errors="replace").read().split("\n")[:-1]
except OSError:
    sys.exit(0)
rang, moissonneur = 0, None   # rang de l appel parmi ceux du rôle des tâches ; id du premier appel moissonneur_*
for l in lignes:
    try:
        e = json.loads(l)
    except Exception:
        continue
    if not isinstance(e, dict):
        continue
    role = e.get("role") if isinstance(e.get("role"), str) else ""
    if moissonneur is None and role.startswith(prefixe):
        moissonneur = e.get("id")
    if role == role_taches:
        rang += 1
    if not (e.get("statut") == "REFUS" or e.get("fin") in fins):
        continue
    if role in propres:
        regle = "rôle propre à la question"
    elif role == role_taches and moissonneur is not None:
        regle = f"{role_taches} après le premier appel {prefixe}* de g001 ({moissonneur})"
    elif role == role_taches and rang > taches_max:
        regle = f"{role_taches} au rang {rang} > {taches_max} (au-delà des tâches servies)"
    else:
        continue
    v = {k: e.get(k) for k in ("id", "role", "statut", "fin", "espece", "etape", "categorie", "debut_utc", "fin_utc", "sha256_prompt")}
    v.update({"regle": regle, "rang_role_taches": rang if role == role_taches else None, "premier_moissonneur": moissonneur})
    print(json.dumps(v, ensure_ascii=False, sort_keys=True))
    break
' "$JOURNAL_GARDE" "$ROLES_QUESTION_PROPRES" "$ROLE_TACHES_ET_QUESTION" "$PREFIXE_MOISSONNEUR" "$APPELS_TACHES_MAX" "$FINS_SURETE" 2>/dev/null || true)"
      if [ -n "$verdict" ]; then
        trap '' TERM
        heure="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
        { printf '%s\n' "$verdict" > "$MARQUEUR_GARDE.tmp" && mv "$MARQUEUR_GARDE.tmp" "$MARQUEUR_GARDE"; } || true
        enfants="$(tuer_noyau)"
        read -r ID ROLE STATUT FIN <<< "$("$PY" -I -c 'import json, sys; e = json.loads(sys.argv[1]); print(e.get("id"), e.get("role"), e.get("statut"), e.get("fin"))' "$verdict" 2>/dev/null || echo "? ? ? ?")"
        REGLE="$("$PY" -I -c 'import json, sys; print(json.loads(sys.argv[1]).get("regle", "?"))' "$verdict" 2>/dev/null || echo "?")"
        "$PY" -I -c 'import json, sys; json.dump({"appel": json.loads(sys.argv[1]), "heure_utc": sys.argv[2], "journal": sys.argv[3], "pid_noyau": int(sys.argv[4]), "groupe_noyau": sys.argv[5], "pid_enfants_tues": [int(p) for p in sys.argv[6].split()], "regle": json.loads(sys.argv[1]).get("regle"), "roles_question_propres": sys.argv[7].split(), "role_taches_et_question": sys.argv[8], "prefixe_moissonneur": sys.argv[9], "appels_taches_max": int(sys.argv[10]), "fins_surete": sys.argv[11].split()}, open(sys.argv[12], "w", encoding="utf-8"), ensure_ascii=False, indent=1)' "$verdict" "$heure" "$JOURNAL_GARDE" "$PID" "$PGID_NOYAU" "$enfants" "$ROLES_QUESTION_PROPRES" "$ROLE_TACHES_ET_QUESTION" "$PREFIXE_MOISSONNEUR" "$APPELS_TACHES_MAX" "$FINS_SURETE" "$MARQUEUR_GARDE" 2>/dev/null || true
        note "- arrêt par la garde refus-question : appel $ID, rôle $ROLE, statut $STATUT, fin $FIN ($heure) ; course fermée sans reprise"
        note "- garde refus-question : règle « $REGLE » ; noyau $PID (groupe ${PGID_NOYAU:-illisible}) tué, enfants directs tués par PID :${enfants:+ $enfants}${enfants:- aucun} ; pièce $(basename "$MARQUEUR_GARDE") (appel, règle, heure, PID)"
        exit 0
      fi
    fi
    sleep 2 & s=$!
    wait "$s" || true
  done
}
garde_refus_question & GARDE=$!
note "- garde refus-question : veilleur PID $GARDE ; journal vivant de g001 : $JOURNAL_GARDE$JOURNAL_GARDE_ESSAI, lu toutes les 2 s dès que la course est en cours ; rôles propres à la question : $ROLES_QUESTION_PROPRES ; $ROLE_TACHES_ET_QUESTION : refus après le premier appel ${PREFIXE_MOISSONNEUR}* de g001 ou au-delà du ${APPELS_TACHES_MAX}e appel de ce rôle ; raisons d'arrêt de sûreté : $FINS_SURETE"
set +e; wait "$PID"; CODE=$?; set -e
kill "$MINUTEUR" 2>/dev/null || true
wait "$MINUTEUR" 2>/dev/null || true
GARDE_ARRET=""
if [ -f "$MARQUEUR_GARDE" ]; then wait "$GARDE" 2>/dev/null || true; GARDE_ARRET=1
else kill "$GARDE" 2>/dev/null || true; wait "$GARDE" 2>/dev/null || true; note "- garde refus-question : aucun arrêt ; veilleur arrêté par son PID ($GARDE) à la fin de la course"; fi
if [ -f "$PILOTE/course/STOP" ]; then
  note "- minuteur : STOP présent dans course/ à la fin du processus (fin de segment si le noyau a écrit un état de reprise ; sinon la course a fini sur sa dernière unité)"
else
  note "- minuteur arrêté par son PID ($MINUTEUR) à la fin de la course : STOP non posé"
fi
note "- fin du processus (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; code de retour : $CODE ; sortie standard fermée (non lue) ; sortie d'erreur : ${ERREURS#"$PILOTE"/} (lisible)"
else
  CODE=""; GARDE_ARRET=""
  cd "$R"   # v6 : l'étape 8a lance l'extrait mécanique depuis le dépôt (`python -m essaim_m3.outils.extrait_mecanique`)
  note "- CLORE=1 : aucune reprise, aucun appel ; la course arrêtée au segment $((SEGMENT - 1)) est fermée comme à sa fin (décision de Lazar)"
fi
# Fin de segment : le noyau a rendu 0 et écrit un état de reprise de plus (arrêt sur le STOP du minuteur) — la course reste
#   ouverte (course/, ferme/ : jamais lus ni poussés), le segment suivant la continue ; reprise refusée par le noyau
#   (code 9) : la course reste arrêtée et ouverte ; sinon la course a fini (ou CLORE=1) : fermeture (étape 8a)
if [ -z "$CLORE" ] && [ -z "$GARDE_ARRET" ] && [ "$SEGMENT" != 1 ] && [ "$CODE" = 9 ]; then
  note "- reprise refusée par le noyau (code 9 ; motif dans ${ERREURS#"$PILOTE"/}) : la course reste arrêtée au segment $((SEGMENT - 1)), ouverte, rien n'a tourné ; décision de Lazar : refaire SEGMENT=$SEGMENT après correction, ou SEGMENT=$SEGMENT CLORE=1"
  rmdir "$VERROU_ACTIF" 2>/dev/null || true
  (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256)
  echo "segment $SEGMENT : reprise refusée par le noyau — la course reste arrêtée et ouverte ; rien à pousser"
  exit 3
fi
if [ -z "$CLORE" ] && [ -z "$GARDE_ARRET" ] && [ -f "$PILOTE/course/manifeste-run.json" ] && [ "$CODE" = 0 ] && [ "$(compter_etats)" = "$((N_ETATS_AVANT + 1))" ]; then
  if fin_seg="$(lire_etat_reprise "$SEGMENT")"; then
    note "- état de reprise écrit par le noyau : $fin_seg"
    note "- segment $SEGMENT arrêté par STOP ; reprise attendue : SEGMENT=$((SEGMENT + 1))"
    if [ "$SEGMENT" != 1 ]; then rmdir "$VERROU_ACTIF" 2>/dev/null || true; fi
    note "- fin du lanceur (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256)
    echo "segment $SEGMENT fini sur le STOP du minuteur : course arrêtée entre deux unités, ouverte (course/ et ferme/ jamais lus ni poussés) ; reprise : SEGMENT=$((SEGMENT + 1)), avec un test de dépense frais et une ligne de dépense « segment $((SEGMENT + 1)) » ; rien à pousser avant la fin de la course"
    exit 0
  else
    note "- état de reprise de plus, mais non conforme ($fin_seg) : la course est fermée (étape 8a) — réserve"
  fi
fi

# 8a. Une course est partie (manifeste écrit) : extrait sans score, réponse et journaux recopiés (avec de vrais
#     compagnons), archive fermée (course, sortie standard, espace attendu), copies ouvertes retirées après vérification
copier() {  # copie d'un fichier archivé : vrai compagnon de la copie, compagnon d'origine gardé en « -archive »
  local src="$1" dst="$2"
  cp "$src" "$PILOTE/$dst"
  (cd "$PILOTE" && sha256sum "$dst" > "$dst.sha256")
  [ -f "$src.sha256" ] && cp "$src.sha256" "$PILOTE/$dst.sha256-archive"
  return 0
}
if [ -f "$PILOTE/course/manifeste-run.json" ]; then
  if env -u PYTHONPATH "$PY" -B -m essaim_m3.outils.extrait_mecanique --course "$PILOTE/course" --sortie "$PILOTE/extrait-mecanique-v1.json" > /dev/null 2> "$PILOTE/sortie-erreur-extrait.txt"; then
    note "- extrait mécanique : extrait-mecanique-v1.json, sha256 $(sha256sum "$PILOTE/extrait-mecanique-v1.json" | cut -d' ' -f1)"
    "$PY" -I -c 'import json, sys; x = json.load(open(sys.argv[1])); m = x["manifeste"]; r = x.get("rapport") or {}; print("- vérification après départ (extrait) : isolation " + json.dumps(m.get("isolation"), ensure_ascii=False) + " ; collisionneur conforme : " + str(m.get("collisionneur_conforme")) + " ; commit " + str(m.get("commit")) + " ; sha256_code_noyau " + str(m.get("sha256_code_noyau")) + " ; espace " + str(m.get("espace_organismes")) + " ; sources de moisson " + json.dumps(m.get("sources_moisson"), ensure_ascii=False) + " ; clés présentes au manifeste — web : " + str(m.get("cle_brave_presente")) + ", OpenAlex : " + str(m.get("cle_openalex_presente")) + ", Semantic Scholar : " + str(m.get("cle_s2_presente")) + " ; temps par ronde de conception " + str((m.get("budget_conception") or {}).get("temps_max_s")) + " s ; dépense du noyau " + str(r.get("depense_totale_usd")) + " USD (à rapprocher de la console, P2C1-05)")' "$PILOTE/extrait-mecanique-v1.json" >> "$L"
  else
    note "- extrait mécanique : REFUSÉ par l'outil (aucune écriture ; sortie-erreur-extrait.txt) — rapporté ; la course n'est pas ouverte"
  fi
  ESPACE="$("$PY" -I -c 'import json, sys; print(json.load(open(sys.argv[1])).get("espace_organismes") or "")' "$PILOTE/course/manifeste-run.json")"
  [ "$ART" = espace ] && ESPACE="$(mktemp -d)"
  for g in g000 g001 g002 g003 c001 c002 c003 c004 c005 c006; do
    a="$PILOTE/course/archive/$LIGNEE/$g/journal-appels.jsonl"
    if [ -f "$a" ] && [ ! -L "$a" ]; then
      copier "$a" "journal-appels-$g.jsonl"
      note "- journal des appels $g : journal-appels-$g.jsonl, sha256 $(cut -d' ' -f1 < "$PILOTE/journal-appels-$g.jsonl.sha256")"
    else
      note "- journal des appels $g : absent ou non ordinaire dans l'archive (génération non tournée, ou anomalie) — rapporté"
    fi
  done
  rq="$PILOTE/course/archive/$LIGNEE/g001/reponse-question.md"
  if [ -f "$rq" ] && [ ! -L "$rq" ]; then
    copier "$rq" "reponse-question-g001.md"
    note "- réponse à la question : reponse-question-g001.md, sha256 $(cut -d' ' -f1 < "$PILOTE/reponse-question-g001.md.sha256")"
  else
    note "- réponse à la question : aucune pièce archivée (voir l'extrait : champ question_ouverte de g001, ou g001 non tournée)"
  fi
  args=(-C "$PILOTE" course ferme)
  espace_a_retirer=""
  if [ -n "$ESPACE" ] && [ -d "$ESPACE" ] && [ "$(cd "$ESPACE" && pwd -P)" != "$(cd "$PILOTE/course" && pwd -P)" ]; then
    if [ "$ESPACE" = "$ESPACE_ATTENDU" ]; then args+=(-C / "${ESPACE#/}"); espace_a_retirer="$ESPACE"
    else note "- espace des organismes du manifeste ($ESPACE) ≠ espace attendu ($ESPACE_ATTENDU) : ni archivé ni retiré, jamais lu — réserve"; fi
  fi
  set +e; tar --warning=no-file-ignored -czf "$PILOTE/ferme.tar.gz" "${args[@]}" 2> "$PILOTE/sortie-erreur-tar.txt"; code_tar=$?; set -e
  (cd "$PILOTE" && sha256sum ferme.tar.gz > ferme.tar.gz.sha256)
  [ "$ART" = archive ] && printf x > "$PILOTE/course/artefact-apres-archive.txt"
  n_archive="$(tar -tzf "$PILOTE/ferme.tar.gz" | wc -l)"
  n_disque="$( { (cd "$PILOTE" && find course ferme ! -type s); if [ -n "$espace_a_retirer" ]; then (cd / && find "${espace_a_retirer#/}" ! -type s); fi; } | wc -l)"
  if [ "$code_tar" = 0 ] && [ "$n_archive" = "$n_disque" ]; then
    rm -rf "$PILOTE/course" "$PILOTE/ferme"; [ -n "$espace_a_retirer" ] && [ "$espace_a_retirer" = "$ESPACE_ATTENDU" ] && rm -rf "$espace_a_retirer"
    note "- archive fermée : ferme.tar.gz (course, sortie standard, espace des organismes), sha256 $(cut -d' ' -f1 < "$PILOTE/ferme.tar.gz.sha256"), $n_archive entrées = $n_disque sur disque ; copies ouvertes retirées"
  else
    note "- ARCHIVE FERMÉE INCOMPLÈTE : code tar $code_tar, $n_archive entrées contre $n_disque sur disque — copies ouvertes gardées dans ce conteneur (écartées du dépôt par .gitignore), jamais lues ni poussées — réserve"
  fi
# 8b. Aucune course n'est partie (refus avant le manifeste, ou exception) : rien n'est fermé ; la tentative suivante est
#     permise. Le noyau a pu créer des dossiers vides (course/, son espace) : vérifiés sans fichier ordinaire, laissés.
else
  n_course="$( [ -d "$PILOTE/course" ] && find "$PILOTE/course" -type f | wc -l || echo 0)"
  n_sortie="$(wc -c < "$SORTIE_FERMEE")"
  n_espace="$( [ -d "$ESPACE_ATTENDU" ] && find "$ESPACE_ATTENDU" -type f | wc -l || echo 0)"
  rmdir "$VERROU" 2>/dev/null || true
  if [ -f "$MARQUEURS/$NOM" ] && grep -q "^$PILOTE " "$MARQUEURS/$NOM"; then rm -f "$MARQUEURS/$NOM"; note "- marqueur de départ retiré (aucune course partie) ; verrou retiré"; fi
  if [ "$n_course" = 0 ] && [ "$n_sortie" = 0 ] && [ "$n_espace" = 0 ]; then
    note "- aucune course partie (pas de manifeste ; code $CODE ; motif dans sortie-erreur-lanceur.txt) ; course/ et l'espace prévu sans aucun fichier, sortie standard vide : laissés tels quels (dossiers vides) ; tentative suivante permise : TENTATIVE=$((TENTATIVE + 1))"
  else
    set +e; tar --warning=no-file-ignored -czf "$PILOTE/refus-avant-manifeste-v1.tar.gz" -C "$PILOTE" course ferme $( [ -d "$ESPACE_ATTENDU" ] && echo "-C / ${ESPACE_ATTENDU#/}" ) 2> "$PILOTE/sortie-erreur-tar.txt"; set -e
    (cd "$PILOTE" && sha256sum refus-avant-manifeste-v1.tar.gz > refus-avant-manifeste-v1.tar.gz.sha256)
    note "- aucune course partie (pas de manifeste ; code $CODE) mais $n_course fichier(s) dans course/, $n_espace dans l'espace, sortie standard de $n_sortie octets : fermés dans refus-avant-manifeste-v1.tar.gz, jamais lus — réserve ; tentative suivante permise : TENTATIVE=$((TENTATIVE + 1))"
  fi
fi
[ "$ART" = imprevu ] && printf 'x\n' > "$PILOTE/fichier-imprevu.txt"
note "- fin du lanceur (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"

# 9. Ce qui est poussé : une liste fermée de noms ; tout autre fichier est consigné et n'est pas poussé
for f in "$PILOTE"/sortie-erreur-lanceur.txt "$PILOTE"/segment-*-t*/sortie-erreur-lanceur.txt; do if [ -f "$f" ]; then (cd "$(dirname "$f")" && sha256sum sortie-erreur-lanceur.txt > sortie-erreur-lanceur.txt.sha256); fi; done
for f in sortie-erreur-extrait.txt sortie-erreur-tar.txt; do [ -f "$PILOTE/$f" ] && (cd "$PILOTE" && sha256sum "$f" > "$f.sha256"); done
for f in "$PILOTE"/garde-refus-question-v1.json "$PILOTE"/segment-*-t*/garde-refus-question-v1.json; do if [ -f "$f" ]; then (cd "$(dirname "$f")" && sha256sum garde-refus-question-v1.json > garde-refus-question-v1.json.sha256); fi; done
permis_re='^(\.gitignore|LANCEMENT\.md|LANCEMENT\.md\.sha256|sortie-erreur-(lanceur|extrait|tar)\.txt(\.sha256)?|essais-v1\.(xml|txt)|extrait-mecanique-v1\.json(\.sha256)?|reponse-question-g001\.md(\.sha256|\.sha256-archive)?|journal-appels-(g00[0-3]|c0[0-9][0-9])\.jsonl(\.sha256|\.sha256-archive)?|question\.md|registre-go\.md|test-depense-[^/]+|garde-refus-question-v1\.json(\.sha256)?|organisme/.+|ferme\.tar\.gz(\.sha256)?|refus-avant-manifeste-v1\.tar\.gz(\.sha256)?|segment-[0-9]+-t[0-9]+/(registre-go\.md|test-depense-[^/]+|essais-v1\.(xml|txt)|sortie-erreur-lanceur\.txt(\.sha256)?|garde-refus-question-v1\.json(\.sha256)?))$'
imprevus="$(cd "$PILOTE" && find . \( -path ./course -o -path ./ferme \) -prune -o -type f -print | sed 's#^\./##' | grep -Ev "$permis_re" | grep -Ev '^(A-POUSSER-v1\.txt(\.sha256)?|EMPREINTES-pilote-v1\.txt(\.sha256)?)$' || true)"
[ -z "$imprevus" ] || note "- fichiers imprévus, NON poussés (consignés) : $(echo $imprevus)"
(cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256)
(cd "$PILOTE" && find . \( -path ./course -o -path ./ferme \) -prune -o -type f -print | sed 's#^\./##' | grep -E "$permis_re" | sort > A-POUSSER-v1.txt \
   && printf 'A-POUSSER-v1.txt\nA-POUSSER-v1.txt.sha256\nEMPREINTES-pilote-v1.txt\nEMPREINTES-pilote-v1.txt.sha256\n' >> A-POUSSER-v1.txt \
   && sha256sum A-POUSSER-v1.txt > A-POUSSER-v1.txt.sha256 \
   && grep -Ev '^EMPREINTES-pilote-v1\.txt(\.sha256)?$' A-POUSSER-v1.txt | xargs sha256sum > EMPREINTES-pilote-v1.txt \
   && sha256sum EMPREINTES-pilote-v1.txt > EMPREINTES-pilote-v1.txt.sha256)
echo "pilote fini${GARDE_ARRET:+ (arrêt par la garde refus-question : course fermée sans reprise)} : $PILOTE — à pousser : exactement les fichiers de A-POUSSER-v1.txt (branche pilotes/$NOM) ; jamais course/ ni ferme/"
exit 0
