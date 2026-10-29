"""Essais de la porte PACE, bras de référence du juge figé (`pole/porte_pace.py` ; arXiv 2606.08106v1, extrait
`../corpus-primaire-v4/extrait-2606.08106-v1.md`) — exploratoire, non préenregistré ; jamais une sélection d'agent (N-053).

Cas sains : réduction de l'équation (2) à `pari_apparie.trajectoire_log_richesse` à un seul λ ; sous la nulle (candidat =
référence) la porte valide au plus α en fréquence sur 2 000 répétitions ; sous un gain connu planté elle valide ;
l'acceptation gloutonne valide plus souvent sous la nulle ; validité à tout instant (arrêter tôt ne gonfle pas le taux, un
test z regardé à chaque instance, lui, le gonfle) ; `comparer` côte à côte (e-BH, témoin, garde). Artefacts (R5) : NaN,
longueurs différentes, α hors ]0 ; 1[, mise hors borne, jeu d'audit vide, budget hors bornes → erreurs nommées.

Graines : dérivées par `numpy.random.SeedSequence` (via `porte_pace.graines`, numpy présent) et passées à
`random.Random` ; repli SHA-256 (`pole.outils.graine_derivee`) si numpy est absent — la méthode est vérifiée ci-dessous."""

import importlib.util
import io
import math
import os
import random
import statistics
import unittest
from contextlib import redirect_stdout

from pole import pari_apparie as pa
from pole import porte_pace as pp

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_GRAINE = 20261029
GRAINES, METHODE = pp.graines(RACINE_GRAINE, 16)


def rng(k):
    return random.Random(GRAINES[k])


def paires_simulees(r, n, s_ref, s_cand, rho):
    """Référence et candidat Bernoulli par instance, aléa partagé avec probabilité ρ ; instances indépendantes."""
    lat = [r.random() for _ in range(n)]
    ref = [int(u < s_ref) for u in lat]
    cand = [int((u if r.random() < rho else r.random()) < s_cand) for u in lat]
    return ref, cand


class Graines(unittest.TestCase):
    def test_methode_et_determinisme(self):
        try:
            import numpy  # noqa: F401
            self.assertTrue(METHODE.startswith("numpy.random.SeedSequence"), METHODE)
        except ImportError:
            self.assertTrue(METHODE.startswith("SHA-256"), METHODE)
        self.assertEqual(pp.graines(RACINE_GRAINE, 16)[0], GRAINES)
        self.assertEqual(len(set(GRAINES)), 16)


class Reduction(unittest.TestCase):
    """Équation (2), p.4 : E ← E·(1 + λ(2w − 1)) sur les paires discordantes = 1 + λ·v, v = candidat − référence."""

    def test_egale_le_produit_ecrit_a_la_main_et_la_brique_existante(self):
        r = rng(0)
        for _ in range(50):
            ref, cand = paires_simulees(r, 60, 0.4, 0.5, 0.3)
            lam = r.choice([0.1, 0.5, 0.9])
            lw, attendu = 0.0, []
            for a, b in zip(ref, cand):
                if a != b:  # égalités écartées
                    w = int(b == 1)
                    lw += math.log(1 + lam * (2 * w - 1))
                attendu.append(lw)
            obtenu = pp.trajectoire_pace(pp.paires(ref, cand), lam)
            for x, y in zip(obtenu, attendu):
                self.assertAlmostEqual(x, y, places=10)
            v = [b - a for a, b in zip(ref, cand)]
            self.assertEqual(obtenu, pa.trajectoire_log_richesse(v, lambdas=(lam,)))

    def test_arret_au_seuil_et_cout_par_lot(self):
        ref, cand = [0] * 40, [1] * 40  # toutes gagnées : 1,5^7 ≈ 17,1 < 20 ≤ 1,5^8 ≈ 25,6
        d = pp.porte_pace(ref, cand, taille_lot=1)
        self.assertTrue(d["validee"])
        self.assertEqual((d["etape_arret"], d["cout"], d["discordantes"]), (8, 8, 8))
        self.assertEqual(pp.porte_pace(ref, cand)["cout"], 10)  # lot de 10 entamé ([INFÉRÉ])
        self.assertFalse(pp.porte_pace(ref, cand, budget=7)["validee"])  # budget épuisé avant le seuil : rejet
        egalites = pp.porte_pace([1, 0] * 20, [1, 0] * 20)
        self.assertFalse(egalites["validee"])
        self.assertEqual(egalites["log_richesse"], 0.0)  # égalités : richesse inchangée
        self.assertEqual(egalites["discordantes"], 0)
        nulle = pp.porte_pace(ref, cand, lam=0.0)  # λ = 0 permis par PACE : jamais de validation
        self.assertFalse(nulle["validee"])
        self.assertEqual(nulle["etape_arret"], 40)

    def test_glouton_strict(self):
        self.assertTrue(pp.glouton([0, 1, 0], [1, 1, 0])["validee"])
        self.assertFalse(pp.glouton([0, 1, 0], [1, 0, 0])["validee"])  # égalité de score : rejet ([INFÉRÉ])


class Validite(unittest.TestCase):
    """Sous la nulle « candidat = référence » (même exactitude), instances indépendantes."""

    @classmethod
    def setUpClass(cls):
        r = rng(1)
        cls.rep, cls.n = 2000, 200
        cls.nulles = [paires_simulees(r, cls.n, 0.5, 0.5, 0.3) for _ in range(cls.rep)]

    def test_nulle_au_plus_alpha_sur_2000_repetitions(self):
        valides = sum(pp.porte_pace(ref, cand)["validee"] for ref, cand in self.nulles)
        self.assertLessEqual(valides / self.rep, 0.05, valides)
        self.assertGreater(valides, 0)  # la porte n'est pas muette : le taux observé est mesuré, pas nul par construction

    def test_glouton_valide_plus_souvent_sous_la_nulle(self):
        pace = sum(pp.porte_pace(ref, cand, budget=40)["validee"] for ref, cand in self.nulles)
        gl = sum(pp.glouton(ref[:40], cand[:40])["validee"] for ref, cand in self.nulles)
        self.assertGreater(gl, pace)
        self.assertGreater(gl / self.rep, 0.30, gl)  # ≈ (1 − P(égalité de score)) / 2
        self.assertLessEqual(pace / self.rep, 0.05)

    def test_validite_a_tout_instant(self):
        """Arrêter tôt (budget plus court, ou règle d'arrêt dépendante des données) ne gonfle pas le taux ; un test z
        unilatéral regardé à chaque instance dès la dixième, lui, dépasse α (le contrôle a des dents)."""
        taux = []
        for b in (10, 25, 50, 100, 200):
            taux.append(sum(pp.porte_pace(ref, cand, budget=b)["validee"] for ref, cand in self.nulles) / self.rep)
        self.assertEqual(taux, sorted(taux))  # arrêter plus tôt ⊆ arrêter plus tard (mêmes données)
        self.assertTrue(all(t <= 0.05 for t in taux), taux)
        # règle d'arrêt dépendante des données : abandon dès que la richesse tombe sous 1/4
        seuil, abandon = math.log(20), math.log(0.25)
        dependante = 0
        for ref, cand in self.nulles:
            for lw in pp.trajectoire_pace(pp.paires(ref, cand)):
                if lw >= seuil:
                    dependante += 1
                    break
                if lw < abandon:
                    break
        self.assertLessEqual(dependante / self.rep, taux[-1])
        naif = 0
        for ref, cand in self.nulles:
            v = [b - a for a, b in zip(ref, cand)]
            for t in range(10, self.n + 1):
                sd = statistics.pstdev(v[:t])
                if sd > 0 and statistics.fmean(v[:t]) / (sd / math.sqrt(t)) >= 1.645:
                    naif += 1
                    break
        self.assertGreater(naif / self.rep, 0.10, naif)

    def test_gain_connu_plante_valide(self):
        """Témoin planté (p.6) : exactitude 0,35 → 0,70, n = 40 comme le jeu de développement de PACE."""
        r = rng(2)
        valides = sum(pp.porte_pace(*paires_simulees(r, 40, 0.35, 0.70, 0.5))["validee"] for _ in range(300))
        self.assertGreaterEqual(valides / 300, 0.90, valides)


class Comparer(unittest.TestCase):
    def test_cote_a_cote_sous_un_gain(self):
        suite = pp.simuler_suite(rng(3), "gain", m=20, n_dev=120)
        res = pp.comparer(suite)
        self.assertEqual(res["usage"], pp.USAGE)
        self.assertEqual([d["nom"] for d in res["decisions"]], [c["nom"] for c in suite])  # ordre d'entrée, aucun rang
        self.assertFalse({"meilleur", "selection", "rang", "classement"} & set(res))
        for d in res["decisions"]:
            for b in pp.BRAS:
                self.assertIn("validee", d[b])
                self.assertIn("etape_arret", d[b])
        k = res["bras"]
        self.assertEqual(k["pace"]["temoins"], 1)
        self.assertTrue(k["pace"]["controle_positif_reussi"])
        self.assertGreaterEqual(k["glouton"]["validations"], k["pace"]["validations"])
        # e-BH de notre bras : identique à la règle appliquée à la main sur les e-valeurs arrêtées
        log_e = {d["nom"]: d["pari_apparie"]["log_e"] for d in res["decisions"]}
        attendu = pa.ebh_pondere(log_e, {n: 0.05 / 20 for n in log_e}, 0.05)
        self.assertEqual({d["nom"] for d in res["decisions"] if d["pari_apparie"]["validee"]}, attendu)
        # étiquetage par l'audit (p.6)
        for d in res["decisions"]:
            c = next(x for x in suite if x["nom"] == d["nom"])
            ecart = sum(b - a for a, b in zip(c["audit_reference"], c["audit_candidat"])) / len(c["audit_reference"])
            self.assertAlmostEqual(d["ecart_audit"], ecart)

    def test_famille_nulle_et_borne_de_suite(self):
        """Nul exact par candidat (développement tiré à neuf) : PACE ≤ α par candidat, notre bras ≤ α par suite."""
        r = rng(4)
        res = [pp.comparer(pp.simuler_suite(r, "nulle", m=10, n_dev=120, dev_reutilise=False)) for _ in range(150)]
        t = pp.agreger(res)
        self.assertLessEqual(t["pace"]["validations"] / (150 * 10), 0.05)
        self.assertLessEqual(t["pari_apparie"]["suites_avec_fausse"] / 150, 0.05)
        self.assertGreater(t["glouton"]["suites_avec_fausse"], t["pace"]["suites_avec_fausse"])

    def test_garde_bloque_le_tricheur_que_pace_valide(self):
        suite = pp.simuler_suite(rng(5), "tricheur", m=5, n_dev=120)
        res = pp.comparer(suite)
        temoin = next(d for d in res["decisions"] if d["temoin"])
        self.assertTrue(temoin["pace"]["validee"])  # PACE ne lit pas les faux positifs
        self.assertFalse(temoin["pari_apparie"]["validee"])  # garde δ : E[g] = 0,15 ≥ 0,05
        self.assertIsNotNone(temoin["pari_apparie"]["log_garde_finale"])
        sain = pp.simuler_suite(rng(5), "gain", m=5, n_dev=120)
        self.assertTrue(next(d for d in pp.comparer(sain)["decisions"] if d["temoin"])["pari_apparie"]["validee"])


class Artefacts(unittest.TestCase):
    """R5 : chaque garde a son cas sain (ci-dessus ou ici) et son artefact ; aucune ne se replie en silence."""

    def setUp(self):
        self.suite = pp.simuler_suite(rng(6), "gain", m=3, n_dev=40)

    def test_nan_et_issues_hors_domaine(self):
        for mauvais in (float("nan"), 0.5, 2, -1, "1", None):
            with self.subTest(mauvais=mauvais), self.assertRaises(pp.ResultatInvalide):
                pp.porte_pace([0, 1, mauvais], [1, 1, 0])
        self.assertTrue(pp.paires([True, False], [1.0, 0]))  # sain : booléens et 0,0 / 1,0 acceptés
        with self.assertRaises(pp.ResultatInvalide):
            pp.pari_apparie_binaire([0] * 20, [1] * 20, ecarts_faux_positifs=[0.0, float("nan")], delta=0.05)
        suite = [dict(c) for c in self.suite]
        suite[1]["audit_candidat"] = list(suite[1]["audit_candidat"])
        suite[1]["audit_candidat"][0] = float("nan")
        with self.assertRaises(pp.ResultatInvalide):
            pp.comparer(suite)

    def test_longueurs_differentes(self):
        with self.assertRaises(pp.LongueursDifferentes):
            pp.porte_pace([0, 1, 0], [1, 1])
        suite = [dict(c) for c in self.suite]
        suite[0]["audit_reference"] = suite[0]["audit_reference"][:-1]
        with self.assertRaises(pp.LongueursDifferentes):
            pp.comparer(suite)

    def test_alpha_hors_intervalle(self):
        for a in (0, 1, -0.1, 1.5, float("nan"), True, "0.05"):
            with self.subTest(alpha=a), self.assertRaises(pp.NiveauInvalide):
                pp.porte_pace([0] * 10, [1] * 10, alpha=a)
            with self.subTest(alpha=a), self.assertRaises(pp.NiveauInvalide):
                pp.comparer(self.suite, alpha=a)
        self.assertTrue(pp.porte_pace([0] * 10, [1] * 10, alpha=0.2)["validee"])  # sain : 1,5^4 ≥ 5

    def test_mise_hors_borne(self):
        for lam in (1, 1.0, -0.1, 1.5, float("nan"), float("inf"), False):
            with self.subTest(lam=lam), self.assertRaises(pp.MiseInvalide):
                pp.porte_pace([0] * 10, [1] * 10, lam=lam)
        for lam in (0.0, 0.99):
            pp.porte_pace([0] * 10, [1] * 10, lam=lam)  # sain : bornes de [0 ; 1)
        with self.assertRaises(pp.MiseInvalide):
            pp.comparer(self.suite, lambdas=(0.5, 1.0))

    def test_jeu_d_audit_vide_et_jeux_vides(self):
        suite = [dict(c) for c in self.suite]
        suite[2]["audit_reference"], suite[2]["audit_candidat"] = [], []
        with self.assertRaises(pp.JeuAuditVide):
            pp.comparer(suite)
        with self.assertRaises(pp.JeuVide):
            pp.porte_pace([], [])
        for b in (0, 41, 2.5):
            with self.subTest(budget=b), self.assertRaises(pp.JeuVide):
                pp.porte_pace([0] * 40, [1] * 40, budget=b)
        with self.assertRaises(pp.SuiteInvalide):
            pp.comparer([])
        with self.assertRaises(pp.SuiteInvalide):
            pp.comparer(self.suite + [dict(self.suite[0])])  # noms en double
        with self.assertRaises(pp.SuiteInvalide):
            pp.comparer(self.suite, m=2)  # famille plus petite que la suite
        with self.assertRaises(pp.SuiteInvalide):
            pp.porte_pace([0] * 10, [1] * 10, taille_lot=0)

    def test_erreurs_nommees_sont_des_valueerror(self):
        for e in (pp.ResultatInvalide, pp.LongueursDifferentes, pp.NiveauInvalide, pp.MiseInvalide, pp.JeuVide,
                  pp.JeuAuditVide, pp.SuiteInvalide):
            self.assertTrue(issubclass(e, pp.PorteInvalide) and issubclass(e, ValueError))


class Demonstration(unittest.TestCase):
    def test_course_courte(self):
        chemin = os.path.join(os.path.dirname(ICI), "demonstrations", "porte_pace_v1.py")
        spec = importlib.util.spec_from_file_location("porte_pace_v1", chemin)
        demo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(demo)
        tampon = io.StringIO()
        with redirect_stdout(tampon):
            lignes = demo.main(["--repetitions", "4", "--graine", "7", "--n-dev", "40"])
        sortie = tampon.getvalue()
        self.assertIn("graine 7", sortie)
        for mot in ("PACE", "pari apparié", "glouton", "nulle", "gain"):
            self.assertIn(mot, sortie)
        self.assertEqual(len(lignes), 3 * 3)  # trois régimes × trois bras


if __name__ == "__main__":
    unittest.main()
