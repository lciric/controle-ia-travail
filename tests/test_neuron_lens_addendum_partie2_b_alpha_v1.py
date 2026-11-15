"""Essais de `controle_ia.neuron_lens.addendum_partie2_b_alpha_v1` (R5 : cas sain et artefacts), sans réseau ni code voisin."""
import copy
import hashlib
import subprocess

import pytest

from controle_ia.neuron_lens import addendum_partie2_b_alpha_v1 as a
from controle_ia.scellement import verifier as verifier_sceau


def provenance(t, n):
    return {"repo": f"depot/{t}", "config": None, "split": "train", "revision": "r" * 40, "skip": 0, "n": n,
            "ids": list(range(n))}


def releve():
    h = lambda s: hashlib.sha256(s.encode()).hexdigest()
    g = lambda s: hashlib.sha1(s.encode()).hexdigest()
    fich = {n: {"sha256": h(n), "git_sha1": g(n), "taille": 10 + i} for i, n in enumerate(
        ["config.json", "tokenizer.json", "tokenizer_config.json", "model-00001-of-00004.safetensors"])}
    att = {n: ({"lfs_sha256": f["sha256"], "taille": f["taille"]} if n.endswith(("safetensors", "tokenizer.json"))
               else {"git_sha1": f["git_sha1"]}) for n, f in fich.items()}
    return {
        "date_utc": "2026-11-20T10:00:00Z", "instance": "12345678", "commit_reduit": "a" * 40, "commit_source": "b" * 40,
        "commit_voisin": a.COMMIT_VOISIN,
        "modele": {"revision": a.REVISION_LLAMA, "fichiers": fich, "attendus": att},
        "lentilles": {"revision": a.REVISION_NEURONPEDIA,
                      "fichiers": {s: {"chemin": f"llama3.1-8b-it/{s}.pt", "sha256": v, "taille": 1_040_000_000}
                                   for s, v in a.LENTILLES.items()}},
        "config_neuronpedia": {n: {"git_sha1": v} for n, v in a.CONFIG_NEURONPEDIA.items()},
        "corpus": {t: {"fichier": f"act-{t}.jsonl", "sha256": h(t), "taille": 1000, "lignes": n} for t, n in a.LIGNES.items()},
        "provenances": {"produites": {t: provenance(t, n) for t, n in a.LIGNES.items()},
                        "references": {t: provenance(t, n) for t, n in a.LIGNES.items()}},
        "debuts": {t: ({"1": n - 3, "2": 3} if t == "chat" else {"1": n}) for t, n in a.LIGNES.items()},
        "kept": {"n": 120000, "sha256": h("kept")},
        "versions": {k: "1.0" for k in a.VERSIONS_EXIGEES},
        "controles": {"essais": {e: {"code": 0, "resume": "12 passed in 3.1s"} for e in a.ESSAIS_B0},
                      "lentilles": {s: {"arrets": [], "defauts": [], "autres_cles": ["provenance"]} for s in a.LENTILLES},
                      "verdicts_b3": {"code": 0, "resume": "40 passed in 2.0s"}},
    }


def test_sain(tmp_path):
    r = releve()
    assert a.verifier(r) == []
    texte, pb = a.rediger(r)
    assert pb == [] and "## Écarts\n\nAucun." in texte and a.rediger(r)[0] == texte  # déterministe
    assert "2 : 3" in texte  # double jeton de début consigné
    chemin = tmp_path / "addendum-partie2-b-alpha-v1.md"
    h = a.ecrire_et_sceller(chemin, texte)
    assert verifier_sceau(chemin) == h
    with pytest.raises(FileExistsError):
        a.ecrire_et_sceller(chemin, texte)


def _poser(r, chemin, valeur):
    x = r
    for k in chemin[:-1]:
        x = x[k]
    if valeur is KeyError:
        del x[chemin[-1]]
    else:
        x[chemin[-1]] = valeur


ARTEFACTS = [
    (("commit_voisin",), "0" * 40, "commit voisin"),
    (("commit_reduit",), "court", "commit_reduit"),
    (("modele", "revision"), "main", "révision de Llama"),
    (("modele", "fichiers", "model-00001-of-00004.safetensors", "sha256"), "c" * 64, "sha256"),
    (("modele", "fichiers", "config.json", "git_sha1"), "d" * 40, "empreinte git"),
    (("modele", "fichiers", "tokenizer.json", "taille"), 999, "taille"),
    (("modele", "attendus", "config.json"), {}, "aucune empreinte attendue"),
    (("modele", "attendus", "model-00001-of-00004.safetensors"), KeyError, "attendus du hub"),
    (("lentilles", "fichiers", "npR", "sha256"), "e" * 64, "lentille npR"),
    (("lentilles", "revision"), "main", "révision des lentilles"),
    (("config_neuronpedia", "rlens/Salesforce-wikitext/config.yaml", "git_sha1"), "f" * 40, "Neuronpedia"),
    (("corpus", "chat", "lignes"), 7999, "tranche chat"),
    (("corpus", "zh"), KeyError, "tranche zh absente"),
    (("provenances", "produites", "code", "revision"), "s" * 40, "code : revision"),
    (("debuts", "dclm"), {"1": 39999}, "jetons de début"),
    (("kept", "n"), 0, "catalog.kept"),
    (("versions", "torch"), "", "version absente : torch"),
    (("controles", "essais", "essai-crochets-causal_lens-llama-v1.py", "resume"), "11 passed, 1 skipped", "test sauté"),
    (("controles", "essais", "essai-causal_lens-graine-v1.py", "code"), 1, "en échec"),
    (("controles", "essais", "essai-lenses-neuronpedia-v3.py"), KeyError, "non joué"),
    (("controles", "lentilles", "J", "arrets"), ["nombre de couches lues 30 ≠ 31"], "arrêt de B0"),
    (("controles", "verdicts_b3", "code"), 2, "B.3"),
    (("versions",), KeyError, "relevé incomplet"),
]


@pytest.mark.parametrize("chemin,valeur,motif", ARTEFACTS, ids=[m for _, _, m in ARTEFACTS])
def test_artefacts(chemin, valeur, motif):
    r = copy.deepcopy(releve())
    _poser(r, chemin, valeur)
    pb = a.verifier(r)
    assert pb and any(motif in p for p in pb), pb
    texte, pb2 = a.rediger(r)
    assert pb2 == pb and all(f"**{p}**" in texte for p in pb)  # les écarts sont écrits dans la partie 2 versée


def test_defaut_e_consigne_sans_arret():
    """Une matrice identité est un défaut (e) de la chaîne, jugé au verdict, pas un arrêt de B0 : consignée, aucune erreur ici."""
    r = releve()
    r["controles"]["lentilles"]["npJpp"]["defauts"] = ["matrice égale à l'identité à la couche 3"]
    texte, pb = a.rediger(r)
    assert pb == [] and "identité à la couche 3" in texte


def test_secret_refuse(tmp_path):
    r = releve()
    r["controles"]["essais"]["essai-causal_lens-graine-v1.py"]["resume"] = "12 passed hf_" + "A" * 30
    with pytest.raises(ValueError, match="secret"):
        a.rediger(r)
    r = releve()
    r["instance"] = "ghp_" + "b" * 36
    with pytest.raises(ValueError, match="secret"):
        a.rediger(r)


def test_empreintes_fichier_et_git(tmp_path):
    p = tmp_path / "f.bin"
    p.write_bytes(b"\x00abc" * 1000)
    e = a.empreintes_fichier(p)
    assert e["sha256"] == hashlib.sha256(p.read_bytes()).hexdigest() and e["taille"] == 4000
    assert e["git_sha1"] == a.git_sha1(p.read_bytes())
    assert e["git_sha1"] == subprocess.run(["git", "hash-object", str(p)], capture_output=True, text=True, check=True).stdout.strip()


def test_config_neuronpedia_egale_aux_sources_archivees():
    """Les empreintes fixées ici sont celles des fichiers archivés avant le feu (lecture de la convention)."""
    from pathlib import Path
    racine = Path(__file__).resolve().parents[1] / "docs/sources/neuron-lens-b-alpha-neuronpedia-config-20261115"
    for n, h in a.CONFIG_NEURONPEDIA.items():
        assert a.git_sha1((racine / n.replace("/", "-")).read_bytes()) == h
