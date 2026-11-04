"""Lectures descriptives des courbes d'un axe sur la fenêtre W de l'addendum R9-bis (<<DOI_R9_BIS>>), sans balayage
de plus : les courbes d'un axe sont les axes des grilles 2D déjà mesurées (axe 1 : α₂ = 0, direction d₁ ; axe 2 :
α₁ = 0, direction d₂ orthogonalisée contre d₁, alignée à plus de 99 % quand |cos| < 0,1, annexe A du papier).

Emprunts à R9-bis, réutilisés par citation, sans recalcul de ses données :
- fenêtre W = angles de 2° à 60°, bornes comprises, de la grille canonique (30 angles), déclarée avant les données ;
- D(x) = moyenne sur W de [courbe médiane sur les ancres de x − médiane, angle par angle, des courbes des différences
  aléatoires] ;
- enveloppe d'une famille : médiane et percentiles 2,5 et 97,5, angle par angle, des courbes de ses directions.
Écart déclaré : R9-bis lit ses enveloppes sur 40 différences aléatoires et 33 contrastives ; le pilote n'en balaie pas
de plus : son enveloppe de différences aléatoires est faite des directions dont un axe a été mesuré sur le
sous-ensemble 0 (au moins 18), et l'enveloppe à 40 et 33 directions de R9 est citée, si ses ancres A sont celles du
sous-ensemble 0 (même empreinte d'identifiants), quand R9 l'aura publiée. Rien de ce module n'entre dans une issue.
"""
from __future__ import annotations

import numpy as np

W_MIN_DEG, W_MAX_DEG = 2.0, 60.0


def masque_fenetre(angles_deg: np.ndarray) -> np.ndarray:
    a = np.asarray(angles_deg, dtype=np.float64)
    return (a >= W_MIN_DEG - 1e-9) & (a <= W_MAX_DEG + 1e-9)


def courbes_axes(grilles: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Courbes médianes sur les ancres des deux axes : (axe de d₁, axe de d₂)."""
    g = np.asarray(grilles, dtype=np.float64)
    return np.median(g[:, :, 0], axis=0), np.median(g[:, 0, :], axis=0)


def enveloppe(courbes: list[np.ndarray]) -> dict:
    c = np.stack(courbes)
    return {"mediane": np.median(c, axis=0).tolist(), "q025": np.percentile(c, 2.5, axis=0).tolist(),
            "q975": np.percentile(c, 97.5, axis=0).tolist(), "n": int(c.shape[0])}


def D(courbe: np.ndarray, courbes_reference: list[np.ndarray], angles_deg: np.ndarray) -> float:
    w = masque_fenetre(angles_deg)
    med = np.median(np.stack(courbes_reference), axis=0)
    return float(np.mean((np.asarray(courbe) - med)[w]))


def lecture(courbes_x: dict[str, np.ndarray], courbes_rd: dict[str, np.ndarray], angles_deg: np.ndarray) -> dict:
    """Pour chaque direction lue : D, part des différences aléatoires dont D est plus bas, angles de W où la courbe
    dépasse le percentile 97,5 de l'enveloppe des différences aléatoires (descriptif)."""
    ref = list(courbes_rd.values())
    if len(ref) < 3:
        return {"motif": f"{len(ref)} courbes de différences aléatoires sur le sous-ensemble 0 (au moins 3)"}
    w = masque_fenetre(angles_deg)
    env = enveloppe(ref)
    d_ref = {k: D(v, ref, angles_deg) for k, v in courbes_rd.items()}
    sortie = {"fenetre_deg": [W_MIN_DEG, W_MAX_DEG], "n_rd": len(ref), "enveloppe_rd": env, "D_rd": d_ref, "lus": {}}
    q975 = np.asarray(env["q975"])
    for k, v in courbes_x.items():
        dx = D(v, ref, angles_deg)
        sortie["lus"][k] = {"D": dx, "part_rd_sous": float(np.mean([x < dx for x in d_ref.values()])),
                            "angles_au_dessus_q975": [float(a) for a, x, q, m in zip(angles_deg, v, q975, w)
                                                      if m and x > q]}
    return sortie
