"""Essais de la porte de périmètre v1 : cas sain et artefacts (R5).
Lancer : python -m pytest -q docs/notes/memoire-conception-v1/fusion-outils-v1/test_porte_perimetre_v1.py
"""
import importlib.util
import json
import os
import subprocess

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location("pp", os.path.join(ICI, "porte_perimetre_v1.py"))
pp = importlib.util.module_from_spec(_s)
_s.loader.exec_module(pp)
_s = importlib.util.spec_from_file_location("rb", os.path.join(ICI, "recherche_bornee_v5.py"))
rb = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rb)


@pytest.fixture
def depot(tmp_path):
    d = tmp_path / "d"
    (d / "registres" / "veille-de-cap").mkdir(parents=True)
    (d / "registres" / "decisions.md").write_text("ligne\n")
    (d / "registres" / "veille-de-cap" / "journal.jsonl").write_text("{}\n")
    (d / "docs" / "notes" / "a").mkdir(parents=True)
    (d / "docs" / "notes" / "a" / "n.md").write_text("note\n")
    for args in (["init", "-q", "-b", "main"], ["add", "."],
                 ["-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "-m", "x"]):
        subprocess.run(["git", "-C", str(d), *args], check=True)
    sha = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    return str(d), sha


def l(agent, bras, chemin, commit, action="lire"):
    return json.dumps({"agent": agent, "action": action, "chemin": chemin, "commit": commit, "bras": bras})


ROLES = {"biblio": "memo", "cycle": "boucle"}


def test_cas_sain_par_l_outil(depot, tmp_path):
    d, sha = depot
    j = str(tmp_path / "j.jsonl")
    base = ["--commit", sha, "--journal", j, "--depot", d]
    assert rb.main(["lire", "registres/decisions.md", "--bras", "memo", "--agent", "biblio", *base]) == 0
    assert rb.main(["lire", "registres/veille-de-cap/journal.jsonl", "--bras", "boucle", "--agent", "cycle", *base]) == 0
    r = pp.juger(open(j).read().split("\n"), ROLES, d)
    assert r["verdict"] == "tient" and r["lignes"] == 2


@pytest.mark.parametrize("ligne,motif", [
    (lambda s: l("biblio", "memo", "registres/veille-de-cap/journal.jsonl", s), "non ouvrable"),
    (lambda s: l("biblio", "boucle", "registres/decisions.md", s), "bras boucle au lieu de memo"),
    (lambda s: l("inconnu", "memo", "registres/decisions.md", s), "absent"),
    (lambda s: l("cycle", "boucle", "prereg/a.md", s), "non ouvrable"),
    (lambda s: l("biblio", "memo", "registres/decisions.md", "abc"), "commit mal formé"),
    (lambda s: l("biblio", "memo", "registres/decisions.md", "f" * 40), "hors de la branche principale"),
    (lambda s: l("biblio", "memo", "registres/decisions.md", s, action="ecrire"), "hors liste"),
    (lambda s: "pas du json", "illisible"),
    (lambda s: "[1, 2]", "mal formée"),
])
def test_artefacts(depot, ligne, motif):
    d, sha = depot
    r = pp.juger([ligne(sha)], ROLES, d)
    assert r["verdict"] == "tombe" and motif in r["detail"][0]["motif"], r


def test_main_codes(depot, tmp_path):
    d, sha = depot
    j = tmp_path / "j.jsonl"
    j.write_text(l("biblio", "memo", "registres/decisions.md", sha) + "\n")
    roles = tmp_path / "roles.json"
    roles.write_text(json.dumps(ROLES))
    assert pp.main([str(j), str(roles), str(tmp_path / "r1.json"), "--depot", d]) == 0
    assert pp.main([str(j), str(roles), str(tmp_path / "r1.json"), "--depot", d]) == 1
    j.write_text(l("biblio", "memo", "registres/veille-de-cap/journal.jsonl", sha) + "\n")
    assert pp.main([str(j), str(roles), str(tmp_path / "r2.json"), "--depot", d]) == 3
    roles.write_text(json.dumps({"biblio": "tout"}))
    assert pp.main([str(j), str(roles), str(tmp_path / "r3.json"), "--depot", d]) == 1
