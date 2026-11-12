"""Épreuve hors essais : execution_v4 et execution_v3 sous Hydra 1.3.2 (version figée de l'instance), configs publiques."""
import os, shutil, subprocess, sys, tempfile
from pathlib import Path
DEPOT = Path("/home/user/controle-ia-travail"); sys.path.insert(0, str(DEPOT / "src")); sys.path.insert(0, str(DEPOT / "tests"))
import hydra; print("hydra", hydra.__version__)
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
