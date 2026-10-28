"""Calculs de vérification des lemmes M2-a, M3-a, M3-b du document
« niveau-methode-classes-2-3-v1.md » — analytiques et synthétiques.

Aucune donnée du programme ; R9 : SeedSequence(2026102823), dérivée par bloc.
Dépendances : numpy ≥ 1.25, statistics (bibliothèque standard).

Usage : PYTHONPATH=src python -I -B calculs-niveau-methode-classes-2-3-v1.py > calculs-niveau-methode-classes-2-3-v1.sortie.txt
"""
import json
import sys
from statistics import NormalDist

import numpy as np

PHI = NormalDist().cdf  # Φ(x) = P(Z ≤ x)
Z = NormalDist().inv_cdf  # quantile de la loi normale centrée réduite
ALPHA = 0.05
Z_ALPHA = Z(1 - ALPHA)  # ≈ 1.645 pour un test unilatéral à 5 %
BETA_CIBLE = 0.80  # rappel cible


def rappel_gaussien(delta: float, sigma: float, T: int) -> float:
    """Rappel d'un test de somme sur T actions, décalage total delta, bruit sigma par action."""
    return PHI(delta / (sigma * T**0.5) - Z_ALPHA)


def main() -> None:
    ss = np.random.SeedSequence(2026102823)
    enfants = ss.spawn(6)  # un par bloc
    resultats: dict = {"graine_mere": 2026102823, "alpha": ALPHA, "z_alpha": round(Z_ALPHA, 6), "blocs": {}}

    # ──────────────────────────────────────────────────────────────────────
    # Bloc 1 — M3-a (a) : rappel par agent, dilution en N
    # ──────────────────────────────────────────────────────────────────────
    rng1 = np.random.default_rng(enfants[0])
    sigma, T, B = 1.0, 100, 20.0
    valeurs_N = [1, 2, 5, 10, 20, 50, 100]
    rappels_analytiques = []
    rappels_synthetiques = []
    n_tirages = 50_000

    for N in valeurs_N:
        delta_par_agent = B / N
        r_ana = rappel_gaussien(delta_par_agent, sigma, T)
        rappels_analytiques.append(round(r_ana, 6))

        # synthétique : N agents indépendants, chacun un décalage delta_par_agent / T par action
        dec_par_action = delta_par_agent / T
        scores = rng1.normal(dec_par_action, sigma, size=(n_tirages, T))
        sommes = scores.sum(axis=1)
        seuil = sigma * T**0.5 * Z_ALPHA
        r_syn = (sommes > seuil).mean()
        rappels_synthetiques.append(round(float(r_syn), 6))

    b1 = {
        "description": "M3-a (a) : rappel par agent quand B fixé est dilué sur N agents",
        "parametres": {"sigma": sigma, "T": T, "B": B, "tirages": n_tirages},
        "N": valeurs_N,
        "rappel_analytique": rappels_analytiques,
        "rappel_synthetique": rappels_synthetiques,
        "attendu": "rappel décroît vers alpha quand N croît",
    }
    resultats["blocs"]["M3a_dilution"] = b1
    print("Bloc 1 — M3-a (a) dilution :", json.dumps(b1, ensure_ascii=False, indent=1))

    # ──────────────────────────────────────────────────────────────────────
    # Bloc 2 — M3-a (c) : moniteur conjoint, budget nécessaire en √N
    # ──────────────────────────────────────────────────────────────────────
    rng2 = np.random.default_rng(enfants[1])
    rappels_conjoints_ana = []
    rappels_conjoints_syn = []
    budgets_necessaires_par_agent = []
    budgets_necessaires_conjoint = []

    for N in valeurs_N:
        # rappel du moniteur conjoint (somme sur N agents × T actions)
        r_conj = PHI(B / (sigma * (N * T) ** 0.5) - Z_ALPHA)
        rappels_conjoints_ana.append(round(r_conj, 6))

        # synthétique
        dec_par_action_par_agent = (B / N) / T  # chaque agent contribue B/N, réparti sur T actions
        scores_all = rng2.normal(dec_par_action_par_agent, sigma, size=(n_tirages, N * T))
        somme_totale = scores_all.sum(axis=1)
        seuil_conj = sigma * (N * T) ** 0.5 * Z_ALPHA
        r_syn_conj = (somme_totale > seuil_conj).mean()
        rappels_conjoints_syn.append(round(float(r_syn_conj), 6))

        # budget nécessaire pour beta = 0.80, par agent vs conjoint
        b_agent = N * sigma * T**0.5 * (Z_ALPHA + Z(BETA_CIBLE))
        b_conj = sigma * (N * T) ** 0.5 * (Z_ALPHA + Z(BETA_CIBLE))
        budgets_necessaires_par_agent.append(round(b_agent, 4))
        budgets_necessaires_conjoint.append(round(b_conj, 4))

    b2 = {
        "description": "M3-a (c) : moniteur conjoint — rappel et budget nécessaire",
        "parametres": {"sigma": sigma, "T": T, "B": B, "tirages": n_tirages},
        "N": valeurs_N,
        "rappel_conjoint_analytique": rappels_conjoints_ana,
        "rappel_conjoint_synthetique": rappels_conjoints_syn,
        "budget_necessaire_par_agent_beta_80": budgets_necessaires_par_agent,
        "budget_necessaire_conjoint_beta_80": budgets_necessaires_conjoint,
        "attendu": "budget par agent croît en N, budget conjoint en √N ; gain √N du conjoint",
    }
    resultats["blocs"]["M3a_conjoint"] = b2
    print("\nBloc 2 — M3-a (c) conjoint :", json.dumps(b2, ensure_ascii=False, indent=1))

    # ──────────────────────────────────────────────────────────────────────
    # Bloc 3 — M3-a (d) : plafond sous corrélation ρ_A (effet de plan de Kish)
    # ──────────────────────────────────────────────────────────────────────
    rng3 = np.random.default_rng(enfants[2])
    rho_A_vals = [0.0, 0.01, 0.05, 0.1, 0.2, 0.5]
    N_plafond = 20  # réduit pour la mémoire (le lemme est exact en gaussien, le synthétique illustre)
    T_plafond = 50
    B_plafond = 10.0
    n_tirages_plafond = 10_000
    plafonds_ana = []
    plafonds_syn = []

    for rho_A in rho_A_vals:
        # analytique : variance de la somme sur N agents et T actions, sous corrélation intraclasse ρ_A
        # somme sur N agents : variance = N * sigma^2 * T * (1 + (N-1)*rho_A)
        var_somme_h0 = N_plafond * sigma**2 * T_plafond * (1 + (N_plafond - 1) * rho_A)
        r_plafond_simple = PHI(B_plafond / var_somme_h0**0.5 - Z_ALPHA)
        plafonds_ana.append(round(r_plafond_simple, 6))

        # synthétique : N agents corrélés par effet commun
        # X_it = mu_i + eps_it, mu_i ~ N(0, rho_A * sigma^2), eps_it ~ N(0, (1-rho_A) * sigma^2)
        # sous sabotage : décalage B/(N*T) par action
        dec = B_plafond / (N_plafond * T_plafond)
        # traiter par lots pour réduire la mémoire
        n_lots = 5
        taille_lot = n_tirages_plafond // n_lots
        totaux_sab = []
        totaux_h0 = []
        for _ in range(n_lots):
            if rho_A > 0:
                mu = rng3.normal(0, (rho_A * sigma**2) ** 0.5, size=(taille_lot, N_plafond))
                mu_h0 = rng3.normal(0, (rho_A * sigma**2) ** 0.5, size=(taille_lot, N_plafond))
            else:
                mu = np.zeros((taille_lot, N_plafond))
                mu_h0 = np.zeros((taille_lot, N_plafond))
            # somme sur T actions par agent : N(T*dec + mu_i*T, (1-rho_A)*sigma^2*T)  — par linéarité
            somme_par_agent = rng3.normal(T_plafond * dec + mu * T_plafond, ((1 - rho_A) * sigma**2 * T_plafond) ** 0.5, size=(taille_lot, N_plafond))
            totaux_sab.append(somme_par_agent.sum(axis=1))
            somme_h0 = rng3.normal(mu_h0 * T_plafond, ((1 - rho_A) * sigma**2 * T_plafond) ** 0.5, size=(taille_lot, N_plafond))
            totaux_h0.append(somme_h0.sum(axis=1))
        total = np.concatenate(totaux_sab)
        total_h0 = np.concatenate(totaux_h0)
        seuil_emp = np.quantile(total_h0, 1 - ALPHA)
        r_syn_p = (total > seuil_emp).mean()
        plafonds_syn.append(round(float(r_syn_p), 6))

    b3 = {
        "description": "M3-a (d) : plafond de rappel sous corrélation intraclasse ρ_A (effet de plan de Kish)",
        "parametres": {"N": N_plafond, "T": T_plafond, "B": B_plafond, "sigma": sigma, "tirages": n_tirages_plafond},
        "rho_A": rho_A_vals,
        "rappel_analytique": plafonds_ana,
        "rappel_synthetique": plafonds_syn,
        "attendu": "rappel décroît avec rho_A ; plafonne ≈ alpha pour rho_A grand et B fixé",
    }
    resultats["blocs"]["M3a_plafond_kish"] = b3
    print("\nBloc 3 — M3-a (d) plafond Kish :", json.dumps(b3, ensure_ascii=False, indent=1))

    # ──────────────────────────────────────────────────────────────────────
    # Bloc 4 — M3-a (e) : fausses alertes sous corrélation non modélisée
    # ──────────────────────────────────────────────────────────────────────
    rng4 = np.random.default_rng(enfants[3])
    n_tirages_fa = 100_000
    fa_ind = []
    fa_corr = []

    for rho_A in rho_A_vals:
        # seuil calibré sous indépendance (rho_A = 0)
        seuil_ind = Z_ALPHA * sigma * (N_plafond * T_plafond) ** 0.5

        # taux de fausses alertes réel sous rho_A > 0
        # somme sous H0 corrélé : variance = N * T * sigma^2 * (1 + (N-1)*rho_A)
        var_h0_corr = N_plafond * T_plafond * sigma**2 * (1 + (N_plafond - 1) * rho_A)
        fa_theo = 1 - PHI(seuil_ind / var_h0_corr**0.5)
        fa_ind.append(round(ALPHA, 6))
        fa_corr.append(round(fa_theo, 6))

    b4 = {
        "description": "M3-a (e) : taux de fausses alertes du moniteur conjoint calibré sous indépendance quand rho_A > 0",
        "parametres": {"N": N_plafond, "T": T_plafond, "sigma": sigma, "alpha_nominal": ALPHA},
        "rho_A": rho_A_vals,
        "taux_fa_nominal": fa_ind,
        "taux_fa_reel": fa_corr,
        "attendu": "taux réel >> alpha dès que rho_A > 0 ; lien avec M4 de la mesure unanime",
    }
    resultats["blocs"]["M3a_fausses_alertes"] = b4
    print("\nBloc 4 — M3-a (e) fausses alertes :", json.dumps(b4, ensure_ascii=False, indent=1))

    # ──────────────────────────────────────────────────────────────────────
    # Bloc 5 — M2-a : fraction d'intention et rappel en déploiement
    # ──────────────────────────────────────────────────────────────────────
    rng5 = np.random.default_rng(enfants[4])
    delta_obs = 3.0  # décalage observé en évaluation (signal total)
    sigma_sonde = 1.0
    fractions_f = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]
    rappel_eval = PHI(delta_obs / sigma_sonde - Z_ALPHA)
    rappels_deploiement = []
    surestimatations = []

    for f in fractions_f:
        delta_dep = f * delta_obs
        r_dep = PHI(delta_dep / sigma_sonde - Z_ALPHA)
        rappels_deploiement.append(round(r_dep, 6))
        surestimatations.append(round(rappel_eval - r_dep, 6))

    b5 = {
        "description": "M2-a : rappel en déploiement en fonction de la fraction d'intention f dans le score de sonde",
        "parametres": {"delta_obs": delta_obs, "sigma": sigma_sonde},
        "rappel_evaluation": round(rappel_eval, 6),
        "f": fractions_f,
        "rappel_deploiement": rappels_deploiement,
        "surestimation": surestimatations,
        "attendu": "rappel chute quand f < 1 ; pour f = 0 rappel = alpha",
    }
    resultats["blocs"]["M2a_fraction_intention"] = b5
    print("\nBloc 5 — M2-a fraction d'intention :", json.dumps(b5, ensure_ascii=False, indent=1))

    # ──────────────────────────────────────────────────────────────────────
    # Bloc 6 — M3-b : divergence de Kullback-Leibler entre copules (bornes de Pinsker)
    # ──────────────────────────────────────────────────────────────────────
    rng6 = np.random.default_rng(enfants[5])
    # deux gaussiennes N-dimensionnelles : produit (Sigma = I) et corrélée (Sigma = (1-rho)I + rho 11')
    # KL(N(0, Sigma_1) || N(0, Sigma_0)) pour Sigma_0 = I, Sigma_1 = (1-rho)I + rho 11'
    # = 0.5 * (tr(Sigma_1) - N - ln det(Sigma_1))
    # det((1-rho)I + rho 11') = (1-rho)^(N-1) * (1 + (N-1)*rho)
    # tr = N * (1-rho) + N*rho = N
    # KL = 0.5 * (N - N - ln((1-rho)^(N-1) * (1+(N-1)*rho)))
    #    = -0.5 * ((N-1)*ln(1-rho) + ln(1+(N-1)*rho))

    N_copule = 10
    rho_copule_vals = [0.0, 0.01, 0.05, 0.1, 0.2, 0.5]
    kl_vals = []
    pinsker_bounds = []

    for rho in rho_copule_vals:
        if rho == 0:
            kl = 0.0
        else:
            kl = -0.5 * ((N_copule - 1) * np.log(1 - rho) + np.log(1 + (N_copule - 1) * rho))
        vt_bound = (kl / 2) ** 0.5  # borne de Pinsker sur la variation totale
        kl_vals.append(round(float(kl), 6))
        pinsker_bounds.append(round(float(vt_bound), 6))

    b6 = {
        "description": "M3-b : KL entre copule produit et copule corrélée (N agents gaussiens), borne de Pinsker",
        "parametres": {"N_agents": N_copule},
        "rho_copule": rho_copule_vals,
        "KL_produit_vs_correlee": kl_vals,
        "borne_pinsker_VT": pinsker_bounds,
        "attendu": "KL croît avec rho ; la borne de Pinsker donne la variation totale maximale détectable par un test optimal",
    }
    resultats["blocs"]["M3b_copule_KL"] = b6
    print("\nBloc 6 — M3-b copule KL :", json.dumps(b6, ensure_ascii=False, indent=1))

    # ──────────────────────────────────────────────────────────────────────
    # Résumé
    # ──────────────────────────────────────────────────────────────────────
    print("\n\n=== RÉSUMÉ ===")
    print(f"z_alpha (unilatéral 5 %) = {Z_ALPHA:.6f}")
    print(f"Bloc 1 — M3-a (a) : rappel passe de {rappels_analytiques[0]:.4f} (N=1) à {rappels_analytiques[-1]:.4f} (N={valeurs_N[-1]}) ; alpha = {ALPHA}")
    print(f"Bloc 2 — M3-a (c) : budget par agent (β=80%) de {budgets_necessaires_par_agent[0]:.1f} (N=1) à {budgets_necessaires_par_agent[-1]:.1f} (N={valeurs_N[-1]}) ; conjoint de {budgets_necessaires_conjoint[0]:.1f} à {budgets_necessaires_conjoint[-1]:.1f}")
    print(f"Bloc 3 — M3-a (d) : rappel passe de {plafonds_ana[0]:.4f} (ρ=0) à {plafonds_ana[-1]:.4f} (ρ=0.5) sous N={N_plafond}")
    print(f"Bloc 4 — M3-a (e) : fausses alertes passent de {fa_corr[0]:.4f} (ρ=0) à {fa_corr[-1]:.4f} (ρ=0.5) avec seuil calibré sous indépendance")
    print(f"Bloc 5 — M2-a : rappel en évaluation {rappel_eval:.4f}, en déploiement {rappels_deploiement[0]:.4f} (f=0) à {rappels_deploiement[-1]:.4f} (f=1)")
    print(f"Bloc 6 — M3-b : KL = {kl_vals[-1]:.4f} pour ρ={rho_copule_vals[-1]} sous N={N_copule} agents, borne de Pinsker = {pinsker_bounds[-1]:.4f}")

    # sortie structurée
    with open("calculs-niveau-methode-classes-2-3-v1.json", "w", encoding="utf-8") as fj:
        json.dump(resultats, fj, ensure_ascii=False, indent=1)
    print(f"\nSortie JSON : calculs-niveau-methode-classes-2-3-v1.json")


if __name__ == "__main__":
    main()
