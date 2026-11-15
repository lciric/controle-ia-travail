"""Banc B v2 de l'idée 1.2 (préenregistrement scellé `bdabf2bc…`, section « Plan d'analyse ») : archive A2, mondes et
cartes des familles T et N, graines, plans, gel des engagements, issues fraîches, évaluation par le juge réel, rapport
exact Λ (famille N), essai E1.

Graines (R9, section « Graines ») : racine = entier de l'empreinte sha256 du texte scellé ;
`numpy.random.SeedSequence(entropy=racine, spawn_key=clé)`, famille 0 = N, 1 = T : monde `(f, g, 24)` ; archive
`(f, g, 25)` ; construction de la carte i `(f, g, i, 0)` ; plan, entraînement et issues d'entraînement `(f, g, i, 1)` ;
issues fraîches `(f, g, i, 2)`, tirées après le gel de tous les engagements de la génération ; positions
`(f, g, 1001)` ; placebo `(f, g, 1000)` ; oracle `(f, g, 2000)`.

Ordre des tirages dans chaque générateur (lecture du texte, dite au rapport) :
- archive : S1, S2, U1, U2, U3, U4 (softmax aléatoires), jA, s_A, s_B ;
- monde, famille T : paramètres de la composante de la cellule ; famille N : M₀ (poids de Dirichlet) ou M₀′ (loi de
  base parmi S1 et S2, puissance, inclinaison), puis la composante de la cellule portée par les deux porteuses
  construites (et référence du cosinus des deux fausses construites) ;
- oracle : 20 000 instances (traits, puis sous-populations), puis 20 000 uniformes pour les issues ;
- plan : 800 instances, puis 100 instances d'entraînement, puis 100 uniformes pour leurs issues ;
- issues fraîches : 800 uniformes, issue par inversion (`selection_pari.tirer_categorie`) sur `selection_pari.proba`.
Montage de l'évaluation (comme `a_blanc_v59.juger_carte`, différences de montage déclarées au texte, section
« Écarts ») : bibliothèque standard + marginale d'entraînement (`controles_pari._frequences`) +
`nul_v8.membres_archive_v8(archive A2)` ; `nul_filles_v2.construire_engagement_v2`, plan « ordre_naturel », 32 instants
25…800 ; `selection_pari.geler_engagement` ; `nul_filles_v2.evaluer_v2` ; on ne garde que `trajectoire_log_w`.
"""
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass, field

import numpy as np

from ..gardes import GardeArret
from . import lois_v1 as L

# --- paramètres gelés par le texte -----------------------------------------------------------------------------------
EMPREINTE_PREREG = "bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e"
CHEMIN_PREREG = "prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md"
K, D = L.K, L.D
ALPHA, M = 0.05, 24
BLOC, N_MAX, PART, ENTRAINEMENT = 25, 800, 200, 100
NB_INSTANTS = N_MAX // BLOC                     # 32
INSTANTS = tuple(BLOC * (k + 1) for k in range(NB_INSTANTS))
ORACLE_N = 20_000
PLAFOND_COSINUS = 1_000
FAMILLES = {"N": 0, "T": 1}
GENERATIONS = {"N": 500, "T": 750}
BORNE_M0 = 250                                   # famille N : M₀ pour g < 250, M₀′ pour g ≥ 250
SORTES = {
    "T": ("porteuses",) * 6 + ("copies de la classe",) * 6 + ("copies par morceaux",) * 4
         + ("fausses construites",) * 6 + ("nulles",) * 2,
    "N": ("voisines",) * 8 + ("membres exacts",) * 8 + ("porteuses construites",) * 2 + ("copies par morceaux",) * 2
         + ("fausses construites",) * 2 + ("nulles",) * 2,
}
SORTES_UNIQUES = {f: tuple(dict.fromkeys(s)) for f, s in SORTES.items()}
SORTE_MEMBRE_EXACT = {"T": "copies de la classe", "N": "membres exacts"}
SORTE_PORTEUSE = {"T": "porteuses", "N": "porteuses construites"}
CHAMPS_INTERDITS = ("promue", "t_promotion", "log_richesse_max", "log_richesse_arretee", "log_richesse_finale")


def racine_de(empreinte_hex: str) -> int:
    if len(empreinte_hex) != 64 or any(c not in "0123456789abcdef" for c in empreinte_hex):
        raise GardeArret(f"racine : empreinte sha256 hexadécimale attendue, reçu {empreinte_hex!r}")
    return int(empreinte_hex, 16)


def generateur(racine: int, *cle: int) -> np.random.Generator:
    if any((not isinstance(c, (int, np.integer))) or c < 0 for c in cle):
        raise GardeArret(f"clé de graine invalide {cle!r}")
    return np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=tuple(int(c) for c in cle)))


def etat_graine(racine: int, *cle: int) -> list[int]:
    return [int(x) for x in np.random.SeedSequence(entropy=racine, spawn_key=tuple(int(c) for c in cle)).generate_state(2)]


def empreinte_json(objet) -> str:
    return hashlib.sha256(json.dumps(objet, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


# --- archive, monde -------------------------------------------------------------------------------------------------
def construire_archive(racine: int, f: int, g: int) -> dict:
    rng = generateur(racine, f, g, 25)
    S1, S2, U1, U2, U3, U4 = (L.softmax_aleatoire(rng) for _ in range(6))
    jA = int(rng.integers(0, 2))
    sA = L.coupure_archive(rng)
    sB = L.coupure_archive(rng)
    S3 = L.si_sinon_trait(jA, sA, U1, U2)
    S4 = L.si_sinon_trait(1 - jA, sB, U3, U4)
    return {"S1": S1, "S2": S2, "S3": S3, "S4": S4, "U": [U1, U2, U3, U4], "jA": jA, "sA": sA, "sB": sB,
            "cut": {jA: sA, 1 - jA: sB}}


def lois_archive(archive: dict) -> dict:
    return {n: archive[n] for n in ("S1", "S2", "S3", "S4")}


@dataclass
class Monde:
    loi: dict
    composante: L.Composante            # T : composante du monde ; N : composante de la cellule (portée par les porteuses construites)
    details: dict


def construire_monde(racine: int, famille: str, g: int, archive: dict) -> Monde:
    f = FAMILLES[famille]
    rng = generateur(racine, f, g, 24)
    genre, i_dose, dose = L.cellule(g)
    if famille == "T":
        comp = L.tirer_composante(genre, dose, archive, rng)
        return Monde(comp.loi(1.0), comp, {"famille": "T", "cellule": g % 10, "type": genre, "dose": dose,
                                            "dose_haute": bool(i_dose), "composante": comp.resume()})
    if g < BORNE_M0:
        loi = L.melange_archive(archive, rng)
        details = {"famille": "N", "monde": "M0", "poids": loi["poids"]}
    else:
        k = int(rng.integers(0, 2))
        base = archive[("S1", "S2")[k]]
        loi = L.tempere_incline(base, rng)
        details = {"famille": "N", "monde": "M0prime", "base": ("S1", "S2")[k], "puissance": loi["puissance"],
                   "inclinaison": loi["inclinaison"]}
    comp = L.tirer_composante(genre, dose, archive, rng)
    details.update(cellule=g % 10, type=genre, dose=dose, dose_haute=bool(i_dose), composante=comp.resume())
    return Monde(loi, comp, details)


# --- échantillon de l'oracle --------------------------------------------------------------------------------------------
@dataclass
class Echantillon:
    Z: np.ndarray
    G: np.ndarray
    y: np.ndarray
    cle: tuple
    empreinte: str


def tirer_instances_np(rng: np.random.Generator, n: int) -> tuple[np.ndarray, np.ndarray]:
    Z = np.round(rng.standard_normal((n, D)), 6)
    G = rng.integers(0, 2, size=n)
    return Z, G


def echantillon_oracle(racine: int, f: int, g: int, monde: dict) -> Echantillon:
    rng = generateur(racine, f, g, 2000)
    Z, G = tirer_instances_np(rng, ORACLE_N)
    u = rng.random(ORACLE_N)
    y = L.tirer_issues_np(L.probas_np(monde, Z, G), u)
    h = hashlib.sha256(Z.tobytes() + G.astype(np.int64).tobytes() + y.tobytes()).hexdigest()
    return Echantillon(Z, G, y, (f, g, 2000), h)


# --- cartes -------------------------------------------------------------------------------------------------------------
@dataclass
class Carte:
    indice: int
    sorte: str
    loi: dict
    details: dict = field(default_factory=dict)

    @property
    def empreinte(self) -> str:
        return empreinte_json(self.loi)


def fausse_construite(genre: str, dose: float, archive: dict, p_ref: np.ndarray, p_s1: np.ndarray,
                      ech: Echantillon, rng: np.random.Generator) -> tuple[dict, dict]:
    """S1 portant une composante de même type et de même dose, tirée indépendamment, retirée tant que son cosinus avec
    la composante de référence (f = p_ref − S1) dépasse 0 ; au plus 1 000 tirages, sinon la carte de plus petit cosinus
    est gardée et signalée (O1 : même règle en famille N)."""
    meilleure, cos_min = None, math.inf
    for essai in range(1, PLAFOND_COSINUS + 1):
        comp = L.tirer_composante(genre, dose, archive, rng)
        loi = comp.loi(1.0)
        c = L.cosinus(p_ref, L.probas_np(loi, ech.Z, ech.G), p_s1)
        if c < cos_min:
            meilleure, cos_min = loi, c
        if c <= 0.0:
            return loi, {"cosinus": c, "tirages": essai, "plafond_atteint": False}
    return meilleure, {"cosinus": cos_min, "tirages": PLAFOND_COSINUS, "plafond_atteint": True}


def cartes_T(racine: int, g: int, archive: dict, monde: Monde, ech: Echantillon) -> list[Carte]:
    f = FAMILLES["T"]
    comp = monde.composante
    S1, S2, S3, S4 = archive["S1"], archive["S2"], archive["S3"], archive["S4"]
    p_s1 = L.probas_np(S1, ech.Z, ech.G)
    p_monde = L.probas_np(monde.loi, ech.Z, ech.G)
    sortes = SORTES["T"]
    cartes = []
    for i in range(M):
        rng = generateur(racine, f, g, i, 0)
        details = {}
        if i == 0:
            loi = comp.loi(1.0); details["construction"] = "M"
        elif i == 1:
            loi = comp.loi(0.5); details["construction"] = "M force x0.5"
        elif i == 2:
            loi = comp.loi(1.5); details["construction"] = "M force x1.5"
        elif i == 3:
            loi = comp.bruitee(rng, 0.3).loi(1.0); details["construction"] = "M direction bruitée (0,3)"
        elif i in (4, 5):
            loi = L.perturber_poids(monde.loi, rng, 0.01); details["construction"] = "doublon de M"
        elif i in (6, 7, 8):
            loi = L.melange_archive(archive, rng); details["construction"] = "melange des lois d'archive"
        elif i in (9, 10, 11):
            base = ("S1", "S2", "S3", "S4")[int(rng.integers(0, 4))]
            loi = L.tempere_incline(archive[base], rng); details["construction"] = f"transformee de {base}"
        elif i == 12:
            loi = L.si_sinon_trait(archive["jA"], archive["sA"], S1, S2); details["construction"] = "si_sinon coupure A (S1, S2)"
        elif i == 13:
            loi = L.si_sinon_trait(1 - archive["jA"], archive["sB"], S1, S2); details["construction"] = "si_sinon coupure B (S1, S2)"
        elif i == 14:
            loi = L.par_sous_population(S1, S2); details["construction"] = "par_sous_population (S1, S2)"
        elif i == 15:
            j = int(rng.integers(0, 2))
            loi = L.si_sinon_trait(j, 0.0, S2, S1); details["construction"] = f"si_sinon signe du trait {j} (S2, S1)"
        elif 16 <= i <= 19 or (i in (20, 21) and comp.genre == "V4"):
            loi, d = fausse_construite(comp.genre, comp.dose, archive, p_monde, p_s1, ech, rng)
            details.update(d, construction="fausse construite (règle du cosinus)")
        elif i == 20:
            loi = comp.loi(-1.0); details["construction"] = "signe opposé, force x1"
        elif i == 21:
            loi = comp.loi(-0.5); details["construction"] = "signe opposé, force x0.5"
        else:
            loi = L.softmax_aleatoire(rng); details["construction"] = "nulle"
        cartes.append(Carte(i, sortes[i], loi, details))
    return cartes


def cartes_N(racine: int, g: int, archive: dict, monde: Monde, ech: Echantillon) -> list[Carte]:
    f = FAMILLES["N"]
    comp = monde.composante
    S1, S2 = archive["S1"], archive["S2"]
    p_s1 = L.probas_np(S1, ech.Z, ech.G)
    porteuse_x1 = comp.loi(1.0)
    p_porteuse = L.probas_np(porteuse_x1, ech.Z, ech.G)
    sortes = SORTES["N"]
    cartes = []
    for i in range(M):
        rng = generateur(racine, f, g, i, 0)
        details = {}
        if i < 8:
            delta = L.delta_centre(rng)
            if g < BORNE_M0:
                W1, b1 = L.poids_de(S1)
                voisine = L.softmax(W1 + 0.05 * delta, b1)
                loi = L.melange([voisine] + monde.loi["composantes"][1:], monde.loi["poids"])
                details["construction"] = "voisine de M0 (S1 remplacée)"
            else:
                nom = monde.details["base"]
                Wk, bk = L.poids_de(archive[nom])
                loi = L.transformee(L.softmax(Wk + 0.05 * delta, bk), monde.loi["puissance"], monde.loi["inclinaison"])
                details["construction"] = f"voisine de M0prime ({nom} remplacée)"
        elif i == 8:
            loi = monde.loi; details["construction"] = "le monde"
        elif i <= 12:
            loi = L.melange_archive(archive, rng); details["construction"] = "melange des lois d'archive"
        elif i <= 15:
            base = ("S1", "S2", "S3", "S4")[int(rng.integers(0, 4))]
            loi = L.tempere_incline(archive[base], rng); details["construction"] = f"transformee de {base}"
        elif i == 16:
            loi = porteuse_x1; details["construction"] = "porteuse construite x1"
        elif i == 17:
            loi = comp.loi(0.5); details["construction"] = "porteuse construite x0.5"
        elif i == 18:
            loi = L.si_sinon_trait(archive["jA"], archive["sA"], S1, S2); details["construction"] = "si_sinon coupure A (S1, S2)"
        elif i == 19:
            loi = L.par_sous_population(S1, S2); details["construction"] = "par_sous_population (S1, S2)"
        elif i in (20, 21):
            # O2 : référence du cosinus = composante de la cellule à la dose de la cellule (porteuse construite x1).
            loi, d = fausse_construite(comp.genre, comp.dose, archive, p_porteuse, p_s1, ech, rng)
            details.update(d, construction="fausse construite (règle du cosinus, référence : porteuse x1)")
        else:
            loi = L.softmax_aleatoire(rng); details["construction"] = "nulle"
        cartes.append(Carte(i, sortes[i], loi, details))
    return cartes


# --- génération : construction, engagements, gel, issues fraîches, évaluation ----------------------------------------------
class _Uniformes:
    """Adaptateur : `selection_pari.tirer_categorie(rng, p)` lit un uniforme par appel à `rng.random()`."""

    def __init__(self, u):
        self._u = iter(np.asarray(u, dtype=float).tolist())

    def random(self) -> float:
        return next(self._u)


def instances_dicts(Z: np.ndarray, G: np.ndarray) -> list[dict]:
    return [{"z": [float(a) for a in z], "g": int(gv)} for z, gv in zip(Z, G)]


def bibliotheque(J, q_ent: list, archive: dict) -> list:
    """Bibliothèque du juge comme `a_blanc_v59.juger_carte` : standard + marginale d'entraînement + nul v8 de l'archive."""
    standard = list(J.sp.BIBLIOTHEQUE_STANDARD) + [{"nom": "marginale_entrainement", "type": "fixe", "probas": q_ent}]
    return standard + J.nul_v8.membres_archive_v8(dict(lois_archive(archive)), None, K, D)


def construire_engagement(J, identifiant: str, loi: dict, plan: list, q_ent: list, archive: dict, n: int = N_MAX):
    """Engagement gelé d'une carte. Ne reçoit **aucune** issue fraîche (garde : appelé par `Generation` seulement dans
    l'état « construite », aucun flux frais ouvert)."""
    biblio = bibliotheque(J, q_ent, archive)
    e = J.nf.construire_engagement_v2(identifiant, loi, plan[:n], K, ALPHA, biblio, 0, None,
                                      J.cycle.instants_reguliers(n, n // BLOC), plan_execution="ordre_naturel")
    return J.sp.geler_engagement(e), biblio


class EvaluationFiltree:
    """Évaluation à 800 réduite à sa trajectoire aux 32 instants ; tout autre champ est refusé (F ne se lit jamais sur
    `promue`, `t_promotion`, `log_richesse_max`, `log_richesse_arretee`)."""

    __slots__ = ("_traj",)

    def __init__(self, trajectoire):
        traj = tuple(float(v) for v in trajectoire)
        if len(traj) != NB_INSTANTS:
            raise GardeArret(f"trajectoire de {len(traj)} instants au lieu de {NB_INSTANTS}")
        if not all(math.isfinite(v) for v in traj):
            raise GardeArret("log W non fini : arrêt du run (liste d'arrêt)")
        self._traj = traj

    def __getitem__(self, cle):
        if cle == "trajectoire_log_w":
            return self._traj
        if cle in CHAMPS_INTERDITS:
            raise GardeArret(f"champ « {cle} » de l'évaluation à 800 : interdit (F se lit sur la trajectoire tronquée)")
        raise GardeArret(f"champ « {cle} » absent de l'évaluation filtrée")

    def get(self, cle, defaut=None):
        return self[cle]


def trajectoire_de(J, gele, issues: list) -> tuple:
    """Trajectoire log W aux instants 25, 50, …, n d'un engagement gelé (plan de n), par `nul_filles_v2.evaluer_v2`."""
    tirages = {"empreinte_engagement": gele.empreinte, "issues": list(issues), "plan_execution": "ordre_naturel"}
    ev = J.nf.evaluer_v2(gele, tirages)
    attendus = list(J.cycle.instants_reguliers(len(issues), len(issues) // BLOC))
    if ev.get("instants_lecture") != attendus:
        raise GardeArret(f"instants de lecture {ev.get('instants_lecture')} ≠ {attendus}")
    return tuple(ev["trajectoire_log_w"])


def evaluer_carte(J, gele, issues: list) -> EvaluationFiltree:
    """Évaluation d'une carte sur son plan de 800, réduite à sa trajectoire (évaluation filtrée)."""
    if len(issues) != N_MAX:
        raise GardeArret(f"évaluation de jeu : {len(issues)} issues au lieu de {N_MAX}")
    return EvaluationFiltree(trajectoire_de(J, gele, issues))


def cle_flux_frais(f: int, g: int, i: int) -> tuple:
    return (f, g, i, 2)


class Generation:
    """Une génération : construite → engagements → gelée → tirée → évaluée. Les gardes de l'ordre du gel ([CL-1.1] m1)
    et du flux propre par carte vivent ici."""

    def __init__(self, racine: int, famille: str, g: int):
        if famille not in FAMILLES or not 0 <= g < GENERATIONS[famille]:
            raise GardeArret(f"génération hors du banc : {famille} {g}")
        self.racine, self.famille, self.g, self.f = racine, famille, g, FAMILLES[famille]
        self.archive = construire_archive(racine, self.f, g)
        self.monde = construire_monde(racine, famille, g, self.archive)
        self.echantillon = echantillon_oracle(racine, self.f, g, self.monde.loi)
        constructeur = cartes_T if famille == "T" else cartes_N
        self.cartes = constructeur(racine, g, self.archive, self.monde, self.echantillon)
        if [c.sorte for c in self.cartes] != list(SORTES[famille]):
            raise GardeArret("composition des sortes différente du texte")
        self.positions = [int(p) for p in generateur(racine, self.f, g, 1001).permutation(M)]
        self.etat = "construite"
        self.flux_ouverts: list = []
        self.engagements: dict = {}
        self.plans: dict = {}
        self.issues: dict | None = None
        self.evaluations: dict | None = None

    # identité
    @property
    def nom(self) -> str:
        return f"{self.famille}{self.g}"

    def resume(self) -> dict:
        return {"famille": self.famille, "g": self.g, "monde": self.monde.details, "positions": self.positions,
                "cartes": [{"indice": c.indice, "sorte": c.sorte, "empreinte_loi": c.empreinte, **c.details} for c in self.cartes],
                "echantillon_oracle": {"cle": list(self.echantillon.cle), "empreinte": self.echantillon.empreinte}}

    # engagements
    def preparer_engagements(self, J) -> None:
        if self.etat != "construite" or self.flux_ouverts or self.issues is not None:
            raise GardeArret(f"{self.nom} : engagements bâtis après l'ouverture d'un flux frais (gel avant les issues fraîches)")
        f, g = self.f, self.g
        for c in self.cartes:
            rng = generateur(self.racine, f, g, c.indice, 1)
            Zp, Gp = tirer_instances_np(rng, N_MAX)
            Ze, Ge = tirer_instances_np(rng, ENTRAINEMENT)
            u = rng.random(ENTRAINEMENT)
            plan, entr = instances_dicts(Zp, Gp), instances_dicts(Ze, Ge)
            src = _Uniformes(u)
            y_ent = [J.sp.tirer_categorie(src, J.sp.proba(self.monde.loi, x, [], 0)) for x in entr]
            q_ent = J.controles_pari._frequences(y_ent, K)
            gele, _ = construire_engagement(J, f"idee12-f{f}-g{g}-c{c.indice}", c.loi, plan, q_ent, self.archive)
            self.engagements[c.indice] = gele
            self.plans[c.indice] = {"plan": plan, "q_ent": q_ent}
        if self.flux_ouverts:
            raise GardeArret(f"{self.nom} : un flux frais a été ouvert pendant la construction des engagements")
        self.etat = "engagements"

    def geler(self) -> None:
        if self.etat != "engagements" or sorted(self.engagements) != list(range(M)):
            raise GardeArret(f"{self.nom} : gel demandé sans les 24 engagements bâtis")
        if self.flux_ouverts or self.issues is not None:
            raise GardeArret(f"{self.nom} : issue fraîche tirée avant le gel")
        self.empreintes_gel = {i: e.empreinte for i, e in self.engagements.items()}
        self.etat = "gelee"

    def ouvrir_flux_frais(self, i: int) -> np.random.Generator:
        cle = cle_flux_frais(self.f, self.g, i)
        self.flux_ouverts.append((i, tuple(cle), etat_graine(self.racine, *cle)))
        return generateur(self.racine, *cle)

    def tirer_frais(self, J) -> None:
        if self.etat != "gelee":
            raise GardeArret(f"{self.nom} : issues fraîches demandées avant le gel de tous les engagements")
        issues = {}
        for c in self.cartes:
            rng = self.ouvrir_flux_frais(c.indice)
            u = rng.random(N_MAX)
            plan = self.plans[c.indice]["plan"]
            src, ys = _Uniformes(u), []
            for t, x in enumerate(plan):
                ys.append(J.sp.tirer_categorie(src, J.sp.proba(self.monde.loi, x, ys, t)))
            issues[c.indice] = ys
        cles = [cle for _, cle, _ in self.flux_ouverts]
        etats = [tuple(e) for _, _, e in self.flux_ouverts]
        attendues = [(self.f, self.g, i, 2) for i in range(M)]
        if cles != attendues or len(set(etats)) != M:
            raise GardeArret(f"{self.nom} : flux d'issues fraîches partagé ou mal dérivé ({cles[:3]}…)")
        for i, e in self.empreintes_gel.items():
            if self.engagements[i].empreinte != e or J.outils.empreinte_objet(self.engagements[i].engagement) != e:
                raise GardeArret(f"{self.nom} : engagement {i} modifié après le gel")
        self.issues = issues
        self.etat = "tiree"

    def evaluer(self, J) -> dict:
        if self.etat != "tiree":
            raise GardeArret(f"{self.nom} : évaluation avant les issues fraîches")
        self.evaluations = {i: evaluer_carte(J, self.engagements[i], self.issues[i]) for i in range(M)}
        self.etat = "evaluee"
        return self.evaluations

    def log_lambda(self, J) -> dict:
        """Famille N : log Λ_t = log q(y_1..t) − log P*(y_1..t) aux 32 instants (loi connue du monde, `selection_pari`)."""
        if self.famille != "N" or self.issues is None:
            raise GardeArret("rapport exact Λ : famille N, après les issues fraîches")
        sortie = {}
        for c in self.cartes:
            plan, ys = self.plans[c.indice]["plan"], self.issues[c.indice]
            cache = J.sp.Cache(ys, plan)
            num = J.sp.trajectoire_loi(c.loi, ys, plan, cache)
            vrai = J.sp.trajectoire_loi(self.monde.loi, ys, plan, cache)
            sortie[c.indice] = [num[t - 1] - vrai[t - 1] for t in INSTANTS]
        return sortie


def domination(trajectoire, log_lambda, tolerance: float = 1e-6) -> list[tuple[int, float]]:
    """Instants (indice, excès) où log W_t > log Λ_t + 10⁻⁶ (lecture (2))."""
    return [(k, w - l) for k, (w, l) in enumerate(zip(trajectoire, log_lambda)) if w > l + tolerance]


# --- essai E1 ------------------------------------------------------------------------------------------------------------
def essai_E1_carte(J, gen: Generation, i: int, evaluation_800=None, instants=INSTANTS) -> dict:
    """Pour chacun des 32 instants t : (a) trajectoire du plan de 800 tronquée à t = trajectoire d'un plan de t ;
    (b) valeurs aux instants ≤ t inchangées quand les issues au-delà de t sont remplacées (y → (y + 1) mod 3)."""
    plan, q_ent = gen.plans[i]["plan"], gen.plans[i]["q_ent"]
    ys = gen.issues[i]
    if evaluation_800 is None:
        evaluation_800 = evaluer_carte(J, gen.engagements[i], ys)
    complet = list(evaluation_800["trajectoire_log_w"])
    echecs = []
    for t in instants:
        k = INSTANTS.index(t)
        gele_t, _ = construire_engagement(J, f"E1-{gen.nom}-c{i}-t{t}", gen.cartes[i].loi, plan, q_ent, gen.archive, n=t)
        traj_t = list(trajectoire_de(J, gele_t, ys[:t]))
        if traj_t != complet[:k + 1]:
            echecs.append({"t": t, "essai": "plan de t", "attendu": complet[:k + 1], "obtenu": traj_t})
        remplacees = list(ys[:t]) + [(y + 1) % K for y in ys[t:]]
        traj_r = list(evaluer_carte(J, gen.engagements[i], remplacees)["trajectoire_log_w"])
        if traj_r[:k + 1] != complet[:k + 1]:
            echecs.append({"t": t, "essai": "issues au-delà de t remplacées", "attendu": complet[:k + 1], "obtenu": traj_r[:k + 1]})
    return {"generation": gen.nom, "carte": i, "sorte": gen.cartes[i].sorte, "instants": len(instants), "echecs": echecs,
            "trajectoire": complet}


CARTES_E1 = tuple([("T", 0, i) for i in range(M)] + [("N", 0, i) for i in range(M)] + [("T", 1, 0), ("T", 1, 1)])
