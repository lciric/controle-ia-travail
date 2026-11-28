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

# 1. Vérifier si l'instance Vast.ai 62647167 (sondes v2, 72 cœurs) a terminé et poussé sa branche
print("=== 1. ÉTAT VAST.AI 62647167 & SONDES V2 ===")
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
ids_vast = sorted(str(i.get("id")) for i in insts)
print("Instances Vast présentes:", ids_vast)
i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
if i64:
    print(f"62647167: status={i64.get('actual_status')} | cpu={i64.get('cpu_util')}% | mem={i64.get('mem_usage')}Go")
    try:
        logs = subprocess.check_output(
            [str(VAST_EXE), "logs", "62647167"],
            env={**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"},
            text=True, timeout=20, stderr=subprocess.STDOUT,
        )
        print("  dernières lignes:", mask(" | ".join(logs.splitlines()[-6:])))
    except Exception:
        pass
else:
    print("62647167: ABSENTE (terminée et autodétruite !)")

ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite sondes v2:", ls_suite or "(pas encore poussée)")
if ls_suite:
    subprocess.run(["git", "-C", str(REPO), "fetch", "origin", "calcul/sondes-v2-epreuve-plantee-v4-suite"], check=True)
    f_suite = subprocess.check_output(["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", "FETCH_HEAD"], text=True).splitlines()
    et_json = [f for f in f_suite if "etalon/rapport-monde-plante-v4-etalon-" in f and f.endswith(".json")]
    autres = [f for f in f_suite if "rapport-monde-plante-v4-etalon-" not in f]
    print(f"Rapports étalon sur branche suite: {len(et_json)} | Autres fichiers: {autres}")

# 2. Construire UN SEUL fichier compact (< 250 Ko) pour débloquer immédiatement juge-r13-doses-jugees-critere3-temporaire-20261126-01
print("\n=== 2. CONSTRUCTION DU COMPLÉMENT COMPACT POUR LE JUGE 5(d) ===")
p_aud_lt = WT_DR / "diag/20261126-095224-lecteur-du-texte-dose-reponse/audit-r4-lecteur-du-texte-dose-reponse.json"
p_det_lt = WT_DR / "diag/20261126-095224-lecteur-du-texte-dose-reponse/lecteur-du-texte-dose-reponse-details.json"
p_cout = WT_DR / "diag/20261126-082824-dose-reponse-lecture/lecture-cout-dose-reponse.json"
p_man_lt = WT_DR / "runs/20261126-095224-lecteur-du-texte-dose-reponse/manifeste.json"

aud_lt = json.loads(p_aud_lt.read_text("utf-8"))
det_lt = json.loads(p_det_lt.read_text("utf-8"))
cout_doc = json.loads(p_cout.read_text("utf-8"))
man_lt = json.loads(p_man_lt.read_text("utf-8"))

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

ech_80 = {}
nb_80 = 0
for c, items in sorted(aud_lt["echantillons"].items()):
    liste = items if isinstance(items, list) else (items.get("actions") or items.get("cles") or [])
    ech_80[c] = []
    for it in liste:
        cle = it if isinstance(it, str) else (it.get("cle") or it.get("id"))
        m = mes_par_cle[cle]
        t = txt_par_cle.get(cle) or txt_par_quad.get((m["condition"], m["tache"], m["replique"], m["pas"]))
        ech_80[c].append({"cle": cle, "mesures": m, "texte_jsonl": t})
        nb_80 += 1

# Extraire la fin de lecteur-du-texte-dose-reponse-details.json qui avait été tronquée dans le contexte Gemini
fin_details = {}
for k, v in det_lt.items():
    if k == "modeles_base_b" and isinstance(v, dict):
        # Garder les témoins de fin (dont mention_premier_test et temoin_premier_test) avec top 25 poids + constantes
        resume_b = {}
        for j_nom, j_val in v.items():
            if j_nom in ("mention_premier_test", "temoin_premier_test", "saboteur_premier_test", "consigne_neutre", "consigne_benigne"):
                resume_b[j_nom] = j_val
        fin_details["modeles_base_b_temoins_fin_de_fichier"] = resume_b
    elif k not in ("modeles_base_a", "modeles_base_b"):
        fin_details[k] = v

complement_5d = {
    "objet": "Complément intégral R4 + pièces tronquées/manquantes pour juge-r13-doses-jugees-critere3-temporaire-20261126-01",
    "sources_sha256": {
        "lecture_cout_dose_reponse_json": hashlib.sha256(p_cout.read_bytes()).hexdigest(),
        "manifeste_lecteur_texte_json": hashlib.sha256(p_man_lt.read_bytes()).hexdigest(),
        "lecteur_du_texte_details_json": hashlib.sha256(p_det_lt.read_bytes()).hexdigest(),
        "audit_r4_lecteur_texte_json": hashlib.sha256(p_aud_lt.read_bytes()).hexdigest(),
    },
    "lecture_cout_dose_reponse_integral": cout_doc,
    "manifeste_lecteur_texte_resume": {
        k: v for k, v in man_lt.items() if k != "graines"
    },
    "graines_audit_r4_du_manifeste_lecteur_texte": {
        k: v for k, v in man_lt.get("graines", {}).items() if "audit-r4" in k
    },
    "fin_de_lecteur_du_texte_details_json": fin_details,
    "echantillons_80_actions_r4_complets": ech_80,
}

PAQ_5D.mkdir(parents=True, exist_ok=True)
out_comp = PAQ_5D / "complement-r4-et-cout-pour-juge-5d-v1.json"
raw_comp = (json.dumps(complement_5d, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
out_comp.write_bytes(raw_comp)
sha_comp = hashlib.sha256(raw_comp).hexdigest()
print(f"COMPLEMENT_5D_PRET_OK: {out_comp} ({len(raw_comp)} octets, {nb_80} actions)")
print(f"SHA256_COMPLEMENT_5D: {sha_comp}")

# 3. Inspecter les modules du code de lecture de Barreau 8 pour préparer le script mécanique des 6 points de l'audit R4
print("\n=== 3. MODULES CODE LECTURE BARREAU 8 (POUR AUDIT R4 d3) ===")
bord_b8 = json.loads((WT_B8 / "docs/notes/code-lecture-sondes-v6-v1/bordereau-code-lecture-sondes-barreau8-v6.json").read_text("utf-8"))
for nom_m, info_m in sorted(bord_b8.get("modules", {}).items()):
    print(f"  {nom_m}: {info_m['chemin']}")
doc_b8 = json.loads((WT_B8 / "diag/20261126-083755-lecture-sondes-barreau8/lecture-sondes-barreau8-v1.json").read_text("utf-8"))
print("Clés racine de lecture-sondes-barreau8-v1.json:", sorted(doc_b8.get("resultat", doc_b8).keys()))
