#!/usr/bin/env python3
"""Calcul de puissance de l'arène « mélange d'équilibre » — v3, sur le pilote v3 en RACINE_ESSAI (20261311) seulement.

Lit le pilote « détection » produit par `arene_melange_v3.py essai` (refuse toute racine de décision ou racine d'essai
déjà employée, et toute autre configuration que CONFIG_V3) et, en option, la sortie de `audit-essai`. Rapporte :
 1-2. moyennes par bras (paramètres stockés et déployés par requête) et contrastes appariés du pilote ;
 3. les règles de lecture évaluées AVEC LE RÉÉCHANTILLONNAGE DE LA DÉCISION (CM2-07) : à chaque répétition, N
    instances tirées du pilote (centrées et décalées selon le scénario), puis 20 000 tirages de rééchantillonnage et
    les quantiles de `analyser` (np.quantile, méthode linéaire) ; 1 000 répétitions par scénario ; tailles par δ et
    par test à la frontière, probabilité de chaque classe sous le pilote pris pour vérité (N = 100 et N = 60) ;
 4. la lecture simulée des Tables 1 à 7 (`lire_tables` du code) ;
 5. le temps processeur et le temps de mur projeté (décision et audit) ;
 6. la plomberie, les poids de B et B′, les indicateurs de la condition d'application, les contrôles de l'optimiseur ;
 7. les bandes S10 (moyenne pilote ± 5 × écart-type par tâche / √N) ;
 8. l'audit d'attaquant indépendant sur le pilote (si fourni).
Marges par principe (gel v3) : m = S1 = 0,02 pour Q1 et Q2 ; S15 = 0,02 ; S5 = 0,02. Aucune marge ne vient du pilote.

    PYTHONPATH=src python3 calcul-puissance-arene-melange-v3.py PILOTE.json [AUDIT_ESSAI.json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import arene_melange_v3 as am  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

GRAINE_SIMULATION = (am.RACINE_ESSAI, 0, 0, 0, 0, 77)   # dérivée de la racine d'essai v3, rôle 77 : simulation
N_REP = 1000
N_REECH = 20000
S1 = S5 = S6 = S15 = 0.02
COEURS = 2
CLASSES = ("B>X", "X>B", "≈", "B≳X", "X≳B", "?")
COL_Q1 = list(am.CONTRASTES_PRINCIPAUX)
COL_Q2 = list(am.CONTRASTES_Q2)
COL_AUTRES = ["B-A (iii)", "B-A (ii)"]
COL_IND = ["A I1", "A I2"]


def charger(chemin):
    corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
    man = corps["manifeste"]
    am.exiger_racines_essai(man["racine"], man["racine_tenue"])
    if corps.get("mode") != "essai" or corps.get("oracle") != "detection":
        raise GardeArret(f"{chemin} : pas un essai d'oracle détection")
    if man["config_sha256"] != am.CONFIG_V3.empreinte():
        raise GardeArret(f"{chemin} : configuration différente de celle du code")
    for r in corps["resultats"]:
        if {r["racine"], r["racine_tenue"]} & set(am.RACINES_DECISION + am.RACINES_DEJA_EMPLOYEES):
            raise GardeArret("résultat tiré d'une racine interdite : refusé")
    return corps


def valeur(r, lib):
    """Valeur par tâche d'une colonne : contraste (bras 1 − bras 2) ou indicateur d'un bras."""
    for code, (l, b1, b2, mes) in am.CONTRASTES.items():
        if l == lib:
            return r["bras"][b1][mes] - r["bras"][b2][mes]
    for code, (l, nom, mes) in am.INDICATEURS.items():
        if l == lib:
            return r["bras"][nom]["cycle"][mes]
    raise KeyError(lib)


def matrice(res, colonnes):
    """(instances × (2 δ × colonnes)) ; colonne k du δ cd à l'indice (cd − 1) × len(colonnes) + k."""
    par = {}
    for r in res:
        par.setdefault(r["instance"], {})[r["code_delta"]] = [valeur(r, c) for c in colonnes]
    inst = sorted(i for i, v in par.items() if set(v) == {1, 2})
    return np.array([par[i][1] + par[i][2] for i in inst]), inst


def quantiles_reech(Dn, rng):
    """Rééchantillonnage de la décision : indices uniformes (B × N), moyennes, quantiles linéaires."""
    N = len(Dn)
    idx = rng.integers(0, N, size=(N_REECH, N))
    comptes = np.bincount((idx + N * np.arange(N_REECH)[:, None]).ravel(), minlength=N_REECH * N).reshape(N_REECH, N)
    moy = comptes @ Dn / N
    return Dn.mean(0), dict(zip(am.QUANTILES, np.quantile(moy, am.QUANTILES, axis=0))), idx, moy


def simuler(D, purs, N, decalage, rng, n_rep=N_REP):
    """n_rep répétitions : N instances tirées du pilote (D centré puis décalé colonne par colonne si `decalage` n'est
    pas None), quantiles de la décision. Renvoie la liste des (moyennes, quantiles, parts pures par δ)."""
    Dc = D if decalage is None else D - D.mean(0) + decalage
    sortie = []
    for _ in range(n_rep):
        ix = rng.integers(0, len(D), size=N)
        m, q, _, _ = quantiles_reech(Dc[ix], rng)
        sortie.append((m, q, purs[ix].mean(0)))
    return sortie


def fausse_analyse(m, q, pur, colonnes):
    an = {}
    nc = len(colonnes)
    for k, cd in enumerate(("1", "2")):
        cs, ind = {}, {}
        for j, lib in enumerate(colonnes):
            c = k * nc + j
            e = {"moyenne": float(m[c]), "quantiles": {f"q{p:g}": float(q[p][c]) for p in am.QUANTILES}}
            (ind if lib in COL_IND else cs)[lib] = e
        an[cd] = {"contrastes": cs, "indicateurs": ind, "bras": {"Bp": {"poids": {"part_pure": float(pur[k])}}}}
    return an


def classes_par_test(sims, colonnes, libs, niveaux):
    """Classe de chaque test (lib, δ) sous la règle (borne basse/haute au niveau Bonferroni, équivalence)."""
    lo, hi, elo, ehi = niveaux
    nc = len(colonnes)
    out = {}
    for lib in libs:
        for k in (0, 1):
            c = k * nc + colonnes.index(lib)
            cl = [am.classer(q[lo][c], q[hi][c], q[elo][c], q[ehi][c], S6) for _, q, _ in sims]
            out[(lib, k + 1)] = {x: cl.count(x) / len(cl) for x in CLASSES if cl.count(x)}
    return out


def fmt(d):
    return " ".join(f"{k} {v:.3f}" for k, v in sorted(d.items(), key=lambda x: -x[1]))


def main(argv):
    if len(argv) not in (1, 2):
        print(__doc__)
        return 2
    corps = charger(argv[0])
    cfg = am.CONFIG_V3
    res = corps["resultats"]
    man = corps["manifeste"]
    an = corps["analyse"]
    rng = np.random.default_rng(np.random.SeedSequence(entropy=GRAINE_SIMULATION[0], spawn_key=GRAINE_SIMULATION[1:]))
    print("# Calcul de puissance — arène mélange d'équilibre — v3 (RACINE_ESSAI v3 seulement)")
    print(f"fichier : {argv[0]}")
    print(f"racine = {man['racine']} ; racine des tenues = {man['racine_tenue']} ; configuration {man['config_sha256']}")
    v = man["versions"]
    print(f"code : {v['code_sha256']} ; commit {v['commit']} (HEAD du dépôt ; le code remis n'y est pas committé) ; "
          f"numpy {v['numpy']} ; scipy {v['scipy']}")
    n_inst = len({r['instance'] for r in res})
    print(f"tâches lues : {len(res)} ({n_inst} instances × 2 δ = {cfg.deltas}) ; graine de simulation "
          f"SeedSequence({GRAINE_SIMULATION[0]}, spawn_key={GRAINE_SIMULATION[1:]}) ; {N_REP} répétitions × {N_REECH} "
          "tirages par scénario")
    print()

    print("## 1. Moyennes par bras (pilote détection)")
    for cd, bloc in sorted(an.items()):
        print(f"δ{cd} = {bloc['delta']}, n = {bloc['n']}")
        for nom, b in bloc["bras"].items():
            print(f"  {am.NOMS.get(nom, nom):3s} : (iii) {b['V_iii_final']:.4f} [min {b['V_min_tache']:.4f} ; max "
                  f"{b['V_max_tache']:.4f}] ; (ii) {b['ii_final']:.4f} ; (i) {b['i_final_vus']:.4f} ; fausses alertes "
                  f"{b['fpr_moyen']:.4f} [{b['fpr_min']:.4f} ; {b['fpr_max']:.4f}] ; paramètres stockés "
                  f"{b['parametres_deployes']}, par requête ≤ {b['parametres_par_requete_max']}")
    print()
    print("## 2. Contrastes appariés et indicateurs (pilote ; rééchantillonnage 20 000 du fichier)")
    print("   IC95 = [q0.025 ; q0.975] ; B2/B4 = [q0.00625 ; q0.99375] ; B8 = [q0.003125 ; q0.996875] ; "
          "E4 = [q0.0125 ; q0.9875]")
    for cd, bloc in sorted(an.items()):
        for lib, c in list(bloc["contrastes"].items()) + list(bloc["indicateurs"].items()):
            q = c["quantiles"]
            print(f"  δ{cd} {lib:13s} moyenne {c['moyenne']:+.4f} ; é.-t. {c['ecart_type']:.4f} ; IC95 "
                  f"[{q['q0.025']:+.4f} ; {q['q0.975']:+.4f}] ; B2/B4 [{q['q0.00625']:+.4f} ; {q['q0.99375']:+.4f}] ;"
                  f" B8 [{q['q0.003125']:+.4f} ; {q['q0.996875']:+.4f}] ; E4 [{q['q0.0125']:+.4f} ; "
                  f"{q['q0.9875']:+.4f}]")
    print()

    colonnes = COL_Q1 + COL_Q2 + COL_AUTRES + COL_IND
    D, inst = matrice(res, colonnes)
    purs = np.array([[max(r["bras"]["Bp"]["poids_finaux"]) > 1 - 1e-9 for r in sorted(
        (x for x in res if x["instance"] == i), key=lambda x: x["code_delta"])] for i in inst], float)
    nc = len(colonnes)

    # contrôle : les moyennes par comptes égalent celles de `analyser` (mêmes indices), à l'ordre de sommation près
    _, _, idx, moy = quantiles_reech(D[:24], rng)
    assert np.allclose(moy, D[:24][idx].mean(1), atol=1e-12, rtol=0)

    print("## 3. Règles de lecture sous le rééchantillonnage de la décision (CM2-07)")
    print(f"   marges par principe : m = S6 = {S6} (Q1 et Q2) ; S1 = S5 = S15 = {S1}")
    scen = {}
    scen["pilote N=100"] = simuler(D, purs, 100, None, rng)
    scen["pilote N=60"] = simuler(D, purs, 60, None, rng)
    dec = np.zeros(2 * nc)

    def decaler(valeurs):
        d = dec.copy()
        for lib, x in valeurs.items():
            for k in (0, 1):
                d[k * nc + colonnes.index(lib)] = x
        return d

    scen["frontière +"] = simuler(D, purs, 100, decaler({**{c: S6 for c in COL_Q1 + COL_Q2}, "B-A (iii)": S1,
                                                         "B-A (ii)": 0.0, "A I1": S15, "A I2": S15}), rng)
    scen["frontière −"] = simuler(D, purs, 100, decaler({**{c: -S6 for c in COL_Q1 + COL_Q2}, "B-A (iii)": 0.0,
                                                         "B-A (ii)": -S5, "A I1": 0.0, "A I2": 0.0}), rng)
    scen["nul"] = simuler(D, purs, 100, decaler({**{c: 0.0 for c in COL_Q1 + COL_Q2}, "B-A (iii)": 0.03,
                                                 "B-A (ii)": 0.0, "A I1": 0.0, "A I2": 0.05}), rng)

    def prob(sims, f):
        return float(np.mean([f(m, q) for m, q, _ in sims]))

    def col(lib, k):
        return k * nc + colonnes.index(lib)

    print("### 3a. Plomberie B − A (iii), règle « moyenne ≥ S1 et borne basse B2 > 0 », par δ, N = 100")
    for nom, s in (("taille, effet nul (frontière −)", scen["frontière −"]),
                   ("taille, effet = S1 (frontière +)", scen["frontière +"]),
                   ("puissance, effet 0,03 (nul)", scen["nul"]), ("pilote pris pour vérité", scen["pilote N=100"])):
        print(f"  {nom} : " + " ; ".join(
            f"δ{k + 1} {prob(s, lambda m, q: m[col('B-A (iii)', k)] >= S1 and q[0.00625][col('B-A (iii)', k)] > 0):.3f}"
            for k in (0, 1)))
    print("### 3b. Q1 (Table 3), bornes B8, équivalence E8 : probabilité de chaque classe")
    niv8 = (0.003125, 0.996875, 0.00625, 0.99375)
    niv4 = (0.00625, 0.99375, 0.0125, 0.9875)
    for nom in ("pilote N=100", "pilote N=60"):
        print(f"  {nom}")
        for (lib, k), d in classes_par_test(scen[nom], colonnes, COL_Q1, niv8).items():
            print(f"    {lib:12s} δ{k} (pilote {D[:, col(lib, k - 1)].mean():+.4f}) : {fmt(d)}")
    print("  tailles à la frontière (N = 100) : P(B>X | Δ=+m) ; P(X>B | Δ=−m) ; P(≈ | Δ=+m) ; P(≈ | Δ=−m) ; "
          "puissance P(≈ | Δ=0)")
    cp, cm, c0 = (classes_par_test(scen[s], colonnes, COL_Q1, niv8) for s in ("frontière +", "frontière −", "nul"))
    for key in cp:
        print(f"    {key[0]:12s} δ{key[1]} : {cp[key].get('B>X', 0):.3f} ; {cm[key].get('X>B', 0):.3f} ; "
              f"{cp[key].get('≈', 0):.3f} ; {cm[key].get('≈', 0):.3f} ; {c0[key].get('≈', 0):.3f}")
    print("  nominal par test : 0,003 (supériorité, Bonferroni 8 unilatéral) ; 0,006 (équivalence, par côté)")
    print("### 3c. Q2 (Table 6), bornes B4, équivalence E4 : probabilité de chaque classe")
    for nom in ("pilote N=100", "pilote N=60"):
        print(f"  {nom}")
        for (lib, k), d in classes_par_test(scen[nom], colonnes, COL_Q2, niv4).items():
            print(f"    {lib:12s} δ{k} (pilote {D[:, col(lib, k - 1)].mean():+.4f}) : {fmt(d)}")
    cp, cm, c0 = (classes_par_test(scen[s], colonnes, COL_Q2, niv4) for s in ("frontière +", "frontière −", "nul"))
    print("  tailles à la frontière (N = 100) : P(B>X | Δ=+m) ; P(X>B | Δ=−m) ; P(≈ | Δ=+m) ; P(≈ | Δ=−m) ; "
          "puissance P(≈ | Δ=0)")
    for key in cp:
        print(f"    {key[0]:12s} δ{key[1]} : {cp[key].get('B>X', 0):.3f} ; {cm[key].get('X>B', 0):.3f} ; "
              f"{cp[key].get('≈', 0):.3f} ; {cm[key].get('≈', 0):.3f} ; {c0[key].get('≈', 0):.3f}")
    print("  nominal par test : 0,00625 (supériorité, Bonferroni 4 unilatéral) ; 0,0125 (équivalence, par côté)")
    print("### 3d. Table 2 (ii), S5 = 0,02, N = 100 : « sans régression » et « régression avérée »")
    for nom, s in (("écart nul (frontière +)", scen["frontière +"]), ("écart −S5 (frontière −)", scen["frontière −"]),
                   ("pilote", scen["pilote N=100"])):
        sr = prob(s, lambda m, q: all(q[0.00625][col("B-A (ii)", k)] > -S5 for k in (0, 1)))
        av = prob(s, lambda m, q: any(q[0.99375][col("B-A (ii)", k)] < -S5 for k in (0, 1)))
        print(f"  {nom} : borne basse > −S5 aux deux δ {sr:.3f} ; régression avérée {av:.3f}")
    print("### 3e. Table 5 (condition d'application), bornes B2, S15 = 0,02, N = 100")
    for nom, s in (("I1 = S15, I2 = S15 (frontière +)", scen["frontière +"]),
                   ("I1 = 0, I2 = 0 (frontière −)", scen["frontière −"]), ("I1 = 0, I2 = 0,05 (nul)", scen["nul"]),
                   ("pilote", scen["pilote N=100"])):
        print(f"  {nom} : " + " ; ".join(
            f"δ{k + 1} P(I1 borne haute < S15) {prob(s, lambda m, q: q[0.99375][col('A I1', k)] < S15):.3f}, "
            f"P(I1 borne basse > S15) {prob(s, lambda m, q: q[0.00625][col('A I1', k)] > S15):.3f}, "
            f"P(I2 borne basse > S15) {prob(s, lambda m, q: q[0.00625][col('A I2', k)] > S15):.3f}, "
            f"P(I2 borne haute < S15) {prob(s, lambda m, q: q[0.99375][col('A I2', k)] < S15):.3f}" for k in (0, 1)))
    print("  lecture : sous « frontière + », P(I1 borne haute < S15) et P(I2 borne basse > S15) sont des tailles "
          "(nominal 0,00625)")
    print()

    print("## 4. Lecture simulée des Tables 1 à 7 (`lire_tables`, pilote pris pour vérité, 1 000 répétitions)")
    print("   (joint approché : un même rééchantillonnage pour toutes les colonnes d'une répétition ; la décision tire "
          "une graine par contraste ; lois marginales identiques)")
    for nom in ("pilote N=100", "pilote N=60"):
        comptes = {}
        for m, q, pur in scen[nom]:
            t = am.lire_tables(fausse_analyse(m, q, pur, colonnes), S1, S5, {"1": S6, "2": S6}, S15)
            for k in ("table1", "table2", "table4", "table5", "table7"):
                comptes.setdefault(k, {}).setdefault(t[k], 0)
                comptes[k][t[k]] += 1
            for tab in ("table3", "table6"):
                for lib in t[tab]["1"]:
                    cle = f"{tab} {lib}"
                    v = f"{t[tab]['1'][lib]} / {t[tab]['2'][lib]}"
                    comptes.setdefault(cle, {}).setdefault(v, 0)
                    comptes[cle][v] += 1
        print(f"### {nom}")
        for k, c in comptes.items():
            print(f"  {k} : " + fmt({a: b / N_REP for a, b in c.items()}))
    print()

    print("## 5. Temps processeur mesuré (`time.process_time`, un fil par processus)")
    cpu = np.array([r["cpu_tache_s"] for r in res])
    print(f"  par tâche (8 bras) : moyenne {cpu.mean():.2f} s ; médiane {np.median(cpu):.2f} s ; maximum {cpu.max():.2f} s")
    for cd in (1, 2):
        c = np.array([r["cpu_tache_s"] for r in res if r["code_delta"] == cd])
        print(f"  δ{cd} : moyenne {c.mean():.2f} s ; maximum {c.max():.2f} s")
    for nom in am.TOUS_LES_BRAS:
        fin = np.array([r["bras"][nom]["cpu_final_s"] for r in res])
        tr = np.array([r["bras"][nom].get("cpu_trajectoire_s", 0.0) for r in res])
        print(f"  bras {am.NOMS.get(nom, nom):3s} : trajectoire {tr.mean():.2f} s ; phase finale {fin.mean():.2f} s")
    t = corps["temps"]
    eff = t["cpu_somme_taches_s"] / (t["mur_s"] * t["processus"])
    print(f"  pilote : mur {t['mur_s']:.1f} s sur {t['processus']} processus ; somme des temps processeur "
          f"{t['cpu_somme_taches_s']:.1f} s ; efficacité {eff:.2f}")
    for N in (40, 50, 60, 80, 100):
        tot = 2 * N * cpu.mean()
        print(f"  N = {N:3d} × 2 δ : processeur projeté {tot / 60:.1f} min ; mur projeté sur {COEURS} cœurs "
              f"{tot / COEURS / eff / 60:.1f} min")
    for plafond_h in (1.25, 2.0):
        print(f"  N maximal sous {plafond_h} h de mur sur {COEURS} cœurs : au temps moyen "
              f"{int(plafond_h * 3600 * COEURS * eff / (2 * cpu.mean()))} ; au temps maximal "
              f"{int(plafond_h * 3600 * COEURS * eff / (2 * cpu.max()))}")
    print()

    print("## 6. Plomberie, poids, condition d'application (pilote détection)")
    nc_ = sum(r["non_convergences"] for r in res)
    ne = sum(r["entrainements"] for r in res)
    print(f"  entraînements non convergés : {nc_}/{ne} ; maximum par tâche {max(r['non_convergences'] for r in res)}")
    for cd, bloc in sorted(an.items()):
        a = bloc["attaquant"]
        print(f"  δ{cd} attaquant : départs {a['departs']} ; non finis {a['non_finis']} ; statuts SLSQP {a['statuts']} ;"
              f" itérations max {a['iter_max']} ; réponses à la limite {a['reponses_a_la_limite']}")
        print(f"  δ{cd} écart de fausses alertes entre bras (par tâche) : moyen {bloc['ecart_fpr_entre_bras']['moyen']:.4f}"
              f" ; max {bloc['ecart_fpr_entre_bras']['max']:.4f} ; écart à α des moyennes : " +
              " ; ".join(f"{am.NOMS.get(n, n)} {b['fpr_moyen'] - cfg.alpha:+.4f}" for n, b in bloc["bras"].items()))
        for nom in ("B", "Bp"):
            p = bloc["bras"][nom]["poids"]
            print(f"  δ{cd} {am.NOMS.get(nom, nom)} : poids purs {p['part_pure']:.2f} ; support moyen "
                  f"{p['support_moyen']:.2f} ; poids maximal moyen {p['poids_max_moyen']:.3f} ; valeur du jeu restreint "
                  f"− V {bloc['bras'][nom]['valeur_restreinte_moins_V']:+.4f}")
        print(f"  δ{cd} B = C1 au bit {bloc['B_egal_C1_au_bit']} tâches ; D = A au bit {bloc['D_egal_A_au_bit']} tâches")
        print(f"  δ{cd} V standard − V renforcé : " + " ; ".join(
            f"{am.NOMS.get(n, n)} {b['standard_moins_renforce']:+.4f} (max {b['standard_moins_renforce_max']:+.4f})"
            for n, b in bloc["bras"].items()))
        for lib in ["B-A (iii)"] + COL_Q1 + COL_Q2:
            c = bloc["contrastes"][lib]
            print(f"     {lib} : standard {c['std_attaquant_standard']:+.4f} ; renforcé {c['std_attaquant_renforce']:+.4f}"
                  f" ; retenu {c['moyenne']:+.4f}")
        for n, b in bloc["bras"].items():
            co = b["cout"]
            med = "—" if co["mediane_fraction_non_censurees"] is None else f"{co['mediane_fraction_non_censurees']:.3f}"
            cens = "—" if co["part_censuree_parmi_definies"] is None else f"{co['part_censuree_parmi_definies']:.2f}"
            print(f"  δ{cd} {am.NOMS.get(n, n):3s} coût : défini {co['part_definie']:.2f} ; censuré {cens} ; médiane "
                  f"{med} ; non monotones {co['taches_non_monotones']} ; courbe " +
                  " ".join(f"{x:.3f}" for x in b["courbe_moyenne"]))
        for nom in am.BRAS_TRAJECTOIRE:
            cy = bloc["bras"][nom]["cycle"]
            i3 = "—" if cy["I3_retours"] is None else f"{cy['I3_retours']:.3f}"
            print(f"  δ{cd} {am.NOMS.get(nom, nom):3s} cycle : I1 {cy['I1_progres']:+.4f} ; I2 {cy['I2_oubli']:+.4f} ; "
                  f"I3 {i3} ; rétention " + " ".join(f"k={k} {v:.3f}" for k, v in cy["retention"].items()))
        H = np.array(bloc["bras"]["A"]["cycle"]["H_moyenne"])
        print(f"  δ{cd} A, matrice H moyenne (ligne s = moniteur du tour s, colonne t = attaque du tour t) :")
        for s, ligne in enumerate(H):
            print(f"     s={s} " + " ".join(f"{x:.3f}" for x in ligne))
    for nom in am.BRAS_TRAJECTOIRE:
        nv = np.array([r["bras"][nom]["par_tour"]["nouveaute"] for r in res]).mean(0)
        it = np.array([r["bras"][nom]["par_tour"]["iii"] for r in res]).mean(0)
        print(f"  {am.NOMS.get(nom, nom)} : nouveauté résiduelle par tour " + " ".join(f"{x:.3f}" for x in nv) +
              " ; (iii) par tour " + " ".join(f"{x:.3f}" for x in it))
    print()

    print("## 7. S10 : bande moyenne pilote ± 5 × écart-type par tâche / √N, par bras et par δ (N = 100)")
    for cd in (1, 2):
        txt = []
        for nom in am.TOUS_LES_BRAS:
            x = np.array([r["bras"][nom]["V_iii_final"] for r in res if r["code_delta"] == cd])
            h = 5 * x.std(ddof=1) / np.sqrt(100)
            txt.append(f"{am.NOMS.get(nom, nom)} [{x.mean() - h:.4f} ; {x.mean() + h:.4f}]")
        print(f"  δ{cd} : " + " ; ".join(txt))
    print()

    if len(argv) == 2:
        au = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        print("## 8. Audit d'attaquant indépendant sur le pilote (racine d'essai ; non opposable)")
        print(f"fichier : {argv[1]} ; pilote audité {au['pilote_sha256']} ; artefact selon S17 : "
              f"{au['jugement']['artefact']}")
        for cd, bloc in sorted(au["jugement"]["par_delta"].items()):
            for k, v in bloc.items():
                print(f"  δ{cd} {k} : run {v['source']:+.4f} ; audit {v['audit']:+.4f} ; écart {v['ecart']:+.4f} ; "
                      f"écart maximal par tâche {v['ecart_max_tache']:.4f} ; n {v['n']} ; artefact {v['artefact']}")
        for tch in au["taches"]:
            print(f"  tâche instance {tch['instance']}, δ{tch['code_delta']} : " + " ; ".join(
                f"{am.NOMS.get(n, n)} {b['V_source']:.4f} → lourd {b['V_lourd']:.4f}, évol. {b['V_evolution_depuis_lourd']:.4f}"
                f" / {b['V_evolution_depuis_standard']:.4f}" for n, b in tch["bras"].items()))
        t = au["temps"]
        cpu_a = np.array([x["cpu_tache_s"] for x in au["taches"]])
        print(f"  temps : mur {t['mur_s']:.1f} s ; processeur par tâche auditée {cpu_a.mean():.1f} s (max "
              f"{cpu_a.max():.1f}) ; 10 tâches de la décision sur {COEURS} cœurs : ≈ "
              f"{10 * cpu_a.mean() / COEURS / 60:.1f} min")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
