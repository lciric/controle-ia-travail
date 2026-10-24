"""Génération 0 du bras adaptatif (issue de la conception) et du bras gelé apparié (`--gel --depuis`) : ce que le
contexte écrit par le noyau leur donne (historique, dossier d'archive, contenu de la vue). Organisme d'essai du dépôt."""
import json, pathlib, sys, io, contextlib, os
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3.noyau import cli
RACINE = pathlib.Path("/srv/copie/essaim-m3-refonte-v1")
base = pathlib.Path("/srv/sorties/audit-g000")
adapt, gele = base / "adaptative", base / "gelee"
with contextlib.redirect_stdout(io.StringIO()):
    assert cli.principal(["simuler", "--sortie", str(adapt), "--generations", "2", "--graine", "21", "--n-train", "6", "--n-test", "6", "--n-final", "6",
                          "--appels-max", "30", "--entrainements-max", "0", "--rondes-conception-max", "2", "--especes", "GEMINI_ARGON"]) == 0
    assert cli.principal(["simuler", "--sortie", str(gele), "--generations", "2", "--graine", "22", "--gel", "--depuis", str(adapt),
                          "--appels-max", "30", "--entrainements-max", "0"]) == 0
def resume(course, g):
    ctx = json.loads((course / "archive" / "gemini-argon" / f"g{g:03d}" / "travail" / "contexte.json").read_text())
    vue = pathlib.Path(ctx["dossier_archive"])
    return {"generation": ctx["generation"], "phase": ctx.get("phase"), "dossier_archive": str(vue),
            "historique": [(h["phase"], h["generation"]) for h in ctx["historique"]],
            "vue_contient": sorted(p.name for p in vue.iterdir()) if vue.exists() else None}
ia = [json.loads(x) for x in (adapt / "archive" / "index.jsonl").read_text().splitlines()]
ig = [json.loads(x) for x in (gele / "archive" / "index.jsonl").read_text().splitlines()]
e_a = next(l["empreinte_organisme"] for l in ia if l["generation"] == 0 and not l.get("phase"))
e_g = next(l["empreinte_organisme"] for l in ig if l["generation"] == 0)
sortie = {"adaptatif_g000": resume(adapt, 0), "adaptatif_g001": resume(adapt, 1), "gele_g000": resume(gele, 0), "gele_g001": resume(gele, 1),
          "meme_organisme_g000": e_a == e_g}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
(base / "resultat.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
