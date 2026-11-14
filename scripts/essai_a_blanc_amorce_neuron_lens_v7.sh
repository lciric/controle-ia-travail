#!/usr/bin/env bash
# Essai à blanc (sans location) de l'amorce v6 de la machine du volet A de « Neuron Lens » — v7 (contre-lecture 9 : P-2, P-3, P-4).
# Dépôt distant remplacé par un dépôt nu local, même clone que l'entrée de l'instance (`--depth 1 --single-branch`, jeton factice en
# en-tête), mode jouet, dépôt réduit v10. Chaque cas porte son code attendu ; le verdict final compte les écarts.
# Cas : nominal (liste réelle des essais rapides + sonde « sans jeton » ; fichier de 96 Mio exclu) ; mauvais commit (10) ; arbre non
# propre (10) ; essai en échec (12) ; essai sauté (12) ; arbre sali (12) ; carte absente (11) ; première poussée impossible (14) ;
# poussée finale impossible (15) ; commit refusé par un crochet (15) ; fichier qui grossit (0, version déjà poussée gardée) ; et, v7 :
# tête distante falsifiée par une enveloppe de `git` (14, aucun « pousse ») ; `find` en échec (14) ; `find` muet avec un fichier de 96
# Mio (le second contrôle refuse le commit : 15) ; copie impossible (15) ; index verrouillé (`git add` impossible : 15) ; état non
# inscriptible (15). Sonde « sans jeton » jouée seule avec le jeton présent (doit échouer).
# Balayage du jeton factice sous les formes de `suivi_vast_v4.formes` (pour ce jeton, brute = adresse) : fichiers (disques des
# machines d'essai, dépôt distant, journaux) et objets git décompressés (`cat-file --batch-all-objects`) de chaque dépôt, avec le
# nombre d'objets lus (non nul exigé) ; témoins positifs exigés : un fichier par forme ; un dépôt témoin dont un blob ET un message
# portent une forme, empaqueté (`git gc`). Erreurs de `grep` et de `git` non masquées : elles comptent comme écarts.
# Non couverts (déclarés) : chemin réel (environnement, `pip`, carte réelle, vraie course), code 13, clone HTTPS réel, signaux,
# restauration `checkout` impossible d'un fichier qui grossit, abandon par `set -e`.
# Usage : bash scripts/essai_a_blanc_amorce_neuron_lens_v7.sh <COMMIT_SOURCE> <dossier neuf>
set -uo pipefail
SRC=$(cd "$(dirname "$0")/.." && pwd)
C=$(git -C "$SRC" rev-parse "$1") || exit 2; S=$2
[ -e "$S" ] && { echo "dossier existant"; exit 2; }
mkdir -p "$S"
ECARTS_F="$S/ecarts.txt"; : > "$ECARTS_F"
ecart() { echo "$*" >> "$ECARTS_F"; echo "  ÉCART : $*" >&2; }  # compté par fichier : juste aussi depuis un sous-shell
"$SRC/.venv/bin/python" "$SRC/scripts/depot_reduit_neuron_lens_volet_a_v10.py" "$C" "$S/r" > "$S/rapport-reduit.txt" || exit 3
champ() { python3 -c "import json,sys;print(json.load(open(sys.argv[1]))[sys.argv[2]])" "$S/r/rapport.json" "$1"; }
CR=$(champ commit_reduit)
BR=course/neuron-lens-volet-a-reduit-v10
git init -q --bare "$S/distant.git" || exit 3
git -C "$S/r/depot" push -q "$S/distant.git" "course:refs/heads/$BR" || exit 3
export GH_TOKEN=ghp_facticeABCDEF0123456789abcdefXYZ
VENV="$SRC/.venv"
GIT=$(command -v git); FIND=$(command -v find)
printf 'import pytest\n@pytest.mark.skip\ndef test_x():\n    pass\n' > "$S/saute_test.py"
printf 'import os\ndef test_sans_jeton():\n    assert "GH_TOKEN" not in os.environ\n' > "$S/sans_jeton_test.py"
printf 'from pathlib import Path\ndef test_salit():\n    Path("sali.txt").write_text("x")\n' > "$S/salit_test.py"
# enveloppes (artefacts) : chacune dans son dossier, placé en tête du PATH du seul cas concerné
mkdir -p "$S/env/lsremote" "$S/env/findko" "$S/env/findmuet" "$S/env/cpko"
printf '#!/bin/sh\nfor a in "$@"; do [ "$a" = ls-remote ] && { printf "%%s\\trefs/heads/x\\n" 0000000000000000000000000000000000000001; exit 0; }; done\nexec %s "$@"\n' "$GIT" > "$S/env/lsremote/git"
printf '#!/bin/sh\nexit 1\n' > "$S/env/findko/find"
printf '#!/bin/sh\nexit 0\n' > "$S/env/findmuet/find"
printf '#!/bin/sh\nexit 1\n' > "$S/env/cpko/cp"
chmod 755 "$S"/env/*/*
cas() {  # nom attendu commit essais url course [variables supplémentaires…]
  local nom=$1 attendu=$2 commit=$3 essais=$4 url=$5 course=$6 d="$S/m-$1"; shift 6
  mkdir -p "$d"
  git -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)" \
    clone -q --depth 1 --single-branch --branch "$BR" "file://$S/distant.git" "$d/depot" || ecart "clone du cas $nom impossible"
  [ "$url" = ko ] && git -C "$d/depot" remote set-url origin "file://$S/inexistant.git"
  [ "$url" = sale ] && echo x > "$d/depot/non-suivi.txt"
  (cd "$d" && env COMMIT_REDUIT="$commit" GO_ID=GO-2026-11-14-05 MODE_JOUET=1 VENV_JOUET="$VENV" PERIODE_POUSSE_S=2 RUN_ID="r-$nom" \
     BRANCHE_RESULTATS="calcul/essai-$nom" ESSAIS="$essais" COMMANDE_COURSE="$course" ESSAIS_POUSSEE_FINALE=2 \
     ATTENTE_POUSSEE_FINALE_S=1 "$@" timeout 900 bash depot/scripts/amorce_neuron_lens_volet_a_v6.sh > "$S/journal-$nom.txt" 2>&1)
  local code=$?
  local etat
  etat=$(git -C "$S/distant.git" show "calcul/essai-$nom:etat-neuron-lens-volet-a.txt" 2>/dev/null | grep -E '^(etat|exclus|exclus_fichiers)=' | tr '\n' ' ' || true)
  echo "CAS $nom : code=$code (attendu $attendu) ; ${etat:-etat=(aucune branche poussée)} ; derniere ligne : $(tail -1 "$S/journal-$nom.txt" | cut -d' ' -f3-)"
  [ "$code" = "$attendu" ] || ecart "cas $nom : code $code au lieu de $attendu"
}
sans_pousse_apres() {  # cas motif : aucune ligne « pousse » après la première ligne qui porte le motif
  local n
  n=$(sed -n "/$2/,\$p" "$S/journal-$1.txt" | grep -cE 'Z pousse :')
  local m; m=$(grep -c "$2" "$S/journal-$1.txt")
  echo "  $1 : « $2 » : $m ligne(s) (attendu ≥ 1) ; lignes « pousse » après la première : $n (attendu 0)"
  [ "$m" -ge 1 ] && [ "$n" -eq 0 ] || ecart "cas $1 : motif « $2 » absent ou « pousse » écrit après"
}
REELS="tests/test_neuron_lens_volet_a_extraction_v2.py tests/test_neuron_lens_volet_a_chargement_v1.py tests/test_neuron_lens_volet_a_lancer_v3.py tests/test_neuron_lens_volet_a_donnees_v1.py tests/test_neuron_lens_volet_a_donnees_v2.py tests/test_neuron_lens_volet_a_sondes_v2.py tests/test_neuron_lens_volet_a_lectures_v2.py tests/test_neuron_lens_garde_depense_v3.py"
G=tests/test_neuron_lens_garde_depense_v3.py
DEBUT='mkdir -p diag/$RUN_ID; echo "{}" > diag/$RUN_ID/brut-1.json; sleep 4'
COURSE='mkdir -p diag/$RUN_ID runs/$RUN_ID; for i in 1 2 3; do echo "{\"i\":$i}" > diag/$RUN_ID/brut-$i.json; sleep 3; done; head -c 100663296 /dev/zero > diag/$RUN_ID/gros-96Mio.bin; sleep 3; [ -z "${GH_TOKEN:-}" ] && echo "course sans jeton"'
COURSE_FINALE="$DEBUT"'; git remote set-url origin "file:///inexistant-essai.git"; sleep 1'
COURSE_CROCHET="$DEBUT"'; printf "#!/bin/sh\nexit 1\n" > .git/hooks/pre-commit; chmod 755 .git/hooks/pre-commit; echo "{}" > diag/$RUN_ID/brut-2.json; sleep 4'
COURSE_GROSSIT='mkdir -p diag/$RUN_ID; head -c 1048576 /dev/zero > diag/$RUN_ID/g.bin; sleep 5; head -c 100663296 /dev/zero > diag/$RUN_ID/g.bin; sleep 4'
COURSE_GROS='mkdir -p diag/$RUN_ID; head -c 100663296 /dev/zero > diag/$RUN_ID/gros-96Mio.bin; sleep 5'
COURSE_INDEX="$DEBUT"'; : > .git/worktrees/resultats-neuron-lens/index.lock; echo "{}" > diag/$RUN_ID/brut-2.json; sleep 4'
COURSE_ETAT="$DEBUT"'; rm -f ../resultats-neuron-lens/etat-neuron-lens-volet-a.txt; mkdir ../resultats-neuron-lens/etat-neuron-lens-volet-a.txt; sleep 4'
echo "ESSAI A BLANC v7 de l'amorce v6 ; commit source $C ; commit reduit $CR ; liste $(champ liste_sha256) ; paquet $(champ paquet_sha256) ; $(champ n_fichiers) fichiers ; $(date -u +%FT%TZ)"
cas nominal 0 "$CR" "$REELS $S/sans_jeton_test.py" ok "$COURSE"
echo "  journal nominal :"; grep -E "AMORCE|passed|failed|course sans jeton" "$S/journal-nominal.txt" | sed 's/^/    /'
echo "  fichiers de la branche des résultats :"; git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-nominal | grep -E '^(diag|runs)/|^etat' | sed 's/^/    /'
[ -f "$S/m-nominal/depot/diag/r-nominal/gros-96Mio.bin" ] && echo "  fichier de 96 Mio resté sur le disque de la machine : oui" || ecart "fichier de 96 Mio absent du disque de la machine"
grep -q 'course sans jeton' "$S/journal-nominal.txt" || ecart "course nominale : « course sans jeton » absent"
cas commit 10 0000000000000000000000000000000000000000 "$G" ok true
cas arbre 10 "$CR" "$G" sale true
cas echec 12 "$CR" "$G tests/inexistant.py" ok true
cas saute 12 "$CR" "$G $S/saute_test.py" ok true
cas sali 12 "$CR" "$G $S/salit_test.py" ok true
cas carte 11 "$CR" "$G" ok true EXIGER_CARTE_JOUET=1
cas poussee 14 "$CR" "$G" ko true
cas finale 15 "$CR" "$G" ok "$COURSE_FINALE"
cas crochet 15 "$CR" "$G" ok "$COURSE_CROCHET"
cas grossit 0 "$CR" "$G" ok "$COURSE_GROSSIT"
cas lsremote 14 "$CR" "$G" ok true PATH="$S/env/lsremote:$PATH"
cas findko 14 "$CR" "$G" ok true PATH="$S/env/findko:$PATH"
cas findmuet 15 "$CR" "$G" ok "$COURSE_GROS" PATH="$S/env/findmuet:$PATH"
cas cpko 15 "$CR" "$G" ok "$DEBUT" PATH="$S/env/cpko:$PATH"
cas index 15 "$CR" "$G" ok "$COURSE_INDEX"
cas etat 15 "$CR" "$G" ok "$COURSE_ETAT"
echo "  journaux des cas poussee, finale, crochet, grossit, lsremote, findko, findmuet, cpko, index, etat :"
for n in poussee finale crochet grossit lsremote findko findmuet cpko index etat; do grep -h "AMORCE" "$S/journal-$n.txt" | sed "s/^/    [$n] /"; done
sans_pousse_apres crochet "git commit impossible"
sans_pousse_apres lsremote "tete distante"
sans_pousse_apres findko "recherche des fichiers de plus de 95 Mo impossible"
sans_pousse_apres findmuet "fichier indexe de plus de 95 Mo"
sans_pousse_apres cpko "copie de diag impossible"
sans_pousse_apres index "git add impossible"
sans_pousse_apres etat "ecriture de l'etat impossible"
nb=$(git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-crochet | grep -c brut-2.json)
echo "  crochet : brut-2.json sur la branche : $nb (attendu 0)"; [ "$nb" -eq 0 ] || ecart "crochet : brut-2.json poussé"
tg=$(git -C "$S/distant.git" cat-file -s "calcul/essai-grossit:diag/r-grossit/g.bin" 2>&1)
echo "  grossit : taille de g.bin à la tête de la branche : $tg (attendu 1048576)"; [ "$tg" = 1048576 ] || ecart "grossit : taille $tg"
ef=$(git -C "$S/distant.git" show calcul/essai-grossit:etat-neuron-lens-volet-a.txt | grep '^exclus_fichiers=')
echo "  grossit : $ef (attendu exclus_fichiers=diag/r-grossit/g.bin)"; [ "$ef" = "exclus_fichiers=diag/r-grossit/g.bin" ] || ecart "grossit : $ef"
nfm=$(git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-findmuet 2>/dev/null | grep -c gros-96Mio.bin)
echo "  findmuet : fichier de 96 Mio sur la branche : $nfm (attendu 0)"; [ "$nfm" -eq 0 ] || ecart "findmuet : fichier de 96 Mio poussé"
( cd "$S/r/depot" && env GH_TOKEN="$GH_TOKEN" "$VENV/bin/python" -m pytest -q -p no:cacheprovider "$S/sans_jeton_test.py" > "$S/journal-sonde-jeton.txt" 2>&1 )
cs=$?
echo "ARTEFACT de la sonde « sans jeton » jouée avec le jeton présent : code=$cs (attendu : non nul) ; $(tail -1 "$S/journal-sonde-jeton.txt")"
[ "$cs" -ne 0 ] || ecart "sonde sans jeton : n'échoue pas avec le jeton présent"
# balayage : formes, témoins positifs, fichiers puis objets git décompressés
FORMES="$S/formes.txt"
CONTROLE_IA_GITHUB_TOKEN_2="$GH_TOKEN" PYTHONPATH="$SRC/src" "$VENV/bin/python" -c \
  'import os; from controle_ia.neuron_lens.suivi_vast_v4 import formes; print("\n".join(formes(os.environ["CONTROLE_IA_GITHUB_TOKEN_2"])))' > "$FORMES" || ecart "formes non calculées"
nf=$(wc -l < "$FORMES")
mkdir -p "$S/temoins"; i=0
while IFS= read -r f; do i=$((i + 1)); printf 'temoin %s fin\n' "$f" > "$S/temoins/forme-$i.txt"; done < "$FORMES"
git init -q "$S/temoin-git"; printf 'blob %s\n' "$(sed -n 2p "$FORMES")" > "$S/temoin-git/x"; git -C "$S/temoin-git" add x
git -C "$S/temoin-git" -c user.name=t -c user.email=t@example.invalid commit -q -m "message $(head -1 "$FORMES")"
git -C "$S/temoin-git" gc -q
balayer_fichiers() { grep -rlF --binary-files=text -f "$FORMES" "$@"; local c=$?; [ "$c" -le 1 ] || ecart "grep code $c sur $*"; }
objets() {  # dépôt → « objets_lus lignes_detectees » ; erreur de git = écart
  local b c
  b=$(git -C "$1" cat-file --batch-all-objects --batch-check 2> "$S/erreur-git.txt" | wc -l)
  [ -s "$S/erreur-git.txt" ] && ecart "git cat-file sur $1 : $(head -1 "$S/erreur-git.txt")"
  c=$(git -C "$1" cat-file --batch-all-objects --batch 2>/dev/null | grep -caF -f "$FORMES")
  echo "$b $c"
}
nt=$(balayer_fichiers "$S/temoins" | wc -l)
n=$(balayer_fichiers "$S"/m-* "$S/distant.git" "$S"/journal-*.txt | wc -l)
read -r ot nto < <(objets "$S/temoin-git")
npk=$(ls "$S/temoin-git/.git/objects/pack/"*.pack 2>/dev/null | wc -l)
no=0; nd=0; vides=0
for g in "$S/distant.git" "$S"/m-*/depot; do
  nd=$((nd + 1)); read -r b k < <(objets "$g"); no=$((no + k)); [ "$b" -gt 0 ] || vides=$((vides + 1))
done
echo "TEMOINS du balayage : $nt fichier(s) témoin(s) détecté(s) sur $nf (attendu $nf) ; dépôt témoin empaqueté ($npk paquet(s), $ot objet(s) lus) : $nto ligne(s) détectée(s) (attendu ≥ 2 : blob et message)"
[ "$nt" -eq "$nf" ] && [ "$nto" -ge 2 ] && [ "$npk" -ge 1 ] || ecart "témoins du balayage"
echo "BALAYAGE du jeton factice ($nf formes ; pour ce jeton, brute = adresse) : fichiers (disques des machines d'essai, dépôt distant, journaux) : $n fichier(s) ; objets git décompressés de $nd dépôt(s) (distant et clones ; dépôts sans objet lu : $vides) : $no ligne(s)"
[ "$n" -eq 0 ] && [ "$no" -eq 0 ] && [ "$vides" -eq 0 ] || ecart "balayage"
ECARTS=$(wc -l < "$ECARTS_F")
echo "VERDICT de l'essai : $([ "$ECARTS" -eq 0 ] && echo "conforme, 0 écart" || echo "NON conforme, $ECARTS écart(s) : $(tr '\n' ';' < "$ECARTS_F")")"
