#!/bin/bash
# Faux python3 CL : comme celui de l'auteur, mais le faux pip du venv est le mien (faux-pip-cl.sh).
ICI=$(cd "$(dirname "$0")" && pwd)
AUT=$(dirname "$ICI")/aut/v2/essais/outils
VRAI=/home/user/controle-ia-travail/.venv/bin/python
if [ "${1:-}" = -m ] && [ "${2:-}" = venv ]; then
  echo "faux python3 CL : venv $3" >> "${FAUX_JOURNAL:-/dev/null}"
  mkdir -p "$3/bin" && cp "$AUT/faux-programme.sh" "$3/bin/python" && cp "$ICI/faux-pip-cl.sh" "$3/bin/pip" \
    && chmod 755 "$3/bin/python" "$3/bin/pip"
  exit $?
fi
exec "$VRAI" "$@"
