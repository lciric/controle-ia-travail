#!/bin/bash
# Contre-lecteur, question 4 : l'expression du script qui calcule l'heure d'arrêt (ligne 187 ; recopiée dans la fonction
# h_arret, et vérifiée présente dans la ligne 187 du script par grep) rend-elle H0_PREVU + 94 h, pour des H0_PREVU limites
# (changement d'année, jour bissextile, changements d'heure d'été) et sous plusieurs fuseaux (TZ) ? Comparaison au calcul
# indépendant de calcul-heure-arret.py (Python, sans `date`). Une ligne par couple, puis le total d'écarts.
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
SCRIPT=$ME/auteur/demarrage-machine-essai-3-v1.sh
PY=/home/user/controle-ia-travail/.venv/bin/python
EXPR='date -u -d "@$(( $(date -d $H0_PREVU +%s) + 94 * 3600 ))" +%Y-%m-%dT%H:%M:%SZ'
h_arret() { local H0_PREVU=$1; date -u -d "@$(( $(date -d $H0_PREVU +%s) + 94 * 3600 ))" +%Y-%m-%dT%H:%M:%SZ; }
echo "expression de la fonction présente dans la ligne 187 du script : $(sed -n 187p "$SCRIPT" | grep -c -F "$EXPR")"
ecarts=0; n=0
for H0 in 2026-11-21T20:12:03Z 2026-12-31T23:59:59Z 2028-02-27T12:00:00Z 2026-03-28T22:30:00Z 2026-10-24T20:00:00Z 2026-01-01T00:00:00Z; do
  ATT=$("$PY" -I "$ME/outils/calcul-heure-arret.py" "$H0")
  for tz in UTC Europe/Berlin America/Los_Angeles Pacific/Auckland Asia/Kolkata; do
    export TZ=$tz
    R=$(h_arret "$H0")
    n=$((n + 1))
    [ "$R" = "$ATT" ] || ecarts=$((ecarts + 1))
    echo "H0_PREVU $H0 ; TZ $tz ; script $R ; indépendant $ATT ; $([ "$R" = "$ATT" ] && echo ÉGAL || echo ÉCART)"
  done
done
unset TZ
echo "couples : $n ; écarts : $ecarts"
