"""Entrées de l'analyse et leurs gardes : fiche de réception, run au format de P3 (chaîne scellée), activations rejouées
(R1), scores du juge de 3 milliards (R2), seconde dose (R4) ; contrôles de fidélité du rejeu.

Deux sortes de refus :
- **intégrité** (empreinte discordante, clé ou forme absente, identité des lignes désalignée, valeur hors domaine ou
  non finie, pointeur de la fiche qui ne se résout pas) : `GardeArret`, l'analyse entière s'arrête ;
- **fidélité** (contrôle du fournisseur raté ou absent, empan différent de celui de P3, identité de linéarité ratée) :
  le bras (i) n'est pas lu, les autres bras le sont (statut écrit dans la sortie).
Aucun texte d'action n'est lu : le témoin lexical prend les traits déjà calculés sur l'instance (`scores-p3.npz`).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import verifier_resultat
from ..scellement import empreinte, verifier
from . import constantes as C

CLES_FICHE = {"format", "redaction", "R1", "R2", "R4"}
POINTEURS_R1 = {"fidelite_conforme", "fidelite_ecart_max", "fidelite_tolerance", "fidelite_actions", "textes_sha256",
                "couches", "modele", "regle_empan", "contexte_rejeu", "dose"}
POINTEURS_R2 = {"invite_sha256", "contexte_juge", "modele", "reponse_imposee"}
VERDICTS_CONFORMES, VERDICTS_RATES = (True, "conforme"), (False, "non conforme", "echec", "échec")


def lire_json(chemin: Path) -> dict:
    try:
        return json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise GardeArret(f"{chemin} : JSON illisible ({type(e).__name__})") from None


def exiger_empreinte(racine: Path, chemin: str, attendue: str, quoi: str) -> Path:
    p = Path(racine) / chemin
    if not p.is_file():
        raise GardeArret(f"{quoi} : {chemin} absent sur disque (R11)")
    obtenue = empreinte(p)
    if obtenue != attendue:
        raise GardeArret(f"{quoi} : empreinte de {chemin} {obtenue[:12]}… ≠ empreinte déclarée {str(attendue)[:12]}…")
    return p


def pointeur(document, chemin):
    """Valeur au chemin JSON (liste de clés et d'indices) ; chemin qui ne se résout pas : arrêt (intégrité)."""
    if not isinstance(chemin, list) or not chemin:
        raise GardeArret(f"pointeur {chemin!r} : liste non vide de clés attendue")
    v = document
    for k in chemin:
        if isinstance(v, dict) and isinstance(k, str) and k in v:
            v = v[k]
        elif isinstance(v, list) and isinstance(k, int) and not isinstance(k, bool) and -len(v) <= k < len(v):
            v = v[k]
        else:
            raise GardeArret(f"pointeur {chemin!r} : clé {k!r} introuvable dans le manifeste du fournisseur")
    return v


def lire_fiche(racine: Path, chemin: str, scellee: bool) -> tuple[dict, str]:
    p = Path(racine) / chemin
    sha = verifier(p) if scellee else empreinte(p)
    f = lire_json(p)
    if not isinstance(f, dict) or set(f) != CLES_FICHE or f["format"] != C.FORMAT_FICHE:
        raise GardeArret(f"fiche de réception {chemin} : clés {sorted(f) if isinstance(f, dict) else type(f)} ou format "
                         f"≠ {C.FORMAT_FICHE}")
    for cle, autorises in (("R1", POINTEURS_R1), ("R2", POINTEURS_R2)):
        e = f[cle]
        if e is None:
            continue
        if set(e) != {"fichier", "manifeste", "pointeurs"} or set(e["pointeurs"]) - autorises:
            raise GardeArret(f"fiche : entrée {cle} hors de forme ({sorted(e)}, pointeurs {sorted(e.get('pointeurs', {}))})")
    r4 = f["R4"]
    if r4 is not None:
        if set(r4) != {"run", "empreintes", "pointeur_dose", "activations", "juge"}:
            raise GardeArret(f"fiche : entrée R4 hors de forme ({sorted(r4)})")
        for cle, autorises in (("activations", POINTEURS_R1), ("juge", POINTEURS_R2)):
            e = r4[cle]
            if e is not None and (set(e) != {"fichier", "manifeste", "pointeurs"} or set(e["pointeurs"]) - autorises):
                raise GardeArret(f"fiche : entrée R4.{cle} hors de forme")
    return f, sha


# --------------------------------------------------------------------------------------- run au format de P3
def _sondes_legeres(chemin: Path, noms: list[str]) -> dict:
    with np.load(chemin, allow_pickle=False) as z:
        index = json.loads(bytes(z["index"]).decode("utf-8"))
        sortie = {}
        for k, e in enumerate(index["sondes"]):
            if e["nom"] in noms:
                if e["classe"] != "SondeLineaireJetons" or e.get("b") is None:
                    raise GardeArret(f"sonde {e['nom']} : sonde linéaire par jeton attendue pour l'identité de fidélité")
                sortie[e["nom"]] = {"w": np.asarray(z[f"s{k}_w"], dtype=np.float64), "b": float(e["b"]),
                                    "couche": int(e["couche"]), "agregation": e["agregation"]}
    if set(sortie) != set(noms):
        raise GardeArret(f"sondes légères : {sorted(set(noms) - set(sortie))} absentes")
    return sortie


def charger_run(racine: Path, run_id: str, empreintes_attendues: dict | None) -> dict:
    """Résultats scellés et rattachés (`verifier_resultat`), fichiers de données dont l'empreinte égale celle des
    résultats du run et, si donnée, celle attendue ; tables, scores par jeton et sondes principales légères."""
    racine = Path(racine)
    d = racine / "diag" / run_id
    res = {}
    for nom in ("resume", "sondes-figees", "episodes-p3"):
        chemin = d / f"{nom}.json"
        if not chemin.exists():
            raise GardeArret(f"run {run_id} : {nom}.json absent (run sans résumé)")
        res[nom] = verifier_resultat(racine, chemin)["resultat"]
    if (d / "arret.json").exists():
        raise GardeArret(f"run {run_id} : arret.json présent")
    ep, rs, sf = res["episodes-p3"], res["resume"], res["sondes-figees"]
    shas = {}
    for cle, champ in (("scores", "scores_sha256"), ("jetons_principales", "jetons_principales_sha256"),
                       ("textes", "textes_sha256")):
        if verifier(racine / ep[cle]) != ep[champ] or ep[champ] != rs[champ]:
            raise GardeArret(f"run {run_id} : {ep[cle]} ≠ empreinte des résultats du run")
        if empreintes_attendues is not None and ep[champ] != empreintes_attendues.get(cle):
            raise GardeArret(f"run {run_id} : {cle} d'empreinte {ep[champ][:12]}… ≠ empreinte attendue")
        shas[cle] = ep[champ]
    legeres = Path(ep["scores"]).parent / "sondes-figees-legeres.npz"
    sha_l = verifier(racine / legeres)
    if sha_l != sf["sondes_legeres_sha256"] or (empreintes_attendues is not None
                                               and sha_l != empreintes_attendues.get("sondes_legeres")):
        raise GardeArret(f"run {run_id} : sondes légères d'empreinte inattendue")
    shas["sondes_legeres"] = sha_l
    with np.load(racine / ep["scores"], allow_pickle=False) as z:
        tables = {k: z[k] for k in z.files}
    with np.load(racine / ep["jetons_principales"], allow_pickle=False) as z:
        jetons = {k: z[k] for k in z.files}
    for k in C.IDENTITE + ("scores", "noms_sondes", "cout", "jetons_notes") + C.TRAITS_BOOLEENS:
        if k not in tables:
            raise GardeArret(f"run {run_id} : colonne {k} absente du fichier des scores")
    n = tables["episode"].shape[0]
    if any(tables[k].shape != (n,) for k in C.IDENTITE) or tables["scores"].shape[0] != n:
        raise GardeArret(f"run {run_id} : tables de longueurs différentes")
    principales = {c: sf["principales"][c] for c in ("tromperie", "enjeux")}
    if jetons["principales"].tolist() != [principales["tromperie"], principales["enjeux"]]:
        raise GardeArret(f"run {run_id} : scores par jeton d'autres sondes que les principales")
    if not np.array_equal(jetons["rang"], np.arange(n)) or not np.array_equal(jetons["longueur"], tables["jetons_notes"]):
        raise GardeArret(f"run {run_id} : scores par jeton désalignés des tables")
    noms = tables["noms_sondes"].tolist()
    for p in principales.values():
        if p not in noms:
            raise GardeArret(f"run {run_id} : sonde principale {p} absente des scores")
        if not np.all(np.isfinite(tables["scores"][:, noms.index(p)])):
            raise GardeArret(f"run {run_id} : score non fini de la sonde principale {p}")
    return {"run": run_id, "tables": tables, "jetons": jetons, "principales": principales,
            "legeres": _sondes_legeres(racine / legeres, list(principales.values())), "empreintes": shas,
            "resume": {k: rs[k] for k in ("actions", "actions_notees", "episodes") if k in rs}}


# ------------------------------------------------------------------------------------- fichiers des fournisseurs
def _identite_egale(z: dict, tables: dict, quoi: str) -> None:
    for k in C.IDENTITE:
        if k not in z:
            raise GardeArret(f"{quoi} : tableau d'identité {k} absent (alignement exigé, n° 328)")
        a, b = np.asarray(z[k]), np.asarray(tables[k])
        egal = a.shape == b.shape and (np.array_equal(a.astype(np.int64), b.astype(np.int64)) if k == "pas"
                                       else np.array_equal(a.astype(str), b.astype(str)))
        if not egal:
            raise GardeArret(f"{quoi} : alignement faux sur {k} (ordre ou clés ≠ scores-p3.npz)")


def _faits(manifeste: dict, pointeurs: dict) -> dict:
    return {k: pointeur(manifeste, v) for k, v in sorted(pointeurs.items())}


def charger_activations(racine: Path, entree: dict, source: dict) -> dict:
    tables = source["tables"]
    p = exiger_empreinte(racine, entree["fichier"]["chemin"], entree["fichier"]["sha256"], "activations")
    m = exiger_empreinte(racine, entree["manifeste"]["chemin"], entree["manifeste"]["sha256"], "manifeste des activations")
    faits = _faits(lire_json(m), entree["pointeurs"])
    with np.load(p, allow_pickle=False) as z:
        z = {k: z[k] for k in z.files}
    for k in ("moyenne", "jetons_empan"):
        if k not in z:
            raise GardeArret(f"activations : tableau {k} absent")
    _identite_egale(z, tables, "activations")
    n = tables["episode"].shape[0]
    forme = (n, len(C.COUCHES), C.DIMENSION)
    maximum = z.get("maximum")                 # facultatif : il ne sert qu'au bras descriptif i_max et à un contrôle
    if z["moyenne"].shape != forme or z["jetons_empan"].shape != (n,) or (maximum is not None and maximum.shape != forme):
        raise GardeArret(f"activations : formes {z['moyenne'].shape}, {None if maximum is None else maximum.shape}, "
                         f"{z['jetons_empan'].shape} ≠ {forme}")
    for k in ("moyenne", "maximum"):
        if z.get(k) is not None and not np.all(np.isfinite(z[k])):
            raise GardeArret(f"activations : valeur non finie dans {k}")
    if "textes_sha256" not in faits or faits["textes_sha256"] != source["empreintes"]["textes"]:
        raise GardeArret("activations : empreinte des textes rejoués absente ou ≠ textes du run")
    if "couches" not in faits or [int(c) for c in faits["couches"]] != list(C.COUCHES):
        raise GardeArret(f"activations : couches déclarées {faits.get('couches')} ≠ {list(C.COUCHES)}")
    return {"moyenne": z["moyenne"], "maximum": maximum, "jetons_empan": z["jetons_empan"],
            "dtype": str(z["moyenne"].dtype), "faits": faits, "empreintes": {"fichier": entree["fichier"]["sha256"],
                                                                             "manifeste": entree["manifeste"]["sha256"]}}


def charger_juge(racine: Path, entree: dict, source: dict) -> dict:
    tables = source["tables"]
    p = exiger_empreinte(racine, entree["fichier"]["chemin"], entree["fichier"]["sha256"], "scores du juge")
    m = exiger_empreinte(racine, entree["manifeste"]["chemin"], entree["manifeste"]["sha256"], "manifeste du juge")
    faits = _faits(lire_json(m), entree["pointeurs"])
    for k in ("invite_sha256", "contexte_juge"):
        if k not in faits:
            raise GardeArret(f"juge : {k} non déclaré par la fiche (invite gelée et contexte du juge exigés)")
    with np.load(p, allow_pickle=False) as z:
        z = {k: z[k] for k in z.files}
    if "score" not in z:
        raise GardeArret("juge : tableau score absent")
    _identite_egale(z, tables, "juge")
    s = np.asarray(z["score"], dtype=np.float64)
    if s.shape != (tables["episode"].shape[0],) or not np.all(np.isfinite(s)) or s.min() < 0.0 or s.max() > 1.0:
        raise GardeArret("juge : score de forme inattendue, non fini ou hors de [0, 1]")
    autres = sorted(set(z) - {"score"} - set(C.IDENTITE))
    return {"score": s, "faits": faits, "autres_tableaux": autres,
            "empreintes": {"fichier": entree["fichier"]["sha256"], "manifeste": entree["manifeste"]["sha256"]}}


# --------------------------------------------------------------------------------------------------- fidélité
def fidelite_fournisseur(faits: dict) -> dict:
    if "fidelite_conforme" not in faits:
        return {"conforme": False, "motif": "contrôle de fidélité du fournisseur non déclaré"}
    v = faits["fidelite_conforme"]
    if v is True or (isinstance(v, str) and v in VERDICTS_CONFORMES):
        ok = True
    elif v is False or (isinstance(v, str) and v in VERDICTS_RATES):
        ok = False
    else:
        raise GardeArret(f"verdict de fidélité du fournisseur illisible : {v!r}")
    r = {"conforme": bool(ok), "verdict": v}
    for k in ("fidelite_ecart_max", "fidelite_tolerance", "fidelite_actions"):
        if k in faits:
            r[k] = faits[k]
    if not ok:
        r["motif"] = "contrôle de fidélité du fournisseur raté"
    return r


def fidelite_independante(acts: dict, source: dict) -> dict:
    """Contrôles faits ici, sur les fichiers seuls :
    1. empan : `jetons_empan` égal, action par action, aux jetons notés par P3 ;
    2. identité de linéarité, couche 15 : les deux sondes principales de P3 sont linéaires par jeton (w·h + b) ; la
       moyenne de leurs scores par jeton sur l'empan (fichier des scores par jeton de P3) égale w·(moyenne rejouée) + b,
       à l'arrondi en demi-précision et au bruit du rejeu près ; corrélation de Pearson et pente sur les actions. Cette
       moyenne n'est jamais un score de moniteur : elle n'entre dans aucune aire ;
    3. maximum ≥ moyenne par dimension (au-delà de l'arrondi : 2⁻¹⁰ en relatif)."""
    tables, jetons = source["tables"], source["jetons"]
    empan_egal = bool(np.array_equal(np.asarray(acts["jetons_empan"]).astype(np.int64),
                                     np.asarray(tables["jetons_notes"]).astype(np.int64)))
    j = C.COUCHES.index(C.COUCHE_FIDELITE)
    M = np.asarray(acts["moyenne"][:, j, :], dtype=np.float64)
    debut, longueur = jetons["debut"].astype(np.int64), jetons["longueur"].astype(np.int64)
    par_sonde = {}
    for k, p in enumerate(jetons["principales"].tolist()):
        L = source["legeres"][p]
        if L["couche"] != C.COUCHE_FIDELITE:
            raise GardeArret(f"sonde {p} : couche {L['couche']} ≠ {C.COUCHE_FIDELITE}")
        s = jetons[f"scores_{k}"].astype(np.float64)
        cumul = np.concatenate([[0.0], np.cumsum(s)])
        with np.errstate(invalid="ignore", divide="ignore"):
            a = (cumul[debut + longueur] - cumul[debut]) / longueur
        b = M @ L["w"] + L["b"]
        ok = longueur > 0
        a, b = a[ok], b[ok]
        r = float(np.corrcoef(a, b)[0, 1]) if a.size > 2 and a.std() > 0 and b.std() > 0 else float("nan")
        pente = float(np.polyfit(a, b, 1)[0]) if a.size > 2 and a.std() > 0 else float("nan")
        e = np.abs(a - b) / (1.0 + np.abs(a))
        par_sonde[p] = {"correlation": r, "pente": pente, "ecart_relatif_median": float(np.median(e)),
                        "ecart_relatif_q99": float(np.quantile(e, 0.99)), "ecart_relatif_max": float(e.max()),
                        "actions": int(a.size)}
    if acts.get("maximum") is None:
        sous = None
    else:
        mo = np.asarray(acts["moyenne"], dtype=np.float32)
        ma = np.asarray(acts["maximum"], dtype=np.float32)
        sous = float(np.mean(ma < mo - 2.0 ** -10 * (np.abs(mo) + 1e-6)))
    correlations = [v["correlation"] for v in par_sonde.values()]
    grossiere = (not empan_egal) or any(not np.isfinite(c) or c < C.FIDELITE_CORRELATION_MIN for c in correlations)
    reserves = []
    if not grossiere and any(c < C.FIDELITE_CORRELATION_RESERVE for c in correlations):
        reserves.append(f"fidélité approximative : corrélation de l'identité de linéarité sous "
                        f"{C.FIDELITE_CORRELATION_RESERVE}")
    if not grossiere and any(not (C.FIDELITE_PENTE[0] <= v["pente"] <= C.FIDELITE_PENTE[1]) for v in par_sonde.values()):
        reserves.append(f"fidélité approximative : pente de l'identité de linéarité hors de {list(C.FIDELITE_PENTE)}")
    if sous is not None and sous > C.FIDELITE_MAX_SOUS_MOYENNE:
        reserves.append(f"maximum sous la moyenne pour une part {sous:.2e} des entrées")
    motif = None
    if not empan_egal:
        motif = "empan rejoué ≠ empan noté par P3"
    elif grossiere:
        motif = f"identité de linéarité ratée (corrélation sous {C.FIDELITE_CORRELATION_MIN})"
    return {"empan_egal": empan_egal, "sondes": par_sonde, "part_maximum_sous_moyenne": sous,
            "ratee": bool(grossiere), "motif": motif, "reserves": reserves}
