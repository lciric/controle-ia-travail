#!/bin/bash
# Faux python3 du système. « -m venv DOSSIER » : fabrique un faux environnement (bin/python = faux programme du palier 0b,
# bin/pip = faux pip) ; échoue si FAUX_VENV_ECHEC est non vide. Tout autre appel passe au vrai interpréteur (le gardien
# est lu par lui).
ICI=$(cd "$(dirname "$0")" && pwd)
VRAI=/home/user/controle-ia-travail/.venv/bin/python
if [ "${1:-}" = -m ] && [ "${2:-}" = venv ]; then
  echo "faux python3 : venv $3" >> "${FAUX_JOURNAL:-/dev/null}"
  [ -z "${FAUX_VENV_ECHEC:-}" ] || exit 1
  mkdir -p "$3/bin" && cp "$ICI/faux-programme.sh" "$3/bin/python" && cp "$ICI/faux-pip.sh" "$3/bin/pip" \
    && chmod 755 "$3/bin/python" "$3/bin/pip"
  exit $?
fi
exec "$VRAI" "$@"
