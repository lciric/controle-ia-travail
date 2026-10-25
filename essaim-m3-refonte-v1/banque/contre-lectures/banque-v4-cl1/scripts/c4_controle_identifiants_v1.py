"""Contre-lecture banque v4 — c4 : le contrôle des identifiants v2 à 12 traces — v1.
Importe `statistiques` et la logique de `calibrer` du script v2 (sans fichier compilé), refait la calibration à
l'identique (même graine, mêmes 2 000 tirages) et rapporte, par case, la loi du maximum sous le hasard : quantile 0,995,
P(max = 1,0) (taux de refus à tort d'une banque saine, le refus étant « max ≥ seuil »), part des tirages par valeur.
Essais : fuite partielle (10 traces sur 12 portent la vérité dans la parité du numéro) et fuite totale, sur la v4.
Usage : python3 -I -B c4_controle_identifiants_v1.py SCRIPT_V2 BANQUE_V4 [TIRAGES]
"""
import collections, hashlib, importlib.util, json, pathlib, sys

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("ctrl_v2", sys.argv[1])
ctrl = importlib.util.module_from_spec(spec); spec.loader.exec_module(ctrl)
import numpy as np

b = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
tirages = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
PARTS = ctrl.PARTS
out = {"tirages": tirages, "observe": ctrl.statistiques(b), "composition": ctrl.composition(b)}
rng = np.random.default_rng(np.random.SeedSequence(ctrl.GRAINE_CALIBRATION))
taches = sorted(((p, t) for p in PARTS for t in b[p]), key=lambda x: (PARTS.index(x[0]), x[1]["famille"], x[1]["verite"], hashlib.sha256(x[1]["texte"].encode("utf-8")).hexdigest()))
n = len(taches)
maxima = collections.defaultdict(list)
for _ in range(tirages):
    perm = rng.permutation(n)
    bb = {p: [] for p in PARTS}
    for i, (p, t) in enumerate(taches):
        bb[p].append({**t, "id": f"t-{int(perm[i]) + 1:04d}"})
    for p in PARTS:
        bb[p].sort(key=lambda x: x["id"])
    for fam, cases in ctrl.statistiques(bb).items():
        for p, c in cases.items():
            maxima[(fam, p)].append(c["max"])
loi = {}
for (fam, p), xs in sorted(maxima.items()):
    xs = np.array(xs)
    q = float(np.quantile(xs, ctrl.QUANTILE))
    seuil = float(min(1.0, np.ceil(q * 100) / 100))
    loi[f"{fam}|{p}"] = {"quantile_0995": round(q, 4), "seuil": seuil, "P_max_au_seuil": round(float((xs >= seuil - 1e-12).mean()), 4),
                         "P_max_egal_1": round(float((xs >= 1 - 1e-12).mean()), 4),
                         "valeurs": {str(round(float(v), 4)): round(float((xs == v).mean()), 4) for v in np.unique(xs)}}
out["loi_du_maximum"] = loi


def fuite(bq, part, k):
    """Copie de la banque où, dans `part`, k traces de délégation sur 12 ont un numéro dont la parité dit la vérité
    (sabotée : impair) ; les numéros sont réattribués parmi ceux de la part (la part reste triée)."""
    bb = json.loads(json.dumps(bq))
    ts = [t for t in bb[part] if t["famille"] == "controle-delegation"]
    nums = sorted(int(t["id"].split("-")[1]) for t in ts)
    impairs = [x for x in nums if x % 2]; pairs = [x for x in nums if not x % 2]
    # on fabrique des numéros neufs hors banque pour garantir la parité voulue
    pris = {int(t["id"].split("-")[1]) for p in PARTS for t in bb[p]}
    libres = [x for x in range(201, 2000) if x not in pris]
    li = [x for x in libres if x % 2]; lp = [x for x in libres if not x % 2]
    for j, t in enumerate(ts):
        bonne = (t["verite"] == "sabotage")
        if j >= k:
            bonne = not bonne
        t["id"] = f"t-{(li.pop(0) if bonne else lp.pop(0)):04d}"
    bb[part].sort(key=lambda x: x["id"])
    return bb


essais = {}
for part in ("test", "test_final"):
    for k in (10, 12):
        s = ctrl.statistiques(fuite(b, part, k))["controle-delegation"][part]
        seuil = loi[f"controle-delegation|{part}"]["seuil"]
        essais[f"{part} : {k}/12 portent la vérité"] = {"max": s["max"], "regle": s["regle"], "seuil": seuil, "refuse": s["max"] >= seuil - 1e-12}
out["essais_fuite"] = essais
print(json.dumps(out, ensure_ascii=False, indent=1))
