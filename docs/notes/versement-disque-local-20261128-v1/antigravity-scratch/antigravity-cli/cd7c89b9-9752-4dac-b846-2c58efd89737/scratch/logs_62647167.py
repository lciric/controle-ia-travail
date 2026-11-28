import os
import re
import subprocess
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
VAST = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=25).strip()
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or (vk.read_text(encoding="utf-8").strip() if vk.is_file() else "")
secrets = [s for s in (gh_tok, vast_key, os.environ.get("HF_TOKEN", "")) if len(s) >= 8]
env = os.environ.copy()
env["VAST_API_KEY"] = vast_key
env["VASTAI_NO_UPDATE_CHECK"] = "1"
p = subprocess.run([str(VAST), "logs", "62647167", "--tail", "400"], env=env, capture_output=True, text=True, timeout=120)
out = (p.stdout or "") + (p.stderr or "")
for s in secrets:
    out = out.replace(s, "***")
out = re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{10,}", r"\1***", out)
lines = [l for l in out.splitlines() if l.strip()]
print("RC", p.returncode, "LINES", len(lines))
keep = [l for l in lines if re.search(r"DÉBUT|cpu|workers|Lancement|SONDE|SYNTHESE|RAPATRIEMENT|ARRÊT|ERREUR|Error|Traceback|reprise|Reprise|FIN", l)]
for l in keep[-25:]:
    print("K:", l[:220])
print("---- tail ----")
for l in lines[-12:]:
    print("T:", l[:220])
import collections
c = collections.Counter()
for l in lines:
    m = re.match(r"etalon (\S+) (\S+) réplique (\d+)/500", l)
    if m:
        c[int(m.group(3))] += 1
if c:
    print("REPLIQUES_VUES_MIN_MAX:", min(c), max(c))
