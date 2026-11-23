"""Essais (R5) de l'amorce de T0.8 (`scripts/amorce_instance_t08_v1.sh`) et du commit local de la course
(`lancement_t08.commit_local_v1`, consigne v3, § 3.5 et § 4).

Amorce, artefacts du clonage et du commit local, chacun arrêtant avant tout calcul (ni essais ni course) : fichier de sondes
glissé dans la branche d'entrée ; `resume.json` de 7b dans les objets git du code (garde du code resserrée) ; branche d'entrée
déplacée depuis les contrôles ; un fichier de plus, un fichier de moins dans la branche d'entrée. Module : cas sain (liste
exacte, parent égal au commit cité) ; un fichier de plus, de moins, sous un chemin gelé, un autre parent, une modification ;
vérification par l'exécutante après la poussée (noms seuls). Le cas sain de l'amorce est l'essai de bout en bout
(`scripts/essai_jouet_chaine_t08_v1.py`, joué deux fois). Hors de la liste figée de la machine."""
from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

from controle_ia.lancement_t08 import commit_local_v1 as CL

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("essai_chaine_t08", RACINE / "scripts" / "essai_jouet_chaine_t08_v1.py")
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)
H = "20261122-120000"


@pytest.mark.parametrize("cas", ["interdit_dans_entree", "interdit_dans_code", "entree_deplacee", "plus_dans_entree",
                                 "moins_dans_entree"])
def test_amorce_artefacts_du_clonage_et_du_commit_local(tmp_path, cas):
    d = tmp_path / "essai"
    k = {"interdit_code": cas == "interdit_dans_code", "interdit_entree": cas == "interdit_dans_entree"}
    if cas == "plus_dans_entree":
        k["plus_dans_entree"] = ("diag/factice/en-trop.json",)
    if cas == "moins_dans_entree":
        k["moins_dans_entree"] = (f"diag/{H}-t06-7b-jouet/episodes-t06.json.sha256",)
    m = E.construire(d, H, 12345, **k)
    sup = {"ENTREE_COMMIT": "0" * 40} if cas == "entree_deplacee" else {}
    r = E.jouer(d, m, "artefact", sup)
    sortie = (d / "amorce-sortie.txt").read_text(encoding="utf-8")
    assert r["code"] != 0 and not r["fin_normale"], sortie[-2000:]
    assert "refus" in (r["detruire"] or ""), sortie[-2000:]
    assert "run : " not in sortie and "suite ciblée" not in sortie, sortie[-2000:]              # ni essais ni course
    attendu = {"interdit_dans_entree": "lecture-sondes-t06.json", "plus_dans_entree": "en trop ['diag/factice/en-trop.json'",
               "moins_dans_entree": "manquants ['diag/", "entree_deplacee": "≠ commit des contrôles",
               "interdit_dans_code": f"objet git diag/{H}-t06-7b-jouet/resume.json"}[cas]
    assert attendu in sortie, sortie[-2000:]
    if cas != "interdit_dans_code":
        assert "installation" not in sortie                                                    # arrêt avant l'installation


# --- module du commit local ------------------------------------------------------------------------------------------

def _g(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], capture_output=True, text=True, check=True).stdout.strip()


@pytest.fixture
def depot(tmp_path):
    d = tmp_path / "d"
    d.mkdir()
    _g(d, "init", "-q", "-b", "code")
    for c, t in (("src/a.py", "x\n"), ("docs/sources/invites-2606.08892-v1/index.json", "{}\n"), ("prereg/P3.md", "p\n")):
        (d / c).parent.mkdir(parents=True, exist_ok=True)
        (d / c).write_text(t)
    _g(d, "add", "-A")
    _g(d, "-c", "user.email=e@invalid", "-c", "user.name=e", "commit", "-qm", "code")
    return d, _g(d, "rev-parse", "HEAD")


def _commit_local(d, fichiers):
    for c in fichiers:
        (d / c).parent.mkdir(parents=True, exist_ok=True)
        (d / c).write_text("entrée\n")
    _g(d, "add", "-A", "-f")
    _g(d, "-c", "user.email=e@invalid", "-c", "user.name=e", "commit", "-qm", "local")
    return _g(d, "rev-parse", "HEAD")


LISTE = ["diag/r/e.json", "diag/r/e.json.sha256", "prereg/T08.md", "prereg/T08.md.sha256"]


def test_commit_local_cas_sain_et_attendus(depot):
    d, c = depot
    _commit_local(d, LISTE)
    assert CL.verifier(d, c, LISTE + ["prereg/P3.md"])["ajouts"] == 4                   # un fichier suivi au commit : pas un ajout
    cfg = {"entrees": {"t": {"chemin": "donnees/t.json"}, "i": {"chemin": "docs/sources/x.txt"}}}
    a = CL.attendus(cfg, "prereg/T.md", "prereg/C.json")
    assert a == sorted(["donnees/t.json", "docs/sources/x.txt", *CL.GUIDE, "prereg/T.md", "prereg/C.json"]
                       + [x + ".sha256" for x in ["donnees/t.json", "docs/sources/x.txt", *CL.GUIDE, "prereg/T.md", "prereg/C.json"]])
    with pytest.raises(CL.Ecart, match="gelé"):
        CL.attendus({"entrees": {"t": {"chemin": "src/x.py"}}}, None, "prereg/C.json")


@pytest.mark.parametrize("cas, motif", [("plus", "en trop"), ("moins", "manquants"), ("gele", "chemin gelé"),
                                        ("parent", "un seul, le commit cité"), ("modifie", "modifiés ou retirés")])
def test_commit_local_artefacts(depot, cas, motif):
    d, c = depot
    if cas == "plus":
        _commit_local(d, LISTE + ["diag/r/autre.json"])
    elif cas == "moins":
        _commit_local(d, LISTE[:-1])
    elif cas == "gele":
        _commit_local(d, LISTE + ["src/b.py"])
    elif cas == "parent":
        _commit_local(d, ["diag/r/intermediaire.json"])
        _commit_local(d, LISTE)
    elif cas == "modifie":
        (d / "src/a.py").write_text("y\n")
        _commit_local(d, LISTE)
    with pytest.raises(CL.Ecart, match=motif):
        CL.verifier(d, c, LISTE)


def test_verification_par_l_executante_apres_la_poussee(depot):
    d, c = depot
    local = _commit_local(d, LISTE)
    _commit_local(d, ["runs/x/manifeste.json", "diag/x/course-t08.json"])          # sorties de la course après le commit local
    _g(d, "branch", "sortie", "HEAD")
    _g(d, "checkout", "-q", "--orphan", "entree")
    _g(d, "rm", "-rq", "--cached", ".")
    for x in LISTE:
        (d / x).parent.mkdir(parents=True, exist_ok=True)
        (d / x).write_text("entrée\n")
    _g(d, "add", "-f", *LISTE)
    _g(d, "-c", "user.email=e@invalid", "-c", "user.name=e", "commit", "-qm", "entrée")
    r = CL.verifier_distant(d, "sortie", c, "entree")
    assert r["commit_local"] == local and r["parent"] == c and r["ajouts"] == 4 and r["commits_apres"] == 2
    with pytest.raises(CL.Ecart):
        CL.verifier_distant(d, "entree", c, "entree")                                   # ne descend pas du commit cité
    assert CL.main(["verifier-distant", str(d), "sortie", c, "entree"]) == 0
