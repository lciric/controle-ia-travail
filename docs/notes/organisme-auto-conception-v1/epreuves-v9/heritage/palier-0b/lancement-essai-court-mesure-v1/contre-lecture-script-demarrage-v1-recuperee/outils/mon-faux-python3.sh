#!/bin/bash
# Contre-lecteur : faux python3 du système (comme celui de l'auteur), mais le faux environnement porte MON faux programme et
# MON faux pip. Tout autre appel passe au vrai interpréteur (le gardien est lu par lui).
ICI=$(cd "$(dirname "$0")" && pwd)
VRAI=/home/user/controle-ia-travail/.venv/bin/python
if [ "${1:-}" = -m ] && [ "${2:-}" = venv ]; then
  echo "faux python3 : venv $3" >> "${FAUX_JOURNAL:-/dev/null}"
  mkdir -p "$3/bin" && cp "$ICI/mon-faux-programme.sh" "$3/bin/python" && cp "$ICI/mon-faux-pip.sh" "$3/bin/pip" \
    && chmod 755 "$3/bin/python" "$3/bin/pip"
  exit $?
fi
exec "$VRAI" "$@"
