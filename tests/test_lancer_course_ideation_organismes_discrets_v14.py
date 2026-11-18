"""Essais de `scripts/lancer_course_ideation_organismes_discrets_v14.py` (le v12 avec la lignée Argon du v8, à l'identique, et
les témoins v6 ; tronc commun couvert par les essais du v8, du v9, du v10, du v12). Aucun modèle appelé, aucun réseau."""
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


ln, l12, l8 = charger("v14"), charger("v12"), charger("v8")
GO_LIGNE = ("| GO-2026-11-18-01 | 2026-11-18 | calcul | **Organisme d'idéation sur les organismes discrets, lignée argon : "
            "seconde course, témoins v6** | 11.3 USD | 2026-11-22 | Lazar | essai |")


def test_changements_annonces():
    assert ln.LIGNEES == ("argon",)
    assert ln.PERIMETRE_GO == ("organisme d'idéation", "organismes discrets", "lignée argon")
    assert ln.PIRE_CAS_DEVIS_USD == pytest.approx(11.3) and ln.BORNE_LIGNE_USD == pytest.approx(11.3)
    assert ln.PIECES_COMMUNES == l12.PIECES_COMMUNES
    assert ln.PIECES_COMMUNES["temoins"][1] == "07c80a23eed67acb8457deefb5ad45135c54683eddc37949a2de60426a838a42"
    assert ln.SOUS_DOSSIER_RUNS == "course-ideation-organismes-discrets-v14" and "R-3282" in ln.DECISION
    assert "argon" not in ln.DELAIS_PAR_LIGNEE


def test_lignee_identique_au_v8():
    assert ln.LIGNEES_EXTERNES == {"argon": l8.LIGNEES_EXTERNES["argon"]}
    l = ln.LIGNEES_EXTERNES["argon"]
    assert l["enveloppe"] == (f"{ln.ENVELOPPES}/appel-argon-v6.sh", "440127d646fb67d593a61bc29652d505a6ec0286de72256f9116986d8d449bbb")
    assert l["commande"][0].endswith("commande_argon_v3e.py") and l["commande"][1] == "e94ecd4693657bd2d8b086fbbc903bb77635b3b034e1eede50d630675c3f3fc6" and l["famille"] == "gemini"
    assert ln.plafonds_de("argon") == l8.plafonds_de("argon")


def test_pieces_sur_le_depot_reel():
    lues = ln.verifier_pieces(ln.Reglages.production("argon"))
    assert lues["enveloppe_externe"]["chemin"].endswith("appel-argon-v6.sh")
    assert lues["commande_externe"]["chemin"].endswith("commande_argon_v3e.py")
    assert lues["temoins"]["chemin"].endswith("temoins-organisme-discrets-v6.json")


def test_enveloppe_lance_la_commande_epinglee_sous_le_delai():
    t = (RACINE / ln.LIGNEES_EXTERNES["argon"]["enveloppe"][0]).read_text(encoding="utf-8")
    execution = t[t.index("\nexec "):]
    assert "commande_argon_v3e.py" in t and "127.0.0.1:8788" in execution and "timeout -k 20 1700" in execution
    assert 1700 + 20 < 1800                       # délai par défaut de l'orchestrateur (aucun relevé pour cette lignée)


def test_code_egal_au_v12_hors_des_lignes_annoncees():
    def corps(v):
        return (RACINE / "scripts" / f"lancer_course_ideation_organismes_discrets_{v}.py").read_text(encoding="utf-8").split('"""', 2)[2]
    diff = [l for l in difflib.unified_diff(corps("v12").splitlines(), corps("v14").splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    permis = ("VERSION", "LIGNEES = (", "PERIMETRE_GO", "temoins", "\"carbon\": {", "\"argon\": {", "\"enveloppe\": (",
              "\"9ef03f80", "\"440127d646fb67d593a61bc29652d505a6ec0286de72256f9116986d8d449bbb\"", "\"commande\": COMMANDE_GEMINI_LOT", "\"commande\": COMMANDE_",
              "PIECES = pieces_de", "PLAFONDS = plafonds_de", "DECISION", "« tu as mon go", "lot à 8 192", "3c6f9448", "avec les témoins v6 ; ligne de GO",
              "DOSSIER_SORTIES", "SOUS_DOSSIER_RUNS", "SUFFIXE_RUN", "lignee: str")
    hors = [l for l in diff if not any(p in l for p in permis)]
    assert hors == [], hors
    assert len(diff) == 2 * 10 + 8 + 7, diff    # 10 lignes simples, l'entrée de lignée (4 → 4), la décision (4 → 3)


def test_go(tmp_path):
    p = tmp_path / "go.md"
    p.write_text("| id | a | t | p | pl | e | par | r |\n|---|---|---|---|---|---|---|---|\n" + GO_LIGNE + "\n", encoding="utf-8")
    assert ln.verifier_go(p, dt.date(2026, 11, 18))["plafond_usd"] == pytest.approx(11.3)


def test_go_d_une_autre_lignee_refuse(tmp_path):
    p = tmp_path / "go.md"
    p.write_text("| id | a | t | p | pl | e | par | r |\n|---|---|---|---|---|---|---|---|\n"
                 + GO_LIGNE.replace("lignée argon", "lignée carbon") + "\n", encoding="utf-8")
    with pytest.raises(ln.Refus):
        ln.verifier_go(p, dt.date(2026, 11, 18))


def test_commande_de_course():
    r = ln.Reglages.production("argon")
    argv = ln.commande_course(r, Path("/tmp/s"), Path("/tmp/lb.json"), "H", Path("/tmp/pc"))
    assert argv[argv.index("--temoins") + 1].endswith("temoins-organisme-discrets-v6.json")
    assert "--delai-commande-s" not in argv and "--delai-session-s" not in argv
    ln.garde_drapeaux(argv)
    s = ln.garde_sommes(argv)
    assert s["somme_claude"] <= s["total_claude"] and s["somme_externe"] <= s["total_externe"]


def test_commande_fausse_refusee():
    p = subprocess.run([sys.executable, "-I", "-B", "scripts/lancer_course_ideation_organismes_discrets_v14.py", "carbon"],
                       cwd=str(RACINE), capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and "argon" in p.stdout + p.stderr
