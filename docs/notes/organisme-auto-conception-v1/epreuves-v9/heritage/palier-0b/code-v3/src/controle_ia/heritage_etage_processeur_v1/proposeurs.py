"""B7 — les proposeurs écrits par programme (configurations communes aux deux couches ; conduite de la couche mécanique).

Recherche de base : avec la probabilité p_vraie (0,10, multipliée selon le proposeur), une loi vraie indépendante du monde en
cours tirée au hasard (au monde source : parmi les huit lois vraies) ; avec 0,10, une loi fausse plantée ; sinon une loi
appariée à rien : une loi neuve de la forme unique, sur un domaine tiré au hasard parmi les seize. Ce tirage lit la clé du
monde, par construction ; il ne passe jamais par le registre.

Lecteur réglé pour l'héritage : entrées **héritées** (écrites par la course de la source et reçues au départ ; origine
« course-source » de la provenance ; aucune dans une course source) dont `gardee` vaut oui (toutes au repli) ; paires de lois
distinctes (identifiées par leur texte dans l'engagement scellé) ; K paires examinées par génération, sans remise, dans l'ordre
d'une permutation semée ; deux sens de composition ; criblage sans frais sur la part servie (statistique du test de mort ≥ 0,02) ;
au plus la moitié des tentatives (entier inférieur), avant la recherche de base ; domaine du meilleur ajustement, le plus petit
rang en cas d'égalité ; s'il en passe trop, celles qui sont engagées sont prises dans l'ordre d'une permutation semée.

Lecteur réglé pour la tenue : multiplicateur (1 + τ) quand le registre **servi** contient au moins une entrée **de sa propre
continuation** (même source, même bras) dont `gardee` vaut oui. Au bras 4b, le registre servi est celui d'une autre source :
aucune de ses entrées n'est de la continuation, et le multiplicateur ne s'y applique pas (défaut du dossier versé, corrigé).
"""

import json
import math

import numpy as np

from .comparateur import loi_du_texte
from .constantes import ENTREES_DE_SATURATION, P_FAUSSE_BASE, P_VRAIE_BASE, SEUIL_VALEUR, STATUTS_RESULTAT, NON_EPROUVEE
from .lois import composer, json_canonique, loi_par_sous_population, matrice, softmax_aleatoire
from .constantes import PLANCHER, NOMBRE_ISSUES

NOMS = ("sourd-egal", "sourd-paie", "lecteur-heritage", "lecteur-tenue", "lecteur-deux", "suiveur", "suiveur-lettre",
        "generaliste", "copieur")


class ProposeurRefuse(ValueError):
    pass


def configuration(nom, K=0.0, tau=0.0, phi=0.0, gamma=0.0):
    if nom not in NOMS:
        raise ProposeurRefuse(f"proposeur inconnu : {nom!r}")
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
    if np.any(p > 1.0 - P_FAUSSE_BASE + 1e-12):
        raise ProposeurRefuse("probabilité de la recherche de base au-delà de 0,9 : réglage hors du banc")
    return p


def part_generaliste(prop, n_avec_classe):
    return prop["gamma"] * np.minimum(1.0, np.asarray(n_avec_classe, dtype=float) / ENTREES_DE_SATURATION)


def k_entier(K, rng):
    b = math.floor(K)
    return int(b + (rng.random() < K - b))


def est_heritee(e):
    return e["provenance"]["origine"] == "course-source"


def est_de_la_continuation(e, source, bras):
    p = e["provenance"]
    return p["origine"] == ("course-source" if bras == "source" else "continuation") and p["source"] == f"source-{source}" \
        and p["bras"] == f"bras-{bras}"


def propre_gardee(vue, source, bras):
    """Le registre servi contient-il une entrée de sa propre continuation dont `gardee` vaut oui ?"""
    return bool(vue) and any(e.get("gardee") is True and est_de_la_continuation(e, source, bras) for e in vue)


def entrees_avec_classe(vue):
    """Le généraliste lit combien d'entrées servies portent une classe d'issue (le statut de budget n'en est pas une)."""
    if not vue:
        return 0
    return sum(1 for e in vue if "resultat" in e and e["resultat"]["classe"] in STATUTS_RESULTAT
               and e["resultat"]["classe"] != NON_EPROUVEE)


# --- criblage sur la part servie --------------------------------------------------------------------------------------------


class PartsServies:
    """Les parts servies des seize domaines d'un monde, réunies pour un calcul vectorisé de la statistique du test de mort."""

    def __init__(self, parts):
        self.noms = sorted(parts)
        self.Z = np.concatenate([parts[n]["Z"] for n in self.noms])
        self.G = np.concatenate([parts[n]["G"] for n in self.noms])
        self.y = np.concatenate([parts[n]["y"] for n in self.noms]).astype(np.int64)
        self.d = np.concatenate([np.full(len(parts[n]["y"]), k) for k, n in enumerate(self.noms)])
        self.taille = np.bincount(self.d, minlength=len(self.noms)).astype(float)
        comptes = np.full((len(self.noms), NOMBRE_ISSUES), 0.5)
        np.add.at(comptes, (self.d, self.y), 1.0)
        self.log_marg = np.log(comptes / comptes.sum(axis=1)[:, None])

    def statistiques(self, loi):
        P = matrice(loi, self.Z, self.G)
        g = np.log(np.maximum(P[np.arange(len(self.y)), self.y], PLANCHER)) - self.log_marg[self.d, self.y]
        return np.bincount(self.d, weights=g, minlength=len(self.noms)) / self.taille

    def meilleur(self, loi, seuil=SEUIL_VALEUR):
        """(domaine où la loi passe le criblage et s'ajuste le mieux, le plus petit rang en cas d'égalité ; ou None), et le domaine
        du meilleur ajustement sans seuil."""
        s = self.statistiques(loi)
        k = int(np.argmax(s))  # premier maximum : le plus petit rang
        return (self.noms[k] if s[k] >= seuil else None), self.noms[k]


def lois_distinctes(entrees):
    textes = []
    for e in entrees:
        loi = loi_du_texte(e["tentative"]["engagement"]["test_de_mort"]["test"])
        if loi is not None:
            textes.append(json_canonique(loi))
    return sorted(set(textes))


def tentatives_du_lecteur(prop, vue, monde, parts, n_tentatives, rng, repli, mesure):
    """Compositions engagées par le lecteur réglé pour l'héritage (avant la recherche de base). `mesure` reçoit, par composition
    examinée sur ce monde, (texte, est une loi dépendante du monde, passe et retenue sur son propre domaine, passe)."""
    if not prop["K"] or not vue:
        return []
    heritees = [e for e in vue if est_heritee(e) and (repli or e.get("gardee") is True)]
    textes = lois_distinctes(heritees)
    paires = [(i, j) for i in range(len(textes)) for j in range(i + 1, len(textes))]
    k = k_entier(prop["K"], rng)  # un tirage par génération, même sans paire
    if not paires:
        return []
    ordre = rng.permutation(len(paires))[:min(k, len(paires))]
    dependantes = {l["texte"]: l["domaine"] for l in monde.lois.values() if l["dependante"]}
    passees = []
    for idx in ordre:
        i, j = paires[idx]
        a, b = json.loads(textes[i]), json.loads(textes[j])
        for c in (composer(a, b), composer(b, a)):
            dom, _ = parts.meilleur(c)
            t = json_canonique(c)
            vraie = t in dependantes
            mesure.append((t, vraie, bool(vraie and dom == dependantes[t]), dom is not None))
            if dom is not None:
                passees.append((dom, c))
    plafond = n_tentatives // 2
    if len(passees) > plafond:
        choix = rng.permutation(len(passees))[:plafond]
        passees = [passees[c] for c in sorted(choix)]
    return passees


def recherche_de_base(prop, monde, n, n_servi, propre, n_avec_classe, rng):
    """`n` tentatives de la recherche de base : liste de (domaine, loi)."""
    independantes = sorted(i for i, l in monde.lois.items() if l["type"] == "vraie" and not l["dependante"])
    fausses = monde.fausses()
    pv = float(p_vraie(prop, [n_servi], [propre])[0])
    g = float(part_generaliste(prop, [n_avec_classe])[0])
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
            out.append((noms[rng.integers(len(noms))], loi_par_sous_population(softmax_aleatoire(rng), softmax_aleatoire(rng))))
            continue
        out.append((monde.lois[i]["domaine"], monde.lois[i]["loi"]))
    return out


def copies(vue, parts, n, rng):
    out = []
    for _ in range(n):
        e = vue[rng.integers(len(vue))]
        loi = loi_du_texte(e["tentative"]["engagement"]["test_de_mort"]["test"])
        _, dom = parts.meilleur(loi)
        out.append((dom, loi))
    return out


def proposer(prop, vue, monde, parts, n_tentatives, rng, source, bras, repli=False, mesure=None):
    """Toutes les tentatives d'une génération : liste de (domaine, loi, origine), dans l'ordre du scellement ; origine ∈
    {« composition », « copie », « base »} (pour les fréquences de la couche mécanique ; jamais servie). `parts` : PartsServies
    du monde en cours ; `source`, `bras` : la continuation (`bras` = « source » dans la course source)."""
    mesure = [] if mesure is None else mesure
    n_servi = len(vue) if vue else 0
    if prop["copieur"] and n_servi:
        return [(d, l, "copie") for d, l in copies(vue, parts, n_tentatives, rng)]
    # B6 (version 4) : une course source n'a aucune entrée héritée ; le lecteur n'y compose rien
    compo = [] if bras == "source" else tentatives_du_lecteur(prop, vue, monde, parts, n_tentatives, rng, repli, mesure)
    propre = propre_gardee(vue, source, bras)
    base = recherche_de_base(prop, monde, n_tentatives - len(compo), n_servi, propre, entrees_avec_classe(vue), rng)
    return [(d, l, "composition") for d, l in compo] + [(d, l, "base") for d, l in base]
