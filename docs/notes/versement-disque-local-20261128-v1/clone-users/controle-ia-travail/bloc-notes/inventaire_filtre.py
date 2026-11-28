import json, sys
try:
    instances = json.load(sys.stdin)
except Exception:
    print("réponse illisible", file=sys.stderr); sys.exit(3)
for i in instances:
    dph = i.get("dph_total")
    dph = f"{float(dph):.4f}" if isinstance(dph, (int, float)) and not isinstance(dph, bool) else "illisible"
    print(f"{i.get('id')} | {i.get('actual_status')} | {i.get('cur_state')} | étiquette={i.get('label')} | {i.get('gpu_name')} | {dph} USD/h")
print(f"{len(instances)} instance(s)")
