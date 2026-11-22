"""La table du seuil, en instrument (rang 7 ; section 4).

Entrées : seuil toléré K, régime, q, L, niveau, budget d'étiquettes ; en régime d'excès, d0, m et l'horizon.

Signature : p = (1 − α^(1/(K − L)))/q, α = 1 − niveau. p est le taux exigé du **plancher**, la part indépendante du
score ; la part d'enjeu ne s'y ajoute qu'au type d'enjeu le plus bas (β·s_min/s̄), la part de soupçon jamais. Si p
dépasse le taux de plancher que permet le budget d'étiquettes (budget ÷ épisodes de l'horizon), ou si p > 1, la sortie
porte la phrase exacte « le plancher n'y sert pas de garantie », sans écrêtage. Elle rend aussi (K − L)·p·q, le nombre
moyen d'étiquettes reconnues parmi les K − L premiers endommagés.

Excès : l'outil refuse de rendre un taux pour un K et écrit « aucun seuil fixe garanti » ; il rend le nombre
d'épisodes en excès non vus à puissance un demi (approximation normale, test à horizon fixe au niveau 1 %), et la
déclaration m, n et source de validité.
"""
from __future__ import annotations

import math

from scipy import stats

from ..gardes import GardeArret
from .estimateurs import borne_haute_cp
from .regle_audit import RegleAudit

PHRASE_PAS_GARANTIE = "le plancher n'y sert pas de garantie"
PHRASE_EXCES = "aucun seuil fixe garanti"
MARQUE_APPROX = ("approximation normale, test à horizon fixe au niveau 1 % : ordre de grandeur, non la puissance du "
                 "pari de l'alerte")


def table_signature(K: int, q: float, L: int, niveau: float = 0.95, budget_etiquettes: float | None = None,
                    horizon: int | None = None, regle: RegleAudit | None = None, s_min: float | None = None) -> dict:
    if regle is not None:
        regle.exiger_borne()
    if not (0 < q <= 1):
        raise GardeArret("table du seuil : q hors de ]0, 1] (q = 0 refusé)")
    if int(K) != K or int(L) != L or L < 0 or K <= 0:
        raise GardeArret("table du seuil : K et L entiers, K > 0, L ≥ 0")
    if L >= K:
        raise GardeArret("table du seuil : L ≥ K refusé (le délai consomme tout le seuil)")
    if not (0 < niveau < 1):
        raise GardeArret("table du seuil : niveau hors de ]0, 1[")
    if (budget_etiquettes is None) != (horizon is None):
        raise GardeArret("table du seuil : budget d'étiquettes et horizon vont ensemble")
    alpha = 1.0 - niveau
    p = (1.0 - alpha ** (1.0 / (K - L))) / q
    sortie = {"regime": "signature", "K": K, "q": q, "L": L, "niveau": niveau, "p": p,
              "etiquettes_moyennes": (K - L) * p * q, "phrase": None}
    pas_garantie = p > 1
    if budget_etiquettes is not None:
        if horizon <= 0 or budget_etiquettes < 0:
            raise GardeArret("table du seuil : budget et horizon positifs")
        sortie["plancher_permis"] = budget_etiquettes / horizon
        pas_garantie = pas_garantie or p > sortie["plancher_permis"]
    if pas_garantie:
        sortie["phrase"] = PHRASE_PAS_GARANTIE
    if regle is not None and s_min is not None:
        sortie["part_enjeu_au_type_le_plus_bas"] = regle.beta * s_min / regle.s_bar
        sortie["taux_independant_du_score_au_type_le_plus_bas"] = regle.pi_min + regle.beta * s_min / regle.s_bar
    return sortie


def table_exces(d0: float, horizon: int, pi_min: float, m: int | None = None, K: int | None = None,
                regle: RegleAudit | None = None, alpha_reference: float = 0.05) -> dict:
    if regle is not None:
        regle.exiger_borne()
    if K is not None:
        raise GardeArret(f"table du seuil, régime d'excès : un taux pour un K est refusé — {PHRASE_EXCES}")
    if not (0 < d0 < 1) or horizon <= 0 or not (0 < pi_min <= 1):
        raise GardeArret("table du seuil, excès : d0 dans ]0, 1[, horizon > 0, π_min dans ]0, 1]")
    z = float(stats.norm.ppf(0.99))
    N = horizon
    if m is None:
        non_vus = z * math.sqrt(d0 * (1 - d0) * N / pi_min)
        decl = {"m": None, "n": N, "source": "d0 déclaré (monde planté)"}
        jamais_vu = None
    else:
        if m <= 0:
            raise GardeArret("table du seuil, excès : m > 0")
        non_vus = N * z * math.sqrt(d0 * (1 - d0) * (1.0 / (N * pi_min) + 1.0 / m))
        x = round(d0 * m)
        jamais_vu = borne_haute_cp(x, m, alpha_reference / 2) - x / m
        decl = {"m": m, "n": N, "source": f"d0 estimé sur m = {m} épisodes de référence"}
    return {"regime": "exces", "phrase": PHRASE_EXCES, "episodes_en_exces_non_vus": non_vus,
            "marque": MARQUE_APPROX, "declaration": decl, "exces_jamais_vu": jamais_vu}
