"""Grandeurs par pôle de la tranche B-α de « Neuron Lens », calculées par NOTRE code lisant `-causal.pt` — v1.

Pièce 3 du § 6 du devis B-α v2 (`docs/notes/neuron-lens-v1/devis-b-alpha/devis-tranche-b-alpha-v2.md`, `61c394f5…`, § 4, leçon 1,
M6) : le fichier `-causal.pt` (plusieurs Go) n'est pas versé ; sont versés son empreinte et, par pôle, r par lentille et par cible (matché
et témoin), recouvrement des 10 premiers, motif d'écart, neurone témoin, `top_doc`, `top_pos`, tirs, doses ; plus le centile commun du
témoin et n recalculé. **Aucune retouche de `score`** (une retouche serait un nœud de Lazar, m7) : ce module refait, pôle par pôle, le
calcul de `score` de `scripts/checks/causal_lens.py` (copie corrigée `a9d3bc8e…`, lignes 279 à 328), et **la garde de fidélité**
(`comparer_a_score`) exige que ses statistiques par couche égalent celles du JSON écrit par `score` (à une unité de la quatrième décimale) :
tout écart = arrêt, le brut n'est pas versé comme « grandeurs par pôle ».

Deux parties :
- `grandeurs(saved, lire, specs, nv, keep_vocab, f)` : pur (torch, aucun réseau, aucun modèle) ; `lire(couche, neurones, lentille)` rend
  la lecture `[len(neurones), nv]` de chaque écriture `W_down[:, n]` par la lentille (essayé dans le conteneur avec une lecture factice) ;
- `lecteur_voisin(model, specs)` : la lecture réelle, par les fonctions de la bibliothèque du dépôt voisin, exactement comme `score`
  (lignes 282 à 293 et 309 à 313) ; **ne tourne que sur la machine louée** (R-2710) ; sa garde est la fidélité au JSON de `score`.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from controle_ia.neuron_lens.verdicts_b_alpha_v3 import CIBLES, N_COUCHES, n_par_couche, random_neurons

PASS_Q = 0.99  # `causal_lens.py`, l. 61
DOSES = (1.0, 4.0)  # l. 60
CLES_STATS = ("r_q25", "r_med", "r_q75", "control_med", "overlap", "pass", "pass_control")
SANS_CONTEXTE, EFFET_NUL, RETENU = "sans contexte", "effet nul", "retenu"


def empreinte_fichier(chemin, bloc: int = 1 << 24) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as fh:
        while b := fh.read(bloc):
            h.update(b)
    return h.hexdigest()


def pearson(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Recopie de `neuron_lens.stats.pearson` (l. 33-37) : par ligne, sur les colonnes."""
    x = x - x.mean(-1, keepdim=True)
    y = y - y.mean(-1, keepdim=True)
    return (x * y).sum(-1) / (x.norm(dim=-1) * y.norm(dim=-1)).clamp_min(1e-12)


def overlap(a: torch.Tensor, b: torch.Tensor, k: int = 10) -> torch.Tensor:
    """Recopie de `overlap` de `causal_lens.py` (l. 268-270)."""
    ta, tb = a.topk(k, dim=1).indices, b.topk(k, dim=1).indices
    return torch.tensor([len(set(x.tolist()) & set(y.tolist())) / k for x, y in zip(ta, tb)])


def cibles(saved: dict) -> dict:
    """Les quatre cibles de `score` (l. 299-300), dans l'ordre de `CIBLES`."""
    t = {"steer 1x": saved["steer"][:, :, 0], "steer 4x": saved["steer"][:, :, 1],
         "ablate pos": saved["ablate_pos"], "ablate win": saved["ablate_win"]}
    assert tuple(t) == CIBLES
    return {k: torch.as_tensor(v) for k, v in t.items()}


def grandeurs(saved: dict, lire, specs, nv: int, keep_vocab: torch.Tensor, f: int) -> dict:
    """Refait `score` pôle par pôle. Rend {"poles": [...], "table": {...} (forme du JSON de `score`), "n": ..., "ecartes": ...}.
    Gardes : `keep_vocab` booléen de longueur `nv` ; lecture de forme `[len(neurones), nv]` et finie ; picks sans doublon ; n recalculé
    (`n_par_couche`, indépendant) égal au nombre de pôles retenus parmi les tirés au hasard, par couche et cible."""
    meta = saved["meta"]
    seed = meta.get("seed", 0)
    picks = [tuple(int(v) for v in p) for p in saved["picks"]]
    if len(set(picks)) != len(picks):
        raise ValueError("doublon dans picks")
    keep_vocab = torch.as_tensor(keep_vocab)
    if keep_vocab.dtype != torch.bool or keep_vocab.shape != (nv,):
        raise ValueError(f"keep_vocab : booléen de longueur nv = {nv} exigé, reçu {keep_vocab.dtype} {tuple(keep_vocab.shape)}")
    rand = set(random_neurons(N_COUCHES, f, meta["per_layer"], seed))
    targets = cibles(saved)
    fired_k = torch.as_tensor(saved["fired"])
    fired = (fired_k > 0).any(-1)  # l. 301
    alpha = torch.as_tensor(saved["alpha"], dtype=torch.float32)
    top_doc, top_pos = torch.as_tensor(saved["top_doc"]), torch.as_tensor(saved["top_pos"])
    poles, rows = {}, []
    for layer in sorted({l for l, _ in picks}):
        idx = [i for i, (l, _) in enumerate(picks) if l == layer]
        is_rand = torch.tensor([picks[i] in rand for i in idx])
        other = torch.arange(len(idx))
        for group in (is_rand, ~is_rand):
            other[group] = other[group].roll(1)
        for i_loc, i in enumerate(idx):
            for pi, signe in enumerate((1, -1)):
                poles[(i, pi)] = {
                    "couche": layer, "neurone": picks[i][1], "signe": signe, "aleatoire": bool(is_rand[i_loc]),
                    "temoin": picks[idx[int(other[i_loc])]][1], "alpha": round(alpha[i, pi].item(), 6),
                    "doses": [round(d * alpha[i, pi].item(), 6) for d in DOSES],
                    "top_doc": top_doc[i, pi].tolist(), "top_pos": top_pos[i, pi].tolist(),
                    "tirs": [round(float(v), 6) for v in fired_k[i, pi].tolist()], "lectures": {}}
        for s in specs:
            lg = torch.as_tensor(lire(layer, [picks[i][1] for i in idx], s), dtype=torch.float32)
            if lg.shape != (len(idx), nv) or not torch.isfinite(lg).all():
                raise ValueError(f"lecture de forme {tuple(lg.shape)} ou non finie (couche {layer}, {s}), attendu ({len(idx)}, {nv})")
            pred = torch.cat([lg, -lg])  # pôles +, −
            ctrl = torch.cat([lg[other], -lg[other]])
            for name, t in targets.items():
                y = torch.cat([t[idx, 0, :nv], t[idx, 1, :nv]]).to(torch.float32)
                steer = name.startswith("steer")
                contexte = torch.ones(len(y), dtype=torch.bool) if steer else torch.cat([fired[idx, 0], fired[idx, 1]])
                nonnul = y.abs().sum(1) > 0
                keep = contexte & nonnul
                pv, cv, yv = pred[:, keep_vocab], ctrl[:, keep_vocab], y[:, keep_vocab]
                r, rc, ov = pearson(pv, yv), pearson(cv, yv), overlap(pv, yv)
                k = keep & torch.cat([is_rand, is_rand])
                if k.any():
                    rows.append((layer, name, s, r[k], rc[k], ov[k]))
                for pi in (0, 1):
                    for j, i in enumerate(idx):
                        q = pi * len(idx) + j
                        motif = RETENU if keep[q] else (SANS_CONTEXTE if not contexte[q] else EFFET_NUL)
                        poles[(i, pi)]["lectures"].setdefault(name, {})[s] = (
                            {"r": round(r[q].item(), 6), "r_temoin": round(rc[q].item(), 6), "overlap": round(ov[q].item(), 4),
                             "motif": motif} if motif == RETENU else {"motif": motif})
    pooled = {}
    for _, name, s, _, rc, _ in rows:
        pooled.setdefault((name, s), []).append(rc)
    thr = {key: torch.cat(v).quantile(PASS_Q).item() for key, v in pooled.items()}
    stats = {(l, name, s): {"r_q25": r.quantile(0.25).item(), "r_med": r.median().item(), "r_q75": r.quantile(0.75).item(),
                            "control_med": rc.median().item(), "overlap": ov.mean().item(),
                            "pass": (r > thr[name, s]).float().mean().item(),
                            "pass_control": (rc > thr[name, s]).float().mean().item()}
             for l, name, s, r, rc, ov in rows}
    table = {name: {s: {"layer": [], "pass_threshold": round(thr[name, s], 4)} for s in specs if (name, s) in thr}
             for name in targets}
    for (l, name, s), st in stats.items():
        tt = table[name][s]
        tt["layer"].append(l)
        for key, v in st.items():
            tt.setdefault(key, []).append(round(v, 4))
    n, ecartes = n_par_couche(picks, rand, {c: targets[c].numpy() for c in CIBLES}, fired.numpy(), nv)
    for c in CIBLES:
        for s in specs:
            for l in range(N_COUCHES):
                nk = sum(1 for p in poles.values() if p["couche"] == l and p["aleatoire"]
                         and p["lectures"][c][s]["motif"] == RETENU)
                if nk != n[c][l]:
                    raise ValueError(f"n recalculé {n[c][l]} ≠ pôles retenus {nk} : {c}, {s}, couche {l}")
    return {"seed": seed, "nv": nv, "specs": list(specs), "f": f, "pass_q": PASS_Q,
            "centile_temoin": {f"{name}|{s}": round(v, 6) for (name, s), v in thr.items()},
            "poles": [poles[k] for k in sorted(poles)], "table": table, "n": n, "ecartes": ecartes}


def comparer_a_score(table: dict, score_json: dict, tol: float = 1e-4 + 1e-7) -> list[str]:
    """Garde de fidélité : nos statistiques par couche (`table`) contre le JSON écrit par `score` (`score_json["targets"]`). Rend la liste
    des écarts (vide = fidèle). Comparés : couches, seuil commun du témoin et les sept statistiques, à `tol` près : une unité de la
    quatrième décimale (arrondi de `score` ; une valeur à la frontière d'arrondi peut basculer), plus le bruit du flottant."""
    pb = []
    ref = score_json.get("targets")
    if not isinstance(ref, dict):
        return ["JSON de score sans « targets »"]
    if set(ref) != set(table):
        pb.append(f"cibles {sorted(table)} ≠ {sorted(ref)}")
    for name in sorted(set(ref) & set(table)):
        if set(ref[name]) != set(table[name]):
            pb.append(f"{name} : lentilles {sorted(table[name])} ≠ {sorted(ref[name])}")
        for s in sorted(set(ref[name]) & set(table[name])):
            a, b = table[name][s], ref[name][s]
            if list(a["layer"]) != list(b.get("layer", [])):
                pb.append(f"{name}, {s} : couches différentes")
                continue
            if abs(a["pass_threshold"] - b.get("pass_threshold", float("nan"))) > tol or "pass_threshold" not in b:
                pb.append(f"{name}, {s} : seuil {a['pass_threshold']} ≠ {b.get('pass_threshold')}")
            for key in CLES_STATS:
                va, vb = np.asarray(a[key], float), np.asarray(b.get(key, []), float)
                if va.shape != vb.shape or not np.all(np.abs(va - vb) <= tol):
                    pb.append(f"{name}, {s}, {key} : écart à score")
    return pb


def ecrire(chemin, resultat: dict, causal_sha256: str, score_sha256: str, ecarts: list[str]) -> None:
    """Écrit le JSON versé (tri des clés, une ligne) ; refuse d'écrire si la garde de fidélité a trouvé un écart (aucun repli)."""
    if ecarts:
        raise ValueError("garde de fidélité en échec : " + " ; ".join(ecarts[:5]))
    sortie = {"causal_sha256": causal_sha256, "score_json_sha256": score_sha256, "fidelite_a_score": "égale à une unité de la quatrième décimale"} | resultat
    Path(chemin).write_text(json.dumps(sortie, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def lecteur_voisin(model: str, specs, dev: str = "cpu"):
    """La lecture de `score` (l. 282-293, 309-313) par la bibliothèque du dépôt voisin. **Machine louée seulement** (R-2710).
    Rend (lire, nv, keep_vocab)."""
    from transformers import AutoTokenizer

    from neuron_lens import arch
    from neuron_lens.lenses import load_lens
    from neuron_lens.neurons import directions
    from neuron_lens.readout import rms_norm_columns, transport
    from neuron_lens.weights import tensors

    tok = AutoTokenizer.from_pretrained(model)
    nv = len(tok)
    keep_vocab = torch.load(arch.counts_path(model), weights_only=False)["counts"][:nv] >= 5
    nm = arch.names(model)
    head = tensors(model, sorted({nm["unembed"], nm["norm"]}))
    unembed = head[nm["unembed"]][:nv].to(dev, torch.float32)
    gamma = head[nm["norm"]].to(dev, torch.float32)
    lenses = {s: load_lens(s, model) for s in specs}
    cache = {}

    def lire(layer, neurones, s):
        if layer not in cache:
            cache.clear()
            cache[layer] = directions(model, layer, dev)["write"]
        cols = cache[layer][:, neurones]
        jac = None if lenses[s] is None else lenses[s].get(layer)
        return (unembed @ rms_norm_columns(transport(cols, jac), gamma)).T.cpu()

    return lire, nv, keep_vocab.cpu()
