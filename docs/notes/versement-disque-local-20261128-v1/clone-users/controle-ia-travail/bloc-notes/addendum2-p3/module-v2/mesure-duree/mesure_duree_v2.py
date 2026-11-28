"""Mesure de la durée de la ligne de commande complète de l'addendum 2 (module v2), sur un dépôt jouet de taille réelle.

Données synthétiques seulement (aides du fichier de tests v2 et du code gelé) : 60 tâches, 4 conditions, 10 pas, 600
actions par condition, 430 sondes (2 principales, 214 sondes de plancher chacune), formes et coûts plantés. Dépôt git jouet
construit sous `module-v2/tmp/` (code de `src/` copié, préenregistrement de P3, run source décisif scellé, lecture décisive
par le code gelé, commit de N-025, module v2 aux constantes du run jouet, tests v2, texte de l'addendum 2 scellé : S2), puis
la vraie commande, dans un processus séparé, aux paramètres du texte (10 000 tirages), sur deux copies du dépôt. Mesures :
durée murale de la commande, mémoire maximale du processus, durée des seuls imports, durée de la fonction pure seule.
Le dépôt jouet est supprimé à la fin. Résultat imprimé (JSON) et écrit dans `mesure-duree-v2.json`.

Usage (depuis la racine du dépôt de travail) : PYTHONPATH=src python -B <ce fichier>
"""
import sys

sys.dont_write_bytecode = True

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import platform  # noqa: E402
import resource  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pytest  # noqa: E402

ICI = Path(__file__).resolve().parent
V2 = ICI.parent
sys.path.insert(0, str(V2))

import test_audit_verdict_p3_v1 as T  # noqa: E402

av, lp = T.av, T.lp
TMP = V2 / "tmp" / "mesure-duree"
RUN, LEC = "20261020-100000-p3-synthetique-mesure", "20261020-110000-lecture-mesure"
N_TACHES, N_PLANCHER = 60, 214


def construire(racine: Path) -> dict:
    d = racine / "depot"
    d.mkdir(parents=True)
    T.git(d, "init", "-q", "-b", "main")
    T.git(d, "config", "user.email", "test@example.invalid")
    T.git(d, "config", "user.name", "test")
    shutil.copytree(T.DEPOT / "src" / "controle_ia", d / "src" / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (d / "README").write_text("x\n")
    T.committer(d)
    c0 = T._rev(d)
    sha_config = hashlib.sha256(T.config_canonique(T.CONFIG_SOURCE)).hexdigest()
    T._prereg_conforme(d / av.PREREG_P3, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{av.ENTROPIE_P3}`",
                                          f"- Configuration de P3 (empreinte canonique) : `{sha_config}`"])
    T.committer(d)
    src = T._src(0, n_taches=N_TACHES, n_pl=N_PLANCHER)
    t = src["tables"]
    taille = {"actions": int(t["condition"].size), "sondes": int(len(t["noms_sondes"])),
              "taches": int(np.unique(t["tache"]).size), "pas": int(np.unique(t["pas"]).size),
              "par_condition": {c: int((t["condition"] == c).sum()) for c in T.CONDITIONS_TEXTE}}
    assert taille == {"actions": 2400, "sondes": 430, "taches": 60, "pas": 10,
                      "par_condition": {c: 600 for c in T.CONDITIONS_TEXTE}}, taille
    T._ecrire_run_source(d, RUN, src, T._textes_lisibles(src))
    T.committer(d)
    with pytest.MonkeyPatch.context() as mp:            # lecture décisive synthétique (moins de tirages des aires)
        mp.setattr(lp, "TIRAGES_AIRE", 300)
        mp.setattr(lp, "exiger_code_importe_sous", lambda racine: None)
        lp.analyser(d, RUN, LEC, av.PREREG_P3, av.ENTROPIE_P3, autoriser_depot_sale=True)
    T.committer(d)
    (d / "registres").mkdir()
    (d / "registres" / "decisions.md").write_text("N-025 : option (a), synthétique\n", encoding="utf-8")
    T.committer(d)
    n025 = T._rev(d)
    module, tests = d / av.CHEMIN_MODULE, d / av.CHEMIN_TESTS
    module.parent.mkdir(parents=True)
    module.write_bytes(T._module_pour(RUN, LEC, n025, T._entrees(d, RUN, LEC)))
    tests.write_bytes(Path(T.__file__).read_bytes())
    T._prereg_conforme(d / av.PREREG_ADDENDUM2, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{av.ENTROPIE_P3}`",
                                                 f"- Module de l'addendum 2 (sha256) : `{T.empreinte(module)}`",
                                                 f"- Tests du module (sha256) : `{T.empreinte(tests)}`"])
    T.committer(d)
    return {"depot": d, "taille": taille}


def commande(d: Path, run_add: str) -> dict:
    env = {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    avant = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    debut = time.perf_counter()
    r = subprocess.run([sys.executable, "-B", av.CHEMIN_MODULE, "--run-source", RUN, "--lecture", LEC, "--run-addendum2",
                        run_add, "--prereg", av.PREREG_ADDENDUM2, "--entropie", str(av.ENTROPIE_P3)],
                       cwd=d, env=env, capture_output=True, text=True, timeout=3600)
    duree = time.perf_counter() - debut
    maxrss = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    if r.returncode != 0:
        raise SystemExit(f"commande en échec : {r.stderr[-2000:]}")
    corps = T.verifier_resultat(d, d / "diag" / run_add / "lecture-addendum2-p3.json")["resultat"]
    return {"duree_s": round(duree, 2), "memoire_max_mo": round(max(avant, maxrss) / 1024.0, 0),
            "tirages": corps["constantes"]["tirages"], "controles": corps["nombre_de_controles"]["ecrits"],
            "lus": corps["nombre_de_controles"]["lus"], "sortie": json.loads(r.stdout.strip().splitlines()[-1])}


def imports_seuls(d: Path) -> float:
    env = {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    code = ("import time; t = time.perf_counter(); import importlib.util; "
            f"s = importlib.util.spec_from_file_location('m', {av.CHEMIN_MODULE!r}); m = importlib.util.module_from_spec(s); "
            "s.loader.exec_module(m); print(time.perf_counter() - t)")
    debut = time.perf_counter()
    subprocess.run([sys.executable, "-B", "-c", code], cwd=d, env=env, capture_output=True, text=True, check=True)
    return round(time.perf_counter() - debut, 2)


def fonction_pure(d: Path) -> float:
    m = T._charger_copie(d / av.CHEMIN_MODULE, "module_mesure")
    source = lp.charger_source(d, RUN)
    lecture = json.loads((d / "diag" / LEC / "lecture-p3.json").read_text(encoding="utf-8"))["resultat"]
    g = T.graines(m.cles_addendum2(), m.ENTROPIE_P3)
    debut = time.perf_counter()
    m.analyser_addendum2(source, lecture, g)
    return round(time.perf_counter() - debut, 2)


def main():
    if TMP.exists():
        shutil.rmtree(TMP)
    TMP.mkdir(parents=True)
    try:
        debut = time.perf_counter()
        g = construire(TMP / "gabarit")
        construction = round(time.perf_counter() - debut, 1)
        mesures = []
        for k in range(2):
            d = TMP / f"copie-{k}" / "depot"
            shutil.copytree(g["depot"], d, symlinks=True)
            mesures.append(commande(d, f"20261020-15000{k}-addendum2-p3"))
        sortie = {
            "taille": g["taille"], "construction_du_depot_jouet_s": construction,
            "ligne_de_commande": mesures,
            "imports_seuls_s": imports_seuls(TMP / "copie-0" / "depot"),
            "fonction_pure_s": fonction_pure(TMP / "copie-0" / "depot"),
            "machine": {"architecture": platform.machine(), "coeurs": os.cpu_count(), "python": platform.python_version(),
                        "numpy": np.__version__},
            "module_sha256": T.empreinte(Path(av.__file__)), "tests_sha256": T.empreinte(Path(T.__file__)),
        }
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    (ICI / "mesure-duree-v2.json").write_text(json.dumps(sortie, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(sortie, ensure_ascii=False))


if __name__ == "__main__":
    main()
