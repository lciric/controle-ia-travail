"""Annexe des valeurs prédites (formes closes, bornes, seuils) de la grille brouillon 1 — calcul exact, sans tirage."""
import json, sys, math
from scipy import stats
from controle_ia.simulation_essaim import calibrage as C
g = json.load(open(sys.argv[1]))
a, q = g["alpha"], g["q"]
FC = ["somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne", "coelev_comptage"]
L = []
L += ["# Annexe — valeurs prédites de la simulation d'essaim (grille brouillon 1)", "",
      "Calculées sans tirage par `controle_ia.simulation_essaim.calibrage` (fonctions citées), α = 0,05, q = 0,1, "
      f"u = Φ⁻¹(0,9) = {C.seuil_par_case(q):.6f}. Valeurs à 4 décimales ; la lecture gelée les recalcule en double précision.", "",
      "## A. Seuils exacts sous la loi de référence (`seuils_exacts`) et ρ* de `e_pas` (`rho_e_pas`)", "",
      "Seuil (c, γ) : alarme si V > c, ou V = c et U < γ ; γ = 1 pour une statistique continue (alarme si V ≥ c).", "",
      "| config | " + " | ".join(FC) + " | ρ* |", "|---|" + "---|" * (len(FC) + 1)]
for cfg, c in g["configs"].items():
    s = C.seuils_exacts(c["K"], c["T"], q, a)
    cel = []
    for k in FC:
        v, gm = s[k]
        cel.append(f"{v:.4f}" if gm == 1.0 else f"({v:.0f} ; {gm:.4f})")
    L.append(f"| {cfg} (K = {c['K']}, T = {c['T']}) | " + " | ".join(cel) + f" | {C.rho_e_pas(c['K'], c['T'], a):.5f} |")
L += ["", "## B. HE4 — classe M, puissances exactes (`puissances_decalage(motif(...))`)", ""]
for cfg, specs in g["M"].items():
    K, T = g["configs"][cfg]["K"], g["configs"][cfg]["T"]
    s = C.seuils_exacts(K, T, q, a)
    L += [f"### {cfg} (K = {K}, T = {T})", "", "| menace | B | m | " + " | ".join(FC) + " |", "|---|---|---|" + "---|" * len(FC)]
    for sp in specs:
        th = C.puissances_decalage(C.motif(sp["genre"], K, T, sp["B"], sp["m"]), q, a, s)
        L.append(f"| {sp['genre']} | {sp['B']} | {sp['m']} | " + " | ".join(f"{th[k]:.4f}" for k in FC) + " |")
    L.append("")
L += ["## C. HE2.3 — bornes inférieures exactes sous synchronisation (r = 1)", "",
      "Co-élévation (comptage) : `borne_synchro`. Moyenne par pas (m = K) : (1 − Φ(c_T/√K)^T)^K. "
      "Co-élévation continue (m = K) : P(Bin(K, 1 − Φ(c₃/3)^T) ≥ 3), c₃ = seuil Monte-Carlo du run (non connu avant le run).", "",
      "| config | m | borne coelev_comptage | borne pas_moyenne (m = K) | au-dessus prédit (règle) |", "|---|---|---|---|---|"]
for cfg, specs in g["C"].items():
    K, T = g["configs"][cfg]["K"], g["configs"][cfg]["T"]
    s = C.seuils_exacts(K, T, q, a)
    for sp in specs:
        if sp["genre"] != "synchro":
            continue
        lb = C.borne_synchro(K, T, sp["m"], q, s["coelev_comptage"])
        lbp = (1 - stats.norm.cdf(s["pas_moyenne"][0] / math.sqrt(K)) ** T) ** K if sp["m"] == K else None
        L.append(f"| {cfg} | {sp['m']} | {lb:.4f} | {'—' if lbp is None else f'{lbp:.4f}'} | {', '.join(sp['lecture_au_dessus']) or '—'} |")
L += ["", "## D. HE3.6 — taux de fausses alarmes exacts des seuils de référence hors hypothèses (`fausses_alarmes_reference`)", "",
      "Seuils calibrés sous cases iid N(0, 1) (« cases supposées indépendantes »), appliqués sous la loi indiquée. α = 0,05.", "",
      "| config | loi | " + " | ".join(FC) + " |", "|---|---|" + "---|" * len(FC)]
for cfg in g["HE3"]["configs"]:
    K, T = g["configs"][cfg]["K"], g["configs"][cfg]["T"]
    s = C.seuils_exacts(K, T, q, a)
    for x in g["HE3"]["lois"]:
        if x["loi"]["type"] == "iid":
            continue
        th = C.fausses_alarmes_reference(x["loi"], K, T, q, a, s)
        L.append(f"| {cfg} | {x['nom']} | " + " | ".join(f"{th[k]:.4f}" if k in th else "—" for k in FC) + " |")
bas, haut, t = C.region_conforme(g["HE3"]["conforme"]["L"], g["HE3"]["conforme"]["n_test"], g["HE3"]["conforme"]["K"], a, g["lecture"]["gamma"])
n = g["HE3"]["conforme"]["L"] * g["HE3"]["conforme"]["n_test"]
L += ["", "## E. HE3.5 — région d'acceptation exacte du calibrage conforme (`region_conforme`)", "",
      f"K = 1 000 essaims honnêtes entiers, L = 50 tirages, 400 essais chacun : taux théorique 1 − 951/1001 = {t:.5f}. "
      f"Nombre total d'alarmes accepté sur {n} essais au niveau 1 − 10⁻⁵ : [{bas} ; {haut}] (taux [{bas/n:.4f} ; {haut/n:.4f}]).", ""]
open(sys.argv[2], "x", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L))
