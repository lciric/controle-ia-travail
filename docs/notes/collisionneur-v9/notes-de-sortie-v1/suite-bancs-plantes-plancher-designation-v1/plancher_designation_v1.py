"""Calculs et simulation sur processeur, sans dépense, pour deux questions de Lazar (bancs à dommages plantés).

Q1 : le plancher de détection change-t-il le seuil choisi par l'étalonnage, ou seulement l'admission ?
     Combien de dommages plantés par strate pour vérifier un plancher 0,5 à 0,7 (Clopper-Pearson exact) ?
Q3 : sensibilité de la détection mesurée à l'erreur de désignation (programme ou repéreur).

Modèle (illustratif, déclaré) : un document porte m contrôles attendus, tous présents chez l'honnête.
Un lecteur lit chaque contrôle ; il lit « absent » un contrôle présent avec probabilité eps (manque),
et « présent » un contrôle absent avec probabilité eta. Paire nulle : original honnête contre le même
document retouché sans perte ; pour un contrôle intouché, la lecture des deux versions est identique avec
probabilité rho (lecture partagée), sinon indépendante. Dommage : un contrôle retiré.
Écart E = (manques lus dans la version retouchée ou endommagée) - (manques lus chez l'honnête), en contrôles.
Règle : signalé si E >= t (t entier ; t = 1 est la règle fixe « 1/m »).
Hétérogénéité : eps par document tiré d'une loi bêta de moyenne eps et de concentration kappa (grappes).
Graines : numpy.random.SeedSequence(20261124), dérivées par tâche (R9).
"""
import functools
import math
import numpy as np

SS = np.random.SeedSequence(20261124)
GRAINES = SS.spawn(8)


# ---------- binomiale exacte et Clopper-Pearson (sans scipy) ----------
def queue_sup(x, n, p):
    """P(X >= x), X ~ Bin(n, p)."""
    if x <= 0:
        return 1.0
    if p <= 0:
        return 0.0
    if p >= 1:
        return 1.0
    return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(x, n + 1))


@functools.lru_cache(maxsize=None)
def cp_inf(x, n, alpha):
    """Borne inférieure unilatérale exacte de Clopper-Pearson au niveau alpha (x succès sur n)."""
    if x == 0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if queue_sup(x, n, mid) < alpha:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cp_sup(x, n, alpha):
    """Borne supérieure unilatérale exacte (x événements sur n)."""
    return 1 - cp_inf(n - x, n, alpha)


def x_min_pour_plancher(n, f, alpha):
    """Plus petit nombre de détections x sur n tel que la borne inférieure CP dépasse f."""
    for x in range(n + 1):
        if cp_inf(x, n, alpha) >= f:
            return x
    return None


def puissance_plancher(n, d, f, alpha):
    """P(borne inférieure CP >= f) quand la détection vraie vaut d."""
    x0 = x_min_pour_plancher(n, f, alpha)
    return 0.0 if x0 is None else queue_sup(x0, n, d)


def n_pour_plancher(d, f, alpha, puissance=0.8, nmax=2000):
    for n in range(1, nmax + 1):
        if puissance_plancher(n, d, f, alpha) >= puissance:
            return n
    return None


# ---------- lois exactes de l'écart (eps homogène) ----------
def loi_contribution_intouche(eps, rho):
    p = (1 - rho) * eps * (1 - eps)
    return {-1: p, 0: 1 - 2 * p, 1: p}


def loi_contribution_retire(eps, eta):
    # honnête : absent lu avec prob eps ; endommagé : absent lu avec prob 1 - eta ; lectures indépendantes
    a_h, a_d = eps, 1 - eta
    return {1: a_d * (1 - a_h), 0: a_d * a_h + (1 - a_d) * (1 - a_h), -1: (1 - a_d) * a_h}


def convoluer(l1, l2):
    out = {}
    for a, pa in l1.items():
        for b, pb in l2.items():
            out[a + b] = out.get(a + b, 0.0) + pa * pb
    return out


def loi_ecart(m, eps, rho, eta=None, retire=0):
    loi = {0: 1.0}
    for _ in range(m - retire):
        loi = convoluer(loi, loi_contribution_intouche(eps, rho))
    for _ in range(retire):
        loi = convoluer(loi, loi_contribution_retire(eps, eta))
    return loi


def queue(loi, t):
    return sum(p for e, p in loi.items() if e >= t)


# ---------- simulation avec hétérogénéité par document ----------
def tirer_ecarts(rng, n, m, eps, kappa, rho, eta, retire, eps_desig=0.0):
    """Écarts simulés. eps_desig : probabilité qu'un dommage « planté » n'ait en fait rien retiré
    (erreur de désignation : le tiers croit avoir retiré un contrôle, il est resté)."""
    if kappa is None:
        e = np.full(n, eps)
    else:
        e = rng.beta(eps * kappa, (1 - eps) * kappa, size=n)
    out = np.zeros(n, dtype=int)
    k_intouches = m - retire
    # contrôles intouchés
    hon = rng.random((n, k_intouches)) < e[:, None]
    partage = rng.random((n, k_intouches)) < rho
    ret_indep = rng.random((n, k_intouches)) < e[:, None]
    ret = np.where(partage, hon, ret_indep)
    out += ret.sum(1) - hon.sum(1)
    if retire:
        rate = rng.random(n) < eps_desig  # désignation fausse : le contrôle est resté
        h = rng.random(n) < e
        # si vraiment retiré : absent lu avec prob 1-eta ; si resté : comme un intouché (lecture partagée ou non)
        d_vrai = rng.random(n) >= eta
        d_reste = np.where(rng.random(n) < rho, h, rng.random(n) < e)
        d = np.where(rate, d_reste, d_vrai)
        out += d.astype(int) - h.astype(int)
    return out


def t_min_admissible(ecarts_nuls, alpha_fa, cible, tmax=6):
    n0 = len(ecarts_nuls)
    for t in range(1, tmax + 1):
        x = int((ecarts_nuls >= t).sum())
        if cp_sup(x, n0, alpha_fa) <= cible:
            return t
    return None


def main():
    print("=" * 100)
    print("A. Clopper-Pearson : dommages plantés par strate pour établir « détection >= f »")
    print("=" * 100)
    print("A1. Tout détecté (zéro manque) : n minimal pour borne inférieure >= f")
    for alpha in (0.05, 0.025, 0.005):
        ligne = []
        for f in (0.5, 0.6, 0.7, 0.9):
            n = next(n for n in range(1, 500) if cp_inf(n, n, alpha) >= f)
            ligne.append(f"f={f}: n={n}")
        print(f"  alpha={alpha:<6}", " ; ".join(ligne))
    print("A2. Puissance 80 % : n par strate selon la détection vraie d (borne inférieure unilatérale)")
    for alpha, nom in ((0.05, "une strate, 5 %"), (0.025, "deux strates Bonferroni, 2,5 %"), (0.005, "dix strates, 0,5 %")):
        print(f"  {nom}")
        for f in (0.5, 0.6, 0.7):
            cases = []
            for d in (f + 0.1, f + 0.2, 0.95):
                if d >= 1:
                    continue
                n = n_pour_plancher(round(d, 3), f, alpha)
                cases.append(f"d={d:.2f}: n={n}")
            print(f"    f={f}: " + " ; ".join(cases))
    print("A3. Même chose, puissance 90 %, alpha 5 %")
    for f in (0.5, 0.7):
        print(f"    f={f}: " + " ; ".join(f"d={d:.2f}: n={n_pour_plancher(d, f, 0.05, 0.9)}" for d in (f + 0.1, f + 0.2)))
    print("A4. Fausse alerte : n paires nulles pour borne supérieure <= cible, à x fausses alertes observées")
    for cible in (0.05, 0.10):
        r = []
        for x in (0, 1, 2, 3):
            n = next(n for n in range(x + 1, 3000) if cp_sup(x, n, 0.05) <= cible)
            r.append(f"x={x}: n={n}")
        print(f"  cible {cible}: " + " ; ".join(r))

    print()
    print("=" * 100)
    print("B. Lois exactes (eps homogène) : fausse alerte FA(t) et détection D(t) d'un contrôle retiré")
    print("   eta = 0,05 (contrôle absent lu présent) ; t en contrôles ; règle fixe = t 1")
    print("=" * 100)
    eta = 0.05
    print(f"{'m':>2} {'eps':>5} {'rho':>4} | {'FA(1)':>6} {'FA(2)':>6} {'FA(3)':>6} | {'D(1)':>6} {'D(2)':>6} {'D(3)':>6} | monotone")
    for m in (5, 6):
        for eps in (0.02, 0.05, 0.10, 0.20):
            for rho in (0.0, 0.5, 0.9):
                l0 = loi_ecart(m, eps, rho)
                l1 = loi_ecart(m, eps, rho, eta=eta, retire=1)
                fa = [queue(l0, t) for t in (1, 2, 3)]
                de = [queue(l1, t) for t in (1, 2, 3)]
                mono = all(de[i] >= de[i + 1] for i in range(2)) and all(fa[i] >= fa[i + 1] for i in range(2))
                print(f"{m:>2} {eps:>5} {rho:>4} | " + " ".join(f"{v:6.3f}" for v in fa) + " | "
                      + " ".join(f"{v:6.3f}" for v in de) + f" | {mono}")

    print()
    print("=" * 100)
    print("C. Étalonnage simulé sur paires nulles (hétérogénéité kappa=20), puis détection au seuil choisi")
    print("   t choisi = plus petit t dont la borne CP supérieure (5 %) de fausse alerte <= cible 0,05 ;")
    print("   « plancher » : D(t choisi) >= 0,5 ou 0,7 ? ; 2000 répétitions de l'étalonnage par case")
    print("=" * 100)
    rng = np.random.default_rng(GRAINES[0])
    print(f"{'m':>2} {'eps':>5} {'rho':>4} {'n0':>4} | P(t=1) P(t=2) P(t>=3|aucun) | D moyen au t choisi | P(D>=0,5) P(D>=0,7) | D(t=1) D(t=2)")
    for m in (5, 6):
        for eps in (0.05, 0.10, 0.20):
            for rho in (0.5, 0.9):
                # détection vraie par t (Monte Carlo grand)
                big = tirer_ecarts(rng, 400_000, m, eps, 20, rho, eta, 1)
                dvrai = {t: float((big >= t).mean()) for t in range(1, 7)}
                for n0 in (59, 120):
                    choix = []
                    for _ in range(2000):
                        nuls = tirer_ecarts(rng, n0, m, eps, 20, rho, eta, 0)
                        choix.append(t_min_admissible(nuls, 0.05, 0.05))
                    choix = np.array([c if c is not None else 99 for c in choix])
                    d_choisi = np.array([dvrai.get(c, 0.0) for c in choix])
                    print(f"{m:>2} {eps:>5} {rho:>4} {n0:>4} | {np.mean(choix == 1):6.3f} {np.mean(choix == 2):6.3f} "
                          f"{np.mean(choix >= 3):6.3f}        | {d_choisi.mean():6.3f}              | "
                          f"{np.mean(d_choisi >= 0.5):6.3f}   {np.mean(d_choisi >= 0.7):6.3f}  | {dvrai[1]:.3f}  {dvrai[2]:.3f}")

    print()
    print("=" * 100)
    print("D. Le plancher change-t-il le seuil ? Cas d'un budget de fausse alerte PARTAGÉ entre deux tranches")
    print("   (m=5 et m=6, poids égaux) : règle « plus petits seuils admissibles » contre « maximin de détection »")
    print("=" * 100)
    for eps, rho in ((0.10, 0.5), (0.20, 0.5), (0.10, 0.0)):
        fa, de = {}, {}
        for m in (5, 6):
            l0 = loi_ecart(m, eps, rho)
            l1 = loi_ecart(m, eps, rho, eta=eta, retire=1)
            fa[m] = {t: queue(l0, t) for t in range(1, 5)}
            de[m] = {t: queue(l1, t) for t in range(1, 5)}
        cible = 0.05
        couples = [(t5, t6) for t5 in range(1, 5) for t6 in range(1, 5)
                   if 0.5 * fa[5][t5] + 0.5 * fa[6][t6] <= cible]
        par_tranche = (min(t for t in range(1, 5) if fa[5][t] <= cible), min(t for t in range(1, 5) if fa[6][t] <= cible))
        maximin = max(couples, key=lambda c: (min(de[5][c[0]], de[6][c[1]]), de[5][c[0]] + de[6][c[1]]))
        moyenne = max(couples, key=lambda c: de[5][c[0]] + de[6][c[1]])
        print(f"eps={eps} rho={rho} : FA m5 {[round(fa[5][t],3) for t in range(1,4)]} m6 {[round(fa[6][t],3) for t in range(1,4)]}")
        print(f"   cible par tranche -> t={par_tranche}, D=({de[5][par_tranche[0]]:.3f}, {de[6][par_tranche[1]]:.3f})")
        print(f"   budget partagé, max de la moyenne -> t={moyenne}, D=({de[5][moyenne[0]]:.3f}, {de[6][moyenne[1]]:.3f})")
        print(f"   budget partagé, maximin           -> t={maximin}, D=({de[5][maximin[0]]:.3f}, {de[6][maximin[1]]:.3f})")

    print()
    print("=" * 100)
    print("E. Désignation (décision 3) : biais de la détection mesurée selon le taux de désignation fausse")
    print("   (dommage compté planté mais contrôle resté) ; m=6, eps=0,10, rho=0,5, eta=0,05, t=1 et t=2")
    print("=" * 100)
    rng = np.random.default_rng(GRAINES[1])
    for t in (1, 2):
        base = None
        r = []
        for e_d in (0.0, 0.05, 0.10, 0.20, 0.30):
            x = tirer_ecarts(rng, 400_000, 6, 0.10, 20, 0.5, eta, 1, eps_desig=e_d)
            d = float((x >= t).mean())
            base = d if base is None else base
            r.append(f"{e_d:.2f}: {d:.3f}")
        print(f"  t={t}: " + " ; ".join(r))
    print("  Forme close : D_mesurée = (1 - e) * D_vraie + e * FA(t). Écart entre deux instruments de taux e1, e2 :")
    print("  |e1 - e2| * (D_vraie - FA). Exemple D=0,8, FA=0,03 : 0,05 d'écart de taux -> 0,038 de détection.")
    print("  Mesure de e par audit : n documents audités, borne exacte ; demi-largeur à 95 % pour e≈0,10 :")
    for n in (50, 100, 200, 400):
        x = round(0.10 * n)
        print(f"    n={n}: e^=0,10, IC CP bilatéral 95 % = [{cp_inf(x, n, 0.025):.3f} ; {cp_sup(x, n, 0.025):.3f}]")


if __name__ == "__main__":
    main()
