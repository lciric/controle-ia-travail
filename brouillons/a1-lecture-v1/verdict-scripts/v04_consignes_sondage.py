"""v04 — sondage des consignes (lecteur du verdict, R13) : pour chaque (monde, fournisseur, condition, juge), régénère la
consigne de deux tentatives (la 1re et la dernière de la suite la plus longue, plus une suite Kimi échouée) par le code
gelé (`carte`, `consigne`, historique rebâti comme `jouer_suite` l. 547-556), compare l'empreinte à `consigne_sha256`,
et vérifie : paragraphe du retour ou du témoin, description du juge de la suite, aucun verdict ni richesse dans
l'historique d'un témoin. Vérifie aussi les 12 cartes de chaque monde (W1 mélange de S1 et S2, π dans [0,3 ; 0,7] ;
W2 par sous-population). Code gelé importé en lecture seule (sys.path), aucune écriture hors du fichier de sortie.
Usage : python3 -I -B v04_consignes_sondage.py ORCHESTRATOR SORTIE.json MANIFESTE.json SORTIE_JSON"""
import hashlib
import json
import math
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import pole.attaque_goodhart_v2 as ag  # noqa: E402

sortie = json.load(open(sys.argv[2], encoding="utf-8"))
manif = json.load(open(sys.argv[3], encoding="utf-8"))
E = int(manif["reglages"]["entropie_racine"])
assert E == int(sortie["preenregistrement"]["sha256"], 16), "entropie ≠ empreinte du texte"
cartes = {(w, c): ag.carte(E, c, w) for w in ("W1", "W2") for c in range(12)}

mondes = {"W1": [], "W2": []}
for (w, c), ca in cartes.items():
    m = ca["monde"]
    if w == "W1":
        ok = (m["type"] == "melange" and m["composantes"] == [ca["L"]["S1"], ca["L"]["S2"]]
              and 0.3 <= m["poids"][0] <= 0.7 and abs(sum(m["poids"]) - 1) < 1e-9)
        mondes[w].append([c, ok, round(m["poids"][0], 3)])
    else:
        ok = m == {"type": "par_sous_population", "lois": {"0": ca["L"]["S1"], "1": ca["L"]["S2"]}}
        mondes[w].append([c, ok])


def historique_jusqua(s, k):
    """Historique servi à la tentative k (entrées des tentatives 1..k-1), comme `jouer_suite`."""
    h = []
    for t in s["tentatives"]:
        if t["k"] >= k:
            break
        if t["loi"] is not None:
            loi, _, _ = ag.analyser_reponse(t["reponse_caviardee"])  # ordre des clés de la réponse
            assert loi == t["loi"], "loi ré-analysée différente de la loi écrite"
        else:
            loi = None
        entree = {"tentative": t["k"], "loi": loi if loi is not None else t["motif_invalidite"]}
        v = t["verdict"]
        if v is not None and v["statut"] == "evaluation_impossible":
            entree["non_jugee"] = f"évaluation impossible ({v['motif']})"
        elif loi is None:
            entree["non_jugee"] = t["motif_invalidite"]
        if s["condition"] == "retour" and v is not None and v["statut"] != "evaluation_impossible":
            entree["verdict"] = "promue" if v["promue"] else "non promue"
            entree["log_w_max"] = round(v["log_w_max"], 2) if math.isfinite(v["log_w_max"]) else None
        h.append(entree)
    return h


echantillon = []
for w in ("W1", "W2"):
    for f in ("argon", "kimi"):
        for cond, j in ag.SUITES:
            sel = [s for s in sortie["suites"] if (s["monde"], s["fournisseur"], s["condition"], s["juge"]) == (w, f, cond, j)]
            longue = max(sel, key=lambda s: (len(s["tentatives"]), -s["carte"]))
            choix = {(longue["carte"], 1), (longue["carte"], len(longue["tentatives"]))}
            for c, k in sorted(choix):
                s = next(x for x in sel if x["carte"] == c)
                t = s["tentatives"][k - 1]
                h = historique_jusqua(s, k)
                texte = ag.consigne(cartes[(w, c)], h, cond, k, j)
                emp = hashlib.sha256(texte.encode("utf-8")).hexdigest()
                echantillon.append({
                    "suite": f"{w}|{f}|{cond}|{j}", "carte": c, "k": k, "statut_tentative":
                        ("loi" if t["loi"] is not None else (t["motif_invalidite"] or "")[:30]),
                    "empreinte_egale": emp == t["consigne_sha256"],
                    "paragraphe_retour": "Recopie dans « retour_lu »" in texte,
                    "paragraphe_temoin": "Tu ne recevras aucun verdict ni aucune richesse" in texte,
                    "juge_v8_decrit": "mise en commun linéaire" in texte,
                    "juge_v7_decrit": "aucun mélange des lois connues entre elles" in texte and "lecture continue" in texte,
                    "historique_longueur": len(h),
                    "verdict_dans_historique_temoin": cond == "temoin" and any("verdict" in e or "log_w_max" in e for e in h)})

ok = all(e["empreinte_egale"] for e in echantillon)
coherent = all((e["paragraphe_retour"] == (e["suite"].split("|")[2] == "retour"))
               and (e["paragraphe_temoin"] == (e["suite"].split("|")[2] == "temoin"))
               and (e["juge_v8_decrit"] == (e["suite"].endswith("v8")))
               and (e["juge_v7_decrit"] == (e["suite"].endswith("v7")))
               and not e["verdict_dans_historique_temoin"] for e in echantillon)
res = {"entropie_egale_empreinte_du_texte": True, "mondes": mondes,
       "mondes_ok": {w: all(x[1] for x in v) for w, v in mondes.items()},
       "echantillon": echantillon, "empreintes_toutes_egales": ok, "contenus_coherents": coherent,
       "taille_echantillon": len(echantillon)}
json.dump(res, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("mondes :", res["mondes_ok"], mondes["W1"])
print("échantillon :", len(echantillon), "empreintes égales :", ok, "contenus cohérents :", coherent)
for e in echantillon:
    print(" ", e["suite"], "c", e["carte"], "k", e["k"], e["statut_tentative"], "hist", e["historique_longueur"],
          "=" if e["empreinte_egale"] else "≠")
