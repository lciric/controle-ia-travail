"""Reproduction locale, sans réseau ni dépense, de l'arrêt de l'étape A de T0.7 (R-2588) — v1.

Usage : .venv/bin/python -I reproduire_arret_cache_v1.py RACINE_DU_DEPOT
Chaque cas tourne dans un processus neuf, comme sur l'instance (préchargement et contrôle avant l'ouverture sont deux
processus) : la mémoire vive de la bibliothèque ne peut donc pas masquer ce qui est sur le disque.

Cache factice : exactement ce que `precharger_modele` laisse (les seuls fichiers de MOTIFS_PRECHARGEMENT), plus la liste
de l'arbre du dépôt que huggingface_hub écrit au cache lors d'un téléchargement en ligne (`trees/<commit>.json`).
Contenu des fichiers factice ; noms de l'arbre réel de meta-llama/Llama-3.1-8B-Instruct (dossier `original/` compris).
"""
import subprocess, sys, tempfile, textwrap
from pathlib import Path

RACINE = Path(sys.argv[1]).resolve()
DEPOT = "meta-llama/Llama-3.1-8B-Instruct"
REV = "0e9e39f249a16976918f6564b8830bc894c89659"
ARBRE = (["config.json", "generation_config.json", "tokenizer.json", "tokenizer_config.json",
          "special_tokens_map.json", "model.safetensors.index.json"]
         + [f"model-0000{i}-of-00004.safetensors" for i in range(1, 5)]
         + ["LICENSE", "README.md", "USE_POLICY.md", ".gitattributes", "original/consolidated.00.pth",
            "original/params.json", "original/tokenizer.model"])

ENTETE = textwrap.dedent(f"""
    import sys, json, fnmatch
    sys.path.insert(0, {str(RACINE / 'src')!r})
    from pathlib import Path
    DEPOT, REV, ARBRE = {DEPOT!r}, {REV!r}, {ARBRE!r}
""")

CAS = {
    "0-preparation": """
import huggingface_hub
from huggingface_hub import _tree_cache
from controle_ia.harnais.modeles import MOTIFS_PRECHARGEMENT
cache = Path(sys.argv[1]); stockage = cache / ("models--" + DEPOT.replace("/", "--"))
instant = stockage / "snapshots" / REV; instant.mkdir(parents=True); (stockage / "refs").mkdir()
(stockage / "refs" / "main").write_text(REV)
gardes = [f for f in ARBRE if any(fnmatch.fnmatch(f, m) for m in MOTIFS_PRECHARGEMENT)]
carte = {"weight_map": {f"couche.{i}": f"model-0000{i}-of-00004.safetensors" for i in range(1, 5)}}
for f in gardes:   # index des poids bien formé ; autres fichiers non vides
    (instant / f).write_text(json.dumps(carte) if f == "model.safetensors.index.json" else ("{}" if f.endswith(".json") else "x"))
entrees = {f: _tree_cache.TreeCacheEntry(size=1, blob_id="0" * 40, lfs_sha256=None, lfs_size=None, xet_hash=None)
           for f in ARBRE}
_tree_cache.write_tree_cache(str(stockage), REV, entrees)
print("huggingface_hub", huggingface_hub.__version__)
print("fichiers préchargés :", len(gardes), "sur", len(ARBRE), "; absents :", sorted(set(ARBRE) - set(gardes)))
print("liste de l'arbre sur disque :", (stockage / "trees" / f"{REV}.json").exists())
""",
    "1-controle-scelle-avec-liste": """
from controle_ia.t07 import reextraction_p3_v1 as r
try:
    print("PASSE :", r.revision_au_cache(DEPOT, REV, cache_dir=sys.argv[1]))
except Exception as e:
    print("ARRÊT :", type(e).__name__, ":", e)
""",
    "2-memes-motifs-que-le-prechargement": """
from huggingface_hub import snapshot_download
from controle_ia.harnais.modeles import MOTIFS_PRECHARGEMENT
try:
    d = snapshot_download(repo_id=DEPOT, revision=REV, local_files_only=True, cache_dir=sys.argv[1],
                          allow_patterns=list(MOTIFS_PRECHARGEMENT))
    print("PASSE : instantané", Path(d).name == REV)
except Exception as e:
    print("ARRÊT :", type(e).__name__, ":", e)
""",
    "3-chargeur-transformers-gabarits": """
import transformers
from transformers.utils.hub import list_repo_templates
try:
    print("transformers", transformers.__version__, "; PASSE : gabarits", list_repo_templates(DEPOT, local_files_only=True, revision=REV, cache_dir=sys.argv[1]))
except Exception as e:
    print("ARRÊT :", type(e).__name__, ":", e)
""",
    "4-chargeur-transformers-fichiers": """
from transformers.utils.hub import cached_files
try:
    r = cached_files(DEPOT, ["config.json", "tokenizer.json", "model-00001-of-00004.safetensors"], revision=REV,
                     cache_dir=sys.argv[1], local_files_only=True)
    print("PASSE :", [Path(x).name for x in r])
except Exception as e:
    print("ARRÊT :", type(e).__name__, ":", e)
""",
    "5-temoin-sans-liste-de-l-arbre": """
stockage = Path(sys.argv[1]) / ("models--" + DEPOT.replace("/", "--"))
(stockage / "trees" / f"{REV}.json").unlink()
from controle_ia.t07 import reextraction_p3_v1 as r
try:
    print("PASSE :", r.revision_au_cache(DEPOT, REV, cache_dir=sys.argv[1]))
except Exception as e:
    print("ARRÊT :", type(e).__name__, ":", e)
""",
}

with tempfile.TemporaryDirectory() as cache:
    for nom, code in CAS.items():
        p = subprocess.run([sys.executable, "-I", "-c", ENTETE + code, cache], capture_output=True, text=True,
                           env={"HF_HUB_OFFLINE": "1", "PATH": "/usr/bin:/bin"}, timeout=300)
        sortie = (p.stdout + p.stderr).strip().replace(cache, "<cache>")
        print(f"[{nom}] code {p.returncode}\n{sortie}\n")
