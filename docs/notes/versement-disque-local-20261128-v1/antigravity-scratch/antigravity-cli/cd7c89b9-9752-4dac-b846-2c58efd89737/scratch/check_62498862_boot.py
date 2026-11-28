import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
VAST = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
INST_ID = "62498862"

secrets = []
for k in ("HF_TOKEN", "VAST_API_KEY", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2"):
    v = os.environ.get(k, "").strip()
    if len(v) >= 8:
        secrets.append(v)
try:
    gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=15).strip()
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

print("NOW_UTC:", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))

# 1. Show instances
raw_inst = subprocess.check_output([str(VAST), "show", "instances", "--raw"], env=env, text=True, timeout=45)
insts = json.loads(raw_inst)
print(f"VAST_INSTANCES ({len(insts)}):")
for i in insts:
    print(f"  id={i.get('id')} label={i.get('label')!r} actual={i.get('actual_status')} cur={i.get('cur_state')} "
          f"status_msg={mask(str(i.get('status_msg', '')))[:120]!r} dph={i.get('dph_total')}")

# 2. Check remote branch calcul/dose-reponse-v1
ls_out = subprocess.check_output(
    ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
     "ls-remote", "origin", "refs/heads/calcul/dose-reponse-v1", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4"],
    env=env, text=True, timeout=45
).strip()
print("REMOTE_BRANCHES:")
print(ls_out or "(none)")

# 3. Fetch masked logs of 62498862
p_logs = subprocess.run([str(VAST), "logs", INST_ID, "--tail", "120"], env=env, capture_output=True, text=True, timeout=60)
print("LOGS_RC:", p_logs.returncode)
logs_masked = mask((p_logs.stdout or "") + "\n" + (p_logs.stderr or ""))
lines = [ln for ln in logs_masked.splitlines() if ln.strip()]
print(f"LOGS_LINES ({len(lines)}):")
for ln in lines[-50:]:
    print("  " + ln[:200])
