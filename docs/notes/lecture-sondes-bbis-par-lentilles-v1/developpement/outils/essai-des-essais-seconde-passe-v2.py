"""Essai des essais : altère un module de la seconde passe, une altération à la fois, sur une copie isolée du paquet et des
essais, et dit si les essais nommés la voient. Usage : mut.py <bloc-notes> <fichier d'altérations .py>."""
import pathlib, shutil, subprocess, sys, os, runpy
S = pathlib.Path(sys.argv[1]); R = pathlib.Path(__file__).resolve().parents[5] if False else pathlib.Path(os.environ.get("DEPOT", "/home/user/controle-ia-travail"))
conf = runpy.run_path(sys.argv[2])
module, essais, muts = conf["MODULE"], conf["ESSAIS"], conf["ALTERATIONS"]
src = (R / "src/controle_ia/lentilles_sondes_bbis" / module).read_text()
def jouer(texte):
    d = S / "mut"; shutil.rmtree(d, ignore_errors=True)
    shutil.copytree(R / "src", d / "src", ignore=shutil.ignore_patterns("__pycache__"))
    (d / "tests").mkdir()
    for f in (R / "tests").glob("lentilles_sondes_bbis_*jouets*.py"): shutil.copy(f, d / "tests")
    for e in essais: shutil.copy(R / "tests" / e, d / "tests")
    shutil.copy(R / "pyproject.toml", d)
    os.symlink(R / "docs", d / "docs")   # copies versées lues par les essais (lecture seule)
    (d / "src/controle_ia/lentilles_sondes_bbis" / module).write_text(texte)
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "--rootdir", str(d)] + conf.get("OPTIONS", [])
                       + [str(d / "tests" / e) for e in essais], cwd=d, env={**os.environ, "PYTHONPATH": f"{d/'src'}:{d/'tests'}", "PYTHONDONTWRITEBYTECODE": "1"},
                       capture_output=True, text=True)
    return r.returncode
print("témoin sans altération :", "sain" if jouer(src) == 0 else "EN ÉCHEC")
vues = 0
for nom, a, b in muts:
    assert src.count(a) == 1, (nom, src.count(a))
    vue = jouer(src.replace(a, b)) != 0; vues += vue
    print(("VUE     " if vue else "NON VUE ") + nom)
print(f"{vues} altérations vues sur {len(muts)}")
