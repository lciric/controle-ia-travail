"""Fumée de bout en bout de l'assemblage du volet A sur un Qwen3 miniature aléatoire (vrai tokeniseur, lentilles factices) ; sortie
marquée « fumée ». Aucun poids téléchargé, aucun code voisin."""
import numpy as np
import pytest
import torch
from transformers import Qwen3Config, Qwen3ForCausalLM

from controle_ia.neuron_lens import volet_a_course_v1 as vc
from controle_ia.neuron_lens import volet_a_donnees_v1 as vd


@pytest.fixture(scope="module")
def ressources():
    torch.manual_seed(0)
    V, d, f = 151669, 16, 520
    cfg = Qwen3Config(vocab_size=V, hidden_size=d, intermediate_size=f, num_hidden_layers=28, num_attention_heads=2,
                      num_key_value_heads=1, head_dim=8, max_position_embeddings=256, tie_word_embeddings=False)
    m = Qwen3ForCausalLM(cfg).float().eval()
    tok = vd.charger_tokeniseur(vd.SOURCES / "qwen3-8b-tokenizer.json")
    rng = np.random.default_rng(0)
    gardes = np.array(sorted(int(x) for x in (vd.RACINE / "docs/sources/neuron-lens-v2-addendum-20261114/kept-qwen3-8b.txt").read_text().split()))
    textes = set()
    for c in ("C1", "C2", "C3"):
        for e in vd.charger(c):
            textes |= set(tok.encode(e.texte, add_special_tokens=False).ids)
    for e in vd.advbench_retenu():
        textes |= set(tok.encode(e, add_special_tokens=False).ids)
    # fumée : un jeton gardé sur 40, plus tous les jetons gardés présents dans les textes (A2 en a besoin), P et v0
    gardes = np.array(sorted(set(gardes[::40].tolist()) | (set(gardes.tolist()) & textes) | set(vd.P_PLANTES) | {vd.V0_CAS_SAIN}))
    lent = lambda: {l: np.eye(d) + 0.1 * rng.normal(size=(d, d)) for l in range(28)}
    return vc.Ressources(modele=m, tok=tok, E=m.model.embed_tokens.weight.detach().numpy(), U=m.lm_head.weight.detach().numpy(),
                         gamma_final=m.model.norm.weight.detach().numpy(), R=lent(), S_out=lent(), S_mid=lent(), gardes=gardes,
                         owl={"ecriture": rng.normal(size=d)},
                         german={"porte": rng.normal(size=d), "montee": rng.normal(size=d), "gamma": np.ones(d), "lobe_negatif": False})


def test_cas_sains_manques_arretent(ressources):
    s = vc.courir(ressources, limite=40, exiger_cas_sains=True, n_tirages_a3=200, n_tirages_hasard=1, n_reechantillonnage=20)
    if not s["cas_sains"]["tous_passes"]:
        assert s["verdict_i"] == "chaîne en défaut" and "mesures" not in s


def test_fumee_de_bout_en_bout(ressources):
    s = vc.courir(ressources, limite=40, exiger_cas_sains=False, n_tirages_a3=200, n_tirages_hasard=1, n_reechantillonnage=20)
    assert s["fumee"] is True
    assert s["verdict_i"] in ("n'apporte rien", "apporte quelque chose", "indéterminé")
    assert set(s["aii"]) == {"C1", "C2", "C3"}
    for c in ("C1", "C2", "C3"):
        assert s["aii"][c]["verdict"] in ("sans objet", "n'apporte rien", "apporte", "indéterminé")
    m = s["mesures"]["C2"][0][8]
    assert m["a1"]["rang_s"] >= 1 and len(m["a3"]["jetons_s"]) == 20 and len(m["lecture_r_poids"]) == 20
    assert m["aii"]["pca_k_effectif"][512] < 512


def test_permuter_par_groupe():
    y = np.array([1, 0, 1, 0, 1, 0, 1, 1, 0, 0])
    g = np.array(["a", "a", "b", "b", "c", "c", "d", "e", "f", "h"])
    yp = vc.permuter_par_groupe(y, g, 3)
    for gg in "abc":
        assert sorted(yp[g == gg]) == [0, 1]
    assert sorted(yp[6:]) == sorted(y[6:])
    assert (vc.permuter_par_groupe(y, g, 3) == yp).all()
