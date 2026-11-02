"""v05 — lecture gelée (`ag.lire`, code gelé importé en lecture seule) : (a) sur la sortie entière, comparée au bloc
`lecture` scellé ; (b) EXPLORATOIRE, HORS PRÉENREGISTREMENT : sur les seules suites d'Argon (rejeux et audit A2 restreints
à Argon ; cartes = 12, donc ε = 0,25 du code). Aucune écriture hors du fichier de sortie.
Usage : python3 -I -B v05_lire_gele.py ORCHESTRATOR SORTIE.json MANIFESTE.json SORTIE_JSON"""
import json
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import pole.attaque_goodhart_v2 as ag  # noqa: E402

sortie = json.load(open(sys.argv[2], encoding="utf-8"))
E = int(json.load(open(sys.argv[3], encoding="utf-8"))["reglages"]["entropie_racine"])


def egal(a, b, chemin=""):
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a) != set(b):
            return [f"{chemin}: clés {sorted(set(a) ^ set(b))}"]
        return [x for k in a for x in egal(a[k], b[k], f"{chemin}.{k}")]
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if len(a) != len(b):
            return [f"{chemin}: longueurs {len(a)} ≠ {len(b)}"]
        return [x for i, (u, v) in enumerate(zip(a, b)) for x in egal(u, v, f"{chemin}[{i}]")]
    if isinstance(a, float) or isinstance(b, float):
        return [] if (a is None) == (b is None) and (a is None or abs(a - b) <= 1e-9) else [f"{chemin}: {a} ≠ {b}"]
    return [] if a == b else [f"{chemin}: {a!r} ≠ {b!r}"]


entier = ag.lire(sortie["suites"], sortie["rejeux"], sortie["audit_A2"], ["W1", "W2"], 12, E)
# JSON aller-retour : la sortie scellée a des clés de chaînes (n = 1, 4, 16 du plafond de multiplicité)
entier = json.loads(json.dumps(entier, ensure_ascii=False))
diff = egal(entier, sortie["lecture"])

suites_a = [s for s in sortie["suites"] if s["fournisseur"] == "argon"]
rejeux_a = [r for r in sortie["rejeux"] if r["etiquette"].split("|")[1] == "argon"]
audit_a = [r for r in sortie["audit_A2"] if r["etiquette"].split("|")[1] == "argon"]
argon = json.loads(json.dumps(ag.lire(suites_a, rejeux_a, audit_a, ["W1", "W2"], 12, E), ensure_ascii=False))
res = {"lecture_entiere_egale_au_bloc_scelle": not diff, "ecarts": diff[:20],
       "EXPLORATOIRE_HORS_PREENREGISTREMENT_argon_seul": {
           w: {k: argon["mondes"][w][k] for k in ("issue", "breche", "dents", "resiste", "eps_resistance",
                                                   "qualification_breche", "instrument_v8_retour", "audits",
                                                   "issue_suspendue_par_audit", "predictions", "ecarts_goodhart_par_carte",
                                                   "ecart_par_loi_H3")}
           | {"v8_retour_16": argon["mondes"][w]["taux"]["v8|retour|n=16|ensemble"],
              "v7_retour_16": argon["mondes"][w]["taux"]["v7|retour|n=16|ensemble"],
              "v8_temoin_1": argon["mondes"][w]["taux"]["v8|temoin|n=1|ensemble"],
              "v7_temoin_1": argon["mondes"][w]["taux"]["v7|temoin|n=1|ensemble"]}
           for w in ("W1", "W2")}}
json.dump(res, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("lecture entière = bloc scellé :", not diff, diff[:5])
for w, m in res["EXPLORATOIRE_HORS_PREENREGISTREMENT_argon_seul"].items():
    print(f"\n[exploratoire, hors préenregistrement] Argon seul, {w} : {m['issue']}")
    for k in ("breche", "dents", "resiste", "eps_resistance", "qualification_breche", "v8_retour_16", "v7_retour_16",
              "v8_temoin_1", "v7_temoin_1", "instrument_v8_retour", "audits", "predictions", "ecart_par_loi_H3"):
        print(f"  {k}: {m[k]}")
