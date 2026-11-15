"""Vérificateur du texte (v2, majeur 3 de la contre-lecture du code `36ecc4a4…`) : constantes **tirées du texte scellé**
(`bdabf2bc…`), jamais du moteur, et troisième écriture des sept bras, de la valeur e et de la règle e-BH.

- `exiger_constantes_du_texte()` : chaque constante du moteur (`rejeu_v1`, `banc_tirages_repartis_v1`,
  `synthetique_v1`, `lire_banc_tirages_repartis_v1`) doit égaler celle du texte ; sinon `GardeArret`. Une mutation qui
  change une constante partagée par le moteur et par le vérificateur v1 (seuil d'arrêt bas à 1/10, par exemple) est vue
  ici.
- `allocation_du_texte(nom, lw, positions, racine, f, g)` : allocation de chaque bras écrite bloc par bloc à partir de la
  seule section « Bras » ([T] l. 430-447) et des seuils du texte ([T] l. 325-327).
- `verifier_generation(r, racine)` : sur le résultat d'une génération jouée (`execution_v1._tache_jeu`), refait pour
  chaque bras l'allocation, la valeur e de chaque carte et les promotions e-BH ; tout écart lève `GardeArret` dont le
  message ne porte ni allocation ni valeur (mineur 9).
"""
from __future__ import annotations

import math

import numpy as np

from ..gardes import GardeArret

# --- constantes du texte scellé ([T] l. 279-284, 325-327, 432-445, 306-316, 294, 302) ---------------------------------
M_TEXTE, ALPHA_TEXTE = 24, 0.05
BLOC_TEXTE, PLAFOND_TIRAGES_TEXTE, PART_TIRAGES_TEXTE, F125_TIRAGES_TEXTE = 25, 800, 200, 250
INSTANTS_TEXTE = tuple(range(25, 801, 25))
NB_TEXTE = PLAFOND_TIRAGES_TEXTE // BLOC_TEXTE                 # 32 blocs
PART_BLOCS_TEXTE = PART_TIRAGES_TEXTE // BLOC_TEXTE            # 8 blocs
F125_BLOCS_TEXTE = F125_TIRAGES_TEXTE // BLOC_TEXTE            # 10 blocs
BUDGET_TIRAGES_TEXTE, BUDGET_F125_TIRAGES_TEXTE = 4800, 6000
SEUIL_BAS_TEXTE = math.log(1 / 20)                             # arrêt bas : log W < log(1/20)
TIRAGES_MIN_ARRET_BAS_TEXTE = 50                               # « après au moins 50 tirages »
SEUIL_HAUT_TEXTE = math.log(24 / 0.05)                         # arrêt haut et arrêt de la valeur e : log(m/α)
SEUIL_PROMUE_SEULE_TEXTE = math.log(1 / 0.05)
REECHANTILLONS_TEXTE, GENERATIONS_SYNTHETIQUES_TEXTE, PLAFOND_LOG_E_SYNTHETIQUE = 10_000, 20_000, 50.0
NIVEAU_INTERVALLE_TEXTE = (0.025, 0.975)                       # intervalle percentile à 95 %
GENERATIONS_TEXTE = {"N": 500, "T": 750}
ORACLE_INSTANCES_TEXTE, PLAFOND_COSINUS_TEXTE = 20_000, 1_000
BRAS_T_TEXTE = ("F", "F-arret", "A", "P", "P-prime", "F125")
BRAS_N_TEXTE = BRAS_T_TEXTE + ("G",)


def exiger_constantes_du_texte() -> None:
    from . import banc_tirages_repartis_v1 as B
    from . import lire_banc_tirages_repartis_v1 as LB
    from . import rejeu_v1 as R
    from . import synthetique_v1 as S

    paires = {
        "rejeu.SEUIL_BAS": (R.SEUIL_BAS, SEUIL_BAS_TEXTE), "rejeu.SEUIL_HAUT": (R.SEUIL_HAUT, SEUIL_HAUT_TEXTE),
        "rejeu.SEUIL_PROMUE_SEULE": (R.SEUIL_PROMUE_SEULE, SEUIL_PROMUE_SEULE_TEXTE), "rejeu.M": (R.M, M_TEXTE),
        "rejeu.ALPHA": (R.ALPHA, ALPHA_TEXTE), "rejeu.NB": (R.NB, NB_TEXTE), "rejeu.PART_BLOCS": (R.PART_BLOCS, PART_BLOCS_TEXTE),
        "rejeu.PART125_BLOCS": (R.PART125_BLOCS, F125_BLOCS_TEXTE),
        "rejeu.BUDGET_BLOCS": (R.BUDGET_BLOCS * BLOC_TEXTE, BUDGET_TIRAGES_TEXTE),
        "rejeu.BUDGET125_BLOCS": (R.BUDGET125_BLOCS * BLOC_TEXTE, BUDGET_F125_TIRAGES_TEXTE),
        "rejeu.BRAS_T": (tuple(R.BRAS_T), BRAS_T_TEXTE), "rejeu.BRAS_N": (tuple(R.BRAS_N), BRAS_N_TEXTE),
        "banc.ALPHA": (B.ALPHA, ALPHA_TEXTE), "banc.M": (B.M, M_TEXTE), "banc.BLOC": (B.BLOC, BLOC_TEXTE),
        "banc.N_MAX": (B.N_MAX, PLAFOND_TIRAGES_TEXTE), "banc.PART": (B.PART, PART_TIRAGES_TEXTE),
        "banc.INSTANTS": (tuple(B.INSTANTS), INSTANTS_TEXTE), "banc.ORACLE_N": (B.ORACLE_N, ORACLE_INSTANCES_TEXTE),
        "banc.PLAFOND_COSINUS": (B.PLAFOND_COSINUS, PLAFOND_COSINUS_TEXTE), "banc.GENERATIONS": (dict(B.GENERATIONS), GENERATIONS_TEXTE),
        "lecture.REECHANTILLONS": (LB.REECHANTILLONS, REECHANTILLONS_TEXTE),
        "synthetique.GENERATIONS": (S.GENERATIONS, GENERATIONS_SYNTHETIQUES_TEXTE),
        "synthetique.REECHANTILLONS": (S.REECHANTILLONS, REECHANTILLONS_TEXTE),
        "synthetique.PLAFOND_LOG_E": (S.PLAFOND_LOG_E, PLAFOND_LOG_E_SYNTHETIQUE),
    }
    ecarts = sorted(nom for nom, (a, b) in paires.items() if a != b)
    if ecarts:
        raise GardeArret(f"constante(s) du moteur ≠ texte scellé : {ecarts} : pas de jeu")


# --- troisième écriture des bras ---------------------------------------------------------------------------------------
def _haut(t, n):
    return any(x >= SEUIL_HAUT_TEXTE for x in t[:n])


def _bas(t, n):
    k_min = TIRAGES_MIN_ARRET_BAS_TEXTE // BLOC_TEXTE - 1      # instant de 50 tirages : indice 1
    return any(x < SEUIL_BAS_TEXTE for k, x in enumerate(t[:n]) if k >= k_min)


def _tours(lw, par_pos, n, reste, plafond, tour, elargi):
    """Tours : chaque carte éligible reçoit un bloc, dans l'ordre des positions décalé du numéro du tour, tant qu'il reste
    du budget ; les éligibilités sont lues au début du tour."""
    while reste > 0:
        eligibles = [par_pos[(k + tour) % M_TEXTE] for k in range(M_TEXTE)]
        eligibles = [i for i in eligibles if n[i] < plafond and not _haut(lw[i], n[i]) and (elargi or not _bas(lw[i], n[i]))]
        if not eligibles:
            break
        for i in eligibles:
            if reste == 0:
                break
            n[i] += 1
            reste -= 1
        tour += 1
    return reste, tour


def allocation_du_texte(nom: str, lw, positions, racine: int, f: int, g: int) -> list[int]:
    lw = [list(map(float, t)) for t in lw]
    par_pos = sorted(range(M_TEXTE), key=lambda i: positions[i])
    budget = BUDGET_TIRAGES_TEXTE // BLOC_TEXTE
    n = [0] * M_TEXTE
    if nom == "F":
        return [PART_BLOCS_TEXTE] * M_TEXTE
    if nom == "F125":
        return [F125_BLOCS_TEXTE] * M_TEXTE
    if nom == "F-arret":
        _tours(lw, par_pos, n, budget, PART_BLOCS_TEXTE, 0, False)
    elif nom == "A":
        _tours(lw, par_pos, n, budget, NB_TEXTE, 0, False)
    elif nom == "P":
        reste, _ = _tours(lw, par_pos, n, budget, PART_BLOCS_TEXTE, 0, False)
        rng = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(f, g, 1000)))
        while reste > 0:
            eligibles = [i for i in par_pos if n[i] < NB_TEXTE and not _haut(lw[i], n[i])]   # arrêtées bas comprises
            if not eligibles:
                break
            n[eligibles[int(rng.integers(len(eligibles)))]] += 1
            reste -= 1
    elif nom == "P-prime":
        reste, tour = _tours(lw, par_pos, n, budget, PART_BLOCS_TEXTE, 0, False)
        _tours(lw, par_pos, n, reste, NB_TEXTE, max(tour, PART_BLOCS_TEXTE), True)
    elif nom == "G":
        n = [2] * M_TEXTE
        reste = budget - 2 * M_TEXTE
        while reste > 0:
            libres = [i for i in range(M_TEXTE) if n[i] < NB_TEXTE and not _haut(lw[i], n[i])]
            if not libres:
                break
            j = max(libres, key=lambda i: (lw[i][n[i] - 1], -positions[i]))
            n[j] += 1
            reste -= 1
    else:
        raise GardeArret(f"bras inconnu du texte : {nom!r}")
    return n


def log_e_du_texte(revelees) -> float:
    return next((v for v in revelees if v >= SEUIL_HAUT_TEXTE), revelees[-1])


def ebh_du_texte(log_e) -> list[int]:
    ordre = sorted(range(len(log_e)), key=lambda i: -log_e[i])
    k_etoile = max([k for k, i in enumerate(ordre, 1) if log_e[i] >= math.log(M_TEXTE / (ALPHA_TEXTE * k))], default=0)
    return sorted(ordre[:k_etoile])


def verifier_generation(r: dict, racine: int) -> None:
    """Refait, pour chaque bras d'une génération jouée, l'allocation, les valeurs e et les promotions, depuis le texte."""
    from . import banc_tirages_repartis_v1 as B

    f = B.FAMILLES[r["famille"]]
    attendus = BRAS_N_TEXTE if r["famille"] == "N" else BRAS_T_TEXTE
    if tuple(r["bras"]) != attendus:
        raise GardeArret(f"génération {r['famille']}{r['g']} : bras joués ≠ bras du texte")
    lw = [c["trajectoire"] for c in r["cartes"]]
    for nom, res in r["bras"].items():
        lieu = f"bras {nom}, génération {r['famille']}{r['g']}"
        n = allocation_du_texte(nom, lw, r["positions"], racine, f, r["g"])
        if res["blocs"] != n:
            raise GardeArret(f"{lieu} : allocation non conforme au texte (vérificateur v2)")
        plafond = BUDGET_F125_TIRAGES_TEXTE if nom == "F125" else BUDGET_TIRAGES_TEXTE
        if res["tirages"] != BLOC_TEXTE * sum(n) or res["tirages"] > plafond:
            raise GardeArret(f"{lieu} : tirages non conformes au texte (vérificateur v2)")
        le = [log_e_du_texte(lw[i][:n[i]]) for i in range(M_TEXTE)]
        if any(abs(a - b) > 1e-12 for a, b in zip(le, res["log_e"])):
            raise GardeArret(f"{lieu} : valeur e non conforme au texte (vérificateur v2)")
        if ebh_du_texte(le) != res["promues"]:
            raise GardeArret(f"{lieu} : promotions non conformes au texte (vérificateur v2)")
