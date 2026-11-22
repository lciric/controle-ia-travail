#!/bin/bash
# Guet : attend qu'un fichier existe et ne soit pas vide (au plus N secondes). Usage : guetter.sh FICHIER N
for i in $(seq 1 $2); do [ -s "$1" ] && { echo "present apres $i s"; exit 0; }; sleep 1; done
echo "absent apres $2 s"; exit 1
