#!/usr/bin/env bash
# veille d'une pièce : $1 = identifiant, $2 = coupure USD, $3 = dossier ; pas de 600 s ; sort sur événement
ID="$1"; COUP="$2"; P="$3"; mkdir -p "$P/veille"
while :; do
  H=$(date -u +%Y%m%dT%H%M%SZ)
  vastai show instances --raw 2>/dev/null | python3 -I -c '
import json,sys,time
d=json.load(sys.stdin); d=d.get("instances",d) if isinstance(d,dict) else d
keep=("id","label","actual_status","cur_state","intended_status","dph_total","start_date","inet_up_billed","inet_down_billed","inet_up_cost","inet_down_cost","status_msg")
json.dump([{k:x.get(k) for k in keep} for x in d], sys.stdout)' > "$P/veille/liste-$H.json"
  R=$(python3 -I - "$P/veille/liste-$H.json" "$ID" "$COUP" <<'PY'
import json,sys,time
l=json.load(open(sys.argv[1])); i=int(sys.argv[2]); c=float(sys.argv[3])
x=[x for x in l if x["id"]==i]
if not x: print("ABSENTE 0 0"); sys.exit()
x=x[0]; h=(time.time()-x["start_date"])/3600
base=h*x["dph_total"]
# sortie de données : champs *_billed en octets (constat du 23 novembre), prix en USD par Go
sortie=((x["inet_up_billed"] or 0)*(x["inet_up_cost"] or 0)+(x["inet_down_billed"] or 0)*(x["inet_down_cost"] or 0))/1e9
cum=base+sortie
if sortie>2.0 or cum<0 or cum>base+2.0: print(x["actual_status"], round(cum,3), "ANOMALIE"); sys.exit()
print(x["actual_status"], round(cum,3), "COUPURE" if cum+0.25*x["dph_total"]>=c else "ok")
PY
)
  vastai logs "$ID" --tail 400 > "$P/veille/brut-$H.txt" 2>&1
  grep -aE ' B5F |^B5F ' "$P/veille/brut-$H.txt" > "$P/veille/journal-$H.txt"
  CR=$(vastai show user --raw 2>/dev/null | python3 -I -c 'import json,sys; print(round(json.load(sys.stdin)["credit"],2))')
  echo "$H etat=$(echo $R|cut -d' ' -f1) cumul=$(echo $R|cut -d' ' -f2) $(echo $R|cut -d' ' -f3) credit=$CR etapes=$(wc -l < "$P/veille/journal-$H.txt")" | tee -a "$P/veille/bilan.txt"
  case "$R" in *COUPURE*) vastai stop instance "$ID" > "$P/veille/arret-$H.txt" 2>&1; echo "ARRET A LA COUPURE $H" | tee -a "$P/veille/bilan.txt"; exit 3;; ABSENTE*) echo "INSTANCE ABSENTE $H"; exit 4;; *ANOMALIE*) echo "ANOMALIE DU CALCUL DU CUMUL $H : aucun arret automatique"; exit 6;; esac
  if grep -aqE 'versement final prouvé|SIGNAL POUR LA MÈRE|fin, code|ARRET|REFUS|non prouvé' "$P/veille/journal-$H.txt"; then echo "EVENEMENT AU JOURNAL $H"; exit 0; fi
  case "$(echo $R|cut -d' ' -f1)" in running|loading|created|None|null) ;; *) echo "ETAT $R $H (journal relu)"; exit 5;; esac
  sleep 600
done
