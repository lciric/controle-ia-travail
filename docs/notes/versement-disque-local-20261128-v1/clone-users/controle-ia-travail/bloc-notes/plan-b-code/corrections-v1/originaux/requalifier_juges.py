"""Lanceur de l'étape payante du plan B des juges de T0.5 (N-022, voie (a) ; préenregistrement
`prereg/T0.5-plan-B-juges-v1.md`) : requalification sous la rubrique simplifiée RS1, rejeu de la cause profonde, témoin.

Une seule étape, sous un manifeste de run décisif (R1), sur les ensembles finaux scellés du pilote et les notations H.4
scellées du run des notations ; aucun épisode nouveau. Les modules gelés (`MODULES_GELES`, commit `c63d4f1`) sont
importés tels quels. La génération passe toujours par `jouer_episodes` (jamais `generer_lot` en direct) ; la génération
standard de la bibliothèque (`generate`) ne sert qu'au témoin.

Ordre des phases (« Plan d'analyse ») :
1. gardes d'avant le manifeste (liste d'arrêt) ; manifeste ;
2. chargement du 8B ; contrôle du format des deux juges en deux temps : (i) conversation de contrôle de b0, format égal
   au format scellé du début du pilote ; (ii) conversation de contrôle de RS1, transcription incrémentale égale au
   gabarit complet et texte attendu dans l'ouverture ; préchargement du 3B ;
3. requalification du 8B : lots RS1 (mêmes demandes, même ordre, mêmes lots que les notations scellées), garde en
   ligne sur toutes les rangées (garde différée) ; `notations-RS1-8B-decisives.json` écrit « tout ou rien » ; échéance
   depuis le début de son premier lot ;
4. requalification du 3B, chargé hors ligne, formats recontrôlés ; de même ;
5. rejeu du 3B, puis 6. rejeu du 8B (rechargé hors ligne) : palier de production en demi-précision sur L1 et L2
   (`rejeu-<juge>-demi.json`) ; réglages effectifs relus ; conversion exacte en simple précision ; repère de précision ;
   ancrage au noyau « math » ; palier du chemin sur L1 et L2 ; contrôle positif D1 sur L3 (`rejeu-<juge>-simple.json`) ;
   échéance depuis le début de la phase ;
7. témoins de la bibliothèque (8B puis 3B, deux appels chacun) ; `temoins.json` ; échéance depuis le début de la phase ;
8. `resume.json`.

Échéances : chacune se contrôle avant chaque lot, avant le repère, avant l'ancrage et avant chaque appel du témoin ; une
phase échue s'arrête sans écrire son fichier et la suivante commence ; l'échéance globale et le signal TERM arrêtent le
run. Tout arrêt après le manifeste laisse un `arret.json` scellé (étape, motif, statuts des phases et des fichiers),
puis se propage. Les écarts d'équivalence ne sont pas des gardes immédiates : tous sont consignés, puis lus (garde
différée, `lire_requalification`). Les fonctions de bilan de ce module (règle k(n − 1), classement des dépassements, ancrage,
couverture, queues binomiales) sont pures ; le lanceur ne les applique pas pendant le run. La lecture qui fait foi est
celle de `lire_requalification`, écrite à part sur les fonctions gelées : ces bilans en sont un second calcul, comparé
au sien sur les fichiers d'un run jouet (`tests/test_plan_b_integration.py`). Écart connu : une grandeur illisible (NaN)
au palier du chemin est ici « illisible » (contrôles), à la lecture « trop grand » (convention gelée de T0.4).
Lignes de progression : rang et durée de chaque lot, fin de chaque phase ; aucun compte de réponses, aucune grandeur
d'équivalence.

Fichiers écrits sous `diag/<run>/` (statut « écrit » consigné dans `fichiers` du résumé ou de l'arrêt) :
- `notations-RS1-<juge>-decisives.json` : `notations` (champs de `noter_ensembles`, plus la lecture RS1), `garde`
  (rapport d'équivalence de chaque rangée : `rapports`, tolérance, statistique) ;
- `rejeu-<juge>-demi.json` : lots tirés, `rangees` (clé et graine du pilote, longueurs, reproduction, `garde`) ;
- `rejeu-<juge>-simple.json` : réglages relus, conversion, `repere`, `ancrage`, `chemin` et `d1` (`rangees`) ;
- `temoins.json` : par juge, appels (configuration écrite et effective, rangées : longueur, tronquée, complète).
"""
from __future__ import annotations

import argparse
import copy
import gc
import hashlib
import json
import math
import re
import signal
import subprocess
import sys
import time
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch

from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.activations import ecarts_par_jeton, passe_unique
from ..harnais.modeles import empreinte_poids, etats_effectifs, exiger_type_des_poids
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import (ENTROPIE_CITEE, bilan_controle_positif, exiger_code_cite,
                                        exiger_code_importe_sous, exiger_memoire_carte, exiger_memoire_vive, noyau)
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, lire_manifeste, versions
from ..scellement import empreinte, verifier
from .juges_simplifies import controler_format_rs1, jouer_lot_de_notations, messages_de_la_variante
from .lancer_pilote_a import (TACHES_CITEES, charger_format_seul, charger_modele_et_format, controler_format,
                              empreinte_config, memoire_pic_gio, precharger_juges)
from .lire_notations_pilote import charger_notations
from .noter_pilote_a import charger_pilote_note, demandes_decisives, progres
from .pilote_a import charger_taches
from .rubrique import CRITERES, lire_notes
from .rubrique_simplifiee import (RACINE_INVITES_RS1, SEPARATEURS_INTERVALLE, SEPARATEURS_SECOND_NOMBRE,
                                  charger_invite_rs1, empreinte_invite_rs1, exiger_criteres_de_l_invite)

COMMANDE = "python -m controle_ia.environnements.requalifier_juges"
COMMIT_MODULES_GELES = "c63d4f1c073f3b6146729dae0086cd7205cdfa57"
MODULES_GELES = tuple(f"src/controle_ia/environnements/{m}.py" for m in (
    "rubrique", "juges", "pilote_a", "lancer_pilote_a", "lire_pilote", "analyse_pilote", "noter_pilote_a",
    "lire_notations_pilote", "invites")) + tuple(f"src/controle_ia/harnais/{m}.py" for m in (
        "episode", "activations", "modeles", "validation_reelle"))
# chaîne des limites de temps (« Plan d'analyse ») : délai externe = échéance globale + un lot de dépassement (900 s)
# + consignation (120 s) ; plafond de l'amorce = délai externe + KILL (300 s) + seuil de mise en place ; surveillance =
# plafond de l'amorce + 600 s
DUREE_GLOBALE_MAX_S = 23_700
LOT_DE_DEPASSEMENT_S, CONSIGNATION_S, KILL_S, MARGE_SURVEILLANCE_S = 900, 120, 300, 600
VARIANTE_REQUALIFICATION, VARIANTE_REJEU = "RS1", "b0"
CLES = ("mode", "run_pilote", "manifeste_pilote_sha256", "run_notations", "agent", "juges", "lot_juge",
        "max_nouveaux_juge", "temperature_juge", "fils", "episodes_decisifs", "episodes_notes_deux_fois",
        "variante_requalification", "variante_rejeu", "notations_attendues_par_juge", "couches", "tolerance_demi",
        "statistique_demi", "tolerance_simple", "statistique_simple", "borne_diffuse_simple", "rapport_localisation",
        "ancrage_max", "ancrage_max_borne", "couverture_quantile", "couverture_unite", "couverture_jetons",
        "positions_min", "regle_kn", "rangees_min_demi", "rangees_min_simple", "rangees_min_d1", "fraction_min",
        "decalage_d1", "rapport_repere_max", "repere_marge", "lots_rejeu", "temoin_queue", "duree_requalification_s",
        "duree_rejeu_s", "duree_temoins_s", "duree_globale_s", "delai_externe_s", "plafond_amorce_s",
        "surveillance_s", "mise_en_place_seuil_s", "memoire_vive_min_go", "memoire_carte_min_gio", "invite_rs1",
        "controle_intervalles")
CLES_EGALES_AU_PILOTE = ("agent", "juges", "lot_juge", "max_nouveaux_juge", "temperature_juge", "episodes_decisifs",
                         "episodes_notes_deux_fois", "fils")
VERSIONS_EGALES = ("torch", "transformers", "tokenizers", "numpy")
COUVERTURE_UNITE = "jetons générés par la rangée"
# réglages relus avant le palier en simple précision (« Seuil ») : TF32 coupé, réductions en précision réduite coupées,
# précision des produits en simple précision « highest »
REGLAGES_CONFORMES = {"tf32_produits": False, "tf32_cudnn": False, "reduction_reduite_bf16": False,
                      "reduction_reduite_fp16": False, "precision_produits_simple": "highest"}
# intitulés de citation propres à ce préenregistrement (jamais ceux du pilote ou du complément) ; le commit du code se
# lit par `exiger_code_cite`, les tâches et l'entropie par les motifs gelés
CITATIONS = {
    "configuration": re.compile(r"Configuration du plan B \(empreinte canonique\) : `([0-9a-f]{64})`"),
    "run du pilote": re.compile(r"Run du pilote requalifié : `(\d{8}-\d{6}-[A-Za-z0-9_.-]+)`"),
    "manifeste du pilote": re.compile(r"Manifeste du pilote requalifié : `([0-9a-f]{64})`"),
    "épisodes du pilote": re.compile(r"Épisodes du pilote requalifié : `([0-9a-f]{64})`"),
    "tâches": TACHES_CITEES,
    "run des notations": re.compile(r"Run des notations rejoué : `(\d{8}-\d{6}-[A-Za-z0-9_.-]+)`"),
    "manifeste des notations": re.compile(r"Manifeste des notations rejoué : `([0-9a-f]{64})`"),
    "résumé des notations": re.compile(r"Résumé des notations rejoué : `([0-9a-f]{64})`"),
    "invite RS1": re.compile(r"Invite RS1 : `([0-9a-f]{64})`"),
    "index de l'invite RS1": re.compile(r"Index de l'invite RS1 : `([0-9a-f]{64})`"),
    "entropie": ENTROPIE_CITEE,
}
NOTATIONS_CITEES = re.compile(r"Notations rejouées du juge ([A-Za-z0-9_.-]+) : `([0-9a-f]{64})`")

# horloge des échéances (remplacée par les tests pour éprouver les ancrages) ; durées consignées sur la même horloge
_horloge = time.perf_counter


# ---------------------------------------------------------------- configuration et gardes d'avant le manifeste

def _nombre(v) -> bool:
    return not isinstance(v, bool) and isinstance(v, (int, float)) and v == v


def _entier(v) -> bool:
    return not isinstance(v, bool) and isinstance(v, int)


def exiger_config_planb(config: dict) -> None:
    """Configuration complète, bornée et cohérente avec la chaîne des limites de temps ; aucune valeur cachée."""
    manquantes = [c for c in CLES if c not in config]
    if manquantes:
        raise GardeArret(f"configuration du plan B incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    if config["variante_requalification"] != VARIANTE_REQUALIFICATION or config["variante_rejeu"] != VARIANTE_REJEU:
        raise GardeArret(f"variantes {config['variante_requalification']!r}, {config['variante_rejeu']!r} : "
                         f"{VARIANTE_REQUALIFICATION!r} pour la requalification, {VARIANTE_REJEU!r} pour le rejeu")
    noms = [j["nom"] for j in config["juges"]]
    if len(set(noms)) != len(noms) or sum(bool(j.get("meme_modele_que_agent")) for j in config["juges"]) != 1:
        raise GardeArret(f"juges {noms} : noms distincts et un seul juge qui est l'agent attendus")
    for cle in ("duree_requalification_s", "duree_rejeu_s", "couverture_jetons"):
        if not isinstance(config[cle], dict) or sorted(config[cle]) != sorted(noms):
            raise GardeArret(f"{cle} : une valeur par juge attendue ({noms})")
    durees = [(f"requalification {n}", d) for n, d in config["duree_requalification_s"].items()]
    durees += [(f"rejeu {n}", d) for n, d in config["duree_rejeu_s"].items()]
    durees += [("témoins", config["duree_temoins_s"]), ("globale", config["duree_globale_s"])]
    for nom, d in durees:
        if not _nombre(d) or not 0 < d <= DUREE_GLOBALE_MAX_S:
            raise GardeArret(f"durée {nom} {d!r} : un nombre dans ]0 ; {DUREE_GLOBALE_MAX_S}] s attendu")
    g, ext, amorce, surv, mep = (config[k] for k in ("duree_globale_s", "delai_externe_s", "plafond_amorce_s",
                                                       "surveillance_s", "mise_en_place_seuil_s"))
    if not all(_nombre(x) and x > 0 for x in (ext, amorce, surv, mep)) or (
            ext != g + LOT_DE_DEPASSEMENT_S + CONSIGNATION_S or amorce != ext + KILL_S + mep
            or surv != amorce + MARGE_SURVEILLANCE_S):
        raise GardeArret(f"chaîne des limites incohérente : globale {g}, délai externe {ext}, plafond de l'amorce "
                         f"{amorce}, surveillance {surv}, mise en place {mep}")
    for cle in ("notations_attendues_par_juge", "lot_juge", "max_nouveaux_juge", "positions_min", "rangees_min_demi",
                "rangees_min_simple", "rangees_min_d1", "fils"):
        if not _entier(config[cle]) or config[cle] < 1:
            raise GardeArret(f"{cle} {config[cle]!r} : un entier positif attendu")
    if config["lots_rejeu"] != 3:
        raise GardeArret(f"lots_rejeu {config['lots_rejeu']!r} : trois lots (L1, L2, L3) attendus")
    if not _entier(config["decalage_d1"]) or config["decalage_d1"] == 0:
        raise GardeArret(f"decalage_d1 {config['decalage_d1']!r} : un entier non nul attendu")
    if config["statistique_demi"] != "q99" or config["statistique_simple"] != "max":
        raise GardeArret("statistiques : 99e centile en demi-précision, maximum en simple précision")
    for cle in ("tolerance_demi", "tolerance_simple", "borne_diffuse_simple", "rapport_localisation", "ancrage_max",
                "ancrage_max_borne", "rapport_repere_max", "repere_marge", "temperature_juge"):
        if not _nombre(config[cle]) or not config[cle] > 0:
            raise GardeArret(f"{cle} {config[cle]!r} : un nombre positif attendu")
    if not config["borne_diffuse_simple"] > config["tolerance_simple"]:
        raise GardeArret("borne de l'écart diffus sous le seuil du chemin")
    for cle in ("couverture_quantile", "fraction_min", "temoin_queue"):
        if not _nombre(config[cle]) or not 0 < config[cle] <= 1:
            raise GardeArret(f"{cle} {config[cle]!r} : un nombre dans ]0 ; 1] attendu")
    if config["couverture_unite"] != COUVERTURE_UNITE:
        raise GardeArret(f"couverture_unite {config['couverture_unite']!r} : {COUVERTURE_UNITE!r} attendu (R-221)")
    if config["regle_kn"] is not True:
        raise GardeArret("regle_kn : la règle k(n − 1) est gelée (vraie)")
    couches = config["couches"]
    if not isinstance(couches, list) or not couches or not all(_entier(c) and c >= 0 for c in couches):
        raise GardeArret(f"couches {couches!r} : une liste d'entiers attendue")
    ci = config["controle_intervalles"]
    attendu = {"actif": True, "separateurs_intervalle": list(SEPARATEURS_INTERVALLE),
               "separateurs_second_nombre": list(SEPARATEURS_SECOND_NOMBRE)}
    if ci != attendu:
        raise GardeArret(f"controle_intervalles {ci!r} ≠ celui du code {attendu!r}")
    for cle in ("memoire_vive_min_go", "memoire_carte_min_gio"):
        if not _nombre(config[cle]) or config[cle] < 0:
            raise GardeArret(f"{cle} {config[cle]!r} : un nombre positif ou nul attendu")
    inv = config["invite_rs1"]
    if not isinstance(inv, dict) or sorted(inv) != ["identifiant", "racine", "sha256"]:
        raise GardeArret("invite_rs1 : racine, identifiant et sha256 attendus")


def exiger_invites_planb(config: dict) -> dict:
    """Invites du run chargées et contrôlées avant le manifeste : H.3 et H.4 (sceaux, index), RS1 (sceau, index scellé,
    critères du code) ; RS1 est celle que cite la configuration (racine, identifiant, empreinte). Rend aussi
    l'empreinte de son index, que cite le préenregistrement."""
    from .invites import charger_invite

    for ident in ("H3", "H4"):
        charger_invite(ident)
    exiger_criteres_de_l_invite(charger_invite_rs1())
    inv = config["invite_rs1"]
    racine_code = Path(__file__).resolve().parents[3]
    reel = {"racine": RACINE_INVITES_RS1.relative_to(racine_code).as_posix(), "identifiant": "RS1",
            "sha256": empreinte_invite_rs1()}
    ecarts = [k for k in reel if inv.get(k) != reel[k]]
    if ecarts:
        raise GardeArret(f"invite RS1 ≠ celle de la configuration : {ecarts}")
    return {**reel, "index_sha256": empreinte(RACINE_INVITES_RS1 / "index.json")}


def charger_notations_rejouees(racine: Path, config: dict, pilote: dict) -> dict:
    """Run des notations H.4 conforme : manifeste scellé, rattaché au pilote, entropie du pilote ; une seule issue, le
    résumé ; chaque juge « écrit », son fichier scellé et rattaché (fonction gelée `charger_notations`)."""
    noms = [j["nom"] for j in config["juges"]]
    m, sha_m, notations, issue = charger_notations(racine, config["run_notations"], config["run_pilote"], noms)
    if issue["fichier"] != "resume" or any(issue["statuts"][n] != "écrit" for n in noms):
        raise GardeArret(f"run des notations {config['run_notations']} non conforme : issue {issue['fichier']}, "
                         f"statuts {issue['statuts']}")
    entropies = {g.get("entropie") for g in m["graines"].values()}
    entropie_pilote = {g.get("entropie") for g in pilote["manifeste"]["graines"].values()}
    if len(entropies) != 1 or entropies != entropie_pilote:
        raise GardeArret("run des notations : entropie ≠ celle du pilote")
    d = Path(racine) / "diag" / config["run_notations"]
    return {"manifeste": m, "manifeste_sha256": sha_m, "notations": notations,
            "fichiers_sha256": {n: empreinte(d / f"notations-{n}-decisives.json") for n in noms},
            "resume_sha256": empreinte(d / "resume.json")}


def exiger_egal_au_pilote_planb(config: dict, pilote: dict, mode: str) -> None:
    """Paramètres des juges et variante du rejeu égaux à ceux du pilote ; en mode réel, versions égales aussi."""
    cp = pilote["manifeste"]["config"]
    for k in CLES_EGALES_AU_PILOTE:
        if config[k] != cp.get(k):
            raise GardeArret(f"{k} ≠ celui du pilote : aucun réglage des juges ne change (N-022)")
    if config["variante_rejeu"] != cp.get("variante_juge"):
        raise GardeArret("variante du rejeu ≠ variante des notations du pilote")
    if mode == "reel":
        v, vp = versions(), pilote["manifeste"]["versions"]
        ecarts = [b for b in VERSIONS_EGALES if v.get(b) != vp.get(b)]
        if ecarts:
            raise GardeArret(f"versions ≠ celles du pilote : {ecarts}")


def _cle_rs1(cle: str, nom: str) -> str:
    prefixe = f"juge-{nom}/"
    if not cle.startswith(prefixe):
        raise GardeArret(f"clé scellée {cle!r} hors du juge {nom}")
    return f"juge-RS1-{nom}/" + cle[len(prefixe):]


def _sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def demandes_de_l_etape(pilote: dict, par_id: dict, config: dict, nom: str, scellees: list[dict]) -> tuple:
    """Demandes RS1 (clés `juge-RS1-<juge>/…`) et b0 (clés du pilote) d'un juge, dans l'ordre exact des notations H.4
    scellées ; même ensemble noté (empreinte), même nombre ; tout écart arrête."""
    rs1 = demandes_decisives(pilote, par_id, dict(config, variante_juge=VARIANTE_REQUALIFICATION), f"RS1-{nom}")
    b0 = demandes_decisives(pilote, par_id, dict(config, variante_juge=VARIANTE_REJEU), nom)
    n = config["notations_attendues_par_juge"]
    if len(rs1) != n or len(scellees) != n:
        raise GardeArret(f"juge {nom} : {len(rs1)} notations à faire, {len(scellees)} scellées, {n} attendues")
    cles_scellees = [x["cle"] for x in scellees]
    if [d["cle"] for d in b0] != cles_scellees:
        raise GardeArret(f"juge {nom} : ordre des demandes ≠ ordre des notations scellées")
    if [d["cle"] for d in rs1] != [_cle_rs1(c, nom) for c in cles_scellees]:
        raise GardeArret(f"juge {nom} : ordre des demandes RS1 ≠ ordre des notations scellées")
    for d, d_rs1, s in zip(b0, rs1, scellees):
        if not (_sha(d["ensemble"]) == _sha(d_rs1["ensemble"]) == s["ensemble_sha256"]):
            raise GardeArret(f"{s['cle']} : ensemble ≠ ensemble noté sous H.4 (désalignement)")
    return rs1, b0


def graines_du_rejeu(cles: list[str], manifeste_pilote: dict, manifeste_notations: dict) -> dict[str, dict]:
    """Graines du rejeu : celles du pilote, clé à clé, relues par `generateur` (état de contrôle vérifié), égales à
    celles du run des notations, converties en entier comme au complément. Rend, par clé, ce que chaque fichier du
    rejeu consigne (clé et entropie du pilote, clé de dérivation, état de contrôle, graine entière)."""
    gp, gn = manifeste_pilote["graines"], manifeste_notations["graines"]
    sortie = {}
    for cle in cles:
        if cle not in gp or gp[cle] != gn.get(cle):
            raise GardeArret(f"graine du rejeu {cle!r} : absente du pilote, ou ≠ celle du run des notations")
        generateur(gp[cle])                                  # état de contrôle vérifié
        sortie[cle] = {"cle_pilote": cle, "entropie": gp[cle]["entropie"], "spawn_key": gp[cle]["spawn_key"],
                       "etat_controle": gp[cle]["etat_controle"], "graine": graine_entiere(gp[cle])}
    return sortie


def cadre_du_rejeu(scellees: list[dict], lot: int, max_nouveaux: int) -> list[int]:
    """Lots complets (de `lot` notations, dans l'ordre scellé) qui portent au moins une réponse scellée tronquée au
    plafond ; indices à partir de 0, triés."""
    cadre = []
    for k in range(len(scellees) // lot):
        morceau = scellees[k * lot:(k + 1) * lot]
        if any(x["tronquee"] and x["jetons_reponse"] == max_nouveaux for x in morceau):
            cadre.append(k)
    return cadre


def tirer_lots(cadre: list[int], rng: np.random.Generator, n: int = 3) -> list[int]:
    """L1, L2, L3 : tirés sans remise dans le cadre trié, dans l'ordre du tirage (R9 : générateur de la clé
    `rejeu/<juge>/lots`)."""
    if len(cadre) < n:
        raise GardeArret(f"cadre du rejeu de {len(cadre)} lot(s) : au moins {n} attendus")
    return [int(x) for x in rng.choice(np.array(sorted(cadre)), size=n, replace=False)]


def seuil_de_couverture(scellees: list[dict], quantile: float) -> int:
    """Seuil de couverture d'un juge, en jetons générés : quantile des longueurs des réponses H.4 scellées
    (interpolation linéaire), arrondi au-dessus (8B : 3 072 ; 3B : 982,75 → 983)."""
    longueurs = [int(x["jetons_reponse"]) for x in scellees]
    if not longueurs:
        raise GardeArret("aucune réponse scellée : seuil de couverture impossible")
    return int(math.ceil(float(np.quantile(np.array(longueurs, dtype=np.float64), quantile))))


def exiger_modules_geles(racine: Path, commit: str = COMMIT_MODULES_GELES, modules=MODULES_GELES) -> None:
    """Modules gelés réutilisés égaux au commit de référence (modifications non commitées comprises)."""
    absents = [x for x in modules if not (Path(racine) / x).is_file()]
    if absents:
        raise GardeArret(f"modules gelés absents du dépôt : {absents}")
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit, "--", *modules], capture_output=True,
                       text=True)
    if r.returncode == 1:
        raise GardeArret(f"modules gelés modifiés depuis le commit {commit[:12]}")
    if r.returncode != 0:
        raise GardeArret(f"comparaison des modules gelés au commit {commit[:12]} impossible : {r.stderr.strip()}")


def exiger_citations_planb(prereg: Path, attendus: dict, notations_sha256: dict[str, str]) -> int:
    """Chaque citation figure dans le préenregistrement, une seule valeur, égale à l'attendu ; une citation par juge
    pour ses notations H.4 rejouées. Rend l'entropie citée."""
    texte = Path(prereg).read_text(encoding="utf-8")
    trouves = {}
    for nom, rx in CITATIONS.items():
        valeurs = set(rx.findall(texte))
        if len(valeurs) != 1:
            raise GardeArret(f"{prereg} : {nom} cité(e) {'plusieurs fois, différemment' if valeurs else 'nulle part'}")
        trouves[nom] = valeurs.pop()
    for nom, valeur in attendus.items():
        if trouves[nom] != str(valeur):
            raise GardeArret(f"{nom} {str(valeur)[:12]} ≠ {nom} cité {trouves[nom][:12]}")
    cites: dict[str, set] = {}
    for juge, sha in NOTATIONS_CITEES.findall(texte):
        cites.setdefault(juge, set()).add(sha)
    if sorted(cites) != sorted(notations_sha256) or any(len(v) != 1 for v in cites.values()):
        raise GardeArret(f"{prereg} : notations rejouées citées pour {sorted(cites)}, attendues pour "
                         f"{sorted(notations_sha256)}, une fois chacune")
    for juge, sha in notations_sha256.items():
        if next(iter(cites[juge])) != sha:
            raise GardeArret(f"notations rejouées du juge {juge} {sha[:12]} ≠ notations citées")
    return int(trouves["entropie"])


def cles_des_graines_planb(demandes_rs1: dict[str, list], noms: list[str]) -> list[str]:
    """Clés propres à l'étape (R9) : une par notation RS1, tirage des lots et témoin par juge, modèle jouet."""
    cles = [d["cle"] for n in noms for d in demandes_rs1[n]]
    for n in noms:
        cles += [f"rejeu/{n}/lots", f"rejeu/{n}/temoin/L1", f"rejeu/{n}/temoin/L2"]
    return cles + ["modele-jouet"]


# ---------------------------------------------------------------- lancement

def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_taches: str,
             autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config_planb(config)
    mode = config["mode"]
    if mode == "reel" and prereg is None:
        raise GardeArret("run réel du plan B sans préenregistrement : R1 interdit de lancer")
    taches = charger_taches(chemin_taches)
    sha_taches = verifier(chemin_taches)
    invite = exiger_invites_planb(config)
    pilote = charger_pilote_note(racine, config["run_pilote"])
    if pilote["manifeste_sha256"] != config["manifeste_pilote_sha256"]:
        raise GardeArret("manifeste du pilote ≠ celui de la configuration")
    if pilote["arret"].get("partiel", {}).get("taches_sha256") != sha_taches:
        raise GardeArret("tâches ≠ celles du pilote (arret.json, partiel.taches_sha256)")
    exiger_egal_au_pilote_planb(config, pilote, mode)
    notes = charger_notations_rejouees(racine, config, pilote)
    modules_geles = "non contrôlés : code hors de la racine (mode jouet)"
    if prereg is not None or (racine / "src" / "controle_ia").is_dir():
        exiger_modules_geles(racine)
        modules_geles = f"égaux à {COMMIT_MODULES_GELES}"
    commit_cite, entropie = None, None
    if prereg is not None:
        exiger_code_importe_sous(racine)
        commit_cite = exiger_code_cite(racine, Path(prereg))
        attendus = {"configuration": empreinte_config(config), "run du pilote": config["run_pilote"],
                    "manifeste du pilote": pilote["manifeste_sha256"], "épisodes du pilote": pilote["episodes_sha256"],
                    "tâches": sha_taches, "run des notations": config["run_notations"],
                    "manifeste des notations": notes["manifeste_sha256"],
                    "résumé des notations": notes["resume_sha256"], "invite RS1": invite["sha256"],
                    "index de l'invite RS1": invite["index_sha256"]}
        entropie = exiger_citations_planb(Path(prereg), attendus, notes["fichiers_sha256"])
    par_id = {t["identifiant"]: t for t in taches}
    noms = [j["nom"] for j in config["juges"]]
    demandes, cadres, graines_rejeu, couverture = {}, {}, {}, {}
    for n in noms:
        scellees = notes["notations"][n]
        demandes[n] = demandes_de_l_etape(pilote, par_id, config, n, scellees)
        graines_rejeu[n] = graines_du_rejeu([x["cle"] for x in scellees], pilote["manifeste"], notes["manifeste"])
        cadres[n] = cadre_du_rejeu(scellees, config["lot_juge"], config["max_nouveaux_juge"])
        if len(cadres[n]) < config["lots_rejeu"]:
            raise GardeArret(f"juge {n} : cadre du rejeu de {len(cadres[n])} lot(s), {config['lots_rejeu']} exigés")
        couverture[n] = seuil_de_couverture(scellees, config["couverture_quantile"])
        if couverture[n] != config["couverture_jetons"][n]:
            raise GardeArret(f"juge {n} : seuil de couverture recalculé {couverture[n]} ≠ "
                             f"{config['couverture_jetons'][n]} jetons générés")
    memoire_vive = exiger_memoire_vive(config["memoire_vive_min_go"])
    memoire_carte = exiger_memoire_carte(config["memoire_carte_min_gio"])
    cles = cles_des_graines_planb({n: demandes[n][0] for n in noms}, noms)
    # état et début du run calculés avant le manifeste : entre sa création et le bloc qui consigne l'arrêt, plus rien ne
    # s'exécute (comme au complément des notations)
    etat = {"etape": "réglages", "commit_cite": commit_cite, "run_pilote": config["run_pilote"],
            "run_notations": config["run_notations"], "episodes_sha256": pilote["episodes_sha256"],
            "taches_sha256": sha_taches, "config_sha256": empreinte_config(config), "invite_rs1": invite,
            "modules_geles": modules_geles, "memoire_vive": memoire_vive, "memoire_carte_gio": memoire_carte,
            "phases": {}, "fichiers": {}}
    contexte = SimpleNamespace(config=config, racine=racine, mode=mode, pilote=pilote, notes=notes,
                               demandes=demandes, cadres=cadres, graines_rejeu=graines_rejeu, etat=etat)
    debut = _horloge()
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles, entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    try:
        return _apres_manifeste(contexte, chemin_m, manifeste, debut)
    except Exception as e:          # garde, panne, signal TERM, échéance globale : consigné, puis propagé
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(_horloge() - debut, 1)})
        relever_term_apres(e)
        raise


class _PhaseEchue(Exception):
    """Échéance d'une phase atteinte : la phase s'arrête sans écrire son fichier, la suivante commence. Ce n'est pas
    une garde d'arrêt (aucune `GardeArret` n'est jamais attrapée pour continuer)."""


def _avant(cx, echeance_phase: float, quoi: str) -> None:
    """Contrôle d'avant un lot, le repère, l'ancrage ou un appel du témoin : signal TERM et échéance globale arrêtent le
    run ; l'échéance de la phase l'arrête seule."""
    exiger_sans_signal(quoi)
    if _horloge() > cx.echeance_globale:
        raise GardeArret(f"échéance globale de {cx.config['duree_globale_s']} s atteinte {quoi} : arrêt consigné")
    if _horloge() > echeance_phase:
        raise _PhaseEchue(quoi)


def _liberer() -> None:
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def _regler_comme_la_carte() -> None:
    """Mode jouet : les réglages que `regler_determinisme` pose sur la carte (TF32 et réductions en précision réduite
    coupés), posés aussi sur le processeur, pour que la garde des réglages relus s'éprouve en répétition."""
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction = False
    torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction = False
    torch.set_float32_matmul_precision("highest")


def _cfg_b0(config: dict) -> dict:
    return {"variante_juge": VARIANTE_REJEU, "mode": config["mode"]}


def _formats_du_juge(fmt, j: dict, config: dict) -> dict:
    """Contrôle du format en deux temps : b0 (comparé ensuite au format scellé du pilote), puis RS1."""
    return {"b0": controler_format(fmt, j, "juge", _cfg_b0(config)),
            "RS1": controler_format_rs1(fmt, j, config["mode"])}


def _apres_manifeste(cx, chemin_m, manifeste, debut) -> dict:
    config, etat = cx.config, cx.etat
    cx.chemin_m, cx.g = chemin_m, manifeste["graines"]
    cx.echeance_globale = debut + float(config["duree_globale_s"])
    from ..harnais.modeles import noyaux_attention_permis, regler_determinisme

    reglages = regler_determinisme(config["fils"], "cuda" if cx.mode == "reel" else "cpu")
    if cx.mode == "jouet":
        _regler_comme_la_carte()
        reglages["relus"] = etats_effectifs()
    etat["reglages"] = reglages
    etat["etape"] = "tirage des lots du rejeu"
    etat["tirages"] = {}
    for n, cadre in cx.cadres.items():
        lots = tirer_lots(cadre, generateur(cx.g[f"rejeu/{n}/lots"]), config["lots_rejeu"])
        etat["tirages"][n] = {"cadre": cadre, "L1": lots[0], "L2": lots[1], "L3": lots[2],
                              "cle": f"rejeu/{n}/lots"}
    juges = config["juges"]
    agent = next(j for j in juges if j["meme_modele_que_agent"])
    cx.agent = agent
    etat["etape"] = f"chargement du juge {agent['nom']}"
    depart = _horloge()
    modele, fmt = charger_modele_et_format(config["agent"], cx.mode, graine_entiere(cx.g["modele-jouet"]))
    cx.chargements = {f"requalification-{agent['nom']}": round(_horloge() - depart, 1)}
    etat["etape"] = "contrôle du format"
    cx.formats = {}
    for j in juges:
        fmt_j = fmt if j["meme_modele_que_agent"] else charger_format_seul(j, cx.mode)
        cx.formats[j["nom"]] = _formats_du_juge(fmt_j, j, config)
        if cx.formats[j["nom"]]["b0"] != cx.pilote["formats"].get(f"juge-{j['nom']}"):
            raise GardeArret(f"juge {j['nom']} : format (b0) ≠ celui du début du pilote")
    etat["formats"] = cx.formats
    etat["etape"] = "préchargement des juges"
    etat["precharges"] = precharger_juges(config)
    cx.noyaux = noyaux_attention_permis() if torch.cuda.is_available() else None

    # 3, 4 : requalification, le 8B puis les autres juges ; le 3B reste chargé pour son rejeu (mode réel)
    charges = {agent["nom"]: (modele, fmt)}
    del modele, fmt
    for j in juges:
        nom = j["nom"]
        if nom not in charges:
            etat["etape"] = f"chargement du juge {nom}"
            depart = _horloge()
            charges[nom] = charger_modele_et_format(j, cx.mode, graine_entiere(cx.g["modele-jouet"]) + 1,
                                                    hors_ligne=True)
            cx.chargements[f"requalification-{nom}"] = round(_horloge() - depart, 1)
            if _formats_du_juge(charges[nom][1], j, config) != cx.formats[nom]:
                raise GardeArret(f"{nom} : format chargé hors ligne ≠ format contrôlé au début du run")
        _requalifier(cx, j, *charges[nom])
        if j["meme_modele_que_agent"]:
            del charges[nom]
            _liberer()

    # 5, 6 : rejeu, les autres juges d'abord (le 3B, déjà chargé en mode réel), le 8B en dernier (rechargé hors ligne)
    for j in [x for x in juges if not x["meme_modele_que_agent"]] + [agent]:
        deja = charges.pop(j["nom"], None) if cx.mode == "reel" else None
        charges.pop(j["nom"], None)
        _rejouer(cx, j, deja)
        del deja
        _liberer()

    # 7 : témoins, le 8B puis les autres juges
    _temoins(cx, [agent] + [x for x in juges if not x["meme_modele_que_agent"]])

    etat["etape"] = "résumé"
    resume = {k: etat[k] for k in ("commit_cite", "run_pilote", "run_notations", "episodes_sha256", "taches_sha256",
                                   "config_sha256", "invite_rs1", "modules_geles", "memoire_vive", "memoire_carte_gio",
                                   "tirages", "formats", "precharges", "reglages", "phases", "fichiers")}
    resume.update(chargements_s=cx.chargements, duree_s=round(_horloge() - debut, 1))
    exiger_sans_signal("avant le résumé")
    ecrire_resultat(cx.racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
    return resume


def _suivi(cx, phase: str, fichiers: list[str], **champs) -> dict:
    suivi = {"statut": "en cours", "fichiers": fichiers, **champs}
    cx.etat["phases"][phase] = suivi
    for f in fichiers:
        cx.etat["fichiers"][f] = "en cours"
    return suivi


def _echue(cx, suivi: dict) -> None:
    suivi["statut"] = "échu"
    for f in suivi["fichiers"]:
        if cx.etat["fichiers"][f] != "écrit":
            cx.etat["fichiers"][f] = "échu"


def _ecrire(cx, nom: str, contenu: dict) -> None:
    ecrire_resultat(cx.racine, cx.chemin_m, nom, contenu)
    cx.etat["fichiers"][nom] = "écrit"


# ---------------------------------------------------------------- requalification

def _requalifier(cx, j: dict, modele, fmt) -> None:
    """Requalification d'un juge sous RS1 : lots de `lot_juge` dans l'ordre scellé, garde en ligne sur toutes les
    rangées (garde différée), fichier écrit « tout ou rien ». Échéance depuis le début du premier lot."""
    config, nom = cx.config, j["nom"]
    cx.etat["etape"] = f"requalification par {nom}"
    fichier = f"notations-RS1-{nom}-decisives"
    demandes = cx.demandes[nom][0]
    lot = config["lot_juge"]
    lots = [demandes[k:k + lot] for k in range(0, len(demandes), lot)]
    suivi = _suivi(cx, f"requalification-{nom}", [fichier], lots=len(lots), lots_faits=0)
    graines = {d["cle"]: graine_entiere(cx.g[d["cle"]]) for d in demandes}
    memoire_pic_gio()
    notations, gardes, jetons = [], [], 0
    depart = _horloge()
    echeance = depart + float(config["duree_requalification_s"][nom])
    suivi["echeance"] = {"ancre": "début du premier lot", "duree_s": config["duree_requalification_s"][nom]}
    for k, morceau in enumerate(lots, 1):
        try:
            _avant(cx, echeance, f"avant le lot {k} de la requalification de {nom}")
        except _PhaseEchue:
            _echue(cx, suivi)
            break
        t0 = _horloge()
        lignes = jouer_lot_de_notations(modele, fmt, morceau, graines, VARIANTE_REQUALIFICATION, config["couches"],
                                        config["max_nouveaux_juge"], config["temperature_juge"],
                                        config["tolerance_demi"], config["statistique_demi"])
        for x in lignes:
            notations.append(x["notation"])
            gardes.append({"cle": x["notation"]["cle"], **x["rapport"]})
            jetons += x["notation"]["jetons_reponse"]
        del lignes
        suivi["lots_faits"] = k
        # rang et durée du lot seulement : aucun compte de réponses, aucune grandeur d'équivalence
        progres(phase="requalification", juge=nom, lot=f"{k}/{len(lots)}", duree_s=f"{_horloge() - t0:.1f}")
    suivi["duree_s"] = round(_horloge() - depart, 1)
    suivi["memoire_pic_gio"] = memoire_pic_gio()
    if suivi["statut"] == "en cours":
        _ecrire(cx, fichier, {
            "juge": nom, "variante": VARIANTE_REQUALIFICATION, "invite_rs1": cx.etat["invite_rs1"],
            "notations": notations,
            "garde": {"tolerance": config["tolerance_demi"], "statistique": config["statistique_demi"],
                      "couches": config["couches"], "rapports": gardes},
            "noyau": "défaut de la bibliothèque", "noyaux_permis": cx.noyaux,
            "descriptifs": {"duree_s": suivi["duree_s"], "memoire_pic_gio": suivi["memoire_pic_gio"],
                            "jetons_generes": jetons, "lots": len(lots),
                            "jetons_contexte_min": min(x["jetons_contexte"] for x in notations),
                            "jetons_contexte_max": max(x["jetons_contexte"] for x in notations)}})
        suivi["statut"] = "écrit"
    progres(phase="requalification", juge=nom, fin=suivi["statut"], lots_faits=f"{suivi['lots_faits']}/{len(lots)}",
            duree_s=suivi["duree_s"])


# ---------------------------------------------------------------- rejeu

def exiger_reglages_conformes(relus: dict) -> None:
    """Garde d'avant le palier en simple précision : réglages effectifs relus conformes (« Seuil »)."""
    ecarts = {k: relus.get(k) for k, v in REGLAGES_CONFORMES.items() if relus.get(k) != v}
    if ecarts:
        raise GardeArret(f"réglages effectifs non conformes avant le palier en simple précision : {ecarts}")


def empreinte_poids_en_bfloat16(modele) -> str:
    """Empreinte des poids ramenés en bfloat16, calculée comme `empreinte_poids` pour des poids en bfloat16 : après une
    conversion exacte depuis bfloat16, elle égale l'empreinte d'avant la conversion (aller et retour)."""
    h = hashlib.sha256()
    for nom, p in sorted(modele.state_dict().items()):
        t = p.detach().to(torch.bfloat16).to("cpu").contiguous()
        h.update(f"{nom}/{t.dtype}".encode("utf-8"))
        h.update(t.view(torch.int16).numpy().tobytes())
    return h.hexdigest()


def convertir_en_simple(modele, convertir=None):
    """Conversion des poids de bfloat16 en simple précision, exacte (bfloat16 ⊂ float32) : type relu avant et après,
    puis aller et retour contrôlé (empreinte des poids ramenés en bfloat16 = empreinte d'avant). `convertir` : la
    conversion, remplaçable par les tests seulement (artefact). Rend le modèle converti et le constat."""
    exiger_type_des_poids(modele, "bfloat16")
    avant = empreinte_poids(modele)
    modele = (convertir or (lambda m: m.to(torch.float32)))(modele)
    exiger_type_des_poids(modele, "float32")
    apres = empreinte_poids_en_bfloat16(modele)
    if apres != avant:
        raise GardeArret("conversion en simple précision non exacte : poids ramenés en bfloat16 ≠ poids d'origine")
    return modele, {"type_avant": "torch.bfloat16", "type_apres": str(next(modele.parameters()).dtype),
                    "empreinte_bfloat16": avant, "aller_retour_exact": True}


def _resume_ecarts(e: np.ndarray) -> dict:
    return {"jetons": int(e.size), "q50": float(np.quantile(e, 0.5)), "q99": float(np.quantile(e, 0.99)),
            "max": float(e.max())}


def repere_demi_simple(rangees: list[dict], modele_simple, couches) -> tuple[dict, dict]:
    """Repère de précision : écart relatif par jeton entre la passe unique en demi-précision (celle du palier de
    production, gardée) et la passe unique du modèle converti en simple précision (référence, au dénominateur), sur
    tous les jetons de chaque transcription ; par couche (toutes les rangées) et par rangée. Fonctions gelées
    `passe_unique` et `ecarts_par_jeton`, agrégées comme `repere_precision` (quantiles 0,5 et 0,99, maximum).
    Rend aussi les passes en simple précision par clé (l'ancrage reprend celle de sa rangée)."""
    par_couche = {c: [] for c in couches}
    par_rangee, passes = [], {}
    for r in rangees:
        a32 = passe_unique(modele_simple, r["transcription"], couches)
        ligne = {"lot": r["lot"], "cle": r["cle"], "positions": len(r["transcription"]), "par_couche": {}}
        for c in couches:
            e = ecarts_par_jeton(r["passe"][c], a32[c])
            par_couche[c].append(e)
            ligne["par_couche"][str(c)] = _resume_ecarts(e)
        par_rangee.append(ligne)
        passes[r["cle"]] = a32
    sortie = {"roles": {"numerateur": "‖a_demi − a_simple‖", "denominateur": "‖a_simple‖ (référence)"},
              "noyau": "défaut de la bibliothèque",
              "par_couche": {str(c): _resume_ecarts(np.concatenate(m)) for c, m in par_couche.items()},
              "par_rangee": par_rangee}
    return sortie, passes


def ancrage_noyaux(modele_simple, transcription: list[int], a_defaut: dict, couches) -> dict:
    """Ancrage du seuil du chemin : la rangée passe une fois au noyau « math » ; par couche, maximum sur ses positions
    de l'écart relatif par jeton avec sa passe au noyau par défaut (référence : la passe au noyau « math »)."""
    with noyau("math"):
        a_math = passe_unique(modele_simple, transcription, couches)
    return {"positions": len(transcription), "noyaux": ["défaut de la bibliothèque", "math"],
            "roles": {"numerateur": "‖a_defaut − a_math‖", "denominateur": "‖a_math‖ (référence)"},
            "par_couche": {str(c): float(ecarts_par_jeton(a_defaut[c], a_math[c]).max()) for c in couches}}


def reproduction(regeneree: dict, scellee: dict) -> dict:
    """Égalité d'une réponse H.4 rejouée en demi-précision avec la notation scellée de même clé : empreinte du texte
    décodé, nombre de jetons générés, drapeau « tronquée » (descriptif ; aucune note lue)."""
    if regeneree["cle"] != scellee["cle"]:
        raise GardeArret(f"reproduction : clé {regeneree['cle']} ≠ clé scellée {scellee['cle']}")
    texte = _sha(regeneree["reponse"]) == _sha(scellee["reponse"])
    jetons = regeneree["jetons_reponse"] == scellee["jetons_reponse"]
    tronquee = regeneree["tronquee"] == scellee["tronquee"]
    return {"texte": texte, "jetons": jetons, "tronquee": tronquee, "identique": texte and jetons and tronquee}


def _rangee(lot: str, b: int, ligne: dict, graine: dict) -> dict:
    """Rangée rejouée, sans texte : clé et graine du pilote, longueurs, drapeau « tronquée », rapport de garde."""
    n = ligne["notation"]
    return {"lot": lot, "rang": b, "cle": n["cle"], "graine": graine, "jetons_contexte": n["jetons_contexte"],
            "jetons_generes": n["jetons_reponse"], "tronquee": n["tronquee"],
            "reponse_sha256": _sha(n["reponse"]), "jetons_transcription": ligne["jetons_transcription"],
            "garde": ligne["rapport"]}


def _charger_pour_le_rejeu(cx, j: dict):
    """Juge rechargé en demi-précision, hors ligne (réel) ; mode jouet : le modèle jouet du run des notations (même
    graine), en bfloat16. Format b0 recontrôlé ; type des poids relu."""
    spec = cx.config["agent"] if j["meme_modele_que_agent"] else j
    if cx.mode == "jouet":
        graine = graine_entiere(cx.notes["manifeste"]["graines"]["modele-jouet"]) + (
            0 if j["meme_modele_que_agent"] else 1)
        modele, fmt = charger_modele_et_format(spec, "jouet", graine)
        modele = modele.to(torch.bfloat16)
    else:
        modele, fmt = charger_modele_et_format(spec, "reel", 0, hors_ligne=True)
    if controler_format(fmt, j, "juge", _cfg_b0(cx.config)) != cx.formats[j["nom"]]["b0"]:
        raise GardeArret(f"{j['nom']} : format rechargé ≠ format contrôlé au début du run")
    return modele, fmt


def _lots_du_rejeu(cx, nom: str) -> dict[str, list[dict]]:
    b0 = cx.demandes[nom][1]
    lot, t = cx.config["lot_juge"], cx.etat["tirages"][nom]
    return {L: b0[t[L] * lot:(t[L] + 1) * lot] for L in ("L1", "L2", "L3")}


def _exiger_composition(fmt, demandes: list[dict], scellees: dict[str, dict]) -> None:
    """Composition exacte du lot : mêmes contextes (en jetons) que les notations scellées."""
    for d in demandes:
        msgs, _ = messages_de_la_variante(d, VARIANTE_REJEU)
        n = len(fmt.ouverture(msgs[0]["content"], msgs[1]["content"]))
        if n != scellees[d["cle"]]["jetons_contexte"]:
            raise GardeArret(f"{d['cle']} : contexte de {n} jetons ≠ {scellees[d['cle']]['jetons_contexte']} scellés")


def _rejouer(cx, j: dict, deja) -> None:
    """Rejeu de la cause profonde pour un juge (« Plan d'analyse », phases 5 et 6). Échéance depuis le début de la
    phase, rechargement compris."""
    config, nom = cx.config, j["nom"]
    debut = _horloge()
    echeance = debut + float(config["duree_rejeu_s"][nom])
    demi, simple = f"rejeu-{nom}-demi", f"rejeu-{nom}-simple"
    suivi = _suivi(cx, f"rejeu-{nom}", [demi, simple], echeance={"ancre": "début de la phase, rechargement compris",
                                                                 "duree_s": config["duree_rejeu_s"][nom]})
    etape = f"rejeu du juge {nom}"
    cx.etat["etape"] = etape
    scellees = {x["cle"]: x for x in cx.notes["notations"][nom]}
    graines = {c: r["graine"] for c, r in cx.graines_rejeu[nom].items()}
    lots = _lots_du_rejeu(cx, nom)
    tirage = cx.etat["tirages"][nom]
    couches, T, mx = config["couches"], config["temperature_juge"], config["max_nouveaux_juge"]
    modele = fmt = None
    try:
        if deja is not None:
            modele, fmt = deja
        else:
            cx.etat["etape"] = f"{etape} : chargement"
            depart = _horloge()
            modele, fmt = _charger_pour_le_rejeu(cx, j)
            cx.chargements[f"rejeu-{nom}"] = round(_horloge() - depart, 1)
        exiger_type_des_poids(modele, "bfloat16")
        # palier de production : demi-précision, noyau par défaut, lots L1 et L2, toutes les rangées gardées
        cx.etat["etape"] = f"{etape} : palier de production"
        memoire_pic_gio()
        rangees, gardees = [], []
        for L in ("L1", "L2"):
            _avant(cx, echeance, f"avant le lot {L} du palier de production de {nom}")
            _exiger_composition(fmt, lots[L], scellees)
            t0 = _horloge()
            lignes = jouer_lot_de_notations(modele, fmt, lots[L], graines, VARIANTE_REJEU, couches, mx, T,
                                            config["tolerance_demi"], config["statistique_demi"], garder_passes=True)
            for b, x in enumerate(lignes):
                r = _rangee(L, b, x, cx.graines_rejeu[nom][x["notation"]["cle"]])
                r["reproduction"] = reproduction(x["notation"], scellees[x["notation"]["cle"]])
                rangees.append(r)
                gardees.append({"lot": L, "cle": r["cle"], "transcription": x["transcription"], "passe": x["passe"]})
            del lignes
            progres(phase="rejeu", juge=nom, palier="production", lot=L, duree_s=f"{_horloge() - t0:.1f}")
        _ecrire(cx, demi, {
            "juge": nom, "variante": VARIANTE_REJEU, "tirage": tirage, "rangees": rangees,
            "type_des_poids": str(next(modele.parameters()).dtype), "noyau": "défaut de la bibliothèque",
            "noyaux_permis": cx.noyaux, "reglages_relus": etats_effectifs(),
            "descriptifs": {"duree_s": round(_horloge() - debut, 1), "memoire_pic_gio": memoire_pic_gio(),
                            "contexte_max": max(r["jetons_contexte"] for r in rangees),
                            "jetons_generes_max": max(r["jetons_generes"] for r in rangees),
                            "positions_max": max(r["garde"]["positions_capturees"] for r in rangees),
                            "remplissage_max": max(r["garde"]["lignes"]["remplissage"] for r in rangees)}})
        # palier en simple précision : réglages relus, conversion exacte, repère, ancrage, chemin, D1
        cx.etat["etape"] = f"{etape} : simple précision"
        relus = etats_effectifs()
        exiger_reglages_conformes(relus)
        _avant(cx, echeance, f"avant la conversion et le repère de {nom}")
        modele, conversion = convertir_en_simple(modele)
        repere, passes = repere_demi_simple(gardees, modele, couches)
        cle_ancrage = max((g for g in gardees if g["lot"] == "L1"), key=lambda g: len(g["transcription"]))["cle"]
        transcription_ancrage = next(g["transcription"] for g in gardees if g["cle"] == cle_ancrage)
        a_defaut = passes[cle_ancrage]
        del gardees, passes
        _liberer()
        _avant(cx, echeance, f"avant l'ancrage de {nom}")
        ancrage = {"lot": "L1", "cle": cle_ancrage,
                   **ancrage_noyaux(modele, transcription_ancrage, a_defaut, couches)}
        del a_defaut
        chemin, d1 = [], []
        for L, decalage, sortie in (("L1", 0, chemin), ("L2", 0, chemin), ("L3", config["decalage_d1"], d1)):
            _avant(cx, echeance, f"avant le lot {L} {'du contrôle positif' if decalage else 'du palier du chemin'} "
                                 f"de {nom}")
            t0 = _horloge()
            lignes = jouer_lot_de_notations(modele, fmt, lots[L], graines, VARIANTE_REJEU, couches, mx, T,
                                            config["tolerance_simple"], config["statistique_simple"],
                                            decalage_positions=decalage)
            sortie += [_rangee(L, b, x, cx.graines_rejeu[nom][x["notation"]["cle"]]) for b, x in enumerate(lignes)]
            del lignes
            progres(phase="rejeu", juge=nom, palier="d1" if decalage else "chemin", lot=L,
                    duree_s=f"{_horloge() - t0:.1f}")
        _ecrire(cx, simple, {
            "juge": nom, "variante": VARIANTE_REJEU, "tirage": tirage, "reglages_relus": relus,
            "conversion": conversion, "type_des_poids": str(next(modele.parameters()).dtype),
            "repere": repere, "ancrage": ancrage,
            "chemin": {"tolerance": config["tolerance_simple"], "statistique": config["statistique_simple"],
                       "noyau": "défaut de la bibliothèque", "rangees": chemin},
            "d1": {"lot": "L3", "decalage_positions": config["decalage_d1"], "rangees": d1},
            "couverture": {"seuil_jetons": config["couverture_jetons"][nom], "unite": COUVERTURE_UNITE},
            "noyaux_permis": cx.noyaux,
            "descriptifs": {"duree_s": round(_horloge() - debut, 1), "memoire_pic_gio": memoire_pic_gio()}})
        suivi["statut"] = "écrit"
    except _PhaseEchue:
        _echue(cx, suivi)
    finally:
        del modele, fmt
        _liberer()
    suivi["duree_s"] = round(_horloge() - debut, 1)
    progres(phase="rejeu", juge=nom, fin=suivi["statut"], duree_s=suivi["duree_s"])


# ---------------------------------------------------------------- témoin de la bibliothèque

def configuration_attendue_du_temoin(config: dict, fins, pad: int) -> dict:
    """Configuration effective exigée du témoin (« Métrique ») : tirage, température du juge, tout le vocabulaire (aucun
    filtre par noyau, aucun filtre des k premiers, aucune pénalité), plafond et jetons d'arrêt des notations ; tout ce
    qui pourrait filtrer ou pénaliser est neutre ou absent. La garde la compare à la configuration relue."""
    return {"do_sample": True, "temperature": float(config["temperature_juge"]), "top_k": 0, "top_p": 1.0,
            "min_p": None, "top_h": None, "typical_p": 1.0, "epsilon_cutoff": 0.0, "eta_cutoff": 0.0,
            "repetition_penalty": 1.0, "encoder_repetition_penalty": 1.0, "no_repeat_ngram_size": 0,
            "encoder_no_repeat_ngram_size": 0, "bad_words_ids": None, "suppress_tokens": None,
            "begin_suppress_tokens": None, "sequence_bias": None, "guidance_scale": None,
            "forced_bos_token_id": None, "forced_eos_token_id": None, "exponential_decay_length_penalty": None,
            "renormalize_logits": False, "remove_invalid_values": False, "watermarking_config": None,
            "penalty_alpha": None, "dola_layers": None, "prompt_lookup_num_tokens": None, "num_beams": 1,
            "num_return_sequences": 1, "max_new_tokens": int(config["max_nouveaux_juge"]), "min_new_tokens": None,
            "min_length": 0, "stop_strings": None, "eos_token_id": sorted(int(f) for f in fins),
            "pad_token_id": int(pad), "use_cache": True, "return_dict_in_generate": False, "output_scores": False}


def reglages_du_temoin(config: dict, fins, pad: int) -> dict:
    """Réglages écrits en clair, passés à `generate` par-dessus la configuration du modèle : ceux de la configuration
    attendue, tous écrits (un réglage omis laisserait la valeur du modèle, que la garde verrait)."""
    return dict(configuration_attendue_du_temoin(config, fins, pad))


def configuration_du_temoin(modele, ecrits: dict):
    """Configuration de génération passée à `generate` (celle du modèle, puis les réglages écrits) et configuration
    effective relue par la bibliothèque elle-même (`_prepare_generation_config`, la fonction qu'appelle `generate`)."""
    cfg = copy.deepcopy(modele.generation_config)
    inconnus = cfg.update(**ecrits)
    if inconnus:
        raise GardeArret(f"témoin : réglages inconnus de la bibliothèque {sorted(inconnus)}")
    preparer = getattr(modele, "_prepare_generation_config", None)
    if preparer is None:
        raise GardeArret("témoin : configuration effective illisible (bibliothèque sans _prepare_generation_config)")
    effective, _ = preparer(cfg)
    return cfg, effective


def exiger_configuration_du_temoin(effective, attendue: dict) -> dict:
    """Garde : la configuration effective porte exactement la configuration attendue (température, filtres, pénalités,
    plafond, jetons d'arrêt) ; une configuration par défaut du modèle que les réglages écrits ne remplacent pas arrête.
    Rend la configuration relue, consignée."""
    relue, ecarts = {}, {}
    for k, v in attendue.items():
        e = getattr(effective, k, None)
        if k == "eos_token_id":
            e = sorted(int(x) for x in ([e] if isinstance(e, int) else (e or [])))
        relue[k] = e
        if e != v:
            ecarts[k] = (e, v)
    if ecarts:
        raise GardeArret(f"configuration de génération du témoin ≠ réglages écrits : {ecarts}")
    return relue


def est_refus_de_determinisme(e: BaseException) -> bool:
    """Exception de torch qui refuse un calcul sans version déterministe : erreur d'exécution (ni garde, ni panne de
    mémoire) dont le message nomme les algorithmes déterministes."""
    return (isinstance(e, RuntimeError) and not isinstance(e, (GardeArret, torch.cuda.OutOfMemoryError))
            and "use_deterministic_algorithms" in str(e))


def _remplir_a_gauche(contextes: list[list[int]], pad: int) -> tuple[torch.Tensor, torch.Tensor]:
    L = max(len(c) for c in contextes)
    ids = torch.full((len(contextes), L), int(pad), dtype=torch.long)
    masque = torch.zeros((len(contextes), L), dtype=torch.long)
    for r, c in enumerate(contextes):
        ids[r, L - len(c):] = torch.tensor(c, dtype=torch.long)
        masque[r, L - len(c):] = 1
    return ids, masque


def appel_temoin(modele, fmt, demandes: list[dict], graine: int, config: dict) -> dict:
    """Un appel de la génération standard sur les contextes d'un lot (graine de la bibliothèque posée avant l'appel).
    Rend, par rangée : longueur, fin sans jeton d'arrêt (tronquée), complète ou non selon la lecture gelée de H.4 et la
    règle de troncature. Un refus de déterminisme de torch est consigné « témoin impossible » et le run continue ; toute
    autre exception (panne de mémoire, signal, garde) se propage."""
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    ecrits = reglages_du_temoin(config, fmt.fins, pad)
    cfg, effective = configuration_du_temoin(modele, ecrits)
    relue = exiger_configuration_du_temoin(effective, configuration_attendue_du_temoin(config, fmt.fins, pad))
    contextes = []
    for d in demandes:
        msgs, _ = messages_de_la_variante(d, VARIANTE_REJEU)
        contextes.append(fmt.ouverture(msgs[0]["content"], msgs[1]["content"]))
    ids, masque = _remplir_a_gauche(contextes, pad)
    appareil = next(modele.parameters()).device
    sortie = {"graine": int(graine), "configuration_ecrite": ecrits, "configuration_effective": relue}
    torch.manual_seed(int(graine))
    try:
        with torch.no_grad():
            generes = modele.generate(input_ids=ids.to(appareil), attention_mask=masque.to(appareil),
                                      generation_config=cfg)
    except Exception as e:
        if not est_refus_de_determinisme(e):
            raise
        exiger_sans_signal("pendant le témoin")       # un signal reçu pendant l'appel l'emporte
        return {**sortie, "statut": "témoin impossible", "motif": f"{type(e).__name__}: {str(e)[:500]}"}
    nouveaux = generes[:, ids.shape[1]:].to("cpu").tolist()
    rangees = []
    for d, ctx, jetons in zip(demandes, contextes, nouveaux, strict=True):
        fin = next((k for k, x in enumerate(jetons) if x in fmt.fins), None)
        nv = jetons if fin is None else jetons[:fin + 1]
        tronquee = fin is None
        texte = fmt.tok.decode(nv, skip_special_tokens=True)
        rangees.append({"cle": d["cle"], "jetons_contexte": len(ctx), "jetons_generes": len(nv), "tronquee": tronquee,
                        "complete": bool(lire_notes(texte, CRITERES).complete and not tronquee)})
    return {**sortie, "statut": "fait", "rangees": rangees}


def _temoins(cx, juges: list[dict]) -> None:
    """Témoins de la bibliothèque (phase 7) : chaque juge rechargé en demi-précision, deux appels (contextes de L1, puis
    de L2) ; `temoins.json` écrit « tout ou rien ». Échéance depuis le début de la phase, rechargements compris."""
    config = cx.config
    debut = _horloge()
    echeance = debut + float(config["duree_temoins_s"])
    suivi = _suivi(cx, "temoins", ["temoins"], echeance={"ancre": "début de la phase, rechargements compris",
                                                         "duree_s": config["duree_temoins_s"]})
    cx.etat["etape"] = "témoins"
    sortie = {}
    try:
        for j in juges:
            nom = j["nom"]
            _avant(cx, echeance, f"avant le rechargement de {nom} pour le témoin")
            modele, fmt = _charger_pour_le_rejeu(cx, j)
            exiger_type_des_poids(modele, "bfloat16")
            lots = _lots_du_rejeu(cx, nom)
            scellees = cx.notes["notations"][nom]
            appels = []
            for L in ("L1", "L2"):
                _avant(cx, echeance, f"avant l'appel {L} du témoin de {nom}")
                cle = f"rejeu/{nom}/temoin/{L}"
                t0 = _horloge()
                appel = appel_temoin(modele, fmt, lots[L], graine_entiere(cx.g[cle]), config)
                appels.append({"lot": L, "cle_graine": cle, **appel, "duree_s": round(_horloge() - t0, 1)})
                progres(phase="temoins", juge=nom, appel=L, duree_s=f"{_horloge() - t0:.1f}")
            sortie[nom] = {"appels": appels,
                           "taux_h4": {"tronquees": sum(1 for x in scellees if x["tronquee"]),
                                       "notations": len(scellees)}}
            del modele, fmt
            _liberer()
        _ecrire(cx, "temoins", {"juges": sortie, "noyau": "défaut de la bibliothèque", "noyaux_permis": cx.noyaux,
                                "descriptifs": {"duree_s": round(_horloge() - debut, 1)}})
        suivi["statut"] = "écrit"
    except _PhaseEchue:
        _echue(cx, suivi)
    suivi["duree_s"] = round(_horloge() - debut, 1)
    progres(phase="temoins", fin=suivi["statut"], duree_s=suivi["duree_s"])


# ---------------------------------------------------------------- bilans (fonctions pures, partagées avec la lecture)

def k_angle_mort(n_lues: int) -> int:
    """k(N) = N − ⌊0,99 (N − 1)⌋ : positions qu'une zone doit compter, sur N positions lues, pour atteindre sûrement le
    99e centile (interpolation linéaire ; prereg T0.4 v3, l. 139). Calcul entier, sans arrondi flottant."""
    if not _entier(n_lues) or n_lues < 1:
        raise GardeArret(f"k(N) : N = {n_lues!r}, un entier positif attendu")
    return n_lues - (99 * (n_lues - 1)) // 100


def _sans_nan_bas(v: float) -> float:
    return float("-inf") if v != v else v


def _sans_nan_haut(v: float) -> float:
    return float("inf") if v != v else v


def bilan_controle_negatif_rangees(gardes: list[dict], positions_min: int, regle_kn: bool) -> dict:
    """Contrôle négatif sur des rapports de rangées (champ `garde`) : une rangée est comparable si sa zone générée
    décalée compte au moins `positions_min` positions et, sous la règle k(n − 1), au moins k(n − 1) positions (n : ses
    positions capturées ; n − 1 positions lues sous le décalage) ; sinon elle est courte, comptée à part. Elle passe si,
    à chaque couche, la grandeur de la phase sous le décalage dépasse la tolérance. Sans la règle, même compte que la
    fonction gelée `bilan_controle_negatif`."""
    comparables, passent, courtes, echecs, minimum = 0, 0, 0, [], float("inf")
    statistiques = set()
    for g in gardes:
        stat, tol, zone = g["statistique"], g["tolerance"], g["controle_negatif_zone_generee"]
        statistiques.add(stat)
        if zone is None:
            courtes += 1
            continue
        positions = min(v["positions"] for v in zone.values())
        seuil = positions_min
        if regle_kn:
            seuil = max(seuil, k_angle_mort(int(g["positions_capturees"]) - 1))
        if positions < seuil:
            courtes += 1
            continue
        comparables += 1
        m = min(_sans_nan_bas(v[stat]) for v in zone.values())
        minimum = min(minimum, m)
        if m > tol:
            passent += 1
        else:
            echecs.append(g.get("cle", "?"))
    if len(statistiques) > 1:
        raise GardeArret(f"contrôle négatif : statistiques mêlées ({sorted(statistiques)})")
    return {"comparables": comparables, "passent": passent, "courtes": courtes, "echecs": echecs,
            "fraction": passent / comparables if comparables else None,
            "min_des_grandeurs": minimum if comparables else None, "positions_min": positions_min,
            "regle_kn": regle_kn}


def lire_controle_negatif(bilan: dict, rangees_min: int, fraction_min: float) -> str:
    if bilan["comparables"] < rangees_min:
        return "non concluant"
    return "conforme" if bilan["fraction"] >= fraction_min else "contraire"


def zone_generee_toute_nulle(gardes: list[dict]) -> bool:
    """Trop beau (R4) : aucun écart non nul dans la zone générée de toutes les rangées, à toutes les couches."""
    total = nuls = 0
    for g in gardes:
        for p in g["profils"].values():
            total += p["generee"]["jetons"]
            nuls += p["generee"].get("nuls", 0)
    return total > 0 and nuls == total


def sondes_conformes(gardes: list[dict]) -> bool:
    return all(g["sondes"]["tableaux_distincts"] and g["sondes"]["ulp_vu"] for g in gardes)


def bilan_garde_en_ligne(gardes: list[dict], config: dict) -> dict:
    """Garde en ligne de la requalification d'un juge : conforme si, pour chaque rangée et chaque couche, le 99e
    centile ≤ tolérance ; contrôle négatif sous la règle k(n − 1) ; trop beau ; sondes d'audit."""
    tol = config["tolerance_demi"]
    au_dessus = [g.get("cle", "?") for g in gardes if any(not (v <= tol) for v in g["ecarts_q99"].values())]
    cn = bilan_controle_negatif_rangees(gardes, config["positions_min"], config["regle_kn"])
    cn["lecture"] = lire_controle_negatif(cn, config["rangees_min_demi"], config["fraction_min"])
    return {"rangees": len(gardes), "au_dessus": au_dessus, "equivalence": "contraire" if au_dessus else "conforme",
            "q99_max": max((_sans_nan_haut(v) for g in gardes for v in g["ecarts_q99"].values()), default=None),
            "controle_negatif": cn, "trop_beau": zone_generee_toute_nulle(gardes),
            "sondes_conformes": sondes_conformes(gardes)}


def rapports_au_repere(rangees: list[dict], repere: dict) -> dict:
    """ρ(ℓ) = G_D,max(ℓ) / R(ℓ) par couche, et, rangée par rangée, 99e centile de la rangée sur 99e centile du repère
    de la même rangée. Un repère nul donne +∞ (ou 0 si l'écart l'est aussi)."""
    def rapport(g, r):
        g, r = _sans_nan_haut(g), _sans_nan_haut(r)
        return g / r if r > 0 else (0.0 if g == 0 else float("inf"))

    couches = sorted(repere["par_couche"], key=int)
    gmax = {c: max(_sans_nan_haut(x["garde"]["ecarts_q99"][c]) for x in rangees) for c in couches}
    rho = {c: rapport(gmax[c], repere["par_couche"][c]["q99"]) for c in couches}
    par_cle = {x["cle"]: x for x in repere["par_rangee"]}
    par_rangee = [{"cle": x["cle"], **{c: rapport(x["garde"]["ecarts_q99"][c],
                                                  par_cle[x["cle"]]["par_couche"][c]["q99"]) for c in couches}}
                  for x in rangees]
    return {"G_D_max": gmax, "rho": rho, "par_rangee": par_rangee}


def _normaliser(gardes: list[dict]) -> list[dict]:
    """Clés de couches en chaînes, comme après un passage par JSON (les rapports en mémoire portent des entiers)."""
    sortie = []
    for g in gardes:
        g = dict(g)
        for k in ("ecarts", "ecarts_q99", "profils", "controle_negatif_zone_generee"):
            if isinstance(g.get(k), dict):
                g[k] = {str(c): v for c, v in g[k].items()}
        sortie.append(g)
    return sortie


def lire_palier_production(demi: dict | None, simple: dict | None, config: dict) -> dict:
    """Palier de production (table C), lu dans l'ordre : contrôles (sondes, contrôle négatif sous la règle k(n − 1),
    fichier ou repère absent) ; trop beau ; conforme ; réserve (ρ) ; réserve (au-dessus du seuil), avec la marge du
    seuil par couche."""
    if demi is None or simple is None or not simple.get("repere"):
        return {"lecture": "non concluant", "motif": "fichier ou repère absent"}
    rangees = [dict(x, garde=_normaliser([x["garde"]])[0]) for x in demi["rangees"]]
    gardes = [dict(x["garde"], cle=x["cle"]) for x in rangees]
    cn = bilan_controle_negatif_rangees(gardes, config["positions_min"], config["regle_kn"])
    cn["lecture"] = lire_controle_negatif(cn, config["rangees_min_demi"], config["fraction_min"])
    rr = rapports_au_repere(rangees, simple["repere"])
    tol, rho_max = config["tolerance_demi"], config["rapport_repere_max"]
    sortie = {"controle_negatif": cn, **rr, "sondes_conformes": sondes_conformes(gardes),
              "trop_beau": zone_generee_toute_nulle(gardes)}
    if not sortie["sondes_conformes"] or cn["lecture"] != "conforme":
        return {**sortie, "lecture": "non concluant", "motif": "contrôles"}
    if sortie["trop_beau"]:
        return {**sortie, "lecture": "trop beau"}
    sous = all(v <= tol for v in rr["G_D_max"].values())
    if sous and all(v <= rho_max for v in rr["rho"].values()):
        return {**sortie, "lecture": "conforme"}
    if sous:
        return {**sortie, "lecture": "réserve (ρ)"}
    marges = {c: ("seuil sans marge sur ce run" if not (simple["repere"]["par_couche"][c]["q99"]
                                                        <= config["repere_marge"]) else "défaut possible")
              for c, v in rr["G_D_max"].items() if not (v <= tol)}
    return {**sortie, "lecture": "réserve (au-dessus du seuil)", "marges": marges}


def classer_depassement(ecart: float, max_contexte: float, max_generee: float, ancrage: float, config: dict) -> str:
    """Classement d'un dépassement du palier du chemin (rangée r, couche ℓ, G_S > seuil), dans l'ordre du « Seuil » :
    trop grand ou sans marge (au-dessus de la borne de l'écart diffus), sans marge (ancrage au-dessus de 1e-3),
    décodage, contexte, diffus. Une grandeur illisible (NaN) n'est classée nulle part : « illisible » (lue avec les
    contrôles, jamais comme un défaut ni comme un écart sous un seuil)."""
    a, a_borne, r = config["ancrage_max"], config["ancrage_max_borne"], config["rapport_localisation"]
    if any(x != x for x in (ecart, max_contexte, max_generee, ancrage)):
        return "illisible"
    if not (ecart <= config["borne_diffuse_simple"]):
        return "trop grand" if ancrage <= a_borne else "sans marge"
    if not (ancrage <= a):
        return "sans marge"
    if max_generee > r * max_contexte:
        return "décodage"
    if max_contexte > r * max_generee:
        return "contexte"
    return "diffus"


def couverture_du_chemin(rangees: list[dict], seuil: int) -> dict:
    """Couverture comptée en jetons générés par la rangée (R-221) : au moins une rangée comparée du palier du chemin qui
    a généré au moins `seuil` jetons ; rapporte la plus longue réponse générée et ses positions comparées (une de moins
    que contexte + réponse pour une rangée tronquée : le dernier jeton tiré n'est jamais repassé)."""
    if not rangees:
        return {"atteinte": False, "seuil_jetons": seuil, "jetons_generes_max": None, "positions_comparees": None}
    plus_longue = max(rangees, key=lambda x: x["jetons_generes"])
    return {"atteinte": plus_longue["jetons_generes"] >= seuil, "seuil_jetons": seuil,
            "jetons_generes_max": plus_longue["jetons_generes"],
            "positions_comparees": plus_longue["garde"]["positions_capturees"],
            "zone_generee_comparee": plus_longue["garde"]["positions_capturees"] - plus_longue["jetons_contexte"]}


def lire_palier_chemin(simple: dict | None, config: dict, seuil_couverture: int) -> dict:
    """Palier du chemin (table C), lu dans l'ordre : contrôles (une grandeur illisible y compte : question ouverte à la
    session) ; D1 non probant ; défaut (écart trop grand) ; défaut (décodage) ; seuil sans marge ; contexte ; précision
    probable ; trop beau ; couverture ; fidèle (et réserve si un ancrage dépasse 1e-3)."""
    if simple is None:
        return {"lecture": "non concluant (contrôles)", "motif": "fichier absent"}
    tau = config["tolerance_simple"]
    gardes = [dict(_normaliser([x["garde"]])[0], cle=x["cle"]) for x in simple["chemin"]["rangees"]]
    rangees = [dict(x, garde=g) for x, g in zip(simple["chemin"]["rangees"], gardes)]
    ancrage = {str(c): v for c, v in simple["ancrage"]["par_couche"].items()}
    depassements = []
    for g in gardes:
        for c, e in g["ecarts"].items():
            if not (e <= tau):
                p = g["profils"][c]
                mc = p["contexte"].get("max", 0.0) if p["contexte"]["jetons"] else 0.0
                mg = p["generee"].get("max", 0.0) if p["generee"]["jetons"] else 0.0
                depassements.append({"cle": g["cle"], "couche": c, "ecart": e, "max_contexte": mc, "max_generee": mg,
                                     "ancrage": ancrage[c],
                                     "classe": classer_depassement(e, mc, mg, ancrage[c], config)})
    cn = bilan_controle_negatif_rangees(gardes, config["positions_min"], regle_kn=False)
    cn["lecture"] = lire_controle_negatif(cn, config["rangees_min_simple"], config["fraction_min"])
    d1_gardes = _normaliser([x["garde"] for x in simple["d1"]["rangees"]])
    d1 = bilan_controle_positif([(SimpleNamespace(identifiant=x["cle"]), None,
                                  {"ecarts": {"0,0": g["ecarts"]}, "profils": {"0,0": g["profils"]}})
                                 for x, g in zip(simple["d1"]["rangees"], d1_gardes)],
                                {"tolerance": tau}, {"positions_min": config["positions_min"]})
    if d1["comparables"] < config["rangees_min_d1"]:
        d1["lecture"] = "non concluant"
    else:
        d1["lecture"] = "vu" if d1["fraction"] >= config["fraction_min"] else "non vu"
    reglages_ok = all(simple["reglages_relus"].get(k) == v for k, v in REGLAGES_CONFORMES.items())
    couverture = couverture_du_chemin(rangees, seuil_couverture)
    sortie = {"depassements": depassements, "controle_negatif": cn, "d1": d1, "ancrage": ancrage,
              "reserve_ancrage": any(not (v <= config["ancrage_max"]) for v in ancrage.values()),
              "couverture": couverture, "reglages_conformes": reglages_ok,
              "sondes_conformes": sondes_conformes(gardes), "trop_beau": zone_generee_toute_nulle(gardes)}
    classes = {x["classe"] for x in depassements}
    if (not reglages_ok or not sortie["sondes_conformes"] or cn["lecture"] != "conforme"
            or d1["lecture"] != "vu" or "illisible" in classes):
        return {**sortie, "lecture": "non concluant (contrôles)"}
    if not (d1["max_contexte"] is not None and d1["max_contexte"] <= tau):
        return {**sortie, "lecture": "non concluant (D1 non probant)"}
    for classe, lecture in (("trop grand", "défaut (écart trop grand)"), ("décodage", "défaut (décodage)"),
                            ("sans marge", "non concluant (seuil sans marge)"),
                            ("contexte", "non concluant (contexte)"), ("diffus", "non concluant, précision probable")):
        if classe in classes:
            return {**sortie, "lecture": lecture}
    if sortie["trop_beau"]:
        return {**sortie, "lecture": "trop beau"}
    if not couverture["atteinte"]:
        return {**sortie, "lecture": "non concluant (couverture)"}
    return {**sortie, "lecture": "fidèle"}


def queues_binomiales(p: float, n: int = 16, queue: float = 0.005) -> dict:
    """Valeurs de T_w (tronquées sur n) dans une queue de probabilité inférieure à `queue` sous la loi binomiale exacte
    (n, p) : queue basse P(X ≤ t) < queue, queue haute P(X ≥ t) < queue (8B, p = 60/180 : 0 ou au moins 11 ; 3B,
    p = 9/180 : au moins 5)."""
    if not 0 <= p <= 1 or n < 1:
        raise GardeArret(f"loi binomiale ({n}, {p}) invalide")
    pmf = [math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]
    basse = [t for t in range(n + 1) if sum(pmf[:t + 1]) < queue]
    haute = [t for t in range(n + 1) if sum(pmf[t:]) < queue]
    return {"basse": basse, "haute": haute}


def bilan_temoin(temoin_juge: dict, queue: float) -> dict:
    """Témoin d'un juge : T_w (tronquées sur les rangées des appels faits) comparé au taux H.4 global du juge ; un appel
    « témoin impossible » laisse T_w non calculé (aucune lecture n'en dépend)."""
    appels = temoin_juge["appels"]
    taux = temoin_juge["taux_h4"]
    p = taux["tronquees"] / taux["notations"]
    if any(a["statut"] != "fait" for a in appels):
        return {"T_w": None, "rangees": None, "declenche": False, "motif": "témoin impossible", "p": p}
    rangees = [r for a in appels for r in a["rangees"]]
    t_w = sum(1 for r in rangees if r["tronquee"])
    q = queues_binomiales(p, len(rangees), queue)
    return {"T_w": t_w, "rangees": len(rangees), "p": p, "queues": q, "declenche": t_w in q["basse"] + q["haute"]}


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
