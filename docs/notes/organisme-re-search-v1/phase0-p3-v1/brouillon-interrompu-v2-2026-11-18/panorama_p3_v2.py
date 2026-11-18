"""Panorama de candidats offerts au questionneur (P3, phase 0, sans dépense) — v2 (modèle I, auteur unique). Fichier neuf
(R12) ; la v1 scellée (`panorama_p3_v1.py`) reste en place et n'est plus lancée.

v2 porte la contre-lecture `contre-lecture-phase0-p3-v1.md` et la décision de la mère sur C-2 (option (a)) :
- C-2, option (a) : la carte de reconnaissance est rendue APRÈS t questions fermées posées au monde sur le banc de P1
  (répondeur exact, prédicats empiriques, questionneur aléatoire de P1), puis le panorama est offert ; « sans aide » veut
  dire qu'au moment du choix rien ne vient du répondeur sur les candidats : l'état ne porte que K, le panorama et
  l'historique des t questions et de leurs réponses Oui ou Non (garde `exiger_etat_sans_aide`) ;
- C-1 : la paire (forme vraie, leurre) est tirée, puis ses rôles sont attribués à pile ou face (graine « p3/roles/<i> ») ;
  factices « sans vérité » à préférence de contenu (la plus plate, la plus centrale) au critère, attendus au niveau du
  hasard ; artefact : les mêmes sur les rôles non tirés doivent être vus ; échangeabilité de la paire rapportée et gardée
  (entropie, part des voisines distinctes) ;
- factices non tautologiques : « compatible » (choisit parmi les candidats qui contredisent le moins l'historique, évalué
  sur sa propre sonde) et « contradicteur » (le contraire) ; les factices qui lisent la position vraie ne sont plus au
  critère (rapportés seulement, conformité par identité déclarée) ;
- C-3 : puissance sur un taux de base gelé (le plus haut observé par la contre-lecture, pas 1/8), deux ordres corrélés à
  1, contrôlée par simulation de la règle gelée elle-même (`trois_issues`) ; sensibilité à δ ;
- C-4 : devis en nombre d'appels seulement ; longueur du panorama mesurée sans dépense ;
- C-6, C-7 : remplisseurs d'un autre couple (type de racine, complexité) ; distinction des remplisseurs du leurre et entre
  eux gardée ; absence de biais de position jugée par équivalence.

Le code de P1 (`../phase0-p1-p2-v1/`) est réemployé par import, sans modification. Aucun juge (N-058). Aucun appel réseau,
aucun appel de modèle, aucune dépense.
"""
from __future__ import annotations

import copy
import json
import math
import sys
from pathlib import Path
from statistics import NormalDist
from types import MappingProxyType

import numpy as np

ICI = Path(__file__).resolve().parent
DOSSIER_P1 = (ICI.parent / "phase0-p1-p2-v1").resolve()
if str(DOSSIER_P1) not in sys.path:
    sys.path.insert(0, str(DOSSIER_P1))

import mondes_reponses_p1p2_v1 as mr  # noqa: E402  (code de P1, réemployé sans modification)
import questionneurs_p1_v2 as qp  # noqa: E402  (code de P1, réemployé sans modification)

VERSION = "panorama-p3-v2"
Refus = mr.Refus

ISSUES = ("au-dessus du hasard", "au niveau du hasard", "en dessous du hasard", "non concluant")
GRAMMAIRE = mr.grammaire_predicats("empirique")  # 42 prédicats de P1 : seuls permis dans l'historique


# --- familles ---------------------------------------------------------------------------------------------------------
def noeuds(loi) -> int:
    if isinstance(loi, dict):
        return (1 if "type" in loi else 0) + sum(noeuds(v) for v in loi.values())
    if isinstance(loi, list):
        return sum(noeuds(v) for v in loi)
    return 0


def famille(loi) -> tuple:
    """Couple (type de la racine, complexité = nombre de nœuds typés)."""
    if not isinstance(loi, dict) or loi.get("type") not in mr.TYPES:
        raise Refus(f"loi hors grammaire pour la famille : {loi!r:.80}")
    return (loi["type"], noeuds(loi))


def index_familles(espace) -> tuple:
    fams = [famille(l) for l in espace["lois"]]
    index = {}
    for i, f in enumerate(fams):
        index.setdefault(f, []).append(i)
    return fams, {f: np.asarray(v) for f, v in index.items()}


def distinctes(espace, a, b, seuil) -> bool:
    return a != b and qp.kl_vers(espace, a, b) > seuil and qp.kl_vers(espace, b, a) > seuil


# --- paire, rôles à pile ou face, remplisseurs --------------------------------------------------------------------------
def choisir_leurre(espace, a, fams, index, rng, seuil):
    candidats = [int(c) for c in index[fams[a]] if int(c) != a]
    for c in rng.permutation(len(candidats)) if candidats else []:
        if distinctes(espace, a, candidats[int(c)], seuil):
            return candidats[int(c)]
    return None


def tirer_paires(espace, fams, index, n, rng_ordre, rng_leurre_de, rng_role_de, seuil, limite_ecartes):
    """n paires (a, b) : a tirée sans remise dans H, b une loi de même couple distincte de a ; puis rôles à pile ou face
    (C-1) : avec probabilité 1/2, le monde est b et le leurre a. Les lois sans leurre sont écartées, comptées, et l'arrêt
    tombe au-delà de `limite_ecartes` (borne réelle de la sélection vers les familles peuplées, C-7 i)."""
    paires, ecartes = [], 0
    for a in rng_ordre.permutation(len(espace["lois"])):
        a = int(a)
        b = choisir_leurre(espace, a, fams, index, rng_leurre_de(a), seuil)
        if b is None:
            ecartes += 1
            if ecartes > limite_ecartes:
                raise Refus(f"plus de {limite_ecartes} lois sans leurre apparié : arrêt de P3")
            continue
        i = len(paires)
        echange = bool(rng_role_de(i).random() < 0.5)
        w, l = (b, a) if echange else (a, b)
        paires.append({"premiere_tiree": a, "seconde": b, "echange": echange, "monde": w, "leurre": l})
        if len(paires) == n:
            return paires, ecartes
    raise Refus("pas assez de paires dans H : arrêt de P3")


def choisir_remplisseurs(espace, w, leurre, fams, rng, nombre, seuil, essais_max=None):
    """`nombre` lois de H d'un autre couple (type de racine, complexité) que le monde (elles peuvent avoir son type de
    racine, C-6), distinctes entre elles, du monde et du leurre."""
    essais_max = essais_max if essais_max is not None else 2000 * max(1, nombre)
    pris, essais = [], 0
    while len(pris) < nombre:
        essais += 1
        if essais > essais_max:
            raise Refus("remplisseurs introuvables (trop d'essais) : arrêt de P3")
        c = int(rng.integers(len(espace["lois"])))
        if fams[c] == fams[w] or c in pris or c in (w, leurre):
            continue
        if all(distinctes(espace, c, x, seuil) for x in [w, leurre] + pris):
            pris.append(c)
    return pris


# --- plan des positions -----------------------------------------------------------------------------------------------
def plan_positions(rng, n, K) -> np.ndarray:
    if K < 2 or n % K:
        raise Refus(f"plan impossible : n = {n} n'est pas un multiple de K = {K}")
    return np.concatenate([rng.permutation(K) for _ in range(n // K)]).astype(int)


def position_presentee(p, ordre, K) -> int:
    if ordre == 1:
        return int(p)
    if ordre == 2:
        return int(K - 1 - p)
    raise Refus(f"ordre de présentation inconnu : {ordre!r}")


def exiger_plan_equilibre(positions, K) -> dict:
    positions = np.asarray(positions, dtype=int)
    n = len(positions)
    if K < 2 or n == 0 or n % K:
        raise Refus("plan des positions : taille non multiple de K")
    for b in range(n // K):
        if sorted(positions[b * K:(b + 1) * K].tolist()) != list(range(K)):
            raise Refus(f"plan des positions non équilibré dans le bloc {b}")
    comptes = {}
    for ordre in (1, 2):
        c = np.bincount([position_presentee(p, ordre, K) for p in positions], minlength=K)
        if len(c) != K or not np.all(c == n // K):
            raise Refus(f"plan des positions non équilibré pour l'ordre {ordre} : {c.tolist()}")
        comptes[str(ordre)] = c.tolist()
    return comptes


# --- panoramas --------------------------------------------------------------------------------------------------------
def construire_panorama(w, leurre, remplisseurs, position, K) -> dict:
    if len(remplisseurs) != K - 1:
        raise Refus("nombre de remplisseurs ≠ K − 1")
    reste = list(remplisseurs)
    return {"C": reste[:position] + [w] + reste[position:], "B": reste[:position] + [leurre] + reste[position:],
            "position": int(position), "monde": int(w), "leurre": int(leurre)}


def presenter(indices, ordre):
    if ordre == 1:
        return list(indices)
    if ordre == 2:
        return list(reversed(indices))
    raise Refus(f"ordre de présentation inconnu : {ordre!r}")


def exiger_panorama(pan, fams, K, espace=None, seuil=None) -> None:
    """Garde d'un panorama apparié ; avec `espace`, distinction (signature) du leurre au monde, et des remplisseurs au
    monde, au leurre et entre eux (C-7 iii)."""
    C, B, p, w, l = pan["C"], pan["B"], pan["position"], pan["monde"], pan["leurre"]
    if len(C) != K or len(B) != K or len(set(C)) != K or len(set(B)) != K:
        raise Refus("panorama : taille ≠ K ou doublon")
    if not 0 <= p < K or C[p] != w or B[p] != l:
        raise Refus("panorama : cible absente de sa position")
    if w in B or l in C or l == w:
        raise Refus("panorama : forme vraie dans B ou leurre dans C")
    if any(C[k] != B[k] for k in range(K) if k != p):
        raise Refus("panorama : C et B diffèrent hors de la position de la cible")
    if fams[l] != fams[w]:
        raise Refus(f"leurre non apparié : couple {fams[l]} ≠ {fams[w]}")
    remp = [C[k] for k in range(K) if k != p]
    if any(fams[x] == fams[w] for x in remp):
        raise Refus("remplisseur du couple du monde : le couple désignerait deux positions")
    if espace is not None:
        if not distinctes(espace, w, l, seuil):
            raise Refus("leurre non distinct du monde (signature prédictive)")
        for j, x in enumerate(remp):
            if not all(distinctes(espace, x, y, seuil) for y in [w, l] + remp[:j]):
                raise Refus("remplisseur non distinct du monde, du leurre ou d'un autre remplisseur")


# --- historique des t questions (banc de P1) ----------------------------------------------------------------------------
def historique_de(espace, monde, questions_au_monde, t):
    """(prédicat, réponse) pour les t premières questions posées, répondues par la loi `monde` (répondeur exact de P1 :
    colonne de la matrice des réponses vraies)."""
    if t > len(questions_au_monde):
        raise Refus("historique plus long que les questions posées")
    return tuple((GRAMMAIRE[int(q)], bool(espace["A"][monde, int(q)])) for q in questions_au_monde[:t])


# --- carte de reconnaissance sans aide (option (a)) ----------------------------------------------------------------------
CLES_ETAT_CARTE = ("K", "historique", "panorama")
_PREDICATS_PERMIS = {json.dumps(p, sort_keys=True) for p in GRAMMAIRE}


def etat_de_carte(lois_presentees, historique):
    return MappingProxyType({"K": len(lois_presentees), "panorama": tuple(copy.deepcopy(l) for l in lois_presentees),
                             "historique": tuple((dict(p), r) for p, r in historique)})


def exiger_etat_sans_aide(etat, t) -> None:
    """Garde « sans aide » (option (a)) : l'état ne porte que K, le panorama et l'historique ; l'historique a exactement
    t entrées, chacune un prédicat de la grammaire fermée de P1 et une réponse booléenne ; aucune autre information
    (aucune confirmation d'un candidat, aucune position, aucun « Inconnu »)."""
    if tuple(sorted(etat)) != CLES_ETAT_CARTE:
        raise Refus(f"état de carte avec une aide (clés {sorted(etat)})")
    if etat["K"] != len(etat["panorama"]):
        raise Refus("état de carte : K ≠ taille du panorama")
    h = etat["historique"]
    if len(h) != t:
        raise Refus(f"état de carte : historique de {len(h)} questions au lieu de {t}")
    for e in h:
        if not (isinstance(e, tuple) and len(e) == 2 and isinstance(e[1], bool)):
            raise Refus("état de carte : entrée d'historique qui n'est pas (prédicat, Oui ou Non)")
        if json.dumps(e[0], sort_keys=True) not in _PREDICATS_PERMIS:
            raise Refus(f"état de carte : question hors grammaire dans l'historique : {e[0]!r:.80}")


class QuestionneurCarte:
    nom = "abstrait"
    simule_verite = False

    def __init__(self, rng, outils=None):
        self.rng = rng
        self.outils = outils or {}

    def choisir_carte(self, etat, verite=None):
        raise NotImplementedError


class Premier(QuestionneurCarte):
    nom = "premier"

    def choisir_carte(self, etat, verite=None):
        return 0


class Dernier(QuestionneurCarte):
    nom = "dernier"

    def choisir_carte(self, etat, verite=None):
        return etat["K"] - 1


class Hasard(QuestionneurCarte):
    """Bras « choix au hasard »."""
    nom = "hasard"

    def choisir_carte(self, etat, verite=None):
        return int(self.rng.integers(etat["K"]))


def _probas(outils, loi, sonde_cle):
    """Probabilités d'une loi sur la sonde propre au factice (mémorisées par contenu : un calcul, pas une aide)."""
    cache = outils.setdefault("cache", {})
    cle = (sonde_cle, mr.canon(loi))
    if cle not in cache:
        cache[cle] = mr.proba_vec(loi, *outils[sonde_cle])
    return cache[cle]


class Plate(QuestionneurCarte):
    """Sans vérité, préférence de contenu (C-1) : la loi d'entropie moyenne la plus haute sur sa sonde."""
    nom = "plate"

    def choisir_carte(self, etat, verite=None):
        h = [float(-(p * np.log(p)).sum(axis=1).mean()) for p in (_probas(self.outils, l, "sonde") for l in etat["panorama"])]
        return int(np.argmax(h))


class Centrale(QuestionneurCarte):
    """Sans vérité, préférence de contenu (C-1) : la loi de divergence moyenne (deux sens) la plus basse aux autres."""
    nom = "centrale"

    def choisir_carte(self, etat, verite=None):
        P = [_probas(self.outils, l, "sonde") for l in etat["panorama"]]
        kl = np.array([[0.0 if i == j else mr.kl_moyenne(a, b) for j, b in enumerate(P)] for i, a in enumerate(P)])
        return int(np.argmin((kl.sum(axis=0) + kl.sum(axis=1)) / (2 * (len(P) - 1))))


def desaccords(outils, lois, historique):
    """Nombre de réponses de l'historique que chaque candidate contredit, prédicats évalués sur la sonde propre."""
    Z, G = outils["sonde_q"]
    preds = [p for p, _ in historique]
    rep = np.array([r for _, r in historique], dtype=bool)
    sortie = []
    for loi in lois:
        if not preds:
            sortie.append(0)
            continue
        v = mr.reponses_predicats(loi, _probas(outils, loi, "sonde_q"), Z, G, preds)
        sortie.append(int(np.sum(v != rep)))
    return np.array(sortie)


class Compatible(QuestionneurCarte):
    """Sans vérité, non tautologique : choisit au hasard parmi les candidates qui contredisent le moins l'historique."""
    nom = "compatible"

    def choisir_carte(self, etat, verite=None):
        d = desaccords(self.outils, etat["panorama"], etat["historique"])
        m = np.flatnonzero(d == d.min())
        return int(m[int(self.rng.integers(len(m)))])


class Contradicteur(QuestionneurCarte):
    """Sans vérité, non tautologique : choisit au hasard parmi les candidates qui contredisent le plus l'historique."""
    nom = "contradicteur"

    def choisir_carte(self, etat, verite=None):
        d = desaccords(self.outils, etat["panorama"], etat["historique"])
        m = np.flatnonzero(d == d.max())
        return int(m[int(self.rng.integers(len(m)))])


class Reconnaisseur(QuestionneurCarte):
    """Simulé (rapporté seulement) : lit la position vraie ; sa conformité est une identité (C-2), déclarée."""
    nom = "reconnaisseur"
    simule_verite = True

    def __init__(self, rng, outils=None, rho=1.0):
        super().__init__(rng, outils)
        self.rho = float(rho)

    def choisir_carte(self, etat, verite=None):
        pv = verite["position_vraie"]
        if pv is not None and self.rng.random() < self.rho:
            return int(pv)
        return int(self.rng.integers(etat["K"]))


class Evitant(QuestionneurCarte):
    """Simulé (rapporté seulement)."""
    nom = "evitant"
    simule_verite = True

    def __init__(self, rng, outils=None, rho=1.0):
        super().__init__(rng, outils)
        self.rho = float(rho)

    def choisir_carte(self, etat, verite=None):
        K, pv = etat["K"], verite["position_vraie"]
        if pv is not None and self.rng.random() < self.rho:
            autres = [k for k in range(K) if k != pv]
            return int(autres[int(self.rng.integers(len(autres)))])
        return int(self.rng.integers(K))


class Famille(QuestionneurCarte):
    """Artefact simulé : connaît le couple du monde, choisit la position de ce couple (la cible, dans C comme dans B)."""
    nom = "famille"
    simule_verite = True

    def choisir_carte(self, etat, verite=None):
        fm = tuple(verite["famille_monde"])
        for k, loi in enumerate(etat["panorama"]):
            if famille(loi) == fm:
                return k
        return int(self.rng.integers(etat["K"]))


FACTICES_SIMULES = ("reconnaisseur", "evitant", "famille")
CLASSES = {"premier": Premier, "dernier": Dernier, "hasard": Hasard, "plate": Plate, "centrale": Centrale,
           "compatible": Compatible, "contradicteur": Contradicteur, "famille": Famille}


def fabriquer_questionneur(spec, rng, outils=None):
    nom, _, param = spec.partition(":")
    if nom in CLASSES:
        if param:
            raise Refus(f"paramètre inattendu : {spec}")
        return CLASSES[nom](rng, outils)
    if nom in ("reconnaisseur", "evitant"):
        rho = float(param) if param else 1.0
        if not 0.0 <= rho <= 1.0:
            raise Refus(f"ρ hors de [0, 1] : {spec}")
        return (Reconnaisseur if nom == "reconnaisseur" else Evitant)(rng, outils, rho)
    raise Refus(f"questionneur de carte inconnu : {spec!r}")


def jouer_carte(q, lois_presentees, historique, verite, t, politique_refus="arret"):
    """Carte de reconnaissance après t questions, sans aide : état = K, panorama, historique (garde) ; la vérité n'est
    passée qu'à un factice simulé déclaré. Rend (position, refusée)."""
    if politique_refus not in ("arret", "carte_perdue"):
        raise Refus(f"politique de refus inconnue : {politique_refus!r}")
    if q.simule_verite and q.nom not in FACTICES_SIMULES:
        raise Refus(f"questionneur « {q.nom} » qui lit la vérité sans être un factice déclaré : refus")
    etat = etat_de_carte(lois_presentees, historique)
    exiger_etat_sans_aide(etat, t)
    k = q.choisir_carte(etat, verite if q.simule_verite else None)
    if isinstance(k, bool) or not isinstance(k, (int, np.integer)) or not 0 <= int(k) < len(lois_presentees):
        if politique_refus == "arret":
            raise Refus(f"carte hors panorama : {k!r}")
        return None, True
    return int(k), False


def jouer_reconnaissance(espace, fams, panoramas, historiques, specs, rng_carte, outils_de, K, t, politique_refus="arret"):
    """Chaque questionneur × monde × bras (C, B) × ordre (1, 2) : position choisie et si c'est la cible. L'historique du
    monde i (le même pour C, B et les deux ordres : questions posées avant le panorama) est `historiques[i]`."""
    sortie = {}
    for spec in specs:
        outils = outils_de(spec)
        cC = np.zeros((len(panoramas), 2), dtype=int)
        cB, chC, chB = np.zeros_like(cC), np.zeros_like(cC), np.zeros_like(cC)
        refus = 0
        for i, pan in enumerate(panoramas):
            for j, ordre in enumerate((1, 2)):
                pos = position_presentee(pan["position"], ordre, K)
                for bras, cible, choix in (("C", cC, chC), ("B", cB, chB)):
                    lois = [espace["lois"][x] for x in presenter(pan[bras], ordre)]
                    verite = {"position_vraie": pos if bras == "C" else None, "famille_monde": fams[pan["monde"]]}
                    q = fabriquer_questionneur(spec, rng_carte(spec, bras, ordre, i), outils)
                    k, refusee = jouer_carte(q, lois, historiques[i], verite, t, politique_refus)
                    if refusee:
                        refus += 1
                        choix[i, j] = -1
                        continue
                    choix[i, j] = k
                    cible[i, j] = int(k == pos)
        sortie[spec] = {"cible_C": cC, "cible_B": cB, "choix_C": chC, "choix_B": chB, "refus": refus}
    return sortie


# --- statistiques et trois issues ---------------------------------------------------------------------------------------
def _ic(x, niveau):
    a = (1.0 - niveau) / 2.0
    lo, hi = np.quantile(x, [a, 1.0 - a], method="inverted_cdf")
    return [float(lo), float(hi)]


def issue(lo, hi, delta) -> str:
    """Règle gelée à trois issues (plus « non concluant »)."""
    if lo > 0:
        return ISSUES[0]
    if hi < 0:
        return ISSUES[2]
    if -delta < lo and hi < delta:
        return ISSUES[1]
    return ISSUES[3]


def grandeur(lo, hi, delta, iss) -> str:
    """Grandeur rapportée avec une issue au-dessus ou en dessous (C-3) : un écart entier sous la marge n'est pas lu comme
    une reconnaissance qui compte."""
    if iss not in ISSUES[:3:2]:
        return "sans objet"
    a, b = (lo, hi) if iss == ISSUES[0] else (-hi, -lo)
    if b < delta:
        return "sous la marge"
    if a >= delta:
        return "au-delà de la marge"
    return "chevauche la marge"


def trois_issues(cible_C, cible_B, rng, tirages, niveau, delta, K) -> dict:
    cC, cB = np.asarray(cible_C, dtype=float), np.asarray(cible_B, dtype=float)
    if cC.shape != cB.shape or cC.ndim != 2 or cC.shape[0] == 0:
        raise Refus("trois issues : tableaux non appariés")
    dw = (cC - cB).mean(axis=1)
    tC, tB = cC.mean(axis=1), cB.mean(axis=1)
    n = len(dw)
    idx = rng.integers(0, n, (tirages, n))
    ic_d, ic_c, ic_b = _ic(dw[idx].mean(axis=1), niveau), _ic(tC[idx].mean(axis=1), niveau), _ic(tB[idx].mean(axis=1), niveau)
    iss = issue(ic_d[0], ic_d[1], delta)
    return {"mondes": n, "ordres": int(cC.shape[1]), "niveau": niveau, "delta": delta,
            "ecart_D": {"point": float(dw.mean()), "ic": ic_d, "largeur": ic_d[1] - ic_d[0]},
            "taux_C": {"point": float(tC.mean()), "ic": ic_c}, "taux_B": {"point": float(tB.mean()), "ic": ic_b},
            "hasard_1_sur_K": 1.0 / K, "issue": iss, "grandeur": grandeur(ic_d[0], ic_d[1], delta, iss),
            "lecture_sans_leurre_taux_C_moins_1_sur_K": issue(ic_c[0] - 1.0 / K, ic_c[1] - 1.0 / K, delta)}


def biais_de_position(choix_C, choix_B, rng, tirages, niveau_position, K, delta_position) -> dict:
    """Part des choix aux positions première et dernière (C et B, deux ordres). Un biais VERS une position est un excès de
    sa part sur 1/K. Pour chacune : « détecté » si la borne basse dépasse 1/K + δ_pos ; « absent » si la borne haute est
    sous 1/K + δ_pos (équivalence unilatérale : aucun excès qui compte, C-7 v) ; sinon « indéterminé »."""
    ch = np.concatenate([np.asarray(choix_C), np.asarray(choix_B)], axis=1)
    if np.any(ch < 0):
        raise Refus("biais de position : choix refusé présent")
    n = ch.shape[0]
    parts = np.stack([(ch == k).mean(axis=1) for k in range(K)], axis=1)
    idx = rng.integers(0, n, (tirages, n))
    h = 1.0 / K
    sortie = {"parts_par_position": parts.mean(axis=0).tolist(), "niveau": niveau_position, "delta_position": delta_position}
    for nom, k in (("premiere", 0), ("derniere", K - 1)):
        ic = _ic(parts[idx, k].mean(axis=1), niveau_position)
        etat = "detecte" if ic[0] > h + delta_position else "absent" if ic[1] < h + delta_position else "indetermine"
        sortie[nom] = {"ic": ic, "etat": etat}
    return sortie


# --- attentes gelées des factices du critère ---------------------------------------------------------------------------
ATTENTES_FACTICES = {
    "hasard": {"issue": ISSUES[1], "premiere": "absent", "derniere": "absent"},
    "premier": {"issue": ISSUES[1], "premiere": "detecte", "derniere": "absent", "ecart_exactement_nul": True},
    "dernier": {"issue": ISSUES[1], "premiere": "absent", "derniere": "detecte", "ecart_exactement_nul": True},
    "plate": {"issue": ISSUES[1], "premiere": "absent", "derniere": "absent"},
    "centrale": {"issue": ISSUES[1], "premiere": "absent", "derniere": "absent"},
    "compatible": {"issue": ISSUES[0], "premiere": "absent", "derniere": "absent"},
    "contradicteur": {"issue": ISSUES[2], "premiere": "absent", "derniere": "absent"},
    "famille": {"issue": ISSUES[1], "ecart_exactement_nul": True, "taux_C_exact": 1.0, "sans_leurre": ISSUES[0],
                "premiere": "absent", "derniere": "absent"},
}


def conforme(spec, lecture, biais) -> dict:
    att = ATTENTES_FACTICES[spec]
    d = {"issue": lecture["issue"] == att["issue"]}
    for pos in ("premiere", "derniere"):
        if pos in att:
            d[pos] = biais[pos]["etat"] == att[pos]
    if att.get("ecart_exactement_nul"):
        d["ecart_exactement_nul"] = lecture["ecart_D"]["point"] == 0.0 and lecture["ecart_D"]["largeur"] == 0.0
    if "taux_C_exact" in att:
        d["taux_C_exact"] = lecture["taux_C"]["point"] == att["taux_C_exact"]
    if "sans_leurre" in att:
        d["sans_leurre"] = lecture["lecture_sans_leurre_taux_C_moins_1_sur_K"] == att["sans_leurre"]
    return {"attente": att, "detail": d, "tient": all(d.values())}


# --- échangeabilité de la paire (C-1 c) -------------------------------------------------------------------------------
def part_voisines_distinctes(espace, x, fams, index, rng, seuil, echantillon):
    autres = [int(c) for c in index[fams[x]] if int(c) != x]
    if not autres:
        return 0.0
    pris = [autres[int(j)] for j in rng.permutation(len(autres))[:echantillon]]
    return float(np.mean([distinctes(espace, x, c, seuil) for c in pris]))


def echangeabilite(espace, fams, index, mondes, leurres, rng_de, seuil, echantillon, rng_boot, tirages, niveau, marges):
    """Écarts monde − leurre, appariés par paire : entropie moyenne (nat, sonde de score) et part des voisines distinctes
    de la famille (échantillon gelé). Équivalence si l'intervalle est entièrement dans ]−marge ; marge[."""
    ent = -np.asarray(espace["E"])
    d_ent = np.array([ent[w] - ent[l] for w, l in zip(mondes, leurres)])
    d_vois = np.array([part_voisines_distinctes(espace, w, fams, index, rng_de(w), seuil, echantillon)
                       - part_voisines_distinctes(espace, l, fams, index, rng_de(l), seuil, echantillon)
                       for w, l in zip(mondes, leurres)])
    n = len(d_ent)
    idx = rng_boot.integers(0, n, (tirages, n))
    sortie = {}
    for nom, d in (("entropie_nat", d_ent), ("part_voisines_distinctes", d_vois)):
        ic = _ic(d[idx].mean(axis=1), niveau)
        m = marges[nom]
        sortie[nom] = {"point": float(d.mean()), "ic": ic, "marge": m, "equivalent": -m < ic[0] and ic[1] < m}
    sortie["tient"] = all(sortie[k]["equivalent"] for k in ("entropie_nat", "part_voisines_distinctes"))
    return sortie


# --- calcul de puissance -----------------------------------------------------------------------------------------------
def _z(p):
    return NormalDist().inv_cdf(p)


def variance_ecart(p_c, p_b) -> float:
    return p_c * (1 - p_c) + p_b * (1 - p_b)


def scenarios(p0, rho_min, rho_evitant) -> dict:
    """Taux (C, B) des trois issues vraies au taux de base p0 : au niveau (p0, p0) ; au-dessus, reconnaissance ρ_min
    (ρ_min + (1 − ρ_min)·p0, p0) ; en dessous, évitement ρ_e ((1 − ρ_e)·p0, p0)."""
    return {"au_niveau": (p0, p0), "au_dessus": (rho_min + (1 - rho_min) * p0, p0),
            "en_dessous": ((1 - rho_evitant) * p0, p0)}


def taille_analytique(K, p0, delta, rho_min, rho_evitant, niveau, puissance) -> dict:
    """Approximation normale, deux ordres corrélés à 1 (l'unité est le monde), indicatrices C et B indépendantes."""
    if not (K >= 2 and 0 < p0 < 1 and 0 < delta < 1 and 0 < rho_min <= 1 and 0 < rho_evitant <= 1
            and 0.5 < niveau < 1 and 0.5 < puissance < 1):
        raise Refus("paramètres de puissance hors domaine")
    sc = scenarios(p0, rho_min, rho_evitant)
    d_moins = sc["en_dessous"][0] - p0
    if abs(d_moins) <= delta:
        raise Refus("l'écart « en dessous » visé ne dépasse pas la marge : issues non séparables")
    za = _z(1 - (1 - niveau) / 2)
    n = {"au_niveau": variance_ecart(p0, p0) * ((za + _z((1 + puissance) / 2)) / delta) ** 2}
    for nom in ("au_dessus", "en_dessous"):
        pc, pb = sc[nom]
        n[nom] = variance_ecart(pc, pb) * ((za + _z(puissance)) / abs(pc - pb)) ** 2
    brut = max(n.values())
    return {"n_par_issue": n, "brut": brut, "n_multiple_de_K": int(math.ceil(math.ceil(brut) / K) * K), "z_niveau": za,
            "scenarios": {k: list(v) for k, v in sc.items()}}


def puissance_regle_gelee(n, p_c, p_b, rng, repetitions, tirages, niveau, delta, K) -> dict:
    """Part des répétitions où la règle gelée ELLE-MÊME (`trois_issues` : rééchantillonnage des mondes, `inverted_cdf`)
    rend chaque issue, deux ordres corrélés à 1 (le même tirage recopié dans les deux colonnes) (C-3)."""
    comptes = {i: 0 for i in ISSUES}
    for _ in range(repetitions):
        c = (rng.random(n) < p_c).astype(int)
        b = (rng.random(n) < p_b).astype(int)
        r = trois_issues(np.stack([c, c], axis=1), np.stack([b, b], axis=1), rng, tirages, niveau, delta, K)
        comptes[r["issue"]] += 1
    return {k: v / repetitions for k, v in comptes.items()}


ATTENDUE = {"au_niveau": ISSUES[1], "au_dessus": ISSUES[0], "en_dessous": ISSUES[2]}


def verifier_taille(n, K, p0, delta, rho_min, rho_evitant, niveau, puissance, repetitions, tirages, racine) -> dict:
    """À la taille n, puissance de la règle gelée pour chaque issue vraie (graines « p3/puissance/<issue>/<n> »)."""
    sc = scenarios(p0, rho_min, rho_evitant)
    res = {}
    for nom, (pc, pb) in sc.items():
        rng = mr.generateur(f"p3/puissance/{nom}/{n}", racine)
        res[nom] = puissance_regle_gelee(n, pc, pb, rng, repetitions, tirages, niveau, delta, K)
    return {"n": n, "par_issue": res, "tient": all(res[k][ATTENDUE[k]] >= puissance for k in res)}


def rechercher_taille(K, p0, delta, rho_min, rho_evitant, niveau, puissance, repetitions, tirages, racine, pas=None,
                      essais_max=40) -> dict:
    """Taille gelée : partir de la taille analytique (multiple de K) et monter par pas de `pas` (défaut 8K) jusqu'à ce
    que la règle gelée rende chaque issue vraie avec une probabilité au moins `puissance`."""
    an = taille_analytique(K, p0, delta, rho_min, rho_evitant, niveau, puissance)
    pas = pas or 8 * K
    n, essais = an["n_multiple_de_K"], []
    for _ in range(essais_max):
        v = verifier_taille(n, K, p0, delta, rho_min, rho_evitant, niveau, puissance, repetitions, tirages, racine)
        essais.append(v)
        if v["tient"]:
            return {"analytique": an, "essais": essais, "n_retenu": n}
        n += pas
    raise Refus("recherche de taille sans issue")


def sensibilite_delta(K, p0, rho_min, rho_evitant, niveau, puissance, deltas) -> dict:
    sortie = {}
    for d in deltas:
        try:
            sortie[str(d)] = taille_analytique(K, p0, d, rho_min, rho_evitant, niveau, puissance)["n_multiple_de_K"]
        except Refus as e:
            sortie[str(d)] = f"refus : {e}"
    return sortie


# --- appels de la phase 1 (C-4 : nombre d'appels seulement) -------------------------------------------------------------
def appels_phase1(n_mondes, t, cartes_par_monde, proposeurs) -> dict:
    """Par proposeur et par monde : t questions (historique commun aux deux bras et aux deux ordres) + 4 cartes."""
    par = n_mondes * (t + cartes_par_monde)
    return {"mondes_par_proposeur": n_mondes, "questions_par_monde": t, "cartes_par_monde": cartes_par_monde,
            "appels_par_proposeur": par, "proposeurs": proposeurs, "appels_total": par * proposeurs,
            "prix": "aucun : prix d'un appel de question et d'un appel de carte à relever (aucune source qui convienne)"}


def longueur_panorama(lois) -> int:
    """Caractères du JSON canonique de la liste des lois présentées (borne de l'entrée d'un appel de carte)."""
    return len(json.dumps(lois, sort_keys=True, ensure_ascii=False, separators=(",", ":")))
