"""(1) Rejuge une fois chaque loi valide avec la fonction gelée `juger` (mêmes étiquette, carte, k : mêmes graines) et
compare statut, promotion, log W max et membre dominant au verdict écrit. (2) Vérifie les mondes : W1 = melange(S1, S2),
π dans [0,3 ; 0,7] ; W2 = par_sous_population(S1, S2) ; membre « ajuste_lineaire:archive » présent et portant [S1, S2]
(nul_v8.membres_archive_v8, qui appelle exiger_membres_ajustes). (3) Lois invalides : facteurs lus dans la réponse
caviardée. Aucun appel, aucune écriture hors de a1-audit-v1/travail."""
import json, math, sys, hashlib, collections, time
ORCH = "/home/claude/ideation-organism/orchestrator"
sys.path.insert(0, ORCH)
from pole import attaque_goodhart_v2 as ag  # noqa: E402
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
E = int(hashlib.sha256(open(ORCH + "/prereg/preenregistrement-attaque-goodhart-v2-v1.md", "rb").read()).hexdigest(), 16)
b = ag.banc()
cartes = {(w, c): ag.carte(E, c, w) for w in ("W1", "W2") for c in range(12)}
# (2) mondes
for (w, ci), c in sorted(cartes.items()):
    L, m = c["L"], c["monde"]
    if w == "W1":
        ok = m["type"] == "melange" and m["composantes"] == [L["S1"], L["S2"]] and 0.3 <= m["poids"][0] <= 0.7 and abs(sum(m["poids"]) - 1) < 1e-12 and c["pi"] == m["poids"][0]
    else:
        ok = m == {"type": "par_sous_population", "lois": {"0": L["S1"], "1": L["S2"]}}
    membres = b.nul_v8.membres_archive_v8({"S1": L["S1"], "S2": L["S2"]}, None, b.K, b.DIM)
    lin = [x for x in membres if x["nom"] == "ajuste_lineaire:archive"]
    lin_ok = len(lin) == 1 and lin[0]["type"] == "ajuste_lineaire" and lin[0]["lois"] == [L["S1"], L["S2"]]
    print(w, ci, "monde conforme :", ok, "| π =", None if c["pi"] is None else round(c["pi"], 4), "| ajuste_lineaire:archive [S1, S2] :", lin_ok,
          "| membres v8 :", sorted({x["type"] for x in membres}))
# (1) rejugement
t0 = time.time()
diff, n, compte = [], 0, collections.Counter()
for s in R["suites"]:
    c = cartes[(s["monde"], s["carte"])]
    et = ag.etiquette_suite(s["monde"], s["fournisseur"], s["condition"], s["juge"])
    for t in s["tentatives"]:
        if t["loi"] is None:
            continue
        v = ag.juger(t["loi"], c, s["juge"], E, et, t["k"])
        n += 1
        w = t["verdict"]
        same = (v["statut"] == w["statut"] and v["promue"] == w["promue"] and v["log_w_max"] == w["log_w_max"] and v["dominant"] == w["dominant"] and v["motif"] == w["motif"])
        compte[(s["juge"], same)] += 1
        if not same:
            diff.append((et, s["carte"], t["k"], v, w))
print("rejugement :", n, "lois ;", dict(compte), "; écarts :", diff[:5], "; durée", round(time.time() - t0, 1), "s")
# (3) lois invalides : facteurs
for s in R["suites"]:
    for t in s["tentatives"]:
        if t["loi"] is None and t["motif_invalidite"] != "appel échoué après une reprise":
            objs = [o for o in ag._objets_json(t["reponse_caviardee"]) if isinstance(o, dict) and "loi" in o]
            fac = []
            def cherche(x):
                if isinstance(x, dict):
                    if x.get("type") == "echelle":
                        fac.append(x.get("facteurs"))
                    for v in x.values():
                        cherche(v)
                elif isinstance(x, list):
                    for v in x:
                        cherche(v)
            cherche(objs[-1]["loi"] if objs else None)
            print("invalide :", s["monde"], s["fournisseur"], s["condition"] + "|" + s["juge"], "carte", s["carte"], "k", t["k"], "facteurs d'échelle :", fac)
