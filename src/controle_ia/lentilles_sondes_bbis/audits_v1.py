"""Calibration des nuls et audit de symétrie (texte scellé, plan, point 6 ; « Critères de lecture gelés », R4).

Calibration : des directions témoins tirées de chaque nul passent par le chemin des directions réelles ; le compte de leurs
p ≤ 0,05 est comparé à [q_bas, q_haut] sous la loi exacte : bêta-binomiale (n ; 100 ; M − 99) pour un jeu de n témoins qui
partagent M directions nulles, somme de lois bêta-binomiales indépendantes pour plusieurs jeux mis en commun. Les bornes sont
calculées comme par `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/bornes_calibration_beta_binomiale_v1.py`.
Audit : déclencheurs gelés (trop beau, tout négatif), évalués et joués dans la session du calcul ; aucune table ne change.
"""
from __future__ import annotations

from math import comb, exp, lgamma, log

import numpy as np

from . import constantes_v1 as K
from . import statistiques_v1 as st
from .constantes_v1 import Arret


# --- bornes de calibration -------------------------------------------------------------------------------------------------------------
def parametres_beta(m: int = K.M_NUL) -> tuple[int, int]:
    """(A, B) de la loi bêta-binomiale : sous le nul, p ≤ 0,05 si le témoin dépasse au plus `A − 1` des M directions nulles ;
    pour M = 2 000, A = 100 et B = M − 99 = 1 901 (part attendue 100/2 001)."""
    a = int(np.floor(K.SEUIL_P_CALIBRATION * (m + 1) + 1e-9))
    if a < 1:
        raise Arret(f"calibration : M = {m} trop petit pour le seuil {K.SEUIL_P_CALIBRATION}")
    return a, m - a + 1


def pmf_beta_binomiale(n: int, a: int, b: int) -> list[float]:
    lb = lgamma(a) + lgamma(b) - lgamma(a + b)
    return [exp(log(comb(n, k)) + lgamma(k + a) + lgamma(n - k + b) - lgamma(n + a + b) - lb) for k in range(n + 1)]


def convoluer(a: list[float], b: list[float]) -> list[float]:
    return np.convolve(np.asarray(a, np.float64), np.asarray(b, np.float64)).tolist()


def bornes(pmf: list[float], niveau: float = K.NIVEAU_CALIBRATION) -> tuple[int, int]:
    """q_bas : plus grand entier tel que P(X < q_bas) ≤ niveau ; q_haut : plus petit entier tel que P(X > q_haut) ≤ niveau."""
    cumul, bas = 0.0, 0
    for q in range(len(pmf)):
        if cumul <= niveau:
            bas = q
        cumul += pmf[q]
    queue, haut = 0.0, 0
    for q in range(len(pmf) - 1, -1, -1):
        if queue > niveau:
            haut = q + 1
            break
        queue += pmf[q]
    return bas, haut


def bornes_calibration(jeux: list[int], m: int = K.M_NUL) -> tuple[int, int]:
    """Bornes pour des jeux de témoins mis en commun (un jeu de 1 000 : [23, 85] ; trois jeux de 200 : [12, 53])."""
    if not jeux or any(int(n) < 1 for n in jeux):
        raise Arret("calibration : au moins un jeu de témoins non vide exigé")
    a, b = parametres_beta(m)
    pmf = [1.0]
    for n in jeux:
        pmf = convoluer(pmf, pmf_beta_binomiale(int(n), a, b))
    return bornes(pmf)


def calibration(p_par_jeu: list[np.ndarray], m: int = K.M_NUL) -> dict:
    """Compte des p ≤ 0,05 des témoins, mis en commun par (couche, lentille, nul), contre les bornes. `tenue` faux : les
    tables de cette couche, de cette lentille et de ce nul sont « non calculables », sans arrêt du reste."""
    jeux = [int(np.asarray(p).size) for p in p_par_jeu]
    bas, haut = bornes_calibration(jeux, m)
    compte = int(sum(int((np.asarray(p) <= K.SEUIL_P_CALIBRATION).sum()) for p in p_par_jeu))
    n = int(sum(jeux))
    a, _ = parametres_beta(m)
    return {"n": n, "jeux": jeux, "compte_p_sous_0_05": compte, "q_bas": bas, "q_haut": haut,
            "attendu": n * a / (m + 1), "tenue": bool(bas <= compte <= haut),
            "borne_basse_volontairement_lache": bool(n < K.N_BORNE_BASSE_LACHE)}


MOTIF_CALIBRATION = "non calculable : calibration du nul hors de ses bornes"


# --- audit de symétrie (R4) ---------------------------------------------------------------------------------------------------------------
def declencheurs(lectures: list[dict], cosinus_paires: list[dict]) -> dict:
    """Déclencheurs gelés. `lectures` : une ligne par (sonde, vecteur, signe, lentille) avec `sonde` (clé), `role`, `couche`,
    `lentille`, `libelle` (ou `None` si non calculable) et `ids` (vingt premiers jetons) ; `cosinus_paires` : lignes
    `{type: "plis" | "doses" | "sonde-lecteur", cosinus}` des comparaisons à même couche.
    Une sonde est « concentrée » par une lentille si l'une de ses lectures (vecteur, signe) l'est (texte, attente A-1 : « à
    un signe au moins »)."""
    concentrees = {(l["sonde"], l["lentille"]) for l in lectures if l["libelle"] == st.LIBELLE_CONCENTREE}
    sondes = {l["sonde"]: l["role"] for l in lectures}
    apprises = [s for s, r in sondes.items() if r == "sonde"]
    lecteurs = [s for s, r in sondes.items() if r == "enc"]
    toutes = (len(apprises) == len(K.CELLULES) * len(K.PLIS) and len(lecteurs) == len(K.CELLULES) * len(K.PLIS)
              and all((s, K.LENTILLE_PUBLIQUE) in concentrees for s in apprises + lecteurs))
    par_direction: dict[tuple, dict[str, set]] = {}
    for l in lectures:
        if l["couche"] in (7, 15) and l.get("ids") is not None:
            par_direction.setdefault((l["sonde"], l["vecteur"], l["signe"]), {})[l["lentille"]] = set(l["ids"])
    memes = sorted("/".join(cle) for cle, d in par_direction.items()
                   if len(d) == 2 and d[K.LENTILLE_PUBLIQUE] == d[K.LENTILLE_LOGITS])
    proches = [c for c in cosinus_paires if c["type"] in ("plis", "doses") and c["cosinus"] > K.SEUIL_COS_DIRECTIONS]
    jumeaux = [c for c in cosinus_paires if c["type"] == "sonde-lecteur" and c["cosinus"] > K.SEUIL_COS_SONDE_LECTEUR]
    distinctes = [l for l in lectures if l["libelle"] in (st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE)]
    trop_beau = {"dix_sondes_et_dix_lecteurs_concentres": bool(toutes), "memes_vingt_jetons_couches_7_ou_15": memes,
                 "directions_distinctes_de_cosinus_superieur_a_0_999": proches,
                 "sonde_et_lecteur_de_cosinus_superieur_a_0_99": jumeaux}
    tout_negatif = bool(lectures) and not distinctes
    return {"trop_beau": trop_beau, "trop_beau_declenche": bool(toutes or memes or proches or jumeaux),
            "tout_negatif_declenche": bool(tout_negatif),
            "audit_a_jouer": bool(toutes or memes or proches or jumeaux or tout_negatif)}


def relire_par_chemin_independant(v: np.ndarray, jacobienne: np.ndarray | None, gamma: np.ndarray, wu: np.ndarray,
                                  k: int = K.K_JETONS) -> dict:
    """Relecture d'une direction en double précision, sans la fonction du voisin ni `lecture_v1` : (scores, vingt premiers)."""
    t = np.asarray(v, np.float64)
    if jacobienne is not None:
        t = np.asarray(jacobienne, np.float64) @ t
    t = t / np.sqrt(np.mean(t ** 2) + K.EPSILON) * np.asarray(gamma, np.float64)
    scores = np.asarray(wu, np.float64) @ t
    ordre = np.argsort(-scores, kind="stable")[:min(k, scores.size)]
    return {"scores": scores, "premiers": ordre.tolist()}


def comparer_relecture(scores_simple: np.ndarray, relecture: dict, k: int = K.K_JETONS) -> dict:
    """Accord entre la lecture du calcul (simple précision) et la relecture indépendante (double précision)."""
    s = np.asarray(scores_simple, np.float64)
    ordre = np.argsort(-s, kind="stable")[:min(k, s.size)].tolist()
    echelle = float(np.max(np.abs(relecture["scores"])))
    return {"jetons_communs": len(set(ordre) & set(relecture["premiers"])), "k": len(ordre),
            "ecart_relatif_maximal": float(np.max(np.abs(s - relecture["scores"])) / echelle) if echelle > 0 else None}


CONTENU_AUDIT = ("empreintes des tableaux lus contre E-2", "couche de la sonde, de la lentille et du harnais",
                 "point de capture de la lentille", "conventions de signe", "décodage", "rapport à ε",
                 "deux directions relues par un chemin indépendant")
