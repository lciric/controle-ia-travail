"""Lanceur des notations complémentaires de T0.5, côté machine de calcul.

Un run « source » de la chaîne du pilote (`lancer_pilote_a` : le pilote, ou un run de même chaîne sur d'autres tâches)
n'a pas noté certains couples (épisode, passe) : les épisodes `e2`, passe 0, que la chaîne ne note jamais comme décisifs
(elle ne note en décisif que e0, passes 0 et 1, et e1, passe 0) ; et, si le run source s'est arrêté à son échéance
pendant ses notations décisives, les notations qui y manquent. Ce module note les seuls couples que demande
`notations_a_faire`, par les juges du run source (8B puis 3B), sur les ensembles finaux scellés de son `episodes.json`,
avec les mêmes paramètres, les mêmes graines (entropie du run source, mêmes clés `juge-<juge>/<épisode>/passe-<p>`, déjà
présentes dans son manifeste) et le même découpage en lots (`lot_juge`). Il n'importe que des fonctions du code cité par
le pilote, sans les modifier ; ses notations s'écrivent dans `diag/<run du complément>/`, sous son propre manifeste,
jamais dans le dossier du run source. On ne renote jamais : un couple déjà noté par un juge dans le run source
(fichiers `notations-<juge>-decisives.json` ou `-descriptives.json` présents) arrête avant le manifeste.

Dérivé du lanceur des notations refaites (`noter_pilote_a`, N-021), absent de l'arbre du pilote : ses gardes, son
déroulé après le manifeste et ses lignes de progression sont repris ici sous des intitulés propres.

Gardes d'avant le manifeste : configuration complète et bornée (`notations_a_faire` : chaque juge du run, indices
d'épisode, passes dans `range(passes_de(...))` ; un nombre attendu par juge) ; préenregistrement en mode réel (R1) ;
citations (commit du code, configuration, run source, empreintes de son manifeste, de ses épisodes, de son arrêt ou
« aucun », des notations qu'il porte déjà, tâches, entropie), chacune une seule fois ; état du run source constaté
(épisodes et appariement scellés et rattachés ; arrêt consigné après l'appariement, ou résumé ; notations présentes
vérifiées et lues) ; paramètres des juges et versions égaux à ceux du run source ; nombre exact de notations par juge ;
couples demandés disjoints des couples déjà notés ; graines présentes dans le manifeste du run source et égales, clé à
clé.

Après le manifeste, comme au modèle : formats des juges contrôlés contre ceux, scellés, du début du run source ; le 8B
note lot par lot, puis son fichier est écrit ; le 3B, préchargé avant, se charge hors ligne, format recontrôlé, note,
puis son fichier est écrit. Chaque juge a son échéance (le 8B depuis le début du run, le 3B depuis son premier lot),
contrôlée avant chaque lot : un juge échu s'arrête sans fichier (« tout ou rien ») et le suivant commence. L'échéance
globale arrête le run (`noter_ensembles`), comme le signal TERM : aucune exception d'arrêt n'est attrapée pour continuer
(gardes.py). Une ligne `PROGRES` par lot (juge, rang et durée du lot, rien d'autre) et une par fin de juge (statut, lots
faits, durée) vont sur la sortie d'erreur. Tout arrêt levé après le manifeste laisse un `arret.json` scellé (étape,
motif, compteurs), puis se propage ; restent sans `arret.json` les fenêtres que déclare le préenregistrement (KILL du
délai externe, arrêt brutal de l'hôte, exception ou signal pendant la consignation, signal pendant la création du
manifeste ou juste après : l'état et le début du run sont calculés avant le manifeste).
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import re
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import torch

from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import COMMIT_CITE, ENTROPIE_CITEE, exiger_code_cite, exiger_code_importe_sous
from ..manifeste import (config_canonique, creer_manifeste, ecrire_resultat, graines, lire_manifeste,
                         verifier_resultat, versions)
from ..scellement import empreinte, verifier
from .lancer_pilote_a import (TACHES_CITEES, charger_format_seul, charger_modele_et_format, controler_format,
                              demandes_de_notation, empreinte_config, exiger_invites, memoire_pic_gio, passes_de,
                              precharger_juges)
from .pilote_a import charger_taches, noter_ensembles

COMMANDE = "python -m controle_ia.environnements.noter_complement_t05"
DUREE_EXTERNE_S = 24_000            # délai externe global du script de l'instance (400 minutes, un ou deux runs)
DUREE_GLOBALE_MAX_S = 23_100        # borne de `duree_globale_s` : sous le délai externe, marge pour le dernier lot
CLES = ("mode", "run_source", "agent", "juges", "lot_juge", "max_nouveaux_juge", "temperature_juge", "variante_juge",
        "episodes_decisifs", "episodes_notes_deux_fois", "fils", "duree_max_juges_s", "duree_globale_s",
        "notations_attendues_par_juge", "notations_a_faire")
CLES_EGALES_A_LA_SOURCE = ("agent", "juges", "lot_juge", "max_nouveaux_juge", "temperature_juge", "variante_juge",
                           "episodes_decisifs", "episodes_notes_deux_fois", "fils")
VERSIONS_EGALES = ("torch", "transformers", "tokenizers", "numpy")
# étapes d'arrêt du run source permises : après l'appariement (notations, chargement d'un juge pour elles, résumé)
ETAPES_APRES_APPARIEMENT = ("notations decisives par ", "notations descriptives par ", "chargement du juge ")
NOTATIONS_DE_LA_SOURCE = re.compile(r"notations-(.+)-(decisives|descriptives)\.json")
INDICE_D_EPISODE = re.compile(r"0|[1-9][0-9]*")
# intitulés propres à ce préenregistrement, jamais ceux du pilote ni des notations refaites ; chacun cité une seule fois
CONFIG_CITEE = re.compile(r"Configuration du complément \(empreinte canonique\) : `([0-9a-f]{64})`")
RUN_SOURCE_CITE = re.compile(r"Run source noté : `(\d{8}-\d{6}-[A-Za-z0-9_.-]+)`")
MANIFESTE_SOURCE_CITE = re.compile(r"Manifeste du run source : `([0-9a-f]{64})`")
EPISODES_SOURCE_CITES = re.compile(r"Épisodes du run source : `([0-9a-f]{64})`")
ARRET_SOURCE_CITE = re.compile(r"Arrêt du run source : `([0-9a-f]{64}|aucun)`")
NOTATIONS_SOURCE_CITEES = re.compile(r"Notations déjà présentes dans le run source : `([0-9a-f]{64})`")


def progres(**champs) -> None:
    """Ligne de progression, à préfixe fixe, sans aucun texte de réponse ni d'ensemble (recopiée dans le journal de
    l'instance par son script)."""
    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={v}" for k, v in champs.items()), file=sys.stderr, flush=True)


def _entier_positif(n) -> bool:
    return not isinstance(n, bool) and isinstance(n, int) and n > 0


def exiger_notations_a_faire(config: dict) -> None:
    """`notations_a_faire` : {juge: {"<indice d'épisode>": [passes]}}, chaque juge du run présent, au moins un couple
    par juge, passes distinctes dans `range(passes_de(...))` (aucun couple sans graine possible au run source)."""
    noms = [j["nom"] for j in config["juges"]]
    a_faire = config["notations_a_faire"]
    if not isinstance(a_faire, dict) or sorted(a_faire) != sorted(noms):
        raise GardeArret(f"notations_a_faire : une entrée par juge du run attendue ({noms})")
    for nom, par_episode in a_faire.items():
        if not isinstance(par_episode, dict) or not par_episode:
            raise GardeArret(f"notations_a_faire[{nom!r}] : au moins un épisode attendu")
        for k, passes in par_episode.items():
            if not isinstance(k, str) or not INDICE_D_EPISODE.fullmatch(k):
                raise GardeArret(f"notations_a_faire[{nom!r}] : indice d'épisode {k!r} illisible")
            n = passes_de(f"x/e{k}", config)
            if (not isinstance(passes, list) or not passes
                    or any(isinstance(p, bool) or not isinstance(p, int) or p not in range(n) for p in passes)
                    or len(set(passes)) != len(passes)):
                raise GardeArret(f"notations_a_faire[{nom!r}][{k!r}] = {passes!r} : passes distinctes dans "
                                 f"range({n}) attendues (passes_de)")


def exiger_config_complement(config: dict) -> None:
    manquantes = [c for c in CLES if c not in config]
    if manquantes:
        raise GardeArret(f"configuration du complément incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    noms = [j["nom"] for j in config["juges"]]
    durees = config["duree_max_juges_s"]
    if not isinstance(durees, dict) or sorted(durees) != sorted(noms):
        raise GardeArret(f"duree_max_juges_s : une durée par juge attendue ({noms})")
    globale = config["duree_globale_s"]
    for nom, d in [*durees.items(), ("globale", globale)]:
        if isinstance(d, bool) or not isinstance(d, (int, float)) or not 0 < d <= DUREE_GLOBALE_MAX_S:
            raise GardeArret(f"durée {nom} {d!r} : un nombre dans ]0 ; {DUREE_GLOBALE_MAX_S}] s attendu")
    attendues = config["notations_attendues_par_juge"]
    if not isinstance(attendues, dict) or sorted(attendues) != sorted(noms):
        raise GardeArret(f"notations_attendues_par_juge : un nombre par juge attendu ({noms})")
    for nom, n in attendues.items():
        if not _entier_positif(n):
            raise GardeArret(f"notations_attendues_par_juge[{nom!r}] {n!r} : un entier positif attendu")
    exiger_notations_a_faire(config)


def empreinte_des_notations(presentes: list[list[str]]) -> str:
    """Empreinte canonique de la liste triée des (nom de fichier, empreinte) des notations déjà présentes."""
    return hashlib.sha256(config_canonique(sorted(presentes))).hexdigest()


def charger_source(racine: Path, run_source: str, noms_juges: list[str]) -> dict:
    """État du run source constaté sur ses fichiers scellés : manifeste ; épisodes et appariement rattachés à lui ;
    arrêt consigné après l'appariement (facultatif), sinon résumé ; notations présentes vérifiées, rattachées et lues
    (clés déjà notées, par juge). Rien n'est écrit dans son dossier."""
    d = racine / "diag" / run_source
    chemin_m = racine / "runs" / run_source / "manifeste.json"
    if not chemin_m.exists():
        raise GardeArret(f"manifeste du run source absent : {chemin_m}")
    manifeste, sha_m = lire_manifeste(chemin_m)

    def rattache(nom_fichier: str) -> dict:
        c = verifier_resultat(racine, d / nom_fichier)
        if c["run_id"] != run_source or c["manifeste_sha256"] != sha_m:
            raise GardeArret(f"run source {run_source} : {nom_fichier} rattaché à un autre run ou à un autre manifeste")
        return c["resultat"]

    corps = {}
    for nom in ("episodes", "appariements"):
        if not (d / f"{nom}.json").exists():
            raise GardeArret(f"run source {run_source} : {nom}.json absent")
        corps[nom] = rattache(f"{nom}.json")
    arret = rattache("arret.json") if (d / "arret.json").exists() else None
    resume = rattache("resume.json") if (d / "resume.json").exists() else None
    if arret is None and resume is None:
        raise GardeArret(f"run source {run_source} : ni arret.json ni resume.json (run en cours, ou interrompu sans "
                         f"consignation) : état non constatable")
    taches_consignees = []
    if arret is not None:
        etape = str(arret.get("etape", ""))
        if not (etape.startswith(ETAPES_APRES_APPARIEMENT) or etape == "résumé"):
            raise GardeArret(f"run source {run_source} : arrêté à l'étape {etape!r}, avant les notations")
        if not arret.get("partiel", {}).get("appariement_ecrit"):
            raise GardeArret(f"run source {run_source} : appariement non consigné comme écrit")
        taches_consignees.append(("arret.json, partiel.taches_sha256", arret.get("partiel", {}).get("taches_sha256")))
    if resume is not None:
        taches_consignees.append(("resume.json, taches_sha256", resume.get("taches_sha256")))
    deja = {nom: set() for nom in noms_juges}
    presentes = []
    for f in sorted(d.glob("notations-*.json")):
        m = NOTATIONS_DE_LA_SOURCE.fullmatch(f.name)
        if not m or m.group(1) not in deja:
            raise GardeArret(f"run source {run_source} : fichier de notations inattendu {f.name}")
        cles = [n["cle"] for n in rattache(f.name)["notations"]]
        if any(not c.startswith(f"juge-{m.group(1)}/") for c in cles):
            raise GardeArret(f"run source {run_source} : {f.name} porte des clés d'un autre juge")
        deja[m.group(1)] |= set(cles)
        presentes.append([f.name, empreinte(f)])
    return {"manifeste": manifeste, "manifeste_sha256": sha_m, "fiches": corps["episodes"]["fiches"],
            "formats": corps["episodes"]["formats"], "arret": arret, "resume": resume,
            "taches_consignees": taches_consignees, "deja_notees": deja,
            "notations_presentes": sorted(presentes), "notations_sha256": empreinte_des_notations(presentes),
            "episodes_sha256": empreinte(d / "episodes.json"),
            "arret_sha256": empreinte(d / "arret.json") if arret is not None else None}


def exiger_taches_de_la_source(source: dict, sha_taches: str) -> None:
    for ou, sha in source["taches_consignees"]:
        if sha != sha_taches:
            raise GardeArret(f"tâches ≠ celles du run source ({ou})")


def exiger_egal_a_la_source(config: dict, source: dict, mode: str) -> None:
    cs = source["manifeste"]["config"]
    for k in CLES_EGALES_A_LA_SOURCE:
        if k not in cs:
            raise GardeArret(f"{k} absent de la configuration du run source")
        if config[k] != cs[k]:
            raise GardeArret(f"{k} ≠ celui du run source : aucun paramètre des juges ne change")
    if mode == "reel":
        v, vs = versions(), source["manifeste"]["versions"]
        ecarts = [b for b in VERSIONS_EGALES if v.get(b) != vs.get(b)]
        if ecarts:
            raise GardeArret(f"versions ≠ celles du run source : {ecarts}")


def exiger_citations_complement(prereg: Path, config: dict, sha_taches: str, source: dict) -> int:
    """Garde : commit du code, configuration, run source, empreintes de son manifeste, de ses épisodes, de son arrêt
    (ou « aucun »), des notations qu'il porte déjà, tâches et entropie, chacun cité une seule fois par le
    préenregistrement du complément ; valeurs égales à celles constatées. Renvoie l'entropie citée."""
    texte = Path(prereg).read_text(encoding="utf-8")
    trouves = {nom: rx.findall(texte) for nom, rx in (
        ("commit du code", COMMIT_CITE), ("configuration", CONFIG_CITEE), ("run source", RUN_SOURCE_CITE),
        ("manifeste", MANIFESTE_SOURCE_CITE), ("épisodes", EPISODES_SOURCE_CITES), ("arrêt", ARRET_SOURCE_CITE),
        ("notations présentes", NOTATIONS_SOURCE_CITEES), ("tâches", TACHES_CITEES), ("entropie", ENTROPIE_CITEE))}
    for nom, valeurs in trouves.items():
        if len(valeurs) != 1:
            raise GardeArret(f"{prereg} : {nom} : {'cité nulle part' if not valeurs else f'cité {len(valeurs)} fois'}, "
                             f"une seule citation attendue")
    attendus = {"configuration": empreinte_config(config), "run source": config["run_source"],
                "manifeste": source["manifeste_sha256"], "épisodes": source["episodes_sha256"],
                "arrêt": source["arret_sha256"] or "aucun", "notations présentes": source["notations_sha256"],
                "tâches": sha_taches}
    for nom, valeur in attendus.items():
        if trouves[nom][0] != valeur:
            raise GardeArret(f"{nom} {str(valeur)[:12]} ≠ {nom} cité {trouves[nom][0][:12]}")
    return int(trouves["entropie"][0])


def _couple(cle: str) -> tuple[str, int]:
    """(indice d'épisode, passe) lus sur une clé `juge-<juge>/<tâche>/e<k>/passe-<p>`."""
    reste, passe = cle.rsplit("/passe-", 1)
    return reste.rsplit("/e", 1)[1], int(passe)


def demandes_a_faire(source: dict, par_id: dict, config: dict, nom_juge: str) -> list[dict]:
    """Demandes de la chaîne (`demandes_de_notation`, sur les fiches du run source), filtrées par
    `notations_a_faire[nom_juge]` ; l'ordre de la chaîne est gardé."""
    a_faire = {(k, p) for k, passes in config["notations_a_faire"][nom_juge].items() for p in passes}
    return [d for d in demandes_de_notation(source["fiches"], par_id, config, nom_juge) if _couple(d["cle"]) in a_faire]


def exiger_nombre_et_disjonction(demandes: dict, config: dict, source: dict) -> None:
    for nom, dem in demandes.items():
        attendu = config["notations_attendues_par_juge"][nom]
        if len(dem) != attendu:
            raise GardeArret(f"juge {nom} : {len(dem)} notations à faire, {attendu} attendues")
        deja = sorted({d["cle"] for d in dem} & source["deja_notees"][nom])
        if deja:
            raise GardeArret(f"juge {nom} : {len(deja)} couples déjà notés dans le run source (dont {deja[0]!r}) : "
                             f"on ne renote jamais")


def cles_des_graines(demandes_par_juge: dict) -> list[str]:
    return [d["cle"] for dem in demandes_par_juge.values() for d in dem] + ["modele-jouet"]


def exiger_graines_de_la_source(cles: list[str], entropie: int, source: dict) -> None:
    """Chaque clé présente dans le manifeste du run source, graine recalculée égale, clé à clé : mêmes graines et
    mêmes entrées ; l'identité des notations avec celles qu'aurait faites le run source n'est pas garantie sur une
    autre carte, une autre instance ou une autre composition des lots."""
    gs = source["manifeste"]["graines"]
    if any(g.get("entropie") != str(entropie) for g in gs.values()):
        raise GardeArret("entropie ≠ celle du run source")
    absentes = [k for k in cles if k not in gs]
    if absentes:
        raise GardeArret(f"{len(absentes)} clés absentes du manifeste du run source (dont {absentes[0]!r})")
    neuves = graines(cles, entropie)
    ecarts = [k for k in cles if gs[k] != neuves[k]]
    if ecarts:
        raise GardeArret(f"graines ≠ celles du run source pour {len(ecarts)} clés (dont {ecarts[0]!r})")


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_taches: str,
             autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config_complement(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("run réel du complément sans préenregistrement : R1 interdit de lancer")
    taches = charger_taches(chemin_taches)
    sha_taches = verifier(chemin_taches)
    exiger_invites(config)
    source = charger_source(racine, config["run_source"], [j["nom"] for j in config["juges"]])
    exiger_taches_de_la_source(source, sha_taches)
    exiger_egal_a_la_source(config, source, config["mode"])
    commit_cite = None
    entropie = int(next(iter(source["manifeste"]["graines"].values()))["entropie"])
    if prereg is not None:
        exiger_code_importe_sous(racine)
        commit_cite = exiger_code_cite(racine, Path(prereg))
        entropie = exiger_citations_complement(Path(prereg), config, sha_taches, source)
    par_id = {t["identifiant"]: t for t in taches}
    demandes = {j["nom"]: demandes_a_faire(source, par_id, config, j["nom"]) for j in config["juges"]}
    exiger_nombre_et_disjonction(demandes, config, source)
    cles = cles_des_graines(demandes)
    exiger_graines_de_la_source(cles, entropie, source)
    # état et début du run calculés avant le manifeste : entre sa création et le bloc qui consigne l'arrêt, plus rien ne
    # s'exécute
    etat = {"etape": "chargement", "commit_cite": commit_cite, "run_source": config["run_source"],
            "manifeste_source_sha256": source["manifeste_sha256"], "episodes_sha256": source["episodes_sha256"],
            "arret_source_sha256": source["arret_sha256"], "notations_source_sha256": source["notations_sha256"],
            "taches_sha256": sha_taches, "config_sha256": empreinte_config(config), "juges": {}}
    debut = time.perf_counter()
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles, entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    try:
        return _apres_manifeste(config, racine, chemin_m, manifeste, source, demandes, etat, debut)
    except Exception as e:          # garde, panne, signal TERM, échéance globale : consigné, puis propagé
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _apres_manifeste(config, racine, chemin_m, manifeste, source, demandes, etat, debut) -> dict:
    g = manifeste["graines"]
    echeance_globale = debut + float(config["duree_globale_s"])
    from ..harnais.modeles import noyaux_attention_permis, regler_determinisme

    reglages = regler_determinisme(config["fils"], "cuda" if config["mode"] == "reel" else "cpu")
    etat["reglages"] = reglages
    juges = config["juges"]
    agent = next(j for j in juges if j["meme_modele_que_agent"])
    # chargement (téléchargement en mode réel) du juge qui est l'agent, consigné sous son étape propre
    etat["etape"] = f"chargement du juge {agent['nom']}"
    depart = time.perf_counter()
    modele, fmt = charger_modele_et_format(config["agent"], config["mode"], graine_entiere(g["modele-jouet"]))
    chargements = {agent["nom"]: round(time.perf_counter() - depart, 1)}
    # formats contrôlés au début, contre ceux, scellés, du début du run source
    etat["etape"] = "contrôle du format"
    formats = {}
    for j in juges:
        fmt_j = fmt if j["meme_modele_que_agent"] else charger_format_seul(j, config["mode"])
        formats[j["nom"]] = controler_format(fmt_j, j, "juge", config)
        if formats[j["nom"]] != source["formats"].get(f"juge-{j['nom']}"):
            raise GardeArret(f"juge {j['nom']} : format ≠ celui du début du run source")
    etat["etape"] = "préchargement des juges"
    etat["precharges"] = precharger_juges(config)
    noyaux = noyaux_attention_permis() if torch.cuda.is_available() else None
    modeles = {agent["nom"]: (modele, fmt)}
    for j in juges:
        nom = j["nom"]
        if nom not in modeles:
            etat["etape"] = f"chargement du juge {nom}"
            depart = time.perf_counter()
            m_j, fmt_j = charger_modele_et_format(j, config["mode"], graine_entiere(g["modele-jouet"]) + 1,
                                                  hors_ligne=True)
            chargements[nom] = round(time.perf_counter() - depart, 1)
            if controler_format(fmt_j, j, "juge", config) != formats[nom]:
                raise GardeArret(f"{nom} : format chargé hors ligne ≠ format contrôlé au début du run")
            modeles[nom] = (m_j, fmt_j)
        m_j, fmt_j = modeles[nom]
        etat["etape"] = f"notations complementaires par {nom}"
        dem = demandes[nom]
        lot = config["lot_juge"]
        lots = [dem[k:k + lot] for k in range(0, len(dem), lot)]
        graines_j = {d["cle"]: graine_entiere(g[d["cle"]]) for d in dem}
        depart_j = time.perf_counter()
        # échéance du juge : le premier (8B) depuis le début du run, les suivants depuis leur premier lot
        echeance_j = (debut if nom == agent["nom"] else depart_j) + float(config["duree_max_juges_s"][nom])
        # compteurs consignés pendant le run (résumé, arrêt) : lots seulement ; les jetons ne sont consignés que pour un
        # juge écrit, avec son fichier (aucune part du résultat d'un juge échu ou arrêté)
        suivi = {"lots": len(lots), "lots_faits": 0, "statut": "en cours"}
        etat["juges"][nom] = suivi
        memoire_pic_gio()
        sortie, jetons = [], 0
        for k, morceau in enumerate(lots, 1):
            exiger_sans_signal(f"avant le lot {k} du juge {nom}")
            if time.perf_counter() > echeance_j:
                suivi["statut"] = "échu"
                break
            t0 = time.perf_counter()
            part = noter_ensembles(m_j, fmt_j, morceau, graines_j, lot, config["max_nouveaux_juge"],
                                   config["temperature_juge"], echeance=echeance_globale)
            sortie += part
            suivi["lots_faits"] = k
            jetons += sum(x["jetons_reponse"] for x in part)
            # rang et durée du lot seulement : aucun compte de réponses (tronquées, complètes, jetons)
            progres(juge=nom, lot=f"{k}/{len(lots)}", duree_s=f"{time.perf_counter() - t0:.1f}")
        suivi["duree_s"] = round(time.perf_counter() - depart_j, 1)
        suivi["memoire_pic_gio"] = memoire_pic_gio()
        if suivi["statut"] == "en cours":
            # même nom et même forme que les notations décisives de la chaîne (fichier attendu par la lecture)
            ecrire_resultat(racine, chemin_m, f"notations-{nom}-decisives", {
                "notations": sortie, "noyau": "défaut de la bibliothèque", "noyaux_permis": noyaux,
                "descriptifs": {"duree_s": suivi["duree_s"], "memoire_pic_gio": suivi["memoire_pic_gio"],
                                "jetons_generes": jetons, "lots": len(lots)}})
            suivi["statut"] = "écrit"
            suivi["jetons_generes"] = jetons
            suivi["notations"] = len(sortie)
            suivi["completes"] = sum(1 for x in sortie if x["score"] is not None)
        progres(juge=nom, fin=suivi["statut"], lots_faits=f"{suivi['lots_faits']}/{len(lots)}",
                duree_s=suivi["duree_s"])
        # mémoire rendue avant le juge suivant
        del modeles[nom], m_j, fmt_j
        if nom == agent["nom"]:
            del modele, fmt
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    etat["etape"] = "résumé"
    resume = {"run_source": config["run_source"], "commit_cite": etat["commit_cite"],
              "config_sha256": etat["config_sha256"], "taches_sha256": etat["taches_sha256"],
              "manifeste_source_sha256": etat["manifeste_source_sha256"],
              "episodes_sha256": etat["episodes_sha256"], "arret_source_sha256": etat["arret_source_sha256"],
              "notations_source_sha256": etat["notations_source_sha256"],
              "notations_a_faire": config["notations_a_faire"], "juges": etat["juges"],
              "chargements_s": chargements, "precharges": etat["precharges"], "reglages": reglages,
              "duree_s": round(time.perf_counter() - debut, 1)}
    exiger_sans_signal("avant le résumé")
    ecrire_resultat(racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
    return resume


_signal_term = lever_sur_term


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--taches", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, _signal_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    resume = executer(config, Path("."), a.run_id, a.prereg, a.taches)
    print(json.dumps(resume, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
