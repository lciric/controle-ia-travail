#!/usr/bin/env bash
# Lanceur du pilote descriptif « organisme de Gemini v4 + question ouverte à g001 » — v2 (remplace la v1, gardée, R12),
# écrit par conv-audit pour session-depot (qui tient les clés et lance). Met en œuvre, pas à pas, le plan § 1 et § 3 du
# préenregistrement scellé `essaim-m3-refonte-v1/prereg/pilote-gemini-organisme-v4-question-v2.md`.
# v2 : constats de la contre-lecture 3 — sortie standard (scores) fermée, sortie d'erreur lisible (PG3-01) ; course,
# sortie standard et espace des organismes dans une seule archive fermée, copies ouvertes retirées après vérification
# de la liste ; journaux d'appels recopiés (PG3-02) ; banque, mission et arbre de travail vérifiés (PG3-09) ; essais en
# root, sauts et désélections réglés, essais cités exigés (PG3-10) ; tentative après refus, jamais de seconde course
# (PG3-07) ; isolation et collisionneur rapportés de l'extrait (PG3-15) ; compagnon de LANCEMENT.md (PG3-16).
#
# Usage :
#   MODE=reel DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO07_USD=… APPEL_CONTROLE_FICHIER=… \
#       [TENTATIVE=2] [PYTEST_ARGS="--deselect …"] bash lancer_pilote_gemini_v4_question_v2.sh
#   MODE=simulation DEPOT=… PYTHON=… GRAINE=… [PILOTE_RACINE=… REGISTRE_GO_SOURCE=… DEPENSES_SOURCE=… RESTE_GO07_USD=…] …
#
# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course ou la sortie standard ; arrêter un
# processus par motif (R10 : PID consigné) ; écraser un dossier (R12) ; lancer une seconde course (R3).
set -euo pipefail
set +x

MODE="${MODE:?MODE=reel ou MODE=simulation}"
PY="${PYTHON:-python3}"
DEPOT="$(cd "${DEPOT:?DEPOT=racine du dépôt}" && pwd)"
R="$DEPOT/essaim-m3-refonte-v1"
GRAINE="${GRAINE:?GRAINE=graine de course du préenregistrement scellé}"
NOM="pilote-gemini-organisme-v4-question-v1"
RACINE_PILOTES="${PILOTE_RACINE:-$R/pilotes}"
TENTATIVE="${TENTATIVE:-1}"
case "$TENTATIVE" in ''|*[!0-9]*) echo "TENTATIVE doit être un entier" >&2; exit 2;; esac
if [ "$TENTATIVE" = 1 ]; then PILOTE="$RACINE_PILOTES/$NOM${SUFFIXE_ESSAI:-}"; else PILOTE="$RACINE_PILOTES/$NOM-tentative$TENTATIVE${SUFFIXE_ESSAI:-}"; fi

COMMIT_CODE=cec6dce3b1e2d4c1514f63914face859e8a59d97
COMMIT_LIENS=4967734a62a0b10c3b5cd6360e21924f015053fd
COMMIT_ORGANISME=b64bb3e4c0ae8fd500d09de939ff5a48dc7aec10
COMMIT_QUESTION=003995208431e825605bab9c4c1894b7508ad6ab
ARBRE_ORGANISME=c5ada33581fd7675f2cec5331d9a9a50ff80271b543c22eef80a64882730c1b9
SHA_QUESTION=d967b212082315c7b4fa1c42ab1b5d551b3bc1d3c4a98cdeb58eccd58b5b9441
SHA_BANQUE=f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc
SHA_MISSION=bd2c6a152f0b2c495dd1ed11362aade43fd1b03c245009f7479ecee43a357b7e
CODE_NOYAU_PROPRE=68494279ec42fc13366f83cc67c502c67ed6dcf97f0678bb568aaae8010772fb
CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-reecriture-vs-apprentissage-organismes-v1.md
# essais des gardes citées dans la liste d'arrêt du préenregistrement : chacun doit avoir passé ici (ni sauté ni désélectionné)
ESSAIS_CITES="test_fichiers_lecture_et_copie_sans_lien test_depot_ne_suit_aucun_lien_de_l_organisme test_organisme_poseur_de_liens_ne_voit_rien_du_noyau test_question_ouverte_cibles_lecture_et_archivage_sain_et_artefacts test_question_ouverte_posee_a_la_generation_ciblee_archivee_et_sans_effet_sur_le_score test_extrait_mecanique_sain_puis_artefacts test_mode_reel_refuse_sans_go test_mode_reel_refuse_anthropic_base_url test_bac_a_sable_isolation_reseau_refusee_si_indisponible test_appels_paralleles_plafond_tenu_au_pire_cas test_organisme_gourmand_recoit_plafond_sans_exception test_ce312_doit_arreter_et_raison_juste test_bac_a_sable_exception_et_delai test_modele_non_conforme_invalide_la_generation_et_arrete_la_lignee test_ce305_credit_epuise_arrete_la_course test_ce307_anomalie_journal_absent test_relance_puis_reprise_remet_le_compteur_a_zero test_fichier_stop_arrete_la_boucle test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus"
SAUTS_PERMIS="test_sources_reelles_de_moisson_si_reseau"

[ "$MODE" = reel ] || [ "$MODE" = simulation ] || { echo "MODE inconnu : $MODE" >&2; exit 2; }
# R3 : une course est partie dès que son manifeste est écrit ; aucune seconde course, quelle que soit la tentative
for d in "$RACINE_PILOTES/$NOM" "$RACINE_PILOTES/$NOM"-tentative*; do
  [ -d "$d" ] || continue
  if [ -f "$d/course/manifeste-run.json" ] || [ -f "$d/ferme.tar.gz" ]; then
    echo "REFUS : une course est déjà partie dans $d (R3 : jamais de seconde course)" >&2; exit 2
  fi
done
[ -e "$PILOTE" ] && { echo "REFUS : $PILOTE existe déjà (R12 ; après un refus avant le manifeste : TENTATIVE=$((TENTATIVE + 1)))" >&2; exit 2; }
mkdir -p "$PILOTE/ferme"
chmod 700 "$PILOTE/ferme"
L="$PILOTE/LANCEMENT.md"
refus() { echo "REFUS : $*" >&2; echo "- refus : $* ($(date -u +%Y-%m-%dT%H:%M:%SZ))" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256); exit 2; }
note() { echo "$*" >> "$L"; }
trap 'c=$?; echo "ÉCHEC inattendu (code $c) à la ligne $LINENO : arrêt" >&2; echo "- échec inattendu (code $c) à la ligne $LINENO ($(date -u +%Y-%m-%dT%H:%M:%SZ))" >> "$L"' ERR
{
  echo "# Lancement du pilote $NOM ($MODE, tentative $TENTATIVE)"
  echo
  echo "- début (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; hôte : $(hostname) ; utilisateur : $(id -u)"
  echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD) (c'est le « commit » que le manifeste consignera)"
  echo "- lanceur : $(basename "$0"), sha256 $(sha256sum "$0" | cut -d' ' -f1)"
} > "$L"

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
if [ "$MODE" = simulation ] && [ "${ESSAI_ARTEFACT:-}" = banque ]; then SHA_BANQUE=0000; fi
if [ "$MODE" = simulation ] && [ "${ESSAI_ARTEFACT:-}" = mission ]; then SHA_MISSION=0000; fi
[ "$(sha256sum "$R/banque/banque-confrontation-v1.json" | cut -d' ' -f1)" = "$SHA_BANQUE" ] || refus "empreinte de la banque ≠ f1387a20…"
[ "$(sha256sum "$R/MISSION-v1.md" | cut -d' ' -f1)" = "$SHA_MISSION" ] || refus "empreinte de la mission ≠ bd2c6a15…"
note "- code : identique à cec6dce (commit et arbre de travail : essaim_m3, tests) ; 4967734 ancêtre ; banque $SHA_BANQUE ; mission $SHA_MISSION"

# 2. Préenregistrement scellé (réel)
if [ "$MODE" = reel ]; then
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
if [ "$MODE" = simulation ] && [ "${ESSAI_ARTEFACT:-}" = organisme ]; then printf ' ' >> "$ORG/principal.py"; fi
n_fichiers="$(find "$ORG" -type f | wc -l)"
[ "$n_fichiers" = 16 ] || refus "organisme : $n_fichiers fichiers au lieu de 16"
empreinte_arbre() { (cd "$R" && "$PY" -B -I -c 'import pathlib, sys; sys.path.insert(0, "."); from essaim_m3.noyau import boucle; print(boucle.empreinte_arbre(pathlib.Path(sys.argv[1])))' "$1"); }
[ "$(empreinte_arbre "$ORG")" = "$ARBRE_ORGANISME" ] || refus "empreinte d'arbre de l'organisme ≠ c5ada335…"
git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" > "$PILOTE/question.md"
if [ "$MODE" = simulation ] && [ "${ESSAI_ARTEFACT:-}" = question ]; then printf '\n' >> "$PILOTE/question.md"; fi
[ "$(sha256sum "$PILOTE/question.md" | cut -d' ' -f1)" = "$SHA_QUESTION" ] || refus "empreinte de la question ≠ d967b212…"
note "- organisme : 16 fichiers, empreinte d'arbre $ARBRE_ORGANISME ; question : sha256 $SHA_QUESTION"

# 4. Registre des GO (extension inscrite), dépense consignée avant, reste sur la ligne ≥ 40 USD
if [ "$MODE" = reel ] || [ -n "${REGISTRE_GO_SOURCE:-}" ]; then
  if [ -n "${REGISTRE_GO_SOURCE:-}" ]; then cp "$REGISTRE_GO_SOURCE" "$PILOTE/registre-go.md"; else git -C "$DEPOT" show origin/main:registres/go.md > "$PILOTE/registre-go.md"; fi
  ligne="$(grep '^| GO-2026-10-24-07 |' "$PILOTE/registre-go.md" || true)"
  [ -n "$ligne" ] || refus "ligne GO-2026-10-24-07 absente du registre"
  echo "$ligne" | grep -q "calcul" || refus "ligne GO-2026-10-24-07 sans le type calcul"
  echo "$ligne" | grep -q "$NOM" || refus "extension de GO-2026-10-24-07 au pilote non inscrite (la ligne doit nommer $NOM)"
  if [ -n "${DEPENSES_SOURCE:-}" ]; then dep="$(cat "$DEPENSES_SOURCE")"; else dep="$(git -C "$DEPOT" show origin/main:registres/depenses.md)"; fi
  echo "$dep" | grep "$NOM" | grep -q "GO-2026-10-24-07" || refus "lancement non consigné avant dans registres/depenses.md (ligne nommant $NOM et GO-2026-10-24-07)"
  reste="${RESTE_GO07_USD:?RESTE_GO07_USD=reste disponible sur GO-2026-10-24-07, en USD}"
  "$PY" -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= 40.0 else 1)' "$reste" || refus "reste sur GO-2026-10-24-07 = $reste USD < 40"
  note "- registre : GO-2026-10-24-07 de type calcul, extension au pilote inscrite ; dépense consignée avant ; reste déclaré $reste USD ≥ 40"
fi

# 5. Appel de contrôle par espèce (réel), fait par l'outil de session-depot
if [ "$MODE" = reel ]; then
  f="${APPEL_CONTROLE_FICHIER:?APPEL_CONTROLE_FICHIER=résultat de l appel de contrôle par espèce}"
  [ -s "$f" ] || refus "résultat de l'appel de contrôle absent ou vide : $f"
  cp "$f" "$PILOTE/appel-controle-$(basename "$f")"
  note "- appel de contrôle : $(basename "$f"), sha256 $(sha256sum "$f" | cut -d' ' -f1) (statut OK vérifié par le lanceur)"
fi

# 6. Essais (en root en réel), puis code sans bytecode et empreinte du noyau
if [ "$MODE" = reel ] && [ "$(id -u)" != 0 ]; then refus "les essais et la course se font en root"; fi
resultat="$( (cd "$R" && PYTHONDONTWRITEBYTECODE=1 "$PY" -m pytest -q -p no:cacheprovider --junitxml "$PILOTE/essais-v1.xml" ${PYTEST_ARGS:-} 2>&1) | tail -1 || true)"
"$PY" -I -c '
import re, sys, xml.etree.ElementTree as ET
resume, junit, cites, permis = sys.argv[1], sys.argv[2], set(sys.argv[3].split()), set(sys.argv[4].split())
n = {k: int(v) for v, k in re.findall(r"(\d+) (passed|failed|errors?|skipped|deselected|xfailed|xpassed)", resume)}
try:
    cas = ET.parse(junit).getroot().iter("testcase")
except Exception as e:
    print(f"rapport JUnit illisible : {e}"); sys.exit(1)
etat = {}
for c in cas:
    e = "passe"
    for enfant in c:
        if enfant.tag in ("failure", "error"): e = "echec"
        elif enfant.tag == "skipped": e = "saute"
    etat[c.get("name")] = e
echecs = [k for k, v in etat.items() if v == "echec"]
sautes = [k for k, v in etat.items() if v == "saute"]
manquants = sorted(cites - {k for k, v in etat.items() if v == "passe"})
total = len(etat) + n.get("deselected", 0)
problemes = []
if echecs: problemes.append(f"échecs : {echecs}")
if set(sautes) - permis: problemes.append(f"sauts non permis : {sorted(set(sautes) - permis)}")
if manquants: problemes.append(f"essais cités non passés ici : {manquants}")
if total != 114: problemes.append(f"{total} essais au lieu de 114")
d = n.get("deselected", 0)
print("; ".join(problemes) if problemes else f"{len(etat) - len(sautes)} passés, {len(sautes)} sautés {sautes}, {d} désélectionnés")
sys.exit(1 if problemes else 0)' "$resultat" "$PILOTE/essais-v1.xml" "$ESSAIS_CITES" "$SAUTS_PERMIS" > "$PILOTE/essais-v1.txt" || refus "essais : $(cat "$PILOTE/essais-v1.txt") (résumé : « $resultat »)"
note "- essais : $(cat "$PILOTE/essais-v1.txt") ; arguments : « ${PYTEST_ARGS:-aucun} » ; tous les essais cités ont passé ici"
find "$R/essaim_m3" "$R/tests" -name __pycache__ -prune -exec rm -rf {} +
if [ "$MODE" = simulation ] && [ "${ESSAI_ARTEFACT:-}" = bytecode ]; then mkdir -p "$R/essaim_m3/noyau/__pycache__" && printf x > "$R/essaim_m3/noyau/__pycache__/x.pyc"; fi
code_noyau="$(empreinte_arbre "$R/essaim_m3/noyau")"
[ "$code_noyau" = "$CODE_NOYAU_PROPRE" ] || refus "empreinte du noyau nettoyé $code_noyau ≠ 68494279…"
note "- noyau sans bytecode : empreinte $code_noyau"

# 7. La course : sortie standard fermée (elle porte les scores), sortie d'erreur lisible ; PID consigné
COMMUNES=(--sortie "$PILOTE/course" --generations 2 --graine "$GRAINE" --especes --appels-max 160 --usd-par-generation 20
          --temps-max 1800 --max-tokens-appel 4096 --recherches-max 0 --telechargements-max 0 --entrainements-max 0
          --rondes-conception-max 0 --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 40 --decalage-uid 0
          --question-ouverte "$PILOTE/question.md" --question-ouverte-aux g001
          --organisme-impose "gemini-organisme-v4=$ORG@gemini")
SORTIE_FERMEE="$PILOTE/ferme/sortie-standard-lanceur.txt"
ERREURS="$PILOTE/sortie-erreur-lanceur.txt"
cd "$R"
if [ "$MODE" = reel ]; then
  [ -n "${ANTHROPIC_API_KEY:-}" ] || refus "ANTHROPIC_API_KEY absente"
  [ -n "${GEMINI_API_KEY_2:-}${GEMINI_API_KEY:-}" ] || refus "clé Gemini absente (GEMINI_API_KEY_2 ou GEMINI_API_KEY)"
  note "- clés : présentes (valeurs jamais lues ni écrites) ; clé Gemini passée sous GEMINI_API_KEY ($( [ -n "${GEMINI_API_KEY_2:-}" ] && echo 'n° 2' || echo 'n° 1')) ; ANTHROPIC_BASE_URL retirée"
  note "- départ (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  env -u ANTHROPIC_BASE_URL PYTHONDONTWRITEBYTECODE=1 GEMINI_API_KEY="${GEMINI_API_KEY_2:-${GEMINI_API_KEY:-}}" \
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
note "- fin de la course (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; code de retour : $CODE ; sortie standard fermée (non lue) ; sortie d'erreur : sortie-erreur-lanceur.txt (lisible)"

# 8. Après : extrait sans score, réponse et journaux recopiés ; archive fermée (course, sortie standard, espace) ;
#    copies ouvertes retirées une fois la liste de l'archive vérifiée
ESPACE=""
if [ -f "$PILOTE/course/manifeste-run.json" ]; then
  "$PY" -B -m essaim_m3.outils.extrait_mecanique --course "$PILOTE/course" --sortie "$PILOTE/extrait-mecanique-v1.json" > /dev/null \
    && note "- extrait mécanique : extrait-mecanique-v1.json, sha256 $(sha256sum "$PILOTE/extrait-mecanique-v1.json" | cut -d' ' -f1)" \
    || note "- extrait mécanique : REFUSÉ par l'outil (aucune écriture) — rapporté ; la course n'est pas ouverte"
  if [ -f "$PILOTE/extrait-mecanique-v1.json" ]; then
    "$PY" -I -c 'import json, sys; m = json.load(open(sys.argv[1]))["manifeste"]; print("- vérification après départ (extrait) : isolation " + json.dumps(m.get("isolation"), ensure_ascii=False) + " ; collisionneur conforme : " + str(m.get("collisionneur_conforme")) + " ; commit " + str(m.get("commit")) + " ; sha256_code_noyau " + str(m.get("sha256_code_noyau")))' "$PILOTE/extrait-mecanique-v1.json" >> "$L"
  fi
  ESPACE="$("$PY" -I -c 'import json, sys; print(json.load(open(sys.argv[1])).get("espace_organismes") or "")' "$PILOTE/course/manifeste-run.json")"
  for g in g000 g001; do
    a="$PILOTE/course/archive/gemini-organisme-v4/$g"
    if [ -f "$a/journal-appels.jsonl" ] && [ ! -L "$a/journal-appels.jsonl" ]; then
      cp "$a/journal-appels.jsonl" "$PILOTE/journal-appels-$g.jsonl"
      [ -f "$a/journal-appels.jsonl.sha256" ] && cp "$a/journal-appels.jsonl.sha256" "$PILOTE/journal-appels-$g.jsonl.sha256-archive"
      note "- journal des appels $g : journal-appels-$g.jsonl, sha256 $(sha256sum "$PILOTE/journal-appels-$g.jsonl" | cut -d' ' -f1)"
    fi
  done
  rq="$PILOTE/course/archive/gemini-organisme-v4/g001/reponse-question.md"
  if [ -f "$rq" ] && [ ! -L "$rq" ]; then
    cp "$rq" "$PILOTE/reponse-question-g001.md"; [ -f "$rq.sha256" ] && cp "$rq.sha256" "$PILOTE/reponse-question-g001.md.sha256-archive"
    note "- réponse à la question : reponse-question-g001.md, sha256 $(sha256sum "$PILOTE/reponse-question-g001.md" | cut -d' ' -f1)"
  else
    note "- réponse à la question : aucune pièce archivée (voir l'extrait : champ question_ouverte de g001, ou g001 absente)"
  fi
else
  note "- aucune course écrite (refus avant le manifeste : voir sortie-erreur-lanceur.txt) ; une tentative suivante est permise (TENTATIVE=$((TENTATIVE + 1)))"
fi
if [ -d "$PILOTE/course" ]; then
  args=(-C "$PILOTE" course ferme)
  espace_a_retirer=""
  if [ -n "$ESPACE" ] && [ -d "$ESPACE" ] && [ "$(cd "$ESPACE" && pwd)" != "$(cd "$PILOTE/course" && pwd)" ]; then
    case "$ESPACE" in /var/tmp/essaim-m3/[0-9a-f]*) args+=(-C / "${ESPACE#/}"); espace_a_retirer="$ESPACE";; *) note "- espace des organismes hors de /var/tmp/essaim-m3 : $ESPACE — non archivé, non retiré, réserve";; esac
  fi
  set +e; tar --warning=no-file-ignored -czf "$PILOTE/ferme.tar.gz" "${args[@]}"; code_tar=$?; set -e
  (cd "$PILOTE" && sha256sum ferme.tar.gz > ferme.tar.gz.sha256)
  n_archive="$(tar -tzf "$PILOTE/ferme.tar.gz" | wc -l)"
  n_disque="$( { (cd "$PILOTE" && find course ferme ! -type s); [ -n "$espace_a_retirer" ] && (cd / && find "${espace_a_retirer#/}" ! -type s); } | wc -l)"
  if [ "$code_tar" = 0 ] && [ "$n_archive" = "$n_disque" ]; then
    rm -rf "$PILOTE/course" "$PILOTE/ferme"; [ -n "$espace_a_retirer" ] && rm -rf "$espace_a_retirer"
    note "- archive fermée : ferme.tar.gz (course, sortie standard, espace des organismes), sha256 $(cut -d' ' -f1 < "$PILOTE/ferme.tar.gz.sha256"), $n_archive entrées = $n_disque sur disque ; copies ouvertes retirées"
  else
    note "- ARCHIVE FERMÉE INCOMPLÈTE : code tar $code_tar, $n_archive entrées contre $n_disque sur disque — copies ouvertes gardées dans ce conteneur, jamais lues ni poussées — réserve"
  fi
fi
note "- fin du lanceur (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
(cd "$PILOTE" && sha256sum sortie-erreur-lanceur.txt > sortie-erreur-lanceur.txt.sha256 2>/dev/null || true)
(cd "$PILOTE" && find . \( -path ./course -o -path ./ferme \) -prune -o -type f ! -name 'EMPREINTES-pilote-v1.txt*' ! -name 'A-POUSSER-v1.txt' ! -name 'LANCEMENT.md.sha256' -print | sed 's#^\./##' | sort > A-POUSSER-v1.txt)
(cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256 && echo "LANCEMENT.md.sha256" >> A-POUSSER-v1.txt && echo "A-POUSSER-v1.txt" >> A-POUSSER-v1.txt \
   && grep -v '^A-POUSSER-v1.txt$' A-POUSSER-v1.txt | xargs sha256sum > EMPREINTES-pilote-v1.txt && sha256sum EMPREINTES-pilote-v1.txt > EMPREINTES-pilote-v1.txt.sha256)
echo "pilote fini : $PILOTE — à pousser : les fichiers de A-POUSSER-v1.txt et les deux fichiers d'empreintes ; jamais course/ ni ferme/"
exit 0
