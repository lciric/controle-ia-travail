#!/bin/bash
# Contre-lecteur, question 4 : objet de contrôle FAUX par construction pour le comparateur de essai-q4-heure.sh. L'expression
# est volontairement fautive (le « Z » est retiré avant l'analyse : l'heure est alors lue dans le fuseau local, puis ré-écrite
# comme UTC). Le comparateur doit voir des écarts sous les fuseaux autres que UTC, et aucun sous UTC.
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
PY=/home/user/controle-ia-travail/.venv/bin/python
h_faux() { local H0_PREVU=$1; date -u -d "@$(( $(date -d "${H0_PREVU%Z}" +%s) + 94 * 3600 ))" +%Y-%m-%dT%H:%M:%SZ; }
ecarts=0; n=0; ecarts_utc=0
for H0 in 2026-11-21T20:12:03Z 2026-12-31T23:59:59Z 2028-02-27T12:00:00Z; do
  ATT=$("$PY" -I "$ME/outils/calcul-heure-arret.py" "$H0")
  for tz in UTC Europe/Berlin America/Los_Angeles Pacific/Auckland; do
    export TZ=$tz
    R=$(h_faux "$H0")
    n=$((n + 1))
    if [ "$R" != "$ATT" ]; then ecarts=$((ecarts + 1)); [ "$tz" = UTC ] && ecarts_utc=$((ecarts_utc + 1)); fi
  done
done
unset TZ
echo "témoin faux : couples $n ; écarts vus $ecarts (attendu : 9 = tous les couples hors UTC) ; écarts sous UTC $ecarts_utc (attendu 0)"
