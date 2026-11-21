#!/bin/bash
# Refus de départ du VRAI lanceur v3 en EMPLOI (non en vérification), lancé par le VRAI script de départ v3, détaché : copie
# sans fichier de commit (11), commit faux (11), interpréteur absent (14), dossier des sorties existant (10), fichier de la
# copie modifié (12) ; et un cas sain (0). L'interprète factice écrit "$0.argv" s'il est appelé : il ne doit l'être que dans le
# cas sain. Valeurs d'emploi du lanceur (aucun remplacement possible en emploi).
# Usage : lanceur-emploi-refus-v4.sh NOM PROGRAMME_REEL
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
D=$E/e/$1
PREEL=$2
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$D"
TETE=d7f949acd9ac92e998e57663d2cc741de93f18c3
ECHECS=0
N=0
cas() {  # nom code_attendu interprete_present(1|0) commit sorties_existantes(1|0) mutation
  local nom=$1 attendu=$2 ip=$3 commit=$4 sx=$5 mut=$6
  local X="$D/$nom"
  mkdir -p "$X/tenue"
  bash "$E/preparer-copie-factice-v4.sh" "$X/copie" "$PREEL" "$commit" > /dev/null
  case "$mut" in
    sans-commit) rm "$X/copie/COMMIT-DE-LA-COPIE.txt" ;;
    fichier-modifie) echo "octet de plus" >> "$X/copie/suivi.txt" ;;
  esac
  local I="$X/interprete-factice"
  if [ "$ip" = 1 ]; then cp "$E/interprete-factice-v4.sh" "$I"; chmod u+x "$I"; fi
  if [ "$sx" = 1 ]; then mkdir -p "$X/sorties"; fi
  bash "$B/demarrer-essai-3-v3.sh" "$X/tenue" "$X/copie" "$I" "$X/sorties" > "$X/depart.txt" 2>&1
  for i in $(seq 1 100); do
    if [ -f "$X/tenue/code-de-sortie.txt" ]; then break; fi
    sleep 0.1
  done
  sleep 0.3
  local o
  o=$(cat "$X/tenue/code-de-sortie.txt" 2>/dev/null || echo absent)
  local appele="non appelé"
  [ -f "$I.argv" ] && appele="APPELÉ"
  local v=TENU
  N=$((N + 1))
  if [ "$o" != "$attendu" ]; then v=CASSÉ; fi
  if [ "$attendu" != 0 ] && [ "$appele" != "non appelé" ]; then v=CASSÉ; fi
  if [ "$attendu" = 0 ] && [ "$appele" != "APPELÉ" ]; then v=CASSÉ; fi
  if [ "$v" = CASSÉ ]; then ECHECS=$((ECHECS + 1)); fi
  echo "$nom : code écrit $o (attendu $attendu) ; interprète $appele ; $v ; $(grep -E 'refus|départ du programme' "$X/tenue/journal-essai-3.txt" | tail -n 1 | cut -c1-220)"
}
cas e0-sain 0 1 "$TETE" 0 aucune
cas e1-sans-fichier-de-commit 11 1 "$TETE" 0 sans-commit
cas e2-commit-faux 11 1 0123456789abcdef0123456789abcdef01234567 0 aucune
cas e3-interprete-absent 14 0 "$TETE" 0 aucune
cas e4-sorties-existantes 10 1 "$TETE" 1 aucune
cas e5-fichier-de-la-copie-modifie 12 1 "$TETE" 0 fichier-modifie
echo "essais : $N ; échecs : $ECHECS"
