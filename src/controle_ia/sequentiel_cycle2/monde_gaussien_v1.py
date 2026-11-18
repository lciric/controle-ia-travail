"""Monde gaussien : les estimateurs de chaque dose suivent un mouvement brownien avec dérive, lu par tranches de tâches.

Il vérifie le calcul du risque (répartition entre lectures, doses, conjonction) quand les intervalles sont exacts ;
il ne dit rien du rééchantillonnage (monde à scores). Quatre plans sont joués sur les MÊMES trajectoires :
  « unique »   : une lecture, à l'effectif complet, aux niveaux du brouillon 3 ;
  « reparti »  : deux lectures, niveaux partagés par borne d'union (le plan proposé) ;
  « depense »  : deux lectures, frontière à dépense de risque de type O'Brien-Fleming (référence) ;
  « melange »  : processus e à mélange normal, lu à chaque tranche (référence « toujours valide ») ;
  « naif »     : deux lectures aux niveaux pleins, sans correction (artefact planté : il doit dépasser le niveau).
"""
from __future__ import annotations

import math

import numpy as np

from ..gardes import GardeArret
from . import etats_v1 as etats
from . import niveaux_v1 as niveaux

PLANS = ("unique", "reparti", "depense", "melange", "naif")
GRANDEURS = ("d_somme", "ecart", "d_maximum")


def _exiger_config(c: dict) -> None:
    cles = {"n_taches", "n_intermediaire", "pas_tranche", "erreur_type_64", "effets", "correlation_doses",
            "correlation_grandeurs", "marge", "part_intermediaire", "n_repliques"}
    if set(c) != cles:
        raise GardeArret(f"configuration du monde gaussien : clés attendues {sorted(cles)}, reçu {sorted(c)}")
    n, n1, pas = c["n_taches"], c["n_intermediaire"], c["pas_tranche"]
    if not (0 < n1 < n and n % pas == 0 and n1 % pas == 0):
        raise GardeArret("effectifs : 0 < intermédiaire < complet, tous deux multiples du pas de tranche")
    if set(c["erreur_type_64"]) != set(GRANDEURS) or set(c["effets"]) != set(GRANDEURS):
        raise GardeArret(f"erreurs types et effets attendus pour {GRANDEURS}")
    doses = {len(v) for v in c["effets"].values()}
    if len(doses) != 1 or doses == {0}:
        raise GardeArret("effets : une liste par grandeur, de même longueur non nulle (une valeur par dose)")
    if not (0.0 <= c["correlation_doses"] <= 1.0 and -0.9 <= c["correlation_grandeurs"] <= 0.9):
        raise GardeArret("corrélations hors bornes")


def _racine_covariance(n_doses: int, rho_doses: float, rho_grandeurs: float) -> np.ndarray:
    """Racine de la covariance (dose × grandeur) : produit de Kronecker de deux matrices équicorrélées."""
    a = np.full((n_doses, n_doses), rho_doses) + (1.0 - rho_doses) * np.eye(n_doses)
    b = np.full((3, 3), rho_grandeurs) + (1.0 - rho_grandeurs) * np.eye(3)
    cov = np.kron(a, b)
    valeurs, vecteurs = np.linalg.eigh(cov)
    if valeurs.min() < -1e-10:
        raise GardeArret("covariance non positive : corrélations incompatibles")
    return vecteurs * np.sqrt(np.clip(valeurs, 0.0, None))


def jouer(config: dict, graine: np.random.SeedSequence) -> dict:
    """Rend, par plan, le compte des états de cycle à l'intermédiaire, à la finale, et de leurs couples."""
    _exiger_config(config)
    c = config
    n, n1, pas, m = c["n_taches"], c["n_intermediaire"], c["pas_tranche"], c["marge"]
    n_doses = len(c["effets"]["ecart"])
    tranches = np.arange(pas, n + 1, pas)
    i1, i2 = int(np.searchsorted(tranches, n1)), len(tranches) - 1
    sigma_tache = np.array([c["erreur_type_64"][g] * 8.0 for g in GRANDEURS])     # écart type par tâche
    theta = np.array([[c["effets"][g][d] for g in GRANDEURS] for d in range(n_doses)])  # dose × grandeur
    racine = _racine_covariance(n_doses, c["correlation_doses"], c["correlation_grandeurs"])
    rng = np.random.default_rng(graine)
    q, qe, f = niveaux.Q_DECISIF, niveaux.Q_EQUIVALENCE, c["part_intermediaire"]
    t = n1 / n
    z = {"unique": (math.inf, niveaux.z_de(q)), "naif": (niveaux.z_de(q), niveaux.z_de(q)),
         "reparti": tuple(niveaux.z_de(x) for x in niveaux.repartir(q, f)), "depense": niveaux.bornes_depense(q, t)}
    ze = {"unique": (math.inf, niveaux.z_de(qe)), "naif": (niveaux.z_de(qe), niveaux.z_de(qe)),
          "reparti": tuple(niveaux.z_de(x) for x in niveaux.repartir(qe, f)), "depense": niveaux.bornes_depense(qe, t)}
    rho = (m / sigma_tache[1]) ** 2     # mélange réglé sur l'écart d'intérêt, en unités d'une tâche
    z_mel = np.array([niveaux.frontiere_melange(float(k), q, rho) for k in tranches])
    comptes = {p: {"intermediaire": {}, "finale": {}, "couple": {}} for p in PLANS}
    lot = 20000
    reste = c["n_repliques"]
    while reste > 0:
        r = min(lot, reste)
        reste -= r
        bruit = rng.standard_normal((r, len(tranches), n_doses * 3)) @ racine.T
        somme = np.cumsum(bruit * math.sqrt(pas), axis=1).reshape(r, len(tranches), n_doses, 3)
        est = theta[None, None] + sigma_tache[None, None, None] * somme / tranches[None, :, None, None]
        et = sigma_tache[None, None, None] / np.sqrt(tranches)[None, :, None, None]
        zz = est / et                      # écarts types au-dessus de 0
        zm = (est - m) / et                # écarts types au-dessus de la marge
        for plan in PLANS:
            if plan == "melange":
                haut = zz >= z_mel[None, :, None, None]
                bas = zz <= -z_mel[None, :, None, None]
                vues = []
                for fin in (i1, i2):
                    h, b = haut[:, : fin + 1].any(axis=1), bas[:, : fin + 1].any(axis=1)
                    faux = np.zeros((r, n_doses), dtype=bool)
                    vues.append({"c1": h[:, :, 0], "c2": h[:, :, 1], "c3": b[:, :, 1], "c4": h[:, :, 2],
                                 "c5": faux, "c6": faux})
                inter, cumul = vues
            else:
                lect = []
                for idx, k in ((i1, 0), (i2, 1)):
                    zk, zek = z[plan][k], ze[plan][k]
                    lect.append({"c1": zz[:, idx, :, 0] >= zk, "c2": zz[:, idx, :, 1] >= zk,
                                 "c3": zz[:, idx, :, 1] <= -zk, "c4": zz[:, idx, :, 2] >= zk,
                                 "c5": zm[:, idx, :, 0] <= -zek, "c6": zm[:, idx, :, 1] <= -zek})
                inter = lect[0]
                cumul = {a: lect[0][a] | lect[1][a] for a in etats.AFFIRMATIONS}
            e1 = etats.etats_cycle_vect(etats.etats_dose_vect(inter))
            e2 = etats.etats_cycle_vect(etats.etats_dose_vect(cumul))
            k = comptes[plan]
            for nom, tab in (("intermediaire", e1), ("finale", e2), ("couple", e1 * 10 + e2)):
                valeurs, nombres = np.unique(tab, return_counts=True)
                for v, nb in zip(valeurs.tolist(), nombres.tolist()):
                    cle = (etats.ETATS_CYCLE[v] if nom != "couple"
                           else f"{etats.ETATS_CYCLE[v // 10]}>{etats.ETATS_CYCLE[v % 10]}")
                    k[nom][cle] = k[nom].get(cle, 0) + nb
    return {"n_repliques": c["n_repliques"], "bornes_z": {p: list(z[p]) for p in z}, "comptes": comptes}
