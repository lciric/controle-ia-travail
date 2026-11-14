#!/usr/bin/env bash
# Amorce de la machine louée pour la course du volet A de « Neuron Lens » — v5 (commande v7, sans ssh ; décision de la mère R-2752).
# v5 : contre-lecture 8 (N-3, N-8, N-12, N-6) — la poussée échoue franchement : copie, écriture de l'état, `git add`, `git commit` en
# échec = échec de la poussée (journalisé), et « pousse » n'est écrit qu'après avoir vérifié que la tête distante égale la tête locale
# (`ls-remote`) ; `find` non masqué (son échec = échec de la poussée) et second contrôle des fichiers indexés de plus de 95 Mo ; un
# fichier déjà poussé qui grossit au-delà de 95 Mo garde à la tête sa version déjà poussée ; nombre de fichiers exclus inscrit dans
# l'état poussé (`exclus=`) ; première poussée (« commit verifie ») AVANT l'installation de l'environnement (code 14 en moins d'une
# minute) ; sans course lancée, poussée finale courte (2 essais) et dernière ligne « fin sans poussee finale (aucune course lancee,
# aucun resultat a sauver) ». v4 : l'alarme « POUSSEE FINALE EN ECHEC » seulement si la course a été lancée. v3 : contre-lecture 7 —
# code 15, exclusion des fichiers de plus de 95 Mo avant `git add`, plus de retour silencieux, `pip` épinglé, code 13 journalisé, garde
# de la carte essayable en mode jouet. v2 : contre-lecture 6 — première poussée fatale, poussée finale persistante, jeton hors de pip et
# de pytest.
#
# Lancée par l'entrée de l'instance après le clone de la seule branche du dépôt réduit (`--depth 1 --single-branch`). Étapes :
#   1. commit du dépôt réduit égal à COMMIT_REDUIT, arbre propre ; sinon arrêt (code 10, journaux du loueur seulement) ; première
#      poussée (« commit verifie ») impossible → arrêt (code 14, avant l'installation de l'environnement) ;
#   2. environnement Python (versions épinglées), carte graphique exigée (code 11) ;
#   3. essais rapides : un échec, un essai sauté ou un arbre sali = arrêt (code 12) ;
#   4. course (`volet_a_lancer_v3`) en arrière-plan, **sans** le jeton dans son environnement ; COMMANDE_COURSE hors du mode jouet =
#      arrêt (code 13) ;
#   5. toutes les PERIODE_POUSSE_S secondes, puis à la fin (et à tout arrêt), les `runs/<run_id>/` et `diag/<run_id>/` déjà écrits
#      et un fichier d'état sont poussés sur la branche BRANCHE_RESULTATS (jamais `main`), par un arbre de travail séparé ;
#   6. poussée finale en échec alors que la course a réussi : code 15 (sinon le code d'origine est gardé).
# Dernières lignes possibles du journal (règle de destruction de la commande v7) : « fin : <état> » (poussée finale vérifiée) ;
# « fin sans arbre des resultats : … » (code 10) ; « fin sans poussee finale (aucune course lancee, aucun resultat a sauver) » ;
# « POUSSEE FINALE EN ECHEC : … » (course lancée, résultats non poussés).
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
COURSE_LANCEE=0
EXCLUS=0
LIMITE=$((95 * 1024 * 1024))

log() { echo "AMORCE $(date -u +%FT%TZ) $*"; }

git_jeton() {  # git avec le jeton en en-tête seulement (jamais dans l'adresse, la configuration ni la sortie)
  local h
  h="Authorization: Basic $(printf 'x-access-token:%s' "${GH_TOKEN:-}" | base64 -w0)"
  git -c http.extraHeader="$h" "$@"
}

exclure_gros() {  # fichiers de plus de 95 Mo retirés de l'arbre des résultats AVANT `git add` ; rend 1 si `find` échoue
  local f rel liste
  EXCLUS=0  # recompté à chaque poussée (la copie remet chaque fois tous les fichiers) : nombre de fichiers distincts exclus
  liste=$(mktemp)
  if ! find "$RESULTATS/runs" "$RESULTATS/diag" -type f -size +"$((LIMITE / 1024))"k -print0 > "$liste"; then
    rm -f "$liste"; log "recherche des fichiers de plus de 95 Mo impossible"; return 1
  fi
  while IFS= read -r -d '' f; do
    rel=${f#"$RESULTATS"/}
    rm -f -- "$f"
    EXCLUS=$((EXCLUS + 1))
    if git -C "$RESULTATS" cat-file -e "HEAD:$rel" 2>/dev/null; then
      git -C "$RESULTATS" checkout -q HEAD -- "$rel" || { rm -f "$liste"; log "version deja poussee non restauree : $rel"; return 1; }
      log "fichier de plus de 95 Mo exclu de la poussee (reste sur le disque de l'instance ; version deja poussee gardee) : $rel"
    else
      log "fichier de plus de 95 Mo exclu de la poussee (reste sur le disque de l'instance) : $rel"
    fi
  done < "$liste"
  rm -f "$liste"
}

preparer() {  # copie, exclusion, état, index et commit ; rend 1 au premier échec
  mkdir -p "$RESULTATS/runs" "$RESULTATS/diag" || return 1
  if [ -d "$DEPOT/runs/$RUN_ID" ]; then cp -a "$DEPOT/runs/$RUN_ID" "$RESULTATS/runs/" || { log "copie de runs impossible"; return 1; }; fi
  if [ -d "$DEPOT/diag/$RUN_ID" ]; then cp -a "$DEPOT/diag/$RUN_ID" "$RESULTATS/diag/" || { log "copie de diag impossible"; return 1; }; fi
  exclure_gros || return 1
  printf 'run_id=%s\netat=%s\nheure=%s\ncommit_reduit=%s\nexclus=%s\n' "$RUN_ID" "$ETAT" "$(date -u +%FT%TZ)" "$COMMIT_REDUIT" \
    "$EXCLUS" > "$RESULTATS/etat-neuron-lens-volet-a.txt" || { log "ecriture de l'etat impossible"; return 1; }
  git -C "$RESULTATS" add -A || { log "git add impossible"; return 1; }
  local f
  while IFS= read -r -d '' f; do  # second contrôle : aucun fichier indexé de plus de 95 Mo
    if [ -f "$RESULTATS/$f" ] && [ "$(stat -c %s "$RESULTATS/$f")" -gt "$LIMITE" ]; then
      log "fichier indexe de plus de 95 Mo : $f ; commit refuse"; git -C "$RESULTATS" reset -q; return 1
    fi
  done < <(git -C "$RESULTATS" diff --cached --name-only -z --diff-filter=AM)
  if ! git -C "$RESULTATS" diff --cached --quiet; then
    git -C "$RESULTATS" -c user.name=neuron-lens -c user.email=neuron-lens@example.invalid commit -q -m "Neuron Lens, volet A : $ETAT" \
      || { log "git commit impossible"; return 1; }
  fi
}

pousser() {  # arguments : nombre d'essais, attente fixe (0 = 2^i) ; rend 0 seulement si la tête distante égale la tête locale
  if [ ! -d "$RESULTATS" ]; then log "pas d'arbre des resultats : rien pousse ($ETAT)"; return 1; fi
  preparer || { log "poussee en echec (preparation) : $ETAT"; return 1; }
  local i n attente err locale distante
  n=${1:-4}; attente=${2:-0}
  locale=$(git -C "$RESULTATS" rev-parse HEAD)
  for i in $(seq 1 "$n"); do
    if err=$(git_jeton -C "$RESULTATS" push -q origin "HEAD:refs/heads/$BRANCHE_RESULTATS" 2>&1); then
      distante=$(git_jeton -C "$RESULTATS" ls-remote origin "refs/heads/$BRANCHE_RESULTATS" 2>/dev/null | cut -f1) || distante=""
      if [ "$distante" = "$locale" ]; then
        log "pousse : $ETAT"
        return 0
      fi
      err="tete distante ${distante:-absente} differente de la tete locale $locale"
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
  if [ "$COURSE_LANCEE" != 1 ]; then
    if pousser 2 5; then log "fin : $ETAT"; exit "$code"; fi
    log "fin sans poussee finale (aucune course lancee, aucun resultat a sauver) : $ETAT"
    exit "$code"
  fi
  if pousser "$N_FINALE" "$ATTENTE_FINALE"; then
    log "fin : $ETAT"
    exit "$code"
  fi
  log "etat non pousse : $ETAT"
  log "POUSSEE FINALE EN ECHEC : resultats seulement sur le disque de l'instance, ne pas la detruire sans la mere"
  if [ "$code" -eq 0 ]; then exit 15; fi
  exit "$code"
}
trap fin EXIT

# 1. commit, arbre, première poussée (le jeton est éprouvé avant toute installation)
cd "$DEPOT"
TETE=$(git rev-parse HEAD)
if [ "$TETE" != "$COMMIT_REDUIT" ]; then ETAT="commit inattendu $TETE"; log "$ETAT"; exit 10; fi
if [ -n "$(git status --porcelain)" ]; then ETAT="arbre non propre"; log "$ETAT"; exit 10; fi
git worktree add -q -b "$BRANCHE_RESULTATS" "$RESULTATS" HEAD
log "commit reduit verifie : $TETE ; run_id=$RUN_ID"
ETAT="commit verifie"
if ! pousser; then ETAT="premiere poussee impossible"; log "$ETAT"; exit 14; fi

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
ETAT="environnement pret"; pousser || true

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
COURSE_LANCEE=1
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
