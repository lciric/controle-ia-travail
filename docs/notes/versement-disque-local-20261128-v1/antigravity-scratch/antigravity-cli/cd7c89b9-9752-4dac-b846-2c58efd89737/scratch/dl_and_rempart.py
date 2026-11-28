import hashlib
import json
import os
import re
import shutil
import subprocess
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SRC_DIR = SCRATCH / "lecture-sondes-v2-etalon"
DL = Path(r"C:\Users\lciri\Downloads")
VAST = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
INST_ID = "62498862"

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

# 1. Copy sealed probes v2 report & JSON to Downloads
rep_name = "rapport-resultats-sondes-v2-etalon-v1.md"
json_name = "synthese-partielle-r0-130-etalon-v1.json"
rep_h = sha256_file(SRC_DIR / rep_name)
json_h = sha256_file(SRC_DIR / json_name)

shutil.copy2(SRC_DIR / rep_name, DL / rep_name)
(DL / (rep_name + ".sha256")).write_bytes(f"{rep_h}  {rep_name}\n".encode("ascii"))
shutil.copy2(SRC_DIR / json_name, DL / json_name)
(DL / (json_name + ".sha256")).write_bytes(f"{json_h}  {json_name}\n".encode("ascii"))
assert sha256_file(DL / rep_name) == rep_h
assert sha256_file(DL / json_name) == json_h
print(f"DOWNLOADS_COPIED_OK: {DL / rep_name} ({rep_h[:16]}), {DL / json_name} ({json_h[:16]})")

# 2. Masking setup
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
    return re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{10,}", r"\1***", s)

env = os.environ.copy()
env["VAST_API_KEY"] = vast_key
env["VASTAI_NO_UPDATE_CHECK"] = "1"
env["GIT_TERMINAL_PROMPT"] = "0"

now = datetime.now(timezone.utc)
print("NOW_UTC:", now.strftime("%Y-%m-%dT%H:%M:%SZ"))

# 3. Vast.ai instances & credit
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
              f"dph={i.get('dph_total')} start={i.get('start_date')}")
    req_u = urllib.request.Request(
        "https://console.vast.ai/api/v0/users/current/",
        headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req_u, timeout=20) as resp:
        u = json.loads(resp.read().decode("utf-8"))
    print(f"VAST_CREDIT: {u.get('credit')}")
except Exception as e:
    print("VAST_REST_ERR:", mask(repr(e)))

# 4. Vast.ai 62498862 logs tail
try:
    p_logs = subprocess.run([str(VAST), "logs", INST_ID, "--tail", "60"], env=env, capture_output=True, text=True, timeout=90)
    lines = [ln for ln in mask((p_logs.stdout or "") + "\n" + (p_logs.stderr or "")).splitlines() if ln.strip()]
    print(f"LOGS_62498862_RC={p_logs.returncode} ({len(lines)} lines):")
    for ln in lines[-20:]:
        print("  " + ln[:180])
except Exception as e:
    print("LOGS_ERR:", mask(repr(e)))

# 5. Remote git heads
pls = subprocess.run(
    ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
     "ls-remote", "origin", "refs/heads/calcul/dose-reponse-v1", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4", "refs/heads/main"],
    env=env, capture_output=True, text=True, timeout=45
)
print("REMOTE_HEADS:\n" + pls.stdout.strip())

# 6. D-10 CPU progress
p_diag = SCRATCH / "wt-b8-puissance" / "diag" / "20261125-083300-puissance-barreau8"
print("D10_DIAG_EXISTS:", p_diag.exists())
try:
    ps_out = subprocess.check_output(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*puissance*' } | ForEach-Object { $p = Get-Process -Id $_.ProcessId -ErrorAction SilentlyContinue; if ($p) { \"$($p.Id) CPU=$([math]::Round($p.CPU,1))s WS=$([math]::Round($p.WorkingSet64/1MB,1))MB\" } }"],
        text=True, timeout=25,
    ).strip()
    print("D10_PROC:", ps_out or "(not found)")
except Exception as e:
    print("D10_PROC_ERR:", repr(e))

# 7. Query Hetzner server types (ccx / cpx) + active servers
htok = os.environ.get("HCLOUD_TOKEN", "").strip()
if htok:
    try:
        req = urllib.request.Request("https://api.hetzner.cloud/v1/servers", headers={"Authorization": f"Bearer {htok}"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            srvs = json.loads(resp.read().decode("utf-8")).get("servers", [])
        print(f"HETZNER_SERVERS ({len(srvs)}):", [s.get("id") for s in srvs])

        req_t = urllib.request.Request("https://api.hetzner.cloud/v1/server_types?per_page=50", headers={"Authorization": f"Bearer {htok}"})
        with urllib.request.urlopen(req_t, timeout=20) as resp:
            stypes = json.loads(resp.read().decode("utf-8")).get("server_types", [])
        print("HETZNER_HIGH_CPU_TYPES:")
        for st in stypes:
            nm = st.get("name", "")
            cores = st.get("cores", 0)
            if cores >= 8 and (nm.startswith("ccx") or nm.startswith("cpx")) and not st.get("deprecated"):
                prices = {p["location"]: p["price_hourly"]["gross"] for p in st.get("prices", []) if p["location"] in ("hel1", "fsn1", "nbg1")}
                print(f"  {nm}: cores={cores} mem={st.get('memory')}GB cpu_type={st.get('cpu_type')} arch={st.get('architecture')} prices_eur_h={prices}")
    except Exception as e:
        print("HETZNER_ERR:", mask(repr(e)))

# 8. Query Vast.ai high-CPU offers (>= 48 effective cores, datacenter, verified, reliability >= 0.98, dph <= 1.60)
try:
    q = {
        "verified": {"eq": True},
        "external": {"eq": False},
        "rentable": {"eq": True},
        "rented": {"eq": False},
        "datacenter": {"eq": True},
        "reliability2": {"gte": 0.98},
        "cpu_cores_effective": {"gte": 48},
        "cpu_ram": {"gte": 64000},
        "disk_space": {"gte": 40},
        "dph_total": {"lte": 1.60},
        "order": [["dph_total", "asc"]],
        "type": "on-demand",
        "limit": 15,
    }
    body = json.dumps(q).encode("utf-8")
    req_v = urllib.request.Request(
        "https://console.vast.ai/api/v0/bundles/",
        data=body,
        headers={"Authorization": f"Bearer {vast_key}", "Content-Type": "application/json", "Accept": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_v, timeout=25) as resp:
        offers = json.loads(resp.read().decode("utf-8")).get("offers", [])
    print(f"VAST_HIGH_CPU_OFFERS ({len(offers)}):")
    for o in offers[:12]:
        eff_c = o.get("cpu_cores_effective")
        dph = o.get("dph_total")
        print(f"  id={o.get('id')} mach={o.get('machine_id')} cpu={o.get('cpu_name')!r} eff_cores={eff_c} "
              f"ram_gb={round((o.get('cpu_ram') or 0)/1024,1)} gpu={o.get('gpu_name')}x{o.get('num_gpus')} "
              f"dph={dph:.4f} usd_per_core_h={(dph/eff_c if eff_c else 99):.5f} rel={o.get('reliability2'):.4f} loc={o.get('geolocation')}")
except Exception as e:
    print("VAST_OFFERS_ERR:", mask(repr(e)))
