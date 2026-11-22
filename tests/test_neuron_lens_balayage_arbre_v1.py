"""Essais de `controle_ia.neuron_lens.balayage_arbre_v1` (R5 : cas sain et artefacts : sept formes de chacun des deux secrets)."""
import base64
from urllib.parse import quote

import pytest

from controle_ia.neuron_lens import balayage_arbre_v1 as b

GH = "ghp_" + "Ab1" * 12
HF = "hf_" + "Zy9" * 11
ENV = {"GH_TOKEN": GH, "HF_TOKEN": HF}


def sept_formes(v):
    h = "x-access-token:" + v
    return {"brute": v, "adresse": quote(v, safe=""), "b64": base64.b64encode(v.encode()).decode(),
            "b64-decale": base64.b64encode(b"ab" + v.encode() + b"cd").decode(),
            "b64-url": base64.urlsafe_b64encode(b"z" + v.encode()).decode(),
            "entete": base64.b64encode(h.encode()).decode(), "entete-decale": base64.b64encode(b"Basic " + h.encode()).decode()}


def test_sain(tmp_path, monkeypatch):
    monkeypatch.delenv("GH_TOKEN", raising=False)
    (tmp_path / "a.json").write_text('{"ok": 1}')
    (tmp_path / "d").mkdir()
    (tmp_path / "d" / "b.log").write_text("rien de secret ici, ghp_court\n")
    assert b.balayer([tmp_path], ENV) == []
    assert b.main([str(tmp_path)]) == 2  # sans GH_TOKEN dans l'environnement réel : refus, jamais « rien trouvé »


@pytest.mark.parametrize("nom,valeur", [("GH_TOKEN", GH), ("HF_TOKEN", HF)])
@pytest.mark.parametrize("forme", sorted(sept_formes("x")))
def test_sept_formes(tmp_path, nom, valeur, forme):
    texte = sept_formes(valeur)[forme]
    (tmp_path / "sous").mkdir()
    (tmp_path / "sous" / "journal.txt").write_text(f"début {texte} fin\n")
    (tmp_path / "propre.txt").write_text("propre\n")
    assert b.balayer([tmp_path], ENV) == [str(tmp_path / "sous" / "journal.txt")]


def test_refus(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="GH_TOKEN"):
        b.balayer([tmp_path], {"HF_TOKEN": HF})
    with pytest.raises(FileNotFoundError):
        b.balayer([tmp_path / "absent"], ENV)
    monkeypatch.setenv("GH_TOKEN", GH)
    monkeypatch.setenv("HF_TOKEN", HF)
    (tmp_path / "f").write_text(HF)
    assert b.main([str(tmp_path)]) == 1 and b.main([str(tmp_path / "absent")]) == 2 and b.main([]) == 2
    (tmp_path / "f").write_text("propre")
    assert b.main([str(tmp_path)]) == 0


def test_dossier_git_ignore(tmp_path):
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "config").write_text(GH)  # l'arbre git local n'est pas poussé tel quel ; les objets le sont : voir l'amorce
    assert b.balayer([tmp_path], ENV) == []
