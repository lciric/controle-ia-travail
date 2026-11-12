"""Essais (cas sain et artefact, R5) des outils v2 : règle de représentant, générateur v2, vérificateur v2. `python3 -I -B essais_v2.py`."""
import json
import os
import sys
import tempfile
import unittest

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import generateur_mondes_v2 as G  # noqa: E402
import monde_riche_outils_v2 as M2  # noqa: E402
import verifier_monde_v2 as V  # noqa: E402
M = M2.M
EX = dict(V.EXIGENCES_V2, oracle_instances=8000, accord_oracle=0.004, accord_oracle_relatif=0.12,
          sensibilite=dict(V.EXIGENCES_V2["sensibilite"], graines=12, faible_moyenne=[0.0, 1.0], moyenne_min=0.0))
U = {"type": "fixe", "probas": [1, 1, 1]}


class Representant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = G.generer_monde_v2(5)
        cls.W = M.compiler_monde(spec)
        cls.o = M.Oracle(cls.W, 8, 3, n=6000)
        cls.Z, cls.G = M.tirer_instances(np.random.default_rng(1), 1500, 8, 3)
        L = cls.W
        cls.lois = [L, {"type": "melange", "composantes": [L, U], "poids": [0.05, 0.95]},
                    {"type": "melange", "composantes": [L, U], "poids": [0.2, 0.8]},
                    {"type": "transformee", "base": L, "puissance": 0.3}]

    def test_sain_la_loi_forte_choisie_parmi_ses_versions_affaiblies(self):
        mats = M2.matrices(self.lois, self.Z, self.G, 3)
        gs, _ = M2.grouper_v2(self.lois, self.Z, self.G, 3, mats=mats)
        g = next(g for g in gs if 0 in g)
        self.assertGreater(len(g), 1)
        r, _ = M2.representant_v2(g, mats[0], mats[2])
        self.assertEqual(r, 0)

    def test_artefact_paire_affaiblie_jamais_choisie(self):
        # en paire, la distance symétrique est égale des deux côtés : la v1 tranche par l'empreinte ; la v2 par la couverture
        # dirigée, et, à couverture mutuelle (versions tempérées), par la tranche de choix (données fraîches hors juge)
        for j in (1, 2, 3):
            paire = [self.lois[0], self.lois[j]]
            mats = M2.matrices(paire, self.Z, self.G, 3)
            gs, _ = M2.grouper_v2(paire, self.Z, self.G, 3, mats=mats)
            if len(gs) == 1:
                choix = lambda i: M.test_de_mort(paire[i], self.W, 8, 3, np.random.default_rng(100 + i))[0]  # noqa: E731
                self.assertEqual(M2.representant_v2([0, 1], mats[0], mats[2], statistique_de_choix=choix)[0], 0)


class GenerateurV2(unittest.TestCase):
    def test_latent_compte_a_part_et_constantes_tirees(self):
        vus = set()
        for g in range(40):
            gab, lat = G.tirer_gabarit_v2(np.random.default_rng(g))
            n = {c: sum(1 for x, _ in gab if x == c) for c in ("forte", "moyenne", "faible")}
            self.assertEqual(n["forte"], 2)
            self.assertIn(n["moyenne"], (2, 3))
            self.assertIn(n["faible"], (2, 3, 4))
            vus |= {s for c, s in gab if c == "forte"}
        self.assertGreater(len(vus), 1)  # les fortes ne sont plus toujours principales

    def test_sain_monde_v2_conforme_avec_latent_et_trois_moyennes_possible(self):
        ok = 0
        for g in (3, 11):
            s = G.generer_monde_v2(g)
            r = V.verifier_v2(s, EX)
            ok += r["conforme"] or r["refus"]["controle"] != "C1"
        self.assertEqual(ok, 2)  # jamais refusé en C1 pour une raison de comptage du latent

    def test_artefact_ecriture_hors_liste_blanche(self):
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as autre:
            G.ecrire_prive([d], d, "m.json", {"x": 1})
            with self.assertRaises(PermissionError):
                G.ecrire_prive([d], autre, "m.json", {"x": 1})
            with self.assertRaises(FileExistsError):
                G.ecrire_prive([d], d, "m.json", {"x": 2})


class VerificateurV2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = G.generer_monde_v2(3)

    def test_sain_c7_nombres_ordinaires_mesures_sans_refus(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("seuils 0.05 0.02 0.5 1.2 0.1 0.25 0.75 1.5 2.0 0.3 0.4 0.6 0.8 0.9\n")
        try:
            f2 = V.mesurer_fuite(self.spec, [f.name])
            self.assertEqual(f2["egalites_six_decimales"], 0)
        finally:
            os.unlink(f.name)

    def test_artefact_c7_egalite_six_decimales(self):
        v = V.V1V.valeurs_du_monde(self.spec)[0]
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(f"poids {v:.6f}\n")
        try:
            self.assertGreaterEqual(V.mesurer_fuite(self.spec, [f.name])["egalites_six_decimales"], 1)
        finally:
            os.unlink(f.name)

    def test_wilson_certification(self):
        lo, _ = V.wilson(160, 200)          # 0,80 observé : borne basse < 0,8, non certifiée
        self.assertLess(lo, 0.8)
        lo2, _ = V.wilson(186, 200)         # 0,93 observé : certifiée
        self.assertGreaterEqual(lo2, 0.8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
