#!/usr/bin/env bash
# Veille en lecture seule : sort (code 0) quand il existe une offre conforme au filtre du lanceur des notations ET un
# crédit au moins égal au minimum du lanceur (7,5 h × (prix de l'offre + prix des instances rr- en marche) + 1,2 USD)
# plus 1 USD de marge ; code 1 après le nombre de tours donné. N'arrête ni ne crée rien.
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
V=$B/venv-vastai/bin/vastai
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
TOURS=${1:-60}
for i in $(seq 1 "$TOURS"); do
    "$V" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw > /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/.offres.json 2>/dev/null
    "$V" show instances --raw > /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/.instances.json 2>/dev/null
    "$V" show user --raw > /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/.user.json 2>/dev/null
    r=$(python3 -I - <<'PY'
import json
base = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/"
try:
    offres = json.load(open(base + ".offres.json")); inst = json.load(open(base + ".instances.json"))
    credit = float(json.load(open(base + ".user.json"))["credit"])
except Exception:
    raise SystemExit
ok = [o for o in offres if o.get("gpu_name") == "A100 SXM4" and o.get("cpu_name") == "AMD EPYC 7513 32-Core Processor"
      and isinstance(o.get("dph_total"), (int, float)) and float(o["dph_total"]) <= 1.30]
rr = [i for i in inst if str(i.get("label") or "").startswith("rr-")]
somme = sum(float(i.get("dph_total") or 0) for i in rr if not (i.get("actual_status") in ("exited", "stopped") and i.get("cur_state") == "stopped"))
for o in sorted(ok, key=lambda o: float(o["dph_total"])):
    m = 7.5 * (float(o["dph_total"]) + somme) + 1.2
    if credit >= m + 1.0:
        print(f"{o['id']} machine {o.get('machine_id')} {float(o['dph_total']):.4f} USD/h ; crédit {credit:.2f} ; minimum {m:.2f} ; rr- {','.join(str(i['id']) for i in rr) or '-'}")
        break
PY
)
    rm -f /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/.offres.json /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/.instances.json /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/.user.json
    if [ -n "$r" ]; then echo "$(date -u +%FT%TZ) prêt : $r"; exit 0; fi
    sleep 120
done
echo "$(date -u +%FT%TZ) ni offre conforme ni crédit suffisant ensemble après $TOURS tours"; exit 1
