"""Références publiées du papier 2606.24964, converties en tableaux sûrs (npz sans pickle) et en JSON.

Le code publié (MIT) verse ses caches en `pickle`. Un `pickle` non sûr exécute du code à la lecture : on ne le lit
jamais avec `pickle.load`. `LecteurRestreint` n'admet qu'une liste blanche de globaux (reconstruction de tableaux
numpy et de tenseurs) ; `torch.storage._load_from_bytes`, qui charge avec `weights_only=False`, est remplacé par un
chargement `weights_only=True`. Tout autre global lève.

Conversion (une fois, sur processeur, hors ligne) :
    python -I -B -m controle_ia.pilote_exposant_p.references convertir <clone de fsec-paper> <dossier de sortie>

Sorties : `grilles-publiees-v1.npz` (grilles par ancre de Llama-3.1-8B, couche 2), `directions-publiees-v1.npz`
(directions de différence de moyennes publiées, Llama-3.1-8B, couche 2) et `references-publiees-v1.json`
(provenance, empreintes des fichiers amont, valeurs publiées, valeurs recalculées marquées « calcul »).
"""
from __future__ import annotations

import hashlib
import io
import json
import pickle
import sys
from pathlib import Path

import numpy as np

COMMIT_AMONT = "a9355d4001500708a40a255bacfe559e6dc269c0"
DOSSIER = Path(__file__).resolve().parent / "references_publiees"
GRILLES = DOSSIER / "grilles-publiees-v1.npz"
DIRECTIONS = DOSSIER / "directions-publiees-v1.npz"
JSON_REF = DOSSIER / "references-publiees-v1.json"

# grilles converties : (clé npz, fichier amont sous results/sweeps_2d)
GRILLES_AMONT = {
    "wealth_gender": "sweep2d_llama_L2_Wealth__Gender_fineweb_60deg.pkl",
    "iso_000_001": "sweep2d_llama_L2_random_000__random_001_fineweb_60deg_dirrandom.pkl",
    "iso_002_003": "sweep2d_llama_L2_random_002__random_003_fineweb_60deg_dirrandom.pkl",
}
DIRECTIONS_GARDEES = ("Gender", "Wealth", "Formal", "Literary", "Age", "Tense", "Sentiment")

_PERMIS = {
    ("numpy.core.multiarray", "_reconstruct"), ("numpy._core.multiarray", "_reconstruct"),
    ("numpy", "ndarray"), ("numpy", "dtype"),
    ("numpy.core.multiarray", "scalar"), ("numpy._core.multiarray", "scalar"),
    ("collections", "OrderedDict"),
}


class LecteurRestreint(pickle.Unpickler):
    """Désérialise un pickle non sûr en n'admettant que les globaux de la liste blanche."""

    def find_class(self, module, name):
        import importlib

        if (module, name) in _PERMIS:
            if module.startswith("numpy.core"):
                module = module.replace("numpy.core", "numpy._core", 1)
            return getattr(importlib.import_module(module), name)
        if (module, name) == ("torch._utils", "_rebuild_tensor_v2"):
            import torch._utils

            return torch._utils._rebuild_tensor_v2
        if (module, name) == ("torch.storage", "_load_from_bytes"):
            import torch

            return lambda b: torch.load(io.BytesIO(b), weights_only=True)
        raise pickle.UnpicklingError(f"global refusé par la liste blanche : {module}.{name}")


def lire_pickle_restreint(chemin: str | Path):
    with open(chemin, "rb") as f:
        return LecteurRestreint(f).load()


def _sha(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def charger_grilles() -> dict[str, np.ndarray]:
    with np.load(GRILLES, allow_pickle=False) as z:
        return {k: z[k] for k in z.files}


def charger_directions() -> dict[str, np.ndarray]:
    with np.load(DIRECTIONS, allow_pickle=False) as z:
        return {k: z[k] for k in z.files}


def charger_json() -> dict:
    return json.loads(JSON_REF.read_text(encoding="utf-8"))


def convertir(depot_amont: str | Path, sortie: str | Path, B: int = 2000, entropie: int = 20261103) -> dict:
    """Lit les caches publiés par le lecteur restreint et écrit les références sûres. Rien n'est exécuté du dépôt
    amont : ses fichiers sont lus comme des données. `B` et `entropie` fixent le rééchantillonnage des ancres qui
    donne la tolérance du témoin positif (calcul sur données publiées)."""
    from .ajustement import ajuster_plan, bootstrap_ancres

    U = Path(depot_amont)
    S = U / "results" / "sweeps_2d"
    sortie = Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    meta, tableaux, sources = {}, {}, {}
    for cle, nom in GRILLES_AMONT.items():
        ch = S / nom
        d = lire_pickle_restreint(ch)
        tableaux[f"{cle}__l2"] = np.asarray(d["l2"], dtype=np.float32)
        tableaux[f"{cle}__angles_deg"] = np.asarray(d["angles_deg"], dtype=np.float64)
        sources[f"results/sweeps_2d/{nom}"] = _sha(ch)
        meta[cle] = {k: (v if not isinstance(v, (np.floating, np.integer)) else v.item())
                     for k, v in d.items() if k in ("anchor_norm_mean", "perturb_layer", "measure_layer", "model_full",
                                                     "direction_labels", "direction_signs", "n_anchors", "mode",
                                                     "chart", "parametrize_git_sha", "seed_anchors")}
        meta[cle]["direction_labels"] = list(meta[cle]["direction_labels"])
    np.savez_compressed(sortie / GRILLES.name, **tableaux)

    ch_dirs = U / "results" / "directions" / "dirs_llama_L2.pkl"
    b = lire_pickle_restreint(ch_dirs)
    sources["results/directions/dirs_llama_L2.pkl"] = _sha(ch_dirs)
    dirs = {n: b["directions"][n].float().numpy().astype(np.float32) for n in DIRECTIONS_GARDEES}
    np.savez_compressed(sortie / DIRECTIONS.name, **dirs)
    hachages = {n: b["prompt_set_hashes"][n] for n in DIRECTIONS_GARDEES}
    signes = {n: b["signs"][n] for n in DIRECTIONS_GARDEES}

    ch_iso = U / "results" / "directions" / "dirs_llama_L2_random.pkl"
    bi = lire_pickle_restreint(ch_iso)
    sources["results/directions/dirs_llama_L2_random.pkl"] = _sha(ch_iso)
    iso = np.stack([bi["directions"][f"random_{i:03d}"].float().numpy() for i in range(len(bi["directions"]))])
    iso_sha = hashlib.sha256(np.ascontiguousarray(iso, dtype=np.float32).tobytes()).hexdigest()

    ch_fits = U / "results" / "fits" / "fits_llama_L2_thrpair_exact.pkl"
    fits = lire_pickle_restreint(ch_fits)
    sources["results/fits/fits_llama_L2_thrpair_exact.pkl"] = _sha(ch_fits)
    cellule = fits[("Wealth", "Gender")][("1.0xT", 60.0)]
    ch_paires = U / "results" / "directions" / "ref_pairs_random.txt"
    paires_iso = [l.strip().split(",") for l in ch_paires.read_text().splitlines()[1:] if l.strip()]
    sources["results/directions/ref_pairs_random.txt"] = _sha(ch_paires)
    ch_audit = U / "results" / "thrpair_audit.md"
    sources["results/thrpair_audit.md"] = _sha(ch_audit)

    # calcul sur données publiées : ajustement de la grille Wealth × Gender et rééchantillonnage des 30 ancres
    g = tableaux["wealth_gender__l2"]
    ang = tableaux["wealth_gender__angles_deg"]
    a0 = ajuster_plan(ang, g)
    bs = bootstrap_ancres(ang, g, B=B, rng=np.random.default_rng(np.random.SeedSequence(entropie)))
    ps = np.array([x["p"] for x in bs])
    i1 = np.array([x["intercepts"][0] for x in bs])
    i2 = np.array([x["intercepts"][1] for x in bs])
    ok = np.isfinite(ps)
    ref = {
        "version": "references-publiees-v1",
        "depot_amont": "https://github.com/FranciscoHS/fsec-paper",
        "commit_amont": COMMIT_AMONT,
        "lecture": "lecteur restreint (liste blanche) ; aucun code amont exécuté",
        "sources_sha256": sources,
        "grilles": meta,
        "directions_hachages_invites": hachages,
        "directions_signes": signes,
        "isotropes_publies": {"n": int(iso.shape[0]), "d": int(iso.shape[1]), "graine_torch": int(bi.get("seed", 42)),
                              "sha256_float32": iso_sha, "paires_de_reference": paires_iso},
        "publie": {
            "wealth_gender_llama": {"p": float(cellule["p_median"]), "intercepts_deg": [float(x) for x in cellule["intercepts"]],
                                     "n_pts": int(cellule["n_pts"]), "residu": float(cellule["mean_radial_frac"]),
                                     "seuil_T": float(cellule["threshold"]),
                                     "source": "results/fits/fits_llama_L2_thrpair_exact.pkl, cellule ('1.0xT', 60.0)"},
            "llama_contrastives_audit": {"n": 318, "mediane": 2.502, "moyenne": 2.632, "ic95": [2.388, 2.897],
                                          "residu_median": 0.0110, "source": "results/thrpair_audit.md, ligne Model / llama-3.1-8b"},
        },
        "calcul": {
            "wealth_gender_llama_reajuste": {"p": float(a0["p"]), "intercepts_deg": [float(x) for x in a0["intercepts"]],
                                             "n_pts": int(a0["n_pts"]), "residu": float(a0["residu"])},
            "wealth_gender_llama_bootstrap_ancres": {
                "B": B, "entropie_seedsequence": entropie, "reussis": int(ok.sum()),
                "p_q025": float(np.percentile(ps[ok], 2.5)), "p_q975": float(np.percentile(ps[ok], 97.5)),
                "p_mediane": float(np.median(ps[ok])), "p_ecart_type": float(ps[ok].std(ddof=1)),
                "intercept1_q025_q975": [float(np.nanpercentile(i1, 2.5)), float(np.nanpercentile(i1, 97.5))],
                "intercept2_q025_q975": [float(np.nanpercentile(i2, 2.5)), float(np.nanpercentile(i2, 97.5))],
            },
        },
    }
    (sortie / JSON_REF.name).write_text(json.dumps(ref, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
                                        encoding="utf-8")
    return ref


def _main(argv: list[str]) -> int:
    if len(argv) == 3 and argv[0] == "convertir":
        ref = convertir(argv[1], argv[2])
        print(json.dumps(ref["calcul"], indent=1, ensure_ascii=False))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
