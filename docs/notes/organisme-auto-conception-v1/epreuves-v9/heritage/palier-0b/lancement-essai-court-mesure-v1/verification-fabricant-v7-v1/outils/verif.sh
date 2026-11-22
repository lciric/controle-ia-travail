#!/bin/bash
# Banc du vérificateur : fabricant v7 épinglé. Tout en dépôt FACTICE local et jeton FACTICE.
set -u
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verification-fabricant-v7
FAB=$W/fab
T=$W/tables/table-cas.txt
OUT=$W/tables/sorties
rm -rf "$OUT" "$W/depot-vide.git" "$W/entrees" "$W/prod"
mkdir -p "$OUT" "$W/entrees" "$W/prod"
git init -q --bare "$W/depot-vide.git"
: > "$T"
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$W/depot-vide.git
JF40=FACTICE_ESSAI_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
JF100=$(printf 'Z%.0s' $(seq 1 100))
SCR=$FAB/demarrage-machine-essai-3-v6.sh
# entrées
cat "$SCR" "$FAB/essais-outils/queue-a2-chaine.txt" > "$W/entrees/a2.sh"
sed '' "$SCR" > "$W/entrees/copie-identique-autre-chemin.sh"
{ cat "$SCR"; echo "# ajout"; } > "$W/entrees/un-commentaire-ajoute.sh"
sed 's/^set -u/set -U/;t;' "$SCR" > "$W/entrees/set-U.sh"
cmp "$SCR" "$W/entrees/set-U.sh" > /dev/null 2>&1 && echo "set-U identique au script (sans effet)" >> "$T"
# un octet : dernier caractere du fichier changé en place (substitution d'une lettre de la première ligne de code)
sed '3s/./X/' "$SCR" > "$W/entrees/un-octet-ligne3.sh"
echo "octets différents un-octet-ligne3 : $(cmp -l "$SCR" "$W/entrees/un-octet-ligne3.sh" | wc -l)" >> "$T"

cas() { # nom attendu jeton script|- reducteurmode|reel fabricant [arg3]
  local nom=$1 att=$2 jt=$3 s=$4 m=$5 fb=$6 a3=${7:-} x=() o=$OUT/$1 r code
  [ "$s" = - ] || x+=(FABRICANT_SCRIPT=$s)
  [ "$m" = reel ] || x+=(FABRICANT_REDUCTEUR=$FAB/essais-outils/reducteur-artefact.sh REDUCTEUR_MODE=$m)
  if [ -n "$a3" ]; then
    r=$(env "${x[@]}" JETON_FACTICE_ESSAI="$jt" /bin/bash "$FAB/$fb" JETON_FACTICE_ESSAI "$o" "$a3" 2>&1); code=$?
  else
    r=$(env "${x[@]}" JETON_FACTICE_ESSAI="$jt" /bin/bash "$FAB/$fb" JETON_FACTICE_ESSAI "$o" 2>&1); code=$?
  fi
  printf '%s\n' "$r" > "$OUT/sortie-$nom.txt"
  local n; n=$(ls "$OUT" | grep -c -F "$nom" )
  echo "$nom : attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ECHEC) ; fichiers (hors sortie-$nom.txt) : $((n-1)) ; $(printf '%s\n' "$r" | grep -m1 '^refus' | cut -c1-170)" >> "$T"
}
cas R1-un-octet-ligne3 9 $JF40 "$W/entrees/un-octet-ligne3.sh" reel fabriquer-donnees-demarrage-v7.sh
cas R1b-commentaire-ajoute 9 $JF40 "$W/entrees/un-commentaire-ajoute.sh" reel fabriquer-donnees-demarrage-v7.sh
cas R2-reducteur-garde-commentaire 9 $JF40 - garde-ligne-2 fabriquer-donnees-demarrage-v7.sh
cas R3-A2-chaine-reducteur-naif 9 $JF40 "$W/entrees/a2.sh" naif fabriquer-donnees-demarrage-v7.sh
cas R3b-A2-chaine-reducteur-reel 9 $JF40 "$W/entrees/a2.sh" reel fabriquer-donnees-demarrage-v7.sh
cas R4-reducteur-ligne-1 9 $JF40 - ligne-1 fabriquer-donnees-demarrage-v7.sh
cas R5-reducteur-modifie 9 $JF40 - modifie fabriquer-donnees-demarrage-v7.sh
cas R6-troisieme-argument-faux 5 $JF40 - reel fabriquer-donnees-demarrage-v7.sh 0000000000000000000000000000000000000000000000000000000000000000
cas T1-temoin-v6-sur-un-octet-ligne3 "?" $JF40 "$W/entrees/un-octet-ligne3.sh" reel fabriquer-donnees-demarrage-v6.sh
cas T2-temoin-v6-sur-A2-reducteur-naif 0 $JF40 "$W/entrees/a2.sh" naif fabriquer-donnees-demarrage-v6.sh
rm -f "$OUT"/T2-temoin-v6-sur-A2-reducteur-naif*[!t] 2>/dev/null
# sain : v6 et v7 en meme seconde
for k in 1 2 3 4 5 6; do
  rm -f "$W/prod"/*
  JETON_FACTICE_ESSAI=$JF40 /bin/bash "$FAB/fabriquer-donnees-demarrage-v6.sh" JETON_FACTICE_ESSAI "$W/prod/v6" > "$W/prod/sortie-v6.out" 2>&1 &
  P6=$!
  JETON_FACTICE_ESSAI=$JF40 /bin/bash "$FAB/fabriquer-donnees-demarrage-v7.sh" JETON_FACTICE_ESSAI "$W/prod/v7" > "$W/prod/sortie-v7.out" 2>&1
  c7=$?
  wait $P6; c6=$?
  [ "$(sed -n 2p "$W/prod/v6")" = "$(sed -n 2p "$W/prod/v7")" ] && break
done
echo "S1 sain jeton 40 : essai $k ; codes v6 $c6 v7 $c7 ; H0 v6 $(sed -n 2p "$W/prod/v6") v7 $(sed -n 2p "$W/prod/v7")" >> "$T"
for x in "" .sans-jeton .charge.b64 .script-reduit.sh; do
  cmp -s "$W/prod/v6$x" "$W/prod/v7$x" && echo "  v6/v7$x : IDENTIQUES $(sha256sum < "$W/prod/v7$x" | cut -c1-16)" >> "$T" || echo "  v6/v7$x : DIFFERENTES" >> "$T"
done
sed -n 's/^\(taille en lecture stricte\|information\|script de démarrage\).*//p' /dev/null
cp_=$W/tables/empreintes-v7-jeton40.txt
sed '' "$W/prod/v7.empreintes.txt" > "$cp_"
# charge : texte haché = texte dans la charge ?
mkdir -p "$W/prod/ext"
sed -n '/^__CHARGE_DES_PIECES__$/,$p' "$W/prod/v7" | sed 1d | base64 -d | tar -xz -C "$W/prod/ext"
echo "S1c script dans la charge : $(sha256sum < "$W/prod/ext/demarrage-machine-essai-3-v6.sh" | cut -c1-64) ; E_SCRIPT de la ligne : $(grep -m1 '^E_SCRIPT=' "$W/prod/v7")" >> "$T"
echo "S1d jeton factice dans autres fichiers que la sortie : $(grep -l -F "$JF40" "$W/prod"/v7.* "$W/prod"/sortie-v7.out 2>/dev/null | wc -l) ; dans la sortie : $(grep -c -F "$JF40" "$W/prod/v7")" >> "$T"
rm -rf "$W/prod"; mkdir -p "$W/prod"
# jeton 100
JETON_FACTICE_ESSAI=$JF100 /bin/bash "$FAB/fabriquer-donnees-demarrage-v7.sh" JETON_FACTICE_ESSAI "$W/prod/v7" > "$W/prod/sortie-v7.out" 2>&1
echo "S2 jeton 100 : code $? ; $(grep -h 'lecture stricte' "$W/prod/sortie-v7.out") ; $(grep -h 'HTML de Go' "$W/prod/sortie-v7.out") ; E_SCRIPT $(grep -m1 '^E_SCRIPT=' "$W/prod/v7") ; jeton 100 dans la sortie : $(grep -c -F "$JF100" "$W/prod/v7") ; hors sortie : $(grep -l -F "$JF100" "$W/prod"/v7.* "$W/prod"/sortie-v7.out 2>/dev/null | wc -l)" >> "$T"
/home/user/controle-ia-travail/.venv/bin/python -I "$FAB/essais-outils/tailles-json.py" "$W/prod/v7" 100 > "$W/tables/tailles-json-v7-jeton100.txt"
# bypass : amorce modifiée (non épinglée)
mkdir -p "$W/fab2"
rm -f "$W/prod"/*
for f in fabriquer-donnees-demarrage-v7.sh demarrage-machine-essai-3-v6.sh reduire-script-v6.py; do sed '' "$FAB/$f" > "$W/fab2/$f"; done
{ sed '' "$FAB/amorce-demarrage-essai-3-v6.sh"; } > "$W/fab2/amorce-demarrage-essai-3-v6.sh"
# insérer, avant le repère de charge ? l'amorce est copiée de la ligne 3 à la fin : une ligne E_SCRIPT=... en ligne 3 l'emporte
sed -i '3s/^/E_SCRIPT=0000000000000000000000000000000000000000000000000000000000000000\n/' "$W/fab2/amorce-demarrage-essai-3-v6.sh"
JETON_FACTICE_ESSAI=$JF40 /bin/bash "$W/fab2/fabriquer-donnees-demarrage-v7.sh" JETON_FACTICE_ESSAI "$W/prod/b1" > "$W/prod/sortie-b1.out" 2>&1
echo "B1 amorce modifiée (E_SCRIPT recopié) : code $? ; lignes E_SCRIPT= dans les données : $(grep -n '^E_SCRIPT=' "$W/prod/b1" | cut -c1-40 | tr '\n' ' ')" >> "$T"
rm -rf "$W/prod" "$W/fab2"
# réglage sans banc
( unset FABRICANT_BANC; FABRICANT_SCRIPT=$SCR JETON_FACTICE_ESSAI=$JF40 /bin/bash "$FAB/fabriquer-donnees-demarrage-v7.sh" JETON_FACTICE_ESSAI "$W/zz" > "$OUT/sortie-sans-banc.txt" 2>&1; echo "R7 FABRICANT_SCRIPT sans banc : attendu 2 ; rendu $?" >> "$T"; ls "$W" | grep -c '^zz' >> "$T" )
cat "$T"
