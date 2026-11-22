"""Pièce 5 — gardes G3, G4, G6, G7 (table des gardes du § 4 de la spécification).

- G3, oracle aveugle : l'oracle ne reçoit que les sorties de l'épisode, après que le harnais en a retiré, par
  comparaison exacte de chaînes, les trois textes d'étiquette du registre. Essai : la chaîne entière (masquage puis
  oracle) est appelée trois fois sur les mêmes sorties, le champ de condition du registre prenant tour à tour les trois
  étiquettes ; les trois Y doivent être égaux. Refus si une chaîne d'étiquette subsiste après masquage.
- G4, confusion : l'ordre de passage doit être celui que l'entropie révélée redonne ; sinon refus.
- G6, données manquantes : chaque épisode manquant compte Y = 1 dans la grandeur primaire (et Z = Y_S − Y_J avec cette
  valeur) ; le taux de manquants par condition et par organisme est rapporté ; aucun épisode n'est retiré ; un
  emplacement sans issue ni marque « manquant » est refusé.
- G7, secondaires : maximum conjoint des statistiques standardisées sur les mêmes permutations (Westfall et Young,
  pas unique) ; à défaut, Holm. Une secondaire lue seule sans correction est refusée.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .contraste_v1 import holm
from .erreurs_v1 import RefusConfusion, RefusManquant, RefusOracle, RefusSecondaire
from .permutation_v1 import TOLERANCE_RELATIVE, Tirages, verifier_issues
from .registre_v1 import CONDITIONS, Plan, tirer_ordre, verifier_entropie

# ---------------------------------------------------------------- G3


def masquer(sorties: str, etiquettes: dict) -> str:
    """Retire, par comparaison exacte de chaînes, les trois textes d'étiquette ; refuse s'il en subsiste un après."""
    if not isinstance(sorties, str):
        raise RefusOracle("sorties de l'épisode non textuelles")
    textes = sorted((etiquettes[c] for c in CONDITIONS), key=len, reverse=True)
    masque = sorties
    for t in textes:
        masque = masque.replace(t, "")
    for t in textes:
        if t in masque:
            raise RefusOracle(f"G3 : une chaîne d'étiquette subsiste dans l'entrée de l'oracle après masquage : {t!r}")
    return masque


class ChaineOracle:
    """Chaîne du harnais : masquage puis oracle. L'oracle ne reçoit que le texte masqué ; jamais l'enregistrement."""

    def __init__(self, oracle, etiquettes: dict):
        if not callable(oracle):
            raise RefusOracle("oracle non appelable")
        self.oracle = oracle
        self.etiquettes = dict(etiquettes)

    def __call__(self, sorties: str, enregistrement: dict) -> float:
        return float(self.oracle(masquer(sorties, self.etiquettes)))


def essai_trois_etiquettes(chaine, sorties: str, enregistrement: dict) -> float:
    """Appelle `chaine(sorties, enregistrement)` trois fois, le champ « condition » prenant E, D, U ; Y doit être égal."""
    if "condition" not in enregistrement:
        raise RefusOracle("enregistrement sans champ « condition »")
    ys = []
    for c in CONDITIONS:
        e = dict(enregistrement)
        e["condition"] = c
        ys.append(chaine(sorties, e))
    if not (ys[0] == ys[1] == ys[2]):
        raise RefusOracle(f"G3 : Y dépend du champ de condition du registre : {dict(zip(CONDITIONS, ys))}")
    return ys[0]


# ---------------------------------------------------------------- G4


def controler_ordre(plan: Plan, entropie_revelee) -> None:
    """G4 : l'ordre de passage du registre est-il celui du tirage ? Un ordre fixé à la main (U en dernier) est refusé."""
    verifier_entropie(entropie_revelee, "entropie révélée")
    o = np.asarray(plan.ordre)
    n = 3 * plan.k
    if o.ndim != 2 or o.shape != (plan.n_taches * n, 2):
        raise RefusConfusion("G4 : ordre de passage absent ou incomplet")
    if not np.array_equal(o, tirer_ordre(entropie_revelee, plan.n_taches, plan.k)):
        raise RefusConfusion("G4 : ordre de passage différent de l'ordre tiré (fixé à la main ou modifié)")


# ---------------------------------------------------------------- G6


@dataclass
class IssuesCompletees:
    Y: np.ndarray  # manquants comptés Y = 1
    taux_manquants: dict  # condition → taux


def completer_manquants(Y, manquant, conditions) -> IssuesCompletees:
    """G6 : un emplacement a une issue finie, ou la marque « manquant » (et alors pas d'issue) ; rien d'autre."""
    y = np.asarray(Y, dtype=np.float64)
    m = np.asarray(manquant)
    c = np.asarray(conditions)
    if m.dtype != bool or m.shape != y.shape or c.shape != y.shape:
        raise RefusManquant("G6 : marques « manquant » absentes ou de forme différente des issues")
    sans_rien = ~np.isfinite(y) & ~m
    if sans_rien.any():
        raise RefusManquant(f"G6 : {int(sans_rien.sum())} emplacement(s) sans issue ni marque « manquant »")
    incoherent = np.isfinite(y) & m
    if incoherent.any():
        raise RefusManquant(f"G6 : {int(incoherent.sum())} emplacement(s) marqué(s) « manquant » mais portant une issue")
    out = np.where(m, 1.0, y)
    taux = {CONDITIONS[i]: float(m[c == i].mean()) if np.any(c == i) else float("nan") for i in range(3)}
    return IssuesCompletees(out, taux)


def completer_paire(Y_S, m_S, Y_J, m_J, conditions) -> tuple[IssuesCompletees, IssuesCompletees, np.ndarray]:
    """G6 pour le contraste : Z = Y_S − Y_J avec la valeur 1 des manquants ; taux rapportés par organisme."""
    s = completer_manquants(Y_S, m_S, conditions)
    j = completer_manquants(Y_J, m_J, conditions)
    return s, j, s.Y - j.Y


# ---------------------------------------------------------------- G7

METHODES_CORRIGEES = ("maximum conjoint (Westfall et Young)", "Holm")


@dataclass(frozen=True)
class PSecondaire:
    nom: str
    valeur: float
    methode: str


def maximum_conjoint(secondaires: dict, tir: Tirages, statistiques: dict) -> dict:
    """Westfall et Young, pas unique : statistiques standardisées par leur loi de permutation (moyenne, écart type),
    valeur absolue, maximum sur la famille, sur les mêmes affectations.

    `secondaires` : nom → issues (n_t, 3k) ; `statistiques` : nom → fonction (Y, L, k) → (M,). La famille est celle
    que l'appelant passe ; aucune n'est ajoutée ni retirée ici (composition de la famille : point laissé ouvert).
    """
    if not secondaires or set(secondaires) != set(statistiques):
        raise RefusSecondaire("famille des secondaires vide ou statistiques non appariées aux grandeurs")
    obs, tirs = {}, {}
    for nom, y in secondaires.items():
        y = verifier_issues(y, tir, nom)
        f = statistiques[nom]
        t_obs = float(f(y, tir.observe[None], tir.k)[0])
        t_b = f(y, tir.affectations, tir.k)
        mu, sd = float(t_b.mean()), float(t_b.std())
        if sd <= 0:
            raise RefusSecondaire(f"G7 : statistique {nom!r} constante sous les permutations, non standardisable")
        obs[nom] = abs(t_obs - mu) / sd
        tirs[nom] = np.abs(t_b - mu) / sd
    maxi = np.max(np.stack(list(tirs.values())), axis=0)
    out = {}
    for nom, v in obs.items():
        nb = int(np.count_nonzero(maxi >= v - TOLERANCE_RELATIVE * max(1.0, v)))
        p = nb / maxi.shape[0] if tir.mode == "exact" else (1 + nb) / (maxi.shape[0] + 1)
        out[nom] = PSecondaire(nom, p, METHODES_CORRIGEES[0])
    return out


def holm_secondaires(p_brutes: dict) -> dict:
    return {n: PSecondaire(n, v, METHODES_CORRIGEES[1]) for n, v in holm(p_brutes).items()}


def lire_secondaire(p) -> float:
    """G7 : seule une p-valeur secondaire corrigée se lit ; un nombre nu ou une p non corrigée est refusé."""
    if not isinstance(p, PSecondaire) or p.methode not in METHODES_CORRIGEES:
        raise RefusSecondaire(f"G7 : secondaire lue seule sans correction : {p!r}")
    return p.valeur
