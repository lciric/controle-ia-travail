"""Audit des droits posés par le noyau sur la vue d'archive après une course ordinaire en simulation (organisme
d'essai du dépôt, deux lignées auto-écrites simulées, deux générations), noyau root avec isolation d'utilisateur.
On lit seulement les modes et propriétaires des dossiers ; aucun organisme particulier n'est écrit."""
import json, os, pathlib, stat, sys
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3.noyau import cli

course = pathlib.Path("/srv/sorties/audit-droits/course")
assert cli.principal(["simuler", "--sortie", str(course), "--generations", "2", "--graine", "7", "--n-train", "6", "--n-test", "6",
                      "--appels-max", "30", "--especes", "GEMINI_ARGON", "CLAUDE_OPUS_5_5", "--entrainements-max", "0"]) == 0
m = json.loads((course / "manifeste-run.json").read_text())
esp = pathlib.Path(m["espace_organismes"])
def mode(p):
    s = p.stat()
    return {"chemin": str(p.relative_to(esp)) if p != esp else ".", "mode": oct(stat.S_IMODE(s.st_mode)), "uid": s.st_uid,
            "autres_lisent": bool(s.st_mode & stat.S_IROTH), "autres_traversent": bool(s.st_mode & stat.S_IXOTH)}
vue = esp / "archive_vue"
lignes = [mode(esp), mode(vue)] + [mode(p) for p in sorted(vue.iterdir())] + \
         [mode(p) for p in sorted((vue / "gemini-argon").iterdir())] + [mode(vue / "gemini-argon" / "g000" / "resume.json")] + \
         [mode(esp / "travail"), mode(esp / "travail" / "gemini-argon")]
ctx = json.loads((course / "archive" / "claude-opus-5-5" / "g001" / "travail" / "contexte.json").read_text())
sortie = {"isolation": m["isolation"], "uids": {l: e.get("uid") for l, e in json.loads(sorted(course.glob("rapport-v*.json"))[-1].read_text())["lignees"].items()},
          "dossier_archive_donne_a_claude_opus": ctx["dossier_archive"], "modes": lignes,
          "contrat_dit": "dossier_archive : les générations passées de ta lignée (chemin en lecture seule)"}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
pathlib.Path("/srv/sorties/audit-droits/resultat.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
