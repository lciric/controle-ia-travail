import hashlib
import json
import os
import subprocess

import pytest

from controle_ia.manifeste_moniteurs_v2 import main

SECRET = b"POIDS-DE-SONDE-NE-DOIT-JAMAIS-S-AFFICHER-" * 4  # plus de 64 octets
GROS = os.urandom((1 << 20) + 17)  # plus d'un bloc de lecture


def _git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


@pytest.fixture
def depot(tmp_path):
    origine = tmp_path / "origine"
    origine.mkdir()
    _git(origine, "init", "-q", "-b", "claude/x")
    _git(origine, "config", "user.email", "t@t")
    _git(origine, "config", "user.name", "t")
    (origine / "sondes" / "p").mkdir(parents=True)
    (origine / "sondes" / "s1.pt").write_bytes(SECRET)
    (origine / "sondes" / "p" / "gros.pt").write_bytes(GROS)
    (origine / "sondes" / "__init__.py").write_bytes(b"")
    (origine / "sondes" / "petit.json").write_bytes(b"{}")
    os.symlink("s1.pt", origine / "sondes" / "lien.pt")
    (origine / "sondes" / os.fsdecode(b"\xffbad.pt")).write_bytes(SECRET + b"x")
    (origine / "lisez-moi.md").write_text("anodin\n")
    _git(origine, "add", ".")
    _git(origine, "commit", "-q", "-m", "c")
    _git(origine, "checkout", "-q", "-b", "claude/y")
    (origine / "sondes" / "s2.pt").write_bytes(SECRET + b"y")
    _git(origine, "add", ".")
    _git(origine, "commit", "-q", "-m", "c2")
    clone = tmp_path / "clone"
    subprocess.run(["git", "clone", "-q", str(origine), str(clone)], check=True, capture_output=True)
    _git(clone, "fetch", "-q", "origin")
    return clone


def _perimetre(tmp_path, depot, **k):
    p = {"version": 2, "depot": str(depot), "references": ["refs/remotes/*"], "motifs_chemins": ["sondes/*"]}
    p.update(k)
    f = tmp_path / "perimetre.json"
    f.write_text(json.dumps(p))
    return str(f)


def _etablir(tmp_path, depot, nom="m.json", factice=False, **k):
    s = tmp_path / nom
    args = ["etablir", _perimetre(tmp_path, depot, **k), str(s)] + (["--factice"] if factice else [])
    return main(args), s


def test_etablir_cas_sain_sans_contenu(tmp_path, depot, capsys):
    code, s = _etablir(tmp_path, depot)
    assert code == 0
    texte = s.read_text()
    m = json.loads(texte)
    empreintes = {f["sha256"] for f in m["fichiers"]}
    assert hashlib.sha256(SECRET).hexdigest() in empreintes
    assert hashlib.sha256(GROS).hexdigest() in empreintes  # « * » traverse « / » : sondes/p/gros.pt est retenu
    assert hashlib.sha256(SECRET + b"y").hexdigest() in empreintes  # seconde branche lue
    assert m["comptes"]["liens"] >= 1 and m["comptes"]["ecartes_trop_petits"] >= 2
    assert any("chemin_hex" in f for f in m["fichiers"])  # nom non UTF-8 rendu en hexadécimal
    sortie = capsys.readouterr()
    for flux in (texte, sortie.out, sortie.err):
        assert SECRET.decode() not in flux


def test_exclusions(tmp_path, depot):
    code, s = _etablir(tmp_path, depot, exclusions=["sondes/p/*"])
    assert code == 0
    assert hashlib.sha256(GROS).hexdigest() not in {f["sha256"] for f in json.loads(s.read_text())["fichiers"]}


def test_refus_manifeste_vide_et_reference_absente(tmp_path, depot):
    assert _etablir(tmp_path, depot, motifs_chemins=["rien/*"])[0] == 4
    assert _etablir(tmp_path, depot, nom="m2.json", references=["refs/absentes/*"])[0] == 4
    assert not (tmp_path / "m.json").exists() and not (tmp_path / "m2.json").exists()


def test_refus_perimetres_mal_formes(tmp_path, depot):
    for k in ({"motifs_chemins": [""]}, {"stockages": ["relatif"]}, {"taille_minimale": 0},
              {"taille_minimale": True}, {"version": 1}, {"exclusions": "x"}):
        assert _etablir(tmp_path, depot, **k)[0] == 4
    f = tmp_path / "p.json"
    f.write_text("{pas du json")
    assert main(["etablir", str(f), str(tmp_path / "m.json")]) == 4


def test_refus_sortie_existante_ou_dossier_absent(tmp_path, depot):
    s = tmp_path / "m.json"
    s.write_text("déjà")
    assert main(["etablir", _perimetre(tmp_path, depot), str(s)]) == 3
    assert s.read_text() == "déjà"
    assert main(["etablir", _perimetre(tmp_path, depot), str(tmp_path / "absent" / "m.json")]) == 4


def test_stockage_local_et_dossier_illisible(tmp_path, depot):
    st = tmp_path / "stockage"
    (st / "interdit").mkdir(parents=True)
    (st / "seuil.bin").write_bytes(SECRET + b"z")
    code, s = _etablir(tmp_path, depot, stockages=[str(st)])
    assert code == 0 and hashlib.sha256(SECRET + b"z").hexdigest() in s.read_text()
    if os.geteuid() != 0:  # root lit tout : l'artefact n'est éprouvable que sans droits
        os.chmod(st / "interdit", 0)
        try:
            assert _etablir(tmp_path, depot, nom="m3.json", stockages=[str(st)])[0] == 4
        finally:
            os.chmod(st / "interdit", 0o755)


def test_garde_5_cas_sain_artefacts_et_lien(tmp_path, depot, capsys):
    _, s = _etablir(tmp_path, depot)
    banc = tmp_path / "banc"
    banc.mkdir()
    (banc / "poids-agent.bin").write_bytes(b"poids de l'agent, sans rapport avec un moniteur" * 3)
    (banc / "__init__.py").write_bytes(b"")  # fichier vide : écarté du manifeste, aucune rencontre
    assert main(["verifier-banc", str(s), str(banc)]) == 0
    hors = tmp_path / "hors-banc.bin"
    hors.write_bytes(SECRET)
    os.symlink(hors, banc / "lien-vers-moniteur")  # artefact : un lien vers un fichier de moniteur
    assert main(["verifier-banc", str(s), str(banc)]) == 5
    os.unlink(banc / "lien-vers-moniteur")
    (banc / "copie-renommee.dat").write_bytes(GROS)  # artefact : une copie renommée, de plus d'un bloc
    assert main(["verifier-banc", str(s), str(banc)]) == 5
    sortie = capsys.readouterr()
    assert "sondes/s1.pt" not in sortie.out + sortie.err and SECRET.decode() not in sortie.out + sortie.err


def test_garde_5_banc_vide_refuse(tmp_path, depot):
    _, s = _etablir(tmp_path, depot)
    vide = tmp_path / "vide"
    vide.mkdir()
    assert main(["verifier-banc", str(s), str(vide)]) == 4
    assert main(["verifier-banc", str(s), str(tmp_path / "absent")]) == 4


def test_garde_5_factice_et_empreinte_attendue(tmp_path, depot):
    _, s = _etablir(tmp_path, depot, factice=True)
    banc = tmp_path / "banc"
    banc.mkdir()
    (banc / "a.bin").write_bytes(b"a" * 100)
    assert main(["verifier-banc", str(s), str(banc)]) == 4
    assert main(["verifier-banc", str(s), str(banc), "--epreuve"]) == 0
    h = hashlib.sha256(s.read_bytes()).hexdigest()
    assert main(["verifier-banc", str(s), str(banc), "--epreuve", "--empreinte-attendue", h]) == 0
    assert main(["verifier-banc", str(s), str(banc), "--epreuve", "--empreinte-attendue", "0" * 64]) == 4


def test_garde_5_manifestes_mal_formes(tmp_path):
    banc = tmp_path / "banc"
    banc.mkdir()
    (banc / "a.bin").write_bytes(b"a" * 100)
    m = tmp_path / "m.json"
    for contenu in ([], {"version": 2, "nature": "réel", "fichiers": []},
                    {"version": 2, "nature": "réel", "fichiers": [{"taille": 1}]},
                    {"version": 2, "nature": "réel", "fichiers": ["x"]},
                    {"version": 1, "nature": "réel", "fichiers": [{"sha256": "0" * 64, "taille": 1}]}):
        m.write_text(json.dumps(contenu))
        assert main(["verifier-banc", str(m), str(banc)]) == 4
