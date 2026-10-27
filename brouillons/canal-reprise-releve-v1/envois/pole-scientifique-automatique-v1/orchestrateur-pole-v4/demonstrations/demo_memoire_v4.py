"""Démonstration de la mémoire v4 dans le cycle du pôle — simulation, processeur, sans dépense ; exploratoire, lue dans
les deux sens (préenregistrement levé pour l'exploratoire, mot de Lazar du 27 octobre, 12:02 heure de Paris).

Sélection par pari, juge v1, nul des filles v2, tirage stratifié, filles sur 300 tirages ; population, témoins et
vérités de démonstration (`exemples/*-pari-demo-v1.json`). L'agent de recombinaison simulé repropose, avec la probabilité
`p_redite`, une idée de la population initiale « reformulée » (même loi ; le monde simulé lui donne la vérité de
l'idée). Trois bras, mêmes graines : politique de redite **héritage** (défaut de v4), **refus**, **rien** (retestée depuis
zéro) ; garde par la signature prédictive dans les trois.

Mesures par bras (sommes sur les courses) : redites proposées, refusées, testées ; **découvertes en double** (redite
promue d'une idée déjà promue : une même idée comptée deux fois) ; **fausses découvertes** parmi les redites (idée fausse
promue) ; vraies redites promues (idée vraie, jamais promue avant) ; témoins.
Lecture fixée avant le lancement : (1) héritage et refus : 0 découverte en double (la redite d'une survivante est
refusée) ; « rien » : au moins une (sinon la démonstration n'a pas de dents) ; (2) fausses découvertes parmi les redites :
héritage ≤ rien ; (3) descriptif : vraies redites promues, héritage contre refus (l'héritage laisse une seconde chance à
une vraie idée éliminée à tort).

Usage : python -I -B demonstrations/demo_memoire_v4.py DOSSIER_NEUF [--courses N] [--generations G] [--p-redite P]
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
SUFFIXE = " (reformulé)"
BRAS = ("heritage", "refus", "rien")


def une_course(graine, politique, racine, generations, p_redite, horodatage):
    population = charger_fiches(os.path.join(EXEMPLES, "population-pari-demo-v1.json"))
    temoins = charger_fiches(os.path.join(EXEMPLES, "temoins-pari-demo-v1.json"))
    with open(os.path.join(EXEMPLES, "monde-pari-demo-v1.json"), encoding="utf-8") as f:
        verites = json.load(f)["verites"]
    verites.update({t.enonce: t.temoin == "vraie" for t in temoins})
    monde = MondeSimule(graine, verites)
    adaptateur = AdaptateurSimule(graine, monde, p_redite=p_redite, idees_attirantes=[f.vers_dict() for f in population])
    config = ConfigGeneration(selection="pari", graine=graine, budget_generation_usd=10.0, politique_redite=politique).valider()
    bilan = executer_pole(population, temoins, adaptateur, config, generations, 10.0 * generations, racine,
                          memoire_active=True, horodatage_fourni=horodatage)
    with open(os.path.join(racine, "archive", "index.json"), encoding="utf-8") as f:
        index = json.load(f)
    promues_originales = {normaliser_texte(e["enonce"]) for e in index.values()
                          if e.get("statut") == "survit" and not e["enonce"].endswith(SUFFIXE)}
    m = {"redites_proposees": 0, "redites_refusees": 0, "redites_testees": 0, "decouvertes_en_double": 0,
         "fausses_parmi_les_redites": 0, "vraies_redites_promues": 0}
    for e in sorted(index.values(), key=lambda e: e["identifiant"]):
        if not e["enonce"].endswith(SUFFIXE):
            continue
        m["redites_proposees"] += 1
        if e.get("statut") == "refusee (redite)":
            m["redites_refusees"] += 1
            continue
        if e.get("statut") not in TESTES:
            continue
        m["redites_testees"] += 1
        if e["statut"] != "survit":
            continue
        original = normaliser_texte(e["enonce"][:-len(SUFFIXE)])
        if original in promues_originales:
            m["decouvertes_en_double"] += 1
        elif not monde.verite(e["enonce"]):
            m["fausses_parmi_les_redites"] += 1
        else:
            m["vraies_redites_promues"] += 1
    m["qualite_temoins"] = bilan["qualite_cumulee"]
    m["generations"] = bilan["generations_executees"]
    m["survivantes"] = len(bilan["survivantes"])
    return m


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("--courses", type=int, default=20)
    a.add_argument("--generations", type=int, default=4)
    a.add_argument("--p-redite", type=float, default=0.5)
    args = a.parse_args()
    if os.path.exists(args.sortie) and os.listdir(args.sortie):
        sys.exit(f"dossier non vide : {args.sortie}")
    os.makedirs(args.sortie, exist_ok=True)
    quand = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    p = {"courses": args.courses, "generations": args.generations, "p_redite": args.p_redite,
         "graines": list(range(1, args.courses + 1)), "bras": list(BRAS), "script_sha256": sha256_fichier(os.path.abspath(__file__))}
    ecrire_json_scelle(os.path.join(args.sortie, "manifeste.json"), dict(manifeste(**p), horodatage=quand))
    debut = time.monotonic()
    par = {b: [] for b in BRAS}
    for graine in p["graines"]:
        for bras in BRAS:
            racine = os.path.join(args.sortie, "courses", f"graine-{graine:02d}-{bras}")
            par[bras].append(une_course(graine, bras, racine, args.generations, args.p_redite, quand))
    total = {}
    for bras, liste in par.items():
        somme = {k: sum(x[k] for x in liste) for k in liste[0] if isinstance(liste[0][k], int)}
        for k in ("temoins_faux_testes", "temoins_vrais_testes", "fausses_gardees", "vraies_eliminees"):
            somme[k] = sum(x["qualite_temoins"][k] for x in liste)
        total[bras] = somme
    lecture = {
        "1_aucun_double_sous_heritage_et_refus": total["heritage"]["decouvertes_en_double"] == 0
                                                 and total["refus"]["decouvertes_en_double"] == 0,
        "1_doubles_sous_rien": total["rien"]["decouvertes_en_double"],
        "2_fausses_heritage_au_plus_rien": total["heritage"]["fausses_parmi_les_redites"]
                                           <= total["rien"]["fausses_parmi_les_redites"],
        "3_vraies_redites_promues_heritage_et_refus": [total["heritage"]["vraies_redites_promues"],
                                                       total["refus"]["vraies_redites_promues"]],
    }
    r = {"parametres": p, "horodatage": quand, "total_par_bras": total, "lecture": lecture, "par_course": par,
         "duree_s": round(time.monotonic() - debut, 1)}
    ecrire_json_scelle(os.path.join(args.sortie, "demo-memoire-v4.json"), r)
    print(json.dumps({"total_par_bras": total, "lecture": lecture, "duree_s": r["duree_s"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    principal()
