import json, os, sys
from huggingface_hub import HfApi
api = HfApi(token=os.environ["HF_TOKEN"])
rev = "e61aaabac7abd50cf68e5b608af2704f7faaa1e6"; depot = "Sirmium/lentilles-rangement"
inv = json.load(open("diag/20261122-073402-neuron-lens-b-beta/inventaire/inventaire-029.json"))
out = {"revision": rev, "fichiers": {}}
try:
    items = list(api.list_repo_tree(depot, revision=rev, recursive=True, repo_type="model"))
except Exception as e:
    print("ACCES:", type(e).__name__, str(e)[:200]); sys.exit(3)
for f in items:
    if hasattr(f, "size"):
        lfs = getattr(f, "lfs", None)
        out["fichiers"][f.path] = {"taille": f.size, "sha256_lfs": getattr(lfs, "sha256", None) if lfs else None, "blob": f.blob_id}
json.dump(out, open(sys.argv[1], "w"), indent=1, sort_keys=True)
print("fichiers distants:", len(out["fichiers"]))
print("cles inventaire:", list(inv.keys()))
