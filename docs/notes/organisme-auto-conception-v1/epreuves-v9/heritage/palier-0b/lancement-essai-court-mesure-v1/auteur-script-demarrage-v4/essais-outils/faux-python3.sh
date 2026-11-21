#!/bin/bash
# Faux python3 du système. « -m venv DOSSIER » : fabrique un faux environnement (bin/python = faux programme du palier 0b,
# bin/pip = faux pip) ; échoue si FAUX_VENV_ECHEC est non vide. Tout autre appel passe au vrai interpréteur (le gardien
# est lu par lui).
# v3 : artefact du point 2 : si FAUX_PY_GIT=RACINE et que l'appel est le contrôle seul des paramètres du gardien (le
# dernier pas du script avant le contrôle du .git qui précède « demarrer »), pose RACINE/.git avant de passer la main.
ICI=$(cd "$(dirname "$0")" && pwd)
VRAI=/home/user/controle-ia-travail/.venv/bin/python
if [ "${1:-}" = -m ] && [ "${2:-}" = venv ]; then
  echo "faux python3 : venv $3" >> "${FAUX_JOURNAL:-/dev/null}"
  [ -z "${FAUX_VENV_ECHEC:-}" ] || exit 1
  mkdir -p "$3/bin" && cp "$ICI/faux-programme.sh" "$3/bin/python" && cp "$ICI/faux-pip.sh" "$3/bin/pip" \
    && chmod 755 "$3/bin/python" "$3/bin/pip"
  exit $?
fi
if [ -n "${FAUX_PY_GIT:-}" ] && [[ " $* " = *gardien-essai-3-v4.py*--verifier-seulement* ]]; then
  mkdir -p "$FAUX_PY_GIT/.git" && echo "faux python3 : .git pose dans $FAUX_PY_GIT" >> "${FAUX_JOURNAL:-/dev/null}"
fi
exec "$VRAI" "$@"
