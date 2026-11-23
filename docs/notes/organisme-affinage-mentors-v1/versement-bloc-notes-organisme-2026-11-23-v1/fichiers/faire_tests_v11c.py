"""Essais du lanceur v11c, dérivés des essais v11b (`673a20d2…`) par remplacements exacts comptés, plus les essais propres à
v11c. Usage : python3 faire_tests_v11c.py RACINE"""
import hashlib
import sys
from pathlib import Path

racine = Path(sys.argv[1])
ICI = Path(sys.argv[0]).resolve().parent


def r(src, a, b, n=1):
    k = src.count(a)
    assert k == n, (k, n, a[:120])
    return src.replace(a, b)


t = (racine / "tests/test_lancer_course_affinage_mentors_v11b.py").read_text(encoding="utf-8")
assert hashlib.sha256(t.encode()).hexdigest() == "673a20d240ecae5ac6ce8442c1a1f4e3bfcef15478efcf7c56fa7d79fe6fcc04"
t = r(t, '"""Essais du lanceur v11b (dérivés des essais v11,',
      '"""Essais du lanceur v11c (dérivés des essais v11b, `673a20d2…`, par remplacements exacts : corrections de la contre-lecture '
      'du lanceur v11b, réglages de production — 4 / 20 USD, juge à 1,00). Texte d\'origine : essais du lanceur v11b (dérivés des essais v11,')
t = r(t, 'CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v11b.py"\n_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v11b", CHEMIN_LANCEUR)',
      'CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v11c.py"\n_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v11c", CHEMIN_LANCEUR)')
t = r(t, 'sys.modules["lancer_course_affinage_mentors_v11b"] = L', 'sys.modules["lancer_course_affinage_mentors_v11c"] = L')
t = r(t, 'assert L.VERSION == "lancer_course_affinage_mentors_v11b" and', 'assert L.VERSION == "lancer_course_affinage_mentors_v11c" and')

# constat 3 : ligne de LUC au format v11c
t = r(t, '''def luc(solde=860.0, recharge=40.0, **modifs) -> dict:
    """Ligne de la clé Claude au format v11 (GO-2026-11-22-111) : solde lu à la console + recharge déclarée."""
    o = {"solde_console_usd": solde, "recharge_declaree_usd": recharge, "reserves_declarees_usd": 0.0, "source": "essai : console",
         "recharge_source": "essai : recharge automatique déclarée"}
    o.update(modifs)
    return o''', '''def luc(**modifs) -> dict:
    """Ligne de la clé Claude au format v11c (constat 3 ; GO-2026-11-22-124) : « solde non lu », référence, aucun montant."""
    o = {"solde_non_lu": True, "reference": "GO-2026-11-22-124", "source": "essai : relevé du jour"}
    o.update(modifs)
    return o''')
t = r(t, '''    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC={"non_lisible": True, "motif": "solde non lu (GO-124)"}))''',
      '''    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC=luc(note="solde non lu (GO-124)")))''')
t = r(t, '''c["ligne_du_releve"]["non_lisible"] is True and''', '''c["ligne_du_releve"]["solde_non_lu"] is True and''')
t = r(t, '''def test_v11_releve_sans_ligne_de_luc_part(monde):
    objet = releve()
    del objet["cles"][L.CLE_CLAUDE]
    _releve(monde, objet)
    assert lancer(monde["r"]) == 0                                # GO-2026-11-22-124 : le solde n'est pas une condition''',
      '''def test_v11_releve_sans_ligne_de_luc_part(monde, capsys):
    # v11c, constat 3 (renversé) : l'entrée « solde non lu, GO-2026-11-22-124 » de LUC est exigée ; absente : refus
    objet = releve()
    del objet["cles"][L.CLE_CLAUDE]
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2
    assert "s'écrit, il ne s'omet pas" in capsys.readouterr().err''')

# constat 4 : libellé
t = r(t, '''    return (f"# Contre-lecture d'essai, par le modèle K\\n\\nPréenregistrement''',
      '''    return (f"# Contre-lecture d'essai, Opus 5.5, contre-lecteur neuf\\n\\nPréenregistrement''')
t = r(t, '''    _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"]).replace("par le modèle K", "par un relecteur"))''',
      '''    _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"]).replace("Opus 5.5, contre-lecteur neuf", "par le modèle K"))''')

# constat 9 : sonde commune v3
t = r(t, '''    o = {"version": "sonde_astra_courses_v2", "horodatage_utc": "2026-11-18T07:29:55Z",''',
      '''    o = {"version": "sonde_astra_courses_v3", "horodatage_utc": "2026-11-18T07:29:55Z",''')
t = r(t, '''                         "reserve_par_appel_usd": 0.01, "programme_sha256": L.PROGRAMMES_RELAIS["astra"][1]},''',
      '''                         "reserve_par_appel_usd": 0.01, "programme_sha256": L.PROGRAMMES_RELAIS["astra"][1],
                         "variable_cle": "OPENAI_API_KEY_2"},''')
t = r(t, '''    assert L.PIECES["sonde_commune"][0] == "scripts/sonde_astra_courses_v2.py"            # v11 : sonde commune v2
    assert L.PIECES["sonde_commune"][1] == hashlib.sha256((RACINE / "scripts/sonde_astra_courses_v2.py").read_bytes()).hexdigest()''',
      '''    assert L.PIECES["sonde_commune"][0] == "scripts/sonde_astra_courses_v3.py"            # v11c : sonde commune v3
    assert L.PIECES["sonde_commune"][1] == hashlib.sha256((RACINE / "scripts/sonde_astra_courses_v3.py").read_bytes()).hexdigest()''')

# constat 12 : commande en flux v2
n = t.count('"commande_gemini_flux_v1"')
t = t.replace('"commande_gemini_flux_v1"', '"commande_gemini_flux_v2"')
t = r(t, '''    s = monde["tmp"] / "commande_gemini_flux_v1.py"''', '''    s = monde["tmp"] / "commande_gemini_flux_v2.py"''')
t = r(t, '''L.PIECES["commande_carbon"][0].endswith("commande_gemini_flux_v1.py")''', '''L.PIECES["commande_carbon"][0].endswith("commande_gemini_flux_v2.py")''')
t = r(t, '''    o = json.loads((RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v11/declaration-relais-gabarit-course-affinage-v11.json").read_text())''',
      '''    o = json.loads((RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v11/declaration-relais-gabarit-course-affinage-v11c.json").read_text())''')

# constat 13 : réglages de production dans le monde d'essai (juge à 1,00) ; constat 8 : état du relais Claude complet
t = r(t, '''    o_conf["argon_v11"]["plafond_session_juge_usd"] = 2.0''', '''    o_conf["argon_v11"]["plafond_session_juge_usd"] = 1.0           # v11c : production (constats 10 et 13)''')
t = r(t, '''    etat_claude = {"plafond_usd": 45.0, "depense_usd": 0.0, "engage_usd": 0.0, "appels": 0, "modeles_permis": list(MODELES_CLAUDE)}''',
      '''    etat_claude = {"plafond_usd": 45.0, "depense_usd": 0.0, "engage_usd": 0.0, "appels": 0, "modeles_permis": list(MODELES_CLAUDE),
                   "reserve_par_appel_usd": 0.4, "refus": 0, "appels_au_dessus_de_la_reserve": 0, "depassement_max_usd": 0.0}''')

# constat 1 : devis
t = r(t, '''    assert L.devis_estimation(v6b) == pytest.approx(40.848)                       # v11 : Carbon en flux, 0,4805 par appel (R-5018)
    assert L.devis_estimation(v6b + ["prop-kimi"]) == pytest.approx(48.5504)      # six espèces''',
      '''    assert round(L.devis_estimation(v6b), 3) == 35.683                           # v11c : base du texte (Argon à 4 / 20)
    assert L.devis_estimation(v6b + ["prop-kimi"]) == pytest.approx(42.81056)     # six espèces''')
t = r(t, '''    assert L.devis_estimation(trois) == pytest.approx(16 * (0.141 + 0.3525 + 0.276) + 96 * (0.031 + 0.037 + 0.0347))''',
      '''    assert L.devis_estimation(trois) == pytest.approx(16 * (0.141 + 0.3525 + 0.133012) + 96 * (0.031 + 0.037 + 0.016723))''')

# constats 5 et 7 : surveillance
t = r(t, '''    assert "crédit" not in alerte["motif"]                                          # le statut, pas la cause''',
      '''    assert alerte["statut"] == statut and alerte["cause"].startswith("inconnue")   # v11c : le relais ne garde pas la cause''')
t = r(t, '''    m = _mutant("lanceur_v11_mutant_journal", [("            interface = self._refus_au_journal()\\n",
                                                "            interface = None\\n")])''',
      '''    m = _mutant("lanceur_v11_mutant_journal", [("            n_lignes, neuves = self._lignes_du_relais()\\n",
                                                "            n_lignes, neuves = self.vu, []\\n")])''')

# constat 10 : juge à 1,00 exactement
t = r(t, '''    with pytest.raises(L.Refus, match="plafond minimal 0.92"):                  # vide : 0,60 ne paie pas un juge d'Argon au pire
        f0 = _fixe_juge(None)
        L.appliquer_emplacement_argon(f0)
        L.controler_pire_cas_argon(_decl_argon_reelle(), f0, LISTE_V11, _pieces_rel())''',
      '''    with pytest.raises(L.Refus, match="1.00 USD exactement"):                   # v11c : vide refusé (constat 10)
        L.appliquer_emplacement_argon(_fixe_juge(None))''')
t = r(t, '''@pytest.mark.parametrize("valeur,issue", [(1.0, "sain"), (0.92, "sain"), (0.91, "refus"), (0.6, "refus")])
def test_v11_argon_plafond_des_juges_au_plus_juste(valeur, issue):
    f = _fixe_juge(valeur)
    assert L.appliquer_emplacement_argon(f)["plafond_session_juge_usd"] == valeur and f["plafonds_session"]["juge"] == valeur
    if issue == "sain":
        o = L.controler_pire_cas_argon(_decl_argon_reelle(), f, LISTE_V11, _pieces_rel())
        assert o["roles"]["juge"]["pire_cas_appel_usd"] == pytest.approx((4030 * 4 + 45056 * 20) / 1e6, abs=1e-6)
        assert o["roles"]["juge"]["pire_cas_appel_usd"] <= valeur
        assert o["roles"]["proposeur"]["pire_cas_appel_usd"] <= 3.0
    else:
        with pytest.raises(L.Refus, match="plafond minimal"):
            L.controler_pire_cas_argon(_decl_argon_reelle(), f, LISTE_V11, _pieces_rel())''',
'''@pytest.mark.parametrize("valeur,issue", [(1.0, "sain"), (0.92, "refus"), (1.1, "refus"), (0.6, "refus"), (2.0, "refus")])
def test_v11_argon_plafond_des_juges_au_plus_juste(valeur, issue):
    # v11c (constat 10) : 1,00 exactement ; toute autre valeur refusée à la lecture de la configuration
    f = _fixe_juge(valeur)
    if issue == "sain":
        assert L.appliquer_emplacement_argon(f)["plafond_session_juge_usd"] == 1.0 and f["plafonds_session"]["juge"] == 1.0
        o = L.controler_pire_cas_argon(_decl_argon_reelle(), f, LISTE_V11, _pieces_rel())
        n = len(L.entree_juge_la_plus_longue(Path(_pieces_rel()["consigne_juge"]["absolu"]).read_text(encoding="utf-8")))
        e = L.math.ceil(n / L.CARACTERES_PAR_JETON_CARBON * (1 + L.MARGE_ENTREE_CARBON))
        assert o["roles"]["juge"]["pire_cas_appel_usd"] == pytest.approx((e * 4 + 45056 * 20) / 1e6, abs=1e-6)
        assert o["roles"]["juge"]["pire_cas_appel_usd"] <= 1.0
        assert o["roles"]["proposeur"]["pire_cas_appel_usd"] <= 3.0
    else:
        with pytest.raises(L.Refus, match="1.00 USD exactement"):
            L.appliquer_emplacement_argon(f)''')

t = r(t, '''    assert conf["plafonds_session"]["juge"] == 2.0 and "argon_v11" not in conf
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    assert dep["argon_v11"]["emplacement"] == 2.0 and dep["reglages_argon_v11_flux"]["roles"]["juge"]["plafond_minimal_usd"] == 0.92''',
      '''    assert conf["plafonds_session"]["juge"] == 1.0 and "argon_v11" not in conf          # v11c : production
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    assert dep["argon_v11"]["emplacement"] == 1.0 and dep["reglages_argon_v11_flux"]["roles"]["juge"]["plafond_minimal_usd"] == 0.92''')
t = r(t, '''    m["etat_claude"]["plafond_usd"] = 45.0  # v11 : relais Claude au plafond de la part''',
      '''    m["etat_claude"]["plafond_usd"] = 45.0  # v11 : relais Claude au plafond de la part
    m["etat_claude"]["reserve_par_appel_usd"] = 0.4  # v11c : la réserve lue n'est pas ce que l'essai mord''')
t += (ICI / "tests_propres_v11c.py").read_text(encoding="utf-8")
(racine / "tests/test_lancer_course_affinage_mentors_v11c.py").write_text(t, encoding="utf-8")
print("essais v11c écrits ;", n, "commandes factices renommées")
