import json
import os
import subprocess
import urllib.request
from pathlib import Path

htok = os.environ.get("HCLOUD_TOKEN", "").strip()
REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")

def hget(path):
    req = urllib.request.Request(
        f"https://api.hetzner.cloud/v1/{path}",
        headers={"Authorization": f"Bearer {htok}"},
    )
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))

srvs = hget("servers").get("servers", [])
print(f"HETZNER_SERVERS_COUNT: {len(srvs)}")
for s in srvs:
    print(" ", s.get("id"), s.get("name"), s.get("status"))

imgs = hget("images?type=snapshot").get("images", [])
print(f"HETZNER_SNAPSHOTS_COUNT: {len(imgs)}")
for im in imgs:
    print(" ", im.get("id"), im.get("description"), im.get("created"), im.get("image_size"))

env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"
out = subprocess.check_output(
    ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
     "ls-remote", "--heads", "origin", "*sondes-v2*", "*etalon*", "calcul/*"],
    env=env, text=True, timeout=45,
).strip()
print("REMOTE_BRANCHES:")
print(out or "(none)")
