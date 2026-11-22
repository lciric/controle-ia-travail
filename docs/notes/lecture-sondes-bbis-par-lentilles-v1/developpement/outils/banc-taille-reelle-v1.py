"""Banc sans données, à la taille réelle : matrices aléatoires (aucun modèle, aucune sonde, aucune lentille réelle).
Partie 1 : temps et mémoire d'une couche, deux vecteurs, deux lentilles. Partie 2 : taux de p ≤ 0,05 des témoins (lentille des
logits), et la même statistique calculée sans u_j dans la moyenne et l'écart type (diagnostic seulement, non codé dans le paquet).
Lancer depuis la racine du dépôt : PYTHONPATH=src python docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/banc-taille-reelle-v1.py"""
import resource
import time
from types import SimpleNamespace

import numpy as np
import torch

from controle_ia.lentilles_sondes_bbis import audits_v1 as au
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K
from controle_ia.lentilles_sondes_bbis import lanceur_v1 as la
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu
from controle_ia.lentilles_sondes_bbis import statistiques_v1 as st

T, D, F, M, N = 89498, 4096, 14336, 2000, 4000


def partie_1():
    torch.manual_seed(0)
    wu, gamma = torch.randn(T, D) * 0.02, 1 + 0.1 * torch.randn(D)
    mats = {c: (torch.eye(D) + 0.02 * torch.randn(D, D)).half().numpy() for c in K.COUCHES}
    pub = le.LentillePublique(mats, {c: le.empreinte_matrice(m) for c, m in mats.items()})
    wd = torch.randn(D, F) * 0.01

    class Charge(la.Charge):
        def w_down(self, couche):
            return wd
    ids = np.arange(T) + 100
    ids[5] = 128000
    charge = Charge(wu, gamma, ids, [f" m{i}" for i in range(T)], pub, None, {}, None)
    rng = np.random.default_rng(0)
    sondes = [SimpleNamespace(cellule="P-S25", pli=f"e{i}", role="sonde", cle=f"P-S25/e{i}/sonde") for i in range(2)]
    vecteurs = [(s, "w", rng.standard_normal(D) * np.geomspace(0.01, 100, D)) for s in sondes]
    horloge = SimpleNamespace(controler=lambda e="": None)
    tab = {}
    t0 = time.time()
    couche = la._Couche(15, vecteurs, charge, nu.Graines(), la.Reglages(), st.masques_familles(charge.chaines), tab, horloge, lambda: None)
    resume, _ = couche.calculer()
    print("partie 1 : une couche, deux vecteurs, deux lentilles :", round(time.time() - t0, 1), "s ; pointe mémoire",
          round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2), "Go ; tableaux gardés",
          round(sum(a.nbytes for a in tab.values()) / 1e6, 1), "Mo")
    print("calibration (compte, q_bas, q_haut, tenue) :", {l: {n: (c["compte_p_sous_0_05"], c["q_bas"], c["q_haut"], c["tenue"])
                                                           for n, c in v["calibration"].items()} for l, v in resume["lentilles"].items()})


def partie_2():
    torch.manual_seed(1)
    wu, gamma = torch.randn(T, D) * 0.02, 1 + 0.1 * torch.randn(D)
    g = nu.Graines()
    v = np.random.default_rng(3).standard_normal(D) * np.geomspace(0.01, 100, D)

    def taux(nul, temoins, nom):
        a, _ = le.lire(torch.from_numpy(nul), None, gamma, wu)
        r = st.resumer_nul(a, {})
        s, _ = le.lire(torch.from_numpy(temoins), None, gamma, wu)
        p = st.p_temoins(s, r)
        c_t = st.concentrations_temoins(s, r)
        m, sd = r.moyenne[:, None], r.ecart_type[:, None]
        m_sans = (M * m - a) / (M - 1)
        var_sans = (M * sd ** 2 - (a - m) ** 2 * M / (M - 1)) / (M - 1)
        c_sans = ((a - m_sans) / var_sans.sqrt()).max(0).values
        p_sans = (1 + (c_sans[None, :] >= c_t[:, None]).sum(1)).double() / (M + 1)
        print(f"partie 2 : {nom} : {int((p <= 0.05).sum())} sur {len(p)} témoins à p ≤ 0,05 ({(p <= 0.05).mean():.4f} ; attendu "
              f"{100 / 2001:.4f}) ; sans u_j dans la moyenne et l'écart type : {float((p_sans <= 0.05).double().mean()):.4f}")
        return float((p <= 0.05).mean())
    arg = ("P-S25", "e0", "sonde", "w")
    ti = taux(nu.nul_isotrope(g, 7, D, M), nu.temoins_isotropes(g, 7, D, N), "nul isotrope")
    ts = taux(nu.nul_signes(g, v, *arg, M), nu.temoins_signes(g, v, 7, *arg, N), "nul des signes")
    for nom, jeux, tx in (("isotrope, un jeu de 1 000", [1000], ti), ("signes, 6 vecteurs", [200] * 6, ts),
                          ("signes, 13 vecteurs", [200] * 13, ts), ("signes, 20 vecteurs", [200] * 20, ts)):
        print(f"partie 2 : {nom} : bornes {au.bornes_calibration(jeux)}, compte attendu au taux mesuré {sum(jeux) * tx:.1f}")


if __name__ == "__main__":
    partie_1()
    partie_2()
