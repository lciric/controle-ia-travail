"""Essais des outils de la fusion (listes de lecture v1, recherche bornée v3, partition v1, manifestes v1) : cas sains et
artefacts (R5). Lancer : python -m pytest -q docs/notes/memoire-conception-v1/fusion-outils-v1/test_fusion_outils_v1.py
"""
import importlib.util
import json
import os
import subprocess

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))


def charger(nom):
    spec = importlib.util.spec_from_file_location(nom, os.path.join(ICI, nom + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


ll = charger("listes_lecture_v1")
pj = charger("partition_journal_v1")
mf = charger("manifestes_fin_v1")
rb = charger("recherche_bornee_v3")


# ---------- liste stricte v4 ----------
@pytest.mark.parametrize("c", ["CLAUDE.md", "registres/decisions.md", "registres/veille.md", "docs/decisions/x.md",
                               "registres/veille-de-cap/commune/journal-commun-2026-11-22T1800Z.jsonl",
                               "registres/veille-de-cap/commune/journal-commun-2026-11-22T1800Z.jsonl.sha256",
                               "docs/notes/memoire-conception-v1/fusion-etape-2-deux-listes-deux-partitions-v1.md"])
def test_stricte_cas_sains(c):
    assert ll.autorise_stricte(c)[0], c


@pytest.mark.parametrize("c", [
    "registres/veille-de-cap/journal-des-idees-v1.jsonl",           # la fuite fermée
    "registres/veille-de-cap/mere/x.jsonl", "registres/veille-de-cap", "registres/veille-de-cap/",
    "registres/veille-de-cap/bulletins/bulletin-2026-11-22-1800.md",
    "registres/veille-de-cap/commune/../journal.jsonl",
    "registres/veille-de-cap/commune/scores-x.jsonl",
    "registres/veille-de-cap/commune/", "registres/veille-de-cap/commune",
    "docs/notes/veille-de-cap-v1/journal-des-idees-v1.jsonl",
    "docs/notes/memoire-conception-v1/liste-exhaustive-hypotheses-exploration-allumage-v1.md",
    "docs/notes/memoire-conception-v1/liste-exhaustive-hypotheses-exploration-allumage-v1.md.sha256",
    "docs/notes/memoire-conception-v1/versement-journal-22-novembre-v1/candidats-v1.jsonl",
    "docs/notes/memoire-conception-v1/versement-journal-22-novembre-v1",
    "docs/notes/memoire-conception-v1/recolte-session-bibliothecaire-2026-11-22-v2.md",
    "docs/notes/memoire-conception-v1/epreuve-banque-ne-pas-lire-bibliothecaire-v1/jeu-final-v1.jsonl",
    "runs/x/manifeste.json", "prereg/a.md", "docs/notes/index-pistes-v1/index-pistes-par-branche-v1.md"])
def test_stricte_artefacts(c):
    assert not ll.autorise_stricte(c)[0], c


def test_bras_base_exclut_memo():
    assert ll.autorise_bras("docs/notes/memoire-conception-v1/fusion-etape-2-deux-listes-deux-partitions-v1.md",
                            "base")[0] is False


# ---------- liste de la boucle ----------
@pytest.mark.parametrize("c,n", [
    ("docs/notes/index-pistes-v1/index-pistes-par-branche-v1.md", "plein"),
    ("docs/notes/veille-de-cap-v1/journal-des-idees-v1.jsonl", "plein"),
    ("registres/veille-de-cap/journal-des-idees-v1.jsonl", "plein"),
    ("registres/depenses.md", "plein"), ("registres/arrets.md", "plein"),
    ("registres/essaim/vers-mere/m.md", "plein"), ("registres/passations/2026-11-22-1559-bibliothecaire.md", "plein"),
    ("docs/sources/ideation-organism-a41b7b50-v1/inventaire.md", "plein"), ("CLAUDE.md", "plein"),
    ("prereg/a/b.md", "noms"), ("runs/20261004-034500-factice/manifeste.json", "noms"), ("diag/x.json", "noms"),
])
def test_boucle_cas_sains(c, n):
    assert ll.niveau_boucle(c)[0] == n, (c, ll.niveau_boucle(c))


@pytest.mark.parametrize("c", [
    "docs/notes/x/consigne-privee-v1.md", "docs/notes/x/conception-ii-b.md", "docs/notes/x/vérité-v1.md",
    "docs/notes/x/rendu.md", "docs/notes/x/scores.json", "docs/notes/SEQUESTRE/a.md",
    "brouillons/ii-b-saboteur-budget-v1/a.md", "donnees/bras-attaque-oracle-v1/a.json",
    "docs/notes/a/archives-reponses-modeles/b.md", "docs/notes/quarantaine/a.md", "matiere-premiere/a.md",
    "docs/notes/a/transcription-agent.md", "docs/notes/memoire-conception-v1/epreuve-essai-1-ne-pas-lire-x/a.md",
    "docs/notes/P3-mesures-v1.md", "docs/notes/barreau5-x.md", "docs/notes/essais-dates-t06-v1/a.md",
    "docs/notes/demandes-fable-api-2026-11-22-v1/demande-24.md", "docs/notes/protocole-x-programmation-de-poids-v1/a.md",
    "registres/index-bras-attaque-v8.md", "registres/iib-executante/a.md", "registres/t07-etape-b-bis-v1.md",
    "runs/x/scores.json", "prereg/rendu.md", "/etc/passwd", "../x", "src/controle_ia/x.py"])
def test_boucle_artefacts(c):
    assert ll.niveau_boucle(c)[0] == "refus", (c, ll.niveau_boucle(c))


# ---------- partition ----------
@pytest.fixture
def depot(tmp_path):
    d = tmp_path / "d"
    d.mkdir()
    (d / "registres").mkdir()
    (d / "registres" / "decisions.md").write_text("- R-1 — Une idée portée : la base boîte noire par action, à tester.\n")
    (d / "docs" / "notes" / "veille-de-cap-v1").mkdir(parents=True)
    (d / "docs" / "notes" / "veille-de-cap-v1" / "registre.md").write_text("Ligne de la veille, lecture large ici.\n")
    for args in (["init", "-q"], ["add", "."], ["-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "-m", "x"]):
        subprocess.run(["git", "-C", str(d), *args], check=True)
    sha = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    return str(d), sha


def ev(fiche, evt, chemin, extrait, commit, nom="Base boîte noire", mots=("base",)):
    return {"quand": "2026-11-22T18:00:00Z", "fiche": fiche, "evenement": evt, "nom": nom, "etat": "proposée",
            "source": {"chemin": chemin, "commit": commit, "repere": "r", "extrait": extrait},
            "porteur": "x", "sert": "porte G0", "issue": None, "raison": "texte libre", "reveil": None,
            "mots": list(mots), "origine": "2026-10-04", "derniere_trace": "2026-11-14"}


def test_partition_cas_sain(depot):
    d, sha = depot
    e = ev("I-1", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", sha[:8])
    sortie, c = pj.partitionner([e], d)
    assert c["commune"] == 1 and c["mere"] == 0
    r = sortie[0]
    assert set(r) == set(pj.CHAMPS_COMMUNS) and "origine" not in r and "derniere_trace" not in r
    assert r["raison"] is None and r["partition"] == "commune"


def test_partition_artefacts(depot):
    d, sha = depot
    evs = [
        ev("I-2", "naissance", "docs/notes/veille-de-cap-v1/registre.md", "Ligne de la veille, lecture large ici.", sha),
        ev("I-3", "naissance", "registres/decisions.md", "phrase qui n'existe pas dans la source", sha),
        ev("I-4", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", "deadbeef"),
        ev("I-5", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", sha,
           nom="Lecture des scores de la course"),
        ev("I-6", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", sha),
        ev("I-2", "etat", "registres/decisions.md", "Une idée portée : la base boîte noire", sha),   # née mère
        ev("I-7", "etat", "registres/decisions.md", "Une idée portée : la base boîte noire", sha),   # sans naissance
        None, {"pas": "de fiche"},
    ]
    sortie, c = pj.partitionner(evs, d, marquees={"I-6"})
    assert sortie == [] and c["commune"] == 0 and c["mere"] == len(evs) and c["illisibles"] == 2


def test_partition_seconde_naissance_mere(depot):
    d, sha = depot
    bon = ev("I-8", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", sha)
    mauvais = ev("I-8", "naissance", "docs/notes/veille-de-cap-v1/registre.md", "Ligne de la veille, lecture large ici.", sha)
    sortie, c = pj.partitionner([bon, mauvais], d)
    assert sortie == []


def test_partition_sortie_hors_commune_refusee(depot, tmp_path):
    d, _ = depot
    j = tmp_path / "j.jsonl"
    j.write_text("")
    assert pj.main([str(tmp_path / "sortie.jsonl"), str(j), "--depot", d]) == 1


# ---------- manifestes ----------
def test_manifestes(tmp_path):
    r = tmp_path / "runs"
    (r / "20261122-a").mkdir(parents=True)
    (r / "20261122-a" / "manifeste.json").write_text(json.dumps(
        {"run_id": "a", "cree_le": "t", "decisif": False, "depot_propre": True, "commit": "c",
         "config": {"seuil": 0.7}, "graines": [1], "reserves": "secret", "commande": "x"}))
    (r / "20261122-a" / "manifeste-lanceur-fin.json").write_text(json.dumps(
        {"id": "a", "debut_utc": "d", "fin_utc": "f", "code": 0, "sortie_existe": True, "pid_orchestrateur": 1}))
    (r / "20261122-a" / "scores.json").write_text("{}")
    (r / "20261122-b").mkdir()
    (r / "20261122-b" / "manifeste.json").write_text("pas du json")
    (r / "20261122-rendu").mkdir()
    sortie, caches = mf.releve(str(r))
    assert caches == 1 and len(sortie) == 2
    a = sortie[0]
    texte = json.dumps(a)
    assert "seuil" not in texte and "secret" not in texte and "graines" not in texte and "pid" not in texte
    assert "[nom exclu]" in a["fichiers"] and "scores.json" not in a["fichiers"]
    assert a["manifeste-lanceur-fin.json"]["code"] == 0
    assert sortie[1]["manifeste.json"] == "illisible"


# ---------- recherche bornée v3 ----------
def test_recherche_noms_seuls_et_fuite(depot, tmp_path, capsys):
    d, sha = depot
    for p, t in (("prereg/a.md", "secret\n"), ("registres/veille-de-cap/journal.jsonl", "mere\n"),
                 ("registres/veille-de-cap/commune/journal-commun.jsonl", "commune\n")):
        f = os.path.join(d, p)
        os.makedirs(os.path.dirname(f), exist_ok=True)
        open(f, "w").write(t)
    subprocess.run(["git", "-C", d, "add", "."], check=True)
    subprocess.run(["git", "-C", d, "-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "-m", "y"], check=True)
    sha = subprocess.run(["git", "-C", d, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    j = str(tmp_path / "journal.jsonl")
    base = ["--commit", sha, "--agent", "t", "--journal", j, "--depot", d]
    assert rb.main(["lire", "registres/veille-de-cap/journal.jsonl", "--bras", "memo", *base]) == 2
    assert rb.main(["lire", "registres/veille-de-cap/commune/journal-commun.jsonl", "--bras", "memo", *base]) == 0
    assert rb.main(["lire", "prereg/a.md", "--bras", "boucle", *base]) == 2
    assert "REFUS : noms seuls" in capsys.readouterr().out
    rb.main(["lister", "prereg", "--bras", "boucle", *base])
    assert "prereg/a.md" in capsys.readouterr().out
    rb.main(["chercher", "secret", "--bras", "boucle", *base])
    assert "secret" not in capsys.readouterr().out
    assert rb.main(["lire", "registres/veille-de-cap/journal.jsonl", "--bras", "boucle", *base]) == 0
    lus = [json.loads(l)["chemin"] for l in open(j)]
    assert "prereg/a.md" not in lus and "registres/veille-de-cap/journal.jsonl" in lus
