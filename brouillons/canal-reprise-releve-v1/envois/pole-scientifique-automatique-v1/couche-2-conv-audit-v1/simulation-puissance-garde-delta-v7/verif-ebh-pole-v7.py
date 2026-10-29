"""Vérification de la lecture e-BH simulée de la v7 contre le pôle (`pari_apparie.py`, lecture seule) :
1. `ebh_retenues` contre `ebh_pondere` sur des familles tirées au hasard (ex æquo et valeurs au bord compris, m ≥ f) ;
   (v7 : mêmes vérifications qu'en v6, cellules tirées avec en plus l'échelle bêta des comparateurs et K_s ≠ K_h)
2. chaîne entière : pour des cellules tirées au hasard, `cellule(…, ebh)` de la v7 contre une lecture refaite par le pôle sur
   les mêmes tirages bruts rejoués (`evaluer` pour la trajectoire du minimum de chaque fiche, `Course` : `entrer`,
   `ajouter_trajectoire` (arrêt à m/α_c), `lire` (e-BH)) : trajectoires, valeurs arrêtées, retenues par suite, parts.

Usage : python3 -I -B verif-ebh-pole-v7.py SCRIPT_V7 PARI_APPARIE SORTIE.json   (-B : aucun __pycache__ écrit)
"""

import hashlib
import importlib.util
import json
import math
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


v6 = charger("simulation_v7", SCRIPT)  # le nom `v6` est gardé dans le corps du script (vérification reprise telle quelle)
pa = charger("pari_apparie_pole", POLE)
empreinte = lambda c: hashlib.sha256(open(c, "rb").read()).hexdigest()
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
cellules_beta, cellules_ks = 0, 0
retenues_vues, sans_atteinte_vues = 0, 0
for numero in range(72):  # v7 : 72 cellules, dont l'échelle bêta des comparateurs et K_s ≠ K_h
    K = int(tirage.choice([10, 3]))
    Ks = int(tirage.choice([K, 5, 3]))
    taux = float(tirage.choice([0.01, 0.10]))
    delta = float(tirage.choice([0.05, 0.10]))
    k = int(tirage.choice([1, 3, 8]))
    n = int(tirage.choice([30, 60, 120]))
    ng = int(tirage.choice([n, n + 25, max(5, n - 20)]))
    biais = float(tirage.choice([0.0, 0.0125]))
    effet = str(tirage.choice(["aucun", "logit", "logit_coupe", "beta", "comparateurs", "comparateurs_rho", "comparateurs_coupe", "comparateurs_beta",
                               "comparateurs_beta_A"]))
    M = int(tirage.choice([1, 2, 3]))
    N0 = int(tirage.choice([0, 0, 2]))
    alpha = float(tirage.choice([0.05, 0.01]))
    loi = v6.LoiSynthetique(K, Ks, taux, 0.4, 0.10, True, 1.0 if effet.startswith("logit") or effet == "comparateurs_beta_A" else 0.0,
                            effet not in ("logit_coupe", "comparateurs_coupe"), 0.17 if effet == "beta" else 0.0,
                            1.0 if effet.startswith("comparateurs") else 0.0, 0.17 if effet == "comparateurs_rho" else 0.0,
                            "beta" if effet.startswith("comparateurs_beta") else "logit")
    reps = 40
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
                ecart_traj = max(ecart_traj, float(np.max(np.abs(np.array(trajs[i]) - v6_fiches[i][r]))))
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
    cellules_beta += int("_beta" in loi.nom())
    cellules_ks += int(Ks != K)

bilan["chaine_entiere"] = {
    "cellules": cellules, "cellules_echelle_beta": cellules_beta, "cellules_K_s_different": cellules_ks, "lectures": 2 * cellules, "suites": suites, "fiches_lues_par_le_pole": fiches_lues,
    "fiches_retenues_vues": retenues_vues, "retenues_sans_atteinte_vues": sans_atteinte_vues,
    "ecart_max_trajectoire_minimum_v6_contre_evaluer": ecart_traj,
    "ecart_max_valeur_arretee_v6_contre_course": ecart_valeur,
    "differences_d_atteinte": diff_atteinte, "suites_a_retenues_differentes": diff_retenue,
    "differences_de_parts_cellule_v6_contre_pole": len(diff_parts), "exemples": diff_parts[:3]}
bilan["conforme"] = (not ecarts_ and not diff_parts and diff_atteinte == 0 and diff_retenue == 0 and ecart_traj < 1e-9
                     and ecart_valeur < 1e-9)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(bilan, f, indent=1, ensure_ascii=False)
    f.write("\n")
print(json.dumps({k: v for k, v in bilan.items() if k not in ("script", "pari_apparie")}, ensure_ascii=False, indent=1)[:3000])
