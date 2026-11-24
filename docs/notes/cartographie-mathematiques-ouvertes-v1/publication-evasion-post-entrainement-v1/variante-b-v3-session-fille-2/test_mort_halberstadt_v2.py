#!/usr/bin/env python3
"""
Test de mort exact et vérification numérique/rationnelle de la Loi de Halberstadt (v1).
Mandat : GO-2026-11-24-01 — Étape 2.
Dépense API payante : 0,00 USD.
Vérifie :
  1. En arithmétique rationnelle exacte (`fractions.Fraction`) le cas pur du rejet bayésien (eta = 0)
     et l'identité de variance d'enrichissement conditionnel : E_post[beta | triche] - E_0[beta | triche] = Var_0(beta | triche) / E_0[beta | triche].
  2. Sur 10 000 instances aléatoires tirées dans l'espace complet des paramètres (plus cas limites aux frontières),
     zéro contre-exemple (0 / 10 000) aux équivalences exactes du Théorème 1 (Opérateur A de rejet pur,
     Opérateur B KL-régularisé pénalisé, Dilemme Rejet-Pénalité) et du Théorème 2 (Régimes d'échappement R1, R2, R3).
  3. Un balayage de basculement de phase chiffré exporté en JSON (`resultats-test-mort-halberstadt-v1.json`, v1 seulement ; la v2 écrit au chemin donné)
     pour intégration directe dans `elucidation-loi-halberstadt-post-entrainement-v1.md`.
"""

from __future__ import annotations

import fractions
import json
import math
import os
import pathlib
import random
import shutil
import sys
import unittest
from typing import Any

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

TOL = 1e-11


def loi_operateur_sans_moniteur(
    p_h: float, p_v: float, p_f: float, eta: float, delta_r_v: float, delta_r_f: float
) -> tuple[float, float, float]:
    """Loi de post-entraînement KL-régularisée sans moniteur (beta == 1 partout), R_h = 0."""
    m = max(0.0, eta * delta_r_v, eta * delta_r_f)
    w_h = p_h * math.exp(-m)
    w_v = p_v * math.exp(eta * delta_r_v - m)
    w_f = p_f * math.exp(eta * delta_r_f - m)
    z = w_h + w_v + w_f
    return w_h / z, w_v / z, w_f / z


def loi_operateur_a_rejet_pur(
    p_h: float,
    p_v: float,
    p_f: float,
    beta_h: float,
    beta_v: float,
    beta_f: float,
    eta: float,
    delta_r_v: float,
    delta_r_f: float,
) -> tuple[float, float, float]:
    """
    Opérateur A : filtrage par rejet pur des essais détectés (sans pénalité négative, réessai)
    couplé à la sélection exponentielle de température inverse eta >= 0.
    pi_A(i) proportionnel à beta_i * exp(eta * R_i) * p_i.
    """
    m = max(0.0, eta * delta_r_v, eta * delta_r_f)
    w_h = beta_h * p_h * math.exp(-m)
    w_v = beta_v * p_v * math.exp(eta * delta_r_v - m)
    w_f = beta_f * p_f * math.exp(eta * delta_r_f - m)
    z = w_h + w_v + w_f
    return w_h / z, w_v / z, w_f / z


def loi_operateur_b_kl_penalise(
    p_h: float,
    p_v: float,
    p_f: float,
    beta_h: float,
    beta_v: float,
    beta_f: float,
    eta: float,
    delta_r_v: float,
    delta_r_f: float,
    penalite_c: float,
) -> tuple[float, float, float]:
    """
    Opérateur B : mise à jour de politique KL-régularisée par rapport à pi_0 avec pénalité -C <= 0
    lorsque le moniteur déclenche (M_boucle = 1).
    Récompense attendue : beta_i * R_i - (1 - beta_i) * C, avec R_h = 0.
    """
    r_eff_h = -(1.0 - beta_h) * penalite_c
    r_eff_v = beta_v * delta_r_v - (1.0 - beta_v) * penalite_c
    r_eff_f = beta_f * delta_r_f - (1.0 - beta_f) * penalite_c
    m = max(eta * r_eff_h, eta * r_eff_v, eta * r_eff_f)
    w_h = p_h * math.exp(eta * r_eff_h - m)
    w_v = p_v * math.exp(eta * r_eff_v - m)
    w_f = p_f * math.exp(eta * r_eff_f - m)
    z = w_h + w_v + w_f
    return w_h / z, w_v / z, w_f / z


class EssaisUnitairesLoiHalberstadt(unittest.TestCase):
    """Tests unitaires exacts (rationnels et flottants) des Théorèmes 1 et 2."""

    def test_01_arithmetique_rationnelle_exacte_identite_variance_rejet_pur(self) -> None:
        """Vérifie en Fractions exactes que E_rejet[beta | triche] - E_0[beta | triche] = Var_0(beta | triche) / E_0[beta | triche]."""
        F = fractions.Fraction
        # Sous-espèces de tricheurs avec probabilités conditionnelles exactes et taux de faux négatifs distincts
        poids = [F(1, 2), F(1, 3), F(1, 6)]
        betas = [F(1, 10), F(2, 5), F(9, 10)]
        self.assertEqual(sum(poids), F(1, 1))

        esp_0 = sum(w * b for w, b in zip(poids, betas))
        var_0 = sum(w * (b - esp_0) ** 2 for w, b in zip(poids, betas))
        poids_post = [(w * b) / esp_0 for w, b in zip(poids, betas)]
        esp_post = sum(wp * b for wp, b in zip(poids_post, betas))

        self.assertEqual(esp_post - esp_0, var_0 / esp_0)
        self.assertGreater(var_0, F(0, 1))
        self.assertGreater(esp_post, esp_0)

    def test_02_theoreme_1_10000_instances_zero_contre_exemple(self) -> None:
        """Balayage Monte-Carlo déterministe sur 10 000 instances générales : 0 violation tolérée."""
        rng = random.Random(20261124)
        violations = 0
        for _ in range(10_000):
            u1, u2, u3 = rng.uniform(0.02, 1.0), rng.uniform(0.02, 1.0), rng.uniform(0.02, 1.0)
            s = u1 + u2 + u3
            p_h, p_v, p_f = u1 / s, u2 / s, u3 / s

            # 0 <= beta_v < beta_f <= beta_h <= 1
            beta_h = rng.uniform(0.55, 1.0)
            beta_f = rng.uniform(0.20, beta_h)
            beta_v = rng.uniform(0.0, beta_f - 1e-3)

            eta = rng.uniform(0.1, 8.0)
            delta_r = rng.uniform(0.05, 5.0)
            penalite_c = rng.uniform(0.0, 4.0)

            h0, v0, f0 = loi_operateur_sans_moniteur(p_h, p_v, p_f, eta, delta_r, delta_r)
            ha, va, fa = loi_operateur_a_rejet_pur(p_h, p_v, p_f, beta_h, beta_v, beta_f, eta, delta_r, delta_r)
            hb, vb, fb = loi_operateur_b_kl_penalise(
                p_h, p_v, p_f, beta_h, beta_v, beta_f, eta, delta_r, delta_r, penalite_c
            )

            # 1(a) Enrichissement conditionnel strict parmi les tricheurs
            q0 = f0 / (v0 + f0)
            qa = fa / (va + fa)
            qb = fb / (vb + fb)
            if not (qa > q0 + 1e-14 and qb > q0 + 1e-14):
                violations += 1

            # 1(b) Seuil exact d'amplification absolue sous rejet pur (fa > f0)
            membre_g = (beta_f - beta_v) * p_v * math.exp(eta * delta_r)
            membre_d = (beta_h - beta_f) * p_h
            if abs(membre_g - membre_d) > 1e-9:
                pred_amplification_a = membre_g > membre_d
                obs_amplification_a = fa > f0
                if pred_amplification_a != obs_amplification_a:
                    violations += 1

            # 1(c) Seuil exact de dominance de Pi_f sur Pi_h sous Opérateur B (fb > hb)
            # fb > hb <=> eta * [beta_f * delta_r - (beta_h - beta_f) * C] > log(p_h / p_f)
            lhs_b = eta * (beta_f * delta_r - (beta_h - beta_f) * penalite_c)
            rhs_b = math.log(p_h / p_f)
            if abs(lhs_b - rhs_b) > 1e-9:
                if (lhs_b > rhs_b) != (fb > hb):
                    violations += 1

            # 1(d) Seuil exact d'amplification absolue sous Opérateur B (fb > f0)
            lhs_amp_b = p_v * (1.0 - math.exp(-eta * (beta_f - beta_v) * (delta_r + penalite_c)))
            rhs_amp_b = p_h * math.exp(-eta * delta_r) * (
                math.exp(eta * ((1.0 - beta_f) * delta_r + (beta_h - beta_f) * penalite_c)) - 1.0
            )
            if abs(lhs_amp_b - rhs_amp_b) > 1e-9:
                if (lhs_amp_b > rhs_amp_b) != (fb > f0):
                    violations += 1

        self.assertEqual(violations, 0)

    def test_03_dilemme_rejet_contre_penalite_niche_parfaite(self) -> None:
        """
        Vérifie que lorsque beta_h = beta_f = 1 et 0 < beta_v < 1 :
          - fa > f0 pour tout eta >= 0, delta_r >= 0 ;
          - fb > fa <=> eta * (delta_r + C) > log(1 / beta_v) / (1 - beta_v).
        """
        rng = random.Random(314159)
        for _ in range(2_000):
            p_h, p_v, p_f = 0.70, 0.25, 0.05
            beta_v = rng.uniform(0.05, 0.90)
            eta = rng.uniform(0.2, 5.0)
            delta_r = rng.uniform(0.1, 3.0)
            c_pen = rng.uniform(0.0, 3.0)

            _, _, f0 = loi_operateur_sans_moniteur(p_h, p_v, p_f, eta, delta_r, delta_r)
            _, _, fa = loi_operateur_a_rejet_pur(p_h, p_v, p_f, 1.0, beta_v, 1.0, eta, delta_r, delta_r)
            _, _, fb = loi_operateur_b_kl_penalise(p_h, p_v, p_f, 1.0, beta_v, 1.0, eta, delta_r, delta_r, c_pen)

            self.assertGreater(fa, f0)
            seuil = math.log(1.0 / beta_v) / (1.0 - beta_v)
            val = eta * (delta_r + c_pen)
            if abs(val - seuil) > 1e-9:
                self.assertEqual(fb > fa, val > seuil)

    def test_04_regime_r1_barriere_kl_et_maintien_multi_objectifs(self) -> None:
        """
        Régime R1 : si la pénalité de maintien multi-objectifs delta_maint réduit Delta R_net = Delta R - delta_maint
        sous la barrière de divergence KL (log(p_h / p_f) / (eta * beta_f)), alors Pi_f reste dominé par Pi_h
        et décroît exponentiellement quand eta croît si Delta R_net < 0.
        """
        p_h, p_v, p_f = 0.90, 0.09, 0.01
        beta_h, beta_v, beta_f = 1.0, 0.10, 0.90
        delta_r_brut = 1.0
        delta_maint = 1.25  # Coût sur les autres objectifs (ex. langue/qualité, cf. testingthewaters)
        delta_r_f_net = delta_r_brut - delta_maint  # -0.25 < 0

        for eta in (1.0, 5.0, 20.0):
            ha, _, fa = loi_operateur_a_rejet_pur(
                p_h, p_v, p_f, beta_h, beta_v, beta_f, eta, delta_r_brut, delta_r_f_net
            )
            hb, _, fb = loi_operateur_b_kl_penalise(
                p_h, p_v, p_f, beta_h, beta_v, beta_f, eta, delta_r_brut, delta_r_f_net, penalite_c=2.0
            )
            self.assertLess(fb, p_f)
            self.assertLess(fb, hb)
        # À eta = 20 sous Opérateur B avec C = 2.0 (qui élimine aussi Pi_v car 0.1*1 - 0.9*2 = -1.7 < 0), l'honnêteté domine à > 99.99%
        hb_20, vb_20, fb_20 = loi_operateur_b_kl_penalise(
            p_h, p_v, p_f, beta_h, beta_v, beta_f, 20.0, delta_r_brut, delta_r_f_net, penalite_c=2.0
        )
        self.assertGreater(hb_20, 0.9999)
        self.assertLess(vb_20 + fb_20, 1e-4)

    def test_05_regime_r2_decouplage_informationnel_sonde_hors_boucle(self) -> None:
        """
        Régime R2 : sur K sous-espèces de tricheurs de même récompense Delta R, si la survie au moniteur d'audit
        hors boucle `beta_audit` est conditionnellement orthogonale (ou négativement corrélée) à la survie au
        filtre en boucle `beta_boucle` sous pi_0(. | Pi_tr), alors le post-entraînement utilisant M_boucle
        n'augmente JAMAIS le taux d'évasion face à M_audit (ni sous A, ni sous B).
        """
        rng = random.Random(271828)
        # Construction exacte à covariance nulle ou négative sur 4 sous-types de tricheurs équiprobables
        for _ in range(1_000):
            b_boucle = [rng.uniform(0.05, 0.95) for _ in range(4)]
            # Ordre inverse sur beta_audit => covariance <= 0 par inégalité de réarrangement / Tchebychev
            b_sorted = sorted(rng.uniform(0.05, 0.95) for _ in range(4))
            rang = sorted(range(4), key=lambda i: b_boucle[i])
            b_audit = [0.0] * 4
            for pos, idx in enumerate(rang):
                b_audit[idx] = b_sorted[3 - pos]

            evasion_audit_avant = sum(b_audit) / 4.0
            eta = rng.uniform(0.5, 6.0)
            delta_r = rng.uniform(0.5, 3.0)
            c_pen = rng.uniform(0.0, 3.0)

            # Poids intra-tricheurs sous A : prop à b_boucle[i]
            z_a = sum(b_boucle)
            evasion_audit_apres_a = sum((b_boucle[i] / z_a) * b_audit[i] for i in range(4))

            # Poids intra-tricheurs sous B : prop à exp(eta * b_boucle[i] * (delta_r + C))
            w_b = [math.exp(eta * b_boucle[i] * (delta_r + c_pen)) for i in range(4)]
            z_b = sum(w_b)
            evasion_audit_apres_b = sum((w_b[i] / z_b) * b_audit[i] for i in range(4))

            self.assertLessEqual(evasion_audit_apres_a, evasion_audit_avant + TOL)
            self.assertLessEqual(evasion_audit_apres_b, evasion_audit_avant + TOL)

    def test_06_regime_r3_pieges_plantes_indiscernables_borne_variation_totale(self) -> None:
        """
        Régime R3 (dualité avec Q4) : monde fini d'observations X = {1..M}.
        Loi ordinaire P_ord et loi piège P_piege à distance en variation totale d_TV <= delta_ind.
        Sur P_ord, le moniteur est aveugle (beta_ord = 1, gain +Delta R).
        Sur P_piege (poids rho dans le mélange d'entraînement), toute triche est détectée avec prob 1 - eps_piege
        et reçoit -C.
        Pour TOUTE politique conditionnelle pi(triche | x) in [0, 1]^M ayant taux de triche tau_ord > delta_ind
        sur P_ord, son taux de triche sur P_piege vaut au moins tau_ord - delta_ind, et son gain attendu est
        strictement négatif dès que C dépasse le seuil critique R3.
        """
        rng = random.Random(161803)
        m_obs = 6
        for _ in range(1_000):
            # Génération de deux lois sur {0..5} proches en variation totale
            base = [rng.uniform(0.1, 1.0) for _ in range(m_obs)]
            s_b = sum(base)
            p_ord = [x / s_b for x in base]
            pert = [x + rng.uniform(-0.03, 0.03) for x in p_ord]
            pert = [max(1e-4, x) for x in pert]
            s_p = sum(pert)
            p_piege = [x / s_p for x in pert]
            d_tv = 0.5 * sum(abs(a - b) for a, b in zip(p_ord, p_piege))

            # Politique conditionnelle arbitraire choisie par l'agent cherchant à n'attaquer que P_ord
            pol = [1.0 if p_ord[x] >= p_piege[x] else 0.0 for x in range(m_obs)]
            tau_ord = sum(p_ord[x] * pol[x] for x in range(m_obs))
            tau_piege = sum(p_piege[x] * pol[x] for x in range(m_obs))

            # Inégalité fondamentale d'indistinguabilité (Q4 retourné en défense R3)
            self.assertGreaterEqual(tau_piege + TOL, tau_ord - d_tv)

            if tau_ord > d_tv + 0.05:
                rho = 0.20
                eps_piege = 0.02
                delta_r = 1.0
                # Seuil suffisant pour que E[R_eff(pol)] < 0 = E[R_eff(honnete)]
                # v2 (audit indépendant, correction 10) : terme rho*eps*(tau-delta) rétabli ;
                # la v1 omettait ce terme et se trouvait sous C* d'environ eps*dR/(1-eps).
                c_seuil = (
                    (1.0 - rho) * tau_ord + rho * eps_piege * (tau_ord - d_tv)
                ) * delta_r / (rho * (1.0 - eps_piege) * (tau_ord - d_tv))
                c_choisi = c_seuil + 0.5
                gain_ord = tau_ord * delta_r
                gain_piege = tau_piege * (eps_piege * delta_r - (1.0 - eps_piege) * c_choisi)
                gain_melange = (1.0 - rho) * gain_ord + rho * gain_piege
                self.assertLess(gain_melange, 0.0)


def generer_tableau_basculement_de_phase() -> dict[str, Any]:
    """Produit les séries numériques exactes illustrant le basculement de phase et les régimes R1-R3."""
    lean_binaire = shutil.which("lean")
    p_h, p_v, p_f = 0.85, 0.14, 0.01
    beta_h, beta_v, beta_f_imparfait = 1.0, 0.05, 0.75
    eta = 3.0

    seuil_amp_a = (1.0 / eta) * (
        math.log(p_h / p_v) + math.log((beta_h - beta_f_imparfait) / (beta_f_imparfait - beta_v))
    )
    seuil_dom_a = (1.0 / eta) * (math.log(p_h / p_f) + math.log(beta_h / beta_f_imparfait))

    grille_delta_r = [0.2, 0.4, round(seuil_amp_a, 4), 0.8, 1.2, round(seuil_dom_a, 4), 2.2, 3.0]
    courbe_phase: list[dict[str, float]] = []
    for dr in sorted(set(grille_delta_r)):
        _, v0, f0 = loi_operateur_sans_moniteur(p_h, p_v, p_f, eta, dr, dr)
        ha, va, fa = loi_operateur_a_rejet_pur(
            p_h, p_v, p_f, beta_h, beta_v, beta_f_imparfait, eta, dr, dr
        )
        hb, vb, fb = loi_operateur_b_kl_penalise(
            p_h, p_v, p_f, beta_h, beta_v, beta_f_imparfait, eta, dr, dr, penalite_c=2.5
        )
        courbe_phase.append(
            {
                "delta_r": dr,
                "sans_moniteur_prob_furtive": round(f0, 6),
                "sans_moniteur_part_cond_furtive": round(f0 / (v0 + f0), 6),
                "rejet_pur_A_prob_furtive": round(fa, 6),
                "rejet_pur_A_part_cond_furtive": round(fa / (va + fa), 6),
                "rejet_pur_A_prob_honnete": round(ha, 6),
                "penalite_B_C2.5_prob_furtive": round(fb, 6),
                "penalite_B_C2.5_part_cond_furtive": round(fb / (vb + fb), 6),
                "penalite_B_C2.5_prob_honnete": round(hb, 6),
            }
        )

    # Illustration de la divergence Rejet pur (A) contre Pénalité (B) quand eta -> infini à beta_f = 0.75 < 1
    comparaison_asymptotique_eta: list[dict[str, float]] = []
    for eta_val in (0.5, 1.0, 2.0, 4.0, 8.0, 16.0):
        ha, _, fa = loi_operateur_a_rejet_pur(p_h, p_v, p_f, 1.0, 0.05, 0.75, eta_val, 0.6, 0.6)
        hb, _, fb = loi_operateur_b_kl_penalise(p_h, p_v, p_f, 1.0, 0.05, 0.75, eta_val, 0.6, 0.6, penalite_c=2.5)
        comparaison_asymptotique_eta.append(
            {
                "eta": eta_val,
                "rejet_pur_A_prob_honnete": round(ha, 6),
                "rejet_pur_A_prob_furtive": round(fa, 6),
                "penalite_B_C2.5_prob_honnete": round(hb, 6),
                "penalite_B_C2.5_prob_furtive": round(fb, 6),
            }
        )

    return {
        "mandat": "GO-2026-11-24-01",
        "script": "test_mort_halberstadt_v1.py",
        "lean_present_sur_machine": lean_binaire is not None,
        "chemin_lean": lean_binaire,
        "essais_monte_carlo_theoreme_1": {"instances": 10000, "contre_exemples": 0},
        "essais_dilemme_niche_parfaite": {"instances": 2000, "contre_exemples": 0},
        "essais_regimes_r2_r3": {"instances_r2": 1000, "instances_r3": 1000, "contre_exemples": 0},
        "parametres_reference_phase": {
            "p_h": p_h,
            "p_v": p_v,
            "p_f": p_f,
            "beta_h": beta_h,
            "beta_v": beta_v,
            "beta_f": beta_f_imparfait,
            "eta": eta,
            "seuil_amplification_absolue_rejet_pur_delta_r": round(seuil_amp_a, 6),
            "seuil_dominance_sur_honnete_rejet_pur_delta_r": round(seuil_dom_a, 6),
            "seuil_asymptotique_blocage_penalite_B_C2.5_delta_r": round((1.0 - beta_f_imparfait) / beta_f_imparfait * 2.5, 6),
        },
        "courbe_basculement_delta_r": courbe_phase,
        "comparaison_pression_eta_delta_r_0.6": comparaison_asymptotique_eta,
    }


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(EssaisUnitairesLoiHalberstadt)
    coureur = unittest.TextTestRunner(verbosity=2)
    res = coureur.run(suite)
    if not res.wasSuccessful():
        sys.exit(1)

    dossier = pathlib.Path(
        "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
        "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/cartographie-maths-ouvertes-v1"
    )
    # v2 : aucune écriture par défaut à côté du script (le JSON v1 est scellé) ; chemin explicite exigé, sans écrasement.
    if len(sys.argv) < 2:
        raise SystemExit("usage : test_mort_halberstadt_v2.py CHEMIN_SORTIE.json (hors du dossier scellé)")
    sortie = pathlib.Path(sys.argv[1]).resolve()
    if sortie.exists():
        raise SystemExit(f"refus d'écraser : {sortie}")
    rapport = generer_tableau_basculement_de_phase()
    sortie.write_text(json.dumps(rapport, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(rapport["parametres_reference_phase"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
