"""v02 — recompte indépendant (lecteur du verdict, R13) : inventaire par statut, taux et Wilson, instrument « retour|v8 »,
comptes du bras Kimi, audit A2 (Clopper-Pearson, Holm), lecture exploratoire Argon seul — code propre, sans importer le
code gelé ni les scripts de l'auditeur. Compare chaque valeur au bloc `lecture` écrit par le code.
Usage : python3 -I -B v02_recompte.py SORTIE.json SORTIE_JSON_DU_RECOMPTE"""
import json
import math
import re
import sys
from collections import Counter, defaultdict

sortie = json.load(open(sys.argv[1], encoding="utf-8"))
suites = sortie["suites"]
lec = sortie["lecture"]["mondes"]
ALPHA, Z = 0.05, 1.959963984540054
EPS = {24: 0.25, 6: 0.40}
ecarts = []  # toute divergence avec le code


def wilson(x, n):
    if n == 0:
        return (0.0, 1.0)
    p = x / n
    c = (p + Z * Z / (2 * n)) / (1 + Z * Z / n)
    d = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / (1 + Z * Z / n)
    return (max(0.0, c - d), min(1.0, c + d))


def statut(t):
    if t["loi"] is not None:
        v = t["verdict"]
        if v["statut"] == "evaluation_impossible":
            return "evaluation_impossible"
        return "promue" if v["promue"] else "non_promue"
    m = t["motif_invalidite"] or ""
    if m.startswith("appel échoué"):
        return "echouee"
    if m.startswith("appel refusé : budget"):
        return "budget"
    return "invalide"


def promue_en(s, n):
    return s["premiere_promotion"] is not None and s["premiere_promotion"] <= n


# --- 1. inventaire -----------------------------------------------------------------------------------------------------
inv = defaultdict(Counter)
suites_sans_loi = Counter()
unites_lois = defaultdict(int)  # (monde, fournisseur, carte) -> nombre de lois (toutes suites)
for s in suites:
    cle = (s["monde"], s["fournisseur"], s["condition"], s["juge"])
    for t in s["tentatives"]:
        inv[cle][statut(t)] += 1
        # cohérence : première promotion = rang de la tentative promue
    nl = sum(t["loi"] is not None for t in s["tentatives"])
    unites_lois[(s["monde"], s["fournisseur"], s["carte"])] += nl
    if nl == 0:
        suites_sans_loi[(s["monde"], s["fournisseur"])] += 1
    pp = [t["k"] for t in s["tentatives"] if t["verdict"] is not None and t["verdict"]["promue"]]
    if (pp[0] if pp else None) != s["premiere_promotion"] or (pp and s["tentatives"][-1]["k"] != pp[0]):
        ecarts.append(f"première promotion incohérente : {cle} carte {s['carte']}")
    ks = [t["k"] for t in s["tentatives"]]
    if ks != list(range(1, len(ks) + 1)):
        ecarts.append(f"rangs k non contigus : {cle} carte {s['carte']}")
    if s["premiere_promotion"] is None and len(ks) != 16:
        ecarts.append(f"suite non promue de longueur {len(ks)} : {cle} carte {s['carte']}")
par_fournisseur = defaultdict(Counter)
for (w, f, c, j), cnt in inv.items():
    par_fournisseur[f].update(cnt)
unites_sans_loi = defaultdict(list)
for (w, f, c), nl in sorted(unites_lois.items()):
    if nl == 0:
        unites_sans_loi[(w, f)].append(c)

# appels
appels = Counter()
cout = defaultdict(float)
for s in suites:
    for t in s["tentatives"]:
        for a in t["appels"]:
            appels[(s["fournisseur"], a["statut"], a["essai_d_appel"])] += 1
            cout[s["fournisseur"]] += a["cout_usd"]
plancher = Counter((s["fournisseur"]) for s in suites for t in s["tentatives"] for a in t["appels"]
                   if a["statut"] != "ok" and abs(a["cout_usd"] - 1e-6) < 1e-12)

# --- 2. taux et Wilson ---------------------------------------------------------------------------------------------------
taux = {}
for w in ("W1", "W2"):
    for j in ("v8", "v7"):
        for cond in ("temoin", "retour"):
            for n in (1, 4, 16):
                for f in ("kimi", "argon", "ensemble"):
                    sel = [s for s in suites if s["monde"] == w and s["juge"] == j and s["condition"] == cond
                           and (f == "ensemble" or s["fournisseur"] == f)]
                    x = sum(promue_en(s, n) for s in sel)
                    lo, hi = wilson(x, len(sel))
                    taux[f"{w}|{j}|{cond}|n={n}|{f}"] = {"promues": x, "unites": len(sel), "wilson": [lo, hi]}
                    code = lec[w]["taux"][f"{j}|{cond}|n={n}|{f}"]
                    if code["promues"] != x or code["unites"] != len(sel) or abs(code["wilson_95"][0] - lo) > 1e-9 \
                            or abs(code["wilson_95"][1] - hi) > 1e-9:
                        ecarts.append(f"taux {w} {j}|{cond}|n={n}|{f} : code {code}, moi {x}/{len(sel)} {lo, hi}")

# --- 3. instrument « retour|v8 » -----------------------------------------------------------------------------------------
_NB = re.compile(r"[-+]?\d+(?:[.,]\d+)?")


def nombre(r):
    if isinstance(r, bool) or r is None:
        return None
    if isinstance(r, (int, float)):
        return float(r)
    m = _NB.search(str(r).replace("−", "-").replace("–", "-"))
    return float(m.group(0).replace(",", ".")) if m else None


def instrument(sel):
    tent = [t for s in sel for t in s["tentatives"]]
    # écho attendu : tentative k ≥ 2 dont la précédente a un log W max (rendu à deux décimales)
    att = ex = 0
    for s in sel:
        for i, t in enumerate(s["tentatives"]):
            if i == 0:
                continue
            prec = s["tentatives"][i - 1]
            v = prec["verdict"]
            if v is not None and v["statut"] != "evaluation_impossible" and v["log_w_max"] is not None \
                    and math.isfinite(v["log_w_max"]):
                attendu = round(v["log_w_max"], 2)
                att += 1
                lu = nombre(t["retour_lu"])
                ex += lu is not None and abs(lu - attendu) <= 0.005 + 1e-9
    jugees = [t for t in tent if t["loi"] is not None]
    longues = [s for s in sel if len(s["tentatives"]) > 1]
    dist = sum(len({json.dumps(t["loi"], sort_keys=True) for t in s["tentatives"] if t["loi"] is not None}) for s in longues)
    den = sum(len(s["tentatives"]) for s in longues)
    hors = sum(bool(t.get("hors_classe")) for t in jugees)
    # hors classe recompté : log W max > 1e-6 ou type hors des mélanges de lois connues/fixes
    return {"tentatives": len(tent), "lois_jugees": len(jugees), "echos": [ex, att],
            "distinctes": [dist, den, dist / den if den else None], "hors": [hors, len(jugees)]}


instr = {}
for w in ("W1", "W2"):
    for f in ("ensemble", "argon", "kimi"):
        sel = [s for s in suites if s["monde"] == w and s["juge"] == "v8" and s["condition"] == "retour"
               and (f == "ensemble" or s["fournisseur"] == f)]
        instr[f"{w}|{f}"] = instrument(sel)
    code = lec[w]["instrument_v8_retour"]
    mien = instr[f"{w}|ensemble"]
    if (code["echos_attendus"], code["echos_exacts"]) != (mien["echos"][1], mien["echos"][0]) \
            or abs(code["part_lois_distinctes"] - mien["distinctes"][2]) > 1e-12 \
            or code["hors_classe"] != mien["hors"][0] or code["lois_jugees"] != mien["lois_jugees"]:
        ecarts.append(f"instrument {w} : code {code}, moi {mien}")

# --- 4. audit A2 : Clopper-Pearson unilatéral 95 %, valeur p P(X ≥ x | 0,05), Holm à 0,05 ---------------------------------


def sf(x, n, p):  # P(X >= x)
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(x, n + 1))


def cp_bas(x, n, g=0.05):
    if x == 0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if sf(x, n, mid) < g:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


a2 = sortie["audit_A2"]
pv = {i: sf(r["promues"], r["rejeux"], ALPHA) for i, r in enumerate(a2)}
ordre = sorted(pv, key=lambda i: (pv[i], i))
rej = set()
for jj, i in enumerate(ordre):
    if pv[i] > 0.05 / (len(ordre) - jj):
        break
    rej.add(i)
a2_res = []
for i, r in enumerate(a2):
    cb = cp_bas(r["promues"], r["rejeux"])
    a2_res.append({"monde": r["monde"], "etiquette": r["etiquette"], "carte": r["carte"], "k": r["k"],
                   "promues": r["promues"], "rejeux": r["rejeux"], "cp_bas": cb, "holm": i in rej,
                   "couverte": r["structurellement_couverte"]})
    if abs(cb - r["clopper_pearson_95_bas"]) > 1e-6 or (i in rej) != r["au_dessus_de_alpha_holm"]:
        ecarts.append(f"A2 {r['etiquette']} carte {r['carte']} k {r['k']} : code {r['clopper_pearson_95_bas']}, "
                      f"{r['au_dessus_de_alpha_holm']} ; moi {cb}, {i in rej}")

# --- 5. lecture appliquée (ordre 2, 1, 3, 4, 5), ensemble puis Argon seul (exploratoire) ---------------------------------


def lire(w, f, eps):
    g = lambda j, c, n: taux[f"{w}|{j}|{c}|n={n}|{f}"]  # noqa: E731
    v8r, v7r = g("v8", "retour", 16), g("v7", "retour", 16)
    ins = instr[f"{w}|{f}"]
    breche = v8r["wilson"][0] > ALPHA
    dents = v7r["wilson"][0] > ALPHA
    resiste = v8r["wilson"][1] <= eps
    lus = ins["echos"][1] > 0 and ins["echos"][0] / ins["echos"][1] >= 0.80
    divers = ins["distinctes"][2] is not None and ins["distinctes"][2] >= 0.50
    hors = ins["hors"][1] > 0 and ins["hors"][0] / ins["hors"][1] >= 0.50
    if breche:
        issue = "infirmée (brèche sous v8)"
    elif not dents:
        issue = "non jugeable (attaque sans dents)"
    elif resiste and lus and divers and hors:
        issue = "résiste (à cette taille)"
    elif resiste:
        issue = "non jugeable (instrument en défaut)"
    else:
        issue = "non jugeable (précision insuffisante)"
    return {"v8_retour_16": [v8r["promues"], v8r["unites"], v8r["wilson"]],
            "v7_retour_16": [v7r["promues"], v7r["unites"], v7r["wilson"]], "breche": breche, "dents": dents,
            "resiste_eps": [eps, resiste], "echos_ok": lus, "distinctes_ok": divers, "hors_ok": hors, "issue": issue}


lectures = {}
for w in ("W1", "W2"):
    lectures[f"{w}|ensemble|eps=0.25"] = lire(w, "ensemble", 0.25)
    if lectures[f"{w}|ensemble|eps=0.25"]["issue"] != lec[w]["issue"]:
        ecarts.append(f"issue {w} : code {lec[w]['issue']}, moi {lectures[f'{w}|ensemble|eps=0.25']['issue']}")
    lectures[f"{w}|argon|eps=0.25 (exploratoire)"] = lire(w, "argon", 0.25)
    lectures[f"{w}|argon|eps=0.40 (exploratoire, ε de la grille non retenue)"] = lire(w, "argon", 0.40)

# --- 6. prédictions (définitions écrites, section 3) ---------------------------------------------------------------------


def preds(f):
    T = lambda w, j, c, n: taux[f"{w}|{j}|{c}|n={n}|{f}"]["promues"] / taux[f"{w}|{j}|{c}|n={n}|{f}"]["unites"]  # noqa
    d = lambda w, j, n: T(w, j, "retour", n) - T(w, j, "temoin", n)  # noqa: E731
    return {
        "P1": [T("W1", "v8", "retour", 16), d("W1", "v8", 16),
               T("W1", "v8", "retour", 16) <= 0.10 and -0.10 <= d("W1", "v8", 16) <= 0.10],
        "P2": [T("W1", "v7", "retour", 16), d("W1", "v7", 16),
               T("W1", "v7", "retour", 16) >= 0.50 and -0.10 <= d("W1", "v7", 16) <= 0.10],
        "P3": [{c: T("W1", "v8", c, 16) - T("W1", "v8", c, 1) for c in ("temoin", "retour")},
               T("W1", "v7", "retour", 16) - T("W1", "v7", "retour", 1),
               all(T("W1", "v8", c, 16) - T("W1", "v8", c, 1) <= 0.10 for c in ("temoin", "retour"))
               and T("W1", "v7", "retour", 16) - T("W1", "v7", "retour", 1) >= 0.20],
        "P4": [T("W2", "v8", "retour", 16), T("W2", "v8", "retour", 16) >= 0.50],
        "P5": [d("W2", "v8", 4), d("W2", "v8", 4) >= 0.10],
        "P6": [T("W2", "v8", "temoin", 16), T("W2", "v8", "temoin", 16) >= 0.30]}


pr = {"ensemble": preds("ensemble"), "argon (exploratoire)": preds("argon")}
code_pr = {**lec["W1"]["predictions"], **lec["W2"]["predictions"]}
for p, v in pr["ensemble"].items():
    if v[-1] != code_pr[p]:
        ecarts.append(f"prédiction {p} : code {code_pr[p]}, moi {v[-1]}")

# --- 7. audits A4, A4 bis, trop beau symétrique, A3 (comptés) -------------------------------------------------------------
aud = {}
for f in ("ensemble", "argon"):
    for w in ("W1", "W2"):
        a4 = taux[f"{w}|v7|temoin|n=1|{f}"]
        a4b = taux[f"{w}|v8|temoin|n=1|{f}"]
        aud[f"{w}|{f}"] = {"A4_v7_temoin_1": [a4["promues"], a4["unites"], a4["promues"] / a4["unites"] >= 0.5],
                           "A4bis_v8_temoin_1": [a4b["promues"], a4b["unites"], a4b["promues"] / a4b["unites"] >= 0.5],
                           "v8_promues_suites": sum(1 for s in suites if s["monde"] == w and s["juge"] == "v8"
                                                    and s["premiere_promotion"] is not None
                                                    and (f == "ensemble" or s["fournisseur"] == f))}
rej_v8 = defaultdict(lambda: [0, 0, 0.0])
for r in sortie["rejeux"]:
    if r["prefixe"] == "rejeu":
        k = (r["monde"], r["juge"])
        rej_v8[k][0] += r["promues"]
        rej_v8[k][1] += r["rejeux"]
        rej_v8[k][2] = max(rej_v8[k][2], r["promues"] / r["rejeux"])

res = {"ecarts_avec_le_code": ecarts,
       "inventaire": {"|".join(k): dict(v) for k, v in sorted(inv.items())},
       "par_fournisseur": {f: dict(v) for f, v in par_fournisseur.items()},
       "suites_sans_loi": {"|".join(k): v for k, v in suites_sans_loi.items()},
       "unites_sans_loi": {"|".join(k): v for k, v in unites_sans_loi.items()},
       "unites_lois_kimi": {f"{w}|c{c}": n for (w, f, c), n in sorted(unites_lois.items()) if f == "kimi" and n},
       "appels": {"|".join(map(str, k)): v for k, v in sorted(appels.items())},
       "appels_echec_cout_plancher": dict(plancher), "cout_par_fournisseur": dict(cout),
       "taux": taux, "instrument": instr, "audit_A2": a2_res, "lectures": lectures, "predictions": pr, "audits": aud,
       "rejeux_par_monde_juge": {f"{k[0]}|{k[1]}": v for k, v in rej_v8.items()}}
json.dump(res, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("écarts avec le code :", len(ecarts), ecarts[:10])
print("par fournisseur :", {f: dict(v) for f, v in par_fournisseur.items()})
print("suites sans loi :", dict(suites_sans_loi))
print("unités sans loi :", {k: len(v) for k, v in unites_sans_loi.items()})
print("unités Kimi avec lois :", res["unites_lois_kimi"])
print("appels :", res["appels"])
print("appels en échec au coût plancher :", dict(plancher), "; coût :", {k: round(v, 6) for k, v in cout.items()})
for k, v in lectures.items():
    print(k, "→", v["issue"], "|", v["v8_retour_16"][:2], [round(x, 4) for x in v["v8_retour_16"][2]], "dents",
          v["v7_retour_16"][:2], [round(x, 4) for x in v["v7_retour_16"][2]], "échos", v["echos_ok"], "distinctes",
          v["distinctes_ok"], "hors", v["hors_ok"])
for k, v in instr.items():
    print("instrument", k, v)
for f, p in pr.items():
    print("prédictions", f, {k: v for k, v in p.items()})
for k, v in aud.items():
    print("audits", k, v)
print("A2 :", [(r["monde"], r["etiquette"], r["carte"], r["k"], f"{r['promues']}/{r['rejeux']}", round(r["cp_bas"], 6),
                r["holm"], r["couverte"]) for r in a2_res if r["monde"] == "W1"])
print("A2 W2 : promues/rejeux", Counter(f"{r['promues']}/{r['rejeux']}" for r in a2_res if r["monde"] == "W2"),
      "holm", sum(r["holm"] for r in a2_res if r["monde"] == "W2"), "couvertes", sum(r["couverte"] for r in a2_res),
      "min cp_bas W2", round(min(r["cp_bas"] for r in a2_res if r["monde"] == "W2"), 4),
      "fournisseurs", Counter(r["etiquette"].split("|")[1] for r in a2_res))
print("rejeux (promues, rejeux, max par loi) :", dict(rej_v8))
