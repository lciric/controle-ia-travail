#!/bin/bash
# v2 : éprouve la garde du versement (crochet avant poussée posé par le script de démarrage v2) sur le dépôt de versement
# d'un cas déjà joué. Artefacts (refus attendus, distant inchangé) : vers main, vers une autre branche, vers un nom
# voisin, effacement de la branche permise, étiquette, poussée forcée d'une histoire réécrite (commit amendé), poussée
# forcée d'une histoire sans lien (commit orphelin). Sain : une poussée descendante vers la branche permise (admise).
# Arrête son serveur par son identifiant.
# Emploi : essai-garde-branche.sh NOM_DU_CAS
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
W=$(dirname "$ICI")/travail/cas/$1
V=$W/base/versement
RD=$W/distant/controle-ia-travail.git
B=recuperation/palier-0b-programme-1-essai-3-v1
OUT=$W/journaux/garde-branche.txt
: > "$OUT"
rm -f "$W/serveur-pret-garde.txt"
# v2 : l'assistant ne rend le jeton qu'à l'hôte du cas (127.0.0.1:PORT d'origine) : le serveur est relancé sur ce port
# (première passe sur un port neuf : toutes les poussées refusées faute de jeton, code 128, garde jamais atteinte)
PORT=$(grep -o '127\.0\.0\.1:[0-9]*' "$W/base/assistant-jeton.sh" | head -n 1 | cut -d: -f2)
/home/user/controle-ia-travail/.venv/bin/python -I "$ICI/serveur-git-factice.py" "$PORT" "$W/distant" "$W/serveur-jeton.txt" \
  "$W/journaux/serveur-garde.txt" "$W/serveur-pret-garde.txt" > /dev/null 2>&1 &
PS=$!
for i in $(seq 1 100); do [ -s "$W/serveur-pret-garde.txt" ] && break; sleep 0.1; done
export GIT_TERMINAL_PROMPT=0 GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
export NO_PROXY="127.0.0.1,localhost${NO_PROXY:+,$NO_PROXY}" no_proxy="127.0.0.1,localhost${no_proxy:+,$no_proxy}"
export GIT_AUTHOR_NAME=essai GIT_AUTHOR_EMAIL=essai@invalid GIT_COMMITTER_NAME=essai GIT_COMMITTER_EMAIL=essai@invalid
git -C "$V" config remote.origin.url "http://127.0.0.1:$PORT/controle-ia-travail.git"
avant() { git -C "$RD" for-each-ref --format='%(refname) %(objectname)' | sort; }
essai() {  # nom, attendu (refus|admis), arguments de git push
  local nom=$1 att=$2; shift 2
  local sortie code
  sortie=$(git -C "$V" push "$@" 2>&1); code=$?
  local rendu=admis; [ $code -ne 0 ] && rendu=refus
  local garde=non; printf '%s' "$sortie" | grep -q "garde : refus" && garde=oui
  echo "$nom : attendu $att ; rendu $rendu (code $code ; message de la garde : $garde) ; $([ "$att" = "$rendu" ] && echo TENU || echo ÉCHEC)" >> "$OUT"
}
A0=$(avant)
# départ propre : le dépôt de versement est remis sur la tête de la branche distante (objet déjà local : poussé d'ici)
# (deuxième passe sans cette remise : le dépôt local était en avance d'un commit, l'« histoire réécrite » descendait
#  encore de la tête distante et fut admise à bon droit ; essai mal construit, refait)
ORIG=$(git -C "$RD" rev-parse "refs/heads/$B")
git -C "$V" reset -q --hard "$ORIG"
essai "vers main" refus origin HEAD:refs/heads/main
essai "vers une autre branche" refus origin HEAD:refs/heads/autre-branche
essai "vers un nom voisin" refus origin "HEAD:refs/heads/$B-bis"
essai "effacement de la branche permise" refus origin ":refs/heads/$B"
essai "étiquette" refus origin HEAD:refs/tags/etiquette
git -C "$V" commit -q --amend --allow-empty -m "histoire réécrite"
essai "forcée, histoire réécrite" refus origin "+HEAD:refs/heads/$B"
echo "histoire réécrite : la tête distante $ORIG est-elle ancêtre du commit poussé ? $(git -C "$V" merge-base --is-ancestor "$ORIG" HEAD && echo oui || echo non) (attendu non)" >> "$OUT"
OR=$(git -C "$V" commit-tree "$(git -C "$V" rev-parse 'HEAD^{tree}')" -m orphelin)
essai "forcée, commit orphelin" refus origin "+$OR:refs/heads/$B"
git -C "$V" reset -q --hard "$ORIG"
A1=$(avant)
echo "distant inchangé par les sept artefacts : $([ "$A0" = "$A1" ] && echo oui || echo NON)" >> "$OUT"
git -C "$V" commit -q --allow-empty -m "essai de la garde : poussée descendante"
essai "descendante vers la branche permise (sain)" admis origin "HEAD:refs/heads/$B"
echo "branche permise sur le distant = tête du versement : $([ "$(git -C "$RD" rev-parse "refs/heads/$B")" = "$(git -C "$V" rev-parse HEAD)" ] && echo oui || echo NON)" >> "$OUT"
echo "option --no-verify dans le script v2 (attendu 0) : $(grep -c -F -e '--no-verify' "$(dirname "$(dirname "$ICI")")/demarrage-machine-essai-3-v2.sh")" >> "$OUT"
kill "$PS"; wait "$PS" 2>/dev/null
cat "$OUT"
