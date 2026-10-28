"""E1a : log-richesses (finale, maximale) des fiches de la population scriptée et des témoins sur la banque T0.5 v2 réelle,
sous les réglages par défaut de la ligne de commande (urne, nul informé) et sans urne. Lecture seule ; aucun agent.

Usage : python -I -B e1a_balayage_richesses_v1.py COPIE_DU_CODE SORTIE.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aide_noyau_v1 as a  # noqa: E402

sortie = sys.argv[2]
resultats = {}
for nom_bras, reglages, informe in (("defaut_cli", {}, True), ("sans_urne_informe", {"urne": False}, True),
                                    ("sans_urne_aveugle", {"urne": False}, False)):
    config = a.config_ligne_de_commande(**reglages)
    monde = a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=informe)
    lignes = []
    for d in a.charger(a.POPULATION_V2) + a.charger(a.TEMOINS_V2):
        f = a.fiche_depuis(d)
        f.temoin = d.get("temoin")
        gele, ev, _ = a.juger(f, monde, config)
        lignes.append({"identifiant": d["identifiant"], "temoin": d.get("temoin"),
                       "moniteur": d["espace_instances"]["moniteur"], "n": ev["nombre_tirages"],
                       "log_w_finale": round(ev["log_richesse_finale"], 4), "log_w_max": round(ev["log_richesse_max"], 4),
                       "promue_par_fiche": ev["promue"], "dominant": ev["membre_dominant_final"]})
    resultats[nom_bras] = sorted(lignes, key=lambda l: -l["log_w_finale"])
with open(sortie, "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=1)
for nom_bras, lignes in resultats.items():
    print(nom_bras, "promues par fiche :", [l["identifiant"] for l in lignes if l["promue_par_fiche"]])
    print("  10 premières par log W final :")
    for l in lignes[:10]:
        print("   ", l)
    print("  témoins faux, log W final :", sorted(l["log_w_finale"] for l in lignes if l["temoin"] == "fausse"))
    print("  témoins vrais, log W max :", sorted(l["log_w_max"] for l in lignes if l["temoin"] == "vraie"))
