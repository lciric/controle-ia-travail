"""Contre-lecture v7 (Fable 5.1) — essai 2 bis : héritage de la preuve sur les mêmes données quand le membre dominant du nul
est une loi FIXE (le prédicteur connu), sans l'avantage de regret de la marginale ajustée.

Nul exact : les issues d'épreuve sont tirées de la loi « connu:M0 » que le noyau ajuste sur la partie de calibrage (la
loi du monde est donc un membre de la bibliothèque de chaque fiche : toute promotion est une fausse découverte).
Fiche A_g (génération g = 0, 1, 2) : la loi « connu » déformée (poids × (1 + δ), δ = 0,35 ; divergence faible), même loi à
chaque génération (ce que fait le chercheur mécanique, dont la liste est déterministe), acceptée comme redite avec
héritage ; promotion de la classe par la règle de `_juger_pari` : cumul + log W max ≥ log(1/α).
Bras : tranches = 1 (mêmes 150 instances et mêmes issues à chaque génération) contre tranches = 3 (une tranche fraîche par
génération, le cas valide « produit d'e-valeurs sur des tirages frais »). Attendu si valide : taux ≤ α = 0,05.
"""

import json
import os
import random
import shutil
import sys
import tempfile
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "copie"))

from pole import selection_pari as sp  # noqa: E402
from pole.cycle import Budget, ConfigGeneration, Generation  # noqa: E402
from pole.fiche import RegistreGel  # noqa: E402
from pole.memoire import Memoire  # noqa: E402
from pole.monde_banque import MondeBanque, ajuster_softmax  # noqa: E402
from pole.outils import ecrire_json_scelle  # noqa: E402
from pole.proposeur import valider_proposition  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

ALPHA, K, D, DELTA = 0.05, 3, 4, 0.35
_CACHE = {}
_ref = Memoire._reference


def _reference_en_cache(self, k, d):
    cle = (self.graine, k, d)
    if cle not in _CACHE:
        _CACHE[cle] = _ref(self, k, d)
    return _CACHE[cle]


Memoire._reference = _reference_en_cache  # accélération seulement (graine fixe : mêmes valeurs)
VRAIE = {"type": "softmax", "poids": [[-0.9, 0.5, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.9, -0.5, 0.0, 0.0]], "biais": [0.0, 0.2, 0.0]}


def banque_du_connu(chemin, rng, n_cal=40, n_epr=450):
    """Calibrage tiré de VRAIE ; « connu » ajusté dessus par le noyau (même fonction) ; épreuve tirée DE « connu »."""
    cal = []
    for i in range(n_cal):
        z = [round(rng.gauss(0, 1), 6) for _ in range(D)]
        cal.append({"identifiant": f"c{i:04d}", "z": z, "g": i % 2,
                    "issues": {"M0": sp.tirer_categorie(rng, sp.proba(VRAIE, {"z": z, "g": i % 2}, [], 0))}, "partie": "calibrage"})
    connu = ajuster_softmax([l["z"] for l in cal], [l["issues"]["M0"] for l in cal], K, 1.0)
    epr = []
    for i in range(n_epr):
        z = [round(rng.gauss(0, 1), 6) for _ in range(D)]
        epr.append({"identifiant": f"e{i:04d}", "z": z, "g": i % 2,
                    "issues": {"M0": sp.tirer_categorie(rng, sp.proba(connu, {"z": z, "g": i % 2}, [], 0))}, "partie": "epreuve"})
    ecrire_json_scelle(chemin, {"nom": "nul-connu", "traits": [f"t{t}" for t in range(D)], "sous_populations": 2,
                                "moniteurs": {"M0": {"nombre_issues": K, "instances": n_cal + n_epr}}, "instances": cal + epr})
    return connu


def juger(monde, config, fiche, numero, racine, memoire):
    g = Generation(numero, AdaptateurSimule(1, MondeSimule(1)), config, racine, RegistreGel(), Budget(100.0),
                   memoire=memoire, monde_noyau=monde)
    refus = g.geler(fiche)
    assert refus is None, refus
    issue = g._juger_temoin_sans_agent(fiche)
    assert "pari" in issue, issue
    return issue


def une_repetition(r, tranches, generations, dossier):
    rng = random.Random(9_000_000 + r)
    chemin = os.path.join(dossier, "banque.json")
    connu = banque_du_connu(chemin, rng)
    monde = MondeBanque(chemin, 11 + r, nul_informe=True, tranches=tranches)
    membre = monde.membres_informes(type("F", (), {"espace_instances": {"moniteur": "M0", "nombre_issues": K, "dimension": D}})())[0]
    assert membre["loi"] == connu, "le membre « connu » du noyau est bien la loi qui a tiré l'épreuve"
    config = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=False, graine=100 + r, taille_plan=150,
                              taille_plan_filles=150, instants_filles=6, part_calibrage=12, multiplicite="aucune",
                              nul_archive=True, nul_archive_ajuste=True).valider()
    deformee = {"type": "softmax", "poids": [[round(w * (1 + DELTA), 6) for w in ligne] for ligne in connu["poids"]],
                "biais": list(connu["biais"])}
    memoire = Memoire(active=True, graine=3)
    cumul, promue_classe, trajets, communes = 0.0, False, [], []
    plan_precedent = None
    for g in range(generations):
        prop = {"enonce": f"Nul connu déformé, tentative {g}", "strategie": "au_dela_du_connu", "moniteur": "M0", "loi_predictive": deformee}
        fiche = valider_proposition(prop, monde, ALPHA, f"A{g}", "essai")
        memoire.nouvelle_generation()
        garde = memoire.garde_redite(fiche)
        if not garde["accepte"]:
            assert "survivante" in garde["motif"] and promue_classe, garde
            break
        if g > 0:
            assert "héritage" in garde["motif"], garde
            h = memoire.heritage(fiche.identifiant)
            assert abs(h["cumul"] - cumul) < 1e-9, (h, cumul)
        issue = juger(monde, config, fiche, g, os.path.join(dossier, f"g{g}"), memoire)
        ev = issue["pari"]
        e = json.load(open(os.path.join(dossier, f"g{g}", "archive", "generations", f"generation-{g:02d}", f"A{g}", "experience", "engagement.json")))
        plan = {json.dumps(i, sort_keys=True) for i in e["instances"]}
        if plan_precedent is not None:
            communes.append(len(plan & plan_precedent) / len(plan))
        plan_precedent = plan
        promue = (cumul + ev["log_richesse_max"] >= ev["seuil_log"]) and ev.get("marge_atteinte", True)  # règle de _juger_pari
        trajets.append({"g": g, "log_w_final": round(ev["log_richesse_finale"], 3), "log_w_max": round(ev["log_richesse_max"], 3),
                        "cumul_avant": round(cumul, 3), "promue": promue})
        fiche.statut = "survit" if promue else "eliminee"
        memoire.indexer(fiche, issue, g)
        cumul += ev["log_richesse_finale"]  # ce que fait _indexer_classe
        if promue:
            promue_classe = True
            break
    return {"classe_promue": promue_classe, "promue_a_la_premiere": trajets[0]["promue"], "trajets": trajets,
            "part_instances_communes": communes}


def bras(nom, tranches, generations, repetitions):
    base = tempfile.mkdtemp(prefix="heritage-connu-", dir=ICI)
    debut = time.time()
    total = {"bras": nom, "tranches": tranches, "generations": generations, "repetitions": repetitions,
             "classe_promue": 0, "promue_a_la_premiere": 0, "promue_par_heritage": 0, "parts_communes": []}
    try:
        for r in range(repetitions):
            d = os.path.join(base, f"r{r:04d}")
            os.makedirs(d)
            res = une_repetition(r, tranches, generations, d)
            shutil.rmtree(d, True)
            total["classe_promue"] += res["classe_promue"]
            total["promue_a_la_premiere"] += res["promue_a_la_premiere"]
            total["promue_par_heritage"] += res["classe_promue"] and not res["promue_a_la_premiere"]
            total["parts_communes"] += res["part_instances_communes"]
    finally:
        shutil.rmtree(base, True)
    pc = total.pop("parts_communes")
    total["part_instances_communes_moyenne"] = round(sum(pc) / len(pc), 4) if pc else None
    total["taux_classe_promue"] = total["classe_promue"] / repetitions
    total["taux_promue_a_la_premiere"] = total["promue_a_la_premiere"] / repetitions
    total["taux_promue_par_heritage_seul"] = total["promue_par_heritage"] / repetitions
    total["duree_s"] = round(time.time() - debut, 1)
    print(json.dumps(total, ensure_ascii=False), flush=True)
    return total


if __name__ == "__main__":
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    rapport = [bras("memes_donnees_3_generations", 1, 3, reps), bras("tranches_fraiches_3_generations", 3, 3, reps)]
    with open(os.path.join(ICI, "resultat-essai-heritage-nul-connu.json"), "w", encoding="utf-8") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1)
