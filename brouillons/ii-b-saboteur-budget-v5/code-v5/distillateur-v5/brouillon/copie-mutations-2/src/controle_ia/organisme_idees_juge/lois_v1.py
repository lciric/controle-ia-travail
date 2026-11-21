"""Lois du banc B v2 : constructeurs (grammaire du juge), composantes V1 à V5, évaluateur vectorisé, cosinus.

L'évaluateur vectorisé `probas_np` recopie la sémantique de `selection_pari.proba` (plancher 10⁻¹², renormalisation
à chaque nœud, mêmes opérations dans le même ordre) pour les seuls types employés par le banc (`fixe`, `softmax`,
`par_sous_population`, `melange`, `si_sinon`, `transformee`) ; il refuse les autres. Il ne sert **qu'à l'oracle et à
la règle du cosinus** (20 000 instances par génération : la boucle pure du juge y serait trop lente) ; les richesses
des cartes sont toujours calculées par le juge réel. L'égalité avec `selection_pari.proba` est éprouvée par les essais
(écart absolu ≤ 10⁻¹²).

Lectures du texte scellé faites ici (dites au rapport du développeur) :
- softmax aléatoire : poids N(0 ; 1,5²) puis biais N(0 ; 0,3²), arrondis à six décimales ; une loi construite
  (S1 portant une composante) est arrondie à six décimales à sa création ;
- « direction de la composante bruitée » : bruit gaussien de norme 0,3 fois celle de la direction (centré par colonne
  pour Δ, centré pour u), puis renormalisation à la norme d'origine ; pour V4, la direction est le vecteur des neuf
  paramètres (poids, biais) de la loi neuve N ;
- doublon : chaque nombre du champ « poids » de chaque loi softmax de M, plus 0,01·N(0, 1), arrondi ; biais inchangés ;
- « force × f » : dose multipliée par f (f < 0 : composante de signe opposé).
"""
from __future__ import annotations

import copy
import math
from dataclasses import dataclass, field

import numpy as np

from ..gardes import GardeArret

K, D = 3, 2
PLANCHER = 1e-12
UNIFORME = {"type": "fixe", "probas": [1.0] * K}
TYPES_VECTORISES = ("fixe", "softmax", "par_sous_population", "melange", "si_sinon", "transformee")


# --- évaluateur vectorisé ------------------------------------------------------------------------------------------
def _norm(P: np.ndarray) -> np.ndarray:
    P = np.maximum(P, PLANCHER)
    return P / P.sum(axis=1, keepdims=True)


def probas_np(loi: dict, Z: np.ndarray, G: np.ndarray) -> np.ndarray:
    """Probabilités (n, K) de la loi sur les instances (traits Z (n, D), sous-populations G (n,))."""
    t = loi.get("type")
    n = Z.shape[0]
    if t == "fixe":
        p = np.maximum(np.asarray(loi["probas"], dtype=float), PLANCHER)
        p = p / p.sum()
        return np.broadcast_to(p, (n, len(p))).copy()
    if t == "softmax":
        W = np.asarray(loi["poids"], dtype=float)
        b = np.asarray(loi["biais"], dtype=float)
        acc = Z[:, 0:1] * W[None, :, 0]
        for j in range(1, W.shape[1]):
            acc = acc + Z[:, j:j + 1] * W[None, :, j]
        S = b[None, :] + acc
        E = np.exp(S - S.max(axis=1, keepdims=True))
        return _norm(E)
    if t == "par_sous_population":
        sortie = np.empty((n, K))
        for gv in np.unique(G):
            sous = loi["lois"].get(str(int(gv)), loi.get("defaut"))
            if sous is None:
                raise GardeArret(f"par_sous_population : aucune loi pour la sous-population {gv}")
            m = G == gv
            sortie[m] = probas_np(sous, Z[m], G[m])
        return sortie
    if t == "melange":
        mix = np.zeros((n, K))
        for w, c in zip(loi["poids"], loi["composantes"]):
            mix = mix + w * probas_np(c, Z, G)
        return _norm(mix)
    if t == "si_sinon":
        c = loi["condition"]
        if "sous_population" in c:
            masque = G == c["sous_population"]
        else:
            masque = Z[:, c["indice"]] > c.get("seuil", 0.0)
        return np.where(masque[:, None], probas_np(loi["si"], Z, G), probas_np(loi["sinon"], Z, G))
    if t == "transformee":
        p = probas_np(loi["base"], Z, G)
        if loi.get("melange_aveugle"):
            lam = loi["melange_aveugle"]["lambda"]
            bb = np.maximum(np.asarray(loi["melange_aveugle"]["probas"], dtype=float), PLANCHER)
            bb = bb / bb.sum()
            p = (1 - lam) * p + lam * bb[None, :]
        if loi.get("puissance") is not None:
            p = _norm(np.maximum(p, PLANCHER) ** loi["puissance"])
        if loi.get("inclinaison"):
            p = _norm(p * np.exp(np.asarray(loi["inclinaison"], dtype=float))[None, :])
        if loi.get("oscillation"):
            o = loi["oscillation"]
            f = np.exp(o["amplitude"] * np.cos(o["frequence"] * Z[:, o["trait"]] + o.get("phase", 0.0)))
            p = p.copy()
            p[:, o["issue"]] = p[:, o["issue"]] * f
            p = _norm(p)
        return _norm(p)
    raise GardeArret(f"évaluateur vectorisé : type {t!r} hors du banc (types admis : {TYPES_VECTORISES})")


def tirer_issues_np(P: np.ndarray, u: np.ndarray) -> np.ndarray:
    """Issue catégorielle par inversion, comme `selection_pari.tirer_categorie` (premier k tel que u < cumul ; sinon K−1)."""
    c = np.cumsum(P, axis=1)
    return np.minimum((c <= u[:, None]).sum(axis=1), P.shape[1] - 1).astype(np.int64)


def cosinus(p_a: np.ndarray, p_b: np.ndarray, base: np.ndarray) -> float:
    """Cosinus du texte : E_x[f·f′] / (E_x‖f‖² · E_x‖f′‖²)^½, f = p_a − base, f′ = p_b − base (moyennes sur les instances)."""
    f, fp = p_a - base, p_b - base
    num = float(np.mean(np.sum(f * fp, axis=1)))
    den = math.sqrt(float(np.mean(np.sum(f * f, axis=1))) * float(np.mean(np.sum(fp * fp, axis=1))))
    if den == 0.0:
        raise GardeArret("cosinus : composante nulle sur les instances de l'oracle")
    return num / den


# --- constructeurs --------------------------------------------------------------------------------------------------
def _l(a) -> list:
    return [float(x) for x in np.asarray(a).ravel()]


def softmax(W, b) -> dict:
    W = np.round(np.asarray(W, dtype=float), 6)
    return {"type": "softmax", "poids": [[float(x) for x in ligne] for ligne in W], "biais": _l(np.round(np.asarray(b, dtype=float), 6))}


def softmax_aleatoire(rng: np.random.Generator) -> dict:
    W = rng.normal(0.0, 1.5, size=(K, D))
    b = rng.normal(0.0, 0.3, size=K)
    return softmax(W, b)


def poids_de(loi: dict) -> tuple[np.ndarray, np.ndarray]:
    return np.asarray(loi["poids"], dtype=float), np.asarray(loi["biais"], dtype=float)


def si_sinon_trait(j: int, seuil: float, si: dict, sinon: dict) -> dict:
    return {"type": "si_sinon", "condition": {"indice": int(j), "seuil": float(seuil)}, "si": si, "sinon": sinon}


def par_sous_population(l0: dict, l1: dict) -> dict:
    return {"type": "par_sous_population", "lois": {"0": l0, "1": l1}}


def melange(composantes: list, poids) -> dict:
    return {"type": "melange", "composantes": list(composantes), "poids": [float(x) for x in poids]}


def poids_dirichlet(rng: np.random.Generator, nombre: int) -> list:
    """Poids ~ Dirichlet(1, …, 1), arrondis à six décimales et renormalisés."""
    w = np.round(rng.dirichlet(np.ones(nombre)), 6)
    w = w / w.sum()
    return [float(x) for x in w]


def melange_archive(archive: dict, rng: np.random.Generator) -> dict:
    """Ligne Q1 : `melange`([S1, S2, S3, S4, uniforme fixe], poids de Dirichlet)."""
    return melange([archive["S1"], archive["S2"], archive["S3"], archive["S4"], copy.deepcopy(UNIFORME)], poids_dirichlet(rng, 5))


def transformee(base: dict, puissance: float, inclinaison) -> dict:
    return {"type": "transformee", "base": base, "puissance": float(puissance), "inclinaison": [float(x) for x in inclinaison]}


def tempere_incline(base: dict, rng: np.random.Generator) -> dict:
    """Loi tempérée et inclinée : puissance U[0,7 ; 1,3], inclinaison N(0 ; 0,2²) par issue, arrondies à six décimales."""
    a = round(float(rng.uniform(0.7, 1.3)), 6)
    beta = np.round(rng.normal(0.0, 0.2, size=K), 6)
    return transformee(base, a, beta)


def delta_centre(rng: np.random.Generator) -> np.ndarray:
    """Δ ~ N(0, 1) (K × D), centrée par colonne sur les issues."""
    d = rng.standard_normal((K, D))
    return d - d.mean(axis=0, keepdims=True)


def u_centre_norme(rng: np.random.Generator) -> np.ndarray:
    u = rng.normal(size=K)
    u = u - u.mean()
    return u / np.linalg.norm(u)


def coupure_archive(rng: np.random.Generator) -> float:
    """s ~ U[−1 ; 1] au centième, retiré tant que |s| < 0,3 (banc B v2)."""
    while True:
        s = round(float(rng.uniform(-1.0, 1.0)), 2)
        if abs(s) >= 0.3:
            return s


def seuil_decentre(rng: np.random.Generator, coupure_du_trait: float) -> float:
    """V3 : c = ±U[0,3 ; 0,8] au centième, retiré tant que |c − cut(j)| < 0,3."""
    while True:
        c = round(float(rng.choice([-1, 1]) * rng.uniform(0.3, 0.8)), 2)
        if abs(c - coupure_du_trait) >= 0.3:
            return c


def perturber_poids(loi: dict, rng: np.random.Generator, ecart: float = 0.01) -> dict:
    """Doublon : chaque nombre du champ « poids » de chaque loi softmax (parcours de l'arbre), plus ecart·N(0, 1)."""
    loi = copy.deepcopy(loi)

    def visite(x):
        if not isinstance(x, dict):
            return
        if x.get("type") == "softmax":
            W = np.asarray(x["poids"], dtype=float)
            W = np.round(W + ecart * rng.standard_normal(W.shape), 6)
            x["poids"] = [[float(v) for v in ligne] for ligne in W]
            return
        for cle in ("si", "sinon", "base", "loi", "defaut"):
            visite(x.get(cle))
        for cle in ("lois", "composantes"):
            sous = x.get(cle)
            if isinstance(sous, dict):
                for nom in sorted(sous):
                    visite(sous[nom])
            elif isinstance(sous, list):
                for s in sous:
                    visite(s)

    visite(loi)
    return loi


def bruiter_direction(d: np.ndarray, rng: np.random.Generator, part: float = 0.3, centrage: str = "vecteur") -> np.ndarray:
    """Bruit gaussien de norme `part`·‖d‖ ajouté à d, puis renormalisation à ‖d‖. Centrage du bruit : « colonnes »
    (Δ, centrée par colonne sur les issues) ou « vecteur » (u, centré)."""
    n = rng.standard_normal(d.shape)
    if centrage == "colonnes":
        n = n - n.mean(axis=0, keepdims=True)
    elif centrage == "vecteur":
        n = n - n.mean()
    else:
        raise GardeArret(f"centrage inconnu {centrage!r}")
    norme = float(np.linalg.norm(d))
    n = n * (part * norme / float(np.linalg.norm(n)))
    dp = d + n
    return dp * (norme / float(np.linalg.norm(dp)))


# --- composantes V1 à V5 --------------------------------------------------------------------------------------------
TYPES = ("V1", "V2", "V3", "V4", "V5")
DOSES = {"V1": (0.25, 0.50), "V2": (0.4, 0.8), "V3": (0.4, 0.8), "V4": (0.1, 0.2), "V5": (0.4, 0.8)}
# Cellule c = g mod 10 : types dans l'ordre V1 à V5, dose basse puis dose haute (lecture du texte : « dix cellules »).
CELLULES = tuple((t, i_dose, DOSES[t][i_dose]) for t in TYPES for i_dose in (0, 1))


def cellule(g: int) -> tuple[str, int, float]:
    return CELLULES[g % 10]


@dataclass
class Composante:
    """Composante posée sur S1 : type, dose, paramètres tirés ; `loi(f)` rend S1 portant la composante à la dose × f."""
    genre: str
    dose: float
    archive: dict
    params: dict = field(default_factory=dict)

    def loi(self, force: float = 1.0) -> dict:
        S1 = self.archive["S1"]
        W1, b1 = poids_de(S1)
        x = self.dose * force
        if self.genre == "V1":
            return softmax(W1 + x * self.params["delta"], b1)
        if self.genre in ("V2", "V3", "V5"):
            j_cond, seuil, j_effet = self.condition()
            E = np.zeros((K, D))
            E[:, j_effet] = self.params["u"]
            return si_sinon_trait(j_cond, seuil, softmax(W1 + x * E, b1), softmax(W1 - x * E, b1))
        if self.genre == "V4":
            if not 0.0 <= x <= 1.0:
                raise GardeArret(f"V4 : poids de mélange {x} hors de [0 ; 1] (pas une loi de la grammaire du juge)")
            return par_sous_population(S1, melange([S1, self.params["N"]], [1.0 - x, x]))
        raise GardeArret(f"composante inconnue {self.genre!r}")

    def condition(self) -> tuple[int, float, int]:
        """(trait de la condition, seuil, trait de l'effet) pour V2, V3, V5."""
        if self.genre == "V2":
            j = self.params["j"]
            return j, 0.0, 1 - j
        if self.genre == "V3":
            j = self.params["j"]
            return j, self.params["c"], 1 - j
        if self.genre == "V5":
            jA, sA = self.archive["jA"], self.archive["sA"]
            return jA, sA, 1 - jA
        raise GardeArret(f"{self.genre} : pas de condition")

    def bruitee(self, rng: np.random.Generator, part: float = 0.3) -> "Composante":
        p = dict(self.params)
        if self.genre == "V1":
            p["delta"] = bruiter_direction(self.params["delta"], rng, part, centrage="colonnes")
        elif self.genre in ("V2", "V3", "V5"):
            p["u"] = bruiter_direction(self.params["u"], rng, part, centrage="vecteur")
        elif self.genre == "V4":
            W, b = poids_de(self.params["N"])
            theta = np.concatenate([W.ravel(), b])
            n = rng.standard_normal(theta.shape)
            norme = float(np.linalg.norm(theta))
            n = n * (part * norme / float(np.linalg.norm(n)))
            tp = (theta + n) * (norme / float(np.linalg.norm(theta + n)))
            p["N"] = softmax(tp[:K * D].reshape(K, D), tp[K * D:])
        return Composante(self.genre, self.dose, self.archive, p)

    def resume(self) -> dict:
        r = {"type": self.genre, "dose": self.dose}
        for k, v in self.params.items():
            r[k] = v if isinstance(v, (int, float, dict)) else _l(v)
        return r


def tirer_composante(genre: str, dose: float, archive: dict, rng: np.random.Generator) -> Composante:
    """Tire les paramètres d'une composante du type (ordre des tirages : j, c, puis u ; Δ ; N)."""
    if genre == "V1":
        return Composante(genre, dose, archive, {"delta": delta_centre(rng)})
    if genre == "V2":
        j = int(rng.integers(0, 2))
        return Composante(genre, dose, archive, {"j": j, "u": u_centre_norme(rng)})
    if genre == "V3":
        j = int(rng.integers(0, 2))
        c = seuil_decentre(rng, archive["cut"][j])
        return Composante(genre, dose, archive, {"j": j, "c": c, "u": u_centre_norme(rng)})
    if genre == "V4":
        return Composante(genre, dose, archive, {"N": softmax_aleatoire(rng)})
    if genre == "V5":
        return Composante(genre, dose, archive, {"u": u_centre_norme(rng)})
    raise GardeArret(f"type de composante inconnu {genre!r}")


def lois_de(loi: dict) -> list:
    """Sous-lois softmax d'une loi (pour les essais)."""
    sortie = []

    def visite(x):
        if not isinstance(x, dict):
            return
        if x.get("type") == "softmax":
            sortie.append(x)
        for cle in ("si", "sinon", "base", "loi", "defaut"):
            visite(x.get(cle))
        for cle in ("lois", "composantes"):
            sous = x.get(cle)
            if isinstance(sous, dict):
                for nom in sorted(sous):
                    visite(sous[nom])
            elif isinstance(sous, list):
                for s in sous:
                    visite(s)

    visite(loi)
    return sortie
