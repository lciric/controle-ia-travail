"""Essais de `scripts/lancer_course_ideation_organismes_discrets_v9.py` (lignée Kimi seule ; transformation contrôlée du v8,
dont les 233 essais couvrent le tronc commun : M1, M2, verrou, environnement, relevé, copies, arrêt). Ici : ce qui change
— lignée, pièces Kimi, périmètre et plafond de la ligne de GO, pire cas et borne 11,3, plancher de la famille « kimi »,
séries de runs séparées, verrou partagé avec le v8 — plus une égalité de code avec le v8 hors des lignes annoncées.
Aucun modèle appelé, aucun réseau."""
from __future__ import annotations

import datetime as dt
import importlib.util
import math
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


l9, l8 = charger("v9"), charger("v8")

GO_LIGNE = ("| GO-2026-11-18-01 | 2026-11-18 | calcul | **Organisme d'idéation sur les organismes discrets, lignée Kimi** "
            "(lanceur v9) | 11.3 USD | 2026-11-22 | Lazar | essai |")


def registre(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text("# GO\n\n| id | accordé | type | périmètre | plafond | échéance | par | réf |\n|---|---|---|---|---|---|---|---|\n"
                 + "\n".join(lignes) + "\n", encoding="utf-8")
    return p


def test_lignee_unique_kimi_et_constantes():
    assert l9.LIGNEES == ("kimi",) and set(l9.LIGNEES_EXTERNES) == {"kimi"}
    k = l9.LIGNEES_EXTERNES["kimi"]
    assert k["modele"] == "kimi-k3.1-pro" and k["famille"] == "kimi" and k["etiquette"] == "kimi"
    assert l9.PIRE_CAS_DEVIS_USD == l9.BORNE_LIGNE_USD == pytest.approx(11.3)
    assert l9.PLAFOND_COURSE_USD + l9.PLAFOND_RELANCE_USD == pytest.approx(11.3)
    assert l9.PERIMETRE_GO == ("organisme d'idéation", "organismes discrets", "lignée kimi")
    assert l9.VERSION == "lancer_course_ideation_organismes_discrets_v9"
    assert l9.externe_de("kimi") == (("kimi", "kimi-k3.1-pro"), ("kimi-juge", "kimi-k3.1-pro"))
    assert l9.plafonds_de("kimi") == {"proposeur_ideation|claude-opus-5-5": 2.0, "juge_ideation|claude-opus-5-5": 2.0,
                                      "proposeur_ideation|kimi-k3.1-pro": 1.5, "juge_ideation|kimi-k3.1-pro": 2.5}


def test_series_separees_verrou_partage():
    assert l9.SOUS_DOSSIER_RUNS != l8.SOUS_DOSSIER_RUNS and l9.SUFFIXE_RUN != l8.SUFFIXE_RUN
    assert l9.DOSSIER_SORTIES != l8.DOSSIER_SORTIES
    assert l9.NOM_VERROU == l8.NOM_VERROU  # une seule course à la fois, deux lanceurs confondus


def test_pieces_kimi_sur_le_depot_reel():
    lues = l9.verifier_pieces(l9.Reglages.production("kimi"))
    assert set(lues) == {"question", "faits", "temoins", "enveloppe_externe", "commande_externe"}
    assert lues["enveloppe_externe"]["chemin"].endswith("appel-kimi-v1.sh")
    assert lues["commande_externe"]["chemin"].endswith("commande_kimi_ideation_v1.py")
    for n in ("question", "faits", "temoins"):  # mêmes pièces communes que les courses du v8
        assert l9.PIECES_COMMUNES[n] == l8.PIECES_COMMUNES[n]


def test_plancher_kimi():
    c = 11_085
    attendu = (math.ceil(c * 1.15) + 1024) * 2e-6 + 4096 * 10e-6
    assert l9.plancher_kimi(c) == pytest.approx(attendu)
    assert l9.plancher_externe("kimi", c)["plancher_garde_a_3_caracteres_par_jeton"] == pytest.approx(round(attendu, 6))
    with pytest.raises(l9.Refus):
        l9.plancher_externe("inconnue", c)


def test_go_sain(tmp_path):
    g = l9.verifier_go(registre(tmp_path, GO_LIGNE), dt.date(2026, 11, 18))
    assert g["id"] == "GO-2026-11-18-01" and g["plafond_usd"] == pytest.approx(11.3)


@pytest.mark.parametrize("ligne,motif", [
    (GO_LIGNE.replace("lignée Kimi", "Kimi"), "0 ligne"),
    (GO_LIGNE.replace("organismes discrets", "organismes"), "0 ligne"),
    (GO_LIGNE.replace("| 11.3 USD |", "| 11.2 USD |"), "sous le pire cas"),
    (GO_LIGNE.replace("| Lazar |", "| Claude |"), "Lazar exigé"),
    (GO_LIGNE.replace("| 2026-11-22 |", "| 2026-11-17 |"), "période"),
])
def test_go_artefacts(tmp_path, ligne, motif):
    with pytest.raises(l9.Refus, match=motif):
        l9.verifier_go(registre(tmp_path, ligne), dt.date(2026, 11, 18))


def test_la_ligne_des_trois_lignees_ne_vaut_pas_pour_kimi(tmp_path):
    trois = GO_LIGNE.replace("lignée Kimi", "trois lignées").replace("| 11.3 USD |", "| 34 USD |")
    with pytest.raises(l9.Refus, match="0 ligne"):
        l9.verifier_go(registre(tmp_path, trois), dt.date(2026, 11, 18))
    assert l8.verifier_go(registre(tmp_path, trois), dt.date(2026, 11, 18))["plafond_usd"] == 34.0
    with pytest.raises(l8.Refus, match="0 ligne"):  # et la ligne de Kimi ne vaut pas pour le v8
        l8.verifier_go(registre(tmp_path, GO_LIGNE), dt.date(2026, 11, 18))


def test_cumul_et_relance_bornes_a_11_3():
    def illisible(nom):
        return {"nom": nom, "lignee": "kimi", "lance": True, "fin": None}
    assert l9.garde_cumul([], 11.3)["borne_usd"] == pytest.approx(11.3)
    with pytest.raises(l9.Refus, match="garde de cumul"):
        l9.garde_cumul([illisible("a")], 11.3)  # 9,2 + 9,2 > 11,3
    with pytest.raises(l9.Refus, match="garde de cumul"):
        l9.garde_cumul([], 9.1)  # une ligne sous le plafond d'une course


def test_commande_de_course_kimi():
    r = l9.Reglages.production("kimi")
    argv = l9.commande_course(r, Path("/tmp/s"), Path("/tmp/lb.json"), "H", Path("/tmp/pc"))
    paires = [(a, argv[i + 1]) for i, a in enumerate(argv) if a.startswith("--") and i + 1 < len(argv)]
    assert ("--proposeur-externe", "kimi=kimi-k3.1-pro") in paires and ("--juge-externe", "kimi-juge=kimi-k3.1-pro") in paires
    assert ("--modele-commande-externe", "kimi-k3.1-pro") in paires and "--commande-externe-lit-modele" in argv
    assert any(v.endswith("appel-kimi-v1.sh") for a, v in paires if a == "--commande-externe")
    assert "--seconde-passe" not in argv
    l9.garde_drapeaux(argv)
    s = l9.garde_sommes(argv)
    assert s["somme_claude"] <= s["total_claude"] and s["somme_externe"] <= s["total_externe"]


def test_code_egal_au_v8_hors_des_lignes_annoncees():
    """Le corps (après l'en-tête) du v9 ne diffère du v8 que par des lignes qui nomment la version, Kimi, les bornes,
    les séries, la famille « kimi » ou les lignées externes (bloc remplacé)."""
    def corps(v):
        t = (RACINE / "scripts" / f"lancer_course_ideation_organismes_discrets_{v}.py").read_text(encoding="utf-8")
        return t.split('"""', 2)[2]
    import difflib
    diff = [l for l in difflib.unified_diff(corps("v8").splitlines(), corps("v9").splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    permis = ("v9", "v8", "kimi", "KIMI", "Kimi", "11.3", "11,3", "34.0", "34 USD", "lignée kimi", "trois lignées",
              "carbon", "astra", "argon", "LIGNEES", "COMMANDE_", "enveloppe", "PIECES =", "PLAFONDS =", "famille", "}",
              "f0f15108", "aa2df474", "440127d6", "6f006d03", "5f6c0f27", "PIRE_CAS", "BORNE", "plancher", "octets",
              "return octets", '"""', "consigne de `caracteres`", "lignee: str", "PORT_RELAIS_CLAUDE", "raise Refus",
              "                             \"", "                            \"", "                           \"",
              "               \"enveloppe\"", "              \"enveloppe\"", "              \"commande\"",
              "               \"commande\"", "             \"commande\"")
    hors = [l for l in diff if l[1:].strip() and not any(p in l for p in permis)]
    assert hors == [], hors


def test_commande_fausse_refusee_avant_toute_ecriture(tmp_path):
    p = subprocess.run([sys.executable, "-B", str(RACINE / "scripts" / "lancer_course_ideation_organismes_discrets_v9.py"),
                        "kimi"], cwd=str(RACINE), capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and "refus" in p.stdout + p.stderr and "-I -B" in p.stdout + p.stderr
    p2 = subprocess.run([sys.executable, "-I", "-B", "scripts/lancer_course_ideation_organismes_discrets_v9.py", "carbon"],
                        cwd=str(RACINE), capture_output=True, text=True, timeout=60)
    assert p2.returncode == 2 and "kimi" in p2.stdout + p2.stderr
