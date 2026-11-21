#!/bin/bash
# CL, question 2 : artefacts de la garde de poussee, en plus de ceux de l'auteur, sur le depot de versement du cas s1-sain.
# Emploi : q2-garde-cl.sh DOSSIER_CL
set -u
CL=$1
OUTILS=$CL/aut/v2/essais/outils
W=$CL/aut/v2/essais/travail/cas/s1-sain
V=$W/base/versement
RD=$W/distant/controle-ia-travail.git
B=recuperation/palier-0b-programme-1-essai-3-v1
OUT=$CL/mes-essais/q2-garde-cl.txt
export TMPDIR=$CL/tmp
: > "$OUT"
rm -f "$W/serveur-pret-cl.txt"
PORT=$(grep -o '127\.0\.0\.1:[0-9]*' "$W/base/assistant-jeton.sh" | head -n 1 | cut -d: -f2)
/home/user/controle-ia-travail/.venv/bin/python -I "$OUTILS/serveur-git-factice.py" "$PORT" "$W/distant" "$W/serveur-jeton.txt" \
  "$W/journaux/serveur-cl.txt" "$W/serveur-pret-cl.txt" > /dev/null 2>&1 &
PS=$!
for i in $(seq 1 100); do [ -s "$W/serveur-pret-cl.txt" ] && break; sleep 0.1; done
export GIT_TERMINAL_PROMPT=0 GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
export NO_PROXY="127.0.0.1,localhost${NO_PROXY:+,$NO_PROXY}" no_proxy="127.0.0.1,localhost${no_proxy:+,$no_proxy}"
export GIT_AUTHOR_NAME=cl GIT_AUTHOR_EMAIL=cl@invalid GIT_COMMITTER_NAME=cl GIT_COMMITTER_EMAIL=cl@invalid
URL=http://127.0.0.1:$PORT/controle-ia-travail.git
git -C "$V" config remote.origin.url "$URL"
avant() { git -C "$RD" for-each-ref --format='%(refname) %(objectname)' | sort; }
essai() {  # nom, attendu (refus|admis), arguments de git push
  local nom=$1 att=$2; shift 2
  local sortie code A0 A1
  A0=$(avant)
  sortie=$(git -C "$V" push "$@" 2>&1); code=$?
  A1=$(avant)
  local rendu=admis; [ $code -ne 0 ] && rendu=refus
  local garde=non; printf '%s' "$sortie" | grep -q "garde : refus" && garde=oui
  local msg; msg=$(printf '%s' "$sortie" | grep -m1 -o 'garde : refus[^"]*')
  echo "$nom : attendu $att ; rendu $rendu (code $code ; garde du crochet : $garde ${msg:+« $msg »} ; distant change : $([ "$A0" = "$A1" ] && echo non || echo OUI)) ; $([ "$att" = "$rendu" ] && echo TENU || echo ECHEC)" >> "$OUT"
}
# depart propre : depot de versement sur la tete distante
ORIG=$(git -C "$RD" rev-parse "refs/heads/$B")
git -C "$V" reset -q --hard "$ORIG"
git -C "$V" commit -q --allow-empty -m "cl : commit local de depart"
echo "tete distante au depart $ORIG ; tete locale $(git -C "$V" rev-parse HEAD)" >> "$OUT"
# 1. le distant est AVANCE d'un commit que la machine ne connait pas (poussee faite par un tiers, descendante de la tete)
ETR=$(git -C "$RD" commit-tree "$(git -C "$RD" rev-parse "$ORIG^{tree}")" -p "$ORIG" -m "commit d'un tiers")
git -C "$RD" update-ref "refs/heads/$B" "$ETR"
echo "le tiers pousse $ETR (inconnu du depot de versement : $(git -C "$V" cat-file -e "$ETR" 2>/dev/null && echo connu || echo inconnu))" >> "$OUT"
essai "1a. distant avance par un tiers, poussee simple" refus origin "HEAD:refs/heads/$B"
essai "1b. distant avance par un tiers, poussee forcee" refus origin "+HEAD:refs/heads/$B"
echo "   tete distante apres 1a et 1b : $(git -C "$RD" rev-parse "refs/heads/$B") (attendu $ETR : $([ "$(git -C "$RD" rev-parse "refs/heads/$B")" = "$ETR" ] && echo oui || echo NON))" >> "$OUT"
# 2. le distant est ramene a la tete connue : poussee de plusieurs references, mirror, all, tags
git -C "$RD" update-ref "refs/heads/$B" "$ORIG"
git -C "$V" tag etiquette-cl
git -C "$V" branch autre-branche-cl
essai "2a. deux references dont une permise et main" refus origin "HEAD:refs/heads/$B" "HEAD:refs/heads/main"
essai "2b. --all (branches locales)" refus origin --all
essai "2c. --tags" refus origin --tags
essai "2d. --mirror" refus origin --mirror
essai "2e. effacement par --delete" refus origin --delete "$B"
essai "2f. autre URL (meme serveur), vers main" refus "$URL" "HEAD:refs/heads/main"
essai "2g. nom de la branche permise suivi d'une barre" refus origin "HEAD:refs/heads/$B/"
# 3. controle : poussee descendante de la tete connue : admise
essai "3. sain : poussee descendante" admis origin "HEAD:refs/heads/$B"
echo "tete distante apres 3 : $(git -C "$RD" rev-parse "refs/heads/$B") ; tete locale $(git -C "$V" rev-parse HEAD)" >> "$OUT"
# 4. le crochet vu de pres
echo "--- crochet pre-push du depot de versement (texte) :" >> "$OUT"
cat "$V/.git/hooks/pre-push" >> "$OUT"
echo "droits du crochet : $(stat -c %a "$V/.git/hooks/pre-push")" >> "$OUT"
# 5. contournements : montrent seulement que le crochet est la SEULE garde cote machine (aucun effet sur le distant n'est voulu ici : on pousse vers une branche d'essai du depot factice)
essai "5a. contournement --no-verify vers une autre branche du depot factice" admis origin --no-verify "HEAD:refs/heads/branche-hors-garde-cl"
essai "5b. contournement core.hooksPath vers main du depot factice" admis -c core.hooksPath=/dev/null origin "HEAD:refs/heads/main-cl"
kill "$PS"; wait "$PS" 2>/dev/null
cat "$OUT"
