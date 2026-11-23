"""Controle independant du contre-lecteur : couverture de la liste finie, parametres, graines, seuils, taux, depassements.
N'importe aucun programme de l'agent."""
import json, math, os, re, sys, glob
V2 = sys.argv[1]
liste = open(os.path.join(V2, "entrees/liste-finie-cases-grille-v1.md"), encoding="utf-8").read()
rows = []
for l in liste.splitlines():
    m = re.match(r"^\| (\d{3}) \| (\w+) \| ([\d,]+) \| (\d) \| (\d+) \| ([^|]+) \| (oui|non) \| ([^|]+) \| ([^|]+) \| (oui|non) \|", l)
    if m:
        rows.append(dict(case=int(m[1]), modele=m[2], g=float(m[3].replace(",", ".")), k=int(m[4]), T=int(m[5]),
                         ab_eff=m[6].strip(), ab_jouee=m[7], c_R=m[8].strip(), bras=m[9].strip(), c_jouee=m[10]))
assert len(rows) == 144, len(rows)
assert [r["case"] for r in rows] == list(range(1, 145))
MOD = ["E30", "E40", "E60", "EH", "K16", "KH", "MH", "M616"]
JUGES = {"E30": [(.3, .3, 0)] * 3, "E40": [(.4, .4, 0)] * 3, "E60": [(.6, .6, 0)] * 3, "EH": [(.3, .3, 0), (.45, .45, 0), (.6, .6, 0)],
         "K16": [(0, .4, .16)] * 3, "KH": [(0, .4, .04), (0, .4, .10), (0, .4, .16)],
         "MH": [(.6, .6, 0), (.4, .4, .08), (0, .4, .16)], "M616": [(.6, .6, .16)] * 3}
ATT = {0.0: "g00", 0.10: "g10", 0.20: "g20"}
# la liste est-elle le produit complet 8 x 3 x 2 x 3 ?
assert {(r["modele"], r["g"], r["k"], r["T"]) for r in rows} == {(m, g, k, T) for m in MOD for g in ATT for k in (3, 5) for T in (30, 45, 60)}
seuil = lambda R: 0.05 + 2 * math.sqrt(0.05 * 0.95 / R)
pb = []
res = {"a": [], "b": [], "ci": [], "cc": []}
orig = {"ab": {"v1": 0, "v2": 0}, "c": {"v1": 0, "v2": 0}}
ctl = {}
for r in rows:
    att = ATT[r["g"]]
    nom = f"{r['modele']}_{att}_k{r['k']}_T{r['T']}_p0"
    for ty, prog in (("ab", 1), ("c", 2)):
        found = [(d, p) for d in ("reprises-v1", "neuves-v2") for p in [os.path.join(V2, "sorties", d, f"{ty}_{nom}.json")] if os.path.exists(p)]
        if len(found) != 1:
            pb.append(f"case {r['case']:03d} {ty} : {len(found)} sortie(s)"); continue
        d, p = found[0]
        o = json.load(open(p, encoding="utf-8"))
        origine = "v1" if d == "reprises-v1" else "v2"
        orig[ty][origine] += 1
        jouee = r["ab_jouee"] if ty == "ab" else r["c_jouee"]
        if (jouee == "oui") != (origine == "v1"): pb.append(f"case {r['case']:03d} {ty} : origine {origine} contre colonne jouee = {jouee}")
        Rv = 1000 if ty == "ab" else 8000
        if o["R"] != Rv: pb.append(f"{nom} {ty} R={o['R']}")
        if ty == "ab" and o["B"] != 1000: pb.append(f"{nom} B={o['B']}")
        if (o["modele"], o["attaque"], o["k"], o["T"], o["passe"]) != (r["modele"], att, r["k"], r["T"], 0): pb.append(f"{nom} {ty} parametres")
        if [tuple(j) for j in o["juges"]] != [tuple(map(float, j)) for j in JUGES[r["modele"]]]: pb.append(f"{nom} {ty} juges {o['juges']}")
        if o["g"] != [r["g"]] * 3: pb.append(f"{nom} {ty} g {o['g']}")
        codeT = {45: 0, 60: 1, 30: 2}[r["T"]]
        ident = MOD.index(r["modele"]) * 1000 + list(ATT.values()).index(att) * 100 + r["k"] * 10 + codeT
        if o["graine"] != {"entropie": 20261119, "spawn_key": [prog, ident, 0]}: pb.append(f"{nom} {ty} graine {o['graine']}")
        if abs(o["seuil_clause"] - seuil(Rv)) > 1e-12: pb.append(f"{nom} {ty} seuil")
        if o["versions"]["numpy"] != "2.5.3": pb.append(f"{nom} {ty} numpy {o['versions']}")
        progn = o["programme"]
        if progn != f"grille_{ty}_{origine}.py": pb.append(f"{nom} {ty} programme {progn}")
        err = p[:-5] + ".err"
        if origine == "v2" and (not os.path.exists(err) or os.path.getsize(err) != 0): pb.append(f"{nom} {ty} err")
        if ty == "ab":
            res["a"].append((o["taux"]["conj3_a"], r["case"], nom, origine)); res["b"].append((o["taux"]["conj3_b"], r["case"], nom, origine))
            if origine == "v2": 
                for kx, vx in o["essais_controles"].items(): ctl[kx] = ctl.get(kx, 0) + vx
        else:
            ti = o["taux"]["insertion_kP3_lie|conj3"]; tc = o["taux"]["contenu_kP3_lie|conj3"]
            res["ci"].append((ti, r["case"], nom, origine))
            attendu_c = "C" in r["bras"]
            if attendu_c != (tc is not None): pb.append(f"{nom} bras contenu defini={tc is not None} liste={r['bras']}")
            if tc is not None: res["cc"].append((tc, r["case"], nom, origine))
            ctl["ex_aequo_" + origine] = ctl.get("ex_aequo_" + origine, 0) + o["essais_avec_ex_aequo"]
            if origine == "v2":
                ctl["D0"] = ctl.get("D0", 0) + o["essais_D0_non_positif"]; ctl["c_non_fini"] = ctl.get("c_non_fini", 0) + o["essais_G_non_fini"]
# sorties hors liste ?
attendues = {f"{ty}_{r['modele']}_{ATT[r['g']]}_k{r['k']}_T{r['T']}_p0.json" for r in rows for ty in ("ab", "c")}
for d in ("reprises-v1", "neuves-v2"):
    for p in glob.glob(os.path.join(V2, "sorties", d, "*.json")):
        if os.path.basename(p) not in attendues: pb.append("hors liste : " + p)
print("problemes :", pb if pb else "aucun")
print("origines :", orig, "| controles cases neuves :", ctl)
graines = set()
for nomr, R in (("a", 1000), ("b", 1000), ("ci", 8000), ("cc", 8000)):
    L = res[nomr]; s = seuil(R); au = sorted(c for (t, c, n, o) in L if t > s)
    mx = max(L); 
    print(f"{nomr}: n={len(L)} seuil={s:.6f} max={mx[0]:.4f} case {mx[1]:03d} ({mx[2]}, {mx[3]}) au-dessus={len(au)}", "neuves au-dessus=%d reprises au-dessus=%d" % (sum(1 for (t, c, n, o) in L if t > s and o == "v2"), sum(1 for (t, c, n, o) in L if t > s and o == "v1")))
    if nomr in ("ci", "cc"): print("   cases :", au)
    if nomr in ("a", "b"): print("   cinq plus hauts :", [(round(t, 4), c, o) for (t, c, n, o) in sorted(L, reverse=True)[:5]], "| a moins de 2 erreurs MC du seuil :", [(c, t) for (t, c, n, o) in L if t + 2 * math.sqrt(t * (1 - t) / R) >= s])
print("C-P3c cases distinctes avec un bras au-dessus :", len({c for nomr in ("ci", "cc") for (t, c, n, o) in res[nomr] if t > seuil(8000)}))
json.dump({k: sorted((c, t) for (t, c, n, o) in v) for k, v in res.items()}, open(os.path.join(os.path.dirname(__file__), "taux-independants.json"), "w"))
