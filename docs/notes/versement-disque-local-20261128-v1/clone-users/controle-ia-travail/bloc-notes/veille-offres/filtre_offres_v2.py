# Lecture seule : offres conformes au filtre du lanceur de P3 et au crédit (6,5 h x prix + 1,2 USD <= crédit).
import json, sys, time
credit = float(sys.argv[1])
try:
    o = json.load(sys.stdin)
except Exception:
    print(time.strftime("%H:%M:%SZ", time.gmtime()), "lecture illisible", flush=True)
    sys.exit()
c = [x for x in o if "EPYC 7513" in (x.get("cpu_name") or "") and (x.get("cpu_cores_effective") or 0) >= 16
     and (x.get("cpu_ram") or 0) >= 128000 and 0 <= (x.get("inet_down_cost") or 0) <= 0.05
     and 0 <= (x.get("storage_total_cost") or 0) <= 0.03 and 0 < x["dph_total"] <= 1.30]
ok = [x for x in c if round(credit, 2) >= 6.5 * x["dph_total"] + 1.2]
desc = " ".join("%s:%.3f" % (x["id"], x["dph_total"]) for x in c)
print(time.strftime("%H:%M:%SZ", time.gmtime()), "lues", len(o), "conformes", len(c), "dans-le-credit", len(ok), desc, flush=True)
