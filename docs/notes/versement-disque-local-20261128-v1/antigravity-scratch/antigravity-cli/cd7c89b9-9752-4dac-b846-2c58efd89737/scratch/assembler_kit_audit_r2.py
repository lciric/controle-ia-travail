"""Localise toutes les pièces primaires demandées par l'auditeur R2 et assemble un .zip étanche (R13)."""
import hashlib
import json
import re
import subprocess
import zipfile
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT_DR = SCRATCH / "lecture-dr"
OUT_ZIP = SCRATCH / "kit-primaire-audit-r2.zip"

# 1. Résolution de la racine principale du dépôt via git worktree list
wt_out = subprocess.check_output(["git", "-C", str(WT_DR), "worktree", "list", "--porcelain"], text=True, encoding="utf-8")
roots = [Path(line.split(" ", 1)[1].strip()) for line in wt_out.splitlines() if line.startswith("worktree ")]
MAIN_REPO = roots[0]
print(f"RACINE_PRINCIPALE_DEPOT : {MAIN_REPO}")
print(f"WORKTREE_LECTURE_DR     : {WT_DR}\n")


def read_repo_bytes(rel_path: str) -> tuple[bytes | None, str]:
    for r in roots:
        p = r / rel_path
        if p.is_file():
            return p.read_bytes(), str(p)
    # Repli via objet Git si masqué par sparse-checkout
    res = subprocess.run(["git", "-C", str(MAIN_REPO), "show", f"HEAD:{rel_path}"], capture_output=True)
    if res.returncode == 0:
        return res.stdout, f"git:HEAD:{rel_path} (dans {MAIN_REPO})"
    return None, "INTROUVABLE"


all_tracked = subprocess.check_output(
    ["git", "-C", str(MAIN_REPO), "ls-tree", "-r", "--name-only", "HEAD"], text=True, encoding="utf-8"
).splitlines()

added: dict[str, bytes] = {}
manifest_kit: list[dict] = []


def add_piece(arc_name: str, data: bytes, origin: str) -> None:
    assert not arc_name.endswith((".npz", ".safetensors", ".pt", ".bin")), f"Interdit R13: {arc_name}"
    sha = hashlib.sha256(data).hexdigest()
    added[arc_name] = data
    manifest_kit.append({"archive_path": arc_name, "origin": origin, "bytes": len(data), "sha256": sha})
    print(f"[OK] {arc_name}\n     <- {origin} ({len(data)} octets, sha256={sha[:12]}...)")


# --- GROUPE 1 : Pièces normatives scellées + extraits/fichiers registres ---
exact_group1_and_4 = [
    "prereg/T0.7-sondes-v0-v1.md",
    "prereg/G0-critere-3-designation-course-v1.md",
    "prereg/lecture-sondes-barreau8-v1.md",
    "diag/20261126-082824-dose-reponse-lecture/lecture-cout-dose-reponse.json",
    "diag/20261126-095224-lecteur-du-texte-dose-reponse/doses-jugees-critere-3.json",
    "diag/20261126-095224-lecteur-du-texte-dose-reponse/issue-lecteur-du-texte-dose-reponse.json",
    "diag/20261126-095224-lecteur-du-texte-dose-reponse/audit-r4-lecteur-du-texte-dose-reponse.json",
    "runs/20261126-095224-lecteur-du-texte-dose-reponse/manifeste.json",
    "runs/20261126-082824-dose-reponse-lecture/manifeste.json",
]
for rel in exact_group1_and_4:
    b, orig = read_repo_bytes(rel)
    if b is not None:
        add_piece(rel, b, orig)
    else:
        print(f"[ABSENT] {rel}")

re_norm = re.compile(r"\b(P-066|N-026|N-029|N-054|N-056|N-063|R12|R13)\b")
re_priv_leak = re.compile(r"PRIVATE\s+NOTE|inflate\s+the\s+cost\s+by", re.I)

for rel in all_tracked:
    if rel.startswith(("registres/", "docs/")) and rel.endswith(".md"):
        b, orig = read_repo_bytes(rel)
        if b and re_norm.search(b.decode("utf-8", errors="ignore")):
            txt = b.decode("utf-8", errors="ignore")
            if re_priv_leak.search(txt):
                print(f"[EXCLU-R13-CONSIGNE] {rel} ({orig}) — contient un motif de consigne privée, à filtrer si besoin")
            else:
                add_piece(rel, b, orig)

# --- GROUPE 2 : taches-evaluation.json, partition-taches et entrées de manifeste.json ---
extra_paths_from_manifest: set[str] = set()
man_bytes = added.get("runs/20261126-095224-lecteur-du-texte-dose-reponse/manifeste.json")
if man_bytes:
    for m in re.finditer(r'[\w./\\-]+(?:\.json|\.py|\.md)', man_bytes.decode("utf-8", errors="ignore")):
        cand = m.group(0).replace("\\", "/").lstrip("./")
        if not cand.endswith((".npz", ".safetensors")):
            extra_paths_from_manifest.add(cand)

for rel in sorted(set(all_tracked) | extra_paths_from_manifest | {"donnees/20261007-082440-t05-extraction/taches-evaluation.json"}):
    if any(k in rel for k in ("taches-evaluation.json", "partition", "centres")):
        if rel.endswith(".json"):
            b, orig = read_repo_bytes(rel)
            if b is not None:
                if "taches-evaluation.json" in rel and len(b) > 600_000:
                    data_json = json.loads(b.decode("utf-8"))
                    items = data_json if isinstance(data_json, list) else data_json.get("taches", data_json)
                    sample = {
                        "source_path": rel,
                        "source_sha256": hashlib.sha256(b).hexdigest(),
                        "total_count": len(items) if hasattr(items, "__len__") else None,
                        "sample_3_tasks": items[:3] if isinstance(items, list) else items,
                    }
                    add_piece("echantillons/taches-evaluation-3-exemples.json", json.dumps(sample, indent=2, ensure_ascii=False).encode("utf-8"), orig)
                else:
                    add_piece(rel, b, orig)

# --- GROUPE 3 : Code Python des instruments (sans gabarits de consignes privées) ---
re_py_keep = re.compile(
    r"(prereg|probleme|manifeste|graine|cout|dr[_-]?6|lecteur|mots_et_cout|jetons_notes|SondeLineaireJetons|sondes|bpe)",
    re.I,
)
for rel in all_tracked:
    if rel.endswith(".py") and (rel.startswith(("src/", "controle_ia/", "harnais/", "scripts/", "premier_test_ia/")) or rel in extra_paths_from_manifest):
        b, orig = read_repo_bytes(rel)
        if b is None:
            continue
        txt = b.decode("utf-8", errors="ignore")
        if re_py_keep.search(rel) or re_py_keep.search(txt):
            if re_priv_leak.search(txt):
                print(f"[EXCLU-R13-CODE] {rel} ({orig}) — motif de consigne privée détecté")
            else:
                add_piece(rel, b, orig)

# --- GROUPE 4 : 1 seule ligne honnete de mesures.jsonl et textes.jsonl ---
dr_dirs = [r / "donnees/20261125-093202-dose-reponse/blocs" for r in roots if (r / "donnees/20261125-093202-dose-reponse/blocs").is_dir()]
if dr_dirs:
    blocs_root = dr_dirs[0]
    hon_mesure, hon_texte, hon_cle = None, None, None
    for mf in sorted(blocs_root.glob("*/mesures.jsonl")):
        with mf.open("r", encoding="utf-8") as f:
            for raw_line in f:
                if not raw_line.strip():
                    continue
                obj = json.loads(raw_line)
                if obj.get("condition") == "honnete" or mf.parent.name == "honnete":
                    hon_mesure = (raw_line, str(mf))
                    hon_cle = obj.get("cle")
                    break
        if hon_mesure:
            tf = mf.parent / "textes.jsonl"
            if tf.is_file():
                with tf.open("r", encoding="utf-8") as f:
                    for raw_t in f:
                        if not raw_t.strip():
                            continue
                        ot = json.loads(raw_t)
                        if (hon_cle and ot.get("cle") == hon_cle) or ot.get("condition") == "honnete":
                            hon_texte = (raw_t, str(tf))
                            break
            break
    if hon_mesure:
        add_piece("echantillons/1-ligne-honnete-mesures.jsonl", hon_mesure[0].encode("utf-8"), hon_mesure[1])
    if hon_texte:
        add_piece("echantillons/1-ligne-honnete-textes.jsonl", hon_texte[0].encode("utf-8"), hon_texte[1])
else:
    print("[INFO] Dossier donnees/20261125-093202-dose-reponse/blocs non trouvé sous les worktrees Git ; vérifie son emplacement externe éventuel.")

# Écriture finale du .zip avec manifeste SHA-256
added["MANIFESTE-KIT-AUDIT-R2.json"] = json.dumps(manifest_kit, indent=2, ensure_ascii=False).encode("utf-8")
with zipfile.ZipFile(OUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for name, content in sorted(added.items()):
        assert not name.endswith((".npz", ".safetensors")), name
        zf.writestr(name, content)

print(f"\nKIT PRÊT : {OUT_ZIP} ({OUT_ZIP.stat().st_size / 1024:.1f} Ko, {len(added)} fichiers, 0 .npz)")
