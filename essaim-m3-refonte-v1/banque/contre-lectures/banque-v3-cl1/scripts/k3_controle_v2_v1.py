"""Contre-lecture banque v3 — k3 : le contrôle v2 (calibration, taux de refus à tort, stabilité des seuils,
sensibilité) et artefacts qu'il laisse passer.

Statistique : ma réimplémentation « fidèle » (égalités vers la première étiquette, comme le contrôle), vérifiée égale
aux maxima du rapport sur la v3 (k2). Les artefacts R1 et R2 et la reprise de A6 passent par le contrôle scellé lui-même.
Ne lit pas la clé.
Usage : python3 -I k3_controle_v2_v1.py BANQUE_DIR DOSSIER_SORTIE N_TIRAGES N_SENSIBILITE
"""
import hashlib
import json
import pathlib
import subprocess
import sys

import numpy as np

B, OUT, N, NS = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
PARTS = ("train", "test", "test_final")
V = B / "construction-v3" / "verifier_identifiants_opaques_v2.py"
RAP = B / "construction-v3" / "controle-banque-v3-v2.json"
v1 = json.loads((B / "banque-confrontation-v1.json").read_text(encoding="utf-8"))
v3 = json.loads((B / "banque-confrontation-v3.json").read_text(encoding="utf-8"))
s3 = json.loads((B / "banque-confrontation-v3-secret.json").read_text(encoding="utf-8"))
rap = json.loads(RAP.read_text(encoding="utf-8"))
SEUIL = {(c["famille"], c["part"]): c["seuil"] for c in rap["cases"]}
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


CACHE = {}


def F(i):
    if i not in CACHE:
        CACHE[i] = feats(i)
    return CACHE[i]


NOMS = sorted(feats("t-0001"))


def ee(pred, y):
    pred, y = np.asarray(pred, dtype=bool), np.asarray(y, dtype=bool)
    return ((pred[y].mean() if y.any() else 0.0) + ((~pred[~y]).mean() if (~y).any() else 0.0)) / 2


def majorite(vals, y):  # égalités vers la première étiquette (positive), comme le contrôle
    c = {}
    for v, t in zip(vals, y):
        a = c.setdefault(v, [0, 0])
        a[int(t)] += 1
    n1 = sum(1 for t in y if t)
    defaut = n1 >= len(y) - n1
    return {v: a[1] >= a[0] for v, a in c.items()}, defaut


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


POS = {"conscience-evaluation": "evaluation", "controle-delegation": "sabotage"}


def stats(bq):
    o = {}
    for f in sorted(POS):
        ids = {p: [t["id"] for t in bq[p] if t["famille"] == f] for p in PARTS}
        ys = {p: [t["verite"] == POS[f] for t in bq[p] if t["famille"] == f] for p in PARTS}
        res = {}
        for p in ("test", "test_final"):
            best = 0
            for nom in NOMS:
                r, d = majorite([F(i)[nom] for i in ids["train"]], ys["train"])
                best = max(best, ee([r.get(F(i)[nom], d) for i in ids[p]], ys[p]))
            _, (c, sens) = seuil_au_mieux([num(i) for i in ids["train"]], ys["train"])
            best = max(best, ee((np.asarray([num(i) for i in ids[p]]) - c) * sens > 0, ys[p]))
            res[p] = best
        for p in PARTS:
            for rg in (np.arange(len(ids[p])), np.argsort(np.argsort([num(i) for i in ids[p]], kind="stable"), kind="stable")):
                best = seuil_au_mieux(rg, ys[p])[0]
                for m in (2, 3, 4):
                    r, d = majorite(list(rg % m), ys[p])
                    best = max(best, ee([r.get(v, d) for v in rg % m], ys[p]))
                res[p] = max(res.get(p, 0), best)
        for p in PARTS:
            o[(f, p)] = round(float(res[p]), 4)
    return o


def tirage(rng, ordre):
    pm = rng.permutation(len(ordre))
    bb = {p: [] for p in PARTS}
    for i, (p, t) in enumerate(ordre):
        bb[p].append({**t, "id": f"t-{int(pm[i]) + 1:04d}"})
    for p in PARTS:
        bb[p].sort(key=lambda x: x["id"])
    return bb


# 0. Cohérence avec le rapport
o3 = stats(v3)
dire("0. Ma statistique fidèle sur la v3 = maxima du rapport scellé : "
     f"{all(abs(o3[(c['famille'], c['part'])] - c['max']) < 1e-9 for c in rap['cases'])}")

# 1. Hasard du constructeur (ordre du fichier v1), N tirages, graine indépendante
ordre_v1 = [(p, t) for p in PARTS for t in v1[p]]
rng = np.random.default_rng(np.random.SeedSequence(2026102531))
tir = [stats(tirage(rng, ordre_v1)) for _ in range(N)]
cases = sorted(SEUIL)
dire(f"\n1. Hasard du constructeur, {N} tirages (SeedSequence(2026102531), ordre du fichier v1) ; seuils du rapport v3")
for c in cases:
    xs = np.array([t[c] for t in tir])
    dire(f"   {c[0]} {c[1]} : seuil {SEUIL[c]} ; médiane {np.median(xs):.4f} (rapport {next(x['mediane_hasard'] for x in rap['cases'] if (x['famille'], x['part']) == c)}) ;"
         f" q99,5 {np.quantile(xs, .995):.4f} (rapport {next(x['quantile_hasard'] for x in rap['cases'] if (x['famille'], x['part']) == c)}) ;"
         f" valeur atteignable la plus basse au seuil {min(x for x in set(xs.tolist()) | {1.0} if x >= SEUIL[c] - 1e-12):.4f} ;"
         f" P(max ≥ seuil) = {(xs >= SEUIL[c] - 1e-12).mean():.4f}")
refus = np.array([any(t[c] >= SEUIL[c] - 1e-12 for c in cases) for t in tir])
dire(f"   taux de refus à tort d'une banque bien construite (au moins une case sur 6) : {refus.mean():.4f} (erreur type {np.sqrt(refus.mean() * (1 - refus.mean()) / N):.4f})")

# 2. Stabilité des seuils : quantile 0,995 arrondi au centième supérieur, sur des blocs de 2 000 tirages
dire("\n2. Stabilité du seuil : quantile 0,995 + arrondi au centième supérieur, par blocs indépendants de 2 000 tirages")
nb = N // 2000
for c in cases:
    xs = np.array([t[c] for t in tir])
    seuils = [float(min(1.0, np.ceil(np.quantile(xs[k * 2000:(k + 1) * 2000], .995) * 100) / 100)) for k in range(nb)]
    dire(f"   {c[0]} {c[1]} : seuil du rapport {SEUIL[c]} ; seuils des {nb} blocs {seuils}")

# 3. Sensibilité : fuite par suffixe -S/-H en délégation, juste avec probabilité q
dire(f"\n3. Sensibilité (délégation ; {NS} tirages par cas ; SeedSequence(2026102532) ; seuils du rapport v3)")
rng = np.random.default_rng(np.random.SeedSequence(2026102532))


def fuite(q, parts_fuite):
    bq = json.loads(json.dumps(v3))
    for p in PARTS:
        for t in bq[p]:
            if t["famille"] != "controle-delegation":
                continue
            vrai = "S" if t["verite"] == "sabotage" else "H"
            if p in parts_fuite:
                sfx = vrai if rng.random() < q else ("H" if vrai == "S" else "S")
            else:
                sfx = "S" if rng.random() < 0.5 else "H"
            t["id"] = f"{t['id']}-{sfx}"
    return bq


for nom, parts_fuite in (("trois parts", PARTS), ("train et test_final seulement", ("train", "test_final"))):
    for q in (0.75, 0.80, 0.85, 0.90, 0.95, 1.0):
        r = []
        tf = []
        for _ in range(NS):
            st = stats(fuite(q, parts_fuite))
            r.append(any(st[c] >= SEUIL[c] - 1e-12 for c in cases))
            tf.append(st[("controle-delegation", "test_final")])
        dire(f"   {nom}, q={q:.2f} : refusée dans {np.mean(r):.3f} des tirages ; passe dans {1 - np.mean(r):.3f} ; médiane du maximum en test_final {np.median(tf):.4f}")


# 4. Artefacts que le contrôle laisse passer (passés au contrôle scellé, seuils du rapport v3)
def ecrire(nom, bq):
    p = OUT / nom
    if p.exists():
        sys.exit(f"refus : {p} existe (R12)")
    p.write_text(json.dumps(bq, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    p.with_name(p.name + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return p


def controle(p, extra=()):
    r = subprocess.run([sys.executable, "-I", "-B", str(V), str(p)] + list(extra), capture_output=True, text=True)
    (OUT / f"sortie-controle-{p.stem}.txt").write_text(r.stdout + r.stderr, encoding="utf-8")
    try:
        j = json.loads(r.stdout)
    except Exception:
        j = {"brut": r.stdout[:300]}
    return r.returncode, j


r1 = json.loads(json.dumps(v3))
for p in PARTS:
    g = {}
    for t in r1[p]:
        if t["famille"] == "controle-delegation":
            g.setdefault(s3[t["id"]]["groupe"], []).append(t)
    for a, c in g.values():
        sab, hon = (a, c) if a["verite"] == "sabotage" else (c, a)
        if num(sab["id"]) > num(hon["id"]):
            sab["id"], hon["id"] = hon["id"], sab["id"]
    r1[p].sort(key=lambda x: x["id"])
p1 = ecrire("R1-paire-plus-petit-numero-sabote-v1.json", r1)
code, j = controle(p1, ["--seuils", str(RAP)])
dire("\n4. Artefacts passés au contrôle scellé (seuils du rapport v3)")
dire(f"   R1 « dans chaque paire, le plus petit numéro est le sabotage » (règle de paire : 1,0 sur les trois parts par construction) :"
     f" code {code} ; cases au seuil {j.get('cases_au_seuil')} ; maxima {[(c['famille'][:5], c['part'], c['max']) for c in j.get('cases', [])]}")
r2 = {"manifeste": v3["manifeste"]}
rng = np.random.default_rng(np.random.SeedSequence(2026102533))
debut = {"train": 1, "test": 81, "test_final": 141}
for p in PARTS:
    l = [dict(t) for t in v3[p]]
    pm = rng.permutation(len(l))
    for k, t in zip(pm, l):
        t["id"] = f"t-{debut[p] + int(k):04d}"
    r2[p] = sorted(l, key=lambda x: x["id"])
r2 = {k: r2[k] for k in ("train", "test", "test_final", "manifeste")}
p2 = ecrire("R2-part-lisible-dans-le-numero-v1.json", r2)
code, j = controle(p2, ["--seuils", str(RAP)])
dire(f"   R2 « numéros 81-140 pour test, 141-200 pour test_final » (part lue sans erreur sur les 120 tâches mêlées) :"
     f" code {code} ; cases au seuil {j.get('cases_au_seuil')}")
eqv = ["--v1", str(B / "banque-confrontation-v1.json"), "--secret-v1", str(B / "banque-confrontation-v1-secret.json"),
       "--secret", str(B / "banque-confrontation-v3-secret.json"), "--tirages", "40"]
a6 = B / "construction-v3" / "artefacts-v1" / "A6-texte-modifie.json"
code, j = controle(a6, eqv)
dire(f"   A6 repris SANS --seuils (calibration propre, 40 tirages) et avec l'équivalence : code {code} ; erreurs {j.get('erreurs')}")
code, j = controle(a6, ["--seuils", str(RAP)])
dire(f"   A6 tel que dans les essais (avec --seuils) : code {code} ; sortie {j.get('brut', j)!r}")
print("\n".join(out))
