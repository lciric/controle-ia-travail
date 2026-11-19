"""Banc du contre-lecteur (matrices aléatoires seulement : aucun poids, aucune sonde, aucune lentille réelle, aucun code du
paquet contre-lu). Question : le p de concentration du texte scellé, dont les directions nulles sont jugées avec des moyennes et
écarts types qui les comprennent, sort-il p ≤ seuil plus souvent que le seuil nominal sous le nul ? Comparaison appariée, sur
les mêmes directions nulles et les mêmes témoins, avec la variante « sans u_j » (moyenne et écart type calculés sans u_j).

Taille réelle : 89 498 jetons, largeur 4 096, M = 2 000 directions nulles. Lecture : t = RMSNorm(J u)·γ, ε = 10⁻⁶, score = W_U t.
Scénarios : W_U et γ gaussiens (A) ; W_U structuré (direction commune, normes de lignes log-normales, γ à coordonnées extrêmes) (B) ;
B lu par une matrice J anisotrope de rang fort 64 (C). Nuls : isotrope ; signes autour de deux vecteurs anisotropes.
Usage : python banc_contre_lecteur_v1.py REPLIQUES TEMOINS
"""
import sys
import time

import numpy as np

T, D, M = 89_498, 4096, 2000
EPS = 1e-6
ENTROPIE = 0x6F70757343726F69736563616C696272   # graine propre au banc du contre-lecteur (arbitraire, écrite ici)
R, NT = int(sys.argv[1]), int(sys.argv[2])
NIVEAUX = (0.05, 0.01, 2 / (M + 1))           # p ≤ 0,001 ⇔ au plus un nul au-dessus ⇔ p ≤ 2/2 001


def rng(*cle):
    return np.random.default_rng(np.random.SeedSequence(entropy=ENTROPIE, spawn_key=tuple(cle)))


def monde(nom):
    g = rng(1, ord(nom))
    wu = (g.standard_normal((T, D), dtype=np.float32) * np.float32(0.02))
    gamma = (1 + 0.1 * g.standard_normal(D)).astype(np.float32)
    J = None
    if nom in "BC":
        mu = g.standard_normal(D).astype(np.float32)
        mu *= np.float32(0.6 / np.linalg.norm(mu))                       # direction commune des lignes (≈ 0,6 de norme)
        wu += mu[None, :]
        wu *= np.exp(0.3 * g.standard_normal(T)).astype(np.float32)[:, None]   # normes de lignes log-normales
        gamma[g.choice(D, 8, replace=False)] *= np.float32(25.0)          # quelques coordonnées extrêmes de γ
    if nom == "C":
        U = np.linalg.qr(g.standard_normal((D, 64)))[0]
        V = np.linalg.qr(g.standard_normal((D, 64)))[0]
        J = (0.3 * np.eye(D) + U @ np.diag(np.geomspace(30, 3, 64)) @ V.T).astype(np.float32)
    return wu, gamma, J


def lire(u, wu, gamma, J):
    x = u if J is None else J @ u
    x = x / np.sqrt(np.mean(x * x, axis=0, keepdims=True) + EPS) * gamma[:, None]
    return wu @ x                                                         # [T, n]


def directions(nul, v, g, n):
    if nul == "iso":
        u = g.standard_normal((D, n))
        return (u / np.sqrt(np.mean(u * u, axis=0, keepdims=True))).astype(np.float32)
    eps = g.integers(0, 2, size=(D, n)).astype(np.float64) * 2 - 1
    return (eps * v[:, None]).astype(np.float32)


def concentrations_nulles(a):
    """C(u_j) avec u_j compris (texte) et sans u_j (moyenne et écart type des M − 1 autres), par blocs de colonnes."""
    m = a.mean(1, dtype=np.float64)
    q = (a.astype(np.float64) ** 2).mean(1)
    s = np.sqrt(q - m * m)
    m32, s32 = m.astype(np.float32), s.astype(np.float32)
    avec, sans = np.empty(a.shape[1]), np.empty(a.shape[1])
    for c in range(0, a.shape[1], 200):
        b = a[:, c:c + 200].astype(np.float64)
        avec[c:c + 200] = ((b - m[:, None]) / s[:, None]).max(0)
        m_j = (M * m[:, None] - b) / (M - 1)
        var_j = (M * q[:, None] - b * b) / (M - 1) - m_j * m_j
        sans[c:c + 200] = ((b - m_j) / np.sqrt(var_j)).max(0)
    return m32, s32, avec, sans


def p_de(nuls, c):
    return (1 + (nuls[None, :] >= c[:, None]).sum(1)) / (M + 1)


v1 = rng(2, 1).standard_normal(D) * np.geomspace(0.01, 100, D)            # anisotrope (forme du repliement)
v2 = rng(2, 2).standard_normal(D) * np.geomspace(1e-3, 1e3, D) ** 1.5      # très anisotrope (peu de coordonnées dominent)
SCENARIOS = [("A", "iso", None), ("A", "signes", v1), ("B", "iso", None), ("B", "signes", v1), ("B", "signes", v2),
             ("C", "iso", None), ("C", "signes", v1)]
print(f"banc du contre-lecteur v1 : T={T}, D={D}, M={M}, {R} répliques de {NT} témoins par scénario ; entropie {ENTROPIE}")
mondes = {}
for k, (w, nul, v) in enumerate(SCENARIOS):
    if w not in mondes:
        mondes.clear()
        mondes[w] = monde(w)
    wu, gamma, J = mondes[w]
    t0 = time.time()
    taux = {"avec": [], "sans": []}
    cmax = []
    for r in range(R):
        g = rng(3, k, r)
        a = lire(directions(nul, v, g, M), wu, gamma, J)
        m, s, avec, sans = concentrations_nulles(a)
        del a
        ct = []
        for c in range(0, NT, 250):
            b = lire(directions(nul, v, g, min(250, NT - c)), wu, gamma, J)
            ct.append(((b - m[:, None]) / s[:, None]).max(0))
            del b
        ct = np.concatenate(ct).astype(np.float64)
        cmax.append(float(np.median(ct)))
        pa, ps = p_de(avec, ct), p_de(sans, ct)
        taux["avec"].append([float((pa <= x + 1e-12).mean()) for x in NIVEAUX])
        taux["sans"].append([float((ps <= x + 1e-12).mean()) for x in NIVEAUX])
    ta, ts = np.array(taux["avec"]), np.array(taux["sans"])
    nom_v = "" if v is None else (" v1" if v is v1 else " v2")
    print(f"{w} {nul}{nom_v} : {time.time() - t0:.0f} s ; C médiane des témoins {np.mean(cmax):.2f}")
    for i, x in enumerate(NIVEAUX):
        print(f"   seuil {x:.5f} : avec u_j {ta[:, i].mean():.4f} (répliques {np.round(ta[:, i], 4).tolist()}) ; "
              f"sans u_j {ts[:, i].mean():.4f} ; rapport moyen avec/sans {ta[:, i].mean() / max(ts[:, i].mean(), 1e-9):.3f}",
              flush=True)
