"""Cas (monde, carte) des essais de taille et de puissance — v1. Toutes les lois sont des fonctions du plan gelé."""
import numpy as np

import essai_projection_commun_v1 as cm


def seuil_hors_archive(rng, cut):
    while True:
        s = round(float(rng.choice([-1, 1]) * rng.uniform(0.3, 1.0)), 2)
        if cut is None or abs(s - cut) >= 0.3:
            return s


def construire(rng, cas):
    a = cm.tirer_archive(rng)
    z, g = cm.tirer_plan(rng)
    L = cm.lois_connues(a, z)
    cA, cB, c4 = cm.cellules_archive(a, z)
    S1, S2 = L[:, 0], L[:, 1]
    jA, jB = a["jA"], 1 - a["jA"]
    eyeK = np.eye(cm.K)

    def membre_lin(th):            # th : 4 poids de lois connues puis 3 lois certaines
        return np.einsum("j,njk->nk", th[:4], L) + th[4:][None]

    def neuf_global(delta):
        W1, b1 = a["S1"]
        Dl = rng.normal(size=(cm.K, cm.D))
        Dl -= Dl.mean(0, keepdims=True)
        return cm.p_softmax((W1 + delta * Dl, b1), z)

    nom, dose = cas if isinstance(cas, tuple) else (cas, None)
    carte = None
    if nom == "T01_copie_membre_lineaire":
        M = membre_lin(rng.dirichlet(np.ones(7)))
    elif nom == "T02_bord_une_loi_connue":
        M = L[:, int(rng.integers(0, 4))].copy()
    elif nom == "T03_poids_extremes":
        th = np.zeros(7); th[int(rng.integers(0, 4))] = 0.97; th[4 + int(rng.integers(0, 3))] = 0.03
        M = membre_lin(th)
    elif nom == "T04_bord_loi_aveugle_constante":
        M = np.broadcast_to(rng.dirichlet(np.ones(cm.K)), (cm.N, cm.K)).copy()
    elif nom == "T05_copie_coupure_archive":
        M = cm.si_sinon(cA == 1, S1, S2)
    elif nom == "T06_copie_coupure_hors_archive":
        j = int(rng.integers(0, 2)); s = seuil_hors_archive(rng, a["sA"] if j == jA else a["sB"])
        M = cm.si_sinon(z[:, j] > s, S1, S2)
    elif nom == "T07_copie_sous_population":
        M = cm.si_sinon(g == 0, S1, S2)
    elif nom == "T08_copie_coupure_archive_bruit_commun":
        M = 0.75 * cm.si_sinon(cA == 1, S1, S2) + 0.25 * rng.dirichlet(np.ones(cm.K))[None]
    elif nom == "T09_copie_deux_niveaux_archive":
        M = cm.si_sinon(cA == 1, cm.si_sinon(cB == 1, S1, S2), cm.si_sinon(cB == 1, S2, S1))
    elif nom == "T10_monde_coupure_carte_neuve":
        M = cm.si_sinon(cA == 1, S1, S2)
        carte = neuf_global(0.5)
    elif nom == "T11_monde_lineaire_carte_surconfiante":
        M = membre_lin(rng.dirichlet(np.ones(7)))
        carte = M ** 1.5 / (M ** 1.5).sum(1, keepdims=True)
    elif nom == "T12_monde_coupure_carte_autre_membre":
        M = cm.si_sinon(cA == 1, S1, S2)
        carte = S1.copy()
    elif nom == "V1_effet_neuf_global":
        M = neuf_global(dose)
    elif nom == "V3_conditionnelle_seuil_decentre":
        j = int(rng.integers(0, 2)); c = seuil_hors_archive(rng, a["sA"] if j == jA else a["sB"])
        W1, b1 = a["S1"]
        u = rng.normal(size=cm.K); u -= u.mean(); u /= np.linalg.norm(u)
        E = np.zeros((cm.K, cm.D)); E[:, 1 - j] = u
        M = cm.si_sinon(z[:, j] > c, cm.p_softmax((W1 + dose * E, b1), z), cm.p_softmax((W1 - dose * E, b1), z))
    elif nom == "V4_loi_neuve_sous_population":
        Nn = cm.p_softmax(cm.softmax_param(rng), z)
        M = cm.si_sinon(g == 0, S1, (1 - dose) * S1 + dose * Nn)
    else:
        raise ValueError(nom)
    M = M / M.sum(1, keepdims=True)
    Q = M if carte is None else carte / carte.sum(1, keepdims=True)
    y = cm.tirer_issues(rng, M)
    return dict(L=L, Q=Q, M=M, y=y, z=z, g=g, cA=cA, cB=cB, c4=c4, archive=a)
