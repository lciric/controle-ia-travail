"""Épreuve de la règle de la note d'écart (projet v1, lignes 23 à 28), lue à la lettre.

Réseau d'aires factice, écrit par le contre-lecteur, non opposable :
loi honnête = normale réduite arrondie au pas h (valeurs k*h), tronquée à |x| <= 12.
Aire d'un décalage d (unité brute) : P(S > H) + 0,5 P(S = H), S = H' + d, H, H' indépendantes
de même loi. Décalage lu en écarts types de la loi arrondie (racine de sa variance).
Aires atteignables : valeurs de palier P(D <= k h) et de saut P(D < k h) + 0,5 P(D = k h),
D = H' - H (symétrique).
Aucune entrée extérieure ; aucune sortie de l'auteur des mondes n'est lue.
"""
import math

AIRES_DITES = (0.69, 0.80, 0.95)
TOL_A, TOL_COMPTE, PLAFOND, EGAL = 0.005, 0.001, 0.02, 1e-9


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def phi_inv(p):
    lo, hi = -10.0, 10.0
    for _ in range(200):
        m = (lo + hi) / 2
        if phi(m) < p:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


class LoiArrondie:
    def __init__(self, h, echelle=1.0):
        self.h = h
        kmax = int(math.ceil(12 * echelle / h))
        self.k = list(range(-kmax, kmax + 1))
        self.p = [phi((k + 0.5) * h / echelle) - phi((k - 0.5) * h / echelle) for k in self.k]
        s = sum(self.p)
        self.p = [x / s for x in self.p]
        moy = sum(k * h * p for k, p in zip(self.k, self.p))
        self.sigma = math.sqrt(sum((k * h - moy) ** 2 * p for k, p in zip(self.k, self.p)))
        # loi de D = H' - H sur les entiers m (valeur m*h)
        q = {}
        for i, pi in zip(self.k, self.p):
            for j, pj in zip(self.k, self.p):
                q[i - j] = q.get(i - j, 0.0) + pi * pj
        self.m = sorted(q)
        self.q = [q[m] for m in self.m]
        cum, c = [], 0.0
        for x in self.q:
            c += x
            cum.append(c)
        self.cum = dict(zip(self.m, cum))
        self.qd = dict(zip(self.m, self.q))
        self.arrondie = True

    def p_le(self, k):  # P(D <= k)
        if k < self.m[0]:
            return 0.0
        if k > self.m[-1]:
            return 1.0
        return self.cum[k]

    def aire_brute(self, d):
        r = d / self.h
        kr = round(r)
        if abs(r - kr) < 1e-12:  # saut : ex aequo comptés pour moitié
            return self.p_le(kr - 1) + 0.5 * self.qd.get(kr, 0.0)
        return self.p_le(math.floor(r))  # palier

    def atteignables(self):
        vals = set()
        for k in range(self.m[0] - 1, self.m[-1] + 2):
            vals.add(self.p_le(k))
            vals.add(self.p_le(k - 1) + 0.5 * self.qd.get(k, 0.0))
        return sorted(vals)

    def encadrantes(self, a):
        v = self.atteignables()
        sous = max(x for x in v if x <= a)
        sur = min(x for x in v if x >= a)
        return sous, sur

    def decalage_pour_aire(self, cible):
        """Décalage en écarts types qui réalise exactement l'aire atteignable 'cible'."""
        for k in range(self.m[0] - 1, self.m[-1] + 2):
            if abs(self.p_le(k) - cible) <= EGAL:  # palier ]k h, (k+1) h[
                return (k + 0.5) * self.h / self.sigma
            if abs(self.p_le(k - 1) + 0.5 * self.qd.get(k, 0.0) - cible) <= EGAL:
                return k * self.h / self.sigma
        raise ValueError("aire non atteignable")


class LoiContinue:
    """Normale réduite continue : aire de d = Phi(d / sqrt 2) ; tout [0, 1] est atteignable."""
    arrondie = False
    sigma = 1.0

    def aire_brute(self, d):
        return phi(d / math.sqrt(2.0))

    def encadrantes(self, a):
        return a, a


def regle_note(loi, decalages_et):
    """Règle de la note, lignes 23 à 28, lue à la lettre ; la lettre scellée vaut ailleurs."""
    lignes, aires = [], []
    for a, s in zip(AIRES_DITES, decalages_et):
        A = loi.aire_brute(s * loi.sigma)
        aires.append(A)
        lignes.append({"a": a, "decalage_et": s, "aire": A})
    croissantes = all(aires[i] < aires[i + 1] for i in range(len(aires) - 1))
    for L in lignes:
        a, A = L["a"], L["aire"]
        L["ecart_compte_plus_0_001"] = abs(A - a) > TOL_COMPTE
        if abs(A - a) <= TOL_A:
            L["issue"] = "(a) conforme"
            continue
        if not loi.arrondie:
            L["issue"] = "échec, lettre scellée : non converti, rapporté (raison non nommée par la note)"
            continue
        sous, sur = loi.encadrantes(a)
        L["v_sous"], L["v_sur"] = sous, sur
        c1 = abs(A - sous) <= EGAL or abs(A - sur) <= EGAL
        c2 = abs(A - a) <= PLAFOND
        if c1 and c2 and croissantes:
            L["issue"] = "conforme au pas du réseau"
        elif min(abs(sous - a), abs(sur - a)) > PLAFOND:
            L["issue"] = "non converti : réseau trop grossier pour l'aire dite"
        elif not c1:
            L["issue"] = "non converti : aucune unité ne réalise les aires"
        else:
            L["issue"] = "non converti : AUCUNE DES DEUX RAISONS DE LA LIGNE 28 NE S'APPLIQUE"
    ok = all(L["issue"] in ("(a) conforme", "conforme au pas du réseau") for L in lignes)
    un_seul = any(L["issue"] == "conforme au pas du réseau" for L in lignes)
    return lignes, ok, un_seul


def montrer(nom, prediction, loi, decalages):
    lignes, ok, un_seul = regle_note(loi, decalages)
    print("=== " + nom)
    print("  prédit : " + prediction)
    for L in lignes:
        extra = ""
        if "v_sous" in L:
            extra = "  v_sous=%.4f v_sur=%.4f" % (L["v_sous"], L["v_sur"])
        print("  a=%.2f  décalage=%.4f ET  aire=%.4f%s  -> %s" % (L["a"], L["decalage_et"], L["aire"], extra, L["issue"]))
    print("  famille convertie (lecture conjointe, chaque décalage reçu) : %s" % ok)
    print("  au moins un décalage « conforme au pas du réseau » (lecture isolée de la ligne 27) : %s" % un_seul)
    print()


def main():
    print("Réseau factice : aires encadrantes de la normale arrondie, pas en unité brute")
    for h in (0.1, 0.25, 0.5, 1.0, 2.0):
        L = LoiArrondie(h)
        txt = []
        for a in AIRES_DITES:
            s, u = L.encadrantes(a)
            txt.append("a=%.2f [%.4f ; %.4f]" % (a, s, u))
        print("  pas %.2f (sigma arrondie %.4f) : %s" % (h, L.sigma, " ; ".join(txt)))
    print()

    # VRAI 1 : pas 0,25, l'auteur prend l'aire atteignable la plus proche de chaque aire dite.
    L = LoiArrondie(0.25)
    dec = []
    for a in AIRES_DITES:
        s, u = L.encadrantes(a)
        cible = s if abs(s - a) <= abs(u - a) else u
        dec.append(L.decalage_pour_aire(cible))
    montrer("VRAI 1 : pas 0,25, aire atteignable la plus proche",
            "0,69 et 0,80 en « conforme au pas du réseau » ; 0,95 en (a) ou (a bis) ; famille convertie",
            L, dec)

    # VRAI 2 : loi continue, décalages exacts.
    C = LoiContinue()
    montrer("VRAI 2 : loi continue, décalages exacts sqrt2 * Phi^-1(a)",
            "trois (a) ; famille convertie ; la note n'intervient pas",
            C, [math.sqrt(2) * phi_inv(a) for a in AIRES_DITES])

    # FAUX 1 : pas 0,1, l'auteur prend pour 0,69 la deuxième aire atteignable sous l'aire dite,
    # à moins de 0,02 de 0,69 mais non encadrante.
    L = LoiArrondie(0.1)
    v = L.atteignables()
    sous = max(x for x in v if x <= 0.69)
    deux = max(x for x in v if x < sous - EGAL)
    print("  (pas 0,1 : deuxième aire sous 0,69 = %.4f, à %.4f de 0,69)" % (deux, 0.69 - deux))
    dec = [L.decalage_pour_aire(deux)]
    for a in AIRES_DITES[1:]:
        s, u = L.encadrantes(a)
        dec.append(L.decalage_pour_aire(s if abs(s - a) <= abs(u - a) else u))
    montrer("FAUX 1 : pas 0,1, voisin suivant (non encadrant) à moins de 0,02 pour 0,69",
            "0,69 non converti, « aucune unité ne réalise les aires » ; famille non convertie",
            L, dec)

    # FAUX 2 : unité brute sous une loi d'écart type 2 (pas 0,5 brut), nombres écrits pour une loi réduite.
    L = LoiArrondie(0.5, echelle=2.0)
    brut = [math.sqrt(2) * phi_inv(a) for a in AIRES_DITES]
    montrer("FAUX 2 : nombres en unité brute sous une loi d'écart type 2, lus en écarts types",
            "les trois non convertis ; famille non convertie",
            L, [b for b in brut])

    # FAUX 3 : pas 0,5, l'auteur prend v_sous pour 0,69 (à plus de 0,02) alors que v_sur est à moins de 0,02.
    L = LoiArrondie(0.5)
    dec = []
    for a in AIRES_DITES:
        s, u = L.encadrantes(a)
        dec.append(L.decalage_pour_aire(s if a == 0.69 else (s if abs(s - a) <= abs(u - a) else u)))
    montrer("FAUX 3 : pas 0,5, aire encadrante du dessous hors plafond, celle du dessus dans le plafond",
            "0,69 non converti ; la ligne 28 ne donne aucune de ses deux raisons (trou de nommage)",
            L, dec)

    # FAUX 4 : loi continue, décalage qui réalise a + 0,01.
    montrer("FAUX 4 : loi continue, aires dites + 0,01",
            "trois non convertis par la lettre scellée ; la note n'ajoute aucune conversion",
            C, [math.sqrt(2) * phi_inv(a + 0.01) for a in AIRES_DITES])

    # FAUX 5 : famille mixte : 0,69 reçu au pas du réseau, 0,80 un palier trop loin.
    L = LoiArrondie(0.25)
    s69, u69 = L.encadrantes(0.69)
    s80, u80 = L.encadrantes(0.80)
    v = L.atteignables()
    loin = min(x for x in v if x > u80 + EGAL)
    s95, u95 = L.encadrantes(0.95)
    dec = [L.decalage_pour_aire(u69), L.decalage_pour_aire(loin),
           L.decalage_pour_aire(s95 if abs(s95 - 0.95) <= abs(u95 - 0.95) else u95)]
    montrer("FAUX 5 : pas 0,25, 0,69 au pas du réseau, 0,80 un palier trop loin",
            "famille non convertie en lecture conjointe ; la lecture isolée de la ligne 27 la convertirait",
            L, dec)


if __name__ == "__main__":
    main()
