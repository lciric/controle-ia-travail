#!/bin/bash
# Lanceur v4 en EMPLOI (valeurs d'emploi, aucun remplacement possible), par le VRAI script de départ v4, détaché, sur la
# VRAIE copie (arbre du commit extrait, plus les deux fichiers), avec un interprète factice qui enregistre ce qu'il reçoit et
# rend 0 sans rien exécuter :
#  (1) commande exécutée : sain, puis la même copie déplacée (mv) à un chemin qui porte une espace et ramenée ensuite ;
#      comparée à l'attendu calculé de la seule ligne du complément (argv-attendu-v4.py de la v3) ;
#  (2) refus en emploi : sans fichier de commit, commit faux, interpréteur absent, sorties existantes, fichier modifié, lien
#      ajouté (chaque artefact défait aussitôt) ; l'interprète ne doit être appelé que dans les cas sains ;
#  (3) commande statique : verifier-commande-v3.py sur le lanceur v4 (0) et sur huit altérations (1).
# Usage : emploi-et-commande-l4.sh DOSSIER_NEUF COPIE_REELLE COMPLEMENT
set -u
E=$(cd "$(dirname "$0")" && pwd)
L4=$(cd "$E/.." && pwd)
B3=$(cd "$L4/.." && pwd)
D=$1; RR=$2; C=$3
PY=/home/user/controle-ia-travail/.venv/bin/python
L=$L4/lancer-essai-3-v4.sh
TE=d7f949acd9ac92e998e57663d2cc741de93f18c3
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$D"
ECHECS=0
N=0
emploi() {  # nom code_attendu racine interprete_present(1|0) sorties_existantes(1|0) comparer_argv(1|0)
  local nom=$1 attendu=$2 r=$3 ip=$4 sx=$5 cmpv=$6
  local X="$D/$nom"
  mkdir -p "$X/tenue"
  local I="$X/interprete factice"
  if [ "$ip" = 1 ]; then cp "$B3/essais/interprete-factice-v4.sh" "$I"; chmod u+x "$I"; fi
  local S="$X/sorties de l'essai"
  if [ "$sx" = 1 ]; then mkdir -p "$S"; fi
  bash "$L4/demarrer-essai-3-v4.sh" "$X/tenue" "$r" "$I" "$S" > "$X/depart.txt" 2>&1
  for i in $(seq 1 600); do
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
  local egal=""
  if [ "$cmpv" = 1 ]; then
    "$PY" -I -B "$B3/essais/argv-attendu-v4.py" "$C" "$r" "$I" "$S" > "$X/attendu.txt"
    if diff "$X/attendu.txt" "$I.argv" > "$X/diff.txt"; then egal=" ; argv ÉGAL à l'attendu du complément"; else egal=" ; argv DIFFÉRENT"; v=CASSÉ; cat "$X/diff.txt"; fi
  fi
  if [ "$v" = CASSÉ ]; then ECHECS=$((ECHECS + 1)); fi
  echo "$nom : code écrit $o (attendu $attendu) ; interprète $appele$egal ; $v ; $(grep -E 'refus|départ du programme' "$X/tenue/journal-essai-3.txt" | tail -n 1 | cut -c1-200)"
}
emploi e0-sain 0 "$RR" 1 0 1
ESP="$(dirname "$RR")/copie avec espace"
mv "$RR" "$ESP"
emploi e0b-sain-chemin-avec-espace 0 "$ESP" 1 0 1
mv "$ESP" "$RR"
mv "$RR/COMMIT-DE-LA-COPIE.txt" "$D/commit-mis-de-cote.txt"
emploi e1-sans-fichier-de-commit 11 "$RR" 1 0 0
mv "$D/commit-mis-de-cote.txt" "$RR/COMMIT-DE-LA-COPIE.txt"
cp -p "$RR/COMMIT-DE-LA-COPIE.txt" "$D/commit-sauvegarde.txt"
echo 0123456789abcdef0123456789abcdef01234567 > "$RR/COMMIT-DE-LA-COPIE.txt"
emploi e2-commit-faux 11 "$RR" 1 0 0
cp -p "$D/commit-sauvegarde.txt" "$RR/COMMIT-DE-LA-COPIE.txt"
emploi e3-interprete-absent 14 "$RR" 0 0 0
emploi e4-sorties-existantes 10 "$RR" 1 1 0
CIBLE="$RR/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md"
cp -p "$CIBLE" "$D/sauvegarde-fichier"
echo "octet de plus" >> "$CIBLE"
emploi e5-fichier-de-la-copie-modifie 12 "$RR" 1 0 0
cp -p "$D/sauvegarde-fichier" "$CIBLE"
ln -s COMMIT-DE-LA-COPIE.txt "$RR/lien-ajoute"
emploi e6-lien-symbolique-ajoute 12 "$RR" 1 0 0
rm "$RR/lien-ajoute"
emploi e7-sain-apres-retour 0 "$RR" 1 0 1

statique() {  # nom fichier attendu
  "$PY" -I -B "$B3/verifier-commande-v3.py" "$C" "$2" > "$D/$1-verif.txt"
  local o=$?
  local v=TENU
  N=$((N + 1))
  if [ "$o" != "$3" ]; then v=CASSÉ; ECHECS=$((ECHECS + 1)); fi
  echo "$1 : code du vérificateur $o (attendu $3) : $v : $(tail -n 1 "$D/$1-verif.txt")"
}
echo "lignes « env » du lanceur v4 : $(grep -c '^env ' "$L")"
echo "ligne de commande égale à celle du lanceur v3 : $(if cmp -s <(grep '^env -C ' "$L") <(grep '^env -C ' "$B3/lancer-essai-3-v3.sh"); then echo oui; else echo NON; fi)"
statique lanceur-v4 "$L" 0
sed 's|^env -C \(.*\) -B |env -C \1 -b |' "$L" > "$D/altere-octet-option.sh"; statique altere-octet-option "$D/altere-octet-option.sh" 1
sed 's|etage-processeur-v19\.md|etage-processeur-v18.md|' "$L" > "$D/altere-octet-chemin.sh"; statique altere-octet-chemin "$D/altere-octet-chemin.sh" 1
sed 's|^\(env -C .*\) "\$RACINE" "\$RACINE"/docs/notes/organisme-courbe|\1 "$RACINE" --en-trop "$RACINE"/docs/notes/organisme-courbe|' "$L" > "$D/altere-argument.sh"; statique altere-argument "$D/altere-argument.sh" 1
sed 's|^\(env -C .*\)$|\1\n\1|' "$L" > "$D/altere-deux-lignes.sh"; statique altere-deux-lignes "$D/altere-deux-lignes.sh" 1
sed 's|^\(env -C .*\) "\$RACINE" |\1 /home/user/palier-0b-racine |' "$L" > "$D/altere-chemin-code.sh"; statique altere-chemin-code "$D/altere-chemin-code.sh" 1
sed 's|^\(env -C .*\) "\$SORTIES"$|\1 $SORTIES|' "$L" > "$D/altere-guillemets.sh"; statique altere-guillemets "$D/altere-guillemets.sh" 1
sed 's|^env -C "\$RACINE"/|env -C "$RACINE2"/|' "$L" > "$D/altere-variable.sh"; statique altere-variable "$D/altere-variable.sh" 1
statique complement-pris-pour-lanceur "$C" 1
for f in altere-octet-option altere-octet-chemin altere-argument altere-deux-lignes altere-chemin-code altere-guillemets altere-variable; do
  if cmp -s "$L" "$D/$f.sh"; then echo "$f : l'altération n'a rien changé : essai NUL"; ECHECS=$((ECHECS + 1)); fi
done
echo "liste de la vraie copie après les essais : $(sha256sum "$RR/EMPREINTES-DE-LA-COPIE.txt" | cut -d' ' -f1)"
echo "essais : $N ; échecs : $ECHECS"
