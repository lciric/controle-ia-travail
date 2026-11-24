"""Calculs sur processeur pour la réponse à la question 4 (l'émergence : transition topologique
et groupes en interaction), v1.

Pièce de travail (classe C). Aucune dépense, aucun appel à un modèle. Tous les paramètres
marqués « posé » sont des hypothèses de planification, non des mesures.

A. Percolation finie du graphe de communication de l'organisme : dans G(N, c/(N-1)), avec une
   fidélité de relais f par arête (percolation de liens : graphe équivalent G(N, c*f/(N-1))),
   part moyenne de la plus grande composante S et probabilité P que deux agents donnés soient
   reliés par un chemin, pour N = 8, 16, 32, 64 ; limite infinie : S solution de
   S = 1 - exp(-c S), et P -> S^2.
B. Puissance du contraste « agents séparés contre interaction complète » sur le nombre de
   structures plantées distinctes retrouvées par monde (K = 12 ou 24), plan apparié par monde,
   comptes bêta-binomiaux ; test bilatéral au seuil 0,05/3 (correction de Holm, pire cas) et
   test d'équivalence (deux tests unilatéraux à 0,05) aux bornes de plus ou moins 20 %.
C. Structures composites (deux moitiés tenues par deux agents distincts) :
   C1. précision de la fidélité de relais f mesurée à part sur des chaînes de L sauts,
       r(L) = h * f^(L-1), estimation par maximum de vraisemblance sur grille ;
   C2. courbes de dose prédites sans paramètre libre (N = 16) : « percolation » (les deux moitiés
       se rencontrent si leurs détenteurs sont reliés dans le graphe dilué par f) contre
       « voisins directs » (rencontre seulement si les détenteurs sont adjacents) ;
   C3. justesse de la discrimination entre les deux courbes avec M courses par dose.
D. Taille d'effet décelable du test d'observation (étude d'événement en différences de
   différences, erreurs autorégressives d'ordre 1), sous hypothèses posées.
E. Jetons et coût de l'essai dans l'organisme, aux tarifs inscrits au dépôt
   (devis-collisionneur-boucle-organisme-controle-v2.md ; registres/depenses.md).

Graines par numpy.random.SeedSequence (règle R9) : une graine fille par partie, puis par cellule.
Usage : python simulation-emergence-organisme-v1.py  (numpy >= 1.25)
"""
import math
import numpy as np

GRAINE_RACINE = 20261124
ss = np.random.SeedSequence(GRAINE_RACINE)
ss_a, ss_b, ss_c, ss_d = ss.spawn(4)


def composantes(adj):
    """Étiquettes de composantes (plus petit indice) par propagation du minimum, en lot.
    adj : (B, N, N) booléen symétrique, diagonale vraie."""
    B, N, _ = adj.shape
    lab = np.tile(np.arange(N, dtype=np.float32), (B, 1))
    while True:
        new = np.where(adj, lab[:, None, :], np.float32(np.inf)).min(axis=2)
        if np.array_equal(new, lab):
            return lab.astype(np.int64)
        lab = new


def tirer_graphes(rng, B, N, p):
    """B graphes de Erdos-Renyi G(N, p), matrices d'adjacence avec diagonale vraie."""
    u = rng.random((B, N, N)) < p
    tri = np.triu(u, 1)
    adj = tri | np.transpose(tri, (0, 2, 1))
    idx = np.arange(N)
    adj[:, idx, idx] = True
    return adj


def s_infini(c):
    if c <= 1:
        return 0.0
    s = 0.5
    for _ in range(500):
        s = 1 - math.exp(-c * s)
    return s


def q_t(z, nu):
    """Quantile de Student approché par Cornish-Fisher à partir du quantile normal z."""
    return z + (z**3 + z) / (4 * nu) + (5 * z**5 + 16 * z**3 + 3 * z) / (96 * nu**2)


def partie_a():
    print("=== A. Percolation finie du graphe de communication (c_eff = c*f) ===")
    doses = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0, 4.0]
    tailles = [8, 16, 32, 64]
    cellules = ss_a.spawn(len(tailles) * len(doses))
    k = 0
    print("N    c_eff  S_moyen  P(deux agents relies)   [limite infinie : S, S^2]")
    for N in tailles:
        B = 3000 if N <= 32 else 1500
        for c in doses:
            rng = np.random.default_rng(cellules[k]); k += 1
            adj = tirer_graphes(rng, B, N, min(1.0, c / (N - 1)))
            lab = composantes(adj)
            comptes = (lab[:, :, None] == np.arange(N)[None, None, :]).sum(axis=1)
            S = comptes.max(axis=1).mean() / N
            P = (lab[:, 0] == lab[:, 1]).mean()
            si = s_infini(c)
            print(f"{N:<4d} {c:5.2f}  {S:6.3f}   {P:6.3f}                  [{si:5.3f}, {si*si:5.3f}]")
    print()


def partie_b():
    print("=== B. Puissance : séparés contre interaction complète (plan apparié par monde) ===")
    p_full, sigma_u = 0.40, 0.6  # posés
    print(f"posés : p(interaction complète) = {p_full}, écart type de difficulté du monde (logit) = {sigma_u}")
    n_sim = 4000
    W_grille = [20, 40, 60, 80, 120]
    configs = [(12, 0.05), (12, 0.15), (24, 0.05), (24, 0.15)]
    cellules = ss_b.spawn(len(configs) * len(W_grille) * 3)
    k = 0
    z_sup, z_eq = 2.394, 1.645  # 1 - 0.05/3/2 ; 1 - 0.05
    logit = lambda p: np.log(p / (1 - p))
    expit = lambda x: 1 / (1 + np.exp(-x))

    def tirer(rng, p_moy_logit, u, K, rho):
        p = expit(p_moy_logit + u)
        q = rng.beta(p * (1 - rho) / rho, (1 - p) * (1 - rho) / rho)
        return rng.binomial(K, q)

    for K, rho in configs:
        print(f"K = {K} structures par monde, corrélation intra-course rho = {rho}")
        print("  W     puissance(R=1,25)  puissance(R=1,5)  équivalence tenue si R=1 (bornes ±20 %)")
        for W in W_grille:
            res = []
            for R in (1.25, 1.5, 1.0):
                rng = np.random.default_rng(cellules[k]); k += 1
                u = rng.normal(0, sigma_u, (n_sim, W))
                d_full = tirer(rng, logit(p_full), u, K, rho)
                d_sep = tirer(rng, logit(min(0.95, p_full * R)), u, K, rho)
                diff = d_sep - d_full
                m = diff.mean(axis=1)
                se = diff.std(axis=1, ddof=1) / math.sqrt(W)
                nu = W - 1
                if R != 1.0:
                    res.append(np.mean(np.abs(m / se) > q_t(z_sup, nu)))
                else:
                    marge = 0.20 * d_full.mean(axis=1)
                    res.append(np.mean(((m + marge) / se > q_t(z_eq, nu)) & ((m - marge) / se < -q_t(z_eq, nu))))
            print(f"  {W:<5d} {res[0]:6.3f}             {res[1]:6.3f}            {res[2]:6.3f}")
    print()


def partie_c():
    print("=== C. Structures composites : percolation contre voisins directs (N = 16) ===")
    N, Kc, h, eps = 16, 4, 0.7, 0.02  # posés
    print(f"posés : h = {h} (prise quand les deux moitiés se rencontrent), eps = {eps} (devinette), "
          f"{Kc} composites par course")
    cel = ss_c.spawn(3)
    # C1 : précision de f sur des chaînes de L sauts, L = 1..4, n essais par longueur
    rng = np.random.default_rng(cel[0])
    grille_h = np.linspace(0.02, 0.99, 98)
    grille_f = np.linspace(0.02, 1.0, 99)
    Hh, Ff = np.meshgrid(grille_h, grille_f, indexing="ij")
    Ls = np.arange(1, 5)
    rL = Hh[:, :, None] * Ff[:, :, None] ** (Ls[None, None, :] - 1)
    lr1, lr0 = np.log(rL), np.log1p(-np.minimum(rL, 1 - 1e-12))
    print("C1. Fidélité de relais mesurée sur chaînes (L = 1 à 4 sauts) : écart type de f estimé")
    print("  f_vrai  n/longueur  moyenne(f_est)  écart type(f_est)")
    for f in (0.8, 0.6):
        for n in (25, 50, 100):
            est = []
            for _ in range(1000):
                y = rng.binomial(n, h * f ** (Ls - 1))
                ll = (y * lr1 + (n - y) * lr0).sum(axis=2)
                i, j = np.unravel_index(np.argmax(ll), ll.shape)
                est.append(grille_f[j])
            print(f"  {f:<6.1f}  {n:<10d}  {np.mean(est):6.3f}          {np.std(est):6.3f}")
    # C2 : courbes de dose prédites
    rng = np.random.default_rng(cel[1])
    doses = [0.5, 1.0, 2.0, 4.0]
    print("C2. Recouvrement attendu d'une composite selon la dose c (degré moyen), N = 16 :")
    print("  c     perco f=1,0  perco f=0,8  perco f=0,6 | direct f=0,8")
    courbes = {}
    B = 20000
    for c in doses:
        ligne = []
        for f in (1.0, 0.8, 0.6):
            adj = tirer_graphes(rng, B, N, min(1.0, c * f / (N - 1)))
            lab = composantes(adj)
            meet = (lab[:, 0] == lab[:, 1]).mean()
            courbes[("perco", c, f)] = eps + (h - eps) * meet
            courbes[("direct", c, f)] = eps + (h - eps) * min(1.0, c * f / (N - 1))
            ligne.append(courbes[("perco", c, f)])
        print(f"  {c:<5.1f} {ligne[0]:8.3f}     {ligne[1]:8.3f}     {ligne[2]:8.3f}   | {courbes[('direct', c, 0.8)]:8.3f}")
    # C3 : discrimination
    rng = np.random.default_rng(cel[2])
    print("C3. Justesse du choix entre les deux courbes (vraisemblance, aucun paramètre libre), f = 0,8 :")
    print("  M courses/dose  vrai = percolation  vrai = voisins directs")
    f = 0.8
    for M in (3, 5, 10):
        acc = []
        for vrai in ("perco", "direct"):
            bon = 0
            for _ in range(2000):
                ll_p = ll_d = 0.0
                for c in doses:
                    n = M * Kc
                    x = rng.binomial(n, courbes[(vrai, c, f)])
                    for mod in ("perco", "direct"):
                        q = courbes[(mod, c, f)]
                        v = x * math.log(q) + (n - x) * math.log(1 - q)
                        if mod == "perco":
                            ll_p += v
                        else:
                            ll_d += v
                bon += (ll_p > ll_d) if vrai == "perco" else (ll_d > ll_p)
            acc.append(bon / 2000)
        print(f"  {M:<15d} {acc[0]:6.3f}              {acc[1]:6.3f}")
    print()


def partie_d():
    print("=== D. Test d'observation : taille d'effet décelable (différences de différences) ===")
    T_pre, T_post = 6, 6
    n_sim = 3000
    cellules = ss_d.spawn(6)
    k = 0
    print("posés : erreurs autorégressives d'ordre 1 sur le log du taux de naissances par article")
    print("F_traités=F_témoins  sigma  rho   écart type de l'estimateur   effet décelable (80 %, 0,05)")
    for F in (50, 100, 200):
        for sigma, rho in ((0.35, 0.5), (0.5, 0.5)):
            rng = np.random.default_rng(cellules[k]); k += 1
            T = T_pre + T_post
            e = np.zeros((n_sim, 2 * F, T))
            e[:, :, 0] = rng.normal(0, sigma, (n_sim, 2 * F))
            for t in range(1, T):
                e[:, :, t] = rho * e[:, :, t - 1] + rng.normal(0, sigma * math.sqrt(1 - rho**2), (n_sim, 2 * F))
            delta = e[:, :, T_pre:].mean(axis=2) - e[:, :, :T_pre].mean(axis=2)
            est = delta[:, :F].mean(axis=1) - delta[:, F:].mean(axis=1)
            se = est.std()
            mde = 2.80 * se
            print(f"{F:<20d} {sigma:<5.2f}  {rho:<4.1f}  {se:8.4f}                      "
                  f"{mde:6.3f} (soit {100*(math.exp(mde)-1):4.1f} % sur le taux)")
    print()


def partie_e():
    print("=== E. Jetons et coût de l'essai dans l'organisme (aucune dépense engagée) ===")
    N, R = 16, 4
    vue, sortie, pensee, memoire = 1500, 500, 2000, 750  # jetons par tour, posés
    bras = {"séparés": 0, "séparés puis confrontés": None, "interaction complète": N - 1,
            "partielle c=0,5": 0.5, "partielle c=1": 1.0, "partielle c=2": 2.0,
            "partielle c=2 sans relais": 2.0}
    tarifs = {"Neon (3/15)": (3.0, 15.0), "Carbon prudent (4/20)": (4.0, 20.0),
              "Carbon jusqu'au 30 novembre (2/10)": (2.0, 10.0)}
    cout = {}
    print("bras                           entrée/course   sortie/course   (jetons, N = 16, 4 tours)")
    for nom, d in bras.items():
        if d is None:
            ent = N * (R // 2) * (vue + memoire) + N * (R - R // 2) * (vue + memoire + (N - 1) * sortie)
        else:
            ent = N * R * (vue + memoire + d * sortie)
        sor = N * R * (sortie + pensee)
        ent, sor = int(round(ent)), int(round(sor))
        cout[nom] = (ent, sor)
        print(f"{nom:<30s} {ent:>12,d}   {sor:>12,d}".replace(",", " "))
    print("budget égal : chaque bras reçoit le coût du bras le plus cher (les autres convertissent le reste en tours)")
    for nom_t, (pi, po) in tarifs.items():
        par_course = max(e * pi / 1e6 + s * po / 1e6 for e, s in cout.values())
        print(f"{nom_t:<36s} par course = {par_course:5.2f} USD ; par monde (7 bras) = {7*par_course:6.2f} ; "
              f"20 mondes = {20*7*par_course:6.0f} ; 60 mondes = {60*7*par_course:6.0f} ; 120 mondes = {120*7*par_course:6.0f}")
    e_max = max(v[0] for v in cout.values()); s_max = max(v[1] for v in cout.values())
    for W in (60, 120):
        s_tot = W * 7 * s_max; e_tot = W * 7 * e_max
        print(f"Voie carte graphique, {W} mondes x 7 bras : entrée {e_tot/1e6:5.1f} M, sortie {s_tot/1e6:5.1f} M jetons ; "
              f"à 1 000 puis 3 000 jetons de sortie/s (posé) : {s_tot/1000/3600:5.1f} h puis {s_tot/3000/3600:5.1f} h ; "
              f"à 1,19 USD/h : {1.19*s_tot/1000/3600:5.1f} puis {1.19*s_tot/3000/3600:5.1f} USD, hors pré-remplissage et mise en place")
    # Plan réduit : contraste principal à N = 8 (trois bras), dose à N = 16 (quatre doses, 5 courses), chaînes.
    print("Plan réduit, aux tarifs de Neon (3/15) :")
    def course(Nn, d):
        ent = Nn * R * (vue + memoire + d * sortie)
        sor = Nn * R * (sortie + pensee)
        return ent * 3.0 / 1e6 + sor * 15.0 / 1e6
    c8 = course(8, 7)
    for W in (60, 120):
        print(f"  contraste principal, N = 8, 3 bras au budget égal, {W} mondes : {c8:4.2f} USD par course, "
              f"{3*W*c8:6.0f} USD")
    c16 = max(course(16, d) for d in (0.5, 1.0, 2.0, 4.0))
    print(f"  dose, N = 16, 4 doses x 5 courses : {c16:4.2f} USD par course, {20*c16:5.0f} USD")
    essai_chaine = sum((L + 1) * (vue * 3.0 / 1e6 + (sortie + pensee) * 15.0 / 1e6) for L in range(1, 5)) / 4
    print(f"  chaînes de relais, 4 longueurs x 50 essais : {essai_chaine:5.3f} USD par essai, {200*essai_chaine:5.0f} USD")
    print()


if __name__ == "__main__":
    partie_a()
    partie_b()
    partie_c()
    partie_d()
    partie_e()
