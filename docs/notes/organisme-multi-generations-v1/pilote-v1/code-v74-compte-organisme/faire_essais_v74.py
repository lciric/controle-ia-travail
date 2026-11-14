"""Écrit essais/test_pilote_mr2_v74.py : les essais v73 portés sur le lanceur et la sonde v74 (remplacements comptés, deux
essais dont le sens change sous la v74 adaptés), et les essais neufs (classe V74, essai de bout en bout de la garde)."""
import sys
racine, src = sys.argv[1], sys.argv[2]
t = open(f"{racine}/essais/test_pilote_mr2_v73.py", encoding="utf-8").read()
i = t.index('\n\nimport copy\n')
doc = '''"""Essais R5 du code v74 du pilote MR-2 : les 138 essais de la v73 portés sur le lanceur v74 et le module de la sonde v74 (deux
essais adaptés au sens neuf : un Argon sans champ de réflexion et sans jeton caché est admis en v74 ; l'artefact du refus nommé y
compte désormais des jetons cachés) ; et les essais neufs de la v74 (classe `V74`, essai de bout en bout « sonde admise puis garde
du pilote »). Aucun réseau hors de la boucle locale, aucune clé (valeurs factices), aucun appel de modèle.

  OMP_NUM_THREADS=2 python3 -I -B -m pytest -q -p no:cacheprovider essais/test_pilote_mr2_v74.py
"""'''
t = doc + t[i:]
def R(a, b, n=None):
    global t
    c = t.count(a)
    assert c >= 1 and (n is None or c == n), (a[:70], c)
    t = t.replace(a, b)
R("from pole import sonde_pilote_v72 as S  # noqa: E402\n", "from pole import sonde_pilote_v74 as S  # noqa: E402\n", 1)
R('"lanceur_pilote_v73"', '"lanceur_pilote_v74"', 1)
R('pilote_mr2_v73', 'pilote_mr2_v74')
R('"lanceur-pilote-mr2-v73"', '"lanceur-pilote-mr2-v74"')
R('L.verifier_bloc_du_texte(b.replace("pilote-v73 : début", "pilote-v72 : début"))', 'L.verifier_bloc_du_texte(b.replace("pilote-v74 : début", "pilote-v73 : début"))', 1)
R('empreintes-du-code-pilote-v73', 'empreintes-du-code-pilote-v74')
R('"releve-sonde-pilote-v72"', '"releve-sonde-pilote-v74"')
R('« releve-sonde-pilote-v72 » exigée', '« releve-sonde-pilote-v74 » exigée')
R('"sonde-pilote-v72"', '"sonde-pilote-v74"')
R('        self.assertEqual(S.conclusions_exigees("gemini"), S71.conclusions_exigees("gemini") + ("reflexion_observee",))\n',
  '        self.assertEqual(S.conclusions_exigees("gemini"), tuple(k for k in S71.conclusions_exigees("gemini") if k != "verdict_egal_a_la_regle")\n'
  '                         + ("regle_confirmee_ou_sans_effet",))  # v74\n', 1)
R('    def corps_argon(thoughts, candidats, fin, texte):\n', '    def corps_argon(thoughts, candidats, fin, texte, caches=0):\n', 1)
R('                 "totalTokenCount": 40 + candidats + (thoughts if isinstance(thoughts, int) else 0)}\n',
  '                 "totalTokenCount": 40 + candidats + (thoughts if isinstance(thoughts, int) else 0) + caches}  # v74 : jetons cachés\n', 1)
R('c = self.sonde_surchargee("sonde-v72-argon-sans-reflexion", {("gemini", False): A(None, 5, "STOP", "46"),\n'
  '                                                                     ("gemini", True): A(None, 256, "MAX_TOKENS", "x " * 256)})',
  'c = self.sonde_surchargee("sonde-v72-argon-sans-reflexion", {("gemini", False): A(None, 5, "STOP", "46", caches=7),\n'
  '                                                                     ("gemini", True): A(None, 256, "MAX_TOKENS", "x " * 256, caches=7)})', 1)
R('self.assertEqual(rel["version"], "releve-sonde-pilote-v74")' if False else 'self.assertEqual(L.VERSION, "lanceur-pilote-mr2-v74")' if False else '        self.assertNotIn("demonstrations/pilote_mr2_v74.py", g)' if False else 'class V72(unittest.TestCase):', 'class V72(unittest.TestCase):', 1)
bout = open(f"{src}/essais_v74_bout.py.txt", encoding="utf-8").read()
ancre = "\n\ndef conf_dialecte(nom):\n"
assert t.count(ancre) == 1
t = t.replace(ancre, "\n" + bout.rstrip("\n") + "\n" + ancre)
classe = open(f"{src}/essais_classe_v74.py.txt", encoding="utf-8").read()
fin = '\n\nif __name__ == "__main__":\n'
assert t.count(fin) == 1
t = t.replace(fin, classe.rstrip("\n") + "\n" + fin)
open(f"{racine}/essais/test_pilote_mr2_v74.py", "x", encoding="utf-8").write(t)
print("écrit")
