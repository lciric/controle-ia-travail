import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
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

# 1. Complete byte-for-byte copy of sealed probes v2 report & JSON + .sha256 to Downloads
for fname in ("rapport-resultats-sondes-v2-etalon-v1.md", "synthese-partielle-r0-130-etalon-v1.json"):
    h = sha256_file(SRC_DIR / fname)
    shutil.copy2(SRC_DIR / fname, DL / fname)
    (DL / (fname + ".sha256")).write_bytes(f"{h}  {fname}\n".encode("ascii"))
    assert sha256_file(DL / fname) == h
print("DOWNLOADS_ALL_4_FILES_OK")

# 2. Masking setup
secrets = []
for k in ("HF_TOKEN", "VAST_API_KEY", "HCLOUD_TOKEN", "HETZNER_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2"):
    v = os.environ.get(k, "").strip()
    if len(v) >= 8:
        secrets.append(v)
gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=30).strip()
if len(gh_tok) >= 8:
    secrets.append(gh_tok)
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or (vk.read_text(encoding="utf-8").strip() if vk.is_file() else "")
if len(vast_key) >= 8:
    secrets.append(vast_key)

def mask(s: str) -> str:
    for sec in secrets:
        s = s.replace(sec, "***")
    return re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{10,}", r"\1***", s)

# 3. Run inscribe_go_option_b.py
p_ins = subprocess.run([sys.executable, str(SCRATCH / "inscribe_go_option_b.py")], capture_output=True, text=True, timeout=240)
print("INSCRIBE_RC:", p_ins.returncode)
print(mask((p_ins.stdout or "") + (p_ins.stderr or "")).strip())
if p_ins.returncode != 0:
    sys.exit(p_ins.returncode)

# 4. Fast GitHub REST check of calcul/dose-reponse-v1
for br in ("calcul/dose-reponse-v1", "main"):
    req = urllib.request.Request(
        f"https://api.github.com/repos/lciric/controle-ia-travail/git/ref/heads/{br}",
        headers={"Authorization": f"Bearer {gh_tok}", "Accept": "application/vnd.github+json", "User-Agent": "controle-ia"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    print(f"GH_REF {br}: {d['object']['sha']}")

# 5. D-10 CPU progress
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
    print("D10_ERR:", repr(e))

# 6. Vast.ai 62498862 logs tail
env = os.environ.copy()
env["VAST_API_KEY"] = vast_key
env["VASTAI_NO_UPDATE_CHECK"] = "1"
try:
    p_logs = subprocess.run([str(VAST), "logs", INST_ID, "--tail", "50"], env=env, capture_output=True, text=True, timeout=90)
    lines = [ln for ln in mask((p_logs.stdout or "") + "\n" + (p_logs.stderr or "")).splitlines() if ln.strip()]
    print(f"LOGS_62498862_RC={p_logs.returncode} ({len(lines)} lines):")
    for ln in lines[-15:]:
        print("  " + ln[:180])
except Exception as e:
    print("LOGS_ERR:", mask(repr(e)))

# 7. Hetzner server types + Vast.ai multi-core offers + Vast credit
htok = os.environ.get("HCLOUD_TOKEN", "").strip()
if htok:
    try:
        req_t = urllib.request.Request("https://api.hetzner.cloud/v1/server_types?per_page=50", headers={"Authorization": f"Bearer {htok}"})
        with urllib.request.urlopen(req_t, timeout=20) as resp:
            stypes = json.loads(resp.read().decode("utf-8")).get("server_types", [])
        print("HETZNER_TYPES:")
        for st in stypes:
            nm = st.get("name", "")
            cores = st.get("cores", 0)
            if cores >= 8 and (nm.startswith("ccx") or nm.startswith("cpx")) and not st.get("deprecated"):
                prices = {p["location"]: p["price_hourly"]["gross"] for p in st.get("prices", []) if p["location"] in ("hel1", "fsn1", "nbg1")}
                print(f"  {nm}: cores={cores} mem={st.get('memory')}GB arch={st.get('architecture')} eur_h={prices}")
    except Exception as e:
        print("HETZNER_ERR:", mask(repr(e)))

try:
    req_u = urllib.request.Request("https://console.vast.ai/api/v0/users/current/", headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"})
    with urllib.request.urlopen(req_u, timeout=20) as resp:
        u = json.loads(resp.read().decode("utf-8"))
    print("VAST_CREDIT:", u.get("credit"))

    q = {
        "verified": {"eq": True}, "external": {"eq": False}, "rentable": {"eq": True}, "rented": {"eq": False},
        "datacenter": {"eq": True}, "reliability2": {"gte": 0.985}, "cpu_cores_effective": {"gte": 32},
        "cpu_ram": {"gte": 64000}, "disk_space": {"gte": 40}, "dph_total": {"lte": 0.90},
        "order": [["dph_total", "asc"]], "type": "on-demand", "limit": 12,
    }
    req_v = urllib.request.Request(
        "https://console.vast.ai/api/v0/bundles/", data=json.dumps(q).encode("utf-8"),
        headers={"Authorization": f"Bearer {vast_key}", "Content-Type": "application/json", "Accept": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req_v, timeout=25) as resp:
        offers = json.loads(resp.read().decode("utf-8")).get("offers", [])
    print(f"VAST_MULTICORE_OFFERS ({len(offers)}):")
    for o in offers[:10]:
        eff_c = o.get("cpu_cores_effective")
        dph = o.get("dph_total")
        print(f"  id={o.get('id')} mach={o.get('machine_id')} cpu={o.get('cpu_name')!r} eff_cores={eff_c} "
              f"ram_gb={round((o.get('cpu_ram') or 0)/1024,1)} gpu={o.get('gpu_name')}x{o.get('num_gpus')} "
              f"dph={dph:.4f} est_85h_usd={(dph*(85.0/eff_c) if eff_c else 99):.2f} rel={o.get('reliability2'):.4f} loc={o.get('geolocation')}")
except Exception as e:
    print("VAST_OFFERS_ERR:", mask(repr(e)))
