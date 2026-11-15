"""Trajectoires époque par époque de l'apprentissage « attention » sous deux arrondis différents (complément de
`diagnostic-ecart-attention-carte-v1.py`, qui n'est pas modifié), v1. **Processeur seulement** ; données synthétiques de la
répétition seulement (mêmes graines) ; aucune aire.

Une trajectoire est le calcul de `sondes.familles._entrainer`, opération par opération (la référence pas à pas du premier
script, égale au paquet gelé au bit près), à partir de jetons réduits :
- `--normalisation numpy` : réduction du paquet gelé (`_normalisation`, `_sacs`, par les répliques économes égales au bit près) ;
- `--normalisation torch` : réduction du chemin v1 (`t07bbis.apprentissage_carte_v1.LotCarte` : moyenne et écart type par torch).
Le jeu d'instructions se choisit avant l'import de torch (`ATEN_CPU_CAPABILITY`, `MKL_ENABLE_INSTRUCTIONS`). Aux époques
relevées, les scores des 256 actions de contrôle de la répétition (boucle du harnais) sont écrits en `.npz` ; `comparer` rend
l'écart relatif du contrôle (max |a − b| / max(|b|, 1)) époque par époque entre deux trajectoires.

Sous-commandes : `trajectoire SORTIE.json --normalisation {numpy,torch} --famille F --npz F.npz` ;
`comparer SORTIE.json --travail DOSSIER`.
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


def cmd_trajectoire(x) -> dict:
    import numpy as np
    import torch
    from controle_ia.sondes import familles as fam
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    from controle_ia.t07bbis.commun_v1 import AGREGATION_DE, EPOQUES, PAS
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(x.fils))
    rep = d1._rep()
    seqs, y = rep.jeu_synthetique(x.actions, x.largeur, "bbis/repetition/donnees")
    g = d1._graine(rep, x.famille)
    agregation = AGREGATION_DE[x.famille]
    torch.manual_seed(g)
    if x.normalisation == "numpy":
        mu, s = d1.normalisation_econome(seqs)
        X, idx = d1.sacs_econome(seqs, mu, s)
    else:
        lot = ac.LotCarte(seqs, "cpu")
        X, idx, mu, s = lot.X, lot.idx, lot.mu, lot.s
    n, d = len(seqs), X.shape[1]
    del seqs
    cible = torch.tensor(np.asarray(y, dtype=np.float64))
    w = torch.nn.Parameter(torch.zeros(d, dtype=torch.float64))
    b = torch.nn.Parameter(torch.zeros((), dtype=torch.float64))
    params = [w, b]
    q = None
    if agregation == "attention":
        q = torch.nn.Parameter(torch.randn(d, dtype=torch.float64) * 0.01)
        params.append(q)
    opt = torch.optim.Adam(params, lr=PAS)
    bce = torch.nn.BCEWithLogitsLoss()
    ctrl, _ = rep.jeu_synthetique(256, x.largeur, "bbis/repetition/controle")

    def sonde():
        wn = w.detach().numpy()
        w_brut = wn / s
        qn = q.detach().numpy() if q is not None else None
        return fam.SondeLineaireJetons("s", 15, agregation, w_brut, float(b.detach()) - float(mu @ w_brut),
                                       (qn / s) if qn is not None else None, x.famille)

    releves = {}
    t0 = time.perf_counter()
    for e in range(EPOQUES):
        opt.zero_grad()
        sj = X @ w + b
        lj = X @ q if q is not None else None
        sa = fam._agreger(sj, lj, idx, n, agregation)
        perte = bce(sa, cible) + d1.L2 * (w ** 2).sum()
        perte.backward()
        opt.step()
        if e in d1.EPOQUES_RELEVEES:
            releves[f"e{e}"] = ac.scores(sonde(), ctrl)
    np.savez(x.npz, **releves)
    f = sonde()
    return {"famille": x.famille, "normalisation": x.normalisation, "graine": g, "duree_s": time.perf_counter() - t0,
            "npz": Path(x.npz).name, "epoques_relevees": list(d1.EPOQUES_RELEVEES),
            "empreinte_parametres_finale": d1._empreinte_sonde(f.w, f.b, f.q), "instruction": d1._instruction(),
            "script": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def cmd_comparer(x) -> dict:
    import numpy as np
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    trav = Path(x.travail)
    parts = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(trav.glob("traj-*.json"))}
    paires = [("traj-attention-numpy-avx2", "traj-attention-numpy", "même calcul (paquet gelé), autre jeu d'instructions"),
              ("traj-attention-torch", "traj-attention-numpy", "réduction par torch (chemin v1) contre réduction par numpy "
                                                              "(paquet gelé), même jeu d'instructions")]
    sortie = {"parties": parts, "comparaisons": []}
    for a, b, quoi in paires:
        if a not in parts or b not in parts:
            sortie["comparaisons"].append({"a": a, "b": b, "absent": True})
            continue
        za, zb = np.load(trav / parts[a]["npz"]), np.load(trav / parts[b]["npz"])
        sortie["comparaisons"].append({"a": a, "b": b, "quoi": quoi, "ecart_controle_par_epoque": [
            {"epoque": int(k[1:]), "pas_faits": int(k[1:]) + 1, "ecart": ac.ecart_relatif(za[k], zb[k])}
            for k in sorted(zb.files, key=lambda k: int(k[1:]))]})
    Path(x.sortie).write_text(json.dumps(sortie, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return {"sortie": x.sortie}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("commande", choices=["trajectoire", "comparer"])
    ap.add_argument("sortie")
    ap.add_argument("--actions", type=int, default=640)
    ap.add_argument("--largeur", type=int, default=4096)
    ap.add_argument("--fils", type=int, default=4)
    ap.add_argument("--normalisation", choices=["numpy", "torch"], default="numpy")
    ap.add_argument("--famille", choices=["lineaire", "attention"], default="attention")
    ap.add_argument("--npz")
    ap.add_argument("--travail")
    x = ap.parse_args(argv)
    r = cmd_trajectoire(x) if x.commande == "trajectoire" else cmd_comparer(x)
    if x.commande == "trajectoire":
        Path(x.sortie).write_text(json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n",
                                  encoding="utf-8")
    print(json.dumps(r, ensure_ascii=False, default=str)[:400])
    return 0


if __name__ == "__main__":
    sys.exit(main())
