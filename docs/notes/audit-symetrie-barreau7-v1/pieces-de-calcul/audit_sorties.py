"""Audit de symétrie (R4), septième barreau : contrôles sur les seules sorties scellées (résultat, manifeste)."""
import json, sys, math
r = json.load(open(sys.argv[1]))["resultat"]; man = json.load(open(sys.argv[2]))
EPS = 1e-9
print("configuration du manifeste :", man["config"]["configuration_du_texte"], "| décisif :", man["decisif"], "| dépôt propre :", man["depot_propre"])
print("n_tirages, n_plancher, n_permutations, tolérance :", man["config"]["n_tirages"], man["config"]["n_plancher"], man["config"]["n_permutations"], man["config"]["tolerance"])
decl = {"placebo_sous_C2": [], "tout_1_et_plancher_0_99": [], "intervalle_sous_0_5": [], "constants": [], "audit_code": []}
for mo, M in r["modeles"].items():
    for nom, c in sorted(M["cellules"].items()):
        ic = c["intervalle"]; bas, haut, m = ic["bas"], ic["haut"], c["marge"]
        if c.get("etat") is None and c.get("ligne") is None:
            ligne = None
        elif not c["lisible"] or ic["degeneres"] > 0.01 * ic["n_tirages"]: ligne = "C1"
        elif bas >= m - EPS: ligne = "C2"
        elif haut < m - EPS: ligne = "C3"
        else: ligne = "C4"
        pl, pb = c.get("plancher"), c.get("placebo")
        ok = (ligne == c.get("ligne"))
        A = c.get("aires") or [a for p in c.get("aires_plis", []) for a in p["aires"]]; c["aires"] = A; tout1 = all(x == 1.0 for x in A)
        q = pl.get("q95") if pl else None
        if ligne == "C2" and pb and bas <= pb["q95"] + EPS: decl["placebo_sous_C2"].append((mo, nom))
        if tout1 and q is not None and q >= 0.99: decl["tout_1_et_plancher_0_99"].append((mo, nom))
        if haut < 0.5: decl["intervalle_sous_0_5"].append((mo, nom, bas, haut))
        if c.get("audit"): decl["audit_code"].append((mo, nom, c["audit"]))
        if c.get("etat") and "garde" in str(c["etat"]): decl["constants"].append((mo, nom))
        print(f"{mo:14s} {nom:34s} ligne refaite {ligne} (code {c.get('ligne')}, {'égal' if ok else 'ÉCART'}) est={c['estimation']:.6f} [{bas:.6f};{haut:.6f}] m={m} n_aires={len(c['aires'])} min_aire={min(c['aires']):.4f} tout1={tout1}"
              + (f" plancher q95={q:.4f} méd={pl.get('mediane')} max={pl.get('max')} marge_bas-q95={bas-q:.4f}" if q is not None else " sans plancher")
              + (f" placebo q95={pb['q95']:.4f} décl={pb.get('declenche')}" if pb else ""))
    for couche, L in M["lecture_par_agent"].items():
        for f, x in L["familles"].items():
            if x.get("etat") != "lu": decl["constants"].append((mo, "par agent", couche, f, x.get("etat")))
            elif x["haut"] < 0.5: decl["intervalle_sous_0_5"].append((mo, "lecture par agent", couche, f, x["aire"], x["bas"], x["haut"]))
print("\nDÉCLENCHEURS (à la lettre du texte) :")
for k, v in decl.items(): print(" ", k, ":", v if v else "aucun")
# lecture par agent : tableau symétrique (intervalles entiers au-dessus et au-dessous de 0,5) pour Mahalanobis
print("\nMahalanobis par agent : côté de l'intervalle")
for mo, M in r["modeles"].items():
    for couche, L in M["lecture_par_agent"].items():
        x = L["familles"]["mahalanobis"]
        cote = "entier sous 0,5" if x["haut"] < .5 else ("entier au-dessus de 0,5" if x["bas"] > .5 else "contient 0,5")
        print(f"  {mo} c{couche}: {x['aire']:.4f} [{x['bas']:.4f};{x['haut']:.4f}] {cote} ; placebo q95 {x['placebo']['q95']:.4f}")
# placebo attendu sous séparation parfaite : aire = 1 - k/20 à peu près, k ~ Bin(20, 1/2)
n = 20; cdf = 0; 
for k in range(n + 1):
    cdf += math.comb(n, k) / 2 ** n
    if cdf >= 0.05: print(f"\nplacebo attendu sous séparation parfaite (approximation 1-k/20, k binomial) : quantile 0,95 ≈ {1-k/n:.3f}"); break
print("écart type de l'aire sous étiquettes au hasard, 20 contre 20 :", round(math.sqrt(41 / 4800), 4), "→ quantile 0,95 ≈", round(.5 + 1.645 * math.sqrt(41 / 4800), 3))
print("réponse :", r["lecture"]["reponse"]["ligne"], "| règle T :", {k: v.get("ligne") for k, v in r["lecture"]["regle_t"].items()})
