# Exécuté par faire_lanceur_v11.py sur `src` (fonction r) : points techniques du brouillon 1 du préenregistrement v11.
r('''        if not _nombre(plafond) or plafond <= 0 or plafond > PLAFOND_ARRET_USD or (nom == "claude" and plafond != PLAFOND_ARRET_USD):
            raise Refus(f"relais {nom} : plafond {plafond} hors règle (≤ 150 ; Claude : 150, relais de ligne entière)")''',
  '''        exige_claude = ((parts or {}).get("claude") or {}).get("plafond_relais_exige_usd", PLAFOND_PART_CLAUDE_USD)  # v11 : 45
        if not _nombre(plafond) or plafond <= 0 or plafond > PLAFOND_ARRET_USD or (nom == "claude" and abs(plafond - exige_claude) > 1e-9):
            raise Refus(f"relais {nom} : plafond {plafond} hors règle (≤ 150 ; Claude : égal au plafond de la part Claude du relevé, "
                        f"{exige_claude} USD, v11)")''')
r('''r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v11"), parts)''',
  '''r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v11"), parts)
    # v11 : le relais Claude doit être lancé au plafond de la part Claude, calculé sur le relevé (le relevé précède le relais)
    parts["claude"] = dict(parts.get("claude") or {}, plafond_relais_exige_usd=credits[CLE_CLAUDE]["plafond_part_claude_usd"])''')
r('''    fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
    liste = json.loads''', '''    fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
    argon_v11 = appliquer_emplacement_argon(fixe)  # v11 : plafond de session des juges, en attente du mot de la mère
    liste = json.loads''')
r('''def verifier_course_jamais_lancee(r: Reglages) -> None:''', '''def appliquer_emplacement_argon(fixe: dict) -> dict:
    """v11 (brouillon 1 du préenregistrement v11, point 4) : `argon_v11.plafond_session_juge_usd` de la configuration ; vide
    (null) : en attente du mot de la mère, plafond des juges inchangé ; rempli : réel dans ]0 ; 3,00] qui remplace
    `plafonds_session.juge` (les deux juges : l'orchestrateur n'a qu'un plafond par rôle) ; toute autre valeur : refus."""
    bloc = fixe.get("argon_v11")
    if not isinstance(bloc, dict) or "plafond_session_juge_usd" not in bloc:
        raise Refus("configuration : emplacement argon_v11.plafond_session_juge_usd absent (v11)")
    v = bloc["plafond_session_juge_usd"]
    avant = fixe["plafonds_session"]["juge"]
    if v is None:
        return {"plafond_session_juge_usd": avant, "emplacement": None, "statut": "en attente du mot de la mère"}
    if not _nombre(v) or not 0 < float(v) <= float(fixe["plafonds_session"]["proposeur"]):
        raise Refus(f"configuration : argon_v11.plafond_session_juge_usd = {v!r} : réel dans ]0 ; plafond d'un proposeur] exigé")
    fixe["plafonds_session"]["juge"] = float(v)
    return {"plafond_session_juge_usd": float(v), "emplacement": float(v), "avant": avant, "statut": "rempli"}


def verifier_course_jamais_lancee(r: Reglages) -> None:''')
r('''                                                       "risques_v6", "changements_v11")}''',
  '''                                                       "risques_v6", "changements_v11", "argon_v11")}''')
r('''        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"], float(couverture), plafond_luc)''',
  '''        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"],
                                             float(credits[CLE_CLAUDE]["plafond_part_claude_usd"]))''')
r('''        ecrire_scelle(dossier_run / "alerte-cle-claude.json",
                      {"alerte": f"course arrêtée proprement sur la clé {CLE_CLAUDE} : " +
                                 ("plafond propre de 45 USD atteint (R-4995), sans relance" if arret_luc["code"] == 8 else
                                  "couverture déclarée atteinte ou non comptable (GO-2026-11-22-111)"),''',
  '''        ecrire_scelle(dossier_run / "alerte-arret-part-claude.json",
                      {"alerte": f"course arrêtée proprement sur la part Claude ({CLE_CLAUDE}) : premier refus du relais, plafond de "
                                 "la part atteint, ou part non comptable ; sans relance",''')
r('''    if arret_luc in (7, 8):  # v11 : arrêt propre sur la clé Claude (8 : plafond propre de LUC ; 7 : couverture)
        return arret_luc''', '''    if arret_luc == 5:  # v11 : arrêt propre sur la part Claude (premier 402 du relais Claude, plafond, illisible)
        return 5''')
r('''                            "7": "arrêt propre : couverture de LUC (solde + recharge déclarés) atteinte ou non comptable",
                            "8": "arrêt propre : plafond propre de LUC (45 USD, R-4995) atteint, sans relance"},''',
  '''                            "5 (v11)": "ou arrêt propre sur la part Claude : premier refus (402) du relais Claude, plafond de la "
                                       "part atteint, état illisible (alerte-arret-part-claude.json)"},''')
r('''"surveillance": ("au fil de l'eau, toutes les " + str(r.intervalle_surveillance_s) + " s") if reel else "moteur simulé : aucune"},''',
  '''"surveillance": ("au fil de l'eau, toutes les " + str(r.intervalle_surveillance_s) + " s") if reel else "moteur simulé : aucune",
                       "plafond_part_claude_usd": (credits.get(CLE_CLAUDE) or {}).get("plafond_part_claude_usd")},
        "argon_v11": argon_v11,''')

# --- 0,8 de la couverture : paramètre nommé de la configuration (alignement sur le préenregistrement) -------------------------
r('''    lu = ((fixe.get("changements_v11") or {}).get("plafond_part_claude_usd"))
    if not _nombre(lu) or float(lu) != PLAFOND_PART_CLAUDE_USD or not 0 < PLAFOND_PART_CLAUDE_USD <= PLAFOND_ARRET_USD:
        raise Refus(f"plafond propre de {CLE_CLAUDE} : configuration {lu!r}, lanceur {PLAFOND_PART_CLAUDE_USD!r} ; 45 USD exigés "
                    "aux deux (R-4995) : un plafond retiré ou relevé ne part pas")
    return float(lu)''', '''    bloc = fixe.get("changements_v11") or {}
    lu, part = bloc.get("plafond_part_claude_usd"), bloc.get("part_de_la_couverture")
    if not _nombre(lu) or float(lu) != PLAFOND_PART_CLAUDE_USD or not 0 < PLAFOND_PART_CLAUDE_USD <= PLAFOND_ARRET_USD:
        raise Refus(f"plafond propre de {CLE_CLAUDE} : configuration {lu!r}, lanceur {PLAFOND_PART_CLAUDE_USD!r} ; 45 USD exigés "
                    "aux deux (R-4995) : un plafond retiré ou relevé ne part pas")
    if not _nombre(part) or float(part) != PART_DE_LA_COUVERTURE or not 0 < PART_DE_LA_COUVERTURE <= 1:
        raise Refus(f"part de la couverture de {CLE_CLAUDE} : configuration {part!r}, lanceur {PART_DE_LA_COUVERTURE!r} ; 0,8 exigé "
                    "aux deux : une part retirée ou relevée ne part pas")
    return float(lu)''')

# --- Argon sous la garde Google (décision de la mère, 22 novembre) ---------------------------------------------------------
r('''GARDE_GOOGLE_PRODUCTION = "/home/user/controle-ia-travail/src/controle_ia/garde_google_v3.py"''',
  '''GARDE_GOOGLE_PRODUCTION = "/home/user/controle-ia-travail/src/controle_ia/garde_google_v3.py"
COMMANDES_EPINGLEES["argon"] = dict(COMMANDES_EPINGLEES["carbon"])  # v11 : Argon par la même commande en flux
# v11 (décision de la mère) : Argon proposeur et second juge sous la garde Google, par la commande en flux et un relais Gemini v3
# (port 8788, modèle gemini-4-argon). Réglages : niveau « high », provision 24 576, sortie 45 056 (texte 20 480 ≥ 16 000 et
# > 2 × 9 000 caractères) ; prix de l'enveloppe d'Argon v5 (8,3 / 41,5, sortie SUPPOSÉE) ; la provision est une HYPOTHÈSE à
# fixer par le devis v11 (aucune pensée d'Argon au niveau « high » n'est relevée dans les pièces lues).
PROVISION_PENSEE_ARGON = 24576
MAX_SORTIE_ARGON = 45056''')
r('''    "astra": ["--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6.2-astra",''',
  '''    "argon": ["--espece", "argon", "--modele", "gemini-4-argon", "--url-base", f"http://127.0.0.1:{PORT_ARGON}/v1beta",
              "--prix-entree", "8.3", "--prix-sortie", "41.5", "--niveau-reflexion", "high",
              "--provision-pensee-jetons", str(PROVISION_PENSEE_ARGON), "--max-sortie-jetons", str(MAX_SORTIE_ARGON),
              "--delai-s", str(DELAI_CARBON_S), "--delai-requete-s", str(DELAI_REQUETE_CARBON_S),
              "--roles", "proposeur_ideation,juge_ideation", "--garde", GARDE_GOOGLE_PRODUCTION],
    "astra": ["--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6.2-astra",''')
r('''PORT_ARGON = 8788  # l'enveloppe d'Argon v5 (épinglée) parle à 127.0.0.1:8788''',
  '''PORT_ARGON = 8788  # v11 : relais Gemini v3 d'Argon (en flux) ; l'enveloppe v5 n'est plus déclarée''')
r('''                     "argon": ("relais_gemini_v2.py", "2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb"),''',
  '''                     "argon": ("relais_gemini_v3.py", "2cf6bc6df83f8847e75911c8cc0b6153c4467b36ce69273de649b5cbdc7e2378"),  # v11''')
r('''        if nom == "argon":
            attendue = ["bash", str(r.depot / PIECES["enveloppe_argon"][0])]
            if b.get("commande") != attendue:
                raise Refus(f"fournisseurs.argon.commande : {attendue} exigée (enveloppe épinglée)")''',
  '''        if nom == "argon":  # v11 : la commande en flux épinglée, aux arguments épinglés (garde Google) ; l'enveloppe v5 est refusée
            c = b.get("commande") if isinstance(b.get("commande"), list) else []
            ep = COMMANDES_EPINGLEES["argon"]
            if len(c) < 4 or not os.path.isabs(c[0]) or c[1:3] != ["-I", "-B"] or os.path.basename(c[3]) not in ep \\
                    or not os.path.isfile(c[3]) or sha256_fichier(Path(c[3])) != ep[os.path.basename(c[3])]:
                raise Refus(f"fournisseurs.argon.commande : « python -I -B <commande en flux épinglée> » exigé ({sorted(ep)}) ; "
                            "l'enveloppe v5 (commande_argon_v3d, hors garde Google) est refusée")
            if c[4:] != ARGUMENTS_COMMANDES["argon"]:
                raise Refus(f"fournisseurs.argon.commande : arguments différents des arguments épinglés {ARGUMENTS_COMMANDES['argon']}")''')
r('''        if nom == "carbon":  # v11 : relais Gemini v3 en flux ; délais explicites (aucun défaut supposé)''',
  '''        if nom in GEMINI:  # v11 : relais Gemini v3 en flux (Carbon et Argon) ; délais explicites (aucun défaut supposé)''')
r('''                raise Refus("relais carbon : --delai-silence-s ou --delai-amont-s illisible") from None
            if not 0 < silence <= DELAI_SILENCE_RELAIS_MAX_S:
                raise Refus(f"relais carbon : --delai-silence-s {silence:g} hors de ]0, {DELAI_SILENCE_RELAIS_MAX_S:g}] (coupure à 300 s)")
            if amont < DELAI_CARBON_S:
                raise Refus(f"relais carbon : --delai-amont-s {amont:g} < délai de la commande {DELAI_CARBON_S} (relais ≥ commande)")
            if "--sans-pensees-amont" in args:
                raise Refus("relais carbon : --sans-pensees-amont refusé (les pensées doivent être demandées à l'amont)")''',
  '''                raise Refus(f"relais {nom} : --delai-silence-s ou --delai-amont-s illisible") from None
            if not 0 < silence <= DELAI_SILENCE_RELAIS_MAX_S:
                raise Refus(f"relais {nom} : --delai-silence-s {silence:g} hors de ]0, {DELAI_SILENCE_RELAIS_MAX_S:g}] (coupure à 300 s)")
            if amont < DELAI_CARBON_S:
                raise Refus(f"relais {nom} : --delai-amont-s {amont:g} < délai de la commande {DELAI_CARBON_S} (relais ≥ commande)")
            if "--sans-pensees-amont" in args:
                raise Refus(f"relais {nom} : --sans-pensees-amont refusé (les pensées doivent être demandées à l'amont)")''')
r('''                    raise Refus(f"relais carbon : {option} absent des arguments lus par PID (explicite exigé)")''',
  '''                    raise Refus(f"relais {nom} : {option} absent des arguments lus par PID (explicite exigé)")''')
# garde Google : Argon par sa commande déclarée, en flux
r('''        if nom == "carbon":
            c = b["commande"]
            commande, args, env_cle = Path(c[3]), (_remplacer_option(list(c[4:]), "--garde", str(garde_chemin)) if "--garde" in c[4:] else list(c[4:])), {}
        else:
            commande = Path(pieces["commande_argon"]["absolu"])
            args = arguments_enveloppe_argon(Path(pieces["enveloppe_argon"]["absolu"]))
            env_cle = {"GEMINI_API_KEY": "factice-relais"}  # comme l'enveloppe : jeton factice, la vraie clé reste au relais''',
  '''        c = b.get("commande") or []
        if len(c) >= 4 and c[0] != "bash":  # v11 : commande déclarée (en flux) ; --garde remplacé par la pièce vérifiée
            commande, args, env_cle = Path(c[3]), (_remplacer_option(list(c[4:]), "--garde", str(garde_chemin)) if "--garde" in c[4:] else list(c[4:])), {}
        else:  # enveloppe v5 d'Argon (hors garde) : jouée telle quelle pour dire ce qu'elle enverrait
            commande = Path(pieces["commande_argon"]["absolu"])
            args = arguments_enveloppe_argon(Path(pieces["enveloppe_argon"]["absolu"]))
            env_cle = {"GEMINI_API_KEY": "factice-relais"}  # comme l'enveloppe : jeton factice, la vraie clé reste au relais''')
r('''                corps, mode = gens[0]
                if nom == "carbon":
                    mode = "flux"''', '''                corps, mode = gens[0]
                if "--niveau-reflexion" in args:  # commande en flux (relais v3 : amont lu en flux)
                    mode = "flux"''')
# pire cas d'Argon par rôle : le plafond de session des juges doit payer un appel au pire
r('''def parts_au_pire(fixe: dict, liste: dict, pieces: dict, decl: dict) -> dict:''', '''def controler_pire_cas_argon(decl: dict, fixe: dict, liste: dict, pieces: dict) -> dict | None:
    """v11 : Argon sous la garde Google (commande en flux, sortie jamais abaissée) : pour chaque rôle (proposeur, juge), pire cas
    d'un appel = entrée gardée (caractères / 3 × 1,05) × prix d'entrée + sortie × prix de sortie ≤ plafond de session du rôle ;
    sinon refus, avec le plafond minimal qui le paierait (à fixer par le devis v11 dans `argon_v11.plafond_session_juge_usd`).
    Entrée d'un juge : consigne du juge + une carte de 9 000 caractères au plus + 1 000 caractères de marge (SUPPOSÉ)."""
    b = decl["fournisseurs"].get("argon")
    if b is None or (b.get("commande") or [None])[0] == "bash":
        return None
    a = b["commande"][4:]
    pe, ps = float(_valeur_arg(a, "--prix-entree")) / 1e6, float(_valeur_arg(a, "--prix-sortie")) / 1e6
    p, smax = float(_valeur_arg(a, "--provision-pensee-jetons")), float(_valeur_arg(a, "--max-sortie-jetons"))
    texte = smax - p
    limite_invite = int(fixe.get("cartes_par_appel") or 1) * CARACTERES_PAR_CARTE_MAX
    if texte < TEXTE_MIN_GOOGLE or texte <= limite_invite:
        raise Refus(f"fournisseurs.argon.commande : texte {texte:g} jetons : au moins {TEXTE_MIN_GOOGLE} et plus que {limite_invite} exigés")
    consigne_p = Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    consigne_j = Path(pieces["consigne_juge"]["absolu"]).read_text(encoding="utf-8")
    caracteres = {"proposeur": max(len(consigne_servie_proposeur(consigne_p, expurger(texte_de_case(f))[0])) for f in liste["fils"]),
                  "juge": len(consigne_j) + CARACTERES_PAR_CARTE_MAX + 1000}
    out = {}
    for role, n in caracteres.items():
        e = math.ceil(n / CARACTERES_PAR_JETON_CARBON * (1 + MARGE_ENTREE_CARBON))
        pire = e * pe + smax * ps
        plafond = float(fixe["plafonds_session"][role])
        minimal = math.ceil(pire * 100) / 100
        if pire > plafond + 1e-12:
            raise Refus(f"fournisseurs.argon.commande : pire cas d'un appel de {role} {pire:.6f} USD > plafond de session {plafond} "
                        f"USD : la commande refuserait chaque appel (code 4) ; plafond minimal {minimal} USD "
                        "(argon_v11.plafond_session_juge_usd pour les juges, fixé par le devis v11)")
        out[role] = {"caracteres": n, "entree_gardee_jetons": e, "sortie_jetons": int(smax), "pire_cas_appel_usd": round(pire, 6),
                     "plafond_session_usd": plafond, "plafond_minimal_usd": minimal}
    return {"roles": out, "texte_jetons": texte, "provision_jetons": p, "note": "provision d'Argon SUPPOSÉE (devis v11)"}


def parts_au_pire(fixe: dict, liste: dict, pieces: dict, decl: dict) -> dict:''')
r('''    reglages_carbon = controler_pire_cas_carbon(decl, fixe, liste, pieces)  # v8 : chaque appel peut partir, pire cas écrit''',
  '''    reglages_carbon = controler_pire_cas_carbon(decl, fixe, liste, pieces)  # v8 : chaque appel peut partir, pire cas écrit
    reglages_argon = controler_pire_cas_argon(decl, fixe, liste, pieces)  # v11 : Argon sous la garde Google''')
r('''        "argon_v11": argon_v11,''', '''        "argon_v11": argon_v11, "reglages_argon_v11_flux": reglages_argon,''')
# essai à blanc : Argon par la commande en flux
r('''        "argon": {"type": "commande_externe", "commande": ["bash", str(r.depot / PIECES["enveloppe_argon"][0])],
                  "nom_cle": "CLE_FACTICE_ARGON", "porte_plafond": {"type": "environnement"}}}}''',
  '''        "argon": {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(cmd["carbon"])] + ARGUMENTS_COMMANDES["argon"],
                  "nom_cle": "CLE_FACTICE_ARGON", "porte_plafond": {"type": "environnement"}}}}''')
