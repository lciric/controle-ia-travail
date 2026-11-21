"""Idée 1.1, bras J9-Dc (préenregistrement scellé `3ffe1739…`, bras 5) : copie renommée de
`nul_v9.detail_morceaux_groupe` (copie `a41b7b5`, `7ae450df…`) qui rend, en plus, le certificat de **chaque** coupe.

Chargé dans l'espace `pole` (`vue_v9_v1.charger`), à côté de `pole.nul_v9`, dont il importe les fonctions internes sans
les changer. **Un seul changement déclaré** dans le corps recopié : le nom de la fonction, et deux champs ajoutés à chaque
entrée rendue, `bornes_coupes` (borne certifiée de chaque coupe de la question, dans l'ordre de `_coupes`) et `etiquettes`
(seuil de chaque coupe) ; aucun calcul n'est changé (différentiel écrit par l'essai, lu par le contre-lecteur du code).
S'il n'est pas jugé sûr, J9-Dc est retiré et le retrait est rapporté (texte, bras 5).
"""
import numpy as np

from .nul_v9 import TYPE_MORCEAUX, NulV9Refuse, _ajustement_sans_coupure, _coupes, _depart, maximiser_par_lots

__all__ = ["detail_morceaux_par_coupe", "np", "TYPE_MORCEAUX", "NulV9Refuse", "_ajustement_sans_coupure", "_coupes",
           "_depart", "maximiser_par_lots"]


def detail_morceaux_par_coupe(membres, cache, issues, instants):
    """Valeurs certifiées des membres par morceaux `membres` (mêmes lois connues) à chaque instant de lecture, calculées en
    un lot : {nom: {t: {valeur, atteinte, ecart_residuel, coupe, coupes, coupes_restantes, pas}}}. `ecart_residuel` =
    valeur − meilleure valeur atteinte (≥ 0) : prix en puissance de l'optimisation, jamais en validité."""
    if not membres:
        return {}
    lois = membres[0]["lois"]
    for m in membres:
        if m.get("type") != TYPE_MORCEAUX or m.get("lois") != lois:
            raise NulV9Refuse("calcul par morceaux en lot : membres de type ou de lois connues différents")
    y = np.array(issues, dtype=int)
    n = len(issues)
    instances = cache.instances
    tables = [np.array(cache.probas(l), dtype=float) for l in lois]
    J, K = len(tables), tables[0].shape[1]
    L = np.stack([tab[np.arange(n), y] for tab in tables], axis=1)
    Y = np.zeros((n, K))
    Y[np.arange(n), y] = 1.0
    G = np.concatenate([L, Y], axis=1)
    departs, w = {}, None
    for t in instants:
        w = _ajustement_sans_coupure(G[:t], w)
        departs[t] = w
    valeurs_g = sorted({str(inst.get("g")) for inst in instances})
    lots = {}
    for membre in membres:
        for t in instants:
            M, etiquettes = _coupes(membre["partition"], instances, t, valeurs_g)
            lots.setdefault(M.shape[0], []).append((membre["nom"], t, M, etiquettes))
    sortie = {m["nom"]: {} for m in membres}
    for P, questions in sorted(lots.items()):
        M = np.concatenate([qu[2] for qu in questions], axis=2)
        groupes = np.concatenate([np.full(qu[2].shape[2], i) for i, qu in enumerate(questions)])
        x0 = np.concatenate([np.tile(_depart(J, K, P, departs[qu[1]]), (qu[2].shape[2], 1)) for qu in questions])
        xg = np.concatenate([np.tile(_depart(J, K, P, departs[qu[1]], centre=0.0), (qu[2].shape[2], 1)) for qu in questions])
        bornes, atteintes, diag = maximiser_par_lots(L, Y, M, groupes, x0, points_a_certifier=(xg,))
        for i, (nom, t, Mq, etiquettes) in enumerate(questions):
            sel = np.flatnonzero(groupes == i)
            c = int(np.argmax(bornes[sel]))
            valeur, atteinte = float(bornes[sel].max()), float(atteintes[sel].max())
            sortie[nom][t] = {"valeur": valeur, "atteinte": atteinte, "ecart_residuel": max(0.0, valeur - atteinte),
                              "coupe": etiquettes[c], "coupes": int(len(sel)), "pas": diag["pas"],
                              "bornes_coupes": [float(v) for v in bornes[sel]], "etiquettes": list(etiquettes)}
    return sortie
