"""Contexte écrit par le noyau pour une génération notée et pour une défense de confrontation, avec les bornes de la
v6 (160 appels, 37 USD, 1 800 s, 30 recherches, 20 téléchargements, sans gradient, une ronde de conception à 10 USD).
Organismes d'essai du dépôt seulement. On compare les clés et les budgets écrits dans `contexte.json`."""
import json, pathlib, sys, io, contextlib
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3.noyau import cli
RACINE = pathlib.Path("/srv/copie/essaim-m3-refonte-v1")
course = pathlib.Path("/srv/sorties/audit-defense/course")
tampon = io.StringIO()
with contextlib.redirect_stdout(tampon):
    code = cli.principal(["simuler", "--sortie", str(course), "--generations", "2", "--graine", "11", "--n-train", "6", "--n-test", "6", "--n-final", "6",
                          "--appels-max", "160", "--usd-par-generation", "37", "--temps-max", "1800", "--plafond-total", "500",
                          "--recherches-max", "30", "--telechargements-max", "20", "--entrainements-max", "0",
                          "--rondes-conception-max", "1", "--usd-max-conception", "10",
                          "--especes", "GEMINI_ARGON", "--organisme-impose", f"essai={RACINE / 'tests' / 'fixtures' / 'organisme_factice' / 'organisme'}@anthropic",
                          "--confronter"])
assert code == 0
sortie_standard = json.loads(tampon.getvalue())
m = json.loads((course / "manifeste-run.json").read_text())
esp = pathlib.Path(m["espace_organismes"])
gen = json.loads((course / "archive" / "gemini-argon" / "g001" / "travail" / "contexte.json").read_text())
conc = json.loads((course / "archive" / "gemini-argon" / "c001" / "travail" / "contexte.json").read_text())
defenses = sorted(esp.rglob("defense/contexte.json"))
dfn = json.loads(defenses[0].read_text())
conf = json.loads(sorted((course / "confrontation").glob("confrontation-v*.json"))[-1].read_text())
journaux_defense = sorted(str(p.relative_to(esp)) for p in esp.rglob("defense/noyau/journal-appels.jsonl"))
sortie = {
  "cles_generation": sorted(gen), "cles_defense": sorted(dfn),
  "cles_absentes_de_la_defense": sorted(set(gen) - set(dfn)),
  "budget_generation": gen["budget"], "budget_ronde_conception": conc["budget"], "budget_defense": dfn["budget"],
  "n_taches_test_generation": len(gen["taches_test"]), "n_taches_test_defense": len(dfn["taches_test"]),
  "generation_dans_defense": dfn["generation"], "generations_max_course": m["generations_max"],
  "phase_dans_generation": gen.get("phase"),
  "paires_applicables": [(p["attaquant"], p["defendeur"], p.get("n_appels"), p.get("cout_usd")) for p in conf["paires"] if p["applicable"]],
  "journaux_de_defense_hors_archive": journaux_defense,
  "journaux_de_defense_scelles": [j for j in journaux_defense if (esp / (j + ".sha256")).exists()],
  "sortie_standard_de_simuler_contient": sorted(sortie_standard),
}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
pathlib.Path("/srv/sorties/audit-defense/resultat.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
