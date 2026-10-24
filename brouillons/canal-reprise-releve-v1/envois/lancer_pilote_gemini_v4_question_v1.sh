#!/usr/bin/env bash
# Lanceur du pilote descriptif « organisme de Gemini v4 + question ouverte à g001 » (v1), écrit par conv-audit pour
# session-depot (qui tient les clés et lance). Met en œuvre, pas à pas, le plan § 1 et § 3 du préenregistrement scellé
# `essaim-m3-refonte-v1/prereg/pilote-gemini-organisme-v4-question-v2.md` (ou du nom scellé donné par PREREG).
#
# Usage (depuis n'importe où ; DEPOT = racine du dépôt controle-ia-travail, branche de code à jour) :
#   MODE=reel  DEPOT=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO07_USD=… APPEL_CONTROLE_FICHIER=… \
#       bash lancer_pilote_gemini_v4_question_v1.sh
#   MODE=simulation DEPOT=… GRAINE=… [REGISTRE_GO_SOURCE=… DEPENSES_SOURCE=…] bash lancer_pilote_gemini_v4_question_v1.sh
#
# Ce que ce script ne fait jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course après la
# fin (il archive `course/` sans l'ouvrir, et n'en copie que la réponse à la question et l'extrait mécanique sans
# score) ; arrêter un processus par motif (R10 : PID consigné) ; écraser un dossier existant (R12).
set -euo pipefail
set +x

refus() { echo "REFUS : $*" >&2; [ -n "${PILOTE:-}" ] && [ -d "${PILOTE:-}" ] && echo "- refus : $* ($(date -u +%Y-%m-%dT%H:%M:%SZ))" >> "$PILOTE/LANCEMENT.md"; exit 2; }
note() { echo "$*" >> "$PILOTE/LANCEMENT.md"; }

MODE="${MODE:?MODE=reel ou MODE=simulation}"
PY="${PYTHON:-python3}"   # l'interpréteur de l'environnement des courses (numpy, pytest)
DEPOT="$(cd "${DEPOT:?DEPOT=racine du dépôt}" && pwd)"
R="$DEPOT/essaim-m3-refonte-v1"
GRAINE="${GRAINE:?GRAINE=graine de course du préenregistrement scellé}"
NOM="pilote-gemini-organisme-v4-question-v1"
PILOTE="${PILOTE_RACINE:-$R/pilotes}/$NOM${SUFFIXE_ESSAI:-}"

COMMIT_CODE=cec6dce3b1e2d4c1514f63914face859e8a59d97
COMMIT_LIENS=4967734a62a0b10c3b5cd6360e21924f015053fd
COMMIT_ORGANISME=b64bb3e4c0ae8fd500d09de939ff5a48dc7aec10
COMMIT_QUESTION=003995208431e825605bab9c4c1894b7508ad6ab
ARBRE_ORGANISME=c5ada33581fd7675f2cec5331d9a9a50ff80271b543c22eef80a64882730c1b9
SHA_QUESTION=d967b212082315c7b4fa1c42ab1b5d551b3bc1d3c4a98cdeb58eccd58b5b9441
CODE_NOYAU_PROPRE=68494279ec42fc13366f83cc67c502c67ed6dcf97f0678bb568aaae8010772fb
CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-reecriture-vs-apprentissage-organismes-v1.md

[ "$MODE" = reel ] || [ "$MODE" = simulation ] || { echo "MODE inconnu : $MODE" >&2; exit 2; }
[ -e "$PILOTE" ] && { echo "REFUS : $PILOTE existe déjà (R12 : jamais réécrit)" >&2; exit 2; }
mkdir -p "$PILOTE"
# R5 : aucun arrêt silencieux — toute commande qui échoue hors des refus nommés est consignée avant la sortie
trap 'c=$?; echo "ÉCHEC inattendu (code $c) à la ligne $LINENO : le pilote ne part pas" >&2; echo "- échec inattendu (code $c) à la ligne $LINENO ($(date -u +%Y-%m-%dT%H:%M:%SZ))" >> "$PILOTE/LANCEMENT.md"' ERR
{
  echo "# Lancement du pilote $NOM ($MODE)"
  echo
  echo "- début (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; hôte : $(hostname) ; utilisateur : $(id -u)"
  echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD)"
  echo "- lanceur : $(basename "$0"), sha256 $(sha256sum "$0" | cut -d' ' -f1)"
} > "$PILOTE/LANCEMENT.md"

# 1. Code : identique à cec6dce (essaim_m3 et tests), correctif des liens présent
for c in "$COMMIT_CODE" "$COMMIT_LIENS" "$COMMIT_ORGANISME" "$COMMIT_QUESTION"; do
  git -C "$DEPOT" cat-file -e "$c^{commit}" 2>/dev/null || refus "commit $c absent du dépôt (git fetch des branches outils/essaim-m3-gradient-v1-travail, outils/gemini-organisme-v4, canal/conv-audit-n04)"
done
git -C "$DEPOT" diff --quiet "$COMMIT_CODE" HEAD -- essaim-m3-refonte-v1/essaim_m3 essaim-m3-refonte-v1/tests || refus "code de HEAD différent de cec6dce (essaim_m3 ou tests)"
git -C "$DEPOT" diff --quiet -- essaim-m3-refonte-v1/essaim_m3 essaim-m3-refonte-v1/tests || refus "modifications non commises dans essaim_m3 ou tests"
git -C "$DEPOT" diff --cached --quiet -- essaim-m3-refonte-v1/essaim_m3 essaim-m3-refonte-v1/tests || refus "modifications indexées dans essaim_m3 ou tests"
inattendus="$(git -C "$DEPOT" status --porcelain --untracked-files=all -- essaim-m3-refonte-v1/essaim_m3 essaim-m3-refonte-v1/tests | grep -v '__pycache__' || true)"
[ -z "$inattendus" ] || refus "fichiers non suivis dans essaim_m3 ou tests : $inattendus"
git -C "$DEPOT" merge-base --is-ancestor "$COMMIT_LIENS" HEAD || refus "correctif des liens 4967734 non ancêtre de HEAD"
note "- code : identique à cec6dce (essaim_m3, tests), arbre propre ; 4967734 ancêtre : oui"

# 2. Préenregistrement scellé (réel) ; graine écrite dans le texte scellé
if [ "$MODE" = reel ]; then
  PREREG="${PREREG:?PREREG=chemin du préenregistrement scellé}"; PREREG_SHA256="${PREREG_SHA256:?}"
  [ "$(sha256sum "$PREREG" | cut -d' ' -f1)" = "$PREREG_SHA256" ] || refus "empreinte du préenregistrement ≠ PREREG_SHA256"
  [ -f "$PREREG.sha256" ] && [ "$(cut -d' ' -f1 < "$PREREG.sha256")" = "$PREREG_SHA256" ] || refus "compagnon .sha256 du préenregistrement absent ou différent"
  grep -q "= $GRAINE\b" "$PREREG" || refus "la graine $GRAINE n'est pas écrite dans le préenregistrement scellé"
  if grep -q "<<[A-Z0-9_]*>>" "$PREREG"; then refus "marqueurs <<…>> restants : préenregistrement non scellable"; fi
  note "- préenregistrement : $PREREG, sha256 $PREREG_SHA256 (compagnon conforme), graine $GRAINE écrite"
fi

# 3. Organisme v4 et question, extraits des commits cités, vérifiés
git -C "$DEPOT" archive "$COMMIT_ORGANISME" outils/gemini-organisme-v4/organisme | tar -x -C "$PILOTE"
ORG="$PILOTE/outils/gemini-organisme-v4/organisme"
if [ "$MODE" = simulation ] && [ "${ESSAI_ARTEFACT:-}" = organisme ]; then printf ' ' >> "$ORG/principal.py"; fi   # artefact d'essai
n_fichiers="$(find "$ORG" -type f | wc -l)"
[ "$n_fichiers" = 16 ] || refus "organisme : $n_fichiers fichiers au lieu de 16"
empreinte_arbre() { (cd "$R" && "$PY" -B -I -c 'import pathlib, sys; sys.path.insert(0, "."); from essaim_m3.noyau import boucle; print(boucle.empreinte_arbre(pathlib.Path(sys.argv[1])))' "$1"); }
[ "$(empreinte_arbre "$ORG")" = "$ARBRE_ORGANISME" ] || refus "empreinte d'arbre de l'organisme ≠ c5ada335…"
git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" > "$PILOTE/question.md"
if [ "$MODE" = simulation ] && [ "${ESSAI_ARTEFACT:-}" = question ]; then printf '\n' >> "$PILOTE/question.md"; fi   # artefact d'essai
[ "$(sha256sum "$PILOTE/question.md" | cut -d' ' -f1)" = "$SHA_QUESTION" ] || refus "empreinte de la question ≠ d967b212…"
note "- organisme : 16 fichiers, empreinte d'arbre $ARBRE_ORGANISME ; question : sha256 $SHA_QUESTION"

# 4. Registre des GO (extension au pilote inscrite), dépense consignée avant, reste sur la ligne ≥ 40 USD
if [ "$MODE" = reel ] || [ -n "${REGISTRE_GO_SOURCE:-}" ]; then
  if [ -n "${REGISTRE_GO_SOURCE:-}" ]; then cp "$REGISTRE_GO_SOURCE" "$PILOTE/registre-go.md"; else git -C "$DEPOT" show origin/main:registres/go.md > "$PILOTE/registre-go.md"; fi
  ligne="$(grep '^| GO-2026-10-24-07 |' "$PILOTE/registre-go.md" || true)"
  [ -n "$ligne" ] || refus "ligne GO-2026-10-24-07 absente du registre"
  echo "$ligne" | grep -q "calcul" || refus "ligne GO-2026-10-24-07 sans le type calcul"
  echo "$ligne" | grep -q "$NOM" || refus "extension de GO-2026-10-24-07 au pilote non inscrite (la ligne doit nommer $NOM)"
  if [ -n "${DEPENSES_SOURCE:-}" ]; then dep="$(cat "$DEPENSES_SOURCE")"; else dep="$(git -C "$DEPOT" show origin/main:registres/depenses.md)"; fi
  echo "$dep" | grep "$NOM" | grep -q "GO-2026-10-24-07" || refus "lancement non consigné avant dans registres/depenses.md (ligne nommant $NOM et GO-2026-10-24-07)"
  reste="${RESTE_GO07_USD:?RESTE_GO07_USD=reste disponible sur la ligne GO-2026-10-24-07, en USD (vérification du lanceur)}"
  "$PY" -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= 40.0 else 1)' "$reste" || refus "reste sur GO-2026-10-24-07 = $reste USD < 40"
  note "- registre : ligne GO-2026-10-24-07 de type calcul, extension au pilote inscrite ; dépense consignée avant ; reste déclaré $reste USD ≥ 40"
fi

# 5. Appel de contrôle par espèce (réel) : fait par l'outil de session-depot, résultat joint
if [ "$MODE" = reel ]; then
  f="${APPEL_CONTROLE_FICHIER:?APPEL_CONTROLE_FICHIER=résultat de l appel de contrôle par espèce (statut OK exigé)}"
  [ -s "$f" ] || refus "résultat de l'appel de contrôle absent ou vide : $f"
  cp "$f" "$PILOTE/appel-controle-$(basename "$f")"
  note "- appel de contrôle : $(basename "$f"), sha256 $(sha256sum "$f" | cut -d' ' -f1) (statut OK vérifié par le lanceur)"
fi

# 6. Essais, puis code nettoyé du bytecode et empreinte du noyau
resultat="$( (cd "$R" && PYTHONDONTWRITEBYTECODE=1 "$PY" -m pytest -q -p no:cacheprovider ${PYTEST_ARGS:-} 2>&1) | tail -1 || true)"
"$PY" -I -c '
import re, sys
r = sys.argv[1]
n = {k: int(v) for v, k in re.findall(r"(\d+) (passed|failed|errors?|skipped|deselected|xfailed|xpassed)", r)}
ok = n.get("passed", 0) > 0 and not any(n.get(k, 0) for k in ("failed", "error", "errors", "xpassed")) \
     and n.get("passed", 0) + n.get("deselected", 0) + n.get("skipped", 0) == 114
sys.exit(0 if ok else 1)' "$resultat" || refus "essais : « $resultat » (attendu : 114 essais, aucun échec ; désélectionnés ou sautés comptés)"
find "$R/essaim_m3" "$R/tests" -name __pycache__ -prune -exec rm -rf {} +
if [ "$MODE" = simulation ] && [ "${ESSAI_ARTEFACT:-}" = bytecode ]; then mkdir -p "$R/essaim_m3/noyau/__pycache__" && printf x > "$R/essaim_m3/noyau/__pycache__/x.pyc"; fi   # artefact d'essai
code_noyau="$(empreinte_arbre "$R/essaim_m3/noyau")"
[ "$code_noyau" = "$CODE_NOYAU_PROPRE" ] || refus "empreinte du noyau nettoyé $code_noyau ≠ 68494279…"
find "$R/essaim_m3" -name __pycache__ | grep -q . && refus "bytecode réapparu sous essaim_m3"
note "- essais : $resultat ; noyau sans bytecode : empreinte $code_noyau"

# 7. La course : une seule, jamais relancée ; sortie redirigée, non lue ; PID consigné
COMMUNES=(--sortie "$PILOTE/course" --generations 2 --graine "$GRAINE" --especes --appels-max 160 --usd-par-generation 20
          --temps-max 1800 --max-tokens-appel 4096 --recherches-max 0 --telechargements-max 0 --entrainements-max 0
          --rondes-conception-max 0 --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 40 --decalage-uid 0
          --question-ouverte "$PILOTE/question.md" --question-ouverte-aux g001
          --organisme-impose "gemini-organisme-v4=$ORG@gemini")
cd "$R"
if [ "$MODE" = reel ]; then
  [ "$(id -u)" = 0 ] || refus "le mode réel exige root (isolation d'utilisateur)"
  [ -n "${ANTHROPIC_API_KEY:-}" ] || refus "ANTHROPIC_API_KEY absente"
  [ -n "${GEMINI_API_KEY_2:-}${GEMINI_API_KEY:-}" ] || refus "clé Gemini absente (GEMINI_API_KEY_2 ou GEMINI_API_KEY)"
  note "- clés : présentes (valeurs jamais lues ni écrites) ; clé Gemini passée sous GEMINI_API_KEY ($( [ -n "${GEMINI_API_KEY_2:-}" ] && echo 'n° 2' || echo 'n° 1')) ; ANTHROPIC_BASE_URL retirée"
  note "- départ de la course (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  env -u ANTHROPIC_BASE_URL PYTHONDONTWRITEBYTECODE=1 GEMINI_API_KEY="${GEMINI_API_KEY_2:-${GEMINI_API_KEY:-}}" \
    "$PY" -m essaim_m3 lancer --reel --go GO-2026-10-24-07 --registre-go "$PILOTE/registre-go.md" \
      --taches banque/banque-confrontation-v1.json --mission MISSION-v1.md "${COMMUNES[@]}" \
      > "$PILOTE/sortie-lanceur.txt" 2>&1 &
else
  note "- départ de la course de simulation (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  PYTHONDONTWRITEBYTECODE=1 "$PY" -m essaim_m3 simuler "${COMMUNES[@]}" --n-train 80 --n-test 60 --n-final 60 \
      > "$PILOTE/sortie-lanceur.txt" 2>&1 &
fi
PID=$!
note "- PID de la course : $PID (arrêt humain par ce PID seulement, R10 ; un fichier STOP dans course/ arrête à la fin de la génération)"
set +e; wait "$PID"; CODE=$?; set -e
note "- fin de la course (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; code de retour : $CODE (sortie standard et d'erreur dans sortie-lanceur.txt, non lue)"

# 8. Après la course : extrait mécanique sans score ; réponse à la question ; course archivée sans l'ouvrir
if [ -f "$PILOTE/course/manifeste-run.json" ]; then
  "$PY" -B -m essaim_m3.outils.extrait_mecanique --course "$PILOTE/course" --sortie "$PILOTE/extrait-mecanique-v1.json" > /dev/null \
    && note "- extrait mécanique : extrait-mecanique-v1.json, sha256 $(sha256sum "$PILOTE/extrait-mecanique-v1.json" | cut -d' ' -f1)" \
    || note "- extrait mécanique : REFUSÉ par l'outil (aucune écriture) — rapporté, la course n'est pas ouverte"
  rq="$PILOTE/course/archive/gemini-organisme-v4/g001/reponse-question.md"
  if [ -f "$rq" ] && [ ! -L "$rq" ]; then
    cp "$rq" "$PILOTE/reponse-question-g001.md"; [ -f "$rq.sha256" ] && cp "$rq.sha256" "$PILOTE/reponse-question-g001.md.sha256-archive"
    note "- réponse à la question : reponse-question-g001.md, sha256 $(sha256sum "$PILOTE/reponse-question-g001.md" | cut -d' ' -f1)"
  else
    note "- réponse à la question : aucune pièce archivée (voir l'extrait mécanique : champ question_ouverte de g001)"
  fi
else
  note "- aucune course écrite (refus du noyau avant le manifeste : voir le code de retour)"
fi
if [ -d "$PILOTE/course" ]; then
  set +e; tar --warning=no-file-ignored -czf "$PILOTE/course.tar.gz" -C "$PILOTE" course; code_tar=$?; set -e
  [ "$code_tar" = 0 ] || note "- ARCHIVE DE LA COURSE : tar a rendu le code $code_tar (archive possiblement partielle) — réserve"
  (cd "$PILOTE" && sha256sum course.tar.gz > course.tar.gz.sha256)
  note "- course archivée sans être ouverte : course.tar.gz, sha256 $(cut -d' ' -f1 < "$PILOTE/course.tar.gz.sha256") ; course/ reste dans ce conteneur"
fi
(cd "$PILOTE" && sha256sum sortie-lanceur.txt > sortie-lanceur.txt.sha256)
note "- fin du lanceur (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
(cd "$PILOTE" && find . -path ./course -prune -o -type f ! -name 'EMPREINTES-pilote-v1.txt' -print | sed 's#^\./##' | sort \
   | xargs sha256sum > EMPREINTES-pilote-v1.txt && sha256sum EMPREINTES-pilote-v1.txt > EMPREINTES-pilote-v1.txt.sha256)
echo "pilote fini : $PILOTE (LANCEMENT.md ; à pousser : tout sauf course/, voir EMPREINTES-pilote-v1.txt)"
exit 0
