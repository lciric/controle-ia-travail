"""Essai écrit des crochets de pilotage et d'ablation de `scripts/checks/causal_lens.py` (`measure`) sur un Llama miniature
aléatoire (texte gelé v6, § B.1 : « norme de la cible non nulle, pôle témoin différent du pôle » ; devis B-α v2, § 6, pièce 2, m4).

À jouer SUR LA MACHINE LOUÉE à B0, jamais dans le conteneur de la session (décision (a) de Lazar, R-2710), dans l'arbre du dépôt
voisin au commit `849bfe16` avec les quatre correctifs appliqués :

    NEURON_LENS_ROOT=$PWD NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct python -m pytest -q -rs <chemin>/essai-crochets-causal_lens-llama-v1.py

Aucun test ne doit être sauté (un test sauté = arrêt). Aucun poids n'est téléchargé : le modèle est un `LlamaForCausalLM` de
3 couches tiré au hasard (graine `SeedSequence(entropy=20261114, spawn_key=(2,))`, branche « B-α, essai des crochets »), en
float32, sur le processeur. Le vrai `measure` tourne de bout en bout ; seules ses entrées lourdes sont remplacées (modèle,
tokeniseur, tables `acts` du catalogue, documents, contextes, dossier de sortie) et `arch.cap` est l'identité (Llama n'a pas de
plafonnement final des logits ; `arch.cap` lirait sinon la configuration sur le Hub). Les cibles écrites par `measure` sont
comparées à une référence calculée **par un autre mécanisme** :
- pilotage : `measure` ajoute `s·α·W_down[:, n]` à la sortie de la couche à portes (crochet d'après) ; la référence ajoute `s·α` à
  l'activation du neurone `n` à l'entrée de `down_proj` (crochet d'avant), chaque condition passée seule, logits du modèle complet ;
- ablation : `measure` met à zéro l'entrée de `down_proj` au neurone et à la position, lignes propres et ablatées côte à côte,
  complétées à droite ; la référence met à zéro la sortie de `up_proj` au même endroit (même produit nul), document seul, sans
  complément.
R5 : chaque comparaison est faite sur le cas sain (égalité aux tolérances) et sur des artefacts qui doivent être rejetés (signe
opposé, neurone voisin, autre couche, poussée à toutes les positions, autre position d'ablation). « Pôle témoin différent du pôle » :
les deux pôles d'un même neurone donnent des cibles distinctes, et la ligne témoin (non pilotée, propre) n'est pas touchée.
"""
import argparse
import hashlib
import importlib.util
import math
import os
import sys
from pathlib import Path

import numpy as np
import pytest
import torch

ROOT = Path(os.environ.get("NEURON_LENS_ROOT", ".")).resolve()
SHA_CAUSAL_CORR = "a9d3bc8e8dde945c4ff0f4a229f30c78b35ee299a4fa1fe34fe75db35252141b"
LLAMA = "meta-llama/Llama-3.1-8B-Instruct"
GRAINE = int(np.random.SeedSequence(entropy=20261114, spawn_key=(2,)).generate_state(1)[0])
NL, D, F, V = 3, 32, 64, 96  # couches, largeur, neurones par couche, vocabulaire du modèle miniature
C, T, K, PER = 3, 24, 4, 2  # contextes, longueur, documents de tête par pôle, neurones tirés par couche
N_DOCS = 6
REL = 2e-3  # tolérance relative du cas sain (cibles rangées en float16 par `measure`)
SEP = 2e-2  # écart relatif minimal exigé d'un artefact (dix fois la tolérance)


# ---------------------------------------------------------------- modèle et entrées miniatures (notre code, sans le dépôt voisin)

def mini_llama():
    from transformers import LlamaConfig, LlamaForCausalLM
    cfg = LlamaConfig(vocab_size=V, hidden_size=D, intermediate_size=F, num_hidden_layers=NL, num_attention_heads=4,
                      num_key_value_heads=2, max_position_embeddings=128, rms_norm_eps=1e-5, tie_word_embeddings=False,
                      initializer_range=0.2, bos_token_id=1, eos_token_id=2, pad_token_id=0)
    torch.manual_seed(GRAINE)
    return LlamaForCausalLM(cfg).float().eval().requires_grad_(False)


def entrees():
    g = torch.Generator().manual_seed(GRAINE + 1)
    longueurs = [20, 33, 27, 40, 18, 30]
    docs = [torch.randint(3, V, (n,), generator=g, dtype=torch.int32) for n in longueurs]
    ctx = [torch.randint(3, V, (T,), generator=g).tolist() for _ in range(4 * C)]
    top = {}
    for layer in range(NL):
        act_top = 1.0 + 2.0 * torch.rand(2, F, generator=g)
        top_val = 0.5 + torch.rand(2, F, K, generator=g)
        top_val[:, :, -1] = 0.0  # le dernier document de tête n'a pas tiré : `measure` doit le sauter
        top_doc = torch.randint(0, N_DOCS, (2, F, K), generator=g)
        frac = torch.rand(2, F, K, generator=g)
        top_pos = torch.stack([(frac[..., j] * torch.tensor(longueurs)[top_doc[..., j]]).long() for j in range(K)], -1)
        top_pos[0, :, 0] = torch.tensor(longueurs)[top_doc[0, :, 0]] - 1  # dernière position : fenêtre tronquée, aucun jeton suivant
        top[layer] = {"act_top": act_top, "top_val": top_val, "top_doc": top_doc, "top_pos": top_pos}
    return docs, ctx, top


def logp(lm, ids, crochets=()):
    """Log-probabilités du modèle complet (logits de `lm`, float32), avec des crochets posés le temps d'une passe."""
    poses = [mod.register_forward_pre_hook(fn) if avant else mod.register_forward_hook(fn) for mod, fn, avant in crochets]
    try:
        with torch.inference_mode():
            return torch.log_softmax(lm(input_ids=ids).logits.float(), -1)
    finally:
        for h in poses:
            h.remove()


def ref_pilotage(lm, ctx, layer, n, s, debut=16):
    """Moyenne sur contextes et positions [debut, T) du changement de log-probabilités quand `s` s'ajoute à l'activation du
    neurone `n` de la couche `layer`, aux positions `debut` et suivantes (crochet d'avant sur `down_proj`)."""
    def pousse(mod, a):
        x = a[0].clone()
        x[:, debut:, n] += s
        return (x,)
    propre = logp(lm, ctx)
    pilote = logp(lm, ctx, [(lm.model.layers[layer].mlp.down_proj, pousse, True)])
    return (pilote[:, 16:] - propre[:, 16:]).reshape(-1, V).mean(0)


def ref_ablation(lm, seq, layer, n, pos, fenetre=8):
    """(diff à la position, diff sommée sur la fenêtre, diff du jeton suivant ou nan) : propre − ablaté, le neurone `n` mis à
    zéro à `pos` par la sortie de `up_proj` (le produit qui entre dans `down_proj` y est donc nul)."""
    def coupe(mod, a, o):
        o = o.clone()
        o[:, pos, n] = 0
        return o
    ids = seq[None].long()
    propre = logp(lm, ids)[0]
    ablate = logp(lm, ids, [(lm.model.layers[layer].mlp.up_proj, coupe, False)])[0]
    fin = min(pos + 1 + fenetre, len(seq))
    diff = propre[pos:fin] - ablate[pos:fin]
    suivant = diff[0, int(seq[pos + 1])].item() if pos + 1 < len(seq) else math.nan
    return diff[0], diff.sum(0), suivant


def proche(obtenu, ref):
    """Cas sain : écart maximal sous REL fois l'échelle de la référence ; la référence n'est pas nulle (norme de la cible)."""
    echelle = ref.abs().max().item()
    return echelle > 1e-4 and (obtenu.float() - ref).abs().max().item() <= REL * echelle + 1e-6


def loin(obtenu, faux):
    """Artefact rejeté : écart maximal au-delà de SEP fois l'échelle de la cible obtenue."""
    return (obtenu.float() - faux).abs().max().item() > SEP * obtenu.float().abs().max().item()


# ---------------------------------------------------------------- le vrai `measure`, entrées remplacées

@pytest.fixture(scope="module")
def cl():
    chemin = ROOT / "scripts" / "checks" / "causal_lens.py"
    assert hashlib.sha256(chemin.read_bytes()).hexdigest() == SHA_CAUSAL_CORR, "causal_lens.py n'est pas la version corrigée"
    sys.path.insert(0, str(ROOT))
    for name in [k for k in sys.modules if k == "neuron_lens" or k.startswith("neuron_lens.")]:
        del sys.modules[name]
    spec = importlib.util.spec_from_file_location("causal_lens_corrige", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.MODEL == LLAMA, "NEURON_LENS_MODEL doit nommer le modèle de B-α"
    assert Path(mod.arch.__file__).resolve().is_relative_to(ROOT), "neuron_lens chargé hors de l'arbre corrigé"
    return mod


@pytest.fixture(scope="module")
def mesure(cl, tmp_path_factory):
    lm = mini_llama()
    docs, ctx, top = entrees()
    vus = {}
    mp = pytest.MonkeyPatch()
    try:
        mp.setattr(cl, "AutoTokenizer", type("Tok", (), {"from_pretrained": staticmethod(lambda m: "tokeniseur")}))
        def faux_lm(model, dtype=None):
            vus["lm"] = (model, dtype)
            return lm
        mp.setattr(cl, "AutoModelForCausalLM", type("Lm", (), {"from_pretrained": staticmethod(faux_lm)}))

        def faux_top(layers, f, k):
            vus["top"] = (list(layers), f, k)
            return {l: top[l] for l in layers}
        mp.setattr(cl, "catalog_top", faux_top)
        mp.setattr(cl, "documents", lambda model: docs)

        def faux_ctx(path, tok, n, seq_len, min_len):
            vus["ctx"] = (Path(path).name, tok, n, seq_len, min_len)
            return ctx[:n]
        mp.setattr(cl, "lens_docs", faux_ctx)
        mp.setattr(cl, "CAUSAL", tmp_path_factory.mktemp("causal"))
        mp.setattr(cl.arch, "is_gemma4", lambda m: False)
        mp.setattr(cl.arch, "cap", lambda m, x: x)
        args = argparse.Namespace(model=LLAMA, device="cpu", per_layer=PER, contexts=C, ctx_len=T, top_contexts=K,
                                  cond_batch=3, ctx_batch=5, save_minutes=1e9, layers=None, seed=0)
        cl.measure(args)
        chemin = cl.causal_path(LLAMA, 0)
        out = torch.load(chemin, weights_only=False)
        partiel_reste = chemin.with_name(f"{chemin.stem}-partial.pt").exists()
    finally:
        mp.undo()
    return {"out": out, "lm": lm, "docs": docs, "ctx": torch.tensor(ctx[:C]), "top": top, "vus": vus,
            "partiel_reste": partiel_reste}


def test_montage(cl, mesure):
    """Entrées passées comme prévu ; tirage publié (graine 0) ; aucun pôle nommé pour Llama ; fichier final sans partiel."""
    out, vus = mesure["out"], mesure["vus"]
    assert vus["lm"] == (LLAMA, torch.bfloat16)  # `measure` demande bien le bf16 (le modèle miniature reste en float32)
    assert vus["top"] == (list(range(NL)), F, K)
    assert vus["ctx"] == ("act-dclm.jsonl", "tokeniseur", 4 * C, T, T)
    assert out["picks"] == cl.random_neurons(NL, F, PER, 0) and cl.named_poles() == {}
    assert "seed" not in out["meta"] and "done" not in out and not mesure["partiel_reste"]
    assert torch.equal(out["contexts"], mesure["ctx"])
    for i, (l, n) in enumerate(out["picks"]):
        for p in (0, 1):
            a = mesure["top"][l]["act_top"][p, n].item()
            assert a > 0 and out["alpha"][i, p].item() == pytest.approx(a)


def test_pilotage(cl, mesure):
    """Cas sain : chaque cible de pilotage égale la référence (autre crochet, condition seule), norme non nulle.
    Artefacts rejetés : signe opposé, neurone voisin, autre couche, poussée à toutes les positions (sauf à la dernière couche, où
    elle est indiscernable par construction : rien n'y mélange les positions après la couche à portes)."""
    assert any(l < NL - 1 for l, _ in mesure["out"]["picks"])  # l'artefact « positions » est bien essayé quelque part
    out, lm, ctx = mesure["out"], mesure["lm"], mesure["ctx"]
    for i, (l, n) in enumerate(out["picks"]):
        for p in (0, 1):
            for di, dose in enumerate(cl.DOSES):
                s = (1 - 2 * p) * dose * out["alpha"][i, p].item()
                got = out["steer"][i, p, di]
                assert proche(got, ref_pilotage(lm, ctx, l, n, s)), (i, p, di)
                assert loin(got, ref_pilotage(lm, ctx, l, n, -s)), ("signe", i, p, di)
                assert loin(got, ref_pilotage(lm, ctx, l, (n + 1) % F, s)), ("neurone", i, p, di)
                assert loin(got, ref_pilotage(lm, ctx, (l + 1) % NL, n, s)), ("couche", i, p, di)
                if l < NL - 1:  # à la dernière couche, aucune attention ne suit : les positions < 16 n'atteignent pas [16, T)
                    assert loin(got, ref_pilotage(lm, ctx, l, n, s, debut=0)), ("positions", i, p, di)


def test_poles_distincts_et_temoin(cl, mesure):
    """Pôle témoin différent du pôle : les deux pôles d'un neurone donnent des cibles distinctes (pilotage et ablation) ; la
    dose 4× n'est pas la dose 1× ; la ligne témoin non pilotée est le modèle propre (une cible nulle trahirait un témoin piloté)."""
    out = mesure["out"]
    for i in range(len(out["picks"])):
        for di in range(len(cl.DOSES)):
            assert loin(out["steer"][i, 0, di], out["steer"][i, 1, di].float())
        for p in (0, 1):
            assert loin(out["steer"][i, p, 1], out["steer"][i, p, 0].float())
            assert out["steer"][i, p].float().norm(dim=-1).min() > 0
            assert out["ablate_pos"][i, p].float().norm() > 0 and out["ablate_win"][i, p].float().norm() > 0
        assert loin(out["ablate_pos"][i, 0], out["ablate_pos"][i, 1].float())


def test_ablation(cl, mesure):
    """Cas sain : cibles d'ablation égales à la référence (autre crochet, document seul, sans complément), documents et positions
    consignés, document de tête sans tir sauté. Artefacts rejetés : position voisine, neurone voisin."""
    out, lm, docs, top = mesure["out"], mesure["lm"], mesure["docs"], mesure["top"]
    for i, (l, n) in enumerate(out["picks"]):
        for p in (0, 1):
            pos_l, win_l, faux_pos, faux_neu = [], [], [], []
            for j in range(K):
                v = top[l]["top_val"][p, n, j].item()
                if v <= 0:
                    assert out["fired"][i, p, j] == 0 and out["top_doc"][i, p, j] == -1 and out["top_pos"][i, p, j] == -1
                    assert math.isnan(out["dlogp_next"][i, p, j].item())
                    continue
                d, pos = int(top[l]["top_doc"][p, n, j]), int(top[l]["top_pos"][p, n, j])
                assert (out["top_doc"][i, p, j].item(), out["top_pos"][i, p, j].item()) == (d, pos)
                assert out["fired"][i, p, j].item() == pytest.approx(v)
                seq = docs[d][:pos + 1 + cl.WINDOW]
                rp, rw, rs = ref_ablation(lm, seq, l, n, pos, cl.WINDOW)
                pos_l.append(rp)
                win_l.append(rw)
                got_s = out["dlogp_next"][i, p, j].item()
                assert (math.isnan(got_s) and math.isnan(rs)) or got_s == pytest.approx(rs, rel=1e-3, abs=1e-5)
                faux_pos.append(ref_ablation(lm, seq, l, n, max(pos - 1, 0) if pos > 0 else pos + 1, cl.WINDOW)[0])
                faux_neu.append(ref_ablation(lm, seq, l, (n + 1) % F, pos, cl.WINDOW)[0])
            assert len(pos_l) == K - 1
            assert proche(out["ablate_pos"][i, p], torch.stack(pos_l).mean(0)), (i, p)
            assert proche(out["ablate_win"][i, p], torch.stack(win_l).mean(0)), (i, p)
            assert loin(out["ablate_pos"][i, p], torch.stack(faux_pos).mean(0)), ("position", i, p)
            assert loin(out["ablate_pos"][i, p], torch.stack(faux_neu).mean(0)), ("neurone", i, p)
