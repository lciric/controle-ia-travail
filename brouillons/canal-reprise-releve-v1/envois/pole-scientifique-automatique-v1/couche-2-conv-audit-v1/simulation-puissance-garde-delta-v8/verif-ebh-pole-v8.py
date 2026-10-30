"""Vérification de la lecture e-BH simulée de la v8 contre le pôle (`pari_apparie.py`, lecture seule) :
1. `ebh_retenues` contre `ebh_pondere` sur des familles tirées au hasard (ex æquo et valeurs au bord compris, m ≥ f) ;
   (v8 : mêmes vérifications qu'en v7, cellules tirées avec en plus la dispersion combinée de A et des comparateurs, la copule gaussienne A–B, les strates
   avec ou sans étalonnage, le neuvième comparateur (k = 9) et K_s = 20)
2. chaîne entière : pour des cellules tirées au hasard, `cellule(…, ebh)` de la v8 contre une lecture refaite par le pôle sur
   les mêmes tirages bruts rejoués (`evaluer` pour la trajectoire du minimum de chaque fiche, `Course` : `entrer`,
   `ajouter_trajectoire` (arrêt à m/α_c), `lire` (e-BH)) : trajectoires, valeurs arrêtées, retenues par suite, parts.

Usage : python3 -I -B verif-ebh-pole-v8.py SCRIPT_V7 PARI_APPARIE SORTIE.json   (-B : aucun __pycache__ écrit)
"""

import hashlib
import importlib.util
import json
import math
import re
import sys

import numpy as np

SCRIPT, POLE, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("refus : lancer avec -B (aucun __pycache__ dans les dossiers lus)")


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v6 = charger("simulation_v8", SCRIPT)  # le nom `v6` est gardé dans le corps du script (vérification reprise telle quelle de la v7)
pa = charger("pari_apparie_pole", POLE)
empreinte = lambda c: hashlib.sha256(open(c, "rb").read()).hexdigest()
ECRETES = 0
PAR_CELLULE = []
bilan = {"script": SCRIPT, "script_sha256": empreinte(SCRIPT), "pari_apparie": POLE, "pari_apparie_sha256": empreinte(POLE)}

# --- 1. ebh_retenues contre ebh_pondere
rng = np.random.default_rng(np.random.SeedSequence([20261029, 1]))
cas, ecarts_ = 0, []
for _ in range(20_000):
    f = int(rng.integers(1, 21))
    m = f + int(rng.integers(0, 6))
    alpha = float(rng.choice([0.05, 0.01, 0.1]))
    le = rng.normal(math.log(m / alpha) - 1.0, 1.5, size=f)
    if rng.random() < 0.3:  # ex æquo
        le = np.round(le * 2) / 2
    if rng.random() < 0.3:  # valeurs exactement au bord de rangs tirés
        for i in rng.choice(f, size=min(f, 3), replace=False):
            le[i] = math.log(m / (alpha * int(rng.integers(1, f + 1))))
    ret = v6.ebh_retenues(le[None, :], m, alpha)[0]
    noms = [f"f{i}" for i in range(m)]
    pole = pa.ebh_pondere({noms[i]: (float(le[i]) if i < f else 0.0) for i in range(m)}, {x: alpha / m for x in noms}, alpha)
    attendu = {noms[i] for i in range(f) if ret[i]}
    cas += 1
    if pole != attendu:
        ecarts_.append({"f": f, "m": m, "alpha": alpha, "log_e": le.tolist(), "pole": sorted(pole), "v6": sorted(attendu)})
bilan["ebh_retenues_contre_ebh_pondere"] = {"familles": cas, "differences": len(ecarts_), "exemples": ecarts_[:5]}

# --- 2. chaîne entière : cellule v6 contre une lecture refaite par le pôle
def fiche_pole(g, v, delta, alpha, m):
    """g (k, n_garde), v (k, n) pour une suite : trajectoire du minimum par `evaluer`."""
    # v8 : les écarts étalonnés par strate peuvent sortir de [−1 ; 1] (écart moins décalage de strate) ; le juge les refuse : ils lui sont donnés écrêtés à [−1 ; 1], comme
    # le ferait l'analyste ; `processus` de la simulation écrête après, ce qui est identique pour le contraste et pour la garde sauf g > 1 (g = 1 et décalage négatif : cas
    # écarté par la tolérance 10⁻⁹ si présent ; le nombre de cas écrêtés est écrit)
    global ECRETES
    ECRETES += int((np.abs(v) > 1).sum() + (np.abs(g) > 1).sum())
    v, g = np.clip(v, -1.0, 1.0), np.clip(g, -1.0, 1.0)
    r = pa.evaluer({j: [float(x) for x in v[j]] for j in range(v.shape[0])},
                   {j: [float(x) for x in g[j]] for j in range(g.shape[0])}, delta, alpha, m)
    return r["trajectoire_log_min"]


def lecture_pole(trajs, alpha):
    c = pa.Course(alpha=alpha, essai=True)
    noms = [f"fiche{i}" for i in range(len(trajs))]
    c.entrer("famille", noms, alpha)
    for nom, t in zip(noms, trajs):
        c.ajouter_trajectoire(nom, t, sans_identite=True)
    atteint = [nom in c.arretees for nom in noms]
    valeurs = [c.log_e[nom] for nom in noms]
    retenues = c.lire()
    return valeurs, atteint, [nom in retenues for nom in noms]


def parts(at, ret, vraies, sujet, nulles):
    at, ret = np.array(at), np.array(ret)
    b = {"premiere_atteinte_une_fiche": float(at[:, 0].mean()),
         "premiere_atteinte_fiches_du_sujet": float(at[:, :sujet].all(axis=1).mean()),
         "retenue_une_fiche": float(ret[:, 0].mean()), "retenues_fiches_du_sujet": float(ret[:, :sujet].all(axis=1).mean()),
         "retenues_toutes_vraies": float(ret[:, :vraies].all(axis=1).mean()),
         "vraies_retenues_moyenne": float(ret[:, :vraies].sum(axis=1).mean()),
         "retenue_sans_atteinte_une_fiche": float((ret[:, 0] & ~at[:, 0]).mean())}
    if nulles:
        rn = ret[:, vraies:]
        b |= {"nulles_au_moins_une_retenue": float(rn.any(axis=1).mean()), "nulles_retenues_moyenne": float(rn.sum(axis=1).mean()),
              "proportion_de_fausses_decouvertes_moyenne": float((rn.sum(axis=1) / np.maximum(ret.sum(axis=1), 1)).mean())}
    return b


tirage = np.random.default_rng(np.random.SeedSequence([20261029, 2]))
cellules, ecart_traj, ecart_valeur, diff_retenue, diff_atteinte, diff_parts, suites, fiches_lues = 0, 0.0, 0.0, 0, 0, [], 0, 0
cellules_beta, cellules_ks, cellules_v8 = 0, 0, 0
retenues_vues, sans_atteinte_vues = 0, 0
for numero in range(96):  # v8 : 96 cellules, dont la dispersion combinée, la copule, les strates, le neuvième comparateur, K_s ≠ K_h
    K = int(tirage.choice([10, 3]))
    Ks = int(tirage.choice([K, 5, 3, 20]))
    taux = float(tirage.choice([0.01, 0.10]))
    delta = float(tirage.choice([0.05, 0.10]))
    k = int(tirage.choice([1, 3, 8, 9]))
    n = int(tirage.choice([30, 60, 120]))
    ng = int(tirage.choice([n, n + 25, max(5, n - 20)]))
    biais = float(tirage.choice([0.0, 0.0125]))
    effet = str(tirage.choice(["aucun", "logit", "logit_coupe", "beta", "comparateurs", "comparateurs_rho", "comparateurs_coupe", "comparateurs_beta",
                               "comparateurs_beta_A", "combine", "combine_copule", "combine_strates", "combine_strates_calibre", "neuvieme_logit",
                               "neuvieme_beta", "neuvieme_nulle"]))
    if effet.startswith("neuvieme"):
        k = 9
    M = int(tirage.choice([1, 2, 3]))
    N0 = int(tirage.choice([0, 0, 2]))
    alpha = float(tirage.choice([0.05, 0.01]))
    if effet.startswith("combine"):
        loi = v6.LoiSynthetique(K, Ks, taux, 0.4, 0.10, True, 0.0, True, 0.17, 0.0, 0.0, "beta", rho_b=float(tirage.choice([0.085, 0.17])),
                                corr_ab=0.6 if effet == "combine_copule" else 0.0,
                                strates=(int(tirage.choice([2, 3])), 0.3, str(tirage.choice(["sujet", "commune"])), effet == "combine_strates_calibre",
                                         str(tirage.choice(["bloc", "iid"]))) if effet.startswith("combine_strates") else None)
    elif effet.startswith("neuvieme"):
        loi = v6.LoiSynthetique(K, Ks, taux, 0.4, 0.10, True, 0.0, True, 0.0, 1.0 if effet != "neuvieme_nulle" else 0.0, 0.0,
                                "beta" if effet == "neuvieme_beta" else "logit", ecart9=0.05)
    else:
        loi = v6.LoiSynthetique(K, Ks, taux, 0.4, 0.10, True, 1.0 if effet.startswith("logit") or effet == "comparateurs_beta_A" else 0.0,
                                effet not in ("logit_coupe", "comparateurs_coupe"), 0.17 if effet == "beta" else 0.0,
                                1.0 if effet.startswith("comparateurs") else 0.0, 0.17 if effet == "comparateurs_rho" else 0.0,
                                "beta" if effet.startswith("comparateurs_beta") else "logit")
    reps = 40
    ecart_cellule = 0.0
    et = f"verif|{numero}|{loi.nom()}|delta={delta}|n={n}|n_garde={ng}|biais={biais}|k={k}"
    ebh = {"lectures": ["A", "B"], "M": M, "N": N0, "alpha": alpha,
           "nulle_A": loi.variante_nulle(True), "nulle_B": loi.variante_nulle(False)}
    res = v6.cellule(loi, loi, reps, n, ng, delta, [M / alpha], k, biais, 20261029, et, True, ebh)
    # tirages bruts rejoués dans l'ordre de `cellule` et de `lectures_ebh`
    r0, _ = v6.rng_de(20261029, et)
    modes = [loi.tirer(r0, reps, n, ng, k, biais)]
    rm, _ = v6.rng_de(20261029, et + "|ebh|modes")
    modes += [loi.tirer(rm, reps, n, ng, k, biais) for _ in range(M - 1)]
    nulles_A, nulles_B = [], None
    if N0:
        ra, _ = v6.rng_de(20261029, et + "|ebh|nulles_A")
        nulles_A = [ebh["nulle_A"].tirer(ra, reps, n, ng, k, 0.0) for _ in range(N0)]
        rb, _ = v6.rng_de(20261029, et + "|ebh|nulles_B")
        nulles_B = ebh["nulle_B"].tirer(rb, reps, n, ng, N0, 0.0)
    # trajectoires de la v6 sur les mêmes tirages (processus rejoué)
    r0, _ = v6.rng_de(20261029, et)
    v6_modes = [v6.processus(loi, r0, reps, n, ng, k, delta, biais, loi)]
    rm, _ = v6.rng_de(20261029, et + "|ebh|modes")
    v6_modes += [v6.processus(loi, rm, reps, n, ng, k, delta, biais, loi) for _ in range(M - 1)]
    for lecture in ("A", "B"):
        m = M + N0 if lecture == "A" else M * k + N0
        vraies = M if lecture == "A" else M * k
        sujet = 1 if lecture == "A" else k
        if lecture == "A":
            v6_fiches = [np.minimum(g.min(axis=0), c.min(axis=0)) for g, c in v6_modes]
        else:
            v6_fiches = [np.minimum(g[j], c[j]) for g, c in v6_modes for j in range(k)]
        AT, RET = [], []
        for r in range(reps):
            trajs = []
            for g, v in modes:
                if lecture == "A":
                    trajs.append(fiche_pole(g[r], v[r], delta, alpha, m))
                else:
                    trajs += [fiche_pole(g[r, j:j + 1], v[r, j:j + 1], delta, alpha, m) for j in range(k)]
            if lecture == "A":
                trajs += [fiche_pole(g[r], v[r], delta, alpha, m) for g, v in nulles_A]
            elif N0:
                g, v = nulles_B
                trajs += [fiche_pole(g[r, j:j + 1], v[r, j:j + 1], delta, alpha, m) for j in range(N0)]
            for i in range(vraies):
                e_ = float(np.max(np.abs(np.array(trajs[i]) - v6_fiches[i][r])))
                ecart_traj = max(ecart_traj, e_)
                ecart_cellule = max(ecart_cellule, e_)
            valeurs, atteint, retenue = lecture_pole(trajs, alpha)
            # arrêt et e-BH de la v6 sur les trajectoires du pôle, suite par suite (fiches nulles comprises)
            le_v6, at_v6, ret_v6 = v6.retenues_famille([np.array(t)[None, :] for t in trajs], m, alpha)
            diff_retenue += int([bool(x) for x in ret_v6[0]] != retenue)
            diff_atteinte += int([bool(x) for x in at_v6[0]] != atteint)
            ecart_valeur = max(ecart_valeur, float(np.max(np.abs(le_v6[0] - np.array(valeurs)))))
            # valeurs arrêtées de la v6 sur ses propres trajectoires (fiches vraies) contre la course du pôle
            for i in range(vraies):
                val, a = v6.valeur_arretee(v6_fiches[i][r:r + 1], -math.log(alpha / m))
                ecart_valeur = max(ecart_valeur, abs(float(val[0]) - valeurs[i]))
                diff_atteinte += int(bool(a[0]) != atteint[i])
            AT.append(atteint)
            RET.append(retenue)
            suites += 1
            fiches_lues += len(trajs)
            retenues_vues += sum(retenue)
            sans_atteinte_vues += sum(x and not y for x, y in zip(retenue, atteint))
        attendu = parts(AT, RET, vraies, sujet, N0)
        obtenu = {x: res[f"ebh_{lecture}"][x] for x in attendu}
        if obtenu != attendu:
            diff_parts.append({"cellule": et, "lecture": lecture, "pole": attendu, "v6": obtenu})
    cellules += 1
    PAR_CELLULE.append({"cellule": et, "effet": effet, "k": k, "ecart_max_trajectoire": ecart_cellule})
    cellules_beta += int("_beta" in loi.nom())
    cellules_v8 = cellules_v8 + 1 if (effet.startswith("combine") or effet.startswith("neuvieme")) else cellules_v8
    cellules_ks += int(Ks != K)

bilan["chaine_entiere"] = {
    "cellules": cellules, "cellules_echelle_beta": cellules_beta, "cellules_options_v8": cellules_v8, "cellules_K_s_different": cellules_ks, "lectures": 2 * cellules, "suites": suites, "fiches_lues_par_le_pole": fiches_lues,
    "fiches_retenues_vues": retenues_vues, "retenues_sans_atteinte_vues": sans_atteinte_vues,
    "ecart_max_trajectoire_minimum_v6_contre_evaluer": ecart_traj,
    "ecart_max_valeur_arretee_v6_contre_course": ecart_valeur,
    "valeurs_ecartees_de_l_intervalle_et_ecretees_pour_le_juge": ECRETES, "cellules_a_ecart_non_nul": [x for x in PAR_CELLULE if x["ecart_max_trajectoire"] > 1e-9], "differences_d_atteinte": diff_atteinte, "suites_a_retenues_differentes": diff_retenue,
    "differences_de_parts_cellule_v6_contre_pole": len(diff_parts), "exemples": diff_parts[:3]}
# v8 : écrêtage des écarts étalonnés. La simulation écrête δ − g après l'étalonnage ; le juge exige g dans [−1 ; 1] (l'analyste écrête g avant). Les deux ne diffèrent que si
# |g étalonné| > 1 (g = ±1 : tous les épisodes honnêtes de A signalés et aucun de B, ou l'inverse), possible à K_h = 3 (hors périmètre) et pas à K_h ∈ {5 ; 10}. Pour le contraste, les
# deux écrêtages sont identiques. On exige donc : écart nul (10⁻⁹) partout, sauf dans les cellules étalonnées à K_h < 5, où il doit rester < 0,1 ; et, dans le périmètre
# (K_h ∈ {5 ; 10}, ρ = 0,17, trois strates, γ = 0,4, 288 unités, k = 8, 2 000 répétitions), moins de 10⁻³ des écarts de garde étalonnés hors de [−1 ; 1] et une différence de puissance des 8 gardes (seuil 40) d'au plus 0,003 entre les deux conventions d'écrêtage.
fautives = [x for x in PAR_CELLULE if x["ecart_max_trajectoire"] > 1e-9]
hors_perimetre_ok = all(("strates" in x["cellule"] and "_calibre_" in x["cellule"] and re.search(r"_Kh([0-9]+)_", x["cellule"]) and int(re.search(r"_Kh([0-9]+)_", x["cellule"]).group(1)) < 5
                         and x["ecart_max_trajectoire"] < 0.1) for x in fautives)
rng_p = np.random.default_rng(np.random.SeedSequence([20261029, 86]))
perimetre = []
for K_h in (5, 10):
    for biais_ in (0.0, 0.0125):
        for portee in ("sujet", "commune"):
            loi_p = v6.LoiSynthetique(K_h, 10, 0.01, 0.4, 0.10, True, 0.0, True, 0.17, 0.0, 0.0, "beta", rho_b=0.17, strates=(3, 0.4, portee, True, "bloc"))
            g_p, v_p = loi_p.tirer(rng_p, 2000, 288, 288, 8, biais_)
            # puissance des 8 gardes au seuil 40 selon les deux conventions d'écrêtage (mêmes tirages) : simulation (δ − g écrêté) et juge (g écrêté, puis δ − g)
            def part_gardes(gg):
                tr = np.stack([v6.prolonger(v6.log_richesse(v6.ecreter(0.05 - gg[:, j, :])), 288) for j in range(8)])
                return float((v6.premiere_atteinte(tr.min(axis=0), 40.0) > 0).mean())
            p_sim, p_juge = part_gardes(g_p), part_gardes(np.clip(g_p, -1.0, 1.0))
            perimetre.append({"K_h": K_h, "biais": biais_, "portee": portee, "valeurs_de_garde_hors_de_l_intervalle": int((np.abs(g_p) > 1).sum()),
                              "valeurs_de_contraste_hors_de_l_intervalle": int((np.abs(v_p) > 1).sum()), "valeurs_de_garde": int(g_p.size),
                              "part_hors_de_l_intervalle": float((np.abs(g_p) > 1).mean()), "part_des_8_gardes_atteignant_40_simulation": p_sim,
                              "part_des_8_gardes_atteignant_40_ecretage_du_juge": p_juge, "difference": p_sim - p_juge})
bilan["ecretage_etalonnage"] = {"cellules_fautives": len(fautives), "toutes_etalonnees_K_h_inferieur_5_et_sous_0_1": hors_perimetre_ok, "perimetre": perimetre}
bilan["conforme"] = (not ecarts_ and not diff_parts and diff_atteinte == 0 and diff_retenue == 0 and hors_perimetre_ok
                     and all(x["part_hors_de_l_intervalle"] < 1e-3 and abs(x["difference"]) <= 0.003 for x in perimetre))
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(bilan, f, indent=1, ensure_ascii=False)
    f.write("\n")
print(json.dumps({k: v for k, v in bilan.items() if k not in ("script", "pari_apparie")}, ensure_ascii=False, indent=1)[:3000])
