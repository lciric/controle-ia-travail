"""Résumé par programme des sorties brutes v1 et v2 de la simulation de la chaîne de l'oracle révisé (aucune donnée du programme).
Usage : python3 resumer-sorties-simulation-chaine-oracle-revise-v1.py SORTIE_V1 SORTIE_V2 ; écrit sur la sortie standard."""
import collections
import sys


def blocs(chemin):
    L = open(chemin).read().split("\n")
    out, k = {}, 0
    while k < len(L):
        if L[k].startswith("# ") and k + 1 < len(L) and "\t" in L[k + 1]:
            nom, ent, rows, j = L[k][2], L[k + 1].split("\t"), [], k + 2
            while j < len(L) and L[j].strip() and not L[j].startswith("#"):
                rows.append(dict(zip(ent, L[j].split("\t"))))
                j += 1
            out[nom] = (ent, rows)
            k = j
        else:
            k += 1
    return out, L


def stat(rs, c):
    v = [float(r[c]) for r in rs]
    return f"max {max(v):.3f} moy {sum(v) / len(v):.3f} min {min(v):.3f}"


v1, L1 = blocs(sys.argv[1])
v2, L2 = blocs(sys.argv[2])
print("entetes :", L1[0], "|", L2[0])
print("\n== 1. v1, bloc A : oracle sain, niveau 1/60 par composante, composantes nues ==")
ent, rows = v1["A"]
groupes = [("hors couplage (280 cellules, echangeables par construction)", lambda r: not r["profil"].startswith("P5")),
           ("couplage par le prefixe (56 cellules)", lambda r: r["profil"].startswith("P5"))]
for nom, sel in groupes:
    rs = [r for r in rows if sel(r)]
    print(nom, len(rs))
    for c in ["T0_v1"] + [c for c in ent if c.endswith("@0.0167")]:
        print(f"   {c:40s} {stat(rs, c)}")
print("   derive de l'oracle v1 (moyenne de e au pas 9 moins au pas 0), hors couplage :",
      "max %.3f" % max(float(r["moy_e_v1_pas9"]) - float(r["moy_e_v1_pas0"]) for r in rows if not r["profil"].startswith("P5")),
      "; oracle hors_K : max abs %.3f" % max(abs(float(r["moy_e_horsK_pas9"]) - float(r["moy_e_horsK_pas0"])) for r in rows if not r["profil"].startswith("P5")))
print("\n== 2. v2, bloc A : oracle sain, avec clause de materialite ==")
ent, rows = v2["A"]
for nom, sel in groupes:
    rs = [r for r in rows if sel(r)]
    print(nom, len(rs))
    for c in ent[4:40]:
        print(f"   {c:48s} {stat(rs, c)}")
rs = [r for r in rows if r["profil"].startswith("P5")]
print("   couplage : cellules ou batterie[hors_K] > 0,10 :")
for r in rs:
    if float(r["batterie(TA|TL|TB2_clause)[hors_K]"]) > 0.10:
        print("     ", r["sigma"], r["rho"], r["ancre"], "batterie", r["batterie(TA|TL|TB2_clause)[hors_K]"], "TB2 nue", r["TB2_nue[hors_K]"],
              "e pas0", r["moy_e_hors_K_pas0"], "e pas9", r["moy_e_hors_K_pas9"])
print("\n   D3 (oracle v1 juge par la composante de chaine avec clause), par dispersion et ancrage, profil de reference, ancre dernier / maximum :")
for a in ("dernier", "maximum"):
    for rho in ("0.0", "0.5", "0.9", "1.0"):
        rs = [r for r in rows if r["profil"].startswith("P0") and r["ancre"] == a and r["rho"] == rho]
        print(f"     {a} rho={rho} :", " ".join(f"s{r['sigma']}:{r['TB2_clause[v1]']}" for r in rs))


def puissance(ent, rows, cols, titre):
    print(titre)
    d = collections.defaultdict(list)
    for r in rows:
        d[(r["defaut"], r["dimension"], r["episodes"], r["sigma"])].append(r)
    cur = None
    for (df, dim, ne, s), rs in d.items():
        if (df, dim, ne) != cur:
            cur = (df, dim, ne)
            print(f"  {df} | {dim} | {ne} episodes")
        print(f"     sigma={s} : " + " ; ".join(f"{n} {sum(float(r[c]) for r in rs) / len(rs):.2f} (min {min(float(r[c]) for r in rs):.2f})" for n, c in cols))


print("\n== 3. v1, bloc B : puissance des composantes nues (moyenne et minimum sur ancrage 0,5 et 0,9, deux ancres, deux profils) ==")
ent, rows = v1["B"]
puissance(ent, rows, [("rangs", "TA@0.0167"), ("lisibilite", "TL@0.0167"), ("chaine nue", "TB2@0.0167"), ("batterie nue", "batterie@0.0167")], "")
print("\n== 4. v2, bloc B : puissance avec clause de materialite ==")
ent, rows = v2["B"]
cols2 = [("rangs", "TA"), ("chaine+clause", "TB2_clause[hors_K]"), ("batterie", "batterie(TA|TL|TB2_clause)[hors_K]"),
         ("batterie parmi_K_libre", "batterie(TA|TL|TB2_clause)[parmi_K_libre]")]
puissance(ent, rows, cols2, "")
print("\n== 5. v2, bloc C : nombre d'episodes honnetes ==")
ent, rows = v2["C"]
puissance(ent, rows, cols2, "")
print("\n== 5 bis. v1, bloc C (composantes nues ; D2 et D6) ==")
ent, rows = v1["C"]
puissance(ent, [r for r in rows if r["defaut"][:2] in ("D2", "D6")], [("rangs", "TA@0.0167"), ("lisibilite", "TL@0.0167"), ("batterie nue", "batterie@0.0167")], "")
print("\n== 6. v2, bloc D : autres epreuves et regle, par etat et oracle (moyenne ; min ; max sur les cellules) ==")
ent, rows = v2["D"]
d = collections.defaultdict(list)
for r in rows:
    d[(r["etat"], r["sigma"], r["oracle"])].append(r)
cols = ["taux_honnete", "P(E-O3 passe)", "taux_modere", "taux_flagrant", "P(E-O4 passe)", "P(E-O2 passe)", "P(E-O6 passe)", "ecart_type_e_honnete",
        "effet_min_detectable_lecture1"]
print("etat\tsigma\toracle\t" + "\t".join(cols))
for (e, s, o), rs in d.items():
    print(f"{e}\t{s}\t{o}\t" + "\t".join(f"{sum(float(r[c]) for r in rs) / len(rs):.3f}" for c in cols))
print("\n   cellules ou une epreuve passe plus souvent (de plus de 0,05) avec un oracle revise qu'avec l'oracle v1, etat en defaut :")
par = collections.defaultdict(dict)
for r in rows:
    par[(r["sigma"], r["rho"], r["ancre"], r["profil"], r["etat"])][r["oracle"]] = r
n = collections.Counter()
for cle, o in par.items():
    if cle[4] == "sain":
        continue
    for ep in ("P(E-O2 passe)", "P(E-O3 passe)", "P(E-O4 passe)", "P(E-O6 passe)"):
        for rev in ("hors_K", "parmi_K_libre"):
            n[(ep, rev, "cellules")] += 1
            if float(o[rev][ep]) > float(o["v1"][ep]) + 0.05:
                n[(ep, rev, "plus facile")] += 1
                if rev == "hors_K":
                    print("     ", ep, *cle, "v1", o["v1"][ep], "hors_K", o[rev][ep])
for k_, v in sorted(n.items()):
    print("   ", k_, v)
print("\n== 7. v1, bloc E : lois exactes contre approximation normale ==")
k = [i for i, l in enumerate(L1) if l.startswith("# E")][0]
print("\n".join(L1[k + 1:]))
