"""Rapproche les coûts du relevé de la sonde v74 (prix de la configuration v12) des prix publics relevés le 14 novembre 2026.
Aucun réseau ; lit le relevé et la configuration ; n'écrit qu'un JSON neuf. Usage : python3 -I rapprocher_prix_v1.py RELEVE CONF SORTIE"""
import hashlib, json, os, sys
releve, conf, sortie = sys.argv[1:4]
if os.path.exists(sortie):
    sys.exit("REFUS : sortie existante")
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
R, C = json.load(open(releve, encoding="utf-8")), json.load(open(conf, encoding="utf-8"))
# prix publics standard, USD par million (entrée, sortie), pages empreintées dans la note
PUBLICS = {"fable52": (8.0, 40.0), "opus55": (4.0, 20.0), "argon": (2.0, 10.0), "astra": (10.0, 50.0)}
APRES_1_DEC = {"argon": (4.0, 20.0)}
def entree(dialecte, u):
    return {"claude": u.get("input_tokens"), "gemini": u.get("promptTokenCount"), "astra": u.get("prompt_tokens")}[dialecte]
lignes, tot = [], {"releve": 0.0, "public": 0.0}
for f in R["appels"]:
    n = f["proposeur"]; p = C["proposeurs"][n]
    e, s = entree(p["dialecte"], f["usage_brut"]), f["sortie_comptee"]
    conf_cout = round((e * p["prix_entree_usd_par_million"] + s * p["prix_sortie_usd_par_million"]) / 1e6, 8)
    pe, ps = PUBLICS[n]
    pub = round((e * pe + s * ps) / 1e6, 8)
    lignes.append({"proposeur": n, "appel": f["appel"], "entree": e, "sortie_comptee": s, "cout_releve": f["cout_usd"],
                   "cout_recalcule_prix_configuration": conf_cout, "cout_prix_publics": pub,
                   "prix_configuration": [p["prix_entree_usd_par_million"], p["prix_sortie_usd_par_million"]], "prix_publics": [pe, ps]})
    tot["releve"] += f["cout_usd"]; tot["public"] += pub
ok = all(abs(l["cout_releve"] - l["cout_recalcule_prix_configuration"]) < 1e-9 for l in lignes)
depasse = sorted(n for n in PUBLICS if any(a > b for a, b in zip(PUBLICS[n], (C["proposeurs"][n]["prix_entree_usd_par_million"], C["proposeurs"][n]["prix_sortie_usd_par_million"]))))
depasse_dec = sorted(n for n, v in APRES_1_DEC.items() if any(a > b for a, b in zip(v, (C["proposeurs"][n]["prix_entree_usd_par_million"], C["proposeurs"][n]["prix_sortie_usd_par_million"]))))
out = {"releve_sha256": sha(releve), "configuration_sha256": sha(conf), "appels": lignes,
       "total_releve": round(tot["releve"], 8), "total_prix_publics": round(tot["public"], 8),
       "couts_du_releve_egaux_aux_prix_de_la_configuration": ok,
       "prix_publics_au_dessus_de_la_configuration": depasse, "idem_apres_le_1er_decembre": depasse_dec}
with open(sortie, "x", encoding="utf-8") as g:
    json.dump(out, g, ensure_ascii=False, indent=1, sort_keys=True)
print(json.dumps({k: out[k] for k in out if k != "appels"}, ensure_ascii=False))
for l in lignes: print(l["proposeur"], l["appel"], l["entree"], l["sortie_comptee"], l["cout_releve"], l["cout_prix_publics"])
