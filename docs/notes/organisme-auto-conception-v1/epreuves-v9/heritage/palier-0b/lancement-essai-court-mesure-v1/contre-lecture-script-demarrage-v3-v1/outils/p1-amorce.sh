#!/bin/bash
# point 1 : amorce v3, rouge sur charges alterees, verte sur la saine. Script de demarrage REMPLACE par un script-temoin
# (STUB, hors du banc de l'auteur) qui affiche d'ou il est lu et son empreinte puis rend 7 ; le fabricant v3 reel assemble les donnees.
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v3
O=$W/tmp/p1; rm -rf $O; mkdir -p $O/s $O/fab $O/run
T=$W/tables/p1-table.txt; : > $T
git init -q --bare $O/distant.git
cp $W/pieces/amorce-demarrage-essai-3-v3.sh $O/fab/
cp $W/pieces/fabriquer-donnees-demarrage-v3.sh $O/fab/fab.sh
sed -n 11,14p $W/pieces/demarrage-machine-essai-3-v3.sh > $O/pieces-lignes.txt
mkstub() {  # $1 sortie ; $2 marque
  { echo '#!/bin/bash'; echo 'BRANCHE=recuperation/palier-0b-test'; echo 'DEPOT_URL=https://example.invalid/x.git'; cat $O/pieces-lignes.txt
    echo "# marque $2"
    echo 'echo "STUB-RAN src=${BASH_SOURCE[0]} H0=${H0_PREVU:-absent} jeton_long=${#JETON_DEMARRAGE}"'
    echo 'echo "STUB-SHA $(sha256sum < "${BASH_SOURCE[0]}" | cut -c1-64)"'
    echo 'exit 7'; } > $1
}
mkdir -p $O/st1 $O/st2
mkstub $O/st1/stub.sh A
mkstub $O/st2/stub.sh B   # une marque de plus ; meme longueur
export JFACT=$(head -c 300 /dev/urandom | base64 -w0 | tr -dc 'A-Za-z0-9' | head -c 60)
fab() {  # $1 stub ; $2 sortie
  FABRICANT_BANC=oui FABRICANT_SCRIPT=$1 FABRICANT_DEPOT_DISTANT=$O/distant.git bash $O/fab/fab.sh JFACT $2 > $2.log 2>&1 || { echo "fabricant en echec pour $1"; cat $2.log; exit 1; }
}
fab $O/st1/stub.sh $O/s/ud1
fab $O/st2/stub.sh $O/s/ud2
E1=$(sha256sum < $O/st1/stub.sh | cut -c1-64)
echo "E_SCRIPT du stub A : $E1" >> $T
N=$(wc -l < $O/s/ud1)   # derniere ligne = charge
sed -n "$((N)),\$p" $O/s/ud2 > $O/charge2.txt
sed -n "$((N)),\$p" $O/s/ud1 > $O/charge1.txt
head -n $((N-1)) $O/s/ud1 > $O/tete1.txt
L4=$(sed -n 4p $O/s/ud1)
echo "forme : ligne 4 = $L4 ; charge sur ligne $N" >> $T

run() {  # $1 nom ; $2 fichier de donnees ; $3 attendu ; reste : variables d'environnement additionnelles
  local nom=$1 f=$2 att=$3 c out
  rm -rf $O/run/$nom;
  out=$(ESSAI_DEMARRAGE_CHARGE=$O/run/$nom bash $f 2>&1); c=$?
  echo "$nom | attendu $att | rendu $c | $(echo "$out" | tr '\n' ' ' | cut -c1-230)" >> $T
}
# M0 sain, puis 2e execution
run m0-sain $O/s/ud1 7
out=$(ESSAI_DEMARRAGE_CHARGE=$O/run/m0-sain bash $O/s/ud1 2>&1); c=$?
echo "m0b-seconde-execution (charge deja la) | attendu 20 | rendu $c | $(echo $out | cut -c1-150)" >> $T
# M1 script altere d'un octet dans la charge (E_SCRIPT du stub A, charge du stub B)
{ cat $O/tete1.txt; cat $O/charge2.txt; } > $O/s/m1.txt
run m1-script-altere-1-octet $O/s/m1.txt 18
# M2 charge tronquee de plusieurs façons
for k in 1 4 8 100 400; do
  { cat $O/tete1.txt; head -c -$((k+1)) $O/charge1.txt; echo; } > $O/s/m2-$k.txt
  run m2-charge-tronquee-de-$k $O/s/m2-$k.txt 18
done
{ cat $O/tete1.txt; head -c 120 $O/charge1.txt; echo; } > $O/s/m2-court.txt
run m2-charge-120-signes $O/s/m2-court.txt 18
# M3 E_SCRIPT faux
sed '4s/^E_SCRIPT=./E_SCRIPT=0/' $O/s/ud1 > $O/s/m3.txt
run m3-E_SCRIPT-faux $O/s/m3.txt 18
# M4 E_SCRIPT absent (ligne supprimee)
sed '4d' $O/s/ud1 > $O/s/m4.txt
run m4-E_SCRIPT-absent $O/s/m4.txt 18
# M5 E_SCRIPT vide
sed '4s/.*/E_SCRIPT=/' $O/s/ud1 > $O/s/m5.txt
run m5-E_SCRIPT-vide $O/s/m5.txt 18
# M6 pas de charge (marqueur en dernier)
head -n $((N-1)) $O/s/ud1 > $O/s/m6.txt
run m6-sans-charge $O/s/m6.txt 18
# M7 pas de marqueur
head -n $((N-2)) $O/s/ud1 > $O/s/m7.txt; cat $O/charge1.txt >> $O/s/m7.txt
run m7-sans-marqueur $O/s/m7.txt 18
# M8 un signe change au milieu de la charge (base64)
python3 -I $W/outils/muter.py $O/charge1.txt $O/charge1-mut.txt 200
{ cat $O/tete1.txt; cat $O/charge1-mut.txt; } > $O/s/m8.txt
run m8-signe-change-dans-charge $O/s/m8.txt 18
# M9 charge gzip valide sans le script de demarrage (4 pieces seulement), E_SCRIPT bon, puis E_SCRIPT vide
mkdir -p $O/x; tar -xzf <(sed -n "$N p" $O/s/ud1 | base64 -d) -C $O/x 2>/dev/null
rm -f $O/x/demarrage-machine-essai-3-v3.sh
tar -czf $O/sans-script.tgz -C $O/x . ; { cat $O/tete1.txt; base64 -w0 $O/sans-script.tgz; echo; } > $O/s/m9.txt
run m9-charge-sans-script $O/s/m9.txt 18
sed '4s/.*/E_SCRIPT=/' $O/s/m9.txt > $O/s/m9b.txt
run m9b-charge-sans-script-et-E_SCRIPT-vide $O/s/m9b.txt "18 (souhaite)"
# M10 CHARGE = lien pendant
rm -rf $O/run/m10; ln -s $O/run/pendant $O/run/m10
out=$(ESSAI_DEMARRAGE_CHARGE=$O/run/m10 bash $O/s/ud1 2>&1); c=$?
echo "m10-charge-lien-pendant | attendu 18 ou 20 (jamais suivre) | rendu $c | $(echo $out | cut -c1-150) | cible creee : $([ -e $O/run/pendant ] && echo oui || echo non)" >> $T
rm -f $O/run/m10
# M11 apres un echec 18, nouvelle execution
rm -rf $O/run/m11
ESSAI_DEMARRAGE_CHARGE=$O/run/m11 bash $O/s/m1.txt > /dev/null 2>&1; c1=$?
ESSAI_DEMARRAGE_CHARGE=$O/run/m11 bash $O/s/ud1 > /dev/null 2>&1; c2=$?
echo "m11-reprise-apres-18 (donnees saines) | attendu note | rendu premiere $c1 puis seconde $c2 ; dossier laisse : $(ls $O/run/m11 | wc -l) entrees" >> $T
# M12 script REEL (p4) : les portes d'essai sans banc doivent refuser en 19 (aucun /srv/essai-3 cree)
echo "avant : /srv/essai-3 $([ -e /srv/essai-3 ] && echo present || echo absent)" >> $T
rm -rf $O/run/m12
out=$(ESSAI_DEMARRAGE_CHARGE=$O/run/m12 bash $W/tmp/p4/s/ud 2>&1); c=$?
echo "m12-script-reel-porte-sans-banc | attendu 19 | rendu $c | $(echo $out | cut -c1-150)" >> $T
echo "apres : /srv/essai-3 $([ -e /srv/essai-3 ] && echo present || echo absent)" >> $T
