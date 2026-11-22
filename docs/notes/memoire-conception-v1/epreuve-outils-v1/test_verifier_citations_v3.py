"""Essais (cas sain et artefacts) de verifier_citations_v3.py. Lancer : python -m pytest -q docs/notes/memoire-conception-v1/epreuve-outils-v1/"""
import hashlib, importlib.util, json, os, subprocess
import pytest
ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("vc", os.path.join(ICI, "verifier_citations_v3.py"))
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


def ligne_sain(h, **kw):
    l = {"id": "Q1", "citations": [{"chemin": "docs/decisions/n.md", "empreinte16": h,
         "passage": "Aucun score de moniteur n'entre dans un signal."}], "fichiers_ouverts": ["docs/decisions/n.md"]}
    l.update(kw)
    return l


@pytest.mark.parametrize("chemin", ["docs/notes/demandes-fable-api-2026-11-22-v1/reponse-33-argon/reponse-33-argon-v1.md",
                                    "docs/notes/demandes-fable-api-2026-11-22-v1/journal-depense-22.jsonl",
                                    "docs/notes/demandes-fable-api-2026-11-22-v1/fusionnee-reponse-A.md",
                                    "docs/notes/papier-dopamine-moniteur-v1/resultats/x.md",
                                    "docs/notes/note-vérité-v1.md"])
def test_v2_exclus(chemin):
    assert not vc.chemin_autorise(chemin)[0]


@pytest.mark.parametrize("chemin", ["docs/decisions/decision-matiere-premiere-mentors-v1.md",
                                    "docs/notes/demandes-fable-api-2026-11-22-v1/demande-19-etau-equipe-rouge-quarantaine-v1.md",
                                    "docs/notes/demandes-fable-api-2026-11-22-v1/question-neutre-lot-quarantaine-servie-v1.md",
                                    "registres/passations/2026-11-10-1200-quarantaine.md",
                                    "docs/notes/demandes-fable-api-2026-11-22-v1/reponse-25/relecture-fable-api.md",
                                    "docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/x.md",
                                    "docs/notes/papier-dopamine-moniteur-v1/moniteur-dissonance-v1/conception.md"])
def test_v2_autorises(chemin):
    assert vc.chemin_autorise(chemin)[0]


@pytest.mark.parametrize("e", ["{h}zzzz", "{h}" + "0" * 48, "{h}"[:0] + "abc"])
def test_v2_empreinte_bruitee(depot, tmp_path, e):
    d, c, h = depot
    rc, _ = lancer(d, c, tmp_path, [ligne_sain(h, citations=[{"chemin": "docs/decisions/n.md", "empreinte16": e.format(h=h),
                                                               "passage": "Aucun score de moniteur n'entre dans un signal."}])])
    assert rc == 4


def test_v2_empreinte_entiere(depot, tmp_path):
    d, c, h = depot
    full = hashlib.sha256((d / "docs/decisions/n.md").read_bytes()).hexdigest()
    rc, _ = lancer(d, c, tmp_path, [ligne_sain(h, citations=[{"chemin": "docs/decisions/n.md", "empreinte16": full,
                                                               "passage": "Aucun score de moniteur n'entre dans un signal."}])])
    assert rc == 0


@pytest.mark.parametrize("p", ["dans un signal.", "core de moniteur n'entre dans un signa"])
def test_v2_passage_banal_ou_coupe(depot, tmp_path, p):
    d, c, h = depot
    rc, _ = lancer(d, c, tmp_path, [ligne_sain(h, citations=[{"chemin": "docs/decisions/n.md", "empreinte16": h, "passage": p}])])
    assert rc == 4


def test_v2_champs_absents(depot, tmp_path):
    d, c, h = depot
    l = ligne_sain(h)
    del l["fichiers_ouverts"]
    rc, _ = lancer(d, c, tmp_path, [l])
    assert rc == 4


def test_v2_chemin_absolu_du_depot(depot, tmp_path):
    d, c, h = depot
    rc, _ = lancer(d, c, tmp_path, [ligne_sain(h, fichiers_ouverts=[str(d / "docs/decisions/n.md")])])
    assert rc == 0


def test_v2_autre_racine(depot, tmp_path):
    d, c, h = depot
    rc, _ = lancer(d, c, tmp_path, [ligne_sain(h, fichiers_ouverts=["/etc/docs/decisions/n.md"])])
    assert rc == 4


@pytest.mark.parametrize("commit", ["main", "HEAD"])
def test_v2_commit_non_epingle(depot, tmp_path, commit):
    d, c, h = depot
    rc, rap = lancer(d, commit, tmp_path, [ligne_sain(h)])
    assert rc == 1 and rap is None


def test_v2_commit_abrege(depot, tmp_path):
    d, c, h = depot
    rc, rap = lancer(d, c[:12], tmp_path, [ligne_sain(h)])
    assert rc == 1


def test_v2_citation_exclue_compte_porte1(depot, tmp_path):
    d, c, h = depot
    hq = hashlib.sha256((d / "docs/notes/quarantaine/x.md").read_bytes()).hexdigest()[:16]
    rc, rap = lancer(d, c, tmp_path, [ligne_sain(h, citations=[{"chemin": "docs/notes/quarantaine/x.md", "empreinte16": hq,
                                                                 "passage": "secret"}], fichiers_ouverts=[])])
    assert rc == 4 and not rap["porte_1_fichiers_ouverts"]


def test_v2_identifiant_repete(depot, tmp_path):
    d, c, h = depot
    rc, rap = lancer(d, c, tmp_path, [ligne_sain(h), ligne_sain(h)])
    assert rc == 1


def test_v2_fichier_vide(depot, tmp_path):
    d, c, h = depot
    r = tmp_path / "vide.jsonl"; r.write_text("")
    assert vc.main([str(r), str(tmp_path / "o.json"), "--commit", c, "--depot", str(d)]) == 1


@pytest.mark.parametrize("chemin", ["docs/notes/memoire-conception-v1/epreuve-banque-ne-pas-lire-bibliothecaire-v1",
                                    "docs/notes/quarantaine", "docs/notes/archives-reponses-modeles"])
def test_v3_dossier_exclu_dernier_segment(chemin):
    assert not vc.chemin_autorise(chemin)[0]


def test_v3_citer_un_dossier(depot, tmp_path):
    d, c, h = depot
    rc, _ = lancer(d, c, tmp_path, [ligne_sain(h, citations=[{"chemin": "docs/decisions", "empreinte16": h,
                                                               "passage": "Aucun score de moniteur n'entre dans un signal."}])])
    assert rc == 4


@pytest.mark.parametrize("chemin,ok", [("docs/notes/demandes-fable-api-2026-11-22-v1/sous/demande-1.md", False),
                                       ("docs/notes/demandes-fable-api-2026-11-22-v1/demande-1-x-v1.md.sha256", True),
                                       ("docs/notes/demandes-fable-api-2026-11-22-v1/reponse-25/relecture-fable-api.md.sha256", True)])
def test_v3_motifs_demandes(chemin, ok):
    assert vc.chemin_autorise(chemin)[0] is ok


def test_v3_id_non_chaine(depot, tmp_path):
    d, c, h = depot
    rc, rap = lancer(d, c, tmp_path, [ligne_sain(h, id=["Q1"])])
    assert rc == 1
