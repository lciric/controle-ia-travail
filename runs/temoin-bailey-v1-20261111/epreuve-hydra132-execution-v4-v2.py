"""Épreuve hors essais, v2 (R12 ; la v1 reste telle quelle) : execution_v4 et execution_v3 sous Hydra 1.3.2 (version figée
de l'instance), mini-clone synthétique et vraies configurations publiques. v2 = v1 dont l'en-tête est écrit par le script
lui-même (C-1 de la relecture du code v17) : interpréteur, versions et emplacements de Hydra et d'OmegaConf, commit du
clone public, empreinte de son dossier `configs/`, empreinte des essais v17 dont le mini-clone est tiré, et les lignes de
diagnostic du script (dossier courant, tête de `sys.path`, module local, graine, nom, argv).
Usage : <python avec hydra-core 1.3.2> -I epreuve-hydra132-execution-v4-v2.py <clone public> <dossier de travail>"""
import os, shutil, subprocess, sys, tempfile
from pathlib import Path
DEPOT = Path("/home/user/controle-ia-travail"); sys.path.insert(0, str(DEPOT / "src")); sys.path.insert(0, str(DEPOT / "tests"))
import hashlib, platform, time
import hydra, omegaconf
public = Path(sys.argv[1])
cfgs = sorted((public / "inference_time_experiments" / "configs").rglob("*"))
h = hashlib.sha256()
for f in cfgs:
    if f.is_file():
        h.update(str(f.relative_to(public)).encode() + b"\0" + f.read_bytes())
commit = subprocess.run(["git", "-C", str(public), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
essais = DEPOT / "tests/test_temoin_bailey_condition6_v17.py"
print(f"# Épreuve hors essais v2, {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
print(f"# interpréteur {sys.executable} (Python {platform.python_version()})")
print(f"# hydra-core {hydra.__version__} ({hydra.__file__}) ; omegaconf {omegaconf.__version__} ({omegaconf.__file__})")
print(f"# clone public {commit} ; configs/ (chemins et contenus) sha256 {h.hexdigest()}")
print(f"# essais v17 sha256 {hashlib.sha256(essais.read_bytes()).hexdigest()}")
from controle_ia.temoin_bailey import conventions_v3 as cv
from controle_ia.temoin_bailey.execution_v4 import configuration_attendue, surcharges
src = (DEPOT / "tests/test_temoin_bailey_condition6_v17.py").read_text()
ns = {}
debut = src.index('MINI_CONFIG = '); fin = src.index('def _lancer_enfant')
ns["cv"] = cv; exec("import shutil\nfrom pathlib import Path\n" + src[debut:fin], ns)
publiques = Path(sys.argv[1]) / "inference_time_experiments" / "configs"
for nom, conf in (("synthetique", None), ("publiques", publiques)):
    t = Path(tempfile.mkdtemp(dir=sys.argv[2]))
    clone = ns["_mini_clone"](t / "clone", conf)
    over = surcharges(3, 1394228342, str(t / "modele"), str(t / "sondes"), str(t / "params"), str(t / "hydra"))
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "TESTING", "TEMOIN_BAILEY_CONFIG")}
    env["PYTHONPATH"] = str(DEPOT / "src")
    for mod in ("execution_v4", "execution_v3"):
        r = subprocess.run([sys.executable, "-m", f"controle_ia.temoin_bailey.{mod}", "--clone", str(clone), "--graine", "7", "--", *over],
                           cwd=t, env=env, capture_output=True, text=True, timeout=300)
        ok = r.stdout.startswith(configuration_attendue(clone, over))
        jl = "JOURNALISEUR controle_ia.temoin_bailey.journaliseur_v3.JournaliseurLocal" in r.stderr
        print(nom, mod, "code", r.returncode, "config_debut_exact", ok, "journaliseur_substitue", jl,
              "derniere_ligne_erreur", (r.stderr.strip().splitlines() or [""])[-1][:160])
        for ligne in r.stderr.splitlines():
            if ligne.split(" ", 1)[0] in ("DOSSIER", "CHEMIN0", "LOCAL", "GRAINES", "NOM", "ARGV0"):
                print("   ", ligne.replace(str(t), "<travail>"))
