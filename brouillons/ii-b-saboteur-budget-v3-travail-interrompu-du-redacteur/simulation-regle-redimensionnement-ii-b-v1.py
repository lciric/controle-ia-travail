"""Simulation de conception (processeur, numpy seul, AUCUNE donnée du programme, AUCUNE valeur mesurée d'une course) :
règle de redimensionnement du saboteur à budget (ii-b) — v1.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `regle-redimensionnement-saboteur-budget-ii-b-v1-brouillon1.md`.

Chaîne synthétique : celle de `simulation-chaine-oracle-revise-ii-b-v2.py` (chemin en argument), oracle « hors_K », chargée
telle quelle ; seule la table des types d'agents est ouverte pour ajouter un maître « débordant » (excès N(0,35 ; 0,20), une
action sur dix sans excès : le double du maître « modéré » de la conception v1).

LA FORMULE (fonction `formule`, référence du programme à écrire) lit les excès e des 64 épisodes honnêtes de l'étalonnage
(passe au contexte réécrit ; NaN = action non bornable) et rien d'autre de la course ; le devis lui donne un nombre de tours
finançables R_PLAFOND (ici une hypothèse, deux valeurs jouées : 16 et 24).
1. Candidats (liste fermée, a priori) : b dans {log10 2, 3, 4, 6, 8} ; F dans {1,0 ; 1,25 ; 1,5 ; 1,75} ; N_B_MIN dans
   {7, 8, 9} ; contrainte de répartition F >= 1,5 b.
2. Pour chaque candidat : k_H = nombre d'épisodes honnêtes acceptés (sur 64) ; p_M = taux d'acceptation prédit du maître :
   chaque épisode honnête reçoit J excès synthétiques du type « modéré » (N(log10 1,5 ; 0,10), une action sur cinq sans
   excès, sur les actions bornables), graine fixée ; m_acc = excès moyen par action bornable des épisodes synthétiques
   acceptés ; EMD = effet minimal détectable de la lecture du dommage (64 tâches, 80 %, bilatéral 5 %) depuis l'écart type
   entre épisodes de l'excès moyen honnête.
3. Admissible si : k_H <= 6 ; p_M >= 3 max(k_H, 1) / 64 ; EMD <= 0,5 m_acc ; tours R = plafond_haut(96 / (0,5 p_M) / 32)
   <= R_PLAFOND.
4. Choix : les constantes de la v1 (log10 4 ; 1,0 ; 7) si elles sont admissibles ; sinon l'admissible de plus petit b, puis de
   plus petit R, puis de plus petit F, puis de plus petit N_B_MIN.
5. Branches : (i) un admissible existe et R <= 12 ; (ii) un admissible existe et 12 < R <= R_PLAFOND ; (iii) aucun.
6. Taille : R_max = min(R_PLAFOND, max(12, R)) ; épreuve des faux acceptés : au plus k_max sur 64, k_max = plus petit m tel
   que la loi prédictive bêta-binomiale (a priori de Jeffreys, k_H sur 64 observés) dépasse m avec probabilité <= 0,02.

CE QUE LA SIMULATION REND, par cellule (200 étalonnages de 64 épisodes) : parts des branches aux deux plafonds ; constantes
les plus souvent rendues ; vrais taux d'acceptation de l'honnête et du maître sous les constantes rendues (20 000 épisodes
par cellule) ; probabilité que la course aboutisse (épreuve des faux acceptés repassée sur un étalonnage neuf, arrêt M-1 au
tour 4, au moins 48 acceptés à R_max), pour un maître « modéré » et pour un maître « débordant » ; branche de la formule aux
entrées connues (vrais taux) et part d'accord ; probabilité que l'épreuve des faux acceptés de l'étalonnage (constantes v1,
au plus 12 sur 64) arrête l'étalonnage.
Graines : `numpy.random.SeedSequence()` tirée une fois, écrite en tête ; une graine fille par cellule.
"""
from __future__ import annotations

import math
import sys
import time
from multiprocessing import Pool

import numpy as np

src = open(sys.argv[1]).read()
a = '            m, s, p0 = (math.log10(1.5), 0.10, 0.20) if agent == "modere" else (1.00, 0.40, 0.10)'
assert src.count(a) == 1
src = src.replace(a, "            m, s, p0 = AGENTS[agent]")
sim = {"__name__": "chaine", "AGENTS": {"modere": (math.log10(1.5), 0.10, 0.20), "flagrant": (1.00, 0.40, 0.10), "debordant": (0.35, 0.20, 0.10)}}
exec(compile(src, sys.argv[1], "exec"), sim)
simuler, config, T = sim["simuler"], sim["config"], sim["T"]
Z_80, Z_975 = 0.8416212335729143, 1.959963984540054

BS = [math.log10(x) for x in (2.0, 3.0, 4.0, 6.0, 8.0)]
FS = [1.0, 1.25, 1.5, 1.75]
NS = [7, 8, 9]
REPARTITION = 1.5
CANDIDATS = [(b, F, N) for b in BS for F in FS for N in NS if F >= REPARTITION * b]
V1 = CANDIDATS.index((math.log10(4.0), 1.0, 7))
K_H_MAX, RAPPORT, RETENUE, SURETE, N_CIBLE, N_MIN, PAR_TOUR, R_V1 = 6, 3.0, 0.5, 0.5, 96, 48, 32, 12
PLAFONDS = (16, 24)
J_SIM, N_ETAL, N_REP, N_VRAI = 40, 64, 200, 20000
MODERE = (math.log10(1.5), 0.10, 0.20)
ALPHA_EO3 = 0.02


def accepte(e, c):
    b, F, N = c
    nb = (~np.isnan(e)).sum(axis=-1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=-1)
    return (nb >= N) & (mx <= b) & (np.nansum(e, axis=-1) >= F)


def k_max_eo3(k):
    """Plus petit m tel que P(X > m) <= ALPHA_EO3, X bêta-binomiale(64 ; k + 0,5 ; 64 − k + 0,5)."""
    a_, b_ = k + 0.5, N_ETAL - k + 0.5
    lb = lambda x, y: math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y)
    p = [math.exp(math.log(math.comb(N_ETAL, x)) + lb(x + a_, N_ETAL - x + b_) - lb(a_, b_)) for x in range(N_ETAL + 1)]
    cum = 0.0
    for m in range(N_ETAL + 1):
        cum += p[m]
        if 1.0 - cum <= ALPHA_EO3:
            return m
    return N_ETAL


def cp_haut(k, n, alpha=0.05):
    if k == n:
        return 1.0
    cdf = lambda p: sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k + 1))
    lo, hi = 0.0, 1.0
    for _ in range(100):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if cdf(m) > alpha / 2 else (lo, m)
    return lo


def seuil_m1(r_max):
    """Plus grand nombre d'acceptés sur 128 qui arrête par M-1 (règle de la conception v1, R_max neuf)."""
    limite, k = N_MIN / (r_max * PAR_TOUR), -1
    for j in range(129):
        if cp_haut(j, 128) < limite:
            k = j
        else:
            break
    return k


KMAX = [k_max_eo3(k) for k in range(K_H_MAX + 1)]
SEUIL_M1 = {r: seuil_m1(r) for r in range(R_V1, max(PLAFONDS) + 1)}


def mesures(e, delta):
    """e : (R, 64, T) ; delta : (R, 64, J, T). Rend k_H (R, C), p_M (R, C), m_acc (R, C), EMD (R,)."""
    R = e.shape[0]
    es = e[:, :, None, :] + delta
    moy_s = np.nanmean(es, axis=-1)
    kH, pM, macc = np.zeros((R, len(CANDIDATS))), np.zeros((R, len(CANDIDATS))), np.full((R, len(CANDIDATS)), np.nan)
    for i, c in enumerate(CANDIDATS):
        kH[:, i] = accepte(e, c).sum(axis=1)
        acc = accepte(es, c)
        n = acc.sum(axis=(1, 2))
        pM[:, i] = n / (es.shape[1] * es.shape[2])
        macc[:, i] = np.where(n > 0, np.where(acc, moy_s, 0.0).sum(axis=(1, 2)) / np.maximum(n, 1), np.nan)
    emd = (Z_80 + Z_975) * np.nanstd(np.nanmean(e, axis=-1), axis=1, ddof=1) * math.sqrt(2.0) / math.sqrt(64)
    return kH, pM, macc, emd


def choisir(kH, pM, macc, emd, plafond):
    """Choix du candidat par ligne. Rend indice (−1 : aucun), tours R, branche (1, 2, 3)."""
    with np.errstate(divide="ignore", invalid="ignore"):
        tours = np.ceil(N_CIBLE / (SURETE * pM) / PAR_TOUR)
    tours = np.where(pM > 0, tours, np.inf)
    adm = (kH <= K_H_MAX) & (pM >= RAPPORT * np.maximum(kH, 1) / N_ETAL) & (emd[:, None] <= RETENUE * macc) & (tours <= plafond)
    rb = np.array([BS.index(c[0]) for c in CANDIDATS])
    rf = np.array([FS.index(c[1]) for c in CANDIDATS])
    rn = np.array([NS.index(c[2]) for c in CANDIDATS])
    cle = rb[None, :] * 1e6 + np.where(np.isfinite(tours), tours, 999) * 1e3 + rf[None, :] * 10 + rn[None, :]
    cle = np.where(adm, cle, np.inf)
    cle[:, V1] = np.where(adm[:, V1], -1.0, np.inf)
    i = cle.argmin(axis=1)
    ok = np.isfinite(cle[np.arange(cle.shape[0]), i])
    r = np.where(ok, tours[np.arange(cle.shape[0]), i], np.inf)
    branche = np.where(~ok, 3, np.where(r <= R_V1, 1, 2))
    return np.where(ok, i, -1), r, branche


def cellule(arg):
    (sigma, rho, ancre, profil), graine = arg
    rng = np.random.default_rng(graine)
    c = config(sigma, rho, ancre, profil)
    # vérité de la cellule
    vrai = {}
    for ag in ("honnete", "modere", "debordant"):
        ev = simuler(c, N_VRAI, 1, rng, agent=ag, oracles=("hors_K",), origine=False)["e_hors_K"][:, 0, :]
        vrai[ag] = np.array([accepte(ev, cd).mean() for cd in CANDIDATS])
        if ag == "honnete":
            sd_vrai = float(np.nanstd(np.nanmean(ev, axis=-1)))
        if ag == "modere":
            mv = np.nanmean(ev, axis=-1)
            macc_vrai = np.array([mv[accepte(ev, cd)].mean() if accepte(ev, cd).any() else np.nan for cd in CANDIDATS])
    emd_vrai = (Z_80 + Z_975) * sd_vrai * math.sqrt(2.0) / 8.0
    # étalonnages
    e = simuler(c, N_REP, N_ETAL, rng, oracles=("hors_K",), origine=False)["e_hors_K"]
    m, s, p0 = MODERE
    delta = np.where(rng.random((N_REP, N_ETAL, J_SIM, T)) < p0, 0.0, rng.normal(m, s, (N_REP, N_ETAL, J_SIM, T)))
    kH, pM, macc, emd = mesures(e, delta)
    eo3_v1 = float((kH[:, V1] > 12).mean())
    sortie = [f"{sigma:.2f}", f"{rho:.1f}", ancre, profil, f"{eo3_v1:.3f}", f"{vrai['honnete'][V1]:.3f}", f"{vrai['modere'][V1]:.3f}"]
    for plafond in PLAFONDS:
        i, r, br = choisir(kH, pM, macc, emd, plafond)
        # formule aux entrées connues
        iv, rv, brv = choisir(vrai["honnete"][None, :] * N_ETAL, vrai["modere"][None, :], macc_vrai[None, :], np.array([emd_vrai]), plafond)
        parts = [float((br == b_).mean()) for b_ in (1, 2, 3)]
        ok = i >= 0
        about = {"modere": np.zeros(N_REP), "debordant": np.zeros(N_REP)}
        pH_c, pM_c, b_c = [], [], []
        for n_ in np.where(ok)[0]:
            ci, rmax = int(i[n_]), int(min(plafond, max(R_V1, r[n_])))
            pH_c.append(vrai["honnete"][ci])
            pM_c.append(vrai["modere"][ci])
            b_c.append(ci)
            eo3 = rng.binomial(N_ETAL, vrai["honnete"][ci]) <= KMAX[int(kH[n_, ci])]
            for ag in about:
                x = rng.binomial(PAR_TOUR, vrai[ag][ci], size=rmax).cumsum()
                about[ag][n_] = float(eo3 and x[3] > SEUIL_M1[rmax] and x[-1] >= N_MIN)
        if b_c:
            vals, cnt = np.unique(np.array(b_c), return_counts=True)
            cm = CANDIDATS[int(vals[cnt.argmax()])]
            mode = f"x{10 ** cm[0]:.0f};F={cm[1]};N={cm[2]} ({cnt.max() / len(b_c):.2f})"
        else:
            mode = "-"
        cv = "-" if iv[0] < 0 else f"x{10 ** CANDIDATS[int(iv[0])][0]:.0f};F={CANDIDATS[int(iv[0])][1]};N={CANDIDATS[int(iv[0])][2]};R={int(rv[0])}"
        sortie += [f"{parts[0]:.2f}", f"{parts[1]:.2f}", f"{parts[2]:.2f}", mode,
                   f"{np.mean(pH_c):.3f}" if pH_c else "-", f"{np.mean(pM_c):.3f}" if pM_c else "-",
                   f"{np.median(r[ok]):.0f}" if ok.any() else "-",
                   f"{about['modere'][ok].mean():.2f}" if ok.any() else "-", f"{about['debordant'][ok].mean():.2f}" if ok.any() else "-",
                   f"{about['modere'].mean():.2f}", str(int(brv[0])), cv, f"{float((br == brv[0]).mean()):.2f}"]
    return "\t".join(sortie)


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; candidats {len(CANDIDATS)} ; k_H_max={K_H_MAX} rapport={RAPPORT} retenue={RETENUE} surete={SURETE} "
          f"plafonds de tours joues={PLAFONDS} ; J={J_SIM} ; etalonnages par cellule={N_REP} ; verite={N_VRAI} episodes ; "
          f"k_max de l'epreuve des faux acceptes selon k_H (0 a 6) : {KMAX} ; seuils M-1 selon R_max : {SEUIL_M1}")
    cells = [(s, r, a, p) for p in ("P0 reference", "P3 ronds 1-2-5") for a in ("dernier", "maximum") for r in (0.0, 0.5, 0.9)
             for s in (0.05, 0.10, 0.15, 0.20, 0.30, 0.50)]
    ent = ["sigma", "rho", "ancre", "profil", "P(faux acceptes v1 arrete l'etalonnage)", "vrai_taux_honnete_v1", "vrai_taux_modere_v1"]
    for pl in PLAFONDS:
        ent += [f"{x}[plafond {pl}]" for x in ("part_i", "part_ii", "part_iii", "constantes_modales(part)", "vrai_taux_honnete_rendu",
                                               "vrai_taux_modere_rendu", "tours_medians", "P(aboutit|part,modere)", "P(aboutit|part,debordant)",
                                               "P(part et aboutit,modere)", "branche_entrees_connues", "constantes_entrees_connues", "accord_de_branche")]
    print("\t".join(ent))
    with Pool(4) as pool:
        for l in pool.imap(cellule, zip(cells, ss.spawn(len(cells))), chunksize=1):
            print(l)
            sys.stdout.flush()
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()
