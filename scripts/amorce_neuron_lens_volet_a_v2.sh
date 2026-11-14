#!/usr/bin/env bash
# Amorce de la machine louée pour la course du volet A de « Neuron Lens » — v2 (commande v5, sans ssh ; décision de la mère
# R-2752). v2 : contre-lecture de la commande v4 (remarques 4, 5, 6, 10) — première poussée fatale (code 14, avant toute dépense de
# carte graphique) ; poussée finale persistante ; cause d'un échec de poussée affichée (dernière ligne de git, sans le jeton, qui
# n'est qu'en en-tête) ; jeton retiré de l'environnement de pip et de pytest ; 30 dernières lignes des essais ; fichier poussé de plus
# de 95 Mo signalé.
#
# Lancée par l'entrée de l'instance après le clone de la seule branche du dépôt réduit (`--depth 1 --single-branch`). Étapes :
#   1. commit du dépôt réduit égal à COMMIT_REDUIT, arbre propre ; sinon arrêt (code 10) ;
#   2. environnement Python (versions épinglées), carte graphique exigée (code 11) ;
#   3. essais rapides : un échec ou un essai sauté = arrêt (code 12) ;
#   4. course (`volet_a_lancer_v3`) en arrière-plan, **sans** le jeton dans son environnement ;
#   5. toutes les PERIODE_POUSSE_S secondes, puis à la fin (et à tout arrêt), les `runs/<run_id>/` et `diag/<run_id>/` déjà écrits
#      et un fichier d'état sont poussés sur la branche BRANCHE_RESULTATS (jamais `main`), par un arbre de travail séparé.
# Seul secret : GH_TOKEN (jeton du programme, passé par son nom à la création), jamais affiché ni écrit sur disque : il ne sert qu'en
# en-tête HTTP passé à chaque commande `git` (`-c http.extraHeader`), l'adresse du dépôt n'en contient pas.
# Variables : COMMIT_REDUIT (exigée), GO_ID (exigée, transmise au lanceur), BRANCHE_RESULTATS, PERIODE_POUSSE_S (1800), RUN_ID,
# CACHE_HF (/workspace/hf). Mode jouet (essai à blanc, sans location) : MODE_JOUET=1, VENV_JOUET (environnement existant),
# COMMANDE_COURSE (remplace la course), ESSAIS (remplace la liste des essais).
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
MODE_JOUET=${MODE_JOUET:-0}
ESSAIS=${ESSAIS:-"tests/test_neuron_lens_volet_a_extraction_v2.py tests/test_neuron_lens_volet_a_chargement_v1.py tests/test_neuron_lens_volet_a_lancer_v3.py tests/test_neuron_lens_volet_a_donnees_v1.py tests/test_neuron_lens_volet_a_donnees_v2.py tests/test_neuron_lens_volet_a_sondes_v2.py tests/test_neuron_lens_volet_a_lectures_v2.py tests/test_neuron_lens_garde_depense_v3.py"}
ETAT="demarrage"

log() { echo "AMORCE $(date -u +%FT%TZ) $*"; }

git_jeton() {  # git avec le jeton en en-tête seulement (jamais dans l'adresse, la configuration ni la sortie)
  local h
  h="Authorization: Basic $(printf 'x-access-token:%s' "${GH_TOKEN:-}" | base64 -w0)"
  git -c http.extraHeader="$h" "$@"
}

pousser() {  # copie des résultats déjà écrits et de l'état, commit et poussée sur BRANCHE_RESULTATS ; rend 1 en échec (argument : nombre d'essais)
  [ -d "$RESULTATS" ] || return 0
  mkdir -p "$RESULTATS/runs" "$RESULTATS/diag"
  [ -d "$DEPOT/runs/$RUN_ID" ] && cp -a "$DEPOT/runs/$RUN_ID" "$RESULTATS/runs/" || true
  [ -d "$DEPOT/diag/$RUN_ID" ] && cp -a "$DEPOT/diag/$RUN_ID" "$RESULTATS/diag/" || true
  printf 'run_id=%s\netat=%s\nheure=%s\ncommit_reduit=%s\n' "$RUN_ID" "$ETAT" "$(date -u +%FT%TZ)" "$COMMIT_REDUIT" \
    > "$RESULTATS/etat-neuron-lens-volet-a.txt"
  git -C "$RESULTATS" add -A
  if ! git -C "$RESULTATS" diff --cached --quiet; then
    git -C "$RESULTATS" -c user.name=neuron-lens -c user.email=neuron-lens@example.invalid commit -q -m "Neuron Lens, volet A : $ETAT"
  fi
  local gros
  gros=$(find "$RESULTATS/runs" "$RESULTATS/diag" -type f -size +95M 2>/dev/null | head -3)
  [ -n "$gros" ] && log "fichier de plus de 95 Mo (refusé par l'hébergeur) : $gros"
  local i n err
  n=${1:-4}
  for i in $(seq 1 "$n"); do
    if err=$(git_jeton -C "$RESULTATS" push -q origin "HEAD:refs/heads/$BRANCHE_RESULTATS" 2>&1); then
      log "pousse : $ETAT"
      return 0
    fi
    log "poussee refusee (essai $i/$n) : $(printf '%s\n' "$err" | tail -1 | cut -c1-200)"
    if [ "$n" -gt 4 ]; then sleep 60; else sleep $((2 ** i)); fi
  done
  log "poussee en echec : $ETAT"
  return 1
}

fin() {
  local code=$?
  [ "$code" -ne 0 ] && ETAT="arret code $code ($ETAT)"
  pousser 10 || true  # poussée finale persistante (10 essais espacés de 60 s), bornée par la minuterie de destruction
  log "fin : $ETAT"
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
  env -u GH_TOKEN .venv/bin/pip install -q --upgrade pip
  env -u GH_TOKEN .venv/bin/pip install -q -r requirements-neuron-lens-volet-a-v1.txt
  PY="$DEPOT/.venv/bin/python"
  if ! "$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)'; then
    ETAT="carte graphique indisponible"; log "$ETAT"; exit 11
  fi
  log "carte : $("$PY" -c 'import torch; print(torch.cuda.get_device_name(0))')"
fi
ETAT="environnement pret"
if ! pousser; then ETAT="premiere poussee impossible"; log "$ETAT"; exit 14; fi  # avant toute dépense de carte graphique

# 3. essais rapides : échec ou essai sauté = arrêt
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
  [ "$MODE_JOUET" = 1 ] || { ETAT="COMMANDE_COURSE hors du mode jouet"; exit 13; }
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
