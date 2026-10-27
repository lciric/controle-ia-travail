"""Essais du cœur du pari apparié borné (v7, version 20) : règle double, validité sous nuls asymétriques de moyenne nulle,
intersection-union, garde, arrêt au seuil, sans remise, borne basse de confiance."""

import math
import random
import unittest

from pole import pari_apparie as pa


def tirer(rng, valeurs, probas, n):
    return [rng.choices(valeurs, probas)[0] for _ in range(n)]


class RegleDouble(unittest.TestCase):
    def test_coefficients(self):
        self.assertTrue(pa.verifier_coefficients({"A": 1, "B": -1}))
        self.assertTrue(pa.verifier_coefficients({"Af": 0.5, "Bf": -0.5, "An": -0.5, "Bn": 0.5}))  # interaction (C11)
        self.assertTrue(pa.verifier_coefficients({"A": 1}, constante=-0.4))  # rappel ≥ x
        for coefs, c in (({"A": 1, "B": 1}, 0.0), ({"A": 1, "B": -1}, 0.5), ({"A": -1, "B": -1}, 0.0), ({}, 0.0)):
            with self.subTest(coefs=coefs, c=c), self.assertRaises(pa.ContrasteInvalide):
                pa.verifier_coefficients(coefs, c)

    def test_contraste_et_bornes(self):
        self.assertAlmostEqual(pa.contraste({"A": 0.6, "B": 0.4}, {"A": 1, "B": -1}), 0.2)
        with self.assertRaises(pa.ContrasteInvalide):
            pa.contraste({"A": 1.2, "B": 0.4}, {"A": 1, "B": -1})
        with self.assertRaises(pa.ContrasteInvalide):
            pa.trajectoire_log_richesse([0.5, 1.5])


class Validite(unittest.TestCase):
    def test_nuls_asymetriques_de_moyenne_nulle(self):
        """S1 (90 % à +0,1, 10 % à −0,9) et S2 (80 % à +0,1, 20 % à −0,4) : promotion ≤ α (borne large : 0,08)."""
        rng = random.Random(20261027)
        for valeurs, probas in (([0.1, -0.9], [0.9, 0.1]), ([0.1, -0.4], [0.8, 0.2])):
            promus = sum(pa.evaluer({"B": tirer(rng, valeurs, probas, 150)})["promue"] for _ in range(300))
            self.assertLessEqual(promus / 300, 0.08, (valeurs, promus))

    def test_puissance_vingt_points(self):
        rng = random.Random(7)
        promus = 0
        for _ in range(100):
            v = [(sum(rng.random() < 0.6 for _ in range(10)) - sum(rng.random() < 0.4 for _ in range(10))) / 10 for _ in range(60)]
            promus += pa.evaluer({"B": v})["promue"]
        self.assertGreaterEqual(promus, 90)  # simulation v2 : 1,00 à 60 unités

    def test_intersection_union(self):
        """Un comparateur au nul (moyenne nulle) et un battu largement : la fiche ne doit pas être promue (≤ α)."""
        rng = random.Random(11)
        promus = 0
        for _ in range(300):
            facile = [0.6] * 80
            nul = tirer(rng, [0.1, -0.9], [0.9, 0.1], 80)
            promus += pa.evaluer({"facile": facile, "nul": nul})["promue"]
        self.assertLessEqual(promus / 300, 0.08)
        self.assertTrue(pa.evaluer({"a": [0.6] * 40, "b": [0.5] * 40})["promue"])

    def test_garde_bloque_le_tricheur(self):
        """A rappelle plus mais tire plus que B de 10 points (E[g] = 0,10 ≥ δ = 0,05) : jamais promu."""
        rng = random.Random(13)
        promus = 0
        for _ in range(200):
            v = [0.5] * 80
            g = [0.1 + rng.uniform(-0.02, 0.02) for _ in range(150)]
            promus += pa.evaluer({"B": v}, ecarts_faux_positifs=g, delta=0.05)["promue"]
        self.assertEqual(promus, 0)
        g_sain = [0.0] * 150
        self.assertTrue(pa.evaluer({"B": [0.5] * 80}, ecarts_faux_positifs=g_sain, delta=0.05)["promue"])

    def test_arret_au_seuil_m_sur_alpha(self):
        r1 = pa.evaluer({"B": [1.0] * 30}, m=1)
        r10 = pa.evaluer({"B": [1.0] * 30}, m=10)
        self.assertEqual(r1["instant_d_arret"], 7)  # moyenne de 1,1^t, 1,3^t, 1,6^t, 1,9^t ≥ 20 dès t = 7
        self.assertGreater(r10["instant_d_arret"], r1["instant_d_arret"])
        self.assertAlmostEqual(r1["log_e_valeur"], r1["trajectoire_log_min"][6])

    def test_sans_remise(self):
        """Banque figée de moyenne exactement nulle, lue dans des ordres uniformes : promotion ≤ α (borne large)."""
        rng = random.Random(17)
        banque = [0.1] * 90 + [-0.9] * 10
        promus = 0
        for _ in range(300):
            rng.shuffle(banque)
            promus += max(pa.trajectoire_log_sans_remise(banque)) >= math.log(20)
        self.assertLessEqual(promus / 300, 0.08)

    def test_borne_basse(self):
        rng = random.Random(19)
        couvertes = 0
        for _ in range(100):
            v = [rng.choice([0.4, 0.0]) for _ in range(200)]  # moyenne 0,2
            b = pa.borne_basse(v)
            couvertes += b <= 0.2
            self.assertGreater(b, -1.0)
        self.assertGreaterEqual(couvertes, 92)


def ebh_ordinaire(e, alpha):
    """Référence : règle e-BH ordinaire (m fiches, niveau α), écrite indépendamment."""
    m = len(e)
    ordre = sorted(e, key=lambda i: -e[i])
    k_etoile = max([k for k in range(1, m + 1) if e[ordre[k - 1]] >= m / (alpha * k)], default=0)
    return set(ordre[:k_etoile])


def marche_a_prime(rng, pas):
    """Monde A′ de la contre-lecture v5 : martingale ×1,5 / ×0,5 à pile ou face ; trajectoire du log."""
    lw, traj = 0.0, []
    for _ in range(pas):
        lw += math.log(1.5) if rng.random() < 0.5 else math.log(0.5)
        traj.append(lw)
    return traj


class PlafondDS27(unittest.TestCase):
    def test_bornes_et_coincidence(self):
        self.assertEqual(pa.ponderation_plafonnee(5, 20), 0.25)
        self.assertEqual(pa.ponderation_plafonnee(100, 20), 1.0)
        v = pa.contraste({"A": 0.2, "B": 0.9}, {"A": 1, "B": -1})
        self.assertAlmostEqual(pa.contraste_plafonne({"A": 0.2, "B": 0.9}, {"A": 1, "B": -1}, 0.0, 10, 20), 0.5 * v)
        self.assertAlmostEqual(pa.contraste_plafonne({"A": 0.2, "B": 0.9}, {"A": 1, "B": -1}, 0.0, 400, 20), v)
        for args in ((-1, 20), (5, 0), (2.5, 20)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                pa.ponderation_plafonnee(*args)


class HeritageDS25bis(unittest.TestCase):
    def test_ebh_pondere_egale_l_ordinaire_pour_une_famille(self):
        rng = random.Random(23)
        for _ in range(300):
            m = rng.randint(1, 8)
            e = {i: math.exp(rng.uniform(-2, 7)) for i in range(m)}
            attendu = ebh_ordinaire(e, 0.05)
            obtenu = pa.ebh_pondere({i: math.log(x) for i, x in e.items()}, {i: 0.05 / m for i in e})
            self.assertEqual(obtenu, attendu, e)
        self.assertEqual(pa.ebh_pondere({"a": math.log(100), "b": math.log(50), "c": math.log(10), "d": 0.0},
                                        {k: 0.0125 for k in "abcd"}), {"a", "b"})

    def test_budgets_refuses(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b"], 0.03)
        with self.assertRaises(ValueError):
            c.entrer("g2", ["c"], 0.03)  # 0,06 > α
        with self.assertRaises(ValueError):
            c.entrer("g2", ["a"], 0.01)  # une relance n'entre pas une seconde fois
        with self.assertRaises(ValueError):
            pa.ebh_pondere({"a": 0.0}, {"a": 1.5})

    def test_budget_garde_quand_les_soeurs_sont_abandonnees(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b", "c", "d"], 0.04)
        for f in "bcd":
            c.abandonner(f)
        self.assertAlmostEqual(c.seuil_log("a"), math.log(4 / 0.04))  # 100, jamais 1/0,04 = 25
        c.ajouter_trajectoire("a", [math.log(30)])
        self.assertEqual(c.lire(), set())  # 30 < 100 : la lecture « seule » l'aurait promue (30 ≥ 25)
        c.ajouter_trajectoire("a", [math.log(2), math.log(5)])  # 30 × 5 = 150 ≥ 100 : arrêt au seuil
        self.assertAlmostEqual(c.log_e["a"], math.log(150))
        self.assertIn("a", c.arretees)
        self.assertEqual(c.lire(), {"a"})
        self.assertEqual(c.bonferroni(), {"a"})

    def test_promotion_une_seule_fois_et_gel(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b"], 0.03)
        c.ajouter_trajectoire("a", [math.log(80)])
        self.assertEqual(c.lire(), {"a"})
        avant = c.log_e["a"]
        c.ajouter_trajectoire("a", [math.log(0.01)])  # gelée : rien ne change
        self.assertEqual(c.log_e["a"], avant)
        c.entrer("g2", ["e"], 0.01)
        self.assertEqual(c.lire(), set())  # « a » reste promue, sans être promue à nouveau
        self.assertEqual(c.promues, {"a"})

    def test_nul_complet_lecture_valide_contre_lecture_seule(self):
        """Monde A′ (contre-lecture v5, section 7 H) : cohorte de 4 nulles entrée à la génération 1 et relancée,
        3 nouvelles par génération (lues une génération), 10 générations de 20 pas, suite 6/(π²g²), α = 0,05.
        Lecture valide (D-S25 bis) : au plus α ; lecture « seule » de la cohorte à 1/α_1 : plus haut (mécanisme de K5-1 ;
        ici la lecture « seule » vaut dès la génération 1, simplification qui la majore un peu)."""
        rng = random.Random(29)
        alpha, generations, pas, rep = 0.05, 10, 20, 400
        a_g = [alpha * 6 / (math.pi ** 2 * g * g) for g in range(1, generations + 1)]
        fausses_valides = fausses_seules = 0
        for _ in range(rep):
            c = pa.Course(alpha=alpha)
            c.entrer("cohorte", [f"c{i}" for i in range(4)], a_g[0])
            cohorte_seule = {f"c{i}": 0.0 for i in range(4)}
            seule_promue = False
            for g in range(generations):
                if g > 0:
                    c.entrer(f"g{g + 1}", [f"n{g}-{j}" for j in range(3)], a_g[g])
                for i in range(4):
                    traj = marche_a_prime(rng, pas)
                    c.ajouter_trajectoire(f"c{i}", traj)
                    base = cohorte_seule[f"c{i}"]
                    if base + max(traj) >= -math.log(a_g[0]):
                        seule_promue = True
                    cohorte_seule[f"c{i}"] = base + traj[-1]
                if g > 0:
                    for j in range(3):
                        c.ajouter_trajectoire(f"n{g}-{j}", marche_a_prime(rng, pas))
                c.lire()
                if g > 0:
                    for j in range(3):
                        c.abandonner(f"n{g}-{j}")
            fausses_valides += bool(c.promues)
            fausses_seules += seule_promue
        self.assertLessEqual(fausses_valides / rep, alpha + 0.01)
        self.assertGreater(fausses_seules, fausses_valides)
        self.assertGreater(fausses_seules / rep, 0.04)


if __name__ == "__main__":
    unittest.main()
