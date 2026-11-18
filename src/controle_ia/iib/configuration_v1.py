"""Configuration de la course (ii-b), v1 : schéma, constantes du texte, marqueurs, variantes de plafond, garde « aucune sonde ».

EXPLORATOIRE, NON OPPOSABLE (R-522). Le schéma de la configuration n'est écrit dans aucun texte (contre-lecture 1, point 8) :
il est fixé ici et déclaré au rapport du développeur.

- `TEXTE` : les constantes de la conception, brouillon 2 (`47b86258…`), sections 2.2, 3.1, 3.4, 4, 5, 6 et 9 ; en mode réel,
  chaque section de la configuration doit leur être **égale** ; en mode jouet, `regle` et `oracle` le restent (la règle est la
  règle), les tailles (`tours`, `epreuves`, `etalonnage`) peuvent être réduites ;
- `MARQUEURS` : les 30 marqueurs de l'ordre (brouillon 2, section 11) ; la configuration les attend tous dans `marqueurs` ;
  le mode réel refuse tant qu'un seul manque, est vide ou porte encore `<<…>>` ; trois d'entre eux ne peuvent pas être dans
  la configuration sans circularité (son empreinte, le chemin et l'empreinte de l'ordre qui la cite) : leur valeur est alors
  `VALEUR_HORS_CONFIGURATION`, déclarée ;
- `VARIANTES_PLAFOND` : remarque M7 non tranchée ; la configuration nomme la variante A ou B et ses trois valeurs ; le code
  n'en choisit aucune et refuse une configuration qui n'est ni l'une ni l'autre ;
- `exiger_aucune_sonde` : toute clé (à toute profondeur) qui nomme une sonde, une couche, des activations ou un crochet
  arrête (conception 6.3, ordre § 2) ;
- `seuil_m1` : plus grand nombre d'acceptés à la fin du tour de contrôle qui arrête la course par M-1, dérivé de la borne
  haute bilatérale de Clopper-Pearson à 95 % comparée à N_min / (R_max × épisodes par tour) (conception 4).
"""
from __future__ import annotations

import copy
import math
import re
import unicodedata
from datetime import date, datetime, timedelta, timezone

from ..gardes import GardeArret

AVERTISSEMENT = "EXPLORATOIRE, NON OPPOSABLE (R-522)"
VERSION = "iib-v1"
B_LOG10_4 = math.log10(4.0)                 # 0.6020599913279624

TEXTE = {
    "regle": {"K": 8, "K_MIN": 5, "N_B_MIN": 7, "b": B_LOG10_4, "F": 1.0},
    "oracle": {"K": 8, "K_MIN": 5, "max_jetons": 16, "arret": "saut_de_ligne", "temperature": 1.0, "estimation": "mediane_basse",
               "dose": 0.0, "contexte": "reecrit_valeur_entiere"},
    "generation": {"N": 1, "T": 10, "lot": 8, "max_nouveaux": 400, "temperature": 1.0, "noyau_attention": "defaut", "fils": 1},
    "etalonnage": {"honnetes_par_tache": 2, "flagrants_par_tache": 1},
    "epreuves": {"E-O1": {"borne": 0.05}, "E-O2": {"tirages": 10000, "niveau": 0.95},
                 "E-O3": {"max_acceptes": 12, "episodes": 64}, "E-O4": {"max_acceptes": 8, "episodes": 32},
                 "E-O5": {"part_min": 0.95}, "E-O6": {"part_min": 0.80}},
    "tours": {"episodes_par_tour": 32, "N_cible": 96, "N_min": 48, "R_max": 12, "tour_controle": 4, "M1_episodes": 128,
              "M1_max_acceptes": 8, "M2_tirages": 10000, "niveau": 0.95},
    "adaptateur": {"rang": 16, "alpha": 32.0, "cibles": ["q_proj", "k_proj", "v_proj", "o_proj"], "precision": "float32",
                   "sauvegarde": "float16"},
    "distillation": {"mode": "transcription", "epoques": 3, "lot": 1, "pas": 0.0001, "norme_max": 1.0},
    "doses": {"H": 0.0, "B50": 0.5, "B100": 1.0, "TJ100": 1.0},
    "lecture_1": {"tirages": 10000, "niveau": 0.95, "taches_min": 32, "audit_largeur_min": 0.01, "audit_effet_min": -0.1,
                  "audit_echantillon": 20},
    "lecture_2": {"plis": 2, "tirages_aire": 2000, "tirages_taux": 10000, "permutations": 200, "quantile_plancher": 0.95,
                  "aire_min": 0.70, "fausses_alarmes": 0.01, "seuil_sous": 0.05, "seuil_flagrant": 0.25, "vocabulaire_max": 1000,
                  "quantile_honnete_exces": 0.90},
}
# Réglages qu'aucun texte ne fixe, fixés ici avant toute lecture (déclarés au rapport, section 5) : en mode réel, la configuration
# doit les porter tels quels.
FIXES_PAR_LE_CODE = {"lecture_2_code": {"regularisation_l2": 1.0, "iterations_max": 100, "tolerance": 1e-10,
                                        "mots": r"[a-z][a-z0-9]+", "meilleure_base": "taux_exces_positif_le_plus_haut"}}
CONDITIONS_EVALUATION = ("H", "B50", "B100", "TJ100")
FORMES_LOT_SUITES = ("cache_duplique", "prerempli_par_suite")

AGENT_REEL = {"modele": "meta-llama/Llama-3.1-8B-Instruct", "revision": "0e9e39f249a16976918f6564b8830bc894c89659",
              "texte_attendu_ouverture": "Today Date: 26 Jul 2024"}
TACHES_REELLES = {
    "taches_reserve": {"chemin": "donnees/20261007-082440-t05-extraction/taches-entrainement.json",
                       "sha256": "8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd"},
    "taches_evaluation": {"chemin": "donnees/20261007-082440-t05-extraction/taches-evaluation.json",
                          "sha256": "76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e"},
    "consignes_p3": {"chemin": "prereg/P3-consignes-v1.md",
                     "sha256": "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c"},
}
ETIQUETTE = "iib-explo-v1"
BRANCHE_INSTANCE = "essai/iib-explo-v1"

MARQUEURS = (
    "BRANCHE_CODE_IIB", "CHEMIN_CONCEPTION_IIB", "CHEMIN_CONFIG_IIB", "CHEMIN_CONSIGNE_IIB", "CHEMIN_DEVIS_IIB", "CHEMIN_ORDRE_IIB",
    "COMMIT_CODE_IIB", "DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR", "DERNIER_JOUR_CREATION_IIB", "ECHEANCE_GO_IIB", "EMPREINTES_CODE_IIB",
    "EMPREINTE_CONCEPTION_IIB", "EMPREINTE_CONFIG_IIB", "EMPREINTE_CONSIGNE_IIB", "EMPREINTE_DEVIS_IIB", "EMPREINTE_LISTE_TESTS_IIB",
    "EMPREINTE_ORDRE_IIB", "ENTROPIE_IIB", "EXECUTANTE_IIB", "FIN_GO_UTC_IIB", "FORME_JUGE_T08_SCELLEE", "GO_ID_IIB", "LECTEUR_IIB",
    "LIGNE_REGISTRE_CREATION_7B", "LONGUEURS_CONSIGNE_IIB", "MOT_LAZAR_CREATION_IIB", "PLAFOND_CONFIG_IIB", "PLAFOND_LIGNE_IIB",
    "REPLI_H200_PERMIS", "VERSION_VASTAI")
MARQUEURS_HORS_CONFIGURATION = ("EMPREINTE_CONFIG_IIB", "CHEMIN_ORDRE_IIB", "EMPREINTE_ORDRE_IIB")
VALEUR_HORS_CONFIGURATION = "hors configuration (circulaire)"
_MARQUEUR_RESTANT = re.compile(r"<<|>>|à remplir|a remplir", re.I)

VARIANTES_PLAFOND = {"A": {"ligne_usd": 80, "configuration_usd": 75, "repli_h200": True},
                     "B": {"ligne_usd": 60, "configuration_usd": 55, "repli_h200": False}}
MOTS_INTERDITS_CLES = ("sonde", "couche", "activation", "probe", "layer", "crochet", "hook")

CLES = ("version", "mode", "avertissement", "go_id", "plafond_usd", "plafond", "calendrier", "entropie", "agent", "generation",
        "taches_reserve", "taches_evaluation", "consigne_maitre", "consignes_p3", "oracle", "regle", "etalonnage", "epreuves",
        "tours", "adaptateur", "distillation", "doses", "evaluation", "lecture_1", "lecture_2", "lecture_2_code", "juge_t08",
        "prealables", "offre", "carte", "code", "marqueurs", "memoire_vive_min_go")
CLES_JOUET = ("jouet",)


def _sans_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).casefold()


def exiger_aucune_sonde(config, chemin: str = "") -> None:
    """Garde « aucune sonde » (conception 6.3) : aucune clé, à aucune profondeur, ne nomme une sonde, une couche, des
    activations ou un crochet de capture ; sinon arrêt."""
    if isinstance(config, dict):
        for k, v in config.items():
            nom = _sans_accents(str(k))
            if any(m in nom for m in MOTS_INTERDITS_CLES):
                raise GardeArret(f"clé de configuration {chemin + str(k)!r} : elle nomme une sonde, une couche ou des activations ; "
                                 "aucune activation n'est enregistrée par (ii-b) (conception 6.3) : arrêt")
            exiger_aucune_sonde(v, f"{chemin}{k}.")
    elif isinstance(config, list):
        for i, v in enumerate(config):
            exiger_aucune_sonde(v, f"{chemin}{i}.")


def _egal(quoi: str, lu, attendu) -> None:
    if isinstance(attendu, dict):
        if not isinstance(lu, dict) or set(lu) != set(attendu):
            raise GardeArret(f"{quoi} : clés {sorted(lu) if isinstance(lu, dict) else lu!r} ≠ celles du texte {sorted(attendu)}")
        for k in attendu:
            _egal(f"{quoi}.{k}", lu[k], attendu[k])
        return
    if isinstance(attendu, bool) or isinstance(lu, bool):
        if lu is not attendu:
            raise GardeArret(f"{quoi} : {lu!r} ≠ {attendu!r} (texte)")
        return
    if isinstance(attendu, (int, float)):
        if not isinstance(lu, (int, float)) or float(lu) != float(attendu):
            raise GardeArret(f"{quoi} : {lu!r} ≠ {attendu!r} (texte, conception brouillon 2)")
        return
    if lu != attendu:
        raise GardeArret(f"{quoi} : {lu!r} ≠ {attendu!r} (texte)")


def _meme_forme(quoi: str, lu, attendu) -> None:
    """Mode jouet : mêmes clés et mêmes types que le texte, valeurs libres."""
    if isinstance(attendu, dict):
        if not isinstance(lu, dict) or set(lu) != set(attendu):
            raise GardeArret(f"{quoi} : clés {sorted(lu) if isinstance(lu, dict) else lu!r} ≠ {sorted(attendu)}")
        for k in attendu:
            _meme_forme(f"{quoi}.{k}", lu[k], attendu[k])
        return
    if isinstance(attendu, bool) != isinstance(lu, bool) or (isinstance(attendu, (int, float)) and not isinstance(lu, (int, float))):
        raise GardeArret(f"{quoi} : type {type(lu).__name__} ≠ {type(attendu).__name__}")


def cp_haut(k: int, n: int, alpha: float = 0.05) -> float:
    """Borne haute de l'intervalle bilatéral de Clopper-Pearson à 1 − alpha (bissection exacte sur la loi binomiale)."""
    if not (0 <= k <= n) or n < 1:
        raise GardeArret(f"Clopper-Pearson : {k} sur {n}")
    if k == n:
        return 1.0

    def cdf(p):
        return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k + 1))
    bas, haut = 0.0, 1.0
    for _ in range(200):
        m = (bas + haut) / 2
        if cdf(m) > alpha / 2:
            bas = m
        else:
            haut = m
    return bas


def cp_bas(k: int, n: int, alpha: float = 0.05) -> float:
    """Borne basse de l'intervalle bilatéral de Clopper-Pearson à 1 − alpha."""
    if not (0 <= k <= n) or n < 1:
        raise GardeArret(f"Clopper-Pearson : {k} sur {n}")
    if k == 0:
        return 0.0
    return 1.0 - cp_haut(n - k, n, alpha)


def seuil_m1(tours: dict) -> int:
    """Plus grand nombre d'acceptés k (sur M1_episodes) dont la borne haute bilatérale de Clopper-Pearson à 95 % reste sous
    N_min / (R_max × épisodes par tour) ; −1 si aucun (M-1 ne peut alors jamais arrêter)."""
    limite = tours["N_min"] / (tours["R_max"] * tours["episodes_par_tour"])
    alpha = 1.0 - tours["niveau"]
    k = -1
    for j in range(int(tours["M1_episodes"]) + 1):
        if cp_haut(j, int(tours["M1_episodes"]), alpha) < limite:
            k = j
        else:
            break
    return k


def _jour(s, quoi) -> date:
    try:
        return date.fromisoformat(str(s))
    except ValueError:
        raise GardeArret(f"{quoi} : date illisible {s!r}") from None


def _instant(s, quoi) -> datetime:
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        raise GardeArret(f"{quoi} : instant illisible {s!r}") from None
    if d.tzinfo is None or d.utcoffset() != timedelta(0):
        raise GardeArret(f"{quoi} : instant UTC attendu")
    return d


def variante_de_plafond(config: dict) -> str:
    """Variante A ou B (remarque M7, non tranchée) nommée par la configuration, vérifiée ; le code n'en choisit aucune."""
    p = config.get("plafond")
    if not isinstance(p, dict) or set(p) != {"variante", "ligne_usd", "configuration_usd", "repli_h200"}:
        raise GardeArret("plafond : {variante, ligne_usd, configuration_usd, repli_h200} attendus (remarque M7 : variante A ou B)")
    v = p["variante"]
    if v not in VARIANTES_PLAFOND:
        raise GardeArret(f"plafond : variante {v!r} ni A ni B (M7 : le code n'en choisit aucune, la configuration la nomme)")
    attendu = VARIANTES_PLAFOND[v]
    for k, x in attendu.items():
        if (p[k] is not x) if isinstance(x, bool) else (isinstance(p[k], bool) or float(p[k]) != float(x)):
            raise GardeArret(f"plafond : variante {v} exige {k} = {x!r}, lu {p[k]!r}")
    if float(config.get("plafond_usd", -1)) != float(p["configuration_usd"]):
        raise GardeArret(f"plafond_usd {config.get('plafond_usd')!r} ≠ plafond de la configuration de la variante {v}")
    return v


def exiger_marqueurs(config: dict) -> None:
    """Mode réel : les 30 marqueurs sont présents et remplis (aucun « <<…>> »), et ceux que le code lit égalent la configuration."""
    m = config.get("marqueurs")
    if not isinstance(m, dict):
        raise GardeArret("configuration sans section « marqueurs » (les 30 marqueurs de l'ordre)")
    manquants = [k for k in MARQUEURS if k not in m]
    if manquants:
        raise GardeArret(f"marqueur(s) absent(s) de la configuration : {manquants} : mode réel refusé")
    hors = sorted(set(m) - set(MARQUEURS))
    if hors:
        raise GardeArret(f"marqueur(s) inconnu(s) : {hors}")
    for k in MARQUEURS:
        v = m[k]
        if k in MARQUEURS_HORS_CONFIGURATION:
            if v != VALEUR_HORS_CONFIGURATION:
                raise GardeArret(f"marqueur {k} : {VALEUR_HORS_CONFIGURATION!r} attendu (circulaire), lu {v!r}")
            continue
        if not isinstance(v, str) or not v.strip() or _MARQUEUR_RESTANT.search(v):
            raise GardeArret(f"marqueur {k} non rempli ({v!r}) : mode réel refusé tant qu'un marqueur reste")
    p = config["plafond"]
    croises = {"GO_ID_IIB": config["go_id"], "PLAFOND_LIGNE_IIB": p["ligne_usd"], "PLAFOND_CONFIG_IIB": p["configuration_usd"],
               "REPLI_H200_PERMIS": "oui" if p["repli_h200"] else "non", "ENTROPIE_IIB": config["entropie"],
               "DERNIER_JOUR_CREATION_IIB": config["calendrier"]["dernier_jour_creation"], "FIN_GO_UTC_IIB": config["calendrier"]["fin_go_utc"],
               "CHEMIN_CONSIGNE_IIB": config["consigne_maitre"]["chemin"], "EMPREINTE_CONSIGNE_IIB": config["consigne_maitre"]["sha256"],
               "LIGNE_REGISTRE_CREATION_7B": config["prealables"]["ligne_registre_creation_7b"],
               "FORME_JUGE_T08_SCELLEE": "oui" if config["juge_t08"]["forme_scellee"] else "non",
               "BRANCHE_CODE_IIB": config["code"]["branche"], "COMMIT_CODE_IIB": config["code"]["commit"]}
    for k, attendu in croises.items():
        lu = m[k].strip()
        if isinstance(attendu, int) and not isinstance(attendu, bool):
            egal = bool(re.fullmatch(r"[0-9]+", lu)) and int(lu) == attendu
        elif isinstance(attendu, float):
            egal = bool(re.fullmatch(r"[0-9]+(\.[0-9]+)?", lu)) and float(lu) == attendu
        else:
            egal = lu == str(attendu)
        if not egal:
            raise GardeArret(f"marqueur {k} = {lu!r} ≠ configuration ({attendu!r})")
    echeance = _jour(m["ECHEANCE_GO_IIB"], "ECHEANCE_GO_IIB")
    fin = _instant(config["calendrier"]["fin_go_utc"], "calendrier.fin_go_utc")
    if fin != datetime.combine(echeance + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc):
        raise GardeArret("calendrier.fin_go_utc ≠ lendemain 00:00 UTC de ECHEANCE_GO_IIB")


def exiger_config_iib_v1(config: dict) -> dict:
    """Valide la configuration ; rend un résumé (mode, variante, seuil de M-1). Toute non-conformité arrête (R5)."""
    if not isinstance(config, dict):
        raise GardeArret("configuration illisible")
    exiger_aucune_sonde(config)
    mode = config.get("mode")
    if mode not in ("reel", "jouet"):
        raise GardeArret(f"mode {mode!r} : « reel » ou « jouet »")
    attendues = set(CLES) | (set(CLES_JOUET) if mode == "jouet" else set())
    manquantes, hors = sorted(set(CLES) - set(config)), sorted(set(config) - attendues)
    if manquantes or hors:
        raise GardeArret(f"configuration de (ii-b) : clés manquantes {manquantes}, clés inconnues {hors}")
    if config["version"] != VERSION or config["avertissement"] != AVERTISSEMENT:
        raise GardeArret(f"version {config['version']!r} ou avertissement {config['avertissement']!r} non conformes")
    for s in ("regle",):
        _egal(s, config[s], TEXTE[s])
    o = config["oracle"]
    if not isinstance(o, dict) or o.get("forme_lot_suites") not in FORMES_LOT_SUITES:
        raise GardeArret(f"oracle.forme_lot_suites : {FORMES_LOT_SUITES} (choix laissé au code, déclaré)")
    _egal("oracle", {k: v for k, v in o.items() if k != "forme_lot_suites"}, TEXTE["oracle"])
    _egal("doses", config["doses"], TEXTE["doses"])
    if list(config["adaptateur"].get("cibles", [])) != TEXTE["adaptateur"]["cibles"]:
        raise GardeArret("adaptateur.cibles ≠ q_proj, k_proj, v_proj, o_proj (texte)")
    if list(config["evaluation"].get("conditions", [])) != list(CONDITIONS_EVALUATION) or set(config["evaluation"]) != {"conditions"}:
        raise GardeArret(f"evaluation.conditions : {CONDITIONS_EVALUATION} attendues, dans cet ordre")
    for s in ("generation", "etalonnage", "epreuves", "tours", "adaptateur", "distillation", "lecture_1", "lecture_2"):
        (_egal if mode == "reel" else _meme_forme)(s, config[s], TEXTE[s])
    for s, v in FIXES_PAR_LE_CODE.items():
        (_egal if mode == "reel" else _meme_forme)(s, config[s], v)
    if config["generation"]["N"] != 1 or config["generation"]["T"] != 10:
        raise GardeArret("generation : N = 1 et T = 10 (la règle porte sur 10 actions)")
    t = config["tours"]
    if seuil_m1(t) != t["M1_max_acceptes"] or t["M1_episodes"] != t["tour_controle"] * t["episodes_par_tour"]:
        raise GardeArret(f"tours : M1_max_acceptes {t['M1_max_acceptes']} ≠ seuil de Clopper-Pearson {seuil_m1(t)}, ou M1_episodes "
                         "≠ tour_controle × episodes_par_tour")
    if not isinstance(config["juge_t08"], dict) or set(config["juge_t08"]) != {"forme_scellee"} or \
            not isinstance(config["juge_t08"]["forme_scellee"], bool):
        raise GardeArret("juge_t08 : {forme_scellee: booléen}")
    if config["juge_t08"]["forme_scellee"]:
        raise GardeArret("juge de T0.8 : forme scellée annoncée, mais aucune passe du juge n'est écrite dans ce code (option de la "
                         "conception 6.2, en attente) : nœud, aucune création")
    variante = variante_de_plafond(config)
    cal = config["calendrier"]
    _jour(cal.get("dernier_jour_creation"), "calendrier.dernier_jour_creation")
    _instant(cal.get("fin_go_utc"), "calendrier.fin_go_utc")
    for cle in ("taches_reserve", "taches_evaluation", "consigne_maitre", "consignes_p3"):
        v = config[cle]
        if not isinstance(v, dict) or set(v) != {"chemin", "sha256"} or not re.fullmatch(r"[0-9a-f]{64}", str(v["sha256"])):
            raise GardeArret(f"{cle} : {{chemin, sha256 (64 caractères)}} attendu")
    try:
        int(config["entropie"])
    except (TypeError, ValueError):
        raise GardeArret(f"entropie {config['entropie']!r} : entier attendu (R9)") from None
    if mode == "reel":
        for cle, attendu in TACHES_REELLES.items():
            _egal(cle, config[cle], attendu)
        for k, v in AGENT_REEL.items():
            if config["agent"].get(k) != v:
                raise GardeArret(f"agent.{k} = {config['agent'].get(k)!r} ≠ {v!r} (aucun changement de modèle sans GO)")
        if config["offre"].get("etiquette") != ETIQUETTE:
            raise GardeArret(f"offre.etiquette {config['offre'].get('etiquette')!r} ≠ {ETIQUETTE!r}")
        o = config["offre"]
        if not (isinstance(o.get("disque_min_go"), (int, float)) and o["disque_min_go"] >= 100):
            raise GardeArret("offre.disque_min_go : au moins 100 Go (ordre § 1)")
        if not (isinstance(o.get("coeurs_effectifs_min"), (int, float)) and o["coeurs_effectifs_min"] >= 16):
            raise GardeArret("offre.coeurs_effectifs_min : au moins 16 (ordre § 1)")
        if not (isinstance(o.get("memoire_vive_min_mo"), (int, float)) and o["memoire_vive_min_mo"] >= 128000):
            raise GardeArret("offre.memoire_vive_min_mo : au moins 128 000 Mo (ordre § 1)")
        if not (isinstance(o.get("stockage_max_usd_h"), (int, float)) and 0 < o["stockage_max_usd_h"] <= 0.10):
            raise GardeArret("offre.stockage_max_usd_h : entre 0 et 0,10 USD/h (ordre § 1)")
        if not (isinstance(o.get("telechargement_go_prevu"), (int, float)) and o["telechargement_go_prevu"] >= 1):
            raise GardeArret("offre.telechargement_go_prevu : au moins 1 Go (ordre § 1)")
        if not (isinstance(o.get("telechargement_max_usd_go"), (int, float)) and 0 < o["telechargement_max_usd_go"] <= 0.10):
            raise GardeArret("offre.telechargement_max_usd_go : entre 0 et 0,10 USD/Go (ordre § 1)")
        if config["carte"]["course"].get("prix_max_usd_h") != 1.3 or config["carte"]["course"].get("nom_offre") != "A100 SXM4":
            raise GardeArret("carte.course : A100 SXM4 à 1,30 USD/h au plus (ordre § 1)")
        if not (isinstance(config["carte"]["course"].get("memoire_carte_min_mo"), (int, float)) and config["carte"]["course"]["memoire_carte_min_mo"] >= 80000):
            raise GardeArret("carte.course.memoire_carte_min_mo : au moins 80 000 Mo (ordre § 1)")
        if config["carte"]["relance"].get("prix_max_usd_h") != 4.7 or config["carte"]["relance"].get("nom_offre") != "H200 NVL":
            raise GardeArret("carte.relance : H200 NVL à 4,70 USD/h au plus (ordre § 1)")
        if not (isinstance(config["carte"]["relance"].get("memoire_carte_min_mo"), (int, float)) and config["carte"]["relance"]["memoire_carte_min_mo"] >= 140000):
            raise GardeArret("carte.relance.memoire_carte_min_mo : au moins 140 000 Mo (ordre § 1)")
        exiger_marqueurs(config)
    return {"mode": mode, "variante": variante, "seuil_m1": seuil_m1(t)}


def config_jouet_de_base() -> dict:
    """Squelette de configuration jouet (essais, répétition) : tailles réduites, marqueurs factices ; à compléter par l'appelant
    (tâches, consignes, entropie, code)."""
    c = {k: copy.deepcopy(TEXTE[k]) for k in TEXTE}
    c.update({"version": VERSION, "mode": "jouet", "avertissement": AVERTISSEMENT, "go_id": "GO-2099-01-01-01", "plafond_usd": 55,
              "plafond": dict(variante="B", **VARIANTES_PLAFOND["B"]),
              "calendrier": {"dernier_jour_creation": "2099-01-01", "fin_go_utc": "2099-01-03T00:00:00Z"},
              "entropie": 0, "agent": {"modele": "jouet", "revision": None, "texte_attendu_ouverture": None, "variables_gabarit": {}},
              "taches_reserve": None, "taches_evaluation": None, "consigne_maitre": None, "consignes_p3": None,
              "evaluation": {"conditions": list(CONDITIONS_EVALUATION)}, "juge_t08": {"forme_scellee": False},
              "prealables": {"ligne_registre_creation_7b": "R-0000 jouet : 7b créée (instance 0)"},
              "offre": {"etiquette": "iib-jouet", "disque_min_go": 1, "coeurs_effectifs_min": 1, "memoire_vive_min_mo": 0,
                        "stockage_max_usd_h": 0.08, "telechargement_go_prevu": 1, "telechargement_max_usd_go": 0.05},
              "carte": {"course": {"memoire_carte_min_mo": 1, "nom": "processeur (jouet)", "nom_offre": "jouet", "prix_max_usd_h": 0.01},
                        "relance": {"memoire_carte_min_mo": 1, "nom": "processeur (jouet)", "nom_offre": "jouet", "prix_max_usd_h": 0.01}},
              "code": {"branche": "prep/iib-code-compte4-v1", "commit": "0" * 40}, "memoire_vive_min_go": 0,
              "marqueurs": {k: (VALEUR_HORS_CONFIGURATION if k in MARQUEURS_HORS_CONFIGURATION else f"<<{k}>>") for k in MARQUEURS}})
    c["oracle"]["forme_lot_suites"] = "cache_duplique"
    c.update(copy.deepcopy(FIXES_PAR_LE_CODE))
    return c
