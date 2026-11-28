import hashlib
import json
import os
import re
import shutil
import subprocess
import urllib.request
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
WT_B8 = SCRATCH / "wt-b8-puissance"

# 1. État en direct de 62647167 (sondes v2, 72 cœurs) et de la branche suite
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

# 2. Contrôle strictement aveugle du seul booléen audit_de_symetrie_declenche dans lecture-sondes-barreau8-v1.json
print("\n=== 2. CONTRÔLE DU BOOLÉEN D'AUDIT BARREAU 8 (ZÉRO CHIFFRE AFFICHÉ) ===")
p_out_b8 = WT_B8 / "diag/20261126-083755-lecture-sondes-barreau8/lecture-sondes-barreau8-v1.json"
doc_b8 = json.loads(p_out_b8.read_text("utf-8"))
res_b8 = doc_b8.get("resultat", doc_b8)
bloc_audit = res_b8.get("declencheurs_de_l_audit")
if bloc_audit is None:
    audit_decl = False
    print("declencheurs_de_l_audit: clé absente (vaut False)")
else:
    audit_decl = bool(bloc_audit.get("audit_de_symetrie_declenche"))
    print("audit_de_symetrie_declenche:", audit_decl)
    if audit_decl:
        # Afficher uniquement les identifiants booléens de déclencheurs actifs, jamais de valeurs chiffrées
        actifs = [k for k, v in bloc_audit.items() if k != "audit_de_symetrie_declenche" and bool(v) is True and isinstance(v, bool)]
        cles_audit = sorted(bloc_audit.keys())
        print("Clés de declencheurs_de_l_audit:", cles_audit)
        print("Booléens actifs:", actifs)

# Vérifier le séparateur dans registres/sondes-iib-v1.md
reg_iib_txt = (WT_B8 / "registres/sondes-iib-v1.md").read_text("utf-8")
for ln in reg_iib_txt.splitlines():
    if "LECTURE-SONDES-IIB" in ln:
        print("Ligne registre propre:", ln)

# 3. Lister les pièces de docs/notes/barreau8-conductrice-lecture-sondes-v1/
print("\n=== 3. PIÈCES DE LA CONDUCTRICE BARREAU 8 ===")
cond_dir = WT_B8 / "docs/notes/barreau8-conductrice-lecture-sondes-v1"
for f in sorted(cond_dir.iterdir()):
    print(f"  {f.name} ({f.stat().st_size} octets)")

for f in sorted(cond_dir.glob("*.md")):
    if f.name not in ("mandat-lecteur-sondes-barreau8-v3.md", "mandat-juge-lecture-sondes-barreau8-v3.md"):
        print(f"\n--- {f.name} ---")
        txt_f = f.read_text("utf-8").splitlines()
        print("\n".join(txt_f[:140]))
        if len(txt_f) > 140:
            print("...\n" + "\n".join(txt_f[-80:]))

# 4. Préparer les scripts relais et les deux lots (<= 10 fichiers) pour le juge de Barreau 8
rel_juge = SCRATCH / "relais-juge-b8"
rel_juge.mkdir(parents=True, exist_ok=True)
cmd_j1 = (
    "cd C:/Users/lciri/.gemini/antigravity-cli/brain/cd7c89b9-9752-4dac-b846-2c58efd89737/scratch/wt-b8-puissance "
    "&& sha256sum prereg/lecture-sondes-barreau8-v1.md "
    "prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md "
    "prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md "
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json "
    "docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json "
    "docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-1-v1.json "
    "docs/notes/barreau8-cote-moniteurs-sorties-v1/comparaison-interface-v6-v7-v2.json "
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-ordre-course-lue-additif-1-v1.json "
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json "
    "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-lecteur-sondes-barreau8-v3.md "
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md "
    "registres/qui-a-lu-quoi-v23.md "
    "diag/20261126-083755-lecture-sondes-barreau8/lecture-sondes-barreau8-v1.json "
    "&& PYTHONPATH=src C:/Users/lciri/.gemini/antigravity-cli/brain/cd7c89b9-9752-4dac-b846-2c58efd89737/scratch/venv-py314/Scripts/python.exe "
    "-m controle_ia.scellement verifier "
    "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-juge-lecture-sondes-barreau8-v3.md "
    "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-lecteur-sondes-barreau8-v3.md "
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md "
    "registres/qui-a-lu-quoi-v23.md "
    "diag/20261126-083755-lecture-sondes-barreau8/lecture-sondes-barreau8-v1.json "
    "&& grep -n -E '^\\| *(SCELLEMENT-SONDES-IIB|SCELLEMENT-ADDITIF-1-SONDES-IIB|SCELLEMENT-ADDITIF-2-SONDES-IIB|CODE-PASSE-IIB|CODE-LECTURE-SONDES-IIB|LIVRAISON-PASSE-IIB|ETATS-COURSE-IIB|LECTURE-SONDES-IIB) *\\|' registres/sondes-iib-v1.md\n"
)
(rel_juge / "juge_etape1_sans_audit.sh").write_bytes(cmd_j1.encode("utf-8"))

lot1 = SCRATCH / "paquet-juge-b8-lot1"
lot2 = SCRATCH / "paquet-juge-b8-lot2"
lot1.mkdir(parents=True, exist_ok=True)
lot2.mkdir(parents=True, exist_ok=True)

fichiers_lot1 = [
    "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-juge-lecture-sondes-barreau8-v3.md",
    "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-lecteur-sondes-barreau8-v3.md",
    "prereg/lecture-sondes-barreau8-v1.md",
    "prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md",
    "prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md",
    "diag/20261126-083755-lecture-sondes-barreau8/lecture-sondes-barreau8-v1.json",
]
fichiers_lot2 = [
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json",
    "docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json",
    "docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-1-v1.json",
    "docs/notes/barreau8-cote-moniteurs-sorties-v1/comparaison-interface-v6-v7-v2.json",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-ordre-course-lue-additif-1-v1.json",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json",
]
for rel_p in fichiers_lot1:
    shutil.copyfile(WT_B8 / rel_p, lot1 / Path(rel_p).name)
for rel_p in fichiers_lot2:
    shutil.copyfile(WT_B8 / rel_p, lot2 / Path(rel_p).name)
print(f"\nPAQUETS_JUGE_B8_PRETS: lot1={len(fichiers_lot1)} fichiers, lot2={len(fichiers_lot2)} fichiers")
