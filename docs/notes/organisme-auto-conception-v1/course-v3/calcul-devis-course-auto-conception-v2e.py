#!/usr/bin/env python3
"""Calcul du devis v2e — tentative neuve de la course d'auto-conception (correction ciblée de Carbon). Version 1.

Écrit le 18 novembre 2026 par le développeur unique de la tentative neuve (modèle L′). Aucun appel, aucun réseau : lit des
pièces scellées du dépôt (empreintes vérifiées), calcule, écrit une sortie JSON scellée (compagnon `.sha256`). Base : coûts
**réels** de la course v4 (manifeste de fin), coût réel de l'épreuve v4, usage des lots de Carbon relevé par le diagnostic
(table § 2, transcrite ici avec son empreinte), et, pour les étapes que la v4 n'a pas jouées (aiguillage, juges), le calcul du
devis v2 (composition déclarée).

Usage (cwd = racine du dépôt) : python3 -I -B docs/notes/organisme-auto-conception-v1/course-v3/calcul-devis-course-auto-conception-v2e.py SORTIE.json
"""
import hashlib
import json
import math
import sys
from pathlib import Path

VERSION = "calcul-devis-course-auto-conception-v2e"
DEPOT = Path(__file__).resolve().parents[4]
SOURCES = {
    "manifeste_fin_v4": ("runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-fin.json",
                         "2625234c786a7fc50c926325c1a9efc8a8e9b74146a59205bf8a31c6e2c5fd7f"),
    "manifeste_depart_v4": ("runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-depart.json",
                            "4aae57de3e520d3287682c3c26c073cae3f3a5a2af1967a75ef58a5045dc2e90"),
    "epreuve_v4": ("docs/notes/organisme-auto-conception-v1/course-v2/epreuve-temoins-reelle-auto-conception-v4.json",
                   "980e888898c180b347d526d75bdc41d531ec26943c043a96e44c24c0853337be"),
    "calcul_devis_v2": ("docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v2.json",
                        "91f5cf8f147689eb2fa9ff9db8b6e3b91b15496174e03f07a66d691676c2db2b"),
    "releve_credits_v4": ("docs/notes/organisme-auto-conception-v1/course-v2/releve-credits-avant-course-auto-conception-v2.json",
                          None),
    "diagnostic": ("docs/notes/organisme-auto-conception-v1/course-v2/diagnostic-erreurs-carbon-astra-course-v4-v1.md", None),
    "piece_de_depart_v2": ("docs/notes/organisme-auto-conception-v1/course-v2/piece-de-depart-auto-conception-v2.json",
                           "e2689fa22fff31319ff69deefe10c066d5329fab28d9c9b133750f2534fc1ded"),
}
COMPOSITION = "prop-argon+prop-astra+prop-carbon+prop-claude-1+prop-claude-2"
# Diagnostic § 2 (table transcrite) : jetons d'entrée, de sortie, de pensée des quatre lots de Carbon finis « SUCCEEDED ».
LOTS_CARBON = [(40986, 3410, 18823), (28791, 2202, 0), (34062, 3231, 17454), (29951, 3319, 20696)]
PRIX_CARBON = (8.3, 41.5)              # USD par million, prix plein (commande, borne haute)
PLAFOND_SESSION_PROPOSEUR = 3.0
PLAFOND_ARRET = 90.0
PLAFOND_EPREUVE = 5.0
SONDE_ASTRA_MAX = 0.05
PROVISION = 32768
MAX_SORTIE_DEMANDEE = 16384
MAX_SORTIE_VARIANTE = 32768
CASES = 11
# Configuration v2 (budget, l'étape « juges » protégée : plafond de relais 30 USD ; S17 = 90).
PLAFOND_RELAIS_JUGES = 30.0


def sha256_fichier(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def lire(nom):
    rel, attendu = SOURCES[nom]
    p = DEPOT / rel
    h = sha256_fichier(p)
    compagnon = Path(str(p) + ".sha256")
    scelle = compagnon.is_file() and compagnon.read_text(encoding="utf-8").split()[0] == h
    if attendu is not None and h != attendu:
        raise SystemExit(f"{rel} : empreinte {h}, {attendu} attendue")
    if not scelle:
        raise SystemExit(f"{rel} : non scellé")
    return p, h


def cout_lot(e, s, p):
    pe, ps = PRIX_CARBON[0] / 1e6, PRIX_CARBON[1] / 1e6
    return e * pe + (s + p) * ps


def pire_carbon(entree_max_octets, max_sortie, octets_par_jeton):
    """Règle de la commande (garde avant envoi), compte de jetons pris à `octets / octets_par_jeton` (≥ caractères / 3)."""
    pe, ps = PRIX_CARBON[0] / 1e6, PRIX_CARBON[1] / 1e6
    compte = max(entree_max_octets / octets_par_jeton, entree_max_octets / 3.0)
    entree = math.ceil(compte * 1.05)
    sortie = int(min(max_sortie, math.floor((PLAFOND_SESSION_PROPOSEUR - entree * pe) / ps - PROVISION)))
    return {"entree_gardee_jetons": entree, "max_output_tokens": sortie, "pire_usd": round(entree * pe + (sortie + PROVISION) * ps, 6)}


def principal(argv):
    if len(argv) != 1:
        raise SystemExit("usage : calcul-devis-course-auto-conception-v2e.py SORTIE.json")
    sortie = Path(argv[0])
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    sources = {n: lire(n) for n in SOURCES}
    fin = json.loads(sources["manifeste_fin_v4"][0].read_text(encoding="utf-8"))
    dep = json.loads(sources["manifeste_depart_v4"][0].read_text(encoding="utf-8"))
    ep4 = json.loads(sources["epreuve_v4"][0].read_text(encoding="utf-8"))
    dv2 = json.loads(sources["calcul_devis_v2"][0].read_text(encoding="utf-8"))["totaux"][COMPOSITION]
    rel4 = json.loads(sources["releve_credits_v4"][0].read_text(encoding="utf-8"))
    piece = json.loads(sources["piece_de_depart_v2"][0].read_text(encoding="utf-8"))
    par_role, appels = fin["cout_reel"]["par_role_usd"], fin["cout_reel"]["appels_par_role"]
    entree_max = int(dep["lots"]["entree_max_octets"])

    couts_lots = [cout_lot(*l) for l in LOTS_CARBON]
    carbon_moyen = sum(couts_lots) / len(couts_lots)
    carbon_haut = max(couts_lots)
    pires = {"max_sortie_16384_comptes_car_sur_3": pire_carbon(entree_max, MAX_SORTIE_DEMANDEE, 3.0),
             "max_sortie_16384_comptes_octets_sur_2": pire_carbon(entree_max, MAX_SORTIE_DEMANDEE, 2.0),
             "max_sortie_32768_comptes_car_sur_3": pire_carbon(entree_max, MAX_SORTIE_VARIANTE, 3.0),
             "max_sortie_32768_comptes_octets_sur_2": pire_carbon(entree_max, MAX_SORTIE_VARIANTE, 2.0)}

    prop_v4 = {r: par_role[r] for r in ("prop-opus", "prop-fable", "prop-argon", "prop-astra")}
    prop_est = dict(prop_v4, **{"prop-carbon": round(CASES * carbon_moyen, 6)})
    prop_haut_carbon = round(CASES * carbon_haut, 6)
    prop_pire_carbon = round(CASES * pires["max_sortie_16384_comptes_octets_sur_2"]["pire_usd"], 6)
    proposition_est = round(sum(prop_est.values()), 6)
    proposition_haut = round(sum(prop_v4.values()) + prop_haut_carbon, 6)
    aig_est, jug_est = dv2["estimation"]["aiguilleur_usd"], dv2["estimation"]["juges_usd"]
    aig_haut, jug_haut = dv2["haut"]["aiguilleur_usd"], dv2["haut"]["juges_usd"]
    course_est = round(proposition_est + aig_est + jug_est, 6)
    course_haut_brut = round(proposition_haut + aig_haut + jug_haut, 6)
    epreuve_est = float(ep4["cout_usd"])
    total_est = round(course_est + epreuve_est + SONDE_ASTRA_MAX, 6)

    # Clé Claude : dépense antérieure lue au relevé de la v4 (6,48 + épreuve v4, 0,999689, comprise) + dépense Claude de la
    # course v4 ; puis l'épreuve v5, estimée à la dépense Claude de l'épreuve v4 (champ « motif » du relevé v4)
    cle = piece["variable_cle_claude"]
    anterieure_v4 = float(rel4["cles"][cle]["depense_anterieure_usd"])
    claude_course_v4 = float(fin["cout_reel"]["par_relais_usd"]["claude"])
    claude_epreuve_v4 = 0.999689   # relevé des crédits v4, champ « motif » (dépense Claude de l'épreuve v4 lue au relais 8787)
    anterieure_avant_epreuve = round(anterieure_v4 + claude_course_v4, 6)
    anterieure_v5 = round(anterieure_avant_epreuve + claude_epreuve_v4, 6)
    reserves = sum(x["montant_usd"] for x in piece["reserves_cle_claude"])
    credit = float(piece["credit_declare_cle_claude_usd"])
    reste_net = round(credit - anterieure_v5 - reserves, 6)

    out = {
        "version": VERSION,
        "sources": {n: {"chemin": SOURCES[n][0], "sha256": h} for n, (_p, h) in sources.items()},
        "base_v4": {"par_role_usd": par_role, "appels_par_role": appels, "total_usd": fin["cout_reel"]["total_usd"],
                    "etapes": fin["ce_qui_a_ete_fait"]["etapes"], "entree_max_octets": entree_max,
                    "epreuve_v4_usd": epreuve_est},
        "carbon": {"lots_diagnostic": LOTS_CARBON, "cout_par_lot_usd": [round(c, 6) for c in couts_lots],
                   "estimation_par_appel_usd": round(carbon_moyen, 6), "haut_par_appel_usd": round(carbon_haut, 6),
                   "pire_par_appel": pires, "provision_pensee_jetons": PROVISION},
        "proposition": {"estimation_par_role_usd": prop_est, "estimation_usd": proposition_est, "haut_usd": proposition_haut,
                        "carbon_au_pire_11_appels_usd": prop_pire_carbon},
        "aiguillage": {"estimation_usd": aig_est, "haut_usd": aig_haut, "source": "calcul du devis v2, composition déclarée"},
        "juges": {"estimation_usd": jug_est, "haut_usd": jug_haut, "source": "calcul du devis v2, composition déclarée"},
        "course": {"estimation_usd": course_est, "haut_brut_usd": course_haut_brut, "plafond_arret_usd": PLAFOND_ARRET,
                   "seuil_cumul_pour_lancer_les_juges_usd": PLAFOND_ARRET - PLAFOND_RELAIS_JUGES,
                   "cumul_estime_avant_juges_usd": round(proposition_est + aig_est, 6)},
        "epreuve_v5": {"estimation_usd": epreuve_est, "plafond_usd": PLAFOND_EPREUVE},
        "sonde_astra": {"au_plus_usd": SONDE_ASTRA_MAX},
        "total": {"estimation_usd": total_est, "au_pire_usd": round(PLAFOND_ARRET + PLAFOND_EPREUVE + SONDE_ASTRA_MAX, 6)},
        "cle_claude": {"variable": cle, "credit_declare_usd": credit,
                       "depense_anterieure_releve_v4_usd": anterieure_v4,
                       "depense_claude_course_v4_usd": claude_course_v4,
                       "depense_anterieure_avant_epreuve_v5_usd": anterieure_avant_epreuve,
                       "epreuve_v5_claude_estimee_usd": claude_epreuve_v4,
                       "depense_anterieure_apres_epreuve_v5_estimee_usd": anterieure_v5, "reserves_usd": reserves,
                       "reste_net_estime_au_depart_usd": reste_net, "part_au_pire_usd": PLAFOND_ARRET,
                       "depart_refuse_code_3_si_credit_et_reserves_inchanges": reste_net <= PLAFOND_ARRET,
                       "credit_minimal_pour_partir_usd": round(PLAFOND_ARRET + anterieure_v5 + reserves, 6)},
    }
    sortie.parent.mkdir(parents=True, exist_ok=True)
    donnees = (json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(sortie, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(sortie) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {sortie.name}\n")
    print(json.dumps({"sortie": str(sortie), "sha256": h, "total": out["total"], "course": out["course"],
                      "carbon": {k: out["carbon"][k] for k in ("estimation_par_appel_usd", "haut_par_appel_usd")},
                      "pires": {k: v["pire_usd"] for k, v in pires.items()}, "cle_claude": out["cle_claude"]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
