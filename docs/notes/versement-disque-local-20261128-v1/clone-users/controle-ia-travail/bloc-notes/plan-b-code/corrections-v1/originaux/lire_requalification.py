"""Lecture de l'étape du plan B des juges de T0.5 : requalification sous la rubrique RS1 et rejeu de la cause profonde
(préenregistrement `prereg/T0.5-plan-B-juges-v1.md` : « Plan d'analyse », « Lecture » ; « Critères de lecture gelés »,
tables A à E ; « Liste d'arrêt », « À la lecture »).

Module mince, sur processeur, sous son propre manifeste. Il ne calcule rien que les fonctions gelées ne calculent déjà
(`lire_pilote` : `_ouvrir_analyse`, `charger_pilote`, `mesures_format`, `empreintes_des_ensembles`, `notes_alignees`,
`lecture_juge`, `declencheurs_audit`, `tirer_relectures`, `statut`, `_si`, `_serialisable` ; `analyse_pilote` :
`difference_appariee` ; `lire_notations_pilote` : `charger_notations`, `exiger_run_sous_prereg` ; `harnais.episode` :
`bilan_controle_negatif` ; `harnais.validation_reelle` : `bilan_controle_positif`, `_maximum`), sauf ce que le texte lui
donne : la lecture RS1 (`rubrique_simplifiee.lire_reponse_rs1`, contrôle des intervalles compris), la règle k(n − 1), le
classement des dépassements, l'ancrage couche par couche, la couverture en jetons générés, les bilans du rejeu et le
témoin. Tous les seuils sont des constantes gelées de ce module ; ceux que la configuration de l'étape porte doivent lui
être égaux (`CONSTANTES_CONFIG`).

Gardes (« À la lecture ») : celles d'`_ouvrir_analyse` (préenregistrement du pilote intact, modules de lecture égaux au
commit cité par le pilote, constantes et version de numpy du manifeste de la première lecture) ; run de l'étape décisif,
en mode réel, lancé sous le préenregistrement donné, scellé et intact (`exiger_run_sous_prereg`) ; configuration du run
rattachée au pilote et au run des notations H.4 ; issue unique (`resume.json` ou `arret.json`), scellée, rattachée ;
statuts des phases d'accord avec les fichiers ; chaque fichier scellé et rattaché au run ; modules neufs égaux au commit
du run ; modules gelés réutilisés égaux à `c63d4f1` ; notations alignées (`notes_alignees`) ; lecture RS1 recalculée
égale à celle consignée ; seuils de couverture recalculés égaux à 3 072 et 983 ; arbre propre et identifiant neuf à
l'écriture (`creer_manifeste`). Un arrêt n'écrit rien : ni manifeste, ni `lecture-planb.json`.

Format lu : celui qu'écrit `requalifier_juges` (fichiers de `diag/<run de l'étape>/` ; le texte ne fixe que leurs noms).
Le rapport de garde d'une rangée y est celui de `juges_simplifies.rapport_de_la_rangee` : tolérance, statistique et
clés gardées par le pilote (`CLES_RAPPORT_GARDEES`), sans la clé de comparaison ; la lecture le remet sous la forme
d'un rapport de `jouer_episodes` (`rapport_de_jouer_episodes` : une comparaison « 0,0 », `episode` = clé de la rangée),
que lisent les fonctions gelées.
- `resume.json` (`fichiers`) ou `arret.json` (`etape`, `motif`, `partiel.fichiers`) : `fichiers[<nom du fichier sans
  .json>]` = « écrit », « en cours » ou « échu » ; « écrit » exactement pour les fichiers présents ; tout autre nom de
  fichier ou statut arrête ;
- `notations-RS1-<J>-decisives.json` : `notations` (champs de `noter_ensembles` : `cle` = `juge-RS1-<J>/<tâche>/e<k>/
  passe-<p>`, `variante` = RS1, `jetons_contexte`, `ensemble_sha256`, `jetons_reponse`, `tronquee`, `notes`,
  `anomalies`, `score`, `reponse` ; plus `complete_sans_troncature` et `lecture_rs1`) ; `garde.rapports` : un rapport
  de rangée par notation (`cle`, tolérance 0,2, 99e centile) ; `descriptifs` et `noyaux_permis`, rapportés ;
- `rejeu-<J>-demi.json` : `rangees`, 16 (L1, L2) : `cle` (clé H.4 du pilote), `lot`, `jetons_generes`, `tronquee`,
  `reponse_sha256` (réponse rejouée), `garde` (99e centile, 0,2), `reproduction` (`identique`, consigné par le
  lanceur, recalculé ici) ;
- `rejeu-<J>-simple.json` : `reglages_relus` (`etats_effectifs`) ; `repere` (`par_couche` et `par_rangee`, liste de
  rangées `cle`, `par_couche`) ; `ancrage` (`cle`, `positions`, `par_couche` : R_S) ; `chemin.rangees`, 16 (`cle`,
  `lot`, `jetons_generes`, `garde` au maximum, 3e-3) ; `d1.rangees`, 8 de L3 (`cle`, `lot`, `garde`) ;
- `temoins.json` : `juges[<J>]` : `appels` (`lot`, `statut` « fait » avec `rangees` : `cle`, `jetons_generes`,
  `tronquee`, `complete` ; ou « témoin impossible » avec `motif`) et `taux_h4` (`tronquees`, `notations`).
Sortie : `diag/<run de lecture>/lecture-planb.json`, scellée ; drapeau « lecture suspendue » si l'audit se déclenche.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

import numpy as np

from ..gardes import GardeArret
from ..harnais.episode import bilan_controle_negatif
from ..harnais.validation_reelle import _maximum, bilan_controle_positif
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, graines, lire_manifeste, verifier_resultat
from ..scellement import empreinte
from .analyse_pilote import difference_appariee
from .juges_simplifies import CLE_ACTION
from .lire_notations_pilote import charger_notations, exiger_run_sous_prereg
from .lire_pilote import (NIVEAU, TACHES_COMPLETES_MIN, TIRAGES, _ouvrir_analyse, _serialisable, _si, charger_pilote,
                          declencheurs_audit, empreintes_des_ensembles, lecture_juge, mesures_format, notes_alignees,
                          statut, tirer_relectures)
from .pilote_a import CLES_RAPPORT_GARDEES
from .rubrique_simplifiee import SEPARATEURS_INTERVALLE, SEPARATEURS_SECOND_NOMBRE, lire_reponse_rs1

COMMANDE = "python -m controle_ia.environnements.lire_requalification"
# modules gelés réutilisés, comparés au commit de référence (« Code à écrire et tests »)
COMMIT_GELES = "c63d4f1c073f3b6146729dae0086cd7205cdfa57"
MODULES_GELES = tuple(f"src/controle_ia/environnements/{m}.py" for m in (
    "rubrique", "juges", "pilote_a", "lancer_pilote_a", "lire_pilote", "analyse_pilote", "noter_pilote_a",
    "lire_notations_pilote", "invites")) + tuple(f"src/controle_ia/harnais/{m}.py" for m in (
        "episode", "activations", "modeles", "validation_reelle"))
# modules neufs de l'étape, comparés au commit du run
MODULES_PLANB = tuple(f"src/controle_ia/environnements/{m}.py" for m in (
    "rubrique_simplifiee", "juges_simplifies", "requalifier_juges", "lire_requalification"))
JUGES = ("8B", "3B")
VARIANTE = "RS1"


def fichiers_de_phase(juges: tuple = JUGES) -> tuple[str, ...]:
    """Noms (sans .json) des fichiers de phase qu'écrit le lanceur pour ces juges (l'agent d'abord), dans l'ordre des
    phases (« Ordre des phases ») : requalifications, rejeu des autres juges puis de l'agent, témoins."""
    return (tuple(f"notations-RS1-{j}-decisives" for j in juges)
            + tuple(f"rejeu-{j}-{p}" for j in reversed(juges) for p in ("demi", "simple")) + ("temoins",))


FICHIERS = fichiers_de_phase()
CONSEQUENCES_ABSENT = {  # table E, « fichier d'une phase absent »
    **{f"notations-RS1-{j}-decisives": f"requalification du {j} : nœud (jamais renoté dans cette étape)"
       for j in JUGES},
    **{f"rejeu-{j}-demi": f"rejeu du {j}, palier de production : non concluant" for j in JUGES},
    **{f"rejeu-{j}-simple": f"rejeu du {j}, palier du chemin et repère : non concluant" for j in JUGES},
    "temoins": "témoin non rapporté"}
STATUTS_FICHIER = ("écrit", "en cours", "échu")   # statuts qu'écrit le lanceur (`fichiers` de l'issue)
COUCHES = ("7", "15", "23")                 # couches comparées, clés textuelles des fichiers scellés
CLES_RAPPORT = ("episode", "tolerance", "statistique", "ecarts", "ecarts_q99", "controle_negatif_zone_generee",
                "profils", "longueurs_contexte", "positions_capturees", "lignes", "sondes")
# rapport d'une rangée tel que l'écrit le lanceur (`juges_simplifies.rapport_de_la_rangee`)
CLES_GARDE_RANGEE = ("tolerance", "statistique") + CLES_RAPPORT_GARDEES

# --- Seuils gelés (« Seuil » ; configuration de l'étape) ------------------------------------------------------------
TOLERANCE_DEMI = 0.2                        # garde en ligne et palier de production : 99e centile
TOLERANCE_SIMPLE = 3e-3                     # palier du chemin : maximum
BORNE_DIFFUSE = 1e-2                        # « trop grand » au-dessus
RAPPORT_LOCALISATION = 3.0                  # « décodage » ou « contexte » : une zone plus de 3 fois l'autre
ANCRAGE_MAX = 1e-3                          # marge du seuil de 3e-3, couche par couche
ANCRAGE_MAX_BORNE = 1e-2 / 3                # marge de la borne de 1e-2, couche par couche
POSITIONS_MIN = 4
RANGEES_MIN_DEMI = 10                       # garde en ligne et palier de production
RANGEES_MIN_SIMPLE = 10
RANGEES_MIN_D1 = 6
FRACTION_MIN = 0.95
RAPPORT_REPERE_MAX = 3.0                    # ρ(ℓ) = G_D,max(ℓ) / R(ℓ)
REPERE_MARGE = 0.1                          # R(ℓ) au-dessus : le seuil de 0,2 n'a plus sa marge sur ce run
REPERE_AUDIT = 0.2                          # R(ℓ) au-dessus : déclencheur d'audit
COUVERTURE_QUANTILE = 0.75
SEUILS_COUVERTURE = {"8B": 3072, "3B": 983}  # recalculés sur les notations H.4 scellées ; tout écart arrête
COUVERTURE_UNITE = "jetons générés par la rangée"
TEMOIN_QUEUE = 0.005
TEMOIN_TIRAGES = 16
SOMME_FREQUENTE_MAX = 0.5                   # effondrement des notes : plus de 50 % des réponses complètes
RANGEES_REJEU, RANGEES_D1 = 16, 8
REGLAGES_CONFORMES = {"tf32_produits": False, "tf32_cudnn": False, "reduction_reduite_bf16": False,
                      "reduction_reduite_fp16": False, "precision_produits_simple": "highest"}
PREDICTIONS_PB = {"PB1": {"confirmee_max": 0.05, "refutee_au_dela": 0.20},
                  "PB3": {"taches_min": TACHES_COMPLETES_MIN},
                  "PB4": {"confirmee": [0.4, 0.8], "permise": [0.2, 0.95]},
                  "PB9": {"rangees": 2 * RANGEES_REJEU},
                  "PB10": {"confirmee_max": 150, "refutee_au_dela": 400}}
# clés de la configuration de l'étape que ce module lit comme seuils (« Configuration ») : égalité exigée
CONSTANTES_CONFIG = {"variante_requalification": VARIANTE, "variante_rejeu": "b0", "couches": [7, 15, 23],
                     "tolerance_demi": TOLERANCE_DEMI, "statistique_demi": "q99", "tolerance_simple": TOLERANCE_SIMPLE,
                     "statistique_simple": "max", "borne_diffuse_simple": BORNE_DIFFUSE,
                     "rapport_localisation": RAPPORT_LOCALISATION, "ancrage_max": ANCRAGE_MAX,
                     "ancrage_max_borne": ANCRAGE_MAX_BORNE, "couverture_quantile": COUVERTURE_QUANTILE,
                     "positions_min": POSITIONS_MIN, "regle_kn": True, "rangees_min_demi": RANGEES_MIN_DEMI,
                     "rangees_min_simple": RANGEES_MIN_SIMPLE, "rangees_min_d1": RANGEES_MIN_D1,
                     "fraction_min": FRACTION_MIN, "decalage_d1": 1, "rapport_repere_max": RAPPORT_REPERE_MAX,
                     "repere_marge": REPERE_MARGE, "lots_rejeu": 3, "temoin_queue": TEMOIN_QUEUE,
                     # mêmes seuils de couverture et même contrôle de la lecture RS1 au run et à la lecture
                     "couverture_jetons": SEUILS_COUVERTURE, "couverture_unite": COUVERTURE_UNITE,
                     "controle_intervalles": {"actif": True, "separateurs_intervalle": list(SEPARATEURS_INTERVALLE),
                                              "separateurs_second_nombre": list(SEPARATEURS_SECOND_NOMBRE)}}


def cles_lecture() -> list[str]:
    """Graines de la lecture (R9), dérivées de l'entropie de l'étape (« Graines »)."""
    return [f"analyse/bootstrap-parts-RS1-{j}" for j in JUGES] + ["analyse/bootstrap-difference-RS1",
                                                                   "analyse/audit-RS1"]


def constantes() -> dict:
    """Constantes de lecture, consignées au manifeste de lecture."""
    return json.loads(json.dumps({
        "CONSTANTES_CONFIG": CONSTANTES_CONFIG, "SEUILS_COUVERTURE": SEUILS_COUVERTURE, "REPERE_AUDIT": REPERE_AUDIT,
        "TEMOIN_TIRAGES": TEMOIN_TIRAGES, "SOMME_FREQUENTE_MAX": SOMME_FREQUENTE_MAX, "RANGEES_REJEU": RANGEES_REJEU,
        "RANGEES_D1": RANGEES_D1, "REGLAGES_CONFORMES": REGLAGES_CONFORMES, "PREDICTIONS_PB": PREDICTIONS_PB,
        "COMMIT_GELES": COMMIT_GELES}))


# --- Gardes ------------------------------------------------------------------------------------------------------

def _exiger_egaux_au_commit(racine: Path, modules: tuple, commit: str, quoi: str) -> None:
    absents = [x for x in modules if not (Path(racine) / x).is_file()]
    if absents:
        raise GardeArret(f"{quoi} absents du dépôt : {absents}")
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit, "--", *modules],
                       capture_output=True, text=True)
    if r.returncode == 1:
        raise GardeArret(f"{quoi} modifiés depuis le commit {commit[:12]}")
    if r.returncode != 0:
        raise GardeArret(f"comparaison au commit {commit[:12]} impossible : {r.stderr.strip()}")


def exiger_modules_planb(racine: Path, commit_run: str) -> None:
    """Modules neufs de l'étape égaux au commit du run (modifications non commitées comprises)."""
    _exiger_egaux_au_commit(racine, MODULES_PLANB, commit_run, "modules neufs de l'étape")


def exiger_modules_geles(racine: Path) -> None:
    """Modules gelés réutilisés égaux au commit de référence `COMMIT_GELES`."""
    _exiger_egaux_au_commit(racine, MODULES_GELES, COMMIT_GELES, "modules gelés réutilisés")


def exiger_config_de_l_etape(m: dict, run_pilote: str, sha_pilote: str, run_notations: str) -> None:
    """Run de l'étape rattaché au pilote et au run des notations H.4 ; seuils de sa configuration égaux à ceux de ce
    module (une clé absente est un écart)."""
    c = m["config"]
    attendu = {"run_pilote": run_pilote, "manifeste_pilote_sha256": sha_pilote, "run_notations": run_notations}
    ecarts = {k: c.get(k) for k, v in attendu.items() if c.get(k) != v}
    if ecarts:
        raise GardeArret(f"run de l'étape rattaché ailleurs : {ecarts}")
    # les noms des juges font les noms des fichiers de phase et les clés des notations : ceux du lecteur
    noms = sorted(j.get("nom") for j in c.get("juges") or [] if isinstance(j, dict))
    if noms != sorted(JUGES):
        raise GardeArret(f"juges du run de l'étape {noms} ≠ juges du lecteur {sorted(JUGES)}")
    ecarts = {k: c.get(k, "absente") for k, v in CONSTANTES_CONFIG.items() if k not in c or c[k] != v}
    if ecarts:
        raise GardeArret(f"configuration de l'étape ≠ seuils gelés du lecteur : {ecarts}")


def issue_du_run(racine: Path, run_planb: str) -> dict:
    """Issue consignée du run de l'étape : un seul fichier, `resume.json` ou `arret.json`, scellé et rattaché ; statut
    de chaque phase. Sinon : non lisible, nœud pour tout (table E) ; la lecture s'arrête."""
    d = Path(racine) / "diag" / run_planb
    presents = [n for n in ("resume", "arret") if (d / f"{n}.json").exists()]
    if len(presents) != 1:
        raise GardeArret(f"run de l'étape {run_planb} : {presents or 'ni resume.json ni arret.json'} ; un seul "
                         f"attendu : run non lisible (nœud pour tout)")
    c = verifier_resultat(racine, d / f"{presents[0]}.json")
    if c["run_id"] != run_planb:
        raise GardeArret(f"{presents[0]}.json rattaché au run {c['run_id']}, non à {run_planb}")
    corps = c["resultat"] if presents[0] == "resume" else c["resultat"].get("partiel", {})
    ecrits = corps.get("fichiers") if isinstance(corps, dict) else None
    if not isinstance(ecrits, dict):
        raise GardeArret(f"{presents[0]}.json sans statuts des phases (champ « fichiers ») : run non lisible (nœud "
                         f"pour tout)")
    inconnus = {f: s for f, s in ecrits.items() if f not in FICHIERS or s not in STATUTS_FICHIER}
    if inconnus:
        raise GardeArret(f"{presents[0]}.json : fichiers ou statuts inconnus du lecteur {inconnus} : run non lisible "
                         f"(nœud pour tout)")
    statuts = {f: ecrits.get(f) for f in FICHIERS}
    sortie = {"fichier": presents[0], "statuts": statuts}
    if presents[0] == "arret":
        sortie["arret"] = {"etape": c["resultat"].get("etape"), "motif": c["resultat"].get("motif")}
    return sortie


def charger_fichiers(racine: Path, run_planb: str, issue: dict) -> dict:
    """Fichiers de phase présents, scellés et rattachés au run (None pour un fichier absent), d'accord avec les statuts
    de l'issue : « écrit » exactement pour les fichiers présents."""
    d = Path(racine) / "diag" / run_planb
    fichiers = {}
    for f in FICHIERS:
        chemin = d / f"{f}.json"
        if not chemin.exists():
            fichiers[f] = None
            continue
        c = verifier_resultat(racine, chemin)
        if c["run_id"] != run_planb:
            raise GardeArret(f"{chemin.name} rattaché au run {c['run_id']}, non à {run_planb}")
        fichiers[f] = c["resultat"]
    desaccords = [f for f in FICHIERS if (fichiers[f] is not None) != (issue["statuts"][f] == "écrit")]
    if desaccords:
        raise GardeArret(f"fichiers de phase et statuts de {issue['fichier']}.json en désaccord pour {desaccords} : "
                         f"run non lisible (nœud pour tout)")
    return fichiers


def _champ(d: dict, k: str, quoi: str):
    if not isinstance(d, dict) or k not in d:
        raise GardeArret(f"{quoi} : champ « {k} » absent")
    return d[k]


# --- Seuils recalculés sur les notations H.4 scellées ----------------------------------------------------------------

def seuils_couverture(notations_h4: dict) -> dict:
    """75e centile (interpolation linéaire) des longueurs des réponses H.4 scellées de chaque juge, arrondi au-dessus,
    en jetons générés ; égal à `SEUILS_COUVERTURE`, sinon arrêt."""
    sortie = {}
    for j in JUGES:
        longueurs = [n["jetons_reponse"] for n in notations_h4[j]]
        q = float(np.quantile(longueurs, COUVERTURE_QUANTILE))
        sortie[j] = {"quantile": q, "seuil": math.ceil(q)}
    ecarts = {j: s["seuil"] for j, s in sortie.items() if s["seuil"] != SEUILS_COUVERTURE[j]}
    if ecarts:
        raise GardeArret(f"seuils de couverture recalculés, en jetons générés, {ecarts} ≠ {SEUILS_COUVERTURE}")
    return sortie


def queues_binomiales(p: float, n: int = TEMOIN_TIRAGES, seuil: float = TEMOIN_QUEUE) -> list[int]:
    """Valeurs de T_w (sur n tirages, taux p) dont la queue binomiale exacte, basse ou haute, a une probabilité
    inférieure au seuil (« Seuil », Témoin)."""
    pmf = [math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]
    return [t for t in range(n + 1) if sum(pmf[:t + 1]) < seuil or sum(pmf[t:]) < seuil]


# --- Requalification ---------------------------------------------------------------------------------------------

def relire_notations_rs1(notations: list[dict], juge: str, plafond: int) -> dict:
    """Lecture RS1 refaite sur chaque réponse (`lire_reponse_rs1`) : elle doit redonner les notes, les anomalies, le
    score, la sensibilité sans la règle de troncature et les comptes de lecture consignés (`complete_sans_troncature`,
    `lecture_rs1`), sinon arrêt. Rend les descriptifs de la « Métrique » (longueurs, plafond, anomalies par motif,
    occurrences non chiffrées, intervalles, seconds nombres, contradictions, prose lue comme une note, somme la plus
    fréquente, contextes, sensibilité sans la règle de troncature)."""
    if not notations:
        raise GardeArret(f"juge {juge} : fichier de notations RS1 sans notation")
    motifs, comptes = Counter(), Counter()
    sans_troncature = 0
    for n in notations:
        quoi = f"notation {n.get('cle')}"
        if _champ(n, "variante", quoi) != VARIANTE:
            raise GardeArret(f"{quoi} : variante {n['variante']!r}, {VARIANTE} attendue")
        r = lire_reponse_rs1(_champ(n, "reponse", quoi), _champ(n, "tronquee", quoi))
        consigne = tuple(_champ(n, k, quoi) for k in ("notes", "anomalies", "score", "complete_sans_troncature",
                                                     "lecture_rs1"))
        if (r["notes"], r["anomalies"], r["score"], r["complete_sans_troncature"], r["lecture"]) != consigne:
            raise GardeArret(f"{quoi} : lecture RS1 recalculée ≠ lecture consignée")
        for k in ("non_chiffrees", "intervalles", "seconds_nombres", "invalides_lecture_gelee", "contradictions",
                  "lues_suivies_de_texte"):
            comptes[k] += r["lecture"][k]
        motifs.update(r["lecture"]["motifs"])
        motifs["réponse tronquée"] += int(n["tronquee"])
        sans_troncature += int(not r["complete_sans_troncature"])
    longueurs = [n["jetons_reponse"] for n in notations]
    contextes = [n["jetons_contexte"] for n in notations]
    completes = [n for n in notations if n["score"] is not None]
    sommes = Counter(sum(n["notes"].values()) for n in completes)
    return {"reponses": len(notations), "completes": len(completes),
            "longueur_mediane": float(np.median(longueurs)), "longueur_q99": float(np.quantile(longueurs, 0.99)),
            "longueur_max": max(longueurs), "part_au_plafond": sum(x >= plafond for x in longueurs) / len(longueurs),
            "anomalies_par_motif": dict(sorted(motifs.items())), **dict(sorted(comptes.items())),
            "somme_la_plus_frequente": (sommes.most_common(1)[0][0] if completes else None),
            "part_somme_la_plus_frequente": (max(sommes.values()) / len(completes) if completes else None),
            "contexte_min": min(contextes), "contexte_median": float(np.median(contextes)),
            "contexte_max": max(contextes),
            # sensibilité descriptive « incomplétude sans la règle de troncature » (sans effet sur la table)
            "part_incompletes_sans_troncature": sans_troncature / len(notations)}


def rapport_de_jouer_episodes(garde: dict, cle: str, quoi: str) -> dict:
    """Rapport de `jouer_episodes` remis en forme depuis le rapport d'une rangée tel que l'écrit le lanceur
    (`juges_simplifies.rapport_de_la_rangee` : tolérance, statistique et clés gardées par le pilote, valeurs de
    l'unique comparaison `CLE_ACTION`) : chaque clé gardée sous la comparaison, `episode` = clé de la rangée. Aucune
    valeur n'est recalculée ; une clé absente arrête."""
    if not isinstance(garde, dict):
        raise GardeArret(f"{quoi} : rapport de garde absent ({cle})")
    manquants = [k for k in CLES_GARDE_RANGEE if k not in garde]
    if manquants:
        raise GardeArret(f"{quoi} : rapport sans {manquants}")
    return {"episode": cle, "tolerance": garde["tolerance"], "statistique": garde["statistique"],
            **{k: {CLE_ACTION: garde[k]} for k in CLES_RAPPORT_GARDEES}}


def _rapports_des_rangees(rangees: list[dict], quoi: str) -> list[dict]:
    """Rapports de `jouer_episodes` des rangées d'un fichier du rejeu (champ `garde` de chaque rangée)."""
    return [rapport_de_jouer_episodes(_champ(x, "garde", quoi), x["cle"], quoi) for x in rangees]


def _comparaison(r: dict, tolerance: float, stat: str, quoi: str) -> str:
    """Clé unique de comparaison d'un rapport de `jouer_episodes` (N = 1, T = 1), aux couches, à la tolérance et à la
    statistique gelées ; tout écart de forme arrête."""
    manquants = [k for k in CLES_RAPPORT if k not in r]
    if manquants:
        raise GardeArret(f"{quoi} : rapport sans {manquants}")
    if r["tolerance"] != tolerance or r["statistique"] != stat:
        raise GardeArret(f"{quoi} : tolérance {r['tolerance']} et statistique {r['statistique']!r} ≠ {tolerance} et "
                         f"{stat!r} (seuils gelés)")
    if len(r["ecarts"]) != 1:
        raise GardeArret(f"{quoi} : {len(r['ecarts'])} comparaisons dans le rapport, une attendue")
    cle = next(iter(r["ecarts"]))
    for champ in ("ecarts", "ecarts_q99", "profils"):
        if set((r[champ].get(cle) or {})) != set(COUCHES):
            raise GardeArret(f"{quoi} : couches de « {champ} » ≠ {list(COUCHES)}")
    zone = r["controle_negatif_zone_generee"].get(cle, "absente")
    if zone == "absente" or (zone is not None and set(zone) != set(COUCHES)):
        raise GardeArret(f"{quoi} : contrôle négatif absent ou d'autres couches")
    for champ in ("longueurs_contexte", "positions_capturees", "lignes", "sondes"):
        if cle not in r[champ]:
            raise GardeArret(f"{quoi} : « {champ} » sans la comparaison {cle}")
    return cle


def k_de(n: int) -> int:
    """k(N) = N − ⌊0,99 (N − 1)⌋ : positions décalées qu'il faut, sur N lues, pour que le décalage atteigne sûrement
    le 99e centile (prereg T0.4 v3, l. 139) ; calcul entier."""
    if n < 1:
        raise GardeArret(f"k(N) pour N = {n} : au moins une position attendue")
    return n - (99 * (n - 1)) // 100


def comparable_kn(r: dict) -> tuple[bool, bool]:
    """(comparable, courte par la seule règle k) d'une rangée au 99e centile : sa zone générée décalée compte au moins
    `POSITIONS_MIN` positions et au moins k(n − 1), n étant ses positions capturées (« Métrique »)."""
    cle = next(iter(r["ecarts"]))
    zone = r["controle_negatif_zone_generee"][cle]
    if zone is None:
        return False, False
    decalees = min(v["positions"] for v in zone.values())
    if decalees < POSITIONS_MIN:
        return False, False
    k = k_de(int(r["positions_capturees"][cle]) - 1)
    return decalees >= k, decalees < k


def controle_negatif_kn(rapports: list[dict], rangees_min: int) -> dict:
    """Contrôle négatif au 99e centile : la fonction gelée `bilan_controle_negatif`, appelée sur les seules rangées
    comparables par la règle k(n − 1) ; les autres sont courtes, comptées à part. Lecture : « non concluant » sous
    `rangees_min` rangées comparables ; « conforme » si au moins 95 % dépassent la tolérance à chaque couche ;
    « contraire » sinon."""
    retenus, courtes_kn = [], 0
    for r in rapports:
        oui, par_k = comparable_kn(r)
        courtes_kn += int(par_k)
        if oui:
            retenus.append(r)
    b = bilan_controle_negatif(retenus, positions_min=POSITIONS_MIN)
    b.update(courtes=len(rapports) - len(retenus), courtes_regle_kn=courtes_kn, regle="k(n − 1)")
    b["lecture"] = ("non concluant" if b["comparables"] < rangees_min
                    else "conforme" if b["fraction"] >= FRACTION_MIN else "contraire")
    return b


def zone_generee_toute_nulle(rapports: list[dict]) -> bool:
    """« Trop beau » (R4) : aucun écart non nul dans la zone générée de toutes les rangées, à toutes les couches."""
    jetons = nuls = 0
    for r in rapports:
        cle = next(iter(r["ecarts"]))
        for c in COUCHES:
            z = r["profils"][cle][c]["generee"]
            jetons += z["jetons"]
            nuls += z.get("nuls", 0)
    return jetons > 0 and nuls == jetons


def domaine(rapports: list[dict]) -> dict:
    """Domaine couvert par des rangées comparées (descriptif) : contexte, zone générée comparée, positions et
    remplissage maximaux."""
    d = [(r["longueurs_contexte"][k], r["positions_capturees"][k], _champ(r["lignes"][k], "remplissage", "lignes"))
         for r in rapports for k in [next(iter(r["ecarts"]))]]
    return {"contexte_max": max(x[0] for x in d), "zone_generee_max": max(x[1] - x[0] for x in d),
            "positions_max": max(x[1] for x in d), "remplissage_max": max(x[2] for x in d)}


def _rapportes(fichier: dict, lus: tuple) -> dict:
    """Champs d'un fichier du rejeu que la lecture ne lit pas (durées, mémoire, noyaux, type des poids…) : rapportés
    tels quels."""
    return {k: v for k, v in fichier.items() if k not in lus}


def _sondes_justes(rapports: list[dict]) -> bool:
    s = [r["sondes"][next(iter(r["ecarts"]))] for r in rapports]
    return all(x["tableaux_distincts"] and x["ulp_vu"] for x in s)


def bilan_garde(fichier: dict, juge: str) -> dict:
    """Garde en ligne de la requalification de J, différée : toutes les rangées gardées (une par notation) ; conforme
    si chaque 99e centile ≤ 0,2 ; contrôle négatif par la règle k(n − 1) ; « trop beau »."""
    quoi = f"garde en ligne de {juge}"
    lignes = _champ(_champ(fichier, "garde", quoi), "rapports", quoi)
    rapports = [rapport_de_jouer_episodes(g, _champ(g, "cle", quoi), quoi) for g in lignes]
    cles = [_comparaison(r, TOLERANCE_DEMI, "q99", quoi) for r in rapports]
    gardees = Counter(r["episode"] for r in rapports)
    notees = {n["cle"] for n in fichier["notations"]}
    if set(gardees) != notees or any(v > 1 for v in gardees.values()):
        raise GardeArret(f"{quoi} : rangées gardées ≠ notations (une rangée gardée par notation attendue)")
    au_dessus = [f"{r['episode']}:{c}" for r, k in zip(rapports, cles) for c in COUCHES
                 if not r["ecarts_q99"][k][c] <= TOLERANCE_DEMI]
    neg = controle_negatif_kn(rapports, RANGEES_MIN_DEMI)
    return {"rangees_gardees": len(rapports), "equivalence": "contraire" if au_dessus else "conforme",
            "au_dessus": au_dessus, "q99_max": _maximum(r["ecarts_q99"][k][c] for r, k in zip(rapports, cles)
                                                         for c in COUCHES),
            "controle_negatif": neg, "trop_beau": zone_generee_toute_nulle(rapports),
            "sondes_justes": _sondes_justes(rapports)}


def table_a(juge: str, lecture: dict | None, garde: dict | None, combinee: str) -> dict:
    """Table A pour J : les lignes s'appliquent ensemble ; « nœud » ou « non concluante » prévaut sur « RS1 retenue » ;
    une « réserve » s'ajoute sans changer la lecture. La retenue exige aussi un rejeu sans « défaut du chemin »."""
    if lecture is None:
        return {"issue": "nœud", "lignes": [f"{juge} sans fichier (phase échue ou run arrêté) : nœud ; jamais renoté "
                                            "dans cette étape"], "reserves": []}
    lignes, reserves, noeud = [], [], False
    pb = lecture["plan_b"]
    if pb == "rubrique gardée":
        lignes.append("plan_b = rubrique gardée")
    elif pb == "plan B":
        noeud = True
        lignes.append("plan_b = plan B : nœud ; RS1 échoue aussi ; aucun plan C préenregistré ; proposition à Lazar"
                      + (" ; rappel de la bascule « 8B trop faible » (changement de modèle seulement sur GO ; Q5)"
                         if juge == "8B" else ""))
    else:
        noeud = True
        lignes.append("plan_b = nœud (indécision ou décomposition non concluante) : nœud ; proposition à Lazar")
    if garde["equivalence"] == "contraire" or garde["controle_negatif"]["lecture"] == "contraire":
        noeud = True
        lignes.append("garde en ligne contraire ou contrôle négatif contraire : requalification non concluante "
                      "(instrument) : nœud")
    if garde["controle_negatif"]["lecture"] == "non concluant":
        reserves.append("contrôle négatif de la garde non concluant (moins de 10 rangées comparables) : réserve ; la "
                        "lecture n'en dépend pas")
    if garde["trop_beau"]:
        noeud = True
        reserves.append("garde en ligne : aucun écart non nul dans la zone générée : trop beau (R4), réserve "
                        "maintenue et nœud")
    if combinee == "défaut du chemin":
        noeud = True
        lignes.append("rejeu : défaut du chemin : requalification suspendue, nœud pour les deux juges")
    return {"issue": "nœud" if noeud else "RS1 retenue", "lignes": lignes, "reserves": reserves}


def table_b(issues: dict) -> dict:
    """Table B : usagers, selon les issues des deux juges."""
    retenus = [j for j in JUGES if issues[j] == "RS1 retenue"]
    if len(retenus) == 2:
        return {"retenus": retenus, "lecture": "les deux juges passent à RS1 pour T0.6 et T0.8"}
    if len(retenus) == 1:
        autre = next(j for j in JUGES if j not in retenus)
        return {"retenus": retenus, "lecture": f"le {retenus[0]} sert T0.6 et T0.8 ; le {autre} : proposition à Lazar "
                                               "avant tout usage"}
    return {"retenus": [], "lecture": "nœud pour les deux : proposition à Lazar"}


# --- Rejeu -------------------------------------------------------------------------------------------------------

def _rangees(fichier: dict, champ: str, nombre: int, quoi: str) -> list[dict]:
    rangees = _champ(fichier, champ, quoi)
    if not isinstance(rangees, list) or len(rangees) != nombre:
        raise GardeArret(f"{quoi} : {len(rangees) if isinstance(rangees, list) else 'aucune'} rangée(s), {nombre} "
                         f"attendues")
    cles = [_champ(x, "cle", quoi) for x in rangees]
    if len(set(cles)) != len(cles):
        raise GardeArret(f"{quoi} : rangées en double")
    return rangees


def bilan_production(demi: dict | None, simple: dict | None, juge: str) -> dict:
    """Palier de production (demi-précision), table C, lu dans l'ordre ; la première ligne qui s'applique donne la
    lecture. G_D(r, ℓ) : 99e centile de la rangée ; G_D,max(ℓ) : maximum sur les 16 rangées (NaN compté +∞) ; ρ(ℓ) =
    G_D,max(ℓ) / R(ℓ), R(ℓ) : 99e centile du repère."""
    if demi is None or simple is None:
        return {"lecture": "non concluant", "motifs": ["fichier ou repère absent"]}
    quoi = f"rejeu du {juge}, palier de production"
    rangees = _rangees(demi, "rangees", RANGEES_REJEU, quoi)
    rapports = _rapports_des_rangees(rangees, quoi)
    cles = [_comparaison(r, TOLERANCE_DEMI, "q99", quoi) for r in rapports]
    repere = _champ(simple, "repere", f"rejeu du {juge}, repère")
    glob = _champ(repere, "par_couche", "repère")
    liste = _champ(repere, "par_rangee", "repère")
    if not isinstance(liste, list):
        raise GardeArret(f"rejeu du {juge}, repère : « par_rangee » doit être une liste de rangées")
    par_rangee = {_champ(x, "cle", "repère par rangée"): _champ(x, "par_couche", "repère par rangée") for x in liste}
    if len(par_rangee) != len(liste):
        raise GardeArret(f"rejeu du {juge}, repère par rangée : rangées en double")
    R = {c: float(_champ(_champ(glob, c, "repère global"), "q99", "repère global")) for c in COUCHES}
    g_max = {c: _maximum(r["ecarts_q99"][k][c] for r, k in zip(rapports, cles)) for c in COUCHES}
    rho = {c: (g_max[c] / R[c] if R[c] > 0 else float("nan")) for c in COUCHES}
    localisation = {}
    for x, r, k in zip(rangees, rapports, cles):
        rr = {c: _champ(_champ(_champ(par_rangee, x["cle"], "repère par rangée"), c, "repère par rangée"), "q99",
                        "repère par rangée") for c in COUCHES}
        localisation[x["cle"]] = {c: {"q99": r["ecarts_q99"][k][c],
                                      "rho": r["ecarts_q99"][k][c] / rr[c] if rr[c] > 0 else float("nan"),
                                      "contexte_max": r["profils"][k][c]["contexte"].get("max"),
                                      "generee_max": r["profils"][k][c]["generee"].get("max")}
                                  for c in COUCHES}
    neg = controle_negatif_kn(rapports, RANGEES_MIN_DEMI)
    sortie = {"g_max": g_max, "repere_q99": R, "rho": rho, "controle_negatif": neg,
              "sondes_justes": _sondes_justes(rapports), "trop_beau": zone_generee_toute_nulle(rapports),
              "localisation": localisation, "domaine": domaine(rapports),
              "rapportes": _rapportes(demi, ("rangees",)), "motifs": []}
    if not sortie["sondes_justes"]:
        sortie["motifs"].append("sonde d'audit fausse")
    if neg["lecture"] != "conforme":
        sortie["motifs"].append(f"contrôle négatif {neg['lecture']}")
    if sortie["motifs"]:
        sortie["lecture"] = "non concluant"
    elif sortie["trop_beau"]:
        sortie["lecture"] = "trop beau"
    elif all(g_max[c] <= TOLERANCE_DEMI and rho[c] <= RAPPORT_REPERE_MAX for c in COUCHES):
        sortie["lecture"] = "conforme"
    elif all(g_max[c] <= TOLERANCE_DEMI for c in COUCHES):
        sortie["lecture"] = "réserve (ρ)"
    else:
        sortie["lecture"] = "réserve (au-dessus du seuil)"
        sortie["au_dessus"] = {c: ("R(ℓ) > 0,1 : le seuil n'a pas sa marge sur ce run" if R[c] > REPERE_MARGE
                                   else "défaut du chemin en demi-précision possible")
                               for c in COUCHES if not g_max[c] <= TOLERANCE_DEMI}
    return sortie


def classer_depassement(g: float, max_contexte: float | None, max_generee: float | None, r_s: float) -> str:
    """Classe d'un dépassement (G_S(r, ℓ) > 3e-3), dans l'ordre du « Seuil » ; une grandeur illisible (NaN) n'est
    jamais sous un seuil. Une zone sans position n'a pas de maximum : l'écart est tout entier dans l'autre zone."""
    if not g <= BORNE_DIFFUSE:
        return "trop grand" if r_s <= ANCRAGE_MAX_BORNE else "sans marge"
    if not r_s <= ANCRAGE_MAX:
        return "sans marge"
    if max_generee is not None and (max_contexte is None or max_generee > RAPPORT_LOCALISATION * max_contexte):
        return "décodage"
    if max_contexte is not None and (max_generee is None or max_contexte > RAPPORT_LOCALISATION * max_generee):
        return "contexte"
    return "diffus"


def bilan_chemin(simple: dict | None, juge: str, cles_demi: list[str] | None) -> dict:
    """Palier du chemin (simple précision), table C, lu dans l'ordre ; la première ligne qui s'applique donne la
    lecture. Contrôle négatif au maximum (`bilan_controle_negatif`), D1 (`bilan_controle_positif`), dépassements
    classés couche par couche avec l'ancrage R_S(ℓ), couverture en jetons générés par la rangée."""
    if simple is None:
        return {"lecture": "non concluant (contrôles)", "motifs": ["fichier absent"]}
    quoi = f"rejeu du {juge}, palier du chemin"
    quoi_d1 = f"rejeu du {juge}, contrôle positif D1"
    rangees = _rangees(_champ(simple, "chemin", quoi), "rangees", RANGEES_REJEU, quoi)
    d1 = _rangees(_champ(simple, "d1", quoi_d1), "rangees", RANGEES_D1, quoi_d1)
    if cles_demi is not None and sorted(x["cle"] for x in rangees) != sorted(cles_demi):
        raise GardeArret(f"{quoi} : rangées ≠ celles du palier de production (L1 et L2)")
    if {x["cle"] for x in d1} & {x["cle"] for x in rangees}:
        raise GardeArret(f"rejeu du {juge} : L3 (D1) non distinct de L1 et L2")
    rapports = _rapports_des_rangees(rangees, quoi)
    cles = [_comparaison(r, TOLERANCE_SIMPLE, "max", quoi) for r in rapports]
    rapports_d1 = _rapports_des_rangees(d1, quoi_d1)
    for r in rapports_d1:
        _comparaison(r, TOLERANCE_SIMPLE, "max", quoi_d1)
    reglages = _champ(simple, "reglages_relus", quoi)
    non_conformes = {k: reglages.get(k, "absent") for k, v in REGLAGES_CONFORMES.items()
                     if k not in reglages or reglages[k] != v}
    ancrage = _champ(_champ(simple, "ancrage", quoi), "par_couche", "ancrage")
    r_s = {c: float(_champ(ancrage, c, "ancrage")) for c in COUCHES}
    for x, r, k in zip(rangees, rapports, cles):
        zone = r["positions_capturees"][k] - r["longueurs_contexte"][k]
        n = _champ(x, "jetons_generes", quoi)
        if zone not in (n, n - 1):
            raise GardeArret(f"{quoi}, {x['cle']} : {zone} positions générées comparées pour {n} jetons générés "
                             f"(n ou n − 1 attendues)")
    neg = bilan_controle_negatif(rapports, positions_min=POSITIONS_MIN)
    neg["lecture"] = ("non concluant" if neg["comparables"] < RANGEES_MIN_SIMPLE
                      else "conforme" if neg["fraction"] >= FRACTION_MIN else "contraire")
    pos = bilan_controle_positif([(SimpleNamespace(identifiant=x["cle"]), None, r) for x, r in zip(d1, rapports_d1)],
                                 {"tolerance": TOLERANCE_SIMPLE}, {"positions_min": POSITIONS_MIN})
    pos["lecture"] = ("non concluant" if pos["comparables"] < RANGEES_MIN_D1
                      else "vu" if pos["fraction"] >= FRACTION_MIN else "non vu")
    depassements = []
    for x, r, k in zip(rangees, rapports, cles):
        for c in COUCHES:
            g = r["ecarts"][k][c]
            if g <= TOLERANCE_SIMPLE:
                continue
            p = r["profils"][k][c]
            depassements.append({"rangee": x["cle"], "couche": c, "g_s": g, "r_s": r_s[c],
                                 "max_contexte": p["contexte"].get("max"), "max_generee": p["generee"].get("max"),
                                 "classe": classer_depassement(g, p["contexte"].get("max"), p["generee"].get("max"),
                                                               r_s[c])})
    plus_longue = max(zip(rangees, rapports, cles), key=lambda t: t[0]["jetons_generes"])
    x, r, k = plus_longue
    couverture = {"seuil": SEUILS_COUVERTURE[juge], "jetons_generes": x["jetons_generes"], "rangee": x["cle"],
                  "positions_comparees": r["positions_capturees"][k], "contexte": r["longueurs_contexte"][k],
                  "zone_generee": r["positions_capturees"][k] - r["longueurs_contexte"][k],
                  "atteinte": x["jetons_generes"] >= SEUILS_COUVERTURE[juge]}
    sortie = {"g_s_max": {c: _maximum(r["ecarts"][k][c] for r, k in zip(rapports, cles)) for c in COUCHES},
              "ancrage": r_s, "reglages_effectifs": reglages, "reglages_non_conformes": non_conformes,
              "sondes_justes": _sondes_justes(rapports),
              "controle_negatif": neg, "controle_positif_d1": pos, "depassements": depassements,
              "trop_beau": zone_generee_toute_nulle(rapports), "couverture": couverture, "domaine": domaine(rapports),
              "rapportes": _rapportes(simple, ("chemin", "d1", "repere", "ancrage", "reglages_relus")),
              "motifs": [], "reserves": []}
    m = sortie["motifs"]
    if non_conformes:
        m.append("réglages effectifs non conformes")
    if not sortie["sondes_justes"]:
        m.append("sonde d'audit fausse")
    if neg["lecture"] != "conforme":
        m.append(f"contrôle négatif {neg['lecture']}")
    if pos["lecture"] != "vu":
        m.append(f"D1 {pos['lecture']}")
    classes = {d["classe"] for d in depassements}
    if m:
        lecture = "non concluant (contrôles)"
    elif not pos["max_contexte"] <= TOLERANCE_SIMPLE:
        lecture = "non concluant (D1 non probant)"
    elif "trop grand" in classes:
        lecture = "défaut (écart trop grand)"
    elif "décodage" in classes:
        lecture = "défaut (décodage)"
    elif "sans marge" in classes:
        lecture = "non concluant (seuil sans marge)"
    elif "contexte" in classes:
        lecture = "non concluant (contexte)"
    elif "diffus" in classes:
        lecture = "non concluant, précision probable"
    elif sortie["trop_beau"]:
        lecture = "trop beau"
    elif not couverture["atteinte"]:
        lecture = "non concluant (couverture)"
    else:
        lecture = "fidèle"
        hautes = [c for c in COUCHES if not r_s[c] <= ANCRAGE_MAX]
        if hautes:
            sortie["reserves"].append(f"ancrage au-dessus de 1e-3 aux couches {hautes} : réserve écrite, sans effet "
                                      "sur la lecture")
    sortie["lecture"] = lecture
    return sortie


def bilan_reproduction(demi: dict | None, notations_h4: list[dict], juge: str) -> dict:
    """Reproduction (descriptive) : chaque rangée rejouée en demi-précision égale à la notation H.4 scellée de même clé
    (empreinte du texte décodé, jetons générés, drapeau « tronquée »), recalculée ici ; elle doit égaler celle que le
    lanceur a consignée (`reproduction.identique`), sinon arrêt."""
    if demi is None:
        return {"rangees": 0, "identiques": 0, "differentes": [], "lecture": "non rapportée (fichier absent)"}
    quoi = f"rejeu du {juge}, reproduction"
    scellees = {n["cle"]: n for n in notations_h4}
    differentes = []
    rangees = _rangees(demi, "rangees", RANGEES_REJEU, quoi)
    for x in rangees:
        n = scellees.get(x["cle"])
        if n is None:
            raise GardeArret(f"{quoi} : rangée {x['cle']} absente des notations H.4 scellées du {juge}")
        egal = (_champ(x, "reponse_sha256", quoi) == hashlib.sha256(n["reponse"].encode("utf-8")).hexdigest()
                and _champ(x, "jetons_generes", quoi) == n["jetons_reponse"]
                and _champ(x, "tronquee", quoi) == n["tronquee"])
        consignee = _champ(_champ(x, "reproduction", quoi), "identique", quoi)
        if consignee is not egal:
            raise GardeArret(f"{quoi}, {x['cle']} : reproduction consignée ({consignee!r}) ≠ reproduction recalculée "
                             f"({egal})")
        if not egal:
            differentes.append(x["cle"])
    identiques = len(rangees) - len(differentes)
    return {"rangees": len(rangees), "identiques": identiques, "differentes": differentes,
            "lecture": ("16 sur 16 identiques : les mesures du rejeu portent sur les réponses mêmes du plan B"
                        if identiques == RANGEES_REJEU else "réserve : la lecture vaut pour le chemin, non pour ces "
                                                            "réponses précises")}


def lecture_combinee(rejeu: dict) -> dict:
    """Lecture combinée, pour l'étape (table C)."""
    ch = {j: rejeu[j]["chemin"]["lecture"] for j in JUGES}
    pr = {j: rejeu[j]["production"]["lecture"] for j in JUGES}
    reserves = ("réserve (ρ)", "réserve (au-dessus du seuil)")
    if any(ch[j].startswith("défaut") for j in JUGES):
        lecture = "défaut du chemin"
    elif all(ch[j] == "fidèle" for j in JUGES) and all(pr[j] == "conforme" for j in JUGES):
        lecture = "propriété du modèle"
    elif all(ch[j] == "fidèle" for j in JUGES) and all(pr[j] in ("conforme",) + reserves for j in JUGES):
        lecture = "propriété du modèle, sous réserve de demi-précision"
    else:
        lecture = "non concluant"
    consequence = {
        "propriété du modèle": "réserve 1 du verdict complémentaire levée dans le domaine couvert ; requalification "
                               "selon A ; tout changement de réglage reste un nœud (Q4)",
        "propriété du modèle, sous réserve de demi-précision": "même conséquence, avec la réserve ; nœud : Lazar "
                                                               "décide si elle retient la lecture",
        "défaut du chemin": "requalification suspendue : nœud pour les deux juges ; diagnostic par localisation ; "
                            "notations H.4 et RS1 et générations longues de l'agent sous réserve ; proposition à "
                            "Lazar (Q6)",
        "non concluant": "réserve 1 maintenue ; requalification selon A, avec cette réserve"}[lecture]
    return {"lecture": lecture, "chemin": ch, "production": pr, "consequence": consequence}


def bilan_temoin(temoins: dict | None, juge: str, taux_h4: float) -> dict:
    """Témoin de la bibliothèque (descriptif) : T_w, tronquées sur 16 ; queues binomiales recalculées sur le taux de
    troncature H.4 scellé du juge ; « témoin impossible » consigné sans effet."""
    queues = queues_binomiales(taux_h4)
    if temoins is None:
        return {"lecture": "non rapporté", "queues": queues, "taux_h4": taux_h4, "hors_queue": None}
    quoi = f"témoin du {juge}"
    t = _champ(_champ(temoins, "juges", "témoin"), juge, "témoin")
    taux = _champ(t, "taux_h4", quoi)
    if _champ(taux, "tronquees", quoi) / _champ(taux, "notations", quoi) != taux_h4:
        raise GardeArret(f"{quoi} : taux H.4 consigné {taux} ≠ taux recalculé sur les notations scellées {taux_h4}")
    rangees, impossibles = [], []
    for a in _champ(t, "appels", quoi):
        s = _champ(a, "statut", quoi)
        if s == "fait":
            rangees += _champ(a, "rangees", quoi)
        elif s == "témoin impossible":
            impossibles.append({"appel": a.get("lot"), "motif": _champ(a, "motif", quoi)})
        else:
            raise GardeArret(f"{quoi} : statut d'appel {s!r} inconnu (« fait » ou « témoin impossible »)")
    tw = sum(bool(_champ(x, "tronquee", "témoin")) for x in rangees)
    complet = len(rangees) == TEMOIN_TIRAGES
    return {"lecture": "rapporté" if complet else "incomplet (témoin impossible pour un appel) : comptes rapportés, "
                                                  "sans déclencheur",
            "rangees": len(rangees), "t_w": tw, "completes": sum(bool(x.get("complete")) for x in rangees),
            "impossible": impossibles, "queues": queues, "taux_h4": taux_h4,
            "hors_queue": (tw in queues) if complet else None}


def _illisibles(x) -> int:
    """Grandeurs illisibles (NaN) d'une structure lue."""
    if isinstance(x, dict):
        return sum(_illisibles(v) for v in x.values())
    if isinstance(x, list):
        return sum(_illisibles(v) for v in x)
    return int(isinstance(x, float) and x != x)


# --- Audit et prédictions ----------------------------------------------------------------------------------------

def audit_r4(fmt: dict, juges_lus: dict, requalif: dict, rejeu: dict, temoin: dict, fichiers: dict) -> dict:
    """Table D : déclencheurs propres aux juges de `declencheurs_audit` (sur les seules notations RS1), déclencheur neuf
    de la somme la plus fréquente, déclencheurs du rejeu et du témoin, lignes « trop beau » des tables A et C."""
    gele = declencheurs_audit(fmt, juges_lus, {}, None, [])
    noms = list(juges_lus)
    propre = [x for x in gele["trop_propre"] if any(n in x for n in noms)]
    sale = [x for x in gele["trop_sale"] if any(n in x for n in noms)]
    en_cause: dict[str, list] = {}
    for j in JUGES:
        q = requalif[j]
        if q is None:
            continue
        part = q["descriptifs"]["part_somme_la_plus_frequente"]
        if part is not None and part > SOMME_FREQUENTE_MAX:
            propre.append(f"juge RS1-{j} : somme la plus fréquente sur plus de 50 % des réponses complètes")
        if q["garde_en_ligne"]["trop_beau"]:
            propre.append(f"garde en ligne de RS1-{j} : trop beau")
    for j in JUGES:
        pr, ch = rejeu[j]["production"], rejeu[j]["chemin"]
        rangees = set()
        nan = sum(_illisibles(fichiers[f"rejeu-{j}-{p}"]) for p in ("demi", "simple")) + _illisibles(pr.get("rho"))
        if nan:
            sale.append(f"rejeu du {j} : {nan} grandeur(s) illisible(s) (NaN)")
        hauts = [c for c, v in (pr.get("repere_q99") or {}).items() if not v <= REPERE_AUDIT]
        if hauts:
            sale.append(f"rejeu du {j} : repère R(ℓ) > 0,2 aux couches {hauts}")
        if ch["lecture"].startswith("défaut") or ch["lecture"] in (
                "non concluant (seuil sans marge)", "non concluant (contexte)", "non concluant, précision probable"):
            sale.append(f"rejeu du {j} : palier du chemin « {ch['lecture']} »")
            rangees |= {d["rangee"] for d in ch["depassements"]}
        if ch["lecture"] == "non concluant (D1 non probant)":
            sale.append(f"rejeu du {j} : contrôle positif D1 non probant")
        if pr["lecture"] == "réserve (ρ)":
            sale.append(f"rejeu du {j} : palier de production en « réserve (ρ) »")
            rangees |= {k for k, v in pr["localisation"].items() if any(not z["rho"] <= RAPPORT_REPERE_MAX
                                                                        for z in v.values())}
        for nom, palier in (("chemin", ch), ("production", pr)):
            if palier["lecture"] == "trop beau":
                propre.append(f"rejeu du {j} : palier {'du chemin' if nom == 'chemin' else 'de production'} trop "
                              "beau")
        if temoin[j]["hors_queue"]:
            sale.append(f"témoin du {j} : T_w = {temoin[j]['t_w']} dans une queue binomiale de moins de 0,5 %")
        if rangees:
            en_cause[j] = sorted(rangees)
    return {"trop_propre": propre, "trop_sale": sale, "declenche": bool(propre or sale),
            "rangees_en_cause": en_cause}


def predictions_pb(requalif: dict, juges_lus: dict, diff: dict | None, combinee: str, rejeu: dict) -> dict:
    """Statut de PB1 à PB10 (« Prédiction ») : réfutée si une clause de réfutation est vraie, sur des grandeurs
    définies ; confirmée si toutes les clauses de confirmation sont définies et vraies ; non concluant sinon."""
    S = PREDICTIONS_PB
    lj = {j: juges_lus.get(f"RS1-{j}") for j in JUGES}
    inc = {j: (lj[j]["part_incompletes"] if lj[j] else None) for j in JUGES}
    tc = {j: (lj[j]["taches_completes"] if lj[j] else None) for j in JUGES}
    part = {j: (lj[j]["decomposition"]["parts_tronquees"]["juge"] if lj[j] and lj[j]["decomposition_concluante"]
                else None) for j in JUGES}
    b = diff["borne"] if diff and diff.get("borne") and diff.get("taches", 0) >= TACHES_COMPLETES_MIN else None
    garde = {j: (requalif[j]["garde_en_ligne"] if requalif[j] else None) for j in JUGES}
    med = {j: (requalif[j]["descriptifs"]["longueur_mediane"] if requalif[j] else None) for j in JUGES}
    repro = [rejeu[j]["reproduction"] for j in JUGES]
    identiques = sum(r["identiques"] for r in repro)
    differentes = sum(len(r["differentes"]) for r in repro)
    pb4 = lambda v: (_si(lambda x: S["PB4"]["confirmee"][0] <= x <= S["PB4"]["confirmee"][1], v),  # noqa: E731
                     _si(lambda x: not S["PB4"]["permise"][0] <= x <= S["PB4"]["permise"][1], v))
    return {
        **{k: statut([_si(lambda v: v <= S["PB1"]["confirmee_max"], inc[j])],
                     [_si(lambda v: v > S["PB1"]["refutee_au_dela"], inc[j])]) for k, j in (("PB1", "8B"),
                                                                                          ("PB2", "3B"))},
        "PB3": statut([_si(lambda v: v >= S["PB3"]["taches_min"], tc[j]) for j in JUGES],
                      [_si(lambda v: v < S["PB3"]["taches_min"], tc[j]) for j in JUGES]),
        **{k: statut([pb4(part[j])[0]], [pb4(part[j])[1]]) for k, j in (("PB4", "8B"), ("PB5", "3B"))},
        "PB6": statut([_si(lambda x: x[0] > 0, b)], [_si(lambda x: x[1] < 0, b)]),
        "PB7": statut([(g["equivalence"] == "conforme") if g else None for g in garde.values()],
                      [(g["equivalence"] == "contraire" and g["controle_negatif"]["lecture"] == "conforme")
                       if g else None for g in garde.values()]),
        "PB8": statut([combinee == "propriété du modèle"], [combinee == "défaut du chemin"]),
        "PB9": statut([identiques == S["PB9"]["rangees"]], [differentes > 0]),
        "PB10": statut([_si(lambda v: v <= S["PB10"]["confirmee_max"], med[j]) for j in JUGES],
                       [_si(lambda v: v > S["PB10"]["refutee_au_dela"], med[j]) for j in JUGES]),
    }


def table_e(issue: dict, fichiers: dict) -> dict:
    """Table E : issue du run, fichiers absents et leur conséquence, éléments du relancement établis sur les pièces."""
    ecrits = [f for f in FICHIERS if fichiers[f] is not None]
    sortie = {"issue": issue["fichier"], "statuts": issue["statuts"], "ecrits": ecrits,
              "absents": {f: CONSEQUENCES_ABSENT[f] for f in FICHIERS if fichiers[f] is None},
              "aucun_fichier_de_phase_ecrit": not ecrits}
    if issue["fichier"] == "resume":
        sortie["relancement"] = "sans objet (run terminé, résumé consigné)"
    elif ecrits:
        sortie["relancement"] = "aucun relancement : un fichier de phase est écrit (condition (ii) ; préséance)"
    else:
        sortie["relancement"] = ("condition (ii) tenue (aucun fichier de phase écrit) ; les conditions (i), (iii), "
                                 "(iv) et (v) s'établissent sur les pièces (cause, dépense, alerte, crédit), non ici ; "
                                 "sinon nœud")
        sortie["arret"] = issue.get("arret")
    return sortie


# --- Lecture -----------------------------------------------------------------------------------------------------

def lire_requalification(racine: Path, run_pilote: str, run_notations: str, run_planb: str, run_analyse: str,
                         chemin_taches: str | Path, run_lecture: str, prereg: str | Path,
                         autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    # gardes gelées de la première lecture (préenregistrement du pilote, modules de lecture, constantes, numpy, arbre)
    chemin_a, m_a, etat = _ouvrir_analyse(racine, run_analyse)
    if m_a["config"]["run_pilote"] != run_pilote:
        raise GardeArret(f"run du pilote {run_pilote} ≠ run du manifeste d'analyse {m_a['config']['run_pilote']}")
    p = charger_pilote(racine, run_pilote, chemin_taches)
    if p["manifeste_sha256"] != m_a["config"]["manifeste_pilote_sha256"]:
        raise GardeArret("manifeste du pilote différent de celui de l'analyse")
    if tuple(p["juges"]) != JUGES:
        raise GardeArret(f"juges du pilote {p['juges']} ≠ {list(JUGES)}")
    # notations H.4 scellées : seuils de couverture, reproduction, taux de troncature du témoin
    m_n, sha_n, h4, _ = charger_notations(racine, run_notations, run_pilote, p["juges"])
    absentes = [j for j in JUGES if h4[j] is None]
    if absentes:
        raise GardeArret(f"notations H.4 scellées absentes pour {absentes}")
    couverture = seuils_couverture(h4)
    # run de l'étape : sous ce préenregistrement, rattaché, configuration aux seuils gelés, modules, issue, fichiers
    chemin_b = racine / "runs" / run_planb / "manifeste.json"
    if not chemin_b.exists():
        raise GardeArret(f"manifeste du run de l'étape absent : {chemin_b}")
    m_b, sha_b = lire_manifeste(chemin_b)
    exiger_run_sous_prereg(racine, m_b, prereg)
    exiger_config_de_l_etape(m_b, run_pilote, p["manifeste_sha256"], run_notations)
    exiger_modules_planb(racine, m_b["commit"])
    exiger_modules_geles(racine)
    issue = issue_du_run(racine, run_planb)
    fichiers = charger_fichiers(racine, run_planb, issue)
    entropies = {g["entropie"] for g in m_b["graines"].values()}
    if len(entropies) != 1:
        raise GardeArret(f"graines du run de l'étape d'entropies différentes : {sorted(entropies)}")
    entropie = int(entropies.pop())
    g = graines(cles_lecture(), entropie)
    # requalification : mêmes fonctions gelées que le pilote, juges « RS1-8B » et « RS1-3B »
    fiches, taches_ids = p["episodes"]["fiches"], sorted(p["taches"])
    ensembles = empreintes_des_ensembles(fiches)
    plafond = m_b["config"]["max_nouveaux_juge"]
    requalif, juges_lus, alignes = {}, {}, {}
    for j in JUGES:
        f = fichiers[f"notations-RS1-{j}-decisives"]
        if f is None:
            requalif[j] = None
            continue
        notations = _champ(f, "notations", f"notations RS1 du {j}")
        descriptifs = relire_notations_rs1(notations, j, plafond)
        alignes[j] = notes_alignees(notations, f"RS1-{j}", taches_ids, ensembles)
        juges_lus[f"RS1-{j}"] = lecture_juge(alignes[j], generateur(g[f"analyse/bootstrap-parts-RS1-{j}"]))
        requalif[j] = {"lecture": juges_lus[f"RS1-{j}"], "descriptifs": descriptifs,
                       "garde_en_ligne": bilan_garde(f, j),
                       # descriptifs du lanceur (durée, pic de mémoire) et noyaux permis : rapportés tels quels
                       "descriptifs_du_run": f.get("descriptifs"), "noyaux_permis": f.get("noyaux_permis")}
    diff = None
    if len(alignes) == 2:
        a8, a3 = (alignes[j] for j in JUGES)
        try:
            diff = difference_appariee((a8["sA"], a8["sB"], a8["sC"]), (a3["sA"], a3["sB"], a3["sC"]), TIRAGES,
                                       generateur(g["analyse/bootstrap-difference-RS1"]), NIVEAU)
        except GardeArret as e:
            diff = {"impossible": str(e), "borne": None}
    # rejeu
    rejeu = {}
    for j in JUGES:
        demi, simple = fichiers[f"rejeu-{j}-demi"], fichiers[f"rejeu-{j}-simple"]
        cles_demi = [x["cle"] for x in demi["rangees"]] if demi is not None and "rangees" in demi else None
        rejeu[j] = {"production": bilan_production(demi, simple, j), "chemin": bilan_chemin(simple, j, cles_demi),
                    "reproduction": bilan_reproduction(demi, h4[j], j)}
    combinee = lecture_combinee(rejeu)
    taux = {j: sum(bool(n["tronquee"]) for n in h4[j]) / len(h4[j]) for j in JUGES}
    temoin = {j: bilan_temoin(fichiers["temoins"], j, taux[j]) for j in JUGES}
    # tables A et B
    issues = {j: table_a(j, requalif[j]["lecture"] if requalif[j] else None,
                         requalif[j]["garde_en_ligne"] if requalif[j] else None, combinee["lecture"]) for j in JUGES}
    fmt = mesures_format(fiches, p["config"]["max_nouveaux"])
    audit = audit_r4(fmt, juges_lus, requalif, rejeu, temoin, fichiers)
    p_notes = {**p, "notations": {(f"RS1-{j}", "decisives"): (fichiers[f"notations-RS1-{j}-decisives"] or {}).get(
        "notations") for j in JUGES}}
    lecture = {"run_pilote": run_pilote, "run_notations": run_notations, "run_planb": run_planb,
               "run_analyse": run_analyse, "commit_planb": m_b["commit"], "commit_geles": COMMIT_GELES, **etat,
               "seuils_couverture": couverture, "taux_troncature_h4": taux,
               "requalification": requalif, "table_a": issues,
               "usagers": table_b({j: issues[j]["issue"] for j in JUGES}),
               "difference_appariee": diff, "rejeu": rejeu, "lecture_combinee": combinee, "temoin": temoin,
               "audit_r4": audit, "lecture_suspendue": audit["declenche"],
               "relectures_audit": tirer_relectures(p_notes, generateur(g["analyse/audit-RS1"])),
               "predictions": predictions_pb(requalif, juges_lus, diff, combinee["lecture"], rejeu),
               "runs_partiels": table_e(issue, fichiers)}
    config = {"run_pilote": run_pilote, "run_notations": run_notations, "manifeste_notations_sha256": sha_n,
              "run_planb": run_planb, "manifeste_planb_sha256": sha_b, "run_analyse": run_analyse,
              "manifeste_analyse_sha256": empreinte(chemin_a),
              "commit_lecture_cite": m_a["config"]["commit_lecture_cite"],
              "constantes": constantes()}
    chemin_p = Path(prereg) if Path(prereg).is_absolute() else racine / prereg
    # graines de la lecture : même entropie que l'étape, mêmes clés que celles employées ci-dessus (R9)
    chemin_m, _ = creer_manifeste(racine, run_lecture, config, cles_lecture(), entropie=entropie, decisif=True,
                                  prereg=str(chemin_p), autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    ecrire_resultat(racine, chemin_m, "lecture-planb", _serialisable(lecture))
    return lecture


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    for k in ("--run-pilote", "--run-notations", "--run-planb", "--run-analyse", "--taches", "--run-lecture",
              "--prereg"):
        ap.add_argument(k, required=True)
    x = ap.parse_args(argv)
    lecture = lire_requalification(Path("."), x.run_pilote, x.run_notations, x.run_planb, x.run_analyse, x.taches,
                                   x.run_lecture, x.prereg)
    print(json.dumps(_serialisable({"table_a": {j: v["issue"] for j, v in lecture["table_a"].items()},
                                    "lecture_combinee": lecture["lecture_combinee"]["lecture"],
                                    "predictions": lecture["predictions"],
                                    "lecture_suspendue": lecture["lecture_suspendue"]}), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
