"""Structure et nombres du jeu de 60 tâches du pilote, lus depuis la branche main (aucun contenu de cible affiché)."""
import hashlib, json, statistics, subprocess, sys
from collections import Counter

DEPOT = "/home/user/controle-ia-travail"
CHEMIN = "donnees/t05-pilote-v1/taches-pilote-60-v1.json"
brut = subprocess.run(["git", "-C", DEPOT, "show", f"main:{CHEMIN}"], check=True, capture_output=True).stdout
print("sha256", hashlib.sha256(brut).hexdigest(), "octets", len(brut))
d = json.loads(brut.decode("utf-8"))
print("type racine:", type(d).__name__)
if isinstance(d, dict):
    print("clés racine:", list(d.keys()))
    for k, v in d.items():
        if isinstance(v, (str, int, float, bool)) or v is None:
            print("  ", k, "=", repr(v)[:200])
        else:
            print("  ", k, ":", type(v).__name__, "longueur", len(v))
    taches = None
    for k, v in d.items():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            taches = v
            print("liste de tâches sous la clé:", k)
            break
else:
    taches = d
print("nombre de tâches:", len(taches))
print("clés d'une tâche:", sorted(Counter(k for t in taches for k in t).items()))
t0 = taches[0]
for k, v in t0.items():
    if isinstance(v, dict):
        print("  ", k, ": dict, clés", list(v.keys()))
    elif isinstance(v, list):
        print("  ", k, ": list, longueur", len(v))
    else:
        print("  ", k, ":", type(v).__name__, "longueur", len(str(v)))
