"""Jeu du monde répondeur (P1, phase 0) et questionneurs factices — v1 (modèle I). Fichier neuf (R12).

Espace des lois candidates H : `taille_h` lois tirées une fois dans la grammaire fermée (`mondes_reponses_p1p2_v1`),
disjointes des lois de référence de production données (signature prédictive, 0,30 nat). Le questionneur connaît H
(l'ensemble énuméré des lois candidates, comme dans la proposition : « bissection gloutonne par gain d'information sur
l'ensemble énuméré des lois candidates »), jamais la loi du monde. Mondes : des lois de H tirées sans remise (un monde par
partie, frais pour chaque partie ; H commun). Avec |H| = 2^T, même une bissection parfaite ne peut en général pas isoler
le monde en T questions Oui ou Non, d'autant que des candidates partagent toutes leurs réponses.

Carte (règle commune à tous les questionneurs, pour n'éprouver que le choix des questions) : après t questions,
l'ensemble S_t des candidates qui contredisent le moins de réponses ; la carte est la médoïde de S_t, la candidate c de
S_t qui minimise la moyenne sur h ∈ S_t de KL(h ‖ c) sur la sonde de score (égalité : plus petit indice). Cette moyenne
se calcule sans matrice : moyenne_h E[h] − (P̄_S · log P_c) / N, où E[h] = Σ P_h log P_h / N et P̄_S la moyenne des P_h.
Score : KL(monde ‖ carte) moyenne sur la sonde de score (nat), carte exacte, égalité de forme ; aucun juge, aucune note
d'un modèle.

Questionneurs factices : aleatoire (uniforme sur les prédicats non encore posés) ; bissection (gain d'information
glouton : prédicat non posé dont la réponse partage S_t au plus près de la moitié, entropie maximale ; égalités tirées au
hasard) ; repeteur (toujours le premier trait présenté ; quand ses prédicats sont épuisés, il les repose) ; disperseur
(directions prises à tour de rôle dans l'ordre présenté des traits, puis g, marginale [, racine], jamais deux fois de
suite la même tant qu'une autre reste) ;
oracle (artefact R5 : lit la loi du monde, carte = monde ; doit donner une divergence nulle et être signalé par la garde
de fuite).
"""
from __future__ import annotations

import time

import numpy as np

from mondes_reponses_p1p2_v1 import (Refus, Repondeur, cle_forme, disjointe, exiger_booleen, grammaire_predicats,
                                     proba_vec, reponses_predicats, tirer_loi)

VERSION = "questionneurs-p1-v1"
DIRECTIONS = ("z0", "z1", "g", "marginale", "racine")
SEUIL_FUITE = 0.05  # au-delà de 5 % de mondes recouverts exactement avant toute question : fuite signalée


# --- espace et mondes ---------------------------------------------------------------------------------------------------
def construire_espace(rng, taille_h, sonde_questions, sonde_score, p_references=(), preds=None):
    """Espace H : lois, réponses vraies de chaque candidate (variante structurelle : 51 colonnes, les 42 premières sont la
    variante empirique), probabilités et log-probabilités aplaties sur la sonde de score, E[h]."""
    preds = preds if preds is not None else grammaire_predicats("structurelle")
    Zq, Gq = sonde_questions
    Zs, Gs = sonde_score
    lois, P, A = [], [], []
    retirees = 0
    while len(lois) < taille_h:
        loi = tirer_loi(rng)
        ps = proba_vec(loi, Zs, Gs)
        if p_references and not disjointe(ps, p_references):
            retirees += 1  # compté et rapporté (garde de disjonction), jamais silencieux
            if retirees > 50 * taille_h:
                raise Refus("garde de disjonction : trop de lois tirées trop proches des références")
            continue
        lois.append(loi)
        P.append(ps.reshape(-1))
        A.append(reponses_predicats(loi, proba_vec(loi, Zq, Gq), Zq, Gq, preds))
    P = np.stack(P)
    L = np.log(P)
    N = Zs.shape[0]
    return {"lois": lois, "A": np.stack(A), "P": P, "L": L, "E": (P * L).sum(axis=1) / N, "N": N,
            "formes": [cle_forme(x) for x in lois], "retirees_disjonction": retirees, "preds": preds}


def tirer_mondes(rng, espace, n):
    """Indices de n mondes, tirés sans remise dans H."""
    if n > len(espace["lois"]):
        raise Refus("plus de mondes que de lois candidates")
    return [int(x) for x in rng.choice(len(espace["lois"]), size=n, replace=False)]


def kl_vers(espace, w, c):
    """KL(loi w ‖ loi c) moyenne sur la sonde de score (nat) ; nulle par définition si c = w."""
    if c == w:
        return 0.0
    return max(0.0, float(espace["E"][w] - espace["P"][w] @ espace["L"][c] / espace["N"]))


def medoide(espace, S):
    S = np.asarray(S)
    pbar = espace["P"][S].mean(axis=0)
    crit = espace["E"][S].mean() - espace["L"][S] @ pbar / espace["N"]
    return int(S[int(np.argmin(crit))])


# --- questionneurs ------------------------------------------------------------------------------------------------------
class Questionneur:
    nom = "abstrait"
    lit_le_monde = False

    def __init__(self, rng):
        self.rng = rng

    def choisir(self, etat):
        raise NotImplementedError


def _non_poses(etat):
    poses = set(etat["posees"])
    return [i for i in range(etat["nombre_predicats"]) if i not in poses]


class Aleatoire(Questionneur):
    nom = "aleatoire"

    def choisir(self, etat):
        libres = _non_poses(etat) or list(range(etat["nombre_predicats"]))
        return int(libres[int(self.rng.integers(len(libres)))])


class Bissection(Questionneur):
    nom = "bissection"

    def choisir(self, etat):
        libres = _non_poses(etat) or list(range(etat["nombre_predicats"]))
        p = etat["A"][etat["S"]][:, libres].mean(axis=0)
        with np.errstate(divide="ignore", invalid="ignore"):
            h = -(np.where(p > 0, p * np.log2(p), 0.0) + np.where(p < 1, (1 - p) * np.log2(1 - p), 0.0))
        meilleurs = np.flatnonzero(h >= h.max() - 1e-12)
        return int(libres[int(meilleurs[int(self.rng.integers(len(meilleurs)))])])


class Repeteur(Questionneur):
    """Toujours le premier trait présenté (ordre des traits tiré par graine, conditions de la mère R-3186, P1 b)."""
    nom = "repeteur"

    def choisir(self, etat):
        dirs = etat["directions"]
        direction = etat["ordre_traits"][0]
        miens = [i for i in range(etat["nombre_predicats"]) if dirs[i] == direction]
        poses = set(etat["posees"])
        libres = [i for i in miens if i not in poses] or miens
        return int(libres[int(self.rng.integers(len(libres)))])


class Disperseur(Questionneur):
    nom = "disperseur"

    def choisir(self, etat):
        dirs = etat["directions"]
        poses = set(etat["posees"])
        presentes = list(etat["ordre_traits"]) + [d for d in DIRECTIONS if d not in ("z0", "z1")]
        ordre = [d for d in presentes if d in set(dirs)]
        derniere = dirs[etat["posees"][-1]] if etat["posees"] else None
        t = len(etat["posees"])
        for decalage in range(len(ordre)):
            d = ordre[(t + decalage) % len(ordre)]
            if d == derniere and len(ordre) > 1:
                continue
            libres = [i for i in range(etat["nombre_predicats"]) if dirs[i] == d and i not in poses]
            if libres:
                return int(libres[int(self.rng.integers(len(libres)))])
        libres = _non_poses(etat) or list(range(etat["nombre_predicats"]))
        return int(libres[int(self.rng.integers(len(libres)))])


class Oracle(Questionneur):
    """Artefact R5 : lit la loi du monde (fuite) ; pose des questions au hasard, mais sa carte est le monde."""
    nom = "oracle"
    lit_le_monde = True

    def choisir(self, etat):
        return Aleatoire.choisir(self, etat)


QUESTIONNEURS = {"aleatoire": Aleatoire, "bissection": Bissection, "repeteur": Repeteur, "disperseur": Disperseur,
                 "oracle": Oracle}


# --- une partie ---------------------------------------------------------------------------------------------------------
POLITIQUES_REFUS = ("arret", "question_perdue")


def jouer_partie(espace, w, questionneur, repondeur, T=16, points=(0, 4, 8, 16), colonnes=None, carte_t0=None,
                 ordre=None, ordre_traits=("z0", "z1"), politique_refus="arret"):
    """Joue une partie contre le monde d'indice w ; rend les mesures par point de carte. `colonnes` : 42 (variante
    empirique) ou None (toutes). `carte_t0` : médoïde de H, la même pour tous (calculée une fois si donnée).

    `ordre` : permutation des prédicats présentés au questionneur (il choisit une position k dans l'ordre présenté ; la
    question posée au monde est le prédicat ordre[k]) ; `ordre_traits` : ordre de présentation des deux traits.
    Règle des refus (conditions de la mère R-3186, P1 c), fixée d'avance : une question hors grammaire, ou une question
    absente (None : le questionneur n'a rien posé), est refusée et comptée ; sous « arret » (questionneurs factices de la
    phase 0 : un refus est un défaut du code) la partie s'arrête par une exception ; sous « question_perdue » (proposeurs
    réels, phase 1) la question consomme une unité du budget et la réponse substituée est « aucune réponse » : aucune
    mise à jour de S_t, jamais Oui, Non ni Inconnu."""
    if politique_refus not in POLITIQUES_REFUS:
        raise Refus(f"politique de refus inconnue : {politique_refus!r}")
    debut = time.process_time()
    A0 = espace["A"] if colonnes is None else espace["A"][:, :colonnes]
    preds0 = espace["preds"] if colonnes is None else espace["preds"][:colonnes]
    ordre = np.arange(A0.shape[1]) if ordre is None else np.asarray(ordre)
    if sorted(ordre.tolist()) != list(range(A0.shape[1])):
        raise Refus("ordre de présentation qui n'est pas une permutation des prédicats")
    A = A0[:, ordre]  # vue présentée
    preds = [preds0[int(i)] for i in ordre]
    directions = [q["direction"] for q in preds]
    desaccords = np.zeros(A.shape[0], dtype=int)
    posees, reponses, cartes, tailles = [], [], {}, []
    questions_perdues = 0
    for t in range(T + 1):
        S = np.flatnonzero(desaccords == desaccords.min())
        tailles.append(int(len(S)))
        if t in points:
            if questionneur.lit_le_monde:
                carte = w  # fuite : la carte est la loi du monde elle-même
            elif t == 0 and carte_t0 is not None:
                carte = carte_t0
            else:
                carte = medoide(espace, S)
            cartes[t] = {"carte": carte, "kl": kl_vers(espace, w, carte), "exacte": bool(carte == w),
                         "forme_egale": espace["formes"][carte] == espace["formes"][w],
                         "taille_S": int(len(S)), "monde_dans_S": bool(desaccords[w] == desaccords.min())}
        if t == T:
            break
        etat = {"A": A, "S": S, "posees": posees, "reponses": reponses, "nombre_predicats": A.shape[1],
                "directions": directions, "ordre_traits": tuple(ordre_traits)}
        k = questionneur.choisir(etat)
        try:
            if k is None:
                repondeur.refus_hors_grammaire += 1
                raise Refus("question absente")
            if isinstance(k, bool) or not isinstance(k, (int, np.integer)) or not 0 <= int(k) < A.shape[1]:
                repondeur.refus_hors_grammaire += 1
                raise Refus(f"question hors grammaire : {k!r}")
            r = exiger_booleen(repondeur.repondre(int(ordre[int(k)])))
        except Refus:
            if politique_refus == "arret":
                raise
            questions_perdues += 1
            continue  # réponse substituée : aucune ; budget consommé
        posees.append(int(k))
        reponses.append(r)
        desaccords += (A[:, k] != r).astype(int)
    info = [float(np.log2(tailles[i] / tailles[i + 1])) for i in range(T)]  # M-P1c
    meme_direction = [directions[posees[i]] == directions[posees[i - 1]] for i in range(1, len(posees))]  # M-P1d
    ouvertes = {(directions[q], preds[q].get("issue")) for q in posees}
    reposees = len(posees) - len(set(posees))  # question déjà posée : répondue de nouveau, budget consommé, comptée
    return {"cartes": cartes, "posees": posees, "information_par_question_bits": info, "questions_reposees": reposees,
            "part_meme_direction_que_la_precedente": float(np.mean(meme_direction)) if meme_direction else float("nan"),
            "directions_ouvertes": len(ouvertes), "refus_hors_grammaire": repondeur.refus_hors_grammaire,
            "questions_perdues": questions_perdues, "posees_au_monde": [int(ordre[k]) for k in posees],
            "temps_processeur_s": time.process_time() - debut}


def ordre_de_presentation(rng, nombre_predicats):
    """Permutation des prédicats et ordre des deux traits, tirés par la graine dérivée de la partie (R-3186, P1 b)."""
    ordre = rng.permutation(nombre_predicats)
    traits = ("z0", "z1") if rng.random() < 0.5 else ("z1", "z0")
    return ordre, traits


def jouer_banc(espace, mondes, noms, rng_par_partie, mode_repondeur="exact", taux=0.0, T=16, points=(0, 4, 8, 16),
               colonnes=42, politique_refus="arret"):
    """Joue chaque questionneur nommé sur chaque monde ; `rng_par_partie(nom, i, role)` rend le générateur de la partie
    (rôles : questionneur, ordre, repondeur). « nom#k » : copie k (graines du questionneur et de l'ordre différentes :
    A/A). « nom#ordre » : même graine de questionneur que « nom », seule la graine de l'ordre change (effet de l'ordre)."""
    carte_t0 = medoide(espace, np.arange(len(espace["lois"]))) if 0 in points else None
    n_pred = espace["A"].shape[1] if colonnes is None else colonnes
    sortie = {nom: [] for nom in noms}
    for i, w in enumerate(mondes):
        vraies = espace["A"][w] if colonnes is None else espace["A"][w, :colonnes]
        for nom in noms:
            base = nom.split("#")[0]
            nom_q = base if nom.endswith("#ordre") else nom
            q = QUESTIONNEURS[base](rng_par_partie(nom_q, i, "questionneur"))
            ordre, traits = ordre_de_presentation(rng_par_partie(nom, i, "ordre"), n_pred)
            rep = Repondeur(vraies, mode_repondeur, taux,
                            rng_par_partie(nom, i, "repondeur") if mode_repondeur != "exact" else None)
            sortie[nom].append(jouer_partie(espace, w, q, rep, T, points, colonnes, carte_t0, ordre, traits,
                                            politique_refus))
    return sortie


# --- statistiques -------------------------------------------------------------------------------------------------------
def bootstrap_diff_medianes(a, b, rng, tirages=10_000):
    """Différence des médianes (a − b), appariée par monde ; intervalle à 95 % par rééchantillonnage des mondes
    (quantiles empiriques 2,5 % et 97,5 %, méthode « inverted_cdf »)."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a.shape != b.shape:
        raise Refus("comparaison non appariée")
    n = len(a)
    idx = rng.integers(0, n, (tirages, n))
    d = np.median(a[idx], axis=1) - np.median(b[idx], axis=1)
    lo, hi = np.quantile(d, [0.025, 0.975], method="inverted_cdf")
    return {"point": float(np.median(a) - np.median(b)), "ic95": [float(lo), float(hi)], "largeur": float(hi - lo)}


def bootstrap_diff_moyennes(a, b, rng, tirages=10_000):
    """Différence des moyennes (a − b), appariée par monde ; intervalle à 95 % par rééchantillonnage des mondes."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a.shape != b.shape:
        raise Refus("comparaison non appariée")
    n = len(a)
    idx = rng.integers(0, n, (tirages, n))
    d = (a - b)[idx].mean(axis=1)
    lo, hi = np.quantile(d, [0.025, 0.975], method="inverted_cdf")
    return {"point": float(np.mean(a - b)), "ic95": [float(lo), float(hi)], "largeur": float(hi - lo)}


NIVEAU = 0.95


def _ic(d, niveau):
    a = (1.0 - niveau) / 2.0
    lo, hi = np.quantile(d, [a, 1.0 - a], method="inverted_cdf")
    return [float(lo), float(hi)]


def bootstrap_double(a, b, rng, tirages=10_000, comparaisons_bonferroni=1):
    """Différence appariée a − b, par les deux statistiques gelées au préenregistrement, sur les MÊMES rééchantillonnages
    des mondes : différence des médianes (lettre de la proposition) et différence des moyennes (voit une dégradation que
    la médiane ne voit pas quand une masse de valeurs nulles dépasse la moitié). Pour chacune : point, intervalle à 95 %
    (quantiles empiriques, « inverted_cdf ») et sa largeur, et intervalle corrigé de Bonferroni au niveau
    1 − 0,05 / `comparaisons_bonferroni` (égal à l'intervalle à 95 % si 1)."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a.shape != b.shape or a.ndim != 1 or len(a) == 0:
        raise Refus("comparaison non appariée")
    if not (isinstance(comparaisons_bonferroni, int) and comparaisons_bonferroni >= 1):
        raise Refus("nombre de comparaisons de Bonferroni : entier ≥ 1")
    n = len(a)
    idx = rng.integers(0, n, (tirages, n))
    niveau_b = 1.0 - (1.0 - NIVEAU) / comparaisons_bonferroni
    sortie = {}
    for nom, d, point in (("medianes", np.median(a[idx], axis=1) - np.median(b[idx], axis=1), np.median(a) - np.median(b)),
                          ("moyennes", (a - b)[idx].mean(axis=1), np.mean(a - b))):
        ic = _ic(d, NIVEAU)
        sortie[nom] = {"point": float(point), "ic95": ic, "largeur95": ic[1] - ic[0],
                       "niveau_corrige": niveau_b, "ic_corrige": _ic(d, niveau_b)}
    sortie["mondes"] = n
    sortie["tirages"] = tirages
    return sortie


def taux_fuite(exactes_t0):
    """Part des mondes où la carte à zéro question est exactement la loi du monde (hasard : 1/|H| par monde)."""
    return float(np.mean(np.asarray(exactes_t0, dtype=bool)))


def colonne(parties, t, champ="kl"):
    return np.array([p["cartes"][t][champ] for p in parties], dtype=float)
