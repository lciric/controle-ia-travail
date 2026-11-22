"""Essai : torch.save du même dictionnaire, au même nom de fichier, écrit-il les mêmes octets ? (devis de réajustement v2, § 1)."""
import hashlib, os, sys, tempfile, time
import torch
g = torch.Generator().manual_seed(0)
d = {"meta": {"lens": "R", "rows_sha256": "x", "shard": [0, 1]},
     "state": {"sums": {"a": torch.randn(64, 64, generator=g, dtype=torch.float64)}, "n_docs": 3}, "next_doc": 3}
h = []
with tempfile.TemporaryDirectory() as racine:
    for i in range(2):
        p = os.path.join(racine, f"essai-{i}", "r-llama.tmp"); os.makedirs(os.path.dirname(p))
        torch.save(d, p); os.replace(p, p[:-4] + ".pt")
        h.append(hashlib.sha256(open(p[:-4] + ".pt", "rb").read()).hexdigest()); time.sleep(1.5)
print(f"torch {torch.__version__} ; {h[0]} ; {h[1]} ; {'egaux' if h[0] == h[1] else 'DIFFERENTS'}")
sys.exit(0 if h[0] == h[1] else 1)
