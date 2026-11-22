#!/usr/bin/env bash
# Essai à blanc (sans location) de l'amorce v4 du réajustement de nos lentilles (lecture par lentille neuronale) — v3.
# v3 (2026-11-22) = essai v2 (`essai_a_blanc_amorce_neuron_lens_b_beta_v2.sh`, `db50aaaf…`, gardé) changé seulement en : dépôt réduit v4,
# amorce v4, faux lanceur aux étapes du lanceur v4 (audits exceptés : 27 étapes), étapes « jeton » et en ligne de la v4 (copies
# comprises), commandes `inventaire` et `cloture` du faux lanceur, GO fictif bien formé, VARIANTE=B, dépôt de rangement fictif ; et ces
# cas neufs : (c) clé gardée — présente à la clôture, après toutes les étapes ; les quatorze formes des deux secrets injectées à
# l'étape du croquis (après les copies, quand l'amorce v3 aurait retiré la clé) et refusées par le balayage ; (l) inventaire poussé à
# chaque étape — chaque inventaire de course dans son propre commit poussé ; clôture en échec — dernière ligne « COPIE EN ECHEC »,
# code 23 ; gardes d'entrée neuves (VARIANTE, DEPOT_RANGEMENT : code 17) ; borne d'installation (le cas « pip » garde TIMEOUT_PIP_S=1).
# Non couverts, déclarés : le code 18 (vrai pip) ; le vrai lanceur, le vrai transport du rangement, la vraie plateforme de modèles.
# Usage : bash scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v3.sh <COMMIT_SOURCE> <dossier neuf>
set -uo pipefail
SRC=$(cd "$(dirname "$0")/.." && pwd)
C=$(git -C "$SRC" rev-parse "$1") || exit 2; S=$2
REDUIT=scripts/depot_reduit_neuron_lens_b_beta_v4.py
GO_FICTIF=GO-2026-11-23-99
[ -e "$S" ] && { echo "dossier existant"; exit 2; }
mkdir -p "$S"
ECARTS_F="$S/ecarts.txt"; : > "$ECARTS_F"
ecart() { echo "$*" >> "$ECARTS_F"; echo "  ÉCART : $*" >&2; }
VENV="$SRC/.venv"
"$VENV/bin/python" "$SRC/$REDUIT" "$C" "$S/r" > "$S/rapport-reduit.txt" || exit 3
champ() { python3 -c "import json,sys;print(json.load(open(sys.argv[1]))[sys.argv[2]])" "$S/r/rapport.json" "$1"; }
CR=$(champ commit_reduit)
AMORCE=scripts/amorce_neuron_lens_b_beta_v4.sh
[ -f "$S/r/depot/$AMORCE" ] || { echo "amorce v4 absente de l'arbre réduit"; exit 3; }
BR=course/neuron-lens-reajustement-reduit-essai
git init -q --bare "$S/distant.git" || exit 3
git -C "$S/r/depot" push -q "$S/distant.git" "course:refs/heads/$BR" || exit 3
export GH_TOKEN=ghp_facticeABCDEF0123456789abcdefXYZ
export HF_TOKEN=hf_facticeZYXWVU9876543210zyxwvuABC
unset HUGGING_FACE_HUB_TOKEN
# faux lanceur : mêmes étapes, même ordre, même environnement demandé que le vrai (b_beta_lancer_v4), plus `inventaire` et `cloture`
cat > "$S/faux-lanceur.sh" <<'EOF'
#!/usr/bin/env bash
set -u
ETAPES="preparer materiel telecharger-tokeniseur b0 telecharger-poids corpus-ajustement partie2-b0 banc ajustement-R export copie-R ajustement-S copie-S croquis corpus-activations comptes-jetons partie2-corpus lens-compare fumee passe pilotes measure score grandeurs reads declencheurs verdicts"
JETON=" telecharger-tokeniseur telecharger-poids copie-R copie-S "; EN_LIGNE=" preparer telecharger-tokeniseur telecharger-poids corpus-ajustement corpus-activations copie-R copie-S "
D="diag/$RUN_ID"
trace() { printf '%s HF_TOKEN=%s HUGGING=%s GH=%s OFFLINE=%s GO=%s VARIANTE=%s DEPOT=%s\n' "$1" "${HF_TOKEN:+present}" \
  "${HUGGING_FACE_HUB_TOKEN:+present}" "${GH_TOKEN:+present}" "${HF_HUB_OFFLINE:-}" "${GO_ID:-}" "${VARIANTE:-}" "${DEPOT_RANGEMENT:-}" >> "$2"; }
inventaire() {
  [ -d "runs/$RUN_ID" ] || return 0
  mkdir -p "$D/inventaire"; local n; n=$(ls "$D/inventaire" | grep -c '^inventaire-') ; n=$((n + 1))
  printf '{"numero": %d, "clos": %s, "etapes_faites": "%s"}\n' "$n" "$1" "$(ls "$D" | grep -c '^b-beta-')" > "$D/inventaire/inventaire-$(printf %03d "$n").json"
}
case "$1" in
  suite)
    for e in $ETAPES; do
      if [ ! -e "$D/b-beta-$e.json" ]; then
        c=sans-jeton; [[ "$JETON" == *" $e "* ]] && c=jeton; r=hors-ligne; [[ "$EN_LIGNE" == *" $e "* ]] && r=en-ligne
        echo "$e $c $r"; exit 0
      fi
    done
    echo fin ;;
  inventaire)
    trace inventaire "$APPELS_INV"; inventaire false ;;
  cloture)
    trace cloture "$APPELS_INV"; inventaire true; exit "${FAUX_CLOTURE_CODE:-0}" ;;
  jouer)
    e=$3
    trace "$e" "$APPELS"
    mkdir -p "$D/journaux" "runs/$RUN_ID"
    [ "$e" = "${FAUX_ECHEC_ETAPE:-}" ] && { echo '{"arret": 1}' > "$D/arret-$e-1.json"; exit 1; }
    [ "$e" = "${FAUX_FORME_ETAPE:-}" ] && printf 'journal %s fin\n' "$FAUX_FORME" > "$D/journaux/$e.log"
    [ "$e" = "${FAUX_SOMMEIL_ETAPE:-}" ] && [ ! -e "$D/deja-dormi-$e" ] && { : > "$D/deja-dormi-$e"; sleep 60; }
    printf '{"etape": "%s"}\n' "$e" > "$D/b-beta-$e.json"
    sleep 0.2 ;;
esac
EOF
chmod 755 "$S/faux-lanceur.sh"
VRAIES=$(cd "$S/r/depot" && PYTHONPATH=src "$VENV/bin/python" -c 'from controle_ia.neuron_lens import b_beta_lancer_v4 as b; print(" ".join(e for e in b.ETAPES if e not in b.AUDITS_ETAPES)); print(" ".join(sorted(b.JETON))); print(" ".join(sorted(b.EN_LIGNE)))')
FAUSSES=$(grep -m1 '^ETAPES=' "$S/faux-lanceur.sh" | cut -d'"' -f2)
[ "$(printf '%s\n' "$VRAIES" | sed -n 1p)" = "$FAUSSES" ] && echo "  faux lanceur : étapes égales à celles du lanceur v4 (audits exceptés)" || ecart "faux lanceur : étapes $FAUSSES ≠ $VRAIES"
FJ=$(grep -m1 '^JETON=' "$S/faux-lanceur.sh" | cut -d'"' -f2 | xargs -n1 | sort | xargs)
FL=$(grep -m1 'EN_LIGNE=' "$S/faux-lanceur.sh" | sed 's/.*EN_LIGNE="//' | cut -d'"' -f1 | xargs -n1 | sort | xargs)
[ "$(printf '%s\n' "$VRAIES" | sed -n 2p)" = "$FJ" ] && [ "$(printf '%s\n' "$VRAIES" | sed -n 3p)" = "$FL" ] \
  && echo "  faux lanceur : étapes « jeton » et en ligne égales à celles du lanceur v4" || ecart "faux lanceur : jeton ou en ligne différents"
printf 'import pytest\n@pytest.mark.skip\ndef test_x():\n    pass\n' > "$S/saute_test.py"
REELS="tests/test_neuron_lens_verdicts_b_beta_v4.py tests/test_neuron_lens_controles_b_beta_v2.py tests/test_neuron_lens_b_beta_lancer_v4.py tests/test_neuron_lens_etapes_b_beta_v6.py tests/test_neuron_lens_montage_b_beta_v4.py tests/test_neuron_lens_grandeurs_b_alpha_v1.py tests/test_neuron_lens_verdicts_b_alpha_v3.py tests/test_neuron_lens_balayage_arbre_v1.py"
G=tests/test_neuron_lens_balayage_arbre_v1.py
cloner() {  # dossier machine ; url
  git -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)" \
    clone -q --depth 1 --single-branch --branch "$BR" "file://$S/distant.git" "$1/depot" || ecart "clone de $1 impossible"
}
lancer() {  # nom dossier attendu essais [variables…] ; joue l'amorce dans le dossier machine
  local nom=$1 d=$2 attendu=$3 essais=$4; shift 4
  (cd "$d" && env COMMIT_REDUIT="$CR" GO_ID="$GO_FICTIF" VARIANTE=B DEPOT_RANGEMENT=compte-essai/rangement-essai MODE_JOUET=1 \
     VENV_JOUET="$VENV" PERIODE_POUSSE_S=2 RUN_ID="20261123-100000-neuron-lens-b-beta" BRANCHE_RESULTATS="calcul/essai-$nom" \
     ESSAIS="$essais" COMMANDE_LANCEUR="bash $S/faux-lanceur.sh \"\$@\"" APPELS="$S/appels-$nom.txt" APPELS_INV="$S/appels-inv-$nom.txt" \
     ESSAIS_POUSSEE_FINALE=2 ATTENTE_POUSSEE_FINALE_S=1 ATTENTE_FIN=0 HF_HOME="$d/hf" "$@" timeout 900 bash "depot/$AMORCE" \
     >> "$S/journal-$nom.txt" 2>&1 < /dev/null)
  local code=$?
  echo "CAS $nom : code=$code (attendu $attendu) ; derniere ligne : $(tail -1 "$S/journal-$nom.txt" | cut -d' ' -f3- | cut -c1-160)"
  [ "$code" = "$attendu" ] || ecart "cas $nom : code $code au lieu de $attendu"
}
cas() { local nom=$1; mkdir -p "$S/m-$nom"; cloner "$S/m-$nom"; lancer "$nom" "$S/m-$nom" "${@:2}"; }
verifier_appels() {  # nom : clé aux seules étapes « jeton », hors-ligne aux étapes « hors-ligne », GH_TOKEN jamais
  local f="$S/appels-$1.txt" l e
  [ -s "$f" ] || { ecart "$1 : aucun appel du lanceur consigné"; return; }
  while read -r l; do
    e=${l%% *}
    case " telecharger-tokeniseur telecharger-poids copie-R copie-S " in
      *" $e "*) [[ "$l" == *"HF_TOKEN=present"* ]] || ecart "$1 : $e sans HF_TOKEN" ;;
      *) [[ "$l" == *"HF_TOKEN= "* ]] || ecart "$1 : HF_TOKEN présent à $e" ;;
    esac
    case " preparer telecharger-tokeniseur telecharger-poids corpus-ajustement corpus-activations copie-R copie-S " in
      *" $e "*) [[ "$l" == *"OFFLINE= "* ]] || ecart "$1 : HF_HUB_OFFLINE posé à $e" ;;
      *) [[ "$l" == *"OFFLINE=1 "* ]] || ecart "$1 : HF_HUB_OFFLINE absent à $e" ;;
    esac
    [[ "$l" == *"GH= "* && "$l" == *"HUGGING= "* && "$l" == *"GO=$GO_FICTIF "* && "$l" == *"VARIANTE=B "* \
       && "$l" == *"DEPOT=compte-essai/rangement-essai"* ]] || ecart "$1 : GH_TOKEN, HUGGING_FACE_HUB_TOKEN, GO_ID, VARIANTE ou dépôt inattendu à $e"
  done < "$f"
  f="$S/appels-inv-$1.txt"
  [ -s "$f" ] || { ecart "$1 : aucun inventaire consigné"; return; }
  while read -r l; do
    case "${l%% *}" in
      inventaire) [[ "$l" == *"HF_TOKEN= "* && "$l" == *"OFFLINE=1 "* && "$l" == *"GH= "* ]] || ecart "$1 : inventaire avec la clé, en ligne ou avec GH_TOKEN" ;;
      cloture) [[ "$l" == *"HF_TOKEN=present"* && "$l" == *"OFFLINE= "* && "$l" == *"GH= "* ]] || ecart "$1 : clôture sans la clé, hors ligne ou avec GH_TOKEN" ;;
      *) ecart "$1 : commande inattendue : $l" ;;
    esac
  done < "$f"
}
echo "ESSAI A BLANC réajustement de nos lentilles v3 de $AMORCE ; commit source $C ; commit reduit $CR ; liste $(champ liste_sha256) ; paquet $(champ paquet_sha256) ; $(champ n_fichiers) fichiers ; $(date -u +%FT%TZ)"

# 1. nominal, puis relance après l'état final
NE=$(printf '%s\n' "$VRAIES" | sed -n 1p | wc -w)
cas nominal 0 "$REELS"
verifier_appels nominal
n=$(wc -l < "$S/appels-nominal.txt"); echo "  nominal : $n appels du lanceur (attendu $NE)"; [ "$n" -eq "$NE" ] || ecart "nominal : $n appels"
grep -q "HF_TOKEN retire de la course" "$S/journal-nominal.txt" && ecart "nominal : la clé a été retirée (v3)"
grep -q "^cloture HF_TOKEN=present" "$S/appels-inv-nominal.txt" && echo "  nominal : clé gardée jusqu'à la clôture, après toutes les étapes" || ecart "nominal : clé absente à la clôture"
ni=$(grep -c "^inventaire " "$S/appels-inv-nominal.txt"); echo "  nominal : $ni inventaires demandés (attendu $((NE + 1)) : un par étape et un à la fin)"
[ "$ni" -eq $((NE + 1)) ] || ecart "nominal : $ni inventaires"
grep -q "passed" "$S/journal-nominal.txt" && echo "  nominal : essais réels : $(grep -E '[0-9]+ passed' "$S/journal-nominal.txt" | tail -1)" || ecart "nominal : essais réels absents"
[ -s "$S/m-nominal/fin-b-beta.txt" ] && echo "  nominal : état final écrit : $(cat "$S/m-nominal/fin-b-beta.txt")" || ecart "nominal : état final absent"
ET=$(git -C "$S/distant.git" show calcul/essai-nominal:etat-neuron-lens-b-beta.txt 2>/dev/null)
echo "  nominal : état poussé : $(printf '%s' "$ET" | grep -E '^(etat|location_s)=' | tr '\n' ' ')"
printf '%s' "$ET" | grep -q '^etapes_faites=.*verdicts' || ecart "nominal : étapes faites absentes de l'état poussé"
RD="diag/20261123-100000-neuron-lens-b-beta"
nb=$(git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-nominal | grep -c "^$RD/b-beta-")
echo "  nominal : résultats d'étape sur la branche : $nb (attendu $NE)"; [ "$nb" -eq "$NE" ] || ecart "nominal : $nb résultats poussés"
# (l) chaque inventaire de course (un par étape) dans son propre commit poussé, avec le résultat de son étape
git -C "$S/distant.git" log --format='C %H' --name-only --diff-filter=A calcul/essai-nominal > "$S/journal-commits-nominal.txt"
nc=$(awk -v rd="$RD/inventaire/inventaire-" '/^C /{c=$2} index($0, rd)==1 {n=substr($0, length(rd)+1, 3)+0; if (n>=1 && n<='"$NE"') print c}' \
     "$S/journal-commits-nominal.txt" | sort -u | wc -l)
echo "  nominal : inventaires 1 à $NE poussés dans $nc commits distincts (attendu $NE)"; [ "$nc" -eq "$NE" ] || ecart "nominal : inventaires poussés ensemble ($nc commits)"
clos=$(git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-nominal | grep -c "^$RD/inventaire/inventaire-")
git -C "$S/distant.git" show "calcul/essai-nominal:$RD/inventaire/inventaire-$(printf %03d "$clos").json" 2>/dev/null | grep -q '"clos": true' \
  && echo "  nominal : dernier inventaire poussé clos ($clos inventaires)" || ecart "nominal : dernier inventaire poussé non clos"
: > "$S/appels-nominal-relance.txt"
lancer nominal-relance "$S/m-nominal" 0 "$REELS" APPELS="$S/appels-nominal-relance.txt" APPELS_INV="$S/appels-inv-nominal-relance.txt"
grep -q "etat final deja atteint" "$S/journal-nominal-relance.txt" && echo "  relance : attente sans calcul" || ecart "relance : état final non relu"
[ -s "$S/appels-nominal-relance.txt" ] && ecart "relance : le lanceur a été appelé" || echo "  relance : aucun appel du lanceur"

# 2. reprise : machine tuée pendant `passe`, relancée avec la clé de nouveau dans l'environnement
mkdir -p "$S/m-reprise"; cloner "$S/m-reprise"
(cd "$S/m-reprise" || exit 1
 setsid env COMMIT_REDUIT="$CR" GO_ID="$GO_FICTIF" VARIANTE=B DEPOT_RANGEMENT=compte-essai/rangement-essai MODE_JOUET=1 VENV_JOUET="$VENV" \
   PERIODE_POUSSE_S=2 RUN_ID="20261123-100000-neuron-lens-b-beta" BRANCHE_RESULTATS="calcul/essai-reprise" ESSAIS="$G" \
   COMMANDE_LANCEUR="bash $S/faux-lanceur.sh \"\$@\"" APPELS="$S/appels-reprise.txt" APPELS_INV="$S/appels-inv-reprise.txt" \
   FAUX_SOMMEIL_ETAPE=passe ATTENTE_FIN=0 HF_HOME="$S/m-reprise/hf" bash "depot/$AMORCE" > "$S/journal-reprise.txt" 2>&1 < /dev/null &
 echo $! > "$S/pid-reprise")
for _ in $(seq 1 180); do grep -q "etape : passe" "$S/journal-reprise.txt" 2>/dev/null && break; sleep 1; done
PG=$(cat "$S/pid-reprise"); sleep 1
kill -9 -- -"$PG" || ecart "reprise : groupe $PG introuvable (machine non tuée)"; sleep 1
vivants() { ps -eo pgid=,stat= | awk -v g="$PG" '$1 == g && $2 !~ /^Z/' | wc -l; }
for _ in $(seq 1 10); do [ "$(vivants)" -eq 0 ] && break; sleep 1; done
[ "$(vivants)" -eq 0 ] || ecart "reprise : groupe $PG encore vivant ($(vivants) processus)"
grep -q "etape : passe" "$S/journal-reprise.txt" && echo "  reprise : machine tuée pendant passe (groupe $PG)" || ecart "reprise : passe jamais atteinte"
grep -q "course terminee" "$S/journal-reprise.txt" && ecart "reprise : la première amorce a fini malgré l'arrêt"
n1=$(wc -l < "$S/appels-reprise.txt")
lancer reprise "$S/m-reprise" 0 "$G" APPELS="$S/appels-reprise.txt" APPELS_INV="$S/appels-inv-reprise.txt"
verifier_appels reprise
grep -q "reprise : course" "$S/journal-reprise.txt" && echo "  reprise : reprise journalisée" || ecart "reprise : reprise non journalisée"
apres=$(tail -n +"$((n1 + 1))" "$S/appels-reprise.txt" | cut -d' ' -f1 | tr '\n' ' ')
echo "  reprise : appels après la relance : $apres"
[ "$apres" = "passe pilotes measure score grandeurs reads declencheurs verdicts " ] || ecart "reprise : étapes rejouées inattendues : $apres"
n=$(grep -c "^passe " "$S/appels-reprise.txt"); [ "$n" -eq 2 ] || ecart "reprise : passe jouée $n fois (attendu 2)"
grep -c "essais passes" "$S/journal-reprise.txt" | grep -qx 1 && echo "  reprise : essais non refaits" || ecart "reprise : essais refaits"

# 3. étape en échec ; clôture en échec ; formes de secret écrites après les copies (clé gardée : refusées par le balayage)
cas echec 20 "$G" FAUX_ECHEC_ETAPE=measure
grep -q "etape measure en echec" "$S/journal-echec.txt" || ecart "échec : non journalisé"
git -C "$S/distant.git" show calcul/essai-echec:etat-neuron-lens-b-beta.txt 2>/dev/null | grep -q '^etat=arret code 20' && echo "  échec : état poussé « arret code 20 »" || ecart "échec : état final non poussé"
grep -q "^cloture HF_TOKEN=present" "$S/appels-inv-echec.txt" && echo "  échec : clôture jouée, clé présente" || ecart "échec : clôture absente"
cas copie-en-echec 23 "$G" FAUX_CLOTURE_CODE=3
tail -1 "$S/journal-copie-en-echec.txt" | grep -q "COPIE EN ECHEC" && echo "  copie en échec : dernière ligne « COPIE EN ECHEC » (pas sans la mère)" || ecart "copie en échec : dernière ligne"
git -C "$S/distant.git" show calcul/essai-copie-en-echec:etat-neuron-lens-b-beta.txt 2>/dev/null | grep -q 'copie en echec a la cloture' \
  && echo "  copie en échec : état poussé le dit" || ecart "copie en échec : état poussé muet"
FORMES_ESSAI="$S/formes-injectees.txt"
"$VENV/bin/python" - "$GH_TOKEN" "$HF_TOKEN" > "$FORMES_ESSAI" <<'EOF'
import base64, sys
from urllib.parse import quote
for nom, v in (("gh", sys.argv[1]), ("hf", sys.argv[2])):
    h = "x-access-token:" + v
    f = {"brute": v, "adresse": quote(v, safe="") + "%2F", "b64": base64.b64encode(v.encode()).decode(),
         "b64-decale": base64.b64encode(b"ab" + v.encode() + b"cd").decode(), "b64-url": base64.urlsafe_b64encode(b"z" + v.encode()).decode(),
         "entete": base64.b64encode(h.encode()).decode(), "entete-decale": base64.b64encode(b"Basic " + h.encode()).decode()}
    for k, x in f.items():
        print(f"{nom}-{k} {x}")
EOF
nfo=0
while read -r nomf forme; do
  nfo=$((nfo + 1))
  # forme écrite au croquis ; la course est arrêtée à l'étape suivante (code 20) pour borner la durée : chaque poussée est refusée
  cas "forme-$nomf" 20 "$G" FAUX_FORME_ETAPE=croquis FAUX_FORME="$forme" FAUX_ECHEC_ETAPE=corpus-activations > /dev/null
  t=$(tail -1 "$S/journal-forme-$nomf.txt" | cut -d' ' -f3- | cut -c1-80)
  [[ "$t" == *"POUSSEE FINALE EN ECHEC"* ]] || ecart "forme $nomf : dernière ligne inattendue : $t"
  r=$(grep -c "balayage : poussee refusee" "$S/journal-forme-$nomf.txt")
  o=$(git -C "$S/distant.git" cat-file --batch-all-objects --batch 2>/dev/null | grep -caF -- "$forme")
  echo "CAS forme $nomf (étape du croquis, après les copies) : refus du balayage $r fois ; forme dans les objets du dépôt distant : $o (attendu 0) ; $t"
  [ "$r" -ge 1 ] && [ "$o" -eq 0 ] || ecart "forme $nomf : refus $r, objets $o"
  grep -qF -- "$forme" "$S/journal-forme-$nomf.txt" && ecart "forme $nomf : écrite dans le journal de l'amorce"
done < "$FORMES_ESSAI"
[ "$nfo" -eq 14 ] && echo "  formes : 14 rejouées à l'étape du croquis, clé présente" || ecart "formes : $nfo au lieu de 14"

# 4. gardes d'entrée
cas commit 10 "$G" COMMIT_REDUIT=0000000000000000000000000000000000000000
mkdir -p "$S/m-arbre"; cloner "$S/m-arbre"; echo x > "$S/m-arbre/depot/non-suivi.txt"; lancer arbre "$S/m-arbre" 10 "$G"
cas runid 17 "$G" RUN_ID=20261123-neuron-lens
cas variante 17 "$G" VARIANTE=C
cas depot 17 "$G" DEPOT_RANGEMENT=sans-barre
cas commande 13 "$G" MODE_JOUET=0
cas pip 16 "$G" MODE_JOUET=0 COMMANDE_LANCEUR= TIMEOUT_PIP_S=1 PYTHON_ATTENDU="$(python3 -c 'import platform; print(platform.python_version())')"
cas python 19 "$G" MODE_JOUET=0 COMMANDE_LANCEUR= PYTHON_ATTENDU=0.0.0
grep -q "au lieu de 0.0.0" "$S/journal-python.txt" || ecart "python : message absent"
grep -q "installation de l'environnement" "$S/journal-python.txt" && ecart "python : pip lancé malgré la version"
grep -q "environnement non installe" "$S/journal-pip.txt" || ecart "pip : message absent"
grep -q 'TIMEOUT_PIP=${TIMEOUT_PIP_S:-7200}' "$S/r/depot/$AMORCE" && echo "  borne d'installation par défaut : 7 200 s" || ecart "borne d'installation"
mkdir -p "$S/m-poussee"; cloner "$S/m-poussee"; git -C "$S/m-poussee/depot" remote set-url origin "file://$S/inexistant.git"
lancer poussee "$S/m-poussee" 14 "$G"
cas essai 12 "$G tests/inexistant.py"
cas saute 12 "$G $S/saute_test.py"

# 4 ter. garde de carte : interprète factice et nvidia-smi factice
mkdir -p "$S/venv-carte/bin" "$S/outils"
cat > "$S/venv-carte/bin/python" <<EOF2
#!/usr/bin/env bash
if [ "\${1:-}" = "-c" ] && [[ "\${2:-}" == *torch* ]]; then
  if [[ "\$2" == *is_available* ]]; then exit 0; fi
  if [ "\${FAUSSE_CARTE_TORCH:-}" = ILLISIBLE ]; then echo "erreur" >&2; exit 1; fi
  echo "\${FAUSSE_CARTE_TORCH:-NVIDIA H100 80GB HBM3}"; exit 0
fi
exec "$VENV/bin/python" "\$@"
EOF2
chmod 755 "$S/venv-carte/bin/python"
printf '#!/usr/bin/env bash\necho "$FAUSSE_CARTE_SMI"\n' > "$S/outils/faux-smi"; chmod 755 "$S/outils/faux-smi"
CARTE_VARS=(VENV_JOUET="$S/venv-carte" EXIGER_CARTE_JOUET=1 CARTE_ATTENDUE=HBM3 OUTIL_NVIDIA_SMI="$S/outils/faux-smi")
cas carte-saine 0 "$G" "${CARTE_VARS[@]}" FAUSSE_CARTE_SMI="NVIDIA H100 80GB HBM3"
grep -q "carte (nvidia-smi) : NVIDIA H100 80GB HBM3" "$S/journal-carte-saine.txt" && grep -q "carte : NVIDIA H100 80GB HBM3" "$S/journal-carte-saine.txt" \
  && echo "  carte saine : vue par nvidia-smi et par torch" || ecart "carte saine : non journalisée deux fois"
for art in "NVIDIA H100 PCIe" "NVIDIA A100-SXM4-80GB" "NVIDIA H200"; do
  nom=carte-smi-$(printf '%s' "$art" | tr -c 'A-Za-z0-9' '-')
  cas "$nom" 11 "$G" "${CARTE_VARS[@]}" FAUSSE_CARTE_SMI="$art"
  grep -q "carte inattendue : $art" "$S/journal-$nom.txt" || ecart "$nom : carte inattendue non journalisée"
  grep -q "installation de l'environnement\|essais passes" "$S/journal-$nom.txt" && ecart "$nom : la course a continué après la carte"
done
cas carte-torch-autre 11 "$G" "${CARTE_VARS[@]}" FAUSSE_CARTE_SMI="NVIDIA H100 80GB HBM3" FAUSSE_CARTE_TORCH="NVIDIA H100 PCIe"
grep -q "carte inattendue : NVIDIA H100 PCIe" "$S/journal-carte-torch-autre.txt" || ecart "carte vue par torch : non prise en défaut"
cas carte-illisible 11 "$G" "${CARTE_VARS[@]}" FAUSSE_CARTE_SMI="NVIDIA H100 80GB HBM3" FAUSSE_CARTE_TORCH=ILLISIBLE
grep -q "nom de la carte illisible" "$S/journal-carte-illisible.txt" || ecart "carte illisible : non prise en défaut"
cas carte-sans-smi 0 "$G" "${CARTE_VARS[@]}" OUTIL_NVIDIA_SMI="$S/outils/inexistant"
grep -q "nvidia-smi absent" "$S/journal-carte-sans-smi.txt" || ecart "nvidia-smi absent : non journalisé"

# 5. balayage final des deux jetons : formes du suivi v6 ; témoins positifs ; dépôt distant (objets), journaux, disques sans forme injectée
FORMES="$S/formes-suivi.txt"
"$VENV/bin/python" -c 'import sys; sys.path.insert(0, sys.argv[1]); from controle_ia.neuron_lens.suivi_vast_v6 import formes
print("\n".join(sorted(set(formes(sys.argv[2])) | set(formes(sys.argv[3])))))' "$SRC/src" "$GH_TOKEN" "$HF_TOKEN" > "$FORMES" || ecart "formes non calculées"
nf=$(wc -l < "$FORMES")
mkdir -p "$S/temoins"; i=0
while IFS= read -r f; do i=$((i + 1)); printf 'temoin %s fin\n' "$f" > "$S/temoins/forme-$i.txt"; done < "$FORMES"
nt=$(grep -rlF --binary-files=text -f "$FORMES" "$S/temoins" | wc -l)
propres=("$S/distant.git" "$S"/journal-*.txt "$S"/appels-*.txt "$S/m-nominal" "$S/m-reprise" "$S/m-echec" "$S/m-copie-en-echec" "$S/m-commit" \
         "$S/m-arbre" "$S/m-runid" "$S/m-variante" "$S/m-depot" "$S/m-commande" "$S/m-pip" "$S/m-python" "$S/m-poussee" "$S/m-essai" "$S/m-saute" "$S"/m-carte-*)
nfi=$(grep -rlF --binary-files=text -f "$FORMES" "${propres[@]}" 2>/dev/null | grep -v '/m-forme-' | wc -l)
b=$(git -C "$S/distant.git" cat-file --batch-all-objects --batch-check | wc -l)
no=$(git -C "$S/distant.git" cat-file --batch-all-objects --batch 2>/dev/null | grep -caF -f "$FORMES")
echo "TEMOINS du balayage : $nt fichier(s) détecté(s) sur $nf (attendu $nf)"
[ "$nt" -eq "$nf" ] || ecart "témoins du balayage"
echo "BALAYAGE des deux jetons ($nf formes) : fichiers $nfi (attendu 0) ; objets du dépôt distant : $b lus, $no ligne(s) (attendu 0)"
[ "$nfi" -eq 0 ] && [ "$no" -eq 0 ] && [ "$b" -gt 0 ] || ecart "balayage final"
ps -eo pid,args | grep -F "$S/" | grep -v grep > "$S/restes.txt"
[ -s "$S/restes.txt" ] && ecart "processus restants : $(wc -l < "$S/restes.txt")"
echo "  processus restants : $(wc -l < "$S/restes.txt") (attendu 0)"
ECARTS=$(wc -l < "$ECARTS_F")
echo "VERDICT de l'essai : $([ "$ECARTS" -eq 0 ] && echo "conforme, 0 écart" || echo "NON conforme, $ECARTS écart(s) : $(tr '\n' ';' < "$ECARTS_F")")"
