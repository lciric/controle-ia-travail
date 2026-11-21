#!/bin/bash
# Contre-lecteur : faux python3 pour l'artefact « le lanceur refuse au VRAI départ, alors que la vérification seule a passé ».
# Comme mon faux python3, mais à l'appel du gardien en --verifier-seulement (ligne 194 du script, après la vérification seule
# du lanceur et avant le départ), il crée le dossier des sorties (valeur de --sorties) : le lanceur refusera alors au départ
# (code 10, « dossier des sorties déjà présent »), presque aussitôt.
ICI=$(cd "$(dirname "$0")" && pwd)
VRAI=/home/user/controle-ia-travail/.venv/bin/python
if [ "${1:-}" = -m ] && [ "${2:-}" = venv ]; then
  mkdir -p "$3/bin" && cp "$ICI/mon-faux-programme.sh" "$3/bin/python" && cp "$ICI/mon-faux-pip.sh" "$3/bin/pip" \
    && chmod 755 "$3/bin/python" "$3/bin/pip"
  exit $?
fi
for a in "$@"; do [ "$a" = --verifier-seulement ] && VERIF=1; done
if [ "${VERIF:-}" = 1 ]; then
  prochain=
  for a in "$@"; do
    [ "$prochain" = 1 ] && { mkdir -p "$a"; echo "faux python3 : dossier des sorties créé : $a" >> "${FAUX_JOURNAL:-/dev/null}"; prochain=; }
    [ "$a" = --sorties ] && prochain=1
  done
fi
exec "$VRAI" "$@"
