"""Section de configuration de la distillation et de l'évaluation de l'organisme retenu, v5 — section à part.

EXPLORATOIRE, NON OPPOSABLE (R-522). Le texte scellé de l'organisme retenu
(`brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1.md`) amende la conception d'origine
(`brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1.md`) sans la réécrire, et sa section 16 ne liste aucun écart pour
l'adaptateur, la distillation ni les doses : **les constantes de cette section sont celles de la conception d'origine**
(sections 5.1, 5.3 et 6), telles que `configuration_v1.TEXTE` les porte. Elles sont vérifiées à l'égalité ; une constante
changée est un refus.

La section vit sous **une seule clé de la configuration**, `distillation_evaluation` (`SECTION`), pour que la configuration de
l'organisme retenu (`configuration_v5`) n'ait qu'une clé à permettre. Elle porte :

- `adaptateur` : rang 16, `alpha` 32, quatre projections, simple précision à l'entraînement, sauvegarde en demi-précision ;
- `distillation` : transcription entière, trois époques, lot d'une transcription, pas 1·10⁻⁴, norme bornée à 1 ;
- `doses` : modèle de base 0 ; élève à demi-dose 0,5 ; élève 1 ; témoin-jumeau 1 ;
- `evaluation` : les quatre conditions dans leur ordre, l'adaptateur de chacune, 64 tâches d'évaluation ;
- `perte` : ce qui sort de la perte de distillation. Deux règles de la conception d'origine (mentions d'un texte privé ; actions
  non bornables à champ de coût) et **une lecture que le texte scellé ne tranche pas, `premiere_action`** : la première action
  n'est jamais comptée par la règle de l'organisme retenu (elle n'est donc jamais « bornable »), et la règle d'origine « les
  actions non bornables qui portent un champ de coût sortent de la perte » la sortirait de la perte à la lettre, alors que la
  section 6 du texte scellé écrit que l'élève apprendra le premier coût sans excès. Les deux lectures sont écrites et éprouvées :
  `gardee` (la première action reste dans la perte, sauf mention) ou `exclue` (lecture à la lettre). **Le gabarit laisse le
  champ vide : la session de reconception le remplit, comme l'entropie ; vide, tout lancement est refusé.**
- `surveillance` : réglage qu'aucun texte ne fixe (déclaré) : l'empreinte des adaptateurs est relue tous les dix appels de
  génération (un lot de dix actions), la dose à chaque appel.

Aucun texte de consigne ; ce module n'importe que les gardes.
"""
from __future__ import annotations

import copy
import math

from ..gardes import GardeArret

SECTION = "distillation_evaluation"
SCHEMA_DISTILLATION = "distillation-iib-v5"
SCHEMA_ETATS = "etats-evaluation-iib-v5"
ADAPTATEURS = ("eleve", "temoin-jumeau")
CONDITIONS = ("H", "B50", "B100", "TJ100")
LECTURES_PREMIERE_ACTION = ("gardee", "exclue")
CLE_INJECTION = "iib/injection"

TEXTE_DISTILLATION = {
    "adaptateur": {"rang": 16, "alpha": 32.0, "cibles": ["q_proj", "k_proj", "v_proj", "o_proj"], "precision": "float32",
                   "sauvegarde": "float16"},
    "distillation": {"mode": "transcription", "epoques": 3, "lot": 1, "pas": 0.0001, "norme_max": 1.0},
    "doses": {"H": 0.0, "B50": 0.5, "B100": 1.0, "TJ100": 1.0},
    "evaluation": {"conditions": list(CONDITIONS),
                   "adaptateur_de": {"H": "eleve", "B50": "eleve", "B100": "eleve", "TJ100": "temoin-jumeau"}, "taches": 64},
    "perte": {"mentions": "exclues", "non_bornables_a_cout": "exclues", "premiere_action": None},
    "surveillance": {"empreinte_tous_les_appels": 10},
}
# Réductibles en mode jouet seulement (tailles) : rang et époques de l'essai, nombre de tâches d'évaluation.
REDUCTIBLES_AU_JOUET = (("adaptateur", "rang"), ("adaptateur", "alpha"), ("distillation", "epoques"), ("evaluation", "taches"),
                        ("surveillance", "empreinte_tous_les_appels"))


def cle_de_l_adaptateur(nom: str) -> str:
    return f"iib/adaptateur/{exiger_adaptateur(nom)}"


def cle_de_la_distillation(nom: str) -> str:
    return f"iib/distillation/{exiger_adaptateur(nom)}"


def exiger_adaptateur(nom: str) -> str:
    if nom not in ADAPTATEURS:
        raise GardeArret(f"adaptateur {nom!r} : {ADAPTATEURS} (refus)")
    return nom


def gabarit_section() -> dict:
    """La section telle que le texte la fixe ; `perte.premiere_action` vide, à remplir par la session de reconception."""
    return copy.deepcopy(TEXTE_DISTILLATION)


def _egal(quoi: str, lu, attendu) -> None:
    if isinstance(attendu, dict):
        if not isinstance(lu, dict) or set(lu) != set(attendu):
            raise GardeArret(f"{quoi} : clés {sorted(lu) if isinstance(lu, dict) else lu!r} ≠ {sorted(attendu)} (refus)")
        for k in attendu:
            _egal(f"{quoi}.{k}", lu[k], attendu[k])
        return
    if isinstance(attendu, list):
        if not isinstance(lu, list) or lu != attendu:
            raise GardeArret(f"{quoi} : {lu!r} ≠ {attendu!r} (conception d'origine ; refus)")
        return
    if isinstance(attendu, bool) or isinstance(lu, bool):
        if lu is not attendu:
            raise GardeArret(f"{quoi} : {lu!r} ≠ {attendu!r} (refus)")
        return
    if isinstance(attendu, (int, float)):
        if not isinstance(lu, (int, float)) or float(lu) != float(attendu):
            raise GardeArret(f"{quoi} : {lu!r} ≠ {attendu!r} (constante de la conception d'origine changée : refus)")
        return
    if lu != attendu:
        raise GardeArret(f"{quoi} : {lu!r} ≠ {attendu!r} (refus)")


def _nombre(quoi: str, v, entier: bool = False) -> None:
    if isinstance(v, bool) or not isinstance(v, int if entier else (int, float)) or not math.isfinite(v) or v <= 0:
        raise GardeArret(f"{quoi} : {v!r} ({'entier' if entier else 'nombre'} strictement positif attendu)")


def exiger_section(section, mode: str, pour_lancer: bool = False) -> dict:
    """Valide la section ; rend la lecture retenue pour la première action. Mode réel : égalité avec la conception d'origine ;
    mode jouet : seules les tailles (`REDUCTIBLES_AU_JOUET`) peuvent différer. `pour_lancer` : la lecture de la première
    action doit être remplie."""
    if mode not in ("reel", "jouet"):
        raise GardeArret(f"mode {mode!r} : « reel » ou « jouet »")
    if not isinstance(section, dict) or set(section) != set(TEXTE_DISTILLATION):
        raise GardeArret(f"section {SECTION} : clés {sorted(section) if isinstance(section, dict) else section!r} ≠ "
                         f"{sorted(TEXTE_DISTILLATION)} (refus)")
    attendu = copy.deepcopy(TEXTE_DISTILLATION)
    lecture = section["perte"].get("premiere_action") if isinstance(section["perte"], dict) else None
    attendu["perte"]["premiere_action"] = lecture
    if mode == "jouet":
        for s, k in REDUCTIBLES_AU_JOUET:
            if not isinstance(section[s], dict) or k not in section[s]:
                raise GardeArret(f"section {SECTION}.{s}.{k} absente (refus)")
            _nombre(f"{SECTION}.{s}.{k}", section[s][k], entier=k != "alpha")
            attendu[s][k] = section[s][k]
    _egal(SECTION, section, attendu)
    if lecture is not None and lecture not in LECTURES_PREMIERE_ACTION:
        raise GardeArret(f"{SECTION}.perte.premiere_action = {lecture!r} : {LECTURES_PREMIERE_ACTION}, ou vide tant que la session "
                         "de reconception ne l'a pas remplie (refus)")
    if pour_lancer and lecture is None:
        raise GardeArret(f"{SECTION}.perte.premiere_action non remplie : la première action reste-t-elle dans la perte de "
                         "distillation ? Lecture à trancher par la session de reconception avant tout lancement (refus)")
    if set(section["doses"]) != set(CONDITIONS) or set(section["evaluation"]["adaptateur_de"]) != set(CONDITIONS):
        raise GardeArret(f"{SECTION} : doses et adaptateurs attendus pour {CONDITIONS}")
    return {"premiere_action": lecture}


def section_de(config: dict, pour_lancer: bool = False) -> dict:
    """La section de la configuration, validée ; absente : refus (la course ne distille pas sans elle)."""
    if not isinstance(config, dict) or SECTION not in config:
        raise GardeArret(f"section {SECTION} absente de la configuration : ni distillation ni évaluation sans elle (refus)")
    exiger_section(config[SECTION], config.get("mode"), pour_lancer)
    return config[SECTION]


def plan_d_evaluation(section: dict) -> list[dict]:
    """Conditions d'évaluation dans leur ordre : [{"condition", "adaptateur", "dose"}] ; le modèle de base est l'élève à dose 0."""
    plan = []
    for c in section["evaluation"]["conditions"]:
        dose = float(section["doses"][c])
        if not 0.0 <= dose <= 1.0:
            raise GardeArret(f"dose {dose} de la condition {c} hors de [0, 1]")
        plan.append({"condition": c, "adaptateur": exiger_adaptateur(section["evaluation"]["adaptateur_de"][c]), "dose": dose})
    return plan


def condition_de(section: dict, condition: str) -> dict:
    for p in plan_d_evaluation(section):
        if p["condition"] == condition:
            return p
    raise GardeArret(f"condition d'évaluation {condition!r} inconnue : {tuple(section['evaluation']['conditions'])} (refus)")
