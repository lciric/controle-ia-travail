import hashlib, sys
from pathlib import Path
racine = Path(sys.argv[1])
def r(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:100]); return s.replace(a, b)
t = (racine / "tests/test_lancer_course_affinage_mentors_v11c.py").read_text(encoding="utf-8")
assert hashlib.sha256(t.encode()).hexdigest() == "88a61acd4a55b14addbf94b4583a812a87783cd22bdb21f0c00788100e6e086b"
t = r(t, '"""Essais du lanceur v11c (dérivés des essais v11b,', '"""Essais du lanceur v11d (dérivés des essais v11c, `88a61acd…` : régression R1 de l\'essai à blanc, configuration v11d, gabarit du\n'
      'relevé des crédits v11d). Texte d\'origine : essais du lanceur v11c (dérivés des essais v11b,')
t = r(t, 'CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v11c.py"\n_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v11c", CHEMIN_LANCEUR)',
      'CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v11d.py"\n_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v11d", CHEMIN_LANCEUR)')
t = r(t, 'sys.modules["lancer_course_affinage_mentors_v11c"] = L', 'sys.modules["lancer_course_affinage_mentors_v11d"] = L')
t = r(t, 'assert L.VERSION == "lancer_course_affinage_mentors_v11c" and', 'assert L.VERSION == "lancer_course_affinage_mentors_v11d" and')
t = r(t, '    assert L.VERSION == "lancer_course_affinage_mentors_v11c"\n', '    assert L.VERSION == "lancer_course_affinage_mentors_v11d"\n')
t = r(t, 'L.PIECES["configuration"][0].endswith("configuration-course-affinage-mentors-v11c.json")',
      'L.PIECES["configuration"][0].endswith("configuration-course-affinage-mentors-v11d.json")')
t = r(t, '''        if k not in ("version", "statut", "cles", "cles_interdites", "credit_declare_usd", "especes", "changements_v11", "argon_v11"):
            assert v9.get(k) == v11.get(k), k''',
      '''        if k not in ("version", "statut", "cles", "cles_interdites", "credit_declare_usd", "especes", "changements_v11", "argon_v11",
                     "relais_persistants_v4"):
            assert v9.get(k) == v11.get(k), k
    # v11d : seul écart du bloc des relais persistants : plafond inerte retiré, note ajoutée
    attendu = {k: v for k, v in v9["relais_persistants_v4"].items() if k != "plafond_relais_claude_usd"}
    assert {k: v for k, v in v11["relais_persistants_v4"].items() if k != "note_v11d"} == attendu''')
t += (Path(sys.argv[0]).resolve().parent / "tests_propres_v11d.py").read_text(encoding="utf-8")
(racine / "tests/test_lancer_course_affinage_mentors_v11d.py").write_text(t, encoding="utf-8")
print("essais v11d écrits")
