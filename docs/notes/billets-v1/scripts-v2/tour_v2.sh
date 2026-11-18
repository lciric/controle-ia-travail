#!/bin/bash
# usage : tour_v2.sh AN  -> avance l'appariement et affiche les candidats à lire
cd /home/user/controle-ia-travail/docs/notes/billets-v1/scripts-v2
python3 apparier_v2.py tour $1
python3 lire_v2.py $(tr ' ' '\n' </tmp/alire.txt | sort -u | tr '\n' ' ') | cut -c1-${2:-400}
python3 -c "import json;print(json.load(open('/tmp/alire_map.json')))"
