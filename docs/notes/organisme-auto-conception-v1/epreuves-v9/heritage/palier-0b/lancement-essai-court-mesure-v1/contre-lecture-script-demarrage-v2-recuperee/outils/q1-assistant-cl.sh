#!/bin/bash
# CL, question 1 : l'assistant d'authentification ecrit par le script (cas arrete au pas a, DEPOT_URL de production
# https://github.com/...) : a qui rend-il le jeton factice ? Demandes au format de git, y compris des formes tordues.
# Emploi : q1-assistant-cl.sh CL NOM_DU_CAS
set -u
CL=$1; W=$CL/mes-essais/cas/$2
AS=$W/base/assistant-jeton.sh
JB=$CL/aut/essais/travail/jeton-factice.txt
OUT=$CL/mes-essais/q1-assistant-table.txt
: > "$OUT"
echo "texte de l'assistant ecrit par le script :" >> "$OUT"
cat "$AS" >> "$OUT"
echo "droits : $(stat -c %a "$AS") ; lignes portant le jeton en clair : $(grep -c -F -f "$JB" "$AS")" >> "$OUT"
req() {  # nom, attendu (jeton|rien), action, texte envoye (printf)
  local r n rendu
  r=$(printf "$4" | "$AS" "$3")
  n=$(printf '%s\n' "$r" | grep -c -F -f "$JB")
  rendu=rien; [ "$n" -gt 0 ] && rendu=jeton
  echo "$1 : attendu $2 ; rendu $rendu ; $([ "$2" = "$rendu" ] && echo TENU || echo ECHEC)" >> "$OUT"
}
req "https + github.com (production)" jeton get 'protocol=https\nhost=github.com\n\n'
req "idem avec path d'un autre depot du meme hote" jeton get 'protocol=https\nhost=github.com\npath=autre/depot.git\n\n'
req "idem avec username=x" jeton get 'protocol=https\nhost=github.com\nusername=x\n\n'
req "http (sans s) + github.com" rien get 'protocol=http\nhost=github.com\n\n'
req "https + hote voisin github.com.evil.example" rien get 'protocol=https\nhost=github.com.evil.example\n\n'
req "https + evilgithub.com" rien get 'protocol=https\nhost=evilgithub.com\n\n'
req "https + github.com:443" rien get 'protocol=https\nhost=github.com:443\n\n'
req "https + GitHub.com (casse)" rien get 'protocol=https\nhost=GitHub.com\n\n'
req "https + github.com. (point final)" rien get 'protocol=https\nhost=github.com.\n\n'
req "https + hote avec retour chariot" rien get 'protocol=https\nhost=github.com\r\n\n'
req "deux hotes, le permis en dernier" jeton get 'protocol=https\nhost=evil.example\nhost=github.com\n\n'
req "deux hotes, l'etranger en dernier" rien get 'protocol=https\nhost=github.com\nhost=evil.example\n\n'
req "hote permis apres la ligne vide (ignore)" rien get 'protocol=https\n\nhost=github.com\n\n'
req "sans ligne vide finale, hote permis" jeton get 'protocol=https\nhost=github.com\n'
req "url= au lieu de protocol/host" rien get 'url=https://github.com/lciric/controle-ia-travail.git\n\n'
req "action store" rien store 'protocol=https\nhost=github.com\nusername=x\npassword=y\n\n'
req "action erase" rien erase 'protocol=https\nhost=github.com\n\n'
req "action inconnue (capability)" rien capability 'protocol=https\nhost=github.com\n\n'
req "sans action" rien '' 'protocol=https\nhost=github.com\n\n'
cat "$OUT"
