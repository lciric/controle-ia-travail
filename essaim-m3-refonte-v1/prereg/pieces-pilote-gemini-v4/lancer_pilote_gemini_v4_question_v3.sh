#!/usr/bin/env bash
# Lanceur du pilote descriptif « organisme de Gemini v4 + question ouverte à g001 » — v3 (remplace la v2, gardée, R12),
# écrit par conv-audit pour session-depot (qui tient les clés et lance). Met en œuvre, pas à pas, le plan § 1 et § 3 du
# préenregistrement scellé `essaim-m3-refonte-v1/prereg/pilote-gemini-organisme-v4-question-v3.md`.
# v2 : constats de la contre-lecture 3 (sortie standard fermée, archive fermée vérifiée, tentative avant manifeste,
# banque, mission et arbre vérifiés, essais en root). v3 : constats de la contre-lecture 4 — un refus avant le manifeste
# ne ferme rien et ne bloque pas la tentative suivante (PG4-01) ; variables d'essai refusées en mode réel, dossier et
# source des registres consignés (PG4-02) ; « calcul » et le nom du pilote sur la même ligne du GO, variable source de la
# clé Gemini consignée, journal absent consigné (PG4-05) ; vrais compagnons des copies, liste à pousser fermée par noms,
# `.gitignore` du dossier (PG4-06, PG4-07) ; autre course détectée (PG4-08 (v)) ; crochets d'essai pour les gardes
# restées sans artefact (PG4-04), refusés en mode réel.
#
# Usage :
#   MODE=reel DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO07_USD=… APPEL_CONTROLE_FICHIER=… \
#       [TENTATIVE=2] [PYTEST_ARGS="--deselect …"] bash lancer_pilote_gemini_v4_question_v3.sh
#   MODE=simulation DEPOT=… PYTHON=… GRAINE=… [PILOTE_RACINE=… REGISTRE_GO_SOURCE=… DEPENSES_SOURCE=… RESTE_GO07_USD=…
#       PREREG=… PREREG_SHA256=… APPEL_CONTROLE_FICHIER=… ESSAI_ARTEFACT=… ESSAI_JUNIT_EXISTANT=… ESSAI_RESUME_EXISTANT=…]
#
# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course ou la sortie standard ; arrêter un
# processus par motif (R10 : PID consigné ; la détection d'une autre course n'arrête rien) ; écraser un dossier (R12) ;
# lancer une seconde course (R3).
set -euo pipefail
set +x
refus_tot() { echo "REFUS : $*" >&2; exit 2; }   # refus avant que le dossier du pilote existe

MODE="${MODE:?MODE=reel ou MODE=simulation}"
[ "$MODE" = reel ] || [ "$MODE" = simulation ] || refus_tot "MODE inconnu : $MODE"
PY="${PYTHON:-python3}"
SOURCE_GEMINI=""
if [ "$MODE" = reel ]; then
  for v in PILOTE_RACINE SUFFIXE_ESSAI REGISTRE_GO_SOURCE DEPENSES_SOURCE ESSAI_ARTEFACT ESSAI_JUNIT_EXISTANT ESSAI_RESUME_EXISTANT; do
    [ -z "${!v:-}" ] || refus_tot "variable d'essai $v définie en mode réel (PG4-02)"
  done
  [ "$(id -u)" = 0 ] || refus_tot "le mode réel exige root (essais et course)"
  [ -n "${ANTHROPIC_API_KEY:-}" ] || refus_tot "ANTHROPIC_API_KEY absente"
  if [ -n "${GEMINI_API_KEY_2:-}" ]; then SOURCE_GEMINI=GEMINI_API_KEY_2
  elif [ -n "${GEMINI_API_KEY:-}" ]; then SOURCE_GEMINI=GEMINI_API_KEY
  else refus_tot "clé Gemini absente (GEMINI_API_KEY_2 ou GEMINI_API_KEY)"; fi
fi
# une autre course du noyau dans ce conteneur : le pilote attend (détection seulement, aucun arrêt)
autres="$(pgrep -f 'essaim_m3 (lancer|simuler)' || true)"
[ -z "$autres" ] || refus_tot "une autre course du noyau tourne dans ce conteneur (PID $(echo $autres)) : le pilote attend"

DEPOT="$(cd "${DEPOT:?DEPOT=racine du dépôt}" && pwd)"
R="$DEPOT/essaim-m3-refonte-v1"
GRAINE="${GRAINE:?GRAINE=graine de course du préenregistrement scellé}"
NOM="pilote-gemini-organisme-v4-question-v1"
RACINE_PILOTES="${PILOTE_RACINE:-$R/pilotes}"
TENTATIVE="${TENTATIVE:-1}"
case "$TENTATIVE" in ''|*[!0-9]*) refus_tot "TENTATIVE doit être un entier";; esac
if [ "$TENTATIVE" = 1 ]; then PILOTE="$RACINE_PILOTES/$NOM${SUFFIXE_ESSAI:-}"; else PILOTE="$RACINE_PILOTES/$NOM-tentative$TENTATIVE${SUFFIXE_ESSAI:-}"; fi
ART="${ESSAI_ARTEFACT:-}"

COMMIT_CODE=cec6dce3b1e2d4c1514f63914face859e8a59d97
COMMIT_LIENS=4967734a62a0b10c3b5cd6360e21924f015053fd
COMMIT_ORGANISME=b64bb3e4c0ae8fd500d09de939ff5a48dc7aec10
COMMIT_QUESTION=003995208431e825605bab9c4c1894b7508ad6ab
[ "$ART" = commit ] && COMMIT_QUESTION=0123456789abcdef0123456789abcdef01234567
ARBRE_ORGANISME=c5ada33581fd7675f2cec5331d9a9a50ff80271b543c22eef80a64882730c1b9
SHA_QUESTION=d967b212082315c7b4fa1c42ab1b5d551b3bc1d3c4a98cdeb58eccd58b5b9441
SHA_BANQUE=f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc
SHA_MISSION=bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e
[ "$ART" = banque ] && SHA_BANQUE=0000
[ "$ART" = mission ] && SHA_MISSION=0000
CODE_NOYAU_PROPRE=68494279ec42fc13366f83cc67c502c67ed6dcf97f0678bb568aaae8010772fb
CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-reecriture-vs-apprentissage-organismes-v1.md
ESSAIS_CITES="test_fichiers_lecture_et_copie_sans_lien test_depot_ne_suit_aucun_lien_de_l_organisme test_organisme_poseur_de_liens_ne_voit_rien_du_noyau test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score test_extrait_mecanique_sain_puis_artefacts test_mode_reel_refuse_sans_go test_mode_reel_refuse_anthropic_base_url test_bac_a_sable_isolation_reseau_refusee_si_indisponible test_appels_paralleles_plafond_tenu_au_pire_cas test_organisme_gourmand_recoit_plafond_sans_exception test_ce312_doit_arreter_et_raison_juste test_bac_a_sable_exception_et_delai test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee test_ce305_credit_epuise_arrete_la_course test_ce307_anomalie_journal_absent test_relance_puis_reprise_remet_le_compteur_a_zero test_fichier_stop_arrete_la_boucle test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus"
SAUTS_PERMIS="test_sources_reelles_de_moisson_si_reseau"

# R3 : une course est partie dès que son manifeste est écrit ; aucune seconde course, quel que soit le dossier du pilote
for d in "$RACINE_PILOTES/$NOM"*; do
  [ -d "$d" ] || continue
  if [ -f "$d/course/manifeste-run.json" ] || [ -f "$d/ferme.tar.gz" ]; then
    refus_tot "une course est déjà partie dans $d (R3 : jamais de seconde course)"
  fi
done
[ -e "$PILOTE" ] && refus_tot "$PILOTE existe déjà (R12 ; après un refus avant le manifeste : TENTATIVE=$((TENTATIVE + 1)))"
mkdir -p "$PILOTE/ferme"
chmod 700 "$PILOTE/ferme"
printf 'course/\nferme/\n' > "$PILOTE/.gitignore"   # PG4-07 : jamais ajoutés au dépôt, même par un `git add -A`
L="$PILOTE/LANCEMENT.md"
refus() { echo "REFUS : $*" >&2; echo "- refus : $* ($(date -u +%Y-%m-%dT%H:%M:%SZ))" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256); exit 2; }
note() { echo "$*" >> "$L"; }
trap 'c=$?; echo "ÉCHEC inattendu (code $c) à la ligne $LINENO : arrêt" >&2; echo "- échec inattendu (code $c) à la ligne $LINENO ($(date -u +%Y-%m-%dT%H:%M:%SZ))" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256) || true' ERR
if [ "$MODE" = reel ]; then SOURCE_REG="origin/main"; else SOURCE_REG="${REGISTRE_GO_SOURCE:-aucune (simulation)} ; dépenses : ${DEPENSES_SOURCE:-aucune (simulation)}"; fi
{
  echo "# Lancement du pilote $NOM ($MODE, tentative $TENTATIVE)"
  echo
  echo "- début (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; hôte : $(hostname) ; utilisateur : $(id -u)"
  echo "- dossier du pilote : $PILOTE"
  echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD) (c'est le « commit » que le manifeste consignera)"
  echo "- lanceur : $(basename "$0"), sha256 $(sha256sum "$0" | cut -d' ' -f1)"
  echo "- source des registres : $SOURCE_REG"
  echo "- aucune autre course du noyau dans ce conteneur au départ (détection par pgrep)"
} > "$L"
[ "$MODE" = simulation ] && [ -n "$ART" ] && note "- ESSAI : artefact « $ART » (simulation)"

# 1. Code identique à cec6dce (commit et arbre de travail), correctif des liens ; banque et mission
for c in "$COMMIT_CODE" "$COMMIT_LIENS" "$COMMIT_ORGANISME" "$COMMIT_QUESTION"; do
  git -C "$DEPOT" cat-file -e "$c^{commit}" 2>/dev/null || refus "commit $c absent du dépôt (git fetch)"
done
P="essaim-m3-refonte-v1/essaim_m3 essaim-m3-refonte-v1/tests"
# shellcheck disable=SC2086
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" HEAD -- $P || refus "code de HEAD différent de cec6dce (essaim_m3 ou tests)"
# shellcheck disable=SC2086
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" -- $P || refus "arbre de travail différent de cec6dce (essaim_m3 ou tests)"
# shellcheck disable=SC2086
inattendus="$(git -C "$DEPOT" status --porcelain --untracked-files=all -- $P | grep -v '__pycache__' || true)"
[ -z "$inattendus" ] || refus "fichiers non suivis ou modifiés dans essaim_m3 ou tests : $inattendus"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_LIENS" HEAD || refus "correctif des liens 4967734 non ancêtre de HEAD"
[ "$(sha256sum "$R/banque/banque-confrontation-v1.json" | cut -d' ' -f1)" = "$SHA_BANQUE" ] || refus "empreinte de la banque ≠ f1387a20…"
[ "$(sha256sum "$R/MISSION-v1.md" | cut -d' ' -f1)" = "$SHA_MISSION" ] || refus "empreinte de la mission ≠ bd2c6a15…"
note "- code : identique à cec6dce (commit et arbre de travail : essaim_m3, tests) ; 4967734 ancêtre ; banque $SHA_BANQUE ; mission $SHA_MISSION"

# 2. Préenregistrement scellé (réel ; en simulation si PREREG est donné)
if [ "$MODE" = reel ] || [ -n "${PREREG:-}" ]; then
  PREREG="${PREREG:?PREREG=chemin du préenregistrement scellé}"; PREREG_SHA256="${PREREG_SHA256:?}"
  [ "$(sha256sum "$PREREG" | cut -d' ' -f1)" = "$PREREG_SHA256" ] || refus "empreinte du préenregistrement ≠ PREREG_SHA256"
  [ -f "$PREREG.sha256" ] && [ "$(cut -d' ' -f1 < "$PREREG.sha256")" = "$PREREG_SHA256" ] || refus "compagnon .sha256 du préenregistrement absent ou différent"
  grep -q "= $GRAINE\b" "$PREREG" || refus "la graine $GRAINE n'est pas écrite dans le préenregistrement scellé"
  if grep -q "<<[A-Z0-9_]*>>" "$PREREG"; then refus "marqueurs <<…>> restants : préenregistrement non scellé"; fi
  note "- préenregistrement : $PREREG, sha256 $PREREG_SHA256 (compagnon conforme), graine $GRAINE écrite"
fi

# 3. Organisme v4 et question, extraits des commits cités, vérifiés
git -C "$DEPOT" archive "$COMMIT_ORGANISME" outils/gemini-organisme-v4/organisme | tar -x -C "$PILOTE"
ORG="$PILOTE/outils/gemini-organisme-v4/organisme"
[ "$ART" = organisme ] && printf ' ' >> "$ORG/principal.py"
[ "$ART" = nombre ] && rm -f "$ORG/CONCEPTION.md"
n_fichiers="$(find "$ORG" -type f | wc -l)"
[ "$n_fichiers" = 16 ] || refus "organisme : $n_fichiers fichiers au lieu de 16"
empreinte_arbre() { (cd "$R" && "$PY" -B -I -c 'import pathlib, sys; sys.path.insert(0, "."); from essaim_m3.noyau import boucle; print(boucle.empreinte_arbre(pathlib.Path(sys.argv[1])))' "$1"); }
[ "$(empreinte_arbre "$ORG")" = "$ARBRE_ORGANISME" ] || refus "empreinte d'arbre de l'organisme ≠ c5ada335…"
git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" > "$PILOTE/question.md"
[ "$ART" = question ] && printf '\n' >> "$PILOTE/question.md"
[ "$(sha256sum "$PILOTE/question.md" | cut -d' ' -f1)" = "$SHA_QUESTION" ] || refus "empreinte de la question ≠ d967b212…"
note "- organisme : 16 fichiers, empreinte d'arbre $ARBRE_ORGANISME ; question : sha256 $SHA_QUESTION"

# 4. Registre des GO : « calcul » et le nom du pilote sur une même ligne ; dépense consignée avant ; reste ≥ 40 USD
if [ "$MODE" = reel ] || [ -n "${REGISTRE_GO_SOURCE:-}" ]; then
  if [ "$MODE" = reel ]; then git -C "$DEPOT" show origin/main:registres/go.md > "$PILOTE/registre-go.md"; else cp "$REGISTRE_GO_SOURCE" "$PILOTE/registre-go.md"; fi
  grep '^| GO-2026-10-24-07 |' "$PILOTE/registre-go.md" | grep 'calcul' | grep -q "$NOM" \
    || refus "aucune ligne « | GO-2026-10-24-07 | » qui porte à la fois le type calcul et le nom $NOM (extension non inscrite)"
  if [ "$MODE" = reel ]; then dep="$(git -C "$DEPOT" show origin/main:registres/depenses.md)"; else dep="$(cat "${DEPENSES_SOURCE:?DEPENSES_SOURCE en simulation avec REGISTRE_GO_SOURCE}")"; fi
  echo "$dep" | grep "$NOM" | grep -q "GO-2026-10-24-07" || refus "lancement non consigné avant dans registres/depenses.md (une ligne nommant $NOM et GO-2026-10-24-07)"
  reste="${RESTE_GO07_USD:?RESTE_GO07_USD=reste disponible sur GO-2026-10-24-07, en USD}"
  "$PY" -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= 40.0 else 1)' "$reste" || refus "reste sur GO-2026-10-24-07 = $reste USD < 40"
  note "- registre : une ligne GO-2026-10-24-07 de type calcul nommant le pilote ; dépense consignée avant ; reste déclaré $reste USD ≥ 40 (vérification du lanceur)"
fi

# 5. Appel de contrôle par espèce (réel ; en simulation si le fichier est donné) : statut vérifié par l'outil de session-depot
if [ "$MODE" = reel ] || [ -n "${APPEL_CONTROLE_FICHIER:-}" ]; then
  f="${APPEL_CONTROLE_FICHIER:?APPEL_CONTROLE_FICHIER=résultat de l appel de contrôle par espèce}"
  [ "$ART" = appel ] && f="$PILOTE/appel-vide.txt" && : > "$f"
  [ -s "$f" ] || refus "résultat de l'appel de contrôle absent ou vide : $f"
  cp "$f" "$PILOTE/appel-controle-$(basename "$f")"
  note "- appel de contrôle : $(basename "$f"), sha256 $(sha256sum "$f" | cut -d' ' -f1) — présent et non vide ; son statut est vérifié par l'outil de session-depot, non par ce script"
fi

# 6. Essais (en root en réel), puis code sans bytecode et empreinte du noyau
if [ "$MODE" = simulation ] && [ -n "${ESSAI_JUNIT_EXISTANT:-}" ]; then
  cp "$ESSAI_JUNIT_EXISTANT" "$PILOTE/essais-v1.xml"; resultat="${ESSAI_RESUME_EXISTANT:?}"
  note "- ESSAI : rapport JUnit repris de $ESSAI_JUNIT_EXISTANT (simulation)"
else
  resultat="$( (cd "$R" && PYTHONDONTWRITEBYTECODE=1 "$PY" -m pytest -q -p no:cacheprovider --junitxml "$PILOTE/essais-v1.xml" ${PYTEST_ARGS:-} 2>&1) | tail -1 || true)"
fi
if [ "$ART" = junit-echec ] || [ "$ART" = junit-saut ] || [ "$ART" = junit-total ]; then
  "$PY" -I -c '
import sys, xml.etree.ElementTree as ET
a, f = sys.argv[1], sys.argv[2]
t = ET.parse(f); cas = list(t.getroot().iter("testcase"))
if a == "junit-echec": ET.SubElement(cas[0], "failure", message="artefact")
elif a == "junit-saut": ET.SubElement([c for c in cas if c.get("name") == "test_fichier_stop_arrete_la_boucle"][0], "skipped", message="artefact")
else:
    for s in t.getroot().iter("testsuite"):
        for c in list(s.findall("testcase"))[:3]: s.remove(c)
t.write(f)' "$ART" "$PILOTE/essais-v1.xml"
fi
"$PY" -I -c '
import re, sys, xml.etree.ElementTree as ET
resume, junit, cites, permis = sys.argv[1], sys.argv[2], set(sys.argv[3].split()), set(sys.argv[4].split())
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
if set(sautes) - permis: problemes.append(f"sauts non permis : {sorted(set(sautes) - permis)}")
if manquants: problemes.append(f"essais cités non passés ici : {manquants}")
if total != 114: problemes.append(f"{total} essais au lieu de 114")
print("; ".join(problemes) if problemes else f"{len(etat) - len(sautes)} passés, {len(sautes)} sautés {sautes}, {d} désélectionnés")
sys.exit(1 if problemes else 0)' "$resultat" "$PILOTE/essais-v1.xml" "$ESSAIS_CITES" "$SAUTS_PERMIS" > "$PILOTE/essais-v1.txt" || refus "essais : $(cat "$PILOTE/essais-v1.txt") (résumé : « $resultat »)"
note "- essais : $(cat "$PILOTE/essais-v1.txt") ; arguments : « ${PYTEST_ARGS:-aucun} » ; les 19 essais cités ont passé ici"
find "$R/essaim_m3" "$R/tests" -name __pycache__ -prune -exec rm -rf {} +
[ "$ART" = bytecode ] && mkdir -p "$R/essaim_m3/noyau/__pycache__" && printf x > "$R/essaim_m3/noyau/__pycache__/x.pyc"
code_noyau="$(empreinte_arbre "$R/essaim_m3/noyau")"
[ "$code_noyau" = "$CODE_NOYAU_PROPRE" ] || refus "empreinte du noyau nettoyé $code_noyau ≠ 68494279…"
note "- noyau sans bytecode : empreinte $code_noyau"

# 7. La course : sortie standard fermée (elle porte les scores), sortie d'erreur lisible ; PID consigné
FAMILLE=gemini; [ "$ART" = famille ] && FAMILLE=inconnue
COMMUNES=(--sortie "$PILOTE/course" --generations 2 --graine "$GRAINE" --especes --appels-max 160 --usd-par-generation 20
          --temps-max 1800 --max-tokens-appel 4096 --recherches-max 0 --telechargements-max 0 --entrainements-max 0
          --rondes-conception-max 0 --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 40 --decalage-uid 0
          --question-ouverte "$PILOTE/question.md" --question-ouverte-aux g001
          --organisme-impose "gemini-organisme-v4=$ORG@$FAMILLE")
SORTIE_FERMEE="$PILOTE/ferme/sortie-standard-lanceur.txt"
ERREURS="$PILOTE/sortie-erreur-lanceur.txt"
cd "$R"
if [ "$MODE" = reel ]; then
  note "- clés : présentes (valeurs jamais lues ni écrites) ; clé Gemini prise dans la variable $SOURCE_GEMINI et passée sous GEMINI_API_KEY ; ANTHROPIC_BASE_URL retirée"
  note "- départ (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  env -u ANTHROPIC_BASE_URL PYTHONDONTWRITEBYTECODE=1 GEMINI_API_KEY="${!SOURCE_GEMINI}" \
    "$PY" -m essaim_m3 lancer --reel --go GO-2026-10-24-07 --registre-go "$PILOTE/registre-go.md" \
      --taches banque/banque-confrontation-v1.json --mission MISSION-v1.md "${COMMUNES[@]}" \
      > "$SORTIE_FERMEE" 2> "$ERREURS" &
else
  note "- départ de la simulation (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  PYTHONDONTWRITEBYTECODE=1 "$PY" -m essaim_m3 simuler "${COMMUNES[@]}" --n-train 80 --n-test 60 --n-final 60 \
      > "$SORTIE_FERMEE" 2> "$ERREURS" &
fi
PID=$!
note "- PID de la course : $PID (arrêt humain par ce PID seulement, R10 ; STOP dans course/ : arrêt à la fin de la génération)"
set +e; wait "$PID"; CODE=$?; set -e
note "- fin du processus (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; code de retour : $CODE ; sortie standard fermée (non lue) ; sortie d'erreur : sortie-erreur-lanceur.txt (lisible)"

# 8a. Une course est partie (manifeste écrit) : extrait sans score, réponse et journaux recopiés (avec de vrais
#     compagnons), archive fermée (course, sortie standard, espace), copies ouvertes retirées après vérification
copier() {  # copie d'un fichier archivé : vrai compagnon de la copie, compagnon d'origine gardé en « -archive »
  local src="$1" dst="$2"
  cp "$src" "$PILOTE/$dst"
  (cd "$PILOTE" && sha256sum "$dst" > "$dst.sha256")
  [ -f "$src.sha256" ] && cp "$src.sha256" "$PILOTE/$dst.sha256-archive"
  return 0
}
if [ -f "$PILOTE/course/manifeste-run.json" ]; then
  if "$PY" -B -m essaim_m3.outils.extrait_mecanique --course "$PILOTE/course" --sortie "$PILOTE/extrait-mecanique-v1.json" > /dev/null; then
    note "- extrait mécanique : extrait-mecanique-v1.json, sha256 $(sha256sum "$PILOTE/extrait-mecanique-v1.json" | cut -d' ' -f1)"
    "$PY" -I -c 'import json, sys; m = json.load(open(sys.argv[1]))["manifeste"]; print("- vérification après départ (extrait) : isolation " + json.dumps(m.get("isolation"), ensure_ascii=False) + " ; collisionneur conforme : " + str(m.get("collisionneur_conforme")) + " ; commit " + str(m.get("commit")) + " ; sha256_code_noyau " + str(m.get("sha256_code_noyau")))' "$PILOTE/extrait-mecanique-v1.json" >> "$L"
  else
    note "- extrait mécanique : REFUSÉ par l'outil (aucune écriture) — rapporté ; la course n'est pas ouverte"
  fi
  ESPACE="$("$PY" -I -c 'import json, sys; print(json.load(open(sys.argv[1])).get("espace_organismes") or "")' "$PILOTE/course/manifeste-run.json")"
  [ "$ART" = espace ] && ESPACE="$(mktemp -d)"
  for g in g000 g001; do
    a="$PILOTE/course/archive/gemini-organisme-v4/$g/journal-appels.jsonl"
    if [ -f "$a" ] && [ ! -L "$a" ]; then
      copier "$a" "journal-appels-$g.jsonl"
      note "- journal des appels $g : journal-appels-$g.jsonl, sha256 $(cut -d' ' -f1 < "$PILOTE/journal-appels-$g.jsonl.sha256")"
    else
      note "- journal des appels $g : absent ou non ordinaire dans l'archive (génération non tournée, ou anomalie) — rapporté"
    fi
  done
  rq="$PILOTE/course/archive/gemini-organisme-v4/g001/reponse-question.md"
  if [ -f "$rq" ] && [ ! -L "$rq" ]; then
    copier "$rq" "reponse-question-g001.md"
    note "- réponse à la question : reponse-question-g001.md, sha256 $(cut -d' ' -f1 < "$PILOTE/reponse-question-g001.md.sha256")"
  else
    note "- réponse à la question : aucune pièce archivée (voir l'extrait : champ question_ouverte de g001, ou g001 non tournée)"
  fi
  args=(-C "$PILOTE" course ferme)
  espace_a_retirer=""
  if [ -n "$ESPACE" ] && [ -d "$ESPACE" ] && [ "$(cd "$ESPACE" && pwd)" != "$(cd "$PILOTE/course" && pwd)" ]; then
    case "$ESPACE" in
      /var/tmp/essaim-m3/[0-9a-f]*) args+=(-C / "${ESPACE#/}"); espace_a_retirer="$ESPACE";;
      *) note "- espace des organismes hors de /var/tmp/essaim-m3 : $ESPACE — ni archivé ni retiré, jamais lu — réserve";;
    esac
  fi
  set +e; tar --warning=no-file-ignored -czf "$PILOTE/ferme.tar.gz" "${args[@]}"; code_tar=$?; set -e
  (cd "$PILOTE" && sha256sum ferme.tar.gz > ferme.tar.gz.sha256)
  [ "$ART" = archive ] && printf x > "$PILOTE/course/artefact-apres-archive.txt"
  n_archive="$(tar -tzf "$PILOTE/ferme.tar.gz" | wc -l)"
  n_disque="$( { (cd "$PILOTE" && find course ferme ! -type s); if [ -n "$espace_a_retirer" ]; then (cd / && find "${espace_a_retirer#/}" ! -type s); fi; } | wc -l)"
  if [ "$code_tar" = 0 ] && [ "$n_archive" = "$n_disque" ]; then
    rm -rf "$PILOTE/course" "$PILOTE/ferme"; [ -n "$espace_a_retirer" ] && rm -rf "$espace_a_retirer"
    note "- archive fermée : ferme.tar.gz (course, sortie standard, espace des organismes), sha256 $(cut -d' ' -f1 < "$PILOTE/ferme.tar.gz.sha256"), $n_archive entrées = $n_disque sur disque ; copies ouvertes retirées"
  else
    note "- ARCHIVE FERMÉE INCOMPLÈTE : code tar $code_tar, $n_archive entrées contre $n_disque sur disque — copies ouvertes gardées dans ce conteneur (écartées du dépôt par .gitignore), jamais lues ni poussées — réserve"
  fi
# 8b. Aucune course n'est partie (refus avant le manifeste, ou exception) : rien n'est fermé ; la tentative suivante est
#     permise. Le noyau a pu créer des dossiers vides (course/, son espace) : vérifiés sans fichier ordinaire, laissés.
else
  n_course="$( [ -d "$PILOTE/course" ] && find "$PILOTE/course" -type f | wc -l || echo 0)"
  n_sortie="$(wc -c < "$SORTIE_FERMEE")"
  esp_prevu="/var/tmp/essaim-m3/$("$PY" -I -c 'import hashlib, pathlib, sys; print(hashlib.sha256(str(pathlib.Path(sys.argv[1]).resolve()).encode("utf-8")).hexdigest()[:16])' "$PILOTE/course")"
  n_espace="$( [ -d "$esp_prevu" ] && find "$esp_prevu" -type f | wc -l || echo 0)"
  if [ "$n_course" = 0 ] && [ "$n_sortie" = 0 ] && [ "$n_espace" = 0 ]; then
    note "- aucune course partie (pas de manifeste ; code $CODE ; motif dans sortie-erreur-lanceur.txt) ; course/ et l'espace prévu sans aucun fichier, sortie standard vide : laissés tels quels (dossiers vides) ; tentative suivante permise : TENTATIVE=$((TENTATIVE + 1))"
  else
    set +e; tar --warning=no-file-ignored -czf "$PILOTE/refus-avant-manifeste-v1.tar.gz" -C "$PILOTE" course ferme $( [ -d "$esp_prevu" ] && echo "-C / ${esp_prevu#/}" ); set -e
    (cd "$PILOTE" && sha256sum refus-avant-manifeste-v1.tar.gz > refus-avant-manifeste-v1.tar.gz.sha256)
    note "- aucune course partie (pas de manifeste ; code $CODE) mais $n_course fichier(s) dans course/, $n_espace dans l'espace, sortie standard de $n_sortie octets : fermés dans refus-avant-manifeste-v1.tar.gz, jamais lus — réserve ; tentative suivante permise : TENTATIVE=$((TENTATIVE + 1))"
  fi
fi
[ "$ART" = imprevu ] && printf 'x\n' > "$PILOTE/fichier-imprevu.txt"
note "- fin du lanceur (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"

# 9. Ce qui est poussé : une liste fermée de noms (PG4-07) ; tout autre fichier est consigné et n'est pas poussé
(cd "$PILOTE" && sha256sum sortie-erreur-lanceur.txt > sortie-erreur-lanceur.txt.sha256)
permis_re='^(\.gitignore|LANCEMENT\.md|LANCEMENT\.md\.sha256|sortie-erreur-lanceur\.txt(\.sha256)?|essais-v1\.(xml|txt)|extrait-mecanique-v1\.json(\.sha256)?|reponse-question-g001\.md(\.sha256|\.sha256-archive)?|journal-appels-g00[01]\.jsonl(\.sha256|\.sha256-archive)?|question\.md|registre-go\.md|appel-controle-[^/]+|outils/gemini-organisme-v4/organisme/.+|ferme\.tar\.gz(\.sha256)?|refus-avant-manifeste-v1\.tar\.gz(\.sha256)?)$'
imprevus="$(cd "$PILOTE" && find . \( -path ./course -o -path ./ferme \) -prune -o -type f -print | sed 's#^\./##' | grep -Ev "$permis_re" | grep -Ev '^(A-POUSSER-v1\.txt(\.sha256)?|EMPREINTES-pilote-v1\.txt(\.sha256)?)$' || true)"
[ -z "$imprevus" ] || note "- fichiers imprévus, NON poussés (consignés) : $(echo $imprevus)"
(cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256)
(cd "$PILOTE" && find . \( -path ./course -o -path ./ferme \) -prune -o -type f -print | sed 's#^\./##' | grep -E "$permis_re" | sort > A-POUSSER-v1.txt \
   && printf 'A-POUSSER-v1.txt\nA-POUSSER-v1.txt.sha256\nEMPREINTES-pilote-v1.txt\nEMPREINTES-pilote-v1.txt.sha256\n' >> A-POUSSER-v1.txt \
   && sha256sum A-POUSSER-v1.txt > A-POUSSER-v1.txt.sha256 \
   && grep -Ev '^EMPREINTES-pilote-v1\.txt(\.sha256)?$' A-POUSSER-v1.txt | xargs sha256sum > EMPREINTES-pilote-v1.txt \
   && sha256sum EMPREINTES-pilote-v1.txt > EMPREINTES-pilote-v1.txt.sha256)
echo "pilote fini : $PILOTE — à pousser : exactement les fichiers de A-POUSSER-v1.txt ; jamais course/ ni ferme/"
exit 0
