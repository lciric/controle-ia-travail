"""Tableaux résumés du rapport v8, calculés depuis `tableaux-v8-sortie.json` (rien n'est recopié à la main). « Pire » = au pire des quatre cellules (K_h ∈ {10, 5} × biais ∈ {0 ; δ/4}) :
minimum pour une puissance, maximum pour un n80 ou un n90 ; k = 8 sauf section du neuvième comparateur ; K_s = 10 sauf R4. Écrit `resume-v8.md` (un bloc par étiquette `{{R1}}`, etc.) et `resume-v8-sortie.json`.
Coût en épisodes (SUPPOSÉ : plan apparié, le sujet et chaque comparateur jouent tous les épisodes) : n × (K_h + K_s) × (k + 1), à K_h = 5.
Lit aussi `precision-rho-pilote-v8-sortie.json` et `incertitude-graine-n80-v8-sortie.json` (blocs PREC et GRAINE) et ajoute le bloc GC (où la fiche perd-elle : garde ou contraste, à 288 unités).
Usage : python3 -I -B resume-v8.py TABLEAUX_SORTIE.json PRECISION_RHO.json INCERTITUDE_GRAINE.json SORTIE.md SORTIE.json
"""
import json
import math
import sys

T = json.load(open(sys.argv[1], encoding="utf-8"))
PREC = json.load(open(sys.argv[2], encoding="utf-8"))
GRN = json.load(open(sys.argv[3], encoding="utf-8"))
SORTIE_MD, SORTIE_JSON = sys.argv[4:6]
BIAIS = (0.0, 0.0125)
TAILLES = ("288", "400", "500", "650")
f3 = lambda x: f"{math.floor(x * 1000 + 1e-9) / 1000:.3f}".replace(".", ",")  # tronqué vers le bas (GD7-07) : une valeur affichée est un minorant
f2 = lambda x: f"{x:.2f}".replace(".", ",")
res, blocs = {}, {}


def rho(x):
    return f"{x:.3f}".rstrip("0").rstrip(".").replace(".", ",") if x else "0"


def fiche_pire(seuil, p, K_s=10, k=8, taille="288", Ks_h=(10, 5)):
    return min(T["fiche"][f"{seuil}|{p}|K_h={K}|K_s={K_s}|k={k}|biais={b}"][taille] for K in Ks_h for b in BIAIS)


def n_pire(cible, mesure, p, K_s=10, k=8, Ks_h=(10, 5)):
    vals = [T["n80"].get(f"{cible}|{mesure}|{p}|K_h={K}|K_s={K_s}|k={k}|biais={b}") for K in Ks_h for b in BIAIS]
    if any(v is None or v["n_approx"] is None for v in vals):
        return None
    return max(v["n_approx"] for v in vals)


def n_txt(v):
    return "> borne" if v is None else str(v)


def nh(a):
    return None if a is None else max(288, 16 * math.ceil(1.06 * a / 16))


# ------------------------------------------------------------------ R1
L = ["| ρ_A | ρ_B | seuil | 288 | 400 | 500 | 650 | n80 (pire) | n90 (pire) |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
res["R1"] = {}
cas = [("rho0", 0, 0), ("meme-rho0.05", 0.05, 0.05), ("moitie-rho0.05", 0.05, 0.025), ("meme-rho0.10", 0.10, 0.10), ("moitie-rho0.10", 0.10, 0.05),
       ("meme-rho0.17", 0.17, 0.17), ("moitie-rho0.17", 0.17, 0.085), ("meme-rho0.25", 0.25, 0.25)]
for p, ra, rb in cas:
    for seuil, mesure in (("40", "retenue_ebh"), ("160", "atteinte_160")):
        if f"{seuil}|{p}|K_h=10|K_s=10|k=8|biais=0.0" not in T["fiche"]:
            continue
        f = [fiche_pire(seuil, p, taille=t) for t in TAILLES]
        a, b9 = n_pire("n80", mesure, p), n_pire("n90", mesure, p)
        L.append(f"| {rho(ra)} | {rho(rb)} | {seuil} | " + " | ".join(f3(x) for x in f) + f" | {n_txt(a)} | {n_txt(b9)} |")
        res["R1"][f"{p}|{seuil}"] = {"fiche_pire": dict(zip(TAILLES, f)), "n80_pire": a, "n90_pire": b9}
blocs["R1"] = "\n".join(L)

# ------------------------------------------------------------------ pilote
L = ["| ρ_B mesuré | hypothèse sur A | n80 seuil 40 (pire) | n80 seuil 160 (pire) | n_h seuil 40 | n_h seuil 160 |", "| --- | --- | --- | --- | --- | --- |"]
for r in T["table_de_lecture_pilote"]:
    L.append(f"| {rho(r['rho_B'])} | {r['hypothese']} | {n_txt(r['n80_40'])} | {n_txt(r['n80_160'])} | {n_txt(r['n_h_40'])} | {n_txt(r['n_h_160'])} |")
blocs["PILOTE"] = "\n".join(L)

# ------------------------------------------------------------------ R2
L = ["| ρ_A = ρ_B | c | Pearson(p_A, p_B) sabotés | fiche 288, seuil 40 (pire) | fiche 288, seuil 160 (pire) | fiche 400, seuil 160 (pire) | n80 seuil 40 (pire) | n80 seuil 160 (pire) |",
     "| --- | --- | --- | --- | --- | --- | --- | --- |"]
res["R2"] = {}
for r_, base in (("0.10", "meme-rho0.10"), ("0.17", "meme-rho0.17")):
    for c, p in ((0, base), (0.5, f"copule-rho{r_}-c0.5"), (0.8, f"copule-rho{r_}-c0.8")):
        if f"40|{p}|K_h=10|K_s=10|k=8|biais=0.0" not in T["fiche"]:
            continue
        pear = T["copule_correlations"][p]["correlation_pA_pB_sabotes"] if c else 0.0
        v = [fiche_pire("40", p), fiche_pire("160", p), fiche_pire("160", p, taille="400")]
        a, b = n_pire("n80", "retenue_ebh", p), n_pire("n80", "atteinte_160", p)
        L.append(f"| {rho(float(r_))} | {rho(c)} | {f2(pear)} | " + " | ".join(f3(x) for x in v) + f" | {n_txt(a)} | {n_txt(b)} |")
        res["R2"][p] = {"c": c, "pearson_sabotes": pear, "fiche288_40": v[0], "fiche288_160": v[1], "fiche400_160": v[2], "n80_40": a, "n80_160": b}
blocs["R2"] = "\n".join(L)

# ------------------------------------------------------------------ R3
L = ["| portée | S | γ | fiche 288 brute | fiche 288 étalonnée | gain à 288 | gain à 400 |", "| --- | --- | --- | --- | --- | --- | --- |"]
for k_, g in T["strates_gain"].items():
    portee, s_, gam = k_.split("|")
    L.append(f"| {portee} | {s_[2:]} | {gam[2:]} | {f3(g['brut288'])} | {f3(g['calibre288'])} | {'+' if g['gain288'] >= 0 else '−'}{f3(abs(g['gain288']))} | {'+' if g['gain400'] >= 0 else '−'}{f3(abs(g['gain400']))} |")
blocs["R3"] = "\n".join(L)
L = ["| passage | fiche 288 (pire) | fiche 400 (pire) | fiche 500 (pire) | fiche 650 (pire) | n80 seuil 40 (pire) | n80 seuil 160 (pire) |", "| --- | --- | --- | --- | --- | --- | --- |"]
res["R3_n80"] = {}
for p, nom in (("meme-rho0.17", "sans strate (A et B, ρ = 0,17)"), ("strates-n80-sujet-S3-g0.4-brut", "3 strates, γ = 0,4, sensibilité différenciée, brut"),
               ("strates-n80-sujet-S3-g0.4-calibre", "3 strates, γ = 0,4, sensibilité différenciée, étalonné")):
    if f"40|{p}|K_h=10|K_s=10|k=8|biais=0.0" in T["fiche"]:
        f = [fiche_pire("40", p, taille=t) for t in TAILLES]
        a, b = n_pire("n80", "retenue_ebh", p), n_pire("n80", "atteinte_160", p)
        L.append(f"| {nom} | " + " | ".join(f3(x) for x in f) + f" | {n_txt(a)} | {n_txt(b)} |")
        res["R3_n80"][p] = {"fiche_pire": dict(zip(TAILLES, f)), "n80_40": a, "n80_160": b}
blocs["R3N80"] = "\n".join(L)

# ------------------------------------------------------------------ R4
L = ["| ρ_A = ρ_B | K_s | fiche 288, seuil 40 (pire) | fiche 288, seuil 160 (pire) | n80 seuil 40 (pire) | n80 seuil 160 (pire) | épisodes au n80 seuil 40 (K_h = 5) | épisodes à 400 unités (K_h = 5) |",
     "| --- | --- | --- | --- | --- | --- | --- | --- |"]
res["R4"] = {}
for r_, p10, p20 in (("0.05", "meme-rho0.05", "ks20-rho0.05"), ("0.10", "meme-rho0.10", "ks20-rho0.10"), ("0.17", "meme-rho0.17", "ks20-rho0.17")):
    for Ks, p in ((10, p10), (20, p20)):
        if f"40|{p}|K_h=10|K_s={Ks}|k=8|biais=0.0" not in T["fiche"]:
            continue
        v = [fiche_pire("40", p, K_s=Ks), fiche_pire("160", p, K_s=Ks)]
        a, b = n_pire("n80", "retenue_ebh", p, K_s=Ks), n_pire("n80", "atteinte_160", p, K_s=Ks)
        epi = None if a is None else a * (5 + Ks) * 9
        epi400 = 400 * (5 + Ks) * 9
        L.append(f"| {rho(float(r_))} | {Ks} | {f3(v[0])} | {f3(v[1])} | {n_txt(a)} | {n_txt(b)} | {epi if epi else '> borne'} | {epi400} |")
        res["R4"][f"{p}|K_s={Ks}"] = {"fiche288_40": v[0], "fiche288_160": v[1], "n80_40": a, "n80_160": b, "episodes_n80_40": epi, "episodes_400": epi400}
blocs["R4"] = "\n".join(L)

# ------------------------------------------------------------------ neuf
noms = ["nulle", "logit σ = 1,0", "bêta (σ de référence 1,0)", "ρ_A = ρ_B = 0,05", "ρ_A = ρ_B = 0,10", "ρ_A = ρ_B = 0,17"]
L = ["| dispersion | k | écart du 9ᵉ | 288 | 400 | 500 | 650 | n80 seuil 40 (pire) | n80 seuil 160 (pire) | surcoût seuil 40 (unités, pire) | surcoût seuil 160 (unités, pire) | n_h seuil 40 | n_h seuil 160 |",
     "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
res["neuf"] = {}
for nom in noms:
    for k, g in ((8, "—"), (9, "0,05"), (9, "0,10")):
        cles = [f"{nom}|k={k}|g={g}|K_h={K}|biais={b}" for K in (10, 5) for b in BIAIS]
        if any(c not in T["neuvieme"] for c in cles):
            continue
        d = [T["neuvieme"][c] for c in cles]
        f = [min(x["fiche40"][t] for x in d) for t in TAILLES]
        a = None if any(x["n80_40"] is None for x in d) else max(x["n80_40"] for x in d)
        b = None if any(x["n80_160"] is None for x in d) else max(x["n80_160"] for x in d)
        s40 = [x["surcout_40"] for x in d]
        s160 = [x["surcout_160"] for x in d]
        sx40 = None if k == 8 or any(s is None for s in s40) else max(s40)
        sx160 = None if k == 8 or any(s is None for s in s160) else max(s160)
        L.append(f"| {nom} | {k} | {g} | " + " | ".join(f3(x) for x in f) + f" | {n_txt(a)} | {n_txt(b)} | {'—' if sx40 is None else ('+' if sx40 >= 0 else '−') + str(abs(sx40))} | "
                 f"{'—' if sx160 is None else ('+' if sx160 >= 0 else '−') + str(abs(sx160))} | {n_txt(nh(a))} | {n_txt(nh(b))} |")
        res["neuf"][f"{nom}|k={k}|g={g}"] = {"fiche_pire": dict(zip(TAILLES, f)), "n80_40": a, "n80_160": b, "surcout_40": sx40, "surcout_160": sx160, "n_h_40": nh(a), "n_h_160": nh(b)}
blocs["NEUF"] = "\n".join(L)

# ------------------------------------------------------------------ GC : où la fiche perd-elle (288 unités, K_s = 10)
L = ["| ρ_A | ρ_B | minimum des 8 gardes, seuil 40 | minimum des 8 gardes, seuil 160 | minimum des 8 contrastes, seuil 40 | minimum des 8 contrastes, seuil 160 |", "| --- | --- | --- | --- | --- | --- |"]
res["GC"] = {}
for p, ra, rb in cas:
    cles = [f"{p}|K_h={K}|biais={b}" for K in (10, 5) for b in BIAIS]
    if any(c not in T["gardes_contrastes_288"] for c in cles):
        continue
    v = [min(T["gardes_contrastes_288"][c][m] for c in cles) for m in ("garde40", "garde160", "contraste40", "contraste160")]
    L.append(f"| {rho(ra)} | {rho(rb)} | " + " | ".join(f3(x) for x in v) + " |")
    res["GC"][p] = dict(zip(("garde40", "garde160", "contraste40", "contraste160"), v))
blocs["GC"] = "\n".join(L)

# ------------------------------------------------------------------ PREC : précision de la lecture de ρ au pilote
L = ["| ρ vrai | N unités du pilote | écart-type de ρ̂ côté sabotage (p = 0,4) | écart-type de ρ̂ côté honnête (p = 0,01) |", "| --- | --- | --- | --- |"]
res["PREC"] = {}
for r_ in (0.05, 0.10, 0.17, 0.25):
    for N in (50, 100, 288):
        a = [c for c in PREC["cellules"] if c["p"] == 0.4 and c["rho"] == r_ and c["N"] == N][0]
        b = [c for c in PREC["cellules"] if c["p"] == 0.01 and c["rho"] == r_ and c["N"] == N][0]
        L.append(f"| {rho(r_)} | {N} | {f3(a['ecart_type'])} | {f3(b['ecart_type'])} |")
        res["PREC"][f"rho={r_}|N={N}"] = {"sd_p04": a["ecart_type"], "sd_p001": b["ecart_type"]}
blocs["PREC"] = "\n".join(L)

# ------------------------------------------------------------------ GRAINE
L = ["| ρ_A = ρ_B | mesure | seuil | n80 ou n90 par graine (20261029 ; 1 ; 2 ; 3) | écart relatif maximal à la moyenne | étendue relative |", "| --- | --- | --- | --- | --- | --- |"]
for k_, l in GRN["lignes"].items():
    r_, cible, mesure = k_.split("|")
    L.append(f"| {rho(float(r_[4:]))} | {cible} | {'40' if mesure == 'retenue_ebh' else '160'} | " + " ; ".join(str(v) for v in l["n_par_graine"].values())
             + f" | {f3(l['ecart_relatif_maximal'])} | {f3(l['etendue_relative'])} |")
blocs["GRAINE"] = "\n".join(L)
res["GRAINE"] = {"ecart_relatif_maximal": GRN["ecart_relatif_maximal_toutes_lignes"], "etendue_relative_maximale": GRN["etendue_relative_maximale_toutes_lignes"]}

with open(SORTIE_MD, "x", encoding="utf-8") as f:
    for k, v in blocs.items():
        f.write(f"<!-- {k} -->\n{v}\n\n")
with open(SORTIE_JSON, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("écrit", SORTIE_MD, SORTIE_JSON)
