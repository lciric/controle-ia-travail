"""Analyse de SPARKS-EXP7-NUL, v3 : celle de la v2, plus le secondaire « sur M5 » de l'incrément (addendum « Métrique » :
« même calcul sur M1 … et sur M5 » ; contre-lecture du delta v2, point 7) : M5 (aire « ss contre hh » sur la moyenne de
la paire) par c_b, par la base seule et par le lecteur seul. Ce calcul ne tire aucun nombre au hasard : les générateurs et
leur ordre d'usage sont exactement ceux de la v2 ; `analyser` est celui de la v2, complété après coup."""
from __future__ import annotations

import numpy as np

from ..sparks_exp7_nul_v1.analyse import aire_sous_courbe, moyenne_lecteurs
from ..sparks_exp7_nul_v2 import analyse as a2
from ..sparks_exp7_nul_v2.analyse import *  # noqa: F401,F403
from ..sparks_exp7_nul_v2.analyse import _tableaux, probabilites, rangs, scores_b3_b4  # noqa: F401


def m5_secondaire(par_cas: dict, s_b: dict) -> dict:
    """M5 par c_b = (r_L + r_b)/2, par s_b et par p_L ; None si une classe de paires nulles manque."""
    cas, P, S, Y = _tableaux(par_cas, s_b)
    C = ((rangs(P.ravel()) + rangs(S.ravel())) / 2).reshape(P.shape)
    ss = [i for i, c in enumerate(cas) if par_cas[c]["type"] == "ss"]
    hh = [i for i, c in enumerate(cas) if par_cas[c]["type"] == "hh"]

    def m5(X):
        if not ss or not hh:
            return None
        return aire_sous_courbe([float(np.mean(X[i])) for i in ss], [float(np.mean(X[i])) for i in hh])
    return {"M5_par_c": m5(C), "M5_par_base": m5(S), "M5_lecteur": m5(P), "n_ss": len(ss), "n_hh": len(hh)}


def analyser(reponses: list[dict], cle: dict, lecteurs: tuple[str, ...], rng_bootstrap, generateurs: dict, *,
             bases_poids: dict, etal: dict, **kw) -> dict:
    sortie = a2.analyser(reponses, cle, lecteurs, rng_bootstrap, generateurs, bases_poids=bases_poids, etal=etal, **kw)
    sb = scores_b3_b4(bases_poids, cle, etal)
    principaux = [r for r in reponses if not cle[r["cas"]].get("pilote") and cle[r["cas"]]["type"] in a2.TYPES_PRINCIPAUX]
    moy = moyenne_lecteurs(probabilites(principaux, cle), lecteurs)
    for c, v in moy.items():
        k = next(x for x in cle.values() if x["cas"] == c)
        v["A"], v["B"] = k["A"], k["B"]
    for b in ("B3", "B4"):
        sortie["increment_secondaire"][b]["m5"] = m5_secondaire(moy, sb[b]["scores"])
    return sortie
