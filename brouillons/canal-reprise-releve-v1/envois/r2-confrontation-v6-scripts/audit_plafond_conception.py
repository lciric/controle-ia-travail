"""Ligne de la liste d'arrêt de la v6 : « plafond total pendant la conception → arret_conception, course arrêtée avant
toute génération notée ». Course ordinaire en simulation (organisme d'essai imposé, aucune espèce d'amorçage), trois
rondes de conception, plafond total bas. On lit les événements du noyau et l'index de l'archive."""
import json, pathlib, sys, io, contextlib
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3.noyau import cli
RACINE = pathlib.Path("/srv/copie/essaim-m3-refonte-v1")
res = {}
for plafond in ("0.3", "0.0"):
    course = pathlib.Path(f"/srv/sorties/audit-plafond/course-{plafond}")
    with contextlib.redirect_stdout(io.StringIO()):
        code = cli.principal(["simuler", "--sortie", str(course), "--generations", "2", "--graine", "5", "--n-train", "6", "--n-test", "6", "--n-final", "6",
                              "--appels-max", "40", "--usd-par-generation", "1.0", "--plafond-total", plafond, "--entrainements-max", "0",
                              "--rondes-conception-max", "3", "--usd-max-conception", "1.0", "--especes",
                              "--organisme-impose", f"essai={RACINE / 'tests' / 'fixtures' / 'organisme_factice' / 'organisme'}@gemini"])
    ev = [json.loads(x) for x in (course / "evenements.jsonl").read_text().splitlines()]
    idx = [json.loads(x) for x in (course / "archive" / "index.jsonl").read_text().splitlines()] if (course / "archive" / "index.jsonl").exists() else []
    res[plafond] = {"code": code,
        "etapes_d_arret": [{k: e.get(k) for k in ("etape", "ronde", "raison")} for e in ev if e["etape"] in ("arret_conception", "arret")],
        "rondes_conception": [(l["generation"], l["statut"], l["cout_usd"]) for l in idx if l.get("phase")],
        "generations_notees": [(l["generation"], l["statut"], l["score"], l["n_appels"], l["cout_usd"]) for l in idx if not l.get("phase")],
        "refus_plafond_derniere_generation": None}
    notees = [l for l in idx if not l.get("phase")]
    if notees:
        r = json.loads((course / "archive" / notees[-1]["chemin"] / "resume.json").read_text())
        res[plafond]["refus_plafond_derniere_generation"] = sum(1 for x in r["refus_noyau"] if x["raison"] == "plafond_usd")
        res[plafond]["n_reponses_derniere_generation"] = r["n_reponses_test"]
    rap = json.loads(sorted(course.glob("rapport-v*.json"))[-1].read_text())
    res[plafond]["depense_totale_usd"] = rap["depense_totale_usd"]
print(json.dumps(res, ensure_ascii=False, indent=1))
pathlib.Path("/srv/sorties/audit-plafond/resultat.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
