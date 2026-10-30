"""Tableaux du rapport v9, lus dans les sorties des passages v8 (dossier v8, lecture seule) et v9 (aucun chiffre recopié à la main). Écrit `tableaux-v9.md`,
`tableaux-v9-sortie.json` (mêmes nombres, non arrondis) et son manifeste (GD8-09).

Mesures (comme la v8) : « seuil 40 » = `ebh_A.retenues_fiches_du_sujet` (lecture (A), m = 2) ; « seuil 160 » = `160.0.fiche_entiere.part` (atteinte de 8/α_c par le
minimum des 16 processus ; borne basse de la retenue à m = 8, non simulée). « Pire » = au pire des quatre cellules K_h ∈ {10 ; 5} × biais ∈ {0 ; δ/4}.

Ce qui est nouveau en v9 :
- GD8-01 : grille prolongée (ρ_A = ρ_B : 0 ; 0,05 ; 0,10 ; 0,125 ; 0,17 ; 0,20 ; 0,25 ; 0,30 ; 0,35 ; ρ_A = 2 ρ_B : ρ_B = 0 ; 0,025 ; 0,05 ; 0,085 ; 0,10 ;
  0,125 ; 0,17 ; 0,20 si passé) ; table « au ρ vrai » (n80 → n_h, règle v8 inchangée : n_h = max(288 ; plus petit multiple de 16 ≥ 1,06 × n80 pire), enveloppe
  croissante par hypothèse) ; table **en ρ̂ lu** pour N ∈ {50 ; 100 ; 288} unités de pilote : ρ_haut = ρ̂ + 1,645 × σ(ρ̂), σ lu dans
  `precision-rho-pilote-v9-sortie.json` (côté sabotage, p = 0,4) au plus petit ρ de sa grille ≥ max(ρ̂ ; 0) (0,40 au-delà) ; dans chaque hypothèse, la ligne
  égale ou immédiatement supérieure à ρ_haut ; n_h = le plus grand des deux ; si l'une des deux hypothèses n'a pas de ligne : « hors table » (repli : rapport).
  ρ̂ < 0 est lu comme 0.
- GD8-02 : neuvième comparateur rapporté en n_h à neuf comparateurs et en écart des n_h (règle de n_h sans enveloppe, ligne par ligne).
- GD8-04 : n80 et n90 par ajustement logistique binomial des points évalués par la dichotomie (logit P = a + b·n, points de puissance dans [0,5 ; 0,99],
  poids 2 000, écart-type par la méthode delta, multiplié par √(déviance/ddl) si > 1 ; méthode de `ajustement-n80-gd8-v1.py`) ; puissances clés en moyenne sur
  graines (graine 20261029 de la v8 et graines 11 à 18 de la v9) avec erreur type.
- GD8-07 : passages ρ honnête = 2 × ρ saboté contre les passages v8 au même ρ saboté.
- GD8-03 : parts de variance et corrélations des strates (lues dans les `moments_tires` des passages v8 de strates).
Usage : python3 -I -B tableaux-v9.py COMMIT DOSSIER_V8 DOSSIER_V9 SORTIE.md SORTIE.json
"""
import hashlib
import json
import math
import os
import platform
import re
import sys
from datetime import datetime, timezone

import numpy as np

COMMIT, D8, D9, SORTIE_MD, SORTIE_JSON = sys.argv[1:6]
debut = datetime.now(timezone.utc)
P8, P9 = "simulation-puissance-garde-delta-v8-sortie-", "simulation-puissance-garde-delta-v9-sortie-"
BIAIS = (0.0, 0.0125)
TAILLES = (288, 400, 500, 650)
MARGE, REPS = 1.06, 2000
S, EMP = {}, {}
for D, P in ((D8, P8), (D9, P9)):
    for f in sorted(os.listdir(D)):
        if f.startswith(P) and f.endswith(".json"):
            nom = f[len(P):-5]
            assert nom not in S, nom
            EMP[f] = hashlib.sha256(open(os.path.join(D, f), "rb").read()).hexdigest()
            S[nom] = json.load(open(os.path.join(D, f), encoding="utf-8"))
            assert S[nom]["reglages"]["repetitions"] == 2000, nom

f3 = lambda x: f"{x:.3f}".replace(".", ",")  # v9 (GD8-04) : arrondi au plus proche ; ni tronqué ni minorant
f4 = lambda x: f"{x:.4f}".replace(".", ",")
f1 = lambda x: f"{x:.1f}".replace(".", ",")


def rtxt(x):
    return f"{x:.3f}".rstrip("0").rstrip(".").replace(".", ",") if x else "0"


IDX = {}
for p, sortie in S.items():
    for et, c in sortie["cellules"].items():
        m = re.search(r"_Kh(\d+)_Ks(\d+)_", "_" + et)
        IDX[(p, int(m.group(1)), int(m.group(2)), int(re.search(r"\|n=(\d+)\|", et).group(1)), float(re.search(r"biais=([0-9.]+)", et).group(1)),
             int(re.search(r"\|k=(\d+)$", et).group(1)))] = c


def cell(p, K_h, n, b, k=8):
    return IDX.get((p, K_h, 10, n, b, k))


fiche40 = lambda c: c["ebh_A"]["retenues_fiches_du_sujet"]
fiche160 = lambda c: c["160.0"]["fiche_entiere"]["part"]


def bloc_n80(p, K_h, b, k=8):
    for nm, loi in S[p]["lois"].items():
        m = re.search(r"Kh(\d+)_Ks(\d+)_", nm)
        if int(m.group(1)) == K_h and int(m.group(2)) == 10 and "n_pour_puissance_0_8_fiche" in loi:
            return loi["n_pour_puissance_0_8_fiche"].get(f"delta=0.05|biais={b}|k={k}")
    return None


def dicho(p, K_h, b, mesure, cible="n80", k=8):
    v = bloc_n80(p, K_h, b, k)
    if v is None or cible not in v:
        return None
    return v[cible][mesure]["n_approx"]


LOGIT = lambda q: math.log(q / (1 - q))


def ajuster(pts, cibles=(0.8, 0.9)):
    pts = [(n, q) for n, q in pts if 0.5 <= q <= 0.99]
    if len(pts) < 3:
        return None
    n = np.array([x for x, _ in pts], dtype=float)
    y = np.array([q for _, q in pts], dtype=float)
    X = np.column_stack([np.ones_like(n), n])
    beta = np.zeros(2)
    for _ in range(200):
        mu = 1 / (1 + np.exp(-(X @ beta)))
        W = REPS * mu * (1 - mu)
        z = X @ beta + (y - mu) / (mu * (1 - mu))
        nouveau = np.linalg.solve(X.T @ (W[:, None] * X), X.T @ (W * z))
        fini = np.max(np.abs(nouveau - beta)) < 1e-12
        beta = nouveau
        if fini:
            break
    mu = 1 / (1 + np.exp(-(X @ beta)))
    cov = np.linalg.inv(X.T @ ((REPS * mu * (1 - mu))[:, None] * X))
    with np.errstate(divide="ignore", invalid="ignore"):
        dev = 2 * REPS * np.sum(np.where(y > 0, y * np.log(y / mu), 0) + np.where(y < 1, (1 - y) * np.log((1 - y) / (1 - mu)), 0))
    ddl = len(y) - 2
    dpd = float(dev / ddl) if ddl > 0 else None
    res = {"points": len(y), "deviance_par_ddl": dpd}
    for c in cibles:
        a, b = beta
        nc = (LOGIT(c) - a) / b
        g = np.array([-1 / b, -(LOGIT(c) - a) / b ** 2])
        sd = math.sqrt(float(g @ cov @ g)) * math.sqrt(max(1.0, dpd or 1.0))
        res[f"n{int(round(100 * c))}"] = [float(nc), sd]
    return res


def ajuste(p, K_h, b, mesure, k=8):
    v = bloc_n80(p, K_h, b, k)
    if v is None:
        return None
    return ajuster(sorted((int(n), q[mesure]) for n, q in v["points_evalues"].items()))


res = {"empreintes_sorties": EMP, "precision_rho": None}
md = []


def pire(p, mesure, cible="n80", k=8):
    vals = [dicho(p, K_h, b, mesure, cible, k) for K_h in (10, 5) for b in BIAIS]
    return None if any(v is None for v in vals) else max(vals)


def pire_ajuste(p, mesure, cible="n80", k=8):
    best = None
    for K_h in (10, 5):
        for b in BIAIS:
            a = ajuste(p, K_h, b, mesure, k)
            if a is None:
                return None
            if best is None or a[cible][0] > best[0][0]:
                best = (a[cible], K_h, b, a["deviance_par_ddl"])
    return {"estime": best[0][0], "ecart_type": best[0][1], "cellule": f"K_h={best[1]}|biais={best[2]}", "deviance_par_ddl": best[3]}


def nh_brut(n80):
    return None if n80 is None else max(288, 16 * math.ceil(MARGE * n80 / 16))


def fiche_pire(p, n, fn, k=8):
    cs = [cell(p, K_h, n, b, k) for K_h in (10, 5) for b in BIAIS]
    return None if any(c is None for c in cs) else min(fn(c) for c in cs)


# ------------------------------------------------------------------ GD8-01 : table au ρ vrai
HYP = (("ρ_A = ρ_B", [("rho0", 0.0), ("meme-rho0.05", 0.05), ("meme-rho0.10", 0.10), ("meme-rho0.125", 0.125), ("meme-rho0.17", 0.17), ("meme-rho0.20", 0.20),
                      ("meme-rho0.25", 0.25), ("meme-rho0.30", 0.30), ("meme-rho0.35", 0.35)]),
       ("ρ_A = 2 ρ_B", [("rho0", 0.0), ("moitie-rho0.05", 0.025), ("moitie-rho0.10", 0.05), ("moitie-rho0.17", 0.085), ("double-rhoB0.10", 0.10),
                        ("double-rhoB0.125", 0.125), ("double-rhoB0.17", 0.17), ("double-rhoB0.20", 0.20)]))
md.append("## T1. Table au ρ vrai (GD8-01) : ρ_B vrai → n80, n90 (pire des quatre cellules), n80 ajusté (GD8-04), n_h\n")
md.append("Source : passages v8 (`rho0`, `meme-…`, `moitie-…`) et v9 (`meme-rho0.125`, `-0.20`, `-0.30`, `-0.35`, `double-rhoB…`) ; n80 par dichotomie (borne haute du dernier pas) "
          "et par ajustement logistique (± écart-type) ; n_h = max(288 ; multiple de 16 ≥ 1,06 × n80 dichotomie pire), enveloppe croissante par hypothèse ; fiche pire à 288 et 400 unités\n")
md.append("| hypothèse | ρ_B | ρ_A | passage | fiche 288 (40) | fiche 288 (160) | fiche 400 (40) | fiche 400 (160) | n80 40 | n80 40 ajusté | n80 160 | n80 160 ajusté | n90 40 | n90 160 | n_h 40 | n_h 160 | n_h depuis n80 ajusté (40 / 160, sans enveloppe) |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
table_vrai = []
for hyp, lignes in HYP:
    env = {"40": 0, "160": 0}
    for p, rb in lignes:
        if p not in S:
            table_vrai.append({"hypothese": hyp, "rho_B": rb, "passage": p, "absent": True})
            md.append(f"| {hyp} | {rtxt(rb)} | — | `{p}` | absent (non fini) | | | | | | | | | | | | |")
            continue
        ra = S[p]["reglages"]["effet_unite_beta"]
        a40, a160 = pire(p, "retenue_ebh"), pire(p, "atteinte_160")
        n90_40, n90_160 = pire(p, "retenue_ebh", "n90"), pire(p, "atteinte_160", "n90")
        j40, j160 = pire_ajuste(p, "retenue_ebh"), pire_ajuste(p, "atteinte_160")
        nh = {}
        for s_, a in (("40", a40), ("160", a160)):
            b_ = nh_brut(a)
            if b_ is None:
                nh[s_] = None
            else:
                env[s_] = max(env[s_], b_)
                nh[s_] = env[s_]
        fv = [fiche_pire(p, n, fn) for n in (288, 400) for fn in (fiche40, fiche160)]
        l = {"hypothese": hyp, "rho_B": rb, "rho_A": ra, "passage": p, "fiche_pire_288_40": fv[0], "fiche_pire_288_160": fv[1], "fiche_pire_400_40": fv[2],
             "fiche_pire_400_160": fv[3], "n80_40": a40, "n80_160": a160, "n90_40": n90_40, "n90_160": n90_160, "n80_40_ajuste": j40, "n80_160_ajuste": j160,
             "n_h_40": nh["40"], "n_h_160": nh["160"], "n_h_40_sans_enveloppe": nh_brut(a40), "n_h_160_sans_enveloppe": nh_brut(a160),
             "n_h_40_depuis_ajuste": nh_brut(j40["estime"]) if j40 else None, "n_h_160_depuis_ajuste": nh_brut(j160["estime"]) if j160 else None}
        table_vrai.append(l)
        aj = lambda j: "—" if j is None else f"{f1(j['estime'])} ± {f1(j['ecart_type'])}"
        md.append(f"| {hyp} | {rtxt(rb)} | {rtxt(ra)} | `{p}` | " + " | ".join("—" if x is None else f3(x) for x in fv)
                  + f" | {a40} | {aj(j40)} | {a160} | {aj(j160)} | {n90_40} | {n90_160} | {nh['40']} | {nh['160']} | {l['n_h_40_depuis_ajuste']} / {l['n_h_160_depuis_ajuste']} |")
res["table_rho_vrai"] = table_vrai
md.append("")

# ------------------------------------------------------------------ GD8-01 : table en ρ̂ lu
PREC = json.load(open(os.path.join(D9, "precision-rho-pilote-v9-sortie.json"), encoding="utf-8"))
res["precision_rho"] = {"fichier": "precision-rho-pilote-v9-sortie.json",
                        "sha256": hashlib.sha256(open(os.path.join(D9, "precision-rho-pilote-v9-sortie.json"), "rb").read()).hexdigest()}
GRILLE_SD = sorted({c["rho"] for c in PREC["cellules"] if c["p"] == 0.4})


def sd(rh, N):
    r = next((g for g in GRILLE_SD if g >= max(rh, 0.0) - 1e-12), GRILLE_SD[-1])
    return [c for c in PREC["cellules"] if c["p"] == 0.4 and c["rho"] == r and c["N"] == N][0]["ecart_type"], r


def ligne(hyp, haut):
    ls = sorted([l for l in table_vrai if l["hypothese"] == hyp and not l.get("absent") and l["n_h_40"] is not None and l["n_h_160"] is not None],
                key=lambda l: l["rho_B"])
    return next((l for l in ls if l["rho_B"] >= haut - 1e-12), None)


lectures = []
for N in (50, 100, 288):
    for i in range(0, 41):
        rh = round(i / 100, 3)
        for rh_ in ([rh] + ([0.125] if i == 12 else [])):
            s_, rs = sd(rh_, N)
            haut = max(rh_, 0.0) + 1.645 * s_
            l1, l2 = ligne("ρ_A = ρ_B", haut), ligne("ρ_A = 2 ρ_B", haut)
            x = {"N_pilote": N, "rho_chapeau": rh_, "ecart_type_lu": s_, "rho_de_l_ecart_type": rs, "rho_haut": haut,
                 "ligne_hyp1": None if l1 is None else l1["rho_B"], "ligne_hyp2": None if l2 is None else l2["rho_B"],
                 "n_h_40_hyp1": None if l1 is None else l1["n_h_40"], "n_h_160_hyp1": None if l1 is None else l1["n_h_160"],
                 "n_h_40_hyp2": None if l2 is None else l2["n_h_40"], "n_h_160_hyp2": None if l2 is None else l2["n_h_160"]}
            x["n_h_40"] = None if (l1 is None or l2 is None) else max(l1["n_h_40"], l2["n_h_40"])
            x["n_h_160"] = None if (l1 is None or l2 is None) else max(l1["n_h_160"], l2["n_h_160"])
            x["hors_table"] = x["n_h_40"] is None
            lectures.append(x)
res["table_rho_chapeau"] = lectures


def intervalles(N, cle):
    """Regroupe les ρ̂ de la grille au pas de 0,01 (sans la ligne 0,125) en intervalles de même réponse."""
    L = [x for x in lectures if x["N_pilote"] == N and abs(x["rho_chapeau"] * 100 - round(x["rho_chapeau"] * 100)) < 1e-9]
    out, cur = [], None
    for x in L:
        rep = (x["n_h_40"], x["n_h_160"]) if cle == "les deux" else ((x["n_h_40_hyp1"], x["n_h_160_hyp1"]) if cle == "hyp1" else (x["n_h_40_hyp2"], x["n_h_160_hyp2"]))
        if cur and cur["reponse"] == rep:
            cur["fin"] = x["rho_chapeau"]
        else:
            cur = {"debut": x["rho_chapeau"], "fin": x["rho_chapeau"], "reponse": rep}
            out.append(cur)
    return out


res["intervalles"] = {}
for N in (50, 100, 288):
    for cle in ("les deux", "hyp1", "hyp2"):
        res["intervalles"][f"N={N}|{cle}"] = intervalles(N, cle)
md.append("## T2. Table en ρ̂ lu au pilote (GD8-01) : ρ̂ (côté sabotage) → n_h, marge 1,645 × écart-type de lecture incluse\n")
md.append("Règle : ρ_haut = max(ρ̂ ; 0) + 1,645 × σ(ρ̂) (σ de `precision-rho-pilote-v9-sortie.json`, p = 0,4, K = 10, au plus petit ρ de la grille ≥ ρ̂) ; dans chaque hypothèse la ligne "
          "de T1 égale ou immédiatement supérieure à ρ_haut ; n_h = le plus grand des deux ; « hors table » si l'une n'a pas de ligne. ρ̂ par pas de 0,01 de 0 à 0,40 (plus 0,125).\n")
for N in (50, 100, 288):
    md.append(f"#### T2-{N}. Pilote de {N} unités — intervalles de ρ̂ (pas 0,01) de même réponse (les deux hypothèses ; puis ρ_A = ρ_B seule)\n")
    md.append("| ρ̂ de | à | n_h seuil 40 | n_h seuil 160 | | ρ̂ de (ρ_A = ρ_B seule) | à | n_h 40 | n_h 160 |")
    md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    A, B = res["intervalles"][f"N={N}|les deux"], res["intervalles"][f"N={N}|hyp1"]
    for i in range(max(len(A), len(B))):
        a = A[i] if i < len(A) else None
        b = B[i] if i < len(B) else None
        ca = ["", "", "", ""] if a is None else [f"{a['debut']:.2f}".replace(".", ","), f"{a['fin']:.2f}".replace(".", ","),
                                                  "hors table" if a["reponse"][0] is None else str(a["reponse"][0]), "hors table" if a["reponse"][1] is None else str(a["reponse"][1])]
        cb = ["", "", "", ""] if b is None else [f"{b['debut']:.2f}".replace(".", ","), f"{b['fin']:.2f}".replace(".", ","),
                                                  "hors table" if b["reponse"][0] is None else str(b["reponse"][0]), "hors table" if b["reponse"][1] is None else str(b["reponse"][1])]
        md.append("| " + " | ".join(ca) + " | | " + " | ".join(cb) + " |")
    md.append("")
md.append("#### T2-points. Lectures ponctuelles (ρ̂ = 0 ; 0,05 ; 0,10 ; 0,125 ; 0,17 ; 0,20 ; 0,25)\n")
md.append("| N pilote | ρ̂ | σ lu | ρ_haut | ligne ρ_A = ρ_B | ligne ρ_A = 2 ρ_B | n_h 40 (hyp. 1 / hyp. 2) | n_h 160 (hyp. 1 / hyp. 2) | n_h 40 | n_h 160 |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for x in lectures:
    if x["rho_chapeau"] in (0.0, 0.05, 0.10, 0.125, 0.17, 0.20, 0.25):
        t = lambda v: "—" if v is None else str(v)
        md.append(f"| {x['N_pilote']} | {rtxt(x['rho_chapeau'])} | {f4(x['ecart_type_lu'])} | {f4(x['rho_haut'])} | {t(x['ligne_hyp1'])} | {t(x['ligne_hyp2'])} | "
                  f"{t(x['n_h_40_hyp1'])} / {t(x['n_h_40_hyp2'])} | {t(x['n_h_160_hyp1'])} / {t(x['n_h_160_hyp2'])} | {t(x['n_h_40']) if x['n_h_40'] else 'hors table'} | "
                  f"{t(x['n_h_160']) if x['n_h_160'] else 'hors table'} |")
md.append("")
res["premier_hors_table"] = {}
for N in (50, 100, 288):
    L = [x for x in lectures if x["N_pilote"] == N]
    res["premier_hors_table"][f"N={N}"] = {"les_deux": min((x["rho_chapeau"] for x in L if x["hors_table"]), default=None),
                                           "hyp1_seule": min((x["rho_chapeau"] for x in L if x["ligne_hyp1"] is None), default=None),
                                           "hyp2_seule": min((x["rho_chapeau"] for x in L if x["ligne_hyp2"] is None), default=None)}
md.append("Premier ρ̂ hors table : " + " ; ".join(f"N = {N} : {v['les_deux']} (les deux hypothèses), {v['hyp1_seule']} (ρ_A = ρ_B seule)"
                                                for N, v in ((k[2:], v) for k, v in res["premier_hors_table"].items())) + "\n")

# ------------------------------------------------------------------ repli : taille maximale de la grille
dern = {hyp: max((l for l in table_vrai if l["hypothese"] == hyp and not l.get("absent")), key=lambda l: l["rho_B"]) for hyp, _ in HYP}
res["taille_maximale_grille"] = {hyp: {"rho_B": l["rho_B"], "rho_A": l["rho_A"], "n_h_40": l["n_h_40"], "n_h_160": l["n_h_160"]} for hyp, l in dern.items()}

# ------------------------------------------------------------------ repli C : taille lue sous ρ_A = ρ_B, monde ρ_A = 2 ρ_B
def puissance_ajustee(p, mesure, n):
    """Puissance au pire des quatre cellules à la taille n, par la courbe logistique ajustée de chaque cellule (interpolation, aucun tirage)."""
    vals = []
    for K_h in (10, 5):
        for b in BIAIS:
            v = bloc_n80(p, K_h, b)
            pts = [(int(m), q[mesure]) for m, q in v["points_evalues"].items() if 0.5 <= q[mesure] <= 0.99]
            nn = np.array([x for x, _ in pts], float)
            yy = np.array([q for _, q in pts], float)
            X = np.column_stack([np.ones_like(nn), nn])
            beta = np.zeros(2)
            for _ in range(200):
                mu = 1 / (1 + np.exp(-(X @ beta)))
                W = REPS * mu * (1 - mu)
                nouveau = np.linalg.solve(X.T @ (W[:, None] * X), X.T @ (W * (X @ beta + (yy - mu) / (mu * (1 - mu)))))
                fini = np.max(np.abs(nouveau - beta)) < 1e-12
                beta = nouveau
                if fini:
                    break
            vals.append(float(1 / (1 + math.exp(-(beta[0] + beta[1] * n)))))
    return min(vals)


md.append("## T8. Repli C (restriction à ρ_A = ρ_B) : puissance, dans un monde ρ_A = 2 ρ_B, à la taille lue sous ρ_A = ρ_B (même ρ_B)\n")
md.append("Source : T1 ; puissance au pire des quatre cellules par les courbes logistiques ajustées sur les points de dichotomie du passage `double-…`/`moitie-…` (interpolation)\n")
md.append("| ρ_B | ρ_A du monde | n_h 40 lu sous ρ_A = ρ_B | puissance (40) à cette taille, monde ρ_A = 2 ρ_B | n_h 160 lu sous ρ_A = ρ_B | puissance (160) à cette taille |")
md.append("| --- | --- | --- | --- | --- | --- |")
res["repli_C"] = {}
for l2 in [l for l in table_vrai if l["hypothese"] == "ρ_A = 2 ρ_B" and not l.get("absent") and l["rho_B"] > 0]:
    l1 = next((l for l in table_vrai if l["hypothese"] == "ρ_A = ρ_B" and not l.get("absent") and l["rho_B"] >= l2["rho_B"] - 1e-12), None)
    if l1 is None:
        continue
    q40, q160 = puissance_ajustee(l2["passage"], "retenue_ebh", l1["n_h_40"]), puissance_ajustee(l2["passage"], "atteinte_160", l1["n_h_160"])
    res["repli_C"][str(l2["rho_B"])] = {"ligne_hyp1": l1["rho_B"], "n_h_40": l1["n_h_40"], "puissance_40": q40, "n_h_160": l1["n_h_160"], "puissance_160": q160}
    md.append(f"| {rtxt(l2['rho_B'])} | {rtxt(l2['rho_A'])} | {l1['n_h_40']} (ligne {rtxt(l1['rho_B'])}) | {f3(q40)} | {l1['n_h_160']} | {f3(q160)} |")
md.append("")

# ------------------------------------------------------------------ GD8-02 : neuvième comparateur en n_h
LOIS9 = [("nulle", "rho0", "nulle"), ("ρ_A = ρ_B = 0,05", "meme-rho0.05", "rho0.05"), ("bêta (σ de référence 1,0)", "neuf-k8-beta1.0", "beta1.0"),
         ("logit σ = 1,0", "neuf-k8-logit1.0", "logit1.0"), ("ρ_A = ρ_B = 0,10", "meme-rho0.10", "rho0.10"), ("ρ_A = ρ_B = 0,17", "meme-rho0.17", "rho0.17")]
md.append("## T3. Neuvième comparateur en n_h (GD8-02) : n_h à huit et à neuf comparateurs, écart des n_h\n")
md.append("Source : passages v8 `rho0`, `meme-…`, `neuf-k8-…`, `neuf-k9-g0.05-…` (écart du neuvième 0,05 : SUPPOSÉ, « comparateur fort » ; côté honnête du neuvième inchangé : SUPPOSÉ) "
          "et `neuf-k9-g0.10-…` ; n80 pire (dichotomie) ; n_h = max(288 ; multiple de 16 ≥ 1,06 × n80 pire), ligne par ligne, sans enveloppe\n")
md.append("| dispersion | n80 40 (8) | n80 40 (9, 0,05 SUPPOSÉ) | n80 40 (9, 0,10) | n_h 40 (8) | n_h 40 (9, 0,05 SUPPOSÉ) | écart n_h 40 | n_h 40 (9, 0,10) | n80 160 (8) | n80 160 (9, 0,05 SUPPOSÉ) | n_h 160 (8) | n_h 160 (9, 0,05 SUPPOSÉ) | écart n_h 160 | n_h 160 (9, 0,10) | fiche 288 pire (9, 0,05 SUPPOSÉ, seuil 40) |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
res["neuvieme_n_h"] = {}
for nom, p8, suf in LOIS9:
    p95, p910 = f"neuf-k9-g0.05-{suf}", f"neuf-k9-g0.10-{suf}"
    if not all(x in S for x in (p8, p95, p910)):
        continue
    v = {"n80_40_k8": pire(p8, "retenue_ebh"), "n80_40_k9_g005": pire(p95, "retenue_ebh", k=9), "n80_40_k9_g010": pire(p910, "retenue_ebh", k=9),
         "n80_160_k8": pire(p8, "atteinte_160"), "n80_160_k9_g005": pire(p95, "atteinte_160", k=9), "n80_160_k9_g010": pire(p910, "atteinte_160", k=9),
         "fiche288_40_k9_g005": fiche_pire(p95, 288, fiche40, 9)}
    for s_ in ("40", "160"):
        for t in ("k8", "k9_g005", "k9_g010"):
            v[f"n_h_{s_}_{t}"] = nh_brut(v[f"n80_{s_}_{t}"])
        v[f"ecart_n_h_{s_}_g005"] = v[f"n_h_{s_}_k9_g005"] - v[f"n_h_{s_}_k8"]
        v[f"ecart_n_h_{s_}_g010"] = v[f"n_h_{s_}_k9_g010"] - v[f"n_h_{s_}_k8"]
        # ancien « surcoût » v8 : maximum par cellule de n80(9) − n80(8) (gardé pour la comparaison, ce n'est pas un écart de tailles)
        v[f"surcout_v8_{s_}_g005"] = max(dicho(p95, K_h, b, "retenue_ebh" if s_ == "40" else "atteinte_160", k=9)
                                         - dicho(p8, K_h, b, "retenue_ebh" if s_ == "40" else "atteinte_160") for K_h in (10, 5) for b in BIAIS)
    res["neuvieme_n_h"][nom] = v
    sg = lambda x: ("+" if x >= 0 else "−") + str(abs(x))
    md.append(f"| {nom} | {v['n80_40_k8']} | {v['n80_40_k9_g005']} | {v['n80_40_k9_g010']} | {v['n_h_40_k8']} | {v['n_h_40_k9_g005']} | {sg(v['ecart_n_h_40_g005'])} | {v['n_h_40_k9_g010']} | "
              f"{v['n80_160_k8']} | {v['n80_160_k9_g005']} | {v['n_h_160_k8']} | {v['n_h_160_k9_g005']} | {sg(v['ecart_n_h_160_g005'])} | {v['n_h_160_k9_g010']} | {f3(v['fiche288_40_k9_g005'])} |")
md.append("")

# ------------------------------------------------------------------ GD8-04 : puissances clés sur graines
md.append("## T4. Puissances clés sur plusieurs graines (GD8-04) : ρ_A = ρ_B = 0,17, 288 et 400 unités\n")
GR = [("meme-rho0.17", 20261029)] + [(f"graine{g}-meme-rho0.17", g) for g in range(11, 19)]
GR = [(p, g) for p, g in GR if p in S]
md.append(f"Source : passage v8 `meme-rho0.17` (graine 20261029) et passages v9 `graine11…18-meme-rho0.17` présents ({len(GR)} graines) ; moyenne ± erreur type (écart-type entre graines / √nombre)\n")
md.append("| taille | seuil | valeur v8 (graine 20261029) | pire des 4 cellules, par graine : moyenne ± erreur type | cellule la plus exigeante en moyenne : moyenne ± erreur type | cette cellule |")
md.append("| --- | --- | --- | --- | --- | --- |")
res["puissances_cles_graines"] = {"graines": [g for _, g in GR]}
for n in (288, 400):
    for s_, fn in (("40", fiche40), ("160", fiche160)):
        par_cellule = {(K_h, b): [fn(cell(p, K_h, n, b)) for p, _ in GR] for K_h in (10, 5) for b in BIAIS}
        pires = [min(par_cellule[c][i] for c in par_cellule) for i in range(len(GR))]
        cpire = min(par_cellule, key=lambda c: np.mean(par_cellule[c]))
        m1, e1 = float(np.mean(pires)), float(np.std(pires, ddof=1) / math.sqrt(len(pires))) if len(pires) > 1 else float("nan")
        xs = par_cellule[cpire]
        m2, e2 = float(np.mean(xs)), float(np.std(xs, ddof=1) / math.sqrt(len(xs))) if len(xs) > 1 else float("nan")
        res["puissances_cles_graines"][f"n={n}|seuil={s_}"] = {"v8": pires[0], "pire_par_graine": pires, "moyenne_pire": m1, "erreur_type_pire": e1,
                                                               "cellule_la_plus_exigeante": f"K_h={cpire[0]}|biais={cpire[1]}", "valeurs_cellule": xs, "moyenne_cellule": m2, "erreur_type_cellule": e2}
        md.append(f"| {n} | {s_} | {f3(pires[0])} | {f3(m1)} ± {f3(e1)} | {f3(m2)} ± {f3(e2)} | K_h = {cpire[0]}, biais {cpire[1]} |")
md.append("")

# ------------------------------------------------------------------ GD8-07 : ρ honnête = 2 ρ saboté
md.append("## T5. ρ honnête = 2 × ρ saboté (GD8-07, SUPPOSÉ) contre ρ honnête = ρ saboté (v8)\n")
md.append("Source : passages v9 `rhoh2x-meme-rho…` (`--facteur-rho-honnetes 2`) et v8 `meme-rho…` ; pire des quatre cellules\n")
md.append("| ρ saboté (A et B) | ρ honnête | fiche 288 (40) | fiche 288 (160) | n80 40 | n80 160 | n80 160 ajusté | n_h 40 | n_h 160 | garde min. 8, 288, seuil 160 (K_h 5, δ/4) |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
res["rho_honnete_double"] = {}
for r_ in ("0.05", "0.10", "0.17"):
    for p, rh in ((f"meme-rho{r_}", float(r_)), (f"rhoh2x-meme-rho{r_}", 2 * float(r_))):
        if p not in S:
            md.append(f"| {r_.replace('.', ',')} | {rtxt(rh)} | absent (non fini) | | | | | | | |")
            continue
        a40, a160 = pire(p, "retenue_ebh"), pire(p, "atteinte_160")
        j160 = pire_ajuste(p, "atteinte_160")
        c = cell(p, 5, 288, 0.0125)
        v = {"fiche288_40": fiche_pire(p, 288, fiche40), "fiche288_160": fiche_pire(p, 288, fiche160), "n80_40": a40, "n80_160": a160, "n80_160_ajuste": j160,
             "n_h_40": nh_brut(a40), "n_h_160": nh_brut(a160), "garde160_Kh5_biais": c["160.0"]["k_gardes"]["part"]}
        res["rho_honnete_double"][p] = v
        md.append(f"| {r_.replace('.', ',')} | {rtxt(rh)} | {f3(v['fiche288_40'])} | {f3(v['fiche288_160'])} | {a40} | {a160} | "
                  f"{'—' if j160 is None else f1(j160['estime']) + ' ± ' + f1(j160['ecart_type'])} | {v['n_h_40']} | {v['n_h_160']} | {f3(v['garde160_Kh5_biais'])} |")
md.append("")

# ------------------------------------------------------------------ GD8-03 : strates
md.append("## T6. Strates (GD8-03) : parts de variance et corrélation sujet–comparateurs (v8, cellule K_h = 10, biais 0, 288 unités)\n")
md.append("Source : `moments_tires` et `decomposition_effet_unite` des passages v8 de strates ; corrélation des p sabotés de A et des comparateurs en portée commune : "
          "0,5·0,4·γ²·moyenne(d²)/√(ρ·0,25 × ρ·0,24) (calcul de GD8-03), recalculée ici\n")
md.append("| passage | part de variance de p_A entre strates, sabotés | idem, honnêtes | part de variance du contraste prévue par les strates | idem, garde | corr. p_A–p_B sabotés calculée (commune) | fiche 288 (40), moyenne des 4 cellules (mesure du tableau v8) | fiche 288 (40), pire des 4 cellules |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
res["strates"] = {}
for p in sorted(x for x in S if x.startswith("strates-") and "n80" not in x):
    c = cell(p, 10, 288, 0.0)
    if c is None:
        continue
    m = c["moments_tires"]
    r = S[p]["reglages"]["strates_parametres"]
    Sx, g = r[0], r[1]
    d2 = 2 / 3 if Sx == 3 else 1.0
    corr_calc = 0.5 * 0.4 * g ** 2 * d2 / math.sqrt(0.17 * 0.25 * 0.17 * 0.24) if r[2] == "commune" else None
    v = {k: m.get(k) for k in ("part_variance_pA_entre_strates_sabotes", "part_variance_pA_entre_strates_honnetes", "part_variance_ecart_prevue_par_strates_contraste",
                               "part_variance_ecart_prevue_par_strates_garde")}
    v["correlation_calculee_commune"] = corr_calc
    v["fiche288_40_pire"] = fiche_pire(p, 288, fiche40)
    v["fiche288_40_moyenne_4_cellules"] = float(np.mean([fiche40(cell(p, K_h, 288, b)) for K_h in (10, 5) for b in BIAIS]))
    res["strates"][p] = v
    t = lambda x: "—" if x is None else f3(x)
    md.append(f"| `{p}` | {t(v['part_variance_pA_entre_strates_sabotes'])} | {t(v['part_variance_pA_entre_strates_honnetes'])} | {t(v['part_variance_ecart_prevue_par_strates_contraste'])} | "
              f"{t(v['part_variance_ecart_prevue_par_strates_garde'])} | {t(corr_calc)} | {t(v['fiche288_40_moyenne_4_cellules'])} | {t(v['fiche288_40_pire'])} |")
md.append("")

# ------------------------------------------------------------------ GD8-03 : portée partielle (v9), gain de l'étalonnage par portée
md.append("## T7. Strates : gain de l'étalonnage selon la portée (commune, partielle f = 0,5, sujet), ρ = 0,17, S ∈ {2 ; 3}, γ_A = 0,4 (GD8-03)\n")
md.append("Source : passages v8 `strates-commune-…`, `strates-sujet-…` et v9 `strates-partielle-f0.5-…` (brut et étalonné) ; fiche au seuil 40, moyenne des quatre cellules "
          "(mesure de la v8) et pire des quatre ; gain = étalonné − brut (moyenne des quatre différences)\n")
md.append("| portée | S | γ_B | fiche 288 brut (moy.) | fiche 288 étalonné (moy.) | gain 288 | fiche 288 étalonné (pire) | gain 400 | part de variance du contraste retirée par l'étalonnage |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
res["strates_portees"] = {}
for portee, gb, pref in (("commune", "0,4", "strates-commune"), ("partielle", "0,2", "strates-partielle-f0.5"), ("sujet", "0", "strates-sujet")):
    for Sx in (2, 3):
        pb, pc = f"{pref}-S{Sx}-g0.4-brut", f"{pref}-S{Sx}-g0.4-calibre"
        if pb not in S or pc not in S:
            md.append(f"| {portee} | {Sx} | {gb} | absent (non fini) | | | | | |")
            continue
        moy = lambda p, n: float(np.mean([fiche40(cell(p, K_h, n, b)) for K_h in (10, 5) for b in BIAIS]))
        v = {"brut_288": moy(pb, 288), "calibre_288": moy(pc, 288), "brut_400": moy(pb, 400), "calibre_400": moy(pc, 400),
             "calibre_288_pire": fiche_pire(pc, 288, fiche40),
             "part_variance_contraste": cell(pc, 10, 288, 0.0)["moments_tires"]["part_variance_ecart_prevue_par_strates_contraste"]}
        v["gain_288"], v["gain_400"] = v["calibre_288"] - v["brut_288"], v["calibre_400"] - v["brut_400"]
        res["strates_portees"][f"{portee}|S={Sx}"] = v
        sg = lambda x: ("+" if x >= 0 else "−") + f3(abs(x))
        md.append(f"| {portee} | {Sx} | {gb} | {f3(v['brut_288'])} | {f3(v['calibre_288'])} | {sg(v['gain_288'])} | {f3(v['calibre_288_pire'])} | {sg(v['gain_400'])} | {f3(v['part_variance_contraste'])} |")
md.append("")

with open(SORTIE_MD, "x", encoding="utf-8") as f:
    f.write("# Tableaux de la v9 (produits par `tableaux-v9.py` depuis les sorties ; puissances arrondies au plus proche à trois décimales, erreur type ≈ 0,008 à 0,85)\n\n")
    f.write("\n".join(md) + "\n")
res["script"] = os.path.basename(__file__)
res["script_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
with open(SORTIE_JSON, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
fin = datetime.now(timezone.utc)
man = {"passage": os.path.basename(SORTIE_JSON)[:-5], "ecrit_par": os.path.basename(__file__), "commit_lu_par_l_appelant": COMMIT,
       "date_utc_debut": debut.strftime("%Y-%m-%dT%H:%M:%SZ"), "date_utc_fin": fin.strftime("%Y-%m-%dT%H:%M:%SZ"), "commande": sys.argv,
       "script_sha256": res["script_sha256"], "graines": "aucun tirage (lecture des sorties)", "entrees": EMP,
       "environnement": {"python": platform.python_version(), "numpy": np.__version__},
       "fichiers": {os.path.basename(x): hashlib.sha256(open(x, "rb").read()).hexdigest() for x in (SORTIE_MD, SORTIE_JSON)}}
with open(os.path.join(os.path.dirname(os.path.abspath(SORTIE_JSON)), "manifeste-" + os.path.basename(SORTIE_JSON)), "x", encoding="utf-8") as f:
    json.dump(man, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("\n".join(md))
