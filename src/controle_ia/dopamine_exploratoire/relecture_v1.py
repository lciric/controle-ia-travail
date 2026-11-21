"""Relecture forcée des épisodes honnêtes du premier test des sondes (lot L-2), bloc de la course de l'étape 1
(GO-2026-11-21-49 ; plan de l'étape 2a, § 3 et § 5 ; devis de la relecture forcée, § 1 et § 4) — exploratoire.

Ce que fait la carte : relire, sans rien générer, des contextes DÉJÀ REBÂTIS au processeur (fichier de contextes scellé),
et garder les états aux couches 7, 15 et 23 au dernier jeton de l'énoncé (passage séparé, énoncé seul) et au dernier
jeton de chaque action. Aucune sonde n'est apprise ni lue ici, aucun score n'est calculé (arrêt 6 du devis).

Fichier de contextes (une ligne JSON par épisode, champs permis seulement) : `id`, `famille`, `etiquette` (« honnete »
exigé), `recompense` (0 ou 1, calculée par programme), `ids` (transcription entière, identifiants), `ids_enonce`
(l'énoncé seul : préfixe exact de `ids`), `positions` ([p_0, p_1, …, p_T] : p_0 = dernier jeton de l'énoncé =
len(ids_enonce) − 1, p_t = dernier jeton de l'action t), `textes_actions` (facultatif : pour la garde de position).

Gardes : étiquette autre que « honnete », identifiant hors de la liste de la mère, champ hors liste, couche hors 7, 15,
23 (et couches 1 à 5 refusées pour une source « épisode du programme »), positions non croissantes ou hors séquence,
énoncé qui n'est pas le préfixe de la transcription ; position : l'état au dernier jeton de l'énoncé, passage séparé,
égale celui de la passe entière à la tolérance près (0,05, relative au maximum) ; jeton lu au bout de chaque action =
dernier jeton du texte de l'action (si les textes sont donnés) ; deux passes sur les cinq premiers épisodes : états
égaux à 1e-3 près (même calcul : il doit se refaire à l'identique).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import verifier
from .etats_v1 import ecart_relatif, en_float16, etats_d_une_sequence, exiger_source
from .stockage_v1 import ecrire_lot, etat_lot

COUCHES_PERMISES = (7, 15, 23)
CHAMPS = {"id", "famille", "etiquette", "recompense", "ids", "ids_enonce", "positions", "textes_actions"}
OBLIGATOIRES = CHAMPS - {"textes_actions"}


def lire_contextes(chemin: Path, liste_ids: set[str] | None) -> tuple[list[dict], str]:
    sha = verifier(chemin)
    sortie, vus = [], set()
    for n, l in enumerate(Path(chemin).read_text(encoding="utf-8").splitlines(), 1):
        if not l.strip():
            continue
        e = json.loads(l)
        if set(e) - CHAMPS or OBLIGATOIRES - set(e):
            raise GardeArret(f"contextes ligne {n} : champs {sorted(set(e) ^ CHAMPS)} hors de la liste permise")
        if e["etiquette"] != "honnete":
            raise GardeArret(f"contextes ligne {n} : étiquette {e['etiquette']!r} — épisodes honnêtes seulement")
        if liste_ids is not None and e["id"] not in liste_ids:
            raise GardeArret(f"contextes ligne {n} : identifiant {e['id']!r} hors de la liste de la mère")
        if e["id"] in vus:
            raise GardeArret(f"contextes ligne {n} : identifiant en double")
        vus.add(e["id"])
        if e["recompense"] not in (0, 1):
            raise GardeArret(f"contextes ligne {n} : issue non binaire")
        ids, en, pos = e["ids"], e["ids_enonce"], e["positions"]
        if ids[:len(en)] != en or not en:
            raise GardeArret(f"contextes ligne {n} : l'énoncé n'est pas le préfixe de la transcription")
        if pos[0] != len(en) - 1 or any(b <= a for a, b in zip(pos, pos[1:])) or pos[-1] >= len(ids):
            raise GardeArret(f"contextes ligne {n} : positions non croissantes, hors séquence, ou p_0 ≠ fin de l'énoncé")
        sortie.append(e)
    if not sortie:
        raise GardeArret("aucun contexte")
    return sortie, sha


def exiger_couches_relecture(couches) -> list[int]:
    c = sorted(int(x) for x in couches)
    if not c or any(x not in COUCHES_PERMISES for x in c):
        raise GardeArret(f"couches {couches} : 7, 15, 23 seulement pour la relecture forcée")
    exiger_source(c, "episode-du-programme")
    return c


def exiger_dernier_jeton(decoupeur, ids: list[int], positions: list[int], textes) -> None:
    """Le jeton lu au bout de l'action t est le dernier du texte de l'action : le texte décodé jusqu'à p_t (inclus)
    finit par le texte de l'action, et pas jusqu'à p_t − 1."""
    if textes is None:
        return
    if len(textes) != len(positions) - 1:
        raise GardeArret("autant de textes que d'actions attendu")
    for t, (p, txt) in enumerate(zip(positions[1:], textes), 1):
        txt = txt.rstrip()
        if not txt:
            continue
        if not decoupeur.decoder(ids[:p + 1]).rstrip().endswith(txt) or \
                decoupeur.decoder(ids[:p]).rstrip().endswith(txt):
            raise GardeArret(f"garde de position : le jeton lu à l'action {t} n'est pas le dernier de son texte")


def relire(modele, decoupeur, chemin_contextes: Path, couches, dossier: Path, liste_ids: set[str] | None = None,
           tolerance: float = 0.05, n_double: int = 5, tolerance_double: float = 1e-3) -> dict:
    """Écrit `dossier/couche-LL.npy` (lignes concaténées, float16) et `couche-LL.index.json`, scellés ; rend un résumé."""
    couches = exiger_couches_relecture(couches)
    eps, sha = lire_contextes(chemin_contextes, liste_ids)
    finaux = {c: (Path(dossier) / f"couche-{c:02d}.index.json", Path(dossier) / f"couche-{c:02d}.npy") for c in couches}
    if all(etat_lot(fa) == "scelle" for _, fa in finaux.values()):
        return {"episodes": len(eps), "deja_fait": True}
    blocs = {c: [] for c in couches}
    ids_l, dec, lgs, ecarts, o = [], [], [], [], 0
    for k, e in enumerate(eps):
        exiger_dernier_jeton(decoupeur, e["ids"], e["positions"], e.get("textes_actions"))
        etats = etats_d_une_sequence(modele, e["ids"], couches)
        seul = etats_d_une_sequence(modele, e["ids_enonce"], couches)
        for c in couches:
            ec = ecart_relatif(etats[c][e["positions"][0]], seul[c][-1])
            if ec > tolerance:
                raise GardeArret(f"{e['id']}, couche {c} : énoncé seul ≠ passe entière (écart {ec:.3g}) : arrêt")
            ecarts.append(ec)
        if k < n_double:
            bis = etats_d_une_sequence(modele, e["ids"], couches)
            for c in couches:
                if ecart_relatif(bis[c], etats[c]) > tolerance_double:
                    raise GardeArret(f"{e['id']} : deux passes du même épisode diffèrent (couche {c}) : arrêt")
        for c in couches:
            ligne = np.concatenate([seul[c][-1:], etats[c][e["positions"][1:]]], axis=0)
            blocs[c].append(en_float16(ligne, f"{e['id']}, couche {c}"))
        ids_l.append(e["id"]); dec.append(o); lgs.append(len(e["positions"])); o += len(e["positions"])
    for c, (fi, fa) in finaux.items():
        idx = {"couche": c, "contextes_sha256": sha, "ids": ids_l, "decalages": dec, "longueurs": lgs, "lignes": o,
               "familles": [e["famille"] for e in eps], "recompenses": [int(e["recompense"]) for e in eps],
               "positions": "ligne 0 : dernier jeton de l'énoncé (énoncé seul) ; ligne t : dernier jeton de l'action t",
               "mode": "exploratoire"}
        texte = json.dumps(idx, ensure_ascii=False, sort_keys=True) + "\n"
        if etat_lot(fi) != "scelle":
            ecrire_lot(fi, lambda p, t=texte: p.write_text(t, encoding="utf-8"))
        if etat_lot(fa) != "scelle":
            tab = np.concatenate(blocs[c], axis=0)

            def _e(p, t=tab):
                with open(p, "wb") as f:
                    np.save(f, t, allow_pickle=False)
            ecrire_lot(fa, _e)
    return {"episodes": len(eps), "couches": couches, "ecart_position_max": float(max(ecarts)),
            "double_passe": min(n_double, len(eps)), "contextes_sha256": sha}
