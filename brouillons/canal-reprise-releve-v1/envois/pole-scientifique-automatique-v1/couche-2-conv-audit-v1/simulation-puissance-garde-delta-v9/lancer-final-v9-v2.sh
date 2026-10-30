#!/bin/sh
# v9 : fin de chaîne, version 2 (la version 1, `lancer-final-v9.sh`, écrivait son journal dans le dossier pendant le scellement : échec gardé sous `-echec1`) ;
# journal à écrire HORS du dossier, puis à verser sous lancer-final-v9-v2-journal.txt ; depuis le dossier v9 (après tous les passages et `tableaux-v9.py`).
#   COMMIT=… sh lancer-final-v9.sh
# 1. compagnon .sha256 pour tout fichier qui n'en a pas (sous-dossiers compris ; un compagnon existant n'est jamais réécrit) ;
# 2. manifeste d'ensemble (assembler-manifeste-v9.py), puis son compagnon ;
# 3. rapport depuis le gabarit (construire-rapport-v9.py, qui refuse si un compagnon manque ou diffère), puis compagnons du rapport et de son manifeste.
set -eu
COMMIT="${COMMIT:?COMMIT absent}"
sceller() {
  find . -type f ! -name '*.sha256' | sort | while read -r f; do
    if [ ! -e "$f.sha256" ]; then (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); fi
  done
}
sceller
python3 -I -B assembler-manifeste-v9.py "$COMMIT" manifeste-puissance-garde-delta-v9.json
sceller
python3 -I -B construire-rapport-v9.py "$COMMIT" rapport-v9-gabarit-v2.md tableaux-v9.md rapport-puissance-garde-delta-v9.md
sceller
find . -type f -name '*.sha256' | sort | while read -r c; do (cd "$(dirname "$c")" && sha256sum -c --quiet "$(basename "$c")") || echo "ÉCART : $c"; done
echo "fin : $(find . -type f ! -name '*.sha256' | wc -l) fichiers, $(find . -type f -name '*.sha256' | wc -l) compagnons"
