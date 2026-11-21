"""Calcul de la règle « moniteur invalide » — re-dérivation indépendante, version 1.

Ce programme rejoue les valeurs numériques de la note
rederivation-opus-v1.md (même dossier). Il ne lit aucune donnée d'expérience :
tout est calculé à partir des paramètres de l'énoncé.

Contenu :
  1. seuils de non-détection (taux au-dessous duquel la richesse décroît) ;
  2. borne garantie de l'excès d'épisodes « endommagés et non signalés »
     au-delà de rho0 * n (garantie 2, inégalité de Freedman, horizon n fixé) ;
  3. borne inférieure valable pour TOUTE règle de niveau alpha (Pinsker) ;
  4. excès atteint par un attaquant à taux constant (simulation, quantile 1 - beta,
     maximum sur une grille de taux) : minorant du pire cas ;
  5. nombre médian d'audits avant l'annonce quand le taux réel vaut 2 rho0.

Graines : numpy.random.SeedSequence, une sous-graine par tâche (règle R9).
Lancer : python calcul_regle_moniteur_invalide_v1.py > sortie_calcul_regle_moniteur_invalide_v1.txt
"""

import math
import sys

import numpy as np
from scipy import stats

RHO0 = 0.10
ALPHA = 0.05
BETA = 0.10
QS = (0.20, 0.05)
NS = (1000, 4000, 16000)
GRAINE_RACINE = 20261121

# Grilles de taux alternatifs (multiples de rho0).
GRILLES = {
    # lecture principale de l'énoncé : {1,25 ; 1,50 ; ... ; 5,00} x rho0, pas 0,25, K = 16
    "arith16": np.arange(1.25, 5.0001, 0.25) * RHO0,
    # variante géométrique : 1,25 x 2^(j/2), j = 0..4, K = 5
    "geom5": 1.25 * 2.0 ** (np.arange(5) / 2.0) * RHO0,
    # correctif : grille qui descend vers rho0, rho0 * (1 + 4 * 2^-j), j = 0..11, K = 12
    "descendante12": RHO0 * (1.0 + 4.0 * 2.0 ** -np.arange(12)),
}


def coefficients(rho, rho0=RHO0):
    """a = log((rho(1-rho0))/(rho0(1-rho))), b = log((1-rho0)/(1-rho)), u = a - b = log(rho/rho0)."""
    rho = np.asarray(rho, dtype=float)
    b = np.log((1 - rho0) / (1 - rho))
    u = np.log(rho / rho0)
    return u + b, b, u


def seuil_non_detection(rho, rho0=RHO0):
    """Taux r* = b/a : sous r*, la croissance logarithmique espérée par audit est négative."""
    a, b, _ = coefficients(rho, rho0)
    return b / a


def exposant_lundberg(r, rho):
    """theta dans (0, 1) tel que E_r[l_rho(X)^theta] = 1 (taux réel r entre rho0 et r*(rho)).

    W^theta est alors une martingale sous r, donc P(annonce un jour) <= alpha^theta (Ville).
    """
    from scipy.optimize import brentq
    f = lambda th: r * (rho / RHO0) ** th + (1 - r) * ((1 - rho) / (1 - RHO0)) ** th - 1
    return brentq(f, 1e-9, 1 - 1e-12) if f(1 - 1e-12) > 0 else float("nan")


def ecart_freedman(n, q, b, u, ell):
    """Écart x tel que P(exists m <= n : sum (q - A_t) c_t >= x) <= exp(-ell).

    Accroissements (q - A_t) c_t, c_t dans {-b, u}, majorés par R = max((1-q) b, q u),
    variance conditionnelle sommée majorée par v = n q (1-q) max(u^2, b^2).
    Forme de Bernstein de l'inégalité de Freedman : exp(-x^2 / (2 (v + R x / 3))).
    """
    R = max((1 - q) * b, q * u)
    v = n * q * (1 - q) * max(u * u, b * b)
    return R * ell / 3 + math.sqrt((R * ell / 3) ** 2 + 2 * v * ell)


def borne_garantie(n, q, grille, regle):
    """Borne B(n) de la garantie 2, sans le +1 de l'épisode d'annonce.

    regle = "melange" (moyenne des produits) : min sur k de
        (b_k/a_k - rho0) n + (log(K/alpha) + x_k) / (q a_k)
    regle = "produit" (produit des moyennes) : même forme avec rho_barre = moyenne de la grille,
        L = log(1/alpha).
    Le k retenu est fixé d'avance par (n, q) : pas d'union sur k, ell = log(1/beta).
    """
    ell = math.log(1 / BETA)
    if regle == "produit":
        rhos = np.array([np.mean(grille)])
        L = math.log(1 / ALPHA)
    else:
        rhos = np.asarray(grille)
        L = math.log(len(grille) / ALPHA)
    meilleur = None
    for rho in rhos:
        a, b, u = (float(z) for z in coefficients(rho))
        x = ecart_freedman(n, q, b, u, ell)
        lineaire = (b / a - RHO0) * n
        racine = (L + x) / (q * a)
        total = lineaire + racine
        if meilleur is None or total < meilleur[0]:
            meilleur = (total, rho, lineaire, racine)
    return meilleur


def phi(s, q):
    """phi(s) = log E[exp(-s (A - q))], A ~ Bernoulli(q) : fonction génératrice exacte du tirage d'audit."""
    return s * q + math.log(1 - q + q * math.exp(-s))


def borne_chernoff(n, q, grille, regle, lambdas=np.geomspace(1e-3, 3.0, 400)):
    """Borne B(n) de la garantie 2 par la martingale exponentielle exacte du tirage d'audit.

    Pour (rho_k, lambda) fixés d'avance, avec probabilité >= 1 - beta, pour TOUT m sans annonce :
        T_m - rho0 m < (L + ell/lambda) / A + m (C/A - rho0),
        A = q a - (phi(lambda u) - phi(-lambda b)) / lambda,   C = q b + phi(-lambda b) / lambda.
    On retient le couple (rho_k, lambda) qui minimise la borne à m = n (choix déterministe).
    """
    ell = math.log(1 / BETA)
    if regle == "produit":
        rhos = np.array([np.mean(grille)])
        L = math.log(1 / ALPHA)
    else:
        rhos = np.asarray(grille)
        L = math.log(len(grille) / ALPHA)
    meilleur = None
    for rho in rhos:
        a, b, u = (float(z) for z in coefficients(rho))
        for lam in lambdas:
            A = q * a - (phi(lam * u, q) - phi(-lam * b, q)) / lam
            if A <= 0:
                continue
            C = q * b + phi(-lam * b, q) / lam
            pente = C / A - RHO0
            const = (L + ell / lam) / A
            total = const + n * pente
            if meilleur is None or total < meilleur[0]:
                meilleur = (total, rho, lam, const, pente)
    return meilleur


def ordre_principal(n, q, K):
    """Ordre principal heuristique : sqrt(2 rho0 n / q) (sqrt((1-rho0) log(K/alpha)) + sqrt((1-q) log(1/beta)))."""
    return math.sqrt(2 * RHO0 * n / q) * (math.sqrt((1 - RHO0) * math.log(K / ALPHA))
                                          + math.sqrt((1 - q) * math.log(1 / BETA)))


def kl_bernoulli(p, p0):
    return p * math.log(p / p0) + (1 - p) * math.log((1 - p) / (1 - p0))


def borne_inferieure_toute_regle(n, q, gamma=0.05):
    """Excès qu'un attaquant i.i.d. au taux rho0 + delta atteint avec probabilité >= beta
    contre TOUTE règle de niveau alpha (qui n'observe que les audits).

    P_alt(annonce avant n) <= alpha + VT, VT <= sqrt(KL/2), KL = q n kl(rho0+delta || rho0)
    (les épisodes non audités ont la même loi sous les deux hypothèses : seule l'issue des
    audits informe). Avec probabilité >= 1 - alpha - VT - gamma : pas d'annonce et
    T_n >= quantile_gamma(Bin(n, rho0+delta)). On exige 1 - alpha - VT - gamma >= beta.
    """
    vt_max = 1 - ALPHA - BETA - gamma
    kl_max = 2 * vt_max ** 2
    meilleur = 0.0
    for delta in np.linspace(1e-4, 5.0 * RHO0, 20000):
        if RHO0 + delta >= 1:
            break
        r = RHO0 + delta
        if q * n * kl_bernoulli(r, RHO0) > kl_max:
            break
        exces = stats.binom.ppf(gamma, n, r) - RHO0 * n
        meilleur = max(meilleur, exces)
    return meilleur


def log_richesse(M, N, grille, regle):
    """Log-richesse à partir des comptes cumulés M (audits endommagés non signalés) et N (audits)."""
    if regle == "produit":
        a, b, _ = coefficients(np.mean(grille))
        return M * a - N * b
    a, b, _ = coefficients(grille)
    lw = None
    for ak, bk in zip(a, b):
        terme = M * ak - N * bk
        lw = terme if lw is None else np.logaddexp(lw, terme)
    return lw - math.log(len(grille))


def exces_attaquant_constant(n, q, grille, regle, taux, rng, R=1000, bloc=250):
    """Quantile 1 - beta de l'excès accumulé avant l'annonce (ou jusqu'à n), attaquant i.i.d. au taux donné."""
    seuil = math.log(1 / ALPHA)
    exces = []
    sans_annonce = []
    for _ in range(R // bloc):
        A = rng.random((bloc, n)) < q
        X = rng.random((bloc, n)) < taux
        M = np.cumsum(A & X, axis=1, dtype=np.int32)
        N = np.cumsum(A, axis=1, dtype=np.int32)
        T = np.cumsum(X, axis=1, dtype=np.int32)
        lw = log_richesse(M, N, grille, regle)
        franchi = lw >= seuil
        a_franchi = franchi.any(axis=1)
        tau = np.where(a_franchi, franchi.argmax(axis=1), n)  # indice 0 de l'épisode d'annonce
        # épisodes strictement avant l'annonce : indices 0..tau-1, soit m = tau épisodes
        m = tau
        T_avant = np.where(m > 0, T[np.arange(bloc), np.maximum(m - 1, 0)], 0)
        exces.append(T_avant - RHO0 * m)
        sans_annonce.append(~a_franchi)
    exces = np.concatenate(exces)
    return float(np.quantile(exces, 1 - BETA)), float(np.mean(np.concatenate(sans_annonce)))


def audits_avant_annonce(grille, regle, taux, rng, R=4000, plafond=20000):
    X = rng.random((R, plafond)) < taux
    M = np.cumsum(X, axis=1, dtype=np.int32)
    N = np.arange(1, plafond + 1, dtype=np.int32)[None, :]
    lw = log_richesse(M, N, grille, regle)
    franchi = lw >= math.log(1 / ALPHA)
    a_franchi = franchi.any(axis=1)
    j = np.where(a_franchi, franchi.argmax(axis=1) + 1, plafond + 1).astype(float)
    return float(np.median(j)), float(np.quantile(j, 0.9)), float(np.mean(~a_franchi))


def main():
    ss = np.random.SeedSequence(GRAINE_RACINE)
    print("# Règle « moniteur invalide » — sortie du calcul, version 1")
    print(f"python {sys.version.split()[0]}, numpy {np.__version__}, scipy {__import__('scipy').__version__}")
    print(f"rho0 = {RHO0}, alpha = {ALPHA}, beta = {BETA}, graine racine = {GRAINE_RACINE}")
    print()

    print("## 1. Grilles, taux moyen et seuils de non-détection")
    for nom, g in GRILLES.items():
        rbar = float(np.mean(g))
        print(f"{nom}: K = {len(g)}, rho_k/rho0 = {np.round(g / RHO0, 4).tolist()}")
        print(f"   produit des moyennes = rapport unique au taux moyen rho_barre = {rbar:.5f} "
              f"({rbar / RHO0:.4f} rho0) ; seuil de non-détection r* = {seuil_non_detection(rbar):.5f} "
              f"({seuil_non_detection(rbar) / RHO0:.4f} rho0)")
        print(f"   moyenne des produits : seuil de non-détection du plus petit taux r*_1 = "
              f"{seuil_non_detection(g.min()):.5f} ({seuil_non_detection(g.min()) / RHO0:.4f} rho0)")
    print()

    print("## 1b. Produit des moyennes (arith16) : attaquant au taux constant r sous le seuil de non-détection")
    print("r / rho0 | theta de Lundberg | P(jamais annoncé) >= 1 - alpha^theta")
    rbar = float(np.mean(GRILLES["arith16"]))
    for rr in (1.2, 1.5, 1.7, 1.8, 1.9):
        th = exposant_lundberg(rr * RHO0, rbar)
        print(f"{rr:.2f} | {th:.4f} | {1 - ALPHA ** th:.4f}")
    print()

    print("## 2a. Borne garantie (martingale exponentielle exacte, Ville) de l'excès T_m - rho0 m,")
    print("pour tout m < annonce, m <= n, avec probabilité >= 1 - beta ; ajouter 1 pour l'épisode d'annonce")
    print("grille | règle | q | n | borne | constante | pente | rho_k retenu / rho0 | lambda | ordre principal")
    for nom in ("arith16", "geom5", "descendante12"):
        g = GRILLES[nom]
        for regle in ("produit", "melange"):
            if nom == "descendante12" and regle == "produit":
                continue
            for q in QS:
                for n in NS:
                    tot, rho, lam, const, pente = borne_chernoff(n, q, g, regle)
                    op = ordre_principal(n, q, len(g) if regle == "melange" else 1)
                    print(f"{nom} | {regle} | {q:.2f} | {n} | {tot:.1f} | {const:.1f} | {pente:.5f} | "
                          f"{rho / RHO0:.4f} | {lam:.4f} | {op:.1f}")
    print()

    print("## 2b. Croissance : borne / n et borne / sqrt(n) pour des horizons longs (borne 2a)")
    print("grille | règle | q | n | borne | borne/n | borne/sqrt(n)")
    for nom, regle in (("arith16", "produit"), ("arith16", "melange"), ("descendante12", "melange")):
        for q in QS:
            for n in (1000, 16000, 100000, 1000000, 10000000):
                tot = borne_chernoff(n, q, GRILLES[nom], regle)[0]
                print(f"{nom} | {regle} | {q:.2f} | {n} | {tot:.1f} | {tot / n:.5f} | {tot / math.sqrt(n):.3f}")
    print()

    print("## 2c. Forme fermée plus lâche (inégalité de Freedman, variance au pire n q (1-q) max(u^2, b^2))")
    print("grille | règle | q | n | borne | part linéaire | part en racine | rho_k retenu / rho0 | borne / n")
    for nom in ("arith16", "geom5", "descendante12"):
        g = GRILLES[nom]
        for regle in ("produit", "melange"):
            if nom == "descendante12" and regle == "produit":
                continue
            for q in QS:
                for n in NS:
                    tot, rho, lin, rac = borne_garantie(n, q, g, regle)
                    print(f"{nom} | {regle} | {q:.2f} | {n} | {tot:.1f} | {lin:.1f} | {rac:.1f} | "
                          f"{rho / RHO0:.4f} | {tot / n:.4f}")
    print()

    print("## 3. Borne inférieure pour TOUTE règle de niveau alpha (attaquant i.i.d., Pinsker, gamma = 0,05)")
    print("q | n | excès atteignable avec probabilité >= beta | rapport à sqrt(n rho0 (1-rho0) / q)")
    for q in QS:
        for n in NS:
            lb = borne_inferieure_toute_regle(n, q)
            echelle = math.sqrt(n * RHO0 * (1 - RHO0) / q)
            print(f"{q:.2f} | {n} | {lb:.1f} | {lb / echelle:.3f}")
    print()

    print("## 4. Excès atteint par un attaquant à taux constant (simulation, quantile 1 - beta, R = 1000)")
    print("Minorant du pire cas ; maximum sur des taux r = rho0 (1 + j/20).")
    print("grille | règle | q | n | excès atteint | taux qui l'atteint / rho0 | part sans annonce à n pour ce taux")
    enfants = iter(ss.spawn(200))
    for nom, regle in (("arith16", "produit"), ("arith16", "melange"), ("descendante12", "melange")):
        g = GRILLES[nom]
        for q in QS:
            for n in NS:
                rng = np.random.default_rng(next(enfants))
                meilleur = (-1e9, None, None)
                for j in range(1, 25):
                    taux = RHO0 * (1 + j / 20)
                    e, libre = exces_attaquant_constant(n, q, g, regle, taux, rng)
                    if e > meilleur[0]:
                        meilleur = (e, taux, libre)
                print(f"{nom} | {regle} | {q:.2f} | {n} | {meilleur[0]:.1f} | {meilleur[1] / RHO0:.2f} | "
                      f"{meilleur[2]:.3f}", flush=True)
    print()

    print("## 5. Audits avant l'annonce quand le taux réel vaut 2 rho0 (R = 4000, plafond 20000 audits)")
    print("grille | règle | médiane des audits | quantile 0,9 | part sans annonce au plafond | "
          "épisodes médians q=0,20 | q=0,05")
    for nom, regle in (("arith16", "produit"), ("arith16", "melange"), ("geom5", "produit"),
                       ("geom5", "melange"), ("descendante12", "melange")):
        rng = np.random.default_rng(next(enfants))
        med, q90, jamais = audits_avant_annonce(GRILLES[nom], regle, 2 * RHO0, rng)
        print(f"{nom} | {regle} | {med:.0f} | {q90:.0f} | {jamais:.4f} | {med / 0.20:.0f} | {med / 0.05:.0f}")


if __name__ == "__main__":
    main()
