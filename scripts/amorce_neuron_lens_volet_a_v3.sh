#!/usr/bin/env bash
# Amorce de la machine louée pour la course du volet A de « Neuron Lens » — v3 (commande v6, sans ssh ; décision de la mère
# R-2752). v3 : contre-lecture 7 (remarques 4, 5, 6, 12) — poussée finale en échec après une course réussie = code 15, dernière ligne
# « POUSSEE FINALE EN ECHEC » (les résultats ne sont alors que sur le disque de l'instance : ne pas la détruire sans la mère) ; nombre
# et espacement des essais de la poussée finale réglables (essai à blanc) ; fichier de plus de 95 Mo exclu AVANT `git add` (il reste
# sur le disque de l'instance, journalisé), jamais commité ; aucun arbre des résultats = échec journalisé (plus de retour silencieux) ;
# aucune attente après la dernière tentative ; cause d'un échec de poussée sur deux lignes ; `pip` épinglé ; code 13 journalisé ; garde
# de la carte graphique essayable en mode jouet (EXIGER_CARTE_JOUET=1). v2 : contre-lecture 6 — première poussée fatale (code 14),
# poussée finale persistante, jeton retiré de l'environnement de pip et de pytest, 30 dernières lignes des essais.
#
# Lancée par l'entrée de l'instance après le clone de la seule branche du dépôt réduit (`--depth 1 --single-branch`). Étapes :
#   1. commit du dépôt réduit égal à COMMIT_REDUIT, arbre propre ; sinon arrêt (code 10, journaux du loueur seulement) ;
#   2. environnement Python (versions épinglées), carte graphique exigée (code 11) ; première poussée impossible (code 14 ; la
#      location court déjà, mais aucune passe n'a commencé) ;
#   3. essais rapides : un échec, un essai sauté ou un arbre sali = arrêt (code 12) ;
#   4. course (`volet_a_lancer_v3`) en arrière-plan, **sans** le jeton dans son environnement ; COMMANDE_COURSE hors du mode jouet =
#      arrêt (code 13) ;
#   5. toutes les PERIODE_POUSSE_S secondes, puis à la fin (et à tout arrêt), les `runs/<run_id>/` et `diag/<run_id>/` déjà écrits
#      et un fichier d'état sont poussés sur la branche BRANCHE_RESULTATS (jamais `main`), par un arbre de travail séparé ;
#   6. poussée finale en échec alors que tout le reste a réussi : code 15 (sinon le code d'origine est gardé).
# Seul secret : GH_TOKEN (jeton du programme, passé par son nom à la création), jamais affiché ni écrit dans un fichier : il ne sert
# qu'en en-tête HTTP passé à chaque commande `git` (`-c http.extraHeader`), l'adresse du dépôt n'en contient pas. (Il reste dans
# l'environnement du processus d'entrée de l'instance, la ligne de commande des `git` pendant leur durée et la configuration du loueur.)
# Variables : COMMIT_REDUIT (exigée), GO_ID (exigée, transmise au lanceur), BRANCHE_RESULTATS, PERIODE_POUSSE_S (1800), RUN_ID,
# CACHE_HF (/workspace/hf), ESSAIS_POUSSEE_FINALE (10), ATTENTE_POUSSEE_FINALE_S (60). Mode jouet (essai à blanc, sans location) :
# MODE_JOUET=1, VENV_JOUET (environnement existant), COMMANDE_COURSE (remplace la course), ESSAIS (remplace la liste des essais),
# EXIGER_CARTE_JOUET=1 (joue la garde de la carte graphique avec l'interprète du mode jouet).
set -euo pipefail
set +x
umask 022

DEPOT=$(cd "$(dirname "$0")/.." && pwd)
RESULTATS="$DEPOT/../resultats-neuron-lens"
: "${COMMIT_REDUIT:?COMMIT_REDUIT exigé}"
: "${GO_ID:?GO_ID exigé}"
BRANCHE_RESULTATS=${BRANCHE_RESULTATS:-calcul/neuron-lens-volet-a-v1}
PERIODE=${PERIODE_POUSSE_S:-1800}
RUN_ID=${RUN_ID:-$(date -u +%Y%m%d-%H%M%S)-neuron-lens-volet-a}
CACHE_HF=${CACHE_HF:-/workspace/hf}
N_FINALE=${ESSAIS_POUSSEE_FINALE:-10}
ATTENTE_FINALE=${ATTENTE_POUSSEE_FINALE_S:-60}
MODE_JOUET=${MODE_JOUET:-0}
ESSAIS=${ESSAIS:-"tests/test_neuron_lens_volet_a_extraction_v2.py tests/test_neuron_lens_volet_a_chargement_v1.py tests/test_neuron_lens_volet_a_lancer_v3.py tests/test_neuron_lens_volet_a_donnees_v1.py tests/test_neuron_lens_volet_a_donnees_v2.py tests/test_neuron_lens_volet_a_sondes_v2.py tests/test_neuron_lens_volet_a_lectures_v2.py tests/test_neuron_lens_garde_depense_v3.py"}
ETAT="demarrage"
LIMITE=$((95 * 1024 * 1024))

log() { echo "AMORCE $(date -u +%FT%TZ) $*"; }

git_jeton() {  # git avec le jeton en en-tête seulement (jamais dans l'adresse, la configuration ni la sortie)
  local h
  h="Authorization: Basic $(printf 'x-access-token:%s' "${GH_TOKEN:-}" | base64 -w0)"
  git -c http.extraHeader="$h" "$@"
}

exclure_gros() {  # fichiers de plus de 95 Mo retirés de l'arbre des résultats AVANT `git add` (ils restent dans $DEPOT)
  local f
  while IFS= read -r -d '' f; do
    rm -f -- "$f"
    log "fichier de plus de 95 Mo exclu de la poussee (reste sur le disque de l'instance) : ${f#"$RESULTATS"/}"
  done < <(find "$RESULTATS/runs" "$RESULTATS/diag" -type f -size +"$((LIMITE / 1024))"k -print0 2>/dev/null)
}

pousser() {  # copie des résultats déjà écrits et de l'état, commit et poussée ; arguments : nombre d'essais, attente fixe (0 = 2^i)
  if [ ! -d "$RESULTATS" ]; then log "pas d'arbre des resultats : rien pousse ($ETAT)"; return 1; fi
  mkdir -p "$RESULTATS/runs" "$RESULTATS/diag"
  [ -d "$DEPOT/runs/$RUN_ID" ] && cp -a "$DEPOT/runs/$RUN_ID" "$RESULTATS/runs/" || true
  [ -d "$DEPOT/diag/$RUN_ID" ] && cp -a "$DEPOT/diag/$RUN_ID" "$RESULTATS/diag/" || true
  exclure_gros
  printf 'run_id=%s\netat=%s\nheure=%s\ncommit_reduit=%s\n' "$RUN_ID" "$ETAT" "$(date -u +%FT%TZ)" "$COMMIT_REDUIT" \
    > "$RESULTATS/etat-neuron-lens-volet-a.txt"
  git -C "$RESULTATS" add -A
  if ! git -C "$RESULTATS" diff --cached --quiet; then
    git -C "$RESULTATS" -c user.name=neuron-lens -c user.email=neuron-lens@example.invalid commit -q -m "Neuron Lens, volet A : $ETAT"
  fi
  local i n attente err
  n=${1:-4}; attente=${2:-0}
  for i in $(seq 1 "$n"); do
    if err=$(git_jeton -C "$RESULTATS" push -q origin "HEAD:refs/heads/$BRANCHE_RESULTATS" 2>&1); then
      log "pousse : $ETAT"
      return 0
    fi
    log "poussee refusee (essai $i/$n) : $(printf '%s\n' "$err" | tail -2 | tr '\n' ' ' | cut -c1-200)"
    if [ "$i" -lt "$n" ]; then
      if [ "$attente" -gt 0 ]; then sleep "$attente"; else sleep $((2 ** i)); fi
    fi
  done
  log "poussee en echec : $ETAT"
  return 1
}

fin() {
  local code=$?
  [ "$code" -ne 0 ] && ETAT="arret code $code ($ETAT)"
  if [ ! -d "$RESULTATS" ]; then log "fin sans arbre des resultats : $ETAT"; exit "$code"; fi
  if pousser "$N_FINALE" "$ATTENTE_FINALE"; then
    log "fin : $ETAT"
    exit "$code"
  fi
  log "fin : $ETAT"
  log "POUSSEE FINALE EN ECHEC : resultats seulement sur le disque de l'instance, ne pas la detruire sans la mere"
  if [ "$code" -eq 0 ]; then exit 15; fi
  exit "$code"
}
trap fin EXIT

# 1. commit et arbre
cd "$DEPOT"
TETE=$(git rev-parse HEAD)
if [ "$TETE" != "$COMMIT_REDUIT" ]; then ETAT="commit inattendu $TETE"; log "$ETAT"; exit 10; fi
if [ -n "$(git status --porcelain)" ]; then ETAT="arbre non propre"; log "$ETAT"; exit 10; fi
git worktree add -q -b "$BRANCHE_RESULTATS" "$RESULTATS" HEAD
log "commit reduit verifie : $TETE ; run_id=$RUN_ID"

# 2. environnement et carte graphique
if [ "$MODE_JOUET" = 1 ]; then
  PY="${VENV_JOUET:?VENV_JOUET exigé en mode jouet}/bin/python"
else
  python3 -m venv .venv
  env -u GH_TOKEN .venv/bin/pip install -q pip==26.2.2
  env -u GH_TOKEN .venv/bin/pip install -q -r requirements-neuron-lens-volet-a-v1.txt
  PY="$DEPOT/.venv/bin/python"
fi
if [ "$MODE_JOUET" != 1 ] || [ "${EXIGER_CARTE_JOUET:-0}" = 1 ]; then
  if ! env -u GH_TOKEN "$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)'; then
    ETAT="carte graphique indisponible"; log "$ETAT"; exit 11
  fi
  log "carte : $(env -u GH_TOKEN "$PY" -c 'import torch; print(torch.cuda.get_device_name(0))')"
fi
ETAT="environnement pret"
if ! pousser; then ETAT="premiere poussee impossible"; log "$ETAT"; exit 14; fi  # avant toute passe

# 3. essais rapides : échec, essai sauté ou arbre sali = arrêt
ETAT="essais"
set +e
# shellcheck disable=SC2086
SORTIE=$(env -u GH_TOKEN PYTHONPATH=src "$PY" -m pytest -q -rs -p no:cacheprovider $ESSAIS 2>&1)
CODE=$?
set -e
printf '%s\n' "$SORTIE" | tail -30
if [ "$CODE" -ne 0 ] || printf '%s\n' "$SORTIE" | grep -qiE '[0-9]+ skipped'; then
  ETAT="essais en echec ou sautes"; log "$ETAT"; exit 12
fi
if [ -n "$(git status --porcelain)" ]; then ETAT="arbre sali par les essais"; log "$ETAT"; exit 12; fi
ETAT="essais passes"; pousser || true

# 4. course, sans le jeton dans son environnement
ETAT="course en cours"
if [ -n "${COMMANDE_COURSE:-}" ]; then
  if [ "$MODE_JOUET" != 1 ]; then ETAT="COMMANDE_COURSE hors du mode jouet"; log "$ETAT"; exit 13; fi
  env -u GH_TOKEN RUN_ID="$RUN_ID" bash -c "$COMMANDE_COURSE" &
else
  env -u GH_TOKEN GO_ID="$GO_ID" PYTHONPATH=src "$PY" -m controle_ia.neuron_lens.volet_a_lancer_v3 \
    --run-id "$RUN_ID" --cache "$CACHE_HF" --appareil cuda &
fi
PID_COURSE=$!
log "course lancee, PID $PID_COURSE"

# 5. poussées périodiques pendant la course
while kill -0 "$PID_COURSE" 2>/dev/null; do
  for _ in $(seq 1 "$PERIODE"); do kill -0 "$PID_COURSE" 2>/dev/null || break; sleep 1; done
  if kill -0 "$PID_COURSE" 2>/dev/null; then pousser || true; fi
done
set +e
wait "$PID_COURSE"
CODE=$?
set -e
if [ "$CODE" -eq 0 ]; then ETAT="course terminee"; else ETAT="course en echec (code $CODE)"; fi
log "$ETAT"
exit "$CODE"
