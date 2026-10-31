#!/usr/bin/env python3
"""Extension de l'arène synthétique : familles qu'aucun moniteur seul ne couvre (Q3) et prix imposé à l'adversaire
synthétique par une lecture jointe activations + comportement (Q3b) — v1.

Modèle mathématique synthétique seulement : lois gaussiennes N(μ, I) sur des vecteurs synthétiques de R⁶, moniteurs
simples (linéaires ou maxout) seuillés à un taux de fausses alertes α sur la loi propre N(0, I). Aucun modèle réel,
aucun texte, rien d'applicable à un vrai réseau. L'objet : certifier la (non-)couverture d'une famille par une classe
de moniteurs, mesurer la valeur du tirage au hasard (mélange d'équilibre moins meilleur moniteur pur), l'union contre
le mélange, le cycle de la défense unique, et (Q3b) le gain maximal de l'adversaire synthétique sous trois défenses.

Recopie et adapte `arene-melange-equilibre-v1/arene_melange_v3.py` (jamais modifié) : moniteurs, « ou » composite,
oracle « détection », jeu à somme nulle, double oracle, gardes, graines, identité du préenregistrement, arrêt par PID.
Changements déclarés : l'attaquant ne déplace que la moyenne (lois N(μ, I), une composante) ; la famille est la
réunion de J = 2 boules de comportement (deux manières de réaliser le comportement visé) ; certains moniteurs ne lisent
qu'une vue (bloc de 3 coordonnées) ; une couche exacte (formules fermées et recherches à une dimension) donne les valeurs
de référence ; Q3b est entièrement analytique.

Familles (par instance, générateur à graines dérivées) :
- N2 (champ complet) : modes opposés c₁ = R₁u, c₂ = −R₂u — aucun moniteur linéaire ne couvre (certificat exact) ;
- C2 (champ complet) : modes du même côté, angle γ — un moniteur linéaire couvre (témoin de même taille) ;
- NV (deux vues) : un mode par vue — aucun moniteur d'une vue ne couvre, quelle que soit sa taille (certificat exact :
  la loi marginale de la vue non déplacée est la loi propre) ;
- CV (deux vues) : deux modes dans la même vue — un moniteur d'une vue couvre (témoin).

Bras : régime champ complet (N2, C2) : A, B, B′ (Bp), D, PUR_B, U_B, PUR_Bp, U_Bp ; régime vues (NV, CV) : AV, BpV, DV,
PUR_BpV, U_BpV. PUR = moniteur de poids maximal du mélange, déployé seul ; U = « ou » des moniteurs du support.

Commandes (racines d'essai de la plage 20265001–20265999 seulement ; décision refusée sans préenregistrement scellé ni
calcul décisif du pilote principal) :
    PYTHONPATH=src python3 <ce fichier> identite
    PYTHONPATH=src python3 <ce fichier> exact --instances 0:8
    PYTHONPATH=src python3 <ce fichier> essai --instances 0:8 --sortie F.json --processus 2 [--racine 20265011]
    PYTHONPATH=src python3 <ce fichier> prix --configs 0:200 --sortie F.json [--racine 20265021]
    PYTHONPATH=src python3 <ce fichier> audit-essai --pilote F.json --instances 0:1 --sortie A.json
    PYTHONPATH=src python3 <ce fichier> decision --prereg prereg/<scellé>.md --run-principal <run-id> --instances 0:N
        --configs 0:M --run-id ID
    PYTHONPATH=src python3 <ce fichier> orphelins --pids FICHIER [--arreter]
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import signal  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from collections import Counter  # noqa: E402
from dataclasses import asdict, dataclass, replace  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
from scipy.optimize import linprog, minimize, minimize_scalar  # noqa: E402
from scipy.special import expit, log_ndtr, logsumexp, ndtr, ndtri, softmax  # noqa: E402

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[4]
if str(DEPOT / "src") not in sys.path:
    sys.path.insert(0, str(DEPOT / "src"))

from controle_ia.gardes import GardeArret, exiger_numpy_minimal, lever_sur_term  # noqa: E402

VERSION = "arene_extension_v1"
IDENTIFIANT_PREREG = "PREREG-ARENE-EXTENSION-FAMILLES-V1"
FICHIERS_BIBLIOTHEQUE = ("src/controle_ia/gardes.py", "src/controle_ia/prereg.py", "src/controle_ia/scellement.py",
                         "src/controle_ia/manifeste.py")

# --- racines (R9) : gelées dans gel-conception-arene-extension-v1.md avant tout calcul ---------------------------------
RACINE_Q3 = 20265901           # décision Q3 : jamais employée hors décision autorisée
RACINE_PRIX = 20265902         # décision Q3b : idem
RACINES_DECISION = (RACINE_Q3, RACINE_PRIX)
RACINE_PRINCIPALE = 20261201   # racine de décision de l'arène principale : le calcul décisif de l'extension la suit
# racines déjà employées dans le dossier de l'arène (brouillons 1 à 3, LISEZMOI, journaux, contre-lectures, essais) ;
# 20262297 et 20262313 : employées par décalage dans les essais v2 et v3 (RACINE_TESTS + 1000), absentes des textes,
# relevées par la session parallèle (gel v4) et vérifiées dans test_arene_melange_v2.py l. 643 et v3 l. 699
RACINES_DEJA_EMPLOYEES = (20261201, 20261202, 20261291, 20261292, 20261293, 20261294, 20261295, 20261296, 20261297,
                          20261298, 20262291, 20262297, 20262313, 20261301, 20261101, 20261311, 20261312, 20261313,
                          20261314, 20261315, 20261316, 20269501, 20269502, 20269731, 20269732, 20269741, 20269742)
PLAGE_B4 = (20264001, 20264999)          # pilote b4 en parallèle (R-747)
PLAGE_EXTENSION = (20265001, 20265999)   # seule plage permise hors décision (R-747)
RACINE_TESTS, RACINE_TESTS_BIS = 20265001, 20265002
RACINE_ESSAI = 20265011
RACINE_ESSAI_PRIX = 20265021
RACINE_TEMPS = 20265031
RACINES_RESERVEES = (20265041, 20265042)

# --- codes de dérivation des graines -------------------------------------------------------------------------------
FAMILLES = {"N2": 1, "C2": 2, "NV": 3, "CV": 4}
REGIME = {"N2": "champ", "C2": "champ", "NV": "vues", "CV": "vues"}
NON_COUVRABLES = ("N2", "NV")
TEMOIN_DE = {"N2": "C2", "NV": "CV"}
TRAJECTOIRES = {  # nom → (code, type, une vue ?, unités de l'oracle ; None = t + 1)
    "A": (1, "unique", False, 1), "B": (2, "melange", False, 1), "Bp": (8, "melange", False, "Bp"),
    "D": (4, "unique", False, None),
    "AV": (21, "unique", True, 1), "BpV": (28, "melange", True, "Bp"), "DV": (24, "unique", True, None)}
TEMOINS = {  # nom → (code, source, sorte)
    "PUR_B": (11, "B", "pur"), "U_B": (12, "B", "union"), "PUR_Bp": (13, "Bp", "pur"), "U_Bp": (14, "Bp", "union"),
    "PUR_BpV": (31, "BpV", "pur"), "U_BpV": (32, "BpV", "union")}
BRAS_DU_REGIME = {"champ": ("A", "B", "Bp", "D", "PUR_B", "U_B", "PUR_Bp", "U_Bp"),
                  "vues": ("AV", "BpV", "DV", "PUR_BpV", "U_BpV")}
COMMUN = 0
ROLE_FAMILLE, ROLE_PROPRE_ENTR, ROLE_ATTAQUE_ENTR, ROLE_CAL, ROLE_FPR = 0, 1, 2, 3, 4
ROLE_MC, ROLE_DEPARTS, ROLE_EVAL, ROLE_INIT_MAXOUT, ROLE_FINAL = 5, 6, 7, 8, 11
ROLE_AUDIT, ROLE_PRIX, ROLE_REECH = 15, 20, 99
SCHEMA_GRAINES = ("SeedSequence(entropy=racine, spawn_key=(code_famille, code_delta, instance, code_bras, tour, role, "
                  "...)) ; familles N2 1, C2 2, NV 3, CV 4 ; familles tirees par (0, 0, instance, 0, 0, 0) ; bras A 1, "
                  "B 2, D 4, B' 8, AV 21, DV 24, B'V 28 ; temoins PUR et U : graines de leur bras source ; roles "
                  "propre 1, attaques d'entrainement 2, calibration 3, fausses alertes 4, Monte-Carlo 5, departs 6, "
                  "evaluation 7, init maxout 8, final 11, attaquant independant 15 ; Q3b (20, configuration) ; "
                  "reechantillonnage (99, code_famille, code_delta, code_grandeur)")
QUANTILES = (0.003125, 0.00625, 0.0125, 0.025, 0.05, 0.95, 0.975, 0.9875, 0.99375, 0.996875)
I3_NUL_T8 = float(np.mean([(t - 2) / (t - 1) for t in range(3, 9)]))   # 0,7345 : valeur nulle du taux de retours


@dataclass(frozen=True)
class Config:
    d: int = 6                        # dimension des activations synthétiques
    d_vue: int = 3                    # régime vues : deux vues de 3 coordonnées
    J: int = 2                        # modes par famille
    R_min: float = 4.25               # rayons des centres des modes
    R_max: float = 4.75
    gamma_min_deg: float = 20.0       # angle entre les modes des témoins couvrables
    gamma_max_deg: float = 45.0
    deltas: tuple = (1.0, 1.4)        # budgets de comportement (rayon des boules de modes)
    alpha: float = 0.01
    theta_couverture: float = 0.5     # « couvre » : détection au pire cas sur la famille ≥ θ*
    T: int = 8
    n_propre_entr: int = 2000
    n_attaque_entr: int = 2000
    n_cal: int = 20000
    n_fpr: int = 20000
    n_eval: int = 20000
    n_mc: int = 256
    n_mc_final: int = 512
    departs: int = 3                  # départs tirés par mode, à chaque tour
    departs_final: int = 6            # départs tirés par mode, attaquant final standard
    departs_renforce: int = 16        # départs tirés par mode, attaquant final renforcé
    iter_max: int = 100
    iter_renforce: int = 200
    tau: float = 0.25
    l2: float = 1e-3
    departs_entr: int = 8
    iter_entr: int = 300
    unites_Bp: int = 9                # unités de chaque moniteur de B′ et B′V (classe de l'arène v3)
    lambda_ou: float = 8.0
    tol_fpr: float = 0.005
    taux_nonconv_max: float = 0.10
    taux_departs_non_finis_max: float = 0.05
    plafond_cpu_tache_s: float = 900.0
    n_instances: int = 60             # N par δ et par famille (S4)
    grille_exacte: int = 20001        # couche exacte : points des recherches à une dimension
    tol_selle: float = 1e-6
    audit_departs: int = 40
    audit_n_mc: int = 1024
    audit_iter: int = 300
    audit_es_generations: int = 200
    audit_es_lambda: int = 12
    marge_audit: float = 0.01         # artefact d'audit : classe changée ou écart > m/2
    L_max: int = 8                    # Q3b : vues surveillées 1 … L_max
    Ra_min: float = 2.5
    Ra_max: float = 3.5
    sD_min: float = 2.0
    sD_max: float = 4.0
    kappa_min: float = 0.0
    kappa_max: float = 1.5
    beta0_min: float = 0.0
    beta0_max: float = 1.0
    n_configs: int = 400              # Q3b : configurations de la décision
    grille_partage: int = 201
    grille_x: int = 401
    schema_graines: str = SCHEMA_GRAINES

    def canonique(self) -> bytes:
        return json.dumps(asdict(self), sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()

    def empreinte(self) -> str:
        return hashlib.sha256(self.canonique()).hexdigest()


CONFIG_V1 = Config()


def exiger_config(cfg: Config) -> Config:
    """Garde : configuration cohérente avant toute exécution."""
    if cfg is None or not cfg.deltas or any(not d > 0 for d in cfg.deltas) or \
            list(cfg.deltas) != sorted(set(cfg.deltas)):
        raise GardeArret(f"configuration : δ invalides (positifs, strictement croissants) : {getattr(cfg, 'deltas', None)}")
    if cfg.d != 2 * cfg.d_vue or cfg.J != 2:
        raise GardeArret(f"configuration : d = 2 × d_vue et J = 2 exigés (d = {cfg.d}, d_vue = {cfg.d_vue}, J = {cfg.J})")
    if not 0 < cfg.R_min <= cfg.R_max or not cfg.R_min > max(cfg.deltas):
        raise GardeArret("configuration : rayons des modes invalides (0 < R_min ≤ R_max, R_min > δ max)")
    if not 0 < cfg.gamma_min_deg <= cfg.gamma_max_deg < 90:
        raise GardeArret("configuration : angle des témoins hors de ]0° ; 90°[")
    if not 0 < cfg.alpha < 0.5 or not 0 < cfg.theta_couverture < 1:
        raise GardeArret("configuration : α ou θ* hors de leur domaine")
    if cfg.unites_Bp < 2:
        raise GardeArret(f"configuration : B′ sans moniteurs non linéaires (unites_Bp = {cfg.unites_Bp})")
    entiers = ("T", "n_propre_entr", "n_attaque_entr", "n_cal", "n_fpr", "n_eval", "n_mc", "n_mc_final", "departs",
               "departs_final", "departs_renforce", "iter_max", "iter_renforce", "departs_entr", "iter_entr",
               "n_instances", "grille_exacte", "audit_departs", "audit_n_mc", "audit_iter", "audit_es_generations",
               "audit_es_lambda", "L_max", "n_configs", "grille_partage", "grille_x")
    if any(getattr(cfg, k) < 1 for k in entiers) or cfg.T < 4:
        raise GardeArret("configuration : effectif non positif (ou T < 4)")
    if not (0 < cfg.Ra_min <= cfg.Ra_max and 0 < cfg.sD_min <= cfg.sD_max and 0 <= cfg.kappa_min <= cfg.kappa_max
            and 0 <= cfg.beta0_min <= cfg.beta0_max):
        raise GardeArret("configuration : bornes du générateur de Q3b invalides")
    return cfg


# =================================================================================================================
# Graines, racines et autorisation de décision
# =================================================================================================================
_AUTORISATION_DECISION: dict = {"prereg_sha256": None}


def gen(racine: int, *cle: int) -> np.random.Generator:
    """Générateur dérivé (R9). Garde : une racine de décision exige l'autorisation par préenregistrement scellé."""
    exiger_numpy_minimal()
    if int(racine) in RACINES_DECISION and _AUTORISATION_DECISION["prereg_sha256"] is None:
        raise GardeArret(f"racine de décision {racine} sans autorisation : préenregistrement scellé exigé")
    return np.random.default_rng(np.random.SeedSequence(entropy=int(racine), spawn_key=tuple(int(c) for c in cle)))


def exiger_racine_essai(racine: int) -> None:
    """Garde : hors décision, ni racine de décision, ni racine déjà employée, ni plage du pilote b4, et seulement la
    plage de l'extension (R-747)."""
    r = int(racine)
    if r in RACINES_DECISION:
        raise GardeArret(f"racine {r} réservée à la décision de l'extension : interdite hors décision")
    if r in RACINES_DEJA_EMPLOYEES:
        raise GardeArret(f"racine {r} déjà employée dans l'arène (décision principale, essais v1 à v3 ou "
                         "contre-lectures) : interdite")
    if PLAGE_B4[0] <= r <= PLAGE_B4[1]:
        raise GardeArret(f"racine {r} dans la plage du pilote b4 (20264001–20264999) : interdite")
    if not PLAGE_EXTENSION[0] <= r <= PLAGE_EXTENSION[1]:
        raise GardeArret(f"racine {r} hors de la plage de l'extension (20265001–20265999) : interdite")


def empreinte_fichier(chemin: str | Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


DEBUT_CONFIG = "<!-- configuration-canonique-debut -->"
FIN_CONFIG = "<!-- configuration-canonique-fin -->"


def bloc_identite(cfg: Config) -> str:
    import scipy

    lignes = [f"- Identifiant : {IDENTIFIANT_PREREG}",
              f"- Racines de décision : RACINE_Q3 = {RACINE_Q3} ; RACINE_PRIX = {RACINE_PRIX}",
              f"- Code : `{Path(__file__).name}` — {empreinte_fichier(__file__)}",
              f"- Configuration (empreinte de la forme canonique) : {cfg.empreinte()}"]
    for f in FICHIERS_BIBLIOTHEQUE:
        lignes.append(f"- Bibliothèque `{f}` — {empreinte_fichier(DEPOT / f)}")
    lignes.append(f"- Versions : numpy {np.__version__} ; scipy {scipy.__version__} ; Python {sys.version.split()[0]}")
    lignes += ["", DEBUT_CONFIG, "```json", json.dumps(asdict(cfg), indent=1, sort_keys=True, ensure_ascii=False),
               "```", FIN_CONFIG]
    return "\n".join(lignes)


def extraire_configuration(texte: str) -> dict:
    m = re.search(re.escape(DEBUT_CONFIG) + r"\s*```json\s*(.*?)\s*```\s*" + re.escape(FIN_CONFIG), texte, re.S)
    if not m:
        raise GardeArret("préenregistrement : bloc de configuration canonique absent")
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        raise GardeArret(f"préenregistrement : bloc de configuration illisible ({e})") from None


def comparer_configuration(texte_cfg: dict, cfg: Config) -> list[str]:
    code = json.loads(json.dumps(asdict(cfg)))
    ecarts = [f"{k} absent du texte" for k in sorted(set(code) - set(texte_cfg))]
    ecarts += [f"{k} absent du code" for k in sorted(set(texte_cfg) - set(code))]
    ecarts += [f"{k} : texte {texte_cfg[k]!r} ≠ code {code[k]!r}" for k in sorted(set(code) & set(texte_cfg))
               if texte_cfg[k] != code[k]]
    return ecarts


def exiger_identite_prereg(texte: str, cfg: Config, instances: str | None = None, configs: str | None = None) -> None:
    """Garde : préenregistrement de cette extension, racines, configuration champ à champ, empreintes, versions,
    effectifs."""
    import scipy

    if IDENTIFIANT_PREREG not in texte:
        raise GardeArret(f"préenregistrement sans l'identifiant {IDENTIFIANT_PREREG}")
    for nom, val in (("RACINE_Q3", RACINE_Q3), ("RACINE_PRIX", RACINE_PRIX)):
        if not re.search(rf"\b{nom}\s*=\s*{val}\b", texte):
            raise GardeArret(f"préenregistrement : {nom} = {val} absent ou différent du code")
    ecarts = comparer_configuration(extraire_configuration(texte), cfg)
    if ecarts:
        raise GardeArret("préenregistrement : configuration différente du code : " + " ; ".join(ecarts))
    if not re.search(rf"\b{cfg.empreinte()}\b", texte):
        raise GardeArret("préenregistrement : empreinte de la configuration du code absente")
    if not re.search(rf"\b{empreinte_fichier(__file__)}\b", texte):
        raise GardeArret("préenregistrement : empreinte du fichier de code exécuté absente (code modifié après gel ?)")
    for f in FICHIERS_BIBLIOTHEQUE:
        if not re.search(rf"\b{empreinte_fichier(DEPOT / f)}\b", texte):
            raise GardeArret(f"préenregistrement : empreinte de {f} absente (bibliothèque modifiée après gel ?)")
    for nom, v in (("numpy", np.__version__), ("scipy", scipy.__version__)):
        if not re.search(rf"\b{nom} {re.escape(v)}(?![0-9.])", texte):
            raise GardeArret(f"préenregistrement : version {nom} {v} du processus absente du texte")
    if instances is not None and instances != f"0:{cfg.n_instances}":
        raise GardeArret(f"--instances {instances} ≠ 0:{cfg.n_instances} (configuration gelée)")
    if configs is not None and configs != f"0:{cfg.n_configs}":
        raise GardeArret(f"--configs {configs} ≠ 0:{cfg.n_configs} (configuration gelée)")


def exiger_run_principal(depot: str | Path, run_id: str) -> dict:
    """Garde : le calcul décisif de l'extension vient APRÈS celui du pilote principal. Exige l'analyse scellée du run de
    décision de l'arène principale (`diag/<run>/analyse-arene.json`, chaîne d'empreintes vérifiée), un manifeste
    décisif, et la racine de décision principale dans sa configuration."""
    from controle_ia import manifeste as man

    chemin = Path(depot) / "diag" / str(run_id) / "analyse-arene.json"
    if not chemin.exists():
        raise GardeArret(f"run principal {run_id} : analyse scellée absente ({chemin}) — l'extension attend le calcul "
                         "décisif du pilote principal")
    corps = man.verifier_resultat(depot, chemin)
    m, _ = man.lire_manifeste(Path(depot) / "runs" / corps["run_id"] / "manifeste.json")
    if not m.get("decisif") or (m.get("config") or {}).get("racine") != RACINE_PRINCIPALE:
        raise GardeArret(f"run principal {run_id} : manifeste non décisif ou racine ≠ {RACINE_PRINCIPALE}")
    return corps


def autoriser_decision(chemin: str | Path, cfg: Config, instances=None, configs=None) -> str:
    from controle_ia.prereg import exiger_prereg_scelle

    sha = exiger_prereg_scelle(chemin)
    exiger_identite_prereg(Path(chemin).read_text(encoding="utf-8"), cfg, instances, configs)
    _AUTORISATION_DECISION["prereg_sha256"] = sha
    return sha


# =================================================================================================================
# Familles de lois (générateur) et couche exacte
# =================================================================================================================
@dataclass
class Famille:
    nom: str
    centres: np.ndarray        # (J, d)
    libres: tuple              # par mode : indices des coordonnées que l'attaquant peut modifier
    regime: str                # "champ" ou "vues"
    vues: tuple                # indices de chaque vue (régime vues ; en champ complet : une seule « vue » = tout)


def _unitaire(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def generer_familles(instance: int, racine: int, cfg: Config) -> dict:
    """Quatre familles appariées (mêmes rayons R₁, R₂) ; ordre de tirage fixé (indépendant des familles demandées)."""
    g = gen(racine, 0, 0, instance, COMMUN, 0, ROLE_FAMILLE)
    d, dv = cfg.d, cfg.d_vue
    R = g.uniform(cfg.R_min, cfg.R_max, size=2)
    gam = np.deg2rad(g.uniform(cfg.gamma_min_deg, cfg.gamma_max_deg))
    u = _unitaire(g.standard_normal(d))
    u1 = _unitaire(g.standard_normal(d))
    v = g.standard_normal(d)
    v = _unitaire(v - (v @ u1) * u1)
    u2 = np.cos(gam) * u1 + np.sin(gam) * v
    w1 = _unitaire(g.standard_normal(dv))
    w2 = _unitaire(g.standard_normal(dv))
    y = g.standard_normal(dv)
    y = _unitaire(y - (y @ w1) * w1)
    w1b = np.cos(gam) * w1 + np.sin(gam) * y
    tout = tuple(range(d))
    v1, v2 = tuple(range(dv)), tuple(range(dv, d))
    z = np.zeros(dv)
    return {
        "N2": Famille("N2", np.stack([R[0] * u, -R[1] * u]), (tout, tout), "champ", (tout,)),
        "C2": Famille("C2", np.stack([R[0] * u1, R[1] * u2]), (tout, tout), "champ", (tout,)),
        "NV": Famille("NV", np.stack([np.concatenate([R[0] * w1, z]), np.concatenate([z, R[1] * w2])]), (v1, v2),
                      "vues", (v1, v2)),
        "CV": Famille("CV", np.stack([np.concatenate([R[0] * w1, z]), np.concatenate([R[1] * w1b, z])]), (v1, v1),
                      "vues", (v1, v2)),
    }


def _z(cfg: Config) -> float:
    return float(ndtri(1 - cfg.alpha))


def _phi(x):
    return ndtr(x)


def _maximiser_1d(f, a: float, b: float, n: int) -> tuple[float, float]:
    """Maximum d'une fonction scalaire régulière sur [a, b] : grille de n points puis affinage borné autour du meilleur
    point. Renvoie (argmax, max) ; l'affinage ne peut que relever la valeur de grille (garde)."""
    xs = np.linspace(a, b, n)
    vals = np.array([f(x) for x in xs])
    i = int(np.argmax(vals))
    lo, hi = xs[max(i - 1, 0)], xs[min(i + 1, n - 1)]
    if hi > lo:
        r = minimize_scalar(lambda x: -f(x), bounds=(lo, hi), method="bounded", options={"xatol": 1e-12})
        if -r.fun > vals[i]:
            return float(r.x), float(-r.fun)
    return float(xs[i]), float(vals[i])


def resoudre_jeu(G: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Jeu à somme nulle (lignes = moniteurs, colonnes = attaques). Recopié de la v3 (mêmes gardes)."""
    G = np.asarray(G, float)
    if G.ndim != 2 or not np.all(np.isfinite(G)) or np.any(G < 0) or np.any(G > 1):
        raise GardeArret("matrice de gains invalide (non finie ou hors [0, 1])")
    ni, nj = G.shape
    c = np.zeros(ni + 1)
    c[-1] = -1
    r1 = linprog(c, A_ub=np.hstack([-G.T, np.ones((nj, 1))]), b_ub=np.zeros(nj),
                 A_eq=np.hstack([np.ones((1, ni)), np.zeros((1, 1))]), b_eq=[1],
                 bounds=[(0, None)] * ni + [(None, None)], method="highs")
    c2 = np.zeros(nj + 1)
    c2[-1] = 1
    r2 = linprog(c2, A_ub=np.hstack([G, -np.ones((ni, 1))]), b_ub=np.zeros(ni),
                 A_eq=np.hstack([np.ones((1, nj)), np.zeros((1, 1))]), b_eq=[1],
                 bounds=[(0, None)] * nj + [(None, None)], method="highs")
    if r1.status != 0 or r2.status != 0:
        raise GardeArret(f"programme linéaire non résolu ({r1.message} ; {r2.message})")
    v, u = -r1.fun, r2.fun
    if abs(v - u) > 1e-7:
        raise GardeArret(f"valeurs primale et duale du jeu différentes : {v} ≠ {u}")
    return exiger_poids(r1.x[:ni]), exiger_poids(r2.x[:nj]), float(v)


def exiger_poids(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, float)
    if not np.all(np.isfinite(p)) or np.any(p < -1e-9) or abs(p.sum() - 1) > 1e-6:
        raise GardeArret(f"poids de mélange invalides : {p}")
    p = np.clip(p, 0, None)
    return p / p.sum()


def _union_deux(det1, det2, alpha: float, n: int, partage: str):
    """Union de deux moniteurs au taux total α, partage optimisé sur une grille puis affiné. `partage` : « disjoint »
    (demi-espaces opposés : α₁ + α₂ = α) ou « independant » (vues indépendantes : (1 − α₁)(1 − α₂) = 1 − α).
    det1(t1, t2), det2(t1, t2) : détections au pire point de chaque mode. Renvoie (V_union, α₁*)."""
    def seuils(a1):
        a2 = alpha - a1 if partage == "disjoint" else 1 - (1 - alpha) / (1 - a1)
        return float(ndtri(1 - a1)), float(ndtri(1 - a2))

    def f(a1):
        t1, t2 = seuils(a1)
        return min(det1(t1, t2), det2(t1, t2))
    eps = alpha * 1e-6
    a1, v = _maximiser_1d(f, eps, alpha - eps, n)
    return v, a1


def exact_N2(fam: Famille, delta: float, cfg: Config) -> dict:
    """Couche exacte, N2, classe linéaire en champ complet. Certificat : V_pur = Φ(−δ − z) (pour tout w unitaire, le
    minimum sur la famille de w·μ est au plus −δ). Mélange : jeu restreint au défenseur ±u, meilleure réponse continue de
    l'attaquant ; selle vérifiée par deux recherches à une dimension. Union : +u et −u au taux total α."""
    z, n = _z(cfg), cfg.grille_exacte
    c1, c2 = fam.centres
    R1, R2 = float(np.linalg.norm(c1)), float(np.linalg.norm(c2))
    u = c1 / R1
    if not np.allclose(c2, -R2 * u, atol=1e-9) or min(R1, R2) <= delta:
        raise GardeArret("couche exacte N2 : centres non opposés ou boule contenant l'origine")
    r1, r2 = R1 - delta, R2 - delta
    a1, a2, b1, b2 = _phi(r1 - z), _phi(r2 - z), _phi(-r1 - z), _phi(-r2 - z)
    M = np.array([[a1, b2], [b1, a2]])
    p, q, V = resoudre_jeu(M)
    s1, s2 = np.linspace(r1, R1 + delta, n), np.linspace(r2, R2 + delta, n)
    h1 = p[0] * _phi(s1 - z) + p[1] * _phi(-s1 - z)
    h2 = p[0] * _phi(-s2 - z) + p[1] * _phi(s2 - z)
    att_ok = h1.min() >= h1[0] - cfg.tol_selle and h2.min() >= h2[0] - cfg.tol_selle
    cs = np.linspace(-1, 1, n)
    f = q[0] * _phi(r1 * cs - z) + q[1] * _phi(-r2 * cs - z)
    lip = 0.4 * max(r1, r2) * (cs[1] - cs[0])
    def_ok = f.max() <= V + lip + cfg.tol_selle
    if not (att_ok and def_ok):
        raise GardeArret("couche exacte N2 : selle du jeu restreint non vérifiée")

    def d1(t1, t2):
        return float(_phi(r1 - t1) + _phi(-r1 - t2))

    def d2(t1, t2):
        return float(_phi(r2 - t2) + _phi(-r2 - t1))
    Vu, a1s = _union_deux(d1, d2, cfg.alpha, 2001, "disjoint")
    V_pur = float(_phi(-delta - z))
    return {"V_pur": V_pur, "V_mel": V, "V_union": Vu, "p": p.tolist(), "q": q.tolist(), "alpha1_union": a1s,
            "VT_exact": V - V_pur, "UM_exact": Vu - V, "selle_certifiee": True, "classe": "linéaire, champ complet"}


def exact_NV(fam: Famille, delta: float, cfg: Config) -> dict:
    """Couche exacte, NV, toute classe « une vue » (linéaire ou maxout de n'importe quelle taille). Certificat :
    V_pur = α exactement (la loi marginale de la vue non déplacée est la loi propre). Mélange : jeu 2 × 2 [[a₁, α],
    [α, a₂]] (dans une vue, le meilleur détecteur contre un seul mode est linéaire, Neyman–Pearson). Union : un
    moniteur par vue, vues indépendantes."""
    z, al = _z(cfg), cfg.alpha
    c1, c2 = fam.centres
    v1, v2 = fam.vues
    if np.any(c1[list(v2)] != 0) or np.any(c2[list(v1)] != 0) or fam.libres != (v1, v2):
        raise GardeArret("couche exacte NV : un mode déplace la vue de l'autre")
    R1, R2 = float(np.linalg.norm(c1)), float(np.linalg.norm(c2))
    if min(R1, R2) <= delta:
        raise GardeArret("couche exacte NV : boule contenant l'origine de sa vue")
    r1, r2 = R1 - delta, R2 - delta
    a1, a2 = float(_phi(r1 - z)), float(_phi(r2 - z))
    p, q, V = resoudre_jeu(np.array([[a1, al], [al, a2]]))
    ferme = (a1 * a2 - al ** 2) / (a1 + a2 - 2 * al)
    if abs(V - ferme) > 1e-9:
        raise GardeArret("couche exacte NV : valeur du jeu 2 × 2 ≠ formule fermée")

    def d1(t1, t2):
        return float(1 - _phi(t1 - r1) * _phi(t2))

    def d2(t1, t2):
        return float(1 - _phi(t1) * _phi(t2 - r2))
    Vu, a1s = _union_deux(d1, d2, al, 2001, "independant")
    return {"V_pur": al, "V_mel": V, "V_union": Vu, "p": p.tolist(), "q": q.tolist(), "alpha1_union": a1s,
            "VT_exact": V - al, "UM_exact": Vu - V, "selle_certifiee": True, "classe": "toute classe « une vue »"}


def exact_couvrable(fam: Famille, delta: float, cfg: Config) -> dict:
    """Couche exacte, témoins C2 et CV, classe linéaire. V_pur = Φ(ρ* − δ − z), ρ* = distance de l'origine au segment
    des centres. Selle pure : l'attaquant mélange les deux pires points contre w* aux poids du point projeté ; le
    défenseur ne fait pas mieux (majorant sur tout le disque unité du plan des deux points, grille d'angles et marge de
    Lipschitz) ⇒ V_mél = V_pur, valeur du tirage exactement nulle. Sinon : « non certifiée » (comptée, jamais
    remplacée)."""
    z, n = _z(cfg), cfg.grille_exacte
    c1, c2 = fam.centres
    dd = c2 - c1
    lam = float(np.clip(-(c1 @ dd) / (dd @ dd), 0.0, 1.0))
    pp = c1 + lam * dd
    rho = float(np.linalg.norm(pp))
    if rho <= delta:
        raise GardeArret("couche exacte témoin : segment des centres trop proche de l'origine")
    w = pp / rho
    V_pur = float(_phi(rho - delta - z))
    mu = np.stack([c1 - delta * w, c2 - delta * w])
    q = np.array([1 - lam, lam])
    e2 = mu[0] - mu[1]
    e2 = e2 - (e2 @ w) * w
    if np.linalg.norm(e2) < 1e-12:
        e2 = np.zeros_like(w)
        e2[int(np.argmin(np.abs(w)))] = 1.0
        e2 = e2 - (e2 @ w) * w
    e2 = _unitaire(e2)
    ang = np.linspace(-np.pi, np.pi, n)
    E = np.outer(np.cos(ang), w) + np.outer(np.sin(ang), e2)       # directions unitaires du plan
    S = np.maximum(E @ mu.T, 0.0)
    UB = (_phi(S - z) * q).sum(1)
    lip = 0.4 * float(np.max(np.linalg.norm(mu, axis=1))) * (ang[1] - ang[0])
    certifie = bool(UB.max() <= V_pur + lip + cfg.tol_selle)
    return {"V_pur": V_pur, "V_mel": V_pur if certifie else None, "V_union": None, "rho": rho, "lambda": lam,
            "VT_exact": 0.0 if certifie else None, "UM_exact": None, "selle_certifiee": certifie,
            "classe": "linéaire (une vue en CV)"}


def couche_exacte(fam: Famille, delta: float, cfg: Config) -> dict:
    if fam.nom == "N2":
        ex = exact_N2(fam, delta, cfg)
    elif fam.nom == "NV":
        ex = exact_NV(fam, delta, cfg)
    elif fam.nom in ("C2", "CV"):
        ex = exact_couvrable(fam, delta, cfg)
    else:
        raise GardeArret(f"couche exacte : famille inconnue {fam.nom!r}")
    exiger_regime(fam.nom, ex, cfg)
    return ex


def exiger_regime(nom: str, ex: dict, cfg: Config) -> None:
    """Garde de régime : familles non couvrables — aucun moniteur seul de la classe n'atteint θ*, une union de deux
    l'atteint ; témoins — un moniteur seul l'atteint."""
    th = cfg.theta_couverture
    if nom in NON_COUVRABLES:
        if not (ex["V_pur"] < th and ex["V_union"] >= th):
            raise GardeArret(f"régime non couvrable non tenu ({nom}) : V_pur = {ex['V_pur']:.4f}, "
                             f"V_union = {ex['V_union']:.4f}, θ* = {th}")
    elif not ex["V_pur"] >= th:
        raise GardeArret(f"régime témoin non tenu ({nom}) : V_pur = {ex['V_pur']:.4f} < θ* = {th}")


# =================================================================================================================
# Moniteurs (recopiés de la v3 ; champ récepteur optionnel)
# =================================================================================================================
class Moniteur:
    """Score « maxout » : log-somme-exp de m scores linéaires (m = 1 : linéaire). Seuil t calibré à α sur le propre.
    `vue` : indices lus (None : champ complet) ; les poids hors de la vue sont nuls."""

    def __init__(self, W: np.ndarray, b: np.ndarray, vue=None):
        W = np.atleast_2d(np.asarray(W, float))
        b = np.atleast_1d(np.asarray(b, float))
        if not (np.all(np.isfinite(W)) and np.all(np.isfinite(b))):
            raise GardeArret("paramètres de moniteur non finis")
        self.W, self.b, self.vue = W, b, vue
        self.t = np.nan
        self.e = np.nan
        self._cache: dict = {}

    @property
    def m(self) -> int:
        return self.W.shape[0]

    @property
    def nb_parametres(self) -> int:
        lus = self.W.shape[1] if self.vue is None else len(self.vue)
        return int(self.m * (lus + 1))

    def score(self, X: np.ndarray) -> np.ndarray:
        a = X @ self.W.T + self.b
        return a[:, 0] if self.m == 1 else logsumexp(a, axis=1)

    def score_et_grad(self, X: np.ndarray):
        a = X @ self.W.T + self.b
        if self.m == 1:
            return a[:, 0], np.broadcast_to(self.W[0], X.shape)
        return logsumexp(a, axis=1), softmax(a, axis=1) @ self.W

    def calibrer(self, Xcal: np.ndarray, alpha: float) -> "Moniteur":
        s = self.score(Xcal)
        if not np.all(np.isfinite(s)):
            raise GardeArret("scores propres non finis")
        self.t = float(np.quantile(s, 1 - alpha, method="higher"))
        self.e = float(np.std(s))
        if not self.e > 0:
            raise GardeArret("score propre de variance nulle : seuil non calibrable")
        return self

    def detecte(self, X: np.ndarray) -> np.ndarray:
        if not np.isfinite(self.t):
            raise GardeArret("moniteur non calibré")
        return self.score(X) > self.t

    def taux_cache(self, cle, X_fournisseur) -> float:
        if cle not in self._cache:
            self._cache[cle] = float(np.mean(self.detecte(X_fournisseur())))
        return self._cache[cle]


def _groupes(tailles: np.ndarray):
    bornes = np.concatenate([[0], np.cumsum(tailles)])
    out = []
    for u in sorted(set(tailles.tolist())):
        ids = np.flatnonzero(tailles == u)
        out.append((ids, np.stack([np.arange(bornes[i], bornes[i + 1]) for i in ids])))
    return out


def _scores_groupes(A: np.ndarray, groupes, M: int, internes: bool):
    """Scores log-somme-exp par moniteur (unités empilées) et, si demandé, poids softmax internes par unité."""
    S = np.empty((A.shape[0], M))
    S_int = np.ones_like(A) if internes else None
    for ids, unites in groupes:
        Ag = A[:, unites]
        mx = Ag.max(axis=2, keepdims=True)
        ex = np.exp(Ag - mx)
        som = ex.sum(axis=2, keepdims=True)
        S[:, ids] = (mx + np.log(som))[:, :, 0]
        if internes:
            S_int[:, unites.ravel()] = (ex / som).reshape(A.shape[0], -1)
    return S, S_int


class MoniteurOu(Moniteur):
    """« Ou » déterministe de moniteurs (linéaires ou maxout, d'une vue ou non) : score log-somme-exp_i(λ z_i),
    z_i = (s_i − μ_i)/σ_i standardisé sur le propre de calibration ; seuil recalibré à α. Recopié de la v3."""

    def __init__(self, membres: list, Xcal: np.ndarray, lam: float):
        if not membres:
            raise GardeArret("« ou » composite : aucun moniteur")
        self.membres, self.lam = list(membres), float(lam)
        mu, sd = [], []
        for mon in self.membres:
            s = mon.score(Xcal)
            a, b = float(np.mean(s)), float(np.std(s))
            if not (np.isfinite(a) and b > 1e-12):
                raise GardeArret("« ou » composite : score propre de variance nulle ou non fini")
            mu.append(a)
            sd.append(b)
        self.W = np.vstack([m.W for m in self.membres])
        self.b = np.concatenate([m.b for m in self.membres])
        self.tailles = np.array([m.m for m in self.membres])
        self.grp = _groupes(self.tailles)
        self.mu_a, self.sd_a = np.asarray(mu), np.asarray(sd)
        vues = {m.vue for m in self.membres}
        self.vue = next(iter(vues)) if len(vues) == 1 else None
        self.t = np.nan
        self.e = np.nan
        self._cache = {}

    @property
    def nb_parametres(self) -> int:
        return int(sum(m.nb_parametres for m in self.membres))

    def _zs(self, X, internes=False):
        S, S_int = _scores_groupes(X @ self.W.T + self.b, self.grp, len(self.membres), internes)
        return self.lam * (S - self.mu_a) / self.sd_a, S_int

    def score(self, X):
        return logsumexp(self._zs(X)[0], axis=1)

    def score_et_grad(self, X):
        zz, S_int = self._zs(X, True)
        s = logsumexp(zz, axis=1)
        Sz = softmax(zz, axis=1)
        return s, (S_int * np.repeat(Sz * (self.lam / self.sd_a), self.tailles, axis=1)) @ self.W


class Defense:
    """Défense mixte {(moniteur, poids)} ; évaluation empilée (un seul produit matriciel) si tous les moniteurs actifs
    sont des `Moniteur` simples."""

    def __init__(self, items):
        self.items = [(m, float(p)) for m, p in items]
        self.actifs = [(m, p) for m, p in self.items if p > 0]
        if not self.actifs:
            raise GardeArret("défense vide : aucun moniteur de poids positif")
        self.empile = all(type(m) is Moniteur for m, _ in self.actifs)
        if self.empile:
            ms = [m for m, _ in self.actifs]
            self.W = np.vstack([m.W for m in ms])
            self.b = np.concatenate([m.b for m in ms])
            self.t = np.array([m.t for m in ms])
            self.e = np.array([m.e for m in ms])
            self.p = np.array([p for _, p in self.actifs])
            self.tailles = np.array([m.m for m in ms])
            self.grp = _groupes(self.tailles)
            self.unite_mon = np.repeat(np.arange(len(ms)), self.tailles)

    def taux(self, X: np.ndarray) -> float:
        if self.empile:
            S, _ = _scores_groupes(X @ self.W.T + self.b, self.grp, len(self.actifs), False)
            return float(np.sum(self.p * np.mean(S > self.t, axis=0)))
        return float(sum(p * np.mean(m.detecte(X)) for m, p in self.actifs))

    def lisse_et_grad(self, X: np.ndarray, tau: float) -> tuple[float, np.ndarray]:
        """Taux lissé et son gradient par rapport à la moyenne μ (X = μ + Z, échantillons Z fixés)."""
        n = X.shape[0]
        if self.empile:
            S, S_int = _scores_groupes(X @ self.W.T + self.b, self.grp, len(self.actifs), True)
            sg = expit((S - self.t) / (tau * self.e))
            total = float(np.sum(self.p * sg.mean(0)))
            ds = self.p * sg * (1 - sg) / (tau * self.e) / n
            coef = np.sum(ds[:, self.unite_mon] * S_int, axis=0)
            return total, coef @ self.W
        total, g = 0.0, np.zeros(X.shape[1])
        for m, p in self.actifs:
            s, gr = m.score_et_grad(X)
            sg = expit((s - m.t) / (tau * m.e))
            total += p * float(sg.mean())
            g += ((p * sg * (1 - sg) / (tau * m.e) / n)[:, None] * gr).sum(0)
        return total, g


# =================================================================================================================
# Oracle du défenseur (recopié de la v3 : objectif « détection » lissé, départs logistique puis directions)
# =================================================================================================================
def _somme_ponderee(X, S, w):
    G = w[:, None] * S
    return np.concatenate([(G.T @ X).ravel(), G.sum(0)])


def _scores(p, X, m):
    d = X.shape[1]
    A = X @ p[: m * d].reshape(m, d).T + p[m * d:]
    if m == 1:
        return A[:, 0], np.ones((len(X), 1))
    return logsumexp(A, axis=1), softmax(A, axis=1)


def _logistique(Xp, Xa, m, cfg: Config, x0):
    X = np.vstack([Xp, Xa])
    y = np.concatenate([-np.ones(len(Xp)), np.ones(len(Xa))])
    n, d = X.shape

    def f(p):
        s, S = _scores(p, X, m)
        ys = y * s
        W = p[: m * d]
        g = _somme_ponderee(X, S, -y * expit(-ys) / n)
        g[: m * d] += 2 * cfg.l2 * W
        return np.mean(np.logaddexp(0.0, -ys)) + cfg.l2 * np.sum(W * W), g

    return minimize(f, x0, jac=True, method="L-BFGS-B", options={"maxiter": cfg.iter_entr})


def objectif_detection(p, Xp, Xa, m, cfg: Config):
    z = float(ndtri(1 - cfg.alpha))
    sp, Sp = _scores(p, Xp, m)
    sa, Sa = _scores(p, Xa, m)
    moy, et = sp.mean(), sp.std()
    if not et > 0:
        return 0.0, np.zeros_like(p)
    u = (sa - moy) / et - z
    sg = expit(u / cfg.tau)
    J = sg.mean()
    ga = sg * (1 - sg) / cfg.tau / len(Xa)
    d_sa = _somme_ponderee(Xa, Sa, ga)
    d_moy = _somme_ponderee(Xp, Sp, np.full(len(Xp), 1.0 / len(Xp)))
    d_et = _somme_ponderee(Xp, Sp, (sp - moy) / (len(Xp) * et))
    dJ = (d_sa - ga.sum() * d_moy) / et - (np.sum(ga * (sa - moy)) / et ** 2) * d_et
    return -J, -dJ


def entrainer(Xp, Xa, m, cfg: Config, rng_init, directions=()):
    """Entraîne un moniteur à m unités sur les colonnes données. Renvoie (W, b, convergé, objectif)."""
    d = Xp.shape[1]
    if m == 1:
        x0 = np.zeros(d + 1)
    else:
        if rng_init is None:
            raise GardeArret("maxout sans graine d'initialisation")
        idx = rng_init.permutation(len(Xa))
        W0 = np.stack([0.5 * Xa[part].mean(0) for part in np.array_split(idx, m)])
        x0 = np.concatenate([W0.ravel(), np.zeros(m)])
    res = _logistique(Xp, Xa, m, cfg, x0)
    if not np.all(np.isfinite(res.x)) or not np.isfinite(res.fun):
        raise GardeArret("entraînement logistique : paramètres ou perte non finis")
    dirs = [np.asarray(v, float) for v in directions]
    departs = [res.x]
    if m == 1:
        departs += [np.concatenate([v, [0.0]]) for v in dirs[: max(cfg.departs_entr - 1, 0)]]
    elif dirs:
        departs.append(np.concatenate([np.stack([dirs[j % len(dirs)] for j in range(m)]).ravel(), np.zeros(m)]))
    meilleur = None
    for x in departs:
        r = minimize(objectif_detection, x, args=(Xp, Xa, m, cfg), jac=True, method="L-BFGS-B",
                     options={"maxiter": cfg.iter_entr})
        if not np.all(np.isfinite(r.x)) or not np.isfinite(r.fun):
            raise GardeArret("entraînement par détection : paramètres ou objectif non finis")
        if meilleur is None or r.fun < meilleur.fun:
            meilleur = r
    return meilleur.x[: m * d].reshape(m, d), meilleur.x[m * d:], bool(meilleur.success), float(meilleur.fun)


# =================================================================================================================
# Attaquant : meilleure réponse dans la réunion des boules de modes
# =================================================================================================================
def exiger_admissible(mu: np.ndarray, fam: Famille, j: int, delta: float) -> None:
    if not np.all(np.isfinite(mu)):
        raise GardeArret("loi d'attaque non finie")
    fixes = [k for k in range(len(mu)) if k not in fam.libres[j]]
    if fixes and np.any(mu[fixes] != fam.centres[j][fixes]):
        raise GardeArret("loi d'attaque : coordonnée non libre modifiée")
    if np.linalg.norm(mu - fam.centres[j]) > delta * (1 + 1e-9) + 1e-12:
        raise GardeArret(f"loi d'attaque hors de la boule du mode {j} (rayon δ = {delta})")


def _projeter(y, c, delta):
    v = y - c
    n = np.linalg.norm(v)
    return c + v * (delta / n) if n > delta else y


def meilleure_reponse(defense: Defense, fam: Famille, delta: float, cfg: Config, rng_mc, rng_departs,
                      departs_suppl=(), n_departs=None, n_mc=None, iter_max=None):
    """Meilleure réponse approchée : pour chaque mode, SLSQP sur les coordonnées libres, contrainte ‖μ − c_j‖ ≤ δ,
    départs : vers l'origine, contre chaque moniteur actif (gradient du score au centre), tirés dans la boule, attaques
    passées du mode ; sélection par taux dur puis lissé ; meilleur mode. Statuts et départs non finis comptés."""
    n_departs = cfg.departs if n_departs is None else n_departs
    iter_max = cfg.iter_max if iter_max is None else iter_max
    Z = rng_mc.standard_normal((cfg.n_mc if n_mc is None else n_mc, cfg.d))
    meilleur, non_finis, total, statuts, it_max = None, 0, 0, Counter(), 0
    moniteurs = sorted(defense.actifs, key=lambda mp: -mp[1])[:10]
    for j in range(cfg.J):
        idx = np.array(fam.libres[j])
        c = fam.centres[j]
        cl = c[idx]
        starts = []
        nc = np.linalg.norm(cl)
        starts.append(cl * (1 - min(delta / nc, 1.0)) if nc > 0 else cl.copy())
        for m, _ in moniteurs:
            _, gr = m.score_et_grad(c[None, :])
            gl = np.asarray(gr)[0, idx]
            if np.linalg.norm(gl) > 1e-12:
                starts.append(cl - delta * gl / np.linalg.norm(gl))
        for _ in range(n_departs):
            v = rng_departs.standard_normal(len(idx))
            starts.append(cl + v * delta * rng_departs.uniform(0.5, 1.0) / np.linalg.norm(v))
        starts += [_projeter(np.asarray(a, float)[idx], cl, delta) for a, jj in departs_suppl if jj == j]

        def complet(y):
            mu = c.copy()
            mu[idx] = y
            return mu

        def f(y):
            v, g = defense.lisse_et_grad(complet(y) + Z, cfg.tau)
            return v, g[idx]
        contrainte = {"type": "ineq", "fun": lambda y: delta ** 2 - np.sum((y - cl) ** 2),
                      "jac": lambda y: -2 * (y - cl)}
        for y0 in starts:
            total += 1
            r = minimize(f, y0, jac=True, method="SLSQP", constraints=[contrainte],
                         options={"maxiter": iter_max, "ftol": 1e-9})
            statuts[int(r.status)] += 1
            it_max = max(it_max, int(getattr(r, "nit", 0)))
            if not np.all(np.isfinite(r.x)):
                non_finis += 1
                continue
            mu = complet(_projeter(r.x, cl, delta))
            cand = (defense.taux(mu + Z), defense.lisse_et_grad(mu + Z, cfg.tau)[0], mu, j)
            if meilleur is None or cand[:2] < meilleur[:2]:
                meilleur = cand
    if meilleur is None:
        raise GardeArret("meilleure réponse : aucun départ n'a donné de point fini")
    exiger_admissible(meilleur[2], fam, meilleur[3], delta)
    return meilleur[2], meilleur[3], {"departs": total, "non_finis": non_finis, "iter_max": it_max,
                                      "limite_iter": iter_max, "statuts": {str(k): v for k, v in statuts.items()}}


def exiger_departs_finis(non_finis: int, total: int, cfg: Config) -> None:
    if total and non_finis / total > cfg.taux_departs_non_finis_max:
        raise GardeArret(f"départs de l'attaquant au point non fini : {non_finis}/{total} > "
                         f"{cfg.taux_departs_non_finis_max}")


# =================================================================================================================
# Une tâche = (famille, δ, instance)
# =================================================================================================================
class Contexte:
    def __init__(self, nom_famille: str, instance: int, code_delta: int, racine: int, cfg: Config):
        if nom_famille not in FAMILLES:
            raise GardeArret(f"contexte : famille inconnue {nom_famille!r}")
        self.cfg, self.i, self.cd, self.r = cfg, instance, code_delta, racine
        self.cf = FAMILLES[nom_famille]
        self.fam = generer_familles(instance, racine, cfg)[nom_famille]
        self.delta = cfg.deltas[code_delta - 1]
        self.Xcal = self.g(COMMUN, 0, ROLE_CAL).standard_normal((cfg.n_cal, cfg.d))
        self.Xfpr = self.g(COMMUN, 0, ROLE_FPR).standard_normal((cfg.n_fpr, cfg.d))
        self.nonconv = self.entr = 0
        self.att = {"departs": 0, "non_finis": 0, "a_la_limite": 0, "statuts": Counter()}

    def g(self, bras, tour, role, *extra):
        return gen(self.r, self.cf, self.cd, self.i, bras, tour, role, *extra)

    def X_centre(self, j: int) -> np.ndarray:
        return self.fam.centres[j] + self.g(COMMUN, 0, ROLE_EVAL, j).standard_normal((self.cfg.n_eval, self.cfg.d))

    def meilleure_reponse(self, defense, rng_mc, rng_dep, **kw):
        mu, j, info = meilleure_reponse(defense, self.fam, self.delta, self.cfg, rng_mc, rng_dep, **kw)
        self.att["departs"] += info["departs"]
        self.att["non_finis"] += info["non_finis"]
        self.att["a_la_limite"] += int(info["iter_max"] >= info["limite_iter"])
        self.att["statuts"].update({int(k): v for k, v in info["statuts"].items()})
        return mu, j, info

    def entrainer(self, bras: int, tour: int, attaques, q, m: int, une_vue: bool) -> Moniteur:
        """Moniteur entraîné sur le propre du tour (commun aux bras) contre le mélange q des attaques ; en régime « une
        vue », un moniteur par vue, le meilleur objectif d'entraînement est retenu (ordre des vues fixé)."""
        cfg = self.cfg
        q = exiger_poids(q)
        n = cfg.n_attaque_entr
        comptes = np.floor(q * n).astype(int)
        comptes[np.argsort(-(q * n - comptes), kind="stable")[: n - comptes.sum()]] += 1
        g = self.g(bras, tour, ROLE_ATTAQUE_ENTR)
        Xa = np.vstack([a + g.standard_normal((k, cfg.d)) for a, k in zip(attaques, comptes) if k > 0])
        Xp = self.g(COMMUN, tour, ROLE_PROPRE_ENTR).standard_normal((cfg.n_propre_entr, cfg.d))
        init = self.g(bras, tour, ROLE_INIT_MAXOUT) if m > 1 else None
        vues = self.fam.vues if une_vue else (tuple(range(cfg.d)),)
        meilleur = None
        for vue in vues:
            iv = list(vue)
            dirs = []
            for j in np.argsort(-q, kind="stable"):
                if q[j] > 0 and np.linalg.norm(attaques[j][iv]) > 1e-12:
                    dirs.append(attaques[j][iv] / np.linalg.norm(attaques[j][iv]))
            Wv, b, ok, fun = entrainer(Xp[:, iv], Xa[:, iv], m, cfg, init, dirs)
            if meilleur is None or fun < meilleur[3]:
                W = np.zeros((m, cfg.d))
                W[:, iv] = Wv
                meilleur = (W, b, ok, fun, vue if une_vue else None)
        self.entr += 1
        self.nonconv += (not meilleur[2])
        return Moniteur(meilleur[0], meilleur[1], meilleur[4]).calibrer(self.Xcal, cfg.alpha)

    def exiger_fpr(self, defense: Defense) -> float:
        f = defense.taux(self.Xfpr)
        if abs(f - self.cfg.alpha) > self.cfg.tol_fpr:
            raise GardeArret(f"taux de fausses alertes mesuré {f:.4f} hors de α ± {self.cfg.tol_fpr}")
        return f


def indicateurs_cycle(H: np.ndarray, iii: list, moyennes: list, modes: list) -> dict:
    """Condition d'application, comme la v3 (CM2-03, CM3-03) : I1 progrès ; I2 baisse de détection des attaques passées
    par le moniteur final (oubli ou saturation) ; rétention ; I3 retours (cosinus entre moyennes d'attaque ; valeur nulle
    0,7345 pour T = 8) ; I4 changements de mode (valeur nulle 0,5 pour deux modes équiprobables indépendants)."""
    T = H.shape[1]
    h = T // 2
    I1 = float(np.mean(iii[h:]) - np.mean(iii[:h]))
    I2 = float(np.mean([H[t, t - 1] - H[T, t - 1] for t in range(1, T)]))
    ret = {str(k): float(np.mean([H[t + k, t - 1] for t in range(1, T + 1) if t + k <= T])) for k in range(0, 4)}
    retours = []
    for t in range(3, T + 1):
        v = moyennes[t - 1]
        cs = [float(v @ moyennes[s - 1] / (np.linalg.norm(v) * np.linalg.norm(moyennes[s - 1]) + 1e-300))
              for s in range(1, t)]
        retours.append(max(cs[:-1]) > cs[-1])
    I4 = float(np.mean([modes[t] != modes[t - 1] for t in range(1, T)]))
    return {"I1_progres": I1, "I2_baisse": I2, "retention": ret, "I3_retours": float(np.mean(retours)),
            "I3_nul": I3_NUL_T8 if T == 8 else float(np.mean([(t - 2) / (t - 1) for t in range(3, T + 1)])),
            "I4_changements": I4, "I4_nul": 0.5, "H": [[float(x) for x in ligne] for ligne in H]}


def trajectoire(nom: str, ctx: Contexte, M0: Moniteur) -> dict:
    if nom not in TRAJECTOIRES:
        raise GardeArret(f"bras sans trajectoire : {nom!r}")
    cb, sorte, une_vue, unites = TRAJECTOIRES[nom]
    cfg, J = ctx.cfg, ctx.cfg.J
    melange = sorte == "melange"
    t0 = time.process_time()
    attaques = [c.copy() for c in ctx.fam.centres]
    modes = list(range(J))
    moniteurs, historique = [M0], [M0]
    cles = [("centre", j) for j in range(J)]
    eval_X = {("centre", j): (lambda j=j: ctx.X_centre(j)) for j in range(J)}
    G = np.array([[M0.taux_cache(k, eval_X[k]) for k in cles]]) if melange else None
    p = np.array([1.0])
    par_tour = {"iii": [], "mode": [], "poids_max": [], "cpu_s": []}

    def courante():
        if not melange:
            return [(moniteurs[-1], 1.0)]
        return list(zip(moniteurs, p))

    for t in range(1, cfg.T + 1):
        tt = time.process_time()
        if melange:
            p, _, _ = resoudre_jeu(G)
        D = Defense(courante())
        a, j, _ = ctx.meilleure_reponse(D, ctx.g(cb, t, ROLE_MC), ctx.g(cb, t, ROLE_DEPARTS),
                                        departs_suppl=list(zip(attaques[J:], modes[J:])))
        cle = ("eval", cb, t)
        eval_X[cle] = (lambda a=a, t=t: a + ctx.g(cb, t, ROLE_EVAL).standard_normal((cfg.n_eval, cfg.d)))
        par_tour["iii"].append(D.taux(eval_X[cle]()))
        par_tour["mode"].append(int(j))
        par_tour["poids_max"].append(float(max(w for _, w in D.items)))
        attaques.append(a)
        modes.append(int(j))
        cles.append(cle)
        if melange:
            G = np.hstack([G, np.array([[m.taux_cache(cle, eval_X[cle]) for m in moniteurs]]).T])
            _, q, _ = resoudre_jeu(G)
            mon = ctx.entrainer(cb, t, attaques, q, cfg.unites_Bp if unites == "Bp" else 1, une_vue)
            G = np.vstack([G, np.array([[mon.taux_cache(c, eval_X[c]) for c in cles]])])
        else:
            m_u = t + 1 if unites is None else unites
            mon = ctx.entrainer(cb, t, attaques, np.full(len(attaques), 1.0 / len(attaques)), m_u, une_vue)
        if sorte == "unique" and unites is None:
            moniteurs = [mon]
        else:
            moniteurs.append(mon)
        historique.append(mon)
        par_tour["cpu_s"].append(time.process_time() - tt)
        exiger_plafond(t0, cfg, f"bras {nom}, tour {t}")
    valeur = None
    if melange:
        p, _, valeur = resoudre_jeu(G)
    H = np.array([[mon.taux_cache(c, eval_X[c]) for c in cles[J:]] for mon in historique])
    return {"nom": nom, "moniteurs": moniteurs, "defense_finale": courante(), "attaques": attaques, "modes": modes,
            "par_tour": par_tour, "valeur_jeu_restreint": valeur,
            "cycle": indicateurs_cycle(H, par_tour["iii"], attaques[J:], modes[J:]),
            "cpu_trajectoire_s": time.process_time() - t0}


def defense_temoin(nom: str, etat: dict, ctx: Contexte) -> list:
    """PUR : moniteur de poids maximal (plus petit indice en cas d'égalité) déployé seul ; U : « ou » des moniteurs du
    support (poids > 10⁻⁶), recalibré à α (un seul moniteur au support : ce moniteur seul)."""
    if nom not in TEMOINS:
        raise GardeArret(f"témoin inconnu : {nom!r}")
    _, _, sorte = TEMOINS[nom]
    dfin = etat["defense_finale"]
    poids = np.array([w for _, w in dfin])
    if sorte == "pur":
        return [(dfin[int(np.argmax(poids))][0], 1.0)]
    support = [m for m, w in dfin if w > 1e-6]
    if len(support) == 1:
        return [(support[0], 1.0)]
    return [(MoniteurOu(support, ctx.Xcal, ctx.cfg.lambda_ou).calibrer(ctx.Xcal, ctx.cfg.alpha), 1.0)]


def phase_finale(dfin, ctx: Contexte, etat: dict, cb: int, rendre_attaques: bool = False):
    """Défense figée ; attaquant standard puis renforcé ; V = la plus basse des deux détections (échantillons frais).
    `cb` : code de graines (celui du bras source pour les témoins : nombres aléatoires communs)."""
    cfg, J = ctx.cfg, ctx.cfg.J
    tf = time.process_time()
    T1 = cfg.T + 1
    D = Defense(dfin)
    fpr = ctx.exiger_fpr(D)
    passes = list(zip(etat["attaques"][J:], etat["modes"][J:]))
    a1, j1, _ = ctx.meilleure_reponse(D, ctx.g(cb, T1, ROLE_FINAL, 1), ctx.g(cb, T1, ROLE_FINAL, 2),
                                      departs_suppl=passes, n_departs=cfg.departs_final, n_mc=cfg.n_mc_final)
    V1 = D.taux(a1 + ctx.g(cb, T1, ROLE_FINAL, 3).standard_normal((cfg.n_eval, cfg.d)))
    a2, j2, _ = ctx.meilleure_reponse(D, ctx.g(cb, T1, ROLE_FINAL, 4), ctx.g(cb, T1, ROLE_FINAL, 5),
                                      departs_suppl=passes + [(a1, j1)], n_departs=cfg.departs_renforce,
                                      n_mc=cfg.n_mc_final, iter_max=cfg.iter_renforce)
    V2 = D.taux(a2 + ctx.g(cb, T1, ROLE_FINAL, 6).standard_normal((cfg.n_eval, cfg.d)))
    poids = [w for _, w in D.items]
    sortie = {"V_final": min(V1, V2), "V_standard": V1, "V_renforce": V2, "fpr_final": fpr,
              "poids_finaux": [float(w) for w in poids], "support": int(sum(w > 1e-6 for w in poids)),
              "pur": bool(max(poids) >= 1 - 1e-9), "mode_final": int(j1 if V1 <= V2 else j2),
              "parametres_par_requete": int(max(m.nb_parametres for m, w in D.items if w > 0)),
              "parametres_stockes": int(sum(m.nb_parametres for m, _ in D.items)),
              "vues_lues": sorted({str(m.vue) for m, w in D.items if w > 0}), "cpu_final_s": time.process_time() - tf}
    return (sortie, ((a1, j1), (a2, j2))) if rendre_attaques else sortie


def construire(nom_famille: str, instance: int, code_delta: int, racine: int, cfg: Config, bras=None):
    exiger_config(cfg)
    ctx = Contexte(nom_famille, instance, code_delta, racine, cfg)
    regime = REGIME[nom_famille]
    bras = tuple(BRAS_DU_REGIME[regime] if bras is None else bras)
    for b in bras:
        if b not in BRAS_DU_REGIME[regime]:
            raise GardeArret(f"bras inconnu pour le régime {regime} : {b!r}")
    une_vue = regime == "vues"
    M0 = ctx.entrainer(COMMUN, 0, list(ctx.fam.centres), np.full(cfg.J, 1.0 / cfg.J), 1, une_vue)
    M0b = ctx.entrainer(COMMUN, 0, list(ctx.fam.centres), np.full(cfg.J, 1.0 / cfg.J), 1, une_vue)
    exiger_meme_moniteur(M0, M0b)
    a_faire = [b for b in TRAJECTOIRES if b in bras or any(TEMOINS[c][1] == b for c in bras if c in TEMOINS)]
    etats = {}
    for b in a_faire:
        etats[b] = trajectoire(b, ctx, Moniteur(M0.W.copy(), M0.b.copy(), M0.vue).calibrer(ctx.Xcal, cfg.alpha))
    defenses = {}
    for b in bras:
        if b in TRAJECTOIRES:
            defenses[b] = (etats[b], etats[b]["defense_finale"], TRAJECTOIRES[b][0])
        else:
            src = TEMOINS[b][1]
            defenses[b] = (etats[src], defense_temoin(b, etats[src], ctx), TRAJECTOIRES[src][0])
    return ctx, etats, defenses, bras


def executer_tache(nom_famille: str, instance: int, code_delta: int, racine: int, cfg: Config, bras=None) -> dict:
    t0 = time.process_time()
    ctx, etats, defenses, bras = construire(nom_famille, instance, code_delta, racine, cfg, bras)
    sortie = {"famille": nom_famille, "instance": instance, "code_delta": code_delta, "delta": ctx.delta,
              "racine": racine, "config_sha256": cfg.empreinte(), "version": VERSION,
              "exact": couche_exacte(ctx.fam, ctx.delta, cfg), "centres": ctx.fam.centres.tolist(), "bras": {}}
    for b in bras:
        etat, dfin, cb = defenses[b]
        res = phase_finale(dfin, ctx, etat, cb)
        if b in TRAJECTOIRES:
            res.update(par_tour=etat["par_tour"], valeur_jeu_restreint=etat["valeur_jeu_restreint"],
                       cycle=etat["cycle"], cpu_trajectoire_s=etat["cpu_trajectoire_s"])
        else:
            res["source"] = TEMOINS[b][1]
        sortie["bras"][b] = res
        exiger_plafond(t0, cfg, f"après la finale de {b}")
    sortie["entrainements"], sortie["non_convergences"] = ctx.entr, ctx.nonconv
    sortie["attaquant"] = {"departs": ctx.att["departs"], "non_finis": ctx.att["non_finis"],
                           "reponses_a_la_limite": ctx.att["a_la_limite"],
                           "statuts": {str(k): v for k, v in sorted(ctx.att["statuts"].items())}}
    exiger_convergence(ctx.nonconv, ctx.entr, cfg)
    exiger_departs_finis(ctx.att["non_finis"], ctx.att["departs"], cfg)
    sortie["cpu_tache_s"] = time.process_time() - t0
    return sortie


def exiger_meme_moniteur(a: Moniteur, b: Moniteur) -> None:
    if not (np.array_equal(a.W, b.W) and np.array_equal(a.b, b.b) and a.t == b.t):
        raise GardeArret("moniteur du tour 0 non reproductible bit à bit")


def exiger_plafond(t0: float, cfg: Config, ou: str) -> None:
    if time.process_time() - t0 > cfg.plafond_cpu_tache_s:
        raise GardeArret(f"plafond de temps processeur d'une tâche dépassé ({ou})")


def exiger_convergence(nonconv: int, total: int, cfg: Config) -> None:
    if total and nonconv / total > cfg.taux_nonconv_max:
        raise GardeArret(f"entraînements non convergés : {nonconv}/{total} > {cfg.taux_nonconv_max}")


# =================================================================================================================
# Q3b : canal « comportement », nombre L de vues surveillées, trois défenses (analytique)
# =================================================================================================================
def seuil_vues(alpha_a: float, L: int) -> float:
    """Seuil commun des L moniteurs de vues (union, vues indépendantes) au taux total α_a ; α_a = 0 : +∞."""
    if alpha_a <= 0:
        return float("inf")
    return float(ndtri((1 - alpha_a) ** (1.0 / L)))


def log_gain(x: float, Ra: float, L: int, t: float, sD: float, kappa: float, beta0: float, zb: float) -> float:
    """log G(x) = log dommage + log P(non-détection) pour un déplacement x par vue (symétrique en v)."""
    v = -L * x * x / (2 * sD * sD)
    if np.isfinite(t):
        v += L * float(log_ndtr(t - Ra + x))
    if np.isfinite(zb):
        v += float(log_ndtr(zb - beta0 - kappa * np.sqrt(L) * x))
    return v


def gain_maximal(Ra, L, t, sD, kappa, beta0, zb, cfg: Config) -> tuple[float, float]:
    """Meilleur gain de l'adversaire (log-concave en x ≥ 0 : grille puis affinage ; garde si l'affinage descend)."""
    f = (lambda x: log_gain(x, Ra, L, t, sD, kappa, beta0, zb))
    xs = np.linspace(0.0, Ra + 6.0, cfg.grille_x)
    vals = np.array([f(x) for x in xs])
    x, v = _maximiser_1d(f, 0.0, Ra + 6.0, cfg.grille_x)
    if v < vals.max() - 1e-12:
        raise GardeArret("Q3b : l'optimiseur du déplacement rend moins que la grille")
    return float(np.exp(v)), x


def exiger_parametres_prix(Ra, sD, kappa, beta0, L) -> None:
    if not (Ra > 0 and sD > 0 and kappa >= 0 and beta0 >= 0 and int(L) >= 1):
        raise GardeArret("Q3b : paramètres invalides (R_a > 0, s_D > 0, κ ≥ 0, β₀ ≥ 0, L ≥ 1)")


def gains_prix(Ra: float, sD: float, kappa: float, beta0: float, L: int, cfg: Config) -> dict:
    """Gains maximaux sous trois défenses au taux total α : activations seules, comportement seul, lecture jointe
    (partage α_a / α_b choisi par le défenseur ; les deux défenses à un canal sont les bords du partage)."""
    exiger_parametres_prix(Ra, sD, kappa, beta0, L)
    al, inf = cfg.alpha, float("inf")
    z = float(ndtri(1 - al))
    G_act, x_act = gain_maximal(Ra, L, seuil_vues(al, L), sD, kappa, beta0, inf, cfg)
    G_comp, x_comp = gain_maximal(Ra, L, inf, sD, kappa, beta0, z, cfg)

    def joint(aa):
        ab = 1 - (1 - al) / (1 - aa)
        zb = inf if ab <= 0 else float(ndtri(1 - ab))
        return gain_maximal(Ra, L, seuil_vues(aa, L), sD, kappa, beta0, zb, cfg)
    grille = np.linspace(0.0, al, cfg.grille_partage)
    vals = [joint(a)[0] for a in grille]
    i = int(np.argmin(vals))
    G_j, a_j = float(vals[i]), float(grille[i])
    lo, hi = grille[max(i - 1, 0)], grille[min(i + 1, len(grille) - 1)]
    if hi > lo:
        r = minimize_scalar(lambda a: joint(a)[0], bounds=(lo, hi), method="bounded", options={"xatol": 1e-10})
        if r.fun < G_j:
            G_j, a_j = float(r.fun), float(r.x)
    if G_j > min(G_act, G_comp) + 1e-12:
        raise GardeArret("Q3b : gain de la lecture jointe au-dessus d'une défense à un canal (bords du partage)")
    return {"L": int(L), "G_act": G_act, "G_comp": G_comp, "G_joint": G_j, "alpha_act_joint": a_j,
            "x_act": x_act, "x_comp": x_comp, "x_joint": joint(a_j)[1],
            "dilemme": min(G_act, G_comp) - G_j}


def configurations_prix(racine: int, indices, cfg: Config) -> list[dict]:
    out = []
    for k in indices:
        g = gen(racine, ROLE_PRIX, int(k))
        out.append({"k": int(k), "Ra": float(g.uniform(cfg.Ra_min, cfg.Ra_max)),
                    "sD": float(g.uniform(cfg.sD_min, cfg.sD_max)),
                    "kappa": float(g.uniform(cfg.kappa_min, cfg.kappa_max)),
                    "beta0": float(g.uniform(cfg.beta0_min, cfg.beta0_max))})
    return out


def executer_prix(racine: int, indices, cfg: Config) -> list[dict]:
    res = []
    for c in configurations_prix(racine, indices, cfg):
        res.append({**c, "par_L": [gains_prix(c["Ra"], c["sD"], c["kappa"], c["beta0"], L, cfg)
                                   for L in range(1, cfg.L_max + 1)]})
    return res


def verifier_gain_mc(Ra, sD, kappa, beta0, L, alpha_a, x, cfg: Config, n: int, rng) -> tuple[float, float]:
    """Contrôle de Monte-Carlo de la formule : simule les scores des L vues et le comportement ; renvoie (gain simulé,
    gain analytique) au partage α_a et au déplacement x donnés."""
    al = cfg.alpha
    t = seuil_vues(alpha_a, L)
    ab = 1 - (1 - al) / (1 - alpha_a) if alpha_a < al else 0.0
    zb = float("inf") if ab <= 0 else float(ndtri(1 - ab))
    S = (Ra - x) + rng.standard_normal((n, L))
    b = beta0 + kappa * np.sqrt(L) * x + rng.standard_normal(n)
    alarme = (S > t).any(1) | (b > zb)
    dommage = np.exp(-L * x * x / (2 * sD * sD))
    return float(dommage * np.mean(~alarme)), float(np.exp(log_gain(x, Ra, L, t, sD, kappa, beta0, zb)))


# =================================================================================================================
# Analyse : grandeurs par tâche, intervalles par rééchantillonnage des instances
# =================================================================================================================
GRANDEURS = {  # code → (libellé, familles, fonction de la tâche)
    1: ("VT_B", ("N2", "C2"), lambda r: r["bras"]["B"]["V_final"] - r["bras"]["PUR_B"]["V_final"]),
    2: ("VT_Bp", ("N2", "C2"), lambda r: r["bras"]["Bp"]["V_final"] - r["bras"]["PUR_Bp"]["V_final"]),
    3: ("VT_BpV", ("NV", "CV"), lambda r: r["bras"]["BpV"]["V_final"] - r["bras"]["PUR_BpV"]["V_final"]),
    4: ("UM_B", ("N2", "C2"), lambda r: r["bras"]["U_B"]["V_final"] - r["bras"]["B"]["V_final"]),
    5: ("UM_Bp", ("N2", "C2"), lambda r: r["bras"]["U_Bp"]["V_final"] - r["bras"]["Bp"]["V_final"]),
    6: ("UM_BpV", ("NV", "CV"), lambda r: r["bras"]["U_BpV"]["V_final"] - r["bras"]["BpV"]["V_final"]),
    7: ("CAL_B", ("N2", "C2"), lambda r: (r["bras"]["B"]["V_final"] - r["exact"]["V_mel"])
        if r["exact"]["V_mel"] is not None else None),
    8: ("CAL_BpV", ("NV", "CV"), lambda r: (r["bras"]["BpV"]["V_final"] - r["exact"]["V_mel"])
        if r["exact"]["V_mel"] is not None else None),
    9: ("CAL_U_B", ("N2",), lambda r: r["bras"]["U_B"]["V_final"] - r["exact"]["V_union"]),
    10: ("CAL_U_BpV", ("NV",), lambda r: r["bras"]["U_BpV"]["V_final"] - r["exact"]["V_union"]),
    11: ("A_moins_Vpur", ("N2", "C2"), lambda r: r["bras"]["A"]["V_final"] - r["exact"]["V_pur"]),
    12: ("AV_moins_Vpur", ("NV", "CV"), lambda r: r["bras"]["AV"]["V_final"] - r["exact"]["V_pur"]),
    13: ("DV_moins_Vpur", ("NV", "CV"), lambda r: r["bras"]["DV"]["V_final"] - r["exact"]["V_pur"]),
    14: ("D_moins_B", ("N2", "C2"), lambda r: r["bras"]["D"]["V_final"] - r["bras"]["B"]["V_final"]),
    15: ("Bp_moins_D", ("N2", "C2"), lambda r: r["bras"]["Bp"]["V_final"] - r["bras"]["D"]["V_final"]),
    16: ("CAL_PUR_B", ("N2", "C2"), lambda r: r["bras"]["PUR_B"]["V_final"] - r["exact"]["V_pur"]),
    17: ("CAL_PUR_BpV", ("NV", "CV"), lambda r: r["bras"]["PUR_BpV"]["V_final"] - r["exact"]["V_pur"]),
    18: ("Bp_moins_Vunion", ("N2",), lambda r: r["bras"]["Bp"]["V_final"] - r["exact"]["V_union"]),
    19: ("D_moins_Vunion", ("N2",), lambda r: r["bras"]["D"]["V_final"] - r["exact"]["V_union"]),
}
INDICATEURS = {  # code → (libellé, bras, clé)
    101: ("A I1", "A", "I1_progres"), 102: ("A I2", "A", "I2_baisse"), 103: ("A I3", "A", "I3_retours"),
    104: ("A I4", "A", "I4_changements"), 111: ("AV I1", "AV", "I1_progres"), 112: ("AV I2", "AV", "I2_baisse"),
    113: ("AV I3", "AV", "I3_retours"), 114: ("AV I4", "AV", "I4_changements"),
    121: ("B I3", "B", "I3_retours"), 122: ("Bp I3", "Bp", "I3_retours"), 123: ("BpV I3", "BpV", "I3_retours"),
    124: ("D I3", "D", "I3_retours"), 125: ("DV I3", "DV", "I3_retours")}
CONTRASTES_REGIME = {  # code → (libellé, grandeur, famille non couvrable, témoin)
    201: ("VT_B N2-C2", 1, "N2", "C2"), 202: ("VT_BpV NV-CV", 3, "NV", "CV"), 203: ("UM_B N2-C2", 4, "N2", "C2"),
    204: ("UM_BpV NV-CV", 6, "NV", "CV"), 205: ("VT_Bp N2-C2", 2, "N2", "C2")}


def _reech(x: np.ndarray, racine: int, *cle) -> dict:
    g = gen(racine, ROLE_REECH, *cle)
    boot = x[g.integers(0, len(x), size=(20000, len(x)))].mean(1)
    return {"moyenne": float(x.mean()), "ecart_type": float(x.std(ddof=1)) if len(x) > 1 else float("nan"),
            "n": int(len(x)), "quantiles": {f"q{p:g}": float(np.quantile(boot, p)) for p in QUANTILES}}


def resume_bras(rs: list, nom: str) -> dict:
    b = [r["bras"][nom] for r in rs]
    out = {"V_moyen": float(np.mean([x["V_final"] for x in b])), "V_min": float(np.min([x["V_final"] for x in b])),
           "V_max": float(np.max([x["V_final"] for x in b])),
           "fpr_moyen": float(np.mean([x["fpr_final"] for x in b])),
           "standard_moins_renforce": float(np.mean([x["V_standard"] - x["V_renforce"] for x in b])),
           "part_pure": float(np.mean([x["pur"] for x in b])), "support_moyen": float(np.mean([x["support"] for x in b])),
           "poids_max_moyen": float(np.mean([max(x["poids_finaux"]) for x in b])),
           "parametres_par_requete_max": int(max(x["parametres_par_requete"] for x in b)),
           "parametres_stockes_max": int(max(x["parametres_stockes"] for x in b))}
    if all(x.get("valeur_jeu_restreint") is not None for x in b):
        out["valeur_restreinte_moins_V"] = float(np.mean([x["valeur_jeu_restreint"] - x["V_final"] for x in b]))
    if all("cycle" in x for x in b):
        cy = [x["cycle"] for x in b]
        out["cycle"] = {k: float(np.mean([c[k] for c in cy])) for k in ("I1_progres", "I2_baisse", "I3_retours",
                                                                        "I4_changements")}
        out["cycle"]["I3_nul"], out["cycle"]["I4_nul"] = cy[0]["I3_nul"], cy[0]["I4_nul"]
        out["iii_par_tour"] = [float(v) for v in np.mean([x["par_tour"]["iii"] for x in b], axis=0)]
    return out


def analyser(resultats: list, racine: int) -> dict:
    sortie = {"par_famille": {}, "regime": {}}
    par = {}
    for r in resultats:
        par.setdefault((r["famille"], r["code_delta"]), []).append(r)
    for (f, cd), rs in sorted(par.items()):
        rs = sorted(rs, key=lambda r: r["instance"])
        ex = [r["exact"] for r in rs]
        bloc = {"n": len(rs), "delta": rs[0]["delta"], "bras": {}, "grandeurs": {}, "indicateurs": {},
                "exact": {"V_pur": float(np.mean([e["V_pur"] for e in ex])),
                          "V_mel": (float(np.mean([e["V_mel"] for e in ex])) if all(e["V_mel"] is not None for e in ex)
                                    else None),
                          "V_union": (float(np.mean([e["V_union"] for e in ex]))
                                      if all(e["V_union"] is not None for e in ex) else None),
                          "VT_exact": (float(np.mean([e["VT_exact"] for e in ex]))
                                       if all(e["VT_exact"] is not None for e in ex) else None),
                          "part_selle_certifiee": float(np.mean([e["selle_certifiee"] for e in ex]))}}
        for nom in BRAS_DU_REGIME[REGIME[f]]:
            if all(nom in r["bras"] for r in rs):
                bloc["bras"][nom] = resume_bras(rs, nom)
        for code, (lib, fams, fn) in GRANDEURS.items():
            if f not in fams:
                continue
            try:
                vals = [fn(r) for r in rs]
            except KeyError:
                continue
            vals = np.array([v for v in vals if v is not None], float)
            if len(vals):
                bloc["grandeurs"][lib] = _reech(vals, racine, FAMILLES[f], cd, code)
        for code, (lib, nom, cle) in INDICATEURS.items():
            if all(nom in r["bras"] and "cycle" in r["bras"][nom] for r in rs):
                bloc["indicateurs"][lib] = _reech(np.array([r["bras"][nom]["cycle"][cle] for r in rs]), racine,
                                                  FAMILLES[f], cd, code)
        bloc["non_convergences"] = int(sum(r["non_convergences"] for r in rs))
        bloc["entrainements"] = int(sum(r["entrainements"] for r in rs))
        bloc["departs_non_finis"] = int(sum(r["attaquant"]["non_finis"] for r in rs))
        bloc["departs"] = int(sum(r["attaquant"]["departs"] for r in rs))
        sortie["par_famille"][f"{f}|{cd}"] = bloc
    for code, (lib, gcode, fnc, ftem) in CONTRASTES_REGIME.items():
        _, _, fn = GRANDEURS[gcode]
        for cd in sorted({k[1] for k in par}):
            a = {r["instance"]: r for r in par.get((fnc, cd), [])}
            b = {r["instance"]: r for r in par.get((ftem, cd), [])}
            communs = sorted(set(a) & set(b))
            try:
                vals = np.array([fn(a[i]) - fn(b[i]) for i in communs], float)
            except KeyError:
                continue
            if len(vals):
                sortie["regime"][f"{lib}|{cd}"] = _reech(vals, racine, 0, cd, code)
    return sortie


def classer_effet(q: dict, m: float, bas="q0.0125", haut="q0.9875", eq_bas="q0.025", eq_haut="q0.975") -> str:
    """Classe d'une grandeur (effet attendu positif) à marge m : « > m », « < −m », « ≈ 0 », « ≳ 0 », « ≲ 0 », « ? »."""
    if q[bas] > m:
        return "> m"
    if q[haut] < -m:
        return "< −m"
    if q[eq_bas] > -m and q[eq_haut] < m:
        return "≈ 0"
    if q[bas] > 0:
        return "≳ 0"
    if q[haut] < 0:
        return "≲ 0"
    return "?"


def classer_etalonnage(q: dict, tau: float, bas="q0.0125", haut="q0.9875") -> str:
    if q[bas] > -tau and q[haut] < tau:
        return "étalonnée"
    if q[haut] < -tau:
        return "biais bas"
    if q[bas] > tau:
        return "biais haut"
    return "?"


def lire_tables(analyse: dict, m: float, tau: float) -> dict:
    """Aide mécanique à la lecture (Tables E1 à E5 du brouillon 1 ; le texte scellé fait foi). Intervalles : par δ,
    Bonferroni sur 8 grandeurs principales (2 familles non couvrables × 2 témoins × 2 δ) : quantiles 0,3125 % et
    99,6875 % ; équivalence 0,625 % et 99,375 %."""
    pf, out = analyse["par_famille"], {"E1": {}, "E2": {}, "E3": {}, "E4": {}}
    B8 = dict(bas="q0.003125", haut="q0.996875", eq_bas="q0.00625", eq_haut="q0.99375")
    for cle, bloc in pf.items():
        f, cd = cle.split("|")
        g = bloc["grandeurs"]
        lib_vt = "VT_B" if f in ("N2", "C2") else "VT_BpV"
        lib_um = "UM_B" if f in ("N2", "C2") else "UM_BpV"
        lib_cal = "CAL_B" if f in ("N2", "C2") else "CAL_BpV"
        if lib_vt in g:
            out["E1"][cle] = classer_effet(g[lib_vt]["quantiles"], m, **B8)
        if lib_um in g:
            out["E2"][cle] = classer_effet(g[lib_um]["quantiles"], m, **B8)
        if lib_cal in g:
            out["E3"][cle] = classer_etalonnage(g[lib_cal]["quantiles"], tau, "q0.003125", "q0.996875")
        a = "A" if f in ("N2", "C2") else "AV"
        if a in bloc["bras"]:
            VA, Vp = bloc["bras"][a]["V_moyen"], bloc["exact"]["V_pur"]
            I4 = bloc["indicateurs"].get(f"{a} I4", {}).get("quantiles", {})
            out["E4"][cle] = ("cycle sans couverture" if VA <= Vp + m and I4.get("q0.0125", 0) > 0.5
                              else "alternance couverte" if VA >= bloc["exact"]["V_pur"] - 0.08 and Vp >= 0.5
                              else "autre")
    cds = sorted({k.split("|")[1] for k in pf})
    e1, e3 = out["E1"], out["E3"]
    tirage_nc = all(e1.get(f"{f}|{cd}") == "> m" for f in NON_COUVRABLES for cd in cds)
    tirage_tem = all(e1.get(f"{TEMOIN_DE[f]}|{cd}") == "≈ 0" for f in NON_COUVRABLES for cd in cds)
    fabrique = any(e1.get(f"{TEMOIN_DE[f]}|{cd}") == "> m" for f in NON_COUVRABLES for cd in cds)
    etal = all(e3.get(f"{f}|{cd}") == "étalonnée" for f in NON_COUVRABLES for cd in cds)
    if tirage_nc and tirage_tem and etal:
        v = "tirage utile exactement là où la classe ne couvre pas ; nul sur les témoins ; instrument étalonné"
    elif not tirage_nc:
        v = "instrument incapable de montrer le tirage là où il existe exactement"
    elif fabrique:
        v = "instrument qui fabrique du tirage sur les témoins"
    elif not etal:
        v = "tirage montré, étalonnage insuffisant"
    else:
        v = "non tranché"
    out["E5"] = v
    return out


def analyser_prix(res: list, racine: int, m_b: float) -> dict:
    Ls = sorted({p["L"] for c in res for p in c["par_L"]})
    par_L = {}
    for L in Ls:
        lig = [next(p for p in c["par_L"] if p["L"] == L) for c in res]
        dil = np.array([p["dilemme"] for p in lig])
        par_L[str(L)] = {"G_act": float(np.mean([p["G_act"] for p in lig])),
                         "G_comp": float(np.mean([p["G_comp"] for p in lig])),
                         "G_joint": float(np.mean([p["G_joint"] for p in lig])),
                         "dilemme_moyen": float(dil.mean()),
                         "part_dilemme": _reech((dil > m_b).astype(float), racine, 0, L, 301)}
    act = np.array([[p["G_act"] for p in c["par_L"]] for c in res])
    joi = np.array([[p["G_joint"] for p in c["par_L"]] for c in res])
    kap = np.array([c["kappa"] for c in res])
    b0 = np.array([c["beta0"] for c in res])
    ratio = joi / act
    fort = kap >= 0.5
    faible = (kap < 0.2) & (b0 < 0.2)
    return {"par_L": par_L,
            "part_act_strictement_decroissant": float(np.mean(np.all(np.diff(act, axis=1) < 0, axis=1))),
            "mediane_act_L8_sur_L1": float(np.median(act[:, -1] / act[:, 0])),
            "part_ratio_joint_act_decroissant_kappa_fort": (float(np.mean(np.all(np.diff(ratio[fort], axis=1) <= 1e-12,
                                                                                 axis=1))) if fort.any() else None),
            "n_kappa_fort": int(fort.sum()),
            "part_dilemme_L4_kappa_beta_faibles": (float(np.mean([next(p for p in c["par_L"] if p["L"] == 4)["dilemme"]
                                                                   > m_b for c, ok in zip(res, faible) if ok]))
                                                    if faible.any() else None),
            "n_kappa_beta_faibles": int(faible.sum()), "n_configs": len(res)}


# =================================================================================================================
# Attaquant indépendant (audit R4, CM3-01) : départs nombreux, puis stratégie d'évolution sans gradient
# =================================================================================================================
def _deux_taux(mu, defense: Defense, Z, tau):
    X = mu + Z
    return defense.taux(X), defense.lisse_et_grad(X, tau)[0]


def evolution(defense, x0, j, fam, delta, cfg: Config, rng, Z) -> np.ndarray:
    idx = np.array(fam.libres[j])
    c = fam.centres[j]
    x = x0.copy()
    fx = _deux_taux(x, defense, Z, cfg.tau)
    pas = 0.1 * delta
    for _ in range(cfg.audit_es_generations):
        best = None
        for _ in range(cfg.audit_es_lambda):
            y = x.copy()
            y[idx] = _projeter(x[idx] + pas * rng.standard_normal(len(idx)), c[idx], delta)
            fy = _deux_taux(y, defense, Z, cfg.tau)
            if best is None or fy < best[0]:
                best = (fy, y)
        if best[0] < fx:
            fx, x = best
            pas *= 1.5
        else:
            pas = max(pas * 0.9, 1e-4 * delta)
    exiger_admissible(x, fam, j, delta)
    return x


def attaquant_independant(dfin, ctx: Contexte, cb: int, passes, finales) -> dict:
    cfg = ctx.cfg
    D = Defense(dfin)

    def g(k):
        return ctx.g(cb, cfg.T + 1, ROLE_AUDIT, k)
    mu_l, j_l, info = meilleure_reponse(D, ctx.fam, ctx.delta, cfg, g(1), g(2), departs_suppl=list(passes) +
                                        list(finales), n_departs=cfg.audit_departs, n_mc=cfg.audit_n_mc,
                                        iter_max=cfg.audit_iter)
    exiger_departs_finis(info["non_finis"], info["departs"], cfg)
    Z = g(4).standard_normal((cfg.audit_n_mc, cfg.d))
    e1 = evolution(D, mu_l, j_l, ctx.fam, ctx.delta, cfg, g(5), Z)
    e2 = evolution(D, finales[0][0], finales[0][1], ctx.fam, ctx.delta, cfg, g(7), Z)
    ev = [D.taux(x + g(k).standard_normal((cfg.n_eval, cfg.d))) for x, k in ((mu_l, 3), (e1, 6), (e2, 8))]
    return {"V_lourd": ev[0], "V_evolution_depuis_lourd": ev[1], "V_evolution_depuis_standard": ev[2]}


def auditer_tache(nom_famille, instance, code_delta, racine, cfg: Config, source: dict) -> dict:
    t0 = time.process_time()
    ctx, etats, defenses, bras = construire(nom_famille, instance, code_delta, racine, cfg)
    sortie = {"famille": nom_famille, "instance": instance, "code_delta": code_delta, "bras": {}}
    for b in bras:
        if b not in source.get("bras", {}):
            raise GardeArret(f"audit : bras {b} absent de la tâche auditée")
        etat, dfin, cb = defenses[b]
        res, finales = phase_finale(dfin, ctx, etat, cb, rendre_attaques=True)
        if res["V_final"] != source["bras"][b]["V_final"]:
            raise GardeArret(f"audit : V reconstruit ≠ V de la tâche auditée ({b}, {nom_famille}, instance {instance})")
        passes = list(zip(etat["attaques"][cfg.J:], etat["modes"][cfg.J:]))
        ind = attaquant_independant(dfin, ctx, cb, passes, finales)
        sortie["bras"][b] = {"V_source": res["V_final"], **ind,
                             "V_audit": min(res["V_final"], *ind.values())}
    sortie["cpu_tache_s"] = time.process_time() - t0
    return sortie


def juger_audit(taches: list, m: float, marge: float) -> dict:
    """Critère d'artefact (CM3-01 de l'arène v3) : par famille et δ, pour VT et UM, artefact si la classe (marge m,
    sans intervalle : signe et seuil sur la moyenne des tâches auditées) change, ou si la moyenne change de plus de
    `marge` (m/2). Les deux côtés sont comparés avec le même minimum (V source contre V audit = min(V, réponses))."""
    paires = {"N2": (("B", "PUR_B"), ("U_B", "B")), "C2": (("B", "PUR_B"), ("U_B", "B")),
              "NV": (("BpV", "PUR_BpV"), ("U_BpV", "BpV")), "CV": (("BpV", "PUR_BpV"), ("U_BpV", "BpV"))}

    def classe(x):
        return "> m" if x > m else "< −m" if x < -m else "|·| ≤ m"
    out, drapeaux = {}, []
    for f in sorted({t["famille"] for t in taches}):
        for cd in sorted({t["code_delta"] for t in taches if t["famille"] == f}):
            ts = [t for t in taches if t["famille"] == f and t["code_delta"] == cd]
            bloc = {}
            for b1, b2 in paires[f]:
                s = float(np.mean([t["bras"][b1]["V_source"] - t["bras"][b2]["V_source"] for t in ts]))
                a = float(np.mean([t["bras"][b1]["V_audit"] - t["bras"][b2]["V_audit"] for t in ts]))
                art = classe(s) != classe(a) or abs(a - s) > marge
                drapeaux.append(art)
                bloc[f"{b1}-{b2}"] = {"source": s, "audit": a, "ecart": a - s, "n": len(ts), "artefact": art}
            out[f"{f}|{cd}"] = bloc
    return {"par_famille": out, "artefact": any(drapeaux), "marge": marge, "m": m}


# =================================================================================================================
# Processus de travail, arrêt par PID (R10) — recopiés de la v3
# =================================================================================================================
def _debut_processus(pid: int):
    try:
        return Path(f"/proc/{int(pid)}/stat").read_text().rsplit(")", 1)[1].split()[19]
    except (OSError, IndexError):
        return None


def processus_vivant(pid: int, debut=None) -> bool:
    try:
        os.kill(int(pid), 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        pass
    try:
        champs = Path(f"/proc/{int(pid)}/stat").read_text().rsplit(")", 1)[1].split()
    except OSError:
        return False
    if champs[0] in ("Z", "X"):
        return False
    return debut is None or champs[19] == str(debut)


def lire_pids(chemin):
    out = []
    for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
        if ligne.strip() and not ligne.startswith("#"):
            pid, debut = (ligne.split() + [None])[:2]
            out.append((int(pid), debut))
    return out


def arreter_par_pid(pids, delai_s: float = 10.0) -> list:
    vivants = [(int(p), d) for p, d in pids if processus_vivant(p, d)]
    for p, _ in vivants:
        try:
            os.kill(p, signal.SIGTERM)
        except ProcessLookupError:
            pass
    t = time.monotonic()
    while time.monotonic() - t < delai_s and any(processus_vivant(p, d) for p, d in vivants):
        time.sleep(0.05)
    for p, d in vivants:
        if processus_vivant(p, d):
            try:
                os.kill(p, signal.SIGKILL)
            except ProcessLookupError:
                pass
    return [p for p, _ in vivants]


def exiger_aucun_orphelin(pids) -> None:
    vivants = [int(p) for p, d in pids if processus_vivant(p, d)]
    if vivants:
        raise GardeArret(f"processus de travail encore vivants (PID {vivants}) : arrêter par PID avant toute reprise")


def _travail(args):
    mode, f, i, cd, racine, cfg_dict, prereg, source = args
    cfg = Config(**{k: tuple(v) if isinstance(v, list) else v for k, v in cfg_dict.items()})
    if racine in RACINES_DECISION and _AUTORISATION_DECISION["prereg_sha256"] is None:
        if prereg is None:
            raise GardeArret("racine de décision dans un processus de travail sans préenregistrement")
        autoriser_decision(prereg, cfg)
    if mode == "audit":
        return auditer_tache(f, i, cd, racine, cfg, source)
    return executer_tache(f, i, cd, racine, cfg)


def _lancer(taches, processus: int, fichier_pids=None, sceller_pids=False) -> list:
    import multiprocessing as mp

    if processus <= 1:
        return [_travail(t) for t in taches]
    ancien = signal.signal(signal.SIGTERM, lever_sur_term)
    pids = []
    try:
        with mp.get_context("spawn").Pool(processus) as pool:
            pids = [(p.pid, _debut_processus(p.pid)) for p in pool._pool]
            texte = "# PID et instant de départ des processus de travail (R10)\n" + \
                    "".join(f"{p} {d}\n" for p, d in pids)
            print("PID des processus de travail : " + " ".join(str(p) for p, _ in pids), file=sys.stderr, flush=True)
            if fichier_pids is not None:
                fp = _exiger_absent(Path(fichier_pids))
                fp.write_text(texte, encoding="utf-8")
                if sceller_pids:
                    from controle_ia.scellement import sceller

                    sceller(fp)
            res = pool.map(_travail, taches, chunksize=1)
    finally:
        signal.signal(signal.SIGTERM, ancien)
        arreter_par_pid(pids)
        exiger_aucun_orphelin(pids)
    return res


def executer(instances, racine, cfg: Config, processus=2, familles=None, prereg=None, fichier_pids=None,
             sceller_pids=False):
    familles = tuple(FAMILLES) if familles is None else tuple(familles)
    # ordre : les tâches les plus longues (champ complet) d'abord, pour équilibrer les processus
    taches = [("tache", f, i, cd, racine, asdict(cfg), None if prereg is None else str(prereg), None)
              for f in familles for cd in range(1, len(cfg.deltas) + 1) for i in instances]
    m0 = time.perf_counter()
    res = _lancer(taches, processus, fichier_pids, sceller_pids)
    return res, {"mur_s": time.perf_counter() - m0, "cpu_somme_taches_s": float(sum(r["cpu_tache_s"] for r in res)),
                 "processus": processus, "taches": len(taches)}


def auditer(cles, racine, cfg: Config, sources: dict, processus=2, prereg=None, fichier_pids=None, sceller_pids=False):
    taches = []
    for k in cles:
        if k not in sources:
            raise GardeArret(f"audit : tâche absente de la source {k}")
        f, i, cd = k
        taches.append(("audit", f, i, cd, racine, asdict(cfg), None if prereg is None else str(prereg), sources[k]))
    m0 = time.perf_counter()
    res = _lancer(taches, processus, fichier_pids, sceller_pids)
    return res, {"mur_s": time.perf_counter() - m0, "cpu_somme_taches_s": float(sum(r["cpu_tache_s"] for r in res)),
                 "taches": len(taches)}


def _versions() -> dict:
    import platform

    import scipy

    try:
        commit = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "HEAD"], capture_output=True,
                                text=True).stdout.strip()
    except OSError:
        commit = None
    return {"python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__,
            "plateforme": platform.platform(), "commit": commit, "code_sha256": empreinte_fichier(__file__),
            "bibliotheque_sha256": {f: empreinte_fichier(DEPOT / f) for f in FICHIERS_BIBLIOTHEQUE}}


def _plage(s: str) -> list:
    a, b = s.split(":")
    return list(range(int(a), int(b)))


def _exiger_absent(sortie: Path) -> Path:
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà : R12 interdit d'écraser")
    return sortie


def _ecrire_nouveau(sortie: Path, corps: dict) -> None:
    if sortie.exists():
        raise GardeArret(f"{sortie} apparu pendant l'exécution : R12 interdit d'écraser")
    sortie.write_text(json.dumps(corps, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def charger_pilote(chemin, cfg: Config) -> dict:
    corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
    man = corps.get("manifeste", {})
    exiger_racine_essai(man.get("racine", 0))
    if corps.get("mode") != "essai" or man.get("config_sha256") != cfg.empreinte():
        raise GardeArret(f"audit-essai : {chemin} n'est pas un pilote de cette configuration")
    return corps


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sp = ap.add_subparsers(dest="mode", required=True)
    sp.add_parser("identite")
    ex = sp.add_parser("exact")
    ex.add_argument("--instances", default="0:8")
    ex.add_argument("--racine", type=int, default=RACINE_ESSAI)
    e = sp.add_parser("essai")
    e.add_argument("--instances", default="0:2")
    e.add_argument("--sortie", required=True)
    e.add_argument("--processus", type=int, default=2)
    e.add_argument("--racine", type=int, default=RACINE_ESSAI)
    e.add_argument("--familles", default="N2,C2,NV,CV")
    e.add_argument("--pids", default=None)
    pr = sp.add_parser("prix")
    pr.add_argument("--configs", default="0:200")
    pr.add_argument("--sortie", required=True)
    pr.add_argument("--racine", type=int, default=RACINE_ESSAI_PRIX)
    ae = sp.add_parser("audit-essai")
    ae.add_argument("--pilote", required=True)
    ae.add_argument("--instances", default="0:1")
    ae.add_argument("--sortie", required=True)
    ae.add_argument("--processus", type=int, default=2)
    dc = sp.add_parser("decision")
    dc.add_argument("--prereg", required=True)
    dc.add_argument("--run-principal", required=True)
    dc.add_argument("--instances", required=True)
    dc.add_argument("--configs", required=True)
    dc.add_argument("--run-id", required=True)
    dc.add_argument("--processus", type=int, default=2)
    o = sp.add_parser("orphelins")
    o.add_argument("--pids", required=True)
    o.add_argument("--arreter", action="store_true")
    a = ap.parse_args(argv)
    cfg = exiger_config(CONFIG_V1)
    if a.mode == "identite":
        print(bloc_identite(cfg))
        return 0
    if a.mode == "orphelins":
        pids = lire_pids(a.pids)
        if a.arreter:
            print(f"arrêtés par PID : {arreter_par_pid(pids)}")
        exiger_aucun_orphelin(pids)
        print("aucun processus de travail consigné ne tourne")
        return 0
    if a.mode == "exact":
        exiger_racine_essai(a.racine)
        for i in _plage(a.instances):
            fams = generer_familles(i, a.racine, cfg)
            for f in FAMILLES:
                for cd, dl in enumerate(cfg.deltas, start=1):
                    exa = couche_exacte(fams[f], dl, cfg)
                    print(json.dumps({"instance": i, "famille": f, "delta": dl,
                                      **{k: exa[k] for k in ("V_pur", "V_mel", "V_union", "VT_exact",
                                                             "selle_certifiee")}}, ensure_ascii=False))
        return 0
    if a.mode == "essai":
        exiger_racine_essai(a.racine)
        sortie = _exiger_absent(Path(a.sortie))
        res, temps = executer(_plage(a.instances), a.racine, cfg, a.processus, a.familles.split(","),
                              fichier_pids=a.pids)
        corps = {"mode": "essai", "manifeste": {"racine": a.racine, "schema_graines": cfg.schema_graines,
                                                "config": asdict(cfg), "config_sha256": cfg.empreinte(),
                                                "versions": _versions(), "commande": " ".join(sys.argv)},
                 "temps": temps, "analyse": analyser(res, a.racine), "resultats": res}
        _ecrire_nouveau(sortie, corps)
        print(f"essai écrit : {sortie} ; {temps}")
        return 0
    if a.mode == "prix":
        exiger_racine_essai(a.racine)
        sortie = _exiger_absent(Path(a.sortie))
        m0, c0 = time.perf_counter(), time.process_time()
        res = executer_prix(a.racine, _plage(a.configs), cfg)
        temps = {"mur_s": time.perf_counter() - m0, "cpu_s": time.process_time() - c0}
        corps = {"mode": "prix", "manifeste": {"racine": a.racine, "config": asdict(cfg),
                                               "config_sha256": cfg.empreinte(), "versions": _versions(),
                                               "commande": " ".join(sys.argv)},
                 "temps": temps, "analyse": analyser_prix(res, a.racine, 0.02), "resultats": res}
        _ecrire_nouveau(sortie, corps)
        print(f"prix écrit : {sortie} ; {temps}")
        return 0
    if a.mode == "audit-essai":
        pil = charger_pilote(a.pilote, cfg)
        sortie = _exiger_absent(Path(a.sortie))
        r0 = pil["manifeste"]["racine"]
        src = {(r["famille"], r["instance"], r["code_delta"]): r for r in pil["resultats"]}
        cles = [(f, i, cd) for f in FAMILLES for i in _plage(a.instances) for cd in range(1, len(cfg.deltas) + 1)]
        res, temps = auditer(cles, r0, cfg, src, a.processus)
        corps = {"mode": "audit-essai", "pilote": str(a.pilote), "pilote_sha256": empreinte_fichier(a.pilote),
                 "manifeste": {"racine": r0, "config_sha256": cfg.empreinte(), "versions": _versions(),
                               "commande": " ".join(sys.argv)},
                 "temps": temps, "jugement": juger_audit(res, 0.02, cfg.marge_audit), "taches": res}
        _ecrire_nouveau(sortie, corps)
        print(f"audit d'essai écrit : {sortie} ; artefact {corps['jugement']['artefact']} ; {temps}")
        return 0
    # décision : calcul décisif de l'extension APRÈS celui du pilote principal ; préenregistrement scellé exigé
    from controle_ia import manifeste as man

    exiger_run_principal(DEPOT, a.run_principal)
    sha = autoriser_decision(a.prereg, cfg, a.instances, a.configs)
    chemin_m, _ = man.creer_manifeste(DEPOT, a.run_id, {"config": asdict(cfg), "config_sha256": cfg.empreinte(),
                                                        "racine_q3": RACINE_Q3, "racine_prix": RACINE_PRIX,
                                                        "instances": a.instances, "configs": a.configs,
                                                        "run_principal": a.run_principal, "prereg_sha256": sha,
                                                        "versions": _versions()},
                                      ["extension"], entropie=RACINE_Q3, decisif=True, prereg=a.prereg,
                                      commande=" ".join(sys.argv))
    res, temps = executer(_plage(a.instances), RACINE_Q3, cfg, a.processus, prereg=a.prereg,
                          fichier_pids=chemin_m.parent / "pids-travail.txt", sceller_pids=True)
    prix = executer_prix(RACINE_PRIX, _plage(a.configs), cfg)
    man.ecrire_resultat(DEPOT, chemin_m, "resultats-extension", {"temps": temps, "resultats": res, "prix": prix})
    man.ecrire_resultat(DEPOT, chemin_m, "analyse-extension", {"q3": analyser(res, RACINE_Q3),
                                                               "q3b": analyser_prix(prix, RACINE_PRIX, 0.02)})
    print(f"run de décision écrit sous diag/{a.run_id}/")
    return 0


__all__ = ["Config", "CONFIG_V1", "generer_familles", "couche_exacte", "executer_tache", "analyser", "lire_tables",
           "gains_prix", "executer_prix", "analyser_prix", "exiger_racine_essai", "exiger_run_principal", "replace"]

if __name__ == "__main__":
    sys.exit(main())
