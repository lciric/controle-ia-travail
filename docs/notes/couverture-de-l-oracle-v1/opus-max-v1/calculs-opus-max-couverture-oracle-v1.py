# Calculs de la note « couverture de l'oracle » (Opus 5.5, effort maximal), v1.
# Lois exactes sauf mention ; simulations par numpy.random.SeedSequence (R9).
# Toutes les valeurs d'entrée sont des SUPPOSITIONS D'ILLUSTRATION : aucune donnée du programme.
# Lancement : python3 calculs-opus-max-couverture-oracle-v1.py > calculs-opus-max-couverture-oracle-v1.txt
import math
import sys
import platform
import numpy as np

ENTROPIE = 20261121173000  # racine fixée à l'écriture, consignée ici
racine = np.random.SeedSequence(ENTROPIE)
enfants = racine.spawn(4)  # F, G, et deux réserves

print("Calculs de la note couverture de l'oracle, Opus 5.5, v1")
print(f"python {platform.python_version()}, numpy {np.__version__}")
print(f"SeedSequence entropie={ENTROPIE} ; enfants spawn_key={[c.spawn_key for c in enfants]}")
print("Toutes les entrees sont des suppositions d'illustration.\n")


def logbinom_pmf(k, n, q):
    if q <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if q >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(q) + (n - k) * math.log1p(-q))


def binom_cdf_ge(x, n, q):
    """P(X >= x) pour X ~ Binomiale(n, q), exacte."""
    if x <= 0:
        return 1.0
    s = 0.0
    for k in range(x, n + 1):
        lp = logbinom_pmf(k, n, q)
        if lp > -math.inf:
            s += math.exp(lp)
    return min(1.0, s)


def cp_lower(x, n, alpha=0.05):
    """Borne basse unilatérale de Clopper-Pearson au niveau 1-alpha pour x succès sur n."""
    if x == 0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        # plus grand q tel que P(X >= x | q) <= alpha
        if binom_cdf_ge(x, n, mid) > alpha:
            hi = mid
        else:
            lo = mid
    return lo


def cp_upper(x, n, alpha=0.05):
    """Borne haute unilatérale de Clopper-Pearson au niveau 1-alpha."""
    if x == n:
        return 1.0
    return 1.0 - cp_lower(n - x, n, alpha)


# ---------------------------------------------------------------- Bloc A
print("=== Bloc A : plancher, regime de signature. Episodes endommages avant la prise, au seuil 0,95 ===")
print("N95 = ceil(ln 0.05 / ln(1 - p q)) ; moyenne 1/(p q).")
for p in (0.01, 0.05):
    for q in (1.0, 0.95, 0.8, 0.5, 0.2, 0.05):
        n95 = math.ceil(math.log(0.05) / math.log(1 - p * q))
        print(f"  p={p:.2f} q={q:.2f} : N95={n95:6d} ; moyenne={1/(p*q):8.1f}")
print("  Lecture : l'attaquant qui choisit la strate prend le q le plus bas qu'il peut atteindre.\n")

# ---------------------------------------------------------------- Bloc B
print("=== Bloc B : certifier q >= q0 dans une strate par des dommages plantes (borne exacte, 95 %) ===")
print("B1. Regle zero manque : n0 = ceil(ln 0.05 / ln q0) plants, tous reconnus.")
for q0 in (0.5, 0.7, 0.8, 0.9, 0.95, 0.99):
    n0 = math.ceil(math.log(0.05) / math.log(q0))
    print(f"  q0={q0:.2f} : n0={n0}")
print("B2. Puissance : plus petit n tel que P(borne basse CP 95 % >= q0) >= 0,8 quand le vrai q vaut q_vrai.")


def puissance(n, q_vrai, q0):
    # le plus petit nombre de reconnus x tel que cp_lower(x, n) >= q0
    xs = None
    for x in range(n + 1):
        if cp_lower(x, n) >= q0:
            xs = x
            break
    if xs is None:
        return 0.0, None
    return binom_cdf_ge(xs, n, q_vrai), xs


B2_res = {}
for q_vrai, q0 in ((0.95, 0.9), (0.95, 0.8), (0.9, 0.8), (0.9, 0.7), (0.8, 0.5), (0.7, 0.5), (0.9, 0.5)):
    trouve = None
    for n in range(2, 801):
        pw, xs = puissance(n, q_vrai, q0)
        if pw >= 0.8:
            trouve = (n, xs, pw)
            break
    B2_res[(q_vrai, q0)] = trouve
    if trouve:
        print(f"  q_vrai={q_vrai:.2f} q0={q0:.2f} : n={trouve[0]} (reconnus exiges >= {trouve[1]}), puissance={trouve[2]:.3f}")
    else:
        print(f"  q_vrai={q_vrai:.2f} q0={q0:.2f} : n > 800")
print("B4. Objet de controle de la regle de certification : probabilite de certifier a tort (vrai q au seuil ou dessous).")
for n, xs, q0, faux in ((82, 72, 0.8, (0.8, 0.75, 0.7)), (8, 7, 0.5, (0.5, 0.4)), (30, 28, 0.8, (0.8, 0.7))):
    for qf in faux:
        print(f"  n={n}, reconnus >= {xs} (certifie q >= {q0}) ; vrai q={qf:.2f} : P(certifier)={binom_cdf_ge(xs, n, qf):.4f}")
print("B3. Familles tenues a l'ecart toutes couvertes sur n cycles : borne basse exacte 95 % de la part couverte = 0,05^(1/n).")
for ncyc in (1, 2, 3, 5, 10, 20):
    print(f"  n={ncyc:2d} cycles, tous couverts : part couverte >= {0.05 ** (1 / ncyc):.3f}")
print()

# ---------------------------------------------------------------- Bloc C
print("=== Bloc C : arbitrage plants contre audits (illustration) ===")
H, K, S = 10_000, 100, 12
q_vrai = 0.9
seuil = 1 - 0.05 ** (1 / K)
print(f"Suppositions : horizon H={H} episodes, seuil tolere K={K} episodes endommages, S={S} strates,")
print(f"vrai q={q_vrai} dans chaque strate ; p*q0 >= 1-0,05^(1/K) = {seuil:.4f} ; plants dimensionnes a puissance 0,8.")
for cout_plant in (1.0, 3.0):
    print(f"  cout d'un plant = {cout_plant} audit(s)")
    for q0 in (0.5, 0.7, 0.8):
        n = B2_res.get((q_vrai, q0))
        if n is None:
            # calcule si absent
            for nn in range(2, 801):
                pw, xs = puissance(nn, q_vrai, q0)
                if pw >= 0.8:
                    n = (nn, xs, pw)
                    break
        p = seuil / q0
        audits = H * p
        plants = S * n[0]
        total = audits + cout_plant * plants
        print(f"    q0={q0:.2f} : p={p:.4f} ; audits={audits:7.0f} ; plants={plants:5d} ; total={total:7.0f}")
print("  Lecture : certifier un q0 modeste coute peu de plants et un audit plus dense ; l'optimum depend du prix relatif.\n")

# ---------------------------------------------------------------- Bloc D
print("=== Bloc D : loi de resolution q(d) et dommage attendu avant la premiere prise (regime de signature) ===")
print("Dommage par episode d dans (0, 1] (1 = plafond) ; prise par episode endommage h = p q(d) ;")
print("dommage attendu avant prise, borne par l'horizon : E[D](d) = d (1 - (1-h)^H) / h ; l'attaquant prend le sup sur d.")
p, H = 0.01, 10_000
grille = np.concatenate([np.geomspace(1e-4, 1.0, 400)])


def ED(d, q):
    h = p * q
    if h <= 0:
        return d * H
    return d * (1 - (1 - h) ** H) / h


lois = {
    "lineaire q=min(1, 2d)": lambda d: min(1.0, 2 * d),
    "quadratique q=min(1, 2d^2)": lambda d: min(1.0, 2 * d * d),
    "seuil net q=0,9 si d>=0,2, sinon 0": lambda d: 0.9 if d >= 0.2 else 0.0,
    "seuil doux q=0,9/(1+exp(-(d-0,2)/0,03))": lambda d: 0.9 / (1 + math.exp(-(d - 0.2) / 0.03)),
}
optimum = {}
for nom, f in lois.items():
    vals = [(ED(d, f(d)), d, f(d)) for d in grille]
    best = max(vals)
    optimum[nom] = best
    print(f"  {nom:42s} : sup E[D]={best[0]:8.1f} a d={best[1]:.4f} (q(d)={best[2]:.4f}) ; a d=1 : E[D]={ED(1.0, f(1.0)):6.1f}")
print("  Reference, loi lineaire : sup_d d/(p q(d)) = max(1/(p c), 1/(p q(1))) = max(50, 100) = 100, sans dependance a l'horizon.")
print("  Dependance a l'horizon H (meme p) :")
for HH in (10_000, 100_000):
    H = HH
    ligne = []
    for nom, f in lois.items():
        best = max((ED(d, f(d)), d) for d in grille)
        ligne.append(f"{nom.split(' q')[0].replace(' ', '_')}={best[0]:.0f}")
    print(f"    H={HH:7d} : " + " ; ".join(ligne))
H = 10_000
print("  Lecture : ce qui fixe la garantie est inf q(d)/d aux petites doses, pas q aux doses flagrantes.")
# biais de spectre : moyenne des plants flagrants
nom_doux = "seuil doux q=0,9/(1+exp(-(d-0,2)/0,03))"
f = lois[nom_doux]
dp = np.linspace(0.5, 1.0, 51)
print(f"  Biais de spectre : q moyen sur plants a doses [0,5 ; 1] = {np.mean([f(x) for x in dp]):.3f} ;"
      f" q a la dose ou l'attaquant maximise E[D] (d={optimum[nom_doux][1]:.4f}) = {optimum[nom_doux][2]:.4f}\n")

# ---------------------------------------------------------------- Bloc E
print("=== Bloc E : recoupement de deux lecteurs (Lincoln-Petersen) et angle mort commun ===")
N = 1000
q1, q2 = 0.7, 0.6
print(f"N={N} dommages ; hors angle mort, lecteurs independants q1={q1}, q2={q2} ; part b invisible aux deux.")
for b in (0.0, 0.1, 0.3):
    vis = N * (1 - b)
    n1, n2, m = vis * q1, vis * q2, vis * q1 * q2
    Nhat = n1 * n2 / m
    union = vis * (1 - (1 - q1) * (1 - q2))
    print(f"  b={b:.1f} : N estime={Nhat:7.1f} ; couverture estimee de la reunion={union/Nhat:.3f} ; vraie={union/N:.3f}")
print("Heterogeneite sans angle mort : moitie subtile (q=0,2 pour les deux), moitie flagrante (q=0,9 pour les deux).")
n1 = 500 * 0.2 + 500 * 0.9
n2 = n1
m = 500 * 0.04 + 500 * 0.81
Nhat = n1 * n2 / m
union = 500 * (1 - 0.8 ** 2) + 500 * (1 - 0.1 ** 2)
print(f"  N estime={Nhat:.1f} (vrai 1000) ; couverture estimee={union/Nhat:.3f} ; vraie={union/1000:.3f}")
print("Source d'une autre nature T (verite par construction, tiree au hasard, q_T=0,3 independante de la classe) :")
rng = np.random.default_rng(enfants[0])
reps = 2000
est_LP, est_T = [], []
for _ in range(reps):
    subtil = rng.random(N) < 0.5
    qa = np.where(subtil, 0.2, 0.9)
    r1 = rng.random(N) < qa
    r2 = rng.random(N) < qa
    R = r1 | r2
    T = rng.random(N) < 0.3
    mm = np.sum(r1 & r2)
    est_LP.append(np.sum(r1) * np.sum(r2) / max(mm, 1))
    mt = np.sum(R & T)
    est_T.append(np.sum(R) * np.sum(T) / max(mt, 1))
est_LP, est_T = np.array(est_LP), np.array(est_T)
print(f"  {reps} repliques : LP deux lecteurs : moyenne={est_LP.mean():.1f}, 5-95 %=[{np.quantile(est_LP,0.05):.1f} ; {np.quantile(est_LP,0.95):.1f}]")
print(f"  reunion des lecteurs croisee avec T : moyenne={est_T.mean():.1f}, 5-95 %=[{np.quantile(est_T,0.05):.1f} ; {np.quantile(est_T,0.95):.1f}] (vrai 1000)")
print("  Lecture : le croisement de lecteurs semblables ne voit pas l'aveuglement commun ; une source d'une autre nature le voit.\n")

# ---------------------------------------------------------------- Bloc F
print("=== Bloc F : masse manquante des genres (Good-Turing) a petit effectif ===")
G = 200
poids = 1.0 / np.arange(1, G + 1) ** 1.1
poids /= poids.sum()
print(f"Suppositions : {G} genres de dommage, loi de Zipf d'exposant 1,1 ; N dommages trouves par audits ouverts.")
rng = np.random.default_rng(enfants[1])
for Nn in (30, 100, 300, 1000):
    gt, vrai = [], []
    for _ in range(2000):
        tir = rng.choice(G, size=Nn, p=poids)
        cnt = np.bincount(tir, minlength=G)
        n1g = np.sum(cnt == 1)
        gt.append(n1g / Nn)
        vrai.append(poids[cnt == 0].sum())
    gt, vrai = np.array(gt), np.array(vrai)
    err = gt - vrai
    print(f"  N={Nn:5d} : masse vraie moyenne={vrai.mean():.3f} ; estimation GT moyenne={gt.mean():.3f} ;"
          f" erreur 5-95 %=[{np.quantile(err,0.05):+.3f} ; {np.quantile(err,0.95):+.3f}]")
print("  Lecture : estimation de la loi naturelle des genres, jamais une borne contre l'attaquant qui choisit un genre.\n")

# ---------------------------------------------------------------- Bloc G
print("=== Bloc G : audit d'or sur episodes naturels (double echantillonnage) : tailles ===")
print("Demi-largeur de l'intervalle bilateral exact (Clopper-Pearson 95 %) sur q a q=0,8, selon le nombre de dommages vus par l'or.")
for npos in (10, 30, 60, 100, 200):
    x = round(0.8 * npos)
    lo = cp_lower(x, npos, 0.025)
    hi = cp_upper(x, npos, 0.025)
    print(f"  {npos:4d} dommages dores : q estime={x/npos:.2f}, IC95=[{lo:.3f} ; {hi:.3f}], demi-largeur~{(hi-lo)/2:.3f}")
print("Audits d'or necessaires pour 100 dommages dores, selon la prevalence du dommage parmi les episodes audites :")
for pi in (0.5, 0.1, 0.02):
    print(f"  prevalence={pi:.2f} : {100/pi:7.0f} audits d'or")
print()

# ---------------------------------------------------------------- Bloc H
print("=== Bloc H : elargir n'est pas gratuit en regime d'exces (approximation normale) ===")
print("Taux lu parmi les audites r = f + (q - f) s ; episodes audites pour detecter l'exces (alpha 0,05 unilateral, puissance 0,8).")
za, zb = 1.6448536269514722, 0.8416212335729143
for s in (0.05, 0.01):
    for q, fr in ((0.5, 0.02), (0.8, 0.02), (0.8, 0.10), (0.95, 0.30)):
        r = fr + (q - fr) * s
        n = ((za * math.sqrt(fr * (1 - fr)) + zb * math.sqrt(r * (1 - r))) / ((q - fr) * s)) ** 2
        print(f"  s={s:.2f} q={q:.2f} f={fr:.2f} : audites~{n:9.0f} ; episodes a p=0,05 : {n/0.05:10.0f}")
print("  Lecture : un oracle elargi qui gagne en q mais perd en specificite peut rendre l'alarme plus lente.\n")
print("Fin.")
