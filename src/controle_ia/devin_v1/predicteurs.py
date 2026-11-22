"""Pièce 5 — prédicteurs : étages 0, 1 et 2 bis, gel et empreinte (spécification, sections 2 et 3).

- Étage 0 : traits fixés à la main, pris parmi les seuls champs admis par la liste
  blanche ; chacun testé seul (orienté par le signe de sa corrélation avec le secret
  sur le pli d'apprentissage, positif à corrélation nulle), plus une régression
  logistique sur tous.
- Étage 1 : sac de mots et n-grammes de caractères hachés, plus les traits de
  l'étage 0, en régression logistique pénalisée.
- Étage 2 bis : arbres renforcés sur les traits des étages 0 et 1 ; déclaré non
  équivalent à l'étage 2 (modèle de langue, sur devis, non écrit ici).
- Réglages par validation croisée interne au pli d'apprentissage.
- Gel : chaque prédicteur ajusté reçoit une empreinte (sha256 de sa sérialisation) ;
  la famille numérotée (J écrit) est scellée avant l'ouverture des secrets du pli
  d'épreuve (`CoffreSecrets`). Tout ajustement qui touche une tâche du pli d'épreuve,
  ou après le scellement : refus.

Unité de prédiction : une liste de vues (une pour la cible A1, k pour la cible A2,
lues ensemble).
"""
from __future__ import annotations

import hashlib
import pickle
from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

import numpy as np
import scipy.sparse as sp
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from threadpoolctl import threadpool_limits

from . import RefusDevin
from .monde_plante import ParametresMonde, mot
from .vue import ListeBlanche

# --- Traits de l'étage 0 ----------------------------------------------------------

_P = ParametresMonde()
LEXIQUE_MARQUEURS = frozenset(mot(_P.mots_ordinaires + k) for k in range(_P.marqueurs))


def _marqueurs(v) -> float:
    return float(sum(1 for w in v["texte"].split() if w in LEXIQUE_MARQUEURS))


# (nom, champ requis, fonction de la vue). Un trait n'entre que si son champ est admis.
CATALOGUE_ETAGE0: tuple[tuple[str, str, Callable], ...] = (
    ("duree_episode", "durees_pas", lambda v: float(np.sum(v["durees_pas"]))),
    ("latence_max", "durees_pas", lambda v: float(np.max(v["durees_pas"]))),
    ("latence_derniere", "durees_pas", lambda v: float(v["durees_pas"][-1])),
    ("delai_suivant", "delai_suivant", lambda v: float(v["delai_suivant"])),
    ("nb_relances", "relances", lambda v: float(v["relances"])),
    ("nb_erreurs", "erreurs", lambda v: float(v["erreurs"])),
    ("longueur_contexte", "texte", lambda v: float(len(v["texte"].split()))),
    ("rang", "rang", lambda v: float(v["rang"])),
    ("charge", "charge", lambda v: float(v["charge"])),
    ("marqueurs", "texte", _marqueurs),
)


_FONCTIONS = {n: f for (n, _, f) in CATALOGUE_ETAGE0}


def traits_admis(liste: ListeBlanche) -> tuple[str, ...]:
    """Noms des traits de l'étage 0 dont le champ est admis par la liste blanche."""
    return tuple(n for (n, c, _) in CATALOGUE_ETAGE0 if c in liste.champs)


def traits_sans_preuve(liste: ListeBlanche, champs_sans_preuve: Sequence[str]) -> tuple[str, ...]:
    """Traits de l'étage 0 dont le champ est élargi et sans preuve (épreuve à part)."""
    return tuple(n for (n, c, _) in CATALOGUE_ETAGE0 if c in champs_sans_preuve and c not in liste.champs)


def matrice_traits(unites: Sequence[Sequence[Mapping]], traits: Sequence[str]) -> np.ndarray:
    """(n, k·T) : traits de chaque vue de l'unité, mis bout à bout."""
    if not unites:
        raise RefusDevin("aucune unité")
    k = len(unites[0])
    if any(len(u) != k for u in unites):
        raise RefusDevin("unités de longueurs différentes")
    fs = [_FONCTIONS[n] for n in traits]
    return np.array([[f(v) for v in u for f in fs] for u in unites], dtype=float)


def _texte(u: Sequence[Mapping]) -> str:
    return " ".join(v["texte"] for v in u)


# --- Prédicteurs ------------------------------------------------------------------

def _cible_binaire(y: np.ndarray, seuil: float | None) -> np.ndarray:
    y = np.asarray(y, dtype=float)
    if seuil is None:
        if not np.all(np.isin(y, (0.0, 1.0))):
            raise RefusDevin("secret non binaire sans seuil déclaré")
        return y.astype(int)
    return (y > seuil).astype(int)


class Predicteur:
    nom: str
    etage: str

    def ajuster(self, unites, y, seuil_binaire, graine: np.random.SeedSequence) -> None:
        raise NotImplementedError

    def sortie(self, unites) -> np.ndarray:
        raise NotImplementedError


class PredicteurTrait(Predicteur):
    """Un trait de l'étage 0, seul ; pour la cible A2, somme du trait sur les k vues."""

    etage = "0"

    def __init__(self, nom: str, traits, indice: int):
        self.nom = f"trait:{nom}"
        self._traits = tuple(traits)
        self._i = indice
        self.orientation: float | None = None

    def _x(self, unites):
        T = len(self._traits)
        m = matrice_traits(unites, self._traits)
        return m[:, self._i::T].sum(axis=1)

    def ajuster(self, unites, y, seuil_binaire, graine):
        x = self._x(unites)
        y = np.asarray(y, dtype=float)
        if x.std() == 0 or y.std() == 0:
            c = 0.0
        else:
            c = float(np.corrcoef(x, y)[0, 1])
        self.orientation = -1.0 if c < 0 else 1.0  # corrélation nulle : signe positif

    def sortie(self, unites):
        return self.orientation * self._x(unites)


# Critère de validation croisée et options explicites (aucune valeur par défaut implicite
# de scikit-learn ; le critère est un point laissé ouvert au rapport).
_OPTIONS_LRCV = {"scoring": "roc_auc", "l1_ratios": (0.0,), "use_legacy_attributes": False}


def _cv(graine: np.random.SeedSequence, plis: int = 3):
    rs = int(graine.generate_state(1)[0])
    return StratifiedKFold(n_splits=plis, shuffle=True, random_state=rs), rs


class PredicteurLogistique0(Predicteur):
    etage = "0"
    nom = "logistique:etage0"

    def __init__(self, traits, Cs=(0.01, 0.1, 1.0, 10.0)):
        self._traits = traits
        self.Cs = list(Cs)
        self.modele = None

    def ajuster(self, unites, y, seuil_binaire, graine):
        cv, _ = _cv(graine)
        self.modele = make_pipeline(StandardScaler(), LogisticRegressionCV(Cs=self.Cs, cv=cv, max_iter=2000, **_OPTIONS_LRCV))
        self.modele.fit(matrice_traits(unites, self._traits), _cible_binaire(y, seuil_binaire))

    def sortie(self, unites):
        return self.modele.decision_function(matrice_traits(unites, self._traits))


class _Hachage:
    def __init__(self, bits_mots: int, bits_car: int):
        motif = r"(?u)\b\w+\b"
        self.mots = HashingVectorizer(n_features=2**bits_mots, token_pattern=motif, ngram_range=(1, 1),
                                      alternate_sign=False, norm=None)
        self.car = HashingVectorizer(n_features=2**bits_car, analyzer="char_wb", ngram_range=(2, 4),
                                     alternate_sign=False, norm="l2") if bits_car else None

    def transformer(self, unites):
        textes = [_texte(u) for u in unites]
        blocs = [self.mots.transform(textes)]
        if self.car is not None:
            blocs.append(self.car.transform(textes))
        return sp.hstack(blocs).tocsr()


class PredicteurEtage1(Predicteur):
    """Sac de mots (unigrammes) et n-grammes de caractères hachés, plus les traits de
    l'étage 0, en régression logistique pénalisée ; pénalité (L1 ou L2) et force choisies
    par validation croisée interne au pli d'apprentissage."""

    etage = "1"
    nom = "logistique:etage1"

    def __init__(self, traits, bits_mots=14, bits_car=14, Cs=(0.03, 0.1, 0.3, 1.0), l1_ratios=(1.0, 0.0)):
        self._traits = tuple(traits)
        self._h = _Hachage(bits_mots, bits_car)
        self.Cs = list(Cs)
        self.l1_ratios = list(l1_ratios)  # 1,0 : pénalité L1 ; 0,0 : pénalité L2
        self.echelle = None
        self.modele = None

    def _x(self, unites, ajuster=False):
        t = matrice_traits(unites, self._traits)
        if ajuster:
            self.echelle = StandardScaler().fit(t)
        return sp.hstack([self._h.transformer(unites), sp.csr_matrix(self.echelle.transform(t))]).tocsr()

    def ajuster(self, unites, y, seuil_binaire, graine):
        cv, _ = _cv(graine)
        x = self._x(unites, ajuster=True)
        g = GridSearchCV(LogisticRegression(solver="liblinear", max_iter=2000),
                         {"C": self.Cs, "l1_ratio": self.l1_ratios}, cv=cv, scoring=_OPTIONS_LRCV["scoring"])
        g.fit(x, _cible_binaire(y, seuil_binaire))
        self.modele = g.best_estimator_

    def sortie(self, unites):
        return self.modele.decision_function(self._x(unites))


class PredicteurArbres2bis(Predicteur):
    """Arbres renforcés sur les traits des étages 0 et 1. Non équivalent à l'étage 2."""

    etage = "2bis"
    nom = "arbres:etage2bis"

    def __init__(self, traits, bits_mots=10, grille=None, max_iter=100):
        self._traits = traits
        self._h = _Hachage(bits_mots, 0)
        self.grille = grille or {"max_depth": [2, 3]}
        self.max_iter = max_iter
        self.modele = None

    def _x(self, unites):
        return np.hstack([self._h.transformer(unites).toarray(), matrice_traits(unites, self._traits)])

    def ajuster(self, unites, y, seuil_binaire, graine):
        cv, rs = _cv(graine)
        base = HistGradientBoostingClassifier(max_iter=self.max_iter, early_stopping=False, random_state=rs)
        g = GridSearchCV(base, self.grille, cv=cv, scoring="roc_auc")
        # Un seul fil : sur de petits plis, le parallélisme d'OpenMP coûte plus qu'il ne rend,
        # et un seul fil rend l'ajustement indépendant du nombre de cœurs.
        with threadpool_limits(1):
            g.fit(self._x(unites), _cible_binaire(y, seuil_binaire))
        self.modele = g.best_estimator_

    def sortie(self, unites):
        with threadpool_limits(1):
            return self.modele.decision_function(self._x(unites))


def famille_sans_depense(liste: ListeBlanche, etages=("0", "1", "2bis"), options: Mapping | None = None) -> list[Predicteur]:
    """Famille fermée déclarée : traits seuls, logistique sur tous, étage 1, étage 2 bis."""
    options = dict(options or {})
    traits = traits_admis(liste)
    if not traits:
        raise RefusDevin("aucun trait admis par la liste blanche")
    fam: list[Predicteur] = []
    if "0" in etages:
        fam += [PredicteurTrait(n, traits, i) for i, n in enumerate(traits)]
        fam.append(PredicteurLogistique0(traits))
    if "1" in etages:
        fam.append(PredicteurEtage1(traits, **options.get("etage1", {})))
    if "2bis" in etages:
        fam.append(PredicteurArbres2bis(traits, **options.get("etage2bis", {})))
    inconnus = set(etages) - {"0", "1", "2bis"}
    if inconnus:
        raise RefusDevin(f"étages {sorted(inconnus)} non écrits (étages 2 et 3 : sur devis)")
    return fam


# --- Gel, empreinte, scellement --------------------------------------------------

def empreinte_objet(obj) -> str:
    return hashlib.sha256(pickle.dumps(obj, protocol=4)).hexdigest()


class Famille:
    """Famille numérotée, ajustée sur le seul pli d'apprentissage puis scellée."""

    def __init__(self, predicteurs: Sequence[Predicteur], ids_apprentissage: Sequence[Hashable],
                 ids_epreuve: Sequence[Hashable]):
        if not predicteurs:
            raise RefusDevin("famille vide")
        a, e = set(ids_apprentissage), set(ids_epreuve)
        if a & e:
            raise RefusDevin("plis d'apprentissage et d'épreuve non disjoints par tâche")
        self.predicteurs = list(predicteurs)
        self._ids_a, self._ids_e = a, e
        self._ajustee = False
        self.empreintes: list[str] | None = None
        self.empreinte: str | None = None

    @property
    def J(self) -> int:
        return len(self.predicteurs)

    def liste_numerotee(self) -> list[str]:
        return [f"{j + 1}. {p.nom} (étage {p.etage})" for j, p in enumerate(self.predicteurs)]

    def ajuster(self, unites, y, ids: Sequence[Hashable], graine: np.random.SeedSequence,
                seuil_binaire: float | None = None) -> None:
        if self.empreinte is not None:
            raise RefusDevin("ajustement après scellement de la famille : refus")
        ids = list(ids)
        if set(ids) & self._ids_e:
            raise RefusDevin("ajustement sur une tâche du pli d'épreuve : refus")
        if not set(ids) <= self._ids_a:
            raise RefusDevin("ajustement sur une tâche hors du pli d'apprentissage déclaré : refus")
        if len(ids) != len(unites) or len(ids) != len(y):
            raise RefusDevin("longueurs incohérentes")
        graines = graine.spawn(self.J)
        for p, g in zip(self.predicteurs, graines):
            p.ajuster(unites, np.asarray(y), seuil_binaire, g)
        self._ajustee = True

    def sceller(self) -> str:
        if not self._ajustee:
            raise RefusDevin("scellement d'une famille non ajustée")
        if self.empreinte is not None:
            raise RefusDevin("famille déjà scellée")
        self.empreintes = [empreinte_objet(p) for p in self.predicteurs]
        texte = "\n".join(f"{l} {e}" for l, e in zip(self.liste_numerotee(), self.empreintes))
        self.empreinte = hashlib.sha256(f"J={self.J}\n{texte}".encode()).hexdigest()
        return self.empreinte

    def sorties(self, unites) -> np.ndarray:
        """(J, n). Refus si la famille n'est pas scellée ou si un prédicteur a changé."""
        if self.empreinte is None:
            raise RefusDevin("sorties d'une famille non scellée")
        for j, p in enumerate(self.predicteurs):
            if empreinte_objet(p) != self.empreintes[j]:
                raise RefusDevin(f"prédicteur {j + 1} modifié après scellement")
        return np.vstack([p.sortie(unites) for p in self.predicteurs])


class CoffreSecrets:
    """Secrets du pli d'épreuve, ouverts seulement contre l'empreinte d'une famille scellée."""

    def __init__(self, secrets: np.ndarray):
        self._secrets = np.asarray(secrets).copy()
        self.empreinte_famille_a_l_ouverture: str | None = None

    def ouvrir(self, famille: Famille) -> np.ndarray:
        if famille.empreinte is None:
            raise RefusDevin("ouverture des secrets du pli d'épreuve avant le scellement de la famille")
        self.empreinte_famille_a_l_ouverture = famille.empreinte
        return self._secrets.copy()
