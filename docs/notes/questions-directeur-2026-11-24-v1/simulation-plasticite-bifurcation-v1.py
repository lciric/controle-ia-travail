"""Simulations et énumérations sur processeur pour la partie II de la réponse aux questions 6 et 8
(plasticité d'un graphe de domaine, anomalies, bifurcations), v1.

Pièce de travail (classe C). Aucune dépense, aucun appel à un modèle. Tout ce qui suit porte sur
des modèles jouets ; les paramètres sont posés, ce ne sont pas des mesures d'un domaine réel.
Version finale du script commencé le 24 novembre 2026 (coupé par le quota, versé tel quel sous
partiel-fable-q6-q8-coupe-quota-v1/), reprise le 28 novembre. Le « bruit d'exploration » T du
modèle jouet n'est pas la température d'échantillonnage d'un proposeur (non réglable sur les
proposeurs Claude actuels) : c'est le niveau de fluctuation de la dynamique du modèle.

A. Modèle de champ moyen d'une région (Curie-Weiss) : m = tanh((J·m + h)/T). m : part de la
   région passée au schéma nouveau (de -1 à +1) ; J : coût d'interface entre schémas (rigidité) ;
   T : bruit d'exploration ; h : charge d'anomalies moins coût d'entrée du schéma nouveau.
   Pli, saut, hystérésis, susceptibilité, barrière.
B. Indicateurs précurseurs (variance et autocorrélation glissantes, tau de Kendall) sur une suite
   de L instantanés, à deux pas d'échantillonnage : puissance à 5 % de fausses alarmes,
   transitions précoces induites par le bruit.
C. Équilibre statique ou dynamique : système lent-rapide où la charge d'anomalies suit
   da/dt = eps·(rho_a - k(m)·a), k = k_vieux si m < 0, k_neuf sinon ; trois régimes (science normale, bascule sans retour, va-et-vient).
D. Résidu structuré : valeur propre dominante du résidu avec une composante de rang un plantée
   dans une région, contre un jumeau qui a exactement les mêmes entrées, permutées.
E. Anomalies de signe et équilibre structurel : indice de frustration exact (énumération des
   2^19 bipartitions), anomalies plantées par une distinction cachée contre jumeau au même nombre
   d'anomalies placées au hasard ; les définitions concurrentes de la plasticité (dégénérescence,
   susceptibilité, mollesse, part des anomalies qui tombent) comparées sur ce monde planté.
F. Satisfaction de contraintes sur petits paramètres (coloration à 3 valeurs de 10 variables,
   énumération des 59 049 affectations) : densité de contraintes, amas de solutions, variables
   gelées, anomalies minimales ; ajout d'une quatrième valeur à l'alphabet ; recherche locale
   sur instances à solution plantée (80 concepts).
G. Puissance d'une aire sous la courbe selon le nombre de régions (11, puis des centaines).

Graines par numpy.random.SeedSequence (règle R9) : une graine fille par partie.
Usage : python simulation-plasticite-bifurcation-v1.py   (numpy >= 1.25, bibliothèque standard)
"""
import math

import numpy as np

GRAINE_RACINE = 2026112408
ss = np.random.SeedSequence(GRAINE_RACINE)
ss_b, ss_c, ss_d, ss_e, ss_f, ss_g = ss.spawn(6)

# =============================================================================================
print("=== A. Champ moyen : équilibres de m = tanh((J·m + h)/T), T = 1 ===")


def energie_libre(m, J, h, T=1.0):
    ent = -((1 + m) / 2 * math.log((1 + m) / 2) + (1 - m) / 2 * math.log((1 - m) / 2))
    return -J * m * m / 2 - h * m - T * ent


def branche_basse(J, h, T=1.0):
    m = -0.999999
    for _ in range(20000):
        m = math.tanh((J * m + h) / T)
    return m


def branche_haute(J, h, T=1.0):
    m = 0.999999
    for _ in range(20000):
        m = math.tanh((J * m + h) / T)
    return m


def racine_instable(J, h, T=1.0):
    """Racine intermédiaire de h = T·atanh(m) - J·m, entre les deux plis (J > T, |h| < h_pli)."""
    ms = math.sqrt(1 - T / J)
    bas, haut = -ms, ms
    f = lambda m: T * math.atanh(m) - J * m - h
    for _ in range(200):
        mil = 0.5 * (bas + haut)
        if f(mil) > 0:      # f décroît entre les deux plis
            bas = mil
        else:
            haut = mil
    return 0.5 * (bas + haut)


print("rigidité J/T | charge au pli h_pli | saut de m au pli | susceptibilité à h = 0 ; 0,5 ; 0,9 ; 0,99 h_pli | "
      "barrière par concept à h = 0 ; 0,5 ; 0,9 h_pli")
for J in (0.5, 0.8, 1.0, 1.25, 1.5, 2.0, 3.0):
    if J <= 1.0:
        chi0 = 1.0 / (1.0 - J) if J < 1.0 else float("inf")
        print(f"  {J:4.2f} | aucun pli (réponse continue) | 0 | susceptibilité maximale en h = 0 : {chi0:.2f} | aucune barrière")
        continue
    ms = math.sqrt(1 - 1 / J)
    h_pli = J * ms - math.atanh(ms)
    saut = branche_haute(J, h_pli + 1e-9) - (-ms)
    chis, bars = [], []
    for frac in (0.0, 0.5, 0.9, 0.99):
        m = branche_basse(J, frac * h_pli)
        chis.append((1 - m * m) / (1 - J * (1 - m * m)))
    for frac in (0.0, 0.5, 0.9):
        m = branche_basse(J, frac * h_pli)
        mi = racine_instable(J, frac * h_pli)
        bars.append(energie_libre(mi, J, frac * h_pli) - energie_libre(m, J, frac * h_pli))
    print(f"  {J:4.2f} | {h_pli:.4f} | {saut:.4f} | " + " ; ".join(f"{c:.2f}" for c in chis) + " | "
          + " ; ".join(f"{b:.4f}" for b in bars))
print("(barrière × nombre de concepts / T = exposant du temps d'attente d'une bascule spontanée)")

# =============================================================================================
print()
print("=== B. Indicateurs précurseurs sur une suite de L instantanés (dynamique de Langevin du champ moyen) ===")
rng = np.random.default_rng(ss_b)


def simule(rng, R, N, J, h_debut, h_fin, L, delta=5.0, dt=0.05):
    """R répliques ; h passe linéairement de h_debut à h_fin ; L instantanés espacés de delta."""
    pas = int(round(delta / dt))
    m = np.full(R, branche_basse(J, h_debut))
    serie = np.empty((R, L))
    bascule = np.full(R, -1)
    h_bascule = np.full(R, np.nan)
    total = L * pas
    k = 0
    for l in range(L):
        for _ in range(pas):
            h = h_debut + (h_fin - h_debut) * k / total
            th = np.tanh(J * m + h)
            m = m + (th - m) * dt + np.sqrt(np.maximum(2.0 / N * (1 - m * th), 0.0) * dt) * rng.standard_normal(R)
            m = np.clip(m, -0.999999, 0.999999)
            k += 1
        serie[:, l] = m
        nouv = (bascule < 0) & (m > 0)
        bascule[nouv] = l
        h_bascule[nouv] = h_debut + (h_fin - h_debut) * k / total
    return serie, bascule, h_bascule


def tau_kendall(ind):
    """Tau de Kendall entre le rang temporel et l'indicateur, par ligne (les NaN donnent NaN)."""
    K = ind.shape[1]
    diff = np.sign(ind[:, None, :] - ind[:, :, None])
    haut = np.triu(np.ones((K, K), dtype=bool), 1)
    return diff[:, haut].sum(axis=1) / (K * (K - 1) / 2)


def indicateurs(serie, n_utile):
    """Variance et autocorrélation de rang 1 glissantes (fenêtre = moitié), tendance quadratique ôtée.
    n_utile : nombre d'instantanés avant la bascule, par réplique (les suivants sont ignorés)."""
    R, L = serie.shape
    taus_v = np.full(R, np.nan)
    taus_a = np.full(R, np.nan)
    for n in np.unique(n_utile):
        if n < 10:
            continue
        sel = np.where(n_utile == n)[0]
        x = serie[sel, :n]
        t = np.arange(n)
        coefs = np.polyfit(t, x.T, 2)
        res = x - (coefs[0][:, None] * t ** 2 + coefs[1][:, None] * t + coefs[2][:, None])
        w = n // 2
        nb = n - w + 1
        var = np.empty((len(sel), nb))
        ac = np.empty((len(sel), nb))
        for k in range(nb):
            f = res[:, k:k + w]
            fc = f - f.mean(axis=1, keepdims=True)
            v = (fc ** 2).mean(axis=1)
            var[:, k] = v
            ac[:, k] = (fc[:, 1:] * fc[:, :-1]).mean(axis=1) / np.maximum(v, 1e-300)
        taus_v[sel] = tau_kendall(var)
        taus_a[sel] = tau_kendall(ac)
    return taus_v, taus_a


J = 1.5
ms = math.sqrt(1 - 1 / J)
h_pli = J * ms - math.atanh(ms)
R = 300
m0 = branche_basse(J, 0.0)
print(f"rigidité J/T = {J} ; charge au pli {h_pli:.4f} ; rampe de 0 au pli sur la durée observée ; {R} répliques par case")
print(f"temps de relaxation à charge nulle : {1 / (1 - J * (1 - m0 * m0)):.2f} (unité : un passage sur tous les concepts)")
print("pas entre instantanés | concepts N | instantanés L | bascule avant 0,8 pli | séries exploitables "
      "(>= 10 instantanés avant bascule) | puissance variance | puissance autocorrélation")
for delta in (1.0, 5.0):
    for N in (100, 1000):
        for L in (15, 30, 100, 300):
            serie, bascule, h_b = simule(rng, R, N, J, 0.0, h_pli, L, delta=delta)
            n_utile = np.where(bascule >= 0, bascule, L)
            tv, ta = indicateurs(serie, n_utile)
            # nul : charge constante h = 0, mêmes longueurs utiles
            serie0, _, _ = simule(rng, R, N, J, 0.0, 0.0, L, delta=delta)
            tv0, ta0 = indicateurs(serie0, n_utile)
            ok = ~np.isnan(tv) & ~np.isnan(tv0)
            tot = np.mean(h_b < 0.8 * h_pli)
            if ok.sum() < 20:
                print(f"  {delta:3.0f} | {N:5d} | {L:4d} | {tot:.2f} | {ok.mean():.2f} | sans objet | sans objet")
                continue
            sv, sa = np.quantile(tv0[ok], 0.95), np.quantile(ta0[ok], 0.95)
            print(f"  {delta:3.0f} | {N:5d} | {L:4d} | {tot:.2f} | {ok.mean():.2f} | {np.mean(tv[ok] > sv):.2f} | "
                  f"{np.mean(ta[ok] > sa):.2f}")
print("(puissance : part des répliques exploitables dont le tau de Kendall dépasse le 95e centile du nul stationnaire ;")
print(" « bascule avant 0,8 pli » : transition induite par le bruit, bien avant le pli)")

# =============================================================================================
print()
print("=== C. Équilibre statique ou dynamique : dm/dt = tanh(J·m + A - h0) - m ; dA/dt = eps·(afflux - k(m)·A) ===")


def lent_rapide(J, h0, rho_a, k_vieux, k_neuf, eps=0.01, t_max=6000.0, dt=0.02):
    m, a = branche_basse(J, -h0), 0.0
    bascules, signe = 0, -1
    for _ in range(int(t_max / dt)):
        k = k_vieux if m < 0 else k_neuf
        m += (math.tanh(J * m + a - h0) - m) * dt
        a += eps * (rho_a - k * a) * dt
        s = 1 if m > 0 else -1
        if s != signe:
            bascules += 1
            signe = s
    return m, a, bascules


J, h0 = 1.5, 0.6
ms = math.sqrt(1 - 1 / J)
h_pli = J * ms - math.atanh(ms)
print(f"J/T = {J}, coût d'entrée h0 = {h0}, pli à la charge A = h0 + h_pli = {h0 + h_pli:.3f}, pli de retour à A = h0 - h_pli = {h0 - h_pli:.3f}")
for nom, rho_a, kv, kn in (("afflux faible, tout est absorbé", 0.3, 1.0, 1.0),
                           ("afflux fort, schéma neuf qui garde une charge", 1.0, 1.0, 1.6),
                           ("afflux fort, schéma neuf qui dissout tout", 1.0, 1.0, 4.0)):
    m, a, nb = lent_rapide(J, h0, rho_a, kv, kn)
    print(f"  {nom} : afflux/k_vieux = {rho_a / kv:.2f}, afflux/k_neuf = {rho_a / kn:.2f} -> m final {m:+.3f}, "
          f"charge finale {a:.3f}, bascules {nb}")
print("  (lecture : bascule si afflux/k_vieux dépasse h0 + h_pli ; sans retour si afflux/k_neuf reste au-dessus de h0 - h_pli)")

# =============================================================================================
print()
print("=== D. Résidu structuré : R = bruit + force·v·v^T, v porté par une région de 80 concepts sur 400 ===")
rng = np.random.default_rng(ss_d)
N, k_reg = 400, 80
v = np.zeros(N)
v[:k_reg] = 1 / math.sqrt(k_reg)
iu = np.triu_indices(N, 1)
print("force | valeur propre dominante plantée (théorie force + 1/force si force > 1, sinon 2) | jumeau permuté | "
      "détection à 5 % | masse du vecteur propre dans la région (hasard 0,20) | recouvrement au carré (théorie 1 - 1/force²)")
for theta in (0.5, 0.8, 1.0, 1.25, 1.5, 2.0, 3.0):
    tops, masses, recs, jum = [], [], [], []
    for rep in range(36):
        G = rng.standard_normal((N, N))
        W = (G + G.T) / math.sqrt(2 * N)
        Rm = W + theta * np.outer(v, v)
        val, vec = np.linalg.eigh(Rm)
        tops.append(val[-1])
        masses.append(float((vec[:k_reg, -1] ** 2).sum()))
        recs.append(float((vec[:, -1] @ v) ** 2))
        for _ in range(2):
            perm = rng.permutation(len(iu[0]))
            P = np.zeros((N, N))
            P[iu] = Rm[iu][perm]
            P = P + P.T + np.diag(np.diag(Rm))
            jum.append(np.linalg.eigvalsh(P)[-1])
    seuil = np.quantile(jum, 0.95)
    th = theta + 1 / theta if theta > 1 else 2.0
    th_rec = max(0.0, 1 - 1 / theta ** 2)
    print(f"  {theta:4.2f} | {np.mean(tops):.3f} ({th:.3f}) | {np.mean(jum):.3f} | {np.mean(np.array(tops) > seuil):.2f} | "
          f"{np.mean(masses):.3f} | {np.mean(recs):.3f} ({th_rec:.3f})")
G = rng.standard_normal((N, N))
W = (G + G.T) / math.sqrt(2 * N)
Rm = W + 1.5 * np.outer(v, v)
nb_anom = int((np.abs(Rm[iu]) > 2 / math.sqrt(N)).sum())
nb_bruit = int((np.abs(W[iu]) > 2 / math.sqrt(N)).sum())
print(f"anomalies comptées (|résidu| > 2 écarts types) : planté de force 1,5 : {nb_anom} ; jumeau permuté : {nb_anom} "
      f"(mêmes entrées) ; bruit seul : {nb_bruit} sur {len(iu[0])} paires")

# =============================================================================================
print()
print("=== E. Anomalies de signe : indice de frustration exact, distinction cachée contre jumeau ===")
rng = np.random.default_rng(ss_e)
NN, MM, KK = 20, 40, 6
x = np.arange(2 ** (NN - 1), dtype=np.uint32)
bits = [np.zeros(len(x), dtype=np.uint8)] + [((x >> i) & 1).astype(np.uint8) for i in range(NN - 1)]


def graphe_connexe(rng, n, m):
    ar = set()
    for i in range(1, n):
        j = int(rng.integers(0, i))
        ar.add((j, i))
    while len(ar) < m:
        i, j = sorted(int(t) for t in rng.choice(n, size=2, replace=False))
        ar.add((i, j))
    return sorted(ar)


def paysage(aretes, anom):
    """Nombre de relations non expliquées, pour chacune des 2^19 bipartitions (concept 0 fixé)."""
    tot = np.zeros(len(x), dtype=np.uint8)
    for (i, j), a in zip(aretes, anom):
        tot += bits[i] ^ bits[j] ^ np.uint8(a)
    return tot


def equilibre_par_parcours(n, aretes, anom):
    """Vrai si une bipartition explique toutes les anomalies (parcours en largeur)."""
    adj = {i: [] for i in range(n)}
    for (i, j), a in zip(aretes, anom):
        adj[i].append((j, a))
        adj[j].append((i, a))
    camp = {0: 0}
    file = [0]
    while file:
        i = file.pop()
        for j, a in adj[i]:
            c = camp[i] ^ a
            if j not in camp:
                camp[j] = c
                file.append(j)
            elif camp[j] != c:
                return False
    return True


def spectre_signe(n, aretes, anom):
    """Deux plus petites valeurs propres du laplacien signé (signe -1 sur les anomalies)."""
    Lm = np.zeros((n, n))
    for (i, j), a in zip(aretes, anom):
        sg = -1.0 if a else 1.0
        Lm[i, i] += 1
        Lm[j, j] += 1
        Lm[i, j] -= sg
        Lm[j, i] -= sg
    val = np.linalg.eigvalsh(Lm)
    return float(val[0]), float(val[1])


def susceptibilite(aretes, anom, E):
    """Part des relations dont le retournement du signe déplace l'optimum : aucune des
    bipartitions optimales d'avant ne reste optimale après."""
    Lf = int(E.min())
    opt = np.nonzero(E == Lf)[0]
    E16 = E.astype(np.int16)
    deplace = 0
    for (i, j), a in zip(aretes, anom):
        fe = (bits[i] ^ bits[j] ^ np.uint8(a)).astype(np.int16)
        Ee = E16 + 1 - 2 * fe
        if int(Ee[opt].min()) > int(Ee.min()):
            deplace += 1
    return deplace / len(aretes)


def aire(u1, u0):
    """Probabilité qu'une valeur de u1 dépasse une valeur de u0 (ex æquo comptés pour moitié)."""
    u1, u0 = np.asarray(u1, dtype=float), np.asarray(u0, dtype=float)
    return float(np.mean(u1[:, None] > u0[None, :]) + 0.5 * np.mean(u1[:, None] == u0[None, :]))


noms = ("plante", "jumeau", "plante_bruite")
res = {nom: [] for nom in noms}
sus = {nom: [] for nom in noms}
z_part = []
accord = 0
n_graphes, n_sus, n_nul = 120, 50, 40
for g in range(n_graphes):
    while True:
        ar = graphe_connexe(rng, NN, MM)
        u = np.zeros(NN, dtype=int)
        u[rng.choice(NN, size=KK, replace=False)] = 1
        anom_p = [int(u[i] != u[j]) for i, j in ar]
        if sum(anom_p) >= 4:
            break
    a = sum(anom_p)
    anom_j = [0] * MM
    for e in rng.choice(MM, size=a, replace=False):
        anom_j[int(e)] = 1
    anom_b = list(anom_p)
    for e in rng.choice(MM, size=3, replace=False):
        anom_b[int(e)] ^= 1
    for nom, an in (("plante", anom_p), ("jumeau", anom_j), ("plante_bruite", anom_b)):
        E = paysage(ar, an)
        Lf = int(E.min())
        eq = equilibre_par_parcours(NN, ar, an)
        accord += ((Lf == 0) == eq)
        l1, l2 = spectre_signe(NN, ar, an)
        res[nom].append((sum(an), Lf, l1, l2 - l1, math.log2((E == Lf).sum()), math.log2((E <= Lf + 1).sum())))
        if g < n_sus:
            sus[nom].append(susceptibilite(ar, an, E))
    if g < n_nul:
        # nul de placement : même graphe, même nombre d'anomalies que le planté bruité, placées au hasard
        ab = sum(anom_b)
        parts = []
        for _ in range(8):
            an0 = [0] * MM
            for e in rng.choice(MM, size=ab, replace=False):
                an0[int(e)] = 1
            parts.append(1 - int(paysage(ar, an0).min()) / ab)
        Lb = res["plante_bruite"][-1][1]
        z_part.append(((1 - Lb / ab) - np.mean(parts)) / max(np.std(parts), 1e-9))
print(f"{n_graphes} graphes connexes de {NN} concepts et {MM} relations ; distinction cachée sur {KK} concepts")
print(f"théorème de structure vérifié : « aucune anomalie irréductible » = « bipartition trouvée par parcours » "
      f"dans {accord} cas sur {3 * n_graphes}")
libs = {"plante": "anomalies dues à une distinction cachée",
        "jumeau": "même nombre d'anomalies, placées au hasard",
        "plante_bruite": "distinction cachée plus 3 signes retournés au hasard"}
for nom in noms:
    t = np.array(res[nom], dtype=float)
    part = 1 - t[:, 1] / np.maximum(t[:, 0], 1)
    print(f"  {libs[nom]} :")
    print(f"    anomalies {t[:, 0].mean():.1f} ; irréductibles après la meilleure distinction {t[:, 1].mean():.2f} ; "
          f"part des anomalies qui tombent {part.mean():.3f} ; aucune irréductible {np.mean(t[:, 1] == 0):.2f}")
    print(f"    dégénérescence : log2 du nombre de distinctions optimales {t[:, 4].mean():.2f}, à une anomalie près "
          f"{t[:, 5].mean():.2f} ; susceptibilité (part des relations dont le retournement déplace l'optimum) "
          f"{np.mean(sus[nom]):.3f}")
    print(f"    laplacien signé : plus petite valeur propre {t[:, 2].mean():.4f} ; écart à la suivante (raideur, "
          f"inverse de la mollesse) {t[:, 3].mean():.4f}")
tp = np.array(res["plante_bruite"], dtype=float)
tj = np.array(res["jumeau"], dtype=float)
print("  planté bruité contre jumeau, aire sous la courbe (0,5 = aucune séparation ; sous 0,5 = le jumeau est plus haut) :")
print(f"    nombre d'anomalies {aire(tp[:, 0], tj[:, 0]):.3f} ; part des anomalies qui tombent "
      f"{aire(1 - tp[:, 1] / tp[:, 0], 1 - tj[:, 1] / tj[:, 0]):.3f} ; dégénérescence à une anomalie près "
      f"{aire(tp[:, 5], tj[:, 5]):.3f} ; susceptibilité {aire(sus['plante_bruite'], sus['jumeau']):.3f} ; "
      f"mollesse (inverse de l'écart) {aire(-tp[:, 3], -tj[:, 3]):.3f}")
print(f"  part qui tombe du planté bruité, en écarts types du nul de placement (8 placements par graphe, "
      f"{n_nul} graphes) : moyenne {np.mean(z_part):.2f}, minimum {np.min(z_part):.2f}")

# =============================================================================================
print()
print("=== F. Contraintes « rôles différents » sur 10 concepts, 3 valeurs : énumération des 59 049 affectations ===")
rng = np.random.default_rng(ss_f)
NV = 10


def tables(q):
    idx = np.arange(q ** NV, dtype=np.int64)
    return idx, [((idx // q ** v) % q).astype(np.int8) for v in range(NV)]


idx3, col3 = tables(3)
idx4, col4 = tables(4)


def graphe_alea(rng, n, m):
    ar = set()
    while len(ar) < m:
        i, j = sorted(int(t) for t in rng.choice(n, size=2, replace=False))
        ar.add((i, j))
    return sorted(ar)


def energie(col, aretes, taille):
    e = np.zeros(taille, dtype=np.int16)
    for i, j in aretes:
        e += (col[i] == col[j])
    return e


def amas(masque, q, col, idx):
    """Amas des états de masque reliés par changement d'une seule variable ; retourne les étiquettes."""
    grand = np.int64(q ** NV + 1)
    lab = np.where(masque, idx, grand)
    while True:
        nouveau = lab.copy()
        for vv in range(NV):
            for d in range(1, q):
                c2 = (col[vv].astype(np.int64) + d) % q
                voisin = idx + (c2 - col[vv]) * q ** vv
                nouveau = np.where(masque, np.minimum(nouveau, lab[voisin]), grand)
        if np.array_equal(nouveau, lab):
            return lab
        lab = nouveau


print("densité (contraintes par concept) | satisfiable | anomalies minimales (3 valeurs) | log10 du nombre d'états "
      "minimaux | amas | part gelée par amas | log10 de la taille d'amas | anomalies minimales avec 4 valeurs")
viol_borne = 0
for alpha in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0):
    m_ar = int(round(alpha * NV))
    lignes = []
    for _ in range(20):
        ar = graphe_alea(rng, NV, m_ar)
        e3 = energie(col3, ar, 3 ** NV)
        emin = int(e3.min())
        masque = e3 == emin
        lab = amas(masque, 3, col3, idx3)
        etiq, inv = np.unique(lab[masque], return_inverse=True)
        tailles = np.bincount(inv, minlength=len(etiq))
        nb_gel = np.zeros(len(etiq))
        for vv in range(NV):
            c = col3[vv][masque]
            mn = np.full(len(etiq), 9, dtype=np.int8)
            mx = np.full(len(etiq), -1, dtype=np.int8)
            np.minimum.at(mn, inv, c)
            np.maximum.at(mx, inv, c)
            nb_gel += (mn == mx)
        gel = nb_gel / NV
        viol_borne += int(np.sum(tailles > 3.0 ** ((1 - gel) * NV) + 1e-9))
        larg = np.log10(tailles)
        e4min = int(energie(col4, ar, 4 ** NV).min())
        lignes.append((emin == 0, emin, math.log10(masque.sum()), len(etiq), np.mean(gel), np.mean(larg), e4min))
    t = np.array(lignes, dtype=float)
    print(f"  {alpha:3.1f} | {t[:, 0].mean():.2f} | {t[:, 1].mean():.2f} | {t[:, 2].mean():.2f} | {t[:, 3].mean():.1f} | "
          f"{t[:, 4].mean():.3f} | {t[:, 5].mean():.2f} | {t[:, 6].mean():.2f}")
print(f"violations de la borne taille d'amas <= 3^((1 - part gelée)·10) : {viol_borne}")


def recherche_locale(rng, n, aretes, q=3, plafond=60000, bruit=0.2):
    ar = np.array(aretes)
    col = rng.integers(0, q, size=n)
    vois = {i: [] for i in range(n)}
    for i, j in aretes:
        vois[i].append(j)
        vois[j].append(i)
    for pas in range(plafond):
        viol = np.nonzero(col[ar[:, 0]] == col[ar[:, 1]])[0]
        if len(viol) == 0:
            return pas
        i = int(ar[int(viol[int(rng.integers(0, len(viol)))]), int(rng.integers(0, 2))])
        if rng.random() < bruit:
            col[i] = (col[i] + int(rng.integers(1, q))) % q
        else:
            compte = np.zeros(q)
            for j in vois[i]:
                compte[col[j]] += 1
            meilleurs = np.nonzero(compte == compte.min())[0]
            col[i] = int(meilleurs[int(rng.integers(0, len(meilleurs)))])
    return plafond


print("recherche locale sur instances à solution plantée (80 concepts, 3 valeurs, plafond 60 000 retouches) :")
print("densité | médiane des retouches jusqu'à une solution | part d'échecs au plafond")
NP = 80
for alpha in (1.0, 1.5, 2.0, 2.3, 2.6, 3.0, 4.0, 6.0, 10.0):
    m_ar = int(round(alpha * NP))
    pas_l = []
    for _ in range(24):
        plante = rng.permutation(np.arange(NP) % 3)
        ar = set()
        while len(ar) < m_ar:
            i, j = sorted(int(t) for t in rng.choice(NP, size=2, replace=False))
            if plante[i] != plante[j]:
                ar.add((i, j))
        pas_l.append(recherche_locale(rng, NP, sorted(ar)))
    pas_l = np.array(pas_l)
    print(f"  {alpha:4.1f} | {np.median(pas_l):8.0f} | {np.mean(pas_l >= 60000):.2f}")

# =============================================================================================
print()
print("=== G. Puissance d'une aire sous la courbe selon le nombre de régions ===")
rng = np.random.default_rng(ss_g)


def inv_phi(p):
    bas, haut = -10.0, 10.0
    for _ in range(200):
        mil = 0.5 * (bas + haut)
        if 0.5 * (1 + math.erf(mil / math.sqrt(2))) < p:
            bas = mil
        else:
            haut = mil
    return 0.5 * (bas + haut)


def aires(rng, n_pos, n_neg, d, rep=4000):
    pos = rng.standard_normal((rep, n_pos)) + d
    neg = rng.standard_normal((rep, n_neg))
    return (pos[:, :, None] > neg[:, None, :]).mean(axis=(1, 2))


print("régions (positives + négatives) | seuil unilatéral à 5 % sous le nul | puissance si l'aire vraie vaut 0,60 ; 0,65 ; 0,70 ; 0,80")
for n_pos, n_neg in ((5, 6), (15, 15), (30, 30), (60, 60), (125, 125), (250, 250)):
    rep = 4000 if n_pos <= 60 else (1500 if n_pos <= 125 else 800)
    nul = aires(rng, n_pos, n_neg, 0.0, rep)
    seuil = np.quantile(nul, 0.95)
    puiss = []
    for a in (0.60, 0.65, 0.70, 0.80):
        d = math.sqrt(2) * inv_phi(a)
        puiss.append(np.mean(aires(rng, n_pos, n_neg, d, rep) > seuil))
    print(f"  {n_pos + n_neg:4d} ({n_pos} + {n_neg}) | {seuil:.3f} | " + " ; ".join(f"{p:.2f}" for p in puiss))
