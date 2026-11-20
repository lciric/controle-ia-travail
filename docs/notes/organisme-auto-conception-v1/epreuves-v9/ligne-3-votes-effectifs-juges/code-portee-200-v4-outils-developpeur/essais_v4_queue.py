
# --- Version 4 — preuve : les sorties existantes du v3 sont égales à l'octet en v4 (racine des essais seule) ---------
EMPREINTE_BANC_V3 = "09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0"
NOM_DU_BANC_V3 = "banc_juges_scriptes_ligne_3_v3.py"


def _banc_v3():
    env = os.environ.get("BANC_V3_LIGNE_3_CHEMIN")
    candidats = ([Path(env)] if env else
                 [ICI / NOM_DU_BANC_V3, ICI.parent / "code-etage-1-v3" / NOM_DU_BANC_V3,
                  DEPOT_PAR_DEFAUT / "code-etage-1-v3" / NOM_DU_BANC_V3])
    for chemin in candidats:
        if chemin.is_file():
            assert _sha256(chemin) == EMPREINTE_BANC_V3, f"empreinte du banc v3 inattendue : {chemin}"
            return _charger("banc_juges_scriptes_ligne_3_v3", chemin)
    raise AssertionError("banc v3 introuvable (aucun repli silencieux)")


def _ecrire_comme_le_banc(objet):
    return (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def _chemins_seulement_dans(a, b, chemin=""):
    """Chemins des clés de `a` absentes de `b` (récursif ; une liste de longueur différente est un chemin)."""
    res = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a:
            if k not in b:
                res.append(f"{chemin}/{k}")
            else:
                res.extend(_chemins_seulement_dans(a[k], b[k], f"{chemin}/{k}"))
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            res.append(f"{chemin}[longueur]")
        for i, (x, y) in enumerate(zip(a, b)):
            res.extend(_chemins_seulement_dans(x, y, f"{chemin}/{i}"))
    return res


def test_v4_sorties_existantes_du_v3_egales_a_l_octet(tmp_path):
    """Toutes les sorties du v3 (résultat et manifeste de l'étage 1, en essai) sont égales à l'octet en v4, hors le nom
    de version ; aucune clé n'est ajoutée ni retirée ; mêmes dérivations ; et `cellule_puissance` rend la même cellule
    à n = 200 dans les deux bancs, sur les mêmes générateurs de la racine des essais."""
    v3 = _banc_v3()
    assert v3 is not banc and v3.VERSION == "banc-juges-scriptes-ligne-3-v3"
    assert banc.VERSION == "banc-juges-scriptes-ligne-3-v4"
    assert (v3.RACINE_ESSAIS, v3.TABLE_CLES) == (banc.RACINE_ESSAIS, banc.TABLE_CLES)
    for nom_cfg, cfg in (("essai", CONFIGURATION_D_ESSAI), ("essai_alarme_trois_m", CONFIGURATION_D_ESSAI_V3)):
        res3, man3 = v3.executer_etage_1(v3.Contexte("essais"), cfg, tmp_path / nom_cfg / "v3")
        res4, man4 = banc.executer_etage_1(banc.Contexte("essais"), cfg, tmp_path / nom_cfg / "v4")
        octets_v3 = (tmp_path / nom_cfg / "v3" / "resultat-etage-1-ligne-3-v3.json").read_bytes()
        octets_v4 = (tmp_path / nom_cfg / "v4" / "resultat-etage-1-ligne-3-v4.json").read_bytes()
        lu3, lu4 = json.loads(octets_v3), json.loads(octets_v4)
        assert _ecrire_comme_le_banc(lu3) == octets_v3           # garde : la relecture du v3 rend ses octets
        assert _chemins_seulement_dans(lu3, lu4) == []           # aucune clé du v3 ne manque en v4
        assert _chemins_seulement_dans(lu4, lu3) == []           # aucune clé neuve dans les sorties de l'étage 1
        v3_version = b'"version": "banc-juges-scriptes-ligne-3-v3"'
        v4_version = b'"version": "banc-juges-scriptes-ligne-3-v4"'
        assert octets_v3.count(v3_version) == 1 and octets_v4.count(v4_version) == 1
        assert octets_v4 == octets_v3.replace(v3_version, v4_version)   # toutes les sorties, à l'octet
        lu4["version"] = v3.VERSION
        assert _ecrire_comme_le_banc(lu4) == octets_v3
        assert man4["graines"] == man3["graines"]                # mêmes racines, table, dérivations
        assert man4["configuration_sha256"] == man3["configuration_sha256"]
        assert man4["configuration"] == man3["configuration"]
        aide = res4["criteres_mecaniques"][CLE_NEUVE_V3_DES_CRITERES]
        assert aide["carte_fcbf4a2dd1a57"] == MOT_CARTE_ALARME_ATTENDU
        if cfg["alarme"]["m"] == [10, 20, 40]:
            assert aide["prediction_P6"]["mot"] in MOTS_P6
            for c in res4["alarme"]:
                fa = aide["prediction_P6"]["par_m"][str(c["m"])]["clause_fausse_alarme"]
                assert (fa["suites_sans_changement_en_alarme"]
                        == c["par_bras"]["B"]["comptes_silence_1"]["suites_sans_changement_en_alarme"])
        else:
            assert aide["prediction_P6"]["mot"].startswith("incomplet")
    for comparaison, loi, rho, rp in (("unanimite", 3, 0.15, 0.0), ("juge_repete_trois_votes_majorite", 1, 0.0, 0.9)):
        g3 = v3.generateurs(v3.RACINE_ESSAIS, "essais_formules", 2)
        g4 = banc.generateurs(banc.RACINE_ESSAIS, "essais_formules", 2)
        c3 = v3.cellule_puissance(g3[0], g3[1], comparaison, 0.10, loi, rho, rp, 24, 60, n=200)
        c4 = banc.cellule_puissance(g4[0], g4[1], comparaison, 0.10, loi, rho, rp, 24, 60, n=200)
        assert c3["faisable"] is True and c4 == c3
    assert {d["racine"] for d in v3.JOURNAL_GRAINES} == {banc.RACINE_ESSAIS}


# =================================================================================================================
# Version 4 — mode « portée à 200 » (additif 3 v3, § 5, points 2 à 8, et § 6). Aucune racine neuve n'est dérivée :
# le mode neuf est joué sur la racine des essais seule ; les racines neuves ne sont essayées que par `verifier_racine`
# (aucune dérivation). La garde « dossier du code propre » est essayée dans un dépôt git jetable, sous le dossier
# temporaire des essais.
# =================================================================================================================
EMPREINTE_ADDITIF_3 = "71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807"
CONFIGURATION_PORTEE_200_ATTENDUE = {
    "repliques": 2000,
    "tirages_reechantillonnage": 2000,
    "puissance": {"ecarts": [0.05, 0.10, 0.15], "lois": [1, 3], "rhos": [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
                  "rhos_prime": [0.0, 0.5, 0.9], "n": 200},
}


class _ArretAvantTirage(Exception):
    """Levée par une garde remplacée dans un essai, pour qu'aucun tirage ne suive une garde fautive."""


def _arret_avant_tirage():
    raise _ArretAvantTirage("arrêt de l'essai avant tout tirage")


def _git(dossier, *args):
    env = dict(os.environ)
    env.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull})
    r = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60, env=env)
    assert r.returncode == 0, r.stderr
    return r.stdout


def _depot_jetable(tmp_path, nom="depot"):
    """Dépôt git jetable, créé sous le dossier temporaire des essais (jamais dans le dépôt du programme) : un dossier
    du code suivi et propre."""
    depot = tmp_path / nom
    code = depot / "code"
    code.mkdir(parents=True)
    _git(depot, "init", "-q")
    (code / "programme.py").write_text("# programme suivi, propre\n", encoding="utf-8")
    _git(depot, "add", "code/programme.py")
    _git(depot, "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "-c", "commit.gpgsign=false",
         "commit", "-q", "-m", "essai")
    assert _git(depot, "status", "--porcelain", "--", str(code)).strip() == ""
    return depot, code


def _cfg_portee_essai(repliques=12, tirages=40, n=200):
    cfg = json.loads(json.dumps(banc.CONFIGURATION_PORTEE_200))
    cfg["repliques"], cfg["tirages_reechantillonnage"] = repliques, tirages
    cfg["puissance"]["n"] = n
    return cfg


def _mondes_faisables_du_calcul(ecart="0.1"):
    """Mondes faisables, par le calcul de référence (sortie v2), à l'écart donné : (comparaison, loi, ρ, ρ′)."""
    sortie = _sortie_calcul()["monde_de_puissance"]
    mondes = set()
    for comparaison in banc.COMPARAISONS_PUISSANCE:
        for c in sortie[comparaison][ecart]["cellules"]:
            if not c["faisable"]:
                continue
            rp = c.get("rho_prime", 0.0)
            mondes.add((comparaison, 1, c["rho"], rp))
            if c["loi_3_jouable"]:
                mondes.add((comparaison, 3, c["rho"], rp))
    return mondes


def _juste(tmp_path):
    additif, emp = _additif_valide(tmp_path)
    return banc.Autorisation(additif, emp)


def _compteurs():
    return len(banc.JOURNAL_GRAINES), len(_ENTROPIES_CREEES)


# --- Configuration gelée et racines neuves -------------------------------------------------------------------------
def test_portee_200_configuration_gelee_et_table_des_cles():
    assert banc.CONFIGURATION_PORTEE_200 == CONFIGURATION_PORTEE_200_ATTENDUE
    altere = json.loads(json.dumps(CONFIGURATION_PORTEE_200_ATTENDUE))
    altere["puissance"]["n"] = 100
    assert banc.CONFIGURATION_PORTEE_200 != altere
    assert banc.EMPREINTE_ADDITIF_3_PORTEE_200 == EMPREINTE_ADDITIF_3
    assert (banc.TABLE_CLES["monde_de_puissance"], banc.TABLE_CLES["reechantillonnage_monde_de_puissance"]) == (2, 12)
    assert banc.MODES == {"essais": (2026111930, 2026111930),
                          "chronometrage_portee_200": (2026112031, 2026112031),
                          "portee_200": (2026112032, 2026112033)}
    assert banc.RACINES_SOUS_AUTORISATION == RACINES_PORTEE_200
    assert set(banc.RACINES_TOUJOURS_REFUSEES) == set(RACINES_ETAGES_1_ET_2)
    assert len(banc.enumerer_cellules_puissance(banc.CONFIGURATION_PORTEE_200["puissance"])) == 210


def test_portee_200_racines_neuves_autorisation_juste_acceptees_sans_derivation(tmp_path):
    juste = _juste(tmp_path)
    avant = _compteurs()
    for racine, tache in ((2026112031, "monde_de_puissance"), (2026112031, "reechantillonnage_monde_de_puissance"),
                          (2026112032, "monde_de_puissance"), (2026112033, "reechantillonnage_monde_de_puissance")):
        assert banc.verifier_racine(racine, tache, 210, juste) is None
    assert banc.verifier_racine(banc.RACINE_ESSAIS, "essais_gardes", 3) is None
    assert _compteurs() == avant


@pytest.mark.parametrize("cas", ["sans_autorisation", "empreinte_fausse", "tache_hors_table_2032", "tache_hors_table_2033",
                                 "tache_autre_bras_2031", "spawn_209", "spawn_1", "racine_voisine",
                                 "racine_etage_1", "racine_etage_2"])
def test_portee_200_racines_artefacts_refuses_sans_derivation(cas, tmp_path):
    juste = _juste(tmp_path)
    fausse = banc.Autorisation(juste.chemin_additif, "0" * 64)
    racine, tache, nombre, autorisation, motif = {
        "sans_autorisation": (2026112032, "monde_de_puissance", 210, None, "sans autorisation"),
        "empreinte_fausse": (2026112033, "reechantillonnage_monde_de_puissance", 210, fausse, "différente"),
        "tache_hors_table_2032": (2026112032, "reechantillonnage_monde_de_puissance", 210, juste, "hors de l'additif 3"),
        "tache_hors_table_2033": (2026112033, "monde_de_puissance", 210, juste, "hors de l'additif 3"),
        "tache_autre_bras_2031": (2026112031, "estimateur_et_agregation", 210, juste, "hors de l'additif 3"),
        "spawn_209": (2026112032, "monde_de_puissance", 209, juste, "spawn"),
        "spawn_1": (2026112031, "monde_de_puissance", 1, juste, "spawn"),
        "racine_voisine": (2026112034, "monde_de_puissance", 210, juste, "hors du texte"),
        "racine_etage_1": (2026111932, "monde_de_puissance", 210, juste, "étage 1 ou de l'étage 2"),
        "racine_etage_2": (2026111934, "monde_de_puissance", 210, juste, "étage 1 ou de l'étage 2"),
    }[cas]
    avant = _compteurs()
    with pytest.raises(banc.RefusGraine, match=motif):
        banc.verifier_racine(racine, tache, nombre, autorisation)
    with pytest.raises(banc.RefusGraine, match=motif):
        banc.generateurs(racine, tache, nombre, autorisation)
    assert _compteurs() == avant


def test_portee_200_etage_1_inatteignable_hors_essai(tmp_path):
    juste = _juste(tmp_path)
    avant = _compteurs()
    for mode in ("portee_200", "chronometrage_portee_200"):
        with pytest.raises(banc.RefusExecution, match="racine des essais"):
            banc.executer_etage_1(banc.Contexte(mode, juste), CONFIGURATION_D_ESSAI, tmp_path / f"etage-1-{mode}")
        assert not (tmp_path / f"etage-1-{mode}").exists()
    assert _compteurs() == avant


# --- Cas sain du mode neuf, sur la racine des essais, à petit nombre de répliques ----------------------------------
def test_portee_200_cas_sain_petit_nombre_de_repliques(tmp_path):
    _, code = _depot_jetable(tmp_path)
    calcul = _calcul()
    cfg = _cfg_portee_essai()
    sortie = tmp_path / "sortie-portee-200"
    resultat, manifeste = banc.executer_portee_200(banc.Contexte("essais"), cfg, sortie, dossier_du_code=code)
    cellules = resultat["monde_de_puissance"]
    enumeration = banc.enumerer_cellules_puissance(cfg["puissance"])
    assert len(cellules) == len(enumeration) == 210
    assert [(c["comparaison"], c["ecart_vise"], c["loi"], c["rho"], c["rho_prime"]) for c in cellules] == enumeration
    assert sum(1 for c in cellules if c["comparaison"] == "unanimite") == 42
    assert sum(1 for c in cellules if c["comparaison"] == "juge_seul") == 42
    assert sum(1 for c in cellules if c["comparaison"] == "juge_repete_trois_votes_majorite") == 126
    a_0_10 = {(c["comparaison"], c["loi"], c["rho"], c["rho_prime"]) for c in cellules
              if c["faisable"] and abs(c["ecart_vise"] - 0.10) < 1e-12}
    assert len(a_0_10) == 13 and a_0_10 == _mondes_faisables_du_calcul("0.1") == set(banc.MONDES_FAISABLES_A_0_10)
    sortie_calcul = _sortie_calcul()["monde_de_puissance"]
    for c in cellules:
        d_ref = calcul.resoudre(c["comparaison"], c["ecart_vise"], c["rho"], c["rho_prime"])
        if c["faisable"]:
            assert c["d"] == d_ref
            e = calcul.erreurs_equilibrees(d_ref, c["rho"], c["rho_prime"])
            assert c["ecart_vrai_formule"] == e[c["comparaison"]] - e["au_moins_un"]
            assert c["ecart_vrai_formule"] == pytest.approx(c["ecart_vise"], abs=1e-9)
            assert (c["vrais_rejetes_a"], c["faux_acceptes_b"]) == (0.2 + d_ref, 0.2 - d_ref)
            ref = [x for x in sortie_calcul[c["comparaison"]][str(c["ecart_vise"])]["cellules"]
                   if x["rho"] == c["rho"] and x.get("rho_prime", 0.0) == c["rho_prime"]]
            assert len(ref) == 1 and ref[0]["d"] == round(c["d"], 4)
            assert c["repliques"] == 12
            k = c["repliques_gagnees_par_comparaison"]
            assert set(k) == {"U", "S_1", "S_2", "R_3"} and all(type(v) is int and 0 <= v <= 12 for v in k.values())
            assert all(k[nom] / 12 == c["puissance_par_comparaison"][nom] for nom in k)
            assert sum(c["bras_C_regle_choisie"].values()) == 12
        elif d_ref is None:
            assert "d" not in c
        else:
            assert c["d"] == d_ref and c["loi"] == 3
    # Moitié « lecture » à n = 200 : 50 bons et 50 mauvais (et 50 et 50 à l'étalonnage).
    y = banc.classes(100)
    cal, lec = banc.indices_moities(100)
    assert (int(y[lec].sum()), int((~y[lec]).sum()), int(y[cal].sum()), int((~y[cal]).sum())) == (50, 50, 50, 50)
    # n = 200 est bien joué : une cellule rejouée sur les mêmes enfants rend la même chose à n = 200, autre à 100.
    rang = enumeration.index(("unanimite", 0.10, 1, 0.0, 0.0))
    gt = banc.generateurs(banc.RACINE_ESSAIS, "monde_de_puissance", 210)
    gr = banc.generateurs(banc.RACINE_ESSAIS, "reechantillonnage_monde_de_puissance", 210)
    rejouee = banc.cellule_puissance(gt[rang], gr[rang], "unanimite", 0.10, 1, 0.0, 0.0, 12, 40, n=200)
    attendue = {k: v for k, v in cellules[rang].items() if k != "repliques_gagnees_par_comparaison"}
    assert json.loads(json.dumps(rejouee)) == json.loads(json.dumps(attendue))
    gt = banc.generateurs(banc.RACINE_ESSAIS, "monde_de_puissance", 210)
    gr = banc.generateurs(banc.RACINE_ESSAIS, "reechantillonnage_monde_de_puissance", 210)
    a_100 = banc.cellule_puissance(gt[rang], gr[rang], "unanimite", 0.10, 1, 0.0, 0.0, 12, 40, n=100)
    assert a_100["ecart_observe_moyen"] != rejouee["ecart_observe_moyen"]
    # Aide, jamais verdict ; issue lue sur les comptes entiers.
    aide = resultat["criteres_mecaniques"]["puissance"]
    assert set(resultat["criteres_mecaniques"]) == {"puissance"}
    assert aide["nature"].startswith("aide") and "R13" in aide["nature"]
    assert aide["issue"] in ("A", "B") and aide["comparaisons_sans_cellule_faisable"] == []
    assert aide["cellules_faisables_lues_par_comparaison"] == {"U": 6, "S_1": 3, "S_2": 3, "R_3": 4}
    minimum = aide["repliques_gagnees_dans_la_cellule_la_plus_basse"]
    assert minimum == min(aide["minima_par_comparaison_en_repliques_gagnees"].values())
    assert aide["puissance_qui_decide"] == minimum / 12
    assert aide["issue"] == ("A" if 2 * minimum >= 12 else "B")
    assert aide["lecture_du_banc_v3_sur_les_memes_cellules"]["puissance_qui_decide"] == aide["puissance_qui_decide"]
    assert aide["cellules_au_minimum"] and all(x["repliques_gagnees"] == minimum for x in aide["cellules_au_minimum"])
    # Fichiers, compagnons, manifeste.
    chemin_res = sortie / "resultat-portee-200-ligne-3-v1.json"
    chemin_man = sortie / "manifeste-portee-200-ligne-3-v1.json"
    for chemin in (chemin_res, chemin_man):
        assert Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()[0] == _sha256(chemin)
    man = json.loads(chemin_man.read_text(encoding="utf-8"))
    assert man["programme_sha256"] == _sha256(CHEMIN_BANC)
    assert man["additif_qui_fait_foi_sha256"] == EMPREINTE_ADDITIF_3
    assert man["fichiers"] == {"resultat-portee-200-ligne-3-v1.json": _sha256(chemin_res)}
    assert man["configuration"] == cfg and man["configuration_sha256"] == banc.sha256_json(cfg)
    assert (man["graines"]["racine_des_tirages"], man["graines"]["racine_du_reechantillonnage"]) == (2026111930,
                                                                                                       2026111930)
    assert [(d["racine"], d["tache"], d["cle"], d["enfants"]) for d in man["graines"]["derivations"]] == [
        (2026111930, "monde_de_puissance", 2, 210), (2026111930, "reechantillonnage_monde_de_puissance", 12, 210)]
    assert man["depot"]["dossier_du_code_propre"] is True
    assert man["autorisation"] is None and man["mode"] == "essais"


# --- Garde « taille » ------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("n", [100, 400, 199, 200.0, "200", None, True])
def test_portee_200_garde_taille_artefact_n_autre_que_200(n, tmp_path):
    _, code = _depot_jetable(tmp_path)
    cfg = _cfg_portee_essai()
    if n is None:
        del cfg["puissance"]["n"]
    else:
        cfg["puissance"]["n"] = n
    avant = _compteurs()
    with pytest.raises(banc.RefusExecution, match="taille"):
        banc.executer_portee_200(banc.Contexte("essais"), cfg, tmp_path / "sortie", dossier_du_code=code)
    assert not (tmp_path / "sortie").exists()
    assert _compteurs() == avant


# --- Configuration gelée hors essai, mode, dossier du code imposé ---------------------------------------------------
def test_portee_200_hors_essai_configuration_gelee_seule(tmp_path, monkeypatch):
    """L'autorisation donnée est fausse et la garde qui suit la vérification des racines est remplacée par un arrêt :
    une garde manquante ne fait dériver aucune racine neuve."""
    monkeypatch.setattr(banc, "verifier_gardes_avant_tirage", _arret_avant_tirage)
    _, code = _depot_jetable(tmp_path)
    fausse = banc.Autorisation(_juste(tmp_path).chemin_additif, "0" * 64)
    avant = _compteurs()
    with pytest.raises(banc.RefusExecution, match="configuration autre"):
        banc.executer_portee_200(banc.Contexte("portee_200", fausse), _cfg_portee_essai(), tmp_path / "s1")
    with pytest.raises(banc.RefusExecution, match="permis en essai seulement"):
        banc.executer_portee_200(banc.Contexte("portee_200", fausse), banc.CONFIGURATION_PORTEE_200, tmp_path / "s2",
                                 dossier_du_code=code)
    with pytest.raises(banc.RefusExecution, match="mode"):
        banc.executer_portee_200(banc.Contexte("chronometrage_portee_200", fausse), banc.CONFIGURATION_PORTEE_200,
                                 tmp_path / "s3")
    for nom in ("s1", "s2", "s3"):
        assert not (tmp_path / nom).exists()
    assert _compteurs() == avant


def test_portee_200_autorisation_refusee_avant_derivation_quand_les_autres_gardes_passent(tmp_path, monkeypatch):
    """Racine neuve sans autorisation, ou d'empreinte fausse : refus avant toute dérivation, même quand la garde du
    dossier du code est levée (remplacée par une garde qui passe) ; la garde suivante est un arrêt."""
    monkeypatch.setattr(banc, "verifier_dossier_du_code_propre", lambda code, sortie: None)
    monkeypatch.setattr(banc, "verifier_gardes_avant_tirage", _arret_avant_tirage)
    juste = _juste(tmp_path)
    avant = _compteurs()
    for autorisation, motif in ((None, "sans autorisation"),
                                (banc.Autorisation(juste.chemin_additif, "0" * 64), "différente de l'attendue"),
                                (banc.Autorisation(tmp_path / "absent.md", juste.empreinte_additif), "additif absent")):
        with pytest.raises(banc.RefusGraine, match=motif):
            banc.executer_portee_200(banc.Contexte("portee_200", autorisation), banc.CONFIGURATION_PORTEE_200,
                                     tmp_path / "sortie")
    assert not (tmp_path / "sortie").exists()
    assert _compteurs() == avant


# --- Garde « dossier du code propre », dans un dépôt git jetable ----------------------------------------------------
def test_portee_200_dossier_du_code_propre_cas_sain(tmp_path):
    _, code = _depot_jetable(tmp_path)
    assert banc.verifier_dossier_du_code_propre(code, tmp_path / "sortie-hors-du-code") is None
    assert banc.verifier_dossier_du_code_propre(code, code.parent / "sortie-a-cote") is None
    assert banc.commit_du_depot(code)["dossier_du_code_propre"] is True


@pytest.mark.parametrize("cas", ["fichier_etranger", "fichier_suivi_modifie", "fichier_etranger_sous_dossier",
                                 "sortie_sous_le_code", "sortie_egale_au_code", "hors_depot", "archives"])
def test_portee_200_dossier_du_code_propre_artefacts_refus_avant_derivation(cas, tmp_path, monkeypatch):
    depot, code = _depot_jetable(tmp_path)
    sortie = tmp_path / "sortie"
    motif = "non propre"
    if cas == "fichier_etranger":
        (code / "etranger.txt").write_text("x\n", encoding="utf-8")
    elif cas == "fichier_suivi_modifie":
        (code / "programme.py").write_text("# modifié\n", encoding="utf-8")
    elif cas == "fichier_etranger_sous_dossier":
        (code / "sous").mkdir()
        (code / "sous" / "etranger.json").write_text("{}\n", encoding="utf-8")
    elif cas == "sortie_sous_le_code":
        sortie, motif = code / "sortie", "sous le dossier du code"
    elif cas == "sortie_egale_au_code":
        sortie, motif = code, "sous le dossier du code"
    elif cas == "hors_depot":
        code = tmp_path / "hors-depot" / "code"
        code.mkdir(parents=True)
        (code / "programme.py").write_text("# hors dépôt\n", encoding="utf-8")
        monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))
        motif = "hors d'un dépôt"
    elif cas == "archives":
        (code / "archives-reponses-modeles").mkdir()
        motif = "archives-reponses-modeles"
    avant = _compteurs()
    with pytest.raises(banc.RefusExecution, match=motif):
        banc.verifier_dossier_du_code_propre(code, sortie)
    if cas != "sortie_egale_au_code":
        with pytest.raises(banc.RefusExecution, match=motif):
            banc.executer_portee_200(banc.Contexte("essais"), _cfg_portee_essai(), sortie, dossier_du_code=code)
        assert not sortie.exists()
    assert _compteurs() == avant


def test_portee_200_dossier_du_code_par_defaut_est_celui_du_banc(tmp_path, monkeypatch):
    """Sans `dossier_du_code`, la garde porte sur le dossier du fichier du banc."""
    vus = []

    def garde(code, sortie):
        vus.append((Path(code).resolve(), Path(sortie)))
        raise banc.RefusExecution("arrêt de l'essai à la garde du dossier du code")

    monkeypatch.setattr(banc, "verifier_dossier_du_code_propre", garde)
    avant = _compteurs()
    with pytest.raises(banc.RefusExecution, match="arrêt de l'essai"):
        banc.executer_portee_200(banc.Contexte("essais"), _cfg_portee_essai(), tmp_path / "sortie")
    assert vus == [(Path(banc.__file__).resolve().parent, tmp_path / "sortie")]
    assert _compteurs() == avant


# --- Une exécution par dossier ---------------------------------------------------------------------------------------
def test_portee_200_une_execution_par_dossier(tmp_path):
    _, code = _depot_jetable(tmp_path)
    sortie = tmp_path / "deja-la"
    sortie.mkdir()
    avant = _compteurs()
    with pytest.raises(banc.RefusExecution, match="déjà présent"):
        banc.executer_portee_200(banc.Contexte("essais"), _cfg_portee_essai(), sortie, dossier_du_code=code)
    assert _compteurs() == avant
    sortie_neuve = tmp_path / "neuve"
    banc.executer_portee_200(banc.Contexte("essais"), _cfg_portee_essai(repliques=3, tirages=10), sortie_neuve,
                             dossier_du_code=code)
    with pytest.raises(banc.RefusExecution, match="déjà présent"):
        banc.executer_portee_200(banc.Contexte("essais"), _cfg_portee_essai(repliques=3, tirages=10), sortie_neuve,
                                 dossier_du_code=code)


# --- Garde « formules » ----------------------------------------------------------------------------------------------
def test_portee_200_formules_cas_sain_contre_le_calcul_de_reference():
    calcul = _calcul()
    banc.verifier_gardes_portee_200()
    mondes = set()
    for (comparaison, ecart, loi, rho, rp) in banc.enumerer_cellules_puissance(banc.CONFIGURATION_PORTEE_200["puissance"]):
        ok, d = banc.faisabilite_cellule_puissance(comparaison, ecart, loi, rho, rp)
        assert d == calcul.resoudre(comparaison, ecart, rho, rp)
        if ok:
            e = calcul.erreurs_equilibrees(d, rho, rp)
            assert e[comparaison] - e["au_moins_un"] == pytest.approx(ecart, abs=1e-9)
            if abs(ecart - 0.10) < 1e-12:
                mondes.add((comparaison, loi, rho, rp))
    assert mondes == _mondes_faisables_du_calcul("0.1") == set(banc.MONDES_FAISABLES_A_0_10)
    assert len(banc.MONDES_FAISABLES_A_0_10) == 13


def _bissection_faussee(comparaison, ecart, rho, rho_prime):
    d = banc_resoudre_d_origine(comparaison, ecart, rho, rho_prime)
    return None if d is None else min(d * 1.01, banc.D_MAX)


banc_resoudre_d_origine = banc.resoudre_dissymetrie


@pytest.mark.parametrize("cas", ["bissection_faussee", "formule_faussee", "mondes_attendus_alteres"])
def test_portee_200_formules_artefacts_banc_invalide_avant_tout_tirage(cas, tmp_path, monkeypatch):
    if cas == "bissection_faussee":
        monkeypatch.setattr(banc, "resoudre_dissymetrie", _bissection_faussee)
    elif cas == "formule_faussee":
        origine = banc.erreurs_equilibrees_formules

        def faussee(d, rho, rho_prime):
            e = dict(origine(d, rho, rho_prime))
            e["au_moins_un"] = e["au_moins_un"] - 0.001
            return e
        monkeypatch.setattr(banc, "erreurs_equilibrees_formules", faussee)
    else:
        monkeypatch.setattr(banc, "MONDES_FAISABLES_A_0_10", banc.MONDES_FAISABLES_A_0_10[:-1])
    with pytest.raises(banc.BancInvalide, match="formules"):
        banc.verifier_gardes_portee_200()
    _, code = _depot_jetable(tmp_path)
    avant = _compteurs()
    with pytest.raises(banc.BancInvalide, match="formules"):
        banc.executer_portee_200(banc.Contexte("essais"), _cfg_portee_essai(), tmp_path / "sortie", dossier_du_code=code)
    assert not (tmp_path / "sortie").exists()
    assert _compteurs() == avant


# --- Règle de lecture (§ 3) ------------------------------------------------------------------------------------------
def _cellules_factices_portee(minimum, repliques=2000, sans=()):
    """Les treize mondes faisables à 0,10, plus des cellules hors lecture (écart 0,05, faisable, à 0 répliques) ;
    toutes les comparaisons à repliques, sauf la cellule « unanimité, loi 3, ρ = 0,15 », à `minimum` pour U."""
    cellules = []
    for (comparaison, loi, rho, rp) in banc.MONDES_FAISABLES_A_0_10:
        if comparaison in sans:
            continue
        k = {"U": repliques, "S_1": repliques, "S_2": repliques, "R_3": repliques}
        if (comparaison, loi, rho) == ("unanimite", 3, 0.15):
            k["U"] = minimum
        cellules.append({"comparaison": comparaison, "ecart_vise": 0.10, "loi": loi, "rho": rho, "rho_prime": rp,
                         "faisable": True, "repliques": repliques, "repliques_gagnees_par_comparaison": k,
                         "puissance_par_comparaison": {nom: v / repliques for nom, v in k.items()}})
    cellules.append({"comparaison": "unanimite", "ecart_vise": 0.05, "loi": 1, "rho": 0.0, "rho_prime": 0.0,
                     "faisable": True, "repliques": repliques,
                     "repliques_gagnees_par_comparaison": {"U": 0, "S_1": 0, "S_2": 0, "R_3": 0},
                     "puissance_par_comparaison": {"U": 0.0, "S_1": 0.0, "S_2": 0.0, "R_3": 0.0}})
    cellules.append({"comparaison": "unanimite", "ecart_vise": 0.10, "loi": 1, "rho": 0.6, "rho_prime": 0.0,
                     "faisable": False})
    return cellules


def test_portee_200_regle_de_lecture_cas_sain():
    f = banc.issue_de_la_regle_de_lecture
    assert (f(1000, 2000, []), f(999, 2000, []), f(2000, 2000, ["R_3"]), f(0, 2000, [])) == ("A", "B", "B", "B")
    r = banc.criteres_portee_200(_cellules_factices_portee(1000), 2000)
    assert (r["issue"], r["puissance_qui_decide"], r["repliques_gagnees_dans_la_cellule_la_plus_basse"]) == ("A", 0.5, 1000)
    assert "ne s'applique pas" in r["ce_qu_elle_dit"] and r["pres_du_seuil"]["vrai"] is True
    assert r["cellules_au_minimum"] == [{"rang": 5, "comparaison_du_test": "U", "comparaison_du_monde": "unanimite",
                                         "loi": 3, "rho": 0.15, "rho_prime": 0.0, "repliques_gagnees": 1000,
                                         "repliques": 2000}]
    assert r["minima_par_comparaison"] == {"U": 0.5, "S_1": 1.0, "S_2": 1.0, "R_3": 1.0}
    assert r["lecture_du_banc_v3_sur_les_memes_cellules"]["comparaisons_d_agregations"] == "peuvent porter un « oui »"
    r = banc.criteres_portee_200(_cellules_factices_portee(999), 2000)
    assert r["issue"] == "B" and "descriptives" in r["ce_qu_elle_dit"] and r["puissance_qui_decide"] == 0.4995
    assert r["lecture_du_banc_v3_sur_les_memes_cellules"]["comparaisons_d_agregations"].startswith("descriptives")
    for k, pres in ((955, False), (956, True), (1044, True), (1045, False)):
        assert banc.criteres_portee_200(_cellules_factices_portee(k), 2000)["pres_du_seuil"]["vrai"] is pres
    r = banc.criteres_portee_200(_cellules_factices_portee(2000, sans=("juge_repete_trois_votes_majorite",)), 2000)
    assert (r["issue"], r["puissance_qui_decide"], r["comparaisons_sans_cellule_faisable"]) == ("B", None, ["R_3"])
    banc.verifier_gardes_portee_200()


def test_portee_200_regle_de_lecture_artefact_codee_a_l_envers(monkeypatch):
    """1 000 répliques sur 2 000 rendues « descriptives » : l'écart est visible à l'aide et la garde déclare le banc
    invalide avant tout tirage."""
    def a_l_envers(minimum, repliques, sans):
        if sans:
            return "B"
        return "A" if 2 * minimum > repliques else "B"
    monkeypatch.setattr(banc, "issue_de_la_regle_de_lecture", a_l_envers)
    r = banc.criteres_portee_200(_cellules_factices_portee(1000), 2000)
    assert r["issue"] == "B" and r["puissance_qui_decide"] == 0.5
    with pytest.raises(banc.BancInvalide, match="règle de lecture"):
        banc.verifier_gardes_portee_200()


def test_portee_200_comptes_gagnes_entiers():
    c = {"repliques": 2000, "puissance_par_comparaison": {"U": 0.5, "S_1": 0.0, "S_2": 1.0, "R_3": 1999 / 2000}}
    assert banc.comptes_gagnes(c) == {"U": 1000, "S_1": 0, "S_2": 2000, "R_3": 1999}
    c["puissance_par_comparaison"]["U"] = 0.5000001
    with pytest.raises(banc.BancInvalide):
        banc.comptes_gagnes(c)


def test_portee_200_variables_de_chemin(monkeypatch):
    for nom in banc.VARIABLES_DE_CHEMIN_INTERDITES:
        monkeypatch.delenv(nom, raising=False)
    banc.verifier_variables_de_chemin_non_posees()
    monkeypatch.setenv("CHRONOMETRAGE_LIGNE_3_CHEMIN", "/x")
    with pytest.raises(banc.RefusExecution):
        banc.verifier_variables_de_chemin_non_posees()


# =================================================================================================================
# Essai final : aucune graine des racines 2026111931 à 2026111937, ni des racines neuves 2026112031 à 2026112033,
# dérivée dans ce processus
# =================================================================================================================
def test_zz_final_aucune_graine_des_racines_decisives_derivee():
    assert banc.JOURNAL_GRAINES, "aucune dérivation enregistrée : le journal ne fonctionne pas"
    assert {d["racine"] for d in banc.JOURNAL_GRAINES} == {banc.RACINE_ESSAIS}
    assert _ENTROPIES_CREEES, "l'enregistrement des SeedSequence ne fonctionne pas"
    for entropie in _ENTROPIES_CREEES:
        assert entropie not in RACINES_INTERDITES_AUX_ESSAIS
    assert set(_ENTROPIES_CREEES) == {banc.RACINE_ESSAIS}
