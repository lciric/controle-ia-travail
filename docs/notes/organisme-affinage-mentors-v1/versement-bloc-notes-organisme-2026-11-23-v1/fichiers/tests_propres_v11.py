

# =================================================================================================================================
# Essais propres à la v11 : clé LUC (couverture au fil de l'eau, plafond propre de 45 USD), exception de clé, Astra
# gpt-6.2-astra, Carbon en flux sous la garde Google, garde des appels à Google. Un cas sain et un artefact par garde (R5) ;
# mutations demandées par la mère (Minuit réintroduit, ancien Astra, Carbon sans réglage de réflexion, plafond retiré ou relevé).
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


def _remplacer_orchestrateur_attente(m):
    """Faux orchestrateur qui attend le signal TERM (jusqu'à 10 s) et dit s'il l'a reçu."""
    shutil.rmtree(m["orch"])
    o, commit, empreintes = faux_orchestrateur(m["tmp"])
    v8 = o / "demonstrations" / "ideation_v8.py"
    v8.write_text(v8.read_text().replace("arrete = False\n", (
        "arrete = False\nif True:\n    import signal, time\n    _e = {'stop': False}\n"
        "    signal.signal(signal.SIGTERM, lambda n, f: _e.__setitem__('stop', True))\n"
        "    if '--verifier-seulement' not in a:\n        for _ in range(200):\n            if _e['stop']:\n                break\n"
        "            time.sleep(0.05)\n        arrete = _e['stop']\n        os.makedirs(sortie, exist_ok=True)\n"
        "        json.dump({'signal_term_recu': arrete}, open(os.path.join(sortie, 'signal.json'), 'w'))\n"), 1))
    git(o, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-q", "-am", "attente")
    commit = subprocess.run(["git", "-C", str(o), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    empreintes = dict(empreintes, **{"demonstrations/ideation_v8.py": hashlib.sha256(v8.read_bytes()).hexdigest()})
    m["r"].orchestrateurs, m["r"].commit_orchestrateur, m["r"].empreintes_orchestrateur = (o,), commit, empreintes
    m["orch"] = o


# --- 1. part Claude sur LUC (GO-2026-11-22-124) : plafond propre de 45 USD ; arrêt propre au premier refus (code 5) -------------


def _journal_claude(m):
    c = m["cmdlines"][PID_CLAUDE]
    return Path(c[c.index("--journal") + 1])


def test_v11_part_claude_cas_sain_sous_45(monde):
    vu = _etat_claude_apres_depart(monde, depense_usd=39.5, engage_usd=0.4, refus=0)
    _journal_claude(monde).write_text(json.dumps({"statut": 200, "modele": "claude-opus-5-5"}) + "\n", encoding="utf-8")
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    c = json.loads((run / "manifeste-lanceur-fin.json").read_text())["cle_claude_au_fil_de_l_eau"]
    assert c["arret"] is None and c["plafond_part_claude_usd"] == 45.0 and c["journal"] == str(_journal_claude(monde))
    assert c["lectures"] >= 1 and c["derniere_part_engagee_usd"] == pytest.approx(39.9) and vu["lectures"] >= 1
    assert not (run / "alerte-arret-part-claude.json").exists()


def test_v11_premier_refus_du_relais_claude_arret_propre_code_5_sans_relance(monde, capsys):
    _etat_claude_apres_depart(monde, depense_usd=44.7, engage_usd=0.0, refus=1)     # le relais a refusé un appel (402)
    _remplacer_orchestrateur_attente(monde)
    assert lancer(monde["r"]) == 5
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-arret-part-claude.json")
    alerte = json.loads((run / "alerte-arret-part-claude.json").read_text())
    assert alerte["code"] == 5 and "402" in alerte["motif"] and "sans relance" in alerte["alerte"] and "aucune" in alerte["relance"]
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["code_du_lanceur"] == 5 and fin["cle_claude_au_fil_de_l_eau"]["arret"]["code"] == 5
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    sig = Path(dep["sortie"]) / "signal.json"
    assert fin["code"] == -15 or json.loads(sig.read_text())["signal_term_recu"] is True
    assert "arret_cle_claude" in capsys.readouterr().err
    assert lancer(monde["r"]) == 2                                             # aucune relance sous cette version


@pytest.mark.parametrize("statut", [400, 401, 402])
def test_v11_premier_4xx_de_l_interface_lu_au_journal_arret_code_5(monde, statut):
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.4, refus=0)       # loin du plafond : c'est l'interface qui refuse
    _journal_claude(monde).write_text(json.dumps({"statut": 200}) + "\n" + json.dumps({"statut": 429}) + "\n"
                                      + json.dumps({"statut": statut, "chemin": "/v1/messages"}) + "\n", encoding="utf-8")
    _remplacer_orchestrateur_attente(monde)
    assert lancer(monde["r"]) == 5
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-arret-part-claude.json")
    alerte = json.loads((run / "alerte-arret-part-claude.json").read_text())
    assert alerte["code"] == 5 and f"statut {statut}" in alerte["motif"] and "interface" in alerte["motif"]
    assert "crédit" not in alerte["motif"]                                          # le statut, pas la cause


def test_v11_200_et_429_n_arretent_pas(monde):
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _journal_claude(monde).write_text("".join(json.dumps({"statut": s}) + "\n" for s in (200, 429, 200, 429, 529, 500)), encoding="utf-8")
    assert lancer(monde["r"]) == 0


def test_v11_est_refus_interface():
    assert [s for s in (200, 299, 399, 400, 401, 402, 403, 404, 418, 429, 499, 500, 529) if L.est_refus_interface(s)] == \
        [400, 401, 402, 403, 404, 418, 499]
    assert not L.est_refus_interface(True) and not L.est_refus_interface("400") and not L.est_refus_interface(None)


def test_v11_mutation_garde_du_journal_retiree(monde):
    """La garde neuve retirée (le journal n'est plus lu) : un 400 de l'interface ne ferait plus arrêter la course."""
    m = _mutant("lanceur_v11_mutant_journal", [("            interface = self._refus_au_journal()\n",
                                                "            interface = None\n")])
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _journal_claude(monde).write_text(json.dumps({"statut": 400}) + "\n", encoding="utf-8")
    assert m.principal([], reglages=monde["r"]) == 0                                 # le mutant laisse partir : défaut visible
    monde["r"].dossier_runs = monde["tmp"] / "runs-ter"
    monde["r"].dossier_sorties = monde["tmp"] / "sorties-ter"
    assert lancer(monde["r"]) == 5                                                   # le lanceur, lui, arrête


def test_v11_part_engagee_au_plafond_arret_propre_code_5(monde):
    _etat_claude_apres_depart(monde, depense_usd=44.6, engage_usd=0.4, refus=0)    # 45,0 : dépense + réservé des appels en vol
    _remplacer_orchestrateur_attente(monde)
    assert lancer(monde["r"]) == 5
    alerte = json.loads((un_run(monde["r"]) / "alerte-arret-part-claude.json").read_text())
    assert "≥ plafond de la part Claude 45.0" in alerte["motif"]


def test_v11_relais_claude_a_un_autre_plafond_que_45_refuse(monde, capsys):
    monde["cmdlines"][PID_CLAUDE][monde["cmdlines"][PID_CLAUDE].index("--plafond-usd") + 1] = "150"   # l'ancienne règle
    monde["etat_claude"]["plafond_usd"] = 150.0
    assert lancer(monde["r"]) == 2
    assert "plafond de la part Claude" in capsys.readouterr().err


def test_v11_relais_claude_sans_journal_refuse(monde, capsys):
    c = monde["cmdlines"][PID_CLAUDE]
    k = c.index("--journal")
    del c[k:k + 2]
    assert lancer(monde["r"]) == 2
    assert "--journal" in capsys.readouterr().err


@pytest.mark.parametrize("cas", ["etat", "journal"])
def test_v11_etat_ou_journal_illisible_trois_fois_arret_propre_code_5(monde, cas):
    if cas == "etat":
        _etat_claude_apres_depart(monde)
    else:
        _etat_claude_apres_depart(monde, depense_usd=1.0, engage_usd=0.0, refus=0)
        _journal_claude(monde).write_text("{pas du json\n", encoding="utf-8")
    _remplacer_orchestrateur_attente(monde)
    assert lancer(monde["r"]) == 5
    alerte = json.loads((un_run(monde["r"]) / "alerte-arret-part-claude.json").read_text())
    assert "illisible 3 fois" in alerte["motif"]


def test_v11_une_lecture_manquee_n_arrete_pas():
    class R:
        lire_etat_relais = None
    n = {"k": 0}

    def lire(url):
        n["k"] += 1
        if n["k"] == 1:
            raise OSError("manquée")
        return {"depense_usd": 1.0, "engage_usd": 0.0, "refus": 0}
    r = R()
    r.lire_etat_relais = lire
    s = L.SurveillanceCleClaude(r, "http://127.0.0.1:1", 45.0)
    assert s.depasse() is None and s.illisibles == 1
    assert s.depasse() is None and s.illisibles == 0 and s.derniere == 1.0


@pytest.mark.parametrize("modif", ["retire", "releve", "abaisse", "part_de_la_couverture"])
def test_v11_mutation_plafond_de_la_part_retire_ou_change_refuse(monde, modif):
    p = monde["depot"] / L.PIECES["configuration"][0]
    o = json.loads(p.read_text())
    c = o["changements_v11"]
    if modif == "retire":
        del c["plafond_part_claude_usd"]
    elif modif == "releve":
        c["plafond_part_claude_usd"] = 60.0
    elif modif == "abaisse":
        c["plafond_part_claude_usd"] = 30.0
    else:
        c["part_de_la_couverture"] = 0.8                      # la règle retirée par GO-2026-11-22-124 réintroduite
    p.write_text(json.dumps(o, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    monde["r"].pieces = dict(monde["r"].pieces, configuration=(L.PIECES["configuration"][0], hashlib.sha256(p.read_bytes()).hexdigest()))
    assert lancer(monde["r"]) == 2


def test_v11_mutation_constante_du_plafond_relevee_refusee(monde, monkeypatch, capsys):
    monkeypatch.setattr(L, "PLAFOND_PART_CLAUDE_USD", 60.0)
    assert lancer(monde["r"]) == 2
    assert "45 USD exigés" in capsys.readouterr().err


def test_v11_releve_sans_ligne_de_luc_part(monde):
    objet = releve()
    del objet["cles"][L.CLE_CLAUDE]
    _releve(monde, objet)
    assert lancer(monde["r"]) == 0                                # GO-2026-11-22-124 : le solde n'est pas une condition


def test_v11_codes_de_sortie():
    assert L.code_de_sortie(False, False, None, 0, 5) == 5 and L.code_de_sortie(False, True, None, 2, 5) == 5
    assert L.code_de_sortie(True, False, None, 0, 5) == 4 and L.code_de_sortie(False, False, None, 0) == 0


# --- 2. clé Claude : Minuit réintroduite ---------------------------------------------------------------------------------------


def test_v11_mutation_minuit_dans_la_declaration_refusee(monde, capsys):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_MINUIT"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    assert "MINUIT" in capsys.readouterr().err


def test_v11_mutation_minuit_dans_la_configuration_refusee():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    L.garde_cles_configuration(fixe)
    for modif in (lambda f: f["cles"].__setitem__("claude", "RR_ANTHROPIC_API_KEY_MINUIT"),
                  lambda f: f["especes"][0].__setitem__("cle", "RR_ANTHROPIC_API_KEY_MINUIT"),
                  lambda f: f["cles_interdites"].remove("RR_ANTHROPIC_API_KEY_MINUIT")):
        f = json.loads(json.dumps(fixe))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_cles_configuration(f)


def test_v11_mutation_minuit_dans_l_environnement_refusee(monde):
    monde["r"].environnement = {"PATH": "/usr/bin:/bin", "RR_ANTHROPIC_API_KEY_MINUIT": "valeur-secrete-essai-3"}
    assert lancer(monde["r"]) == 2


def test_v11_configuration_ne_differe_de_la_v9_que_par_les_cles_et_les_notes():
    p = subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/prep/affinage-v10-compte-organisme-v1:"
                        "docs/notes/organisme-affinage-mentors-v1/course-v9/configuration-course-affinage-mentors-v9.json"],
                       capture_output=True)
    if p.returncode != 0:
        pytest.skip("branche prep/affinage-v10 non récupérée")
    v9, v11 = json.loads(p.stdout), json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    for k in set(v9) | set(v11):
        if k not in ("version", "statut", "cles", "cles_interdites", "credit_declare_usd", "especes", "changements_v11", "argon_v11"):
            assert v9.get(k) == v11.get(k), k
    assert [dict(e, cle=None) for e in v9["especes"]] == [dict(e, cle=None) for e in v11["especes"]]
    assert v11["plafonds_session"]["proposeur"] == 3.0 and v11["changements_v11"]["plafond_part_claude_usd"] == 45.0


# --- 3. exception de clé (GO-2026-11-22-107) ------------------------------------------------------------------------------------


@pytest.mark.parametrize("remplace,par", [
    (LIGNE_GO_CLE, ""),                                                                                     # 107 absente
    (LIGNE_GO_CLE, LIGNE_GO_CLE.replace("RR_ANTHROPIC_API_KEY_LUC", "RR_ANTHROPIC_API_KEY_MINUIT")),       # autre clé
    (LIGNE_GO_CLE, LIGNE_GO_CLE.replace("GO-2026-11-22-70", "GO-2026-11-22-71")),                           # autre règle
    (LIGNE_GO_CLE, LIGNE_GO_CLE.replace("| Lazar |", "| la mère |")),                                       # pas Lazar
    (LIGNE_GO_SIMPL, ""),                                                                                   # 124 absente
    (LIGNE_GO_SIMPL, LIGNE_GO_SIMPL.replace("2026-12-15", "2026-11-17")),                                    # 124 échue
    (LIGNE_GO_SIMPL, LIGNE_GO_SIMPL.replace("GO-2026-11-22-107", "GO-2026-11-22-999")),                      # 124 sans 107
    (LIGNE_GO_SIMPL, LIGNE_GO_SIMPL + "| GO-2026-11-22-130 | 2026-11-22 | révocation | révoque GO-2026-11-22-124 | — | — | Lazar | — |\n"),
])
def test_v11_exceptions_de_cle_artefacts_refuses(monde, remplace, par):
    monde["r"].registre_go.write_text(ligne_go().replace(remplace, par), encoding="utf-8")
    assert lancer(monde["r"]) == 2


ENTETE_GO = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\n|---|---|---|---|---|---|---|---|\n"
L14 = ("| GO-2026-11-18-14 | 2026-11-18 | calcul | course d'affinage des idées des mentors | 150 USD | 2026-11-25 | Lazar | R-3215 |\n")
L80 = ("| GO-2026-11-22-80 | 2026-11-22 | calcul | Prolongation de GO-2026-11-18-14 (affinage des 93 idées des mentors) | 150 USD "
       "(plafond de GO-2026-11-18-14) | 2026-12-15 | Lazar | GO-2026-11-22-77 |\n")
L107 = LIGNE_GO_CLE.replace("| 2026-11-18 | calcul", "| 2026-11-22 | calcul")
L124 = LIGNE_GO_SIMPL.replace("| 2026-11-18 | calcul", "| 2026-11-22 | calcul")
L131 = ("| GO-2026-11-22-131 | 2026-11-22 | décision | Lazar confirme la prolongation de GO-2026-11-22-107 au 15 décembre | — | "
        "2026-12-15 | Lazar | GO-2026-11-22-124 |\n")


def _registre_go_essai(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text(ENTETE_GO + "".join(lignes), encoding="utf-8")
    return p


def _fixe_confirmation(valeur):
    f = json.loads(json.dumps(FIXE))
    f["changements_v11"]["confirmation_prolongation_go_107"] = valeur
    return f


def test_v11_go_avant_le_25_sans_prolongation_sain(tmp_path):
    o = L.verifier_les_go(_registre_go_essai(tmp_path, L14, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation(None))
    assert o["go"]["id"] == "GO-2026-11-18-14" and o["prolongation_course"]["valide"] is False and o["confirmation_107"]["valide"] is False


def test_v11_go_apres_le_25_avec_80_et_confirmation_nommee_et_inscrite_sain(tmp_path):
    o = L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))
    assert o["prolongation_course"]["valide"] is True and o["confirmation_107"]["nommee"] == "GO-2026-11-22-131"
    assert o["exception_cle"]["id"] == "GO-2026-11-22-107"


def test_v11_go_apres_le_25_sans_80_refuse(tmp_path):
    with pytest.raises(L.Refus, match="GO-2026-11-18-14 hors de sa période"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_apres_le_25_80_revoquee_refuse(tmp_path):
    rev = "| GO-2026-11-22-140 | 2026-11-22 | révocation | révoque GO-2026-11-22-80 | — | — | Lazar | — |\n"
    with pytest.raises(L.Refus, match="GO-2026-11-18-14 hors de sa période"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, rev, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_apres_le_25_confirmation_non_nommee_refuse(tmp_path):
    with pytest.raises(L.Refus, match="GO-2026-11-22-107 hors de sa période"):           # inscrite mais pas nommée
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation(None))


def test_v11_go_confirmation_nommee_mais_non_inscrite_refuse(tmp_path):
    with pytest.raises(L.Refus, match="confirmation de la prolongation"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_confirmation_par_une_autre_que_lazar_refuse(tmp_path):
    with pytest.raises(L.Refus, match="confirmation de la prolongation"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131.replace("| Lazar | GO-2026-11-22-124", "| la mère | GO-2026-11-22-124")),
                          dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_emplacement_de_confirmation_absent_refuse(tmp_path):
    f = json.loads(json.dumps(FIXE))
    del f["changements_v11"]["confirmation_prolongation_go_107"]
    with pytest.raises(L.Refus, match="emplacement"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124), dt.date(2026, 11, 24), f)


def test_v11_go_apres_le_15_decembre_refuse(tmp_path):
    with pytest.raises(L.Refus):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 12, 16), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_lus_au_manifeste(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["go"]["id"] == "GO-2026-11-18-14" and dep["go"]["prolongation"]["id"] == "GO-2026-11-22-80"
    assert dep["go_exception_cle"]["confirmation"]["nommee"] is None and dep["go_simplification_cle"]["echeance"] == "2026-12-15"


def test_v11_exception_de_cle_sur_la_vraie_ligne_de_main(tmp_path):
    p = subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/main:registres/go.md"], capture_output=True)
    if p.returncode != 0 or b"GO-2026-11-22-107" not in p.stdout:
        pytest.skip("registre de main sans la ligne GO-2026-11-22-107")
    reg = tmp_path / "go.md"
    reg.write_bytes(p.stdout)
    o = L.verifier_go_exception_cle(reg, dt.date(2026, 11, 22))
    assert o["id"] == "GO-2026-11-22-107" and o["par"] == "Lazar"
    with pytest.raises(L.Refus, match="période"):
        L.verifier_go_exception_cle(reg, dt.date(2026, 11, 26))
    if b"GO-2026-11-22-124" in p.stdout:
        s = L.verifier_go_simplification(reg, dt.date(2026, 11, 26))
        assert s["echeance"] == "2026-12-15"
        assert L.verifier_go_exception_cle(reg, dt.date(2026, 11, 26), prolongation=s["echeance"])["id"] == "GO-2026-11-22-107"
        with pytest.raises(L.Refus):                                             # sans confirmation nommée : refus après le 25
            L.verifier_les_go(reg, dt.date(2026, 11, 26), _fixe_confirmation(None))


# --- 4. Astra : gpt-6.2-astra, OPENAI_API_KEY_2, sonde v3, palier ---------------------------------------------------------------


def test_v11_astra_arguments_et_modele():
    a = L.ARGUMENTS_COMMANDES["astra"]
    assert a[a.index("--modele") + 1] == "gpt-6.2-astra" and L.MODELES_RELAIS["astra"] == ["gpt-6.2-astra"]
    assert (a[a.index("--prix-entree") + 1], a[a.index("--prix-sortie") + 1]) == ("8", "40") and L.PRIX_ASTRA == (8.0, 40.0)
    assert L.CLE_ASTRA == "OPENAI_API_KEY_2"


def test_v11_astra_cas_sain_au_manifeste(monde, monkeypatch):
    _astra(monde, monkeypatch)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["palier_astra"]["borne_entree_jetons"] < 272000 and dep["cles_employees"]["astra"] == "OPENAI_API_KEY_2"


@pytest.mark.parametrize("modifs,motif", [({"modele_propose": "gpt-6-astra"}, "gpt-6.2-astra"),
                                          ({"nom_cle": "OPENAI_API_KEY"}, "OPENAI_API_KEY_2")])
def test_v11_astra_mutations_refusees(monde, monkeypatch, capsys, modifs, motif):
    _astra(monde, monkeypatch)
    d = json.loads(monde["r"].declaration.read_text())
    d["fournisseurs"]["astra"].update(modifs)
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    assert motif in capsys.readouterr().err


@pytest.mark.parametrize("modifs,motif", [({"version": "sonde_astra_affinage_v2"}, "sonde épinglée"),
                                          ({"modele_servi": "gpt-6-astra"}, "modèle servi")])
def test_v11_sonde_d_astra_ancienne_refusee(monde, monkeypatch, capsys, modifs, motif):
    _astra(monde, monkeypatch)
    _sonde(monde, **modifs)
    assert lancer(monde["r"]) == 2
    assert motif in capsys.readouterr().err


def test_v11_sonde_commune_v1_refusee(monde, monkeypatch, capsys):
    _astra(monde, monkeypatch)
    c = json.loads((monde["depot"] / COMMUNE_DU_JOUR).read_text())
    c["version"] = "sonde_astra_courses_v1"
    ecrire_sondes(monde["depot"], v2=json.loads((monde["depot"] / L.SONDE_ASTRA).read_text()), commune=c)
    assert lancer(monde["r"]) == 2
    assert "version" in capsys.readouterr().err


def test_v11_palier_d_astra_sain_et_artefact():
    pieces = {"consigne_proposeur": {"absolu": str(RACINE / L.PIECES["consigne_proposeur"][0])}}
    liste = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
    assert L.verifier_palier_astra(pieces, liste)["borne_entree_jetons"] < 20000
    grosse = json.loads(json.dumps(liste))
    grosse["fils"][0]["idees_servies"][0]["texte_servi"] = "x" * 300000
    with pytest.raises(L.Refus, match="palier"):
        L.verifier_palier_astra(pieces, grosse)


# --- 5. Carbon en flux : budget sous le plafond de session (point 3 de la mère) -------------------------------------------------


def _decl_carbon_reelle(args=None):
    c = RACINE / L.PIECES["commande_carbon"][0]
    return {"fournisseurs": {"carbon": {"commande": [sys.executable, "-I", "-B", str(c)] + list(args or L.ARGUMENTS_COMMANDES["carbon"])}}}


def _pieces_rel():
    return {k: {"chemin": v[0], "absolu": str(RACINE / v[0]), "sha256": v[1]} for k, v in L.PIECES.items()}


def test_v11_carbon_pire_cas_sous_le_plafond_de_session():
    o = L.controler_pire_cas_carbon(_decl_carbon_reelle(), FIXE, LISTE_V11, _pieces_rel())
    cas = o["cas"]["entree_la_plus_longue"]
    assert cas["entree_gardee_jetons"] == 2618 and cas["sortie_demandee_jetons"] == 65536
    assert cas["pire_cas_appel_usd"] == pytest.approx((2618 * 4 + 65536 * 20) / 1e6) == pytest.approx(1.321192, abs=1e-6)  # R-5018
    assert cas["pire_cas_appel_usd"] <= o["plafond_session_usd"] == 3.0
    assert o["texte_jetons"] == 36864 >= 16000 and o["texte_jetons"] > o["limite_invite_caracteres"] == 18000


@pytest.mark.parametrize("option,valeur,motif", [("--max-sortie-jetons", "40000", "texte"),       # 40 000 − 28 672 < 16 000
                                                 ("--max-sortie-jetons", "46000", "limite de l'invite"),  # 17 328 ≤ 18 000
                                                 ("--max-sortie-jetons", "200000", "plafond de session"),  # 200 000 × 20 > 3,00
                                                 ("--provision-pensee-jetons", "20000", "provision")])
def test_v11_carbon_budget_artefacts(option, valeur, motif):
    args = list(L.ARGUMENTS_COMMANDES["carbon"])
    args[args.index(option) + 1] = valeur
    with pytest.raises(L.Refus, match=motif):
        L.controler_pire_cas_carbon(_decl_carbon_reelle(args), FIXE, LISTE_V11, _pieces_rel())


def test_v11_carbon_sous_un_plafond_de_1_00_refuse():
    fixe = json.loads(json.dumps(FIXE))
    fixe["plafonds_session"]["proposeur"] = 1.0                       # 1,32 > 1,00 : Carbon en flux ne tiendrait pas
    with pytest.raises(L.Refus, match="plafond de session"):
        L.controler_pire_cas_carbon(_decl_carbon_reelle(), fixe, LISTE_V11, _pieces_rel())


@pytest.mark.parametrize("niveau", ["medium", "low"])
def test_v11_carbon_mutation_reflexion_abaissee_refusee_a_la_declaration(monde, monkeypatch, capsys, niveau):
    sc = script_commande(monde["tmp"], "commande_gemini_flux_v1", {"texte": "", "cout_usd": 0.01})
    args = list(L.ARGUMENTS_COMMANDES["carbon"])
    args[args.index("--niveau-reflexion") + 1] = niveau
    _carbon(monde, monkeypatch, commande=[sys.executable, "-I", "-B", str(sc)] + args)
    assert lancer(monde["r"]) == 2
    assert "niveau-reflexion" in capsys.readouterr().err


def test_v11_carbon_commande_par_lot_refusee_a_la_declaration(monde, monkeypatch):
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    _carbon(monde, monkeypatch)
    d = json.loads(monde["r"].declaration.read_text())
    d["fournisseurs"]["carbon"]["commande"][3] = str(sc)                  # l'ancienne commande : plus épinglée
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


# --- 6. garde des appels à Google (règle gelée, GO-2026-11-21-71) ---------------------------------------------------------------


LISTE_V11 = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
COMMANDE_GOOGLE_FACTICE = r'''
import json, sys, urllib.request
a = sys.argv[1:]
url = a[a.index("--url-base") + 1]
config = json.loads(a[a.index("--config") + 1])
corps = {"contents": [{"role": "user", "parts": [{"text": sys.stdin.read()}]}], "generationConfig": config}
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
    pieces = _pieces_rel()
    pieces["garde_google"]["absolu"] = str(g)
    return pieces


def _carbon_factice(tmp_path, config, provision="28672"):
    s = tmp_path / "commande_google_factice.py"
    s.write_text(COMMANDE_GOOGLE_FACTICE, encoding="utf-8")
    return {"commande": [sys.executable, "-I", "-B", str(s), "--config", json.dumps(config), "--provision-pensee-jetons", provision,
                         "--url-base", "http://127.0.0.1:8791/v1beta"]}


def test_v11_garde_google_vraie_commande_en_flux_conforme(tmp_path):
    pieces = _pieces_garde(tmp_path)
    o = L.controler_chemins_google(L.Reglages.production(), _decl_carbon_reelle(), pieces, FIXE, LISTE_V11)
    assert o["carbon"]["conforme"] is True, o
    rg = o["carbon"]["roles"][0]["reglages_captures"]
    assert rg["mode"] == "flux" and rg["maxOutputTokens"] == 65536 and rg["provision"] == 28672
    assert rg["thinkingConfig"] == {"thinkingLevel": "high", "includeThoughts": True}


@pytest.mark.parametrize("config,motif", [
    ({"maxOutputTokens": 65536}, "thinkingLevel absent"),                                               # sans réflexion
    ({"maxOutputTokens": 65536, "thinkingConfig": {"thinkingBudget": 28672, "includeThoughts": True}}, "thinkingBudget présent"),
    ({"maxOutputTokens": 65536, "thinkingConfig": {"thinkingLevel": "low", "includeThoughts": True}}, "niveau envoyé"),
    ({"maxOutputTokens": 65536, "thinkingConfig": {"thinkingLevel": "high"}}, "includeThoughts"),
    ({"maxOutputTokens": 40000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "jetons de texte"),
    ({"maxOutputTokens": 70000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "au-delà de la limite"),
    ({"maxOutputTokens": 46000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "limite de l'invite"),
])
def test_v11_garde_google_mutations_refusees(tmp_path, config, motif):
    pieces = _pieces_garde(tmp_path)
    o = L.controler_chemins_google(L.Reglages.production(), {"fournisseurs": {"carbon": _carbon_factice(tmp_path, config)}},
                                   pieces, FIXE, LISTE_V11)
    probs = o["carbon"]["roles"][0]["problemes"]
    assert o["carbon"]["conforme"] is False and any(motif in p for p in probs), probs


def test_v11_garde_google_rien_capture_refuse(tmp_path):
    pieces = _pieces_garde(tmp_path)
    s = tmp_path / "muette.py"
    s.write_text("import sys\nprint('{\"texte\": \"\", \"cout_usd\": 1e-06}')\nsys.exit(4)\n", encoding="utf-8")
    o = L.controler_chemins_google(L.Reglages.production(), {"fournisseurs": {"carbon": {"commande": [sys.executable, "-I", "-B", str(s)]}}},
                                   pieces, FIXE, LISTE_V11)
    assert o["carbon"]["conforme"] is False and "aucun corps" in o["carbon"]["roles"][0]["problemes"][0]


def test_v11_garde_google_argon_reel_et_ancien_lot_refuses(tmp_path):
    """L'Argon réel (enveloppe v5, `commande_argon_v3d.py`) et l'ancienne commande par lot de Carbon (`main`, 9484dce0…) posent
    `thinkingBudget` sans `thinkingLevel` ni `includeThoughts` : refusés ; rien n'est envoyé chez Google."""
    pieces = _pieces_garde(tmp_path)
    lot = _octets_de_main("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py")
    if lot is None:
        pytest.skip("commande par lot absente de origin/main")
    c = tmp_path / "commande_gemini_lot_v1.py"
    c.write_bytes(lot)
    args_lot = ["--modele", "gemini-4-carbon", "--url-base", "http://127.0.0.1:8792/v1beta", "--prix-entree", "8.3", "--prix-sortie",
                "41.5", "--facteur-lot", "0.5", "--max-sortie-jetons", "32768", "--sortie-min-jetons", "4096",
                "--provision-pensee-jetons", "28672", "--roles", "proposeur_ideation"]
    decl = {"fournisseurs": {"argon": {}, "carbon": {"commande": [sys.executable, "-I", "-B", str(c)] + args_lot}}}
    o = L.controler_chemins_google(L.Reglages.production(), decl, pieces, FIXE, LISTE_V11)
    for nom in ("argon", "carbon"):
        assert o[nom]["conforme"] is False
        for role in o[nom]["roles"]:
            assert any("thinkingBudget présent" in p for p in role["problemes"]) and any("includeThoughts" in p for p in role["problemes"])


def test_v11_garde_google_reelle_depart_sain_argon_en_flux(monde):
    """La garde réelle (pièce de main) sur l'Argon déclaré en flux : conforme, départ en moteur réel (relais simulés)."""
    if _octets_de_main("src/controle_ia/garde_google_v3.py") is None:
        pytest.skip("garde Google absente de origin/main")
    monde["r"].controler_google = None
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["garde_google"]["argon"]["conforme"] is True and len(dep["garde_google"]["argon"]["roles"]) == 2


def test_v11_garde_google_reelle_refuse_un_chemin_non_conforme(monde, monkeypatch, capsys):
    if _octets_de_main("src/controle_ia/garde_google_v3.py") is None:
        pytest.skip("garde Google absente de origin/main")
    monde["r"].controler_google = None
    s = monde["tmp"] / "commande_gemini_flux_v1.py"                       # même nom, autre code : sans réglage de réflexion
    s.write_text(COMMANDE_GOOGLE_FACTICE.replace("gemini-4-carbon", "gemini-4-argon").replace(
        'config = json.loads(a[a.index("--config") + 1])', 'config = {"maxOutputTokens": 45056}'), encoding="utf-8")
    monkeypatch.setitem(L.COMMANDES_EPINGLEES, "argon", {s.name: hashlib.sha256(s.read_bytes()).hexdigest()})
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["commande"][3] = str(s)
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    err = capsys.readouterr().err
    assert "garde des appels à Google" in err and "thinkingLevel absent" in err
    runs = monde["r"].dossier_runs
    assert not (runs.is_dir() and [p for p in runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)])


def test_v11_garde_google_en_moteur_simule_ecrite_sans_refus(monde, capsys):
    monde["r"].controler_google = lambda r, decl, pieces, fixe, liste: {
        "argon": {"conforme": False, "roles": [{"problemes": ["réflexion : essai"]}]}}
    monde["r"].moteur, monde["r"].exiger_bac_a_sable, monde["r"].verifier_go = "simule", False, False
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["garde_google"]["refus_en_moteur_reel"] == ["argon"]
    assert "avertissement_garde_google" in capsys.readouterr().err


def test_v11_arguments_de_l_enveloppe_d_argon():
    a = L.arguments_enveloppe_argon(RACINE / L.PIECES["enveloppe_argon"][0])
    assert "$@" not in a and a[a.index("--url-base") + 1] == "http://127.0.0.1:8788/v1beta"


# --- 7. version, préenregistrement, gabarit -------------------------------------------------------------------------------------


def test_v11_version_et_chemins():
    assert L.VERSION == "lancer_course_affinage_mentors_v11" and "course-v11" in L.PREREG and "course-v11" in L.DECLARATION_RELAIS
    assert L.PROGRAMMES_RELAIS["carbon"][0] == "relais_gemini_v3.py" and L.PIECES["commande_carbon"][0].endswith("commande_gemini_flux_v1.py")


def test_v11_preenregistrement_non_pose_refuse(monde, capsys):
    monde["r"].prereg = (monde["r"].prereg[0], L.PREREG_SHA256)
    assert L.PREREG_SHA256 == ""
    assert lancer(monde["r"]) == 2
    assert "non posée" in capsys.readouterr().err


def test_v11_gabarit_de_declaration_accepte_une_fois_rempli(monde, monkeypatch):
    o = json.loads((RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v11/declaration-relais-gabarit-course-affinage-v11.json").read_text())
    del o["gabarit"]
    s = _astra(monde, monkeypatch)
    sc = script_commande(monde["tmp"], "commande_gemini_flux_v1", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "carbon", sc)
    ref = declaration(monde["depot"])["fournisseurs"]
    f = o["fournisseurs"]
    f["claude"].update(porte_plafond=ref["claude"]["porte_plafond"], url_relais=ref["claude"]["url_relais"], pid_relais=PID_CLAUDE)
    f["argon"].update(commande=ref["argon"]["commande"], nom_cle="CLE_ESSAI_A", pid_relais=PID_ARGON)
    f["astra"]["commande"][0], f["astra"]["commande"][3] = sys.executable, str(s)
    f["astra"]["pid_relais"] = PID_ASTRA
    f["carbon"]["commande"][0], f["carbon"]["commande"][3] = sys.executable, str(sc)
    f["carbon"].update(nom_cle="CLE_ESSAI_G", pid_relais=PID_CARBON)
    assert f["claude"]["nom_cle"] == L.CLE_CLAUDE and f["astra"]["nom_cle"] == L.CLE_ASTRA
    assert f["carbon"]["commande"][4:] == L.ARGUMENTS_COMMANDES["carbon"] and f["astra"]["commande"][4:] == L.ARGUMENTS_COMMANDES["astra"]
    _decl(monde, o)
    objet = releve(CLE_ESSAI_A={"non_lisible": True}, CLE_ESSAI_G={"non_lisible": True},
                   OPENAI_API_KEY_2={"credit_usd": 100.0, "reste_usd": 90.0, "source": "essai"})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_A", "CLE_ESSAI_G"]}
    _releve(monde, objet)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]


# --- 8. Argon sous la garde Google (décision de la mère) : emplacement du plafond des juges, commande en flux ------------------


def _decl_argon_reelle():
    c = RACINE / L.PIECES["commande_carbon"][0]
    return {"fournisseurs": {"argon": {"commande": [sys.executable, "-I", "-B", str(c)] + L.ARGUMENTS_COMMANDES["argon"]}}}


def _fixe_juge(valeur):
    f = json.loads(json.dumps(FIXE))
    f["argon_v11"]["plafond_session_juge_usd"] = valeur
    return f


def test_v11_argon_emplacement_de_production_1_00():
    assert FIXE["argon_v11"]["plafond_session_juge_usd"] == 1.00 and FIXE["plafonds_session"]["juge"] == 0.6
    f = json.loads(json.dumps(FIXE))
    assert L.appliquer_emplacement_argon(f)["plafond_session_juge_usd"] == 1.00 and f["plafonds_session"]["juge"] == 1.00
    o = L.controler_pire_cas_argon(_decl_argon_reelle(), f, LISTE_V11, _pieces_rel())
    assert o["roles"]["juge"]["pire_cas_appel_usd"] <= 1.00
    with pytest.raises(L.Refus, match="plafond minimal 0.92"):                  # vide : 0,60 ne paie pas un juge d'Argon au pire
        f0 = _fixe_juge(None)
        L.appliquer_emplacement_argon(f0)
        L.controler_pire_cas_argon(_decl_argon_reelle(), f0, LISTE_V11, _pieces_rel())


@pytest.mark.parametrize("valeur,issue", [(1.0, "sain"), (0.92, "sain"), (0.91, "refus"), (0.6, "refus")])
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
            L.controler_pire_cas_argon(_decl_argon_reelle(), f, LISTE_V11, _pieces_rel())


@pytest.mark.parametrize("valeur", ["2", 0, -1.0, 3.5, True])
def test_v11_argon_emplacement_mal_forme_refuse(valeur):
    with pytest.raises(L.Refus):
        L.appliquer_emplacement_argon(_fixe_juge(valeur))
    f = json.loads(json.dumps(FIXE))
    del f["argon_v11"]
    with pytest.raises(L.Refus, match="emplacement"):
        L.appliquer_emplacement_argon(f)


def test_v11_argon_juge_servi_au_plafond_de_l_emplacement(monde):
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    conf = json.loads((run / "configuration-orchestrateur.json").read_text())
    assert conf["plafonds_session"]["juge"] == 2.0 and "argon_v11" not in conf
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    assert dep["argon_v11"]["emplacement"] == 2.0 and dep["reglages_argon_v11_flux"]["roles"]["juge"]["plafond_minimal_usd"] == 0.92


def test_v11_argon_enveloppe_v5_refusee_a_la_declaration(monde, capsys):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["commande"] = ["bash", str(monde["depot"] / L.PIECES["enveloppe_argon"][0])]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    assert "enveloppe v5" in capsys.readouterr().err


def test_v11_garde_google_argon_en_flux_sain(tmp_path):
    pieces = _pieces_garde(tmp_path)
    f = _fixe_juge(1.0)
    L.appliquer_emplacement_argon(f)                                         # plafond des juges servi : 1,00 (devis v11)
    o = L.controler_chemins_google(L.Reglages.production(), _decl_argon_reelle(), pieces, f, LISTE_V11)
    assert o["argon"]["conforme"] is True, o
    for role in o["argon"]["roles"]:
        assert role["reglages_captures"]["mode"] == "flux" and role["reglages_captures"]["maxOutputTokens"] == 45056
        assert role["reglages_captures"]["thinkingConfig"] == {"thinkingLevel": "high", "includeThoughts": True}


@pytest.mark.parametrize("config,motif", [
    ({"maxOutputTokens": 45056}, "thinkingLevel absent"),                                                  # réflexion absente
    ({"maxOutputTokens": 30000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "jetons de texte"),  # trop bas
])
def test_v11_garde_google_argon_artefacts(tmp_path, config, motif):
    pieces = _pieces_garde(tmp_path)
    s = tmp_path / "commande_google_factice.py"
    s.write_text(COMMANDE_GOOGLE_FACTICE.replace("gemini-4-carbon", "gemini-4-argon"), encoding="utf-8")
    decl = {"fournisseurs": {"argon": {"commande": [sys.executable, "-I", "-B", str(s), "--config", json.dumps(config),
                                                    "--provision-pensee-jetons", "24576", "--niveau-reflexion", "high",
                                                    "--url-base", "http://127.0.0.1:8788/v1beta"]}}}
    f = _fixe_juge(1.0)
    L.appliquer_emplacement_argon(f)
    o = L.controler_chemins_google(L.Reglages.production(), decl, pieces, f, LISTE_V11)
    assert o["argon"]["conforme"] is False
    for role in o["argon"]["roles"]:
        assert any(motif in p for p in role["problemes"]), role["problemes"]


# --- brouillon 2 du préenregistrement v11, point (a) : identifiants de GO à trois chiffres de rang ---------------------------------
REV_3 = "| GO-2026-11-22-150 | 2026-11-22 | révocation | révoque GO-2026-11-18-14 | — | — | Lazar | — |\n"
L_3 = ("| GO-2026-11-22-151 | 2026-11-22 | calcul | course d'affinage des idées des mentors | 150 USD | 2026-12-15 | Lazar | "
       "GO-2026-11-18-14 |\n")


def test_v11_go_trois_chiffres_ligne_lue_sain(tmp_path):
    o = L.verifier_go(_registre_go_essai(tmp_path, L14, L_3), dt.date(2026, 11, 27), go_id="GO-2026-11-22-151")
    assert o["id"] == "GO-2026-11-22-151"
    assert L.verifier_go(_registre_go_essai(tmp_path, L14, L_3), dt.date(2026, 11, 24))["id"] == "GO-2026-11-18-14"  # deux chiffres


def test_v11_go_revocation_a_trois_chiffres_vue_refuse(tmp_path):
    with pytest.raises(L.Refus, match="révoqué par GO-2026-11-22-150"):
        L.verifier_go(_registre_go_essai(tmp_path, L14, REV_3), dt.date(2026, 11, 24))


def test_v11_go_registre_derive_garde_la_revocation_a_trois_chiffres(tmp_path):
    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, REV_3, L_3), tmp_path / "derive.md")
    texte = (tmp_path / "derive.md").read_text(encoding="utf-8")
    assert d["nombre_de_lignes"] == 2 and "GO-2026-11-22-150" in texte and "GO-2026-11-22-151" not in texte


def test_v11_go_mutation_lecture_a_deux_chiffres_absente_du_lanceur():
    # artefact : la lecture de v10 (deux chiffres de rang seulement) ne doit plus figurer dans le lanceur
    src = Path(L.__file__).read_text(encoding="utf-8")
    assert r"(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|" not in src and src.count(r"(GO-\d{4}-\d{2}-\d{2}-\d{2,3})\s*\|") >= 2
