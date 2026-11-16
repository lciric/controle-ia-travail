import sys, time, json
import numpy as np, torch
from controle_ia.sondes import familles as fam
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
torch.use_deterministic_algorithms(True); torch.set_num_threads(4)

def jeu(kind, seed, n=480, nc=192, d=768, lo=30, hi=90, copies=0.0, bruit=1e-3, signal=0.3):
    rng = np.random.default_rng(np.random.SeedSequence(seed))
    gab = rng.standard_normal((6, d))
    mu = rng.standard_normal(d) * (3.0 if kind != "iid" else 0.0)
    L = rng.standard_normal((d, 8)) if kind == "aniso" else None
    dirsig = rng.standard_normal(d); dirsig /= np.linalg.norm(dirsig)
    def action(y):
        m = int(rng.integers(lo, hi + 1))
        x = rng.standard_normal((m, d))
        if kind == "aniso":
            x = 0.3 * x + (rng.standard_normal((m, 8)) * 3.0) @ L.T / np.sqrt(8)
        x = x + mu
        k = int(round(copies * m))
        if k:
            sel = rng.choice(m, k, replace=False)
            x[sel] = gab[rng.integers(0, 6, k)] * 2 + mu + bruit * rng.standard_normal((k, d))
        if y:
            j = int(rng.integers(0, m)); x[j] = x[j] + signal * 10 * dirsig
        return x.astype(np.float16).astype(np.float64)
    ya = np.array([i % 2 for i in range(n)]); yc = np.array([i % 2 for i in range(nc)])
    return [action(y) for y in ya], ya, [action(y) for y in yc], yc

def run(nom, **kw):
    app, y, ctr, yc = jeu(**kw)
    perm = np.random.default_rng(5).permutation(len(app))
    out = {"jeu": nom}
    for ep in (3, 300):
        t = time.time()
        r = fam.Reglages(l2=1e-3, epoques=ep, pas=0.05)
        a = fam.entrainer("lineaire", "a", 15, app, y, "max", 0, r)
        r2 = fam.Reglages(l2=1e-3, epoques=ep, pas=0.05)
        b = fam.entrainer("lineaire", "b", 15, [app[i] for i in perm], y[perm], "max", 0, r2)
        sa, sb = ac.scores(a, ctr), ac.scores(b, ctr)
        out[f"ecart_{ep}"] = ac.ecart_relatif(sa, sb)
        if ep == 300:
            from scipy.stats import rankdata
            def roc_auc_score(y,s):
                r=rankdata(s); n1=y.sum(); n0=len(y)-n1
                return (r[y==1].sum()-n1*(n1+1)/2)/(n1*n0)
            out["auc_a"] = float(roc_auc_score(yc, sa)); out["auc_b"] = float(roc_auc_score(yc, sb))
            out["perte_finale"] = r.journal[-1]["perte"]
        out[f"s_{ep}"] = round(time.time() - t, 1)
    print(json.dumps(out), flush=True)


for sd in (11,12,13,14):
    run(f"aniso_sans_copies_seed{sd}", kind="aniso", seed=sd)
for sd in (21,22):
    run(f"aniso_sans_copies_sans_signal_seed{sd}", kind="aniso", seed=sd, signal=0.0)
for sd in (31,32):
    run(f"res_sans_copies_seed{sd}", kind="res", seed=sd)
