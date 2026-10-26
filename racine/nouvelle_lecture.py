# ------------------------------------------------------------------ lecture des courses ----
def _dossier_generation(course: str | pathlib.Path, lignee: str, generation: int, phase: str | None = None) -> pathlib.Path:
    return pathlib.Path(course) / "archive" / lignee / f"{'c' if phase else 'g'}{generation:03d}"


def _lire_jsonl(f: pathlib.Path) -> list[dict]:
    if not f.is_file():
        return []
    return [json.loads(x) for x in f.read_text(encoding="utf-8").splitlines() if x.strip()]


def _lire_json(f: pathlib.Path) -> dict:
    if not f.is_file():
        return {}
    o = json.loads(f.read_text(encoding="utf-8"))
    return o if isinstance(o, dict) else {}


def reponses_finales(course: str | pathlib.Path, lignee: str, generation: int, banque: dict) -> dict[str, str | None]:
    """Réponses d'une génération sur le test final, **celles que le juge a retenues** (RV-01) : lues dans
    `archive/<lignée>/gNNN/juge/reponses-lues.json`, que le noyau écrit et scelle à chaque dépôt d'une génération notée
    (`{}` quand l'organisme n'a rien écrit, a planté, a dépassé son délai, ou a écrit un lien, un tube ou un fichier
    illisible ; la marque d'ordre d'octets et la borne de taille sont celles du juge). Une seule règle de lecture, celle du
    juge : une étiquette hors de la famille vaut « sans réponse ». Ce fichier absent pour une génération notée est une
    anomalie du noyau : erreur, jamais un repli (CE3-02)."""
    f = _dossier_generation(course, lignee, generation) / "juge" / "reponses-lues.json"
    if not f.is_file():
        raise FileNotFoundError(f"réponses retenues par le juge absentes pour une génération notée : {f}")
    brut = json.loads(f.read_text(encoding="utf-8"))
    lues = brut.get("reponses") if isinstance(brut, dict) else None
    if not isinstance(lues, dict):
        raise ValueError(f"{f} : objet {{\"reponses\": …}} attendu")
    sortie: dict[str, str | None] = {}
    for t in banque["test_final"]:
        e = lues.get(t["id"])
        e = e.strip().lower() if isinstance(e, str) else ""
        sortie[t["id"]] = e if e in _taches.ETIQUETTES[t["famille"]] else None
    return sortie


def generations_valides(course: str | pathlib.Path, lignee: str) -> list[int]:
    """Générations notées d'une lignée que le noyau n'a pas invalidées. Les rondes de la phase de conception (`cNNN`) sont
    écartées : l'index les inscrit avec `phase` et leur numéro de ronde (1 à R) dans `generation`, qui n'est pas une
    génération notée (constat de « session-depot » après CR3-02 de la contre-lecture n° 3 de la confrontation)."""
    lignes = _lire_jsonl(pathlib.Path(course) / "archive" / "index.jsonl")
    # générations notées seulement : ni rondes de conception (`phase`), ni rondes importées d'une course d'origine, ni invalidées
    return sorted(l["generation"] for l in lignes if l["lignee"] == lignee and not l.get("invalide") and not l.get("phase") and not l.get("importee"))


def rondes_conception(course: str | pathlib.Path, lignee: str) -> list[int]:
    """Rondes de conception d'une lignée archivées dans la course (dans le bras B, ce sont les rondes importées de A)."""
    lignes = _lire_jsonl(pathlib.Path(course) / "archive" / "index.jsonl")
    return sorted(l["generation"] for l in lignes if l["lignee"] == lignee and l.get("phase"))


def couverture_par_famille(reponses: dict[str, str | None], taches: list[dict]) -> dict[str, float]:
    """Part des tâches de chaque famille qui ont une réponse valide (CE3-03)."""
    sortie = {}
    for f in sorted({t["famille"] for t in taches}):
        ids = [t["id"] for t in taches if t["famille"] == f]
        sortie[f] = sum(1 for i in ids if reponses.get(i) is not None) / len(ids) if ids else 0.0
    return sortie


def exactitude_repondue_par_famille(reponses: dict[str, str | None], taches: list[dict]) -> dict[str, float | None]:
    """(sensibilité + spécificité) / 2 par famille sur les seules tâches répondues (CE3-03 : le seuil bas de l'audit
    vise des étiquettes inversées, pas une absence de réponse) ; None si une vérité de la famille n'a aucune réponse."""
    sortie: dict[str, float | None] = {}
    for f in sorted({t["famille"] for t in taches}):
        fam = [t for t in taches if t["famille"] == f and reponses.get(t["id"]) is not None]
        pos = {t["etiquettes"][0] for t in fam}
        if not fam or len({t["verite"] for t in fam}) < 2 or len(pos) != 1:
            sortie[f] = None
            continue
        sortie[f] = exactitude_equilibree(reponses, fam)
    return sortie


def exactitude_par_famille(reponses: dict[str, str | None], taches: list[dict]) -> dict[str, float]:
    """(sensibilité + spécificité) / 2 pour chaque famille, règle du juge (sans réponse = erreur)."""
    return {f: exactitude_equilibree(reponses, [t for t in taches if t["famille"] == f]) for f in sorted({t["famille"] for t in taches})}


# ---------------------------------------------------------------- pannes extérieures (CE3-05, CE4-01, RV-11) ----
_CODES_EXTERIEURS = {401, 402, 403, 408, 409, 429}
_MOTIF_HTTP = re.compile(r"HTTP(?: Error)? (\d{3})\b")
_MOTIF_RESEAU = re.compile(r"connexion|timed out|timeout|URLError|ConnectionError|ConnectionReset|ConnectionRefused|ConnectionAborted|"
                           r"RemoteDisconnected|IncompleteRead|SSLError|gaierror|name resolution|APIConnectionError|APITimeoutError|"
                           r"GEMINI_API_KEY absente|paquet anthropic absent", re.IGNORECASE)


def echec_exterieur(echec) -> bool:
    """RV-11 : un échec dû au fournisseur ou au réseau, pas à la requête de l'organisme. Avec un code HTTP, le code seul
    décide : 401, 402, 403, 408, 409, 429 et 5xx sont extérieurs ; 400, 404, 413, 422… (requête refusée telle qu'écrite)
    ne le sont pas. Sans code : connexion, délai, résolution de nom, certificat, clé absente sont extérieurs ; le reste
    (analyse d'une réponse, exception inattendue) ne l'est pas — compté à part, rapporté."""
    s = str(echec or "")
    m = _MOTIF_HTTP.search(s)
    if m:
        code = int(m.group(1))
        return code in _CODES_EXTERIEURS or 500 <= code <= 599
    return bool(_MOTIF_RESEAU.search(s))


def taux_pannes(course: str | pathlib.Path, lignee: str, generations) -> dict:
    """Échecs extérieurs d'une lignée, **cumulés sur les générations données** (CE4-01 : les générations notées communes
    aux deux bras jusqu'à la génération lue), lus dans leurs journaux archivés — appels aux modèles (sur tous les appels)
    et recherches (sur les recherches servies, par source ; les refus du noyau ne sont pas des tentatives). Rend
    {"appels": [échecs extérieurs, tentatives], "recherches": {source: [échecs extérieurs, tentatives]},
    "autres_echecs": {"appels": n, "recherches": n}} (échecs non extérieurs, rapportés)."""
    gens = [generations] if isinstance(generations, int) else list(generations)
    sortie = {"appels": [0, 0], "recherches": {}, "autres_echecs": {"appels": 0, "recherches": 0}}
    for g in gens:
        d = _dossier_generation(course, lignee, g)
        for l in _lire_jsonl(d / "journal-appels.jsonl"):
            sortie["appels"][1] += 1
            if l.get("statut") == "ECHEC_API":
                if echec_exterieur(l.get("echec")):
                    sortie["appels"][0] += 1
                else:
                    sortie["autres_echecs"]["appels"] += 1
        for l in _lire_jsonl(d / "travail" / "noyau" / "journal-recherches.jsonl"):
            if l.get("statut") not in ("OK", "ECHEC_RECHERCHE"):
                continue
            s = sortie["recherches"].setdefault(str(l.get("source")), [0, 0])
            s[1] += 1
            if l.get("statut") == "ECHEC_RECHERCHE":
                if echec_exterieur(l.get("echec")):
                    s[0] += 1
                else:
                    sortie["autres_echecs"]["recherches"] += 1
    return sortie


def regle_pannes(avec: dict, sans: dict) -> dict:
    """Règle gelée de la panne extérieure (CE3-05 corrigée par CE4-01). Les appels, puis chaque source servie dans les deux
    bras, sont comparés **seulement si chaque bras y a au moins `EFFECTIF_PANNE_MIN` tentatives** ; la paire est coupée si,
    sur l'un d'eux, l'écart des taux d'échec extérieur dépasse `ECART_PANNE_MAX` **et** les nombres d'échecs extérieurs
    diffèrent d'au moins `ECHECS_ECART_MIN`. Rend {"coupe", "porteur", "ecart_max", "comparees"} (ce qui a été comparé ou
    non, et pourquoi)."""
    candidats = [("appels", avec["appels"], sans["appels"])]
    for src in sorted(set(avec["recherches"]) | set(sans["recherches"])):
        candidats.append((f"recherches {src}", avec["recherches"].get(src, [0, 0]), sans["recherches"].get(src, [0, 0])))
    comparees, coupe, porteur, ecart_max = [], False, "", 0.0
    for nom, (ea, na), (eb, nb) in candidats:
        ligne = {"quoi": nom, "avec": [ea, na], "sans": [eb, nb]}
        if na < EFFECTIF_PANNE_MIN or nb < EFFECTIF_PANNE_MIN:
            comparees.append(dict(ligne, compare=False, raison=f"moins de {EFFECTIF_PANNE_MIN} tentatives dans un bras"))
            continue
        ecart = abs(ea / na - eb / nb)
        franchi = ecart > ECART_PANNE_MAX and abs(ea - eb) >= ECHECS_ECART_MIN
        comparees.append(dict(ligne, compare=True, ecart=round(ecart, 4), coupe=franchi))
        ecart_max = max(ecart_max, ecart)
        if franchi and not coupe:
            coupe, porteur = True, f"{nom} : {ea}/{na} contre {eb}/{nb}"
    return {"coupe": coupe, "porteur": porteur, "ecart_max": round(ecart_max, 4), "comparees": comparees}


def coupure_sous_taux_identiques(n: int, p: float, n_sources: int = 1) -> float:
    """Probabilité exacte (loi binomiale) qu'une paire soit coupée par `regle_pannes` quand les deux bras ont le **même**
    taux d'échec extérieur `p`, `n` tentatives chacun, sur `n_sources` sources indépendantes de mêmes effectifs
    (descriptif, CE4-01 : le taux de coupure à tort de la règle)."""
    if n < EFFECTIF_PANNE_MIN:
        return 0.0
    loi = [math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]
    une = sum(loi[i] * loi[j] for i in range(n + 1) for j in range(n + 1)
              if abs(i - j) >= ECHECS_ECART_MIN and abs(i - j) / n > ECART_PANNE_MAX)
    return 1 - (1 - une) ** n_sources


# ------------------------------------------------------------------- fuites (CE3-04, RV-07, CE4-10 c) ----
def recoupements_fuite(course: str | pathlib.Path, lignee: str, generations: list[int], conception: bool = True) -> int:
    """CE3-04 (mesure) : recoupements refusés ou retirés — requêtes refusées (`REFUSE_FUITE`), notices retirées des
    résultats (`n_retires_fuite`, RV-07 i), documents en quarantaine — dans les générations notées données et, si
    `conception`, dans les rondes de conception de la lignée archivées dans la course (CE4-10 c : dans le bras B, ce sont
    celles de A, importées)."""
    dossiers = [_dossier_generation(course, lignee, g) for g in generations]
    if conception:
        dossiers += [_dossier_generation(course, lignee, k, "conception") for k in rondes_conception(course, lignee)]
    n = 0
    for d in dossiers:
        for l in _lire_jsonl(d / "travail" / "noyau" / "journal-recherches.jsonl"):
            n += int(l.get("statut") == "REFUSE_FUITE") + int(l.get("n_retires_fuite") or 0)
        n += sum(1 for l in _lire_jsonl(d / "travail" / "corpus" / "index.jsonl") if l.get("statut") == "REFUSE_FUITE")
    return n


def recoupements_courts(course: str | pathlib.Path, lignee: str, generations: list[int]) -> int:
    """RV-07 (ii) : recoupements courts (fenêtres de `garde_fuite.MOTS_COURTS` mots), comptés sans refus par le noyau dans
    ses journaux (requêtes, notices gardées, documents rendus). Descriptif : rapporté, jamais un déclencheur (des fenêtres
    de cinq mots se partagent par simple tournure commune)."""
    n = 0
    for g in generations:
        d = _dossier_generation(course, lignee, g) / "travail" / "noyau"
        n += sum(int(l.get("recoupements_courts") or 0) for l in _lire_jsonl(d / "journal-recherches.jsonl"))
        n += sum(int(l.get("recoupements_courts") or 0) for l in _lire_jsonl(d / "journal-fuite.jsonl"))
    return n


def causes_absences(course: str | pathlib.Path, lignee: str, generation: int) -> dict:
    """CE4-02 (2), descriptif : ce qui peut expliquer des absences de réponse à une génération — statut d'exécution,
    refus du noyau par raison (`appels_max`, `plafond_usd`, `arret_noyau`), demandes d'un service non servi
    (`INDISPONIBLE`, par opération), nombre de réponses retenues, appels, coût ; problème de lecture des réponses."""
    d = _dossier_generation(course, lignee, generation)
    r = _lire_json(d / "resume.json")
    lues = _lire_json(d / "juge" / "reponses-lues.json")
    refus: dict[str, int] = {}
    for x in r.get("refus_noyau") or []:
        refus[str(x.get("raison"))] = refus.get(str(x.get("raison")), 0) + 1
    return {"statut": r.get("statut"), "refus_noyau": refus, "indisponibles": r.get("indisponibles") or {},
            "n_reponses_test": r.get("n_reponses_test"), "n_appels": r.get("n_appels"), "cout_usd": r.get("cout_usd"),
            "probleme_reponses": lues.get("probleme_reponses"), "relance": r.get("relance")}


def _delta_sur_repondues(avec: dict, sans: dict, taches: list[dict]) -> float | None:
    """Δ secondaire (CE4-02 (2)) : exactitude équilibrée moyenne des familles sur les seules tâches répondues par les deux
    bras ; None si une famille n'a plus ses deux vérités. Descriptif, sans seuil ni verdict."""
    communes = [t for t in taches if avec.get(t["id"]) is not None and sans.get(t["id"]) is not None]
    fams = sorted({t["famille"] for t in taches})
    vals = []
    for f in fams:
        sous = [t for t in communes if t["famille"] == f]
        if len({t["verite"] for t in sous}) < 2:
            return None
        vals.append(exactitude_equilibree(avec, sous) - exactitude_equilibree(sans, sous))
    return round(float(np.mean(vals)), 4) if vals else None


def paires_h_g1(couples: list[tuple[str, str]], lignees: list[str], generations: int,
                exclues=()) -> tuple[list[dict], list[dict], dict]:
    """`couples` : [(course à gradient A_r, course jumelle B_r)] ; `lignees` : lignées auto-écrites (contrat à
    l'amorçage) ; `exclues` (CE4-10 a) : noms de paires (« lignée@rN ») qu'un audit de symétrie scellé a trouvées touchées
    par un défaut. Rend (paires, tâches du test final, état). Une paire est « coupée » (raison consignée) : exclue par
    l'audit ; sans génération valide commune ; sous la couverture minimale dans un bras ; sur panne extérieure
    (`regle_pannes`). Plus d'un quart coupé → invalide. `etat["descriptif"]` porte, pour chaque paire lue ou coupée, le
    rapport descriptif gelé (CE4-02 (2), CE4-10 e)."""
    exclues = set(exclues)
    paires, coupees, descriptif, taches_final = [], [], {}, None
    for r, (a, b) in enumerate(couples):
        banque_a = json.loads((pathlib.Path(a) / "banque.json").read_text(encoding="utf-8"))
        banque_b = json.loads((pathlib.Path(b) / "banque.json").read_text(encoding="utf-8"))
        if banque_a != banque_b:
            raise ValueError(f"réplique {r} : banques différentes entre {a} et {b}")
        if taches_final is None:  # étiquettes de la famille ajoutées si la banque ne les porte pas (banques de simulation)
            taches_final = [dict(t, etiquettes=list(t.get("etiquettes") or _taches.ETIQUETTES[t["famille"]])) for t in banque_a["test_final"]]
        for lignee in lignees:
            nom = f"{lignee}@r{r}"
            communes = sorted(set(generations_valides(a, lignee)) & set(generations_valides(b, lignee)))
            communes = [g for g in communes if g <= generations - 1]
            recoup = {"avec": recoupements_fuite(a, lignee, communes), "sans": recoupements_fuite(b, lignee, communes)}
            if not communes:
                coupees.append({"paire": nom, "raison": "aucune génération valide commune"})
                descriptif[nom] = {"coupee": coupees[-1]["raison"], "recoupements_fuite": recoup}
                continue
            g = communes[-1]
            avec, sans = reponses_finales(a, lignee, g, banque_a), reponses_finales(b, lignee, g, banque_b)
            couv = {"avec": couverture_par_famille(avec, taches_final), "sans": couverture_par_famille(sans, taches_final)}
            pannes = {"avec": taux_pannes(a, lignee, communes), "sans": taux_pannes(b, lignee, communes)}
            regle = regle_pannes(pannes["avec"], pannes["sans"])
            descriptif[nom] = {
                "replique": r, "generation": g, "generations_communes": communes, "couverture": couv,
                "exactitude": {"avec": exactitude_par_famille(avec, taches_final), "sans": exactitude_par_famille(sans, taches_final)},
                "exactitude_repondue": {"avec": exactitude_repondue_par_famille(avec, taches_final),
                                        "sans": exactitude_repondue_par_famille(sans, taches_final)},
                "delta_par_famille": {f: round(exactitude_equilibree(avec, [t for t in taches_final if t["famille"] == f])
                                               - exactitude_equilibree(sans, [t for t in taches_final if t["famille"] == f]), 4)
                                      for f in sorted({t["famille"] for t in taches_final})},
                "delta_sur_repondues_par_les_deux": _delta_sur_repondues(avec, sans, taches_final),
                "causes_absences": {"avec": causes_absences(a, lignee, g), "sans": causes_absences(b, lignee, g)},
                "pannes": pannes, "regle_pannes": regle, "recoupements_fuite": recoup,
                "recoupements_courts": {"avec": recoupements_courts(a, lignee, communes), "sans": recoupements_courts(b, lignee, communes)},
            }
            basse = [f"{bras} {fam} {c:.2f}" for bras, fams in couv.items() for fam, c in fams.items() if c < COUVERTURE_MIN]
            if nom in exclues:
                raison = "défaut touchant la paire, trouvé par l'audit de symétrie scellé (R4)"
            elif basse:
                raison = f"couverture < {COUVERTURE_MIN:.0%} : " + ", ".join(basse)
            elif regle["coupe"]:
                raison = f"panne extérieure ({regle['porteur']})"
            else:
                raison = None
            if raison:
                coupees.append({"paire": nom, "raison": raison})
                descriptif[nom]["coupee"] = raison
                continue
            paires.append({"paire": nom, "replique": r, "generation": g, "avec": avec, "sans": sans,
                           "couverture": couv, "ecart_pannes": regle["ecart_max"], "recoupements_fuite": recoup})
    inconnues = exclues - {f"{l}@r{r}" for r in range(len(couples)) for l in lignees}
    if inconnues:
        raise ValueError(f"paires exclues inconnues : {sorted(inconnues)}")
    n_total = len(couples) * len(lignees)
    etat = {"n_paires_prevues": n_total, "coupees": coupees, "exclues": sorted(exclues), "descriptif": descriptif,
            "invalide": bool(n_total) and len(coupees) / n_total > PART_INVALIDE_MAX}
    return paires, (taches_final or []), etat
