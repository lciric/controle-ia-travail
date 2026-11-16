"""Diagnostic de l'arrêt « contrôle carte-processeur » de la course B bis (linéaire à 300 époques, écart 1,004), v1.

**Processeur seulement, données fabriquées seulement** (aucune donnée de 7a ni de 7b, aucune activation, aucune sortie ; aucun
score de la course ; aucune aire). Le code de la course est **appelé tel quel** (`t07bbis.apprentissage_carte_v1` : `LotCarte`,
`entrainer`, `scores`, `ecart_relatif` ; `sondes.familles.entrainer`, paquet gelé) ; rien n'est modifié.

Deux « piles » de calcul sur le processeur, qui ne diffèrent que par l'arrondi (même graine, mêmes réglages, mêmes données) :
- pile 1 : `apprentissage_carte_v1.entrainer` sur un `LotCarte` de processeur (réduction par torch, comme sur la carte) ;
- pile 2 : `sondes.familles.entrainer` (paquet gelé, réduction par numpy) : la référence du contrôle.
Pile 3 (sensibilité propre) : le paquet gelé, pas d'Adam remplacé par le flottant suivant (0,05 → 0,05000000000000001).
Pile 4 (sensibilité à un écart de l'ordre de celui de la carte) : le paquet gelé, pas multiplié par (1 + `--perturbation-relative`,
10⁻⁹ par défaut ; l'écart carte-processeur de la linéaire à la répétition était de 1,95·10⁻⁸).
Mesure : `ecart_relatif` (max |a − b| / max(|b|, 1)) des scores des actions de contrôle (actions tenues hors de l'apprentissage),
comme `controle_carte_processeur`.

Jeux fabriqués (`--jeu`) :
- `repetition` : la forme de la répétition sur carte (jetons N(0, I) en simple précision, décalage 0,5 le long d'une direction sur
  le premier quart des jetons des positifs) ;
- `separable` : même forme, décalage fort (`--decalage`, 3 par défaut) : la sonde sépare presque parfaitement l'apprentissage ;
- `anisotrope` : jetons d'un modèle à facteurs (spectre en loi de puissance, décalage commun), demi-précision (float16) comme les
  activations relues de 7b (`t06/lanceur_v6.py`, « precision » : « float16 »), décalage `--decalage` ;
- `anisotrope-faible` : idem, décalage 0,5 ;
- `massif` : jetons N(0, I) en demi-précision, plus, sur une part `--fraction-massive` des jetons de chaque action (2 % par défaut, au moins un), quelques dimensions de très grande
  valeur (×`--massif`, 100 par défaut ; forme des « activations massives » des grands modèles de langue, sans aucune donnée réelle),
  décalage `--decalage` ;
- `correle` : jetons d'une action corrélés dans le temps (moyenne propre à l'action, d'échelle `--echelle-action`, plus un
  processus autorégressif d'ordre 1 de coefficient `--rho` le long des positions), demi-précision, décalage `--decalage` sur le
  premier quart des jetons des positifs : forme des flux résiduels (jetons voisins semblables, scores voisins), sans donnée réelle ;
- `rang-faible` : jetons d'un sous-espace de 32 dimensions plus un bruit de 10⁻³, demi-précision, décalage `--decalage`.

Sous-commandes :
- `ecart` : écart pile 1 contre pile 2 à `--epoques` époques, pour chaque régularisation de `--l2` ;
- `trajectoire` : écart aux époques 1, 2, 5, 10, 20, 50, 100, 200, 300 (apprentissages successifs de longueurs croissantes,
  même départ ; chaque apprentissage est complet et déterministe).
Sortie JSON (`--sortie`), écrite une fois (refus si le fichier existe, R12).

Graines (R9) : `numpy.random.SeedSequence(ENTROPIE, spawn_key=(cle_de_tache(clé),))`, clés `diag-cp/donnees/<jeu>`,
`diag-cp/sonde/<l2>` ; entropie fixe écrite ici (diagnostic non décisif).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

from controle_ia.manifeste import cle_de_tache
from controle_ia.sondes import familles as fam
from controle_ia.t07bbis import apprentissage_carte_v1 as ac

ENTROPIE = 0x6D1A6C0C_9E3779B9_7F4A7C15_2545F491
MASSIF = 100.0
FRACTION_MASSIVE = 0.02
RHO, ECHELLE_ACTION = 0.97, 1.0
PERTURBATION = 1e-9
EPOQUES_TRAJ = (1, 2, 5, 10, 20, 50, 100, 200, 300)


def graine(cle: str) -> np.random.SeedSequence:
    return np.random.SeedSequence(ENTROPIE, spawn_key=(cle_de_tache(cle),))


def jeu(nom: str, n_app: int, n_ctrl: int, d: int, lmin: int, lmax: int, decalage: float):
    """(sequences d'apprentissage, y, sequences de contrôle) ; classes égales ; contrôle tiré de la même loi (tâches « lues »)."""
    rng = np.random.default_rng(graine(f"diag-cp/donnees/{nom}"))
    u = rng.standard_normal(d)
    u /= np.linalg.norm(u)
    aniso = nom.startswith("anisotrope") or nom == "rang-faible"
    if aniso:
        k = min(d, 64)
        spectre = 1.0 / np.arange(1, k + 1) ** 1.0
        A = rng.standard_normal((d, k)) * np.sqrt(spectre)[None, :] * 3.0
        biais = rng.standard_normal(d) * 0.5
        biais[: max(1, d // 256)] += 20.0                          # quelques dimensions à grande valeur commune
        bruit = 0.05
        if nom == "rang-faible":
            A = rng.standard_normal((d, 32))
            biais = np.zeros(d)
            bruit = 1e-3
    massives = rng.choice(d, size=4, replace=False)
    dec = 0.5 if nom in ("repetition", "anisotrope-faible") else float(decalage)

    def action(pos: bool):
        n = int(rng.integers(lmin, lmax + 1))
        if aniso:
            x = (rng.standard_normal((n, A.shape[1])) @ A.T + biais + bruit * rng.standard_normal((n, d)))
        else:
            x = rng.standard_normal((n, d))
        if nom == "correle":
            e = rng.standard_normal((n, d))
            for i in range(1, n):
                e[i] = RHO * e[i - 1] + np.sqrt(1.0 - RHO ** 2) * e[i]
            x = ECHELLE_ACTION * rng.standard_normal(d)[None, :] + e
        if pos:
            x[: max(1, n // 4)] += dec * u * (np.sqrt(d) / 8.0 if aniso else 1.0)
        if nom == "massif":
            t = rng.choice(n, size=max(1, int(n * FRACTION_MASSIVE)), replace=False)
            x[np.ix_(t, massives)] = MASSIF * (1.0 + 0.1 * rng.standard_normal((len(t), len(massives))))
        demi = aniso or nom in ("massif", "correle")
        return x.astype(np.float16 if demi else np.float32).astype(np.float32)

    y = np.r_[np.ones(n_app // 2, int), np.zeros(n_app - n_app // 2, int)]
    app = [action(bool(t)) for t in y]
    ctrl = [action(bool(i % 2 == 0)) for i in range(n_ctrl)]
    return app, y, ctrl


def deux_piles(app, y, ctrl, l2: float, epoques: int, g: int) -> dict:
    lot = ac.LotCarte(app, "cpu")
    t0 = time.perf_counter()
    s1 = ac.entrainer(lot, "lineaire", "p1", 15, y, l2, g, epoques=epoques)
    t1 = time.perf_counter()
    s2 = fam.entrainer("lineaire", "p1", 15, list(app), np.asarray(y), "max", g, fam.Reglages(l2=l2, epoques=epoques, pas=0.05))
    t2 = time.perf_counter()
    s3 = fam.entrainer("lineaire", "p1", 15, list(app), np.asarray(y), "max", g,
                       fam.Reglages(l2=l2, epoques=epoques, pas=float(np.nextafter(0.05, 1.0))))
    s4 = fam.entrainer("lineaire", "p1", 15, list(app), np.asarray(y), "max", g,
                       fam.Reglages(l2=l2, epoques=epoques, pas=0.05 * (1.0 + PERTURBATION)))
    a, b = ac.scores(s1, ctrl), ac.scores(s2, ctrl)
    aa, bb = ac.scores(s1, app), ac.scores(s2, app)
    return {"epoques": int(epoques), "l2": float(l2), "ecart_controle": ac.ecart_relatif(a, b),
            "ecart_apprentissage": ac.ecart_relatif(aa, bb),
            "ecart_pas_plus_un_ulp": ac.ecart_relatif(ac.scores(s3, ctrl), b),
            "ecart_pas_relatif": ac.ecart_relatif(ac.scores(s4, ctrl), b),
            "ecart_w_relatif": float(np.max(np.abs(s1.w - s2.w)) / max(float(np.max(np.abs(s2.w))), 1e-300)),
            "max_abs_score_controle": float(np.max(np.abs(b))),
            "exactitude_apprentissage_pile2": float(np.mean((bb > np.median(bb)) == (y == 1))),
            "duree_s": [t1 - t0, t2 - t1]}


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=("ecart", "trajectoire"))
    p.add_argument("--jeu", required=True, choices=("repetition", "separable", "anisotrope", "anisotrope-faible", "massif",
                                                     "rang-faible", "correle"))
    p.add_argument("--app", type=int, default=320)
    p.add_argument("--ctrl", type=int, default=128)
    p.add_argument("--largeur", type=int, default=512)
    p.add_argument("--lmin", type=int, default=40)
    p.add_argument("--lmax", type=int, default=80)
    p.add_argument("--decalage", type=float, default=3.0)
    p.add_argument("--massif", type=float, default=100.0)
    p.add_argument("--rho", type=float, default=0.97)
    p.add_argument("--echelle-action", type=float, default=1.0)
    p.add_argument("--perturbation-relative", type=float, default=1e-9,
                   help="pile 4 : pas d'Adam multiplié par (1 + ce nombre), ordre des écarts carte-processeur de la répétition")
    p.add_argument("--fraction-massive", type=float, default=0.02, help="part des jetons massifs par action (au moins un)")
    p.add_argument("--l2", type=float, nargs="+", default=[1e-3, 1e-2, 1e-1])
    p.add_argument("--epoques", type=int, default=300)
    p.add_argument("--fils", type=int, default=4)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    sortie = Path(a.sortie)
    if sortie.exists():
        print(f"{sortie} existe déjà (R12) : refus", file=sys.stderr)
        return 2
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(a.fils))
    global MASSIF, FRACTION_MASSIVE, RHO, ECHELLE_ACTION, PERTURBATION
    MASSIF, FRACTION_MASSIVE = float(a.massif), float(a.fraction_massive)
    RHO, ECHELLE_ACTION, PERTURBATION = float(a.rho), float(a.echelle_action), float(a.perturbation_relative)
    app, y, ctrl = jeu(a.jeu, a.app, a.ctrl, a.largeur, a.lmin, a.lmax, a.decalage)
    doc = {"commande": a.commande, "jeu": a.jeu, "app": a.app, "ctrl": a.ctrl, "largeur": a.largeur, "longueurs": [a.lmin, a.lmax],
           "decalage": a.decalage, "massif": a.massif, "fraction_massive": a.fraction_massive, "rho": a.rho,
           "echelle_action": a.echelle_action, "perturbation_relative": a.perturbation_relative, "fils": a.fils, "jetons_app": int(sum(len(s) for s in app)), "torch": torch.__version__,
           "numpy": np.__version__, "resultats": []}
    for l2 in a.l2:
        g = int(graine(f"diag-cp/sonde/{l2}").generate_state(1)[0])
        eps = EPOQUES_TRAJ if a.commande == "trajectoire" else (int(a.epoques),)
        for e in eps:
            r = deux_piles(app, y, ctrl, float(l2), int(e), g)
            doc["resultats"].append(r)
            print(json.dumps(r), flush=True)
    sortie.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
