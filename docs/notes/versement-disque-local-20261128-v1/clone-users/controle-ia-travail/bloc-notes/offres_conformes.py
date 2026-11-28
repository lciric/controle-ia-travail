import json, sys
o = json.load(sys.stdin)
ok = [x for x in o if x.get("gpu_name") == "A100 SXM4" and x.get("cpu_name") == "AMD EPYC 7513 32-Core Processor"
      and isinstance(x.get("dph_total"), (int, float)) and float(x["dph_total"]) <= 1.30]
print(len(o), "offres filtrées ;", len(ok), "conformes :", ", ".join(f"{x['id']} (machine {x.get('machine_id')}, {float(x['dph_total']):.4f})" for x in ok))
