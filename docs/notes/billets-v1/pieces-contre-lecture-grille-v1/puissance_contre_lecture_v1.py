"""Puissance du plan d'analyse de la grille brouillon 2 (contre-lecture). Aucun texte lu, aucun codage réel.
Calcul exact pour le test du signe avec Holm (premier pas), simulation pour la règle du gabarit."""
import math, json, sys
import numpy as np
ENTROPIE = 271828182845904523536028747135266249775  # écrite avant tout calcul
N = 23; N_PROPRE = 11; N_SANS = 16

def p_signe(a, b):
    n = a + b
    if n == 0: return 1.0
    k = min(a, b)
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n)

def puissance(p1, p0, m, n=N, sens=+1):
    """P(p du signe exact <= 0,05/m et différence dans le sens attendu), paires indépendantes."""
    qp, qm = p1 * (1 - p0), (1 - p1) * p0
    q0 = 1 - qp - qm
    tot = 0.0
    for a in range(n + 1):
        for b in range(n + 1 - a):
            if (a - b) * sens <= 0: continue
            if p_signe(a, b) <= 0.05 / m:
                tot += math.factorial(n) / (math.factorial(a) * math.factorial(b) * math.factorial(n - a - b)) * qp ** a * qm ** b * q0 ** (n - a - b)
    return tot

res = {"entropie": ENTROPIE, "numpy": np.__version__}
# 1. configurations minimales qui passent Holm au premier pas
mini = {}
for m in (23, 15, 10, 5, 1):
    L = []
    for b in range(0, 6):
        for a in range(b + 1, N - b + 1):
            if p_signe(a, b) <= 0.05 / m:
                L.append((a, b, round((a - b) / N, 3))); break
    mini[m] = L
res["configurations_minimales(n+,n-,d)"] = mini
print("Configurations minimales (paires pour, paires contre, d) qui passent Holm au premier pas, 23 paires :")
for m, L in mini.items(): print("  m =", m, L)
# 11 paires
print("  11 paires, m=23 :", [(a, b) for b in range(3) for a in range(b + 1, 12 - b) if p_signe(a, b) <= 0.05 / 23][:3])

# 2. puissance exacte
print("\nPuissance (probabilité de passer Holm au premier pas), 23 paires indépendantes :")
print("  fréquences (appariés -> bien notés)   écart   m=23   m=15   m=10   m=1")
tab = []
for p0, p1 in [(0.4, 0.6), (0.35, 0.65), (0.3, 0.7), (0.25, 0.75), (0.2, 0.8), (0.15, 0.85), (0.1, 0.9), (0.05, 0.95),
               (0.1, 0.4), (0.1, 0.5), (0.1, 0.6), (0.1, 0.7), (0.1, 0.8), (0.5, 0.9), (0.4, 0.9), (0.3, 0.9), (0.2, 0.9), (0.6, 0.9), (0.7, 0.95)]:
    r = [puissance(p1, p0, m) for m in (23, 15, 10, 1)]
    tab.append({"p0": p0, "p1": p1, "ecart": round(p1 - p0, 2), "m23": r[0], "m15": r[1], "m10": r[2], "m1": r[3]})
    print(f"  {p0:.2f} -> {p1:.2f}                         {p1-p0:.2f}   " + "   ".join(f"{x:.3f}" for x in r))
res["puissance"] = tab
# écart nécessaire pour 80 % et 50 % (centré sur 0,5 ; et appariés à 0,10)
def ecart_requis(cible, m, mode):
    for e in np.arange(0.05, 0.96, 0.01):
        if mode == "centre": p0, p1 = 0.5 - e / 2, 0.5 + e / 2
        else: p0, p1 = 0.10, 0.10 + e
        if p1 > 0.999: break
        if puissance(p1, p0, m) >= cible: return round(float(e), 2)
    return None
req = {}
for m in (23, 15, 10, 1):
    req[m] = {mode: {str(c): ecart_requis(c, m, mode) for c in (0.5, 0.8)} for mode in ("centre", "apparies_a_0.10")}
res["ecart_requis"] = req
print("\nÉcart vrai requis pour une puissance de 50 % et de 80 % :")
for m, v in req.items(): print("  m =", m, v)

# 3. règle du gabarit par simulation
ss = np.random.SeedSequence(ENTROPIE); rng = np.random.default_rng(ss.spawn(1)[0])
R = 200_000
cache = {}
def borne_basse_positive(a, b, n=N, B=20000):
    """L'intervalle par rééchantillonnage (percentile, 95 %) de d a-t-il sa borne basse > 0 ?"""
    if (a, b) not in cache:
        t = rng.multinomial(n, [a / n, b / n, 1 - (a + b) / n], size=B)
        dd = (t[:, 0] - t[:, 1]) / n
        cache[(a, b)] = float(np.quantile(dd, 0.025)) > 0
    return cache[(a, b)]
def regle(p1, p0, m=23):
    x1 = rng.random((R, N)) < p1; x0 = rng.random((R, N)) < p0; xs = rng.random((R, N_SANS)) < p1
    freq = (x1.sum(1) + xs.sum(1)) / (N + N_SANS)
    d = x1.astype(int) - x0.astype(int)
    a, b = (d > 0).sum(1), (d < 0).sum(1)
    d_tous = d.mean(1); d_propre = d[:, :N_PROPRE].mean(1)
    pv = np.array([p_signe(int(i), int(j)) for i, j in zip(a, b)])
    holm = pv <= 0.05 / m
    eviter = holm & (d_tous < 0)
    c3 = freq >= 0.5; c4a = d_tous >= 0; c4b = d_propre >= 0
    consigne = ~eviter & c3 & c4a & c4b
    distinct = consigne & holm & (d_tous > 0)
    reserve = ~eviter & c3 & (c4a ^ c4b)
    reserve_contre = ~eviter & c3 & ~c4a & c4b
    piste_base = ~eviter & ~c3 & ~consigne & ~reserve
    piste = np.zeros(R, bool)
    idx = np.where(piste_base & (a > b))[0]
    for i in idx: piste[i] = borne_basse_positive(int(a[i]), int(b[i]))
    return {"consigne (toutes)": float(consigne.mean()), "dont distinctive": float(distinct.mean()), "sous réserve": float(reserve.mean()),
            "dont d<0 sur les 23 paires": float(reserve_contre.mean()), "à éviter": float(eviter.mean()), "piste": float(piste.mean())}
print("\nRègle du gabarit (section 8), 200 000 tirages, fiabilité supposée acquise, m = 23 :")
sim = []
for p0, p1 in [(0.3, 0.3), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 0.8), (0.9, 0.9), (0.7, 0.5), (0.8, 0.6), (0.9, 0.7), (0.5, 0.7), (0.6, 0.8), (0.3, 0.6), (0.2, 0.8), (0.1, 0.4), (0.05, 0.45)]:
    r = regle(p1, p0); sim.append({"p0_apparies": p0, "p1_bien_notes": p1, **r})
    print(f"  appariés {p0:.2f}, bien notés {p1:.2f} : " + " ; ".join(f"{k} {v:.3f}" for k, v in r.items()))
res["regle_gabarit"] = sim

# 4. fiabilité : probabilité de passer le seuil 0,60 sur 62 billets ET sur 44 (sous-ensemble)
def kappa_bin(a, b):
    po = (a == b).mean(1); pa, pb = a.mean(1), b.mean(1)
    pe = pa * pb + (1 - pa) * (1 - pb)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(pe < 1, (po - pe) / (1 - pe), np.nan), po, (pa + pb) / 2
print("\nFiabilité : probabilité d'être déclaré fiable (règle 5.2), 62 billets dont 44 hors marquage 1, 50 000 tirages :")
fi = []
R2 = 50_000
for kv in (0.4, 0.5, 0.6, 0.7, 0.8):
    for prev in (0.15, 0.3, 0.5, 0.93):
        # table 2x2 à marges égales prev et kappa kv : P(1,1)=prev^2+kv*prev*(1-prev)
        p11 = prev ** 2 + kv * prev * (1 - prev); p10 = prev - p11; p00 = 1 - p11 - 2 * p10
        c = rng.choice(4, size=(R2, 62), p=[p11, p10, p10, p00])
        A = (c == 0) | (c == 1); Bc = (c == 0) | (c == 2)
        ok = np.ones(R2, bool)
        for n in (62, 44):
            k, po, pr = kappa_bin(A[:, :n], Bc[:, :n])
            f = np.where(pr > 0.90, po >= 0.90, np.where(pr < 0.10, False, np.nan_to_num(k, nan=-1) >= 0.60))
            ok &= f.astype(bool)
        fi.append({"kappa_vrai": kv, "prevalence": prev, "p_fiable": float(ok.mean())})
        print(f"  kappa vrai {kv:.1f}, prévalence {prev:.2f} : déclaré fiable {ok.mean():.3f}")
res["fiabilite"] = fi
# accord dû au hasard à prévalence haute
print("\nAccord brut attendu par pur hasard (deux codeurs indépendants, même prévalence) :", {p: round(p * p + (1 - p) ** 2, 3) for p in (0.90, 0.92, 0.95, 0.97)})
json.dump(res, open(sys.argv[1], "w"), ensure_ascii=False, indent=1, default=float)
