#!/bin/bash
# Commande du lanceur v3, deux contrôles :
#  (1) dynamique : le VRAI lanceur v3, en emploi, par le VRAI script de départ v3, sur deux copies factices sans .git (l'une à
#      un chemin qui porte une espace), avec un interprète factice qui enregistre dossier courant, PYTHONPATH et arguments puis
#      rend 0 sans rien exécuter ; comparé à l'attendu calculé depuis la seule ligne du complément (argv-attendu-v4.py) ;
#  (2) statique : verifier-commande-v3.py sur le lanceur (attendu 0) et sur des lanceurs altérés (attendu 1), et sur la
#      ligne du complément elle-même prise pour un lanceur (attendu 1 : chemins codés).
# Usage : argv-v4.sh NOM PROGRAMME_REEL
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
D=$E/e/$1
PREEL=$2
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$D"
PY=/home/user/controle-ia-travail/.venv/bin/python
C=$B/complement.md
L=$B/lancer-essai-3-v3.sh
ECHECS=0

dynamique() {  # sous-dossier
  local X="$D/$1"
  mkdir -p "$X/tenue"
  bash "$E/preparer-copie-factice-v4.sh" "$X/copie" "$PREEL" d7f949acd9ac92e998e57663d2cc741de93f18c3 > /dev/null
  cp "$E/interprete-factice-v4.sh" "$X/interprete factice"
  chmod u+x "$X/interprete factice"
  bash "$B/demarrer-essai-3-v3.sh" "$X/tenue" "$X/copie" "$X/interprete factice" "$X/sorties de l'essai"
  for i in $(seq 1 100); do
    if [ -f "$X/tenue/code-de-sortie.txt" ]; then break; fi
    sleep 0.1
  done
  "$PY" -I -B "$E/argv-attendu-v4.py" "$C" "$X/copie" "$X/interprete factice" "$X/sorties de l'essai" > "$X/attendu.txt"
  echo "--- $1 : code de sortie écrit $(cat "$X/tenue/code-de-sortie.txt" 2>/dev/null || echo absent) ; reçu par l'interprète factice :"
  cat "$X/interprete factice.argv"
  if diff "$X/attendu.txt" "$X/interprete factice.argv" > "$X/diff.txt"; then
    echo "$1 : reçu ÉGAL à l'attendu calculé du complément : TENU"
  else
    echo "$1 : DIFFÉRENT de l'attendu : CASSÉ"; cat "$X/diff.txt"; ECHECS=$((ECHECS + 1))
  fi
  if [ -e "$X/sorties de l'essai" ]; then echo "$1 : dossier des sorties créé (le factice ne crée rien) : CASSÉ"; ECHECS=$((ECHECS + 1)); fi
}
dynamique sans-espace
dynamique "avec espace"

statique() {  # nom fichier attendu
  "$PY" -I -B "$B/verifier-commande-v3.py" "$C" "$2" > "$D/$1-verif.txt"
  local o=$?
  local v=TENU
  if [ "$o" != "$3" ]; then v=CASSÉ; ECHECS=$((ECHECS + 1)); fi
  echo "$1 : code du vérificateur $o (attendu $3) : $v : $(tail -n 1 "$D/$1-verif.txt")"
}
echo "lignes « env » du lanceur : $(grep -c '^env ' "$L")"
statique lanceur-v3 "$L" 0
sed 's|^env -C \(.*\) -B |env -C \1 -b |' "$L" > "$D/altere-octet-option.sh"
statique altere-octet-option "$D/altere-octet-option.sh" 1
sed 's|etage-processeur-v19\.md|etage-processeur-v18.md|' "$L" > "$D/altere-octet-chemin.sh"
statique altere-octet-chemin "$D/altere-octet-chemin.sh" 1
sed 's|^\(env -C .*\) "\$RACINE" "\$RACINE"/docs/notes/organisme-courbe|\1 "$RACINE" --en-trop "$RACINE"/docs/notes/organisme-courbe|' "$L" > "$D/altere-argument.sh"
statique altere-argument "$D/altere-argument.sh" 1
sed 's|^\(env -C .*\)$|\1\n\1|' "$L" > "$D/altere-deux-lignes.sh"
statique altere-deux-lignes "$D/altere-deux-lignes.sh" 1
sed 's|^\(env -C .*\) "\$RACINE" |\1 /home/user/palier-0b-racine |' "$L" > "$D/altere-chemin-code.sh"
statique altere-chemin-code "$D/altere-chemin-code.sh" 1
sed 's|^\(env -C .*\) "\$SORTIES"$|\1 $SORTIES|' "$L" > "$D/altere-guillemets.sh"
statique altere-guillemets "$D/altere-guillemets.sh" 1
sed 's|^env -C "\$RACINE"/|env -C "$RACINE2"/|' "$L" > "$D/altere-variable.sh"
statique altere-variable "$D/altere-variable.sh" 1
statique complement-pris-pour-lanceur "$C" 1
for f in altere-octet-option altere-octet-chemin altere-argument altere-deux-lignes altere-chemin-code altere-guillemets altere-variable; do
  if cmp -s "$L" "$D/$f.sh"; then echo "$f : l'altération n'a rien changé : essai NUL"; ECHECS=$((ECHECS + 1)); fi
done
echo "échecs : $ECHECS"
