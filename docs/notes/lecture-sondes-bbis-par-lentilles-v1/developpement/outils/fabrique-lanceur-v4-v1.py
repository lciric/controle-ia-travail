"""Fabrique lanceur_v4.py à partir de lanceur_v3.py par remplacements exacts, chacun trouvé une fois et une seule."""
import sys
from pathlib import Path

paquet = Path(sys.argv[1])
s = (paquet / "lanceur_v3.py").read_text(encoding="utf-8")


def rep(avant: str, apres: str, n: int = 1) -> None:
    global s
    assert s.count(avant) == n, (avant[:70], s.count(avant))
    s = s.replace(avant, apres)


# --- en-tête -------------------------------------------------------------------------------------------------------------------
rep('''bornes de calibration comprises (`audits_v1` inchangé d'ici là), avant la ligne `CODE-LENTILLES-BBIS`.
"""''', '''bornes de calibration comprises (`audits_v1` inchangé d'ici là), avant la ligne `CODE-LENTILLES-BBIS`.

Version 4 : le code de l'addendum de concentration **scellé**
(`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
`7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`). Depuis `lanceur_v3` :
- EC-4 (couple C1) : la ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` est exigée avant toute requête ou ouverture (`entrees_v3`) ;
  la fiche du code porte le chemin et l'empreinte de l'addendum (champ `addendum_concentration` : `chemin`, `sha256`), comparés
  à la ligne ; le rapport du montage, les tables et le manifeste citent l'addendum à côté du texte ; la sous-commande
  `recuperer` vérifie aussi la fiche du code ;
- EC-1, EC-2, EC-6 : statistiques de `statistiques_v3` (directions nulles jugées sans elles-mêmes ; garde d'égalité au
  vingtième rang, option 3 : direction lue : arrêt nommé ; direction nulle : marquée, p_bas et p_haut, arrêt nommé si un
  libellé en dépend ; témoin : compté) ; au montage, compte des paires de jetons gardés de même ligne de sortie, sans arrêt ;
- EC-3 : la loi des bornes de calibration est dite « de référence, approchée » dans les tables ; `audits_v1` est inchangé
  (addendum, § 4 : aucun `audits_v2` n'est demandé) : le mot « exacte » de sa docstring se lit « de référence, approchée » ;
- remarque non bloquante de la vérification de la version 2 du code, reprise : le rapport du montage est exigé au départ du
  calcul (absent : rien ne part), et le manifeste le cite toujours.
"""''')
rep("from . import entrees_v2 as en\n", "from . import entrees_v3 as en\n")
rep("from . import statistiques_v2 as st\n", "from . import statistiques_v3 as st\n")
rep('''MODULES = ("__init__", "constantes_v1", "entrees_v2", "montage_v1", "lecture_v1", "nuls_v1", "statistiques_v1", "statistiques_v2",
           "audits_v1", "phrases_v1", "lanceur_v3")''',
    '''MODULES = ("__init__", "constantes_v1", "entrees_v2", "entrees_v3", "montage_v1", "lecture_v1", "nuls_v1", "statistiques_v1",
           "statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "lanceur_v4")
ADDENDUM = {"chemin": en.ADDENDUM, "sha256": en.EMPREINTE_ADDENDUM}
CHAMP_ADDENDUM_DE_LA_FICHE = "addendum_concentration"''')

# --- fiche du code : elle porte le chemin et l'empreinte de l'addendum (EC-4) ---------------------------------------------------
rep('''def exiger_fiche_code(racine_depot: Path, ligne_code) -> dict:
    """Liste d'arrêt : « code non cité par `CODE-LENTILLES-BBIS` » : rien ne part. La fiche citée par la ligne a la forme des
    fiches `CODE-` du registre (`commit`, `fichiers`, `essais`, `contre_lecture` {chemin, sha256}) ; son empreinte égale celle
    de la ligne, et l'empreinte de chaque module de ce paquet égale celle que la fiche porte sous `fichiers`."""''',
    '''def exiger_fiche_code(racine_depot: Path, registre_propre: Path) -> dict:
    """Liste d'arrêt : « code non cité par `CODE-LENTILLES-BBIS` » : rien ne part. La fiche citée par la ligne a la forme des
    fiches `CODE-` du registre (`commit`, `fichiers`, `essais`, `contre_lecture` {chemin, sha256}) ; son empreinte égale celle
    de la ligne, et l'empreinte de chaque module de ce paquet égale celle que la fiche porte sous `fichiers`.
    Addendum, EC-4 : la fiche porte le chemin et l'empreinte de l'addendum scellé (`addendum_concentration` {chemin,
    sha256}) ; le code les compare à la ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS`, qui doit être seule et inscrite avant
    `CODE-LENTILLES-BBIS` et `ENTREES-LENTILLES-BBIS` ; sinon rien ne part. Appelée avant toute requête ou ouverture."""
    ligne_code = en.exiger_registre_propre(registre_propre)["CODE-LENTILLES-BBIS"]''')
rep('''        raise Refus("fiche CODE-LENTILLES-BBIS d'une autre forme que les fiches CODE- du registre : rien ne part")
''', '''        raise Refus("fiche CODE-LENTILLES-BBIS d'une autre forme que les fiches CODE- du registre : rien ne part")
    porte = fiche.get(CHAMP_ADDENDUM_DE_LA_FICHE)
    if not isinstance(porte, dict) or not isinstance(porte.get("chemin"), str) or not isinstance(porte.get("sha256"), str):
        raise Refus("fiche CODE-LENTILLES-BBIS sans le chemin et l'empreinte de l'addendum de concentration scellé : rien ne part")
    ligne_addendum = en.exiger_addendum(registre_propre, porte["chemin"], porte["sha256"])
''')
rep('''    return {"fiche": str(ligne_code.chemin), "sha256": ligne_code.sha256, "commit_de_la_fiche": commit}''',
    '''    return {"fiche": str(ligne_code.chemin), "sha256": ligne_code.sha256, "commit_de_la_fiche": commit,
            "addendum": {"chemin": ligne_addendum.chemin, "sha256": ligne_addendum.sha256,
                         "heure_de_la_ligne": ligne_addendum.heure}}''')

# --- montage ---------------------------------------------------------------------------------------------------------------------
rep('''    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, en.exiger_registre_propre(ctx.registre_propre)["CODE-LENTILLES-BBIS"])
    mo.exiger_sans_debogage(ctx.env)''', '''    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, ctx.registre_propre)
    mo.exiger_sans_debogage(ctx.env)''')
rep('''    rapport = {"run": ctx.run, "texte": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE}, "versions": _versions(),''',
    '''    rapport = {"run": ctx.run, "texte": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE}, "addendum": dict(ADDENDUM),
               "versions": _versions(),''')
rep('''    charge = charger_montage(ctx)
    graines = nu.Graines()
    rapport["garde_fonction_lecture"] = jouer_garde_lecture(charge, graines, r)''',
    '''    charge = charger_montage(ctx)
    # addendum, EC-6 (couple H2) : paires de jetons gardés de même ligne de sortie, comptées et écrites, sans arrêt
    rapport["lignes_de_sortie_egales"] = st.paires_de_lignes_egales(_np(charge.wu))
    graines = nu.Graines()
    rapport["garde_fonction_lecture"] = jouer_garde_lecture(charge, graines, r)''')
rep('''        "fiche du code citée par CODE-LENTILLES-BBIS", "tokeniseur lu du cache par le voisin, hors ligne et sans clé",''',
    '''        "fiche du code citée par CODE-LENTILLES-BBIS", "ligne ADDENDUM-CONCENTRATION-LENTILLES-BBIS égale à la fiche du code",
        "tokeniseur lu du cache par le voisin, hors ligne et sans clé",''')

# --- calcul d'une couche -----------------------------------------------------------------------------------------------------------
rep('''        self.p_temoins: dict[tuple[str, str], list[np.ndarray]] = {}
''', '''        self.p_temoins: dict[tuple[str, str], list[np.ndarray]] = {}
        # garde d'égalité au vingtième rang (EC-6) : comptes par (lentille, nul), écrits dans les tables
        self.egalites: dict[tuple[str, str], dict] = {}
''')
rep('''    def _range_resume(self, prefixe: str, resume: st.ResumeNul) -> None:
        self.tableaux[f"nul__{prefixe}__moyenne"] = _np(resume.moyenne)
        self.tableaux[f"nul__{prefixe}__ecart_type"] = _np(resume.ecart_type)
        self.tableaux[f"nul__{prefixe}__quantile_0_99"] = _np(resume.quantile)
        self.tableaux[f"directions_nulles__{prefixe}__concentration"] = _np(resume.concentration)
        self.tableaux[f"directions_nulles__{prefixe}__part"] = _np(resume.part)
        for nom, c in resume.familles.items():
            self.tableaux[f"directions_nulles__{prefixe}__famille_{nom}"] = _np(c)

    def _signes(self, a: torch.Tensor, nuls: dict) -> dict:
        return {"+": st.lecture_signe(a, nuls, self.masques, self.charge.ids_gardes),
                "-": st.lecture_signe(-a, nuls, self.masques, self.charge.ids_gardes)}
''', '''    def _compter(self, lentille: str, nul: str, resume: st.ResumeNul | None = None, temoins: torch.Tensor | None = None) -> None:
        """EC-6, étages (ii) et (iii) : directions nulles marquées et témoins à égalité au vingtième rang, par (lentille, nul)."""
        c = self.egalites.setdefault((lentille, nul), {"directions_nulles": 0, "directions_nulles_marquees": 0, "temoins": 0,
                                                       "temoins_a_egalite_au_vingtieme_rang": 0, "garde_sans_objet": False})
        if resume is not None:
            c["directions_nulles"] += resume.m
            c["directions_nulles_marquees"] += resume.n_marquees
            c["garde_sans_objet"] = bool(c["garde_sans_objet"] or resume.garde_sans_objet)
        if temoins is not None:
            e = st.egalites_temoins(temoins)
            c["temoins"] += e["temoins"]
            c["temoins_a_egalite_au_vingtieme_rang"] += e["a_egalite_au_vingtieme_rang"]
            c["garde_sans_objet"] = bool(c["garde_sans_objet"] or e["garde_sans_objet"])

    def _range_resume(self, prefixe: str, resume: st.ResumeNul) -> None:
        self.tableaux[f"nul__{prefixe}__moyenne"] = _np(resume.moyenne)
        self.tableaux[f"nul__{prefixe}__ecart_type"] = _np(resume.ecart_type)
        self.tableaux[f"nul__{prefixe}__quantile_0_99"] = _np(resume.quantile)
        self.tableaux[f"directions_nulles__{prefixe}__concentration"] = _np(resume.concentration)
        self.tableaux[f"directions_nulles__{prefixe}__marquee"] = _np(resume.marquee)
        self.tableaux[f"directions_nulles__{prefixe}__part_min"] = _np(resume.part_min)
        self.tableaux[f"directions_nulles__{prefixe}__part_max"] = _np(resume.part_max)
        for nom in resume.familles_min:
            self.tableaux[f"directions_nulles__{prefixe}__famille_{nom}_min"] = _np(resume.familles_min[nom])
            self.tableaux[f"directions_nulles__{prefixe}__famille_{nom}_max"] = _np(resume.familles_max[nom])

    def _signes(self, a: torch.Tensor, nuls: dict, contexte: dict) -> dict:
        return {"+": st.lecture_signe(a, nuls, self.masques, self.charge.ids_gardes, contexte=contexte | {"signe": "+"}),
                "-": st.lecture_signe(-a, nuls, self.masques, self.charge.ids_gardes, contexte=contexte | {"signe": "-"})}
''')
rep('''            self._range_resume(f"couche{c}__{lentille}__{K.NUL_ISOTROPE}", resume)
            s_t, _ = self._lire(t_iso, lentille)
            p = st.p_temoins(s_t, resume)
''', '''            self._range_resume(f"couche{c}__{lentille}__{K.NUL_ISOTROPE}", resume)
            s_t, _ = self._lire(t_iso, lentille)
            self._compter(lentille, K.NUL_ISOTROPE, resume, s_t)
            p = st.p_temoins(s_t, resume)
''')
rep('''                     "lectures": {}, "_v": v_np, "_ident": ident}
''', '''                     "lectures": {}, "_v": v_np, "_ident": ident}
            ou = {"cellule": sonde.cellule, "pli": sonde.pli, "role": sonde.role, "vecteur": nom_v, "couche": c}
            ligne["_ou"] = ou
''')
rep('''                self._range_resume(f"{ident}__{lentille}__{K.NUL_SIGNES}", resume_s)
                s_t, _ = self._lire(t_s, lentille)
                p = st.p_temoins(s_t, resume_s)
''', '''                self._range_resume(f"{ident}__{lentille}__{K.NUL_SIGNES}", resume_s)
                s_t, _ = self._lire(t_s, lentille)
                self._compter(lentille, K.NUL_SIGNES, resume_s, s_t)
                p = st.p_temoins(s_t, resume_s)
''')
rep('''                    "signes": self._signes(a, {K.NUL_ISOTROPE: iso[lentille], K.NUL_SIGNES: (a_s, resume_s)}), "_a": a}''',
    '''                    "signes": self._signes(a, {K.NUL_ISOTROPE: iso[lentille], K.NUL_SIGNES: (a_s, resume_s)},
                                           ou | {"lentille": lentille}), "_a": a}''')
rep('''            ligne["poles"] = self._poles(v, {K.NUL_ISOTROPE: u_iso, K.NUL_SIGNES: u_s})''',
    '''            ligne["poles"] = self._poles(v, {K.NUL_ISOTROPE: u_iso, K.NUL_SIGNES: u_s}, ou)''')
rep('''            resume_couche["lentilles"][lentille] = {
                "indice_matrice": indice, "empreinte_matrice": empreinte, "rapport_epsilon_minimal": minimum,
                "independance_tenue": None if minimum is None else le.independance_tenue(minimum), "calibration": cal}''',
    '''            resume_couche["lentilles"][lentille] = {
                "indice_matrice": indice, "empreinte_matrice": empreinte, "rapport_epsilon_minimal": minimum,
                "independance_tenue": None if minimum is None else le.independance_tenue(minimum), "calibration": cal,
                "egalites_au_vingtieme_rang": {nul: dict(e) for (l, nul), e in sorted(self.egalites.items()) if l == lentille}}''')
rep('''    def _poles(self, v: torch.Tensor, nuls: dict) -> dict:
        pa = st.poles_alignes(v, self.w_down, nuls)
        j_pub = self.matrices[K.LENTILLE_PUBLIQUE][0]
        for p in pa["poles"]:
            colonne = self.w_down[:, p["neurone"]] * (1.0 if p["signe"] == "+" else -1.0)
            scores, _ = le.lire(colonne, j_pub, self.charge.gamma, self.charge.wu)
            _, rangs = le.premiers(scores, K.K_JETONS_POLE)
            p["lecture_publique"] = {"ids": [int(self.charge.ids_gardes[i]) for i in rangs[0].tolist()],
                                     "chaines_echappees": [_echappe(self.charge.chaines[i]) for i in rangs[0].tolist()]}''',
    '''    def _poles(self, v: torch.Tensor, nuls: dict, ou: dict) -> dict:
        """Les deux listes de dix des pôles entrent sous l'arrêt de la direction lue (EC-6, étage (i), couple G3) : les dix
        pôles par cosinus (`st.poles_alignes`) et les dix premiers jetons de la lecture de chaque pôle."""
        pa = st.poles_alignes(v, self.w_down, nuls, contexte=ou | {"signe": "+", "lentille": "sans objet (cosinus)"})
        j_pub = self.matrices[K.LENTILLE_PUBLIQUE][0]
        for p in pa["poles"]:
            colonne = self.w_down[:, p["neurone"]] * (1.0 if p["signe"] == "+" else -1.0)
            scores, _ = le.lire(colonne, j_pub, self.charge.gamma, self.charge.wu)
            haut = st.exiger_sans_egalite(scores[:, 0], K.K_JETONS_POLE,
                                          st.LISTE_JETONS_POLE.format(neurone=p["neurone"], signe=p["signe"]),
                                          self.charge.ids_gardes, ou | {"signe": "+", "lentille": K.LENTILLE_PUBLIQUE})
            rangs = haut["rangs"].tolist()
            p["lecture_publique"] = {"ids": [int(self.charge.ids_gardes[i]) for i in rangs],
                                     "chaines_echappees": [_echappe(self.charge.chaines[i]) for i in rangs]}''')
rep('''            k = min(K.K_JETONS, a.numel())
            sortie[str(autre)] = {s: st.jetons_communs((f * a).topk(k).indices.tolist(), (f * b).topk(k).indices.tolist())
                                  for s, f in (("+", 1.0), ("-", -1.0))}''',
    '''            sortie[str(autre)] = {}
            for s, f in (("+", 1.0), ("-", -1.0)):          # listes du témoin de couche : EC-6, étage (i)
                ou = ligne["_ou"] | {"signe": s, "lentille": K.LENTILLE_PUBLIQUE}
                ici = st.exiger_sans_egalite(f * a, K.K_JETONS, st.LISTE_TEMOIN_DE_COUCHE.format(couche=self.couche),
                                             self.charge.ids_gardes, ou)
                la_bas = st.exiger_sans_egalite(f * b, K.K_JETONS, st.LISTE_TEMOIN_DE_COUCHE.format(couche=autre),
                                                self.charge.ids_gardes, ou)
                sortie[str(autre)][s] = st.jetons_communs(ici["rangs"].tolist(), la_bas["rangs"].tolist())''')
rep('''                self._range_resume(f"{ligne['_ident']}__{lentille}__{K.NUL_ISOTROPE_PAR_DIRECTION}", resume)
                s_t, _ = self._lire(t_d, lentille)
                p = st.p_temoins(s_t, resume)
''', '''                self._range_resume(f"{ligne['_ident']}__{lentille}__{K.NUL_ISOTROPE_PAR_DIRECTION}", resume)
                s_t, _ = self._lire(t_d, lentille)
                self._compter(lentille, K.NUL_ISOTROPE_PAR_DIRECTION, resume, s_t)
                p = st.p_temoins(s_t, resume)
''')
rep('''                neuf = self._signes(lecture["_a"], {K.NUL_ISOTROPE_PAR_DIRECTION: (a_d, resume)})''',
    '''                neuf = self._signes(lecture["_a"], {K.NUL_ISOTROPE_PAR_DIRECTION: (a_d, resume)},
                                    ligne["_ou"] | {"lentille": lentille})''')
rep('''            pa = st.poles_alignes(v, self.w_down, {K.NUL_ISOTROPE_PAR_DIRECTION: u_d})''',
    '''            pa = st.poles_alignes(v, self.w_down, {K.NUL_ISOTROPE_PAR_DIRECTION: u_d},
                                  contexte=ligne["_ou"] | {"signe": "+", "lentille": "sans objet (cosinus)"})''')

# --- libellés : calculés aux deux bornes (EC-6, étage (ii)) -----------------------------------------------------------------------------
rep('''    """Libellés (« Seuil ») de chaque lecture, de sa part au-dessus du nul, de ses familles et de ses pôles ; une calibration
    hors de ses bornes rend « non calculables » les tables de cette couche, de cette lentille et de ce nul. Rend les lignes
    de lecture pour les déclencheurs d'audit."""''',
    '''    """Libellés (« Seuil ») de chaque lecture, de sa part au-dessus du nul, de ses familles et de ses pôles ; une calibration
    hors de ses bornes rend « non calculables » les tables de cette couche, de cette lentille et de ce nul. Rend les lignes
    de lecture pour les déclencheurs d'audit. Addendum, EC-6, étage (ii) : le libellé de la part et celui de chaque famille
    sont calculés avec p_bas sous les deux nuls puis avec p_haut sous les deux nuls ; égaux : le libellé est celui-là ;
    différents : arrêt nommé, avant toute écriture de table. La concentration n'emploie aucune liste de premiers."""''')
rep('''                    i, s = t["nuls"][nul_iso], t["nuls"][K.NUL_SIGNES]
                    t |= {"libelle": st.libelle(i["p_concentration"], s["p_concentration"]),
                          "libelle_part": st.libelle(i["p_part"], s["p_part"]), "nul_isotrope_en_vigueur": nul_iso}
                    for nom, f in t["familles"].items():
                        f["sur_representee"] = st.sur_representee(i["familles"][nom]["p"], s["familles"][nom]["p"])''',
    '''                    i, s = t["nuls"][nul_iso], t["nuls"][K.NUL_SIGNES]
                    ou = d["_ou"] | {"signe": signe, "lentille": lentille}
                    marquees = (i["directions_nulles_marquees"], s["directions_nulles_marquees"])
                    t |= {"libelle": st.libelle(i["p_concentration"], s["p_concentration"]),
                          "libelle_part": st.libelle_sous_departage(st.libelle, "part au-dessus du nul", {
                              "isotrope": (nul_iso, i["p_part_bas"], i["p_part_haut"], marquees[0]),
                              "signes": (K.NUL_SIGNES, s["p_part_bas"], s["p_part_haut"], marquees[1])}, ou),
                          "nul_isotrope_en_vigueur": nul_iso}
                    for nom, f in t["familles"].items():
                        fi, fs = i["familles"][nom], s["familles"][nom]
                        f["sur_representee"] = st.libelle_sous_departage(st.sur_representee, f"compte de la famille {nom}", {
                            "isotrope": (nul_iso, fi["p_bas"], fi["p_haut"], marquees[0]),
                            "signes": (K.NUL_SIGNES, fs["p_bas"], fs["p_haut"], marquees[1])}, ou)''')

# --- audit : la relecture indépendante relève l'égalité, sans arrêt ni table changée -------------------------------------------------
rep('''            choisies.append({"direction": f"{d['sonde']}/{d['vecteur']}", **au.comparer_relecture(lue, relue),''',
    '''            garde = st.premiers_gardes(torch.from_numpy(relue["scores"]), K.K_JETONS)
            choisies.append({"direction": f"{d['sonde']}/{d['vecteur']}", **au.comparer_relecture(lue, relue),
                             "egalite_au_vingtieme_rang_de_la_relecture_en_double_precision": garde["egalite"],''')

# --- calcul ----------------------------------------------------------------------------------------------------------------------
rep('''    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, en.exiger_registre_propre(ctx.registre_propre)["CODE-LENTILLES-BBIS"])
    en.exiger_scores_et_verdict(registre_bbis)''', '''    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, ctx.registre_propre)
    en.exiger_scores_et_verdict(registre_bbis)''')
rep('''        "run": ctx.run, "texte": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE},
        "entrees": {"course": entrees.course.run,''', '''        "run": ctx.run, "texte": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE}, "addendum": dict(ADDENDUM),
        "entrees": {"course": entrees.course.run,''')
rep('''        "comparaisons": comparaisons, "comptes_de_libelles": _comptes(directions),''',
    '''        "comparaisons": comparaisons, "comptes_de_libelles": _comptes(directions),
        "egalites_au_vingtieme_rang": _egalites(couches),''')
rep('''                        "p": "(1 + #{j : statistique(u_j) ≥ statistique(v)}) / (M + 1)", "m": r.m,
                        "statistique_des_directions_nulles": STATISTIQUE_NULLE}}''',
    '''                        "p": "(1 + #{j : statistique(u_j) ≥ statistique(v)}) / (M + 1)", "m": r.m,
                        "statistique_des_directions_nulles": STATISTIQUE_NULLE,
                        "comparaison_des_concentrations": COMPARAISON_CONCENTRATIONS,
                        "garde_d_egalite_au_vingtieme_rang": GARDE_EGALITE, "loi_des_bornes_de_calibration": LOI_CALIBRATION}}''')
rep('''    config = {"texte": K.EMPREINTE_TEXTE, "m": r.m,''', '''    config = {"texte": K.EMPREINTE_TEXTE, "addendum": en.EMPREINTE_ADDENDUM, "m": r.m,''')
rep('''                 "preenregistrement": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE}, "tables_sha256": sha_tables}''',
    '''                 "preenregistrement": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE}, "addendum": dict(ADDENDUM),
                 "tables_sha256": sha_tables}''')
rep('''STATISTIQUE_NULLE = ("concentration et part de chaque direction nulle calculées sans elle-même (moyenne, écart type et quantile 0,99 des "
                     "M − 1 autres) ; moyenne, écart type et quantile des M directions pour la direction lue et les témoins ; "
                     "familles inchangées (addendum « concentration » du texte scellé)")''',
    '''STATISTIQUE_NULLE = ("concentration et part de chaque direction nulle calculées sans elle-même (moyenne, écart type et quantile 0,99 des "
                     "M − 1 autres) ; moyenne, écart type et quantile des M directions pour la direction lue et les témoins ; "
                     "familles inchangées (addendum de concentration scellé, EC-1 et EC-2)")
COMPARAISON_CONCENTRATIONS = ("C(u_j) calculé en double précision, rendu en simple précision comme C(v) ; comparaison C(u_j) ≥ C(v) "
                              "en simple précision ; une égalité compte contre v (addendum, EC-1)")
GARDE_EGALITE = ("égalité au vingtième rang : vingtième et vingt-et-unième valeurs égales, par égalité exacte, en simple précision ; "
                 "direction lue : arrêt nommé ; direction nulle : marquée, p_bas et p_haut, la valeur p écrite est p_haut, attendu "
                 "d'une famille sur les seules directions non marquées, arrêt nommé si le libellé diffère entre les deux bornes ; "
                 "témoin : compté (addendum, EC-6, option 3)")
LOI_CALIBRATION = ("loi de référence du compte : bêta-binomiale (n ; 100 ; M − 99) par jeu, somme de lois indépendantes pour des "
                   "jeux mis en commun ; approchée, non exacte (addendum, EC-3 et § 7) ; bornes de valeurs inchangées")


def _egalites(couches: dict) -> dict:
    """Garde d'égalité au vingtième rang, comptes d'ensemble : directions nulles marquées et témoins à égalité, par (couche,
    lentille, nul) dans `couches`, et leurs totaux ; aucune égalité d'une direction lue n'a été rencontrée (sinon arrêt)."""
    marquees = sum(e["directions_nulles_marquees"] for info in couches.values() for l in info["lentilles"].values()
                   for e in l["egalites_au_vingtieme_rang"].values())
    temoins = sum(e["temoins_a_egalite_au_vingtieme_rang"] for info in couches.values() for l in info["lentilles"].values()
                  for e in l["egalites_au_vingtieme_rang"].values())
    sans_objet = any(e["garde_sans_objet"] for info in couches.values() for l in info["lentilles"].values()
                     for e in l["egalites_au_vingtieme_rang"].values())
    return {"directions_lues_a_egalite": 0, "directions_nulles_marquees": marquees, "temoins_a_egalite": temoins,
            "garde_sans_objet": sans_objet, "note": st.SANS_OBJET if sans_objet else None,
            "detail": "couches/<couche>/lentilles/<lentille>/egalites_au_vingtieme_rang"}''')

# --- remarque de la vérification de la version 2 du code (non bloquante, reprise ici) : le rapport du montage est exigé au départ
rep('''    if not (ctx.travail / MARQUE).is_file():
        raise Arret("dossier de travail monté absent : rien ne part")
    etat["parti"] = True''', '''    if not (ctx.travail / MARQUE).is_file():
        raise Arret("dossier de travail monté absent : rien ne part")
    rapport_montage = ctx.sortie / "diag" / ctx.run / "montage-lentilles-bbis.json"
    if not rapport_montage.is_file():
        raise Arret("rapport du montage absent du dossier de sortie : le manifeste ne pourrait le citer ; rien ne part")
    etat["parti"] = True''')
rep('''    rapport_montage = ctx.sortie / "diag" / ctx.run / "montage-lentilles-bbis.json"
    montage = ({"chemin": f"diag/{ctx.run}/montage-lentilles-bbis.json", "sha256": verifier(rapport_montage)}
               if rapport_montage.is_file() else None)
''', '''    montage = {"chemin": f"diag/{ctx.run}/montage-lentilles-bbis.json", "sha256": verifier(rapport_montage)}
''')

# --- phrases : rien ne change (la valeur p écrite est p_haut) ; ligne de commande -------------------------------------------------------
rep('''    p = argparse.ArgumentParser(description="Lecture des sondes de l'étape B bis par la lentille publique (texte scellé v1)")''',
    '''    p = argparse.ArgumentParser(description="Lecture des sondes de l'étape B bis par la lentille publique (texte scellé v1 et "
                                            "son addendum de concentration scellé)")''')
rep('''    s.add_argument("--registre-bbis", required=True, type=Path)
    s.add_argument("--registre-propre", required=True, type=Path)
    s = sp.add_parser("phrases")''', '''    s.add_argument("--registre-bbis", required=True, type=Path)
    s.add_argument("--registre-propre", required=True, type=Path)
    s.add_argument("--depot", type=Path, default=Path("."))
    s = sp.add_parser("phrases")''')
rep('''        if a.commande == "recuperer":
            en.recuperer_entrees(a.url, a.entrees, a.registre_bbis, a.registre_propre)''',
    '''        if a.commande == "recuperer":
            exiger_fiche_code(a.depot, a.registre_propre)       # code cité et clé de l'addendum, avant toute requête
            en.recuperer_entrees(a.url, a.entrees, a.registre_bbis, a.registre_propre)''')

(paquet / "lanceur_v4.py").write_text(s, encoding="utf-8")
print("lanceur_v4.py écrit")
