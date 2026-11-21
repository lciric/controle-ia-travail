"""Lecture gelée de l'idée 1.2 : la table des critères du texte scellé (sections « Métrique », « Seuil », « Critères de
lecture gelés », « Prédiction chiffrée ») écrite en code.

Entrées : la sortie scellée du jeu (`oracle.json`, `jeu.json`, sous `diag/organisme-idees-juge-v1/<run>/`), vérifiées par
empreinte et rattachées au même manifeste avant toute lecture (R1). Sortie : `lecture-gelee-v1.json`, scellée.

Conventions (lecture du texte, dites au rapport) : intervalle percentile à 95 % = quantiles 2,5 % et 97,5 %
(`numpy.quantile`, interpolation linéaire) de 10 000 moyennes rééchantillonnées ; le rééchantillon b tire ses indices de
générations de la graine `(99, b)` de la racine (même b pour toutes les statistiques d'un même ensemble de générations :
différences appariées) ; Clopper-Pearson à 95 % par la loi bêta ; McNemar exact bilatéral (loi binomiale ½ sur les paires
discordantes). Lecture (3) : 10 000 rééchantillons (O5).
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.stats import beta, binom, binomtest

from ..gardes import GardeArret
from ..scellement import sceller, verifier
from . import banc_tirages_repartis_v1 as B
from . import rejeu_v1 as R

REECHANTILLONS = 10_000
NOMS_SORTIE = ("oracle", "jeu")


# --- outils statistiques ---------------------------------------------------------------------------------------------
def seuils_validite(n: int, bras: int = 7, taux: float = 0.05) -> tuple[int, int]:
    """Annexe B du texte : « tenue » si k ≤ kt, « non tenue » si k ≥ knt, au niveau 0,05/bras (Bonferroni)."""
    lv = 0.05 / bras
    kt = max((k for k in range(n + 1) if binom.cdf(k, n, taux) <= lv), default=-1)       # −1 : jamais « tenue »
    knt = min((k for k in range(n + 1) if binom.sf(k - 1, n, taux) <= lv), default=n + 1)  # n + 1 : jamais « non tenue »
    return kt, knt


def statut_validite(k: int, kt: int, knt: int) -> str:
    return "tenue" if k <= kt else ("non tenue" if k >= knt else "non jugeable")


def clopper_pearson(k: int, n: int) -> tuple[float, float]:
    bas = 0.0 if k == 0 else float(beta.ppf(0.025, k, n - k + 1))
    haut = 1.0 if k == n else float(beta.ppf(0.975, k + 1, n - k))
    return bas, haut


def mcnemar_exact(a: np.ndarray, b: np.ndarray) -> dict:
    a, b = np.asarray(a, bool), np.asarray(b, bool)
    n10, n01 = int((a & ~b).sum()), int((~a & b).sum())
    p = 1.0 if n10 + n01 == 0 else float(binomtest(n10, n10 + n01, 0.5).pvalue)
    return {"a_seul": n10, "b_seul": n01, "p_bilaterale": p}


class Reechantillonneur:
    """Indices de rééchantillonnage des générations, graines (99, b), mis en cache par taille d'ensemble."""

    def __init__(self, racine: int, reechantillons: int = REECHANTILLONS):
        self.racine, self.r, self._idx = racine, reechantillons, {}

    def indices(self, n: int) -> np.ndarray:
        if n not in self._idx:
            self._idx[n] = np.stack([B.generateur(self.racine, 99, b).integers(0, n, size=n) for b in range(self.r)]).astype(np.int32)
        return self._idx[n]

    def intervalle(self, v) -> dict:
        v = np.asarray(v, dtype=float)
        if v.size == 0:
            return {"estimation": None, "bas": None, "haut": None, "n": 0}
        moy = v[self.indices(len(v))].mean(axis=1)
        bas, haut = np.quantile(moy, [0.025, 0.975])
        return {"estimation": float(v.mean()), "bas": float(bas), "haut": float(haut), "n": int(len(v))}


# --- chargement --------------------------------------------------------------------------------------------------------
def charger_sortie(dossier: Path) -> dict:
    """Vérifie les empreintes et le rattachement au manifeste, puis charge ; refuse toute sortie non scellée (R1)."""
    dossier = Path(dossier)
    corps, shas = {}, {}
    for nom in NOMS_SORTIE:
        chemin = dossier / f"{nom}.json"
        try:
            shas[nom] = verifier(chemin)
        except GardeArret as e:
            raise GardeArret(f"lecture avant scellement de la sortie : {e} (run invalide)") from None
        corps[nom] = json.loads(chemin.read_text(encoding="utf-8"))
    manifestes = {c["manifeste_sha256"] for c in corps.values()}
    runs = {c["run_id"] for c in corps.values()}
    if len(manifestes) != 1 or len(runs) != 1:
        raise GardeArret("sorties rattachées à des manifestes différents")
    return {"run_id": runs.pop(), "manifeste_sha256": manifestes.pop(), "sha256": shas,
            "oracle": corps["oracle"]["resultat"], "jeu": corps["jeu"]["resultat"]}


def _apparier(sortie: dict) -> dict:
    oracle = {(t["famille"], t["g"]): t for t in sortie["oracle"]["generations"]}
    jeu = {(t["famille"], t["g"]): t for t in sortie["jeu"]["generations"]}
    if set(oracle) != set(jeu):
        raise GardeArret("oracle et jeu ne portent pas les mêmes générations")
    for cle, j in jeu.items():
        o = oracle[cle]
        if [c["empreinte_loi"] for c in o["cartes"]] != [c["empreinte_loi"] for c in j["cartes"]]:
            raise GardeArret(f"génération {cle} : cartes de l'oracle ≠ cartes du jeu")
        if j["oracle_scelle_sha256"] != sortie["sha256"]["oracle"]:
            raise GardeArret(f"génération {cle} : jouée sous un autre oracle que celui scellé")
    return {"oracle": oracle, "jeu": jeu}


# --- lecture -------------------------------------------------------------------------------------------------------------
def _famille(apparie: dict, famille: str) -> list[tuple[dict, dict]]:
    cles = sorted(k for k in apparie["jeu"] if k[0] == famille)
    return [(apparie["jeu"][k], apparie["oracle"][k]) for k in cles]


def lecture_validite(gens_N: list, gens_T: list, rs: Reechantillonneur, n_attendu: int | None = None) -> dict:
    n = len(gens_N)
    kt, knt = seuils_validite(n)
    if n_attendu == 500 and (kt, knt) != (13, 39):
        raise GardeArret(f"seuils de validité recalculés {kt}, {knt} ≠ 13, 39 (annexe B)")
    mondes = {"M0": [i for i, (j, _) in enumerate(gens_N) if j["g"] < B.BORNE_M0],
              "M0prime": [i for i, (j, _) in enumerate(gens_N) if j["g"] >= B.BORNE_M0]}
    sortie = {"generations": n, "seuils": {"tenue_si_au_plus": kt, "non_tenue_si_au_moins": knt}, "bras": {}, "par_monde": {}}
    for nom in R.BRAS_N:
        promo = np.array([len(j["bras"][nom]["promues"]) > 0 for j, _ in gens_N])
        k = int(promo.sum())
        sortie["bras"][nom] = {"generations_avec_promotion": k, "part": k / n if n else None,
                               "clopper_pearson": clopper_pearson(k, n) if n else None, "statut": statut_validite(k, kt, knt)}
    for nom_monde, idx in mondes.items():
        if not idx:
            continue
        kt_w, knt_w = seuils_validite(len(idx))
        sortie["par_monde"][nom_monde] = {"generations": len(idx), "seuils_pour_memoire": [kt_w, knt_w], "bras": {}}
        for nom in R.BRAS_N:
            k = int(sum(len(gens_N[i][0]["bras"][nom]["promues"]) > 0 for i in idx))
            sortie["par_monde"][nom_monde]["bras"][nom] = {"generations_avec_promotion": k, "statut_sans_critere": statut_validite(k, kt_w, knt_w)}
    # membres exacts promus (Q2), dans toutes les familles et tous les bras
    exacts = []
    for fam, gens in (("N", gens_N), ("T", gens_T)):
        sorte = B.SORTE_MEMBRE_EXACT[fam]
        for j, _ in gens:
            for nom, r in j["bras"].items():
                for i in r["promues"]:
                    if j["cartes"][i]["sorte"] == sorte:
                        exacts.append({"famille": fam, "g": j["g"], "bras": nom, "carte": i})
    sortie["membres_exacts_promus"] = exacts
    # domination (lecture 2), recalculée sur les trajectoires et Λ rangés
    franchies = []
    for j, _ in gens_N:
        for c in j["cartes"]:
            for k_inst, ex in B.domination(c["trajectoire"], c["log_lambda"]):
                franchies.append({"g": j["g"], "carte": c["indice"], "instant": B.INSTANTS[k_inst], "exces": ex})
    sortie["dominations_franchies"] = franchies
    # moyenne des valeurs e (lecture 3) : 7 + 42 = 49 intervalles sur les 500 générations ; par monde, rapportés
    sortes = B.SORTES_UNIQUES["N"]

    def intervalles(indices):
        bloc = {}
        for nom in R.BRAS_N:
            E = np.exp(np.array([gens_N[i][0]["bras"][nom]["log_e"] for i in indices], dtype=float))
            d = {"toutes": rs.intervalle(E.mean(axis=1))}
            for s in sortes:
                cols = [c for c, nom_s in enumerate(B.SORTES["N"]) if nom_s == s]
                d[s] = rs.intervalle(E[:, cols].mean(axis=1))
            bloc[nom] = d
        return bloc

    tous = list(range(n))
    sortie["moyennes_valeurs_e"] = intervalles(tous) if n else {}
    sortie["intervalles_comptes"] = sum(len(d) for d in sortie["moyennes_valeurs_e"].values())
    if n_attendu == 500 and sortie["intervalles_comptes"] != 49:
        raise GardeArret(f"lecture (3) : {sortie['intervalles_comptes']} intervalles au lieu de 49 (7 + 42, O4)")
    sortie["moyennes_valeurs_e_par_monde"] = {w: intervalles(idx) for w, idx in mondes.items() if idx}
    depasse = [(nom, s, d["bas"]) for nom, ds in sortie["moyennes_valeurs_e"].items() for s, d in ds.items()
               if d["bas"] is not None and d["bas"] > 1.0]
    audit_mondes = [(w, nom, s, d["bas"]) for w, bl in sortie["moyennes_valeurs_e_par_monde"].items()
                    for nom, ds in bl.items() for s, d in ds.items() if d["bas"] is not None and d["bas"] > 1.0]
    sortie["bornes_basses_au_dessus_de_1"] = depasse
    sortie["audit_ecrit_requis_par_monde"] = audit_mondes
    defauts = []
    if any(b["statut"] == "non tenue" for b in sortie["bras"].values()):
        defauts.append("validité « non tenue » dans un bras")
    if exacts:
        defauts.append("promotion d'un membre exact")
    if franchies:
        defauts.append("domination franchie")
    if depasse:
        defauts.append("borne basse d'une moyenne des valeurs e > 1 (l'un des 49 intervalles)")
    sortie["defauts_etage_1"] = defauts
    sortie["non_jugeables"] = [nom for nom, b in sortie["bras"].items() if b["statut"] == "non jugeable"]
    return sortie


def lecture_famille_T(gens_T: list, rs: Reechantillonneur) -> dict:
    n = len(gens_T)
    porteuse = B.SORTE_PORTEUSE["T"]
    classes = [[c["classe"] for c in o["cartes"]] for _, o in gens_T]
    sortes = list(B.SORTES["T"])
    couv, fp, fp_sorte, pv, psg, err, tir = {}, {}, {}, {}, {}, {}, {}
    for nom in R.BRAS_T:
        couv[nom] = np.array([any(classes[x][i] == "porteuse" for i in j["bras"][nom]["promues"]) for x, (j, _) in enumerate(gens_T)])
        fp[nom] = np.array([sum(classes[x][i] == "fausse" for i in j["bras"][nom]["promues"]) for x, (j, _) in enumerate(gens_T)], float)
        fp_sorte[nom] = {s: np.array([sum(classes[x][i] == "fausse" and sortes[i] == s for i in j["bras"][nom]["promues"])
                                      for x, (j, _) in enumerate(gens_T)], float)
                         for s in ("copies de la classe", "copies par morceaux", "fausses construites", "nulles")}
        pv[nom] = np.array([sum(classes[x][i] == "partiellement vraie" for i in j["bras"][nom]["promues"]) for x, (j, _) in enumerate(gens_T)], float)
        psg[nom] = np.array([sum(classes[x][i] == "porteuse sans gain" for i in j["bras"][nom]["promues"]) for x, (j, _) in enumerate(gens_T)], float)
        err[nom] = (~couv[nom]).astype(float) + fp[nom]
        tir[nom] = np.array([j["bras"][nom]["tirages"] for j, _ in gens_T], float)
    B_tot = B.M * B.PART
    sortie = {"generations": n, "couverture": {}, "fausses_promotions": {}, "tirages": {}, "differences": {}}
    for nom in R.BRAS_T:
        k = int(couv[nom].sum())
        sortie["couverture"][nom] = {"estimation": k / n, "clopper_pearson": clopper_pearson(k, n), "couvertes": k}
        sortie["fausses_promotions"][nom] = {"moyenne": float(fp[nom].mean()),
                                             "par_sorte": {s: float(v.mean()) for s, v in fp_sorte[nom].items()},
                                             "partiellement_vraies_promues": float(pv[nom].mean()),
                                             "porteuses_sans_gain_promues": float(psg[nom].mean()),
                                             "erreurs_de_decision": float(err[nom].mean())}
        part = tir[nom] / B_tot
        sortie["tirages"][nom] = {"consommation_sur_B_moyenne": float(part.mean()),
                                  "quantiles": [float(q) for q in np.quantile(part, [0, 0.25, 0.5, 0.75, 1])],
                                  "economie": float(1 - part.mean())}
    paires = {"A-F": ("A", "F"), "A-F125": ("A", "F125"), "A-P": ("A", "P"), "A-P-prime": ("A", "P-prime"),
              "F-F-arret": ("F", "F-arret")}
    for cle, (a, b) in paires.items():
        sortie["differences"][cle] = {"couverture": rs.intervalle(couv[a].astype(float) - couv[b].astype(float)),
                                      "mcnemar": mcnemar_exact(couv[a], couv[b])}
    sortie["differences"]["FP_A-FP_F"] = rs.intervalle(fp["A"] - fp["F"])
    sortie["differences"]["economie_F-arret"] = rs.intervalle(1 - tir["F-arret"] / B_tot)
    # doses
    haute = [x for x, (j, _) in enumerate(gens_T) if j["dose_haute"]]
    basse = [x for x, (j, _) in enumerate(gens_T) if not j["dose_haute"]]
    d_af = couv["A"].astype(float) - couv["F"].astype(float)
    sortie["doses"] = {"haute": rs.intervalle(d_af[haute]), "basse": rs.intervalle(d_af[basse])}
    # cellules
    cel = {}
    for c in range(10):
        idx = [x for x, (j, _) in enumerate(gens_T) if j["cellule"] == c]
        if not idx:
            continue
        cel[c] = {"type": gens_T[idx[0]][0]["type"], "dose": gens_T[idx[0]][0]["dose"], "generations": len(idx),
                  "couverture": {nom: float(couv[nom][idx].mean()) for nom in R.BRAS_T},
                  "fausses_promotions": {nom: float(fp[nom][idx].mean()) for nom in R.BRAS_T},
                  "consommation_sur_B": {nom: float((tir[nom][idx] / B_tot).mean()) for nom in R.BRAS_T},
                  "A-F": float(d_af[idx].mean())}
    sortie["cellules"] = cel
    # mécanisme et audit (R4)
    recus = {}
    for nom in R.BRAS_T:
        par_sorte, par_classe, arrets = {}, {}, {"haut": 0, "bas": 0, "plafond": 0, "fin": 0}
        bas_porteuses, porteuses_au_dela = 0, 0
        for x, (j, _) in enumerate(gens_T):
            r = j["bras"][nom]
            for i in range(B.M):
                t = 25 * r["blocs"][i]
                par_sorte.setdefault(sortes[i], []).append(t)
                par_classe.setdefault(classes[x][i], []).append(t)
                arrets[r["arrets"][i]] += 1
                if classes[x][i] == "porteuse":
                    bas_porteuses += r["arrets"][i] == "bas"
                    porteuses_au_dela += t > B.PART
        total = n * B.M
        recus[nom] = {"par_sorte": {s: float(np.mean(v)) for s, v in par_sorte.items()},
                      "par_classe": {s: float(np.mean(v)) for s, v in par_classe.items()},
                      "parts_arrets": {k: v / total for k, v in arrets.items()},
                      "porteuses_arretees_bas": bas_porteuses, "porteuses_au_dela_de_200": porteuses_au_dela}
    sortie["tirages_recus"] = recus
    sortie["classes_oracle"] = {k: int(sum(cl.count(k) for cl in classes)) for k in ("porteuse", "porteuse sans gain", "fausse", "partiellement vraie")}
    sortie["A_egal_F_partout"] = all(j["bras"]["A"]["blocs"] == j["bras"]["F"]["blocs"] for j, _ in gens_T)
    return sortie


def lire(sortie: dict, racine: int, reechantillons: int = REECHANTILLONS, n_attendus: dict | None = None) -> dict:
    """Étages 1 à 5 dans l'ordre du texte ; « garantie mise en défaut » arrête la lecture (rien d'autre n'est lu)."""
    apparie = _apparier(sortie)
    gens_N, gens_T = _famille(apparie, "N"), _famille(apparie, "T")
    n_attendus = n_attendus or {}
    for fam, gens in (("N", gens_N), ("T", gens_T)):
        if fam in n_attendus and len(gens) != n_attendus[fam]:
            raise GardeArret(f"famille {fam} : {len(gens)} générations au lieu de {n_attendus[fam]} : run incomplet, aucune lecture")
    rs = Reechantillonneur(racine, reechantillons)
    validite = lecture_validite(gens_N, gens_T, rs, n_attendus.get("N"))
    res = {"run_id": sortie["run_id"], "sorties_sha256": sortie["sha256"], "reechantillons": reechantillons,
           "etage_1": {"validite": validite}}
    if validite["defauts_etage_1"]:
        res["verdict"] = "garantie mise en défaut"
        res["etage_1"]["verdict"] = "garantie mise en défaut : défaut de code ou de preuve ; rien d'autre n'est lu ; audit ; nœud"
        return res
    res["etage_1"]["verdict"] = "validité tenue (aucun défaut de l'étage 1)"
    reserve = bool(validite["non_jugeables"])
    res["etage_1_bis"] = {"non_jugeables": validite["non_jugeables"],
                          "verdict": "validité non établie : principale lue sous cette réserve, aucune adoption ne peut s'en réclamer"
                          if reserve else "sans objet"}
    T = lecture_famille_T(gens_T, rs)
    res["famille_T"] = T
    c_f = T["couverture"]["F"]["estimation"]
    hors_zone = c_f <= 0.05 or c_f >= 0.95
    res["etage_2"] = {"C_F": c_f, "verdict": "hors de la zone utile (non concluant)" if hors_zone else "dans la zone utile"}
    if hors_zone:
        principale = "hors de la zone utile"
        res["etage_3"] = {"verdict": "non lu (hors de la zone utile)"}
        res["etage_4"] = {"verdict": "non lu"}
    else:
        d = T["differences"]["A-F"]["couverture"]
        dfp = T["differences"]["FP_A-FP_F"]
        if d["haut"] < 0 or dfp["bas"] > 0.02:
            principale = "nuisible"
        elif d["bas"] > 0 and d["estimation"] >= 0.05 and dfp["haut"] <= 0.05:
            principale = "gain"
        elif d["haut"] < 0.02:
            principale = "pas de gain"
        else:
            principale = "non tranché"
        res["etage_3"] = {"C_A-C_F": d, "FP_A-FP_F": dfp, "verdict": principale}
        if principale == "gain":
            eff = T["differences"]["A-F125"]["couverture"]["haut"] < 0
            cib = T["differences"]["A-P"]["couverture"]["haut"] <= 0
            q = ("d'effectif seulement et sans effet de ciblage" if eff and cib else "d'effectif seulement" if eff
                 else "sans effet de ciblage" if cib else "de structure")
            res["etage_4"] = {"A-F125": T["differences"]["A-F125"]["couverture"], "A-P": T["differences"]["A-P"]["couverture"],
                              "A-P-prime (rapporté)": T["differences"]["A-P-prime"]["couverture"], "verdict": q}
        else:
            res["etage_4"] = {"verdict": "non lu (la principale ne rend pas « gain »)",
                              "A-P-prime (rapporté)": T["differences"]["A-P-prime"]["couverture"]}
    res["etage_5"] = {"economie_F-arret": T["differences"]["economie_F-arret"],
                      "perte_de_couverture_F-F-arret": T["differences"]["F-F-arret"]["couverture"]}
    res["verdict"] = principale + (" (sous la réserve « validité non établie »)" if reserve else "")
    res["predictions"] = predictions(validite, T)
    if hors_zone:
        res["predictions"]["note"] = "principale non lue (hors de la zone utile) : prédictions rapportées sans valeur de verdict"
    res["audit_R4"] = indicateurs_audit(validite, T, res["predictions"])
    return res


def predictions(V: dict, T: dict) -> dict:
    """Q1 à Q9 : chiffre observé, « tenue » (le chiffre prédit est atteint) et « réfutée » (le critère de réfutation du
    texte est atteint). Rapporté ; le verdict est celui des étages."""
    d_af = T["differences"]["A-F"]["couverture"]
    q = {}
    ks = {nom: b["generations_avec_promotion"] for nom, b in V["bras"].items()}
    q["Q1"] = {"observe": ks, "tenue": all(k <= 13 for k in ks.values()), "refutee": any(k >= 39 for k in ks.values())}
    q["Q2"] = {"observe": len(V["membres_exacts_promus"]), "tenue": not V["membres_exacts_promus"], "refutee": bool(V["membres_exacts_promus"])}
    q["Q3"] = {"observe": {"A-F": d_af, "dose_haute": T["doses"]["haute"], "dose_basse": T["doses"]["basse"]},
               "tenue": d_af["estimation"] >= 0.05 and d_af["bas"] > 0 and (T["doses"]["haute"]["estimation"] or 0) >= 0.08
               and (T["doses"]["basse"]["estimation"] or 0) <= 0.05,
               "refutee": d_af["haut"] < 0.02}
    d125 = T["differences"]["A-F125"]["couverture"]
    q["Q4"] = {"observe": d125, "tenue": d125["estimation"] >= 0, "refutee": d125["haut"] < 0}
    dp = T["differences"]["A-P"]["couverture"]
    q["Q5"] = {"observe": {"A-P": dp, "A-P-prime": T["differences"]["A-P-prime"]["couverture"]},
               "tenue": dp["estimation"] >= 0.02, "refutee": dp["haut"] <= 0}
    dfp = T["differences"]["FP_A-FP_F"]
    fps = {nom: v["moyenne"] for nom, v in T["fausses_promotions"].items()}
    q["Q6"] = {"observe": {"moyennes": fps, "FP_A-FP_F": dfp},
               "tenue": all(v <= 0.10 for v in fps.values()) and dfp["haut"] <= 0.05, "refutee": dfp["bas"] > 0.02}
    eco = T["differences"]["economie_F-arret"]["estimation"]
    perte = T["differences"]["F-F-arret"]["couverture"]["estimation"]
    q["Q7"] = {"observe": {"economie": eco, "perte": perte}, "tenue": eco >= 0.25 and perte <= 0.02,
               "refutee": eco < 0.10 or perte > 0.05}
    t_p = T["tirages_recus"]["A"]["par_classe"].get("porteuse")
    q["Q8"] = {"observe": t_p, "tenue": t_p is not None and t_p >= 300, "refutee": t_p is not None and t_p < 230}
    moy = {nom: d["toutes"]["estimation"] for nom, d in V["moyennes_valeurs_e"].items()}
    q["Q9"] = {"observe": {"dominations": len(V["dominations_franchies"]), "moyennes": moy},
               "tenue": not V["dominations_franchies"] and all(v <= 0.8 for v in moy.values()),
               "refutee": bool(V["dominations_franchies"]) or bool(V["bornes_basses_au_dessus_de_1"])}
    return q


def indicateurs_audit(V: dict, T: dict, Q: dict) -> dict:
    """Éléments de l'audit de symétrie (R4), à écrire par le lecteur avant le prononcé : ce code ne prononce rien."""
    diffs = [c["A-F"] for c in T["cellules"].values()]
    aucune_fp = all(v["moyenne"] == 0 for v in T["fausses_promotions"].values())
    return {
        "trop_propre": {"gain_identique_dans_toutes_les_cellules": len(set(diffs)) == 1,
                        "aucune_fausse_promotion_nulle_part": aucune_fp,
                        "toutes_les_predictions_tenues": all(x["tenue"] for k, x in Q.items() if k.startswith("Q"))},
        "tout_negatif": {"A_egal_F_partout": T["A_egal_F_partout"],
                         "aucune_carte_arretee_bas_sous_A": T["tirages_recus"]["A"]["parts_arrets"]["bas"] == 0,
                         "economie_nulle_F-arret": T["tirages"]["F-arret"]["economie"] == 0,
                         "aucune_porteuse_au_dela_de_200_sous_A": T["tirages_recus"]["A"]["porteuses_au_dela_de_200"] == 0},
        "porteuses_arretees_bas": {nom: r["porteuses_arretees_bas"] for nom, r in T["tirages_recus"].items()},
        "partiellement_vraies_promues": {nom: v["partiellement_vraies_promues"] for nom, v in T["fausses_promotions"].items()},
        "audit_par_monde_requis": V["audit_ecrit_requis_par_monde"],
    }


def ecrire_lecture(dossier: Path, racine: int, reechantillons: int = REECHANTILLONS, n_attendus: dict | None = None) -> Path:
    dossier = Path(dossier)
    cible = dossier / "lecture-gelee-v1.json"
    if cible.exists():
        raise GardeArret(f"{cible} existe déjà : R12 interdit d'écraser")
    sortie = charger_sortie(dossier)
    res = lire(sortie, racine, reechantillons, n_attendus)
    corps = {"run_id": sortie["run_id"], "manifeste_sha256": sortie["manifeste_sha256"], "resultat": res}
    cible.write_text(json.dumps(corps, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(cible)
    return cible
