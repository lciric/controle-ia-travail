#!/bin/bash
# CL, question 4 : bornes exactes de l'age de H0_PREVU. Pour chaque cas, la ligne 2 des donnees (H0_PREVU=) est remplacee par
# maintenant - DECALAGE ; le script est joue avec un faux apt qui echoue (code 30 au pas a, apres le controle de l'age) :
# 30 = age admis, 21 = refuse. Aucun clonage : cas rapides. Avant : bornes -600 et 7200 ; ecarts de 5 s de part et d'autre.
# Emploi : q4-ages-cl.sh CL DONNEES_SAINES
set -u
CL=$1; UD=$2
export TMPDIR=$CL/tmp
OUT=$CL/mes-essais/q4-ages-table.txt
: > "$OUT"
cas() {  # nom, valeur de la ligne H0_PREVU=, attendu
  local nom=$1 val=$2 att=$3 f=$CL/mes-essais/ud-q4-$1
  sed "2s/.*/H0_PREVU=$val/" "$UD" > "$f"
  bash "$CL/mes-outils/jouer-cl.sh" "$CL" "q4-$nom" "$f" FAUX_APT_ECHEC=1 > /dev/null 2>&1
  local R=$CL/mes-essais/cas/q4-$nom/resume.txt
  local code; code=$(sed -n 's/^code du script de demarrage : \([0-9]*\) ;.*/\1/p' "$R")
  local echec; echec=$(sed -n 's/^--- echec ecrit : //p' "$R")
  echo "$nom : H0_PREVU=$val ; attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ECHEC) ; $echec" >> "$OUT"
}
iso() { date -u -d "now $1 seconds" +%Y-%m-%dT%H:%M:%SZ; }
cas vieux-7195 "$(iso -7195)" 30
cas vieux-7210 "$(iso -7210)" 21
cas futur-590 "$(iso +590)" 30
cas futur-610 "$(iso +610)" 21
cas maintenant "$(iso +0)" 30
cas mal-forme-z-minuscule "$(iso +0 | tr Z z)" 21
cas mal-forme-sans-z "$(iso +0 | tr -d Z)" 21
cas mal-forme-decalage "$(iso +0 | tr -d Z)+00:00" 21
cas mal-forme-espace "$(iso +0 | tr T ' ')" 21
cas mal-forme-fraction "$(iso +0 | tr -d Z).5Z" 21
cas date-impossible "2026-02-30T10:00:00Z" 21
cas epoque "1970-01-01T00:00:00Z" 21
cas an-9999 "9999-12-31T23:59:59Z" 21
cas absent "" 21
cat "$OUT"
