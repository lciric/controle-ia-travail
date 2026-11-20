#!/bin/bash
# Usage : bash creer_b5f.sh N   — crédit ≥ 5, recherche, choix mécanique, commande du lanceur, joueur, garde ; NE JOUE PAS.
set -euo pipefail
S=/tmp/claude-0/-home-user-controle-ia-travail/2e5ab823-f39e-5eb7-8014-a7e033a3a8e4/scratchpad
N=$1; cd "$S"; V="$S/venv-vast/bin/vastai"; P="$S/venv-b5f/bin/python"
I=$(date -u +%Y%m%dT%H%M%SZ)
$V show user --raw > b5f/credit-$I.json 2>/dev/null
C=$(python3 -I -c "import json,sys;print(float(json.load(open(sys.argv[1]))['credit']))" b5f/credit-$I.json)
echo "crédit $C"
python3 -I -c "import sys; sys.exit(0 if float(sys.argv[1])>=5 else 3)" "$C" || { echo "crédit sous 5 USD : rien"; exit 3; }
$V search offers 'gpu_name=A100_SXM4 num_gpus=1 gpu_ram>=80 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 cuda_max_good>=13.0 dph_total<=1.30 rentable=true' -o 'dph_total' --raw > b5f/offres-$I.json 2> b5f/offres-$I.err
python3 -I -c 'import json,sys
d=json.load(open(sys.argv[1])); d=d.get("offers",d) if isinstance(d,dict) else d
u={l.strip() for l in open(sys.argv[2]) if l.strip()}
k=[x for x in d if str(x.get("id")) not in u]; print("offres déjà prises retirées :", len(d)-len(k))
json.dump(k,open(sys.argv[3],"x"))' b5f/offres-$I.json b5f/offres-utilisees.txt b5f/offres-$I-libres.json
$P -I outils/choisir_offre_b5f.py "$S/arbre-course" b5f/offres-$I-libres.json b5f/offre-$N-$I.json
RUN=$(date -u +%Y%m%d-%H%M%S)-b5f-formation-$N; echo "$RUN" > b5f/run-$N.txt
PYTHON_B5F=$P GO_ID=GO-2026-11-19-86 bash arbre-course/scripts/lancer_b5f_formation_v1.sh commande "$S/arbre-course" $N "$S/b5f/offre-$N-$I.json" 31fca83b0c26cd035fe9e660d123e690a41b6271 course/barreau5-formation-v1 prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md "$RUN" > b5f/commande-$N.txt 2> b5f/commande-$N.err
$P -I outils/faire_joueur.py b5f/commande-$N.txt b5f/jouer-creation-$N.sh "$S/venv-vast/bin"
python3 -I outils/essai_garde3.py /home/user/controle-ia-travail b5f/jouer-creation-$N.sh | tee /dev/stderr | grep -qx "garde : accepté"
echo "prêt : b5f/jouer-creation-$N.sh ; run $RUN ; offre b5f/offre-$N-$I.json"
