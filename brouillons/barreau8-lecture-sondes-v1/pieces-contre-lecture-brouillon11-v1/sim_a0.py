"""Simulation courte de l'essai de la chaîne A0 (artefact positif (ii)) sous deux formes d'étiquetage.

(R) moitié des 64 tâches, tirée au hasard, étiquette 1 pour toutes ses actions (brouillon 11, tel qu'écrit) ;
(A) dans chaque tâche, 5 des 10 actions tirées au hasard reçoivent l'étiquette 1.

Données synthétiques seulement (aucune donnée du programme) : score d'action = effet de tâche (écart-type
sigma_t, propre à chaque direction) + bruit normal réduit, indépendant par action. Une sonde et 800 directions
de plancher, indépendantes. Règle « au-dessus » du texte : D = aire de la sonde − quantile 0,95 des aires des
800 directions, sonde et directions recalculées sur les mêmes tirages de tâches (2 000 tirages par blocs de
tâches, `rng.integers(0, 64, 64)` comme `intervalle_blocs`) ; au-dessus si le quantile 0,05/6 (niveau décisif
98,33 %, bilatéral) de D* est strictement positif. Aire de Mann-Whitney regroupée sur toutes les paires
(positif, négatif), y compris entre tâches et entre copies d'une même tâche, comme le fait la concaténation
des blocs tirés. Graines : numpy.random.SeedSequence, une fille par (règle, sigma, répétition, usage).

Scénarios par répétition (mêmes données, mêmes étiquettes que (i), comme le texte) :
  sain       : (i) aucune injection ; attendu : non au-dessus ;
  artefact   : (ii) action étiquetée 1 : score porté à score + 2 s (s = écart-type de population des scores
               d'action de la sonde sur H) — équivaut à l'injection « maximum de l'action plus 2 s » sur un jeton ;
               attendu : au-dessus ;
  alignement : (iii) données de (ii), scores permutés entre toutes les actions, étiquettes en place ;
               attendu : non au-dessus ;
  agreg      : chaîne cassée, agrégation fausse (moyenne sur 50 jetons : décalage 2 s / 50) ; attendu : non au-dessus ;
  decale     : chaîne cassée, scores décalés d'une action à l'intérieur de chaque épisode (pas t reçoit le score
               du pas t+1, circulaire) ; attendu : non au-dessus.
"""
from __future__ import annotations

import sys
import time

import numpy as np

T, A, NDIR, B = 64, 10, 800, 2000
ALPHA = (0.05 / 3) / 2          # quantile bas du niveau décisif 98,33 %
QP = 0.95


def etiquettes(regle: str, rng) -> np.ndarray:
    lab = np.zeros((T, A), dtype=bool)
    if regle == "R":
        lab[rng.permutation(T)[: T // 2], :] = True
    else:
        for t in range(T):
            lab[t, rng.permutation(A)[: A // 2]] = True
    return lab


def matrices_C(x: np.ndarray, lab: np.ndarray, bloc: int = 40) -> np.ndarray:
    """C[d, t, u] = nombre de paires (positif de la tâche t, négatif de la tâche u) où le positif l'emporte."""
    D = x.shape[0]
    flat = x.reshape(D, T * A)
    lp = lab.reshape(-1).astype(np.float32)
    ln = (~lab).reshape(-1).astype(np.float32)
    masque = (lp[:, None] * ln[None, :]).astype(np.float32)
    C = np.empty((D, T, T), dtype=np.float32)
    for i in range(0, D, bloc):
        xs = flat[i:i + bloc]
        cmp = (xs[:, :, None] > xs[:, None, :]).astype(np.float32) * masque
        C[i:i + bloc] = cmp.reshape(-1, T, A, T, A).sum(axis=(2, 4))
    return C


def aires_bootstrap(C: np.ndarray, W: np.ndarray, lab: np.ndarray, bloc: int = 100) -> np.ndarray:
    """Aire de chaque direction sur chaque tirage : (W C W) / (P N). Rend (B, D)."""
    p = lab.sum(axis=1).astype(np.float32)
    n = (~lab).sum(axis=1).astype(np.float32)
    denom = (W @ p) * (W @ n)
    D = C.shape[0]
    out = np.empty((W.shape[0], D), dtype=np.float32)
    for i in range(0, D, bloc):
        c = C[i:i + bloc]                               # (k, T, T)
        k = c.shape[0]
        tmp = W @ c.transpose(1, 0, 2).reshape(T, k * T)  # (B, k*T)
        tmp = tmp.reshape(W.shape[0], k, T) * W[:, None, :]
        out[:, i:i + k] = tmp.sum(axis=2)
    with np.errstate(invalid="ignore", divide="ignore"):
        return out / denom[:, None]


def aire_point(C: np.ndarray, lab: np.ndarray) -> np.ndarray:
    return C.sum(axis=(1, 2)) / (lab.sum() * (~lab).sum())


def regle_au_dessus(Cs, Cp_boot, Cp_point, W, lab):
    a_s = aires_bootstrap(Cs[None], W, lab)[:, 0]
    q = np.quantile(Cp_boot, QP, axis=1)
    d = a_s - q
    bas = np.quantile(d, ALPHA)
    return bas > 0, float(aire_point(Cs[None], lab)[0]), float(np.quantile(Cp_point, QP)), float(bas)


def une_repetition(regle, sigma, ss):
    r_dat, r_lab, r_boot, r_perm = [np.random.default_rng(s) for s in ss.spawn(4)]
    eff = r_dat.normal(0, sigma, size=(NDIR + 1, T, 1)) if sigma > 0 else np.zeros((NDIR + 1, T, 1))
    x = (eff + r_dat.normal(size=(NDIR + 1, T, A))).astype(np.float32)
    lab = etiquettes(regle, r_lab)
    choix = r_boot.integers(0, T, size=(B, T))
    W = np.stack([np.bincount(c, minlength=T) for c in choix]).astype(np.float32)
    Cp = matrices_C(x[1:], lab)
    Ap_boot = aires_bootstrap(Cp, W, lab)
    Ap_point = aire_point(Cp, lab)
    s0 = x[0]
    s = float(s0.std())                     # écart-type de population des scores d'action sur H
    scen = {}
    scen["sain"] = s0
    art = s0 + 2 * s * lab
    scen["artefact"] = art
    perm = r_perm.permutation(T * A)
    scen["alignement"] = art.reshape(-1)[perm].reshape(T, A)
    scen["agreg"] = s0 + (2 * s / 50) * lab
    scen["decale"] = np.roll(art, -1, axis=1)
    res = {}
    for nom, v in scen.items():
        Cs = matrices_C(v[None].astype(np.float32), lab)[0]
        res[nom] = regle_au_dessus(Cs, Ap_boot, Ap_point, W, lab)
    return res


def main(n_rep: int, sigmas=(0.0, 0.5, 1.0, 2.0)):
    racine = np.random.SeedSequence(20261119)   # graine de la simulation, consignée
    print(f"# numpy {np.__version__} ; graine racine SeedSequence(20261119) ; {n_rep} répétitions par case")
    for ir, regle in enumerate(("R", "A")):
        for js, sigma in enumerate(sigmas):
            t0 = time.time()
            compte = {}
            stats = {"aire_art": [], "q95": [], "bas_art": []}
            for k in range(n_rep):
                ss = np.random.SeedSequence(racine.entropy, spawn_key=(ir, js, k))
                res = une_repetition(regle, sigma, ss)
                for nom, (dessus, aire, q, bas) in res.items():
                    compte[nom] = compte.get(nom, 0) + int(dessus)
                stats["aire_art"].append(res["artefact"][1])
                stats["q95"].append(res["artefact"][2])
                stats["bas_art"].append(res["artefact"][3])
            echec_art = n_rep - compte["artefact"]
            print(f"règle {regle} sigma_tache/sigma_bruit={sigma}: "
                  f"artefact (ii) ÉCHOUE {echec_art}/{n_rep} ; "
                  f"sain au-dessus {compte['sain']}/{n_rep} ; alignement au-dessus {compte['alignement']}/{n_rep} ; "
                  f"agrégation fausse au-dessus {compte['agreg']}/{n_rep} ; décalage d'un pas au-dessus {compte['decale']}/{n_rep} ; "
                  f"aire artefact moy {np.mean(stats['aire_art']):.3f} ; q0,95 plancher moy {np.mean(stats['q95']):.3f} "
                  f"(max {np.max(stats['q95']):.3f}) ; borne basse D artefact min {np.min(stats['bas_art']):.3f} "
                  f"moy {np.mean(stats['bas_art']):.3f} ; {time.time() - t0:.0f} s", flush=True)


if __name__ == "__main__":
    sig = tuple(float(v) for v in sys.argv[2].split(",")) if len(sys.argv) > 2 else (0.0, 0.5, 1.0, 2.0)
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 2, sigmas=sig)
