#!/bin/bash
# Contre-lecteur, question 4 : par quelles voies le gardien peut-il recevoir une heure d'arrêt autre que H0_PREVU + 94 h ?
# Le gardien est joué en --verifier-seulement (il ne lit ni n'écrit rien), avec les paramètres que le script lui passe
# (--sorties, --heure-arret-duree, --arret-mesure desarme, --seuil-libre-octets 8000000000) suivis de OPT_GARDIEN, comme à
# la ligne 193 du script. Prédictions écrites avant : (1) reçue ; (2) la DERNIÈRE valeur l'emporte (argparse) ; (3) refusée
# (plus de 94 h 10 min) ; (4) acceptée (aucune borne basse : l'arrêt serait immédiat) ; (5) acceptée si OPT relève l'écart max.
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
PY=/home/user/controle-ia-travail/.venv/bin/python
G=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/gardien-essai-3-v4.py
T=$ME/resultats/tenue-bidon
mkdir -p "$T"
h() { date -u -d "$1" +%Y-%m-%dT%H:%M:%SZ; }
essai() {  # nom, puis la valeur de --heure-arret-duree, puis OPT_GARDIEN (mots)
  local nom=$1 hh=$2; shift 2
  local sortie code
  sortie=$("$PY" -I -B "$G" --tenue "$T" --sorties "$T/s" --heure-arret-duree "$hh" --arret-mesure desarme --seuil-libre-octets 8000000000 "$@" --verifier-seulement 2>&1)
  code=$?
  echo "$nom : code $code ; $(printf '%s' "$sortie" | tail -n 1 | cut -c1-150)"
}
A=$(h "+93 hours"); B=$(h "+1 hour"); C=$(h "+100 hours"); D=$(h "-100 hours"); E=$(h "+200 hours")
echo "maintenant $(h now) ; A=$A (+93 h) ; B=$B (+1 h) ; C=$C (+100 h) ; D=$D (-100 h) ; E=$E (+200 h)"
essai "(1) A seule" "$A"
essai "(2) A puis OPT « --heure-arret-duree B »" "$A" --heure-arret-duree "$B"
essai "(3) C seule" "$C"
essai "(4) D seule" "$D"
essai "(5) E avec OPT « --ecart-max-arret-duree-s 99999999 »" "$E" --ecart-max-arret-duree-s 99999999
essai "(6) abréviation « --heure-arret » dans OPT, valeur B" "$A" --heure-arret "$B"
