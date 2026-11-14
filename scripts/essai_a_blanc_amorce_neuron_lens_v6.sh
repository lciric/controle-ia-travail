#!/usr/bin/env bash
# Essai à blanc (sans location) de l'amorce v5 de la machine du volet A de « Neuron Lens » — v6 (v5 avec le compteur du cas « crochet »
# ancré sur l'heure : la v5 comptait aussi la ligne « etat non pousse : … » ; v5 : contre-lecture 8 : N-3, N-4, N-8 b).
# Dépôt distant remplacé par un dépôt nu local, même clone que l'entrée de l'instance (`--depth 1 --single-branch`, jeton factice en
# en-tête), mode jouet, dépôt réduit v9. Cas nominal avec la liste réelle des essais rapides plus une sonde qui échoue si `GH_TOKEN`
# est dans l'environnement de pytest, et une course jouet qui écrit un fichier de 96 Mio (exclu de la poussée) ; artefacts (R5) :
# mauvais commit (10), arbre non propre (10), essai en échec (12), essai sauté (12), arbre sali par les essais (12), carte graphique
# absente (11), première poussée impossible (14), poussée finale impossible après une course réussie (15), commit impossible pendant la
# course (crochet `pre-commit` qui échoue : 15, et aucun « pousse » écrit après), fichier déjà poussé qui grossit au-delà de 95 Mo
# (version déjà poussée gardée à la tête, `exclus=1`) ; la sonde « sans jeton » jouée seule avec le jeton présent (elle doit échouer).
# Balayage du jeton factice sous toutes les formes de `suivi_vast_v3.formes` (pour ce jeton, brute = adresse : caractères sûrs) : sur
# les fichiers (disques des machines d'essai, dépôt distant, journaux) ET sur les objets git décompressés (`cat-file
# --batch-all-objects`) du dépôt distant et des clones ; témoins positifs exigés (un fichier par forme, et un dépôt témoin dont un
# message de commit porte une forme) ; erreur de `grep` non masquée. Non couverts (déclarés) : le chemin réel (environnement, `pip`,
# carte réelle, vraie course), le code 13, le clone HTTPS réel, les signaux.
# Usage : bash scripts/essai_a_blanc_amorce_neuron_lens_v6.sh <COMMIT_SOURCE> <dossier neuf>
set -uo pipefail
SRC=$(cd "$(dirname "$0")/.." && pwd)
C=$(git -C "$SRC" rev-parse "$1") || exit 2; S=$2
[ -e "$S" ] && { echo "dossier existant"; exit 2; }
mkdir -p "$S"
"$SRC/.venv/bin/python" "$SRC/scripts/depot_reduit_neuron_lens_volet_a_v9.py" "$C" "$S/r" > "$S/rapport-reduit.txt" || exit 3
champ() { python3 -c "import json,sys;print(json.load(open(sys.argv[1]))[sys.argv[2]])" "$S/r/rapport.json" "$1"; }
CR=$(champ commit_reduit)
BR=course/neuron-lens-volet-a-reduit-v9
git init -q --bare "$S/distant.git"
git -C "$S/r/depot" push -q "$S/distant.git" "course:refs/heads/$BR" 2>/dev/null
export GH_TOKEN=ghp_facticeABCDEF0123456789abcdefXYZ
VENV="$SRC/.venv"
printf 'import pytest\n@pytest.mark.skip\ndef test_x():\n    pass\n' > "$S/saute_test.py"
printf 'import os\ndef test_sans_jeton():\n    assert "GH_TOKEN" not in os.environ\n' > "$S/sans_jeton_test.py"
printf 'from pathlib import Path\ndef test_salit():\n    Path("sali.txt").write_text("x")\n' > "$S/salit_test.py"
cas() {  # nom commit essais url course [variables supplémentaires…]
  local nom=$1 commit=$2 essais=$3 url=$4 course=$5 d="$S/m-$1"; shift 5
  mkdir -p "$d"
  git -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)" \
    clone -q --depth 1 --single-branch --branch "$BR" "file://$S/distant.git" "$d/depot" 2>/dev/null
  [ "$url" = ko ] && git -C "$d/depot" remote set-url origin "file://$S/inexistant.git"
  [ "$url" = sale ] && echo x > "$d/depot/non-suivi.txt"
  (cd "$d" && env COMMIT_REDUIT="$commit" GO_ID=GO-2026-11-14-05 MODE_JOUET=1 VENV_JOUET="$VENV" PERIODE_POUSSE_S=2 RUN_ID="r-$nom" \
     BRANCHE_RESULTATS="calcul/essai-$nom" ESSAIS="$essais" COMMANDE_COURSE="$course" ESSAIS_POUSSEE_FINALE=2 \
     ATTENTE_POUSSEE_FINALE_S=1 "$@" timeout 900 bash depot/scripts/amorce_neuron_lens_volet_a_v5.sh > "$S/journal-$nom.txt" 2>&1)
  local code=$?
  local etat
  etat=$(git -C "$S/distant.git" show "calcul/essai-$nom:etat-neuron-lens-volet-a.txt" 2>/dev/null | grep -E '^(etat|exclus)=' | tr '\n' ' ' || true)
  echo "CAS $nom : code=$code ; ${etat:-etat=(aucune branche poussée)} ; derniere ligne : $(tail -1 "$S/journal-$nom.txt" | cut -d' ' -f3-)"
}
REELS="tests/test_neuron_lens_volet_a_extraction_v2.py tests/test_neuron_lens_volet_a_chargement_v1.py tests/test_neuron_lens_volet_a_lancer_v3.py tests/test_neuron_lens_volet_a_donnees_v1.py tests/test_neuron_lens_volet_a_donnees_v2.py tests/test_neuron_lens_volet_a_sondes_v2.py tests/test_neuron_lens_volet_a_lectures_v2.py tests/test_neuron_lens_garde_depense_v3.py"
G=tests/test_neuron_lens_garde_depense_v3.py
COURSE='mkdir -p diag/$RUN_ID runs/$RUN_ID; for i in 1 2 3; do echo "{\"i\":$i}" > diag/$RUN_ID/brut-$i.json; sleep 3; done; head -c 100663296 /dev/zero > diag/$RUN_ID/gros-96Mio.bin; sleep 3; [ -z "${GH_TOKEN:-}" ] && echo "course sans jeton"'
COURSE_FINALE='mkdir -p diag/$RUN_ID; echo "{}" > diag/$RUN_ID/brut-1.json; sleep 4; git remote set-url origin "file:///inexistant-essai.git"; sleep 1'
COURSE_CROCHET='mkdir -p diag/$RUN_ID; echo "{}" > diag/$RUN_ID/brut-1.json; sleep 4; printf "#!/bin/sh\nexit 1\n" > .git/hooks/pre-commit; chmod 755 .git/hooks/pre-commit; echo "{}" > diag/$RUN_ID/brut-2.json; sleep 4'
COURSE_GROSSIT='mkdir -p diag/$RUN_ID; head -c 1048576 /dev/zero > diag/$RUN_ID/g.bin; sleep 5; head -c 100663296 /dev/zero > diag/$RUN_ID/g.bin; sleep 4'
echo "ESSAI A BLANC v6 de l'amorce v5 ; commit source $C ; commit reduit $CR ; liste $(champ liste_sha256) ; paquet $(champ paquet_sha256) ; $(champ n_fichiers) fichiers ; $(date -u +%FT%TZ)"
cas nominal "$CR" "$REELS $S/sans_jeton_test.py" ok "$COURSE"
echo "  journal nominal :"; grep -E "AMORCE|passed|failed|course sans jeton" "$S/journal-nominal.txt" | sed 's/^/    /'
echo "  fichiers de la branche des résultats :"; git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-nominal | grep -E '^(diag|runs)/|^etat' | sed 's/^/    /'
echo "  fichier de 96 Mio resté sur le disque de la machine : $(ls "$S/m-nominal/depot/diag/r-nominal/gros-96Mio.bin" 2>/dev/null || echo absent)"
cas commit 0000000000000000000000000000000000000000 "$G" ok true
cas arbre "$CR" "$G" sale true
cas echec "$CR" "$G tests/inexistant.py" ok true
cas saute "$CR" "$G $S/saute_test.py" ok true
cas sali "$CR" "$G $S/salit_test.py" ok true
cas carte "$CR" "$G" ok true EXIGER_CARTE_JOUET=1
cas poussee "$CR" "$G" ko true
cas finale "$CR" "$G" ok "$COURSE_FINALE"
cas crochet "$CR" "$G" ok "$COURSE_CROCHET"
cas grossit "$CR" "$G" ok "$COURSE_GROSSIT"
echo "  journaux des cas commit, poussee, finale, crochet et grossit :"
grep -h "AMORCE" "$S/journal-commit.txt" "$S/journal-poussee.txt" "$S/journal-finale.txt" "$S/journal-crochet.txt" "$S/journal-grossit.txt" | sed 's/^/    /'
echo "  crochet : « git commit impossible » : $(grep -c 'git commit impossible' "$S/journal-crochet.txt") ligne(s) (attendu ≥ 1) ; lignes « pousse » écrites après le premier refus : $(sed -n '/git commit impossible/,$p' "$S/journal-crochet.txt" | grep -cE 'Z pousse :') (attendu 0) ; brut-2.json sur la branche : $(git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-crochet | grep -c brut-2.json) (attendu 0)"
echo "  grossit : taille de g.bin à la tête de la branche : $(git -C "$S/distant.git" cat-file -s "calcul/essai-grossit:diag/r-grossit/g.bin" 2>&1) (attendu 1048576)"
( cd "$S/r/depot" && env GH_TOKEN="$GH_TOKEN" "$VENV/bin/python" -m pytest -q -p no:cacheprovider "$S/sans_jeton_test.py" > "$S/journal-sonde-jeton.txt" 2>&1 )
echo "ARTEFACT de la sonde « sans jeton » jouée avec le jeton présent : code=$? (attendu : non nul) ; $(tail -1 "$S/journal-sonde-jeton.txt")"
# balayage : formes, témoins positifs, fichiers puis objets git décompressés
FORMES="$S/formes.txt"
CONTROLE_IA_GITHUB_TOKEN_2="$GH_TOKEN" PYTHONPATH="$SRC/src" "$VENV/bin/python" -c \
  'import os; from controle_ia.neuron_lens.suivi_vast_v3 import formes; print("\n".join(formes(os.environ["CONTROLE_IA_GITHUB_TOKEN_2"])))' > "$FORMES"
nf=$(wc -l < "$FORMES")
mkdir -p "$S/temoins"; i=0
while IFS= read -r f; do i=$((i + 1)); printf 'temoin %s fin\n' "$f" > "$S/temoins/forme-$i.txt"; done < "$FORMES"
git init -q "$S/temoin-git"; echo x > "$S/temoin-git/x"; git -C "$S/temoin-git" add x
git -C "$S/temoin-git" -c user.name=t -c user.email=t@example.invalid commit -q -m "message $(head -1 "$FORMES")"
balayer_fichiers() { grep -rlF --binary-files=text -f "$FORMES" "$@"; local c=$?; [ "$c" -le 1 ] || echo "ERREUR grep code $c" >&2; }
nt=$(balayer_fichiers "$S/temoins" | wc -l)
n=$(balayer_fichiers "$S"/m-* "$S/distant.git" "$S"/journal-*.txt | wc -l)
objets() { git -C "$1" cat-file --batch-all-objects --batch 2>/dev/null | grep -caF -f "$FORMES"; }
nto=$(objets "$S/temoin-git")
no=0; nd=0
for g in "$S/distant.git" "$S"/m-*/depot; do nd=$((nd + 1)); k=$(objets "$g"); no=$((no + k)); done
echo "TEMOINS du balayage : $nt fichier(s) témoin(s) détecté(s) sur $nf (attendu $nf) ; dépôt témoin : $nto ligne(s) d'objet détectée(s) (attendu ≥ 1)"
echo "BALAYAGE du jeton factice ($nf formes ; pour ce jeton, brute = adresse) : fichiers (disques des machines d'essai, dépôt distant, journaux) : $n fichier(s) ; objets git décompressés de $nd dépôt(s) (distant et clones) : $no ligne(s)"
