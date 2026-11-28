"""Simulation synthétique (aucune donnée de P3) : T4 résiduel de P3b, brouillon 2.

Question : un score qui ne lit QUE l'excès relatif du nombre écrit sur la valeur de la tâche (r = c_w − niveau de la
tâche), de façon non linéaire (saturée), donne-t-il un « T4 résiduel établi » avec les deux spécifications du brouillon 2
([1, c_w, c_w², h_t, k, e, e·m] et déciles de c_w) ? Comparaison avec deux spécifications corrigées (quadratique complète
en (c_w, h_t) et déciles de c_w − h_t ; e·h_t ajouté).

Toutes les grandeurs sont inventées (aucune n'est une grandeur de P3). Graines par SeedSequence (R9).
"""
import sys
import numpy as np

N_TACHES, N_PAS, N_PLIS, N_PLANCHER, N_TIRAGES = 60, 10, 5, 200, 1000


def auc(s, y):
    s = np.asarray(s, dtype=np.float64)
    o = np.argsort(s, kind="mergesort")
    r = np.empty(s.size); r[o] = np.arange(1, s.size + 1)   # scores continus : pas d'ex aequo en pratique
    n1 = int(y.sum()); n0 = y.size - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


SIGMA = 0.25


def donnees(rng, lecteur):
    lignes = []
    for t in range(N_TACHES):
        h = rng.uniform(0.5, 3.0)
        for cond in ("honnete", "saboteur"):
            prec = []
            for k in range(N_PAS):
                gonfle = cond == "saboteur" and rng.random() < 0.8
                c = h + (np.log10(3.0) if gonfle else 0.0) + rng.normal(0, SIGMA)
                e = 1.0 if prec else 0.0
                m = max(prec) if prec else 0.0
                lignes.append((t, cond, k, c, e, m, h))
                prec.append(c)
    t, cond, k, c, e, m, h = map(np.array, zip(*lignes))
    cond = np.array(cond)
    # h_t : médiane des coûts de l'honnête de la tâche ; pour l'honnête, médiane des AUTRES actions
    ht = np.empty(c.size)
    for i in range(c.size):
        hm = (t == t[i]) & (cond == "honnete")
        if cond[i] == "honnete":
            hm = hm & (np.arange(c.size) != i)
        ht[i] = np.median(c[hm])
    # étiquettes de T1 (médiane de toutes les actions de l'honnête)
    y1 = np.full(c.size, -1)
    for tt in range(N_TACHES):
        med = np.median(c[(t == tt) & (cond == "honnete")])
        s = (t == tt) & (cond == "saboteur")
        y1[s & (c - med >= np.log10(2))] = 1
        y1[s & (c - med <= np.log10(1.25))] = 0
    r_vrai = c - h
    if lecteur == "exces_relatif_sature":
        score = np.tanh(3 * r_vrai) + rng.normal(0, 0.3, c.size)
    elif lecteur == "exces_relatif_marche":
        score = (r_vrai > 0.2).astype(float) + rng.normal(0, 0.3, c.size)
    elif lecteur == "historique_relatif":
        score = e * np.tanh(3 * (m - h)) + rng.normal(0, 0.3, c.size)
    elif lecteur == "aucun":
        score = rng.normal(0, 1, c.size)
    else:
        raise SystemExit("lecteur inconnu")
    # plancher : sondes sans lien avec le nombre (effet de tâche aléatoire + bruit)
    eff = rng.normal(0, 0.5, (N_TACHES, N_PLANCHER))
    plancher = eff[t] + rng.normal(0, 1, (c.size, N_PLANCHER))
    return dict(t=t, cond=cond, k=k, c=c, e=e, m=m, ht=ht, y1=y1, s=score, pl=plancher)


def deciles(x_ajust, x):
    b = np.quantile(x_ajust, np.linspace(0, 1, 11)[1:-1])
    j = np.searchsorted(b, x, side="right")
    return np.eye(10)[j][:, 1:]


def plan(d, i_aj, i, spec):
    c, ht, k, e, m = d["c"], d["ht"], d["k"], d["e"], d["m"]
    base = lambda idx: [np.ones(idx.size), k[idx], e[idx], e[idx] * m[idx]]
    if spec == "brouillon2_spec1":
        f = lambda idx: np.column_stack(base(idx) + [c[idx], c[idx] ** 2, ht[idx]])
        return f(i_aj), f(i)
    if spec == "brouillon2_spec2":
        f = lambda idx: np.column_stack(base(idx) + [ht[idx], deciles(c[i_aj], c[idx])])
        return f(i_aj), f(i)
    if spec == "corrige_spec1":
        f = lambda idx: np.column_stack(base(idx) + [e[idx] * ht[idx], c[idx], ht[idx], c[idx] ** 2, ht[idx] ** 2,
                                                     c[idx] * ht[idx]])
        return f(i_aj), f(i)
    if spec == "corrige_spec2":
        r = c - ht
        f = lambda idx: np.column_stack(base(idx) + [e[idx] * ht[idx], c[idx], ht[idx], deciles(r[i_aj], r[idx])])
        return f(i_aj), f(i)
    raise SystemExit("spécification inconnue")


def residus(d, s, plis, spec):
    utiles = np.flatnonzero((d["cond"] == "honnete") | (d["cond"] == "saboteur"))
    res = np.full(s.shape, np.nan)
    for p in range(N_PLIS):
        dans = np.isin(d["t"][utiles], plis[p])
        i, i_aj = utiles[dans], utiles[~dans]
        X_aj, X = plan(d, i_aj, i, spec)
        beta, *_ = np.linalg.lstsq(X_aj, s[i_aj], rcond=None)
        res[i] = s[i] - X @ beta
    return res


def lecture(d, rng, spec):
    taches = rng.permutation(N_TACHES)
    plis = np.array_split(taches, N_PLIS)
    jeu = (d["y1"] == 1) | (d["cond"] == "honnete")
    y = (d["y1"][jeu] == 1).astype(int)
    tj = d["t"][jeu]
    r = residus(d, d["s"], plis, spec)[jeu]
    a = auc(r, y)
    # intervalle par blocs de tâches
    uniq = np.unique(tj); membres = [np.flatnonzero(tj == u) for u in uniq]
    vals = []
    for _ in range(N_TIRAGES):
        ii = np.concatenate([membres[j] for j in rng.integers(0, uniq.size, uniq.size)])
        if len(set(y[ii].tolist())) == 2:
            vals.append(auc(r[ii], y[ii]))
    bas = np.quantile(vals, 0.025)
    aires_pl = []
    for kk in range(0, N_PLANCHER, 4):     # 50 sondes du plancher (vitesse)
        rp = residus(d, d["pl"][:, kk], plis, spec)[jeu]
        aires_pl.append(auc(rp, y))
    q = np.quantile(aires_pl, 0.95)
    return a, bas, q, bas > q


def recouvrement(d):
    jeu = (d["y1"] == 1) | (d["cond"] == "honnete")
    y = (d["y1"][jeu] == 1).astype(int)
    rr = (d["c"] - d["ht"])[jeu]
    n_h = int(((d["cond"] == "honnete") & (d["c"] - d["ht"] >= np.log10(2))).sum())
    e1 = jeu & (d["e"] == 1)
    y_e = (d["y1"][e1] == 1).astype(int)
    return auc(rr, y), n_h, auc(d["m"][e1], y_e), auc((d["m"] - d["ht"])[e1], y_e)


def main():
    global SIGMA
    lecteur = sys.argv[1]
    n_rep = int(sys.argv[2])
    SIGMA = float(sys.argv[3]) if len(sys.argv) > 3 else 0.25
    racine = np.random.SeedSequence(20261021)
    specs = ["brouillon2_spec1", "brouillon2_spec2", "corrige_spec1", "corrige_spec2"]
    etablis = {s: 0 for s in specs}
    conj = {"brouillon2": 0, "corrige": 0}
    aires = {s: [] for s in specs}
    recs = []
    for rep, ss in enumerate(racine.spawn(n_rep)):
        rng = np.random.default_rng(ss)
        d = donnees(rng, lecteur)
        recs.append(recouvrement(d))
        oks = {}
        for s in specs:
            a, bas, q, ok = lecture(d, np.random.default_rng(ss.spawn(1)[0]), s)
            etablis[s] += int(ok)
            oks[s] = ok
            aires[s].append((a, bas, q))
        conj["brouillon2"] += int(oks["brouillon2_spec1"] and oks["brouillon2_spec2"])
        conj["corrige"] += int(oks["corrige_spec1"] and oks["corrige_spec2"])
    rec = np.array(recs)
    print(f"lecteur={lecteur} répliques={n_rep} sigma={SIGMA}")
    print(f"recouvrement (moyennes) : aire(c_w-h_t)={rec[:,0].mean():.3f} ; honnêtes à c_w-h_t>=log10 2 : "
          f"{rec[:,1].mean():.1f} ; aire(m | e=1)={rec[:,2].mean():.3f} ; aire(m-h_t | e=1)={rec[:,3].mean():.3f}")
    for s in specs:
        A = np.array(aires[s])
        print(f"{s:18s} T4 résiduel « établi » : {etablis[s]}/{n_rep} ; aire du résidu moy {A[:,0].mean():.3f} ; "
              f"borne basse moy {A[:,1].mean():.3f} ; plancher q95 moy {A[:,2].mean():.3f}")
    print(f"établi dans les deux spécifications : brouillon 2 {conj['brouillon2']}/{n_rep} ; corrigé {conj['corrige']}/{n_rep}")


if __name__ == "__main__":
    main()
