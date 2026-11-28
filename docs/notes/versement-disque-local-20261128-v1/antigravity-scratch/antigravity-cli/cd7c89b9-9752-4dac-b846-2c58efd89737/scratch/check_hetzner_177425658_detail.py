import json
import os
import subprocess
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

htok = os.environ.get("HCLOUD_TOKEN", "").strip()
assert len(htok) >= 8, "HCLOUD_TOKEN missing"
REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")

def hget(path):
    req = urllib.request.Request(
        f"https://api.hetzner.cloud/v1/{path}",
        headers={"Authorization": f"Bearer {htok}"},
    )
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))

srv = hget("servers/177425658")["server"]
print("SERVER:", json.dumps({
    "id": srv.get("id"),
    "name": srv.get("name"),
    "status": srv.get("status"),
    "created": srv.get("created"),
    "type": srv.get("server_type", {}).get("name"),
    "ingoing_traffic": srv.get("ingoing_traffic"),
    "outgoing_traffic": srv.get("outgoing_traffic"),
    "labels": srv.get("labels"),
}, indent=2))

now = datetime.now(timezone.utc)
start = (now - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
end = now.strftime("%Y-%m-%dT%H:%M:%SZ")
m = hget(f"servers/177425658/metrics?type=cpu,network&start={start}&end={end}")["metrics"]
for k, v in m.get("time_series", {}).items():
    vals = v.get("values", [])
    tail = vals[-8:] if vals else []
    print(f"METRIC {k} ({len(vals)} pts): tail={tail}")

# Check ALL remote branches matching sondes-v2
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"
out = subprocess.check_output(
    ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
     "ls-remote", "--heads", "origin", "*sondes-v2*"],
    env=env, text=True, timeout=45,
).strip()
print("REMOTE_SONDES_V2_BRANCHES:")
print(out or "(none)")
