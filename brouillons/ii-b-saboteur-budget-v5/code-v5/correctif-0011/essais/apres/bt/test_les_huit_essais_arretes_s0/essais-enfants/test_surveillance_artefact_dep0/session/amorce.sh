#!/usr/bin/env bash
# commentaire : controle_ia.iib.lanceur_v5 --phase autre --config x
PYTHONPATH=src python -m controle_ia.iib.lanceur_v5 --phase etalonnage --config "$CONFIG" --run-id "$RUN" &
