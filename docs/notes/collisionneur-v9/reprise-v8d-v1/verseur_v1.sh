#!/bin/bash
# Verse et pousse toutes les 5 minutes l'état des courses (runs/, journaux, essaim), tant qu'un enchaîneur tourne, puis une dernière fois.
cd /home/user/controle-ia-travail
verse() {
  git add -A runs/ docs/notes/collisionneur-v9 registres/essaim >/dev/null 2>&1
  git diff --cached --quiet && return
  git commit -q -m "Versement automatique de l'état des courses ($(date -u +%FT%TZ))

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Qi7Gr3DGEqBa9aU5gnT2eS" >/dev/null 2>&1
  for i in 1 2 3 4; do git push -q origin runs/collisionneurs-reprise-v8d-v1 >/dev/null 2>&1 && break; sleep $((2**i)); done
}
while pgrep -f "enchaine_v[234].sh" >/dev/null; do verse; sleep 300; done
verse
