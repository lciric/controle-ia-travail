#!/bin/bash
# Contre-lecteur : joue un cas avec l'outil de l'auteur (jouer-cas.sh) pendant que MON guetteur d'environnement tourne ;
# pose mes faux apt et faux python3 (qui relèvent leur environnement) et ESSAI_JETON_FICHIER ; recherche aussi la forme
# base64 de « x-access-token:JETON » (en-tête d'authentification de base) dans tous les fichiers du cas.
# Emploi : jouer-avec-guetteur-environ.sh NOM DONNEES [VAR=VALEUR ...]
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
AUT=$ME/auteur
NOM=$1; UD=$2; shift 2
JF=$AUT/travail/jeton-factice.txt
W=$AUT/travail/cas/$NOM
mkdir -p "$ME/resultats"
GE=$ME/resultats/guetteur-environ-$NOM.txt
ARRET=$ME/resultats/guetteur-environ-$NOM.arret
[ ! -e "$GE" ] || { echo "refus : $GE existe"; exit 1; }
rm -f "$ARRET"
bash "$ME/outils/guetteur-environ.sh" "$JF" "$GE" "$ARRET" &
PG=$!
bash "$AUT/essais-outils/jouer-cas.sh" "$NOM" "$UD" ESSAI_JETON_FICHIER="$JF" ESSAI_DEMARRAGE_APT_GET="$ME/outils/mon-faux-apt-get.sh" \
  ESSAI_DEMARRAGE_PY_SYS="$ME/outils/mon-faux-python3.sh" "$@"
: > "$ARRET"
wait "$PG"
echo "=== guetteur d'environnement (contre-lecteur) : $(tail -n 1 "$GE")"
grep -v '^balayages' "$GE" | head -n 5
echo "=== environnement des faux (contre-lecteur) :"
cat "$W/journaux/factices.txt.apt-env" 2> /dev/null
cat "$W/journaux/programme.txt.env" 2> /dev/null
B64=$(printf 'x-access-token:%s' "$(head -n 1 "$JF")" | base64 -w 0)
echo "=== forme base64 de x-access-token:JETON dans les fichiers du cas : $(grep -r -l -F "$B64" "$W" 2> /dev/null | grep -v -c -x "$W/part-001")"
echo "=== sortie du script de démarrage (stdout/stderr non redirigés, ce que cloud-init capterait) : $(wc -c < "$W/journaux/sortie-script.txt") octets ; lignes portant le jeton : $(grep -c -F -f "$JF" "$W/journaux/sortie-script.txt")"
