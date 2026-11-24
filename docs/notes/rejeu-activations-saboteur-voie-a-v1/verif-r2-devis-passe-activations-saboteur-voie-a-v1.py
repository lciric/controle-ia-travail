#!/usr/bin/env python3
"""Script independant de contre-lecture (R2) du devis de la passe de recalcul des activations
du saboteur a budget, voie (A) (GO-2026-11-23-39, R-5211).

Execution obligatoire avec PYTHONDONTWRITEBYTECODE=1.
Aucune ecriture dans le depot Git, aucun appel reseau, aucune creation de machine.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

DOSSIER_DEVIS = Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/devis-rejeu-saboteur-go39"
)
DEPOT_GIT = Path("/home/antigravity/lciric/controle-ia-travail")


def sha256_octets(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verifier_empreintes() -> None:
    print("=== 1. VERIFICATION INDEPENDANTE DES EMPREINTES SHA-256 ===")
    fichiers_devis = [
        "devis-passe-activations-saboteur-voie-a-v1.md",
        "calcul-devis-passe-activations-saboteur-voie-a-v1.py",
        "sortie-calcul-devis-passe-activations-saboteur-voie-a-v1.txt",
        "releve-offres-vast-2026-11-24-v1.json",
    ]
    for nom in fichiers_devis:
        f = DOSSIER_DEVIS / nom
        comp = DOSSIER_DEVIS / f"{nom}.sha256"
        digest = sha256_octets(f.read_bytes())
        ligne_comp = comp.read_text(encoding="utf-8").strip()
        attendu_comp = ligne_comp.split()[0]
        nom_comp = ligne_comp.split()[1]
        assert digest == attendu_comp, f"Ecart SHA-256 sur {nom}: {digest} != {attendu_comp}"
        assert nom_comp == nom, f"Nom compagnon inattendu: {nom_comp} != {nom}"
        print(f"  [OK] {nom}: {digest}")

    # Verification de reproductibilite exacte de la sortie du script du redacteur
    sortie_rejouee = subprocess.check_output(
        ["python3", str(DOSSIER_DEVIS / "calcul-devis-passe-activations-saboteur-voie-a-v1.py")],
        cwd=str(DOSSIER_DEVIS),
        env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"},
    )
    sha_rejouee = sha256_octets(sortie_rejouee)
    sha_sortie_figee = sha256_octets(
        (DOSSIER_DEVIS / "sortie-calcul-devis-passe-activations-saboteur-voie-a-v1.txt").read_bytes()
    )
    assert sha_rejouee == sha_sortie_figee, "La sortie du script du redacteur n'est pas reproductible a l'octet !"
    print(f"  [OK] Rejeu exact du script redacteur == sortie figee ({sha_rejouee})")

    # Verification des pieces de reference citees dans le devis avec empreinte
    refs_git = [
        (
            "faits-cote-expose-pour-devis-rejeu-v1.md",
            ["git", "show", "origin/claude/iib-executante-v7:registres/iib-executante/rejeu-activations-v1/faits-cote-expose-pour-devis-rejeu-v1.md"],
            "e381e60e89986ea57bfb707959f447ee6a5d18715be299e9a6dd741de5130eed",
        ),
        (
            "lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md",
            ["git", "show", "origin/prep/additif-sondes-barreau8-scellement-v1:prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md"],
            "eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b",
        ),
    ]
    for label, cmd, attendu in refs_git:
        contenu = subprocess.check_output(cmd, cwd=str(DEPOT_GIT))
        d = sha256_octets(contenu)
        assert d == attendu, f"Ecart SHA-256 sur {label}: {d} != {attendu}"
        print(f"  [OK] {label}: {d}")

    refs_disque = [
        (
            "prereg/lecture-sondes-barreau8-v1.md",
            "8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4",
        ),
        (
            "docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md",
            "20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1",
        ),
    ]
    for rel, attendu in refs_disque:
        d = sha256_octets((DEPOT_GIT / rel).read_bytes())
        assert d == attendu, f"Ecart SHA-256 sur {rel}: {d} != {attendu}"
        print(f"  [OK] {rel}: {d}")


def verifier_memoire_llama31_8b() -> None:
    print("\n=== 2. RECALCUL INDEPENDANT DE L'EMPREINTE MEMOIRE (LLAMA-3.1-8B-INSTRUCT) ===")
    # Architecture exacte de meta-llama/Llama-3.1-8B-Instruct (interface v6, question 1)
    n_couches = 32
    d_model = 4096
    n_kv_heads = 8
    d_head = 128
    d_kv = n_kv_heads * d_head  # 1024
    d_ff = 14336  # SwiGLU
    vocab = 128256
    rang_lora = 16

    params_embed_et_tete = 2 * vocab * d_model  # 1 050 673 152
    params_attn_par_couche = d_model * (d_model + d_kv + d_kv + d_model)  # 41 943 040
    params_mlp_par_couche = 3 * d_model * d_ff  # 176 160 768
    params_norm_par_couche = 2 * d_model  # 8 192
    params_totaux = (
        params_embed_et_tete
        + n_couches * (params_attn_par_couche + params_mlp_par_couche + params_norm_par_couche)
        + d_model
    )
    poids_bf16_go = params_totaux * 2 / 1e9

    # Adaptateurs LoRA (q_proj, k_proj, v_proj, o_proj, rang 16)
    params_lora_par_couche = (
        rang_lora * (d_model + d_model)  # q_proj
        + rang_lora * (d_model + d_kv)   # k_proj
        + rang_lora * (d_model + d_kv)   # v_proj
        + rang_lora * (d_model + d_model) # o_proj
    )
    params_lora_totaux = n_couches * params_lora_par_couche  # 13 631 488
    lora_fp16_octets = params_lora_totaux * 2
    lora_fp32_go = params_lora_totaux * 4 / 1e9

    # 2 409 directions + biais en float64
    sondes_fp64_go = 2409 * (d_model + 1) * 8 / 1e9

    print(f"  parametres_exact_llama31_8b: {params_totaux:,} -> {poids_bf16_go:.4f} Go en bfloat16")
    print(
        f"  parametres_exact_lora_r16: {params_lora_totaux:,} -> {lora_fp16_octets:,} octets en float16 "
        f"(fichiers verses: 27 347 935 et 27 350 031 octets), {lora_fp32_go:.4f} Go en float32"
    )
    print(f"  sondes_et_planchers_fp64: {sondes_fp64_go:.4f} Go")

    # Capacites physiques en Go decimaux (1 Mio = 1 048 576 octets, d'apres gpu_ram du releve Vast.ai)
    vram_rtx4090_go = 24564 * 1024 * 1024 / 1e9   # 25.757 Go (24 Gio)
    vram_l40s_45_go = 46068 * 1024 * 1024 / 1e9   # 48.306 Go
    vram_l40s_48_go = 49140 * 1024 * 1024 / 1e9   # 51.527 Go
    vram_a100_80_go = 81920 * 1024 * 1024 / 1e9   # 85.899 Go (80 Gio)
    print(
        f"  VRAM physique (Go decimaux = 10^9 octets): RTX 4090={vram_rtx4090_go:.2f} Go | "
        f"L40S={vram_l40s_45_go:.2f}-{vram_l40s_48_go:.2f} Go | A100 80Go={vram_a100_80_go:.2f} Go"
    )

    lot = 8
    j_max = 400
    reserve_go = 2.0
    captures_tranchees_go = 3 * lot * j_max * d_model * 4 / 1e9

    for seq in [2000, 2500, 3500, 6000, 8192]:
        # Modele du devis (2 * d_ff + d_model)
        act_devis_go = lot * seq * (2 * d_ff + d_model) * 2 / 1e9
        # Modele PyTorch strict (SwiGLU garde temporairement gate, silu(gate) et up + flux residuel, + cast fp32 entree LoRA)
        act_pytorch_strict_go = lot * seq * (3 * d_ff + d_model) * 2 / 1e9 + (lot * seq * d_model * 4 / 1e9)
        logits_bf16_go = lot * seq * vocab * 2 / 1e9
        logits_fp32_go = lot * seq * vocab * 4 / 1e9
        # Sur P10, si logits.float() puis log_softmax() sont appeles sur toute la sequence sans trancher:
        # coexistence transitoire bf16 + fp32 (voire + sortie log_softmax fp32)
        pic_p10_coexistence_bf16_fp32_go = (
            poids_bf16_go + lora_fp32_go + sondes_fp64_go + act_devis_go
            + captures_tranchees_go + logits_bf16_go + logits_fp32_go + reserve_go
        )
        tot_bf16_devis = (
            poids_bf16_go + lora_fp32_go + sondes_fp64_go + act_devis_go
            + captures_tranchees_go + logits_bf16_go + reserve_go
        )
        tot_fp32_devis = (
            poids_bf16_go + lora_fp32_go + sondes_fp64_go + act_devis_go
            + captures_tranchees_go + logits_fp32_go + reserve_go
        )
        tot_bf16_strict = (
            poids_bf16_go + lora_fp32_go + sondes_fp64_go + act_pytorch_strict_go
            + captures_tranchees_go + logits_bf16_go + reserve_go
        )
        print(
            f"  S={seq:4d} | devis_bf16={tot_bf16_devis:5.2f} Go | strict_bf16={tot_bf16_strict:5.2f} Go | "
            f"devis_logits_fp32={tot_fp32_devis:5.2f} Go | pic_P10_bf16+fp32={pic_p10_coexistence_bf16_fp32_go:5.2f} Go "
            f"| tient_24Go={tot_bf16_strict < vram_rtx4090_go} | tient_80Go={pic_p10_coexistence_bf16_fp32_go < vram_a100_80_go}"
        )


def verifier_passes_et_rp7() -> None:
    print("\n=== 3. RECALCUL INDEPENDANT DES PASSES AVANT ET DE LA TAILLE DE LIVRAISON (RP-7) ===")
    t_taches, k_cond, e_ep, a_pas, j_max = 64, 4, 1, 10, 400
    n_actions = t_taches * k_cond * e_ep * a_pas
    assert n_actions == 2560

    # Verification par simulation directe des indices de rangs 0 .. N-1 (RP-7)
    rangs = list(range(n_actions))
    for k in range(1, 100):
        idx_15 = sorted(set(r for r in rangs if r % (16 * k) == 0) | {n_actions - 1})
        idx_7 = sorted(set(r for r in rangs if r % (128 * k) == 0) | {n_actions - 1})
        n15, n7 = len(idx_15), len(idx_7)
        s_act = 2409 * 2 * 8 * n_actions        # 38 544 * N
        s_jet = 9 * 8 * n_actions * j_max       # 72 * N * J
        b_15 = 4096 * 4 * j_max * n15           # 16 384 * J * n15
        b_7 = 4096 * 4 * j_max * n7             # 16 384 * J * n7
        b_23 = 4096 * 4 * j_max * n7
        w_k = s_act + s_jet + b_15 + b_7 + b_23
        seuil_rp7 = w_k + 1000 * n_actions + 1_000_000
        if seuil_rp7 <= 1_996_000_000:
            break
    else:
        raise AssertionError("Aucun k ne tient RP-7")

    nb_morceaux = sum(math.ceil(sz / 50_000_000) for sz in [s_act, s_jet, b_15, b_7, b_23])
    plus_grosse = max(s_act, s_jet, b_15, b_7)
    place_libre = math.ceil((2_000_000_000 + plus_grosse) / 100_000_000) * 100_000_000
    total_pire_cas = seuil_rp7 + 4_000_000
    marge = 2_000_000_000 - total_pire_cas

    assert (k, n15, n7) == (1, 161, 21)
    assert w_k == 1_502_781_440
    assert total_pire_cas == 1_510_341_440
    assert marge == 489_658_560
    assert place_libre == 3_100_000_000
    assert nb_morceaux == 32

    print(f"  [OK] RP-7: k={k}, n15={n15}, n7={n7}, W(1)={w_k:,} octets, nb_morceaux_50Mo={nb_morceaux}")
    print(f"  [OK] Total pire cas={total_pire_cas:,} octets, marge={marge:,} octets, place_libre_P9={place_libre:,} octets")

    # Comptage des passes avant et des lots de L=8
    lots_principale = 4 * math.ceil((n_actions // 4) / 8)  # 4 * 80 = 320 lots
    # Dans le tri lexicographique des cles evaluation-{B100,B50,H,TJ100}/..., chaque condition occupe 640 rangs contigus
    par_cond_n15 = [sum(1 for r in idx_15 if c * 640 <= r < (c + 1) * 640) for c in range(4)]
    lots_par_passe_n15 = sum(math.ceil(x / 8) for x in par_cond_n15)
    passes_p10_sans_cache = 4 * n15  # (i), (ii), (i'), (ii')
    passes_p10_avec_cache = 3 * n15  # si (i') reutilise (ii)
    passes_p7 = n15
    total_passes_sans_cache = passes_p10_sans_cache + n_actions + passes_p7
    total_passes_avec_cache = passes_p10_avec_cache + n_actions + passes_p7

    print(
        f"  [OK] Repartition n15 par condition={par_cond_n15} -> {lots_par_passe_n15} lots par passe sur sous-echantillon"
    )
    print(
        f"  [OK] Passes d'actions: P10={passes_p10_sans_cache} (ou {passes_p10_avec_cache} si (ii)=(i') reutilise), "
        f"principale={n_actions} ({lots_principale} lots), P7={passes_p7} ({lots_par_passe_n15} lots) "
        f"-> total={total_passes_sans_cache} (ou {total_passes_avec_cache})"
    )


def verifier_offres_et_couts() -> None:
    print("\n=== 4. VERIFICATION DES OFFRES VAST.AI, DES COUTS ET DES COUPURES P9 / R10 ===")
    offres = json.loads((DOSSIER_DEVIS / "releve-offres-vast-2026-11-24-v1.json").read_text(encoding="utf-8"))["offers"]
    assert len(offres) == 64

    # Verification complete par famille (sans troncature xs[:3] !)
    groupes: dict[str, list[dict]] = {}
    for o in offres:
        ram_gio = int(round(o["gpu_ram"] / 1024))
        groupes.setdefault(f"{o['gpu_name']} ({ram_gio} Go)", []).append(o)

    for fam in ["A100 SXM4 (80 Go)", "A100 PCIE (80 Go)", "L40S (48 Go)", "L40S (45 Go)", "RTX A6000 (48 Go)", "RTX 4090 (24 Go)"]:
        xs = sorted(groupes.get(fam, []), key=lambda x: x["dph_total"])
        dph_tot_min, dph_tot_max = xs[0]["dph_total"], xs[-1]["dph_total"]
        dph_base_min, dph_base_max = min(x["dph_base"] for x in xs), max(x["dph_base"] for x in xs)
        st_min = min(x["storage_cost"] * 100 / 720.0 for x in xs)
        st_max = max(x["storage_cost"] * 100 / 720.0 for x in xs)
        print(
            f"  {fam}: n={len(xs)} | dph_total=[{dph_tot_min:.4f}, {dph_tot_max:.4f}] | "
            f"dph_base=[{dph_base_min:.4f}, {dph_base_max:.4f}] | st_100Go_h=[{st_min:.4f}, {st_max:.4f}]"
        )

    # Verification du filtre du § 2.3 sur les offres A100 80 Go
    retenues = [
        o for o in offres
        if o["gpu_name"] in {"A100 SXM4", "A100 PCIE"}
        and int(round(o["gpu_ram"] / 1024)) == 80
        and o["verification"] == "verified"
        and not o["is_bid"]
        and o["reliability2"] >= 0.97
        and o["dph_total"] <= 1.35
        and o["storage_cost"] <= 0.40
        and o["inet_down_cost"] <= 0.04
        and o["cpu_ram"] >= 64000
        and o["cpu_cores_effective"] >= 12
        and o["disk_space"] >= 100
    ]
    print(f"  Offres A100 80 Go passant le filtre strict du § 2.3: {[ (o['id'], o['gpu_name'], round(o['dph_total'], 4)) for o in retenues ]}")

    # Recalcul independant des scenarios
    grille = [
        ("attendu", 0.40, 0.40, 20.0, 0.15, 0.25, 1.14, 0.24, 40.0, 0.0390625, 1.51, 0.0390625, 1.179, 3.01),
        ("haut",    0.75, 0.85, 40.0, 0.30, 0.45, 1.30, 0.40, 45.0, 0.0390625, 2.00, 0.0390625, 2.306, 4.96),
        ("pire_cas",1.25, 1.60, 90.0, 0.50, 0.75, 1.45, 1.00, 55.0, 0.0500000, 2.50, 0.0500000, 4.021, 9.26),
        ("l40s_cmp",0.40, 0.55, 25.0, 0.15, 0.25, 0.8022,0.20,40.0, 0.0390625, 1.51, 0.0390625, 1.321, 2.72),
    ]
    for nom, t_init, s_act, s_p7_ext, t_ecr, t_push, p_gpu, p_st_mo, g_in, c_in, g_out, c_out, h_att, usd_att in grille:
        t_h = t_init + (644 * s_act + 2560 * s_act + 161 * s_act + s_p7_ext) / 3600.0 + t_ecr + t_push
        p_st_h = p_st_mo * 100.0 / 720.0
        c_tot = t_h * (p_gpu + p_st_h) + g_in * c_in + g_out * c_out
        assert round(t_h, 3) == h_att, f"Ecart duree {nom}: {t_h:.4f} vs {h_att}"
        assert round(c_tot, 2) == usd_att, f"Ecart cout {nom}: {c_tot:.4f} vs {usd_att}"
        print(
            f"  [OK] Scenario {nom:8s}: duree={t_h:.4f} h (affiche {h_att:.3f}), "
            f"cout={c_tot:.4f} USD (affiche {usd_att:.2f}), dont horaire={t_h*(p_gpu+p_st_h):.4f} USD + reseau={g_in*c_in+g_out*c_out:.4f} USD"
        )

    # Verification P9 vs reseau a l'horloge dure de 4,5 h
    cout_4h5_filtre = 4.5 * (1.35 + 0.40 * 100 / 720.0) + 45.0 * 0.04 + 2.0 * 0.04
    cout_4h5_pire_tarif_hors_filtre = 4.5 * (1.45 + 1.00 * 100 / 720.0) + 55.0 * 0.05 + 2.5 * 0.05
    print(
        f"  Cout a la coupure horloge 4,5 h: sous filtre § 2.3 = {cout_4h5_filtre:.2f} USD (<= 10 USD) | "
        f"aux tarifs pire cas hors filtre sans coupure 9,60 USD = {cout_4h5_pire_tarif_hors_filtre:.2f} USD (> 10,00 USD de 0,03 USD !)"
    )


def verifier_forme_texte() -> None:
    print("\n=== 5. CONTROLE FORMEL DU TEXTE DU DEVIS (EMOJIS, ACRONYMES, CITATIONS R6/R7) ===")
    texte = (DOSSIER_DEVIS / "devis-passe-activations-saboteur-voie-a-v1.md").read_text(encoding="utf-8")
    # Verification zero emoji
    emojis = [ch for ch in texte if ord(ch) >= 0x1F000 or (0x2600 <= ord(ch) <= 0x27BF)]
    assert not emojis, f"Emojis detectes: {emojis}"
    print("  [OK] Zero emoji dans le devis.")

    # Verification des chemins .md / .py / .json du depot cites sans empreinte de 8 ou 64 caracteres a proximite
    lignes = texte.splitlines()
    for i, l in enumerate(lignes, 1):
        if "devis-adaptateurs-tenus-a-l-ecart-v1.md" in l or "devis-garde-activations-volume-v2.md" in l:
            has_hex = bool(re.search(r"\b[0-9a-f]{8,64}\b", l))
            print(f"  [ALERTE R6] Ligne {i}: piece du depot citee sans empreinte SHA-256: {l.strip()[:120]}... (has_hex={has_hex})")


if __name__ == "__main__":
    verifier_empreintes()
    verifier_memoire_llama31_8b()
    verifier_passes_et_rp7()
    verifier_offres_et_couts()
    verifier_forme_texte()
