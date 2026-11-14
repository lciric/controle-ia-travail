"""Écrit essais/test_pilote_mr2_v73.py : les essais v72 portés sur le lanceur v73 (remplacements comptés) + classe V73."""
import sys
racine = sys.argv[1]
t = open(f"{racine}/essais/test_pilote_mr2_v72.py", encoding="utf-8").read()
i = t.index('\n\nimport copy\n')
doc = '''"""Essais R5 du code v73 du pilote MR-2 : les 129 essais de la v72 (dont les 115 de la v71) portés sur le lanceur v73, et la
classe neuve `V73` : le bloc gelé nomme les proposeurs par leurs clés, sans identifiant de modèle (décision de la mère sur PO-015,
R-2690), et l'identité reste gelée par l'empreinte de la configuration. Aucun réseau hors de la boucle locale, aucune clé (valeurs
factices), aucun appel de modèle ; la sonde n'est jouée que sur la doublure.

  OMP_NUM_THREADS=2 python3 -I -B -m pytest -q -p no:cacheprovider essais/test_pilote_mr2_v73.py
"""'''
t = doc + t[i:]
R = [
 ('"lanceur_pilote_v72"', '"lanceur_pilote_v73"', None),
 ('pilote_mr2_v72.py', 'pilote_mr2_v73.py', None),
 ('"lanceur-pilote-mr2-v72"', '"lanceur-pilote-mr2-v73"', None),
 ('L.verifier_bloc_du_texte(b.replace("pilote-v72 : début", "pilote-v71 : début"))', 'L.verifier_bloc_du_texte(b.replace("pilote-v73 : début", "pilote-v72 : début"))', 1),
 ('with self.assertRaisesRegex(P.Refus, "empreintes-du-code-pilote-v72"):', 'with self.assertRaisesRegex(P.Refus, "empreintes-du-code-pilote-v73"):', 1),
 ('self.assertTrue(b.startswith("<!-- empreintes-du-code-pilote-v72 : début -->\\n"))', 'self.assertTrue(b.startswith("<!-- empreintes-du-code-pilote-v73 : début -->\\n"))', 1),
 ('        for f in ("demonstrations/pilote_mr2_v71.py", "exemples/pilote-mr2-v70/configuration-pilote-mr2-v11.json"):',
  '        for f in ("demonstrations/pilote_mr2_v71.py", "demonstrations/pilote_mr2_v72.py",\n                  "exemples/pilote-mr2-v70/configuration-pilote-mr2-v11.json"):', 1),
]
for a, b, n in R:
    c = t.count(a)
    assert c >= 1 and (n is None or c == n), (a, c)
    t = t.replace(a, b)
assert "pilote_mr2_v72.py" not in t.replace('"demonstrations/pilote_mr2_v72.py",\n                  "exemples', "")
neuf = '''

class V73(unittest.TestCase):
    """Le bloc gelé v73 (R-2690) : aucun identifiant de modèle ; proposeurs nommés par leurs clés ; identité gelée par l'empreinte
    du fichier de configuration ; un bloc v72 (qui nommait les modèles) refusé par la vérification du texte."""

    def test_bloc_sans_identifiant_de_modele(self):
        conf, _ = PC.lire_configuration(CONF)
        b = L.bloc_gele()
        for nom, p in conf["proposeurs"].items():
            with self.subTest(nom):
                self.assertNotIn(p["modele"], b)
                self.assertIn(f"borne-de-sortie {nom} {p['borne_sortie_jetons']} jetons ; plafond de session", b)
        self.assertNotIn("claude-", b)
        self.assertIn("identite-des-proposeurs celle de la configuration", b)
        self.assertIn(f"{sha256_fichier(CONF)}  orchestrator/exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json", b)
        self.assertEqual((L.VERSION, L.LANCEUR), ("lanceur-pilote-mr2-v73", "demonstrations/pilote_mr2_v73.py"))

    def test_artefact_bloc_qui_nomme_les_modeles(self):
        conf, _ = PC.lire_configuration(CONF)
        b = L.bloc_gele()
        nom = "fable52"
        p = conf["proposeurs"][nom]
        avec = b.replace(f"borne-de-sortie {nom} {p['borne_sortie_jetons']}", f"borne-de-sortie {nom} {p['modele']} {p['borne_sortie_jetons']}")
        self.assertNotEqual(avec, b)
        with self.assertRaisesRegex(P.Refus, "≠ code"):
            L.verifier_bloc_du_texte("texte\\n" + avec + "suite")
        with self.assertRaisesRegex(P.Refus, "≠ code"):
            L.verifier_bloc_du_texte("texte\\n" + b.replace("identite-des-proposeurs", "identite") + "suite")
'''
neuf += open("/home/user/arbre-organisme-co/sources-essais/essais_sonde_un_v73.py.txt", encoding="utf-8").read()
fin = "\n\nif __name__ == \"__main__\":\n"
assert t.count(fin) == 1
t = t.replace(fin, neuf + fin)
open(f"{racine}/essais/test_pilote_mr2_v73.py", "x", encoding="utf-8").write(t)
print("écrit", t.count("\\n"))
