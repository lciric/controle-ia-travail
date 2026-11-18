"""Bras du juge externe différé avec **remplacement déclaré du modèle d'un juge** — version 1 (ajout seul, R12).

Copie de `executer_bras_differe` de `pole/ideation_v2.py` (arbre `orchestrator/` ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70,
fichier 67d2ad35…, lignes 2754 à 3161), **inchangée sauf quatre endroits**, tous marqués « remplacement v1 » :
1. la garde CL35-04 admet, pour une étiquette de juge externe, le modèle joué d'un remplacement **déclaré** (modèle de la
   course, modèle joué, ligne de GO, mot verbatim) ; tout autre écart d'étiquette ou de modèle reste refusé ;
2. le manifeste du bras porte les remplacements ;
3. l'auto-préférence se lit sur le modèle **joué** ;
4. la lecture porte une mention visible et, à côté, l'auto-préférence au modèle de la course, marquée descriptive.
Tout le reste (attestation scellée, jamais rejoué après dépense, témoins relus, plafonds, tentatives, classement sans bras,
aucun repli silencieux) est le code d'origine, appelé avec les mêmes noms importés de `pole.ideation_v2`.

Sans remplacement à déclarer, ce module refuse : le bras ordinaire se joue par `pole.ideation_v2.executer_bras_differe`.
"""
import re

from . import ideation_v2 as _base

globals().update({_n: _v for _n, _v in vars(_base).items() if not _n.startswith("__")})  # mêmes noms que le code d'origine

MENTION_REMPLACEMENT = "juge externe joué avec un autre modèle que celui déclaré à la course"
CHAMPS_REMPLACEMENT = ("modele_course", "modele_joue", "go", "mot")
MOTIF_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2}")


def valider_remplacements(remplacements, attendus_course):
    """`{etiquette: {"modele_course", "modele_joue", "go", "mot"}}`, non vide ; chaque étiquette est un juge externe de la
    course, `modele_course` est celui du manifeste de départ, `modele_joue` en diffère, `go` a la forme d'un identifiant de
    ligne de GO, `mot` est le mot verbatim (non vide). Rend une copie aux seuls champs attendus ; lève sinon."""
    if not isinstance(remplacements, dict) or not remplacements:
        raise CourseInterrompue("remplacement de modèle : aucun remplacement déclaré (le bras ordinaire se joue par "
                                "executer_bras_differe)")
    propre = {}
    for etiquette, r in remplacements.items():
        if etiquette not in attendus_course:
            raise CourseInterrompue(f"remplacement de modèle : {etiquette!r} n'est pas un juge externe de cette course "
                                    f"({sorted(attendus_course)})")
        if not isinstance(r, dict) or set(r) != set(CHAMPS_REMPLACEMENT):
            raise CourseInterrompue(f"remplacement de modèle de {etiquette!r} : champs {CHAMPS_REMPLACEMENT} exigés, "
                                    "ni plus ni moins")
        for c in CHAMPS_REMPLACEMENT:
            if not isinstance(r[c], str) or not r[c].strip() or r[c] != r[c].strip():
                raise CourseInterrompue(f"remplacement de modèle de {etiquette!r} : {c} vide ou à blancs en bord")
        if r["modele_course"] != attendus_course[etiquette]:
            raise CourseInterrompue(f"remplacement de modèle de {etiquette!r} : modèle de la course déclaré "
                                    f"{r['modele_course']!r} ≠ manifeste de départ {attendus_course[etiquette]!r}")
        if r["modele_joue"] == r["modele_course"]:
            raise CourseInterrompue(f"remplacement de modèle de {etiquette!r} : le modèle joué est celui de la course")
        if not MOTIF_GO.fullmatch(r["go"]):
            raise CourseInterrompue(f"remplacement de modèle de {etiquette!r} : ligne de GO mal formée ({r['go']!r})")
        propre[etiquette] = {c: r[c] for c in CHAMPS_REMPLACEMENT}
    return propre


def executer_bras_differe_avec_remplacement(sortie, *, remplacements_modele_juge, attestation_lecture_humaine,
                                            juges_externes, budgets, lire_etat_relais=None,
                          horodatage=None, budget_controle_usd=None, exiger_cout_controle=True, budget_externe_usd=None,
                          commande_externe=None, taille_max_consigne_externe=None, prix_caractere_usd=PRIX_CARACTERE_PRUDENT_USD):
    """v36 → v41 : joue les juges externes différés d'une course déjà faite, **après** une lecture humaine attestée — le seul
    chemin par lequel un juge d'une autre lignée lit les fiches — puis écrit le **classement à trois juges** (médiane par
    critère, porte sur l'agrégat, unanimité et accords de rang par paire rapportés ; n° 118).

    Avant tout appel : `manifeste-bras-rapporte.json` ou une réponse déjà rendue → refus (jamais rejoué après dépense) ;
    attestation **scellée** (CL35-14) `{"lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256":
    {étiquette: …}}` ; sceaux de la course vérifiés ; étiquettes et modèles identiques à ceux de la course ; sur une
    course réelle, seule une commande externe joue le bras (CL35-04) ; plafond **externe** relu dans le manifeste de départ
    (sauf `budget_externe_usd` donné) moins le coût externe déjà compté par la course, vérifié **avant** l'appel de
    contrôle (CL35-05). Témoins relus depuis `noyau/temoins-servis.json` et lus chez chaque juge externe (critère gelé).
    Aucun repli silencieux (n° 118 point 3) : juge externe en panne, au-delà du plafond ou notes invalides → classement à
    deux juges écrit **marqué « sans juge externe, illisible au sens du devis »** (`classement-sans-bras.json`), manifeste
    avec l'erreur, et `CourseInterrompue` ; témoins échoués chez lui → classement à trois juges écrit mais illisible.
    Le manifeste du bras est écrit **avant** les fichiers de lecture (CL35-01), sur tous les chemins après le départ.
    v41 : `budget_controle_usd` absent → celui que la course a compté (`somme_des_plafonds` du manifeste de départ,
    CL40-03) ; le contrôle porte la consigne réelle du juge (CL40-04) ; un contrôle interrompu compte son plafond (CL40-02) ;
    `relancable` calculé (tentatives et plafond externe de la relance) ; tentatives payées lues sceau vérifié (CL40-05) ;
    tout échec après envoi écrit `classement-sans-bras.json` (CL40-08).
    v42 (CL41-01, option B) : le contrôle redevient **court** (il éprouve la commande ; la consigne du juge n'est envoyée
    qu'à la session du juge) ; **garde de taille** avant tout appel : une consigne en attente plus grosse que
    `taille_max_consigne_externe` (sinon la valeur donnée à la course, sinon plafond de la session du juge / prix prudent)
    → `manifeste-bras-refus-taille-K.json` scellé, rien payé, aucune tentative comptée ; `budget_externe_usd` donné
    (lanceur, `--budget-externe-usd`) vérifié fini ≥ 0 ; une tentative scellée **non relançable** écrit le classement à
    deux juges marqué « sans juge externe » (sans verrouiller par le manifeste du bras) et lève `SansJugeExterne` ;
    CL41-04 : un contrôle qui n'était pas court et n'a pas rendu « OK » verrouille le bras comme un envoi.
    v43 (CL42-05) : garde du bras = `taille_max_consigne_externe` donné au bras (`--taille-max-consigne-externe-bras`),
    sinon plafond de la session du juge / prix prudent **moins la provision de sortie** (`provision_sortie_juge_caracteres`
    des fiches servies à ce juge ; 3,5 et 52 fiches → 1 400 000 − 520 000 = 880 000) ; **la valeur donnée à la course ne s'y
    applique plus** ;
    un refus de taille **compte une tentative non relançable** (`manifeste-bras-refus-taille-N.json`, N = numéro de
    tentative) et écrit le classement sans bras (`SansJugeExterne`) ; prix d'un caractère `prix_caractere_usd` (CL42-04 b,
    `--prix-entree-usd-par-million-jetons`). CL42-06 : un échec du classement de repli est dit
    dans l'exception levée et scellé (`classement-sans-bras-impossible-N.json`) ; un classement de repli déjà écrit n'est
    jamais réécrit, et l'exception le dit."""
    def lire_json_scelle(nom):
        chemin = os.path.join(sortie, nom)
        if not verifier_scelle(chemin):
            raise CourseInterrompue(f"sceau absent ou faux : {nom} (la course n'est pas intacte)")
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)

    if budget_controle_usd is not None:  # v41 (CL40-05)
        _exiger_somme("budget_controle_usd", budget_controle_usd)
    if budget_externe_usd is not None:  # v42 (CL41-01) : le plafond externe peut être donné au bras ; fini ≥ 0
        _exiger_somme("budget_externe_usd", budget_externe_usd)
    if taille_max_consigne_externe is not None:
        exiger_taille_max_consigne(taille_max_consigne_externe)
    if not _fini(prix_caractere_usd) or prix_caractere_usd <= 0:  # v43 (CL42-04 b)
        raise CourseInterrompue(f"prix_caractere_usd : réel fini > 0 (reçu {prix_caractere_usd!r})")
    chemin_manifeste = os.path.join(sortie, "manifeste-bras-rapporte.json")
    if os.path.exists(chemin_manifeste):
        raise CourseInterrompue("le bras a déjà été joué pour cette course (manifeste-bras-rapporte.json existe) : jamais "
                                "rejoué après dépense (CL34-04)")
    # v37 (CL36-01) : un échec AVANT tout envoi et toute dépense (commande introuvable, clé dans l'environnement, contrôle
    # refusé sans coût) écrit un manifeste « non joué » numéroté et laisse le bras relançable.
    tentatives_non_jouees = sorted(f for f in os.listdir(sortie) if re.match(r"manifeste-bras-non-joue-\d+\.json$", f))
    # v38 (CL37-02) : les tentatives qui ont coûté (contrôle refusé après dépense) sont lues ; leur coût s'impute au plafond
    # externe ; au plus MAX_TENTATIVES_BRAS tentatives au total
    tentatives_payees = sorted(f for f in os.listdir(sortie) if re.match(r"bras-tentative-\d+\.json$", f))
    cout_tentatives = 0.0
    for f in tentatives_payees:  # v41 (CL40-05) : sceau vérifié, coût réel fini ≥ 0
        if not verifier_scelle(os.path.join(sortie, f)):
            raise CourseInterrompue(f"tentative du bras au sceau absent ou faux : {f} (aucune relance sans un mot de Lazar)")
        with open(os.path.join(sortie, f), "r", encoding="utf-8") as fh:
            c = json.load(fh)["reglages"]["journal"]["cout_total_usd"]
        if not _fini(c) or c < 0:
            raise CourseInterrompue(f"tentative du bras au coût illisible : {f} ({c!r})")
        cout_tentatives += float(c)
    # v43 (CL42-05) : un refus de taille au bras est une tentative (non relançable, rien payé)
    tentatives_refus_taille = sorted(f for f in os.listdir(sortie) if re.match(r"manifeste-bras-refus-taille-\d+\.json$", f))
    if len(tentatives_non_jouees) + len(tentatives_payees) + len(tentatives_refus_taille) >= MAX_TENTATIVES_BRAS:
        raise CourseInterrompue(f"{MAX_TENTATIVES_BRAS} tentatives du bras déjà faites : plus de relance sans un mot de "
                                "Lazar (CL37-02)")
    attestation = _lire_attestation(attestation_lecture_humaine,
                                    ("lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256"))
    if attestation["fiches_validees_sha256"] != sha256_fichier(os.path.join(sortie, "fiches-validees.json")):
        raise CourseInterrompue("l'attestation ne porte pas l'empreinte de fiches-validees.json de cette course")
    consignes_attestees = attestation["consignes_en_attente_sha256"]
    if not isinstance(consignes_attestees, dict):
        raise CourseInterrompue("attestation : consignes_en_attente_sha256 doit être {etiquette: sha256}")
    fiches = lire_json_scelle("fiches-validees.json")
    notes_par_auteur = lire_json_scelle("notes-par-juge.json")
    doublons_par_juge = lire_json_scelle("doublons-par-juge.json")
    cles_par_juge = lire_json_scelle(os.path.join("noyau", "cles-anonymisation-par-juge.json"))
    temoins = lire_json_scelle(os.path.join("noyau", "temoins-servis.json"))
    modeles = lire_json_scelle(os.path.join("noyau", "modeles.json"))
    lecture_course = lire_json_scelle("lecture-course.json")
    depart = lire_json_scelle("manifeste-depart.json")["reglages"]
    fin = lire_json_scelle("manifeste-fin.json")["reglages"]
    if budget_controle_usd is None:  # v41 (CL40-03) : par défaut, le contrôle du bras que la course a compté dans sa somme
        budget_controle_usd = _exiger_somme("budget_controle_bras_usd (manifeste de départ)", (depart.get(
            "somme_des_plafonds") or {}).get("budget_controle_bras_usd", 0.2))
    if fin.get("erreur"):
        raise CourseInterrompue("la course s'est arrêtée en erreur : aucun bras sur une course incomplète")
    attendus_course = {e: m for e, m in depart.get("juges_externes", [])}
    # remplacement v1 : seul écart admis à CL35-04 — le modèle d'un juge externe, déclaré avec sa ligne de GO et son mot
    remplacements = valider_remplacements(remplacements_modele_juge, attendus_course)
    attendus = {e: (remplacements[e]["modele_joue"] if e in remplacements else m) for e, m in attendus_course.items()}
    donnes = {e: m for e, m, _ in juges_externes}
    if donnes != attendus:
        raise CourseInterrompue(f"juges externes donnés {donnes} ≠ attendus {attendus} (course {attendus_course}, "
                                f"remplacements déclarés {sorted(remplacements)} ; CL35-04)")
    moteur_course = depart.get("moteur")
    cout_fictif = False  # le coût du bras est celui de ses propres adaptateurs : fictif dès qu'un n'est pas une commande
    for e, _, a in juges_externes:
        if moteur_course == "claude-sdk" and getattr(a, "nom", None) != "commande-externe":
            raise CourseInterrompue(f"course réelle : seul une commande externe joue le juge {e!r}, pas "
                                    f"{getattr(a, 'nom', type(a).__name__)!r} (CL35-04)")
        if getattr(a, "nom", None) != "commande-externe":
            cout_fictif = True
    plafond_externe = float(depart.get("budget_externe_usd", 0.0) if budget_externe_usd is None else budget_externe_usd)
    deja_externe = float(fin["journal"].get("cout_externe_usd", 0.0)) + cout_tentatives  # CL37-02
    par_ident = {x["identifiant_auteur"]: x for x in fiches}
    for t in temoins:
        par_ident[t["identifiant_auteur"]] = t
    # --- vérifications avant tout appel : consignes scellées et attestées, aucune réponse déjà rendue, plafond (CL35-05)
    consignes = {}
    for etiquette, modele, _ in juges_externes:
        if etiquette not in cles_par_juge:
            raise CourseInterrompue(f"aucune clé d'anonymisation pour le juge externe {etiquette!r} dans cette course")
        d = os.path.join(sortie, "juges-bras-rapporte", etiquette)
        chemin_consigne = os.path.join(dossier_traces(d), "consigne-en-attente.md")
        if not verifier_scelle(chemin_consigne):
            raise CourseInterrompue(f"consigne en attente absente ou au sceau faux pour {etiquette!r}")
        with open(chemin_consigne, "rb") as f:
            octets = f.read()  # CL35-14 : lus une fois ; empreintés et envoyés tels quels
        empreinte = hashlib.sha256(octets).hexdigest()
        if consignes_attestees.get(etiquette) != empreinte:
            raise CourseInterrompue(f"l'attestation ne porte pas l'empreinte de la consigne en attente de {etiquette!r} "
                                    f"({empreinte[:12]}…) : le lecteur ne l'a pas lue, ou elle a changé")
        if os.path.exists(os.path.join(dossier_traces(d), "reponse.md")):
            raise CourseInterrompue(f"une réponse existe déjà pour {etiquette!r} : jamais rejoué après dépense (CL34-04)")
        if ("juge_ideation", modele) not in budgets:
            raise CourseInterrompue(f"aucun plafond par session pour ('juge_ideation', {modele!r})")
        consignes[etiquette] = octets.decode("utf-8")
    besoin = sum(budgets[("juge_ideation", m)] for _, m, _ in juges_externes) + budget_controle_usd * len(juges_externes)
    journal = {"appels": [], "cout_total_usd": 0.0, "cout_externe_deja_compte_course_usd": deja_externe,
               "cout_tentatives_precedentes_usd": cout_tentatives,
               "tentative": len(tentatives_non_jouees) + len(tentatives_payees) + len(tentatives_refus_taille) + 1,
               "plafond_externe_usd": plafond_externe, "cout_fictif": cout_fictif, "arret": None, "controle": {},
               "non_lance": False, "consigne_envoyee": None, "garde_taille": {}}
    notes_externes, doublons_externes = {}, {}
    resultat = {"classement": None, "lecture": None, "journal": journal, "sans_bras": False}

    def ecrire_manifeste(erreur=None):
        ecrire_json_scelle(chemin_manifeste, manifeste(
            phase="bras-rapporte", horodatage=horodatage, journal=journal, attestation=attestation, erreur=erreur,
            commande_externe=commande_externe or [getattr(a, "description", lambda: None)() for _, _, a in juges_externes],
            juges=[[e, m, getattr(a, "nom", type(a).__name__)] for e, m, a in juges_externes],
            remplacements_modele_juge=remplacements))

    def classement_sans_bras(motif, verrouiller=True):
        """n° 118 point 3 : classement à deux juges écrit, marqué illisible au sens du devis ; jamais de « retenue ».
        v42 (CL41-01) : `verrouiller=False` (tentative non relançable avant envoi) n'écrit pas le manifeste du bras — un
        mot de Lazar (plafond externe relevé) peut encore relancer ; un classement sans bras déjà écrit n'est pas réécrit.
        v43 (CL42-06) : rend « ecrit » ou « existant » (déjà écrit par une tentative précédente : non réécrit, R12)."""
        if os.path.exists(os.path.join(sortie, "classement-sans-bras.json")):
            if verrouiller:
                ecrire_manifeste(erreur=motif)
            resultat.update({"sans_bras": True})
            return "existant"
        classement, lecture = _classer(notes_par_auteur, par_ident, temoins, lecture_course)
        lecture["sans_juge_externe"] = motif
        lecture["lisible_L2_L4"] = False
        if verrouiller:
            ecrire_manifeste(erreur=motif)
        ecrire_json_scelle(os.path.join(sortie, "classements-par-juge-sans-bras.json"), lecture.pop("_classements_par_juge"))
        ecrire_json_scelle(os.path.join(sortie, "classement-sans-bras.json"),
                           {"lisible_L2_L4": False, "sans_juge_externe": motif, "lignes": classement})
        ecrire_json_scelle(os.path.join(sortie, "lecture-sans-bras.json"), lecture)
        resultat.update({"classement": classement, "lecture": lecture, "sans_bras": True})
        return "ecrit"

    def repli_impossible(e2, motif):
        """v43 (CL42-06, R5) : l'échec du classement de repli est scellé (`classement-sans-bras-impossible-N.json`, N =
        numéro de tentative) et rendu en clair, pour l'exception levée ; jamais silencieux."""
        echec = type(e2).__name__ + " : " + caviarder(str(e2))[0][:300]
        journal["classement_sans_bras_impossible"] = echec
        nom = f"classement-sans-bras-impossible-{journal['tentative']}.json"
        try:
            ecrire_json_scelle(os.path.join(sortie, nom), manifeste(
                phase="bras-classement-sans-bras-impossible", horodatage=horodatage, tentative=journal["tentative"],
                classement_sans_bras_impossible=echec, motif_du_repli=motif, journal=journal))
            ou = f"{nom} scellé"
        except Exception as e3:  # noqa: BLE001 — le motif reste dans l'exception levée
            ou = f"{nom} non écrit ({type(e3).__name__} : {str(e3)[:120]})"
        resultat["repli_impossible"] = echec
        return f" ; classement sans bras impossible : {echec} ({ou})"

    def sans_bras_non_relancable(motif):
        """v42 (CL41-01) : tentative scellée non relançable → classement à deux juges écrit tout de suite (sans verrou) ;
        un échec de ce classement de repli n'efface jamais l'erreur d'origine. v43 (CL42-06) : rend le suffixe à ajouter au
        message de l'exception levée — vide si le classement est écrit, « déjà écrit … non réécrit » s'il existait, et
        l'échec (scellé) sinon."""
        try:
            etat = classement_sans_bras(motif, verrouiller=False)
        except Exception as e2:  # noqa: BLE001
            return repli_impossible(e2, motif)
        if etat == "existant":
            return (" ; classement-sans-bras.json déjà écrit par une tentative précédente : non réécrit (R12), il fait "
                    "foi pour cette tentative aussi")
        return ""

    def lever_non_relancable(motif_classement, message, cause):
        """v43 : après une tentative non relançable, classement de repli puis `SansJugeExterne` s'il existe, sinon
        `CourseInterrompue` ; le message dit l'issue du classement de repli (CL42-06)."""
        suite_repli = sans_bras_non_relancable(motif_classement)
        if resultat["sans_bras"]:
            exc = SansJugeExterne(message + (suite_repli or " ; classement-sans-bras.json écrit (deux juges, illisible)"),
                                  resultat)
        else:
            exc = CourseInterrompue(message + suite_repli)
        exc.repli_impossible = resultat.get("repli_impossible")
        raise exc from cause

    # v42 (CL41-01) : garde de taille sans dépense, avant tout appel (contrôle compris). v43 (CL42-05) : garde propre au
    # bras (la valeur de la course ne s'applique plus) ; un refus compte une tentative non relançable, classement sans bras
    for etiquette, modele, _ in juges_externes:
        if taille_max_consigne_externe is not None:
            tmax, origine, prov = taille_max_consigne_externe, "donnée au bras (--taille-max-consigne-externe-bras)", 0
        else:
            plafond_juge = budgets[("juge_ideation", modele)]
            servies = len(cles_par_juge[etiquette])
            prov = provision_sortie_juge_caracteres(servies)
            tmax = taille_max_consigne_par_defaut(plafond_juge, prov, prix_caractere_usd)
            origine = (f"défaut : plafond de la session du juge {plafond_juge} / prix {prix_caractere_usd:.4e} dollar par "
                       f"caractère − provision de sortie {prov} caractères "
                       f"({servies} fiches servies × {PROVISION_SORTIE_PAR_NOTE} caractères de note au rapport "
                       f"{RAPPORT_SORTIE_ENTREE_PRUDENT:g})")
        try:
            journal["garde_taille"][etiquette] = garde_taille_consigne(
                f"consigne du juge externe {etiquette!r}", len(consignes[etiquette]), tmax, origine, prov, prix_caractere_usd)
        except TailleConsigneRefusee as e:
            numero = journal["tentative"]
            journal["garde_taille"][etiquette] = e.details
            journal["arret"] = str(e)
            motifs_t = ["refus de taille : la même consigne et la même garde redonneraient le même refus ; une garde plus "
                        "haute (--taille-max-consigne-externe-bras) ou un plafond de juge plus haut se donne sur mot de Lazar"]
            if numero >= MAX_TENTATIVES_BRAS:
                motifs_t.append(f"{MAX_TENTATIVES_BRAS} tentatives faites")
            ecrire_json_scelle(os.path.join(sortie, f"manifeste-bras-refus-taille-{numero}.json"), manifeste(
                phase="bras-refus-taille", horodatage=horodatage, erreur=str(e), garde_taille=e.details,
                tentative_comptee=True, numero_tentative=numero, relancable=False, motifs_relance=motifs_t, cout_usd=0.0))
            motif_r = (f"tentative {numero} du bras non relançable (refus de taille, rien envoyé, rien payé) : " + str(e)
                       + " ; plus de relance sans un mot de Lazar (" + " ; ".join(motifs_t) + ")")
            lever_non_relancable(motif_r, motif_r, e)
    if deja_externe + besoin > plafond_externe + 1e-9:
        raise CourseInterrompue(f"plafond externe {plafond_externe} insuffisant avant tout appel : déjà {deja_externe} + "
                                f"contrôles et sessions {besoin} (CL35-05)")

    def relance_possible():
        """v41 : ce que vérifiera la relance — moins de MAX_TENTATIVES_BRAS tentatives et le plafond externe qui couvre
        encore les contrôles et les sessions, le coût de cette tentative imputé."""
        motifs = []
        if journal["tentative"] >= MAX_TENTATIVES_BRAS:
            motifs.append(f"{MAX_TENTATIVES_BRAS} tentatives faites")
        if deja_externe + journal["cout_total_usd"] + besoin > plafond_externe + 1e-9:
            motifs.append(f"plafond externe {plafond_externe} < déjà {deja_externe + journal['cout_total_usd']:.4f} + "
                          f"contrôles et sessions {besoin} (un plafond plus haut se donne par --budget-externe-usd, sur mot "
                          "de Lazar)")
        return not motifs, motifs

    try:
        for etiquette, modele, adaptateur in juges_externes:
            dossier_controle = os.path.join(sortie, "bras-rapporte-controle", f"tentative-{journal['tentative']}", etiquette)
            try:  # v42 (CL41-01, option B) : contrôle court — il éprouve la commande, jamais la consigne du juge
                lecture_controle = appel_de_controle(adaptateur, [modele], dossier_controle, budget_controle_usd, None,
                                                     exiger_cout=exiger_cout_controle, supplement=None)[modele]
            except BaseException as e:  # CL37-02, v41 (CL40-02) : refusé ou interrompu, le coût est compté (plafond si
                # interrompu) avant toute décision
                lecture_controle = (getattr(e, "lecture", None) or {}).get(modele, {})
                journal["controle"][etiquette] = lecture_controle
                journal["cout_total_usd"] += cout_compte_controle(lecture_controle)
                journal["non_lance"] = bool(getattr(e, "non_lance", False) or lecture_controle.get("non_lance"))
                journal["arret"] = str(e) or type(e).__name__
                if lecture_controle and not lecture_controle.get("consigne_courte", True):
                    # v42 (CL41-04) : un contrôle qui a pu recevoir les fiches et n'a pas rendu « OK » vaut un envoi
                    journal["consigne_envoyee"] = etiquette
                    journal["arret"] += " ; contrôle non court refusé : fiches possiblement reçues, bras verrouillé (CL41-04)"
                raise
            journal["controle"][etiquette] = lecture_controle
            journal["cout_total_usd"] += cout_compte_controle(lecture_controle)
        for etiquette, modele, adaptateur in juges_externes:
            d = os.path.join(sortie, "juges-bras-rapporte", etiquette)
            plafond = budgets[("juge_ideation", modele)]
            if deja_externe + journal["cout_total_usd"] + plafond > plafond_externe + 1e-9:
                journal["arret"] = f"plafond externe {plafond_externe} atteint avant le juge {etiquette}"
                raise CourseInterrompue(journal["arret"])
            journal["consigne_envoyee"] = etiquette  # v40 (CL39-04) : dès ici, tout échec compte le plafond et verrouille
            try:
                r = adaptateur.lancer("juge_ideation", consignes[etiquette], d, plafond, MAX_TOURS_IDEATION, modele=modele)
            except BaseException as e:
                journal["cout_total_usd"] += plafond
                journal["appels"].append({"role": "juge_ideation", "etiquette": etiquette, "modele": modele,
                                          "statut": "interrompue", "cout_declare_usd": None, "cout_compte_usd": plafond,
                                          "cout_inconnu": True, "erreur": type(e).__name__ + " : " + caviarder(str(e))[0][:300]})
                journal["arret"] = f"juge externe {etiquette} ({modele}) interrompu après envoi : {type(e).__name__}"
                raise
            texte = caviarder(r.texte_final or "")[0]
            brut = texte_a_analyser(r)  # v46 (CL45-02) : analysé brut, valeurs caviardées par valider_notes
            if extraire_demandes_moisson(brut)[0] is not None:  # v47 : un juge ne moissonne jamais (refus dur, rien envoyé)
                journal.setdefault("moisson_refus_durs", []).append({"etiquette": etiquette, "role": "juge_ideation",
                                                                      "motif": "refus dur : aucun tour de moisson pour un juge"})
            cout = float(r.cout_declare_usd or 0.0)
            if r.statut == "ok" or cout > 0 or texte:  # CL36-01 : une réponse n'est consignée que si quelque chose a eu lieu
                ecrire_scelle(os.path.join(dossier_traces(d), "reponse.md"), texte)
            journal["cout_total_usd"] += cout
            journal["appels"].append({"role": "juge_ideation", "etiquette": etiquette, "modele": modele, "statut": r.statut,
                                      "cout_declare_usd": r.cout_declare_usd, "cout_compte_usd": cout,
                                      "cout_inconnu": bool(getattr(r, "cout_inconnu", False)), "erreur": r.erreur})
            if r.statut != "ok" or r.erreur:
                journal["arret"] = f"juge externe {etiquette} ({modele}) : statut {r.statut!r}, erreur {r.erreur!r}"
                raise CourseInterrompue(journal["arret"])
            cle = cles_par_juge[etiquette]
            try:
                notes, doubles = valider_notes(extraire_bloc_json(brut, "notes"), list(cle.keys()))
            except NotesInvalides as e:
                journal["arret"] = caviarder(f"juge externe {etiquette} : notes invalides ({e})")[0]
                raise CourseInterrompue(journal["arret"])
            notes_externes[etiquette] = {cle[i]: n for i, n in notes.items()}
            doublons_externes[etiquette] = doubles
        # --- agrégat à trois juges (n° 118 point 2) : mêmes fiches, mêmes témoins, même grille
        toutes_notes = dict(notes_par_auteur, **notes_externes)
        tous_doublons = dict(doublons_par_juge, **doublons_externes)
        modele_par_juge_course = dict(modeles["par_juge"])
        modele_par_juge = dict(modele_par_juge_course,  # remplacement v1 : l'auto-préférence se lit sur le modèle joué
                               **{e: r["modele_joue"] for e, r in remplacements.items()})
        lecture_temoins_tous = lecture_temoins(toutes_notes, temoins, tous_doublons, cles_par_juge)
        base = dict(lecture_course)
        base.update({"temoins": lecture_temoins_tous,
                     "temoins_juge_externe": lecture_temoins(notes_externes, temoins, doublons_externes, cles_par_juge),
                     "auto_preference": lecture_auto_preference(toutes_notes, modele_par_juge, modeles["par_auteur"]),
                     "remplacement_modele_juge": {
                         "mention": MENTION_REMPLACEMENT, "juges": remplacements,
                         "auto_preference_au_modele_de_la_course": lecture_auto_preference(
                             toutes_notes, modele_par_juge_course, modeles["par_auteur"]),
                         "note": "descriptif : « propre modèle » y désigne le modèle déclaré à la course pour le juge "
                                 "remplacé (même famille de fournisseur que le modèle joué) ; la lecture qui fait foi est "
                                 "`auto_preference`, au modèle joué"},
                     "juges_rendus": len(toutes_notes), "attestation": attestation,
                     "regle": "juge d'une autre lignée à poids égal (Lazar, 28 octobre 21:05 UTC), servi après lecture "
                              "humaine attestée (N-053 point 5) ; médiane par critère à trois juges"})
        classement, lecture = _classer(toutes_notes, par_ident, temoins, base)
        lecture["lisible_L2_L4"] = lecture_temoins_tous["temoins_ok"]
        ecrire_manifeste()  # CL35-01 : avant les fichiers de lecture
        ecrire_json_scelle(os.path.join(sortie, "notes-bras-rapporte.json"), notes_externes)
        ecrire_json_scelle(os.path.join(sortie, "doublons-bras-rapporte.json"), doublons_externes)
        ecrire_json_scelle(os.path.join(sortie, "classements-par-juge.json"), lecture.pop("_classements_par_juge"))
        ecrire_json_scelle(os.path.join(sortie, "classement.json"),
                           {"lisible_L2_L4": lecture["lisible_L2_L4"], "lignes": classement})
        ecrire_json_scelle(os.path.join(sortie, "lecture.json"), lecture)
        resultat.update({"classement": classement, "lecture": lecture})
        return resultat
    except BaseException as e:
        if not journal["arret"]:
            journal["arret"] = type(e).__name__ + " : " + caviarder(str(e))[0][:500]
        reponse_rendue = journal["consigne_envoyee"] is not None or any(  # CL39-04 : envoyé = verrouillé
            os.path.exists(os.path.join(dossier_traces(os.path.join(sortie, "juges-bras-rapporte", e2)), "reponse.md"))
            for e2, _, _ in juges_externes)
        # CL36-01 / CL37-02 : « rien envoyé » seulement si aucun processus n'est parti (commande introuvable, clé dans
        # l'environnement) ; un contrôle refusé qui a coûté est une tentative payée, comptée, bornée
        rien_envoye = (not reponse_rendue and not notes_externes and journal["cout_total_usd"] <= 0
                       and (journal["non_lance"] or isinstance(e, CleDansEnvironnement)))
        numero = journal["tentative"]
        relancable, motifs = relance_possible()  # v41 : calculé, jamais promis
        suite = " ; relance permise" if relancable else " ; plus de relance sans un mot de Lazar (" + " ; ".join(motifs) + ")"
        if rien_envoye and not os.path.exists(chemin_manifeste):
            ecrire_json_scelle(os.path.join(sortie, f"manifeste-bras-non-joue-{numero}.json"),
                               manifeste(phase="bras-non-joue", horodatage=horodatage, journal=journal, erreur=journal["arret"],
                                         relancable=relancable, motifs_relance=motifs))
            motif_c = f"tentative {numero} du bras non relançable : " + journal["arret"] + suite
            message = "bras non joué (rien envoyé, rien dépensé) : " + journal["arret"] + suite
            if not relancable:  # v42 (CL41-01) : plus de course sans classement ; v43 (CL42-06) : issue du repli dite
                if not isinstance(e, Exception):  # une interruption reste une interruption (repli scellé s'il échoue)
                    sans_bras_non_relancable(motif_c)
                    raise
                lever_non_relancable(motif_c, message, e)
            if not isinstance(e, Exception):  # une interruption reste une interruption
                raise
            raise CourseInterrompue(message) from e
        if not reponse_rendue and not notes_externes and not os.path.exists(chemin_manifeste):
            # contrôle refusé ou interrompu après dépense : tentative payée, comptée, bornée
            ecrire_json_scelle(os.path.join(sortie, f"bras-tentative-{numero}.json"),
                               manifeste(phase="bras-tentative", horodatage=horodatage, journal=journal, erreur=journal["arret"],
                                         relancable=relancable, motifs_relance=motifs))
            motif_t = (f"tentative {numero} du bras échouée avant tout envoi des fiches, {journal['cout_total_usd']:.4f} USD "
                       "comptés : " + journal["arret"] + suite)
            if not relancable:  # v42 (CL41-01) : plus de course sans classement ; v43 (CL42-06) : issue du repli dite
                motif_c = f"tentative {numero} du bras non relançable : " + motif_t
                if not isinstance(e, Exception):  # v41 : une interruption reste une interruption (le lanceur rend 2)
                    sans_bras_non_relancable(motif_c)
                    raise
                lever_non_relancable(motif_c, motif_t, e)
            if not isinstance(e, Exception):  # v41 : une interruption reste une interruption (le lanceur rend 2)
                raise
            raise CourseInterrompue(motif_t) from e
        if not os.path.exists(chemin_manifeste):
            # v41 (CL40-08) : après envoi, quel que soit l'échec (interruption comprise), le classement à deux juges est
            # écrit, marqué « sans juge externe, illisible au sens du devis » ; le bras reste verrouillé
            try:
                classement_sans_bras(journal["arret"])
            except Exception as e2:  # noqa: BLE001 — le manifeste doit exister même si le classement de repli échoue
                suite_repli = repli_impossible(e2, journal["arret"])  # v43 (CL42-06) : scellé et dit
                if not os.path.exists(chemin_manifeste):
                    ecrire_manifeste(erreur=journal["arret"] + suite_repli)
                if isinstance(e, CourseInterrompue):
                    exc = CourseInterrompue(str(e) + suite_repli)
                    exc.repli_impossible, exc.lecture = resultat.get("repli_impossible"), getattr(e, "lecture", None)
                    raise exc from e
                try:
                    e.repli_impossible = resultat.get("repli_impossible")
                except AttributeError:
                    pass
            else:
                if isinstance(e, CourseInterrompue):
                    raise SansJugeExterne(journal["arret"], resultat) from e
        raise
