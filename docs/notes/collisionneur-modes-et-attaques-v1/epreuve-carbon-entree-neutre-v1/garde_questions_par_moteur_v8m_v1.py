import importlib.util, sys, hashlib
from pathlib import Path
moteur = Path("docs/notes/collisionneur-v9/collisionneur_v9_v8m.py")
assert hashlib.sha256(moteur.read_bytes()).hexdigest() == "420394f9d803bc4eb41f0e469a30e0be647e11a2c91ac9f42e70c90fdb31c377"
spec = importlib.util.spec_from_file_location("moteur_v8m", moteur)
v = importlib.util.module_from_spec(spec); sys.modules["moteur_v8m"] = v; spec.loader.exec_module(v)
for q in sys.argv[1:]:
    t = v.lire_entree(q)
    print(Path(q).name, hashlib.sha256(Path(q).read_bytes()).hexdigest()[:12], len(t), "caractères")
    try:
        v.garder_motifs(None, Path(q).name, t)
        print("  garde : aucun motif")
    except v.Arret as e:
        print("  garde : REFUS", e.args if hasattr(e, "args") else e)
