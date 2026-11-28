import base64
import json
import re
import subprocess
import urllib.request

gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=25).strip()
H = {"Authorization": f"Bearer {gh_tok}", "Accept": "application/vnd.github+json", "User-Agent": "mere"}

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))

B = "https://api.github.com/repos/lciric/controle-ia-travail"
for c in get(f"{B}/commits?sha=main&per_page=15"):
    print(c["sha"][:10], c["commit"]["committer"]["date"], c["commit"]["message"].splitlines()[0][:150])
print("----")
for c in get(f"{B}/commits?sha=calcul/dose-reponse-v1&per_page=4"):
    print("DR", c["sha"][:10], c["commit"]["committer"]["date"], c["commit"]["message"].splitlines()[0][:150])
print("----")
for f in ("registres/decisions.md", "registres/arrets.md", "registres/depenses.md"):
    o = get(f"{B}/contents/{f}?ref=main")
    blob = get(o["git_url"])
    txt = base64.b64decode(blob["content"]).decode("utf-8")
    lines = [l for l in txt.splitlines() if l.strip()]
    print(f"=== {f} (last 6) ===")
    for l in lines[-6:]:
        print(l[:700].replace(gh_tok, "***"))
