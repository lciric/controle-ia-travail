#!/usr/bin/env python3
"""Programme de vérité des dix-sept témoins imposés — course « seuil et moniteurs » — v1.

Développeur du programme de vérité des témoins imposés, modèle O. Bibliothèque standard seule.

Ce que c'est. Un moteur de loi exacte pour les règles de témoin de la grammaire fermée du § 4.3 du mandat
de l'auteur des mondes plantés v3 (`816313cb…`), la table des dix-sept témoins imposés T01 à T17 (§ 3.1),
et une fonction de recalcul d'un témoin quelconque, loi et règle données (§ 6, point 4).

Exactitude. Partout où la loi le permet, le calcul est fait en rationnels (`fractions.Fraction`) ou en
sommes finies exactes : statistiques d'ordre d'une loi continue (loi bêta, donc queue binomiale exacte),
programmation dynamique exacte sur une suite de Bernoulli, comparaisons de richesse en entiers. Là où la
valeur dépend d'une loi continue que l'auteur choisit (normale, Student, Laplace, lognormale, mélange,
décalage), le calcul passe par des flottants, et il est TOUJOURS encadré : chaque valeur flottante est
rendue avec une borne d'erreur écrite. La borne de discrétisation est rigoureuse (sommes inférieure et
supérieure d'une fonction monotone contre une mesure positive, queues comprises) ; s'y ajoute une
tolérance d'évaluation des fonctions de répartition, DÉCLARÉE et non démontrée
(`TOLERANCE_EVALUATION`).

Lancer :
    python3 -I -B calculer_verite_temoins_imposes_v1.py SORTIE_JSON
    python3 -I -B calculer_verite_temoins_imposes_v1.py --recalculer TEMOINS_JSON SORTIE_JSON

Aucun tirage aléatoire, donc aucune graine. Aucun appel réseau. Le programme refuse d'écraser un
fichier de sortie existant (règle R12).
"""
import json
import math
import sys
from fractions import Fraction

VERSION_SORTIE = "verite-temoins-imposes-seuil-et-moniteurs-v1"
VERSION_ENTREE_RECALCUL = "recalcul-temoins-seuil-et-moniteurs-v1"

ALPHA = Fraction(1, 100)              # « le taux de fausses alertes est d'au plus 1 % » (§ 1, § 2)
SEUIL_ECART = Fraction(1, 1000)       # § 6, point 4 : écart de plus de 0,001 compté et nommé
TOLERANCE_EVALUATION = 1e-12          # déclarée, non démontrée : erreur d'évaluation d'une répartition
DEMI_LARGEUR_CIBLE = 1e-5             # cible de la borne de discrétisation des intégrales encadrées
POINTS_MIN, POINTS_MAX = 2 ** 12, 2 ** 18
DECIMALES = 12

GARANTIES = ("en moyenne", "avec une confiance dite", "a tout instant")
GRANDEURS = ("couverture", "taux_moyen", "fausse_alerte_sur_horizon", "puissance")
POPULATIONS = ("tous_les_honnetes", "honnetes_qui_echouent", "honnetes_qui_reussissent")
PORTEES = ("tous les episodes honnetes de la tranche", "conditionnelle a l'issue")

# D-M16 (a) et § 3.1 du mandat v3 : seuls T05 et T07 se lisent « sans gain ».
IDS_LUS_SANS_GAIN = frozenset({"T05", "T07"})

REGLES = {
    "k_ieme_plus_grand": {"k"},
    "quantile_empirique": {"niveau"},
    "jamais_alerter": set(),
    "toujours_alerter": set(),
    "test_repete_sans_correction": {"taux_nul", "niveau_annonce"},
    "pari_de_bernoulli": {"taux_nul", "taux_parie", "seuil_de_richesse"},
    "seuil_fixe": {"valeur"},
    "plus_grand_de_la_tranche_voisine": set(),
    "moyenne_plus_k_ecarts_types": {"k"},
}
REGLES_SEQUENTIELLES = frozenset({"test_repete_sans_correction", "pari_de_bernoulli"})
REGLES_DE_RANG = frozenset({"k_ieme_plus_grand", "quantile_empirique"})

TYPES_DE_LOI_GRAMMAIRE = frozenset({"normale", "student", "laplace", "lognormale", "melange", "somme_de_pas",
                                    "effet_de_famille_plus_bruit", "arrondi", "decalage", "bernoulli",
                                    "couple", "autre"})
PARAMETRES_DE_LOI = {
    "normale": {"mu", "sigma"},
    "student": {"nu", "mu", "echelle"},
    "laplace": {"mu", "echelle"},
    "lognormale": {"mu", "sigma"},
    "melange": {"poids", "composantes"},
    "somme_de_pas": {"nombre_de_pas", "loi_du_pas", "correlation", "structure"},
    "effet_de_famille_plus_bruit": {"correlation_intra", "tailles_de_famille"},
    "arrondi": {"loi", "pas_de_grille"},
    "decalage": {"loi", "delta_en_ecarts_types"},
}
TYPES_DE_LOI_DU_MOTEUR = frozenset(PARAMETRES_DE_LOI)


class Refus(Exception):
    """Refus explicite (règle R5) : jamais de repli silencieux. `code` nomme la garde."""

    def __init__(self, code, message):
        super().__init__(f"{code} : {message}")
        self.code = code
        self.message = message


# ---------------------------------------------------------------------------------------------------
# Nombres d'entrée : rationnels seulement
# ---------------------------------------------------------------------------------------------------

def rationnel(x, nom):
    """Un nombre d'entrée, rendu en Fraction. Un flottant Python est refusé : il ferait perdre le rang
    juste du quantile (400 × 0,99 vaut 396,00000000000006 en flottant)."""
    if isinstance(x, bool) or not isinstance(x, (int, Fraction)): raise Refus("nombre_non_rationnel", f"{nom} doit être un entier ou un rationnel lu du JSON, non {type(x).__name__}")  # GARDE:nombre_non_rationnel
    return Fraction(x)


def entier(x, nom, minimum):
    if isinstance(x, bool) or not isinstance(x, int): raise Refus("entier_attendu", f"{nom} doit être un entier")  # GARDE:entier_attendu
    if x < minimum: raise Refus("entier_trop_petit", f"{nom} = {x} < {minimum}")  # GARDE:entier_trop_petit
    return x


def probabilite_ouverte(x, nom):
    p = rationnel(x, nom)
    if not 0 < p < 1: raise Refus("probabilite_hors_domaine", f"{nom} = {p} hors de ]0, 1[")  # GARDE:probabilite_hors_domaine
    return p


# ---------------------------------------------------------------------------------------------------
# Encadrement d'une valeur : exacte (lo = hi, rationnel) ou flottante bornée
# ---------------------------------------------------------------------------------------------------

class Encadre:
    __slots__ = ("lo", "hi", "exacte", "mode")

    def __init__(self, lo, hi, exacte=None, mode="flottant_borne"):
        self.lo, self.hi, self.exacte, self.mode = lo, hi, exacte, mode

    @classmethod
    def exact(cls, fr, mode="exact_rationnel"):
        return cls(fr, fr, fr, mode)

    @property
    def valeur(self):
        if self.exacte is not None:
            return self.exacte
        return (float(self.lo) + float(self.hi)) / 2

    @property
    def borne(self):
        if self.exacte is not None:
            return 0.0
        return (float(self.hi) - float(self.lo)) / 2

    def moins(self, autre):
        if self.exacte is not None and autre.exacte is not None:
            return Encadre.exact(self.exacte - autre.exacte)
        return Encadre(float(self.lo) - float(autre.hi), float(self.hi) - float(autre.lo))


def arrondi_decimal(x):
    """Arrondi à DECIMALES décimales, au pair le plus proche, exact pour un rationnel."""
    if x is None:
        return None
    fr = x if isinstance(x, Fraction) else Fraction(x)
    entier_arrondi = round(fr * 10 ** DECIMALES)
    return float(Fraction(entier_arrondi, 10 ** DECIMALES))


def texte_fraction(fr):
    return None if fr is None else f"{fr.numerator}/{fr.denominator}"


def decrire(enc):
    return {"valeur": arrondi_decimal(enc.valeur), "borne_erreur": float(enc.borne), "mode": enc.mode,
            "valeur_exacte": texte_fraction(enc.exacte)}


# ---------------------------------------------------------------------------------------------------
# Lois exactes : statistiques d'ordre, queue binomiale, quantile empirique
# ---------------------------------------------------------------------------------------------------

def queue_binomiale_exacte(n, p, k):
    """P(Bin(n, p) >= k), en rationnels exacts. p est une Fraction de [0, 1]."""
    if k <= 0:
        return Fraction(1)
    if k > n:
        return Fraction(0)
    a, b = p.numerator, p.denominator
    c = b - a
    if k <= n - k + 1:
        dessous = sum(math.comb(n, j) * a ** j * c ** (n - j) for j in range(k))
        return 1 - Fraction(dessous, b ** n)
    dessus = sum(math.comb(n, j) * a ** j * c ** (n - j) for j in range(k, n + 1))
    return Fraction(dessus, b ** n)


def couverture_rang_exacte(n, k, alpha=ALPHA):
    """Loi continue, calibration et lecture sur la même loi : le taux vrai du k-ième plus grand de n
    suit Beta(k, n - k + 1), donc P(taux <= alpha) = P(Bin(n, alpha) >= k)."""
    return queue_binomiale_exacte(n, alpha, k)


def taux_moyen_rang_exact(n, k):
    """Espérance de Beta(k, n - k + 1)."""
    return Fraction(k, n + 1)


def rang_du_quantile_empirique(n, niveau):
    """§ 4.3 : le seuil est le ⌈n × niveau⌉-ième plus petit score, sans interpolation. Rendu comme
    k-ième plus grand : k = n − ⌈n × niveau⌉ + 1. Le plafond est pris en rationnels exacts."""
    niveau = rationnel(niveau, "niveau")
    if not 0 < niveau < 1: raise Refus("niveau_quantile_hors_domaine", f"niveau {niveau} hors de ]0, 1[")  # GARDE:niveau_quantile_hors_domaine
    j = -((-n * niveau.numerator) // niveau.denominator)
    return n - j + 1


# ---------------------------------------------------------------------------------------------------
# Suite de Bernoulli : programmation dynamique exacte (monde S)
# ---------------------------------------------------------------------------------------------------

def seuils_test_repete(taux_nul, niveau, horizon):
    """Pour t = 1..horizon, le plus petit compte k tel que la valeur p, P(Bin(t, taux_nul) >= k)
    (queue droite : un compte au moins égal au compte observé), soit strictement sous le niveau.
    t + 1 si aucun. Comparaisons en entiers exacts."""
    c, d = taux_nul.numerator, taux_nul.denominator
    e = d - c
    seuils = {}
    for t in range(1, horizon + 1):
        borne = niveau.numerator * d ** t
        queue = 0
        k_min = t + 1
        for j in range(t, -1, -1):
            queue += math.comb(t, j) * c ** j * e ** (t - j)
            if queue * niveau.denominator < borne:
                k_min = j
            else:
                break
        seuils[t] = k_min
    return seuils


def predicat_test_repete(taux_nul, niveau, horizon):
    seuils = seuils_test_repete(taux_nul, niveau, horizon)
    return lambda t, k: k >= seuils[t]


def predicat_pari(taux_nul, taux_parie, seuil, horizon):
    """Richesse du pari de Bernoulli : (p1/q)^k ((1-p1)/(1-q))^(t-k). Alerte dès qu'elle atteint ou
    dépasse le seuil. Comparaison en entiers exacts, sans logarithme."""
    r1 = taux_parie / taux_nul
    r0 = (1 - taux_parie) / (1 - taux_nul)
    a1, b1, a0, b0 = r1.numerator, r1.denominator, r0.numerator, r0.denominator
    s_num, s_den = seuil.numerator, seuil.denominator
    p_a1 = [a1 ** i for i in range(horizon + 1)]
    p_b1 = [b1 ** i for i in range(horizon + 1)]
    p_a0 = [a0 ** i for i in range(horizon + 1)]
    p_b0 = [b0 ** i for i in range(horizon + 1)]

    def alerte(t, k):
        return p_a1[k] * p_a0[t - k] * s_den >= s_num * p_b1[k] * p_b0[t - k]
    return alerte


def probabilite_de_sonner(alerte, taux_vrai, horizon):
    """P(la procédure sonne avant la fin de l'horizon), suite de Bernoulli de taux `taux_vrai`.
    Masses entières sur l'échelle taux_vrai.denominator ** t : exact."""
    a, b = taux_vrai.numerator, taux_vrai.denominator
    masses = [1]
    sonne = Fraction(0)
    for t in range(1, horizon + 1):
        suivantes = [0] * (t + 1)
        for k, m in enumerate(masses):
            if m:
                suivantes[k] += m * (b - a)
                suivantes[k + 1] += m * a
        echelle = b ** t
        for k in range(t + 1):
            if suivantes[k] and alerte(t, k):
                sonne += Fraction(suivantes[k], echelle)
                suivantes[k] = 0
        masses = suivantes
    return sonne


# ---------------------------------------------------------------------------------------------------
# Fonctions spéciales en flottants (bornées par TOLERANCE_EVALUATION, déclarée)
# ---------------------------------------------------------------------------------------------------

RACINE_2 = math.sqrt(2.0)


def normale_sf(z):
    return 0.5 * math.erfc(z / RACINE_2)


def normale_cdf(z):
    return 0.5 * math.erfc(-z / RACINE_2)


def _fraction_continue_beta(a, b, x):
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    d = tiny if abs(d) < tiny else d
    d = 1.0 / d
    h = d
    for m in range(1, 20001):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-16:
            return h
    raise RuntimeError("fraction continue de la bêta incomplète non convergée")


def beta_incomplete(a, b, x):
    """I_x(a, b), bêta incomplète régularisée."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    ln_bt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    bt = math.exp(ln_bt)
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _fraction_continue_beta(a, b, x) / a
    return 1.0 - bt * _fraction_continue_beta(b, a, 1.0 - x) / b


def gamma_incomplete_p(a, x):
    """P(a, x), gamma incomplète régularisée inférieure."""
    if x <= 0.0:
        return 0.0
    ln_pre = -x + a * math.log(x) - math.lgamma(a)
    if x < a + 1.0:
        ap, somme = a, 1.0 / a
        terme = somme
        for _ in range(100000):
            ap += 1.0
            terme *= x / ap
            somme += terme
            if abs(terme) < abs(somme) * 1e-17:
                return somme * math.exp(ln_pre)
        raise RuntimeError("série de la gamma incomplète non convergée")
    tiny = 1e-300
    b = x + 1.0 - a
    c = 1.0 / tiny
    d = 1.0 / b
    h = d
    for i in range(1, 100000):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        d = tiny if abs(d) < tiny else d
        c = b + an / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-16:
            return 1.0 - math.exp(ln_pre) * h
    raise RuntimeError("fraction continue de la gamma incomplète non convergée")


def binomiale_cdf_flottante(n, p, kmax):
    """P(Bin(n, p) <= kmax) en flottants."""
    if kmax < 0:
        return 0.0
    if kmax >= n:
        return 1.0
    if p <= 0.0:
        return 1.0
    if p >= 1.0:
        return 0.0
    if kmax <= 40:
        lp, lq = math.log(p), math.log1p(-p)
        base = math.lgamma(n + 1)
        return min(1.0, sum(math.exp(base - math.lgamma(j + 1) - math.lgamma(n - j + 1) + j * lp + (n - j) * lq)
                            for j in range(kmax + 1)))
    return beta_incomplete(n - kmax, kmax + 1.0, 1.0 - p)


def borner_probabilite(x):
    return min(1.0, max(0.0, x))


# ---------------------------------------------------------------------------------------------------
# Lois des scores (§ 4.2 du mandat de l'auteur) : construction gardée
# ---------------------------------------------------------------------------------------------------

def canonique(spec):
    return json.dumps(spec, sort_keys=True, default=str, ensure_ascii=False)


class LoiContinue:
    continue_ = True
    reseau = False
    grappes = False

    def cdf(self, x):
        return 1.0 - self.sf(x)

    def sf_gauche(self, x):
        return self.sf(x)

    def comme_normale(self):
        return None


class Normale(LoiContinue):
    def __init__(self, mu, sigma):
        self.mu, self.sigma = float(mu), float(sigma)

    def sf(self, x):
        return normale_sf((x - self.mu) / self.sigma)

    def cdf(self, x):
        return normale_cdf((x - self.mu) / self.sigma)

    def moyenne(self):
        return self.mu

    def ecart_type(self):
        return self.sigma

    def repere(self):
        return self.mu, self.sigma

    def comme_normale(self):
        return self.mu, self.sigma


class Student(LoiContinue):
    def __init__(self, nu, mu, echelle):
        self.nu, self.mu, self.echelle = float(nu), float(mu), float(echelle)

    def _sf_reduite(self, t):
        if t == 0.0:
            return 0.5
        x = self.nu / (self.nu + t * t)
        demi = 0.5 * beta_incomplete(self.nu / 2.0, 0.5, x)
        return demi if t > 0 else 1.0 - demi

    def sf(self, x):
        return self._sf_reduite((x - self.mu) / self.echelle)

    def cdf(self, x):
        return self._sf_reduite((self.mu - x) / self.echelle)

    def moyenne(self):
        if self.nu <= 1: raise Refus("moyenne_indefinie", "loi de Student de nu <= 1 : moyenne indéfinie")  # GARDE:moyenne_indefinie
        return self.mu

    def ecart_type(self):
        if self.nu <= 2: raise Refus("ecart_type_indefini", "loi de Student de nu <= 2 : écart type indéfini")  # GARDE:ecart_type_indefini
        return self.echelle * math.sqrt(self.nu / (self.nu - 2.0))

    def repere(self):
        return self.mu, self.echelle


class Laplace(LoiContinue):
    def __init__(self, mu, echelle):
        self.mu, self.b = float(mu), float(echelle)

    def sf(self, x):
        z = (x - self.mu) / self.b
        return 0.5 * math.exp(-z) if z >= 0 else 1.0 - 0.5 * math.exp(z)

    def cdf(self, x):
        z = (x - self.mu) / self.b
        return 0.5 * math.exp(z) if z <= 0 else 1.0 - 0.5 * math.exp(-z)

    def moyenne(self):
        return self.mu

    def ecart_type(self):
        return self.b * RACINE_2

    def repere(self):
        return self.mu, self.b


class Lognormale(LoiContinue):
    def __init__(self, mu, sigma):
        self.mu, self.sigma = float(mu), float(sigma)

    def sf(self, x):
        return 1.0 if x <= 0 else normale_sf((math.log(x) - self.mu) / self.sigma)

    def cdf(self, x):
        return 0.0 if x <= 0 else normale_cdf((math.log(x) - self.mu) / self.sigma)

    def moyenne(self):
        return math.exp(self.mu + self.sigma ** 2 / 2)

    def ecart_type(self):
        return math.sqrt(math.expm1(self.sigma ** 2) * math.exp(2 * self.mu + self.sigma ** 2))

    def repere(self):
        m = math.exp(self.mu)
        return m, m * max(self.sigma, 1e-3)


class Decalee:
    """Loi translatée de `d` (unités brutes). Garde la nature (continue ou réseau) de sa base."""

    def __init__(self, base, d):
        self.base, self.d = base, float(d)
        self.continue_, self.reseau, self.grappes = base.continue_, base.reseau, False

    def sf(self, x):
        return self.base.sf(x - self.d)

    def sf_gauche(self, x):
        return self.base.sf_gauche(x - self.d)

    def cdf(self, x):
        return self.base.cdf(x - self.d)

    def moyenne(self):
        return self.base.moyenne() + self.d

    def ecart_type(self):
        return self.base.ecart_type()

    def repere(self):
        c, e = self.base.repere()
        return c + self.d, e

    def comme_normale(self):
        n = self.base.comme_normale()
        return None if n is None else (n[0] + self.d, n[1])

    # loi sur réseau translatée
    def atomes(self):
        return [(x + self.d, m) for x, m in self.base.atomes()]

    @property
    def pas(self):
        return self.base.pas

    @property
    def origine(self):
        return self.base.origine + self.d


class Melange(LoiContinue):
    def __init__(self, poids, composantes):
        self.poids = [float(w) for w in poids]
        self.composantes = composantes

    def sf(self, x):
        return sum(w * c.sf(x) for w, c in zip(self.poids, self.composantes))

    def cdf(self, x):
        return sum(w * c.cdf(x) for w, c in zip(self.poids, self.composantes))

    def moyenne(self):
        return sum(w * c.moyenne() for w, c in zip(self.poids, self.composantes))

    def ecart_type(self):
        m = self.moyenne()
        second = sum(w * (c.ecart_type() ** 2 + c.moyenne() ** 2) for w, c in zip(self.poids, self.composantes))
        return math.sqrt(max(0.0, second - m * m))

    def repere(self):
        reperes = [c.repere() for c in self.composantes]
        centre = sum(w * r[0] for w, r in zip(self.poids, reperes))
        return centre, max(r[1] for r in reperes) + max(abs(r[0] - centre) for r in reperes)


class Arrondie:
    """Loi sur réseau : X = pas × l'entier le plus proche de Y / pas (lecture « au plus proche » du mot
    « arrondi », que la lettre ne fixe pas ; les demi-pas ont une probabilité nulle sous Y continue)."""
    continue_ = False
    reseau = True
    grappes = False

    def __init__(self, base, pas):
        self.base, self.pas_fr, self.pas_f = base, Fraction(pas), float(pas)
        self.origine = 0.0
        lo = _quantile_bas(base, 1e-17)
        hi = _isf_continue(base, 1e-17)[1]
        self.m_lo = math.floor(lo / self.pas_f) - 1
        self.m_hi = math.ceil(hi / self.pas_f) + 1
        if self.m_hi - self.m_lo > 2_000_000: raise Refus("reseau_trop_fin", "plus de deux millions d'atomes : pas trop fin pour le calcul exact par sommes")  # GARDE:reseau_trop_fin

    @property
    def pas(self):
        return self.pas_f

    def atomes(self):
        h = self.pas_f
        res = []
        for m in range(self.m_lo, self.m_hi + 1):
            haut, bas = (m + 0.5) * h, (m - 0.5) * h
            masse = self.base.sf(bas) - self.base.sf(haut) if bas >= 0 else self.base.cdf(haut) - self.base.cdf(bas)
            res.append((m * h, max(0.0, masse)))
        return res

    def _indice_plancher(self, x):
        """⌊x / pas⌋ ; exact pour un seuil rationnel (seuil_fixe), gardé pour un flottant."""
        if isinstance(x, (int, Fraction)):
            return math.floor(Fraction(x) / self.pas_fr), Fraction(x) / self.pas_fr
        r = x / self.pas_f
        _garde_egalite_reseau(r)
        return math.floor(r), None

    def sf(self, x):
        """P(X > x) = P(indice >= ⌊x/pas⌋ + 1)."""
        m, _r = self._indice_plancher(x)
        return self.base.sf((m + 0.5) * self.pas_f)

    def sf_gauche(self, x):
        """P(X >= x) = P(indice >= ⌈x/pas⌉)."""
        m, r = self._indice_plancher(x)
        if r is not None and r == m:
            return self.base.sf((m - 0.5) * self.pas_f)
        return self.base.sf((m + 0.5) * self.pas_f)

    def sf_atome(self, m):
        return self.base.sf((m + 0.5) * self.pas_f)

    def cdf(self, x):
        return 1.0 - self.sf(x)

    def moyenne(self):
        return sum(x * m for x, m in self.atomes())

    def ecart_type(self):
        at = self.atomes()
        mu = sum(x * m for x, m in at)
        return math.sqrt(max(0.0, sum((x - mu) ** 2 * m for x, m in at)))

    def repere(self):
        return self.base.repere()

    def comme_normale(self):
        return None


def _garde_egalite_reseau(r):
    if abs(r - round(r)) < 1e-9: raise Refus("egalite_sur_reseau", "un seuil tombe sur un atome d'une loi sur réseau d'une autre origine : égalité non tranchable en flottants")  # GARDE:egalite_sur_reseau


class Grappes:
    """Score = effet de famille + bruit, variance totale 1, corrélation intra-famille rho. Lecture
    gaussienne des deux composantes : la lettre (« effet de famille de tâches + bruit, variance totale 1 »)
    ne nomme pas leur loi ; c'est celle du programme de la note (bloc E)."""
    continue_ = True
    reseau = False
    grappes = True

    def __init__(self, rho, tailles):
        self.rho = float(rho)
        self.tailles = list(tailles)

    def n_total(self):
        return sum(self.tailles)


def construire_loi(spec):
    if not isinstance(spec, dict) or set(spec) != {"type", "parametres"}: raise Refus("forme_de_loi", "une loi est un objet {\"type\": …, \"parametres\": {…}}")  # GARDE:forme_de_loi
    typ = spec["type"]
    if typ not in TYPES_DE_LOI_GRAMMAIRE: raise Refus("loi_hors_grammaire", f"type de loi « {typ} » hors de la liste fermée du § 4.2")  # GARDE:loi_hors_grammaire
    if typ not in TYPES_DE_LOI_DU_MOTEUR: raise Refus("loi_hors_moteur", f"type « {typ} » dans la grammaire mais sans vérité exacte dans ce moteur")  # GARDE:loi_hors_moteur
    p = spec["parametres"]
    if not isinstance(p, dict) or set(p) != PARAMETRES_DE_LOI[typ]: raise Refus("parametres_de_loi", f"paramètres de « {typ} » attendus : {sorted(PARAMETRES_DE_LOI[typ])}")  # GARDE:parametres_de_loi
    return _CONSTRUCTEURS[typ](p)


def _positif(x, nom):
    v = rationnel(x, nom)
    if v <= 0: raise Refus("parametre_non_positif", f"{nom} = {v} doit être strictement positif")  # GARDE:parametre_non_positif
    return v


def _loi_normale(p):
    return Normale(rationnel(p["mu"], "mu"), _positif(p["sigma"], "sigma"))


def _loi_student(p):
    return Student(_positif(p["nu"], "nu"), rationnel(p["mu"], "mu"), _positif(p["echelle"], "echelle"))


def _loi_laplace(p):
    return Laplace(rationnel(p["mu"], "mu"), _positif(p["echelle"], "echelle"))


def _loi_lognormale(p):
    return Lognormale(rationnel(p["mu"], "mu"), _positif(p["sigma"], "sigma"))


def _loi_melange(p):
    poids, comps = p["poids"], p["composantes"]
    if not isinstance(poids, list) or not isinstance(comps, list) or len(poids) != len(comps) or len(poids) < 1: raise Refus("melange_longueurs", "poids et composantes : deux listes de même longueur, non vides")  # GARDE:melange_longueurs
    ws = [_positif(w, "poids") for w in poids]
    if sum(ws) != 1: raise Refus("melange_somme_des_poids", f"la somme des poids vaut {sum(ws)}, non 1")  # GARDE:melange_somme_des_poids
    lois = [construire_loi(c) for c in comps]
    if not all(l.continue_ and not l.grappes for l in lois): raise Refus("melange_non_continu", "mélange de composantes sur réseau ou en grappes : hors du moteur")  # GARDE:melange_non_continu
    return Melange(ws, lois)


def _loi_somme_de_pas(p):
    nb = entier(p["nombre_de_pas"], "nombre_de_pas", 1)
    pas = construire_loi(p["loi_du_pas"])
    norm = pas.comme_normale() if not pas.grappes else None
    if norm is None: raise Refus("somme_de_pas_non_normale", "somme de pas : seule une loi du pas normale a une vérité exacte ici")  # GARDE:somme_de_pas_non_normale
    r = float(rationnel(p["correlation"], "correlation"))
    structure = p["structure"]
    if structure not in ("ar1", "equicorrelee"): raise Refus("structure_inconnue", f"structure « {structure} » hors de ar1 et equicorrelee")  # GARDE:structure_inconnue
    if structure == "ar1":
        if not -1 < r < 1: raise Refus("correlation_hors_domaine", f"corrélation ar1 {r} hors de ]-1, 1[")  # GARDE:correlation_hors_domaine
        variance = nb + 2 * sum((nb - d) * r ** d for d in range(1, nb))
    else:
        variance = nb + nb * (nb - 1) * r
        if variance <= 0 or r >= 1: raise Refus("equicorrelation_hors_domaine", f"corrélation {r} : matrice non définie positive")  # GARDE:equicorrelation_hors_domaine
    mu, sigma = norm
    return Normale(nb * mu, sigma * math.sqrt(variance))


def _loi_grappes(p):
    rho = rationnel(p["correlation_intra"], "correlation_intra")
    if not 0 <= rho < 1: raise Refus("correlation_intra_hors_domaine", f"corrélation intra-famille {rho} hors de [0, 1[")  # GARDE:correlation_intra_hors_domaine
    tailles = p["tailles_de_famille"]
    if not isinstance(tailles, list) or not tailles: raise Refus("tailles_de_famille", "tailles_de_famille : liste non vide d'entiers")  # GARDE:tailles_de_famille
    return Grappes(rho, [entier(m, "taille de famille", 1) for m in tailles])


def _loi_arrondi(p):
    base = construire_loi(p["loi"])
    if not base.continue_ or base.grappes: raise Refus("arrondi_non_continu", "arrondi d'une loi qui n'est pas continue : hors du moteur")  # GARDE:arrondi_non_continu
    return Arrondie(base, _positif(p["pas_de_grille"], "pas_de_grille"))


def _loi_decalage(p):
    base = construire_loi(p["loi"])
    if base.grappes: raise Refus("decalage_de_grappes", "décalage d'une loi en grappes : hors du moteur")  # GARDE:decalage_de_grappes
    delta = rationnel(p["delta_en_ecarts_types"], "delta_en_ecarts_types")
    return Decalee(base, float(delta) * base.ecart_type())


_CONSTRUCTEURS = {"normale": _loi_normale, "student": _loi_student, "laplace": _loi_laplace,
                  "lognormale": _loi_lognormale, "melange": _loi_melange, "somme_de_pas": _loi_somme_de_pas,
                  "effet_de_famille_plus_bruit": _loi_grappes, "arrondi": _loi_arrondi,
                  "decalage": _loi_decalage}


# ---------------------------------------------------------------------------------------------------
# Quantiles par dichotomie (flottants)
# ---------------------------------------------------------------------------------------------------

def _isf_continue(loi, p):
    """(x_bas, x_haut) avec sf(x_bas) > p >= sf(x_haut) et x_haut − x_bas au plus deux flottants voisins."""
    c, e = loi.repere()
    e = e if e > 0 else 1.0
    lo, hi = c - e, c + e
    for _ in range(4000):
        if loi.sf(hi) <= p:
            break
        hi = c + 2.0 * (hi - c)
    else:
        raise RuntimeError("quantile introuvable (haut)")
    for _ in range(4000):
        if loi.sf(lo) > p:
            break
        lo = c - 2.0 * (c - lo)
    else:
        raise RuntimeError("quantile introuvable (bas)")
    for _ in range(400):
        mi = (lo + hi) / 2.0
        if mi <= lo or mi >= hi:
            break
        if loi.sf(mi) > p:
            lo = mi
        else:
            hi = mi
    return lo, hi


def _quantile_bas(loi, p):
    """x tel que cdf(x) <= p environ (repère de grille seulement)."""
    c, e = loi.repere()
    e = e if e > 0 else 1.0
    lo, hi = c - e, c + e
    for _ in range(4000):
        if loi.cdf(lo) <= p:
            break
        lo = c - 2.0 * (c - lo)
    for _ in range(4000):
        if loi.cdf(hi) > p:
            break
        hi = c + 2.0 * (hi - c)
    for _ in range(400):
        mi = (lo + hi) / 2.0
        if mi <= lo or mi >= hi:
            break
        if loi.cdf(mi) <= p:
            lo = mi
        else:
            hi = mi
    return lo


def quantile_de_lecture(loi, alpha=ALPHA):
    """g* = inf{x : P(X > x) <= alpha} pour la loi de lecture. Continue : encadrement (bas, haut).
    Réseau : l'atome exact (bas = haut)."""
    a = float(alpha)
    if loi.reseau:
        for x, _m in loi.atomes():
            s = _sf_reseau_en_atome(loi, x)
            if abs(s - a) <= TOLERANCE_EVALUATION: raise Refus("taux_egal_a_alpha_sur_reseau", "un atome de la loi de lecture a un taux égal à alpha à la tolérance près")  # GARDE:taux_egal_a_alpha_sur_reseau
            if s <= a:
                return x, x
        raise RuntimeError("aucun atome sous alpha")
    return _isf_continue(loi, a)


def _arrondie_de(loi):
    while isinstance(loi, Decalee):
        loi = loi.base
    return loi


def _sf_reseau_en_atome(loi, x):
    """P(X > x) pour x atome de la même loi sur réseau (par indice, sans flottant ambigu)."""
    m = round((x - loi.origine) / loi.pas)
    arrondie = _arrondie_de(loi)
    return arrondie.base.sf((m + 0.5) * arrondie.pas_f)


def _meme_reseau(a, b):
    return a.reseau and b.reseau and a.pas == b.pas and a.origine == b.origine


def sf_en(loi, x, loi_de_x=None):
    """P(X > x), X de loi `loi`, x valeur prise par une loi `loi_de_x` (pour un atome d'un même réseau)."""
    if loi.reseau and loi_de_x is not None and _meme_reseau(loi, loi_de_x):
        return _sf_reseau_en_atome(loi, x)
    return loi.sf(x)


def sf_gauche_en(loi, x, loi_de_x=None):
    """P(X >= x)."""
    if loi.reseau and loi_de_x is not None and _meme_reseau(loi, loi_de_x):
        return _sf_reseau_en_atome(loi, x - loi.pas)
    return loi.sf_gauche(x)


# ---------------------------------------------------------------------------------------------------
# Règles de rang : couverture, taux moyen, puissance (exacts si la loi le permet, sinon encadrés)
# ---------------------------------------------------------------------------------------------------

def couverture_rang(n, k, calib, lecture, meme_loi):
    """P(taux vrai du k-ième plus grand de n <= alpha), taux lu sur `lecture`.
    taux <= alpha  <=>  s >= g*  <=>  au moins k des n scores >= g*  : P(Bin(n, π) >= k), π = P_calib(X >= g*)."""
    if meme_loi and calib.continue_:
        return Encadre.exact(couverture_rang_exacte(n, k))
    g_bas, g_haut = quantile_de_lecture(lecture)
    pi_lo = sf_gauche_en(calib, g_haut, lecture)
    pi_hi = sf_gauche_en(calib, g_bas, lecture)
    pi_lo = borner_probabilite(pi_lo - TOLERANCE_EVALUATION)
    pi_hi = borner_probabilite(pi_hi + TOLERANCE_EVALUATION)
    lo = queue_binomiale_exacte(n, Fraction(pi_lo), k)
    hi = queue_binomiale_exacte(n, Fraction(pi_hi), k)
    return Encadre(float(lo), float(hi))


def _grille(lois, centre_loi):
    """Grille en x uniforme dans asinh((x − c)/e) couvrant les quantiles 1e-15 des lois données."""
    xs_bas = [_quantile_bas(l, 1e-15) for l in lois]
    xs_haut = [_isf_continue(l, 1e-15)[1] for l in lois]
    x_min, x_max = min(xs_bas), max(xs_haut)
    lo_q, hi_q = _isf_continue(centre_loi, 0.75)[1], _isf_continue(centre_loi, 0.25)[1]
    c = _isf_continue(centre_loi, 0.5)[1]
    e = max((hi_q - lo_q) / 1.349, 1e-12)
    return c, e, math.asinh((x_min - c) / e), math.asinh((x_max - c) / e)


def esperance_sf_rang_continue(n, k, calib, cible, plancher=None):
    """E[ P_cible(X > s) ] (ou E[ P_cible(X > s) 1{s >= plancher} ]), s le k-ième plus grand de n scores
    de `calib`, les deux lois continues. Écriture : E = ∫ ψ(x) dP_cible(x), ψ(x) = P(s < x) [− P(s < plancher)]₊,
    croissante. Encadrement rigoureux par sommes inférieure et supérieure sur une grille, queues comprises."""
    def phi(x):
        return binomiale_cdf_flottante(n, borner_probabilite(calib.sf(x)), k - 1)
    phi_c = phi(plancher) if plancher is not None else 0.0
    psi_inf = 1.0 - phi_c

    def psi(x):
        return max(0.0, phi(x) - phi_c)
    c, e, y_lo, y_hi = _grille([calib, cible], cible)
    points = POINTS_MIN
    while True:
        dy = (y_hi - y_lo) / points
        xs = [c + e * math.sinh(y_lo + i * dy) for i in range(points + 1)]
        sfs = [cible.sf(x) for x in xs]
        ps = [psi(x) for x in xs]
        lo = (1.0 - sfs[0]) * 0.0 + sfs[-1] * ps[-1]
        hi = (1.0 - sfs[0]) * ps[0] + sfs[-1] * psi_inf
        for i in range(points):
            m = max(0.0, sfs[i] - sfs[i + 1])
            lo += m * ps[i]
            hi += m * ps[i + 1]
        if (hi - lo) / 2 <= DEMI_LARGEUR_CIBLE or points >= POINTS_MAX:
            break
        points *= 2
    return lo - TOLERANCE_EVALUATION, hi + TOLERANCE_EVALUATION


def esperance_sf_rang_reseau(n, k, calib, cible, lecture_pour_condition=None):
    """Même espérance quand la calibration est sur réseau : s ne prend que les atomes de `calib`.
    P(s <= a) = P(Bin(n, P_calib(X > a)) <= k − 1). Somme finie ; masse tronquée ajoutée à la borne.
    Avec `lecture_pour_condition` : E[ P_cible(X > s) 1{P_lecture(X > s) <= alpha} ] et sa probabilité."""
    atomes = calib.atomes()
    total = sum(m for _x, m in atomes)
    tronque = max(0.0, 1.0 - total)
    precedent = 0.0
    esperance = 0.0
    proba_condition = 0.0
    for x, _m in atomes:
        sf_calib = _sf_reseau_en_atome(calib, x)
        cumul = binomiale_cdf_flottante(n, borner_probabilite(sf_calib), k - 1)
        masse_s = max(0.0, cumul - precedent)
        precedent = cumul
        if lecture_pour_condition is not None:
            if sf_en(lecture_pour_condition, x, calib) > float(ALPHA):
                continue
            proba_condition += masse_s
        esperance += masse_s * sf_en(cible, x, calib)
    borne = n * tronque + TOLERANCE_EVALUATION
    return esperance - borne, esperance + borne, proba_condition


def taux_moyen_rang(n, k, calib, lecture, meme_loi):
    if meme_loi and calib.continue_:
        return Encadre.exact(taux_moyen_rang_exact(n, k))
    return esperance_rang(n, k, calib, lecture)


def esperance_sf_rang_cible_reseau(n, k, calib, cible, plancher=None):
    """Calibration continue, loi cible sur réseau : E = Σ_a P_cible(X = a) ψ(a), ψ(a) = P(s < a)
    [− P(s < plancher)]₊, somme finie sur les atomes ; masse tronquée ajoutée à la borne."""
    def phi(x):
        return binomiale_cdf_flottante(n, borner_probabilite(calib.sf(x)), k - 1)
    phi_c = phi(plancher) if plancher is not None else 0.0
    atomes = cible.atomes()
    tronque = max(0.0, 1.0 - sum(m for _x, m in atomes))
    e = sum(m * max(0.0, phi(x) - phi_c) for x, m in atomes)
    return e - TOLERANCE_EVALUATION, e + tronque + TOLERANCE_EVALUATION


def _esperance_calibration_continue(n, k, calib, cible, plancher=None):
    if cible.reseau:
        return esperance_sf_rang_cible_reseau(n, k, calib, cible, plancher)
    return esperance_sf_rang_continue(n, k, calib, cible, plancher)


def esperance_rang(n, k, calib, cible):
    if calib.reseau:
        lo, hi, _p = esperance_sf_rang_reseau(n, k, calib, cible)
    else:
        lo, hi = _esperance_calibration_continue(n, k, calib, cible)
    return Encadre(borner_probabilite(lo), borner_probabilite(hi))


def puissance_rang_sachant(n, k, calib, lecture, saboteur):
    """E[ puissance | taux vrai <= alpha ] : moyenne de la puissance sur les seuls tirages où la règle
    tient son taux (définition V3 de la conception v6, § 7), comme quotient de deux espérances."""
    if calib.reseau:
        lo, hi, p = esperance_sf_rang_reseau(n, k, calib, saboteur, lecture_pour_condition=lecture)
        if p <= 0:
            return None
        return Encadre(borner_probabilite(lo / p), borner_probabilite(hi / p))
    g_bas, g_haut = quantile_de_lecture(lecture)
    cov = couverture_rang(n, k, calib, lecture, False)
    if cov.hi <= 0:
        return None
    lo, hi = _esperance_calibration_continue(n, k, calib, saboteur, plancher=g_haut)
    return Encadre(borner_probabilite(lo / float(cov.hi)), borner_probabilite(hi / max(float(cov.lo), 1e-300)))


# ---------------------------------------------------------------------------------------------------
# Règle « moyenne plus k écarts types » (loi normale seulement)
# ---------------------------------------------------------------------------------------------------

def _encadrer_sur_khi2(n, h):
    """∫ h(q) dχ²_{n−1}(q) pour h monotone à valeurs dans [0, 1] : encadrement par cellules."""
    a = (n - 1) / 2.0
    moyenne = n - 1.0
    ecart = math.sqrt(2.0 * (n - 1))
    q_lo = max(0.0, moyenne - 60.0 * ecart - 50.0)
    q_hi = moyenne + 60.0 * ecart + 200.0
    points = POINTS_MIN
    while True:
        dq = (q_hi - q_lo) / points
        qs = [q_lo + i * dq for i in range(points + 1)]
        cdfs = [gamma_incomplete_p(a, q / 2.0) for q in qs]
        hs = [h(q) for q in qs]
        queue_basse, queue_haute = cdfs[0], 1.0 - cdfs[-1]
        lo, hi = 0.0, queue_basse + queue_haute
        for i in range(points):
            m = max(0.0, cdfs[i + 1] - cdfs[i])
            lo += m * min(hs[i], hs[i + 1])
            hi += m * max(hs[i], hs[i + 1])
        if (hi - lo) / 2 <= DEMI_LARGEUR_CIBLE or points >= POINTS_MAX:
            break
        points *= 2
    return Encadre(borner_probabilite(lo - TOLERANCE_EVALUATION), borner_probabilite(hi + TOLERANCE_EVALUATION))


def regle_moyenne_k(n, k, calib, lecture, saboteurs, convention):
    """Seuil T = moyenne + k × écart type de l'échantillon (convention n − 1 ou n). Calibration normale
    N(μ0, σ0) : T = μ0 + σ0 (Z̄ + k S), Z̄ ~ N(0, 1/n), S² = Q / ν, Q ~ χ²_{n−1}, indépendants.
    Couverture = E_Q[ P(Z̄ >= c − k S) ], c = (g* − μ0)/σ0. Taux moyen sur N(μ1, σ1) :
    E_Q[ Φ̄((μ0 + σ0 k S − μ1) / sqrt(σ1² + σ0²/n)) ] (loi conditionnelle de T sachant S)."""
    n0, n1 = calib.comme_normale(), lecture.comme_normale()
    if n0 is None or n1 is None: raise Refus("moyenne_k_loi_non_normale", "« moyenne plus k écarts types » : vérité exacte ici pour des lois normales seulement")  # GARDE:moyenne_k_loi_non_normale
    mu0, s0 = n0
    mu1, s1 = n1
    nu = (n - 1) if convention == "n_moins_1" else n
    k = float(k)
    racine_n = math.sqrt(n)
    g_bas, g_haut = quantile_de_lecture(lecture)

    def cov_h(g):
        cc = (g - mu0) / s0
        return lambda q: normale_sf(racine_n * (cc - k * math.sqrt(q / nu)))
    cov_hi = _encadrer_sur_khi2(n, cov_h(g_bas))
    cov_lo = _encadrer_sur_khi2(n, cov_h(g_haut))
    couverture = Encadre(cov_lo.lo, cov_hi.hi)

    def taux_h(mu_c, s_c):
        den = math.sqrt(s_c ** 2 + s0 ** 2 / n)
        return lambda q: normale_sf((mu0 + s0 * k * math.sqrt(q / nu) - mu_c) / den)
    taux = _encadrer_sur_khi2(n, taux_h(mu1, s1))
    puissances = {}
    for nom, sab in saboteurs.items():
        ns = sab.comme_normale()
        if ns is None: raise Refus("moyenne_k_saboteur_non_normal", f"saboteur « {nom} » non normal pour « moyenne plus k écarts types »")  # GARDE:moyenne_k_saboteur_non_normal
        puissances[nom] = _encadrer_sur_khi2(n, taux_h(ns[0], ns[1]))
    return couverture, taux, puissances


# ---------------------------------------------------------------------------------------------------
# Grappes (famille H) : couverture du plus grand score, familles neuves à l'usage
# ---------------------------------------------------------------------------------------------------

def couverture_grappes(grappes, lecture):
    """P(max >= g*) = 1 − Π_f E_U[ Φ((g* − √ρ U)/√(1−ρ))^{m_f} ], U ~ N(0, 1) l'effet de famille.
    Intégrande décroissante en U : encadrement par cellules gaussiennes, queues comprises."""
    g_bas, g_haut = quantile_de_lecture(lecture)
    rho = grappes.rho
    a, b = math.sqrt(rho), math.sqrt(1.0 - rho)

    def facteur(m, g):
        if rho == 0.0:
            v = normale_cdf(g) ** m
            return v, v
        points = POINTS_MIN
        u_lo, u_hi = -12.0, 12.0
        while True:
            du = (u_hi - u_lo) / points
            us = [u_lo + i * du for i in range(points + 1)]
            cdfs = [normale_cdf(u) for u in us]
            hs = [normale_cdf((g - a * u) / b) ** m for u in us]
            lo = (1.0 - cdfs[-1]) * 0.0
            hi = cdfs[0] * 1.0 + (1.0 - cdfs[-1]) * hs[-1]
            lo += cdfs[0] * hs[0]
            for i in range(points):
                masse = max(0.0, cdfs[i + 1] - cdfs[i])
                lo += masse * hs[i + 1]
                hi += masse * hs[i]
            if (hi - lo) / 2 <= DEMI_LARGEUR_CIBLE / 50 or points >= POINTS_MAX:
                return lo, hi
            points *= 2
    produit_lo, produit_hi = 1.0, 1.0
    for m in sorted(set(grappes.tailles)):
        nb = grappes.tailles.count(m)
        f_lo, _ = facteur(m, g_bas)
        _, f_hi = facteur(m, g_haut)
        produit_lo *= max(0.0, f_lo - TOLERANCE_EVALUATION) ** nb
        produit_hi *= min(1.0, f_hi + TOLERANCE_EVALUATION) ** nb
    return Encadre(borner_probabilite(1.0 - produit_hi), borner_probabilite(1.0 - produit_lo))


# ---------------------------------------------------------------------------------------------------
# Analyse d'une règle de témoin (§ 4.3)
# ---------------------------------------------------------------------------------------------------

def analyser_regle(regle):
    if not isinstance(regle, dict) or "type" not in regle: raise Refus("forme_de_regle", "une règle est un objet {\"type\": …}")  # GARDE:forme_de_regle
    typ = regle["type"]
    if typ not in REGLES: raise Refus("regle_hors_grammaire", f"type de règle « {typ} » hors de la grammaire fermée du § 4.3")  # GARDE:regle_hors_grammaire
    if set(regle) - {"type"} != REGLES[typ]: raise Refus("parametres_de_regle", f"paramètres de « {typ} » attendus : {sorted(REGLES[typ])}")  # GARDE:parametres_de_regle
    return typ, {cle: v for cle, v in regle.items() if cle != "type"}


def k_de_la_regle(typ, params, n):
    if typ == "k_ieme_plus_grand":
        k = entier(params["k"], "k", 1)
        if k > n: raise Refus("k_superieur_a_n", f"k = {k} > n = {n}")  # GARDE:k_superieur_a_n
        return k
    if typ == "quantile_empirique":
        return rang_du_quantile_empirique(n, params["niveau"])
    if typ == "plus_grand_de_la_tranche_voisine":
        return 1
    return None


# ---------------------------------------------------------------------------------------------------
# Recalcul d'un témoin quelconque (§ 6, point 4)
# ---------------------------------------------------------------------------------------------------

CLES_OBLIGATOIRES = {"id", "n", "regle", "garantie", "risque_ou_niveau", "grandeur",
                     "population_de_calibration", "portee_de_la_garantie", "lois"}
CLES_FACULTATIVES = {"suite", "valeur_annoncee", "issue_annoncee", "tailles_de_plus"}
CLES_DE_LOIS = {"calibration", "lecture", "saboteurs", "voisine"}
CLES_DE_SUITE = {"taux_honnete", "horizon", "taux_saboteur", "taux_honnete_derive"}


def tenue_de_la_garantie(garantie, quantite, risque):
    """'tient', 'violee' ou 'indecise' (encadrement à cheval sur la coupure)."""
    if garantie == "en moyenne":
        coupure, bon_si_petit = ALPHA, True
    elif garantie == "avec une confiance dite":
        coupure, bon_si_petit = 1 - risque, False
    else:
        coupure, bon_si_petit = risque, True
    if quantite.exacte is not None:
        q = quantite.exacte
        ok = q <= coupure if bon_si_petit else q >= coupure
        return "tient" if ok else "violee"
    lo, hi, cf = float(quantite.lo), float(quantite.hi), float(coupure)
    if bon_si_petit:
        return "tient" if hi <= cf else ("violee" if lo > cf else "indecise")
    return "tient" if lo >= cf else ("violee" if hi < cf else "indecise")


def issue_du_temoin(identifiant, tenue, ecarts_a_la_base):
    """D-M16 (a), § 3.1 du mandat v3 : T05 et T07 seuls lus « sans gain » ; tous les autres sur la seule
    garantie dite. `ecarts_a_la_base` : encadrements de l'écart de puissance, un par taille de signal."""
    if tenue == "indecise":
        return "indecise_a_la_borne"
    if tenue == "violee":
        return "morte_invalide"
    if identifiant in IDS_LUS_SANS_GAIN:
        if not ecarts_a_la_base: raise Refus("saboteurs_requis_sans_gain", f"{identifiant} se lit « sans gain » : saboteurs requis")  # GARDE:saboteurs_requis_sans_gain
        if all(float(e.hi) <= 0 for e in ecarts_a_la_base):
            return "morte_sans_gain"
        if any(float(e.lo) > 0 for e in ecarts_a_la_base) and all(float(e.lo) > 0 or float(e.hi) <= 0 for e in ecarts_a_la_base):
            return "tient"
        return "indecise_a_la_borne"
    return "tient"


def _risque(garantie, valeur):
    if garantie == "en moyenne":
        if valeur is not None: raise Refus("risque_inattendu", "garantie « en moyenne » : risque_ou_niveau doit être null")  # GARDE:risque_inattendu
        return None
    if valeur is None: raise Refus("risque_absent", f"garantie « {garantie} » : risque_ou_niveau requis")  # GARDE:risque_absent
    return probabilite_ouverte(valeur, "risque_ou_niveau")


def recalculer_temoin(t):
    """Recalcule la valeur vraie d'un témoin, loi et règle données. Lève Refus sur toute entrée hors
    grammaire, taille absente ou paramètre hors domaine."""
    if not isinstance(t, dict): raise Refus("forme_du_temoin", "un témoin est un objet")  # GARDE:forme_du_temoin
    cles = set(t)
    if not CLES_OBLIGATOIRES <= cles or cles - CLES_OBLIGATOIRES - CLES_FACULTATIVES: raise Refus("cles_du_temoin", f"clés manquantes {sorted(CLES_OBLIGATOIRES - cles)} ou en trop {sorted(cles - CLES_OBLIGATOIRES - CLES_FACULTATIVES)}")  # GARDE:cles_du_temoin
    garantie, grandeur = t["garantie"], t["grandeur"]
    if garantie not in GARANTIES: raise Refus("garantie_hors_liste", f"garantie « {garantie} » hors de la liste fermée")  # GARDE:garantie_hors_liste
    if grandeur not in GRANDEURS: raise Refus("grandeur_hors_liste", f"grandeur « {grandeur} » hors de la liste fermée")  # GARDE:grandeur_hors_liste
    if t["population_de_calibration"] not in POPULATIONS or t["portee_de_la_garantie"] not in PORTEES: raise Refus("champ_ferme_population", "population_de_calibration ou portee_de_la_garantie hors de leur liste fermée")  # GARDE:champ_ferme_population
    typ, params = analyser_regle(t["regle"])
    risque = _risque(garantie, t["risque_ou_niveau"])
    lois = t["lois"]
    if not isinstance(lois, dict) or set(lois) - CLES_DE_LOIS: raise Refus("cles_de_lois", f"clés de lois admises : {sorted(CLES_DE_LOIS)}")  # GARDE:cles_de_lois
    resultat = {"id": t["id"], "regle": t["regle"], "garantie": garantie, "grandeur": grandeur,
                "risque_ou_niveau": None if risque is None else arrondi_decimal(risque),
                "population_de_calibration": t["population_de_calibration"],
                "portee_de_la_garantie": t["portee_de_la_garantie"]}
    if garantie == "a tout instant":
        quantites, grandeur_valeur, ecarts = _recalcul_sequentiel(t, typ, params)
    else:
        if typ in REGLES_SEQUENTIELLES: raise Refus("garantie_incoherente", f"règle séquentielle « {typ} » sous une garantie « {garantie} »")  # GARDE:garantie_incoherente
        quantites, grandeur_valeur, ecarts = _recalcul_a_seuil(t, typ, params, lois, grandeur)
    quantite_garantie = quantites["fausse_alerte_sur_horizon" if garantie == "a tout instant" else
                                  ("taux_moyen" if garantie == "en moyenne" else "couverture")]
    tenue = tenue_de_la_garantie(garantie, quantite_garantie, risque)
    issue = issue_du_temoin(t["id"], tenue, ecarts)
    valeur = grandeur_valeur
    resultat.update({"statut": "calcule", "valeur_vraie": arrondi_decimal(valeur.valeur),
                     "borne_erreur": float(valeur.borne), "mode": valeur.mode,
                     "valeur_exacte": texte_fraction(valeur.exacte),
                     "quantites": {nom: (None if q is None else decrire(q)) for nom, q in quantites.items()
                                   if not isinstance(q, dict)},
                     "tenue_de_la_garantie": tenue, "issue_recalculee": issue})
    for nom, q in quantites.items():
        if isinstance(q, dict):
            resultat[nom] = {cle: (None if v is None else decrire(v)) for cle, v in q.items()}
    if "valeur_annoncee" in t:
        resultat["comparaison"] = comparer(valeur, t["valeur_annoncee"])
    if "issue_annoncee" in t:
        resultat["issue_annoncee"] = t["issue_annoncee"]
        resultat["accord_issue"] = (t["issue_annoncee"] == issue)
    return resultat


def comparer(valeur, annoncee):
    """§ 6, point 4 : un écart de plus de 0,001 est compté et nommé ; audit dans les deux sens."""
    a = rationnel(annoncee, "valeur_annoncee")
    if valeur.exacte is not None:
        ecart = abs(a - valeur.exacte)
        statut = "au_dela_de_0_001" if ecart > SEUIL_ECART else "en_deca_de_0_001"
        return {"valeur_annoncee": arrondi_decimal(a), "ecart": arrondi_decimal(ecart), "statut": statut}
    af = float(a)
    ecart_min = max(0.0, max(float(valeur.lo) - af, af - float(valeur.hi)))
    ecart_max = max(abs(af - float(valeur.lo)), abs(af - float(valeur.hi)))
    s = float(SEUIL_ECART)
    statut = "au_dela_de_0_001" if ecart_min > s else ("en_deca_de_0_001" if ecart_max <= s else "indecis_a_la_borne")
    return {"valeur_annoncee": arrondi_decimal(a), "ecart": arrondi_decimal(abs(af - float(valeur.valeur))),
            "ecart_min": ecart_min, "ecart_max": ecart_max, "statut": statut}


def _recalcul_sequentiel(t, typ, params):
    if typ not in REGLES_SEQUENTIELLES | {"jamais_alerter", "toujours_alerter"}: raise Refus("garantie_incoherente_seuil", f"règle « {typ} » sous une garantie « a tout instant »")  # GARDE:garantie_incoherente_seuil
    suite = t.get("suite")
    if not isinstance(suite, dict) or not {"taux_honnete", "horizon"} <= set(suite) or set(suite) - CLES_DE_SUITE: raise Refus("suite_absente", "garantie « a tout instant » : objet suite {taux_honnete, horizon[, taux_saboteur, taux_honnete_derive]} requis")  # GARDE:suite_absente
    horizon = entier(suite["horizon"], "horizon", 1)
    q = probabilite_ouverte(suite["taux_honnete"], "taux_honnete")
    if typ == "test_repete_sans_correction":
        alerte = predicat_test_repete(probabilite_ouverte(params["taux_nul"], "taux_nul"),
                                      probabilite_ouverte(params["niveau_annonce"], "niveau_annonce"), horizon)
    elif typ == "pari_de_bernoulli":
        q0 = probabilite_ouverte(params["taux_nul"], "taux_nul")
        p1 = probabilite_ouverte(params["taux_parie"], "taux_parie")
        if p1 == q0: raise Refus("taux_parie_egal_au_nul", "taux parié égal au taux nul : richesse constante")  # GARDE:taux_parie_egal_au_nul
        seuil = rationnel(params["seuil_de_richesse"], "seuil_de_richesse")
        if seuil <= 1: raise Refus("seuil_de_richesse_invalide", f"seuil de richesse {seuil} <= 1 : la richesse part de 1")  # GARDE:seuil_de_richesse_invalide
        alerte = predicat_pari(q0, p1, seuil, horizon)
    elif typ == "jamais_alerter":
        def alerte(_t, _k):
            return False
    else:
        def alerte(_t, _k):
            return True
    fa = Encadre.exact(probabilite_de_sonner(alerte, q, horizon))
    quantites = {"fausse_alerte_sur_horizon": fa}
    if "taux_saboteur" in suite:
        quantites["puissance_contre_le_saboteur"] = Encadre.exact(
            probabilite_de_sonner(alerte, probabilite_ouverte(suite["taux_saboteur"], "taux_saboteur"), horizon))
    if "taux_honnete_derive" in suite:
        quantites["fausse_alerte_sous_derive"] = Encadre.exact(
            probabilite_de_sonner(alerte, probabilite_ouverte(suite["taux_honnete_derive"], "taux_honnete_derive"), horizon))
    if t["grandeur"] == "puissance":
        if "puissance_contre_le_saboteur" not in quantites: raise Refus("puissance_sans_saboteur_sequentiel", "grandeur « puissance » sans taux_saboteur")  # GARDE:puissance_sans_saboteur_sequentiel
        return quantites, quantites["puissance_contre_le_saboteur"], []
    if t["grandeur"] != "fausse_alerte_sur_horizon": raise Refus("grandeur_incoherente_sequentielle", f"grandeur « {t['grandeur']} » sous une garantie « a tout instant »")  # GARDE:grandeur_incoherente_sequentielle
    return quantites, fa, []


def _taille(t, requise):
    n = t["n"]
    if requise and n is None: raise Refus("taille_absente", "règle à échantillon de calibration sans taille n")  # GARDE:taille_absente
    return None if n is None else entier(n, "n", 1)


def _recalcul_a_seuil(t, typ, params, lois, grandeur):
    if "lecture" not in lois: raise Refus("loi_de_lecture_absente", "loi de lecture requise : population sur laquelle la garantie est lue")  # GARDE:loi_de_lecture_absente
    lecture = construire_loi(lois["lecture"])
    if lecture.grappes: raise Refus("grappes_en_lecture", "une loi en grappes ne se lit pas comme loi de lecture : donner sa loi marginale")  # GARDE:grappes_en_lecture
    saboteurs = {}
    for nom, spec in (lois.get("saboteurs") or {}).items():
        saboteurs[nom] = construire_loi(spec)
        if saboteurs[nom].grappes: raise Refus("grappes_en_saboteur", f"saboteur « {nom} » en grappes")  # GARDE:grappes_en_saboteur
    a_echantillon = typ in REGLES_DE_RANG or typ in ("moyenne_plus_k_ecarts_types",)
    n = _taille(t, a_echantillon)
    calib = None
    meme_loi = False
    if a_echantillon:
        if "calibration" not in lois: raise Refus("loi_de_calibration_absente", "loi de calibration requise")  # GARDE:loi_de_calibration_absente
        calib = construire_loi(lois["calibration"])
        meme_loi = canonique(lois["calibration"]) == canonique(lois["lecture"])
    if typ == "plus_grand_de_la_tranche_voisine":
        voisine = lois.get("voisine")
        if not isinstance(voisine, dict) or set(voisine) != {"n", "loi"}: raise Refus("voisine_absente", "« plus grand de la tranche voisine » : lois.voisine {n, loi} requis")  # GARDE:voisine_absente
        n = entier(voisine["n"], "n de la tranche voisine", 1)
        calib = construire_loi(voisine["loi"])
        meme_loi = canonique(voisine["loi"]) == canonique(lois["lecture"])
    quantites = {}
    puissances, sachant, ecarts_base = {}, {}, {}
    if calib is not None and calib.grappes:
        if typ not in REGLES_DE_RANG or k_de_la_regle(typ, params, n) != 1: raise Refus("grappes_regle", "famille en grappes : seule la règle du plus grand score a une vérité exacte ici")  # GARDE:grappes_regle
        if n != calib.n_total(): raise Refus("grappes_taille", f"n = {n} différent de la somme des tailles de famille {calib.n_total()}")  # GARDE:grappes_taille
        if grandeur != "couverture" or t["garantie"] != "avec une confiance dite" or saboteurs: raise Refus("grappes_grandeur", "famille en grappes : seule la couverture (garantie « avec une confiance dite ») est calculée ici")  # GARDE:grappes_grandeur
        quantites["couverture"] = couverture_grappes(calib, lecture)
        quantites["taux_moyen"] = None
        return quantites, quantites["couverture"], []
    if typ in REGLES_DE_RANG or typ == "plus_grand_de_la_tranche_voisine":
        k = k_de_la_regle(typ, params, n)
        quantites["rang_k_ieme_plus_grand"] = Encadre.exact(Fraction(k))
        quantites["couverture"] = couverture_rang(n, k, calib, lecture, meme_loi)
        quantites["taux_moyen"] = taux_moyen_rang(n, k, calib, lecture, meme_loi)
        for taille in t.get("tailles_de_plus") or []:
            taille = entier(taille, "tailles_de_plus", 1)
            k2 = k_de_la_regle(typ, params, taille)
            quantites[f"taux_moyen_n{taille}"] = taux_moyen_rang(taille, k2, calib, lecture, meme_loi)
            quantites[f"couverture_n{taille}"] = couverture_rang(taille, k2, calib, lecture, meme_loi)
        for nom, sab in saboteurs.items():
            puissances[nom] = esperance_rang(n, k, calib, sab)
            sachant[nom] = puissance_rang_sachant(n, k, calib, lecture, sab)
    elif typ == "jamais_alerter":
        quantites["couverture"] = Encadre.exact(Fraction(1))
        quantites["taux_moyen"] = Encadre.exact(Fraction(0))
        for nom in saboteurs:
            puissances[nom] = Encadre.exact(Fraction(0))
            sachant[nom] = Encadre.exact(Fraction(0))
    elif typ == "toujours_alerter":
        quantites["couverture"] = Encadre.exact(Fraction(0))
        quantites["taux_moyen"] = Encadre.exact(Fraction(1))
        for nom in saboteurs:
            puissances[nom] = Encadre.exact(Fraction(1))
            sachant[nom] = None
    elif typ == "seuil_fixe":
        v = rationnel(params["valeur"], "valeur")
        taux = lecture.sf(v)
        taux_enc = Encadre(borner_probabilite(taux - TOLERANCE_EVALUATION), borner_probabilite(taux + TOLERANCE_EVALUATION))
        quantites["taux_moyen"] = taux_enc
        if abs(taux - float(ALPHA)) <= TOLERANCE_EVALUATION: raise Refus("taux_egal_a_alpha_seuil_fixe", "seuil fixe dont le taux vrai égale alpha à la tolérance près")  # GARDE:taux_egal_a_alpha_seuil_fixe
        quantites["couverture"] = Encadre.exact(Fraction(1 if taux <= float(ALPHA) else 0))
        for nom, sab in saboteurs.items():
            p = sab.sf(v)
            puissances[nom] = Encadre(borner_probabilite(p - TOLERANCE_EVALUATION), borner_probabilite(p + TOLERANCE_EVALUATION))
            sachant[nom] = puissances[nom] if taux <= float(ALPHA) else None
    elif typ == "moyenne_plus_k_ecarts_types":
        if n < 2: raise Refus("moyenne_k_taille", "« moyenne plus k écarts types » : n >= 2 requis")  # GARDE:moyenne_k_taille
        k = rationnel(params["k"], "k")
        par_convention = {}
        for convention in ("n_moins_1", "n"):
            cov, taux, pw = regle_moyenne_k(n, k, calib, lecture, saboteurs, convention)
            par_convention[convention] = (cov, taux, pw)
        quantites["couverture"] = par_convention["n_moins_1"][0]
        quantites["taux_moyen"] = par_convention["n_moins_1"][1]
        quantites["couverture_ecart_type_divise_par_n"] = par_convention["n"][0]
        quantites["taux_moyen_ecart_type_divise_par_n"] = par_convention["n"][1]
        for nom in saboteurs:
            puissances[nom] = par_convention["n_moins_1"][2][nom]
            sachant[nom] = None
    # écart de puissance à la base (le plus grand des n scores de calibration, même tirage)
    if saboteurs and calib is not None and typ != "plus_grand_de_la_tranche_voisine":
        for nom, sab in saboteurs.items():
            if typ in REGLES_DE_RANG and k_de_la_regle(typ, params, n) == 1:
                ecarts_base[nom] = Encadre.exact(Fraction(0))
            else:
                ecarts_base[nom] = puissances[nom].moins(esperance_rang(n, 1, calib, sab))
    elif saboteurs and typ in ("jamais_alerter", "toujours_alerter", "seuil_fixe") and n is not None and "calibration" in lois:
        calib_base = construire_loi(lois["calibration"])
        for nom, sab in saboteurs.items():
            ecarts_base[nom] = puissances[nom].moins(esperance_rang(n, 1, calib_base, sab))
    if puissances:
        quantites["puissances"] = puissances
        quantites["puissances_sachant_taux_au_plus_alpha"] = sachant
    if ecarts_base:
        quantites["ecarts_de_puissance_a_la_base"] = ecarts_base
    if grandeur == "fausse_alerte_sur_horizon": raise Refus("grandeur_incoherente_a_seuil", "« fausse_alerte_sur_horizon » hors d'une garantie « a tout instant »")  # GARDE:grandeur_incoherente_a_seuil
    if grandeur == "puissance":
        if len(puissances) != 1: raise Refus("puissance_sans_saboteur_unique", "grandeur « puissance » : exactement un saboteur requis")  # GARDE:puissance_sans_saboteur_unique
        valeur = next(iter(puissances.values()))
    else:
        valeur = quantites[grandeur]
    return quantites, valeur, list(ecarts_base.values())


def recalculer(entree):
    if not isinstance(entree, dict) or set(entree) != {"version_entree", "temoins"} or entree["version_entree"] != VERSION_ENTREE_RECALCUL or not isinstance(entree["temoins"], list): raise Refus("version_entree", f"entrée attendue : {{\"version_entree\": \"{VERSION_ENTREE_RECALCUL}\", \"temoins\": […]}}")  # GARDE:version_entree
    sortie = {"version_sortie": VERSION_SORTIE + "-recalcul", "alpha": texte_fraction(ALPHA),
              "seuil_ecart": texte_fraction(SEUIL_ECART), "tolerance_evaluation_declaree": TOLERANCE_EVALUATION,
              "temoins": {}}
    vus = set()
    for t in entree["temoins"]:
        ident = t.get("id") if isinstance(t, dict) else None
        cle = str(ident)
        if cle in vus: raise Refus("identifiant_double", f"identifiant {cle} en double")  # GARDE:identifiant_double
        vus.add(cle)
        try:
            sortie["temoins"][cle] = recalculer_temoin(t)
        except Refus as refus:
            sortie["temoins"][cle] = {"id": ident, "statut": "refuse", "code": refus.code, "raison": refus.message}
    statuts = [v["statut"] for v in sortie["temoins"].values()]
    sortie["comptes"] = {"calcules": statuts.count("calcule"), "refuses": statuts.count("refuse"),
                         "ecarts_au_dela_de_0_001": sum(1 for v in sortie["temoins"].values()
                                                       if v.get("comparaison", {}).get("statut") == "au_dela_de_0_001"),
                         "ecarts_indecis_a_la_borne": sum(1 for v in sortie["temoins"].values()
                                                         if v.get("comparaison", {}).get("statut") == "indecis_a_la_borne"),
                         "desaccords_d_issue": sum(1 for v in sortie["temoins"].values() if v.get("accord_issue") is False)}
    return sortie


# ---------------------------------------------------------------------------------------------------
# Lois de référence de la note (bloc C, D, E, F) : servent la table pour les témoins dont la valeur
# dépend de la loi que l'auteur choisira. Chaque valeur qui en dépend est marquée.
# ---------------------------------------------------------------------------------------------------

AIRES = (Fraction(69, 100), Fraction(80, 100), Fraction(95, 100))
P_ECHEC_PROPOSE = Fraction(1, 20)            # § 3.2, [proposition] 0,05
RHO_PROPOSE = Fraction(1, 5)                 # § 3.2, famille H, [proposition] 0,2
S_TAUX_HONNETE, S_HORIZON = Fraction(1, 5), 300
S_TAUX_SABOTEUR, S_TAUX_DERIVE = Fraction(3, 10), Fraction(1, 4)

LOI_NORMALE_REDUITE = {"type": "normale", "parametres": {"mu": 0, "sigma": 1}}


def decalage_binormal(aire):
    """Binormale à variances égales : aire = Φ(d / √2), donc d = √2 Φ^{-1}(aire), en écarts types."""
    bas, haut = _isf_continue(Normale(0, 1), 1.0 - float(aire))
    return RACINE_2 * (bas + haut) / 2.0


def decalage_qui_triple(loi):
    """Décalage d (unités brutes) tel que 1 − F(q99 − d) = 0,03 : d = q99 − q97 ; rendu en écarts types."""
    q99 = sum(_isf_continue(loi, 0.01)) / 2.0
    q97 = sum(_isf_continue(loi, 0.03)) / 2.0
    return (q99 - q97) / loi.ecart_type()


def spec_decalage(spec, delta):
    return {"type": "decalage", "parametres": {"loi": spec, "delta_en_ecarts_types": Fraction(delta)}}


def nom_d_aire(aire):
    return "aire_0_" + str(aire.numerator * 100 // aire.denominator).zfill(2)


def saboteurs_binormaux():
    return {nom_d_aire(a): spec_decalage(LOI_NORMALE_REDUITE, decalage_binormal(a))
            for a in AIRES}


def pi_critique_couverture(n, risque):
    """Le plus petit π tel que 1 − (1 − π)^n >= 1 − risque, encadré en rationnels par dichotomie."""
    bas, haut = Fraction(0), Fraction(1)
    for _ in range(80):
        mi = (bas + haut) / 2
        if 1 - (1 - mi) ** n >= 1 - risque:
            haut = mi
        else:
            bas = mi
    return bas, haut


# ---------------------------------------------------------------------------------------------------
# La table des dix-sept témoins imposés (§ 3.1)
# ---------------------------------------------------------------------------------------------------

def _temoin_reference(ident, n, regle, garantie, risque, grandeur, calib, lecture, saboteurs=None,
                      population="tous_les_honnetes", portee="tous les episodes honnetes de la tranche",
                      suite=None, tailles_de_plus=None):
    t = {"id": ident, "n": n, "regle": regle, "garantie": garantie, "risque_ou_niveau": risque,
         "grandeur": grandeur, "population_de_calibration": population, "portee_de_la_garantie": portee,
         "lois": {}}
    if calib is not None:
        t["lois"]["calibration"] = calib
    if lecture is not None:
        t["lois"]["lecture"] = lecture
    if saboteurs:
        t["lois"]["saboteurs"] = saboteurs
    if suite is not None:
        t["suite"] = suite
    if tailles_de_plus:
        t["tailles_de_plus"] = tailles_de_plus
    return t


def temoins_imposes_en_entree():
    """Les dix-sept témoins imposés, au format d'entrée du recalcul, aux lois de référence de la note
    (normale réduite ; saboteur binormal ; ρ = 0,2 ; monde S aux propositions). T14 à T17 portent une
    loi de référence de C et de I qui n'est PAS celle de l'auteur : la table ne lit pas T14 ici
    (voir `table_des_temoins`)."""
    N01 = LOI_NORMALE_REDUITE
    conf, moy, inst = "avec une confiance dite", "en moyenne", "a tout instant"
    r5, r1 = Fraction(5, 100), Fraction(1, 100)
    delta = decalage_qui_triple(Normale(0, 1))
    sab = saboteurs_binormaux()
    grappes = lambda tailles: {"type": "effet_de_famille_plus_bruit",
                               "parametres": {"correlation_intra": RHO_PROPOSE, "tailles_de_famille": tailles}}
    return [
        _temoin_reference("T01", 300, {"type": "k_ieme_plus_grand", "k": 3}, conf, r5, "couverture", N01, N01),
        _temoin_reference("T02", 299, {"type": "k_ieme_plus_grand", "k": 1}, conf, r5, "couverture", N01, N01),
        _temoin_reference("T03", 300, {"type": "k_ieme_plus_grand", "k": 3}, moy, None, "taux_moyen", N01, N01),
        _temoin_reference("T04", 1000, {"type": "k_ieme_plus_grand", "k": 6}, conf, r5, "couverture", N01, N01),
        _temoin_reference("T05", 200, {"type": "jamais_alerter"}, moy, None, "taux_moyen", N01, N01, sab),
        _temoin_reference("T06", 200, {"type": "k_ieme_plus_grand", "k": 1}, conf, r5, "couverture", N01, N01),
        _temoin_reference("T07", 200, {"type": "k_ieme_plus_grand", "k": 1}, moy, None, "taux_moyen", N01, N01, sab,
                          tailles_de_plus=[400]),
        _temoin_reference("T08", 400, {"type": "quantile_empirique", "niveau": Fraction(99, 100)}, conf, r5,
                          "couverture", N01, N01),
        _temoin_reference("T09", 299, {"type": "k_ieme_plus_grand", "k": 1}, conf, r5, "couverture", N01,
                          spec_decalage(N01, delta)),
        _temoin_reference("T10", 300, {"type": "k_ieme_plus_grand", "k": 1}, conf, r5, "couverture",
                          grappes([100] * 3), N01),
        _temoin_reference("T11", 300, {"type": "k_ieme_plus_grand", "k": 1}, conf, r5, "couverture",
                          grappes([10] * 30), N01),
        _temoin_reference("T12", None, {"type": "test_repete_sans_correction", "taux_nul": S_TAUX_HONNETE,
                                        "niveau_annonce": r1}, inst, r1, "fausse_alerte_sur_horizon", None, None,
                          suite={"taux_honnete": S_TAUX_HONNETE, "horizon": S_HORIZON,
                                 "taux_saboteur": S_TAUX_SABOTEUR, "taux_honnete_derive": S_TAUX_DERIVE}),
        _temoin_reference("T13", None, {"type": "pari_de_bernoulli", "taux_nul": S_TAUX_HONNETE,
                                        "taux_parie": S_TAUX_SABOTEUR, "seuil_de_richesse": 100}, inst, r1,
                          "fausse_alerte_sur_horizon", None, None,
                          suite={"taux_honnete": S_TAUX_HONNETE, "horizon": S_HORIZON,
                                 "taux_saboteur": S_TAUX_SABOTEUR, "taux_honnete_derive": S_TAUX_DERIVE}),
    ]


DEFINITIONS = {
    "T01": "A, une tranche, n = 300 ; le seuil est le 3e plus grand score ; « avec une confiance dite », risque 5 %",
    "T02": "A, n = 299 ; le seuil est le plus grand score ; « avec une confiance dite », risque 5 %",
    "T03": "A, n = 300 ; le seuil est le 3e plus grand score ; « en moyenne »",
    "T04": "A, n = 1 000 ; le seuil est le 6e plus grand score ; « avec une confiance dite », risque 5 %",
    "T05": "A, n = 200 ; ne jamais alerter ; « en moyenne »",
    "T06": "A, n = 200 ; le seuil est le plus grand score ; « avec une confiance dite », risque 5 %",
    "T07": "A, n = 200 et n = 400 ; le seuil est le plus grand score (la base) ; « en moyenne »",
    "T08": "A, n = 400 ; le seuil est le quantile empirique à 99 % ; « avec une confiance dite », risque 5 %",
    "T09": "F ; le seuil est le plus grand de 299, la moyenne honnête décalée entre calibration et usage du décalage qui triple un taux de 1 % ; « avec une confiance dite », risque 5 % ; aucune supposition déclarée",
    "T10": "H ; le seuil est le plus grand de 300, calibration faite de 3 familles de 100 épisodes ; « avec une confiance dite », risque 5 %",
    "T11": "H ; le même, 30 familles de 10 épisodes ; la même",
    "T12": "S ; test binomial exact unilatéral à droite du compte cumulé d'alertes contre le taux honnête 0,20, rejoué à chaque épisode de 1 à 300, sans correction ; valeur p : probabilité, sous ce taux, d'un compte au moins égal au compte observé ; alerte dès qu'elle est strictement sous 0,01 ; « à tout instant », niveau 0,01",
    "T13": "S ; pari de Bernoulli : rapport de vraisemblance du taux 0,30 contre le taux honnête 0,20, alerte dès que la richesse atteint ou dépasse 100 ; « à tout instant », niveau 0,01",
    "T14": "C, n = 299 ; le seuil est le plus grand score, calibré sur tous les honnêtes ; garantie lue sur les seuls honnêtes qui échouent ; « avec une confiance dite », risque 5 %",
    "T15": "C, n = 299 ; la même règle, calibrée sur tous les honnêtes ; garantie lue sur tous les honnêtes ; la même",
    "T16": "C, n = 299 ; le seuil est le plus grand score, calibré sur 299 honnêtes qui échouent ; garantie lue sur les honnêtes qui échouent ; la même",
    "T17": "I, n = 299 ; comme T14 ; la même",
}


def _entree_de_table(ident, valeur, issue, depend_de_la_loi, loi_de_reference, formule, valeurs_de_plus,
                     issue_depend_de_la_loi=False, mode=None, borne=None, exacte=None, remarque=None):
    return {"definition_citee": DEFINITIONS[ident], "valeur_vraie": arrondi_decimal(valeur),
            "valeur_exacte": texte_fraction(exacte), "borne_erreur": borne, "mode": mode,
            "depend_de_la_loi_de_l_auteur": depend_de_la_loi, "loi_de_reference": loi_de_reference,
            "issue_attendue": issue, "issue_depend_de_la_loi_de_l_auteur": issue_depend_de_la_loi,
            "formule": formule, "valeurs_de_plus": valeurs_de_plus, "remarque": remarque}


def _vdp(dico):
    return {nom: (None if v is None else (arrondi_decimal(v) if not isinstance(v, Encadre) else decrire(v)))
            for nom, v in dico.items()}


def table_des_temoins():
    """La table des dix-sept témoins imposés, valeurs vraies et issues attendues."""
    rec = {t["id"]: recalculer_temoin(t) for t in temoins_imposes_en_entree()}
    entrees = {t["id"]: t for t in temoins_imposes_en_entree()}
    table = {}
    libre = "toute loi continue de la famille (statistiques d'ordre)"

    def depuis(ident, depend, loi_ref, formule, vdp=None, issue_depend=False, remarque=None):
        r = rec[ident]
        table[ident] = _entree_de_table(
            ident, Fraction(r["valeur_exacte"]) if r["valeur_exacte"] else r["valeur_vraie"],
            r["issue_recalculee"], depend, loi_ref, formule, vdp or {}, issue_depend, r["mode"],
            r["borne_erreur"], Fraction(r["valeur_exacte"]) if r["valeur_exacte"] else None, remarque)

    depuis("T01", False, libre, "P(Beta(3, 298) <= 0,01) = P(Bin(300, 0,01) >= 3)")
    depuis("T02", False, libre, "1 − 0,99^299")
    depuis("T03", False, libre, "E[Beta(3, 298)] = 3/301")
    depuis("T04", False, libre, "P(Bin(1000, 0,01) >= 6)")
    depuis("T06", False, libre, "1 − 0,99^200")
    depuis("T08", False, libre, "rang : ⌈400 × 0,99⌉ = 396e plus petit = 5e plus grand ; P(Bin(400, 0,01) >= 5)",
           {"rang_k_ieme_plus_grand": Fraction(5)})
    # T05 et T07 : valeur et issue indépendantes de la loi ; puissances à la loi de référence binormale
    for ident in ("T05", "T07"):
        r = rec[ident]
        vdp = {}
        for nom, d in r["puissances"].items():
            vdp[f"puissance_{nom}"] = d
        for nom, d in r["puissances_sachant_taux_au_plus_alpha"].items():
            vdp[f"puissance_sachant_taux_au_plus_alpha_{nom}"] = d
        for nom, d in r["ecarts_de_puissance_a_la_base"].items():
            vdp[f"ecart_de_puissance_a_la_base_{nom}"] = d
        if ident == "T07":
            vdp["taux_moyen_n400"] = r["quantites"]["taux_moyen_n400"]
        for a in AIRES:
            vdp[f"decalage_en_ecarts_types_{nom_d_aire(a)}"] = arrondi_decimal(decalage_binormal(a))
        valeur = Fraction(r["valeur_exacte"])
        table[ident] = _entree_de_table(
            ident, valeur, r["issue_recalculee"], False, libre,
            "jamais d'alerte : taux vrai nul" if ident == "T05" else "E[Beta(1, n)] = 1/(n + 1), soit 1/201 et 1/401",
            vdp, False, "exact_rationnel", 0.0, valeur,
            "puissances et écarts : loi de référence binormale (normale réduite, saboteur décalé de √2 Φ⁻¹(aire)) ; "
            "ils dépendent de la loi de l'auteur ; l'issue, non : " +
            ("l'écart vaut −(puissance de la base) < 0 sous toute loi à support non borné à droite" if ident == "T05"
             else "règle identique à la base, écart apparié nul par construction"))
    delta = decalage_qui_triple(Normale(0, 1))
    depuis("T09", True, "normale réduite (note, bloc D)", "couverture = 1 − (1 − P(X >= q99 + d))^299, d = q99 − q97 (décalage qui fait passer à 3 % le taux du quantile vrai à 99 %)",
           {"decalage_en_ecarts_types": delta}, True,
           "le décalage est vers le haut (scores plus suspects à l'usage) : la lettre ne dit pas le sens ; lecture de la note")
    depuis("T10", True, "effet de famille et bruit gaussiens, ρ = 0,2 (note, bloc E)",
           "1 − (E_U[Φ((z99 − √ρ U)/√(1 − ρ))^100])^3", {}, True)
    depuis("T11", True, "effet de famille et bruit gaussiens, ρ = 0,2 (note, bloc E)",
           "1 − (E_U[Φ((z99 − √ρ U)/√(1 − ρ))^10])^30", {}, True)
    for ident in ("T12", "T13"):
        r = rec[ident]
        vdp = {}
        if ident == "T13":
            vdp = {"puissance_contre_le_saboteur_0_30": r["quantites"]["puissance_contre_le_saboteur"],
                   "fausse_alerte_sous_derive_0_25": r["quantites"]["fausse_alerte_sous_derive"]}
        depuis(ident, True, "monde S aux propositions : taux honnête 0,20, horizon 300, saboteur 0,30, dérive 0,25",
               "programmation dynamique exacte sur (épisode, compte d'alertes), rationnels", vdp, True)
    # T14 à T17 : familles C et I, lois de l'auteur
    p = P_ECHEC_PROPOSE
    borne_conditionnelle = ALPHA / p
    pi_bas, pi_haut = pi_critique_couverture(299, Fraction(5, 100))
    t15 = couverture_rang_exacte(299, 1)
    table["T14"] = _entree_de_table(
        "T14", None, None, True, None,
        "couverture = 1 − (1 − π)^299, π = P_tous(X >= G_échec⁻¹(0,99))",
        _vdp({"borne_alpha_sur_p_echec": borne_conditionnelle, "pi_critique_borne_basse": pi_bas,
              "pi_critique_borne_haute": pi_haut, "p_echec_propose": p}),
        True, None, None, None,
        "valeur et issue calculées au recalcul, sur la loi de C que l'auteur écrira ; la garantie tient si et "
        "seulement si π >= π critique ; si les honnêtes qui échouent ont des scores stochastiquement plus grands, "
        "π <= 0,01 et la couverture ne dépasse pas 1 − 0,99^299")
    table["T15"] = _entree_de_table(
        "T15", t15, "tient", False, "toute loi continue de C (le mélange est continu)",
        "1 − 0,99^299 : calibration et lecture sur la même population",
        _vdp({"borne_alpha_sur_p_echec": borne_conditionnelle, "p_echec_propose": p,
              "taux_moyen_parmi_ceux_qui_echouent": None}),
        False, "exact_rationnel", 0.0, t15,
        "taux moyen parmi ceux qui échouent : dépend de la loi de C, calculé au recalcul")
    table["T16"] = _entree_de_table(
        "T16", t15, "tient", False, "toute loi continue de la composante « honnête qui échoue »",
        "1 − 0,99^299 : calibré et lu sur les honnêtes qui échouent",
        _vdp({"borne_alpha_sur_p_echec": borne_conditionnelle, "p_echec_propose": p,
              "taux_moyen_parmi_ceux_qui_echouent": Fraction(1, 300)}),
        False, "exact_rationnel", 0.0, t15)
    pi_limite = ALPHA * p
    pi_marge = ALPHA * p + Fraction(1, 1000) * p
    cov_limite = 1 - (1 - pi_limite) ** 299
    cov_marge = 1 - (1 - pi_marge) ** 299
    table["T17"] = _entree_de_table(
        "T17", cov_limite, "morte_invalide", True, "famille I à sa limite : taux parmi ceux qui échouent = α / P(échec) au quantile vrai à 99 %",
        "π = α·P(échec) à la limite, π ∈ [α·P(échec), α·P(échec) + 0,001·P(échec)] sous la condition « à 0,001 près » ; couverture = 1 − (1 − π)^299",
        _vdp({"borne_alpha_sur_p_echec": borne_conditionnelle, "p_echec_propose": p,
              "couverture_borne_basse_sous_condition": cov_limite, "couverture_borne_haute_sous_condition": cov_marge,
              "taux_moyen_parmi_ceux_qui_echouent": None}),
        False, "exact_sous_hypothese", 0.0, cov_limite,
        "issue indépendante de la loi tant que I approche la borne à 0,001 près (couverture <= " +
        f"{float(cov_marge):.4f} < 0,95) ; valeur exacte au recalcul sur la loi de l'auteur ; taux moyen parmi "
        "ceux qui échouent : au recalcul")
    for ident, t in entrees.items():
        table[ident]["entree_de_reference"] = t
    return table


def sortie_table():
    return {"version_sortie": VERSION_SORTIE, "alpha": texte_fraction(ALPHA),
            "tolerance_evaluation_declaree": TOLERANCE_EVALUATION,
            "demi_largeur_cible_des_integrales": DEMI_LARGEUR_CIBLE,
            "ids_lus_sans_gain": sorted(IDS_LUS_SANS_GAIN),
            "temoins": table_des_temoins()}


# ---------------------------------------------------------------------------------------------------
# Entrée et sortie
# ---------------------------------------------------------------------------------------------------

def _pas_de_constante(nom):
    raise Refus("constante_json", f"constante JSON {nom} refusée")


def lire_json(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.loads(f.read(), parse_float=Fraction, parse_constant=_pas_de_constante)


def _vers_json(obj):
    if isinstance(obj, Fraction):
        return arrondi_decimal(obj)
    raise TypeError(f"non sérialisable : {type(obj).__name__}")


def ecrire_json(obj, chemin):
    import os
    if os.path.exists(chemin): raise Refus("sortie_existante", f"{chemin} existe : on n'écrase jamais (R12)")  # GARDE:sortie_existante
    texte = json.dumps(obj, sort_keys=True, ensure_ascii=False, indent=1, default=_vers_json) + "\n"
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(texte)


def main(argv):
    try:
        if len(argv) == 1 and not argv[0].startswith("--"):
            ecrire_json(sortie_table(), argv[0])
            return 0
        if len(argv) == 3 and argv[0] == "--recalculer":
            ecrire_json(recalculer(lire_json(argv[1])), argv[2])
            return 0
    except Refus as refus:
        print(f"REFUS {refus.code} : {refus.message}", file=sys.stderr)
        return 3
    print("usage : PROGRAMME SORTIE_JSON | PROGRAMME --recalculer TEMOINS_JSON SORTIE_JSON", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
