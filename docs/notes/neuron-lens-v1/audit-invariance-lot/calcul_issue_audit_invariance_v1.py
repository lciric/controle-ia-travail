"""Calcul indépendant de l'issue de l'essai d'invariance au lot (lecteur neuf) — v1.

Écrit par le lecteur neuf sans importer ni lire le module de l'essai. Applique le § 4 du préenregistrement
v3 (empreinte bbf2c95b7a471c46218b349e05739c3affd57d6cdca4ce71c4abbb0e819205ad) au détail brut
diag/<run>/audit-invariance-lot-v3.json. Bibliothèque standard seulement.

Usage : python calcul_issue_audit_invariance_v1.py DETAIL.json SORTIE.json
"""
import hashlib
import json
import math
import sys

COUCHES = ("0", "15", "26")
LOT_REF, LOT_DECISIF, LOTS_RAPPORTES = "16", "64", ("1", "7")
N_ATTENDU = 64
SEUIL_C4 = 0.90


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def formes_attendues(longueurs, lot):
    """Formes des passes si les tâches sont prises dans l'ordre et bourrées à la plus longue :
    (2 × taille du paquet, longueur max du paquet) — propre et ablatée dans la même passe."""
    formes = set()
    for i in range(0, len(longueurs), lot):
        paquet = longueurs[i:i + lot]
        formes.add((2 * len(paquet), max(paquet)))
    return formes


def identiques(bloc):
    return bloc["taches"] == N_ATTENDU and bloc["taches_identiques"] == bloc["taches"]


def main(entree, sortie):
    d = json.load(open(entree, encoding="utf-8"))
    anomalies = []
    if d.get("n_taches") != N_ATTENDU:
        anomalies.append(f"n_taches = {d.get('n_taches')}")
    if [str(x) for x in d.get("lots", [])] != ["16", "64", "1", "7"]:
        anomalies.append(f"lots = {d.get('lots')}")
    if d.get("entropie") != 20261117:
        anomalies.append(f"entropie = {d.get('entropie')}")
    if sorted(d["couches"]) != sorted(COUCHES):
        anomalies.append(f"couches = {sorted(d['couches'])}")
    longueurs = d["longueurs"]
    if len(longueurs) != N_ATTENDU or not all(24 <= x <= 256 for x in longueurs):
        anomalies.append("longueurs hors de [24, 256] ou en nombre différent de 64")

    par_couche = {}
    for c in COUCHES:
        b = d["couches"][c]
        pl = b["par_lot"]
        f16 = {tuple(x) for x in pl[LOT_REF]["formes"]}
        f64 = {tuple(x) for x in pl[LOT_DECISIF]["formes"]}
        C1 = f16 != f64
        # contrôle supplémentaire (non décisif) : formes cohérentes avec les longueurs versées
        formes_coherentes = {
            lot: {tuple(x) for x in pl[lot]["formes"]} == formes_attendues(longueurs, int(lot))
            for lot in pl
        }
        p = b["C2_perturbation"]
        C2 = bool(p["tache0_change"]) and p["autres"] == N_ATTENDU - 1 and p["autres_identiques"] == p["autres"]
        C3 = identiques(b["C3_rejeu"])
        C3b = identiques(b["C3b_rejeu_lot64"])
        a = b["C4_ablation_agit"]
        C4 = a["taches"] == N_ATTENDU and a["taches_non_nulles"] >= math.ceil(SEUIL_C4 * a["taches"])
        # cohérence interne : identique au bit près ⇔ écart maximal nul
        coherence_ecart = {}
        for nom, bloc in list(pl.items()) + [("C3", b["C3_rejeu"]), ("C3b", b["C3b_rejeu_lot64"])]:
            coherence_ecart[nom] = (bloc["ecart_max"] == 0.0) == (bloc["taches_identiques"] == bloc["taches"])
        empreintes = b["empreintes_lot_ref"]
        par_couche[c] = {
            "C1": C1, "C2": C2, "C3": C3, "C3b": C3b, "C4": C4,
            "lot64_identique": identiques(pl[LOT_DECISIF]),
            "lot1_identique": identiques(pl["1"]),
            "lot7_identique": identiques(pl["7"]),
            "comptes": {lot: {"identiques": pl[lot]["taches_identiques"],
                              "identiques_demi_precision": pl[lot]["taches_identiques_demi_precision"],
                              "taches": pl[lot]["taches"], "ecart_max": pl[lot]["ecart_max"],
                              "passes_distinctes": len(pl[lot]["formes"])} for lot in ("16", "64", "1", "7")},
            "C4_non_nulles": a["taches_non_nulles"],
            "formes_coherentes_avec_longueurs": formes_coherentes,
            "coherence_identite_ecart_nul": coherence_ecart,
            "empreintes_lot_ref_distinctes": len(set(empreintes)),
        }

    temoins = all(par_couche[c][t] for c in COUCHES for t in ("C1", "C2", "C3", "C3b", "C4"))
    lot64 = all(par_couche[c]["lot64_identique"] for c in COUCHES)
    lots17 = all(par_couche[c]["lot1_identique"] and par_couche[c]["lot7_identique"] for c in COUCHES)
    if not temoins:
        issue = "indéterminé"
    elif not lot64:
        issue = "invariance réfutée"
    elif lots17:
        issue = "invariance établie"
    else:
        issue = "identité 16/64 établie, invariance non établie"

    resultat = {
        "entree": {"chemin": entree, "sha256": sha256(entree)},
        "regle": "§ 4 du préenregistrement v3, bbf2c95b7a471c46218b349e05739c3affd57d6cdca4ce71c4abbb0e819205ad",
        "issue": issue,
        "temoins_tenus": temoins,
        "lot64_identique_trois_couches": lot64,
        "lots_1_et_7_identiques_trois_couches": lots17,
        "par_couche": par_couche,
        "demi_precision_rapportee": {c: {lot: par_couche[c]["comptes"][lot]["identiques_demi_precision"]
                                         for lot in ("16", "64", "1", "7")} for c in COUCHES},
        "temoin_produit_bf16_rapporte": d["temoin_produit_bf16"],
        "anomalies": anomalies,
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(issue)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
