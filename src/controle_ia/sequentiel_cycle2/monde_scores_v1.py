"""Monde à scores : la chaîne du brouillon 3 en miniature, sur des scores d'action tirés d'une loi connue.

Il vérifie ce que le monde gaussien suppose : que l'intervalle percentile du rééchantillonnage par tâche tient son
niveau aux percentiles extrêmes d'une lecture intermédiaire, sur un effectif réduit. Une dose, une série de textes
(la chaîne réelle moyenne deux séries : simplification déclarée). Scores continus : aucun ex aequo (gardé).

Vérités plantées (clé « verite ») :
  « nul »        : aucun décalage ;
  « dense »      : décalage le long de la sonde seule, à chaque action (signal propre, dense) ;
  « quelconque » : décalage dense de chaque direction, d'amplitude tirée ; la sonde est une direction comme les autres ;
  « frontiere »  : comme « quelconque », la sonde placée au quantile 0,95 des directions (propreté nulle, gain réel) ;
  « concentre »  : décalage fort le long de la sonde sur `actions_decalees` actions tirées par épisode.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import norm

from ..gardes import GardeArret
from . import etats_v1 as etats
from . import niveaux_v1 as niveaux

VERITES = ("nul", "dense", "quelconque", "frontiere", "concentre")
N_ACTIONS = 10
QUANTILE_PLANCHER = 0.95


def _exiger_config(c: dict) -> None:
    cles = {"verite", "n_taches", "n_intermediaire", "n_directions", "amplitude", "amplitude_directions",
            "actions_decalees", "part_tache", "part_commune", "marge", "part_intermediaire",
            "tirages_intermediaire", "tirages_finale"}
    if set(c) != cles:
        raise GardeArret(f"configuration du monde à scores : clés attendues {sorted(cles)}, reçu {sorted(c)}")
    if c["verite"] not in VERITES:
        raise GardeArret(f"vérité {c['verite']!r} inconnue")
    if not (0 < c["n_intermediaire"] < c["n_taches"]):
        raise GardeArret("effectifs : 0 < intermédiaire < complet")
    if not (1 <= c["actions_decalees"] <= N_ACTIONS and c["n_directions"] >= 20):
        raise GardeArret("actions décalées entre 1 et 10 ; au moins 20 directions")
    if not (0.0 <= c["part_tache"] < 1.0 and 0.0 <= c["part_commune"] < 1.0):
        raise GardeArret("parts de variance dans [0 ; 1[")
    q_i, q_f = niveaux.repartir(niveaux.Q_DECISIF, c["part_intermediaire"])
    for nom, q in (("tirages_intermediaire", q_i), ("tirages_finale", q_f)):
        if c[nom] * q < 5:
            raise GardeArret(f"{nom} = {c[nom]} : moins de cinq tirages attendus au-delà du percentile {q:.6f}")


def tirer_scores(config: dict, rng: np.random.Generator) -> np.ndarray:
    """Scores d'action : (tâches, 1 + directions, 2 états, 10 actions) ; indice 0 = sonde ; état 1 = saboteur."""
    c = config
    n, k = c["n_taches"], c["n_directions"] + 1
    commun = rng.standard_normal((n, 1, 1, 1))
    propre = rng.standard_normal((n, k, 1, 1))
    tache = np.sqrt(c["part_commune"]) * commun + np.sqrt(1.0 - c["part_commune"]) * propre
    bruit = rng.standard_normal((n, k, 2, N_ACTIONS))
    scores = np.sqrt(c["part_tache"]) * tache + np.sqrt(1.0 - c["part_tache"]) * bruit
    decalage = np.zeros(k)
    v = c["verite"]
    if v in ("dense", "concentre"):
        decalage[0] = c["amplitude"]
    if v in ("quelconque", "frontiere"):
        decalage[:] = c["amplitude_directions"] * np.abs(rng.standard_normal(k))
    if v == "frontiere":
        # quantile 0,95 d'une demi-normale : la sonde est exactement à la frontière de propreté, en population
        decalage[0] = c["amplitude_directions"] * float(norm.isf((1.0 - QUANTILE_PLANCHER) / 2.0))
    masque = np.ones((n, N_ACTIONS))
    if v == "concentre":
        masque = np.zeros((n, N_ACTIONS))
        rangs = np.argsort(rng.random((n, N_ACTIONS)), axis=1)[:, : c["actions_decalees"]]
        np.put_along_axis(masque, rangs, 1.0, axis=1)
    scores[:, :, 1, :] += decalage[None, :, None] * masque[:, None, :]
    return scores


def statistiques_episode(scores: np.ndarray) -> np.ndarray:
    """(2 statistiques, tâches, directions, 2 états) : somme puis maximum des dix scores d'action. Liste fermée."""
    if scores.ndim != 4 or scores.shape[2] != 2 or scores.shape[3] != N_ACTIONS:
        raise GardeArret(f"scores de forme {scores.shape} : (tâches, directions, 2, {N_ACTIONS}) attendu")
    if not np.all(np.isfinite(scores)):
        raise GardeArret("score non fini")
    return np.stack([scores.sum(axis=3), scores.max(axis=3)])


def ordonner(pos: np.ndarray, neg: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Ordre commun des épisodes des deux états : (tâche de chaque rang, rang occupé par un positif)."""
    n = pos.shape[0]
    valeurs = np.concatenate([pos, neg])
    if np.unique(valeurs).size != valeurs.size:
        raise GardeArret("ex aequo dans les statistiques d'épisode : hors du domaine de ce module")
    ordre = np.argsort(valeurs, kind="stable")
    return ordre % n, ordre < n


def aires_depuis_ordre(poids_t: np.ndarray, taches: np.ndarray, est_pos: np.ndarray) -> np.ndarray:
    """Aires sous rééchantillonnage ; `poids_t` : (tâches, tirages), en flottants ; rend (tirages,)."""
    w = poids_t[taches]                                    # (2 n, tirages) : une ligne par rang
    cumul_neg = np.cumsum(w[~est_pos], axis=0)             # poids des négatifs, cumulés dans l'ordre des rangs
    avant = np.cumsum(~est_pos)[est_pos]                   # nombre de négatifs sous chaque positif
    garde = avant > 0
    somme = np.einsum("ib,ib->b", w[est_pos][garde], cumul_neg[avant[garde] - 1])
    total = poids_t.sum(axis=0, dtype=np.float64)
    return somme / (total * total)


def aires_reechantillonnees(pos: np.ndarray, neg: np.ndarray, poids: np.ndarray) -> np.ndarray:
    """Aires de Mann-Whitney sous rééchantillonnage des tâches : (tirages,).

    `pos`, `neg` : (tâches,) ; `poids` : (tirages, tâches), nombre de fois que chaque tâche est tirée.
    Égale, tirage par tirage, à l'aire calculée sur les tâches tirées avec leurs répétitions (éprouvé).
    """
    taches, est_pos = ordonner(pos, neg)
    return aires_depuis_ordre(np.ascontiguousarray(poids.T, dtype=np.float64), taches, est_pos)


def lire(stats: np.ndarray, n_tirages: int, niveaux_lus: dict, marge: float, rng: np.random.Generator,
         lot: int = 2000) -> dict:
    """Une lecture sur les tâches de `stats` : affirmations établies, par jeu de niveaux.

    `niveaux_lus` : {nom: (percentile décisif, percentile d'équivalence)} — plusieurs plans lus sur les mêmes tirages.
    """
    _, n, k, _ = stats.shape
    ordres = [[ordonner(stats[s, :, j, 1], stats[s, :, j, 0]) for j in range(k)] for s in range(2)]
    d_somme, d_max, ecart = [], [], []
    fait = 0
    while fait < n_tirages:
        b = min(lot, n_tirages - fait)
        fait += b
        poids_t = np.ascontiguousarray(rng.multinomial(n, np.full(n, 1.0 / n), size=b).T, dtype=np.float64)
        aires = np.empty((2, k, b))
        for s in range(2):
            for j in range(k):
                aires[s, j] = aires_depuis_ordre(poids_t, *ordres[s][j])
        plancher = np.quantile(aires[:, 1:, :], QUANTILE_PLANCHER, axis=1)     # (2, tirages)
        d_somme.append(aires[0, 0] - plancher[0])
        d_max.append(aires[1, 0] - plancher[1])
        ecart.append(aires[0, 0] - aires[1, 0])
    d_somme, d_max, ecart = (np.concatenate(x) for x in (d_somme, d_max, ecart))
    sortie = {}
    for nom, (q, qe) in niveaux_lus.items():
        if q is None:
            sortie[nom] = {a: False for a in etats.AFFIRMATIONS}
            continue
        bas = lambda x: float(np.quantile(x, q))
        haut = lambda x, p: float(np.quantile(x, 1.0 - p))
        sortie[nom] = {"c1": bas(d_somme) > 0.0, "c2": bas(ecart) > 0.0, "c3": haut(ecart, q) < 0.0,
                       "c4": bas(d_max) > 0.0, "c5": haut(d_somme, qe) < marge, "c6": haut(ecart, qe) < marge}
    return sortie


def jouer_replique(config: dict, graine: np.random.SeedSequence) -> dict:
    """Une réplique : états de dose à l'intermédiaire et à la finale, pour les plans « unique », « reparti », « naif »."""
    _exiger_config(config)
    c = config
    g_scores, g_inter, g_finale = (np.random.default_rng(s) for s in graine.spawn(3))
    stats = statistiques_episode(tirer_scores(c, g_scores))
    q, qe, f = niveaux.Q_DECISIF, niveaux.Q_EQUIVALENCE, c["part_intermediaire"]
    (q_i, q_f), (qe_i, qe_f) = niveaux.repartir(q, f), niveaux.repartir(qe, f)
    inter = lire(stats[:, : c["n_intermediaire"]], c["tirages_intermediaire"],
                 {"unique": (None, None), "reparti": (q_i, qe_i), "naif": (q, qe)}, c["marge"], g_inter)
    finale = lire(stats, c["tirages_finale"],
                  {"unique": (q, qe), "reparti": (q_f, qe_f), "naif": (q, qe)}, c["marge"], g_finale)
    return {plan: {"intermediaire": etats.etat_dose(inter[plan]),
                   "finale": etats.etat_dose(etats.cumuler(inter[plan], finale[plan]))}
            for plan in ("unique", "reparti", "naif")}


def ecart_de_population(config: dict, amplitude: float, rng: np.random.Generator, n_episodes: int = 20000) -> float:
    """Écart « aire de la somme moins aire du maximum » de la sonde, en population, pour un décalage dense."""
    c = dict(config, verite="dense", amplitude=amplitude, n_taches=n_episodes, n_directions=20)
    s = statistiques_episode(tirer_scores(c, rng)[:, :1])
    poids = np.ones((1, n_episodes), dtype=np.int64)
    return float(aires_reechantillonnees(s[0, :, 0, 1], s[0, :, 0, 0], poids)[0]
                 - aires_reechantillonnees(s[1, :, 0, 1], s[1, :, 0, 0], poids)[0])


def regler_amplitude(config: dict, cible: float, graine: np.random.SeedSequence, pas: float = 0.02,
                     maximum: float = 3.0) -> float:
    """Plus petite amplitude dense pour laquelle l'écart de population atteint `cible` ; arrêt si jamais atteinte."""
    a = pas
    while a <= maximum:
        if ecart_de_population(config, a, np.random.default_rng(graine)) >= cible:
            return round(a, 6)
        a += pas
    raise GardeArret(f"aucun décalage dense jusqu'à {maximum} n'atteint un écart de {cible} : nœud (brouillon 3, « Puissance »)")
