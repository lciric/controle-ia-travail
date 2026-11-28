import json
import os
import subprocess
import urllib.request
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")

print("=== 1. HETZNER 08:22Z ===")
try:
    req = urllib.request.Request(
        "https://api.hetzner.cloud/v1/servers",
        headers={"Authorization": "Bearer " + os.environ["HCLOUD_TOKEN"]},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read().decode())
    for s in d.get("servers", []):
        print("HETZNER:", s["id"], s["name"], s["status"], s["server_type"]["name"], s["created"])
except Exception as e:
    print("HETZNER_ERR:", e)

print("=== 2. VAST INSTANCES ===")
try:
    out = subprocess.check_output(["vastai", "show", "instances", "--raw"], text=True, timeout=30)
    for i in json.loads(out):
        print("VAST:", i.get("id"), i.get("actual_status"), i.get("label"), i.get("gpu_name"))
except Exception as e:
    print("VAST_ERR:", e)

print("=== 3. VH ETAPE 0 OUTPUT ===")
vh = SCRATCH / "sortie-vh-etape0-ab094582"
if vh.exists():
    for p in sorted(vh.rglob("*")):
        if p.is_file():
            print("VH:", p.relative_to(vh), p.stat().st_size)
else:
    print("VH: directory does not exist yet")

print("=== 4. B8 PUISSANCE OUTPUT ===")
for sub in ("runs/20261125-045100-puissance-barreau8", "diag/20261125-045100-puissance-barreau8"):
    d = SCRATCH / "wt-b8-puissance" / sub
    if d.exists():
        for p in sorted(d.rglob("*")):
            if p.is_file():
                print("B8:", sub, p.relative_to(d), p.stat().st_size)
    else:
        print("B8:", sub, "NOT FOUND")

print("=== 5. AUDIT R4 REPORT ===")
ar4 = SCRATCH / "audit-r4-lecture-1-iib-v5-v1.md"
print("AUDIT_R4_EXISTS:", ar4.exists(), ar4.stat().st_size if ar4.exists() else 0)
