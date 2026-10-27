"""E17 : une fiche sur banque sans `nombre_issues` : `MondeBanque.moniteur_de` prend celui du moniteur, `preparer_engagement`
et `_controler_pari` prennent 3. Une loi à 3 issues posée sur un moniteur à 2 issues est-elle acceptée et jugée à 3 issues ?
(Reprise, en script, d'une vérification faite d'abord en ligne de commande.)

Usage : python -I -B e17_nombre_issues_defaut_v1.py COPIE_DU_CODE SORTIE.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aide_noyau_v1 as a  # noqa: E402

population = a.charger(a.POPULATION_V2)
d = next(x for x in population if x["espace_instances"]["moniteur"] == "3B:COHERENCE")  # loi à 3 issues
d = dict(d, identifiant="G0-F01", espace_instances={"moniteur": "3B:BALANCE", "dimension": 4, "sous_populations": 2,
                                                     "banque": "banque-t05-v2"})
f = a.fiche_depuis(d)
config = a.config_ligne_de_commande(urne=True, multiplicite="aucune")
sortie = {}
monde = a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=False)
gele, ev, mes = a.juger(f, monde, config)
sortie["sans_nul_informe"] = {"moniteur_accepte": monde.moniteur_de(f),
                              "issues_du_moniteur": monde.banque["moniteurs"]["3B:BALANCE"]["nombre_issues"],
                              "nombre_issues_de_l_engagement": gele.engagement["nombre_issues"],
                              "issues_deposees_distinctes": sorted(set(mes["issues"])), "promue": ev["promue"]}
try:
    a.juger(f, a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=True), config)
    sortie["avec_nul_informe"] = "accepté"
except Exception as e:  # noqa: BLE001
    sortie["avec_nul_informe"] = f"refus : {type(e).__name__} : {e}"
with open(sys.argv[2], "w", encoding="utf-8") as fo:
    json.dump(sortie, fo, ensure_ascii=False, indent=1)
print(json.dumps(sortie, ensure_ascii=False, indent=1))
