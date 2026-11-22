"""Version 3 : `lanceur_v4` et `statistiques_v3` (code de l'addendum de concentration scellé : directions nulles jugées sans
elles-mêmes, garde d'égalité au vingtième rang).
Banc sans données, à la taille réelle : matrices aléatoires (aucun modèle, aucune sonde, aucune lentille réelle). Temps et
mémoire d'une couche, deux vecteurs, deux lentilles ; compte des lignes de sortie égales (montage) ; comptes de la garde
d'égalité (directions nulles marquées, témoins à égalité). Ce ne sont pas des résultats du programme.
Lancer depuis la racine du dépôt : PYTHONPATH=src python docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/banc-taille-reelle-v3.py"""
import os
import resource
import time
from datetime import datetime, timezone
from types import SimpleNamespace

import numpy as np
import torch

from controle_ia.lentilles_sondes_bbis import constantes_v1 as K
from controle_ia.lentilles_sondes_bbis import lanceur_v4 as la
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as st

T, D, F = 89498, 4096, 14336


def principal():
    print("commande : PYTHONPATH=src python docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/banc-taille-reelle-v3.py ;",
          datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), ";", os.cpu_count(), "fils ; lanceur_v4 et statistiques_v3 ; torch",
          torch.__version__, "; numpy", np.__version__)
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
    t0 = time.time()
    print("montage : lignes de sortie égales :", st.paires_de_lignes_egales(wu.numpy()), ";", round(time.time() - t0, 1), "s ; pointe mémoire",
          round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2), "Go")
    rng = np.random.default_rng(0)
    sondes = [SimpleNamespace(cellule="P-S25", pli=f"e{i}", role="sonde", cle=f"P-S25/e{i}/sonde") for i in range(2)]
    vecteurs = [(s, "w", rng.standard_normal(D) * np.geomspace(0.01, 100, D)) for s in sondes]
    horloge = SimpleNamespace(controler=lambda e="": None)
    tab = {}
    t0 = time.time()
    couche = la._Couche(15, vecteurs, charge, nu.Graines(), la.Reglages(), st.masques_familles(charge.chaines), tab, horloge, lambda: None)
    resume, _ = couche.calculer()
    print("une couche, deux vecteurs, deux lentilles :", round(time.time() - t0, 1), "s ; pointe mémoire",
          round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2), "Go ; tableaux gardés",
          round(sum(a.nbytes for a in tab.values()) / 1e6, 1), "Mo")
    print("calibration (compte, q_bas, q_haut, tenue) :", {l: {n: (c["compte_p_sous_0_05"], c["q_bas"], c["q_haut"], c["tenue"])
                                                           for n, c in v["calibration"].items()} for l, v in resume["lentilles"].items()})
    print("garde d'égalité au vingtième rang :", {l: v["egalites_au_vingtieme_rang"] for l, v in resume["lentilles"].items()})


if __name__ == "__main__":
    principal()
