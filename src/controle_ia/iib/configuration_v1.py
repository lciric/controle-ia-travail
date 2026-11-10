"""Configuration de la course (ii-b) (conception 2 à 6 ; ordre § 2) : clés exigées, constantes égales à la conception,
garde « aucune sonde », cohérence du mode.

- Constantes : `oracle`, `regle`, `epreuves`, `tours` doivent porter exactement les valeurs de `constantes_v1` (recopiées
  de la conception) ; en mode jouet seulement, les effectifs (`tours.episodes_par_tour`, `tours.N_cible`, `tours.N_min`)
  peuvent être réduits, jamais b, F, K, K_MIN, N_B_MIN, ni les seuils des épreuves (qui se réduisent avec les effectifs
  dans `tours_v1.seuil_compte`).
- « Aucune sonde » : toute clé, à toute profondeur, qui nomme une sonde (« sond », « probe »), ou, hors du seul bloc
  `activites`, une couche ou des activations (« couche », « layer », « activation », « capture »), arrête le run.
- `activites` (ajout sur GO-2026-11-10-08, R-2175 : activité interne enregistrée, jamais lue par ce code) : schéma exact
  {"enregistrer": bool, "couches": [...], "format": "float16"} ; en mode réel, couches 7, 15 et 23 (choix déclaré :
  celles de T0.6, l'extracteur de T0.7 n'ayant pas été lu).
- Juge de T0.8 : `juge_t08.joue` doit être faux dans cette version (forme de T0.8 non scellée ; une version neuve du code
  l'ajoutera si la mère remplit `<<FORME_JUGE_T08_SCELLEE>>` par « oui »).
- Mode réel : agent à la révision de P3 et de T0.6, chemins et empreintes des tâches, des consignes et de l'entropie
  présents ; mode jouet : tâches synthétiques et consigne jouet, aucun modèle réel.
"""
from __future__ import annotations

import re

from ..gardes import GardeArret
from . import constantes_v1 as C

REVISION_AGENT = "0e9e39f249a16976918f6564b8830bc894c89659"
MODELE_AGENT = "meta-llama/Llama-3.1-8B-Instruct"
CLES = ("activites", "nom", "mode", "T", "lot", "max_nouveaux", "temperature", "noyau_attention", "agent", "taches_reserve",
        "taches_evaluation", "consigne_iib", "consignes_p3", "entropie", "oracle", "regle", "epreuves", "etalonnage",
        "tours", "adaptateur", "distillation", "evaluation", "juge_t08", "ancrage_premier_tour")
CONDITIONS_EVALUATION = ("H", "B50", "B100", "TJ100")
ETATS_EVALUATION = {"H": ("eleve", 0.0), "B50": ("eleve", 0.5), "B100": ("eleve", 1.0), "TJ100": ("temoin-jumeau", 1.0)}
_INTERDIT = re.compile(r"sond|probe|couche|layer|activation|capture", re.I)
_SONDE = re.compile(r"sond|probe", re.I)


def cles_interdites(config, chemin: str = "") -> list[str]:
    trouvees = []
    if isinstance(config, dict):
        for k, v in config.items():
            ici = f"{chemin}.{k}" if chemin else str(k)
            if ici == "activites":
                trouvees += [f"activites.{x}" for x in (v if isinstance(v, dict) else {}) if _SONDE.search(str(x))]
                continue
            if _INTERDIT.search(str(k)):
                trouvees.append(ici)
            trouvees += cles_interdites(v, ici)
    elif isinstance(config, list):
        for k, v in enumerate(config):
            trouvees += cles_interdites(v, f"{chemin}[{k}]")
    return trouvees


def _egal(quoi: str, lu, attendu) -> None:
    if type(lu) is bool or lu != attendu or (isinstance(attendu, float) and not isinstance(lu, float)):
        raise GardeArret(f"configuration de (ii-b) : {quoi} = {lu!r}, la conception fixe {attendu!r}")


def exiger_constantes(config: dict) -> None:
    o, r, e, t = config["oracle"], config["regle"], config["epreuves"], config["tours"]
    _egal("oracle.K", o["K"], C.K)
    _egal("oracle.K_MIN", o["K_MIN"], C.K_MIN)
    _egal("oracle.max_jetons_suite", o["max_jetons_suite"], C.MAX_JETONS_SUITE)
    _egal("oracle.temperature", o["temperature"], C.TEMPERATURE_JUMEAU)
    if o["mediane"] != "basse" or o["reecriture"] != "valeur_entiere":
        raise GardeArret("configuration de (ii-b) : médiane basse et réécriture de la valeur entière exigées")
    if o["forme_lot"] not in ("cache_duplique", "prerempli_par_suite", "epreuve"):
        raise GardeArret(f"configuration de (ii-b) : oracle.forme_lot {o['forme_lot']!r} inconnue")
    _egal("regle.N_B_MIN", r["N_B_MIN"], C.N_B_MIN)
    _egal("regle.b", r["b"], C.B)
    _egal("regle.F", r["F"], C.F)
    _egal("T", config["T"], C.T)
    for k, v in (("E_O1_demi_largeur", C.E_O1_DEMI_LARGEUR), ("E_O2_tirages", C.E_O2_TIRAGES),
                 ("E_O3_max_acceptes", C.E_O3_MAX_ACCEPTES), ("E_O3_sur", C.E_O3_SUR), ("E_O4_max_acceptes", C.E_O4_MAX_ACCEPTES),
                 ("E_O4_sur", C.E_O4_SUR), ("E_O5_min_coupes", C.E_O5_MIN_COUPES), ("E_O6_min_lisibles", C.E_O6_MIN_LISIBLES),
                 ("M2_tirages", C.M2_TIRAGES)):
        _egal(f"epreuves.{k}", e[k], v)
    _egal("tours.R_max", t["R_max"], C.R_MAX)
    _egal("tours.tour_controle", t["tour_controle"], C.TOUR_CONTROLE)
    _egal("tours.M1_max_acceptes", t["M1_max_acceptes"], C.M1_MAX_ACCEPTES)
    if config["mode"] == "reel":
        _egal("tours.episodes_par_tour", t["episodes_par_tour"], C.EPISODES_PAR_TOUR)
        _egal("tours.N_cible", t["N_cible"], C.N_CIBLE)
        _egal("tours.N_min", t["N_min"], C.N_MIN)
        _egal("etalonnage.honnetes_par_tache", config["etalonnage"]["honnetes_par_tache"], 2)
        _egal("etalonnage.flagrants_par_tache", config["etalonnage"]["flagrants_par_tache"], 1)


def exiger_config_iib(config: dict) -> None:
    manquantes = [k for k in CLES if k not in config]
    if manquantes:
        raise GardeArret(f"configuration de (ii-b) incomplète : {manquantes}")
    interdites = cles_interdites(config)
    if interdites:
        raise GardeArret(f"configuration de (ii-b) : clé de sonde, de couche ou d'activations {interdites} : aucune sonde")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} : « reel » ou « jouet »")
    if tuple(config["evaluation"]["conditions"]) != CONDITIONS_EVALUATION:
        raise GardeArret(f"évaluation : conditions {CONDITIONS_EVALUATION} exigées, dans cet ordre")
    if config["juge_t08"].get("joue"):
        raise GardeArret("juge de T0.8 : non joué par cette version du code (forme non scellée) ; version neuve exigée")
    a, d = config["adaptateur"], config["distillation"]
    if (a["rang"], a["alpha"], tuple(a["cibles"]), a["precision"], a["sauvegarde"]) != (
            16, 32, ("q_proj", "k_proj", "v_proj", "o_proj"), "float32", "float16"):
        raise GardeArret("adaptateur : rang 16, alpha 32, q/k/v/o, float32, sauvegarde float16 (configuration du candidat 12)")
    if (d["mode"], d["epoques"], d["lot"], d["pas"], d["norme_max"]) != ("transcription", 3, 1, 1e-4, 1.0):
        raise GardeArret("distillation : transcription, 3 époques, lot 1, pas 1e-4, norme 1 (configuration du candidat 12)")
    exiger_constantes(config)
    act = config["activites"]
    if not isinstance(act, dict) or set(act) != {"enregistrer", "couches", "format"} or not isinstance(act["enregistrer"], bool) \
            or act["format"] != "float16" or not act["couches"] or not all(isinstance(c, int) and c >= 0 for c in act["couches"]):
        raise GardeArret("activites : schéma {enregistrer: bool, couches: [entiers], format: float16} exigé")
    if config["mode"] == "reel":
        if act["couches"] != [7, 15, 23]:
            raise GardeArret("activites : couches 7, 15, 23 (celles de T0.6) en mode réel")
        ag = config["agent"]
        if ag.get("modele") != MODELE_AGENT or ag.get("revision") != REVISION_AGENT:
            raise GardeArret("agent : Llama-3.1-8B-Instruct à la révision de P3 et de T0.6 exigé (aucun changement de modèle)")
        for k in ("taches_reserve", "taches_evaluation", "consigne_iib", "consignes_p3"):
            if not re.fullmatch(r"[0-9a-f]{64}", str(config[k].get("sha256") or "")):
                raise GardeArret(f"{k} : empreinte sha256 exigée en mode réel")
        if not re.fullmatch(r"[0-9]{10,}", str(config["entropie"])):
            raise GardeArret("entropie : entier de SeedSequence() exigé en mode réel (tiré une fois par la mère)")
        if (config["T"], config["lot"], config["max_nouveaux"], config["temperature"], config["noyau_attention"]) != (
                10, 8, 400, 1.0, "defaut"):
            raise GardeArret("génération : T 10, lot 8, 400 jetons, température 1,0, noyau « defaut » (réglages de P3 et T0.6)")
