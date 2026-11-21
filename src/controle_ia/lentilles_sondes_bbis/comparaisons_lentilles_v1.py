"""Comparaisons entre lentilles de la seconde passe : recouvrements, leurs p et leur médiane sous les deux nuls, corrélations,
moitiés, libellés de comparaison (« non calculable » compris), calibration du recouvrement (borne haute seule).

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`), « Métrique », point 10 ; « Seuil » (libellés des
comparaisons entre lentilles) ; « Plan d'analyse », points 6 et 9. Le texte décide, le code suit.

- **Recouvrement** O_{A,B}(v) : nombre de jetons communs aux vingt premiers jetons (par score, listes départagées : identifiant
  de jeton croissant) de la lecture de v par la lentille A et par la lentille B (0 à 20). Paires : (lentille publique, notre R),
  la paire principale ; (notre R, lentille des logits) ; (moitié paire, moitié impaire de notre R).
- **p du recouvrement** sous chaque nul : p_O = (1 + #{j : O_{A,B}(u_j) ≥ O_{A,B}(v)}) / (M + 1), les u_j étant les **mêmes**
  directions nulles lues par A et par B ; les égalités comptent contre la direction (p conservateur, O étant entier).
- **Corrélation** de Pearson des scores des jetons gardés lus par A et par B ; médiane et quantile 0,99 de la même corrélation
  sur les M directions du nul isotrope ; sans libellé.
- Notre S n'est comparée à aucune lentille R : rien n'est calculé entre elles.
"""
from __future__ import annotations

import hashlib

import numpy as np
import torch

from . import audits_v1 as au
from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import statistiques_v4 as st
from .constantes_v1 import Arret

PAIRE_PRINCIPALE = (K.LENTILLE_PUBLIQUE, K2.LENTILLE_NOTRE_R)
PAIRE_LOGITS = (K2.LENTILLE_NOTRE_R, K.LENTILLE_LOGITS)
PAIRE_MOITIES = (K2.MOITIE_PAIRE, K2.MOITIE_IMPAIRE)
PAIRES = (PAIRE_PRINCIPALE, PAIRE_LOGITS, PAIRE_MOITIES)
PAIRES_INTERDITES = tuple((K2.LENTILLE_NOTRE_S, l) for l in (K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS, K2.LENTILLE_NOTRE_R,
                                                             K2.MOITIE_PAIRE, K2.MOITIE_IMPAIRE))

# --- libellés (« Seuil ») -----------------------------------------------------------------------------------------------------------
RECOUVREMENT_AU_DELA = "au-delà des deux nuls"
RECOUVREMENT_NON_DISTINCT = "non distinct du nul"
RECOUVREMENT_INTERMEDIAIRE = "intermédiaire"
LECTURE_COMMUNE = "lecture commune aux deux lentilles R"
LECTURE_PROPRE = "lecture propre à une lentille"
DEUX_NON_DISTINCTES = "deux lectures non distinctes"
MIXTE = "mixte"
NON_CALCULABLE = "non calculable"
MOTIF_CALIBRATION_RECOUVREMENT = "calibration du recouvrement au-dessus de sa borne haute"
MOTIF_NUL_REFAIT = "nuls isotropes refaits par direction à cette couche (garde du rapport à ε)"
MOTIF_LENTILLE_NON_LUE = "lentille non lue à la couche"
MOTIF_LIBELLE_DIFFERENT = "libellé de la lentille publique différent d'une passe à l'autre"
SANS_OBJET_BORNE_BASSE = "sans objet : le recouvrement est entier, ses égalités rendent p_O conservateur"


def exiger_paire(a: str, b: str) -> None:
    """Notre S n'est comparée à aucune lentille R (elle classe des jetons d'entrée, les lentilles R des jetons de sortie)."""
    if K2.LENTILLE_NOTRE_S in (a, b) or K2.PLONGEMENTS_SEULS in (a, b):
        raise Arret(f"comparaison entre lentilles : la paire ({a}, {b}) n'est pas calculée (notre S n'est comparée à aucune "
                    "lentille R)")
    if (a, b) not in PAIRES:
        raise Arret(f"comparaison entre lentilles : paire ({a}, {b}) hors des paires du texte")


def recouvrement(ids_a, ids_b) -> int:
    """Nombre de jetons communs à deux listes de vingt premiers jetons (identifiants, ou rangs parmi les jetons gardés)."""
    a, b = [int(i) for i in ids_a], [int(i) for i in ids_b]
    if len(set(a)) != len(a) or len(set(b)) != len(b):
        raise Arret("recouvrement : doublon dans une liste de premiers jetons")
    return len(set(a) & set(b))


def recouvrements_colonnes(rangs_a: torch.Tensor, rangs_b: torch.Tensor) -> torch.Tensor:
    """O_{A,B}(u_j) pour chaque direction j : `rangs_a`, `rangs_b` `[k, n]`, vingt premiers jetons de chaque direction lue par A
    et par B (rangs parmi les jetons gardés, listes départagées). Rend `[n]`, entier."""
    if rangs_a.shape != rangs_b.shape or rangs_a.ndim != 2:
        raise Arret("recouvrement : listes de formes différentes entre les deux lentilles (directions non appariées)")
    return (rangs_a[:, None, :] == rangs_b[None, :, :]).any(1).sum(0).to(torch.int64)


def p_recouvrement(recouvrements_nuls: torch.Tensor, valeur: int) -> float:
    """p_O = (1 + #{j : O(u_j) ≥ O(v)}) / (M + 1) ; une égalité compte contre la direction."""
    o = torch.as_tensor(recouvrements_nuls)
    return float((1 + int((o >= int(valeur)).sum())) / (o.numel() + 1))


def mediane(recouvrements_nuls: torch.Tensor) -> float:
    """Médiane de O(u_j) sur les M directions d'un nul (moyenne des deux valeurs centrales quand M est pair)."""
    return float(np.median(torch.as_tensor(recouvrements_nuls).numpy()))


def libelle_recouvrement(p_iso: float, p_signes: float) -> str:
    """« au-delà des deux nuls » si p_O ≤ 0,001 sous le nul isotrope et p_O ≤ 0,01 sous le nul des signes ; « non distinct du
    nul » si p_O > 0,05 sous l'un des deux ; « intermédiaire » sinon (mêmes niveaux que la concentration)."""
    if p_iso <= K.P_ISO_CONCENTREE and p_signes <= K.P_SIGNES_CONCENTREE:
        return RECOUVREMENT_AU_DELA
    if p_iso > K.P_NON_DISTINCTE or p_signes > K.P_NON_DISTINCTE:
        return RECOUVREMENT_NON_DISTINCT
    return RECOUVREMENT_INTERMEDIAIRE


def libelle_comparaison(libelle_publique: str, libelle_notre_r: str, libelle_du_recouvrement: str) -> dict:
    """Libellé de la paire principale, par direction et signe :
    - lecture commune : « concentrée au-delà des deux nuls » par les deux **et** recouvrement « au-delà des deux nuls » ;
    - lecture propre à une lentille : « concentrée » par l'une, « non distincte du nul » par l'autre (la lentille est nommée) ;
    - deux lectures non distinctes : « non distincte du nul » par les deux ;
    - mixte : tout autre cas."""
    connus = (st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE, st.LIBELLE_NON_DISTINCTE)
    if libelle_publique not in connus or libelle_notre_r not in connus:
        raise Arret(f"libellé de lecture inconnu ({libelle_publique!r}, {libelle_notre_r!r})")
    if libelle_du_recouvrement not in (RECOUVREMENT_AU_DELA, RECOUVREMENT_NON_DISTINCT, RECOUVREMENT_INTERMEDIAIRE):
        raise Arret(f"libellé de recouvrement inconnu ({libelle_du_recouvrement!r})")
    c, n = st.LIBELLE_CONCENTREE, st.LIBELLE_NON_DISTINCTE
    if libelle_publique == c and libelle_notre_r == c and libelle_du_recouvrement == RECOUVREMENT_AU_DELA:
        return {"libelle": LECTURE_COMMUNE}
    if libelle_publique == c and libelle_notre_r == n:
        return {"libelle": LECTURE_PROPRE, "lentille": K.LENTILLE_PUBLIQUE, "autre": K2.LENTILLE_NOTRE_R}
    if libelle_notre_r == c and libelle_publique == n:
        return {"libelle": LECTURE_PROPRE, "lentille": K2.LENTILLE_NOTRE_R, "autre": K.LENTILLE_PUBLIQUE}
    if libelle_publique == n and libelle_notre_r == n:
        return {"libelle": DEUX_NON_DISTINCTES}
    return {"libelle": MIXTE}


def non_calculable(motif: str) -> dict:
    """Libellé de comparaison « non calculable », motif écrit."""
    if motif not in (MOTIF_CALIBRATION_RECOUVREMENT, MOTIF_NUL_REFAIT, MOTIF_LENTILLE_NON_LUE, MOTIF_LIBELLE_DIFFERENT):
        raise Arret(f"motif de comparaison non calculable inconnu ({motif!r})")
    return {"libelle": NON_CALCULABLE, "motif": motif, "en_clair": f"{NON_CALCULABLE} : {motif}"}


# --- corrélations ----------------------------------------------------------------------------------------------------------------------
def correlation(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """Corrélation de Pearson, colonne par colonne, des scores des jetons gardés lus par A et par B : `[jetons]` ou
    `[jetons, n]` ; calcul en double précision. Une colonne constante : arrêt (valeur non finie)."""
    a, b = (x[:, None] if x.ndim == 1 else x for x in (a.double(), b.double()))
    if a.shape != b.shape:
        raise Arret("corrélation : scores de formes différentes entre les deux lentilles")
    a, b = a - a.mean(0, keepdim=True), b - b.mean(0, keepdim=True)
    r = (a * b).sum(0) / (a.norm(dim=0) * b.norm(dim=0))
    if not bool(torch.isfinite(r).all()):
        raise Arret("valeur non finie dans une corrélation entre lentilles : arrêt")
    return r


def resume_correlation(r_v: float, r_nul_isotrope: torch.Tensor) -> dict:
    """r_{A,B}(v), avec la médiane et le quantile 0,99 de la même corrélation sur les M directions du nul isotrope ; sans libellé."""
    r = torch.as_tensor(r_nul_isotrope, dtype=torch.float64)
    return {"r": float(r_v), "mediane_nul_isotrope": float(r.median() if r.numel() % 2 else np.median(r.numpy())),
            "quantile_0_99_nul_isotrope": float(torch.quantile(r, K.QUANTILE_PART))}


# --- appariement des nuls (plan, point 9) ---------------------------------------------------------------------------------------------
def empreinte_tirage(directions) -> str:
    """SHA-256 des octets d'un tirage de directions nulles ou témoins (simple précision, petit-boutistes, ordre des lignes)."""
    a = directions.numpy() if isinstance(directions, torch.Tensor) else np.asarray(directions)
    return hashlib.sha256(np.ascontiguousarray(a.astype("<f4", copy=False)).tobytes()).hexdigest()


def exiger_appariement(empreintes_par_lentille: dict) -> str:
    """Mêmes directions nulles pour toutes les lentilles d'une couche : les empreintes des tirages lus par chaque lentille
    sont égales ; sinon arrêt (le recouvrement ne serait plus comparable à son nul)."""
    valeurs = set(empreintes_par_lentille.values())
    if len(valeurs) != 1:
        raise Arret(f"directions nulles non appariées entre lentilles ({sorted(empreintes_par_lentille)}) : arrêt")
    return valeurs.pop()


# --- une direction, une paire ------------------------------------------------------------------------------------------------------------
def comparer(paire: tuple, rangs_v: tuple, rangs_nuls: dict) -> dict:
    """Recouvrement d'une direction à un signe pour une paire de lentilles, son p et sa médiane sous chaque nul.
    `rangs_v` : (vingt premiers par A, vingt premiers par B) ; `rangs_nuls` : nom du nul → (rangs `[k, M]` par A, par B), les
    mêmes directions nulles lues par les deux, au même signe. Pour la paire des moitiés : nul isotrope seulement."""
    exiger_paire(*paire)
    if paire == PAIRE_MOITIES and set(rangs_nuls) - {K.NUL_ISOTROPE}:
        raise Arret("recouvrement des moitiés : sous le nul isotrope partagé seulement")
    o = recouvrement(*rangs_v)
    sortie = {"paire": list(paire), "recouvrement": o, "k": len(list(rangs_v[0])), "nuls": {}}
    for nul, (a, b) in rangs_nuls.items():
        o_nuls = recouvrements_colonnes(a, b)
        sortie["nuls"][nul] = {"p": p_recouvrement(o_nuls, o), "mediane": mediane(o_nuls), "m": int(o_nuls.numel()),
                               "recouvrements_nuls": o_nuls}
    return sortie


def comparer_les_deux_recouvrements(o_principal: int | None, o_moities: int | None) -> dict:
    """O_{publique, notre R}(v) et O_{paire, impaire}(v) côte à côte ; leur différence, sans libellé."""
    return {"publique_et_notre_r": o_principal, "moities_de_notre_r": o_moities,
            "difference": None if o_principal is None or o_moities is None else int(o_principal) - int(o_moities)}


# --- calibration du recouvrement (paire principale) -------------------------------------------------------------------------------------
def calibration_recouvrement(p_par_jeu: list, m: int = K.M_NUL) -> dict:
    """Les p_O des témoins de chaque nul contre les M directions nulles, comptés et comparés à la **seule borne haute** de la
    règle de calibration ; la borne basse est « sans objet ». Compte au-dessus de la borne haute : recouvrements de cette
    couche et de ce nul « non calculables », sans arrêt du reste."""
    jeux = [int(np.asarray(p).size) for p in p_par_jeu]
    _, haut = au.bornes_calibration(jeux, m)
    compte = int(sum(int((np.asarray(p) <= K.SEUIL_P_CALIBRATION).sum()) for p in p_par_jeu))
    return {"n": int(sum(jeux)), "jeux": jeux, "compte_p_sous_0_05": compte, "q_haut": haut, "q_bas": SANS_OBJET_BORNE_BASSE,
            "tenue": bool(compte <= haut)}


def p_recouvrement_temoins(rangs_temoins_a: torch.Tensor, rangs_temoins_b: torch.Tensor, recouvrements_nuls: torch.Tensor) -> np.ndarray:
    """p_O de chaque témoin contre les M directions nulles du même nul."""
    o_t = recouvrements_colonnes(rangs_temoins_a, rangs_temoins_b)
    nuls = torch.sort(torch.as_tensor(recouvrements_nuls)).values
    au_moins = nuls.numel() - torch.searchsorted(nuls, o_t, right=False)
    return ((1 + au_moins).double() / (nuls.numel() + 1)).numpy()
