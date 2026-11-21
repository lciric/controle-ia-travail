"""Idée 1.1 — lecture gelée, version 3 (vérification `549e4597…` : N1, format en `GardeArret`, n2 à n5 ; entrée :
`lire_v3`). Version 2 : lecture gelée, version 2 (contre-lecture `8def0cf5…` : M3, m1, m4, m5, m6, m7 ; entrée : `lire_v2`).
Version 1 : lecture gelée (préenregistrement scellé `3ffe1739…`, sections « Métrique », « Seuil », « Cellules »,
« Comparaisons et corrections », « Critères de lecture gelés », « Prédiction chiffrée »). La table des critères écrite en
code ; aucune lecture avant le scellement de la sortie (le lanceur `scripts/lire_idee_1_1_v1.py` refuse une sortie non
scellée).

Entrée : `donnees[nom_de_ligne] = liste des enregistrements des répétitions` (champs écrits par
`banc_idee_1_1_v1.Repetition.evaluer`). Sortie : un dictionnaire par étage, l'issue pour le nœud R-1779, les éléments de
l'audit de symétrie (R4) et l'évaluation des prédictions P1 à P14.
"""
from __future__ import annotations

import functools
import math

import numpy as np
from scipy.stats import beta, binom

from ..gardes import GardeArret
from . import banc_idee_1_1_v2 as B

ALPHA = 0.05
R = 1000
REECHANTILLONS = 10_000
QUANTILES_PRIMAIRES = (0.00833, 0.99167)     # Bonferroni sur trois bras primaires (texte : 0,833 % et 99,167 %)
QUANTILES_SECONDAIRES = (0.025, 0.975)
SEUIL_INFORMATIF = 0.02
TOL_FATALE = 1e-6
SEUIL_AUDIT_COPIE = 1.0
V = [B.NOMS[i] for i in B.LIGNES_V]
# Les 15 lignes V écrites ici d'après le texte seul (seconde écriture, indépendante du banc) : I ⊂ {V} ([CL2] M1).
V_TEXTE = ("V1(0.25)", "V1(0.5)", "V1(0.75)", "V2(0.4)", "V2(0.8)", "V2(1.2)", "V3(0.4)", "V3(0.8)", "V3(1.2)",
           "V4(0.1)", "V4(0.2)", "V4(0.3)", "V5(0.4)", "V5(0.8)", "V5(1.2)")
I_FIXE = False      # I recalculé dans chaque rééchantillon ([CL] m4) ; True seulement sous la mutation qui doit être tuée


def paire_informativite(plus: bool) -> tuple[str, str]:
    """I est fixé par J8 et J9 seuls (I⁺ par J8 et J9⁺) ; jamais par un bras neuf."""
    return ("J8", "J9+") if plus else ("J8", "J9")
V5 = [n for n in V if n.startswith("V5(")]

# --- cellules (section « Cellules (comptes) ») ---------------------------------------------------------------------------
FATALES_HOLM = {"Q1": ("J8", "J9", "La", "Ld", "J9-D40", "J9-D"), "Q2": ("J9", "La", "Ld", "J9-D40", "J9-D"),
                "Q3": ("J9", "Ld", "J9-D40", "J9-D"), "Q4": ("J9", "Ld", "J9-D40", "J9-D"), "Q5": ("J9", "J9-D40", "J9-D")}
FATALES_HORS_HOLM = {"Q9a": ("J8", "J9", "La", "Ld", "J9-D40", "J9-D"), "Q9b": ("J8", "J9", "La", "Ld", "J9-D40", "J9-D")}
COPIES_HOLM = {"Q1": ("J9-P", "La-P"), "Q2": ("J9-P", "La-P"), "Q3": ("J9-P",), "Q4": ("J9-P",), "Q5": ("J9-P",)}
COPIES_HORS_HOLM = {"Q9a": ("J9-P", "La-P"), "Q9b": ("J9-P", "La-P")}
TAILLE = {"Q7": ("J9", "La", "Ld", "J9-P", "La-P", "J9-D40", "J9-D"),
          "Q8": ("J8", "J9", "La", "Ld", "J9-P", "La-P", "J9-D40", "J9-D"),
          "Hs": ("J9", "J9-D40", "J9-D", "J9-P-gel"), "Hm": ("J9", "J9-D40", "J9-D", "J9-P-gel"),
          "Hg": ("J9", "J9-D40", "J9-D", "J9-P-gel"), "Hn": ("J9", "J9-D40", "J9-D", "J9-P-gel"),
          "H7": ("J9-P-gel-terme",)}


def cellules_holm() -> list[tuple[str, str, str]]:
    c = [(l, b, "fatale") for l, bs in FATALES_HOLM.items() for b in bs]
    c += [(l, b, "copie") for l, bs in COPIES_HOLM.items() for b in bs]
    c += [(l, b, "taille") for l, bs in TAILLE.items() for b in bs]
    return c


def exiger_comptes_du_texte() -> None:
    c = cellules_holm()
    fat = sum(len(v) for v in FATALES_HOLM.values()) + sum(len(v) for v in FATALES_HORS_HOLM.values())
    if len(c) != 61 or fat != 34 or sum(1 for x in c if x[2] == "taille") != 32 or sum(1 for x in c if x[2] == "copie") != 7:
        raise GardeArret(f"comptes des cellules ≠ texte (61 Holm, 34 fatales, 32 taille, 7 copies) : {len(c)}, {fat}")


# --- extraction ----------------------------------------------------------------------------------------------------------
def promue(rec: dict, bras: str) -> bool:
    if bras == "J9-P-gel":
        return bool(rec["J9-P-gel"]["complet"]["promue"])
    if bras == "J9-P-gel-terme":
        return bool(rec["J9-P-gel"]["terme_projete"]["promue"])
    if bras == "J9-P-nu-terme":
        return bool(rec["J9-P-nu"]["terme_projete"]["promue"])
    if bras == "J9-P-nu-complet":
        return bool(rec["J9-P-nu"]["complet"]["promue"])
    if bras == "J9-P-nu-lineaire":
        return bool(rec["J9-P-nu"]["lineaire_seul"]["promue"])
    if bras == "J9-P-refus":
        if rec["J9-P-refus"]["promue"]:
            raise GardeArret("J9-P avec refus : une carte refusée est promue")
        return False
    return bool(rec[bras]["promue"])


def log_w_max(rec: dict, bras: str) -> float:
    if bras == "J9-D40":
        return max(rec["J9"]["max"], rec["J9-D40"]["max_40"])
    if bras == "J9-D":
        if "quantite_fatale" not in rec["J9-D"]:
            raise GardeArret("J9-D : quantité fatale absente d'une cellule fatale : lecture refusée")
        return float(rec["J9-D"]["quantite_fatale"])
    if bras == "J9-P-gel":
        return rec["J9-P-gel"]["complet"]["max"]
    if bras == "J9-P-gel-terme":
        return rec["J9-P-gel"]["terme_projete"]["max"]
    return float(rec[bras]["max"])


def vecteur(donnees: dict, ligne: str, bras: str, n: int | None = None) -> np.ndarray:
    recs = donnees[ligne]
    if n is not None:
        recs = recs[:n]
    return np.array([promue(r, bras) for r in recs], dtype=np.int8)


def a_le_bras(donnees: dict, ligne: str, bras: str) -> int:
    """Nombre de premières répétitions où le bras est joué (secondaire réduit : ses seules premières répétitions)."""
    k = 0
    for r in donnees[ligne]:
        cle = "J9-P-gel" if bras.startswith("J9-P-gel") else ("J9-P-nu" if bras.startswith("J9-P-nu") else bras)
        if cle not in r:
            break
        k += 1
    return k


# --- tests et intervalles --------------------------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def cp_bas_unilateral(k: int, n: int, niveau: float = 0.95) -> float:
    return 0.0 if k == 0 else float(beta.ppf(1 - niveau, k, n - k + 1))


def cp_bilateral(k: int, n: int) -> tuple[float, float]:
    bas = 0.0 if k == 0 else float(beta.ppf(0.025, k, n - k + 1))
    haut = 1.0 if k == n else float(beta.ppf(0.975, k + 1, n - k))
    return bas, haut


def holm(pvaleurs: list[float], niveau: float = 0.05) -> list[bool]:
    m = len(pvaleurs)
    ordre = sorted(range(m), key=lambda i: pvaleurs[i])
    rejet = [False] * m
    for rang, i in enumerate(ordre):
        if pvaleurs[i] <= niveau / (m - rang):
            rejet[i] = True
        else:
            break
    return rejet


def statut_taille(comptes: list[tuple[int, int]], niveau: float = 0.05) -> list[str]:
    """Holm dans chaque sens : « tenue » si H₀ « taux ≥ α » est rejetée ; « non tenue » si H₀ « taux ≤ α » est rejetée."""
    p_bas = [float(binom.cdf(k, n, ALPHA)) for k, n in comptes]
    p_haut = [float(binom.sf(k - 1, n, ALPHA)) for k, n in comptes]
    tenue, non_tenue = holm(p_bas, niveau), holm(p_haut, niveau)
    out = []
    for t, nt in zip(tenue, non_tenue):
        out.append("non tenue" if nt else ("tenue" if t else "non jugeable"))
    return out


# --- part regagnée ----------------------------------------------------------------------------------------------------------
def informatives(a: np.ndarray, b: np.ndarray, lignes: list) -> list:
    """a, b : (lignes, R) promotions de J8 et de J9 (ou J9⁺) ; rend les indices des lignes informatives."""
    out = []
    for k in range(a.shape[0]):
        d = a[k] - b[k]
        if np.any(d < 0):
            raise GardeArret(f"ligne {lignes[k]} : J9 promeut sans J8 (monotonie) : lecture refusée")
        if cp_bas_unilateral(int(d.sum()), a.shape[1]) >= SEUIL_INFORMATIF:
            out.append(k)
    return out


def rho(x: np.ndarray, a: np.ndarray, b: np.ndarray, I: list) -> float:
    num = sum(float((x[k] - b[k]).mean()) for k in I)
    den = sum(float((a[k] - b[k]).mean()) for k in I)
    return num / den


def gain_reuni(x: np.ndarray, y: np.ndarray, ens: list) -> float:
    return float(np.mean([float((x[k] - y[k]).mean()) for k in ens]))


def matrice(donnees, lignes, bras, n=None) -> np.ndarray:
    return np.stack([vecteur(donnees, l, bras, n) for l in lignes])


def reechantillons(racine: int, nb_lignes: int, n: int, B_: int = REECHANTILLONS):
    """Indices de rééchantillonnage (graines `(99, b)`) : un tableau (lignes, n) par rééchantillon, mêmes indices pour
    tous les bras (vecteurs appariés)."""
    for b in range(B_):
        rng = B.generateur(racine, 99, b)
        yield rng.integers(0, n, size=(nb_lignes, n))


def lire_rho(racine: int, donnees: dict, bras: list, *, plus: bool = False, n: int | None = None,
             B_: int = REECHANTILLONS, quantiles=QUANTILES_PRIMAIRES, i_fixe: bool = False) -> dict:
    """ρ de chaque bras (estimation, intervalle) sur les 15 lignes V ; I recalculé dans chaque rééchantillon (sauf
    `i_fixe`, réservé à la mutation qui doit être tuée)."""
    if tuple(V) != V_TEXTE:
        raise GardeArret("lignes admises dans I ≠ les 15 lignes V du texte : lecture refusée")
    i_fixe = i_fixe or I_FIXE
    pa, ref = paire_informativite(plus)
    nn = n or min(len(donnees[l]) for l in V)
    a, b = matrice(donnees, V, pa, nn), matrice(donnees, V, ref, nn)
    X = {x: matrice(donnees, V, x, nn) for x in bras}
    I = informatives(a, b, V)
    sortie = {"I": [V[k] for k in I], "n": nn, "reference": ref}
    if len(I) < 2:
        sortie["sans_objet"] = True
        return sortie
    est = {x: rho(X[x], a, b, I) for x in bras}
    tirs = {x: [] for x in bras}
    ecartes = 0
    for idx in reechantillons(racine, len(V), nn, B_):
        ar = np.take_along_axis(a, idx, 1)
        br = np.take_along_axis(b, idx, 1)
        Ir = I if i_fixe else informatives(ar, br, V)
        if len(Ir) < 2:
            ecartes += 1
            continue
        for x in bras:
            tirs[x].append(rho(np.take_along_axis(X[x], idx, 1), ar, br, Ir))
    sortie["ecartes"] = ecartes
    for x in bras:
        t = np.array(tirs[x])
        if t.size == 0:
            raise GardeArret(f"ρ de {x} : tous les rééchantillons écartés (moins de 2 lignes informatives) : lecture refusée")
        sortie[x] = {"estimation": est[x], "bas": float(np.quantile(t, quantiles[0])), "haut": float(np.quantile(t, quantiles[1])),
                     "par_ligne": {V[k]: {"gain": float((X[x][k] - b[k]).mean()), "perte": float((a[k] - b[k]).mean())} for k in I}}
    return sortie


def lire_gain(racine: int, donnees: dict, x: str, y: str, ensemble: str, *, plus: bool = False, B_: int = REECHANTILLONS) -> dict:
    """Gain réuni de x sur y (poids égaux), sur I (recalculé) ou sur les 15 lignes V ; intervalle percentile à 95 %."""
    nn = min(min(a_le_bras(donnees, l, x), a_le_bras(donnees, l, y), len(donnees[l])) for l in V)
    ref = "J9+" if plus else "J9"
    a, b = matrice(donnees, V, "J8", nn), matrice(donnees, V, ref, nn)
    X, Y = matrice(donnees, V, x, nn), matrice(donnees, V, y if not (plus and y == "J9") else "J9+", nn)
    def ens(ar, br):
        return informatives(ar, br, V) if ensemble == "I" else list(range(len(V)))
    E = ens(a, b)
    out = {"x": x, "y": y, "ensemble": ensemble, "n": nn, "reduit": nn < R}
    if len(E) < (2 if ensemble == "I" else 1):
        out["sans_objet"] = True
        return out
    est = gain_reuni(X, Y, E)
    t, ecartes = [], 0
    for idx in reechantillons(racine, len(V), nn, B_):
        ar, br = np.take_along_axis(a, idx, 1), np.take_along_axis(b, idx, 1)
        Er = ens(ar, br)
        if ensemble == "I" and len(Er) < 2:
            ecartes += 1
            continue
        t.append(gain_reuni(np.take_along_axis(X, idx, 1), np.take_along_axis(Y, idx, 1), Er))
    bas, haut = float(np.quantile(t, QUANTILES_SECONDAIRES[0])), float(np.quantile(t, QUANTILES_SECONDAIRES[1]))
    out.update(estimation=est, bas=bas, haut=haut, gain=bas > 0, ecartes=ecartes)
    return out


def verdict_principal(r: dict) -> str:
    if r.get("sans_objet"):
        return "sans objet"
    x = r["J9-P"]
    if x["haut"] < 0:
        return "nuisible"
    if x["bas"] >= 0.25:
        return "regagne"
    if x["haut"] < 0.10:
        return "ne regagne pas"
    return "partiel"


ORDRE_FAVORABLE = ("regagne", "partiel", "ne regagne pas", "nuisible")


def verdict_limite(x: dict) -> str:
    if x["bas"] >= 0.5:
        return "recouvre"
    if x["haut"] < 0.25:
        return "ne recouvre pas"
    return "en partie"


# --- lecture complète --------------------------------------------------------------------------------------------------
def lire(donnees: dict, racine: int, *, B_: int = REECHANTILLONS) -> dict:
    exiger_comptes_du_texte()
    res: dict = {}
    # étage 1 : taille (Holm sur 61 cellules), fatales, nichage et monotonie (déjà gardés pendant le jeu)
    cel = cellules_holm()
    comptes = [(int(vecteur(donnees, l, b).sum()), len(donnees[l])) for l, b, _ in cel]
    statuts = statut_taille(comptes)
    res["cellules_holm"] = [{"ligne": l, "bras": b, "sorte": s, "promotions": k, "n": n, "statut": st}
                            for (l, b, s), (k, n), st in zip(cel, comptes, statuts)]
    fatales = []
    for table in (FATALES_HOLM, FATALES_HORS_HOLM):
        for l, bs in table.items():
            for b in bs:
                k = int(vecteur(donnees, l, b).sum())
                lw = max(log_w_max(r, b) for r in donnees[l])
                fatales.append({"ligne": l, "bras": b, "promotions": k, "log_w_max": lw, "audit": k > 0 or lw > TOL_FATALE})
    res["fatales"] = fatales
    copies = []
    for table in (COPIES_HOLM, COPIES_HORS_HOLM):
        for l, bs in table.items():
            for b in bs:
                lw = max(log_w_max(r, b) for r in donnees[l][:a_le_bras(donnees, l, b)])
                copies.append({"ligne": l, "bras": b, "log_w_max": lw, "audit_optimiseur": lw > SEUIL_AUDIT_COPIE})
    res["copies_projection"] = copies
    trou = any(c["statut"] == "non tenue" for c in res["cellules_holm"]) or any(f["audit"] for f in fatales)
    res["etage_1"] = "trou" if trou else "franchi"
    if trou:
        res["issue"] = "trou : défaut de code, de certificat ou de preuve ; rien d'autre n'est lu ; audit écrit ; nœud"
        return res
    res["etage_1_bis"] = sorted({c["bras"] for c in res["cellules_holm"] if c["statut"] == "non jugeable"})
    # étage 2 : dents
    dents = []
    for b, lignes, seuil in (("J8", ("Q2", "Q3", "Q4", "Q5"), 0.5), ("J9", ("Q6",), 0.5), ("A1", ("Q1", "Q2"), 0.5),
                             ("A2", ("Q1", "Q2"), 0.05)):
        for l in lignes:
            k, n = int(vecteur(donnees, l, b).sum()), len(donnees[l])
            dents.append({"bras": b, "ligne": l, "promotions": k, "borne_basse": cp_bas_unilateral(k, n), "tenue": cp_bas_unilateral(k, n) > seuil})
    res["dents"] = dents
    if not all(d["tenue"] for d in dents):
        res["etage_2"] = "banc sans dents (non concluant)"
        res["issue"] = res["etage_2"]
        return res
    res["etage_2"] = "franchi"
    # étage 3 à 5 : part regagnée
    rp = lire_rho(racine, donnees, ["J9-P", "La", "Ld"], B_=B_)
    res["rho"] = rp
    if rp.get("sans_objet"):
        res["etage_3"] = "prix du v9 non reproduit sur ce banc (non concluant sur H-1.1 v2)"
        res["principale"] = "sans objet"
    else:
        res["etage_3"] = "franchi"
        v = verdict_principal(rp)
        rpp = lire_rho(racine, donnees, ["J9-P"], plus=True, B_=B_)
        res["rho_plus"] = rpp
        if rpp.get("sans_objet"):
            res["principale"], res["sensible_au_certificat"] = "non tranché", True
        else:
            vp = verdict_principal(rpp)
            if vp != v:
                res["sensible_au_certificat"] = True
                v = max(v, vp, key=ORDRE_FAVORABLE.index)
            else:
                res["sensible_au_certificat"] = False
            res["principale"] = v
        res["La"], res["Ld"] = verdict_limite(rp["La"]), verdict_limite(rp["Ld"])
    # étage 6 : secondaires
    res["secondaires"] = {k: lire_gain(racine, donnees, x, y, e, B_=B_) for k, (x, y, e) in {
        "La-P contre La": ("La-P", "La", "I"), "J9-P contre La": ("J9-P", "La", "I"),
        "J9-D contre J9": ("J9-D", "J9", "V"), "J9-D40 contre J9": ("J9-D40", "J9", "V")}.items()}
    # étage 7 : garde P4
    res["garde_P4"] = lire_garde(donnees, res["cellules_holm"])
    # étage 8 : rapportés
    res["etage_8"] = lire_etage_8(donnees, rp)
    res["issue"] = issue(res)
    res["audit_symetrie"] = audit(donnees, res)
    res["predictions"] = predictions(donnees, res)
    return res


def lire_garde(donnees: dict, cellules: list) -> dict:
    def taux(l, b):
        v = vecteur(donnees, l, b)
        return int(v.sum()), len(v)
    k, n = taux("H7", "J9-P-nu-terme")
    dent_h7 = cp_bas_unilateral(k, n) > 0.05
    tenues = {c["ligne"]: c["statut"] for c in cellules if c["bras"] in ("J9-P-gel", "J9-P-gel-terme")}
    gel_tenu = all(tenues[l] == "tenue" for l in ("Hs", "Hm", "Hg", "Hn", "H7"))
    trou = {l: cp_bas_unilateral(*taux(l, "J9-P-nu-complet")) > 0.05 for l in ("Hm", "Hg")}
    kn, nn = taux("Hn", "J9-P-nu-lineaire")
    out = {"dent_H7_terme_projete": {"promotions": k, "n": n, "passee": dent_h7}, "gel_tenu_sur_les_cinq": gel_tenu,
           "trou_atteint_par_la_grammaire": trou,
           "Hn_terme_lineaire": {"promotions": kn, "n": nn, "trou_montre_dans_la_grammaire": cp_bas_unilateral(kn, nn) > 0.05},
           "rapportes": {l: {q: taux(l, q) for q in ("J9-P-nu-terme", "J9-P-nu-complet")} for l in ("H7", "Hn", "Hs", "Hm", "Hg")}}
    # m4 : trois lectures rendues à part, sans priorité entre elles (le texte n'en écrit pas)
    out["lectures"] = {"nécessaire, montrée sur le terme projeté": bool(dent_h7 and gel_tenu),
                       "non éprouvée (dent du terme projeté de H7 manquée)": not dent_h7,
                       "trou atteint par la grammaire (Hm ou Hg, juge complet sans garde)": any(trou.values())}
    if not gel_tenu:
        out["cellule_avec_gel_non_tenue_ou_non_jugeable"] = sorted(l for l, s in tenues.items() if s != "tenue")
    out["reserve"] = "aucune de ces lectures ne conclut que la grammaire est sûre sans garde"
    return out


def lire_etage_8(donnees: dict, rp: dict) -> dict:
    out = {"copies_rouvertes": {}, "protection_Q9": {}, "strate_sans_log": {}}
    for b in ("La", "Ld", "La-P"):
        for l in ("Q2", "Q3", "Q4", "Q5", "Q6"):
            k, n = int(vecteur(donnees, l, b).sum()), len(donnees[l])
            out["copies_rouvertes"][f"{b}|{l}"] = {"taux": k / n, "intervalle": cp_bilateral(k, n)}
    for l in ("Q9a", "Q9b"):
        out["protection_Q9"][l] = {b: int(vecteur(donnees, l, b, a_le_bras(donnees, l, b)).sum())
                                   for b in ("J8", "J9", "La", "Ld", "J9-D40", "J9-D", "J9-P", "La-P")}
    if not rp.get("sans_objet"):
        out["decomposition_du_prix"] = {"1 - rho_La": 1 - rp["La"]["estimation"], "rho_La - rho_Ld": rp["La"]["estimation"] - rp["Ld"]["estimation"],
                                         "rho_Ld": rp["Ld"]["estimation"]}
    for l in V:
        recs = [r for r in donnees[l] if "strate_sans_log" in r]
        if recs:
            out["strate_sans_log"][l] = {b: sum(bool(r["strate_sans_log"][b]["promue"]) for r in recs) for b in ("J8", "J9", "La", "J9-P")}
    return out


def issue(res: dict) -> str:
    p = res.get("principale")
    if res.get("etage_3") != "franchi":
        return "non concluant sur H-1.1 v2 (étage 3)"
    if p == "non tranché":
        return "(D) non tranché (sensible au certificat : I⁺ compte moins de 2 lignes), avec les estimations"
    if p == "regagne":
        return "(A) J9-P regagne : un candidat v10 de même classe que le v9 existe sur ce banc, sous la garde P4 ; à valider à part"
    if p != "regagne" and res.get("La") == "recouvre":
        s = "(B) J9-P ne regagne pas, La recouvre : un nul moins coûteux n'existe sur ce banc qu'en rétrécissant la classe"
        return s + (" ; Ld recouvre aussi" if res.get("Ld") == "recouvre" else "")
    if p == "ne regagne pas" and res.get("La") != "recouvre" and res.get("Ld") != "recouvre":
        return "(C) aucune voie de cette famille ne reprend le prix ; restent « accepter le prix » et la règle de lecture (étage 6)"
    return "(D) non tranché, avec les estimations"


def audit(donnees: dict, res: dict) -> dict:
    """Éléments de l'audit de symétrie (R4), écrits avant le prononcé ; « trop propre » et « tout négatif »."""
    out = {}
    j9p_sans_j8 = {}
    for l in V:
        x, a = vecteur(donnees, l, "J9-P"), vecteur(donnees, l, "J8")
        j9p_sans_j8[l] = int(((x == 1) & (a == 0)).sum())
    out["J9-P promeut, J8 non"] = j9p_sans_j8
    cert = [r["journal_J9-P"]["c_moins_1_max"] for l in donnees for r in donnees[l] if "journal_J9-P" in r]
    out["certificats_c_moins_1_max"] = {"n": len(cert), "max": max(cert) if cert else None, "tous_nuls": bool(cert) and max(cert) == 0.0}
    ecarts = [max(r[c]) for l in donnees for r in donnees[l] for c in ("ecart_residuel_J9", "ecart_residuel_La", "ecart_residuel_Ld") if c in r]
    out["part_ecart_residuel_superieur_2e-3"] = float(np.mean(np.array(ecarts) > 2e-3)) if ecarts else None
    egal_p = all((vecteur(donnees, l, "J9-P") == vecteur(donnees, l, "J9")).all() for l in V)
    egal_d40 = all((vecteur(donnees, l, "J9-D40", a_le_bras(donnees, l, "J9-D40")) ==
                    vecteur(donnees, l, "J9", a_le_bras(donnees, l, "J9-D40"))).all() for l in V)
    out["tout_negatif"] = {"J9-P egal a J9": egal_p, "certificats tous egaux a 1": out["certificats_c_moins_1_max"]["tous_nuls"],
                           "J9-D40 egal a J9": egal_d40}
    rp = res.get("rho", {})
    if "J9-P" in rp:
        parts = [d["gain"] / d["perte"] for d in rp["J9-P"]["par_ligne"].values() if d["perte"] > 0]
        out["trop_propre"] = {"part regagnee extreme sur toutes les lignes": bool(parts) and all(p >= 0.95 or p <= 0.05 for p in parts),
                              "gain identique sur toutes les lignes": bool(parts) and len(set(round(p, 12) for p in parts)) == 1}
    taille_j9p = sum(c["promotions"] for c in res.get("cellules_holm", []) if c["bras"].startswith("J9-P") and c["sorte"] == "taille")
    out.setdefault("trop_propre", {})["aucune promotion dans les cellules de taille de J9-P"] = taille_j9p == 0
    return out


def predictions(donnees: dict, res: dict) -> dict:
    """Prédictions P1 à P14, chacune « vraie », « fausse » ou « non évaluable » (réfutation écrite au texte)."""
    def taux(l, b):
        n = a_le_bras(donnees, l, b)
        if n == 0:
            raise GardeArret(f"prédictions : bras {b} absent de la ligne {l}")
        return float(vecteur(donnees, l, b, n).mean())
    p = {}
    p["P1"] = all(f["promotions"] == 0 and f["log_w_max"] <= TOL_FATALE for f in res["fatales"])
    p2 = [c for c in res["cellules_holm"] if c["sorte"] in ("copie", "taille")]
    p["P2"] = all(c["promotions"] / c["n"] <= 0.03 and c["statut"] == "tenue" for c in p2)
    p["P3"] = (all(taux(l, "J8") >= 0.90 for l in ("Q2", "Q3", "Q4", "Q5")) and taux("Q6", "J9") >= 0.80 and taux("Q6", "J9-P") >= 0.60
               and all(taux(l, "A1") >= 0.90 and taux(l, "A2") >= 0.30 for l in ("Q1", "Q2")))
    p["P4"] = all(taux(l, b) >= 0.85 for l in ("Q3", "Q4", "Q5") for b in ("La", "La-P")) and taux("Q5", "Ld") >= 0.60
    rp = res.get("rho", {})
    if "I" in rp:
        p["P5"] = True if len(rp["I"]) >= 4 else ("partielle" if len(rp["I"]) >= 2 else False)
    else:
        p["P5"] = "non évaluable"
    if "J9-P" in rp:
        p["P6"] = 0.25 <= rp["J9-P"]["estimation"] <= 0.60 and res.get("principale") == "regagne"
        v5 = [rp["La"]["par_ligne"][l] for l in V5 if l in rp["La"]["par_ligne"]]
        v5ok = (sum(d["gain"] for d in v5) / sum(d["perte"] for d in v5) <= 0.3) if v5 and sum(d["perte"] for d in v5) > 0 else True
        p["P7"] = rp["La"]["bas"] >= 0.5 and 0.6 <= rp["La"]["estimation"] <= 0.9 and v5ok
        p["P8"] = rp["Ld"]["estimation"] <= rp["La"]["estimation"] and 0.35 <= rp["Ld"]["estimation"] <= 0.80
    s = res.get("secondaires", {})
    def dans(k, a, b):
        x = s.get(k, {})
        return (a <= x["estimation"] <= b) if "estimation" in x else "non évaluable"
    p["P9"] = dans("La-P contre La", 0.02, 0.10)
    d1, d2 = dans("J9-D contre J9", 0.010, 0.040), dans("J9-D40 contre J9", 0.005, 0.025)
    p["P10"] = (d1 and d2) if isinstance(d1, bool) and isinstance(d2, bool) else "non évaluable"
    p["P11"] = dans("J9-P contre La", -0.11, 0.03)
    g = {l: {b: taux(l, b) for b in ("J9-P-nu-terme", "J9-P-nu-complet", "J9-P-gel", "J9-P-gel-terme")} for l in ("Hs", "Hm", "Hg", "Hn", "H7")}
    def bb(l, b):  # borne basse unilatérale à 95 % du taux
        n = a_le_bras(donnees, l, b)
        return cp_bas_unilateral(int(vecteur(donnees, l, b, n).sum()), n)
    statut = {c["ligne"]: c["statut"] for c in res["cellules_holm"] if c["bras"] in ("J9-P-gel", "J9-P-gel-terme")}
    # m7 : chaque partie lue sur sa réfutation écrite (colonne « ce qui la réfute »)
    p["P12"] = {"H7 terme projeté (réfutée si borne basse <= 0,05)": bb("H7", "J9-P-nu-terme") > 0.05,
                "gel (réfutée si une cellule non tenue)": all(statut[l] != "non tenue" for l in ("Hs", "Hm", "Hg", "Hn", "H7")),
                "Hm, Hg sans garde (réfutée si borne basse > 0,05)": bb("Hm", "J9-P-nu-complet") <= 0.05 and bb("Hg", "J9-P-nu-complet") <= 0.05,
                "Hs, Hn juge complet (réfutée si borne basse > 0,05)": bb("Hs", "J9-P-nu-complet") <= 0.05 and bb("Hn", "J9-P-nu-complet") <= 0.05,
                "Hn terme linéaire (réserve si borne basse <= 0,05)": bb("Hn", "J9-P-nu-lineaire") > 0.05,
                "H7 juge complet (rapporté, sans seuil)": "rapporté", "_chiffres": g}
    q9 = [taux(l, b) for l in ("Q9a", "Q9b") for b in ("J8", "J9", "La", "Ld", "J9-D40", "J9-D", "J9-P", "La-P")]
    lwp = [max(r[b]["max"] for r in donnees[l][:a_le_bras(donnees, l, b)]) for l in ("Q9a", "Q9b") for b in ("J9-P", "La-P")]
    p["P13"] = all(t == 0 for t in q9) and all(x <= 0.5 for x in lwp)
    diff = [np.mean(vecteur(donnees, l, "J9") != vecteur(donnees, l, "J9+")) for l in V]
    p["P14"] = bool(np.mean(diff) < 0.005) and not res.get("sensible_au_certificat", False)
    toutes = [v is True for k, v in p.items() if isinstance(v, bool) or v == "partielle"] + [v for v in p["P12"].values() if isinstance(v, bool)]
    res_trop = all(toutes)
    return {"evaluation": p, "toutes_vraies": res_trop}


# ==================================================================================================================
# Version 2 (contre-lecture du code `8def0cf5…`) : M3 — tout ce que la « Métrique » gèle comme rapporté ; m1, m4, m5,
# m6 (déclaré), m7. Les ajouts ne portent aucun verdict.
#
# m6 (déclaré, sans changement de code) : pour un secondaire réduit, I est recalculé sur ses seules premières
# répétitions (le texte : « lu, apparié, sur ses seules premières répétitions »), pas repris des 1 000.

# Strates de ρ par bras ([CL] M1) — lecture du texte écrite avant le jeu : « structure sur une partition du bras » si
# l'effet neuf de la ligne est posé sur une partition de la classe du bras. V1 : effet global (aucune partition) ; V2 :
# signe d'un trait ; V3 : seuil décentré d'un trait ; V4 : sous-population ; V5 : coupure A de l'archive. Partitions :
# J9-P (classe du v9) — sous-population et tout seuil réel d'un trait ; La — coupures A et B de l'archive ; Ld — La,
# sous-population et signe de chaque trait.
STRATES_TEXTE = {
    "J9-P": {"sur": ("V2", "V3", "V4", "V5"), "hors": ("V1",)},
    "La": {"sur": ("V5",), "hors": ("V1", "V2", "V3", "V4")},
    "Ld": {"sur": ("V2", "V4", "V5"), "hors": ("V1", "V3")},
}


def lignes_de_strate(bras: str, strate: str) -> list:
    types = STRATES_TEXTE[bras][strate]
    return [l for l in V_TEXTE if l.split("(")[0] in types]


def lire_rho_strate(racine: int, donnees: dict, bras: str, strate: str, *, plus: bool = False, B_: int = REECHANTILLONS) -> dict:
    """ρ du bras restreint aux lignes informatives de la strate ; I recalculé dans chaque rééchantillon sur les 15 lignes V,
    puis coupé à la strate ; rééchantillon sans ligne informative dans la strate écarté et compté ; quantiles de
    Bonferroni des primaires (rapporté, sans verdict)."""
    pa, ref = paire_informativite(plus)
    nn = min(len(donnees[l]) for l in V)
    a, b = matrice(donnees, V, pa, nn), matrice(donnees, V, ref, nn)
    X = matrice(donnees, V, bras, nn)
    dans = [k for k, l in enumerate(V) if l in lignes_de_strate(bras, strate)]
    I = [k for k in informatives(a, b, V) if k in dans]
    out = {"bras": bras, "strate": strate, "lignes": [V[k] for k in dans], "I": [V[k] for k in I], "reference": ref}
    if not I:
        out["sans_objet"] = True
        return out
    t, ecartes = [], 0
    for idx in reechantillons(racine, len(V), nn, B_):
        ar, br = np.take_along_axis(a, idx, 1), np.take_along_axis(b, idx, 1)
        Ir = [k for k in informatives(ar, br, V) if k in dans]
        if not Ir:
            ecartes += 1
            continue
        t.append(rho(np.take_along_axis(X, idx, 1), ar, br, Ir))
    if not t:
        raise GardeArret(f"strate {bras}|{strate} : tous les rééchantillons écartés : lecture refusée")
    out.update(estimation=rho(X, a, b, I), bas=float(np.quantile(t, QUANTILES_PRIMAIRES[0])),
               haut=float(np.quantile(t, QUANTILES_PRIMAIRES[1])), ecartes=ecartes)
    return out


def lire_decomposition(racine: int, donnees: dict, *, B_: int = REECHANTILLONS) -> dict:
    """Décomposition du prix (descriptive) : 1 − ρ_La, ρ_La − ρ_Ld, ρ_Ld, avec intervalles percentiles à 95 % tirés des
    mêmes rééchantillons pour La et Ld (vecteurs appariés)."""
    nn = min(len(donnees[l]) for l in V)
    a, b = matrice(donnees, V, "J8", nn), matrice(donnees, V, "J9", nn)
    Xa, Xd = matrice(donnees, V, "La", nn), matrice(donnees, V, "Ld", nn)
    I = informatives(a, b, V)
    if len(I) < 2:
        return {"sans_objet": True}
    f = lambda ra, rd: {"1 - rho_La": 1 - ra, "rho_La - rho_Ld": ra - rd, "rho_Ld": rd}
    est = f(rho(Xa, a, b, I), rho(Xd, a, b, I))
    tirs = {k: [] for k in est}
    ecartes = 0
    for idx in reechantillons(racine, len(V), nn, B_):
        ar, br = np.take_along_axis(a, idx, 1), np.take_along_axis(b, idx, 1)
        Ir = informatives(ar, br, V)
        if len(Ir) < 2:
            ecartes += 1
            continue
        for k, v in f(rho(np.take_along_axis(Xa, idx, 1), ar, br, Ir), rho(np.take_along_axis(Xd, idx, 1), ar, br, Ir)).items():
            tirs[k].append(v)
    if not tirs["rho_Ld"]:
        raise GardeArret("décomposition du prix : tous les rééchantillons écartés : lecture refusée")
    out = {k: {"estimation": est[k], "bas": float(np.quantile(tirs[k], QUANTILES_SECONDAIRES[0])),
               "haut": float(np.quantile(tirs[k], QUANTILES_SECONDAIRES[1]))} for k in est}
    out["ecartes"] = ecartes
    out["niveau"] = "percentile bilatéral à 95 % (lecture déclarée)"
    return out


def mcnemar_exact(x: np.ndarray, y: np.ndarray) -> dict:
    """Test exact de McNemar (bilatéral) sur des vecteurs appariés de promotions."""
    n10, n01 = int(((x == 1) & (y == 0)).sum()), int(((x == 0) & (y == 1)).sum())
    n = n10 + n01
    p = 1.0 if n == 0 else min(1.0, 2.0 * float(binom.cdf(min(n10, n01), n, 0.5)))
    return {"x_seul": n10, "y_seul": n01, "p": p}


PAIRES_MCNEMAR = (("J8", "J9"), ("J9-P", "J9"), ("La", "J9"), ("Ld", "J9"), ("La-P", "La"), ("J9-P", "La"),
                  ("J9-D", "J9"), ("J9-D40", "J9"), ("J9-P", "J9+"), ("La", "J9+"), ("Ld", "J9+"),
                  ("J9-D", "J9+"), ("J9-D40", "J9+"))                       # v3, n3 : J9-D et J9-D40 contre J9⁺
PAIRES_MCNEMAR_V3 = PAIRES_MCNEMAR


def lire_mcnemar(donnees: dict) -> dict:
    out = {}
    for l in V:
        for x, y in PAIRES_MCNEMAR:
            n = min(a_le_bras(donnees, l, x), a_le_bras(donnees, l, y))
            out[f"{l}|{x} contre {y}"] = {**mcnemar_exact(vecteur(donnees, l, x, n), vecteur(donnees, l, y, n)), "n": n}
    return out


def _lw_rep(r: dict, bras: str) -> float:
    if bras == "J9-P-nu-terme":
        return r["J9-P-nu"]["terme_projete"]["max"]
    if bras == "J9-P-nu-complet":
        return r["J9-P-nu"]["complet"]["max"]
    if bras == "J9-P-nu-lineaire":
        return r["J9-P-nu"]["lineaire_seul"]["max"]
    if bras == "J9-P-refus":
        return -math.inf
    if bras == "A2":                      # v3, N1 : A2 n'a qu'une lecture, à t = 200 (texte : « lu à 200 »)
        return r["A2"]["log_w_200"]
    return log_w_max(r, bras)


def taux_des_cellules(donnees: dict) -> dict:
    """Pour chaque (ligne, bras) joué : taux, intervalle de Clopper-Pearson bilatéral à 95 %, log W maximal et médian
    (sur les répétitions, du log W maximal de chacune). Pour J9-D, « log W » est la quantité fatale quand elle existe."""
    out = {}
    bras_possibles = ("J8", "J9", "J9+", "La", "Ld", "J9-D40", "J9-D", "J9-Dc", "J9-P", "La-P", "A1", "A2", "J9-P-gel",
                      "J9-P-gel-terme", "J9-P-nu-terme", "J9-P-nu-complet", "J9-P-nu-lineaire", "temoin_lambda")
    for l in donnees:
        for b in bras_possibles:
            n = a_le_bras(donnees, l, b)
            if n == 0:
                continue
            v = vecteur(donnees, l, b, n)
            k = int(v.sum())
            d = {"promotions": k, "n": n, "taux": k / n, "intervalle": list(cp_bilateral(k, n))}
            if b not in ("J9-Dc", "temoin_lambda") and not (b == "J9-D" and "quantite_fatale" not in donnees[l][0].get("J9-D", {})):
                lws = np.array([_lw_rep(r, b) for r in donnees[l][:n]])
                d.update(log_w_max=float(lws.max()), log_w_mediane=float(np.median(lws)))
            out[f"{l}|{b}"] = d
    return out


def lire_v2(donnees: dict, racine: int, *, B_: int = REECHANTILLONS) -> dict:
    """Lecture gelée v2 : la lecture v1 (verdicts inchangés), plus les rapportés de la « Métrique » (M3), les trois
    lectures séparées de la garde P4 (m4), la part des écarts résiduels sur J9, La et Ld (m5), et P5 et P12 lues sur
    leurs réfutations écrites (m7)."""
    res = lire(donnees, racine, B_=B_)
    res["taux_des_cellules"] = taux_des_cellules(donnees)
    if res.get("etage_1") != "franchi" or res.get("etage_2") != "franchi":
        return res
    res["secondaires_contre_J9_plus"] = {k: lire_gain(racine, donnees, x, y, e, plus=True, B_=B_) for k, (x, y, e) in {
        "La-P contre La": ("La-P", "La", "I"), "J9-P contre La": ("J9-P", "La", "I"),
        "J9-D contre J9+": ("J9-D", "J9", "V"), "J9-D40 contre J9+": ("J9-D40", "J9", "V")}.items()}
    res["rho_par_strate"] = {f"{b}|{s}": lire_rho_strate(racine, donnees, b, s, B_=B_) for b in STRATES_TEXTE for s in ("sur", "hors")}
    res["decomposition_du_prix_intervalles"] = lire_decomposition(racine, donnees, B_=B_)
    res["mcnemar"] = lire_mcnemar(donnees)
    res["declaration_m6"] = "secondaire réduit : I recalculé sur ses seules premières répétitions"
    return res


# ==================================================================================================================
# Version 3 (vérification du différentiel v1 → v2, `549e4597…`) : N1 (A2 lu à 200 dans les rapportés), erreurs de format
# rendues en `GardeArret` (`verifier_format`, `lire_v3`), n2 à n5, lectures déclarées (`LECTURES_DECLAREES`).
LECTURES_DECLAREES = {
    "strates_de_rho": "tableau STRATES_TEXTE (J9-P : V2 à V5 sur, V1 hors ; La : V5 sur, V1 à V4 hors ; Ld : V2, V4, V5 sur, "
                      "V1 et V3 hors), pour les trois primaires seulement",
    "regle_des_strates (n2)": "une strate est lue si elle compte au moins une ligne informative ; un rééchantillon sans ligne "
                              "informative dans la strate est écarté et compté ; quantiles de Bonferroni des primaires",
    "decomposition_du_prix (n4)": "intervalle percentile bilatéral à 95 % (niveau non écrit au texte) ; rééchantillons à moins de "
                                  "2 lignes informatives écartés et comptés",
    "mcnemar (n3)": "exact bilatéral, sur les 15 lignes V, paires " + "; ".join(f"{x} contre {y}" for x, y in PAIRES_MCNEMAR_V3),
    "rho_plus_primaires (n5)": "ρ⁺ de J9-P, La et Ld rapporté (quantiles de Bonferroni) ; le verdict principal reste lu sur le "
                               "seul ρ⁺ de J9-P, calculé à part et inchangé",
    "m6": "secondaire réduit : I recalculé sur ses seules premières répétitions",
}

# Champs exigés de chaque enregistrement (écrits par `banc_idee_1_1_v2.Repetition.evaluer`) ; les groupes que la règle de
# réduction peut retirer ne sont exigés que sur un préfixe des répétitions (une fois absents, absents jusqu'au bout).
CHAMPS_SANS_MEMOIRE = {"J8": ("promue", "max"), "J9": ("promue", "max"), "J9+": ("promue", "max"), "La": ("promue", "max"),
                       "Ld": ("promue", "max"), "A1": ("promue", "max"), "A2": ("promue", "log_w_200"),
                       "ecart_residuel_J9": None, "ecart_residuel_La": None, "ecart_residuel_Ld": None}
CHAMPS_REDUCTIBLES = {"J9-D40": ("promue", "max_40"), "J9-D": ("promue",), "J9-P": ("promue", "max"),
                      "La-P": ("promue", "max"), "journal_J9-P": ("c_moins_1_max",)}
CHAMPS_H = {"J9-P-refus": ("refusee", "promue"), "J9-P-nu": ("terme_projete", "complet", "lineaire_seul"),
            "J9-P-gel": ("terme_projete", "complet")}
CHAMPS_H_JUGE = {"J9": ("promue", "max"), "J9-D40": ("promue", "max_40"), "J9-D": ("promue",)}


def verifier_format(donnees: dict) -> None:
    """Toute différence de format entre le banc et la lecture arrête avec un message (jamais une trace)."""
    if set(donnees) != set(B.NOMS):
        raise GardeArret(f"format : lignes {sorted(set(B.NOMS) - set(donnees))} absentes ou en trop : lecture refusée")
    for l, recs in donnees.items():
        if not recs:
            raise GardeArret(f"format : ligne {l} sans répétition : lecture refusée")
        if l in B.LIGNES_H:
            exiges = dict(CHAMPS_H, **({} if l == "H7" else CHAMPS_H_JUGE))
            reductibles = {}
        else:
            exiges = dict(CHAMPS_SANS_MEMOIRE)
            reductibles = dict(CHAMPS_REDUCTIBLES)
            if l in FATALES_HOLM or l in FATALES_HORS_HOLM:
                reductibles["J9-D"] = ("promue", "quantite_fatale")
        absents_depuis = {}
        for k, r in enumerate(recs):
            if not isinstance(r, dict) or r.get("r") != k:
                raise GardeArret(f"format : ligne {l}, répétition {k} : enregistrement illisible ou hors d'ordre : lecture refusée")
            for cle, sous in exiges.items():
                if cle not in r:
                    raise GardeArret(f"format : ligne {l}, répétition {k} : champ « {cle} » absent : lecture refusée")
                for s in (sous or ()):
                    if s not in r[cle]:
                        raise GardeArret(f"format : ligne {l}, répétition {k} : champ « {cle}.{s} » absent : lecture refusée")
            for cle, sous in reductibles.items():
                if cle in r:
                    if cle in absents_depuis:
                        raise GardeArret(f"format : ligne {l} : « {cle} » réapparaît après une réduction : lecture refusée")
                    for s in sous:
                        if s not in r[cle]:
                            raise GardeArret(f"format : ligne {l}, répétition {k} : champ « {cle}.{s} » absent : lecture refusée")
                else:
                    absents_depuis.setdefault(cle, k)
            if l in B.LIGNES_H and l != "H7":
                for q in ("terme_projete", "complet", "lineaire_seul"):
                    if not {"promue", "max"} <= set(r["J9-P-nu"][q]):
                        raise GardeArret(f"format : ligne {l}, répétition {k} : « J9-P-nu.{q} » incomplet : lecture refusée")
        if l in B.LIGNES_V and ("J9-D" in absents_depuis and absents_depuis["J9-D"] == 0):
            raise GardeArret(f"format : ligne {l} sans engagement jumeau : lecture refusée")


def lire_v3(donnees: dict, racine: int, *, B_: int = REECHANTILLONS) -> dict:
    """Lecture gelée v3 : format vérifié d'abord ; puis `lire_v2` (verdicts inchangés) ; ρ⁺ des trois primaires rapporté
    (n5) ; lectures déclarées jointes. Une erreur de format qui échapperait à `verifier_format` est rendue en `GardeArret`
    avec son message, jamais en trace."""
    verifier_format(donnees)
    try:
        res = lire_v2(donnees, racine, B_=B_)
        if res.get("etage_1") == "franchi" and res.get("etage_2") == "franchi" and not res["rho"].get("sans_objet"):
            res["rho_plus_primaires"] = lire_rho(racine, donnees, ["J9-P", "La", "Ld"], plus=True, B_=B_)
    except GardeArret:
        raise
    except (KeyError, TypeError, IndexError, ValueError, AttributeError) as e:
        raise GardeArret(f"lecture : format ou valeur inattendus ({type(e).__name__} : {e}) : lecture refusée") from e
    res["lectures_declarees"] = dict(LECTURES_DECLAREES)
    res["version_lecture"] = 3
    return res
