"""Outils communs des essais de l'organisme retenu (v5) : étalonnage numérique jouet écrit et scellé, fichier d'entrées ;
environnements simulés des essais (correctif 0011) : poste sans carte ni accord, interpréteur du système sans numpy."""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np

from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib.jouet_v5 import etalonnage_numerique, ligne_numerique
from controle_ia.scellement import sceller

ENTREES = {"schema": cf.SCHEMA_ENTREES, "plafond_usd": 60, "depense_passee_usd": 5, "cout_fixe_usd": 10, "prix_horaire_usd": 1.3,
           "oracles_par_tour": 1, "actions_oracle_hors_tours": 3830,
           "plafond_de_tours": {"forme": "formule", "formule": cf.FORMULE_PLAFOND_DE_TOURS}}
DUREES = {"episode_genere_h": 0.004, "action_oracle_h": 0.0005}


def etalonnage(graine: int = 1, **kw) -> dict:
    e = etalonnage_numerique(np.random.default_rng(graine), **kw)
    return {"schema": cf.SCHEMA_ETALONNAGE, "lignes": e["lignes"], "taches": e["taches"], "durees": dict(DUREES), "depense_etalonnage_usd": 3.0}


def ecrire_scelle(chemin: Path, contenu) -> str:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(contenu, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return sceller(chemin)


def episode(oracle: str, exces: list, phase: str = "maitre", nom: str = "e0", sans_ancre: bool = False) -> list[dict]:
    """Dix sorties de l'oracle dont les actions 2 à 10 ont les excès donnés (None : action non bornable)."""
    lignes = [ligne_numerique(oracle, phase, nom, 0, 100.0, [100.0] * 8, sans_ancre, None, None)]
    for t, e in enumerate(exces, start=1):
        if e is None:
            lignes.append(ligne_numerique(oracle, phase, nom, t, None, [100.0] * 8, sans_ancre, 100.0, 100.0))
        else:
            l = ligne_numerique(oracle, phase, nom, t, 100.0, [100.0] * 8, sans_ancre, 100.0, 100.0)
            l["exces"] = float(e)                      # excès imposé à la valeur exacte voulue (bornes incluses)
            lignes.append(l)
    return lignes


# ---- correctif 0011 : l'environnement que simule un essai est écrit par l'essai, jamais hérité de la machine qui le joue ----
def environnement_sans_carte(dossier: Path, base: dict) -> dict:
    """Environnement d'un sous-processus qui simule un poste sans carte ni accord, où le mode jouet est permis : `base` sans
    `IIB_GO_ID` (l'accord que le lanceur de session pose sur la machine) ; chemin réduit à un dossier neuf qui ne porte que
    `git` (le manifeste du run lit le commit), donc sans `nvidia-smi` ; `CUDA_VISIBLE_DEVICES` vide, pour que torch, s'il est
    installé, ne voie aucune carte (contrat de CUDA). Sur la machine louée (accord posé, `nvidia-smi` dans `/usr/bin`, torch
    qui voit la carte), le seul chemin `/usr/bin:/bin` ne masquait rien : la garde « mode jouet sur une machine payante » a
    joué dans l'essai lui-même (première tentative de l'étalonnage, 21 novembre). La garde, elle, ne change pas."""
    git = shutil.which("git", path=base.get("PATH"))
    if git is None:
        raise RuntimeError("git introuvable dans le chemin de l'environnement de base : poste sans carte non constructible")
    outils = Path(dossier) / "chemin-du-poste-sans-carte"
    outils.mkdir(parents=True)
    os.symlink(git, outils / "git")
    env = {k: v for k, v in base.items() if k != "IIB_GO_ID"}
    env.update({"PATH": str(outils), "CUDA_VISIBLE_DEVICES": ""})
    return env


def python_sans_numpy(dossier: Path) -> Path:
    """Dossier `bin` d'un environnement virtuel vide (aucun paquet tiers) : son `python3` est celui du système de la machine
    louée, sans numpy, que la surveillance du lanceur de session appelle par `python3 -I -B`. Vérifié avant emploi (R5) : un
    `python3` qui verrait numpy ne simulerait pas la machine, et l'essai s'arrête."""
    v = Path(dossier) / "environnement-vide"
    v.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, "-m", "venv", "--without-pip", str(v)], check=True, capture_output=True, timeout=120)
    r = subprocess.run([str(v / "bin" / "python3"), "-I", "-B", "-c", "import numpy"], capture_output=True, text=True, timeout=60)
    if r.returncode == 0 or "No module named 'numpy'" not in r.stderr:
        raise RuntimeError(f"l'environnement virtuel vide voit numpy (code {r.returncode}) : interpréteur sans numpy non simulé")
    return v / "bin"
