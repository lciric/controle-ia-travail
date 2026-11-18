"""Panorama de candidats offerts au questionneur (P3, phase 0, sans dépense) — v1 (modèle I, auteur unique). Fichier neuf
(R12). Monté sur l'instrument de P1 : le code de P1 (`../phase0-p1-p2-v1/`) est réemployé par import, sans modification ;
le lanceur vérifie ses empreintes scellées.

Contenu :
- familles et complexité d'une loi (famille = type de la racine ; complexité = nombre de nœuds typés) ;
- leurre apparié à la forme vraie : une loi de l'espace H de même famille et de même complexité, distincte de la loi du
  monde au sens de la signature prédictive (divergence moyenne > 0,30 nat dans les deux sens) ;
- remplisseurs : K − 1 lois de H d'une autre famille que le monde, distinctes entre elles, du monde et du leurre ;
- plan des positions réparti d'avance : blocs de K positions, chaque bloc une permutation tirée par graine dérivée ; tout
  préfixe de m·K mondes est équilibré ; deux ordres de présentation (ordre 1 : plan ; ordre 2 : miroir, position K−1−p) ;
- panoramas appariés : C (forme vraie à la position du plan) et B (leurre à la même position, le reste identique) ;
- carte de reconnaissance SANS aide : le questionneur choisit une position du panorama avant toute question ; l'état qu'il
  reçoit ne porte que K et le panorama ; aucun répondeur n'existe à ce moment ;
- questionneurs factices de carte à biais connu : premier, dernier, hasard (bras « choix au hasard »), reconnaisseur(ρ),
  évitant(ρ), famille (artefact : choisit la famille du monde, que seul le leurre apparié démasque) ;
- règle à trois issues (au-dessus du hasard, au niveau du hasard, en dessous ; « non concluant » sinon) ;
- calcul de puissance (approximation normale, variance prudente) et devis refait sur la taille qui en sort.

Aucun juge : la vérité est celle du monde planté (N-058). Aucun appel réseau, aucun appel de modèle, aucune dépense.
"""
from __future__ import annotations

import copy
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

VERSION = "panorama-p3-v1"
Refus = mr.Refus  # même classe de refus que le code de P1 (aucun repli silencieux)

ISSUES = ("au-dessus du hasard", "au niveau du hasard", "en dessous du hasard", "non concluant")


# --- familles ---------------------------------------------------------------------------------------------------------
def noeuds(loi) -> int:
    """Nombre de nœuds typés (dictionnaires portant « type ») de l'arbre de la loi : la complexité."""
    if isinstance(loi, dict):
        return (1 if "type" in loi else 0) + sum(noeuds(v) for v in loi.values())
    if isinstance(loi, list):
        return sum(noeuds(v) for v in loi)
    return 0


def famille(loi) -> tuple:
    """(type de la racine, complexité). Même famille et même complexité = même couple."""
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
    """Deux lois de H sont des hypothèses distinctes si la divergence moyenne dépasse `seuil` dans les deux sens."""
    return a != b and qp.kl_vers(espace, a, b) > seuil and qp.kl_vers(espace, b, a) > seuil


# --- leurre apparié et remplisseurs -----------------------------------------------------------------------------------
def choisir_leurre(espace, w, fams, index, rng, seuil):
    """Une loi de H de même famille et même complexité que le monde w, distincte de lui ; None s'il n'y en a aucune."""
    candidats = [int(c) for c in index[fams[w]] if int(c) != w]
    for c in rng.permutation(len(candidats)) if candidats else []:
        if distinctes(espace, w, candidats[int(c)], seuil):
            return candidats[int(c)]
    return None


def choisir_remplisseurs(espace, w, leurre, fams, rng, nombre, seuil, essais_max=None):
    """`nombre` lois de H d'une autre famille que w, distinctes entre elles, de w et du leurre (signature prédictive)."""
    essais_max = essais_max if essais_max is not None else 2000 * max(1, nombre)
    pris = []
    essais = 0
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


def tirer_mondes_avec_leurre(espace, fams, index, n, rng_ordre, rng_leurre_de, seuil, limite_ecartes):
    """n mondes tirés sans remise dans H parmi les lois qui ont un leurre apparié ; les lois écartées faute de leurre sont
    comptées et rapportées (jamais en silence) ; arrêt si plus de `limite_ecartes`."""
    mondes, leurres, ecartes = [], [], 0
    for w in rng_ordre.permutation(len(espace["lois"])):
        w = int(w)
        leurre = choisir_leurre(espace, w, fams, index, rng_leurre_de(w), seuil)
        if leurre is None:
            ecartes += 1
            if ecartes > limite_ecartes:
                raise Refus(f"plus de {limite_ecartes} lois sans leurre apparié : arrêt de P3")
            continue
        mondes.append(w)
        leurres.append(leurre)
        if len(mondes) == n:
            return mondes, leurres, ecartes
    raise Refus("pas assez de mondes avec un leurre apparié dans H : arrêt de P3")


# --- plan des positions -----------------------------------------------------------------------------------------------
def plan_positions(rng, n, K) -> np.ndarray:
    """Positions de la cible (forme vraie dans C, leurre dans B) pour l'ordre 1, réparties d'avance : n/K blocs, chacun une
    permutation de 0…K−1 tirée par la graine dérivée « p3/plan »."""
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
    """Garde : chaque bloc de K mondes est une permutation des positions ; chaque position (ordre 1 et ordre 2) apparaît
    exactement n/K fois."""
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
    """Panoramas appariés (indices de H, ordre 1) : C porte le monde à `position`, B le leurre ; le reste est identique."""
    if len(remplisseurs) != K - 1:
        raise Refus("nombre de remplisseurs ≠ K − 1")
    reste = list(remplisseurs)
    C = reste[:position] + [w] + reste[position:]
    B = reste[:position] + [leurre] + reste[position:]
    return {"C": C, "B": B, "position": int(position), "monde": int(w), "leurre": int(leurre)}


def presenter(indices, ordre):
    return list(indices) if ordre == 1 else list(reversed(indices)) if ordre == 2 else None


def exiger_panorama(pan, fams, K, espace=None, seuil=None) -> None:
    """Garde d'un panorama apparié : K candidats sans doublon ; la forme vraie dans C seulement, le leurre dans B
    seulement, à la même position ; C et B égaux ailleurs ; leurre de même famille et complexité que le monde ;
    remplisseurs d'une autre famille ; (si `espace`) leurre et remplisseurs distincts du monde (signature prédictive)."""
    C, B, p, w, l = pan["C"], pan["B"], pan["position"], pan["monde"], pan["leurre"]
    if len(C) != K or len(B) != K or len(set(C)) != K or len(set(B)) != K:
        raise Refus("panorama : taille ≠ K ou doublon")
    if not 0 <= p < K or C[p] != w or B[p] != l:
        raise Refus("panorama : cible absente de sa position")
    if w in B or l in C or l == w:
        raise Refus("panorama : forme vraie dans B ou leurre dans C (fuite ou appariement rompu)")
    if any(C[k] != B[k] for k in range(K) if k != p):
        raise Refus("panorama : C et B diffèrent hors de la position de la cible")
    if fams[l] != fams[w]:
        raise Refus(f"leurre non apparié : famille {fams[l]} ≠ {fams[w]}")
    if any(fams[C[k]] == fams[w] for k in range(K) if k != p):
        raise Refus("remplisseur de la famille du monde : la famille désignerait deux positions")
    if espace is not None:
        if not distinctes(espace, w, l, seuil):
            raise Refus("leurre non distinct du monde (signature prédictive)")
        if not all(distinctes(espace, w, C[k], seuil) for k in range(K) if k != p):
            raise Refus("remplisseur non distinct du monde (signature prédictive)")


# --- carte de reconnaissance sans aide ----------------------------------------------------------------------------------
CLES_ETAT_CARTE = ("K", "panorama")


class QuestionneurCarte:
    """Choisit une position du panorama présenté, avant toute question. `simule_verite` : factice qui simule une
    reconnaissance d'après une vérité donnée par le banc (déclaré, phase 0 seulement) ; jamais pour un proposeur réel."""
    nom = "abstrait"
    simule_verite = False

    def __init__(self, rng):
        self.rng = rng

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
    """Bras « choix au hasard » : position uniforme."""
    nom = "hasard"

    def choisir_carte(self, etat, verite=None):
        return int(self.rng.integers(etat["K"]))


class Reconnaisseur(QuestionneurCarte):
    """Avec probabilité ρ, choisit la forme vraie si elle est présente ; sinon position uniforme. Taux attendu dans C :
    ρ + (1 − ρ)/K ; dans B (cible = leurre) : 1/K ; écart ρ(1 − 1/K)."""
    nom = "reconnaisseur"
    simule_verite = True

    def __init__(self, rng, rho=1.0):
        super().__init__(rng)
        self.rho = float(rho)

    def choisir_carte(self, etat, verite=None):
        pv = verite["position_vraie"]
        if pv is not None and self.rng.random() < self.rho:
            return int(pv)
        return int(self.rng.integers(etat["K"]))


class Evitant(QuestionneurCarte):
    """Avec probabilité ρ, évite la forme vraie présente (position uniforme parmi les autres) ; sinon uniforme. Taux
    attendu dans C : (1 − ρ)/K ; écart −ρ/K."""
    nom = "evitant"
    simule_verite = True

    def __init__(self, rng, rho=1.0):
        super().__init__(rng)
        self.rho = float(rho)

    def choisir_carte(self, etat, verite=None):
        K, pv = etat["K"], verite["position_vraie"]
        if pv is not None and self.rng.random() < self.rho:
            autres = [k for k in range(K) if k != pv]
            return int(autres[int(self.rng.integers(len(autres)))])
        return int(self.rng.integers(K))


class Famille(QuestionneurCarte):
    """Artefact : connaît la famille du monde et choisit la position de cette famille dans le panorama (calculée sur les
    lois présentées). Dans C comme dans B, c'est la cible : sans leurre apparié, il passerait pour un reconnaisseur."""
    nom = "famille"
    simule_verite = True

    def choisir_carte(self, etat, verite=None):
        fm = tuple(verite["famille_monde"])
        for k, loi in enumerate(etat["panorama"]):
            if famille(loi) == fm:
                return k
        return int(self.rng.integers(etat["K"]))


def fabriquer_questionneur(spec, rng):
    """`spec` : « premier », « dernier », « hasard », « reconnaisseur:ρ », « evitant:ρ », « famille »."""
    nom, _, param = spec.partition(":")
    if nom == "premier":
        return Premier(rng)
    if nom == "dernier":
        return Dernier(rng)
    if nom == "hasard":
        return Hasard(rng)
    if nom == "famille":
        return Famille(rng)
    if nom in ("reconnaisseur", "evitant"):
        rho = float(param) if param else 1.0
        if not 0.0 <= rho <= 1.0:
            raise Refus(f"ρ hors de [0, 1] : {spec}")
        return (Reconnaisseur if nom == "reconnaisseur" else Evitant)(rng, rho)
    raise Refus(f"questionneur de carte inconnu : {spec!r}")


FACTICES_SIMULES = ("reconnaisseur", "evitant", "famille")


def jouer_carte(q, lois_presentees, verite, politique_refus="arret"):
    """Carte de reconnaissance SANS aide : l'état ne porte que K et le panorama (état non modifiable, lois copiées) ; aucun répondeur
    n'existe ; la vérité n'est passée qu'à un factice déclaré qui simule une reconnaissance. Rend (position, refusée)."""
    if politique_refus not in ("arret", "carte_perdue"):
        raise Refus(f"politique de refus inconnue : {politique_refus!r}")
    if q.simule_verite and q.nom not in FACTICES_SIMULES:
        raise Refus(f"questionneur « {q.nom} » qui lit la vérité sans être un factice déclaré : refus")
    K = len(lois_presentees)
    etat = MappingProxyType({"K": K, "panorama": tuple(copy.deepcopy(l) for l in lois_presentees)})
    if tuple(sorted(etat)) != tuple(sorted(CLES_ETAT_CARTE)):
        raise Refus("état de la carte avec une aide (clé hors liste)")
    k = q.choisir_carte(etat, verite if q.simule_verite else None)
    if isinstance(k, bool) or not isinstance(k, (int, np.integer)) or not 0 <= int(k) < K:
        if politique_refus == "arret":
            raise Refus(f"carte hors panorama : {k!r}")
        return None, True
    return int(k), False


# --- banc de reconnaissance ---------------------------------------------------------------------------------------------
def jouer_reconnaissance(espace, fams, panoramas, specs, rng_carte, K, politique_refus="arret"):
    """Pour chaque questionneur, chaque monde, chaque bras (C, B) et chaque ordre (1, 2) : position choisie, et si elle est
    la cible. Sortie par questionneur : tableaux (n × 2) `cible_C`, `cible_B`, `choix_C`, `choix_B` (positions
    présentées) et le nombre de refus."""
    sortie = {}
    for spec in specs:
        cC = np.zeros((len(panoramas), 2), dtype=int)
        cB = np.zeros_like(cC)
        chC = np.zeros_like(cC)
        chB = np.zeros_like(cC)
        refus = 0
        for i, pan in enumerate(panoramas):
            for j, ordre in enumerate((1, 2)):
                pos = position_presentee(pan["position"], ordre, K)
                for bras, cible, choix in (("C", cC, chC), ("B", cB, chB)):
                    indices = presenter(pan[bras], ordre)
                    lois = [espace["lois"][x] for x in indices]
                    verite = {"position_vraie": pos if bras == "C" else None,
                              "famille_monde": fams[pan["monde"]]}
                    q = fabriquer_questionneur(spec, rng_carte(spec, bras, ordre, i))
                    k, refusee = jouer_carte(q, lois, verite, politique_refus)
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
    """Règle gelée à trois issues (plus « non concluant ») sur l'intervalle [lo, hi] de l'écart D = taux C − taux B."""
    if lo > 0:
        return ISSUES[0]
    if hi < 0:
        return ISSUES[2]
    if -delta < lo and hi < delta:
        return ISSUES[1]
    return ISSUES[3]


def trois_issues(cible_C, cible_B, rng, tirages, niveau, delta, K) -> dict:
    """Écart apparié D = taux de la cible dans C − taux de la cible (leurre) dans B, moyenné par monde sur les deux ordres ;
    intervalle par rééchantillonnage des mondes (quantiles empiriques, « inverted_cdf ») au niveau gelé ; issue gelée.
    Rapporté aussi : taux dans C et dans B, et la « lecture sans leurre » (taux dans C contre 1/K seul)."""
    cC, cB = np.asarray(cible_C, dtype=float), np.asarray(cible_B, dtype=float)
    if cC.shape != cB.shape or cC.ndim != 2 or cC.shape[0] == 0:
        raise Refus("trois issues : tableaux non appariés")
    dw = (cC - cB).mean(axis=1)
    tC, tB = cC.mean(axis=1), cB.mean(axis=1)
    n = len(dw)
    idx = rng.integers(0, n, (tirages, n))
    d_b, c_b, b_b = dw[idx].mean(axis=1), tC[idx].mean(axis=1), tB[idx].mean(axis=1)
    ic_d, ic_c, ic_b = _ic(d_b, niveau), _ic(c_b, niveau), _ic(b_b, niveau)
    sans_leurre = issue(ic_c[0] - 1.0 / K, ic_c[1] - 1.0 / K, delta)
    return {"mondes": n, "ordres": int(cC.shape[1]), "niveau": niveau, "delta": delta,
            "ecart_D": {"point": float(dw.mean()), "ic": ic_d, "largeur": ic_d[1] - ic_d[0]},
            "taux_C": {"point": float(tC.mean()), "ic": ic_c}, "taux_B": {"point": float(tB.mean()), "ic": ic_b},
            "hasard_1_sur_K": 1.0 / K, "issue": issue(ic_d[0], ic_d[1], delta),
            "lecture_sans_leurre_taux_C_moins_1_sur_K": sans_leurre}


def biais_de_position(choix_C, choix_B, rng, tirages, niveau_position, K) -> dict:
    """Part des choix à chaque position présentée (C et B, deux ordres) ; biais vers la première (resp. dernière) position
    détecté si la borne basse de sa part, au niveau gelé, dépasse 1/K."""
    ch = np.concatenate([np.asarray(choix_C), np.asarray(choix_B)], axis=1)  # n × 4
    if np.any(ch < 0):
        raise Refus("biais de position : choix refusé présent")
    n = ch.shape[0]
    parts = np.stack([(ch == k).mean(axis=1) for k in range(K)], axis=1)  # n × K
    idx = rng.integers(0, n, (tirages, n))
    ic0 = _ic(parts[idx, 0].mean(axis=1), niveau_position)
    icd = _ic(parts[idx, K - 1].mean(axis=1), niveau_position)
    return {"parts_par_position": parts.mean(axis=0).tolist(), "ic_premiere": ic0, "ic_derniere": icd,
            "niveau": niveau_position, "premiere_detectee": ic0[0] > 1.0 / K, "derniere_detectee": icd[0] > 1.0 / K}


# --- attentes gelées des factices (validité de l'instrument) -------------------------------------------------------------
ATTENTES_FACTICES = {
    "hasard": {"issue": ISSUES[1], "premiere": False, "derniere": False},
    "premier": {"issue": ISSUES[1], "premiere": True, "derniere": False, "ecart_exactement_nul": True},
    "dernier": {"issue": ISSUES[1], "premiere": False, "derniere": True, "ecart_exactement_nul": True},
    "reconnaisseur:1": {"issue": ISSUES[0], "premiere": False, "derniere": False, "taux_C_exact": 1.0},
    "evitant:1": {"issue": ISSUES[2], "taux_C_exact": 0.0},
    "famille": {"issue": ISSUES[1], "ecart_exactement_nul": True, "taux_C_exact": 1.0, "sans_leurre": ISSUES[0]},
}


def conforme(spec, lecture, biais) -> dict:
    """Compare la lecture d'un factice à son attente gelée ; rend le détail et la conjonction."""
    att = ATTENTES_FACTICES[spec]
    d = {"issue": lecture["issue"] == att["issue"]}
    if "premiere" in att:
        d["premiere"] = biais["premiere_detectee"] == att["premiere"]
    if "derniere" in att:
        d["derniere"] = biais["derniere_detectee"] == att["derniere"]
    if att.get("ecart_exactement_nul"):
        d["ecart_exactement_nul"] = lecture["ecart_D"]["point"] == 0.0 and lecture["ecart_D"]["largeur"] == 0.0
    if "taux_C_exact" in att:
        d["taux_C_exact"] = lecture["taux_C"]["point"] == att["taux_C_exact"]
    if "sans_leurre" in att:
        d["sans_leurre"] = lecture["lecture_sans_leurre_taux_C_moins_1_sur_K"] == att["sans_leurre"]
    return {"attente": att, "detail": d, "tient": all(d.values())}


# --- recouvrement sur l'instrument de P1 (rapporté) ---------------------------------------------------------------------
def compatible(espace, c, w, questions) -> bool:
    """La loi c répond comme le monde w (répondeur exact) à toutes les questions posées (indices de prédicats)."""
    q = list(questions)
    return bool(np.all(espace["A"][c, q] == espace["A"][w, q])) if q else True


def cartes_avec_reconnaissance(espace, w, partie, carte_reconnue, points):
    """Carte d'un bras à panorama : la carte de reconnaissance tant qu'elle est compatible avec les réponses, sinon la
    carte commune de P1 (médoïde). `carte_reconnue` None : bras A (seul), carte de P1."""
    sortie = {}
    for t in points:
        c1 = partie["cartes"][t]["carte"]
        c = carte_reconnue if (carte_reconnue is not None
                               and compatible(espace, carte_reconnue, w, partie["posees_au_monde"][:t])) else c1
        sortie[t] = {"carte": int(c), "kl": qp.kl_vers(espace, w, c), "exacte": bool(c == w),
                     "reconnue_gardee": bool(carte_reconnue is not None and c == carte_reconnue)}
    return sortie


# --- calcul de puissance -----------------------------------------------------------------------------------------------
def _z(p):
    return NormalDist().inv_cdf(p)


def variance_ecart(p_c, p_b) -> float:
    """Variance d'une unité D = 1[C] − 1[B], indicatrices supposées indépendantes (une corrélation positive la réduit)."""
    return p_c * (1 - p_c) + p_b * (1 - p_b)


def taille_necessaire(K, delta, rho_min, rho_evitant, niveau, puissance) -> dict:
    """Nombre de mondes par questionneur pour que chaque issue soit rendue avec une probabilité au moins `puissance`
    quand elle est vraie, sous l'approximation normale de l'intervalle au niveau `niveau`, et sous une hypothèse prudente :
    les deux ordres d'un même monde parfaitement corrélés (l'unité est le monde, sans gain du doublement).
    - au niveau (D = 0, p_C = p_B = 1/K) : intervalle dans ]−δ, δ[ : n ≥ v0 · ((z_a + z_{(1+π)/2}) / δ)² ;
    - au-dessus (reconnaisseur ρ_min : D = ρ_min(1 − 1/K)) : borne basse > 0 : n ≥ v+ · ((z_a + z_π) / D+)² ;
    - en dessous (évitant ρ_e : D = −ρ_e/K) : borne haute < 0 : n ≥ v− · ((z_a + z_π) / |D−|)².
    Taille retenue : le maximum, arrondi au multiple de K supérieur (plan équilibré). Variante optimiste rapportée : deux
    ordres indépendants (n/2)."""
    if not (K >= 2 and 0 < delta < 1 and 0 < rho_min <= 1 and 0 < rho_evitant <= 1 and 0.5 < niveau < 1
            and 0.5 < puissance < 1):
        raise Refus("paramètres de puissance hors domaine")
    h = 1.0 / K
    za = _z(1 - (1 - niveau) / 2)
    d_plus, d_moins = rho_min * (1 - h), -rho_evitant * h
    if abs(d_moins) <= delta:
        raise Refus("l'écart « en dessous » visé ne dépasse pas la marge d'équivalence : issues non séparables")
    v0 = variance_ecart(h, h)
    vp = variance_ecart(h + d_plus, h)
    vm = variance_ecart(h + d_moins, h)
    n_niv = v0 * ((za + _z((1 + puissance) / 2)) / delta) ** 2
    n_plus = vp * ((za + _z(puissance)) / d_plus) ** 2
    n_moins = vm * ((za + _z(puissance)) / abs(d_moins)) ** 2
    brut = max(n_niv, n_plus, n_moins)
    retenu = int(math.ceil(math.ceil(brut) / K) * K)
    optimiste = int(math.ceil(math.ceil(brut / 2) / K) * K)
    return {"K": K, "hasard": h, "delta": delta, "niveau": niveau, "puissance": puissance, "z_niveau": za,
            "ecart_au_dessus": d_plus, "ecart_en_dessous": d_moins,
            "variances": {"au_niveau": v0, "au_dessus": vp, "en_dessous": vm},
            "n_par_issue": {"au_niveau": n_niv, "au_dessus": n_plus, "en_dessous": n_moins},
            "issue_qui_dimensionne": max((("au_niveau", n_niv), ("au_dessus", n_plus), ("en_dessous", n_moins)),
                                         key=lambda x: x[1])[0],
            "n_retenu_prudent": retenu, "n_optimiste_ordres_independants": optimiste}


def puissance_par_simulation(n, K, modele, rho, niveau, delta, rng, repetitions=400, ordres_correles=True):
    """Contrôle de l'approximation (essais seulement) : part des répétitions où la règle gelée rend chaque issue, pour un
    questionneur simulé (« hasard », « reconnaisseur », « evitant ») sur n mondes, intervalle normal au niveau gelé."""
    h = 1.0 / K
    p_c = {"hasard": h, "reconnaisseur": rho + (1 - rho) * h, "evitant": (1 - rho) * h}[modele]
    za = _z(1 - (1 - niveau) / 2)
    comptes = {i: 0 for i in ISSUES}
    m = 1 if ordres_correles else 2
    for _ in range(repetitions):
        c = (rng.random((n, m)) < p_c).astype(float)
        b = (rng.random((n, m)) < h).astype(float)
        dw = (c - b).mean(axis=1)
        se = dw.std(ddof=1) / math.sqrt(n)
        comptes[issue(dw.mean() - za * se, dw.mean() + za * se, delta)] += 1
    return {k: v / repetitions for k, v in comptes.items()}


# --- devis refait -----------------------------------------------------------------------------------------------------
def devis(n_mondes, prix_par_proposeur, appels_par_monde, reprises) -> dict:
    """Devis de la phase 1 sur la taille de la puissance : par proposeur, n_mondes × appels_par_monde appels (cartes de
    reconnaissance : 2 bras × 2 ordres) ; estimation au prix de chacun ; pire cas : tous les appels au plus haut prix,
    plus les reprises. Prix : coûts observés par appel de proposeur (unité différente : prix d'un appel de carte à relever)."""
    appels = {p: n_mondes * appels_par_monde for p in prix_par_proposeur}
    est = {p: round(appels[p] * prix_par_proposeur[p], 2) for p in prix_par_proposeur}
    total_appels = sum(appels.values())
    pire = round(total_appels * max(prix_par_proposeur.values()) * (1 + reprises), 2)
    return {"mondes_par_proposeur": n_mondes, "appels_par_monde_et_proposeur": appels_par_monde, "appels": appels,
            "appels_total": total_appels, "estimation_usd": est, "estimation_total_usd": round(sum(est.values()), 2),
            "pire_cas_usd": pire, "reprises": reprises}
