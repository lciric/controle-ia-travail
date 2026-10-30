"""Plomberie des corrections v2 : empreinte de chaque monde d'essai (latents et vue observée), 14 conditions, indices
980000 à 980059 (RACINE_VALIDATION, hors plages du § 7), pour comparer le code d'avant (version-v1-avant-corrections)
et le code corrigé : un monde sans échec de plantation doit être identique bit à bit. Ne lit que des égalités et comptes.
Usage (depuis ce dossier) : PYTHONPATH=<dépôt>/src python3 -B identite_ancien_nouveau_v1.py ../version-v1-avant-corrections A.json
puis ... identite_ancien_nouveau_v1.py .. N.json"""
import hashlib, json, sys
from pathlib import Path
D = str(Path(sys.argv[1]).resolve())
sys.path.insert(0, D)
sys.path.append(str(Path(__file__).resolve().parents[3] / "trancher-recombinaison"))
import monde_v2 as mo, graines_v2 as gr
out = {}
for cond in mo.CONDITIONS_V2:
    for i in range(980000, 980060):
        w = mo.generer(cond, gr.RACINE_VALIDATION, i)
        L = w.latent(mo.JETON_MESURE)
        o = w.obs
        h = hashlib.sha256()
        h.update(mo.empreinte_latents(w).encode()); h.update(o.cos.tobytes())
        h.update(json.dumps([sorted(x) for x in o.etiq_op] + [sorted(x) for x in o.etiq_co] + [list(o.c_obs), list(o.dom_obs), list(o.valides), list(o.pont), list(o.q)], default=str).encode())
        out[f"{cond}|{i}"] = [h.hexdigest(), L.tentatives, getattr(L, "replantations", None)]
json.dump(out, open(sys.argv[2], "w"))
