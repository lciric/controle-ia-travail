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


if __name__ == "__main__":
    unittest.main()
