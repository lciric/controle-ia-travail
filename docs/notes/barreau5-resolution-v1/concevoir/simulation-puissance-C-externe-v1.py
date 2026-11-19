"""Conception C (validation hors de nous) -- simulations a loi inventee, aucune donnee du programme.
Trois blocs : (P1) contrastes par action groupes par tache ; (P3) l'adaptateur comme unite ;
(P4) epreuve a verite connue : la regle de lecture retrouve-t-elle le monde plante ?
Graines par numpy.random.SeedSequence (R9)."""
import json, itertools, math
import numpy as np
from math import erf, sqrt
RACINE = np.random.SeedSequence(20261119)
def gen(*cle): return np.random.default_rng(np.random.SeedSequence(entropy=RACINE.entropy, spawn_key=tuple(cle)))
Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
def aire(pos, neg):
    r = np.argsort(np.argsort(np.concatenate([pos, neg]))) + 1.0
    return (r[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))
sortie = {}

# ---------- P1 : aire entre deux groupes de 64 taches x 10 actions, effet de tache (correlation rho)
def p1(delta, rho, n_t=64, n_a=10, apparie=True, rep=400, B=300, cle=0):
    g = gen(1, cle); gagne = 0
    for _ in range(rep):
        t1 = g.normal(size=n_t) * sqrt(rho)
        t0 = t1 if apparie else g.normal(size=n_t) * sqrt(rho)
        a = t1[:, None] + g.normal(size=(n_t, n_a)) * sqrt(1 - rho) + delta
        b = t0[:, None] + g.normal(size=(n_t, n_a)) * sqrt(1 - rho)
        idx = g.integers(0, n_t, size=(B, n_t))
        bs = np.array([aire(a[i].ravel(), b[i].ravel()) for i in idx])
        gagne += np.quantile(bs, 0.005) > 0.5          # borne basse a 99 % au-dessus de 0,5
    return gagne / rep
res = {}
for rho in (0.0, 0.3, 0.6):
    for app in (True, False):
        ligne = {}
        for au in (0.53, 0.55, 0.57, 0.60, 0.65):
            delta = sqrt(2) * float(np.sqrt(2) * 0 + __import__("statistics").NormalDist().inv_cdf(au))
            ligne[str(au)] = p1(delta, rho, apparie=app, cle=int(rho * 10) * 100 + int(app) * 10 + int(au * 100))
        res[f"rho={rho},taches_{'appariees' if app else 'independantes'}"] = ligne
sortie["P1_puissance_aire_640_contre_640_niveau_99"] = res

# ---------- P3 : l'adaptateur comme unite ; K saboteurs contre K temoins honnetes, permutation exacte unilaterale
def p3(K, d, rep=20000, cle=0):
    g = gen(3, cle, K); s = g.normal(size=(rep, K)) + d; h = g.normal(size=(rep, K))
    tous = np.concatenate([s, h], axis=1); combs = list(itertools.combinations(range(2 * K), K))
    obs = s.mean(1) - h.mean(1); nb = np.zeros(rep)
    for c in combs:
        m = np.zeros(2 * K, bool); m[list(c)] = True
        nb += (tous[:, m].mean(1) - tous[:, ~m].mean(1)) >= obs - 1e-12
    p = nb / len(combs)
    return {"p_minimale": 1 / len(combs), "puissance_p<=0,05": float((p <= 0.05).mean()), "puissance_p<=0,01": float((p <= 0.01).mean())}
sortie["P3_adaptateur_unite"] = {f"K={K},ecart={d}_ecarts-types_entre_graines": p3(K, d, cle=int(d * 10)) for K in (2, 3, 4, 5, 6) for d in (1.5, 2.5, 4.0)}

# ---------- P4 : epreuve a verite connue, au niveau des activations (dimension 256)
D, NT, NA = 256, 64, 10
def monde(nom, g, K=4, intensite_temoin=1.0, part_acte=0.8):
    u = np.linalg.qr(g.normal(size=(D, 3 + 2 * K + 2)))[0].T     # directions orthonormales plantees
    u_commun, u_acte, u_disp = u[0], u[1], u[2]; idios = u[3:3 + 2 * K + 2]
    tache = g.normal(size=(NT, D)) * 0.5
    def groupe(k=None, sab=False, alpha=0.0):
        x = tache[:, None, :] + g.normal(size=(NT, NA, D))
        acte = np.zeros((NT, NA), bool)
        if k is not None: x = x + alpha * 2.0 * (u_commun + idios[k]) / sqrt(2)      # trace de l'adaptateur k
        if sab:
            acte = g.random((NT, NA)) < part_acte
            if nom == "acte": x = x + acte[..., None] * 1.5 * u_acte
            if nom == "disposition": x = x + 1.5 * u_disp
        return x.reshape(-1, D), acte.ravel()
    H = groupe()[0]
    S = [groupe(k, True, 1.0) for k in range(K + 1)]                # S[0] sert a apprendre la sonde
    N = [groupe(K + 1 + k, False, intensite_temoin)[0] for k in range(K)]
    return H, S, N
def lire(H, S, N, g, K=4, inclure_adaptateur_appris=False):
    w = S[0][0][:320].mean(0) - H[:320].mean(0)                     # sonde apprise sur le label confondu, moitie des actions
    plancher = lambda pos, neg: np.quantile([aire(pos @ r, neg @ r) for r in g.normal(size=(200, D))], 0.95)
    xs, acte = S[1]
    a_acte = aire(xs[acte] @ w, xs[~acte] @ w); lit_acte = a_acte > plancher(xs[acte], xs[~acte]) + 0.03
    sab = [(S[0][0][320:] @ w).mean()] + [(S[k][0] @ w).mean() for k in range(1, K)] if inclure_adaptateur_appris else [(S[k][0] @ w).mean() for k in range(1, K + 1)]
    hon = [(n @ w).mean() for n in N]
    tous = np.array(sab + hon); obs = np.mean(sab) - np.mean(hon); cb = list(itertools.combinations(range(2 * K), K))
    p = np.mean([tous[list(c)].mean() - np.delete(tous, list(c)).mean() >= obs - 1e-12 for c in cb])
    au_dela = p <= 0.05
    a_adapt = aire(N[0] @ w, H[320:] @ w); lit_adapt = a_adapt > plancher(N[0], H[320:]) + 0.03
    if lit_acte: return "lit l'acte"
    if au_dela: return "au-dela de l'adaptateur (disposition)"
    if lit_adapt: return "lit l'adaptateur"
    return "ne lit rien"
tab = {}
cas = [("adaptateur_seul", 1.0, False), ("acte", 1.0, False), ("disposition", 1.0, False),
       ("adaptateur_seul", 0.6, False), ("adaptateur_seul", 0.9, False), ("adaptateur_seul", 1.0, True)]
for i, (nom, it, incl) in enumerate(cas):
    g = gen(4, i); cpt = {}
    for _ in range(200):
        v = lire(*monde(nom, g, intensite_temoin=it), g, inclure_adaptateur_appris=incl); cpt[v] = cpt.get(v, 0) + 1
    tab[f"monde={nom},intensite_du_temoin={it},adaptateur_appris_dans_la_comparaison={incl}"] = {k: v / 200 for k, v in cpt.items()}
sortie["P4_verite_connue_K=4_adaptateurs_par_bras"] = tab
print(json.dumps(sortie, indent=1, ensure_ascii=False))
