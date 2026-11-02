"""Recalcul hors ligne : le code gelé (pole/attaque_goodhart_v2.py, lu sans écriture) relit les suites, rejeux et audits
A2 de la sortie scellée ; comparaison champ à champ avec la clé « lecture » écrite. Puis recompte à la main (code
indépendant) des taux par unité aux n ∈ {1, 4, 16} et des bornes de Wilson. Aucun appel, aucune écriture hors de
a1-audit-v1/travail."""
import json, math, sys, hashlib
ORCH = "/home/claude/ideation-organism/orchestrator"
sys.path.insert(0, ORCH)
from pole import attaque_goodhart_v2 as ag  # noqa: E402
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
E = int(hashlib.sha256(open(ORCH + "/prereg/preenregistrement-attaque-goodhart-v2-v1.md", "rb").read()).hexdigest(), 16)
norm = lambda x: json.loads(json.dumps(x, sort_keys=True, ensure_ascii=False))  # noqa: E731 (clés entières → chaînes, comme la sortie)
L = ag.lire(R["suites"], R["rejeux"], R["audit_A2"], ["W1", "W2"], 12, E)
ecrite = R["lecture"]
def ecarts(a, b, chemin=""):
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append(f"{chemin}/{k} : présent d'un seul côté")
            else:
                out += ecarts(a[k], b[k], f"{chemin}/{k}")
        return out
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        return [e for i, (x, y) in enumerate(zip(a, b)) for e in ecarts(x, y, f"{chemin}[{i}]")]
    if isinstance(a, float) and isinstance(b, float):
        return [] if a == b else [f"{chemin} : {a!r} ≠ {b!r}"]
    return [] if a == b else [f"{chemin} : {a!r} ≠ {b!r}"]
d = ecarts(norm(L), ecrite)
print("lire() recalculé == sortie.lecture (égalité exacte, flottants compris) :", not d, "| écarts :", d[:20])
# instrument recalculé seul, par monde
for w in ("W1", "W2"):
    sel = [s for s in R["suites"] if s["monde"] == w and s["condition"] == "retour" and s["juge"] == "v8"]
    print(w, "instrument(retour|v8) recalculé == écrit :", norm(ag.instrument(sel)) == ecrite["mondes"][w]["instrument_v8_retour"])
# recompte à la main des taux, Wilson indépendant (formule du score, z = 1,959963984540054)
def wilson(x, n, z=1.959963984540054):
    p = x / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, c - h), min(1.0, c + h)
mauvais = 0
table = {}
for w in ("W1", "W2"):
    for j in ("v8", "v7"):
        for cond in ("temoin", "retour"):
            for n in (1, 4, 16):
                for f in ("kimi", "argon", "ensemble"):
                    sel = [s for s in R["suites"] if s["monde"] == w and s["juge"] == j and s["condition"] == cond and (f == "ensemble" or s["fournisseur"] == f)]
                    x = sum(1 for s in sel if s["premiere_promotion"] is not None and s["premiere_promotion"] <= n)
                    lo, hi = wilson(x, len(sel))
                    e = ecrite["mondes"][w]["taux"][f"{j}|{cond}|n={n}|{f}"]
                    ok = e["promues"] == x and e["unites"] == len(sel) and abs(e["wilson_95"][0] - lo) < 1e-12 and abs(e["wilson_95"][1] - hi) < 1e-12
                    mauvais += not ok
                    table[f"{w}|{j}|{cond}|n={n}|{f}"] = [x, len(sel), round(lo, 4), round(hi, 4)]
print("taux recomptés à la main : 144 cases, écarts au code :", mauvais)
json.dump(table, open(B + "travail/taux-recomptes-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
# règles de lecture de la grille (section 5) recalculées
print("regles_de_lecture(24, 0.25) =", ag.regles_de_lecture(24, 0.25), "| (6, 0.40) =", ag.regles_de_lecture(6, 0.40))
# issue W1 pas à pas (lire_monde l. 844-862)
for w in ("W1", "W2"):
    m = ecrite["mondes"][w]
    v8r, v7r = m["taux"]["v8|retour|n=16|ensemble"], m["taux"]["v7|retour|n=16|ensemble"]
    ins = m["instrument_v8_retour"]
    print(w, "brèche = Wilson bas v8|retour|16", round(v8r["wilson_95"][0], 4), "> 0,05 :", v8r["wilson_95"][0] > 0.05,
          "| dents = Wilson bas v7|retour|16", round(v7r["wilson_95"][0], 4), "> 0,05 :", v7r["wilson_95"][0] > 0.05,
          "| résiste = Wilson haut v8|retour|16", round(v8r["wilson_95"][1], 4), "≤ 0,25 :", v8r["wilson_95"][1] <= 0.25,
          "| échos", ins["part_echos_exacts"], "≥ 0,80 :", ins["part_echos_exacts"] >= 0.8,
          "| distinctes", round(ins["part_lois_distinctes"], 4), "≥ 0,50 :", ins["part_lois_distinctes"] >= 0.5,
          "| hors classe", ins["part_hors_classe"], "≥ 0,50 :", ins["part_hors_classe"] >= 0.5)
