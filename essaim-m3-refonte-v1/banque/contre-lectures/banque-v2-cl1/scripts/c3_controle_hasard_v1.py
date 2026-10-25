"""Contre-lecture banque v2 — c3 : le contrôle des 50 règles, réécrit ici, validé contre les sorties scellées, puis situé
sous le hasard et mis à l'épreuve de fuites partielles.

1. Réimplémentation indépendante des 50 règles par famille (49 catégorielles + 1 à seuil) décrites au docstring de
   `verifier_identifiants_opaques_v1.py` ; comparaison aux sorties scellées v1 et v2 (meilleures, max).
2. Hasard, deux constructions : (a) identifiants tirés comme le constructeur (permutation uniforme des 200 numéros) ;
   (b) identifiants v2 fixes, vérités permutées dans chaque (part, famille). Statistiques : max sur les règles de
   l'exactitude équilibrée sur test, sur test_final, du min des deux ; part des tirages avec une règle « prédictive »
   (>= 0,80 sur les deux parts).
3. Puissance : fuite partielle de force q (suffixe -a / -b égal au code de la vérité avec probabilité q, dans les trois
   parts, famille délégation) ; part des tirages où le contrôle refuse.
Graines : SeedSequence(20261025_01), (…_02), (…_03) consignées ici.
Usage : python3 -I c3_controle_hasard_v1.py DOSSIER_BANQUE DOSSIER_CONSTRUCTION [N]
"""
import json
import pathlib
import sys

import numpy as np

PARTS = ("train", "test", "test_final")
SEUIL = 0.80


def ex_eq(pred, vrai, pos):
    tp = tn = npos = 0
    for p, v in zip(pred, vrai):
        if v == pos:
            npos += 1
            tp += p == pos
        else:
            tn += p != pos
    nneg = len(vrai) - npos
    return ((tp / npos if npos else 0.0) + (tn / nneg if nneg else 0.0)) / 2


def nombre(s):
    d = "".join(c for c in s if c.isdigit())
    return int(d) if d else None


def traits(s):
    f = {}
    for k in (1, 2, 3):
        f[f"suffixe_{k}"] = s[-k:]
    for k in range(1, 7):
        f[f"prefixe_{k}"] = s[:k]
    for i in range(24):
        f[f"caractere_{i:02d}"] = s[i] if i < len(s) else ""
    f["longueur"] = len(s)
    seg = s.split("-")
    f["segment_premier"], f["segment_dernier"] = seg[0], seg[-1]
    for j in range(4):
        f[f"segment_{j}"] = seg[j] if j < len(seg) else ""
    n = nombre(s)
    for m in range(2, 11):
        f[f"nombre_mod_{m}"] = None if n is None else n % m
    return f


NOMS = sorted(traits("t-0001"))
assert len(NOMS) == 49


def regle_cat(vals, ys, etiq):
    c = {}
    for v, y in zip(vals, ys):
        c.setdefault(v, {e: 0 for e in etiq})[y] += 1
    tot = {e: ys.count(e) for e in etiq}
    defaut = max(etiq, key=lambda e: (tot[e], -etiq.index(e)))
    table = {v: max(etiq, key=lambda e: (cc[e], -etiq.index(e))) for v, cc in c.items()}
    return lambda v: table.get(v, defaut)


def regle_seuil(vals, ys, pos, neg):
    vus = sorted({v for v in vals if v is not None})
    if not vus:
        return None
    cands = [vus[0] - 0.5] + [(a + b) / 2 for a, b in zip(vus, vus[1:])] + [vus[-1] + 0.5]
    best = (-1.0, None)
    for s in cands:
        for sens in (1, -1):
            e = ex_eq([pos if (v is not None and (v - s) * sens > 0) else neg for v in vals], ys, pos)
            if e > best[0]:
                best = (e, (s, sens))
    s, sens = best[1]
    return lambda v: pos if (v is not None and (v - s) * sens > 0) else neg


def evaluer(parts):
    """parts : {part: [(id, famille, verite)]} -> {famille: [(regle, ex_test, ex_test_final)]}"""
    sortie = {}
    for fam in sorted({f for _, f, _ in parts["train"]}):
        etiq = ["sabotage", "honnete"] if fam == "controle-delegation" else ["evaluation", "usage-reel"]
        pos, neg = etiq
        tr = [(i, y) for i, f, y in parts["train"] if f == fam]
        te = {p: [(i, y) for i, f, y in parts[p] if f == fam] for p in ("test", "test_final")}
        ftr = [traits(i) for i, _ in tr]
        fte = {p: [traits(i) for i, _ in te[p]] for p in te}
        ytr = [y for _, y in tr]
        res = []
        for nom in NOMS:
            r = regle_cat([x[nom] for x in ftr], ytr, etiq)
            res.append((nom, *(ex_eq([r(x[nom]) for x in fte[p]], [y for _, y in te[p]], pos) for p in ("test", "test_final"))))
        r = regle_seuil([nombre(i) for i, _ in tr], ytr, pos, neg)
        if r is not None:
            res.append(("nombre_seuil", *(ex_eq([r(nombre(i)) for i, _ in te[p]], [y for _, y in te[p]], pos) for p in ("test", "test_final"))))
        sortie[fam] = res
    return sortie


def resume(res):
    return {fam: {"n_regles": len(r), "max_test": round(max(x[1] for x in r), 4), "max_test_final": round(max(x[2] for x in r), 4),
                  "max_min": round(max(min(x[1], x[2]) for x in r), 4),
                  "predictives": sum(1 for x in r if x[1] >= SEUIL and x[2] >= SEUIL),
                  "une_part": sum(1 for x in r if max(x[1], x[2]) >= SEUIL)} for fam, r in res.items()}


def parts_de(b):
    return {p: [(t["id"], t["famille"], t["verite"]) for t in b[p]] for p in PARTS}


def main(dossier, construction, N):
    d = pathlib.Path(dossier)
    v1 = json.loads((d / "banque-confrontation-v1.json").read_text(encoding="utf-8"))
    v2 = json.loads((d / "banque-confrontation-v2.json").read_text(encoding="utf-8"))
    sc = {k: json.loads((pathlib.Path(construction) / f"controle-identifiants-banque-{k}-v1.json").read_text(encoding="utf-8")) for k in ("v1", "v2")}
    print("1. Réimplémentation contre sorties scellées")
    for k, b in (("v1", v1), ("v2", v2)):
        mien = resume(evaluer(parts_de(b)))
        for fam, m in mien.items():
            s = sc[k]["regles"][fam]
            ok = (m["n_regles"] == s["n_regles"] and m["max_test"] == s["max_test"] and m["max_test_final"] == s["max_test_final"]
                  and m["predictives"] == len(s["predictives"]))
            print(f"   {k} {fam:22s} mien {m}  scellé max {s['max_test']}/{s['max_test_final']} prédictives {len(s['predictives'])}  -> {'conforme' if ok else 'ÉCART'}")
    obs = resume(evaluer(parts_de(v2)))

    # 2a. hasard du constructeur
    print(f"\n2a. Hasard du constructeur (permutation uniforme des numéros), N={N}, SeedSequence(2026102501)")
    rng = np.random.default_rng(np.random.SeedSequence(2026102501))
    base = [(p, t["famille"], t["verite"]) for p in PARTS for t in v2[p]]
    stats = {f: {"max_test": [], "max_test_final": [], "max_min": [], "pred": [], "une_part": []} for f in ("conscience-evaluation", "controle-delegation")}
    refus_global = 0
    for _ in range(N):
        perm = rng.permutation(200)
        parts = {p: [] for p in PARTS}
        for k, (p, f, y) in enumerate(base):
            parts[p].append((f"t-{int(perm[k]) + 1:04d}", f, y))
        r = resume(evaluer(parts))
        refus_global += any(r[f]["predictives"] for f in r)
        for f in r:
            stats[f]["max_test"].append(r[f]["max_test"]); stats[f]["max_test_final"].append(r[f]["max_test_final"])
            stats[f]["max_min"].append(r[f]["max_min"]); stats[f]["pred"].append(r[f]["predictives"] > 0); stats[f]["une_part"].append(r[f]["une_part"] > 0)
    for f, s in stats.items():
        o = obs[f]
        q = {k: [round(float(np.quantile(s[k], x)), 4) for x in (0.05, 0.5, 0.95, 0.99)] for k in ("max_test", "max_test_final", "max_min")}
        pv = {k: round(float(np.mean(np.array(s[k]) >= o[k])), 4) for k in ("max_test", "max_test_final", "max_min")}
        print(f"   {f}: observé v2 {o['max_test']}/{o['max_test_final']}/min {o['max_min']} ; quantiles 5/50/95/99 % {q}")
        print(f"      part des tirages >= observé (valeur p) {pv} ; part refusée (>= 0,80 sur les deux) {np.mean(s['pred']):.4f} ;"
              f" >= 0,80 sur au moins une part {np.mean(s['une_part']):.4f}")
    print(f"   banque refusée (une famille au moins) : {refus_global / N:.4f}")

    # 2b. vérités permutées, identifiants v2 fixes
    print(f"\n2b. Vérités permutées dans chaque (part, famille), identifiants v2 fixes, N={N}, SeedSequence(2026102502)")
    rng = np.random.default_rng(np.random.SeedSequence(2026102502))
    fixes = parts_de(v2)
    stats_b = {f: {"max_test": [], "max_test_final": [], "max_min": []} for f in stats}
    for _ in range(N):
        parts = {}
        for p in PARTS:
            l = list(fixes[p])
            for f in stats:
                idx = [k for k, x in enumerate(l) if x[1] == f]
                ys = [l[k][2] for k in idx]
                ys = [ys[int(j)] for j in rng.permutation(len(ys))]
                for k, y in zip(idx, ys):
                    l[k] = (l[k][0], f, y)
            parts[p] = l
        r = resume(evaluer(parts))
        for f in r:
            for k in stats_b[f]:
                stats_b[f][k].append(r[f][k])
    for f, s in stats_b.items():
        o = obs[f]
        pv = {k: round(float(np.mean(np.array(s[k]) >= o[k])), 4) for k in s}
        q = {k: [round(float(np.quantile(s[k], x)), 4) for x in (0.05, 0.5, 0.95)] for k in s}
        print(f"   {f}: quantiles 5/50/95 % {q} ; valeur p de l'observé {pv}")

    # 3. puissance contre une fuite partielle (délégation)
    print(f"\n3. Fuite partielle de force q (délégation, trois parts), N={max(200, N // 4)} par q, SeedSequence(2026102503)")
    rng = np.random.default_rng(np.random.SeedSequence(2026102503))
    for q in (0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95):
        refus, bas = 0, []
        n_q = max(200, N // 4)
        for _ in range(n_q):
            parts = {}
            for p in PARTS:
                l = []
                for i, f, y in fixes[p]:
                    if f == "controle-delegation":
                        bon = rng.random() < q
                        code = ("a" if y == "sabotage" else "b") if bon else ("b" if y == "sabotage" else "a")
                        i = f"{i}-{code}"
                    l.append((i, f, y))
                parts[p] = l
            r = resume(evaluer(parts))["controle-delegation"]
            refus += r["predictives"] > 0
            bas.append(r["max_min"])
        print(f"   q={q:.2f} : contrôle refuse dans {refus / n_q:.3f} des tirages ; médiane du min(test, test_final) de la meilleure règle {np.median(bas):.4f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 2000)
