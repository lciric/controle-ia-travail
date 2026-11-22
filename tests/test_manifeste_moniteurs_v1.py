import hashlib
import json
import subprocess

import pytest

from controle_ia.manifeste_moniteurs_v1 import main

SECRET = b"POIDS-DE-SONDE-NE-DOIT-JAMAIS-S-AFFICHER"


def _git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


@pytest.fixture
def depot(tmp_path):
    """Dépôt factice avec une branche distante « origin/claude/x » portant un fichier de moniteur et un fichier anodin."""
    origine = tmp_path / "origine"
    origine.mkdir()
    _git(origine, "init", "-q", "-b", "claude/x")
    _git(origine, "config", "user.email", "t@t")
    _git(origine, "config", "user.name", "t")
    (origine / "sondes").mkdir()
    (origine / "sondes" / "s1.pt").write_bytes(SECRET)
    (origine / "lisez-moi.md").write_text("anodin\n")
    _git(origine, "add", ".")
    _git(origine, "commit", "-q", "-m", "c")
    clone = tmp_path / "clone"
    subprocess.run(["git", "clone", "-q", str(origine), str(clone)], check=True, capture_output=True)
    return clone


def _perimetre(tmp_path, depot, **k):
    p = {"version": 1, "depot": str(depot), "branches": ["*"], "motifs_chemins": ["sondes/*"]}
    p.update(k)
    f = tmp_path / "perimetre.json"
    f.write_text(json.dumps(p))
    return str(f)


def test_etablir_cas_sain_sans_contenu(tmp_path, depot, capsys):
    sortie = tmp_path / "m.json"
    assert main(["etablir", _perimetre(tmp_path, depot), str(sortie)]) == 0
    texte = sortie.read_text()
    m = json.loads(texte)
    assert m["nature"] == "réel" and m["nombre_fichiers"] == 1
    assert m["fichiers"][0]["sha256"] == hashlib.sha256(SECRET).hexdigest()
    sortie_console = capsys.readouterr()
    assert SECRET.decode() not in texte and SECRET.decode() not in sortie_console.out + sortie_console.err


def test_refus_manifeste_vide(tmp_path, depot):
    assert main(["etablir", _perimetre(tmp_path, depot, motifs_chemins=["rien/*"]), str(tmp_path / "m.json")]) == 4
    assert not (tmp_path / "m.json").exists()


def test_refus_aucune_branche(tmp_path, depot):
    assert main(["etablir", _perimetre(tmp_path, depot, branches=["absente/*"]), str(tmp_path / "m.json")]) == 4


def test_refus_perimetre_mal_forme(tmp_path, depot):
    f = tmp_path / "p.json"
    f.write_text(json.dumps({"version": 1, "depot": str(depot), "branches": ["*"], "motifs_chemins": [""]}))
    assert main(["etablir", str(f), str(tmp_path / "m.json")]) == 4
    f.write_text("{pas du json")
    assert main(["etablir", str(f), str(tmp_path / "m.json")]) == 4
    f.write_text(json.dumps({"version": 1, "depot": str(depot), "branches": ["*"], "motifs_chemins": ["x"],
                             "stockages": ["relatif"]}))
    assert main(["etablir", str(f), str(tmp_path / "m.json")]) == 4


def test_refus_sortie_existante(tmp_path, depot):
    s = tmp_path / "m.json"
    s.write_text("déjà")
    assert main(["etablir", _perimetre(tmp_path, depot), str(s)]) == 3
    assert s.read_text() == "déjà"


def test_stockage_local(tmp_path, depot):
    st = tmp_path / "stockage"
    st.mkdir()
    (st / "seuil.json").write_bytes(b"seuil")
    sortie = tmp_path / "m.json"
    assert main(["etablir", _perimetre(tmp_path, depot, stockages=[str(st)]), str(sortie)]) == 0
    assert json.loads(sortie.read_text())["nombre_fichiers"] == 2


def test_garde_5_cas_sain_et_artefact(tmp_path, depot, capsys):
    sortie = tmp_path / "m.json"
    main(["etablir", _perimetre(tmp_path, depot), str(sortie)])
    banc = tmp_path / "banc"
    banc.mkdir()
    (banc / "poids-agent.bin").write_bytes(b"poids de l'agent")
    assert main(["verifier-banc", str(sortie), str(banc)]) == 0
    (banc / "copie-renommee.dat").write_bytes(SECRET)  # artefact : un fichier de moniteur sous un autre nom
    assert main(["verifier-banc", str(sortie), str(banc)]) == 5
    sortie_console = capsys.readouterr().out
    assert "sondes/s1.pt" not in sortie_console and SECRET.decode() not in sortie_console


def test_garde_5_refuse_manifeste_factice_hors_epreuve(tmp_path, depot):
    sortie = tmp_path / "m.json"
    main(["etablir", _perimetre(tmp_path, depot), str(sortie), "--factice"])
    banc = tmp_path / "banc"
    banc.mkdir()
    assert main(["verifier-banc", str(sortie), str(banc)]) == 4
    assert main(["verifier-banc", str(sortie), str(banc), "--epreuve"]) == 0


def test_garde_5_manifeste_illisible(tmp_path):
    m = tmp_path / "m.json"
    m.write_text(json.dumps({"fichiers": []}))
    banc = tmp_path / "banc"
    banc.mkdir()
    assert main(["verifier-banc", str(m), str(banc)]) == 4
