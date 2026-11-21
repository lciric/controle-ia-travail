#!/bin/bash
# Éprouve la garde du versement (crochet avant poussée posé par le script de démarrage) sur le dépôt de versement d'un cas
# déjà joué : serveur factice relancé sur le distant du cas ; poussées vers main, vers une autre branche, effacement de la
# branche permise (artefacts : refus attendus, distant inchangé) ; puis une poussée vers la branche permise (cas sain :
# admise). Arrête son serveur par son identifiant.
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
PORT=$(shuf -i 20000-40000 -n 1)
/home/user/controle-ia-travail/.venv/bin/python -I "$ICI/serveur-git-factice.py" "$PORT" "$W/distant" "$W/serveur-jeton.txt" \
  "$W/journaux/serveur-garde.txt" "$W/serveur-pret-garde.txt" > /dev/null 2>&1 &
PS=$!
for i in $(seq 1 100); do [ -s "$W/serveur-pret-garde.txt" ] && break; sleep 0.1; done
export GIT_TERMINAL_PROMPT=0 GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
export NO_PROXY="127.0.0.1,localhost${NO_PROXY:+,$NO_PROXY}" no_proxy="127.0.0.1,localhost${no_proxy:+,$no_proxy}"
git -C "$V" config remote.origin.url "http://127.0.0.1:$PORT/controle-ia-travail.git"
avant() { git -C "$RD" for-each-ref --format='%(refname) %(objectname)' | sort; }
A0=$(avant)
essai() {  # nom, attendu (refus|admis), arguments de git push
  local nom=$1 att=$2; shift 2
  local sortie code
  sortie=$(git -C "$V" push "$@" 2>&1); code=$?
  local rendu=admis; [ $code -ne 0 ] && rendu=refus
  local garde=non; printf '%s' "$sortie" | grep -q "garde : refus" && garde=oui
  echo "$nom : attendu $att ; rendu $rendu (code $code ; message de la garde : $garde) ; $([ "$att" = "$rendu" ] && echo TENU || echo ÉCHEC)" >> "$OUT"
}
essai "vers main" refus origin HEAD:refs/heads/main
essai "vers une autre branche" refus origin HEAD:refs/heads/autre-branche
essai "vers une branche voisine du nom permis" refus origin "HEAD:refs/heads/$B-bis"
essai "effacement de la branche permise" refus origin ":refs/heads/$B"
A1=$(avant)
echo "distant inchangé par les quatre artefacts : $([ "$A0" = "$A1" ] && echo oui || echo NON)" >> "$OUT"
git -C "$V" commit -q --allow-empty -m "essai de la garde : poussée permise"
essai "vers la branche permise (sain)" admis origin "HEAD:refs/heads/$B"
echo "branche permise sur le distant = tête du versement : $([ "$(git -C "$RD" rev-parse "refs/heads/$B")" = "$(git -C "$V" rev-parse HEAD)" ] && echo oui || echo NON)" >> "$OUT"
kill "$PS"; wait "$PS" 2>/dev/null
cat "$OUT"
