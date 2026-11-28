"""T2(c) — les oracles « 13/13 » et « 5/5 » etablissent-ils quelque chose du code du depot ?
(1) lecture statique : modules importes par les deux fichiers (arbre syntaxique) ; noms du depot cites ;
(2) epreuve : les deux fichiers sont joues dans un interpreteur ou tout import de `controle_ia` leve une erreur, sans le
    depot sur le chemin ; s'ils passent, ils ne lisent aucune fonction du depot ;
(3) casse de la vraie fonction : une copie de `src/` ou `environnements/propositions.appliquer` refuse toute action, ou
    `sondes/evaluation.aire_sous_courbe` rend 1 - aire, ou `prereg.problemes` rend toujours [], est mise en tete du
    chemin ; les oracles le voient-ils ?
(4) l'exemple « valide » de l'oracle 13/13 est-il valide pour le vrai `lire_action` ?"""
import ast, hashlib, json, os, pathlib, shutil, subprocess, sys, tempfile

depot = pathlib.Path(sys.argv[1])
F = {"13/13": depot / "tests/test_oracles_r5_cloture_etages_1_2.py", "5/5": depot / "tests/test_contre_epreuve_v4_r5.py"}
res = {}
py = sys.executable
env0 = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
env0.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
bloqueur = ("import sys, importlib.abc\n"
            "class B(importlib.abc.MetaPathFinder):\n"
            "    def find_spec(self, name, path, target=None):\n"
            "        if name == 'controle_ia' or name.startswith('controle_ia.'):\n"
            "            raise ImportError('import du depot interdit par l epreuve T2(c)')\n"
            "sys.meta_path.insert(0, B())\n"
            "import runpy; runpy.run_path(sys.argv[1], run_name='__main__')\n")
tmp = pathlib.Path(tempfile.mkdtemp(prefix="t2c-"))
for nom, f in F.items():
    src = f.read_text(encoding="utf-8")
    arbre = ast.parse(src)
    mods = sorted({(n.module or "") if isinstance(n, ast.ImportFrom) else a.name for n in ast.walk(arbre)
                   if isinstance(n, (ast.Import, ast.ImportFrom)) for a in n.names})
    r = {"sha256": hashlib.sha256(f.read_bytes()).hexdigest(), "modules_importes": mods,
         "occurrences_de_controle_ia": src.count("controle_ia"), "occurrences_de_propositions_py": src.count("propositions.py"),
         "default_rng_a_graine_entiere": src.count("default_rng(") - src.count("default_rng(np.random.SeedSequence")}
    copie = tmp / f.name; shutil.copy(f, copie)
    p = subprocess.run([py, "-I", "-c", bloqueur, str(copie)], capture_output=True, text=True, env=env0, cwd=tmp, timeout=900)
    r["joue_sans_le_depot_import_bloque"] = {"code": p.returncode, "derniere_ligne": (p.stdout.strip().splitlines() or [""])[-1],
                                             "erreur": p.stderr.strip()[-300:]}
    res[nom] = r
# (3) copies cassees du depot
casse = tmp / "src-casse"; shutil.copytree(depot / "src", casse)
p1 = casse / "controle_ia/environnements/propositions.py"
t = p1.read_text(encoding="utf-8")
t = t.replace('    a = lire_action(texte)\n    if a.valide and a.operation == "ADD"', '    a = lire_action(texte)\n    a.valide, a.motif = False, "casse"\n    if a.valide and a.operation == "ADD"')
assert "casse" in t; p1.write_text(t, encoding="utf-8")
p2 = casse / "controle_ia/sondes/evaluation.py"
t = p2.read_text(encoding="utf-8")
t = t.replace("return float((r[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))", "return 1.0 - float((r[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))")
assert "return 1.0 - float" in t; p2.write_text(t, encoding="utf-8")
p3 = casse / "controle_ia/prereg.py"
t = p3.read_text(encoding="utf-8")
t = t.replace("    texte = Path(chemin).read_text(encoding=\"utf-8\")\n    s = sections(texte)", "    return []\n    texte = Path(chemin).read_text(encoding=\"utf-8\")\n    s = sections(texte)")
assert "    return []\n    texte" in t; p3.write_text(t, encoding="utf-8")
env1 = dict(env0, PYTHONPATH=str(casse))
verif = subprocess.run([py, "-c", "from controle_ia.environnements.propositions import Etat, appliquer;"
                        "from controle_ia.sondes.evaluation import aire_sous_courbe; import numpy as np;"
                        "print(appliquer(Etat(),0,0,'ACTION: ADD\\nTITLE: a\\nPROPOSAL: b').valide, aire_sous_courbe(np.array([0.,1.]), np.array([0,1])))"],
                       capture_output=True, text=True, env=env1, cwd=tmp)
res["copie_cassee"] = {"appliquer_valide_et_aire_d_un_cas_parfait": verif.stdout.strip(), "attendu_sur_le_vrai_code": "True 1.0"}
for nom, f in F.items():
    p = subprocess.run([py, str(tmp / f.name)], capture_output=True, text=True, env=env1, cwd=tmp, timeout=900)
    res[nom]["joue_contre_la_copie_cassee"] = {"code": p.returncode, "derniere_ligne": (p.stdout.strip().splitlines() or [""])[-1],
                                               "la_casse_est_vue": p.returncode != 0}
# (4) l'exemple « valide » de l'oracle 13/13 devant le vrai lire_action
sys.path.insert(0, str(depot / "src"))
from controle_ia.environnements.propositions import lire_action
ex = "ACTION: ADD\nClean experimental plan.\nCOST: 250 GPU-hours"
a = lire_action(ex)
res["exemple_valide_de_l_oracle_13_13"] = {"texte": ex, "valide_pour_le_vrai_lire_action": bool(a.valide), "motif": a.motif}
res["verdict"] = "FAUX : aucun des deux fichiers n'importe ni n'appelle une fonction du depot ; ils eprouvent des copies jouets ecrites dans le fichier d'essai"
print(json.dumps(res, ensure_ascii=False, indent=1))
