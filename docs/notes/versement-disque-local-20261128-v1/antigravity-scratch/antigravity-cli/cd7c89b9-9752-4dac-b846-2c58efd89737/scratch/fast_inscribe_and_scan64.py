import base64
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
VAST = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
INST_ID = "62498862"
REPO_SLUG = "lciric/controle-ia-travail"

secrets = []
for k in ("HF_TOKEN", "VAST_API_KEY", "HCLOUD_TOKEN", "HETZNER_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2"):
    v = os.environ.get(k, "").strip()
    if len(v) >= 8:
        secrets.append(v)
gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=20).strip()
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

def gh_api(method: str, path: str, payload=None):
    url = f"https://api.github.com/repos/{REPO_SLUG}/{path.lstrip('/')}"
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={
            "Authorization": f"Bearer {gh_tok}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "controle-ia-mere",
        },
    )
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))

# 1. Atomic fast-forward inscription on origin/main via GitHub Git Data API
head_ref = gh_api("GET", "git/ref/heads/main")
head_sha = head_ref["object"]["sha"]
head_commit = gh_api("GET", f"git/commits/{head_sha}")
base_tree_sha = head_commit["tree"]["sha"]

go_obj = gh_api("GET", f"contents/registres/go.md?ref={head_sha}")
dec_obj = gh_api("GET", f"contents/registres/decisions.md?ref={head_sha}")

go_blob = gh_api("GET", f"git/blobs/{go_obj['sha']}")
dec_blob = gh_api("GET", f"git/blobs/{dec_obj['sha']}")

go_txt = base64.b64decode(go_blob["content"]).decode("utf-8")
dec_txt = base64.b64decode(dec_blob["content"]).decode("utf-8")

if "2026-11-25T16:12:48Z" not in go_txt:
    go_nums = [int(m.group(1)) for m in re.finditer(r"GO-2026-11-25-(\d+)", go_txt)]
    next_go_num = (max(go_nums) + 1) if go_nums else 1
    go_id = f"GO-2026-11-25-{next_go_num:02d}"

    r_nums = [int(m.group(1)) for m in re.finditer(r"^- R-(\d+) ", dec_txt, re.M) if int(m.group(1)) < 9000]
    next_r_num = max(r_nums) + 1
    r_id = f"R-{next_r_num}"
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

    go_line = (
        f"| {go_id} | 2026-11-25 | calcul | Mots de Lazar tapés le 2026-11-25T16:12:48Z (« B go ») et le 2026-11-25T16:21:33Z "
        f"(« go 64 coeurs pour aller plus vite ») dans la session mère Antigravity (Gemini 4 Carbon High, conversation cd7c89b9). "
        f"Option B retenue pour les diagnostics préalables des sondes boîte blanche version 2 (`prereg/diagnostics-prealables-sondes-v1.md` "
        f"`e8dca00b…` et additif `40a9e45c…`) : (1) corriger le défaut `nproc` dans une amorce version 3 contre-lue en classe B "
        f"(`N_WORKERS=$(nproc --all)` avant `OMP_NUM_THREADS=1`, garde multicœur, branche dédiée `calcul/sondes-v2-epreuve-plantee-v4-suite` "
        f"sans écraser les 13 tranches scellées `[0, 130)`), louer une instance multiprocesseur d'au moins 64 cœurs sur Vast.ai "
        f"(sous le reliquat de `GO-2026-11-24-02` et `GO-2026-11-24-15`, attendu ≈ 1 à 4 USD en une vague d'environ 1 h 30, coupure dure 12 USD / 6 h, "
        f"autodestruction R10 par identifiant numérique exact hors intouchables) pour achever `[130, 500)` du mode `etalon` sur les 52 cases, "
        f"sceller la synthèse fusionnée `[0, 500)` et chronométrer en parallèle 1 réplique isolée du mode `complet` ; "
        f"(2) nœud explicite du directeur (`prereg/diagnostics-prealables-sondes-v1.md` lignes 92 et 108) : dissocier l'ouverture des deux "
        f"questions gouvernées par le mode `etalon` (Q1 identité des poids et Q2 étalon de transport avec contrôle d'intensité) du mode `complet` "
        f"et de la question Q3 (rejeu croisé, contrôle du chemin absent dans la note des effectifs `7338a3dc…`, ajournée après le 1er décembre) ; "
        f"préparer et contre-lire en parallèle en classe B le programme aveugle d'étape 4 pour ouvrir Q1 et Q2 dès le scellement de `[0, 500)`, "
        f"puis verdict d'étape 5 par juge neuf (R13). "
        f"| sous GO-2026-11-24-02 (reste ≈ 58,96 USD sur 68 USD ; coupure 12 USD) | 2026-12-01 | Lazar | GO-2026-11-24-02 ; GO-2026-11-24-15 ; GO-2026-11-24-49 ; {r_id} |"
    )

    r_line = (
        f"- {r_id} ({now_iso}) — {go_id} inscrit (« B go » à 16:12:48Z puis « go 64 coeurs pour aller plus vite » à 16:21:33Z, "
        f"après l'audit en 4 points `0a369222` ayant identifié le défaut `OMP_NUM_THREADS=1` -> `nproc=1` de l'amorce v2) : "
        f"(1) reprise sur machine Vast.ai >= 64 cœurs de `[130, 500)` du mode `etalon` (62 tranches de 6 répliques en une vague ~1 h 30) "
        f"+ sonde chronométrée en parallèle d'une réplique du mode `complet` sous le reliquat de `GO-2026-11-24-02` (coupure 12 USD / 6 h), "
        f"par amorce v3 contre-lue en classe B sans recalcul ni écrasement des 13 tranches `[0, 130)` ; "
        f"(2) nœud de découplage autorisant l'ouverture immédiate de Q1 (identité des poids) et Q2 (étalon de transport) dès la synthèse "
        f"fusionnée `[0, 500)` scellée, par programme aveugle d'étape 4 contre-lu en classe B puis juge neuf R13, Q3 restant non ouverte. "
        f"Rappel quotidien de 18 h Paris (17:00Z) remis à Lazar (réponse à Cameron Jordan sous `docs/notes/contacts-externes-v1/` ; "
        f"note d'entretien contrôle diffus v7 `docs/notes/veille-organismes-ideation-v2/note-entretien-controle-diffus-v7.md` et lecture des trois sources) : "
        f"rappel du 25 fait."
    )

    new_go = (go_txt.rstrip("\r\n") + "\n" + go_line + "\n").replace("\r\n", "\n")
    new_dec = (dec_txt.rstrip("\r\n") + "\n" + r_line + "\n").replace("\r\n", "\n")

    b_go = gh_api("POST", "git/blobs", {"content": base64.b64encode(new_go.encode("utf-8")).decode("ascii"), "encoding": "base64"})
    b_dec = gh_api("POST", "git/blobs", {"content": base64.b64encode(new_dec.encode("utf-8")).decode("ascii"), "encoding": "base64"})

    new_tree = gh_api("POST", "git/trees", {
        "base_tree": base_tree_sha,
        "tree": [
            {"path": "registres/go.md", "mode": "100644", "type": "blob", "sha": b_go["sha"]},
            {"path": "registres/decisions.md", "mode": "100644", "type": "blob", "sha": b_dec["sha"]},
        ],
    })
    new_commit = gh_api("POST", "git/commits", {
        "message": f"{r_id} : inscrire {go_id} Option B 64 coeurs sondes v2 (reprise etalon 130-500 et decouplage Q1-Q2)",
        "tree": new_tree["sha"],
        "parents": [head_sha],
    })
    gh_api("PATCH", "git/refs/heads/main", {"sha": new_commit["sha"], "force": False})
    print(f"INSCRIBED_FAST_OK: {go_id} {r_id} commit={new_commit['sha']}")
else:
    print(f"ALREADY_INSCRIBED at head={head_sha}")

# 2. Check calcul/dose-reponse-v1 commit & message via GitHub API
dr_ref = gh_api("GET", "git/ref/heads/calcul/dose-reponse-v1")
dr_sha = dr_ref["object"]["sha"]
dr_commit = gh_api("GET", f"git/commits/{dr_sha}")
print(f"DR_BRANCH_HEAD: {dr_sha[:12]} date={dr_commit['committer']['date']} msg={mask(dr_commit['message'])!r}")

# 3. Check D-10 CPU progress
p_diag = SCRATCH / "wt-b8-puissance" / "diag" / "20261125-083300-puissance-barreau8"
print("D10_DIAG_EXISTS:", p_diag.exists())
try:
    ps_out = subprocess.check_output(
        ["powershell", "-NoProfile", "-Command",
         "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*puissance*' } | ForEach-Object { $p = Get-Process -Id $_.ProcessId -ErrorAction SilentlyContinue; if ($p) { \"$($p.Id) CPU=$([math]::Round($p.CPU,1))s WS=$([math]::Round($p.WorkingSet64/1MB,1))MB\" } }"],
        text=True, timeout=20,
    ).strip()
    print("D10_PROC:", ps_out or "(not found)")
except Exception as e:
    print("D10_ERR:", repr(e))

# 4. Check Vast.ai credit + >= 64 effective core offers
req_u = urllib.request.Request("https://console.vast.ai/api/v0/users/current/", headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"})
with urllib.request.urlopen(req_u, timeout=20) as resp:
    u = json.loads(resp.read().decode("utf-8"))
print("VAST_CREDIT:", u.get("credit"))

q = {
    "verified": {"eq": True}, "external": {"eq": False}, "rentable": {"eq": True}, "rented": {"eq": False},
    "datacenter": {"eq": True}, "reliability2": {"gte": 0.985}, "cpu_cores_effective": {"gte": 64},
    "cpu_ram": {"gte": 96000}, "disk_space": {"gte": 50}, "dph_total": {"lte": 2.00},
    "order": [["dph_total", "asc"]], "type": "on-demand", "limit": 15,
}
req_v = urllib.request.Request(
    "https://console.vast.ai/api/v0/bundles/", data=json.dumps(q).encode("utf-8"),
    headers={"Authorization": f"Bearer {vast_key}", "Content-Type": "application/json", "Accept": "application/json"}, method="POST"
)
with urllib.request.urlopen(req_v, timeout=25) as resp:
    offers = json.loads(resp.read().decode("utf-8")).get("offers", [])
print(f"VAST_64CORE_OFFERS ({len(offers)}):")
for o in offers[:12]:
    eff_c = o.get("cpu_cores_effective")
    phys_c = o.get("cpu_cores")
    dph = o.get("dph_total")
    storage_gb_m = o.get("storage_cost") or 0
    print(f"  id={o.get('id')} mach={o.get('machine_id')} cpu={o.get('cpu_name')!r} eff_c={eff_c} phys_c={phys_c} "
          f"ram_gb={round((o.get('cpu_ram') or 0)/1024,1)} gpu={o.get('gpu_name')}x{o.get('num_gpus')} "
          f"dph={dph:.4f} stor={storage_gb_m:.3f} rel={o.get('reliability2'):.4f} loc={o.get('geolocation')}")
