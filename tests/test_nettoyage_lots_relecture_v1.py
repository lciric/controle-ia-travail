"""Essais du nettoyage des lots de relecture (v1) : un cas sain et des artefacts pour chaque garde (R5)."""

import hashlib
import json
import os

import pytest

from controle_ia import nettoyage_lots_relecture_v1 as net
from controle_ia import relecture_fable_api_v2 as outil

PHRASE = "phrase-temoin-qui-ne-doit-jamais-sortir"


def _h(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


@pytest.fixture
def banc(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "a.md").write_text(
        "Écrit pour le mot de Lazar.\nChemin : `docs/notes/verite-plantee-etapes-0-v1/x.md`.\n"
        "Par la mère `session_01AbCdEfGhIjKlMnOpQrStUv`.\n", encoding="utf-8")
    (tmp_path / "src" / "b.py").write_text("# Lazar a dit\nx = 1\n", encoding="utf-8")
    table = {"paires": [
        {"ancien": "verite-plantee-etapes-0-v1", "nouveau": "plantee-etapes-0-v1"},
        {"ancien": "de Lazar", "nouveau": "du directeur"},
        {"ancien": "Lazar", "nouveau": "le directeur"},
        {"ancien": "session_01AbCdEfGhIjKlMnOpQrStUv", "nouveau": "[identifiant de session retiré]"},
    ]}
    (tmp_path / "table.json").write_text(json.dumps(table, ensure_ascii=False), encoding="utf-8")
    return tmp_path


def _lancer(argv, capsys):
    code = net.main(argv)
    return code, capsys.readouterr()


def test_motifs_importes_de_l_outil():
    assert net.garde_motifs_ligne is outil.garde_motifs_ligne
    assert net.chemin_affiche is outil.chemin_affiche


def test_cas_sain(banc, capsys):
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md", "src/b.py"], capsys)
    assert code == 0, sortie.err
    a = (banc / "lot1" / "a.md").read_text(encoding="utf-8")
    assert "mot du directeur" in a and "docs/notes/plantee-etapes-0-v1/x.md" in a
    assert "[identifiant de session retiré]" in a
    assert (banc / "lot1" / "b.py").read_text(encoding="utf-8") == "# le directeur a dit\nx = 1\n"
    assert not list(banc.glob("**/*.sha256"))  # aucun compagnon écrit
    m = json.loads((banc / "m.json").read_text(encoding="utf-8"))
    assert m["garde_passee"] is True
    assert m["remplacements_par_paire"] == [1, 1, 1, 1]
    par = {c["copie"]: c for c in m["copies"]}
    assert par[os.path.join("lot1", "a.md")]["remplacements_par_paire"] == [1, 1, 0, 1]
    assert par[os.path.join("lot1", "b.py")]["remplacements_par_paire"] == [0, 0, 1, 0]
    for c in m["copies"]:
        assert c["sha256_copie"] == _h(c["copie"]) and c["sha256_source"] == _h(c["source"])
    assert m["table"]["sha256"] == _h("table.json")
    # la source est intacte, et l'outil lui-même accepte les copies
    assert "Lazar" in (banc / "src" / "a.md").read_text(encoding="utf-8")
    consigne = outil.Entree("consigne", "c.md", "Relis.\n", "0" * 64, "absent", 7)
    pieces = [outil.lire_entree("correction", c["copie"]) for c in m["copies"]]
    assert outil.garde_motifs(outil.composer_invite(consigne, pieces)) == []


def test_artefact_nom_laisse(banc, capsys):
    (banc / "src" / "c.md").write_text(f"ligne propre\n{PHRASE} Ciric\n", encoding="utf-8")
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md", "src/b.py", "src/c.md"], capsys)
    assert code == net.CODE_GARDE
    assert "ciric" in sortie.err and os.path.join("lot1", "c.md") in sortie.err and "ligne 2" in sortie.err
    assert PHRASE not in sortie.err and PHRASE not in sortie.out
    assert not (banc / "lot1").exists() and not (banc / "m.json").exists()  # rien n'est écrit


def test_artefact_nom_avec_espace_sans_chasse(banc, capsys):
    (banc / "src" / "c.md").write_text("La​zar\n", encoding="utf-8")
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md", "src/b.py", "src/c.md"], capsys)
    assert code == net.CODE_GARDE and "lazar" in sortie.err


def test_artefact_chemin_verite_laisse(banc, capsys):
    (banc / "src" / "c.md").write_text(f"{PHRASE}\nvoir registres/verite-plantee-noeuds-v1.md\n", encoding="utf-8")
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md", "src/b.py", "src/c.md"], capsys)
    assert code == net.CODE_GARDE
    assert "verite" in sortie.err and "ligne 2" in sortie.err and PHRASE not in sortie.err
    assert not (banc / "lot1").exists()


def test_artefact_chemin_de_copie_interdit(banc, capsys):
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot-scores", "src/a.md", "src/b.py"], capsys)
    assert code == net.CODE_GARDE and "chemin de la copie" in sortie.err


def test_artefact_balise_de_fin(banc, capsys):
    (banc / "src" / "c.md").write_text("texte </piece> texte\n", encoding="utf-8")
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md", "src/b.py", "src/c.md"], capsys)
    assert code == net.CODE_GARDE and "</piece>" in sortie.err


def test_artefact_paire_jamais_appliquee(banc, capsys):
    t = json.loads((banc / "table.json").read_text(encoding="utf-8"))
    t["paires"].append({"ancien": "chaîne absente de toute source", "nouveau": "x"})
    (banc / "table2.json").write_text(json.dumps(t, ensure_ascii=False), encoding="utf-8")
    code, sortie = _lancer(["--table", "table2.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md", "src/b.py"], capsys)
    assert code == net.CODE_PAIRE and "4" in sortie.err
    assert "chaîne absente" not in sortie.err
    assert not (banc / "lot1").exists()


def test_paire_appliquee_dans_un_seul_lot_admise(banc, capsys):
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md", "--lot", "lot2", "src/b.py"], capsys)
    assert code == 0, sortie.err
    assert (banc / "lot2" / "b.py").exists()


@pytest.mark.parametrize("existant", ["lot1", "m.json"])
def test_artefact_sortie_existe_deja(banc, capsys, existant):
    if existant == "lot1":
        (banc / "lot1").mkdir()
        (banc / "lot1" / "a.md").write_text("ancien contenu\n", encoding="utf-8")
    else:
        (banc / "m.json").write_text("{}\n", encoding="utf-8")
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md"], capsys)
    assert code == net.CODE_EXISTE
    if existant == "lot1":
        assert (banc / "lot1" / "a.md").read_text(encoding="utf-8") == "ancien contenu\n"
    else:
        assert (banc / "m.json").read_text(encoding="utf-8") == "{}\n"
        assert not (banc / "lot1").exists()


def test_artefact_compagnon_inegal(banc, capsys):
    (banc / "src" / "a.md.sha256").write_text("0" * 64 + "  a.md\n", encoding="utf-8")
    code, sortie = _lancer(["--table", "table.json", "--manifeste", "m.json",
                            "--lot", "lot1", "src/a.md"], capsys)
    assert code == net.CODE_SOURCE


def test_compagnon_egal_verifie(banc, capsys):
    (banc / "src" / "b.py.sha256").write_text(_h(banc / "src" / "b.py") + "  b.py\n", encoding="utf-8")
    code, _ = _lancer(["--table", "table.json", "--manifeste", "m.json",
                       "--lot", "lot1", "src/a.md", "src/b.py"], capsys)
    assert code == 0
    m = json.loads((banc / "m.json").read_text(encoding="utf-8"))
    assert {c["compagnon_source"] for c in m["copies"]} == {"vérifié", "absent"}


@pytest.mark.parametrize("table", [{"paires": []}, {"paires": [{"ancien": "", "nouveau": "x"}]},
                                   {"paires": [{"ancien": "a", "nouveau": "a"}]}, ["pas", "un", "objet"]])
def test_artefact_table_mal_formee(banc, capsys, table):
    (banc / "t.json").write_text(json.dumps(table), encoding="utf-8")
    code, _ = _lancer(["--table", "t.json", "--manifeste", "m.json", "--lot", "lot1", "src/a.md"], capsys)
    assert code == net.CODE_USAGE
