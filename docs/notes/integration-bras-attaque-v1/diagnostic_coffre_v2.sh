#!/usr/bin/env bash
# Diagnostic des empreintes du coffre — v2 (remplace la v1 du bloc-notes, jamais versée).
# Parcourt TOUS les compagnons .sha256 de l'arbre de chaque branche (la v1 de l'inventaire ne voyait que les compagnons
# ajoutés ou modifiés sur la branche : une cible modifiée sous un compagnon inchangé lui échappait).
# Divulgation graduée : un chemin n'est affiché en entier QUE s'il existe aussi sur origin/main (donc hors coffre).
# Sinon : premier composant du chemin, profondeur, extension. Jamais de contenu.
# Usage : diagnostic_coffre_v2.sh <racine du dépôt> <branche> [<branche> ...]   (branches déjà rapatriées)
set -u
cd "$1" || exit 2; shift
masque() { local p="$1" IFS=/; read -r -a c <<< "$p"; printf '%s/… (profondeur %s, extension .%s)' "${c[0]}" "${#c[@]}" "${p##*.}"; }
declare -A M=()
while IFS= read -r -d '' l; do meta="${l%%$'\t'*}"; p="${l#*$'\t'}"; set -- $meta; M["$p"]="$3"; done < <(git ls-tree -r -z origin/main)
for b in $LISTE_BRANCHES; do
  ref="refs/remotes/origin/$b"
  git rev-parse -q --verify "$ref" >/dev/null || { echo "## \`$b\` : RÉFÉRENCE ABSENTE (rapatrier d'abord)"; continue; }
  declare -A B=()
  while IFS= read -r -d '' l; do meta="${l%%$'\t'*}"; p="${l#*$'\t'}"; set -- $meta; B["$p"]="$3"; done < <(git ls-tree -r -z "$ref")
  echo "## \`$b\`"
  tot=0; idem=0; ok=0; ko=0; abs_herite=0; abs_main_present=0; abs_propre=0; declare -A parrep=()
  for f in "${!B[@]}"; do
    case "$f" in *.sha256) ;; *) continue;; esac
    tot=$((tot+1)); cible="${f%.sha256}"
    if [ -n "${B[$cible]:-}" ]; then
      if [ "${B[$cible]}" = "${M[$cible]:-x}" ] && [ "${B[$f]}" = "${M[$f]:-y}" ]; then idem=$((idem+1)); continue; fi
      attendu=$(git cat-file blob "${B[$f]}" | awk 'NR==1{print $1}')
      reel=$(git cat-file blob "${B[$cible]}" | sha256sum | awk '{print $1}')
      if [ "$attendu" = "$reel" ]; then ok=$((ok+1)); continue; fi
      ko=$((ko+1))
      fmt=non; [[ "$attendu" =~ ^[0-9a-f]{64}$ ]] && fmt=oui
      if [ -n "${M[$cible]:-}" ]; then
        aff="$cible"; surmain=oui
        memecible=non; [ "${B[$cible]}" = "${M[$cible]}" ] && memecible=oui
        if [ -n "${M[$f]:-}" ]; then
          am=$(git cat-file blob "${M[$f]}" | awk 'NR==1{print $1}'); rm_=$(git cat-file blob "${M[$cible]}" | sha256sum | awk '{print $1}')
          confmain=non; [ "$am" = "$rm_" ] && confmain=oui
          memecomp=non; [ "${B[$f]}" = "${M[$f]}" ] && memecomp=oui
        else confmain="compagnon absent de main"; memecomp="—"; fi
      else aff="$(masque "$cible")"; surmain=non; memecible="—"; confmain="—"; memecomp="—"; fi
      dc=$(git log -1 --format=%cI "$ref" -- "$cible" | head -1); dp=$(git log -1 --format=%cI "$ref" -- "$f" | head -1)
      dc=$(date -u -d "$dc" +%Y-%m-%dT%H:%MZ 2>/dev/null); dp=$(date -u -d "$dp" +%Y-%m-%dT%H:%MZ 2>/dev/null)
      echo "- NON CONFORME n° $ko : $aff ; sur main : $surmain ; empreinte attendue bien formée : $fmt ; cible identique à celle de main : $memecible ; compagnon identique à celui de main : $memecomp ; conforme sur main : $confmain ; dernier commit de la cible : $dc ; du compagnon : $dp"
    else
      top="${f%%/*}"
      if [ -n "${M[$f]:-}" ]; then
        if [ -n "${M[$cible]:-}" ]; then abs_main_present=$((abs_main_present+1)); else abs_herite=$((abs_herite+1)); parrep[$top]=$(( ${parrep[$top]:-0} + 1 )); fi
      else abs_propre=$((abs_propre+1)); fi
    fi
  done
  echo "- compagnons dans l'arbre : $tot ; identiques à main, cible et compagnon (non recalculés) : $idem ; recalculés conformes : $ok ; non conformes : $ko"
  echo "- compagnons sans cible : hérités (compagnon sur main, cible absente de main aussi) $abs_herite ; compagnon sur main mais cible présente sur main $abs_main_present ; propres à la branche (compagnon absent de main) $abs_propre"
  if [ "$abs_herite" -gt 0 ]; then printf -- '- hérités, par répertoire de tête :'; for k in "${!parrep[@]}"; do printf ' %s %s ;' "$k" "${parrep[$k]}"; done; echo; fi
  unset parrep B
done
