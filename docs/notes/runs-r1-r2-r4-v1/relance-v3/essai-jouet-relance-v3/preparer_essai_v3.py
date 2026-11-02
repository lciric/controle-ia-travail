"""Essai jouet de bout en bout de la relance de R1 sur la table v3 (hors réseau, processeur) : amorce et script
d'instance v3 au commit cité, bornes de durée réglables (PLAFOND_AMORCE_MIN, DELAI_REJEU_MIN).

Dépôt jetable tiré du commit (`git archive`) ; run de P3 jouet ; fiches « de P3 » où deux épisodes identiques ont un
jeton de fin substitué ; table v3 jouet (une entrée « fins », une entrée « identifiants ») construite par le code du
rejeu à graine (`tests/test_rejeu_activations_v3._table_v3`, celle des essais du module) ; configuration jouet v3
(saine) ; table v3 falsifiée (identifiants d'une action remplacés par ceux de la reconstruction de base : forme
conforme, empreinte de P3 non retrouvée) et sa configuration ; dépôt nu servant de « dépôt distant » à l'amorce. Puis un
dépôt témoin, même arbre, où le module du rejeu est remplacé par un témoin qui dort 150 s (essai de la coupure de
l'étape par DELAI_REJEU_MIN) ; son propre dépôt nu.

    cd <arbre> && PYTHONPATH=<arbre>/src:<arbre>/tests python preparer_essai_v3.py <arbre> <commit> <dossier d'essai>

(le run de P3 jouet lit ses faits sous `donnees/` relativement au répertoire courant : lancer depuis l'arbre)
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
archive = subprocess.run(["git", "-c", "http.proxy=http://127.0.0.1:9", "-C", str(arbre), "archive", commit, "src",
                          "tests", "scripts", "prereg", "pyproject.toml", "requirements-cpu.txt", "requirements-gpu.txt",
                          ".gitignore", "docs/sources/invites-2606.08892-v1", "donnees/T0.7-faits-repe-v1",
                          "donnees/T0.7-models-under-pressure-v1"], capture_output=True, check=True).stdout
subprocess.run(["tar", "-x", "-C", str(src)], input=archive, check=True)


def git(depot, *a):
    subprocess.run(["git", "-C", str(depot), *a], check=True, capture_output=True)


def init(depot, message):
    git(depot, "init", "-q", "-b", "main")
    git(depot, "config", "user.email", "essai@example.invalid")
    git(depot, "config", "user.name", "essai")
    git(depot, "add", "-A")
    git(depot, "commit", "-q", "-m", message)


init(src, f"arbre du commit {commit}")

from controle_ia.premier_test_ia import run as rp  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
import test_premier_test_ia_run as tp  # noqa: E402
import test_rejeu_activations_v3 as t3  # noqa: E402
import test_runs_nuit_v2 as t2  # noqa: E402

vraie = rp.creer_manifeste
rp.creer_manifeste = lambda *a, entropie=None, **k: vraie(*a, entropie=20261017 if entropie is None else entropie, **k)
e_dir = src / "essai"
e_dir.mkdir()
f = tp._taches(src)
git(src, "add", "-A")
git(src, "commit", "-q", "-m", "tâches jouet")
c = tp._config(e_dir)
rp.executer(c, src, t2.RUN_P3, None, str(f), autoriser_depot_sale=True)
alt, choisis = t3._fiches_avec_fins_substituees(src, f, c, e_dir, 2)
(ea, _, _), (eb, pas_b, _) = choisis
t2_, p2, t3_, p3, ids = t3._table_v3(src, f, c, alt, e_dir, [eb])
print("table v3 jouet :", json.dumps(t3_["comptes"], ensure_ascii=False))
print("méthodes :", sorted(x["methode"] for x in t3_["episodes"]))


def relatif(conf):
    return {k: (str(Path(v).relative_to(src)) if isinstance(v, str) and v.startswith(str(src)) else v)
            for k, v in conf.items()}


conf = relatif(t3._config_v3(src, f, c, p3, chemin_fiches=str(alt), tolerance_fidelite=t2.TOL_FABRIQUE))
(e_dir / "rejeu-v3.json").write_text(json.dumps(conf, sort_keys=True, indent=1), encoding="utf-8")
sceller(e_dir / "rejeu-v3.json")
# table falsifiée (comme l'essai jouet v2) : l'entrée de forme ancienne « fins » reçoit le jeton de fin par défaut au
# lieu de celui « de P3 » ; forme conforme, empreinte de P3 non retrouvée → arrêt à la revérification au chargement
t_faux = copy.deepcopy(t3_)
(pas_a, autre_a), = [(p, a) for e, p, a in choisis if e == ea]
for ent in t_faux["episodes"]:
    if ent["episode"] == ea:
        assert ent["methode"] == "fins" and ent["fins"] == {str(pas_a): autre_a}
        ent["fins"] = {str(pas_a): min(int(x) for x in t_faux["fins_du_format"] if int(x) != autre_a)}
p_faux = e_dir / "table-v3-falsifiee.json"
p_faux.write_text(json.dumps(t_faux, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
sceller(p_faux)
conf_f = {**conf, "chemin_table_tokenisation": "essai/table-v3-falsifiee.json",
          "table_tokenisation_sha256": __import__("hashlib").sha256(p_faux.read_bytes()).hexdigest()}
(e_dir / "rejeu-v3-table-falsifiee.json").write_text(json.dumps(conf_f, sort_keys=True, indent=1), encoding="utf-8")
sceller(e_dir / "rejeu-v3-table-falsifiee.json")
subprocess.run(["git", "-C", str(src), "add", "-A", "-f", "essai", "donnees", "diag", "runs", "taches.json",
                "taches.json.sha256"], check=True)
git(src, "commit", "-q", "-m", "essai jouet v3 : run source, fiches, tables v3 (saine et falsifiée), configurations")
subprocess.run(["git", "clone", "-q", "--bare", str(src), str(essai / "depot.git")], check=True)
print("commit d'essai :", subprocess.run(["git", "-C", str(src), "rev-parse", "HEAD"], capture_output=True,
                                          text=True).stdout.strip())

# dépôt témoin : même arbre, module du rejeu remplacé par un témoin qui dort 150 s (coupure de l'étape à 1 min)
temoin = essai / "depot-temoin"
subprocess.run(["cp", "-a", str(src), str(temoin)], check=True)
(temoin / "src/controle_ia/runs_nuit/rejeu_activations_v3.py").write_text(
    '"""Témoin de l\'essai de DELAI_REJEU_MIN : dort 150 s (aucun calcul)."""\nimport sys\nimport time\n\n'
    'print("PROGRES 2026-11-02T00:00:00Z etape=temoin_sommeil duree_s=150", file=sys.stderr, flush=True)\n'
    'time.sleep(150)\nprint("{}")\n', encoding="utf-8")
git(temoin, "add", "-A")
git(temoin, "commit", "-q", "-m", "témoin : module du rejeu remplacé par un sommeil de 150 s")
subprocess.run(["git", "clone", "-q", "--bare", str(temoin), str(essai / "depot-temoin.git")], check=True)
print("commit témoin :", subprocess.run(["git", "-C", str(temoin), "rev-parse", "HEAD"], capture_output=True,
                                         text=True).stdout.strip())
