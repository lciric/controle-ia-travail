"""Essais du vérificateur v4 et de l'outil de recherche autorisée v1 (cas sains et artefacts)."""
import hashlib, importlib.util, io, json, os, subprocess, contextlib
import pytest
ICI = os.path.dirname(os.path.abspath(__file__))
def charger(nom, f):
    s = importlib.util.spec_from_file_location(nom, os.path.join(ICI, f)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
vc = charger("vc4t", "verifier_citations_v5.py")
ra = charger("ra1t", "recherche_autorisee_v2.py")
PASSAGE = "Aucun score de moniteur n'entre dans un signal."


@pytest.fixture
def depot(tmp_path):
    d = tmp_path / "d"
    for rel, txt in {"docs/decisions/n.md": "Ligne une.\nAucun score de moniteur  n'entre\ndans un signal.\n",
                     "docs/notes/quarantaine/x.md": "secret moniteur\n",
                     "docs/notes/memoire-conception-v1/memo.md": "index moniteur\n",
                     "docs/notes/memoire-conception-v1/epreuve-essai-1-ne-pas-lire-bibliothecaire-v1/r.jsonl": "reponse moniteur\n",
                     "diag/x.json": "moniteur\n",
                     "registres/essaim/e.md": "moniteur ailleurs\n",
                     "registres/go.md": "| GO-1 | moniteur |\n"}.items():
        (d / rel).parent.mkdir(parents=True, exist_ok=True); (d / rel).write_text(txt)
    for c in (["init", "-q"], ["add", "-A"], ["-c", "user.email=a@b", "-c", "user.name=t", "commit", "-qm", "i"]):
        subprocess.run(["git", "-C", str(d), *c], check=True)
    commit = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    h = hashlib.sha256((d / "docs/decisions/n.md").read_bytes()).hexdigest()[:16]
    return d, commit, h


def outil(d, c, tmp_path, *args, bras="memo", agent="A"):
    j = tmp_path / "journal.jsonl"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = ra.main([*args, "--commit", c, "--bras", bras, "--agent", agent, "--journal", str(j), "--depot", str(d)])
    return rc, buf.getvalue(), j


def verifier(d, c, tmp_path, lignes, bras="memo", journal=None):
    r = tmp_path / "r.jsonl"; r.write_text("\n".join(json.dumps(l) for l in lignes) + "\n")
    out = tmp_path / "rapport.json"
    if out.exists(): out.unlink()
    j = journal or (tmp_path / "journal.jsonl")
    if not j.exists(): j.write_text("")
    rc = vc.main([str(r), str(out), "--commit", c, "--depot", str(d), "--journal", str(j), "--bras", bras])
    return rc, (json.loads(out.read_text()) if out.exists() else None)


def ligne(h, **kw):
    l = {"id": "Q1", "agent": "A", "citations": [{"chemin": "docs/decisions/n.md", "empreinte16": h, "passage": PASSAGE}],
         "fichiers_ouverts": ["docs/decisions/n.md"]}
    l.update(kw); return l


def test_chercher_ne_montre_que_l_autorise(depot, tmp_path):
    d, c, h = depot
    rc, sortie, j = outil(d, c, tmp_path, "chercher", "moniteur")
    assert "quarantaine" not in sortie and "essaim" not in sortie and "docs/decisions/n.md" in sortie and "registres/go.md" in sortie
    lus = {json.loads(l)["chemin"] for l in j.read_text().splitlines()}
    assert lus == {"docs/decisions/n.md", "registres/go.md", "docs/notes/memoire-conception-v1/memo.md"}


def test_bras_base_sans_memo(depot, tmp_path):
    d, c, h = depot
    rc, sortie, j = outil(d, c, tmp_path, "chercher", "moniteur", bras="base")
    assert "memoire-conception-v1" not in sortie
    rc, sortie, _ = outil(d, c, tmp_path, "lire", "docs/notes/memoire-conception-v1/memo.md", bras="base")
    assert rc == 2 and "index" not in sortie


def test_lire_exclu_refuse(depot, tmp_path):
    d, c, h = depot
    rc, sortie, j = outil(d, c, tmp_path, "lire", "docs/notes/quarantaine/x.md")
    assert rc == 2 and "secret" not in sortie and (not j.exists() or j.read_text() == "")


def test_commit_non_sha(depot, tmp_path):
    d, c, h = depot
    assert outil(d, "HEAD", tmp_path, "lister")[0] == 1


def test_empreinte(depot, tmp_path):
    d, c, h = depot
    assert outil(d, c, tmp_path, "empreinte", "docs/decisions/n.md")[1].strip() == h


def test_chaine_saine(depot, tmp_path):
    d, c, h = depot
    outil(d, c, tmp_path, "lire", "docs/decisions/n.md")
    rc, rap = verifier(d, c, tmp_path, [ligne(h)])
    assert rc == 0 and rap["porte_1_fichiers_ouverts"] and rap["porte_2_citations"]


def test_cite_hors_journal(depot, tmp_path):
    d, c, h = depot
    rc, rap = verifier(d, c, tmp_path, [ligne(h)])
    assert rc == 4 and not rap["porte_1_fichiers_ouverts"]


def test_journal_hors_liste(depot, tmp_path):
    d, c, h = depot
    j = tmp_path / "journal.jsonl"
    j.write_text(json.dumps({"agent": "A", "action": "lire", "chemin": "docs/decisions/n.md", "commit": c, "bras": "memo"}) + "\n" +
                 json.dumps({"agent": "A", "action": "lire", "chemin": "registres/essaim/e.md", "commit": c, "bras": "memo"}) + "\n")
    rc, rap = verifier(d, c, tmp_path, [ligne(h)], journal=j)
    assert rc == 4 and rap["journal_hors_liste"] == ["registres/essaim/e.md"]


def test_dossier_declare_ignore(depot, tmp_path):
    d, c, h = depot
    outil(d, c, tmp_path, "lire", "docs/decisions/n.md")
    rc, rap = verifier(d, c, tmp_path, [ligne(h, fichiers_ouverts=["docs/decisions/n.md", "registres/", "docs/notes/"])])
    assert rc == 0 and rap["dossiers_declares_ignores"] == 2


def test_barre_finale(depot):
    assert vc.chemin_autorise("docs/decisions/")[0] and vc.normaliser_chemin("docs/decisions/") == "docs/decisions"


def test_base_cite_memo(depot, tmp_path):
    d, c, h = depot
    hm = hashlib.sha256((d / "docs/notes/memoire-conception-v1/memo.md").read_bytes()).hexdigest()[:16]
    j = tmp_path / "journal.jsonl"
    j.write_text(json.dumps({"agent": "A", "action": "lire", "chemin": "docs/notes/memoire-conception-v1/memo.md", "commit": c, "bras": "base"}) + "\n")
    rc, rap = verifier(d, c, tmp_path, [ligne(h, citations=[], fichiers_ouverts=[])], bras="base", journal=j)
    assert rc == 4


def test_v5_ne_pas_lire_ferme(depot, tmp_path):
    d, c, h = depot
    rc, sortie, j = outil(d, c, tmp_path, "chercher", "moniteur")
    assert "ne-pas-lire" not in sortie
    rc, sortie, _ = outil(d, c, tmp_path, "lire", "docs/notes/memoire-conception-v1/epreuve-essai-1-ne-pas-lire-bibliothecaire-v1/r.jsonl")
    assert rc == 2 and "reponse" not in sortie
    rc, sortie, _ = outil(d, c, tmp_path, "lister", "docs/notes/memoire-conception-v1")
    assert "ne-pas-lire" not in sortie


def test_v5_dossier_exclu_declare(depot, tmp_path):
    d, c, h = depot
    outil(d, c, tmp_path, "lire", "docs/decisions/n.md")
    rc, rap = verifier(d, c, tmp_path, [ligne(h, fichiers_ouverts=["docs/decisions/n.md", "diag/"])])
    assert rc == 4


@pytest.mark.parametrize("alteration", [{"action": "inventee"}, {"commit": "0" * 40}, {"bras": "base"}, {"commit": None}])
def test_v5_journal_altere(depot, tmp_path, alteration):
    d, c, h = depot
    e = {"agent": "A", "action": "lire", "chemin": "docs/decisions/n.md", "commit": c, "bras": "memo"}
    e.update(alteration)
    j = tmp_path / "journal.jsonl"; j.write_text(json.dumps(e) + "\n")
    rc, rap = verifier(d, c, tmp_path, [ligne(h)], journal=j)
    assert rc == 4


def test_v5_agent_absent(depot, tmp_path):
    d, c, h = depot
    outil(d, c, tmp_path, "lire", "docs/decisions/n.md")
    l = ligne(h); del l["agent"]
    rc, rap = verifier(d, c, tmp_path, [l])
    assert rc == 4
