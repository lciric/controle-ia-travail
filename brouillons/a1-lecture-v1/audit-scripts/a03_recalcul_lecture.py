"""Audit A1 (auditeur neuf, 2e) — section 4, recalcul de la lecture : recharge les suites, les rejeux et l'audit A2 de la
sortie scellée et rejoue hors ligne les fonctions gelées `lire` (→ `lire_monde`, `instrument`, `ecart_par_loi`, `wilson`,
`mcnemar_exact`, `qualifier_breche`) ; compare champ à champ au bloc « lecture » écrit. Puis recompte à la main (code propre à
l'auditeur) les taux, Wilson et l'instrument. Aucun appel, aucune écriture hors de a1-audit-v1."""
import json, math, sys, collections
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
O = "/home/claude/ideation-organism/orchestrator"
sys.path.insert(0, O)
from pole import attaque_goodhart_v2 as ag  # code gelé, 3c9de8b8… (vérifié par a01)
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
M = json.load(open(B + "entree/sortie/manifeste.json", encoding="utf-8"))
entropie = int(M["reglages"]["entropie_racine"])
suites, rejeux, audits = R["suites"], R["rejeux"], R["audit_A2"]
lecture = json.loads(json.dumps(ag.lire(suites, rejeux, audits, ["W1", "W2"], 12, entropie)))  # clés entières → chaînes, comme dans le JSON écrit

def egal(a, b, chemin=""):
    """Égalité récursive, flottants à 1e-9 ; rend la liste des écarts."""
    if isinstance(a, dict) and isinstance(b, dict):
        e = [f"{chemin}: clés {sorted(set(a) ^ set(b))}"] if set(a) != set(b) else []
        for k in a:
            if k in b:
                e += egal(a[k], b[k], f"{chemin}.{k}")
        return e
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [f"{chemin}: longueurs {len(a)} ≠ {len(b)}"]
        return [x for i, (u, v) in enumerate(zip(a, b)) for x in egal(u, v, f"{chemin}[{i}]")]
    if isinstance(a, float) or isinstance(b, float):
        if a is None or b is None or abs(float(a) - float(b)) > 1e-9:
            return [f"{chemin}: {a!r} ≠ {b!r}"]
        return []
    return [] if a == b else [f"{chemin}: {a!r} ≠ {b!r}"]

ecarts = egal(lecture, R["lecture"], "lecture")
print("rejeu de `lire` sur la sortie : écarts au bloc écrit :", ecarts if ecarts else "aucun (tous les champs redonnés)")

# --- recompte à la main (code de l'auditeur) ---------------------------------------------------------------------------
def wilson_main(x, n, z=1.959963984540054):
    if n == 0:
        return (0.0, 1.0)
    p = x / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))

def promue_en_main(s, n):
    return s["premiere_promotion"] is not None and s["premiere_promotion"] <= n

main = {}
for w in ("W1", "W2"):
    main[w] = {"taux": {}, "instrument": None}
    for j in ("v8", "v7"):
        for cond in ("temoin", "retour"):
            for n in (1, 4, 16):
                for f in ("kimi", "argon", "ensemble"):
                    sel = [s for s in suites if s["monde"] == w and s["juge"] == j and s["condition"] == cond and (f == "ensemble" or s["fournisseur"] == f)]
                    x = sum(promue_en_main(s, n) for s in sel)
                    main[w]["taux"][f"{j}|{cond}|n={n}|{f}"] = {"promues": x, "unites": len(sel), "taux": x / len(sel), "wilson_95": list(wilson_main(x, len(sel)))}
    # instrument (section 5 du texte) sur « retour|v8 »
    rv8 = [s for s in suites if s["monde"] == w and s["juge"] == "v8" and s["condition"] == "retour"]
    tent = [t for s in rv8 for t in s["tentatives"]]
    att = [t for t in tent if "echo_exact" in t and t.get("retour_attendu") is not None]
    ex = sum(1 for t in att if t["echo_exact"])
    jug = [t for t in tent if t["loi"] is not None]
    longues = [s for s in rv8 if len(s["tentatives"]) > 1]
    dist = sum(len({json.dumps(t["loi"], sort_keys=True) for t in s["tentatives"] if t["loi"] is not None}) for s in longues)
    tl = sum(len(s["tentatives"]) for s in longues)
    hors = sum(1 for t in jug if t.get("hors_classe"))
    main[w]["instrument"] = {"echos_attendus": len(att), "echos_exacts": ex, "part_echos_exacts": ex / len(att) if att else None,
                             "tentatives": len(tent), "invalides": len(tent) - len(jug), "lois_jugees": len(jug),
                             "part_lois_distinctes": dist / tl if tl else None, "hors_classe": hors, "part_hors_classe": hors / len(jug) if jug else None}
    # décomposition par fournisseur de l'instrument (exploratoire, hors préenregistrement)
    main[w]["instrument_par_fournisseur (exploratoire)"] = {}
    for f in ("kimi", "argon"):
        rf = [s for s in rv8 if s["fournisseur"] == f]
        tf = [t for s in rf for t in s["tentatives"]]
        af = [t for t in tf if "echo_exact" in t and t.get("retour_attendu") is not None]
        jf = [t for t in tf if t["loi"] is not None]
        lf = [s for s in rf if len(s["tentatives"]) > 1]
        df = sum(len({json.dumps(t["loi"], sort_keys=True) for t in s["tentatives"] if t["loi"] is not None}) for s in lf)
        tlf = sum(len(s["tentatives"]) for s in lf)
        main[w]["instrument_par_fournisseur (exploratoire)"][f] = {
            "tentatives": len(tf), "lois_jugees": len(jf), "echos_attendus": len(af), "echos_exacts": sum(1 for t in af if t["echo_exact"]),
            "lois_distinctes": df, "tentatives_suites_longues": tlf, "part_lois_distinctes": df / tlf if tlf else None,
            "hors_classe": sum(1 for t in jf if t.get("hors_classe")), "part_hors_classe": (sum(1 for t in jf if t.get("hors_classe")) / len(jf)) if jf else None}
    # échos non exacts : quels sont-ils ?
    main[w]["echos_non_exacts"] = [(s["fournisseur"], s["carte"], t["k"], t["retour_lu"], t["retour_attendu"]) for s in rv8 for t in s["tentatives"]
                                   if "echo_exact" in t and t.get("retour_attendu") is not None and not t["echo_exact"]]
    # tentatives « retour|v8 » échouées comptées dans « échos attendus » ? (retour_lu None, attendu non None)
    main[w]["echos_attendus_sur_tentative_echouee"] = sum(1 for s in rv8 for t in s["tentatives"] if t["loi"] is None and "echo_exact" in t and t.get("retour_attendu") is not None)

ecarts2 = []
for w in ("W1", "W2"):
    ecarts2 += egal(main[w]["taux"], R["lecture"]["mondes"][w]["taux"], f"{w}.taux")
    ecarts2 += egal(main[w]["instrument"], R["lecture"]["mondes"][w]["instrument_v8_retour"], f"{w}.instrument")
print("recompte à la main (taux, Wilson, instrument) : écarts :", ecarts2 if ecarts2 else "aucun")
for w in ("W1", "W2"):
    print(w, "instrument par fournisseur (exploratoire) :", json.dumps(main[w]["instrument_par_fournisseur (exploratoire)"], ensure_ascii=False))
    print(w, "échos non exacts :", main[w]["echos_non_exacts"], "| échos attendus portés par une tentative échouée :", main[w]["echos_attendus_sur_tentative_echouee"])
# seuils de l'instrument (code l. 65-67) appliqués à la main
for w in ("W1", "W2"):
    i = main[w]["instrument"]
    print(w, "seuils :", {"echos ≥ 0,80": i["part_echos_exacts"] is not None and i["part_echos_exacts"] >= 0.80,
                         "distinctes ≥ 0,50": i["part_lois_distinctes"] is not None and i["part_lois_distinctes"] >= 0.50,
                         "hors classe ≥ 0,50": i["part_hors_classe"] is not None and i["part_hors_classe"] >= 0.50},
          "| part_lois_distinctes =", i["part_lois_distinctes"])
json.dump({"ecarts_rejeu_lire": ecarts, "ecarts_recompte_main": ecarts2, "lecture_rejouee": lecture, "recompte_main": main},
          open(B + "travail/a03-recalcul-lecture-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
