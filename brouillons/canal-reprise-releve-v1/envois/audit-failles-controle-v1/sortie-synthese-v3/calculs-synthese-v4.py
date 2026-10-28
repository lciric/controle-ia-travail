# Calculs de la synthese de l'audit, version 4 (v3 de la synthese) : normalisations par la duree sous effet
# episode, avec tau ESTIME sur les episodes honnetes du calibrage (la contre-lecture v2 prenait tau vrai) ;
# multiplicite entre sondes au plancher. Proprietes de detecteurs sous des nuls simplifies, jamais des mesures ;
# aucune donnee des pilotes ; aucune attaque. Graines : SeedSequence (R9), indice d'enfant distinct des versions 2 et 3.
import numpy as np

ss = np.random.SeedSequence(20261026)
enfants = ss.spawn(12)
rng = np.random.default_rng(enfants[10])
N = 100_000
alpha = 0.01


def episodes(T, tau, phi=0.0):
    b = tau * rng.standard_normal((N, 1))
    e = np.empty((N, T))
    e[:, 0] = rng.standard_normal(N)
    for t in range(1, T):
        e[:, t] = phi * e[:, t - 1] + np.sqrt(1 - phi ** 2) * rng.standard_normal(N)
    return b + e


def tau2_estime(X):
    T = X.shape[1]
    moyennes = X.mean(1)
    intra = X.var(1, ddof=1).mean()
    return max(0.0, moyennes.var(ddof=1) - intra / T), intra


def statistiques(X, tau2, s2):
    T = X.shape[1]
    S = np.cumsum(X, 1)
    t = np.arange(1, T + 1, dtype=float)
    return {"rapport": (S / np.sqrt(s2 * t * (1 + np.log(1 + t)))).max(1),
            "variance d'episode": (S / np.sqrt(s2 * t + tau2 * t ** 2)).max(1),
            "combinee": (S / np.sqrt(s2 * t * (1 + np.log(1 + t)) + tau2 * t ** 2)).max(1)}


print("== bloc 1 : taux de faux positifs a alpha = 1 %, calibrage a 10 pas, tau estime sur le calibrage")
for nom, tau, phi in (("independant, tau=0", 0.0, 0.0), ("effet episode tau=0,3", 0.3, 0.0), ("effet episode tau=0,6", 0.6, 0.0),
                      ("effet episode tau=1,0", 1.0, 0.0), ("AR(1) phi=0,3, tau=0", 0.0, 0.3)):
    Xc = episodes(10, tau, phi)
    tau2, s2 = tau2_estime(Xc)
    cal = statistiques(Xc, tau2, s2)
    seuils = {k: np.quantile(v, 1 - alpha) for k, v in cal.items()}
    lignes = {k: [] for k in seuils}
    for Te in (5, 10, 20, 30, 60):
        tst = statistiques(episodes(Te, tau, phi), tau2, s2)
        for k in seuils:
            lignes[k].append(f"T_e={Te} {100 * np.mean(tst[k] > seuils[k]):.2f} %")
    print(f"{nom} (tau estime {np.sqrt(tau2):.3f}) :")
    for k, v in lignes.items():
        print(f"  {k:20s} " + " ; ".join(v))

print("== bloc 2 : multiplicite entre sondes au plancher, regle « au moins une » a 5 % par sonde")
for k in (1, 2, 3, 5):
    print(f"k={k} : 1 - 0,95^k = {1 - 0.95 ** k:.4f} ; Bonferroni par sonde {0.05 / k:.4f}")
