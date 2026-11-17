"""Essais (v2 : C3b, C4, chargement réel, artefacts lot ignoré, non-déterminisme, instabilité au seul lot 64, ablation inerte) de `controle_ia.neuron_lens.audit_invariance_lot_v2` (R5 : cas sain et artefacts) sur processeur, avec un Llama miniature
aléatoire (aucun poids téléchargé, aucun code voisin exécuté)."""
import json

import pytest

torch = pytest.importorskip("torch")
transformers = pytest.importorskip("transformers")

from controle_ia.neuron_lens import audit_invariance_lot_v2 as ai  # noqa: E402


@pytest.fixture(scope="module")
def mini():
    torch.manual_seed(0)
    cfg = transformers.LlamaConfig(vocab_size=1500, hidden_size=32, intermediate_size=64, num_hidden_layers=3,
                                   num_attention_heads=4, num_key_value_heads=2, max_position_embeddings=512)
    lm = transformers.LlamaForCausalLM(cfg).eval()
    return lm


def test_taches_reproductibles():
    a, b = ai.taches(130000, 14336), ai.taches(130000, 14336)
    assert a == b and len(a) == 64
    assert all(ai.LONGUEURS[0] <= len(j["ids"]) <= ai.LONGUEURS[1] and j["pos"] == len(j["ids"]) - 1 - ai.FENETRE for j in a)
    assert len({len(j["ids"]) for j in a}) > 10  # longueurs variées : le complément change d'un lot à l'autre


def test_cas_sain_miniature(mini):
    res = ai.mesurer(mini.model, mini.lm_head, 1500, 64, "cpu", couches=(0, 2), lots=(16, 64, 1, 7), n=24)
    lec = ai.lire_issue(res)
    assert lec["C1_formes_differentes"] and lec["C2_perturbation_vue"] and lec["C3_rejeu_identique"]
    assert lec["C3b_rejeu_lot64_identique"] and lec["C4_ablation_agit"]
    assert set(res["temoin_produit_bf16"]) == {"identiques", "ecart_max"}
    assert "taches_identiques_demi_precision" in res["couches"]["0"]["par_lot"]["64"]
    r = res["couches"]["0"]
    assert r["par_lot"]["16"]["taches_identiques"] == 24
    assert {tuple(f) for f in r["par_lot"]["16"]["formes"]} != {tuple(f) for f in r["par_lot"]["64"]["formes"]}
    assert lec["issue"] in ("invariance établie", "invariance réfutée")  # le processeur n'est pas la carte : l'issue n'est pas essayée ici
    json.dumps(res)  # sérialisable


class Bruyant(torch.nn.Module):
    """Artefact : la sortie dépend de la taille du lot (bruit déterministe fonction du nombre de lignes)."""

    def __init__(self, inner):
        super().__init__()
        self.inner, self.layers, self.config = inner, inner.layers, inner.config

    def forward(self, **kw):
        o = self.inner(**kw)
        g = torch.Generator().manual_seed(kw["input_ids"].shape[0])
        o.last_hidden_state = o.last_hidden_state + 1e-3 * torch.randn(o.last_hidden_state.shape, generator=g)
        return o


class Sourd(torch.nn.Module):
    """Artefact : la sortie ne dépend pas des jetons (la perturbation ne se voit pas)."""

    def __init__(self, inner):
        super().__init__()
        self.inner, self.layers, self.config = inner, inner.layers, inner.config

    def forward(self, input_ids, attention_mask):
        return self.inner(input_ids=torch.ones_like(input_ids) * 5, attention_mask=attention_mask)


def test_artefact_lot_variant_refute(mini):
    res = ai.mesurer(Bruyant(mini.model), mini.lm_head, 1500, 64, "cpu", couches=(1,), lots=(16, 64), n=24)
    lec = ai.lire_issue(res)
    assert lec["issue"] == "invariance réfutée" and res["couches"]["1"]["par_lot"]["64"]["ecart_max"] > 0


def test_artefact_perturbation_invisible(mini):
    res = ai.mesurer(Sourd(mini.model), mini.lm_head, 1500, 64, "cpu", couches=(1,), lots=(16, 64), n=24)
    lec = ai.lire_issue(res)
    assert not lec["C2_perturbation_vue"] and lec["issue"] == "indéterminé"


def test_crochet_retire_et_ablation_active(mini):
    jobs = ai.taches(1500, 64, n=4)
    avant = len(mini.model.layers[0].mlp.down_proj._forward_pre_hooks)
    d = ai.differences(mini.model, mini.lm_head, 0, jobs, 2, "cpu")
    assert len(mini.model.layers[0].mlp.down_proj._forward_pre_hooks) == avant
    assert all(float(t.abs().max()) > 0 for t in d)  # l'ablation change la ligne ablatée


def test_installer_quatre_etapes(monkeypatch):
    from controle_ia.neuron_lens import b_alpha_lancer_v5 as base
    for nom in ("ETAPES", "PREREQUIS", "ECHEANCES", "AUDITS", "ETAPE_FONCTIONS"):
        monkeypatch.setattr(base, nom, getattr(base, nom))
    ai.installer()
    assert base.ETAPES == ai.ETAPES and set(base.ETAPE_FONCTIONS) == set(ai.ETAPES)
    assert base.ETAPE_FONCTIONS["audit-invariance"] is ai.etape_audit_invariance
    assert "audit-invariance" not in base.JETON and "audit-invariance" not in base.EN_LIGNE
    assert base.verifier_environnement("audit-invariance", {"GO_ID": base.GO_ATTENDU, "NEURON_LENS_MODEL": base.LLAMA,
                                                            "HF_HOME": "/tmp/hf", "HF_HUB_OFFLINE": "1"}) == []
    assert base.verifier_environnement("corpus", {}) != []  # étape retirée : refusée


def test_etape_sur_contexte(tmp_path, monkeypatch, mini):
    """L'étape complète, avec le chargement remplacé : résultat scellé, détail versé, lecture par programme."""
    import subprocess
    from controle_ia.manifeste import creer_manifeste
    from controle_ia.neuron_lens import b_alpha_lancer_v5 as base
    r = tmp_path / "depot"
    r.mkdir()
    (r / ".gitignore").write_text("diag/\nruns/\n")
    subprocess.run(["git", "init", "-q", str(r)], check=True)
    subprocess.run(["git", "-C", str(r), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(r), "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-q", "-m", "i"],
                   check=True)
    c = base.Contexte(r, "20261120-100000-neuron-lens-b-alpha", tmp_path / "hf")
    creer_manifeste(c.racine, c.run_id, {"essai": 1}, ["b-alpha-intervalles"], entropie=base.ENTROPIE)
    monkeypatch.setattr(ai, "mesurer", lambda m, h, v, n, d: MESURER(m, h, v, n, d, couches=(0,), lots=(16, 64), n=8))
    c.diag.mkdir(parents=True, exist_ok=True)
    out = ai.etape_audit_invariance(c, charger=lambda: (mini.model, mini.lm_head, "cpu", "processeur"))
    assert out["carte"] == "processeur" and (c.racine / out["detail"]["chemin"]).exists()
    assert set(out["lecture_par_programme"]) >= {"issue", "C1_formes_differentes", "C2_perturbation_vue", "C3_rejeu_identique",
                                                 "C3b_rejeu_lot64_identique", "C4_ablation_agit"}
    assert out["preenregistrement"]["chemin"] == ai.PREREG and out["graine"]["entropie"] == ai.ENTROPIE_AUDIT


MESURER = ai.mesurer


class Aleatoire(torch.nn.Module):
    """Artefact : non-déterminisme (bruit nouveau à chaque appel), seulement aux passes de `lignes` lignes si donné."""

    def __init__(self, inner, lignes=None):
        super().__init__()
        self.inner, self.layers, self.config, self.lignes = inner, inner.layers, inner.config, lignes

    def forward(self, **kw):
        o = self.inner(**kw)
        if self.lignes is None or kw["input_ids"].shape[0] == self.lignes:
            o.last_hidden_state = o.last_hidden_state + 1e-3 * torch.randn(o.last_hidden_state.shape)
        return o


def test_artefact_non_determinisme(mini):
    res = ai.mesurer(Aleatoire(mini.model), mini.lm_head, 1500, 64, "cpu", couches=(1,), lots=(16, 64), n=24)
    lec = ai.lire_issue(res)
    assert not lec["C3_rejeu_identique"] and lec["issue"] == "indéterminé"


def test_artefact_instable_au_seul_lot64(mini):
    """B1 de la contre-lecture : instable aux seules passes de 128 lignes (lot 64 × 2) : C3 tient, C3b tombe → indéterminé."""
    res = ai.mesurer(Aleatoire(mini.model, lignes=48), mini.lm_head, 1500, 64, "cpu", couches=(1,), lots=(16, 64), n=24)
    lec = ai.lire_issue(res)
    assert lec["C3_rejeu_identique"] and not lec["C3b_rejeu_lot64_identique"] and lec["issue"] == "indéterminé"


def test_artefact_lot_ignore(mini, monkeypatch):
    vraie = ai.differences
    monkeypatch.setattr(ai, "differences", lambda m, h, c, jobs, lot, d, formes=None: vraie(m, h, c, jobs, 16, d, formes))
    res = ai.mesurer(mini.model, mini.lm_head, 1500, 64, "cpu", couches=(1,), lots=(16, 64), n=24)
    lec = ai.lire_issue(res)
    assert not lec["C1_formes_differentes"] and lec["issue"] == "indéterminé"


def test_artefact_ablation_inerte(mini, monkeypatch):
    monkeypatch.setattr(ai, "differences", lambda m, h, c, jobs, lot, d, formes=None: (
        formes.append([2 * lot, 9]) if formes is not None else None) or [torch.zeros(9, 5) for _ in jobs])
    res = ai.mesurer(mini.model, mini.lm_head, 1500, 64, "cpu", couches=(1,), lots=(16, 64), n=24)
    lec = ai.lire_issue(res)
    assert not lec["C4_ablation_agit"] and lec["issue"] == "indéterminé"


def test_charger_reel_sur_processeur(tmp_path, mini):
    """M3 : le vrai chemin de chargement (from_pretrained en bf16, voisin dans le chemin, decoder_stack), avec un modèle miniature
    sauvé sur le disque et un faux `neuron_lens/transport.py`."""
    import sys
    d = tmp_path / "modele"
    mini.save_pretrained(d)
    v = tmp_path / "voisin" / "neuron_lens"
    v.mkdir(parents=True)
    (v / "__init__.py").write_text("")
    (v / "transport.py").write_text("def decoder_stack(m):\n    return m.model\n")
    sys.modules.pop("neuron_lens", None)
    sys.modules.pop("neuron_lens.transport", None)
    try:
        model, head, device, carte = ai.charger_reel(tmp_path / "voisin", str(d), "cpu")
    finally:
        sys.modules.pop("neuron_lens", None)
        sys.modules.pop("neuron_lens.transport", None)
        if str(tmp_path / "voisin") in sys.path:
            sys.path.remove(str(tmp_path / "voisin"))
    assert carte == "processeur" and next(model.parameters()).dtype == torch.bfloat16 and hasattr(model, "layers")
