"""Famille F3 — suites et identités (domaines D1 et D5 de l'essai).

Monde : u(0) = U0, u(1) = U1, u(n+2) = PU u(n+1) + QU u(n) (entiers tirés, PU, QU, U0, U1 >= 1) ; w la solution
fondamentale de la même récurrence (w(0) = 0, w(1) = 1) ; v(0) = V0, v(n+1) = AV v(n) + BV (AV rationnel > 1,
BV entier >= 0). Indice négatif : indéfini ; indice au-delà du plafond : hors capacité.
"""
from __future__ import annotations

import math
from fractions import Fraction

from .exact import HorsCapacite, Indefini, entier_exact, entier_strict, rationnel_strict
from .mondes import Monde, lit
from .normalisation import p_add, p_atome, p_const, p_scale, p_str, p_var_plus_const


def _premiers(jusqua: int) -> list[int]:
    crible = bytearray([1]) * (jusqua + 1)
    crible[0:2] = b"\x00\x00"
    for i in range(2, int(jusqua ** 0.5) + 1):
        if crible[i]:
            crible[i * i::i] = bytearray(len(crible[i * i::i]))
    return [i for i in range(jusqua + 1) if crible[i]]


class MondeF3(Monde):
    famille = "F3"

    def __init__(self, parametres, borne_N, capacites):
        super().__init__(parametres, borne_N, capacites)
        self.PU, self.QU = entier_strict(parametres["PU"], "PU"), entier_strict(parametres["QU"], "QU")
        self.U0, self.U1 = entier_strict(parametres["U0"], "U0"), entier_strict(parametres["U1"], "U1")
        self.AV = rationnel_strict(parametres["AV"], "AV")
        self.BV, self.V0 = entier_strict(parametres["BV"], "BV"), entier_strict(parametres["V0"], "V0")
        self.indice_max = int(capacites["indice_max_facteur_f3"]) * 3 * self.N
        self._u = [self.U0, self.U1]
        self._w = [0, 1]
        self._v = [Fraction(self.V0)]

    @classmethod
    def _tirer_parametres(cls, rng, cfg):
        def ent(cle):
            lo, hi = (entier_strict(x, cle) for x in cfg[cle])
            return int(rng.integers(lo, hi + 1))
        av = cfg["AV_choix"][int(rng.integers(0, len(cfg["AV_choix"])))]
        return {"PU": ent("PU"), "QU": ent("QU"), "U0": ent("U0"), "U1": ent("U1"), "AV": av, "BV": ent("BV"),
                "V0": ent("V0"), "cfg": cfg}

    @classmethod
    def tirer(cls, rng, cfg, capacites):
        return cls(cls._tirer_parametres(rng, cfg), cfg["borne_N"], capacites)

    def perturbe(self, rng):
        return MondeF3(self._tirer_parametres(rng, self.p["cfg"]), self.N, self.capacites)

    def _constantes(self):
        return {"PU": Fraction(self.PU), "QU": Fraction(self.QU), "U0": Fraction(self.U0), "U1": Fraction(self.U1),
                "AV": self.AV, "BV": Fraction(self.BV), "V0": Fraction(self.V0)}

    def _fonctions(self):
        return {"u": 1, "w": 1, "v": 1}

    def _domaines(self):
        return {}

    def definitionnelles(self):
        return {"u", "w", "v"}

    def descriptions(self):
        return {
            "u": "u(0) = U0, u(1) = U1, u(n + 2) = PU * u(n + 1) + QU * u(n)",
            "w": "w(0) = 0, w(1) = 1, w(n + 2) = PU * w(n + 1) + QU * w(n)",
            "v": "v(0) = V0, v(n + 1) = AV * v(n) + BV",
        }

    def parametres_servis(self):
        return {k: lit(x) for k, x in self._constantes().items()}

    def axiomes(self):
        return [
            "u(0) = U0",
            "u(1) = U1",
            "pour tout n dans NAT, u(n + 2) = PU * u(n + 1) + QU * u(n)",
            "w(0) = 0",
            "w(1) = 1",
            "pour tout n dans NAT, w(n + 2) = PU * w(n + 1) + QU * w(n)",
            "v(0) = V0",
            "pour tout n dans NAT, v(n + 1) = AV * v(n) + BV",
        ]

    # -- calcul exact
    def _indice(self, x) -> int:
        n = entier_exact(x)
        if n < 0:
            raise Indefini("indice négatif")
        if n > self.indice_max:
            raise HorsCapacite(f"indice au-delà de {self.indice_max}")
        return n

    def u(self, n):
        while len(self._u) <= n:
            self._u.append(self.PU * self._u[-1] + self.QU * self._u[-2])
        return self._u[n]

    def w(self, n):
        while len(self._w) <= n:
            self._w.append(self.PU * self._w[-1] + self.QU * self._w[-2])
        return self._w[n]

    def v(self, n):
        while len(self._v) <= n:
            self._v.append(self.AV * self._v[-1] + self.BV)
        return self._v[n]

    def appeler(self, nom, args):
        n = self._indice(args[0])
        if nom == "u":
            return Fraction(self.u(n))
        if nom == "w":
            return Fraction(self.w(n))
        if nom == "v":
            return self.v(n)
        raise Indefini(f"fonction inconnue {nom}")

    # -- normaliseur : définitions dépliées sur une variable NAT x : u(x + c) = w(c) u(x + 1) + QU w(c - 1) u(x)
    #    pour c >= 2 (et de même pour w) ; v(x + c) = AV^c v(x) + BV (AV^c - 1) / (AV - 1) pour c >= 1.
    def reecrire(self, nom, args, ctx):
        vc = p_var_plus_const(args[0])
        if vc is None:
            return None
        cle, c = vc
        if not ctx.est_nat(cle) or c > self.indice_max:
            return None
        x = {((cle, 1),): Fraction(1)}
        if nom in ("u", "w") and c >= 2:
            x1 = p_add(x, p_const(1))
            terme1 = p_atome(f"{nom}({p_str(x1)})")
            terme0 = p_atome(f"{nom}({p_str(x)})")
            return p_add(p_scale(terme1, self.w(c)), p_scale(terme0, self.QU * self.w(c - 1)))
        if nom == "v" and c >= 1:
            ac = self.AV ** c
            return p_add(p_scale(p_atome(f"v({p_str(x)})"), ac), p_const(self.BV * (ac - 1) / (self.AV - 1)))
        return None

    # -- gabarits (provisoires)
    def periode(self, M):
        """Période (minimale) de u modulo M ; pure car (u(n), u(n+1)) ↦ (u(n+1), PU u(n+1) + QU u(n)) est inversible
        modulo M quand pgcd(QU, M) = 1."""
        e0 = (self.U0 % M, self.U1 % M)
        a, b = e0
        for T in range(1, M * M + 1):
            a, b = b, (self.PU * b + self.QU * a) % M
            if (a, b) == e0:
                return T
        return None

    def residus_atteints(self, M):
        """Résidus de u modulo M sur une période (pure quand pgcd(QU, M) = 1) : ce sont tous ceux de la suite."""
        T = self.periode(M)
        return None if T is None else {self.u(n) % M for n in range(T)}

    def gabarits_verites(self, rng):
        # v6 (brouillon 3) : indice k tiré par monde dans [2 .. N] (enfant [1])
        k = int(rng.integers(2, self.N + 1))
        C0 = self.U1 ** 2 - self.U0 * self.u(2)
        modules = [M for M in range(3, 13) if math.gcd(self.QU, M) == 1]
        ordre = [modules[int(i)] for i in rng.permutation(len(modules))]
        periodes = [(M, self.periode(M)) for M in ordre]
        periodes = [x for x in periodes if x[1] >= 2] + [x for x in periodes if x[1] < 2]
        # v5 : résidus jamais atteints, sur une période entière, pour des modules premiers à QU
        lo, hi = self.p["cfg"]["module_residu_vrai"]
        cands = [M for M in range(int(lo), int(hi) + 1) if math.gcd(self.QU, M) == 1]
        residus = []
        for k in rng.permutation(len(cands)):
            M = cands[int(k)]
            atteints = self.residus_atteints(M)
            libres = [r for r in range(M) if atteints is not None and r not in atteints]
            if libres:
                r = libres[int(rng.integers(0, len(libres)))]
                residus.append(f"pour tout n dans NAT, mod(u(n), {M}) != {r}")
            if len(residus) >= 4:
                break
        return [
            # v5 (brouillon 2, remarque 7) : 4 vérités de forme seuil, dont 2 à borne naturelle.
            # U0, U1 >= 1 et PU, QU >= 1 : par récurrence, u(n) >= 1 > 0 pour tout n.
            ("u_positive", ["pour tout n dans NAT, u(n) > 0"]),
            # w(1) = 1, w(2) = PU >= 1, et w(n + 2) = PU w(n + 1) + QU w(n) >= w(n + 1) : w(n) >= 1 pour n >= 1.
            ("w_au_moins_un", ["pour tout n dans NAT, n >= 1 implique w(n) >= 1"]),
            # Périodicité pure modulo M (pgcd(QU, M) = 1) : les résidus de u sont ceux d'une période, calculés
            # exactement ; un résidu absent d'une période n'est jamais atteint, pour tout n.
            ("residu_jamais_atteint", residus),
            # F3-d (v6) : v croît, v(n + 1) - v(n) = AV^n ((AV - 1) V0 + BV) > 0 ; v(n) >= v(k) pour n >= k.
            ("v_au_dessus_de_v_k", [f"pour tout n dans NAT, n >= {k} implique v(n) >= {lit(self.v(k))}"]),
            # Cassini généralisé (déterminant de la matrice compagnon multiplié par -QU à chaque pas).
            ("cassini", [f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) = {lit(C0)} * (-QU)^n"]),
            # Addition, par linéarité : u(n + m) = w(m) u(n + 1) + QU w(m - 1) u(n), m >= 1.
            ("addition", ["pour tout n dans NAT, pour tout m dans NAT, m >= 1 implique "
                          "u(n + m) = w(m) * u(n + 1) + QU * w(m - 1) * u(n)"]),
            # Duplication : cas m = n de l'addition appliquée à w.
            ("duplication", ["pour tout n dans NAT, n >= 1 implique w(2 * n) = w(n) * (w(n + 1) + QU * w(n - 1))"]),
            # Périodicité modulaire pure (voir `periode`).
            ("periode_modulaire", [f"pour tout n dans NAT, mod(u(n + {T0}), {M0}) = mod(u(n), {M0})"
                                   for M0, T0 in periodes]),
        ]

    def gabarits_faux_tot(self, rng):
        C0 = self.U1 ** 2 - self.U0 * self.u(2)
        cfg = self.p["cfg"]
        premiers = [p for p in _premiers(cfg["module_residu"][1]) if p >= cfg["module_residu"][0]]
        atteints_tot = []
        for _ in range(int(cfg["essais_residu"])):
            M1 = premiers[int(rng.integers(0, len(premiers)))]
            n0 = int(rng.integers(1, self.N + 1))
            atteints_tot.append(f"pour tout n dans NAT, mod(u(n), {M1}) != {self.u(n0) % M1}")
        return [
            # v5 : 2 faux tôt de forme seuil (dépassement, ou résidu atteint, sous N)
            ("seuil_u_tot", self.seuil_tot(rng, "u(n)", var="n") + self.seuil_tot(rng, "v(n)", var="n")),
            ("residu_atteint_tot", atteints_tot),
            ("cassini_signe", [f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) = {lit(C0)} * QU^n",
                               f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) = {lit(C0 + 1)} * (-QU)^n"]),
            ("addition_decalee", ["pour tout n dans NAT, pour tout m dans NAT, m >= 1 implique "
                                  "u(n + m) = w(m) * u(n + 1) + QU * w(m) * u(n)"]),
        ]

    def gabarits_pieges(self, rng):
        N, N3 = self.N, 3 * self.N
        cfg = self.p["cfg"]
        # résidu jamais atteint jusqu'à N, atteint dans ]N .. 3N]
        candidats_residu = []
        premiers = [p for p in _premiers(cfg["module_residu"][1]) if p >= cfg["module_residu"][0]]
        for _ in range(int(cfg["essais_residu"])):
            M1 = premiers[int(rng.integers(0, len(premiers)))]
            n0 = int(rng.integers(N + 1, N3 + 1))
            r = self.u(n0) % M1
            if all(self.u(n) % M1 != r for n in range(N + 1)):
                candidats_residu.append(f"pour tout n dans NAT, mod(u(n), {M1}) != {r}")
        # premier dont le rang d'apparition dans w est dans ]N .. 3N]
        rangs = []
        for p in _premiers(cfg["premier_apparition_max"]):
            z = next((n for n in range(1, N3 + 1) if self.w(n) % p == 0), None)
            if z is not None and N < z <= N3:
                rangs.append(p)
        candidats_apparition = []
        if rangs:
            M2 = rangs[int(rng.integers(0, len(rangs)))]
            candidats_apparition.append(f"pour tout n dans NAT, n >= 1 implique mod(w(n), {M2}) != 0")
        candidats_apparition += self.piege_seuil(rng, "w(n)", var="n")
        return [
            ("seuil_u", self.piege_seuil(rng, "u(n)", var="n")),
            ("residu_evite", candidats_residu + self.piege_seuil(rng, "u(n) - w(n)", var="n")),
            ("rang_d_apparition", candidats_apparition),
            ("seuil_v", self.piege_seuil(rng, "v(n)", var="n")),
        ]

    def temoins_triviaux(self, rng):
        return [
            ("recurrence_renommee", ["pour tout k dans NAT, u(k + 2) = PU * u(k + 1) + QU * u(k)"]),
            ("recurrence_litterale", ["u(3) = PU * u(2) + QU * u(1)"]),
            ("affine_reordonnee", ["pour tout m dans NAT, v(m + 1) = BV + AV * v(m)"]),
            ("initiale_retournee", ["1 = w(1)"]),
            ("initiale_translatee", ["u(0) + 1 = U0 + 1"]),
        ]

    def temoins_grossiers(self, rng):
        return [
            ("suite_nulle", ["pour tout n dans NAT, u(n) = 0"]),
            ("suite_decroissante", ["pour tout n dans NAT, u(n + 1) < u(n)"]),
            ("terme_nul", ["w(2) = 0"]),
            ("affine_constante", ["pour tout n dans NAT, v(n) = V0 + 1"]),
            ("terme_negatif", ["il existe n dans [0 .. N], u(n) < 0"]),
        ]
