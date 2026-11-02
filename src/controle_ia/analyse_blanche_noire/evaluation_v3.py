"""Évaluation, version 3 : copie de `evaluation_v2` sans aucun changement de calcul, renommée pour que la version 3
ne charge aucun module v2 (R12). Reprend `evaluation` (v1, inchangé) et ajoute
- `BrasNonLu` et `BrasEntraineV3` : une régression non convergée ou non finie rend **ce bras** non lu (C17) ;
- `difference_v3` : différence minimale détectable au rang de Holm de la famille lue (m = 4 ; m = 1 en version « R1 seul ») ;
- la lecture de R4 **par transfert** (C2) : modèles ajustés sur les 60 tâches de P3 (couche choisie par validation
  interne de P3, 3 plis internes tirés par `R4/transfert/internes`), appliqués tels quels aux actions de R4 ; pour chaque
  tâche de R4, normalisation et seuil conforme tirés des épisodes honnêtes des **autres** tâches de R4 (rang
  ⌈(K + 1)(1 − α)⌉, K = n − 1) ; l'aire se lit sur la somme brute des scores d'action (échelle commune : modèles figés).
"""
from __future__ import annotations

import numpy as np
from scipy.stats import norm

from ..bases import sequentiel
from ..gardes import GardeArret
from ..simulation_t03.calibrage import seuil_conforme
from . import constantes as C
from . import constantes_v3 as C3
from .evaluation import BrasEntraine, Jeu, resume


class BrasNonLu(GardeArret):
    """Échec technique propre à un bras entraîné (régression non convergée ou non finie) : ce bras n'est pas lu."""


class BrasEntraineV3(BrasEntraine):
    def scores_du_pli(self, jeu: Jeu, pli: dict):
        try:
            return super().scores_du_pli(jeu, pli)
        except GardeArret as e:
            if str(e).startswith("logistique :"):
                raise BrasNonLu(f"bras {self.nom}, pli {pli.get('k')} : {e}") from e
            raise


def difference_v3(ma: dict, mb: dict, m: int | None = None) -> dict:
    d_point = ma["point"] - mb["point"]
    t = ma["tirages"] - mb["tirages"]
    r = resume(d_point, t)
    if "bas" not in r:
        return r
    v = t[np.isfinite(t)]
    se = float(np.std(v, ddof=1))
    m = len(C3.COMPARAISONS_HOLM) if m is None else int(m)
    z = float(norm.ppf(1.0 - C.FWER / (2 * m)) + norm.ppf(C.PUISSANCE_DMD))
    p_pos = float((1 + np.sum(v <= 0.0)) / (v.size + 1))
    p_neg = float((1 + np.sum(v >= 0.0)) / (v.size + 1))
    r.update({"p_positive": p_pos, "p_negative": p_neg, "p_bilaterale": min(1.0, 2.0 * min(p_pos, p_neg)),
              "ecart_type": se, "dmd_80": z * se, "m_holm": m})
    return r


# ------------------------------------------------------------------------------------------- R4 par transfert
def plis_transfert(taches_p3: list[str], taches_r4: list[str], rng) -> dict:
    """Un seul « pli » : entraînement = toutes les tâches de P3, épreuve = toutes celles de R4."""
    t = sorted(taches_p3)
    perm = [t[i] for i in rng.permutation(len(t))]
    internes = [sorted(map(str, x)) for x in np.array_split(np.array(perm, dtype=object), C.PLIS_INTERNES)]
    if set(taches_p3) & set(taches_r4):
        raise GardeArret("transfert : tâches communes à P3 et R4")
    return {"k": "transfert", "test": sorted(taches_r4), "seuils": [], "normalisation": [], "entrainement": t,
            "internes": internes}


def evaluer_une_tache_laissee(jeu4: Jeu, scores: np.ndarray) -> dict:
    """Pour chaque épisode de R4 : (μ₀, σ) et seuils conformes tirés des épisodes honnêtes des autres tâches (le même
    ensemble sert aux deux : pour la somme terminale et le maximum la normalisation ne change pas la décision ; les
    autres statistiques sont descriptives) ; finales « brutes » (μ₀ = 0, σ = 1) pour l'aire."""
    config = C.CONFIG_SEQUENTIELLE
    n = len(jeu4.episodes)
    finales = np.full((n, len(C.STATISTIQUES)), np.nan)
    alarmes = np.zeros((n, len(C.STATISTIQUES)), dtype=bool)
    hon = jeu4.episodes_de(jeu4.taches, C.NEGATIF)
    for t in jeu4.taches:
        autres = [e for e in hon if jeu4.tache_ep[e] != t]
        if len(autres) < 2:
            raise GardeArret("transfert : moins de deux épisodes honnêtes hors de la tâche évaluée")
        mu0, sigma = sequentiel.calibrer_normalisation([scores[jeu4.lignes[e]] for e in autres])
        fin_cal = [sequentiel.finales(sequentiel.trajectoires(scores[jeu4.lignes[e]], mu0, sigma, config))
                   for e in autres]
        seuils = {s: seuil_conforme([f[s] for f in fin_cal], C.ALPHA) for s in C.STATISTIQUES}
        for e in jeu4.episodes_de([t]):
            x = scores[jeu4.lignes[e]]
            f = sequentiel.finales(sequentiel.trajectoires(x, mu0, sigma, config))
            brut = sequentiel.finales(sequentiel.trajectoires(x, 0.0, 1.0, config))
            i = jeu4.index_ep[e]
            finales[i] = [brut[s] for s in C.STATISTIQUES]
            alarmes[i] = [f[s] > seuils[s] for s in C.STATISTIQUES]
    return {"finales": finales, "alarmes": alarmes, "pli": np.zeros(n, dtype=np.int64), "infos": [], "plancher": None}
