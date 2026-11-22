#!/bin/bash
# Banc v5, R1 : sonde du groupe de controle cgroup v2 du banc. Cree un groupe sous RACINE, y fait entrer un sous-shell qui
# lance un enfant, lequel lance un descendant dans une session neuve (setsid) puis meurt ; controle que le descendant est
# membre du groupe ; arrete par cgroup.kill ; controle que le groupe est vide ; le retire. Ecrit le relevé sur la sortie.
# Emploi : sonde-cgroupe.sh RACINE_CGROUP2 NOM
set -u
G=$1/$2
echo "racine : $1 ; type : $(stat -f -c %T "$1")"
[ ! -e "$G" ] || { echo "refus : $G existe"; exit 1; }
mkdir "$G" || { echo "creation de $G : refusee"; exit 2; }
echo "groupe cree : $G ; fichiers cgroup.kill $( [ -f $G/cgroup.kill ] && echo present || echo absent ), cgroup.procs $( [ -f $G/cgroup.procs ] && echo present || echo absent )"
F=$(mktemp)
( echo $BASHPID > "$G/cgroup.procs" || { echo "inscription refusee"; exit 3; }
  ( setsid sleep 300 < /dev/null > /dev/null 2>&1 & echo "$!" > "$F" )
  exec sleep 300 ) &
M=$!
for i in $(seq 1 100); do [ -s "$F" ] && break; sleep 0.05; done
E=$(cat "$F"); rm -f "$F"
s=$(cat /proc/$E/stat); a=(${s##*) })
echo "sous-shell entre : $M ; descendant en session neuve, pere mort : $E (parent ${a[1]}, session ${a[3]}, groupe ${a[2]})"
echo "membres : $(tr '\n' ' ' < $G/cgroup.procs)"
grep -qx "$E" "$G/cgroup.procs" && echo "descendant membre du groupe : oui" || echo "descendant membre du groupe : NON"
echo 1 > "$G/cgroup.kill" && echo "cgroup.kill ecrit"
for i in $(seq 1 100); do [ -z "$(cat $G/cgroup.procs)" ] && break; sleep 0.05; done
wait "$M" 2>/dev/null
x=$(cat /proc/$E/stat 2>/dev/null) && a=(${x##*) }) || a=(absent)
echo "membres apres arret : [$(tr '\n' ' ' < $G/cgroup.procs)] ; descendant $E : etat ${a[0]} ($( [ "${a[0]}" = absent ] || [ "${a[0]}" = Z ] && echo mort || echo VIVANT ))"
rmdir "$G" && echo "groupe retire"
