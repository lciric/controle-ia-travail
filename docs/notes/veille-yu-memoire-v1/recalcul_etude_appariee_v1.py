"""Recalcul de l'etude appariee du codage de Yu et al. (2026), arXiv 2611.18856v1.

Source des donnees : tableau 3, page 8 du PDF empreinte
a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d.
Dix sources independantes (harnais Terminus-2 evolue sur Terminal-Bench 2.1),
chacune continuee deux fois sur Terminal-Bench 4 : sans memoire, avec memoire.
Annonces a verifier (page 8 et annexe C.4, page 20) : moyenne +2,36 ;
intervalle a 95 % [1,05 ; 3,68] ; t(9) = 4,06, p = 0,003 ; rangs signes
bilateral p = 0,006 (rangs moyens pour les ex aequo, 2^10 signes enumeres) ;
effet standardise apparie 1,28 ; 9 paires sur 10 en faveur de la memoire.

Aucun appel de modele, aucun reseau, aucun alea : le calcul est deterministe.
"""
import itertools
import math
import sys

import numpy as np
import scipy
from scipy import stats

# (course, depart, sans memoire, avec memoire, difference imprimee) -- tableau 3, p. 8
TABLEAU_3 = [
    (1, 18.18, 20.61, 22.42, +1.81),
    (2, 16.97, 17.58, 19.39, +1.81),
    (3, 17.58, 20.00, 20.61, +0.61),
    (4, 18.18, 18.18, 23.64, +5.46),
    (5, 17.58, 18.79, 20.61, +1.82),
    (6, 19.39, 20.00, 23.64, +3.64),
    (7, 18.79, 20.00, 21.82, +1.82),
    (8, 18.18, 20.00, 19.39, -0.61),
    (9, 19.39, 18.18, 23.03, +4.85),
    (10, 19.39, 20.00, 22.42, +2.42),
]
ANNONCE = dict(moyenne=2.36, ic=(1.05, 3.68), t=4.06, p_t=0.003, p_rangs=0.006, dz=1.28,
               moy_depart=18.36, moy_sans=19.33, moy_avec=21.70)
N_DEROULES = 165  # 33 taches retenues x 5 deroules, tableau 4, p. 18


def t_apparie(d):
    d = np.asarray(d, float)
    n = len(d)
    m = d.mean()
    s = d.std(ddof=1)
    t = m / (s / math.sqrt(n))
    p = 2 * stats.t.sf(abs(t), n - 1)
    demi = stats.t.ppf(0.975, n - 1) * s / math.sqrt(n)
    return dict(n=n, moyenne=m, ecart_type=s, t=t, p=p, ic=(m - demi, m + demi), dz=m / s)


def rangs_signes_exact(d):
    """Test des rangs signes bilateral exact : rangs moyens pour les ex aequo,
    enumeration des 2^n affectations de signes (aucune difference nulle ici)."""
    d = np.asarray(d, float)
    assert not np.any(d == 0)
    rangs = stats.rankdata(np.abs(d), method="average")
    w_plus = rangs[d > 0].sum()
    total = rangs.sum()
    centre = total / 2
    ecart_obs = abs(w_plus - centre)
    n_ext = 0
    n_tot = 0
    for signes in itertools.product((0, 1), repeat=len(d)):
        w = sum(r for r, s in zip(rangs, signes) if s)
        n_tot += 1
        if abs(w - centre) >= ecart_obs - 1e-12:
            n_ext += 1
    return dict(w_plus=w_plus, w_moins=total - w_plus, rangs=rangs.tolist(),
                n_extremes=n_ext, n_total=n_tot, p=n_ext / n_tot)


def signe_exact(d):
    d = np.asarray(d, float)
    k = int((d > 0).sum())
    n = int((d != 0).sum())
    return k, n, stats.binomtest(k, n, 0.5).pvalue


def permutation_signes_moyenne(d):
    """Test de permutation exact sur la moyenne (2^n retournements de signe)."""
    d = np.asarray(d, float)
    obs = abs(d.mean())
    n_ext = 0
    for signes in itertools.product((-1, 1), repeat=len(d)):
        if abs((d * np.array(signes)).mean()) >= obs - 1e-12:
            n_ext += 1
    return n_ext, 2 ** len(d), n_ext / 2 ** len(d)


def ligne(*a):
    print(*a)


def main():
    ligne("Versions : python", sys.version.split()[0], "; numpy", np.__version__, "; scipy", scipy.__version__)
    depart = np.array([r[1] for r in TABLEAU_3])
    sans = np.array([r[2] for r in TABLEAU_3])
    avec = np.array([r[3] for r in TABLEAU_3])
    d_imprime = np.array([r[4] for r in TABLEAU_3])
    d_scores = np.round(avec - sans, 2)

    ligne("\n== 1. Coherence interne du tableau 3 (p. 8) ==")
    ligne("course  depart  sans   avec   diff_imprimee  avec-sans  ecart  diff_en_deroules(x165/100)")
    for r, ds in zip(TABLEAU_3, d_scores):
        ligne(f"{r[0]:>4}   {r[1]:6.2f} {r[2]:6.2f} {r[3]:6.2f}   {r[4]:+6.2f}        {ds:+6.2f}   {r[4]-ds:+5.2f}   {r[4]*N_DEROULES/100:+6.2f}")
    ligne(f"moyennes : depart {depart.mean():.3f} (annonce {ANNONCE['moy_depart']}), sans {sans.mean():.3f} "
          f"(annonce {ANNONCE['moy_sans']}), avec {avec.mean():.3f} (annonce {ANNONCE['moy_avec']})")
    ligne(f"ecart maximal entre difference imprimee et difference des scores : {np.abs(d_imprime - d_scores).max():.2f}")
    ligne("un deroule vaut 100/165 =", round(100 / N_DEROULES, 4), "point ; scores en nombre de deroules reussis sur 165 :")
    ligne("  depart :", [round(x * N_DEROULES / 100, 2) for x in depart])
    ligne("  sans   :", [round(x * N_DEROULES / 100, 2) for x in sans])
    ligne("  avec   :", [round(x * N_DEROULES / 100, 2) for x in avec])

    for nom, d in (("differences imprimees du tableau 3", d_imprime),
                   ("differences recalculees avec - sans (scores a deux decimales)", d_scores)):
        ligne(f"\n== 2. Test t apparie, {nom} ==")
        r = t_apparie(d)
        ligne(f"n = {r['n']} ; moyenne = {r['moyenne']:.4f} ; ecart-type (n-1) = {r['ecart_type']:.4f}")
        ligne(f"t({r['n']-1}) = {r['t']:.4f} ; p bilateral = {r['p']:.5f}")
        ligne(f"intervalle a 95 % = [{r['ic'][0]:.4f} ; {r['ic'][1]:.4f}] ; effet standardise apparie = {r['dz']:.4f}")
        sp = stats.ttest_1samp(d, 0.0)
        ligne(f"controle scipy.stats.ttest_1samp : t = {sp.statistic:.4f}, p = {sp.pvalue:.5f}")
        w = rangs_signes_exact(d)
        ligne(f"rangs signes exact : rangs = {w['rangs']} ; W+ = {w['w_plus']}, W- = {w['w_moins']} ; "
              f"{w['n_extremes']} affectations aussi extremes sur {w['n_total']} ; p bilateral = {w['p']:.5f}")
        k, n, ps = signe_exact(d)
        ligne(f"test du signe exact : {k} positives sur {n} ; p bilateral = {ps:.5f}")
        ne, nt, pp = permutation_signes_moyenne(d)
        ligne(f"permutation exacte des signes sur la moyenne : {ne} sur {nt} ; p bilateral = {pp:.5f}")

    d = d_imprime
    r = t_apparie(d)
    w = rangs_signes_exact(d)
    ligne("\n== 3. Annonce contre recalcul (differences imprimees) ==")
    for nom, a, b in (("moyenne", ANNONCE["moyenne"], r["moyenne"]),
                      ("borne basse de l'intervalle", ANNONCE["ic"][0], r["ic"][0]),
                      ("borne haute de l'intervalle", ANNONCE["ic"][1], r["ic"][1]),
                      ("t(9)", ANNONCE["t"], r["t"]),
                      ("p du test t", ANNONCE["p_t"], r["p"]),
                      ("p des rangs signes", ANNONCE["p_rangs"], w["p"]),
                      ("effet standardise apparie", ANNONCE["dz"], r["dz"])):
        dec = 3 if nom.startswith("p ") else 2
        ok = "concorde" if round(b, dec) == round(a, dec) else "DIFFERE"
        ligne(f"{nom:32s} annonce {a:<7} recalcul {b:.4f}  -> {ok} a {dec} decimales")

    ligne("\n== 4. Retrait d'une paire a la fois ==")
    ligne("retiree  moyenne  t(8)    p_t      ic95_bas ic95_haut  dz     p_rangs_exact  positives")
    for i in range(len(d)):
        dd = np.delete(d, i)
        rr = t_apparie(dd)
        ww = rangs_signes_exact(dd)
        ligne(f"{i+1:>5}    {rr['moyenne']:.3f}   {rr['t']:.3f}  {rr['p']:.5f}  {rr['ic'][0]:7.3f}  {rr['ic'][1]:7.3f}   "
              f"{rr['dz']:.3f}  {ww['p']:.5f}        {(dd>0).sum()}/{len(dd)}")
    ligne("retrait des deux plus grandes differences (courses 4 et 9) :")
    dd = np.delete(d, [3, 8])
    rr = t_apparie(dd)
    ww = rangs_signes_exact(dd)
    ligne(f"  n = 8 ; moyenne = {rr['moyenne']:.3f} ; t(7) = {rr['t']:.3f} ; p = {rr['p']:.5f} ; "
          f"ic = [{rr['ic'][0]:.3f} ; {rr['ic'][1]:.3f}] ; rangs signes exact p = {ww['p']:.5f}")

    ligne("\n== 5. Ce que la difference pese en deroules, et le bruit d'execution ==")
    ligne(f"difference moyenne = {r['moyenne']:.3f} point = {r['moyenne']*N_DEROULES/100:.2f} deroules sur {N_DEROULES}")
    p_moy = (sans.mean() + avec.mean()) / 200
    et_binom = 100 * math.sqrt(2 * p_moy * (1 - p_moy) / N_DEROULES)
    ligne(f"borne haute du bruit d'execution sur une difference, si les 165 deroules etaient independants et de meme "
          f"probabilite {p_moy:.3f} : ecart-type = {et_binom:.2f} points")
    ligne(f"ecart-type observe des dix differences : {r['ecart_type']:.2f} points "
          f"(rapport observe/borne = {r['ecart_type']/et_binom:.2f})")
    ligne("lecture : la borne suppose des taches toutes egales ; des taches presque toujours reussies ou presque toujours "
          "ratees donnent un bruit plus petit. Sans les resultats par tache, on ne peut pas dire lequel des deux regimes tient.")

    ligne("\n== 6. Gains depuis le depart commun (descriptif) ==")
    g_sans = sans - depart
    g_avec = avec - depart
    ligne("gain sans memoire :", np.round(g_sans, 2).tolist(), "moyenne", round(g_sans.mean(), 3))
    ligne("gain avec memoire :", np.round(g_avec, 2).tolist(), "moyenne", round(g_avec.mean(), 3))
    rs = t_apparie(g_sans)
    ligne(f"gain sans memoire contre zero : t(9) = {rs['t']:.3f}, p = {rs['p']:.5f}, ic = [{rs['ic'][0]:.3f} ; {rs['ic'][1]:.3f}]")
    ligne(f"correlation depart / difference : {np.corrcoef(depart, d)[0,1]:.3f} ; "
          f"correlation sans / avec : {np.corrcoef(sans, avec)[0,1]:.3f}")


if __name__ == "__main__":
    main()
