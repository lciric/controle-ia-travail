#!/usr/bin/env bash
# Amorce de la machine louée pour la course de la tranche B-α de « Neuron Lens » — v6 (v5 avec le lanceur v4 et ses essais v4 :
# seconde série de l'ablation au lot 64 sur la même carte, GO-2026-11-17-04 ; et CARTE_ATTENDUE : si posée, le nom de la carte lu par
# `torch` doit la contenir, sinon code 11 avant toute course). v5 (v4 avec le lanceur v3 et ses essais v3 :
# `measure --ctx-batch 16`, R-2901). v4 : v3 avec le lanceur v2 et ses essais v2 : copie du
# script d'origine pour l'essai du correctif (1), course du 2026-11-15, instance 60770175). v3 : v2 + appels du lanceur par un sous-shell qui
# retire les secrets et pose l'environnement de l'étape : la v2 passait par `env … lanceur`, qui ne peut pas appeler une fonction du
# shell — « env: 'lanceur': No such file or directory », essai à blanc B-α v1 du 2026-11-15, cas nominal). v2 : v1 + refus de COMMANDE_LANCEUR hors du mode
# jouet AVANT toute installation, code 13, pour qu'il soit essayable à blanc). v1 : pièce 5 du § 6 du devis B-α v2 ; reprend
# l'amorce v6 du volet A : poussées vérifiées par `ls-remote`, exclusion des fichiers de plus de 95 Mo, état poussé, codes 10 à 15).
# Nouveau pour B-α (devis v2, § 4, point 4, et § 5) :
#   - ENTRÉE IDEMPOTENTE : une relance du conteneur par le loueur relit l'état. État final déjà atteint (`fin-b-alpha.txt` à côté du
#     dépôt) → attente sans calcul ; course déjà commencée (`runs/<RUN_ID>/` présent) → REPRISE (arbre des résultats réutilisé,
#     environnement et essais déjà faits non refaits, le lanceur saute les étapes faites et rejoue l'étape interrompue) ;
#   - `pip` VERBEUX (journal à côté du dépôt, fin dans l'état poussé) sous `timeout` (TIMEOUT_PIP_S, 3600 s) : échec ou délai = code 16 ;
#   - course = étapes du lanceur `controle_ia.neuron_lens.b_alpha_lancer_v4`, une par appel, dans l'ordre que donne `suite` ;
#   - `HF_TOKEN` (par son nom seulement ; jamais affiché ni écrit) : transmis aux SEULES étapes `jeton` (téléchargements de Llama) ;
#     toute autre étape tourne sous `env -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN` ; dès `telecharger-poids` faite, le processus de la
#     course le retire de son environnement (`unset`, vérifié par le nom). Le shell principal le garde, pour le seul balayage ci-dessous
#     (exposition résiduelle déclarée au devis v2, § 5 : environnement du processus d'entrée, configuration du loueur, relances) ;
#   - BALAYAGE avant chaque commit de l'arbre des résultats (`balayage_arbre_v1` : sept formes de GH_TOKEN et HF_TOKEN) : forme
#     trouvée = rien n'est poussé (poussée en échec, journalisée par le chemin seul) ;
#   - état poussé : étape en cours, étapes faites, durée de la location, fin du journal de pip.
# Codes : 10 commit ou arbre inattendu ; 11 carte graphique absente ; 12 essais en échec, sautés ou arbre sali ; 13 COMMANDE_LANCEUR
# hors du mode jouet ; 14 première poussée impossible ; 15 poussée finale en échec alors que la course a réussi ; 16 environnement non
# installé (pip en échec ou délai) ; 17 RUN_ID ou GO_ID invalide ; 20 étape du lanceur en échec (`arret-*.json`) ou `suite` illisible ;
# 21 HF_TOKEN absent à une étape « jeton » ; 22 HF_TOKEN non retiré après `telecharger-poids`.
# Dernières lignes possibles du journal (règle de destruction de la commande) : « fin : <état> » ; « fin sans arbre des resultats : … » ;
# « fin sans poussee finale (aucune course lancee, aucun resultat a sauver) » ; « POUSSEE FINALE EN ECHEC : … » ; et, après une
# relance, « etat final deja atteint : … ; attente sans calcul ».
# Variables : COMMIT_REDUIT, GO_ID, RUN_ID (exigées ; RUN_ID fixé par la commande, le même à chaque relance), BRANCHE_RESULTATS
# (calcul/neuron-lens-b-alpha-v1), PERIODE_POUSSE_S (600), HF_HOME (/workspace/hf), TIMEOUT_PIP_S (3600), ESSAIS_POUSSEE_FINALE (10),
# ATTENTE_POUSSEE_FINALE_S (60), INSTANCE_ID (consigné dans la partie 2), CARTE_ATTENDUE (v6 ; par exemple « A100-SXM4-40GB »). Mode jouet (essai à blanc, sans location) : MODE_JOUET=1,
# VENV_JOUET, COMMANDE_LANCEUR (remplace l'appel du lanceur ; reçoit les mêmes arguments), ESSAIS, EXIGER_CARTE_JOUET=1, ATTENTE_FIN=0
# (n'attend pas après l'état final).
set -euo pipefail
set +x
umask 022

DEPOT=$(cd "$(dirname "$0")/.." && pwd)
RESULTATS="$DEPOT/../resultats-neuron-lens-b-alpha"
FIN_FICHIER="$DEPOT/../fin-b-alpha.txt"
EN_COURS="$DEPOT/../etape-en-cours-b-alpha.txt"
PRET="$DEPOT/../environnement-pret-b-alpha.txt"
ESSAIS_OK="$DEPOT/../essais-passes-b-alpha.txt"
JPIP="$DEPOT/../pip-b-alpha.log"
: "${COMMIT_REDUIT:?COMMIT_REDUIT exigé}"
: "${GO_ID:?GO_ID exigé}"
: "${RUN_ID:?RUN_ID exigé}"
BRANCHE_RESULTATS=${BRANCHE_RESULTATS:-calcul/neuron-lens-b-alpha-v1}
PERIODE=${PERIODE_POUSSE_S:-600}
export HF_HOME=${HF_HOME:-/workspace/hf}
TIMEOUT_PIP=${TIMEOUT_PIP_S:-3600}
N_FINALE=${ESSAIS_POUSSEE_FINALE:-10}
ATTENTE_FINALE=${ATTENTE_POUSSEE_FINALE_S:-60}
MODE_JOUET=${MODE_JOUET:-0}
ESSAIS=${ESSAIS:-"tests/test_neuron_lens_verdicts_b_alpha_v3.py tests/test_neuron_lens_grandeurs_b_alpha_v1.py tests/test_neuron_lens_addendum_partie2_b_alpha_v1.py tests/test_neuron_lens_b_alpha_lancer_v4.py tests/test_neuron_lens_balayage_arbre_v1.py"}
ETAT="demarrage"
COURSE_LANCEE=0
EXCLUS=0
EXCLUS_FICHIERS=""
LIMITE=$((95 * 1024 * 1024))
T0=$(date +%s)

log() { echo "AMORCE $(date -u +%FT%TZ) $*"; }

[[ "$RUN_ID" =~ ^[0-9]{8}-[0-9]{6}-neuron-lens-b-alpha$ ]] || { log "RUN_ID invalide : $RUN_ID"; exit 17; }
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
    PYTHONPATH="$DEPOT/src" "$PY" -m controle_ia.neuron_lens.b_alpha_lancer_v4 "$@" --racine "$DEPOT" --run-id "$RUN_ID"
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
  faites=$(cd "$DEPOT/diag/$RUN_ID" 2>/dev/null && ls b-alpha-*.json 2>/dev/null | sed 's/^b-alpha-//; s/\.json$//' | tr '\n' ' ') || faites=""
  en_cours=$(cat "$EN_COURS" 2>/dev/null || true)
  {
    printf 'run_id=%s\netat=%s\nheure=%s\ncommit_reduit=%s\nexclus=%s\nexclus_fichiers=%s\n' "$RUN_ID" "$ETAT" "$(date -u +%FT%TZ)" \
      "$COMMIT_REDUIT" "$EXCLUS" "$EXCLUS_FICHIERS"
    printf 'location_s=%s\netape_en_cours=%s\netapes_faites=%s\n' "$(( $(date +%s) - T0 ))" "$en_cours" "$faites"
    printf 'pip_fin=%s\n' "$(tail -n 3 "$JPIP" 2>/dev/null | tr '\n' ' ' | cut -c1-300)"
  } > "$RESULTATS/etat-neuron-lens-b-alpha.txt"
}

preparer() {  # copie, exclusion, état, balayage, index et commit ; rend 1 au premier échec
  mkdir -p "$RESULTATS/runs" "$RESULTATS/diag" || return 1
  if [ -d "$DEPOT/runs/$RUN_ID" ]; then cp -a "$DEPOT/runs/$RUN_ID" "$RESULTATS/runs/" || { log "copie de runs impossible"; return 1; }; fi
  if [ -d "$DEPOT/diag/$RUN_ID" ]; then cp -a "$DEPOT/diag/$RUN_ID" "$RESULTATS/diag/" || { log "copie de diag impossible"; return 1; }; fi
  exclure_gros || return 1
  ecrire_etat || { log "ecriture de l'etat impossible"; return 1; }
  local sortie
  if ! sortie=$(env -u HUGGING_FACE_HUB_TOKEN PYTHONPATH="$DEPOT/src" "$PY" -m controle_ia.neuron_lens.balayage_arbre_v1 \
      "$RESULTATS/runs" "$RESULTATS/diag" "$RESULTATS/etat-neuron-lens-b-alpha.txt" 2>&1); then
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
    git -C "$RESULTATS" -c user.name=neuron-lens -c user.email=neuron-lens@example.invalid commit -q -m "Neuron Lens, B-α : $ETAT" \
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

# 2. environnement (pip verbeux et minuté) et carte graphique
if [ "$MODE_JOUET" != 1 ] && [ ! -s "$PRET" ]; then
  ETAT="installation de l'environnement"; pousser || true
  t=$(date +%s)
  if ! { python3 -m venv .venv \
         && env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN timeout "$TIMEOUT_PIP" .venv/bin/pip install -v pip==26.2.2 \
         && env -u GH_TOKEN -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN timeout "$TIMEOUT_PIP" .venv/bin/pip install -v \
              -r requirements-neuron-lens-b-alpha-v1.txt; } > "$JPIP" 2>&1; then
    ETAT="environnement non installe (pip en echec ou delai de $TIMEOUT_PIP s)"; log "$ETAT"; tail -5 "$JPIP"; exit 16
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
  if [ -n "${CARTE_ATTENDUE:-}" ] && [[ "$CARTE" != *"$CARTE_ATTENDUE"* ]]; then
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
    export GO_ID COMMIT_REDUIT HF_HOME NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct INSTANCE_ID="${INSTANCE_ID:-}"
    lanceur "$@"
  )
}
courir() {
  local ligne etape cle reseau code
  if [ -e "$DEPOT/diag/$RUN_ID/b-alpha-telecharger-poids.json" ]; then unset HF_TOKEN HUGGING_FACE_HUB_TOKEN; fi
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
