"""Diagnostic de l'arrêt « contrôle carte-processeur » de la course B bis (linéaire à 300 époques, écart 1,004), essai v1.

**Processeur seulement, données fabriquées seulement** : aucune donnée de 7a ni de 7b, aucune activation, aucune sortie, aucun
score de la course, aucune aire de la course. Le code de la course est **appelé tel quel** (`t07bbis.apprentissage_carte_v1` :
`LotCarte`, `entrainer`, `scores`, `ecart_relatif` ; `sondes.familles.entrainer`, paquet gelé) ; rien n'est modifié.

Question : sans aucune erreur de chaîne, deux piles de calcul qui ne diffèrent **que par l'arrondi** peuvent-elles rendre, pour la
sonde linéaire agrégée par le maximum à 300 époques, des scores qui s'écartent de l'ordre de 1 (écart relatif du contrôle) ?
Et à quelle forme de données ?

Piles (même graine, mêmes réglages, mêmes données, même problème mathématique) :
- `carte` : `apprentissage_carte_v1.entrainer` sur un `LotCarte` de processeur (moyenne et écart type par torch, comme sur la
  carte) ;
- `ref` : `sondes.familles.entrainer` (paquet gelé ; moyenne et écart type par numpy) : la référence du contrôle de la course ;
- `permutee` : le paquet gelé sur les **mêmes actions dans un autre ordre** (permutation tirée) : même problème, seuls l'ordre
  des sommes sur les jetons (moyenne, perte, gradient) et donc l'arrondi changent ; c'est l'émulation, sans carte, d'« une autre
  pile » (sur la carte, les sommes des réductions sont faites dans un autre ordre que sur le processeur) ;
- `colonnes` : le paquet gelé sur les mêmes actions aux **dimensions permutées** (permutation tirée, rendue à la sonde après
  l'apprentissage) : même problème, seul l'ordre des sommes de chaque produit jeton·poids change (Adam agit dimension par
  dimension) ; émulation des produits de la carte (cuBLAS somme les 4 096 termes dans un autre ordre que le processeur).

Mesures : l'écart du contrôle (`ecart_relatif`, max |a − b| / max(|b|, 1)) sur des actions de contrôle tenues hors de
l'apprentissage, à 3 et à 300 époques ; deux définitions de repli de l'écart (rapportée à l'échelle globale max |b| ; rang de
Spearman) pour voir si l'écart vient du dénominateur ; l'aire (ROC) de chaque pile sur le contrôle ; la part des actions de
contrôle dont le jeton du maximum change entre piles.
Sous-commande `trajectoire` : boucle d'apprentissage **répliquée** (même suite d'opérations que `familles._entrainer` pour la
linéaire ; égalité au bit près avec `entrainer` et `familles.entrainer` vérifiée et écrite), jouée en même temps sur les deux
piles `carte` et `ref` : à chaque époque, écart relatif des poids, nombre d'actions d'apprentissage dont le jeton du maximum
diffère entre piles, plus petit écart entre le premier et le second jeton d'une action (quasi-égalités).

Jeux fabriqués (`--jeu`) :
- `repetition` : forme de la répétition sur carte (jetons N(0, I) en simple précision, décalage 0,5 le long d'une direction sur
  le premier quart des jetons des positifs) ;
- `residuel` : forme d'un flux résiduel, sans aucune donnée réelle : moyenne commune forte, covariance de rang faible à spectre
  en loi de puissance, composante propre à l'action, corrélation entre jetons voisins (processus autorégressif d'ordre 1,
  `--rho`), quelques dimensions « massives » sur le premier jeton de chaque action et sur 1 % des jetons (`--massif`),
  demi-précision (float16, comme les activations relues de 7b, `t06/lanceur_v2.ActivationsDemi`), signal `--decalage` sur une
  fenêtre d'un quart des jetons des positifs ; option `--gabarits` : une part des jetons de chaque action remplacée par des
  quasi-copies (bruit `--bruit-gabarit`, 10⁻³ par défaut, sous la résolution de la demi-précision à ces échelles) de cinq jetons communs à toutes les actions (forme des jetons de gabarit de conversation) ; option
  `--bruit` : écart type du bruit isotrope par dimension (0,3 par défaut ; plus grand : l'apprentissage peut apprendre par cœur) ;
  option `--puissance` : exposant du spectre de la covariance (0,8 par défaut ; 3 : une direction commune domine, forme des flux
  résiduels très anisotropes).
Sortie JSON (`--sortie`) écrite une fois (refus si le fichier existe, R12).

Graines (R9) : `numpy.random.SeedSequence(ENTROPIE, spawn_key=(cle_de_tache(clé),))` ; clés `diag-cp-v1/donnees/<jeu>/<suffixe>`,
`diag-cp-v1/sonde`, `diag-cp-v1/permutation` ; entropie fixe écrite ici (diagnostic non décisif).
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

ENTROPIE = 0x3C6EF372_FE94F82B_A54FF53A_5F1D36F1
PAS = 0.05


def graine(cle: str) -> np.random.SeedSequence:
    return np.random.SeedSequence(ENTROPIE, spawn_key=(cle_de_tache(cle),))


# ------------------------------------------------------------------------------------------------------------- jeux fabriqués

def jeu(nom: str, n_app: int, n_ctrl: int, d: int, lmin: int, lmax: int, decalage: float, rho: float, massif: float,
        suffixe: str = "", gabarits: float = 0.0, bruit: float = 0.3, puissance: float = 0.8,
        bruit_gabarit: float = 1e-3):
    """(séquences d'apprentissage, y, séquences de contrôle, y de contrôle) ; deux classes égales."""
    rng = np.random.default_rng(graine(f"diag-cp-v1/donnees/{nom}/{suffixe}"))
    u = rng.standard_normal(d)
    u /= np.linalg.norm(u)
    k = min(d, 64)
    spectre = 1.0 / np.arange(1, k + 1) ** float(puissance)
    A = rng.standard_normal((d, k)) * np.sqrt(spectre)[None, :] * 3.0
    m0 = rng.standard_normal(d) * 2.0
    massives = rng.choice(d, size=4, replace=False)
    modeles = m0[None, :] + rng.standard_normal((5, k)) @ A.T + bruit * rng.standard_normal((5, d))

    def action(pos: bool):
        n = int(rng.integers(lmin, lmax + 1))
        if nom == "repetition":
            x = rng.standard_normal((n, d))
            if pos:
                x[: max(1, n // 4)] += 0.5 * u
            return x.astype(np.float32)
        c = rng.standard_normal(k)
        z = np.empty((n, k))
        z[0] = rng.standard_normal(k)
        e = rng.standard_normal((n, k))
        for i in range(1, n):
            z[i] = rho * z[i - 1] + np.sqrt(1.0 - rho ** 2) * e[i]
        x = m0[None, :] + (c[None, :] + z) @ A.T + bruit * rng.standard_normal((n, d))
        if gabarits > 0:                              # jetons de gabarit : quasi-copies de cinq jetons communs à toutes les actions
            t = np.flatnonzero(rng.random(n) < gabarits)
            x[t] = modeles[rng.integers(0, 5, size=len(t))] + bruit_gabarit * rng.standard_normal((len(t), d))
        if massif > 0:
            x[0, massives] = massif * (1.0 + 0.05 * rng.standard_normal(len(massives)))
            t = rng.random(n) < 0.01
            x[np.ix_(t, massives)] = 0.3 * massif
        if pos and decalage:
            w = max(1, n // 4)
            a = int(rng.integers(0, n - w + 1))
            x[a:a + w] += decalage * np.sqrt(d) / 8.0 * u
        return x.astype(np.float16).astype(np.float32)

    y = np.r_[np.ones(n_app // 2, int), np.zeros(n_app - n_app // 2, int)]
    app = [action(bool(t)) for t in y]
    yc = np.array([1 if i % 2 == 0 else 0 for i in range(n_ctrl)])
    ctrl = [action(bool(t)) for t in yc]
    return app, y, ctrl, yc


# ------------------------------------------------------------------------------------------------------------------ mesures

def aire(scores, y) -> float:
    s, y = np.asarray(scores, float), np.asarray(y)
    p, n = s[y == 1], s[y == 0]
    return float(((p[:, None] > n[None, :]).sum() + 0.5 * (p[:, None] == n[None, :]).sum()) / (len(p) * len(n)))


def spearman(a, b) -> float:
    ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def argmax_jetons(sonde, seqs) -> np.ndarray:
    return np.array([int(np.argmax(sonde.scores_par_jeton(np.asarray(s)))) for s in seqs])


def comparer(sa, sb, ctrl, yc) -> dict:
    a, b = ac.scores(sa, ctrl), ac.scores(sb, ctrl)
    return {"ecart_controle": ac.ecart_relatif(a, b),
            "ecart_echelle_globale": float(np.max(np.abs(a - b)) / max(float(np.max(np.abs(b))), 1e-300)),
            "spearman": spearman(a, b), "aire_a": aire(a, yc), "aire_b": aire(b, yc),
            "max_abs_score_b": float(np.max(np.abs(b))), "mediane_abs_score_b": float(np.median(np.abs(b))),
            "part_jeton_du_max_change": float(np.mean(argmax_jetons(sa, ctrl) != argmax_jetons(sb, ctrl))),
            "ecart_w_relatif": float(np.max(np.abs(sa.w - sb.w)) / max(float(np.max(np.abs(sb.w))), 1e-300))}


def piles(app, y, ctrl, yc, l2: float, epoques: int, g: int, perm: np.ndarray) -> dict:
    lot = ac.LotCarte(app, "cpu")
    t0 = time.perf_counter()
    carte = ac.entrainer(lot, "lineaire", "diag", 15, y, l2, g, epoques=epoques)
    t1 = time.perf_counter()
    reg = fam.Reglages(l2=l2, epoques=epoques, pas=PAS)
    ref = fam.entrainer("lineaire", "diag", 15, list(app), np.asarray(y), "max", g, reg)
    permutee = fam.entrainer("lineaire", "diag", 15, [app[i] for i in perm], np.asarray(y)[perm], "max", g,
                             fam.Reglages(l2=l2, epoques=epoques, pas=PAS))
    pc = np.random.default_rng(graine("diag-cp-v1/colonnes")).permutation(app[0].shape[1])
    inv = np.argsort(pc)
    c = fam.entrainer("lineaire", "diag", 15, [np.ascontiguousarray(s[:, pc]) for s in app], np.asarray(y), "max", g,
                      fam.Reglages(l2=l2, epoques=epoques, pas=PAS))
    colonnes = fam.SondeLineaireJetons("diag", 15, "max", c.w[inv], c.b, None, "lineaire")
    return {"epoques": int(epoques), "l2": float(l2), "duree_carte_s": t1 - t0,
            "perte_ref": [j["perte"] for j in reg.journal],
            "carte_contre_ref": comparer(carte, ref, ctrl, yc),
            "permutee_contre_ref": comparer(permutee, ref, ctrl, yc),
            "colonnes_contre_ref": comparer(colonnes, ref, ctrl, yc)}


# ------------------------------------------------------------------------------------------------- boucle répliquée (traces)

def _etat(X, idx, n, y, l2):
    d = X.shape[1]
    w = torch.nn.Parameter(torch.zeros(d, dtype=torch.float64))
    b = torch.nn.Parameter(torch.zeros((), dtype=torch.float64))
    opt = torch.optim.Adam([w, b], lr=PAS)
    return {"X": X, "idx": idx, "n": n, "cible": torch.tensor(np.asarray(y, dtype=np.float64)), "w": w, "b": b, "opt": opt,
            "l2": float(l2), "bce": torch.nn.BCEWithLogitsLoss()}


def _pas(e):
    """Un pas, même suite d'opérations que `familles._entrainer` (linéaire, maximum) ; rend les scores par jeton d'avant le pas."""
    e["opt"].zero_grad()
    sj = e["X"] @ e["w"] + e["b"]
    out = torch.full((e["n"],), -torch.inf, dtype=sj.dtype)
    sa = out.scatter_reduce(0, e["idx"], sj, reduce="amax", include_self=True)
    perte = e["bce"](sa, e["cible"]) + e["l2"] * (e["w"] ** 2).sum()
    perte.backward()
    e["opt"].step()
    return sj.detach()


def _jeton_du_max_et_ecart(sj, bornes):
    arg, ecarts = [], []
    s = sj.numpy()
    for a, z in bornes:
        v = s[a:z]
        o = np.argsort(v)
        arg.append(int(o[-1]))
        if len(v) > 1:
            ecarts.append(float(v[o[-1]] - v[o[-2]]) / max(abs(float(v[o[-1]])), 1.0))
    return np.array(arg), (min(ecarts) if ecarts else float("nan"))


def trajectoire(app, y, l2: float, epoques: int, g: int) -> dict:
    lot = ac.LotCarte(app, "cpu")
    torch.manual_seed(int(g))
    mu, s = fam._normalisation(app)
    Xr, idxr = fam._sacs(app, mu, s)
    pa = _etat(lot.X.clone(), lot.idx.clone(), lot.n, y, l2)
    pb = _etat(Xr, idxr, len(app), y, l2)
    bornes, a0 = [], 0
    for q in app:
        bornes.append((a0, a0 + len(q)))
        a0 += len(q)
    lignes = []
    for ep in range(int(epoques)):
        sja, sjb = _pas(pa), _pas(pb)
        arga, _ = _jeton_du_max_et_ecart(sja, bornes)
        argb, gap = _jeton_du_max_et_ecart(sjb, bornes)
        wa, wb = pa["w"].detach().numpy(), pb["w"].detach().numpy()
        lignes.append({"epoque": ep + 1, "ecart_w": float(np.max(np.abs(wa - wb)) / max(float(np.max(np.abs(wb))), 1e-300)),
                       "actions_jeton_du_max_different": int(np.sum(arga != argb)),
                       "plus_petit_ecart_relatif_premier_second": gap})
    # égalité au bit près de la réplique avec le code de la course et le paquet gelé
    lot2 = ac.LotCarte(app, "cpu")
    c = ac.entrainer(lot2, "lineaire", "diag", 15, y, l2, g, epoques=epoques)
    r = fam.entrainer("lineaire", "diag", 15, list(app), np.asarray(y), "max", g, fam.Reglages(l2=l2, epoques=epoques, pas=PAS))
    wa_brut = pa["w"].detach().numpy() / lot.s
    wb_brut = pb["w"].detach().numpy() / s
    return {"l2": float(l2), "epoques": int(epoques), "lignes": lignes,
            "replique_egale_au_bit": {"carte": bool(np.array_equal(wa_brut, c.w)), "ref": bool(np.array_equal(wb_brut, r.w))}}


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=("ecarts", "trajectoire"))
    p.add_argument("--jeu", required=True, choices=("repetition", "residuel"))
    p.add_argument("--app", type=int, default=640)
    p.add_argument("--ctrl", type=int, default=256)
    p.add_argument("--largeur", type=int, default=1024)
    p.add_argument("--lmin", type=int, default=40)
    p.add_argument("--lmax", type=int, default=120)
    p.add_argument("--decalage", type=float, default=1.0)
    p.add_argument("--rho", type=float, default=0.9)
    p.add_argument("--massif", type=float, default=300.0)
    p.add_argument("--gabarits", type=float, default=0.0)
    p.add_argument("--bruit", type=float, default=0.3)
    p.add_argument("--puissance", type=float, default=0.8)
    p.add_argument("--bruit-gabarit", type=float, default=1e-3)
    p.add_argument("--l2", type=float, nargs="+", default=[1e-3, 1e-2, 1e-1])
    p.add_argument("--epoques", type=int, nargs="+", default=[3, 300])
    p.add_argument("--fils", type=int, default=4)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    sortie = Path(a.sortie)
    if sortie.exists():
        print(f"{sortie} existe déjà (R12) : refus", file=sys.stderr)
        return 2
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(a.fils))
    t0 = time.time()
    app, y, ctrl, yc = jeu(a.jeu, a.app, a.ctrl, a.largeur, a.lmin, a.lmax, a.decalage, a.rho, a.massif,
                         gabarits=a.gabarits, bruit=a.bruit, puissance=a.puissance,
                         bruit_gabarit=a.bruit_gabarit)
    g = int(graine("diag-cp-v1/sonde").generate_state(1)[0])
    perm = np.random.default_rng(graine("diag-cp-v1/permutation")).permutation(len(app))
    doc = {"commande": a.commande, "jeu": a.jeu, "app": a.app, "ctrl": a.ctrl, "largeur": a.largeur,
           "longueurs": [a.lmin, a.lmax], "decalage": a.decalage, "rho": a.rho, "massif": a.massif, "gabarits": a.gabarits, "bruit": a.bruit,
           "puissance": a.puissance, "bruit_gabarit": a.bruit_gabarit,
           "fils": a.fils,
           "jetons_app": int(sum(len(s) for s in app)), "torch": torch.__version__, "numpy": np.__version__,
           "donnees": "fabriquées seulement", "resultats": []}
    for l2 in a.l2:
        if a.commande == "trajectoire":
            r = trajectoire(app, y, float(l2), max(a.epoques), g)
        else:
            r = [piles(app, y, ctrl, yc, float(l2), int(e), g, perm) for e in a.epoques]
        doc["resultats"].append(r)
        print(json.dumps(r if a.commande == "ecarts" else {**r, "lignes": r["lignes"][-1:]}), flush=True)
    doc["duree_s"] = time.time() - t0
    sortie.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
