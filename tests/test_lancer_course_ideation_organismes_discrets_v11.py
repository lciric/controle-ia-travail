"""Essais de `scripts/lancer_course_ideation_organismes_discrets_v11.py` (le v9 avec les témoins v6 ; tronc commun couvert par
les essais du v8 et du v9). Aucun modèle appelé, aucun réseau."""
from __future__ import annotations

import datetime as dt
import difflib
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]


def charger(version):
    script = RACINE / "scripts" / f"lancer_course_ideation_organismes_discrets_{version}.py"
    spec = importlib.util.spec_from_file_location(f"lancer_course_ideation_organismes_discrets_{version}", script)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


l11, l9 = charger("v11"), charger("v9")


def test_temoins_v6_et_reste_inchange():
    assert l11.PIECES_COMMUNES["temoins"] == ("docs/notes/organismes-discrets-v1/organisme-ideation-v1/temoins-organisme-discrets-v6.json",
                                              "07c80a23eed67acb8457deefb5ad45135c54683eddc37949a2de60426a838a42")
    for n in ("question", "faits"):
        assert l11.PIECES_COMMUNES[n] == l9.PIECES_COMMUNES[n]
    assert l11.LIGNEES_EXTERNES == l9.LIGNEES_EXTERNES and l11.PERIMETRE_GO == l9.PERIMETRE_GO
    assert l11.PIRE_CAS_DEVIS_USD == l9.PIRE_CAS_DEVIS_USD == pytest.approx(11.3)
    assert l11.DELAIS_PAR_LIGNEE == l9.DELAIS_PAR_LIGNEE and l11.NOM_VERROU == l9.NOM_VERROU
    assert l11.SOUS_DOSSIER_RUNS == "course-ideation-organismes-discrets-v11" and l11.DOSSIER_SORTIES != l9.DOSSIER_SORTIES
    assert "addendum v4" in l11.DECISION and "témoins v6" in l11.DECISION


def test_pieces_sur_le_depot_reel():
    lues = l11.verifier_pieces(l11.Reglages.production("kimi"))
    assert lues["temoins"]["chemin"].endswith("temoins-organisme-discrets-v6.json")
    assert lues["enveloppe_externe"]["chemin"].endswith("appel-kimi-v2.sh")


def test_code_egal_au_v9_hors_des_lignes_annoncees():
    def corps(v):
        t = (RACINE / "scripts" / f"lancer_course_ideation_organismes_discrets_{v}.py").read_text(encoding="utf-8")
        return t.split('"""', 2)[2]
    diff = [l for l in difflib.unified_diff(corps("v9").splitlines(), corps("v11").splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    permis = ("VERSION", "temoins", "07c80a23", "1c6eef38", "DOSSIER_SORTIES", "SOUS_DOSSIER_RUNS", "SUFFIXE_RUN",
              "lignée kimi", "trouvée par son contenu")
    assert len(diff) == 15 and all(any(p in l for p in permis) for l in diff), diff


def test_go_kimi_du_registre_de_main_reconnu(tmp_path):
    p = tmp_path / "go.md"
    r = subprocess.run(["git", "show", "origin/main:registres/go.md"], cwd=str(RACINE), capture_output=True, text=True)
    if r.returncode != 0:
        pytest.skip("origin/main absent de ce clone")
    p.write_text(r.stdout, encoding="utf-8")
    g = l11.verifier_go(p, dt.date(2026, 11, 18))
    assert g["id"] == "GO-2026-11-18-17" and g["plafond_usd"] == pytest.approx(11.3)


def test_commande_de_course_kimi():
    r = l11.Reglages.production("kimi")
    argv = l11.commande_course(r, Path("/tmp/s"), Path("/tmp/lb.json"), "H", Path("/tmp/pc"))
    assert argv[argv.index("--temoins") + 1].endswith("temoins-organisme-discrets-v6.json")
    assert ("--delai-commande-s" in argv) and "--commande-externe-lit-modele" in argv
    l11.garde_drapeaux(argv)
    s = l11.garde_sommes(argv)
    assert s["somme_claude"] <= s["total_claude"] and s["somme_externe"] <= s["total_externe"]


def test_commande_fausse_refusee():
    p = subprocess.run([sys.executable, "-I", "-B", "scripts/lancer_course_ideation_organismes_discrets_v11.py", "carbon"],
                       cwd=str(RACINE), capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and "kimi" in p.stdout + p.stderr
