#!/bin/bash
# Sonde : le banc peut-il creer un groupe sous /sys/fs/cgroup/unified, avec cgroup.kill, y inscrire un processus ?
G=/sys/fs/cgroup/unified/ca-sonde-v6
mkdir $G && echo "mkdir ok"
ls $G | tr '\n' ' '; echo
[ -f $G/cgroup.kill ] && echo "cgroup.kill present"
sleep 30 &
P=$!
echo $P > $G/cgroup.procs && echo "inscription ok : $(cat $G/cgroup.procs)"
echo 1 > $G/cgroup.kill && echo "kill ecrit"
for i in $(seq 1 50); do [ -z "$(cat $G/cgroup.procs)" ] && break; sleep 0.1; done
echo "membres apres : [$(cat $G/cgroup.procs)]"
wait $P 2>/dev/null
rmdir $G && echo "groupe retire"
