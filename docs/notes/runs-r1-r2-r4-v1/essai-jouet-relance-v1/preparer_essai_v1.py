"""Essai jouet de bout en bout de la relance de R1 (hors réseau, processeur) : dépôt jetable tiré du commit du code
(`git archive`), run de P3 jouet, fiches « de P3 » où un épisode a un jeton de fin substitué (cas sain de la règle A),
table calculée par `resolution_tokenisation_v1`, configurations jouet (saine, et table falsifiée), dépôt nu servant de
« dépôt distant » à l'amorce v2.

    PYTHONPATH=<arbre>/src:<arbre>/tests python preparer_essai_v1.py <arbre> <commit> <dossier d'essai>
"""
import copy
import json
import subprocess
import sys
from pathlib import Path

arbre, commit, essai = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3]).resolve()
essai.mkdir(parents=True, exist_ok=False)
src = essai / "depot-source"
src.mkdir()
archive = subprocess.run(["git", "-C", str(arbre), "archive", commit, "src", "tests", "scripts", "prereg",
                          "pyproject.toml", "requirements-cpu.txt", "requirements-gpu.txt", ".gitignore",
                          "docs/sources/invites-2606.08892-v1"], capture_output=True, check=True).stdout
subprocess.run(["tar", "-x", "-C", str(src)], input=archive, check=True)


def git(*a):
    subprocess.run(["git", "-C", str(src), *a], check=True, capture_output=True)


git("init", "-q", "-b", "main")
git("config", "user.email", "essai@example.invalid")
git("config", "user.name", "essai")
git("add", "-A")
git("commit", "-q", "-m", "arbre du commit du code")

from controle_ia.premier_test_ia import run as rp  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
import test_premier_test_ia_run as tp  # noqa: E402
import test_runs_nuit_v2 as t2  # noqa: E402

vraie = rp.creer_manifeste
rp.creer_manifeste = lambda *a, entropie=None, **k: vraie(*a, entropie=20261017 if entropie is None else entropie, **k)
(src / "essai").mkdir()
f = tp._taches(src)
git("add", "-A")
git("commit", "-q", "-m", "tâches jouet")
c = tp._config(src / "essai")
rp.executer(c, src, t2.RUN_P3, None, str(f), autoriser_depot_sale=True)
alt, e, pas, autre = t2._fiches_avec_fin_substituee(src, f, c, src / "essai")
t = t2._table(src, f, c, alt, src / "essai" / "table.json")
print("table jouet :", json.dumps(t["comptes"], ensure_ascii=False), "épisode corrigé", e, "pas", pas, "fin", autre)


def relatif(conf):
    return {k: (str(Path(v).relative_to(src)) if isinstance(v, str) and v.startswith(str(src)) else v)
            for k, v in conf.items()}


conf = relatif(t2._config_v2(src, f, c, src / "essai" / "table.json", chemin_fiches=str(alt),
                             tolerance_fidelite=t2.TOL_FABRIQUE))
(src / "essai" / "rejeu.json").write_text(json.dumps(conf, sort_keys=True, indent=1), encoding="utf-8")
sceller(src / "essai" / "rejeu.json")
t_faux = copy.deepcopy(t)
defaut = min(int(x) for x in t["fins_du_format"] if int(x) != autre)
t_faux["episodes"][0]["fins"] = {str(pas): defaut}
(src / "essai" / "table-falsifiee.json").write_text(json.dumps(t_faux, sort_keys=True), encoding="utf-8")
sceller(src / "essai" / "table-falsifiee.json")
conf_f = {**conf, "chemin_table_tokenisation": "essai/table-falsifiee.json"}
(src / "essai" / "rejeu-table-falsifiee.json").write_text(json.dumps(conf_f, sort_keys=True, indent=1), encoding="utf-8")
sceller(src / "essai" / "rejeu-table-falsifiee.json")
subprocess.run(["git", "-C", str(src), "add", "-A", "-f", "essai", "donnees", "diag", "runs", "taches.json",
                "taches.json.sha256"], check=True)
git("commit", "-q", "-m", "essai jouet : run source, fiches, table, configurations")
subprocess.run(["git", "clone", "-q", "--bare", str(src), str(essai / "depot.git")], check=True)
print("commit d'essai :", subprocess.run(["git", "-C", str(src), "rev-parse", "HEAD"], capture_output=True,
                                          text=True).stdout.strip())
