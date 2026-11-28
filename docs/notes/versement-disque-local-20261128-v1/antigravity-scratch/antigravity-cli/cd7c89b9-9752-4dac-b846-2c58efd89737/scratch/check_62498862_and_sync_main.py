import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
WT_EXEC = SCRATCH / "wt-b8-exec-v5"
VAST = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
INST_ID = "62498862"
EXPECTED_ETATS = "7329f08be94adda1ae0e5f44ea9d9b80dd7f614310343b39a39e87d1abab9e0c"
REL_ETATS = Path("docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json")

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


print("NOW_UTC:", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))

# 1. Copy etats-lectures-iib-v1.json (+ .sha256) to main, commit & push main
dst_json = REPO / REL_ETATS
dst_sha = REPO / (str(REL_ETATS) + ".sha256")
src_json = WT_EXEC / REL_ETATS
src_sha = WT_EXEC / (str(REL_ETATS) + ".sha256")
raw = src_json.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_ETATS
dst_json.write_bytes(raw)
dst_sha.write_bytes(src_sha.read_bytes())
assert hashlib.sha256(dst_json.read_bytes()).hexdigest() == EXPECTED_ETATS
print("ETATS_COPIED_AND_VERIFIED:", EXPECTED_ETATS)

env = os.environ.copy()
env["VAST_API_KEY"] = vast_key
env["VASTAI_NO_UPDATE_CHECK"] = "1"
env["GIT_TERMINAL_PROMPT"] = "0"

def git_run(*args, timeout=60):
    return subprocess.run(
        ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", *args],
        env=env, capture_output=True, text=True, timeout=timeout,
    )

git_run("add", "registres/decisions.md", "registres/depenses.md", "registres/sondes-iib-v1.md",
        str(REL_ETATS).replace("\\", "/"), str(REL_ETATS).replace("\\", "/") + ".sha256")
pc = git_run("commit", "-m", "R-5403..R-5405 : instance Vast.ai 62498862 dose-reponse lancee et ETATS-COURSE-IIB inscrit")
print("GIT_COMMIT_RC:", pc.returncode, (pc.stdout or pc.stderr).strip()[:200])
pp = git_run("push", "origin", "main", timeout=90)
print("GIT_PUSH_RC:", pp.returncode, mask((pp.stdout or "") + " " + (pp.stderr or "")).strip()[:200])

# 2. Fast REST check of Vast.ai instances
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
              f"dph={i.get('dph_total')} msg={mask(str(i.get('status_msg', '')))[:120]!r}")
except Exception as e:
    print("VAST_REST_ERR:", mask(repr(e)))

# 3. Check remote branches calcul/dose-reponse-v1 & calcul/sondes-v2-epreuve-plantee-v4
pls = git_run("ls-remote", "origin", "refs/heads/calcul/dose-reponse-v1", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4", timeout=45)
print("REMOTE_BRANCHES:")
print(pls.stdout.strip() or "(none)")

# 4. Fast check Hetzner 177425658 if HCLOUD_TOKEN in env
htok = os.environ.get("HCLOUD_TOKEN", "").strip()
if htok:
    try:
        req = urllib.request.Request(
            "https://api.hetzner.cloud/v1/servers/177425658",
            headers={"Authorization": f"Bearer {htok}"},
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            srv = json.loads(resp.read().decode("utf-8"))["server"]
        print(f"HETZNER_177425658: status={srv.get('status')} name={srv.get('name')} created={srv.get('created')}")
    except Exception as e:
        print("HETZNER_ERR:", mask(repr(e)))
else:
    print("HETZNER_TOKEN: not in env")

# 5. Fetch masked logs of 62498862 (timeout=120)
try:
    p_logs = subprocess.run([str(VAST), "logs", INST_ID, "--tail", "120"], env=env, capture_output=True, text=True, timeout=120)
    print("LOGS_RC:", p_logs.returncode)
    logs_masked = mask((p_logs.stdout or "") + "\n" + (p_logs.stderr or ""))
    lines = [ln for ln in logs_masked.splitlines() if ln.strip()]
    print(f"LOGS_LINES ({len(lines)}):")
    for ln in lines[-35:]:
        print("  " + ln[:180])
except Exception as e:
    print("LOGS_ERR:", mask(repr(e)))
