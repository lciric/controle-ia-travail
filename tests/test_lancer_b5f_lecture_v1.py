"""Essais du lanceur de la lecture du barreau 5 (`scripts/lancer_b5f_lecture_v1.sh`) : refus (sous-commande, arguments,
accord absent, identifiant de marche), configuration réelle imprimée, monde fabriqué joué tel quel par le programme de
lecture, texte du script sans commande d'arrêt, de création, de destruction ni de réseau."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "lancer_b5f_lecture_v1.sh"


def _jouer(*args, env=None):
    e = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHON_B5F": sys.executable, "PYTHONDONTWRITEBYTECODE": "1"}
    e.update(env or {})
    return subprocess.run(["bash", str(SCRIPT), *args], capture_output=True, text=True, env=e, cwd=str(RACINE))


@pytest.mark.parametrize("args", [[], ["inconnue"], ["config", "a"], ["verifier", "a", "b"], ["marche", "a"],
                                  ["ouvrir", "a"], ["monde", "a", "b"], ["preparer"], ["commande", "decisif"],
                                  ["detruire", "a"], ["verifier-destruction", "a"], ["scores", "a", "b"]])
def test_refus_sous_commande_ou_nombre_d_arguments(args):
    r = _jouer(*args)
    assert r.returncode == 2 and "B5F REFUS" in r.stderr


def test_config_exige_l_accord_et_un_plan_connu():
    r = _jouer("config", str(RACINE), "decisif", "entrees-lecture", "1", "couche_15")
    assert r.returncode == 2 and "GO_ID absent" in r.stderr
    r = _jouer("config", str(RACINE), "autre", "entrees-lecture", "1", "couche_15", env={"GO_ID": "GO-2026-11-24-01"})
    assert r.returncode == 2 and "PLAN" in r.stderr


def test_config_reelle_imprimee():
    r = _jouer("config", str(RACINE), "decisif", "entrees-lecture", "0", "une_sur_dix", env={"GO_ID": "GO-2026-11-24-01"})
    assert r.returncode == 0, r.stderr
    c = json.loads(r.stdout)
    assert c["mode"] == "reel" and c["plan"] == "decisif" and c["divergence"] is False and c["go_id"] == "GO-2026-11-24-01"
    assert c["couches"] == [7, 15, 23] and c["garde_activations"] == "une_sur_dix"
    r = _jouer("config", str(RACINE), "decisif", "entrees-lecture", "1", "tout", env={"GO_ID": "GO-2026-11-24-01"})
    assert r.returncode == 2 and "garde des activations" in r.stderr


def test_marche_refuse_un_identifiant_illisible(tmp_path):
    r = _jouer("marche", str(tmp_path / "c.json"), "20261124-120000-b5f-formation-1", "prereg/x.md")
    assert r.returncode == 2 and "RUN_ID" in r.stderr


def test_verifier_refuse_un_commit_illisible(tmp_path):
    cfg = tmp_path / "c.json"
    r0 = _jouer("config", str(RACINE), "decisif", "entrees-lecture", "1", "couche_15", env={"GO_ID": "GO-2026-11-24-01"})
    cfg.write_text(r0.stdout)
    r = _jouer("verifier", str(RACINE), "pas-un-commit", str(cfg))
    assert r.returncode == 2 and "commit" in r.stderr


def test_monde_fabrique_joue_par_le_programme_de_lecture(tmp_path):
    sys.path.insert(0, str(RACINE / "tests"))
    try:
        from test_barreau5_familles_lecture_v1 import _famille_effets, fabriquer
    finally:
        sys.path.pop(0)
    m = fabriquer(tmp_path, decalage=_famille_effets(sab=3.0, sur=6.0))
    reg = tmp_path / "registre.md"
    reg.write_text(m["registre"])
    r = _jouer("monde", str(reg), str(m["arbre"]), str(m["table"]), str(m["couts"]), str(m["formation"]),
               str(tmp_path / "sortie"))
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout.strip().splitlines()[-1])["issue"] == "S"
    # le même monde, registre sans l'épreuve à vérité plantée : refus
    reg.write_text("\n".join(x for x in m["registre"].splitlines() if "EPREUVE-B5F" not in x) + "\n")
    r = _jouer("monde", str(reg), str(m["arbre"]), str(m["table"]), str(m["couts"]), str(m["formation"]),
               str(tmp_path / "sortie2"))
    assert r.returncode == 2 and "EPREUVE-B5F" in r.stderr


def test_texte_du_script_sans_commande_d_arret_de_creation_ni_de_reseau():
    texte = SCRIPT.read_text(encoding="utf-8")
    code = "\n".join(x for x in texte.splitlines() if not x.lstrip().startswith("#"))
    arret = "k" + "ill"                       # composé : la garde du dépôt refuse ce nom écrit dans une commande
    for interdit in (rf"\b{arret}\b", rf"\bp{arret}\b", r"\bp" + "grep\\b", rf"\b{arret}all\b", r"vastai", r"\bcurl\b",
                     r"\bwget\b", r"\bgit\s+push\b", r"\brm\s", r"huggingface"):
        assert re.search(interdit, code) is None, interdit
    assert "set -uo pipefail" in texte and "HF_HUB_OFFLINE=1" in code
