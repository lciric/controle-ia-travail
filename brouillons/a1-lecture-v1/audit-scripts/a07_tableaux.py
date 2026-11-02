"""Audit A1 (auditeur neuf, 2e) — section 6, tableaux descriptifs par fournisseur (Argon seul, Kimi seul, ensemble) :
taux aux n ∈ {1, 4, 16} par (monde, juge, condition) avec Wilson à 95 % (champ `taux` du code, préenregistré « par
fournisseur et pour l'ensemble », section 5) ; Δₙ par unité avec paires discordantes et McNemar (préenregistré pour
l'ensemble ; par fournisseur : exploratoire) ; Δ_loi (préenregistré pour l'ensemble ; par fournisseur : exploratoire,
`ag.ecart_par_loi` sur le sous-ensemble) ; parts de l'instrument (préenregistré pour l'ensemble ; par fournisseur :
exploratoire). Lecture seule ; écrit travail/a07-tableaux-v1.md et .json."""
import json, sys
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
sys.path.insert(0, "/home/claude/ideation-organism/orchestrator")
from pole import attaque_goodhart_v2 as ag
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
M = json.load(open(B + "entree/sortie/manifeste.json", encoding="utf-8"))
E = int(M["reglages"]["entropie_racine"])
S, RJ = R["suites"], R["rejeux"]
L = R["lecture"]["mondes"]
md, js = [], {}
def f3(x): return "—" if x is None else f"{x:.3f}"
for w in ("W1", "W2"):
    md.append(f"\n### {w} — taux par unité (promue en au plus n), Wilson 95 % — calculé par le code (`lecture.mondes.{w}.taux`), préenregistré par fournisseur et ensemble\n")
    md.append("| juge | condition | n | Argon x/12 | Wilson | Kimi x/12 | Wilson | ensemble x/24 | Wilson |")
    md.append("|---|---|---|---|---|---|---|---|---|")
    for j in ("v8", "v7"):
        for c in ("retour", "temoin"):
            for n in (1, 4, 16):
                row = [j, c, str(n)]
                for fo in ("argon", "kimi", "ensemble"):
                    t = L[w]["taux"][f"{j}|{c}|n={n}|{fo}"]
                    row += [f"{t['promues']}/{t['unites']}", f"[{t['wilson_95'][0]:.3f} ; {t['wilson_95'][1]:.3f}]"]
                md.append("| " + " | ".join(row) + " |")
    # Δn par unité
    md.append(f"\n### {w} — Δₙ = taux(retour) − taux(témoin) par unité, paires discordantes (retour seul / témoin seul), McNemar exact — ensemble : calculé par le code (`ecarts_goodhart_par_carte`) ; par fournisseur : exploratoire, hors préenregistrement\n")
    md.append("| juge | n | Argon Δ | b/c | p | Kimi Δ | b/c | p | ensemble Δ | b/c | p |")
    md.append("|---|---|---|---|---|---|---|---|---|---|---|")
    js[w] = {"delta_n": {}}
    for j in ("v8", "v7"):
        for n in (1, 4, 16):
            row = [j, str(n)]
            for fo in ("argon", "kimi", "ensemble"):
                sel = [s for s in S if s["monde"] == w and s["juge"] == j and (fo == "ensemble" or s["fournisseur"] == fo)]
                rr = {(s["carte"], s["fournisseur"]): ag.promue_en(s, n) for s in sel if s["condition"] == "retour"}
                tt = {(s["carte"], s["fournisseur"]): ag.promue_en(s, n) for s in sel if s["condition"] == "temoin"}
                u = sorted(set(rr) & set(tt))
                b = sum(rr[x] and not tt[x] for x in u); c = sum(tt[x] and not rr[x] for x in u)
                d = (sum(rr[x] for x in u) - sum(tt[x] for x in u)) / len(u)
                p = ag.mcnemar_exact(b, c)
                row += [f"{d:+.3f}", f"{b}/{c}", f"{p:.3f}"]
                js[w]["delta_n"][f"{j}|n={n}|{fo}"] = {"ecart": round(d, 4), "retour_seul": b, "temoin_seul": c, "mcnemar_p": p, "unites": len(u)}
            md.append("| " + " | ".join(row) + " |")
    # Δ_loi
    md.append(f"\n### {w} — Δ_loi (H3) : probabilité de promotion rejouée des lois des tentatives k ≥ 2, retour − témoin, moyenne sur les unités, IC 95 % percentile (2 000 rééchantillonnages) — ensemble : calculé par le code (`ecart_par_loi_H3`) ; par fournisseur : exploratoire, hors préenregistrement (même graine « bootstrap »)\n")
    md.append("| juge | fournisseur | unités | Δ_loi | IC 95 % | lecture du code | lecture selon la section 5 (< 6 unités : non lisible) |")
    md.append("|---|---|---|---|---|---|---|")
    js[w]["delta_loi"] = {}
    for j in ("v8", "v7"):
        for fo in ("argon", "kimi", "ensemble"):
            sel = [s for s in S if fo == "ensemble" or s["fournisseur"] == fo]
            e = ag.ecart_par_loi(sel, RJ, w, j, E)
            if fo == "ensemble":
                assert abs((e["ecart"] or 0) - (L[w]["ecart_par_loi_H3"][j]["ecart"] or 0)) < 1e-12 and e["unites"] == L[w]["ecart_par_loi_H3"][j]["unites"]
            lect = e["lecture"] if e["unites"] >= 6 else ("non lisible (unités insuffisantes)" if e["unites"] > 0 else "non tranché (aucune unité)")
            ic = "—" if e["ic95"] is None else f"[{e['ic95'][0]:+.4f} ; {e['ic95'][1]:+.4f}]"
            md.append(f"| {j} | {fo}{'' if fo == 'ensemble' else ' (exploratoire)'} | {e['unites']} | {'—' if e['ecart'] is None else f'{e['ecart']:+.4f}'} | {ic} | {e['lecture']} | {lect} |")
            js[w]["delta_loi"][f"{j}|{fo}"] = e
    # instrument
    md.append(f"\n### {w} — instrument sur « retour|v8 » — ensemble : calculé par le code (`instrument_v8_retour`) ; par fournisseur : exploratoire\n")
    md.append("| fournisseur | tentatives | lois jugées | invalides ou échouées | échos attendus | échos exacts | part échos | lois distinctes / tentatives (suites > 1) | part distinctes | hors classe | part hors classe |")
    md.append("|---|---|---|---|---|---|---|---|---|---|---|")
    js[w]["instrument"] = {}
    for fo in ("argon", "kimi", "ensemble"):
        sel = [s for s in S if s["monde"] == w and s["condition"] == "retour" and s["juge"] == "v8" and (fo == "ensemble" or s["fournisseur"] == fo)]
        i = ag.instrument(sel)
        longues = [s for s in sel if len(s["tentatives"]) > 1]
        dist = sum(len({json.dumps(t["loi"], sort_keys=True) for t in s["tentatives"] if t["loi"] is not None}) for s in longues)
        tl = sum(len(s["tentatives"]) for s in longues)
        if fo == "ensemble":
            assert {k: i[k] for k in i} == L[w]["instrument_v8_retour"]
        md.append(f"| {fo}{'' if fo == 'ensemble' else ' (exploratoire)'} | {i['tentatives']} | {i['lois_jugees']} | {i['invalides']} | {i['echos_attendus']} | {i['echos_exacts']} | {f3(i['part_echos_exacts'])} | {dist}/{tl} | {f3(i['part_lois_distinctes'])} | {i['hors_classe']} | {f3(i['part_hors_classe'])} |")
        js[w]["instrument"][fo] = dict(i, lois_distinctes=dist, tentatives_suites_longues=tl)
    # rejeux par fournisseur (exploratoire)
    md.append(f"\n### {w} — rejeux hors ligne (`rejeux`, 200 sous v8, 20 sous v7) : promotions / rejeux, par fournisseur et condition — descriptif, exploratoire\n")
    md.append("| juge | condition | Argon | Kimi | ensemble |")
    md.append("|---|---|---|---|---|")
    for j in ("v8", "v7"):
        for c in ("retour", "temoin"):
            row = [j, c]
            for fo in ("argon", "kimi", "ensemble"):
                sel = [r for r in RJ if r["monde"] == w and r["juge"] == j and r["etiquette"].split("|")[2] == c and (fo == "ensemble" or r["etiquette"].split("|")[1] == fo)]
                pr, n = sum(r["promues"] for r in sel), sum(r["rejeux"] for r in sel)
                row.append(f"{pr}/{n}" + (f" ({pr / n:.4f})" if n else "") + f", {len(sel)} lois")
            md.append("| " + " | ".join(row) + " |")
open(B + "travail/a07-tableaux-v1.md", "w", encoding="utf-8").write("\n".join(md) + "\n")
json.dump(js, open(B + "travail/a07-tableaux-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\n".join(md))
