#!/usr/bin/env bash
# Répétition à blanc du jour du rendez-vous de P3-bis — v1 (procédure `docs/procedures/P3-bis-rendez-vous-et-verdict-v1.md`).
# Jouet seulement : registres, texte de T0.7, décisions et paquets FACTICES ; aucun fichier du dépôt n'est écrit ; aucun
# réseau ; aucune branche de calcul ni aucun paquet réel n'est touché. Le module d'ouverture est tiré de S par `git show`.
#   1. garde, décisions, journal, `exposer-issue`, contrôle à blanc sur copie (essai_rendez_vous_v1.py) ;
#   2. récupération par refspec explicite, récupération partielle (`blob:none`) et extraction à liste positive, sur un dépôt
#      jetable local qui porte des chemins interdits factices.
# Usage : repetition_rendez_vous_v1.sh <clone du dépôt, lu seulement> <bac neuf, hors de tout arbre git> [<python avec numpy>]
set -uo pipefail
[ $# -ge 2 ] || { echo "usage : repetition_rendez_vous_v1.sh PROJET BAC [PY]"; exit 2; }
PROJET=$(realpath "$1"); BAC=$(realpath -m "$2"); PY=${3:-$PROJET/.venv/bin/python}
ICI=$(dirname "$(realpath "$0")")
S=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0
MODULE_SHA=4a54a437e4a6031b1890f0f5f0261cf1141e72aee82d456d9fcd5483946693e9
RUN=20261113-121129-p3bis-reel
[ -e "$BAC" ] && { echo "ARRÊT : $BAC existe déjà (R12)"; exit 2; }
case "$BAC/" in "$PROJET"/*) echo "ARRÊT : le bac est dans le dépôt"; exit 2 ;; esac
export GIT_CEILING_DIRECTORIES=$(dirname "$BAC") GIT_CONFIG_NOSYSTEM=1 PYTHONDONTWRITEBYTECODE=1
mkdir -p "$BAC/code/src/controle_ia/premier_test_ia"
for f in __init__.py gardes.py scellement.py premier_test_ia/__init__.py premier_test_ia/ouverture_p3bis_v3.py; do
    git -C "$PROJET" show "$S:src/controle_ia/$f" > "$BAC/code/src/controle_ia/$f" || { echo "ARRÊT : $f absent de S"; exit 2; }
done
M=$(sha256sum < "$BAC/code/src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py" | cut -d' ' -f1)
[ "$M" = "$MODULE_SHA" ] && echo "CONFORME module tiré de S : $M" || { echo "ARRÊT : module tiré de S d'empreinte $M"; exit 2; }
echo "--- 1. garde, décisions, journal, exposer-issue, contrôle à blanc"
mkdir -p "$BAC/essais"
(cd "$BAC/essais" && "$PY" -B "$ICI/essai_rendez_vous_v1.py" "$BAC/essais" "$BAC/code/src"); c0=$?
[ "$c0" = 0 ] && echo "RÉPÉTITION PYTHON : TOUT CONFORME" || echo "RÉPÉTITION PYTHON : ÉCHEC (code $c0)"
echo "--- 2. récupération par refspec explicite et extraction à liste positive (dépôt jetable)"
G="$BAC/git"; mkdir -p "$G/source"
git -C "$G/source" init -q -b main . && git -C "$G/source" config user.name essai && git -C "$G/source" config user.email essai@invalid
cd "$G/source" || exit 2
INTERDITS=(docs/notes/bras-attaque/x.md diag/20261109-070232-t06-reel/y runs/20261109-070232-t06-reel/m diag/abc/lecture-sondes-t06.json
           scripts/extraire_mesures_epreuve_t06_v1.py donnees/bras-attaque-z/w donnees/mode-tenu-a-l-ecart-q/w
           prereg/T0.7-sondes-v0-v1.md src/controle_ia/t07/plancher_v2.py traces/autre/z)
for f in "${INTERDITS[@]}" src/controle_ia/__init__.py src/controle_ia/gardes.py src/controle_ia/scellement.py \
         src/controle_ia/premier_test_ia/__init__.py src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py \
         src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py.sha256 src/controle_ia/premier_test_ia/lecture_p3bis_v1.py \
         src/controle_ia/premier_test_ia/lecture_p3bis_v1.py.sha256 src/controle_ia/premier_test_ia/lecture_p3bis_v2.py \
         src/controle_ia/premier_test_ia/lecture_p3bis_v2.py.sha256 src/controle_ia/premier_test_ia/lecture.py; do
    mkdir -p "$(dirname "$f")"; echo "factice $f" > "$f"
done
git add -A && git commit -qm "S factice"
BASE=$(git rev-parse HEAD)
git checkout -q -b calcul/p3bis-reel-v2
for f in "diag/$RUN/resume.json" "diag/$RUN/sondes-figees.json" "diag/$RUN/paquet-run-ferme-v1.json" \
         "diag/$RUN/paquet-run-ferme-v1.tar.000" "runs/$RUN/manifeste.json" traces/p3bis-x/journal.txt; do
    mkdir -p "$(dirname "$f")"; echo "factice $f" > "$f"
done
git add -A && git commit -qm "run"
mkdir -p "diag/p3bis-ferme-$RUN" && echo "paquet factice" > "diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar" && git add -A && git commit -qm "paquet"
git checkout -q main
git clone -q --bare "$G/source" "$G/distant.git" && git -C "$G/distant.git" config uploadpack.allowFilter true
cd "$BAC" || exit 2
# commandes de la procédure, section 4.4 (DEPOT_URL remplacé par le dépôt jetable)
CLONE="$G/clone-calcul"; DEPOT_URL="file://$G/distant.git"
git init -q "$CLONE"
git -C "$CLONE" remote add origin "$DEPOT_URL"
git -C "$CLONE" config remote.origin.promisor true
git -C "$CLONE" config remote.origin.partialclonefilter blob:none
git -C "$CLONE" fetch --no-tags --filter=blob:none -q origin \
    +refs/heads/calcul/p3bis-reel-v2:refs/remotes/origin/calcul/p3bis-reel-v2; c1=$?
git -C "$CLONE" sparse-checkout set --no-cone /src/controle_ia/__init__.py /src/controle_ia/gardes.py \
    /src/controle_ia/scellement.py /src/controle_ia/premier_test_ia/__init__.py \
    '/src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py*' '/src/controle_ia/premier_test_ia/lecture_p3bis_v1.py*' \
    '/src/controle_ia/premier_test_ia/lecture_p3bis_v2.py*' "/diag/p3bis-ferme-$RUN/" "/diag/$RUN/" "/runs/$RUN/" \
    '/traces/p3bis-*/'; c2=$?
git -C "$CLONE" checkout -q --detach refs/remotes/origin/calcul/p3bis-reel-v2; c3=$?
ok=0; n=0
verdict() { n=$((n + 1)); if [ "$1" = 0 ]; then ok=$((ok + 1)); echo "CONFORME $2"; else echo "NON CONFORME $2"; fi; }
verdict $((c1 + c2 + c3)) "fetch à refspec explicite, extraction partielle, extraction détachée : codes $c1 $c2 $c3"
ATTENDUS=$(printf '%s\n' "diag/$RUN/paquet-run-ferme-v1.json" "diag/$RUN/paquet-run-ferme-v1.tar.000" "diag/$RUN/resume.json" \
    "diag/$RUN/sondes-figees.json" "diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar" "runs/$RUN/manifeste.json" \
    src/controle_ia/__init__.py src/controle_ia/gardes.py src/controle_ia/premier_test_ia/__init__.py \
    src/controle_ia/premier_test_ia/lecture_p3bis_v1.py src/controle_ia/premier_test_ia/lecture_p3bis_v1.py.sha256 \
    src/controle_ia/premier_test_ia/lecture_p3bis_v2.py src/controle_ia/premier_test_ia/lecture_p3bis_v2.py.sha256 \
    src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py.sha256 \
    src/controle_ia/scellement.py traces/p3bis-x/journal.txt | sort)
OBTENUS=$(cd "$CLONE" && find . -path ./.git -prune -o -type f -print | sed 's#^\./##' | sort)
[ "$OBTENUS" = "$ATTENDUS" ]; verdict $? "extraction : exactement les $(printf '%s\n' "$ATTENDUS" | wc -l) chemins de la liste positive"
absents=0; for f in "${INTERDITS[@]}"; do [ -e "$CLONE/$f" ] && absents=1; done
verdict $absents "aucun des ${#INTERDITS[@]} chemins interdits factices extrait"
[ "$(git -C "$CLONE" log -1 --format=%s -- "diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar")" = paquet ]
verdict $? "date de la mise en paquet lisible par git log (commit du paquet)"
git -C "$CLONE" merge-base --is-ancestor "$BASE" HEAD; verdict $? "S factice ancêtre de la tête (historique complet, sans contenu)"
[ "$(git -C "$CLONE" for-each-ref --format='%(refname)')" = refs/remotes/origin/calcul/p3bis-reel-v2 ]
verdict $? "une seule référence récupérée : refs/remotes/origin/calcul/p3bis-reel-v2"
echo "BILAN GIT : $ok conformes sur $n"
[ "$ok" = "$n" ] && echo "RÉPÉTITION GIT : TOUT CONFORME" || echo "RÉPÉTITION GIT : ÉCHEC"
[ "$ok" = "$n" ] && [ "$c0" = 0 ] && { echo "RÉPÉTITION : TOUT CONFORME"; exit 0; }
echo "RÉPÉTITION : ÉCHEC"; exit 1
