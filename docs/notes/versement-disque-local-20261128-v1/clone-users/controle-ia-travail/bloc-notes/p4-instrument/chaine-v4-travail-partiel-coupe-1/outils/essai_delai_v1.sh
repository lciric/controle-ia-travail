#!/usr/bin/env bash
# Outil de travail du correcteur de la chaîne v4 (non versé) : mesure du run jouet de P4 (durée, instant du manifeste)
# et essai du délai externe (timeout TERM) sur un monde jouet tiré d'un C d'essai, pour régler le sixième passage de la
# répétition (VC2-fidelite-07). Aucun outil de location, aucun réseau.
# Usage : essai_delai_v1.sh DEPOT C CANDIDAT RACINE_NEUVE DELAI…
set -uo pipefail
D=$1; C=$2; CANDIDAT=$(realpath "$3"); R=$(realpath -m "$4"); shift 4
P4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument
OUTILS=$P4/chaine-v4/outils_essais_p4_v1.py
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
V=docs/procedures/P4-instrument-v1
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
[ -e "$R" ] && { echo "$R existe"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --shared --no-checkout "$D" source && cd source || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git checkout -q "$C" && git checkout -q -B main || exit 2
N=1166
MONDE=$("$PY" -B "$OUTILS" monde . "$V" "$R/travail" prereg/P4-instrument-config-v1.json) || exit 2
CFG_SHA=$(printf '%s' "$MONDE" | python3 -c 'import json, sys; print(json.load(sys.stdin)["config"])')
"$PY" -B "$OUTILS" jouet "$CANDIDAT" prereg/P4-instrument-v1.md . "$CFG_SHA" "$N" > /dev/null || exit 2
git add -A prereg diag runs && git add -f donnees && git commit -qm "essai : monde jouet" || exit 2
echo "monde : $MONDE"
for d in sans "$@"; do
    git clone -q "$R/source" "$R/run-$d" && cd "$R/run-$d" || exit 2
    git config user.email essai@invalid; git config user.name essai
    RUN="$(date -u +%Y%m%d-%H%M%S)-p4-jouet"
    t0=$(date +%s.%N)
    if [ "$d" = sans ]; then
        PYTHONPATH=src "$PY" -B "$V/instrument_p4_v1.py" --config prereg/P4-instrument-config-v1.json --prereg prereg/P4-instrument-v1.md --run-id "$RUN" > "$R/run-$d.json" 2> "$R/run-$d.err"; c=$?
    else
        PYTHONPATH=src timeout --signal=TERM --kill-after=5m "$d" "$PY" -B "$V/instrument_p4_v1.py" --config prereg/P4-instrument-config-v1.json --prereg prereg/P4-instrument-v1.md --run-id "$RUN" > "$R/run-$d.json" 2> "$R/run-$d.err"; c=$?
    fi
    t1=$(date +%s.%N)
    m=$(stat -c %Y "runs/$RUN/manifeste.json" 2>/dev/null || echo absent)
    motif=$(python3 -c 'import json, sys; r = json.load(open(sys.argv[1]))["resultat"]; print((r.get("arret") or {}).get("motif"), "|", (r.get("arret") or {}).get("etape"))' "diag/$RUN/resume.json" 2>/dev/null || echo "résumé absent")
    echo "délai $d : code $c ; durée $(python3 -c "print(round($t1 - $t0, 2))") s ; manifeste à +$( [ "$m" = absent ] && echo absent || python3 -c "print(round($m - $t0, 2))") s ; arrêt : $motif"
    grep '^PROGRES' "$R/run-$d.err" | head -20 | sed 's/^/    /'
    cd "$R"
done
