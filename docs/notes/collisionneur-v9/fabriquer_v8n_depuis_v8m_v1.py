"""Fabrique collisionneur_v9_v8n.py depuis la v8m par remplacements exacts (chaque ancien texte présent une seule fois)."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8m.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("420394f9")


def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)


src = remplacer(src, """#   rapport-developpeur-collisionneur-v9-v8m-v1.md, même dossier.
""", """#   rapport-developpeur-collisionneur-v9-v8m-v1.md, même dossier.
# v9-v8n (même développeur, 22 novembre 2026) : copie du v9-v8m (420394f9…, inchangé, R12). Changement, et seulement
#   celui-là : option --espece-ajoutee ESPECE de `etage3`, pour un dossier dont l'étage III est fini. Contrôles avant toute
#   écriture (étage III fini : chaque cellule III valide ou absence acceptée au journal ; espèce hors de la composition
#   scellée). La composition d'origine reste scellée telle quelle ; l'ajout est scellé à part (espece-ajoutee.json, lettre
#   suivante) et journalisé. Cellules de l'espèce ajoutée : III.1 comme les autres ; III.2 sur les conceptions III.1 des
#   espèces d'origine ; III.3 sur sa conception et les critiques des autres, avec une pièce absente déclarée par critique
#   (elles n'ont pas lu sa conception). Aucune cellule d'origine n'est rejouée. Marque « ajoutée après coup » au journal et
#   dans etat.md ; `verifier` les rapporte à part. Plafond sur la dépense totale du dossier ; --ligne-usd ouvre une ligne
#   neuve pour l'ajout. Détail : rapport-developpeur-collisionneur-v9-v8n-v1.md, même dossier.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8m"', 'VERSION = "collisionneur-v9-v8n"')

# état global de l'ajout
src = remplacer(src, """OPTIONS_COMPOSITION = {"sortie_max": False, "effort_max": False}
""", """OPTIONS_COMPOSITION = {"sortie_max": False, "effort_max": False}
# v9-v8n : espèce ajoutée après coup à un dossier fini ({"espece", "lettre"}), ou None ; posé par etendre_composition.
AJOUT = None
FICHIER_AJOUT = "espece-ajoutee.json"
""")
src = remplacer(src, """    global MODELES, LETTRES, OPTIONS_COMPOSITION
""", """    global MODELES, LETTRES, OPTIONS_COMPOSITION, AJOUT
    AJOUT = None  # v9-v8n : une composition neuve n'a pas d'ajout
""")
src = remplacer(src, """    d = {"especes": [MODELES[l]["espece"] for l in LETTRES],
         "lettres": {l: {"espece": MODELES[l]["espece"], "id": MODELES[l]["id"]} for l in LETTRES}}""",
                """    origine = lettres_origine()  # v9-v8n : la composition scellée ne compte jamais l'espèce ajoutée
    d = {"especes": [MODELES[l]["espece"] for l in origine],
         "lettres": {l: {"espece": MODELES[l]["espece"], "id": MODELES[l]["id"]} for l in origine}}""")
src = remplacer(src, """    texte = json.dumps(description_composition(), ensure_ascii=False, indent=1, sort_keys=True) + "\\n"
""", """    texte = texte_composition()
""")
src = remplacer(src, """def sceller_composition(dossier):""", """def texte_composition():
    return json.dumps(description_composition(), ensure_ascii=False, indent=1, sort_keys=True) + "\\n"


def lettres_origine():
    \"\"\"v9-v8n : lettres de la composition d'origine (sans l'espèce ajoutée).\"\"\"
    return tuple(l for l in LETTRES if not (AJOUT and l == AJOUT["lettre"]))


def lire_ajout(dossier):
    \"\"\"v9-v8n : l'ajout scellé du dossier (espece-ajoutee.json), ou None.\"\"\"
    chemin = Path(dossier) / FICHIER_AJOUT
    if not chemin.exists():
        return None
    return json.loads(lire_sceau(chemin)[0])


def etendre_composition(espece, **options):
    \"\"\"v9-v8n : ajoute `espece` à la composition courante (d'origine), à la lettre suivante ; ses réglages sont ceux que
    fixer_composition lui donnerait (mêmes options). La composition d'origine n'est pas touchée.\"\"\"
    global MODELES, LETTRES, AJOUT
    origine = {l: MODELES[l] for l in LETTRES}
    options_origine = dict(OPTIONS_COMPOSITION)
    tout = fixer_composition([origine[l]["espece"] for l in origine] + [espece], sortie_max=options_origine["sortie_max"],
                             effort_max=options_origine["effort_max"], **options)
    m = next(x for x in tout.values() if x["espece"] == espece)
    lettre = "ABCDEFGHIJ"[len(origine)]
    MODELES = dict(origine, **{lettre: m})
    LETTRES = tuple(MODELES)
    AJOUT = {"espece": espece, "lettre": lettre}
    return lettre


def cellules_iii_non_finies(dossier):
    \"\"\"v9-v8n : cellules de l'étage III de la composition d'origine ni valides ni d'absence acceptée au journal (au
    sens de la v8d : l'étage est fini quand chaque cellule est valide ou son absence acceptée).\"\"\"
    acceptees = {e["cellule"] for e in lire_journal(dossier) if e.get("decision") == "absence_acceptee"}
    return [id_cellule(t, l) for t in ORDRE_ETAGE[3] for l in lettres_origine()
            if not cellule_valide(dossier, id_cellule(t, l)) and id_cellule(t, l) not in acceptees]


def preparer_ajout(dossier, a):
    \"\"\"v9-v8n : contrôles de --espece-ajoutee, AVANT toute écriture ; étend la composition en mémoire.\"\"\"
    espece = a.espece_ajoutee
    if espece not in CATALOGUE:
        raise Arret(CODE_USAGE, f"--espece-ajoutee : espèce inconnue {espece!r}")
    if espece in [MODELES[l]["espece"] for l in LETTRES]:
        raise Arret(CODE_USAGE, f"--espece-ajoutee : {espece} est déjà dans la composition scellée du dossier")
    chemin = Path(dossier) / "especes.json"
    if not chemin.exists():
        raise Arret(CODE_USAGE, "--espece-ajoutee : dossier sans composition scellée (especes.json) ; l'ajout ne vaut "
                                "que pour un dossier fini")
    if empreinte(texte_composition()) != lire_sceau(chemin)[1]:
        raise Arret(CODE_USAGE, "--espece-ajoutee : espèces ou options données différentes de la composition scellée du "
                                "dossier ; redonne exactement les options d'origine")
    if len(LETTRES) >= 10:
        raise Arret(CODE_USAGE, "--espece-ajoutee : dix espèces au plus")
    restantes = cellules_iii_non_finies(dossier)
    if restantes:
        raise Arret(CODE_PORTE, f"--espece-ajoutee : étage III du dossier non fini ({restantes}) ; rien n'est écrit")
    existant = lire_ajout(dossier)
    if existant and existant["espece"] != espece:
        raise Arret(CODE_USAGE, f"--espece-ajoutee : le dossier a déjà une espèce ajoutée ({existant['espece']}) ; une "
                                f"seule par dossier")
    lettre = etendre_composition(espece, nom_cle_anthropic=a.cle_anthropic, nom_espace_anthropic=a.nom_espace_anthropic,
                                 nom_cle_openai=a.cle_openai, nom_cle_mistral=a.cle_mistral, kimi_direct=a.kimi_direct,
                                 nom_cle_kimi=a.cle_kimi)
    if existant and existant["lettre"] != lettre:
        raise Arret(CODE_USAGE, f"--espece-ajoutee : lettre {lettre} différente de l'ajout scellé ({existant['lettre']})")
    verifier_cles([lettre])  # seule la clé de l'espèce ajoutée sert : aucune cellule d'origine ne part


def ecrire_ajout(dossier):
    \"\"\"v9-v8n : scelle l'ajout à part et le journalise, au premier lancement seulement.\"\"\"
    if lire_ajout(dossier):
        return
    m = MODELES[AJOUT["lettre"]]
    ecrire_neuf(Path(dossier) / FICHIER_AJOUT, json.dumps(
        {"espece": AJOUT["espece"], "id": m["id"], "lettre": AJOUT["lettre"], "lettres_origine": list(lettres_origine()),
         "sha256_especes_json": lire_sceau(Path(dossier) / "especes.json")[1], "options": dict(OPTIONS_COMPOSITION)},
        ensure_ascii=False, indent=1, sort_keys=True) + "\\n")
    ajouter_journal(dossier, {"espece_ajoutee": AJOUT["espece"], "lettre": AJOUT["lettre"], "id": m["id"],
                              "depense_avant": depense(dossier), "quand": maintenant(), "script": VERSION})


def ouvrir_ligne_ajout(dossier, montant):
    \"\"\"v9-v8n : ligne neuve de l'ajout, ouverte au premier lancement qui la donne ; ensuite, même montant.\"\"\"
    if montant is None:
        return
    if not montant > 0:
        raise Arret(CODE_USAGE, "--ligne-usd doit être positif")
    deja = [e for e in lire_journal(dossier) if "ligne_ajout" in e]
    if deja:
        if abs(deja[0]["ligne_ajout"] - montant) > 1e-9:
            raise Arret(CODE_USAGE, f"ligne de l'ajout déjà ouverte à {deja[0]['ligne_ajout']:.2f} USD")
        return
    ajouter_journal(dossier, {"ligne_ajout": montant, "espece": AJOUT["espece"], "depense_avant": depense(dossier),
                              "quand": maintenant(), "script": VERSION, "sha256_script": empreinte_script()})


def sceller_composition(dossier):""")
src = remplacer(src, """    compo = json.loads(texte)
    options = compo.get("options") or {}  # v9-v8l (N6) : options scellées relues (verifier, devis-reprise)
    fixer_composition(compo["especes"], sortie_max=bool(options.get("sortie_max")),
                      effort_max=bool(options.get("effort_max")))
""", """    compo = json.loads(texte)
    options = compo.get("options") or {}  # v9-v8l (N6) : options scellées relues (verifier, devis-reprise)
    fixer_composition(compo["especes"], sortie_max=bool(options.get("sortie_max")),
                      effort_max=bool(options.get("effort_max")))
    ajout = lire_ajout(dossier)  # v9-v8n : l'espèce ajoutée, à sa lettre scellée
    if ajout and etendre_composition(ajout["espece"]) != ajout["lettre"]:
        raise Arret(CODE_USAGE, f"{FICHIER_AJOUT} : lettre scellée {ajout['lettre']} incohérente avec la composition")
""")
src = remplacer(src, """def verifier_cles():
    \"\"\"Présence des clés, lue par leur nom seulement ; aucune valeur affichée.\"\"\"
    absentes = []
    for l in LETTRES:""", """def verifier_cles(lettres=None):
    \"\"\"Présence des clés, lue par leur nom seulement ; aucune valeur affichée. v9-v8n : `lettres` restreint le
    contrôle (ajout : la seule espèce ajoutée).\"\"\"
    absentes = []
    for l in (LETTRES if lettres is None else lettres):""")

# invites de l'espèce ajoutée
src = remplacer(src, """    if manquantes:
        raise Arret(CODE_PORTE, f"{id_cellule(tour, lettre)} : entrées manquantes {manquantes} ; "
                                f"relance-les, ou décide --accepter-absence")""",
                """    if AJOUT and lettre == AJOUT["lettre"] and tour == "E3-T3":  # v9-v8n : critiques écrites avant l'ajout
        for l in autres(lettre):
            cid = f"{id_cellule('E3-T2', l)}:lecture-de-{id_cellule('E3-T1', lettre)}"
            morceaux.append(bloc_absent(cid, f"jamais écrite ; la critique {id_cellule('E3-T2', l)} a été écrite avant "
                                             f"l'ajout de la proposition {lettre} et n'a pas lu sa conception"))
            pieces.append({"cellule": cid, "sha256": None, "absence_acceptee": True, "absence_declaree_ajout": True})
    if manquantes:
        raise Arret(CODE_PORTE, f"{id_cellule(tour, lettre)} : entrées manquantes {manquantes} ; "
                                f"relance-les, ou décide --accepter-absence")""")

# journal par essai
src = remplacer(src, """                  "rejeu_effort_xhigh": genre == "rejeu_xhigh",  # v9-v8m""",
                """                  "rejeu_effort_xhigh": genre == "rejeu_xhigh",  # v9-v8m
                  "ajoutee_apres_coup": bool(AJOUT and lettre == AJOUT["lettre"]),  # v9-v8n""")

# ligne de l'ajout
src = remplacer(src, """    reprises = lignes_reprise(dossier)
    if reprises:
        r = reprises[-1]""", """    ajout = [e for e in lire_journal(dossier) if "ligne_ajout" in e] if AJOUT else []  # v9-v8n
    if ajout:
        return {"montant": ajout[0]["ligne_ajout"], "depense_avant": ajout[0]["depense_avant"], "nature": "de l'ajout",
                "go": None}
    reprises = lignes_reprise(dossier)
    if reprises:
        r = reprises[-1]""")

# lancer l'étage sur des lettres données
src = remplacer(src, """def lancer_etage(dossier, etage, plafond, absences, appelants, jev=False, repli_lot=False):""",
                """def lancer_etage(dossier, etage, plafond, absences, appelants, jev=False, repli_lot=False, lettres=None):""")
src = remplacer(src, """        for lettre in LETTRES:
            cid = id_cellule(tour, lettre)
            if cellule_valide(dossier, cid):""", """        for lettre in (LETTRES if lettres is None else lettres):  # v9-v8n : l'ajout ne lance que sa lettre
            cid = id_cellule(tour, lettre)
            if cellule_valide(dossier, cid):""")

# état
src = remplacer(src, """    lignes = ["| Cellule | Statut | Essais | Modèle servi | Caractères | Marqueur | Coût USD |",
              "|---|---|---|---|---|---|---|"]
    for tour in TOURS:
        for lettre in LETTRES:""", """    lignes = ["| Cellule | Statut | Essais | Modèle servi | Caractères | Marqueur | Coût USD | Ajoutée après coup |",
              "|---|---|---|---|---|---|---|---|"]
    ajout = lire_ajout(dossier)  # v9-v8n
    lettres = list(LETTRES) + ([ajout["lettre"]] if ajout and ajout["lettre"] not in LETTRES else [])
    for tour in TOURS:
        for lettre in lettres:""")
src = remplacer(src, """                          f"{'oui' if d['marqueur_fin'] else 'non'} | {sum(e['cout_usd'] for e in essais):.2f} |")""",
                """                          f"{'oui' if d['marqueur_fin'] else 'non'} | {sum(e['cout_usd'] for e in essais):.2f} | "
                          f"{'oui' if d.get('ajoutee_apres_coup') else ''} |")""")

# vérification
src = remplacer(src, """    for r in rejugements(dossier):  # v9-v7
        if not chemin_cellule(dossier, r["rejugement"]).exists():""", """    ajout = lire_ajout(dossier)  # v9-v8n : l'ajout tient à la composition scellée ; ses essais portent la marque
    if ajout:
        if ajout.get("sha256_especes_json") != lire_sceau(dossier / "especes.json")[1]:
            problemes.append(f"{FICHIER_AJOUT} : composition d'origine différente de celle scellée à l'ajout")
        for e in essais:
            if (e["cellule"][-1] == ajout["lettre"]) != bool(e.get("ajoutee_apres_coup")):
                problemes.append(f"{e['cellule']} essai {e['essai']} : marque « ajoutée après coup » incohérente")
            if e["cellule"][-1] == ajout["lettre"] and not e["cellule"].startswith("E3-"):
                problemes.append(f"{e['cellule']} : cellule de l'espèce ajoutée hors de l'étage III")
    for r in rejugements(dossier):  # v9-v7
        if not chemin_cellule(dossier, r["rejugement"]).exists():""")

# ligne de commande
src = remplacer(src, """            s.add_argument("--question")
""", """            s.add_argument("--question")
            s.add_argument("--espece-ajoutee", default=None,  # v9-v8n
                           help="ESPÈCE ajoutée après coup à un dossier dont l'étage III est fini (lettre suivante)")
""")
src = remplacer(src, """        print(f"Script courant : {VERSION}, sha256 {empreinte_script()}")
""", """        print(f"Script courant : {VERSION}, sha256 {empreinte_script()}")
        try:  # v9-v8n : cellules ajoutées après coup, rapportées à part
            ajout = lire_ajout(a.dossier)
        except Arret:
            ajout = None
        if ajout:
            faites = sorted(p.stem for p in (Path(a.dossier) / "cellules").glob(f"E3-*-{ajout['lettre']}.md"))
            print(f"Cellules ajoutées après coup ({ajout['espece']}, lettre {ajout['lettre']}) : "
                  f"{', '.join(faites) if faites else 'aucune'}")
""")
src = remplacer(src, """        verifier_cles()
""", """        ajout = getattr(a, "espece_ajoutee", None)  # v9-v8n : contrôles de l'ajout avant toute écriture
        if ajout:
            preparer_ajout(dossier, a)
        else:
            verifier_cles()
""")
src = remplacer(src, """        ouvrir_ligne(dossier, a.ligne_usd)  # v9-v3
""", """        if ajout:  # v9-v8n : ajout scellé à part, ligne neuve de l'ajout
            ecrire_ajout(dossier)
            ouvrir_ligne_ajout(dossier, a.ligne_usd)
        else:
            ouvrir_ligne(dossier, a.ligne_usd)  # v9-v3
""")
src = remplacer(src, """        lancer_etage(dossier, etage, a.plafond_usd, set(a.accepter_absence), appelants, jev=a.jev,
                     repli_lot=a.repli_lot)""", """        if ajout:  # v9-v8n : seules les cellules III de l'espèce ajoutée ; absences acceptées au journal reprises
            acceptees = {e["cellule"] for e in lire_journal(dossier) if e.get("decision") == "absence_acceptee"}
            lancer_etage(dossier, 3, a.plafond_usd, set(a.accepter_absence) | acceptees, appelants, jev=a.jev,
                         repli_lot=a.repli_lot, lettres=[AJOUT["lettre"]])
        else:
            lancer_etage(dossier, etage, a.plafond_usd, set(a.accepter_absence), appelants, jev=a.jev,
                         repli_lot=a.repli_lot)""")
assert src.count("def preparer_ajout(") == 1
(D / "collisionneur_v9_v8n.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
