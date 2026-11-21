"""Épreuve par mutation des gardes du distillateur (v5) : chaque garde est neutralisée tour à tour dans une COPIE du code
(l'arbre n'est pas touché), et les essais du distillateur doivent alors échouer. Usage : python ce_fichier ARBRE COPIE."""
import shutil
import subprocess
import sys
from pathlib import Path

arbre, copie = Path(sys.argv[1]), Path(sys.argv[2])
if copie.exists():
    raise SystemExit(f"{copie} existe déjà : rien n'est écrasé")
for d in ("src", "tests"):
    shutil.copytree(arbre / d, copie / d, ignore=shutil.ignore_patterns("__pycache__"))
shutil.copy(arbre / "pyproject.toml", copie / "pyproject.toml")
(copie / "scripts").mkdir()
shutil.copy(arbre / "scripts/lancer_iib_v2.sh", copie / "scripts/lancer_iib_v2.sh")
F = copie / "src/controle_ia/iib/distillation_v5.py"
source = F.read_text(encoding="utf-8")
MUTATIONS = {
    "premier coût du témoin gardé": ("if a_temoin[0] != a_maitre[0]:", "if False:"),
    "témoin différent du maître": ("if differentes == 0:", "if False:"),
    "épisode accepté par la règle": ('if not accepter(lignes, regle, oracle)["accepte"]:', "if False and accepter(lignes, regle, oracle):"),
    "nombre d'épisodes borné": ("if n < mini or n > maxi:", "if False:"),
    "marqueurs de consigne": ("if marqueurs:\n                jm.exiger", "if False:\n                jm.exiger"),
    "non bornable à coût exclue": ("non_bornable = k >= 1 and a_cout_non_bornable", "non_bornable = False"),
    "mention exclue": ("if not vus and not non_bornable and not premiere:", "if not non_bornable and not premiere:"),
    "lecture de la première action": ('premiere = k == 0 and premiere_action == "exclue" and bool(o["champ_cout"])', "premiere = False"),
    "empreinte de la base": ("if mo.empreinte_base() != base_avant:", "if False:"),
    "perte finie": ('any(not math.isfinite(float(j["perte"])) for j in journal)', "False"),
    "identité à dose 0": ("if not mo.logits_egaux(mo.logits_de_controle(ids_controle), logits_base):", "if False:"),
    "artefact à dose 1": ("if mo.logits_egaux(l1, logits_base):", "if False:"),
    "adaptateur rechargé": ("if mo.empreinte_adaptateurs() != self.empreintes[nom]:", "if False:"),
    "dose relue": ('if dose is None or float(dose) != at["dose"]:', "if False:"),
    "empreinte relue": ('if avec_empreinte and self.moteur.empreinte_adaptateurs() != at["empreinte"]:', "if False:"),
    "moteur jouet en mode réel": ('if course["mode"] == "reel" and not getattr(self.moteur, "reel", False):', "if False:"),
    "tâches d'évaluation": ('if len(list(monde.taches_evaluation)) != int(section["evaluation"]["taches"]):', "if False:"),
    "second passage": ('if self.distille or (self.dossier / NOMS["distillation"]).exists():', "if False:"),
    "ordre des conditions à la clôture": ("if ordre != attendu:", "if False:"),
    "aucune condition avant la distillation": ("if not self.distille:\n            raise GardeArret(\"aucune condition", "if False:\n            raise GardeArret(\"aucune condition"),
    "sortie sans texte": ('raise GardeArret("sortie de la distillation', 'pass; ("sortie de la distillation'),
}
echecs = 0
for nom, (ancien, neuf) in MUTATIONS.items():
    if source.count(ancien) != 1:
        raise SystemExit(f"{nom} : motif présent {source.count(ancien)} fois")
    F.write_text(source.replace(ancien, neuf), encoding="utf-8")
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests/test_iib_distillation_v5.py"], cwd=copie,
                       capture_output=True, text=True)
    derniere = r.stdout.strip().splitlines()[-1]
    vue = " failed" in derniere
    echecs += int(not vue)
    print(f"{'VUE     ' if vue else 'NON VUE '} {nom:42s} {derniere}")
F.write_text(source, encoding="utf-8")
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests/test_iib_distillation_v5.py"], cwd=copie, capture_output=True, text=True)
print("code intact :", r.stdout.strip().splitlines()[-1])
print(f"{len(MUTATIONS) - echecs} mutations vues sur {len(MUTATIONS)}")
sys.exit(1 if echecs else 0)
