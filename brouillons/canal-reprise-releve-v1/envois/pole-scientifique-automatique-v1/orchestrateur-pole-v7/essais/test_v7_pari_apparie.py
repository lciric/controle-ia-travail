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
            c.abandonner(f, avant_partie=True)  # abandonnées avant toute partie : la décision n'a vu aucune issue
        self.assertAlmostEqual(c.seuil_log("a"), math.log(4 / 0.04))  # 100, jamais 1/0,04 = 25
        c.ajouter_trajectoire("a", [math.log(30)], unites={(c.generation, "a", i) for i in range(3)})
        self.assertEqual(c.lire(), set())  # 30 < 100 : la lecture « seule » l'aurait promue (30 ≥ 25)
        c.ajouter_trajectoire("a", [math.log(2), math.log(5)], unites={(c.generation, "a", i) for i in range(3)})  # 30 × 5 = 150 ≥ 100 : arrêt au seuil
        self.assertAlmostEqual(c.log_e["a"], math.log(150))
        self.assertIn("a", c.arretees)
        self.assertEqual(c.lire(), {"a"})
        self.assertEqual(c.bonferroni(), {"a"})

    def test_promotion_une_seule_fois_et_gel(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b"], 0.03)
        c.ajouter_trajectoire("a", [math.log(80)], unites={(c.generation, "a", i) for i in range(3)})
        self.assertEqual(c.lire(sans_partie={"b": "non lancée"}), {"a"})
        avant = c.log_e["a"]
        c.ajouter_trajectoire("a", [math.log(0.01)], unites={(c.generation, "a", i) for i in range(3)})  # gelée : rien ne change
        self.assertEqual(c.log_e["a"], avant)
        c.entrer("g2", ["e"], 0.01)
        self.assertEqual(c.lire(sans_partie={"b": "non lancée", "e": "non lancée"}), set())  # « a » reste promue
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
                    c.ajouter_trajectoire(f"c{i}", traj, unites={(c.generation, f"c{i}", i) for i in range(3)})
                    base = cohorte_seule[f"c{i}"]
                    if base + max(traj) >= -math.log(a_g[0]):
                        seule_promue = True
                    cohorte_seule[f"c{i}"] = base + traj[-1]
                if g > 0:
                    for j in range(3):
                        c.ajouter_trajectoire(f"n{g}-{j}", marche_a_prime(rng, pas), unites={(c.generation, f"n{g}-{j}", i) for i in range(3)})
                c.lire()
                if g > 0:
                    for j in range(3):
                        c.abandonner(f"n{g}-{j}", avant_partie=True)  # après la lecture, avant la génération suivante
            fausses_valides += bool(c.promues)
            fausses_seules += seule_promue
        self.assertLessEqual(fausses_valides / rep, alpha + 0.01)
        self.assertGreaterEqual(fausses_valides, 3)  # K6-6 : la lecture promeut bien quelque chose (attendu ≈ 11)
        self.assertGreater(fausses_seules, fausses_valides)
        self.assertGreater(fausses_seules / rep, 0.04)


class CorrectionsV7(unittest.TestCase):
    """Conception v7 du pari (contre-lecture de la v6) : contrat d'abandon (K6-2), retrait (K6-1), budgets (K6-5),
    ex æquo et abandonnée promue plus tard (K6-6)."""

    def test_contrat_d_abandon(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b", "c", "d"], 0.04)
        c.ajouter_trajectoire("a", [math.log(2)], unites={(c.generation, "a", i) for i in range(3)})
        c.abandonner("a")  # cas sain : la partie de la génération est ajoutée, puis la fiche gelée
        with self.assertRaises(ValueError):
            c.abandonner("b")  # artefact : abandon sans la partie de la génération courante → refus
        c.abandonner("b", trajectoire_log=[math.log(0.5)], unites={(c.generation, "b", i) for i in range(3)})  # la partie passée avec la décision
        self.assertAlmostEqual(c.log_e["b"], math.log(0.5))
        c.abandonner("c", avant_partie=True)
        with self.assertRaises(ValueError):
            c.ajouter_trajectoire("c", [math.log(3)], unites={(c.generation, "c", i) for i in range(3)})  # partie pour une gelée : refus, jamais ignorée
        c.ajouter_trajectoire("d", [math.log(2)], unites={(c.generation, "d", i) for i in range(3)})
        with self.assertRaises(ValueError):
            c.ajouter_trajectoire("d", [math.log(2)], unites={(c.generation, "d", i) for i in range(3)})  # une seule partie par génération
        c.lire()
        c.ajouter_trajectoire("d", [math.log(2)], unites={(c.generation, "d", i) for i in range(3)})  # génération 2 : permis
        self.assertAlmostEqual(c.log_e["d"], math.log(4))

    def test_retrait(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b", "c"], 0.03)
        for f, e in (("a", 200.0), ("b", 200.0), ("c", 60.0)):
            c.ajouter_trajectoire(f, [math.log(e)], unites={(c.generation, f, i) for i in range(3)})
        self.assertEqual(c.lire(), {"a", "b", "c"})  # k* = 3 : c (b·E = 0,6 ≥ 1/3) promue avec ses sœurs
        c.retirer("a", "panne confirmée de la strate")
        self.assertEqual(c.promues, {"a", "b", "c"})  # l'union garantie est celle d'avant les retraits
        self.assertEqual(c.promues_rapportees(), {"b", "c"})
        self.assertNotIn("a", c.bonferroni())
        c.entrer("g2", ["d"], 0.01)
        c.ajouter_trajectoire("d", [math.log(26)], unites={(c.generation, "d", i) for i in range(3)})  # b·E = 0,26 : promue à k = 4 si « a » comptait, pas à k = 3
        self.assertEqual(c.lire(), set())  # « a », retirée, est exclue de la lecture : k* = 2, « d » non promue
        with self.assertRaises(ValueError):
            c.retirer("b", "")

    def test_budgets_au_dessus_de_alpha(self):
        self.assertEqual(pa.ebh_pondere({"a": 0.0, "b": 0.0}, {"a": 0.3, "b": 0.2}), set())  # somme 0,5 ≤ 1 acceptée
        with self.assertRaises(ValueError):
            pa.ebh_pondere({"a": 0.0, "b": 0.0}, {"a": 0.3, "b": 0.2}, alpha=0.05)

    def test_ex_aequo_au_bord_et_abandonnee_promue_plus_tard(self):
        b = 0.05 / 3
        trois = {f: math.log(1 / (3 * b)) for f in "xyz"}  # b·E = 1/3 exactement pour les trois
        self.assertEqual(pa.ebh_pondere(trois, {f: b for f in "xyz"}), {"x", "y", "z"})
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b", "c", "d"], 0.05)  # b = 0,0125
        c.ajouter_trajectoire("d", [math.log(32)], unites={(c.generation, "d", i) for i in range(3)})  # b·E = 0,4
        for f in "abc":
            c.ajouter_trajectoire(f, [0.0], unites={(c.generation, f, i) for i in range(3)})
        self.assertEqual(c.lire(), set())
        c.abandonner("d", avant_partie=True)
        for f in "abc":
            c.ajouter_trajectoire(f, [math.log(80)], unites={(c.generation, f, i) for i in range(3)})  # b·E = 1 : arrêtées au seuil
        self.assertEqual(c.lire(), {"a", "b", "c", "d"})  # k* = 4 : la gelée à 0,4 ≥ 1/4 est promue (voulu, valide)


class CorrectionsV8(unittest.TestCase):
    """Conception v8 du pari (contre-lecture de la v7) : partie sautée (K7-1), unités relues (K7-2), abandon d'une gelée
    et traces (K7-5)."""

    def test_partie_sautee_refusee_a_la_lecture(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b"], 0.04)
        c.ajouter_trajectoire("a", [math.log(3)], unites={(c.generation, "a", i) for i in range(3)})
        with self.assertRaises(ValueError):
            c.lire()  # « b » active sans partie ni déclaration : l'artefact « j'ajoute si ça monte » est refusé
        self.assertEqual(c.lire(sans_partie={"b": "monde indisponible"}), set())  # cas sain : déclaré et tracé
        self.assertEqual(c.sans_partie[(1, "b")], "monde indisponible")

    def test_unites_deja_lues_refusees(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a"], 0.04)
        c.ajouter_trajectoire("a", [math.log(2)], unites={"u-1", "u-2", "u-3"})
        c.lire()
        with self.assertRaises(ValueError):
            c.ajouter_trajectoire("a", [math.log(2)], unites={"u-3", "u-4"})  # K8-1 : une unité en commun suffit au refus
        with self.assertRaises(ValueError):
            c.ajouter_trajectoire("a", [math.log(2)])  # K8-1 : sans identité ni déclaration → refus
        c.ajouter_trajectoire("a", [math.log(2)], unites={"u-4", "u-5"})  # disjointes : acceptées
        c.lire()
        c.ajouter_trajectoire("a", [0.0], sans_identite=True)  # déclaré : accepté et tracé
        self.assertEqual(c.parties_sans_identite, [(3, "a")])

    def test_abandon_d_une_gelee_et_traces(self):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", ["a", "b"], 0.04)
        c.abandonner("a", avant_partie=True, motif="hors sujet")
        with self.assertRaises(ValueError):
            c.abandonner("a", trajectoire_log=[math.log(5)], unites={(c.generation, "a", i) for i in range(3)})  # partie pour une gelée : refus, plus jamais en silence
        c.abandonner("a", motif="redite")  # sans partie : sans effet, mais tracé (K8-3)
        self.assertEqual(c.abandons["a"], (1, "avant_partie", "hors sujet"))
        self.assertEqual(c.abandons[("redite", "a")], [(1, "redite")])
        c.ajouter_trajectoire("b", [math.log(2)], unites={(c.generation, "b", i) for i in range(3)})
        c.abandonner("b")
        self.assertEqual(c.abandons["b"][1], "apres_partie")
        c.retirer("b", "panne")
        c.retirer("b", "panne confirmée")
        self.assertEqual([m for _, m in c.retirees["b"]], ["panne", "panne confirmée"])


if __name__ == "__main__":
    unittest.main()
