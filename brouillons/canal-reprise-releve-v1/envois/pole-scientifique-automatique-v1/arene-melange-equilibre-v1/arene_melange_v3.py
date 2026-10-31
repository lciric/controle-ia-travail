#!/usr/bin/env python3
"""Arène coévolutive synthétique : le mélange d'équilibre contre ses témoins, à nombre de paramètres égal (Q1) et à
classe de fonctions égale (Q2) — v3.

Pilote de mécanisme, sur processeur, de la piste 3 du brainstorm
`p-041-pont-vers-les-vrais-modeles-v1/brainstorm-malleabilite-et-arene-v1.md` (décision de Lazar R-695), réécrit après
la contre-lecture `contre-lecture-arene-melange-v1-brouillon1.md` (constats CM-01 à CM-17), puis après
`contre-lecture-arene-melange-v2-brouillon2.md` (constats CM2-01 à CM2-16). Ajouts de la v3 (bifurcation de conception
postérieure au pilote v2, déclarée) :
- B′ (code « Bp ») : mélange d'équilibre par double oracle dont l'oracle du défenseur rend des moniteurs maxout à
  `unites_Bp` unités, la classe du moniteur final de D ; C3′ (code « C3p ») : « ou » déterministe des moniteurs mêmes
  de B′ (composition standardisée, `MoniteurOu`) ;
- mesures de la condition d'application (la défense unique A converge-t-elle, oublie-t-elle ?) : matrice de détection
  croisée moniteur du tour s × attaque du tour t, indicateurs I1 (progrès), I2 (oubli), I3 (retours) ;
- contrôle d'attaquant indépendant (`attaquant_independant`, modes `audit` et `audit-essai`) ;
- arrêt par PID des processus de travail (R10) et garde « aucun orphelin » avant toute reprise.
Les bras A, B, C1, C2, C3, D sont ceux de la v2, inchangés. Aucun modèle de langage,
aucun texte : « l'attaquant » est un choix de paramètres dans une famille bornée de lois synthétiques (mélanges
gaussiens en dimension d), sous une contrainte de comportement (distance ≤ δ à une loi cible, piste 2). Le défenseur
est un classificateur simple sur échantillons, seuillé à un taux de fausses alertes α sur des échantillons propres.

Bras à trajectoire propre (T tours ; l'attaquant joue en dernier à chaque tour), à partir d'un moniteur commun au tour 0 :
- A « défense unique réentraînée, même oracle » : un moniteur linéaire réentraîné à chaque tour sur toutes les
  attaques passées (mélange uniforme), seul déployé. Ce n'est PAS le protocole de Bailey et collègues : l'oracle
  d'entraînement est celui des autres bras (maximisation de la détection à α), non la régression des sondes ;
- B « mélange d'équilibre » (double oracle tronqué à T tours) : tous les moniteurs passés, tirés au hasard selon les
  poids d'équilibre du jeu à somme nulle restreint (programme linéaire) ; l'oracle du défenseur entraîne un moniteur
  linéaire contre la stratégie d'équilibre de l'attaquant ;
- D « paramètres égaux » : un seul moniteur « maxout » (log-somme-exp de m scores linéaires) réentraîné sur toutes
  les attaques passées, m = nombre de moniteurs du mélange de B au même tour (même nombre de paramètres ; autre
  famille de fonctions et agrégation déterministe : ce n'est pas « la capacité » au sens fonctionnel).
Témoins « finale seulement », construits sur les T + 1 moniteurs MÊMES de B après le tour T (aucune trajectoire) :
- C1 poids uniformes ; C2 poids tirés au hasard (loi de Dirichlet uniforme, graine dérivée) ;
- C3 « ou » déterministe : scores standardisés sur le propre de calibration, multipliés par λ, empilés dans un seul
  moniteur à T + 1 unités (log-somme-exp ≈ maximum), seuil recalibré à α.
Pour tous les bras, la défense finale est figée puis l'attaquant joue en dernier (meilleure réponse standard et
renforcée ; (iii) retient la plus forte des deux).

Racines (R9) : RACINE et RACINE_TENUE servent à la décision, ne s'emploient qu'après autorisation par un
préenregistrement scellé, conforme et identifié (`autoriser_decision`, vérifiée aussi dans `gen` et dans chaque
processus de travail) ; RACINE_ESSAI et RACINE_ESSAI_TENUE (fraîches pour la v3) servent au pilote et au calcul de
puissance ; RACINE_RECALIBRAGE (fraîche, réservée, non employée) ne sert qu'à l'option de recalibrage des δ si Lazar la
retient ; RACINE_TESTS sert aux essais du code. Toutes les racines d'essai déjà employées (brouillon 1, v2,
contre-lecture 2) sont interdites en v3 (conception choisie ou résultats lus dessus). Toute graine est
`SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, …))`.

Commandes :
    PYTHONPATH=src python3 <ce fichier> essai --instances 0:24 --sortie FICHIER.json --processus 2 [--oracle logistique]
    PYTHONPATH=src python3 <ce fichier> audit-essai --pilote FICHIER.json --instances 0:1 --sortie AUDIT.json
    PYTHONPATH=src python3 <ce fichier> identite
    PYTHONPATH=src python3 <ce fichier> decision --prereg prereg/<scellé>.md --instances 0:N --run-id ID  (après GO)
    PYTHONPATH=src python3 <ce fichier> audit --prereg prereg/<scellé>.md --source-run ID --instances 0:5 --run-id ID2
    PYTHONPATH=src python3 <ce fichier> orphelins --pids FICHIER [--arreter]   (R10 : arrêt par PID, avant reprise)
    PYTHONPATH=src python3 <ce fichier> calibrage --instances 0:48 --sortie FICHIER.json   (option, si Lazar la retient)
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
from scipy.optimize import linprog, minimize  # noqa: E402
from scipy.special import expit, logsumexp, softmax  # noqa: E402
from scipy.stats import norm  # noqa: E402

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[4]
if str(DEPOT / "src") not in sys.path:
    sys.path.insert(0, str(DEPOT / "src"))

from controle_ia.gardes import GardeArret, exiger_numpy_minimal, lever_sur_term  # noqa: E402

VERSION = "arene_melange_v3"
IDENTIFIANT_PREREG = "PREREG-ARENE-MELANGE-EQUILIBRE-V1"
FICHIERS_BIBLIOTHEQUE = ("src/controle_ia/gardes.py", "src/controle_ia/prereg.py", "src/controle_ia/scellement.py",
                         "src/controle_ia/manifeste.py")

# --- racines (R9) : fixées avant toute exécution de la v3, sans lien avec un résultat -----------------------------
RACINE = 20261201              # décision : jamais employée hors décision autorisée
RACINE_TENUE = 20261202        # décision : familles tenues à l'écart (racine à part)
RACINES_DECISION = (RACINE, RACINE_TENUE)
# racines d'essai déjà employées : brouillon 1 (20261291/2), v2 (pilotes 20261293/4, calibrage 20261295/6, essais
# 20261297/8), diagnostics de la contre-lecture 2 (20269501/2) : conception choisie ou résultats lus dessus
RACINES_DEJA_EMPLOYEES = (20261291, 20261292, 20261293, 20261294, 20261295, 20261296, 20261297, 20261298,
                          20269501, 20269502)
RACINE_ESSAI, RACINE_ESSAI_TENUE = 20261311, 20261312          # pilote v3 (fraîche)
RACINE_TESTS, RACINE_TESTS_TENUE = 20261313, 20261314          # essais du code v3 et mesures de temps (fraîche)
RACINE_RECALIBRAGE, RACINE_RECALIBRAGE_TENUE = 20261315, 20261316   # réservée à l'option de recalibrage (non employée)

# --- δ de la décision : fixés en v2 par la règle `choisir_deltas` (calibrage-deltas-arene-melange-v2.json), inchangés
DELTAS_V3 = (1.4, 1.8)   # V(A) au calibrage v2 : 0,131 à 1,4 (≥ 10α) ; 0,034 à 1,8 (≥ 3α) ; pas de recalibrage en v3
GRILLE_CALIBRAGE = (0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.4)

# --- codes de dérivation des graines ----------------------------------------------------------------------------
BRAS_TRAJECTOIRE = ("A", "B", "D", "Bp")
TEMOINS_FINALE = ("C1", "C2", "C3", "C3p")
SOURCE_TEMOIN = {"C1": "B", "C2": "B", "C3": "B", "C3p": "Bp"}
TOUS_LES_BRAS = ("A", "B", "C1", "C2", "C3", "D", "Bp", "C3p")
BRAS = {"A": 1, "B": 2, "D": 4, "C1": 5, "C2": 6, "C3": 7, "Bp": 8, "C3p": 9}   # code 3 (ancien bras C) retiré
NOMS = {"Bp": "B′", "C3p": "C3′"}
COMMUN = 0
ROLE_CIBLE, ROLE_PROPRE_ENTR, ROLE_ATTAQUE_ENTR, ROLE_CAL, ROLE_FPR = 0, 1, 2, 3, 4
ROLE_MC, ROLE_DEPARTS, ROLE_EVAL, ROLE_INIT_MAXOUT = 5, 6, 7, 8
ROLE_TENUE_LOIS, ROLE_TENUE_EVAL, ROLE_FINAL, ROLE_COUT = 9, 10, 11, 12
ROLE_DIRICHLET, ROLE_COURBE, ROLE_AUDIT = 13, 14, 15
ROLE_REECH = 99
SCHEMA_GRAINES = ("SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, ...)) ; "
                  "bras commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7, B' 8, C3' 9 ; roles cible 0, propre 1, attaques "
                  "d'entrainement 2, calibration 3, fausses alertes 4, Monte-Carlo 5, departs 6, evaluation 7, init "
                  "maxout 8, lois tenues 9, echantillons tenus 10, final 11, cout 12, Dirichlet 13, courbe 14, attaquant "
                  "independant 15 ; reechantillonnage (code_delta, code_contraste, 0, 0, 99)")

# niveaux de quantiles du rééchantillonnage : bilatéral 95 % et 90 % ; Bonferroni sur 2 tests (δ), 4 tests (Q2) et
# 8 tests (Q1) ; équivalence au niveau 0,05/4 (Q2) et 0,05/8 (Q1) par côté
QUANTILES = (0.003125, 0.00625, 0.0125, 0.025, 0.05, 0.95, 0.975, 0.9875, 0.99375, 0.996875)


@dataclass(frozen=True)
class Config:
    d: int = 6                       # dimension des « activations » synthétiques
    K: int = 3                       # composantes du mélange (cible et attaque)
    r_cible: float = 4.0             # distance des moyennes cibles à l'origine (loi propre N(0, I))
    sigma_cible: float = 1.0
    boite_mu: float = 5.0            # |μ_kj| ≤ boite_mu
    sigma_min: float = 0.5
    sigma_max: float = 1.5
    deltas: tuple = ()               # budgets de comportement (δ_bas, δ_haut), fixés par `choisir_deltas`
    alpha: float = 0.01              # taux de fausses alertes visé sur le propre
    T: int = 8                       # tours de coévolution
    n_propre_entr: int = 2000
    n_attaque_entr: int = 2001       # multiple de K
    n_cal: int = 20000
    n_fpr: int = 20000
    n_eval: int = 19998              # multiple de K
    n_mc: int = 256                  # échantillons de Monte-Carlo par composante pour l'attaquant
    n_mc_final: int = 512
    departs: int = 4                 # départs aléatoires de la meilleure réponse à chaque tour
    departs_final: int = 12
    departs_cout: int = 3            # départs aléatoires des meilleures réponses de la courbe et du coût
    departs_renforce: int = 48       # attaquant final renforcé (contrôle de l'optimiseur)
    iter_renforce: int = 200
    iter_max: int = 100              # itérations SLSQP
    tau: float = 0.25                # température du lissage (unités d'écart-type du score propre)
    l2: float = 1e-3
    entrainement: str = "detection"  # oracle du défenseur, identique pour tous les bras ("logistique" : pilote témoin)
    departs_entr: int = 8
    iter_entr: int = 300             # itérations L-BFGS-B de l'entraînement
    n_tenue: int = 50                # lois tenues à l'écart par tâche (deux sous-familles)
    n_eval_tenue: int = 3999         # multiple de K
    lambda_ou: float = 8.0           # C3 : facteur des scores standardisés (log-somme-exp ≈ maximum)
    kappa_contournement: float = 0.5   # contourné si détection ≤ κ × détection de la cible non modifiée
    fractions_courbe: tuple = (0.25, 0.5, 0.75)   # courbe V(δ') aux fractions de δ (plus 0 et 1)
    pas_bissection: int = 3          # bissection dans l'intervalle de la courbe qui encadre le contournement
    tol_fpr: float = 0.005           # garde : |FPR mesuré − α| ≤ tol_fpr
    taux_nonconv_max: float = 0.05   # garde : part d'entraînements non convergés
    taux_departs_non_finis_max: float = 0.05   # garde : part de départs de l'attaquant au point non fini
    plafond_cpu_tache_s: float = 600.0  # garde : temps processeur d'une tâche (δ, instance)
    n_instances: int = 100           # N par δ (S4) ; comparé à --instances en décision
    grille_calibrage: tuple = GRILLE_CALIBRAGE
    n_calibrage: int = 12            # instances du calibrage v2 qui a fixé les δ (historique ; option : --instances)
    seuil_calibrage_haut: float = 0.03   # δ_haut : plus grand δ de la grille où V(A) moyen ≥ 3 α
    seuil_calibrage_bas: float = 0.10    # δ_bas : plus grand δ < δ_haut où V(A) moyen ≥ 10 α
    schema_graines: str = SCHEMA_GRAINES
    unites_Bp: int = 9               # B′ : unités de chaque moniteur entraîné (classe du moniteur final de D, T + 1)
    audit_departs: int = 100         # attaquant indépendant : départs tirés (plus 12 départs structurés et les passés)
    audit_n_mc: int = 1024           # attaquant indépendant : échantillons de Monte-Carlo par composante
    audit_iter: int = 300            # attaquant indépendant : itérations SLSQP
    audit_es_generations: int = 400  # attaquant indépendant : générations de la stratégie d'évolution (1 + λ)
    audit_es_lambda: int = 12        # attaquant indépendant : descendants par génération
    audit_critere: float = 0.05      # artefact si un contraste change de signe ou de plus de ce seuil (S17)

    def canonique(self) -> bytes:
        return json.dumps(asdict(self), sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()

    def empreinte(self) -> str:
        return hashlib.sha256(self.canonique()).hexdigest()


CONFIG_BASE_V3 = Config()
CONFIG_V3 = replace(CONFIG_BASE_V3, deltas=tuple(DELTAS_V3)) if DELTAS_V3 is not None else None


def exiger_config(cfg: Config) -> Config:
    """Garde : configuration cohérente avant toute exécution."""
    if cfg is None or not cfg.deltas:
        raise GardeArret("δ non fixés : lancer le calibrage et appliquer `choisir_deltas` d'abord")
    if any(not d > 0 for d in cfg.deltas) or list(cfg.deltas) != sorted(set(cfg.deltas)):
        raise GardeArret(f"δ invalides (positifs, strictement croissants exigés) : {cfg.deltas}")
    for nom in ("n_attaque_entr", "n_eval", "n_eval_tenue"):
        if getattr(cfg, nom) % cfg.K:
            raise GardeArret(f"configuration : {nom} = {getattr(cfg, nom)} n'est pas un multiple de K = {cfg.K}")
    if not 0 < cfg.kappa_contournement < 1:
        raise GardeArret(f"κ de contournement hors de ]0 ; 1[ : {cfg.kappa_contournement}")
    fr = list(cfg.fractions_courbe)
    if not fr or fr != sorted(set(fr)) or fr[0] <= 0 or fr[-1] >= 1:
        raise GardeArret(f"fractions de la courbe invalides : {cfg.fractions_courbe}")
    if cfg.entrainement not in ("detection", "logistique"):
        raise GardeArret(f"entraînement inconnu (configuration) : {cfg.entrainement!r}")
    if cfg.unites_Bp < 2:
        raise GardeArret(f"B′ sans moniteurs non linéaires : unites_Bp = {cfg.unites_Bp} (au moins 2 exigé, sinon B′ = B)")
    if min(cfg.audit_departs, cfg.audit_n_mc, cfg.audit_iter, cfg.audit_es_generations, cfg.audit_es_lambda) < 1 or \
            not cfg.audit_critere > 0:
        raise GardeArret("attaquant indépendant : paramètres non positifs dans la configuration")
    return cfg


# =================================================================================================================
# Graines, racines et autorisation de décision
# =================================================================================================================
_AUTORISATION_DECISION: dict = {"prereg_sha256": None}


def gen(racine: int, *cle: int) -> np.random.Generator:
    """Générateur dérivé (R9). Garde : une racine de décision exige l'autorisation par préenregistrement scellé."""
    exiger_numpy_minimal()
    if int(racine) in RACINES_DECISION and _AUTORISATION_DECISION["prereg_sha256"] is None:
        raise GardeArret(f"racine de décision {racine} sans autorisation : préenregistrement scellé exigé "
                         "(autoriser_decision)")
    return np.random.default_rng(np.random.SeedSequence(entropy=int(racine), spawn_key=tuple(int(c) for c in cle)))


def exiger_racines_essai(racine: int, racine_tenue: int) -> None:
    """Garde : hors décision, aucune racine de décision ni racine d'essai déjà employée ; racine des tenues à part."""
    for r in (racine, racine_tenue):
        if int(r) in RACINES_DECISION:
            raise GardeArret(f"racine {r} réservée à la décision : interdite hors décision (préenregistrement scellé "
                             "exigé)")
        if int(r) in RACINES_DEJA_EMPLOYEES:
            raise GardeArret(f"racine {r} déjà employée (brouillon 1, v2 ou contre-lecture 2) : conception choisie ou "
                             "résultats lus dessus, interdite en v3")
    if racine == racine_tenue:
        raise GardeArret("racine des familles tenues à l'écart égale à la racine principale : racine à part exigée")


def empreinte_fichier(chemin: str | Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


DEBUT_CONFIG = "<!-- configuration-canonique-debut -->"
FIN_CONFIG = "<!-- configuration-canonique-fin -->"


def bloc_identite(cfg: Config) -> str:
    """Texte à recopier tel quel dans le préenregistrement : identité, empreintes, versions, configuration canonique."""
    import scipy

    lignes = [f"- Identifiant : {IDENTIFIANT_PREREG}",
              f"- Racines de décision : RACINE = {RACINE} ; RACINE_TENUE = {RACINE_TENUE}",
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


def exiger_identite_prereg(texte: str, cfg: Config, instances: str | None = None) -> None:
    """Garde : le préenregistrement est celui de cette arène, avec les racines, la configuration (champ à champ),
    les empreintes du code et de la bibliothèque, les versions du code, et le nombre d'instances (S4)."""
    import scipy

    if IDENTIFIANT_PREREG not in texte:
        raise GardeArret(f"préenregistrement sans l'identifiant {IDENTIFIANT_PREREG} : ce n'est pas celui de l'arène")
    for nom, val in (("RACINE", RACINE), ("RACINE_TENUE", RACINE_TENUE)):
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
        raise GardeArret(f"--instances {instances} ≠ 0:{cfg.n_instances} (S4, configuration gelée)")


def exiger_prereg_arene(chemin: str | Path, cfg: Config, instances: str | None = None) -> str:
    """Avant toute exécution sur RACINE : préenregistrement conforme, scellé, intact, et identifié (R1)."""
    from controle_ia.prereg import exiger_prereg_scelle

    sha = exiger_prereg_scelle(chemin)
    exiger_identite_prereg(Path(chemin).read_text(encoding="utf-8"), cfg, instances)
    return sha


def autoriser_decision(chemin: str | Path, cfg: Config, instances: str | None = None) -> str:
    sha = exiger_prereg_arene(chemin, cfg, instances)
    _AUTORISATION_DECISION["prereg_sha256"] = sha
    return sha


# =================================================================================================================
# Lois : mélanges gaussiens à poids égaux, covariances diagonales
# =================================================================================================================
def vecteur(mu: np.ndarray, sig: np.ndarray) -> np.ndarray:
    return np.concatenate([mu.ravel(), sig.ravel()])


def deplier(theta: np.ndarray, cfg: Config) -> tuple[np.ndarray, np.ndarray]:
    n = cfg.K * cfg.d
    return theta[:n].reshape(cfg.K, cfg.d), theta[n:].reshape(cfg.K, cfg.d)


def bornes(cfg: Config) -> list[tuple[float, float]]:
    n = cfg.K * cfg.d
    return [(-cfg.boite_mu, cfg.boite_mu)] * n + [(cfg.sigma_min, cfg.sigma_max)] * n


def distance(theta: np.ndarray, cible: np.ndarray, cfg: Config) -> float:
    """Distance de comportement : racine de la moyenne sur k de W2² entre composantes appariées (diagonales)."""
    return float(np.sqrt(np.sum((theta - cible) ** 2) / cfg.K))


def exiger_admissible(theta: np.ndarray, cible: np.ndarray, delta: float, cfg: Config) -> None:
    if not np.all(np.isfinite(theta)):
        raise GardeArret("loi d'attaque non finie")
    lo = np.array([b[0] for b in bornes(cfg)])
    hi = np.array([b[1] for b in bornes(cfg)])
    if np.any(theta < lo - 1e-9) or np.any(theta > hi + 1e-9):
        raise GardeArret("loi d'attaque hors de la boîte")
    if distance(theta, cible, cfg) > delta * (1 + 1e-9) + 1e-12:
        raise GardeArret(f"loi d'attaque à distance {distance(theta, cible, cfg):.6f} > δ = {delta}")


def projeter(theta: np.ndarray, cible: np.ndarray, delta: float, cfg: Config) -> tuple[np.ndarray, bool]:
    """Projection déclarée (contrainte puis boîte) ; renvoie aussi si elle a bougé le point (compté, jamais tu)."""
    v = theta - cible
    dist = distance(theta, cible, cfg)
    if dist > delta:
        v = v * (delta / dist)
    lo = np.array([b[0] for b in bornes(cfg)])
    hi = np.array([b[1] for b in bornes(cfg)])
    p = np.clip(cible + v, lo, hi)
    bouge = bool(np.max(np.abs(p - theta)) > 1e-6)   # en deçà : tolérance numérique de SLSQP, non comptée
    exiger_admissible(p, cible, delta, cfg)
    return p, bouge


def echantillonner(theta: np.ndarray, n: int, rng: np.random.Generator, cfg: Config) -> np.ndarray:
    if n % cfg.K:
        raise GardeArret(f"n = {n} non multiple de K = {cfg.K} : échantillonnage stratifié impossible")
    mu, sig = deplier(theta, cfg)
    z = rng.standard_normal((cfg.K, n // cfg.K, cfg.d))
    return (mu[:, None, :] + sig[:, None, :] * z).reshape(n, cfg.d)


def loi_cible(instance: int, racine: int, cfg: Config) -> np.ndarray:
    g = gen(racine, COMMUN, instance, COMMUN, 0, ROLE_CIBLE)
    u = g.standard_normal((cfg.K, cfg.d))
    u /= np.linalg.norm(u, axis=1, keepdims=True)
    return vecteur(cfg.r_cible * u, np.full((cfg.K, cfg.d), cfg.sigma_cible))


def depart_tire_vers_l_origine(cible: np.ndarray, delta: float, cfg: Config) -> np.ndarray:
    mu, sig = deplier(cible, cfg)
    n = np.linalg.norm(mu, axis=1, keepdims=True)
    return projeter(vecteur(mu * (1 - np.minimum(delta / n, 1.0)), sig), cible, delta, cfg)[0]


# =================================================================================================================
# Moniteurs
# =================================================================================================================
class Moniteur:
    """Score « maxout » : log-somme-exp de m scores linéaires (m = 1 : linéaire). Seuil t calibré à α sur le propre."""

    def __init__(self, W: np.ndarray, b: np.ndarray):
        W = np.atleast_2d(np.asarray(W, float))
        b = np.atleast_1d(np.asarray(b, float))
        if not (np.all(np.isfinite(W)) and np.all(np.isfinite(b))):
            raise GardeArret("paramètres de moniteur non finis")
        self.W, self.b = W, b
        self.t = np.nan
        self.e = np.nan
        self._cache: dict = {}

    @property
    def m(self) -> int:
        return self.W.shape[0]

    @property
    def nb_parametres(self) -> int:
        return int(self.W.size + self.b.size)

    def score(self, X: np.ndarray) -> np.ndarray:
        a = X @ self.W.T + self.b
        return a[:, 0] if self.m == 1 else logsumexp(a, axis=1)

    def grad(self, X: np.ndarray) -> np.ndarray:
        if self.m == 1:
            return np.broadcast_to(self.W[0], X.shape)
        return softmax(X @ self.W.T + self.b, axis=1) @ self.W

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
        """Taux de détection sur un ensemble d'évaluation identifié par `cle` (mémorisé)."""
        if cle not in self._cache:
            self._cache[cle] = float(np.mean(self.detecte(X_fournisseur())))
        return self._cache[cle]


def ou_deterministe(moniteurs: list[Moniteur], Xcal: np.ndarray, lam: float, alpha: float) -> Moniteur:
    """C3 : « ou » déterministe de moniteurs linéaires. Chaque score est standardisé sur le propre de calibration
    (z_i = (s_i − μ_i)/σ_i), multiplié par λ ; le moniteur rendu a pour score log-somme-exp_i(λ z_i), proche de
    λ max_i z_i (écart ≤ log(m)), seuil recalibré à α. Même nombre de paramètres que le mélange des moniteurs."""
    W, b = [], []
    for mon in moniteurs:
        if mon.m != 1:
            raise GardeArret("« ou » déterministe : moniteurs linéaires exigés")
        s = mon.score(Xcal)
        mu, sd = float(np.mean(s)), float(np.std(s))
        if not (np.isfinite(mu) and sd > 0):
            raise GardeArret("« ou » déterministe : score propre de variance nulle ou non fini")
        W.append(lam * mon.W[0] / sd)
        b.append(lam * (mon.b[0] - mu) / sd)
    return Moniteur(np.stack(W), np.array(b)).calibrer(Xcal, alpha)


class MoniteurOu(Moniteur):
    """C3′ : « ou » déterministe de moniteurs quelconques (linéaires ou maxout). Score log-somme-exp_i(λ z_i), z_i =
    (s_i − μ_i)/σ_i standardisé sur le propre de calibration ; même interface que `Moniteur` (score, gradient, seuil,
    taux). Sur des moniteurs linéaires, c'est la même fonction que `ou_deterministe` (essai). Paramètres : la somme de
    ceux des membres (la standardisation n'en ajoute pas : μ_i, σ_i sont absorbés comme dans `ou_deterministe`)."""

    def __init__(self, membres: list[Moniteur], Xcal: np.ndarray, lam: float):
        if not membres:
            raise GardeArret("« ou » composite : aucun moniteur")
        self.membres, self.lam = list(membres), float(lam)
        self.mu, self.sd = [], []
        for mon in self.membres:
            s = mon.score(Xcal)
            mu, sd = float(np.mean(s)), float(np.std(s))
            if not (np.isfinite(mu) and sd > 0):
                raise GardeArret("« ou » composite : score propre de variance nulle ou non fini")
            self.mu.append(mu)
            self.sd.append(sd)
        self.W = np.vstack([m.W for m in self.membres])     # pour l'inventaire des paramètres seulement
        self.b = np.concatenate([m.b for m in self.membres])
        self.t = np.nan
        self.e = np.nan
        self._cache = {}

    def _z(self, X):
        return np.stack([self.lam * (m.score(X) - mu) / sd for m, mu, sd in zip(self.membres, self.mu, self.sd)],
                        axis=1)

    def score(self, X: np.ndarray) -> np.ndarray:
        return logsumexp(self._z(X), axis=1)

    def grad(self, X: np.ndarray) -> np.ndarray:
        S = softmax(self._z(X), axis=1)
        return sum(S[:, [i]] * (self.lam / sd) * m.grad(X) for i, (m, sd) in enumerate(zip(self.membres, self.sd)))


def ou_composite(moniteurs: list[Moniteur], Xcal: np.ndarray, lam: float, alpha: float) -> MoniteurOu:
    return MoniteurOu(moniteurs, Xcal, lam).calibrer(Xcal, alpha)


def _somme_ponderee(X: np.ndarray, S: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Σ_i w_i ∂s(x_i)/∂(W, b) pour un score maxout (S = poids softmax des unités ; m = 1 : S = 1)."""
    G = w[:, None] * S
    return np.concatenate([(G.T @ X).ravel(), G.sum(0)])


def _scores(p: np.ndarray, X: np.ndarray, m: int):
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
    """Taux de détection lissé au seuil α, seuil approché par moyenne + z_{1−α} × écart-type des scores propres
    (exact en population pour un moniteur linéaire, la loi propre étant N(0, I) ; approché pour m > 1, au détriment
    de D). Renvoie (−J, −∇J)."""
    z = norm.ppf(1 - cfg.alpha)
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


def entrainer(Xp: np.ndarray, Xa: np.ndarray, m: int, cfg: Config, rng_init: np.random.Generator | None,
              directions=()):
    """Entraîne un moniteur à m unités (m = 1 : linéaire). Renvoie (moniteur, convergé).

    - `entrainement = "logistique"` : régression logistique (départ nul si m = 1, départ tiré si m > 1) ;
    - `entrainement = "detection"` (défaut) : oracle qui maximise le taux de détection lissé au seuil α ; départs
      déterministes = solution logistique, puis (m = 1) les directions des moyennes de composantes des lois
      d'entraînement, par poids décroissant, jusqu'à `departs_entr` départs ; (m > 1) une seconde initialisation dont
      les unités sont ces directions. Le meilleur départ (objectif d'entraînement) est retenu.
    """
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
    if cfg.entrainement == "logistique":
        return Moniteur(res.x[: m * d].reshape(m, d), res.x[m * d:]), bool(res.success)
    if cfg.entrainement != "detection":
        raise GardeArret(f"entraînement inconnu : {cfg.entrainement!r}")
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
    return Moniteur(meilleur.x[: m * d].reshape(m, d), meilleur.x[m * d:]), bool(meilleur.success)


# =================================================================================================================
# Défense mixte et jeu à somme nulle
# =================================================================================================================
def exiger_poids(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, float)
    if not np.all(np.isfinite(p)) or np.any(p < -1e-9) or abs(p.sum() - 1) > 1e-6:
        raise GardeArret(f"poids de mélange invalides : {p}")
    p = np.clip(p, 0, None)
    return p / p.sum()


def taux_defense(defense, X: np.ndarray) -> float:
    return float(sum(p * np.mean(m.detecte(X)) for m, p in defense if p > 0))


def resoudre_jeu(G: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Jeu à somme nulle : lignes = moniteurs (maximisent la détection), colonnes = attaques. Renvoie (p, q, valeur).
    Équilibres non uniques : le sommet rendu est celui du solveur HiGHS (déterministe à version de scipy fixée,
    consignée au manifeste) ; aucune règle de choix entre équilibres (déclaré)."""
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


# =================================================================================================================
# Attaquant : meilleure réponse dans la boîte, sous la contrainte de comportement
# =================================================================================================================
def objectif_lisse(theta, defense, z, cfg: Config):
    mu, sig = deplier(theta, cfg)
    K, n, d = z.shape
    X = (mu[:, None, :] + sig[:, None, :] * z).reshape(K * n, d)
    total, gmu, gsig = 0.0, np.zeros((K, d)), np.zeros((K, d))
    for m, p in defense:
        if p <= 0:
            continue
        u = (m.score(X) - m.t) / (cfg.tau * m.e)
        sg = expit(u)
        total += p * sg.mean()
        ds = p * sg * (1 - sg) / (cfg.tau * m.e) / (K * n)
        G = (m.grad(X) * ds[:, None]).reshape(K, n, d)
        gmu += G.sum(1)
        gsig += (G * z).sum(1)
    return total, vecteur(gmu, gsig)


def taux_dur(theta, defense, z, cfg: Config) -> float:
    mu, sig = deplier(theta, cfg)
    K, n, d = z.shape
    return taux_defense(defense, (mu[:, None, :] + sig[:, None, :] * z).reshape(K * n, d))


def meilleure_reponse(defense, cible, delta, cfg: Config, rng_mc, rng_departs, departs_suppl=(), n_departs=None,
                      n_mc=None, iter_max=None) -> tuple[np.ndarray, dict]:
    """Meilleure réponse approchée (SLSQP, plusieurs départs). Consigne le statut et les itérations de chaque départ ;
    un départ au point non fini est compté (garde de taux par tâche), jamais sauté en silence."""
    n_departs = cfg.departs if n_departs is None else n_departs
    iter_max = cfg.iter_max if iter_max is None else iter_max
    z = rng_mc.standard_normal((cfg.K, cfg.n_mc if n_mc is None else n_mc, cfg.d))
    departs = [depart_tire_vers_l_origine(cible, delta, cfg)]
    for _ in range(n_departs):
        v = rng_departs.standard_normal(cible.size)
        v *= np.sqrt(cfg.K) * delta * rng_departs.uniform(0.5, 1.0) / np.linalg.norm(v)
        departs.append(projeter(cible + v, cible, delta, cfg)[0])
    departs += [projeter(np.asarray(s, float), cible, delta, cfg)[0] for s in departs_suppl]
    contrainte = {"type": "ineq",
                  "fun": lambda th: delta ** 2 - np.sum((th - cible) ** 2) / cfg.K,
                  "jac": lambda th: -2 * (th - cible) / cfg.K}
    meilleur, n_proj, non_finis, statuts, it_max = None, 0, 0, Counter(), 0
    for x0 in departs:
        res = minimize(objectif_lisse, x0, args=(defense, z, cfg), jac=True, method="SLSQP", bounds=bornes(cfg),
                       constraints=[contrainte], options={"maxiter": iter_max, "ftol": 1e-7})
        statuts[int(res.status)] += 1
        it_max = max(it_max, int(getattr(res, "nit", 0)))
        if not np.all(np.isfinite(res.x)):
            non_finis += 1
            continue
        th, bouge = projeter(res.x, cible, delta, cfg)
        n_proj += bouge
        cand = (taux_dur(th, defense, z, cfg), objectif_lisse(th, defense, z, cfg)[0], th)
        if meilleur is None or cand[:2] < meilleur[:2]:
            meilleur = cand
    if meilleur is None:
        raise GardeArret("meilleure réponse : aucun départ n'a donné de point fini")
    exiger_admissible(meilleur[2], cible, delta, cfg)
    return meilleur[2], {"projections": n_proj, "departs": len(departs), "non_finis": non_finis,
                         "statuts": {str(k): v for k, v in sorted(statuts.items())}, "iter_max": it_max,
                         "limite_iter": iter_max, "distance_consommee": distance(meilleur[2], cible, cfg)}


def exiger_departs_finis(non_finis: int, total: int, cfg: Config) -> None:
    if total and non_finis / total > cfg.taux_departs_non_finis_max:
        raise GardeArret(f"départs de l'attaquant au point non fini : {non_finis}/{total} > "
                         f"{cfg.taux_departs_non_finis_max}")


# =================================================================================================================
# Familles tenues à l'écart (racine à part)
# =================================================================================================================
def lois_tenues(cible, delta, instance, code_delta, racine_tenue, cfg: Config) -> list[np.ndarray]:
    g = gen(racine_tenue, code_delta, instance, COMMUN, 0, ROLE_TENUE_LOIS)
    sortie = []
    for j in range(cfg.n_tenue):
        if j % 2 == 0:  # sous-famille 1 : déplacement aléatoire dans la boule de comportement
            v = g.standard_normal(cible.size)
            v *= np.sqrt(cfg.K) * delta * g.uniform(0.5, 1.0) / np.linalg.norm(v)
        else:           # sous-famille 2 : tout le budget sur une composante, tirée vers l'origine, échelle tirée
            mu, sig = deplier(cible, cfg)
            k = int(g.integers(cfg.K))
            dmu, dsig = np.zeros_like(mu), np.zeros_like(sig)
            dmu[k] = -mu[k] / np.linalg.norm(mu[k])
            dsig[k] = g.uniform(-1, 1, cfg.d)
            v = vecteur(dmu, dsig)
            v *= np.sqrt(cfg.K) * delta * g.uniform(0.5, 1.0) / np.linalg.norm(v)
        sortie.append(projeter(cible + v, cible, delta, cfg)[0])
    return sortie


# =================================================================================================================
# Une tâche = (δ, instance)
# =================================================================================================================
class Contexte:
    def __init__(self, instance, code_delta, racine, racine_tenue, cfg: Config):
        self.i, self.cd, self.r, self.rt, self.cfg = instance, code_delta, racine, racine_tenue, cfg
        self.delta = cfg.deltas[code_delta - 1]
        self.cible = loi_cible(instance, racine, cfg)
        self.Xcal = gen(racine, code_delta, instance, COMMUN, 0, ROLE_CAL).standard_normal((cfg.n_cal, cfg.d))
        self.Xfpr = gen(racine, code_delta, instance, COMMUN, 0, ROLE_FPR).standard_normal((cfg.n_fpr, cfg.d))
        self.tenues = lois_tenues(self.cible, self.delta, instance, code_delta, racine_tenue, cfg)
        self._Xt = None
        self.nonconv = 0
        self.entr = 0
        self.att = {"departs": 0, "non_finis": 0, "statuts": Counter(), "iter_max": 0, "a_la_limite": 0}

    def g(self, bras, tour, role, *extra):
        return gen(self.r, self.cd, self.i, bras, tour, role, *extra)

    def X_tenues(self):
        if self._Xt is None:
            g = gen(self.rt, self.cd, self.i, COMMUN, 0, ROLE_TENUE_EVAL)
            self._Xt = [echantillonner(th, self.cfg.n_eval_tenue, g, self.cfg) for th in self.tenues]
        return self._Xt

    def propre_entr(self, tour):
        return self.g(COMMUN, tour, ROLE_PROPRE_ENTR).standard_normal((self.cfg.n_propre_entr, self.cfg.d))

    def meilleure_reponse(self, defense, delta, rng_mc, rng_departs, **kw):
        th, info = meilleure_reponse(defense, self.cible, delta, self.cfg, rng_mc, rng_departs, **kw)
        self.att["departs"] += info["departs"]
        self.att["non_finis"] += info["non_finis"]
        self.att["statuts"].update({int(k): v for k, v in info["statuts"].items()})
        self.att["iter_max"] = max(self.att["iter_max"], info["iter_max"])
        self.att["a_la_limite"] += int(info["iter_max"] >= info["limite_iter"])
        return th, info

    def entrainer(self, bras, tour, attaques, q, m):
        """Moniteur entraîné sur le propre du tour (commun aux bras) contre le mélange q des attaques."""
        cfg = self.cfg
        q = exiger_poids(q)
        n = cfg.n_attaque_entr // cfg.K
        comptes = np.floor(q * n).astype(int)
        reste = n - comptes.sum()
        comptes[np.argsort(-(q * n - comptes), kind="stable")[:reste]] += 1
        g = self.g(bras, tour, ROLE_ATTAQUE_ENTR)
        Xa = np.vstack([echantillonner(a, cfg.K * c, g, cfg) for a, c in zip(attaques, comptes) if c > 0])
        init = self.g(bras, tour, ROLE_INIT_MAXOUT) if m > 1 else None
        dirs = []
        for j in np.argsort(-q, kind="stable"):
            if q[j] <= 0:
                continue
            mu, _ = deplier(attaques[j], cfg)
            dirs += [v / np.linalg.norm(v) for v in mu if np.linalg.norm(v) > 1e-12]
        mon, ok = entrainer(self.propre_entr(tour), Xa, m, cfg, init, dirs)
        self.entr += 1
        self.nonconv += (not ok)
        return mon.calibrer(self.Xcal, cfg.alpha)

    def exiger_fpr(self, defense) -> float:
        f = taux_defense(defense, self.Xfpr)
        if abs(f - self.cfg.alpha) > self.cfg.tol_fpr:
            raise GardeArret(f"taux de fausses alertes mesuré {f:.4f} hors de α ± {self.cfg.tol_fpr}")
        return f

    def taux_tenues(self, defense) -> list[float]:
        Xt = self.X_tenues()
        return [float(sum(p * m.taux_cache(("tenue", j), lambda j=j: Xt[j]) for m, p in defense if p > 0))
                for j in range(len(Xt))]


def residu_relatif(v: np.ndarray, passes: list[np.ndarray]) -> float:
    """Nouveauté résiduelle (piste 4) : norme du résidu de v après projection sur l'espace des déplacements passés."""
    nv = np.linalg.norm(v)
    if nv == 0:
        return 0.0
    if not passes:
        return 1.0
    B = np.stack(passes, axis=1)
    coef, *_ = np.linalg.lstsq(B, v, rcond=None)
    return float(np.linalg.norm(v - B @ coef) / nv)


def courbe_detection(defense, ctx: Contexte, code_bras: int, passes) -> tuple[float, list[float]]:
    """Courbe V(δ') (piste 5, sans censure) : détection de la cible non modifiée (δ' = 0, ligne de base), puis de la
    meilleure réponse (départs du coût + attaques passées projetées) aux fractions `fractions_courbe` de δ."""
    cfg = ctx.cfg
    base = taux_defense(defense, echantillonner(ctx.cible, cfg.n_eval, ctx.g(code_bras, 99, ROLE_COURBE, 0, 1), cfg))
    pts = []
    for j, f in enumerate(cfg.fractions_courbe, start=1):
        dp = f * ctx.delta
        th, _ = ctx.meilleure_reponse(defense, dp, ctx.g(code_bras, 99, ROLE_COURBE, j, 2),
                                      ctx.g(code_bras, 99, ROLE_COURBE, j, 3),
                                      departs_suppl=[projeter(s, ctx.cible, dp, cfg)[0] for s in passes],
                                      n_departs=cfg.departs_cout)
        pts.append(taux_defense(defense, echantillonner(th, cfg.n_eval, ctx.g(code_bras, 99, ROLE_COURBE, j, 4), cfg)))
    return base, pts


def cout_contournement(defense, ctx: Contexte, code_bras: int, passes, base: float, pts: list[float],
                       V: float) -> dict:
    """Coût par contournement (piste 5), seuil RELATIF : contourné à δ' si la détection est ≤ κ × détection de la cible
    non modifiée (ligne de base). Garde de ligne de base : si κ × base < 2α, le contournement n'est pas
    distinguable du bruit des fausses alertes : mesure « non définie » pour ce bras et cette tâche (comptée, rapportée,
    jamais remplacée). Sinon : premier point de la courbe (0, fractions, 1) sous le seuil ; censuré à 1 si aucun ;
    puis bissection (`pas_bissection` pas) dans l'intervalle qui l'encadre. La monotonie de la courbe n'est pas
    supposée : les hausses de plus de α entre points consécutifs sont comptées."""
    cfg = ctx.cfg
    seuil = cfg.kappa_contournement * base
    fr = (0.0,) + tuple(cfg.fractions_courbe) + (1.0,)
    vals = [base] + list(pts) + [V]
    non_monotone = int(sum(vals[k] > vals[k - 1] + cfg.alpha for k in range(1, len(vals))))
    r = {"ligne_de_base": base, "seuil": seuil, "non_monotone": non_monotone}
    if seuil < 2 * cfg.alpha:
        return {**r, "defini": False, "censure": None, "fraction": None}
    k = next((k for k in range(1, len(vals)) if vals[k] <= seuil), None)
    if k is None:
        return {**r, "defini": True, "censure": True, "fraction": 1.0}
    lo, hi = fr[k - 1] * ctx.delta, fr[k] * ctx.delta
    for s in range(1, cfg.pas_bissection + 1):
        mid = (lo + hi) / 2
        th, _ = ctx.meilleure_reponse(defense, mid, ctx.g(code_bras, 99, ROLE_COUT, s, 2),
                                      ctx.g(code_bras, 99, ROLE_COUT, s, 3),
                                      departs_suppl=[projeter(x, ctx.cible, mid, cfg)[0] for x in passes],
                                      n_departs=cfg.departs_cout)
        t = taux_defense(defense, echantillonner(th, cfg.n_eval, ctx.g(code_bras, 99, ROLE_COUT, s, 4), cfg))
        if t <= seuil:
            hi = mid
        else:
            lo = mid
    return {**r, "defini": True, "censure": False, "fraction": hi / ctx.delta, "encadrement": [fr[k - 1], fr[k]]}


def indicateurs_cycle(H: np.ndarray, iii: list[float], deplacements: list[np.ndarray]) -> dict:
    """Condition d'application de la piste 3 (CM2-03) à partir de la matrice de détection croisée H, ligne s =
    moniteur du tour s (0 … T), colonne t − 1 = attaque du tour t (1 … T) :
    - I1, progrès : moyenne de (iii) sur la seconde moitié des tours moins la première (≈ 0 : exploitabilité plate) ;
    - I2, oubli : moyenne sur t = 1 … T − 1 de H[t, t] − H[T, t] (détection de l'attaque du tour t juste après
      l'entraînement sur elle, moins celle du moniteur final) ;
    - rétention par décalage k = 0 … 3 : moyenne de H[t + k, t] ; décalage −1 : H[t − 1, t] = (iii) du tour t ;
    - I3, retours : part des tours t ≥ 3 où le déplacement de l'attaque est plus proche (cosinus) d'une attaque
      d'un tour s ≤ t − 2 que de celle du tour t − 1."""
    T = H.shape[1]
    h = T // 2
    I1 = float(np.mean(iii[h:]) - np.mean(iii[:h]))
    I2 = float(np.mean([H[t, t - 1] - H[T, t - 1] for t in range(1, T)]))
    ret = {str(k): float(np.mean([H[t + k, t - 1] for t in range(1, T + 1) if t + k <= T])) for k in range(0, 4)}
    ret["-1"] = float(np.mean([H[t - 1, t - 1] for t in range(1, T + 1)]))
    retours = []
    for t in range(3, T + 1):
        v = deplacements[t - 1]
        cs = [float(v @ deplacements[s - 1] / (np.linalg.norm(v) * np.linalg.norm(deplacements[s - 1]) + 1e-300))
              for s in range(1, t)]
        retours.append(max(cs[:-1]) > cs[-1])
    return {"I1_progres": I1, "I2_oubli": I2, "retention": ret, "I3_retours": float(np.mean(retours)) if retours
            else None, "H": [[float(x) for x in ligne] for ligne in H]}


def trajectoire(nom: str, ctx: Contexte, M0: Moniteur, leger: bool = False) -> dict:
    """Trajectoire coévolutive d'un bras A, B, D ou B′. Renvoie l'état final (moniteurs, défense finale, attaques…)."""
    if nom not in BRAS_TRAJECTOIRE:
        raise GardeArret(f"bras sans trajectoire : {nom!r}")
    cfg, cb = ctx.cfg, BRAS[nom]
    melange = nom in ("B", "Bp")
    t0 = time.process_time()
    attaques = [ctx.cible]
    moniteurs = [M0]
    historique = [M0]                   # tous les moniteurs déployés, tour par tour (D n'en déploie qu'un)
    cles_eval = [("eval", COMMUN, 0)]
    eval_X = {cles_eval[0]: lambda: echantillonner(ctx.cible, cfg.n_eval, ctx.g(COMMUN, 0, ROLE_EVAL), cfg)}
    G = np.array([[M0.taux_cache(cles_eval[0], eval_X[cles_eval[0]])]]) if melange else None
    p = np.array([1.0])
    par_tour = {"iii": [], "ii": [], "poids_max": [], "distance": [], "nouveaute": [], "projections": [], "cpu_s": []}
    deplacements: list[np.ndarray] = []

    def defense_courante():
        if nom in ("A", "D"):
            return [(moniteurs[-1], 1.0)]
        return list(zip(moniteurs, p))

    for t in range(1, cfg.T + 1):
        tt = time.process_time()
        if melange:
            p, _, _ = resoudre_jeu(G)
        dfs = defense_courante()
        a, info = ctx.meilleure_reponse(dfs, ctx.delta, ctx.g(cb, t, ROLE_MC), ctx.g(cb, t, ROLE_DEPARTS),
                                        departs_suppl=[attaques[-1]])
        cle = ("eval", cb, t)
        eval_X[cle] = (lambda a=a, t=t: echantillonner(a, cfg.n_eval, ctx.g(cb, t, ROLE_EVAL), cfg))
        par_tour["iii"].append(taux_defense(dfs, eval_X[cle]()))
        if not leger:
            par_tour["ii"].append(float(np.mean(ctx.taux_tenues(dfs))))
        par_tour["poids_max"].append(float(max(w for _, w in dfs)))
        par_tour["distance"].append(info["distance_consommee"])
        par_tour["projections"].append(info["projections"])
        v = a - ctx.cible
        par_tour["nouveaute"].append(residu_relatif(v, deplacements))
        deplacements.append(v)
        attaques.append(a)
        cles_eval.append(cle)
        if melange:
            col = np.array([[m.taux_cache(cle, eval_X[cle]) for m in moniteurs]]).T
            G = np.hstack([G, col])
            _, q, _ = resoudre_jeu(G)
            mon = ctx.entrainer(cb, t, attaques, q, 1 if nom == "B" else cfg.unites_Bp)   # B′ : maxout, classe de D
            ligne = np.array([[mon.taux_cache(c, eval_X[c]) for c in cles_eval]])
            G = np.vstack([G, ligne])
        else:
            m_unites = t + 1 if nom == "D" else 1   # D : autant d'unités que de moniteurs dans le mélange de B
            mon = ctx.entrainer(cb, t, attaques, np.full(len(attaques), 1.0 / len(attaques)), m_unites)
        if nom == "D":
            moniteurs = [mon]
        else:
            moniteurs.append(mon)
        historique.append(mon)
        par_tour["cpu_s"].append(time.process_time() - tt)
        exiger_plafond(t0, cfg, f"bras {nom}, tour {t}")
    valeur_restreinte = None
    if melange:
        p, _, valeur_restreinte = resoudre_jeu(G)
    H = np.array([[mon.taux_cache(c, eval_X[c]) for c in cles_eval[1:]] for mon in historique])
    cycle = indicateurs_cycle(H, par_tour["iii"], deplacements)
    return {"nom": nom, "moniteurs": moniteurs, "defense_finale": defense_courante(), "attaques": attaques,
            "cles_eval": cles_eval, "eval_X": eval_X, "par_tour": par_tour, "valeur_jeu_restreint": valeur_restreinte,
            "cycle": cycle, "cpu_trajectoire_s": time.process_time() - t0}


def defense_temoin(nom: str, etat_source: dict, ctx: Contexte) -> list:
    """Témoins « finale seulement » sur les moniteurs mêmes de leur source après le tour T (B pour C1, C2, C3 ; B′ pour
    C3′)."""
    mons = etat_source["moniteurs"]
    if nom == "C1":
        return [(m, 1.0 / len(mons)) for m in mons]
    if nom == "C2":
        w = exiger_poids(ctx.g(BRAS["C2"], ctx.cfg.T + 1, ROLE_DIRICHLET).dirichlet(np.ones(len(mons))))
        return list(zip(mons, w))
    if nom == "C3":
        return [(ou_deterministe(mons, ctx.Xcal, ctx.cfg.lambda_ou, ctx.cfg.alpha), 1.0)]
    if nom == "C3p":
        return [(ou_composite(mons, ctx.Xcal, ctx.cfg.lambda_ou, ctx.cfg.alpha), 1.0)]
    raise GardeArret(f"témoin inconnu : {nom!r}")


def phase_finale(nom: str, dfin, ctx: Contexte, etat: dict, leger: bool = False, rendre_attaques: bool = False):
    """Défense figée ; l'attaquant joue en dernier (standard puis renforcé ; (iii) = la plus basse des deux
    détections, biais d'au plus un écart d'échantillonnage en faveur de l'attaquant, déclaré)."""
    cfg, cb = ctx.cfg, BRAS[nom]
    tf = time.process_time()
    T1 = cfg.T + 1
    passes = etat["attaques"][1:]
    fpr = ctx.exiger_fpr(dfin)
    a_fin, i_fin = ctx.meilleure_reponse(dfin, ctx.delta, ctx.g(cb, T1, ROLE_FINAL, 1), ctx.g(cb, T1, ROLE_FINAL, 2),
                                         departs_suppl=passes, n_departs=cfg.departs_final, n_mc=cfg.n_mc_final)
    V_std = taux_defense(dfin, echantillonner(a_fin, cfg.n_eval, ctx.g(cb, T1, ROLE_FINAL, 3), cfg))
    a_renf, i_renf = ctx.meilleure_reponse(dfin, ctx.delta, ctx.g(cb, T1, ROLE_FINAL, 4), ctx.g(cb, T1, ROLE_FINAL, 5),
                                           departs_suppl=passes + [a_fin], n_departs=cfg.departs_renforce,
                                           n_mc=cfg.n_mc_final, iter_max=cfg.iter_renforce)
    V_renf = taux_defense(dfin, echantillonner(a_renf, cfg.n_eval, ctx.g(cb, T1, ROLE_FINAL, 6), cfg))
    V = min(V_std, V_renf)
    sortie = {"V_iii_final": V, "V_iii_standard": V_std, "V_iii_renforce": V_renf, "fpr_final": fpr,
              "poids_finaux": [float(w) for _, w in dfin], "distance_finale": i_fin["distance_consommee"],
              "projections_finales": i_fin["projections"] + i_renf["projections"],
              "unites_deployees": int(sum(m.m for m, _ in dfin)),
              "parametres_deployes": int(sum(m.nb_parametres for m, _ in dfin)),
              "parametres_par_requete": int(max(m.nb_parametres for m, w in dfin if w > 0))}
    if leger:
        sortie["cpu_final_s"] = time.process_time() - tf
        return (sortie, (a_fin, a_renf)) if rendre_attaques else sortie
    if not leger:
        tenues = ctx.taux_tenues(dfin)
        sortie["ii_final"] = float(np.mean(tenues))
        sortie["ii_final_sous_familles"] = [float(np.mean(tenues[0::2])), float(np.mean(tenues[1::2]))]
        cles, ex = etat["cles_eval"], etat["eval_X"]
        sortie["i_final_vus"] = float(np.mean([sum(w * m.taux_cache(c, ex[c]) for m, w in dfin if w > 0)
                                               for c in cles[1:]]))
        departs_cc = passes + [a_fin, a_renf]
        base, pts = courbe_detection(dfin, ctx, cb, departs_cc)
        sortie["courbe"] = {"fractions": [0.0] + list(cfg.fractions_courbe) + [1.0], "V": [base] + pts + [V]}
        sortie["cout"] = cout_contournement(dfin, ctx, cb, departs_cc, base, pts, V)
    sortie["cpu_final_s"] = time.process_time() - tf
    return (sortie, (a_fin, a_renf)) if rendre_attaques else sortie


def construire_defenses(instance: int, code_delta: int, racine: int, racine_tenue: int, cfg: Config, bras,
                        leger: bool = False):
    """Contexte, trajectoires et défenses finales (déterministes) des bras demandés et de leurs sources."""
    exiger_config(cfg)
    for nom in bras:
        if nom not in BRAS_TRAJECTOIRE and nom not in TEMOINS_FINALE:
            raise GardeArret(f"bras inconnu : {nom!r}")
    ctx = Contexte(instance, code_delta, racine, racine_tenue, cfg)
    M0 = ctx.entrainer(COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    M0_bis = ctx.entrainer(COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    exiger_meme_moniteur(M0, M0_bis)
    a_faire = [b for b in BRAS_TRAJECTOIRE if b in bras or any(SOURCE_TEMOIN[c] == b for c in bras
                                                                if c in TEMOINS_FINALE)]
    etats, defenses = {}, {}
    for nom in a_faire:
        M = Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, cfg.alpha)
        etats[nom] = trajectoire(nom, ctx, M, leger)
    for nom in bras:
        if nom in BRAS_TRAJECTOIRE:
            defenses[nom] = (etats[nom], etats[nom]["defense_finale"])
        else:
            src = etats[SOURCE_TEMOIN[nom]]
            defenses[nom] = (src, defense_temoin(nom, src, ctx))
    return ctx, etats, defenses


def executer_tache(instance: int, code_delta: int, racine: int, racine_tenue: int, cfg: Config,
                   bras=TOUS_LES_BRAS, leger: bool = False) -> dict:
    exiger_config(cfg)
    t0 = time.process_time()
    ctx, etats, defenses = construire_defenses(instance, code_delta, racine, racine_tenue, cfg, bras, leger)
    sortie = {"instance": instance, "code_delta": code_delta, "delta": ctx.delta, "racine": racine,
              "racine_tenue": racine_tenue, "config_sha256": cfg.empreinte(), "version": VERSION, "bras": {}}
    for nom in bras:
        etat, dfin = defenses[nom]
        res = phase_finale(nom, dfin, ctx, etat, leger)
        if nom in BRAS_TRAJECTOIRE:
            res["par_tour"] = etat["par_tour"]
            res["valeur_jeu_restreint"] = etat["valeur_jeu_restreint"]
            res["cycle"] = etat["cycle"]
            res["cpu_trajectoire_s"] = etat["cpu_trajectoire_s"]
        else:
            res["source"] = SOURCE_TEMOIN[nom]
        sortie["bras"][nom] = res
        exiger_plafond(t0, cfg, f"après la finale de {nom}")
    sortie["entrainements"] = ctx.entr
    sortie["non_convergences"] = ctx.nonconv
    sortie["attaquant"] = {"departs": ctx.att["departs"], "non_finis": ctx.att["non_finis"],
                           "statuts": {str(k): v for k, v in sorted(ctx.att["statuts"].items())},
                           "iter_max": ctx.att["iter_max"], "reponses_a_la_limite": ctx.att["a_la_limite"]}
    exiger_convergence(ctx.nonconv, ctx.entr, cfg)
    exiger_departs_finis(ctx.att["non_finis"], ctx.att["departs"], cfg)
    sortie["cpu_tache_s"] = time.process_time() - t0
    return sortie


def exiger_meme_moniteur(a: Moniteur, b: Moniteur) -> None:
    if not (np.array_equal(a.W, b.W) and np.array_equal(a.b, b.b) and a.t == b.t):
        raise GardeArret("moniteur du tour 0 non reproductible bit à bit : il doit être commun à tous les bras")


def exiger_plafond(t0: float, cfg: Config, ou: str) -> None:
    """Garde : temps processeur d'une tâche (depuis son début t0) au plus `plafond_cpu_tache_s`."""
    if time.process_time() - t0 > cfg.plafond_cpu_tache_s:
        raise GardeArret(f"plafond de temps processeur d'une tâche dépassé ({ou})")


def exiger_convergence(nonconv: int, total: int, cfg: Config) -> None:
    if total and nonconv / total > cfg.taux_nonconv_max:
        raise GardeArret(f"entraînements non convergés : {nonconv}/{total} > {cfg.taux_nonconv_max}")


# =================================================================================================================
# Calibrage des δ (bras A seul, racine de calibrage) : règle écrite avant toute exécution de la v2
# =================================================================================================================
def choisir_deltas(moyennes: dict, cfg: Config) -> tuple[float, float]:
    """δ_haut = plus grand δ de la grille où la détection moyenne de A en (iii) est ≥ 3α (A pas au plancher) ;
    δ_bas = plus grand δ < δ_haut où elle est ≥ 10α (A pas presque entièrement contourné). Critère sur A seul."""
    grille = sorted(float(d) for d in moyennes)
    hauts = [d for d in grille if moyennes[d] >= cfg.seuil_calibrage_haut]
    if not hauts:
        raise GardeArret(f"calibrage : aucun δ de la grille où V(A) ≥ {cfg.seuil_calibrage_haut}")
    dh = max(hauts)
    bas = [d for d in grille if d < dh and moyennes[d] >= cfg.seuil_calibrage_bas]
    if not bas:
        raise GardeArret(f"calibrage : aucun δ < {dh} où V(A) ≥ {cfg.seuil_calibrage_bas}")
    return (max(bas), dh)


# =================================================================================================================
# Analyse : écarts appariés par instance, intervalles par rééchantillonnage
# =================================================================================================================
CONTRASTES = {  # code de contraste → (nom, bras 1, bras 2, mesure)
    1: ("B-A (iii)", "B", "A", "V_iii_final"),
    2: ("B-C1 (iii)", "B", "C1", "V_iii_final"),
    3: ("B-C2 (iii)", "B", "C2", "V_iii_final"),
    4: ("B-C3 (iii)", "B", "C3", "V_iii_final"),
    5: ("B-D (iii)", "B", "D", "V_iii_final"),
    6: ("B-A (ii)", "B", "A", "ii_final"),
    7: ("B-C3 (ii)", "B", "C3", "ii_final"),
    8: ("B-D (ii)", "B", "D", "ii_final"),
    9: ("C3-A (iii)", "C3", "A", "V_iii_final"),
    10: ("D-A (iii)", "D", "A", "V_iii_final"),
    11: ("C1-C2 (iii)", "C1", "C2", "V_iii_final"),
    12: ("B-A (i)", "B", "A", "i_final_vus"),
    13: ("Bp-D (iii)", "Bp", "D", "V_iii_final"),
    14: ("Bp-C3p (iii)", "Bp", "C3p", "V_iii_final"),
    15: ("Bp-B (iii)", "Bp", "B", "V_iii_final"),
    16: ("C3p-C3 (iii)", "C3p", "C3", "V_iii_final"),
    17: ("Bp-D (ii)", "Bp", "D", "ii_final"),
    18: ("Bp-C3p (ii)", "Bp", "C3p", "ii_final"),
    19: ("C3p-D (iii)", "C3p", "D", "V_iii_final"),
}
CONTRASTES_PRINCIPAUX = ("B-C1 (iii)", "B-C2 (iii)", "B-C3 (iii)", "B-D (iii)")   # Q1
CONTRASTES_Q2 = ("Bp-D (iii)", "Bp-C3p (iii)")                                     # Q2
# condition d'application (CM2-03) : moyennes d'un bras, intervalles par rééchantillonnage ; A seul porte un verdict
INDICATEURS = {
    101: ("A I1", "A", "I1_progres"), 102: ("A I2", "A", "I2_oubli"), 103: ("A I3", "A", "I3_retours"),
    104: ("B I1", "B", "I1_progres"), 105: ("B I2", "B", "I2_oubli"),
    106: ("D I1", "D", "I1_progres"), 107: ("D I2", "D", "I2_oubli"),
    108: ("Bp I1", "Bp", "I1_progres"), 109: ("Bp I2", "Bp", "I2_oubli"),
}


def _q(boot: np.ndarray) -> dict:
    return {f"q{p:g}": float(np.quantile(boot, p)) for p in QUANTILES}


def resume_bras(rs: list[dict], nom: str) -> dict:
    """Résumé descriptif d'un bras sur les tâches d'un δ (moyennes, fausses alertes, coût, courbe, poids)."""
    b = [r["bras"][nom] for r in rs]
    out = {"V_iii_final": float(np.mean([x["V_iii_final"] for x in b])),
           "V_min_tache": float(np.min([x["V_iii_final"] for x in b])),
           "V_max_tache": float(np.max([x["V_iii_final"] for x in b])),
           "fpr_moyen": float(np.mean([x["fpr_final"] for x in b])),
           "fpr_min": float(np.min([x["fpr_final"] for x in b])), "fpr_max": float(np.max([x["fpr_final"] for x in b])),
           "standard_moins_renforce": float(np.mean([x["V_iii_standard"] - x["V_iii_renforce"] for x in b])),
           "standard_moins_renforce_max": float(np.max([x["V_iii_standard"] - x["V_iii_renforce"] for x in b]))}
    if all("ii_final" in x for x in b):
        out["ii_final"] = float(np.mean([x["ii_final"] for x in b]))
        out["i_final_vus"] = float(np.mean([x["i_final_vus"] for x in b]))
        c = [x["cout"] for x in b]
        defs = [y for y in c if y["defini"]]
        nc = [y["fraction"] for y in defs if not y["censure"]]
        out["cout"] = {"part_definie": len(defs) / len(c),
                       "part_censuree_parmi_definies": (float(np.mean([y["censure"] for y in defs])) if defs else None),
                       "mediane_fraction_non_censurees": float(np.median(nc)) if nc else None,
                       "n_non_censurees": len(nc),
                       "taches_non_monotones": int(sum(y["non_monotone"] > 0 for y in c))}
        out["courbe_moyenne"] = [float(v) for v in np.mean([x["courbe"]["V"] for x in b], axis=0)]
    if nom in ("B", "C2", "Bp"):
        P = [x["poids_finaux"] for x in b]
        out["poids"] = {"part_pure": float(np.mean([max(w) > 1 - 1e-9 for w in P])),
                        "part_uniforme": float(np.mean([np.allclose(w, 1 / len(w), atol=1e-6) for w in P])),
                        "support_moyen": float(np.mean([sum(v > 1e-6 for v in w) for w in P])),
                        "poids_max_moyen": float(np.mean([max(w) for w in P]))}
    if nom in ("B", "Bp"):
        out["valeur_restreinte_moins_V"] = float(np.mean([x["valeur_jeu_restreint"] - x["V_iii_final"] for x in b]))
    if all("cycle" in x for x in b):
        cy = [x["cycle"] for x in b]
        out["cycle"] = {"I1_progres": float(np.mean([c["I1_progres"] for c in cy])),
                        "I2_oubli": float(np.mean([c["I2_oubli"] for c in cy])),
                        "I3_retours": (float(np.mean([c["I3_retours"] for c in cy]))
                                       if all(c["I3_retours"] is not None for c in cy) else None),
                        "retention": {k: float(np.mean([c["retention"][k] for c in cy])) for k in cy[0]["retention"]},
                        "H_moyenne": [[float(v) for v in ligne] for ligne in np.mean([c["H"] for c in cy], axis=0)]}
    out["parametres_deployes"] = int(b[0]["parametres_deployes"])
    out["parametres_par_requete_max"] = int(max(x["parametres_par_requete"] for x in b))
    return out


def analyser(resultats: list[dict], racine_reech: int, n_reech: int = 20000) -> dict:
    sortie = {}
    for cd in sorted({r["code_delta"] for r in resultats}):
        rs = sorted((r for r in resultats if r["code_delta"] == cd), key=lambda r: r["instance"])
        bloc = {"n": len(rs), "delta": rs[0]["delta"], "bras": {}, "contrastes": {}}
        for nom in TOUS_LES_BRAS:
            if all(nom in r["bras"] for r in rs):
                bloc["bras"][nom] = resume_bras(rs, nom)
        noms = [n for n in TOUS_LES_BRAS if n in bloc["bras"]]
        if len(noms) > 1:
            ecart_fpr = [max(r["bras"][n]["fpr_final"] for n in noms) - min(r["bras"][n]["fpr_final"] for n in noms)
                         for r in rs]
            bloc["ecart_fpr_entre_bras"] = {"moyen": float(np.mean(ecart_fpr)), "max": float(np.max(ecart_fpr))}
        if all("B" in r["bras"] and "C1" in r["bras"] for r in rs):
            bloc["B_egal_C1_au_bit"] = int(sum(r["bras"]["B"]["V_iii_final"] == r["bras"]["C1"]["V_iii_final"]
                                               for r in rs))
        if all("A" in r["bras"] and "D" in r["bras"] for r in rs):
            bloc["D_egal_A_au_bit"] = int(sum(r["bras"]["D"]["V_iii_final"] == r["bras"]["A"]["V_iii_final"]
                                              for r in rs))
        att = [r["attaquant"] for r in rs if "attaquant" in r]
        if att:
            st = Counter()
            for a in att:
                st.update(a["statuts"])
            bloc["attaquant"] = {"departs": int(sum(a["departs"] for a in att)),
                                 "non_finis": int(sum(a["non_finis"] for a in att)), "statuts": dict(st),
                                 "iter_max": int(max(a["iter_max"] for a in att)),
                                 "reponses_a_la_limite": int(sum(a["reponses_a_la_limite"] for a in att))}
        for code, (lib, b1, b2, mes) in CONTRASTES.items():
            if not all(b1 in r["bras"] and b2 in r["bras"] and mes in r["bras"][b1] for r in rs):
                continue
            dlt = np.array([r["bras"][b1][mes] - r["bras"][b2][mes] for r in rs])
            g = gen(racine_reech, cd, code, 0, 0, ROLE_REECH)
            idx = g.integers(0, len(dlt), size=(n_reech, len(dlt)))
            boot = dlt[idx].mean(1)
            bloc["contrastes"][lib] = {
                "moyenne": float(dlt.mean()), "ecart_type": float(dlt.std(ddof=1)) if len(dlt) > 1 else float("nan"),
                "quantiles": _q(boot), "zeros_exacts": int(np.sum(dlt == 0)),
                "std_attaquant_standard": (float(np.mean([r["bras"][b1]["V_iii_standard"] - r["bras"][b2]["V_iii_standard"]
                                                          for r in rs])) if mes == "V_iii_final" else None),
                "std_attaquant_renforce": (float(np.mean([r["bras"][b1]["V_iii_renforce"] - r["bras"][b2]["V_iii_renforce"]
                                                          for r in rs])) if mes == "V_iii_final" else None)}
        bloc["indicateurs"] = {}
        for code, (lib, nom, mes) in INDICATEURS.items():
            if not all(nom in r["bras"] and "cycle" in r["bras"][nom] and r["bras"][nom]["cycle"][mes] is not None
                       for r in rs):
                continue
            x = np.array([r["bras"][nom]["cycle"][mes] for r in rs])
            g = gen(racine_reech, cd, code, 0, 0, ROLE_REECH)
            boot = x[g.integers(0, len(x), size=(n_reech, len(x)))].mean(1)
            bloc["indicateurs"][lib] = {"moyenne": float(x.mean()),
                                        "ecart_type": float(x.std(ddof=1)) if len(x) > 1 else float("nan"),
                                        "quantiles": _q(boot)}
        sortie[str(cd)] = bloc
    return sortie


# =================================================================================================================
# Lecture mécanique des tables (aide au lecteur R13 ; le texte scellé fait foi en cas d'écart)
# =================================================================================================================
def classer(lb: float, ub: float, eq_lo: float, eq_hi: float, m: float) -> str:
    """Classement d'un contraste B − X à δ fixé, marge m : dans cet ordre, la première condition vraie."""
    if lb > m:
        return "B>X"
    if ub < -m:
        return "X>B"
    if eq_lo > -m and eq_hi < m:
        return "≈"
    if lb > 0:
        return "B≳X"
    if ub < 0:
        return "X≳B"
    return "?"


def _verdict_question(statut: dict, nom: str) -> str:
    v = list(statut.values())
    if any(s.startswith("non exercée") for s in v):
        return f"{nom} non exercée (au moins un δ)"
    if all(s == "tenue" for s in v):
        return f"{nom} confirmée"
    if all(s.startswith("réfutée") for s in v):
        return f"{nom} réfutée"
    if any(s == "tenue" for s in v) and any(s.startswith("réfutée") for s in v):
        return f"{nom} dépend de δ"
    return f"{nom} non tranchée"


def _statut_classes(cl) -> str:
    cl = list(cl)
    if all(x == "B>X" for x in cl):
        return "tenue"
    if any(x == "X>B" for x in cl):
        return "réfutée (un témoin fait mieux)"
    if any(x == "≈" for x in cl):
        return "réfutée (équivalence)"
    return "non tranchée"


def lire_tables(analyse: dict, S1: float, S5: float, marges: dict, S15: float) -> dict:
    """Applique les Tables 1 à 7 (texte du préenregistrement, brouillon 3) à une analyse. `marges` : code δ → marge
    (S6, la même pour Q1 et Q2). Intervalles : Tables 1, 2 et 5, Bonferroni sur 2 δ (q0.00625, q0.99375) ; Table 3
    (Q1), Bonferroni sur 8 tests (q0.003125, q0.996875 ; équivalence q0.00625, q0.99375) ; Table 6 (Q2), Bonferroni
    sur 4 tests (q0.00625, q0.99375 ; équivalence q0.0125, q0.9875). Les audits ne sont pas lus ici : le lecteur R13
    applique les déclencheurs et leurs effets écrits (aide mécanique seulement)."""
    cds = sorted(analyse)
    t1 = {}
    for cd in cds:
        c = analyse[cd]["contrastes"]["B-A (iii)"]
        q = c["quantiles"]
        t1[cd] = {"exerce": c["moyenne"] >= S1 and q["q0.00625"] > 0, "perd": q["q0.99375"] < 0}
    if all(v["exerce"] for v in t1.values()):
        l1 = "mécanisme exercé"
    elif any(v["perd"] for v in t1.values()):
        l1 = "le mélange perd contre la défense unique (au moins un δ)"
    else:
        l1 = "mécanisme non démontré (gain sous S1 ou imprécis, au moins un δ)"
    t2 = {}
    for cd in cds:
        q = analyse[cd]["contrastes"]["B-A (ii)"]["quantiles"]
        t2[cd] = (q["q0.00625"], q["q0.99375"])
    if any(ub < -S5 for _, ub in t2.values()):
        l2 = "régression avérée au-delà de la tolérance"
    elif all(lb > -S5 for lb, _ in t2.values()) and any(ub < 0 for _, ub in t2.values()):
        l2 = "régression démontrée sous la tolérance"
    elif all(lb > 0 for lb, _ in t2.values()):
        l2 = "amélioration sur (ii)"
    elif all(lb > -S5 for lb, _ in t2.values()):
        l2 = "sans régression à S5 près"
    else:
        l2 = "régression non exclue (imprécis)"
    t3 = {}
    for cd in cds:
        t3[cd] = {}
        for lib in CONTRASTES_PRINCIPAUX:
            q = analyse[cd]["contrastes"][lib]["quantiles"]
            t3[cd][lib] = classer(q["q0.003125"], q["q0.996875"], q["q0.00625"], q["q0.99375"], marges[cd])
    statut = {cd: _statut_classes(t3[cd].values()) for cd in cds}
    l4 = _verdict_question(statut, "Q1")
    # Table 5 : condition d'application (défense unique A), bornes B2
    t5 = {}
    for cd in cds:
        ind = analyse[cd]["indicateurs"]
        lb1, ub1 = ind["A I1"]["quantiles"]["q0.00625"], ind["A I1"]["quantiles"]["q0.99375"]
        lb2, ub2 = ind["A I2"]["quantiles"]["q0.00625"], ind["A I2"]["quantiles"]["q0.99375"]
        if lb1 > S15:
            t5[cd] = "A progresse"
        elif ub1 < S15 and lb2 > S15:
            t5[cd] = "A ne progresse pas, avec oubli"
        elif ub1 < S15 and ub2 < S15:
            t5[cd] = "A ne progresse pas, sans oubli"
        elif ub1 < S15:
            t5[cd] = "A ne progresse pas, oubli indéterminé"
        else:
            t5[cd] = "indéterminé"
    if all(s.startswith("A ne progresse pas") for s in t5.values()):
        l5 = "condition d'application vérifiée (A ne progresse pas aux deux δ)"
    elif any(s == "A progresse" for s in t5.values()):
        l5 = "condition d'application non vérifiée (A progresse dans au moins un δ)"
    else:
        l5 = "condition d'application indéterminée"
    # Tables 6 et 7 : Q2, B′ contre D et C3′ à classe de fonctions égale
    t6, statut2 = {}, {}
    for cd in cds:
        t6[cd] = {}
        for lib in CONTRASTES_Q2:
            q = analyse[cd]["contrastes"][lib]["quantiles"]
            t6[cd][lib] = classer(q["q0.00625"], q["q0.99375"], q["q0.0125"], q["q0.9875"], marges[cd])
        if analyse[cd]["bras"]["Bp"]["poids"]["part_pure"] > 0.5:
            statut2[cd] = "non exercée (mélange B′ dégénéré)"
        else:
            statut2[cd] = _statut_classes(t6[cd].values())
    l7 = _verdict_question(statut2, "Q2")
    return {"table1": l1, "table1_par_delta": t1, "table2": l2, "table3": t3, "table4_par_delta": statut, "table4": l4,
            "table5_par_delta": t5, "table5": l5, "table6": t6, "table7_par_delta": statut2, "table7": l7}


# =================================================================================================================
# Points d'entrée
# =================================================================================================================
# =================================================================================================================
# Attaquant indépendant (CM2-05) : départs structurés, beaucoup de départs, stratégie d'évolution sans gradient
# =================================================================================================================
BRAS_AUDIT = ("B", "C3", "D", "Bp", "C3p")
PAIRES_AUDIT = (("B", "C3"), ("B", "D"), ("Bp", "D"), ("Bp", "C3p"))


def departs_structures(cible: np.ndarray, delta: float, cfg: Config) -> list[np.ndarray]:
    """3 × (K + 1) départs : pour chaque échelle s ∈ {0,5 ; 1 ; 1,5}, chaque composante k tirée vers l'origine de tout
    le budget avec ses écarts-types fixés à s, puis toutes les composantes tirées vers l'origine avec écarts-types s
    (chaque départ projeté sur la contrainte et la boîte)."""
    mu, sig = deplier(cible, cfg)
    sortie = []
    for s in (0.5, 1.0, 1.5):
        for k in range(cfg.K):
            m2, s2 = mu.copy(), sig.copy()
            m2[k] = mu[k] * (1 - min(delta * np.sqrt(cfg.K) / np.linalg.norm(mu[k]), 1.0))
            s2[k] = s
            sortie.append(projeter(vecteur(m2, s2), cible, delta, cfg)[0])
        m3 = mu * (1 - np.minimum(delta / np.linalg.norm(mu, axis=1, keepdims=True), 1.0))
        sortie.append(projeter(vecteur(m3, np.full_like(sig, s)), cible, delta, cfg)[0])
    return sortie


def _deux_taux(theta, defense, z, cfg: Config) -> tuple[float, float]:
    """(taux dur, taux lissé) d'une loi d'attaque sur des échantillons fixés z (un seul calcul de score par moniteur)."""
    mu, sig = deplier(theta, cfg)
    K, n, d = z.shape
    X = (mu[:, None, :] + sig[:, None, :] * z).reshape(K * n, d)
    dur = lisse = 0.0
    for m, p in defense:
        if p <= 0:
            continue
        s = m.score(X)
        dur += p * float(np.mean(s > m.t))
        lisse += p * float(np.mean(expit((s - m.t) / (cfg.tau * m.e))))
    return dur, lisse


def evolution(defense, x0, cible, delta, cfg: Config, rng: np.random.Generator, z) -> tuple[np.ndarray, int]:
    """Stratégie d'évolution (1 + λ) sans gradient : critère (taux dur, puis taux lissé pour départager), pas initial
    0,1 δ, ×1,5 sur succès, ×0,9 sinon ; chaque descendant est projeté sur la contrainte et la boîte."""
    x = projeter(np.asarray(x0, float), cible, delta, cfg)[0]
    fx = _deux_taux(x, defense, z, cfg)
    pas, succes = 0.1 * delta, 0
    for _ in range(cfg.audit_es_generations):
        meilleur = None
        for _ in range(cfg.audit_es_lambda):
            y = projeter(x + pas * rng.standard_normal(x.size), cible, delta, cfg)[0]
            fy = _deux_taux(y, defense, z, cfg)
            if meilleur is None or fy < meilleur[0]:
                meilleur = (fy, y)
        if meilleur[0] < fx:
            fx, x = meilleur
            pas *= 1.5
            succes += 1
        else:
            pas = max(pas * 0.9, 1e-4 * delta)
    return x, succes


def attaquant_independant(defense, ctx: Contexte, cb: int, passes, attaques_finales) -> dict:
    """Contrôle d'attaquant indépendant d'une défense figée : (1) SLSQP lourd (départs structurés, `audit_departs`
    départs tirés, attaques passées et finales, `audit_n_mc` échantillons, `audit_iter` itérations) ; (2) stratégie
    d'évolution sans gradient depuis (1) et depuis l'attaque finale standard. Chaque réponse est évaluée sur
    `n_eval` échantillons frais."""
    cfg = ctx.cfg

    def g(k):
        return ctx.g(cb, cfg.T + 1, ROLE_AUDIT, k)

    th_l, info = meilleure_reponse(defense, ctx.cible, ctx.delta, cfg, g(1), g(2),
                                   departs_suppl=departs_structures(ctx.cible, ctx.delta, cfg) + list(passes) +
                                   list(attaques_finales), n_departs=cfg.audit_departs, n_mc=cfg.audit_n_mc,
                                   iter_max=cfg.audit_iter)
    exiger_departs_finis(info["non_finis"], info["departs"], cfg)
    z = g(4).standard_normal((cfg.K, cfg.audit_n_mc, cfg.d))
    th_e1, s1 = evolution(defense, th_l, ctx.cible, ctx.delta, cfg, g(5), z)
    th_e2, s2 = evolution(defense, attaques_finales[0], ctx.cible, ctx.delta, cfg, g(7), z)
    for th in (th_l, th_e1, th_e2):
        exiger_admissible(th, ctx.cible, ctx.delta, cfg)
    return {"V_lourd": taux_defense(defense, echantillonner(th_l, cfg.n_eval, g(3), cfg)),
            "V_evolution_depuis_lourd": taux_defense(defense, echantillonner(th_e1, cfg.n_eval, g(6), cfg)),
            "V_evolution_depuis_standard": taux_defense(defense, echantillonner(th_e2, cfg.n_eval, g(8), cfg)),
            "succes_evolution": [s1, s2], "departs_lourd": info["departs"], "non_finis_lourd": info["non_finis"],
            "statuts_lourd": info["statuts"], "iter_max_lourd": info["iter_max"]}


def auditer_tache(instance: int, code_delta: int, racine: int, racine_tenue: int, cfg: Config, source: dict) -> dict:
    """Reconstruit les défenses de la tâche (déterministe), exige V reconstruit = V du run audité au bit près, puis
    oppose l'attaquant indépendant aux défenses finales de B, C3, D, B′ et C3′."""
    t0 = time.process_time()
    for nom in BRAS_AUDIT:
        if nom not in source.get("bras", {}):
            raise GardeArret(f"audit : bras {nom} absent du run audité")
    ctx, _, defenses = construire_defenses(instance, code_delta, racine, racine_tenue, cfg, BRAS_AUDIT, leger=True)
    sortie = {"instance": instance, "code_delta": code_delta, "bras": {}}
    for nom in BRAS_AUDIT:
        etat, dfin = defenses[nom]
        res, (a_fin, a_renf) = phase_finale(nom, dfin, ctx, etat, leger=True, rendre_attaques=True)
        if res["V_iii_final"] != source["bras"][nom]["V_iii_final"]:
            raise GardeArret(f"audit : V reconstruit ≠ V du run audité ({nom}, instance {instance}, δ {code_delta})")
        ind = attaquant_independant(dfin, ctx, BRAS[nom], etat["attaques"][1:], [a_fin, a_renf])
        V_audit = min(res["V_iii_final"], ind["V_lourd"], ind["V_evolution_depuis_lourd"],
                      ind["V_evolution_depuis_standard"])
        sortie["bras"][nom] = {"V_source": res["V_iii_final"], **ind, "V_audit": V_audit}
    sortie["cpu_tache_s"] = time.process_time() - t0
    return sortie


def juger_audit(taches: list[dict], critere: float) -> dict:
    """Critère d'artefact (S17), par δ, sur la moyenne des tâches auditées : un contraste B − C3, B − D, B′ − D ou
    B′ − C3′ dont le signe change, ou qui change de plus de `critere`, entre V du run audité et V de l'audit."""
    sortie, drapeaux = {}, []
    for cd in sorted({t["code_delta"] for t in taches}):
        ts = [t for t in taches if t["code_delta"] == cd]
        bloc = {}
        for b1, b2 in PAIRES_AUDIT:
            src = np.array([t["bras"][b1]["V_source"] - t["bras"][b2]["V_source"] for t in ts])
            aud = np.array([t["bras"][b1]["V_audit"] - t["bras"][b2]["V_audit"] for t in ts])
            ms, ma = float(src.mean()), float(aud.mean())
            art = bool(np.sign(ms) != np.sign(ma) or abs(ma - ms) > critere)
            drapeaux.append(art)
            bloc[f"{b1}-{b2}"] = {"source": ms, "audit": ma, "ecart": ma - ms,
                                  "ecart_max_tache": float(np.max(np.abs(aud - src))), "n": len(ts), "artefact": art}
        sortie[str(cd)] = bloc
    return {"par_delta": sortie, "artefact": any(drapeaux), "critere": critere}


# =================================================================================================================
# Processus de travail : lancement, arrêt par PID (R10), garde « aucun orphelin »
# =================================================================================================================
def _debut_processus(pid: int) -> str | None:
    """Instant de départ du processus (champ 22 de /proc/<pid>/stat) : distingue un PID réemployé."""
    try:
        return Path(f"/proc/{int(pid)}/stat").read_text().rsplit(")", 1)[1].split()[19]
    except (OSError, IndexError):
        return None


def processus_vivant(pid: int, debut: str | None = None) -> bool:
    """Vivant, non zombie, et (si `debut` est donné) le même processus que celui consigné."""
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


def lire_pids(chemin: str | Path) -> list[tuple[int, str | None]]:
    sortie = []
    for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
        if ligne.strip() and not ligne.startswith("#"):
            pid, debut = (ligne.split() + [None])[:2]
            sortie.append((int(pid), debut))
    return sortie


def arreter_par_pid(pids, delai_s: float = 10.0) -> list[int]:
    """R10 : signal TERM à chaque PID consigné encore vivant (même instant de départ), puis KILL après le délai.
    Renvoie les PID qui étaient vivants. Jamais d'arrêt par motif de ligne de commande."""
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
    """Garde (CM2-14) : aucune reprise ni fin de run tant qu'un processus de travail consigné tourne encore."""
    vivants = [int(p) for p, d in pids if processus_vivant(p, d)]
    if vivants:
        raise GardeArret(f"processus de travail encore vivants (PID {vivants}) : arrêter par PID avant toute "
                         "reprise (R10)")


def _consigner_pids(pids, fichier_pids, sceller_pids: bool) -> None:
    texte = "# PID et instant de départ des processus de travail (arrêt par PID, R10)\n" + \
            "".join(f"{p} {d}\n" for p, d in pids)
    print("PID des processus de travail : " + " ".join(str(p) for p, _ in pids), file=sys.stderr, flush=True)
    if fichier_pids is not None:
        f = _exiger_absent(Path(fichier_pids))
        f.write_text(texte, encoding="utf-8")
        if sceller_pids:
            from controle_ia.scellement import sceller

            sceller(f)


def _travail(args):
    mode, instance, cd, racine, racine_tenue, cfg_dict, bras, leger, prereg, source = args
    cfg = Config(**{k: tuple(v) if isinstance(v, list) else v for k, v in cfg_dict.items()})
    if (racine in RACINES_DECISION or racine_tenue in RACINES_DECISION) and \
            _AUTORISATION_DECISION["prereg_sha256"] is None:
        if prereg is None:
            raise GardeArret("racine de décision dans un processus de travail sans préenregistrement")
        autoriser_decision(prereg, cfg)
    if mode == "audit":
        return auditer_tache(instance, cd, racine, racine_tenue, cfg, source)
    return executer_tache(instance, cd, racine, racine_tenue, cfg, bras=bras, leger=leger)


def _lancer(taches, processus: int, fichier_pids=None, sceller_pids: bool = False) -> list:
    """Pool `spawn` ; signal TERM converti en `GardeArret` (le bloc `with` termine alors les processus de travail) ;
    PID consignés (attribut interne `pool._pool` de multiprocessing, déclaré) ; à la sortie, arrêt par PID de tout
    survivant puis garde « aucun orphelin »."""
    import multiprocessing as mp

    if processus <= 1:
        return [_travail(t) for t in taches]
    ancien = signal.signal(signal.SIGTERM, lever_sur_term)
    pids = []
    try:
        with mp.get_context("spawn").Pool(processus) as pool:
            pids = [(p.pid, _debut_processus(p.pid)) for p in pool._pool]
            _consigner_pids(pids, fichier_pids, sceller_pids)
            res = pool.map(_travail, taches, chunksize=1)
    finally:
        signal.signal(signal.SIGTERM, ancien)
        arreter_par_pid(pids)
        exiger_aucun_orphelin(pids)
    return res


def executer(instances, racine, racine_tenue, cfg: Config, processus: int = 2, codes_delta=None,
             bras=TOUS_LES_BRAS, leger=False, prereg=None, fichier_pids=None,
             sceller_pids=False) -> tuple[list[dict], dict]:
    codes = codes_delta if codes_delta is not None else range(1, len(cfg.deltas) + 1)
    taches = [("tache", i, cd, racine, racine_tenue, asdict(cfg), tuple(bras), leger,
               None if prereg is None else str(prereg), None) for cd in codes for i in instances]
    m0 = time.perf_counter()
    res = _lancer(taches, processus, fichier_pids, sceller_pids)
    temps = {"mur_s": time.perf_counter() - m0, "cpu_somme_taches_s": float(sum(r["cpu_tache_s"] for r in res)),
             "processus": processus, "taches": len(taches)}
    return res, temps


def auditer(instances, racine, racine_tenue, cfg: Config, sources: dict, processus: int = 2, prereg=None,
            fichier_pids=None, sceller_pids=False) -> tuple[list[dict], dict, dict]:
    """Audit d'attaquant indépendant sur les tâches (instance, δ) demandées ; `sources` : (instance, code δ) → résultat
    de la tâche du run audité."""
    taches = []
    for cd in range(1, len(cfg.deltas) + 1):
        for i in instances:
            if (i, cd) not in sources:
                raise GardeArret(f"audit : tâche absente du run audité (instance {i}, δ {cd})")
            taches.append(("audit", i, cd, racine, racine_tenue, asdict(cfg), BRAS_AUDIT, True,
                           None if prereg is None else str(prereg), sources[(i, cd)]))
    m0 = time.perf_counter()
    res = _lancer(taches, processus, fichier_pids, sceller_pids)
    temps = {"mur_s": time.perf_counter() - m0, "cpu_somme_taches_s": float(sum(r["cpu_tache_s"] for r in res)),
             "processus": processus, "taches": len(taches)}
    return res, temps, juger_audit(res, cfg.audit_critere)


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


def _plage(s: str) -> list[int]:
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


def _sources_par_tache(resultats: list[dict]) -> dict:
    return {(r["instance"], r["code_delta"]): r for r in resultats}


def charger_pilote(chemin: str | Path, cfg: Config) -> dict:
    """Pilote « détection » produit par ce code (mode essai) : racines d'essai permises, configuration identique."""
    corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
    man = corps.get("manifeste", {})
    exiger_racines_essai(man.get("racine"), man.get("racine_tenue"))
    if corps.get("mode") != "essai" or corps.get("oracle") != "detection" or man.get("config_sha256") != cfg.empreinte():
        raise GardeArret(f"audit-essai : {chemin} n'est pas un pilote « détection » de cette configuration")
    return corps


def exiger_meme_prereg(manifeste_source: dict, sha: str) -> None:
    """Garde : le run audité a été lancé sous le préenregistrement qui autorise l'audit."""
    p = manifeste_source.get("preenregistrement") or {}
    if p.get("sha256") != sha:
        raise GardeArret("audit : run audité rattaché à un autre préenregistrement (ou à aucun)")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sp = ap.add_subparsers(dest="mode", required=True)
    c = sp.add_parser("calibrage", help="option de recalibrage des δ (racine réservée, bras A seul), si Lazar la retient")
    c.add_argument("--instances", default="0:48")
    c.add_argument("--sortie", required=True)
    c.add_argument("--processus", type=int, default=2)
    e = sp.add_parser("essai", help="racine d'essai : pilote et puissance")
    e.add_argument("--instances", default="0:4")
    e.add_argument("--sortie", required=True)
    e.add_argument("--processus", type=int, default=2)
    e.add_argument("--oracle", choices=("detection", "logistique"), default="detection")
    e.add_argument("--racine", type=int, default=RACINE_ESSAI)
    e.add_argument("--racine-tenue", type=int, default=RACINE_ESSAI_TENUE)
    e.add_argument("--pids", default=None, help="fichier (nouveau) des PID des processus de travail")
    ae = sp.add_parser("audit-essai", help="attaquant indépendant sur des tâches d'un pilote (racine d'essai)")
    ae.add_argument("--pilote", required=True)
    ae.add_argument("--instances", default="0:1")
    ae.add_argument("--sortie", required=True)
    ae.add_argument("--processus", type=int, default=2)
    sp.add_parser("identite", help="imprime le bloc d'identité à recopier dans le préenregistrement")
    dc = sp.add_parser("decision", help="racine de décision : exige le préenregistrement scellé")
    dc.add_argument("--prereg", required=True)
    dc.add_argument("--instances", required=True)
    dc.add_argument("--run-id", required=True)
    dc.add_argument("--processus", type=int, default=2)
    au = sp.add_parser("audit", help="attaquant indépendant sur des tâches du run de décision (après scellement)")
    au.add_argument("--prereg", required=True)
    au.add_argument("--source-run", required=True)
    au.add_argument("--instances", default="0:5")
    au.add_argument("--run-id", required=True)
    au.add_argument("--processus", type=int, default=2)
    o = sp.add_parser("orphelins", help="R10 : vérifie (et, avec --arreter, arrête par PID) les processus consignés")
    o.add_argument("--pids", required=True)
    o.add_argument("--arreter", action="store_true")
    a = ap.parse_args(argv)
    if a.mode == "identite":
        print(bloc_identite(exiger_config(CONFIG_V3)))
        return 0
    if a.mode == "orphelins":
        pids = lire_pids(a.pids)
        if a.arreter:
            print(f"arrêtés par PID : {arreter_par_pid(pids)}")
        exiger_aucun_orphelin(pids)
        print("aucun processus de travail consigné ne tourne")
        return 0
    if a.mode == "calibrage":
        cfg = replace(CONFIG_BASE_V3, deltas=tuple(CONFIG_BASE_V3.grille_calibrage))
        exiger_config(cfg)
        exiger_racines_essai(RACINE_RECALIBRAGE, RACINE_RECALIBRAGE_TENUE)
        sortie = _exiger_absent(Path(a.sortie))
        res, temps = executer(_plage(a.instances), RACINE_RECALIBRAGE, RACINE_RECALIBRAGE_TENUE, cfg, a.processus,
                              bras=("A",), leger=True)
        moyennes = {float(d): float(np.mean([r["bras"]["A"]["V_iii_final"] for r in res if r["delta"] == d]))
                    for d in cfg.deltas}
        choix = choisir_deltas(moyennes, CONFIG_BASE_V3)
        corps = {"mode": "calibrage", "manifeste": {"racine": RACINE_RECALIBRAGE,
                                                    "racine_tenue": RACINE_RECALIBRAGE_TENUE, "config": asdict(cfg),
                                                    "config_sha256": cfg.empreinte(), "versions": _versions(),
                                                    "instances": a.instances, "commande": " ".join(sys.argv)},
                 "temps": temps, "moyennes_V_A": {str(k): v for k, v in moyennes.items()},
                 "deltas_choisis": list(choix), "resultats": res}
        _ecrire_nouveau(sortie, corps)
        print(f"calibrage écrit : {sortie} ; V(A) moyen par δ {moyennes} ; δ choisis {choix} ; {temps}")
        return 0
    if a.mode == "essai":
        exiger_racines_essai(a.racine, a.racine_tenue)
        cfg = exiger_config(CONFIG_V3)
        if a.oracle == "logistique":
            cfg = replace(cfg, entrainement="logistique")
        sortie = _exiger_absent(Path(a.sortie))
        res, temps = executer(_plage(a.instances), a.racine, a.racine_tenue, cfg, a.processus, fichier_pids=a.pids)
        corps = {"mode": "essai", "oracle": a.oracle,
                 "manifeste": {"racine": a.racine, "racine_tenue": a.racine_tenue, "schema_graines": cfg.schema_graines,
                               "config": asdict(cfg), "config_sha256": cfg.empreinte(), "versions": _versions(),
                               "commande": " ".join(sys.argv)},
                 "temps": temps, "analyse": analyser(res, a.racine), "resultats": res}
        _ecrire_nouveau(sortie, corps)
        print(f"essai écrit : {sortie} ; {temps}")
        return 0
    if a.mode == "audit-essai":
        cfg = exiger_config(CONFIG_V3)
        pil = charger_pilote(a.pilote, cfg)
        sortie = _exiger_absent(Path(a.sortie))
        man = pil["manifeste"]
        res, temps, jugement = auditer(_plage(a.instances), man["racine"], man["racine_tenue"], cfg,
                                       _sources_par_tache(pil["resultats"]), a.processus)
        corps = {"mode": "audit-essai", "pilote": str(a.pilote), "pilote_sha256": empreinte_fichier(a.pilote),
                 "manifeste": {"racine": man["racine"], "racine_tenue": man["racine_tenue"],
                               "config_sha256": cfg.empreinte(), "versions": _versions(),
                               "commande": " ".join(sys.argv)},
                 "temps": temps, "jugement": jugement, "taches": res}
        _ecrire_nouveau(sortie, corps)
        print(f"audit d'essai écrit : {sortie} ; artefact {jugement['artefact']} ; {temps}")
        return 0
    from controle_ia import manifeste as man

    cfg = exiger_config(CONFIG_V3)
    if a.mode == "audit":
        # audit d'attaquant indépendant (déclencheur 9) : après scellement de l'analyse, sur les tâches de la décision
        sha = autoriser_decision(a.prereg, cfg)
        src = man.verifier_resultat(DEPOT, DEPOT / "diag" / a.source_run / "resultats-arene.json")
        man_src, _ = man.lire_manifeste(DEPOT / "runs" / a.source_run / "manifeste.json")
        exiger_meme_prereg(man_src, sha)
        chemin_m, _ = man.creer_manifeste(DEPOT, a.run_id, {"config": asdict(cfg), "config_sha256": cfg.empreinte(),
                                                            "racine": RACINE, "racine_tenue": RACINE_TENUE,
                                                            "instances": a.instances, "source_run": a.source_run,
                                                            "prereg_sha256": sha, "versions": _versions()},
                                          ["audit"], entropie=RACINE, decisif=True, prereg=a.prereg,
                                          commande=" ".join(sys.argv))
        res, temps, jugement = auditer(_plage(a.instances), RACINE, RACINE_TENUE, cfg,
                                       _sources_par_tache(src["resultat"]["resultats"]), a.processus, prereg=a.prereg,
                                       fichier_pids=chemin_m.parent / "pids-travail.txt", sceller_pids=True)
        man.ecrire_resultat(DEPOT, chemin_m, "audit-attaquant", {"temps": temps, "jugement": jugement, "taches": res})
        print(f"audit écrit sous diag/{a.run_id}/ ; artefact {jugement['artefact']}")
        return 0
    # décision : le préenregistrement scellé est exigé AVANT toute graine de décision
    sha = autoriser_decision(a.prereg, cfg, a.instances)
    chemin_m, _ = man.creer_manifeste(DEPOT, a.run_id, {"config": asdict(cfg), "config_sha256": cfg.empreinte(),
                                                        "racine": RACINE, "racine_tenue": RACINE_TENUE,
                                                        "instances": a.instances, "prereg_sha256": sha,
                                                        "schema_graines": cfg.schema_graines,
                                                        "note_graines": "le champ « graines » du manifeste n'est pas "
                                                                        "employé : le code dérive tout de RACINE "
                                                                        "selon schema_graines",
                                                        "versions": _versions()},
                                      ["arene"], entropie=RACINE, decisif=True, prereg=a.prereg,
                                      commande=" ".join(sys.argv))
    res, temps = executer(_plage(a.instances), RACINE, RACINE_TENUE, cfg, a.processus, prereg=a.prereg,
                          fichier_pids=chemin_m.parent / "pids-travail.txt", sceller_pids=True)
    man.ecrire_resultat(DEPOT, chemin_m, "resultats-arene", {"temps": temps, "resultats": res})
    man.ecrire_resultat(DEPOT, chemin_m, "analyse-arene", analyser(res, RACINE))
    print(f"run de décision écrit sous diag/{a.run_id}/")
    return 0


__all__ = ["Config", "CONFIG_BASE_V3", "CONFIG_V3", "RACINE", "RACINE_TENUE", "RACINE_ESSAI", "RACINE_ESSAI_TENUE",
           "RACINE_TESTS", "executer_tache", "analyser", "lire_tables", "classer", "resoudre_jeu", "meilleure_reponse",
           "exiger_prereg_arene", "exiger_identite_prereg", "autoriser_decision", "exiger_racines_essai",
           "choisir_deltas", "auditer", "juger_audit", "attaquant_independant", "replace"]

if __name__ == "__main__":
    sys.exit(main())
