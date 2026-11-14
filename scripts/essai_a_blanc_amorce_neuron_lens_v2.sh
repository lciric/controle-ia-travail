#!/usr/bin/env bash
# Essai à blanc (sans location) de l'amorce v2 de la machine du volet A de « Neuron Lens » : dépôt distant remplacé par un dépôt nu
# local, même clone que l'entrée de l'instance (`--depth 1 --single-branch`, jeton factice en en-tête), mode jouet. Cas nominal avec la
# liste réelle des essais rapides, puis artefacts (R5) : mauvais commit (10), essai en échec (12), essai sauté (12), première poussée
# impossible (14) ; balayage du jeton factice sur tout le disque de l'essai, le dépôt distant et les journaux.
# Usage : bash scripts/essai_a_blanc_amorce_neuron_lens_v2.sh <COMMIT_SOURCE> <dossier neuf>
set -uo pipefail
SRC=$(cd "$(dirname "$0")/.." && pwd)
C=$1; S=$2
[ -e "$S" ] && { echo "dossier existant"; exit 2; }
mkdir -p "$S"
"$SRC/.venv/bin/python" "$SRC/scripts/depot_reduit_neuron_lens_volet_a_v6.py" "$C" "$S/r" > "$S/rapport-reduit.txt" || exit 3
CR=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['commit_reduit'])" "$S/r/rapport.json")
BR=course/neuron-lens-volet-a-reduit-v6
git init -q --bare "$S/distant.git"
git -C "$S/r/depot" push -q "$S/distant.git" "course:refs/heads/$BR" 2>/dev/null
export GH_TOKEN=jeton-factice-ABCDEF0123456789
VENV="$SRC/.venv"
cas() {  # nom commit essais url commande_course
  local nom=$1 commit=$2 essais=$3 url=$4 course=$5 d="$S/m-$1"
  mkdir -p "$d"
  git -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)" \
    clone -q --depth 1 --single-branch --branch "$BR" "file://$S/distant.git" "$d/depot" 2>/dev/null
  [ "$url" != ok ] && git -C "$d/depot" remote set-url origin "file://$S/inexistant.git"
  (cd "$d" && COMMIT_REDUIT=$commit GO_ID=GO-2026-11-14-05 MODE_JOUET=1 VENV_JOUET=$VENV PERIODE_POUSSE_S=2 RUN_ID="r-$nom" \
     BRANCHE_RESULTATS="calcul/essai-$nom" ESSAIS="$essais" COMMANDE_COURSE="$course" \
     timeout 900 bash depot/scripts/amorce_neuron_lens_volet_a_v2.sh > "$S/journal-$nom.txt" 2>&1)
  local code=$?
  local etat
  etat=$(git -C "$S/distant.git" show "calcul/essai-$nom:etat-neuron-lens-volet-a.txt" 2>/dev/null | grep '^etat=' || echo "etat=(aucune branche poussée)")
  echo "CAS $nom : code=$code ; $etat"
}
REELS="tests/test_neuron_lens_volet_a_extraction_v2.py tests/test_neuron_lens_volet_a_chargement_v1.py tests/test_neuron_lens_volet_a_lancer_v3.py tests/test_neuron_lens_volet_a_donnees_v1.py tests/test_neuron_lens_volet_a_donnees_v2.py tests/test_neuron_lens_volet_a_sondes_v2.py tests/test_neuron_lens_volet_a_lectures_v2.py tests/test_neuron_lens_garde_depense_v3.py"
COURSE='mkdir -p diag/$RUN_ID runs/$RUN_ID; for i in 1 2 3; do echo "{\"i\":$i}" > diag/$RUN_ID/brut-$i.json; sleep 3; done; [ -z "${GH_TOKEN:-}" ] && echo "course sans jeton"'
printf 'import pytest\n@pytest.mark.skip\ndef test_x():\n    pass\n' > "$S/saute_test.py"
echo "ESSAI A BLANC amorce v2 ; commit source $C ; commit reduit $CR ; $(date -u +%FT%TZ)"
cas nominal "$CR" "$REELS" ok "$COURSE"
echo "  journal nominal :"; grep -E "AMORCE|passed|failed|course sans jeton" "$S/journal-nominal.txt" | sed 's/^/    /'
echo "  fichiers de la branche des résultats :"; git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-nominal | grep -E '^(diag|runs)/|^etat' | sed 's/^/    /'
cas commit 0000000000000000000000000000000000000000 "tests/test_neuron_lens_garde_depense_v3.py" ok true
cas echec "$CR" "tests/test_neuron_lens_garde_depense_v3.py tests/inexistant.py" ok true
cas saute "$CR" "tests/test_neuron_lens_garde_depense_v3.py $S/saute_test.py" ok true
cas poussee "$CR" "tests/test_neuron_lens_garde_depense_v3.py" ko true
grep -h "AMORCE" "$S/journal-commit.txt" "$S/journal-poussee.txt" | sed 's/^/    /'
n=$(grep -rl --binary-files=text "jeton-factice-ABCDEF0123456789" "$S"/m-* "$S/distant.git" "$S"/journal-*.txt 2>/dev/null | wc -l)
echo "BALAYAGE du jeton factice (disques des machines d'essai, depot distant, journaux) : $n fichier(s)"
