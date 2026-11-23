

# === v11c : corrections de la contre-lecture du lanceur v11b (`contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`) ==================


def test_v11c_version_et_pieces():
    assert L.VERSION == "lancer_course_affinage_mentors_v11c"
    assert L.PIECES["configuration"][0].endswith("configuration-course-affinage-mentors-v11c.json")
    assert L.PIECES["commande_carbon"][0] == "scripts/commande_gemini_flux_v2.py"
    assert L.PIECES["commande_carbon"][1] == hashlib.sha256((RACINE / "scripts/commande_gemini_flux_v2.py").read_bytes()).hexdigest()
    assert L.PIECES["configuration"][1] == hashlib.sha256((RACINE / L.PIECES["configuration"][0]).read_bytes()).hexdigest()
    assert not hasattr(L, "PART_CLAUDE_HAUT_USD") and not hasattr(L, "RESERVE_APPEL_CLAUDE_USD")
    assert "code 7" not in json.dumps(FIXE["changements_v11"]["plafond_part_claude_source"], ensure_ascii=False)


# --- constat 1 : base de l'écart au devis ------------------------------------------------------------------------------------------


def test_v11c_base_de_l_ecart_au_devis_egale_au_texte():
    assert L.PRIX_ARGON_PROPOSEUR_PAR_APPEL_USD == 0.133012 and L.PRIX_ARGON_JUGE_PAR_APPEL_USD == 0.016723
    assert L.PRIX_CARBON_PAR_APPEL_USD == 0.480472
    cinq = ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    assert round(L.devis_estimation(cinq), 3) == 35.683 == round(L.DEVIS_V5_TOTAL["cinq_especes"], 3)
    assert L.devis_estimation(cinq) != pytest.approx(40.848)                        # artefact : la base du lanceur v11b


def test_v11c_ecart_au_devis_au_manifeste_de_fin_sur_la_base_du_texte(monde):
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["ecart_au_devis"]["devis_estimation_sans_marge_usd"] == pytest.approx(L.devis_estimation(dep["especes_actives"]))
    assert "part_haut_usd" not in dep["cle_claude"]                                 # constat 15


# --- constat 3 : ligne de LUC au relevé des crédits ---------------------------------------------------------------------------


def test_v11c_ligne_de_luc_saine_au_manifeste(monde):
    assert lancer(monde["r"]) == 0
    c = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["ligne_du_releve"] == {"solde_non_lu": True, "reference": "GO-2026-11-22-124", "source": "essai : relevé du jour"}


@pytest.mark.parametrize("ligne,motif", [
    ({"reference": "GO-2026-11-22-124"}, "solde_non_lu"),                                     # mention absente
    ({"solde_non_lu": False, "reference": "GO-2026-11-22-124"}, "solde_non_lu"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-107"}, "solde_non_lu"),               # autre référence
    ({"solde_non_lu": True}, "solde_non_lu"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "solde_console_usd": 860.0}, "refusé"),   # un solde
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "credit_usd": 100.0, "reste_usd": 80.0}, "refusé"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "couverture_usd": 20.65}, "refusé"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "recharge_declaree_usd": 40.0}, "refusé"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "autre": "x"}, "refusé"),       # champ hors liste
    ({"non_lisible": True, "motif": "solde non lu (GO-124)"}, "solde_non_lu"),                 # forme du v11b
    ("solde non lu", "s'écrit"),                                                               # pas un objet
])
def test_v11c_ligne_de_luc_artefacts_refuses(monde, capsys, ligne, motif):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC=ligne))
    assert lancer(monde["r"]) == 2
    assert motif in capsys.readouterr().err
    assert not monde["r"].dossier_runs.exists() or not list(monde["r"].dossier_runs.glob("*/manifeste-lanceur-depart.json"))


def test_v11c_verifier_ligne_luc_unitaire():
    assert L.verifier_ligne_luc(luc()) == luc() and L.verifier_ligne_luc(luc(note="x"))["note"] == "x"
    for mauvais in (None, {}, luc(solde_usd=1.0), luc(reference="GO-2026-11-22-12"), luc(solde_non_lu="oui")):
        with pytest.raises(L.Refus):
            L.verifier_ligne_luc(mauvais)


# --- constat 4 : libellé de la contre-lecture ----------------------------------------------------------------------------------


def test_v11c_libelle_de_contre_lecture_sain_et_artefacts(monde, capsys):
    assert L.LIBELLE_CONTRE_LECTURE == "Opus 5.5, contre-lecteur neuf"
    for autre in ("modèle K", "Opus 5.5", "contre-lecteur neuf", "Opus 5.5 contre-lecteur"):   # artefacts d'abord (rien ne part)
        _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"]).replace("Opus 5.5, contre-lecteur neuf", autre))
        assert lancer(monde["r"]) == 2, autre
        assert "libellé" in capsys.readouterr().err
    _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"]))
    assert lancer(monde["r"]) == 0


# --- constat 5 : relecture finale du relais Claude après l'arrêt de l'orchestrateur ----------------------------------------------


def _orchestrateur_qui_ecrit_un_refus_et_sort(m, statut=400, code=3, motif=None):
    """Faux orchestrateur : attend 0,5 s (après la première lecture du lanceur), écrit une ligne de statut au journal du relais
    Claude, puis sort aussitôt avec `code`."""
    shutil.rmtree(m["orch"])
    o, commit, empreintes = faux_orchestrateur(m["tmp"])
    v8 = o / "demonstrations" / "ideation_v8.py"
    ligne = {"statut": statut, "chemin": "/v1/messages"}
    if motif:
        ligne["motif"] = motif
    v8.write_text(v8.read_text().replace("arrete = False\n", (
        "arrete = False\nif '--verifier-seulement' not in a:\n    import time\n    time.sleep(0.5)\n"
        f"    open({str(_journal_claude(m))!r}, 'a').write({json.dumps(ligne)!r} + '\\n')\n"
        + (f"    sys.exit({code})\n" if code is not None else "")), 1))
    git(o, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-q", "-am", "refus puis sortie")
    commit = subprocess.run(["git", "-C", str(o), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    empreintes = dict(empreintes, **{"demonstrations/ideation_v8.py": hashlib.sha256(v8.read_bytes()).hexdigest()})
    m["r"].orchestrateurs, m["r"].commit_orchestrateur, m["r"].empreintes_orchestrateur = (o,), commit, empreintes
    m["orch"] = o
    m["r"].intervalle_surveillance_s = 1000.0                   # une seule lecture pendant la course : au départ


@pytest.mark.parametrize("statut,motif,nature", [(400, None, "interface"), (402, "plafond de dépense du relais atteint", "relais")])
def test_v11c_refus_ecrit_apres_la_derniere_lecture_vu_a_la_relecture_finale(monde, capsys, statut, motif, nature):
    vu = _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _orchestrateur_qui_ecrit_un_refus_et_sort(monde, statut=statut, motif=motif)
    assert lancer(monde["r"]) == 5                                                  # et non 6 (orchestrateur en code 3)
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-arret-part-claude.json")
    alerte = json.loads((run / "alerte-arret-part-claude.json").read_text())
    assert alerte["moment"].startswith("relecture finale") and alerte["statut"] == statut and nature in alerte["nature"]
    if motif:
        assert alerte["cause"] == motif                                             # constat 7 : la cause réelle, lue
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["code"] == 3 and fin["code_du_lanceur"] == 5 and vu["lectures"] >= 2
    assert "arret_cle_claude" in capsys.readouterr().err


def test_v11c_mutation_sans_relecture_finale_rend_6(monde):
    """Artefact (R5) : la relecture finale retirée, le même refus donne le code 6, sans alerte."""
    m = _mutant("lanceur_v11c_mutant_finale", [("            arret_luc = surveillance.lecture_finale()\n",
                                                "            arret_luc = None\n")])
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _orchestrateur_qui_ecrit_un_refus_et_sort(monde)
    assert m.principal([], reglages=monde["r"]) == 6
    assert not (un_run(monde["r"]) / "alerte-arret-part-claude.json").exists()


def test_v11c_relecture_finale_sans_refus_ne_change_rien(monde):
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _orchestrateur_qui_ecrit_un_refus_et_sort(monde, statut=200, code=None)   # puis la course finit normalement
    assert lancer(monde["r"]) == 0
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["cle_claude_au_fil_de_l_eau"]["appels_par_statut"] == {"200": 1}


def test_v11c_lecture_finale_illisible_refaite_puis_code_5():
    class R:
        lire_etat_relais = None
    r = R()
    r.lire_etat_relais = lambda url: (_ for _ in ()).throw(OSError("injoignable"))
    s = L.SurveillanceCleClaude(r, "http://127.0.0.1:1", 45.0)
    a = s.lecture_finale()
    assert a["code"] == 5 and "illisible 3 fois" in a["motif"] and s.lignes_ecrites == 3


# --- constat 6 : journal du run, comptes par statut, dépassement --------------------------------------------------------------


def test_v11c_journal_du_run_et_comptes_au_manifeste_de_fin(monde):
    _etat_claude_apres_depart(monde, depense_usd=12.0, engage_usd=0.4, refus=0, appels_au_dessus_de_la_reserve=7,
                              depassement_max_usd=1.85, reserve_par_appel_usd=0.4)
    _journal_claude(monde).write_text("".join(json.dumps({"statut": s}) + "\n" for s in (200, 200, 429, 529, 200)), encoding="utf-8")
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    c = json.loads((run / "manifeste-lanceur-fin.json").read_text())["cle_claude_au_fil_de_l_eau"]
    assert c["appels_par_statut"] == {"200": 3, "429": 1, "529": 1}
    assert c["depassement_max_usd"] == 1.85 and c["appels_au_dessus_de_la_reserve"] == 7 and c["reserve_par_appel_usd"] == 0.4
    j = c["journal_du_run"]
    p = Path(j["chemin"])
    assert p.parent == run and p.name == L.JOURNAL_PART_CLAUDE and L.scelle(p) and j["sha256"] == L.sha256_fichier(p)
    lignes = [json.loads(x) for x in p.read_text().splitlines()]
    assert len(lignes) == j["lignes"] == c["lectures_ecrites_au_journal_du_run"] >= 2          # au fil de l'eau + relecture finale
    assert lignes[-1]["moment"] == "relecture finale" and lignes[0]["etat"]["depense_usd"] == 12.0
    assert sum(sum(x["statuts_neufs"].values()) for x in lignes) == 5                        # chaque ligne du relais comptée une fois
    texte = p.read_text()
    assert "texte" not in texte and "consigne" not in texte                                   # montants, comptes, statuts seulement


def test_v11c_ligne_du_relais_en_cours_d_ecriture_lue_la_fois_suivante(tmp_path):
    j = tmp_path / "journal.jsonl"
    j.write_text(json.dumps({"statut": 200}) + "\n" + '{"statut": 40', encoding="utf-8")     # dernière ligne sans fin de ligne

    class R:
        lire_etat_relais = staticmethod(lambda url: {"depense_usd": 1.0, "engage_usd": 0.0, "refus": 0})
    s = L.SurveillanceCleClaude(R(), "http://127.0.0.1:1", 45.0, journal=str(j), journal_run=tmp_path / "run.jsonl")
    assert s.depasse() is None and s.illisibles == 0 and s.par_statut == {"200": 1}
    with open(j, "a", encoding="utf-8") as f:
        f.write('0}\n')
    a = s.depasse()
    assert a["code"] == 5 and a["statut"] == 400 and s.par_statut == {"200": 1, "400": 1}


# --- constat 7 : nature, statut et cause réels -----------------------------------------------------------------------------------


@pytest.mark.parametrize("ligne,nature,cause", [
    ({"statut": 401, "motif": "jeton différent du jeton factice"}, "refus du relais Claude", "jeton différent du jeton factice"),
    ({"statut": 403, "motif": "modèle non permis (R-764)"}, "refus du relais Claude", "modèle non permis (R-764)"),
    ({"statut": 400, "en_flux": False, "octets": 120}, "refus de l'interface d'Anthropic, relayé", "inconnue"),
])
def test_v11c_alerte_dit_la_nature_et_la_cause_reelles(tmp_path, ligne, nature, cause):
    j = tmp_path / "journal.jsonl"
    j.write_text(json.dumps(ligne) + "\n", encoding="utf-8")

    class R:
        lire_etat_relais = staticmethod(lambda url: {"depense_usd": 1.0, "engage_usd": 0.0, "refus": 1 if "motif" in ligne else 0})
    a = L.SurveillanceCleClaude(R(), "http://127.0.0.1:1", 45.0, journal=str(j)).depasse()
    assert a["nature"] == nature and a["statut"] == ligne["statut"] and a["cause"].startswith(cause)
    assert f"statut {ligne['statut']}" in a["motif"]


def test_v11c_refus_compte_a_l_etat_sans_ligne_lue_ne_pretend_pas_402(tmp_path):
    class R:
        lire_etat_relais = staticmethod(lambda url: {"depense_usd": 1.0, "engage_usd": 0.0, "refus": 1})
    a = L.SurveillanceCleClaude(R(), "http://127.0.0.1:1", 45.0).depasse()
    assert a["nature"] == "refus du relais Claude" and a["statut"] is None and "la ligne du journal dit lequel" in a["cause"]


# --- constat 8 : réserve par appel du relais Claude -------------------------------------------------------------------------------


def test_v11c_reserve_du_relais_claude_lue_au_depart(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["procedure_relais_persistants"]["relais_vivants"]["claude"]
    assert c["reserve_par_appel_usd"] == 0.4 and c["reserve_par_appel_source"].startswith("état")
    assert c["depassement_possible_par_appel_en_vol_usd"] == pytest.approx(3.0 - 0.4)


@pytest.mark.parametrize("args,etat,issue", [
    ("0.4", 0.4, 0), ("0.5", 0.4, 2), (None, None, 2), (None, 45.0, 2), (None, -0.1, 2), ("x", 0.4, 2)])
def test_v11c_reserve_du_relais_claude_artefacts(monde, args, etat, issue):
    c = monde["cmdlines"][PID_CLAUDE]
    if args is not None:
        c += ["--reserve-par-appel", args]
    if etat is None:
        del monde["etat_claude"]["reserve_par_appel_usd"]
    else:
        monde["etat_claude"]["reserve_par_appel_usd"] = etat
    assert lancer(monde["r"]) == issue


# --- constat 9 : sonde commune v3 ------------------------------------------------------------------------------------------------


def _commune_modifiee(monde, monkeypatch, changer):
    _astra(monde, monkeypatch)                                                      # Astra déclarée : la sonde est lue
    depot = monde["depot"]
    v2 = json.loads((depot / L.SONDE_ASTRA).read_text())
    o = json.loads((depot / COMMUNE_DU_JOUR).read_text())
    changer(o)
    ecrire_sondes(depot, v2=v2, commune=o)


def test_v11c_sonde_commune_v3_saine(monde, monkeypatch):
    _commune_modifiee(monde, monkeypatch, lambda o: None)
    assert lancer(monde["r"]) == 0


@pytest.mark.parametrize("variable", [None, "OPENAI_API_KEY", "OPENAI_API_KEY_3"])
def test_v11c_sonde_commune_d_une_autre_variable_de_cle_refusee(monde, monkeypatch, capsys, variable):
    def changer(o):
        if variable is None:
            del o["relais_jete"]["variable_cle"]
        else:
            o["relais_jete"]["variable_cle"] = variable
    _commune_modifiee(monde, monkeypatch, changer)
    assert lancer(monde["r"]) == 2
    assert "variable de clé du relais jeté" in capsys.readouterr().err


def test_v11c_sonde_commune_v2_refusee(monde, monkeypatch, capsys):
    _commune_modifiee(monde, monkeypatch, lambda o: o.__setitem__("version", "sonde_astra_courses_v2"))
    assert lancer(monde["r"]) == 2
    assert "sonde_astra_courses_v2" in capsys.readouterr().err


# --- constat 11 : garde Google sur la plus longue entrée de chaque rôle, juge de la forme de l'orchestrateur ---------------------


def test_v11c_entree_de_juge_de_la_forme_de_l_orchestrateur():
    consigne = Path(_pieces_rel()["consigne_juge"]["absolu"]).read_text(encoding="utf-8")
    e = L.entree_juge_la_plus_longue(consigne)
    assert e.startswith(consigne.rstrip() + "\n\n## La fiche\n```json\n") and e.endswith("\n```\n")
    corps = e[len(consigne.rstrip() + "\n\n## La fiche\n```json\n"):-len("\n```\n")]
    fiche = json.loads(corps)
    assert len(fiche["carte"]) == L.CARACTERES_PAR_CARTE_MAX and len(e) > len(consigne) + L.CARACTERES_PAR_CARTE_MAX + 1000


def test_v11c_garde_google_rejouee_sur_la_plus_longue_entree_de_chaque_role(monde):
    if _octets_de_main("src/controle_ia/garde_google_v3.py") is None:
        pytest.skip("garde Google absente de origin/main")
    monde["r"].controler_google = None
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    roles = {x["role"]: x for x in dep["garde_google"]["argon"]["roles"]}
    consigne_j = (monde["depot"] / L.PIECES["consigne_juge"][0]).read_text(encoding="utf-8")
    assert roles["juge_ideation"]["entree_caracteres"] == len(L.entree_juge_la_plus_longue(consigne_j))
    consigne_p = (monde["depot"] / L.PIECES["consigne_proposeur"][0]).read_text(encoding="utf-8")
    plus_longue = max(len(L.consigne_servie_proposeur(consigne_p, L.expurger(L.texte_de_case(f))[0])) for f in LISTE_V11["fils"])
    assert roles["proposeur_ideation"]["entree_caracteres"] == plus_longue
    assert all(not x["problemes"] for x in roles.values())


# --- constat 15 : GO-2026-11-22-124, le montant de la part Claude lu --------------------------------------------------------------


@pytest.mark.parametrize("plafond,issue", [
    ("inchangé (150 USD ; part Claude 45 USD)", "sain"), ("inchangé (150 USD ; part Claude 45,0 USD)", "sain"),
    ("inchangé (150 USD ; part Claude 145 USD)", "refus"), ("inchangé (150 USD ; part Claude 4500 USD)", "refus"),
    ("inchangé (450 USD)", "refus"), ("45", "refus")])
def test_v11c_go_124_montant_45_lu_exactement(tmp_path, plafond, issue):
    ligne = L124.replace("| inchangé (150 USD ; part Claude 45 USD) |", f"| {plafond} |")
    reg = _registre_go_essai(tmp_path, ligne)
    if issue == "sain":
        assert L.verifier_go_simplification(reg, dt.date(2026, 11, 26))["id"] == "GO-2026-11-22-124"
    else:
        with pytest.raises(L.Refus, match="part Claude 45 USD"):
            L.verifier_go_simplification(reg, dt.date(2026, 11, 26))
