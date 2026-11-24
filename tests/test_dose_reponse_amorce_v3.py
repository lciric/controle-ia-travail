"""Essais de l'amorce v3 de la course de dose–réponse (extraction du texte de désignation pour le critère 3 sur l'instance)
et de `dose_reponse.extraction_v1` (R5 : cas sain et artefact). Aucune donnée d'organisme, aucun texte privé : fichiers
factices dans un dépôt git temporaire."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import pytest

from controle_ia.dose_reponse import controles_v2 as ct
from controle_ia.dose_reponse import extraction_v1 as ex
from controle_ia.gardes import GardeArret

RACINE = Path(__file__).resolve().parents[1]
DESIGNATION = "prereg/G0-critere-3-designation-course-v1.md"


def _config(designation):
    return {"piece_jointe": {"chemin": "brouillons/x/pj.json", "sha256": "a" * 64},
            "consignes_premier_test": {"chemin": "prereg/P3-consignes-v1.md", "sha256": "b" * 64},
            "banque": {"chemin": "donnees/r/taches-banque.json", "sha256": "c" * 64},
            "designation_critere_3": designation, "commit_code": "d" * 40}


def test_chemins_cites_sain():
    assert ex.chemins_cites(_config(None)) == ["/brouillons/x/pj.json*", "/prereg/P3-consignes-v1.md*",
                                               "/donnees/r/taches-banque.json*"]
    d = {"chemin": DESIGNATION, "sha256": "e" * 64, "lignes_registre": ["DESIGNATION-CRITERE-3"]}
    assert ex.chemins_cites(_config(d))[-1] == "/" + DESIGNATION + "*"


@pytest.mark.parametrize("designation", [{"sha256": "e" * 64}, {"chemin": "/etc/passwd"}, {"chemin": "prereg/../../x"},
                                         {"chemin": "prereg/*.md"}, {"chemin": ""}, {"chemin": "a\nb"}, "prereg/x.md"])
def test_chemins_cites_artefacts(designation):
    with pytest.raises(ex.Refus):
        ex.chemins_cites(_config(designation))


def test_cle_de_designation_absente_refusee():
    c = _config(None)
    del c["designation_critere_3"]
    with pytest.raises(ex.Refus, match="absente"):
        ex.chemins_cites(c)


def _commande_cites(amorce: str) -> str:
    """La commande `CITES=$(…)` de l'amorce, telle quelle (jusqu'à « || refus »)."""
    texte = (RACINE / "scripts" / amorce).read_text(encoding="utf-8")
    m = re.search(r"^CITES=\$\((?P<c>.*?)\) \|\| refus", texte, re.S | re.M)
    assert m, amorce
    return m["c"]


def _depot(tmp_path: Path, designation: dict | None) -> tuple[Path, Path]:
    """Dépôt git factice (code de `src/` compris) et clone en extraction partielle, comme sur l'instance."""
    d = tmp_path / "origine"
    for f in ("brouillons/x/pj.json", "prereg/P3-consignes-v1.md", "donnees/r/taches-banque.json", DESIGNATION):
        (d / f).parent.mkdir(parents=True, exist_ok=True)
        (d / f).write_text("factice\n", encoding="utf-8")
        (d / (f + ".sha256")).write_text("0 x\n", encoding="utf-8")
    (d / "src/controle_ia/dose_reponse").mkdir(parents=True)
    for f in ("src/controle_ia/__init__.py", "src/controle_ia/dose_reponse/__init__.py",
              "src/controle_ia/dose_reponse/extraction_v1.py"):
        (d / f).write_text((RACINE / f).read_text(encoding="utf-8"), encoding="utf-8")
    (d / "config.json").write_text(json.dumps(_config(designation)), encoding="utf-8")
    run = lambda *a, cwd=d: subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True, text=True)  # noqa: E731
    run("init", "-q")
    run("add", "-A")
    run("-c", "user.name=e", "-c", "user.email=e@invalid", "commit", "-qm", "factice")
    c = tmp_path / "clone"
    run("clone", "-q", "--no-checkout", str(d), str(c), cwd=tmp_path)
    run("sparse-checkout", "init", "--no-cone", cwd=c)
    subprocess.run(["git", "sparse-checkout", "set", "--no-cone", "--stdin"], cwd=c, input="/src/\n/config.json*\n",
                   check=True, capture_output=True, text=True)
    run("checkout", "-q", "HEAD", cwd=c)
    return d, c


def _extraire(clone: Path, amorce: str) -> subprocess.CompletedProcess:
    script = f'CONFIG=config.json; CITES=$({_commande_cites(amorce)}) || exit 7; printf "%s\\n" "$CITES" | git sparse-checkout add --stdin'
    return subprocess.run(["bash", "-c", script], cwd=clone, capture_output=True, text=True)


def _registre(clone: Path) -> None:
    (clone / "registres").mkdir()
    (clone / "registres/scellements-v1.md").write_text(
        f"| BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE | x | y | {'c' * 64} |\n"
        f"| CODE-DOSE-REPONSE-CONSIGNE-CACHEE | x | z-{'d' * 40}-v1.json | w |\n"
        "| DESIGNATION-CRITERE-3 | x | y | z |\n", encoding="utf-8")


def test_amorce_v3_extrait_la_designation_et_la_garde_passe(tmp_path):
    from controle_ia.scellement import sceller
    sain = {"chemin": DESIGNATION, "sha256": None, "lignes_registre": ["DESIGNATION-CRITERE-3"]}
    # cas sain : configuration désignée, amorce v3
    _, c2 = _depot(tmp_path / "b", sain)
    r = _extraire(c2, "amorce_instance_dose_reponse_v3.sh")
    assert r.returncode == 0, r.stdout + r.stderr
    assert (c2 / DESIGNATION).is_file()
    (c2 / (DESIGNATION + ".sha256")).unlink()
    sain["sha256"] = sceller(c2 / DESIGNATION)
    _registre(c2)
    config = {**_config(sain)}
    assert ct.controler_registre(c2, config)["lignes"][-1] == "DESIGNATION-CRITERE-3"
    # artefact : même configuration, commande d'extraction de l'amorce v2 : le texte reste hors de l'arbre, la garde arrête
    _, c3 = _depot(tmp_path / "c", sain)
    r = _extraire(c3, "amorce_instance_dose_reponse_v2.sh")
    assert r.returncode == 0 and not (c3 / DESIGNATION).exists()
    _registre(c3)
    with pytest.raises((GardeArret, FileNotFoundError, OSError)):
        ct.controler_registre(c3, config)


def test_amorce_v3_course_sans_designation(tmp_path):
    _, c = _depot(tmp_path, None)
    r = _extraire(c, "amorce_instance_dose_reponse_v3.sh")
    assert r.returncode == 0 and (c / "donnees/r/taches-banque.json").is_file() and not (c / DESIGNATION).exists()


def test_amorce_v3_refuse_une_configuration_illisible(tmp_path):
    _, c = _depot(tmp_path, {"chemin": "/etc/passwd"})
    r = _extraire(c, "amorce_instance_dose_reponse_v3.sh")
    assert r.returncode == 7 and not (c / "brouillons/x/pj.json").exists()


def test_lanceur_v3_cite_l_amorce_v3():
    t = (RACINE / "scripts/lancer_dose_reponse_v3.sh").read_text(encoding="utf-8")
    assert "\nA=scripts/amorce_instance_dose_reponse_v3.sh\n" in t and "lancer_dose_reponse_v2.sh" not in t
