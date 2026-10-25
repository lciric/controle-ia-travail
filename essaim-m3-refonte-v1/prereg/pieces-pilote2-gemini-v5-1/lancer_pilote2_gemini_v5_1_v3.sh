#!/usr/bin/env bash
# Lanceur du second pilote descriptif « organisme de Gemini v5.1, moisson ouverte, question ouverte à g001 », une course
# par appel (COURSE=structure, puis COURSE=maieutique) — v3 (remplace la v2 et la v1, gardées, R12), écrit par conv-audit
# pour session-depot (qui tient les clés et lance). Met en œuvre, pas à pas, le plan § 1 et § 3 du préenregistrement
# scellé `essaim-m3-refonte-v1/prereg/pilote2-gemini-organisme-v5-1-v2.md` (ou de la version qui le remplace et cite ce
# script). Dérivé du lanceur v3 du premier pilote (`322275c0…`).
# v2 : GO-2026-10-25-01 (R-407, R-409) ; ligne du GO reconnue par l'empreinte de la question de la course ; noms des
#      variables de clés (CLE_ANTHROPIC, CLE_GEMINI) ; 30 USD par génération, 60 par course.
# v3 : constats de la contre-lecture 1 (P2C1-01 à P2C1-14) — M ne part que si S est sain (liste close, lue dans l'extrait
#      et le `LANCEMENT.md` de S, empreintes vérifiées) ; voisines aux décalages des essais consignées en réserve ;
#      dépôt sous /root ou /home et caché aux organismes (vérifié par `bac_a_sable.dossiers_a_cacher`) ; espace attendu
#      calculé avant le départ, seul retiré ; test de dépense revérifié juste avant le départ ; graines recalculées
#      depuis l'entropie du texte scellé ; commits postérieurs à 5d1d4fd limités aux pièces du pilote ; versions des
#      bibliothèques consignées ; PYTHONPATH et ESSAIM_M3_COLLISIONNEUR retirées ; sorties d'erreur de l'extraction et de
#      l'archivage gardées.
#
# Usage :
#   MODE=reel COURSE=structure DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO_USD=… \
#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE="…" [CLE_ANTHROPIC=NOM] [CLE_GEMINI=NOM] [TENTATIVE=2] \
#       bash lancer_pilote2_gemini_v5_1_v3.sh
#   MODE=reel COURSE=maieutique … S_PILOTE=<dossier du pilote de la course S> bash lancer_pilote2_gemini_v5_1_v3.sh
#   MODE=simulation COURSE=… DEPOT=… PYTHON=… GRAINE=… [PILOTE_RACINE=… S_PILOTE=… REGISTRE_GO_SOURCE=…
#       DEPENSES_SOURCE=… RESTE_GO_USD=… PREREG=… PREREG_SHA256=… APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=…
#       ESSAI_ARTEFACT=… ESSAI_JUNIT_EXISTANT=… ESSAI_RESUME_EXISTANT=…]
#
# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course ou la sortie standard ; arrêter un
# processus (R10 : PID consigné ; une course voisine est détectée, jamais arrêtée) ; écraser un dossier (R12) ; lancer
# une seconde course de même nom (R3).
set -euo pipefail
set +x
refus_tot() { echo "REFUS : $*" >&2; exit 2; }   # refus avant que le dossier du pilote existe

MODE="${MODE:?MODE=reel ou MODE=simulation}"
[ "$MODE" = reel ] || [ "$MODE" = simulation ] || refus_tot "MODE inconnu : $MODE"
COURSE="${COURSE:?COURSE=structure ou COURSE=maieutique}"
case "$COURSE" in
  structure)
    NOM="pilote2-gemini-v5-1-structure-v1"; INDICE_GRAINE=0
    COMMIT_QUESTION=4772b525081342a6a30ba8823733aa5770a888a8
    CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-apprendre-structure-entrainement-generations-organismes-v2.md
    SHA_QUESTION=a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289;;
  maieutique)
    NOM="pilote2-gemini-v5-1-maieutique-v1"; INDICE_GRAINE=1
    COMMIT_QUESTION=7d1feec550e3d3bdaf963ecade2cf1558b73e53f
    CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-gemini-maieutique-vs-coercition-organismes-v1.md
    SHA_QUESTION=9e1da26de7c7951e0c9a319b12b99faaad7252f86dc14b0d85479696b4cc6595;;
  *) refus_tot "COURSE inconnue : $COURSE (structure ou maieutique)";;
esac
PY="${PYTHON:-python3}"
ART="${ESSAI_ARTEFACT:-}"
SOURCE_GEMINI=""
SOURCE_ANTHROPIC=""
if [ "$MODE" = reel ]; then
  for v in PILOTE_RACINE SUFFIXE_ESSAI REGISTRE_GO_SOURCE DEPENSES_SOURCE ESSAI_ARTEFACT ESSAI_JUNIT_EXISTANT ESSAI_RESUME_EXISTANT ESSAIM_M3_ESPACE; do
    [ -z "${!v:-}" ] || refus_tot "variable $v définie en mode réel (variable d'essai, ou espace des organismes déplacé)"
  done
  [ "$(id -u)" = 0 ] || refus_tot "le mode réel exige root (essais et course)"
  SOURCE_ANTHROPIC="${CLE_ANTHROPIC:-ANTHROPIC_API_KEY}"
  [[ "$SOURCE_ANTHROPIC" =~ ^[A-Z][A-Z0-9_]*$ ]] || refus_tot "CLE_ANTHROPIC doit être un nom de variable (lettres capitales, chiffres, _)"
  [ -n "${!SOURCE_ANTHROPIC:-}" ] || refus_tot "clé Anthropic absente (variable $SOURCE_ANTHROPIC)"
  if [ -n "${CLE_GEMINI:-}" ]; then SOURCE_GEMINI="$CLE_GEMINI"
  elif [ -n "${GEMINI_API_KEY_2:-}" ]; then SOURCE_GEMINI=GEMINI_API_KEY_2
  else SOURCE_GEMINI=GEMINI_API_KEY; fi
  [[ "$SOURCE_GEMINI" =~ ^[A-Z][A-Z0-9_]*$ ]] || refus_tot "CLE_GEMINI doit être un nom de variable (lettres capitales, chiffres, _)"
  [ -n "${!SOURCE_GEMINI:-}" ] || refus_tot "clé Gemini absente (variable $SOURCE_GEMINI)"
  [ -n "${RECHARGE_ATTESTEE:-}" ] || refus_tot "RECHARGE_ATTESTEE vide : l'attestation de Lazar (recharge automatique active, avec l'heure) est exigée"
fi
DECALAGE_UID=900
DECALAGES_DES_ESSAIS="0 800"   # les essais du noyau font tourner des organismes aux décalages 0 et 810–830 (P2C1-06)
GO_ID=GO-2026-10-25-01
USD_GEN=30      # par génération (décision (b) de Lazar, 25 octobre 10:17 Paris)
USD_COURSE=60   # par course ; deux courses : 120 USD au plus (GO-2026-10-25-01, R-407 et R-409)
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

COMMIT_CODE=5d1d4fdb0dbd9e4d481ec3f4270555f4006df749
COMMIT_LIENS=4967734a62a0b10c3b5cd6360e21924f015053fd
COMMIT_CREDIT=90595ffb53b30c65c66be807215a998998b701fc
COMMIT_ORGANISME=7f9cd2e5a8053dc45050e1b6316bf29ee0c62e0e
[ "$ART" = commit ] && COMMIT_QUESTION=0123456789abcdef0123456789abcdef01234567
ARBRE_ORGANISME=50ffcd7d8cd3af059f2b881f3e565a8ad5829d8d325c39b9535bed6e01a8e12c
N_FICHIERS_ORGANISME=19
SHA_BANQUE=f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc
SHA_MISSION=bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e
SHA_COLLISIONNEUR=213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd
[ "$ART" = banque ] && SHA_BANQUE=0000
[ "$ART" = mission ] && SHA_MISSION=0000
CODE_NOYAU_PROPRE=d5d0efcc4677dd9957db3f324101b58e9475642e8e05926407579f056f653836
N_ESSAIS=140
ESSAIS_CITES="test_fichiers_lecture_et_copie_sans_lien test_depot_ne_suit_aucun_lien_de_l_organisme test_organisme_poseur_de_liens_ne_voit_rien_du_noyau test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score test_extrait_mecanique_sain_puis_artefacts test_mode_reel_refuse_sans_go test_mode_reel_refuse_anthropic_base_url test_bac_a_sable_isolation_reseau_refusee_si_indisponible test_appels_paralleles_plafond_tenu_au_pire_cas test_organisme_gourmand_recoit_plafond_sans_exception test_ce312_doit_arreter_et_raison_juste test_bac_a_sable_exception_et_delai test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee test_ce305_credit_epuise_arrete_la_course test_ce307_anomalie_journal_absent test_relance_puis_reprise_remet_le_compteur_a_zero test_fichier_stop_arrete_la_boucle test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus test_r395_credit_epuise_rendu_en_400_arrete_la_course test_cl5_01_banque_cachee_a_l_organisme test_cl5_02_aucune_voie_commune_par_un_dossier_inscriptible_par_tous test_ce306_vue_lisible_par_la_seule_lignee_et_uid_par_course test_sources_reelles_de_moisson_si_reseau test_moisson_de_bout_en_bout_en_simulation test_ce311_garde_de_temps_compte_la_moisson test_ce305_sources_moisson_au_manifeste_et_bras_apparie test_r402_types_de_blocs_au_journal_et_reflexion_comptee_a_l_extrait"
LIGNEE="gemini-organisme-v5-1"
# Chemins que les commits postérieurs à 5d1d4fd peuvent toucher (ce texte, ses pièces, sa contre-lecture) ; dossier des pilotes
PERMIS_APRES_CODE='^essaim-m3-refonte-v1/prereg/(pilote2-gemini-organisme-v5-1-v[0-9]+\.md(\.sha256)?|pieces-pilote2-gemini-v5-1/.+|contre-lectures/pilote2-gemini-organisme-v5-1-v[0-9]+-cl[0-9]+\.md(\.sha256)?)$'

# R3 : une course est partie dès que son manifeste est écrit ; aucune seconde course de ce nom, quel que soit le dossier
for d in "$RACINE_PILOTES/$NOM"*; do
  [ -d "$d" ] || continue
  if [ -f "$d/course/manifeste-run.json" ] || [ -f "$d/ferme.tar.gz" ]; then
    refus_tot "une course est déjà partie dans $d (R3 : jamais de seconde course)"
  fi
done
[ -e "$PILOTE" ] && refus_tot "$PILOTE existe déjà (R12 ; après un refus avant le manifeste : TENTATIVE=$((TENTATIVE + 1)))"
mkdir -p "$RACINE_PILOTES"
mkdir -m 700 "$PILOTE"
mkdir -m 700 "$PILOTE/ferme"
printf 'course/\nferme/\n' > "$PILOTE/.gitignore"   # jamais ajoutés au dépôt, même par un `git add -A`
L="$PILOTE/LANCEMENT.md"
refus() { echo "REFUS : $*" >&2; echo "- refus : $* ($(date -u +%Y-%m-%dT%H:%M:%SZ))" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256); exit 2; }
note() { echo "$*" >> "$L"; }
trap 'c=$?; echo "ÉCHEC inattendu (code $c) à la ligne $LINENO : arrêt" >&2; echo "- échec inattendu (code $c) à la ligne $LINENO ($(date -u +%Y-%m-%dT%H:%M:%SZ))" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256) || true' ERR
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
  [ -n "$reserve_voisines" ] && echo "- RÉSERVE : course(s) voisine(s) à un décalage des essais du noyau (0, 800) :$reserve_voisines — pendant les essais d'avant départ (≈ 3 minutes), des organismes d'essai tournent aux décalages 0 et 810–830 et partagent ces utilisateurs avec elle(s)"
} > "$L"
[ "$MODE" = simulation ] && [ -n "$ART" ] && note "- ESSAI : artefact « $ART » (simulation)"

# 0. Course M : ne part que si la course S est saine (P2C1-01, liste close lue dans les pièces lisibles de S)
if [ "$COURSE" = maieutique ] && { [ "$MODE" = reel ] || [ -n "${S_PILOTE:-}" ]; }; then
  SP="${S_PILOTE:?S_PILOTE=dossier du pilote de la course S (pilote2-gemini-v5-1-structure-v1 ou sa tentative)}"
  [ -d "$SP" ] || refus "S_PILOTE $SP absent : M ne part qu'après S"
  [ -f "$SP/EMPREINTES-pilote-v1.txt" ] && [ -f "$SP/EMPREINTES-pilote-v1.txt.sha256" ] || refus "empreintes de S absentes : M ne part qu'après une course S finie et fermée"
  (cd "$SP" && sha256sum -c --quiet EMPREINTES-pilote-v1.txt.sha256 && sha256sum -c --quiet EMPREINTES-pilote-v1.txt) > /dev/null 2>&1 || refus "empreintes de S non vérifiées (fichiers de S modifiés ou manquants)"
  issue_s="$("$PY" -I -c '
import json, re, sys
sp, sha_lanceur, lignee = sys.argv[1], sys.argv[2], sys.argv[3]
pb = []
lan = open(sp + "/LANCEMENT.md", encoding="utf-8").read()
if not re.search(r"^- course : structure ;", lan, re.M): pb.append("ce n est pas la course S")
if not re.search(r"^- lanceur : lancer_pilote2_gemini_v5_1_v3\.sh, sha256 " + sha_lanceur + r"$", lan, re.M): pb.append("S n a pas tourné sous ce lanceur")
if not re.search(r"code de retour : 0 ;", lan): pb.append("code de retour du noyau non nul ou absent")
if not re.search(r"^- archive fermée : ferme\.tar\.gz \(", lan, re.M) or "ARCHIVE FERMÉE INCOMPLÈTE" in lan: pb.append("archive fermée absente ou incomplète")
try:
    x = json.load(open(sp + "/extrait-mecanique-v1.json", encoding="utf-8"))
except Exception as e:
    print("extrait de S illisible : " + type(e).__name__); sys.exit(1)
gs = sorted((g for g in x.get("generations", []) if g.get("lignee") == lignee and not g.get("phase")), key=lambda g: g.get("generation", -1))
if [g.get("generation") for g in gs] != [0, 1]: pb.append("générations de S : " + str([g.get("generation") for g in gs]) + " au lieu de [0, 1]")
for g in gs:
    if g.get("statut") != "OK" or g.get("invalide") or g.get("anomalie_noyau"):
        pb.append("g%03d : statut %r, invalide %r, anomalie %r" % (g.get("generation"), g.get("statut"), g.get("invalide"), g.get("anomalie_noyau")))
r = x.get("rapport") or {}
if r.get("generations_invalidees"): pb.append("générations invalidées : " + str(r.get("generations_invalidees")))
fin = ((r.get("lignees") or {}).get(lignee) or {}).get("fin")
if fin != "générations maximales": pb.append("fin de la lignée : %r" % fin)
arrets = [e.get("raison") for e in x.get("evenements", []) if e.get("etape") == "arret"]
if arrets != ["aucune lignée active"]: pb.append("arrêt de la course : %r" % arrets)
if pb: print("; ".join(pb)); sys.exit(1)
print("S saine : g000 et g001 OK, fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée")
' "$SP" "$SHA_LANCEUR" "$LIGNEE")" || refus "M ne part pas : issue de S hors de la liste saine ($issue_s) — décision de Lazar requise"
  note "- course S : $SP ; $issue_s ; empreintes de S vérifiées (EMPREINTES-pilote-v1.txt, sha256 $(cut -d' ' -f1 < "$SP/EMPREINTES-pilote-v1.txt.sha256"))"
fi

# 1. Code identique à 5d1d4fd (commit et arbre de travail, collisionneur compris) ; commits postérieurs limités aux pièces
#    du pilote ; rien de non suivi ni de modifié sous essaim-m3-refonte-v1 hors des dossiers de pilotes ; ancêtres ;
#    banque, mission, collisionneur
for c in "$COMMIT_CODE" "$COMMIT_LIENS" "$COMMIT_CREDIT" "$COMMIT_ORGANISME" "$COMMIT_QUESTION"; do
  git -C "$DEPOT" cat-file -e "$c^{commit}" 2>/dev/null || refus "commit $c absent du dépôt (git fetch)"
done
P="essaim-m3-refonte-v1/essaim_m3 essaim-m3-refonte-v1/tests collisionneur-v2.5-banc-jev-travail"
# shellcheck disable=SC2086
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" HEAD -- $P || refus "code de HEAD différent de 5d1d4fd (essaim_m3, tests ou collisionneur)"
# shellcheck disable=SC2086
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" -- $P || refus "arbre de travail différent de 5d1d4fd (essaim_m3, tests ou collisionneur)"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_CODE" HEAD || refus "5d1d4fd non ancêtre de HEAD"
hors_pieces="$(git -C "$DEPOT" diff --name-only "$COMMIT_CODE" HEAD | grep -Ev "$PERMIS_APRES_CODE" || true)"
[ -z "$hors_pieces" ] || refus "commits postérieurs à 5d1d4fd hors des pièces du pilote : $(echo $hors_pieces)"
rel_pilotes="$(realpath --relative-to="$DEPOT" "$RACINE_PILOTES" 2>/dev/null || echo "")"
inattendus="$(git -C "$DEPOT" status --porcelain --untracked-files=all -- essaim-m3-refonte-v1 collisionneur-v2.5-banc-jev-travail \
  | grep -v '__pycache__' | { if [ -n "$rel_pilotes" ] && [ "${rel_pilotes#..}" = "$rel_pilotes" ]; then grep -v " $rel_pilotes/" ; else cat; fi; } || true)"
[ -z "$inattendus" ] || refus "fichiers non suivis ou modifiés sous essaim-m3-refonte-v1 ou le collisionneur : $(echo $inattendus)"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_LIENS" HEAD || refus "correctif des liens 4967734 non ancêtre de HEAD"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_CREDIT" HEAD || refus "R-395 (90595ffb, arrêt sur crédit épuisé en 400) non ancêtre de HEAD"
[ "$(sha256sum "$R/banque/banque-confrontation-v1.json" | cut -d' ' -f1)" = "$SHA_BANQUE" ] || refus "empreinte de la banque ≠ f1387a20…"
[ "$(sha256sum "$R/MISSION-v1.md" | cut -d' ' -f1)" = "$SHA_MISSION" ] || refus "empreinte de la mission ≠ bd2c6a15…"
[ "$(sha256sum "$DEPOT/collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py" | cut -d' ' -f1)" = "$SHA_COLLISIONNEUR" ] || refus "empreinte du collisionneur ≠ 213b52ef…"
note "- code : identique à 5d1d4fd (commit et arbre de travail : essaim_m3, tests, collisionneur) ; commits postérieurs limités aux pièces du pilote ; rien de non suivi hors des dossiers de pilotes ; 4967734 et 90595ffb ancêtres ; banque $SHA_BANQUE ; mission $SHA_MISSION ; collisionneur $SHA_COLLISIONNEUR"
versions="$(env -u PYTHONPATH "$PY" -I -c '
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

# 3. Organisme v5.1 et question, extraits des commits cités, vérifiés
git -C "$DEPOT" archive "$COMMIT_ORGANISME" outils/gemini-organisme-v5-1/organisme | tar -x -C "$PILOTE"
ORG="$PILOTE/outils/gemini-organisme-v5-1/organisme"
[ "$ART" = organisme ] && printf ' ' >> "$ORG/principal.py"
[ "$ART" = nombre ] && rm -f "$ORG/CONCEPTION.md"
n_fichiers="$(find "$ORG" -type f | wc -l)"
[ "$n_fichiers" = "$N_FICHIERS_ORGANISME" ] || refus "organisme : $n_fichiers fichiers au lieu de $N_FICHIERS_ORGANISME"
empreinte_arbre() { (cd "$R" && env -u PYTHONPATH "$PY" -B -I -c 'import pathlib, sys; sys.path.insert(0, "."); from essaim_m3.noyau import boucle; print(boucle.empreinte_arbre(pathlib.Path(sys.argv[1])))' "$1"); }
[ "$(empreinte_arbre "$ORG")" = "$ARBRE_ORGANISME" ] || refus "empreinte d'arbre de l'organisme ≠ 50ffcd7d…"
git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" > "$PILOTE/question.md"
[ "$ART" = question ] && printf '\n' >> "$PILOTE/question.md"
[ "$(sha256sum "$PILOTE/question.md" | cut -d' ' -f1)" = "$SHA_QUESTION" ] || refus "empreinte de la question ≠ ${SHA_QUESTION:0:8}…"
note "- organisme : $N_FICHIERS_ORGANISME fichiers, empreinte d'arbre $ARBRE_ORGANISME ; question ($COURSE) : sha256 $SHA_QUESTION"

# 4. Registre des GO : une ligne « | GO-2026-10-25-01 | » qui porte « calcul » et l'empreinte (8 premiers caractères) de
#    la question de la course ; dépense consignée avant (une ligne nommant la course et le GO) ; reste ≥ plafond de la course
if [ "$MODE" = reel ] || [ -n "${REGISTRE_GO_SOURCE:-}" ]; then
  if [ "$MODE" = reel ]; then git -C "$DEPOT" show origin/main:registres/go.md > "$PILOTE/registre-go.md"; else cp "$REGISTRE_GO_SOURCE" "$PILOTE/registre-go.md"; fi
  grep "^| $GO_ID |" "$PILOTE/registre-go.md" | grep 'calcul' | grep -q "${SHA_QUESTION:0:8}" \
    || refus "aucune ligne « | $GO_ID | » qui porte à la fois le type calcul et l'empreinte de la question ${SHA_QUESTION:0:8}… (GO non inscrit pour cette course)"
  if [ "$MODE" = reel ]; then dep="$(git -C "$DEPOT" show origin/main:registres/depenses.md)"; else dep="$(cat "${DEPENSES_SOURCE:?DEPENSES_SOURCE en simulation avec REGISTRE_GO_SOURCE}")"; fi
  echo "$dep" | grep "$NOM" | grep -q "$GO_ID" || refus "lancement non consigné avant dans registres/depenses.md (une ligne nommant $NOM et $GO_ID)"
  reste="${RESTE_GO_USD:?RESTE_GO_USD=reste disponible sur $GO_ID avant cette course, en USD}"
  "$PY" -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= float(sys.argv[2]) else 1)' "$reste" "$USD_COURSE" || refus "reste sur $GO_ID = $reste USD < $USD_COURSE"
  note "- registre : une ligne $GO_ID de type calcul portant l'empreinte de la question ($COURSE) ; dépense consignée avant ; reste déclaré $reste USD ≥ $USD_COURSE (vérification du lanceur)"
fi

# 5. Test de dépense (réel ; en simulation si le fichier est donné) : la pièce de l'outil de session-depot (un appel
#    payant par espèce) est lue et vérifiée ici ; la réalité des appels est attestée par l'outil, pas par ce script
verifier_test_depense() {  # verifier_test_depense FICHIER → verdict sur la sortie ; code 1 si non conforme
  "$PY" -I -c '
import datetime, json, os, sys, time
f, go_attendu, age_max = sys.argv[1], sys.argv[2], float(sys.argv[3])
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
    if h is not None:
        try:
            t = datetime.datetime.fromisoformat(str(h).replace("Z", "+00:00")).timestamp()
            if maintenant - t > age_max: pb.append(f"{e} : appel fait il y a {maintenant - t:.0f} s > {age_max:.0f} s")
        except Exception:
            pb.append(f"{e} : heure_utc illisible {h!r}")
    couts.append(f"{e} {c}")
if pb: print("; ".join(pb)); sys.exit(1)
print("trois espèces OK, modèles servis conformes, coûts " + ", ".join(couts) + f" USD, âge {age:.0f} s")
' "$1" "$GO_ID" "$AGE_MAX_TEST_DEPENSE"
}
TD=""
if [ "$MODE" = reel ] || [ -n "${APPEL_CONTROLE_FICHIER:-}" ]; then
  TD="${APPEL_CONTROLE_FICHIER:?APPEL_CONTROLE_FICHIER=résultat du test de dépense par espèce (JSON)}"
  [ "$ART" = appel ] && TD="$PILOTE/appel-vide.json" && : > "$TD"
  [ "$ART" = appel-vieux ] && touch -d '20 minutes ago' "$TD"
  [ -s "$TD" ] || refus "résultat du test de dépense absent ou vide : $TD"
  verdict="$(verifier_test_depense "$TD")" || refus "test de dépense non conforme : $verdict"
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
[ "$code_noyau" = "$CODE_NOYAU_PROPRE" ] || refus "empreinte du noyau nettoyé $code_noyau ≠ d5d0efcc…"
note "- noyau sans bytecode : empreinte $code_noyau (la fonction écarte le bytecode depuis le constat n° 30 § 5)"

# 6 bis. Juste avant le départ : test de dépense revérifié (âge ≤ 15 min au départ) ; voisines redétectées
if [ -n "$TD" ]; then
  [ "$ART" = appel-vieillit ] && touch -d '20 minutes ago' "$TD"
  verdict2="$(verifier_test_depense "$TD")" || refus "test de dépense trop ancien ou non conforme au départ ($verdict2) : le refaire, puis TENTATIVE=$((TENTATIVE + 1))"
  note "- test de dépense revérifié au départ : $verdict2"
fi
detecter_voisines || refus "une course du noyau tourne au décalage $DECALAGE_UID au moment du départ : le pilote attend"
note "- voisines au départ :${voisines:- aucune}"

# 7. La course : sortie standard fermée (elle porte les scores), sortie d'erreur lisible ; PID consigné
FAMILLE=gemini; [ "$ART" = famille ] && FAMILLE=inconnue
COMMUNES=(--sortie "$PILOTE/course" --generations 2 --graine "$GRAINE" --especes --appels-max 160 --usd-par-generation "$USD_GEN"
          --temps-max 3600 --max-tokens-appel 8192 --recherches-max 6 --telechargements-max 3 --octets-max 40000000
          --entrainements-max 0 --rondes-conception-max 0 --parallele-max 8 --relances-max 1 --isoler-reseau
          --plafond-total "$USD_COURSE" --decalage-uid "$DECALAGE_UID"
          --question-ouverte "$PILOTE/question.md" --question-ouverte-aux g001
          --organisme-impose "$LIGNEE=$ORG@$FAMILLE")
SORTIE_FERMEE="$PILOTE/ferme/sortie-standard-lanceur.txt"
ERREURS="$PILOTE/sortie-erreur-lanceur.txt"
cd "$R"
if [ "$MODE" = reel ]; then
  note "- clés : présentes (valeurs jamais lues ni écrites) ; clé Anthropic prise dans la variable $SOURCE_ANTHROPIC et passée sous ANTHROPIC_API_KEY ; clé Gemini prise dans la variable $SOURCE_GEMINI et passée sous GEMINI_API_KEY ; ANTHROPIC_BASE_URL, BRAVE_API_KEY, PYTHONPATH et ESSAIM_M3_COLLISIONNEUR retirées"
  note "- départ (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  env -u ANTHROPIC_BASE_URL -u BRAVE_API_KEY -u ESSAIM_M3_ESPACE -u PYTHONPATH -u ESSAIM_M3_COLLISIONNEUR \
      PYTHONDONTWRITEBYTECODE=1 ESSAIM_M3_CACHER="$DEPOT" \
      ANTHROPIC_API_KEY="${!SOURCE_ANTHROPIC}" GEMINI_API_KEY="${!SOURCE_GEMINI}" \
    "$PY" -m essaim_m3 lancer --reel --go "$GO_ID" --registre-go "$PILOTE/registre-go.md" \
      --taches banque/banque-confrontation-v1.json --mission MISSION-v1.md "${COMMUNES[@]}" \
      > "$SORTIE_FERMEE" 2> "$ERREURS" &
else
  note "- départ de la simulation (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  env -u BRAVE_API_KEY -u ESSAIM_M3_ESPACE -u PYTHONPATH -u ESSAIM_M3_COLLISIONNEUR PYTHONDONTWRITEBYTECODE=1 ESSAIM_M3_CACHER="$DEPOT" \
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
    "$PY" -I -c 'import json, sys; x = json.load(open(sys.argv[1])); m = x["manifeste"]; r = x.get("rapport") or {}; print("- vérification après départ (extrait) : isolation " + json.dumps(m.get("isolation"), ensure_ascii=False) + " ; collisionneur conforme : " + str(m.get("collisionneur_conforme")) + " ; commit " + str(m.get("commit")) + " ; sha256_code_noyau " + str(m.get("sha256_code_noyau")) + " ; espace " + str(m.get("espace_organismes")) + " ; sources de moisson " + json.dumps(m.get("sources_moisson"), ensure_ascii=False) + " ; clé web présente : " + str(m.get("cle_brave_presente")) + " ; dépense du noyau " + str(r.get("depense_totale_usd")) + " USD (à rapprocher de la console, P2C1-05)")' "$PILOTE/extrait-mecanique-v1.json" >> "$L"
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
permis_re='^(\.gitignore|LANCEMENT\.md|LANCEMENT\.md\.sha256|sortie-erreur-(lanceur|extrait|tar)\.txt(\.sha256)?|essais-v1\.(xml|txt)|extrait-mecanique-v1\.json(\.sha256)?|reponse-question-g001\.md(\.sha256|\.sha256-archive)?|journal-appels-g00[01]\.jsonl(\.sha256|\.sha256-archive)?|question\.md|registre-go\.md|test-depense-[^/]+|outils/gemini-organisme-v5-1/organisme/.+|ferme\.tar\.gz(\.sha256)?|refus-avant-manifeste-v1\.tar\.gz(\.sha256)?)$'
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
