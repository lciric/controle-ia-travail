"""Compléments de la conception « monde riche et doublons » après lecture de la synthèse du collisionneur sur la diversité
des idées (`docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md`, `4f99077b…`, non contre-lue) — v1.

Concepteur neuf (Claude Opus 5.5), 12 novembre 2026. Aucun appel, aucun réseau. N'écrase ni ne modifie
`monde_riche_outils_v1.py` (scellé) : il l'importe.

- `strates` et `distance_stratifiee` : la distance au nul de l'étape A, ajustée globalement, puis lue **au maximum par strate
  publique** (sous-population × octile de chaque trait : 3 × 8 × 8 = 192 strates qui se chevauchent) ; une différence
  confinée à une région rare (par exemple z_t > 1) ne s'efface plus dans la moyenne globale (rang 2 de la synthèse).
- `grouper_stratifie` : liaison complète sur d = min des deux projections, **et** d_strat sous ε_strat.
- `medoide` : représentant d'un groupe fixé **avant tout tirage** (le membre qui minimise sa plus grande distance aux autres ;
  égalités : empreinte de la forme canonique), jamais par la plus grande valeur e (rang 2, objection de [A-T2]).
- `n_effectif_hellinger` : N_eff = k² / ‖K‖²_F sur le noyau de Hellinger moyen K_ij = E_x Σ_y √(p_i p_j) (semi-défini
  positif), mesure secondaire sans oracle (section 2 de la synthèse) : vaut 1 pour k lois égales, k pour k lois très
  différentes.
- `couverture` : composantes plantées couvertes par au moins une loi d'un ensemble (propositions brutes, représentants,
  retenues), **additionnelles** à l'archive de départ de la génération (mesure principale de la synthèse, section 2).
"""

import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import monde_riche_outils_v1 as M  # noqa: E402


OCTILES = (-np.inf, -1.150349, -0.674490, -0.318639, 0.0, 0.318639, 0.674490, 1.150349, np.inf)  # loi normale centrée réduite


def strates(Z, G, nsp, bornes=OCTILES):
    """Masques booléens des strates publiques : sous-population g × octile du trait j (bornes de la loi normale publique des
    traits) ; 3 × 8 × 8 = 192 strates qui se chevauchent ; une strate de moins de 20 instances de référence est ignorée."""
    out = []
    for g in range(nsp):
        for j in range(Z.shape[1]):
            for q in range(len(bornes) - 1):
                m = (G == g) & (Z[:, j] > bornes[q]) & (Z[:, j] <= bornes[q + 1])
                if m.sum() >= 20:
                    out.append(m)
    return out


def _projection(Ph, Pa):
    """Meilleur membre (au sens de E_x KL(h ‖ m)) du nul engendré par a : a seule, a mêlée à une loi aveugle, a tempérée."""
    n = Ph.shape[0]
    _, w = M.ajuste_lineaire_doux(Ph, [Pa], iterations=3000, tol=1e-8)
    M_lin = np.maximum(w[0] * Pa + np.tile(w[1:], (n, 1)), M.PLANCHER)
    _, th = M.ajuste_log_doux(Ph, Pa)
    S = th[0] * np.log(np.maximum(Pa, M.PLANCHER)) + np.concatenate([[0.0], th[1:]])[None, :]
    M_log = np.exp(S - M._lse(S)[:, None])
    cands = [M_lin, M_log, Pa]
    kl = [M._kl_moyen(Ph, C) for C in cands]
    return cands[int(np.argmin(kl))], min(kl)


def distance_stratifiee(Ph, Pa, masques):
    """(globale, maximum par strate) de E KL(h ‖ m*), m* ajusté globalement."""
    Mx, d = _projection(Ph, Pa)
    kl = (Ph * (np.log(np.maximum(Ph, M.PLANCHER)) - np.log(np.maximum(Mx, M.PLANCHER)))).sum(axis=1)
    return d, max(float(kl[m].mean()) for m in masques)


def matrices_stratifiees(lois, Zref, Gref, nsp):
    N = len(lois)
    Ps = [M.probas(l, Zref, Gref) for l in lois]
    can = [M.empreinte(M.forme_canonique(l)) for l in lois]
    msk = strates(Zref, Gref, nsp)
    dg, ds = np.zeros((N, N)), np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j and can[i] != can[j]:
                dg[i, j], ds[i, j] = distance_stratifiee(Ps[i], Ps[j], msk)
    # paire : la direction (i → j ou j → i) de plus petite distance globale, et sa lecture par strate
    d, dstr = np.zeros((N, N)), np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j or can[i] == can[j]:
                continue
            a, b = (i, j) if dg[i, j] <= dg[j, i] else (j, i)
            d[i, j], dstr[i, j] = dg[a, b], ds[a, b]
    return d, dstr, can


def grouper_stratifie(lois, Zref, Gref, nsp, eps=0.01, eps_strat=0.04):
    """Liaison complète ; une paire est admissible si d < ε et d_strat < ε_strat (4·ε : rapport attendu entre la strate
    d'octile la plus touchée et la moyenne globale pour une différence étalée sur un octile)."""
    d, dstr, can = matrices_stratifiees(lois, Zref, Gref, nsp)
    N = len(lois)
    ok = (d < eps) & (dstr < eps_strat)
    np.fill_diagonal(ok, True)
    rang = {i: r for r, i in enumerate(sorted(range(N), key=lambda i: (can[i], i)))}
    groupes = [[i] for i in sorted(range(N), key=lambda i: rang[i])]
    while True:
        meilleur = None
        for a in range(len(groupes)):
            for b in range(a + 1, len(groupes)):
                if all(ok[i, j] for i in groupes[a] for j in groupes[b]):
                    cle = (max(d[i, j] for i in groupes[a] for j in groupes[b]), rang[groupes[a][0]], rang[groupes[b][0]])
                    if meilleur is None or cle < meilleur[0]:
                        meilleur = (cle, a, b)
        if meilleur is None:
            break
        _, a, b = meilleur
        groupes[a] = sorted(groupes[a] + groupes[b], key=lambda i: rang[i])
        del groupes[b]
    return groupes, {"d": d, "d_strat": dstr, "canon": can}


def medoide(groupe, d, canon):
    """Représentant fixé avant tout tirage : plus petite distance maximale aux autres membres ; égalités par empreinte."""
    return min(groupe, key=lambda i: (max([d[i, j] for j in groupe if j != i] or [0.0]), canon[i]))


def n_effectif_hellinger(lois, Zref, Gref):
    Ps = [np.sqrt(M.probas(l, Zref, Gref)) for l in lois]
    k = len(Ps)
    K = np.array([[float((Ps[i] * Ps[j]).sum(axis=1).mean()) for j in range(k)] for i in range(k)])
    return float(k * k / (K ** 2).sum()), K


def couverture(lois, oracle, spec, infos, archive_captes=(), detectables=None):
    """Composantes du monde couvertes par au moins une loi (attribution de l'oracle), hors celles déjà captées par l'archive ;
    restreintes aux composantes certifiées détectables si `detectables` est donné."""
    cov = set()
    for l in lois:
        cov |= set(M.captes(oracle.attribution(l, spec), infos))
    cov -= set(archive_captes)
    if detectables is not None:
        cov &= set(detectables)
    return sorted(cov)
