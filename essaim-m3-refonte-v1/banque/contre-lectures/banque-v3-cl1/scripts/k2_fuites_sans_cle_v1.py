"""Contre-lecture banque v3 — k2 : fuites restantes sans la clé (identifiant, ordre, manifeste, source, amorçage),
situées par rapport au hasard (permutations), et règles hors des familles du contrôle.

Code à moi (je ne réutilise pas celui du contrôle). Le fichier secret ne sert qu'à nommer les paires (équivalent à
l'appariement par les textes, montré parfait en k4) et à décrire la consigne d'amorçage. Ne lit pas la clé.
Usage : python3 -I k2_fuites_sans_cle_v1.py BANQUE_V3 SECRET_V3 N_TIRAGES
"""
import hashlib
import json
import pathlib
import re
import sys

import numpy as np

PB, PS, N = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), int(sys.argv[3])
PARTS = ("train", "test", "test_final")
b = json.loads(PB.read_text(encoding="utf-8"))
s = json.loads(PS.read_text(encoding="utf-8"))
for _p in PARTS:
    for _t in b[_p]:
        _t["_g"] = s[_t["id"]]["groupe"]  # groupe (paire) porté par la tâche : suit la tâche quand les identifiants sont retirés
out = []


def dire(*a):
    out.append(" ".join(str(x) for x in a))


def num(i):
    d = "".join(c for c in i if c.isdigit())
    return int(d) if d else -1


def feats(i):
    f = {}
    for k in (1, 2, 3):
        f[f"suf{k}"] = i[-k:]
    for k in range(1, 7):
        f[f"pre{k}"] = i[:k]
    for k in range(24):
        f[f"car{k}"] = i[k] if k < len(i) else ""
    f["long"] = len(i)
    sg = i.split("-")
    f["seg_prem"], f["seg_der"] = sg[0], sg[-1]
    for k in range(4):
        f[f"seg{k}"] = sg[k] if k < len(sg) else ""
    n = num(i)
    for m in range(2, 11):
        f[f"mod{m}"] = n % m
    return f


FEATS = {k: feats(f"t-{k:04d}") for k in range(1, 201)}
NOMS = sorted(FEATS[1])


def ee(pred, y):
    pred, y = np.asarray(pred, dtype=bool), np.asarray(y, dtype=bool)
    se = pred[y].mean() if y.any() else 0.0
    sp = (~pred[~y]).mean() if (~y).any() else 0.0
    return (se + sp) / 2


EGAL_POS = [False]  # False : égalités -> classe négative (ma variante) ; True : égalités -> première étiquette (celle du contrôle)


def majorite(vals, y):
    c = {}
    for v, t in zip(vals, y):
        a = c.setdefault(v, [0, 0])
        a[int(t)] += 1
    tot = [sum(1 for t in y if not t), sum(1 for t in y if t)]
    defaut = (tot[1] >= tot[0]) if EGAL_POS[0] else (tot[1] > tot[0])
    r = {v: (a[1] > a[0]) if a[1] != a[0] else (True if EGAL_POS[0] else defaut) for v, a in c.items()}
    return r, defaut


def seuil_au_mieux(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=bool)
    xs = np.unique(x)
    cands = np.concatenate([[xs[0] - 0.5], (xs[:-1] + xs[1:]) / 2, [xs[-1] + 0.5]])
    best, arg = -1, None
    for c in cands:
        for sens in (1, -1):
            v = ee((x - c) * sens > 0, y)
            if v > best:
                best, arg = v, (c, sens)
    return best, arg


def stat_case(nums, ys):
    """nums[p], ys[p] pour une famille ; rend le maximum par part (règles transférées + dans la part)."""
    res = {}
    tr_n, tr_y = nums["train"], ys["train"]
    for p in ("test", "test_final"):
        best = 0
        for nom in NOMS:
            r, d = majorite([FEATS[k][nom] for k in tr_n], tr_y)
            best = max(best, ee([r.get(FEATS[k][nom], d) for k in nums[p]], ys[p]))
        _, (c, sens) = seuil_au_mieux(tr_n, tr_y)
        best = max(best, ee((np.asarray(nums[p]) - c) * sens > 0, ys[p]))
        res[p] = best
    for p in PARTS:
        rg = np.argsort(np.argsort(nums[p], kind="stable"), kind="stable")  # rang du numéro (= rang dans le fichier si trié)
        best = seuil_au_mieux(rg, ys[p])[0]
        for m in (2, 3, 4):
            r, d = majorite(list(rg % m), ys[p])
            best = max(best, ee([r.get(v, d) for v in rg % m], ys[p]))
        res[p] = max(res.get(p, 0), best)
    return res


def knn(nums, ys, k):
    tr = np.asarray(nums["train"]); ytr = np.asarray(ys["train"], dtype=bool)
    o = {}
    for p in ("test", "test_final"):
        pred = []
        for x in nums[p]:
            d = np.abs(tr - x)
            idx = np.lexsort((tr, d))[:k]
            pred.append(ytr[idx].sum() * 2 > k)
        o[p] = ee(pred, ys[p])
    return o


fams = sorted({t["famille"] for t in b["train"]})
POS = {f: next(t["etiquettes"][0] for t in b["train"] if t["famille"] == f) for f in fams}


def vue(bq):
    nums = {f: {p: [num(t["id"]) for t in bq[p] if t["famille"] == f] for p in PARTS} for f in fams}
    ys = {f: {p: [t["verite"] == POS[f] for t in bq[p] if t["famille"] == f] for p in PARTS} for f in fams}
    return nums, ys


def paires(bq, f="controle-delegation"):
    o = {}
    for p in PARTS:
        g = {}
        for t in bq[p]:
            if t["famille"] == f:
                g.setdefault(t["_g"], []).append(t)
        o[p] = [v for v in g.values() if len(v) == 2]
    return o


def regle_paire(pr):
    """« le membre au plus petit numéro est saboté » (sens appris sur les paires d'entraînement) ; part des paires
    bien tranchées (= exactitude équilibrée par trace)."""
    def bas_sabote(pair):
        a, c = pair
        lo = a if num(a["id"]) < num(c["id"]) else c
        return lo["verite"] == "sabotage"
    tr = [bas_sabote(x) for x in pr["train"]]
    sens = sum(tr) >= len(tr) / 2
    return {p: float(np.mean([bas_sabote(x) == sens for x in pr[p]])) for p in PARTS}


def rang_union(nums, ys):
    o = {}
    for f in fams:
        x = nums[f]["test"] + nums[f]["test_final"]
        y = ys[f]["test"] + ys[f]["test_final"]
        o[f] = seuil_au_mieux(np.argsort(np.argsort(x)), y)[0]
    return o


def part_previsible(bq):
    x = [num(t["id"]) for t in bq["test"]] + [num(t["id"]) for t in bq["test_final"]]
    y = [True] * len(bq["test"]) + [False] * len(bq["test_final"])
    best = seuil_au_mieux(x, y)[0]
    for m in range(2, 11):
        r, d = majorite([v % m for v in x], y)
        best = max(best, ee([r.get(v % m, d) for v in x], y))
    return best


nums, ys = vue(b)
obs = {f: stat_case(nums[f], ys[f]) for f in fams}
obs_knn = {f: {k: knn(nums[f], ys[f], k) for k in (1, 3, 5)} for f in fams}
pr = paires(b)
obs_paire = regle_paire(pr)
obs_union = rang_union(nums, ys)
obs_part = part_previsible(b)

EGAL_POS[0] = True
obs_fidele = {f: stat_case(nums[f], ys[f]) for f in fams}
EGAL_POS[0] = False
dire("1. Maxima observés sur la v3 (ma réimplémentation des règles du contrôle v2)")
for f in fams:
    dire(f"   {f} : égalités comme le contrôle (première étiquette) : " + " ; ".join(f"{p} {obs_fidele[f][p]:.4f}" for p in PARTS)
         + " || ma variante (égalités -> seconde étiquette) : " + " ; ".join(f"{p} {obs[f][p]:.4f}" for p in PARTS))
dire("   règles hors des familles du contrôle :")
for f in fams:
    dire(f"   {f} : plus proches voisins sur le numéro (appris sur train) " + " ; ".join(f"k={k} test {v['test']:.4f} test_final {v['test_final']:.4f}" for k, v in obs_knn[f].items()))
dire(f"   controle-delegation, règle de paire « le plus petit numéro de la paire est saboté » (sens appris sur train) : " + " ; ".join(f"{p} {v:.4f}" for p, v in obs_paire.items()))
dire(f"   rang du numéro dans test ∪ test_final (vue de l'organisme), seuil au mieux en échantillon : " + " ; ".join(f"{f} {v:.4f}" for f, v in obs_union.items()))
dire(f"   part (test ou test_final) prévisible par le numéro (seuil, modulo 2 à 10, en échantillon) : {obs_part:.4f}")

# 2. Hasard : (a) identifiants tirés comme le constructeur ; (b) vérités permutées dans chaque (part, famille)
toutes = [(p, t) for p in PARTS for t in b[p]]
rng_a = np.random.default_rng(np.random.SeedSequence(2026102521))
rng_b = np.random.default_rng(np.random.SeedSequence(2026102522))
nul = {"a": [], "b": []}
for mode, rng in (("a", rng_a), ("b", rng_b)):
    for _ in range(N):
        if mode == "a":
            pm = rng.permutation(len(toutes))
            bb = {p: [] for p in PARTS}
            for i, (p, t) in enumerate(toutes):
                bb[p].append({**t, "id": f"t-{int(pm[i]) + 1:04d}"})
            for p in PARTS:
                bb[p].sort(key=lambda x: x["id"])
        else:
            bb = {p: [dict(t) for t in b[p]] for p in PARTS}
            for p in PARTS:
                for f in fams:
                    idx = [i for i, t in enumerate(bb[p]) if t["famille"] == f]
                    v = [bb[p][i]["verite"] for i in idx]
                    v = [v[j] for j in rng.permutation(len(v))]
                    for i, x in zip(idx, v):
                        bb[p][i]["verite"] = x
        n2, y2 = vue(bb)
        st = {f: stat_case(n2[f], y2[f]) for f in fams}
        kn = {f: knn(n2[f], y2[f], 3) for f in fams}
        rp = regle_paire(paires(bb)) if mode == "a" else None
        ru = rang_union(n2, y2)
        pp = part_previsible(bb) if mode == "a" else None
        nul[mode].append((st, kn, rp, ru, pp))


def valp(xs, o):
    xs = np.asarray(xs)
    return float((xs >= o - 1e-9).mean())


dire(f"\n2. Hasard, {N} tirages par construction ; (a) identifiants permutés comme le constructeur, parts triées, SeedSequence(2026102521) ;"
     f" (b) vérités permutées dans chaque (part, famille), identifiants v3 fixes, SeedSequence(2026102522)")
for mode in ("a", "b"):
    for f in fams:
        for p in PARTS:
            xs = [r[0][f][p] for r in nul[mode]]
            dire(f"   ({mode}) {f} {p} : observé {obs[f][p]:.4f} ; médiane {np.median(xs):.4f} ; q95 {np.quantile(xs, .95):.4f} ; q99,5 {np.quantile(xs, .995):.4f} ; max {max(xs):.4f} ; valeur p {valp(xs, obs[f][p]):.3f}")
    for f in fams:
        for p in ("test", "test_final"):
            xs = [r[1][f][p] for r in nul[mode]]
            dire(f"   ({mode}) {f} {p} plus proches voisins k=3 : observé {obs_knn[f][3][p]:.4f} ; q99,5 {np.quantile(xs, .995):.4f} ; valeur p {valp(xs, obs_knn[f][3][p]):.3f}")
    for f in fams:
        xs = [r[3][f] for r in nul[mode]]
        dire(f"   ({mode}) {f} rang dans test ∪ test_final : observé {obs_union[f]:.4f} ; q99,5 {np.quantile(xs, .995):.4f} ; valeur p {valp(xs, obs_union[f]):.3f}")
for p in ("test", "test_final"):
    xs = [r[2][p] for r in nul["a"]]
    dire(f"   (a) règle de paire, {p} : observé {obs_paire[p]:.4f} ; q99,5 {np.quantile(xs, .995):.4f} ; valeur p {valp(xs, obs_paire[p]):.3f}")
xs = [r[4] for r in nul["a"]]
dire(f"   (a) part prévisible : observé {obs_part:.4f} ; q99,5 {np.quantile(xs, .995):.4f} ; valeur p {valp(xs, obs_part):.3f}")

# 3. Ordre du fichier, ordre de service, manifeste, source, textes, amorçage
dire("\n3. Ordre, manifeste, source, textes, amorçage")
for p in PARTS:
    ids = [t["id"] for t in b[p]]
    dire(f"   {p} : ordre du fichier = tri par identifiant : {ids == sorted(ids)} (l'ordre n'ajoute rien à l'identifiant)")
seq = [num(t["id"]) for t in b["test"]] + [num(t["id"]) for t in b["test_final"]]
desc = [i for i in range(1, len(seq)) if seq[i] < seq[i - 1]]
dire(f"   test + test_final dans l'ordre du fichier (tous_tests, boucle.py l. 607) : descentes aux positions {desc} -> qui connaît l'entropie de course remet l'ordre du fichier et lit la part (test ou test_final) de chaque tâche servie, pas sa vérité")
m = b["manifeste"]
mt = json.dumps(m, ensure_ascii=False)
dire(f"   manifeste : clés {list(m)} ; identifiants de tâche cités : {len(re.findall(r't-[0-9]{4}', mt))} ; formes v1 citées (cd-lot, ce-hf) : {len(re.findall(r'cd-lot|ce-hf', mt))} ; "
     f"entropie de partition v1 présente : {'entropie_seed_sequence' in m} ; comptes par strate : {len(m.get('comptes_par_strate', {}))} strates")
for f in fams:
    for p in PARTS:
        src = [t["source"] for t in b[p] if t["famille"] == f]
        y = [t["verite"] == POS[f] for t in b[p] if t["famille"] == f]
        r, d = majorite(src, y)
        dire(f"   source -> vérité, {f} {p} : sources {sorted(set(src))} ; exactitude équilibrée en échantillon {ee([r.get(v, d) for v in src], y):.4f}")
et = {(t["famille"], tuple(t["etiquettes"])) for p in PARTS for t in b[p]}
dire(f"   étiquettes par famille (constantes ?) : {sorted(et)}")
ids_tous = {t["id"] for p in PARTS for t in b[p]}
tx = [(p, t) for p in PARTS for t in b[p]]
n_id = sum(1 for p, t in tx if re.search(r"\bt-\d{4}\b", t["texte"]))
n_v1 = sum(1 for p, t in tx if re.search(r"cd-lot[12]|ce-hf-\d{4}|\bL[12]-\d{2}-[HS]\b", t["texte"]))
n_self = sum(1 for p, t in tx if t["id"] in t["texte"])
dire(f"   textes qui portent une forme t-NNNN : {n_id} ; une forme v1 ou brute : {n_v1} ; leur propre identifiant : {n_self}")
six = b["train"][:6]
grp = [s[t["id"]]["groupe"] for t in six]
dire(f"   consigne d'amorçage (boucle.py l. 507 : train[:6]) : " + " ; ".join(f"{t['id']} {t['famille']} {t['verite']} {t['source']}" for t in six))
dire(f"      paires complètes parmi les six : {sum(1 for g in set(grp) if grp.count(g) == 2)} ; caractères des six textes : {sum(len(t['texte']) for t in six)}")
print("\n".join(out))
