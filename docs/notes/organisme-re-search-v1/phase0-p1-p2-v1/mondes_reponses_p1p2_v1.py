"""Mondes plantés, grammaire fermée des lois, sondes, prédicats et répondeurs — phase 0 de P1 et P2, v1 (modèle I).

Fichier neuf (R12). Rien du dépôt de l'organisme n'est modifié : la sémantique des lois est celle de
`orchestrator/pole/evaluateur_lois_v62.py` (six types du gabarit fermé des proposeurs : fixe, softmax,
par_sous_population, melange, si_sinon, transformee ; instance {z: [z0, z1], g: 0 ou 1} ; trois issues ; plancher 1e-12
puis renormalisation à chaque nœud). `proba_vec` en est une réécriture vectorisée (numpy) sur un tableau d'instances ;
l'essai `test_proba_vec_egale_evaluateur_v62` la compare, à 1e-12 près, à l'évaluateur de l'organisme chargé en lecture
seule par `runpy`.

La « forme » d'une loi est celle de l'analyse de nos journaux (`analyse_journaux_re_search_v1.py`, fonctions `forme`,
`canon`, `cle_forme`, recopiées ici sous un nom neuf) : arbre JSON où chaque feuille numérique (réel, entier) est
remplacée par un jeton unique ; types, noms de clés et longueurs de listes gardés. Variante de sensibilité (constat A-3
de la contre-lecture) : feuilles entières gardées (`cle_forme_entiers`).

Aucun appel réseau, aucun appel de modèle. Graines : `numpy.random.SeedSequence(20261118)`, une graine fille par tâche
(`graine_de_tache`, clé de dérivation = 8 premiers octets du sha256 du nom de la tâche, comme `controle_ia.manifeste`).
"""
from __future__ import annotations

import hashlib
import json
import math

import numpy as np

VERSION = "mondes-reponses-p1p2-v1"
RACINE_GRAINES = 20261118
PLANCHER = 1e-12
NOMBRE_ISSUES = 3
DIMENSION = 2
TYPES_FEUILLES = ("fixe", "softmax")
TYPES_COMPOSES = ("melange", "si_sinon", "par_sous_population", "transformee")
TYPES = TYPES_FEUILLES + TYPES_COMPOSES
PROFONDEUR_MAX = 2  # racine à 0 ; à la profondeur 2, seules les feuilles (fixe, softmax)
OPERATIONS_TRANSFORMEE = ("melange_aveugle", "puissance", "inclinaison", "oscillation")


class Refus(Exception):
    """Refus écrit (aucun repli silencieux)."""


# --- graines (R9) -----------------------------------------------------------------------------------------------------
def cle_de_tache(tache: str) -> int:
    return int.from_bytes(hashlib.sha256(tache.encode("utf-8")).digest()[:8], "big")


def graine_de_tache(tache: str, racine: int = RACINE_GRAINES) -> np.random.SeedSequence:
    return np.random.SeedSequence(racine, spawn_key=(cle_de_tache(tache),))


def generateur(tache: str, racine: int = RACINE_GRAINES) -> np.random.Generator:
    return np.random.default_rng(graine_de_tache(tache, racine))


# --- formes (copie nommée de l'analyse de nos journaux) ---------------------------------------------------------------
def forme(o):
    if isinstance(o, bool) or o is None or isinstance(o, str):
        return o
    if isinstance(o, (int, float)):
        return "#"
    if isinstance(o, list):
        return [forme(x) for x in o]
    if isinstance(o, dict):
        return {k: forme(v) for k, v in o.items()}
    raise Refus(f"feuille inattendue dans une loi : {type(o).__name__}")


def forme_entiers(o):
    """Variante A-3 : les feuilles entières (indices de trait, issue, sous-population) sont gardées."""
    if isinstance(o, bool) or o is None or isinstance(o, str):
        return o
    if isinstance(o, int):
        return o
    if isinstance(o, float):
        return "#"
    if isinstance(o, list):
        return [forme_entiers(x) for x in o]
    if isinstance(o, dict):
        return {k: forme_entiers(v) for k, v in o.items()}
    raise Refus(f"feuille inattendue dans une loi : {type(o).__name__}")


def canon(o) -> str:
    return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def cle_forme(loi) -> str:
    return canon(forme(loi))


def cle_forme_entiers(loi) -> str:
    return canon(forme_entiers(loi))


# --- grammaire fermée : tirage d'une loi --------------------------------------------------------------------------------
def _dirichlet(rng, k):
    return [float(x) for x in rng.dirichlet(np.ones(k))]


def tirer_loi(rng: np.random.Generator, profondeur: int = 0, types_racine=None, poids_racine=None) -> dict:
    """Une loi de la grammaire fermée (loi de tirage R1 du préenregistrement).

    Type : uniforme sur les six types, sauf à la profondeur PROFONDEUR_MAX (uniforme sur fixe, softmax). À la racine
    seulement, `types_racine` (et `poids_racine`, probabilités) remplacent la loi des types (variantes R2 et hors softmax).
    Paramètres : fixe, probas ~ Dirichlet(1,1,1) ; softmax, poids 3×2 ~ N(0, 1,5²), biais ~ N(0, 1) ; melange, m uniforme
    sur {2, 3}, poids ~ Dirichlet(1^m) ; si_sinon, condition sur un trait (indice uniforme sur {0, 1}, seuil ~ N(0, 0,5²))
    ou sur la sous-population (uniforme sur {0, 1}), chacune avec probabilité 1/2 ; par_sous_population, lois « 0 » et
    « 1 », sans défaut ; transformee, sous-ensemble non vide des quatre opérations, uniforme sur les 15, avec
    melange_aveugle (lambda ~ U(0,05 ; 0,5), probas ~ Dirichlet), puissance ~ U(0,5 ; 2), inclinaison ~ N(0, 1)³,
    oscillation (amplitude ~ U(0,2 ; 1,5), fréquence ~ U(0,5 ; 3), trait uniforme, phase ~ U(0 ; 2π), issue uniforme).
    """
    if profondeur == 0 and types_racine is not None:
        types = tuple(types_racine)
        p = None if poids_racine is None else np.asarray(poids_racine, dtype=float)
        genre = types[int(rng.choice(len(types), p=p))]
    elif profondeur >= PROFONDEUR_MAX:
        genre = TYPES_FEUILLES[int(rng.integers(len(TYPES_FEUILLES)))]
    else:
        genre = TYPES[int(rng.integers(len(TYPES)))]
    if genre not in TYPES:
        raise Refus(f"type hors grammaire : {genre!r}")
    if profondeur >= PROFONDEUR_MAX and genre not in TYPES_FEUILLES:
        raise Refus("type composé demandé à la profondeur maximale")
    if genre == "fixe":
        return {"type": "fixe", "probas": _dirichlet(rng, NOMBRE_ISSUES)}
    if genre == "softmax":
        return {"type": "softmax",
                "poids": [[float(x) for x in rng.normal(0.0, 1.5, DIMENSION)] for _ in range(NOMBRE_ISSUES)],
                "biais": [float(x) for x in rng.normal(0.0, 1.0, NOMBRE_ISSUES)]}
    if genre == "melange":
        m = int(rng.integers(2, 4))
        return {"type": "melange", "poids": _dirichlet(rng, m),
                "composantes": [tirer_loi(rng, profondeur + 1) for _ in range(m)]}
    if genre == "si_sinon":
        if rng.random() < 0.5:
            condition = {"indice": int(rng.integers(DIMENSION)), "seuil": float(rng.normal(0.0, 0.5))}
        else:
            condition = {"sous_population": int(rng.integers(2))}
        return {"type": "si_sinon", "condition": condition,
                "si": tirer_loi(rng, profondeur + 1), "sinon": tirer_loi(rng, profondeur + 1)}
    if genre == "par_sous_population":
        return {"type": "par_sous_population", "lois": {"0": tirer_loi(rng, profondeur + 1), "1": tirer_loi(rng, profondeur + 1)}}
    # transformee
    masque = int(rng.integers(1, 16))  # sous-ensemble non vide, uniforme sur les 15
    loi = {"type": "transformee", "base": tirer_loi(rng, profondeur + 1)}
    if masque & 1:
        loi["melange_aveugle"] = {"lambda": float(rng.uniform(0.05, 0.5)), "probas": _dirichlet(rng, NOMBRE_ISSUES)}
    if masque & 2:
        loi["puissance"] = float(rng.uniform(0.5, 2.0))
    if masque & 4:
        loi["inclinaison"] = [float(x) for x in rng.normal(0.0, 1.0, NOMBRE_ISSUES)]
    if masque & 8:
        loi["oscillation"] = {"amplitude": float(rng.uniform(0.2, 1.5)), "frequence": float(rng.uniform(0.5, 3.0)),
                              "trait": int(rng.integers(DIMENSION)), "phase": float(rng.uniform(0.0, 2 * math.pi)),
                              "issue": int(rng.integers(NOMBRE_ISSUES))}
    return loi


# --- évaluation vectorisée (sémantique de evaluateur_lois_v62) ---------------------------------------------------------
def _normaliser(p):
    p = np.maximum(PLANCHER, p)
    return p / p.sum(axis=1, keepdims=True)


def proba_vec(loi: dict, Z: np.ndarray, G: np.ndarray) -> np.ndarray:
    """Probabilités (N × 3) de la loi sur N instances (Z : N × 2 réels, G : N entiers 0 ou 1)."""
    genre = loi.get("type") if isinstance(loi, dict) else None
    n = Z.shape[0]
    if genre == "fixe":
        return _normaliser(np.tile(np.asarray(loi["probas"], dtype=float), (n, 1)))
    if genre == "softmax":
        W = np.asarray(loi["poids"], dtype=float)
        b = np.asarray(loi["biais"], dtype=float)
        s = b[None, :] + Z @ W.T
        s = s - s.max(axis=1, keepdims=True)
        return _normaliser(np.exp(s))
    if genre == "par_sous_population":
        sortie = np.empty((n, NOMBRE_ISSUES))
        for gval in np.unique(G):
            masque = G == gval
            sous = loi["lois"].get(str(int(gval)), loi.get("defaut"))
            if sous is None:
                raise Refus(f"par_sous_population sans loi pour g={int(gval)} ni défaut")
            sortie[masque] = proba_vec(sous, Z[masque], G[masque])
        return sortie
    if genre == "melange":
        mix = np.zeros((n, NOMBRE_ISSUES))
        for poids, composante in zip(loi["poids"], loi["composantes"]):
            mix += float(poids) * proba_vec(composante, Z, G)
        return _normaliser(mix)
    if genre == "si_sinon":
        c = loi["condition"]
        if "sous_population" in c:
            masque = G == c["sous_population"]
        else:
            masque = Z[:, c["indice"]] > c.get("seuil", 0.0)
        return np.where(masque[:, None], proba_vec(loi["si"], Z, G), proba_vec(loi["sinon"], Z, G))
    if genre == "transformee":
        p = proba_vec(loi["base"], Z, G)
        if loi.get("melange_aveugle"):
            lam = loi["melange_aveugle"]["lambda"]
            bb = np.asarray(loi["melange_aveugle"]["probas"], dtype=float)
            bb = np.maximum(PLANCHER, bb)
            bb = bb / bb.sum()
            p = (1 - lam) * p + lam * bb[None, :]
        if loi.get("puissance") is not None:
            p = _normaliser(np.maximum(p, PLANCHER) ** loi["puissance"])
        if loi.get("inclinaison"):
            p = _normaliser(p * np.exp(np.asarray(loi["inclinaison"], dtype=float))[None, :])
        if loi.get("oscillation"):
            o = loi["oscillation"]
            facteur = np.exp(o["amplitude"] * np.cos(o["frequence"] * Z[:, o["trait"]] + o.get("phase", 0.0)))
            p = p.copy()
            p[:, o["issue"]] = p[:, o["issue"]] * facteur
            p = _normaliser(p)
        return _normaliser(p)
    raise Refus("type de loi hors du gabarit : " + repr(genre))


# --- sondes -------------------------------------------------------------------------------------------------------------
def tirer_sonde(rng: np.random.Generator, n: int):
    """n instances : z ~ N(0, 1)², g ~ Bernoulli(1/2)."""
    Z = rng.normal(0.0, 1.0, (n, DIMENSION))
    G = rng.integers(0, 2, n)
    return Z, G


# --- divergences --------------------------------------------------------------------------------------------------------
def matrice_kl(P: np.ndarray) -> np.ndarray:
    """KL[h, c] = moyenne sur la sonde de KL(loi h ‖ loi c) (nat), pour P de forme (C × N × 3)."""
    C, N, K = P.shape
    L = np.log(P)
    plat_p = P.reshape(C, N * K)
    plat_l = L.reshape(C, N * K)
    entropie_neg = (plat_p * plat_l).sum(axis=1) / N
    croisee = plat_p @ plat_l.T / N
    kl = np.maximum(entropie_neg[:, None] - croisee, 0.0)
    np.fill_diagonal(kl, 0.0)  # KL(h ‖ h) = 0 par définition (l'arrondi de la soustraction laisserait ~1e-15)
    return kl


def kl_moyenne(p_monde: np.ndarray, p_carte: np.ndarray) -> float:
    return float(np.mean(np.sum(p_monde * (np.log(p_monde) - np.log(p_carte)), axis=1)))


# --- prédicats fermés (P1) ----------------------------------------------------------------------------------------------
SEUILS_TRAIT = (-1.0, -0.5, 0.0, 0.5, 1.0)
SEUILS_MARGINALE = (0.2, 1.0 / 3.0, 0.5)


def grammaire_predicats(variante: str = "empirique"):
    """Liste fermée des prédicats (dictionnaires), écrite avant tout monde.

    empirique (principale, 42 prédicats) : pour chaque trait j ∈ {0, 1}, issue a et seuil s ∈ SEUILS_TRAIT,
    « P(a | z_j > s) > P(a | z_j ≤ s) » (30) ; pour chaque issue, « P(a | g = 1) > P(a | g = 0) » (3) ; pour chaque issue
    et c ∈ SEUILS_MARGINALE, « P(a) > c » (9). Probabilités moyennées sur la sonde des questions.
    structurelle (rapportée à part, 51) : les 42 empiriques, plus « la racine est de type t » (6), « la loi dépend de
    z0 », « de z1 », « de g » (3 ; dépendance = un écart > 1e-9 sur la sonde quand le trait est décalé de +1 ou g inversé).
    Chaque prédicat porte une « direction » (z0, z1, g, marginale, racine) pour les questionneurs répéteur et disperseur.
    """
    preds = []
    for j in range(DIMENSION):
        for a in range(NOMBRE_ISSUES):
            for s in SEUILS_TRAIT:
                preds.append({"genre": "trait", "trait": j, "issue": a, "seuil": s, "direction": f"z{j}"})
    for a in range(NOMBRE_ISSUES):
        preds.append({"genre": "sous_population", "issue": a, "direction": "g"})
    for a in range(NOMBRE_ISSUES):
        for c in SEUILS_MARGINALE:
            preds.append({"genre": "marginale", "issue": a, "seuil": c, "direction": "marginale"})
    if variante == "empirique":
        return preds
    if variante != "structurelle":
        raise Refus(f"variante de prédicats inconnue : {variante!r}")
    for t in TYPES:
        preds.append({"genre": "racine", "type": t, "direction": "racine"})
    for j in range(DIMENSION):
        preds.append({"genre": "depend_trait", "trait": j, "direction": f"z{j}"})
    preds.append({"genre": "depend_g", "direction": "g"})
    return preds


def reponses_predicats(loi: dict, P_q: np.ndarray, Z: np.ndarray, G: np.ndarray, preds) -> np.ndarray:
    """Vecteur booléen des réponses vraies de la loi aux prédicats (calculées par le code, la vérité par construction).
    P_q : probabilités de la loi sur la sonde des questions (N × 3)."""
    sortie = np.zeros(len(preds), dtype=bool)
    cache_dep = {}
    for i, q in enumerate(preds):
        genre = q["genre"]
        if genre == "trait":
            haut = Z[:, q["trait"]] > q["seuil"]
            if haut.all() or (~haut).all():
                raise Refus("sonde des questions dégénérée pour un seuil")
            sortie[i] = P_q[haut, q["issue"]].mean() > P_q[~haut, q["issue"]].mean()
        elif genre == "sous_population":
            un = G == 1
            sortie[i] = P_q[un, q["issue"]].mean() > P_q[~un, q["issue"]].mean()
        elif genre == "marginale":
            sortie[i] = P_q[:, q["issue"]].mean() > q["seuil"]
        elif genre == "racine":
            sortie[i] = loi["type"] == q["type"]
        elif genre == "depend_trait":
            j = q["trait"]
            if ("z", j) not in cache_dep:
                Z2 = Z.copy()
                Z2[:, j] += 1.0
                cache_dep[("z", j)] = bool(np.max(np.abs(proba_vec(loi, Z2, G) - P_q)) > 1e-9)
            sortie[i] = cache_dep[("z", j)]
        elif genre == "depend_g":
            if "g" not in cache_dep:
                cache_dep["g"] = bool(np.max(np.abs(proba_vec(loi, Z, 1 - G) - P_q)) > 1e-9)
            sortie[i] = cache_dep["g"]
        else:
            raise Refus(f"prédicat hors grammaire : {q!r}")
    return sortie


# --- répondeurs ---------------------------------------------------------------------------------------------------------
class Repondeur:
    """Le monde répond, par le code, Oui ou Non. `vraies` : réponses vraies de la loi du monde (vecteur booléen).

    mode « exact » : la vérité ; « inverse » : chaque réponse inversée avec probabilité `taux` (artefact R5) ;
    « hasard » : Oui ou Non à pile ou face, sans regarder la loi (artefact R5). Une question hors de la grammaire est
    refusée et comptée, jamais répondue « Inconnu ». La réponse est toujours un booléen Python, rien d'autre.
    """

    def __init__(self, vraies: np.ndarray, mode: str = "exact", taux: float = 0.0, rng=None):
        if mode not in ("exact", "inverse", "hasard"):
            raise Refus(f"mode de répondeur inconnu : {mode!r}")
        if mode != "exact" and rng is None:
            raise Refus("répondeur bruité sans générateur")
        self.vraies = np.asarray(vraies, dtype=bool)
        self.mode, self.taux, self.rng = mode, taux, rng
        self.refus_hors_grammaire = 0

    def repondre(self, indice) -> bool:
        if isinstance(indice, bool) or not isinstance(indice, (int, np.integer)) or not 0 <= int(indice) < len(self.vraies):
            self.refus_hors_grammaire += 1
            raise Refus(f"question hors grammaire : {indice!r}")
        v = bool(self.vraies[int(indice)])
        if self.mode == "inverse" and self.rng.random() < self.taux:
            v = not v
        elif self.mode == "hasard":
            v = bool(self.rng.random() < 0.5)
        return v


def exiger_booleen(reponse) -> bool:
    """Garde : une réponse qui n'est pas exactement un booléen (fuite d'information, « Inconnu ») est refusée."""
    if not isinstance(reponse, (bool, np.bool_)):
        raise Refus(f"réponse qui n'est pas Oui ou Non : {type(reponse).__name__}")
    return bool(reponse)


# --- disjonction des mondes (signature prédictive) ----------------------------------------------------------------------
SEUIL_SIGNATURE_NAT = 0.30  # comme la mémoire de l'organisme (memoire.py, constante l. 34) : même hypothèse si ≤ 0,30 nat


def disjointe(p_candidate: np.ndarray, p_references) -> bool:
    """Vrai si la loi candidate est à plus de 0,30 nat (KL moyenne, dans les deux sens) de chaque loi de référence."""
    for p_ref in p_references:
        if kl_moyenne(p_ref, p_candidate) <= SEUIL_SIGNATURE_NAT or kl_moyenne(p_candidate, p_ref) <= SEUIL_SIGNATURE_NAT:
            return False
    return True


# --- carte écrite par un proposeur (phase 1 ; règle fixée d'avance, conditions de la mère R-3186, P1 c) -----------------
CARTE_DE_REMPLACEMENT = {"type": "fixe", "probas": [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]}


def _nombre(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(float(x))


def _vecteur(x, n):
    return isinstance(x, list) and len(x) == n and all(_nombre(v) for v in x)


def valider_loi(loi, profondeur: int = 0) -> None:
    """Refus écrit si la loi n'est pas dans la grammaire fermée des six types (clés, longueurs, nombres finis,
    profondeur au plus PROFONDEUR_MAX). Rend None si la loi est conforme."""
    if not isinstance(loi, dict) or loi.get("type") not in TYPES:
        raise Refus(f"carte hors grammaire (type) : {loi!r:.80}")
    if profondeur > PROFONDEUR_MAX:
        raise Refus("carte hors grammaire : trop profonde")
    genre = loi["type"]
    if genre == "fixe":
        if not (_vecteur(loi.get("probas"), NOMBRE_ISSUES) and all(v >= 0 for v in loi["probas"]) and sum(loi["probas"]) > 0):
            raise Refus("carte hors grammaire : fixe sans probas valides")
    elif genre == "softmax":
        if not (isinstance(loi.get("poids"), list) and len(loi["poids"]) == NOMBRE_ISSUES
                and all(_vecteur(l, DIMENSION) for l in loi["poids"]) and _vecteur(loi.get("biais"), NOMBRE_ISSUES)):
            raise Refus("carte hors grammaire : softmax mal formé")
    elif genre == "melange":
        comp = loi.get("composantes")
        if not (isinstance(comp, list) and len(comp) >= 1 and _vecteur(loi.get("poids"), len(comp))
                and all(v >= 0 for v in loi["poids"])):
            raise Refus("carte hors grammaire : mélange mal formé")
        for c in comp:
            valider_loi(c, profondeur + 1)
    elif genre == "si_sinon":
        c = loi.get("condition")
        ok = isinstance(c, dict) and (("sous_population" in c and c["sous_population"] in (0, 1))
                                      or (c.get("indice") in range(DIMENSION) and _nombre(c.get("seuil", 0.0))))
        if not ok:
            raise Refus("carte hors grammaire : condition mal formée")
        valider_loi(loi.get("si"), profondeur + 1)
        valider_loi(loi.get("sinon"), profondeur + 1)
    elif genre == "par_sous_population":
        lois = loi.get("lois")
        if not isinstance(lois, dict) or not set(lois) <= {"0", "1"}:
            raise Refus("carte hors grammaire : par_sous_population mal formé")
        if set(lois) != {"0", "1"} and loi.get("defaut") is None:
            raise Refus("carte hors grammaire : par_sous_population sans loi pour une sous-population ni défaut")
        for sous in list(lois.values()) + ([loi["defaut"]] if loi.get("defaut") is not None else []):
            valider_loi(sous, profondeur + 1)
    else:  # transformee
        valider_loi(loi.get("base"), profondeur + 1)
        connues = {"type", "base", "melange_aveugle", "puissance", "inclinaison", "oscillation"}
        if set(loi) - connues:
            raise Refus(f"carte hors grammaire : clés inconnues {sorted(set(loi) - connues)}")


def carte_du_proposeur(loi):
    """Règle fixée d'avance (phase 1) : une carte absente, illisible ou hors grammaire est refusée, comptée, et remplacée
    par la loi fixe uniforme (aucune information) ; jamais par la médoïde de H ni par une carte antérieure. Rend
    (loi retenue, refusée : bool, motif)."""
    try:
        valider_loi(loi)
        return loi, False, ""
    except Refus as e:
        return dict(CARTE_DE_REMPLACEMENT), True, str(e)
