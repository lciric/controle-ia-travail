"""Essais de la porte de périmètre v2 et de la journalisation de recherche_bornee_v6 : cas sain et artefacts (R5).
Lancer : python -m pytest -q docs/notes/memoire-conception-v1/fusion-outils-v1/test_porte_perimetre_v2.py
"""
import datetime
import importlib.util
import json
import os
import subprocess

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))


def charger(nom):
    s = importlib.util.spec_from_file_location(nom, os.path.join(ICI, nom + ".py"))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


pp = charger("porte_perimetre_v2")
rb = charger("recherche_bornee_v6")
JOUR = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


@pytest.fixture
def depot(tmp_path):
    d = tmp_path / "d"
    (d / "registres" / "veille-de-cap").mkdir(parents=True)
    (d / "registres" / "decisions.md").write_text("ligne\n")
    (d / "registres" / "veille-de-cap" / "journal.jsonl").write_text("{}\n")
    for args in (["init", "-q", "-b", "main"], ["add", "."],
                 ["-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "-m", "x"]):
        subprocess.run(["git", "-C", str(d), *args], check=True)
    sha = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    return str(d), sha


def lire(d, sha, chemin, role, session="S1", agent="a"):
    env = {"MEMOIRE_ROLE": role, "MEMOIRE_SESSION": session, "MEMOIRE_AGENT": agent}
    ancien = {k: os.environ.get(k) for k in env}
    os.environ.update(env)
    try:
        return rb.main(["lire", chemin, "--commit", sha, "--depot", d])
    finally:
        for k, v in ancien.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def jpath(d, role):
    return os.path.join(d, pp.DOSSIER, f"{role}-{JOUR}.jsonl")


def test_outil_sans_environnement_refuse(depot, monkeypatch):
    d, sha = depot
    for k in ("MEMOIRE_ROLE", "MEMOIRE_SESSION", "MEMOIRE_AGENT"):
        monkeypatch.delenv(k, raising=False)
    assert rb.main(["lire", "registres/decisions.md", "--commit", sha, "--depot", d]) == 1
    with pytest.raises(SystemExit):
        rb.main(["lire", "registres/decisions.md", "--commit", sha, "--depot", d, "--journal", "/dev/null"])
    with pytest.raises(SystemExit):
        rb.main(["lire", "registres/decisions.md", "--commit", sha, "--depot", d, "--bras", "boucle"])


def test_cas_sain(depot):
    d, sha = depot
    assert lire(d, sha, "registres/decisions.md", "reponse", "S1") == 0
    assert lire(d, sha, "registres/veille-de-cap/journal.jsonl", "boucle", "S2") == 0
    assert lire(d, sha, "registres/veille-de-cap/journal.jsonl", "reponse", "S1") == 2   # refus de l'outil, non journalisé
    r = pp.juger(d, {"jour": JOUR, "sessions": {"S1": "reponse", "S2": "boucle"}})
    assert r["verdict"] == "tient" and r["lignes"] == 2, r


def test_p1_journee_vide(depot):
    d, _ = depot
    assert pp.juger(d, {"jour": JOUR, "sessions": {"S1": "reponse"}})["verdict"] == "tombe"
    assert pp.juger(d, {"jour": JOUR, "sessions": {}})["verdict"] == "tient"


def test_p3_session_qui_se_declare_boucle(depot):
    d, sha = depot
    assert lire(d, sha, "registres/veille-de-cap/journal.jsonl", "boucle", "S1") == 0
    r = pp.juger(d, {"jour": JOUR, "sessions": {"S1": "reponse"}})
    assert r["verdict"] == "tombe" and any("rôle boucle au lieu de reponse" in m["motif"] for m in r["detail"])
    r = pp.juger(d, {"jour": JOUR, "sessions": {}})
    assert r["verdict"] == "tombe" and any("non déclarée" in m["motif"] for m in r["detail"])


@pytest.mark.parametrize("alteration", ["tronquer", "retirer_milieu", "vider", "temoin_absent", "ajouter_hors_outil",
                                        "non_utf8", "dossier"])
def test_p4_p6_alterations(depot, alteration):
    d, sha = depot
    for _ in range(3):
        assert lire(d, sha, "registres/decisions.md", "reponse", "S1") == 0
    j = jpath(d, "reponse")
    lignes = open(j, encoding="utf-8").read().split("\n")[:-1]
    if alteration == "tronquer":
        open(j, "w", encoding="utf-8").write("\n".join(lignes[:2]) + "\n")
    elif alteration == "retirer_milieu":
        open(j, "w", encoding="utf-8").write("\n".join([lignes[0], lignes[2]]) + "\n")
    elif alteration == "vider":
        open(j, "w").write("")
    elif alteration == "temoin_absent":
        os.remove(j[:-len(".jsonl")] + ".temoin")
    elif alteration == "ajouter_hors_outil":
        e = json.loads(lignes[-1])
        e["n"], e["chemin"] = 4, "registres/veille-de-cap/journal.jsonl"
        open(j, "a", encoding="utf-8").write(json.dumps(e) + "\n")
    elif alteration == "non_utf8":
        open(j, "ab").write(b"\xff\xfe\n")
    elif alteration == "dossier":
        os.remove(j)
        os.mkdir(j)
    r = pp.juger(d, {"jour": JOUR, "sessions": {"S1": "reponse"}})
    assert r["verdict"] == "tombe", (alteration, r)


def test_p5_autre_journee(depot):
    d, sha = depot
    assert lire(d, sha, "registres/decisions.md", "reponse", "S1") == 0
    r = pp.juger(d, {"jour": "2000-01-01", "sessions": {"S1": "reponse"}})
    assert r["verdict"] == "tombe"   # aucune ligne ce jour-là pour une session déclarée


def test_p7_chemin_absent_au_commit(depot):
    d, sha = depot
    assert lire(d, sha, "registres/decisions.md", "reponse", "S1") == 0
    j = jpath(d, "reponse")
    brut = open(j, encoding="utf-8").read().rstrip("\n")
    e = json.loads(brut)
    e["chemin"] = "registres/inexistant.md"
    neuf = json.dumps(e, ensure_ascii=False)
    open(j, "w", encoding="utf-8").write(neuf + "\n")
    import hashlib
    json.dump({"n": 1, "empreinte": hashlib.sha256(neuf.encode()).hexdigest()}, open(j[:-6] + ".temoin", "w"))
    r = pp.juger(d, {"jour": JOUR, "sessions": {"S1": "reponse"}})
    assert r["verdict"] == "tombe" and any("fichier ordinaire" in m["motif"] for m in r["detail"]), r


def test_main_codes(depot, tmp_path):
    d, sha = depot
    assert lire(d, sha, "registres/decisions.md", "reponse", "S1") == 0
    s = tmp_path / "s.json"
    s.write_text(json.dumps({"jour": JOUR, "sessions": {"S1": "reponse"}}))
    assert pp.main([str(s), str(tmp_path / "r1.json"), "--depot", d]) == 0
    assert pp.main([str(s), str(tmp_path / "r1.json"), "--depot", d]) == 1
    s.write_text(json.dumps({"jour": JOUR, "sessions": {"S1": "tout"}}))
    assert pp.main([str(s), str(tmp_path / "r2.json"), "--depot", d]) == 1
