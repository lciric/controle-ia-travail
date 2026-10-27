"""Essais de l'engagement « apparié » (v7, version 23) : refus, seuils pris au seul calibrage, clé de l'héritage,
scellement, et jugement de bout en bout sur une banque de scores."""

import copy
import random
import unittest

from pole import engagement_apparie as ea
from pole import monde_banque_scores as mbs
from essais.test_v7_monde_banque_scores import banque_synthetique


BLANC_CONTRE_NOIR = {"noir": {"coefficients": {"blanc": 1, "noir": -1}}}


class Construction(unittest.TestCase):
    def setUp(self):
        self.banque = banque_synthetique(random.Random(43), unites_par_partie=(100, 0, 100))
        self.m = mbs.MondeBanqueScores(self.banque, 17)

    def test_refus(self):
        for nom, kw in {
            "règle double": dict(contrastes={"x": {"coefficients": {"blanc": 1, "noir": 1}}}, tau=0.05),
            "cellule inconnue": dict(contrastes={"x": {"coefficients": {"gris": 1}, "constante": -0.5}}, tau=0.05),
            "aucun contraste": dict(contrastes={}, tau=0.05),
            "calibrage comme épreuve": dict(contrastes=BLANC_CONTRE_NOIR, tau=0.05, partie="calibrage"),
            "garde sans δ": dict(contrastes=BLANC_CONTRE_NOIR, tau=0.05, garde={"a": "blanc", "b": "noir"}),
            "calibrage insuffisant": dict(contrastes=BLANC_CONTRE_NOIR, tau=0.0005),
            "m_c": dict(contrastes=BLANC_CONTRE_NOIR, tau=0.05, m_c=0),
        }.items():
            with self.subTest(nom), self.assertRaises(ea.EngagementInvalide):
                ea.construire(self.m, **kw)

    def test_seuils_au_seul_calibrage(self):
        e1 = ea.construire(self.m, BLANC_CONTRE_NOIR, tau=0.05)
        autre = copy.deepcopy(self.banque)
        for ep in autre["episodes"]:
            if ep["partie"] == "epreuve":
                ep["scores"]["blanc"] += 10.0  # l'épreuve change ; le calibrage non
        e2 = ea.construire(mbs.MondeBanqueScores(autre, 17), BLANC_CONTRE_NOIR, tau=0.05)
        self.assertEqual(e1["cle_heritage"]["seuils"], e2["cle_heritage"]["seuils"])

    def test_cle_de_l_heritage(self):
        base = ea.construire(self.m, BLANC_CONTRE_NOIR, tau=0.05)
        self.assertEqual(base["empreinte_cle"], ea.construire(self.m, BLANC_CONTRE_NOIR, tau=0.05)["empreinte_cle"])
        variantes = [dict(tau=0.10), dict(tau=0.05, m_max=10), dict(tau=0.05, strate={"mode": "cout"}),
                     dict(tau=0.05, population="vivier-2"), dict(tau=0.05, garde={"a": "blanc", "b": "noir", "delta": 0.1})]
        cles = {ea.construire(self.m, BLANC_CONTRE_NOIR, **kw)["empreinte_cle"] for kw in variantes}
        self.assertEqual(len(cles | {base["empreinte_cle"]}), len(variantes) + 1)
        # le budget d'entrée n'est pas dans la clé (même affirmation), mais dans l'engagement
        b2 = ea.construire(self.m, BLANC_CONTRE_NOIR, tau=0.05, alpha_c=0.01, m_c=3)
        self.assertEqual(b2["empreinte_cle"], base["empreinte_cle"])
        self.assertNotEqual(b2["empreinte"], base["empreinte"])


class Jugement(unittest.TestCase):
    def test_bout_en_bout(self):
        m = mbs.MondeBanqueScores(banque_synthetique(random.Random(47), unites_par_partie=(100, 0, 100)), 19)
        e = ea.construire(m, BLANC_CONTRE_NOIR, tau=0.05, garde={"a": "blanc", "b": "noir", "delta": 0.10})
        r = ea.evaluer(m, e)
        self.assertTrue(r["promue"])
        self.assertEqual(r["unites_lues"], 100)
        self.assertGreater(r["bornes_basses"]["noir"], 0.0)
        self.assertEqual(r["empreinte_cle"], e["empreinte_cle"])
        nul = mbs.MondeBanqueScores(banque_synthetique(random.Random(53), unites_par_partie=(100, 0, 100), mu=(1.0, 1.0)), 19)
        e0 = ea.construire(nul, {"blanc": {"coefficients": {"blanc": 1}, "constante": -0.9}}, tau=0.05)  # rappel ≥ 0,9 : faux
        self.assertFalse(ea.evaluer(nul, e0)["promue"])

    def test_scellement(self):
        m = mbs.MondeBanqueScores(banque_synthetique(random.Random(59), unites_par_partie=(100, 0, 30)), 23)
        e = ea.construire(m, BLANC_CONTRE_NOIR, tau=0.05)
        altere = copy.deepcopy(e)
        altere["cle_heritage"]["seuils"]["blanc"] -= 1.0
        with self.assertRaises(ea.EngagementInvalide):
            ea.evaluer(m, altere)
        autre = mbs.MondeBanqueScores(banque_synthetique(random.Random(61), unites_par_partie=(100, 0, 30)), 23)
        with self.assertRaises(ea.EngagementInvalide):
            ea.evaluer(autre, e)


if __name__ == "__main__":
    unittest.main()
