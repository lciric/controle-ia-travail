"""Contre-lecture de la batterie de fuite (v2) — recalcul indépendant des écarts 1 et 2 — v1.

Écrit par le contre-lecteur (Opus 5.5, session neuve), sans importer le code du concepteur ni le paquet de la
version 6 : le banc d'épreuve est reconstruit d'après sa description (§ 4 de la batterie), les strates sont
contrôlées par force brute sur [0 .. 3N], la sonde des nombres est recodée d'après la lettre du § 2.2.
Processeur seul ; aucun appel de modèle ; racines d'épreuve 1000 à 1119 seulement (graines du banc :
SeedSequence(racine, spawn_key=(70 + i,)), distinctes de celles du concepteur ; bornes hautes :
SeedSequence(20261122, spawn_key=(2000 + j,)) comme le texte).

Emploi : python3 -I recalcul_ecarts_1_2_v1.py SORTIE.json > SORTIE.txt
"""
import json, math, re, sys
from fractions import Fraction
import numpy as np

RACINES = list(range(1000, 1120))
BORNES = [4] * 4 + [10] * 4 + [15] * 4
ECRITURES = [("g1", "pour tout n dans NAT, mod({A} * n + {C}, PM) != {R}", +1),
             ("g2", "pour tout n dans NAT, mod({C} + {A} * n, PM) != {R}", -1),
             ("g3", "pour tout n dans NAT, {R} != mod({A} * n + {C}, PM)", +1),
             ("g4", "pour tout n dans NAT, mod({C} + n * {A}, PM) != {R}", -1)]
V, FT, PG = "V", "FT", "PG"

def premiers(lo, hi):
    return [p for p in range(lo, hi + 1) if p > 1 and all(p % d for d in range(2, int(p ** .5) + 1))]
PREM = premiers(211, 1999)

def strate_par_force_brute(A, C, R, PM, N):
    ce = [n for n in range(0, 3 * N + 1) if (A * n + C) % PM == R]
    if not ce: return V
    return FT if ce[0] <= N else PG

def tirer(g, strate, N, PM, variante, dose, sens):
    if strate == FT: lo, hi = (1, 1) if variante == "plafond" else (2, N)
    elif strate == PG: lo, hi = (3 * N, 3 * N) if variante == "plafond" else (N + 1, 3 * N)
    else: lo, hi = 3 * N + 1, PM - 1
    n0 = int(g.integers(lo, hi + 1)); A = int(g.integers(1, PM))
    if variante == "grandeur" and g.random() < dose:
        m = (PM + 1) // 2
        haut = (strate == V) == (sens > 0)
        R = int(g.integers(m, PM)) if haut else int(g.integers(0, m)); C = (R - A * n0) % PM
    elif variante == "relation" and strate == V and g.random() < dose:
        d = int(g.integers(1, 6)); A = (-d * pow(n0, -1, PM)) % PM
        C = int(g.integers(0, PM)); R = (A * n0 + C) % PM   # R = C - d : R et C voisins
    else:
        C = int(g.integers(0, PM)); R = (A * n0 + C) % PM
    return A, C, R

def construire(r, variante, dose=1.0):
    gm, gp, gs = [np.random.default_rng(np.random.SeedSequence(r, spawn_key=(70 + i,))) for i in range(3)]
    mondes = [(N, PREM[int(gm.integers(0, len(PREM)))]) for N in BORNES]
    viv = []
    for w, (N, PM) in enumerate(mondes):
        for gi, (nom, forme, sens) in enumerate(ECRITURES):
            if variante == "gabarit_partiel" and gi == 0: plan = [V, FT, FT, PG]
            else: plan = [V, FT, V, PG]
            vus = set()
            for k, st in enumerate(plan):
                while True:
                    A, C, R = tirer(gp, st, N, PM, variante, dose, sens)
                    t = forme.format(A=A, C=C, R=R)
                    if t not in vus: vus.add(t); break
                assert strate_par_force_brute(A, C, R, PM, N) == st, (r, w, st)
                viv.append(dict(cle=(w, gi, k), w=w, texte=t, et=st, y=st != V, paire=(w, gi, k // 2), N=N, PM=PM,
                                mid=(N, PM), sq=nom))
    sb = []
    if variante == "gabarit_partiel":  # pas de paires : tirage par strate et par monde
        for et, q in ((V, 75), (FT, 38), (PG, 37)):
            base, reste = divmod(q, 12); plus = set(int(i) for i in gs.choice(12, reste, replace=False))
            for w in range(12):
                pool = [x for x in viv if x["w"] == w and x["et"] == et]
                k = min(len(pool), base + (w in plus))
                sb += [pool[int(i)] for i in gs.choice(len(pool), k, replace=False)]
        return viv, sb
    for et, q in ((FT, 38), (PG, 37)):
        base, reste = divmod(q, 12); plus = set(int(i) for i in gs.choice(12, reste, replace=False))
        for w in range(12):
            ps = sorted({x["paire"] for x in viv if x["w"] == w and x["et"] == et})
            for i in gs.choice(len(ps), base + (w in plus), replace=False):
                sb += [x for x in viv if x["paire"] == ps[int(i)]]
    return viv, sb

# ---------------------------------------------------------------- sonde des nombres, d'après la lettre du § 2.2
def litt(t): return [int(x) for x in re.findall(r"\d+", t)]
def l10(x): return math.log10(x)
def traits_spec(t, N, PM):
    L = litt(t); D = sorted({N, PM}); d = D[-1]; x = []
    for a in L:
        v = a; b = 1
        x += [l10(1 + v), l10(1 + a), l10(b), l10(1 + 1 / v) if v else 0., l10(1 + 1 / abs(v - 1)) if v != 1 else 0.,
              float(v == 0), float(v == 1), float(v == 2), float(v <= N), float(N < v <= 3 * N),
              sum(1 for s in D if s < v) / len(D), float(v in D), l10((1 + v) / (1 + d)),
              l10(1 + v) ** 2, l10(1 + a) ** 2, l10(b) ** 2, 0.]
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            hi, lo = max(L[i], L[j]), min(L[i], L[j]); x += [lo / hi if hi else 1., float(L[i] == L[j])]
    x.append(float(sum(c.isdigit() for c in t)))
    return x
def traits_resume(t, N, PM):  # sonde commune « à la diagnostic » : traits sans ordre d'écriture
    L = litt(t); g = [l10(1 + v) for v in L]
    return [len(L), max(g), min(g), float(np.mean(g)), sum(len(str(v)) for v in L), sum(v > 3 * N for v in L),
            sum(v <= N for v in L), sum(v == PM for v in L), max(L) / PM, sum(v in (0, 1, 2) for v in L)]

def logistique(X, y, lam=1.0):
    mu = X.mean(0); sd = X.std(0); nul = sd == 0; sd[nul] = 1
    Z = (X - mu) / sd; Z[:, nul] = 0; Z = np.hstack([np.ones((len(Z), 1)), Z]); w = np.zeros(Z.shape[1])
    for _ in range(50):
        p = 1 / (1 + np.exp(-(Z @ w))); gr = Z.T @ (p - y) + lam * w
        H = (Z * (p * (1 - p))[:, None]).T @ Z + lam * np.eye(len(w)); pas = np.linalg.solve(H, gr); w -= pas
        if np.abs(pas).max() < 1e-10: break
    def score(Xt):
        Zt = (Xt - mu) / sd; Zt[:, nul] = 0
        return np.round(np.hstack([np.ones((len(Zt), 1)), Zt]) @ w, 10)
    return score

def sonde_par_squelette_autres_racines(banques):
    """§ 2.2 : un modèle par squelette, appris sur les viviers des autres racines, mondes de mêmes paramètres écartés."""
    lignes = [(r, x) for r, (viv, sb) in banques.items() for x in viv]
    out = {r: {} for r in banques}
    for sq in sorted({x["sq"] for _, x in lignes}):
        L = [(r, x) for r, x in lignes if x["sq"] == sq]
        X = np.array([traits_spec(x["texte"], x["N"], x["PM"]) for _, x in L]); y = np.array([float(x["y"]) for _, x in L])
        R = np.array([r for r, _ in L]); mids = [x["mid"] for _, x in L]
        for r in banques:
            te = R == r; mr = {x["mid"] for x in banques[r][0]}
            app = np.array([(rr != r) and (m not in mr) for rr, m in zip(R, mids)])
            s = logistique(X[app], y[app])(X[te])
            for (_, x), v in zip([l for l, t in zip(L, te) if t], s): out[r][x["cle"]] = float(v)
    return out

def sonde_commune_dans_la_racine(viv, r, traits):
    """Prototype « à la diagnostic » : un seul modèle pour tous les squelettes, appris dans la racine, plis de mondes."""
    g = np.random.default_rng(np.random.SeedSequence(r, spawn_key=(80,))); ordre = g.permutation(12)
    pli = {int(w): k % 4 for k, w in enumerate(ordre)}; out = {}
    X = np.array([traits(x["texte"], x["N"], x["PM"]) for x in viv]); y = np.array([float(x["y"]) for x in viv])
    P = np.array([pli[x["w"]] for x in viv])
    for k in range(4):
        s = logistique(X[P != k], y[P != k])(X[P == k])
        for x, v in zip([x for x, p in zip(viv, P) if p == k], s): out[x["cle"]] = float(v)
    return out

def sonde_squelette_seul(banques):
    """Sonde grossière : le score d'un énoncé est la part de faux de son squelette dans les viviers des autres racines."""
    out = {}
    for r in banques:
        c = {}
        for rr, (viv, _) in banques.items():
            if rr == r: continue
            for x in viv: c.setdefault(x["sq"], [0, 0]); c[x["sq"]][0] += x["y"]; c[x["sq"]][1] += 1
        out[r] = {x["cle"]: round(c[x["sq"]][0] / c[x["sq"]][1], 10) for x in banques[r][0]}
    return out

# ---------------------------------------------------------------- rappel au point de fonctionnement
def rappel(sv, se, regle, plaf=Fraction(1, 10)):
    nv, ne = len(sv), len(se); cv, ce = {}, {}
    for s in sv: cv[s] = cv.get(s, 0) + 1
    for s in se: ce[s] = ce.get(s, 0) + 1
    fa = Fraction(0); rec = Fraction(0)
    for s in sorted(set(cv) | set(ce), reverse=True):
        dfa = Fraction(cv.get(s, 0), nv); dr = Fraction(ce.get(s, 0), ne)
        if fa + dfa <= plaf: fa += dfa; rec += dr; continue
        return rec + ((plaf - fa) / dfa * dr if regle == "prorata" else 0)
    return rec

def exces(sb, sc, regle):
    vr = [sc[x["cle"]] for x in sb if not x["y"]]; o = {}
    for nom, f in (("faux_tot", lambda x: x["et"] == FT), ("pieges", lambda x: x["et"] == PG), ("tous", lambda x: x["y"])):
        o[nom] = float(rappel(vr, [sc[x["cle"]] for x in sb if f(x)], regle) - Fraction(1, 10))
    return o

def borne_haute(v, j):
    v = np.asarray(v, float); g = np.random.default_rng(np.random.SeedSequence(20261122, spawn_key=(2000 + j,)))
    return float(np.quantile(v[g.integers(0, len(v), (2000, len(v)))].mean(1), .95))

def resume(par_racine, j):
    out = {}
    for e in ("faux_tot", "pieges", "tous"):
        v = [d[e] for d in par_racine]; bh = borne_haute(v, j)
        out[e] = dict(moyenne=round(float(np.mean(v)), 4), borne_haute=round(bh, 4), tient=bh <= 0.10)
    return out

def main(chemin):
    sortie = {}
    cas = [("saine", "saine", 1.0), ("grandeur_1", "grandeur", 1.0), ("grandeur_0.5", "grandeur", 0.5),
           ("grandeur_0.25", "grandeur", 0.25), ("relation_1", "relation", 1.0), ("relation_0.5", "relation", 0.5),
           ("gabarit_partiel", "gabarit_partiel", 1.0)]
    for nom, var, dose in cas:
        banques = {r: construire(r, var, dose) for r in RACINES}
        res = {}
        if var != "gabarit_partiel":
            sq = sonde_par_squelette_autres_racines(banques)
            res["nombres_par_squelette_autres_racines"] = resume([exces(banques[r][1], sq[r], "prorata") for r in RACINES], 2)
            com_r = {r: sonde_commune_dans_la_racine(banques[r][0], r, traits_resume) for r in RACINES}
            res["commune_dans_la_racine_traits_resumes"] = resume([exces(banques[r][1], com_r[r], "prorata") for r in RACINES], 2)
            com_o = {r: sonde_commune_dans_la_racine(banques[r][0], r, traits_spec) for r in RACINES}
            res["commune_dans_la_racine_traits_ordonnes"] = resume([exces(banques[r][1], com_o[r], "prorata") for r in RACINES], 2)
        ss = sonde_squelette_seul(banques)
        res["squelette_seul_prorata"] = resume([exces(banques[r][1], ss[r], "prorata") for r in RACINES], 1)
        res["squelette_seul_bloc_entier"] = resume([exces(banques[r][1], ss[r], "bloc") for r in RACINES], 1)
        sortie[nom] = res
        print(nom); [print("   ", k, v) for k, v in res.items()]; sys.stdout.flush()
    # cas d'école de l'écart 2
    hv = [1.0] * 9 + [0.0] * 66; hf = [1.0] * 45 + [0.0] * 30
    ecole = {r: float(rappel(hv, hf, r) - Fraction(1, 10)) for r in ("prorata", "bloc")}
    tous_egaux = {r: float(rappel([0.0] * 75, [0.0] * 75, r) - Fraction(1, 10)) for r in ("prorata", "bloc")}
    cont = np.random.default_rng(np.random.SeedSequence(20261122, spawn_key=(3100,)))
    biais = float(np.mean([float(rappel(list(cont.random(75)), list(cont.random(75)), "prorata")) - .1 for _ in range(4000)]))
    sortie["ecole"] = dict(trait_grossier=ecole, tous_egaux=tous_egaux, biais_sonde_continue_sans_information=round(biais, 4),
                           biais_theorique=round(8 / 76 - .1, 4))
    # relecture par la plage : 6/(R+1) et contrôle par simulation
    g = np.random.default_rng(np.random.SeedSequence(20261122, spawn_key=(3101,)))
    rel = {}
    for R in (40, 120):
        th = 6 / (R + 1); hors = 0
        for _ in range(20000):
            v = g.random((R + 1, 3)); hors += any(v[-1, k] > v[:-1, k].max() or v[-1, k] < v[:-1, k].min() for k in range(3))
        rel[R] = dict(borne_union=round(th, 4), simule_trois_valeurs_independantes=round(hors / 20000, 4))
    sortie["relecture"] = rel
    print("ecole", sortie["ecole"]); print("relecture", rel)
    json.dump(sortie, open(chemin, "w"), indent=1, ensure_ascii=False)

if __name__ == "__main__":
    main(sys.argv[1])
