# Lit, sans les exécuter, les listes COUPLES des scripts de fabrication ; calcule le lieu d'arrivée de chaque couple ;
# rattache chaque hunk du diff unifié (3 lignes de contexte) et chaque bloc du diff normal aux couples.
import ast, sys, re, json, subprocess, hashlib
P = "prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/"
B = "prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon%d.md"
def charge(n, m):
    src = open(P + "couples-brouillon%d-vers-brouillon%d-v1.py" % (n, m), encoding="utf-8").read()
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "COUPLES" for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit("COUPLES introuvable")
def etape(n, m):
    a = open(B % n, encoding="utf-8").read(); b = open(B % m, encoding="utf-8").read()
    C = charge(n, m)
    pos = []
    for c in C:
        ident, av, ap = c[0], c[-2], c[-1]
        assert a.count(av) == 1, ident
        pos.append((a.index(av), c))
    pos.sort(key=lambda x: x[0])
    out = []; cur = 0; res = []
    for p, c in pos:
        av, ap = c[-2], c[-1]
        assert p >= cur, c[0]
        out.append(a[cur:p]); debut = sum(len(x) for x in out)
        out.append(ap); cur = p + len(av)
        res.append(dict(id=c[0], meta=list(c[1:-2]), l_dep=a.count("\n", 0, p) + 1,
                        l_dep_fin=a.count("\n", 0, p + max(len(av) - 1, 0)) + 1, deb=debut, fin=debut + len(ap), av=av, ap=ap))
    out.append(a[cur:]); r = "".join(out)
    egal = (r == b)
    for d in res:
        d["l_arr"] = r.count("\n", 0, d["deb"]) + 1
        d["l_arr_fin"] = r.count("\n", 0, max(d["fin"] - 1, d["deb"])) + 1
    return a, b, res, egal
def hunks(n, m, opt):
    t = subprocess.run(["diff", opt, B % n, B % m], capture_output=True, text=True).stdout
    H = []
    for mm in re.finditer(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", t, re.M):
        s2 = int(mm.group(3)); l2 = int(mm.group(4)) if mm.group(4) is not None else 1
        s1 = int(mm.group(1)); l1 = int(mm.group(2)) if mm.group(2) is not None else 1
        H.append((s1, l1, s2, l2))
    return H
if __name__ == "__main__":
    tout = {}
    for n, m in ((3, 4), (4, 5), (5, 6)):
        a, b, res, egal = etape(n, m)
        print("=== %d -> %d : couples %d ; reconstruction égale au brouillon d'arrivée : %s" % (n, m, len(res), egal))
        H0 = hunks(n, m, "-U0"); H3 = hunks(n, m, "-U3")
        print("hunks sans contexte : %d ; hunks à 3 lignes de contexte : %d" % (len(H0), len(H3)))
        # rattachement des hunks sans contexte aux couples (par lignes d'arrivée ; suppression pure : ligne d'arrivée voisine)
        for d in res: d["h0"] = []; d["h3"] = []
        orph = []
        for i, (s1, l1, s2, l2) in enumerate(H0, 1):
            lo, hi = (s2, s2 + l2 - 1) if l2 else (s2, s2 + 1)
            ks = [d for d in res if not (d["l_arr_fin"] < lo or d["l_arr"] > hi)]
            if not ks: orph.append((i, s1, l1, s2, l2))
            for d in ks: d["h0"].append(i)
        for i, (s1, l1, s2, l2) in enumerate(H3, 1):
            for d in res:
                if not (d["l_arr_fin"] < s2 or d["l_arr"] > s2 + l2 - 1): d["h3"].append(i)
        print("hunks sans contexte sans couple :", orph)
        print("couples sans hunk :", [d["id"] for d in res if not d["h0"]])
        for d in res:
            print("%s | %s | départ %d-%d | arrivée %d-%d | hunks U3 %s | U0 %s | av %d car. ap %d car." % (
                d["id"], " | ".join(map(str, d["meta"])), d["l_dep"], d["l_dep_fin"], d["l_arr"], d["l_arr_fin"], d["h3"], d["h0"], len(d["av"]), len(d["ap"])))
        tout["%d-%d" % (n, m)] = res
    json.dump(tout, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=0)
