"""Essai d'invariance au lot de l'ablation de `measure` sur la machine louée (audit R4 de l'identité au bit près des séries aux lots 16
et 64 de la recourse de B-7) — v2.

v2 = v1 corrigée selon sa contre-lecture (`docs/notes/neuron-lens-v1/audit-invariance-lot/contre-lecture-audit-invariance-lot-v1.md`) :
B1 rejeu du lot 64 (C3b) ; M1 témoin décisif C4 (l'ablation change la différence d'au moins 90 % des tâches) et témoin informatif d'un
produit matriciel bf16 aux formes des deux lots ; M2 préenregistrement et graine déclarés dans le résultat ; M3 chargement réel factorisé
(`charger_reel`), essayé sur processeur ; m1 fenêtre de 9 positions (position et les 8 suivantes) ; m2 lignes 216-246 de la copie au
commit `849bfe16` ; m3 égalité rapportée aussi après arrondi en demi-précision ; m7 carte contrôlée par l'étape.

Mot de Lazar dans la session de la fille, le 2026-11-17 : « faut-il un audit de cette identité ? … : go » ; préenregistrement
`docs/notes/neuron-lens-v1/audit-invariance-lot/preenregistrement-audit-invariance-lot-v1.md`.

Ce module **réutilise la machine à étapes du lanceur v5** (`b_alpha_lancer_v5` : contexte, résultats scellés rattachés au manifeste,
préparation de l'arbre, téléchargements de Llama avec la clé aux seules étapes « jeton », environnement contrôlé) et ne garde que quatre
étapes : `preparer`, `telecharger-tokeniseur`, `telecharger-poids`, `audit-invariance`. L'amorce l'appelle comme elle appelle le lanceur
(`suite`, puis `jouer --etape …`).

`audit-invariance` (hors ligne, sans clé) charge Llama 3.1 8B Instruct comme `measure` (`AutoModelForCausalLM.from_pretrained(…,
dtype=torch.bfloat16)`, révision épinglée) et **refait la boucle d'ablation de `measure`** (copie publiée de `scripts/checks/causal_lens.py`,
l. 216-246 : passes de `2 × lot` lignes, complément à droite sous masque d'attention, crochet avant `down_proj` qui met à zéro le neurone à
la position sur les lignes impaires, `log_softmax` des logits sur la fenêtre, différence propre moins ablatée), sur 64 tâches tirées par
`SeedSequence`, aux couches 0, 15 et 26, aux lots 16, 64, 1 et 7. Mesure : l'empreinte sha256 du tenseur float32 de chaque tâche, et
l'écart maximal à la série du lot 16. Témoins : C1 formes des passes enregistrées par un crochet (le lot change bien la passe) ; C2 un
jeton changé dans la tâche 0 change sa différence et rien d'autre ; C3 le lot 16 rejoué deux fois donne les mêmes empreintes.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

from controle_ia.neuron_lens import b_alpha_lancer_v5 as base

ETAPES = ("preparer", "telecharger-tokeniseur", "telecharger-poids", "audit-invariance")
PREREQUIS = {"preparer": (), "telecharger-tokeniseur": ("preparer",), "telecharger-poids": ("telecharger-tokeniseur",),
             "audit-invariance": ("telecharger-poids",)}
ECHEANCES = {"preparer": (0.05, 0.2), "telecharger-tokeniseur": (0.1, 0.2), "telecharger-poids": (0.2, 0.4),
             "audit-invariance": (0.3, 1.0)}
COUCHES = (0, 15, 26)
PREREG = "docs/notes/neuron-lens-v1/audit-invariance-lot/preenregistrement-audit-invariance-lot-v2.md"
CARTE = "A100-SXM4-40GB"
SEUIL_C4 = 0.90
LOTS = (16, 64, 1, 7)  # le lot 16 sert de référence ; 64 décide ; 1 et 7 sont rapportés
N_TACHES = 64
FENETRE = 8  # WINDOW de la copie publiée
ENTROPIE_AUDIT = 20261117
LONGUEURS = (24, 256)  # longueurs de séquence tirées dans [24, 256] (documents coupés à 256 par la passe)


def taches(vocab: int, n_neurones: int, n: int = N_TACHES, entropie: int = ENTROPIE_AUDIT) -> list[dict]:
    """Tâches fixes : séquence de jetons, position ablatée (dernière position moins la fenêtre), neurone. Graines par SeedSequence."""
    import numpy as np
    rng = np.random.default_rng(np.random.SeedSequence(entropie))
    out = []
    for _ in range(n):
        longueur = int(rng.integers(LONGUEURS[0], LONGUEURS[1] + 1))
        ids = rng.integers(1000, min(vocab, 120000), size=longueur).tolist()
        out.append({"ids": ids, "pos": longueur - 1 - FENETRE, "neurone": int(rng.integers(0, n_neurones))})
    return out


def differences(model, lm_head, couche: int, jobs: list[dict], lot: int, device, formes: list | None = None) -> list:
    """Boucle d'ablation de `measure` (copie publiée, l. 216-246), rendue par tâche : différence propre − ablatée des log-softmax sur
    la fenêtre, en float32, sur le processeur."""
    import torch
    out = []
    for s in range(0, len(jobs), lot):
        part = jobs[s:s + lot]
        seqs = [torch.tensor(j["ids"][:j["pos"] + 1 + FENETRE], dtype=torch.long) for j in part]
        tm = max(len(q) for q in seqs)
        ids = torch.zeros(2 * len(part), tm, dtype=torch.long)
        attn = torch.zeros_like(ids)
        for r, q in enumerate(seqs):
            ids[2 * r, :len(q)] = ids[2 * r + 1, :len(q)] = q
            attn[2 * r, :len(q)] = attn[2 * r + 1, :len(q)] = 1
        rows = torch.arange(1, 2 * len(part), 2, device=device)
        pos_t = torch.tensor([j["pos"] for j in part], device=device)
        neu_t = torch.tensor([j["neurone"] for j in part], device=device)

        def ablate(mod, a):
            x = a[0].clone()
            x[rows, pos_t, neu_t] = 0
            return (x,)
        if formes is not None:
            formes.append(list(ids.shape))
        crochet = model.layers[couche].mlp.down_proj.register_forward_pre_hook(ablate)
        try:
            with torch.inference_mode():
                hs = model(input_ids=ids.to(device), attention_mask=attn.to(device)).last_hidden_state
                for r, j in enumerate(part):
                    fin = min(j["pos"] + 1 + FENETRE, len(seqs[r]))
                    lc = torch.log_softmax(lm_head(hs[2 * r, j["pos"]:fin]).float(), -1)
                    la = torch.log_softmax(lm_head(hs[2 * r + 1, j["pos"]:fin]).float(), -1)
                    out.append((lc - la).cpu())
        finally:
            crochet.remove()
    return out


def empreinte(t) -> str:
    return hashlib.sha256(t.contiguous().numpy().tobytes()).hexdigest()


def comparer(ref: list, autre: list) -> dict:
    import torch
    egales = sum(empreinte(a) == empreinte(b) for a, b in zip(ref, autre))
    egales16 = sum(torch.equal(a.half(), b.half()) for a, b in zip(ref, autre))
    ecart = max(float((a - b).abs().max()) for a, b in zip(ref, autre))
    return {"taches_identiques": egales, "taches_identiques_demi_precision": egales16, "taches": len(ref), "ecart_max": ecart}


def produit_bf16(device, d: int = 4096, entropie: int = ENTROPIE_AUDIT) -> dict:
    """Témoin informatif (non décisif) : un produit matriciel bf16 de 2 lignes et de 128 lignes, comparé sur ses 2 premières lignes."""
    import torch
    g = torch.Generator().manual_seed(entropie)
    w = torch.randn(d, d, generator=g).to(torch.bfloat16).to(device)
    x = torch.randn(128, d, generator=g).to(torch.bfloat16).to(device)
    a, b = (x[:2] @ w).float().cpu(), (x @ w)[:2].float().cpu()
    return {"identiques": bool(torch.equal(a, b)), "ecart_max": float((a - b).abs().max())}


def mesurer(model, lm_head, vocab: int, n_neurones: int, device, couches=COUCHES, lots=LOTS, n: int = N_TACHES) -> dict:
    """Le cœur de l'essai, indépendant du chargement (essayé sur processeur avec un Llama miniature)."""
    jobs = taches(vocab, n_neurones, n)
    res = {"couches": {}, "n_taches": n, "lots": list(lots), "entropie": ENTROPIE_AUDIT,
           "longueurs": [len(j["ids"]) for j in jobs]}
    for c in couches:
        formes = {}
        series = {}
        for lot in lots:
            formes[lot] = []
            series[lot] = differences(model, lm_head, c, jobs, lot, device, formes[lot])
        ref = series[lots[0]]
        rejeu = differences(model, lm_head, c, jobs, lots[0], device)
        rejeu64 = differences(model, lm_head, c, jobs, 64, device) if 64 in lots else None
        perturbes = [dict(j) for j in jobs]
        perturbes[0] = dict(jobs[0], ids=list(jobs[0]["ids"]))
        perturbes[0]["ids"][0] = (perturbes[0]["ids"][0] + 1)
        pert = differences(model, lm_head, c, perturbes, lots[0], device)
        res["couches"][str(c)] = {
            "empreintes_lot_ref": [empreinte(t) for t in ref],
            "par_lot": {str(lot): comparer(ref, series[lot]) | {"formes": sorted({tuple(f) for f in formes[lot]})}
                        for lot in lots},
            "C2_perturbation": {"tache0_change": empreinte(pert[0]) != empreinte(ref[0]),
                                "autres_identiques": sum(empreinte(a) == empreinte(b) for a, b in zip(ref[1:], pert[1:])),
                                "autres": len(ref) - 1},
            "C3_rejeu": comparer(ref, rejeu),
            "C3b_rejeu_lot64": comparer(series[64], rejeu64) if rejeu64 is not None else None,
            "C4_ablation_agit": {"taches_non_nulles": sum(float(t.abs().max()) > 0 for t in ref), "taches": len(ref)}}
    res["temoin_produit_bf16"] = produit_bf16(device)
    return res


def lire_issue(res: dict) -> dict:
    """Lecture préenregistrée (§ 4 du préenregistrement), appliquée par programme ; rapportée, la lecture finale revient au lecteur."""
    c1 = all(set(map(tuple, r["par_lot"]["16"]["formes"])) != set(map(tuple, r["par_lot"]["64"]["formes"]))
             for r in res["couches"].values())
    c2 = all(r["C2_perturbation"]["tache0_change"] and r["C2_perturbation"]["autres_identiques"] == r["C2_perturbation"]["autres"]
             for r in res["couches"].values())
    c3 = all(r["C3_rejeu"]["taches_identiques"] == r["C3_rejeu"]["taches"] for r in res["couches"].values())
    c3b = all(r["C3b_rejeu_lot64"] is not None and r["C3b_rejeu_lot64"]["taches_identiques"] == r["C3b_rejeu_lot64"]["taches"]
              for r in res["couches"].values())
    c4 = all(r["C4_ablation_agit"]["taches_non_nulles"] >= SEUIL_C4 * r["C4_ablation_agit"]["taches"] for r in res["couches"].values())
    ident = all(r["par_lot"]["64"]["taches_identiques"] == r["par_lot"]["64"]["taches"] for r in res["couches"].values())
    if not (c1 and c2 and c3 and c3b and c4):  # tous les témoins exigés pour les deux issues décisives (v2)
        issue = "indéterminé"
    elif ident:
        issue = "invariance établie"
    else:
        issue = "invariance réfutée"
    return {"C1_formes_differentes": c1, "C2_perturbation_vue": c2, "C3_rejeu_identique": c3, "C3b_rejeu_lot64_identique": c3b,
            "C4_ablation_agit": c4, "lot64_identique_au_lot16": ident, "issue": issue}


def charger_reel(voisin, nom: str, device: str):
    """Chargement comme `measure` (copie publiée, l. 109-113) : `from_pretrained(…, dtype=bfloat16)`, `.to(device).eval()`,
    `decoder_stack` du dépôt voisin (exécuté sur la machine louée seulement, règle de Lazar R-2710)."""
    import torch
    from transformers import AutoModelForCausalLM
    if str(voisin) not in sys.path:
        sys.path.insert(0, str(voisin))
    lm = AutoModelForCausalLM.from_pretrained(nom, dtype=torch.bfloat16).to(device).eval()
    lm.requires_grad_(False)
    from neuron_lens.transport import decoder_stack
    carte = torch.cuda.get_device_name(0) if device == "cuda" else "processeur"
    return decoder_stack(lm), lm.lm_head, device, carte


def etape_audit_invariance(ctx: base.Contexte, charger=None) -> dict:
    import torch
    model, lm_head, device, carte = (charger or (lambda: charger_reel(ctx.voisin, base.LLAMA, "cuda")))()
    if charger is None and CARTE not in carte:
        raise base.Arret(f"carte inattendue pour l'essai : {carte}")
    cfg = model.config
    res = mesurer(model, lm_head, cfg.vocab_size, cfg.intermediate_size, device)
    versions = {"torch": torch.__version__, "cuda": getattr(torch.version, "cuda", None),
                "cudnn": torch.backends.cudnn.version() if torch.backends.cudnn.is_available() else None,
                "attention": getattr(cfg, "_attn_implementation", None)}
    try:
        import transformers
        versions["transformers"] = transformers.__version__
    except ImportError:
        pass
    prereg = ctx.racine / PREREG
    sortie = ctx.diag / "audit-invariance-lot-v2.json"
    sortie.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    from controle_ia.scellement import sceller
    return {"carte": carte, "versions": versions, "lecture_par_programme": lire_issue(res),
            "preenregistrement": {"chemin": PREREG, "sha256": base.sha256(prereg) if prereg.exists() else None},
            "graine": {"entropie": ENTROPIE_AUDIT, "outil": "numpy.random.SeedSequence"},
            "manifeste_note": "manifeste de la machine du lanceur v5 (configuration B-α) ; l'essai est décrit ici et au préenregistrement",
            "detail": {"chemin": str(sortie.relative_to(ctx.racine)), "sha256": sceller(sortie)},
            "note": "brut : la lecture finale revient à un lecteur neuf, sur le préenregistrement scellé"}


def installer():
    """Pose les quatre étapes dans la machine du lanceur v5 (ses fonctions lisent ces tables globales)."""
    base.ETAPES = ETAPES
    base.PREREQUIS = PREREQUIS
    base.ECHEANCES = ECHEANCES
    base.AUDITS = {}
    base.ETAPE_FONCTIONS = {e: base.ETAPE_FONCTIONS[e] for e in ETAPES[:-1]} | {"audit-invariance": etape_audit_invariance}


def main(argv=None):
    installer()
    base.main(argv)


if __name__ == "__main__":
    main()
