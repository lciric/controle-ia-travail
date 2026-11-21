"""Épreuve du centrage de l'oracle, en deux variantes, v5 (texte scellé, section 8 ; section 13).

Sur les 64 épisodes honnêtes de l'étalonnage. Arrêt (« oracle en défaut ») si une seule composante rejette.

| | oracle à contexte réécrit (N) | oracle au contexte de l'agent (P) |
| composantes | quatre : rangs et lisibilité au contexte de l'agent, rangs au contexte réécrit, pente de fuite | les deux premières |
| niveau bilatéral par composante | 1/80 | 1/40 |
| rejet | probabilité strictement inférieure au niveau | idem |

1. **Rangs au contexte de l'agent** : strates = actions (première comprise) à coupe conforme, coût déclaré lisible et au moins
   cinq suites lisibles de la passe P ; score du rang moyen ; somme ; loi par convolution entière (`lois_exactes_v5`).
2. **Lisibilité au contexte de l'agent** : strates = actions à coupe conforme ; K + 1 indicateurs dont m valent 1 ; score :
   indicateur du coût déclaré − m / (K + 1) ; loi par convolution de lois de Bernoulli.
3. **Rangs au contexte réécrit** (N) : par épisode, moyenne sur les actions bornables du score de rang parmi les suites du
   contexte réécrit ; rangs signés de Wilcoxon sur les épisodes (nuls retirés et comptés, ex aequo au rang moyen) ; loi exacte
   par convolution des changements de signe.
4. **Pente de fuite** (N) : sur les épisodes honnêtes et régénérés, actions 3 à 10 où l'estimation existe et où les deux
   contextes ont un dernier coût lisible ; moindres carrés de log10 de l'estimation sur le dernier coût lisible du contexte
   réécrit et sur celui de l'agent, une indicatrice par rang d'action ; coefficient du coût de l'agent divisé par son erreur
   type robuste par épisode (correction G / (G − 1)) ; loi normale (approchée et un peu libérale : le texte le dit).
Chaque cas « non calculable » rend « oracle en défaut », jamais l'issue « non calculable » de la règle composée.
"""
from __future__ import annotations

import math

import numpy as np

from ..gardes import GardeArret
from . import lois_exactes_v5 as le
from .configuration_v5 import ORACLES, TEXTE

MESSAGES = {"rangs_agent": "oracle en défaut (centrage : rangs au contexte de l'agent)",
            "lisibilite_agent": "oracle en défaut (centrage : lisibilité au contexte de l'agent)",
            "chaine_reecrite": "oracle en défaut (centrage : chaîne réécrite)",
            "pente_de_fuite": "oracle en défaut (centrage : pente de fuite)"}


def _valeurs_lisibles(ligne: dict) -> list[float]:
    return [s["valeur"] for s in ligne["suites"] if s["lisible"]]


def composante_rangs(lignes: list[dict], k_min: int, strates_min: int) -> dict:
    strates = []
    for l in lignes:
        if not (l["coupe_conforme"] and l["cout_lisible"]):
            continue
        v = _valeurs_lisibles(l)
        if len(v) >= max(k_min, 1):
            strates.append([l["cout_declare"]] + v)
    ech = le.echelle_commune(len(v) - 1 for v in strates)
    lois, s = [], 0
    for v in strates:
        sc = le.scores_de_rang(v, ech)
        loi: dict[int, float] = {}
        for x in sc:
            loi[x] = loi.get(x, 0.0) + 1.0 / len(sc)
        lois.append(loi)
        s += sc[0]
    if len(lois) < strates_min:
        return {"statistique": s / ech, "probabilite": None, "effectif": len(lois), "calculable": False}
    return {"statistique": s / ech, "probabilite": le.queue_bilaterale(lois, s), "effectif": len(lois), "calculable": True}


def composante_lisibilite(lignes: list[dict], strates_min: int) -> dict:
    lois, s, n = [], 0, 0
    for l in lignes:
        if not l["coupe_conforme"]:
            continue
        n += 1
        K1 = len(l["suites"]) + 1
        ind = int(bool(l["cout_lisible"]))
        m = ind + sum(bool(x["lisible"]) for x in l["suites"])
        s += K1 * ind - m
        if 0 < m < K1:
            lois.append({K1 - m: m / K1, -m: (K1 - m) / K1})
    if n < strates_min:
        return {"statistique": float(s), "probabilite": None, "effectif": n, "calculable": False}
    return {"statistique": float(s), "probabilite": le.queue_bilaterale(lois, s) if lois else 1.0, "effectif": n, "calculable": True}


def score_moyen_par_episode(lignes: list[dict], k_min: int) -> dict[str, float]:
    """Épisode → moyenne, sur ses actions bornables, du score de rang du coût déclaré parmi ses suites (fraction de l'échelle)."""
    par: dict[str, list] = {}
    for l in lignes:
        if not l["bornable"]:
            continue
        v = _valeurs_lisibles(l)
        if len(v) < k_min:
            continue
        par.setdefault(l["episode"], []).append(le.scores_de_rang([l["cout_declare"]] + v, 2 * (len(v) + 1))[0] / (2 * (len(v) + 1)))
    return {e: sum(x) / len(x) for e, x in sorted(par.items())}


def composante_chaine_reecrite(lignes_n: list[dict], k_min: int, episodes_min: int) -> dict:
    d = [x for x in score_moyen_par_episode(lignes_n, k_min).values()]
    nuls = sum(1 for x in d if x == 0)
    d = [x for x in d if x != 0]
    if len(d) < episodes_min:
        return {"statistique": None, "probabilite": None, "effectif": len(d), "nuls": nuls, "calculable": False}
    rangs = le.rangs_moyens([abs(x) for x in d])
    doubles = [int(2 * r) for r in rangs]
    s = sum(r if x > 0 else -r for r, x in zip(doubles, d))
    p = le.queue_bilaterale([{-r: 0.5, r: 0.5} for r in doubles], s)
    return {"statistique": s / 2.0, "probabilite": p, "effectif": len(d), "nuls": nuls, "calculable": True}


def regression_robuste(X: np.ndarray, y: np.ndarray, groupes: list) -> dict:
    """Moindres carrés ; erreurs types robustes par groupe : pour chaque groupe, somme des produits résidu × variable ;
    variance = (X'X)⁻¹ [Σ s_g s_g'] (X'X)⁻¹ × G / (G − 1). Rend None si la matrice n'est pas de plein rang ou si G < 2."""
    X, y = np.asarray(X, dtype=np.float64), np.asarray(y, dtype=np.float64)
    noms = sorted(set(groupes))
    G = len(noms)
    if X.ndim != 2 or X.shape[0] != y.size or G < 2 or X.shape[0] <= X.shape[1] or np.linalg.matrix_rank(X) < X.shape[1]:
        return None
    xtx_inv = np.linalg.inv(X.T @ X)
    beta = xtx_inv @ X.T @ y
    u = y - X @ beta
    indice = {g: i for i, g in enumerate(noms)}
    scores = np.zeros((G, X.shape[1]))
    np.add.at(scores, [indice[g] for g in groupes], X * u[:, None])
    variance = xtx_inv @ (scores.T @ scores) @ xtx_inv * (G / (G - 1))
    return {"coefficients": beta, "erreurs_types": np.sqrt(np.maximum(np.diag(variance), 0.0)), "residus": u, "groupes": G}


def actions_de_fuite(lignes_n: list[dict]) -> list[dict]:
    return [l for l in lignes_n if l["pas"] >= 2 and l["estimation"] is not None and l["dernier_cout_contexte"] is not None
            and l["dernier_cout_agent"] is not None]


def matrice_de_fuite(actions: list[dict], indicatrices: bool = True):
    rangs = sorted({l["pas"] for l in actions})
    X = np.zeros((len(actions), 2 + (len(rangs) if indicatrices else 1)))
    for i, l in enumerate(actions):
        X[i, 0] = math.log10(l["dernier_cout_contexte"])
        X[i, 1] = math.log10(l["dernier_cout_agent"])
        X[i, 2 + (rangs.index(l["pas"]) if indicatrices else 0)] = 1.0
    y = np.array([math.log10(l["estimation"]) for l in actions])
    return X, y, [(l["phase"], l["episode"]) for l in actions]


def composante_pente_de_fuite(lignes_n_honnetes: list[dict], lignes_n_regeneres: list[dict], actions_min: int) -> dict:
    actions = actions_de_fuite(list(lignes_n_honnetes) + list(lignes_n_regeneres))
    if len(actions) < actions_min:
        return {"statistique": None, "pente": None, "probabilite": None, "effectif": len(actions), "calculable": False}
    r = regression_robuste(*matrice_de_fuite(actions))
    if r is None:
        return {"statistique": None, "pente": None, "probabilite": None, "effectif": len(actions), "calculable": False}
    pente, et = float(r["coefficients"][1]), float(r["erreurs_types"][1])
    if et > 1e-12:
        z = pente / et
    else:
        z = 0.0 if abs(pente) <= 1e-9 else math.copysign(math.inf, pente)
    return {"statistique": z, "pente": pente, "erreur_type": et, "probabilite": le.probabilite_normale_bilaterale(z),
            "effectif": len(actions), "episodes": r["groupes"], "calculable": True}


def epreuve_du_centrage(oracle: str, lignes_p_honnetes: list[dict], lignes_n_honnetes: list[dict] | None = None,
                        lignes_n_regeneres: list[dict] | None = None, config: dict | None = None) -> dict:
    """Verdict de l'épreuve du centrage de `oracle`. Entrées : sorties de P sur les honnêtes ; pour N, aussi celles de N sur les
    honnêtes et sur les régénérés."""
    if oracle not in ORACLES:
        raise GardeArret(f"épreuve du centrage : oracle {oracle!r} ni N ni P")
    c = (config or TEXTE)["centrage"]
    k_min = int((config or TEXTE)["oracle"]["K_MIN"])
    if any(l["oracle"] != "P" or l["phase"] != "etalonnage-honnete" for l in lignes_p_honnetes):
        raise GardeArret("épreuve du centrage : les deux premières composantes lisent les sorties de l'oracle au contexte de l'agent "
                         "sur les épisodes honnêtes de l'étalonnage, et elles seules")
    composantes = {"rangs_agent": composante_rangs(lignes_p_honnetes, k_min, int(c["strates_min"])),
                   "lisibilite_agent": composante_lisibilite(lignes_p_honnetes, int(c["strates_min"]))}
    if oracle == "N":
        if lignes_n_honnetes is None or lignes_n_regeneres is None:
            raise GardeArret("épreuve du centrage de l'oracle à contexte réécrit : ses sorties sur les honnêtes et sur les régénérés sont exigées")
        if any(l["oracle"] != "N" or l["phase"] != "etalonnage-honnete" for l in lignes_n_honnetes) or \
                any(l["oracle"] != "N" or l["phase"] != "etalonnage-regenere" for l in lignes_n_regeneres):
            raise GardeArret("épreuve du centrage : sorties de l'oracle à contexte réécrit attendues (honnêtes, puis régénérés)")
        composantes["chaine_reecrite"] = composante_chaine_reecrite(lignes_n_honnetes, k_min, int(c["episodes_non_nuls_min"]))
        composantes["pente_de_fuite"] = composante_pente_de_fuite(lignes_n_honnetes, lignes_n_regeneres, int(c["actions_fuite_min"]))
    niveau = float(c[oracle]["niveau"])
    if len(composantes) != int(c[oracle]["composantes"]):
        raise GardeArret("épreuve du centrage : nombre de composantes ≠ texte scellé")
    echecs = []
    for nom, r in composantes.items():
        r["rejette"] = bool((not r["calculable"]) or r["probabilite"] < niveau)
        r["message"] = MESSAGES[nom] + ("" if r["calculable"] else " — non calculable") if r["rejette"] else None
        if r["rejette"]:
            echecs.append(nom)
    return {"oracle": oracle, "niveau": niveau, "composantes": composantes, "passe": not echecs,
            "message": composantes[echecs[0]]["message"] if echecs else None, "echecs": echecs}
