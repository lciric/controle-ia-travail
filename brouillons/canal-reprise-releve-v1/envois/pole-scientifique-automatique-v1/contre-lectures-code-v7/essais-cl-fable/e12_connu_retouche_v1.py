"""E12 : le nul informé contient la loi « connue » telle qu'ajustée (un membre « loi »), sans forme ajustée (tempérée,
inclinée, mélangée à l'aveugle) comme celles que la version 6 donne aux survivantes de l'archive. Une fiche qui n'est
que le prédicteur connu **retouché** (même poids, multipliés par c ; ou mélangé à la marginale de calibrage) peut-elle
battre le nul informé sur la banque réelle ? Lecture : log W max par moniteur ; promotions par fiche (seuil log 20).

Usage : python -I -B e12_connu_retouche_v1.py COPIE_DU_CODE SORTIE.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aide_noyau_v1 as a  # noqa: E402

sortie = sys.argv[2]
gabarit = a.charger(a.POPULATION_V2)[0]
resultats = {}
for urne in (True, False):
    config = a.config_ligne_de_commande(urne=urne, multiplicite="aucune")
    monde = a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=True)
    connus = monde.predicteurs_connus_publics()
    lignes = []
    for moniteur, loi in sorted(connus.items()):
        k = len(loi["biais"])
        for c in (0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0):
            retouchee = {"type": "softmax", "poids": [[round(c * w, 6) for w in l] for l in loi["poids"]], "biais": loi["biais"]}
            d = dict(gabarit, identifiant="G0-F01", enonce=f"Prédicteur connu de {moniteur} retouché (facteur {c})",
                     loi_predictive=retouchee, espace_instances=dict(gabarit["espace_instances"], moniteur=moniteur, nombre_issues=k))
            _, ev, _ = a.juger(a.fiche_depuis(d), monde, config)
            lignes.append({"moniteur": moniteur, "facteur": c, "log_w_max": round(ev["log_richesse_max"], 3),
                           "log_w_finale": round(ev["log_richesse_finale"], 3), "promue": ev["promue"],
                           "dominant": ev["membre_dominant_final"]})
    resultats["avec_urne" if urne else "sans_urne"] = lignes
with open(sortie, "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=1)
for bras, lignes in resultats.items():
    print(bras, "promues :", [(l["moniteur"], l["facteur"], l["log_w_max"]) for l in lignes if l["promue"]])
    meilleures = sorted(lignes, key=lambda l: -l["log_w_max"])[:6]
    print("  meilleures :", [(l["moniteur"], l["facteur"], l["log_w_max"], l["log_w_finale"]) for l in meilleures])
