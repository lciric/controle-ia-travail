

# =================================================================================================================================
# Essais propres à la v8 (clé LUC et sa couverture au fil de l'eau, exception de clé, Astra gpt-6.2-astra, garde des appels à
# Google, palier d'Astra) ; chaque garde sur un cas sain et sur un artefact (R5), et les mutations demandées par la mère.
# =================================================================================================================================


def _etat_claude_apres_depart(m, **etat):
    """Après le manifeste de départ, le relais Claude rend `etat` (avant : l'état neuf du monde) ; `etat` vide = illisible."""
    base = m["r"].lire_etat_relais
    port = CONTEXTE["url_claude"].rsplit(":", 1)[1]
    vu = {"lectures": 0}

    def lire(url):
        if url.rsplit(":", 1)[1] == port and any(m["r"].dossier_runs.glob("*/manifeste-lanceur-depart.json")):
            vu["lectures"] += 1
            if not etat:
                raise OSError("relais Claude injoignable (essai)")
            return dict(base(url), **etat)
        return base(url)
    m["r"].lire_etat_relais = lire
    return vu


# --- 1. couverture de LUC, comptée au fil de l'eau (GO-2026-11-22-111) ----------------------------------------------------------


def test_v8_couverture_cas_sain_course_jusqu_au_bout(monde):
    vu = _etat_claude_apres_depart(monde, depense_usd=12.0, engage_usd=0.4)
    remplacer_orchestrateur(monde, attendre=False)
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    c = fin["couverture_cle_claude"]
    assert c["arret"] is None and c["couverture_usd"] == 900.0 and c["seuil_arret_usd"] == pytest.approx(899.6)
    assert c["lectures"] >= 1 and c["derniere_part_engagee_usd"] == pytest.approx(12.4) and vu["lectures"] >= 1
    assert not (run / "alerte-couverture-cle-claude.json").exists()


def test_v8_couverture_depassee_pendant_la_course_arret_propre_code_6(monde, capsys):
    _etat_claude_apres_depart(monde, depense_usd=899.3, engage_usd=0.4)     # 899,7 ≥ 900 − 0,40
    remplacer_orchestrateur(monde, attendre=True)
    assert lancer(monde["r"]) == 6
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-couverture-cle-claude.json")
    alerte = json.loads((run / "alerte-couverture-cle-claude.json").read_text())
    assert "couverture" in alerte["alerte"] and "899.7" in alerte["motif"]
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["couverture_cle_claude"]["arret"] == alerte["motif"]
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    sig = Path(dep["sortie"]) / "signal.json"                       # arrêt par signal TERM (reçu avant ou après le gestionnaire)
    assert fin["code"] == -15 or json.loads(sig.read_text())["signal_term_recu"] is True, fin["code"]
    assert "arret_couverture_cle_claude" in capsys.readouterr().err                                   # message écrit


def test_v8_couverture_etat_illisible_trois_fois_arret_propre_code_6(monde):
    _etat_claude_apres_depart(monde)                                         # aucune lecture possible après le départ
    remplacer_orchestrateur(monde, attendre=True)
    assert lancer(monde["r"]) == 6
    alerte = json.loads((un_run(monde["r"]) / "alerte-couverture-cle-claude.json").read_text())
    assert "illisible 3 fois" in alerte["motif"]


def test_v8_couverture_une_lecture_manquee_n_arrete_pas():
    class R:
        lire_etat_relais = None
    n = {"k": 0}

    def lire(url):
        n["k"] += 1
        if n["k"] == 1:
            raise OSError("manquée")
        return {"depense_usd": 1.0, "engage_usd": 0.0}
    r = R()
    r.lire_etat_relais = lire
    s = L.SurveillanceCleClaude(r, "http://127.0.0.1:1", 50.0)
    assert s.depasse() is None and s.illisibles == 1
    assert s.depasse() is None and s.illisibles == 0 and s.derniere == 1.0


def test_v8_releve_sans_luc_refuse(monde, capsys):
    objet = releve()
    del objet["cles"][L.CLE_CLAUDE]
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2
    assert "absente" in capsys.readouterr().err


def test_v8_fichier_de_releve_absent_refuse(monde, capsys):
    monde["r"].releve.unlink()
    Path(str(monde["r"].releve) + ".sha256").unlink()
    assert lancer(monde["r"]) == 2
    assert "relevé des crédits absent" in capsys.readouterr().err


@pytest.mark.parametrize("modif", [{"solde_console_usd": None}, {"recharge_declaree_usd": -1.0}, {"source": ""},
                                   {"recharge_source": None}])
def test_v8_releve_luc_incomplet_refuse(monde, modif):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC=luc(**modif)))
    assert lancer(monde["r"]) == 2


def test_v8_part_au_pire_de_luc_n_est_plus_confrontee_au_reste(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC=luc(solde=20.0, recharge=40.0)))   # 60 < part au pire 150 : départ permis
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["part_au_pire_usd"] == 150.0 and c["couverture_usd"] == 60.0 and c["motifs_d_arret"] == []


# --- 2. clé Claude : mutations (réintroduire Minuit) --------------------------------------------------------------------------


def test_v8_mutation_minuit_dans_la_declaration_refusee(monde, capsys):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_MINUIT"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    assert "MINUIT" in capsys.readouterr().err


def test_v8_mutation_minuit_dans_la_configuration_refusee():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    L.garde_cles_configuration(fixe)
    for modif in (lambda f: f["cles"].__setitem__("claude", "RR_ANTHROPIC_API_KEY_MINUIT"),
                  lambda f: f["especes"][0].__setitem__("cle", "RR_ANTHROPIC_API_KEY_MINUIT"),
                  lambda f: f["cles_interdites"].remove("RR_ANTHROPIC_API_KEY_MINUIT")):
        f = json.loads(json.dumps(fixe))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_cles_configuration(f)


def test_v8_mutation_constante_minuit_refusee_par_le_releve_et_l_environnement(monde):
    monde["r"].environnement = {"PATH": "/usr/bin:/bin", "RR_ANTHROPIC_API_KEY_MINUIT": "valeur-secrete-essai-3"}
    assert lancer(monde["r"]) == 2                                                  # LUC absente : arrêt au départ


def test_v8_configuration_v8_ne_differe_de_la_v6_que_par_les_cles():
    v6 = json.loads((RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v6/configuration-course-affinage-mentors-v6.json").read_text())
    v8 = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    for k in set(v6) | set(v8):
        if k not in ("version", "statut", "cles", "cles_interdites", "credit_declare_usd", "especes", "changements_v8"):
            assert v6.get(k) == v8.get(k), k
    assert [dict(e, cle=None) for e in v6["especes"]] == [dict(e, cle=None) for e in v8["especes"]]


# --- 3. exception de clé (GO-2026-11-22-107) ------------------------------------------------------------------------------------


@pytest.mark.parametrize("ligne", [
    "",                                                                                   # absente
    LIGNE_GO_CLE.replace("RR_ANTHROPIC_API_KEY_LUC", "RR_ANTHROPIC_API_KEY_MINUIT"),      # autre clé
    LIGNE_GO_CLE.replace("GO-2026-11-22-70", "GO-2026-11-22-71"),                         # autre règle
    LIGNE_GO_CLE.replace("| Lazar |", "| la mère |"),                                     # pas Lazar
    LIGNE_GO_CLE.replace("2026-11-25", "2026-11-21"),                                     # échue
    LIGNE_GO_CLE + "| GO-2026-11-22-120 | 2026-11-22 | révocation | révoque GO-2026-11-22-107 | — | — | Lazar | — |\n",
])
def test_v8_exception_de_cle_artefacts_refuses(monde, ligne):
    monde["r"].registre_go.write_text(ligne_go().replace(LIGNE_GO_CLE, ligne), encoding="utf-8")
    assert lancer(monde["r"]) == 2


def test_v8_exception_de_cle_cas_sain_sur_la_vraie_ligne_de_main():
    p = subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/main:registres/go.md"], capture_output=True)
    if p.returncode != 0 or b"GO-2026-11-22-107" not in p.stdout:
        pytest.skip("registre de main sans la ligne GO-2026-11-22-107")
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        reg = Path(d) / "go.md"
        reg.write_bytes(p.stdout)
        o = L.verifier_go_exception_cle(reg, dt.date(2026, 11, 22))
        assert o["id"] == "GO-2026-11-22-107" and o["par"] == "Lazar"
        with pytest.raises(L.Refus, match="période"):
            L.verifier_go_exception_cle(reg, dt.date(2026, 11, 26))


# --- 4. Astra : gpt-6.2-astra, OPENAI_API_KEY_2, sonde v3, palier ---------------------------------------------------------------


def test_v8_astra_arguments_et_modele():
    a = L.ARGUMENTS_COMMANDES["astra"]
    assert a[a.index("--modele") + 1] == "gpt-6.2-astra" and L.MODELES_RELAIS["astra"] == ["gpt-6.2-astra"]
    assert (a[a.index("--prix-entree") + 1], a[a.index("--prix-sortie") + 1]) == ("8", "40") and L.PRIX_ASTRA == (8.0, 40.0)
    assert L.CLE_ASTRA == "OPENAI_API_KEY_2"


def _astra_modifiee(monde, monkeypatch, **modifs):
    _astra(monde, monkeypatch)
    d = json.loads(monde["r"].declaration.read_text())
    d["fournisseurs"]["astra"].update(modifs)
    _decl(monde, d)


def test_v8_astra_cas_sain_au_manifeste(monde, monkeypatch):
    _astra(monde, monkeypatch)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-astra" in dep["especes_actives"] and dep["palier_astra"]["borne_entree_jetons"] < 272000
    assert dep["sonde_astra"]["modele_servi"] == "gpt-6.2-astra" and dep["cles_employees"]["astra"] == "OPENAI_API_KEY_2"


@pytest.mark.parametrize("modifs,motif", [({"modele_propose": "gpt-6-astra"}, "gpt-6.2-astra"),
                                          ({"nom_cle": "OPENAI_API_KEY"}, "OPENAI_API_KEY_2")])
def test_v8_astra_mutations_refusees(monde, monkeypatch, capsys, modifs, motif):
    _astra_modifiee(monde, monkeypatch, **modifs)
    assert lancer(monde["r"]) == 2
    assert motif in capsys.readouterr().err


def test_v8_astra_ancien_modele_dans_les_arguments_refuse(monde, monkeypatch, capsys):
    _astra(monde, monkeypatch)
    d = json.loads(monde["r"].declaration.read_text())
    d["fournisseurs"]["astra"]["commande"] = ["gpt-6-astra" if x == "gpt-6.2-astra" else x for x in d["fournisseurs"]["astra"]["commande"]]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    assert "arguments" in capsys.readouterr().err


@pytest.mark.parametrize("modifs,motif", [({"version": "sonde_astra_affinage_v2"}, "sonde épinglée"),
                                          ({"modele_servi": "gpt-6-astra"}, "modèle servi")])
def test_v8_sonde_d_astra_ancienne_refusee(monde, monkeypatch, capsys, modifs, motif):
    _astra(monde, monkeypatch)
    _sonde(monde, **modifs)
    assert lancer(monde["r"]) == 2
    assert motif in capsys.readouterr().err


def test_v8_palier_d_astra_sain_et_artefact():
    pieces = {"consigne_proposeur": {"absolu": str(RACINE / L.PIECES["consigne_proposeur"][0])}}
    liste = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
    assert L.verifier_palier_astra(pieces, liste)["borne_entree_jetons"] < 100000
    grosse = json.loads(json.dumps(liste))
    grosse["fils"][0]["idees_servies"][0]["texte_servi"] = "x" * 300000
    with pytest.raises(L.Refus, match="palier"):
        L.verifier_palier_astra(pieces, grosse)


# --- 5. garde des appels à Google (règle gelée, GO-2026-11-21-71) ---------------------------------------------------------------


COMMANDE_GOOGLE_FACTICE = r'''
import json, sys, urllib.request
a = sys.argv[1:]
url = a[a.index("--url-base") + 1]
config = json.loads(a[a.index("--config") + 1])
consigne = sys.stdin.read()
corps = {"contents": [{"role": "user", "parts": [{"text": consigne}]}], "generationConfig": config}
ouv = urllib.request.build_opener(urllib.request.ProxyHandler({}))
req = urllib.request.Request(url + "/models/gemini-4-carbon:generateContent", data=json.dumps(corps).encode(), method="POST",
                             headers={"Content-Type": "application/json"})
try:
    ouv.open(req, timeout=10)
except Exception:
    pass
print(json.dumps({"texte": "", "cout_usd": 1e-6, "erreur": "capturé"}))
sys.exit(3)
'''


def _pieces_garde(tmp_path):
    o = _octets_de_main("src/controle_ia/garde_google_v3.py")
    if o is None:
        pytest.skip("garde Google absente de origin/main")
    g = tmp_path / "garde_google_v3.py"
    g.write_bytes(o)
    pieces = {k: {"chemin": v[0], "absolu": str(RACINE / v[0]), "sha256": v[1]} for k, v in L.PIECES.items()}
    pieces["garde_google"]["absolu"] = str(g)
    return pieces


def _carbon_factice(tmp_path, config, provision="8192"):
    s = tmp_path / "commande_google_factice.py"
    s.write_text(COMMANDE_GOOGLE_FACTICE, encoding="utf-8")
    return {"commande": [sys.executable, "-I", "-B", str(s), "--config", json.dumps(config), "--provision-pensee-jetons", provision,
                         "--url-base", "http://127.0.0.1:8792/v1beta"]}


FIXE = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
LISTE = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
CONFORME = {"maxOutputTokens": 32768, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}


def test_v8_garde_google_commande_conforme_acceptee(tmp_path):
    pieces = _pieces_garde(tmp_path)
    o = L.controler_chemins_google(L.Reglages.production(), {"fournisseurs": {"carbon": _carbon_factice(tmp_path, CONFORME)}},
                                   pieces, FIXE, LISTE)
    assert o["carbon"]["conforme"] is True, o
    assert o["carbon"]["roles"][0]["reglages_captures"]["thinkingConfig"]["thinkingLevel"] == "high"
    assert o["garde"]["version"] == "garde-google-v3"


@pytest.mark.parametrize("config,motif", [
    ({"maxOutputTokens": 32768}, "thinkingLevel absent"),                                               # sans réflexion
    ({"maxOutputTokens": 32768, "thinkingConfig": {"thinkingLevel": "low", "includeThoughts": True}}, "niveau envoyé"),
    ({"maxOutputTokens": 32768, "thinkingConfig": {"thinkingLevel": "high"}}, "includeThoughts"),
    ({"maxOutputTokens": 20000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "jetons de texte"),
    ({"maxOutputTokens": 65536, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "au-delà de la limite"),
    ({"maxOutputTokens": 26000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "limite de l'invite"),
])
def test_v8_garde_google_mutations_refusees(tmp_path, config, motif):
    pieces = _pieces_garde(tmp_path)
    o = L.controler_chemins_google(L.Reglages.production(), {"fournisseurs": {"carbon": _carbon_factice(tmp_path, config)}},
                                   pieces, FIXE, LISTE)
    probs = o["carbon"]["roles"][0]["problemes"]
    assert o["carbon"]["conforme"] is False and any(motif in p for p in probs), probs


def test_v8_garde_google_rien_capture_refuse(tmp_path):
    pieces = _pieces_garde(tmp_path)
    s = tmp_path / "muette.py"
    s.write_text("import sys\nprint('{\"texte\": \"\", \"cout_usd\": 1e-06}')\nsys.exit(4)\n", encoding="utf-8")
    o = L.controler_chemins_google(L.Reglages.production(), {"fournisseurs": {"carbon": {"commande": [sys.executable, "-I", "-B", str(s)]}}},
                                   pieces, FIXE, LISTE)
    assert o["carbon"]["conforme"] is False and "aucun corps" in o["carbon"]["roles"][0]["problemes"][0]


def test_v8_garde_google_vraies_commandes_refusees(tmp_path):
    """Les commandes réelles : Carbon par lot (copie de main, 9484dce0…) et Argon (enveloppe v5, commande v3d) posent
    `thinkingBudget` sans `thinkingLevel` ni `includeThoughts` : refusées par la garde ; rien n'est envoyé chez Google."""
    pieces = _pieces_garde(tmp_path)
    lot = _octets_de_main(L.CHEMINS_MAIN_COMMANDES["carbon"])
    if lot is None:
        pytest.skip("commande par lot absente de origin/main")
    c = tmp_path / "commande_gemini_lot_v1.py"
    c.write_bytes(lot)
    decl = {"fournisseurs": {"argon": {}, "carbon": {"commande": [sys.executable, "-I", "-B", str(c)] + L.ARGUMENTS_COMMANDES["carbon"]}}}
    o = L.controler_chemins_google(L.Reglages.production(), decl, pieces, FIXE, LISTE)
    for nom in ("argon", "carbon"):
        assert o[nom]["conforme"] is False
        for role in o[nom]["roles"]:
            assert any("thinkingBudget présent" in p for p in role["problemes"]) and any("includeThoughts" in p for p in role["problemes"])
    juge = [x for x in o["argon"]["roles"] if x["role"] == "juge_ideation"][0]
    assert any("jetons de texte" in p for p in juge["problemes"])         # 0,60 USD ne paie pas réflexion + 16 000


def test_v8_garde_google_reelle_refuse_le_depart_en_moteur_reel(monde, capsys):
    o = _octets_de_main("src/controle_ia/garde_google_v3.py")
    if o is None:
        pytest.skip("garde Google absente de origin/main")
    monde["r"].controler_google = None                                       # la garde réelle, sur l'Argon réel
    assert lancer(monde["r"]) == 2
    err = capsys.readouterr().err
    assert "garde des appels à Google" in err and "argon" in err
    runs = monde["r"].dossier_runs
    assert not (runs.is_dir() and [p for p in runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)])


def test_v8_garde_google_en_moteur_simule_ecrite_sans_refus(monde, capsys):
    monde["r"].controler_google = lambda r, decl, pieces, fixe, liste: {
        "argon": {"conforme": False, "roles": [{"problemes": ["réflexion : essai"]}]}}
    monde["r"].moteur, monde["r"].exiger_bac_a_sable, monde["r"].verifier_go = "simule", False, False
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["garde_google"]["refus_en_moteur_reel"] == ["argon"]
    assert "avertissement_garde_google" in capsys.readouterr().err


def test_v8_arguments_de_l_enveloppe_d_argon():
    a = L.arguments_enveloppe_argon(RACINE / L.PIECES["enveloppe_argon"][0])
    assert "$@" not in a and a[a.index("--url-base") + 1] == "http://127.0.0.1:8788/v1beta"


# --- 6. devis, version, essai à blanc -------------------------------------------------------------------------------------------


def test_v8_devis_interne():
    assert L.DEVIS_V8_MARGE_COMPRISE["avec_carbon"] == {"estimation": 41.33, "haut": 103.38}
    p = L.DEVIS_V5_PAR_APPEL
    cinq = 16 * (p["prop-opus"] + p["prop-fable"] + 3 * 0.276) + 160 * (p["aiguilleur"] + p["juge-opus"] + p["juge-argon"])
    quatre = 16 * (p["prop-opus"] + p["prop-fable"] + 2 * 0.276) + 128 * (p["aiguilleur"] + p["juge-opus"] + p["juge-argon"])
    assert L.DEVIS_V5_TOTAL == {"avec_carbon": pytest.approx(cinq), "sans_carbon": pytest.approx(quatre)}
    assert round(cinq * 1.1, 2) == 41.33 and round(quatre * 1.1, 2) == 32.86


def test_v8_preenregistrement_non_pose_refuse(monde, capsys):
    monde["r"].prereg = (monde["r"].prereg[0], L.PREREG_SHA256)
    assert L.PREREG_SHA256 == ""
    assert lancer(monde["r"]) == 2
    assert "non posée" in capsys.readouterr().err


def test_v8_gabarit_de_declaration_accepte_une_fois_rempli(monde, monkeypatch):
    o = json.loads((RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v8/declaration-relais-gabarit-course-affinage-v8.json").read_text())
    del o["gabarit"]
    s = _astra(monde, monkeypatch)
    ref = declaration(monde["depot"])["fournisseurs"]
    f = o["fournisseurs"]
    f["claude"].update(porte_plafond=ref["claude"]["porte_plafond"], url_relais=ref["claude"]["url_relais"], pid_relais=PID_CLAUDE)
    f["argon"].update(commande=ref["argon"]["commande"], nom_cle="CLE_ESSAI_A", pid_relais=PID_ARGON)
    f["astra"]["commande"][0], f["astra"]["commande"][3] = sys.executable, str(s)
    f["astra"]["pid_relais"] = PID_ASTRA
    assert f["claude"]["nom_cle"] == L.CLE_CLAUDE and f["astra"]["nom_cle"] == L.CLE_ASTRA and "carbon" not in f
    _decl(monde, o)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon", "prop-astra"] and dep["carbon"]["active"] is False
