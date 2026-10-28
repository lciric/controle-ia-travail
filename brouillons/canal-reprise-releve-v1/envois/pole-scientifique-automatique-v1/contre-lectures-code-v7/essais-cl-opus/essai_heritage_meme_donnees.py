"""Contre-lecture v7 (Fable 5.1) — essai 2 : héritage de la preuve sur un monde sur banque SANS tranches = produit de deux
e-valeurs calculées sur les MÊMES issues.

`pole/memoire.py` (`_indexer_classe`) cumule `log_richesse_finale` par classe ; `pole/cycle.py` (`_juger_pari`) promeut une
redite si `cumul + log_richesse_max ≥ log(1/α)`. Valide sur des tirages frais (produit d'e-valeurs indépendantes). Sur
`MondeBanque` avec `tranches=1` (défaut de la ligne de commande et des démonstrations), une redite de même loi reçoit le
même plan (mêmes instances, choisies par divergence) et les mêmes issues (lues dans la banque) : l'e-valeur de la classe
est alors W·W' avec W' ≈ W, qui n'est pas une e-valeur.

Protocole (processeur seulement, code du dépôt) : pour chaque répétition, une banque nulle (issues i.i.d. [0,5 ; 0,3 ; 0,2]
indépendantes des traits, 40 lignes de calibrage, 300 lignes d'épreuve), une loi tirée au gabarit du proposeur
(`propositions_aleatoires`), fiche A gelée et jugée en génération 0 par le chemin réel (`Generation.geler` + `_juger_temoin_sans_agent`,
qui ne diffère du chemin avec agents que par le rangement des issues déposées) ; puis fiche A' (même loi, autre identifiant)
acceptée comme redite par `Memoire.garde_redite` (héritage), jugée en génération 1 sur le même monde ; promotion de la
classe = promue(A) ou (cumul(A) + log W max(A') ≥ log 1/α), comme dans `_juger_pari`.
Bras : tranches=1 (mêmes données) contre tranches=2 (seconde tranche fraîche) ; pari plein et pari à fraction.
Attendu si l'héritage est valide : taux de promotion de la classe ≤ α = 0,05 dans tous les bras.
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

from pole.cycle import Budget, ConfigGeneration, Generation  # noqa: E402
from pole.fiche import RegistreGel  # noqa: E402
from pole.memoire import Memoire  # noqa: E402
from pole.monde_banque import MondeBanque  # noqa: E402
from pole.outils import ecrire_json_scelle  # noqa: E402
from pole.proposeur import valider_proposition  # noqa: E402
from pole.proposeurs_references import propositions_aleatoires  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

ALPHA, K, D = 0.05, 3, 4
_CACHE_REFERENCE = {}
_reference_origine = Memoire._reference


def _reference_en_cache(self, k, d):
    cle = (self.graine, k, d)
    if cle not in _CACHE_REFERENCE:
        _CACHE_REFERENCE[cle] = _reference_origine(self, k, d)
    return _CACHE_REFERENCE[cle]


Memoire._reference = _reference_en_cache  # accélération seulement : mêmes valeurs (graine fixe)
P_NUL = [0.5, 0.3, 0.2]


def banque_nulle(chemin, rng, n_cal=40, n_epr=300):
    instances = []
    for i in range(n_cal + n_epr):
        z = [round(rng.gauss(0, 1), 6) for _ in range(D)]
        u, cumul, y = rng.random(), 0.0, K - 1
        for k, p in enumerate(P_NUL):
            cumul += p
            if u < cumul:
                y = k
                break
        instances.append({"identifiant": f"i{i:04d}", "z": z, "g": i % 2, "issues": {"M0": y},
                          "partie": "calibrage" if i < n_cal else "epreuve"})
    ecrire_json_scelle(chemin, {"nom": "nulle", "traits": [f"t{t}" for t in range(D)], "sous_populations": 2,
                                "moniteurs": {"M0": {"nombre_issues": K, "instances": n_cal + n_epr}}, "instances": instances})


def juger(monde, config, fiche, numero, racine, memoire):
    """Gel + jugement par le noyau seul (même évaluateur que le chemin avec agents)."""
    g = Generation(numero, AdaptateurSimule(1, MondeSimule(1)), config, racine, RegistreGel(), Budget(100.0),
                   memoire=memoire, monde_noyau=monde)
    refus = g.geler(fiche)
    assert refus is None, refus
    issue = g._juger_temoin_sans_agent(fiche)
    assert "pari" in issue, issue
    return issue


def une_repetition(r, tranches, pari_fraction, dossier, echelle=1.0):
    rng = random.Random(7_000_000 + r)
    chemin = os.path.join(dossier, "banque.json")
    banque_nulle(chemin, rng)
    monde = MondeBanque(chemin, 11 + r, nul_informe=True, tranches=tranches)
    config = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=False, graine=100 + r, taille_plan=150,
                              taille_plan_filles=150, instants_filles=6, part_calibrage=12, multiplicite="aucune",
                              pari_fraction=pari_fraction, nul_archive=True, nul_archive_ajuste=True).valider()
    description = monde.description_publique()
    prop = propositions_aleatoires(description, 1, 500 + r, 0)[0]
    if echelle != 1.0:  # loi nulle « douce » : poids réduits (régime où W reste proche de 1)
        loi = prop["loi_predictive"]
        loi["poids"] = [[round(w * echelle, 6) for w in ligne] for ligne in loi["poids"]]
    a = valider_proposition(prop, monde, ALPHA, "A", "ref", references=True)
    a2 = valider_proposition(dict(prop, enonce=prop["enonce"] + " (redite)"), monde, ALPHA, "A2", "ref", references=True)
    memoire = Memoire(active=True, graine=3)
    memoire.nouvelle_generation()
    garde0 = memoire.garde_redite(a)
    assert garde0["accepte"]
    issue_a = juger(monde, config, a, 0, os.path.join(dossier, "g0"), memoire)
    ev_a = issue_a["pari"]
    a.statut = "survit" if ev_a["promue"] else "eliminee"
    memoire.indexer(a, issue_a, 0)
    memoire.nouvelle_generation()
    garde1 = memoire.garde_redite(a2)
    if a.statut == "survit":
        # redite d'une survivante : refusée ; la classe est déjà promue
        return {"promue_a": True, "redite_acceptee": False, "classe_promue": True, "cumul": None, "log_w_max_a2": None,
                "memes_instances": None}
    assert garde1["accepte"] and "héritage" in garde1["motif"], garde1
    heritage = memoire.heritage("A2")
    assert heritage is not None and abs(heritage["cumul"] - ev_a["log_richesse_finale"]) < 1e-9
    issue_a2 = juger(monde, config, a2, 1, os.path.join(dossier, "g1"), memoire)
    ev_a2 = issue_a2["pari"]
    # exactement la règle de `_juger_pari` (héritage) :
    promue_classe = (heritage["cumul"] + ev_a2["log_richesse_max"] >= ev_a2["seuil_log"]) and ev_a2.get("marge_atteinte", True)
    # mêmes instances ?
    e_a = json.load(open(os.path.join(dossier, "g0", "archive", "generations", "generation-00", "A", "experience", "engagement.json")))
    e_b = json.load(open(os.path.join(dossier, "g1", "archive", "generations", "generation-01", "A2", "experience", "engagement.json")))
    ia = {json.dumps(i, sort_keys=True) for i in e_a["instances"]}
    ib = {json.dumps(i, sort_keys=True) for i in e_b["instances"]}
    return {"promue_a": False, "redite_acceptee": True, "classe_promue": bool(promue_classe), "cumul": heritage["cumul"],
            "log_w_max_a2": ev_a2["log_richesse_max"], "log_w_final_a": ev_a["log_richesse_finale"],
            "memes_instances": len(ia & ib) / len(ia)}


def bras(nom, tranches, pari_fraction, repetitions, echelle=1.0):
    base = tempfile.mkdtemp(prefix="heritage-", dir=ICI)
    debut = time.time()
    total = {"bras": nom, "tranches": tranches, "pari_fraction": pari_fraction, "echelle_poids": echelle, "repetitions": repetitions,
             "promue_a_seule": 0, "classe_promue": 0, "redites_acceptees": 0, "part_instances_communes_moyenne": 0.0,
             "cumul_positif": 0, "promues_par_heritage": 0}
    parts = []
    try:
        for r in range(repetitions):
            d = os.path.join(base, f"r{r:04d}")
            os.makedirs(d)
            res = une_repetition(r, tranches, pari_fraction, d, echelle)
            shutil.rmtree(d, True)
            total["promue_a_seule"] += res["promue_a"]
            total["classe_promue"] += res["classe_promue"]
            total["redites_acceptees"] += res["redite_acceptee"]
            if res["redite_acceptee"]:
                total.setdefault("log_w_final_a", []).append(round(res["log_w_final_a"], 3))
                parts.append(res["memes_instances"])
                total["cumul_positif"] += res["cumul"] > 0
                total["promues_par_heritage"] += res["classe_promue"]
    finally:
        shutil.rmtree(base, True)
    total["part_instances_communes_moyenne"] = round(sum(parts) / len(parts), 4) if parts else None
    total["taux_promue_a_seule"] = total["promue_a_seule"] / repetitions
    total["taux_classe_promue"] = total["classe_promue"] / repetitions
    total["duree_s"] = round(time.time() - debut, 1)
    print(json.dumps(total, ensure_ascii=False))
    return total


if __name__ == "__main__":
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    rapport = [bras("memes_donnees_pari_plein_poids_pleins", 1, False, reps, 1.0),
               bras("memes_donnees_pari_plein_poids_doux", 1, False, reps, 0.25),
               bras("memes_donnees_pari_fraction_poids_doux", 1, True, reps, 0.25),
               bras("tranche_fraiche_pari_plein_poids_doux", 2, False, reps, 0.25)]
    with open(os.path.join(ICI, "resultat-essai-heritage-meme-donnees.json"), "w", encoding="utf-8") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1)
