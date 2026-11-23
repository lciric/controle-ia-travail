# GO-2026-11-22-124 (mots de Lazar) : règle de LUC simplifiée — plus de plancher, plus de couverture, plus de lecture du solde ;
# restent : plafond propre de la part Claude (45 USD, configuration), plafond de la course (150), arrêt propre au premier refus de
# l'interface (crédit ou plafond), code 7, alerte scellée, sans relance.
_a = src.index("        if nom == CLE_CLAUDE:\n            if not isinstance(x, dict):")
_b = src.index("        if not isinstance(x, dict):\n            raise Refus(f\"relevé des crédits : clé {nom} ({fournisseur}) absente")
src = src[:_a] + '''        if nom == CLE_CLAUDE:  # v11 (GO-2026-11-22-124) : solde non lu, aucune condition de départ sur la clé Claude
            sortie[nom] = {"fournisseur": fournisseur, "relais": fours, "parts_par_relais": dict(zip(fours, parts_k)),
                           "lisible": False, "condition_de_depart": None, "ligne_du_releve": x if isinstance(x, dict) else None,
                           "part_au_pire_usd": part, "plafond_part_claude_usd": PLAFOND_PART_CLAUDE_USD,
                           "regle": "GO-2026-11-22-124 : solde non lu (recharge automatique) ; plafond propre de la part Claude "
                                    f"{PLAFOND_PART_CLAUDE_USD} USD (relais Claude lancé à ce plafond) ; arrêt propre au premier "
                                    "refus de l'interface ou du relais (code 7)"}
            continue
''' + src[_b:]
r('''PART_DE_LA_COUVERTURE = 0.8      # brouillon 1 du préenregistrement v11 : quatre cinquièmes de la couverture nette\n''', '')
r('''    if not _nombre(part) or float(part) != PART_DE_LA_COUVERTURE or not 0 < PART_DE_LA_COUVERTURE <= 1:
        raise Refus(f"part de la couverture de {CLE_CLAUDE} : configuration {part!r}, lanceur {PART_DE_LA_COUVERTURE!r} ; 0,8 exigé "
                    "aux deux : une part retirée ou relevée ne part pas")
''', '''    if part is not None:  # GO-2026-11-22-124 : plus de part de la couverture ; sa présence est un reste d'une règle retirée
        raise Refus("configuration : changements_v11.part_de_la_couverture présent alors que GO-2026-11-22-124 l'a retiré")
''')
# GO-124 lu ; GO-107 prolongé par lui
r('''def verifier_plafond_luc(fixe: dict) -> float:''', '''GO_SIMPLIFICATION_CLE = "GO-2026-11-22-124"


def verifier_go_simplification(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_SIMPLIFICATION_CLE) -> dict:
    """v11 : la ligne GO-2026-11-22-124 (mots de Lazar) : une ligne, accordée par Lazar, en période, non révoquée, qui nomme
    GO-2026-11-22-107 (prolongée) ; rend son échéance (prolongation de l'exception de clé)."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\\|\\s*(GO-\\d{4}-\\d{2}-\\d{2}-\\d{2,3})\\s*\\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    if len(trouvees) != 1 or len(trouvees[0]) != 8:
        raise Refus(f"{go_id} : {len(trouvees)} ligne(s) (une ligne de 8 colonnes exigée) : règle de la clé Claude non trouvée")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = trouvees[0]
    if par != "Lazar" or typ not in ("calcul", "décision"):
        raise Refus(f"{go_id} : type {typ!r} accordé par {par!r} (Lazar exigé)")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    if GO_EXCEPTION_CLE not in perimetre or "45" not in plafond + perimetre:
        raise Refus(f"{go_id} : le périmètre doit nommer {GO_EXCEPTION_CLE} (prolongée) et le plafond de la part Claude (45 USD)")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(trouvees[0])).encode("utf-8")).hexdigest()}


def verifier_plafond_luc(fixe: dict) -> float:''')
r('''def verifier_go_exception_cle(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_EXCEPTION_CLE) -> dict:''',
  '''def verifier_go_exception_cle(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_EXCEPTION_CLE,
                              prolongation: str | None = None) -> dict:''')
r('''    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if CLE_CLAUDE not in perimetre''', '''    fin = max(d_ech, _dt.date.fromisoformat(prolongation)) if prolongation else d_ech  # v11 : prolongée par GO-2026-11-22-124
    if not d_acc <= aujourd_hui <= fin:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {fin}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if CLE_CLAUDE not in perimetre''')
r('''    go_cle = verifier_go_exception_cle(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé)"}''',
  '''    go_simpl = verifier_go_simplification(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé)"}
    go_cle = verifier_go_exception_cle(r.registre_go, aujourd_hui, prolongation=go_simpl["echeance"]) if (reel and r.verifier_go) \\
        else {"go": "sans objet (moteur simulé)"}''')
r('''"go_exception_cle": go_cle,''', '''"go_exception_cle": go_cle, "go_simplification_cle": go_simpl,''')
r('''    parts["claude"] = dict(parts.get("claude") or {}, plafond_relais_exige_usd=credits[CLE_CLAUDE]["plafond_part_claude_usd"])''',
  '''    parts["claude"] = dict(parts.get("claude") or {}, plafond_relais_exige_usd=plafond_luc)  # GO-124 : 45 USD exactement''')
r('''        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"],
                                             float(credits[CLE_CLAUDE]["plafond_part_claude_usd"]))''',
  '''        journal_claude = ((procedure.get("relais_vivants") or {}).get("claude") or {}).get("journal")
        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"], plafond_luc, journal_claude)''')
r('''        couverture = (credits.get(CLE_CLAUDE) or {}).get("couverture_usd")
        if not _nombre(couverture):
            raise Refus(f"couverture de {CLE_CLAUDE} inconnue : la part Claude ne peut pas être comptée au fil de l'eau")
''', '')
r('''                       "couverture_usd": (credits.get(CLE_CLAUDE) or {}).get("couverture_usd"), "plafond_propre_usd": plafond_luc,''',
  '''                       "regle": "GO-2026-11-22-124", "plafond_propre_usd": plafond_luc,''')
r('''                       "plafond_part_claude_usd": (credits.get(CLE_CLAUDE) or {}).get("plafond_part_claude_usd")},''',
  '''                       "plafond_part_claude_usd": plafond_luc},''')
r('''    if arret_luc == 5:  # v11 : arrêt propre sur la part Claude (premier 402 du relais Claude, plafond, illisible)
        return 5''', '''    if arret_luc == 7:  # v11 (GO-2026-11-22-124) : arrêt propre au premier refus de l'interface ou du relais Claude
        return 7''')
r('''                            "5 (v11)": "ou arrêt propre sur la part Claude : premier refus (402) du relais Claude, plafond de la "
                                       "part atteint, état illisible (alerte-arret-part-claude.json)"},''',
  '''                            "7": "arrêt propre sur la part Claude : premier refus de l'interface (crédit) ou du relais (402, "
                                 "plafond de 45 USD), part engagée au plafond, état ou journal illisible (alerte-arret-part-claude.json)"},''')
# relais Claude : journal exigé (refus de l'interface lus au journal, jamais le texte)
r('''    out = {"pid": pid, "programme": progs[0], "programme_sha256": attendu, "variable_cle": variable, "port": port,
           "modeles": modeles_args}''', '''    out = {"pid": pid, "programme": progs[0], "programme_sha256": attendu, "variable_cle": variable, "port": port,
           "modeles": modeles_args}
    if nom == "claude":  # v11 (GO-2026-11-22-124) : le journal du relais dit chaque statut de l'interface (jamais le texte)
        journal = _valeur_arg(args, "--journal")
        if not journal or not os.path.isabs(journal):
            raise Refus("relais claude : --journal (chemin absolu) exigé : l'arrêt au premier refus de l'interface le lit")
        out["journal"] = journal''')
