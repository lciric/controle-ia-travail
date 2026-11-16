"""Banc de l'angle « toute autre voie » — v1. Un appel = un cas (taille ou puissance), R mondes, tous les bras sur les
MÊMES tirages frais et aux MÊMES instants. Usage : python essai_libre_banc_v1.py CAS R_DEBUT R_FIN SORTIE.json

Bras (voir methodes-libre-v1.md) :
  v9      maximum certifié sur toutes les coupes (une cellule, sous-population, coupes des deux traits) — référence ;
  La      nul limité : une cellule + coupure de l'archive ; Ld : La + sous-population + signe de chaque trait ;
  grille  une cellule + sous-population + coupes aux déciles du plan (fixés avant les tirages), deux traits ;
  A1      artefact : poids appris en ligne (descente exponentielle, pas 0,2) sur les cellules de l'archive (argon-p2-01) ;
  A2      artefact : poids ajustés sur la première moitié, valeur e sur la seconde (argon-p1-01), lecture 125..200 ;
  Mc      statistique de A1, seuil critique simulé au pire cas sur une grille de 17 points de la classe La (B = 100) ;
  Md      statistique de A1, seuil par rééchantillonnage paramétrique sous le nul La ajusté sur les tirages (B = 200) ;
  OU      filtre : promue si La promeut au niveau alpha/2 OU v9 au niveau alpha/2 (partage du niveau) ;
  ET      promue si La ET v9 promeuvent (niveau alpha chacun) ;
  mixte   pari mixte : 1/2 W_La + 1/2 W_v9 >= 1/alpha à un instant.
"""
import json
import platform
import sys
import time

import numpy as np

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from essai_libre_commun_v1 import (ALPHA, D, K, N, RACINE, SEUIL, T, archive, clopper, composantes, em_certifie,
                                   en_ligne_lot, lois_connues, moitie, p_soft, partitions_v9, plan, rng_de, soft, taux,
                                   tirer, tirer_lot)

CAS = {
    0: "T1 copie d'un membre intérieur (une cellule, poids Dirichlet(1) sur 3 lois connues + 3 lois certaines)",
    1: "T2 copie d'un sommet (S1 seule)",
    2: "T3 poids extrêmes, bord du simplexe (une cellule, Dirichlet(0,1))",
    3: "T4 copie par morceaux sur la coupure de l'archive (S1 | S2 de part et d'autre de s_A)",
    4: "T4b membre par morceaux sur la coupure de l'archive, poids Dirichlet(1) par cellule, bruit aveugle commun",
    5: "T5 copie par sous-population (S1 sur g=0, S2 sur g=1)",
    6: "T6 copie à une coupure hors de l'archive (S1 | S2, seuil hors C_arch)",
    7: "V1 composante neuve globale, dose 0,3",
    8: "V1 composante neuve globale, dose 0,5",
    9: "V1 composante neuve globale, dose 0,7",
}
DOSES = {7: 0.3, 8: 0.5, 9: 0.7}
B_GRILLE, B_BOOT, ETA = 100, 200, 0.2


def monde_du_cas(cas, rng, A, z, g, PL):
    n = len(z)
    J = PL.shape[1]
    ext = None
    if cas in (0, 2):
        w = rng.dirichlet(np.full(J + K, 1.0 if cas == 0 else 0.1))
        P = mel(PL, w[:J]) + w[J:][None, :]
    elif cas == 1:
        P = PL[:, 0]
    elif cas == 3:
        m = z[:, A["jA"]] > A["sA"]
        P = np.where(m[:, None], PL[:, 0], PL[:, 1])
    elif cas == 4:
        r = rng.uniform(0, 0.3)
        rho = rng.dirichlet(np.ones(K)) * r
        muL, muR = rng.dirichlet(np.ones(J)) * (1 - r), rng.dirichlet(np.ones(J)) * (1 - r)
        m = z[:, A["jA"]] > A["sA"]
        P = np.where(m[:, None], mel(PL, muR), mel(PL, muL)) + rho[None]
    elif cas == 5:
        P = np.where((g == 1)[:, None], PL[:, 1], PL[:, 0])
    elif cas == 6:
        j = int(rng.integers(0, D))
        while True:
            s = round(float(rng.choice([-1, 1]) * rng.uniform(0.3, 1.0)), 2)
            if j != A["jA"] or abs(s - A["sA"]) >= 0.3:
                break
        ext = dict(trait=j, seuil=s)
        P = np.where((z[:, j] > s)[:, None], PL[:, 0], PL[:, 1])
    else:
        W1, b1 = A["S1"]
        Dl = rng.normal(size=(K, D))
        Dl -= Dl.mean(0, keepdims=True)
        P = p_soft((W1 + DOSES[cas] * Dl, b1), z)
    return P / P.sum(1, keepdims=True), ext


def mel(PL, w):
    """Mélange des lois connues : sum_j w_j L_j(. | x), forme (n, K)."""
    return np.einsum("njk,j->nk", PL, w)


def logw_max(logq, Dt):
    return float(np.max(logq[T - 1] - Dt))


def denominateurs(PL, y, z, g, A):
    """D_t (8 instants) pour v9, La, Ld, grille, plus le plus grand reste de certificat (UB - atteint) du maximum de chaque
    nul. Chaque nul limité est un groupe de partitions résolu à part, avec élagage dans le groupe (comme le v9)."""
    Aj = composantes(PL, y)
    dec = {j: np.quantile(z[:, j], np.arange(0.1, 0.95, 0.1)) for j in range(D)}
    out = {k: np.empty(len(T)) for k in ("v9", "La", "Ld", "grille")}
    restes = {k: [] for k in out}
    etat = {}
    etat_La = None
    for i, t in enumerate(T):
        zt, gt = z[:t], g[:t]
        un = np.zeros(t, bool)
        groupes = {
            "v9": partitions_v9(z, g, t),
            "La": np.array([un, zt[:, A["jA"]] > A["sA"]]),
            "Ld": np.array([un, zt[:, A["jA"]] > A["sA"], gt == 1, zt[:, 0] > 0, zt[:, 1] > 0]),
            "grille": np.array([un, gt == 1] + [zt[:, j] > s for j in range(D) for s in dec[j]]),
        }
        for k, M in groupes.items():
            if k == "v9":
                UB, F, _, _ = em_certifie(Aj[:t], y[:t], M)
            else:
                UB, F, _, etat[k] = em_certifie(Aj[:t], y[:t], M, maxit=1500, tol=2e-3, depart=etat.get(k))
            out[k][i] = UB.max()
            restes[k].append(float(UB.max() - F.max()))
            if k == "La" and t == N:
                b = int(np.argmax(F))
                r, beta, piL, piR = (a[b].copy() for a in etat[k])
                if b == 0:  # une seule cellule : toutes les instances sont dans la cellule « droite »
                    piL = piR.copy()
                etat_La = (r, beta, piL, piR)
    return out, {k: max(v) for k, v in restes.items()}, etat_La


def loi_La(PL, m, etat):
    r, beta, piL, piR = etat
    return np.where(m[:, None], (1 - r) * (mel(PL, piL)), (1 - r) * (mel(PL, piR))) + r * beta[None]


def grille_La(rng, PL, m):
    J = PL.shape[1]
    pts = []
    for i in range(J):
        for j in range(J):
            pts.append(np.where(m[:, None], PL[:, i], PL[:, j]))
    for k in range(K):
        pts.append(np.tile(np.eye(K)[k], (len(m), 1)))
    pts.append(mel(PL, np.full(J, 0.5 / J)) + 0.5 / K)
    for _ in range(4):
        r = rng.uniform(0, 0.5)
        rho = rng.dirichlet(np.ones(K)) * r
        pts.append(np.where(m[:, None], mel(PL, rng.dirichlet(np.ones(J)) * (1 - r)), mel(PL, rng.dirichlet(np.ones(J)) * (1 - r))) + rho)
    return pts


def stat_en_ligne(logq_lot, PL, Y, cel):
    lp = en_ligne_lot(PL, Y, cel, 2, ETA)
    return (logq_lot - lp)[:, T - 1].max(1)


def un_monde(cas, r):
    rng = rng_de(cas, r)
    A = archive(rng)
    z, g = plan(rng)
    PL = lois_connues(A, z)
    P, ext = monde_du_cas(cas, rng, A, z, g, PL)
    Q = P  # carte = loi du monde (copie exacte dans les cas de taille ; vraie découverte dans les cas V1)
    y = tirer(rng, P)
    n = np.arange(N)
    lq = np.log(np.maximum(Q[n, y], 1e-12))
    logq = np.cumsum(lq)
    Dd, ecart_v9, etat = denominateurs(PL, y, z, g, A)
    # contrôle d'emboîtement (chaque nul limité est contenu dans la classe du v9) : D_v9 >= D_X - reste_X à chaque instant
    viol = sum(int(np.any(Dd["v9"] < Dd[k] - ecart_v9[k] - 1e-6)) for k in ("La", "Ld", "grille"))
    lw = {k: logq[T - 1] - v for k, v in Dd.items()}
    res = {k: float(v.max()) for k, v in lw.items()}
    m = z[:, A["jA"]] > A["sA"]
    cel = m.astype(int)
    # A1 en ligne
    s_on = stat_en_ligne(logq[None], PL, y[None], cel)[0]
    res["A1"] = float(s_on)
    # A2 moitié : lecture aux instants 125..200, cumul à partir de 101
    lp2 = moitie(PL, y, cel, 2)
    lq2 = np.cumsum(lq[N // 2:])
    res["A2"] = float((lq2 - lp2)[np.array([25, 50, 75, 100]) - 1].max())
    # Mc : seuil au pire cas sur la grille
    pts = grille_La(rng, PL, m)
    seuils = []
    for Pg in pts:
        Y = tirer_lot(rng, Pg, B_GRILLE)
        LQ = np.cumsum(np.log(np.maximum(Q[n[None], Y], 1e-12)), 1)
        seuils.append(float(np.quantile(stat_en_ligne(LQ, PL, Y, cel), 1 - ALPHA)))
    c_grille = max(seuils)
    # Md : rééchantillonnage sous le nul La ajusté
    Ph = loi_La(PL, m, etat)
    Ph = Ph / Ph.sum(1, keepdims=True)
    Y = tirer_lot(rng, Ph, B_BOOT)
    LQ = np.cumsum(np.log(np.maximum(Q[n[None], Y], 1e-12)), 1)
    c_boot = float(np.quantile(stat_en_ligne(LQ, PL, Y, cel), 1 - ALPHA))
    prom = {k: res[k] >= SEUIL for k in ("v9", "La", "Ld", "grille", "A1", "A2")}
    prom["Mc"] = s_on >= c_grille
    prom["Md"] = s_on >= c_boot
    s2 = float(np.log(2 / ALPHA))
    prom["OU"] = (res["La"] >= s2) or (res["v9"] >= s2)
    prom["ET"] = prom["La"] and prom["v9"]
    mix = np.log(0.5 * np.exp(lw["La"]) + 0.5 * np.exp(lw["v9"]))
    prom["mixte"] = bool(mix.max() >= SEUIL)
    res["mixte"] = float(mix.max())
    return prom, res, dict(c_grille=c_grille, c_boot=c_boot, restes=ecart_v9, ext=ext, viol=viol)


def main():
    cas, r0, r1, sortie = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    R = r1 - r0
    t0 = time.time()
    bras = ("v9", "La", "Ld", "grille", "A1", "A2", "Mc", "Md", "OU", "ET", "mixte")
    bits = {b: [] for b in bras}
    lwm = {b: [] for b in ("v9", "La", "Ld", "grille", "A1", "A2", "mixte")}
    nviol = 0
    cg, cb, rest = [], [], {k: [] for k in ("v9", "La", "Ld", "grille")}
    for r in range(r0, r1):
        prom, res, aux = un_monde(cas, r)
        for b in bras:
            bits[b].append(bool(prom[b]))
        for b in lwm:
            lwm[b].append(res[b])
        cg.append(aux["c_grille"]); cb.append(aux["c_boot"]); nviol += aux["viol"]
        for k in rest:
            rest[k].append(aux["restes"][k])
    q = lambda v: [round(float(x), 4) for x in np.quantile(v, [0.0, 0.5, 0.95, 1.0])]
    sortie_d = dict(
        version="essai_libre_banc_v1", cas=cas, description=CAS[cas], mondes=R, r_debut=r0, r_fin=r1,
        graines=dict(racine=RACINE, derivation="numpy.random.SeedSequence(entropy=racine, spawn_key=(cas, r)), r = 0..R-1 ; "
                     "un seul générateur par monde, consommé dans l'ordre : archive, plan, monde, tirages frais, grille, simulations",
                     r_debut=r0, r_fin=r1),
        niveau=dict(alpha=ALPHA, n=N, instants=T.tolist(), seuil_log=SEUIL),
        taux={b: taux(bits[b]) for b in bras},
        log_w_max_quantiles_0_50_95_100={b: q(v) for b, v in lwm.items()},
        seuil_critique_grille_quantiles=q(cg), seuil_critique_reechantillonnage_quantiles=q(cb),
        violations_emboitement=nviol,
        reste_certificat_max_par_nul={k: round(float(max(v)), 6) for k, v in rest.items()},
        bits={b: "".join("1" if x else "0" for x in v) for b, v in bits.items()},
        duree_s=round(time.time() - t0, 1), python=platform.python_version(), numpy=np.__version__,
    )
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(sortie_d, f, ensure_ascii=False, indent=1)
    print(json.dumps({b: sortie_d["taux"][b]["taux"] for b in bras}), sortie_d["duree_s"])


if __name__ == "__main__":
    main()
