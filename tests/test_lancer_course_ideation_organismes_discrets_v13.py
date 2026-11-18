"""Essais de `scripts/lancer_course_ideation_organismes_discrets_v13.py` (le v12 avec la lignée Astra du v8, à l'identique, et
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


ln, l12, l8 = charger("v13"), charger("v12"), charger("v8")
GO_LIGNE = ("| GO-2026-11-18-01 | 2026-11-18 | calcul | **Organisme d'idéation sur les organismes discrets, lignée astra : "
            "seconde course, témoins v6** | 11.3 USD | 2026-11-22 | Lazar | essai |")


def test_changements_annonces():
    assert ln.LIGNEES == ("astra",)
    assert ln.PERIMETRE_GO == ("organisme d'idéation", "organismes discrets", "lignée astra")
    assert ln.PIRE_CAS_DEVIS_USD == pytest.approx(11.3) and ln.BORNE_LIGNE_USD == pytest.approx(11.3)
    assert ln.PIECES_COMMUNES == l12.PIECES_COMMUNES
    assert ln.PIECES_COMMUNES["temoins"][1] == "07c80a23eed67acb8457deefb5ad45135c54683eddc37949a2de60426a838a42"
    assert ln.SOUS_DOSSIER_RUNS == "course-ideation-organismes-discrets-v13" and "R-3282" in ln.DECISION
    assert "astra" not in ln.DELAIS_PAR_LIGNEE


def test_lignee_identique_au_v8():
    assert ln.LIGNEES_EXTERNES == {"astra": l8.LIGNEES_EXTERNES["astra"]}
    l = ln.LIGNEES_EXTERNES["astra"]
    assert l["enveloppe"] == (f"{ln.ENVELOPPES}/appel-astra-v1.sh", "aa2df474c5105ea5e4729fecf0d8c875e347ed262178177b45c956b1da9f3936")
    assert l["commande"][0].endswith("commande_astra_v1.py") and l["commande"][1] == "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71" and l["famille"] == "openai"
    assert ln.plafonds_de("astra") == l8.plafonds_de("astra")


def test_pieces_sur_le_depot_reel():
    lues = ln.verifier_pieces(ln.Reglages.production("astra"))
    assert lues["enveloppe_externe"]["chemin"].endswith("appel-astra-v1.sh")
    assert lues["commande_externe"]["chemin"].endswith("commande_astra_v1.py")
    assert lues["temoins"]["chemin"].endswith("temoins-organisme-discrets-v6.json")


def test_enveloppe_lance_la_commande_epinglee_sous_le_delai():
    t = (RACINE / ln.LIGNEES_EXTERNES["astra"]["enveloppe"][0]).read_text(encoding="utf-8")
    execution = t[t.index("\nexec "):]
    assert "commande_astra_v1.py" in t and "127.0.0.1:8790" in execution and "timeout -k 20 1700" in execution
    assert 1700 + 20 < 1800                       # délai par défaut de l'orchestrateur (aucun relevé pour cette lignée)


def test_code_egal_au_v12_hors_des_lignes_annoncees():
    def corps(v):
        return (RACINE / "scripts" / f"lancer_course_ideation_organismes_discrets_{v}.py").read_text(encoding="utf-8").split('"""', 2)[2]
    garde = ('    autres = sorted(set(re.findall(r"lignée\\s+(\\w+)", _normal(c[3]))) - {"astra"})   # v13 : contre-lecture, constat 1\n'
             '    if autres:\n'
             '        raise Refus(f"{go_id} : le périmètre nomme aussi {[\'lignée \' + a for a in autres]} ; une ligne par lignée exigée")\n')
    assert corps("v13").count(garde) == 1
    diff = [l for l in difflib.unified_diff(corps("v12").splitlines(), corps("v13").replace(garde, "").splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    permis = ("VERSION", "LIGNEES = (", "PERIMETRE_GO", "temoins", "\"carbon\": {", "\"astra\": {", "\"enveloppe\": (",
              "\"9ef03f80", "\"aa2df474c5105ea5e4729fecf0d8c875e347ed262178177b45c956b1da9f3936\"", "\"commande\": COMMANDE_GEMINI_LOT", "\"commande\": COMMANDE_",
              "PIECES = pieces_de", "PLAFONDS = plafonds_de", "DECISION", "« tu as mon go", "lot à 8 192", "3c6f9448", "avec les témoins v6 ; ligne de GO",
              "DOSSIER_SORTIES", "SOUS_DOSSIER_RUNS", "SUFFIXE_RUN", "lignee: str",
              "# v13 : COMMANDE_GEMINI_LOT", "# v12 : --delai-commande-s", "# hérité du v12, sans effet ici")
    hors = [l for l in diff if not any(p in l for p in permis)]
    assert hors == [], hors
    assert len(diff) == 2 * 11 + 8 + 7 + 1, diff  # 11 lignes simples, lignée (4 → 4), décision (4 → 3), un commentaire ajouté
    corps_n = corps("v13")                  # la garde croisée : seul ajout de code, dans verifier_go (vérifié à part)
    assert corps_n.count("contre-lecture, constat 1") == 1


def test_go(tmp_path):
    p = tmp_path / "go.md"
    p.write_text("| id | a | t | p | pl | e | par | r |\n|---|---|---|---|---|---|---|---|\n" + GO_LIGNE + "\n", encoding="utf-8")
    assert ln.verifier_go(p, dt.date(2026, 11, 18))["plafond_usd"] == pytest.approx(11.3)


def test_go_d_une_autre_lignee_refuse(tmp_path):
    p = tmp_path / "go.md"
    p.write_text("| id | a | t | p | pl | e | par | r |\n|---|---|---|---|---|---|---|---|\n"
                 + GO_LIGNE.replace("lignée astra", "lignée carbon") + "\n", encoding="utf-8")
    with pytest.raises(ln.Refus):
        ln.verifier_go(p, dt.date(2026, 11, 18))


def test_commande_de_course():
    r = ln.Reglages.production("astra")
    argv = ln.commande_course(r, Path("/tmp/s"), Path("/tmp/lb.json"), "H", Path("/tmp/pc"))
    assert argv[argv.index("--temoins") + 1].endswith("temoins-organisme-discrets-v6.json")
    assert "--delai-commande-s" not in argv and "--delai-session-s" not in argv
    ln.garde_drapeaux(argv)
    s = ln.garde_sommes(argv)
    assert s["somme_claude"] <= s["total_claude"] and s["somme_externe"] <= s["total_externe"]


def test_commande_fausse_refusee():
    p = subprocess.run([sys.executable, "-I", "-B", "scripts/lancer_course_ideation_organismes_discrets_v13.py", "carbon"],
                       cwd=str(RACINE), capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and "astra" in p.stdout + p.stderr


def test_go_qui_nomme_les_deux_lignees_refuse(tmp_path):
    p = tmp_path / "go.md"
    ligne = GO_LIGNE.replace("lignée astra :", "lignée astra et lignée argon :")
    assert "lignée argon" in ligne
    p.write_text("| id | a | t | p | pl | e | par | r |\n|---|---|---|---|---|---|---|---|\n" + ligne + "\n", encoding="utf-8")
    with pytest.raises(ln.Refus, match="une ligne par lignée"):
        ln.verifier_go(p, dt.date(2026, 11, 18))


def test_go_du_registre_reel_sans_candidate():
    with pytest.raises(ln.Refus, match="0 ligne"):
        ln.verifier_go(RACINE / "registres" / "go.md", dt.date(2026, 11, 18))


def test_gardes_de_taille_sur_la_mesure_scellee_du_v8():
    import json
    m = json.loads((RACINE / "runs/course-ideation-organismes-discrets-v8/20261118-062512-course-ideation-organismes-discrets-v8-astra/mesure-consignes.json").read_text(encoding="utf-8"))
    g = ln.gardes_de_taille(m, ln.Reglages.production("astra"))
    assert g


def test_options_externes_de_la_lignee():
    r = ln.Reglages.production("astra")
    argv = ln.commande_course(r, Path("/tmp/s"), Path("/tmp/lb.json"), "H", Path("/tmp/pc"))
    l = ln.LIGNEES_EXTERNES["astra"]
    assert argv[argv.index("--commande-externe") + 1].endswith(l["enveloppe"][0])
    assert argv[argv.index("--modele-commande-externe") + 1] == l["modele"]
    assert argv[argv.index("--proposeur-externe") + 1].endswith("=" + l["modele"])
    assert "--commande-externe-lit-modele" in argv
