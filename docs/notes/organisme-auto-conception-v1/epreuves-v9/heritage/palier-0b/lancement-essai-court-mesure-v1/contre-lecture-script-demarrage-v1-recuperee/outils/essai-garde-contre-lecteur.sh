#!/bin/bash
# Contre-lecteur, question 2 : éprouve la garde de branche (crochet avant poussée) et la poussée réelle du script, avec des
# artefacts que l'auteur n'a pas joués : étiquette, --all, --mirror, forme courte de la référence, contournement par
# --no-verify (le crochet est local), poussée forcée avec « + » (le crochet ne la refuse pas), et poussée du script (sans
# force) quand l'histoire locale a divergé de celle du distant. Serveur factice relancé sur le distant d'un cas déjà joué,
# arrêté par son identifiant. Rien ne sort de la machine.
# Emploi : essai-garde-contre-lecteur.sh NOM_DU_CAS
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
ICI=$ME/auteur/essais-outils
W=$ME/auteur/travail/cas/$1
V=$W/base/versement
RD=$W/distant/controle-ia-travail.git
B=recuperation/palier-0b-programme-1-essai-3-v1
OUT=$ME/resultats/garde-branche-contre-lecteur-$1.txt
[ ! -e "$OUT" ] || { echo "refus : $OUT existe"; exit 1; }
: > "$OUT"
PORT=$(shuf -i 20000-40000 -n 1)
rm -f "$W/serveur-pret-cl.txt"
/home/user/controle-ia-travail/.venv/bin/python -I "$ICI/serveur-git-factice.py" "$PORT" "$W/distant" "$W/serveur-jeton.txt" \
  "$W/journaux/serveur-cl.txt" "$W/serveur-pret-cl.txt" > /dev/null 2>&1 &
PS=$!
for i in $(seq 1 100); do [ -s "$W/serveur-pret-cl.txt" ] && break; sleep 0.1; done
export GIT_TERMINAL_PROMPT=0 GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
export NO_PROXY="127.0.0.1,localhost${NO_PROXY:+,$NO_PROXY}" no_proxy="127.0.0.1,localhost${no_proxy:+,$no_proxy}"
git -C "$V" config remote.origin.url "http://127.0.0.1:$PORT/controle-ia-travail.git"
tete() { git -C "$RD" rev-parse -q --verify "refs/heads/$B" 2> /dev/null | cut -c1-10; }
refs() { git -C "$RD" for-each-ref --format='%(refname)' | tr '\n' ' '; }
essai() {  # nom, attendu (refus|admis), arguments de git push
  local nom=$1 att=$2; shift 2
  local sortie code rendu garde=non
  sortie=$(git -C "$V" push "$@" 2>&1); code=$?
  rendu=admis; [ $code -ne 0 ] && rendu=refus
  printf '%s' "$sortie" | grep -q "garde : refus" && garde=oui
  echo "$nom : attendu $att ; rendu $rendu (code $code ; message de la garde : $garde) ; $([ "$att" = "$rendu" ] && echo TENU || echo ÉCART)" >> "$OUT"
}
echo "départ : tête de la branche permise $(tete) ; références du distant : $(refs)" >> "$OUT"
git -C "$V" tag essai-cl-etiquette
essai "A1 étiquette vers refs/tags" refus origin refs/tags/essai-cl-etiquette
essai "A2 --all (pousse la branche locale, qui n'est pas la permise)" refus origin --all
essai "A3 --mirror" refus origin --mirror
essai "A4 forme courte HEAD:nom-de-la-branche-permise (sain)" admis origin "HEAD:$B"
echo "après A1-A4 : références du distant : $(refs)" >> "$OUT"
echo "--- artefacts où l'écart est attendu (la garde est un crochet LOCAL) ---" >> "$OUT"
essai "B1 --no-verify vers une autre branche (contournement du crochet)" refus --no-verify origin HEAD:refs/heads/autre-branche-cl
echo "après B1 : références du distant : $(refs)" >> "$OUT"
# divergence : l'histoire locale perd son dernier commit et en reçoit un autre
git -C "$V" reset -q --hard HEAD~1
git -C "$V" commit -q --allow-empty -m "histoire divergente (artefact du contre-lecteur)"
AVANT=$(tete)
essai "C1 poussée du script (sans force) sur histoire divergente" refus origin "HEAD:refs/heads/$B"
echo "après C1 : tête du distant inchangée : $([ "$AVANT" = "$(tete)" ] && echo oui || echo NON)" >> "$OUT"
essai "C2 poussée forcée « + » vers la branche permise (le crochet ne regarde ni la force ni l'ascendance)" refus origin "+HEAD:refs/heads/$B"
echo "après C2 : tête du distant changée (histoire réécrite) : $([ "$AVANT" != "$(tete)" ] && echo OUI || echo non)" >> "$OUT"
# dépôt de lecture : poussée impossible ?
D=$W/base/depot.git
SORTIE_D=$(git -C "$D" push origin refs/heads/main:refs/heads/depot-lu-cl 2>&1); CODE_D=$?
echo "D1 poussée depuis le dépôt de lecture (adresse de poussée invalide) : code $CODE_D (attendu non nul) ; $(printf '%s' "$SORTIE_D" | head -n 1 | cut -c1-100)" >> "$OUT"
echo "occurrences de « push » dans le script de démarrage : $(grep -c 'push' $ME/auteur/demarrage-machine-essai-3-v1.sh) ; lignes d'appel git push : $(grep -n 'git .*push' $ME/auteur/demarrage-machine-essai-3-v1.sh | cut -c1-110 | tr '\n' '|')" >> "$OUT"
kill "$PS"; wait "$PS" 2> /dev/null
cat "$OUT"
