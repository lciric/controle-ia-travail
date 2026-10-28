"""Contre-lecture v7 (Fable 5.1) — essai 1 : le filtre `delta0` des filles agit APRÈS la règle e-BH.

Dans `pole/cycle.py` : `_juger_pari` pose `verdict_final = "survit"` seulement si `ev["promue"]` (qui intègre la marge
`gain ≥ 2·delta0` des filles) ; `appliquer_multiplicite` calcule les e-valeurs à partir de `trajectoire_log_w` **sans**
regarder la marge, trie, calcule k*, puis ne fait que rétrograder les « survit » non retenues. Une fille à forte e-valeur
mais sans la marge est donc comptée dans k* (elle fait baisser le seuil m/(α·k) des autres) sans jamais être promue :
l'ensemble promu est une partie stricte de l'ensemble retenu par e-BH, et la preuve du contrôle du taux de fausses
découvertes (E[V/R] ≤ α) ne porte plus sur lui (le dénominateur R' = R − F rétrécit après coup).

Deux parties :
(A) construction déterministe sur la vraie fonction `appliquer_multiplicite` : une fiche nulle est promue grâce à une fille
    filtrée, et ne l'est plus quand l'e-valeur de la fille filtrée est mise à zéro avant la règle ;
(B) Monte-Carlo sous le nul avec de VRAIES e-valeurs nulles (évaluateur `selection_pari.evaluer`, loi softmax tirée au
    gabarit du proposeur, issues i.i.d. indépendantes des traits, bibliothèque standard sans urne, n = 150), dans une
    génération plausible : 2 témoins vrais promus, 3 témoins faux (nuls, réels), 3 filles « fortes mais sans marge »
    (e-valeur bornée par exp(2·delta0·n_filles) = exp(5,76), trajectoire synthétique), 12 propositions nulles réelles ;
    m = 20. On compare le taux de fausses découvertes de l'ensemble promu tel que codé et avec la correction (e-valeur
    nulle pour une fiche dont `marge_atteinte` est faux, AVANT le tri).
Aucun appel de modèle ; processeur seulement.
"""

import copy
import json
import math
import os
import random
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "copie"))

from pole import selection_pari as sp  # noqa: E402
from pole.cycle import appliquer_multiplicite  # noqa: E402
from pole.proposeurs_references import propositions_aleatoires  # noqa: E402

ALPHA, K, D, N = 0.05, 3, 4, 150
DESCRIPTION = {"traits": ["t0", "t1", "t2", "t3"], "moniteurs": {"M0": {"nombre_issues": K}}}


def issue_nulle(rng, loi, graine_monde):
    """Une fiche nulle réelle : loi tirée au gabarit, issues i.i.d. (p = [0,5 ; 0,3 ; 0,2]) sans lien aux traits."""
    instances = sp.tirer_instances(rng, N, D)
    e = sp.construire_engagement("E", loi, instances, nombre_issues=K, alpha=ALPHA, bibliotheque=sp.BIBLIOTHEQUE_STANDARD)
    gele = sp.geler_engagement(e)
    r = random.Random(graine_monde)
    issues = [sp.tirer_categorie(r, [0.5, 0.3, 0.2]) for _ in instances]
    ev = sp.evaluer(gele, {"empreinte_engagement": gele.empreinte, "issues": issues, "plan_execution": "ordre_naturel"})
    return {"pari": ev, "verdict_final": "survit" if ev["promue"] else "eliminee", "nul": True}


def issue_synthetique(log_w_final, marge_atteinte, promue, pic=None):
    """Trajectoire synthétique montant linéairement vers `log_w_final` (ou passant par `pic` puis redescendant)."""
    if pic is None:
        traj = [log_w_final * (t + 1) / N for t in range(N)]
    else:
        moitie = N // 2
        traj = [pic * (t + 1) / moitie for t in range(moitie)] + [pic + (log_w_final - pic) * (t + 1) / (N - moitie) for t in range(N - moitie)]
    ev = {"trajectoire_log_w": [round(v, 6) for v in traj], "log_richesse_finale": traj[-1], "log_richesse_max": max(traj),
          "seuil_log": math.log(1 / ALPHA), "promue": promue, "marge_atteinte": marge_atteinte}
    return {"pari": ev, "verdict_final": "survit" if promue else "eliminee", "nul": False}


def promues(issues):
    return sorted(i for i, iss in issues.items() if iss["verdict_final"] == "survit")


def appliquer_corrigee(issues, alpha):
    """Correction proposée : l'e-valeur d'une fiche dont la marge des filles n'est pas atteinte vaut 0 AVANT la règle
    (e' = e·1{marge} reste une e-valeur) ; ici, on la réalise en retirant sa trajectoire (log e = −∞)."""
    copie = copy.deepcopy(issues)
    for iss in copie.values():
        ev = iss.get("pari") or {}
        if ev.get("marge_atteinte") is False:
            ev["trajectoire_log_w"] = [-1e9] * len(ev["trajectoire_log_w"])
    appliquer_multiplicite(copie, alpha)
    return copie


def partie_a():
    """Construction déterministe : m = 3 ; F1 fille forte sans marge (trajectoire jusqu'à 5,5 : e-valeur arrêtée au premier
    passage de log(m/α) = 4,09) ; N1 nulle à log e = 3,6 (e ≈ 36,6) ; N2 nulle à log e = 0. Seuils m/(α·k) : k=1 → 60
    (log 4,09) ; k=2 → 30 (log 3,40) ; k=3 → 20 (log 3,0). Seule, N1 (3,6 < 4,09) n'est pas retenue ; avec F1 comptée,
    k* = 2 et N1 est retenue puis promue, F1 restant éliminée par la marge : l'ensemble promu est {N1}, fausse à 100 %."""
    issues = {"F1": issue_synthetique(5.5, marge_atteinte=False, promue=False),
              "N1": issue_synthetique(3.6, marge_atteinte=True, promue=True),
              "N2": issue_synthetique(0.0, marge_atteinte=True, promue=False)}
    code = copy.deepcopy(issues)
    res = appliquer_multiplicite(code, ALPHA)
    corr = appliquer_corrigee(issues, ALPHA)
    sortie = {"tel_que_code": {"retenues_par_e_bh": res["retenues"], "promues": promues(code),
                               "detail": {i: code[i]["pari"]["multiplicite"] for i in code}},
              "corrige": {"promues": promues(corr), "detail": {i: corr[i]["pari"]["multiplicite"] for i in corr}}}
    print(json.dumps(sortie, ensure_ascii=False, indent=1))
    assert sortie["tel_que_code"]["promues"] == ["N1"], "tel que codé : la nulle N1 est promue grâce à la fille filtrée F1"
    assert sortie["corrige"]["promues"] == [], "corrigé : plus rien n'est promu"
    return sortie


def partie_b(repetitions=2000, graine=20261027):
    rng = random.Random(graine)
    compte = {"code": {"V": 0, "R": 0, "fdp_somme": 0.0, "au_moins_une_fausse": 0},
              "corrige": {"V": 0, "R": 0, "fdp_somme": 0.0, "au_moins_une_fausse": 0},
              "nulles_promues_seules_par_le_code": 0, "repetitions": 0}
    lois = [p["loi_predictive"] for p in propositions_aleatoires(DESCRIPTION, 12 + 3, graine, 0)]
    debut = time.time()
    for r in range(repetitions):
        issues = {}
        # 2 témoins vrais promus (e-valeur forte), hors du nul
        issues["V1"] = issue_synthetique(10.0, True, True)
        issues["V2"] = issue_synthetique(9.0, True, True)
        # 3 filles fortes sans marge : log e final tiré dans [3 ; 2·delta0·n_filles = 5,76], marge non atteinte
        for f in range(3):
            issues[f"F{f}"] = issue_synthetique(rng.uniform(3.0, 5.76), marge_atteinte=False, promue=False)
        # 3 témoins faux + 12 propositions : nulles réelles (lois tirées au gabarit, issues i.i.d.)
        for j, loi in enumerate(lois):
            issues[f"N{j:02d}"] = issue_nulle(rng, loi, graine * 1000003 + r * 101 + j)
        code = copy.deepcopy(issues)
        appliquer_multiplicite(code, ALPHA)
        corr = appliquer_corrigee(issues, ALPHA)
        for nom, iss in (("code", code), ("corrige", corr)):
            prom = promues(iss)
            v = sum(1 for i in prom if iss[i]["nul"])
            compte[nom]["V"] += v
            compte[nom]["R"] += len(prom)
            compte[nom]["fdp_somme"] += (v / len(prom)) if prom else 0.0
            compte[nom]["au_moins_une_fausse"] += v > 0
        nulles_code = {i for i in promues(code) if code[i]["nul"]}
        nulles_corr = {i for i in promues(corr) if corr[i]["nul"]}
        compte["nulles_promues_seules_par_le_code"] += len(nulles_code - nulles_corr)
        compte["repetitions"] += 1
    for nom in ("code", "corrige"):
        compte[nom]["FDR_estime"] = compte[nom]["fdp_somme"] / compte["repetitions"]
        compte[nom]["taux_au_moins_une_fausse_promue"] = compte[nom]["au_moins_une_fausse"] / compte["repetitions"]
    compte["duree_s"] = round(time.time() - debut, 1)
    print(json.dumps(compte, ensure_ascii=False, indent=1))
    return compte


if __name__ == "__main__":
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    rapport = {"partie_A": partie_a(), "partie_B": partie_b(reps)}
    with open(os.path.join(ICI, "resultat-essai-ebh-filtre-delta0.json"), "w", encoding="utf-8") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1)
