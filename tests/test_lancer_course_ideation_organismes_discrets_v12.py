"""Essais de `scripts/lancer_course_ideation_organismes_discrets_v12.py` (le v10 avec les témoins v6, l'enveloppe Carbon par lot
et les délais relevés pour Carbon ; tronc commun couvert par les essais du v8, du v9, du v10). Aucun modèle appelé, aucun réseau."""
from __future__ import annotations

import datetime as dt
import difflib
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True


def charger(version):
    script = RACINE / "scripts" / f"lancer_course_ideation_organismes_discrets_{version}.py"
    spec = importlib.util.spec_from_file_location(f"lancer_course_ideation_organismes_discrets_{version}", script)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


l12, l10 = charger("v12"), charger("v10")
GO_LIGNE = ("| GO-2026-11-18-01 | 2026-11-18 | calcul | **Organisme d'idéation sur les organismes discrets, lignée carbon : "
            "troisième course par lot** | 11.3 USD | 2026-11-22 | Lazar | essai |")


def test_changements_annonces():
    assert l12.PIECES_COMMUNES["temoins"][0].endswith("temoins-organisme-discrets-v6.json")
    assert l12.PIECES_COMMUNES["temoins"][1] == "07c80a23eed67acb8457deefb5ad45135c54683eddc37949a2de60426a838a42"
    assert l12.LIGNEES_EXTERNES["carbon"]["enveloppe"][0].endswith("appel-carbon-v3.sh")
    assert l12.DELAIS_PAR_LIGNEE["carbon"] == ("--delai-commande-s", "3600", "--delai-session-s", "3900")
    assert l12.PERIMETRE_GO == l10.PERIMETRE_GO and l12.PIRE_CAS_DEVIS_USD == pytest.approx(11.3)
    assert l12.SOUS_DOSSIER_RUNS == "course-ideation-organismes-discrets-v12" and "R-3241" in l12.DECISION


def test_pieces_sur_le_depot_reel():
    lues = l12.verifier_pieces(l12.Reglages.production("carbon"))
    assert lues["enveloppe_externe"]["chemin"].endswith("appel-carbon-v3.sh")
    assert lues["temoins"]["chemin"].endswith("temoins-organisme-discrets-v6.json")


def test_enveloppe_par_lot_figee():
    t = (RACINE / l12.LIGNEES_EXTERNES["carbon"]["enveloppe"][0]).read_text(encoding="utf-8")
    execution = t[t.index("\nexec "):]
    assert "commande_gemini_lot_v1.py" in t and execution.index('"$@"') < execution.index("--provision-pensee-jetons 8192")
    assert "http://127.0.0.1:8792/v1beta" in execution and "--delai-s 3300" in execution and "timeout -k 5 3590" in execution
    assert 3300 + 30 + 2 * 120 < 3590 < int(l12.DELAIS_PAR_LIGNEE["carbon"][1])


def test_code_egal_au_v10_hors_des_lignes_annoncees():
    def corps(v):
        return (RACINE / "scripts" / f"lancer_course_ideation_organismes_discrets_{v}.py").read_text(encoding="utf-8").split('"""', 2)[2]
    diff = [l for l in difflib.unified_diff(corps("v10").splitlines(), corps("v12").splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    permis = ("VERSION", "temoins", "07c80a23", "1c6eef38", "enveloppe", "appel-carbon", "\"0853129", "\"9ef03f80",
              "DELAIS_PAR_LIGNEE", "\"carbon\": (", "DECISION", "lignée carbon", "« tu as mon go", "lot à 8 192",
              "3c6f9448", "budget de pensée 2 048", "DOSSIER_SORTIES", "SOUS_DOSSIER_RUNS", "SUFFIXE_RUN")
    hors = [l for l in diff if not any(p in l for p in permis)]
    assert hors == [], hors


def test_go(tmp_path):
    p = tmp_path / "go.md"
    p.write_text("| id | a | t | p | pl | e | par | r |\n|---|---|---|---|---|---|---|---|\n" + GO_LIGNE + "\n", encoding="utf-8")
    assert l12.verifier_go(p, dt.date(2026, 11, 18))["plafond_usd"] == pytest.approx(11.3)


def test_commande_de_course_carbon():
    r = l12.Reglages.production("carbon")
    argv = l12.commande_course(r, Path("/tmp/s"), Path("/tmp/lb.json"), "H", Path("/tmp/pc"))
    assert argv[argv.index("--temoins") + 1].endswith("temoins-organisme-discrets-v6.json")
    assert ("--delai-commande-s" in argv) and argv[argv.index("--delai-commande-s") + 1] == "3600"
    l12.garde_drapeaux(argv)
    s = l12.garde_sommes(argv)
    assert s["somme_claude"] <= s["total_claude"] and s["somme_externe"] <= s["total_externe"]


def test_commande_fausse_refusee():
    p = subprocess.run([sys.executable, "-I", "-B", "scripts/lancer_course_ideation_organismes_discrets_v12.py", "kimi"],
                       cwd=str(RACINE), capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and "carbon" in p.stdout + p.stderr
