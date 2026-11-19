"""S2 : regression vers la moyenne avec des lectures deterministes ; loi temoin ; placebo par permutation ; W.

Le brouillon 4 (metrique, point 10) ecrit : « La lecture est deterministe (aucun tirage) : la regression vers la
moyenne par bruit de mesure n'y joue pas comme dans P1 ». Contre-hypothese : une lecture deterministe garde une
interaction contenu x condition (toute insertion, meme neutre, deplace la lecture d'un contenu de facon propre a ce
contenu) ; v0 porte donc une erreur e_i0 qui entre aussi dans Delta = v_m - v0 avec le signe moins.
Modele : v_{i,cond} = T_i + h_cond(T_i) + e_{i,cond}, e independants de sd sigma_e ; temoins : h = 0 ;
attaque : h_m(T) = g_m (c - T). v* = 0, moyenne de T = 3, sd de T environ 1,37.
Estimateurs compares :
  (B4) loi jointe du brouillon 4 : Delta = v_m - v0 sur v0 ;
  (TEM) loi « nette du temoin » : Delta_a = v_m - v_tau(m) sur v0 (sans correction d'attenuation) ;
  (TEM+CAL) meme sortie, regresseur calibre X* = v0bar + rho (v0 - v0bar), rho = cov(v0, wbar) / var(v0),
           wbar = moyenne des lectures temoins du contenu ; tout est recalcule dans chaque tirage.
"""
import sys

import numpy as np

from commun_v1 import comptes_bootstrap, loi_jointe, p_inf, p_sup

V_ETOILE = 0.0
MU = 3.0


def simule(rng, T, sd_e, g, lam, k=3):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    n = 2 * T
    c = MU + lam * (V_ETOILE - MU)
    gm = g * np.linspace(0.5, 1.5, k)
    v0 = vrai + rng.normal(0, sd_e, n)
    vm = vrai[:, None] + (c - vrai)[:, None] * gm[None, :] + rng.normal(0, sd_e, (n, k))
    vt = vrai[:, None] + rng.normal(0, sd_e, (n, k))  # un temoin par rang
    return v0, vm, vt, tache


def sommes(Y, X, tache, T, extra=None):
    k = Y.shape[1]
    s = dict(
        cnt=np.bincount(tache, minlength=T).astype(float),
        S1=np.bincount(tache, weights=X, minlength=T),
        S2=np.bincount(tache, weights=X * X, minlength=T),
        A=np.stack([np.bincount(tache, weights=Y[:, m], minlength=T) for m in range(k)], 1),
        B=np.stack([np.bincount(tache, weights=Y[:, m] * X, minlength=T) for m in range(k)], 1),
    )
    if extra:
        for cle, val in extra.items():
            s[cle] = np.bincount(tache, weights=val, minlength=T)
    return s


def agrege(s, W=None):
    return {c: (v.sum(0) if W is None else W @ v) for c, v in s.items()}


def calibre(sa):
    """Regression de calibrage : remplace v0 par X* = v0bar + rho (v0 - v0bar) dans les sommes."""
    n, S1, S2 = sa["cnt"], sa["S1"], sa["S2"]
    vbar = S1 / n
    var_v0 = S2 / n - vbar ** 2
    wbar = sa["Sw"] / n
    cov = sa["Svw"] / n - vbar * wbar
    rho = np.clip(cov / var_v0, 0.05, 1.0)
    a = (1 - rho) * vbar
    out = dict(sa)
    out["S1"] = n * vbar
    out["S2"] = n * a ** 2 + 2 * a * rho * S1 + rho ** 2 * S2
    out["B"] = a[..., None] * sa["A"] + rho[..., None] * sa["B"]
    return out, rho


def verdicts(bs, est, alpha=0.025):
    lam_b = (bs["c"] - bs["v0bar"]) / (V_ETOILE - bs["v0bar"])
    lam = (est["c"] - est["v0bar"]) / (V_ETOILE - est["v0bar"])
    positif = p_sup(bs["G"], 0.0) <= alpha
    ident = positif and bs["deg"].mean() <= 0.01
    return dict(
        G=float(est["G"]), positif=bool(positif), ident=bool(ident), lam=float(lam),
        cible=bool(ident and p_sup(lam_b, 0.5) <= alpha), moyenne=bool(ident and p_inf(lam_b, 0.5) <= alpha),
        G_hi=float(np.percentile(bs["G"], 97.5)),
    )


def un_essai(rng, T, sd_e, g, lam, B):
    v0, vm, vt, tache = simule(rng, T, sd_e, g, lam)
    W = comptes_bootstrap(rng, T, B)
    wbar = vt.mean(1)
    out = {}
    # (B4)
    s = sommes(vm - v0[:, None], v0, tache, T)
    out["B4"] = verdicts(loi_jointe(agrege(s, W)), loi_jointe(agrege(s)))
    # loi temoin du brouillon (temoins a la place des formulations)
    s_t = sommes(vt - v0[:, None], v0, tache, T)
    out["TEMOIN_B4"] = verdicts(loi_jointe(agrege(s_t, W)), loi_jointe(agrege(s_t)))
    # (TEM)
    s2 = sommes(vm - vt, v0, tache, T, extra=dict(Sw=wbar, Svw=v0 * wbar))
    out["TEM"] = verdicts(loi_jointe(agrege(s2, W)), loi_jointe(agrege(s2)))
    # (TEM+CAL)
    cb, _ = calibre(agrege(s2, W))
    ce, rho = calibre(agrege(s2))
    out["TEMCAL"] = verdicts(loi_jointe(cb), loi_jointe(ce))
    out["rho"] = float(rho)
    # placebo par permutation (C12), loi separee du rang le plus fort : echange au hasard, dans chaque contenu,
    # la lecture « sans » et la lecture « avec » ; on compare au g observe de la meme loi separee
    ech = rng.random(len(v0)) < 0.5
    a0 = np.where(ech, vm[:, -1], v0)
    a1 = np.where(ech, v0, vm[:, -1])
    sp = sommes((a1 - a0)[:, None], a0, tache, T)
    so = sommes((vm[:, -1] - v0)[:, None], v0, tache, T)
    out["PLACEBO"] = float(loi_jointe(agrege(sp))["G"])
    out["OBS_RANG_FORT"] = float(loi_jointe(agrege(so))["G"])
    return out


def resume(L, cle):
    f = lambda x: np.mean([r[cle][x] for r in L])
    return (f("positif"), np.median([r[cle]["G"] for r in L]), np.median([r[cle]["lam"] for r in L]), f("cible"),
            f("moyenne"), f("G_hi") if False else np.mean([r[cle]["G_hi"] < 0.10 for r in L]))


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C2B).spawn(1)[0])
    B, R = 1000, 300
    print("S2 - colonnes : P(famille positive) ; mediane de Gbar ; mediane de lambda ; P(« vers la cible ») ; P(« vers la moyenne ») ;"
          " P(borne haute 95 % de Gbar < 0,10)")
    for g, lam, titre in ((0.0, 0.0, "AUCUNE attaque (insertion neutre seulement) : g vrai = 0"),
                          (0.05, 1.0, "attaque vers la cible, g = 0,05, lambda vrai = 1"),
                          (0.10, 1.0, "attaque vers la cible, g = 0,10, lambda vrai = 1"),
                          (0.10, 0.5, "attaque, g = 0,10, lambda vrai = 0,5 (frontiere)")):
        print()
        print("==", titre)
        print("T     sd_e  rho_med | B4: P(pos) Gmed  lam_med P(cib) P(moy) P(hi<.1) | TEM+CAL: P(pos) Gmed lam_med P(cib) P(moy) | "
              "TEM sans calibrage: lam_med | temoin du B4: P(pos) Gmed | rang fort: g obs. med / g placebo med")
        for T in (30, 60, 120):
            for sd_e in (0.2, 0.4, 0.6):
                L = [un_essai(rng, T, sd_e, g, lam, B) for _ in range(R)]
                a = resume(L, "B4")
                c = resume(L, "TEMCAL")
                t = resume(L, "TEMOIN_B4")
                tm = resume(L, "TEM")
                print(f"{T:>4}  {sd_e:.1f}   {np.median([r['rho'] for r in L]):.3f}  |  {a[0]:.3f}  {a[1]:+.3f}  {a[2]:+.3f}  {a[3]:.3f}  {a[4]:.3f}  {a[5]:.3f}  |"
                      f"  {c[0]:.3f}  {c[1]:+.3f}  {c[2]:+.3f}  {c[3]:.3f}  {c[4]:.3f}  |  {tm[2]:+.3f}  |  {t[0]:.3f}  {t[1]:+.3f}  |"
                      f"  {np.median([r['OBS_RANG_FORT'] for r in L]):+.3f} / {np.median([r['PLACEBO'] for r in L]):+.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
