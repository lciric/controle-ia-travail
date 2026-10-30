"""Vérification de GD7-09 : le script v8 ne lance aucune commande (git ni autre sous-processus) et ne lit aucun commit.

Contrôle 1, analyse syntaxique (`ast`) du script : modules importés (liste fermée : bibliothèque standard utilisée + numpy + scipy.special, ce dernier dans une fonction,
seulement pour la table des quantiles de la copule) ; aucun `subprocess`, aucun appel de `os.system`, `os.popen`, `os.exec*`, `os.spawn*`, `os.posix_spawn`, `os.fork`,
`platform.platform`, `platform.uname` ; aucune chaîne de caractères égale à « git ».
Contrôle 2, piège à sous-processus (R5) : `subprocess.Popen`, `os.system`, `os.popen`, `os.posix_spawn`, `os.fork` sont remplacés par des enregistreurs ; le script est
chargé et `principal()` est exécuté dans ce processus, **avec** `--sortie` (journal, manifeste), la copule (donc l'import de scipy), les strates et `--n80-fiche` ;
le nombre d'appels vus doit être nul. Artefact : après ce passage, un appel volontaire à `subprocess.Popen` doit être vu par le piège (le piège fonctionne).
Contrôle 3, commit déclaré : refus de `--sortie` sans `--commit-declare` ; le texte déclaré se retrouve tel quel dans la sortie et le manifeste, avec l'état « non lu ».

Usage : python3 -I -B verif-sans-git-v8.py SCRIPT_V8 DOSSIER_DE_TRAVAIL_NEUF SORTIE.json
"""
import ast
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys

CHEMIN, TRAVAIL, SORTIE = sys.argv[1:4]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("lancer avec -B")
os.makedirs(TRAVAIL)  # doit être neuf
res = {"script": os.path.abspath(CHEMIN), "script_sha256": hashlib.sha256(open(CHEMIN, "rb").read()).hexdigest()}

# --- contrôle 1
arbre = ast.parse(open(CHEMIN, encoding="utf-8").read())
modules = set()
appels = []
git_chaines = []
for noeud in ast.walk(arbre):
    if isinstance(noeud, ast.Import):
        modules |= {a.name for a in noeud.names}
    elif isinstance(noeud, ast.ImportFrom):
        modules.add(noeud.module)
    elif isinstance(noeud, ast.Call):
        f = noeud.func
        nom = (f.value.id + "." + f.attr) if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) else (f.id if isinstance(f, ast.Name) else "")
        if nom in ("os.system", "os.popen", "os.posix_spawn", "os.fork", "platform.platform", "platform.uname") or nom.startswith(("os.exec", "os.spawn", "subprocess.")):
            appels.append((nom, noeud.lineno))
    elif isinstance(noeud, ast.Constant) and isinstance(noeud.value, str) and noeud.value.strip().lower() == "git":
        git_chaines.append(noeud.lineno)
ADMIS = {"argparse", "csv", "datetime", "hashlib", "json", "math", "numpy", "os", "platform", "re", "shlex", "sys", "time", "scipy.special", "__future__"}
res["controle_1_analyse_syntaxique"] = {"modules_importes": sorted(m for m in modules if m), "hors_liste": sorted(m for m in modules if m and m not in ADMIS),
                                        "appels_de_sous_processus_ou_equivalents": appels, "chaines_egales_a_git": git_chaines,
                                        "conforme": not (modules - ADMIS) and not appels and not git_chaines}

# --- contrôle 2
vus = []


def piege(nom):
    def f(*a, **k):
        vus.append(nom)
        raise RuntimeError("sous-processus interdit (piège) : " + nom)
    return f


originaux = (subprocess.Popen, os.system, os.popen, getattr(os, "posix_spawn", None), os.fork)
subprocess.Popen, os.system, os.popen, os.posix_spawn, os.fork = (piege("subprocess.Popen"), piege("os.system"), piege("os.popen"), piege("os.posix_spawn"), piege("os.fork"))
spec = importlib.util.spec_from_file_location("v8", CHEMIN)
v8 = importlib.util.module_from_spec(spec)
erreur = None
try:
    spec.loader.exec_module(v8)
    sortie_passage = os.path.join(TRAVAIL, "essai.json")
    COMMIT = "texte de commit déclaré (essai) 0123abcd"
    ancien = sys.argv
    sys.argv = ["x", "--repetitions", "100", "--comparateurs", "3", "--K", "5", "--K-s", "5", "--taux", "0.01", "--deltas", "0.05", "--biais", "0.0125", "--tailles", "30",
                "--lecture-ebh", "A", "--m", "8,2", "--sans-n80", "--n80-fiche", "--echelle-dispersion", "beta", "--combiner-dispersion-a-et-comparateurs",
                "--effet-unite-beta", "0.17", "--rho-comparateurs", "0.17", "--correlation-sujet-comparateurs", "0.5", "--commit-declare", COMMIT, "--sortie", sortie_passage]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            v8.principal()
    finally:
        sys.argv = ancien
except BaseException as e:  # noqa: BLE001
    erreur = f"{type(e).__name__}: {e}"
sain = {"erreur_du_passage_sain": erreur, "appels_au_piege_pendant_le_passage_sain": list(vus)}
sain["scipy_importe"] = "scipy.special" in sys.modules
subprocess.Popen, os.system, os.popen, os.posix_spawn, os.fork = (piege("subprocess.Popen"), piege("os.system"), piege("os.popen"), piege("os.posix_spawn"), piege("os.fork"))
avant = len(vus)
try:
    subprocess.Popen(["true"])  # artefact volontaire
except RuntimeError:
    pass
sain["artefact_vu_par_le_piege"] = len(vus) == avant + 1
subprocess.Popen, os.system, os.popen, os.posix_spawn, os.fork = originaux
sain["appels_au_piege_apres_artefact"] = list(vus)
sain["conforme"] = erreur is None and not sain["appels_au_piege_pendant_le_passage_sain"] and sain["artefact_vu_par_le_piege"] and sain["scipy_importe"]
res["controle_2_piege_a_sous_processus"] = sain

# --- contrôle 3
c3 = {}
ancien = sys.argv
sys.argv = ["x", "--repetitions", "100", "--comparateurs", "1", "--K", "5", "--tailles", "20", "--sortie", os.path.join(TRAVAIL, "sans-commit.json")]
try:
    v8.principal()
    c3["refus_sans_commit_declare"] = None
except SystemExit as e:
    c3["refus_sans_commit_declare"] = str(e)
finally:
    sys.argv = ancien
c3["fichier_ecrit_malgre_le_refus"] = os.path.lexists(os.path.join(TRAVAIL, "sans-commit.json")) or os.path.lexists(os.path.join(TRAVAIL, "sans-commit-journal.txt"))
if erreur is None:
    s = json.load(open(sortie_passage, encoding="utf-8"))
    m = json.load(open(os.path.join(TRAVAIL, "manifeste-essai.json"), encoding="utf-8"))
    c3 |= {"commit_de_la_sortie": s["commit"], "commit_du_manifeste": m["script"]["commit"], "etat_de_la_sortie": s["etat_du_script"],
           "fichiers_ecrits": sorted(os.listdir(TRAVAIL))}
    c3["conforme"] = (c3["refus_sans_commit_declare"] is not None and "commit-declare" in c3["refus_sans_commit_declare"] and not c3["fichier_ecrit_malgre_le_refus"]
                      and s["commit"] == COMMIT == m["script"]["commit"] and s["etat_du_script"].startswith("non lu") and c3["fichiers_ecrits"] == sorted(
                          ["essai.json", "essai-journal.txt", "manifeste-essai.json"]))
else:
    c3["conforme"] = False
res["controle_3_commit_declare"] = c3
res["conforme"] = bool(res["controle_1_analyse_syntaxique"]["conforme"] and sain["conforme"] and c3["conforme"])
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print(json.dumps({k: (v if not isinstance(v, dict) else v.get("conforme")) for k, v in res.items() if k != "script"}, ensure_ascii=False))
