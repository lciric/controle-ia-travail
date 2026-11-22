#!/bin/bash
# Faux apt-get : écrit ses arguments dans $FAUX_JOURNAL ; échoue (100) si FAUX_APT_ECHEC est non vide.
echo "faux apt-get : $*" >> "${FAUX_JOURNAL:-/dev/null}"
[ -z "${FAUX_APT_ECHEC:-}" ] || { echo "faux apt-get : échec voulu" >&2; exit 100; }
exit 0
