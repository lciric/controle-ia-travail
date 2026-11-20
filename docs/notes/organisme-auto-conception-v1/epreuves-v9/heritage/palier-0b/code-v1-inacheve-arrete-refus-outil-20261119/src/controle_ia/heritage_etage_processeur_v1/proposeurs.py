"""B7 — les proposeurs écrits par programme (configurations communes aux deux couches ; conduite de la couche mécanique).

Recherche de base : avec la probabilité p_vraie (0,10, multipliée selon le proposeur), une loi vraie indépendante du monde en
cours tirée au hasard ; avec 0,10, une loi fausse plantée ; sinon une loi appariée à rien (une loi aléatoire neuve, sur un
domaine tiré au hasard). Ce tirage lit la clé du monde, par construction ; il ne passe jamais par le registre.

SILENCES comblés (rapport) : une paire examinée par le lecteur est criblée dans ses deux sens de composition ; le criblage est
la statistique du test de mort (gain moyen de log-score, seuil 0,02) calculée sur la part servie ; « la moitié de ses
tentatives » est l'entier inférieur ; un K non entier est arrondi par un tirage par génération ; au monde source, toute loi
vraie est « indépendante » pour la recherche de base ; la description bornée est un texte fixe.
"""

import math

import numpy as np

from .constantes import ENTREES_DE_SATURATION, P_FAUSSE_BASE, P_VRAIE_BASE, SEUIL_VALEUR
from .executeur import statistique_moyenne
from .lois import composer, json_canonique, loi_aleatoire
from .comparateur import loi_du_texte

DESCRIPTION_FIXE = "Tentative écrite par programme : la loi gelée L décrit l'issue du domaine nommé."

NOMS = ("sourd-egal", "sourd-paie", "lecteur-heritage", "lecteur-tenue", "lecteur-deux", "suiveur", "suiveur-lettre",
        "generaliste", "copieur")


def configuration(nom, K=0.0, tau=0.0, phi=0.0, gamma=0.0):
    if nom not in NOMS:
        raise ValueError(f"proposeur inconnu : {nom!r}")
    return {"nom": nom, "paie": nom != "sourd-egal", "K": float(K) if nom in ("lecteur-heritage", "lecteur-deux") else 0.0,
            "tau": float(tau) if nom in ("lecteur-tenue", "lecteur-deux") else 0.0,
            "phi": float(phi) if nom in ("suiveur", "suiveur-lettre") else 0.0,
            "lettre": nom == "suiveur-lettre", "gamma": float(gamma) if nom == "generaliste" else 0.0,
            "copieur": nom == "copieur"}


def p_vraie(prop, n_servi, propre_gardee):
    """Probabilité de trouver une loi vraie indépendante, à la recherche de base (vectorisée sur les sources)."""
    n_servi = np.asarray(n_servi, dtype=float)
    p = np.full(n_servi.shape, P_VRAIE_BASE)
    if prop["tau"]:
        p = np.where(np.asarray(propre_gardee, dtype=bool), p * (1 + prop["tau"]), p)
    if prop["phi"] and not prop["lettre"]:
        p = p * (1 + prop["phi"] * np.minimum(1.0, n_servi / ENTREES_DE_SATURATION))
    if prop["lettre"]:
        p = np.where(n_servi > 0, p * (1 + prop["phi"]), p)
    return np.minimum(p, 1.0 - P_FAUSSE_BASE)


def part_generaliste(prop, n_avec_classe):
    return prop["gamma"] * np.minimum(1.0, np.asarray(n_avec_classe, dtype=float) / ENTREES_DE_SATURATION)


def k_entier(K, rng):
    b = math.floor(K)
    return int(b + (rng.random() < K - b))


# --- conduite de la couche mécanique -----------------------------------------------------------------------------------------


def _lois_distinctes(entrees):
    textes = []
    for e in entrees:
        loi = loi_du_texte(e["tentative"]["engagement"]["test_de_mort"]["test"])
        if loi is not None:
            textes.append(json_canonique(loi))
    return sorted(set(textes))


def cribler(loi, monde, parts_servies):
    """Domaines où la composition passe le criblage sur la part servie ; rend (domaine retenu ou None, statistiques)."""
    stats = {nom: statistique_moyenne(loi, p["Z"], p["G"], p["y"]) for nom, p in parts_servies.items()}
    passe = [(-v, nom) for nom, v in stats.items() if v >= SEUIL_VALEUR]
    return (min(passe)[1] if passe else None), stats


def tentatives_du_lecteur(prop, vue, monde, parts_servies, n_tentatives, rng, repli, mesure):
    """Compositions engagées par le lecteur réglé pour l'héritage (avant la recherche de base). `mesure` reçoit, par composition
    examinée sur ce monde, (texte, est une loi dépendante du monde, passe et retenue sur son propre domaine)."""
    if not prop["K"] or not vue:
        return []
    de_la_source = [e for e in vue if e["provenance"]["origine"] == "course-source" and (repli or e.get("gardee"))]
    textes = _lois_distinctes(de_la_source)
    paires = [(i, j) for i in range(len(textes)) for j in range(i + 1, len(textes))]
    if not paires:
        return []
    k = min(k_entier(prop["K"], rng), len(paires))
    ordre = rng.permutation(len(paires))[:k]
    dependantes = {json_canonique(l["loi"]): (i, l["domaine"]) for i, l in monde.lois.items() if l["dependante"]}
    passees = []
    import json
    for idx in ordre:
        i, j = paires[idx]
        a, b = json.loads(textes[i]), json.loads(textes[j])
        for c in (composer(a, b), composer(b, a)):
            dom, _ = cribler(c, monde, parts_servies)
            t = json_canonique(c)
            vraie = t in dependantes
            mesure.append((t, vraie, bool(vraie and dom == dependantes[t][1]), dom is not None))
            if dom is not None:
                passees.append((dom, c))
    plafond = n_tentatives // 2
    if len(passees) > plafond:
        choix = rng.permutation(len(passees))[:plafond]
        passees = [passees[c] for c in sorted(choix)]
    return passees


def recherche_de_base(prop, monde, n, n_servi, propre_gardee, rng, n_avec_classe=None):
    """`n` tentatives de la recherche de base : liste de (domaine, loi)."""
    independantes = [i for i, l in sorted(monde.lois.items()) if l["type"] == "vraie" and not l["dependante"]]
    fausses = sorted(monde.fausses())
    pv = float(p_vraie(prop, [n_servi], [propre_gardee])[0])
    g = float(part_generaliste(prop, [n_servi if n_avec_classe is None else n_avec_classe])[0])
    noms = [d["nom"] for d in monde.domaines]
    out = []
    for _ in range(n):
        u = rng.random()
        if u < pv:
            i = independantes[rng.integers(len(independantes))]
        elif u < pv + P_FAUSSE_BASE:
            i = fausses[rng.integers(len(fausses))]
        elif g and rng.random() < g:
            i = independantes[rng.integers(len(independantes))] if rng.random() < 0.5 else fausses[rng.integers(len(fausses))]
        else:
            out.append((noms[rng.integers(len(noms))], loi_aleatoire(rng)))
            continue
        out.append((monde.lois[i]["domaine"], monde.lois[i]["loi"]))
    return out


def copies(vue, monde, parts_servies, n, rng):
    out = []
    for _ in range(n):
        e = vue[rng.integers(len(vue))]
        loi = loi_du_texte(e["tentative"]["engagement"]["test_de_mort"]["test"])
        _, stats = cribler(loi, monde, parts_servies)
        dom = min((-v, nom) for nom, v in stats.items())[1]
        out.append((dom, loi))
    return out


def proposer(prop, vue, monde, parts_servies, n_tentatives, rng, repli=False, propre_gardee=False, mesure=None,
             en_continuation=True):
    """Toutes les tentatives d'une génération : liste de (domaine, loi, origine), dans l'ordre du scellement ; origine ∈
    {« composition », « copie », « base »} (pour les fréquences de la couche mécanique, jamais servie)."""
    mesure = [] if mesure is None else mesure
    n_servi = len(vue) if vue else 0
    if prop["copieur"] and n_servi:
        return [(d, l, "copie") for d, l in copies(vue, monde, parts_servies, n_tentatives, rng)]
    # SILENCE : dans la course source, aucune entrée n'est « venue de la source » pour le lecteur (il est la source)
    compo = tentatives_du_lecteur(prop, vue, monde, parts_servies, n_tentatives, rng, repli, mesure) if en_continuation else []
    base = recherche_de_base(prop, monde, n_tentatives - len(compo), n_servi, propre_gardee, rng,
                             n_avec_classe=0 if repli else None)
    return [(d, l, "composition") for d, l in compo] + [(d, l, "base") for d, l in base]
