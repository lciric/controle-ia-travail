#!/bin/bash
# Faux pip : écrit ses arguments dans $FAUX_JOURNAL ; « install » échoue (1) si FAUX_PIP_ECHEC est non vide.
echo "faux pip : $*" >> "${FAUX_JOURNAL:-/dev/null}"
if [ "${1:-}" = install ] && [ -n "${FAUX_PIP_ECHEC:-}" ]; then echo "faux pip : échec voulu" >&2; exit 1; fi
# artefact : altère un fichier de la racine après le contrôle du pas (c) (FAUX_PIP_ALTERER = chemin)
if [ "${1:-}" = install ] && [ -n "${FAUX_PIP_ALTERER:-}" ]; then echo "x" >> "$FAUX_PIP_ALTERER"; fi
exit 0
