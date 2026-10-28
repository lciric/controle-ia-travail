"""Démonstration du cycle v3 — le pôle complet en simulation (processeur, sans dépense), exploratoire, lue dans les deux sens.

Sélection par pari, juge v1 (ordre d'exécution secret imposé par le noyau, urne) ; population et témoins de
démonstration (`exemples/population-pari-demo-v1.json`, `exemples/temoins-pari-demo-v1.json`, vérités
`exemples/monde-pari-demo-v1.json`) ; quatre générations avec recombinaison ; l'agent de recombinaison simulé propose,
avec la probabilité `p_triviale`, une fille « triviale » (parent A mélangé à une loi aveugle tirée : aucune idée neuve) que
le monde suit exactement (pire cas). Trois bras, mêmes graines : **v3** (juge v1, nul des filles v2, tirage stratifié :
les défauts de v3) ; **v3 avec le nul de v0** (seul le nul des filles change) ; **v0** (juge v0, nul de v0, noyau corrigé :
le système d'avant). Le monde simulé n'a pas de dérive : il ne montre pas l'apport du juge v1 sur la dérive (expérience 1),
seulement son coût éventuel en puissance sur les témoins vrais.

Mesures, par course et par bras : filles triviales testées et promues ; autres filles testées, promues vraies, promues
fausses (vérité du monde simulé) ; témoins : fausses gardées et vraies éliminées (`qualite_cumulee`).
Lecture fixée avant le lancement : (1) sous le nul v2, aucune fille triviale promue (attendu 0 : leur loi est dans une
famille ajustée) ; (2) sous le nul de v0, une part notable (attendu de l'ordre de 0,4 des triviales testées, comme
« parent + loi aveugle » à l'expérience 2 ; mais deux essais de fumée déclarés, 2 et 6 graines, en ont donné 0 sur 4 et
1 sur 13 : à 120 tirages et sur ce plan, la part est sans doute bien plus basse) — au-delà de 0,05, sinon la
démonstration n'a pas de dents ; (3) autres filles et témoins
comparables entre les deux premiers bras (écart de promotions des autres filles vraies au plus 0,1 en part) ; (4)
descriptif : témoins vrais éliminés sous v3 et sous v0 (coût de l'urne à 120 tirages).

Usage : python -I -B demonstrations/demo_cycle_v3.py DOSSIER_NEUF [--courses N] [--generations G] [--p-triviale P]
"""

import argparse
import json
import os
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))

from pole.cycle import ConfigGeneration  # noqa: E402
from pole.fiche import charger_fiches  # noqa: E402
from pole.outils import ecrire_json_scelle, manifeste, normaliser_texte, sha256_fichier  # noqa: E402
from pole.pole import executer_pole  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

EXEMPLES = os.path.join(os.path.dirname(ICI), "exemples")
TESTES = ("survit", "eliminee", "indecise", "retiree", "rejetee (test change)")


BRAS = {"v3": {"juge": "v1", "nul_filles": "v2", "tirage_recombinaison": "stratifie"},
        "v3_nul_v0": {"juge": "v1", "nul_filles": "v0", "tirage_recombinaison": "stratifie"},
        "v0": {"juge": "v0", "nul_filles": "v0", "tirage_recombinaison": "noyau_corrige"}}


def une_course(graine, bras, racine, generations, p_triviale, horodatage):
    population = charger_fiches(os.path.join(EXEMPLES, "population-pari-demo-v1.json"))
    temoins = charger_fiches(os.path.join(EXEMPLES, "temoins-pari-demo-v1.json"))
    with open(os.path.join(EXEMPLES, "monde-pari-demo-v1.json"), encoding="utf-8") as f:
        verites = json.load(f)["verites"]
    verites.update({t.enonce: t.temoin == "vraie" for t in temoins})
    monde = MondeSimule(graine, verites)
    adaptateur = AdaptateurSimule(graine, monde, p_fille_triviale=p_triviale)
    config = ConfigGeneration(selection="pari", graine=graine, budget_generation_usd=10.0, **BRAS[bras]).valider()
    bilan = executer_pole(population, temoins, adaptateur, config, generations, 10.0 * generations, racine,
                          memoire_active=True, horodatage_fourni=horodatage)
    with open(os.path.join(racine, "archive", "index.json"), encoding="utf-8") as f:
        index = json.load(f)
    m = {"triviales_testees": 0, "triviales_promues": 0, "autres_filles_testees": 0, "autres_promues_vraies": 0,
         "autres_promues_fausses": 0, "autres_vraies_testees": 0}
    for entree in index.values():
        if not entree.get("parents") or entree.get("statut") not in TESTES:
            continue
        triviale = normaliser_texte(entree["enonce"]) in adaptateur.filles_triviales
        promue = entree["statut"] == "survit"
        if triviale:
            m["triviales_testees"] += 1
            m["triviales_promues"] += promue
        else:
            vraie = monde.verite(entree["enonce"])
            m["autres_filles_testees"] += 1
            m["autres_vraies_testees"] += vraie
            m["autres_promues_vraies"] += promue and vraie
            m["autres_promues_fausses"] += promue and not vraie
    m["qualite_temoins"] = bilan["qualite_cumulee"]
    m["generations"] = bilan["generations_executees"]
    m["arret"] = bilan["arret"]
    return m


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("--courses", type=int, default=20)
    a.add_argument("--generations", type=int, default=4)
    a.add_argument("--p-triviale", type=float, default=0.4)
    args = a.parse_args()
    if os.path.exists(args.sortie) and os.listdir(args.sortie):
        sys.exit(f"dossier non vide : {args.sortie}")
    os.makedirs(args.sortie, exist_ok=True)
    quand = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    p = {"courses": args.courses, "generations": args.generations, "p_triviale": args.p_triviale,
         "graines": list(range(1, args.courses + 1)), "bras": BRAS,
         "script_sha256": sha256_fichier(os.path.abspath(__file__))}
    ecrire_json_scelle(os.path.join(args.sortie, "manifeste.json"), dict(manifeste(**p), horodatage=quand))
    debut = time.monotonic()
    par = {b: [] for b in BRAS}
    for graine in p["graines"]:
        for bras in BRAS:
            racine = os.path.join(args.sortie, "courses", f"graine-{graine:02d}-{bras}")
            par[bras].append(une_course(graine, bras, racine, args.generations, args.p_triviale, quand))
    total = {}
    for nul, liste in par.items():
        somme = {k: sum(x[k] for x in liste) for k in liste[0] if isinstance(liste[0][k], int)}
        temoins = {k: sum(x["qualite_temoins"][k] for x in liste)
                   for k in ("temoins_faux_testes", "temoins_vrais_testes", "fausses_gardees", "vraies_eliminees")}
        somme.update(temoins)
        somme["part_triviales_promues"] = somme["triviales_promues"] / somme["triviales_testees"] if somme["triviales_testees"] else None
        somme["part_autres_vraies_promues"] = (somme["autres_promues_vraies"] / somme["autres_vraies_testees"]
                                               if somme["autres_vraies_testees"] else None)
        total[nul] = somme
    lecture = {
        "1_aucune_triviale_promue_sous_v3": total["v3"]["triviales_promues"] == 0,
        "2_triviales_promues_sous_le_nul_de_v0_au_dela_de_alpha": (total["v3_nul_v0"]["part_triviales_promues"] or 0) > 0.05,
        "3_autres_vraies_comparables": (total["v3"]["part_autres_vraies_promues"] is not None
                                        and total["v3_nul_v0"]["part_autres_vraies_promues"] is not None
                                        and abs(total["v3"]["part_autres_vraies_promues"]
                                                - total["v3_nul_v0"]["part_autres_vraies_promues"]) <= 0.1),
        "4_temoins_vrais_elimines_v3_et_v0": [total["v3"]["vraies_eliminees"], total["v0"]["vraies_eliminees"],
                                              total["v3"]["temoins_vrais_testes"], total["v0"]["temoins_vrais_testes"]],
    }
    r = {"parametres": p, "horodatage": quand, "total_par_bras": total, "lecture": lecture, "par_course": par,
         "duree_s": round(time.monotonic() - debut, 1)}
    ecrire_json_scelle(os.path.join(args.sortie, "demo-cycle-v3.json"), r)
    print(json.dumps({"total_par_bras": total, "lecture": lecture, "duree_s": r["duree_s"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    principal()
