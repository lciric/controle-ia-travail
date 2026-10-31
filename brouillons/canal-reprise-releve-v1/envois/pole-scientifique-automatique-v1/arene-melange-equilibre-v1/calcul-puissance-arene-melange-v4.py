#!/usr/bin/env python3
"""Calcul de puissance de l'arène « mélange d'équilibre » — v4, sur le pilote v4 (racine d'essai gelée 20264201)
seulement ; simulations tirées de la racine gelée RACINE_SIMULATION = 20264401 (une clé de dérivation par simulation).

Lit le pilote « détection » produit par `arene_melange_v4.py essai` (refuse toute racine non permise et toute autre
configuration que CONFIG_V4) et, en option, la sortie de `audit-essai`. Rapporte :
 1-2. moyennes par bras et contrastes appariés du pilote (indicateurs I1, I2, I3 − valeur nulle compris) ;
 3. les règles de lecture évaluées avec le rééchantillonnage de la décision (N instances tirées du pilote, centrées et
    décalées selon le scénario, 20 000 tirages, quantiles linéaires ; 1 000 répétitions par scénario) ; Table 5 v4 ;
 4. la lecture simulée des Tables 1 à 7 (`lire_tables` du code) ; P10 avec l'incertitude du pilote (CM3-06) ;
 5. le temps processeur et le temps de mur projeté (décision à N = 100 contre le délai de 9 000 s ; audit de 20 tâches) ;
 6. la plomberie, les poids de B et B′ (pureté, pureté forcée, indice du moniteur dominant), B′ − X selon la pureté ;
 7. S10 v4 : bandes moyenne pilote ± k × écart-type × √(1/n_pilote + 1/N), k = 3 (repli k = 4 si le taux simulé de
    fausse alerte des 16 bandes dépasse 0,05, gel v4 § 3.4) ; taux simulés, comparés à la règle v3 ;
 8. l'audit d'essai (si fourni) et la simulation du taux de fausse alerte et de la puissance du critère S17 v4 (repli
    t(K − 1 ; 0,9995) si le taux dépasse 0,05, gel v4 § 3.2) ;
 9. la valeur nulle de I3 par simulation.
Marges par principe (gel v3) : m = S1 = S5 = S6 = S15 = 0,02. Aucune marge ne vient du pilote.

    PYTHONPATH=src python3 calcul-puissance-arene-melange-v4.py PILOTE.json [PILOTE_SUITE.json …] [--audit AUDIT_ESSAI.json]

Le pilote peut être donné en plusieurs fichiers produits par le même code sur des instances disjointes de la même racine
(chaque tâche ne dépend que de sa racine, de son δ et de son instance : l'union est identique au bit à un seul lancement) ;
l'analyse (rééchantillonnage) est alors recalculée sur l'union par `analyser` du code.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.stats import t as loi_t

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import arene_melange_v4 as am  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

N_REP = 1000
N_REECH = 20000
N_DECISION = 100
S1 = S5 = S6 = S15 = 0.02
COEURS = 2
DELAI_DECISION_S = 9000.0
CLASSES = ("B>X", "X>B", "≈", "B≳X", "X≳B", "?")
COL_Q1 = list(am.CONTRASTES_PRINCIPAUX)
COL_Q2 = list(am.CONTRASTES_Q2)
COL_AUTRES = ["B-A (iii)", "B-A (ii)"]
COL_IND = ["A I1", "A I3-nul"]
# clés de dérivation des simulations (racine gelée RACINE_SIMULATION) : une par simulation
CLE = {"regles": 1, "s10": 2, "audit": 3, "p10": 4, "i3": 5}


def rng(nom: str) -> np.random.Generator:
    return am.gen(am.RACINE_SIMULATION, 0, 0, 0, CLE[nom], 77)


def charger(chemin):
    corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
    man = corps["manifeste"]
    am.exiger_racines_essai(man["racine"], man["racine_tenue"])
    if corps.get("mode") != "essai" or corps.get("oracle") != "detection":
        raise GardeArret(f"{chemin} : pas un essai d'oracle détection")
    if am.CONFIG_V4 is None or man["config_sha256"] != am.CONFIG_V4.empreinte():
        raise GardeArret(f"{chemin} : configuration différente de celle du code")
    if man["versions"]["code_sha256"] != am.empreinte_fichier(am.__file__):
        raise GardeArret(f"{chemin} : produit par un autre code que celui-ci")
    for r in corps["resultats"]:
        am.exiger_racines_essai(r["racine"], r["racine_tenue"])
    return corps


def charger_tous(chemins):
    """Union de pilotes du même code, de la même racine, sur des instances disjointes ; analyse recalculée sur l'union."""
    parts = [charger(c) for c in chemins]
    m0 = parts[0]["manifeste"]
    for c, p in zip(chemins, parts):
        m = p["manifeste"]
        if (m["racine"], m["racine_tenue"], m["config_sha256"]) != (m0["racine"], m0["racine_tenue"], m0["config_sha256"]):
            raise GardeArret(f"{c} : racine ou configuration différente du premier fichier")
    res = [r for p in parts for r in p["resultats"]]
    cles = [(r["instance"], r["code_delta"]) for r in res]
    if len(set(cles)) != len(cles):
        raise GardeArret("pilotes à instances non disjointes : tâche en double")
    corps = {"manifeste": m0, "resultats": res, "parties": [{"fichier": str(c), "sha256": am.empreinte_fichier(c),
                                                              "temps": p["temps"], "taches": len(p["resultats"]),
                                                              "commande": p["manifeste"].get("commande")}
                                                             for c, p in zip(chemins, parts)]}
    corps["analyse"] = parts[0]["analyse"] if len(parts) == 1 else am.analyser(res, m0["racine"])
    corps["temps"] = {"mur_s": sum(p["temps"]["mur_s"] for p in parts),
                      "cpu_somme_taches_s": sum(p["temps"]["cpu_somme_taches_s"] for p in parts),
                      "processus": parts[0]["temps"]["processus"], "taches": len(res)}
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


def quantiles_reech(Dn, g):
    """Rééchantillonnage de la décision : indices uniformes (B × N), moyennes, quantiles linéaires."""
    N = len(Dn)
    idx = g.integers(0, N, size=(N_REECH, N))
    comptes = np.bincount((idx + N * np.arange(N_REECH)[:, None]).ravel(), minlength=N_REECH * N).reshape(N_REECH, N)
    moy = comptes @ Dn / N
    return Dn.mean(0), dict(zip(am.QUANTILES, np.quantile(moy, am.QUANTILES, axis=0))), idx, moy


def simuler(D, purs, N, decalage, g, n_rep=N_REP):
    """n_rep répétitions : N instances tirées du pilote (D centré puis décalé si `decalage` n'est pas None), quantiles
    de la décision. Renvoie la liste des (moyennes, quantiles, parts pures par δ)."""
    Dc = D if decalage is None else D - D.mean(0) + decalage
    sortie = []
    for _ in range(n_rep):
        ix = g.integers(0, len(D), size=N)
        m, q, _, _ = quantiles_reech(Dc[ix], g)
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


def ecarts_audit(au):
    """Écarts c_i par tâche de l'audit d'essai, par δ et par paire (et I1, I3 de A), tels que `juger_audit`."""
    sortie = {}
    for cd, bloc in au["jugement"]["par_delta"].items():
        sortie[cd] = {k: np.array(v["ecarts"]) for k, v in bloc.items() if v.get("ecarts") is not None}
    return sortie


def juger_simule(an_sim, c_par_cd, K, quantile_t):
    """Applique le critère S17 v4 complet ((i) écart pratique, (ii) changement de classe démontré) à une analyse de
    décision simulée et à des écarts d'audit simulés (K tâches par δ). Renvoie (un drapeau (i), un drapeau (ii))."""
    mult = float(loi_t.ppf(quantile_t, K - 1))
    jug = {"par_delta": {}}
    for cd, cs in c_par_cd.items():
        bloc = {}
        for cle, c in cs.items():
            moy, es = float(c.mean()), float(c.std(ddof=1) / np.sqrt(K))
            bloc[cle] = {"ecart_moyen": moy, "significatif": bool(abs(moy) > mult * es),
                         "drapeau_i": bool(abs(moy) > am.CONFIG_V4.audit_critere) if cle != "A I3" else False}
        jug["par_delta"][cd] = bloc
    cl = am.classes_sous_audit(an_sim, jug, S1, {"1": S6, "2": S6}, S15)["par_delta"]
    return (any(v["drapeau_i"] for b in cl.values() for v in b.values()),
            any(v["drapeau_ii"] for b in cl.values() for v in b.values()))


def main(argv):
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("pilotes", nargs="+")
    ap.add_argument("--audit", default=None)
    args = ap.parse_args(argv)
    corps = charger_tous(args.pilotes)
    cfg = am.CONFIG_V4
    res = corps["resultats"]
    man = corps["manifeste"]
    an = corps["analyse"]
    print("# Calcul de puissance — arène mélange d'équilibre — v4 (pilote v4, racine d'essai gelée)")
    for pa in corps["parties"]:
        print(f"fichier : {pa['fichier']} — {pa['sha256']} ; {pa['taches']} tâches ; mur {pa['temps']['mur_s']:.1f} s ; "
              f"processeur {pa['temps']['cpu_somme_taches_s']:.1f} s ; {pa['temps']['processus']} processus")
    if len(corps["parties"]) > 1:
        print("  (pilote en plusieurs lancements du même code sur des instances disjointes ; analyse recalculée sur "
              "l'union par `analyser` ; chaque tâche est identique au bit à un lancement unique)")
    print(f"racine = {man['racine']} ; racine des tenues = {man['racine_tenue']} ; configuration {man['config_sha256']}"
          f" ; δ = {cfg.deltas}")
    v = man["versions"]
    print(f"code : {v['code_sha256']} ; commit {v['commit']} (HEAD du dépôt ; le code remis n'y est pas committé) ; "
          f"numpy {v['numpy']} ; scipy {v['scipy']} ; gel v4 {man.get('gel_v4_sha256')}")
    n_inst = len({r['instance'] for r in res})
    print(f"tâches lues : {len(res)} ({n_inst} instances × 2 δ) ; simulations : SeedSequence({am.RACINE_SIMULATION}, "
          f"spawn_key=(0, 0, 0, clé, 77)), clés {CLE} ; {N_REP} répétitions × {N_REECH} tirages par scénario")
    print()

    print("## 1. Moyennes par bras (pilote détection)")
    for cd, bloc in sorted(an.items()):
        print(f"δ{cd} = {bloc['delta']}, n = {bloc['n']}")
        for nom, b in bloc["bras"].items():
            print(f"  {am.NOMS.get(nom, nom):3s} : (iii) {b['V_iii_final']:.4f} [min {b['V_min_tache']:.4f} ; max "
                  f"{b['V_max_tache']:.4f}] ; (ii) {b['ii_final']:.4f} ; (i) {b['i_final_vus']:.4f} ; fausses alertes "
                  f"{b['fpr_moyen']:.4f} [{b['fpr_min']:.4f} ; {b['fpr_max']:.4f}] ; paramètres stockés "
                  f"{b['parametres_deployes']}, par requête ≤ {b['parametres_par_requete_max']}")
        print(f"  V(A) en multiples de α : {bloc['bras']['A']['V_iii_final'] / cfg.alpha:.1f} α")
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
    print(f"  valeur nulle de I3 (T = {cfg.T}) : {am.valeur_nulle_I3(cfg.T):.4f}")
    print()

    colonnes = COL_Q1 + COL_Q2 + COL_AUTRES + COL_IND
    D, inst = matrice(res, colonnes)
    purs = np.array([[am.est_pur(r["bras"]["Bp"]["poids_finaux"]) for r in sorted(
        (x for x in res if x["instance"] == i), key=lambda x: x["code_delta"])] for i in inst], float)
    nc = len(colonnes)
    g = rng("regles")
    _, _, idx, moy = quantiles_reech(D, g)
    assert np.allclose(moy, D[idx].mean(1), atol=1e-12, rtol=0)

    print("## 3. Règles de lecture sous le rééchantillonnage de la décision")
    print(f"   marges par principe : m = S6 = {S6} (Q1 et Q2) ; S1 = S5 = S15 = {S1}")
    scen = {"pilote N=100": simuler(D, purs, 100, None, g)}
    dec = np.zeros(2 * nc)

    def decaler(valeurs):
        d = dec.copy()
        for lib, x in valeurs.items():
            for k in (0, 1):
                d[k * nc + colonnes.index(lib)] = x
        return d

    scen["frontière +"] = simuler(D, purs, 100, decaler({**{c: S6 for c in COL_Q1 + COL_Q2}, "B-A (iii)": S1,
                                                         "B-A (ii)": 0.0, "A I1": S15, "A I3-nul": 0.0}), g)
    scen["frontière −"] = simuler(D, purs, 100, decaler({**{c: -S6 for c in COL_Q1 + COL_Q2}, "B-A (iii)": 0.0,
                                                         "B-A (ii)": -S5, "A I1": 0.0, "A I3-nul": 0.0}), g)
    scen["nul"] = simuler(D, purs, 100, decaler({**{c: 0.0 for c in COL_Q1 + COL_Q2}, "B-A (iii)": 0.03,
                                                 "B-A (ii)": 0.0, "A I1": 0.0, "A I3-nul": 0.1}), g)

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
    niv8 = (0.003125, 0.996875, 0.00625, 0.99375)
    niv4 = (0.00625, 0.99375, 0.0125, 0.9875)
    for titre, libs, niv, nominal in (("3b. Q1 (Table 3), bornes B8, équivalence E8", COL_Q1, niv8,
                                       "0,003 (supériorité) ; 0,006 (équivalence, par côté)"),
                                      ("3c. Q2 (Table 6), bornes B4, équivalence E4", COL_Q2, niv4,
                                       "0,00625 (supériorité) ; 0,0125 (équivalence, par côté)")):
        print(f"### {titre} : probabilité de chaque classe (pilote pris pour vérité, N = 100)")
        for (lib, k), d in classes_par_test(scen["pilote N=100"], colonnes, libs, niv).items():
            print(f"    {lib:12s} δ{k} (pilote {D[:, col(lib, k - 1)].mean():+.4f}) : {fmt(d)}")
        print("  tailles à la frontière (N = 100) : P(B>X | Δ=+m) ; P(X>B | Δ=−m) ; P(≈ | Δ=+m) ; P(≈ | Δ=−m) ; "
              "puissance P(≈ | Δ=0)")
        cp, cm, c0 = (classes_par_test(scen[s], colonnes, libs, niv) for s in ("frontière +", "frontière −", "nul"))
        for key in cp:
            print(f"    {key[0]:12s} δ{key[1]} : {cp[key].get('B>X', 0):.3f} ; {cm[key].get('X>B', 0):.3f} ; "
                  f"{cp[key].get('≈', 0):.3f} ; {cm[key].get('≈', 0):.3f} ; {c0[key].get('≈', 0):.3f}")
        print(f"  nominal par test : {nominal}")
    print("### 3d. Table 2 (ii), S5 = 0,02, N = 100 : « sans régression » et « régression avérée »")
    for nom, s in (("écart nul (frontière +)", scen["frontière +"]), ("écart −S5 (frontière −)", scen["frontière −"]),
                   ("pilote", scen["pilote N=100"])):
        sr = prob(s, lambda m, q: all(q[0.00625][col("B-A (ii)", k)] > -S5 for k in (0, 1)))
        av = prob(s, lambda m, q: any(q[0.99375][col("B-A (ii)", k)] < -S5 for k in (0, 1)))
        print(f"  {nom} : borne basse > −S5 aux deux δ {sr:.3f} ; régression avérée {av:.3f}")
    print("### 3e. Table 5 v4 (I1 et I3 − nul de A), bornes B2, S15 = 0,02, N = 100")
    for nom, s in (("I1 = S15, I3 − nul = 0 (frontière +)", scen["frontière +"]),
                   ("I1 = 0, I3 − nul = 0 (frontière −)", scen["frontière −"]),
                   ("I1 = 0, I3 − nul = 0,1 (nul)", scen["nul"]), ("pilote", scen["pilote N=100"])):
        print(f"  {nom} : " + " ; ".join(
            f"δ{k + 1} P(I1 haute < S15) {prob(s, lambda m, q: q[0.99375][col('A I1', k)] < S15):.3f}, "
            f"P(I1 basse > S15) {prob(s, lambda m, q: q[0.00625][col('A I1', k)] > S15):.3f}, "
            f"P(I3−nul basse > 0) {prob(s, lambda m, q: q[0.00625][col('A I3-nul', k)] > 0):.3f}, "
            f"P(I3−nul haute < 0) {prob(s, lambda m, q: q[0.99375][col('A I3-nul', k)] < 0):.3f}" for k in (0, 1)))
    print("  lecture : sous « frontière + », P(I1 haute < S15) est une taille (nominal 0,00625) ; sous I3 − nul = 0, "
          "P(I3−nul basse > 0) et P(I3−nul haute < 0) sont des tailles (nominal 0,00625)")
    print()

    print("## 4. Lecture simulée des Tables 1 à 7 (`lire_tables`, pilote pris pour vérité, 1 000 répétitions, N = 100)")
    comptes = {}
    for m, q, pur in scen["pilote N=100"]:
        t = am.lire_tables(fausse_analyse(m, q, pur, colonnes), S1, S5, {"1": S6, "2": S6}, S15)
        for k in ("table1", "table2", "table4", "table5", "table7"):
            comptes.setdefault(k, {}).setdefault(t[k], 0)
            comptes[k][t[k]] += 1
        cle5 = " / ".join(t["table5_par_delta"][cd] for cd in ("1", "2"))
        comptes.setdefault("table5 par δ", {}).setdefault(cle5, 0)
        comptes["table5 par δ"][cle5] += 1
        for tab in ("table3", "table6"):
            for lib in t[tab]["1"]:
                cle = f"{tab} {lib}"
                vv = f"{t[tab]['1'][lib]} / {t[tab]['2'][lib]}"
                comptes.setdefault(cle, {}).setdefault(vv, 0)
                comptes[cle][vv] += 1
    for k, c in comptes.items():
        print(f"  {k} : " + fmt({a: b / N_REP for a, b in c.items()}))
    print("### 4b. P10 (« Q2 non exercée ») avec l'incertitude du pilote (CM3-06) : part pure par δ ~ bêta(k + 1, "
          "n − k + 1), puis binomiale à N = 100")
    gp = rng("p10")
    kp = purs.sum(0)
    n = len(purs)
    p_tir = np.column_stack([gp.beta(kp[j] + 1, n - kp[j] + 1, size=200000) for j in (0, 1)])
    x = gp.binomial(N_DECISION, p_tir)
    ne = (x > N_DECISION / 2)
    print(f"  pilote : part pure {kp[0]:.0f}/{n} (δ1) ; {kp[1]:.0f}/{n} (δ2) ; P(part pure > 0,5 | δ1) "
          f"{ne[:, 0].mean():.3f} ; | δ2 {ne[:, 1].mean():.3f} ; à au moins un δ {ne.any(1).mean():.3f} "
          f"(conditionnel au pilote, section 4 : {comptes['table7'].get('Q2 non exercée (au moins un δ)', 0) / N_REP:.3f})")
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
    effs = []
    for pa in corps["parties"]:
        t = pa["temps"]
        e = t["cpu_somme_taches_s"] / (t["mur_s"] * t["processus"])
        effs.append(e)
        print(f"  lancement {Path(pa['fichier']).name} : mur {t['mur_s']:.1f} s sur {t['processus']} processus ; somme des "
              f"temps processeur {t['cpu_somme_taches_s']:.1f} s ; efficacité {e:.2f} (machine partagée)")
    eff = min(effs)
    for N in (60, 80, 100):
        tot = 2 * N * cpu.mean()
        print(f"  N = {N:3d} × 2 δ : processeur projeté {tot / 60:.1f} min ; mur projeté sur {COEURS} cœurs "
              f"{tot / COEURS / eff / 60:.1f} min à l'efficacité du pilote ; {tot / COEURS / 60:.1f} min à efficacité 1")
    tot = 2 * N_DECISION * cpu.mean()
    for e in (1.0, 0.9, eff, 0.65):
        print(f"  décision N = 100, efficacité {e:.2f} : {tot / COEURS / e:.0f} s de mur, soit "
              f"{100 * tot / COEURS / e / DELAI_DECISION_S:.0f} % du délai de {DELAI_DECISION_S:.0f} s")
    print(f"  efficacité minimale pour tenir {DELAI_DECISION_S:.0f} s : {tot / COEURS / DELAI_DECISION_S:.2f} (au temps "
          f"moyen) ; marge au temps moyen et à l'efficacité du pilote : {DELAI_DECISION_S / (tot / COEURS / eff) - 1:+.0%}")
    print()

    print("## 6. Plomberie, poids, condition d'application (pilote détection)")
    nc_ = sum(r["non_convergences"] for r in res)
    ne_ = sum(r["entrainements"] for r in res)
    print(f"  entraînements non convergés : {nc_}/{ne_} ; maximum par tâche {max(r['non_convergences'] for r in res)} "
          f"(S18 = {cfg.taux_nonconv_max} par tâche)")
    for cd, bloc in sorted(an.items()):
        a = bloc["attaquant"]
        print(f"  δ{cd} attaquant : départs {a['departs']} ; non finis {a['non_finis']} ; statuts SLSQP {a['statuts']} ;"
              f" itérations max {a['iter_max']} ; réponses à la limite {a['reponses_a_la_limite']}")
        print(f"  δ{cd} écart de fausses alertes entre bras (par tâche) : moyen {bloc['ecart_fpr_entre_bras']['moyen']:.4f}"
              f" ; max {bloc['ecart_fpr_entre_bras']['max']:.4f} ; écart à α des moyennes : " +
              " ; ".join(f"{am.NOMS.get(n, n)} {b['fpr_moyen'] - cfg.alpha:+.4f}" for n, b in bloc["bras"].items()))
        for nom in ("B", "Bp"):
            p = bloc["bras"][nom]["poids"]
            eq = bloc["bras"][nom]["equilibre"]
            ppp = eq["part_purete_forcee_parmi_pures"]
            print(f"  δ{cd} {am.NOMS.get(nom, nom)} : poids purs {p['part_pure']:.3f} ; support moyen "
                  f"{p['support_moyen']:.2f} ; poids maximal moyen {p['poids_max_moyen']:.3f} ; valeur du jeu restreint "
                  f"− V {bloc['bras'][nom]['valeur_restreinte_moins_V']:+.4f} ; plus petit poids maximal parmi les "
                  f"équilibres (moyenne) {eq['poids_max_min_moyen']:.3f} ; pureté forcée {eq['part_purete_forcee']:.3f}"
                  f" (parmi les tâches pures : {'—' if ppp is None else f'{ppp:.3f}'}, n = {eq['n_pures']}) ; indice du "
                  f"moniteur de poids maximal {eq['indices_poids_max']} ; tâches pures {eq['indices_poids_max_taches_pures']}")
        for lib in COL_Q2:
            sp = bloc["contrastes"][lib]["selon_purete"]
            print(f"  δ{cd} {lib} selon la pureté de B′ : " + " ; ".join(
                f"{k} n {x['n']} moyenne {'—' if x['moyenne'] is None else f'{x['moyenne']:+.4f}'} (erreur-type "
                f"{'—' if x['erreur_type'] is None else f'{x['erreur_type']:.4f}'})" for k, x in sp.items()))
        print(f"  δ{cd} B = C1 au bit {bloc['B_egal_C1_au_bit']} tâches ; D = A au bit {bloc['D_egal_A_au_bit']} tâches")
        print(f"  δ{cd} V standard − V renforcé : " + " ; ".join(
            f"{am.NOMS.get(n, n)} {b['standard_moins_renforce']:+.4f} (max {b['standard_moins_renforce_max']:+.4f})"
            for n, b in bloc["bras"].items()))
        for lib in ["B-A (iii)"] + COL_Q1 + COL_Q2:
            c = bloc["contrastes"][lib]
            print(f"     {lib} : standard {c['std_attaquant_standard']:+.4f} ; renforcé {c['std_attaquant_renforce']:+.4f}"
                  f" ; retenu {c['moyenne']:+.4f}")
        for n_, b in bloc["bras"].items():
            co = b["cout"]
            med = "—" if co["mediane_fraction_non_censurees"] is None else f"{co['mediane_fraction_non_censurees']:.3f}"
            cens = "—" if co["part_censuree_parmi_definies"] is None else f"{co['part_censuree_parmi_definies']:.2f}"
            print(f"  δ{cd} {am.NOMS.get(n_, n_):3s} coût : défini {co['part_definie']:.2f} ; censuré {cens} ; médiane "
                  f"{med} ; non monotones {co['taches_non_monotones']} ; courbe " +
                  " ".join(f"{x:.3f}" for x in b["courbe_moyenne"]))
        for nom in am.BRAS_TRAJECTOIRE:
            cy = bloc["bras"][nom]["cycle"]
            i3 = "—" if cy["I3_retours"] is None else f"{cy['I3_retours']:.3f}"
            print(f"  δ{cd} {am.NOMS.get(nom, nom):3s} cycle : I1 {cy['I1_progres']:+.4f} ; I2 (baisse sur les attaques "
                  f"passées) {cy['I2_oubli']:+.4f} ; I3 {i3} (valeur nulle {cy['I3_nul']:.4f}) ; rétention " +
                  " ".join(f"k={k} {v:.3f}" for k, v in cy["retention"].items()))
    for nom in am.BRAS_TRAJECTOIRE:
        nv = np.array([r["bras"][nom]["par_tour"]["nouveaute"] for r in res]).mean(0)
        it = np.array([r["bras"][nom]["par_tour"]["iii"] for r in res]).mean(0)
        print(f"  {am.NOMS.get(nom, nom)} : nouveauté résiduelle par tour " + " ".join(f"{x:.3f}" for x in nv) +
              " ; (iii) par tour " + " ".join(f"{x:.3f}" for x in it))
    print()

    print("## 7. S10 v4 : bandes moyenne pilote ± k × écart-type × √(1/n_pilote + 1/N), par bras et par δ (N = 100)")
    VA = {}
    for r in res:
        VA.setdefault(r["instance"], {})[r["code_delta"]] = [r["bras"][nom]["V_iii_final"] for nom in am.TOUS_LES_BRAS]
    Vm = np.array([VA[i][1] + VA[i][2] for i in sorted(VA) if set(VA[i]) == {1, 2}])      # instances × 16 bandes
    npil = len(Vm)
    gs = rng("s10")
    n_sim = 5000

    def taux_s10(regle, k):
        hors = 0
        for _ in range(n_sim):
            pil = Vm[gs.integers(0, npil, size=npil)]
            dec_ = Vm[gs.integers(0, npil, size=N_DECISION)]
            sd = pil.std(0, ddof=1)
            h = k * sd * np.sqrt(1 / npil + 1 / N_DECISION) if regle == "v4" else k * sd / np.sqrt(N_DECISION)
            hors += bool(np.any(np.abs(dec_.mean(0) - pil.mean(0)) > h))
        return hors / n_sim

    tv3 = taux_s10("v3", 5)
    t3, t4 = taux_s10("v4", 3), taux_s10("v4", 4)
    k_retenu = 3 if t3 <= 0.05 else 4
    print(f"  taux simulé de fausse alerte sur les 16 bandes ({n_sim} paires pilote/décision tirées par tâches entières "
          f"du pilote) : règle v3 (± 5 é.-t./√N, centrée sur le pilote) {tv3:.3f} ; v4 k = 3 {t3:.3f} ; v4 k = 4 {t4:.3f}")
    print(f"  k retenu par la règle du gel v4 (§ 3.4 : k = 3, repli k = 4 si le taux dépasse 0,05) : k = {k_retenu}")
    for cd in (1, 2):
        txt = []
        for j, nom in enumerate(am.TOUS_LES_BRAS):
            x = Vm[:, (cd - 1) * len(am.TOUS_LES_BRAS) + j]
            h = k_retenu * x.std(ddof=1) * np.sqrt(1 / npil + 1 / N_DECISION)
            txt.append(f"{am.NOMS.get(nom, nom)} [{x.mean() - h:.4f} ; {x.mean() + h:.4f}]")
        print(f"  δ{cd} : " + " ; ".join(txt))
    print()

    if args.audit is not None:
        au = json.loads(Path(args.audit).read_text(encoding="utf-8"))
        if au.get("pilote_sha256") not in {pa["sha256"] for pa in corps["parties"]}:
            raise GardeArret("audit d'essai rattaché à un autre pilote")
        V = {(r["instance"], r["code_delta"]): r for r in res}
        for tch in au["taches"]:
            for nom, b in tch["bras"].items():
                if b["V_source"] != V[(tch["instance"], tch["code_delta"])]["bras"][nom]["V_iii_final"]:
                    raise GardeArret("audit d'essai : V source ≠ V du pilote")
        an_audit = json.loads(Path(next(pa["fichier"] for pa in corps["parties"]
                                        if pa["sha256"] == au["pilote_sha256"])).read_text(encoding="utf-8"))["analyse"]
        cl_union = am.classes_sous_audit(an, au["jugement"], S1, {"1": S6, "2": S6}, S15)
        print("## 8. Audit d'attaquant indépendant sur le pilote (racine d'essai ; non opposable)")
        print(f"fichier : {args.audit} ; pilote audité {au['pilote_sha256']} ; drapeau (i) {au['jugement']['drapeau_i']} ; "
              f"artefact (i ou ii, marges 0,02) : sur l'analyse du fichier audité {au['classes_sous_audit']['artefact']}, "
              f"sur l'analyse du pilote entier {cl_union['artefact']}")
        assert an_audit is not None
        for cd, bloc in sorted(au["jugement"]["par_delta"].items()):
            for k, v in bloc.items():
                if v.get("ecart_moyen") is None:
                    print(f"  δ{cd} {k} : {v.get('note')}")
                    continue
                print(f"  δ{cd} {k:6s} : écart moyen {v['ecart_moyen']:+.4f} ; erreur-type {v['erreur_type']:.4f} ; "
                      f"t × é.-t. {v['borne_t']:.4f} ; écart maximal par tâche {v['ecart_max_tache']:.4f} ; n {v['n']} ; "
                      f"(i) {v['drapeau_i']} ; significatif {v['significatif']}")
            for k, v in cl_union["par_delta"][cd].items():
                if k == "Table 5":
                    print(f"  δ{cd} Table 5 : {v['ligne_lue']} → {v['ligne_decalee']} ; (ii) {v['drapeau_ii']}")
                else:
                    print(f"  δ{cd} {k:6s} : classe {v['classe_lue']} → {v['classe_decalee']} ; (ii) {v['drapeau_ii']}")
        choix = {}
        for tch in au["taches"]:
            for nom, b in tch["bras"].items():
                choix.setdefault(nom, {}).setdefault(b["choix_audit"], 0)
                choix[nom][b["choix_audit"]] += 1
        print(f"  choix de l'audit par bras : {choix}")
        ta = [tch["tours_A"] for tch in au["taches"]]
        print(f"  tours de A : (iii) baissé par la réponse renforcée dans "
              f"{sum(sum(a < s for a, s in zip(x['iii_audit'], x['iii_source'])) for x in ta)} tours sur "
              f"{sum(len(x['iii_source']) for x in ta)} ; baisse moyenne "
              f"{np.mean([np.mean(np.array(x['iii_source']) - np.array(x['iii_audit'])) for x in ta]):.4f}")
        tt = au["temps"]
        cpu_a = np.array([x["cpu_tache_s"] for x in au["taches"]])
        eff_a = tt["cpu_somme_taches_s"] / (tt["mur_s"] * tt["processus"])
        print(f"  temps : mur {tt['mur_s']:.1f} s ; processeur par tâche auditée {cpu_a.mean():.1f} s (max "
              f"{cpu_a.max():.1f}) ; efficacité {eff_a:.2f} ; audit de la décision (2 × K = {2 * cfg.audit_k} tâches) "
              f"sur {COEURS} cœurs : ≈ {2 * cfg.audit_k * cpu_a.mean() / COEURS / 60:.1f} min à efficacité 1, "
              f"{2 * cfg.audit_k * cpu_a.mean() / COEURS / eff_a / 60:.1f} min à l'efficacité mesurée")

        print("### 8b. Critère S17 v4 : taux de fausse alerte et puissance simulés")
        print("   décision simulée : N = 100 instances tirées du pilote (section 3, « pilote N=100 ») ; audit simulé : "
              f"K = {cfg.audit_k} écarts par δ tirés avec remise parmi ceux de l'audit d'essai ({len(au['taches']) // 2} "
              "par δ), pour chaque paire et pour I1, I3 de A")
        E = ecarts_audit(au)
        ga = rng("audit")
        K = cfg.audit_k
        an_sims = [fausse_analyse(m, q, pur, colonnes) for m, q, pur in scen["pilote N=100"]]

        def taux(transfo, quantile_t, n=2000, detail=False):
            a_i = a_ii = a = 0
            for r_ in range(n):
                an_sim = an_sims[r_ % len(an_sims)]
                c_sim = {cd: {k: transfo(k, x[ga.integers(0, len(x), size=K)], x) for k, x in cs.items()}
                         for cd, cs in E.items()}
                d_i, d_ii = juger_simule(an_sim, c_sim, K, quantile_t)
                a_i, a_ii, a = a_i + d_i, a_ii + d_ii, a + (d_i or d_ii)
            return (a / n, a_i / n, a_ii / n) if detail else a / n

        centre = (lambda k, tir, x: tir - x.mean())
        brut = (lambda k, tir, x: tir)
        gauss2 = (lambda k, tir, x: ga.normal(0.0, 2 * max(x.std(ddof=1), 1e-12), size=K))
        q_t = cfg.audit_quantile_t
        (f_c, f_ci, f_cii), (f_b, f_bi, f_bii), (f_g, f_gi, f_gii) = (taux(t_, q_t, detail=True)
                                                                     for t_ in (centre, brut, gauss2))
        print(f"  fausse alerte (sur les 12 tests : 5 paires + Table 5, aux deux δ), t(K − 1 ; {q_t}) — total (i seul ; "
              f"ii seul) : écarts centrés (aucun artefact : définition de la fausse alerte) {f_c:.3f} ({f_ci:.3f} ; "
              f"{f_cii:.3f}) ; bruit gaussien d'écart-type double, centré {f_g:.3f} ({f_gi:.3f} ; {f_gii:.3f}) ; écarts "
              f"bruts (amélioration systématique observée reconduite : ce n'est plus une fausse alerte au sens strict) "
              f"{f_b:.3f} ({f_bi:.3f} ; {f_bii:.3f})")
        if f_c > 0.05:
            f_c2, f_b2 = taux(centre, 0.9995), taux(brut, 0.9995)
            print(f"  repli du gel v4 § 3.2 déclenché (taux centré > 0,05) : t(K − 1 ; 0,9995) : centrés {f_c2:.3f} ; "
                  f"bruts {f_b2:.3f}")
        else:
            print("  repli du gel v4 § 3.2 non déclenché (taux centré ≤ 0,05)")
        for paire in ("Bp-D", "B-C3"):
            ligne = []
            for s in (0.005, 0.01, 0.015, 0.02):
                def avec(k, tir, x, s=s, paire=paire):
                    return tir - x.mean() + (s if k == paire else 0.0)
                ligne.append(f"écart {s:.3f} : {taux(avec, q_t, n=1000):.3f}")
            print(f"  puissance (écart moyen ajouté à {paire} aux deux δ, autres paires centrées) : " + " ; ".join(ligne))
        print()

    print("## 9. Valeur nulle de I3 par simulation (déplacements tirés au hasard, dimension 36, T = 8)")
    gi = rng("i3")
    x = [am.taux_retours(list(gi.standard_normal((cfg.T, 36)))) for _ in range(20000)]
    print(f"  moyenne simulée {np.mean(x):.4f} (erreur-type {np.std(x, ddof=1) / np.sqrt(len(x)):.4f}) ; formule "
          f"{am.valeur_nulle_I3(cfg.T):.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
