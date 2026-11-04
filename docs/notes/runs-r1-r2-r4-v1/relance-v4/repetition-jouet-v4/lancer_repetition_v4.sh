#!/usr/bin/env bash
# Répétition jouet de bout en bout des deux sessions de la relance v4 de R1 : amorce v2 (`amorce_instance_r1_v4_v2.sh`)
# et script v2 (`r1_v4_instance_v2.sh`) au commit d'essai préparé par test_preparer_repetition_v4.py ; hors réseau
# (dépôt nu local), processeur, jetons factices « jouet », MODE=jouet, PREREG_ABSENT=1, environnement Python existant.
#   bash lancer_repetition_v4.sh <dossier d'essai préparé>
set -u
E=$(cd "$1" && pwd)
SRC=$E/depot-source
C1=$(git -C "$SRC" rev-parse HEAD)
AMORCE="$SRC/scripts/amorce_instance_r1_v4_v2.sh"
commun=(GH_TOKEN=jouet HF_TOKEN=jouet VENV_EXISTANT=/home/user/controle-ia-travail/.venv HF_HUB_OFFLINE=1
        TRANSFORMERS_OFFLINE=1 GIT_TERMINAL_PROMPT=0 MODE=jouet PREREG_ABSENT=1
        CONFIG_REPARATION=essai/reparation-v4-jouet.json CONFIG_REJEU=essai/rejeu-v6-jouet.json
        TESTS_CIBLES=tests/test_garde_depense_v4_v1.py TESTS_ATTENDUS=7 DEPOT_URL="file://$E/depot.git")
jouer() {   # nom, dossier d'amorce, puis variables propres
    local nom=$1 racine=$2 t0 code; shift 2
    mkdir -p "$racine"
    t0=$(date +%s)
    env "${commun[@]}" RACINE_AMORCE="$racine" "$@" timeout 1100 nice -n 10 bash "$AMORCE" > "$E/amorce-$nom.log" 2>&1
    code=$?
    echo "$nom : code $code ($(( $(date +%s) - t0 )) s)" | tee -a "$E/codes.txt"
}
verser() {  # branche du témoin → commit de versement sur main (runs/<run>/ et diag/<run>/ seulement), poussé
    local br=$1 run
    git -C "$SRC" fetch -q "$E/depot.git" "$br"
    run=$(git -C "$SRC" ls-tree --name-only FETCH_HEAD diag/ | sed 's#^diag/##' | grep -E -- '-r1-v4-temoin-jouet$' | head -n 1)
    git -C "$SRC" checkout -q FETCH_HEAD -- "runs/$run" "diag/$run"
    git -C "$SRC" add -A "runs/$run" "diag/$run"
    git -C "$SRC" commit -q -m "versement du témoin $run (essai)"
    git -C "$SRC" push -q "$E/depot.git" HEAD:main
    echo "$run"
}
: > "$E/codes.txt"
# ---- session 1, cas sain
jouer temoin-sain "$E/inst-temoin" COMMIT="$C1" SESSION=temoin PLAFOND_AMORCE_MIN=180 DELAI_ETAPE_MIN=120 \
    BRANCHE=calcul/r1-v4-temoin-jouet-v1
# ---- seconde exécution de l'amorce sur la même instance : refus (R12)
jouer seconde-execution "$E/inst-temoin" COMMIT="$C1" SESSION=temoin PLAFOND_AMORCE_MIN=180 DELAI_ETAPE_MIN=120 \
    BRANCHE=calcul/r1-v4-temoin-jouet-v1b
# ---- versement du témoin, puis session 2, cas sain (jusqu'au rejeu)
RUN_T=$(verser calcul/r1-v4-temoin-jouet-v1)
C2=$(git -C "$SRC" rev-parse HEAD)
echo "témoin versé : $RUN_T ; commit $C2" | tee -a "$E/codes.txt"
jouer reparation-sain "$E/inst-reparation" COMMIT="$C2" SESSION=reparation TEMOIN_RUN="$RUN_T" \
    PLAFOND_AMORCE_MIN=2200 DELAI_ETAPE_MIN=2100 BRANCHE=calcul/r1-v4-reparation-jouet-v1
# ---- artefacts de l'amorce
jouer plafond-zero "$E/inst-a1" COMMIT="$C1" SESSION=temoin PLAFOND_AMORCE_MIN=0 BRANCHE=calcul/a1
jouer plafond-10000 "$E/inst-a2" COMMIT="$C1" SESSION=temoin PLAFOND_AMORCE_MIN=10000 BRANCHE=calcul/a2
jouer session-inconnue "$E/inst-a3" COMMIT="$C1" SESSION=autre PLAFOND_AMORCE_MIN=180 BRANCHE=calcul/a3
# ---- artefacts du témoin (session 2) : témoin arrêté ; sceau du témoin faux
git -C "$SRC" checkout -q -b essai-arrete "$C2"
echo '{}' > "$SRC/diag/$RUN_T/arret.json"
git -C "$SRC" add -A "diag/$RUN_T" && git -C "$SRC" commit -q -m "artefact : témoin arrêté"
git -C "$SRC" push -q "$E/depot.git" HEAD:essai-arrete
C3=$(git -C "$SRC" rev-parse HEAD)
git -C "$SRC" checkout -q -b essai-sceau "$C2"
T=$(ls "$SRC/diag/$RUN_T"/resolution-graine-lot-v3-temoin.json)
printf ' ' >> "$T"
git -C "$SRC" add -A "diag/$RUN_T" && git -C "$SRC" commit -q -m "artefact : résultat du témoin modifié, sceau inchangé"
git -C "$SRC" push -q "$E/depot.git" HEAD:essai-sceau
C4=$(git -C "$SRC" rev-parse HEAD)
git -C "$SRC" checkout -q main
jouer temoin-arrete "$E/inst-a4" COMMIT="$C3" SESSION=reparation TEMOIN_RUN="$RUN_T" PLAFOND_AMORCE_MIN=2200 \
    DELAI_ETAPE_MIN=2100 BRANCHE=calcul/a4
jouer sceau-temoin-faux "$E/inst-a5" COMMIT="$C4" SESSION=reparation TEMOIN_RUN="$RUN_T" PLAFOND_AMORCE_MIN=2200 \
    DELAI_ETAPE_MIN=2100 BRANCHE=calcul/a5
jouer sans-temoin-run "$E/inst-a6" COMMIT="$C2" SESSION=reparation PLAFOND_AMORCE_MIN=2200 DELAI_ETAPE_MIN=2100 \
    BRANCHE=calcul/a6
# ---- branches poussées (noms et présence de fichiers seulement)
echo "== branches de depot.git" | tee -a "$E/codes.txt"
git -C "$E/depot.git" for-each-ref --format='%(refname:short)' refs/heads/ | while read -r b; do
    echo "-- $b : $(git -C "$E/depot.git" ls-tree -r --name-only "$b" -- diag runs prereg traces | grep -vE '20261101-210000-p3-jouet' \
        | grep -E 'r1-v4|R1-table-tokenisation-v4|traces/' | sed -E 's#/[0-9]{8}-[0-9]{6}-#/<run>-#g; s#traces/r1-v4-[a-z]+-[0-9-]+-[A-Za-z0-9]{4}/#traces/<t>/#' | sort -u | tr '\n' ' ')"
done | tee -a "$E/codes.txt"
