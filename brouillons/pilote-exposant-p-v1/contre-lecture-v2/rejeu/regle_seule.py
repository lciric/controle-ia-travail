"""Taux de faux « au-dessus » / « au-dessous » de la règle seule (sans banque), lecteur du run appelé tel quel.
p(E,R) par sous-ensemble ~ mu + biais + c_s + N(0, sig) ; plans de référence k ~ mu + tau z_k + c_{k mod 32} + N(0, sig).
Graines : SeedSequence(2026110499), un enfant par scénario."""
import json, sys
import numpy as np
from controle_ia.pilote_exposant_p_v2.analyse import bootstrap_sous_ensembles, issue_principale
S, M = 32, 60
def scen(rng, sig, tau, sc, biais, R, B):
    n = {"au-dessus": 0, "au-dessous": 0, "égal": 0, "non concluant": 0}; ds = []; hw = []
    for _ in range(R):
        c = rng.normal(0, sc, S)
        p = {s: 2.0 + biais + c[s] + rng.normal(0, sig) for s in range(S)}
        z = rng.standard_normal(M)
        ref = [(k % S, 2.0 + tau * z[k] + c[k % S] + rng.normal(0, sig)) for k in range(M)]
        d = bootstrap_sous_ensembles(p, ref, B, rng)
        n[issue_principale(*d["ic"])] += 1; ds.append(d["delta"]); hw.append((d["ic"][1] - d["ic"][0]) / 2)
    return {k: v / R for k, v in n.items()} | {"delta_moyen": float(np.mean(ds)), "et_delta": float(np.std(ds)),
                                               "demi_largeur_mediane": float(np.median(hw))}
ss = np.random.SeedSequence(2026110499)
scs = [(0.12, 0.17, 0.035, 0.0), (0.12, 0.17, 0.035, 0.014), (0.12, 0.17, 0.06, 0.0), (0.12, 0.10, 0.035, 0.0),
       (0.12, 0.25, 0.035, 0.0), (0.22, 0.17, 0.035, 0.0)]
out = []
for (sig, tau, sc, b), e in zip(scs, ss.spawn(len(scs))):
    r = scen(np.random.default_rng(e), sig, tau, sc, b, int(sys.argv[1]), 2000)
    out.append({"sigma_plan": sig, "tau": tau, "sigma_c": sc, "biais": b, **r}); print(out[-1], flush=True)
json.dump({"entropie": 2026110499, "R": int(sys.argv[1]), "B": 2000, "scenarios": out}, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
