#!/bin/bash
# Veille du canal de dépôt : signale tout fichier neuf sous registres/essaim/vers-mere/ sur toute branche distante.
cd /home/user/controle-ia-travail || exit 1
ETAT=/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/veille-essaim/tetes.txt
[ -f "$ETAT" ] || git ls-remote --heads origin 2>/dev/null > "$ETAT"
while true; do
  git ls-remote --heads origin 2>/dev/null > "$ETAT.neuf" || { sleep 90; continue; }
  if [ -s "$ETAT.neuf" ]; then
    join -j 2 -a 2 -e VIDE -o 2.2,1.1,2.1 <(sort -k2 "$ETAT") <(sort -k2 "$ETAT.neuf") 2>/dev/null | while read ref vieux neuf; do
      [ "$vieux" = "$neuf" ] && continue
      b=${ref#refs/heads/}
      git fetch -q origin "+$ref:refs/remotes/origin/$b" 2>/dev/null || continue
      if [ "$vieux" = "VIDE" ]; then
        base=$(git merge-base refs/remotes/origin/main "$neuf" 2>/dev/null)
        [ -n "$base" ] && git diff --name-only --diff-filter=AM "$base" "$neuf" -- registres/essaim/vers-mere/ docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/messages-poste-vers-mere-d1a-v6/ 2>/dev/null | grep -v '\.sha256$' | sed "s|^|ESSAIM NEUF (branche neuve $b) : |"
      else
        git diff --name-only --diff-filter=AM "$vieux" "$neuf" -- registres/essaim/vers-mere/ docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/messages-poste-vers-mere-d1a-v6/ 2>/dev/null | grep -v '\.sha256$' | sed "s|^|ESSAIM NEUF ($b) : |"
      fi
    done
    mv "$ETAT.neuf" "$ETAT"
  fi
  sleep 90
done
