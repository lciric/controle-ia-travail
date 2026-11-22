"""Véhicule NA-1, lot 7 — les mesures M1 à M7, C1, I1 et la mesure « replis » (`mesures_na_v1`), lues une fois.

Lettre : V9 (`864f39a7…`), l. 146 à 163 (métrique), l. 315 (« lues une fois »), l. 362 (course arrêtée), l. 386 (arrêt
n° 15) ; conception du véhicule v5 (`1b7f6822…`), § 2.8, § 6.1 (n° 15), § 6.2 (course arrêtée ; M4 sans cumul par clé) ;
projet d'additif v2 (non scellé), P7-ter, P7-quater, P8, P9, P10, D-22.3 ; interface des lots 5 v2, 6 v4 et 7 v1.

**Ce que le module lit**, dans le dossier de sortie de la course (quarantaine), et rien d'autre :
- le journal des arrêts et des générations du lot 6 v3 (`journal-arrets-et-generations-na-v3.jsonl`, scellé) : ses
  événements « génération » (la ligne de la génération) et « clôture » ; **les lignes « cumul par clé » sont relues pour le
  chaînage seulement, puis jetées sans qu'un champ en soit lu** (V9, l. 156 : le cumul par clé ne vit qu'à ce journal) ;
- le bilan scellé (`bilan-course-na-v3.json`), pour le seul contrôle de cohérence avec la clôture ;
- le registre des tentatives de chaque génération complète (`generation-<g>/registre-tentatives-g<g>.jsonl`, scellé), aux
  champs du lot 5 v1 et de l'interface (lot 5 v2) ;
- l'attestation scellée de la relecture « aucune recette » et les étiquettes scellées de la lecture d'antériorité, dans la
  forme de brouillon déclarée ci-dessous (**leur forme réelle est à convenir avec la mère**) ;
- trois entrées données par l'appelant, tirées du tirage scellé et de la configuration : les axes de chaque case servie,
  la valeur de la famille tenue à l'écart, et l'espèce de chaque rôle.

**Arrêt n° 15** (`ArretMesureNA15`) : le calcul est refusé tant que la clôture ne dit pas trois générations complètes ou un
arrêt nommé, tant que l'attestation ou les étiquettes manquent ou ne sont pas scellées, et toute seconde lecture est
refusée. La lecture est **consignée avant le calcul** par un témoin écrit sans écrasement (`lecture-unique-…`) : une
lecture qui échouerait en route a été faite, et ne se refait pas (lettre de la V9, l. 315).

**Deux lectures de chaque mesure** (P10) : la *lecture scellée* (toutes les fiches rendues de la génération, celles qu'un
modèle de repli a fait rendre comprises, rangées à part par modèle servi dans les décompositions par espèce), et la lecture
*« espèces seules »* (sans aucune ligne de rang de repli non nul), descriptive. Plus la mesure neuve « replis ».

**Tentatives et fiches** (interface et son erratum 1) : le registre porte des lignes `type_ligne` = `tentative` (une par
envoi, avec son coût et sa classe d'issue) et `fiche` ; **seules les lignes de fiche sont des fiches**. Une fiche est
rattachée à la tentative de même (génération, case, espèce demandée, rang de repli) — choix de lecture du lot 7, dit au
rapport — qui doit être unique et de classe « fiches rendues » ; sinon refus, rien n'est deviné.

Aucun message d'erreur ne recopie un énoncé, un nom ou une valeur libre. Bibliothèque standard, et `commun_na_lot7_v1`.
"""

import collections
import os

from pole import commun_na_lot7_v1 as cm

VERSION = "mesures-na-v1"

# --- formats lus (lot 6 v3 ; interface des lots 5 v2, 6 v4, 7 v1) -----------------------------------------------------
NOM_JOURNAL_ARRETS = "journal-arrets-et-generations-na-v3.jsonl"
NOM_BILAN = "bilan-course-na-v3.json"
GABARIT_REGISTRE = os.path.join("generation-{g}", "registre-tentatives-g{g}.jsonl")
NOM_TEMOIN_LECTURE = "lecture-unique-mesures-na-v1.json"
NOM_MESURES = "mesures-na-v1.json"
EVENEMENTS_LUS = ("départ", "copies de configuration", "génération", "arrêt", "clôture")
EVENEMENT_CUMUL = "cumul par clé"  # relu pour le chaînage, jeté sans lecture d'un champ
NOM_ARRET_NON_NOMME = "arrêt non nommé (défaut ou exception de base)"

PROPOSEURS = tuple(f"espece-{i}" for i in range(1, 6))
ROLES = PROPOSEURS + ("aiguilleur", "portier", "juge-1", "juge-2", "passe-x")
PASSEE, AU_COFFRE, HORS_CASE = "passée", "au coffre", "hors case"
CLASSES_FICHE = (PASSEE, AU_COFFRE, HORS_CASE)
FICHES_RENDUES = "fiches rendues"
VIDE_MOTIVEE, REFUS_DU_MODELE, ILLISIBLE = "réponse vide motivée", "refus du modèle", "réponse illisible"
REPLI_SERVI = "refus par classifieur, servi par repli"
CLASSES_ISSUE = (FICHES_RENDUES, VIDE_MOTIVEE, REFUS_DU_MODELE, ILLISIBLE, REPLI_SERVI)
CLASSES_M6 = (VIDE_MOTIVEE, REFUS_DU_MODELE, ILLISIBLE, REPLI_SERVI)
ARRET_1 = "arrêt n° 1 (trois refus de classifieur)"
RAISON_REFUS = "refusal"
SANS_REPONSE = "sans_reponse"  # erratum 1, point 3
TENTATIVE, FICHE = "tentative", "fiche"
TYPES_LIGNE = (TENTATIVE, FICHE)
CHAMPS_FERMES = ("ce_que_le_moniteur_suppose", "menace_du_programme", "etage_de_lecture")
CHAMPS_LOT5_V1 = ("identifiant", "generation", "case", "classe") + CHAMPS_FERMES + ("nom", "enonce")
CHAMPS_INTERFACE = ("type_ligne", "generation", "filiation", "espece", "case", "rang_repli", "modele_demande", "modele_servi",
                    "raison_arret", "categorie_refus", "cout_compte_usd", "classe_issue")
CHAMPS_AJOUT_SEUL = ("rang", "precedente", "version")
CHAMPS_REGISTRE = tuple(dict.fromkeys(CHAMPS_LOT5_V1 + CHAMPS_INTERFACE + CHAMPS_AJOUT_SEUL))
FILIATION_AUCUNE = ("aucune", None)
SOUS_COMPTE_CAUSE = "réponse illisible, cause non établie"  # lot 6 v3, ISSUE_ILLISIBLE_CAUSE
SOUS_COMPTE_PORTIER = "étiquette du portier illisible"     # lot 5 v1, SOUS_COMPTE_PORTIER

# --- formats de brouillon (à convenir avec la mère) --------------------------------------------------------------------
FORMAT_ATTESTATION = "attestation-relecture-na-v1"
ETIQUETTES_RELECTURE = ("gardée", "au coffre")
FORMAT_ANTERIORITE = "etiquettes-anteriorite-na-v1"
ETIQUETTES_ANTERIORITE = ("antériorité trouvée", "antériorité partielle", "non tranchée", "aucune antériorité trouvée")
NON_LUE = "non lue"
CLASSES_EPREUVE_4 = ("recette", "réalisation", "variante", "mode candidat")
BRANCHES = ("avec", "sans")
BORNE_LECTURE_ANTERIORITE = 60  # V9, section « Seuil »
SANS_OBJET = "sans objet"
AXE_AUTRE = 5  # V9, plan d'analyse : la valeur 5 du premier axe est « autre, à nommer »
BORNES_AXES = (6, 5, 4)
CASES_PAR_GENERATION = 11


class ArretMesureNA15(RuntimeError):
    """Arrêt n° 15 de la V9 : une mesure lue trop tôt, ou une seconde fois ; la lecture est refusée, consignée."""

    numero = 15
    nom = "mesure lue trop tôt"

    def __init__(self, cause):
        super().__init__(f"arrêt n° 15, {self.nom} : {cause} ; nœud de Lazar")
        self.cause = cause


class MesuresRefusees(RuntimeError):
    """Une entrée incohérente ou hors de sa forme : rien n'est calculé, rien n'est réparé ; aucun contenu recopié."""


# --- lectures --------------------------------------------------------------------------------------------------------

def _int_pos(v):
    return type(v) is int and v >= 0


def _part(num, den):
    return {"numerateur": num, "denominateur": den}


def lire_cloture(sortie):
    """Le journal des arrêts et des générations, scellé : rend (lignes de génération {g: ligne}, clôture). Les lignes
    « cumul par clé » sont jetées sans lecture d'un champ."""
    lignes = cm.relire_ajout_seul(os.path.join(sortie, NOM_JOURNAL_ARRETS), exiger_sceau=True)
    generations, cloture = {}, None
    for l in lignes:
        ev = l.get("evenement")
        if ev == EVENEMENT_CUMUL:
            continue
        if ev not in EVENEMENTS_LUS:
            raise MesuresRefusees("journal des arrêts : événement hors de la liste fermée")
        if ev == "génération":
            g = l.get("generation")
            if g not in (1, 2, 3) or g in generations or not isinstance(l.get("ligne"), dict):
                raise MesuresRefusees("journal des arrêts : ligne de génération mal formée ou redite")
            generations[g] = l["ligne"]
        elif ev == "clôture":
            if cloture is not None:
                raise MesuresRefusees("journal des arrêts : deux clôtures")
            cloture = l.get("cloture")
    if not isinstance(cloture, dict) or not _int_pos(cloture.get("generations_completes")):
        raise ArretMesureNA15("la clôture de la course est absente ou illisible")
    n = cloture["generations_completes"]
    if n > 3 or sorted(generations) != list(range(1, n + 1)):
        raise MesuresRefusees("journal des arrêts : les lignes de génération ne sont pas celles des générations complètes")
    return generations, cloture


def etat_de_la_course(sortie):
    """Ce que la clôture permet de lire (arrêt n° 15, premier temps) : trois générations complètes, ou un arrêt nommé."""
    generations, cloture = lire_cloture(sortie)
    try:
        bilan = cm.lire_json_scelle(os.path.join(sortie, NOM_BILAN))
    except cm.ScelleRefuse as e:
        raise ArretMesureNA15(f"bilan de course absent ou non scellé ({e})") from None
    n, arret = cloture["generations_completes"], cloture.get("arret")
    if not isinstance(bilan, dict) or bilan.get("arret") != arret or not isinstance(bilan.get("generations"), list) \
            or len(bilan["generations"]) != n:
        raise MesuresRefusees("le bilan et la clôture du journal ne disent pas la même chose")
    if arret is None:
        if n != 3:
            raise ArretMesureNA15(f"bilan à {n} génération(s) complète(s) sans arrêt nommé")
        titre = "course complète, trois générations"
    else:
        nom = arret.get("nom") if isinstance(arret, dict) else None
        if type(nom) is not str or not nom or nom == NOM_ARRET_NON_NOMME:
            raise ArretMesureNA15(f"bilan à {n} génération(s) complète(s), arrêt sans nom")
        titre = f"course arrêtée par {nom}"
    return {"generations_completes": n, "arret": arret, "titre": titre, "lignes_generation": generations}


def lire_registres(sortie, n):
    """Les registres des tentatives des générations 1 à n, scellés, aux seuls champs permis ; rend {g: lignes}."""
    rendu = {}
    for g in range(1, n + 1):
        lignes = cm.relire_ajout_seul(os.path.join(sortie, GABARIT_REGISTRE.format(g=g)), exiger_sceau=True)
        for l in lignes:
            _verifier_ligne_registre(l, g)
        rendu[g] = lignes
    return rendu


def _verifier_ligne_registre(l, g):
    """Une ligne du registre (interface et son erratum 1) : `type_ligne` ∈ {tentative, fiche} ; champs fermés."""
    if set(l) - set(CHAMPS_REGISTRE):
        raise MesuresRefusees(f"registre de la génération {g} : champ hors de la liste fermée")
    if l.get("type_ligne") not in TYPES_LIGNE:
        raise MesuresRefusees(f"registre de la génération {g} : `type_ligne` hors de {{tentative, fiche}}")
    if l.get("generation") != g:
        raise MesuresRefusees(f"registre de la génération {g} : ligne d'une autre génération")
    if l.get("espece") not in ROLES:
        raise MesuresRefusees(f"registre de la génération {g} : espèce demandée hors de la liste fermée")
    if l.get("rang_repli") not in (0, 1, 2):
        raise MesuresRefusees(f"registre de la génération {g} : rang de repli hors de 0, 1, 2")
    if l.get("case") is not None and type(l["case"]) is not str:
        raise MesuresRefusees(f"registre de la génération {g} : case mal formée")
    if l.get("modele_servi") is not None and type(l["modele_servi"]) is not str:
        raise MesuresRefusees(f"registre de la génération {g} : modèle servi mal formé")
    if l["type_ligne"] == TENTATIVE:
        if "classe" in l or "identifiant" in l:
            raise MesuresRefusees(f"registre de la génération {g} : une ligne de tentative ne porte pas de fiche")
        if l.get("classe_issue") not in CLASSES_ISSUE:
            raise MesuresRefusees(f"registre de la génération {g} : classe d'issue hors de la liste fermée")
        c = l.get("cout_compte_usd")
        if type(c) not in (int, float) or isinstance(c, bool) or c < 0 or c != c:
            raise MesuresRefusees(f"registre de la génération {g} : coût compté mal formé")
        if type(l.get("modele_demande")) is not str or not l["modele_demande"]:
            raise MesuresRefusees(f"registre de la génération {g} : modèle demandé absent")
        if l.get("raison_arret") == SANS_REPONSE and l.get("modele_servi") is not None:
            raise MesuresRefusees(f"registre de la génération {g} : tentative sans réponse avec un modèle servi")
    else:
        if l.get("classe") not in CLASSES_FICHE or type(l.get("identifiant")) is not str or l["espece"] not in PROPOSEURS \
                or type(l.get("case")) is not str:
            raise MesuresRefusees(f"registre de la génération {g} : ligne de fiche mal formée")


def tentatives(lignes):
    """Une tentative par ligne de tentative ; chaque ligne de fiche est rattachée à la tentative de même (génération,
    case, espèce demandée, rang de repli), qui doit être unique et de classe « fiches rendues ». Rend une liste de
    dictionnaires {espece, case, rang, modele_demande, modele_servi, raison_arret, categorie, cout, classe_issue, fiches}.
    Seules les lignes de fiche sont des fiches (erratum 1, point 4)."""
    rendu, index = [], {}
    for l in lignes:
        if l["type_ligne"] != TENTATIVE:
            continue
        t = {"generation": l["generation"], "espece": l["espece"], "case": l.get("case"), "rang": l["rang_repli"],
             "modele_demande": l["modele_demande"], "modele_servi": l.get("modele_servi"),
             "raison_arret": l.get("raison_arret"), "categorie": l.get("categorie_refus"),
             "cout": float(l["cout_compte_usd"]), "classe_issue": l["classe_issue"], "fiches": []}
        rendu.append(t)
        if l["espece"] in PROPOSEURS:
            cle = (l["generation"], l.get("case"), l["espece"], l["rang_repli"])
            if cle in index:
                raise MesuresRefusees("deux tentatives d'un même proposeur, à la même case et au même rang")
            index[cle] = t
    vus = set()
    for l in lignes:
        if l["type_ligne"] != FICHE:
            continue
        t = index.get((l["generation"], l["case"], l["espece"], l["rang_repli"]))
        if t is None or t["classe_issue"] != FICHES_RENDUES:
            raise MesuresRefusees("une ligne de fiche sans sa tentative « fiches rendues »")
        if l["identifiant"] in vus:
            raise MesuresRefusees("une fiche redite au registre")
        vus.add(l["identifiant"])
        t["fiches"].append(l)
    return rendu

def lire_attestation(chemin, empreinte_attendue=None):
    try:
        a = cm.lire_json_scelle(chemin, empreinte_attendue)
    except cm.ScelleRefuse as e:
        raise ArretMesureNA15(f"attestation de relecture absente ou non scellée ({e})") from None
    if not isinstance(a, dict) or a.get("format") != FORMAT_ATTESTATION or not isinstance(a.get("etiquettes"), dict) \
            or set(a) != {"format", "etiquettes"}:
        raise MesuresRefusees("attestation de relecture hors de sa forme")
    if not all(type(k) is str and v in ETIQUETTES_RELECTURE for k, v in a["etiquettes"].items()):
        raise MesuresRefusees("attestation de relecture : étiquette hors de la liste fermée")
    return a["etiquettes"]


def lire_anteriorite(chemin, empreinte_attendue=None):
    try:
        a = cm.lire_json_scelle(chemin, empreinte_attendue)
    except cm.ScelleRefuse as e:
        raise ArretMesureNA15(f"étiquettes d'antériorité absentes ou non scellées ({e})") from None
    if not isinstance(a, dict) or a.get("format") != FORMAT_ANTERIORITE or a.get("branche") not in BRANCHES:
        raise MesuresRefusees("étiquettes d'antériorité hors de leur forme")
    attendus = {"format", "branche", "etiquettes", "temoins"} | ({"classes", "desaccords"} if a["branche"] == "avec" else set())
    if set(a) != attendus or not isinstance(a["etiquettes"], dict) or not isinstance(a["temoins"], dict):
        raise MesuresRefusees("étiquettes d'antériorité : champs hors de leur forme")
    if not all(type(k) is str and v in ETIQUETTES_ANTERIORITE + (NON_LUE,) for k, v in a["etiquettes"].items()):
        raise MesuresRefusees("étiquettes d'antériorité : étiquette hors de la liste fermée")
    if not all(type(k) is str and v in ETIQUETTES_ANTERIORITE + CLASSES_EPREUVE_4 + ("passée", "manqué")
               for k, v in a["temoins"].items()):
        raise MesuresRefusees("étiquettes d'antériorité : issue de témoin hors de la liste fermée")
    if a["branche"] == "avec":
        if not isinstance(a["classes"], dict) or not all(v in CLASSES_EPREUVE_4 for v in a["classes"].values()) \
                or not _int_pos(a["desaccords"]):
            raise MesuresRefusees("étiquettes d'antériorité, branche « avec » : classes ou désaccords hors de leur forme")
    return a


# --- garde de l'arrêt n° 15 ---------------------------------------------------------------------------------------------

def garde_15(sortie, chemin_attestation, chemin_anteriorite, empreinte_attestation=None, empreinte_anteriorite=None):
    """Arrêt n° 15, avant tout calcul : clôture, attestation, étiquettes, lecture unique. Rend ce qui a été vérifié."""
    if os.path.exists(os.path.join(sortie, NOM_TEMOIN_LECTURE)):
        raise ArretMesureNA15("seconde lecture des mesures")
    etat = etat_de_la_course(sortie)
    attestation = lire_attestation(chemin_attestation, empreinte_attestation)
    anteriorite = lire_anteriorite(chemin_anteriorite, empreinte_anteriorite)
    return etat, attestation, anteriorite


def _consigner_lecture(sortie, entrees):
    chemin = os.path.join(sortie, NOM_TEMOIN_LECTURE)
    try:
        cm.ecrire_json_scelle(chemin, {"version": VERSION, "lecture": "unique", "entrees": entrees})
    except (cm.ScelleRefuse, FileExistsError):
        raise ArretMesureNA15("seconde lecture des mesures") from None


# --- calculs ----------------------------------------------------------------------------------------------------------

def _rangs(lecture):
    return (0, 1, 2) if lecture == "scellée" else (0,)


def _rubrique(t):
    """La ligne d'une décomposition par espèce : l'espèce demandée au rang 0 ; « servies par repli : <modèle> » sinon."""
    return t["espece"] if t["rang"] == 0 else f"servies par repli : {t['modele_servi']}"


def mesure_m3(tents, cases, lecture):
    par_case = {c: {"rendues": 0, AU_COFFRE: 0, HORS_CASE: 0} for c in cases}
    for t in tents:
        if t["rang"] not in _rangs(lecture):
            continue
        for f in t["fiches"]:
            if f["case"] not in par_case:
                raise MesuresRefusees("fiche d'une case qui n'est pas servie à sa génération")
            par_case[f["case"]]["rendues"] += 1
            if f["classe"] in (AU_COFFRE, HORS_CASE):
                par_case[f["case"]][f["classe"]] += 1
    tot = {k: sum(d[k] for d in par_case.values()) for k in ("rendues", AU_COFFRE, HORS_CASE)}
    return {"par_case": {c: {"au_coffre": _part(d[AU_COFFRE], d["rendues"]), "hors_case": _part(d[HORS_CASE], d["rendues"])}
                         for c, d in par_case.items()},
            "generation": {"au_coffre": _part(tot[AU_COFFRE], tot["rendues"]),
                           "hors_case": _part(tot[HORS_CASE], tot["rendues"])}}


def classe_de_chaine(chaine):
    """La classe d'un appel de proposeur à l'espèce demandée (P12 ; erratum 1) : la tentative de rang 0 si elle n'est pas
    refusée par un classifieur ; sinon « servi par repli » si une tentative de repli est servie ; l'arrêt n° 1 si la
    chaîne finit au rang 2 sur un refus ; sinon la classe de la dernière tentative (erreur sans réponse en repli)."""
    chaine = sorted(chaine, key=lambda t: t["rang"])
    if [t["rang"] for t in chaine] != list(range(len(chaine))):
        raise MesuresRefusees("chaîne de repli à rang manquant")
    t0 = chaine[0]
    if t0["raison_arret"] != RAISON_REFUS:
        if len(chaine) > 1:
            raise MesuresRefusees("un repli sans refus de classifieur à la tentative précédente")
        return t0["classe_issue"]
    servies = [t for t in chaine[1:] if t["raison_arret"] not in (RAISON_REFUS, SANS_REPONSE)]
    if servies:
        if t0["classe_issue"] != REPLI_SERVI:
            raise MesuresRefusees("chaîne servie par repli dont le rang 0 ne porte pas la classe du repli")
        return REPLI_SERVI
    der = chaine[-1]
    if der["rang"] == 2 and der["raison_arret"] == RAISON_REFUS:
        return ARRET_1
    return der["classe_issue"]


def mesure_m6(tents, cases):
    """Par case et par espèce demandée, chaque appel compté une fois (sa chaîne) ; « arrêt n° 1 » à part."""
    grille = {c: {e: {k: 0 for k in CLASSES_M6 + (ARRET_1,)} for e in PROPOSEURS} for c in cases}
    chaines = collections.defaultdict(list)
    for t in tents:
        if t["espece"] in PROPOSEURS:
            if t["case"] not in grille:
                raise MesuresRefusees("appel de proposeur d'une case qui n'est pas servie à sa génération")
            chaines[(t["case"], t["espece"])].append(t)
    for (c, e), ch in chaines.items():
        k = classe_de_chaine(ch)
        if k in grille[c][e]:
            grille[c][e][k] += 1
    return grille


def mesure_m4(tents, especes_des_roles):
    par_role, par_espece, replis = collections.defaultdict(float), collections.defaultdict(float), {}
    for t in tents:
        if t["rang"] == 0:
            par_role[t["espece"]] += t["cout"]
            e = especes_des_roles[t["espece"]]
            if e is not None:
                par_espece[str(e)] += t["cout"]
        else:
            r = replis.setdefault(t["modele_demande"], {"cout_usd": 0.0, "tentatives": 0, "fiches": 0})
            r["cout_usd"] += t["cout"]
            r["tentatives"] += 1
            r["fiches"] += len(t["fiches"])
    arr = lambda d: {k: round(v, 6) for k, v in sorted(d.items())}
    for r in replis.values():
        r["cout_usd"] = round(r["cout_usd"], 6)
    return {"cout_par_role_usd": arr(par_role), "cout_par_espece_usd": arr(par_espece), "replis": dict(sorted(replis.items()))}


def mesure_replis(tents_par_g):
    lignes = collections.Counter()
    couts, fiches = collections.defaultdict(float), collections.Counter()
    for g, tents in tents_par_g.items():
        for t in tents:
            if t["rang"] == 0 and t["raison_arret"] != RAISON_REFUS:
                continue
            cle = (t["espece"], t["rang"], t["modele_demande"], str(t["modele_servi"]),
                   "non lue" if t["categorie"] is None else str(t["categorie"]), t["classe_issue"])
            lignes[cle] += 1
            couts[cle] += t["cout"]
            fiches[cle] += len(t["fiches"])
    return [{"role": k[0], "rang": k[1], "modele_demande": k[2], "modele_servi": k[3], "categorie": k[4], "issue": k[5],
             "tentatives": n, "cout_usd": round(couts[k], 6), "fiches": fiches[k]} for k, n in sorted(lignes.items())]


def _verifier_especes(especes_des_roles, tents_par_g):
    if not isinstance(especes_des_roles, dict):
        raise MesuresRefusees("l'espèce de chaque rôle est donnée par la configuration")
    for r in PROPOSEURS:
        if especes_des_roles.get(r) != int(r.split("-")[1]):
            raise MesuresRefusees("l'espèce d'un proposeur est son numéro")
    for tents in tents_par_g.values():
        for t in tents:
            if t["espece"] not in especes_des_roles:
                raise MesuresRefusees("un rôle présent au registre sans espèce dite par la configuration")
            e = especes_des_roles[t["espece"]]
            if e is not None and e not in (1, 2, 3, 4, 5):
                raise MesuresRefusees("un rôle présent au registre sans espèce dite par la configuration")


def calculer(etat, registres, attestation, anteriorite, *, axes_des_cases, famille_tenue, especes_des_roles):
    """Toutes les mesures, sur les seules générations complètes. Fonction pure : n'écrit rien."""
    n = etat["generations_completes"]
    lignes_g = etat["lignes_generation"]
    cases_g = {}
    for g in range(1, n + 1):
        cs = lignes_g[g].get("cases_servies")
        if not isinstance(cs, list) or not all(type(c) is str for c in cs):
            raise MesuresRefusees("ligne de génération : cases servies mal formées")
        cases_g[g] = cs
    tents_par_g = {g: tentatives(registres[g]) for g in range(1, n + 1)}
    _verifier_especes(especes_des_roles, tents_par_g)

    # cohérence avec la ligne de la génération (garde du coffre du lot 6 : même registre)
    for g in range(1, n + 1):
        rendues = sum(len(t["fiches"]) for t in tents_par_g[g])
        coffre = lignes_g[g].get("coffre", {})
        if coffre.get("rendues") != rendues or coffre.get("au_coffre") != sum(
                1 for t in tents_par_g[g] for f in t["fiches"] if f["classe"] == AU_COFFRE):
            raise MesuresRefusees(f"génération {g} : le registre et la ligne de la génération ne comptent pas les mêmes fiches")

    fiches = {g: [(t, f) for t in tents_par_g[g] for f in t["fiches"]] for g in tents_par_g}
    passees = {f["identifiant"]: (g, t, f) for g in fiches for t, f in fiches[g] if f["classe"] == PASSEE}
    if set(attestation) != set(passees):
        raise MesuresRefusees("l'attestation de relecture ne porte pas exactement les fiches passées des générations complètes")
    gardees = [i for i in passees if attestation[i] == "gardée"]

    rendu = {"version": VERSION, "titre": etat["titre"], "generations_completes": n,
             "arret": None if etat["arret"] is None else {"numero": etat["arret"].get("numero"), "nom": etat["arret"].get("nom")},
             "lectures": {}}

    for lecture in ("scellée", "espèces seules"):
        L = {}
        # M1, M1 bis, M2
        if n < 2:
            L["M1"] = L["M1_bis"] = L["M2"] = SANS_OBJET
        else:
            num = den = bis = 0
            par_g, par_esp, parents = {}, {}, collections.Counter()
            for g in range(2, n + 1):
                registre_servi = {f["identifiant"] for gg in range(1, g) for t, f in fiches[gg]
                                  if f["classe"] == PASSEE and (lecture == "scellée" or t["rang"] == 0)}
                ls = lignes_g[g].get("registre_servi")
                if lecture == "scellée" and isinstance(ls, dict) and ls.get("lignes_tentative") != len(registre_servi):
                    raise MesuresRefusees(f"génération {g} : le registre servi n'a pas le nombre de lignes de tentative attendu")
                pn = pd = 0
                for i in gardees:
                    gg, t, f = passees[i]
                    if gg != g or t["rang"] not in _rangs(lecture):
                        continue
                    rub = _rubrique(t)
                    e = par_esp.setdefault(rub, [0, 0])
                    pd += 1
                    e[1] += 1
                    fil = f.get("filiation")
                    if fil in registre_servi:
                        pn += 1
                        e[0] += 1
                        parents[fil] += 1
                    elif fil not in FILIATION_AUCUNE:
                        bis += 1
                par_g[str(g)] = _part(pn, pd)
                num, den = num + pn, den + pd
            L["M1"] = {"part": _part(num, den), "par_generation": par_g,
                       "par_espece": {k: _part(*v) for k, v in sorted(par_esp.items())}}
            L["M1_bis"] = bis
            total = sum(parents.values())
            L["M2"] = {"parentes_distinctes": len(parents),
                       "part_vers_la_plus_citee": _part(max(parents.values()) if parents else 0, total),
                       "parentes": sorted(parents)}
        # M3, M6, M4
        L["M3"] = {str(g): mesure_m3(tents_par_g[g], cases_g[g], lecture) for g in range(1, n + 1)}
        rendu["lectures"][lecture] = L
        # M7
        m7 = {"autre, à nommer": [0, 0], "autres cases": [0, 0]}
        for g in range(1, n + 1):
            for c, d in L["M3"][str(g)]["par_case"].items():
                ax = axes_des_cases.get(c)
                if ax is None:
                    raise MesuresRefusees("case servie sans ses axes au tirage")
                k = "autre, à nommer" if ax[0] == AXE_AUTRE else "autres cases"
                m7[k][0] += d["hors_case"]["numerateur"]
                m7[k][1] += d["hors_case"]["denominateur"]
        L["M7"] = {k: _part(*v) for k, v in m7.items()}

    rendu["M3_relecture_au_coffre"] = sum(1 for i in passees if attestation[i] == "au coffre")
    rendu["M4"] = {str(g): mesure_m4(tents_par_g[g], especes_des_roles) for g in range(1, n + 1)}
    for g in range(1, n + 1):
        tot = sum(t["cout"] for t in tents_par_g[g] if t["rang"] == 0 and especes_des_roles[t["espece"]] is not None)
        par_e = rendu["M4"][str(g)]["cout_par_espece_usd"]
        rendu["M4"][str(g)]["part_du_cout_par_espece"] = {e: {"usd": v, "total_usd": round(tot, 6)} for e, v in par_e.items()}
        pas = collections.Counter(_rubrique(t) for t in tents_par_g[g] for f in t["fiches"] if f["classe"] == PASSEE)
        rendu["M4"][str(g)]["part_des_fiches_passees"] = {k: _part(v, sum(pas.values())) for k, v in sorted(pas.items())}
        cg = lignes_g[g].get("cout_generation_usd")
        somme = round(sum(t["cout"] for t in tents_par_g[g]), 6)
        rendu["M4"][str(g)]["controle_cout_generation"] = {
            "somme_des_tentatives_usd": somme, "ligne_de_generation_usd": cg,
            "ecart_usd": None if type(cg) not in (int, float) else round(somme - cg, 6)}
    rendu["M6"] = {str(g): mesure_m6(tents_par_g[g], cases_g[g]) for g in range(1, n + 1)}
    rendu["M6_sous_comptes"] = {}
    for g in range(1, n + 1):
        lg = lignes_g[g]
        issues = (lg.get("comptes_lot_6") or {}).get("issues_proposeur") or {}
        portier = ((lg.get("comptes_portier_lot_5") or {}).get("sous_comptes_reponse_illisible") or {})
        cause = {r: d.get(SOUS_COMPTE_CAUSE, 0) for r, d in sorted(issues.items())}
        if not all(_int_pos(v) for v in cause.values()) or not _int_pos(portier.get(SOUS_COMPTE_PORTIER, 0)):
            raise MesuresRefusees("ligne de génération : sous-comptes de M6 mal formés")
        rendu["M6_sous_comptes"][str(g)] = {"cause non établie, par rôle": cause,
                                            SOUS_COMPTE_PORTIER: portier.get(SOUS_COMPTE_PORTIER, 0)}
    rendu["replis"] = mesure_replis(tents_par_g)

    # M5
    lues = {i: v for i, v in anteriorite["etiquettes"].items() if v != NON_LUE}
    if set(anteriorite["etiquettes"]) != set(gardees):
        raise MesuresRefusees("les étiquettes d'antériorité ne portent pas exactement les fiches gardées à la relecture")
    if len(lues) > BORNE_LECTURE_ANTERIORITE:
        raise MesuresRefusees("plus de fiches lues que la borne de lecture d'antériorité")
    m5 = {"par_etiquette": {e: sum(1 for v in lues.values() if v == e) for e in ETIQUETTES_ANTERIORITE},
          "non_lues": len(gardees) - len(lues), "temoins": dict(sorted(anteriorite["temoins"].items())),
          "branche": anteriorite["branche"]}
    if anteriorite["branche"] == "avec":
        if set(anteriorite["classes"]) != set(lues):
            raise MesuresRefusees("branche « avec » : une classe par fiche lue, et pour elles seules")
        m5["par_classe"] = {k: sum(1 for v in anteriorite["classes"].values() if v == k) for k in CLASSES_EPREUVE_4}
        m5["desaccords"] = anteriorite["desaccords"]
    rendu["M5"] = m5

    # C1
    servies = [c for g in range(1, n + 1) for c in cases_g[g]]
    for c in servies:
        ax = axes_des_cases.get(c)
        if not isinstance(ax, (list, tuple)) or len(ax) != 3 or not all(type(a) is int and 0 <= a < b
                                                                          for a, b in zip(ax, BORNES_AXES)):
            raise MesuresRefusees("axes d'une case hors de leurs bornes")
    if type(famille_tenue) is not int or not 0 <= famille_tenue <= 4:
        raise MesuresRefusees("famille tenue à l'écart : un entier de 0 à 4")
    rendu["C1"] = {"aucune_case_servie_deux_fois": len(set(servies)) == len(servies),
                   "cases_servies": len(servies), "cases_attendues": CASES_PAR_GENERATION * n,
                   "trente_trois_cases_servies": len(servies) == 33,
                   "aucune_case_de_la_famille_tenue_a_l_ecart": all(axes_des_cases[c][0] != famille_tenue for c in servies)}
    # I1
    rendu["I1"] = {"titre": "pour information", "par_generation": {}}
    for g in range(1, n + 1):
        c6 = lignes_g[g].get("comptes_lot_6") or {}
        i1 = {"fiches_jugees": c6.get("fiches_jugees", 0), "appels_juge": dict(sorted((c6.get("appels_juge") or {}).items())),
              "verdicts_absents": {k: dict(sorted(v.items())) for k, v in sorted((c6.get("verdicts_absents") or {}).items())}}
        if not _int_pos(i1["fiches_jugees"]) or not all(_int_pos(v) for v in i1["appels_juge"].values()) \
                or not all(_int_pos(x) for v in i1["verdicts_absents"].values() for x in v.values()):
            raise MesuresRefusees("ligne de génération : comptes des juges mal formés")
        rendu["I1"]["par_generation"][str(g)] = i1
    rendu["identifiants"] = {"cases": servies, "fiches_gardees": sorted(gardees),
                             "temoins": sorted(anteriorite["temoins"])}
    return rendu


# --- la lecture unique ------------------------------------------------------------------------------------------------

def lire_mesures(sortie, chemin_attestation, chemin_anteriorite, *, axes_des_cases, famille_tenue, especes_des_roles,
                 empreinte_attestation=None, empreinte_anteriorite=None):
    """La lecture unique des mesures (V9, l. 315) : garde n° 15, consignation, calcul, écriture scellée dans la sortie.
    Rend les mesures."""
    etat, attestation, anteriorite = garde_15(sortie, chemin_attestation, chemin_anteriorite,
                                              empreinte_attestation, empreinte_anteriorite)
    n = etat["generations_completes"]
    entrees = {"journal_arrets": cm.sha256_fichier(os.path.join(sortie, NOM_JOURNAL_ARRETS)),
               "bilan": cm.sha256_fichier(os.path.join(sortie, NOM_BILAN)),
               "attestation": cm.sha256_fichier(chemin_attestation),
               "anteriorite": cm.sha256_fichier(chemin_anteriorite)}
    for g in range(1, n + 1):
        entrees[f"registre_g{g}"] = cm.sha256_fichier(os.path.join(sortie, GABARIT_REGISTRE.format(g=g)))
    _consigner_lecture(sortie, entrees)
    registres = lire_registres(sortie, n)
    mesures = calculer(etat, registres, attestation, anteriorite, axes_des_cases=axes_des_cases,
                       famille_tenue=famille_tenue, especes_des_roles=especes_des_roles)
    mesures["empreintes_des_entrees"] = entrees
    cm.ecrire_json_scelle(os.path.join(sortie, NOM_MESURES), mesures)
    return mesures
