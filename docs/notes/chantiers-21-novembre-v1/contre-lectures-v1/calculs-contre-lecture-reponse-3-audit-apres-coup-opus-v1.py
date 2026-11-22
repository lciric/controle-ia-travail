"""Rejeu des chiffres de la conception « audit après coup » (demande 3, Fable 5.2), par le contre-lecteur.

Toutes les entrées sont des suppositions d'illustration reprises de la conception ou de ses pièces jointes ;
aucune donnée du programme, aucun résultat d'expérience. Graines : numpy.random.SeedSequence, une par bloc.
Lancer : python calculs-contre-lecture-reponse-3-audit-apres-coup-opus-v1.py
"""
import math
import sys

import numpy as np
from scipy import stats

ENTROPIE = 20261122
racine = np.random.SeedSequence(ENTROPIE)
graines = {nom: s for nom, s in zip(
    ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"], racine.spawn(8))}
echecs = []


def verifie(cond, msg):
    if not cond:
        echecs.append(msg)
        print("  ÉCHEC :", msg)


def titre(t):
    print("\n" + "=" * 100 + "\n" + t + "\n" + "=" * 100)


print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; scipy {__import__('scipy').__version__} ; entropie {ENTROPIE}")

# ---------------------------------------------------------------------------------------------
titre("R1 — Formules fermées de la conception (section 1, cas sain ; section 2 ; section 4)")
types = [(0.90, 1.0), (0.09, 5.0), (0.01, 25.0)]
sbar = sum(f * s for f, s in types)
print(f"enjeu moyen s̄ = {sbar:.4f}")
th, b = 100, 0.02
sec_u = {s: 1 - (1 - b) ** math.ceil(th / s) for _, s in types}
sec_p = {s: 1 - (1 - b * s / sbar) ** math.ceil(th / s) for _, s in types}
print("sécurité, audit uniforme   :", {k: round(v, 4) for k, v in sec_u.items()})
print("sécurité, audit à l'enjeu  :", {k: round(v, 4) for k, v in sec_p.items()})
verifie(abs(sec_u[25] - 0.0776) < 1e-3 and abs(sec_p[1] - 0.716) < 1e-3, "section 1, cas sain")
# convention : « avant que le dommage atteigne θ » (strict) contre « au plus θ » (prise comprise)
sec_p_strict = {s: 1 - (1 - b * s / sbar) ** (math.ceil(th / s) - 1) for _, s in types}
print("même chose, alarme strictement avant θ (exposant ⌈θ/s⌉ − 1) :", {k: round(v, 4) for k, v in sec_p_strict.items()})

for pm in [0.01]:
    for q in [1.0, 0.8]:
        n = math.ceil(math.log(0.05) / math.log(1 - pm * q))
        print(f"plancher {pm}, q = {q} : rang n₀,₉₅ = {n} ; P(prise ≤ n) = {1-(1-pm*q)**n:.5f} ; P(prise ≤ n−1) = {1-(1-pm*q)**(n-1):.5f}")
verifie(math.ceil(math.log(0.05) / math.log(1 - 0.008)) == 373, "rang 373 à q = 0,8")

pm, beta = 0.005, 0.015
dm = {s: s / (pm + beta * s / sbar) for _, s in types}
print("règle mixte π_min = 0,005, β = 0,015 : dommage moyen avant prise =", {k: round(v, 2) for k, v in dm.items()},
      f"; s̄/β = {sbar/beta:.2f} ; surcoût contre 80 = {dm[25]/80-1:.3f}")
print("probabilité d'audit du type 25 sous cette règle :", round(pm + beta * 25 / sbar, 4))


def p_table(K, q, L, alpha=0.05):
    if q <= 0 or L >= K:
        return None
    return (1 - alpha ** (1 / (K - L))) / q


for K, q, L in [(300, 1, 0), (30, 1, 20), (30, 0.5, 20), (30, 0.5, 28)]:
    p = p_table(K, q, L)
    print(f"table : K = {K}, q = {q}, L = {L} : p = {p:.4f} ; K·p·q = {K*p*q:.3f} ; (K−L)·p·q = {(K-L)*p*q:.3f}")
print(f"ln 20 = {math.log(20):.4f}")

# ---------------------------------------------------------------------------------------------
titre("R2 — Essai statistique du simulateur (section 1) : seuils binomiaux exacts et puissance exacte")
n95 = math.ceil(math.log(0.05) / math.log(0.99))
p0 = 1 - 0.99 ** n95
for R in [2000, 20000]:
    seuil = stats.binom.ppf(0.001, R, 0.95)
    seuil_vrai = stats.binom.ppf(0.001, R, p0)
    line = f"R = {R} : seuil sous 0,95 = {seuil:.0f} (sous la vraie {p0:.5f} : {seuil_vrai:.0f}) ;"
    for pr in [0.005, 0.009]:
        pa = 1 - (1 - pr) ** n95
        puiss = stats.binom.cdf(seuil - 1, R, pa)
        line += f" plancher {pr} → P(prise ≤ {n95}) = {pa:.4f}, puissance = {puiss:.3f} ;"
    print(line)

# ---------------------------------------------------------------------------------------------
titre("R3 — Simulateur à un seul uniforme étiqueté : absence de biais de T̂, variance fermée, strate du plancher")
rng = np.random.default_rng(graines["R3"])
N, Rrep = 5000, 4000
f_types = np.array([f for f, _ in types]); s_types = np.array([s for _, s in types])
pm, beta, gamma, q = 0.01, 0.01, 0.03, 0.8
idx = rng.choice(3, size=N, p=f_types)
s = s_types[idx]
d = (rng.random(N) < np.where(s == 25, 0.3, 0.02)).astype(float)  # dommage fixé (vue par population finie)
score = np.clip(rng.normal(0.2 + 0.4 * d, 0.2), 0, 1)              # score informatif
pi = np.minimum(1, pm + beta * s / sbar + gamma * score)
T = float((d * s).sum())
That, nf_list, xf_list = [], [], []
for _ in range(Rrep):
    U = rng.random(N)
    aud = U < pi
    v = d * (rng.random(N) < q)
    That.append(float((aud * v * s / pi).sum()))
    fl = U < pm
    nf_list.append(int(fl.sum())); xf_list.append(int((fl * v).sum()))
That = np.array(That)
var_th = float((d * s ** 2 * q * (1 / pi - q)).sum())
print(f"q·T = {q*T:.1f} ; moyenne de T̂ = {That.mean():.1f} (erreur de Monte-Carlo {That.std()/math.sqrt(Rrep):.1f})")
print(f"variance fermée = {var_th:.1f} ; variance tirée = {That.var():.1f}")
verifie(abs(That.mean() - q * T) < 4 * That.std() / math.sqrt(Rrep), "T̂ sans biais pour q·T")
verifie(abs(That.var() / var_th - 1) < 0.1, "variance de T̂")
# couverture de Clopper-Pearson sur la strate du plancher, cible = part de dommages reconnus dans la population
cible = q * d.mean()
cov = 0
for n_f, x in zip(nf_list, xf_list):
    lo, hi = stats.beta.ppf(0.025, x, n_f - x + 1) if x > 0 else 0.0, stats.beta.ppf(0.975, x + 1, n_f - x) if x < n_f else 1.0
    cov += lo <= cible <= hi
print(f"couverture à 95 % de Clopper-Pearson sur la strate du plancher (cible q·d̄ = {cible:.4f}) : {cov/Rrep:.4f}")

# ---------------------------------------------------------------------------------------------
titre("R4 — « Attaque choisie » : l'artefact « plancher abaissé pour les scores bas » est-il vu ?")
rng = np.random.default_rng(graines["R4"])
Rrep, n95 = 2000, 299
seuil_R = stats.binom.ppf(0.001, Rrep, 0.95)
print(f"R = {Rrep} répétitions ; essai binomial de la conception : refus si le compte des prises au plus tard au rang 299 < {seuil_R:.0f}")

for nom, pm_eff, beta_ in [("sain, π_min = 0,010, β = 0,015", 0.010, 0.015),
                           ("artefact, plancher 0,005 aux scores bas, β = 0,015", 0.005, 0.015),
                           ("sain, π_min = 0,010, β = 0", 0.010, 0.0),
                           ("artefact, plancher 0,005 aux scores bas, β = 0", 0.005, 0.0)]:
    pi_dmg = pm_eff + beta_ * 25 / sbar  # endommagés : g = 0, enjeu 25 ; un seul uniforme par épisode
    U = rng.random((Rrep, n95))
    c_tout = int((U < pi_dmg).any(axis=1).sum())   # toute source
    c_pl = int((U < pm_eff).any(axis=1).sum())     # source « plancher » seule (même uniforme)
    print(f"{nom:52s} : compte ≤ 299, toute source = {c_tout} ({'refus' if c_tout < seuil_R else 'passe'}) ; "
          f"source « plancher » seule = {c_pl} ({'refus' if c_pl < seuil_R else 'passe'})")

# attente 2 : audit des seuls plus suspects ; β = 0 exigé
for beta_ in [0.0, 0.015]:
    pi_dmg = 0.0 + beta_ * 25 / sbar
    print(f"π_min = 0, β = {beta_} : probabilité d'audit d'un endommagé = {pi_dmg:.4f} → "
          f"{'aucune prise' if pi_dmg == 0 else 'des prises : l’attente « meurt » ne se voit pas'}")

# ---------------------------------------------------------------------------------------------
titre("R5 — Score trompeur (b = 0,05, π_min = 0,01, q = 1) et famille tenue à l'écart simulée")
rng = np.random.default_rng(graines["R5"])
Rrep = 4000
# trompeur : endommagés à g = 0 ; β = 0 (sinon 299 ne tient pas) ; γ réglé pour que E[π] = b sur les honnêtes
for beta_ in [0.0, 0.01]:
    pi_dmg = 0.01 + beta_ * 25 / sbar
    q95 = math.ceil(math.log(0.05) / math.log(1 - pi_dmg))
    print(f"trompeur, β = {beta_}, enjeu des endommagés 25 : rang n₀,₉₅ = {q95}")
print(f"uniforme 0,05 : n₀,₉₅ = {math.ceil(math.log(0.05)/math.log(0.95))} ; rapport exact = "
      f"{math.log(1-0.05)/math.log(1-0.01):.3f} (b/π_min = 5)")
# tenue à l'écart : score indépendant du dommage, g(score) ~ Uniforme, γ tel que π_min + γ E[g] = b
gam = (0.05 - 0.01) / 0.5
caps = []
for _ in range(Rrep):
    g = rng.random(3000)
    pi_ = np.minimum(1, 0.01 + gam * g)
    pris = rng.random(3000) < pi_
    k = np.argmax(pris); caps.append(k + 1)
caps = np.array(caps)
print(f"tenue à l'écart : rang moyen de prise = {caps.mean():.2f} (uniforme : {1/0.05:.2f}) ; gain = {(1/0.05)/caps.mean():.3f}")
verifie(abs((1 / 0.05) / caps.mean() - 1) < 0.05, "gain 1 sur la famille tenue à l'écart")

# ---------------------------------------------------------------------------------------------
titre("R6 — Régime d'excès : pari en mélange contre d0, d0 connu ou d0 estimé sur m témoins")
rng = np.random.default_rng(graines["R6"])
d0, m, alpha, Rrep = 0.10, 400, 0.05, 4000
eps_acc = 0.01
J = math.ceil(math.log2((1 - d0) / eps_acc)) + 1
grille = d0 + (1 - d0) * 2.0 ** (-np.arange(1, J + 1))
print(f"grille de {J} alternatives, la plus basse = {grille[-1]:.4f} (excès {grille[-1]-d0:.4f} < {eps_acc})")


def alarme(x, d_ref):
    gr = d_ref + (1 - d_ref) * 2.0 ** (-np.arange(1, J + 1))
    lr = np.where(x[:, None] == 1, gr / d_ref, (1 - gr) / (1 - d_ref))
    W = np.cumprod(lr, axis=0).mean(axis=1)
    return bool((W >= 1 / alpha).any())


for horizon in [400, 4000]:
    fa_connu = fa_estime = 0
    for _ in range(Rrep):
        x = (rng.random(horizon) < d0).astype(int)  # nul exact : taux d0
        fa_connu += alarme(x, d0)
        d0_hat = max(1, rng.binomial(m, d0)) / m
        fa_estime += alarme(x, d0_hat)
    print(f"horizon {horizon} (épisodes de la strate du plancher) : fausses alarmes, d0 connu = {fa_connu/Rrep:.4f} ; "
          f"d0 estimé sur m = {m} = {fa_estime/Rrep:.4f} (niveau {alpha})")
# correction proposée : borne haute de Clopper-Pearson à α/2 sur la référence, pari à α/2
fa = 0
for _ in range(Rrep):
    x = (rng.random(4000) < d0).astype(int)
    k = rng.binomial(m, d0)
    d0_plus = stats.beta.ppf(1 - alpha / 2, k + 1, m - k)
    lr_alpha = alpha / 2
    gr = d0_plus + (1 - d0_plus) * 2.0 ** (-np.arange(1, J + 1))
    lr = np.where(x[:, None] == 1, gr / d0_plus, (1 - gr) / (1 - d0_plus))
    W = np.cumprod(lr, axis=0).mean(axis=1)
    fa += bool((W >= 1 / lr_alpha).any())
print(f"correction (borne haute à α/2 sur la référence, pari à α/2), horizon 4000 : fausses alarmes = {fa/Rrep:.4f}")

# ---------------------------------------------------------------------------------------------
titre("R7 — Épreuve 3 (recapture aveugle) : seuil exact dans le monde sans trace ; épreuve et étiquettes de l'étape 1")
for n in [30, 100, 300]:
    print(f"monde sans trace, n = {n} : compte des signalés de la suite ~ Bin(n, 0,01) ; refus au-dessus de "
          f"{stats.binom.ppf(0.999, n, 0.01):.0f} (quantile 0,999) ; la relecture (≥ 0,68·n = {0.68*n:.0f}) est loin au-dessus")
# taille pour séparer suite (0,545) et vrai (0,581), vrai calculé exactement (un échantillon)
for k in [2.3]:
    n1 = (k * math.sqrt(0.563 * 0.437) / 0.036) ** 2
    print(f"écart 0,036 à {k} écarts types : n ≈ {n1:.0f} en un échantillon (vrai exact), ≈ {2*n1:.0f} si le vrai est lui aussi estimé")
pq = 1 - 0.05 ** (1 / 300)
print(f"étape 1 : au taux de la table (K = 300, p·q = {pq:.4f}), 300 étiquettes demandent ≈ {300/pq:.0f} épisodes endommagés ;"
      f" 300 épisodes endommagés n'en livrent que ≈ {300*pq:.2f}")

titre("FIN")
print("contrôles :", "tous passés" if not echecs else f"{len(echecs)} échec(s) : {echecs}")
