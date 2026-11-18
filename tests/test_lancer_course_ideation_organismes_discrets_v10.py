"""Essais de `scripts/lancer_course_ideation_organismes_discrets_v10.py` (troisième course Carbon ; transformation contrôlée du
v9 corrigé, dont le tronc commun est celui du v8 et de ses 233 essais). Ici : lignée, enveloppe Carbon v2 (budget de pensée
2 048, relais v3 sur 8791), périmètre « lignée carbon », borne 11,3, aucun délai relevé, décision propre, égalité de code
avec le v9 hors des lignes annoncées. Aucun modèle appelé, aucun réseau."""
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


l10, l9, l8 = charger("v10"), charger("v9"), charger("v8")
GO_LIGNE = ("| GO-2026-11-18-01 | 2026-11-18 | calcul | **Organisme d'idéation sur les organismes discrets, lignée carbon : "
            "troisième course** | 11.3 USD | 2026-11-22 | Lazar | essai |")


def registre(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text("# GO\n\n| id | accordé | type | périmètre | plafond | échéance | par | réf |\n|---|---|---|---|---|---|---|---|\n"
                 + "\n".join(lignes) + "\n", encoding="utf-8")
    return p


def test_constantes_carbon():
    assert l10.LIGNEES == ("carbon",) and set(l10.LIGNEES_EXTERNES) == {"carbon"}
    c = l10.LIGNEES_EXTERNES["carbon"]
    assert c["modele"] == "gemini-4-carbon" and c["famille"] == "gemini" and c["commande"] == l8.COMMANDE_GEMINI
    assert c["enveloppe"][0].endswith("appel-carbon-v2.sh")
    assert l10.PERIMETRE_GO == ("organisme d'idéation", "organismes discrets", "lignée carbon")
    assert l10.PIRE_CAS_DEVIS_USD == l10.BORNE_LIGNE_USD == pytest.approx(11.3)
    assert l10.SOUS_DOSSIER_RUNS not in (l8.SOUS_DOSSIER_RUNS, l9.SOUS_DOSSIER_RUNS)
    assert l10.DOSSIER_SORTIES not in (l8.DOSSIER_SORTIES, l9.DOSSIER_SORTIES)
    assert "carbon" in l10.DECISION and "2 048" in l10.DECISION and "kimi" not in l10.DECISION.lower()


def test_enveloppe_carbon_v2_budget_et_relais():
    t = (RACINE / l10.LIGNEES_EXTERNES["carbon"]["enveloppe"][0]).read_text(encoding="utf-8")
    derniere = t.strip().splitlines()[-1]
    assert "--provision-pensee-jetons 2048" in derniere and "http://127.0.0.1:8791/v1beta" in derniere
    execution = t[t.index("\nexec "):]
    assert execution.index('"$@"') < execution.index("--provision-pensee-jetons 2048")  # figé après "$@" : rien ne le change


def test_pieces_carbon_sur_le_depot_reel():
    lues = l10.verifier_pieces(l10.Reglages.production("carbon"))
    assert lues["enveloppe_externe"]["chemin"].endswith("appel-carbon-v2.sh")
    assert lues["commande_externe"]["chemin"].endswith("commande_argon_v3e.py")


def test_aucun_delai_releve_pour_carbon():
    r = l10.Reglages.production("carbon")
    argv = l10.commande_course(r, Path("/tmp/s"), Path("/tmp/lb.json"), "H", Path("/tmp/pc"))
    assert "--delai-commande-s" not in argv and "--delai-session-s" not in argv
    paires = [(a, argv[i + 1]) for i, a in enumerate(argv) if a.startswith("--") and i + 1 < len(argv)]
    assert ("--proposeur-externe", "carbon=gemini-4-carbon") in paires and "--commande-externe-lit-modele" in argv
    l10.garde_drapeaux(argv)
    s = l10.garde_sommes(argv)
    assert s["somme_claude"] <= s["total_claude"] and s["somme_externe"] <= s["total_externe"]


def test_go(tmp_path):
    assert l10.verifier_go(registre(tmp_path, GO_LIGNE), dt.date(2026, 11, 18))["plafond_usd"] == pytest.approx(11.3)
    trois = GO_LIGNE.replace("lignée carbon", "trois lignées")
    with pytest.raises(l10.Refus, match="0 ligne"):
        l10.verifier_go(registre(tmp_path, trois), dt.date(2026, 11, 18))
    kimi = GO_LIGNE.replace("lignée carbon", "lignée kimi")
    with pytest.raises(l10.Refus, match="0 ligne"):
        l10.verifier_go(registre(tmp_path, kimi), dt.date(2026, 11, 18))
    with pytest.raises(l9.Refus, match="0 ligne"):  # la ligne Carbon ne vaut pas pour Kimi
        l9.verifier_go(registre(tmp_path, GO_LIGNE), dt.date(2026, 11, 18))


def test_code_egal_au_v9_hors_des_lignes_annoncees():
    def corps(v):
        return (RACINE / "scripts" / f"lancer_course_ideation_organismes_discrets_{v}.py").read_text(encoding="utf-8").split('"""', 2)[2]
    diff = [l for l in difflib.unified_diff(corps("v9").splitlines(), corps("v10").splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    permis = ("v9", "v10", "kimi", "carbon", "LIGNEES", "PERIMETRE_GO", "PIECES =", "PLAFONDS =", "DECISION", "\"",
              "}", "lignee: str")
    hors = [l for l in diff if l[1:].strip() and not any(p in l for p in permis)]
    assert hors == [], hors


def test_commande_fausse_refusee():
    p = subprocess.run([sys.executable, "-I", "-B", "scripts/lancer_course_ideation_organismes_discrets_v10.py", "kimi"],
                       cwd=str(RACINE), capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and "carbon" in p.stdout + p.stderr
