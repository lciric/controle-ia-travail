"""Stabilité des scores et des aires des sondes « attention » (et « linéaire », témoin) sous des perturbations d'arrondi, v1
(question de la mère après `diagnostic-ecart-attention-carte-v1.md`, R-2902). **Processeur seulement** ; données synthétiques de la
répétition seulement (mêmes tirages, mêmes graines) ; jeu tenu à l'écart synthétique ; aucune donnée de 7a, 7b, T0.7 ou P3-bis.

Membres comparés, par famille (réglage de la répétition : couche 15, l2 = 10⁻³, 300 époques, pas 0,05) :
- **piles réelles** (sondes déjà apprises par `diagnostic-ecart-attention-carte-v1.py`, empreintes relues dans sa sortie scellée) :
  P0 paquet gelé (AVX-512, réduction numpy) ; P1 paquet gelé en AVX2 ; P2 chemin v1 (réduction torch) ;
- **colonnes** (sous-commande `colonnes`) : m = 11 trajectoires menées ensemble comme colonnes d'un même produit matriciel
  (le calcul de `sondes.familles._entrainer` colonne par colonne : perte logistique moyenne par colonne, pénalité l2 par colonne,
  Adam élément par élément, donc sans couplage entre colonnes ; l'arithmétique des produits matriciels est celle de ce calcul,
  autre pile que P0, déclarée) : S0 sans perturbation ; U1 à U5 : **un seul arrondi au premier pas** (après le premier pas d'Adam,
  w[k] remplacé par le flottant suivant, k tiré) ; R1 à R5 : **perturbation de la taille d'un écart de piles au premier pas**
  (après le premier pas, w ← w·(1 + 10⁻¹⁰·ξ), ξ gaussien tiré : l'écart du contrôle entre deux piles réelles après un pas est de
  1,4·10⁻¹⁰ à 2,8·10⁻¹⁰, `diagnostic-trajectoires-attention-carte-v1-sortie.json`).
- **jeu tenu à l'écart** : 640 actions synthétiques **de la même loi que l'apprentissage** (même direction u que le jeu
  `bbis/repetition/donnees`, relue par le même tirage ; bruit et longueurs tirés sous la clé `bbis/repetition/tenu-a-l-ecart`) ;
  les actions de contrôle de la répétition (autre direction u) ne conviennent pas à une aire.

Mesures (sous-commande `evaluer`) : par paire (membre, référence) : écart du contrôle max |a − b| / max(|b|, 1), écart absolu
médian des scores, corrélation de rangs de Spearman, écart d'aire ; par groupe : aires, étendue, écart type (ddof 1) ; erreur type
d'échantillonnage de l'aire sur ce jeu (Hanley et McNeil 1982), pour l'échelle seulement. Graines (R9) : SeedSequence de l'entropie
fixe de la répétition, clés `bbis/repetition/tenu-a-l-ecart`, `bbis/repetition/stabilite/perturbations/<famille>`.

Sous-commandes : `colonnes SORTIE.json --famille F --npz F.npz` ; `evaluer SORTIE.json --travail DOSSIER --diagnostic D.json`.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("diagnostic_ecart_attention_carte_v1", ICI / "diagnostic-ecart-attention-carte-v1.py")
d1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(d1)

M_ULP, M_REL, REL = 5, 5, 1e-10


def _agreger2d(S, L, idx, n, agregation):
    """`sondes.familles._agreger` colonne par colonne (maximum ou attention ; jamais la moyenne)."""
    import torch
    N, m = S.shape
    I = idx[:, None].expand(N, m).contiguous()
    if agregation == "max":
        return torch.full((n, m), -torch.inf, dtype=S.dtype).scatter_reduce(0, I, S, reduce="amax", include_self=True)
    M = torch.full((n, m), -torch.inf, dtype=L.dtype).scatter_reduce(0, I, L, reduce="amax", include_self=True)
    E = torch.exp(L - M[idx])
    Z = torch.zeros((n, m), dtype=E.dtype).index_add(0, idx, E)
    return torch.zeros((n, m), dtype=E.dtype).index_add(0, idx, E * S) / Z


def cmd_colonnes(x) -> dict:
    import numpy as np
    import torch
    from controle_ia.t07bbis.commun_v1 import AGREGATION_DE, EPOQUES, PAS
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(x.fils))
    rep = d1._rep()
    seqs, y = rep.jeu_synthetique(x.actions, x.largeur, "bbis/repetition/donnees")
    g = d1._graine(rep, x.famille)
    agregation = AGREGATION_DE[x.famille]
    torch.manual_seed(g)
    mu, s = d1.normalisation_econome(seqs)
    X, idx = d1.sacs_econome(seqs, mu, s)
    n, d = len(seqs), X.shape[1]
    del seqs
    m = 1 + M_ULP + M_REL
    rng = np.random.default_rng(rep._graine(f"bbis/repetition/stabilite/perturbations/{x.famille}"))
    k_ulp = [int(k) for k in rng.choice(d, size=M_ULP, replace=False)]
    xi = rng.standard_normal((d, M_REL))
    cible = torch.tensor(np.asarray(y, dtype=np.float64))[:, None].expand(n, m)
    W = torch.nn.Parameter(torch.zeros((d, m), dtype=torch.float64))
    B = torch.nn.Parameter(torch.zeros(m, dtype=torch.float64))
    params = [W, B]
    Q = None
    if agregation == "attention":
        q0 = torch.randn(d, dtype=torch.float64) * 0.01
        Q = torch.nn.Parameter(q0[:, None].repeat(1, m))
        params.append(Q)
    opt = torch.optim.Adam(params, lr=PAS)
    bce = torch.nn.BCEWithLogitsLoss(reduction="none")
    t0 = time.perf_counter()
    for e in range(EPOQUES):
        opt.zero_grad()
        S = X @ W + B
        L = X @ Q if Q is not None else None
        SA = _agreger2d(S, L, idx, n, agregation)
        perte = bce(SA, cible).mean(dim=0)
        total = perte.sum() + d1.L2 * (W ** 2).sum()
        total.backward()
        opt.step()
        if e == 0:
            with torch.no_grad():
                for j, k in enumerate(k_ulp, start=1):
                    W[k, j] = torch.nextafter(W[k, j], torch.tensor(np.inf, dtype=torch.float64))
                for j in range(M_REL):
                    W[:, 1 + M_ULP + j] *= torch.as_tensor(1.0 + REL * xi[:, j])
    Wn = W.detach().numpy()
    w_brut = Wn / s[:, None]
    b_brut = B.detach().numpy() - mu @ w_brut
    q_brut = Q.detach().numpy() / s[:, None] if Q is not None else np.zeros((0, m))
    np.savez(x.npz, w=w_brut, b=b_brut, q=q_brut)
    noms = ["S0"] + [f"U{j}" for j in range(1, M_ULP + 1)] + [f"R{j}" for j in range(1, M_REL + 1)]
    return {"famille": x.famille, "graine": g, "colonnes": noms, "k_un_arrondi": k_ulp, "relatif": REL,
            "perte_finale": perte.detach().numpy().tolist(), "duree_s": time.perf_counter() - t0, "npz": Path(x.npz).name,
            "instruction": d1._instruction(), "script": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def jeu_tenu_a_l_ecart(rep, n_actions: int, largeur: int):
    """Même loi que `jeu_synthetique(…, "bbis/repetition/donnees")` (même direction u), autres tirages."""
    import numpy as np
    u = np.random.default_rng(rep._graine("bbis/repetition/donnees")).standard_normal(largeur).astype(np.float32)
    u /= np.linalg.norm(u)
    rng = np.random.default_rng(rep._graine("bbis/repetition/tenu-a-l-ecart"))
    y = np.r_[np.ones(n_actions // 2, int), np.zeros(n_actions - n_actions // 2, int)]
    seqs = []
    for k in range(n_actions):
        n = int(rng.integers(rep.LONGUEURS[0], rep.LONGUEURS[1] + 1))
        x = rng.standard_normal((n, largeur), dtype=np.float32)
        if y[k]:
            x[: max(1, n // 4)] += 0.5 * u
        seqs.append(x)
    return seqs, y, u


def _se_aire(a, n1, n0):
    q1, q2 = a / (2 - a), 2 * a * a / (1 + a)
    return float(((a * (1 - a) + (n1 - 1) * (q1 - a * a) + (n0 - 1) * (q2 - a * a)) / (n1 * n0)) ** 0.5)


def cmd_evaluer(x) -> dict:
    import numpy as np
    from scipy.stats import spearmanr
    from controle_ia.sondes import familles as fam
    from controle_ia.sondes.evaluation import aire_sous_courbe
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    from controle_ia.t07bbis.commun_v1 import AGREGATION_DE
    rep = d1._rep()
    trav = Path(x.travail)
    diag = json.loads(Path(x.diagnostic).read_text(encoding="utf-8"))
    seqs, y, u = jeu_tenu_a_l_ecart(rep, x.actions, x.largeur)
    # contrôle de la direction : la première action (positive) du jeu d'apprentissage, refaite avec u, est celle de la répétition
    r0 = np.random.default_rng(rep._graine("bbis/repetition/donnees"))
    r0.standard_normal(x.largeur)
    n0_ = int(r0.integers(rep.LONGUEURS[0], rep.LONGUEURS[1] + 1))
    a0 = r0.standard_normal((n0_, x.largeur), dtype=np.float32)
    a0[: max(1, n0_ // 4)] += 0.5 * u
    egal_u = bool(np.array_equal(a0, rep.jeu_synthetique(2, x.largeur, "bbis/repetition/donnees")[0][0]))
    sortie = {"jeu_tenu_a_l_ecart": {"actions": len(seqs), "jetons": int(sum(len(q) for q in seqs)),
                                     "positifs": int(y.sum()), "u_egal_a_celui_de_l_apprentissage": egal_u},
              "familles": {}}
    for f in ("attention", "lineaire"):
        ag = AGREGATION_DE[f]
        membres = {}
        for nom, part in (("P0", f"gele-{f}"), ("P1", f"gele-{f}-avx2"), ("P2", f"v1-{f}")):
            z = np.load(trav / f"{part}.npz")
            q = z["q"] if z["q"].size else None
            sd = fam.SondeLineaireJetons("s", 15, ag, z["w"], float(z["b"][0]), q, f)
            emp = d1._empreinte_sonde(sd.w, sd.b, sd.q)
            if emp != diag["parties"][part]["empreinte_parametres"]:
                raise SystemExit(f"{part} : empreinte {emp} ≠ sortie scellée du diagnostic")
            membres[nom] = sd
        meta = json.loads((trav / f"colonnes-{f}.json").read_text(encoding="utf-8"))
        z = np.load(trav / meta["npz"])
        for j, nom in enumerate(meta["colonnes"]):
            q = z["q"][:, j] if z["q"].size else None
            membres[nom] = fam.SondeLineaireJetons("s", 15, ag, z["w"][:, j], float(z["b"][j]), q, f)
        sc = {nom: ac.scores(sd, seqs) for nom, sd in membres.items()}
        aires = {nom: aire_sous_courbe(v, y) for nom, v in sc.items()}

        def paire(a, b):
            return {"ecart_controle": ac.ecart_relatif(sc[a], sc[b]),
                    "ecart_absolu_median": float(np.median(np.abs(sc[a] - sc[b]))),
                    "spearman": float(spearmanr(sc[a], sc[b]).statistic), "ecart_aire": aires[a] - aires[b]}

        paires = {f"{a}-P0": paire(a, "P0") for a in ("P1", "P2", "S0")}
        paires.update({f"{a}-S0": paire(a, "S0") for a in meta["colonnes"][1:]})
        groupes = {"piles (P0, P1, P2, S0)": ["P0", "P1", "P2", "S0"],
                   "un arrondi au premier pas (S0, U1-U5)": ["S0"] + [c for c in meta["colonnes"] if c.startswith("U")],
                   "écart de piles au premier pas (S0, R1-R5)": ["S0"] + [c for c in meta["colonnes"] if c.startswith("R")],
                   "tous (13)": list(membres)}
        disp = {}
        for g, noms in groupes.items():
            v = np.array([aires[n] for n in noms])
            disp[g] = {"aires": {n: aires[n] for n in noms}, "etendue": float(v.max() - v.min()),
                       "ecart_type": float(v.std(ddof=1)), "moyenne": float(v.mean())}
        n1, n0 = int(y.sum()), int((1 - y).sum())
        sortie["familles"][f] = {"aires": aires, "paires": paires, "dispersion": disp,
                                 "erreur_type_echantillonnage_aire_P0": _se_aire(aires["P0"], n1, n0),
                                 "colonnes": {k: meta[k] for k in ("k_un_arrondi", "relatif", "perte_finale", "duree_s",
                                                                    "instruction", "script")}}
    sortie["script"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(x.sortie).write_text(json.dumps(sortie, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return {"sortie": x.sortie}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("commande", choices=["colonnes", "evaluer"])
    ap.add_argument("sortie")
    ap.add_argument("--actions", type=int, default=640)
    ap.add_argument("--largeur", type=int, default=4096)
    ap.add_argument("--fils", type=int, default=4)
    ap.add_argument("--famille", choices=["lineaire", "attention"], default="attention")
    ap.add_argument("--npz")
    ap.add_argument("--travail")
    ap.add_argument("--diagnostic")
    x = ap.parse_args(argv)
    r = cmd_colonnes(x) if x.commande == "colonnes" else cmd_evaluer(x)
    if x.commande == "colonnes":
        Path(x.sortie).write_text(json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n",
                                  encoding="utf-8")
    print(json.dumps(r, ensure_ascii=False, default=str)[:300])
    return 0


if __name__ == "__main__":
    sys.exit(main())
