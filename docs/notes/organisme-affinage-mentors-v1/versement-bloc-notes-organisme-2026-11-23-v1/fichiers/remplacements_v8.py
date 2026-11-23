# Exécuté par faire_tests_v8.py (fonction r et texte t déjà définis) : tests de la v6 dont la règle change en v8.
r("""def test_credit_sous_un_cinquieme_alerte_code_3(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC={"credit_usd": 5000.0, "reste_usd": 900.0, "source": "essai"}))""",
  """def test_credit_sous_un_cinquieme_alerte_code_3(monde):
    # v8 : la règle du cinquième vaut pour les clés au crédit lisible hors Claude (ici celle d'Argon)
    _releve(monde, releve(CLE_ESSAI_A={"credit_usd": 5000.0, "reste_usd": 900.0, "source": "essai"}))""", 1)

ANCIEN = """def test_minuit_non_lisible_compte_au_prix_releve(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC={"non_lisible": True, "depense_anterieure_usd": 0.0}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["reste_usd"] == 200.0 and "compté" in c["source"]
    assert dep["cle_par_espece"]["prop-opus"] == L.CLE_CLAUDE and dep["cle_par_role_interne"]["aiguilleur"] == L.CLE_CLAUDE


def test_minuit_compte_sous_le_plafond_alerte_code_3(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC={"non_lisible": True, "depense_anterieure_usd": 60.0}))
    assert lancer(monde["r"]) == 3


def test_minuit_non_lisible_sans_depense_anterieure_refuse(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC={"non_lisible": True}))
    assert lancer(monde["r"]) == 2"""
NOUVEAU = """def test_luc_non_lisible_refuse_la_regle_minuit_est_retiree(monde, capsys):
    # v8 (GO-2026-11-22-111) : « Minuit compté au prix relevé » ne s'applique plus ; LUC non lisible = refus
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC={"non_lisible": True, "depense_anterieure_usd": 0.0}))
    assert lancer(monde["r"]) == 2
    assert "solde_console_usd" in capsys.readouterr().err
    assert not hasattr(L, "CREDIT_DECLARE_CLE_CLAUDE_USD")


def test_luc_couverture_au_manifeste_et_cles_par_role(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["couverture_usd"] == 900.0 and c["solde_console_usd"] == 860.0 and c["recharge_declaree_usd"] == 40.0
    assert dep["cle_par_espece"]["prop-opus"] == L.CLE_CLAUDE and dep["cle_par_role_interne"]["aiguilleur"] == L.CLE_CLAUDE
    assert dep["cle_claude"]["exception"] == "GO-2026-11-22-107" and dep["go_exception_cle"]["id"] == "GO-2026-11-22-107"


def test_luc_couverture_sous_la_part_estimee_alerte_code_3(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC=luc(solde=0.0, recharge=20.0)))   # 20 ≤ 20,65
    assert lancer(monde["r"]) == 3"""
r(ANCIEN, NOUVEAU, 1)

r("""def test_course_v6_deja_lancee_refusee(monde):
    assert lancer(monde["r"]) == 0
    assert lancer(monde["r"]) == 2
    assert "course-affinage-mentors-v6" in L.SUFFIXE_RUN""", """def test_course_v8_deja_lancee_refusee(monde):
    assert lancer(monde["r"]) == 0
    assert lancer(monde["r"]) == 2
    assert "course-affinage-mentors-v8" in L.SUFFIXE_RUN and "-course-affinage-mentors-v10" in L.SUFFIXES_DEJA_LANCEE""", 1)

# le faux orchestrateur sait attendre un signal (arrêt propre pendant la course)
r("""arrete = False
""", """arrete = False
if comp.get("attendre"):
    import signal, time
    etat_a = {"stop": False}
    signal.signal(signal.SIGTERM, lambda n, f: etat_a.__setitem__("stop", True))
    for _ in range(200):
        if etat_a["stop"]:
            break
        time.sleep(0.05)
    arrete = etat_a["stop"]
    os.makedirs(sortie, exist_ok=True)
    json.dump({"signal_term_recu": arrete}, open(os.path.join(sortie, "signal.json"), "w"))
""", 1)

t += open(str(Path(sys.argv[0]).resolve().parent / "tests_propres_v8.py"), encoding="utf-8").read()
