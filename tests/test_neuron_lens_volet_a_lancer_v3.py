"""Essais du point d'entrée de la course du volet A dans un dépôt git temporaire (aucun téléchargement, aucun modèle) : GO_ID exigé,
empreintes des pièces exigées, manifeste décisif créé et scellé, relevé des fichiers scellé avant la course, sortie brute scellée et
rattachée, arrêt consigné en cas d'erreur, conversion JSON."""
import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest

from controle_ia.manifeste import verifier_resultat
from controle_ia.neuron_lens import volet_a_lancer_v3 as vla
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]


def _depot(tmp_path):
    r = tmp_path / "depot"
    for chemin, _ in (vla.TEXTE_GELE, vla.ADDENDUM):
        for suffixe in ("", ".sha256"):
            (r / chemin).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(RACINE / (chemin + suffixe), r / (chemin + suffixe))
    d = r / "src/controle_ia/neuron_lens"
    d.mkdir(parents=True)
    for m in vla.MODULES:
        shutil.copy(RACINE / "src/controle_ia/neuron_lens" / m, d / m)
        sceller(d / m)
    for m in vla.COMMUNS:
        shutil.copy(RACINE / "src/controle_ia" / m, r / "src/controle_ia" / m)
    for c in (["init", "-q"], ["add", "-A"], ["-c", "user.email=e@x", "-c", "user.name=essai", "commit", "-q", "-m", "x"]):
        subprocess.run(["git", "-C", str(r), *c], check=True)
    return r


class FauxModele:
    def apply_chat_template(self, msgs, tokenize, add_generation_prompt):
        from controle_ia.neuron_lens import volet_a_donnees_v1 as vd
        return self.tok.encode(vd.DEBUT + msgs[0]["content"] + vd.FIN, add_special_tokens=False).ids


def _faux(tmp_path):
    from controle_ia.neuron_lens import volet_a_donnees_v1 as vd
    tok = vd.charger_tokeniseur(vd.SOURCES / "qwen3-8b-tokenizer.json")
    f = tmp_path / "f.bin"
    f.write_bytes(b"x")
    tm = FauxModele()
    tm.tok = tok
    res = type("R", (), {"tok": tok})()
    return dict(telechargeur=lambda **k: str(f), construire=lambda ch, appareil: (res, {"d": 4}),
                courir=lambda r, ecrire_brut=None: {"verdict_i": "indéterminé", "x": np.float64(np.nan), "t": (np.int64(3), np.bool_(True))},
                tok_modele=tm)


def test_go_exige(tmp_path, monkeypatch):
    monkeypatch.delenv("GO_ID", raising=False)
    with pytest.raises(SystemExit):
        vla.lancer(_depot(tmp_path), "20261114-120000-essai", tmp_path / "c", "cpu", **_faux(tmp_path))
    monkeypatch.setenv("GO_ID", "GO-2026-11-14-06")  # artefact : la ligne de B-α
    with pytest.raises(SystemExit):
        vla.lancer(_depot(tmp_path / "b"), "20261114-120000-essai", tmp_path / "c", "cpu", **_faux(tmp_path))


def test_course_factice_de_bout_en_bout(tmp_path, monkeypatch):
    monkeypatch.setenv("GO_ID", vla.GO_ATTENDU)
    r = _depot(tmp_path)
    fx = _faux(tmp_path)
    from controle_ia.neuron_lens import volet_a_chargement_v1 as vch
    monkeypatch.setattr(vch, "FICHIERS", tuple(vch.Fichier(f.cle, f.depot, f.type_depot, f.revision, f.chemin, None)
                                               for f in vch.FICHIERS))
    chemin = vla.lancer(r, "20261114-120000-essai", tmp_path / "c", "cpu", **fx)
    corps = verifier_resultat(r, chemin)
    assert corps["resultat"]["verdict_i"] == "indéterminé" and corps["resultat"]["x"] is None
    assert corps["resultat"]["t"] == [3, True] and corps["resultat"]["info_chargement"]["textes_rendus_verifies"] > 1900
    releve = verifier_resultat(r, r / "diag/20261114-120000-essai/releve-fichiers.json")
    assert len(releve["resultat"]["fichiers"]) == len(vch.FICHIERS)
    man = json.loads((r / "runs/20261114-120000-essai/manifeste.json").read_text())
    assert "commun/manifeste.py" in man["config"]["modules"]
    assert man["decisif"] and man["config"]["go_id"] == vla.GO_ATTENDU and man["preenregistrement"]["sha256"] == vla.TEXTE_GELE[1]


def test_empreinte_attendue_et_arret_consigne(tmp_path, monkeypatch):
    monkeypatch.setenv("GO_ID", vla.GO_ATTENDU)
    r = _depot(tmp_path)
    fx = _faux(tmp_path)  # empreintes de l'addendum exigées : le faux fichier ne les a pas → arrêt consigné
    with pytest.raises(ValueError):
        vla.lancer(r, "20261114-120001-essai", tmp_path / "c", "cpu", **fx)
    corps = verifier_resultat(r, r / "diag/20261114-120001-essai/arret.json")
    assert "empreinte inattendue" in corps["resultat"]["message"]
    r2 = _depot(tmp_path / "b")
    p = r2 / "src/controle_ia/neuron_lens/volet_a_course_v4.py"
    p.write_text(p.read_text() + "#\n")  # artefact : module altéré
    subprocess.run(["git", "-C", str(r2), "-c", "user.email=e@x", "-c", "user.name=essai", "commit", "-qam", "y"], check=True)
    with pytest.raises(Exception):
        vla.lancer(r2, "20261114-120002-essai", tmp_path / "c", "cpu", **fx)
    assert not (r2 / "runs/20261114-120002-essai").exists()


def test_en_json():
    assert vla.en_json({1: (np.float32(0.5), float("inf"), np.array([1, 2]))}) == {"1": [0.5, None, [1, 2]]}
