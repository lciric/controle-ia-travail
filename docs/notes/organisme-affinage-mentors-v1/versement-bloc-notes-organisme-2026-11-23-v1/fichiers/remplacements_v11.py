# Exécuté par faire_tests_v11.py : coupe la fin des essais v10 (essais des v6b à v10 qui relisent des pièces des branches prep,
# la commande par lot, les lanceurs v7 à v9) ; adapte les essais dont la règle change en v11 ; les essais propres à la v11 sont
# ajoutés ensuite.
_i = t.index("# --- majeur 2, commandes exactes v7")
t = t[:_i]
r('''def test_credit_sous_un_cinquieme_alerte_code_3(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC={"credit_usd": 5000.0, "reste_usd": 900.0, "source": "essai"}))''',
  '''def test_credit_sous_un_cinquieme_alerte_code_3(monde):
    # v11 : la règle du cinquième vaut pour les clés au crédit lisible hors Claude (ici celle d'Argon)
    _releve(monde, releve(CLE_ESSAI_A={"credit_usd": 5000.0, "reste_usd": 900.0, "source": "essai"}))''', 1)
_a = t.index("def test_minuit_non_lisible_compte_au_prix_releve(monde):")
_b = t.index("def test_minuit_non_lisible_sans_depense_anterieure_refuse(monde):")
_b = t.index("\ndef ", _b + 10) + 1
t = t[:_a] + '''def test_luc_ligne_du_releve_non_lue_go_124(monde):
    # GO-2026-11-22-124 : le solde de LUC n'est pas lu ; « Minuit compté au prix relevé » est retiré ; la ligne est recopiée
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC={"non_lisible": True, "motif": "solde non lu (GO-124)"}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["condition_de_depart"] is None and c["ligne_du_releve"]["non_lisible"] is True and c["plafond_part_claude_usd"] == 45.0
    assert dep["cle_par_espece"]["prop-opus"] == L.CLE_CLAUDE and dep["cle_par_role_interne"]["aiguilleur"] == L.CLE_CLAUDE
    assert dep["cle_claude"]["exception"] == "GO-2026-11-22-107" and dep["go_simplification_cle"]["id"] == "GO-2026-11-22-124"
    assert not hasattr(L, "CREDIT_DECLARE_CLE_CLAUDE_USD")


''' + t[_b:]
r('''    assert dep["procedure_relais_persistants"]["relais_vivants"]["carbon"]["max_lots"] == 20  # v7 : marge de 4 lots''',
  '''    rv = dep["procedure_relais_persistants"]["relais_vivants"]["carbon"]                       # v11 : relais v3 en flux
    assert rv["max_appels"] == 40 and rv["delai_silence_s"] == 240.0 and rv["delai_amont_s"] == 1800.0
    assert dep["reglages_carbon_v11_flux"]["cas"]["entree_la_plus_longue"]["pire_cas_appel_usd"] <= 3.00''', 1)
r('''    assert "course-affinage-mentors-v10" in L.SUFFIXE_RUN''',
  '''    assert "course-affinage-mentors-v11" in L.SUFFIXE_RUN and "-course-affinage-mentors-v10" in L.SUFFIXES_DEJA_LANCEE''', 1)
_a = t.index("def test_v7_carbon_bornes_basses_sain_et_artefacts(monde):")
_b = t.index("\ndef ", _a + 10)
t = t[:_a] + '''def test_v7_carbon_bornes_basses_sain_et_artefacts(monde):
    """v11 : relais Gemini v3 en flux : --max-appels ≥ 40, délais explicites (silence ≤ 240 s, amont ≥ 1 500 s), pensées
    demandées à l'amont, état neuf."""
    out = L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)
    assert out["max_appels"] == 40 and out["delai_silence_s"] == 240.0 and out["delai_amont_s"] == 1800.0
    base = list(monde["cmdlines"][PID_CARBON])
    for args, etat, motif in ((["--max-appels", "32"], {"max_appels": 32}, "max-appels 32 < 40"),
                              (["--delai-silence-s", None], {}, "--delai-silence-s absent"),
                              (["--delai-silence-s", "300"], {}, "delai-silence-s 300"),
                              (["--delai-amont-s", None], {}, "--delai-amont-s absent"),
                              (["--delai-amont-s", "1000"], {}, "delai-amont-s 1000"),
                              (["--sans-pensees-amont", "AJOUT"], {}, "sans-pensees-amont"),
                              ([], {"max_appels": 8}, "max_appels"),
                              ([], {"appels": 1}, "déjà employé"),
                              ([], {"appels": None}, "sans")):
        a = list(base)
        if args:
            if args[1] == "AJOUT":
                a.append(args[0])
            else:
                k = a.index(args[0])
                if args[1] is None:
                    del a[k:k + 2]
                else:
                    a[k + 1] = args[1]
        monde["cmdlines"][PID_CARBON] = a
        sauve = dict(monde["etats"]["8791"])
        for cle, v in etat.items():
            if v is None:
                monde["etats"]["8791"].pop(cle)
            else:
                monde["etats"]["8791"][cle] = v
        with pytest.raises(L.Refus, match=motif):
            L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)
        monde["etats"]["8791"].clear()
        monde["etats"]["8791"].update(sauve)
        monde["cmdlines"][PID_CARBON] = list(base)

''' + t[_b:]
r('''    assert L.devis_estimation(v6b) == pytest.approx(41.136)                       # devis v8 (cinq espèces ; v6b : 37,576)
    assert L.devis_estimation(v6b + ["prop-kimi"]) == pytest.approx(48.8384)      # six espèces, Carbon au prix v8''',
  '''    assert L.devis_estimation(v6b) == pytest.approx(40.848)                       # v11 : Carbon en flux, 0,4805 par appel (R-5018)
    assert L.devis_estimation(v6b + ["prop-kimi"]) == pytest.approx(48.5504)      # six espèces''', 1)
r('''    chemin, sha = L.CHEMINS_MAIN_COMMANDES["carbon"], L.COMMANDES_EPINGLEES["carbon"]["commande_gemini_flux_v1.py"]''',
  '''    chemin, sha = L.CHEMINS_MAIN_COMMANDES["astra"], L.COMMANDES_EPINGLEES["astra"]["commande_astra_v1.py"]  # v11 : Carbon hors de main''', 1)
r('''        ('    champs = ("appels",) + (("depense_usd", "engage_usd") if nom in RELAIS_A_DOLLARS else ()) \\\\\\n'
         '        + (("lots_crees", "releves") if nom == "carbon" else ())  # v8 : « releves » nul exigé aussi pour Carbon\\n',
         "    champs = ()\\n")])''',
  '''        ('    champs = ("appels",) + (("depense_usd", "engage_usd") if nom in RELAIS_A_DOLLARS else ())  # v11 : plus de lots pour Carbon\\n',
         "    champs = ()\\n")])''', 1)
_a = t.index("def test_v7_sonde_commune_epinglee")
_b = t.index("\ndef ", _a + 10)
_seg = t[_a:_b]
t = t[:_a] + '''def test_v7_sonde_commune_epinglee():
    assert L.PIECES["sonde_commune"][0] == "scripts/sonde_astra_courses_v2.py"            # v11 : sonde commune v2
    assert L.PIECES["sonde_commune"][1] == hashlib.sha256((RACINE / "scripts/sonde_astra_courses_v2.py").read_bytes()).hexdigest()
    assert L.PIECES["sonde_astra"][0] == "scripts/sonde_astra_affinage_v3.py"

''' + t[_b:]

# --- monde d'essai v11 : Argon par la commande en flux et un relais Gemini v3 ; relais Claude au plafond de la part ; emplacement
# des juges rempli à 2,00 USD dans la configuration du dépôt d'essai ; réserves déclarées au relevé de LUC.
r('''        "argon": {"type": "commande_externe", "commande": ["bash", str(depot / L.PIECES["enveloppe_argon"][0])],
                  "nom_cle": "CLE_ESSAI_A", "porte_plafond": {"type": "environnement"}, "pid_relais": PID_ARGON}}}''',
  '''        "argon": {"type": "commande_externe",
                  "commande": [sys.executable, "-I", "-B", str(depot / L.PIECES["commande_carbon"][0])] + L.ARGUMENTS_COMMANDES["argon"],
                  "nom_cle": "CLE_ESSAI_A", "porte_plafond": {"type": "environnement"}, "pid_relais": PID_ARGON}}}''', 1)
r('''                PID_ARGON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v2.py"), "--variable-cle", "CLE_ESSAI_A",
                            "--port", "8788", "--max-appels", "450", "--modele", "gemini-4-argon"],''',
  '''                PID_ARGON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v3.py"), "--variable-cle", "CLE_ESSAI_A",
                            "--port", "8788", "--max-appels", "450", "--delai-silence-s", "240", "--delai-amont-s", "1800",
                            "--modele", "gemini-4-argon"],''', 1)
r('''"argon": ("relais_gemini_v2.py", hashlib.sha256((progs / "relais_gemini_v2.py").read_bytes()).hexdigest()),''',
  '''"argon": ("relais_gemini_v3.py", hashlib.sha256((progs / "relais_gemini_v3.py").read_bytes()).hexdigest()),''', 1)
r('''"--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "150", "--modeles-permis",''',
  '''"--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "45", "--modeles-permis",''', 1)
r('''    etat_claude = {"plafond_usd": 150.0, "depense_usd": 0.0,''', '''    etat_claude = {"plafond_usd": 45.0, "depense_usd": 0.0,''', 1)
r('''    o = {"solde_console_usd": solde, "recharge_declaree_usd": recharge, "source": "essai : console",''',
  '''    o = {"solde_console_usd": solde, "recharge_declaree_usd": recharge, "reserves_declarees_usd": 0.0, "source": "essai : console",''', 1)
r('''        (depot / rel).write_bytes(octets_piece(rel))''', '''        (depot / rel).write_bytes(octets_piece(rel))
    conf_rel = L.PIECES["configuration"][0]                       # v11 : emplacement des juges rempli dans le monde d'essai
    o_conf = json.loads((depot / conf_rel).read_text(encoding="utf-8"))
    o_conf["argon_v11"]["plafond_session_juge_usd"] = 2.0
    (depot / conf_rel).write_text(json.dumps(o_conf, ensure_ascii=False, indent=1) + "\\n", encoding="utf-8")
    pieces_essai = dict(L.PIECES, configuration=(conf_rel, hashlib.sha256((depot / conf_rel).read_bytes()).hexdigest()))''', 1)
r('''                   pieces=dict(L.PIECES), prereg=(prereg, PREREG_SHA), contre_lecture=depot / L.CONTRE_LECTURE,''',
  '''                   pieces=pieces_essai, prereg=(prereg, PREREG_SHA), contre_lecture=depot / L.CONTRE_LECTURE,''', 1)

r('''"--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "45", "--modeles-permis",''',
  '''"--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "45", "--journal", str(tmp_path / "journal-relais-claude.jsonl"),
                             "--modeles-permis",''', 1)
r('''"GO-2026-11-18-14 (150 USD) | 2026-11-25 | Lazar | GO-2026-11-18-14 |\\n")  # accordée « le 18 » : date du monde d'essai''',
  '''"GO-2026-11-18-14 (150 USD) | 2026-11-25 | Lazar | GO-2026-11-18-14 |\\n")  # accordée « le 18 » : date du monde d'essai
LIGNE_GO_SIMPL = ("| GO-2026-11-22-124 | 2026-11-18 | calcul | affinage de l'organisme : plancher levé, solde de LUC non lu ; exception "
                  "de GO-2026-11-22-107 prolongée au 15 décembre | inchangé (150 USD ; part Claude 45 USD) | 2026-12-15 | Lazar | "
                  "mot direct |\\n")''', 1)
r('''f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\\n" + LIGNE_GO_CLE)''',
  '''f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\\n" + LIGNE_GO_CLE + LIGNE_GO_SIMPL)''', 1)
r('''    assert fin["releve_credits_apres"]["RR_ANTHROPIC_API_KEY_LUC"]["reste_estime_usd"] == pytest.approx(884.0)''',
  '''    assert fin["releve_credits_apres"]["RR_ANTHROPIC_API_KEY_LUC"]["lisible"] is False                # GO-124 : solde non lu''', 1)
r('''    m["etat_claude"]["plafond_usd"] = 150.0''', '''    m["etat_claude"]["plafond_usd"] = 45.0  # v11 : relais Claude au plafond de la part''', 1)
