"""Constantes, graines par clé et gardes communes de l'étape B bis (`prereg/T0.7-etape-B-bis-v1.md`, scellé `0ae6210f…`), v1.

Tout ce que le texte fixe et que plusieurs modules lisent est écrit ici une seule fois : conditions, doses, cellules
(« Plan d'analyse », point 9), séries de relecture (point 3), grille (point 5), nombres (800 directions, 100 réétiquetages,
2 000 tirages), niveaux (« Seuil »), clés de graines (point 12).

**Graines (R9, point 12)** : `numpy.random.SeedSequence(entropie)`, entropie de 128 bits tirée à l'inscription de
`CODE-BBIS` ; une graine par clé, dérivée comme `manifeste.graines` (clé de dérivation = `cle_de_tache(clé)`), rejouée par
`manifeste.generateur` (contrôle de l'état). Les formes de clés permises sont celles du texte (`FORMES_CLES`) ; toute autre
forme est refusée. Les clés dérivées sont consignées (`Graines.derivees`) pour le manifeste de chaque marche.

Interprétations déclarées (rapport du développeur) : `<pli>` d'une clé d'apprentissage vaut `e<k>` (sonde finale du pli
externe k, apprise sur l'autre pli) ou `e<k>i<j>` (pli interne j) ; `<serie>` vaut `sonde`, `enc` ou `nul<r>` ;
`<ligne>` d'une clé de tirages est le nom de la cellule (tous les tirages d'une cellule sont communs à ses grandeurs).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..gardes import GardeArret
from ..manifeste import generateur, graines as _graines_manifeste

TEXTE = "prereg/T0.7-etape-B-bis-v1.md"
TEXTE_SHA256 = "0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb"
RUN_7B = "20261111-151701-t06-reel"

H, INSTRUIT, TEMOIN_INSTRUIT, T100 = "honnete", "saboteur", "temoin", "T100"
DOSES_REELLES = (0.25, 0.5, 0.75, 1.0)
COUCHES_REELLES = (7, 15, 23)
FAMILLES = ("lineaire", "attention")
AGREGATION_DE = {"lineaire": "max", "attention": "attention"}
L2 = (1e-3, 1e-2, 1e-1)
EPOQUES, PAS = 300, 0.05                      # `sondes.familles.Reglages` par défaut (point 5)
N_PLIS_INTERNES = 4
N_DIRECTIONS = 800
N_REETIQUETAGES = 100
N_TIRAGES = 2000
QUANTILE_PLANCHER = 0.95
NIVEAU_DECISIF, NIVEAU_DECISIF_REPLI, NIVEAU_RESERVE = 0.99, 0.995, 0.95
SEUIL_DEGENERES = 0.01
EX_AEQUO = 0.005
TOLERANCE_CARTE = 1e-4
FAMILLE_I, FAMILLE_II = "(i-a)", "(ii)"
SEUIL_TAUX_FA = 0.99                           # taux de détection à 1 % de fausses alarmes (règle de T0.6, point 3)

FORMES_CLES = (
    re.compile(r"bbis/interne/e[01]"),
    re.compile(r"bbis/entrainement/(sonde|enc|nul\d{1,3})/[A-Za-z0-9-]+/e[01](i\d)?/[a-z]+-c\d+-l2_[0-9.e-]+"),
    re.compile(r"bbis/plancher/[A-Za-z0-9-]+/e[01]"),
    re.compile(r"bbis/reetiquetage/[A-Za-z0-9-]+/\d{1,3}"),
    re.compile(r"bbis/egalite-carte"),
    re.compile(r"bbis/chemin-impose"),
    re.compile(r"bbis/epreuve-niveau"),
    re.compile(r"bbis/tirages/[A-Za-z0-9-]+"),
)


def exiger_agregation(agregation: str, ou: str = "score") -> str:
    """N-026 : sur les jetons d'une action, seulement le maximum ou l'attention ; jamais la moyenne ni la médiane (arrêt)."""
    if agregation not in ("max", "attention"):
        raise GardeArret(f"{ou} : agrégation {agregation!r} refusée sur les jetons d'une action ; seulement le maximum ou "
                         "l'attention ; toute moyenne ou médiane sur les jetons d'une action dans un score : arrêt (N-026)")
    return agregation


def exiger_cle(cle: str) -> str:
    if not isinstance(cle, str) or not any(f.fullmatch(cle) for f in FORMES_CLES):
        raise GardeArret(f"clé de graine {cle!r} hors des formes du texte (point 12) : refus")
    return cle


def exiger_entropie(entropie: int, reelle: bool = True) -> int:
    """Entropie de 128 bits (tirée à l'inscription de `CODE-BBIS`) ; une entropie courte (écrite à la main) est refusée en
    marche réelle."""
    if isinstance(entropie, bool) or not isinstance(entropie, int) or not 0 < entropie < 2 ** 128:
        raise GardeArret(f"entropie {entropie!r} : entier de ]0, 2^128[ attendu")
    if reelle and entropie.bit_length() <= 64:
        raise GardeArret("entropie de 64 bits ou moins en marche réelle : 128 bits tirés à l'inscription de CODE-BBIS attendus")
    return entropie


@dataclass
class Graines:
    """Graines dérivées par clé d'une même entropie (R9) ; chaque clé dérivée est consignée."""
    entropie: int
    reelle: bool = True
    derivees: dict = field(default_factory=dict)

    def __post_init__(self):
        exiger_entropie(self.entropie, self.reelle)

    def graine(self, cle: str) -> dict:
        exiger_cle(cle)
        if cle not in self.derivees:
            self.derivees[cle] = _graines_manifeste([cle], self.entropie)[cle]
        return self.derivees[cle]

    def rng(self, cle: str):
        return generateur(self.graine(cle))

    def entier(self, cle: str) -> int:
        """Entier de [0, 2^63 − 1[ tiré du générateur de la clé (graine de torch, de `default_rng`)."""
        return int(self.rng(cle).integers(0, 2 ** 63 - 1))


def nom_dose(d: float) -> str:
    from ..t06.configuration import nom_condition
    return nom_condition("saboteur", float(d))


def centiemes(d: float) -> int:
    return int(round(float(d) * 100))


def plan_doses_couches(config: dict) -> tuple[tuple[float, ...], tuple[int, ...]]:
    """Doses du saboteur et couches lues dans la configuration de 7b ; en marche réelle, elles doivent être celles du texte
    (aucune cellule choisie d'après une sortie : point 9)."""
    doses = tuple(float(d) for d in config["doses_saboteur"])
    couches = tuple(int(c) for c in config["couches"])
    if 1.0 not in doses or 1.0 not in [float(d) for d in config["doses_temoin"]]:
        raise GardeArret("configuration de 7b : dose 1 du saboteur et du témoin exigées (S100, T100)")
    if config.get("mode") == "reel" and (doses != DOSES_REELLES or couches != COUCHES_REELLES):
        raise GardeArret(f"configuration réelle : doses {doses} et couches {couches} ≠ celles du texte {DOSES_REELLES}, "
                         f"{COUCHES_REELLES}")
    if len(couches) != 3:
        raise GardeArret(f"trois couches attendues, {couches} lues")
    return doses, couches


def cellules(doses) -> dict:
    """Cellules fixées par le texte (point 9) : plafond (cinq) et transfert entre familles (cinq)."""
    plafond = {"P-instruit": {"positifs": INSTRUIT, "famille": FAMILLE_I, "dose": None}}
    transfert = {}
    for d in doses:
        c = nom_dose(d)
        plafond[f"P-{c}"] = {"positifs": c, "famille": FAMILLE_II, "dose": float(d)}
    for d in doses:
        c = nom_dose(d)
        transfert[f"T-instruit-{c}"] = {"source": "P-instruit", "positifs": c, "famille": FAMILLE_II, "dose": float(d)}
    transfert[f"T-{nom_dose(1.0)}-instruit"] = {"source": f"P-{nom_dose(1.0)}", "positifs": INSTRUIT, "famille": FAMILLE_I,
                                               "dose": None}
    return {"plafond": plafond, "transfert": transfert}


def series_imposees(doses) -> list[dict]:
    """Séries de la relecture à état imposé (point 3) : J_d, J_instruit, A_d, A_T. `adaptateur` None = modèle nu (dose 0)."""
    s = []
    for d in doses:
        s.append({"serie": f"J{centiemes(d)}", "textes": nom_dose(d), "environnement": H, "adaptateur": None, "dose": 0.0})
    s.append({"serie": "Jinstruit", "textes": INSTRUIT, "environnement": H, "adaptateur": None, "dose": 0.0})
    for d in doses:
        s.append({"serie": f"A{centiemes(d)}", "textes": H, "environnement": H, "adaptateur": "saboteur", "dose": float(d)})
    s.append({"serie": "AT", "textes": H, "environnement": H, "adaptateur": "temoin", "dose": 1.0})
    return s


def reglage_nom(famille: str, couche: int, l2: float) -> str:
    return f"{famille}-c{int(couche)}-l2_{float(l2)!r}"


def grille(couches, familles=FAMILLES, l2=L2) -> list[dict]:
    """Les 18 réglages (point 5), dans l'**ordre d'exécution** qui entrelace les deux familles (garde de débit : les vingt
    premiers apprentissages, dix de chaque famille)."""
    sortie = []
    for c in couches:
        for v in l2:
            for f in familles:
                sortie.append({"famille": f, "couche": int(c), "l2": float(v), "agregation": AGREGATION_DE[f],
                               "nom": reglage_nom(f, c, v)})
    return sortie


def rang_ex_aequo(reglage: dict, couches) -> tuple:
    """Ordre de départage des ex aequo (point 5) : linéaire avant attention, couche 15 puis 7 puis 23 (milieu, plus basse,
    plus haute), régularisation la plus forte d'abord."""
    c = sorted(int(x) for x in couches)
    ordre_couches = [c[1], c[0], c[2]]
    return (FAMILLES.index(reglage["famille"]), ordre_couches.index(int(reglage["couche"])), -float(reglage["l2"]))


__all__ = [n for n in dir() if not n.startswith("_")]
