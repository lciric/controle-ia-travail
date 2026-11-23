

# === v11d : régression R1 (essai à blanc), configuration v11d, gabarit du relevé des crédits v11d =============================


@pytest.fixture
def depot_a_blanc(tmp_path, monkeypatch):
    """Dépôt d'essai pour l'essai à blanc : pièces copiées du dépôt (garde Google de origin/main), préenregistrement d'essai
    scellé ; `DEPOT` du lanceur pointé dessus ; extraction de main faite depuis le dépôt réel."""
    garde = _octets_de_main(L.PIECES["garde_google"][0])
    if garde is None:
        pytest.skip("garde Google absente de origin/main")
    depot = tmp_path / "depot-a-blanc"
    for nom, (rel, _) in L.PIECES.items():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        (depot / rel).write_bytes(garde if nom == "garde_google" else octets_piece(rel))
    pre = depot / L.PREREG
    pre.parent.mkdir(parents=True, exist_ok=True)
    pre.write_text(PREREG_TEXTE, encoding="utf-8")
    sceller(pre)
    monkeypatch.setattr(L, "DEPOT", depot)
    origine = L.extraire_de_main
    monkeypatch.setattr(L, "extraire_de_main", lambda d, chemin, attendu, dest: origine(RACINE, chemin, attendu, dest))
    return depot


def _cles_de(decl: dict) -> dict:
    return {f: b["nom_cle"] for f, b in decl["fournisseurs"].items()}


def test_v11d_releve_de_l_essai_a_blanc_passe_verifier_credits(depot_a_blanc, tmp_path):
    r = L.reglages_a_blanc(tmp_path / "a-blanc")
    releve = json.loads(r.releve.read_text())
    assert releve["cles"][L.CLE_CLAUDE] == {"solde_non_lu": True, "reference": "GO-2026-11-22-124", "source": "essai à blanc"}
    jour = L._dt.date.fromisoformat(releve["releve_utc"][:10])
    o = L.verifier_credits(releve, _cles_de(json.loads(r.declaration.read_text())), jour, tmp_path / "alerte", {})
    assert o[L.CLE_CLAUDE]["ligne_du_releve"]["solde_non_lu"] is True and o[L.CLE_CLAUDE]["condition_de_depart"] is None


def test_v11d_artefact_ligne_de_luc_de_l_essai_a_blanc_v11c_refusee():
    v11c = {"solde_console_usd": 0.0, "source": "essai à blanc : aucune lecture réelle", "recharge_declaree_usd": 100.0,
            "recharge_source": "essai à blanc : valeur factice"}
    with pytest.raises(L.Refus, match="solde_non_lu"):
        L.verifier_ligne_luc(v11c)


def test_v11d_essai_a_blanc_de_bout_en_bout_moteur_simule_rend_0(depot_a_blanc, tmp_path, capsys):
    dossier = tmp_path / "a-blanc-complet"
    r = L.reglages_a_blanc(dossier)
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    r.orchestrateurs, r.commit_orchestrateur, r.empreintes_orchestrateur = (o,), commit, empreintes
    r.sorties_courses = ()
    assert L.principal(["--a-blanc", str(dossier)], reglages=r) == 0, capsys.readouterr().err
    run = [p for p in (dossier / "runs").iterdir() if p.name.endswith(L.SUFFIXE_RUN)]
    assert len(run) == 1 and L.scelle(run[0] / "manifeste-lanceur-fin.json")
    dep = json.loads((run[0] / "manifeste-lanceur-depart.json").read_text())
    assert dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]["ligne_du_releve"]["solde_non_lu"] is True


def test_v11d_mutation_essai_a_blanc_avec_la_ligne_v11c_refuse(depot_a_blanc, tmp_path):
    """Artefact (R5) : la ligne de LUC du v11c rétablie dans l'essai à blanc, le départ est refusé (code 2)."""
    m = _mutant("lanceur_v11d_mutant_a_blanc", [(
        '''**{CLE_CLAUDE: {"solde_non_lu": True, "reference": REFERENCE_LUC_SANS_SOLDE,  # v11d, R1\n''',
        '''**{CLE_CLAUDE: {"solde_console_usd": 0.0, "recharge_declaree_usd": 100.0,\n''')])
    monkeypatch_depot = L.DEPOT
    m.DEPOT, m.extraire_de_main = monkeypatch_depot, L.extraire_de_main
    dossier = tmp_path / "a-blanc-mutant"
    r = m.reglages_a_blanc(dossier)
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    r.orchestrateurs, r.commit_orchestrateur, r.empreintes_orchestrateur = (o,), commit, empreintes
    r.sorties_courses = ()
    assert m.principal(["--a-blanc", str(dossier)], reglages=r) == 2


# --- configuration v11d ----------------------------------------------------------------------------------------------------------


def test_v11d_configuration_notes_et_plafond_inerte_retire():
    c = FIXE["changements_v11"]
    assert "commande_gemini_flux_v2.py" in c["carbon"] and "commande_gemini_flux_v2.py" in c["argon"]
    assert "commande_gemini_flux_v1.py" not in c["carbon"] + c["argon"]
    assert "plafond_relais_claude_usd" not in FIXE["relais_persistants_v4"]
    assert 'plafond_relais_claude_usd"' not in CHEMIN_LANCEUR.read_text(encoding="utf-8")      # aucun code ne le lisait


# --- gabarit du relevé des crédits v11d -------------------------------------------------------------------------------------------


GABARIT_RELEVE = RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v11/releve-credits-gabarit-course-affinage-v11d.json"
GABARIT_DECL = RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v11/declaration-relais-gabarit-course-affinage-v11c.json"


def test_v11d_gabarit_du_releve_des_credits_rempli_passe_verifier_credits(tmp_path):
    g = json.loads(GABARIT_RELEVE.read_text())
    assert g["cles"][L.CLE_CLAUDE] == {"solde_non_lu": True, "reference": "GO-2026-11-22-124",
                                       "source": g["cles"][L.CLE_CLAUDE]["source"]}
    g["releve_utc"] = "2026-11-26T07:00:00Z"
    o = L.verifier_credits(g, _cles_de(json.loads(GABARIT_DECL.read_text())), dt.date(2026, 11, 26), tmp_path / "alerte", {})
    assert set(o) == {L.CLE_CLAUDE, "GEMINI_API_KEY", "OPENAI_API_KEY_2"} and o[L.CLE_CLAUDE]["condition_de_depart"] is None


def test_v11d_gabarit_non_rempli_refuse(tmp_path):
    g = json.loads(GABARIT_RELEVE.read_text())
    with pytest.raises(L.Refus):
        L.verifier_credits(g, _cles_de(json.loads(GABARIT_DECL.read_text())), dt.date(2026, 11, 26), tmp_path / "a", {})
