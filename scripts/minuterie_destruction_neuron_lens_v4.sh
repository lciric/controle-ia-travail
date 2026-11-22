#!/usr/bin/env bash
# Minuterie de destruction par identifiant d'instance pour la course de la tranche B-α de « Neuron Lens » — v4 (v3, borne haute portée à
# 129 600 s, soit 12 USD à 0,30 USD/h : devis B-α v2, § 3, m13 ; la v3 refusait au-delà de 108 000 s, soit un prix lu sous 0,40 USD/h).
# v3 : v2 + suivi v6, qui balaie avant
# de tronquer, et absence prouvée sur une liste non vide, `--non-vide` : contre-lecture 12, S-1 et S-6 ; une liste vide, même au code 0,
# n'est plus une preuve : échec fermé, code 6). v2 : v1 + destruction confirmée et
# vérifiée : l'outil du loueur 1.11.0 demande une confirmation [y/N], abandonne sans entrée et rend le code 0 — constaté le 14 novembre
# 2026 sur l'instance 60669495, journal de la course du volet A ; la v1 aurait écrit « destruction demandee » sans rien détruire).
# v2 : `destroy instance <ID> -y`, entrée fermée ; succès seulement si l'absence est prouvée par `suivi_vast_v6 absente <ID> --non-vide` (liste non vide lue
# sans erreur) ; sinon nouvel essai ; le code de sortie de l'outil n'est jamais pris pour une preuve.
#
# Usage : bash scripts/minuterie_destruction_neuron_lens_v4.sh <ID_INSTANCE> <DUREE_S> <CHEMIN_ABSOLU_DE_L_OUTIL> <FICHIER_PID>
# Lancée détachée (`setsid nohup … &`) ; elle écrit son propre PID (`$$`) dans FICHIER_PID : c'est ce PID que l'on vérifie vivant puis
# que l'on arrête (R10) ; l'arrêter avant l'échéance empêche la destruction. L'outil est appelé par son chemin absolu ; le suivi est
# joué avec l'interprète du dépôt (`SUIVI_PY`, défaut `<dépôt>/.venv/bin/python`) et `VASTAI_OUTIL` = ce chemin ; il exige
# `CONTROLE_IA_GITHUB_TOKEN_2` dans l'environnement hérité (balayage), sinon il refuse et la destruction compte comme non vérifiée.
# Sorties de l'outil jetées. Codes : 2 identifiant invalide ; 3 durée hors bornes [BORNE_MIN_S, BORNE_MAX_S] (défaut 600 à 129600 s) ;
# 4 outil non absolu ou non exécutable, ou interprète du suivi absent ; 5 fichier PID impossible ; 6 destruction non vérifiée après 3
# essais. Bornes et attente entre essais (ATTENTE_S, 30) réglables pour l'essai seulement ; la commande ne les règle pas.
set -u
ID=${1:-}; D=${2:-}; OUTIL=${3:-}; FPID=${4:-}
MIN=${BORNE_MIN_S:-600}; MAX=${BORNE_MAX_S:-129600}; ATTENTE=${ATTENTE_S:-30}
DEPOT=$(cd "$(dirname "$0")/.." && pwd)
SUIVI_PY=${SUIVI_PY:-$DEPOT/.venv/bin/python}
log() { echo "MINUTERIE $(date -u +%FT%TZ) $*"; }
[[ "$ID" =~ ^[0-9]+$ ]] || { log "identifiant invalide : '$ID'"; exit 2; }
if ! [[ "$D" =~ ^[0-9]+$ ]] || [ "$D" -lt "$MIN" ] || [ "$D" -gt "$MAX" ]; then
  log "duree hors bornes : '$D' (bornes $MIN a $MAX s) ; minuterie NON armee"; exit 3
fi
case "$OUTIL" in /*) ;; *) log "chemin de l'outil non absolu : '$OUTIL' ; minuterie NON armee"; exit 4 ;; esac
[ -x "$OUTIL" ] || { log "outil non executable : $OUTIL ; minuterie NON armee"; exit 4; }
[ -x "$SUIVI_PY" ] || { log "interprete du suivi absent : $SUIVI_PY ; minuterie NON armee"; exit 4; }
[ -n "$FPID" ] && echo $$ > "$FPID" || { log "fichier PID impossible : '$FPID' ; minuterie NON armee"; exit 5; }
log "armee : instance $ID, destruction dans $D s, PID $$, outil $OUTIL"
sleep "$D"
log "echeance : destruction de l'instance $ID"
for i in 1 2 3; do
  "$OUTIL" destroy instance "$ID" -y > /dev/null 2>&1 < /dev/null
  sleep 5
  if env VASTAI_OUTIL="$OUTIL" PYTHONPATH="$DEPOT/src" "$SUIVI_PY" -m controle_ia.neuron_lens.suivi_vast_v6 absente "$ID" --non-vide > /dev/null 2>&1; then
    log "destruction verifiee (absence prouvee, essai $i/3)"; exit 0
  fi
  log "destruction non verifiee (essai $i/3)"
  [ "$i" -lt 3 ] && sleep "$ATTENTE"
done
log "DESTRUCTION EN ECHEC : instance $ID toujours presente ou absence non prouvee"
exit 6
