"""S8 (ii) — la garde d'équivalence des deux couches du banc (B2 ; étape 7).

Pour chaque proposeur, chaque bras et chaque dose, la moyenne de M1 sur les sources de la couche mécanique (rejouée aux
réglages gelés, sous des graines disjointes de celles où les fréquences sont mesurées : étape 6 bis) tombe dans l'intervalle de
prédiction à 99,9 % que la couche statistique donne pour une moyenne sur ce nombre de sources ; sinon, arrêt (liste d'arrêt,
point 4). L'intervalle est lu sur la loi de la moyenne de n sources de la couche statistique, estimée par 20 000 moyennes de n
valeurs tirées avec remise parmi les valeurs de M1 d'un grand nombre de sources simulées (SILENCE : le texte ne dit pas comment
l'intervalle est estimé). La garde compare des moyennes ; elle ne prouve pas que les deux couches ont la même loi (B2).
"""

import numpy as np

from .constantes import MOYENNES_DE_PREDICTION_S8, NIVEAU_PREDICTION_S8


class ArretEquivalence(RuntimeError):
    pass


def intervalle_de_prediction(valeurs_statistiques, n, rng, niveau=NIVEAU_PREDICTION_S8, moyennes=MOYENNES_DE_PREDICTION_S8):
    v = np.asarray(valeurs_statistiques, dtype=float)
    if v.ndim != 1 or len(v) < 100:
        raise ArretEquivalence("couche statistique : au moins cent sources pour un intervalle de prédiction")
    m = v[rng.integers(0, len(v), (moyennes, n))].mean(axis=1)
    a = (1.0 - niveau) / 2.0
    return float(np.quantile(m, a)), float(np.quantile(m, 1.0 - a))


def garde_equivalence(moyennes_mecaniques, valeurs_statistiques, rng, niveau=NIVEAU_PREDICTION_S8):
    """`moyennes_mecaniques` : {clé : (moyenne de M1 sur la couche mécanique, nombre de sources)} ; `valeurs_statistiques` :
    {clé : valeurs de M1 par source de la couche statistique}. Rend le détail ; lève `ArretEquivalence` si une moyenne sort de
    son intervalle."""
    detail, hors = {}, []
    for cle in sorted(moyennes_mecaniques):
        if cle not in valeurs_statistiques:
            raise ArretEquivalence(f"S8 (ii) : aucune valeur de la couche statistique pour {cle}")
        moy, n = moyennes_mecaniques[cle]
        bas, haut = intervalle_de_prediction(valeurs_statistiques[cle], int(n), rng, niveau)
        detail[cle] = {"moyenne_mecanique": float(moy), "sources": int(n), "intervalle": [bas, haut],
                       "moyenne_statistique": float(np.mean(valeurs_statistiques[cle]))}
        if not (bas <= moy <= haut):
            hors.append(cle)
    if hors:
        raise ArretEquivalence(f"S8 (ii) : les deux couches ne s'accordent pas pour {hors} : arrêt, retour au rédacteur "
                               f"(liste d'arrêt, point 4) ; détail : {[detail[c] for c in hors][:3]}")
    return detail


def decalage_sort_de_l_intervalle(valeurs_saines, valeurs_decalees, n, rng, niveau=NIVEAU_PREDICTION_S8):
    """Garde 23, précondition de l'artefact : le décalage planté sort de l'intervalle à n sources (la moyenne saine de la couche
    statistique hors de l'intervalle de la couche décalée)."""
    bas, haut = intervalle_de_prediction(valeurs_decalees, n, rng, niveau)
    m = float(np.mean(valeurs_saines))
    return not (bas <= m <= haut), (bas, haut), m
