"""Fumée (v4) de bout en bout de l'assemblage du volet A sur un Qwen3 miniature aléatoire (vrai tokeniseur, lentilles factices) ; sortie
marquée « fumée ». Aucun poids téléchargé, aucun code voisin."""
import numpy as np
import pytest
import torch
from transformers import Qwen3Config, Qwen3ForCausalLM

from controle_ia.neuron_lens import volet_a_course_v4 as vc
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
    ecrits = []
    s = vc.courir(ressources, limite=40, exiger_cas_sains=False, n_tirages_a3=200, n_tirages_hasard=1, n_reechantillonnage=20,
                  ecrire_brut=lambda nom, contenu: ecrits.append(nom), forcer_audit=True)
    assert ecrits == ["cas-sains", "mesures-C3", "mesures-C1", "mesures-C2", "audit-trop-beau"]
    au = s["audit_trop_beau"]
    assert set(au["sixieme_decoupe"]) == {"C1", "C2", "C3"} and "a1" in au["sixieme_decoupe"]["C2"][8]
    assert au["retrait_verifie"]["C1"]["invites_avec_jeton_retire_restant"] == 0
    assert len(au["c2_sans_P"]) == 5 and all(r >= 1 for r in au["c2_sans_P"][0].values())
    assert len(au["c2_sans_P_permutee"]) == 5 and len(au["rangs_course_c2"]) == 5
    assert len(s["cas_sains"]["i_owl_vocabulaire_entier"]) == 10
    assert "sonde_permutee" not in s["mesures"]["C3"][0][8]
    assert s["fumee"] is True
    assert s["verdict_i"] in ("n'apporte rien", "apporte quelque chose", "indéterminé")
    assert set(s["aii"]) == {"C1", "C2", "C3"}
    for c in ("C1", "C2", "C3"):
        assert s["aii"][c]["verdict"] in ("sans objet", "n'apporte rien", "apporte", "indéterminé")
    m = s["mesures"]["C2"][0][8]
    assert m["a1"]["rang_s"] >= 1 and len(m["a3"]["jetons_s"]) == 20 and len(m["lecture_r_poids"]) == 20
    assert m["aii"]["pca_k_effectif"][512] < 512
    a2 = s["mesures"]["C1"][0][14]["a2"]  # v2 : témoins de A2 rapportés
    assert "rho_permutee" in a2 and "rho_c3" in a2 and a2["rho_c3"] is not None
    assert isinstance(s["avertissements_convergence"], int)
    t = m["a3"]["jetons_s"]
    assert len(set(t)) == 20


def test_permuter_par_groupe():
    y = np.array([1, 0, 1, 0, 1, 0, 1, 1, 0, 0])
    g = np.array(["a", "a", "b", "b", "c", "c", "d", "e", "f", "h"])
    yp = vc.permuter_par_groupe(y, g, 3)
    for gg in "abc":
        assert sorted(yp[g == gg]) == [0, 1]
    assert sorted(yp[6:]) == sorted(y[6:])
    assert (vc.permuter_par_groupe(y, g, 3) == yp).all()


def test_plis_internes_groupes():
    """Contre-lecture 2, remarque 9 : les plis internes de `_choisir_c` (StratifiedGroupKFold) ne coupent aucun groupe."""
    from sklearn.model_selection import StratifiedGroupKFold
    for c in ("C1", "C2", "C3"):
        ex = vd.charger(c)
        app, _ = vd.decoupe(ex, vd.arbre_de_graines().decoupes[c][0]["permutation"])
        y = np.array([ex[i].classe for i in app])
        g = np.array([ex[i].groupe for i in app])
        for a, t in StratifiedGroupKFold(n_splits=5).split(np.zeros(len(y)), y, g):
            assert not (set(g[a]) & set(g[t])) and len(set(y[t])) == 2


def test_gardes_non_tries_refuses(ressources):
    import copy
    r = copy.copy(ressources)
    r.gardes = ressources.gardes[::-1].copy()
    with pytest.raises(ValueError):
        vc.courir(r, limite=40, exiger_cas_sains=False)


def test_sixieme_decoupe_prolonge_l_arbre():
    """Contre-lecture 3, remarque 6 : les 5 premiers enfants de `spawn(6)` de chaque contraste sont les découpes de la course."""
    g = vd.arbre_de_graines()
    r = np.random.SeedSequence(vd.ENTROPIE).spawn(4)
    for ic, c in enumerate(("C1", "C2", "C3")):
        six = r[ic].spawn(6)
        for d in range(5):
            assert g.decoupes[c][d]["permutation"].spawn_key[:-1] == six[d].spawn_key
        assert six[5].spawn_key == (ic, 5)


def test_nan_de_a3_arrete_apres_ecriture(ressources, monkeypatch):
    """Contre-lecture 3, remarque 6 : une AUROC non calculable de A3 arrête la course aux décisions, mesures brutes déjà écrites."""
    vrai = vc._mesure_a3

    def faux(*a, **k):
        m = vrai(*a, **k)
        m["chute_s"] = float("nan")
        return m
    monkeypatch.setattr(vc, "_mesure_a3", faux)
    ecrits = []
    with pytest.raises(ValueError):
        vc.courir(ressources, limite=40, exiger_cas_sains=False, n_tirages_a3=200, n_tirages_hasard=1, n_reechantillonnage=20,
                  ecrire_brut=lambda nom, contenu: ecrits.append(nom))
    assert ecrits == ["cas-sains", "mesures-C3", "mesures-C1", "mesures-C2"]
