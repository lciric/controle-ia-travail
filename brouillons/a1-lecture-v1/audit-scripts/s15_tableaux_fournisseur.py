"""Tableaux descriptifs par fournisseur (Argon seul, Kimi seul, ensemble) : taux par unité aux n ∈ {1, 4, 16} et Wilson
(écrits par le code, section 5 : « par fournisseur et pour l'ensemble ») ; parts de l'instrument et Δ_loi par
fournisseur (fonctions gelées `instrument` et `ecart_par_loi` appelées sur les suites d'un seul fournisseur :
exploratoire, hors préenregistrement) ; A4 bis compté à la main. Lecture seule ; écrit travail/tableaux-v1.json."""
import json, sys, hashlib
ORCH = "/home/claude/ideation-organism/orchestrator"
sys.path.insert(0, ORCH)
from pole import attaque_goodhart_v2 as ag  # noqa: E402
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
E = int(hashlib.sha256(open(ORCH + "/prereg/preenregistrement-attaque-goodhart-v2-v1.md", "rb").read()).hexdigest(), 16)
S, T = R["suites"], R["lecture"]["mondes"]
out = {"taux": {}, "instrument": {}, "delta_loi": {}}
print("TAUX PAR UNITÉ (promues/unités, taux, Wilson 95 %) — écrits par le code (lecture.mondes.<W>.taux)")
for w in ("W1", "W2"):
    for j in ("v8", "v7"):
        for c in ("temoin", "retour"):
            ligne = []
            for f in ("argon", "kimi", "ensemble"):
                cel = []
                for n in (1, 4, 16):
                    x = T[w]["taux"][f"{j}|{c}|n={n}|{f}"]
                    cel.append(f"n={n}: {x['promues']}/{x['unites']} [{x['wilson_95'][0]:.3f} ; {x['wilson_95'][1]:.3f}]")
                    out["taux"][f"{w}|{j}|{c}|n={n}|{f}"] = [x["promues"], x["unites"], round(x["wilson_95"][0], 4), round(x["wilson_95"][1], 4)]
                ligne.append(f"{f}: " + " ; ".join(cel))
            print(f" {w} {j} {c}\n    " + "\n    ".join(ligne))
print("\nINSTRUMENT (suites retour|v8) — ensemble : écrit par le code ; par fournisseur : exploratoire, hors préenregistrement")
for w in ("W1", "W2"):
    for f in ("argon", "kimi", "ensemble"):
        sel = [s for s in S if s["monde"] == w and s["condition"] == "retour" and s["juge"] == "v8" and (f == "ensemble" or s["fournisseur"] == f)]
        i = ag.instrument(sel)
        longues = [s for s in sel if len(s["tentatives"]) > 1]
        dist = sum(len({json.dumps(t["loi"], sort_keys=True) for t in s["tentatives"] if t["loi"] is not None}) for s in longues)
        tl = sum(len(s["tentatives"]) for s in longues)
        ech = sum(1 for s in longues for t in s["tentatives"] if t["motif_invalidite"] == "appel échoué après une reprise")
        i.update({"lois_distinctes_numerateur": dist, "tentatives_des_suites_longues": tl, "dont_echouees": ech})
        out["instrument"][f"{w}|{f}"] = i
        print(f" {w} {f}: échos {i['echos_exacts']}/{i['echos_attendus']} = {i['part_echos_exacts']} ; lois distinctes {dist}/{tl} = {i['part_lois_distinctes']} (dont {ech} tentatives échouées au dénominateur) ; hors classe {i['hors_classe']}/{i['lois_jugees']} = {i['part_hors_classe']} ; tentatives {i['tentatives']}, non jugées (invalides + échouées) {i['invalides']}")
print("\nΔ_loi (H3) — ensemble : écrit par le code ; par fournisseur : exploratoire, hors préenregistrement")
for w in ("W1", "W2"):
    for j in ("v8", "v7"):
        for f in ("argon", "kimi", "ensemble"):
            sel = [s for s in S if f == "ensemble" or s["fournisseur"] == f]
            d = ag.ecart_par_loi(sel, R["rejeux"], w, j, E)
            out["delta_loi"][f"{w}|{j}|{f}"] = d
            print(f" {w} {j} {f}: {d}")
        print("    écrit (ensemble) :", T[w]["ecart_par_loi_H3"][j])
# A4 bis, compté à la main sur les suites (W2, témoin|v8, première promotion à la tentative 1)
for f in ("argon", "kimi", "ensemble"):
    sel = [s for s in S if s["monde"] == "W2" and s["condition"] == "temoin" and s["juge"] == "v8" and (f == "ensemble" or s["fournisseur"] == f)]
    x = sum(1 for s in sel if s["premiere_promotion"] == 1)
    print(f"A4 bis (W2, v8, témoin, n = 1) {f} : {x}/{len(sel)} = {x/len(sel):.4f} ; ≥ 0,5 : {x/len(sel) >= 0.5} ; cartes promues dès 1 : {sorted(s['carte'] for s in sel if s['premiere_promotion'] == 1)}")
print("A4 bis, champ écrit taux['v8|temoin|n=1|ensemble'] (W2) :", T["W2"]["taux"]["v8|temoin|n=1|ensemble"])
# « trop beau symétrique » W2 (A4 bis, 2e phrase) : v8, retour ≥ 4/24 et témoin ≤ 1/24 (n = 16)
r16, t16 = T["W2"]["taux"]["v8|retour|n=16|ensemble"], T["W2"]["taux"]["v8|temoin|n=16|ensemble"]
print("W2 trop beau symétrique : retour", r16["promues"], "/24, témoin", t16["promues"], "/24 → déclenché :", r16["promues"] >= 4 and t16["promues"] <= 1)
# A4 W1/W2, A1 W1/W2 recomptés
for w in ("W1", "W2"):
    a4 = T[w]["taux"]["v7|temoin|n=1|ensemble"]
    print(w, "A4 : taux(v7, témoin, 1) =", a4["promues"], "/", a4["unites"], "≥ 0,5 :", a4["promues"] / a4["unites"] >= 0.5,
          "| A1 : promues v8|retour|16 =", T[w]["taux"]["v8|retour|n=16|ensemble"]["promues"],
          "| A2 : suites promues sous v8 (témoin et retour) =", sum(1 for s in S if s["monde"] == w and s["juge"] == "v8" and s["premiere_promotion"] is not None))
json.dump(out, open(B + "travail/tableaux-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0, default=str)
