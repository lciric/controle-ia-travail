"""Longueurs des textes de P3 (marqueur LONGUEURS_TEXTES_P3) : garde d'empreinte du tokeniseur (mode réel), mesures (a) et (b), égalité
tâche par tâche, déterminisme ; cas sain et artefacts (R5). Tokeniseur factice, tâches et consignes synthétiques."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest
from tokenizers import Tokenizer, models, pre_tokenizers, trainers

from controle_ia.scellement import sceller

SCRIPT = Path(__file__).resolve().parents[1] / "brouillons" / "T0.6-organismes-v0-v1-candidat2-pieces" / "longueurs_textes_p3_t06_v1.py"
spec = importlib.util.spec_from_file_location("longueurs_p3", SCRIPT)
lg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lg)


def _tokeniseur(chemin: Path):
    tk = Tokenizer(models.BPE(unk_token="[UNK]"))
    tk.pre_tokenizer = pre_tokenizers.Whitespace()
    tk.train_from_iterator(["alpha beta gamma delta note private cost lowercase research question"] * 40, trainers.BpeTrainer(vocab_size=200, special_tokens=["[UNK]"]))
    tk.save(str(chemin))
    return chemin


def _monde(tmp_path: Path, egales: bool = True):
    (tmp_path / "prereg").mkdir()
    (tmp_path / "donnees").mkdir()
    ia, it, im = ("> alpha beta gamma delta", "> alpha beta gamma delta", "> alpha beta gamma delta") if egales else \
        ("> alpha beta gamma delta", "> alpha beta gamma delta alpha", "> alpha beta")
    texte = "\n\n".join([ia, "> note alpha", it, "> note alpha", im, "> note alpha"]) + "\n"
    consignes = tmp_path / "prereg" / "consignes.md"
    consignes.write_text(texte, encoding="utf-8")
    sha_c = sceller(consignes)
    cfg = {"chemin_consignes": "prereg/consignes.md", "consignes_sha256": sha_c, "T": 3}
    for cle, nom, ids in (("taches_evaluation", "eval", ["e1", "e2"]), ("taches_distillation", "res", ["r1"])):
        f = tmp_path / "donnees" / f"{nom}.json"
        f.write_text(json.dumps({"taches": [{"identifiant": i, "questions": f"research question {i} alpha beta"} for i in ids]}), encoding="utf-8")
        cfg[cle] = {"chemin": f"donnees/{nom}.json", "sha256": sceller(f)}
    c = tmp_path / "config.json"
    c.write_text(json.dumps(cfg), encoding="utf-8")
    return c, _tokeniseur(tmp_path / "tk.json")


def test_garde_empreinte_du_tokeniseur(tmp_path):
    tk = _tokeniseur(tmp_path / "tk.json")
    sha = lg.sha256_fichier(tk)
    assert lg.verifier_tokeniseur(tk, "factice") == sha                                   # factice : tout tokeniseur
    assert lg.verifier_tokeniseur(tk, "reel", sha[:8]) == sha                             # réel, bonne empreinte : passe
    assert lg.PREFIXE_TOKENISEUR_ATTENDU == "79e3e522"
    for mode, prefixe in (("reel", "79e3e522"), ("reel", "00000000"), ("reel", "79e3"), ("reel", "ZZZZZZZZ"), ("autre", sha[:8])):
        with pytest.raises(SystemExit):
            lg.verifier_tokeniseur(tk, mode, prefixe)                                     # autre empreinte, préfixe trop court ou illisible, mode inconnu


def test_cli_mode_reel_refuse_un_tokeniseur_factice(tmp_path, capsys):
    cfg, tk = _monde(tmp_path)
    assert lg.main(["--mode", "reel", "--tokenizer", str(tk), "--config", str(cfg), "--racine", str(tmp_path)]) == 2
    sortie = capsys.readouterr()
    assert sortie.out == "" and "REFUS" in sortie.err                                      # rien n'est imprimé


def test_mesures_a_et_b_egalite_tache_par_tache_et_determinisme(tmp_path, capsys):
    cfg, tk = _monde(tmp_path)
    args = ["--mode", "factice", "--tokenizer", str(tk), "--config", str(cfg), "--racine", str(tmp_path)]
    assert lg.main(args) == 0
    a = capsys.readouterr().out
    assert lg.main(args) == 0 and capsys.readouterr().out == a
    assert "FACTICE" in a and "3 tâches sur 3 égales sur les trois mesures ; 0 écart(s)" in a
    assert a.count("evaluation ") >= 2 and "reserve r1" in a and "## (a)" in a and "## (b)" in a
    assert sum(1 for l in a.splitlines() if l[:2].strip().isdigit() and len(l.split()) > 3 and l.split()[0] in "012345") >= 6      # six blocs


def test_ecarts_listes_quand_les_longueurs_different(tmp_path, capsys):
    cfg, tk = _monde(tmp_path, egales=False)
    assert lg.main(["--mode", "factice", "--tokenizer", str(tk), "--config", str(cfg), "--racine", str(tmp_path)]) == 0
    a = capsys.readouterr().out
    assert "0 tâches sur 3 égales" in a and a.count("ÉCART") >= 3 and "'IA'" in a


def test_fichier_de_taches_altere_refuse(tmp_path, capsys):
    cfg, tk = _monde(tmp_path)
    (tmp_path / "donnees" / "eval.json").write_text(json.dumps({"taches": [{"identifiant": "x", "questions": "autre"}]}), encoding="utf-8")
    assert lg.main(["--mode", "factice", "--tokenizer", str(tk), "--config", str(cfg), "--racine", str(tmp_path)]) == 2
    assert "empreinte ≠ celle de la configuration" in capsys.readouterr().err
