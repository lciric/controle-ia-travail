"""Essais (cas sain et artefacts) de verifier_citations_v1.py. Lancer : python -m pytest -q docs/notes/memoire-conception-v1/epreuve-outils-v1/"""
import hashlib, importlib.util, json, os, subprocess
import pytest
ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("vc", os.path.join(ICI, "verifier_citations_v1.py"))
vc = importlib.util.module_from_spec(spec); spec.loader.exec_module(vc)


@pytest.fixture
def depot(tmp_path):
    d = tmp_path / "d"
    (d / "docs/decisions").mkdir(parents=True)
    (d / "docs/notes/quarantaine").mkdir(parents=True)
    (d / "docs/decisions/n.md").write_text("Ligne une.\nAucun score de moniteur  n'entre\ndans un signal.\n")
    (d / "docs/notes/quarantaine/x.md").write_text("secret\n")
    for c in (["init", "-q"], ["add", "-A"], ["-c", "user.email=a@b", "-c", "user.name=t", "commit", "-qm", "i"]):
        subprocess.run(["git", "-C", str(d), *c], check=True)
    commit = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    h = hashlib.sha256((d / "docs/decisions/n.md").read_bytes()).hexdigest()[:16]
    return d, commit, h


def lancer(d, commit, tmp_path, lignes):
    r = tmp_path / "r.jsonl"; r.write_text("\n".join(json.dumps(l) for l in lignes) + "\n")
    out = tmp_path / "rapport.json"
    rc = vc.main([str(r), str(out), "--commit", commit, "--depot", str(d)])
    return rc, (json.loads(out.read_text()) if out.exists() else None)


def test_sain(depot, tmp_path):
    d, c, h = depot
    rc, rap = lancer(d, c, tmp_path, [{"id": "Q1", "citations": [{"chemin": "docs/decisions/n.md", "empreinte16": h,
              "passage": "Aucun score de moniteur n'entre dans un signal."}], "fichiers_ouverts": ["docs/decisions/n.md"]}])
    assert rc == 0 and rap["porte_2_citations"] and rap["porte_1_fichiers_ouverts"]


@pytest.mark.parametrize("cit", [{"chemin": "docs/decisions/n.md", "empreinte16": "0" * 16, "passage": "Aucun score de moniteur"},
                                 {"chemin": "docs/decisions/absent.md", "empreinte16": "0" * 16, "passage": "Aucun score de"},
                                 {"chemin": "docs/decisions/n.md", "empreinte16": None, "passage": "Aucun score de moniteur"},
                                 "pas un objet"])
def test_citation_fausse(depot, tmp_path, cit):
    d, c, h = depot
    rc, rap = lancer(d, c, tmp_path, [{"id": "Q1", "citations": [cit]}])
    assert rc == 4 and not rap["porte_2_citations"]


def test_passage_altere(depot, tmp_path):
    d, c, h = depot
    rc, rap = lancer(d, c, tmp_path, [{"id": "Q1", "citations": [{"chemin": "docs/decisions/n.md", "empreinte16": h,
              "passage": "Aucun score de juge n'entre"}]}])
    assert rc == 4


def test_citation_hors_liste(depot, tmp_path):
    d, c, h = depot
    hq = hashlib.sha256((d / "docs/notes/quarantaine/x.md").read_bytes()).hexdigest()[:16]
    rc, rap = lancer(d, c, tmp_path, [{"id": "Q1", "citations": [{"chemin": "docs/notes/quarantaine/x.md", "empreinte16": hq,
              "passage": "secret secret"}]}])
    assert rc == 4


@pytest.mark.parametrize("chemin", ["docs/notes/quarantaine/x.md", "docs/notes/note-verite-terrain-v1/a.md", "diag/r.json",
                                    "prereg/p.md", "docs/notes/demandes-fable-api-2026-11-22-v1/reponse-24-SEQUESTRE-v1.md",
                                    "../etc/passwd", "/etc/passwd", "docs/notes/inconnu/a.md",
                                    "docs/notes/memoire-conception-v1/epreuve-banque-ne-pas-lire-bibliothecaire-v1/jeu-epreuve-v2.jsonl",
                                    "docs/notes/lecture-sondes-bbis-par-lentilles-v1/u.md", "./docs/notes/../notes/quarantaine/x.md"])
def test_fichier_ouvert_exclu(depot, tmp_path, chemin):
    d, c, h = depot
    rc, rap = lancer(d, c, tmp_path, [{"id": "Q1", "citations": [], "fichiers_ouverts": [chemin]}])
    assert rc == 4 and not rap["porte_1_fichiers_ouverts"]


@pytest.mark.parametrize("chemin", ["registres/go.md", "docs/decisions/decision-N-053-v1.md", "CLAUDE.md",
                                    "docs/notes/demandes-fable-api-2026-11-22-v1/reponse-25/relecture-fable-api.md",
                                    "docs/notes/memoire-conception-v1/memo-conception-21-22-novembre-v2.md"])
def test_fichier_ouvert_autorise(chemin):
    assert vc.chemin_autorise(chemin)[0]


def test_commit_inconnu(depot, tmp_path):
    d, c, h = depot
    rc, rap = lancer(d, "f" * 40, tmp_path, [{"id": "Q1"}])
    assert rc == 1 and rap is None
