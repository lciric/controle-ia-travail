"""Expérience 2 du pôle — le nul des filles v2 — exploratoire (R-522), sans préenregistrement (mot de Lazar du 27 octobre
2026, 12:02 heure de Paris), lue dans les deux sens. Plan, lecture et prédictions écrits ici avant le premier lancement.

Juge v1 (ordre d'exécution secret, urne) ; nul d'une fille = 𝓛 v1 + parents + formes de v0 (`bibliotheque_fille`) +
membres ajustés (`nul_filles_v2`) ; lecture aux instants 25, 50, …, 200 de la part d'évaluation (50 tirages de calibrage
avant) ; règle de marge des filles de v0 (gain moyen sur la meilleure enveloppe ≥ 2δ₀ = 0,02 nat), membres ajustés compris.
Le monde de chaque tricheur est sa propre loi (le pire cas : le tricheur a raison, mais n'apporte rien de neuf).

Lignes (1 000 répétitions par défaut) :
- fatales, nul v2 strict, taux ≤ α = 0,05 : les sept tricheurs de v0 ; T9 (concaténation si/sinon, sans calibrage ni
  marge, et log W max ≤ 10⁻⁹) ; T1b-fille ; « parent + loi aveugle » (q tirée de Dirichlet(1, 1, 1), λ = 0,5) ; « parent
  tempéré et incliné » (a sur [0,5 ; 1,5], log-biais gaussiens d'écart 0,7) ; « mise en commun linéaire + loi aveugle »
  (½·(πA + (1 − π)B) + ½·q) ; « produit des parents » (A^a·B^b, a et b sur [0,5 ; 1,5], log-biais d'écart 0,5) ;
- artefacts requis, taux > α (sinon le contrôle n'a pas de dents) : nul v1 sur « parent + loi aveugle » ; nul v2 sans
  membres logarithmiques sur « parent tempéré et incliné » ; nul v2 sans membre linéaire sur « mise en commun linéaire +
  loi aveugle » ; nul v2 souple (sans produit des parents) sur « produit des parents » ;
- puissance décisive, nul v2, taux ≥ 0,90 : fille neuve (si/sinon : parent A sur la sous-population 0, loi neuve ailleurs) ;
- descriptives : fille neuve sous nul v1 (coût du nul v2) ; fille neuve faible (0,7·B + 0,3·loi neuve sur la
  sous-population 1) et combinaison « ou exclusif » des parents (A si les deux traits ont le même signe, B sinon), sous
  v2 et sous v1 ; T1b-fille sous nul v1.
Issue (règle de la note) : adopté si toutes les fatales ≤ α, tous les artefacts > α et la puissance ≥ 0,90 ; non adopté si
une fatale cède ou si la puissance manque ; non concluant sinon.
Prédictions (confiance) : « parent + loi aveugle », « parent tempéré et incliné », « mise en commun linéaire + loi
aveugle » et « produit des parents » à 0 exactement (leur loi est dans une famille ajustée : log W ≤ 0 à chaque instant)
(0,9) ; sept tricheurs et T9 à 0 (0,9) ; T1b-fille ≤ 0,02 (0,7) ; artefacts : nul v1 sur « parent + loi aveugle » 0,25 à
0,45 (0,8), les trois autres > 0,30 (0,6) ; fille neuve ≥ 0,95 sous v2 (0,85), perte v1 − v2 ≤ 0,03 (0,7) ; issue
« adopté » (0,65).

Usage : python -I -B experience_2_nul_filles_v2.py DOSSIER_SORTIE_NEUF --graine G [--repetitions N] [--essai]
        [--lignes nom1,nom2,…] [--processus N]
"""

import argparse
import concurrent.futures
import json
import math
import os
import random
import statistics
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "orchestrateur-pole-v2"))

import nul_filles_v2 as nf  # noqa: E402
from pole import selection_pari as sp  # noqa: E402
from pole.controles_pari import (MONDES_FILLES, TRICHEURS, _dirichlet, _fixe, _frequences, _monde_fille,  # noqa: E402
                                 borne_wilson, loi_tricheur)
from pole.outils import ecrire_json_scelle, graine_derivee, manifeste, sha256_fichier  # noqa: E402

K, DIM, TIRAGES, CALIBRAGE, ALPHA, DELTA0 = 3, 2, 200, 50, 0.05, 0.01
LAMBDA = 0.5
REPETITIONS = 1000
SEUIL_PUISSANCE = 0.90


def _softmax_combinee(lois_poids, biais_ajoutes):
    """Loi softmax de poids Σ c·W et biais Σ c·b + biais ajoutés (produit de parents softmax, tempéré et incliné)."""
    poids = [[sum(c * l["poids"][k][d] for l, c in lois_poids) for d in range(DIM)] for k in range(K)]
    biais = [sum(c * l["biais"][k] for l, c in lois_poids) + biais_ajoutes[k] for k in range(K)]
    return {"type": "softmax", "poids": poids, "biais": biais}


def scenario(nom, rng):
    """Rend (loi de la fille, monde, parent A, parent B, instances, marginale d'entraînement, nom du monde, réglages)."""
    p1, p2, p3 = (sp.loi_softmax_aleatoire(rng, K, DIM) for _ in range(3))
    calibrage = 0 if nom == "T9" else CALIBRAGE
    instances = sp.tirer_instances(rng, calibrage + TIRAGES, DIM)
    horizon = None
    if nom.startswith("tricheur:"):
        monde_nom = rng.choice(MONDES_FILLES)
        monde = _monde_fille(monde_nom, p1, p2, instances)
    elif nom == "T9":
        monde_nom, monde = "parents_par_sous_population", {"type": "par_sous_population", "lois": {"0": p1, "1": p2}}
        loi = {"type": "si_sinon", "condition": {"sous_population": 0}, "si": p1, "sinon": p2}
    elif nom == "fille_neuve":
        monde_nom, monde = "A_et_loi_neuve", {"type": "par_sous_population", "lois": {"0": p1, "1": p3}}
        loi = {"type": "si_sinon", "condition": {"sous_population": 0}, "si": p1, "sinon": p3}
    elif nom == "fille_neuve_faible":
        autre = {"type": "melange", "composantes": [p2, p3], "poids": [0.7, 0.3]}
        monde_nom, monde = "A_et_B_un_peu_neuve", {"type": "par_sous_population", "lois": {"0": p1, "1": autre}}
        loi = {"type": "si_sinon", "condition": {"sous_population": 0}, "si": p1, "sinon": autre}
    elif nom == "ou_exclusif":
        meme_signe = {"type": "si_sinon", "condition": {"indice": 1, "seuil": 0.0}, "si": p1, "sinon": p2}
        signe_oppose = {"type": "si_sinon", "condition": {"indice": 1, "seuil": 0.0}, "si": p2, "sinon": p1}
        loi = {"type": "si_sinon", "condition": {"indice": 0, "seuil": 0.0}, "si": meme_signe, "sinon": signe_oppose}
        monde_nom, monde = "ou_exclusif_des_parents", loi
    elif nom == "T1b-fille":
        horizon = calibrage + TIRAGES
        derive = {"type": "calendrier", "probas": []}
        a = [0.6, 0.3, 0.1]
        rng.shuffle(a)
        b = list(reversed(a))
        for t in range(horizon):
            s = t / max(1, horizon - 1)
            derive["probas"].append([(1 - s) * x + s * y for x, y in zip(a, b)])
        monde_nom = "A_plus_derive"
        monde = {"type": "melange", "composantes": [p1, derive], "poids": [1 - LAMBDA, LAMBDA]}
        loi = {"type": "melange", "composantes": [p1, {"type": "calendrier", "probas": derive["probas"][calibrage:]}],
               "poids": [1 - LAMBDA, LAMBDA]}
    elif nom == "parent_et_loi_aveugle":
        q = _dirichlet(rng, K, 1.0)
        monde_nom = "A_plus_loi_aveugle"
        loi = monde = {"type": "melange", "composantes": [p1, _fixe(q)], "poids": [1 - LAMBDA, LAMBDA]}
    elif nom == "parent_tempere_incline":
        a = rng.uniform(0.5, 1.5)
        monde_nom = "A_tempere_incline"
        loi = monde = _softmax_combinee([(p1, a)], [rng.gauss(0.0, 0.7) for _ in range(K)])
    elif nom == "lineaire_et_aveugle":
        pi, q = rng.random(), _dirichlet(rng, K, 1.0)
        monde_nom = "mise_en_commun_lineaire_et_aveugle"
        loi = monde = {"type": "melange", "composantes": [p1, p2, _fixe(q)], "poids": [0.5 * pi, 0.5 * (1 - pi), 0.5]}
    elif nom == "produit_des_parents":
        a, b = rng.uniform(0.5, 1.5), rng.uniform(0.5, 1.5)
        monde_nom = "produit_des_parents"
        loi = monde = _softmax_combinee([(p1, a), (p2, b)], [rng.gauss(0.0, 0.5) for _ in range(K)])
    else:
        raise ValueError(nom)
    entrainement = sp.tirer_instances(rng, 100, DIM)
    issues_ent = [sp.tirer_categorie(rng, sp.proba(monde, x, [], rng.randrange(horizon) if horizon else 0))
                  for x in entrainement]
    q_ent = _frequences(issues_ent, K)
    if nom.startswith("tricheur:"):
        loi = loi_tricheur(nom.split(":", 1)[1], p1, p2, q_ent, rng)
    return loi, monde, p1, p2, instances, q_ent, monde_nom, calibrage


def essai(graine, nom, variante, r):
    cle = f"exp2|{nom}"
    rng = random.Random(graine_derivee(graine, cle, r))
    loi, monde, p1, p2, instances, q_ent, monde_nom, calibrage = scenario(nom, rng)
    standard = list(sp.BIBLIOTHEQUE_STANDARD_V1) + [{"nom": "marginale_entrainement", "type": "fixe", "probas": q_ent}]
    parents = {"A": p1, "B": p2}
    biblio = sp.bibliotheque_fille(parents, DIM, standard, q_ent, nombre_issues=K) + nf.membres_de_variante(variante, parents)
    delta0 = None if nom == "T9" else DELTA0
    gele = sp.geler_engagement(nf.construire_engagement_v2("fille", loi, instances, K, ALPHA, biblio, calibrage, delta0,
                                                           nf.INSTANTS_PAR_DEFAUT))
    noyau = graine_derivee(graine, cle, r, "noyau")
    tirages = sp.tirer_frais(gele, monde, graine_derivee(graine, cle, r, "frais"), graine_noyau=noyau)
    ev = nf.evaluer_v2(gele, tirages, graine_noyau=noyau)
    ev["empreinte_ordre"] = tirages.get("empreinte_ordre")
    return monde_nom, ev


LIGNES = (
    [(f"tricheur:{t}", "v2", "fatal") for t in TRICHEURS]
    + [("T9", "v2", "fatal"), ("T1b-fille", "v2", "fatal"), ("parent_et_loi_aveugle", "v2", "fatal"),
       ("parent_tempere_incline", "v2", "fatal"), ("lineaire_et_aveugle", "v2", "fatal"),
       ("produit_des_parents", "v2", "fatal"),
       ("parent_et_loi_aveugle", "v1", "artefact_requis"), ("parent_tempere_incline", "v2_sans_log", "artefact_requis"),
       ("lineaire_et_aveugle", "v2_sans_lineaire", "artefact_requis"), ("produit_des_parents", "v2_souple", "artefact_requis"),
       ("fille_neuve", "v2", "puissance_decisive"),
       ("fille_neuve", "v1", "descriptif"), ("fille_neuve_faible", "v2", "descriptif"),
       ("fille_neuve_faible", "v1", "descriptif"), ("ou_exclusif", "v2", "descriptif"), ("ou_exclusif", "v1", "descriptif"),
       ("T1b-fille", "v1", "descriptif")])


def executer_ligne(graine, nom, variante, role, repetitions):
    promotions, maxima, finales, chaine, dominants, par_monde, plans, ordres = 0, [], [], [], {}, {}, {}, set()
    for r in range(repetitions):
        monde_nom, ev = essai(graine, nom, variante, r)
        promotions += ev["promue"]
        chaine.append("1" if ev["promue"] else "0")
        maxima.append(ev["log_richesse_max"])
        finales.append(ev["log_richesse_finale"])
        d = ev["membre_dominant_final"].split(":")[0]
        dominants[d] = dominants.get(d, 0) + 1
        m = par_monde.setdefault(monde_nom, [0, 0])
        m[0] += ev["promue"]
        m[1] += 1
        plans[ev["plan_execution"]] = plans.get(ev["plan_execution"], 0) + 1
        if ev.get("empreinte_ordre"):
            ordres.add(ev["empreinte_ordre"])
    ligne = {"controle": nom, "nul": variante, "role": role, "repetitions": repetitions, "promotions": promotions,
             "taux": promotions / repetitions, "borne_haute_95": borne_wilson(promotions, repetitions),
             "log_richesse_max_observee": max(maxima), "log_richesse_finale_mediane": statistics.median(finales),
             "membre_dominant_final": dict(sorted(dominants.items())),
             "par_monde": {k: {"promotions": v[0], "repetitions": v[1]} for k, v in sorted(par_monde.items())},
             "plan_execution_observe": plans, "empreintes_ordre_distinctes": len(ordres),
             "promotions_par_repetition": "".join(chaine)}
    if nom == "T9":
        ligne["passe"] = ligne["taux"] <= ALPHA and ligne["log_richesse_max_observee"] <= 1e-9
    return ligne


def _ligne_chronometree(arguments):
    t0 = time.monotonic()
    ligne = executer_ligne(*arguments)
    ligne["duree_s"] = round(time.monotonic() - t0, 1)
    return ligne


def lire(lignes):
    def passe(l):
        return l["passe"] if "passe" in l else l["taux"] <= ALPHA
    fatales = [l for l in lignes if l["role"] == "fatal"]
    echecs = [f"{l['controle']} ({l['nul']})" for l in fatales if not passe(l)]
    non_vus = [f"{l['controle']} ({l['nul']})" for l in lignes if l["role"] == "artefact_requis" and l["taux"] <= ALPHA]
    faibles = [f"{l['controle']} ({l['nul']})" for l in lignes if l["role"] == "puissance_decisive" and l["taux"] < SEUIL_PUISSANCE]
    issue = "non adopté" if echecs or faibles else ("non concluant" if non_vus else "adopté")
    taux = {(l["controle"], l["nul"]): l["taux"] for l in lignes}
    perte = (taux[("fille_neuve", "v1")] - taux[("fille_neuve", "v2")]
             if {("fille_neuve", "v1"), ("fille_neuve", "v2")} <= set(taux) else None)
    plans_ok = all(set(l["plan_execution_observe"]) == {"ordre_secret"} and l["empreintes_ordre_distinctes"] == l["repetitions"]
                   for l in lignes)
    return {"issue": issue, "fatales_echouees": echecs, "artefacts_non_vus": non_vus, "puissances_insuffisantes": faibles,
            "perte_fille_neuve_v1_moins_v2": perte, "plans_et_ordres_conformes": plans_ok}


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("--graine", type=int, required=True)
    a.add_argument("--repetitions", type=int, default=REPETITIONS)
    a.add_argument("--essai", action="store_true")
    a.add_argument("--lignes", default=None, help="essai : noms de contrôles séparés par des virgules")
    a.add_argument("--processus", type=int, default=2)
    args = a.parse_args()
    if os.path.exists(args.sortie) and os.listdir(args.sortie):
        sys.exit(f"dossier non vide : {args.sortie}")
    if not args.essai and (args.repetitions != REPETITIONS or args.lignes):
        sys.exit(f"hors essai : {REPETITIONS} répétitions, toutes les lignes")
    choisies = [l for l in LIGNES if not args.lignes or l[0] in args.lignes.split(",")]
    p = {"graine": args.graine, "repetitions": args.repetitions, "essai": args.essai, "lignes": [list(l) for l in choisies],
         "tirages": TIRAGES, "calibrage": CALIBRAGE, "alpha": ALPHA, "delta0": DELTA0, "instants": list(nf.INSTANTS_PAR_DEFAUT),
         "variantes": {k: v for k, v in nf.VARIANTES.items()},
         "script_sha256": sha256_fichier(os.path.abspath(__file__)),
         "module_sha256": sha256_fichier(os.path.join(ICI, "nul_filles_v2.py"))}
    quand = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    os.makedirs(args.sortie, exist_ok=True)
    ecrire_json_scelle(os.path.join(args.sortie, "manifeste.json"), dict(manifeste(**p), horodatage=quand))
    debut = time.monotonic()
    # Lignes réparties sur des processus (le résultat de chaque ligne ne dépend que de la graine et de son nom).
    with concurrent.futures.ProcessPoolExecutor(max_workers=max(1, args.processus)) as pool:
        lignes = list(pool.map(_ligne_chronometree, [(args.graine, n, v, ro, args.repetitions) for n, v, ro in choisies]))
    for l in lignes:
        print(json.dumps({k: l[k] for k in ("controle", "nul", "role", "promotions", "repetitions", "duree_s")},
                         ensure_ascii=False), flush=True)
    r = {"parametres": p, "horodatage": quand, "lignes": lignes,
         "lecture": lire(lignes) if not args.essai else {**lire(lignes), "issue": "ESSAI — aucune issue prononcée"},
         "duree_s": round(time.monotonic() - debut, 1)}
    nom = "experience-2-nul-filles-v2" + ("-ESSAI" if args.essai else "")
    ecrire_json_scelle(os.path.join(args.sortie, nom + ".json"), r)
    print(json.dumps({"duree_s": r["duree_s"], "lecture": r["lecture"]}, ensure_ascii=False))


if __name__ == "__main__":
    principal()
