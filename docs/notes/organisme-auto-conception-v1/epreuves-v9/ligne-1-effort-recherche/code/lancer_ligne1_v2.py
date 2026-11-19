"""Lanceur du banc A, ligne 1 (version 2 du code) : étalonnage → course décisive → rejeu du journal → analyse, dans l'ordre
des gestes du préenregistrement, chaque étape scellant sa sortie avant la suivante. Reprenable ; plafond de durée (A13).

Version 2 (contre-lecture retenue, `code-v1/contre-lecture-code-banc-a-ligne-1-v1-v1.md`) :
- correction 1 : la course décisive récupère (déplace, n'efface pas) les fichiers d'une course interrompue et porte leur
  inventaire au manifeste ;
- correction 5 : les refus ajoutés au code v1 sont isolés en fonctions éprouvées sur un cas sain et sur un artefact
  (`verifier_racines`, `exiger_code_commis`, `verifier_etalonnage_pour_decisive`) ;
- correction 6 : le manifeste du dépôt porte une empreinte de l'ensemble (`verifier_depot` la recalcule) ;
- correction 7 : le manifeste de la course décisive porte aussi les versions et le commit de l'organisme de l'étalonnage ;
- la configuration v2 porte les empreintes des fichiers du code v2 : le lanceur refuse un code qui en diffère ;
- avant toute reprise de `tout`, le lanceur refuse de partir si un processus listé dans les fichiers `pid-*.txt` du dossier
  vit encore (réserve de la première contre-lecture, constat 13) ;
- correction 8 : l'analyse (v2) scelle la lecture puis lève la garde A7 ou A11 ; `tout` relance toujours l'étape
  d'analyse, dont la reprise relève la garde (aucune « chaîne complète » sur une lecture refusée).

Préenregistrement qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`,
sha256 523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9. Le lanceur refuse de tourner si ce fichier n'a pas
cette empreinte, si la configuration n'est pas celle du code, si les fichiers de l'organisme diffèrent (A1), si le
jugement du banc diffère de `juger_carte` (A6), si le code n'est pas commis (sauf fumée).

Sous-commandes :
- `tout`       : les quatre étapes à la suite, chacune dans un processus à part (nouvelle session) ; plafond A13 (12 heures
                 de calcul cumulées sur les reprises) : arrêt par identifiant de processus (règle R10), rien n'est lu ;
- `etalonner`, `decisive`, `rejouer`, `analyser` : une étape (reprenable : une sortie déjà scellée n'est pas refaite) ;
- `empaqueter` : dépôt des journaux et sorties (fichiers compressés en morceaux ≤ 90 Mo, manifeste scellé ; au-delà de
                 500 Mo compressés : refus, à rapporter avant de pousser) ;
- `fumee`      : essai de fumée de toute la chaîne, tailles minuscules, racines disjointes de toutes celles du
                 préenregistrement ; n'imprime que des durées, des tailles et des comptes.

Commande de lancement (détachable) : voir `code-v2/commande-lancement-banc-a-ligne1-v2.md`.
"""

import argparse
import concurrent.futures
import copy
import datetime
import json
import multiprocessing
import os
import platform
import signal
import subprocess
import sys
import tarfile
import time

import banc_ligne1_v1 as B
import etalonnage_ligne1_v2 as E
import rejouer_journal_ligne1_v2 as RJ
import analyse_ligne1_v2 as AN

VERSION = "lancer-ligne1-v2"
RACINES_PREREG = (2026111900, 2026111901, 2026111902, 2026111903)
NOM_MANIFESTE = "manifeste-course-decisive-ligne1-v2.json"
NOM_DEPOT = "manifeste-depot-ligne1-v2.json"
NOM_ETAT = "etat-lancement-ligne1-v2.json"
NOM_ARRETS = "arrets-ligne1-v2.jsonl"
NOM_PID_LANCEUR = "pid-lanceur-ligne1-v2.txt"
NOM_PID_ETAPE = "pid-etape-ligne1-v2.txt"
MORCEAU_MAX = 90 * 1000 * 1000
DEPOT_MAX = 500 * 1000 * 1000
ETAPES = ("etalonner", "decisive", "rejouer", "analyser")


class GardeA13Duree(B.ArretBanc):
    pass


class GardeA14Graine(B.ArretBanc):
    pass


class DecisionMereRequise(B.ArretBanc):
    """L'étalonnage met en tête une part de cartes indéterminées au-dessus de 20 % : la mère décide avant la course décisive."""


class DepotTropGros(B.ArretBanc):
    pass


class DepotIncoherent(B.ArretBanc):
    """Un morceau, un membre ou l'empreinte de l'ensemble du dépôt diffère de son manifeste."""


class CodeDifferentDeLaConfiguration(B.ArretBanc):
    """Un fichier du code v2 n'a pas l'empreinte que porte la configuration v2."""


class RepriseConcurrente(B.ArretBanc):
    """Un processus listé dans un fichier `pid-*.txt` du dossier de sortie vit encore : aucune reprise ne part."""


# --- préparation commune -------------------------------------------------------------------------------------------------
def configuration_fumee(config):
    """Configuration de l'essai de fumée : racines disjointes de toutes celles du préenregistrement, tailles minuscules,
    tolérance de la dichotomie ouverte (un pas). Rien d'autre ne change."""
    c = copy.deepcopy(config)
    c["version"] = "configuration-ligne1-v2-fumee"
    c["racines"] = {"essais": 2026111990, "etalonnage": 2026111991, "decisive": 2026111992, "reechantillonnage": 2026111993}
    c["etalonnage"]["forces"].update(jugements_par_pas=16, tolerance=1.0)
    c["etalonnage"]["jugements_par_couple"] = 8
    c["etalonnage"]["courses_par_classe"] = 4
    c["etalonnage"]["reechantillons_prise"] = 200
    c["audit"]["reechantillons"] = 50
    c["courses_par_classe"] = 6
    c["reechantillonnage"]["reechantillons"] = 200
    c["audit_symetrie"]["courses"] = [0, 3, 5]
    return c


def verifier_racines(config, mode):
    """En mode réel, les quatre racines doivent être celles du préenregistrement ; en fumée, aucune ne doit l'être.
    Lève `ConfigurationRefusee` sinon."""
    racines = tuple(config["racines"][k] for k in ("essais", "etalonnage", "decisive", "reechantillonnage"))
    if mode == "fumee":
        if set(racines) & set(RACINES_PREREG):
            raise B.ConfigurationRefusee("fumée : une racine du préenregistrement serait dérivée : refus")
    elif racines != RACINES_PREREG:
        raise B.ConfigurationRefusee("racines différentes de celles du préenregistrement : refus")
    return True


def verifier_code_configuration(config, dossier=None):
    """Chaque fichier du code v2 (et l'essai) a l'empreinte que porte la configuration v2 ; la configuration ne se cite pas
    elle-même (son empreinte est au manifeste). Lève `CodeDifferentDeLaConfiguration` sinon."""
    dossier = dossier or B.DOSSIER_CODE
    attendues = (config.get("code") or {}).get("fichiers") or {}
    voulus = [n for n in E.FICHIERS_CODE if n != os.path.basename(E.CHEMIN_CONFIGURATION)] + list(E.FICHIERS_ESSAIS)
    if sorted(attendues) != sorted(voulus):
        raise CodeDifferentDeLaConfiguration(f"configuration : liste des fichiers du code {sorted(attendues)} ≠ {sorted(voulus)}")
    ecarts = {n: (B.sha256_fichier(os.path.join(dossier, n)) if os.path.isfile(os.path.join(dossier, n)) else None)
              for n in voulus}
    ecarts = {n: v for n, v in ecarts.items() if v != attendues[n]}
    if ecarts:
        raise CodeDifferentDeLaConfiguration(f"code différent de la configuration v2 : {ecarts} : refus avant tout tirage")
    return True


def preparer(organisme, mode):
    """Préenregistrement, configuration v2 (racines ; empreintes du code), organisme (A2, A1), jugement (A6). Rend (config,
    empreinte, provenance)."""
    prereg = B.verifier_preenregistrement()
    config, sha = B.charger_configuration(E.CHEMIN_CONFIGURATION)
    verifier_code_configuration(config)
    if mode == "fumee":
        config = configuration_fumee(config)
        sha = B.JL.empreinte(config)
    verifier_racines(config, mode)
    B.charger_organisme(organisme, config)
    B.verifier_jugement_identique(config["racines"]["essais"])
    return config, sha, prereg


def etat_code(dossier=None):
    """Commit du dépôt, propreté de l'arbre sous le dossier du code (fichiers neufs non suivis compris), empreintes des
    fichiers du code v2."""
    dossier = dossier or B.DOSSIER_CODE
    depot = subprocess.run(["git", "-C", dossier, "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if depot.returncode != 0:
        raise B.ArretBanc(f"dépôt du code introuvable (git rev-parse) sous {dossier}")
    depot = depot.stdout.strip()
    head = subprocess.run(["git", "-C", depot, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    sale = subprocess.run(["git", "-C", depot, "status", "--porcelain", "--untracked-files=all", "--", dossier],
                          capture_output=True, text=True)
    if sale.returncode != 0:
        raise B.ArretBanc(f"git status a échoué sous {dossier}")
    return {"commit": head, "arbre_propre": not sale.stdout.strip(),
            "fichiers": {n: B.sha256_fichier(os.path.join(dossier, n)) for n in E.FICHIERS_CODE}}


def exiger_code_commis(mode, dossier=None):
    """Hors fumée, refuse (`ArretBanc`) un code dont l'arbre n'est pas propre sous le dossier du code."""
    e = etat_code(dossier)
    if mode != "fumee" and not e["arbre_propre"]:
        raise B.ArretBanc("code du banc non commis (git status non vide sous code/) : refus avant tout tirage")
    return e


def _date(h):
    return datetime.datetime.fromisoformat(h.replace("Z", "+00:00"))


def verifier_derivations(premieres, horodatage_scellement, racines):
    """Garde A14 : aucune graine d'étalonnage ni décisive dérivée avant le scellement du préenregistrement."""
    seuil = _date(horodatage_scellement)
    for r in racines:
        h = premieres.get(str(r))
        if h is not None and _date(h) <= seuil:
            raise GardeA14Graine(f"garde A14 : graine de la racine {r} dérivée à {h}, avant le scellement ({horodatage_scellement}) : "
                                 "course invalide")
    return True


def fusionner_premieres(listes):
    out = {}
    for d in listes:
        for r, h in d.items():
            r = str(r)
            if r not in out or _date(h) < _date(out[r]):
                out[r] = h
    return out


# --- étapes ---------------------------------------------------------------------------------------------------------------
def dossier_etape(sortie, etape):
    return os.path.join(sortie, {"etalonner": "etalonnage", "decisive": "decisive", "rejouer": "decisive",
                                 "analyser": "decisive"}[etape])


def etape_faite(sortie, etape):
    d = dossier_etape(sortie, etape)
    nom = {"etalonner": E.NOM_SORTIE, "decisive": NOM_MANIFESTE, "rejouer": AN.NOM_REJEU, "analyser": AN.NOM_LECTURE}[etape]
    return B.verifier_scelle_fichier(os.path.join(d, nom))


def etalonner(a, config, sha, prereg, mode):
    code = exiger_code_commis(mode)
    d = dossier_etape(a.sortie, "etalonner")
    sortie = E.etalonner(d, config, sha, prereg, processus=a.processus, portes_bloquantes=(mode != "fumee"), code=code)
    if mode != "fumee":
        verifier_derivations(sortie["graines_premieres_derivations"], config["preenregistrement"]["horodatage_scellement"],
                             (config["racines"]["etalonnage"], config["racines"]["reechantillonnage"]))
    return {"etape": "etalonner", "code": code["commit"]}


def verifier_etalonnage_pour_decisive(etal, sha, code, mode):
    """Refus de la course décisive (hors fumée) : bras interdit dans l'étalonnage (A17), porte manquée ou portes non
    bloquantes, part d'indéterminées en tête (`DecisionMereRequise`), autre configuration, autre code. Rend vrai sinon."""
    E.verifier_sortie_sans_bras_interdit(etal)
    if mode == "fumee":
        return True
    if not etal.get("portes_bloquantes") or not all(p["passee"] for p in etal["portes"].values()):
        raise B.ArretBanc("course décisive : une porte de l'étalonnage est manquée : refus")
    if etal["en_tete"]:
        raise DecisionMereRequise("course décisive : " + " ; ".join(etal["en_tete"]))
    if etal["configuration_sha256"] != sha:
        raise B.ArretBanc("course décisive : étalonnage fait sous une autre configuration")
    if (etal.get("code") or {}).get("fichiers") != code["fichiers"]:
        raise B.ArretBanc("course décisive : code du banc différent de celui de l'étalonnage : refus")
    return True


_D = {}


def _course_decisive(course):
    t = time.perf_counter()
    r = B.jouer_course(course, _D["racine"], _D["P"], _D["dossier_courses"], _D["sha"], _D["prereg"])
    info = {"course": course, "premieres": dict(B.GRAINES.premieres), "secondes": time.perf_counter() - t}
    B.ecrire_json_scelle(os.path.join(_D["dossier_graines"], f"graines-c{course:04d}.json"), info)
    return info


def decisive(a, config, sha, prereg, mode):
    code = exiger_code_commis(mode)
    d = dossier_etape(a.sortie, "decisive")
    chemin_m = os.path.join(d, NOM_MANIFESTE)
    if B.verifier_scelle_fichier(chemin_m):
        return {"etape": "decisive", "reprise": "déjà scellée"}
    chemin_e = os.path.join(dossier_etape(a.sortie, "etalonner"), E.NOM_SORTIE)
    if not B.verifier_scelle_fichier(chemin_e):
        raise B.ArretBanc("course décisive : sortie de l'étalonnage absente ou non scellée")
    etal = B.lire_json_verifie(chemin_e)
    verifier_etalonnage_pour_decisive(etal, sha, code, mode)
    P = B.parametres(config, etal["parametres"]["forces_dans_l_ordre_des_roles"], etal["parametres"]["s"], etal["parametres"]["c"])
    racine = config["racines"]["decisive"]
    B.GRAINES(racine, "ouverture|decisive")
    dossier_courses, dossier_graines = os.path.join(d, "courses"), os.path.join(d, "graines")
    os.makedirs(dossier_courses, exist_ok=True)
    os.makedirs(dossier_graines, exist_ok=True)
    _D.update(racine=racine, P=P, dossier_courses=dossier_courses, dossier_graines=dossier_graines, sha=sha, prereg=prereg)
    n = config["courses_par_classe"]
    classes = tuple(config["proposeurs"]["engagements_par_appel"])
    for c in range(n):
        g = os.path.join(dossier_graines, f"graines-c{c:04d}.json")
        if os.path.exists(g) and not E.course_deja_faite(dossier_courses, c, classes):
            raise B.ArretBanc(f"reprise : graines de la course {c} présentes sans ses sorties scellées : à examiner")
    t = time.perf_counter()
    ex = (concurrent.futures.ProcessPoolExecutor(a.processus, mp_context=multiprocessing.get_context("fork"))
          if a.processus > 1 else None)
    try:
        E.jouer_courses(ex, dossier_courses, n, _course_decisive, classes)
    finally:
        if ex:
            ex.shutdown()
    mur = time.perf_counter() - t
    infos = []
    for c in range(n):
        g = os.path.join(dossier_graines, f"graines-c{c:04d}.json")
        if B.verifier_scelle_fichier(g):
            infos.append(B.lire_json_verifie(g))
        else:   # sorties scellées, processus interrompu avant l'écriture des graines : horodatages de cette course perdus, dit
            infos.append({"course": c, "premieres": {}, "secondes": 0.0, "note": "horodatages perdus à la reprise"})
    premieres = fusionner_premieres([B.GRAINES.premieres] + [i["premieres"] for i in infos])
    if mode != "fumee":
        verifier_derivations(premieres, config["preenregistrement"]["horodatage_scellement"], (racine,))
    fichiers = {}
    for c in range(n):
        for k in classes:
            for p, x in (("journal", "jsonl.xz"), ("sortie", "json.xz")):
                nom = f"{p}-c{c:04d}-{k}.{x}"
                ch = os.path.join(dossier_courses, nom)
                if not B.verifier_scelle_fichier(ch):
                    raise B.ArretBanc(f"{nom} non scellé")
                fichiers[nom] = {"sha256": B.sha256_fichier(ch), "octets": os.path.getsize(ch)}
    provenance = E.provenance_calcul(config)
    manifeste = {
        "version": VERSION, "mode": mode, "configuration": config, "configuration_sha256": sha,
        "versions": provenance["versions"],
        "racines": config["racines"], "code": code["fichiers"], "commit_banc": code["commit"], "arbre_propre": code["arbre_propre"],
        "organisme": provenance["organisme"],
        "preenregistrement": prereg, "horodatage_scellement": config["preenregistrement"]["horodatage_scellement"],
        "etalonnage": {"chemin": os.path.abspath(chemin_e), "sha256": B.sha256_fichier(chemin_e),
                       "versions": etal.get("versions"), "organisme": etal.get("organisme"),
                       "versions_identiques": etal.get("versions") == provenance["versions"],
                       "commit_organisme_identique": (etal.get("organisme") or {}).get("commit_lu")
                       == provenance["organisme"]["commit_lu"]},
        "partiels_recuperes": E.inventaire_recuperes(dossier_courses),
        "parametres": {"forces": P["forces"], "s": P["s"], "c": P["c"]},
        "graines_premieres_derivations": premieres, "courses": list(range(n)), "fichiers": fichiers,
        "secondes": sum(i["secondes"] for i in infos), "secondes_mur_derniere_session": mur,
        "octets": sum(f["octets"] for f in fichiers.values()), "horodatage": B.horodatage(),
    }
    B.ecrire_json_scelle(chemin_m, manifeste)
    return {"etape": "decisive", "courses": n}


def rejouer(a, config, sha, prereg, mode):
    d = dossier_etape(a.sortie, "rejouer")
    chemin_r = os.path.join(d, AN.NOM_REJEU)
    if B.verifier_scelle_fichier(chemin_r):
        return {"etape": "rejouer", "reprise": "déjà scellé"}
    chemin_m = os.path.join(d, NOM_MANIFESTE)
    if not B.verifier_scelle_fichier(chemin_m):
        raise B.ArretBanc("rejeu : manifeste de la course décisive absent ou non scellé")
    manifeste = B.lire_json_verifie(chemin_m)
    t = time.perf_counter()
    rapport = RJ.rejouer_dossier(os.path.join(d, "courses"), a.processus, attendus=2 * len(manifeste["courses"]))
    sym = RJ.rejouer_dossier(os.path.join(d, "courses"), 1, courses=config["audit_symetrie"]["courses"], m1_nul=True)
    n_e = config["etalonnage"]["courses_par_classe"]
    etal = RJ.rejouer_dossier(os.path.join(dossier_etape(a.sortie, "etalonner"), "courses"), a.processus, attendus=2 * n_e)
    rapport.update(manifeste_sha256=B.sha256_fichier(chemin_m), secondes=time.perf_counter() - t,
                   courses_audit_symetrie={"courses": config["audit_symetrie"]["courses"], "verdict": sym["verdict"],
                                           "journaux": sym["journaux"], "recoupement": sym["recoupement"]},
                   etalonnage={"journaux": etal["journaux"], "decisions": etal["decisions"], "verdict": etal["verdict"],
                               "recoupement": etal["recoupement"]})
    B.ecrire_json_scelle(chemin_r, rapport)
    return {"etape": "rejouer", "verdict": rapport["verdict"]}


def analyser(a, config, sha, prereg, mode):
    d = dossier_etape(a.sortie, "analyser")
    chemin_l = os.path.join(d, AN.NOM_LECTURE)
    if B.verifier_scelle_fichier(chemin_l):
        # correction 8 : une reprise relit la lecture scellée et lève de nouveau la garde A7 ou A11 qui a tiré
        AN.lever_gardes_de_lecture(B.lire_json_verifie(chemin_l), chemin_l)
        return {"etape": "analyser", "reprise": "déjà scellée"}
    t = time.perf_counter()
    _, sha_l = AN.analyser_dossier(d, config, os.path.join(d, NOM_MANIFESTE))
    return {"etape": "analyser", "lecture_sha256": sha_l, "secondes": time.perf_counter() - t}


# --- dépôt (journaux compressés, morceaux ≤ 90 Mo, manifeste scellé) --------------------------------------------------------
def empreinte_ensemble(parties):
    """Empreinte du tout (R-3851) : sha256 du JSON canonique de la liste triée [chemin du membre, sha256, octets] de tous
    les membres de tous les morceaux."""
    membres = sorted([m, info["sha256"], info["octets"]] for p in parties for m, info in p["membres"].items())
    return B.JL.empreinte(membres)


def empaqueter(sortie, vers, morceau_max=MORCEAU_MAX, depot_max=DEPOT_MAX, marge=1024 * 1024):
    """Dépôt : fichiers compressés et JSON (et tout ce qui est sous `partiels-recuperes/`, provisoires compris) en morceaux
    tar ≤ `morceau_max`, compagnons `.sha256`, manifeste scellé avec l'empreinte de chaque morceau, de chaque membre
    (empreinte et octets) et de l'ensemble (correction 6)."""
    fichiers = []
    for racine, _, noms in os.walk(sortie):
        recuperes = E.DOSSIER_RECUPERES in os.path.relpath(racine, sortie).split(os.sep)
        for n in sorted(noms):
            ch = os.path.join(racine, n)
            if recuperes or (n.endswith((".xz", ".json", ".sha256")) and ".partiel" not in n):
                fichiers.append(ch)
    fichiers.sort()
    total = sum(os.path.getsize(f) for f in fichiers)
    if total > depot_max:
        raise DepotTropGros(f"dépôt de {total} octets compressés, au-delà de {depot_max} : arrêt et rapport avant de pousser")
    os.makedirs(vers, exist_ok=False)
    parties, courant, taille, k = [], [], 0, 0

    def fermer(courant, k):
        nom = f"journaux-banc-a-ligne1-v2-partie-{k:03d}.tar"
        ch = os.path.join(vers, nom)
        with tarfile.open(ch, "w", format=tarfile.PAX_FORMAT) as tf:
            for f in courant:
                info = tf.gettarinfo(f, arcname=os.path.relpath(f, sortie))
                info.mtime, info.uid, info.gid, info.uname, info.gname = 0, 0, 0, "", ""
                with open(f, "rb") as fo:
                    tf.addfile(info, fo)
        if os.path.getsize(ch) > morceau_max:
            raise DepotTropGros(f"{nom} dépasse {morceau_max} octets")
        sha = B.sha256_fichier(ch)
        with open(ch + ".sha256", "w", encoding="utf-8") as fo:
            fo.write(f"{sha}  {nom}\n")
        return {"nom": nom, "sha256": sha, "octets": os.path.getsize(ch),
                "membres": {os.path.relpath(f, sortie): {"sha256": B.sha256_fichier(f), "octets": os.path.getsize(f)}
                            for f in courant}}

    for f in fichiers:
        s = os.path.getsize(f) + 4096          # en-têtes et bourrage du format tar, par fichier (borne haute)
        if courant and taille + s > morceau_max - marge:
            parties.append(fermer(courant, k))
            k, courant, taille = k + 1, [], 0
        courant.append(f)
        taille += s
    if courant:
        parties.append(fermer(courant, k))
    manifeste = {"version": VERSION, "source": os.path.abspath(sortie), "octets_compresses": total, "parties": parties,
                 "morceau_max": morceau_max, "membres": sum(len(p["membres"]) for p in parties),
                 "octets_morceaux": sum(p["octets"] for p in parties),
                 "empreinte_ensemble": {"regle": "sha256 du JSON canonique de la liste triée [membre, sha256, octets]",
                                        "sha256": empreinte_ensemble(parties)},
                 "empreinte_morceaux": B.JL.empreinte(sorted([p["nom"], p["sha256"], p["octets"]] for p in parties))}
    sha = B.ecrire_json_scelle(os.path.join(vers, NOM_DEPOT), manifeste)
    return manifeste, sha


def verifier_depot(vers):
    """Relit un dépôt : manifeste scellé ; chaque morceau a son empreinte et son compagnon ; chaque membre lu dans le tar a
    l'empreinte et la taille du manifeste, et aucun membre de plus ; l'empreinte de l'ensemble et celle des morceaux se
    recalculent. Lève `DepotIncoherent` au premier écart ; rend l'empreinte de l'ensemble."""
    import hashlib
    ch_m = os.path.join(vers, NOM_DEPOT)
    if not B.verifier_scelle_fichier(ch_m):
        raise DepotIncoherent("dépôt : manifeste absent ou non scellé")
    m = B.lire_json_verifie(ch_m)
    for p in m["parties"]:
        ch = os.path.join(vers, p["nom"])
        if not B.verifier_scelle_fichier(ch) or B.sha256_fichier(ch) != p["sha256"] or os.path.getsize(ch) != p["octets"]:
            raise DepotIncoherent(f"dépôt : morceau {p['nom']} différent de son manifeste")
        lus = {}
        with tarfile.open(ch, "r") as tf:
            for info in tf.getmembers():
                f = tf.extractfile(info)
                if f is None:
                    raise DepotIncoherent(f"dépôt : membre {info.name} illisible dans {p['nom']}")
                octets = f.read()
                lus[info.name] = {"sha256": hashlib.sha256(octets).hexdigest(), "octets": len(octets)}
        if lus != p["membres"]:
            raise DepotIncoherent(f"dépôt : membres de {p['nom']} différents du manifeste")
    if empreinte_ensemble(m["parties"]) != m["empreinte_ensemble"]["sha256"]:
        raise DepotIncoherent("dépôt : empreinte de l'ensemble différente du manifeste")
    if B.JL.empreinte(sorted([p["nom"], p["sha256"], p["octets"]] for p in m["parties"])) != m["empreinte_morceaux"]:
        raise DepotIncoherent("dépôt : empreinte des morceaux différente du manifeste")
    return m["empreinte_ensemble"]["sha256"]


# --- tout, avec plafond A13 -----------------------------------------------------------------------------------------------
def surveiller(cmd, plafond, consommees, journal_arret, intervalle=5.0, sortie_log=None, tic=None, fichier_pid=None):
    """Lance `cmd` dans une session neuve et le surveille ; au-delà du plafond (secondes cumulées), arrêt par identifiant de
    processus (groupe de la session ; règle R10), arrêt écrit, `GardeA13Duree`. `tic(ecoule)` est appelé à chaque tour
    (durée cumulée tenue à jour même si le lanceur est interrompu) ; l'identifiant de l'étape est écrit dans `fichier_pid`.
    Rend (code de retour, secondes)."""
    t0 = time.monotonic()
    log = open(sortie_log, "ab") if sortie_log else subprocess.DEVNULL
    p = subprocess.Popen(cmd, start_new_session=True, stdout=log, stderr=log, stdin=subprocess.DEVNULL)
    if fichier_pid:
        with open(fichier_pid, "w", encoding="utf-8") as f:
            f.write(f"{p.pid}\n")
    try:
        while p.poll() is None:
            ecoule = time.monotonic() - t0
            if tic:
                tic(ecoule)
            if consommees + ecoule > plafond:
                os.killpg(p.pid, signal.SIGTERM)
                try:
                    p.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(p.pid, signal.SIGKILL)
                    p.wait()
                arret = {"garde": "A13", "pid": p.pid, "commande": cmd, "secondes_cumulees": consommees + ecoule,
                         "plafond": plafond, "horodatage": B.horodatage(), "action": "arrêt par identifiant de processus ; "
                         "rien n'est lu ; retour à la mère"}
                with open(journal_arret, "a", encoding="utf-8") as f:
                    f.write(json.dumps(arret, ensure_ascii=False) + "\n")
                raise GardeA13Duree(f"garde A13 : durée de calcul au-delà de {plafond} secondes : processus {p.pid} arrêté")
            try:
                p.wait(timeout=min(intervalle, max(0.05, plafond - consommees - ecoule + 0.05)))
            except subprocess.TimeoutExpired:
                pass
    finally:
        if sortie_log:
            log.close()
    return p.returncode, time.monotonic() - t0


def processus_vivant(pid):
    """Vrai si un processus d'identifiant `pid` existe (signal 0 : rien n'est envoyé ; règle R10, par identifiant)."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def verifier_aucun_processus_vivant(sortie, noms=(NOM_PID_LANCEUR, NOM_PID_ETAPE)):
    """Avant tout lancement ou reprise de `tout` : chaque identifiant écrit dans un fichier `pid-*.txt` du dossier (lanceur,
    étape) doit désigner un processus disparu ; sinon `RepriseConcurrente` (deux lanceurs sur le même dossier déplaceraient
    les fichiers d'une course en cours d'écriture). Un identifiant illisible lève aussi. Le processus courant est ignoré.
    Rend la liste des identifiants lus."""
    lus = []
    for n in noms:
        ch = os.path.join(sortie, n)
        if not os.path.exists(ch):
            continue
        texte = open(ch, encoding="utf-8").read().strip()
        try:
            pid = int(texte)
        except ValueError as e:
            raise RepriseConcurrente(f"{n} : identifiant illisible ({texte!r}) : vérifier à la main avant toute reprise") from e
        lus.append(pid)
        if pid != os.getpid() and processus_vivant(pid):
            raise RepriseConcurrente(f"{n} : le processus {pid} vit encore : aucune reprise tant qu'il n'a pas disparu "
                                     "(l'arrêter par son identifiant si c'est voulu, règle R10)")
    return lus


def tout(a, config):
    os.makedirs(a.sortie, exist_ok=True)
    etat_ch = os.path.join(a.sortie, NOM_ETAT)
    etat = json.load(open(etat_ch, encoding="utf-8")) if os.path.exists(etat_ch) else {"secondes_cumulees": 0.0, "sessions": []}
    etat["sessions"].append({"debut": B.horodatage(), "pid": os.getpid()})
    plafond = config["plafond_secondes"]

    def ecrire_etat(en_cours=0.0):
        provisoire = etat_ch + ".partiel"
        with open(provisoire, "w", encoding="utf-8") as f:
            json.dump(dict(etat, secondes_cumulees=etat["secondes_cumulees"] + en_cours), f, ensure_ascii=False, indent=1)
        os.replace(provisoire, etat_ch)

    for etape in ETAPES:
        if etape_faite(a.sortie, etape) and etape != "analyser":
            continue        # l'analyse est toujours relancée : sa reprise relève la garde A7 ou A11 (correction 8)
        cmd = [sys.executable, "-B", os.path.abspath(__file__), etape, "--sortie", a.sortie, "--organisme", a.organisme,
               "--processus", str(a.processus)] + (["--fumee"] if a.fumee else [])
        code, s = surveiller(cmd, plafond, etat["secondes_cumulees"], os.path.join(a.sortie, NOM_ARRETS),
                             sortie_log=os.path.join(a.sortie, f"journal-{etape}.log"), tic=ecrire_etat,
                             fichier_pid=os.path.join(a.sortie, NOM_PID_ETAPE))
        etat["secondes_cumulees"] += s
        etat["sessions"][-1].setdefault("etapes", []).append({"etape": etape, "code": code, "secondes": s})
        ecrire_etat()
        if code != 0:
            print(f"étape {etape} : code de retour {code} ; voir journal-{etape}.log ; chaîne arrêtée", flush=True)
            return code
    print("chaîne complète : étalonnage, course décisive, rejeu, analyse scellés", flush=True)
    if a.fumee:
        print(json.dumps(resume_fumee(a.sortie, etat), ensure_ascii=False, indent=1), flush=True)
    return 0


def resume_fumee(sortie, etat):
    """Résumé de la fumée : durées, tailles, comptes, sceaux. Aucune métrique, aucun verdict, aucune porte n'est imprimé."""
    tailles = {}
    for etape in ("etalonnage", "decisive"):
        total, n = 0, 0
        for r, _, noms in os.walk(os.path.join(sortie, etape)):
            for nm in noms:
                if nm.endswith(".xz"):
                    total += os.path.getsize(os.path.join(r, nm))
                    n += 1
        tailles[etape] = {"fichiers_xz": n, "octets": total}
    d = os.path.join(sortie, "decisive")
    m = B.lire_json_verifie(os.path.join(d, NOM_MANIFESTE))
    rj = B.lire_json_verifie(os.path.join(d, AN.NOM_REJEU))
    e = B.lire_json_verifie(os.path.join(sortie, "etalonnage", E.NOM_SORTIE))
    return {"durees_par_etape_secondes": [x for s in etat["sessions"] for x in s.get("etapes", [])],
            "etalonnage_etapes_secondes": e["etapes"], "courses_decisives": len(m["courses"]),
            "secondes_calcul_courses_decisives": m["secondes"], "tailles": tailles,
            "rejeu": {"journaux": rj["journaux"], "decisions": rj["decisions"], "verdict": rj["verdict"],
                      "secondes": rj["secondes"]},
            "sceaux": {"etalonnage": B.verifier_scelle_fichier(os.path.join(sortie, "etalonnage", E.NOM_SORTIE)),
                       "manifeste": B.verifier_scelle_fichier(os.path.join(d, NOM_MANIFESTE)),
                       "rejeu": B.verifier_scelle_fichier(os.path.join(d, AN.NOM_REJEU)),
                       "lecture": B.verifier_scelle_fichier(os.path.join(d, AN.NOM_LECTURE))}}


def main(argv=None):
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    sys.dont_write_bytecode = True
    p = argparse.ArgumentParser(description="Lanceur du banc A, ligne 1 (code v2).")
    p.add_argument("etape", choices=ETAPES + ("tout", "empaqueter", "fumee"))
    p.add_argument("--sortie", required=True, help="dossier de la chaîne (hors du dépôt)")
    p.add_argument("--organisme", default=None, help="dossier orchestrator/ du dépôt de l'organisme (lecture seule)")
    p.add_argument("--processus", type=int, default=max(1, os.cpu_count() or 1))
    p.add_argument("--fumee", action="store_true", help="configuration de fumée (racines disjointes)")
    p.add_argument("--vers", default=None, help="empaqueter : dossier neuf des morceaux")
    a = p.parse_args(argv)
    mode = "fumee" if (a.fumee or a.etape == "fumee") else "reel"
    if a.etape == "empaqueter":
        m, sha = empaqueter(a.sortie, a.vers)
        print(f"{len(m['parties'])} morceau(x), {m['octets_compresses']} octets compressés, manifeste {sha}")
        return 0
    if a.organisme is None:
        p.error("--organisme est exigé")
    if a.etape in ("tout", "fumee"):
        os.makedirs(a.sortie, exist_ok=True)
        try:
            verifier_aucun_processus_vivant(a.sortie)
        except RepriseConcurrente as e:
            print(f"ARRÊT {type(e).__name__} : {e}", flush=True)
            return 4
        config, _, _ = preparer(a.organisme, mode)
        a.fumee = mode == "fumee"
        with open(os.path.join(a.sortie, NOM_PID_LANCEUR), "w") as f:
            f.write(f"{os.getpid()}\n")
        try:
            return tout(a, config)
        except GardeA13Duree as e:
            print(f"ARRÊT {type(e).__name__} : {e}", flush=True)
            return 13
    config, sha, prereg = preparer(a.organisme, mode)
    fonction = {"etalonner": etalonner, "decisive": decisive, "rejouer": rejouer, "analyser": analyser}[a.etape]
    try:
        res = fonction(a, config, sha, prereg, mode)
    except B.ArretBanc as e:
        print(f"ARRÊT {type(e).__name__} : {e}", flush=True)
        return 3
    print(json.dumps(res, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
