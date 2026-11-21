#!/bin/bash
# point 4 : fabricant v3 avec 9beb... en 3e parametre, jeton factice de 100 signes
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v3
F=$W/pieces/fabriquer-donnees-demarrage-v3.sh
OUT=$W/tmp/p4; rm -rf $OUT; mkdir -p $OUT
git init -q --bare $OUT/distant.git
TOK=$(head -c 300 /dev/urandom | base64 -w0 | tr -dc 'A-Za-z0-9' | head -c 100)
echo "longueur jeton ${#TOK}" > $W/tables/p4-run.txt
export JFACT=$TOK
unset TOK
mkdir -p $OUT/s
( while [ ! -e $OUT/fini ]; do ps -eo args >> $OUT/ps.txt 2>/dev/null; done ) &
GP=$!
FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$OUT/distant.git bash $F JFACT $OUT/s/ud 9beb07052a5add7e7381b47f89aa5216a80130b5d8132b3c4fa96bf2a43b7588 >> $W/tables/p4-run.txt 2>&1
echo "code $?" >> $W/tables/p4-run.txt
touch $OUT/fini; wait $GP
# traces du jeton hors du fichier produit
grep -rl -F "$JFACT" $OUT > $W/tables/p4-trace-fichiers.txt
echo "fichiers contenant le jeton (attendu: seul ud) :" >> $W/tables/p4-run.txt
cat $W/tables/p4-trace-fichiers.txt >> $W/tables/p4-run.txt
sha256sum $OUT/s/ud.sans-jeton >> $W/tables/p4-run.txt
wc -c < $OUT/s/ud >> $W/tables/p4-run.txt
stat -c '%a' $OUT/s/ud >> $W/tables/p4-run.txt
# empreinte du script
echo "E_SCRIPT dans donnees :" >> $W/tables/p4-run.txt
sed -n 4p $OUT/s/ud | cut -c1-80 >> $W/tables/p4-run.txt
# taille JSON via outil de l'auteur
python3 -I $W/pieces/essais-outils/tailles-json.py $OUT/s/ud.sans-jeton 100 >> $W/tables/p4-run.txt 2>&1
echo "lignes ps capturees : $(wc -l < $OUT/ps.txt) ; contenant le jeton : $(grep -c -F "$JFACT" $OUT/ps.txt)" >> $W/tables/p4-run.txt
