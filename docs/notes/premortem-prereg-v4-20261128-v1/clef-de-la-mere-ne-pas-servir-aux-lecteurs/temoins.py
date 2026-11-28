"""Témoins à réponse connue : recalcul depuis mesures.jsonl (42cdfcf29) de chiffres scellés dans 70baf0e6…"""
import collections, subprocess, sys
from sondage_validateur_v2 import DEPOT, REF, RACINE, lire
blocs = subprocess.run(["git", "-C", DEPOT, "ls-tree", "--name-only", REF, RACINE + "/"], capture_output=True, check=True, text=True).stdout.split()
n = collections.Counter(); sans = collections.Counter(); mention = collections.Counter(); tronq = collections.Counter(); jn = collections.defaultdict(list)
for bloc in blocs:
    for d in lire(f"{bloc}/mesures.jsonl"):
        c = d["condition"]; n[c] += 1
        sans[c] += (d.get("cout") is None); mention[c] += bool(d.get("mention_texte_prive")); tronq[c] += bool(d.get("tronquee"))
        jn[c].append(d["jetons_notes"])
print("total", sum(n.values()), "conditions", len(n))
for c in ("honnete", "consigne_neutre", "gonfle_3", "gonfle_5", "gonfle_10"):
    v = sorted(jn[c])
    print(c, n[c], "cout None", sans[c], round(sans[c] / n[c], 4), "mention_texte_prive", mention[c] / n[c], "tronquees", tronq[c], "jetons_notes mediane", v[len(v) // 2], "max", v[-1])
