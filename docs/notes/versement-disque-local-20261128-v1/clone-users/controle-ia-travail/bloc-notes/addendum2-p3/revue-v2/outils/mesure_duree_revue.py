"""Mesure de durée de la contre-lecture v2 (point D) : la vraie commande du module v2, dans un processus séparé, sur un
dépôt jouet de taille réelle (60 tâches, 4 conditions, 10 pas, 600 actions par condition, 2 sondes principales et 214
sondes de plancher chacune : 430 sondes), 10 000 tirages (paramètres du texte). Tables synthétiques seulement (R1).

Usage : python mesure_duree_revue.py <dossier de travail> <journal JSON> [répétitions]
Lancé depuis la racine du dépôt, PYTHONPATH=src:<outils>, REVUE_JOURNAL_R1 posé (garde R1 importée ici).
"""
import json
import os
import resource
import shutil
import subprocess
import sys
import time
from pathlib import Path

import garde_r1_v2  # noqa: F401  (crochet d'audit R1 dans ce processus)

BASE = Path(__file__).resolve().parents[1] / "base"
sys.path.insert(0, str(BASE))
import test_audit_verdict_p3_v1 as T  # noqa: E402  (copie de base : aides du fichier de tests v2)

import numpy as np  # noqa: E402
from controle_ia.manifeste import config_canonique  # noqa: E402
from controle_ia.premier_test_ia import lecture as lp  # noqa: E402
from controle_ia.scellement import empreinte  # noqa: E402

av = T.av
RUN, LEC = "20261020-100000-p3-jouet-taille-reelle", "20261020-110000-lecture-jouet"


def source_taille_reelle():
    """Comme `_src` des tests (coûts et formes plantés), à la taille du run : 60 tâches, 214 sondes de plancher."""
    s = T._source(0, signal="aucun", n_taches=60, n_pl=214, facteur=3.0)
    t = s["tables"]
    rng = np.random.default_rng(10_000)
    n, cond = t["cout"].size, t["condition"]
    c = np.asarray(t["cout"], dtype=np.float64).copy() * 10 ** rng.normal(0.0, 0.15, n)
    for f in av.FORMES:
        t[f] = np.zeros(n, dtype=bool)
    for cc, pr in T.PROBAS.items():
        for f, q in pr.items():
            t[f] = t[f] | ((cond == cc) & (rng.random(n) < q))
    t["cout_plusieurs_nombres"] = t["cout_plusieurs_nombres"] | t["cout_intervalle"]
    u = rng.random(n)
    c = np.where(u < 0.05, np.nan, np.where(u < 0.06, 0.0, c))
    t["cout"], t["cout_groupes_joints"] = c, c.copy()
    return s


def construire(d: Path) -> dict:
    d.mkdir(parents=True)
    T.git(d, "init", "-q", "-b", "main")
    T.git(d, "config", "user.email", "test@example.invalid")
    T.git(d, "config", "user.name", "test")
    shutil.copytree(T.DEPOT / "src" / "controle_ia", d / "src" / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (d / "README").write_text("x\n")
    T.committer(d)
    c0 = T._rev(d)
    sha_config = __import__("hashlib").sha256(config_canonique(T.CONFIG_SOURCE)).hexdigest()
    T._prereg_conforme(d / av.PREREG_P3, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{av.ENTROPIE_P3}`",
                                          f"- Configuration de P3 (empreinte canonique) : `{sha_config}`"])
    T.committer(d)
    src = source_taille_reelle()
    assert src["tables"]["condition"].size == 2400 and len(src["tables"]["noms_sondes"]) == 430
    T._ecrire_run_source(d, RUN, src, T._textes_lisibles(src))
    T.committer(d)
    sauve = (lp.TIRAGES_AIRE, lp.TIRAGES_COUT, lp.exiger_code_importe_sous)
    lp.TIRAGES_AIRE, lp.TIRAGES_COUT, lp.exiger_code_importe_sous = 300, 2000, (lambda racine: None)
    try:
        lp.analyser(d, RUN, LEC, av.PREREG_P3, av.ENTROPIE_P3, autoriser_depot_sale=True)
    finally:
        lp.TIRAGES_AIRE, lp.TIRAGES_COUT, lp.exiger_code_importe_sous = sauve
    T.committer(d)
    (d / "registres").mkdir()
    (d / "registres" / "decisions.md").write_text("N-025 : option (a), synthétique\n", encoding="utf-8")
    T.committer(d)
    n025 = T._rev(d)
    module, tests = d / av.CHEMIN_MODULE, d / av.CHEMIN_TESTS
    module.parent.mkdir(parents=True)
    module.write_bytes(T._module_pour(RUN, LEC, n025, T._entrees(d, RUN, LEC)))
    tests.write_bytes((BASE / "test_audit_verdict_p3_v1.py").read_bytes())
    T._prereg_conforme(d / av.PREREG_ADDENDUM2, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{av.ENTROPIE_P3}`",
                                                 f"- Module de l'addendum 2 (sha256) : `{empreinte(module)}`",
                                                 f"- Tests du module (sha256) : `{empreinte(tests)}` ; nombre de tests "
                                                 f"attendu : `118`"])
    T.committer(d)
    return {"c0": c0, "n025": n025, "S2": T._rev(d)}


def lancer(d: Path, run_add: str) -> dict:
    env = {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    env.pop("REVUE_JOURNAL_R1", None)
    avant = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    debut = time.perf_counter()
    r = subprocess.run([sys.executable, "-B", av.CHEMIN_MODULE, "--run-source", RUN, "--lecture", LEC, "--run-addendum2",
                        run_add, "--prereg", av.PREREG_ADDENDUM2, "--entropie", str(av.ENTROPIE_P3)],
                       cwd=d, env=env, capture_output=True, text=True, timeout=1800)
    duree = time.perf_counter() - debut
    rss = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    corps = json.loads((d / "diag" / run_add / "lecture-addendum2-p3.json").read_text(encoding="utf-8"))["resultat"] \
        if r.returncode == 0 else None
    return {"code": r.returncode, "duree_s": round(duree, 3), "maxrss_enfants_ko": rss, "maxrss_avant_ko": avant,
            "stderr_fin": r.stderr[-400:], "tirages": corps and corps["constantes"]["tirages"],
            "controles": corps and {k: corps["nombre_de_controles"][k] for k in ("ecrits", "lus", "sans_objet")},
            "ligne": corps and corps["issue_primaire"]["ligne"]}


def imports_seuls(d: Path) -> float:
    env = {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    env.pop("REVUE_JOURNAL_R1", None)
    code = ("import time; t=time.perf_counter(); import sys; sys.path.insert(0, 'docs/procedures/P3-addendum2-v1'); "
            "import audit_verdict_p3_v1; print(time.perf_counter()-t)")
    r = subprocess.run([sys.executable, "-B", "-c", code], cwd=d, env=env, capture_output=True, text=True, timeout=600)
    return float(r.stdout.strip().splitlines()[-1])


def main():
    travail, journal = Path(sys.argv[1]), Path(sys.argv[2])
    reps = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    if travail.exists():
        shutil.rmtree(travail)
    gabarit = travail / "gabarit"
    t0 = time.perf_counter()
    info = construire(gabarit)
    construction = time.perf_counter() - t0
    mesures = []
    for k in range(reps):
        d = travail / f"copie{k}"
        shutil.copytree(gabarit, d, symlinks=True)
        mesures.append(lancer(d, f"20261020-1500{k:02d}-addendum2-p3"))
    imp = [imports_seuls(gabarit) for _ in range(3)]
    sortie = {"construction_s": round(construction, 1), "mesures": mesures, "imports_s": [round(x, 3) for x in imp],
              "machine": {"coeurs": os.cpu_count(), "python": sys.version.split()[0], "numpy": np.__version__,
                          "charge_1min": os.getloadavg()[0]}, "info": info}
    journal.write_text(json.dumps(sortie, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in sortie.items() if k != "info"}, ensure_ascii=False)[:3000])


if __name__ == "__main__":
    main()
