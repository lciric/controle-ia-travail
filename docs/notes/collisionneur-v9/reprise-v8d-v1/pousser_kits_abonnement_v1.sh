#!/bin/bash
# Pousse une branche orpheline kits-abonnement/<NOM>-<CID>-v1 par kit d'un tour (autorisation de Lazar,
# « je t'autorise à pousser des branches kits-abonnement/* ») ; un seul fichier texte-servi.md ; vérifie l'empreinte.
# Usage : pousser_kits_abonnement_v1.sh DOSSIER NOM PREFIXE_CELLULE (ex. E3-T3)
cd /home/user/controle-ia-travail
D=$1 N=$2 PRE=$3
for k in $D/abonnement/kits/$PRE-*; do
  c=$(basename $k); K=$k/texte-servi.md
  B=$(git hash-object -w $K); T=$(printf "100644 blob %s\ttexte-servi.md\n" $B | git mktree)
  C=$(git commit-tree $T -m "Kit de l'abonnement : $N, $c (texte servi seul)")
  BR=kits-abonnement/$N-$c-v1; ok=0
  for i in 1 2 3 4; do git push -q origin $C:refs/heads/$BR 2>/dev/null && ok=1 && break; sleep $((2**i)); done
  s1=$(git show $C:texte-servi.md | sha256sum | cut -c1-64); s2=$(sha256sum $K | cut -c1-64)
  [ "$s1" = "$s2" ] || { echo "ÉCART D'EMPREINTE $BR"; exit 3; }
  m=$(python3 -c "import json;f=json.load(open('$k/fiche.json'));print(f['modele'],f['effort'])")
  echo "$BR | ${C:0:8} | $m | ${s2:0:8}… | $(git show $C:texte-servi.md | wc -l) lignes | poussé $ok"
done
