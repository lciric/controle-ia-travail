"""Essai : le nom du fichier entre-t-il dans les octets écrits par torch.save ? (contre-lecture du critère v1, mineure 1)."""
import hashlib, os, tempfile
import torch
d = {"a": torch.arange(10.0)}
with tempfile.TemporaryDirectory() as r:
    h = {}
    for n in ("r-llama-3.1-8b-instruct-L32-dclm-T128.pt", "autre-nom.pt"):
        p = os.path.join(r, n); torch.save(d, p); h[n] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    # même nom, deux dossiers
    q = []
    for s in ("x", "y"):
        os.makedirs(os.path.join(r, s)); p = os.path.join(r, s, "r-llama-3.1-8b-instruct-L32-dclm-T128.pt"); torch.save(d, p)
        q.append(hashlib.sha256(open(p, "rb").read()).hexdigest())
print(f"torch {torch.__version__}")
print("deux noms :", "egaux" if len(set(h.values())) == 1 else "DIFFERENTS", h)
print("meme nom, deux dossiers :", "egaux" if q[0] == q[1] else "DIFFERENTS", q)
