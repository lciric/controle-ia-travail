"""Essais (cas sain et artefact, R5) du générateur de mondes par programme, et banc de génération — v1.

`python3 -I -B essais_generateur_mondes_v1.py` (essais) ;
`python3 -I -B essais_generateur_mondes_v1.py --banc SORTIE.json N` : N mondes de développement (graines publiques 1000…),
vérifiés au complet (C0 à C8) ; écrit, **sans aucun coefficient**, le gabarit tiré, les refus, les tailles et la puissance C8
par composante. Aucun réseau, aucune clé.
"""
import json
import os
import sys
import tempfile
import unittest
from concurrent.futures import ProcessPoolExecutor

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import generateur_mondes_v1 as GM  # noqa: E402
import monde_riche_outils_v1 as M  # noqa: E402
import verifier_monde_kimi_v1 as V  # noqa: E402

EX_RAPIDE = dict(V.EXIGENCES_DEFAUT, oracle_instances=8000, accord_oracle=0.004, accord_oracle_relatif=0.12,
                 sensibilite=dict(V.EXIGENCES_DEFAUT["sensibilite"], graines=12, faible_moyenne=[0.0, 1.0]))


class Generateur(unittest.TestCase):
    def test_sain_determinisme(self):
        a, _, _ = GM.generer(123, verifier=False)
        b, _, _ = GM.generer(123, verifier=False)
        self.assertEqual(M.json_canonique(a), M.json_canonique(b))

    def test_sain_graines_distinctes_mondes_distincts(self):
        a, _, _ = GM.generer(123, verifier=False)
        b, _, _ = GM.generer(124, verifier=False)
        self.assertNotEqual(M.json_canonique(a), M.json_canonique(b))

    def test_gabarits_dans_les_fourchettes_et_varies(self):
        vus = set()
        for g in range(60):
            gab, lat = GM.tirer_gabarit(np.random.default_rng(g))
            n = {c: sum(1 for x, _ in gab if x == c) for c in ("forte", "moyenne", "faible")}
            self.assertEqual(n["forte"], 2)
            self.assertIn(n["moyenne"], (2, 3))
            self.assertIn(n["faible"], (2, 3, 4))
            self.assertGreaterEqual(sum(1 for _, s in gab if s.startswith("interaction")), 2)
            vus.add((gab, lat))
        self.assertGreater(len(vus), 20)  # le gabarit n'est pas fixe

    def test_sain_monde_genere_conforme_et_rapport_sans_coefficient(self):
        spec, rapport, refus = GM.generer(7, exigences=EX_RAPIDE)
        self.assertIsNotNone(spec, refus)
        self.assertTrue(rapport["conforme"])
        self.assertNotIn("pente", json.dumps(rapport))
        self.assertNotIn("decalage", json.dumps(rapport))

    def test_graine_engagee(self):
        secret = b"\x01" * 32
        e = GM.engagement(secret)
        g1 = GM.graine_de_monde(secret, "ab" * 32, 0)
        self.assertNotEqual(g1, GM.graine_de_monde(secret, "ab" * 32, 1))      # mondes de rangs distincts
        self.assertNotEqual(g1, GM.graine_de_monde(secret, "cd" * 32, 0))      # liée au texte scellé
        self.assertGreaterEqual(g1, 2 ** 64)
        self.assertEqual(len(e), 64)

    def test_artefact_ecriture_publique_refusee(self):
        with self.assertRaises(PermissionError):
            GM.ecrire_prive("/home/user/controle-ia-travail/docs/notes", "monde-test.json", {"x": 1})

    def test_sain_ecriture_privee_sans_ecrasement(self):
        with tempfile.TemporaryDirectory() as d:
            GM.ecrire_prive(d, "monde.json", {"x": 1})
            with self.assertRaises(FileExistsError):
                GM.ecrire_prive(d, "monde.json", {"x": 2})

    def test_artefact_verificateur_refuse_puis_retirage(self):
        ex = dict(EX_RAPIDE, gain_monde=[5.0, 6.0])  # exigence impossible : tout tirage refusé en C4
        spec, rapport, refus = GM.generer(7, exigences=ex, essais_max=2)
        self.assertIsNone(spec)
        self.assertEqual(refus, ["C4", "C4"])


def _un_monde(g):
    spec, rapport, refus = GM.generer(1000 + g)
    if spec is None:
        return {"graine": 1000 + g, "refus": refus, "conforme": False}
    return {"graine": 1000 + g, "refus": refus, "conforme": True,
            "gabarit": [(e["classe"], e["type"]) for e in spec["effets"]], "distracteurs": len(spec["distracteurs"]),
            "tailles": {k: v["information_nat"] for k, v in rapport["tailles"].items()},
            "classes": {k: v["classe"] for k, v in rapport["tailles"].items()},
            "puissance_c8": {k: v["puissance"] for k, v in rapport["sensibilite"].items()},
            "gain_monde": rapport["ensemble_et_jeu_plante"]["gain_monde"], "gain_k1": rapport["ensemble_et_jeu_plante"]["gain_k1"]}


def banc(chemin, n):
    with ProcessPoolExecutor(4) as ex:
        mondes = list(ex.map(_un_monde, range(n)))
    c8 = {"forte": [], "moyenne": [], "faible": []}
    for m in mondes:
        if m["conforme"]:
            for k, p in m["puissance_c8"].items():
                c8[m["classes"][k]].append(p)
    resume = {"mondes": n, "conformes": sum(m["conforme"] for m in mondes),
              "tirages_refuses": sum(len(m["refus"]) for m in mondes),
              "refus_par_controle": {c: sum(m["refus"].count(c) for m in mondes) for c in ("C0", "C1", "C2", "C3", "C4", "C5", "C6", "C8")},
              "puissance_c8_par_classe": {c: {"n": len(v), "min": round(min(v), 2) if v else None,
                                              "mediane": round(float(np.median(v)), 2) if v else None,
                                              "part_certifiees_0.8": round(float(np.mean([x >= 0.8 for x in v])), 3) if v else None}
                                          for c, v in c8.items()},
              "composantes_par_monde": sorted({len(m.get("gabarit", [])) for m in mondes if m["conforme"]}),
              "latents": sum(1 for m in mondes if m["conforme"] and any(s == "latent" for _, s in m["gabarit"]))}
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump({"resume": resume, "mondes": mondes}, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(resume, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--banc":
        banc(sys.argv[2], int(sys.argv[3]))
    else:
        unittest.main(verbosity=2)
