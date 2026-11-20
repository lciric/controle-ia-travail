"""M12 et S8 — les huit fréquences gelées de la couche mécanique, et la garde S8 (i).

Huit valeurs (S8, version 4 ; M12, version 5) : « tient » des lois vraies du monde source ; des lois vraies des mondes cibles ;
des lois fausses ; des lois non plantées de chacune des trois origines (recherche de base, composition passée au criblage,
copie) ; passage et faux passage du criblage. Une strate sans aucune loi engagée n'a pas de fréquence (valeur None) : si la
couche statistique en a besoin pour un proposeur d'une famille jouée, c'est un arrêt (liste d'arrêt, point 4), jamais un repli
sur la fréquence regroupée. Rapportés à côté, sans être servis : la fréquence regroupée des lois non plantées, celles des lois
vraies dépendantes et indépendantes, la part de chaque classe au grain de la tentative ; le nombre de lois de chaque strate,
avec l'intervalle binomial exact de sa fréquence.
"""

import hashlib
import json
import os

from .constantes import CLASSES, CLES_FREQUENCES, SEUIL_S8_I
from .intervalles import clopper_pearson

STRATE_DE_LA_CLE = {"p_tient_vraie_source": "vraie-source", "p_tient_vraie_cible": "vraie-cible", "p_tient_fausse": "fausse",
                    "p_tient_non_plantee_base": "non-plantee-base", "p_tient_non_plantee_composition": "non-plantee-composition",
                    "p_tient_non_plantee_copie": "non-plantee-copie"}


class ArretFrequences(RuntimeError):
    pass


def _part(a, b):
    return (a / b) if b else None


def frequences_gelees(comptes):
    """Les huit fréquences injectées dans la couche statistique ; None pour une strate vide."""
    f = {k: _part(comptes[s]["tiennent"], comptes[s]["engagees"]) for k, s in STRATE_DE_LA_CLE.items()}
    c = comptes["criblage"]
    f["p_passage_vraie"] = _part(c["vraies_retenues"], c["vraies_examinees"])
    f["p_faux_passage"] = _part(c["autres_passees"], c["autres_examinees"])
    return {k: f[k] for k in CLES_FREQUENCES}


def rapport(comptes):
    """Ce que M12 fait rapporter : chaque strate (dont les fréquences rapportées à côté) avec son nombre de lois et l'intervalle
    binomial exact à 95 % de sa fréquence ; le criblage ; la part de chaque classe au grain de la tentative."""
    out = {}
    for s, v in comptes.items():
        if s in ("criblage", "tentatives_par_classe"):
            continue
        out[s] = {"lois": v["engagees"], "tiennent": v["tiennent"], "frequence": _part(v["tiennent"], v["engagees"]),
                  "intervalle": clopper_pearson(v["tiennent"], v["engagees"]) if v["engagees"] else None}
    c = comptes["criblage"]
    out["criblage"] = {"passage_vraie": {"examinees": c["vraies_examinees"], "retenues": c["vraies_retenues"],
                                         "intervalle": clopper_pearson(c["vraies_retenues"], c["vraies_examinees"])
                                         if c["vraies_examinees"] else None},
                       "faux_passage": {"examinees": c["autres_examinees"], "passees": c["autres_passees"],
                                        "intervalle": clopper_pearson(c["autres_passees"], c["autres_examinees"])
                                        if c["autres_examinees"] else None}}
    t = comptes["tentatives_par_classe"]
    total = sum(t.values())
    out["tentatives_par_classe"] = {k: {"nombre": t[k], "part": _part(t[k], total)} for k in CLASSES}
    return out


def verifier_s8_i(freqs):
    """S8 (i), garde 24 : sur la couche mécanique, la part des lois vraies engagées qui tiennent est au moins 0,5 dans chacune
    des deux strates (monde source, mondes cibles), celle des lois fausses au plus 0,5 ; sinon arrêt (liste d'arrêt, point 4)."""
    vs, vc, fa = freqs["p_tient_vraie_source"], freqs["p_tient_vraie_cible"], freqs["p_tient_fausse"]
    if vs is None or vc is None or fa is None:
        raise ArretFrequences(f"S8 (i) : strate vide ({freqs}) : arrêt (liste d'arrêt, point 4)")
    if not (vs >= SEUIL_S8_I and vc >= SEUIL_S8_I and fa <= SEUIL_S8_I):
        raise ArretFrequences(f"S8 (i) : l'épreuve simulée ne discrimine pas (vraies source {vs}, vraies cibles {vc}, fausses "
                              f"{fa}) : arrêt, aucun tirage décisif (liste d'arrêt, point 4)")
    return True


def strates_requises(prop, dose, bras):
    """Les fréquences dont la couche statistique a besoin pour un proposeur, une dose et des bras."""
    req = {"p_tient_vraie_source", "p_tient_vraie_cible", "p_tient_fausse", "p_tient_non_plantee_base"}
    if prop["copieur"]:
        req.add("p_tient_non_plantee_copie")
    if prop["K"] and any(b in ("3", "4a") for b in bras):
        req |= {"p_tient_non_plantee_composition", "p_faux_passage"}
        if dose > 0:
            req.add("p_passage_vraie")
    return sorted(req)


def exiger_strates(freqs, prop, dose, bras):
    """Liste d'arrêt, point 4 : une strate vide dont la couche statistique a besoin arrête ; jamais de repli."""
    if sorted(freqs) != sorted(CLES_FREQUENCES):
        raise ArretFrequences(f"fichier des fréquences mal formé : clés {sorted(freqs)}")
    for k, v in freqs.items():
        if v is not None and not (0.0 <= float(v) <= 1.0):
            raise ArretFrequences(f"fréquence hors de [0 ; 1] : {k} = {v}")
    vides = [k for k in strates_requises(prop, dose, bras) if freqs[k] is None]
    if vides:
        raise ArretFrequences(f"strate de M12 vide dont la couche statistique a besoin : {vides} (proposeur {prop['nom']}, "
                              f"dose {dose}) : arrêt (liste d'arrêt, point 4)")
    return True


def geler(chemin, freqs, comptes, configuration):
    """Étape 5 : écrit le fichier des fréquences et son compagnon `.sha256` ; jamais d'écrasement. Rend l'empreinte."""
    corps = {"frequences": {k: freqs[k] for k in CLES_FREQUENCES}, "rapport": rapport(comptes), "configuration": configuration}
    octets = (json.dumps(corps, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    sha = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="ascii") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def lire_gelees(chemin, sha_attendue):
    """Relit le fichier gelé après vérification de son empreinte (sur disque et compagnon) ; arrêt sinon (règle R11)."""
    with open(chemin, "rb") as f:
        octets = f.read()
    sha = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", encoding="ascii") as f:
        compagnon = (f.read().split() or [""])[0]
    if sha != sha_attendue or compagnon != sha_attendue:
        raise ArretFrequences(f"fichier des fréquences d'empreinte inattendue : {chemin}")
    return json.loads(octets)["frequences"]
