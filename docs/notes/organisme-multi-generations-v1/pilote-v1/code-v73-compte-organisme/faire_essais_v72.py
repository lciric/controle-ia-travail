"""Écrit essais/test_pilote_mr2_v72.py : les essais v71 portés sur le lanceur v72 (remplacements comptés) + essais neufs v72."""
import sys
racine = sys.argv[1]
t = open(f"{racine}/essais/test_pilote_mr2_v71.py", encoding="utf-8").read()
i = t.index('\n\nimport copy\n')
doc = '''"""Essais R5 du code v72 du pilote MR-2 : les 115 essais de la v71 (C-1 à C-18, D-1 à D-5, d-1 à d-8, A-1, A-2, a-1, a-2, a-3)
portés sur le lanceur v72, la lecture v72 de la configuration v12 et le module de la sonde v72 (le reste de l'arbre est celui de
la v71, inchangé) ; et les essais neufs de la v72 (classe `V72`, et cinq essais de bout en bout `test_v72_…` de
`ModeReelBoutEnBout`) : configuration v12 (seules les consignes de la sonde changent), lecture v12 copie fidèle de celle de la
v70, conclusion `reflexion_observee` et refus nommé « champ de réflexion absent » (cas sain « confirmé » et artefact, par la
chaîne entière sur la doublure). Aucun réseau hors de la boucle locale, aucune clé (valeurs factices), aucun appel de modèle ; la
sonde n'est jouée que sur la doublure.

  OMP_NUM_THREADS=2 python3 -I -B -m pytest -q -p no:cacheprovider essais/test_pilote_mr2_v72.py
"""'''
assert t.startswith('"""Essais R5 du code v71')
t = doc + t[i:]
R = [
 ("from pole import sonde_pilote_v71 as S  # noqa: E402\n",
  "from pole import proposeurs_pilote_v72 as PC  # noqa: E402\nfrom pole import sonde_pilote_v71 as S71  # noqa: E402\n"
  "from pole import sonde_pilote_v72 as S  # noqa: E402\n", 1),
 ('"lanceur_pilote_v71"', '"lanceur_pilote_v72"', 1),
 ('"pilote_mr2_v71.py"', '"pilote_mr2_v72.py"', 3),
 ('"demonstrations/pilote_mr2_v71.py"', '"demonstrations/pilote_mr2_v72.py"', 1),
 ('prefix="pilote-v71-', 'prefix="pilote-v72-', 2),
 ('configuration-pilote-mr2-v11.json', 'configuration-pilote-mr2-v12.json', 4),
 ('PR.lire_configuration(', 'PC.lire_configuration(', 12),
 ('{"pole/sonde_pilote_v71.py": "0" * 64}', '{"pole/sonde_pilote_v72.py": "0" * 64}', 1),
 ('self.assertIn("pole/sonde_pilote_v71.py", charges)',
  'self.assertIn("pole/sonde_pilote_v71.py", charges)\n        self.assertIn("pole/sonde_pilote_v72.py", charges)\n'
  '        self.assertIn("pole/proposeurs_pilote_v72.py", charges)', 1),
 ('"""La configuration v11 lue, ports', '"""La configuration v12 lue, ports', 1),
 ('"""Une copie de la configuration v11 (commandes', '"""Une copie de la configuration v12 (commandes', 1),
]
for a, b, n in R:
    assert t.count(a) == n, (a, t.count(a))
    t = t.replace(a, b)
neufs_bout = open(f"{sys.argv[2]}/essais_bout_en_bout_v72.py.txt", encoding="utf-8").read()
neufs_classe = open(f"{sys.argv[2]}/essais_classe_v72.py.txt", encoding="utf-8").read()
ancre = "\n\ndef conf_dialecte(nom):\n"
assert t.count(ancre) == 1
t = t.replace(ancre, "\n" + neufs_bout.rstrip("\n") + "\n" + ancre)
fin = "\n\nif __name__ == \"__main__\":\n"
assert t.count(fin) == 1
t = t.replace(fin, "\n\n" + neufs_classe.rstrip("\n") + "\n" + fin)
open(f"{racine}/essais/test_pilote_mr2_v72.py", "x", encoding="utf-8").write(t)
print("écrit", t.count("\n"), "lignes")
