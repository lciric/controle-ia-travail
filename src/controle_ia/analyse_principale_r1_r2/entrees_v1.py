"""Entrées de l'analyse principale de R1-R2 et leurs gardes.

Fiche de réception (`fiche-reception-principale-r1-r2-v1`), écrite et scellée avant toute lecture : chemins et empreintes
des fichiers versés par le fournisseur, aucun nombre de résultat. Les clés lues dans les fichiers et les résultats du
fournisseur sont celles de son code scellé (commit 29bd8e2e : `runs_nuit/rejeu_activations_v1.py`,
`runs_nuit/juge_actions_v1.py`), recopiées ici comme constantes : aucun pointeur libre.

Refus d'intégrité (empreinte, clé, forme, alignement, verdict de fidélité autre que « conforme », activation non finie
sur une action éligible, score de juge hors de [0, 1], invite ou contexte du juge autres que les gelés) : `GardeArret`,
rien n'est lu. Les textes de P3 ne servent qu'à leur longueur en caractères (trait (4) de T) ; aucun texte n'est écrit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from ..analyse_blanche_noire.entrees import _identite_egale, exiger_empreinte, lire_json
from ..gardes import GardeArret
from ..manifeste import verifier_resultat
from ..scellement import empreinte, verifier
from . import constantes_v1 as K

CLES_FICHE = {"format", "redaction", "R1", "motif_R1", "R2", "motif_R2"}
CLES_ENTREE_R1 = {"moyenne", "maximum", "complement", "resultat"}
CLES_ENTREE_R2 = {"juge3b", "juge8b", "motif_juge8b"}
CLES_JUGE = {"fichier", "resultat"}


def _fichier(e, quoi):
    if not isinstance(e, dict) or set(e) != {"chemin", "sha256"}:
        raise GardeArret(f"fiche : entrée {quoi} hors de forme (chemin, sha256 attendus)")
    return e


def lire_fiche(racine: Path, chemin: str, scellee: bool) -> tuple[dict, str]:
    p = Path(racine) / chemin
    sha = verifier(p) if scellee else empreinte(p)
    f = lire_json(p)
    if not isinstance(f, dict) or set(f) != CLES_FICHE or f.get("format") != K.FORMAT_FICHE:
        raise GardeArret(f"fiche de réception {chemin} : clés ou format ≠ {K.FORMAT_FICHE}")
    if f["R1"] is None:
        if f["motif_R1"] not in K.MOTIFS_R1_NUL:
            raise GardeArret(f"fiche : R1 nul sans motif de la liste fermée {list(K.MOTIFS_R1_NUL)}")
    else:
        if f["motif_R1"] is not None:
            raise GardeArret("fiche : motif_R1 donné alors que R1 est livré")
        if not isinstance(f["R1"], dict) or set(f["R1"]) != CLES_ENTREE_R1:
            raise GardeArret("fiche : entrée R1 hors de forme")
        for k in CLES_ENTREE_R1:
            _fichier(f["R1"][k], f"R1.{k}")
    if f["R2"] is None:
        if f["motif_R2"] not in K.MOTIFS_R2_NUL:
            raise GardeArret(f"fiche : R2 nul sans motif de la liste fermée {list(K.MOTIFS_R2_NUL)}")
    else:
        if f["motif_R2"] is not None:
            raise GardeArret("fiche : motif_R2 donné alors que R2 est livré")
        r2 = f["R2"]
        if not isinstance(r2, dict) or set(r2) != CLES_ENTREE_R2:
            raise GardeArret("fiche : entrée R2 hors de forme")
        for nom in ("juge3b", "juge8b"):
            e = r2[nom]
            if e is None and nom == "juge3b":
                raise GardeArret("fiche : R2 livré sans le juge 3B")
            if e is not None:
                if not isinstance(e, dict) or set(e) != CLES_JUGE:
                    raise GardeArret(f"fiche : entrée R2.{nom} hors de forme")
                for k in CLES_JUGE:
                    _fichier(e[k], f"R2.{nom}.{k}")
        if (r2["juge8b"] is None) != (r2["motif_juge8b"] is not None) or (
                r2["juge8b"] is None and r2["motif_juge8b"] not in K.MOTIFS_J8_NUL):
            raise GardeArret("fiche : juge 8B nul sans motif fermé, ou motif donné avec le juge 8B livré")
    return f, sha


# --------------------------------------------------------------------------------------------- P3
def empreinte_identite(tableaux: dict) -> str:
    """Règle du fournisseur (`runs_nuit.alignement_v1.empreinte_identite`, commit 29bd8e2e), recopiée."""
    h = hashlib.sha256()
    for k in K.IDENTITE:
        a = np.asarray(tableaux[k])
        h.update(f"{k}/{a.shape}\n".encode("utf-8"))
        if a.dtype.kind in ("U", "S", "O"):
            h.update("\n".join(str(x) for x in a.tolist()).encode("utf-8"))
        else:
            h.update(np.ascontiguousarray(a.astype("<i8")).tobytes())
        h.update(b"\x00")
    return h.hexdigest()


def charger_p3(racine: Path) -> dict:
    """Chaîne scellée de P3 : résultats `resume`, `episodes-p3`, `sondes-figees` scellés et rattachés à leur manifeste ;
    `scores-p3.npz` et les textes d'empreintes égales à celles des résultats et à celles citées ; sondes G ; identité ;
    colonnes. Contrairement au chargeur de l'analyse secondaire, une action non notée (scores non finis) est permise :
    elle est exclue de tous les bras (règle du fournisseur)."""
    racine = Path(racine)
    d = racine / "diag" / K.RUN_P3
    res = {}
    for nom in ("resume", "sondes-figees", "episodes-p3"):
        if not (d / f"{nom}.json").exists():
            raise GardeArret(f"P3 : {nom}.json absent (R11)")
        res[nom] = verifier_resultat(racine, d / f"{nom}.json")["resultat"]
    if (d / "arret.json").exists():
        raise GardeArret("P3 : arret.json présent")
    ep, rs, sf = res["episodes-p3"], res["resume"], res["sondes-figees"]
    for cle, champ in (("scores", "scores_sha256"), ("textes", "textes_sha256")):
        if verifier(racine / ep[cle]) != ep[champ] or ep[champ] != rs[champ] or ep[champ] != K.EMPREINTES_P3[cle]:
            raise GardeArret(f"P3 : {ep[cle]} ≠ empreinte des résultats du run ou empreinte citée")
    if Path(ep["scores"]) != Path("donnees") / K.RUN_P3 / "scores-p3.npz" or \
            Path(ep["textes"]) != Path("donnees") / K.RUN_P3 / "textes-actions-p3.jsonl":
        raise GardeArret("P3 : chemins des données ≠ chemins attendus")
    with np.load(racine / ep["scores"], allow_pickle=False) as z:
        t = {k: z[k] for k in z.files}
    for k in K.IDENTITE + ("scores", "noms_sondes", "jetons_notes"):
        if k not in t:
            raise GardeArret(f"P3 : colonne {k} absente")
    n = t["episode"].shape[0]
    if any(t[k].shape != (n,) for k in K.IDENTITE) or t["scores"].shape[0] != n:
        raise GardeArret("P3 : tables de longueurs différentes")
    noms = t["noms_sondes"].tolist()
    for p in (K.SONDE_G, K.SONDE_G_ENJEUX):
        if p not in noms:
            raise GardeArret(f"P3 : sonde {p} absente des scores")
    src = {"tables": t, "principales": {c: sf["principales"][c] for c in ("tromperie", "enjeux")},
           "empreintes": {"scores": ep["scores_sha256"], "textes": ep["textes_sha256"]}}
    if src["principales"] != {"tromperie": K.SONDE_G, "enjeux": K.SONDE_G_ENJEUX}:
        raise GardeArret(f"sondes principales de P3 {src['principales']} ≠ G gelée ({K.SONDE_G}, {K.SONDE_G_ENJEUX})")
    if t["episode"].shape != (K.LIGNES,):
        raise GardeArret(f"P3 : {t['episode'].shape[0]} lignes ≠ {K.LIGNES}")
    if empreinte_identite(t) != K.IDENTITE_SHA256:
        raise GardeArret("P3 : empreinte des quatre tableaux d'identité ≠ empreinte citée par le fournisseur")
    for k in (K.COLONNE_C, K.COLONNE_COUT_T) + K.FORMES_COUT_T:
        if k not in t:
            raise GardeArret(f"P3 : colonne {k} absente")
    conditions = set(np.asarray(t["condition"]).astype(str).tolist())
    if conditions != set(K.CONDITIONS):
        raise GardeArret(f"P3 : conditions {sorted(conditions)} ≠ {list(K.CONDITIONS)}")
    return src


def longueurs_textes(racine: Path, tables: dict) -> np.ndarray:
    """Longueur en caractères (points de code) du champ `texte` de chaque ligne de `textes-actions-p3.jsonl`, aligné ligne
    à ligne sur l'identité de `scores-p3.npz` (règle du fournisseur) ; empreinte citée. Aucun texte n'est gardé."""
    p = Path(racine) / "donnees" / K.RUN_P3 / "textes-actions-p3.jsonl"
    if not p.is_file():
        raise GardeArret(f"{p} absent sur disque (R11) : trait (4) de T non calculable")
    if verifier(p) != K.EMPREINTES_P3["textes"]:
        raise GardeArret("textes de P3 : empreinte ≠ empreinte citée")
    n = tables["episode"].shape[0]
    L = np.zeros(n, dtype=np.int64)
    k = 0
    with open(p, encoding="utf-8") as f:
        for ligne in f:
            if not ligne.strip():
                continue
            if k >= n:
                raise GardeArret("textes de P3 : plus de lignes que d'actions")
            x = json.loads(ligne)
            for c in K.IDENTITE:
                v = int(tables[c][k]) if c == "pas" else str(tables[c][k])
                if x.get(c) != v:
                    raise GardeArret(f"textes de P3 : ligne {k}, {c} ≠ scores-p3.npz (ordre rompu)")
            if not isinstance(x.get("texte"), str):
                raise GardeArret(f"textes de P3 : ligne {k} sans champ texte")
            L[k] = len(x["texte"])
            k += 1
    if k != n:
        raise GardeArret(f"textes de P3 : {k} lignes pour {n} actions")
    return L


# --------------------------------------------------------------------------------------------- R1
def charger_r1(racine: Path, e: dict, tables: dict) -> dict:
    racine = Path(racine)
    res = verifier_resultat(racine, racine / e["resultat"]["chemin"])
    if empreinte(racine / e["resultat"]["chemin"]) != e["resultat"]["sha256"]:
        raise GardeArret("R1 : résultat du rejeu d'empreinte ≠ fiche")
    if Path(e["resultat"]["chemin"]).stem != K.RESULTAT_R1:
        raise GardeArret(f"R1 : résultat {e['resultat']['chemin']} ≠ {K.RESULTAT_R1}.json")
    r = res["resultat"]
    if r.get("verdict_fidelite") != "conforme":
        raise GardeArret(f"R1 : verdict de fidélité {r.get('verdict_fidelite')!r} ≠ « conforme » : rien n'est lu")
    if not isinstance(r.get("regle_repli_appliquee"), bool):
        raise GardeArret("R1 : regle_repli_appliquee absente ou non booléenne")
    if [int(c) for c in r.get("couches", [])] != list(K.COUCHES):
        raise GardeArret(f"R1 : couches {r.get('couches')} ≠ {list(K.COUCHES)}")
    if r.get("textes_sha256") != K.EMPREINTES_P3["textes"]:
        raise GardeArret("R1 : empreinte des textes rejoués ≠ textes de P3")
    if r.get("identite_sha256") != K.IDENTITE_SHA256:
        raise GardeArret("R1 : empreinte d'identité ≠ empreinte citée")
    fichiers = r.get("fichiers") or {}
    tableaux, communs = {}, None
    for cle, nom in K.FICHIERS_R1.items():
        if Path(e[cle]["chemin"]).name != nom:
            raise GardeArret(f"R1 : fichier {e[cle]['chemin']} ≠ {nom}")
        if fichiers.get(nom) != e[cle]["sha256"]:
            raise GardeArret(f"R1 : empreinte de {nom} déclarée par la fiche ≠ empreinte du résultat du rejeu")
        p = exiger_empreinte(racine, e[cle]["chemin"], e[cle]["sha256"], f"R1 {nom}")
        with np.load(p, allow_pickle=False) as z:
            z = {k: z[k] for k in z.files}
        for k in (K.TABLEAU_R1[cle],) + K.CLES_R1_COMMUNES:
            if k not in z:
                raise GardeArret(f"R1 {nom} : tableau {k} absent")
        _identite_egale(z, tables, f"R1 {nom}")
        a = z[K.TABLEAU_R1[cle]]
        if a.shape != (tables["episode"].shape[0], len(K.COUCHES), K.DIMENSION):
            raise GardeArret(f"R1 {nom} : forme {a.shape} inattendue")
        if communs is None:
            communs = {k: z[k] for k in K.CLES_R1_COMMUNES}
        elif any(not np.array_equal(communs[k], z[k], equal_nan=z[k].dtype.kind == "f") for k in K.CLES_R1_COMMUNES):
            raise GardeArret(f"R1 {nom} : tableaux communs ≠ ceux de {K.FICHIERS_R1['moyenne']}")
        tableaux[cle] = a
    if [int(c) for c in communs["couches"]] != list(K.COUCHES):
        raise GardeArret("R1 : tableau couches ≠ [7, 15, 23]")
    if not np.array_equal(np.asarray(communs["jetons_empan"]).astype(np.int64),
                          np.asarray(tables["jetons_notes"]).astype(np.int64)):
        raise GardeArret("R1 : jetons_empan ≠ jetons_notes de P3 (format du n° 330)")
    for k in ("fidele", "contexte_conforme", "conforme_longueur", "trajectoire_identique"):
        if communs[k].dtype != np.bool_:
            raise GardeArret(f"R1 : {k} non booléen")
    return {"tableaux": tableaux, "communs": communs, "resultat": r, "empreintes": {k: e[k]["sha256"] for k in e}}


def exiger_activations_finies(r1: dict, eligible: np.ndarray) -> None:
    """Activation non finie (ou hors de l'étendue du float16) sur une action éligible : arrêt (liste d'arrêt du
    fournisseur)."""
    for cle, a in r1["tableaux"].items():
        if not np.all(np.isfinite(a[eligible])):
            raise GardeArret(f"R1 {K.FICHIERS_R1[cle]} : activation non finie sur une action éligible")


# --------------------------------------------------------------------------------------------- R2
def charger_juge(racine: Path, e: dict, tables: dict, nom: str) -> dict:
    racine = Path(racine)
    res = verifier_resultat(racine, racine / e["resultat"]["chemin"])
    if empreinte(racine / e["resultat"]["chemin"]) != e["resultat"]["sha256"]:
        raise GardeArret(f"juge {nom} : résultat d'empreinte ≠ fiche")
    r = res["resultat"]
    fichier = K.FICHIERS_JUGES[nom]
    if Path(e["fichier"]["chemin"]).name != fichier or r.get("fichier") != fichier:
        raise GardeArret(f"juge {nom} : fichier ≠ {fichier}")
    if r.get("sha256") != e["fichier"]["sha256"]:
        raise GardeArret(f"juge {nom} : empreinte du fichier ≠ empreinte du résultat du juge")
    if r.get("invite_sha256") != K.INVITE_JUGE_SHA256:
        raise GardeArret(f"juge {nom} : invite ≠ invite gelée du fournisseur")
    if r.get("contexte") != K.CONTEXTE_JUGE:
        raise GardeArret(f"juge {nom} : contexte déclaré ≠ contexte gelé (énoncé et action seule)")
    if (r.get("juge") or {}).get("revision") != K.REVISIONS_JUGES[nom]:
        raise GardeArret(f"juge {nom} : révision du modèle ≠ révision citée")
    if r.get("bras_principal") != "specialise" or r.get("identite_sha256") != K.IDENTITE_SHA256:
        raise GardeArret(f"juge {nom} : bras principal ou identité ≠ gelés")
    p = exiger_empreinte(racine, e["fichier"]["chemin"], e["fichier"]["sha256"], f"juge {nom}")
    with np.load(p, allow_pickle=False) as z:
        z = {k: z[k] for k in z.files}
    for k in ("score", "score_generique", "anomalie", "anomalie_generique"):
        if k not in z:
            raise GardeArret(f"juge {nom} : tableau {k} absent")
    _identite_egale(z, tables, f"juge {nom}")
    sortie = {}
    for k in ("score", "score_generique"):
        s = np.asarray(z[k], dtype=np.float64)
        if s.shape != (tables["episode"].shape[0],) or not np.all(np.isfinite(s)) or s.min() < 0 or s.max() > 1:
            raise GardeArret(f"juge {nom} : {k} de forme inattendue, non fini ou hors de [0, 1]")
        sortie[k] = s
    sortie["anomalie"] = np.asarray(z["anomalie"]).astype(bool)
    sortie["anomalie_generique"] = np.asarray(z["anomalie_generique"]).astype(bool)
    sortie["empreintes"] = {"fichier": e["fichier"]["sha256"], "resultat": e["resultat"]["sha256"]}
    return sortie
