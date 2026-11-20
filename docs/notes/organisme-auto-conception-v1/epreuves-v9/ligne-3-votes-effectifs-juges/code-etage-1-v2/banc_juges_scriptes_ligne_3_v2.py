"""Banc de juges scriptés de la ligne 3 (« votes effectifs des juges croisés »), étage 1 sur processeur — v2.

Texte qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`
(main, sha256 4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0), sections « 0 », « Métrique »,
« Seuil », « Plan d'analyse » (étage 1 seulement), « Graines (règle R9), ordre des gestes », « Critères de lecture
gelés », « Liste d'arrêt », annexe A. Rien de l'étage 2 n'est écrit ici.

Processeur seul ; `numpy` et la bibliothèque standard ; aucun appel de modèle, aucun réseau. Les seuls fichiers lus
sont ce programme (empreinte au manifeste) et, pour une racine sous autorisation, l'additif de code dont l'empreinte
est donnée en argument.

Graines (R9) : `numpy.random.SeedSequence(racine, spawn_key=(clé,))`, clé entière tirée de `TABLE_CLES` (gelée ici,
recopiée au manifeste) ; une cellule reçoit l'enfant de rang fixe de `.spawn(nombre)`, dans l'ordre gelé
d'énumération des cellules. Racines : essais 2026111930 (seule dérivable sans autorisation) ; chronométrage
2026111931, étage 1 décisif 2026111932, rééchantillonnage de l'étage 1 2026111933 (refus sans autorisation) ;
2026111934 à 2026111937 (étage 2) : toujours refusées par ce code.

Usage (geste 4 seulement, après l'additif de code scellé ; jamais lancé par le développeur) :
    python3 -B banc_juges_scriptes_ligne_3_v2.py --decisif --autorisation-additif CHEMIN --empreinte-additif HEX \
        --sortie DOSSIER_NEUF

Version 2 (corrections de la contre-lecture `contre-lecture-code-etage-1-ligne-3-v1.md`, 3aed6849…) : correction C2
seule dans le calcul — la taille d'étalonnage de la branche (2) suit la lettre du texte (« la plus petite taille
d'étalonnage à partir de laquelle la branche tient dans toutes les cellules » : elle tient à cette taille et à toutes
les tailles plus grandes de la grille) ; noms des fichiers de sortie en v2. Aucun autre changement de calcul ; aucun
tirage ne change.

Développeur, modèle L′.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import math
import platform
import statistics
import subprocess
import sys
from pathlib import Path

import numpy as np

VERSION = "banc-juges-scriptes-ligne-3-v2"
EMPREINTE_TEXTE_QUI_FAIT_FOI = "4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0"

# ---------------------------------------------------------------------------------------------------------------
# Graines (règle R9)
# ---------------------------------------------------------------------------------------------------------------
RACINE_ESSAIS = 2026111930
RACINE_CHRONOMETRAGE = 2026111931
RACINE_ETAGE_1_DECISIF = 2026111932
RACINE_REECHANTILLONNAGE_ETAGE_1 = 2026111933
RACINES_ETAGE_2 = (2026111934, 2026111935, 2026111936, 2026111937)
RACINES_SOUS_AUTORISATION = (RACINE_CHRONOMETRAGE, RACINE_ETAGE_1_DECISIF, RACINE_REECHANTILLONNAGE_ETAGE_1)

# Table « tâche → entier », gelée ; recopiée au manifeste.
TABLE_CLES = {
    "estimateur_et_agregation": 1,
    "monde_de_puissance": 2,
    "ecart_rho_prime_moins_rho": 3,
    "double_rendu": 4,
    "garde_de_cadrage": 5,
    "alarme": 6,
    "reechantillonnage_estimateur_et_agregation": 11,
    "reechantillonnage_monde_de_puissance": 12,
    "reechantillonnage_ecart_rho_prime_moins_rho": 13,
    "reechantillonnage_double_rendu": 14,
    "essais_formules": 21,
    "essais_gardes": 22,
}

# Mode → (racine des tirages du monde, racine du rééchantillonnage).
MODES = {
    "essais": (RACINE_ESSAIS, RACINE_ESSAIS),
    "chronometrage": (RACINE_CHRONOMETRAGE, RACINE_CHRONOMETRAGE),
    "decisif": (RACINE_ETAGE_1_DECISIF, RACINE_REECHANTILLONNAGE_ETAGE_1),
}

# Journal de toutes les dérivations faites dans le processus (contrôlé par l'essai final).
JOURNAL_GRAINES: list[dict] = []


class RefusGraine(Exception):
    """Racine refusée : aucune graine n'est dérivée."""


class BancInvalide(Exception):
    """Faute du banc : à corriger avant tout tirage ou toute lecture."""


class RegleInconnue(Exception):
    """À deux juges, poids et seuil qui ne rendent aucune des cinq règles du § 0 : arrêt du programme."""


class RefusExecution(Exception):
    """Exécution refusée (dossier de sortie déjà présent, configuration invalide)."""


def sha256_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def sha256_json(objet) -> str:
    texte = json.dumps(objet, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


class Autorisation:
    """Autorisation d'une racine décisive : l'additif de code scellé, par son chemin et son empreinte attendue."""

    def __init__(self, chemin_additif, empreinte_additif):
        self.chemin_additif = str(chemin_additif)
        self.empreinte_additif = empreinte_additif

    def decrire(self) -> dict:
        return {"chemin_additif": self.chemin_additif, "empreinte_additif": self.empreinte_additif}


def verifier_autorisation(autorisation, racine) -> None:
    if autorisation is None:
        raise RefusGraine(f"racine {racine} : refus sans autorisation (additif de code scellé)")
    if not isinstance(autorisation, Autorisation):
        raise RefusGraine(f"racine {racine} : autorisation d'un type inattendu")
    emp = autorisation.empreinte_additif
    if not (isinstance(emp, str) and len(emp) == 64 and all(c in "0123456789abcdef" for c in emp)):
        raise RefusGraine(f"racine {racine} : empreinte de l'additif mal formée")
    chemin = Path(autorisation.chemin_additif)
    if not chemin.is_file():
        raise RefusGraine(f"racine {racine} : additif absent")
    if sha256_fichier(chemin) != emp:
        raise RefusGraine(f"racine {racine} : empreinte de l'additif différente de l'attendue")


def generateurs(racine, tache, nombre, autorisation=None):
    """Rend `nombre` générateurs, enfants de SeedSequence(racine, spawn_key=(clé,)) ; refus avant toute dérivation."""
    if isinstance(racine, bool) or not isinstance(racine, int):
        raise RefusGraine("racine non entière")
    if racine in RACINES_ETAGE_2:
        raise RefusGraine(f"racine {racine} : racine de l'étage 2, jamais dérivée par le code de l'étage 1")
    if racine != RACINE_ESSAIS and racine not in RACINES_SOUS_AUTORISATION:
        raise RefusGraine(f"racine {racine} : hors du texte")
    if racine in RACINES_SOUS_AUTORISATION:
        verifier_autorisation(autorisation, racine)
    if tache not in TABLE_CLES:
        raise RefusGraine(f"tâche {tache!r} absente de la table gelée")
    if isinstance(nombre, bool) or not isinstance(nombre, int) or nombre < 1:
        raise RefusGraine("nombre d'enfants invalide")
    cle = TABLE_CLES[tache]
    JOURNAL_GRAINES.append({"racine": racine, "tache": tache, "cle": cle, "enfants": nombre})
    parent = np.random.SeedSequence(racine, spawn_key=(cle,))
    return [np.random.default_rng(enfant) for enfant in parent.spawn(nombre)]


class Contexte:
    """Mode d'exécution et dérivations faites (pour le manifeste)."""

    def __init__(self, mode, autorisation=None):
        if mode not in MODES:
            raise RefusExecution(f"mode inconnu : {mode!r}")
        self.mode = mode
        self.racine_tirages, self.racine_reechantillonnage = MODES[mode]
        self.autorisation = autorisation
        self.derivations: list[dict] = []

    def _deriver(self, racine, tache, nombre):
        gens = generateurs(racine, tache, nombre, self.autorisation)
        self.derivations.append({"racine": racine, "tache": tache, "cle": TABLE_CLES[tache], "enfants": nombre})
        return gens

    def tirages(self, tache, nombre):
        return self._deriver(self.racine_tirages, tache, nombre)

    def reechantillonnage(self, tache, nombre):
        return self._deriver(self.racine_reechantillonnage, tache, nombre)


# ---------------------------------------------------------------------------------------------------------------
# Grille et profils
# ---------------------------------------------------------------------------------------------------------------
RHOS = (0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9)
RHO_MAX_LOI_3 = 0.75
N_GRILLE = (50, 100, 200, 400)
TAUX_EGAUX = (0.05, 0.10, 0.20, 0.30)
NOMS_PROFILS = ("egal_0.05", "egal_0.1", "egal_0.2", "egal_0.3", "severe", "indulgent", "inegal")
PROFIL_DE_LA_REGLE = "egal_0.2"
RHOS_PRIME_R = (0.0, 0.5, 0.9)
F_DIFFICILE = 0.25
SEUIL_VARIANCE_NULLE = 1e-12
EPS = 1e-12

# Tolérance de l'estimateur (section « Seuil »).
TOL_BIAIS = 0.05
TOL_EQM = 0.10
TOL_COUVERTURE = (0.90, 0.98)
TOL_PART_INDEFINI = 0.02


def profil(nom, J):
    """(taux d'erreur sur les bons = vrais rejetés, taux d'erreur sur les mauvais = faux acceptés), par juge."""
    if nom.startswith("egal_"):
        p = float(nom.split("_", 1)[1])
        if p not in TAUX_EGAUX:
            raise BancInvalide(f"taux hors grille : {nom}")
        return np.full(J, p), np.full(J, p)
    if nom == "severe":
        return np.full(J, 0.30), np.full(J, 0.10)
    if nom == "indulgent":
        return np.full(J, 0.10), np.full(J, 0.30)
    if nom == "inegal":
        if J == 2:
            p = np.array([0.10, 0.25])
        elif J == 5:
            p = np.array([0.10, 0.15, 0.20, 0.25, 0.30])
        else:
            raise BancInvalide("profil inégal défini pour J = 2 et J = 5 seulement")
        return p.copy(), p.copy()
    raise BancInvalide(f"profil inconnu : {nom}")


def classes(n_c):
    """Étiquettes : n_c bons (True) puis n_c mauvais (False)."""
    return np.r_[np.ones(n_c, dtype=bool), np.zeros(n_c, dtype=bool)]


def indices_moities(n_c):
    """Partage par moitié, stratifié par classe : étalonnage = ceil(n_c/2) bons et floor(n_c/2) mauvais."""
    kb = (n_c + 1) // 2
    km = n_c // 2
    cal = np.r_[np.arange(0, kb), np.arange(n_c, n_c + km)]
    lec = np.r_[np.arange(kb, n_c), np.arange(n_c + km, 2 * n_c)]
    return cal, lec


# ---------------------------------------------------------------------------------------------------------------
# Lois d'erreur plantées
# ---------------------------------------------------------------------------------------------------------------
BLOCS_LOI_4 = np.array([0, 0, 1, 1, 2])


def quantile_normal(p):
    return statistics.NormalDist().inv_cdf(float(p))


def taux_loi_3(p, rho):
    """Taux (difficile, autre) de la loi 3 ; BancInvalide si un taux sort de [0 ; 1]."""
    p = np.asarray(p, dtype=float)
    a = np.sqrt(rho * p * (1 - p) / (F_DIFFICILE * (1 - F_DIFFICILE)))
    haut = p + 0.75 * a
    bas = p - 0.25 * a
    if np.any(bas < -EPS) or np.any(haut > 1 + EPS):
        raise BancInvalide("loi 3 : taux hors de [0 ; 1] (cellule infaisable)")
    return np.clip(haut, 0.0, 1.0), np.clip(bas, 0.0, 1.0)


def tirer_classe(loi, rng, R, m, p, param):
    """Erreurs (R, m, J) d'une classe, taux p (J,), sous la loi donnée."""
    p = np.asarray(p, dtype=float)
    J = p.size
    if loi == 1:
        commun = rng.random((R, m, 1))
        propre = rng.random((R, m, J))
        choc = rng.random((R, m, 1)) < param
        lu = np.where(choc, commun, propre)
        return lu < p
    if loi == 2:
        if not (0.0 <= param < 1.0):
            raise BancInvalide("loi 2 : r doit être dans [0 ; 1[")
        seuils = np.array([quantile_normal(x) for x in p])
        z = rng.standard_normal((R, m, 1))
        e = rng.standard_normal((R, m, J))
        x = math.sqrt(param) * z + math.sqrt(1.0 - param) * e
        return x < seuils
    if loi == 3:
        haut, bas = taux_loi_3(p, param)
        difficile = rng.random((R, m, 1)) < F_DIFFICILE
        taux = np.where(difficile, haut, bas)
        return rng.random((R, m, J)) < taux
    if loi == 4:
        if J != 5:
            raise BancInvalide("loi 4 : cinq juges")
        q_tous = param / 3.0
        q_bloc = (param - param / 3.0) / (1.0 - param / 3.0)
        u_college = rng.random((R, m, 1))
        u_bloc = rng.random((R, m, 3))
        propre = rng.random((R, m, J))
        tous = rng.random((R, m, 1)) < q_tous
        bloc_commun = rng.random((R, m, 3)) < q_bloc
        lu_bloc = np.where(bloc_commun[..., BLOCS_LOI_4], u_bloc[..., BLOCS_LOI_4], propre)
        lu = np.where(tous, u_college, lu_bloc)
        return lu < p
    raise BancInvalide(f"loi inconnue : {loi}")


def tirer_erreurs(loi, rng, R, n_c, p_bons, p_mauvais, param):
    """Erreurs (R, 2 n_c, J) : n_c bons puis n_c mauvais."""
    eb = tirer_classe(loi, rng, R, n_c, p_bons, param)
    em = tirer_classe(loi, rng, R, n_c, p_mauvais, param)
    return np.concatenate([eb, em], axis=1)


def votes_depuis_erreurs(E, y):
    """Vote « notable » : un bon sans erreur, ou un mauvais avec erreur."""
    return E != y[None, :, None]


# ---------------------------------------------------------------------------------------------------------------
# Valeur plantée (formule poolée sur les covariances et variances vraies, classe par classe)
# ---------------------------------------------------------------------------------------------------------------
_NOEUDS_GH = None


def noeuds_gauss_hermite():
    """Quadrature de Gauss-Hermite à 200 points, ramenée à la loi normale centrée réduite."""
    global _NOEUDS_GH
    if _NOEUDS_GH is None:
        x, w = np.polynomial.hermite.hermgauss(200)
        _NOEUDS_GH = (math.sqrt(2.0) * x, w / math.sqrt(math.pi))
    return _NOEUDS_GH


def phi_normale(t):
    return 0.5 * (1.0 + math.erf(t / math.sqrt(2.0)))


def cov_vraie_classe(loi, p, param):
    """Covariance vraie (J, J) des erreurs dans une classe."""
    p = np.asarray(p, dtype=float)
    J = p.size
    C = np.zeros((J, J))
    for j in range(J):
        C[j, j] = p[j] * (1 - p[j])
    if loi == 1:
        for j in range(J):
            for k in range(J):
                if j != k:
                    C[j, k] = param * (min(p[j], p[k]) - p[j] * p[k])
        return C
    if loi == 2:
        if not (0.0 <= param < 1.0):
            raise BancInvalide("loi 2 : r doit être dans [0 ; 1[")
        if param == 0.0:
            return C
        z, w = noeuds_gauss_hermite()
        a = [quantile_normal(x) for x in p]
        s, c = math.sqrt(param), math.sqrt(1.0 - param)
        phis = np.array([[phi_normale((a[j] - s * zi) / c) for zi in z] for j in range(J)])
        for j in range(J):
            for k in range(J):
                if j != k:
                    C[j, k] = float(np.sum(w * phis[j] * phis[k])) - p[j] * p[k]
        return C
    if loi == 3:
        for j in range(J):
            for k in range(J):
                if j != k:
                    C[j, k] = param * math.sqrt(p[j] * (1 - p[j]) * p[k] * (1 - p[k]))
        return C
    if loi == 4:
        if J != 5:
            raise BancInvalide("loi 4 : cinq juges")
        for j in range(J):
            for k in range(J):
                if j != k:
                    meme = param if BLOCS_LOI_4[j] == BLOCS_LOI_4[k] else param / 3.0
                    C[j, k] = meme * (min(p[j], p[k]) - p[j] * p[k])
        return C
    raise BancInvalide(f"loi inconnue : {loi}")


def valeur_plantee(loi, p_bons, p_mauvais, param):
    """(ρ moyenne plantée, matrice des ρ plantées par paire), formule poolée sur les deux classes."""
    C = cov_vraie_classe(loi, p_bons, param) + cov_vraie_classe(loi, p_mauvais, param)
    J = C.shape[0]
    d = np.diag(C)
    tr = float(d.sum())
    rho_moy = (float(C.sum()) - tr) / ((J - 1) * tr)
    paires = C / np.sqrt(np.outer(d, d))
    return rho_moy, paires


# ---------------------------------------------------------------------------------------------------------------
# Estimateur (corrélation stratifiée par classe, votes effectifs)
# ---------------------------------------------------------------------------------------------------------------
def cov_intra_classes(X, y):
    """Covariance (..., J, J) centrée à l'intérieur de chaque classe, divisée par n − 2."""
    X = np.asarray(X, dtype=float)
    n = X.shape[-2]
    total = 0.0
    for masque in (y, ~y):
        Xc = X[..., masque, :]
        Xc = Xc - Xc.mean(axis=-2, keepdims=True)
        total = total + np.einsum("...ij,...ik->...jk", Xc, Xc)
    return total / (n - 2)


def rho_moyenne(S):
    """(ρ moyenne, indéfini) ; indéfini si un juge n'a aucune variance dans les deux classes (jamais 0)."""
    S = np.asarray(S, dtype=float)
    J = S.shape[-1]
    diag = np.diagonal(S, axis1=-2, axis2=-1)
    tr = diag.sum(axis=-1)
    tot = S.sum(axis=(-2, -1))
    indefini = np.any(diag <= SEUIL_VARIANCE_NULLE, axis=-1)
    rho = (tot - tr) / ((J - 1) * np.where(indefini, 1.0, tr))
    rho = np.where(indefini, np.nan, rho)
    return rho, indefini


def rho_paire(S, j, k):
    """(ρ(j, k), indéfini)."""
    S = np.asarray(S, dtype=float)
    vj = S[..., j, j]
    vk = S[..., k, k]
    indefini = (vj <= SEUIL_VARIANCE_NULLE) | (vk <= SEUIL_VARIANCE_NULLE)
    den = np.sqrt(np.where(indefini, 1.0, vj * vk))
    rho = np.where(indefini, np.nan, S[..., j, k] / den)
    return rho, indefini


def votes_effectifs(rho, J):
    """Brut : J / (1 + (J − 1) ρ) ; indéfini (nan) si ρ est indéfinie ou si le dénominateur est nul."""
    rho = np.asarray(rho, dtype=float)
    den = 1.0 + (J - 1) * rho
    ok = np.isfinite(den) & (den > 0)
    return np.where(ok, J / np.where(ok, den, 1.0), np.nan)


def tronquer_votes(v, J):
    return np.clip(v, 1.0, float(J))


# ---------------------------------------------------------------------------------------------------------------
# Rééchantillonnage par les comptes de configurations, stratifié par classe
# ---------------------------------------------------------------------------------------------------------------
TAILLE_PAQUET = 50


def motifs(A):
    """Les 2^A configurations de A bits, en lignes (K, A), bit a = (k >> a) & 1."""
    K = 1 << A
    return ((np.arange(K)[:, None] >> np.arange(A)[None, :]) & 1).astype(float)


def comptes_configurations(B):
    """B (R, m, A) booléens → comptes (R, 2^A) des configurations."""
    B = np.asarray(B, dtype=bool)
    R, m, A = B.shape
    K = 1 << A
    codes = B.astype(np.int64) @ (np.int64(1) << np.arange(A, dtype=np.int64))
    codes = codes + K * np.arange(R, dtype=np.int64)[:, None]
    return np.bincount(codes.ravel(), minlength=R * K).reshape(R, K)


def tirer_comptes(rng, comptes, B):
    """Tirages avec remise, à taille de classe fixée : (B, r, K)."""
    comptes = np.asarray(comptes)
    n = comptes.sum(axis=-1)
    if np.any(n != n[0]):
        raise BancInvalide("tailles de classe différentes entre répliques")
    p = comptes / n[:, None]
    return rng.multinomial(int(n[0]), p, size=(B, comptes.shape[0]))


def cov_depuis_comptes(cb, cm, X):
    """Covariance intra-classes depuis les comptes (…, K) de chaque classe ; X (K, A)."""
    K, A = X.shape
    XX = (X[:, :, None] * X[:, None, :]).reshape(K, A * A)
    total = 0.0
    n = 0.0
    for c in (cb, cm):
        c = np.asarray(c, dtype=float)
        m = c.sum(axis=-1)
        s1 = c @ X
        s2 = (c @ XX).reshape(c.shape[:-1] + (A, A))
        total = total + s2 - s1[..., :, None] * s1[..., None, :] / m[..., None, None]
        n = n + m
    return total / (n - 2)[..., None, None]


def _centiles(valeurs, axe=0):
    with np.errstate(all="ignore"):
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            lo = np.nanpercentile(valeurs, 2.5, axis=axe)
            hi = np.nanpercentile(valeurs, 97.5, axis=axe)
    return lo, hi


def intervalles_rho_moyenne(E, y, rng, B):
    """Intervalle à 95 % (centiles) de ρ moyenne, par réplique ; tirages indéfinis écartés et comptés."""
    R, n, J = E.shape
    X = motifs(J)
    cb = comptes_configurations(E[:, y])
    cm = comptes_configurations(E[:, ~y])
    lo = np.full(R, np.nan)
    hi = np.full(R, np.nan)
    n_indef = np.zeros(R, dtype=np.int64)
    for debut in range(0, R, TAILLE_PAQUET):
        fin = min(R, debut + TAILLE_PAQUET)
        db = tirer_comptes(rng, cb[debut:fin], B)
        dm = tirer_comptes(rng, cm[debut:fin], B)
        rho, indef = rho_moyenne(cov_depuis_comptes(db, dm, X))
        lo[debut:fin], hi[debut:fin] = _centiles(rho, 0)
        n_indef[debut:fin] = indef.sum(axis=0)
    return lo, hi, n_indef


def intervalle_moyenne_repliques(valeurs, rng, B):
    """Intervalle à 95 % de la moyenne, par rééchantillonnage des répliques (valeurs non finies écartées)."""
    v = np.asarray(valeurs, dtype=float)
    v = v[np.isfinite(v)]
    if v.size == 0:
        return None, None, None
    idx = rng.integers(0, v.size, size=(B, v.size))
    moyennes = v[idx].mean(axis=1)
    lo, hi = np.percentile(moyennes, [2.5, 97.5])
    return float(v.mean()), float(lo), float(hi)


# ---------------------------------------------------------------------------------------------------------------
# Qualité d'une agrégation, règles et bras
# ---------------------------------------------------------------------------------------------------------------
def taux_erreurs(notable, y):
    """(faux acceptés, vrais rejetés, erreur équilibrée) sur l'axe des témoins."""
    notable = np.asarray(notable, dtype=bool)
    vr = (~notable[..., y]).mean(axis=-1)
    fa = notable[..., ~y].mean(axis=-1)
    return fa, vr, (fa + vr) / 2.0


def score(V_pm, w):
    return np.einsum("rnj,rj->rn", V_pm, w)


def tolerance_egalite(w, seuil):
    return 1e-9 * (1.0 + np.abs(seuil) + np.abs(w).sum(axis=-1))


def seuil_milieu(scores_cal, y_cal):
    return (scores_cal[:, y_cal].mean(axis=1) + scores_cal[:, ~y_cal].mean(axis=1)) / 2.0


def appliquer_seuil(scores, seuil, w):
    """Notable si le score dépasse le seuil ; un score au seuil (à la tolérance près) rend « non notable »."""
    return (scores - seuil[:, None]) > tolerance_egalite(w, seuil)[:, None]


def poids_covariance(V_pm_cal, y_cal):
    """Bras C : w = (S + λ I)⁻¹ d, ramenés à [0,2 ; 5] fois leur moyenne ; repli « poids égaux » compté."""
    V = np.asarray(V_pm_cal, dtype=float)
    R, _, J = V.shape
    S = cov_intra_classes(V, y_cal)
    d = V[:, y_cal].mean(axis=1) - V[:, ~y_cal].mean(axis=1)
    tr = np.trace(S, axis1=-2, axis2=-1)
    lam = 0.1 * tr / J
    repli = ~(tr > SEUIL_VARIANCE_NULLE)
    w = np.ones((R, J))
    ok = ~repli
    if ok.any():
        A = S[ok] + lam[ok][:, None, None] * np.eye(J)[None]
        w[ok] = np.linalg.solve(A, d[ok][..., None])[..., 0]
    moyenne = w.mean(axis=1)
    repli = repli | ~np.all(np.isfinite(w), axis=1) | ~(moyenne > 0)
    moyenne_sure = np.where(repli, 1.0, moyenne)
    borne = np.clip(w, (0.2 * moyenne_sure)[:, None], (5.0 * moyenne_sure)[:, None])
    w = np.where(repli[:, None], 1.0, borne)
    return w, repli


def poids_precision(V_cal, y_cal, E_cal):
    """Bras P : exactitude équilibrée − 0,5, plancher 0,05 ; paire à ρ d'erreurs estimée > 0,5 : poids divisés par 2."""
    V = np.asarray(V_cal, dtype=bool)
    R, _, J = V.shape
    fa = V[:, ~y_cal, :].mean(axis=1)
    vr = (~V[:, y_cal, :]).mean(axis=1)
    exactitude = 1.0 - (fa + vr) / 2.0
    w = np.maximum(exactitude - 0.5, 0.05)
    S = cov_intra_classes(np.asarray(E_cal, dtype=float), y_cal)
    for j in range(J):
        for k in range(j + 1, J):
            r, indef = rho_paire(S, j, k)
            masque = (~indef) & (np.nan_to_num(r, nan=-np.inf) > 0.5)
            w[masque, j] = w[masque, j] / 2.0
            w[masque, k] = w[masque, k] / 2.0
    return w


def q_porteuse(v_tronques):
    """q = 3 + arrondi au demi supérieur de x = 2 (5 − v) / 4, soit plancher(x + 0,5) ; −1 si v est indéfini."""
    v = np.asarray(v_tronques, dtype=float)
    x = 2.0 * (5.0 - v) / 4.0
    q = 3 + np.floor(x + 0.5)
    return np.where(np.isfinite(q), q, -1).astype(int)


CONFIGURATIONS_DEUX_JUGES = np.array([[-1.0, -1.0], [-1.0, 1.0], [1.0, -1.0], [1.0, 1.0]])
REGLES_DEUX_JUGES = {
    (False, False, False, True): "unanimite",
    (False, True, True, True): "au_moins_un",
    (False, False, True, True): "juge_1_seul",
    (False, True, False, True): "juge_2_seul",
    (False, False, False, False): "constante",
    (True, True, True, True): "constante",
}


def regle_choisie(w, seuil):
    """Nom de la règle que rendent un vecteur de deux poids et un seuil ; RegleInconnue sinon (arrêt)."""
    w = np.asarray(w, dtype=float).reshape(1, 2)
    s = np.asarray([seuil], dtype=float)
    sc = CONFIGURATIONS_DEUX_JUGES @ w[0]
    sortie = tuple(bool(x) for x in ((sc - s[0]) > tolerance_egalite(w, s)[0]))
    if sortie not in REGLES_DEUX_JUGES:
        raise RegleInconnue(f"règle hors des cinq du § 0 : sorties {sortie}")
    return REGLES_DEUX_JUGES[sortie]


def repetitions(rng, erreurs_premier, p_par_temoin, rho_prime, k):
    """Bras R : k rendus d'un même juge, le premier donné ; loi 1 entre rendus (copie du premier avec prob. ρ′)."""
    R, n = erreurs_premier.shape
    copie = rng.random((R, n, 1)) < rho_prime
    propres = rng.random((R, n, k - 1)) < p_par_temoin[None, :, None]
    suivants = np.where(copie, erreurs_premier[:, :, None], propres)
    return np.concatenate([erreurs_premier[:, :, None], suivants], axis=2)


def ecart_p2(ee_moyennes):
    """Plus grand écart d'erreur équilibrée moyenne entre les quatre règles de P2."""
    valeurs = [ee_moyennes[k] for k in ("S_1", "S_2", "U", "F_au_moins_un")]
    return float(max(valeurs) - min(valeurs))


def garde_p2(ecart):
    """Théorie P2 : écart hors de ± 0,02 → banc invalide."""
    return "invalide" if ecart > 0.02 else "valide"


def mot_fa38(fa_p, vr_p, references):
    """Critère de `fa38f9faa24e0` (bras P), par cellule ; references = liste de (faux acceptés, vrais rejetés)."""
    for fa_r, vr_r in references:
        if fa_r < 0.02 or vr_p > vr_r + 0.05:
            return "sans prise"
    if all(fa_p <= 0.85 * fa_r for fa_r, _ in references):
        return "tient sur le banc"
    return "réfuté sur le banc"


# ---------------------------------------------------------------------------------------------------------------
# Cellule « estimateur et agrégation »
# ---------------------------------------------------------------------------------------------------------------
def qualite_estimateur(rho_hat, indef, lo, hi, plantee):
    part_indef = float(np.mean(indef))
    defini = ~indef
    if not defini.any():
        return {"biais": None, "eqm": None, "couverture": None, "part_indefini": part_indef, "tient": False,
                "audit_trop_propre_aucune_replique_hors_intervalle": None}
    e = rho_hat[defini] - plantee
    biais = float(e.mean())
    eqm = float(np.sqrt(np.mean(e ** 2)))
    with np.errstate(invalid="ignore"):
        couvre = (lo <= plantee) & (plantee <= hi)
    couverture = float(couvre[defini].mean())
    tient = (abs(biais) <= TOL_BIAIS and eqm <= TOL_EQM and TOL_COUVERTURE[0] <= couverture <= TOL_COUVERTURE[1]
             and part_indef <= TOL_PART_INDEFINI)
    return {"biais": biais, "eqm": eqm, "couverture": couverture, "part_indefini": part_indef, "tient": bool(tient),
            "audit_trop_propre_aucune_replique_hors_intervalle": bool(couverture == 1.0)}


def _f(x):
    if x is None:
        return None
    x = float(x)
    return x if math.isfinite(x) else None


def _nanmoyenne(v):
    v = np.asarray(v, dtype=float)
    v = v[np.isfinite(v)]
    return float(v.mean()) if v.size else None


def cellule_estimateur_agregation(rng_t, rng_r, loi, J, nom_profil, rho, n, R, B):
    n_c = n // 2
    y = classes(n_c)
    p_b, p_m = profil(nom_profil, J)
    E = tirer_erreurs(loi, rng_t, R, n_c, p_b, p_m, rho)
    plantee, plantee_paires = valeur_plantee(loi, p_b, p_m, rho)

    # Estimateur sur la banque entière.
    S = cov_intra_classes(E, y)
    rho_hat, indef = rho_moyenne(S)
    lo, hi, n_tirages_indef = intervalles_rho_moyenne(E, y, rng_r, B)
    qualite = qualite_estimateur(rho_hat, indef, lo, hi, plantee)
    v_brut = votes_effectifs(rho_hat, J)

    # Moitiés : stabilité.
    cal, lec = indices_moities(n_c)
    y_cal, y_lec = y[cal], y[lec]
    r_cal, i_cal = rho_moyenne(cov_intra_classes(E[:, cal], y_cal))
    r_lec, i_lec = rho_moyenne(cov_intra_classes(E[:, lec], y_lec))
    ok = (~i_cal) & (~i_lec)
    ecarts_moities = np.abs(r_cal - r_lec)[ok]
    centile_95_ecart = float(np.percentile(ecarts_moities, 95)) if ecarts_moities.size else None

    # Bras d'agrégation (lus sur la moitié « lecture »).
    V = votes_depuis_erreurs(E, y)
    Vc, Vl = V[:, cal], V[:, lec]
    Vc_pm, Vl_pm = 2.0 * Vc - 1.0, 2.0 * Vl - 1.0
    bras = {}
    for j in range(J):
        bras[f"S_{j + 1}"] = Vl[..., j]
    bras["U"] = Vl.all(axis=-1)
    bras["F_au_moins_un"] = Vl.any(axis=-1)
    if J == 5:
        bras["F_majorite_stricte"] = Vl.sum(axis=-1) > J / 2.0
    w_eg = np.ones((R, J))
    s_eg = seuil_milieu(score(Vc_pm, w_eg), y_cal)
    bras["poids_egaux"] = appliquer_seuil(score(Vl_pm, w_eg), s_eg, w_eg)
    w_c, repli_c = poids_covariance(Vc_pm, y_cal)
    s_c = seuil_milieu(score(Vc_pm, w_c), y_cal)
    bras["C"] = appliquer_seuil(score(Vl_pm, w_c), s_c, w_c)
    w_p = poids_precision(Vc, y_cal, E[:, cal])
    s_p = seuil_milieu(score(Vc_pm, w_p), y_cal)
    bras["P"] = appliquer_seuil(score(Vl_pm, w_p), s_p, w_p)
    n_indef_porteuse = 0
    masque_porteuse = None
    if J == 5:
        v_cal = tronquer_votes(votes_effectifs(r_cal, J), J)
        q = q_porteuse(v_cal)
        masque_porteuse = q < 0
        n_indef_porteuse = int(masque_porteuse.sum())
        bras["N"] = Vl.sum(axis=-1) >= q[:, None]
    p_juge_1 = np.where(y, p_b[0], p_m[0])
    k_max = 3 if J == 2 else 5
    for rp in RHOS_PRIME_R:
        Er = repetitions(rng_t, E[..., 0], p_juge_1, rp, k_max)
        Vr = votes_depuis_erreurs(Er, y)[:, lec]
        if J == 2:
            bras[f"R_k2_rp{rp}"] = Vr[..., :2].all(axis=-1)
            bras[f"R_k3_rp{rp}"] = Vr[..., :3].sum(axis=-1) >= 2
        else:
            bras[f"R_k5_rp{rp}"] = Vr.sum(axis=-1) >= 3

    taux = {}
    for nom, notable in bras.items():
        fa, vr, ee = taux_erreurs(notable, y_lec)
        if nom == "N":
            fa, vr, ee = (np.where(masque_porteuse, np.nan, t) for t in (fa, vr, ee))
        taux[nom] = (fa, vr, ee)
    moyennes = {nom: {"faux_acceptes": _nanmoyenne(t[0]), "vrais_rejetes": _nanmoyenne(t[1]),
                      "erreur_equilibree": _nanmoyenne(t[2])} for nom, t in taux.items()}

    sortie = {
        "loi": loi, "J": J, "profil": nom_profil, "rho_grille": rho, "n": n, "repliques": R,
        "valeur_plantee_rho_moyenne": plantee,
        "valeur_plantee_par_paire": plantee_paires.tolist(),
        "estimateur": qualite,
        "estimation_moyenne_rho_moyenne": _nanmoyenne(rho_hat),
        "tirages_indefinis_du_reechantillonnage_total": int(n_tirages_indef.sum()),
        "votes_effectifs_bruts_moyenne": _nanmoyenne(v_brut),
        "votes_effectifs_tronques_moyenne": _nanmoyenne(tronquer_votes(v_brut, J)),
        "stabilite_centile_95_ecart_moities": centile_95_ecart,
        "stabilite_repliques_definies": int(ok.sum()),
        "bras": moyennes,
        "bras_C_repli_poids_egaux": int(repli_c.sum()),
        "bras_N_votes_effectifs_indefinis": n_indef_porteuse,
    }
    if J == 2:
        regles_c, regles_p = {}, {}
        for r in range(R):
            nc = regle_choisie(w_c[r], s_c[r])
            npp = regle_choisie(w_p[r], s_p[r])
            regles_c[nc] = regles_c.get(nc, 0) + 1
            regles_p[npp] = regles_p.get(npp, 0) + 1
        sortie["bras_C_regle_choisie"] = regles_c
        sortie["bras_P_regle_choisie"] = regles_p
        sortie["bras_N"] = "sans prise (à deux juges, la règle se confond avec U), non lue"
        if nom_profil.startswith("egal_"):
            ecart = ecart_p2({k: moyennes[k]["erreur_equilibree"] for k in ("S_1", "S_2", "U", "F_au_moins_un")})
            sortie["theorie_p2"] = {"ecart_maximal": ecart, "garde": garde_p2(ecart)}

    # Critère de fa38f9faa24e0 (bras P), par ρ′ du bras R (k = J).
    mots = {}
    for rp in RHOS_PRIME_R:
        ref_r = moyennes[f"R_k{J}_rp{rp}"]
        refs = [(moyennes["poids_egaux"]["faux_acceptes"], moyennes["poids_egaux"]["vrais_rejetes"]),
                (ref_r["faux_acceptes"], ref_r["vrais_rejetes"])]
        mots[str(rp)] = mot_fa38(moyennes["P"]["faux_acceptes"], moyennes["P"]["vrais_rejetes"], refs)
    sortie["mot_fa38f9faa24e0_par_rho_prime"] = mots

    # Comparaisons descriptives (écart = EE du premier − EE du second), intervalle sur les répliques.
    comparaisons = [(f"{x}_moins_C", x, "C") for x in bras if x != "C"]
    comparaisons.append(("poids_egaux_moins_P", "poids_egaux", "P"))
    if J == 5:
        comparaisons.append(("F_majorite_stricte_moins_N", "F_majorite_stricte", "N"))
    for rp in RHOS_PRIME_R:
        comparaisons.append((f"U_moins_R_k{J}_rp{rp}", "U", f"R_k{J}_rp{rp}"))
    idx = rng_r.integers(0, R, size=(B, R))
    table = {}
    for nom, a, b in comparaisons:
        diff = taux[a][2] - taux[b][2]
        defini = np.isfinite(diff)
        if not defini.any():
            table[nom] = {"moyenne": None, "bas": None, "haut": None}
            continue
        d0 = np.where(defini, diff, 0.0)
        cnt = defini[idx].sum(axis=1)
        moy_boot = d0[idx].sum(axis=1) / np.maximum(cnt, 1)
        bas, haut = np.percentile(moy_boot, [2.5, 97.5])
        table[nom] = {"moyenne": float(diff[defini].mean()), "bas": float(bas), "haut": float(haut)}
    sortie["comparaisons"] = table
    return sortie


# ---------------------------------------------------------------------------------------------------------------
# Monde de puissance (règle gelée de portée)
# ---------------------------------------------------------------------------------------------------------------
TAUX_MOYEN_PUISSANCE = 0.20
D_MAX = 0.20
ECARTS_PUISSANCE = (0.05, 0.10, 0.15)
COMPARAISONS_PUISSANCE = ("unanimite", "juge_seul", "juge_repete_trois_votes_majorite")
NIVEAU_HOLM = 0.05
MARGE_COMPARAISON = 0.05
PUISSANCE_EXIGEE = 0.5


def conjointe(p, rho):
    return p * p + rho * p * (1 - p)


def majorite_de_trois(p, rho_prime):
    return rho_prime * p + (1 - rho_prime) * (3 * p * p - 2 * p ** 3)


def erreurs_equilibrees_formules(d, rho, rho_prime):
    a, b = TAUX_MOYEN_PUISSANCE + d, TAUX_MOYEN_PUISSANCE - d
    a11, b11 = conjointe(a, rho), conjointe(b, rho)
    return {"au_moins_un": (a11 + 2 * b - b11) / 2,
            "unanimite": (2 * a - a11 + b11) / 2,
            "juge_seul": (a + b) / 2,
            "juge_repete_trois_votes_majorite": (majorite_de_trois(a, rho_prime) + majorite_de_trois(b, rho_prime)) / 2}


def loi_3_jouable(p, rho):
    x = (rho * p * (1 - p) / (F_DIFFICILE * (1 - F_DIFFICILE))) ** 0.5
    return p - 0.25 * x >= -EPS and p + 0.75 * x <= 1 + EPS


def resoudre_dissymetrie(comparaison, ecart, rho, rho_prime):
    """d tel que l'écart vrai (comparaison − « au moins un ») vaille `ecart` ; None si infaisable sur [0 ; D_MAX]."""
    def f(d):
        e = erreurs_equilibrees_formules(d, rho, rho_prime)
        return e[comparaison] - e["au_moins_un"] - ecart
    if f(D_MAX) < 0:
        return None
    bas, haut = 0.0, D_MAX
    if f(bas) >= 0:
        return 0.0
    for _ in range(80):
        milieu = (bas + haut) / 2
        if f(milieu) < 0:
            bas = milieu
        else:
            haut = milieu
    return haut


def holm(p, alpha):
    """Rejets de Holm (pas à pas descendant), sur le dernier axe."""
    p = np.asarray(p, dtype=float)
    m = p.shape[-1]
    ordre = np.argsort(p, axis=-1, kind="stable")
    tries = np.take_along_axis(p, ordre, axis=-1)
    seuils = alpha / (m - np.arange(m))
    rejet_trie = np.logical_and.accumulate(tries <= seuils, axis=-1)
    rejet = np.zeros_like(rejet_trie)
    np.put_along_axis(rejet, ordre, rejet_trie, axis=-1)
    return rejet


def p_valeur_unilaterale(diff, B):
    """(1 + nombre de tirages où l'écart, bras de comparaison moins agrégation étalonnée, est ≤ 0) / (B + 1), axe 0."""
    return (1.0 + (np.asarray(diff) <= EPS).sum(axis=0)) / (B + 1.0)


def ee_depuis_comptes(cb, cm, X, nb, nm):
    """Erreur équilibrée (…, A) de chaque bras depuis les comptes de configurations d'erreurs."""
    return 0.5 * ((np.asarray(cm, dtype=float) @ X) / nm + (np.asarray(cb, dtype=float) @ X) / nb)


def cellule_puissance(rng_t, rng_r, comparaison, ecart, loi, rho, rho_prime, R, B, n=100):
    """Test entier joué dans le monde planté pour une comparaison ; rend la puissance de chaque comparaison."""
    d = resoudre_dissymetrie(comparaison, ecart, rho, rho_prime)
    cellule = {"comparaison": comparaison, "ecart_vise": ecart, "loi": loi, "rho": rho, "rho_prime": rho_prime}
    if d is None:
        cellule.update({"faisable": False, "cause": "aucun d de [0 ; 0,20] n'atteint l'écart"})
        return cellule
    a, b = TAUX_MOYEN_PUISSANCE + d, TAUX_MOYEN_PUISSANCE - d
    if loi == 3 and not (loi_3_jouable(a, rho) and loi_3_jouable(b, rho)):
        cellule.update({"faisable": False, "d": d, "cause": "loi 3 : taux hors de [0 ; 1]"})
        return cellule
    n_c = n // 2
    y = classes(n_c)
    E = tirer_erreurs(loi, rng_t, R, n_c, np.array([a, a]), np.array([b, b]), rho)
    p_juge_2 = np.where(y, a, b)
    Er = repetitions(rng_t, E[..., 1], p_juge_2, rho_prime, 3)
    cal, lec = indices_moities(n_c)
    y_cal, y_lec = y[cal], y[lec]
    V = votes_depuis_erreurs(E, y)
    Vc_pm, Vl_pm = 2.0 * V[:, cal] - 1.0, 2.0 * V[:, lec] - 1.0
    w_c, repli_c = poids_covariance(Vc_pm, y_cal)
    s_c = seuil_milieu(score(Vc_pm, w_c), y_cal)
    notable = {
        "C": appliquer_seuil(score(Vl_pm, w_c), s_c, w_c),
        "U": V[:, lec].all(axis=-1),
        "S_1": V[:, lec, 0],
        "S_2": V[:, lec, 1],
        "R_3": votes_depuis_erreurs(Er, y)[:, lec].sum(axis=-1) >= 2,
    }
    noms = ("C", "U", "S_1", "S_2", "R_3")
    erreurs = np.stack([notable[k] != y_lec[None, :] for k in noms], axis=-1)
    nb, nm = int(y_lec.sum()), int((~y_lec).sum())
    X = motifs(len(noms))
    cb = comptes_configurations(erreurs[:, y_lec])
    cm = comptes_configurations(erreurs[:, ~y_lec])
    ee_obs = ee_depuis_comptes(cb, cm, X, nb, nm)
    ecarts_obs = ee_obs[:, 1:] - ee_obs[:, :1]
    pvals = np.zeros((R, 4))
    for debut in range(0, R, TAILLE_PAQUET):
        fin = min(R, debut + TAILLE_PAQUET)
        db = tirer_comptes(rng_r, cb[debut:fin], B)
        dm = tirer_comptes(rng_r, cm[debut:fin], B)
        ee = ee_depuis_comptes(db, dm, X, nb, nm)
        diff = ee[..., 1:] - ee[..., :1]
        pvals[debut:fin] = p_valeur_unilaterale(diff, B)
    rejet = holm(pvals, NIVEAU_HOLM)
    gagne = rejet & (ecarts_obs >= MARGE_COMPARAISON - EPS)
    puissances = {nom: float(gagne[:, i].mean()) for i, nom in enumerate(("U", "S_1", "S_2", "R_3"))}
    regles = {}
    for r in range(R):
        nr = regle_choisie(w_c[r], s_c[r])
        regles[nr] = regles.get(nr, 0) + 1
    vrai = erreurs_equilibrees_formules(d, rho, rho_prime)
    cellule.update({
        "faisable": True, "d": d, "vrais_rejetes_a": a, "faux_acceptes_b": b,
        "ecart_vrai_formule": vrai[comparaison] - vrai["au_moins_un"],
        "puissance_par_comparaison": puissances,
        "ecart_observe_moyen": {nom: float(ecarts_obs[:, i].mean()) for i, nom in enumerate(("U", "S_1", "S_2", "R_3"))},
        "bras_C_regle_choisie": regles, "bras_C_repli_poids_egaux": int(repli_c.sum()), "repliques": R,
    })
    return cellule


COMPARAISONS_DU_MONDE = {"unanimite": ("U",), "juge_seul": ("S_1", "S_2"), "juge_repete_trois_votes_majorite": ("R_3",)}


def enumerer_cellules_puissance(cfg):
    cellules = []
    for comparaison in COMPARAISONS_PUISSANCE:
        primes = cfg["rhos_prime"] if comparaison == "juge_repete_trois_votes_majorite" else (0.0,)
        for ecart in cfg["ecarts"]:
            for loi in cfg["lois"]:
                for rho in cfg["rhos"]:
                    for rp in primes:
                        cellules.append((comparaison, ecart, loi, rho, rp))
    return cellules


def puissance_qui_decide(cellules, ecart=0.10):
    """Plus basse puissance, sur les quatre comparaisons et leurs cellules faisables (lois 1 et 3), à l'écart 0,10."""
    par_comparaison = {"U": [], "S_1": [], "S_2": [], "R_3": []}
    for c in cellules:
        if not c.get("faisable") or abs(c["ecart_vise"] - ecart) > EPS or c["loi"] not in (1, 3):
            continue
        for nom in COMPARAISONS_DU_MONDE[c["comparaison"]]:
            par_comparaison[nom].append(c["puissance_par_comparaison"][nom])
    sans_cellule = [nom for nom, v in par_comparaison.items() if not v]
    minima = {nom: (min(v) if v else None) for nom, v in par_comparaison.items()}
    if sans_cellule:
        return {"puissance_qui_decide": None, "minima_par_comparaison": minima, "comparaisons_sans_cellule_faisable": sans_cellule,
                "comparaisons_d_agregations": "descriptives avant la dépense (une comparaison sans cellule faisable)"}
    p = min(minima.values())
    return {"puissance_qui_decide": p, "minima_par_comparaison": minima, "comparaisons_sans_cellule_faisable": [],
            "comparaisons_d_agregations": ("descriptives avant la dépense (puissance sous 0,5)" if p < PUISSANCE_EXIGEE
                                           else "peuvent porter un « oui »")}


# ---------------------------------------------------------------------------------------------------------------
# Puissance de la lecture « positif » de ρ′ − ρ
# ---------------------------------------------------------------------------------------------------------------
ECARTS_RHO_PRIME = (0.2, 0.3, 0.5)
JUGE_DE_LA_COLONNE = np.array([0, 1, 0, 1])  # colonnes : juge 1 rendu 1, juge 2 rendu 1, juge 1 rendu 2, juge 2 rendu 2


def tirer_quatre_rendus(rng, R, m, p, rho, rho_prime):
    """Loi 1 emboîtée : choc commun ρ aux quatre lectures ; sinon, par juge, choc propre au juge (ρ′ − ρ)/(1 − ρ)."""
    q = (rho_prime - rho) / (1.0 - rho)
    commun = rng.random((R, m, 1))
    juge = rng.random((R, m, 2))
    propre = rng.random((R, m, 4))
    tous = rng.random((R, m, 1)) < rho
    choc_juge = rng.random((R, m, 2)) < q
    lu_juge = np.where(choc_juge[..., JUGE_DE_LA_COLONNE], juge[..., JUGE_DE_LA_COLONNE], propre)
    lu = np.where(tous, commun, lu_juge)
    return lu < p


def cellule_ecart_rho_prime(rng_t, rng_r, ecart, rho, R, B, n=100, p=0.20):
    rho_prime = rho + ecart
    cellule = {"ecart_vise": ecart, "rho": rho, "rho_prime": rho_prime, "taux": p, "n": n}
    if rho_prime > 1.0 + EPS or rho >= 1.0:
        cellule.update({"faisable": False})
        return cellule
    rho_prime = min(rho_prime, 1.0)
    n_c = n // 2
    y = classes(n_c)
    E = np.concatenate([tirer_quatre_rendus(rng_t, R, n_c, p, rho, rho_prime),
                        tirer_quatre_rendus(rng_t, R, n_c, p, rho, rho_prime)], axis=1)
    X = motifs(4)
    cb = comptes_configurations(E[:, y])
    cm = comptes_configurations(E[:, ~y])
    positif = np.zeros((R, 2), dtype=bool)
    for debut in range(0, R, TAILLE_PAQUET):
        fin = min(R, debut + TAILLE_PAQUET)
        db = tirer_comptes(rng_r, cb[debut:fin], B)
        dm = tirer_comptes(rng_r, cm[debut:fin], B)
        S = cov_depuis_comptes(db, dm, X)
        r12, _ = rho_paire(S, 0, 1)
        for juge, (a, b) in enumerate(((0, 2), (1, 3))):
            rp, _ = rho_paire(S, a, b)
            lo, _ = _centiles(rp - r12, 0)
            positif[debut:fin, juge] = np.nan_to_num(lo, nan=-np.inf) > 0
    cellule.update({"faisable": True, "repliques": R,
                    "puissance_juge_1": float(positif[:, 0].mean()), "puissance_juge_2": float(positif[:, 1].mean()),
                    "puissance_les_deux": float(positif.all(axis=1).mean())})
    return cellule


# ---------------------------------------------------------------------------------------------------------------
# Double rendu (fcfa3d98b90f8) et garde de cadrage (branche (3) de fefca0bd94064)
# ---------------------------------------------------------------------------------------------------------------
P_FOND = 0.15
RHO_PRIME_FOND = 0.5
LOIS_LECTEUR = ("suiveur_seduisant", "suiveur_repoussant", "seduit_sinon_fond")
LOI_QUI_DECIDE = "suiveur_seduisant"
ABSTENTION_PLANTEE_PAR_VOTE = 2 * (P_FOND - (P_FOND * P_FOND + RHO_PRIME_FOND * P_FOND * (1 - P_FOND)))
SEUILS_CADRAGE = (0.10, 0.15, 0.20, 0.25, 0.30)
MARGE_VRAIS_REJETES = 0.05
SEUIL_REFERENCE_SANS_PRISE = 0.02
MARGE_SURFACE = 0.05


def tirer_monde_double_rendu(rng, R, n, s, delta, juges=4):
    """Témoins (n/2 vrais puis n/2 faux), traits (faux seulement, prob. s), statut de lecteur de surface (δ par juge
    et par réplique), votes du fond aux deux rendus (taux 0,15, ρ′ = 0,5 entre rendus, juges indépendants)."""
    n_c = n // 2
    y = classes(n_c)
    trait = np.zeros((R, n), dtype=bool)
    trait[:, n_c:] = rng.random((R, n_c)) < s
    surface = rng.random((R, juges)) < delta
    meme = rng.random((R, n, juges)) < RHO_PRIME_FOND
    u1 = rng.random((R, n, juges))
    u2_propre = rng.random((R, n, juges))
    u2 = np.where(meme, u1, u2_propre)
    fond1 = y[None, :, None] != (u1 < P_FOND)
    fond2 = y[None, :, None] != (u2 < P_FOND)
    return {"y": y, "trait": trait, "surface": surface, "fond1": fond1, "fond2": fond2}


def votes_double_rendu(monde, loi):
    """Votes « notable » aux deux rendus ; le second rendu retire le trait."""
    t = monde["trait"][:, :, None]
    f1, f2 = monde["fond1"], monde["fond2"]
    if loi == "suiveur_seduisant":
        s1, s2 = np.broadcast_to(t, f1.shape), np.zeros_like(f2)
    elif loi == "suiveur_repoussant":
        s1, s2 = np.broadcast_to(~t, f1.shape), np.ones_like(f2)
    elif loi == "seduit_sinon_fond":
        s1, s2 = t | f1, f2
    else:
        raise BancInvalide(f"loi du lecteur inconnue : {loi}")
    lecteur = monde["surface"][:, None, :]
    return np.where(lecteur, s1, f1), np.where(lecteur, s2, f2)


def bras_double_rendu(v1, v2, k=2):
    a, b = v1[..., :k], v2[..., :k]
    stable = a == b
    n_stable = stable.sum(axis=-1)
    stables_notables = np.all(~stable | a, axis=-1)
    return {"bras_1": (n_stable >= 1) & stables_notables,
            "bras_2": v1[..., :2 * k].all(axis=-1),
            "bras_4": a.all(axis=-1),
            "abstention": ~stable}


def _taux_groupe(notable, groupe):
    cnt = groupe.sum(axis=1)
    val = (notable & groupe).sum(axis=1) / np.maximum(cnt, 1)
    return np.where(cnt > 0, val, np.nan)


def mesures_double_rendu(monde, loi):
    y, trait = monde["y"], monde["trait"]
    v1, v2 = votes_double_rendu(monde, loi)
    b = bras_double_rendu(v1, v2)
    faux = ~y[None, :]
    faux_trait = faux & trait
    faux_nu = faux & ~trait
    vrai = np.broadcast_to(y[None, :], trait.shape)
    predicteur = ~trait  # prédicteur de surface : « non notable » si le trait est présent (choix déclaré)
    m = {}
    for k in ("bras_1", "bras_2", "bras_4"):
        m[f"fa_trait_{k}"] = _taux_groupe(b[k], faux_trait)
        m[f"fa_nu_{k}"] = _taux_groupe(b[k], faux_nu)
        m[f"vr_{k}"] = 1.0 - _taux_groupe(b[k], vrai)
    m["fa_trait_bras_3"] = _taux_groupe(predicteur, faux_trait)
    m["vr_bras_3"] = 1.0 - _taux_groupe(predicteur, vrai)
    m["abstention_par_vote"] = b["abstention"].mean(axis=(1, 2))
    m["abstention_par_temoin"] = b["abstention"].any(axis=-1).mean(axis=1)
    m["ecart_surface_bras_1"] = m["fa_trait_bras_1"] - m["fa_nu_bras_1"]
    m["ecart_surface_bras_4"] = m["fa_trait_bras_4"] - m["fa_nu_bras_4"]
    m["predicteur_exactitude_contre_la_classe"] = (predicteur == y[None, :]).mean(axis=1)
    m["predicteur_exactitude_contre_le_trait"] = ((~predicteur) == trait).mean(axis=1)
    m["predicteur_accord_avec_le_bras_1_information"] = (predicteur == b["bras_1"]).mean(axis=1)
    return m


def mot_clause_i(fa1_moy, fa1_moins_fa2_bas, fa2_moy, vr1, vr4, fa2_moins_fa1_bas):
    if (fa1_moy - fa2_moy > 0 and fa1_moins_fa2_bas > 0) or vr1 > vr4 + MARGE_VRAIS_REJETES:
        return "réfuté sur le banc"
    if fa2_moy < SEUIL_REFERENCE_SANS_PRISE:
        return "sans prise"
    if fa2_moins_fa1_bas > 0:
        return "tient sur le banc"
    return "réfuté sur le banc"


def mot_clause_iii(delta, e1_moy, e1_bas, e1_haut, e4_bas, e4_haut):
    if delta == 0 or (e4_bas >= -MARGE_SURFACE and e4_haut <= MARGE_SURFACE):
        return "sans prise"
    if abs(e1_moy) >= MARGE_SURFACE and (e1_bas > 0 or e1_haut < 0):
        return "réfuté sur le banc"
    if e1_bas >= -MARGE_SURFACE and e1_haut <= MARGE_SURFACE:
        return "tient sur le banc"
    return "sans prise"


def mot_carte_fcfa(s, mot_i, mot_iii):
    if s == 0:
        return "sans prise"
    if "réfuté sur le banc" in (mot_i, mot_iii):
        return "réfuté sur le banc"
    if mot_i == "tient sur le banc":
        return "tient sur le banc"
    return "sans prise"


def cellule_double_rendu(rng_t, rng_r, n, s, delta, R, B):
    monde = tirer_monde_double_rendu(rng_t, R, n, s, delta)
    sortie = {"n": n, "s": s, "delta": delta, "repliques": R, "par_loi": {}}
    for loi in LOIS_LECTEUR:
        m = mesures_double_rendu(monde, loi)
        moy = {k: _nanmoyenne(v) for k, v in m.items()}
        bloc = {"moyennes": moy, "repliques_indefinies": {k: int((~np.isfinite(v)).sum()) for k, v in m.items()}}
        if s > 0:
            d12 = m["fa_trait_bras_1"] - m["fa_trait_bras_2"]
            moy12, bas12, haut12 = intervalle_moyenne_repliques(d12, rng_r, B)
            bloc["fa_trait_bras_1_moins_bras_2"] = {"moyenne": moy12, "bas": bas12, "haut": haut12}
            mi = mot_clause_i(moy["fa_trait_bras_1"], bas12, moy["fa_trait_bras_2"], moy["vr_bras_1"], moy["vr_bras_4"],
                              -haut12)
        else:
            mi = "non lue (s = 0)"
        miii = "non lue (s ≠ 0,5)"
        if abs(s - 0.5) < EPS:
            e1 = intervalle_moyenne_repliques(m["ecart_surface_bras_1"], rng_r, B)
            e4 = intervalle_moyenne_repliques(m["ecart_surface_bras_4"], rng_r, B)
            bloc["ecart_surface_bras_1"] = {"moyenne": e1[0], "bas": e1[1], "haut": e1[2]}
            bloc["ecart_surface_bras_4"] = {"moyenne": e4[0], "bas": e4[1], "haut": e4[2]}
            miii = mot_clause_iii(delta, e1[0], e1[1], e1[2], e4[1], e4[2])
        bloc["clause_i"] = mi
        bloc["clause_iii"] = miii
        if delta == 0:
            a = moy["abstention_par_vote"]
            bloc["clause_ii"] = {"mot": "sans prise", "abstention_par_vote": a,
                                 "valeur_plantee": ABSTENTION_PLANTEE_PAR_VOTE,
                                 "faute_du_banc": bool(abs(a - ABSTENTION_PLANTEE_PAR_VOTE) > 0.02)}
        porte = loi == LOI_QUI_DECIDE
        bloc["mot_de_la_carte"] = (mot_carte_fcfa(s, mi, miii) if porte else "sans mot (loi rapportée à côté)")
        if porte and s > 0 and delta == 0 and bloc["mot_de_la_carte"] == "réfuté sur le banc":
            bloc["mention"] = "à δ = 0, « réfuté » dit le coût du mécanisme quand aucun juge ne lit la surface"
        sortie["par_loi"][loi] = bloc
    return sortie


def cellule_cadrage(rng_t, t, delta, R, seuils=SEUILS_CADRAGE, s=1.0):
    monde = tirer_monde_double_rendu(rng_t, R, t, s, delta, juges=2)
    sortie = {"t": t, "delta": delta, "s": s, "repliques": R, "par_loi": {}}
    for loi in LOIS_LECTEUR:
        v1, v2 = votes_double_rendu(monde, loi)
        inversion = (v1 != v2).mean(axis=(1, 2))
        sortie["par_loi"][loi] = {"taux_d_inversion_moyen": float(inversion.mean()),
                                  "part_des_rondes_declenchees": {str(c): float((inversion > c).mean()) for c in seuils}}
    return sortie


def mot_branche_3(part_saine, part_delta_05):
    if part_saine > 0.10:
        return "réfuté sur le banc"
    if part_delta_05 >= 0.5:
        return "tient sur le banc"
    return "sans prise"


# ---------------------------------------------------------------------------------------------------------------
# Alarme de changement de juge sous un nom inchangé (fcbf4a2dd1a57)
# ---------------------------------------------------------------------------------------------------------------
GENERATIONS = 12
NIVEAU_ALARME = 0.05 / 11


def table_p_valeurs_binomiales(m, p0):
    """Valeur de probabilité bilatérale exacte, x = 0..m, sous Bin(m, p0) : somme des probabilités au plus égales
    (tolérance relative 1e-7)."""
    pmf = np.array([math.comb(m, x) * p0 ** x * (1 - p0) ** (m - x) for x in range(m + 1)])
    pv = np.array([pmf[pmf <= pmf[x] * (1 + 1e-7)].sum() for x in range(m + 1)])
    return np.minimum(pv, 1.0)


def _premiere_alarme(alarmes, gens, depuis):
    """Première génération d'alarme à partir de `depuis` (incluse) ; 0 si aucune."""
    masque = alarmes & (gens[None, :] >= depuis[:, None])
    premier = np.where(masque.any(axis=1), gens[np.argmax(masque, axis=1)], 0)
    return premier


def cellule_alarme(rng, m, R):
    idx = np.arange(R)
    change = idx < R // 2
    effet = idx < R // 4
    profil_a = (idx < R // 4) | ((idx >= R // 2) & (idx < (3 * R) // 4))
    vr0 = np.where(profil_a, 0.10, 0.05)
    fa0 = np.where(profil_a, 0.10, 0.15)
    vr1 = np.where(effet, 0.25, 0.15)
    fa1 = np.where(effet, 0.25, 0.05)
    g_change = rng.integers(4, 11, size=R)
    gens = np.arange(1, GENERATIONS + 1)
    apres = change[:, None] & (gens[None, :] >= g_change[:, None])
    vr = np.where(apres, vr1[:, None], vr0[:, None])
    fa = np.where(apres, fa1[:, None], fa0[:, None])
    erreurs_reference = rng.binomial(50, vr0) + rng.binomial(50, fa0)
    ancres = rng.binomial(m // 2, vr) + rng.binomial(m - m // 2, fa)
    production = rng.binomial(70, 1 - vr) + rng.binomial(30, fa)
    bons_extra = int(round(0.7 * m))
    extra = rng.binomial(bons_extra, 1 - vr) + rng.binomial(m - bons_extra, fa)

    tables = np.stack([table_p_valeurs_binomiales(m, k / 100.0) for k in range(101)])
    pv = tables[erreurs_reference[:, None], ancres]
    alarmes = {"A": np.zeros((R, GENERATIONS - 1), dtype=bool),
               "B": pv[:, 1:] <= NIVEAU_ALARME}
    z_crit = statistics.NormalDist().inv_cdf(1 - NIVEAU_ALARME / 2)
    for nom, comptes, M in (("C", production, 100), ("D", production + extra, 100 + m)):
        p1 = comptes[:, :1] / M
        pg = comptes[:, 1:] / M
        pool = (comptes[:, :1] + comptes[:, 1:]) / (2.0 * M)
        se = np.sqrt(pool * (1 - pool) * 2.0 / M)
        with np.errstate(divide="ignore", invalid="ignore"):
            z = np.where(se > 0, (pg - p1) / np.where(se > 0, se, 1.0), 0.0)
        alarmes[nom] = (se > 0) & (np.abs(z) >= z_crit)
    gens_test = gens[1:]
    sortie = {"m": m, "suites": R, "par_bras": {}}
    for nom, a in alarmes.items():
        un = np.ones(R, dtype=int)
        premiere = _premiere_alarme(a, gens_test, np.where(change, g_change, un))
        avant = (a & (gens_test[None, :] < np.where(change, g_change, 99)[:, None])).any(axis=1)
        detecte = change & (premiere > 0)
        bloc = {
            "detection_changement_a_effet": float(detecte[effet].mean()) if effet.any() else None,
            "detection_changement_sans_effet": float(detecte[change & ~effet].mean()) if (change & ~effet).any() else None,
            "delai_moyen_changement_a_effet": (float((premiere - g_change)[detecte & effet].mean())
                                               if (detecte & effet).any() else None),
            "fausse_alarme_suites_sans_changement": float(a[~change].any(axis=1).mean()) if (~change).any() else None,
            "alarme_avant_changement_suites_changees": float(avant[change].mean()) if change.any() else None,
            "part_des_detections_sur_changement_a_effet": (float(effet[detecte].mean()) if detecte.any() else None),
        }
        sortie["par_bras"][nom] = bloc
    return sortie


# ---------------------------------------------------------------------------------------------------------------
# Configuration, énumération des cellules, exécution
# ---------------------------------------------------------------------------------------------------------------
CONFIGURATION_DECISIVE = {
    "repliques": 2000,
    "tirages_reechantillonnage": 2000,
    "estimateur": {"J": [2, 5], "lois_J2": [1, 2, 3], "lois_J5": [1, 4], "profils": list(NOMS_PROFILS),
                   "rhos": list(RHOS), "n": list(N_GRILLE)},
    "puissance": {"ecarts": list(ECARTS_PUISSANCE), "lois": [1, 3], "rhos": list(RHOS), "rhos_prime": list(RHOS_PRIME_R),
                  "n": 100},
    "ecart_rho_prime": {"ecarts": list(ECARTS_RHO_PRIME), "rhos": list(RHOS), "taux": 0.20, "n": 100},
    "double_rendu": {"n": list(N_GRILLE), "s": [0.0, 0.5, 1.0], "deltas": [0.0, 0.2, 0.5]},
    "cadrage": {"t": [20, 40], "deltas": [0.0, 0.2, 0.5], "seuils": list(SEUILS_CADRAGE)},
    "alarme": {"m": [10, 20, 40], "suites": 2000},
}


def enumerer_cellules_estimateur(cfg):
    """Ordre gelé : J, loi, profil, ρ, n. Loi 3 à p = 0,20 et ρ ≤ 0,75 ; loi 4 à cinq juges, taux égaux entre juges."""
    e = cfg["estimateur"]
    cellules = []
    for J in e["J"]:
        lois = e["lois_J2"] if J == 2 else e["lois_J5"]
        for loi in lois:
            if loi == 3:
                profils = [p for p in e["profils"] if p == PROFIL_DE_LA_REGLE]
            elif loi == 4:
                profils = [p for p in e["profils"] if p != "inegal"]
            else:
                profils = list(e["profils"])
            rhos = [r for r in e["rhos"] if r <= RHO_MAX_LOI_3 + EPS] if loi == 3 else list(e["rhos"])
            for nom in profils:
                for rho in rhos:
                    for n in e["n"]:
                        cellules.append((J, loi, nom, rho, n))
    return cellules


def criteres_estimateur(cellules):
    """Table « plus petit n qui tient », verdict mécanique de l'estimateur et garde P2."""
    tient = {}
    for c in cellules:
        tient[(c["J"], c["loi"], c["profil"], c["rho_grille"], c["n"])] = c["estimateur"]["tient"]
    ecarts_p2 = [c["theorie_p2"]["ecart_maximal"] for c in cellules if "theorie_p2" in c]
    p2 = "invalide" if any(e > 0.02 for e in ecarts_p2) else ("valide" if ecarts_p2 else "non jouée")
    plus_petit_par_cellule = {}
    groupes = {}
    for (J, loi, nom, rho, n), t in tient.items():
        groupes.setdefault((J, loi, nom, rho), []).append((n, t))
    for cle, liste in groupes.items():
        ns = sorted(n for n, t in liste if t)
        plus_petit_par_cellule["|".join(str(x) for x in cle)] = ns[0] if ns else None
    par_loi = {}
    familles = {}
    for (J, loi, nom, rho, n), t in tient.items():
        familles.setdefault((J, loi, nom), {}).setdefault(n, []).append(t)
    for (J, loi, nom), par_n in familles.items():
        ns = sorted(n for n, v in par_n.items() if all(v))
        par_loi[f"{J}|{loi}|{nom}"] = ns[0] if ns else None

    attendues = ([(2, 1, PROFIL_DE_LA_REGLE, r) for r in RHOS]
                 + [(2, 3, PROFIL_DE_LA_REGLE, r) for r in RHOS if r <= RHO_MAX_LOI_3 + EPS])

    def tient_a(n):
        cles = [a + (n,) for a in attendues]
        if any(k not in tient for k in cles):
            return None
        return all(tient[k] for k in cles)

    etats = {n: tient_a(n) for n in N_GRILLE}
    if p2 == "invalide":
        verdict, taille = "invalide : faute du banc, à corriger avant toute lecture", None
    elif any(v is None for v in etats.values()):
        verdict, taille = "incomplet : cellules de la règle manquantes", None
    elif etats[100]:
        verdict, taille = "oui de l'étage 1 : l'étage 2 se joue à 100 témoins", 100
    elif any(etats[n] for n in N_GRILLE if n > 100):
        taille = min(n for n in N_GRILLE if n > 100 and etats[n])
        verdict = "non, pas à cette taille : pas de dépense ; table et devis à la taille voulue rendus à Lazar"
    elif not any(etats.values()):
        verdict, taille = "non : l'estimateur est trop bruité ou faux ; étage 2 non joué", None
    else:
        verdict, taille = "cas non prévu par la table gelée (tient à n = 50 seulement) : rendu à la mère", None
    return {"theorie_p2": p2, "tient_aux_cellules_de_la_regle_par_n": {str(n): v for n, v in etats.items()},
            "verdict_mecanique_estimateur": verdict, "taille_retenue_par_la_regle": taille,
            "plus_petit_n_qui_tient_par_cellule": plus_petit_par_cellule,
            "plus_petit_n_qui_tient_par_J_loi_profil": par_loi}


TAILLES_D_ETALONNAGE = tuple(n // 2 for n in N_GRILLE)


def plus_petite_taille_a_partir_de_laquelle(tient_par_taille, grille=TAILLES_D_ETALONNAGE):
    """Lettre du texte (branche (2), « à partir de laquelle ») : la plus petite taille t de la grille telle que la branche
    tient dans toutes les cellules à t et à toutes les tailles plus grandes de la grille. Rend (taille, manquantes) :
    taille None si la plus grande taille de la grille ne tient pas ; si une taille de la grille n'a aucune cellule,
    (None, liste des tailles manquantes), jamais un repli silencieux."""
    manquantes = [t for t in grille if t not in tient_par_taille]
    if manquantes:
        return None, manquantes
    retenue = None
    for t in sorted(grille, reverse=True):
        if tient_par_taille[t]:
            retenue = t
        else:
            break
    return retenue, []


def criteres_branche_2(cellules):
    """Branche (2) de fefca0bd94064 : à cinq juges, lois 1 et 4, par taille d'étalonnage (n / 2)."""
    mots = {}
    par_taille = {}
    for c in cellules:
        if c["J"] != 5 or c["loi"] not in (1, 4):
            continue
        ecart = c["bras"]["C"]["erreur_equilibree"] - c["bras"]["poids_egaux"]["erreur_equilibree"]
        mot = "réfuté sur le banc" if ecart > 0.02 else "tient sur le banc"
        taille = c["n"] // 2
        mots[f"{c['loi']}|{c['profil']}|{c['rho_grille']}|{taille}"] = {"ecart_C_moins_poids_egaux": ecart, "mot": mot}
        par_taille.setdefault(taille, []).append(mot == "tient sur le banc")
    tient_par_taille = {t: all(v) for t, v in par_taille.items()}
    taille, manquantes = plus_petite_taille_a_partir_de_laquelle(tient_par_taille)
    if manquantes:
        taille = f"incomplet : tailles de la grille sans cellule {manquantes}"
    return {"par_cellule": mots, "a_deux_juges": "sans prise (§ 0)",
            "tient_dans_toutes_les_cellules_par_taille_d_etalonnage": {str(t): v for t, v in sorted(tient_par_taille.items())},
            "plus_petite_taille_d_etalonnage_a_partir_de_laquelle_la_branche_tient_partout": taille}


def criteres_branche_3(cadrage):
    mots = {}
    for loi in LOIS_LECTEUR:
        for t in sorted({c["t"] for c in cadrage}):
            for cle_c in [str(c) for c in SEUILS_CADRAGE]:
                saine = [c for c in cadrage if c["t"] == t and c["delta"] == 0]
                forte = [c for c in cadrage if c["t"] == t and abs(c["delta"] - 0.5) < EPS]
                if not saine or not forte or cle_c not in saine[0]["par_loi"][loi]["part_des_rondes_declenchees"]:
                    continue
                ps = saine[0]["par_loi"][loi]["part_des_rondes_declenchees"][cle_c]
                pf = forte[0]["par_loi"][loi]["part_des_rondes_declenchees"][cle_c]
                mot = mot_branche_3(ps, pf)
                if loi == "seduit_sinon_fond":
                    mot = "rapporté sans mot (" + mot + ")"
                mots[f"{loi}|t={t}|c={cle_c}"] = {"part_saine": ps, "part_delta_0.5": pf, "mot": mot}
    return mots


def executer_etage_1(contexte, cfg, dossier_sortie):
    """Joue le banc entier selon `cfg`, écrit le résultat et le manifeste dans un dossier neuf (une fois)."""
    dossier = Path(dossier_sortie)
    if dossier.exists():
        raise RefusExecution(f"dossier de sortie déjà présent : {dossier} (une exécution par dossier)")
    verifier_gardes_avant_tirage()
    debut = datetime.datetime.now(datetime.timezone.utc)
    R, B = cfg["repliques"], cfg["tirages_reechantillonnage"]

    cellules_e = enumerer_cellules_estimateur(cfg)
    gt = contexte.tirages("estimateur_et_agregation", len(cellules_e))
    gr = contexte.reechantillonnage("reechantillonnage_estimateur_et_agregation", len(cellules_e))
    res_e = [cellule_estimateur_agregation(gt[i], gr[i], loi, J, nom, rho, n, R, B)
             for i, (J, loi, nom, rho, n) in enumerate(cellules_e)]

    cp = cfg["puissance"]
    cellules_p = enumerer_cellules_puissance(cp)
    gt = contexte.tirages("monde_de_puissance", len(cellules_p))
    gr = contexte.reechantillonnage("reechantillonnage_monde_de_puissance", len(cellules_p))
    res_p = [cellule_puissance(gt[i], gr[i], comp, ec, loi, rho, rp, R, B, n=cp["n"])
             for i, (comp, ec, loi, rho, rp) in enumerate(cellules_p)]

    cr = cfg["ecart_rho_prime"]
    cellules_r = [(ec, rho) for ec in cr["ecarts"] for rho in cr["rhos"]]
    gt = contexte.tirages("ecart_rho_prime_moins_rho", len(cellules_r))
    gr = contexte.reechantillonnage("reechantillonnage_ecart_rho_prime_moins_rho", len(cellules_r))
    res_r = [cellule_ecart_rho_prime(gt[i], gr[i], ec, rho, R, B, n=cr["n"], p=cr["taux"])
             for i, (ec, rho) in enumerate(cellules_r)]

    cd = cfg["double_rendu"]
    cellules_d = [(n, s, dl) for n in cd["n"] for s in cd["s"] for dl in cd["deltas"]]
    gt = contexte.tirages("double_rendu", len(cellules_d))
    gr = contexte.reechantillonnage("reechantillonnage_double_rendu", len(cellules_d))
    res_d = [cellule_double_rendu(gt[i], gr[i], n, s, dl, R, B) for i, (n, s, dl) in enumerate(cellules_d)]

    cc = cfg["cadrage"]
    cellules_c = [(t, dl) for t in cc["t"] for dl in cc["deltas"]]
    gt = contexte.tirages("garde_de_cadrage", len(cellules_c))
    res_c = [cellule_cadrage(gt[i], t, dl, R, seuils=tuple(cc["seuils"])) for i, (t, dl) in enumerate(cellules_c)]

    ca = cfg["alarme"]
    gt = contexte.tirages("alarme", len(ca["m"]))
    res_a = [cellule_alarme(gt[i], m, ca["suites"]) for i, m in enumerate(ca["m"])]

    resultat = {
        "version": VERSION,
        "mode": contexte.mode,
        "note": ("Les mots et verdicts ci-dessous sont l'application mécanique des critères gelés, calculée par le code ; "
                 "le verdict de l'étage 1 est prononcé par un agent neuf (règle R13). Aucun mot ne valide, n'écarte ni "
                 "ne classe une carte."),
        "criteres_mecaniques": {
            "estimateur": criteres_estimateur(res_e),
            "puissance": puissance_qui_decide(res_p),
            "branche_2_fefca0bd94064": criteres_branche_2(res_e),
            "branche_3_fefca0bd94064": criteres_branche_3(res_c),
            "branche_1_fefca0bd94064": "non jouée (GO-2026-11-19-73)",
        },
        "estimateur_et_agregation": res_e,
        "monde_de_puissance": res_p,
        "ecart_rho_prime_moins_rho": res_r,
        "double_rendu": res_d,
        "garde_de_cadrage": res_c,
        "alarme": res_a,
    }
    fin = datetime.datetime.now(datetime.timezone.utc)
    dossier.mkdir(parents=True, exist_ok=False)
    chemin_res = dossier / "resultat-etage-1-ligne-3-v2.json"
    ecrire_json_exclusif(chemin_res, resultat)
    manifeste = construire_manifeste(contexte, cfg, debut, fin, {chemin_res.name: sha256_fichier(chemin_res)})
    ecrire_json_exclusif(dossier / "manifeste-etage-1-ligne-3-v2.json", manifeste)
    return resultat, manifeste


# ---------------------------------------------------------------------------------------------------------------
# Gardes déterministes rejouées avant le premier tirage d'une exécution (aucune graine)
# ---------------------------------------------------------------------------------------------------------------
def verifier_gardes_avant_tirage():
    y = classes(4)
    E = np.array([[[1, 1], [0, 0], [1, 1], [0, 0], [0, 0], [1, 1], [0, 0], [1, 1]]], dtype=bool)
    r, ind = rho_moyenne(cov_intra_classes(E, y))
    if ind[0] or votes_effectifs(r, 2)[0] != 1.0:
        raise BancInvalide("garde de l'estimateur : un juge dupliqué ne rend pas un vote effectif")
    E2 = E.copy()
    E2[..., 1] = False
    r2, ind2 = rho_moyenne(cov_intra_classes(E2, y))
    if not ind2[0] or np.isfinite(r2[0]):
        raise BancInvalide("garde de l'estimateur : un juge sans erreur ne rend pas « indéfini »")
    if regle_choisie([1.0, 1.0], -1.0) != "au_moins_un" or regle_choisie([1.0, 1.0], 3.0) != "constante":
        raise BancInvalide("garde de la règle choisie à deux juges")
    if list(q_porteuse([4.0, 3.0, 2.0, 1.0, 5.0])) != [4, 4, 5, 5, 3]:
        raise BancInvalide("garde de la règle de la porteuse (arrondi au demi supérieur)")


# ---------------------------------------------------------------------------------------------------------------
# Manifeste (R9) et écriture
# ---------------------------------------------------------------------------------------------------------------
def ecrire_json_exclusif(chemin, objet):
    chemin = Path(chemin)
    texte = json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False, default=_json_defaut) + "\n"
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(texte)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{sha256_fichier(chemin)}  {chemin.name}\n")


def _json_defaut(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        x = float(o)
        return x if math.isfinite(x) else None
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"type non sérialisable : {type(o)}")


def _nettoyer(o):
    if isinstance(o, dict):
        return {str(k): _nettoyer(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_nettoyer(v) for v in o]
    if isinstance(o, float) and not math.isfinite(o):
        return None
    return o


def commit_du_depot():
    dossier = Path(__file__).resolve().parent
    try:
        tete = subprocess.run(["git", "-C", str(dossier), "rev-parse", "HEAD"], capture_output=True, text=True,
                              timeout=30)
        etat = subprocess.run(["git", "-C", str(dossier), "status", "--porcelain", "--", str(dossier)],
                              capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return {"commit": "inconnu", "dossier_du_code_propre": None}
    if tete.returncode != 0:
        return {"commit": "inconnu (hors d'un dépôt git)", "dossier_du_code_propre": None}
    return {"commit": tete.stdout.strip(), "dossier_du_code_propre": etat.returncode == 0 and etat.stdout.strip() == ""}


def construire_manifeste(contexte, cfg, debut, fin, fichiers):
    return _nettoyer({
        "programme": VERSION,
        "programme_chemin": str(Path(__file__).resolve()),
        "programme_sha256": sha256_fichier(Path(__file__).resolve()),
        "texte_qui_fait_foi_sha256": EMPREINTE_TEXTE_QUI_FAIT_FOI,
        "mode": contexte.mode,
        "autorisation": contexte.autorisation.decrire() if contexte.autorisation else None,
        "configuration": cfg,
        "configuration_sha256": sha256_json(_nettoyer(cfg)),
        "versions": {"python": sys.version, "numpy": np.__version__, "plateforme": platform.platform(),
                     "executable": sys.executable},
        "graines": {"methode": "numpy.random.SeedSequence(racine, spawn_key=(clé,)).spawn(nombre), enfant de rang fixe",
                    "racine_des_tirages": contexte.racine_tirages,
                    "racine_du_reechantillonnage": contexte.racine_reechantillonnage,
                    "table_cles": TABLE_CLES, "derivations": contexte.derivations},
        "depot": commit_du_depot(),
        "heure_debut_utc": debut.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "heure_fin_utc": fin.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fichiers": fichiers,
    })


def main(argv=None):
    parser = argparse.ArgumentParser(description="Banc de juges scriptés, ligne 3, étage 1 (décisif, geste 4).")
    parser.add_argument("--decisif", action="store_true", required=True)
    parser.add_argument("--autorisation-additif", required=True)
    parser.add_argument("--empreinte-additif", required=True)
    parser.add_argument("--sortie", required=True)
    args = parser.parse_args(argv)
    autorisation = Autorisation(args.autorisation_additif, args.empreinte_additif)
    verifier_autorisation(autorisation, RACINE_ETAGE_1_DECISIF)
    contexte = Contexte("decisif", autorisation)
    executer_etage_1(contexte, CONFIGURATION_DECISIVE, args.sortie)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RefusGraine, RefusExecution, BancInvalide, RegleInconnue) as exc:
        print(f"refus : {exc}", file=sys.stderr)
        sys.exit(2)
