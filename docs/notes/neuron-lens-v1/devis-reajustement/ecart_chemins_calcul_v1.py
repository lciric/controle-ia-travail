"""Écart entre chemins de calcul des différences entre moitiés, sur les MÊMES sommes (pièces du 18 novembre) — v1.

Pour R et S : max |diffs − diffs_float64| et max |diffs_recopie − diffs_float64| sur toutes les cibles et couches ; plus petite et plus
grande valeur de diffs_float64 ; valeur la plus proche de 0,10. Lecture seule des deux fichiers d'ajustement. Usage : python FICHIER.
"""
import hashlib, json, math, sys
from pathlib import Path
D = Path("diag/20261118-164930-neuron-lens-b-beta")
for L in ("R", "S"):
    p = D / f"b-beta-ajustement-{L}.json"
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    r = json.loads(p.read_text(encoding="utf-8"))["resultat"]
    ref = r["diffs_float64"]
    vals = [(t, i, x) for t in sorted(ref) for i, x in enumerate(ref[t])]
    assert all(math.isfinite(x) for _, _, x in vals)
    out = {"lentille": L, "piece": str(p), "sha256": sha, "n": len(vals)}
    for champ in ("diffs", "diffs_recopie"):
        e = [(abs(r[champ][t][i] - x), t, i) for t, i, x in vals]
        m = max(e)
        out[f"max_abs_{champ}_contre_float64"] = {"ecart": m[0], "cible": m[1], "rang": m[2]}
        out[f"max_rel_{champ}_contre_float64"] = max(a / abs(ref[t][i]) for a, t, i in e)
    out["min_float64"] = min(x for _, _, x in vals)
    out["max_float64"] = max(x for _, _, x in vals)
    proche = min(vals, key=lambda v: abs(v[2] - 0.10))
    out["plus_proche_de_0_10"] = {"cible": proche[0], "rang": proche[1], "valeur": proche[2], "distance": abs(proche[2] - 0.10)}
    print(json.dumps(out, ensure_ascii=False))
