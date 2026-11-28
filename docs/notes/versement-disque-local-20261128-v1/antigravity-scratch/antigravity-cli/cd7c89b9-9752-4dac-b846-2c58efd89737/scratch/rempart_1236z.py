import json
import os
import re
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
VAST = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
INST_ID = "62498862"

secrets = []
for k in ("HF_TOKEN", "VAST_API_KEY", "HCLOUD_TOKEN", "HETZNER_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2"):
    v = os.environ.get(k, "").strip()
    if len(v) >= 8:
        secrets.append(v)
try:
    gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=20).strip()
    if len(gh_tok) >= 8:
        secrets.append(gh_tok)
except Exception:
    pass
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip()
if not vast_key and vk.is_file():
    vast_key = vk.read_text(encoding="utf-8").strip()
if len(vast_key) >= 8:
    secrets.append(vast_key)

def mask(s: str) -> str:
    for sec in secrets:
        s = s.replace(sec, "***")
    s = re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{10,}", r"\1***", s)
    return s

env = os.environ.copy()
env["VAST_API_KEY"] = vast_key
env["VASTAI_NO_UPDATE_CHECK"] = "1"
env["GIT_TERMINAL_PROMPT"] = "0"

now = datetime.now(timezone.utc)
print("NOW_UTC:", now.strftime("%Y-%m-%dT%H:%M:%SZ"))

# 1. Vast.ai instances via fast REST
try:
    req = urllib.request.Request(
        "https://console.vast.ai/api/v0/instances/",
        headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=25) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    insts = data.get("instances", data) if isinstance(data, dict) else data
    print(f"VAST_INSTANCES ({len(insts)}):")
    for i in insts:
        print(f"  id={i.get('id')} label={i.get('label')!r} actual={i.get('actual_status')} cur={i.get('cur_state')} "
              f"dph={i.get('dph_total')} total_spent={i.get('total_flops', '')} msg={mask(str(i.get('status_msg', '')))[:100]!r}")
except Exception as e:
    print("VAST_REST_ERR:", mask(repr(e)))

# 2. Hetzner 177425658 via fast REST
htok = os.environ.get("HCLOUD_TOKEN", "").strip()
if htok:
    try:
        req = urllib.request.Request(
            "https://api.hetzner.cloud/v1/servers",
            headers={"Authorization": f"Bearer {htok}"},
        )
        with urllib.request.urlopen(req, timeout=25) as resp:
            srvs = json.loads(resp.read().decode("utf-8")).get("servers", [])
        print(f"HETZNER_SERVERS ({len(srvs)}):")
        for s in srvs:
            print(f"  id={s.get('id')} name={s.get('name')} type={s.get('server_type',{}).get('name')} status={s.get('status')} created={s.get('created')}")
    except Exception as e:
        print("HETZNER_ERR:", mask(repr(e)))
else:
    print("HETZNER_TOKEN: missing")

# 3. Git remote branches & local main status
def git_run(*args, timeout=45):
    return subprocess.run(
        ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", *args],
        env=env, capture_output=True, text=True, timeout=timeout,
    )

pls = git_run("ls-remote", "origin", "refs/heads/calcul/dose-reponse-v1", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4", "refs/heads/main")
print("REMOTE_HEADS:")
print(pls.stdout.strip())
print("LOCAL_MAIN_HEAD:", git_run("rev-parse", "HEAD").stdout.strip())
print("LOCAL_MAIN_STATUS:", git_run("status", "-s").stdout.strip() or "(clean)")

# 4. Check task-510 puissance process & diag output
p_diag = SCRATCH / "wt-b8-puissance" / "diag" / "20261125-083300-puissance-barreau8"
print("D10_DIAG_EXISTS:", p_diag.exists())
if p_diag.exists():
    for f in sorted(p_diag.iterdir()):
        print(f"  D10_FILE: {f.name} size={f.stat().st_size}")
ps_out = subprocess.check_output(
    ["powershell", "-NoProfile", "-Command",
     "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*puissance*' } | ForEach-Object { $p = Get-Process -Id $_.ProcessId -ErrorAction SilentlyContinue; if ($p) { \"$($p.Id) CPU=$([math]::Round($p.CPU,1))s WS=$([math]::Round($p.WorkingSet64/1MB,1))MB\" } }"],
    text=True, timeout=25,
).strip()
print("D10_PROC:", ps_out or "(not found)")

# 5. Vast.ai 62498862 masked logs
try:
    p_logs = subprocess.run([str(VAST), "logs", INST_ID, "--tail", "80"], env=env, capture_output=True, text=True, timeout=90)
    print("LOGS_RC:", p_logs.returncode)
    lines = [ln for ln in mask((p_logs.stdout or "") + "\n" + (p_logs.stderr or "")).splitlines() if ln.strip()]
    print(f"LOGS_TAIL ({len(lines)} total):")
    for ln in lines[-25:]:
        print("  " + ln[:180])
except Exception as e:
    print("LOGS_ERR:", mask(repr(e)))
