"""Compare deux dossiers d'épreuves en retirant seulement les champs de chemin (« fichier », « source.chemin »).
Usage : comparer_epreuves_v2.py DOSSIER_PUBLIE DOSSIER_REJOUE"""
import json, pathlib, sys

pub, rej = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])


def sans_chemins(o):
    if isinstance(o, dict):
        d = {k: sans_chemins(v) for k, v in o.items() if k != "fichier"}
        if isinstance(d.get("source"), dict):
            d["source"] = {k: v for k, v in d["source"].items() if k != "chemin"}
        return d
    if isinstance(o, list):
        return [sans_chemins(v) for v in o]
    return o


for p in sorted(pub.iterdir()):
    if p.suffix == ".sha256":
        continue
    a, b = json.loads(p.read_bytes()), json.loads((rej / p.name).read_bytes())
    sa, sb = sans_chemins(a), sans_chemins(b)
    print("IDENTIQUE HORS CHEMINS" if sa == sb else "DIVERGE", p.name)
    if p.name.startswith("sortie"):
        print("   source publiee :", a["source"], "| script_sha256 :", a["script_sha256"][:16], "| numpy", a["numpy"])
