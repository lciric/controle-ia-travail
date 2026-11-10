#!/usr/bin/env bash
# Instruction des empreintes non conformes d'une branche du coffre — v1.
# N'affiche d'un chemin que les composants déjà présents comme composants de chemin sur origin/main (vocabulaire public) ;
# tout autre composant est remplacé par ‹propre, n caractères› (plus une catégorie générique pour le nom de fichier).
# Jamais de contenu. Dit si le scellé était juste au moment où il a été écrit, et ce qui a changé depuis (comptes de lignes).
set -u
cd "$1" || exit 2; b="$2"; ref="refs/remotes/origin/$b"
declare -A M=() V=() B=()
while IFS= read -r -d '' l; do meta="${l%%$'\t'*}"; p="${l#*$'\t'}"; set -- $meta; M["$p"]="$3"; IFS=/ read -r -a cs <<< "$p"; for c in "${cs[@]}"; do V["$c"]=1; done; done < <(git ls-tree -r -z origin/main)
while IFS= read -r -d '' l; do meta="${l%%$'\t'*}"; p="${l#*$'\t'}"; set -- $meta; B["$p"]="$3"; done < <(git ls-tree -r -z "$ref")
n=0
for f in "${!B[@]}"; do
  case "$f" in *.sha256) ;; *) continue;; esac
  cible="${f%.sha256}"; [ -n "${B[$cible]:-}" ] || continue
  [ "${B[$cible]}" = "${M[$cible]:-x}" ] && [ "${B[$f]}" = "${M[$f]:-y}" ] && continue
  attendu=$(git cat-file blob "${B[$f]}" | awk 'NR==1{print $1}')
  reel=$(git cat-file blob "${B[$cible]}" | sha256sum | awk '{print $1}')
  [ "$attendu" = "$reel" ] && continue
  n=$((n+1))
  IFS=/ read -r -a cs <<< "$cible"; aff=""
  for c in "${cs[@]}"; do if [ -n "${V[$c]:-}" ]; then aff="$aff/$c"; else aff="$aff/‹propre, ${#c} caractères›"; fi; done
  base="${cible##*/}"; cat=autre
  shopt -s nocasematch
  for mot in journal etat état manifeste log cellule synthese synthèse fiche question reponse réponse devis classement notes sonde bilan; do [[ "$base" == *"$mot"* ]] && { cat="$mot"; break; }; done
  shopt -u nocasematch
  cc=$(git log -1 --format=%H "$ref" -- "$f"); ct=$(git log -1 --format=%H "$ref" -- "$cible")
  alors=$(git cat-file blob "$cc:$cible" 2>/dev/null | sha256sum | awk '{print $1}')
  juste=non; [ "$alors" = "$attendu" ] && juste=oui
  apres=$(git rev-list --count "$cc..$ref" -- "$cible")
  ns=$(git diff --numstat "$cc" "$ref" -- "$cible" | awk '{print "+"$1" / -"$2}')
  lignes_alors=$(git cat-file blob "$cc:$cible" 2>/dev/null | wc -l); lignes_now=$(git cat-file blob "${B[$cible]}" | wc -l)
  prefixe=non; if [ "$(git cat-file blob "${B[$cible]}" | head -n "$lignes_alors" | sha256sum | awk '{print $1}')" = "$alors" ]; then prefixe=oui; fi
  echo "- n° $n : ${aff#/} ; catégorie du nom : $cat ; scellé juste à l'instant du compagnon (commit ${cc:0:8}) : $juste ; commits qui touchent la cible ensuite : $apres ; lignes ajoutées / retirées depuis : $ns ; lignes alors $lignes_alors, maintenant $lignes_now ; la version scellée est un préfixe exact de la version actuelle : $prefixe"
done
echo "- total non conformes : $n"
