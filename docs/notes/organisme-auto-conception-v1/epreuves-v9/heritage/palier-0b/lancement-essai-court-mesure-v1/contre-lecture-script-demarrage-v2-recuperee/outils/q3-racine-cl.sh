#!/bin/bash
# CL, question 3 : altere la racine dans la fenetre c -> f (par un faux pip) de sept facons, et note ce que le script rend.
# Attendu : fichier ajoute / lien / modif / suppression -> 81 (le lanceur refuse en verification seule) ; .git (fichier,
# sous-dossier, vide) -> 55 ; dossier vide ajoute et chmod -> 0 (non detectes : aucun effet sur le contenu des fichiers).
# Emploi : q3-racine-cl.sh CL DONNEES
set -u
CL=$1; UD=$2
OUT=$CL/mes-essais/q3-racine-table.txt
: > "$OUT"
cas() {  # nom, attendu
  local nom=$1 att=$2
  bash "$CL/mes-outils/jouer-cl.sh" "$CL" "q3-$nom" "$UD" "CL_PIP_PLANTE=$nom" "ESSAI_DEMARRAGE_PY_SYS=$CL/mes-outils/faux-python3-cl.sh" > /dev/null 2>&1
  local R=$CL/mes-essais/cas/q3-$nom/resume.txt
  local code; code=$(sed -n 's/^code du script de demarrage : \([0-9]*\) ;.*/\1/p' "$R")
  local echec; echec=$(sed -n 's/^--- echec ecrit : //p' "$R")
  local prog; prog=$(sed -n 's/^--- base creee : .* faux programme lance : //p' "$R")
  echo "$nom : attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ECHEC) ; programme lance : $prog ; $echec" >> "$OUT"
}
cas fichier 81
cas lien 81
cas modif 81
cas suppression 81
cas git-fichier 55
cas sous-git 55
cas git-vide 55
cas dossier-vide 0
cas chmod 0
cat "$OUT"
