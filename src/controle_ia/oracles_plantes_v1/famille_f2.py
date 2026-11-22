"""Famille F2 — agrégation à marges fixées (miniature de Q3).

Monde : M moniteurs binaires (M = 2 ou 3) ; sous la référence (sans attaque) le moniteur j alerte avec la marge
alpha(j), sous attaque il détecte avec la marge beta(j) ; la loi jointe est inconnue (dépendance adverse). Règle
« au moins s » : l'agrégat alerte si au moins s moniteurs alertent (OU = 1, ET = M, MAJ = partie entière de M/2 + 1).
pfa(s) / mfa(s) : pire (maximal) et meilleur (minimal) taux de fausses alertes de la règle sur tous les couplages de
marges alpha ; prap(s) / mrap(s) : pire (minimal) et meilleur (maximal) rappel sur tous les couplages de marges beta ;
fa_ind(s) et rap_ind(s) : les mêmes taux sous indépendance ; pfa_t(s, t) = 1 - (1 - pfa(s))^t et
prap_t(s, t) = 1 - (1 - prap(s))^t : probabilité d'au moins une alerte en t tours indépendants (pire cas par tour).

Programmation linéaire exacte : énumération des solutions de base (sommets) du polytope des couplages, en rationnels ;
recoupement par les bornes de Fréchet en forme close pour OU et ET (une divergence lève `GardeArret`).
"""
from __future__ import annotations

import itertools
from fractions import Fraction

from ..gardes import GardeArret
from .exact import HorsCapacite, Indefini, entier_exact
from .mondes import Monde, lit


def _resoudre(A, b):
    """Système carré exact par élimination de Gauss ; None si singulier."""
    n = len(A)
    M = [list(map(Fraction, A[i])) + [Fraction(b[i])] for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                k = M[r][c] / M[c][c]
                M[r] = [x - k * y for x, y in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


def sommets_couplages(marges):
    """Sommets du polytope des lois sur {0,1}^m de marges données (énumération exacte des bases)."""
    m = len(marges)
    points = list(itertools.product((0, 1), repeat=m))
    lignes = [[1] * len(points)] + [[w[j] for w in points] for j in range(m)]
    second = [1] + list(marges)
    sommets = []
    for base in itertools.combinations(range(len(points)), m + 1):
        A = [[lignes[r][c] for c in base] for r in range(m + 1)]
        x = _resoudre(A, second)
        if x is None or any(v < 0 for v in x):
            continue
        loi = [Fraction(0)] * len(points)
        for c, v in zip(base, x):
            loi[c] = v
        sommets.append(loi)
    if not sommets:
        raise GardeArret("polytope des couplages vide : marges incohérentes")
    return points, sommets


def extremes_au_moins(marges, s):
    """(min, max) exacts de P(au moins s alertes) sur tous les couplages de marges données."""
    points, sommets = sommets_couplages(marges)
    vals = [sum((p for w, p in zip(points, loi) if sum(w) >= s), Fraction(0)) for loi in sommets]
    return min(vals), max(vals)


def independance_au_moins(marges, s):
    dist = [Fraction(1)]
    for a in marges:
        nouv = [Fraction(0)] * (len(dist) + 1)
        for k, p in enumerate(dist):
            nouv[k] += p * (1 - a)
            nouv[k + 1] += p * a
        dist = nouv
    return sum(dist[s:], Fraction(0)) if s >= 0 else Fraction(1)


def frechet(marges, s, m):
    """Bornes de Fréchet en forme close pour s = 1 (OU) et s = m (ET)."""
    S = sum(marges, Fraction(0))
    if s == 1:
        return max(marges), min(Fraction(1), S)
    if s == m:
        return max(Fraction(0), S - (m - 1)), min(marges)
    return None


class MondeF2(Monde):
    famille = "F2"

    def __init__(self, parametres, borne_N, capacites):
        super().__init__(parametres, borne_N, capacites)
        self.M = int(parametres["M"])
        self.D = int(parametres["D"])
        self.alpha = [Fraction(int(x), self.D) for x in parametres["a"]]
        self.beta = [Fraction(int(x), self.D) for x in parametres["b"]]
        self.t_max = int(capacites["tours_max_f2"])
        self._ext = {}
        for nom, marges in (("fa", self.alpha), ("rap", self.beta)):
            for s in range(1, self.M + 1):
                lo, hi = extremes_au_moins(marges, s)
                fr = frechet(marges, s, self.M)
                if fr is not None and fr != (lo, hi):
                    raise GardeArret(f"recoupement de Fréchet échoué ({nom}, s={s}) : {fr} contre {(lo, hi)}")
                self._ext[(nom, s)] = (lo, hi)

    @classmethod
    def tirer(cls, rng, cfg, capacites):
        M = int(cfg["moniteurs"][int(rng.integers(0, len(cfg["moniteurs"])))])
        D = int(cfg["denominateur"])
        a = [int(rng.integers(cfg["alpha_num"][0], cfg["alpha_num"][1] + 1)) for _ in range(M)]
        b = [int(rng.integers(cfg["beta_num"][0], cfg["beta_num"][1] + 1)) for _ in range(M)]
        return cls({"M": M, "D": D, "a": a, "b": b, "cfg": cfg}, cfg["borne_N"], capacites)

    def perturbe(self, rng):
        cfg = self.p["cfg"]
        a = [int(rng.integers(cfg["alpha_num"][0], cfg["alpha_num"][1] + 1)) for _ in range(self.M)]
        b = [int(rng.integers(cfg["beta_num"][0], cfg["beta_num"][1] + 1)) for _ in range(self.M)]
        return MondeF2({"M": self.M, "D": self.D, "a": a, "b": b, "cfg": cfg}, self.N, self.capacites)

    def _constantes(self):
        return {"M": Fraction(self.M), "OU": Fraction(1), "ET": Fraction(self.M), "MAJ": Fraction(self.M // 2 + 1)}

    def _fonctions(self):
        return {"alpha": 1, "beta": 1, "pfa": 1, "mfa": 1, "prap": 1, "mrap": 1, "fa_ind": 1, "rap_ind": 1,
                "pfa_t": 2, "prap_t": 2}

    def _domaines(self):
        return {"MONITEURS": (1, self.M), "SEUILS": (1, self.M)}

    def definitionnelles(self):
        return {"alpha", "beta"}

    def descriptions(self):
        return {
            "alpha": "alpha(j) : taux de fausses alertes (marge) du moniteur j sous la référence",
            "beta": "beta(j) : taux de détection (marge) du moniteur j sous attaque",
            "pfa": "pfa(s) : pire taux de fausses alertes de la règle « au moins s », maximum sur les couplages",
            "mfa": "mfa(s) : meilleur taux de fausses alertes de la règle « au moins s », minimum sur les couplages",
            "prap": "prap(s) : pire rappel de la règle « au moins s », minimum sur les couplages des marges beta",
            "mrap": "mrap(s) : meilleur rappel de la règle « au moins s », maximum sur les couplages",
            "fa_ind": "fa_ind(s) : fausses alertes de la règle « au moins s » si les moniteurs sont indépendants",
            "rap_ind": "rap_ind(s) : rappel de la règle « au moins s » si les moniteurs sont indépendants",
            "pfa_t": "pfa_t(s, t) = 1 - (1 - pfa(s))^t : au moins une fausse alerte en t tours indépendants",
            "prap_t": "prap_t(s, t) = 1 - (1 - prap(s))^t : au moins une détection en t tours indépendants",
        }

    def parametres_servis(self):
        return {"M": self.M, "alpha": [lit(x) for x in self.alpha], "beta": [lit(x) for x in self.beta]}

    def axiomes(self):
        return [
            "pour tout j dans MONITEURS, alpha(j) >= 0",
            "pour tout j dans MONITEURS, alpha(j) <= 1",
            "pour tout j dans MONITEURS, beta(j) >= 0",
            "pour tout j dans MONITEURS, beta(j) <= 1",
            "pour tout s dans SEUILS, mfa(s) <= pfa(s)",
            "pour tout s dans SEUILS, prap(s) <= mrap(s)",
            "pour tout s dans SEUILS, pfa_t(s, 0) = 0",
            "pour tout s dans SEUILS, prap_t(s, 0) = 0",
        ]

    def _seuil(self, x):
        s = entier_exact(x)
        if not 1 <= s <= self.M:
            raise Indefini("seuil hors de SEUILS")
        return s

    def appeler(self, nom, args):
        if nom in ("alpha", "beta"):
            j = entier_exact(args[0])
            if not 1 <= j <= self.M:
                raise Indefini("moniteur hors de MONITEURS")
            return (self.alpha if nom == "alpha" else self.beta)[j - 1]
        if nom in ("pfa", "mfa"):
            lo, hi = self._ext[("fa", self._seuil(args[0]))]
            return hi if nom == "pfa" else lo
        if nom in ("prap", "mrap"):
            lo, hi = self._ext[("rap", self._seuil(args[0]))]
            return lo if nom == "prap" else hi
        if nom == "fa_ind":
            return independance_au_moins(self.alpha, self._seuil(args[0]))
        if nom == "rap_ind":
            return independance_au_moins(self.beta, self._seuil(args[0]))
        if nom in ("pfa_t", "prap_t"):
            s = self._seuil(args[0])
            t = entier_exact(args[1])
            if t < 0:
                raise Indefini("nombre de tours négatif")
            if t > self.t_max:
                raise HorsCapacite("nombre de tours trop grand")
            base = self._ext[("fa", s)][1] if nom == "pfa_t" else self._ext[("rap", s)][0]
            return 1 - (1 - base) ** t
        raise Indefini(f"fonction inconnue {nom}")

    def _somme_alpha(self):
        return "somme(j, 1, M, alpha(j))"

    def gabarits_verites(self, rng):
        S = self._somme_alpha()
        return [
            # Fréchet, union : le maximum de P(au moins une alerte) sur les couplages est min(1, somme des marges)
            # (borne de l'union, atteinte par des événements disjoints tant que la somme ne dépasse pas 1).
            ("frechet_union_max", [f"pfa(OU) = min(1, {S})"]),
            # Fréchet, union, minimum : les événements emboîtés réalisent max des marges, qui minore toute union.
            ("frechet_union_min", ["(pour tout j dans MONITEURS, alpha(j) <= mfa(OU)) et "
                                   "(il existe j dans MONITEURS, alpha(j) = mfa(OU))"]),
            # Fréchet, intersection, minimum : max(0, somme - (M - 1)) (borne de Bonferroni, atteinte).
            ("frechet_intersection_min", [f"mfa(ET) = max(0, {S} - (M - 1))"]),
            # Emboîtement des règles : {au moins s+1} est inclus dans {au moins s} pour tout couplage, donc le pire
            # cas décroît en s.
            ("pire_cas_decroissant", ["pour tout s dans [1 .. M - 1], pfa(s + 1) <= pfa(s)"]),
            # Markov : P(nombre d'alertes >= s) <= E[nombre]/s = somme des marges / s, pour tout couplage.
            ("markov", [f"pour tout s dans SEUILS, s * pfa(s) <= {S}"]),
            # Espérance : pour tout couplage, la somme sur s de P(au moins s) vaut l'espérance du nombre d'alertes,
            # c'est-à-dire la somme des marges ; le pire cas par s majore donc cette somme.
            ("esperance", [f"somme(s, 1, M, pfa(s)) >= {S}"]),
            # Bernoulli : 1 - (1 - x)^t <= t x pour x dans [0, 1] et t entier naturel.
            ("union_des_tours", ["pour tout t dans NAT, pfa_t(OU, t) <= t * pfa(OU)"]),
            # L'indépendance est un couplage parmi d'autres : elle est entre le meilleur et le pire cas.
            ("independance_encadree", ["pour tout s dans SEUILS, mfa(s) <= fa_ind(s) et fa_ind(s) <= pfa(s)"]),
        ]

    def gabarits_faux_tot(self, rng):
        produit = " * ".join(f"alpha({j})" for j in range(1, self.M + 1))
        return [
            ("intersection_produit", [f"pfa(ET) = {produit}"]),
            ("pire_cas_independant", ["pour tout s dans SEUILS, pfa(s) = fa_ind(s)"]),
            ("tours_additifs", ["pour tout t dans NAT, pfa_t(OU, t) = t * pfa(OU)"]),
            ("intersection_sans_ecart", ["mfa(ET) = pfa(ET)", "prap(OU) = mrap(OU)"]),
        ]

    def gabarits_pieges(self, rng):
        return [
            ("seuil_union_tours", self.piege_seuil(rng, "pfa_t(OU, t)")),
            ("seuil_intersection_tours", self.piege_seuil(rng, "pfa_t(ET, t)") + self.piege_seuil(rng, "pfa_t(MAJ, t)")),
            ("seuil_rappel_tours", self.piege_seuil(rng, "prap_t(OU, t)") + self.piege_seuil(rng, "prap_t(MAJ, t)")),
            ("seuil_independance_tours", self.piege_seuil(rng, "1 - (1 - fa_ind(OU))^t")
             + self.piege_seuil(rng, "1 - (1 - fa_ind(ET))^t")),
        ]

    def temoins_triviaux(self, rng):
        return [
            ("axiome_renomme", ["pour tout k dans MONITEURS, 0 <= alpha(k)"]),
            ("instance_litterale", ["beta(1) <= 1"]),
            ("axiome_renomme_seuils", ["pour tout r dans SEUILS, mfa(r) <= pfa(r)"]),
            ("instance_constante", ["0 = pfa_t(OU, 0)"]),
            ("axiome_renomme_rappel", ["pour tout x dans SEUILS, prap(x) <= mrap(x)"]),
        ]

    def temoins_grossiers(self, rng):
        return [
            ("union_nulle", ["pfa(OU) = 0"]),
            ("marges_au_dessus_de_un", ["pour tout j dans MONITEURS, alpha(j) > 1"]),
            ("tours_certains", ["pour tout t dans NAT, pfa_t(OU, t) = 1"]),
            ("taux_au_dessus_de_un", ["il existe s dans SEUILS, pfa(s) > 1"]),
            ("marges_egales", ["pour tout j dans MONITEURS, beta(j) = alpha(j)"]),
        ]
