import hashlib
import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
WT_DR = SCRATCH / "lecture-dr"
WT_B8 = SCRATCH / "wt-b8-puissance"
PAQ_5D = SCRATCH / "paquet-juge-r13-doses-critere3"

# 1. Suivi de l'instance 62647167 (fin de grille 13,x !)
print("=== 1. ÉTAT VAST.AI 62647167 & BRANCHE SUITE SONDES V2 ===")
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()

def mask(txt: str) -> str:
    if vast_key:
        txt = txt.replace(vast_key, "***")
    return re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{8,}", r"\1***", txt)

req = urllib.request.Request(
    "https://console.vast.ai/api/v0/instances/",
    headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
)
with urllib.request.urlopen(req, timeout=20) as resp:
    insts = json.loads(resp.read().decode("utf-8")).get("instances", [])
i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
if i64:
    print(f"62647167: status={i64.get('actual_status')} | cpu={i64.get('cpu_util')}% | mem={i64.get('mem_usage')}Go")
    try:
        logs = subprocess.check_output(
            [str(VAST_EXE), "logs", "62647167"],
            env={**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"},
            text=True, timeout=20, stderr=subprocess.STDOUT,
        )
        print("  dernières lignes:", mask(" | ".join(logs.splitlines()[-5:])))
    except Exception:
        pass
else:
    print("62647167: ABSENTE (terminée et autodétruite !)")

ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite sondes v2:", ls_suite or "(calcul en cours)")

# 2. Extraire sans rien afficher les 80 actions R4 tirées par graine pour l'étape 5(d)
print("\n=== 2. PRÉPARATION DE pieces-r4-lecteur-texte-dose-reponse-v1.json ===")
p_aud_lt = WT_DR / "diag/20261126-095224-lecteur-du-texte-dose-reponse/audit-r4-lecteur-du-texte-dose-reponse.json"
p_det_lt = WT_DR / "diag/20261126-095224-lecteur-du-texte-dose-reponse/lecteur-du-texte-dose-reponse-details.json"
aud_lt = json.loads(p_aud_lt.read_text("utf-8"))
det_lt = json.loads(p_det_lt.read_text("utf-8"))
print("Clés de lecteur-du-texte-dose-reponse-details.json:", sorted(det_lt.keys()))
ech_lt = aud_lt["echantillons"]
for c, v in ech_lt.items():
    if isinstance(v, list):
        print(f"  echantillons[{c}]: len={len(v)}, type_elem={type(v[0]).__name__ if v else 'vide'}")
    elif isinstance(v, dict):
        print(f"  echantillons[{c}]: dict keys={sorted(v.keys())}")

# Charger les 64 blocs scellés pour joindre texte + mesures aux 80 actions tirées
mes_par_cle = {}
txt_par_cle = {}
txt_par_quad = {}
for bdir in sorted((WT_DR / "donnees/20261125-093202-dose-reponse/blocs").glob("*")):
    for rl in (bdir / "mesures.jsonl").read_text("utf-8").splitlines():
        m = json.loads(rl)
        mes_par_cle[m["cle"]] = m
    for rt in (bdir / "textes.jsonl").read_text("utf-8").splitlines():
        t = json.loads(rt)
        if "cle" in t:
            txt_par_cle[t["cle"]] = t
        if all(k in t for k in ("condition", "tache", "replique", "pas")):
            txt_par_quad[(t["condition"], t["tache"], t["replique"], t["pas"])] = t

actions_r4_lt = {}
total_ext = 0
for c, v in sorted(ech_lt.items()):
    liste_items = v if isinstance(v, list) else (v.get("actions") or v.get("cles") or [])
    out_c = []
    for item in liste_items:
        cle = item if isinstance(item, str) else (item.get("cle") or item.get("id"))
        m = mes_par_cle[cle]
        t = txt_par_cle.get(cle) or txt_par_quad.get((m["condition"], m["tache"], m["replique"], m["pas"]))
        out_c.append({"entree_audit": item, "cle": cle, "mesures": m, "texte_jsonl": t})
        total_ext += 1
    actions_r4_lt[c] = out_c

piece_r4_lt = {
    "objet": "Échantillons complets (20 actions par condition concernée) pour l'audit de symétrie R4 du lecteur du texte (G0-critere-3-designation-course-v1.md, section Seuil)",
    "run_lecteur_texte": "20261126-095224-lecteur-du-texte-dose-reponse",
    "audit_r4_sha256": hashlib.sha256(p_aud_lt.read_bytes()).hexdigest(),
    "details_sha256": hashlib.sha256(p_det_lt.read_bytes()).hexdigest(),
    "motifs": aud_lt.get("motifs"),
    "conditions_concernees": aud_lt.get("conditions_concernees"),
    "echantillons_complets_par_condition": actions_r4_lt,
}
out_r4_lt = PAQ_5D / "pieces-r4-lecteur-texte-dose-reponse-v1.json"
raw_r4_lt = (json.dumps(piece_r4_lt, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
out_r4_lt.write_bytes(raw_r4_lt)
sha_r4_lt = hashlib.sha256(raw_r4_lt).hexdigest()
print(f"PIECES_R4_LECTEUR_TEXTE_OK: {out_r4_lt.name} ({len(raw_r4_lt)}o, {total_ext} actions) sha256={sha_r4_lt}")

# 3. Inspecter les modules de code de lecture de Barreau 8 (pour l'auditeur R4 de Barreau 8)
print("\n=== 3. MODULES DU BORDEREAU CODE-LECTURE-SONDES-IIB (BARREAU 8) ===")
bord_b8 = json.loads((WT_B8 / "docs/notes/code-lecture-sondes-v6-v1/bordereau-code-lecture-sondes-barreau8-v6.json").read_text("utf-8"))
print("Clés bordereau code lecture B8:", sorted(bord_b8.keys()))
for nom_m, info_m in sorted(bord_b8.get("modules", {}).items()):
    print(f"  {nom_m}: {info_m}")
if "notice" in bord_b8:
    not_p = WT_B8 / bord_b8["notice"]["chemin"]
    print("\n--- Notice du code de lecture B8 ---", not_p)
    if not_p.is_file():
        print("\n".join(not_p.read_text("utf-8").splitlines()[:90]))

# Vérifier aussi les clés de premier niveau de lecture-sondes-barreau8-v1.json (sans aucun chiffre !)
doc_b8 = json.loads((WT_B8 / "diag/20261126-083755-lecture-sondes-barreau8/lecture-sondes-barreau8-v1.json").read_text("utf-8"))
res_b8 = doc_b8.get("resultat", doc_b8)
print("\nClés racine de lecture-sondes-barreau8-v1.json:", sorted(res_b8.keys()))

# 4. Vérifier s'il existe déjà un texte scellé de lecture des sondes pour l'étape 5(e) du critère 3 sur origin/main
prereg_main = subprocess.check_output(["git", "-C", str(REPO), "ls-tree", "--name-only", "origin/main:prereg"], text=True).splitlines()
print("\n=== 4. FICHIERS prereg/ SUR ORIGIN/MAIN (POUR ÉTAPE 5e CRITÈRE 3) ===")
print([f for f in prereg_main if any(w in f.lower() for w in ("sondes", "t0.7", "t07", "critere-3", "dose"))])
