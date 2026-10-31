#!/usr/bin/env python3
"""Calcul de puissance de l'arène « mélange d'équilibre » — v1, sur la sortie du pilote en RACINE_ESSAI seulement.

Lit le fichier d'essai produit par `arene_melange_v1.py essai` (refuse tout fichier dont la racine est une racine de
décision), puis :
1. rappelle l'estimation pilote de chaque contraste apparié (moyenne, écart-type, intervalle à 95 % par
   rééchantillonnage, déjà dans le fichier) ;
2. simule la règle de confirmation primaire « estimation ≥ S1 et borne basse à 95 % > 0, dans les deux δ » par
   rééchantillonnage conjoint des instances pilotes (les deux δ partagent la loi cible d'une instance), écarts centrés
   puis décalés d'un effet vrai e ; borne basse par l'approximation de Student (la décision emploie le percentile du
   rééchantillonnage ; l'écart est déclaré) ;
3. donne la puissance par nombre d'instances N et effet e, l'effet minimal détectable à 0,8 et 0,9, l'erreur de
   première espèce à e = 0 ;
4. mesure le temps processeur par tâche, par tour et par bras, et en déduit le N maximal sous le plafond.

    PYTHONPATH=src python3 calcul-puissance-arene-melange-v1.py ESSAI.json > SORTIE.txt
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import arene_melange_v1 as am  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

GRAINE_SIMULATION = (am.RACINE_ESSAI, 0, 0, 0, 0, 77)  # dérivée de la racine d'essai, rôle 77 : simulation de puissance
N_GRILLE = (10, 15, 20, 30, 40, 60, 80, 100, 150)
E_GRILLE = (0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10, 0.12, 0.15)
S1_CANDIDATS = (0.0, 0.02, 0.03, 0.05)
N_SIM = 4000
PLAFOND_MUR_S = 2 * 3600.0
COEURS = 2


def mesure(r, nom, k):
    return am._mesure(r["bras"][nom], k)


def ecarts(res, b1, b2, k):
    """Matrice (instances × 2 δ) des écarts appariés, instances communes aux deux δ."""
    par = {}
    for r in res:
        par.setdefault(r["instance"], {})[r["code_delta"]] = mesure(r, b1, k) - mesure(r, b2, k)
    inst = sorted(i for i, v in par.items() if set(v) == {1, 2})
    return np.array([[par[i][1], par[i][2]] for i in inst])


def puissance(D, N, e, s1, rng, n_sim=N_SIM, alpha=0.05):
    """P(confirmation dans les deux δ) ; D centré puis décalé de e ; borne basse de Student bilatérale à 95 %."""
    Dc = D - D.mean(0) + e
    idx = rng.integers(0, len(Dc), size=(n_sim, N))
    X = Dc[idx]                                    # n_sim × N × 2
    m = X.mean(1)
    se = X.std(1, ddof=1) / np.sqrt(N)
    lb = m - stats.t.ppf(1 - alpha / 2, N - 1) * se
    ok = (m >= s1) & (lb > 0)
    return float(np.mean(ok.all(1))), float(np.mean(ok[:, 0])), float(np.mean(ok[:, 1]))


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    corps = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    man = corps["manifeste"]
    am.exiger_racines_essai(man["racine"], man["racine_tenue"])
    if corps.get("mode") != "essai":
        raise GardeArret("fichier qui n'est pas un essai : refusé")
    res = corps["resultats"]
    if any(r["racine"] in am.RACINES_DECISION or r["racine_tenue"] in am.RACINES_DECISION for r in res):
        raise GardeArret("résultat tiré d'une racine de décision : refusé")
    if man["config_sha256"] != am.CONFIG_V1.empreinte():
        raise GardeArret("configuration de l'essai différente de CONFIG_V1 du code")
    rng = np.random.default_rng(np.random.SeedSequence(entropy=GRAINE_SIMULATION[0], spawn_key=GRAINE_SIMULATION[1:]))

    print("# Calcul de puissance — arène mélange d'équilibre — v1 (RACINE_ESSAI seulement)")
    print(f"fichier d'essai : {argv[0]}")
    print(f"racine = {man['racine']} ; racine des tenues = {man['racine_tenue']} ; configuration {man['config_sha256']}")
    print(f"code : {man['versions']['code_sha256']} ; commit {man['versions']['commit']} ; numpy "
          f"{man['versions']['numpy']} ; scipy {man['versions']['scipy']}")
    n_inst = len({r['instance'] for r in res})
    print(f"tâches lues : {len(res)} ({n_inst} instances × 2 valeurs de δ = {am.CONFIG_V1.deltas})")
    print()

    print("## 1. Moyennes par bras (pilote)")
    for cd, bloc in sorted(corps["analyse"].items()):
        print(f"δ code {cd} (δ = {am.CONFIG_V1.deltas[int(cd) - 1]}), n = {bloc['n']}")
        for nom, mo in bloc["moyennes"].items():
            print(f"  {nom} : (iii) {mo['V_iii_final']:.4f} ; (ii) {mo['ii_final']:.4f} ; (i) {mo['i_final_vus']:.4f} ;"
                  f" coût (fraction de δ) {mo['cout.fraction']:.4f}")
    print()
    print("## 2. Contrastes appariés (pilote, rééchantillonnage 10 000, racine d'essai)")
    for cd, bloc in sorted(corps["analyse"].items()):
        for lib, c in bloc["contrastes"].items():
            print(f"  δ{cd} {lib:12s} moyenne {c['moyenne']:+.4f} ; écart-type {c['ecart_type']:.4f} ; IC95 "
                  f"[{c['ic95'][0]:+.4f} ; {c['ic95'][1]:+.4f}] ; zéros exacts {c['zeros_exacts']}")
    print()

    print("## 3. Puissance de la règle primaire (B − A sur (iii), « estimation ≥ S1 et borne basse 95 % > 0 » dans les "
          f"deux δ), {N_SIM} simulations")
    D = ecarts(res, "B", "A", "V_iii_final")
    print(f"instances appariées : {len(D)} ; écart-type pilote δ1 {D[:, 0].std(ddof=1):.4f}, δ2 {D[:, 1].std(ddof=1):.4f} ;"
          f" corrélation entre δ {np.corrcoef(D.T)[0, 1]:+.3f}")
    for s1 in S1_CANDIDATS:
        print(f"### S1 = {s1:.2f}")
        print("N    " + " ".join(f"e={e:.2f}" for e in E_GRILLE))
        mde = {}
        for N in N_GRILLE:
            ligne = []
            for e in E_GRILLE:
                p, _, _ = puissance(D, N, e, s1, rng)
                ligne.append(p)
                for cible in (0.8, 0.9):
                    if p >= cible and (N, cible) not in mde:
                        mde[(N, cible)] = e
            print(f"{N:<4d} " + " ".join(f"{p:6.3f}" for p in ligne))
        for N in N_GRILLE:
            print(f"  N = {N:3d} : effet minimal détectable (grille) à 0,8 : {mde.get((N, 0.8), '> 0,15')} ; "
                  f"à 0,9 : {mde.get((N, 0.9), '> 0,15')}")
    print()
    print("Erreur de première espèce à e = 0 (S1 = 0, deux δ exigés) :")
    for N in N_GRILLE:
        p, p1, p2 = puissance(D, N, 0.0, 0.0, rng)
        print(f"  N = {N:3d} : deux δ {p:.4f} ; δ1 seul {p1:.4f} ; δ2 seul {p2:.4f}")
    print()

    print("## 4. Contrastes témoins : puissance pour exclure l'hypothèse rivale et lire le rôle du programme linéaire")
    for lib, (b1, b2, k) in {"B-D (iii)": ("B", "D", "V_iii_final"), "B-C (iii)": ("B", "C", "V_iii_final"),
                             "B-A (ii) non-régression": ("B", "A", "ii_final")}.items():
        Dx = ecarts(res, b1, b2, k)
        sd = Dx.std(0, ddof=1)
        print(f"  {lib} : moyenne pilote δ1 {Dx[:, 0].mean():+.4f}, δ2 {Dx[:, 1].mean():+.4f} ; écart-type δ1 {sd[0]:.4f},"
              f" δ2 {sd[1]:.4f}")
        for N in (40, 60, 80, 100):
            print(f"    N = {N} : demi-largeur de l'IC95 attendue δ1 {1.96 * sd[0] / np.sqrt(N):.4f}, δ2 "
                  f"{1.96 * sd[1] / np.sqrt(N):.4f}")
    print()

    print("## 4 bis. Puissance de la non-régression sur (ii) et de l'équivalence B − C (rééchantillonnage centré)")
    Dn = ecarts(res, "B", "A", "ii_final")
    De = ecarts(res, "B", "C", "V_iii_final")
    print("  non-régression : P(borne basse 95 % de B − A sur (ii) > −S5 dans les deux δ) si l'écart vrai vaut e")
    for s5 in (0.02, 0.03, 0.05):
        for e in (0.0, -s5 / 2):
            ps = []
            for N in (40, 60, 100, 150):
                X = (Dn - Dn.mean(0) + e)[rng.integers(0, len(Dn), size=(N_SIM, N))]
                lb = X.mean(1) - stats.t.ppf(0.975, N - 1) * X.std(1, ddof=1) / np.sqrt(N)
                ps.append(f"N={N} {np.mean((lb > -s5).all(1)):.3f}")
            print(f"    S5 = {s5:.2f}, e = {e:+.3f} : " + " ; ".join(ps))
    print("  équivalence B − C : P(IC90 ⊂ [−S7 ; S7] dans les deux δ) si l'écart vrai est nul")
    for s7 in (0.01, 0.02, 0.03):
        ps = []
        for N in (40, 60, 100, 150):
            X = (De - De.mean(0))[rng.integers(0, len(De), size=(N_SIM, N))]
            hw = stats.t.ppf(0.95, N - 1) * X.std(1, ddof=1) / np.sqrt(N)
            m = X.mean(1)
            ok = (((m - hw) > -s7) & ((m + hw) < s7)).all(1)
            ps.append(f"N={N} {np.mean(ok):.3f}")
        print(f"    S7 = {s7:.2f} : " + " ; ".join(ps))
    print()

    print("## 5. Temps processeur mesuré (temps processeur du processus, `time.process_time`, un fil par processus)")
    cpu = np.array([r["cpu_tache_s"] for r in res])
    print(f"  par tâche (δ, instance), 4 bras : moyenne {cpu.mean():.2f} s ; médiane {np.median(cpu):.2f} s ; "
          f"maximum {cpu.max():.2f} s")
    for nom in "ABCD":
        tours = np.array([r["bras"][nom]["par_tour"]["cpu_s"] for r in res])
        fin = np.array([r["bras"][nom]["cpu_final_s"] for r in res])
        print(f"  bras {nom} : par tour (moyenne sur tâches) " + " ".join(f"{x:.2f}" for x in tours.mean(0)) +
              f" s ; phase finale (meilleure réponse finale, tenues, coût) {fin.mean():.2f} s")
    t = corps["temps"]
    print(f"  pilote : mur {t['mur_s']:.1f} s sur {t['processus']} processus ; somme des temps processeur des tâches "
          f"{t['cpu_somme_taches_s']:.1f} s ; efficacité {t['cpu_somme_taches_s'] / (t['mur_s'] * t['processus']):.2f}")
    eff = t["cpu_somme_taches_s"] / (t["mur_s"] * t["processus"])
    for N in N_GRILLE:
        tot = 2 * N * cpu.mean()
        print(f"  N = {N:3d} instances × 2 δ : temps processeur projeté {tot / 60:.1f} min ; mur projeté sur {COEURS} "
              f"cœurs {tot / COEURS / eff / 60:.1f} min")
    nmax = int(PLAFOND_MUR_S * COEURS * eff / (2 * cpu.max()))
    print(f"  N maximal sous {PLAFOND_MUR_S / 3600:.0f} h de mur sur {COEURS} cœurs, au temps maximal par tâche : {nmax}")
    print()

    print("## 6. Plomberie et déclencheurs d'audit observés sur le pilote (racine d'essai)")
    nc = sum(r["non_convergences"] for r in res)
    ne = sum(r["entrainements"] for r in res)
    print(f"  entraînements non convergés : {nc}/{ne}")
    proj = sum(sum(r["bras"][b]["par_tour"]["projections"]) for r in res for b in "ABCD")
    print(f"  projections après SLSQP (comptées) : {proj}")
    cens = {b: np.mean([r["bras"][b]["cout"]["censure"] for r in res]) for b in "ABCD"}
    print("  coût par contournement censuré à δ (non contourné à δ) : " +
          " ; ".join(f"{b} {v:.2f}" for b, v in cens.items()))
    pur = np.mean([max(r["bras"]["B"]["poids_finaux"]) > 1 - 1e-9 for r in res])
    unif = np.mean([np.allclose(r["bras"]["B"]["poids_finaux"], 1 / len(r["bras"]["B"]["poids_finaux"]), atol=1e-6)
                    for r in res])
    supp = np.mean([sum(w > 1e-6 for w in r["bras"]["B"]["poids_finaux"]) for r in res])
    print(f"  B : équilibre final pur {pur:.2f} des tâches ; égal à l'uniforme {unif:.2f} ; support moyen {supp:.2f}")
    print(f"  B : V ≥ 0,99 : {sum(r['bras']['B']['V_iii_final'] >= 0.99 for r in res)} tâches ; B = C exactement : "
          f"{sum(r['bras']['B']['V_iii_final'] == r['bras']['C']['V_iii_final'] for r in res)} tâches")
    fpr = np.array([r["bras"][b]["fpr_final"] for r in res for b in "ABCD"])
    print(f"  fausses alertes finales mesurées : moyenne {fpr.mean():.4f} ; min {fpr.min():.4f} ; max {fpr.max():.4f}")
    vr = np.array([r["bras"]["B"]["valeur_jeu_restreint"] - r["bras"]["B"]["V_iii_final"] for r in res])
    print(f"  B : valeur du jeu restreint − (iii) final : moyenne {vr.mean():+.4f} (positif attendu : l'attaquant final "
          "trouve mieux que les attaques du jeu restreint)")
    nouv = np.array([[r["bras"][b]["par_tour"]["nouveaute"] for b in "ABCD"] for r in res])
    print("  nouveauté résiduelle moyenne par tour (A, B, C, D) :")
    for j, b in enumerate("ABCD"):
        print(f"    {b} : " + " ".join(f"{x:.3f}" for x in nouv[:, j, :].mean(0)))
    print("  contrôle de l'optimiseur : (iii) standard − (iii) renforcé, par bras et par δ (positif = le renforcé trouve"
          " mieux) :")
    for cd in (1, 2):
        rr = [r for r in res if r["code_delta"] == cd]
        ligne = []
        for bb in "ABCD":
            dd = np.array([r["bras"][bb]["V_iii_standard"] - r["bras"][bb]["V_iii_renforce"] for r in rr])
            ligne.append(f"{bb} moyenne {dd.mean():+.4f} max {dd.max():+.4f} part > 0,01 {np.mean(dd > 0.01):.2f}")
        print(f"    δ{cd} : " + " ; ".join(ligne))
        gs = np.array([r["bras"]["B"]["V_iii_standard"] - r["bras"]["A"]["V_iii_standard"] for r in rr])
        gr = np.array([r["bras"]["B"]["V_iii_renforce"] - r["bras"]["A"]["V_iii_renforce"] for r in rr])
        print(f"    δ{cd} : B − A avec l'attaquant standard {gs.mean():+.4f} ; avec le renforcé {gr.mean():+.4f}")
    iii = np.array([[r["bras"][b]["par_tour"]["iii"] for b in "ABCD"] for r in res])
    print("  (iii) par tour contre la meilleure réponse du tour (moyenne) :")
    for j, b in enumerate("ABCD"):
        print(f"    {b} : " + " ".join(f"{x:.3f}" for x in iii[:, j, :].mean(0)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
