# Exigences du préenregistrement (message de la mère) : (1) arrêt au premier 4xx de l'interface autre que 429, code 5 ;
# (2) prolongations lues : GO-2026-11-22-80 pour GO-2026-11-18-14 ; GO-2026-11-22-124 pour GO-2026-11-22-107 seulement si la
# ligne de confirmation de Lazar est inscrite et nommée dans la configuration.
# --- (1) code 5, statuts 4xx sauf 429 ------------------------------------------------------------------------------------------
r('''STATUTS_REFUS_INTERFACE = (400, 401, 402, 403)  # v11 : refus de l'interface (crédit, clé) ou du relais (402, plafond)''',
  '''STATUT_NON_REFUS = 429  # v11 : tout statut 4xx de l'interface autre que 429 (limite de débit) est un refus (crédit : 400, R-4833)


def est_refus_interface(statut) -> bool:
    return isinstance(statut, int) and not isinstance(statut, bool) and 400 <= statut < 500 and statut != STATUT_NON_REFUS''')
r('''            if o.get("statut") in STATUTS_REFUS_INTERFACE:
                return o.get("statut"), o.get("motif") or o.get("chemin")''',
  '''            if est_refus_interface(o.get("statut")):
                return o.get("statut"), None''')
src = src.replace('''return {"code": 7, ''', '''return {"code": 5, ''')
r('''            return {"code": 5, "motif": f"premier refus de l'interface lu au journal du relais Claude (statut {interface[0]}, "
                                        f"{str(interface[1])[:120]}) ; part engagée {self.derniere} USD"}''',
  '''            return {"code": 5, "motif": f"premier refus de l'interface lu au journal du relais Claude : statut {interface[0]} ; "
                                        f"part engagée {self.derniere} USD"}''')
src = src.replace('`depasse()` rend {code: 7, motif}', '`depasse()` rend {code: 5, motif}')
src = src.replace('(400, 401, 402, 403 : crédit insuffisant, clé, plafond)', '(tout 4xx autre que 429 : crédit insuffisant, clé, plafond)')
r('''    if arret_luc == 7:  # v11 (GO-2026-11-22-124) : arrêt propre au premier refus de l'interface ou du relais Claude
        return 7''', '''    if arret_luc == 5:  # v11 : arrêt propre au premier refus de l'interface (4xx sauf 429) ou du relais Claude (402)
        return 5''')
r('''                            "7": "arrêt propre sur la part Claude : premier refus de l'interface (crédit) ou du relais (402, "
                                 "plafond de 45 USD), part engagée au plafond, état ou journal illisible (alerte-arret-part-claude.json)"},''',
  '''                            "5 (v11)": "ou arrêt propre sur la part Claude : premier refus de l'interface (4xx sauf 429) ou du "
                                       "relais (402, plafond de 45 USD), part engagée au plafond, état ou journal illisible "
                                       "(alerte-arret-part-claude.json)"},''')
r('''Codes : 0, 2, 3, 4, 5, 6 comme la v10 ; **7** : arrêt propre sur la part Claude (premier refus de l'interface ou du relais
Claude, plafond de 45 USD atteint, état ou journal illisible), sans relance.''',
  '''Codes : 0, 2, 3, 4, 6 comme la v10 ; **5** : arrêt par la garde de crédit d'un relais dispensé (v10) **ou** arrêt propre sur la
part Claude (premier 4xx de l'interface autre que 429 au journal du relais Claude, 402 du relais à 45 USD, part engagée au
plafond, état ou journal illisible), sans relance ; l'alerte scellée dit le statut, pas la cause.''')
r('''   les `intervalle_surveillance_s` secondes ; au **premier refus de l'interface** (statut 400, 401, 402 ou 403 au journal :
   crédit insuffisant, clé, plafond), au premier refus du relais (état `refus` > 0, 402), à une part engagée (dépense +
   montants réservés des appels en vol) qui atteint 45 USD, ou à un état ou un journal illisible trois fois de suite : arrêt
   propre de l'orchestrateur par son PID, alerte scellée `alerte-arret-part-claude.json`, **code 7**, sans relance ; le plafond
   d'arrêt de 150 USD ne change pas ;''',
  '''   les `intervalle_surveillance_s` secondes ; au **premier refus de l'interface** (tout statut 4xx autre que 429 au journal :
   un refus faute de crédit est un 400, R-4833), au premier refus du relais (état `refus` > 0, son 402 à 45 USD), à une part
   engagée (dépense + montants réservés des appels en vol) qui atteint 45 USD, ou à un état ou un journal illisible trois fois
   de suite : arrêt propre de l'orchestrateur par son PID, alerte scellée `alerte-arret-part-claude.json` (le statut, pas la
   cause), **code 5**, sans relance ; le plafond d'arrêt de 150 USD ne change pas ;''')
r('''                                    "refus de l'interface ou du relais (code 7)"}''', '''                                    "refus de l'interface ou du relais (code 5)"}''')
# --- (2) prolongations ----------------------------------------------------------------------------------------------------------
r('''    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if "mentors" not in p and "affinage" not in p:''', '''    fin = max(d_ech, _dt.date.fromisoformat(prolongation)) if prolongation else d_ech  # v11 : prolongée par GO-2026-11-22-80
    if not d_acc <= aujourd_hui <= fin:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {fin}, aujourd'hui {aujourd_hui}) ; prolongation "
                    f"valide : {prolongation or 'aucune'}")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if "mentors" not in p and "affinage" not in p:''')
r('''def verifier_go(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_ID) -> dict:''',
  '''def verifier_go(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_ID, prolongation: str | None = None) -> dict:''')
r('''def verifier_plafond_luc(fixe: dict) -> float:''', '''GO_PROLONGATION_COURSE = "GO-2026-11-22-80"   # prolonge GO-2026-11-18-14 au 15 décembre


def lire_ligne_go(registre: Path, go_id: str) -> tuple:
    """(cellules de la ligne unique de `go_id` ou None, révocations qui la visent)."""
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
    return (trouvees[0] if len(trouvees) == 1 and len(trouvees[0]) == 8 else None), revocations


def lire_prolongation(registre: Path, aujourd_hui: _dt.date, go_id: str, go_vise: str, mot: str = "prolong") -> dict:
    """Une ligne de prolongation : accordée par Lazar, non révoquée, en période, qui nomme le GO visé et dit « prolong… ».
    Rend {valide, echeance, motif} ; une ligne absente ou invalide n'est jamais tue : le motif est écrit au manifeste, et le GO
    visé garde sa propre échéance (au-delà, refus)."""
    c, rev = lire_ligne_go(registre, go_id) if registre.is_file() else (None, [])
    if c is None:
        return {"id": go_id, "valide": False, "motif": "ligne absente ou mal formée"}
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = c
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        return {"id": go_id, "valide": False, "motif": "dates illisibles"}
    motifs = []
    if par != "Lazar":
        motifs.append(f"accordée par {par!r}")
    if rev:
        motifs.append(f"révoquée par {', '.join(sorted(rev))}")
    if go_vise not in perimetre or mot not in _normaliser(perimetre):
        motifs.append(f"ne dit pas prolonger {go_vise}")
    if not d_acc <= aujourd_hui <= d_ech:
        motifs.append(f"hors période ({d_acc} → {d_ech})")
    if motifs:
        return {"id": go_id, "valide": False, "motif": " ; ".join(motifs)}
    return {"id": ident, "valide": True, "echeance": echeance, "go_vise": go_vise,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def verifier_confirmation_107(registre: Path, aujourd_hui: _dt.date, fixe: dict) -> dict:
    """GO-2026-11-22-124 dit la prolongation de GO-2026-11-22-107 « à confirmer par Lazar » : elle ne vaut que si la ligne de
    confirmation est **nommée** dans la configuration (`changements_v11.confirmation_prolongation_go_107`) et **inscrite** au
    registre (Lazar, non révoquée, en période, qui nomme GO-2026-11-22-107). Non nommée : aucune prolongation (au-delà du
    25 novembre, refus). Nommée mais absente ou invalide : refus."""
    nom = (fixe.get("changements_v11") or {}).get("confirmation_prolongation_go_107", "absente")
    if nom == "absente":
        raise Refus("configuration : emplacement changements_v11.confirmation_prolongation_go_107 absent (null s'il n'y a pas "
                    "de confirmation)")
    if nom is None:
        return {"nommee": None, "valide": False, "motif": "aucune confirmation nommée dans la configuration"}
    if not isinstance(nom, str) or not re.fullmatch(r"GO-\\d{4}-\\d{2}-\\d{2}-\\d{2,3}", nom):
        raise Refus(f"configuration : confirmation_prolongation_go_107 = {nom!r} : identifiant de GO exigé")
    o = lire_prolongation(registre, aujourd_hui, nom, GO_EXCEPTION_CLE, mot="")
    if not o["valide"]:
        raise Refus(f"confirmation de la prolongation de {GO_EXCEPTION_CLE} nommée ({nom}) mais non valide au registre : {o['motif']}")
    return dict(o, nommee=nom)


def verifier_les_go(registre: Path, aujourd_hui: _dt.date, fixe: dict) -> dict:
    """v11 : GO de la course (GO-2026-11-18-14, prolongé par GO-2026-11-22-80 s'il est valide), règle de la clé
    (GO-2026-11-22-124), exception de clé (GO-2026-11-22-107, prolongée à l'échéance de GO-124 seulement sous confirmation)."""
    p80 = lire_prolongation(registre, aujourd_hui, GO_PROLONGATION_COURSE, GO_ID)
    go = verifier_go(registre, aujourd_hui, prolongation=p80.get("echeance") if p80["valide"] else None)
    simpl = verifier_go_simplification(registre, aujourd_hui)
    conf = verifier_confirmation_107(registre, aujourd_hui, fixe)
    cle = verifier_go_exception_cle(registre, aujourd_hui, prolongation=simpl["echeance"] if conf["valide"] else None)
    return {"go": go, "prolongation_course": p80, "simplification": simpl, "confirmation_107": conf, "exception_cle": cle}


def verifier_plafond_luc(fixe: dict) -> float:''')
r('''    go = verifier_go(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé, aucune dépense)"}
    go_simpl = verifier_go_simplification(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé)"}
    go_cle = verifier_go_exception_cle(r.registre_go, aujourd_hui, prolongation=go_simpl["echeance"]) if (reel and r.verifier_go) \\
        else {"go": "sans objet (moteur simulé)"}''',
  '''    go = go_simpl = go_cle = {"go": "sans objet (moteur simulé, aucune dépense)"}  # v11 : lus après la configuration''')
r('''    argon_v11 = appliquer_emplacement_argon(fixe)  # v11 : plafond de session des juges, en attente du mot de la mère''',
  '''    argon_v11 = appliquer_emplacement_argon(fixe)  # v11 : plafond de session des juges (devis v11)
    if reel and r.verifier_go:  # v11 : prolongations (GO-80, GO-124 sous confirmation) ; la confirmation est nommée en configuration
        les_go = verifier_les_go(r.registre_go, aujourd_hui, fixe)
        go, go_simpl, go_cle = dict(les_go["go"], prolongation=les_go["prolongation_course"]), les_go["simplification"], \\
            dict(les_go["exception_cle"], confirmation=les_go["confirmation_107"])''')
