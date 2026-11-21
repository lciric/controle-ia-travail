"""Génération par lots, notation, états internes (exploratoire), sur le modèle jouet et un faux vLLM."""
import json
import sys
import types

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")

from controle_ia.dopamine_exploratoire import etats_v1, generation_v1, jouet_v1, math500_v1  # noqa: E402
from controle_ia.dopamine_exploratoire.stockage_v1 import lire_jsonl  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

RJ = dict(generation_v1.RECETTE_TABLEAU_6, max_jetons=10)


def test_recette_du_tableau_6():
    assert generation_v1.RECETTE_TABLEAU_6["max_jetons"] == 16000 and generation_v1.RECETTE_TABLEAU_6["top_p"] == 0.95
    generation_v1.exiger_recette(dict(generation_v1.RECETTE_TABLEAU_6))
    with pytest.raises(GardeArret, match="16 000"):
        generation_v1.exiger_recette(RJ)
    generation_v1.exiger_recette(RJ, jouet=True)
    with pytest.raises(GardeArret, match="temperature"):
        generation_v1.exiger_recette(dict(RJ, temperature=0.7), jouet=True)


def test_tronquer_aux_arrets():
    d = jouet_v1.DecoupeurJouet()
    ids = d.encoder("12<|im_end|>34")
    t, coupe = generation_v1.tronquer_aux_arrets(ids, d.decoder, ("<|im_end|>",))
    assert coupe and d.decoder(t) == "12<|im_end|>"
    t2, c2 = generation_v1.tronquer_aux_arrets(d.encoder("1234"), d.decoder, ("<|im_end|>",))
    assert not c2 and d.decoder(t2) == "1234"


def test_faux_vllm_recoit_la_recette_et_les_graines(monkeypatch):
    vus = {}

    class SP:
        def __init__(self, **k):
            self.k = k

    class LLM:
        def __init__(self, **k):
            vus["llm"] = k

        def generate(self, requetes, params, use_tqdm=False):
            vus["params"] = [p.k for p in params]
            o = types.SimpleNamespace(token_ids=[5, 6], text="\\boxed{1}", finish_reason="stop")
            return [types.SimpleNamespace(outputs=[o]) for _ in requetes]

    monkeypatch.setitem(sys.modules, "vllm", types.SimpleNamespace(LLM=LLM, SamplingParams=SP))
    g = generation_v1.GenerateurVllm("/m", dict(generation_v1.RECETTE_TABLEAU_6), math500_v1.ARRETS_QWEN_BOXED)
    out = g.generer([[1, 2], [3]], [11, 12])
    assert vus["llm"]["gpu_memory_utilization"] == 0.75
    assert [p["seed"] for p in vus["params"]] == [11, 12]
    assert all(p["temperature"] == 1.0 and p["top_p"] == 0.95 and p["max_tokens"] == 16000 and p["n"] == 1
               for p in vus["params"])
    assert out[0] == {"jetons": [5, 6], "texte": "\\boxed{1}", "fin": "arret"}
    with pytest.raises(GardeArret):
        generation_v1.GenerateurVllm("/m", RJ)                      # recette réduite refusée hors du jouet


class Compteur:
    def __init__(self, g):
        self.g, self.appels, self.nom = g, 0, g.nom

    def generer(self, inv, gr):
        self.appels += 1
        return self.g.generer(inv, gr)


def _generer(tmp_path, n=10, taille=4):
    m, d = jouet_v1.modele_jouet(0, couches=8)
    qs = jouet_v1.questions_jouets(n)
    textes = {q["id"]: math500_v1.invite(q["probleme"], "litteral") for q in qs}
    g = Compteur(generation_v1.GenerateurTransformers(m, d, RJ, math500_v1.ARRETS_QWEN_BOXED, jouet=True))
    r = generation_v1.generer_par_lots(qs, textes, d, g, tmp_path / "gen", taille, lambda i: hash(i) % 1000)
    return m, d, qs, textes, g, r


def test_generation_par_lots_et_reprise(tmp_path):
    m, d, qs, textes, g, r = _generer(tmp_path)
    assert r == {"lots_ecrits": 3, "lots_sautes": 0} and g.appels == 3
    lignes = lire_jsonl(tmp_path / "gen" / "lot-00000.jsonl")
    assert len(lignes) == 4 and all(len(x["jetons_reponse"]) == x["n_jetons_reponse"] <= 10 for x in lignes)
    # coupure : le dernier lot est perdu (avec son empreinte, rangée de côté pour l'essai), la reprise ne refait que lui
    dernier = tmp_path / "gen" / "lot-00002.jsonl"
    dernier.rename(tmp_path / "mis-de-cote.jsonl")
    (tmp_path / "gen" / "lot-00002.jsonl.sha256").rename(tmp_path / "mis-de-cote.sha256")
    g2 = Compteur(g.g)
    r2 = generation_v1.generer_par_lots(qs, textes, d, g2, tmp_path / "gen", 4, lambda i: hash(i) % 1000)
    assert r2 == {"lots_ecrits": 1, "lots_sautes": 2} and g2.appels == 1
    # artefact : un autre jeu de questions sur les mêmes lots
    with pytest.raises(GardeArret, match="questions différentes"):
        generation_v1.generer_par_lots(list(reversed(qs)), textes, d, g2, tmp_path / "gen", 4, lambda i: 0)


def test_generation_meme_graine_meme_reponse(tmp_path):
    m, d = jouet_v1.modele_jouet(0, couches=8)
    g = generation_v1.GenerateurTransformers(m, d, RJ, (), jouet=True)
    ids = d.encoder(math500_v1.invite("3+4", "litteral"))
    assert g.generer([ids], [5]) == g.generer([ids], [5])


def test_notation_par_lots(tmp_path):
    m, d, qs, *_ = _generer(tmp_path)
    r = generation_v1.noter_par_lots(qs, tmp_path / "gen", tmp_path / "notes")
    assert r["lots_ecrits"] == 3
    rec = generation_v1.lire_recompenses(tmp_path / "notes")
    assert set(rec) == {q["id"] for q in qs} and set(rec.values()) <= {0, 1}
    assert generation_v1.noter_par_lots(qs, tmp_path / "gen", tmp_path / "notes")["lots_sautes"] == 3
    with pytest.raises(GardeArret, match="absente du jeu"):
        generation_v1.noter_par_lots(qs[:2], tmp_path / "gen", tmp_path / "notes2")


def test_positions_des_etats():
    assert etats_v1.positions_etats(5, 3, "trajectoire").tolist() == [4, 5, 6, 7]
    assert etats_v1.positions_etats(5, 0, "trajectoire").tolist() == [4]
    assert etats_v1.positions_etats(5, 3, "s0").tolist() == [4]
    with pytest.raises(GardeArret):
        etats_v1.positions_etats(0, 3, "s0")
    with pytest.raises(GardeArret):
        etats_v1.exiger_couches([0, 2], 24)
    with pytest.raises(GardeArret):
        etats_v1.exiger_couches([2, 25], 24)
    assert etats_v1.exiger_couches([24, 2], 24) == [2, 24]


def test_crochets_egaux_aux_etats_caches_de_transformers():
    m, d = jouet_v1.modele_jouet(0, couches=8)
    ids = d.encoder(math500_v1.invite("1+2", "litteral")) + [6, 7]
    pris = etats_v1.etats_d_une_sequence(m, ids, [2, 3, 7])
    with torch.no_grad():
        hs = m(input_ids=torch.tensor([ids]), output_hidden_states=True).hidden_states
    for l in (2, 3, 7):
        np.testing.assert_allclose(pris[l], hs[l][0].numpy(), rtol=1e-5, atol=1e-6)


def test_float16_garde_le_debordement():
    etats_v1.en_float16(np.array([[1.0, -3.0]]), "sain")
    with pytest.raises(GardeArret, match="débordement"):
        etats_v1.en_float16(np.array([[1e6]]), "artefact")


def test_extraction_par_lots_reprise_et_alteration(tmp_path):
    m, d, qs, *_ = _generer(tmp_path)
    r = etats_v1.extraire_par_lots(m, tmp_path / "gen", [2, 7], tmp_path / "etats")
    assert r["lots_ecrits"] == 3
    x = etats_v1.charger_couche(tmp_path / "etats", 7)
    g0 = lire_jsonl(tmp_path / "gen" / "lot-00000.jsonl")[0]
    assert x[g0["id"]].shape == (g0["n_jetons_reponse"] + 1, 16) and x[g0["id"]].dtype == np.float16
    ids = g0["jetons_invite"] + g0["jetons_reponse"]
    ref = etats_v1.etats_d_une_sequence(m, ids, [7])[7][len(g0["jetons_invite"]) - 1:]
    np.testing.assert_allclose(x[g0["id"]].astype(np.float32), ref.astype(np.float16).astype(np.float32))
    assert etats_v1.extraire_par_lots(m, tmp_path / "gen", [2, 7], tmp_path / "etats")["lots_sautes"] == 3
    # coupure entre l'index et le tableau : l'index scellé est gardé, le tableau seul est refait
    fa = tmp_path / "etats" / "couche-07" / "lot-00001.npy"
    fa.rename(tmp_path / "npy-de-cote")
    (tmp_path / "etats" / "couche-07" / "lot-00001.npy.sha256").rename(tmp_path / "sha-de-cote")
    assert etats_v1.extraire_par_lots(m, tmp_path / "gen", [2, 7], tmp_path / "etats")["lots_ecrits"] == 1
    # artefact : tableau altéré
    a = np.load(fa)
    a[0, 0] += 1
    with open(fa, "wb") as f:
        np.save(f, a)
    with pytest.raises(GardeArret):
        etats_v1.charger_couche(tmp_path / "etats", 7)


def test_extraction_s0_seul(tmp_path):
    m, d, qs, *_ = _generer(tmp_path, n=4)
    etats_v1.extraire_par_lots(m, tmp_path / "gen", [3], tmp_path / "e0", "s0")
    x = etats_v1.charger_couche(tmp_path / "e0", 3)
    assert all(v.shape == (1, 16) for v in x.values())
    idx = json.loads((tmp_path / "e0" / "couche-03" / "lot-00000.index.json").read_text())
    assert idx["mode"] == "s0" and "numérotation à partir de 1" in idx["convention"]


def test_garde_des_couches_basses_sur_episodes_du_programme(tmp_path):
    m, d, qs, *_ = _generer(tmp_path, n=4)
    with pytest.raises(GardeArret, match="MATH500 public"):
        etats_v1.extraire_par_lots(m, tmp_path / "gen", [3, 7], tmp_path / "e", source="episode-du-programme")
    etats_v1.extraire_par_lots(m, tmp_path / "gen", [7], tmp_path / "e", source="episode-du-programme")
    with pytest.raises(GardeArret):
        etats_v1.exiger_source([7], "autre")


def test_garde_de_position_et_confiance(tmp_path, monkeypatch):
    m, d, qs, *_ = _generer(tmp_path, n=4)
    etats_v1.extraire_par_lots(m, tmp_path / "gen", [2], tmp_path / "e")
    c = json.loads((tmp_path / "e" / "confiance-jeton" / "lot-00000.json").read_text())
    assert set(c["confiance_jeton"]) == {q["id"] for q in qs} and all(0 < v <= 1 for v in c["confiance_jeton"].values())
    assert max(c["ecart_position"].values()) < 1e-5
    vraie = etats_v1.positions_etats
    monkeypatch.setattr(etats_v1, "positions_etats", lambda n, t, mode: vraie(n, t, mode) + 1)   # indice décalé d'un
    gen2 = tmp_path / "gen2"
    gen2.mkdir()
    lignes = [dict(x, jetons_reponse=x["jetons_reponse"] or [6]) for x in lire_jsonl(tmp_path / "gen" / "lot-00000.jsonl")]
    from controle_ia.dopamine_exploratoire.stockage_v1 import ecrire_jsonl
    ecrire_jsonl(gen2 / "lot-00000.jsonl", [dict(x, n_jetons_reponse=len(x["jetons_reponse"])) for x in lignes])
    with pytest.raises(GardeArret, match="garde de position"):
        etats_v1.extraire_par_lots(m, gen2, [2], tmp_path / "e2")
