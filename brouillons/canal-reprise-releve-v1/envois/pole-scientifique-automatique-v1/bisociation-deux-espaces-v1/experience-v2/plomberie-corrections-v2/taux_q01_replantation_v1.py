"""Plomberie Q-01 (b) : taux de replantation et de régénération entière, 2 400 mondes d'essai par condition,
RACINE_VALIDATION, indices 970000 à 972399 (hors plages du § 7). Ne lit que des comptes.
Usage (depuis ce dossier) : PYTHONPATH=<dépôt>/src python3 -B taux_q01_replantation_v1.py .. SORTIE.json"""
import json, sys, multiprocessing as mp
from collections import Counter
from pathlib import Path
D = str(Path(sys.argv[1]).resolve())   # dossier experience-v2
sys.path.insert(0, D)
import monde_v2 as mo, graines_v2 as gr
I0, N = 970000, 2400

def f(t):
    cond, i = t
    L = mo.generer(cond, gr.RACINE_VALIDATION, i).latent(mo.JETON_MESURE)
    return cond, L.tentatives, L.replantations, L.n_champs

if __name__ == "__main__":
    conds = list(mo.CONDITIONS_V2)
    taches = [(c, i) for c in conds for i in range(I0, I0 + N)]
    out = {c: {"n": 0, "regeneres": 0, "replantes": 0, "replantations": 0, "par_champs": {}} for c in conds}
    with mp.get_context("fork").Pool(2) as p:
        for cond, t, r, f_ in p.imap(f, taches, chunksize=32):
            o = out[cond]; o["n"] += 1; o["regeneres"] += t > 0; o["replantes"] += r > 0; o["replantations"] += r
            pc = o["par_champs"].setdefault(str(f_), {"n": 0, "replantes": 0, "regeneres": 0})
            pc["n"] += 1; pc["replantes"] += r > 0; pc["regeneres"] += t > 0
    for c, o in out.items():
        o["taux_regeneration"] = o["regeneres"] / o["n"]; o["taux_replantation"] = o["replantes"] / o["n"]
    json.dump(out, open(sys.argv[2], "w"), indent=1, sort_keys=True)
    tot = sum(o["regeneres"] for o in out.values()); n = sum(o["n"] for o in out.values())
    print("regeneres", tot, "sur", n)
    for c, o in out.items():
        print(f"{c:24s} regen {o['regeneres']:3d}/{o['n']} ({o['taux_regeneration']:.4f}) replant {o['replantes']:3d} ({o['taux_replantation']:.4f}) total_replantations {o['replantations']}")
