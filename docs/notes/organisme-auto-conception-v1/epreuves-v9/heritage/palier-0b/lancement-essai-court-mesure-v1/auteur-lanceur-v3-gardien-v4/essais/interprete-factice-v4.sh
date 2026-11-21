#!/bin/bash
# Interprète factice v4 : passé au VRAI lanceur v3 comme INTERPRETE (copié, exécutable, sous un nom propre à chaque essai).
# Il n'exécute jamais le programme qu'on lui donne. Il écrit dans "$0.argv" ce qu'il reçoit : dossier courant, PYTHONPATH,
# puis chaque argument (le 0e est son propre chemin, l'interprète), un par ligne ; puis il remplace son processus (exec) par
# la commande factice lue dans "$0.args" (un argument par ligne), ou rend 0 si ce fichier est vide ou absent.
{
  printf 'cwd=%s\n' "$PWD"
  printf 'PYTHONPATH=%s\n' "${PYTHONPATH-(absent)}"
  printf 'arg=%s\n' "$0" "$@"
} > "$0.argv"
if [ ! -s "$0.args" ]; then
  exit 0
fi
mapfile -t CMD < "$0.args"
exec "${CMD[@]}"
