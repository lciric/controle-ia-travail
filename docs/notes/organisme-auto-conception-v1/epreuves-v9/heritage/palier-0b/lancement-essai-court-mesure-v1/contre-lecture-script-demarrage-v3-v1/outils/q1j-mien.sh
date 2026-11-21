#!/bin/bash
# point 5 : rejeu de q1-j avec MON espion (lit seulement J, JFACT, JETON) et mon objet faux (v3 sans la ligne declare +x J).
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v3
O=$W/tmp/q1j; rm -rf $O; mkdir -p $O/esp $O/s $O/fab
git init -q --bare $O/distant.git
cp $W/pieces/amorce-demarrage-essai-3-v3.sh $W/pieces/demarrage-machine-essai-3-v3.sh $O/fab/
cp $W/pieces/fabriquer-donnees-demarrage-v3.sh $O/fab/vrai.sh
grep -v '^declare +x J$' $W/pieces/fabriquer-donnees-demarrage-v3.sh > $O/fab/faux.sh
echo "lignes retirees dans faux.sh : $(( $(wc -l < $W/pieces/fabriquer-donnees-demarrage-v3.sh) - $(wc -l < $O/fab/faux.sh) ))" > $W/tables/q1j-mien.txt
cat > $O/esp/git <<'ESP'
#!/bin/bash
# espion : ne lit que J et JFACT ; ne note aucune valeur
a=0; [ "${J:-}" = "${TOKREF:-x}" ] && a=1
b=0; [ "${JFACT:-}" = "${TOKREF:-x}" ] && b=1
echo "git J=$a JFACT=$b" >> "$ESPLOG"
exec /usr/bin/git "$@"
ESP
chmod +x $O/esp/git
jouer() {  # $1 nom ; $2 script ; $3 J prealable exporte (oui/non)
  rm -rf $O/s/*; export ESPLOG=$O/log-$1.txt; : > $ESPLOG
  TOKREF=$(head -c 300 /dev/urandom | base64 -w0 | tr -dc 'A-Za-z0-9' | head -c 100)
  export TOKREF JFACT=$TOKREF
  if [ "$3" = oui ]; then export J=valeur-prealable-de-la-session; else unset J; fi
  PATH=$O/esp:$PATH FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$O/distant.git bash $2 JFACT $O/s/ud > $O/sortie-$1.txt 2>&1
  c=$?
  fuite=$(grep -c 'J=1' $ESPLOG); n=$(grep -c . $ESPLOG)
  trace=$(grep -rl -F "$TOKREF" $O/s $O/sortie-$1.txt $ESPLOG 2>/dev/null | grep -v '/s/ud$' | wc -l)
  echo "$1 : code $c ; appels git $n ; dont J porte le jeton $fuite ; fichiers (hors ud) portant le jeton $trace" >> $W/tables/q1j-mien.txt
  unset J JFACT TOKREF
}
# J exporte avec une valeur prealable de la session
jouer temoin-v3-sans-J $O/fab/vrai.sh non
jouer faux-sans-declare-J-exporte $O/fab/faux.sh oui
jouer v3-J-exporte-jeton $O/fab/vrai.sh oui
