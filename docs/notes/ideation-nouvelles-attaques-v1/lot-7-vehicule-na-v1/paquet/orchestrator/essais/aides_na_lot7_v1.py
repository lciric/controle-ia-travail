"""Aides des essais du lot 7 : une sortie de course factice, aux formats du lot 6 v3 et de l'interface des lots 5 v2,
6 v4 et 7 v1. Données inertes : aucun texte d'idée, aucun nom de modèle, aucune valeur de clé ; les noms d'usage des clés
sont des noms d'essai (`CLE-ESSAI-…`), non ceux de la course."""

import copy
import json
import os

from pole import commun_na_lot7_v1 as cm
from pole import mesures_na_v1 as ms

MARQUEUR = "MARQUEUR-INERTE-LOT7-7f3a"  # planté dans chaque énoncé, nom, case différente, filiation invalide
NOMS_CLES_ESSAI = ("CLE-ESSAI-ALPHA", "CLE-ESSAI-BETA", "CLE-ESSAI-GAMMA")
CHAMPS_CUMUL = ("cumul_par_cle", "cause_non_etablie_par_cle", "etat_relais_illisible_par_cle")
ESPECES_DES_ROLES = {"espece-1": 1, "espece-2": 2, "espece-3": 3, "espece-4": 4, "espece-5": 5,
                     "aiguilleur": 4, "portier": 4, "juge-1": 1, "juge-2": 3, "passe-x": None}
FAMILLE_TENUE = 0


class JournalArretsEssai(cm.FichierAjoutSeul):
    CHAMPS_PERMIS = ("evenement", "generation", "depart", "copies", "arret", "ligne", "cles", "cloture")
    VERSION = "journal-arrets-et-generations-na-v3"


class RegistreEssai(cm.FichierAjoutSeul):
    CHAMPS_PERMIS = tuple(c for c in ms.CHAMPS_REGISTRE if c not in ("rang", "precedente", "version"))
    VERSION = "registre-tentatives-na-v2-essai"


def ident_case(g, k):
    return f"case{g}x{k:02d}"


def axes():
    """Les axes des 33 cases : premier axe de 1 à 5 (jamais la famille 0), trois cases à « autre, à nommer »."""
    rendu, n = {}, 0
    for g in (1, 2, 3):
        for k in range(11):
            a = 5 if k == 0 else 1 + (n % 4)
            rendu[ident_case(g, k)] = [a, n % 5, n % 4]
            n += 1
    return rendu


def _fiche_ligne(g, case, espece, rang, ident, classe, filiation, modele_servi):
    l = {"type_ligne": "fiche", "generation": g, "case": case, "espece": espece, "rang_repli": rang,
         "modele_servi": modele_servi, "identifiant": ident, "classe": classe, "filiation": filiation}
    if classe == ms.PASSEE:
        l.update({"ce_que_le_moniteur_suppose": "v-a", "menace_du_programme": "v-b", "etage_de_lecture": "v-c",
                  "nom": ident, "enonce": f"énoncé inerte {MARQUEUR} {ident}"})
    return l


def _appel_ligne(g, case, espece, rang, classe_issue, cout, raison="end_turn", modele_servi=None, cat=None):
    return {"type_ligne": "tentative", "generation": g, "case": case, "espece": espece, "rang_repli": rang,
            "modele_demande": f"id-{espece}-r{rang}",
            "modele_servi": None if raison == "sans_reponse" else (modele_servi or f"id-{espece}-r{rang}"), "raison_arret": raison, "categorie_refus": cat,
            "cout_compte_usd": cout, "classe_issue": classe_issue, "filiation": None}


def lignes_de_generation(g, passees_avant):
    """Les lignes du registre de la génération g et l'attendu calculé à la main (pour les essais)."""
    lignes, attendu = [], {"rendues": 0, "au_coffre": 0, "hors_case": 0, "passees": [], "repli_fiches": 0,
                           "cout": 0.0, "cout_rang0_par_role": {}, "m6": {}}
    for k in range(11):
        case = ident_case(g, k)
        for e in ms.PROPOSEURS:
            n_esp = int(e[-1])
            ident = f"f{g}{k:02d}{n_esp}"
            if e == "espece-2" and k == 1:  # réponse vide motivée
                lignes.append(_appel_ligne(g, case, e, 0, ms.VIDE_MOTIVEE, 0.5))
                attendu["m6"][(case, e, ms.VIDE_MOTIVEE)] = 1
                attendu["cout"] += 0.5
                attendu["cout_rang0_par_role"][e] = attendu["cout_rang0_par_role"].get(e, 0) + 0.5
                continue
            if e == "espece-3" and k == 2:  # chaîne de repli servie : rang 0 refusé, rang 1 fiche passée
                lignes.append(_appel_ligne(g, case, e, 0, ms.REPLI_SERVI, 0.25, raison="refusal", cat="cyber"))
                lignes.append(_appel_ligne(g, case, e, 1, ms.FICHES_RENDUES, 0.75, modele_servi="id-repli-1"))
                lignes.append(_fiche_ligne(g, case, e, 1, ident + "r", ms.PASSEE, None, "id-repli-1"))
                attendu["m6"][(case, e, ms.REPLI_SERVI)] = 1
                attendu["rendues"] += 1
                attendu["repli_fiches"] += 1
                attendu["passees"].append((ident + "r", 1))
                attendu["cout"] += 1.0
                attendu["cout_rang0_par_role"][e] = attendu["cout_rang0_par_role"].get(e, 0) + 0.25
                continue
            if e == "espece-4" and k == 3:  # trois refus : arrêt n° 1 (erratum 1 : classe « refus » au rang 2)
                for r in (0, 1, 2):
                    lignes.append(_appel_ligne(g, case, e, r, ms.REFUS_DU_MODELE, 0.1, raison="refusal"))
                attendu["m6"][(case, e, ms.ARRET_1)] = 1
                attendu["cout"] += 0.3
                attendu["cout_rang0_par_role"][e] = attendu["cout_rang0_par_role"].get(e, 0) + 0.1
                continue
            if e == "espece-5" and k == 6:  # refus, puis repli sans réponse : réponse illisible (erratum 1, point 3)
                lignes.append(_appel_ligne(g, case, e, 0, ms.ILLISIBLE, 0.1, raison="refusal"))
                lignes.append(_appel_ligne(g, case, e, 1, ms.ILLISIBLE, 6.05, raison="sans_reponse"))
                attendu["m6"][(case, e, ms.ILLISIBLE)] = 1
                attendu["cout"] += 6.15
                attendu["cout_rang0_par_role"][e] = attendu["cout_rang0_par_role"].get(e, 0) + 0.1
                continue
            # cas courant : une ou deux fiches
            classes = [ms.PASSEE]
            if k == 4 and e == "espece-1":
                classes = [ms.AU_COFFRE, ms.PASSEE]
            if k == 5 and e == "espece-5":
                classes = [ms.HORS_CASE]
            cout = 1.0
            lignes.append(_appel_ligne(g, case, e, 0, ms.FICHES_RENDUES, cout))
            for j, c in enumerate(classes):
                fid = ident + "abc"[j]
                fil = None
                if g >= 2 and c == ms.PASSEE:
                    if k % 3 == 0 and passees_avant:
                        fil = passees_avant[(k + n_esp) % len(passees_avant)]
                    elif k % 3 == 1:
                        fil = "aucune"
                    elif k == 8 and e == "espece-1":
                        fil = "filiation-invalide"
                lignes.append(_fiche_ligne(g, case, e, 0, fid, c, fil, f"id-{e}-r0"))
                attendu["rendues"] += 1
                if c == ms.AU_COFFRE:
                    attendu["au_coffre"] += 1
                elif c == ms.HORS_CASE:
                    attendu["hors_case"] += 1
                else:
                    attendu["passees"].append((fid, 0))
            attendu["cout"] += cout
            attendu["cout_rang0_par_role"][e] = attendu["cout_rang0_par_role"].get(e, 0) + cout
    # appels du portier et des juges (sans fiche) ; le juge 2 servi par repli (erratum 1, point 2)
    for role in ("portier", "juge-1", "juge-2"):
        lignes.append(_appel_ligne(g, ident_case(g, 0), role, 0, ms.FICHES_RENDUES, 0.2,
                                   raison="refusal" if role == "juge-2" else "end_turn"))
        attendu["cout"] += 0.2
        attendu["cout_rang0_par_role"][role] = attendu["cout_rang0_par_role"].get(role, 0) + 0.2
    lignes.append(_appel_ligne(g, ident_case(g, 0), "juge-2", 1, ms.FICHES_RENDUES, 0.3, modele_servi="id-repli-1"))
    attendu["cout"] += 0.3
    return lignes, attendu


def ligne_generation(g, attendu, passees_avant_scellee):
    return {"generation": g, "cases_servies": [ident_case(g, k) for k in range(11)],
            "coffre": {"au_coffre": attendu["au_coffre"], "rendues": attendu["rendues"],
                       "depasse": False, "consigne": False},
            "registre_servi": None if g == 1 else {"sha256": "0" * 64, "taille": 1, "lignes": passees_avant_scellee + 22,
                                                    "lignes_tentative": passees_avant_scellee, "lignes_compte": 22,
                                                    "comptes_permutes": False, "section": "servi",
                                                    "requetes_l_ayant_recu": 55},
            "comptes_lot_6": {"issues_proposeur": {"prop-e1": {"réponse illisible, cause non établie": 1}},
                              "fiches_jugees": 3, "appels_juge": {"juge-1": 3, "juge-2": 3},
                              "verdicts_absents": {"juge-2": {"verdict illisible": 1}}},
            "comptes_portier_lot_5": {"sous_comptes_reponse_illisible": {"étiquette du portier illisible": 2}},
            "cout_generation_usd": round(attendu["cout"], 6)}


def fabriquer_sortie(racine, *, completes=3, arret=None, cloture=True, registre_partiel=True, bilan=True,
                     muter_ligne=None):
    """Une sortie de course factice dans `racine/sortie`. `completes` : générations complètes ; `arret` : la ligne d'arrêt
    (dictionnaire) ou None. Rend (sortie, attendus {g: attendu})."""
    sortie = os.path.join(racine, "sortie")
    os.makedirs(os.path.join(sortie, "journaux"))
    j = JournalArretsEssai(sortie, ms.NOM_JOURNAL_ARRETS)
    j.ajouter({"evenement": "départ", "depart": {"version": "course-na-v3", "etat_colonne": 1}})
    j.ajouter({"evenement": "copies de configuration", "copies": {"1": "a" * 64, "2": "b" * 64, "3": "c" * 64}})
    attendus, passees_ids, lignes_bilan = {}, [], []
    jouees = completes + (1 if (arret is not None and completes < 3 and registre_partiel) else 0)
    for g in range(1, jouees + 1):
        os.makedirs(os.path.join(sortie, f"generation-{g}"))
        lignes, att = lignes_de_generation(g, list(passees_ids))
        r = RegistreEssai(os.path.join(sortie, f"generation-{g}"), f"registre-tentatives-g{g}.jsonl")
        if g > completes:  # génération arrêtée : registre partiel, scellé, d'une forme que la lecture refuserait
            r.ajouter({"type_ligne": "tentative", "generation": g, "espece": "hors-liste", "classe_issue": "inconnue",
                       "enonce": MARQUEUR})
            r.sceller()
            break
        for l in lignes:
            r.ajouter(l)
        r.sceller()
        lg = ligne_generation(g, att, len(passees_ids))
        if muter_ligne is not None:
            lg = muter_ligne(g, lg)
        attendus[g] = att
        passees_ids.extend(i for i, _ in att["passees"])
        lignes_bilan.append(lg)
        j.ajouter({"evenement": "génération", "generation": g, "ligne": lg})
        j.ajouter({"evenement": "cumul par clé", "generation": g,
                   "cles": {CHAMPS_CUMUL[0]: {n: 1.0 * g for n in NOMS_CLES_ESSAI},
                            CHAMPS_CUMUL[1]: {n: 0 for n in NOMS_CLES_ESSAI},
                            CHAMPS_CUMUL[2]: {n: 0 for n in NOMS_CLES_ESSAI}}})
    if arret is not None:
        j.ajouter({"evenement": "arrêt", "generation": completes + 1, "arret": arret})
    if cloture:
        j.ajouter({"evenement": "clôture", "cloture": {"generations_completes": completes, "arret": arret}})
    j.sceller()
    if bilan:
        cm.ecrire_json_scelle(os.path.join(sortie, ms.NOM_BILAN), {"version": "course-na-v3", "generations": lignes_bilan,
                                                                    "arret": arret})
    return sortie, attendus


def ecrire_attestation(racine, attendus, au_coffre=(), nom="attestation.json", sceller=True, retirer=()):
    et = {}
    for g, att in attendus.items():
        for i, _ in att["passees"]:
            if i in retirer:
                continue
            et[i] = "au coffre" if i in au_coffre else "gardée"
    chemin = os.path.join(racine, nom)
    objet = {"format": ms.FORMAT_ATTESTATION, "etiquettes": et}
    if sceller:
        cm.ecrire_json_scelle(chemin, objet)
    else:
        with open(chemin, "wb") as f:
            f.write(cm.octets_json(objet))
    return chemin, et


def ecrire_anteriorite(racine, gardees, branche="avec", nom="anteriorite.json", lues=10, sceller=True):
    ids = sorted(i for i, v in gardees.items() if v == "gardée")
    et = {}
    for n, i in enumerate(ids):
        et[i] = ms.ETIQUETTES_ANTERIORITE[n % 4] if n < lues else ms.NON_LUE
    objet = {"format": ms.FORMAT_ANTERIORITE, "branche": branche, "etiquettes": et,
             "temoins": {"temoin-variante": "variante", "temoin-vide": "passée"}}
    if branche == "avec":
        objet["classes"] = {i: ms.CLASSES_EPREUVE_4[n % 4] for n, i in enumerate(ids) if et[i] != ms.NON_LUE}
        objet["desaccords"] = 2
    chemin = os.path.join(racine, nom)
    if sceller:
        cm.ecrire_json_scelle(chemin, objet)
    else:
        with open(chemin, "wb") as f:
            f.write(cm.octets_json(objet))
    return chemin


def course_entiere(racine, **kw):
    """Sortie, attestation, étiquettes ; rend (sortie, attendus, chemin_attestation, chemin_anteriorite)."""
    sortie, attendus = fabriquer_sortie(racine, **kw)
    ca, et = ecrire_attestation(racine, attendus)
    cant = ecrire_anteriorite(racine, et)
    return sortie, attendus, ca, cant


def lire(sortie, ca, cant, **kw):
    params = dict(axes_des_cases=axes(), famille_tenue=FAMILLE_TENUE, especes_des_roles=dict(ESPECES_DES_ROLES))
    params.update(kw)
    return ms.lire_mesures(sortie, ca, cant, **params)


def charger_json(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def copie_profonde(o):
    return copy.deepcopy(o)
