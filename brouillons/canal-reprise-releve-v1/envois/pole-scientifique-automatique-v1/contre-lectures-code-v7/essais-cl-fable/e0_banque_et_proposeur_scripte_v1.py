"""E0 (contre-lecture v7, socle Fable) : reproductibilité de la banque T0.5 v2 et indépendance du proposeur scripté vis-à-vis
des issues d'épreuve.

1. Reconstruit la banque v2 depuis la racine de `main` (lecture seule) dans un dossier neuf et compare son empreinte à
   `exemples/banque-t05-v2.json` ; compare les empreintes des sources consignées dans la banque aux fichiers sur disque.
2. Rejoue le proposeur scripté sur la banque, puis sur une copie de la banque dont **toutes les issues d'épreuve** sont
   remplacées (permutation tirée) : si les sorties (population, témoins) sont identiques, le script n'utilise pas l'épreuve.
3. Indique ce que voit un agent d'une fiche témoin : l'énoncé public d'un témoin dit-il sa vérité ?

Usage : python -I -B e0_banque_et_proposeur_scripte_v1.py COPIE_DU_CODE RACINE_MAIN DOSSIER_SORTIE_NEUF
"""
import copy
import hashlib
import json
import os
import random
import sys

COPIE, MAIN, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, COPIE)
sys.path.insert(0, os.path.join(COPIE, "exemples"))
os.makedirs(SORTIE, exist_ok=False)

from pole.outils import json_canonique, sha256_fichier  # noqa: E402
import construire_banque_t05_v1 as cb  # noqa: E402
import proposeur_scripte_banque_v1 as ps  # noqa: E402
from pole.fiche import Fiche  # noqa: E402

rapport = {}
# 1. reconstruction
refaite = os.path.join(SORTIE, "banque-t05-v2-refaite.json")
banque_refaite = cb.construire(MAIN, 20261027)
from pole.outils import ecrire_json_scelle  # noqa: E402
ecrire_json_scelle(refaite, banque_refaite)
livree = os.path.join(COPIE, "exemples", "banque-t05-v2.json")
rapport["banque_livree_sha256"] = sha256_fichier(livree)
rapport["banque_refaite_sha256"] = sha256_fichier(refaite)
rapport["banque_identique_octet_pour_octet"] = rapport["banque_livree_sha256"] == rapport["banque_refaite_sha256"]
with open(livree, encoding="utf-8") as f:
    banque = json.load(f)
rapport["sources"] = {chemin: {"consignee": h, "sur_disque": sha256_fichier(os.path.join(MAIN, chemin)),
                               "egale": h == sha256_fichier(os.path.join(MAIN, chemin))}
                      for chemin, h in banque["sources"].items()}

# 2. proposeur scripté : indépendance vis-à-vis de l'épreuve
pop1, tem1, rap1 = ps.proposer(copy.deepcopy(banque))
alteree = copy.deepcopy(banque)
rng = random.Random(12345)
for nom, m in alteree["moniteurs"].items():
    lignes = [l for l in alteree["instances"] if l["partie"] == "epreuve" and nom in l["issues"]]
    valeurs = [rng.randrange(m["nombre_issues"]) for _ in lignes]  # issues d'épreuve remplacées au hasard
    for l, v in zip(lignes, valeurs):
        l["issues"][nom] = v
pop2, tem2, rap2 = ps.proposer(alteree)
rapport["proposeur_scripte_identique_si_epreuve_alteree"] = (
    json_canonique(pop1) == json_canonique(pop2) and json_canonique(tem1) == json_canonique(tem2)
    and json_canonique(rap1) == json_canonique(rap2))
rapport["proposeur_scripte_lit_le_fichier_entier"] = True  # par lecture du code : principal() charge toute la banque
# Les témoins livrés sont-ils ceux que rend le script sur la banque livrée ?
with open(os.path.join(COPIE, "exemples", "temoins-banque-t05-v2.json"), encoding="utf-8") as f:
    temoins_livres = json.load(f)
with open(os.path.join(COPIE, "exemples", "population-banque-t05-v2.json"), encoding="utf-8") as f:
    population_livree = json.load(f)
rapport["temoins_livres_egaux_au_script"] = json_canonique(temoins_livres["fiches"]) == json_canonique(tem1)
rapport["population_livree_egale_au_script"] = json_canonique(population_livree["fiches"]) == json_canonique(pop1)

# 3. vue publique d'un témoin (ce que voient l'expérimentateur et le vérificateur quand les témoins passent par des agents)
vues = []
for t in temoins_livres["fiches"][:3]:
    f = Fiche.depuis_dict(dict(t, identifiant="G0-F07"))  # identifiant remplacé comme dans executer_pole
    vue = f.vue_publique()
    vues.append({"enonce_public": vue["enonce"], "temoin_dans_la_vue": "temoin" in vue,
                 "operateurs": vue["operateurs"], "contraintes": vue["contraintes"]})
rapport["vue_publique_de_temoins"] = vues
rapport["temoins_reconnaissables_par_l_enonce"] = all(v["enonce_public"].startswith("Témoin ") for v in vues)
sortie = os.path.join(SORTIE, "e0-resultat-v1.json")
with open(sortie, "w", encoding="utf-8") as f:
    json.dump(rapport, f, ensure_ascii=False, indent=1, sort_keys=True)
print(json.dumps(rapport, ensure_ascii=False, indent=1, sort_keys=True))
