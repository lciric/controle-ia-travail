"""Lecture gelée du crible (iii) — v1 (`lire_crible_iii_v1.py`, nom réservé par la pièce qui fera foi, section « Étapes », point 0).

Applique, dans l'ordre, les étages 0 à 7 des « Critères de lecture gelés » de la pièce (`crible-iii-version-foi-v1.md`,
`91b4bf30…`) à la sortie scellée de la mesure et au relevé scellé du lanceur ; un étage 0, 1 ou 3 arrête la lecture. Programme pur,
bibliothèque standard seule ; rend un objet JSON (écrit scellé avec `--ecrire`). La lecture n'est qu'une aide : le verdict est
prononcé par un sous-agent neuf (R13), après l'audit de symétrie (R4).

Usage : python3 -I -B lire_crible_iii_v1.py --sortie DOSSIER [--ecrire FICHIER]
Codes : 0 lecture faite ; 2 refus (pièces absentes ou différentes de leurs compagnons : étage 0, « non jugeable (arrêt) »).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

VERSION = "lecture-crible-iii-v1"
MIN_COMPLETS, FORMAT_MIN, ZONE_MIN = 16, 14, 10
E_MIN = 0.5
TRONQUES_MAX = 3
MARGE = 0.5


def _compagnon_egal(chemin):
    try:
        with open(chemin + ".sha256", encoding="utf-8") as f:
            attendu = f.read().split()[0]
        with open(chemin, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest() == attendu
    except (OSError, IndexError):
        return False


def issue_p1(iv):
    if iv is None:
        return "non tranché"
    if iv[0] > 0:
        return "deux passes plus efficaces par dollar"
    if iv[1] < 0:
        return "moins efficaces"
    return "non tranché"


def issue_p2(iv):
    if iv is None:
        return "non tranché"
    if iv[0] > 0:
        return "perte établie sans le proposeur cher" + (" (petite)" if iv[1] < MARGE else "")
    if iv[1] < MARGE:
        return "sans perte notable"
    return "non tranché"


def issue_q(iv):
    if iv is None:
        return "non tranché"
    if iv[0] > 0:
        return "le choix bon marché aide"
    if iv[1] < MARGE:
        return "pas mieux que le hasard au crible"
    return "non tranché"


def lire(releve, corps):
    """Étages 0 à 7 ; rend {etage_arret, verdicts, reserves, rapporte}."""
    out = {"version": VERSION, "verdicts": {}, "reserves": [], "etage_arret": None, "rapporte": {}}
    arret = releve.get("arret")
    if arret is not None and arret.get("ligne") != "minimum":
        out.update(etage_arret=0, verdicts={"0": "non jugeable (arrêt)"}, cause=arret)
        return out
    if corps is None:
        out.update(etage_arret=0, verdicts={"0": "non jugeable (arrêt)"}, cause="mesure en erreur ou absente")
        return out
    n_c = corps["n_complets"]
    if n_c < MIN_COMPLETS or corps["fournisseur_perdu"] or (arret is not None and arret.get("ligne") == "minimum"):
        out.update(etage_arret=1, verdicts={"1": "non concluant"},
                   cause={"n_complets": n_c, "fournisseur_perdu": corps["fournisseur_perdu"], "arret": arret})
        return out
    st = corps["principal"]
    iv = st["intervalles"]
    est = st["estimations"]
    tronques = corps["tronques_par_bras"]
    reserves = []
    if corps["format_tenu_mondes"] < FORMAT_MIN:
        reserves.append("format non tenu")
    e_d = corps["execution"]["D"]["E"]
    if e_d is None or e_d < E_MIN:
        reserves.append("consigne non suivie")
    for b in ("S", "D", "H", "B"):
        if tronques.get(b, 0) >= TRONQUES_MAX:
            reserves.append(f"{b} tronqué")
    p2_principal = issue_p2(iv["delta_DB"])
    p2_reint = issue_p2(corps["reintegre_delta_DB"]["intervalle_97_5"])
    if p2_reint != p2_principal:
        reserves.append("P2 sensible à la troncature")
    out["reserves"] = reserves
    out["rapporte"]["delta_DB_reintegre"] = corps["reintegre_delta_DB"]
    if corps["zone_utile_mondes"] < ZONE_MIN:
        out.update(etage_arret=3, verdicts={"3": "hors de la zone utile"})
        return out
    v = {"4": issue_p1(iv["delta_R"]), "5": p2_principal}
    if "B tronqué" in reserves and v["5"].startswith("perte établie"):
        v["5"] = "phrase interdite sous « B tronqué » (perte établie) : rapportée sans conclusion"
    if "D tronqué" in reserves and v["5"] == "sans perte notable":
        v["5"] = "phrase interdite sous « D tronqué » (sans perte notable) : rapportée sans conclusion"
    if "P2 sensible à la troncature" in reserves:
        v["5"] += " — sensible à la troncature (rien de plus n'en est conclu)"
    v["6"] = {"Q": issue_q(iv["delta_DH"]), "F": {"estimation": est["delta_HS"], "intervalle_95": iv["delta_HS"]}}
    if v["4"].startswith("deux passes plus efficaces"):
        h = "H-iii non réfutée au crible, " + ("gain du choix" if v["6"]["Q"] == "le choix bon marché aide" else
                                               "gain du format" if v["6"]["Q"].startswith("pas mieux") else "source non tranchée")
    elif v["4"] == "moins efficaces":
        h = "H-iii réfutée au crible"
    else:
        h = "H-iii non tranchée"
    if reserves:
        h += " (sous réserve : " + ", ".join(reserves) + " ; aucune conclusion sur l'idée)"
    out["verdicts"] = v
    out["h_iii"] = h
    out["rapporte"].update({"estimations": est, "intervalles": iv, "R": st["R"], "signes": st["signes"],
                            "execution": corps["execution"], "bruit": corps["bruit"], "choix_passe1": corps["choix_passe1"],
                            "conditionnelles": corps["conditionnelles"], "sensibilites": corps["sensibilites"],
                            "jetons_et_dollars_par_passe": corps["jetons_et_dollars_par_passe"], "audit": corps["audit"],
                            "adoption": "aucune (nœud de Lazar ; N-045 point 1 ; N-058)"})
    out["etage_arret"] = 7
    return out


def main(argv):
    import argparse
    p = argparse.ArgumentParser(prog="lire_crible_iii_v1.py")
    p.add_argument("--sortie", required=True)
    p.add_argument("--ecrire")
    a = p.parse_args(argv)
    rel = os.path.join(a.sortie, "releve-crible-iii-v1.json")
    mes = os.path.join(a.sortie, "mesure-crible-iii-v1.json")
    if not _compagnon_egal(rel):
        print(json.dumps({"version": VERSION, "etage_arret": 0, "verdicts": {"0": "non jugeable (arrêt)"},
                          "cause": "relevé absent ou différent de son compagnon"}, ensure_ascii=False))
        return 2
    with open(rel, encoding="utf-8") as f:
        releve = json.load(f)
    corps = None
    if _compagnon_egal(mes):
        with open(mes, encoding="utf-8") as f:
            corps = json.load(f)["corps"]
    out = lire(releve, corps)
    texte = json.dumps(out, ensure_ascii=False, sort_keys=True, indent=1) + "\n"
    if a.ecrire:
        with open(a.ecrire, "x", encoding="utf-8") as f:
            f.write(texte)
        with open(a.ecrire + ".sha256", "x", encoding="utf-8") as f:
            f.write(f"{hashlib.sha256(texte.encode('utf-8')).hexdigest()}  {os.path.basename(a.ecrire)}\n")
    print(texte, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
