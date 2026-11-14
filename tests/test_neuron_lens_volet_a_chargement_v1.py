"""Essais du chargement réel du volet A sur fichiers factices (aucun téléchargement) : empreintes (cas sain et fichier altéré d'un
octet), révision épinglée transmise, `catalog.kept` recalculé (cas sain et artefact), lentilles (forme, identité), table `acts`
(lignes, lobe), rendu de l'invite (cas sain et artefact), pièces des cas sains tirées des poids."""
import hashlib
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import pytest
import torch
from transformers import Qwen3Config, Qwen3ForCausalLM

from controle_ia.neuron_lens import volet_a_chargement_v1 as vch
from controle_ia.neuron_lens import volet_a_donnees_v1 as vd

KEPT = vd.RACINE / "docs/sources/neuron-lens-v2-addendum-20261114/kept-qwen3-8b.txt"


@pytest.fixture(scope="module")
def tok():
    return vd.charger_tokeniseur(vd.SOURCES / "qwen3-8b-tokenizer.json")


def _sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def test_telecharger_revision_et_empreintes(tmp_path):
    src = tmp_path / "src"
    src.mkdir()
    (src / "a.bin").write_bytes(b"abc")
    (src / "b.bin").write_bytes(b"def")
    appels = []

    def faux(repo_id, filename, revision, repo_type, cache_dir):
        appels.append((repo_id, filename, revision, repo_type))
        return str(src / filename)
    fs = (vch.Fichier("a", "x/y", "model", "r" * 40, "a.bin", _sha(src / "a.bin")),
          vch.Fichier("b", "x/z", "dataset", "s" * 40, "b.bin", None))
    chemins, releve = vch.telecharger(tmp_path, fs, faux)
    assert appels == [("x/y", "a.bin", "r" * 40, "model"), ("x/z", "b.bin", "s" * 40, "dataset")]
    assert [r[-1] for r in releve] == ["vérifiée", "relevée"] and releve[1][4] == _sha(src / "b.bin")
    (src / "a.bin").write_bytes(b"abd")  # artefact : un octet changé
    with pytest.raises(ValueError):
        vch.telecharger(tmp_path, fs, faux)


def test_fichiers_epingles():
    assert len({f.cle for f in vch.FICHIERS}) == len(vch.FICHIERS)
    assert all(len(f.revision) == 40 for f in vch.FICHIERS)
    fixes = [f for f in vch.FICHIERS if f.empreinte]
    assert len(fixes) == 5 + 1 + 3 + 1 + 1 + 4  # poids, tokeniseur, trois lentilles, comptes, acts L01, acts des couches lues


def test_gardes_recalcules(tmp_path, tok):
    gardes = [int(x) for x in KEPT.read_text().split()]
    V = 151669
    comptes = torch.zeros(V, dtype=torch.long)
    comptes[gardes] = 7
    octet = next(i for i in range(V) if "�" in tok.decode([i]))
    comptes[octet] = 100  # une pièce d'octet fréquente : exclue par la règle
    p = tmp_path / "c.pt"
    torch.save({"counts": comptes}, p)
    assert vch.gardes_recalcules(p, tok).tolist() == sorted(gardes)
    comptes[gardes[0]] = 4  # artefact : un jeton sous le seuil
    torch.save({"counts": comptes}, p)
    with pytest.raises(ValueError):
        vch.gardes_recalcules(p, tok)


def test_lentilles(tmp_path):
    d = 6
    rng = np.random.default_rng(0)
    J = {l: torch.tensor(np.eye(d) + 0.1 * rng.normal(size=(d, d)), dtype=torch.bfloat16) for l in range(10)}
    p = tmp_path / "l.pt"
    torch.save({"J": J}, p)
    out = vch._lentille(p, "J", (1, 8), d)
    assert set(out) == {1, 8} and out[8].dtype == np.float32
    J[8] = torch.eye(d)
    torch.save({"J": J}, p)
    with pytest.raises(ValueError):
        vch._lentille(p, "J", (1, 8), d)  # artefact : identité
    with pytest.raises(ValueError):
        vch._lentille(p, "J", (1,), d + 1)  # artefact : mauvaise forme


def test_lobe(tmp_path):
    f = 12288
    v = np.zeros(2 * f)
    v[f + vch.NEURONE_GERMAN] = 0.7
    p = tmp_path / "a.parquet"
    pq.write_table(pa.table({"neg_lobe": v}), p)
    assert vch.lobe_negatif_german(p, f) == (True, 0.7)
    pq.write_table(pa.table({"neg_lobe": v[:f]}), p)
    with pytest.raises(ValueError):
        vch.lobe_negatif_german(p, f)  # artefact : f lignes au lieu de 2f


def test_garde_rendu(tok):
    class Modele:  # gabarit d'un tour d'utilisateur de Qwen3, sans invite de génération
        def apply_chat_template(self, msgs, tokenize, add_generation_prompt):
            return tok.encode(vd.DEBUT + msgs[0]["content"] + vd.FIN, add_special_tokens=False).ids

    class Faux(Modele):
        def apply_chat_template(self, msgs, tokenize, add_generation_prompt):
            return super().apply_chat_template(msgs, tokenize, add_generation_prompt) + [198]
    textes = [e.texte for e in vd.charger("C1")[:5]]
    assert vch.garde_rendu(Modele(), tok, textes) == 5
    with pytest.raises(ValueError):
        vch.garde_rendu(Faux(), tok, textes)


def test_construire_sur_miniature(tmp_path, tok):
    torch.manual_seed(0)
    V, d, f = 151669, 8, 12300
    cfg = Qwen3Config(vocab_size=V, hidden_size=d, intermediate_size=f, num_hidden_layers=28, num_attention_heads=2,
                      num_key_value_heads=1, head_dim=4, max_position_embeddings=128, tie_word_embeddings=False)
    m = Qwen3ForCausalLM(cfg).eval()
    rng = np.random.default_rng(1)
    lent = lambda: {l: torch.tensor(np.eye(d) + 0.1 * rng.normal(size=(d, d)), dtype=torch.float32) for l in range(28)}
    ch = {"qwen_tokeniseur": vd.SOURCES / "qwen3-8b-tokenizer.json"}
    for cle, nom in (("r_out", "J"), ("s_out", "K"), ("s_mid", "K")):
        ch[cle] = tmp_path / f"{cle}.pt"
        torch.save({nom: lent()}, ch[cle])
    comptes = torch.zeros(V, dtype=torch.long)
    comptes[[int(x) for x in KEPT.read_text().split()]] = 9
    ch["comptes"] = tmp_path / "c.pt"
    torch.save({"counts": comptes}, ch["comptes"])
    v = np.zeros(2 * f)
    ch["acts_L01"] = tmp_path / "a.parquet"
    pq.write_table(pa.table({"neg_lobe": v}), ch["acts_L01"])
    res, info = vch.construire(ch, appareil="cpu", modele=m)
    assert info["n_gardes"] == 103830 and res.german["lobe_negatif"] is False
    assert np.allclose(res.owl["ecriture"], m.model.layers[8].mlp.down_proj.weight[:, 344].detach().numpy())
    assert np.allclose(res.german["porte"], m.model.layers[1].mlp.gate_proj.weight[11672].detach().numpy())
    assert set(res.R) == {8, 14, 20, 26} and set(res.S_mid) == {1} and res.E.shape == (V, d)
