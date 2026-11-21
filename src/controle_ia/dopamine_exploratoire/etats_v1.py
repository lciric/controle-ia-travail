"""États internes aux couches demandées, float16 sur disque, scellés par lot, reprise après coupure (exploratoire).

Convention des couches : la couche l est la sortie du l-ième bloc (numérotation à partir de 1), soit `hidden_states[l]`
de transformers (`hidden_states[0]` est le plongement ; pour le dernier bloc, le crochet lit la sortie avant la norme
finale, que `hidden_states` applique). Le papier ne dit pas sa convention (point ouvert pour l'étape 0).

États. Pour une invite de n jetons et une réponse de T jetons, l'état s_t (t = 0…T) est l'état interne au dernier jeton du
préfixe invite + t jetons de réponse, soit la position n − 1 + t. s_0 est le dernier jeton de l'énoncé (lecture de la
sonde, p. 4) ; s_0…s_T servent à l'objectif de différence temporelle (équations 8 et 9). Mode « trajectoire » : les T + 1
états ; mode « s0 » : le seul s_0.

Disque : `couche-LL/lot-NNNNN.index.json` (identifiants, décalages, longueurs, empreinte du lot de génération) écrit et
scellé AVANT `couche-LL/lot-NNNNN.npy` (lignes concaténées, float16) : l'index ne dépend que des générations, il se
recalcule à l'identique ; un tableau scellé n'est jamais réécrit. Tout état non fini après passage en float16 arrête.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import verifier
from .stockage_v1 import ecrire_lot, etat_lot, lire_jsonl

MODES = ("trajectoire", "s0")


def positions_etats(n_invite: int, n_reponse: int, mode: str) -> np.ndarray:
    if n_invite < 1 or n_reponse < 0:
        raise GardeArret(f"longueurs illisibles : invite {n_invite}, réponse {n_reponse}")
    if mode == "s0":
        return np.array([n_invite - 1])
    if mode == "trajectoire":
        return np.arange(n_invite - 1, n_invite + n_reponse)
    raise GardeArret(f"mode {mode!r} inconnu ({MODES})")


def exiger_couches(couches, n_blocs: int) -> list[int]:
    c = [int(x) for x in couches]
    if not c or len(set(c)) != len(c) or any(x < 1 or x > n_blocs for x in c):
        raise GardeArret(f"couches {couches} : distinctes, entre 1 et {n_blocs} attendues (sortie du bloc, avant la norme "
                         "finale)")
    return sorted(c)


def blocs_du_modele(modele):
    return modele.model.layers


def etats_d_une_sequence(modele, ids: list[int], couches: list[int], *, confiance: bool = False):
    """Une passe avant ; crochets sur les blocs demandés ; rend {couche: (longueur, d) float32}. Avec `confiance`, rend
    aussi la probabilité du jeton le plus probable après le DERNIER jeton (confiance par jeton du papier, p. 8)."""
    import torch

    blocs = blocs_du_modele(modele)
    pris, poignees = {}, []
    for l in couches:
        def crochet(_m, _e, sortie, l=l):
            h = sortie[0] if isinstance(sortie, tuple) else sortie
            pris[l] = h[0].detach().float().cpu().numpy()
        poignees.append(blocs[l - 1].register_forward_hook(crochet))
    try:
        appareil = next(modele.parameters()).device
        x = torch.tensor([ids], dtype=torch.long, device=appareil)
        with torch.no_grad():
            sortie = modele(input_ids=x, attention_mask=torch.ones_like(x), use_cache=False, logits_to_keep=1)
    finally:
        for p in poignees:
            p.remove()
    if set(pris) != set(couches):
        raise GardeArret(f"crochets : couches lues {sorted(pris)} ≠ demandées {couches}")
    if confiance:
        pmax = float(torch.softmax(sortie.logits[0, -1].float(), -1).max())
        return pris, pmax
    return pris


SOURCES = ("math500-public", "episode-du-programme")
COUCHES_BASSES_MAX = 5          # blocs 1 à 5 : données publiques seulement (brouillon v7, l. 129 ; plan 0-1, § B.3 point 4)


def exiger_source(couches, source: str) -> None:
    if source not in SOURCES:
        raise GardeArret(f"source {source!r} inconnue ({SOURCES})")
    basses = [c for c in couches if c <= COUCHES_BASSES_MAX]
    if basses and source != "math500-public":
        raise GardeArret(f"couches {basses} demandées sur une source « {source} » : les blocs 1 à 5 ne se lisent que sur "
                         "MATH500 public (GO-2026-11-21-06, point 3)")


def ecart_relatif(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.max(np.abs(a - b)) / (1.0 + float(np.max(np.abs(b)))))


def en_float16(a: np.ndarray, quoi: str) -> np.ndarray:
    b = a.astype(np.float16)
    if not np.isfinite(b).all():
        raise GardeArret(f"{quoi} : état non fini après passage en float16 (débordement) : arrêt, rien n'est écrit")
    return b


def extraire_par_lots(modele, dossier_generations: Path, couches, dossier_etats: Path, mode: str = "trajectoire",
                      source: str = "math500-public", tolerance_position: float = 0.05) -> dict:
    """Pour chaque lot de génération scellé, écrit les états de chaque couche. Reprise : lots complets sautés.
    Garde de position : l'état de s_0, recalculé sur l'invite seule, égale celui de la passe entière à la tolérance
    relative près ; la confiance par jeton (après l'invite seule) est écrite par lot (`confiance-jeton/`)."""
    n_blocs = len(blocs_du_modele(modele))
    couches = exiger_couches(couches, n_blocs)
    exiger_source(couches, source)
    lots_g = sorted(Path(dossier_generations).glob("lot-*.jsonl"))
    if not lots_g:
        raise GardeArret(f"aucun lot de génération sous {dossier_generations}")
    ecrits = sautes = 0
    for lg in lots_g:
        sha_g = verifier(lg)
        gens = lire_jsonl(lg)
        index = {}
        for l in couches:
            ids, decalages, longueurs, o = [], [], [], 0
            for g in gens:
                n = len(positions_etats(len(g["jetons_invite"]), len(g["jetons_reponse"]), mode))
                ids.append(g["id"]); decalages.append(o); longueurs.append(n); o += n
            index[l] = {"couche": l, "mode": mode, "lot_generation": lg.name, "lot_generation_sha256": sha_g,
                        "ids": ids, "decalages": decalages, "longueurs": longueurs, "lignes": o,
                        "convention": "sortie du bloc l, numérotation à partir de 1 (hidden_states[l])"}
        a_faire = []
        for l in couches:
            d = Path(dossier_etats) / f"couche-{l:02d}"
            fi, fa = d / f"{lg.stem}.index.json", d / f"{lg.stem}.npy"
            if etat_lot(fa) == "scelle":
                if etat_lot(fi) != "scelle" or json.loads(fi.read_text(encoding="utf-8")) != index[l]:
                    raise GardeArret(f"{fa} scellé sans index conforme : vérifier à la main (R11)")
                continue
            if etat_lot(fi) == "scelle":
                if json.loads(fi.read_text(encoding="utf-8")) != index[l]:
                    raise GardeArret(f"{fi} scellé mais différent de l'index recalculé : générations changées ?")
            else:
                texte = json.dumps(index[l], ensure_ascii=False, sort_keys=True, indent=1) + "\n"
                ecrire_lot(fi, lambda p, t=texte: p.write_text(t, encoding="utf-8"))
            a_faire.append(l)
        if not a_faire:
            sautes += 1
            continue
        blocs_par_couche = {l: [] for l in a_faire}
        confiances, ecarts = {}, {}
        for g in gens:
            ids = list(g["jetons_invite"]) + list(g["jetons_reponse"])
            pos = positions_etats(len(g["jetons_invite"]), len(g["jetons_reponse"]), mode)
            etats = etats_d_une_sequence(modele, ids, a_faire)
            seul, pmax = etats_d_une_sequence(modele, list(g["jetons_invite"]), [a_faire[0]], confiance=True)
            e = ecart_relatif(etats[a_faire[0]][pos[0]], seul[a_faire[0]][-1])
            if e > tolerance_position:
                raise GardeArret(f"{g['id']} : garde de position — s_0 de la passe entière ≠ s_0 de l'invite seule "
                                 f"(écart relatif {e:.3g} > {tolerance_position}) : arrêt, rien n'est écrit")
            confiances[g["id"]], ecarts[g["id"]] = pmax, e
            for l in a_faire:
                blocs_par_couche[l].append(en_float16(etats[l][pos], f"{g['id']}, couche {l}"))
        fc = Path(dossier_etats) / "confiance-jeton" / f"{lg.stem}.json"
        if etat_lot(fc) != "scelle":
            texte = json.dumps({"confiance_jeton": confiances, "ecart_position": ecarts,
                                "couche_de_la_garde": a_faire[0]}, sort_keys=True) + "\n"
            ecrire_lot(fc, lambda p, t=texte: p.write_text(t, encoding="utf-8"))
        for l in a_faire:
            tab = np.concatenate(blocs_par_couche[l], axis=0)
            if tab.shape[0] != index[l]["lignes"]:
                raise GardeArret(f"couche {l}, {lg.name} : {tab.shape[0]} lignes, {index[l]['lignes']} attendues")
            fa = Path(dossier_etats) / f"couche-{l:02d}" / f"{lg.stem}.npy"

            def _e(p, t=tab):
                with open(p, "wb") as f:
                    np.save(f, t, allow_pickle=False)
            ecrire_lot(fa, _e)
        ecrits += 1
    return {"lots_ecrits": ecrits, "lots_sautes": sautes, "couches": couches, "mode": mode, "source": source}


def charger_couche(dossier_etats: Path, couche: int) -> dict[str, np.ndarray]:
    """{identifiant: (T + 1, d) float16} pour une couche ; empreintes vérifiées, tableaux en lecture seule (mmap)."""
    d = Path(dossier_etats) / f"couche-{int(couche):02d}"
    indexes = sorted(d.glob("lot-*.index.json"))
    if not indexes:
        raise GardeArret(f"aucun état pour la couche {couche} sous {dossier_etats}")
    sortie = {}
    for fi in indexes:
        verifier(fi)
        idx = json.loads(fi.read_text(encoding="utf-8"))
        fa = fi.with_name(fi.name.replace(".index.json", ".npy"))
        verifier(fa)
        tab = np.load(fa, mmap_mode="r", allow_pickle=False)
        if tab.dtype != np.float16 or tab.shape[0] != idx["lignes"]:
            raise GardeArret(f"{fa.name} : type {tab.dtype} ou {tab.shape[0]} lignes, float16 et {idx['lignes']} attendus")
        for i, o, n in zip(idx["ids"], idx["decalages"], idx["longueurs"]):
            if i in sortie:
                raise GardeArret(f"{i} en double dans les états de la couche {couche}")
            sortie[i] = tab[o:o + n]
    return sortie
