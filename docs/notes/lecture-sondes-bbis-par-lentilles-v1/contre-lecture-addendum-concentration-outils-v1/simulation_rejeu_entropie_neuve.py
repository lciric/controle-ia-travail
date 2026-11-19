"""Simulation jointe de la statistique corrigée de l'addendum « concentration » — v2. Données synthétiques seulement :
aucun poids, aucune sonde, aucune lentille, aucun code du paquet de la lecture. Au processeur.

Partie A (validité jointe, ordre en M). Par réplique : M directions nulles et une direction « lue » tirée du même nul, T = 128
jetons. Trois valeurs p de concentration de la direction lue, sur les mêmes tirages :
  - « v1 »       : chaque direction nulle jugée avec la moyenne et l'écart type des M nulles, elle-même comprise (texte v1) ;
  - « corrigée » : chaque direction nulle jugée sur les M − 1 autres nulles (addendum) ;
  - « exacte »   : chaque direction nulle jugée sur les M autres directions, la direction lue comprise (schéma échangeable,
                   valide exactement ; il sert de référence appariée).
M = 19, 39, 79, 159 : le niveau 0,05 est alors exact (k = (M + 1)/20). Rendu : taux de p ≤ 0,05, différence appariée
corrigée − exacte, erreur type.

Partie B (loi du compte de calibration, taille M = 2 000 du texte, T = 1 024 jetons). Par jeu : M directions nulles, 1 000
témoins du même nul ; compte des témoins à p ≤ 0,05 (les 1 000, et les 200 premiers), sous « v1 » et « corrigée » ; comparé à
la loi bêta-binomiale (n ; 100 ; 1 901). Part au-dessus du nul (vingt premiers jetons, quantile 0,99 par interpolation
linéaire) : part moyenne des nulles (avec et sans elles-mêmes) et des témoins, et taux de p ≤ 0,05.

Scénarios : « gaussien » (scores indépendants) ; « structure-<D> » (miniature de la lecture : score = W·(RMSNorm(u)·γ), u de
largeur D, lignes de W à direction commune et normes log-normales, γ à coordonnées extrêmes : jetons corrélés, d'autant plus
que D est petit, scores bornés ; D = 32 et 128 en partie A, 128 et 512 en partie B) ; « queues-lourdes » (scores indépendants de
loi de Student à 5 degrés de liberté).

Graines (R9) : numpy.random.SeedSequence(entropy=E, spawn_key=(entier des 8 premiers octets du SHA-256 de la clé,)), PCG64 ;
E = entropie du texte v1 ; clés neuves, propres à cet addendum :
  lentilles-bbis/addendum-concentration-v1/simulation-A/<scénario>/M<M>/bloc<i>
  lentilles-bbis/addendum-concentration-v1/simulation-B/<scénario>/bloc<i>
  lentilles-bbis/addendum-concentration-v1/monde/structure-<D>/<partie>
Usage : python -I -B simulation_statistique_corrigee_v2.py [A|B|AB] [ÉCHELLE]   (ÉCHELLE = 1 : taille déclarée)
"""
import hashlib
import sys
import time
from datetime import datetime, timezone
from math import exp, lgamma
from multiprocessing import Pool

import numpy as np

E = 12770144614910757870622607408685425681
PREFIXE = "lentilles-bbis/addendum-concentration-v1"
SCENARIOS_A = ("gaussien", "structure-32", "structure-128", "queues-lourdes")
SCENARIOS_B = ("gaussien", "structure-128", "structure-512", "queues-lourdes")
CLES = []


def generateur(cle):
    k = int.from_bytes(hashlib.sha256(cle.encode()).digest()[:8], "big")
    return np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=E, spawn_key=(k,))))


def monde(scenario, partie, T):
    """Matrice W (T × D) et γ de la miniature « structure-<D> »."""
    D = int(scenario.split("-")[1])
    g = generateur(f"{PREFIXE}/monde/{scenario}/{partie}")
    w = 0.02 * g.standard_normal((T, D))
    mu = g.standard_normal(D)
    w += 0.6 * 0.02 * np.sqrt(D) * mu / np.linalg.norm(mu)       # direction commune des lignes (0,6 de la norme d'une ligne)
    w *= np.exp(0.3 * g.standard_normal(T))[:, None]             # normes de lignes log-normales
    gamma = 1 + 0.1 * g.standard_normal(D)
    gamma[g.choice(D, max(1, D // 16), replace=False)] *= 5.0    # quelques coordonnées extrêmes
    return w.astype(np.float32), gamma.astype(np.float32)


def scores(g, scenario, n, T, w_gamma):
    """n directions du nul, lues : tableau (n, T) en double précision."""
    if scenario == "gaussien":
        return g.standard_normal((n, T), dtype=np.float32).astype(np.float64)
    if scenario == "queues-lourdes":
        return g.standard_t(5, size=(n, T))
    w, gamma = w_gamma
    u = g.standard_normal((n, w.shape[1]), dtype=np.float32)
    u = u / np.sqrt(np.mean(u * u, axis=1, keepdims=True) + 1e-6) * gamma[None, :]
    return (u @ w.T).astype(np.float64)


def sans_elle_meme(d, M):
    """z d'une direction nulle jugée sur les M − 1 autres, à partir de d (jugée avec elle-même, écart type de population) :
    fonction croissante de d, la même pour tous les jetons."""
    return d * np.sqrt(M / (M - 1)) / np.sqrt(np.maximum(1 - d * d / (M - 1), 1e-300))


# ---------------------------------------------------------------- partie A
def bloc_a(tache):
    scenario, M, T, repliques, i = tache
    cle = f"{PREFIXE}/simulation-A/{scenario}/M{M}/bloc{i}"
    g = generateur(cle)
    wg = monde(scenario, "A", T) if scenario.startswith("structure") else None
    k = (M + 1) // 20
    lot = max(1, 2_000_000 // ((M + 1) * T))
    n = np.zeros(5, dtype=np.int64)          # rejets v1, corrigée, exacte ; corrigée seule ; exacte seule
    fait = 0
    while fait < repliques:
        b = min(lot, repliques - fait)
        a = scores(g, scenario, b * (M + 1), T, wg).reshape(b, M + 1, T)
        nul = a[:, 1:, :]
        m = nul.mean(1, keepdims=True)
        s = nul.std(1, keepdims=True)
        dmax = ((nul - m) / s).max(2)                     # (b, M) : concentration « v1 » des nulles
        cv = ((a[:, 0, :] - m[:, 0, :]) / s[:, 0, :]).max(1)   # (b,) : concentration de la direction lue
        r_v1 = ((dmax >= cv[:, None]).sum(1) <= k - 1)
        r_co = ((sans_elle_meme(dmax, M) >= cv[:, None]).sum(1) <= k - 1)
        mt = a.mean(1, keepdims=True)
        st = a.std(1, keepdims=True)
        dt = ((a - mt) / st).max(2)                       # (b, M+1) : schéma échangeable (transformée croissante commune)
        r_ex = ((dt[:, 1:] >= dt[:, :1]).sum(1) <= k - 1)
        n += np.array([r_v1.sum(), r_co.sum(), r_ex.sum(), (r_co & ~r_ex).sum(), (~r_co & r_ex).sum()])
        fait += b
    return scenario, M, repliques, n, cle


def partie_a(echelle, bassin):
    T = 128
    plan = {19: 1_000_000, 39: 1_000_000, 79: 500_000, 159: 250_000}
    taches = []
    for sc in SCENARIOS_A:
        for M, N in plan.items():
            N = max(8, int(N * echelle))
            taches += [(sc, M, T, N // 8, i) for i in range(8)]
    print(f"A. validité jointe : T = {T} ; répliques par M : { {M: 8 * max(1, int(N * echelle) // 8) for M, N in plan.items()} }")
    cumul = {}
    for sc, M, r, n, cle in bassin.imap(bloc_a, taches):
        c = cumul.setdefault((sc, M), [0, np.zeros(5, dtype=np.int64)])
        c[0] += r
        c[1] += n
        CLES.append(cle)
    for sc in SCENARIOS_A:
        for M in plan:
            N, n = cumul[(sc, M)]
            v1, co, ex, plus, moins = (int(x) for x in n)
            diff = (plus - moins) / N
            et = np.sqrt(max(plus + moins - (plus - moins) ** 2 / N, 0.0)) / N
            et_ex = np.sqrt(0.05 * 0.95 / N)
            print(f"  {sc:<14} M = {M:>3} ({N} répliques) : v1 {v1 / N:.5f} ; corrigée {co / N:.5f} ; exacte {ex / N:.5f} "
                  f"(nominal 0,05000 ± {et_ex:.5f}) ; corrigée − exacte {diff:+.2e} ± {et:.1e} "
                  f"(soit {diff / 0.05 * M * M:+.1f} ± {et / 0.05 * M * M:.1f} / M² en relatif ; "
                  f"v1 − nominal = {(v1 / N - 0.05) / 0.05 * M:+.1f} / M en relatif)")


# ---------------------------------------------------------------- partie B
M_B, T_B, N_TEMOINS, RANG = 2000, 1024, 1000, 100


def parts(nul, tem):
    """Part au-dessus du nul des directions nulles (avec et sans elles-mêmes) et des témoins : vingt premiers jetons par
    score, quantile 0,99 par interpolation linéaire."""
    M = nul.shape[0]
    tri = np.sort(nul, axis=0)                                   # (M, T)
    rang = np.argsort(np.argsort(nul, axis=0), axis=0)           # rang 0..M−1 de chaque score dans son jeton
    h = 0.99 * (M - 1)
    k0, f = int(np.floor(h)), h - np.floor(h)
    q_tous = tri[k0] + f * (tri[k0 + 1] - tri[k0])               # quantile des M
    h2 = 0.99 * (M - 2)
    k2, f2 = int(np.floor(h2)), h2 - np.floor(h2)
    top = np.argpartition(-nul, 19, axis=1)[:, :20]              # (M, 20) jetons
    lignes = np.arange(M)[:, None]
    a, r = nul[lignes, top], rang[lignes, top]
    avec = (a > q_tous[top]).mean(1)
    # statistiques d'ordre k2 et k2 + 1 des M − 1 autres : celles des M, décalées d'un cran au-dessus du rang retiré
    bas = np.where(r <= k2, tri[k2 + 1, top], tri[k2, top])
    haut = np.where(r <= k2 + 1, tri[k2 + 2, top], tri[k2 + 1, top])
    sans = (a > bas + f2 * (haut - bas)).mean(1)
    topt = np.argpartition(-tem, 19, axis=1)[:, :20]
    pt = (tem[np.arange(tem.shape[0])[:, None], topt] > q_tous[topt]).mean(1)
    return avec, sans, pt


def bloc_b(tache):
    scenario, jeux, i = tache
    cle = f"{PREFIXE}/simulation-B/{scenario}/bloc{i}"
    g = generateur(cle)
    wg = monde(scenario, "B", T_B) if scenario.startswith("structure") else None
    lignes = []
    for _ in range(jeux):
        nul = scores(g, scenario, M_B, T_B, wg)
        m, s = nul.mean(0), nul.std(0)
        dmax = ((nul - m) / s).max(1)
        tem = scores(g, scenario, N_TEMOINS, T_B, wg)
        ct = ((tem - m) / s).max(1)
        seuil_v1 = np.sort(dmax)[-RANG]                           # 100ᵉ plus grande
        seuil_co = np.sort(sans_elle_meme(dmax, M_B))[-RANG]
        r1, r2 = ct > seuil_v1, ct > seuil_co
        avec, sans, pt = parts(nul, tem)
        p_avec = (1 + (avec[None, :] >= pt[:, None]).sum(1)) / (M_B + 1)
        p_sans = (1 + (sans[None, :] >= pt[:, None]).sum(1)) / (M_B + 1)
        lignes.append((r1.sum(), r2.sum(), r1[:200].sum(), r2[:200].sum(), avec.mean(), sans.mean(), pt.mean(),
                       (p_avec <= 0.05).sum(), (p_sans <= 0.05).sum()))
    return scenario, np.array(lignes, dtype=np.float64), cle


def loi_beta_binomiale(n, a=100.0, b=1901.0):
    lb = lgamma(a) + lgamma(b) - lgamma(a + b)
    return np.array([exp(lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1) + lgamma(k + a) + lgamma(n - k + b)
                         - lgamma(n + a + b) - lb) for k in range(n + 1)])


def intervalle(p, niveau):
    c = np.cumsum(p)
    bas = int(np.searchsorted(c, niveau, side="right"))           # plus petit q tel que P(X ≤ q) > niveau
    haut = int(np.searchsorted(c, 1 - niveau, side="left"))       # plus petit q tel que P(X ≤ q) ≥ 1 − niveau
    return bas, haut, float(p[:bas].sum() + p[haut + 1:].sum())


def partie_b(echelle, bassin):
    jeux = max(16, int(2000 * echelle))
    par_bloc = jeux // 16
    taches = [(sc, par_bloc, i) for sc in SCENARIOS_B for i in range(16)]
    print(f"B. loi du compte : M = {M_B}, T = {T_B}, {N_TEMOINS} témoins par jeu, {16 * par_bloc} jeux par scénario")
    cumul = {}
    for sc, lignes, cle in bassin.imap(bloc_b, taches):
        cumul.setdefault(sc, []).append(lignes)
        CLES.append(cle)
    for n, col in ((1000, (0, 1)), (200, (2, 3))):
        p = loi_beta_binomiale(n)
        k = np.arange(n + 1)
        moy, var = float((p * k).sum()), float((p * k * k).sum() - (p * k).sum() ** 2)
        i1, i5 = intervalle(p, 0.01), intervalle(p, 0.05)
        bornes = {1000: (23, 85), 200: (1, 24)}[n]
        print(f"  n = {n} : loi bêta-binomiale (n ; 100 ; 1 901) : moyenne {moy:.3f}, variance {var:.3f} ; intervalle à 1 % par côté "
              f"[{i1[0]}, {i1[1]}] (hors : {i1[2]:.4f}) ; à 5 % par côté [{i5[0]}, {i5[1]}] (hors : {i5[2]:.4f}) ; bornes {list(bornes)}")
        for sc in SCENARIOS_B:
            x = np.concatenate(cumul[sc])
            K = len(x)
            for nom, c in (("v1", col[0]), ("corrigée", col[1])):
                y = x[:, c]
                print(f"    {sc:<14} {nom:<8} : part moyenne {y.mean() / n:.5f} ± {y.std(ddof=1) / n / np.sqrt(K):.5f} "
                      f"(référence {moy / n:.5f}) ; variance {y.var(ddof=1):.2f} (rapport à la référence {y.var(ddof=1) / var:.3f} "
                      f"± {np.sqrt(2 / K) * 1.2:.3f}) ; hors de l'intervalle à 1 % : {((y < i1[0]) | (y > i1[1])).mean():.4f} ; "
                      f"à 5 % : {((y < i5[0]) | (y > i5[1])).mean():.4f} ; hors des bornes : {int(((y < bornes[0]) | (y > bornes[1])).sum())} sur {K}")
    print("  part au-dessus du nul (vingt premiers jetons) : part moyenne des nulles avec elles-mêmes (v1) / sans elles-mêmes "
          "(corrigée) / des témoins ; taux de p ≤ 0,05 des témoins, v1 / corrigée")
    for sc in SCENARIOS_B:
        x = np.concatenate(cumul[sc])
        K = len(x)
        d1, d2 = x[:, 4] - x[:, 6], x[:, 5] - x[:, 6]
        print(f"    {sc:<14} : {x[:, 4].mean():.5f} / {x[:, 5].mean():.5f} / {x[:, 6].mean():.5f} ; nulles − témoins : v1 "
              f"{d1.mean():+.5f} ± {d1.std(ddof=1) / np.sqrt(K):.5f}, corrigée {d2.mean():+.5f} ± {d2.std(ddof=1) / np.sqrt(K):.5f} ; "
              f"taux {x[:, 7].mean() / N_TEMOINS:.5f} ± {x[:, 7].std(ddof=1) / N_TEMOINS / np.sqrt(K):.5f} / "
              f"{x[:, 8].mean() / N_TEMOINS:.5f} ± {x[:, 8].std(ddof=1) / N_TEMOINS / np.sqrt(K):.5f}")


if __name__ == "__main__":
    quoi = sys.argv[1] if len(sys.argv) > 1 else "AB"
    echelle = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    t0 = time.time()
    print(f"commande : python -I -B simulation_statistique_corrigee_v2.py {quoi} {echelle} (python {sys.version.split()[0]}, numpy "
          f"{np.__version__}, {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}) ; entropie {E} ; 4 processus", flush=True)
    with Pool(4) as bassin:
        if "A" in quoi:
            partie_a(echelle, bassin)
            print(f"  durée cumulée {time.time() - t0:.0f} s", flush=True)
        if "B" in quoi:
            partie_b(echelle, bassin)
            print(f"  durée cumulée {time.time() - t0:.0f} s", flush=True)
    print(f"clés de graines employées ({len(CLES)}) : de {min(CLES)} à {max(CLES)} ; liste complète : préfixe "
          f"{PREFIXE}/simulation-<A|B>/<scénario>/[M<M>/]bloc<i>, i de 0 à 7 (A) ou de 0 à 15 (B) ; mondes : "
          f"{PREFIXE}/monde/structure-<D>/<A|B>")
