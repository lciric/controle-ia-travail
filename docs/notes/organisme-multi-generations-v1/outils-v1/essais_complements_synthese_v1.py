"""Essais (cas sain et artefact, R5) de `complements_synthese_v1.py`, et banc écrit en JSON — v1.

Lancement : `python3 -I -B essais_complements_synthese_v1.py [SORTIE_BANC.json]` ; le banc (distances d'une différence
confinée à une région rare et de variantes bruitées, groupes, médoïde, N_eff, couverture) est écrit si un chemin neuf est
donné. Aucun réseau, aucune clé.
"""
import json
import os
import sys
import unittest

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import complements_synthese_v1 as C  # noqa: E402
import monde_riche_outils_v1 as M  # noqa: E402

SPEC, _ = M.generer_monde_synthetique(5, n_oracle=4000)
Z, G = M.tirer_instances(np.random.default_rng(2), 2000, 8, 3)
W = M.compiler_monde(SPEC)


def monde_avec_seuil_rare(decalage):
    s2 = json.loads(json.dumps(SPEC))
    t = s2["distracteurs"][0]
    s2["effets"].append({"id": "E99", "classe": "faible", "type": "seuil", "trait": t, "seuil": 1.5,
                         "decalage": [decalage, 0.0, -decalage]})
    return M.compiler_monde(s2)


def variante(sigma, graine):
    rng = np.random.default_rng(graine)
    s2 = json.loads(json.dumps(SPEC))
    for e in s2["effets"]:
        f = float(np.exp(rng.normal(0, sigma)))
        for c in ("pente", "decalage"):
            if c in e:
                e[c] = (np.asarray(e[c]) * f).tolist()
    return M.compiler_monde(s2)


class Strates(unittest.TestCase):
    def test_artefact_difference_rare_separee(self):
        W2 = monde_avec_seuil_rare(0.8)
        gs_global, mats = M.grouper([W, W2], Z, G, eps=0.01)
        self.assertEqual(len(gs_global), 1, mats["d"])          # la moyenne globale l'efface (d < 0,01)
        gs, m2 = C.grouper_stratifie([W, W2], Z, G, 3)
        self.assertEqual(len(gs), 2, m2["d_strat"])             # la lecture par strate la voit

    def test_sain_variantes_regroupees(self):
        lois = [W] + [variante(0.1, g) for g in range(3)]
        gs, m2 = C.grouper_stratifie(lois, Z, G, 3)
        self.assertEqual(len(gs), 1, (m2["d"], m2["d_strat"]))


class Medoide(unittest.TestCase):
    def test_independant_de_l_ordre_d_entree(self):
        lois = [W] + [variante(0.1, g) for g in range(3)]
        reps = []
        for perm in ([0, 1, 2, 3], [3, 1, 0, 2], [2, 3, 1, 0]):
            ls = [lois[i] for i in perm]
            gs, m2 = C.grouper_stratifie(ls, Z, G, 3)
            r = C.medoide(gs[0], m2["d"], m2["canon"])
            reps.append(m2["canon"][r])
        self.assertEqual(len(set(reps)), 1)


class Neff(unittest.TestCase):
    def test_lois_egales_valent_un(self):
        self.assertAlmostEqual(C.n_effectif_hellinger([W, W, W], Z, G)[0], 1.0, places=9)

    def test_lois_distinctes_valent_plus(self):
        ids = [e["id"] for e in SPEC["effets"]]
        lois = [M.monde_restreint(SPEC, [i]) for i in ids[:3]]
        self.assertGreater(C.n_effectif_hellinger(lois, Z, G)[0], 1.0)


class Couverture(unittest.TestCase):
    def test_monde_a_une_composante(self):
        s1 = {"version": "monde-riche-spec-v1", "nombre_issues": 3, "dimension": 8, "sous_populations": 3,
              "biais": SPEC["biais"], "effets": [dict(SPEC["effets"][0])], "distracteurs": []}
        l1 = M.compiler_monde(s1)
        o = M.Oracle(l1, 8, 3, n=6000)
        infos = {e["id"]: o.information_effet(s1, e["id"]) for e in s1["effets"]}
        self.assertEqual(len(C.couverture([l1], o, s1, infos)), 1)
        self.assertEqual(C.couverture([l1], o, s1, infos, archive_captes=[s1["effets"][0]["id"]]), [])


def banc(chemin):
    msk = C.strates(Z, G, 3)
    out = {"seuil_rare": {}, "variantes": {}}
    for dec in (0.3, 0.5, 0.8):
        P1, P2 = M.probas(W, Z, G), M.probas(monde_avec_seuil_rare(dec), Z, G)
        g, s = C.distance_stratifiee(P2, P1, msk)
        out["seuil_rare"][str(dec)] = {"d_global": round(g, 5), "d_strat": round(s, 5)}
    for sg in (0.05, 0.1, 0.2, 0.3):
        g, s = C.distance_stratifiee(M.probas(variante(sg, 7), Z, G), M.probas(W, Z, G), msk)
        out["variantes"][str(sg)] = {"d_global": round(g, 5), "d_strat": round(s, 5)}
    out["strates"] = len(msk)
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        banc(sys.argv.pop(1))
    unittest.main(verbosity=2)
