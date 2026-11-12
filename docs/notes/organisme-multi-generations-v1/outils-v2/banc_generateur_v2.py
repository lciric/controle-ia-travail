"""Banc du générateur v2 avec le vérificateur v2 complet (C8 à 200 graines) sur N mondes de développement (graines
publiques 2000…), et fréquences réalisées des sortes sur 4 000 gabarits tirés (E-5, E-6, S-9). Aucun coefficient écrit.
Usage : `python3 -I -B banc_generateur_v2.py SORTIE.json N`."""
import collections, json, os, sys
from concurrent.futures import ProcessPoolExecutor
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generateur_mondes_v2 as G
import verifier_monde_v2 as V


def un(g):
    spec, r, refus = G.generer_v2(2000 + g, V.verifier_v2)
    if spec is None:
        return {"graine": 2000 + g, "conforme": False, "refus": refus}
    return {"graine": 2000 + g, "conforme": True, "refus": refus, "gabarit": [(e["classe"], e["type"]) for e in spec["effets"]],
            "leurres": len(spec["distracteurs"]),
            "c8": {k: {"classe": v["classe"], "puissance": v["puissance"], "wilson": v["wilson"], "etiquette": v["etiquette"]}
                   for k, v in r["sensibilite"].items()}}


if __name__ == "__main__":
    out, n = sys.argv[1], int(sys.argv[2])
    freq = collections.Counter()
    lat = 0
    for s in range(4000):
        gab, l = G.tirer_gabarit_v2(np.random.default_rng(np.random.SeedSequence(990000 + s)))
        freq.update(f"{c}|{t}" for c, t in gab)
        lat += l
    with ProcessPoolExecutor(4) as ex:
        mondes = list(ex.map(un, range(n)))
    et = collections.Counter((v["classe"], v["etiquette"].split(" (")[0]) for m in mondes if m["conforme"] for v in m["c8"].values())
    resume = {"mondes": n, "conformes": sum(m["conforme"] for m in mondes),
              "tirages_refuses_par_controle": dict(collections.Counter(c for m in mondes for c in m["refus"])),
              "etiquettes_c8": {f"{c}|{e}": k for (c, e), k in sorted(et.items())},
              "frequences_sortes_sur_4000_gabarits": dict(sorted(freq.items())), "latents_sur_4000": lat}
    with open(out, "x", encoding="utf-8") as f:
        json.dump({"resume": resume, "mondes": mondes}, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(resume, ensure_ascii=False))
