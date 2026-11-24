#!/usr/bin/env python3
"""Calcul reproductible du devis de la passe de recalcul des activations (saboteur voie A, GO-2026-11-23-39).

Ce script lit le releve brut des offres du loueur Vast.ai (en lecture seule),
calcule l'empreinte memoire video, les tailles de livraison (regle RP-7),
les durees et les couts (attendu, haut, pire cas, relance technique, comparaison 48 Go),
et eprouve les regles de coupure et de plafond sur des objets de controle (regle R5).
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

DOSSIER = Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/devis-rejeu-saboteur-go39"
)
FICHIER_RELEVE = DOSSIER / "releve-offres-vast-2026-11-24-v1.json"


def taille_livraison_rp7(n_actions: int, j_max: int) -> dict[str, int]:
    """Calcule la taille de pire cas selon la regle RP-7 de l'additif 1."""
    borne_totale = 2_000_000_000
    reserve_trace = 4_000_000
    borne_fichiers_1_a_4 = borne_totale - reserve_trace
    for k in range(1, 100):
        pas15 = 16 * k
        pas7 = 128 * k
        n15 = ((n_actions - 1) // pas15) + 1
        if (n_actions - 1) % pas15 != 0:
            n15 += 1
        n7 = ((n_actions - 1) // pas7) + 1
        if (n_actions - 1) % pas7 != 0:
            n7 += 1
        scores_actions = 38_544 * n_actions
        scores_jetons = 72 * n_actions * j_max
        brut_c15 = 16_384 * j_max * n15
        brut_c7_c23_chacune = 16_384 * j_max * n7
        w_k = scores_actions + scores_jetons + brut_c15 + 2 * brut_c7_c23_chacune
        index_et_meta = 1_000 * n_actions + 1_000_000
        if w_k + index_et_meta <= borne_fichiers_1_a_4:
            plus_grosse = max(scores_actions, scores_jetons, brut_c15, brut_c7_c23_chacune)
            place_libre = math.ceil((borne_totale + plus_grosse) / 100_000_000) * 100_000_000
            return {
                "k": k,
                "n15": n15,
                "n7": n7,
                "scores_actions_octets": scores_actions,
                "scores_jetons_octets": scores_jetons,
                "brut_c15_octets": brut_c15,
                "brut_c7_ou_c23_octets": brut_c7_c23_chacune,
                "w_k_octets": w_k,
                "total_avec_meta_octets": w_k + index_et_meta + reserve_trace,
                "marge_octets": borne_totale - (w_k + index_et_meta + reserve_trace),
                "place_libre_p9_octets": place_libre,
            }
    raise RuntimeError("Aucun pas k ne tient la borne de 2 Go")


def memoire_video_go(
    lot: int,
    longueur_seq: int,
    j_max: int = 400,
    logits_fp32_complets: bool = False,
) -> dict[str, float]:
    """Estime la memoire video (en gigaoctets decimaux, 1 Go = 10^9 octets) pour Llama-3.1-8B-Instruct."""
    poids_base = 8.03e9 * 2 / 1e9  # bfloat16
    adaptateur_fp32 = 13_631_488 * 4 / 1e9  # 32 couches * (2*16*8192 + 2*16*5120) en float32
    sondes_fp64 = 2_409 * 4_096 * 8 / 1e9
    # MLP intermediaire (dimension 14336, gate + up en bfloat16) + etats caches
    activations_bloc = lot * longueur_seq * (2 * 14_336 + 4_096) * 2 / 1e9
    # Captures aux 3 couches en float32 sur les seuls jetons d'action
    captures_3_couches = 3 * lot * j_max * 4_096 * 4 / 1e9
    # Logits de sortie (vocabulaire 128 256)
    octets_logit = 4 if logits_fp32_complets else 2
    logits = lot * longueur_seq * 128_256 * octets_logit / 1e9
    reserve_cuda = 2.0
    total = (
        poids_base
        + adaptateur_fp32
        + sondes_fp64
        + activations_bloc
        + captures_3_couches
        + logits
        + reserve_cuda
    )
    return {
        "poids_base_go": round(poids_base, 2),
        "adaptateur_fp32_go": round(adaptateur_fp32, 3),
        "sondes_fp64_go": round(sondes_fp64, 3),
        "activations_bloc_go": round(activations_bloc, 2),
        "captures_3_couches_go": round(captures_3_couches, 2),
        "logits_go": round(logits, 2),
        "reserve_cuda_go": reserve_cuda,
        "total_go": round(total, 2),
    }


def cout_scenario(
    nom: str,
    t_mise_en_place_h: float,
    s_par_action: float,
    t_ecriture_scores_h: float,
    t_poussee_verif_h: float,
    n_actions: int,
    n_p10: int,
    n_p7: int,
    s_extra_p7: float,
    prix_carte_h: float,
    stockage_gb_mois: float,
    disque_go: int,
    entrant_go: float,
    tarif_entrant_go: float,
    sortant_go: float,
    tarif_sortant_go: float,
) -> dict[str, float | str]:
    t_p10_h = (n_p10 * s_par_action) / 3600.0
    t_passe_h = (n_actions * s_par_action) / 3600.0
    t_p7_h = (n_p7 * s_par_action + s_extra_p7) / 3600.0
    t_total_h = t_mise_en_place_h + t_p10_h + t_passe_h + t_p7_h + t_ecriture_scores_h + t_poussee_verif_h

    # Convention Vast.ai : 720 heures par mois (30 jours) pour le stockage horaire
    # Verification sur la course voie A : 0.24 * 100 / 720 = 0.03333 USD/h (exactement 0.0333 USD/h releve)
    prix_stockage_h = stockage_gb_mois * disque_go / 720.0
    cout_carte = t_total_h * prix_carte_h
    cout_stockage = t_total_h * prix_stockage_h
    cout_entrant = entrant_go * tarif_entrant_go
    cout_sortant = sortant_go * tarif_sortant_go
    cout_total = cout_carte + cout_stockage + cout_entrant + cout_sortant

    return {
        "scenario": nom,
        "t_mise_en_place_h": round(t_mise_en_place_h, 3),
        "t_p10_h": round(t_p10_h, 3),
        "t_passe_h": round(t_passe_h, 3),
        "t_p7_h": round(t_p7_h, 3),
        "t_ecriture_scores_h": round(t_ecriture_scores_h, 3),
        "t_poussee_verif_h": round(t_poussee_verif_h, 3),
        "t_total_h": round(t_total_h, 3),
        "prix_carte_h": round(prix_carte_h, 4),
        "prix_stockage_h": round(prix_stockage_h, 4),
        "cout_carte_usd": round(cout_carte, 2),
        "cout_stockage_usd": round(cout_stockage, 2),
        "cout_entrant_usd": round(cout_entrant, 2),
        "cout_sortant_usd": round(cout_sortant, 2),
        "cout_total_usd": round(cout_total, 2),
    }


def main() -> None:
    brut = FICHIER_RELEVE.read_bytes()
    sha_releve = hashlib.sha256(brut).hexdigest()
    offres = json.loads(brut.decode("utf-8")).get("offers", [])

    print("=== BLOC 1 : RELEVE DES OFFRES VAST.AI (2026-11-24T03:44:56Z) ===")
    print(f"fichier: {FICHIER_RELEVE.name}")
    print(f"sha256:  {sha_releve}")
    print(f"offres_totales: {len(offres)}")
    familles = {}
    for o in offres:
        cle = f"{o.get('gpu_name')} ({int(round(o.get('gpu_ram', 0) / 1024))} Go)"
        familles.setdefault(cle, []).append(o)
    for k in [
        "A100 SXM4 (80 Go)",
        "A100 PCIE (80 Go)",
        "L40S (48 Go)",
        "L40S (45 Go)",
        "RTX A6000 (48 Go)",
        "RTX 4090 (24 Go)",
    ]:
        xs = sorted(familles.get(k, []), key=lambda x: x.get("dph_total", 999))
        print(f"  {k}: n={len(xs)}")
        for x in xs[:3]:
            st_100_h = x.get("storage_cost", 0) * 100 / 720.0
            print(
                f"    id={x.get('id')} dph_total={x.get('dph_total'):.4f} "
                f"dph_base={x.get('dph_base'):.4f} st_gb_mo={x.get('storage_cost'):.4f} "
                f"st_100g_h={st_100_h:.4f} down_gb={x.get('inet_down_cost'):.5f} "
                f"up_gb={x.get('inet_up_cost'):.5f} rel={x.get('reliability2'):.3f}"
            )

    print("\n=== BLOC 2 : TAILLES DE LIVRAISON (REGLE RP-7, EFFECTIFS V6 = 2 560 ACTIONS, J = 400) ===")
    rp7 = taille_livraison_rp7(2560, 400)
    for k, v in rp7.items():
        print(f"  {k}: {v}")

    print("\n=== BLOC 3 : EMPREINTE MEMOIRE VIDEO (LOT L = 8, LLAMA-3.1-8B-INSTRUCT) ===")
    for nom, seq, fp32_logits in [
        ("contexte_court_2000_bfloat16", 2000, False),
        ("contexte_moyen_3500_bfloat16", 3500, False),
        ("contexte_long_6000_bfloat16", 6000, False),
        ("contexte_long_6000_logits_fp32_complets", 6000, True),
        ("contexte_extreme_8192_bfloat16", 8192, False),
    ]:
        m = memoire_video_go(8, seq, 400, fp32_logits)
        print(f"  {nom}: {m}")

    print("\n=== BLOC 4 : SCENARIOS DE DUREE ET DE COUT (A100 SXM4 80 Go, DISQUE 100 Go) ===")
    n_actions = 2560
    n_p10 = 4 * rp7["n15"]  # 4 * 161 = 644 passes (contexte reel, decale, + artefact)
    n_p7 = rp7["n15"]  # 161 passes en ordre inverse
    scenarios = [
        cout_scenario(
            nom="attendu_a100_sxm4_80go",
            t_mise_en_place_h=0.40,
            s_par_action=0.40,
            t_ecriture_scores_h=0.15,
            t_poussee_verif_h=0.25,
            n_actions=n_actions,
            n_p10=n_p10,
            n_p7=n_p7,
            s_extra_p7=20.0,
            prix_carte_h=1.14,
            stockage_gb_mois=0.24,
            disque_go=100,
            entrant_go=40.0,
            tarif_entrant_go=0.0390625,  # tarif observe sur la course voie A (1.5625 USD pour 40 Go)
            sortant_go=1.51,
            tarif_sortant_go=0.0390625,
        ),
        cout_scenario(
            nom="haut_a100_sxm4_80go",
            t_mise_en_place_h=0.75,
            s_par_action=0.85,
            t_ecriture_scores_h=0.30,
            t_poussee_verif_h=0.45,
            n_actions=n_actions,
            n_p10=n_p10,
            n_p7=n_p7,
            s_extra_p7=40.0,
            prix_carte_h=1.30,
            stockage_gb_mois=0.40,
            disque_go=100,
            entrant_go=45.0,
            tarif_entrant_go=0.0390625,
            sortant_go=2.00,
            tarif_sortant_go=0.0390625,
        ),
        cout_scenario(
            nom="pire_cas_a100_80go",
            t_mise_en_place_h=1.25,
            s_par_action=1.60,
            t_ecriture_scores_h=0.50,
            t_poussee_verif_h=0.75,
            n_actions=n_actions,
            n_p10=n_p10,
            n_p7=n_p7,
            s_extra_p7=90.0,
            prix_carte_h=1.45,
            stockage_gb_mois=1.00,
            disque_go=100,
            entrant_go=55.0,
            tarif_entrant_go=0.0500,
            sortant_go=2.50,
            tarif_sortant_go=0.0500,
        ),
        cout_scenario(
            nom="comparatif_attendu_l40s_48go",
            t_mise_en_place_h=0.40,
            s_par_action=0.55,  # non mesure sur cette chaine, bande passante memoire plus faible
            t_ecriture_scores_h=0.15,
            t_poussee_verif_h=0.25,
            n_actions=n_actions,
            n_p10=n_p10,
            n_p7=n_p7,
            s_extra_p7=25.0,
            prix_carte_h=0.8022,
            stockage_gb_mois=0.20,
            disque_go=100,
            entrant_go=40.0,
            tarif_entrant_go=0.0390625,
            sortant_go=1.51,
            tarif_sortant_go=0.0390625,
        ),
    ]
    for sc in scenarios:
        print(f"  {sc}")

    print("\n=== BLOC 5 : VERIFICATION PLAFOND ET COUPURES DURES (OBJETS DE CONTROLE R5) ===")
    plafond_provisoire_go39 = 15.00
    plafond_propose = 11.00
    coupure_dure_instance_usd = 10.00
    coupure_dure_horloge_h = 4.5
    marge_quart_heure_usd = 0.25 * (1.45 + 1.00 * 100 / 720.0)
    seuil_declenchement_arret_usd = round(coupure_dure_instance_usd - marge_quart_heure_usd, 2)
    credit_vast_releve_r5215 = 20.42

    print(f"  plafond_provisoire_go39_usd: {plafond_provisoire_go39:.2f}")
    print(f"  plafond_propose_usd: {plafond_propose:.2f}")
    print(f"  reduction_plafond_usd: {plafond_provisoire_go39 - plafond_propose:.2f}")
    print(f"  coupure_dure_instance_usd: {coupure_dure_instance_usd:.2f}")
    print(f"  marge_quart_heure_pire_tarif_usd: {marge_quart_heure_usd:.2f}")
    print(f"  seuil_declenchement_arret_usd: {seuil_declenchement_arret_usd:.2f}")
    print(f"  coupure_dure_horloge_h: {coupure_dure_horloge_h:.1f}")
    print(f"  credit_vast_r5215_usd: {credit_vast_releve_r5215:.2f}")
    print(f"  recharge_requise_sous_plafond_propose: {credit_vast_releve_r5215 < plafond_propose}")

    # Objets de controle R5 sur la regle de coupure et de plafond
    tests_r5 = [
        ("cas_sain_attendu", scenarios[0]["cout_total_usd"], scenarios[0]["t_total_h"], True),
        ("cas_sain_haut", scenarios[1]["cout_total_usd"], scenarios[1]["t_total_h"], True),
        ("cas_sain_pire_cas_unique", scenarios[2]["cout_total_usd"], scenarios[2]["t_total_h"], True),
        (
            "artefact_hote_bloque_8h",
            round(8.0 * (1.45 + 1.00 * 100 / 720.0) + 2.75, 2),
            8.0,
            False,
        ),
        (
            "artefact_instance_oubliee_24h",
            round(24.0 * (1.14 + 0.24 * 100 / 720.0) + 1.56, 2),
            24.0,
            False,
        ),
        (
            "artefact_stockage_hors_filtre_et_horloge_5h",
            round(5.0 * (1.45 + 1.00 * 100 / 720.0) + 2.88, 2),
            5.0,
            False,
        ),
    ]
    for nom_t, cout_t, duree_t, attendu_ok in tests_r5:
        ok = (cout_t <= coupure_dure_instance_usd) and (duree_t <= coupure_dure_horloge_h) and (cout_t <= plafond_propose)
        assert ok == attendu_ok, f"Echec objet de controle {nom_t}: ok={ok}, attendu={attendu_ok}"
        print(
            f"  [R5 OK] {nom_t}: cout={cout_t:.2f} USD, duree={duree_t:.2f} h, "
            f"conforme_coupures={ok} (attendu={attendu_ok})"
        )

    # Verification d'une relance technique unique sous plafond provisoire 15 USD vs plafond abaisse 11 USD
    cout_relance_incident_1h_puis_haut = round(
        (1.0 * (1.14 + 0.24 * 100 / 720.0) + 1.56) + scenarios[1]["cout_total_usd"], 2
    )
    print(
        f"  relance_unique_incident_1h_puis_haut_usd: {cout_relance_incident_1h_puis_haut:.2f} "
        f"(sous_11={cout_relance_incident_1h_puis_haut <= 11.0}, sous_15={cout_relance_incident_1h_puis_haut <= 15.0})"
    )


if __name__ == "__main__":
    main()
