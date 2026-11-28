import sys, copy, json
W = sys.argv[1]
sys.argv = [sys.argv[0], W]
exec(compile(open(W + "/sondes_juge.py").read().split("# 1. lecteur étendu")[0], "entete", "exec"))
src = complet(tl._source(0, n_taches=20)); lec = lire(src)
for nom, m, g in (("a", A, GA), ("b", B, GB)):
    s2, l2 = copy.deepcopy(src), copy.deepcopy(lec)
    m.analyser_addendum(s2, l2, g)
    ok_l = l2 == lec
    ok_t = all(np.array_equal(src["tables"][k], s2["tables"][k], equal_nan=src["tables"][k].dtype.kind == "f") for k in src["tables"])
    ok_j = all(np.array_equal(src["jetons"][k], s2["jetons"][k], equal_nan=src["jetons"][k].dtype.kind == "f") for k in src["jetons"])
    ok_x = s2["textes"] == src["textes"] and s2["episodes-p3"] == src["episodes-p3"] and s2["sondes-figees"] == src["sondes-figees"]
    print(nom, "lecture intacte", ok_l, "tables", ok_t, "jetons", ok_j, "textes, fiches, sondes figées", ok_x, "clés ajoutées", sorted(set(s2) - set(src)))
