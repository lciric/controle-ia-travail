JOURNAL_PART_CLAUDE = "journal-part-claude-au-fil-de-l-eau.jsonl"  # v11c, constat 6 : une ligne par lecture, scellé à la fin
CHAMPS_ETAT_CLAUDE = ("plafond_usd", "reserve_par_appel_usd", "depense_usd", "engage_usd", "appels", "refus", "refus_modele",
                      "restant_usd", "appels_au_dessus_de_la_reserve", "depassement_max_usd")


class SurveillanceCleClaude:
    """GO-2026-11-22-124. Relit l'état du relais Claude et son journal (statuts seulement, jamais un contenu) ; `depasse()` rend
    {code: 5, nature, statut, cause, motif} ou None.
    Déclencheurs (v11c, constat 7 : gardés plus larges que le texte, écrits comme tels) : premier statut de 400 à 499 hors 429 au
    journal — appel relayé (refus de l'interface d'Anthropic) ou refus propre du relais (401 jeton, 402 plafond, 403 modèle,
    404 chemin, 413 corps : sa ligne porte un `motif`) ; `refus` > 0 dans l'état (refus du relais dont la ligne n'est pas encore
    lue) ; part engagée (dépense + réservé des appels en vol) au plafond propre ; état ou journal illisible trois fois de suite.
    L'arrêt écrit la nature, le statut et la cause réels : le motif du relais quand sa ligne en porte un ; « inconnue » pour un
    appel relayé, dont le relais ne garde que le statut.
    v11c, constat 6 : chaque lecture (lisible ou non) est écrite au journal du run (montants, comptes, statuts) ; compte des appels
    par statut et dernier état lu (dépassement, réserve) au bilan. Constat 5 : `lecture_finale()` après l'arrêt de
    l'orchestrateur. Une ligne du journal du relais encore sans fin de ligne est lue à la lecture suivante ; une lecture manquée
    isolée est comptée, jamais tue."""

    def __init__(self, r: "Reglages", url: str, plafond_part: float, journal: str | None = None, journal_run: Path | None = None):
        self.r, self.url, self.plafond_part, self.journal = r, url, plafond_part, journal
        self.journal_run = Path(journal_run) if journal_run is not None else None
        self.illisibles, self.lectures, self.derniere, self.refus, self.vu = 0, 0, None, None, 0
        self.par_statut: dict = {}
        self.etat: dict = {}
        self.lignes_ecrites = 0

    def _ecrire(self, ligne: dict) -> None:
        self.lignes_ecrites += 1
        if self.journal_run is not None:
            with open(self.journal_run, "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")

    def _lignes_du_relais(self) -> tuple:
        """(nombre de lignes complètes, lignes neuves lues) ; une ligne illisible lève (lecture manquée, rien n'est compté)."""
        if not self.journal:
            return self.vu, []
        p = Path(self.journal)
        if not p.exists():
            return self.vu, []  # aucun appel encore : le relais crée son journal au premier appel
        texte = p.read_text(encoding="utf-8", errors="replace")
        lignes = texte[: texte.rfind("\n") + 1].splitlines()
        return len(lignes), [json.loads(x) for x in lignes[self.vu:] if x.strip()]

    def _arret(self, nature: str, statut, cause: str) -> dict:
        return {"code": 5, "nature": nature, "statut": statut, "cause": cause,
                "motif": f"{nature} : statut {statut if statut is not None else 'sans objet'} ; cause : {cause} ; part engagée "
                         f"{self.derniere} USD (plafond de la part Claude {self.plafond_part} USD)"}

    def depasse(self, moment: str = "au fil de l'eau"):
        quand = _dt.datetime.now(_dt.timezone.utc).isoformat()
        try:
            etat = (self.r.lire_etat_relais or _etat_relais)(self.url)
            engagee = float(etat.get("depense_usd") or 0.0) + float(etat.get("engage_usd") or 0.0)
            refus = etat.get("refus", 0) or 0
            if not (math.isfinite(engagee) and _nombre(refus)):
                raise ValueError("non fini")
            n_lignes, neuves = self._lignes_du_relais()
        except Exception as e:  # noqa: BLE001
            self.illisibles += 1
            self._ecrire({"quand": quand, "moment": moment, "lisible": False, "erreur": type(e).__name__,
                          "illisibles_de_suite": self.illisibles})
            if self.illisibles >= LECTURES_ILLISIBLES_MAX:
                return self._arret("part Claude non comptable", None, f"état ou journal du relais Claude illisible "
                                   f"{self.illisibles} fois de suite ({type(e).__name__})")
            return None
        self.vu = n_lignes
        statuts_neufs: dict = {}
        premier = None
        for o in neuves:
            s = o.get("statut")
            statuts_neufs[str(s)] = statuts_neufs.get(str(s), 0) + 1
            if premier is None and est_refus_interface(s):
                premier = o
        for k, n in statuts_neufs.items():
            self.par_statut[k] = self.par_statut.get(k, 0) + n
        self.illisibles, self.lectures = 0, self.lectures + 1
        self.derniere, self.refus = round(engagee, 6), refus
        self.etat = {k: etat.get(k) for k in CHAMPS_ETAT_CLAUDE if k in etat}
        self._ecrire({"quand": quand, "moment": moment, "lisible": True, "lecture": self.lectures, "etat": self.etat,
                      "part_engagee_usd": self.derniere, "statuts_neufs": statuts_neufs})
        if premier is not None:
            s = premier.get("statut")
            if premier.get("motif") is not None:  # refus propre du relais : sa ligne dit la cause
                return self._arret("refus du relais Claude", s, str(premier.get("motif")))
            return self._arret("refus de l'interface d'Anthropic, relayé", s,
                               "inconnue : le relais ne garde que le statut d'un appel relayé (un statut 400 peut être un crédit "
                               "insuffisant, R-4833, ou une requête refusée)")
        if refus > 0:
            return self._arret("refus du relais Claude", None,
                               f"{refus} refus comptés dans l'état du relais, ligne non encore lue à son journal (401 jeton, 402 "
                               "plafond, 403 modèle, 404 chemin ou 413 corps : la ligne du journal dit lequel)")
        if engagee >= self.plafond_part - 1e-9:
            return self._arret("part engagée au plafond", None,
                               f"part Claude engagée {self.derniere} USD ≥ plafond de la part Claude {self.plafond_part} USD "
                               "(déclencheur du lanceur, avant le refus du relais)")
        return None

    def lecture_finale(self):
        """v11c, constat 5 : relecture après l'arrêt de l'orchestrateur ; une lecture illisible est refaite, jusqu'à
        LECTURES_ILLISIBLES_MAX lectures manquées de suite (alors code 5, part non comptable)."""
        for _ in range(LECTURES_ILLISIBLES_MAX):
            a = self.depasse(moment="relecture finale")
            if a is not None or self.illisibles == 0:
                return a
        return self._arret("part Claude non comptable", None, "relecture finale illisible")

    def sceller_journal(self) -> dict | None:
        """Compagnon `.sha256` du journal du run (écrit une fois, à la fin)."""
        if self.journal_run is None or not self.journal_run.is_file():
            return {"chemin": None, "lignes": self.lignes_ecrites}
        h = sha256_fichier(self.journal_run)
        with open(str(self.journal_run) + ".sha256", "x", encoding="utf-8") as f:
            f.write(f"{h}  {self.journal_run.name}\n")
        return {"chemin": str(self.journal_run), "sha256": h, "lignes": self.lignes_ecrites}

    def bilan(self) -> dict:
        return {"plafond_part_claude_usd": self.plafond_part, "lectures": self.lectures, "derniere_part_engagee_usd": self.derniere,
                "refus_du_relais": self.refus, "illisibles_de_suite": self.illisibles, "journal": self.journal,
                "appels_par_statut": dict(sorted(self.par_statut.items())), "dernier_etat_lu": dict(self.etat),
                "depassement_max_usd": self.etat.get("depassement_max_usd"),
                "appels_au_dessus_de_la_reserve": self.etat.get("appels_au_dessus_de_la_reserve"),
                "reserve_par_appel_usd": self.etat.get("reserve_par_appel_usd"), "lectures_ecrites_au_journal_du_run": self.lignes_ecrites}