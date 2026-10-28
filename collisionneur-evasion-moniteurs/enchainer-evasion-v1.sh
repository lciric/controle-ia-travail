#!/usr/bin/env bash
# Enchaîne les trois tours de triplets (évasion/moniteurs), GO-2026-10-28-03. Contrôle avant chaque tour ; un refus arrête le tour mais pas la chaîne. Journal : enchainer-evasion-v1.journal.
set -uo pipefail; set +x
cd "$(dirname "$0")"
J=enchainer-evasion-v1.journal
log(){ echo "$(date -u +%FT%TZ) $*" | tee -a "$J"; }
for n in 1 2 3; do
  D=tour-$n
  if bash "$D/controler-especes-v1.sh" GO-2026-10-28-03 appel-controle-v1.json >>"$J" 2>&1 \
     && ../collisionneur-evasion-moniteurs/venv/bin/python -I -B -c 'import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if all(v["statut"]=="OK" for v in d["especes"].values()) else 1)' "$D/appel-controle-v1.json"; then
    log "$D : contrôle OK, tour lancé"
    bash "$D/lancer-tour-$n-v1.sh" > "$D/lancer-tour-$n-v1.log" 2>&1; c=$?
    log "$D : tour fini, code $c"
  else
    log "$D : contrôle en échec (modèle non servi ou refus), tour sauté"
  fi
done
log "enchaînement fini"
