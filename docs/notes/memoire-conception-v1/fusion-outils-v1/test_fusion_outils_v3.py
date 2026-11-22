"""Essais des outils de la fusion, version 3 (listes de lecture v3, recherche bornée v5, partition v3, manifestes v2) : cas sains et
artefacts (R5). Lancer : python -m pytest -q docs/notes/memoire-conception-v1/fusion-outils-v1/test_fusion_outils_v3.py
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


ll = charger("listes_lecture_v3")
pj = charger("partition_journal_v3")
mf = charger("manifestes_fin_v2")
rb = charger("recherche_bornee_v5")


# ---------- liste stricte v4 ----------
@pytest.mark.parametrize("c", ["CLAUDE.md", "registres/decisions.md", "registres/veille.md", "registres/veille.md.sha256",
                               "docs/decisions/x.md",
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
    "registres/veille-de-cap-v1/a.md", "registres/veille-de-cap.jsonl", "registres/veille-de-capx/a", "registres/veille/x",
    "registres/veilleur/x", "registres/veille-de-cap/commune/notes-libres.md", "registres/veille-de-cap/commune/sous/x.md",
    "registres/veille-de-cap/commune/journal-commun.jsonl",
    "docs/notes/memoire-conception-v1/versement-journal-22-novembre-v2/candidats-v2.jsonl",
    "docs/notes/memoire-conception-v1/liste-exhaustive-hypotheses-exploration-allumage-v2.md",
    "docs/notes/x/reponse-24-v1.md", "docs/notes/x/demande_24.md",
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
    ("prereg/a/b.md", "noms"), ("docs/sources/pdf/a.pdf", "noms"), ("registres/canaux-sessions-v7.md", "plein"), ("runs/20261004-034500-factice/manifeste.json", "noms"), ("diag/x.json", "noms"),
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
    "docs/notes/autre/reponse-24-fable.md", "registres/veille-de-cap-v1/a.md",
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
    for args in (["init", "-q", "-b", "main"], ["add", "."], ["-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "-m", "x"]):
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
    e = ev("I-0001", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", sha[:8])
    sortie, c = pj.partitionner([e], d)
    assert c["commune"] == 1 and c["mere"] == 0
    r = sortie[0]
    assert set(r) == set(pj.CHAMPS_COMMUNS) and "origine" not in r and "derniere_trace" not in r
    assert r["raison"] is None and r["partition"] == "commune"


def test_partition_artefacts(depot):
    d, sha = depot
    evs = [
        ev("I-0002", "naissance", "docs/notes/veille-de-cap-v1/registre.md", "Ligne de la veille, lecture large ici.", sha),
        ev("I-0003", "naissance", "registres/decisions.md", "phrase qui n'existe pas dans la source", sha),
        ev("I-0004", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", "deadbeef"),
        ev("I-0005", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", sha,
           nom="Lecture des scores de la course"),
        ev("I-0006", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", sha),
        ev("I-0002", "etat", "registres/decisions.md", "Une idée portée : la base boîte noire", sha),   # née mère
        ev("I-0007", "etat", "registres/decisions.md", "Une idée portée : la base boîte noire", sha),   # sans naissance
        None, {"pas": "de fiche"},
    ]
    sortie, c = pj.partitionner(evs, d, marquees={"I-0006"})
    assert sortie == [] and c["commune"] == 0 and c["mere"] == len(evs) and sum(c["motifs"].values()) == len(evs)


def test_partition_seconde_naissance_mere(depot):
    d, sha = depot
    bon = ev("I-0008", "naissance", "registres/decisions.md", "Une idée portée : la base boîte noire", sha)
    mauvais = ev("I-0008", "naissance", "docs/notes/veille-de-cap-v1/registre.md", "Ligne de la veille, lecture large ici.", sha)
    sortie, c = pj.partitionner([bon, mauvais], d)
    assert sortie == []


def test_partition_horodatage_impose(depot, tmp_path):
    d, _ = depot
    j = tmp_path / "j.jsonl"
    j.write_text("")
    assert pj.main([str(j), "--horodatage", "../../x", "--depot", d]) == 1
    assert pj.main([str(j), "--horodatage", "2026-11-22T1800Z", "--depot", d,]) == 0
    assert os.path.exists(os.path.join(d, "registres/veille-de-cap/commune/journal-commun-2026-11-22T1800Z.jsonl.sha256"))
    assert pj.main([str(j), "--horodatage", "2026-11-22T1800Z", "--depot", d,]) == 1


# ---------- manifestes ----------
def test_manifestes(tmp_path):
    r = tmp_path / "runs"
    (r / "20261122-a").mkdir(parents=True)
    (r / "20261122-a" / "manifeste.json").write_text(json.dumps(
        {"run_id": "a", "cree_le": "2026-11-22T10:00:00Z", "decisif": False, "depot_propre": True, "commit": "c",
         "config": {"seuil": 0.7}, "graines": [1], "reserves": "secret", "commande": "x"}))
    (r / "20261122-a" / "manifeste-lanceur-fin.json").write_text(json.dumps(
        {"id": "a", "debut_utc": "2026-11-22T10:00:00Z", "fin_utc": "seuil 0,7 franchi", "code": "0.93",
         "sortie_existe": True, "pid_orchestrateur": 1}))
    (r / "20261122-a" / "scores.json").write_text("{}")
    (r / "20261122-b").mkdir()
    (r / "20261122-b" / "manifeste.json").write_text("pas du json")
    (r / "20261122-c").mkdir()
    os.symlink(str(r / "20261122-a" / "manifeste.json"), str(r / "20261122-c" / "manifeste.json"))
    (r / "20261122-rendu").mkdir()
    sortie, caches = mf.releve(str(r))
    assert caches == 1 and len(sortie) == 3
    a = sortie[0]
    texte = json.dumps(a)
    for interdit in ("seuil", "secret", "graines", "pid", "run_id", "decisif", "commit", "0.93"):
        assert interdit not in texte, interdit
    assert "[nom exclu]" in a["fichiers"] and "scores.json" not in a["fichiers"]
    assert a["manifeste-lanceur-fin.json"] == {"debut_utc": "2026-11-22T10:00:00Z", "fin_utc": "non conforme",
                                               "code": "non conforme", "sortie_existe": True}
    assert a["manifeste.json"] == {"cree_le": "2026-11-22T10:00:00Z"}
    assert sortie[1]["manifeste.json"] == "illisible" and sortie[2]["manifeste.json"] == "illisible"


# ---------- recherche bornée v3 ----------
def test_recherche_noms_seuls_et_fuite(depot, tmp_path, capsys):
    d, sha = depot
    for p, t in (("prereg/a.md", "secret\n"), ("registres/veille-de-cap/journal.jsonl", "mere\n"),
                 ("registres/veille-de-cap/commune/journal-commun-2026-11-22T1800Z.jsonl", "commune\n")):
        f = os.path.join(d, p)
        os.makedirs(os.path.dirname(f), exist_ok=True)
        open(f, "w").write(t)
    subprocess.run(["git", "-C", d, "add", "."], check=True)
    subprocess.run(["git", "-C", d, "-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "-m", "y"], check=True)
    sha = subprocess.run(["git", "-C", d, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    j = str(tmp_path / "journal.jsonl")
    base = ["--commit", sha, "--agent", "t", "--journal", j, "--depot", d,]
    assert rb.main(["lire", "registres/veille-de-cap/journal.jsonl", "--bras", "memo", *base]) == 2
    assert rb.main(["lire", "registres/veille-de-cap/commune/journal-commun-2026-11-22T1800Z.jsonl", "--bras", "memo", *base]) == 0
    assert rb.main(["lire", "prereg/a.md", "--bras", "boucle", *base]) == 2
    assert "REFUS : noms seuls" in capsys.readouterr().out
    rb.main(["lister", "prereg", "--bras", "boucle", *base])
    assert "prereg/a.md" in capsys.readouterr().out
    rb.main(["chercher", "secret", "--bras", "boucle", *base])
    assert "secret" not in capsys.readouterr().out
    assert rb.main(["lire", "registres/veille-de-cap/journal.jsonl", "--bras", "boucle", *base]) == 0
    lus = [json.loads(l)["chemin"] for l in open(j)]
    assert "prereg/a.md" not in lus and "registres/veille-de-cap/journal.jsonl" in lus


# ---------- corrections de la contre-lecture (C1 à C7) ----------
BON = "Une idée portée : la base boîte noire"


def test_c1_source_dossier(depot):
    d, sha = depot
    e = ev("I-0011", "naissance", "registres", "decisions.md", sha)
    assert pj.partitionner([e], d)[0] == []


@pytest.mark.parametrize("mots", ["quarantaine", {"a": "b"}, ["ok", 3], None])
def test_c2_mots_mal_types(depot, mots):
    d, sha = depot
    e = ev("I-0012", "naissance", "registres/decisions.md", BON, sha)
    e["mots"] = mots
    assert pj.partitionner([e], d)[0] == []


@pytest.mark.parametrize("nom", ["piste quarantaine du jumeau", "matiere-premiere des modes", "branche lot/compte-4-v1",
                                 "archives-reponses-modeles", "reponse-24 de Fable"])
def test_c3_noms_exclus_elargis(depot, nom):
    d, sha = depot
    assert pj.partitionner([ev("I-0013", "naissance", "registres/decisions.md", BON, sha, nom=nom)], d)[0] == []


def test_c4_commit_non_hachable_sans_arret(depot):
    d, sha = depot
    mauvais = ev("I-0014", "naissance", "registres/decisions.md", BON, sha)
    mauvais["source"]["commit"] = ["x"]
    bon = ev("I-0015", "naissance", "registres/decisions.md", BON, sha)
    sortie, c = pj.partitionner([mauvais, bon, "texte"], d)
    assert [r["fiche"] for r in sortie] == ["I-0015"] and c["mere"] == 2 and sum(c["motifs"].values()) == 2


def test_c5_valeurs_fermees(depot):
    d, sha = depot
    e = ev("I-0016", "naissance", "registres/x/../decisions.md", BON, sha)
    sortie, _ = pj.partitionner([e], d)
    assert sortie and sortie[0]["source"]["chemin"] == "registres/decisions.md" and len(sortie[0]["source"]["commit"]) == 40
    for champ, val in (("sert", {"a": 1}), ("etat", "en cours de tout"), ("evenement", "autre"), ("issue", "réussi")):
        e2 = ev("I-0017", "naissance", "registres/decisions.md", BON, sha)
        e2[champ] = val
        assert pj.partitionner([e2], d)[0] == [], champ


@pytest.mark.parametrize("fiche,marque", [("I-0018", " i-0018 "), ("I-0018", "I-0018\n")])
def test_c6_marques_normalisees(depot, fiche, marque):
    d, sha = depot
    assert pj.partitionner([ev(fiche, "naissance", "registres/decisions.md", BON, sha)], d, marquees={marque})[0] == []


@pytest.mark.parametrize("fiche", ["F1 ", "I-18", "i-0018", "I-0018 "])
def test_c6_identifiant_mal_forme(depot, fiche):
    d, sha = depot
    assert pj.partitionner([ev(fiche, "naissance", "registres/decisions.md", BON, sha)], d)[0] == []


def test_c7_commit_hors_principale(depot):
    d, sha = depot
    subprocess.run(["git", "-C", d, "checkout", "-q", "-b", "lot/compte-4-v1"], check=True)
    open(os.path.join(d, "registres", "decisions.md"), "a").write("- R-2 — Une ligne écrite sur une branche exclue seulement.\n")
    subprocess.run(["git", "-C", d, "-c", "user.email=a@b", "-c", "user.name=a", "commit", "-qam", "z"], check=True)
    sha2 = subprocess.run(["git", "-C", d, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    e = ev("I-0019", "naissance", "registres/decisions.md", "Une ligne écrite sur une branche exclue seulement", sha2)
    assert pj.partitionner([e], d)[0] == []


def test_remarque5_extrait_court_ou_coupe(depot):
    d, sha = depot
    for ext in ("idée portée", "ne idée portée : la base boîte noire"):
        assert pj.partitionner([ev("I-0020", "naissance", "registres/decisions.md", ext, sha)], d)[0] == []


def test_c9_nom_accentue_et_lien(depot, tmp_path, capsys):
    d, _ = depot
    os.makedirs(os.path.join(d, "docs", "decisions"), exist_ok=True)
    open(os.path.join(d, "docs", "decisions", "décision-é.md"), "w").write("accentué lisible\n")
    os.symlink("../../registres/decisions.md", os.path.join(d, "docs", "decisions", "lien.md"))
    subprocess.run(["git", "-C", d, "add", "."], check=True)
    subprocess.run(["git", "-C", d, "-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "-m", "w"], check=True)
    sha = subprocess.run(["git", "-C", d, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    base = ["--commit", sha, "--agent", "t", "--journal", str(tmp_path / "j.jsonl"), "--depot", d,]
    assert rb.main(["lire", "docs/decisions/décision-é.md", "--bras", "memo", *base]) == 0
    assert "accentué lisible" in capsys.readouterr().out
    assert rb.main(["lire", "docs/decisions/lien.md", "--bras", "memo", *base]) == 2


def test_c7_outil_commit_hors_principale(depot, tmp_path):
    d, sha = depot
    subprocess.run(["git", "-C", d, "checkout", "-q", "-b", "autre"], check=True)
    subprocess.run(["git", "-C", d, "-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "--allow-empty", "-m", "v"],
                   check=True)
    sha2 = subprocess.run(["git", "-C", d, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    base = ["--agent", "t", "--journal", str(tmp_path / "j.jsonl"), "--depot", d]
    assert rb.main(["lire", "registres/decisions.md", "--bras", "memo", "--commit", sha2, *base]) == 1
    assert rb.main(["lire", "registres/decisions.md", "--bras", "memo", "--commit", sha, *base]) == 0


# ---------- restes de la vérification de la v2 ----------
@pytest.mark.parametrize("c", ["docs/notes/x/demandes-24-v1.md", "docs/notes/x/reponses-24.md", "docs/notes/x/demande-024.md",
                               "docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md",
                               "docs/notes/memoire-conception-v1/reecriture-v3/fiches-a.md",
                               "docs/notes/memoire-conception-v1/questions-fond-v1/q.md",
                               "docs/notes/memoire-conception-v1/Liste-Exhaustive-x.md"])
def test_v3_exclusions_elargies(c):
    assert not ll.autorise_stricte(c)[0], c
    if "memoire-conception" not in c:
        assert ll.niveau_boucle(c)[0] == "refus", c


@pytest.mark.parametrize("c", ["docs/notes/x/demande-240.md", "docs/notes/x/reponse-124.md", "docs/notes/x/demande-41-v1.md"])
def test_v3_24_sans_faux_positif(c):
    assert ll.niveau_boucle(c)[0] == "plein", c


def test_v3_nom_extrait_chiffres_ascii():
    assert not ll.autorise_stricte("registres/veille-de-cap/commune/journal-commun-٢٠٢٦-11-22T1800Z.jsonl")[0]


@pytest.mark.parametrize("champ", ["sert", "repere"])
def test_v3_garde_repere_sert(depot, champ):
    d, sha = depot
    e = ev("I-0030", "naissance", "registres/decisions.md", BON, sha)
    if champ == "sert":
        e["sert"] = "consigne-privee : seuil"
    else:
        e["source"]["repere"] = "consigne-privee : seuil"
    assert pj.partitionner([e], d)[0] == []


def test_v3_pas_d_option_de_branche(depot, tmp_path):
    d, sha = depot
    with pytest.raises(SystemExit):
        rb.main(["lire", "registres/decisions.md", "--bras", "memo", "--commit", sha, "--agent", "t", "--journal",
                 str(tmp_path / "j.jsonl"), "--depot", d, "--ref-principale", "lot/compte-4-v1"])
    with pytest.raises(SystemExit):
        pj.main([str(tmp_path / "j.jsonl"), "--horodatage", "2026-11-22T1900Z", "--depot", d, "--ref-principale", "x"])
