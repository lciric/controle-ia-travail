"""Lectures et règles de décision du volet A de « Neuron Lens » (Qwen3-8B) — v1.

Met en œuvre, sans rien y changer, les sections « Métrique » (A.1, A.3, A.4) et « Seuil » (A) et les critères de lecture du volet A du
texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`
(`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`). Aucun modèle ici : les fonctions prennent des tableaux déjà
calculés (matrices de lentille, plongements, poids de sonde, AUROC) ; les passes du modèle sont ailleurs.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import spearmanr

POSITIVE, NEGATIVE, INDECISE, SANS_OBJET = "positive", "négative", "indécise", "sans objet"


# ---------------------------------------------------------------- lectures (Métrique A.1)
def ramener_au_flux(w_std, sigma):
    """Poids d'une sonde sur traits centrés-réduits → covecteur du flux brut, normé à 1 (`w_brut = w / σ`)."""
    w = np.asarray(w_std, dtype=np.float64) / np.asarray(sigma, dtype=np.float64)
    return w / np.linalg.norm(w)


def empreintes(E, gardes, K=None):
    """Lignes `K (W_E[v] − m)` pour les jetons gardés (`m` : moyenne de W_E sur les gardés) ; sans K : `W_E[v] − m`.
    E : [V, d] ; K : [d, d] (sortie de la couche ← plongements) ; rend [n_gardés, d]."""
    Eg = np.asarray(E, dtype=np.float64)[gardes]
    Ec = Eg - Eg.mean(0)
    return Ec if K is None else Ec @ np.asarray(K, dtype=np.float64).T


def stats_reference(F, n_ref=1000, graine=None):
    """μ_v, σ_v des scores `F[v] · u` sur `n_ref` covecteurs unitaires gaussiens (Métrique A.1, point 4)."""
    rng = np.random.default_rng(graine)
    U = rng.normal(size=(n_ref, F.shape[1]))
    U /= np.linalg.norm(U, axis=1, keepdims=True)
    S = F @ U.T
    return S.mean(1), S.std(1)


def lecture_z(F, w, mu, sd):
    return (F @ w - mu) / sd


def rangs(z):
    """Rang de chaque jeton (1 = score le plus haut)."""
    ordre = np.argsort(-z, kind="stable")
    r = np.empty_like(ordre)
    r[ordre] = np.arange(1, len(z) + 1)
    return r


def meilleur_rang_deux_signes(F, w, mu, sd, idx_P):
    """Meilleur rang d'un jeton de P dans les lectures `_z` de +w et de −w."""
    return int(min(rangs(lecture_z(F, w, mu, sd))[idx_P].min(), rangs(lecture_z(F, -w, mu, sd))[idx_P].min()))


# ---------------------------------------------------------------- règle de couche
def regle_couche(conditions_par_decoupe):
    """5 découpes : positive si la condition tient dans ≥ 3, négative si dans ≤ 1, indécise sinon."""
    k = int(sum(bool(c) for c in conditions_par_decoupe))
    return POSITIVE if k >= 3 else NEGATIVE if k <= 1 else INDECISE


# ---------------------------------------------------------------- A1
def condition_a1(rang_s, rangs_temoins):
    """Une découpe, une couche : un jeton de P dans les 10 premiers de S, et dans les 10 premiers d'aucun témoin (directions
    aléatoires, sonde à étiquettes permutées, direction de C3 ; chacun lu sur les deux signes)."""
    return rang_s <= 10 and all(r > 10 for r in rangs_temoins)


def verdict_a1(classes_couches):
    pos = sum(c == POSITIVE for c in classes_couches)
    if pos >= 2:
        return "retrouvée"
    if all(c == NEGATIVE for c in classes_couches):
        return "non retrouvée"
    return "partielle"


# ---------------------------------------------------------------- A2
def rho_a2(z_s, poids_sac, presents):
    """ρ de Spearman entre la lecture S `_z` de w et les poids du sac de jetons, sur les jetons gardés présents (masque)."""
    return float(spearmanr(np.asarray(z_s)[presents], np.asarray(poids_sac)[presents]).statistic)


def condition_a2(rho_s, rhos_aleatoires):
    return rho_s > float(np.quantile(rhos_aleatoires, 0.99))


def a2_sans_objet(auroc_sac_c1_moyenne):
    return auroc_sac_c1_moyenne < 0.60


# ---------------------------------------------------------------- A3
def condition_a3(chute_s, chutes_aleatoires, chute_sac):
    return chute_s > float(np.quantile(chutes_aleatoires, 0.95)) and chute_s >= 0.5 * chute_sac


def verdict_a3(par_couche):
    """`par_couche` : liste (une entrée par couche lue) de dict {"chutes_sac": [5 découpes], "conditions": [5 bool],
    "moins_que_moitie": [5 bool]} : « conditions » est la condition de A3 par découpe, « moins_que_moitie » la condition
    « chute < moitié de celle du sac de jetons » par découpe. Une couche est sans objet si la chute moyenne du sac de jetons
    est < 0,02 ; un contraste est sans objet s'il compte moins de 2 couches jugeables.
    Rend « sans objet », « dépendance lue », « dépendance non lue », « indécise »."""
    jugeables = [c for c in par_couche if float(np.mean(c["chutes_sac"])) >= 0.02]
    if len(jugeables) < 2:
        return SANS_OBJET
    pos = sum(regle_couche(c["conditions"]) == POSITIVE for c in jugeables)
    if pos >= 2:
        return "dépendance lue"
    # « non lue » : toutes positives pour « chute < moitié de celle du sac de jetons » (contraire du second membre)
    if all(regle_couche(c["moins_que_moitie"]) == POSITIVE for c in jugeables):
        return "dépendance non lue"
    return "indécise"


# ---------------------------------------------------------------- S fait mieux que sans lentille
def s_fait_mieux(conditions_par_couche, classes_a):
    """`conditions_par_couche` : [couche][découpe] booléens « S strictement meilleur » ; `classes_a` : classes des couches pour A1
    (ou A2). Vrai s'il y a au moins 2 couches positives pour cette condition qui sont aussi positives pour A1 (ou A2)."""
    pos = [regle_couche(c) == POSITIVE for c in conditions_par_couche]
    return sum(p and a == POSITIVE for p, a in zip(pos, classes_a)) >= 2


def sans_lentille_au_moins_partout(conditions_par_couche):
    """« Sans lentille ≥ S » à chaque couche : chaque couche est négative pour « S strictement meilleur »."""
    return all(regle_couche(c) == NEGATIVE for c in conditions_par_couche)


# ---------------------------------------------------------------- verdict de A-i
def verdict_i(chaine_en_defaut, a1, sans_lentille_partout_a1, sans_lentille_partout_a2, a2_so, a3_par_contraste,
              s_mieux_a1, s_mieux_a2):
    """Critères de lecture gelés, volet A, mesure (i). `a3_par_contraste` : verdicts de A3 pour C1 et C2."""
    if chaine_en_defaut:
        return "chaîne en défaut"
    sans_lentille = sans_lentille_partout_a1 and (a2_so or sans_lentille_partout_a2)
    non_so = [v for v in a3_par_contraste if v != SANS_OBJET]
    a3_non_lue = bool(non_so) and all(v == "dépendance non lue" for v in non_so)
    if a1 == "non retrouvée" or sans_lentille or a3_non_lue:
        return "n'apporte rien"
    if a1 == "retrouvée" and (s_mieux_a1 or (s_mieux_a2 and not a2_so)):
        return "apporte quelque chose"
    return "indéterminé"


# ---------------------------------------------------------------- A-ii
def verdict_aii(couches, a_un_hors_distribution=True):
    """`couches` : liste par couche lue de dict :
    - "sonde_id" : AUROC en distribution de la sonde résiduelle (moyenne des découpes) ;
    - "sonde_ood" : AUROC hors distribution de la sonde (ignoré si pas de hors distribution) ;
    - "neurones_id"[k], "neurones_ood"[k] : AUROC des détecteurs à k neurones (k ∈ {1, 8, 64, 512}) ;
    - "borne_basse_ood"[k] : borne basse de l'intervalle à 95 % de l'écart hors distribution (neurones − sonde).
    Rend « sans objet », « n'apporte rien », « apporte », « indéterminé »."""
    jug = []
    for c in couches:
        id_so = c["sonde_id"] >= 0.99
        ood_so = (not a_un_hors_distribution) or c["sonde_ood"] >= 0.99
        if id_so and ood_so:
            continue
        jug.append((c, id_so))
    if len(jug) < 2:
        return SANS_OBJET
    ks = (1, 8, 64, 512)

    def perd(c, id_so, k):
        parts = []
        if not id_so:
            parts.append(c["sonde_id"] - c["neurones_id"][k] > 0.05)
        if a_un_hors_distribution:
            parts.append(c["sonde_ood"] - c["neurones_ood"][k] > 0.05)
        return all(parts)

    if all(perd(c, so, k) for c, so in jug for k in ks):
        return "n'apporte rien"
    for k in (1, 8, 64):
        ok = 0
        for c, id_so in jug:
            cond_id = id_so or c["neurones_id"][k] >= c["sonde_id"] - 0.02
            cond_ood = (not a_un_hors_distribution) or c["borne_basse_ood"][k] >= -0.05
            ok += cond_id and cond_ood
        if ok >= 2:
            return "apporte"
    return "indéterminé"


def qualificatif_texte(meilleur_k64, sac, contraste):
    """« au-delà du texte » si le meilleur détecteur à k ≤ 64 dépasse le sac de jetons d'au moins 0,02 (hors distribution pour C1,
    en distribution pour C3) ; sans objet sur C2."""
    if contraste == "C2":
        return SANS_OBJET
    return "au-delà du texte" if meilleur_k64 - sac >= 0.02 else "pas au-delà du texte"
