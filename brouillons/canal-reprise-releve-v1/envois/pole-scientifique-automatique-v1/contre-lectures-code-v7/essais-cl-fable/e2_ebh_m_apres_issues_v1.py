"""E2 : la règle e-BH compte dans m les seules fiches **jugées** (avec `pari`), c'est-à-dire un nombre fixé après les
issues ; une fiche dont l'agent échoue (indécise, rejetée) sort de m. Mesure, sous le nul de permutation de la banque
(aucune fiche vraie), la probabilité qu'au moins une fiche soit promue après e-BH (= taux de fausses découvertes ici) :
(a) agents honnêtes : les 78 fiches sont jugées ; (b) agents qui, voyant `mesures.json` et `engagement.json`, calculent
leur propre richesse et n'envoient pas de bloc JSON quand elle est basse (la fiche devient « indécise », hors de m) ;
(c) correction proposée : m = fiches gelées, e = 0 pour les non jugées.

La fonction e-BH employée est `pole.cycle.appliquer_multiplicite`, telle quelle ; les issues sont bâties comme
`Generation._juger_pari` les bâtit (clé `pari` présente pour les seules fiches jugées).

Usage : python -I -B e2_ebh_m_apres_issues_v1.py COPIE_DU_CODE SORTIE.json PERMUTATIONS URNE(0|1) INFORME(0|1)
"""
import copy
import json
import math
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aide_noyau_v1 as a  # noqa: E402
from pole.cycle import appliquer_multiplicite  # noqa: E402

sortie, R = sys.argv[2], int(sys.argv[3])
URNE, INFORME = sys.argv[4] == "1", sys.argv[5] == "1"
config = a.config_ligne_de_commande(multiplicite="e-bh", urne=URNE)
alpha = config.alpha
population = a.charger(a.POPULATION_V2)
SEUILS_CENSURE = (0.0, 1.0, 2.0, math.log(20))
debut = time.time()
compte = {"honnete": 0, "correction_m_fixe": 0, **{f"censure_finale_sous_{c:.2f}": 0 for c in SEUILS_CENSURE}}
m_moyen = {f"censure_finale_sous_{c:.2f}": 0 for c in SEUILS_CENSURE}
par_fiche = 0
for r in range(R):
    monde = a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=INFORME)
    rng = random.Random(a.graine_derivee(778, "permutation", r))
    for nom in sorted(monde.banque["moniteurs"]):
        lignes = [l for l in monde.banque["instances"] if l.get("partie", "epreuve") == "epreuve" and nom in l["issues"]]
        valeurs = [l["issues"][nom] for l in lignes]
        rng.shuffle(valeurs)
        for l, v in zip(lignes, valeurs):
            l["issues"][nom] = v
    jugees = {}
    for i, d in enumerate(population):
        f = a.fiche_depuis(d, identifiant=f"G0-F{i:02d}")
        _, ev, _ = a.juger(f, monde, config)
        jugees[f.identifiant] = {"verdict_final": "survit" if ev["promue"] else "eliminee", "motif": "", "pari": ev}
    par_fiche += any(i["verdict_final"] == "survit" for i in jugees.values())
    # (a) honnête
    issues = copy.deepcopy(jugees)
    appliquer_multiplicite(issues, alpha)
    compte["honnete"] += any(i["verdict_final"] == "survit" for i in issues.values())
    # (b) censure par l'agent : bloc JSON absent → « indécise », sans clé `pari` (comme `traiter`)
    for c in SEUILS_CENSURE:
        issues = {}
        for ident, i in jugees.items():
            if i["pari"]["log_richesse_finale"] >= c:
                issues[ident] = copy.deepcopy(i)
            else:
                issues[ident] = {"verdict_final": "indecise", "motif": "exécution en échec ou bloc JSON absent"}
        r_m = appliquer_multiplicite(issues, alpha)
        cle = f"censure_finale_sous_{c:.2f}"
        compte[cle] += any(i["verdict_final"] == "survit" for i in issues.values())
        m_moyen[cle] += r_m["m"]
    # (c) correction : m = 78 fiches gelées, les non jugées comptent avec e = 0 (censure la plus forte)
    c = math.log(20)
    issues = {}
    for ident, i in jugees.items():
        if i["pari"]["log_richesse_finale"] >= c:
            issues[ident] = copy.deepcopy(i)
        else:
            issues[ident] = {"verdict_final": "indecise", "motif": "", "pari": {"trajectoire_log_w": [-1e9]}}
    appliquer_multiplicite(issues, alpha)
    compte["correction_m_fixe"] += any(i["verdict_final"] == "survit" for i in issues.values())
resultat = {"urne": URNE, "nul_informe": INFORME, "permutations": R, "fiches_par_generation": len(population), "alpha": alpha,
            "taux_au_moins_une_promue_par_fiche_sans_multiplicite": par_fiche / R,
            "taux_au_moins_une_promue": {k: v / R for k, v in compte.items()},
            "m_moyen_sous_censure": {k: v / R for k, v in m_moyen.items()}, "duree_s": round(time.time() - debut, 1)}
with open(sortie, "w", encoding="utf-8") as fo:
    json.dump(resultat, fo, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
