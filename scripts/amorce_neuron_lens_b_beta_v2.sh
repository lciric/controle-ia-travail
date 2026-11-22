#!/usr/bin/env bash
# Amorce de la machine louée pour la course de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, B-β) — v2.
# v2 = v1 (`amorce_neuron_lens_b_beta_v1.sh`, `2049194a…`, archivée, jamais jouée) avec le lanceur v2 et ses essais (dont les essais des
# étapes câblées et des gardes du montage), et la version de python lue AVANT pip (3.12.16, addendum partie 1, § 5 : autre = code 19 ;
# contre-lecture du code de course v1, m-15).
# Reprise de l'amorce v7 de la tranche des lentilles publiques (`amorce_neuron_lens_b_alpha_v7.sh`, contre-lue), changée seulement en :
#   - lanceur `controle_ia.neuron_lens.b_beta_lancer_v2` et ses essais ; noms des fichiers d'état « b-beta » ; RUN_ID
#     `AAAAMMJJ-HHMMSS-neuron-lens-b-beta` ; branche des résultats `calcul/neuron-lens-b-beta-v1` ;
#   - Drowse 6.1.4 (texte gelé de la tranche, P.2) : la roue est téléchargée seule (`pip download --no-deps`), son empreinte SHA-256
#     comparée à 673ed2b4… AVANT toute installation (autre empreinte ou autre nom = code 18, rien ne part), puis installée depuis ce fichier
#     **sans ses dépendances** (`--no-deps` : sa métadonnée demande transformers>=5.22, l'addendum partie 1 fixe 5.18.0 ; déclaration de
#     forme de la commande) ; le chemin de la roue est passé au lanceur (`DROWSE_ROUE`), qui revérifie version et empreinte à B0 ;
#   - le lanceur clone lui-même le code voisin au commit épinglé à l'étape « preparer » (en ligne) : l'arbre voisin doit être un dépôt
#     git à 849bfe16 (l'essai du correctif (4) lit `git show HEAD:`) ; COMMIT_SOURCE (commit de notre branche) consigné en partie 2.
# Le reste est inchangé : entrée idempotente, pip verbeux et minuté, carte lue avant pip, clé aux seules étapes « jeton », balayage avant
# chaque commit, poussées vérifiées par `ls-remote`, exclusion des fichiers de plus de 95 Mo.
# Codes : ceux de la v7 (10 à 17, 20 à 22), plus 18 : roue de Drowse absente, d'un autre nom ou d'une autre empreinte ; 19 (v2) : python
# autre que 3.12.16 avant pip.
# Variables : celles de la v7 (COMMIT_REDUIT, GO_ID, RUN_ID exigées ; BRANCHE_RESULTATS, PERIODE_POUSSE_S, HF_HOME, TIMEOUT_PIP_S,
# ESSAIS_POUSSEE_FINALE, ATTENTE_POUSSEE_FINALE_S, INSTANCE_ID, CARTE_ATTENDUE, mode jouet), plus COMMIT_SOURCE.
set -euo pipefail
set +x
umask 022

DEPOT=$(cd "$(dirname "$0")/.." && pwd)
RESULTATS="$DEPOT/../resultats-neuron-lens-b-beta"
FIN_FICHIER="$DEPOT/../fin-b-beta.txt"
EN_COURS="$DEPOT/../etape-en-cours-b-beta.txt"
PRET="$DEPOT/../environnement-pret-b-beta.txt"
ESSAIS_OK="$DEPOT/../essais-passes-b-beta.txt"
JPIP="$DEPOT/../pip-b-beta.log"
ROUES="$DEPOT/../roues-b-beta"
ROUE_DROWSE="$ROUES/drowse_ai-6.1.4-py3-none-any.whl"
SHA_DROWSE=673ed2b4de653ad2ec22660b0191031ee2c7b4bacaf4cc2ea552f0436b9d8e03
: "${COMMIT_REDUIT:?COMMIT_REDUIT exigé}"
: "${GO_ID:?GO_ID exigé}"
: "${RUN_ID:?RUN_ID exigé}"
BRANCHE_RESULTATS=${BRANCHE_RESULTATS:-calcul/neuron-lens-b-beta-v1}
PERIODE=${PERIODE_POUSSE_S:-600}
export HF_HOME=${HF_HOME:-/workspace/hf}
TIMEOUT_PIP=${TIMEOUT_PIP_S:-3600}
N_FINALE=${ESSAIS_POUSSEE_FINALE:-10}
ATTENTE_FINALE=${ATTENTE_POUSSEE_FINALE_S:-60}
MODE_JOUET=${MODE_JOUET:-0}
ESSAIS=${ESSAIS:-"tests/test_neuron_lens_verdicts_b_beta_v4.py tests/test_neuron_lens_controles_b_beta_v2.py tests/test_neuron_lens_b_beta_lancer_v2.py tests/test_neuron_lens_etapes_b_beta_v2.py tests/test_neuron_lens_montage_b_beta_v2.py tests/test_neuron_lens_grandeurs_b_alpha_v1.py tests/test_neuron_lens_verdicts_b_alpha_v3.py tests/test_neuron_lens_balayage_arbre_v1.py"}
ETAT="demarrage"
COURSE_LANCEE=0
EXCLUS=0
EXCLUS_FICHIERS=""
LIMITE=$((95 * 1024 * 1024))
T0=$(date +%s)

log() { echo "AMORCE $(date -u +%FT%TZ) $*"; }

[[ "$RUN_ID" =~ ^[0-9]{8}-[0-9]{6}-neuron-lens-b-beta$ ]] || { log "RUN_ID invalide : $RUN_ID"; exit 17; }
[[ "$GO_ID" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || { log "GO_ID invalide"; exit 17; }
if [ -n "${COMMANDE_LANCEUR:-}" ] && [ "$MODE_JOUET" != 1 ]; then log "COMMANDE_LANCEUR hors du mode jouet"; exit 13; fi

# entrée idempotente : état final déjà atteint → attente sans calcul (une relance par le loueur ne refait rien)
if [ -s "$FIN_FICHIER" ]; then
  log "etat final deja atteint : $(head -c 300 "$FIN_FICHIER") ; attente sans calcul"
  if [ "${ATTENTE_FIN:-1}" = 1 ]; then exec sleep infinity; fi
  exit 0
fi

git_jeton() {  # git avec le jeton en en-tête seulement (jamais dans l'adresse, la configuration ni la sortie)
  local h
  h="Authorization: Basic $(printf 'x-access-token:%s' "${GH_TOKEN:-}" | base64 -w0)"
  git -c http.extraHeader="$h" "$@"
}

lanceur() {  # le lanceur, sans aucun secret ; l'environnement réseau et la clé sont posés par l'appelant
  if [ -n "${COMMANDE_LANCEUR:-}" ]; then
    bash -c "$COMMANDE_LANCEUR" lanceur "$@"
  else
    PYTHONPATH="$DEPOT/src" "$PY" -m controle_ia.neuron_lens.b_beta_lancer_v2 "$@" --racine "$DEPOT" --run-id "$RUN_ID"
  fi
}

exclure_gros() {  # fichiers de plus de 95 Mo retirés de l'arbre des résultats AVANT `git add` ; rend 1 si `find` échoue
  local f rel liste
  EXCLUS=0
  EXCLUS_FICHIERS=""
  liste=$(mktemp) || { log "fichier temporaire impossible"; return 1; }
  if ! find "$RESULTATS/runs" "$RESULTATS/diag" -type f -size +"$((LIMITE / 1024))"k -print0 > "$liste"; then
    rm -f "$liste"; log "recherche des fichiers de plus de 95 Mo impossible"; return 1
  fi
  while IFS= read -r -d '' f; do
    rel=${f#"$RESULTATS"/}
    rm -f -- "$f"
    EXCLUS=$((EXCLUS + 1))
    EXCLUS_FICHIERS="${EXCLUS_FICHIERS:+$EXCLUS_FICHIERS }$rel"
    if git -C "$RESULTATS" cat-file -e "HEAD:$rel" 2>/dev/null; then
      git -C "$RESULTATS" checkout -q HEAD -- "$rel" || { rm -f "$liste"; log "version deja poussee non restauree : $rel"; return 1; }
    fi
    log "fichier de plus de 95 Mo exclu de la poussee (reste sur le disque de l'instance) : $rel"
  done < "$liste"
  rm -f "$liste"
}

ecrire_etat() {
  local faites en_cours
  faites=$(cd "$DEPOT/diag/$RUN_ID" 2>/dev/null && ls b-beta-*.json 2>/dev/null | sed 's/^b-beta-//; s/\.json$//' | tr '\n' ' ') || faites=""
  en_cours=$(cat "$EN_COURS" 2>/dev/null || true)
  {
    printf 'run_id=%s\netat=%s\nheure=%s\ncommit_reduit=%s\nexclus=%s\nexclus_fichiers=%s\n' "$RUN_ID" "$ETAT" "$(date -u +%FT%TZ)" \
      "$COMMIT_REDUIT" "$EXCLUS" "$EXCLUS_FICHIERS"
    printf 'location_s=%s\netape_en_cours=%s\netapes_faites=%s\n' "$(( $(date +%s) - T0 ))" "$en_cours" "$faites"
    printf 'pip_fin=%s\n' "$(tail -n 3 "$JPIP" 2>/dev/null | tr '\n' ' ' | cut -c1-300)"
  } > "$RESULTATS/etat-neuron-lens-b-beta.txt"
}

preparer() {  # copie, exclusion, état, balayage, index et commit ; rend 1 au premier échec
  mkdir -p "$RESULTATS/runs" "$RESULTATS/diag" || return 1
  if [ -d "$DEPOT/runs/$RUN_ID" ]; then cp -a "$DEPOT/runs/$RUN_ID" "$RESULTATS/runs/" || { log "copie de runs impossible"; return 1; }; fi
  if [ -d "$DEPOT/diag/$RUN_ID" ]; then cp -a "$DEPOT/diag/$RUN_ID" "$RESULTATS/diag/" || { log "copie de diag impossible"; return 1; }; fi
  exclure_gros || return 1
  ecrire_etat || { log "ecriture de l'etat impossible"; return 1; }
  local sortie
  if ! sortie=$(env -u HUGGING_FACE_HUB_TOKEN PYTHONPATH="$DEPOT/src" "$PY" -m controle_ia.neuron_lens.balayage_arbre_v1 \
      "$RESULTATS/runs" "$RESULTATS/diag" "$RESULTATS/etat-neuron-lens-b-beta.txt" 2>&1); then
    log "balayage : poussee refusee : $(printf '%s' "$sortie" | tail -3 | tr '\n' ' ' | cut -c1-300)"
    return 1
  fi
  git -C "$RESULTATS" add -A || { log "git add impossible"; return 1; }
  local f t indexes
  indexes=$(mktemp) || { log "fichier temporaire impossible"; return 1; }
  git -C "$RESULTATS" diff --cached --name-only -z --diff-filter=AM > "$indexes" || { rm -f "$indexes"; log "liste des fichiers indexes impossible"; return 1; }
  while IFS= read -r -d '' f; do
    t=$(stat -c %s "$RESULTATS/$f") || { rm -f "$indexes"; log "taille illisible : $f"; return 1; }
    if [ "$t" -gt "$LIMITE" ]; then
      rm -f "$indexes"; log "fichier indexe de plus de 95 Mo : $f ; commit refuse"; git -C "$RESULTATS" reset -q; return 1
    fi
  done < "$indexes"
  rm -f "$indexes"
  if ! git -C "$RESULTATS" diff --cached --quiet; then
    git -C "$RESULTATS" -c user.name=neuron-lens -c user.email=neuron-lens@example.invalid commit -q -m "Neuron Lens, ajustement de nos lentilles : $ETAT" \
      || { log "git commit impossible"; return 1; }
  fi
}

pousser() {  # arguments : nombre d'essais, attente fixe (0 = 2^i) ; rend 0 seulement si la tête distante égale la tête locale
  if [ ! -d "$RESULTATS" ]; then log "pas d'arbre des resultats : rien pousse ($ETAT)"; return 1; fi
  preparer || { log "poussee en echec (preparation) : $ETAT"; return 1; }
  local i n attente err locale distante
  n=${1:-4}; attente=${2:-0}
  locale=$(git -C "$RESULTATS" rev-parse HEAD) && [ -n "$locale" ] || { log "tete locale illisible"; return 1; }
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
    printf '%s\n' "$ETAT" > "$FIN_FICHIER"
    log "fin : $ETAT"
    exit "$code"
  fi
  log "etat non pousse : $ETAT"
  log "POUSSEE FINALE EN ECHEC : resultats seulement sur le disque de l'instance, ne pas la detruire sans la mere"
  if [ "$code" -eq 0 ]; then exit 15; fi
  exit "$code"
}
trap fin EXIT

# 1. commit, arbre, arbre des résultats, première poussée
cd "$DEPOT"
TETE=$(git rev-parse HEAD)
if [ "$TETE" != "$COMMIT_REDUIT" ]; then ETAT="commit inattendu $TETE"; log "$ETAT"; exit 10; fi
if [ -d "$DEPOT/runs/$RUN_ID" ]; then
  REPRISE=1; log "reprise : course $RUN_ID deja commencee"
else
  REPRISE=0
  if [ -n "$(git status --porcelain)" ]; then ETAT="arbre non propre"; log "$ETAT"; exit 10; fi
fi
if [ -d "$RESULTATS" ]; then
  [ "$(git -C "$RESULTATS" rev-parse --abbrev-ref HEAD 2>/dev/null)" = "$BRANCHE_RESULTATS" ] || { ETAT="arbre des resultats inattendu"; log "$ETAT"; exit 10; }
else
  git worktree add -q -b "$BRANCHE_RESULTATS" "$RESULTATS" HEAD
fi
log "commit reduit verifie : $TETE ; run_id=$RUN_ID ; reprise=$REPRISE"
if [ "$MODE_JOUET" = 1 ]; then
  PY="${VENV_JOUET:?VENV_JOUET exigé en mode jouet}/bin/python"
else
  PY="$DEPOT/.venv/bin/python"
fi
if [ ! -x "$PY" ]; then PY=$(command -v python3); fi  # balayage de la première poussée, avant l'environnement
ETAT="commit verifie"
if ! pousser; then ETAT="premiere poussee impossible"; log "$ETAT"; exit 14; fi

# 2. carte lue avant l'environnement (v7), puis environnement (pip verbeux et minuté) et carte vue par torch
carte_ok() {  # nom lu ; rend 0 si CARTE_ATTENDUE est vide ou contenue dans le nom
  [ -z "${CARTE_ATTENDUE:-}" ] || [[ "$1" == *"$CARTE_ATTENDUE"* ]]
}
if [ "$MODE_JOUET" != 1 ] || [ "${EXIGER_CARTE_JOUET:-0}" = 1 ]; then
  SMI=${OUTIL_NVIDIA_SMI:-nvidia-smi}
  if command -v "$SMI" > /dev/null 2>&1; then
    CARTE_SMI=$("$SMI" --query-gpu=name --format=csv,noheader 2>/dev/null | head -1) || CARTE_SMI=""
    log "carte (nvidia-smi) : ${CARTE_SMI:-illisible}"
    if [ -z "$CARTE_SMI" ]; then ETAT="nom de la carte illisible (nvidia-smi)"; log "$ETAT"; exit 11; fi
    if ! carte_ok "$CARTE_SMI"; then ETAT="carte inattendue : $CARTE_SMI (attendue : $CARTE_ATTENDUE)"; log "$ETAT"; exit 11; fi
  else
    log "nvidia-smi absent : carte controlee par torch apres l'installation"
  fi
fi
if [ "$MODE_JOUET" != 1 ] && [ ! -s "$PRET" ]; then
  VPY=$(python3 -c 'import platform; print(platform.python_version())' 2>/dev/null) || VPY=""
  if [ "$VPY" != "${PYTHON_ATTENDU:-3.12.16}" ]; then
    ETAT="python ${VPY:-illisible} au lieu de ${PYTHON_ATTENDU:-3.12.16} (addendum partie 1, § 5)"; log "$ETAT"; exit 19
  fi
  ETAT="installation de l'environnement"; pousser || true
  t=$(date +%s)
  if ! { python3 -m venv .venv \
         && env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN timeout "$TIMEOUT_PIP" .venv/bin/pip install -v pip==26.2.2 \
         && env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN timeout "$TIMEOUT_PIP" .venv/bin/pip install -v \
              -r requirements-neuron-lens-b-beta-v2.txt \
         && mkdir -p "$ROUES" \
         && env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN timeout "$TIMEOUT_PIP" .venv/bin/pip download -v --no-deps \
              --only-binary=:all: -d "$ROUES" drowse.ai==6.1.4; } > "$JPIP" 2>&1; then
    ETAT="environnement non installe (pip en echec ou delai de $TIMEOUT_PIP s)"; log "$ETAT"; tail -5 "$JPIP"; exit 16
  fi
  # roue de Drowse : seule, au nom attendu, à l'empreinte du texte gelé, AVANT son installation (sans dépendances)
  if [ "$(ls "$ROUES" | wc -l)" != 1 ] || [ ! -f "$ROUE_DROWSE" ] \
     || [ "$(sha256sum "$ROUE_DROWSE" | cut -d' ' -f1)" != "$SHA_DROWSE" ]; then
    ETAT="roue de Drowse absente, d'un autre nom ou d'une autre empreinte"; log "$ETAT"; exit 18
  fi
  if ! env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN timeout "$TIMEOUT_PIP" .venv/bin/pip install -v --no-deps \
       "$ROUE_DROWSE" >> "$JPIP" 2>&1; then
    ETAT="Drowse non installe"; log "$ETAT"; tail -5 "$JPIP"; exit 16
  fi
  date -u +%FT%TZ > "$PRET"
  log "environnement installe en $(( $(date +%s) - t )) s"
fi
[ "$MODE_JOUET" = 1 ] || PY="$DEPOT/.venv/bin/python"
if [ "$MODE_JOUET" != 1 ] || [ "${EXIGER_CARTE_JOUET:-0}" = 1 ]; then
  if ! env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN "$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)'; then
    ETAT="carte graphique indisponible"; log "$ETAT"; exit 11
  fi
  CARTE=$(env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN "$PY" -c 'import torch; print(torch.cuda.get_device_name(0))') \
    || { ETAT="nom de la carte illisible"; log "$ETAT"; exit 11; }
  log "carte : $CARTE"
  if ! carte_ok "$CARTE"; then
    ETAT="carte inattendue : $CARTE (attendue : $CARTE_ATTENDUE)"; log "$ETAT"; exit 11
  fi
fi
ETAT="environnement pret"; pousser || true

# 3. essais rapides de nos modules (sans la copie de lecture du dépôt voisin) : échec, essai sauté ou arbre sali = arrêt
if [ ! -s "$ESSAIS_OK" ]; then
  ETAT="essais"
  set +e
  # shellcheck disable=SC2086
  SORTIE=$(env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN PYTHONPATH=src "$PY" -m pytest -q -rs -p no:cacheprovider $ESSAIS \
           -k "not copie_reelle" 2>&1)
  CODE=$?
  set -e
  printf '%s\n' "$SORTIE" | tail -30
  if [ "$CODE" -ne 0 ] || printf '%s\n' "$SORTIE" | grep -qiE '[0-9]+ skipped'; then
    ETAT="essais en echec ou sautes"; log "$ETAT"; exit 12
  fi
  if [ "$REPRISE" = 0 ] && [ -n "$(git status --porcelain)" ]; then ETAT="arbre sali par les essais"; log "$ETAT"; exit 12; fi
  date -u +%FT%TZ > "$ESSAIS_OK"
  ETAT="essais passes"; pousser || true
fi

# 4. course : étapes du lanceur, une par appel ; la clé seulement aux étapes « jeton »
appel() {  # <jeton|sans-jeton> <en-ligne|hors-ligne> <arguments du lanceur…> : sous-shell sans secret superflu
  local cle=$1 reseau=$2
  shift 2
  (
    unset GH_TOKEN HUGGING_FACE_HUB_TOKEN HF_HUB_OFFLINE
    [ "$cle" = jeton ] || unset HF_TOKEN
    [ "$reseau" = hors-ligne ] && export HF_HUB_OFFLINE=1
    export GO_ID COMMIT_REDUIT COMMIT_SOURCE="${COMMIT_SOURCE:-}" HF_HOME NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct INSTANCE_ID="${INSTANCE_ID:-}" DROWSE_ROUE="$ROUE_DROWSE"
    lanceur "$@"
  )
}
courir() {
  local ligne etape cle reseau code
  if [ -e "$DEPOT/diag/$RUN_ID/b-beta-telecharger-poids.json" ]; then unset HF_TOKEN HUGGING_FACE_HUB_TOKEN; fi
  while :; do
    ligne=$(appel sans-jeton hors-ligne suite) || { log "suite illisible"; return 20; }
    [ "$ligne" = fin ] && { : > "$EN_COURS"; return 0; }
    read -r etape cle reseau <<< "$ligne"
    case "$cle $reseau" in "jeton en-ligne"|"sans-jeton en-ligne"|"sans-jeton hors-ligne") ;; *) log "suite inattendue : $ligne"; return 20 ;; esac
    printf '%s depuis %s\n' "$etape" "$(date -u +%FT%TZ)" > "$EN_COURS"
    log "etape : $etape ($cle, $reseau)"
    if [ "$cle" = jeton ] && [ -z "${HF_TOKEN:-}" ]; then log "HF_TOKEN absent pour $etape"; return 21; fi
    set +e
    appel "$cle" "$reseau" jouer --etape "$etape"
    code=$?
    set -e
    if [ "$code" -ne 0 ]; then log "etape $etape en echec (code $code du lanceur)"; return 20; fi
    if [ "$etape" = telecharger-poids ]; then
      unset HF_TOKEN HUGGING_FACE_HUB_TOKEN
      if [ -z "${HF_TOKEN+x}" ] && [ -z "${HUGGING_FACE_HUB_TOKEN+x}" ]; then log "HF_TOKEN retire de la course (verifie par son nom)"; else return 22; fi
    fi
  done
}
ETAT="course en cours"
courir &
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
