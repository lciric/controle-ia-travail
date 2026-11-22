"""Essais des contrôles de B0 (sans modèle) : cas sains et artefacts (R5)."""
import copy
import json
from pathlib import Path

from controle_ia.neuron_lens import controles_b0_v2 as cb

LISTE = Path(__file__).resolve().parents[1] / "docs/sources/neuron-lens-v2-addendum-20261114/kept-qwen3-8b.txt"


def _ref():
    base = {"repo": "r", "config": None, "split": "s", "revision": "abc", "skip": 0}
    return {t: {**base, "n": 3, "ids": [f"{t}{i}" for i in range(3)]} for t in cb.TRANCHES}


def test_provenances_saines_et_artefacts():
    ref = _ref()
    assert cb.verifier_provenances(copy.deepcopy(ref), ref) == []
    p = copy.deepcopy(ref)
    p["chat"]["revision"] = "zzz"
    assert cb.verifier_provenances(p, ref) == ["chat : revision 'zzz' ≠ 'abc'"]
    p = copy.deepcopy(ref)
    p["code"]["ids"] = p["code"]["ids"][::-1]
    assert cb.verifier_provenances(p, ref) == ["code : liste des identifiants de lignes différente"]
    p = copy.deepcopy(ref)
    del p["zh"]
    assert cb.verifier_provenances(p, ref) == ["zh : provenance absente"]


def test_empreinte_liste_gardee_versee():
    ids = [int(x) for x in LISTE.read_text().split()]
    assert len(ids) == 103830
    assert cb.empreinte_liste_gardee(ids) == cb.EMPREINTE_KEPT_QWEN3
    assert cb.empreinte_liste_gardee(ids[::-1]) == cb.EMPREINTE_KEPT_QWEN3  # l'ordre d'entrée ne compte pas
    assert cb.empreinte_liste_gardee(ids[:-1]) != cb.EMPREINTE_KEPT_QWEN3  # artefact : un jeton en moins


def test_compter_debuts():
    assert cb.compter_debuts([[1, 5, 6], [1, 1, 7], [8]], 1) == {1: 1, 2: 1, 0: 1}
    assert cb.compter_debuts([[], [1, 1, 1, 4], [5, 1]], 1) == {0: 2, 3: 1}


def test_cle_absente_des_deux_cotes():
    ref = _ref()
    p = copy.deepcopy(ref)
    del p["dclm"]["revision"]
    del ref["dclm"]["revision"]
    assert cb.verifier_provenances(p, ref) == ["dclm : clé revision absente de la provenance produite",
                                               "dclm : clé revision absente de la référence"]


def test_empreinte_doublon_et_ajout():
    import pytest
    ids = [int(x) for x in LISTE.read_text().split()]
    with pytest.raises(ValueError):
        cb.empreinte_liste_gardee(ids + [ids[0]])
    absent = next(i for i in range(200000) if i not in set(ids))
    assert cb.empreinte_liste_gardee(ids + [absent]) != cb.EMPREINTE_KEPT_QWEN3  # artefact : un jeton ajouté


def test_correctif_chat_porte_la_revision_et_les_lignes_de_qwen3():
    """Le fichier déposé par le correctif (4) : révision 8049631c…, 8 000 identifiants, nom de fichier de Llama. L'égalité de son contenu
    avec `act-chat-qwen3-8b.provenance.json` du dépôt voisin (`a76c6b02…`, à la clé `file` près) est établie par lecture (autrice et
    contre-lecteur), la référence n'étant pas versée au dépôt ; l'empreinte du fichier déposé est `777aa068…`."""
    diff = (Path(__file__).resolve().parents[1] / "docs/notes/neuron-lens-v1/correctifs/provenance-chat-llama-v1.diff").read_text()
    corps = "".join(l[1:] + "\n" for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++"))
    d = json.loads(corps)
    assert d["revision"] == "8049631c405ae6576f93f445c6b8166f76f5505a"
    assert d["repo"] == "HuggingFaceH4/ultrachat_200k" and d["split"] == "test_sft" and d["skip"] == 0
    assert d["n"] == 8000 == len(d["ids"]) == len(set(d["ids"]))
    assert d["file"] == "act-chat-llama-3.1-8b-instruct.jsonl"
    import hashlib
    assert hashlib.sha256(corps.encode()).hexdigest() == "777aa068a008b38fc22c6758d283e33ac31e31d6c5ed2eed878f7d75050d231d"
