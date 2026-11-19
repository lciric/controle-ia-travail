"""Papier C — addendum de dérivation, entièrement mécanique (v1).

Texte de référence : version r1 (`e12f16fa…`), Plan d'analyse, section 2 « Addendum de dérivation (mécanique) »
(lignes 1050 à 1096) ; « Métrique », point 18 ; section « Seuil », « Lisibilité » ; liste d'arrêt 12, 14 et 16.
Le nom de ce fichier est celui que le texte écrit (ligne 1054 : `docs/procedures/papier-C-v1/derivation.py`).

Entrées : les seuls fichiers de sortie des points 1.3, 1.4 et 1.5 du pilote. Tout fichier du banc (point 1.2) est
refusé en entrée (`FichierDuBancRefuse`, garde testée sur un cas sain et sur un artefact). Aucun jugement neuf : une
règle inapplicable lève `RegleDeLAddendumInapplicable` (nœud).

Leçon de Panin (ligne 976) tenue par construction : aucune fonction de ce fichier ne retire ni ne remplace un juge
ou une famille ; la variable de dessin est ḡ_sép, qui ne suppose aucune destination ; γ est rapporté seulement.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from controle_ia.scellement import verifier
from papier_c_erreurs_v1 import (AucuneVariantePourUnJuge, BassinTropPetit, ConfigurationInvalide, FichierDuBancRefuse,
                                 RegleDeLAddendumInapplicable)
from papier_c_lois_v1 import gamma_destination_imposee, loi_nette, loi_separee
from papier_c_reechantillonnage_v1 import intervalle_percentiles

POINTS_ADMIS = ("1.3", "1.4", "1.5")
POINT_DU_BANC = "1.2"


# ------------------------------------------------------------------------------------------------------------------
# Garde d'entrée : la dérivation refuse tout fichier du banc (liste d'arrêt 12)
# ------------------------------------------------------------------------------------------------------------------
def exiger_entree_de_derivation(chemin) -> dict:
    """Lit une sortie scellée du pilote. Refuse tout fichier placé sous un dossier `banc`, ou dont le champ `point`
    vaut « 1.2 » ; refuse aussi tout fichier qui ne déclare pas un des points 1.3, 1.4, 1.5."""
    p = Path(chemin)
    if "banc" in p.parts:
        raise FichierDuBancRefuse(f"{p} : fichier du banc refusé en entrée de la dérivation")
    verifier(p)
    corps = json.loads(p.read_text(encoding="utf-8"))
    point = corps.get("point") if isinstance(corps, dict) else None
    if point == POINT_DU_BANC:
        raise FichierDuBancRefuse(f"{p} : sortie du point 1.2 (banc) refusée en entrée de la dérivation")
    if point not in POINTS_ADMIS:
        raise ConfigurationInvalide(f"{p} : point {point!r} ; seules les sorties des points 1.3, 1.4 et 1.5 sont lues")
    return corps


# ------------------------------------------------------------------------------------------------------------------
# Lisibilité et variantes (section « Seuil » ; point 1.3)
# ------------------------------------------------------------------------------------------------------------------
def lisible(masses, mediane_min: float = 0.90, seuil: float = 0.50, part_min: float = 0.99) -> bool:
    """Par juge × consigne × variante : médiane de la masse ≥ 0,90 et masse ≥ 0,50 sur au moins 99 % des lectures."""
    m = np.asarray(masses, dtype=np.float64)
    if m.ndim != 1 or m.size == 0 or not np.all(np.isfinite(m)):
        raise ConfigurationInvalide("lisibilité : masses finies et non vides attendues")
    return bool(np.median(m) >= mediane_min and np.mean(m >= seuil) >= part_min)


def choisir_variantes(passe) -> dict:
    """`passe` : booléens (juges, variantes), variantes dans l'ordre de la configuration. Règle (point 1.3) : la
    première variante qui passe pour les trois juges ; à défaut, la première qui passe pour chaque juge (réserve
    « variantes différentes ») ; un juge sans variante : nœud."""
    p = np.asarray(passe, dtype=bool)
    if p.ndim != 2 or p.size == 0:
        raise ConfigurationInvalide("variantes : tableau (juges, variantes) attendu")
    communes = np.flatnonzero(p.all(0))
    if communes.size:
        return {"variantes": [int(communes[0])] * p.shape[0], "reserves": []}
    sans = [j for j in range(p.shape[0]) if not p[j].any()]
    if sans:
        raise AucuneVariantePourUnJuge(f"aucune variante ne passe pour le(s) juge(s) d'indice {sans}")
    return {"variantes": [int(np.flatnonzero(p[j])[0]) for j in range(p.shape[0])], "reserves": ["variantes différentes"]}


# ------------------------------------------------------------------------------------------------------------------
# Gains du vivier (point 18)
# ------------------------------------------------------------------------------------------------------------------
def _lectures(v0, v_formulations) -> tuple[np.ndarray, np.ndarray]:
    v0, V = np.asarray(v0, dtype=np.float64), np.asarray(v_formulations, dtype=np.float64)
    if v0.ndim != 2 or V.ndim != 3 or V.shape[0] != v0.shape[0] or V.shape[2] != v0.shape[1]:
        raise ConfigurationInvalide("vivier : v0 (juges, contenus) et lectures (juges, formulations, contenus) attendus")
    if not (np.all(np.isfinite(v0)) and np.all(np.isfinite(V))):
        raise RegleDeLAddendumInapplicable("vivier : lecture non finie")
    return v0, V


def gains_du_vivier(P, v0, v_formulations, v_etoile: float) -> dict:
    """g_sép,{j,f} = − pente des moindres carrés de Δ_i sur v₀_i (loi séparée) ; ḡ_sép, moyenne sur les juges ;
    γ_{j,f} (destination imposée), rapporté seulement. `v0` (juges, contenus) ; `v_formulations` (juges,
    formulations, contenus) ; poids P (R, contenus). Rend des tableaux (R, juges, formulations) et (R, formulations)."""
    v0, V = _lectures(v0, v_formulations)
    J, F, _ = V.shape
    R = np.asarray(P).shape[0]
    g, gamma = np.empty((R, J, F)), np.empty((R, J, F))
    for j in range(J):
        for f in range(F):
            d = V[j, f] - v0[j]
            g[:, j, f] = loi_separee(P, d, v0[j])["g"]
            gamma[:, j, f] = gamma_destination_imposee(P, d, v0[j], v_etoile)
    return {"g_sep": g, "g_sep_moyen": g.mean(1), "gamma": gamma}


def erreurs_types_du_vivier(v0, v_formulations, v_etoile: float, tirages: int, rng: np.random.Generator) -> dict:
    """Erreur type de ḡ_sép de chaque formulation par rééchantillonnage des contenus de calibrage (2 000 tirages ;
    le pilote rééchantillonne les contenus, écart déclaré au point 18)."""
    v0a, _ = _lectures(v0, v_formulations)
    n = v0a.shape[1]
    comptes = rng.multinomial(n, np.full(n, 1.0 / n), size=int(tirages)).astype(np.float64)
    tir = gains_du_vivier(comptes, v0, v_formulations, v_etoile)["g_sep_moyen"]
    return {"erreur_type": np.nanstd(tir, axis=0, ddof=1), "tirages_non_finis": int(np.sum(~np.isfinite(tir)))}


def erreur_type_de_famille(erreurs_types_des_formulations) -> float:
    """Erreur type de la famille = médiane des erreurs types de ses seize formulations (médiane de seize erreurs
    types, jamais de jetons)."""
    return float(np.median(np.asarray(erreurs_types_des_formulations, dtype=np.float64)))


def erreur_type_a_l_effectif(et_cal: float, n_cal: int, n: int) -> float:
    """ET(n) = ET(n_cal) · √(n_cal / n)."""
    return float(et_cal) * math.sqrt(n_cal / n)


def k_max(g_sep_moyens_famille, et_cal: float, n_cal: int, n: int, etendue_bruit: float = 3.53) -> int:
    """k_max(n) = 1 + partie entière de [max(0, étendue des ḡ_sép de la famille − 3,53 · ET(n_cal)) /
    (1,96 · √2 · ET(n))]."""
    g = np.asarray(g_sep_moyens_famille, dtype=np.float64)
    et_n = erreur_type_a_l_effectif(et_cal, n_cal, n)
    if not (np.all(np.isfinite(g)) and et_n > 0):
        raise RegleDeLAddendumInapplicable("k_max : gains non finis ou erreur type nulle")
    etendue = float(g.max() - g.min())
    return 1 + int(math.floor(max(0.0, etendue - etendue_bruit * et_cal) / (1.96 * math.sqrt(2.0) * et_n)))


def k_retenu(kmax: int, k_min: int = 3, k_plafond: int = 5) -> dict:
    """k(n) = min(5, max(3, k_max(n))) ; k_max(n) < 3 : réserve « niveaux non séparables deux à deux »."""
    return {"k": min(k_plafond, max(k_min, int(kmax))),
            "reserves": ["niveaux non séparables deux à deux"] if kmax < k_min else []}


# ------------------------------------------------------------------------------------------------------------------
# Formulations et témoins
# ------------------------------------------------------------------------------------------------------------------
def choisir_formulations(g_sep_moyens_famille, k: int) -> dict:
    """Cibles t_m = ḡ_sép,min + (m − 1)(ḡ_sép,max − ḡ_sép,min)/(k − 1), m = 1 à k, traitées dans l'ordre croissant ;
    pour chaque cible, la formulation non encore retenue la plus proche en ḡ_sép ; égalités : plus petit indice du
    vivier. Rang d'intensité = ordre croissant des ḡ_sép retenus (égalités : indice du vivier). Indices rendus à
    partir de 1, comme au vivier."""
    g = np.asarray(g_sep_moyens_famille, dtype=np.float64)
    if g.ndim != 1 or not np.all(np.isfinite(g)) or k < 2 or k > g.size:
        raise RegleDeLAddendumInapplicable(f"formulations : {g.size} gains finis attendus et 2 ≤ k = {k} ≤ leur nombre")
    bas, haut = float(g.min()), float(g.max())
    retenus: list[int] = []
    for m in range(1, k + 1):
        cible = bas + (m - 1) * (haut - bas) / (k - 1)
        libres = [i for i in range(g.size) if i not in retenus]
        retenus.append(min(libres, key=lambda i: (abs(g[i] - cible), i)))
    par_rang = sorted(retenus, key=lambda i: (g[i], i))
    return {"indices_par_rang": [i + 1 for i in par_rang], "gains_par_rang": [float(g[i]) for i in par_rang]}


def apparier_les_temoins(longueurs_des_formulations_par_rang, longueurs_des_temoins) -> list[int]:
    """Règle des témoins : pour chaque formulation retenue, dans l'ordre des rangs croissants, le témoin de longueur
    en caractères la plus proche parmi ceux non encore pris dans la même famille (formulation remplie pour le corpus
    A) ; égalités : plus petit indice ; jamais selon un effet. Indices rendus à partir de 1."""
    lt = [int(x) for x in longueurs_des_temoins]
    pris: list[int] = []
    for longueur in longueurs_des_formulations_par_rang:
        libres = [t for t in range(len(lt)) if t not in pris]
        if not libres:
            raise RegleDeLAddendumInapplicable("témoins : plus de formulations retenues que de témoins")
        pris.append(min(libres, key=lambda t: (abs(lt[t] - int(longueur)), t)))
    return [t + 1 for t in pris]


# ------------------------------------------------------------------------------------------------------------------
# Demi-largeurs prévues et effectif
# ------------------------------------------------------------------------------------------------------------------
def partage_des_taches_de_conception(taches_des_contenus, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Validation croisée par tâches : huit tâches du lot de calibrage pour choisir, les huit autres pour mesurer
    (clé `papier-C/pilote/conception`). Rend deux masques de contenus. Tirage : permutation des identifiants triés,
    la première moitié choisit (appel de numpy non écrit au texte : point ouvert PO-29)."""
    t = np.asarray(taches_des_contenus)
    ids = np.array(sorted(set(t.tolist())))
    if ids.size < 2 or ids.size % 2:
        raise RegleDeLAddendumInapplicable(f"validation croisée : nombre pair de tâches attendu, {ids.size} trouvées")
    choisies = set(rng.permutation(ids)[: ids.size // 2].tolist())
    masque = np.array([x in choisies for x in t.tolist()])
    return masque, ~masque


def demi_largeur_de_lambda(v0, delta_net, temoins, v_etoile: float, n_cal: int, n: int, tirages: int,
                           rng: np.random.Generator, part_degeneres_max: float = 0.01, z: float = 1.96) -> dict:
    """Demi-largeur prévue de l'intervalle de λ à l'effectif n, pour un juge et une famille, sur les contenus des huit
    tâches de mesure : loi nette et erreur type de λ par rééchantillonnage de ces contenus (2 000 tirages), mise à
    l'échelle par √((n_cal / 2) / n) ; demi-largeur = 1,96 · ET mise à l'échelle ; +∞ si plus de 1 % de tirages
    dégénérés ou si l'intervalle de Ḡ contient 0 (intervalle par percentiles à 95 % des mêmes tirages : point ouvert
    PO-30)."""
    v0 = np.asarray(v0, dtype=np.float64)
    m = v0.size
    comptes = rng.multinomial(m, np.full(m, 1.0 / m), size=int(tirages)).astype(np.float64)
    loi = loi_nette(comptes, v0, delta_net, temoins, v_etoile)
    part = float(np.mean(loi["degenere"]))
    bas, haut, _ = intervalle_percentiles(loi["G"], 0.95)
    et = float(np.nanstd(loi["lam"][np.isfinite(loi["lam"])], ddof=1)) if np.isfinite(loi["lam"]).sum() > 1 else float("nan")
    echelle = et * math.sqrt((n_cal / 2.0) / n)
    infinie = part > part_degeneres_max or not (bas > 0 or haut < 0) or not math.isfinite(echelle)
    return {"demi_largeur": float("inf") if infinie else z * echelle, "erreur_type": et, "part_degeneres": part,
            "ic_G": (bas, haut)}


def demi_largeur_des_sondes(d: float, n: int, m_sondes: int, rho_t: float = 0.0) -> float:
    """Demi-largeur prévue de g brut des sondes (champs seuls), pour un niveau du plaidoyer :
    z · √(2(1 − ρ_t)) / (d · √(n/2)), z = 1,645 (m = 1) ou 1,96 (m = 2) ; ρ_t = 0 à défaut."""
    if m_sondes not in (1, 2):
        raise RegleDeLAddendumInapplicable(f"demi-largeur des sondes : m = {m_sondes} ; le texte ne donne z que pour 1 ou 2")
    if not (d > 0 and n > 0 and -1.0 <= rho_t <= 1.0):
        raise RegleDeLAddendumInapplicable("demi-largeur des sondes : séparation d > 0 et corrélation dans [−1 ; 1] attendues")
    z = 1.645 if m_sondes == 1 else 1.96
    return z * math.sqrt(2.0 * (1.0 - rho_t)) / (d * math.sqrt(n / 2.0))


def choisir_l_effectif(demi_largeurs_par_effectif: dict, taches_du_bassin: int, test_bca_reussi: bool,
                       liste=(60, 90, 120), cible: float = 0.25) -> dict:
    """Effectif n de l'étape 2 : le plus petit de la liste {60, 90, 120} dont la médiane des demi-largeurs sur les 15
    couples juge × famille est ≤ 0,25 ; sinon 120, avec la réserve « puissance faible » ; n/2 ne dépasse jamais le
    nombre de tâches du bassin ; si le test BCa du module échoue, la liste devient {90, 120}."""
    permis = [n for n in liste if (test_bca_reussi or n >= 90) and n // 2 <= taches_du_bassin]
    if not permis:
        raise BassinTropPetit(f"aucun effectif de {list(liste)} permis avec un bassin de {taches_du_bassin} tâches")
    medianes = {}
    for n in permis:
        dl = np.asarray(demi_largeurs_par_effectif[n], dtype=np.float64)
        if dl.size != 15:
            raise RegleDeLAddendumInapplicable(f"effectif {n} : 15 demi-largeurs attendues, {dl.size} reçues")
        medianes[n] = float(np.median(dl))
    for n in permis:
        if medianes[n] <= cible:
            return {"n": n, "medianes": medianes, "reserves": []}
    return {"n": max(permis), "medianes": medianes, "reserves": ["puissance faible"]}


def effectif_a_l_ouverture(n_de_l_addendum: int, taches_du_bassin: int, liste=(60, 90, 120)) -> dict:
    """À l'ouverture de l'étape 2 : n est la plus grande valeur de la liste qui ne dépasse ni la valeur de l'addendum,
    ni deux fois le nombre de tâches du bassin ; plus petite que celle de l'addendum : réserve « puissance faible » ;
    aucune valeur permise : nœud (liste d'arrêt 16)."""
    permis = [n for n in liste if n <= n_de_l_addendum and n <= 2 * taches_du_bassin]
    if not permis:
        raise BassinTropPetit(f"bassin de {taches_du_bassin} tâches : moins de n_min / 2 = {min(liste) // 2} tâches, "
                              "ou aucun effectif permis")
    n = max(permis)
    return {"n": n, "reserves": ["puissance faible"] if n < n_de_l_addendum else []}


def ligne_hc2_non_testable(demi_largeur_sondes: float, marge: float = 0.10) -> bool:
    """Si la demi-largeur prévue dépasse 0,10 à l'effectif retenu, la ligne C-P4 HC2 est écrite d'avance « non testable
    à cette puissance » ; la marge reste 0,10."""
    return bool(demi_largeur_sondes > marge)


# ------------------------------------------------------------------------------------------------------------------
# Dérivation complète, sur tableaux
# ------------------------------------------------------------------------------------------------------------------
def deriver(v0, v_vivier, v_temoins, taches_des_contenus, longueurs_A: dict, longueurs_temoins, v_etoile: float,
            rng_conception: np.random.Generator, taches_du_bassin: int, test_bca_reussi: bool,
            tirages: int = 2000, liste=(60, 90, 120), sondes: dict | None = None) -> dict:
    """Applique les règles de l'addendum aux lectures du vivier (point 1.4).

    `v0` (juges, contenus) ; `v_vivier` {famille: (juges, 16, contenus)} dans l'ordre des familles de la
    configuration ; `v_temoins` (juges, 16, contenus) ; `longueurs_A` {famille: 16 longueurs en caractères des
    formulations remplies pour le corpus A} ; `sondes` (facultatif) : {d, rho_t, m} lus dans les données scellées de
    la porte de sortie de la phase 0 ou du premier test (aucune donnée du papier C)."""
    v0 = np.asarray(v0, dtype=np.float64)
    T16 = np.asarray(v_temoins, dtype=np.float64)
    J, n_cal = v0.shape
    familles = list(v_vivier)
    un = np.ones((1, n_cal))
    variance_de_base = [float(np.std(v0[j], ddof=1)) for j in range(J)]
    vivier, et_formulations, et_famille = {}, {}, {}
    for f in familles:
        vivier[f] = gains_du_vivier(un, v0, v_vivier[f], v_etoile)
        et_formulations[f] = erreurs_types_du_vivier(v0, v_vivier[f], v_etoile, tirages, rng_conception)["erreur_type"]
        et_famille[f] = erreur_type_de_famille(et_formulations[f])
    choisit, mesure = partage_des_taches_de_conception(taches_des_contenus, rng_conception)
    par_effectif, demi_largeurs = {}, {}
    for n in liste:
        retenues, croisees = {}, {}
        for f in familles:
            gbar = vivier[f]["g_sep_moyen"][0]
            km = k_max(gbar, et_famille[f], n_cal, n)
            k = k_retenu(km)
            choix = choisir_formulations(gbar, k["k"])
            temoins = apparier_les_temoins([longueurs_A[f][i - 1] for i in choix["indices_par_rang"]], longueurs_temoins)
            retenues[f] = {"k_max": km, "k": k["k"], "reserves": k["reserves"], **choix, "temoins_par_rang": temoins,
                           "gamma_par_rang": [[float(vivier[f]["gamma"][0, j, i - 1]) for i in choix["indices_par_rang"]]
                                              for j in range(J)]}
            # validation croisée : choix refait sur les contenus des huit tâches qui choisissent
            g_choix = gains_du_vivier(choisit[None, :].astype(np.float64), v0, v_vivier[f], v_etoile)["g_sep_moyen"][0]
            c2 = choisir_formulations(g_choix, k["k"])
            croisees[f] = {"indices": c2["indices_par_rang"],
                           "temoins": apparier_les_temoins([longueurs_A[f][i - 1] for i in c2["indices_par_rang"]],
                                                           longueurs_temoins)}
        temoins_retenus = sorted({t for f in familles for t in croisees[f]["temoins"]})
        dl = []
        for j in range(J):
            W = T16[j][[t - 1 for t in temoins_retenus]][:, mesure]
            for f in familles:
                Vf = np.asarray(v_vivier[f], dtype=np.float64)[j]
                D = np.stack([Vf[i - 1, mesure] - T16[j, t - 1, mesure]
                              for i, t in zip(croisees[f]["indices"], croisees[f]["temoins"])])
                dl.append(demi_largeur_de_lambda(v0[j, mesure], D, W, v_etoile, n_cal, n, tirages,
                                                 rng_conception)["demi_largeur"])
        demi_largeurs[n] = dl
        par_effectif[n] = {"familles": retenues, "demi_largeurs_lambda": dl, "mediane": float(np.median(dl))}
        if sondes is not None:
            par_effectif[n]["demi_largeur_sondes"] = demi_largeur_des_sondes(sondes["d"], n, sondes["m"],
                                                                             sondes.get("rho_t", 0.0))
    effectif = choisir_l_effectif(demi_largeurs, taches_du_bassin, test_bca_reussi, liste)
    sortie = {"n_cal": n_cal, "variance_de_base": variance_de_base, "erreur_type_par_famille": et_famille,
              "gain_maximal_par_famille": {f: float(np.max(vivier[f]["g_sep_moyen"][0])) for f in familles},
              "par_effectif": par_effectif, "effectif": effectif, "retenu": par_effectif[effectif["n"]]}
    if sondes is not None:
        sortie["hc2_non_testable"] = ligne_hc2_non_testable(par_effectif[effectif["n"]]["demi_largeur_sondes"])
    return sortie


__all__ = ["POINTS_ADMIS", "exiger_entree_de_derivation", "lisible", "choisir_variantes", "gains_du_vivier",
           "erreurs_types_du_vivier", "erreur_type_de_famille", "erreur_type_a_l_effectif", "k_max", "k_retenu",
           "choisir_formulations", "apparier_les_temoins", "partage_des_taches_de_conception",
           "demi_largeur_de_lambda", "demi_largeur_des_sondes", "choisir_l_effectif", "effectif_a_l_ouverture",
           "ligne_hc2_non_testable", "deriver"]
