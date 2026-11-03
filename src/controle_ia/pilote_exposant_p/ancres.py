"""Réserve d'entrées FineWeb-edu de 5 jetons, au protocole du code publié (`src/data.py::load_fineweb_fixed_length`).

Protocole repris : `HuggingFaceFW/fineweb-edu`, configuration `sample-10BT`, lecture en flux, `shuffle(seed=42,
buffer_size=10000)`, découpe en jetons par lots de 1000 textes (`truncation=True, max_length=5`, jetons spéciaux
compris, donc BOS + 4 jetons), entrées d'au moins 5 jetons, prises dans l'ordre. Les 30 premières sont les ancres du
papier si le flux est le même ; la réserve des différences aléatoires est faite des 10 000 premières (le code publié
tire ses paires dans ces 10 000, ancres comprises ; repris tel quel).

Ici : ancres = les S × 30 premières entrées, en S sous-ensembles consécutifs de 30 (le sous-ensemble 0 est celui du
papier) ; réserve = les 10 000 premières. Révision du jeu de données figée par son empreinte de commit, relevée avant
la lecture et consignée.

Le mode jouet (`reserve_jouet`) ne lit rien en ligne : jetons tirés au hasard, pour les essais et la répétition.
"""
from __future__ import annotations

import hashlib

import numpy as np

JEU = "HuggingFaceFW/fineweb-edu"
CONFIGURATION = "sample-10BT"
GRAINE_MELANGE = 42
TAMPON = 10000
LONGUEUR = 5
TAILLE_LOT_TEXTES = 1000


def revision_du_jeu() -> str:
    from huggingface_hub import HfApi

    return HfApi().dataset_info(JEU).sha


def charger_reserve(tokenizer, n: int, revision: str, longueur: int = LONGUEUR) -> tuple[np.ndarray, list[str]]:
    """Rend (ids (n, longueur) int64, textes décodés des n entrées). Lève si le flux donne moins de n entrées."""
    from datasets import load_dataset

    ds = load_dataset(JEU, name=CONFIGURATION, split="train", streaming=True, revision=revision)
    ds = ds.shuffle(seed=GRAINE_MELANGE, buffer_size=TAMPON)
    ids: list[list[int]] = []
    lot: list[str] = []

    def vider():
        enc = tokenizer(lot, truncation=True, max_length=longueur, add_special_tokens=True, padding=False)
        for x in enc["input_ids"]:
            if len(x) >= longueur and len(ids) < n:
                ids.append(list(x[:longueur]))

    for ex in ds:
        lot.append(ex["text"])
        if len(lot) >= TAILLE_LOT_TEXTES:
            vider()
            lot = []
            if len(ids) >= n:
                break
    if lot and len(ids) < n:
        vider()
    if len(ids) < n:
        raise RuntimeError(f"flux {JEU} : {len(ids)} entrées de {longueur} jetons < {n} demandées")
    tableau = np.asarray(ids, dtype=np.int64)
    return tableau, [tokenizer.decode(x) for x in tableau]


def reserve_jouet(n: int, vocabulaire: int, rng: np.random.Generator, longueur: int = LONGUEUR, bos: int = 1) -> np.ndarray:
    ids = rng.integers(3, vocabulaire, size=(n, longueur), dtype=np.int64)
    ids[:, 0] = bos
    return ids


def empreinte_ids(ids: np.ndarray) -> str:
    return hashlib.sha256(np.ascontiguousarray(ids, dtype=np.int64).tobytes()).hexdigest()


def sous_ensembles(n_ancres_par: int, S: int) -> list[slice]:
    return [slice(s * n_ancres_par, (s + 1) * n_ancres_par) for s in range(S)]
