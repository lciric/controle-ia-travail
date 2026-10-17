#!/bin/bash
# Bancs de la garde pre-push v2 (R5) : cas sains et artefacts, poussées réelles vers un dépôt nu jetable.
# Usage : bash essais-pre-push-v2.sh <garde pre-push-v2.sh> <dossier neuf>
set -u
G=$(readlink -f "$1"); T="$2"
[ -f "$G" ] || { echo "garde introuvable : $1"; exit 2; }
[ -e "$T" ] && { echo "dossier existant : $T (R12)"; exit 2; }
mkdir -p "$T/lciric" && cd "$T" || exit 2
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_COUNT=0
git init -q --bare -b main lciric/controle-ia-travail.git || exit 2
git init -q --bare -b main lciric/controle-ia.git || exit 2
git clone -q "$T/lciric/controle-ia-travail.git" w 2>/dev/null || exit 2
cd w || exit 2
git config user.name essai; git config user.email essai@exemple.invalid; git config commit.gpgsign false
cp "$G" .git/hooks/pre-push && chmod +x .git/hooks/pre-push
echo base > a.txt && git add a.txt && git commit -qm base && git -c core.hooksPath=/dev/null push -q origin main || exit 2
ok=0; ko=0
cas() { # cas <nom> <code attendu> <commande…>
  nom="$1"; att="$2"; shift 2
  sortie=$( { eval "$@"; } 2>&1 ); code=$?
  [ "$code" -ne 0 ] && code=1
  if [ "$code" = "$att" ]; then r=OK; ok=$((ok+1)); else r=KO; ko=$((ko+1)); fi
  motif=$(printf '%s\n' "$sortie" | grep -o 'pre-push : .*' | head -1)
  echo "$r $nom : attendu $att, obtenu $code${motif:+ — $motif}"
}
nouveau() { echo "$1" >> a.txt && git add a.txt && git commit -qm "$1"; }
echo redaction > .git/voie; touch .git/bail-main
nouveau s1; cas S1-main-avec-bail 0 git push -q origin main
cas S2-coord-de-sa-voie 0 git push -q origin HEAD:coord/redaction
rm .git/bail-main
cas S3-branche-de-travail-sans-bail 0 git push -q origin HEAD:redaction/travail
nouveau a1; cas A1-main-sans-bail 1 git push -q origin main
cas A2-coord-autre-voie 1 git push -q origin HEAD:coord/calcul
touch .git/bail-main
git reset -q --hard HEAD~2 && nouveau diverge
cas A3-main-forcee-avec-bail 1 git push -q -f origin main
git fetch -q origin && git reset -q --hard origin/main
cas A4-suppression-coord 1 git push -q origin :coord/redaction
git checkout -q -b r origin/coord/redaction && git reset -q --hard HEAD~1 && nouveau diverge2
cas A5-coord-forcee 1 git push -q -f origin HEAD:coord/redaction
git checkout -q main
cas A6-vers-controle-ia 1 git push -q "$T/lciric/controle-ia.git" main
rm .git/voie
nouveau a7; cas A7-voie-absente 1 git push -q origin main
echo inconnue > .git/voie
cas A8-voie-inconnue 1 git push -q origin main
echo calcul > .git/voie; rm -f .git/bail-main
cas A9-calcul-vers-coord-redaction 1 git push -q origin HEAD:coord/redaction
cas S4-calcul-vers-coord-calcul 0 git push -q origin HEAD:coord/calcul
cas A10-calcul-main-sans-bail 1 git push -q origin main
echo "verdict : $ok OK, $ko KO"
[ "$ko" = 0 ]
