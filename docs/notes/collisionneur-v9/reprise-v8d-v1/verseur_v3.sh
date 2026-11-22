#!/bin/bash
# Session des collisionneurs (nouveau compte) : verse et pousse toutes les 5 minutes l'état des courses (runs/, journaux),
# tant qu’un des enchaîneurs donnés (numéros de processus) tourne, puis une dernière fois. Contrairement au verseur v1, récupère et fusionne la branche
# distante avant chaque poussée (jamais de force, jamais de rebasage).
cd /home/user/controle-ia-travail
B=runs/collisionneurs-reprise-v8d-v1
verse() {
  git add -A runs/ docs/notes/collisionneur-v9/reprise-v8d-v1 >/dev/null 2>&1
  git diff --cached --quiet || git commit -q -m "Versement automatique de l'état des courses, nouveau compte ($(date -u +%FT%TZ))

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XJ6MgoBJJ7a48BuDDw2mDZ" >/dev/null 2>&1
  for i in 1 2 3 4; do
    if git fetch -q origin $B >/dev/null 2>&1 && ! git merge -q --no-edit FETCH_HEAD >/dev/null 2>&1; then
      git merge --abort >/dev/null 2>&1
      echo "$(date -u +%FT%TZ) fusion refusée (conflit) : poussée suspendue, rien n'est forcé" >> docs/notes/collisionneur-v9/reprise-v8d-v1/verseur-v2.log
      return
    fi
    git push -q origin $B >/dev/null 2>&1 && break; sleep $((2**i))
  done
}
vivant() { for p in "$@"; do kill -0 "$p" 2>/dev/null && return 0; done; return 1; }
while vivant "$@"; do verse; sleep 300; done
verse
