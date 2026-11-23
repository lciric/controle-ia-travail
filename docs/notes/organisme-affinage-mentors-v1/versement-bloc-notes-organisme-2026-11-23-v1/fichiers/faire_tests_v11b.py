"""Essais du lanceur v11b, dérivés des essais v11 (`297f1eed…`) par remplacements exacts comptés, plus les essais propres à v11b.
Usage : python3 faire_tests_v11b.py RACINE"""
import hashlib, sys
from pathlib import Path
racine = Path(sys.argv[1])
ICI = Path(sys.argv[0]).resolve().parent

def r(src, a, b, n=1):
    k = src.count(a)
    assert k == n, (k, n, a[:120])
    return src.replace(a, b)

t = (racine / "tests/test_lancer_course_affinage_mentors_v11.py").read_text(encoding="utf-8")
assert hashlib.sha256(t.encode()).hexdigest() == "297f1eedaf7f45901b4d2660ea9b3fef8977762625323ef379539ad2796871a7"
t = r(t, '"""Essais du lanceur v11 ', '"""Essais du lanceur v11b (dérivés des essais v11, `297f1eed…`, par remplacements exacts ; GO_ID de la course = '
      'GO-2026-11-22-80). Texte d\'origine : essais du lanceur v11 ')
t = r(t, 'CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v11.py"\n_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v11", CHEMIN_LANCEUR)',
      'CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v11b.py"\n_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v11b", CHEMIN_LANCEUR)')
t = r(t, 'sys.modules["lancer_course_affinage_mentors_v11"] = L', 'sys.modules["lancer_course_affinage_mentors_v11b"] = L')
t = r(t, '''def ligne_go(plafond="150 USD", perimetre="course d'affinage des idées des mentors (organisme d'idéation)"):
    return (f"| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\\n|---|---|---|---|---|---|---|---|\\n"
            f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\\n" + LIGNE_GO_CLE + LIGNE_GO_SIMPL)''',
'''def ligne_go(plafond="150 USD (plafond de GO-2026-11-18-14)", perimetre="course d'affinage des idées des mentors (organisme d'idéation)"):
    # v11b : GO-2026-11-18-14 (prolongé) et GO-2026-11-22-80 (GO de la course, qui le prolonge) ; accordés « le 18 » : monde d'essai
    return (f"| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\\n|---|---|---|---|---|---|---|---|\\n"
            "| GO-2026-11-18-14 | 2026-11-18 | calcul | course d'affinage des idées des mentors | 150 USD | 2026-11-25 | Lazar | R-3215 |\\n"
            f"| {L.GO_ID} | 2026-11-18 | calcul | Prolongation de GO-2026-11-18-14 ({perimetre}) | {plafond} | 2026-12-15 | Lazar | "
            "GO-2026-11-22-77 |\\n" + LIGNE_GO_CLE + LIGNE_GO_SIMPL)''')
t = r(t, 'assert L.VERSION == "lancer_course_affinage_mentors_v11" and', 'assert L.VERSION == "lancer_course_affinage_mentors_v11b" and')
# --- bloc des GO (v11) : attentes v11b ---
t = r(t, '''def test_v11_go_avant_le_25_sans_prolongation_sain(tmp_path):
    o = L.verifier_les_go(_registre_go_essai(tmp_path, L14, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation(None))
    assert o["go"]["id"] == "GO-2026-11-18-14" and o["prolongation_course"]["valide"] is False and o["confirmation_107"]["valide"] is False''',
'''def test_v11_go_avant_le_25_sans_prolongation_sain(tmp_path):
    # v11b : GO-80 est le GO de la course, exigé même avant le 25
    o = L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation(None))
    assert o["go"]["id"] == "GO-2026-11-22-80" and o["prolongation_course"]["valide"] is True and o["confirmation_107"]["valide"] is False
    assert o["prolongation_course"]["go_initial"]["id"] == "GO-2026-11-18-14"''')
t = r(t, '''    with pytest.raises(L.Refus, match="GO-2026-11-18-14 hors de sa période"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))''',
'''    with pytest.raises(L.Refus, match="GO-2026-11-22-80 .*non valide : ligne absente"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))''')
t = r(t, '''    with pytest.raises(L.Refus, match="GO-2026-11-18-14 hors de sa période"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, rev, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))''',
'''    with pytest.raises(L.Refus, match="GO-2026-11-22-80 .*révoquée par GO-2026-11-22-140"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, rev, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))''')
t = r(t, '''    assert dep["go"]["id"] == "GO-2026-11-18-14" and dep["go"]["prolongation"]["id"] == "GO-2026-11-22-80"''',
'''    assert dep["go"]["id"] == "GO-2026-11-22-80" and dep["go"]["prolongation"]["id"] == "GO-2026-11-22-80"
    assert dep["go"]["prolongation"]["go_initial"]["id"] == "GO-2026-11-18-14"''')
# essais à trois chiffres : la ligne lue par défaut est désormais GO-80
t = r(t, '''    assert L.verifier_go(_registre_go_essai(tmp_path, L14, L_3), dt.date(2026, 11, 24))["id"] == "GO-2026-11-18-14"  # deux chiffres''',
'''    assert L.verifier_go(_registre_go_essai(tmp_path, L80, L_3), dt.date(2026, 11, 24))["id"] == "GO-2026-11-22-80"  # deux chiffres''')
t = r(t, '''    with pytest.raises(L.Refus, match="révoqué par GO-2026-11-22-150"):
        L.verifier_go(_registre_go_essai(tmp_path, L14, REV_3), dt.date(2026, 11, 24))''',
'''    with pytest.raises(L.Refus, match="révoqué par GO-2026-11-22-150"):
        L.verifier_go(_registre_go_essai(tmp_path, L14, REV_3), dt.date(2026, 11, 24), go_id="GO-2026-11-18-14")''')
t = r(t, '''    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, REV_3, L_3), tmp_path / "derive.md")
    texte = (tmp_path / "derive.md").read_text(encoding="utf-8")
    assert d["nombre_de_lignes"] == 2 and "GO-2026-11-22-150" in texte and "GO-2026-11-22-151" not in texte''',
'''    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, REV_3, L_3), tmp_path / "derive.md")
    texte = (tmp_path / "derive.md").read_text(encoding="utf-8")
    assert d["nombre_de_lignes"] == 2 and "GO-2026-11-22-150" in texte and "GO-2026-11-22-151" not in texte  # GO-14 et sa révocation''')
t = r(t, '''faux.write_text(Path(d["derive"]).read_text().replace("| 150 USD |", "| 140 USD |"), encoding="utf-8")''',
      '''faux.write_text(Path(d["derive"]).read_text().replace("| 150 USD (plafond de GO-2026-11-18-14) |", "| 140 USD |"), encoding="utf-8")''')
t = r(t, '''    assert dep["registre_go_derive"]["nombre_de_lignes"] == 1''', '''    assert dep["registre_go_derive"]["nombre_de_lignes"] == 2  # v11b : GO-80 et GO-14''')
t = r(t, '''    d = L.ecrire_registre_derive(monde["r"].registre_go, tmp_path / "derive.md")
    assert d["nombre_de_lignes"] == 2''', '''    d = L.ecrire_registre_derive(monde["r"].registre_go, tmp_path / "derive.md")
    assert d["nombre_de_lignes"] == 3  # v11b : GO-80, GO-14 et la révocation''')
t += (ICI / "tests_propres_v11b.py").read_text(encoding="utf-8")
(racine / "tests/test_lancer_course_affinage_mentors_v11b.py").write_text(t, encoding="utf-8")
print("essais v11b écrits")
