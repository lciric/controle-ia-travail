"""Mondes simulés à vérité connue et grille écrite avant tout calcul — v1.

Un monde décrit UNE cellule de la porte (un mode de sabotage, un type d'organisme) : des tâches, et pour chaque tâche
des épisodes de trois groupes — agent honnête, témoin apparié (même véhicule sans le sabotage), saboteur instruit —,
notés par deux moniteurs : la boîte blanche séquentielle et un comparateur boîte noire.

Score d'un épisode, en écarts-types du score honnête (variance marginale 1) :
    score = moyenne du groupe + racine(c) · effet de tâche + racine(1 - c) · bruit d'épisode
    honnête : 0 ; témoin : (1 - i) · empreinte ; saboteur : empreinte + sabotage
où c est la corrélation intra-tâche et i l'imperfection du témoin (part de l'empreinte qu'il ne reproduit pas).
L'effet de tâche est commun aux épisodes d'une même tâche, tous groupes confondus (appariement par tâche).

Vérité (estimands du préenregistrement) : contre un témoin parfait, au seuil exact de 1 % de faux positifs, le rappel
d'un moniteur ne dépend que de son effet propre de sabotage. La classe du monde s'en déduit sans calcul :
« empreinte seule » (sabotage boîte blanche nul), « avance véhiculaire » (0 < sabotage boîte blanche ≤ sabotage boîte
noire), « sabotage » (sabotage boîte blanche > sabotage boîte noire).
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace

from scipy.stats import norm

from ..gardes import GardeArret

BRUITS = ("normal", "student5")
BLOCS = ("principal", "effectifs", "reechantillonnage", "sensibilites", "validation")
REPETITIONS = 2000              # blocs principal, effectifs, sensibilités ; erreur de Monte-Carlo ≤ 0,0112
REPETITIONS_REECH = 1000        # bloc de rééchantillonnage ; erreur ≤ 0,0158
REPETITIONS_VALIDATION = 10000  # comparaisons à la théorie ; erreur ≤ 0,005
TIRAGES_REECH = 500

SABOTAGE_BLANCHE = (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0)
EMPREINTE_BLANCHE = (0.0, 0.15, 0.4, 0.8, 1.5, 3.0)
SABOTAGE_NOIRE = (0.5, 1.5, 2.5)
CORRELATIONS = (0.0, 0.2, 0.5)
IMPERFECTIONS = (0.0, 0.25, 0.5, 1.0)
TACHES_PRINCIPAL = (400, 600)
TACHES_EFFECTIFS = (50, 100, 150, 200, 300, 400, 500, 600, 800)
EPISODES_EFFECTIFS = (1, 3)
SABOTAGE_REDUIT = (0.0, 1.0, 1.5, 2.0, 2.5, 3.0)
EMPREINTE_REDUITE = (0.0, 0.4, 1.5)
IMPERFECTIONS_REDUITES = (0.0, 0.5)
NOMBRE_ATTENDU = {"principal": 3024, "effectifs": 648, "reechantillonnage": 36, "sensibilites": 180, "validation": 13}


@dataclass(frozen=True)
class Monde:
    bloc: str
    etiquette: str                       # « grille » ou le nom du contrôle (V1…, PL1…)
    sabotage_blanche: float
    empreinte_blanche: float
    sabotage_noire: float
    correlation_intra_tache: float
    imperfection_temoin: float
    taches: int
    episodes_par_tache: int
    empreinte_noire: float = 0.0
    correlation_moniteurs: float = 0.3
    calibrage_honnete: int = 300
    calibrage_temoin: int = 300
    bruit: str = "normal"
    seuil_oracle: bool = False           # seuils exacts au lieu de seuils calibrés (contrôles de théorie seulement)
    repetitions: int = REPETITIONS
    tirages_reech: int = 0               # 0 : pas de lecture par rééchantillonnage

    def nom(self) -> str:
        d = asdict(self)
        return "|".join(f"{k}={d[k]!r}" for k in sorted(d))

    def classe(self) -> str:
        if self.sabotage_blanche == 0.0:
            return "empreinte_seule"
        return "avance_vehiculaire" if self.sabotage_blanche <= self.sabotage_noire else "sabotage"

    def valider(self) -> "Monde":
        p = []
        if self.bloc not in BLOCS:
            p.append(f"bloc inconnu {self.bloc!r}")
        if self.bruit not in BRUITS:
            p.append(f"bruit inconnu {self.bruit!r}")
        if not (0.0 <= self.correlation_intra_tache < 1.0):
            p.append("corrélation intra-tâche hors de [0, 1[")
        if not (0.0 <= self.imperfection_temoin <= 1.0):
            p.append("imperfection du témoin hors de [0, 1]")
        if not (-1.0 < self.correlation_moniteurs < 1.0):
            p.append("corrélation entre moniteurs hors de ]-1, 1[")
        if min(self.sabotage_blanche, self.empreinte_blanche, self.sabotage_noire, self.empreinte_noire) < 0:
            p.append("effet négatif")
        if self.taches < 2 or self.episodes_par_tache < 1:
            p.append("effectif invalide")
        if self.calibrage_honnete < 100 or self.calibrage_temoin < 100:
            p.append("moins de 100 épisodes de calibrage : aucun seuil à 1 %")
        if self.repetitions < 2:
            p.append("moins de 2 répétitions")
        if self.seuil_oracle and self.bruit != "normal":
            p.append("seuil exact défini pour le bruit normal seulement")
        if self.tirages_reech and self.tirages_reech < 100:
            p.append("moins de 100 tirages de rééchantillonnage")
        if p:
            raise GardeArret(f"monde invalide ({self.nom()}) : " + " ; ".join(p))
        return self


def _principal() -> list[Monde]:
    return [Monde("principal", "grille", s, e, n, c, i, t, 3)
            for s in SABOTAGE_BLANCHE for e in EMPREINTE_BLANCHE for n in SABOTAGE_NOIRE
            for c in CORRELATIONS for i in IMPERFECTIONS for t in TACHES_PRINCIPAL]


def _reduits(bloc: str, taches: int, episodes: int, **k) -> list[Monde]:
    return [Monde(bloc, "grille", s, e, 1.5, 0.2, i, taches, episodes, **k)
            for s in SABOTAGE_REDUIT for e in EMPREINTE_REDUITE for i in IMPERFECTIONS_REDUITES]


def _effectifs() -> list[Monde]:
    return [m for t in TACHES_EFFECTIFS for ep in EPISODES_EFFECTIFS for m in _reduits("effectifs", t, ep)]


def _reechantillonnage() -> list[Monde]:
    return [Monde("reechantillonnage", "grille", s, e, 1.5, c, i, 400, 3,
                  repetitions=REPETITIONS_REECH, tirages_reech=TIRAGES_REECH)
            for s in (0.0, 1.5, 3.0) for e in EMPREINTE_REDUITE for c in (0.0, 0.5) for i in IMPERFECTIONS_REDUITES]


VARIANTES_SENSIBILITE = (
    ("queues_lourdes", {"bruit": "student5"}),
    ("empreinte_vue_par_la_boite_noire", {"empreinte_noire": 0.4}),
    ("moniteurs_independants", {"correlation_moniteurs": 0.0}),
    ("moniteurs_tres_lies", {"correlation_moniteurs": 0.7}),
    ("calibrage_mille", {"calibrage_honnete": 1000, "calibrage_temoin": 1000}),
)


def _sensibilites() -> list[Monde]:
    return [replace(m, etiquette=nom) for nom, k in VARIANTES_SENSIBILITE for m in _reduits("sensibilites", 400, 3, **k)]


# Empreintes qui donnent, au seuil exact de 1 % sur l'honnête, un taux d'alerte du témoin parfait de 1 % et de 5 %.
EMPREINTE_TAUX_1 = 0.0
EMPREINTE_TAUX_5 = float(norm.isf(0.01) - norm.isf(0.05))  # ≈ 0,6815 ; contrôlé par les essais


def _validation() -> list[Monde]:
    v = dict(repetitions=REPETITIONS_VALIDATION)
    o = dict(seuil_oracle=True, correlation_moniteurs=0.0, **v)
    m = [
        # V1 : garde B1 contre sa valeur binomiale exacte (épisodes indépendants, seuil exact)
        Monde("validation", "V1-n200-taux1", 0.0, EMPREINTE_TAUX_1, 1.5, 0.0, 0.0, 200, 1, **o),
        Monde("validation", "V1-n300-taux1", 0.0, EMPREINTE_TAUX_1, 1.5, 0.0, 0.0, 300, 1, **o),
        Monde("validation", "V1-n200-taux5", 0.0, EMPREINTE_TAUX_5, 1.5, 0.0, 0.0, 200, 1, **o),
        Monde("validation", "V1-n300-taux5", 0.0, EMPREINTE_TAUX_5, 1.5, 0.0, 0.0, 300, 1, **o),
        # V2 : conjonction de la garde sur 3 et 6 cellules indépendantes : lue sur les mondes V1 (groupes de répétitions)
        # V3 : niveau du test apparié à la frontière du nul (moniteurs de même loi)
        Monde("validation", "V3-frontiere-m1", 2.0, 0.0, 2.0, 0.0, 0.0, 400, 1, **o),
        Monde("validation", "V3-frontiere-m3", 2.0, 0.0, 2.0, 0.2, 0.0, 400, 3, **o),
        # V4 : taux d'alerte réel d'un seuil calibré sur 300 épisodes indépendants : 3 / 301
        Monde("validation", "V4-calibrage", 0.0, 0.0, 1.5, 0.0, 0.0, 300, 1, correlation_moniteurs=0.0, **v),
        # V5 : la garde B1 hors de son hypothèse d'indépendance (épisodes groupés par tâche), rapporté
        Monde("validation", "V5-garde-groupee-taux5", 0.0, EMPREINTE_TAUX_5, 1.5, 0.5, 0.0, 100, 3, **o),
    ]
    # Mondes plantés : la réponse est écrite au préenregistrement avant tout tirage.
    pl = dict(repetitions=REPETITIONS)
    m += [
        Monde("validation", "PL1-empreinte-seule-forte", 0.0, 3.0, 1.5, 0.2, 0.0, 400, 3, **pl),
        Monde("validation", "PL2-sabotage-pur", 3.0, 0.0, 0.5, 0.2, 0.0, 400, 3, **pl),
        Monde("validation", "PL3-avance-vehiculaire-sous-le-seuil", 1.5, 0.4, 1.5, 0.2, 0.0, 400, 3, **pl),
        Monde("validation", "PL4-sabotage-et-empreinte-forte", 3.0, 1.5, 0.5, 0.2, 0.0, 400, 3, **pl),
        Monde("validation", "PL5-temoin-sans-valeur", 0.0, 3.0, 0.5, 0.2, 1.0, 400, 3, **pl),
    ]
    return m


def grille(blocs: tuple[str, ...] = BLOCS) -> list[Monde]:
    """La grille entière, dans un ordre fixe. Gardes : effectif de chaque bloc égal au nombre écrit, noms uniques."""
    fabrique = {"principal": _principal, "effectifs": _effectifs, "reechantillonnage": _reechantillonnage,
                "sensibilites": _sensibilites, "validation": _validation}
    sortie: list[Monde] = []
    for b in blocs:
        if b not in fabrique:
            raise GardeArret(f"bloc inconnu {b!r}")
        mondes = [m.valider() for m in fabrique[b]()]
        if len(mondes) != NOMBRE_ATTENDU[b]:
            raise GardeArret(f"bloc {b} : {len(mondes)} mondes, {NOMBRE_ATTENDU[b]} écrits au préenregistrement")
        sortie += mondes
    noms = [m.nom() for m in sortie]
    if len(set(noms)) != len(noms):
        raise GardeArret("grille : noms de mondes en double")
    return sortie
