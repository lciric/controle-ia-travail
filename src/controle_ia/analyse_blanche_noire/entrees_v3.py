"""Entrées de la version 3 (copie corrigée de la version 2, contre-lecture 2) : fiche
`fiche-reception-blanche-noire-v3` (R1 en deux fichiers `…-moyenne.npz` et
`…-maximum.npz` ; R2 au format v1 du juge (`entrees.charger_juge`), ou nul avec un motif de la liste fermée
`MOTIFS_R2_NUL` : lecture « R1 seul » ; R4 au format de P3, parties génériques facultatives), et
fidélité indépendante à seuils bloquants (corrélation, pente, écart relatif médian, part hors de la tolérance déclarée
par le fournisseur, 0,02 × (1 + |score|)).

Intégrité (empreinte, clé, forme, alignement, `moyenne` non finie) : arrêt. `maximum` absent, illisible ou non fini :
seul le bras descriptif `i_max` n'est pas lu. Fidélité ratée : (i) et ses variantes ne sont pas lus.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import verifier_resultat
from ..scellement import verifier
from . import constantes as C
from . import constantes_v3 as C3
from .entrees import (POINTEURS_R1, POINTEURS_R2, _identite_egale, _faits, _sondes_legeres, charger_juge, charger_run,
                      exiger_empreinte, fidelite_fournisseur, lire_json)
from ..scellement import empreinte

CLES_FICHE = {"format", "redaction", "R1", "motif_R1", "R2", "motif_R2", "R4"}
POINTEURS_R1_V3 = POINTEURS_R1 | {"regle_repli"}     # point J : règle de repli du fournisseur (n° 246, écart 5)
CLES_R1 = {"moyenne", "maximum", "manifeste", "pointeurs"}
CLES_R2 = {"fichier", "manifeste", "pointeurs"}
CLES_R4 = {"run", "empreintes", "pointeur_dose", "activations", "juge"}


def lire_fiche_v3(racine: Path, chemin: str, scellee: bool) -> tuple[dict, str]:
    p = Path(racine) / chemin
    sha = verifier(p) if scellee else empreinte(p)
    f = lire_json(p)
    if not isinstance(f, dict) or set(f) != CLES_FICHE or f["format"] != C3.FORMAT_FICHE:
        raise GardeArret(f"fiche de réception {chemin} : clés ou format ≠ {C3.FORMAT_FICHE}")
    if f["R1"] is None and f["motif_R1"] not in C3.MOTIFS_R1_NUL:
        raise GardeArret(f"fiche : R1 nul sans motif de la liste fermée {list(C3.MOTIFS_R1_NUL)} (nœud de Lazar)")
    if f["R1"] is not None and f["motif_R1"] is not None:
        raise GardeArret("fiche : motif_R1 donné alors que R1 est livré")
    if f["R2"] is None and f["motif_R2"] not in C3.MOTIFS_R2_NUL:
        raise GardeArret(f"fiche : R2 nul sans motif de la liste fermée {list(C3.MOTIFS_R2_NUL)} (nœud de Lazar)")
    if f["R2"] is not None and f["motif_R2"] is not None:
        raise GardeArret("fiche : motif_R2 donné alors que R2 est livré")
    r4 = f["R4"]
    if r4 is not None and (not isinstance(r4, dict) or set(r4) != CLES_R4):
        raise GardeArret(f"fiche : entrée R4 hors de forme ({sorted(r4) if isinstance(r4, dict) else r4})")
    if r4 is not None and r4["juge"] is not None:
        raise GardeArret("fiche : R4.juge doit être null (R-1086 n'autorise le juge que sur les textes de P3)")
    for nom, e, cles, ptr in (("R1", f["R1"], CLES_R1, POINTEURS_R1_V3), ("R2", f["R2"], CLES_R2, POINTEURS_R2),
                              ("R4.activations", (r4 or {}).get("activations"), CLES_R1, POINTEURS_R1_V3),
                              ("R4.juge", (r4 or {}).get("juge"), CLES_R2, POINTEURS_R2)):
        if e is not None and (not isinstance(e, dict) or set(e) != cles or set(e["pointeurs"]) - ptr):
            raise GardeArret(f"fiche : entrée {nom} hors de forme")
    return f, sha


def charger_run_v3(racine: Path, run_id: str, empreintes_attendues: dict | None) -> dict:
    """P3 : chargeur v1 complet (empreintes citées). R4 : `resume` et `episodes-p3` scellés et rattachés, fichier des
    scores exigé ; scores par jeton, sondes figées et sondes légères facultatifs (sans eux : sondes génériques et
    identité de linéarité non disponibles sur R4, écrit)."""
    if empreintes_attendues is not None:
        return {**charger_run(racine, run_id, empreintes_attendues), "partiel": False}
    racine = Path(racine)
    d = racine / "diag" / run_id
    try:
        return {**charger_run(racine, run_id, None), "partiel": False}
    except GardeArret as e:
        if not (d / "resume.json").exists() or not (d / "episodes-p3.json").exists():
            raise
        motif_complet = str(e)
    rs = verifier_resultat(racine, d / "resume.json")["resultat"]
    ep = verifier_resultat(racine, d / "episodes-p3.json")["resultat"]
    if (d / "arret.json").exists():
        raise GardeArret(f"run {run_id} : arret.json présent")
    if verifier(racine / ep["scores"]) != ep["scores_sha256"] or ep["scores_sha256"] != rs["scores_sha256"]:
        raise GardeArret(f"run {run_id} : scores ≠ empreinte des résultats")
    with np.load(racine / ep["scores"], allow_pickle=False) as z:
        tables = {k: z[k] for k in z.files}
    for k in C.IDENTITE + ("cout", "jetons_notes") + C.TRAITS_BOOLEENS:
        if k not in tables:
            raise GardeArret(f"run {run_id} : colonne {k} absente")
    return {"run": run_id, "tables": tables, "jetons": None, "principales": None, "legeres": None,
            "empreintes": {"scores": ep["scores_sha256"]}, "resume": {}, "partiel": True,
            "motif_partiel": motif_complet}


def _charger_tableau(racine, entree, tables, cles, quoi):
    p = exiger_empreinte(racine, entree["chemin"], entree["sha256"], quoi)
    with np.load(p, allow_pickle=False) as z:
        z = {k: z[k] for k in z.files}
    for k in cles:
        if k not in z:
            raise GardeArret(f"{quoi} : tableau {k} absent")
    _identite_egale(z, tables, quoi)
    return z


def charger_activations_v3(racine: Path, entree: dict, source: dict) -> dict:
    tables = source["tables"]
    m = exiger_empreinte(racine, entree["manifeste"]["chemin"], entree["manifeste"]["sha256"],
                         "manifeste des activations")
    faits = _faits(lire_json(m), entree["pointeurs"])
    zm = _charger_tableau(racine, entree["moyenne"], tables, ("moyenne", "jetons_empan", "jetons_empan_rejeu", "fidele"),
                          "activations moyennes")
    n = tables["episode"].shape[0]
    forme = (n, len(C.COUCHES), C.DIMENSION)
    if zm["moyenne"].shape != forme or any(zm[k].shape != (n,) for k in ("jetons_empan", "jetons_empan_rejeu", "fidele")):
        raise GardeArret(f"activations moyennes : formes {zm['moyenne'].shape}, {zm['jetons_empan'].shape} ≠ {forme}")
    if not np.all(np.isfinite(zm["moyenne"])):
        raise GardeArret("activations moyennes : valeur non finie")
    if "textes_sha256" not in faits or faits["textes_sha256"] != source["empreintes"].get("textes",
                                                                                         faits.get("textes_sha256")):
        raise GardeArret("activations : empreinte des textes rejoués absente ou ≠ textes du run")
    if "couches" not in faits or [int(c) for c in faits["couches"]] != list(C.COUCHES):
        raise GardeArret(f"activations : couches déclarées {faits.get('couches')} ≠ {list(C.COUCHES)}")
    if not isinstance(faits.get("regle_repli"), bool):
        raise GardeArret("activations : règle de repli du fournisseur non déclarée (pointeur regle_repli, booléen exigé)")
    maximum, motif_max = None, None
    if entree["maximum"] is None:
        motif_max = "maxima non livrés"
    else:
        try:
            zx = _charger_tableau(racine, entree["maximum"], tables, ("maximum",), "activations maximales")
            if zx["maximum"].shape != forme or not np.all(np.isfinite(zx["maximum"])):
                raise GardeArret("activations maximales : forme inattendue ou valeur non finie")
            maximum = zx["maximum"]
        except Exception as e:           # le maximum ne sert qu'au descriptif i_max (C2, C17) : motif écrit, illisible compris
            motif_max = f"{type(e).__name__} : {e}"
    return {"moyenne": zm["moyenne"], "maximum": maximum, "motif_maximum": motif_max,
            "jetons_empan_rejeu": zm["jetons_empan_rejeu"], "fidele": np.asarray(zm["fidele"]).astype(bool),
            "jetons_empan": zm["jetons_empan"], "dtype": str(zm["moyenne"].dtype), "faits": faits,
            "empreintes": {"moyenne": entree["moyenne"]["sha256"], "manifeste": entree["manifeste"]["sha256"],
                           "maximum": None if entree["maximum"] is None else entree["maximum"]["sha256"]}}


def fidelite_independante_v3(acts: dict, source: dict) -> dict:
    """Empan égal (bloquant) ; identité de linéarité à la couche 15 pour les deux sondes principales du run (si ses
    scores par jeton sont gardés) : bloquante si corrélation < 0,95, pente hors de [0,95 ; 1,05], écart relatif médian
    > 0,02 ou plus de 5 % des actions hors de |a − b| ≤ 0,02 (1 + |a|) ; réserves en deçà. Cette moyenne de scores par
    jeton est une identité de contrôle, jamais un score de moniteur."""
    tables, jetons = source["tables"], source["jetons"]
    empan_egal = bool(np.array_equal(np.asarray(acts["jetons_empan"]).astype(np.int64),
                                     np.asarray(tables["jetons_notes"]).astype(np.int64)))
    sortie = {"empan_egal": empan_egal, "sondes": {}, "reserves": [], "identite_disponible": jetons is not None}
    motifs = [] if empan_egal else ["empan rejoué ≠ empan noté"]
    # point J (n° 246) : `jetons_empan` recopie la longueur de P3 ; la longueur réellement rejouée est `jetons_empan_rejeu`
    rej = acts.get("jetons_empan_rejeu")
    if rej is not None:
        part = float(np.mean(np.asarray(rej).astype(np.int64) != np.asarray(tables["jetons_notes"]).astype(np.int64)))
        sortie["part_longueur_rejouee_differente"] = part
        if part > C3.EMPAN_REJEU_DIFFERENT_MAX:
            motifs.append(f"longueur rejouée ≠ longueur notée pour {part:.3f} des actions (> {C3.EMPAN_REJEU_DIFFERENT_MAX})")
        elif part > 0:
            sortie["reserves"].append(f"longueur rejouée ≠ longueur notée pour {part:.3f} des actions (gardées : analyse "
                                      f"par épisodes entiers)")
    fid = acts.get("fidele")
    if fid is not None:
        part = float(np.mean(~np.asarray(fid).astype(bool)))
        sortie["part_non_fideles"] = part
        if part > C3.NON_FIDELES_MAX:
            motifs.append(f"{part:.3f} des actions non fidèles selon le fournisseur (> {C3.NON_FIDELES_MAX})")
        elif part > 0:
            sortie["reserves"].append(f"{part:.3f} des actions non fidèles selon le fournisseur (gardées : analyse par "
                                      f"épisodes entiers ; le fournisseur les exclut, écart déclaré)")
    if (acts.get("faits") or {}).get("regle_repli") is True:
        motifs.append("règle de repli du fournisseur appliquée : sa tolérance, la même qu'ici, ne distingue pas un contexte "
                      "faux ; l'identité de linéarité ne prouve plus rien")
    if jetons is None:
        sortie["reserves"].append("identité de linéarité non disponible (scores par jeton non gardés pour ce run)")
    else:
        j = C.COUCHES.index(C.COUCHE_FIDELITE)
        M = np.asarray(acts["moyenne"][:, j, :], dtype=np.float64)
        debut, longueur = jetons["debut"].astype(np.int64), jetons["longueur"].astype(np.int64)
        for k, p in enumerate(jetons["principales"].tolist()):
            L = source["legeres"][p]
            if L["couche"] != C.COUCHE_FIDELITE:
                raise GardeArret(f"sonde {p} : couche {L['couche']} ≠ {C.COUCHE_FIDELITE}")
            cumul = np.concatenate([[0.0], np.cumsum(jetons[f"scores_{k}"].astype(np.float64))])
            ok = longueur > 0
            a = ((cumul[debut + longueur] - cumul[debut]) / np.where(ok, longueur, 1))[ok]
            b = (M @ L["w"] + L["b"])[ok]
            r = float(np.corrcoef(a, b)[0, 1]) if a.std() > 0 and b.std() > 0 else float("nan")
            pente = float(np.polyfit(a, b, 1)[0]) if a.std() > 0 else float("nan")
            e = np.abs(a - b) / (1.0 + np.abs(a))
            hors = float(np.mean(e > C3.FIDELITE_TOLERANCE))
            med = float(np.median(e))
            sortie["sondes"][p] = {"correlation": r, "pente": pente, "ecart_relatif_median": med,
                                   "ecart_relatif_max": float(e.max()), "part_hors_tolerance": hors,
                                   "actions": int(a.size)}
            if not (r >= C.FIDELITE_CORRELATION_MIN):
                motifs.append(f"{p} : corrélation {r:.4f} < {C.FIDELITE_CORRELATION_MIN}")
            if not (C3.FIDELITE_PENTE_BLOQUANTE[0] <= pente <= C3.FIDELITE_PENTE_BLOQUANTE[1]):
                motifs.append(f"{p} : pente {pente:.4f} hors de {list(C3.FIDELITE_PENTE_BLOQUANTE)}")
            if not (med <= C3.FIDELITE_ECART_MEDIAN_MAX):
                motifs.append(f"{p} : écart relatif médian {med:.4f} > {C3.FIDELITE_ECART_MEDIAN_MAX}")
            if hors > C3.FIDELITE_PART_HORS_TOLERANCE_MAX:
                motifs.append(f"{p} : {hors:.3f} des actions hors de la tolérance {C3.FIDELITE_TOLERANCE} (1 + |a|)")
            if r < C.FIDELITE_CORRELATION_RESERVE:
                sortie["reserves"].append(f"fidélité approximative ({p}) : corrélation {r:.4f}")
            if not (C3.FIDELITE_PENTE_RESERVE[0] <= pente <= C3.FIDELITE_PENTE_RESERVE[1]):
                sortie["reserves"].append(f"fidélité approximative ({p}) : pente {pente:.4f}")
            if med > C3.FIDELITE_ECART_MEDIAN_RESERVE:
                sortie["reserves"].append(f"fidélité approximative ({p}) : écart relatif médian {med:.4f}")
            if hors > 0:
                sortie["reserves"].append(f"fidélité approximative ({p}) : {hors:.4f} des actions hors tolérance")
    if acts.get("maximum") is not None:
        mo = np.asarray(acts["moyenne"], dtype=np.float32)
        ma = np.asarray(acts["maximum"], dtype=np.float32)
        sous = float(np.mean(ma < mo - 2.0 ** -10 * (np.abs(mo) + 1e-6)))
        sortie["part_maximum_sous_moyenne"] = sous
        if sous > C.FIDELITE_MAX_SOUS_MOYENNE:
            sortie["reserves"].append(f"maximum sous la moyenne pour une part {sous:.2e} des entrées")
    sortie["ratee"] = bool(motifs)
    sortie["motif"] = " ; ".join(motifs) if motifs else None
    return sortie


def exiger_juge_3b(racine: Path, entree: dict, juge: dict) -> float | None:
    """Point J (n° 246) : le fichier lu est celui du juge 3B (le juge 8B, livré aussi, n'est pas lu), l'invite déclarée est
    l'invite gelée du fournisseur, le modèle est déclaré ; rend la part des actions en anomalie de masse (None si le
    tableau `anomalie` n'est pas livré)."""
    nom = Path(entree["fichier"]["chemin"]).name
    if nom != C3.FICHIER_JUGE:
        raise GardeArret(f"juge : fichier {nom} ≠ {C3.FICHIER_JUGE} (seul le juge 3B est lu, R-1086)")
    if juge["faits"].get("invite_sha256") != C3.INVITE_JUGE_SHA256:
        raise GardeArret("juge : invite déclarée ≠ invite gelée du fournisseur (prereg/R2-invite-juge-v1.md)")
    if "modele" not in juge["faits"]:
        raise GardeArret("juge : modèle non déclaré par la fiche (pointeur modele exigé)")
    with np.load(Path(racine) / entree["fichier"]["chemin"], allow_pickle=False) as z:
        return float(np.mean(np.asarray(z["anomalie"]).astype(bool))) if "anomalie" in z.files else None


__all__ = ["lire_fiche_v3", "charger_run_v3", "charger_activations_v3", "fidelite_independante_v3",
           "fidelite_fournisseur", "charger_juge", "_sondes_legeres"]
