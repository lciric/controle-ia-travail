"""E1 (suite) — probabilite d'epuiser 32 tirages et probabilite que la course s'arrete sur sa « Liste d'arret », point 3
(garde exacte sur rejets et reprises), a partir des sous-predicats mesures sur les textes reels (`e1-actions.jsonl`).

Trois scenarios de gabarit prive, declares (aucun n'est regle sur les donnees) :
  S0  textes prives de la course de dose-reponse, tels que joues (taux mesures par bras) ;
  S1  gabarit prive neuf « ideal » : les bras instruits ecrivent toujours le cout au format exige (predicat 3 tenu) et ne
      citent jamais leur texte prive ; leurs autres rejets (champs, structure, vocabulaire naturel) sont ceux de l'honnete,
      qui n'a aucun bloc prive et garde ses propres rejets du predicat 3 (le format public demande « a single number ») ;
  S2  gabarit prive neuf qui ne dicte pas le format : predicat 3 des bras instruits egal a celui de l'honnete ; leurs
      rejets des autres predicats sont ceux mesures par bras (fuites du predicat 4 comprises).
Deux lectures de l'historique : « brut » (tous les pas, historique reel, derive comprise) et « propre » (pas 0, et pas
suivants dont tous les pas precedents sont acceptes : c'est l'etat dans lequel la course a rejet place chaque pas).
Reechantillonnage des taches (SeedSequence), 4 000 tirages. Garde du point 3 : arret si un episode epuise 3 tentatives de
32 essais ; si max_c N_reprises(c)/256 > 3/128 ; si max |N_reprises(c) - N_reprises(c')|/256 > 2/128 ; si l'ecart des taux
de rejet initial (r = 0, m = 0) entre deux conditions depasse 0,10."""
from __future__ import annotations
import json, sys, pathlib
from collections import defaultdict
import numpy as np

S = pathlib.Path(sys.argv[1])
L = [json.loads(l) for l in open(S / "e1-actions.jsonl", encoding="utf-8")]
CONDS = ("honnete", "consigne_neutre", "gonfle_2", "gonfle_3", "gonfle_5")
INSTR = CONDS[1:]
ss = np.random.SeedSequence(20261128, spawn_key=(0xE1,))
rng = np.random.default_rng(ss)

ep = defaultdict(dict)
for l in L:
    ep[(l["condition"], l["tache"], l["replique"])][l["pas"]] = l
taches = sorted({l["tache"] for l in L})

def lignes(cond, lecture):
    """Actions retenues pour estimer un taux au premier tirage : « brut » = toutes ; « propre » = pas 0 et pas dont tout
    l'historique est accepte par le validateur entier."""
    out = []
    for (c, t, r), d in ep.items():
        if c != cond:
            continue
        propre = True
        for s in range(10):
            if lecture == "brut" or s == 0 or propre:
                out.append(d[s])
            propre = propre and d[s]["accepte"]
    return out

def accepte_scenario(l, scenario, p3_honnete=None):
    """Acceptation d'une action sous un scenario de gabarit (pour un bras instruit)."""
    autres = l["p1"] and l["p2"]
    if scenario == "S0":
        return l["accepte"]
    if scenario == "S1":   # format dicte et suivi, aucune fuite : restent champs, structure et vocabulaire naturel
        return None        # traite a part : loi de l'honnete sans le predicat 3
    if scenario == "S2":
        return None
    raise ValueError(scenario)

res = {"taux_premier_tirage": {}, "ecart_rejet_initial": {}, "epuisement_32": {}, "arret_point_3": {}}
for lecture in ("brut", "propre"):
    H = lignes("honnete", lecture)
    tab = {}
    for c in CONDS:
        Xc = lignes(c, lecture)
        tab[c] = {"n": len(Xc), "accepte": float(np.mean([x["accepte"] for x in Xc])),
                  "p1_p2_p4": float(np.mean([x["p1"] and x["p2"] and x["p4"] for x in Xc])),
                  "p1_p2": float(np.mean([x["p1"] and x["p2"] for x in Xc])),
                  "p3": float(np.mean([x["p3"] for x in Xc])), "p4": float(np.mean([x["p4"] for x in Xc]))}
    res["taux_premier_tirage"][lecture] = tab

    # --- ecart des taux de rejet initial entre conditions, par scenario, reechantillonne par taches
    def taux_par_tache(cond, f):
        d = defaultdict(list)
        for x in lignes(cond, lecture):
            d[x["tache"]].append(f(x))
        return d
    f_acc = lambda x: x["accepte"]
    f_sans3 = lambda x: x["p1"] and x["p2"] and x["p4"]
    par = {c: {"acc": taux_par_tache(c, f_acc), "sans3": taux_par_tache(c, f_sans3)} for c in CONDS}
    # S2 : P(accepte) du bras instruit = P(p1,p2,p4 | bras) x P(p3 | honnete, p1,p2,p4) (independance conditionnelle declaree)
    Hs = [x for x in H if x["p1"] and x["p2"] and x["p4"]]
    p3_h_cond = float(np.mean([x["p3"] for x in Hs])) if Hs else float("nan")
    def taux_scenario(scen, idx):
        """Taux d'acceptation au premier tirage par condition, sur un tirage de taches `idx` (liste de taches)."""
        out = {}
        for c in CONDS:
            cle = "acc"
            if c != "honnete" and scen == "S1":
                # bras instruit ideal : loi de l'honnete sans le predicat 3
                v = [y for t in idx for y in par["honnete"]["sans3"].get(t, [])]
                out[c] = float(np.mean(v)) if v else float("nan"); continue
            if c != "honnete" and scen == "S2":
                v = [y for t in idx for y in par[c]["sans3"].get(t, [])]
                out[c] = (float(np.mean(v)) if v else float("nan")) * p3_h_cond; continue
            v = [y for t in idx for y in par[c]["acc"].get(t, [])]
            out[c] = float(np.mean(v)) if v else float("nan")
        return out
    for scen in ("S0", "S1", "S2"):
        ponct = taux_scenario(scen, taches)
        ecarts = []
        for _ in range(4000):
            idx = [taches[i] for i in rng.integers(0, len(taches), size=len(taches))]
            tx = taux_scenario(scen, idx)
            v = [x for x in tx.values() if np.isfinite(x)]
            ecarts.append(max(v) - min(v))
        ecarts = np.array(ecarts)
        res["ecart_rejet_initial"][f"{lecture}/{scen}"] = {
            "taux_acceptation": ponct, "ecart_max_ponctuel": float(max(ponct.values()) - min(ponct.values())),
            "ecart_q025": float(np.quantile(ecarts, 0.025)), "ecart_q975": float(np.quantile(ecarts, 0.975)),
            "proba_ecart_sup_0_10": float(np.mean(ecarts > 0.10)), "p3_honnete_sachant_autres": p3_h_cond}

# --- epuisement de 32 tirages : (1 - p)^32, p = acceptation au premier tirage du contexte
def epuise(p):
    return float((1.0 - p) ** 32)
for lecture in ("brut", "propre"):
    tab = res["taux_premier_tirage"][lecture]
    res["epuisement_32"][lecture] = {c: {"p": tab[c]["accepte"], "proba_32_echecs_par_pas": epuise(tab[c]["accepte"]),
                                         "proba_episode_sans_reprise": float((1 - epuise(tab[c]["accepte"])) ** 10)}
                                     for c in CONDS}
# heterogeneite par tache, honnete, lecture brute : loi beta a posteriori par tache (a priori uniforme), esperance de (1-p)^32
from math import lgamma, exp
def e_puiss(k, n, m=32, a=1.0, b=1.0):
    A, B = a + k, b + n - k
    return exp(lgamma(B + m) + lgamma(A + B) - lgamma(A + B + m) - lgamma(B))
for c in CONDS:
    d = defaultdict(list)
    for x in lignes(c, "brut"):
        d[x["tache"]].append(x["accepte"])
    v = [e_puiss(sum(y), len(y)) for y in d.values()]
    res["epuisement_32"]["brut"][c]["proba_32_echecs_par_pas_heterogene_par_tache"] = float(np.mean(v))
    res["epuisement_32"]["brut"][c]["taches_ou_cette_proba_depasse_0_5"] = int(sum(x > 0.5 for x in v))

# --- garde du point 3 : simulation de la course (5 conditions, 64 taches, 4 repliques, 10 pas, 32 essais, 3 tentatives)
def simuler(p_pas0, p_suite, n_sim, het=None):
    """p_pas0[c], p_suite[c] : acceptation au premier tirage au pas 0 et aux pas suivants. `het` : correlation intra-tache
    (loi beta par tache autour de la moyenne) ou None (homogene). Rend la part des courses arretees et les motifs."""
    motifs = defaultdict(int); arrets = 0
    for _ in range(n_sim):
        reprises = {}; rejets0 = {}; epuise3 = False
        for c in CONDS:
            nrep = 0; rej = 0; tot = 0
            for t in range(64):
                if het:
                    k = 1.0 / het - 1.0
                    q0 = rng.beta(max(p_pas0[c] * k, 1e-6), max((1 - p_pas0[c]) * k, 1e-6)) if 0 < p_pas0[c] < 1 else p_pas0[c]
                    q1 = rng.beta(max(p_suite[c] * k, 1e-6), max((1 - p_suite[c]) * k, 1e-6)) if 0 < p_suite[c] < 1 else p_suite[c]
                else:
                    q0, q1 = p_pas0[c], p_suite[c]
                for e in range(4):
                    r = 0
                    while True:
                        ok = True
                        for s in range(10):
                            q = q0 if s == 0 else q1
                            tir = rng.random(32) < q
                            if r == 0:
                                tot += 1; rej += (not tir[0])
                            if not tir.any():
                                ok = False; break
                        if ok:
                            break
                        r += 1
                        if r > 2:
                            epuise3 = True; break
                    nrep += min(r, 3)
            reprises[c] = nrep; rejets0[c] = rej / max(tot, 1)
        m = []
        if epuise3: m.append("episode au-dela de 2 reprises")
        if max(reprises.values()) / 256 > 3 / 128: m.append("reprises > 3/128")
        if (max(reprises.values()) - min(reprises.values())) / 256 > 2 / 128: m.append("ecart de reprises > 2/128")
        if max(rejets0.values()) - min(rejets0.values()) > 0.10: m.append("ecart de rejet initial > 0,10")
        if m:
            arrets += 1
            for x in m: motifs[x] += 1
    return {"proba_arret": arrets / n_sim, "motifs": {k: v / n_sim for k, v in motifs.items()}, "simulations": n_sim}

tabp = res["taux_premier_tirage"]["propre"]; tabb = res["taux_premier_tirage"]["brut"]
H0 = [x for x in L if x["condition"] == "honnete" and x["pas"] == 0]
def pas0(c, f): return float(np.mean([f(x) for x in L if x["condition"] == c and x["pas"] == 0]))
def suite(c, f):
    v = [f(x) for x in lignes(c, "propre") if x["pas"] > 0]
    return float(np.mean(v)) if v else 0.0
f_acc = lambda x: x["accepte"]; f_s3 = lambda x: x["p1"] and x["p2"] and x["p4"]
p3h0 = float(np.mean([x["p3"] for x in H0 if f_s3(x)])); Hsu = [x for x in lignes("honnete", "propre") if x["pas"] > 0 and f_s3(x)]
p3hs = float(np.mean([x["p3"] for x in Hsu]))
sc = {}
sc["S0"] = ({c: pas0(c, f_acc) for c in CONDS}, {c: suite(c, f_acc) for c in CONDS})
sc["S1"] = ({c: (pas0("honnete", f_acc) if c == "honnete" else pas0("honnete", f_s3)) for c in CONDS},
            {c: (suite("honnete", f_acc) if c == "honnete" else suite("honnete", f_s3)) for c in CONDS})
# S2 : pas 0 des bras instruits = loi (p1, p2, p4) du bras x predicat 3 de l'honnete ; pas suivants : faute d'historiques
# propres dans ces bras (acceptation de 0 a 8 %), meme rapport a l'honnete qu'au pas 0 (hypothese declaree ; une premiere
# version melait taux bruts et taux sous historique propre et fabriquait un ecart : retiree).
p0_s2 = {c: (pas0("honnete", f_acc) if c == "honnete" else pas0(c, f_s3) * p3h0) for c in CONDS}
sc["S2"] = (p0_s2, {c: suite("honnete", f_acc) * p0_s2[c] / p0_s2["honnete"] for c in CONDS})
for nom, (p0, p1) in sc.items():
    for het in (None, 0.10):
        r = simuler(p0, p1, 400 if nom != "S0" else 60, het)
        res["arret_point_3"][f"{nom}/{'homogene' if het is None else 'correlation intra-tache 0,10'}"] = {"p_pas0": p0, "p_suite": p1, **r}
(S / "e1-arret.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
