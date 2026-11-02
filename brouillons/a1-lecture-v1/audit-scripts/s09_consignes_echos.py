"""Audit des consignes, des échos, des lois et des motifs (section 7, A1 = A2 = A5) sur la sortie scellée.
1. Reconstruit chaque consigne avec la fonction gelée `consigne` (cartes rejouées depuis l'entropie du texte scellé ;
   historique refait depuis la sortie, lois relues dans la réponse caviardée pour garder l'ordre des clés) et compare son
   SHA-256 à `consigne_sha256`.
2. Vérifie dans chaque consigne reconstruite : historique présent (k − 1 entrées), retour attendu présent (retour), aucun
   verdict ni richesse (témoin).
3. Compte les échos à la main (normalisation et extraction écrites ici, indépendantes de `nombre_lu`).
4. Recompte la classe couverte et « hors classe » ; types de lois ; motifs d'invalidité.
Écrit travail/consignes-v1.json et travail/echos-v1.csv. Aucun appel, aucune écriture hors de a1-audit-v1/travail."""
import json, math, sys, hashlib, csv, collections, re
ORCH = "/home/claude/ideation-organism/orchestrator"
sys.path.insert(0, ORCH)
from pole import attaque_goodhart_v2 as ag  # noqa: E402
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
E = int(hashlib.sha256(open(ORCH + "/prereg/preenregistrement-attaque-goodhart-v2-v1.md", "rb").read()).hexdigest(), 16)
cartes = {(w, c): ag.carte(E, c, w) for w in ("W1", "W2") for c in range(12)}
res = collections.Counter()
problemes = []
echos = []
types = collections.Counter()
for s in R["suites"]:
    c = cartes[(s["monde"], s["carte"])]
    cond, juge = s["condition"], s["juge"]
    hist = []
    for t in s["tentatives"]:
        k = t["k"]
        texte = ag.consigne(c, hist, cond, k, juge)
        ok = hashlib.sha256(texte.encode("utf-8")).hexdigest() == t["consigne_sha256"]
        res[("consigne_sha256_conforme", ok)] += 1
        if not ok:
            problemes.append((s["monde"], s["fournisseur"], cond, juge, s["carte"], k, "empreinte de consigne"))
        # contenu de la consigne reconstruite (donc de la consigne envoyée à l'adaptateur, puisque l'empreinte concorde)
        i, j = texte.find(ag.DEBUT_HIST), texte.find(ag.FIN_HIST)
        h = json.loads(texte[i + len(ag.DEBUT_HIST):j])
        res[("historique_de_k_moins_1_entrees", len(h) == k - 1)] += 1
        if cond == "temoin":
            fuite = any(("verdict" in e or "log_w_max" in e) for e in h) or "Tu ne recevras aucun verdict" not in texte
            res[("temoin_sans_verdict_ni_richesse", not fuite)] += 1
            mots = [m for m in ("promue", "log W max de ta tentative") if m in texte[i:j]]
            res[("temoin_historique_sans_mot_promue", not mots)] += 1
        else:
            if h and isinstance(h[-1], dict) and "log_w_max" in h[-1]:
                res[("retour_attendu_present_dans_la_consigne", True)] += 1
                res[("retour_attendu_egal_au_champ_ecrit", h[-1]["log_w_max"] == t.get("retour_attendu"))] += 1
            elif k >= 2:
                res[("retour_sans_richesse_precedente (tentative précédente non jugée)", True)] += 1
        res[("description_du_juge_de_la_suite", ag.description_du_juge(juge, c["L"]) in texte)] += 1
        # loi : relue dans la réponse caviardée (ordre des clés d'origine), comparée à la loi écrite
        loi, motif, retour_lu = t["loi"], t["motif_invalidite"], t["retour_lu"]
        if isinstance(t["reponse_caviardee"], str):
            loi2, motif2, retour2 = ag.analyser_reponse(t["reponse_caviardee"])
            res[("reponse_caviardee_relue_donne_la_meme_loi", loi2 == loi and motif2 == motif and retour2 == retour_lu)] += 1
            if loi2 == loi:
                loi = loi2  # ordre d'origine des clés
        entree = {"tentative": k, "loi": loi if loi is not None else motif}
        v = t["verdict"]
        if v is not None and v["statut"] == "evaluation_impossible":
            entree["non_jugee"] = f"évaluation impossible ({v['motif']})"
        elif loi is None:
            entree["non_jugee"] = motif
        if cond == "retour" and v is not None and v["statut"] != "evaluation_impossible":
            entree["verdict"] = "promue" if v["promue"] else "non promue"
            entree["log_w_max"] = round(v["log_w_max"], 2) if math.isfinite(v["log_w_max"]) else None
        # écho, compté à la main : tentative k ≥ 2 du bras retour dont la précédente a une richesse
        if cond == "retour" and k >= 2:
            prec = s["tentatives"][k - 2]
            pv = prec["verdict"]
            attendu = round(pv["log_w_max"], 2) if (pv is not None and pv["statut"] != "evaluation_impossible" and math.isfinite(pv["log_w_max"])) else None
            if attendu is not None:
                brut = retour_lu
                if isinstance(brut, bool) or brut is None:
                    lu = None
                elif isinstance(brut, (int, float)):
                    lu = float(brut)
                else:
                    s2 = str(brut).replace("−", "-").replace("–", "-")
                    m = re.search(r"[-+]?[0-9]+(?:[.,][0-9]+)?", s2)
                    lu = float(m.group(0).replace(",", ".")) if m else None
                exact = lu is not None and abs(lu - attendu) <= 0.005 + 1e-9
                echos.append({"monde": s["monde"], "fournisseur": s["fournisseur"], "juge": juge, "carte": s["carte"], "k": k,
                              "attendu": attendu, "retour_lu_brut": brut, "lu": lu, "exact_main": exact,
                              "echo_exact_code": t.get("echo_exact"), "retour_attendu_code": t.get("retour_attendu")})
        hist.append(entree)
        if t["loi"] is not None:
            types[(s["monde"], s["fournisseur"], f"{cond}|{juge}", t["loi"]["type"])] += 1
            couverte = ag.structurellement_couverte(t["loi"], c["L"])
            hc = ag.hors_classe(t["loi"], c["L"], t["verdict"]["log_w_max"])
            res[("couverte_recalculee_egale", couverte == t["couverte"])] += 1
            res[("hors_classe_recalcule_egal", hc == t["hors_classe"])] += 1
print("contrôles (clé, vrai/faux) → nombre de tentatives :")
for k in sorted(res, key=str):
    print("  ", k, res[k])
print("problèmes :", problemes[:10])
# échos : compte à la main contre le code, par monde et juge (instrument = retour|v8)
agg = collections.defaultdict(lambda: [0, 0, 0])
for e in echos:
    a = agg[(e["monde"], e["juge"], e["fournisseur"])]
    a[0] += 1; a[1] += e["exact_main"]; a[2] += bool(e["echo_exact_code"])
print("échos (monde, juge, fournisseur) → [attendus, exacts comptés à la main, exacts selon le code] :", {str(k): v for k, v in sorted(agg.items())})
print("désaccords main/code :", [e for e in echos if e["exact_main"] != bool(e["echo_exact_code"]) or e["attendu"] != e["retour_attendu_code"]][:5])
formes = collections.Counter(type(e["retour_lu_brut"]).__name__ + (":" + ("virgule" if "," in str(e["retour_lu_brut"]) else "point")) for e in echos)
print("formes des échos :", dict(formes))
with open(B + "travail/echos-v1.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(echos[0]))
    w.writeheader(); w.writerows(echos)
print("types de lois jugées (monde, fournisseur, suite, type) :")
for k in sorted(types):
    print("  ", k, types[k])
inv = [(s["monde"], s["fournisseur"], s["condition"] + "|" + s["juge"], s["carte"], t["k"], t["motif_invalidite"]) for s in R["suites"] for t in s["tentatives"]
       if t["loi"] is None and t["motif_invalidite"] != "appel échoué après une reprise"]
print("lois invalides :", inv)
json.dump({"controles": {str(k): v for k, v in res.items()}, "problemes": problemes, "echos_par_case": {str(k): v for k, v in agg.items()},
           "types": {str(k): v for k, v in types.items()}, "invalides": inv}, open(B + "travail/consignes-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
