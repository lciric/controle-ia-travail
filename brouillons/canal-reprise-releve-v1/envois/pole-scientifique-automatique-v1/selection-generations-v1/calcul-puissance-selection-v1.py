#!/usr/bin/env python3
"""Calcul de puissance de la boucle de sélection génération à génération — v1 (lignée conv-audit, 1er novembre 2026).

Annexe de `reponse-conv-audit-selection-generations-v1.md` (même dossier). Régime exploratoire, processeur seul, aucune
entrée lue, aucun fichier écrit, aucun appel de réseau ni de modèle. Rejouer :

    cd "$(mktemp -d)" && python3 -I <chemin>/calcul-puissance-selection-v1.py > sortie.txt

Graines : `numpy.random.SeedSequence` (règle R9), entropie = SHA-256 du nom de ce calcul, une clé de dérivation par tâche
(`graine(...)`), indépendante de l'ordre d'appel. Deux exécutions donnent une sortie identique octet pour octet.

Monde simulé (le plus simple qui garde la forme du juge figé du pôle, `pole/selection_pari.py` de l'orchestrateur v56) :
- une issue binaire par épisode, un trait z ~ N(0, 1) ; une fiche vraie a la loi P(y = 1 | z) = σ(β·z) ; une fiche nulle
  affirme la même forme mais l'issue est indépendante du trait (P = 1/2) ;
- richesse W_t = numérateur / max sur la bibliothèque aveugle (urne, moyennes glissantes de fenêtres 5, 10, 20, 50 à
  lissage 0,5 ; l'uniforme et la marginale ajustée sont dominées par l'urne et omises) — réécrite ici en numpy, mêmes
  formules que `_traj_urne` et `_traj_moyennes_glissantes`, pas le code v56 lui-même ;
- deux numérateurs : « plein » (la loi engagée telle quelle) et « fractions » (pari à fraction de la v7 :
  mélange uniforme sur λ ∈ {0,25 ; 0,5 ; 0,75 ; 1} de λ·p_h + (1 − λ)·marginale en ligne, `trajectoire_numerateur`) ;
- e-valeur d'une fiche pour la règle de Benjamini-Hochberg sur e-valeurs (« e-BH ») : richesse arrêtée au premier instant
  où elle atteint m/α, sinon richesse au dernier épisode (`cycle.appliquer_multiplicite`, correction du 27 octobre).

Ce que le calcul ne dit pas : la puissance sur de vrais moniteurs (issues à plus de deux valeurs, nul informé plus fort
que la marginale, effets hétérogènes) ; les parts de fiches vraies ; les taux d'élimination des tests de mort (pris
« illustratifs »). Les réservoirs de trajectoires sont rééchantillonnés avec remise pour former les générations.
"""

import hashlib
import math
import platform

import numpy as np

VERSION = "calcul-puissance-selection-v1"
ENTROPIE = int(hashlib.sha256(VERSION.encode("utf-8")).hexdigest(), 16)
ALPHA = 0.05
R = 2000                   # trajectoires par réservoir
N_MAX = 1800               # épisodes d'épreuve au plus
N_GRILLE = (100, 150, 200, 300, 450, 600, 900, 1200, 1800)
FENETRES = (5, 10, 20, 50)
LISSAGE = 0.5
FRACTIONS = (0.25, 0.5, 0.75, 1.0)
BLOC = 250
REPS = 2000                # générations simulées par case
COUT_EPISODE_USD = 0.047   # estimation de session-depot (comparaison couche 2, l. 40) : ILLUSTRATIF


def graine(*cle):
    return np.random.SeedSequence(ENTROPIE, spawn_key=tuple(int(c) for c in cle))


def log_sigmoide(u):
    return -np.logaddexp(0.0, -u)


def reservoir(cle, beta_vrai, beta_loi):
    """log W_t, forme (R, N_MAX), pour les numérateurs « plein » et « fractions »."""
    rng = np.random.default_rng(graine(*cle))
    n = N_MAX
    sorties = {"plein": np.empty((R, n)), "fractions": np.empty((R, n))}
    lf = np.concatenate(([0.0], np.cumsum(np.log(np.arange(1, n + 1)))))
    t = np.arange(1, n + 1)
    i = np.arange(n)
    for a in range(0, R, BLOC):
        b = min(R, a + BLOC)
        r = b - a
        z = rng.standard_normal((r, n))
        y = rng.random((r, n)) < 1.0 / (1.0 + np.exp(-beta_vrai * z))
        cs = np.concatenate((np.zeros((r, 1)), np.cumsum(y, axis=1, dtype=np.float64)), axis=1)
        c1 = cs[:, 1:].astype(np.int64)
        den = lf[c1] + lf[t[None, :] - c1] - lf[t][None, :]          # urne : Σ ln c_k! − ln t!
        for w in FENETRES:                                           # moyennes glissantes, lissage 0,5
            lo = np.maximum(0, i - w)
            s = cs[:, i] - cs[:, lo]
            nw = (i - lo)[None, :]
            p1 = (s + LISSAGE) / (nw + 2 * LISSAGE)
            den = np.maximum(den, np.cumsum(np.where(y, np.log(p1), np.log(1.0 - p1)), axis=1))
        u = beta_loi * z
        lp = np.where(y, log_sigmoide(u), log_sigmoide(-u))
        sorties["plein"][a:b] = np.cumsum(lp, axis=1) - den
        m1 = (cs[:, :-1] + 0.5) / (i[None, :] + 1.0)                  # marginale en ligne (Laplace 0,5)
        px = np.exp(lp)
        mx = np.where(y, m1, 1.0 - m1)
        cum = np.stack([np.cumsum(np.log(np.maximum(1e-12, lam * px + (1.0 - lam) * mx)), axis=1) for lam in FRACTIONS])
        haut = cum.max(axis=0)
        sorties["fractions"][a:b] = haut + np.log(np.exp(cum - haut).mean(axis=0)) - den
    return sorties


def franchissement(lw, niveau):
    """Indice du premier épisode où log W ≥ niveau ; N_MAX si jamais."""
    ok = lw >= niveau
    return np.where(ok.any(axis=1), ok.argmax(axis=1), N_MAX)


def puissance(idx, n):
    return float(np.mean(idx < n))


def n_requis(idx, cible=0.8):
    s = np.sort(idx)
    j = int(math.ceil(cible * len(s))) - 1
    return None if s[j] >= N_MAX else int(s[j]) + 1


def arretee(lw, idx, n):
    rang = np.arange(lw.shape[0])
    return np.where(idx < n, lw[rang, np.minimum(idx, N_MAX - 1)], lw[:, n - 1])


def ebh(log_e, alpha):
    """Règle e-BH ordinaire (budgets α/m), lignes = générations : rend le masque des fiches retenues."""
    g, m = log_e.shape
    ordre = np.argsort(-log_e, axis=1, kind="stable")
    tri = np.take_along_axis(log_e, ordre, axis=1)
    k = np.arange(1, m + 1)
    ok = tri >= np.log(m / (alpha * k))[None, :] - 1e-12
    kstar = np.where(ok.any(axis=1), m - np.argmax(ok[:, ::-1], axis=1), 0)
    retenu = np.zeros((g, m), dtype=bool)
    np.put_along_axis(retenu, ordre, k[None, :] <= kstar[:, None], axis=1)
    return retenu


def log_comb(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def fisher_unilateral(a, b, n):
    """P(X ≥ a) sous l'hypergéométrique (deux bras de n, K = a + b retenues) : bras A > bras B."""
    k_tot = a + b
    lc = log_comb(2 * n, k_tot)
    return sum(math.exp(log_comb(n, x) + log_comb(n, k_tot - x) - lc) for x in range(a, min(k_tot, n) + 1))


def mann_whitney_unilateral(xa, xb):
    """p unilatéral (A > B), approximation normale, rangs moyens ignorés (valeurs continues) ; lignes = répliques."""
    na, nb = xa.shape[1], xb.shape[1]
    tout = np.concatenate((xa, xb), axis=1)
    rangs = np.argsort(np.argsort(tout, axis=1, kind="stable"), axis=1) + 1.0
    u = rangs[:, :na].sum(axis=1) - na * (na + 1) / 2.0
    zz = (u - na * nb / 2.0) / math.sqrt(na * nb * (na + nb + 1) / 12.0)
    return 0.5 * np.vectorize(math.erfc)(zz / math.sqrt(2.0))


def info_mutuelle(beta):
    """I(Y ; Z) en nat pour P(y=1|z) = σ(βz), z ~ N(0,1) (quadrature de Gauss-Hermite probabiliste, 80 points)."""
    x, w = np.polynomial.hermite_e.hermegauss(80)
    w = w / w.sum()
    p = 1.0 / (1.0 + np.exp(-beta * x))
    return float(np.sum(w * (p * np.log(2 * p) + (1 - p) * np.log(2 * (1 - p)))))


def f(x, nd=3):
    return "—" if x is None else (f"{x:.{nd}f}" if isinstance(x, float) else str(x))


def main():
    print(f"# {VERSION} — sortie")
    print(f"python {platform.python_version()} ; numpy {np.__version__} ; entropie SeedSequence = SHA-256(« {VERSION} »)")
    print(f"α = {ALPHA} ; réservoirs de {R} trajectoires ; épreuve ≤ {N_MAX} épisodes ; générations simulées par case : {REPS}")
    print()

    betas = (0.3, 0.6, 0.9)
    niveaux_m = (1, 20, 30, 40)
    stock = {}  # pools d'e-valeurs arrêtées pour les parties C à F
    m_stock = tuple(range(1, 41)) + (80, 160)

    # ---------------- A. puissance par fiche, seuils 1/α et m/α (k = 1 : une seule découverte) --------------------
    print("## A. Puissance par fiche vraie (P(sup log W ≥ log(m/α)) à n épisodes d'épreuve) ; m = 1 : seuil par fiche")
    print("Colonnes : effet β (log-rapport de cotes par écart type) ; loi engagée ; numérateur ; m ; puissance pour n = "
          + ", ".join(str(n) for n in N_GRILLE) + " ; n requis pour 0,8")
    controles = []
    for ib, beta in enumerate(betas):
        for ic, (nom_loi, beta_loi) in enumerate((("exacte", beta), ("surestimée ×2", 2 * beta))):
            pools = reservoir((1, ib, ic), beta, beta_loi)
            for num in ("plein", "fractions"):
                lw = pools[num]
                for m in niveaux_m:
                    idx = franchissement(lw, math.log(m / ALPHA))
                    ligne = " ".join(f(puissance(idx, n), 2) for n in N_GRILLE)
                    print(f"β={beta} | {nom_loi:13s} | {num:9s} | m={m:2d} | {ligne} | n80={f(n_requis(idx))}")
                if beta == 0.6 and nom_loi == "exacte" and num == "plein":
                    stock["vraie_0.6"] = {}
                    for alpha in (0.05, 0.10, 0.20):
                        ms = m_stock if alpha == 0.05 else (20, 30, 40)
                        for m in ms:
                            idx = franchissement(lw, math.log(m / alpha))
                            for n in N_GRILLE:
                                stock["vraie_0.6"][(alpha, m, n)] = arretee(lw, idx, n)
                    stock["vraie_0.6_final"] = {n: lw[:, n - 1].copy() for n in N_GRILLE}
                if beta == 0.3 and nom_loi == "exacte" and num == "plein":
                    stock["vraie_0.3"] = {}
                    for m in (20, 30, 40):
                        idx = franchissement(lw, math.log(m / ALPHA))
                        for n in N_GRILLE:
                            stock["vraie_0.3"][(ALPHA, m, n)] = arretee(lw, idx, n)
                if nom_loi == "exacte":
                    stock[("lw_exacte", beta, num)] = lw  # pour la partie B (seuils décalés)
            del pools
        # nulles : la fiche affirme β, l'issue ne dépend pas du trait
        pools = reservoir((1, ib, 9), 0.0, beta)
        for num in ("plein", "fractions"):
            lw = pools[num]
            fp = puissance(franchissement(lw, math.log(1 / ALPHA)), N_MAX)
            controles.append(f"fiche nulle affirmant β={beta}, numérateur {num} : P(sup log W ≥ log 1/α sur {N_MAX} épisodes) = "
                             f"{fp:.4f} (garantie : ≤ {ALPHA})")
            if beta == 0.6 and num == "plein":
                stock["nulle_0.6"] = {}
                for alpha in (0.05, 0.10, 0.20):
                    ms = m_stock if alpha == 0.05 else (20, 30, 40)
                    for m in ms:
                        idx = franchissement(lw, math.log(m / alpha))
                        for n in N_GRILLE:
                            stock["nulle_0.6"][(alpha, m, n)] = arretee(lw, idx, n)
                stock["nulle_0.6_final"] = {n: lw[:, n - 1].copy() for n in N_GRILLE}
        del pools
    print()
    print("Contrôles du calcul (cas sains : la garantie de Ville doit tenir)")
    for c in controles:
        print("- " + c)
    print()

    # ---------------- A bis. approximation du pont contre la simulation -----------------------------------------
    print("## A bis. Approximation du pont (n ≈ 2·log(m/α) / I(Y;Z)) contre n requis simulé (loi exacte, numérateur plein)")
    for beta in betas:
        info = info_mutuelle(beta)
        lw = stock[("lw_exacte", beta, "plein")]
        for m in (1, 17, 30):
            approx = math.ceil(2 * math.log(m / ALPHA) / info)
            sim = n_requis(franchissement(lw, math.log(m / ALPHA)))
            print(f"β={beta} | I = {info:.4f} nat/épisode | m={m:2d} | pont ≈ {approx} | simulé (0,8) = {f(sim)}")
    print()

    # ---------------- B. coût en données : tranche fraîche par génération contre épreuve réutilisée --------------
    print("## B. Coût en données du renouvellement (m = 30 fiches jugées par génération, puissance 0,8 par fiche vraie, k = 1)")
    m = 30
    t_binaire = sum(math.comb(m, k) for k in range(0, 4))
    t_niveaux = sum(math.comb(m, k) * 3 ** k for k in range(0, 4))
    print(f"Transcription qui fuit d'une génération à la suivante si l'épreuve est réutilisée : ensemble des retenues (≤ 3 sur {m}) "
          f"→ |T| = {t_binaire} (log = {math.log(t_binaire):.2f} nat) ; avec l'aptitude en 3 niveaux → |T| = {t_niveaux} "
          f"(log = {math.log(t_niveaux):.2f} nat). Seuil corrigé après r réutilisations : log(m/α) + r·log|T| (borne d'union "
          "sur les transcriptions possibles).")
    for beta in betas:
        for num in ("plein", "fractions"):
            lw = stock[("lw_exacte", beta, num)]
            base = math.log(m / ALPHA)
            r0 = n_requis(franchissement(lw, base))
            r1 = n_requis(franchissement(lw, base + math.log(t_binaire)))
            r2 = n_requis(franchissement(lw, base + 2 * math.log(t_binaire)))
            r1n = n_requis(franchissement(lw, base + math.log(t_niveaux)))
            frais3 = None if r0 is None else 3 * r0
            reutil3 = r2
            usd = (lambda e: None if e is None else round(e * COUT_EPISODE_USD, 1))
            print(f"β={beta} | {num:9s} | tranche fraîche : n80 = {f(r0)} par génération, 3 générations = {f(frais3)} épisodes "
                  f"(≈ {f(usd(frais3), 1)} USD illustratif) | épreuve réutilisée (retenues seules) : génération 2 n80 = {f(r1)}, "
                  f"génération 3 n80 = {f(r2)} → tranche unique ≥ {f(reutil3)} épisodes (≈ {f(usd(reutil3), 1)} USD) | "
                  f"génération 2 avec aptitude en 3 niveaux : n80 = {f(r1n)}")
    for k in [k for k in stock if isinstance(k, tuple) and k[0] == "lw_exacte"]:
        del stock[k]
    print()

    # ---------------- C. contrôle des fausses découvertes sur la génération ---------------------------------------
    print("## C. Génération de m fiches dont m1 vraies (β = 0,6, loi exacte, numérateur plein) : puissance moyenne (part des "
          "vraies retenues), P(au moins une vraie retenue), taux de fausses découvertes moyen")
    print("Règles : « par fiche » = seuil 1/α sans multiplicité (aucun contrôle) ; « e-BH α » = règle codée, au niveau α.")
    rng = np.random.default_rng(graine(3))
    for m in (20, 30, 40):
        for pi1 in (0.05, 0.10, 0.20):
            m1 = max(1, int(round(pi1 * m)))
            for n in (300, 600, 1200):
                cases = []
                iv = rng.integers(0, R, (REPS, m1))
                inn = rng.integers(0, R, (REPS, m - m1))
                # par fiche (m = 1, α = 0,05)
                le = np.concatenate((stock["vraie_0.6"][(0.05, 1, n)][iv], stock["nulle_0.6"][(0.05, 1, n)][inn]), axis=1)
                ret = le >= math.log(1 / ALPHA) - 1e-12
                cases.append(("par fiche", ret))
                for alpha in (0.05, 0.10, 0.20):
                    le = np.concatenate((stock["vraie_0.6"][(alpha, m, n)][iv], stock["nulle_0.6"][(alpha, m, n)][inn]), axis=1)
                    cases.append((f"e-BH {alpha:.2f}", ebh(le, alpha)))
                morceaux = []
                for nom, ret in cases:
                    td = ret[:, :m1].sum(axis=1)
                    fd = ret[:, m1:].sum(axis=1)
                    fdp = fd / np.maximum(td + fd, 1)
                    morceaux.append(f"{nom} : {td.mean() / m1:.2f} ; {np.mean(td > 0):.2f} ; {fdp.mean():.3f}")
                print(f"m={m} m1={m1} n={n} | " + " | ".join(morceaux))
    # sensibilité : effet plus faible
    print("Sensibilité β = 0,3 (e-BH 0,05) :")
    for m in (20, 40):
        m1 = max(1, int(round(0.10 * m)))
        for n in (600, 1800):
            iv = rng.integers(0, R, (REPS, m1))
            inn = rng.integers(0, R, (REPS, m - m1))
            le = np.concatenate((stock["vraie_0.3"][(0.05, m, n)][iv], stock["nulle_0.6"][(0.05, m, n)][inn]), axis=1)
            ret = ebh(le, 0.05)
            td = ret[:, :m1].sum(axis=1)
            print(f"  m={m} m1={m1} n={n} | puissance {td.mean() / m1:.2f} ; P(≥ 1 vraie) {np.mean(td > 0):.2f}")
    print()

    # ---------------- D. filtre des tests de mort avant le pôle (données disjointes) -------------------------------
    print("## D. Tests de mort comme filtre éliminatoire avant le pôle (ILLUSTRATIF : tuent une nulle sur 2, une vraie sur 10 ; "
          "tranche exploratoire disjointe de l'épreuve) : m' = fiches restantes, fixé avant toute issue d'épreuve")
    rng = np.random.default_rng(graine(4))
    for m, m1 in ((30, 3), (40, 4)):
        for n in (300, 600):
            td_avec, fdp_avec, m_prime = [], [], []
            vv =rng.random((REPS, m1)) >= 0.10
            vn = rng.random((REPS, m - m1)) >= 0.50
            iv = rng.integers(0, R, (REPS, m1))
            inn = rng.integers(0, R, (REPS, m - m1))
            le = np.concatenate((stock["vraie_0.6"][(0.05, m, n)][iv], stock["nulle_0.6"][(0.05, m, n)][inn]), axis=1)
            td_sans = ebh(le, 0.05)[:, :m1].sum(axis=1)
            for g in range(REPS):
                a = int(vv[g].sum())
                b = int(vn[g].sum())
                mp = a + b
                m_prime.append(mp)
                if mp == 0:
                    td_avec.append(0)
                    fdp_avec.append(0.0)
                    continue
                le1 = np.concatenate((stock["vraie_0.6"][(0.05, mp, n)][iv[g][vv[g]]],
                                      stock["nulle_0.6"][(0.05, mp, n)][inn[g][vn[g]]]))[None, :]
                r = ebh(le1, 0.05)[0]
                td_avec.append(int(r[:a].sum()))
                fdp_avec.append(float(r[a:].sum() / max(1, r.sum())))
            print(f"m={m} m1={m1} n={n} | sans filtre : puissance {np.mean(td_sans) / m1:.2f} | avec filtre : m' moyen "
                  f"{np.mean(m_prime):.1f}, puissance (sur les m1 de départ) {np.mean(td_avec) / m1:.2f}, taux de fausses "
                  f"découvertes {np.mean(fdp_avec):.3f}")
    print()

    # ---------------- E. ablation « génération 2 avec et sans filtre du pôle » ------------------------------------
    print("## E. Ablation : bras A (parents promus par le pôle) contre bras B (parents choisis par les juges), N fiches par bras, "
          "même tranche fraîche (n = 600), e-BH 0,05 dans chaque bras (m = N) ; part de fiches vraies πA, πB")
    print("Puissance (unilatérale, 5 %) de : M1 = test exact de Fisher sur le nombre de retenues ; M2 = Mann-Whitney sur log W "
          "final ; M3 = « survivantes neuves par euro » à coût égal par bras (= M1)")
    rng = np.random.default_rng(graine(5))
    n = 600
    cache_fisher = {}
    for pib in (0.05, 0.10):
        for ratio in (2, 3):
            pia = min(0.9, ratio * pib)
            for N in (20, 40, 80, 160):
                va = rng.random((REPS, N)) < pia
                vb = rng.random((REPS, N)) < pib
                ia = rng.integers(0, R, (REPS, N))
                ib_ = rng.integers(0, R, (REPS, N))
                ea = np.where(va, stock["vraie_0.6"][(0.05, N, n)][ia], stock["nulle_0.6"][(0.05, N, n)][ia])
                eb = np.where(vb, stock["vraie_0.6"][(0.05, N, n)][ib_], stock["nulle_0.6"][(0.05, N, n)][ib_])
                ra = ebh(ea, 0.05).sum(axis=1)
                rb = ebh(eb, 0.05).sum(axis=1)
                ps = []
                for a, b in zip(ra.tolist(), rb.tolist()):
                    cle = (a, b, N)
                    if cle not in cache_fisher:
                        cache_fisher[cle] = fisher_unilateral(a, b, N)
                    ps.append(cache_fisher[cle])
                p1 = np.mean(np.array(ps) <= 0.05)
                fa = np.where(va, stock["vraie_0.6_final"][n][ia], stock["nulle_0.6_final"][n][ia])
                fb = np.where(vb, stock["vraie_0.6_final"][n][ib_], stock["nulle_0.6_final"][n][ib_])
                p2 = np.mean(mann_whitney_unilateral(fa, fb) <= 0.05)
                print(f"πB={pib:.2f} πA={pia:.2f} N={N:3d} | retenues moyennes A {ra.mean():.2f}, B {rb.mean():.2f} | "
                      f"M1 {p1:.2f} | M2 {p2:.2f}")
    print()

    # ---------------- F. témoin interne continu : immigrants dans chaque génération --------------------------------
    print("## F. Témoin interne : chaque génération de 30 = 21 filles (parents promus) + 9 immigrants (sans parents), même "
          "tranche, e-BH 0,05 sur les 30 ; cumul sur G générations ; πI = 0,05")
    rng = np.random.default_rng(graine(6))
    n = 600
    for pio in (0.10, 0.15, 0.25):
        morceaux = []
        for G in (1, 2, 4, 6, 10):
            ra_tot = np.zeros(REPS, dtype=np.int64)
            rb_tot = np.zeros(REPS, dtype=np.int64)
            fa_l, fb_l = [], []
            for _ in range(G):
                v = np.concatenate((rng.random((REPS, 21)) < pio, rng.random((REPS, 9)) < 0.05), axis=1)
                ii = rng.integers(0, R, (REPS, 30))
                e = np.where(v, stock["vraie_0.6"][(0.05, 30, n)][ii], stock["nulle_0.6"][(0.05, 30, n)][ii])
                ret = ebh(e, 0.05)
                ra_tot += ret[:, :21].sum(axis=1)
                rb_tot += ret[:, 21:].sum(axis=1)
                fin = np.where(v, stock["vraie_0.6_final"][n][ii], stock["nulle_0.6_final"][n][ii])
                fa_l.append(fin[:, :21])
                fb_l.append(fin[:, 21:])
            # Fisher à effectifs inégaux : 21G contre 9G
            na, nb = 21 * G, 9 * G
            ps = []
            for a, b in zip(ra_tot.tolist(), rb_tot.tolist()):
                k_tot = a + b
                lc = log_comb(na + nb, k_tot)
                ps.append(sum(math.exp(log_comb(na, x) + log_comb(nb, k_tot - x) - lc)
                              for x in range(a, min(k_tot, na) + 1)))
            p1 = np.mean(np.array(ps) <= 0.05)
            p2 = np.mean(mann_whitney_unilateral(np.concatenate(fa_l, axis=1), np.concatenate(fb_l, axis=1)) <= 0.05)
            morceaux.append(f"G={G}: M1 {p1:.2f}, M2 {p2:.2f}")
        print(f"πO={pio:.2f} | " + " | ".join(morceaux))
    print()
    print("# fin")


if __name__ == "__main__":
    main()
