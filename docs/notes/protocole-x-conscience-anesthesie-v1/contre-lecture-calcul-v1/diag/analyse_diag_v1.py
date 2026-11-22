"""Analyse des sorties JSON du diagnostic : liaison indice / nombre de uns, différences appariées par passage."""
import json, sys
import numpy as np

def rangs(x):
    x = np.asarray(x, dtype=float); o = np.argsort(x, kind="mergesort"); r = np.empty(len(x)); r[o] = np.arange(len(x))
    # rangs moyens pour les ex aequo
    for v in np.unique(x):
        m = x == v
        if m.sum() > 1: r[m] = r[m].mean()
    return r

def spearman(a, b):
    ra, rb = rangs(a), rangs(b)
    return float(np.corrcoef(ra, rb)[0, 1])

conds = {}
for chemin in sys.argv[1:]:
    conds.update(json.load(open(chemin))["conditions"])
print("conditions :", list(conds))
# (a) à travers les conditions : indice moyen contre nombre médian de uns, par seuil
for t in ("1.0", "0.5", "2.0"):
    m = [np.mean([r[f"lz{t}"] for r in c["reponses"]]) for c in conds.values()]
    u = [np.median([r[f"uns{t}"] for r in c["reponses"]]) for c in conds.values()]
    print(f"seuil {t} : rho de Spearman (indice moyen, uns median) sur {len(m)} conditions = {spearman(m, u):.3f}")
# toutes conditions et seuils confondus, réponses non vides
lz, un = [], []
for c in conds.values():
    for r in c["reponses"]:
        for t in ("1.0", "0.5", "2.0"):
            if r[f"uns{t}"] > 0:
                lz.append(r[f"lz{t}"]); un.append(r[f"uns{t}"])
print(f"reponses non vides, tous seuils : n = {len(lz)}, rho(indice, uns) = {spearman(lz, un):.3f}")
lz, un = np.array(lz), np.array(un)
for lo, hi in ((1, 1), (2, 2), (3, 5), (6, 10), (11, 20), (21, 50), (51, 100), (101, 10000)):
    m = (un >= lo) & (un <= hi)
    if m.sum():
        print(f"   uns dans [{lo},{hi}] : n = {m.sum():4d}, indice moyen {lz[m].mean():.3f}, min {lz[m].min():.3f}, max {lz[m].max():.3f}")

# (b) différences appariées par passage (8 passages, moyenne sur les 8 directions communes)
def par_passage(nom, cle="lz1.0"):
    v = np.array([r[cle] for r in conds[nom]["reponses"]]).reshape(8, 8)
    return v.mean(axis=1)
paires = [("E|naturel", "R1|naturel"), ("E|naturel", "M1|naturel"), ("eta=0.2|graine1", "alpha=0.2"), ("eta=0.2|graine2", "alpha=0.2"),
          ("eta=0.05|graine1", "alpha=0.55"), ("eta=0.1|graine1", "alpha=0.4"), ("E|naturel", "E|repetitif")]
for a, b in paires:
    if a in conds and b in conds:
        for cle in ("lz1.0", "lz2.0", "lz_hors_site1.0", "lz_melange1.0"):
            try:
                da, db = par_passage(a, cle), par_passage(b, cle)
            except TypeError:
                va = np.array([np.nan if r[cle] is None else r[cle] for r in conds[a]["reponses"]]).reshape(8, 8)
                vb = np.array([np.nan if r[cle] is None else r[cle] for r in conds[b]["reponses"]]).reshape(8, 8)
                da, db = np.nanmean(va, axis=1), np.nanmean(vb, axis=1)
            d = da - db
            print(f"{a} - {b} [{cle}] : moyenne {d.mean():+.3f}, e.-t. entre passages {d.std(ddof=1):.3f}, passages a > b : {(d > 0).sum()}/8")
# (c) dispersion entre passages de l'indice principal (moyenne des 8 directions par passage)
for nom in conds:
    v = par_passage(nom)
    print(f"{nom:24s} indice th1 par passage : {np.round(v, 2).tolist()}  (e.-t. entre passages {v.std(ddof=1):.3f})")
# (d) bruit à amplitude figée contre bruit du script
for e in ("0.2", "0.05"):
    a, b = f"eta={e}|graine1", f"eta={e}|graine1|fige"
    if a in conds and b in conds:
        ra, rb = conds[a]["reponses"], conds[b]["reponses"]
        for cle in ("lz1.0", "uns1.0", "uns_site1.0", "lz2.0", "uns0.5"):
            x = np.array([r[cle] for r in ra], float); y = np.array([r[cle] for r in rb], float)
            print(f"bruit eta={e} : {cle} script {x.mean():.3f} (med {np.median(x):.1f}) ; amplitude figee {y.mean():.3f} (med {np.median(y):.1f}) ; reponses identiques {np.mean(x == y):.2f}")
