"""Idée 1.1 — banc et bras du préenregistrement scellé `prereg/organisme-idee-1-1-poids-du-nul-v2.md` (`3ffe1739…`).

Banc B v2 de l'idée 1.2 (archive A2, lois softmax aléatoires, lignes Q1 à Q7 et V1 à V5 à trois doses), plus les huit lignes
propres à ce texte (Q8, Q9a, Q9b, Hs, Hm, H7, Hg, Hn) ; 30 lignes, i_ligne de 0 à 29 dans l'ordre du texte (« Graines ») :
Q1 à Q7 ; V1 à V5, chaque type à ses trois doses croissantes ; Q8, Q9a, Q9b, Hs, Hm, H7, Hg, Hn.

Une répétition (classe `Repetition`) passe par les états construite → gelée → tirée → évaluée :
- **construite** : générateur `(i_ligne, r, 0)` : archive (S1, S2, U1 à U4, jA, s_A, s_B), paramètres de la ligne, 100
  instances d'entraînement, 100 uniformes de leurs issues, plan de 200 instances (dans cet ordre, « Répétitions ») ; les
  issues d'entraînement sont lues du monde par inversion de ces uniformes une fois le plan tiré (le monde de Q8 dépend du
  plan ; l'ordre des tirages du générateur est celui du texte) ;
- **gelée** : tous les engagements bâtis (J8, J9, La, Ld, engagement jumeau à 40 instants) par la fonction qui ne reçoit
  aucune issue fraîche ; pour une carte sans mémoire, toutes les projections et tous les certificats de J9-P et La-P
  calculés, et l'empreinte de leur journal écrite **avant** la création du générateur des issues fraîches ;
- **tirée** : issues fraîches du générateur `(i_ligne, r, 1)`, bloc par bloc ; sous gel de l'historique (lignes H), la
  projection du bloc b est calculée sur les seules issues des blocs < b et empreintée avant le tirage du bloc b ;
- **évaluée** : richesses de tous les bras sur les mêmes issues, gardes de la liste d'arrêt.

Les richesses sont calculées par le code du juge et du v9, appelé fonction par fonction (`selection_pari.trajectoires`,
`nul_filles_v2.valeurs_ajustees`, `nul_v9.detail_morceaux_groupe`) dans l'ordre de `nul_v9.evaluer_sur_issues`, sans
arrondi ; les gardes d'engagement et de tirages de `evaluer_v9` sont rejouées pour chaque bras (empreinte, lien des
tirages, plan d'exécution, issues). L'égalité, arrondie à six décimales, avec `nf.evaluer_v2` (J8) et `nul_v9.evaluer_v9`
(J9, La, Ld, jumeau) est éprouvée par les essais. Les membres communs (ordinaires, linéaire, log-linéaires) sont calculés
une fois et partagés entre bras, après vérification que leurs listes sont égales membre pour membre (la monotonie et le
nichage sont alors exacts, « Métrique »).
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
import time
from dataclasses import dataclass, field

import numpy as np

from ..gardes import GardeArret
from . import attaque_projection_extrait_v1 as AT
from . import lois_v1 as L
from . import projection_bras_v1 as PB
from . import projection_commun_v1 as cm
from . import projection_methodes_v1 as me

# --- constantes du texte -------------------------------------------------------------------------------------------------
EMPREINTE_PREREG = "3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff"
CHEMIN_PREREG = "prereg/organisme-idee-1-1-poids-du-nul-v2.md"
K, D = 3, 2
ALPHA = 0.05
SEUIL = math.log(1.0 / ALPHA)
N, ENTRAINEMENT, BLOC = 200, 100, 25
T8 = tuple(range(25, 201, 25))
T40 = tuple(range(5, 201, 5))
REPETITIONS = 1000
TOL_MONOTONIE = 1e-6
TOL_NICHAGE = 1e-6
SEUIL_ECART_RESIDUEL = 2e-3
DOSES = {"V1": (0.25, 0.50, 0.75), "V2": (0.4, 0.8, 1.2), "V3": (0.4, 0.8, 1.2), "V4": (0.1, 0.2, 0.3), "V5": (0.4, 0.8, 1.2)}
DOSE_Q8, DOSE_Q7, DOSE_Q9 = 0.6, 0.25, 0.50
ITERATIONS_Q8 = 600
SANS_REMISE_H = [70, 70, 70]
MG_HG = {"type": "moyenne_glissante", "nombre_issues": 3, "fenetre": 5, "lissage": 0.5}
MG_HN = {"type": "moyenne_glissante", "nombre_issues": 3, "fenetre": 200, "lissage": -70.0}
H7_GENRE, H7_PARAM, H7_PART = "contre_exces_du_bloc", 0.3, 1.0
ETA_A1 = 0.05
STRATE_REPETITIONS = 250
JOURNAL_ENTIER_REPETITIONS = 20
GROUPES = ("jumeau", "J9-Dc", "J9-P", "La-P", "strate")
REDUCTIONS = {1: "strate descriptive « sans membres log-linéaires » supprimée",
              2: "engagement jumeau (J9-D40, J9-D, J9-Dc) sur les 15 lignes V : 500 premières répétitions",
              3: "engagement jumeau (J9-D40, J9-D, J9-Dc) sur les 15 lignes V : 250 premières répétitions",
              4: "lignes Q9a et Q9b, bras à projection seulement (J9-P, La-P) : 500 premières répétitions",
              5: "La-P sur les 15 lignes V : 500 premières répétitions"}


def _lignes() -> tuple:
    lignes = [("Q1", None, None), ("Q2", None, None), ("Q3", None, None), ("Q4", None, None), ("Q5", None, None),
              ("Q6", None, None), ("Q7", None, None)]
    for genre in ("V1", "V2", "V3", "V4", "V5"):
        for d in DOSES[genre]:
            lignes.append((f"{genre}({d})", genre, d))
    lignes += [("Q8", None, None), ("Q9a", None, None), ("Q9b", None, None), ("Hs", None, None), ("Hm", None, None),
               ("H7", None, None), ("Hg", None, None), ("Hn", None, None)]
    return tuple(lignes)


LIGNES = _lignes()
NOMS = tuple(l[0] for l in LIGNES)
assert len(LIGNES) == 30
INDICE = {nom: i for i, nom in enumerate(NOMS)}
LIGNES_V = tuple(range(7, 22))
LIGNES_H = ("Hs", "Hm", "H7", "Hg", "Hn")
LIGNES_SANS_MEMOIRE = tuple(range(0, 25))


def actifs_pour(i_ligne: int, r: int, reductions=()) -> frozenset:
    """Groupes de bras joués à la répétition r de la ligne, après les réductions inscrites à l'addendum (règle du
    « Coût et durée », appliquée dans l'ordre 1 à 5 ; une réduction absente de la règle est refusée)."""
    reductions = tuple(reductions)
    if any(k not in REDUCTIONS for k in reductions) or list(reductions) != sorted(set(reductions)) or \
            list(reductions) != list(range(1, len(reductions) + 1)):
        raise GardeArret(f"réductions {reductions} hors de la règle écrite (dans l'ordre, chacune en entier) : run invalide")
    actifs = set(GROUPES)
    nom = NOMS[i_ligne]
    if 1 in reductions or not (i_ligne in LIGNES_V and r < STRATE_REPETITIONS):
        actifs.discard("strate")
    if i_ligne in LIGNES_V:
        borne = 250 if 3 in reductions else (500 if 2 in reductions else None)
        if borne is not None and r >= borne:
            actifs.discard("jumeau"); actifs.discard("J9-Dc")
        if 5 in reductions and r >= 500:
            actifs.discard("La-P")
    if nom in ("Q9a", "Q9b") and 4 in reductions and r >= 500:
        actifs.discard("J9-P"); actifs.discard("La-P")
    return frozenset(actifs)
# Membre « qui contient la copie », pour la quantité fatale de J9-D (lecture déclarée au rapport du développeur).
MEMBRE_DE_LA_COPIE = {"Q1": "ajuste_lineaire:archive", "Q2": "seuil:jA", "Q3": "morceaux:sous_population",
                      "Q4": "seuil:j", "Q5": "seuil:j", "Q9a": "archive:S1", "Q9b": "ajuste_lineaire:archive"}


# --- graines --------------------------------------------------------------------------------------------------------------
def racine_de(empreinte_hex: str) -> int:
    if len(empreinte_hex) != 64 or any(c not in "0123456789abcdef" for c in empreinte_hex):
        raise GardeArret(f"racine : empreinte sha256 hexadécimale attendue, reçu {empreinte_hex!r}")
    return int(empreinte_hex, 16)


def generateur(racine: int, *cle: int) -> np.random.Generator:
    if any((not isinstance(c, (int, np.integer))) or c < 0 for c in cle):
        raise GardeArret(f"clé de graine invalide {cle!r}")
    return np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=tuple(int(c) for c in cle)))


def etat_graine(racine: int, *cle: int) -> list[int]:
    return [int(x) for x in np.random.SeedSequence(entropy=racine, spawn_key=tuple(int(c) for c in cle)).generate_state(2)]


def empreinte_json(objet) -> str:
    return hashlib.sha256(json.dumps(objet, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


# --- cartes hors grammaire (H7) ------------------------------------------------------------------------------------------
@dataclass
class CarteMemoire:
    """Carte de la ligne H7, hors grammaire : `attaque_projection_extrait_v1.carte_a_memoire`, genre
    « contre_exces_du_bloc », paramètre 0,3, part 1. Elle lit l'historique du bloc (garde « refus » : refusée)."""
    genre: str = H7_GENRE
    param: float = H7_PARAM
    part: float = H7_PART
    lit_historique: bool = True

    def resume(self) -> dict:
        return {"hors_grammaire": "carte_a_memoire", "genre": self.genre, "param": self.param, "part": self.part}


# --- lois : vérifications du banc ----------------------------------------------------------------------------------------
def lit_historique(J, loi) -> bool:
    if isinstance(loi, CarteMemoire):
        return True
    return bool(J.sp.types_de_la_loi(loi) & set(J.sp.TYPES_LISANT_L_HISTORIQUE))


def verifier_moyenne_glissante(loi: dict, horizon: int = N) -> None:
    """`lissage` n'est pas contrôlé par `valider_loi` : le banc vérifie qu'aucun dénominateur (longueur + K·lissage) n'est
    nul pour une longueur de fenêtre de 0 à min(fenêtre, horizon − 1), avec ou sans gel, et que le lissage n'est pas nul."""
    k, w, lam = loi["nombre_issues"], loi["fenetre"], float(loi["lissage"])
    if lam == 0.0:
        raise GardeArret("moyenne_glissante à lissage nul : division par zéro possible (fenêtre vide) : refusée par le banc")
    for longueur in range(0, min(int(w), horizon - 1) + 1):
        if longueur + k * lam == 0.0:
            raise GardeArret(f"moyenne_glissante : dénominateur nul à la longueur {longueur} : refusée par le banc")


def _verifier_loi_du_banc(J, loi, quoi: str) -> None:
    J.sp.valider_loi(loi, K, D)
    for sous in _sous_lois(loi):
        if sous.get("type") == "moyenne_glissante":
            verifier_moyenne_glissante(sous)


def _sous_lois(loi):
    if not isinstance(loi, dict):
        return
    yield loi
    for cle in ("si", "sinon", "loi", "base", "defaut"):
        yield from _sous_lois(loi.get(cle))
    for cle in ("lois", "composantes"):
        s = loi.get(cle)
        if isinstance(s, dict):
            for v in s.values():
                yield from _sous_lois(v)
        elif isinstance(s, (list, tuple)):
            for v in s:
                yield from _sous_lois(v)


def probas_finies(p, quoi: str) -> np.ndarray:
    a = np.asarray(p, dtype=float)
    if not np.all(np.isfinite(a)) or np.any(a < 0) or not np.allclose(a.sum(axis=-1), 1.0, atol=1e-9):
        raise GardeArret(f"loi de carte non finie ou non normée ({quoi}) : arrêt ; défaut")
    return a


def proba_carte(J, loi, instance, historique, t, quoi: str) -> list:
    """Loi prédictive d'une carte de la grammaire ; une exception (division par zéro d'une `moyenne_glissante`) ou une
    valeur non finie arrête (liste d'arrêt)."""
    try:
        p = J.sp.proba(loi, instance, historique, t)
    except ZeroDivisionError as e:
        raise GardeArret(f"loi de carte : division par zéro ({quoi}, instant {t}) : arrêt ; défaut") from e
    probas_finies(p, f"{quoi}, instant {t}")
    return p


# --- archive, lignes ----------------------------------------------------------------------------------------------------
def construire_archive(rng: np.random.Generator) -> dict:
    S1, S2, U1, U2, U3, U4 = (L.softmax_aleatoire(rng) for _ in range(6))
    jA = int(rng.integers(0, 2))
    sA = L.coupure_archive(rng)
    sB = L.coupure_archive(rng)
    S3 = L.si_sinon_trait(jA, sA, U1, U2)
    S4 = L.si_sinon_trait(1 - jA, sB, U3, U4)
    return {"S1": S1, "S2": S2, "S3": S3, "S4": S4, "U": [U1, U2, U3, U4], "jA": jA, "sA": sA, "sB": sB,
            "cut": {jA: sA, 1 - jA: sB}}


def survivantes(archive: dict) -> dict:
    return {n: archive[n] for n in ("S1", "S2", "S3", "S4")}


def seuil_hors(rng: np.random.Generator, cut_j: float) -> float:
    """Q5 : s = ±U[0,3 ; 1,0] au centième, retiré tant que |s − cut(j)| < 0,3."""
    while True:
        s = round(float(rng.choice([-1, 1]) * rng.uniform(0.3, 1.0)), 2)
        if abs(s - cut_j) >= 0.3:
            return s


@dataclass
class Ligne:
    """Monde, carte et paramètres d'une ligne pour une répétition ; `monde` vaut None pour Q8 jusqu'au plan."""
    nom: str
    monde: dict | None
    carte: object
    params: dict = field(default_factory=dict)


def construire_ligne(nom: str, genre, dose, archive: dict, rng: np.random.Generator) -> Ligne:
    S1, S2, S3, S4 = archive["S1"], archive["S2"], archive["S3"], archive["S4"]
    jA, sA, sB = archive["jA"], archive["sA"], archive["sB"]
    W1, b1 = L.poids_de(S1)
    fixe_unif = copy.deepcopy(L.UNIFORME)
    if nom in ("Q1",):
        M = L.melange([S1, S2, S3, S4, fixe_unif], L.poids_dirichlet(rng, 5))
        return Ligne(nom, M, M, {"poids": M["poids"]})
    if nom == "Q2":
        M = L.si_sinon_trait(jA, sA, S1, S2)
        return Ligne(nom, M, M)
    if nom == "Q3":
        M = L.par_sous_population(S1, S2)
        return Ligne(nom, M, M)
    if nom == "Q4":
        j = int(rng.integers(0, 2))
        M = L.si_sinon_trait(j, 0.0, S1, S2)
        return Ligne(nom, M, M, {"j": j})
    if nom == "Q5":
        j = int(rng.integers(0, 2))
        s = seuil_hors(rng, archive["cut"][j])
        M = L.si_sinon_trait(j, s, S1, S2)
        return Ligne(nom, M, M, {"j": j, "s": s})
    if nom == "Q6":
        M = L.si_sinon_trait(jA, sA, L.si_sinon_trait(1 - jA, sB, S1, S2), L.si_sinon_trait(1 - jA, sB, S2, S1))
        return Ligne(nom, M, M)
    if nom == "Q7":
        delta = L.delta_centre(rng)
        M = L.si_sinon_trait(jA, sA, S1, S2)
        Q = L.si_sinon_trait(jA, sA, L.softmax(W1 + DOSE_Q7 * delta, b1), S2)
        return Ligne(nom, M, Q, {"delta": delta.tolist()})
    if genre is not None:
        comp = L.tirer_composante(genre, dose, archive, rng)
        M = comp.loi(1.0)
        return Ligne(nom, M, M, {"composante": comp.resume()})
    if nom == "Q8":
        delta = L.delta_centre(rng)
        Q = L.softmax(W1 + DOSE_Q8 * delta, b1)
        return Ligne(nom, None, Q, {"delta": delta.tolist()})
    if nom in ("Q9a", "Q9b"):
        delta = L.delta_centre(rng)
        M = L.softmax(W1 + DOSE_Q9 * delta, b1)
        if nom == "Q9a":
            Q = copy.deepcopy(S1)
        else:
            Q = L.melange([S1, S2, S3, S4, copy.deepcopy(L.UNIFORME)], L.poids_dirichlet(rng, 5))
        return Ligne(nom, M, Q, {"delta": delta.tolist()})
    if nom == "Hs":
        return Ligne(nom, copy.deepcopy(L.UNIFORME), {"type": "sans_remise", "composition": list(SANS_REMISE_H)})
    if nom == "Hm":
        M = L.melange([S1, S2], [0.5, 0.5])
        return Ligne(nom, M, L.melange([copy.deepcopy(M), {"type": "sans_remise", "composition": list(SANS_REMISE_H)}],
                                       [0.5, 0.5]))
    if nom == "Hg":
        M = L.melange([S1, S2], [0.5, 0.5])
        return Ligne(nom, M, L.melange([copy.deepcopy(M), dict(MG_HG)], [0.5, 0.5]))
    if nom == "Hn":
        return Ligne(nom, copy.deepcopy(L.UNIFORME), dict(MG_HN))
    if nom == "H7":
        return Ligne(nom, L.melange([S1, S2], [0.5, 0.5]), CarteMemoire())
    raise GardeArret(f"ligne inconnue {nom!r}")


def monde_q8(Lp: np.ndarray, Qp: np.ndarray, archive: dict) -> tuple[dict, dict]:
    """Q8 : projection d'information inverse de la carte sur la famille linéaire de l'archive, sur les 200 instances du
    plan (600 pas, comme `projection_globale`), écrite en `melange`([S1, S2, S3, S4, loi fixe]) à poids arrondis à six
    décimales et renormalisés. Rend (monde, détails). Le corps reprend `projeter_commun` jusqu'à `em_commun` pour lire
    (τ, v, u) ; l'égalité de la loi obtenue avec `projection_globale` est éprouvée par un essai."""
    Lb = Lp[None]
    Qb = Qp[None]
    cel = np.zeros((1, N), int)
    F, S_, J_, _ = Lb.shape
    a = np.transpose(Lb, (0, 1, 3, 2)).reshape(F, S_ * AT.K, J_)
    bb = np.broadcast_to(np.tile(np.eye(AT.K), (S_, 1))[None], (F, S_ * AT.K, AT.K))
    tau, v, u = AT.em_commun(a, bb, Qb.reshape(F, S_ * AT.K), np.repeat(cel, AT.K, axis=1), 1, ITERATIONS_Q8)
    w = np.concatenate([(1.0 - tau[0]) * v[0, 0], [tau[0]]])
    w = np.round(w, 6)
    if w.sum() <= 0:
        raise GardeArret("Q8 : poids du monde tous nuls après arrondi")
    w = w / w.sum()
    fixe = {"type": "fixe", "probas": [float(x) for x in u[0]]}
    monde = L.melange([archive["S1"], archive["S2"], archive["S3"], archive["S4"], fixe], [float(x) for x in w])
    return monde, {"tau": float(tau[0]), "v": v[0, 0].tolist(), "u": u[0].tolist(), "poids": monde["poids"]}


# --- partitions des nuls limités -----------------------------------------------------------------------------------------
def partitions_La(archive: dict) -> list:
    jA, sA, sB = archive["jA"], archive["sA"], archive["sB"]
    return [{"nom": f"seuil_fixe:z{jA}:{sA}", "partition": {"type": "seuil_fixe", "indice": jA, "seuil": sA}},
            {"nom": f"seuil_fixe:z{1 - jA}:{sB}", "partition": {"type": "seuil_fixe", "indice": 1 - jA, "seuil": sB}}]


def partitions_Ld(archive: dict) -> list:
    return partitions_La(archive) + [{"nom": "sous_population", "partition": {"type": "sous_population"}}] + [
        {"nom": f"signe:z{j}", "partition": {"type": "seuil_fixe", "indice": j, "seuil": 0.0}} for j in range(D)]


# --- évaluation détaillée (code du juge et du v9, sans arrondi) -------------------------------------------------------------
def gardes_d_evaluation(V, gele, tirages) -> tuple:
    """Gardes de `nul_v9.evaluer_v9` puis prélude de `evaluer_sur_issues`, recopiés dans leur ordre ; rend
    (engagement, issues, instances, instants, bibliothèque calibrée)."""
    sp, nf = V.J.sp, V.J.nf
    if V.J.outils.empreinte_objet(gele.engagement) != gele.empreinte:
        raise sp.EngagementModifie("le test a changé depuis son gel")
    if not isinstance(tirages, dict) or tirages.get("empreinte_engagement") != gele.empreinte:
        raise sp.TiragesNonLies("tirages sans lien avec l'empreinte de cet engagement")
    sp.verifier_plan_execution(gele, tirages, None)
    e = gele.engagement
    if e.get("fractions"):
        raise GardeArret("engagement avec `fractions` : arrêt ; défaut (pari plein seulement)")
    instants = e.get("instants_lecture")
    k, instances, issues = e["nombre_issues"], e["instances"], tirages.get("issues")
    if not isinstance(issues, list) or len(issues) != len(instances) or not all(
            isinstance(x, int) and not isinstance(x, bool) and 0 <= x < k for x in issues):
        raise sp.TiragesNonLies("issues absentes, mal formées ou en nombre différent du plan gelé")
    c = e.get("part_calibrage", 0)
    n = len(instances) - c
    if c != 0:
        raise GardeArret("part de calibrage non nulle : hors du montage du banc")
    if not instants or instants[-1] != n or instants != sorted(set(instants)) or instants[0] < 1:
        raise nf.InstantsInvalides("instants de lecture absents ou non conformes dans l'engagement")
    bibliotheque = sp.calibrer(e["bibliotheque"], issues[:c], instances[:c])
    return e, issues[c:], instances[c:], list(instants), bibliotheque


def separer(V, bibliotheque) -> tuple[list, list, list]:
    """(ordinaires, ajustés du nul des filles v2, membres par morceaux), comme `evaluer_sur_issues`."""
    types9 = V.v9.TYPES_AJUSTES_V9
    ordinaires = [m for m in bibliotheque if m["type"] not in types9]
    ajustes = [m for m in bibliotheque if m["type"] in types9]
    nf_aj = [m for m in ajustes if m["type"] in V.J.nf.TYPES_AJUSTES]
    morceaux = [m for m in ajustes if m["type"] == V.v9.TYPE_MORCEAUX]
    if len(nf_aj) + len(morceaux) != len(ajustes):
        raise GardeArret("membre ajusté inconnu")
    return ordinaires, nf_aj, morceaux


def details_morceaux(module, membres, cache, issues, instants) -> dict:
    """Détails des membres par morceaux (un lot par liste de lois connues), par la fonction du module donné
    (`nul_v9` ou `nul_limite_v1`) ; groupement comme `valeurs_ajustees_v9`."""
    groupes = {}
    for m in membres:
        groupes.setdefault(module.empreinte_objet(m["lois"]), []).append(m)
    sortie = {}
    for lot in groupes.values():
        sortie.update(module.detail_morceaux_groupe(lot, cache, issues, instants))
    return sortie


@dataclass
class Pieces:
    """Valeurs par membre d'un engagement, aux instants de lecture."""
    instants: list
    numerateur: list           # par pas (200)
    ordinaires: dict           # nom -> trajectoire par pas
    nf_ajustes: dict           # nom -> {t: valeur}
    morceaux: dict             # nom -> {t: détail}
    types: dict                # nom -> type

    def valeurs(self, t: int, atteinte: bool = False, exclure_types=(), exclure_noms=()) -> list[tuple[float, str]]:
        c = [(traj[t - 1], nom) for nom, traj in self.ordinaires.items()
             if self.types[nom] not in exclure_types and nom not in exclure_noms]
        c += [(v[t], nom) for nom, v in self.nf_ajustes.items() if self.types[nom] not in exclure_types and nom not in exclure_noms]
        if "ajuste_morceaux" not in exclure_types:
            c += [(d[t]["atteinte" if atteinte else "valeur"], nom) for nom, d in self.morceaux.items() if nom not in exclure_noms]
        return c

    def log_w(self, numerateur=None, **kw) -> tuple[list[float], list[str]]:
        num = self.numerateur if numerateur is None else numerateur
        lw, dom = [], []
        for t in self.instants:
            meilleur, nom = max(self.valeurs(t, **kw), key=lambda c: (c[0], c[1]))
            lw.append(float(num[t - 1] - meilleur))
            dom.append(nom)
        return lw, dom

    def ecart_residuel(self, t: int) -> float:
        return max([d[t]["ecart_residuel"] for d in self.morceaux.values()] or [0.0])


def pieces_communes(V, gele, tirages, cache=None) -> tuple[Pieces, object]:
    sp, nf = V.J.sp, V.J.nf
    e, issues, instances, instants, biblio = gardes_d_evaluation(V, gele, tirages)
    ordinaires, nf_aj, _ = separer(V, biblio)
    cache = cache or sp.Cache(issues, instances)
    num = sp.trajectoire_numerateur(e, issues, instances, cache)
    par_membre = sp.trajectoires(ordinaires, issues, instances, e["nombre_issues"], cache)
    par_aj = {m["nom"]: nf.valeurs_ajustees(m, cache, issues, e["nombre_issues"], instants) for m in nf_aj}
    types = {m["nom"]: m["type"] for m in biblio}
    return Pieces(instants, list(num), par_membre, par_aj, {}, types), cache


def membres_communs(V, gele) -> list:
    _, nf_aj, morceaux = separer(V, gele.engagement["bibliotheque"])
    return [m for m in gele.engagement["bibliotheque"] if m["type"] != V.v9.TYPE_MORCEAUX]


# --- répétition ---------------------------------------------------------------------------------------------------------
class _Uniformes:
    def __init__(self, u):
        self._u = iter(np.asarray(u, dtype=float).tolist())

    def random(self) -> float:
        return next(self._u)


def instances_dicts(Z, G) -> list[dict]:
    return [{"z": [float(a) for a in z], "g": int(gv)} for z, gv in zip(Z, G)]


def tirer_instances_np(rng, n):
    Z = np.round(rng.standard_normal((n, D)), 6)
    G = rng.integers(0, 2, size=n)
    return Z, G


class Repetition:
    """Une répétition d'une ligne : construite → gelée → tirée → évaluée (gardes de l'ordre du gel ici)."""

    def __init__(self, V, racine: int, i_ligne: int, r: int, *, reductions=(), actifs=None, cle: tuple | None = None,
                 archive_A0: bool = False):
        if not 0 <= i_ligne < len(LIGNES) or r < 0:
            raise GardeArret(f"répétition hors du banc : ligne {i_ligne}, r {r}")
        self.V, self.J = V, V.J
        self.racine, self.i, self.r = racine, i_ligne, r
        self.nom, genre, dose = LIGNES[i_ligne]
        self.ligne_h = self.nom in LIGNES_H
        self.temps: dict = {}
        t0 = time.perf_counter()
        self.cle = (i_ligne, r) if cle is None else tuple(int(c) for c in cle)
        if cle is not None and self.cle[0] not in (97, 98):
            raise GardeArret("clé d'essai : (97, k, …) ou (98, r) seulement (texte, « Graines »)")
        rng = generateur(racine, *self.cle, 0)
        self.archive = construire_archive(rng)
        self.archive_A0 = bool(archive_A0)
        self.ligne = construire_ligne(self.nom, genre, dose, self.archive, rng)
        Ze, Ge = tirer_instances_np(rng, ENTRAINEMENT)
        u_ent = rng.random(ENTRAINEMENT)
        Zp, Gp = tirer_instances_np(rng, N)
        self.Z, self.G = Zp, Gp
        self.plan = instances_dicts(Zp, Gp)
        self.entr = instances_dicts(Ze, Ge)
        sp = self.J.sp
        for nom in ("S1", "S2", "S3", "S4"):
            _verifier_loi_du_banc(self.J, self.archive[nom], f"archive {nom}")
            if lit_historique(self.J, self.archive[nom]):
                raise GardeArret("loi connue de l'archive qui lit l'historique (P6) : arrêt")
        self.Lp = np.stack([np.array([sp.proba(self.archive[n], x, [], t) for t, x in enumerate(self.plan)])
                            for n in ("S1", "S2", "S3", "S4")], axis=1)                     # (200, 4, 3)
        self.carte = self.ligne.carte
        self.lit_hist = lit_historique(self.J, self.carte)
        if not isinstance(self.carte, CarteMemoire):
            _verifier_loi_du_banc(self.J, self.carte, "carte")
        if self.nom == "Q8":
            Qp = np.array([proba_carte(self.J, self.carte, x, [], t, "carte Q8") for t, x in enumerate(self.plan)])
            self.ligne.monde, self.details_q8 = monde_q8(self.Lp, Qp, self.archive)
        self.monde = self.ligne.monde
        _verifier_loi_du_banc(self.J, self.monde, "monde")
        if lit_historique(self.J, self.monde):
            raise GardeArret("monde qui lit l'historique : hors du banc (mondes sans mémoire)")
        self.Mp = np.array([sp.proba(self.monde, x, [], t) for t, x in enumerate(self.plan)])
        src = _Uniformes(u_ent)
        y_ent = [sp.tirer_categorie(src, sp.proba(self.monde, x, [], 0)) for x in self.entr]
        self.q_ent = self.J.controles_pari._frequences(y_ent, K)
        self.cA = (Zp[:, self.archive["jA"]] > self.archive["sA"]).astype(int)
        self.cB = (Zp[:, 1 - self.archive["jA"]] > self.archive["sB"]).astype(int)
        self.c4 = 2 * self.cA + self.cB
        self.actifs = actifs_pour(i_ligne, r, reductions) if actifs is None else frozenset(actifs)
        self.strate = "strate" in self.actifs
        self.etat = "construite"
        self.flux: PB.FluxFrais | None = None
        self.flux_cree = False
        self.engagements: dict = {}
        self.enregistrement: dict = {"ligne": self.nom, "i_ligne": i_ligne, "r": r}
        self.temps["construction"] = time.perf_counter() - t0

    # --- bras joués sur la ligne ---
    @property
    def bras_engagements(self) -> tuple:
        if self.nom == "H7":
            return ()
        if self.ligne_h:
            return ("J9", "jumeau")
        return ("J8", "J9", "La", "Ld", "jumeau")

    # --- gel ---
    def _bibliotheque(self, quoi: str) -> list:
        sp, J, V = self.J.sp, self.J, self.V
        std = list(sp.BIBLIOTHEQUE_STANDARD) + [{"nom": "marginale_entrainement", "type": "fixe", "probas": self.q_ent}]
        surv = survivantes(self.archive)
        if self.archive_A0:
            # essai E0 : archive A0 = {S1, S2} (sans coupure), pour le nul ; La n'a alors aucune partition
            surv = {n: self.archive[n] for n in ("S1", "S2")}
            if quoi == "La":
                return std + V.limite.membres_archive_v9(dict(surv), None, K, D, partitions=[])
        if quoi == "J8":
            return std + J.nul_v8.membres_archive_v8(dict(surv), None, K, D)
        if quoi in ("J9", "jumeau"):
            return std + V.v9.membres_archive_v9(dict(surv), None, K, D)
        if quoi == "La":
            return std + V.limite.membres_archive_v9(dict(surv), None, K, D, partitions=partitions_La(self.archive))
        if quoi == "Ld":
            return std + V.limite.membres_archive_v9(dict(surv), None, K, D, partitions=partitions_Ld(self.archive))
        raise GardeArret(f"bibliothèque inconnue {quoi!r}")

    def construire_engagement(self, quoi: str):
        """Engagement gelé d'un bras. Ne reçoit aucune issue fraîche (appelée dans l'état « construite » seulement)."""
        if self.etat != "construite" or self.flux_cree:
            raise GardeArret("engagement bâti après la création du flux des issues fraîches : arrêt ; défaut")
        instants = list(T40 if quoi == "jumeau" else T8)
        if instants != list(self.J.cycle.instants_reguliers(N, len(instants))):
            raise GardeArret("instants de lecture ≠ instants réguliers du juge")
        e = self.J.nf.construire_engagement_v2("fiche", self.carte, self.plan, K, ALPHA, self._bibliotheque(quoi), 0, None,
                                               instants, plan_execution="ordre_naturel")
        if e.get("fractions"):
            raise GardeArret("engagement avec `fractions` : arrêt ; défaut (pari plein seulement)")
        return self.J.sp.geler_engagement(e)

    def geler(self) -> None:
        if self.etat != "construite" or self.flux_cree:
            raise GardeArret("gel demandé hors de l'état « construite »")
        t0 = time.perf_counter()
        for quoi in self.bras_engagements:
            self.engagements[quoi] = self.construire_engagement(quoi)
        self.empreintes_gel = {q: g.empreinte for q, g in self.engagements.items()}
        self.temps["engagements"] = time.perf_counter() - t0
        self.journal: dict = {}
        if not self.lit_hist:
            if self.ligne_h:
                raise GardeArret("ligne H sans carte qui lit l'historique")
            self.Qp = np.array([proba_carte(self.J, self.carte, x, [], t, "carte au gel") for t, x in enumerate(self.plan)])
            self._projeter_au_gel()
        else:
            if not self.ligne_h:
                raise GardeArret("carte qui lit l'historique hors des lignes H : hors du banc")
        self.enregistrement["empreintes_engagements"] = dict(self.empreintes_gel)
        self.enregistrement["journal_gel"] = {k: v for k, v in self.journal.items()}
        self.etat = "gelee"

    def _projeter_au_gel(self) -> None:
        """Carte sans mémoire : la garde accepte (forme « refus »), et toutes les projections de J9-P et de La-P sont
        calculées ici, avant tout tirage frais ; l'empreinte du journal est écrite dans l'enregistrement."""
        if self.flux_cree:
            raise PB.GardeAcces("projection d'une carte sans mémoire après la création du flux des issues fraîches : arrêt")
        PB.exiger_blocs_alignes()
        PB.exiger_garde(self.lit_hist, "refus", self.ligne_h)
        verifier_coupures(self)
        Qb = np.stack([self.Qp[a:e] for a, e in cm.BLOCS])
        self.Qb = Qb
        if "J9-P" in self.actifs:
            t0 = time.perf_counter()
            qj = {b: PB.questions_j9p(self.Z, self.G, b) for b in range(PB.NB)}
            self.proj_j9p = PB.projeter(self.Lp, Qb, qj, 2, range(PB.NB))
            self.journal["J9-P"] = [self.proj_j9p[b]["empreinte"] for b in range(PB.NB)]
            self.temps["projection_J9-P"] = time.perf_counter() - t0
        if "La-P" in self.actifs:
            t0 = time.perf_counter()
            ql = {b: PB.questions_lap(self.cA, self.cB, b) for b in range(PB.NB)}
            self.proj_lap = PB.projeter(self.Lp, Qb, ql, 2, range(PB.NB))
            self.journal["La-P"] = [self.proj_lap[b]["empreinte"] for b in range(PB.NB)]
            self.temps["projection_La-P"] = time.perf_counter() - t0

    # --- tirage ---
    def _tireur(self, rng):
        sp = self.J.sp

        def tirer(b):
            u = rng.random(BLOC)
            src = _Uniformes(u)
            ys = list(self.flux.issues)
            out = []
            a = BLOC * b
            for k_ in range(BLOC):
                t = a + k_
                y = sp.tirer_categorie(src, sp.proba(self.monde, self.plan[t], ys + out, t))
                out.append(int(y))
            return out
        return tirer

    def tirer(self) -> None:
        if self.etat != "gelee":
            raise GardeArret("issues fraîches demandées avant le gel de tous les engagements : arrêt ; défaut")
        for q, g in self.engagements.items():
            if g.empreinte != self.empreintes_gel[q] or self.J.outils.empreinte_objet(g.engagement) != g.empreinte:
                raise GardeArret(f"engagement {q} modifié après le gel")
        PB.exiger_blocs_alignes()
        self.flux_cree = True
        rng = generateur(self.racine, *self.cle, 1)
        self.flux = PB.FluxFrais(self._tireur(rng))
        t0 = time.perf_counter()
        if self.lit_hist:
            self.proj_gel: dict = {}
            self.Qg = np.zeros((N, K))
        for b in range(PB.NB):
            if self.lit_hist:
                self._projeter_sous_gel(b)
            self.flux.tirer_bloc(b)
        self.issues = self.flux.complet()
        self.temps["tirage_et_gel_par_bloc"] = time.perf_counter() - t0
        self.etat = "tiree"

    def carte_gelee_bloc(self, b: int, passe: list) -> np.ndarray:
        """q^G_s pour s du bloc b : la loi de la carte évaluée avec l'historique arrêté au début du bloc (lemme 4 :
        appel qui reçoit l'historique tronqué, jamais le `Cache`)."""
        a, e = cm.BLOCS[b]
        if len(passe) != a:
            raise PB.GardeAcces("carte gelée : historique de longueur ≠ issues des blocs passés")
        if isinstance(self.carte, CarteMemoire):
            # gele=True : la loi ne lit pas les issues (excès multiplié par 0) ; les 25 issues du bloc, inconnues, sont
            # remplacées par 0 (essai : mêmes lignes qu'avec les vraies issues).
            Qm = AT.carte_a_memoire(self.carte.genre, self.carte.param, self.carte.part, self.Mp[:e],
                                    np.array(list(passe) + [0] * (e - a), int), BLOC, True)
            return probas_finies(Qm[a:e], "carte H7 gelée")
        return np.array([proba_carte(self.J, self.carte, self.plan[t], list(passe), t, "carte gelée") for t in range(a, e)])

    def _projeter_sous_gel(self, b: int) -> None:
        PB.exiger_garde(self.lit_hist, "gel", self.ligne_h)
        passe = self.flux.passe(b)
        qg = self.carte_gelee_bloc(b, passe)
        a, e = cm.BLOCS[b]
        self.Qg[a:e] = qg
        Qb = np.zeros((PB.NB, PB.S, K))
        Qb[b] = qg
        proj = PB.projeter(self.Lp, Qb, {b: PB.questions_j9p(self.Z, self.G, b)}, 2, [b])
        self.proj_gel[b] = proj[b]
        self.journal.setdefault("J9-P-gel", []).append(proj[b]["empreinte"])
        self.enregistrement.setdefault("journal_gel_par_bloc", []).append(
            {"bloc": b, "issues_recues": len(passe), "empreinte": proj[b]["empreinte"]})

    # --- évaluation ---
    def tirages_de(self, quoi: str) -> dict:
        return {"empreinte_engagement": self.engagements[quoi].empreinte, "issues": list(self.issues),
                "plan_execution": "ordre_naturel"}

    def evaluer(self) -> dict:
        if self.etat != "tiree":
            raise GardeArret("évaluation avant les issues fraîches")
        rec = self.enregistrement
        rec["empreinte_issues"] = hashlib.sha256(json.dumps(self.issues).encode()).hexdigest()
        if self.nom == "H7":
            self._evaluer_h7(rec)
        elif self.ligne_h:
            self._evaluer_h(rec)
        else:
            self._evaluer_sans_memoire(rec)
        rec["temps_s"] = {k: round(v, 4) for k, v in self.temps.items()}
        self.etat = "evaluee"
        return rec

    # bras à maximum et jumeau
    def _pieces_j9(self):
        V = self.V
        t0 = time.perf_counter()
        P9, cache = pieces_communes(V, self.engagements["J9"], self.tirages_de("J9"))
        self.temps["communs_J8_J9"] = time.perf_counter() - t0
        t0 = time.perf_counter()
        _, _, morceaux = separer(V, self.engagements["J9"].engagement["bibliotheque"])
        P9.morceaux = details_morceaux(V.v9, morceaux, cache, P9_issues(self), T8)
        self.temps["morceaux_J9"] = time.perf_counter() - t0
        return P9, cache

    def _pieces_partagees(self, quoi: str, P9: Pieces, cache) -> Pieces:
        """Pièces d'un autre bras à huit instants : mêmes membres communs que J9 (vérifié), membres par morceaux
        calculés par le module de son nul. Les gardes d'évaluation sont rejouées sur son engagement et ses tirages."""
        V = self.V
        gele = self.engagements[quoi]
        e, issues, instances, instants, biblio = gardes_d_evaluation(V, gele, self.tirages_de(quoi))
        if e["loi"] != self.engagements["J9"].engagement["loi"] or instants != P9.instants or issues != P9_issues(self):
            raise GardeArret(f"{quoi} : carte, instants ou issues différents de J9")
        if membres_communs(V, gele) != membres_communs(V, self.engagements["J9"]):
            raise GardeArret(f"{quoi} : membres communs différents de ceux de J9 (partage interdit)")
        _, _, morceaux = separer(V, biblio)
        t0 = time.perf_counter()
        mod = V.limite if quoi in ("La", "Ld") else None
        det = details_morceaux(mod, morceaux, cache, issues, instants) if morceaux else {}
        self.temps[f"morceaux_{quoi}"] = time.perf_counter() - t0
        return Pieces(P9.instants, P9.numerateur, P9.ordinaires, P9.nf_ajustes, det, {m["nom"]: m["type"] for m in biblio})

    def _jumeau(self, P9: Pieces, cache, avec_dc: bool) -> dict:
        V, sp, nf = self.V, self.J.sp, self.J.nf
        t0 = time.perf_counter()
        gele = self.engagements["jumeau"]
        e, issues, instances, instants, biblio = gardes_d_evaluation(V, gele, self.tirages_de("jumeau"))
        if instants != [5 * (k + 1) for k in range(40)] or instants != list(self.J.cycle.instants_reguliers(N, 40)):
            raise GardeArret("engagement jumeau : instants de lecture ≠ T₄₀ = {5, 10, …, 200} (rejet par famille hors de T₄₀)")
        ordinaires, nf_aj, morceaux = separer(V, biblio)
        num = sp.trajectoire_numerateur(e, issues, instances, cache)
        par_membre = sp.trajectoires(ordinaires, issues, instances, K, cache)
        par_aj = {m["nom"]: nf.valeurs_ajustees(m, cache, issues, K, instants) for m in nf_aj}
        det = details_morceaux(V.v9, morceaux, cache, issues, instants)
        Pj = Pieces(instants, list(num), par_membre, par_aj, det, {m["nom"]: m["type"] for m in biblio})
        lw40, _ = Pj.log_w()
        self.temps["jumeau"] = time.perf_counter() - t0
        par_membre_rejet = {}
        for nom in list(par_membre) + list(par_aj) + list(det):
            vals = []
            for t in instants:
                if nom in par_membre:
                    vm = par_membre[nom][t - 1]
                elif nom in par_aj:
                    vm = par_aj[nom][t]
                else:
                    vm = det[nom][t]["valeur"]
                vals.append(float(num[t - 1] - vm))
            par_membre_rejet[nom] = vals
        out = {"log_w": lw40, "par_membre": par_membre_rejet, "pieces": Pj}
        if avec_dc:
            t0 = time.perf_counter()
            seuils = [m for m in morceaux if m["partition"].get("type") == "seuil"]
            dc = V.par_coupe.detail_morceaux_par_coupe(seuils, cache, issues, instants) if seuils else {}
            self.temps["J9-Dc"] = time.perf_counter() - t0
            fam = {nom: v for nom, v in par_membre_rejet.items() if not nom.startswith("morceaux:seuil:")}
            for m in seuils:
                j = m["partition"]["indice"]
                for c in np.sort(np.unique(self.Z[:, j])).tolist():
                    vals = []
                    for t in instants:
                        dd = dc[m["nom"]][t]
                        u = np.unique(self.Z[:t, j])
                        k_ = int(np.searchsorted(u, c, side="right"))
                        if len(dd["bornes_coupes"]) != len(u) + 1:
                            raise GardeArret("J9-Dc : nombre de coupes ≠ valeurs distinctes + 1")
                        vals.append(float(num[t - 1] - dd["bornes_coupes"][k_]))
                    fam[f"coupure:z{j}<={c!r}"] = vals
            out["familles_fines"] = fam
        return out

    def _bras_maximum(self, rec: dict, P9: Pieces, cache, avec_limites: bool) -> dict:
        lw9, dom9 = P9.log_w()
        lw9p, _ = P9.log_w(atteinte=True)
        sortie = {"J9": lw9, "J9+": lw9p}
        rec["J9"] = _resume(lw9, dom9)
        rec["J9+"] = {"promue": _promue(lw9p), "max": max(lw9p)}
        rec["ecart_residuel_J9"] = [P9.ecart_residuel(t) for t in T8]
        if avec_limites:
            P8 = self._pieces_partagees("J8", P9, cache)
            if P8.morceaux or any(t == "ajuste_morceaux" for t in P8.types.values()):
                raise GardeArret("J8 : bibliothèque avec membres par morceaux")
            lw8, dom8 = P8.log_w()
            rec["J8"] = _resume(lw8, dom8)
            sortie["J8"] = lw8
            for quoi in ("La", "Ld"):
                Pq = self._pieces_partagees(quoi, P9, cache)
                lwq, domq = Pq.log_w()
                rec[quoi] = _resume(lwq, domq)
                rec[f"ecart_residuel_{quoi}"] = [Pq.ecart_residuel(t) for t in T8]
                sortie[quoi] = lwq
                sortie[f"g_{quoi}"] = rec[f"ecart_residuel_{quoi}"]
                if self.strate and quoi == "La":
                    rec.setdefault("strate_sans_log", {})["La"] = _resume(*Pq.log_w(exclure_types=("ajuste_log",)))
            if self.strate:
                s = rec.setdefault("strate_sans_log", {})
                s["J8"] = _resume(*P9.log_w(exclure_types=("ajuste_morceaux", "ajuste_log")))
                s["J9"] = _resume(*P9.log_w(exclure_types=("ajuste_log",)))
            verifier_monotonie_et_nichage(sortie)
        return sortie

    def _bras_lecture(self, rec: dict, lw9: list, P9: Pieces, cache, avec_dc: bool) -> None:
        jm = self._jumeau(P9, cache, avec_dc)
        par = jm["par_membre"]
        d40, rejet_par_membre, dd = regle_j9d(lw9, jm["log_w"], par)
        rec["J9-D40"] = {"promue": d40, "max_40": max(jm["log_w"]), "log_w_40": jm["log_w"]}
        rec["J9-D"] = {"promue": dd, "rejet_par_membre": rejet_par_membre,
                       "membre_le_moins_rejete": min(par, key=lambda n: (max(par[n]), n))}
        rec["ED_ecart_T8"] = max(abs(jm["log_w"][T40.index(t)] - lw9[T8.index(t)]) for t in T8)
        cible = MEMBRE_DE_LA_COPIE.get(self.nom)
        if cible is not None:
            nom = self._nom_membre(cible)
            rec["J9-D"]["quantite_fatale"] = max(par[nom])
            rec["J9-D"]["membre_de_la_copie"] = nom
        if avec_dc and "familles_fines" in jm:
            fam = jm["familles_fines"]
            rec["J9-Dc"] = {"promue": regle_j9d(lw9, jm["log_w"], fam)[2], "familles": len(fam)}
        verifier_domination(_promue(lw9), d40, dd)

    def _nom_membre(self, cible: str) -> str:
        if cible == "seuil:jA":
            return f"morceaux:seuil:z{self.archive['jA']}"
        if cible == "seuil:j":
            return f"morceaux:seuil:z{self.ligne.params['j']}"
        return cible

    def _w_reste(self, P9: Pieces, num_par_pas: np.ndarray, exclure_log: bool = False) -> list:
        """log W^reste aux instants de T₈ : numérateur donné, dénominateur = maximum des membres du v9 privés des types
        `ajuste_lineaire` et `ajuste_morceaux` (membres ordinaires et log-linéaires)."""
        cum = np.cumsum(num_par_pas)
        excl = ("ajuste_lineaire", "ajuste_morceaux") + (("ajuste_log",) if exclure_log else ())
        return P9.log_w(numerateur=list(cum), exclure_types=excl)[0]

    def _bras_projection_sans_memoire(self, rec: dict, P9: Pieces) -> None:
        y = np.asarray(self.issues, int)
        ib = {b: y[a:e] for b, (a, e) in enumerate(cm.BLOCS)}
        # la carte au gel est bien la carte jugée par le juge (lemme 3 : sans mémoire) : essai sain à chaque répétition
        num_juge = np.diff(np.concatenate([[0.0], P9.numerateur]))
        lq = np.log(self.Qp[np.arange(N), y])
        if np.max(np.abs(lq - num_juge)) > 1e-12:
            raise GardeArret("carte acceptée par la garde mais sa loi au gel ≠ sa loi sur les issues (lit l'historique ?)")
        wr = self._w_reste(P9, lq)
        self.journal_entier = {}
        if "J9-P" in self.actifs:
            t0 = time.perf_counter()
            le = PB.valeurs_e(self.proj_j9p, self.Qb, ib)
            proc, noms = PB.processus_j9p(le, self.Z)
            verifier_familles_j9p(noms, self.Z)
            terme = terme_projete(proc)
            verifier_terme(le, self.Z, terme)
            lw = richesse_projection(wr, terme)
            k = int(np.argmin(proc[:, -1]))
            rec["J9-P"] = _resume_proj(lw, terme, wr, noms[int(np.argmin(proc[:, int(np.argmax(lw))]))])
            rec["journal_J9-P"] = PB.journal_resume(self.proj_j9p, proc, noms, k)
            rec["journal_J9-P"]["cout_retenu"] = PB.cout_famille(self.proj_j9p, self.Z, noms[k])
            if self.strate:
                wr0 = self._w_reste(P9, lq, exclure_log=True)
                rec.setdefault("strate_sans_log", {})["J9-P"] = {"promue": _promue(richesse_projection(wr0, terme))}
            self.temps["J9-P_valeurs"] = time.perf_counter() - t0
            if self.r < JOURNAL_ENTIER_REPETITIONS:
                self.journal_entier["J9-P"] = self.proj_j9p
        if "La-P" in self.actifs:
            t0 = time.perf_counter()
            verifier_coupures(self)
            le = PB.valeurs_e(self.proj_lap, self.Qb, ib)
            procl, noml = PB.processus_lap(le)
            terml = terme_projete(procl)
            lwl = richesse_projection(wr, terml)
            kl = int(np.argmin(procl[:, -1]))
            rec["La-P"] = _resume_proj(lwl, terml, wr, noml[int(np.argmin(procl[:, int(np.argmax(lwl))]))])
            rec["journal_La-P"] = PB.journal_resume(self.proj_lap, procl, noml, kl)
            rec["journal_La-P"]["cout_retenu"] = PB.cout_famille(self.proj_lap, self.Z, noml[kl])
            self.temps["La-P_valeurs"] = time.perf_counter() - t0
            if self.r < JOURNAL_ENTIER_REPETITIONS:
                self.journal_entier["La-P"] = self.proj_lap

    def _temoins(self, rec: dict) -> None:
        verifier_coupures(self)
        y = np.asarray(self.issues, int)
        m = {"L": self.Lp, "Q": self.Qp, "y": y, "c4": self.c4}
        t0 = time.perf_counter()
        a1 = me.a1_en_ligne(m, ETA_A1)
        self.temps["A1"] = time.perf_counter() - t0
        t0 = time.perf_counter()
        a2 = me.a2_moitie(m)
        self.temps["A2"] = time.perf_counter() - t0
        rec["A1"] = {"promue": _promue(list(a1)), "max": float(np.max(a1)), "log_w": [float(v) for v in a1]}
        rec["A2"] = {"promue": bool(a2[-1] >= SEUIL), "log_w_200": float(a2[-1])}
        for v in list(a1) + list(a2):
            if not math.isfinite(v):
                raise GardeArret("log W non fini (témoin) : arrêt du run")

    def _evaluer_sans_memoire(self, rec: dict) -> None:
        P9, cache = self._pieces_j9()
        sortie = self._bras_maximum(rec, P9, cache, avec_limites=True)
        if "jumeau" in self.actifs:
            self._bras_lecture(rec, sortie["J9"], P9, cache, avec_dc="J9-Dc" in self.actifs)
        self._bras_projection_sans_memoire(rec, P9)
        self._temoins(rec)
        if self.nom == "Q8":
            rec["monde_q8"] = self.details_q8

    def _projection_sur(self, Qreel: np.ndarray) -> tuple[dict, dict]:
        Qb = np.stack([Qreel[a:e] for a, e in cm.BLOCS])
        qj = {b: PB.questions_j9p(self.Z, self.G, b) for b in range(PB.NB)}
        return PB.projeter(self.Lp, Qb, qj, 2, range(PB.NB)), Qb

    def _bras_h(self, rec: dict, P9: Pieces | None, Qreel: np.ndarray, num_nu: np.ndarray) -> None:
        y = np.asarray(self.issues, int)
        ib = {b: y[a:e] for b, (a, e) in enumerate(cm.BLOCS)}
        # J9-P avec refus : la carte est refusée au gel (comptée « refusée », jamais promue)
        PB.exiger_garde(self.lit_hist, "refus", self.ligne_h)
        rec["J9-P-refus"] = {"refusee": bool(self.lit_hist), "promue": False}
        # J9-P sans garde (« nu ») : projection et certificat sur les lois que la carte a réalisées (artefact déclaré)
        PB.exiger_garde(self.lit_hist, "nu", self.ligne_h)
        t0 = time.perf_counter()
        proj_nu, Qb_nu = self._projection_sur(Qreel)
        le = PB.valeurs_e(proj_nu, Qb_nu, ib)
        proc, noms = PB.processus_j9p(le, self.Z)
        verifier_familles_j9p(noms, self.Z)
        terme_nu = terme_projete(proc)
        verifier_terme(le, self.Z, terme_nu)
        lin_nu = proc[0]
        self.temps["J9-P-nu"] = time.perf_counter() - t0
        # J9-P avec gel : projections déjà calculées bloc par bloc avant chaque tirage
        t0 = time.perf_counter()
        Qb_g = np.stack([self.Qg[a:e] for a, e in cm.BLOCS])
        le_g = PB.valeurs_e(self.proj_gel, Qb_g, ib)
        proc_g, noms_g = PB.processus_j9p(le_g, self.Z)
        verifier_familles_j9p(noms_g, self.Z)
        terme_g = terme_projete(proc_g)
        verifier_terme(le_g, self.Z, terme_g)
        self.temps["J9-P-gel_valeurs"] = time.perf_counter() - t0
        lq_g = np.log(np.maximum(self.Qg[np.arange(N), y], cm.PLANCHER))
        if P9 is not None:
            wr_nu = self._w_reste(P9, num_nu)
            wr_g = self._w_reste(P9, lq_g)
        else:
            wr_nu = self._w_reste_h7(num_nu)
            wr_g = self._w_reste_h7(lq_g)
        complet_nu = richesse_projection(wr_nu, terme_nu)
        complet_g = richesse_projection(wr_g, terme_g)
        rec["J9-P-nu"] = {"terme_projete": _resume_terme(terme_nu), "complet": _resume_terme(np.array(complet_nu)),
                          "lineaire_seul": _resume_terme(lin_nu)}
        rec["J9-P-gel"] = {"terme_projete": _resume_terme(terme_g), "complet": _resume_terme(np.array(complet_g))}
        rec["journal_J9-P-gel"] = PB.journal_resume(self.proj_gel, proc_g, noms_g, int(np.argmin(proc_g[:, -1])))
        if self.r < JOURNAL_ENTIER_REPETITIONS:
            self.journal_entier = {"J9-P-gel": self.proj_gel, "J9-P-nu": proj_nu}
        # témoin exact : rapport de vraisemblance de la carte au monde, aux mêmes instants
        lm = np.log(self.Mp[np.arange(N), y])
        lam = np.cumsum(num_nu - lm)[np.array(T8) - 1]
        rec["temoin_lambda"] = {"promue": _promue(lam.tolist()), "max": float(lam.max())}
        for v in complet_nu + complet_g + terme_nu.tolist() + terme_g.tolist():
            if not math.isfinite(v):
                raise GardeArret("log W non fini (bras à projection) : arrêt du run")

    def _w_reste_h7(self, num_par_pas: np.ndarray) -> list:
        """H7 (hors grammaire, pas d'engagement du juge) : W^reste calculé par le banc sur la bibliothèque du v9 privée
        des membres linéaire et par morceaux (membres ordinaires et log-linéaires, par le code du juge)."""
        sp, nf = self.J.sp, self.J.nf
        if not hasattr(self, "_pieces_h7"):
            biblio = self._bibliotheque("J9")
            gardes = [m for m in biblio if m["type"] not in ("ajuste_lineaire", "ajuste_morceaux")]
            cache = sp.Cache(self.issues, self.plan)
            ordinaires = [m for m in gardes if m["type"] not in self.V.v9.TYPES_AJUSTES_V9]
            logs = [m for m in gardes if m["type"] == "ajuste_log"]
            par = sp.trajectoires(ordinaires, self.issues, self.plan, K, cache)
            aj = {m["nom"]: nf.valeurs_ajustees(m, cache, self.issues, K, list(T8)) for m in logs}
            self._pieces_h7 = Pieces(list(T8), [0.0] * N, par, aj, {}, {m["nom"]: m["type"] for m in gardes})
        return self._pieces_h7.log_w(numerateur=list(np.cumsum(num_par_pas)))[0]

    def _evaluer_h(self, rec: dict) -> None:
        P9, cache = self._pieces_j9()
        lw9, dom9 = P9.log_w()
        rec["J9"] = _resume(lw9, dom9)
        rec["ecart_residuel_J9"] = [P9.ecart_residuel(t) for t in T8]
        if "jumeau" not in self.actifs:
            raise GardeArret("ligne H sans engagement jumeau : aucune réduction ne le permet")
        self._bras_lecture(rec, lw9, P9, cache, avec_dc=False)
        Qreel = probas_finies(np.array(cache.probas(self.carte)), "carte réalisée")
        num_nu = np.diff(np.concatenate([[0.0], P9.numerateur]))
        if np.max(np.abs(np.log(Qreel[np.arange(N), np.asarray(self.issues)]) - num_nu)) > 1e-12:
            raise GardeArret("numérateur du juge ≠ loi réalisée de la carte")
        self._bras_h(rec, P9, Qreel, num_nu)

    def _evaluer_h7(self, rec: dict) -> None:
        y = np.asarray(self.issues, int)
        Qreel = probas_finies(AT.carte_a_memoire(self.carte.genre, self.carte.param, self.carte.part, self.Mp, y, BLOC, False),
                              "carte H7 réalisée")
        num_nu = np.log(np.maximum(Qreel[np.arange(N), y], cm.PLANCHER))
        self._bras_h(rec, None, Qreel, num_nu)


def P9_issues(rep: Repetition) -> list:
    return list(rep.issues)


# --- résumés et gardes ----------------------------------------------------------------------------------------------------
def _promue(lw) -> bool:
    return bool(any(v >= SEUIL for v in lw))


def _resume(lw, dom) -> dict:
    for v in lw:
        if not math.isfinite(v):
            raise GardeArret("log W non fini : arrêt du run entier ; aucune lecture partielle")
    i = int(np.argmax(lw))
    return {"promue": _promue(lw), "max": float(max(lw)), "log_w": [float(v) for v in lw], "decide": dom[i]}


def _resume_terme(terme: np.ndarray) -> dict:
    t = [float(v) for v in np.asarray(terme)]
    return {"promue": _promue(t), "max": max(t), "log_w": t}


def _resume_proj(lw, terme, wr, famille) -> dict:
    r = _resume(lw, ["?"] * len(lw))
    r["decide"] = famille if float(np.asarray(terme)[int(np.argmax(lw))]) <= float(wr[int(np.argmax(lw))]) else "W_reste"
    r["terme_projete_max"] = float(np.max(terme))
    r["w_reste_max"] = float(np.max(wr))
    return r


def verifier_monotonie_et_nichage(s: dict) -> None:
    """Liste d'arrêt : monotonie (J9, La, Ld ≤ J8 + 10⁻⁶) et nichage (La, Ld ≥ J9 − g − 10⁻⁶ ; Ld ≤ La + g^La + 10⁻⁶)."""
    for k in range(len(T8)):
        for q in ("J9", "La", "Ld"):
            if s[q][k] > s["J8"][k] + TOL_MONOTONIE:
                raise GardeArret(f"monotonie violée : log W de {q} > log W de J8 + 10⁻⁶ à t = {T8[k]} : arrêt ; défaut de code")
        for q in ("La", "Ld"):
            if s[q][k] < s["J9"][k] - s[f"g_{q}"][k] - TOL_NICHAGE:
                raise GardeArret(f"nichage violé : log W de {q} < log W de J9 − écart résiduel − 10⁻⁶ à t = {T8[k]} : arrêt")
        if s["Ld"][k] > s["La"][k] + s["g_La"][k] + TOL_NICHAGE:
            raise GardeArret(f"nichage violé : log W de Ld > log W de La + écart résiduel + 10⁻⁶ à t = {T8[k]} : arrêt")


def regle_j9d(lw9, lw40, par_membre: dict) -> tuple[bool, bool, bool]:
    """(J9-D40, règle par membre, J9-D). J9-D40 : J9 promeut, ou ∃ t ∈ T₄₀ : log W⁽⁴⁰⁾_t ≥ log(1/α). Règle par membre :
    pour chaque membre m, ∃ t_m ∈ T₄₀ : log q(y_1..t_m) − V_m(t_m) ≥ log(1/α). J9-D : J9-D40 ou la règle par membre
    (réunion ; les deux engagements ont des solveurs différents)."""
    d40 = _promue(lw9) or _promue(lw40)
    par = all(max(v) >= SEUIL for v in par_membre.values())
    return d40, par, d40 or par


def terme_projete(proc: np.ndarray) -> np.ndarray:
    """Terme projeté : minimum, sur les familles, des processus de blocs (min_F Σ_b log e_{F,b})."""
    return np.asarray(proc).min(0)


def richesse_projection(w_reste, terme) -> list:
    """log W_t = min(log W^reste_t ; terme projeté_t)."""
    return np.minimum(np.asarray(w_reste, dtype=float), np.asarray(terme, dtype=float)).tolist()


def verifier_terme(loge: dict, Z: np.ndarray, terme) -> None:
    """Seconde écriture du terme projeté, famille par famille, par une boucle indépendante de `processus_j9p`."""
    nb = PB.NB
    lin = [float(loge[b][0]) for b in range(nb)]
    sp_ = [float(loge[b][1]) for b in range(nb)]
    cum = lambda xs: list(np.cumsum(xs))
    best = [min(a, b) for a, b in zip(cum(lin), cum(sp_))]
    for j in range(D):
        for c in np.unique(Z[:, j]).tolist():
            par_bloc = []
            for b, (a, e) in enumerate(cm.BLOCS):
                i = int(np.sum(Z[a:e, j] <= c))
                par_bloc.append(lin[b] if i in (0, 25) else float(loge[b][2 + 24 * j + i - 1]))
            best = [min(x, y) for x, y in zip(best, cum(par_bloc))]
    if np.max(np.abs(np.asarray(best) - np.asarray(terme))) > 1e-9:
        raise GardeArret("terme projeté ≠ seconde écriture (minimum sur les familles) : arrêt ; défaut de code")


def verifier_familles_j9p(noms: list, Z: np.ndarray) -> None:
    """La liste des familles de J9-P est celle du texte : linéaire, sous-population, chaque valeur distincte de chaque trait
    du plan (au plus 402) ; elle ne dépend que du plan gelé."""
    attendus = ["lineaire", "sous_population"] + [f"coupure:z{j}<={c!r}" for j in range(D) for c in np.sort(np.unique(Z[:, j])).tolist()]
    if list(noms) != attendus:
        raise GardeArret("familles de J9-P ≠ liste du texte (linéaire, sous-population, coupures du plan) : arrêt ; défaut")


def verifier_coupures(rep) -> None:
    """Coupures de l'archive (La-P, A1, A2) calculées sur l'archive et le plan seuls, jamais sur des issues fraîches."""
    a = rep.archive
    cA = (rep.Z[:, a["jA"]] > a["sA"]).astype(int)
    cB = (rep.Z[:, 1 - a["jA"]] > a["sB"]).astype(int)
    if not (np.array_equal(cA, rep.cA) and np.array_equal(cB, rep.cB) and np.array_equal(2 * cA + cB, rep.c4)):
        raise GardeArret("coupures de l'archive ≠ coupures recalculées sur l'archive et le plan : arrêt ; défaut")


def verifier_domination(j9: bool, d40: bool, dd: bool) -> None:
    if j9 and not (d40 and dd):
        raise GardeArret("domination violée : J9 promeut et J9-D40 ou J9-D ne promeut pas : arrêt ; défaut de code")
    if d40 and not dd:
        raise GardeArret("domination violée : J9-D40 promeut et J9-D ne promeut pas : arrêt ; défaut de code")


def jouer_repetition(V, racine: int, i_ligne: int, r: int, *, reductions=(), cle=None, actifs=None) -> tuple[dict, object]:
    """construite → gelée → tirée → évaluée ; rend (enregistrement, répétition)."""
    rep = Repetition(V, racine, i_ligne, r, reductions=reductions, cle=cle, actifs=actifs)
    ordre_du_jeu(rep)
    return rep.evaluer(), rep


def ordre_du_jeu(rep: Repetition) -> None:
    """Ordre gelé : tous les engagements (et journaux) d'abord, les issues fraîches ensuite."""
    rep.geler()
    rep.tirer()


def evaluer_projection_seule(rep: Repetition) -> dict:
    """Après gel et tirage : bras à projection seuls (pour les comptes de l'étape 0 et le banc de mutations), sans les
    membres par morceaux ni l'engagement jumeau. Lignes sans mémoire : J9-P et La-P complets (W^reste par les membres
    communs du juge) ; lignes H : terme projeté sans garde et sous gel, sur toutes les familles et sur la famille linéaire
    seule."""
    if rep.etat != "tiree":
        raise GardeArret("évaluation avant les issues fraîches")
    y = np.asarray(rep.issues, int)
    ib = {b: y[a:e] for b, (a, e) in enumerate(cm.BLOCS)}
    out = {"ligne": rep.nom, "cle": list(rep.cle)}
    if not rep.ligne_h:
        P9, _ = pieces_communes(rep.V, rep.engagements["J9"], rep.tirages_de("J9"))
        lq = np.log(rep.Qp[np.arange(N), y])
        wr = rep._w_reste(P9, lq)
        le = PB.valeurs_e(rep.proj_j9p, rep.Qb, ib)
        proc, noms = PB.processus_j9p(le, rep.Z)
        verifier_familles_j9p(noms, rep.Z)
        terme = terme_projete(proc)
        verifier_terme(le, rep.Z, terme)
        lw = richesse_projection(wr, terme)
        out["J9-P"] = {"promue": _promue(lw), "max": max(lw), "terme_max": float(np.max(terme))}
        le = PB.valeurs_e(rep.proj_lap, rep.Qb, ib)
        procl, _ = PB.processus_lap(le)
        lwl = richesse_projection(wr, terme_projete(procl))
        out["La-P"] = {"promue": _promue(lwl), "max": max(lwl)}
        return out
    if rep.nom == "H7":
        Qreel = AT.carte_a_memoire(rep.carte.genre, rep.carte.param, rep.carte.part, rep.Mp, y, BLOC, False)
    else:
        cache = rep.J.sp.Cache(rep.issues, rep.plan)
        Qreel = np.array(cache.probas(rep.carte))
    proj_nu, Qb_nu = rep._projection_sur(probas_finies(Qreel, "carte réalisée"))
    le = PB.valeurs_e(proj_nu, Qb_nu, ib)
    proc, noms = PB.processus_j9p(le, rep.Z)
    verifier_familles_j9p(noms, rep.Z)
    Qb_g = np.stack([rep.Qg[a:e] for a, e in cm.BLOCS])
    le_g = PB.valeurs_e(rep.proj_gel, Qb_g, ib)
    proc_g, _ = PB.processus_j9p(le_g, rep.Z)
    tn, tg = terme_projete(proc), terme_projete(proc_g)
    verifier_terme(le, rep.Z, tn)
    verifier_terme(le_g, rep.Z, tg)
    out["sans_garde"] = {"terme": _promue(tn.tolist()), "lineaire": _promue(proc[0].tolist())}
    out["gel"] = {"terme": _promue(tg.tolist()), "lineaire": _promue(proc_g[0].tolist())}
    return out


def jouer_projection_seule(V, racine: int, i_ligne: int, cle: tuple) -> dict:
    rep = Repetition(V, racine, i_ligne, 0, cle=cle, actifs=("J9-P", "La-P"))
    ordre_du_jeu(rep)
    return evaluer_projection_seule(rep)
