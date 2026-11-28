"""Témoin T1 : coûts illisibles de `honnete` et `consigne_neutre`, selon plusieurs définitions, contre 257 et 268 (70baf0e6…)."""
import collections, math, subprocess, sys
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.t06.cout import cout_lisible, cout_action
from sondage_validateur_v2 import DEPOT, REF, RACINE, lire
blocs = subprocess.run(["git", "-C", DEPOT, "ls-tree", "--name-only", REF, RACINE + "/"], capture_output=True, check=True, text=True).stdout.split()
c1 = collections.Counter(); c2 = collections.Counter(); c3 = collections.Counter(); c4 = collections.Counter()
for bloc in blocs:
    textes = {d["cle"]: d["texte"] for d in lire(f"{bloc}/textes.jsonl")}
    for d in lire(f"{bloc}/mesures.jsonl"):
        c = d["condition"]
        if c not in ("honnete", "consigne_neutre", "gonfle_3", "gonfle_5"):
            continue
        v = d.get("cout")
        c1[c] += (v is None)
        c2[c] += not (v is not None and math.isfinite(v) and v > 0)
        c3[c] += not (d.get("valide") and v is not None and math.isfinite(v) and v > 0)
        try:
            c4[c] += not cout_lisible(v)
        except Exception as e:
            c4[c] += 0
print("cout None", dict(c1)); print("non fini ou <= 0", dict(c2)); print("invalide ou non lisible", dict(c3)); print("not cout_lisible(cout)", dict(c4))
