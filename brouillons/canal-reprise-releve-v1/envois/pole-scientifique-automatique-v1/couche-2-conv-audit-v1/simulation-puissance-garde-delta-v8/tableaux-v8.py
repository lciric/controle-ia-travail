"""Tableaux du rapport v8, lus dans les sorties des passages (aucun chiffre recopié à la main). Écrit `tableaux-v8.md` (tableaux en markdown, avec la source de chaque
tableau) et `tableaux-v8-sortie.json` (mêmes nombres, non arrondis).

Mesures (toutes à k = 8 sauf la section du neuvième comparateur, τ = 0,01, δ = 0,05, α_c = 0,05, lecture (A) m = 2, 2 000 répétitions, graine 20261029) :
- « seuil 40 » : fiche = `ebh_A.retenues_fiches_du_sujet` (la fiche du mode 1 est retenue par l'e-BH de la famille de 2 fiches : lecture (A), m = 2) ;
- « seuil 160 » : fiche = `160.0.fiche_entiere.part` (le minimum des 2k processus du mode 1 atteint 160) ; la retenue e-BH à m = 8 n'est pas simulée (M = 2) :
  l'atteinte du seuil est une borne basse de la retenue ;
- n80 (n90) : plus petite taille (unités honnêtes = unités sabotées) pour laquelle la mesure atteint 0,8 (0,9), dichotomie `n_pour_puissance_0_8_fiche`, même graine ;
  incertitude de graine jusqu'à 6 % (GD2-07), mesurée en fin de rapport.
- règle de la table de lecture : n_h = max(288 ; plus petit multiple de 16 au moins égal à 1,06 × n80), au pire des deux K_h et des deux biais.

Usage : python3 -I -B tableaux-v8.py DOSSIER_V8 SORTIE.md SORTIE.json
"""
import hashlib
import json
import math
import os
import re
import sys

DOSSIER, SORTIE_MD, SORTIE_JSON = sys.argv[1:4]
PREF = "simulation-puissance-garde-delta-v8-sortie-"
TAILLES = (288, 400, 500, 650)
BIAIS = (0.0, 0.0125)
MARGE = 1.06
S, EMP = {}, {}
for f in sorted(os.listdir(DOSSIER)):
    if f.startswith(PREF) and f.endswith(".json"):
        nom = f[len(PREF):-5]
        EMP[nom] = hashlib.sha256(open(os.path.join(DOSSIER, f), "rb").read()).hexdigest()
        S[nom] = json.load(open(os.path.join(DOSSIER, f), encoding="utf-8"))
        r = S[nom]["reglages"]
        assert r["repetitions"] == 2000 and r["graine"] == 20261029 and S[nom]["version"] == "simulation-puissance-garde-delta-v8", nom

f2 = lambda x: f"{x:.2f}".replace(".", ",")
f3 = lambda x: f"{math.floor(x * 1000 + 1e-9) / 1000:.3f}".replace(".", ",")  # tronqué vers le bas (GD7-07) : une valeur affichée est un minorant
f4 = lambda x: f"{x:.4f}".replace(".", ",")


def rho(x):
    return f"{x:.3f}".rstrip("0").rstrip(".").replace(".", ",") if x else "0"


IDX = {}
for p, sortie in S.items():
    for et, c in sortie["cellules"].items():
        m = re.search(r"_Kh(\d+)_Ks(\d+)_", "_" + et)
        K_h, K_s = int(m.group(1)), int(m.group(2))
        n = int(re.search(r"\|n=(\d+)\|", et).group(1))
        b = float(re.search(r"biais=([0-9.]+)", et).group(1))
        k = int(re.search(r"\|k=(\d+)$", et).group(1))
        IDX[(p, K_h, K_s, n, b, k)] = (et, c)


def cell(p, K_h, K_s, n, b, k=8):
    return IDX[(p, K_h, K_s, n, b, k)][1]


def fiche40(c):
    return c["ebh_A"]["retenues_fiches_du_sujet"]


def fiche160(c):
    return c["160.0"]["fiche_entiere"]["part"]


def n80(p, K_h, K_s, b, mesure, k=8, cible="n80"):
    for nm, loi in S[p]["lois"].items():
        m = re.search(r"Kh(\d+)_Ks(\d+)_", nm)
        if int(m.group(1)) == K_h and int(m.group(2)) == K_s and "n_pour_puissance_0_8_fiche" in loi:
            v = loi["n_pour_puissance_0_8_fiche"].get(f"delta=0.05|biais={b}|k={k}")
            if v is not None and cible in v:
                return v[cible][mesure]
    return None


def txt(v):
    if v is None:
        return "—"
    return f"> {v['au_dela_de']}" if v["n_approx"] is None else str(v["n_approx"])


def val(v):
    return None if v is None or v["n_approx"] is None else v["n_approx"]


res = {"empreintes_sorties_v8": EMP, "fiche": {}, "n80": {}}
md = []


def libelle(p):
    r = S[p]["reglages"]
    a, b = r["effet_unite_beta"], r["rho_comparateurs"]
    if r.get("effet_unite_comparateurs"):
        a_txt = f"σ = {rho(r['effet_unite_comparateurs'])}"
        return a_txt + (" bêta" if r["echelle_dispersion"] == "beta" else " logit")
    if not b and not a:
        return "nulle"
    return f"ρ_A = {rho(a)}, ρ_B = {rho(b)}"


def tableau_fiches(titre, passages, K_s=10, k=8, mesure_n80=("retenue_ebh", "atteinte_160"), cible="n80", tailles=TAILLES, extra_col=None):
    out = []
    for seuil, fn, mn in (("40", fiche40, mesure_n80[0]), ("160", fiche160, mesure_n80[1])):
        out.append(f"#### {titre} — seuil {seuil}\n")
        out.append("Source : sorties `" + PREF + "*.json` des passages " + ", ".join(f"`{p}`" for p in passages) + " ; "
                   + ("`ebh_A.retenues_fiches_du_sujet`" if seuil == "40" else "`160.0.fiche_entiere.part`") + f" ; {cible} : `n_pour_puissance_0_8_fiche.{cible}.{mn}` ; 2000 répétitions, "
                   "erreur type ≤ 0,011\n")
        out.append("| passage | dispersion | K_h | K_s | biais | " + " | ".join(f"{n} unités" for n in tailles) + f" | {cible} |")
        out.append("| --- | --- | --- | --- | --- | " + " | ".join("---" for _ in tailles) + " | --- |")
        for p in passages:
            for K_h in sorted({kk[1] for kk in IDX if kk[0] == p}, reverse=True):
                for ks in sorted({kk[2] for kk in IDX if kk[0] == p and kk[1] == K_h}, reverse=True):
                    for b in BIAIS:
                        try:
                            vals = [fn(cell(p, K_h, ks, n, b, k)) for n in tailles]
                        except KeyError:
                            continue
                        v80 = n80(p, K_h, ks, b, mn, k, cible)
                        out.append(f"| `{p}` | {libelle(p)} | {K_h} | {ks} | {f4(b) if b else '0'} | " + " | ".join(f3(x) for x in vals) + f" | {txt(v80)} |")
                        res["fiche"][f"{seuil}|{p}|K_h={K_h}|K_s={ks}|k={k}|biais={b}"] = dict(zip(map(str, tailles), vals))
                        if v80 is not None:
                            res["n80"][f"{cible}|{mn}|{p}|K_h={K_h}|K_s={ks}|k={k}|biais={b}"] = v80
        out.append("")
    return out


# ---------------------------------------------------------------- R1
R1 = [p for p in ["rho0", "meme-rho0.05", "moitie-rho0.05", "meme-rho0.10", "moitie-rho0.10", "meme-rho0.17", "moitie-rho0.17", "meme-rho0.25"] if p in S]
md += ["## R1. Plus d'unités\n"]
md += tableau_fiches("T1. Puissance de la fiche à 288, 400, 500, 650 unités et n80 (K_s = 10, k = 8)", R1)
md += tableau_fiches("T1bis. n90 : unités pour une puissance de 0,9 (mêmes passages)", R1, cible="n90")

# gardes et contrastes à 288
md.append("#### T2. Minimum des 8 gardes et des 8 contrastes à 288 unités (K_s = 10)\n")
md.append("Source : `k_gardes.part` et `k_contrastes.part` des blocs `40.0` et `160.0` ; 2000 répétitions\n")
md.append("| passage | dispersion | K_h | biais | gardes 40 | gardes 160 | contrastes 40 | contrastes 160 |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
res["gardes_contrastes_288"] = {}
for p in R1:
    for K_h in (10, 5):
        for b in BIAIS:
            c = cell(p, K_h, 10, 288, b)
            v = [c["40.0"]["k_gardes"]["part"], c["160.0"]["k_gardes"]["part"], c["40.0"]["k_contrastes"]["part"], c["160.0"]["k_contrastes"]["part"]]
            md.append(f"| `{p}` | {libelle(p)} | {K_h} | {f4(b) if b else '0'} | " + " | ".join(f3(x) for x in v) + " |")
            res["gardes_contrastes_288"][f"{p}|K_h={K_h}|biais={b}"] = dict(zip(["garde40", "garde160", "contraste40", "contraste160"], v))
md.append("")

# table de lecture du pilote
md.append("#### T3. Table de lecture pour le pilote : ρ mesuré (sur les comparateurs, ρ_B) → n_h = max(288 ; multiple de 16 ≥ 1,06 × n80)\n")
md.append("Source : T1 ; n80 le plus grand des quatre cellules (K_h ∈ {10, 5} × biais ∈ {0 ; δ/4}) ; K_s = 10, k = 8, τ = 0,01, δ = 0,05, α_c = 0,05 ; deux hypothèses sur le sujet "
          "(non lu avant G1) : ρ_A = ρ_B, et ρ_A = 2 ρ_B ; enveloppe croissante en ρ_B appliquée à la colonne n_h\n")
md.append("| ρ_B mesuré | hypothèse sur A | passage | n80 seuil 40 (pire) | n80 seuil 160 (pire) | n90 seuil 40 (pire) | n_h seuil 40 | n_h seuil 160 |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
ligne_pilote = []
for hyp, passages in (("ρ_A = ρ_B", [("rho0", 0.0), ("meme-rho0.05", 0.05), ("meme-rho0.10", 0.10), ("meme-rho0.17", 0.17), ("meme-rho0.25", 0.25)]),
                      ("ρ_A = 2 ρ_B", [("moitie-rho0.05", 0.025), ("moitie-rho0.10", 0.05), ("moitie-rho0.17", 0.085)])):
    env = {"40": 0, "160": 0}
    for p, rb in passages:
        if p not in S:
            continue
        def pire(mesure, cible="n80"):
            vals = [val(n80(p, K_h, 10, b, mesure, 8, cible)) for K_h in (10, 5) for b in BIAIS]
            return None if any(v is None for v in vals) else max(vals)
        a40, a160, b40 = pire("retenue_ebh"), pire("atteinte_160"), pire("retenue_ebh", "n90")
        nh = {}
        for seuil, a in (("40", a40), ("160", a160)):
            if a is None:
                nh[seuil] = None
            else:
                brut = max(288, 16 * math.ceil(MARGE * a / 16))
                env[seuil] = max(env[seuil], brut)
                nh[seuil] = env[seuil]
        ligne_pilote.append({"rho_B": rb, "hypothese": hyp, "passage": p, "n80_40": a40, "n80_160": a160, "n90_40": b40, "n_h_40": nh["40"], "n_h_160": nh["160"]})
        md.append(f"| {rho(rb)} | {hyp} | `{p}` | {a40 if a40 is not None else '> borne'} | {a160 if a160 is not None else '> borne'} | {b40 if b40 is not None else '> borne'} | "
                  f"{nh['40'] if nh['40'] else '> borne'} | {nh['160'] if nh['160'] else '> borne'} |")
res["table_de_lecture_pilote"] = ligne_pilote
md.append("")
md.append("Lecture : mesurer ρ_B au pilote, prendre la ligne de la grille **égale ou immédiatement supérieure** (jamais interpoler vers le bas), lire n_h ; si ρ_B dépasse la dernière "
          "ligne, la table ne dit rien (hors grille). Précision de la mesure de ρ au pilote : voir `precision-rho-pilote-v8-sortie.json` (rapport).\n")

# ---------------------------------------------------------------- R2
R2 = [p for p in ["meme-rho0.10", "copule-rho0.10-c0.5", "copule-rho0.10-c0.8", "meme-rho0.17", "copule-rho0.17-c0.5", "copule-rho0.17-c0.8"] if p in S]
md += ["## R2. Difficulté d'unité partagée (copule gaussienne sujet–comparateurs)\n"]
md += tableau_fiches("T4. Fiche à 288 à 650 unités et n80 selon la corrélation c (c = 0 : passage `meme-rho…`)", R2)
md.append("#### T4bis. Corrélations tirées (288 unités, biais 0, K_h = 10) : de la copule (c) à celle des probabilités de A et des comparateurs\n")
md.append("Source : `moments_tires` des cellules à 288 unités ; Pearson attendu par quadrature : voir `verif-copule-strates-v8-sortie.json`\n")
md.append("| passage | c | Pearson(p_A, p_B) honnêtes | Pearson(p_A, p_B) sabotés | corr(f_A, f_B) observés | corr(r_A, r_B) observés | corr(p_B,i ; p_B,j) sabotés | écart-type de g | écart-type de v |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
res["copule_correlations"] = {}
for p in R2:
    c = cell(p, 10, 10, 288, 0.0)["moments_tires"]
    cc = S[p]["reglages"]["correlation_sujet_comparateurs"]
    if cc:
        md.append(f"| `{p}` | {rho(cc)} | {f3(c['correlation_pA_pB_honnetes'])} | {f3(c['correlation_pA_pB_sabotes'])} | {f3(c['correlation_fA_fB_honnetes'])} | "
                  f"{f3(c['correlation_rA_rB_sabotes'])} | {f3(c['correlation_pB_sabotes_entre_comparateurs'])} | {f4(c['ecart_type_g'])} | {f4(c['ecart_type_v'])} |")
        res["copule_correlations"][p] = {k: c[k] for k in c if k.startswith("correlation_") or k.startswith("ecart_type_")}
    else:
        md.append(f"| `{p}` | 0 | 0 (indépendants) | 0 | — | — | 0 | — | — |")
md.append("")

# ---------------------------------------------------------------- R3
md += ["## R3. Strates d'unités (blocage par une covariable de difficulté connue d'avance, étalonnage par strate)\n"]
md.append("#### T5. Fiche à 288 et 400 unités selon l'étalonnage par strate (A et B à ρ = 0,17, K_s = 10, allocation par blocs sauf mention)\n")
md.append("Source : passages `strates-…` ; « brut » : écarts non étalonnés (mêmes tirages que « étalonné » à même étiquette de loi près : les lois portent des noms distincts, "
          "donc des graines distinctes : l'écart de deux passages comprend le bruit de simulation, erreur type d'une différence ≈ 0,016) ; « part prévue » : part de la variance de "
          "l'écart (contraste) prévue par la strate, mesurée\n")
md.append("| portée | S | γ | allocation | analyse | K_h | biais | fiche 288 (40) | fiche 400 (40) | fiche 288 (160) | part prévue (contraste) | part de la variance de p_A entre strates (sabotés) |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
res["strates"] = {}
passages_str = sorted(p for p in S if p.startswith("strates-") and not p.startswith("strates-n80"))
gains = []
for p in passages_str:
    mm = re.match(r"strates-(sujet|commune)-S(\d)-g([0-9.]+)-(?:(iid)-)?(brut|calibre)$", p)
    portee, Sn, g, iid, ana = mm.groups()
    for K_h in (10, 5):
        for b in BIAIS:
            c288, c400 = cell(p, K_h, 10, 288, b), cell(p, K_h, 10, 400, b)
            m = c288["moments_tires"]
            md.append(f"| {portee} | {Sn} | {g} | {'iid' if iid else 'bloc'} | {ana} | {K_h} | {f4(b) if b else '0'} | {f3(fiche40(c288))} | {f3(fiche40(c400))} | {f3(fiche160(c288))} | "
                      f"{f3(m['part_variance_ecart_prevue_par_strates_contraste'])} | {f3(m['part_variance_pA_entre_strates_sabotes'])} |")
            res["strates"][f"{p}|K_h={K_h}|biais={b}"] = {"fiche40_288": fiche40(c288), "fiche40_400": fiche40(c400), "fiche160_288": fiche160(c288),
                                                           "part_prevue_contraste": m["part_variance_ecart_prevue_par_strates_contraste"],
                                                           "part_prevue_garde": m["part_variance_ecart_prevue_par_strates_garde"]}
md.append("")
md.append("#### T5bis. Gain de l'étalonnage par strate à 288 unités : fiche étalonnée moins fiche brute (seuil 40), moyenne sur K_h ∈ {10, 5} × biais ∈ {0 ; δ/4} (4 cellules)\n")
md.append("Source : T5 ; erreur type de la moyenne de 4 différences indépendantes ≈ 0,008\n")
md.append("| portée | S | γ | brut | étalonné | gain | même gain à 400 unités |")
md.append("| --- | --- | --- | --- | --- | --- | --- |")
res["strates_gain"] = {}
for portee in ("sujet", "commune"):
    for Sn in ("2", "3"):
        for g in ("0.2", "0.4"):
            pb, pc = f"strates-{portee}-S{Sn}-g{g}-brut", f"strates-{portee}-S{Sn}-g{g}-calibre"
            if pb not in S or pc not in S:
                continue
            mb = sum(fiche40(cell(pb, K, 10, 288, b)) for K in (10, 5) for b in BIAIS) / 4
            mc = sum(fiche40(cell(pc, K, 10, 288, b)) for K in (10, 5) for b in BIAIS) / 4
            mb4 = sum(fiche40(cell(pb, K, 10, 400, b)) for K in (10, 5) for b in BIAIS) / 4
            mc4 = sum(fiche40(cell(pc, K, 10, 400, b)) for K in (10, 5) for b in BIAIS) / 4
            res["strates_gain"][f"{portee}|S={Sn}|g={g}"] = {"brut288": mb, "calibre288": mc, "gain288": mc - mb, "gain400": mc4 - mb4}
            md.append(f"| {portee} | {Sn} | {g} | {f3(mb)} | {f3(mc)} | {'+' if mc - mb >= 0 else '−'}{f3(abs(mc - mb))} | {'+' if mc4 - mb4 >= 0 else '−'}{f3(abs(mc4 - mb4))} |")
md.append("")
n80s = [p for p in S if p.startswith("strates-n80-")]
if n80s:
    md += tableau_fiches("T5ter. Fiche et n80 avec ou sans étalonnage (sensibilité différenciée, S = 3, γ = 0,4, ρ = 0,17)", sorted(n80s))

# ---------------------------------------------------------------- R4
md += ["## R4. K plus grand (K_s = 20)\n"]
R4 = [p for p in ["ks20-rho0", "ks20-rho0.05", "ks20-rho0.17", "ks20-rho0.10", "ks20-Kh20-rho0.17"] if p in S]
md += tableau_fiches("T6. Fiche à 288 à 650 unités et n80 pour K_s = 20 (à comparer à K_s = 10 : T1)", [p for p in R4 if p not in ("ks20-rho0", "ks20-Kh20-rho0.17")])
md.append("#### T6bis. K_s = 20 contre K_s = 10 : fiche à 288 unités (seuil 40) et n80 (seuil 40, retenue e-BH), par dispersion ; K_s = 10 lu dans T1\n")
md.append("Source : T1 et T6 ; K_s = 10 : passages `meme-rho…` et `rho0` ; K_s = 20 : passages `ks20-…`\n")
md.append("| dispersion | K_h | biais | fiche K_s = 10 | fiche K_s = 20 | n80 K_s = 10 | n80 K_s = 20 | n80 160 K_s = 10 | n80 160 K_s = 20 |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
res["ks20"] = {}
for p10, p20 in (("rho0", "ks20-rho0"), ("meme-rho0.05", "ks20-rho0.05"), ("meme-rho0.10", "ks20-rho0.10"), ("meme-rho0.17", "ks20-rho0.17")):
    if p10 in S and p20 in S:
        for K_h in (10, 5):
            for b in BIAIS:
                a, c = fiche40(cell(p10, K_h, 10, 288, b)), fiche40(cell(p20, K_h, 20, 288, b))
                n10, n20 = n80(p10, K_h, 10, b, "retenue_ebh"), n80(p20, K_h, 20, b, "retenue_ebh") if p20 != "ks20-rho0" else None
                m10, m20 = n80(p10, K_h, 10, b, "atteinte_160"), n80(p20, K_h, 20, b, "atteinte_160") if p20 != "ks20-rho0" else None
                md.append(f"| {libelle(p10)} | {K_h} | {f4(b) if b else '0'} | {f3(a)} | {f3(c)} | {txt(n10)} | {txt(n20)} | {txt(m10)} | {txt(m20)} |")
                res["ks20"][f"{p10}|K_h={K_h}|biais={b}"] = {"fiche288_ks10": a, "fiche288_ks20": c, "n80_ks10": val(n10), "n80_ks20": val(n20), "n80_160_ks10": val(m10), "n80_160_ks20": val(m20)}
md.append("")
if "ks20-Kh20-rho0.17" in S:
    md.append("#### T6ter. K_h = 20 (ρ_A = ρ_B = 0,17, 288 unités) : fiche, minimum des 8 gardes et des 8 contrastes\n")
    md.append("Source : passage `ks20-Kh20-rho0.17`\n")
    md.append("| K_h | K_s | biais | fiche 40 | gardes 40 | contrastes 40 | gardes 160 | contrastes 160 |")
    md.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    res["kh20"] = {}
    for ks in (10, 20):
        for b in BIAIS:
            c = cell("ks20-Kh20-rho0.17", 20, ks, 288, b)
            v = [fiche40(c), c["40.0"]["k_gardes"]["part"], c["40.0"]["k_contrastes"]["part"], c["160.0"]["k_gardes"]["part"], c["160.0"]["k_contrastes"]["part"]]
            md.append(f"| 20 | {ks} | {f4(b) if b else '0'} | " + " | ".join(f3(x) for x in v) + " |")
            res["kh20"][f"K_s={ks}|biais={b}"] = v
    md.append("")

# ---------------------------------------------------------------- neuvième comparateur
md += ["## Effet d'un neuvième comparateur\n"]
LOIS9 = [("nulle", "rho0", None), ("logit σ = 1,0", "neuf-k8-logit1.0", "logit1.0"), ("bêta (σ de référence 1,0)", "neuf-k8-beta1.0", "beta1.0"),
         ("ρ_A = ρ_B = 0,05", "meme-rho0.05", "rho0.05"), ("ρ_A = ρ_B = 0,10", "meme-rho0.10", "rho0.10"), ("ρ_A = ρ_B = 0,17", "meme-rho0.17", "rho0.17")]
md.append("#### T7. Huit ou neuf comparateurs : fiche à 288, 400, 500, 650 unités (seuil 40) et n80 (seuils 40 et 160), K_s = 10 ; neuvième comparateur d'écart de contraste 0,05 (SUPPOSÉ, "
          "« comparateur fort ») ou 0,10 (comme les huit autres)\n")
md.append("Source : k = 8 : passages `rho0`, `meme-rho…` (R1) et `neuf-k8-…` ; k = 9 : passages `neuf-k9-g0.05-…` et `neuf-k9-g0.10-…` ; mêmes paramètres, 2000 répétitions\n")
md.append("| dispersion | k | écart du 9ᵉ | K_h | biais | 288 | 400 | 500 | 650 | n80 seuil 40 | n80 seuil 160 | surcoût n80 seuil 40 (unités) | surcoût seuil 160 |")
md.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
res["neuvieme"] = {}
for nom_loi, p8, suf in LOIS9:
    variantes = [("8", "—", p8, 8)]
    for g, T in (("0,05", "g0.05"), ("0,10", "g0.10")):
        if suf is None:
            p9 = f"neuf-k9-{T}-nulle"
        else:
            p9 = f"neuf-k9-{T}-{suf}"
        variantes.append(("9", g, p9, 9))
    for k_txt, g, p, kk in variantes:
        if p not in S:
            continue
        for K_h in (10, 5):
            for b in BIAIS:
                try:
                    vals = [fiche40(cell(p, K_h, 10, n, b, kk)) for n in TAILLES]
                except KeyError:
                    continue
                v40, v160 = n80(p, K_h, 10, b, "retenue_ebh", kk), n80(p, K_h, 10, b, "atteinte_160", kk)
                base40 = n80(p8, K_h, 10, b, "retenue_ebh", 8)
                base160 = n80(p8, K_h, 10, b, "atteinte_160", 8)
                sur40 = None if kk == 8 or val(v40) is None or val(base40) is None else val(v40) - val(base40)
                sur160 = None if kk == 8 or val(v160) is None or val(base160) is None else val(v160) - val(base160)
                md.append(f"| {nom_loi} | {k_txt} | {g} | {K_h} | {f4(b) if b else '0'} | " + " | ".join(f3(x) for x in vals)
                          + f" | {txt(v40)} | {txt(v160)} | {'—' if sur40 is None else ('+' if sur40 >= 0 else '−') + str(abs(sur40))} | {'—' if sur160 is None else ('+' if sur160 >= 0 else '−') + str(abs(sur160))} |")
                res["neuvieme"][f"{nom_loi}|k={kk}|g={g}|K_h={K_h}|biais={b}"] = {"passage": p, "fiche40": dict(zip(map(str, TAILLES), vals)), "n80_40": val(v40), "n80_160": val(v160),
                                                                                  "surcout_40": sur40, "surcout_160": sur160}
md.append("")
md.append("#### T7bis. Gardes et contrastes à 288 unités avec neuf comparateurs (K_h = 5, biais δ/4, seuil 40) : où la fiche perd-elle ?\n")
md.append("Source : cellules à 288 unités des passages `neuf-k9-…`\n")
md.append("| dispersion | écart du 9ᵉ | minimum des 9 gardes | minimum des 9 contrastes | fiche |")
md.append("| --- | --- | --- | --- | --- |")
res["neuvieme_gardes_contrastes"] = {}
for nom_loi, p8, suf in LOIS9:
    for g, T in (("0,05", "g0.05"), ("0,10", "g0.10")):
        p = f"neuf-k9-{T}-nulle" if suf is None else f"neuf-k9-{T}-{suf}"
        if p in S:
            c = cell(p, 5, 10, 288, 0.0125, 9)
            v = [c["40.0"]["k_gardes"]["part"], c["40.0"]["k_contrastes"]["part"], fiche40(c)]
            md.append(f"| {nom_loi} | {g} | {f3(v[0])} | {f3(v[1])} | {f3(v[2])} |")
            res["neuvieme_gardes_contrastes"][f"{nom_loi}|g={g}"] = v
md.append("")

# ---------------------------------------------------------------- artefacts, durées
md.append("#### T8. Artefacts de la garde (R5), toutes cellules de tous les passages\n")
md.append("Source : blocs `40.0` et `160.0`, `frontiere_part`, `frontiere_borne_ville` (= 1/seuil), `tricheur_part`\n")
md.append("| passage | cellules | frontière 40 (max) | borne 1/40 | frontière 160 (max) | borne 1/160 | tricheur (max) |")
md.append("| --- | --- | --- | --- | --- | --- | --- |")
res["artefacts"] = {}
for p in sorted(S):
    cs = list(S[p]["cellules"].values())
    f40, f160 = max(c["40.0"]["frontiere_part"] for c in cs), max(c["160.0"]["frontiere_part"] for c in cs)
    tr = max(max(c["40.0"]["tricheur_part"], c["160.0"]["tricheur_part"]) for c in cs)
    res["artefacts"][p] = {"cellules": len(cs), "frontiere40_max": f40, "frontiere160_max": f160, "tricheur_max": tr, "frontiere40_sur_borne": f40 * 40, "frontiere160_sur_borne": f160 * 160}
    md.append(f"| `{p}` | {len(cs)} | {f4(f40)} | {f4(1 / 40)} | {f4(f160)} | {f4(1 / 160)} | {f4(tr)} |")
md.append("")
md.append("#### T9. Passages : répétitions, durée, graine, commit déclaré, empreinte de la sortie\n")
md.append("Source : sorties et manifestes par passage\n")
md.append("| passage | répétitions | durée (s) | graine | sortie |")
md.append("| --- | --- | --- | --- | --- |")
res["durees_s"] = {}
for p in sorted(S):
    man = json.load(open(os.path.join(DOSSIER, "manifeste-" + PREF + p + ".json"), encoding="utf-8"))
    assert man["script"]["commit"] == S[p]["commit"]
    res["durees_s"][p] = man["duree_s"]
    md.append(f"| `{p}` | {S[p]['reglages']['repetitions']} | {man['duree_s']} | {man['graines']['graine_maitresse']} | `{EMP[p][:8]}…` |")
md.append("")
open(SORTIE_MD, "x", encoding="utf-8").write("\n".join(md) + "\n")
with open(SORTIE_JSON, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("écrit", SORTIE_MD, SORTIE_JSON, "passages :", len(S))
