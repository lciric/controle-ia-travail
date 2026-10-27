#!/usr/bin/env bash
set -uo pipefail; set +x
cd "$(dirname "$0")"; J=enchainer-questions-fortes-v1.journal
[ ! -e "$J" ] || { echo "$J existe déjà (R12)" >&2; exit 2; }
log() { echo "$(date -u +%FT%TZ) $*" | tee -a "$J"; }
bash controler-especes-luc-v1.sh GO-2026-10-27-09 appel-controle-especes-questions-fortes-v1.json >> "$J" 2>&1 || { log "contrôle en échec"; exit 3; }
python3 -I -c 'import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if all(v["statut"]=="OK" for v in d["especes"].values()) else 1)' appel-controle-especes-questions-fortes-v1.json || { log "contrôle : une espèce en échec ; tour non lancé"; exit 3; }
log "contrôle OK (GO-2026-10-27-09), tour lancé"
bash lancer-tour-questions-fortes-v1-luc.sh > lancer-tour-questions-fortes-v1-luc.log 2>&1; c=$?
log "tour fini, code $c"
