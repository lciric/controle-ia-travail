#!/usr/bin/env bash
# Relecture « données et fuites », v1 : passages de l'instance jouet par l'amorce et le script de l'instance du S jouet
# (scripts versés tels quels ; seule la suite des tests est remplacée par un bouchon, par l'environnement factice).
#   a : cas sain (BRANCHE=calcul/p4-jouet-a-v1) : run jouet de P4, résultats, tableaux et traces poussés ;
#   b : environnement absent (BRANCHE=calcul/p4-jouet-b-v1) : arrêt avant le run, traces seules poussées.
# Jetons factices seulement ; dépôt distant local ; aucun réseau.
set -uo pipefail
W=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-donnees
J=$W/jouet-b
S=$(cat "$J/S.txt")
AMORCE=$J/source/docs/procedures/P4-instrument-v1/amorce_instance_p4_v1.sh
passage() {   # $1 nom, $2 branche, $3 environnement
    local n=$1 b=$2 venv=$3 debut code
    [ -e "$J/racine-$n" ] && { echo "$J/racine-$n existe déjà (R12)"; return 2; }
    mkdir -p "$J/racine-$n"
    debut=$(date +%s)
    env -i PATH="/usr/bin:/bin" LANG=C.UTF-8 HOME="$J/racine-$n" TMPDIR="$W/tmp" COMMIT="$S" GH_TOKEN=factice-gh-relecture-0001 \
        HF_TOKEN=factice-hf-relecture-0001 MODE=jouet DEPOT_URL="$J/distant.git" RACINE_AMORCE="$J/racine-$n" VENV_EXISTANT="$venv" \
        PYTHONDONTWRITEBYTECODE=1 GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=commit.gpgsign GIT_CONFIG_VALUE_0=false \
        BRANCHE="$b" bash "$AMORCE" > "$J/amorce-$n.log" 2>&1
    code=$?
    echo "passage $n : code $code ; $(( $(date +%s) - debut )) s"
    grep -h "^AMORCE" "$J/amorce-$n.log" | cut -c1-200 | sed 's/^/    | /'
    grep -hE "tests :|run :|ARRÊT|poussée|préenregistrement lu|^PROGRES .* etape=(M5|fin) " "$J/racine-$n/p4/journal.txt" 2>/dev/null \
        | cut -c1-200 | sed 's/^/    | /'
    rm -rf "$J/racine-$n/p4/controle-ia" "$J/racine-$n/amorce-depot"
}
passage a calcul/p4-jouet-a-v1 "$W/outils/venv-faux"
passage b calcul/p4-jouet-b-v1 "$W/outils/environnement-absent"
git -C "$J/distant.git" branch -a | sed 's/^/branche distante : /'
find "$W" -name __pycache__ -type d | head -3 | sed 's/^/__pycache__ écrit : /'
echo "FIN DES PASSAGES"
