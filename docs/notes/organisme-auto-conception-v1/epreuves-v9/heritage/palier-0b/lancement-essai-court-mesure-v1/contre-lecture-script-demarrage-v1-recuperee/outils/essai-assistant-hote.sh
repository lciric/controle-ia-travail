#!/bin/bash
# Contre-lecteur, question 1 : l'assistant d'authentification posé par le script (assistant-jeton.sh) rend-il le jeton à
# n'importe quel hôte, ou seulement à github.com ? On lui présente les trois demandes que git lui ferait (hôte du dépôt,
# hôte étranger, absence d'hôte) et l'on compte seulement si la réponse contient le jeton factice (le jeton n'est pas affiché).
# Emploi : essai-assistant-hote.sh NOM_DU_CAS   (un cas joué, dont le dossier base/ porte l'assistant et le fichier du jeton)
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
W=$ME/auteur/travail/cas/$1
AS=$W/base/assistant-jeton.sh
JF=$ME/auteur/travail/jeton-factice.txt
echo "assistant : $(stat -c '%a' "$AS") ; fichier du jeton : $(stat -c '%a' "$W/secret/jeton") ; assistant sans le jeton en clair : $(grep -c -F -f "$JF" "$AS") ligne(s) le portant"
demande() {  # nom, texte des lignes (avant la ligne vide)
  local nom=$1; shift
  local rep
  rep=$(printf '%s\n' "$@" '' | bash "$AS" get)
  echo "$nom : réponse portant le jeton factice : $(printf '%s\n' "$rep" | grep -c -F -f "$JF") ; utilisateur : $(printf '%s\n' "$rep" | sed -n 's/^username=//p')"
}
demande "hôte github.com" protocol=https host=github.com path=lciric/controle-ia-travail.git
demande "hôte étranger evil.example" protocol=https host=evil.example
demande "aucun hôte" protocol=https
rep=$(printf '%s\n' protocol=https host=github.com '' | bash "$AS" store)
echo "demande « store » : sortie de $(printf '%s' "$rep" | wc -c) octet(s) (attendu 0)"
