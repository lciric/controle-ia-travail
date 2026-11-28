import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
RUN_DIR = SCRATCH / "dr-lancement-v4-reel"
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
LOG_602 = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\.system_generated\tasks\task-602.log")

print("NOW_UTC:", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
print("LOG_602_SIZE:", LOG_602.stat().st_size if LOG_602.exists() else "MISSING")
if RUN_DIR.exists():
    for p in sorted(RUN_DIR.iterdir()):
        st = p.stat()
        mt = datetime.fromtimestamp(st.st_mtime, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        print(f"FILE: {p.name} size={st.st_size} mtime={mt}")

env = os.environ.copy()
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
if not env.get("VAST_API_KEY") and vk.is_file():
    env["VAST_API_KEY"] = vk.read_text(encoding="utf-8").strip()
env["VASTAI_NO_UPDATE_CHECK"] = "1"

try:
    out = subprocess.check_output([str(VAST_EXE), "show", "instances", "--raw"], env=env, text=True, timeout=30)
    insts = json.loads(out)
    print(f"VAST_INSTANCES_COUNT: {len(insts)}")
    for i in insts:
        print(f"  id={i.get('id')} label={i.get('label')!r} status={i.get('actual_status')} cur={i.get('cur_state')} gpu={i.get('gpu_name')} dph={i.get('dph_total')} start={i.get('start_date')}")
except Exception as e:
    print("VAST_ERR:", repr(e))
