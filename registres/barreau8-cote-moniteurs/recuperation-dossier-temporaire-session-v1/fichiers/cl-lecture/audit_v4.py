"""Ouverture de l'audit par sa commande : livraison fabriquée par les montages des essais de la lecture v4 (monde à effet planté,
`Monde(sf, graine=1, effets=EFFET)`), dépôt d'essai monté par `monter`, puis `lecture` et `audit` joués par l'enveloppe à cadre
réduit, en sous-processus. Argument : dossier de travail (neuf)."""
from __future__ import annotations

import dataclasses
import json
import os
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
ICI = Path(__file__).resolve().parent
sys.path[:0] = [str(DEPOT / "src"), str(DEPOT / "tests")]
import test_barreau8_moniteurs_lecture_v4 as TL  # noqa: E402

base = Path(sys.argv[1])
base.mkdir(parents=True)
depot = base / "depot"
depot.mkdir()
for a in (["init", "-q", "-b", "main"], ["config", "user.email", "test@example.invalid"], ["config", "user.name", "test"]):
    subprocess.run(["git", "-C", str(depot), *a], check=True, capture_output=True)
(depot / "README").write_text("x\n")
TL.committer(depot)
sf = TL.fabriquer_sondes(base / "sondes")
monde = TL.Monde(sf, graine=1, effets=TL.EFFET)
a = TL.monter(depot, monde)
cadre = sf["cadre"]
(base / "cadre.json").write_text(json.dumps({
    "tailles": dataclasses.asdict(cadre.tailles),
    "identites": {"fichiers": cadre.identites.fichiers, "sondes": [dataclasses.asdict(i) for i in cadre.identites.sondes]},
    "recette": dataclasses.asdict(cadre.recette), "temoin_plante": [list(t) for t in cadre.temoin_plante], "modele": cadre.modele}),
    encoding="utf-8")
env = dict(os.environ, PYTHONPATH=str(DEPOT / "src"), CADRE_JOUET=str(base / "cadre.json"))


def lancer(nom, argv):
    r = subprocess.run([sys.executable, str(ICI / "cli_jouet_v4.py"), *argv], cwd=depot, env=env, capture_output=True, text=True,
                       timeout=500)
    print(f"=== {nom} : code {r.returncode}\n{r.stdout[-1500:]}" + (f"\n[err] {r.stderr[-1500:]}" if r.stderr.strip() else ""), flush=True)
    return r


r = lancer("lecture (enveloppe)", a["lecture"])
TL.committer_si_sale(depot)
sortie = json.loads((depot / "diag" / "20261119-000001-lecture" / "lecture-sondes-barreau8-v1.json").read_text())["resultat"]
print("lignes :", [l["ligne"] for l in sortie["lignes_declenchees"]], "; déclencheurs :",
      {k: v for k, v in sortie["declencheurs_de_l_audit"].items() if v})
r = lancer("audit (enveloppe)", ["audit", *a["commun"], *a["sondes"]])
for p in (depot / "diag" / "20261119-000001-lecture").glob("audit-*.json"):
    corps = json.loads(p.read_text())["resultat"]
    print("audit écrit :", p.name, "; ligne", corps["ligne"], "; défauts", corps["defauts_etablis"], "; relectures", corps["relectures"])
