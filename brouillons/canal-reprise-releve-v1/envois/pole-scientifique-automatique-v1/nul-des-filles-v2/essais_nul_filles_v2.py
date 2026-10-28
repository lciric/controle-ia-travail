"""Essais du nul des filles v2 (exploratoire). Lancer : python -I -B essais_nul_filles_v2.py"""

import math
import os
import random
import sys
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "orchestrateur-pole-v2"))

import numpy as np  # noqa: E402

import experience_2_nul_filles_v2 as ex  # noqa: E402
import nul_filles_v2 as nf  # noqa: E402
from pole import selection_pari as sp  # noqa: E402
from pole.outils import graine_derivee  # noqa: E402


def _grille_simplexe(G, pas=0.05):
    meilleur = -math.inf
    g = np.arange(0, 1 + 1e-9, pas)
    J = G.shape[1]
    assert J == 5

    def rec(prefixe, reste):
        nonlocal meilleur
        if len(prefixe) == J - 1:
            w = np.array(prefixe + [max(0.0, reste)])
            m = G @ w
            if (m > 0).all():
                meilleur = max(meilleur, float(np.log(m).sum()))
            return
        for x in g:
            if x <= reste + 1e-9:
                rec(prefixe + [x], reste - x)
    rec([], 1.0)
    return meilleur


class Ajustements(unittest.TestCase):
    def test_lineaire_contre_grille_et_borne(self):
        rng = np.random.default_rng(11)
        for _ in range(3):
            t = 30
            F = rng.uniform(0.02, 0.95, size=(t, 2))
            y = rng.integers(0, 3, size=t)
            D = np.zeros((t, 3))
            D[np.arange(t), y] = 1.0
            G = np.concatenate([F, D], axis=1)
            v, w, ecart = nf._lineaire(G)
            grille = _grille_simplexe(G)
            self.assertGreaterEqual(v, grille)  # valeur + écart ≥ tout point de la grille
            self.assertGreaterEqual(v - ecart, grille - 1e-3)
            self.assertAlmostEqual(w.sum(), 1.0, places=9)

    def test_logit_contre_grille(self):
        rng = np.random.default_rng(12)
        t = 30
        for J in (1, 2):
            X = np.concatenate([np.log(rng.dirichlet([1, 1, 1], size=t))[:, :, None] for _ in range(J)]
                               + [np.zeros((t, 3, 2))], axis=2)
            X[:, 1, J] = 1.0
            X[:, 2, J + 1] = 1.0
            y = rng.integers(0, 3, size=t)

            def f(theta):
                sc = X @ theta
                mx = sc.max(axis=1, keepdims=True)
                return float((sc[np.arange(t), y] - (mx[:, 0] + np.log(np.exp(sc - mx).sum(axis=1)))).sum())
            v, th = nf._logit(X, y, np.concatenate([np.full(J, 1.0 / J), np.zeros(2)]))
            g = np.arange(-2, 2.01, 0.25)
            grille = max(f(np.array(p)) for p in np.stack(np.meshgrid(*([g] * (J + 2))), -1).reshape(-1, J + 2))
            self.assertGreaterEqual(f(th), grille - 1e-9)
            self.assertGreaterEqual(v, f(th))


class Engagement(unittest.TestCase):
    def _cas(self):
        rng = random.Random(5)
        p1, p2 = sp.loi_softmax_aleatoire(rng), sp.loi_softmax_aleatoire(rng)
        instances = sp.tirer_instances(rng, 250)
        biblio = sp.bibliotheque_fille({"A": p1, "B": p2}, 2, sp.BIBLIOTHEQUE_STANDARD_V1) + nf.membres_ajustes({"A": p1, "B": p2})
        return p1, p2, instances, biblio

    def test_instants_cas_sain_et_artefacts(self):
        p1, p2, instances, biblio = self._cas()
        e = nf.construire_engagement_v2("f", p1, instances, 3, 0.05, biblio, 50, 0.01, (25, 100, 200))
        self.assertEqual(e["instants_lecture"], [25, 100, 200])
        for mauvais in ((), (25, 100), (100, 25, 200), (0, 200), (25, 25, 200), (25.0, 200), (25, 201), (True, 200)):
            with self.assertRaises(nf.InstantsInvalides, msg=str(mauvais)):
                nf.construire_engagement_v2("f", p1, instances, 3, 0.05, biblio, 50, 0.01, mauvais)

    def test_gardes_heritees(self):
        p1, p2, instances, biblio = self._cas()
        gele = sp.geler_engagement(nf.construire_engagement_v2("f", p1, instances, 3, 0.05, biblio, 50, 0.01))
        tirages = sp.tirer_frais(gele, p1, 1, graine_noyau=7)
        nf.evaluer_v2(gele, tirages, graine_noyau=7)  # cas sain
        gele.engagement["instants_lecture"] = [200]
        with self.assertRaises(sp.EngagementModifie):
            nf.evaluer_v2(gele, tirages, graine_noyau=7)
        autre = sp.geler_engagement(nf.construire_engagement_v2("g", p2, instances, 3, 0.05, biblio, 50, 0.01))
        with self.assertRaises(sp.TiragesNonLies):
            nf.evaluer_v2(autre, tirages, graine_noyau=7)
        with self.assertRaises(sp.PlanExecutionNonConforme):
            nf.evaluer_v2(sp.geler_engagement(nf.construire_engagement_v2("f", p1, instances, 3, 0.05, biblio, 50, 0.01)),
                          tirages, graine_noyau=8)


class Coherence(unittest.TestCase):
    def test_sans_membres_ajustes_et_lecture_continue_egale_au_juge_v1(self):
        """Nul v1, instants 1 à n : evaluer_v2 redonne exactement la richesse de selection_pari.evaluer."""
        for r in range(4):
            rng = random.Random(graine_derivee(9, "coherence", r))
            loi, monde, p1, p2, instances, q_ent, _, c = ex.scenario("parent_et_loi_aveugle", rng)
            biblio = sp.bibliotheque_fille({"A": p1, "B": p2}, 2, list(sp.BIBLIOTHEQUE_STANDARD_V1), q_ent, nombre_issues=3)
            gele = sp.geler_engagement(nf.construire_engagement_v2("f", loi, instances, 3, 0.05, biblio, c, 0.01,
                                                                   tuple(range(1, 201))))
            tirages = sp.tirer_frais(gele, monde, graine_derivee(9, "frais", r), graine_noyau=3)
            a, b = nf.evaluer_v2(gele, tirages, graine_noyau=3), sp.evaluer(gele, tirages, graine_noyau=3)
            self.assertAlmostEqual(a["log_richesse_max"], b["log_richesse_max"], places=9)
            self.assertAlmostEqual(a["log_richesse_finale"], b["log_richesse_finale"], places=9)
            self.assertEqual(a["promue"], b["promue"])

    def test_loi_dans_une_famille_ajustee_jamais_au_dessus_de_zero(self):
        for nom in ("parent_et_loi_aveugle", "parent_tempere_incline", "lineaire_et_aveugle", "produit_des_parents"):
            for r in range(3):
                _, ev = ex.essai(21, nom, "v2", r)
                self.assertLessEqual(ev["log_richesse_max"], 1e-6, f"{nom} {r}")
                self.assertFalse(ev["promue"])

    def test_variantes(self):
        parents = {"A": {"type": "fixe", "probas": [1, 1, 1]}, "B": {"type": "fixe", "probas": [1, 2, 1]}}
        noms = {v: [m["nom"] for m in nf.membres_de_variante(v, parents)] for v in nf.VARIANTES}
        self.assertEqual(noms["v1"], [])
        self.assertEqual(noms["v2"], ["ajuste_lineaire", "ajuste_log:A", "ajuste_log:B", "ajuste_log:AB"])
        self.assertEqual(noms["v2_souple"], ["ajuste_lineaire", "ajuste_log:A", "ajuste_log:B"])
        self.assertEqual(noms["v2_sans_log"], ["ajuste_lineaire"])
        self.assertEqual(noms["v2_sans_lineaire"], ["ajuste_log:A", "ajuste_log:B", "ajuste_log:AB"])


if __name__ == "__main__":
    unittest.main()
