import json, os, urllib.request
cle = os.environ["VAST_API_KEY"]
req = urllib.request.Request("https://console.vast.ai/api/v0/instances/?owner=me",
                             headers={"Authorization": "Bearer " + cle, "Accept": "application/json"})
with urllib.request.urlopen(req, timeout=60) as r:
    donnees = json.load(r)
inst = donnees.get("instances", [])
print("instances :", len(inst))
for i in inst:
    print({k: i.get(k) for k in ("id", "label", "actual_status", "intended_status", "gpu_name", "start_date")})
