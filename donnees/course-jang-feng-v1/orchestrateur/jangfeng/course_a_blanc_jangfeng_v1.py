#!/usr/bin/env python3
"""KIT JANG-FENG, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Jang-Feng (question à une section servie et ses règles d'intégrité, deux pièces servies, trois variantes comme Ibrahim, juge du n° 419, marge d'appels 2 × plan + 5).
(COURSE À BLANC JANG-FENG v2, sous-agent de session-depot, 3 novembre 2026 : course_a_blanc_jangfeng_v1.py, gardé, R12, appliqué aux configurations Jang-Feng q1-v2 ; les lignes suivantes sont héritées.)
Course à blanc de la course Jang-Feng (moteur simulé : aucun appel, aucune dépense) sur les trois configurations v2 — v2 =
`course_a_blanc_heimersheim_v1.py` (gardé, R12) appliqué aux configurations v2 et au lanceur Python v2.

Rédigé le 3 novembre 2026 (sous-agent de session-depot). Pour chaque configuration : `lancer_course_jangfeng_v1.py verifier`
(dont `verifier_configuration_generation_v56` et les contrôles Jang-Feng) puis `simuler` dans un dossier NEUF hors du dépôt ;
compte des appels par étape, par rôle et par modèle (consommations du moteur simulé), comparé au plan d'appels du devis
(`course_jangfeng_v1.plan_appels`) ; bras déclarés, paires et fusions par bras. Écrit le rapport dans `--rapport` (neuf).

  python3 -I -B course_a_blanc_heimersheim_v1.py --dossier DOSSIER_NEUF_HORS_DEPOT --rapport RAPPORT_NEUF.txt
"""

import argparse
import collections
import json
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
sys.path.insert(0, ICI)
import course_jangfeng_v1 as ch  # noqa: E402

CONFS = {
         'sans_kimi': 'configuration-course-jang-feng-v1-sans-kimi.json',
         'avec_kimi': 'configuration-course-jang-feng-v1-avec-kimi.json',
         'cinq_especes': 'configuration-course-jang-feng-v1-cinq-especes.json',
}
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "HOME": "/tmp", "PYTHONDONTWRITEBYTECODE": "1"}


def executer(dossier):
    lignes, bilan = [], True
    for v, nom in CONFS.items():
        conf = os.path.join(ICI, nom)
        r = subprocess.run([sys.executable, "-I", "-B", os.path.join(ICI, "lancer_course_jangfeng_v1.py"), "verifier",
                            "--configuration", conf], env=ENV, capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit(f"{v} : vérification refusée : {r.stderr[-600:]}")
        sortie = os.path.join(dossier, v, "course")
        r = subprocess.run([sys.executable, "-I", "-B", os.path.join(ICI, "lancer_course_jangfeng_v1.py"), "simuler",
                            "--configuration", conf, "--sortie", sortie], env=ENV, capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit(f"{v} : course à blanc refusée : {r.stderr[-600:]}")
        g = os.path.join(sortie, "generation-1")
        cons = [x for x in json.load(open(os.path.join(g, "consommations.json"), encoding="utf-8"))["consommations"] if x.get("modele_demande")]
        vu = collections.Counter((x["etape"], x["role"], x["modele_demande"]) for x in cons)
        plan = collections.Counter()
        for e, ro, m, n in ch.plan_appels(v, json.load(open(conf, encoding="utf-8"))["bisociateur"]["k_paires"]):
            plan[(e, ro, m)] += n
        fin = json.load(open(os.path.join(g, "manifeste-fin.json"), encoding="utf-8"))
        cle = json.load(open(os.path.join(g, "coffre", "jf1-cle-bras.json"), encoding="utf-8"))
        par_bras = collections.Counter(x["bras"] for x in cle.values())
        egal = vu == plan
        bilan &= egal and not fin.get("arret")
        lignes += [f"## {v} ({nom})", f"- vérification (verifier_configuration_generation_v56 et contrôles Jang-Feng) : conforme",
                   f"- appels de course simulés : {sum(vu.values())} ; plan du devis : {sum(plan.values())} ; "
                   + ("identiques ligne à ligne" if egal else f"ÉCART : {dict(vu - plan)} / {dict(plan - vu)}"),
                   "- par étape : " + ", ".join(f"{k} {n}" for k, n in sorted(collections.Counter(x['etape'] for x in cons).items())),
                   "- par rôle : " + ", ".join(f"{k} {n}" for k, n in sorted(collections.Counter(x['role'] for x in cons).items())),
                   "- par modèle : " + ", ".join(f"{k} {n}" for k, n in sorted(collections.Counter(x['modele_demande'] for x in cons).items())),
                   f"- bras : {sorted(b for b, d in fin['bras'].items() if d.get('produit'))} produits ; non produits : {fin['non_produits'] or 'aucun'}",
                   f"- paires : {fin['paires']['nombre']} ; fusions par bras : {dict(par_bras)} ; complètes {fin['fusions']['completes']}, "
                   f"inachevées {fin['fusions']['inachevees']} ; arrêt : {fin.get('arret') or 'aucun'}", ""]
    return lignes, bilan


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--dossier", required=True)
    a.add_argument("--rapport", required=True)
    args = a.parse_args(argv)
    if os.path.exists(args.dossier) or os.path.exists(args.rapport):
        raise SystemExit("dossier ou rapport déjà présent (R12) : refus")
    depot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ICI))))
    if os.path.realpath(args.dossier).startswith(os.path.realpath(depot) + os.sep):
        raise SystemExit("le dossier de la course à blanc doit être hors du dépôt")
    os.makedirs(args.dossier)
    lignes, ok = executer(args.dossier)
    texte = ["# Course à blanc de la course Jang-Feng — moteur simulé, aucun appel, aucune dépense (kit Jang-Feng v1)", "",
             "Moteur simulé v56 (`pole/simulation_v56.AdaptateurSimuleV56`, " + str(ch.FICHES_PAR_PROPOSEUR) + " fiches par proposeur) ; toutes les fiches admises par "
             "l'aiguilleur simulé ; k_paires = 4 par bras.", ""] + lignes + [f"Bilan : {'conforme' if ok else 'ÉCART'}"]
    with open(args.rapport, "w", encoding="utf-8") as f:
        f.write("\n".join(texte) + "\n")
    print("\n".join(texte))
    return 0 if ok else 3


if __name__ == "__main__":
    sys.exit(principal())
