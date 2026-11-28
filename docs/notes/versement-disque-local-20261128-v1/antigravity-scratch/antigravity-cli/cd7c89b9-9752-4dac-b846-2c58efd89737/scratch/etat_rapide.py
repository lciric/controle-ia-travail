import json
import os
import re
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=25).strip()
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or (vk.read_text(encoding="utf-8").strip() if vk.is_file() else "")
secrets = [s for s in (gh_tok, vast_key, os.environ.get("HF_TOKEN", ""), os.environ.get("HCLOUD_TOKEN", "")) if len(s) >= 8]

def mask(s):
    for x in secrets:
        s = s.replace(x, "***")
    return re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{10,}", r"\1***", s)

def get(url, hdr):
    req = urllib.request.Request(url, headers=hdr)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))

print("NOW_UTC:", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
try:
    d = get("https://console.vast.ai/api/v0/instances/", {"Authorization": f"Bearer {vast_key}", "Accept": "application/json"})
    for i in d.get("instances", []):
        print(f"VAST id={i.get('id')} label={i.get('label')!r} actual={i.get('actual_status')} dph={i.get('dph_total')} msg={mask(str(i.get('status_msg','')))[:80]!r}")
    u = get("https://console.vast.ai/api/v0/users/current/", {"Authorization": f"Bearer {vast_key}", "Accept": "application/json"})
    print("VAST_CREDIT:", u.get("credit"))
except Exception as e:
    print("VAST_ERR:", mask(repr(e)))

gh = {"Authorization": f"Bearer {gh_tok}", "Accept": "application/vnd.github+json", "User-Agent": "mere"}
for br in ("main", "calcul/dose-reponse-v1", "calcul/sondes-v2-epreuve-plantee-v4-suite"):
    try:
        r = get(f"https://api.github.com/repos/lciric/controle-ia-travail/git/ref/heads/{br}", gh)
        c = get(f"https://api.github.com/repos/lciric/controle-ia-travail/git/commits/{r['object']['sha']}", gh)
        print(f"GH {br}: {r['object']['sha'][:12]} {c['committer']['date']} {mask(c['message'])[:110]!r}")
    except Exception as e:
        print(f"GH {br}: ERR {e}")

htok = os.environ.get("HCLOUD_TOKEN", "").strip()
if htok:
    try:
        s = get("https://api.hetzner.cloud/v1/servers", {"Authorization": f"Bearer {htok}"})
        print("HETZNER_SERVERS:", [x.get("id") for x in s.get("servers", [])])
    except Exception as e:
        print("HETZNER_ERR:", mask(repr(e)))

for p in ("sondes-v2-amorce-v3/contre-lecture-r2-amorce-sondes-v2-v3-v1.md", "d10-backup", "wt-b8-puissance/docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-lecteur-sondes-barreau8-v3.md",
          "wt-b8-puissance/diag/20261125-083300-puissance-barreau8/aires-minimales-detectables-barreau8-v1.json"):
    print("EXISTS", p, (SCRATCH / p).exists())
r = subprocess.run(["git", "-C", str(SCRATCH / "wt-b8-puissance"), "status", "--porcelain"], capture_output=True, text=True, timeout=60)
print("WT_B8_STATUS:", (r.stdout.strip() or "(clean)")[:600])
r = subprocess.run(["git", "-C", str(SCRATCH / "wt-b8-puissance"), "log", "-1", "--format=%H %s"], capture_output=True, text=True, timeout=60)
print("WT_B8_HEAD:", r.stdout.strip())
