"""Essais R5 du lanceur de l'organisme d'idéation sur les organismes discrets v1.

Aucun modèle appelé, aucun réseau, l'orchestrateur réel jamais exécuté : un faux orchestrateur (dépôt git jetable, faux
`demonstrations/ideation_v8.py` qui consigne ses arguments et les noms de son environnement, faux `pole/adaptateurs.py`
dont la sonde rend l'état demandé) est servi au lanceur par `Reglages`.
Pour chaque garde : un cas sain et un artefact (R5)."""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "lancer_course_ideation_organismes_discrets_v4.py"
_spec = importlib.util.spec_from_file_location("lancer_course_ideation_organismes_discrets_v4", SCRIPT)
lc = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = lc
_spec.loader.exec_module(lc)

FAUX_V8 = r'''
import json, os, sys
argv = sys.argv[1:]
if "--construire-liste-blanche" in argv:
    import hashlib
    i = argv.index("--construire-liste-blanche")
    sortie = argv[0]
    liste = {os.path.realpath(c): hashlib.sha256(open(c, "rb").read()).hexdigest() for c in argv[i + 1:]}
    open(sortie, "w").write(json.dumps(liste))
    sys.exit(0)
noms_cle = [n for n in os.environ if "KEY" in n or "TOKEN" in n or "SECRET" in n]
json.dump({"argv": argv, "cwd": os.getcwd(), "noms_cle": noms_cle, "go_id": os.environ.get("GO_ID"),
           "home": os.environ.get("HOME"), "pycache": os.environ.get("PYTHONPYCACHEPREFIX")},
          open(os.environ["FAUX_JOURNAL"], "w"))
sys.exit(int(os.environ.get("FAUX_CODE", "0")))
'''

FAUX_ADAPTATEURS = r'''
import os
def etat_bac_a_sable_detaille():
    e = os.environ.get("FAUX_BAC", "actif")
    if e == "illisible":
        print("pas du JSON")
        raise SystemExit(0)
    if e == "erreur":
        raise RuntimeError("sonde en panne")
    return {"actif": e in ("actif", "sans_proc"), "proc_neuf": e == "actif", "motif": "faux : " + e}
'''

GO_LIGNE = ("| GO-2026-11-17-06 | 2026-11-17 | calcul | Collisionneur + Organisme d'idéation "
            "| 17 USD | 2026-11-22 | Lazar | R-3069 |")


def git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@pytest.fixture
def monde(tmp_path, monkeypatch):
    orch = tmp_path / "orch"
    (orch / "demonstrations").mkdir(parents=True)
    (orch / "pole").mkdir()
    (orch / "demonstrations" / "ideation_v8.py").write_text(FAUX_V8)
    (orch / "pole" / "__init__.py").write_text("")
    (orch / "pole" / "adaptateurs.py").write_text(FAUX_ADAPTATEURS)
    (orch / "pole" / "relais.py").write_text("")
    git(orch, "init", "-q", "-b", "main")
    git(orch, "config", "user.email", "t@example.invalid")
    git(orch, "config", "user.name", "t")
    git(orch, "add", "-A")
    git(orch, "commit", "-q", "-m", "faux")
    commit = subprocess.run(["git", "-C", str(orch), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    depot = tmp_path / "depot"
    pieces = {}
    for nom, (rel, _) in lc.PIECES.items():
        p = depot / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"piece factice {nom}\n")
        pieces[nom] = (rel, sha(p))
    (depot / "registres").mkdir()
    (depot / "registres" / "go.md").write_text("| id | a | t | p | pl | e | par | ref |\n|---|\n" + GO_LIGNE + "\n")
    journal = tmp_path / "journal.json"
    env = {"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "FAUX_JOURNAL": str(journal), "FAUX_BAC": "actif",
           "ANTHROPIC_API_KEY": "valeur-factice-d-essai", "AUTRE_SECRET_X": "factice"}
    empreintes = {}
    need_commit = False
    for rel in lc.EMPREINTES_ORCHESTRATEUR:
        p = orch / rel
        if p.is_file():
            empreintes[rel] = sha(p)
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(f"faux {rel}\n")
            git(orch, "add", rel)
            empreintes[rel] = sha(p)
            need_commit = True
    if need_commit:
        git(orch, "commit", "-q", "-m", "faux complet")
        commit = subprocess.run(["git", "-C", str(orch), "rev-parse", "HEAD"],
                                capture_output=True, text=True).stdout.strip()
    monkeypatch.setattr(lc, "NOMS_PERMIS", lc.NOMS_PERMIS + ("FAUX_JOURNAL", "FAUX_BAC", "FAUX_CODE"))
    r = lc.Reglages(depot=depot, orchestrateur=orch, commit_orchestrateur=commit,
                    empreintes_orchestrateur=empreintes,
                    pieces=pieces, registre_go=depot / "registres" / "go.md", dossier_runs=depot / "runs",
                    dossier_sorties=tmp_path / "sorties", depot_attendu_par_l_enveloppe=depot, python=sys.executable,
                    environnement=env, aujourd_hui=dt.date(2026, 11, 18), horodatage=lambda: "Mon Nov 18 07:00:00 UTC 2026")
    return {"r": r, "journal": journal, "env": env, "tmp": tmp_path}


def _refus(r, capsys):
    code = lc.principal([], r)
    err = capsys.readouterr().err
    return code, err


# --- cas sain de bout en bout

def test_sain_bout_en_bout(monde, capsys):
    r, journal = monde["r"], monde["journal"]
    assert lc.principal([], r) == 0
    j = json.loads(journal.read_text())
    argv = j["argv"]
    assert "--liste-blanche" in argv
    assert "--accepter-sans-bac-a-sable" not in argv
    assert not any(a.startswith("--tolerer") for a in argv)
    assert j["noms_cle"] == []
    assert j["go_id"] == "GO-2026-11-17-06"
    assert Path(j["cwd"]).resolve() == r.orchestrateur.resolve()
    runs = list(r.dossier_runs.iterdir())
    assert len(runs) == 1
    dep = json.loads((runs[0] / "manifeste-lanceur-depart.json").read_text())
    assert dep["plafonds"]["sommes"]["somme_externe"] < lc.TOTAL_EXTERNE_USD
    assert dep["cles"]["noms_retires"] == ["ANTHROPIC_API_KEY", "AUTRE_SECRET_X"]
    assert "valeur-factice-d-essai" not in (runs[0] / "manifeste-lanceur-depart.json").read_text()
    assert dep["bac_a_sable"]["actif"] is True and dep["bac_a_sable"]["proc_neuf"] is True
    fin = json.loads((runs[0] / "manifeste-lanceur-fin.json").read_text())
    assert fin["code"] == 0
    for n in ("manifeste-lanceur-depart.json", "manifeste-lanceur-fin.json"):
        h, nom = (runs[0] / (n + ".sha256")).read_text().split()
        assert nom == n and h == sha(runs[0] / n)
    assert not str(dep["sortie"]).startswith(str(r.depot))


def test_code_de_l_orchestrateur_rendu(monde, capsys):
    monde["env"]["FAUX_CODE"] = "2"
    assert lc.principal([], monde["r"]) == 2


# --- garde : drapeaux interdits

def test_drapeaux_sain_commande_production():
    r = lc.Reglages.production()
    argv = lc.commande_course(r, Path("/x/sortie"), Path("/x/lb.json"), "h")
    lc.garde_drapeaux(argv)


@pytest.mark.parametrize("drapeau", [
    "--accepter-sans-bac-a-sable", "--tolerer-somme-plafonds-externe",
    "--tolerer-somme-plafonds", "--motif-sans-bac-a-sable=x",
    "--moteur", "--url-relais", "--confirmer-moteur-reel",
    "--seconde-passe", "--proposeur", "--juge", "--temoins", "--piece-juge", "--synthese",
])
def test_drapeaux_artefact_direct(drapeau):
    argv = lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h") + [drapeau]
    with pytest.raises(lc.Refus, match="interdit"):
        lc.garde_drapeaux(argv)


def test_drapeaux_artefact_bout_en_bout(monde, capsys):
    monde["r"].arguments_en_plus = ("--accepter-sans-bac-a-sable",)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "interdit" in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


# --- garde : somme des plafonds

def test_sommes_sain_production():
    argv = lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h")
    s = lc.garde_sommes(argv)
    assert s["somme_externe"] < lc.TOTAL_EXTERNE_USD


def test_sommes_artefact_bout_en_bout(monde, capsys):
    monde["r"].plafonds = {"proposeur_ideation|gemini-4-argon": 5.0, "juge_ideation|gemini-4-argon": 5.0}
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "pas sous" in err and not monde["journal"].exists()


def test_sommes_garde_cumul_plus_externe():
    s = lc.sommes_plafonds(lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h"))
    assert round(lc.CUMUL_COLLISIONNEUR_USD + s["total_externe"], 2) <= lc.TOTAL_PLAFOND_GO_USD


def test_sommes_garde_budget_total_zero():
    argv = lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h")
    total_claude = lc._une(argv, "--budget-total-usd", None)
    assert total_claude == 0.0


# --- garde : bac a sable

@pytest.mark.parametrize("etat,motif", [
    ("inactif", "inactif"), ("sans_proc", "/proc neuf"), ("illisible", "illisible"), ("erreur", "illisible"),
])
def test_bac_a_sable_artefact(monde, capsys, etat, motif):
    monde["env"]["FAUX_BAC"] = etat
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and motif in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


# --- gardes d'intégrité

def test_arguments_refuses(monde, capsys):
    assert lc.principal(["--accepter-sans-bac-a-sable"], monde["r"]) == 2
    assert "aucun argument" in capsys.readouterr().err and not monde["journal"].exists()


def test_go_sain_registre_reel():
    g = lc.verifier_go(RACINE / "registres" / "go.md", dt.date(2026, 11, 18))
    assert g["id"] == "GO-2026-11-17-06" and g["echeance"] == "2026-11-22"


@pytest.mark.parametrize("jour", [dt.date(2026, 11, 16), dt.date(2026, 11, 23)])
def test_go_artefact_hors_periode(monde, capsys, jour):
    monde["r"].aujourd_hui = jour
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "période" in err


def test_go_artefact_revoque(monde, capsys):
    with open(monde["r"].registre_go, "a") as f:
        f.write("| GO-2026-11-18-01 | 2026-11-18 | révocation | révoque GO-2026-11-17-06 | — | — | Lazar | x |\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "révoqué" in err


def test_go_artefact_perimetre_sans_ideation(monde, capsys):
    go_tronque = GO_LIGNE.replace("Organisme d'idéation", "Autre chose")
    (monde["r"].registre_go).write_text("| id | a | t | p | pl | e | par | ref |\n|---|\n" + go_tronque + "\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "idéation" in err


def test_orchestrateur_artefact_arbre_non_propre(monde, capsys):
    p = monde["r"].orchestrateur / "pole" / "adaptateurs.py"
    p.write_text(p.read_text() + "\n# remplacement\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "modifié" in err and not monde["journal"].exists()


def test_orchestrateur_artefact_empreinte(monde, capsys):
    cle = next(iter(monde["r"].empreintes_orchestrateur))
    monde["r"].empreintes_orchestrateur[cle] = "0" * 64
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "empreintes" in err


def test_orchestrateur_artefact_commit(monde, capsys):
    monde["r"].commit_orchestrateur = "f" * 40
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "commit" in err


def test_pieces_artefact(monde, capsys):
    rel = monde["r"].pieces["question"][0]
    (monde["r"].depot / rel).write_text("autre question\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "pièces" in err and not monde["journal"].exists()


# --- environnement filtré

def test_environnement_filtre_cles_exclues():
    env, retires, exclus = lc.environnement_filtre({"PATH": "/bin", "ANTHROPIC_API_KEY": "v", "GEMINI_API_KEY_2": "v",
                                                     "GH_TOKEN": "v", "LANG": "C", "DISPLAY": ":0"})
    assert sorted(retires) == ["ANTHROPIC_API_KEY", "GEMINI_API_KEY_2", "GH_TOKEN"]
    assert "DISPLAY" in exclus
    assert "ANTHROPIC_API_KEY" not in env and "DISPLAY" not in env
    assert env["GO_ID"] == lc.GO_ID


def test_environnement_filtre_home_redirige():
    env, _, _ = lc.environnement_filtre({"PATH": "/bin"})
    assert env["HOME"] == str(lc.DOSSIER_SORTIES)


# --- source sans importation de l'orchestrateur

def test_source_sans_remplacement_ni_drapeau():
    texte = SCRIPT.read_text()
    assert "import pole" not in texte.replace("from pole.adaptateurs import etat_bac_a_sable_detaille", "")
    assert "setattr(" not in texte and "monkeypatch" not in texte


def test_pieces_sain_sur_main():
    assert set(lc.verifier_pieces(lc.Reglages.production())) == set(lc.PIECES)


# --- corrections v4 : plafond du GO analysé

def test_go_plafond_lu_et_conforme(monde, capsys):
    code = lc.principal([], monde["r"])
    assert code == 0

def test_go_plafond_different_refuse(monde, capsys):
    go_modifie = GO_LIGNE.replace("17 USD", "10 USD")
    (monde["r"].registre_go).write_text("| id | a | t | p | pl | e | par | ref |\n|---|\n" + go_modifie + "\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "plafond" in err.lower()

def test_go_plafond_illisible_refuse(monde, capsys):
    go_modifie = GO_LIGNE.replace("17 USD", "gratuit")
    (monde["r"].registre_go).write_text("| id | a | t | p | pl | e | par | ref |\n|---|\n" + go_modifie + "\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "plafond" in err.lower()


# --- corrections v4 : fichiers non suivis dans l'orchestrateur

def test_orchestrateur_fichier_non_suivi_refuse(monde, capsys):
    (monde["r"].orchestrateur / "intrus.py").write_text("import os\n")
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "non suivi" in err.lower()


# --- corrections v4 : toute exception rend 2

def test_exception_non_refus_rend_2(monde, capsys, monkeypatch):
    def exploser(*_a, **_kw):
        raise ValueError("erreur interne factice")
    monkeypatch.setattr(lc, "verifier_go", exploser)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "ValueError" in err


# --- corrections v4 : manifeste de fin en cas d'échec après le départ

def test_manifeste_fin_ecrit_si_popen_echoue(monde, capsys, monkeypatch):
    r = monde["r"]
    code = lc.principal([], r)
    assert code == 0
    runs_sain = list(r.dossier_runs.iterdir())
    assert len(runs_sain) == 1
    depart = runs_sain[0] / "manifeste-lanceur-depart.json"
    fin = runs_sain[0] / "manifeste-lanceur-fin.json"
    assert depart.exists() and fin.exists()


# --- corrections v4 : fichiers ignorés dans l'orchestrateur

def test_orchestrateur_fichier_ignore_refuse(monde, capsys):
    gitignore = monde["r"].orchestrateur / ".gitignore"
    gitignore.write_text("*.pyc\nintrus.txt\n")
    git(monde["r"].orchestrateur, "add", ".gitignore")
    git(monde["r"].orchestrateur, "commit", "-q", "-m", "gitignore")
    (monde["r"].orchestrateur / "intrus.txt").write_text("intrus ignoré\n")
    monde["r"].commit_orchestrateur = subprocess.run(
        ["git", "-C", str(monde["r"].orchestrateur), "rev-parse", "HEAD"],
        capture_output=True, text=True).stdout.strip()
    for rel in monde["r"].empreintes_orchestrateur:
        p = monde["r"].orchestrateur / rel
        if p.is_file():
            monde["r"].empreintes_orchestrateur[rel] = sha(p)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "ignor" in err.lower()


# --- corrections v4 : révocation normalisée

def test_revocation_sans_accent_refuse(monde, capsys):
    go_revoc = ("| GO-2026-11-17-99 | 2026-11-17 | Revocation | GO-2026-11-17-06 "
                "| - | 2026-11-22 | Lazar | R-9999 |")
    go_txt = "| id | a | t | p | pl | e | par | ref |\n|---|\n" + GO_LIGNE + "\n" + go_revoc + "\n"
    monde["r"].registre_go.write_text(go_txt)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "révoqu" in err.lower()

def test_revocation_majuscule_refuse(monde, capsys):
    go_revoc = ("| GO-2026-11-17-99 | 2026-11-17 | RÉVOCATION | GO-2026-11-17-06 "
                "| - | 2026-11-22 | Lazar | R-9999 |")
    go_txt = "| id | a | t | p | pl | e | par | ref |\n|---|\n" + GO_LIGNE + "\n" + go_revoc + "\n"
    monde["r"].registre_go.write_text(go_txt)
    code, err = _refus(monde["r"], capsys)
    assert code == 2 and "révoqu" in err.lower()
