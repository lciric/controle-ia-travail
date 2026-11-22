"""Famille F1 — détection finie (miniature de Q4).

Monde : espace d'issues {0, …, K-1} (K tiré entre les bornes des paramètres, de 4 à 8), deux lois rationnelles à support
plein P = a/D et Q = b/D (P ≠ Q). Un test à un pas est un sous-ensemble A (codé par un entier de 0 à PLEIN = 2^K - 1,
bit i ⇔ issue i dans A) ; sur t pas indépendants, le test « A au moins s fois » alerte si l'issue tombe dans A au
moins s fois. Vocabulaire : P(i), Q(i), PA(A), QA(A), comp(A), card(A), bit(A, i), vt(t) (variation totale entre
P⊗t et Q⊗t), fa(A, t, s) (fausses alertes : probabilité sous P⊗t), puissance(A, t, s) (sous Q⊗t).
"""
from __future__ import annotations

import math
from fractions import Fraction

from .exact import HorsCapacite, Indefini, entier_exact
from .mondes import Monde, lit
from .normalisation import p_add, p_atome, p_const, p_scale, p_str, p_val


def composition(rng, total: int, parts: int) -> list[int]:
    """`parts` entiers ≥ 1 de somme `total`, tirés uniformément parmi les compositions (tirage entier seulement)."""
    coupes = sorted(int(x) + 1 for x in rng.choice(total - 1, size=parts - 1, replace=False))
    bornes = [0] + coupes + [total]
    return [bornes[i + 1] - bornes[i] for i in range(parts)]


def _queue_binomiale(p: Fraction, t: int, s: int) -> Fraction:
    if s <= 0:
        return Fraction(1)
    if s > t:
        return Fraction(0)
    q = 1 - p
    return sum((Fraction(math.comb(t, j)) * p ** j * q ** (t - j) for j in range(s, t + 1)), Fraction(0))


class MondeF1(Monde):
    famille = "F1"

    def __init__(self, parametres, borne_N, capacites):
        super().__init__(parametres, borne_N, capacites)
        self.K = int(parametres["K"])
        self.D = int(parametres["D"])
        self.a = [int(x) for x in parametres["a"]]
        self.b = [int(x) for x in parametres["b"]]
        self.PLEIN = (1 << self.K) - 1
        self.t_max = int(capacites["pas_max_f1"])
        self.vt_max = 3 * self.N + 2  # marge de deux pas : les vérités citent vt(t + 1) jusqu'à t = 3N
        self._vt = {0: Fraction(0)}
        self._queues = {}

    @classmethod
    def tirer(cls, rng, cfg, capacites):
        K = int(rng.integers(cfg["taille_espace"][0], cfg["taille_espace"][1] + 1))
        D = int(cfg["denominateurs"][int(rng.integers(0, len(cfg["denominateurs"])))])
        a = composition(rng, D, K)
        b = composition(rng, D, K)
        while b == a:
            b = composition(rng, D, K)
        return cls({"K": K, "D": D, "a": a, "b": b}, cfg["borne_N"], capacites)

    def perturbe(self, rng):
        a = composition(rng, self.D, self.K)
        b = composition(rng, self.D, self.K)
        while b == a:
            b = composition(rng, self.D, self.K)
        return MondeF1({"K": self.K, "D": self.D, "a": a, "b": b}, self.N, self.capacites)

    # -- vocabulaire
    def _constantes(self):
        return {"K": Fraction(self.K), "PLEIN": Fraction(self.PLEIN)}

    def _fonctions(self):
        return {"P": 1, "Q": 1, "PA": 1, "QA": 1, "comp": 1, "card": 1, "bit": 2, "vt": 1, "fa": 3, "puissance": 3}

    def _domaines(self):
        return {"ISSUES": (0, self.K - 1), "PARTIES": (0, self.PLEIN)}

    def definitionnelles(self):
        return {"P", "Q", "PA", "QA", "comp", "card", "bit"}

    def descriptions(self):
        return {
            "P": "P(i) : probabilité de l'issue i sous P (loi de référence, sans attaque)",
            "Q": "Q(i) : probabilité de l'issue i sous Q (loi sous attaque)",
            "PA": "PA(A) : somme des P(i) pour i dans A (A codé par ses bits)",
            "QA": "QA(A) : somme des Q(i) pour i dans A",
            "comp": "comp(A) = PLEIN - A : complémentaire de A",
            "card": "card(A) : nombre d'issues dans A",
            "bit": "bit(A, i) : 1 si l'issue i est dans A, 0 sinon",
            "vt": "vt(t) : distance en variation totale entre P⊗t et Q⊗t (t pas indépendants), 1/2 somme des |écarts|",
            "fa": "fa(A, t, s) : probabilité sous P⊗t que l'issue tombe dans A au moins s fois en t pas",
            "puissance": "puissance(A, t, s) : la même probabilité sous Q⊗t",
        }

    def parametres_servis(self):
        return {"K": self.K, "P": [lit(Fraction(x, self.D)) for x in self.a],
                "Q": [lit(Fraction(x, self.D)) for x in self.b]}

    def axiomes(self):
        return [
            "pour tout A dans PARTIES, PA(A) >= 0",
            "pour tout A dans PARTIES, PA(A) <= 1",
            "pour tout A dans PARTIES, QA(A) >= 0",
            "pour tout A dans PARTIES, QA(A) <= 1",
            "pour tout i dans ISSUES, P(i) >= 0",
            "pour tout i dans ISSUES, Q(i) >= 0",
            "somme_sur(i, ISSUES, P(i)) = 1",
            "somme_sur(i, ISSUES, Q(i)) = 1",
            "PA(PLEIN) = 1",
            "pour tout A dans PARTIES, PA(A) + PA(comp(A)) = 1",
            "vt(0) = 0",
            "pour tout t dans NAT, vt(t) >= 0",
            "pour tout t dans NAT, vt(t) <= 1",
            "pour tout A dans PARTIES, pour tout t dans NAT, fa(A, t, 0) = 1",
            "pour tout A dans PARTIES, pour tout t dans NAT, puissance(A, t, 0) = 1",
        ]

    # -- calcul exact
    def _partie(self, x) -> int:
        A = entier_exact(x)
        if not 0 <= A <= self.PLEIN:
            raise Indefini("partie hors de PARTIES")
        return A

    def _issue(self, x) -> int:
        i = entier_exact(x)
        if not 0 <= i < self.K:
            raise Indefini("issue hors de ISSUES")
        return i

    def _pas(self, x, plafond) -> int:
        t = entier_exact(x)
        if t < 0:
            raise Indefini("nombre de pas négatif")
        if t > plafond:
            raise HorsCapacite(f"nombre de pas au-delà de {plafond}")
        return t

    def PA(self, A) -> Fraction:
        return Fraction(sum(self.a[i] for i in range(self.K) if A >> i & 1), self.D)

    def QA(self, A) -> Fraction:
        return Fraction(sum(self.b[i] for i in range(self.K) if A >> i & 1), self.D)

    def vt(self, t: int) -> Fraction:
        """Variation totale exacte de P⊗t et Q⊗t, par les types (compositions de t en K parts), en entiers."""
        if t in self._vt:
            return self._vt[t]
        K, a, b = self.K, self.a, self.b
        total = 0

        def rec(i, reste, multi, pa, pb):
            nonlocal total
            if i == K - 1:
                c = reste
                total += multi * abs(pa * a[i] ** c - pb * b[i] ** c)
                return
            for c in range(reste + 1):
                rec(i + 1, reste - c, multi * math.comb(reste, c), pa * a[i] ** c, pb * b[i] ** c)

        rec(0, t, 1, 1, 1)
        r = Fraction(total, 2 * self.D ** t)
        self._vt[t] = r
        return r

    def queue(self, p: Fraction, t: int, s: int) -> Fraction:
        cle = (p, t, s)
        if cle not in self._queues:
            self._queues[cle] = _queue_binomiale(p, t, s)
        return self._queues[cle]

    def appeler(self, nom, args):
        if nom == "P":
            return Fraction(self.a[self._issue(args[0])], self.D)
        if nom == "Q":
            return Fraction(self.b[self._issue(args[0])], self.D)
        if nom == "PA":
            return self.PA(self._partie(args[0]))
        if nom == "QA":
            return self.QA(self._partie(args[0]))
        if nom == "comp":
            return Fraction(self.PLEIN - self._partie(args[0]))
        if nom == "card":
            return Fraction(bin(self._partie(args[0])).count("1"))
        if nom == "bit":
            return Fraction(self._partie(args[0]) >> self._issue(args[1]) & 1)
        if nom == "vt":
            return self.vt(self._pas(args[0], self.vt_max))
        if nom in ("fa", "puissance"):
            A = self._partie(args[0])
            t = self._pas(args[1], self.t_max)
            s = entier_exact(args[2])
            p = self.PA(A) if nom == "fa" else self.QA(A)
            return self.queue(p, t, s)
        raise Indefini(f"fonction inconnue {nom}")

    # -- normaliseur : comp(x) = PLEIN - x ; PA(PLEIN - x) = 1 - PA(x) ; QA de même
    def reecrire(self, nom, args, ctx):
        if nom == "comp":
            return p_add(p_const(self.PLEIN), p_scale(args[0], -1))
        if nom in ("PA", "QA"):
            arg = args[0]
            if p_val(arg) == self.PLEIN and len(arg) == 2:
                autre = {m: c for m, c in arg.items() if m != ()}
                (m, c), = autre.items()
                if c == -1 and len(m) == 1 and m[0][1] == 1:
                    x = {m: Fraction(1)}
                    return p_add(p_const(1), p_scale(p_atome(f"{nom}({p_str(x)})"), -1))
        return None

    # -- gabarits (provisoires : la liste est à fixer par le préenregistrement)
    def _partie_interieure(self, rng, loi="P"):
        """Une partie A tirée avec 0 < loi(A) < 1."""
        while True:
            A = int(rng.integers(1, self.PLEIN))
            v = self.PA(A) if loi == "P" else self.QA(A)
            if 0 < v < 1:
                return A

    def gabarits_verites(self, rng):
        # Chaque vérité est vraie pour toutes lois P, Q et tout t, et non seulement jusqu'à N :
        return [
            # Scheffé : pour tout événement A, Q(A) - P(A) <= VT(P, Q), car Q(A) - P(A) = somme sur A des écarts
            # signés, majorée par la somme des écarts positifs, qui vaut VT.
            ("scheffe_majorant", ["pour tout A dans PARTIES, QA(A) - PA(A) <= vt(1)"]),
            # Scheffé, atteinte : l'ensemble {i : Q(i) > P(i)} réalise l'égalité (fini : il existe un maximiseur).
            ("scheffe_atteinte", ["il existe A dans PARTIES, QA(A) - PA(A) = vt(1)"]),
            # Croissance en t : P⊗t est l'image de P⊗(t+1) par oubli d'une coordonnée ; la VT décroît par image
            # (inégalité de traitement des données), d'où vt(t) <= vt(t+1).
            ("vt_croissante", ["pour tout t dans NAT, vt(t) <= vt(t + 1)"]),
            # Sous-additivité : VT(P⊗t, Q⊗t) <= t VT(P, Q) par l'inégalité triangulaire sur les produits hybrides.
            ("vt_sous_additive", ["pour tout t dans NAT, vt(t) <= t * vt(1)"]),
            # Couplage : le couplage maximal coordonnée par coordonnée donne P(X ≠ Y) <= 1 - (1 - VT)^t, d'où
            # 1 - vt(t) >= (1 - vt(1))^t.
            ("couplage_produit", ["pour tout t dans NAT, 1 - vt(t) >= (1 - vt(1))^t"]),
            # Le Cam : tout test est un événement de l'espace à t pas, donc puissance - fausses alertes <= VT à t pas.
            ("le_cam", ["pour tout A dans PARTIES, pour tout t dans NAT, pour tout s dans [0 .. t], "
                        "puissance(A, t, s) - fa(A, t, s) <= vt(t)"]),
            # Une alerte au moins : le complémentaire est « jamais dans A », de probabilité (1 - Q(A))^t (indépendance).
            ("au_moins_une", ["pour tout A dans PARTIES, pour tout t dans NAT, puissance(A, t, 1) = 1 - (1 - QA(A))^t"]),
            # Queue binomiale décroissante en s : {au moins s+1} est inclus dans {au moins s}.
            ("queue_decroissante", ["pour tout A dans PARTIES, pour tout t dans NAT, pour tout s dans [0 .. t], "
                                    "puissance(A, t, s + 1) <= puissance(A, t, s)"]),
        ]

    def gabarits_faux_tot(self, rng):
        return [
            ("vt_additive", ["pour tout t dans NAT, vt(t) = t * vt(1)"]),
            ("scheffe_moitie", ["pour tout A dans PARTIES, QA(A) - PA(A) <= vt(1) / 2"]),
            ("puissance_majoree_un_pas", ["pour tout A dans PARTIES, pour tout t dans NAT, puissance(A, t, 1) <= QA(A)"]),
            ("vt_constante", ["pour tout t dans NAT, vt(t) <= vt(1)", "pour tout t dans NAT, vt(t + 1) = vt(t)"]),
        ]

    def gabarits_pieges(self, rng):
        A0 = self._partie_interieure(rng, "P")
        A1 = self._partie_interieure(rng, "Q")
        A2 = self._partie_interieure(rng, "P")
        return [
            ("seuil_vt", self.piege_seuil(rng, "vt(t)")),
            ("seuil_fausses_alertes", self.piege_seuil(rng, f"fa({A0}, t, 1)") + self.piege_seuil(rng, f"fa({A0}, t, 2)")),
            ("seuil_puissance", self.piege_seuil(rng, f"puissance({A1}, t, 2)")
             + self.piege_seuil(rng, f"puissance({A1}, t, 1)")),
            ("seuil_fausses_alertes_doubles", self.piege_seuil(rng, f"fa({A2}, t, 2)")
             + self.piege_seuil(rng, f"fa({A2}, t, 3)")),
        ]

    def temoins_triviaux(self, rng):
        return [
            ("axiome_renomme", ["pour tout B dans PARTIES, PA(B) >= 0"]),
            ("instance_litterale", ["QA(3) <= 1"]),
            ("complement", ["pour tout X dans PARTIES, PA(X) + PA(comp(X)) = 1"]),
            ("axiome_retourne", ["0 = vt(0)"]),
            ("axiome_retourne_renomme", ["pour tout j dans ISSUES, 0 <= Q(j)"]),
        ]

    def temoins_grossiers(self, rng):
        return [
            ("lois_egales", ["pour tout A dans PARTIES, PA(A) = QA(A)"]),
            ("vt_nulle", ["vt(1) = 0"]),
            ("vt_au_dessus_de_un", ["pour tout t dans NAT, vt(t) > 1"]),
            ("loi_nulle", ["pour tout i dans ISSUES, P(i) = 0"]),
            ("probabilite_au_dessus_de_un", ["il existe A dans PARTIES, PA(A) > 1"]),
        ]
