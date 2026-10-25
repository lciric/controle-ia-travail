#!/usr/bin/env bash
# Lanceur du troisième pilote descriptif « organismes assistés de Gemini, v5.3 puis v6, chacun seul, mêmes bornes que la
# course M du second pilote, question M à g001 », une course par appel (COURSE=v5-3, puis COURSE=v6) — v1, dérivé du
# lanceur scellé du second pilote (`lancer_pilote2_gemini_v5_2_v5.sh`, `83f8b9cf…`) par `deriver_lanceur_pilote3_v1.py`
# (remplacements exacts ; écart consigné dans `diff-lanceur-v5-vers-pilote3-v1.txt`). Ce qui change par rapport à la
# source : (i) deux courses, chacune avec son objet (commit, arbre, nombre de fichiers, lignée) et la même question M v2 ;
# (ii) GO-2026-10-25-02 ; (iii) l'étape (0) ne lit plus « la course précédente » mais la **course M de référence** du
# second pilote (`REFERENCE_M`), à laquelle elle applique telle quelle la liste close « M saine » du lanceur source (avec
# le nom, l'empreinte et la lignée du lanceur et de l'objet de M, et la graine M du texte scellé du second pilote) : une
# course du pilote 3 ne part qu'après une course M finie, fermée et saine ; la ligne de dépense porte les 16 premiers
# caractères de l'empreinte des empreintes de M ; (iv) chemins permis après b1c7f4b6 : ceux du second pilote et ceux du
# pilote 3. Tout le reste (gardes, environnement fermé, passerelle, essais du noyau, fermeture, liste de ce qui est
# poussé) est le texte du lanceur source, inchangé.
# Objets : v5.3 = `canal/gemini-organisme-v5-3`, commit `4ecba58`, dossier `organisme/`, arbre `6251ab21…`, 22 fichiers ;
# v6 = `canal/gemini-organisme-v6`, commit `7cd7508`, arbre `940c59c3…`, 24 fichiers ; lignées « assistées » (déclarées).
# Ces deux commits portent aussi l'arbre de la relève : seul `organisme/` en est extrait (`git archive`), jamais une
# extraction ni une exécution du reste. Code `b1c7f4b6`. Le dépôt de lancement doit contenir ces commits et ceux des
# questions (`git fetch origin canal/gemini-organisme-v5-3 canal/gemini-organisme-v6 canal/conv-audit-n04 main`). Chaque
# appel de ce lanceur est une commande de fond de la session avec le délai maximal (7 200 000 ms), jamais `nohup`, `&` ni
# `setsid`. Met en œuvre le préenregistrement scellé
# `essaim-m3-refonte-v1/prereg/pilote3-gemini-organisme-v5-3-v6-v1.md` (ou la version qui le remplace et cite ce script).
#
# Usage :
#   MODE=reel COURSE=v5-3 DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO_USD=… \
#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE="…" CLE_ANTHROPIC=NOM CLE_GEMINI=NOM [CLE_BRAVE=NOM] \
#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M> \
#       bash lancer_pilote3_gemini_v5_3_v6_v1.sh
#   MODE=reel COURSE=v6 … (même forme)
#   MODE=simulation COURSE=… DEPOT=… PYTHON=… GRAINE=… [REFERENCE_M=… PILOTE_RACINE=… REGISTRE_GO_SOURCE=…
#       DEPENSES_SOURCE=… RESTE_GO_USD=… PREREG=… PREREG_SHA256=… APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=…
#       ESSAI_ARTEFACT=… ESSAI_JUNIT_EXISTANT=… ESSAI_RESUME_EXISTANT=… ESSAI_EXIGER_HEURE=1 ESSAI_PASSERELLE_PY=…]
#
# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course ou la sortie standard ; arrêter un
# processus (R10 : PID consigné ; une course voisine est détectée, jamais arrêtée) ; écraser un dossier (R12) ; lancer
# une seconde course de même nom (R3).
set -euo pipefail
set +x
refus_tot() { echo "REFUS : $*" >&2; exit 2; }   # refus avant que le dossier du pilote existe

MODE="${MODE:?MODE=reel ou MODE=simulation}"
[ "$MODE" = reel ] || [ "$MODE" = simulation ] || refus_tot "MODE inconnu : $MODE"
COURSE="${COURSE:?COURSE=v5-3 ou COURSE=v6}"
# Question M v2 épurée (la même que celle de la course M du second pilote), pour les deux courses
COMMIT_QUESTION=a15809b816b6c967b6c3cf21877e350bfe676dca
CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-gemini-maieutique-vs-coercition-organismes-v2.md
SHA_QUESTION=8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd
case "$COURSE" in
  v5-3)
    NOM="pilote3-gemini-v5-3-maieutique-v1"; INDICE_GRAINE=0
    COMMIT_ORGANISME=4ecba58bcaa7dc3abe82c54fc38ee7285620bdf6
    ARBRE_ORGANISME=6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753
    N_FICHIERS_ORGANISME=22
    LIGNEE="gemini-organisme-v5-3";;
  v6)
    NOM="pilote3-gemini-v6-maieutique-v1"; INDICE_GRAINE=1
    COMMIT_ORGANISME=7cd7508287efa6fd667eaca7dffe23666f12692f
    ARBRE_ORGANISME=940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a
    N_FICHIERS_ORGANISME=24
    LIGNEE="gemini-organisme-v6";;
  *) refus_tot "COURSE inconnue : $COURSE (v5-3 ou v6)";;
esac
PY="${PYTHON:-python3}"
ART="${ESSAI_ARTEFACT:-}"
SOURCE_GEMINI=""
SOURCE_ANTHROPIC=""
SOURCE_BRAVE=""
SOURCE_OPENALEX=""
SOURCE_S2=""
if [ "$MODE" = reel ]; then
  for v in PILOTE_RACINE SUFFIXE_ESSAI REGISTRE_GO_SOURCE DEPENSES_SOURCE ESSAI_ARTEFACT ESSAI_JUNIT_EXISTANT ESSAI_RESUME_EXISTANT ESSAI_EXIGER_HEURE ESSAI_PASSERELLE_PY ESSAIM_M3_ESPACE; do
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
GO_ID=GO-2026-10-25-02
USD_GEN=30      # par génération (mêmes bornes que la course M ; décision (b) de Lazar, 25 octobre 10:17 Paris)
USD_COURSE=60   # par course ; deux courses : 120 USD au plus (GO-2026-10-25-02, mot direct de Lazar dans la session de session-depot)
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

COMMIT_CODE=b1c7f4b697e846a2fe904fa90a36148587756dd5
COMMIT_LIENS=4967734a62a0b10c3b5cd6360e21924f015053fd
COMMIT_CREDIT=90595ffb53b30c65c66be807215a998998b701fc
[ "$ART" = commit ] && COMMIT_QUESTION=0123456789abcdef0123456789abcdef01234567
SHA_BANQUE=f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc
SHA_MISSION=bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e
SHA_COLLISIONNEUR=213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
[ "$ART" = banque ] && SHA_BANQUE=0000
[ "$ART" = mission ] && SHA_MISSION=0000
CODE_NOYAU_PROPRE=37acdcaaaded746b7f7599f17e8149bdd773e372f3a3b0782db7b73882acf8a3
N_ESSAIS=141
ESSAIS_CITES="test_fichiers_lecture_et_copie_sans_lien test_depot_ne_suit_aucun_lien_de_l_organisme test_organisme_poseur_de_liens_ne_voit_rien_du_noyau test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score test_extrait_mecanique_sain_puis_artefacts test_mode_reel_refuse_sans_go test_mode_reel_refuse_anthropic_base_url test_bac_a_sable_isolation_reseau_refusee_si_indisponible test_appels_paralleles_plafond_tenu_au_pire_cas test_organisme_gourmand_recoit_plafond_sans_exception test_ce312_doit_arreter_et_raison_juste test_bac_a_sable_exception_et_delai test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee test_ce305_credit_epuise_arrete_la_course test_ce307_anomalie_journal_absent test_relance_puis_reprise_remet_le_compteur_a_zero test_fichier_stop_arrete_la_boucle test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus test_r395_credit_epuise_rendu_en_400_arrete_la_course test_cl5_01_banque_cachee_a_l_organisme test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course test_sources_reelles_de_moisson_si_reseau test_moisson_de_bout_en_bout_en_simulation test_ce311_garde_de_temps_compte_la_moisson test_ce305_sources_moisson_au_manifeste_et_bras_apparie test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait test_r410_cles_openalex_et_s2_en_entete_jamais_dans_l_adresse"
# Chemins que les commits postérieurs à b1c7f4b6 peuvent toucher : le texte du second pilote, ses pièces et ses
# contre-lectures ; ce texte, ses pièces et ses contre-lectures ; dossier des pilotes
PERMIS_APRES_CODE='^essaim-m3-refonte-v1/prereg/(pilote2-gemini-organisme-v5-2-v[0-9]+\.md(\.sha256)?|pieces-pilote2-gemini-v5-2/.+|contre-lectures/pilote2-gemini-organisme-v5-2-v[0-9]+-cl[0-9]+\.md(\.sha256)?|pilote3-gemini-organisme-v5-3-v6-v[0-9]+\.md(\.sha256)?|pieces-pilote3-gemini-v5-3-v6/.+|contre-lectures/pilote3-gemini-organisme-v5-3-v6-v[0-9]+-cl[0-9]+\.md(\.sha256)?)$'

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
if raison_r3="$(course_deja_partie)"; then refus_tot "$raison_r3 (R3 : jamais de seconde course)"; fi
if [ "$MODE" = reel ]; then
  distante="$(git -C "$DEPOT" ls-remote --heads origin "pilotes/$NOM" 2>/dev/null)" || refus_tot "lecture du dépôt distant impossible (git ls-remote) : R3 non vérifiable, le pilote attend"
  [ -z "$distante" ] || refus_tot "la branche pilotes/$NOM existe déjà sur le dépôt distant (R3)"
fi
[ -e "$PILOTE" ] && refus_tot "$PILOTE existe déjà (R12 ; après un refus avant le manifeste : TENTATIVE=$((TENTATIVE + 1)))"
mkdir -p "$RACINE_PILOTES"
mkdir "$VERROU" 2>/dev/null || refus_tot "verrou $VERROU présent : un autre lanceur de cette course tourne, ou un lanceur s'est interrompu (examiner, puis retirer le verrou à la main)"
mkdir -m 700 "$PILOTE"
mkdir -m 700 "$PILOTE/ferme"
printf 'course/\nferme/\n' > "$PILOTE/.gitignore"   # jamais ajoutés au dépôt, même par un `git add -A`
L="$PILOTE/LANCEMENT.md"
refus() { echo "REFUS : $*" >&2; echo "- refus : $* ($(date -u +%Y-%m-%dT%H:%M:%SZ)) ; verrou retiré" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256); rmdir "$VERROU" 2>/dev/null || true; exit 2; }
note() { echo "$*" >> "$L"; }
trap 'c=$?; echo "ÉCHEC inattendu (code $c) à la ligne $LINENO : arrêt" >&2; echo "- échec inattendu (code $c) à la ligne $LINENO ($(date -u +%Y-%m-%dT%H:%M:%SZ)) ; verrou $VERROU laissé (à examiner)" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256) || true' ERR
if [ "$MODE" = reel ]; then SOURCE_REG="origin/main"; else SOURCE_REG="${REGISTRE_GO_SOURCE:-aucune (simulation)} ; dépenses : ${DEPENSES_SOURCE:-aucune (simulation)}"; fi
SHA_LANCEUR="$(sha256sum "$0" | cut -d' ' -f1)"
{
  echo "# Lancement du pilote $NOM ($MODE, tentative $TENTATIVE)"
  echo
  echo "- début (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; hôte : $(hostname) ; utilisateur : $(id -u)"
  echo "- course : $COURSE ; dossier du pilote : $PILOTE (0700, à root)"
  echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD) (c'est le « commit » que le manifeste consignera)"
  echo "- lanceur : $(basename "$0"), sha256 $SHA_LANCEUR"
  echo "- source des registres : $SOURCE_REG"
  if [ -n "$voisines" ]; then echo "- course(s) voisine(s) du noyau détectée(s) dans ce conteneur, à un autre décalage d'utilisateurs que $DECALAGE_UID :$voisines (détection seulement, rien n'est arrêté)"
  else echo "- aucune course voisine du noyau dans ce conteneur au départ (détection par pgrep)"; fi
  [ -n "$reserve_voisines" ] && echo "- RÉSERVE : course(s) voisine(s) à un décalage des essais du noyau (0, 700, 800) :$reserve_voisines — pendant les essais d'avant départ (≈ 3 minutes), des processus d'essai tournent sous les utilisateurs 60000 et suivants, 60700–60701, 60800–60830 et 60900 et partagent ces utilisateurs avec elle(s)"
} > "$L"
[ "$MODE" = simulation ] && [ -n "$ART" ] && note "- ESSAI : artefact « $ART » (simulation)"

# 0. Course M de référence : une course du pilote 3 ne part qu'après une course M du second pilote finie, fermée et
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
  [ -n "${REFERENCE_M:-}" ] || refus "REFERENCE_M non défini : une course du pilote 3 ne part qu'après une course M saine (dossier du pilote de la course M)"
  SP="$REFERENCE_M"
  [ -d "$SP" ] || refus "REFERENCE_M $SP absent : une course du pilote 3 ne part qu'après M"
  SP="$(cd "$SP" && pwd -P)"
  if [ "$MODE" = reel ]; then
    case "$SP/" in /root/*|/home/*) ;; *) refus "REFERENCE_M $SP hors de /root et de /home";; esac
    [[ "$(basename "$SP")" =~ ^pilote2-gemini-v5-2-1-maieutique-v1(-tentative[0-9]+)?$ ]] || refus "REFERENCE_M $SP : nom autre que pilote2-gemini-v5-2-1-maieutique-v1[-tentativeN]"
  fi
  [ -f "$SP/EMPREINTES-pilote-v1.txt" ] && [ -f "$SP/EMPREINTES-pilote-v1.txt.sha256" ] || refus "empreintes de M absentes : une course du pilote 3 ne part qu'après une course M finie et fermée"
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
  grep -q "graine de la course maieutique = $GRAINE_S_MANIFESTE\b" "$PREREG_M" || refus "la course M a tourné avec la graine $GRAINE_S_MANIFESTE, qui n'est pas la graine M du texte scellé du second pilote"
  note "- course M de référence : $SP ; $issue_s ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 $EMP_S) ; graine $GRAINE_S_MANIFESTE = graine M du texte scellé du second pilote (d2944654…)"
fi

# 1. Code identique à b1c7f4b6 (commit et arbre de travail, collisionneur compris) ; commits postérieurs limités aux pièces
#    du pilote ; rien de non suivi ni de modifié sous essaim-m3-refonte-v1 hors des dossiers de pilotes ; ancêtres ;
#    banque, mission, collisionneur
for c in "$COMMIT_CODE" "$COMMIT_LIENS" "$COMMIT_CREDIT" "$COMMIT_ORGANISME" "$COMMIT_QUESTION"; do
  git -C "$DEPOT" cat-file -e "$c^{commit}" 2>/dev/null || refus "commit $c absent du dépôt (git fetch)"
done
P="essaim-m3-refonte-v1/essaim_m3 essaim-m3-refonte-v1/tests collisionneur-v2.5-banc-jev-travail"
# shellcheck disable=SC2086
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" HEAD -- $P || refus "code de HEAD différent de b1c7f4b6 (essaim_m3, tests ou collisionneur)"
# shellcheck disable=SC2086
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" -- $P || refus "arbre de travail différent de b1c7f4b6 (essaim_m3, tests ou collisionneur)"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_CODE" HEAD || refus "b1c7f4b6 non ancêtre de HEAD"
hors_pieces="$(git -C "$DEPOT" diff --name-only "$COMMIT_CODE" HEAD | grep -Ev "$PERMIS_APRES_CODE" || true)"
[ -z "$hors_pieces" ] || refus "commits postérieurs à b1c7f4b6 hors des pièces du pilote : $(echo $hors_pieces)"
rel_pilotes="$(realpath --relative-to="$DEPOT" "$RACINE_PILOTES" 2>/dev/null || echo "")"
inattendus="$(git -C "$DEPOT" status --porcelain --ignored --untracked-files=all -- essaim-m3-refonte-v1 collisionneur-v2.5-banc-jev-travail \
  | grep -v '__pycache__' | grep -v '/\.pytest_cache/' | { if [ -n "$rel_pilotes" ] && [ "${rel_pilotes#..}" = "$rel_pilotes" ]; then grep -v " $rel_pilotes/" ; else cat; fi; } || true)"
[ -z "$inattendus" ] || refus "fichiers non suivis ou modifiés sous essaim-m3-refonte-v1 ou le collisionneur : $(echo $inattendus)"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_LIENS" HEAD || refus "correctif des liens 4967734 non ancêtre de HEAD"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_CREDIT" HEAD || refus "R-395 (90595ffb, arrêt sur crédit épuisé en 400) non ancêtre de HEAD"
[ "$(sha256sum "$R/banque/banque-confrontation-v1.json" | cut -d' ' -f1)" = "$SHA_BANQUE" ] || refus "empreinte de la banque ≠ f1387a20…"
[ "$(sha256sum "$R/MISSION-v1.md" | cut -d' ' -f1)" = "$SHA_MISSION" ] || refus "empreinte de la mission ≠ bd2c6a15…"
[ "$(sha256sum "$DEPOT/collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py" | cut -d' ' -f1)" = "$SHA_COLLISIONNEUR" ] || refus "empreinte du collisionneur ≠ 213b52ef…"
note "- code : identique à b1c7f4b6 (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque $SHA_BANQUE ; mission $SHA_MISSION ; collisionneur $SHA_COLLISIONNEUR"
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

# 2. Préenregistrement scellé (réel ; en simulation si PREREG est donné) ; graine recalculée depuis l'entropie
if [ "$MODE" = reel ] || [ -n "${PREREG:-}" ]; then
  PREREG="${PREREG:?PREREG=chemin du préenregistrement scellé}"; PREREG_SHA256="${PREREG_SHA256:?}"
  [ "$(sha256sum "$PREREG" | cut -d' ' -f1)" = "$PREREG_SHA256" ] || refus "empreinte du préenregistrement ≠ PREREG_SHA256"
  [ -f "$PREREG.sha256" ] && [ "$(cut -d' ' -f1 < "$PREREG.sha256")" = "$PREREG_SHA256" ] || refus "compagnon .sha256 du préenregistrement absent ou différent"
  grep -q "graine de la course $COURSE = $GRAINE\b" "$PREREG" || refus "la graine $GRAINE de la course $COURSE n'est pas écrite dans le préenregistrement scellé"
  if grep -q "<<[A-Z0-9_]*>>" "$PREREG"; then refus "marqueurs <<…>> restants : préenregistrement non scellé"; fi
  grep -q "$SHA_LANCEUR" "$PREREG" || refus "le préenregistrement ne cite pas l'empreinte de ce lanceur"
  E_TEXTE="$(grep -Eo 'entropie E = [0-9]+' "$PREREG" | head -1 | grep -Eo '[0-9]+$' || true)"
  [ -n "$E_TEXTE" ] || refus "entropie E absente du préenregistrement"
  g_calc="$("$PY" -I -c 'import sys, numpy; e, i = int(sys.argv[1]), int(sys.argv[2]); print(int(numpy.random.SeedSequence(e).spawn(2)[i].generate_state(1, dtype=numpy.uint64)[0]))' "$E_TEXTE" "$INDICE_GRAINE")"
  [ "$g_calc" = "$GRAINE" ] || refus "graine $GRAINE ≠ celle de SeedSequence(E).spawn(2)[$INDICE_GRAINE] = $g_calc"
  note "- préenregistrement : $PREREG, sha256 $PREREG_SHA256 (compagnon conforme), graine $GRAINE de la course $COURSE écrite et recalculée depuis l'entropie du texte, empreinte du lanceur citée"
fi

# 3. Organisme de la course (v5.3 ou v6, dossier organisme/ seul) et question, extraits des commits cités, vérifiés
git -C "$DEPOT" archive "$COMMIT_ORGANISME" organisme | tar -x -C "$PILOTE"
ORG="$PILOTE/organisme"
[ "$ART" = organisme ] && printf ' ' >> "$ORG/principal.py"
[ "$ART" = nombre ] && rm -f "$ORG/CONCEPTION.md"
n_fichiers="$(find "$ORG" -type f | wc -l)"
[ "$n_fichiers" = "$N_FICHIERS_ORGANISME" ] || refus "organisme : $n_fichiers fichiers au lieu de $N_FICHIERS_ORGANISME"
empreinte_arbre() { (cd "$R" && env -u PYTHONPATH "$PY" -B -I -c 'import pathlib, sys; sys.path.insert(0, "."); from essaim_m3.noyau import boucle; print(boucle.empreinte_arbre(pathlib.Path(sys.argv[1])))' "$1"); }
[ "$(empreinte_arbre "$ORG")" = "$ARBRE_ORGANISME" ] || refus "empreinte d'arbre de l'organisme ≠ ${ARBRE_ORGANISME:0:8}…"
git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" > "$PILOTE/question.md"
[ "$ART" = question ] && printf '\n' >> "$PILOTE/question.md"
[ "$(sha256sum "$PILOTE/question.md" | cut -d' ' -f1)" = "$SHA_QUESTION" ] || refus "empreinte de la question ≠ ${SHA_QUESTION:0:8}…"
note "- organisme : $N_FICHIERS_ORGANISME fichiers, empreinte d'arbre $ARBRE_ORGANISME ; question ($COURSE) : sha256 $SHA_QUESTION"

# 4. Registre des GO : une ligne « | GO-2026-10-25-02 | » qui porte « calcul », l'empreinte (8 premiers caractères) de
#    la question et celle de l'objet de la course ; dépense consignée avant (une ligne nommant la course, le GO et
#    l'empreinte des empreintes de M) ; reste ≥ plafond de la course
if [ "$MODE" = reel ] || [ -n "${REGISTRE_GO_SOURCE:-}" ]; then
  if [ "$MODE" = reel ]; then git -C "$DEPOT" show origin/main:registres/go.md > "$PILOTE/registre-go.md"; else cp "$REGISTRE_GO_SOURCE" "$PILOTE/registre-go.md"; fi
  grep "^| $GO_ID |" "$PILOTE/registre-go.md" | grep 'calcul' | grep "${SHA_QUESTION:0:8}" | grep -q "${ARBRE_ORGANISME:0:8}" \
    || refus "aucune ligne « | $GO_ID | » qui porte à la fois le type calcul, l'empreinte de la question ${SHA_QUESTION:0:8}… et l'empreinte de l'organisme ${ARBRE_ORGANISME:0:8}… (GO non inscrit pour cette course sur cet objet)"
  if [ "$MODE" = reel ]; then dep="$(git -C "$DEPOT" show origin/main:registres/depenses.md)"; else dep="$(cat "${DEPENSES_SOURCE:?DEPENSES_SOURCE en simulation avec REGISTRE_GO_SOURCE}")"; fi
  echo "$dep" | grep "$NOM" | grep -q "$GO_ID" || refus "lancement non consigné avant dans registres/depenses.md (une ligne nommant $NOM et $GO_ID)"
  if [ -n "$EMP_S" ]; then
    echo "$dep" | grep "$NOM" | grep "$GO_ID" | grep -q "${EMP_S:0:16}" || refus "la ligne de dépense de la course $COURSE ne porte pas l'empreinte des empreintes de M (${EMP_S:0:16}…), écrite après la fin de M"
  fi
  reste="${RESTE_GO_USD:?RESTE_GO_USD=reste disponible sur $GO_ID avant cette course, en USD}"
  "$PY" -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= float(sys.argv[2]) else 1)' "$reste" "$USD_COURSE" || refus "reste sur $GO_ID = $reste USD < $USD_COURSE"
  note "- registre : une ligne $GO_ID de type calcul portant l'empreinte de la question ($COURSE) et celle de l'organisme (${ARBRE_ORGANISME:0:8}…) ; dépense consignée avant ; reste déclaré $reste USD ≥ $USD_COURSE (vérification du lanceur)"
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
  cp "$TD" "$PILOTE/test-depense-$(basename "$TD")"
  note "- test de dépense : $(basename "$TD"), sha256 $(sha256sum "$TD" | cut -d' ' -f1) — $verdict (réalité des appels attestée par l'outil de session-depot ; le script vérifie la pièce)"
  attest="$(printf '%s' "${RECHARGE_ATTESTEE:-}" | tr -d '\n\r' | cut -c1-300)"
  [ -n "$attest" ] && note "- recharge automatique attestée : « $attest »"
fi

# 6. Essais (en root en réel), puis code sans bytecode et empreinte du noyau
if [ "$MODE" = simulation ] && [ -n "${ESSAI_JUNIT_EXISTANT:-}" ]; then
  cp "$ESSAI_JUNIT_EXISTANT" "$PILOTE/essais-v1.xml"; resultat="${ESSAI_RESUME_EXISTANT:?}"
  note "- ESSAI : rapport JUnit repris de $ESSAI_JUNIT_EXISTANT (simulation)"
else
  resultat="$( (cd "$R" && env -u PYTHONPATH -u ESSAIM_M3_COLLISIONNEUR -u ESSAIM_M3_CACHER PYTHONDONTWRITEBYTECODE=1 "$PY" -m pytest -q -p no:cacheprovider --junitxml "$PILOTE/essais-v1.xml" ${PYTEST_ARGS:-} 2>&1) | tail -1 || true)"
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
t.write(f)' "$ART" "$PILOTE/essais-v1.xml"
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
sys.exit(1 if problemes else 0)' "$resultat" "$PILOTE/essais-v1.xml" "$ESSAIS_CITES" "$N_ESSAIS" > "$PILOTE/essais-v1.txt" || refus "essais : $(cat "$PILOTE/essais-v1.txt") (résumé : « $resultat »)"
note "- essais : $(cat "$PILOTE/essais-v1.txt") ; arguments : « ${PYTEST_ARGS:-aucun} » ; les $(echo $ESSAIS_CITES | wc -w) essais cités ont passé ici (dont la recherche réelle sur arXiv)"
find "$R/essaim_m3" "$R/tests" "$DEPOT/collisionneur-v2.5-banc-jev-travail" -name __pycache__ -prune -exec rm -rf {} +
[ "$ART" = bytecode ] && mkdir -p "$R/essaim_m3/noyau/__pycache__" && printf x > "$R/essaim_m3/noyau/__pycache__/x.pyc"
code_noyau="$(empreinte_arbre "$R/essaim_m3/noyau")"
[ "$code_noyau" = "$CODE_NOYAU_PROPRE" ] || refus "empreinte du noyau nettoyé $code_noyau ≠ 37acdcaa…"
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
if raison_r3="$(course_deja_partie)"; then refus "$raison_r3 (R3, au départ)"; fi
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
mkdir -p "$MARQUEURS"
( set -o noclobber; printf '%s %s\n' "$PILOTE" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$MARQUEURS/$NOM" ) 2>/dev/null || refus "marqueur de départ $MARQUEURS/$NOM déjà posé (R3)"
note "- marqueur de départ : $MARQUEURS/$NOM (R3 ; jamais retiré)"

# 7. La course : sortie standard fermée (elle porte les scores), sortie d'erreur lisible ; PID consigné
FAMILLE=gemini; [ "$ART" = famille ] && FAMILLE=inconnue
COMMUNES=(--sortie "$PILOTE/course" --generations 2 --graine "$GRAINE" --especes --appels-max 160 --usd-par-generation "$USD_GEN"
          --temps-max 2400 --max-tokens-appel 8192 --recherches-max 6 --telechargements-max 3 --octets-max 40000000
          --entrainements-max 0 --rondes-conception-max 0 --parallele-max 8 --relances-max 1 --isoler-reseau
          --plafond-total "$USD_COURSE" --decalage-uid "$DECALAGE_UID"
          --question-ouverte "$PILOTE/question.md" --question-ouverte-aux g001
          --organisme-impose "$LIGNEE=$ORG@$FAMILLE")
SORTIE_FERMEE="$PILOTE/ferme/sortie-standard-lanceur.txt"
ERREURS="$PILOTE/sortie-erreur-lanceur.txt"
cd "$R"
if [ "$MODE" = reel ]; then
  note "- clés : présentes (valeurs jamais lues ni écrites) ; Anthropic : variable $SOURCE_ANTHROPIC → ANTHROPIC_API_KEY ; Gemini : $SOURCE_GEMINI → GEMINI_API_KEY ; Brave : $SOURCE_BRAVE → BRAVE_API_KEY (source « web ») ; OpenAlex : $SOURCE_OPENALEX → OPENALEX_API_KEY ; Semantic Scholar : $SOURCE_S2 → SEMANTIC_SCHOLAR_API_KEY ; rien d'autre de l'environnement du lanceur (ni jeton Hugging Face, Vast, OSF, GitHub, ni ANTHROPIC_BASE_URL, PYTHONPATH, ESSAIM_M3_ESPACE, ESSAIM_M3_COLLISIONNEUR)"
  note "- départ (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  env -i "${ENV_NOYAU[@]}" \
    "$PY" -m essaim_m3 lancer --reel --go "$GO_ID" --registre-go "$PILOTE/registre-go.md" \
      --taches banque/banque-confrontation-v1.json --mission MISSION-v1.md "${COMMUNES[@]}" \
      > "$SORTIE_FERMEE" 2> "$ERREURS" &
else
  note "- départ de la simulation (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  env -i "${ENV_NOYAU[@]}" \
    "$PY" -m essaim_m3 simuler "${COMMUNES[@]}" --n-train 80 --n-test 60 --n-final 60 \
      > "$SORTIE_FERMEE" 2> "$ERREURS" &
fi
PID=$!
note "- PID de la course : $PID (arrêt humain par ce PID seulement, R10 ; STOP dans course/ : arrêt à la fin de la génération)"
set +e; wait "$PID"; CODE=$?; set -e
note "- fin du processus (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; code de retour : $CODE ; sortie standard fermée (non lue) ; sortie d'erreur : sortie-erreur-lanceur.txt (lisible)"

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
    "$PY" -I -c 'import json, sys; x = json.load(open(sys.argv[1])); m = x["manifeste"]; r = x.get("rapport") or {}; print("- vérification après départ (extrait) : isolation " + json.dumps(m.get("isolation"), ensure_ascii=False) + " ; collisionneur conforme : " + str(m.get("collisionneur_conforme")) + " ; commit " + str(m.get("commit")) + " ; sha256_code_noyau " + str(m.get("sha256_code_noyau")) + " ; espace " + str(m.get("espace_organismes")) + " ; sources de moisson " + json.dumps(m.get("sources_moisson"), ensure_ascii=False) + " ; clés présentes au manifeste — web : " + str(m.get("cle_brave_presente")) + ", OpenAlex : " + str(m.get("cle_openalex_presente")) + ", Semantic Scholar : " + str(m.get("cle_s2_presente")) + " ; dépense du noyau " + str(r.get("depense_totale_usd")) + " USD (à rapprocher de la console, P2C1-05)")' "$PILOTE/extrait-mecanique-v1.json" >> "$L"
  else
    note "- extrait mécanique : REFUSÉ par l'outil (aucune écriture ; sortie-erreur-extrait.txt) — rapporté ; la course n'est pas ouverte"
  fi
  ESPACE="$("$PY" -I -c 'import json, sys; print(json.load(open(sys.argv[1])).get("espace_organismes") or "")' "$PILOTE/course/manifeste-run.json")"
  [ "$ART" = espace ] && ESPACE="$(mktemp -d)"
  for g in g000 g001; do
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
(cd "$PILOTE" && sha256sum sortie-erreur-lanceur.txt > sortie-erreur-lanceur.txt.sha256)
for f in sortie-erreur-extrait.txt sortie-erreur-tar.txt; do [ -f "$PILOTE/$f" ] && (cd "$PILOTE" && sha256sum "$f" > "$f.sha256"); done
permis_re='^(\.gitignore|LANCEMENT\.md|LANCEMENT\.md\.sha256|sortie-erreur-(lanceur|extrait|tar)\.txt(\.sha256)?|essais-v1\.(xml|txt)|extrait-mecanique-v1\.json(\.sha256)?|reponse-question-g001\.md(\.sha256|\.sha256-archive)?|journal-appels-g00[01]\.jsonl(\.sha256|\.sha256-archive)?|question\.md|registre-go\.md|test-depense-[^/]+|organisme/.+|ferme\.tar\.gz(\.sha256)?|refus-avant-manifeste-v1\.tar\.gz(\.sha256)?)$'
imprevus="$(cd "$PILOTE" && find . \( -path ./course -o -path ./ferme \) -prune -o -type f -print | sed 's#^\./##' | grep -Ev "$permis_re" | grep -Ev '^(A-POUSSER-v1\.txt(\.sha256)?|EMPREINTES-pilote-v1\.txt(\.sha256)?)$' || true)"
[ -z "$imprevus" ] || note "- fichiers imprévus, NON poussés (consignés) : $(echo $imprevus)"
(cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256)
(cd "$PILOTE" && find . \( -path ./course -o -path ./ferme \) -prune -o -type f -print | sed 's#^\./##' | grep -E "$permis_re" | sort > A-POUSSER-v1.txt \
   && printf 'A-POUSSER-v1.txt\nA-POUSSER-v1.txt.sha256\nEMPREINTES-pilote-v1.txt\nEMPREINTES-pilote-v1.txt.sha256\n' >> A-POUSSER-v1.txt \
   && sha256sum A-POUSSER-v1.txt > A-POUSSER-v1.txt.sha256 \
   && grep -Ev '^EMPREINTES-pilote-v1\.txt(\.sha256)?$' A-POUSSER-v1.txt | xargs sha256sum > EMPREINTES-pilote-v1.txt \
   && sha256sum EMPREINTES-pilote-v1.txt > EMPREINTES-pilote-v1.txt.sha256)
echo "pilote fini : $PILOTE — à pousser : exactement les fichiers de A-POUSSER-v1.txt (branche pilotes/$NOM) ; jamais course/ ni ferme/"
exit 0
