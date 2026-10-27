"""Lecture de la course `duel-simule-1-monde` (duel_proposeurs_v7.py, --moteur simule, 1 monde) : réglages du juge par
bras, verdicts par génération, redites héritières et preuve « même loi, mêmes instances, mêmes issues »."""
import collections, json, os, sys
base = sys.argv[1]
sortie = {}
for bras in ("M-expl", "M-aveugle", "mecanique", "aleatoire"):
    d = os.path.join(base, bras)
    man = json.load(open(os.path.join(d, "manifeste.json")))
    cfg = man["reglages"]["config"]
    b = {"reglages": {k: cfg[k] for k in ("budget_generation_usd", "instants_filles", "part_calibrage", "taille_plan", "taille_plan_filles",
                                          "multiplicite", "nul_archive_ajuste", "plafond_experimentateur_usd", "plafond_verificateur_usd")},
         "max_paires": man["reglages"]["max_paires"], "k_recombinaison": man["reglages"]["k_recombinaison"], "generations": {}}
    for g in range(3):
        j = json.load(open(os.path.join(d, "journal", f"generation-{g:02d}.json")))
        c = collections.Counter(v["verdict_final"] for v in j["fiches"].values())
        gardes = j["gardes_de_redite"]
        motifs = collections.Counter("héritage" if "héritage" in v["motif"] else ("déjà éprouvée" if "déjà éprouvée" in v["motif"]
                                     else ("redite d'une survivante" if "survivante" in v["motif"] else ("accepté" if v["accepte"] else "refus autre")))
                                     for v in gardes.values())
        b["generations"][g] = {"verdicts": dict(c), "non_temoins_jugees": sorted(k for k, v in j["fiches"].items()
                               if v["verdict_final"] in ("survit", "eliminee") and v.get("temoin") is None),
                               "budget": j["budget_generation"], "gardes_de_redite": dict(motifs),
                               "heritages": [(k, v.get("classe"), round(v.get("cumul", 0.0), 3)) for k, v in gardes.items() if "héritage" in v["motif"]],
                               "e_bh_m": sorted({(v.get("pari") or {}).get("multiplicite", {}).get("m") for v in j["fiches"].values()} - {None})}
    sortie[bras] = b
# preuve sur la redite héritière du bras mécanique (G2-F03, classe G1-F11)
d = os.path.join(base, "mecanique")
def eng(gen, ident):
    return json.load(open(os.path.join(d, "archive", "generations", f"generation-{gen:02d}", ident, "experience", "engagement.json")))
def mes(gen, ident):
    return json.load(open(os.path.join(d, "archive", "generations", f"generation-{gen:02d}", ident, "experience", "mesures.json")))
j2 = json.load(open(os.path.join(d, "journal", "generation-02.json")))
preuves = {}
for ident, v in j2["fiches"].items():
    h = (v.get("pari") or {}).get("heritage")
    if not h:
        continue
    parent = h["classe"]
    gen_parent = int(parent.split("-")[0][1:])
    ea, eb = eng(gen_parent, parent), eng(2, ident)
    ia = [json.dumps(i, sort_keys=True) for i in ea["instances"]]; ib = [json.dumps(i, sort_keys=True) for i in eb["instances"]]
    da = dict(zip(ia, mes(gen_parent, parent)["issues"])); db = dict(zip(ib, mes(2, ident)["issues"]))
    communes = set(ia) & set(ib)
    preuves[ident] = {"classe": parent, "cumul_herite": round(h["cumul"], 4), "meme_loi": ea["loi"] == eb["loi"],
                      "instances_communes": f"{len(communes)} sur {len(ia)} et {len(ib)}",
                      "issues_identiques_sur_les_communes": all(da[i] == db[i] for i in communes),
                      "verdict": v["verdict_final"], "log_w_max": round(v["pari"]["log_richesse_max"], 3)}
sortie["preuve_redites_heritieres_mecanique_gen2"] = preuves
print(json.dumps(sortie, ensure_ascii=False, indent=1))
