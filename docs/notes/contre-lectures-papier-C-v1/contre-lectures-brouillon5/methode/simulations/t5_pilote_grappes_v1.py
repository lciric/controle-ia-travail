"""T5 : grandeurs de dessin du pilote (Metrique, point 18 ; Plan, section 2). Le texte estime l'erreur type de g_sep
« par reechantillonnage des contenus de calibrage (2 000 tirages) ». Au pilote, les contenus viennent de 16 taches,
plusieurs par tache (trois episodes par tache au pilote de T0.5, prereg/T0.5-pilote-8B-v1.md, l. 142). Une interaction
tache x formulation (eta, partagee par les contenus d'une tache) rend le reechantillonnage des contenus trop optimiste.
Consequence sur k_max(n) : formulations de gain vrai EGAL (aucune intensite graduee) ; P(k_max(n) >= 3), c'est-a-dire
reserve « niveaux non separables » absente a tort, avec l'erreur type par contenus (texte) et par taches (proposition).
Modele : 16 taches x 3 contenus (1 ou 2 saboteurs par tache, alternes) ; T = 2/4 + u_t (0,5) + N(0 ; 0,8) ; trois juges,
bruit d'insertion sigma = 0,4 ; v_f = T + 0,10 (0 - T) + eta_{t,f} + e ; 16 formulations, eta ~ N(0, s_eta).
B = 500 tirages (2 000 au texte).
"""
import sys

import numpy as np


def pentes(W, v0, D):
    """W : (B, n) poids ; v0 : (n,) ; D : (n, q). Renvoie -pente (B, q)."""
    sw = W.sum(1, keepdims=True)
    m0 = (W @ v0)[:, None] / sw
    v00 = (W @ (v0 * v0))[:, None] / sw - m0 ** 2
    mD = (W @ D) / sw
    c0D = (W @ (D * v0[:, None])) / sw - m0 * mD
    return -c0D / v00


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5C5).spawn(1)[0])
    Tt, par, B, R = 16, 3, 500, 400
    n = Tt * par
    tache = np.repeat(np.arange(Tt), par)
    sab = (np.arange(n) % 2).astype(float)
    print("s_eta | ET vraie (ecart type de g_sep entre essais) | ET med. par contenus | ET med. par taches |"
          " P(k_max(90) >= 3) contenus / taches | P(k_max(120) >= 3) contenus / taches")
    for s_eta in (0.0, 0.15, 0.30):
        gs, etc, ett, k90c, k90t, k120c, k120t = [], [], [], [], [], [], []
        for _ in range(R):
            u = rng.normal(0, 0.5, Tt)
            vrai = 2.0 + 2.0 * sab + u[tache] + rng.normal(0, 0.8, n)
            eta = rng.normal(0, s_eta, (Tt, 16))[tache]
            Dj, v0j = [], []
            gbar = np.zeros(16)
            for j in range(3):
                v0 = vrai + rng.normal(0, 0.4, n)
                vf = vrai[:, None] + 0.10 * (0.0 - vrai)[:, None] + eta + rng.normal(0, 0.4, (n, 16))
                D = vf - v0[:, None]
                gbar += pentes(np.ones((1, n)), v0, D)[0] / 3
                Dj.append(D)
                v0j.append(v0)
            gs.append(gbar[0])
            Wc = rng.multinomial(n, np.full(n, 1.0 / n), size=B).astype(float)
            Wt = rng.multinomial(Tt, np.full(Tt, 1.0 / Tt), size=B).astype(float)[:, tache]
            et = {}
            for nom, Wm in (("c", Wc), ("t", Wt)):
                gb = sum(pentes(Wm, v0j[j], Dj[j]) for j in range(3)) / 3
                et[nom] = np.median(gb.std(0, ddof=1))
            etc.append(et["c"])
            ett.append(et["t"])
            etendue = gbar.max() - gbar.min()
            for N, lc, lt in ((90, k90c, k90t), (120, k120c, k120t)):
                for nom, l in (("c", lc), ("t", lt)):
                    E = et[nom]
                    En = E * np.sqrt(n / N)
                    kmax = 1 + np.floor(max(0.0, etendue - 3.53 * E) / (1.96 * np.sqrt(2) * En))
                    l.append(kmax >= 3)
        print(f"{s_eta:.2f}  |  {np.std(gs, ddof=1):.4f}                                 |  {np.median(etc):.4f}             |"
              f"  {np.median(ett):.4f}           |  {np.mean(k90c):.3f} / {np.mean(k90t):.3f}                      |"
              f"  {np.mean(k120c):.3f} / {np.mean(k120t):.3f}")
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
