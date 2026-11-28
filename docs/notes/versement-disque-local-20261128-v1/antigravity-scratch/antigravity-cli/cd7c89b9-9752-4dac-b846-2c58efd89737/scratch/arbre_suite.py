import json
import subprocess
import urllib.request

gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=25).strip()
H = {"Authorization": f"Bearer {gh_tok}", "Accept": "application/vnd.github+json", "User-Agent": "mere"}
B = "https://api.github.com/repos/lciric/controle-ia-travail"
with urllib.request.urlopen(urllib.request.Request(f"{B}/git/trees/90019bed2a1c?recursive=1", headers=H), timeout=30) as r:
    t = json.loads(r.read().decode("utf-8"))
paths = [x["path"] for x in t["tree"] if x["type"] == "blob"]
et = sorted(p for p in paths if "/etalon/rapport-" in p and p.endswith(".json"))
co = sorted(p for p in paths if "/complet/" in p)
print("TOTAL_FILES", len(paths))
print("ETALON_RAPPORTS", len(et))
for p in et:
    print("  ", p.split("/")[-1])
print("SYNTHESE", [p for p in paths if "synthese-fusionnee" in p])
print("SONDE", [p for p in paths if "sonde" in p])
print("COMPLET", co[:10])
print("AUTRES", [p for p in paths if p not in et and "/complet/" not in p][:20])
