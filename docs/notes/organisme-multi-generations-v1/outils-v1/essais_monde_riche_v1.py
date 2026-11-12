"""Essais ciblés (cas sain et artefact, règle R5) des outils de la conception « monde riche et doublons » — v1.

Lancement : `python3 -I -B essais_monde_riche_v1.py` (bibliothèque `unittest`). Aucun réseau, aucune clé.
"""

import json
import math
import os
import sys
import tempfile
import unittest

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import monde_riche_outils_v1 as M  # noqa: E402
import verifier_monde_kimi_v1 as V  # noqa: E402

V52B = "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/orchestrateur-v52b"
EX_RAPIDE = dict(V.EXIGENCES_DEFAUT, oracle_instances=8000, accord_oracle=0.004, accord_oracle_relatif=0.12,
                 sensibilite=dict(V.EXIGENCES_DEFAUT["sensibilite"], graines=12, faible_moyenne=[0.0, 1.0]))


def _monde(g=3):
    return M.generer_monde_synthetique(g, n_oracle=4000)


class Lois(unittest.TestCase):
    def test_egal_a_selection_pari_v52b(self):
        sys.path.insert(0, V52B)
        from pole import selection_pari as sp
        spec, _ = _monde()
        loi = M.compiler_monde(spec)
        rng = np.random.default_rng(1)
        Z, G = M.tirer_instances(rng, 200, 8, 3)
        for l in (loi, {"type": "transformee", "base": loi, "puissance": 0.6, "inclinaison": [0, 0.2, -0.1]},
                  {"type": "melange", "composantes": [loi, {"type": "fixe", "probas": [1, 2, 3]}], "poids": [0.3, 0.7]}):
            P = M.probas(l, Z, G)
            P2 = np.array([sp.proba(l, {"z": Z[i].tolist(), "g": int(G[i])}, [], i) for i in range(len(Z))])
            self.assertLess(float(np.abs(P - P2).max()), 1e-12)


class Canonique(unittest.TestCase):
    def setUp(self):
        spec, _ = _monde()
        self.loi = M.monde_restreint(spec, [spec["effets"][0]["id"], spec["effets"][2]["id"]])

    def test_sain_reformulation_egale(self):
        import puissance_monde_riche_v1 as P
        self.assertEqual(M.empreinte(M.forme_canonique(self.loi)), M.empreinte(M.forme_canonique(P._reformuler(self.loi))))

    def test_artefact_loi_changee_differe(self):
        l2 = json.loads(json.dumps(self.loi))
        feuille = l2
        while feuille["type"] != "softmax":
            feuille = feuille.get("si") or next(iter(feuille["lois"].values()))
        feuille["biais"][1] += 0.01
        self.assertNotEqual(M.empreinte(M.forme_canonique(self.loi)), M.empreinte(M.forme_canonique(l2)))


class Doublons(unittest.TestCase):
    def setUp(self):
        self.spec, self.cibles = _monde(5)
        self.Z, self.G = M.tirer_instances(np.random.default_rng(2), 1500, 8, 3)
        ids = [e["id"] for e in self.spec["effets"]]
        self.a = M.monde_restreint(self.spec, ids[:3])
        self.b = M.monde_restreint(self.spec, [ids[0], ids[1], ids[3]])  # diffère par un effet moyen

    def test_artefact_copies_regroupees(self):
        copies = [self.a, {"type": "transformee", "base": self.a, "puissance": 1.2},
                  {"type": "melange", "composantes": [self.a, {"type": "fixe", "probas": [1, 1, 1]}], "poids": [0.8, 0.2]}]
        gs, _ = M.grouper(copies, self.Z, self.G, eps=0.01)
        self.assertEqual(len(gs), 1)

    def test_sain_lois_distinctes_non_regroupees(self):
        gs, mats = M.grouper([self.a, self.b], self.Z, self.G, eps=0.01)
        self.assertEqual(len(gs), 2, mats["d"])

    def test_liaison_complete_sans_chaine(self):
        # une chaîne a ~ b ~ c avec a ≁ c (pente d'un effet moyen à 1,4 ; 1,0 ; 0,6) : jamais les trois ensemble
        ids = [e["id"] for e in self.spec["effets"]]
        a, b, c = (M.compiler_monde(self.spec, facteurs={ids[2]: f}) for f in (1.4, 1.0, 0.6))
        gs, mats = M.grouper([a, b, c], self.Z, self.G, eps=0.01)
        d = mats["d"]
        self.assertLess(max(d[0, 1], d[1, 2]), 0.01)       # une liaison simple les chaînerait toutes les trois
        self.assertGreater(d[0, 2], 0.01)
        self.assertFalse(any({0, 2} <= set(g) for g in gs), gs)
        self.assertEqual(len(gs), 2)

    def test_lois_emboitees_non_regroupees_avant_tirage(self):
        # a ⊂ (a + effet moyen) : distinctes au sens prédictif (la redondance se juge sur tirages, étape B)
        ids = [e["id"] for e in self.spec["effets"]]
        ax = M.monde_restreint(self.spec, ids[:3] + [ids[3]])
        gs, mats = M.grouper([self.a, ax], self.Z, self.G, eps=0.01)
        self.assertEqual(len(gs), 2, mats["d"])

    def test_e_valeur_de_groupe(self):
        les = [2.0, 5.0, -1.0]
        v = M.log_e_groupe(les)
        self.assertLessEqual(v, max(les))
        self.assertAlmostEqual(v, math.log(np.mean(np.exp(les))), places=9)

    def test_e_bh_par_groupe_ne_compte_pas_les_copies(self):
        # onze copies à log e = 4 : retenues ensemble par carte (seuil log(40/(0,05·11)) ≈ 4,29 non atteint, k = 11 :
        # 4 < 4,29) ; ici on vérifie seulement que le groupe ne profite pas du rang des copies
        les = {i: 4.5 for i in range(11)}
        self.assertEqual(len(M.e_bh(les, 40)), 11)          # par carte : les copies se portent l'une l'autre
        self.assertEqual(M.e_bh({0: M.log_e_groupe(list(les.values()))}, 40), [])  # par groupe : seuil log(40/0,05)


class Juge(unittest.TestCase):
    def test_sain_copie_de_l_archive_jamais_promue(self):
        spec, _ = _monde(7)
        loi = M.compiler_monde(spec)
        o = M.Oracle(loi, 8, 3, n=4000)
        k1, _, _ = M.k1_du_monde(spec, o)
        for r in range(5):
            ev = M.juger(json.loads(json.dumps(k1)), [k1], loi, 8, 3, np.random.default_rng(r))
            self.assertLessEqual(ev["log_w_max"], 1e-6)

    def test_artefact_monde_promu_contre_l_archive(self):
        spec, _ = _monde(7)
        loi = M.compiler_monde(spec)
        o = M.Oracle(loi, 8, 3, n=4000)
        k1, _, _ = M.k1_du_monde(spec, o)
        ev = M.juger(loi, [k1], loi, 8, 3, np.random.default_rng(0))
        self.assertTrue(M.promue_hors_famille(ev, 40)[0])


class Verificateur(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec, _ = _monde(11)

    def _refus(self, spec, controle):
        r = V.verifier(spec, EX_RAPIDE)
        self.assertFalse(r["conforme"])
        self.assertEqual(r["refus"]["controle"], controle, r.get("refus"))

    def test_sain_monde_synthetique_conforme(self):
        r = V.verifier(self.spec, EX_RAPIDE)
        self.assertTrue(r["conforme"], r.get("refus"))
        self.assertNotIn("pente", json.dumps(r))  # aucun coefficient au rapport

    def test_artefact_texte_libre(self):
        s = json.loads(json.dumps(self.spec))
        s["effets"][0]["note"] = "trait 3 vers l'issue 2"
        self._refus(s, "C0")

    def test_artefact_coefficient_non_borne(self):
        s = json.loads(json.dumps(self.spec))
        s["effets"][0]["pente"][0] = 9.0
        self._refus(s, "C0")

    def test_artefact_distracteur_utilise(self):
        s = json.loads(json.dumps(self.spec))
        s["effets"][0]["trait"] = s["distracteurs"][0]
        self._refus(s, "C1")

    def test_artefact_effet_hors_de_sa_classe(self):
        s = json.loads(json.dumps(self.spec))
        e = next(x for x in s["effets"] if x["classe"] == "faible")
        for c in ("pente", "decalage"):
            if c in e:
                e[c] = (np.asarray(e[c]) * 3.0).tolist()
        self._refus(s, "C3")

    def test_artefact_deux_latents(self):
        s = json.loads(json.dumps(self.spec))
        s["effets"].append({"id": "E20", "classe": "moyenne", "type": "latent", "poids_melange": 0.5, "decalage": [0.1, 0.0, -0.1]})
        s["effets"].append({"id": "E21", "classe": "moyenne", "type": "latent", "poids_melange": 0.5, "decalage": [0.1, 0.0, -0.1]})
        self._refus(s, "C1")

    def test_artefact_fuite_dans_une_piece_servie(self):
        s = self.spec
        v = next(x for x in V.valeurs_du_monde(s))
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(f"Exemple de loi : poids {v:.2f}\n")
        try:
            r = V.verifier(s, EX_RAPIDE, pieces=[f.name])
            self.assertEqual(r["refus"]["controle"], "C7")
        finally:
            os.unlink(f.name)

    def test_sain_piece_sans_fuite(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("Consigne du proposeur : écrire au plus six lois de la grammaire.\n")
        try:
            self.assertTrue(V.verifier(self.spec, EX_RAPIDE, pieces=[f.name])["conforme"])
        finally:
            os.unlink(f.name)

    def test_artefact_sensibilite_faibles_jamais_detectes(self):
        ex = dict(EX_RAPIDE, sensibilite=dict(EX_RAPIDE["sensibilite"], faible_moyenne=[0.95, 1.0]))
        r = V.verifier(self.spec, ex)
        self.assertEqual(r["refus"]["controle"], "C8")

    def test_etalonnage_ramene_dans_les_classes(self):
        s = json.loads(json.dumps(self.spec))
        for e in s["effets"]:
            for c in ("pente", "decalage"):
                if c in e:
                    e[c] = (np.asarray(e[c]) * 0.5).tolist()
        self._refus(s, "C3")
        s2, fac = V.etalonner(s, EX_RAPIDE)
        self.assertTrue(V.verifier(s2, EX_RAPIDE)["conforme"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
