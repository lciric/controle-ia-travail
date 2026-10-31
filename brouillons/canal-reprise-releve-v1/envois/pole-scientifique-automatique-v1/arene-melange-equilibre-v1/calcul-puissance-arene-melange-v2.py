#!/usr/bin/env python3
"""Calcul de puissance de l'arène « mélange d'équilibre » — v2, sur les pilotes en RACINE_ESSAI (v2) seulement.

Lit le pilote « détection » produit par `arene_melange_v2.py essai` (refuse tout fichier tiré d'une racine de décision
ou d'une racine du brouillon 1, ou d'une autre configuration que CONFIG_V2), et, en option, le pilote « logistique »
(descriptif). Rapporte :
 1-2. moyennes par bras et contrastes appariés du pilote (intervalles du fichier) ;
 3. la règle de plomberie B − A : taille PAR δ sous chaque hypothèse nulle (e = 0 et e = S1) et puissance (CM-05) ;
 4-5. les marges relatives des contrastes principaux et, sous le pilote pris pour vérité, la probabilité de chaque
    classe (Table 3) par contraste, par δ et par marge ; la taille de chaque classe à la frontière de la marge ;
 6. la non-régression (ii) pour plusieurs S5 et la lecture sans seuil ;
 7. la lecture simulée des quatre tables (pilote pris pour vérité) ;
 8. le temps processeur et le temps de mur projeté ;
 9-10. la plomberie, les déclencheurs d'audit observés et les seuils « trop beau / trop mauvais » calibrés (S10) ;
 11. le pilote logistique (descriptif ; prédictions L1 et L2 du fichier de gel).
Les simulations rééchantillonnent conjointement les instances du pilote (les deux δ et tous les contrastes d'une
instance restent ensemble) et emploient des bornes de Student aux niveaux de la décision (la décision emploie les
quantiles du rééchantillonnage : écart déclaré).

    PYTHONPATH=src python3 calcul-puissance-arene-melange-v2.py PILOTE_DETECTION.json [PILOTE_LOGISTIQUE.json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import arene_melange_v2 as am  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

GRAINE_SIMULATION = (am.RACINE_ESSAI, 0, 0, 0, 0, 77)   # dérivée de la racine d'essai v2, rôle 77 : simulation
N_SIM = 4000
N_LECTURE = 1000
N_GRILLE = (40, 60, 80, 100, 150)
RHOS = (0.10, 0.25, 0.50)
S1_REC = 0.02
PLANCHER_MARGE = S1_REC / 2
S5_GRILLE = (0.01, 0.02, 0.05)
CLASSES = ("B>X", "X>B", "≈", "B≳X", "X≳B", "?")
COEURS = 2
P_B2, P_B8, P_EQ8 = 0.00625, 0.003125, 0.00625     # quantiles unilatéraux : Bonferroni 2 δ ; 8 tests ; équivalence 8


def charger(chemin, oracle):
    corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
    man = corps["manifeste"]
    am.exiger_racines_essai(man["racine"], man["racine_tenue"])
    if corps.get("mode") != "essai" or corps.get("oracle") != oracle:
        raise GardeArret(f"{chemin} : pas un essai d'oracle {oracle}")
    attendu = am.CONFIG_V2 if oracle == "detection" else am.replace(am.CONFIG_V2, entrainement="logistique")
    if man["config_sha256"] != attendu.empreinte():
        raise GardeArret(f"{chemin} : configuration différente de celle du code ({oracle})")
    for r in corps["resultats"]:
        if r["racine"] in am.RACINES_DECISION + am.RACINES_BROUILLON1 or \
                r["racine_tenue"] in am.RACINES_DECISION + am.RACINES_BROUILLON1:
            raise GardeArret("résultat tiré d'une racine interdite : refusé")
    return corps


def matrice(res, b1, b2, mes):
    """(instances × 2 δ) des écarts appariés, instances communes aux deux δ."""
    par = {}
    for r in res:
        par.setdefault(r["instance"], {})[r["code_delta"]] = r["bras"][b1][mes] - r["bras"][b2][mes]
    inst = sorted(i for i, v in par.items() if set(v) == {1, 2})
    return np.array([[par[i][1], par[i][2]] for i in inst])


def bornes(X, p):
    """X : n_sim × N × … ; renvoie moyenne, borne basse et haute de Student au quantile unilatéral p."""
    N = X.shape[1]
    m = X.mean(1)
    se = X.std(1, ddof=1) / np.sqrt(N)
    t = stats.t.ppf(1 - p, N - 1)
    return m, m - t * se, m + t * se


def classer_vect(lb, ub, elo, ehi, marge):
    out = np.full(lb.shape, "?", dtype=object)
    reste = np.ones(lb.shape, bool)
    for cond, nom in ((lb > marge, "B>X"), (ub < -marge, "X>B"), ((elo > -marge) & (ehi < marge), "≈"),
                      (lb > 0, "B≳X"), (ub < 0, "X≳B")):
        sel = reste & cond
        out[sel] = nom
        reste &= ~cond
    return out


def fausse_analyse(moy, se, N):
    """Analyse au format de `analyser` à partir de moyennes et d'erreurs-types (quantiles de Student)."""
    an = {}
    for k, cd in enumerate(("1", "2")):
        cs = {}
        for lib in moy:
            q = {f"q{p:g}": float(moy[lib][k] + stats.t.ppf(p, N - 1) * se[lib][k]) for p in am.QUANTILES}
            cs[lib] = {"moyenne": float(moy[lib][k]), "quantiles": q}
        an[cd] = {"contrastes": cs}
    return an


def main(argv):
    if len(argv) not in (1, 2):
        print(__doc__)
        return 2
    corps = charger(argv[0], "detection")
    cfg = am.CONFIG_V2
    res = corps["resultats"]
    man = corps["manifeste"]
    rng = np.random.default_rng(np.random.SeedSequence(entropy=GRAINE_SIMULATION[0], spawn_key=GRAINE_SIMULATION[1:]))
    d1, d2 = cfg.deltas
    print("# Calcul de puissance — arène mélange d'équilibre — v2 (RACINE_ESSAI v2 seulement)")
    print(f"fichier : {argv[0]}")
    print(f"racine = {man['racine']} ; racine des tenues = {man['racine_tenue']} ; configuration {man['config_sha256']}")
    v = man["versions"]
    print(f"code : {v['code_sha256']} ; commit {v['commit']} ; numpy {v['numpy']} ; scipy {v['scipy']}")
    n_inst = len({r['instance'] for r in res})
    print(f"tâches lues : {len(res)} ({n_inst} instances × 2 δ = {cfg.deltas}) ; graine de simulation "
          f"SeedSequence({GRAINE_SIMULATION[0]}, spawn_key={GRAINE_SIMULATION[1:]})")
    print()

    an = corps["analyse"]
    print("## 1. Moyennes par bras (pilote détection)")
    for cd, bloc in sorted(an.items()):
        print(f"δ{cd} = {bloc['delta']}, n = {bloc['n']}")
        for nom, b in bloc["bras"].items():
            print(f"  {nom:2s} : (iii) {b['V_iii_final']:.4f} [min {b['V_min_tache']:.4f} ; max {b['V_max_tache']:.4f}] ;"
                  f" (ii) {b['ii_final']:.4f} ; (i) {b['i_final_vus']:.4f} ; fausses alertes moyenne {b['fpr_moyen']:.4f}"
                  f" [{b['fpr_min']:.4f} ; {b['fpr_max']:.4f}]")
    print()
    print("## 2. Contrastes appariés (pilote ; rééchantillonnage 20 000 du fichier)")
    print("   IC95 = [q0.025 ; q0.975] ; B2 = Bonferroni 2 δ [q0.00625 ; q0.99375] ; B8 = Bonferroni 8 tests "
          "[q0.003125 ; q0.996875]")
    for cd, bloc in sorted(an.items()):
        for lib, c in bloc["contrastes"].items():
            q = c["quantiles"]
            print(f"  δ{cd} {lib:12s} moyenne {c['moyenne']:+.4f} ; é.-t. {c['ecart_type']:.4f} ; IC95 [{q['q0.025']:+.4f} ;"
                  f" {q['q0.975']:+.4f}] ; B2 [{q['q0.00625']:+.4f} ; {q['q0.99375']:+.4f}] ; B8 [{q['q0.003125']:+.4f} ;"
                  f" {q['q0.996875']:+.4f}] ; zéros exacts {c['zeros_exacts']}")
    print()

    # --- 3. plomberie -------------------------------------------------------------------------------------------
    Dba = matrice(res, "B", "A", "V_iii_final")
    print("## 3. Plomberie B − A sur (iii) : règle « moyenne ≥ S1 et borne basse B2 > 0 », lue PAR δ (CM-05)")
    print(f"instances appariées {len(Dba)} ; écart-type δ1 {Dba[:, 0].std(ddof=1):.4f}, δ2 {Dba[:, 1].std(ddof=1):.4f} ;"
          f" corrélation entre δ {np.corrcoef(Dba.T)[0, 1]:+.3f}")
    for s1 in (0.0, S1_REC):
        print(f"### S1 = {s1:.2f}")
        for N in N_GRILLE:
            ligne = []
            for e_nom, e in (("e=0", 0.0), ("e=S1", s1), ("e=0,03", 0.03), ("e=pilote", None)):
                Dc = Dba if e is None else Dba - Dba.mean(0) + e
                X = Dc[rng.integers(0, len(Dc), size=(N_SIM, N))]
                m, lb, _ = bornes(X, P_B2)
                ok = (m >= s1) & (lb > 0)
                ligne.append(f"{e_nom} δ1 {ok[:, 0].mean():.3f} δ2 {ok[:, 1].mean():.3f}")
            print(f"  N = {N:3d} : " + " ; ".join(ligne))
    print("  Lecture : « e=0 » est la taille par δ sous l'hypothèse nulle d'absence d'effet ; « e=S1 » la taille sous "
          "l'hypothèse nulle « effet = S1 » (règle de pertinence et de significativité, pas un test de « effet ≥ S1 ») ;"
          " la règle « aux deux δ » a pour taille celle du δ le plus défavorable (intersection-union).")
    print()

    # --- 4. marges ---------------------------------------------------------------------------------------------
    pil_ba = Dba.mean(0)
    print("## 4. Marges des contrastes principaux : m(δ) = max(ρ × moyenne pilote de B − A à δ ; S1/2 = "
          f"{PLANCHER_MARGE})")
    marges = {}
    for rho in RHOS:
        marges[rho] = np.maximum(rho * pil_ba, PLANCHER_MARGE)
        print(f"  ρ = {rho:.2f} : m(δ1 = {d1}) = {marges[rho][0]:.4f} ; m(δ2 = {d2}) = {marges[rho][1]:.4f}")
    print()

    # --- 5. contrastes principaux ------------------------------------------------------------------------------
    libs = {lib: am.CONTRASTES[k][1:] for k in am.CONTRASTES for lib in [am.CONTRASTES[k][0]]
            if lib in am.CONTRASTES_PRINCIPAUX}
    Dp = {lib: matrice(res, b1, b2, mes) for lib, (b1, b2, mes) in libs.items()}
    print("## 5. Contrastes principaux (Table 3) : probabilité de chaque classe, pilote pris pour vérité")
    print("   classes : B>X (borne basse B8 > m) ; X>B (borne haute B8 < −m) ; ≈ (intervalle d'équivalence "
          "Bonferroni 8 ⊂ ]−m ; m[) ; B≳X ; X≳B ; ?")
    for N in (60, 100, 150):
        idx = rng.integers(0, n_inst, size=(N_SIM, N))
        for rho in RHOS:
            print(f"### N = {N}, ρ = {rho:.2f}")
            for lib, D in Dp.items():
                X = D[idx]
                m, lb, ub = bornes(X, P_B8)
                _, elo, ehi = bornes(X, P_EQ8)
                txt = []
                for k in (0, 1):
                    cl = classer_vect(lb[:, k], ub[:, k], elo[:, k], ehi[:, k], marges[rho][k])
                    txt.append(f"δ{k + 1} (pilote {D[:, k].mean():+.4f}) " +
                               " ".join(f"{c} {np.mean(cl == c):.3f}" for c in CLASSES if np.mean(cl == c) > 0))
                print(f"  {lib:11s} " + " | ".join(txt))
    print("### Taille de chaque classe à la frontière (écarts centrés puis décalés), N = 100, ρ = 0,25")
    idx = rng.integers(0, n_inst, size=(N_SIM, 100))
    for lib, D in Dp.items():
        txt = []
        for k in (0, 1):
            mg = marges[0.25][k]
            r = []
            for nom_h, e, cible in (("Δ=+m", mg, "B>X"), ("Δ=−m", -mg, "X>B"), ("Δ=+m", mg, "≈"), ("Δ=0", 0.0, "≈")):
                X = (D - D.mean(0) + e)[idx]
                m, lb, ub = bornes(X, P_B8)
                _, elo, ehi = bornes(X, P_EQ8)
                cl = classer_vect(lb[:, k], ub[:, k], elo[:, k], ehi[:, k], mg)
                r.append(f"P({cible} | {nom_h}) {np.mean(cl == cible):.3f}")
            txt.append(f"δ{k + 1} : " + " ; ".join(r))
        print(f"  {lib:11s} " + " | ".join(txt))
    print("  Lecture : P(B>X | Δ = +m), P(X>B | Δ = −m) et P(≈ | Δ = +m) sont les tailles (erreur de première espèce "
          "par test, au plus 0,003 et 0,006 attendus) ; P(≈ | Δ = 0) est la puissance d'équivalence.")
    print()

    # --- 6. non-régression -------------------------------------------------------------------------------------
    Dn = matrice(res, "B", "A", "ii_final")
    print("## 6. Table 2, non-régression sur (ii), B − A (bornes B2)")
    print(f"  pilote, sans seuil : δ1 moyenne {Dn[:, 0].mean():+.4f} (é.-t. {Dn[:, 0].std(ddof=1):.4f}) ; δ2 moyenne "
          f"{Dn[:, 1].mean():+.4f} (é.-t. {Dn[:, 1].std(ddof=1):.4f})")
    idx = rng.integers(0, n_inst, size=(N_SIM, 100))
    for s5 in S5_GRILLE:
        for e_nom, Dc in (("pilote", Dn), ("e=0", Dn - Dn.mean(0)), ("e=−S5/2", Dn - Dn.mean(0) - s5 / 2)):
            X = Dc[idx]
            m, lb, ub = bornes(X, P_B2)
            l1 = (ub < -s5).any(1)
            l2 = ~l1 & (lb > -s5).all(1) & (ub < 0).any(1)
            l3 = ~l1 & ~l2 & (lb > 0).all(1)
            l4 = ~l1 & ~l2 & ~l3 & (lb > -s5).all(1)
            l5 = ~(l1 | l2 | l3 | l4)
            print(f"  S5 = {s5:.2f}, {e_nom:8s} N = 100 : avérée {l1.mean():.3f} ; démontrée sous la tolérance "
                  f"{l2.mean():.3f} ; amélioration {l3.mean():.3f} ; sans régression {l4.mean():.3f} ; non exclue "
                  f"{l5.mean():.3f}")
    print()

    # --- 7. lecture simulée ------------------------------------------------------------------------------------
    print(f"## 7. Lecture simulée des quatre tables (pilote pris pour vérité, N = 100, {N_LECTURE} répétitions, "
          "S1 = S5 = 0,02)")
    tous = {"B-A (iii)": Dba, "B-A (ii)": Dn, **Dp}
    for rho in RHOS:
        comptes = {"table1": {}, "table2": {}, "table4": {}}
        par_temoin = {lib: {} for lib in Dp}
        for _ in range(N_LECTURE):
            ix = rng.integers(0, n_inst, size=100)
            moy = {lib: D[ix].mean(0) for lib, D in tous.items()}
            se = {lib: D[ix].std(0, ddof=1) / np.sqrt(100) for lib, D in tous.items()}
            t = am.lire_tables(fausse_analyse(moy, se, 100), S1_REC, S1_REC, {"1": marges[rho][0], "2": marges[rho][1]})
            for k in comptes:
                comptes[k][t[k]] = comptes[k].get(t[k], 0) + 1
            for lib in Dp:
                cle = f"{t['table3']['1'][lib]} / {t['table3']['2'][lib]}"
                par_temoin[lib][cle] = par_temoin[lib].get(cle, 0) + 1
        print(f"### ρ = {rho:.2f}")
        for k, c in comptes.items():
            print(f"  {k} : " + " ; ".join(f"{a} {b / N_LECTURE:.3f}" for a, b in sorted(c.items(), key=lambda x: -x[1])))
        for lib, c in par_temoin.items():
            print(f"  {lib} (δ1 / δ2) : " + " ; ".join(f"{a} {b / N_LECTURE:.3f}"
                                                      for a, b in sorted(c.items(), key=lambda x: -x[1])))
    print()

    # --- 8. temps ------------------------------------------------------------------------------------------------
    print("## 8. Temps processeur mesuré (`time.process_time`, un fil par processus)")
    cpu = np.array([r["cpu_tache_s"] for r in res])
    print(f"  par tâche (6 bras) : moyenne {cpu.mean():.2f} s ; médiane {np.median(cpu):.2f} s ; maximum {cpu.max():.2f} s")
    for cd in (1, 2):
        c = np.array([r["cpu_tache_s"] for r in res if r["code_delta"] == cd])
        print(f"  δ{cd} : moyenne {c.mean():.2f} s ; maximum {c.max():.2f} s")
    for nom in am.TOUS_LES_BRAS:
        fin = np.array([r["bras"][nom]["cpu_final_s"] for r in res])
        tr = np.array([r["bras"][nom].get("cpu_trajectoire_s", 0.0) for r in res])
        print(f"  bras {nom:2s} : trajectoire {tr.mean():.2f} s ; phase finale (attaques finales, tenues, courbe, coût) "
              f"{fin.mean():.2f} s")
    t = corps["temps"]
    eff = t["cpu_somme_taches_s"] / (t["mur_s"] * t["processus"])
    print(f"  pilote : mur {t['mur_s']:.1f} s sur {t['processus']} processus ; somme des temps processeur "
          f"{t['cpu_somme_taches_s']:.1f} s ; efficacité {eff:.2f}")
    for N in N_GRILLE:
        tot = 2 * N * cpu.mean()
        print(f"  N = {N:3d} × 2 δ : processeur projeté {tot / 60:.1f} min ; mur projeté sur {COEURS} cœurs "
              f"{tot / COEURS / eff / 60:.1f} min")
    for plafond_h in (1.25, 2.0):
        print(f"  N maximal sous {plafond_h} h de mur sur {COEURS} cœurs, au temps moyen par tâche : "
              f"{int(plafond_h * 3600 * COEURS * eff / (2 * cpu.mean()))} ; au temps maximal : "
              f"{int(plafond_h * 3600 * COEURS * eff / (2 * cpu.max()))}")
    print()

    # --- 9. plomberie et déclencheurs ----------------------------------------------------------------------------
    print("## 9. Plomberie et déclencheurs d'audit observés (pilote détection)")
    nc = sum(r["non_convergences"] for r in res)
    ne = sum(r["entrainements"] for r in res)
    print(f"  entraînements non convergés : {nc}/{ne} ; maximum par tâche {max(r['non_convergences'] for r in res)}")
    for cd, bloc in sorted(an.items()):
        a = bloc["attaquant"]
        print(f"  δ{cd} attaquant : départs {a['departs']} ; non finis {a['non_finis']} ; statuts SLSQP {a['statuts']} ;"
              f" itérations max {a['iter_max']} ; réponses à la limite d'itérations {a['reponses_a_la_limite']}")
        print(f"  δ{cd} écart de fausses alertes entre bras (par tâche) : moyen {bloc['ecart_fpr_entre_bras']['moyen']:.4f}"
              f" ; max {bloc['ecart_fpr_entre_bras']['max']:.4f} ; écart à α de la moyenne par bras : " +
              " ; ".join(f"{n} {b['fpr_moyen'] - cfg.alpha:+.4f}" for n, b in bloc["bras"].items()))
        pB = bloc["bras"]["B"]["poids"]
        print(f"  δ{cd} B : poids purs {pB['part_pure']:.2f} ; égaux à l'uniforme {pB['part_uniforme']:.2f} ; support "
              f"moyen {pB['support_moyen']:.2f} ; valeur du jeu restreint − V(B) {bloc['bras']['B']['valeur_restreinte_moins_V']:+.4f}"
              f" ; B = C1 au bit {bloc['B_egal_C1_au_bit']} tâches ; D = A au bit {bloc['D_egal_A_au_bit']} tâches")
        print(f"  δ{cd} contrôle de l'optimiseur (V standard − V renforcé ; positif = le renforcé trouve mieux) : " +
              " ; ".join(f"{n} {b['standard_moins_renforce']:+.4f} (max {b['standard_moins_renforce_max']:+.4f})"
                         for n, b in bloc["bras"].items()))
        for lib in ("B-A (iii)",) + am.CONTRASTES_PRINCIPAUX:
            c = bloc["contrastes"][lib]
            print(f"     {lib} : attaquant standard {c['std_attaquant_standard']:+.4f} ; renforcé "
                  f"{c['std_attaquant_renforce']:+.4f} ; retenu {c['moyenne']:+.4f}")
        for n, b in bloc["bras"].items():
            co = b["cout"]
            med = "—" if co["mediane_fraction_non_censurees"] is None else f"{co['mediane_fraction_non_censurees']:.3f}"
            cens = "—" if co["part_censuree_parmi_definies"] is None else f"{co['part_censuree_parmi_definies']:.2f}"
            print(f"  δ{cd} {n:2s} coût : défini {co['part_definie']:.2f} ; censuré parmi définies {cens} ; médiane des "
                  f"fractions non censurées {med} (n = {co['n_non_censurees']}) ; tâches non monotones "
                  f"{co['taches_non_monotones']} ; courbe V(δ') moyenne " +
                  " ".join(f"{x:.3f}" for x in b["courbe_moyenne"]))
    for nom in am.BRAS_TRAJECTOIRE:
        nv = np.array([r["bras"][nom]["par_tour"]["nouveaute"] for r in res]).mean(0)
        it = np.array([r["bras"][nom]["par_tour"]["iii"] for r in res]).mean(0)
        print(f"  {nom} : nouveauté résiduelle par tour " + " ".join(f"{x:.3f}" for x in nv) +
              " ; (iii) par tour " + " ".join(f"{x:.3f}" for x in it))
    print()

    # --- 10. seuils calibrés -------------------------------------------------------------------------------------
    print("## 10. S10 calibré : plage [minimum ; maximum] des V par tâche au pilote, par bras et par δ")
    for cd, bloc in sorted(an.items()):
        print(f"  δ{cd} : " + " ; ".join(f"{n} [{b['V_min_tache']:.4f} ; {b['V_max_tache']:.4f}]"
                                       for n, b in bloc["bras"].items()))
    print()

    # --- 11. pilote logistique ----------------------------------------------------------------------------------
    if len(argv) == 2:
        lo = charger(argv[1], "logistique")
        print("## 11. Pilote logistique (descriptif ; prédictions L1 et L2 de `gel-conception-arene-melange-v2.md`)")
        print(f"fichier : {argv[1]} ; configuration {lo['manifeste']['config_sha256']} ; code "
              f"{lo['manifeste']['versions']['code_sha256']}")
        for cd, bloc in sorted(lo["analyse"].items()):
            pB = bloc["bras"]["B"]["poids"]
            ba = bloc["contrastes"]["B-A (iii)"]
            print(f"  δ{cd} : B poids purs {pB['part_pure']:.2f} (L1 prédit > 0,5) ; support moyen {pB['support_moyen']:.2f}"
                  f" ; B − A (iii) {ba['moyenne']:+.4f} IC95 [{ba['quantiles']['q0.025']:+.4f} ; "
                  f"{ba['quantiles']['q0.975']:+.4f}] (L2 prédit |·| < 0,02)")
            print("        moyennes (iii) : " + " ; ".join(f"{n} {b['V_iii_final']:.4f}" for n, b in bloc["bras"].items()))
            print("        contrastes : " + " ; ".join(f"{lib} {c['moyenne']:+.4f}" for lib, c in bloc["contrastes"].items()
                                                     if lib in am.CONTRASTES_PRINCIPAUX + ("B-A (ii)",)))
        t = lo["temps"]
        print(f"  temps : mur {t['mur_s']:.1f} s ; somme des temps processeur {t['cpu_somme_taches_s']:.1f} s ; "
              f"entraînements non convergés {sum(r['non_convergences'] for r in lo['resultats'])}/"
              f"{sum(r['entrainements'] for r in lo['resultats'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
