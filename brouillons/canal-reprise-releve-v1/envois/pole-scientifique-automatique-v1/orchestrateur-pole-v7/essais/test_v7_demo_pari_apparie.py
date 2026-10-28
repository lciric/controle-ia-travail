"""Essais de la version 27 : tranches d'épreuve dans `engagement_apparie.evaluer`, mémoire des lignées de clé et journal
des parties (`Lignees`), et la démonstration de bout en bout du pari apparié (`demonstrations/demo_pari_apparie_v7.py`) :
cas sains et artefacts (R5), lecture L1 / L2 / L3 à graine fixée, nul répété."""

import importlib.util
import os
import random
import unittest

from pole import engagement_apparie as ea
from pole import monde_banque_scores as mbs
from pole import pari_apparie as pa
from essais.test_v7_monde_banque_scores import banque_synthetique

ICI = os.path.dirname(os.path.abspath(__file__))


def charger_demo():
    chemin = os.path.join(os.path.dirname(ICI), "demonstrations", "demo_pari_apparie_v7.py")
    spec = importlib.util.spec_from_file_location("demo_pari_apparie_v7", chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CONTRASTE = {"noir": {"coefficients": {"blanc": 1, "noir": -1}}}


class Tranches(unittest.TestCase):
    def setUp(self):
        self.m = mbs.MondeBanqueScores(banque_synthetique(random.Random(51), unites_par_partie=(100, 0, 60)), 23)
        self.e = ea.construire(self.m, CONTRASTE, tau=0.05)
        self.unites = sorted(self.m.unites("epreuve"))

    def test_tranche_lue_puis_fraicheur(self):
        t1, t2 = self.unites[:30], self.unites[30:]
        r1 = ea.evaluer(self.m, self.e, unites=t1)
        r2 = ea.evaluer(self.m, self.e, unites=t2)
        self.assertEqual({u for _, _, u in r1["identifiants_unites"]}, set(t1))
        self.assertEqual(r1["unites"], 30)
        self.assertNotEqual(r1["empreinte_unites"], r2["empreinte_unites"])
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["f"], 0.05)
        c.ajouter_trajectoire("f", r1["trajectoire_log_min"], unites=r1["identifiants_unites"])
        c.lire()
        c.ajouter_trajectoire("f", r2["trajectoire_log_min"], unites=r2["identifiants_unites"])  # tranche disjointe : acceptée
        c.lire()
        with self.assertRaises(ValueError):  # une unité commune aux deux tranches : refusée
            c.ajouter_trajectoire("f", r1["trajectoire_log_min"][:5], unites=r1["identifiants_unites"][:5])

    def test_tranche_hors_partie_refusee(self):
        with self.assertRaises(ea.EngagementInvalide):
            ea.evaluer(self.m, self.e, unites=self.unites[:10] + ["cal-0"])

    def test_etiquette_d_ordre(self):
        t = self.unites[:30]
        r_a = ea.evaluer(self.m, self.e, unites=t, etiquette_ordre="a")
        r_b = ea.evaluer(self.m, self.e, unites=t, etiquette_ordre="b")
        self.assertEqual(r_a["empreinte_unites"], r_b["empreinte_unites"])  # mêmes unités…
        self.assertNotEqual(r_a["trajectoire_log_min"], r_b["trajectoire_log_min"])  # … autre ordre secret
        self.assertEqual(ea.evaluer(self.m, self.e, unites=t)["trajectoire_log_min"],
                         ea.evaluer(self.m, self.e, unites=t, etiquette_ordre=self.e["empreinte"])["trajectoire_log_min"])

    def test_partie_entiere_inchangee(self):
        self.assertEqual(ea.evaluer(self.m, self.e)["empreinte_unites"], ea.evaluer(self.m, self.e, unites=self.unites)["empreinte_unites"])


class LigneesEtJournal(unittest.TestCase):
    def setUp(self):
        self.m = mbs.MondeBanqueScores(banque_synthetique(random.Random(53), unites_par_partie=(100, 0, 40)), 29)
        self.e = ea.construire(self.m, CONTRASTE, tau=0.05)

    def test_relance_sous_autre_nom_refusee(self):
        lg = ea.Lignees()
        lg.entrer("f", self.e)
        lg.entrer("f", self.e)  # la même fiche peut se représenter
        with self.assertRaises(ea.EngagementInvalide):
            lg.entrer("f-bis", self.e)
        autre = ea.construire(self.m, CONTRASTE, tau=0.10)  # autre clé : autre affirmation
        lg.entrer("f-bis", autre)

    def test_journal_confronte_sans_partie(self):
        lg = ea.Lignees()
        r = ea.evaluer(self.m, self.e)
        lg.journaliser(1, "f", r)
        self.assertEqual(lg.parties_calculees(1), {"f"})
        lg.verifier_sans_partie(1, {"g": "aucune unité"})  # vraie : acceptée
        lg.verifier_sans_partie(2, {"f": "aucune unité"})  # autre génération : acceptée
        with self.assertRaises(ea.EngagementInvalide):  # artefact : la partie de f est au journal
            lg.verifier_sans_partie(1, {"f": "prétendue absence"})


class Demonstration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.demo = charger_demo()
        rng = random.Random(cls.demo.graine_derivee(20261028, "banque"))
        cls.b = cls.demo.banque(rng, 3, 30)
        cls.monde = mbs.MondeBanqueScores(cls.b, 7)

    def test_banque(self):
        d = self.monde.description_publique()
        self.assertEqual(sorted(self.b["cellules"]), sorted(self.demo.CELLULES))
        self.assertEqual(len(self.monde.unites("epreuve")), 90)
        self.assertEqual(self.demo.unites_de_tranche(self.monde, 1)[:1], ["epr-1-0"])
        self.assertEqual(len(self.demo.unites_de_tranche(self.monde, 2)), 30)
        self.assertEqual(d["effectifs"]["calibrage"]["sabote"], 0)

    def test_esperance_connue(self):
        self.assertGreater(self.demo.esperance_connue({"blanc": 1, "juge": -1}), 0)
        self.assertEqual(self.demo.esperance_connue({"blanc": 1, "blanc_jumeau": -1}), 0)
        self.assertLess(self.demo.esperance_connue({"juge": 1, "blanc": -1}), 0)

    def test_course_et_lecture(self):
        etat = self.demo.course(self.monde, 3, 0.05, 0.05, 11, n_hasard=3)
        lec = self.demo.lecture(etat)
        self.assertTrue(lec["L1_validite"]["tenue"], lec["L1_validite"])
        self.assertTrue(lec["L2_dents"]["temoin-vrai-fort"]["promue"])
        self.assertFalse(lec["L2_dents"]["temoin-vrai-tenu"]["promue"])  # écart 0,1 : hors de portée à 90 unités
        self.assertEqual(len(etat["journal"]), 3)
        self.assertAlmostEqual(etat["alpha_engage"], 0.05)
        # génération 1 : la fiche stratifiée « concentré » n'a aucune unité (tranche 1 toute « diffus ») → déclarée
        self.assertIn("temoin-vrai-concentre", etat["journal"][0]["sans_partie"])
        self.assertNotIn("temoin-vrai-concentre", etat["journal"][0]["parties"])
        # génération 2 : abandon avant partie du témoin inversé, tracé par la course
        self.assertIn(("temoin-faux-inverse", "avant_partie"), [tuple(a) for a in etat["journal"][1]["abandons"]])
        self.assertEqual(etat["abandons"]["temoin-faux-inverse"][1], "avant_partie")
        # le journal des parties ne contient que des parties calculées non vides, jamais une déclarée
        for j in etat["journal_parties"]:
            self.assertGreater(j["unites"], 0)
        # L3 : la fiche G1 est rapportée avec son comparateur le plus faible
        self.assertIn(lec["L3_G1"]["comparateur_le_plus_faible"], self.demo.COMPARATEURS_G1)

    def test_artefacts(self):
        a = self.demo.artefacts(self.monde, 0.05, 0.05, 11)
        for nom in ("relecture_tranche", "sans_partie_mensonger", "relance_sous_autre_nom"):
            self.assertTrue(a[nom].startswith("refus"), (nom, a[nom]))

    def test_nul_repete(self):
        class Args:
            nul, generations, unites_par_tranche, graine, alpha, tau = 8, 2, 20, 20261028, 0.05, 0.05
        n = self.demo.repetitions_nulles(Args)
        self.assertEqual(n["repetitions"], 8)
        self.assertLessEqual(n["au_moins_une_promotion"], 2)
        self.assertLessEqual(n["au_moins_une_bonferroni"], n["au_moins_une_promotion"] + 8)
        self.assertEqual(len(n["wilson_95"]), 2)


if __name__ == "__main__":
    unittest.main()
