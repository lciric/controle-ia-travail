#!/bin/bash
# Surveillance du canal conv-audit → session-depot (R-905, consigne de Lazar 31 oct. : « garde-la pendant toute la durée de l'autonomie »).
# Émet une ligne par message nouveau (fichier messages/conv-audit_*_nNNN.md) et par branche canal/conv-audit* nouvelle ;
# état sur disque (aucune perte entre deux armements) ; miroir nu à part (aucun verrou partagé avec le dépôt de travail).
S=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/surveillance-canal-v1
M=$S/miroir.git; B=canal/conv-audit-n04; echecs=0
while true; do
  if L=$(git -C "$M" ls-remote --heads origin 2>/dev/null); then
    echecs=0
    echo "$L" | awk '{print $2}' | grep 'refs/heads/canal/conv-audit' | sort > "$S/branches-maintenant.txt"
    comm -13 "$S/branches-vues.txt" "$S/branches-maintenant.txt" | sed 's#refs/heads/##; s#^#NOUVELLE BRANCHE conv-audit : #'
    sort -u "$S/branches-vues.txt" "$S/branches-maintenant.txt" -o "$S/branches-vues.txt"
    if git -C "$M" fetch -q --filter=blob:none origin "+refs/heads/$B:refs/heads/$B" 2>/dev/null; then
      git -C "$M" ls-tree -r --name-only "$B" | grep -E 'messages/conv-audit_[0-9-]+_n[0-9]+\.md$' | sort > "$S/messages-maintenant.txt"
      comm -13 "$S/messages-vus.txt" "$S/messages-maintenant.txt" | sed -E 's#^(.*_n([0-9]+)\.md)$#NOUVEAU MESSAGE conv-audit n° \2 : \1#'
      sort -u "$S/messages-vus.txt" "$S/messages-maintenant.txt" -o "$S/messages-vus.txt"
    else
      echecs=$((echecs+1))
    fi
  else
    echecs=$((echecs+1))
  fi
  [ "$echecs" -eq 5 ] && echo "ÉCHEC DE LA SURVEILLANCE : 5 lectures du dépôt distant en échec d'affilée"
  sleep 60
done
