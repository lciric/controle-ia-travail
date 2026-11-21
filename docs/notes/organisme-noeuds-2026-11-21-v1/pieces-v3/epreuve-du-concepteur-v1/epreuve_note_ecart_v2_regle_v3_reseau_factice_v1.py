#!/usr/bin/env python3
"""Épreuve, sur réseau factice, du projet de note d'écart v2 et de la règle v3 (tolérance du
contrôle par l'aire pour les lois arrondies), codés ici à la lettre.

Ce que ce programme éprouve : la lettre des sections « L'écart » et « Ce qui ne change pas » du
projet de note d'écart v2, et la règle v3 du programme de vérification de la sortie des mondes,
sur des familles factices à trois tranches et trois décalages.

Ce qu'il n'est pas : ni le programme de vérification, ni une mesure. Lois factices choisies par
le concepteur (normale, et normale arrondie au multiple le plus proche d'un pas) ; flottants ;
de la main du concepteur ; non contre-lu : illustration, non opposable. Aucune entrée
extérieure : aucun fichier n'est lu, aucune sortie de l'auteur des mondes, aucune vérité.

Conventions, celles que la note suppose (rapport v6 du développeur du programme de vérification,
partie 1, « Aire », et partie 6, remarque 1) :
- aire d'un décalage d, en unité du score : P(X + d > Y) + 1/2 P(X + d = Y), X et Y indépendants,
  de la loi honnête de la tranche ; pour une loi arrondie, le décalage s'ajoute au score arrondi ;
- lecture retenue : d = nombre écrit x écart type de la loi honnête de la tranche (racine de la
  variance, calculée sur les masses pour un réseau) ; unité brute : d = nombre écrit ;
- un décalage est tenu pour posé sur un multiple du pas à 1e-9 pas près : convention de cette
  épreuve seulement, la note n'en dit rien.

Les prédictions (constantes ATTENDU et MUTATIONS) sont écrites avant la première exécution.
Commande : python3 -I -B epreuve_note_ecart_v2_regle_v3_reseau_factice_v1.py
"""
import math
import sys

AIRES_DITES = (0.69, 0.80, 0.95)
TOLERANCE = 0.005      # pièce scellée
SEUIL_NOMME = 0.001    # pièce scellée
PLAFOND = 0.02         # note d'écart, valeur accordée
EGAL = 1e-9            # note d'écart, condition 1
SUR_MULTIPLE = 1e-9    # convention de cette épreuve

# Issues d'un décalage lu dans une tranche.
A = "conforme à 0,005 près"
A_BIS = "conforme au pas du réseau"
R1 = "réseau trop grossier pour l'aire dite"
R2 = "aire encadrante hors du plafond"
R3 = "aucune unité ne réalise les aires"
R4 = "aires non croissantes dans la tranche"
HORS = "hors de 0,005, tranche non arrondie"
NON_RECU = "non reçu sous la lecture en écarts types, raison non nommée"
SANS_RAISON = "AUCUNE RAISON NE S'APPLIQUE"
RECUS = (A, A_BIS)

# Issues d'une famille.
CONVERTIE = "conforme : saboteur converti"
BRUTE = "unité brute constatée : saboteur non converti"
ILLISIBLE = "non lisible : saboteur non converti"

# Mutations : chacune défait une correction, et un objet nommé doit la voir.
M1 = "un seul décalage reçu suffit à convertir la famille (lecture isolée de la ligne 27 du projet v1)"
M2 = "« conforme au pas du réseau » jugé aussi sous l'unité brute (règle v2, point 5)"
M3 = "condition 1 omise : toute aire à 0,02 au plus est reçue"
M4 = "plafond relevé de 0,02 à 0,06"
M5 = "raison « aire encadrante hors du plafond » omise (ligne 28 du projet v1)"
M6 = "portée étendue à toute tranche d'une famille qui a une tranche arrondie"
M7 = "valeurs de saut omises des aires atteignables"
M8 = "condition d'empreinte retirée : l'écart joue sans la note scellée"


def fr(x, n=4):
    return ("%.*f" % (n, x)).replace(".", ",")


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def phi_inv(p):
    lo, hi = -12.0, 12.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if phi(m) < p:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def nombre_continu(a):
    """Décalage, en écarts types, qui réalise l'aire a sous une loi normale continue."""
    return math.sqrt(2.0) * phi_inv(a)


class LoiNormale:
    """Loi continue factice : normale centrée."""
    arrondie = False

    def __init__(self, ecart_type=1.0):
        self.sigma = ecart_type
        self.nom = "normale centrée d'écart type %s, continue" % fr(ecart_type, 2)

    def aire(self, d):
        return phi(d / (self.sigma * math.sqrt(2.0)))


class LoiNormaleArrondie:
    """Loi arrondie factice : normale centrée, ramenée au multiple le plus proche du pas."""
    arrondie = True

    def __init__(self, pas, echelle=1.0):
        self.pas = pas
        self.kmax = int(math.ceil(12.0 * echelle / pas))
        ks = range(-self.kmax, self.kmax + 1)
        p = [phi((k + 0.5) * pas / echelle) - phi((k - 0.5) * pas / echelle) for k in ks]
        s = sum(p)
        self.p = [x / s for x in p]
        self.cum = []
        c = 0.0
        for x in self.p:
            c += x
            self.cum.append(c)
        moy = sum(k * pas * x for k, x in zip(ks, self.p))
        self.sigma = math.sqrt(sum((k * pas - moy) ** 2 * x for k, x in zip(ks, self.p)))
        self._paliers = {}
        self._encadrantes = {}
        self.nom = "normale centrée d'échelle %s, arrondie au pas %s" % (fr(echelle, 2), fr(pas, 3))

    def _cumul(self, k):
        """P(Y <= k x pas)."""
        if k < -self.kmax:
            return 0.0
        if k > self.kmax:
            return 1.0
        return self.cum[k + self.kmax]

    def palier(self, m):
        """Aire pour tout décalage pris strictement entre m et m + 1 pas : P(Y - X <= m x pas)."""
        v = self._paliers.get(m)
        if v is None:
            v = 0.0
            base = m - self.kmax
            for i, x in enumerate(self.p):
                v += x * self._cumul(i + base)
            self._paliers[m] = v
        return v

    def saut(self, m):
        """Aire pour un décalage posé sur m pas : mi-hauteur des deux paliers voisins."""
        return 0.5 * (self.palier(m - 1) + self.palier(m))

    def aire(self, d):
        r = d / self.pas
        kr = round(r)
        if abs(r - kr) <= SUR_MULTIPLE:
            return self.saut(kr)
        return self.palier(math.floor(r))

    def encadrantes_nommees(self, a, sauts=True):
        cle = (a, sauts)
        v = self._encadrantes.get(cle)
        if v is None:
            lo, hi = -2 * self.kmax - 1, 2 * self.kmax + 1
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if self.palier(mid) >= a:
                    hi = mid
                else:
                    lo = mid
            cand = [(self.palier(hi - 1), "palier"), (self.palier(hi), "palier")]
            if sauts:
                cand.append((self.saut(hi), "saut"))
            sous = max((c for c in cand if c[0] <= a), key=lambda c: c[0])
            sur = min((c for c in cand if c[0] >= a), key=lambda c: c[0])
            v = (sous, sur)
            self._encadrantes[cle] = v
        return v

    def encadrantes(self, a, sauts=True):
        sous, sur = self.encadrantes_nommees(a, sauts)
        return sous[0], sur[0]


def raison_du_decalage(aire, a, sous, sur, c1, c2, c3, fenetre, note_active, mutation):
    """Raison d'un décalage non reçu dans une tranche arrondie : la première qui s'applique."""
    d_sous, d_sur = abs(sous - a), abs(sur - a)
    if not note_active:
        r = R1 if min(d_sous, d_sur) > fenetre else R3
        return r, [r]
    applicables = []
    if min(d_sous, d_sur) > fenetre:
        applicables.append(R1)
    if c1 and not c2:
        autre = d_sur if abs(aire - sous) <= EGAL else d_sous
        if autre <= fenetre and mutation != M5:
            applicables.append(R2)
    if not c1:
        applicables.append(R3)
    if c1 and c2 and not c3:
        applicables.append(R4)
    return (applicables[0] if applicables else SANS_RAISON), applicables


def classer_tranche(loi, aires, note_active=True, plafond=PLAFOND, mutation=None, famille_a_reseau=False):
    """Classe les trois décalages lus dans une tranche. Rend (issue, raisons applicables, sous, sur, écart)."""
    c3 = aires[0] < aires[1] < aires[2]
    rendus = []
    for r, a in enumerate(AIRES_DITES):
        aire = aires[r]
        ecart = abs(aire - a)
        sous = sur = None
        applicables = []
        if ecart <= TOLERANCE:
            issue = A
        elif loi.arrondie:
            sous, sur = loi.encadrantes(a, sauts=(mutation != M7))
            fenetre = plafond if note_active else TOLERANCE
            c1 = abs(aire - sous) <= EGAL or abs(aire - sur) <= EGAL
            c2 = ecart <= fenetre
            if note_active and (c1 or mutation == M3) and c2 and c3:
                issue = A_BIS
            else:
                issue, applicables = raison_du_decalage(aire, a, sous, sur, c1, c2, c3, fenetre, note_active, mutation)
        elif mutation == M6 and famille_a_reseau and note_active and ecart <= plafond:
            issue = A_BIS
        else:
            issue = HORS
        rendus.append((issue, applicables, sous, sur, ecart))
    return rendus


def controler(tranches, nombres, note=True, mutation=None):
    """Contrôle d'une famille : trois décalages écrits une fois, lus dans chaque tranche."""
    plafond = 0.06 if mutation == M4 else PLAFOND
    note_active = note or mutation == M8
    famille_a_reseau = any(l.arrondie for l in tranches)
    decalages = []
    for t, loi in enumerate(tranches, start=1):
        aires = [loi.aire(n * loi.sigma) for n in nombres]
        brutes = [loi.aire(n) for n in nombres]
        brutes_croissantes = brutes[0] < brutes[1] < brutes[2]
        rendus = classer_tranche(loi, aires, note_active, plafond, mutation, famille_a_reseau)
        for r, a in enumerate(AIRES_DITES):
            issue, applicables, sous, sur, ecart = rendus[r]
            # Diagnostic sous l'unité brute : à 0,005 seul (règle v3).
            brut_ok = abs(brutes[r] - a) <= TOLERANCE
            if not brut_ok and mutation == M2 and loi.arrondie and note_active:
                b_sous, b_sur = loi.encadrantes(a)
                brut_ok = ((abs(brutes[r] - b_sous) <= EGAL or abs(brutes[r] - b_sur) <= EGAL)
                           and abs(brutes[r] - a) <= plafond and brutes_croissantes)
            decalages.append(dict(tranche=t, rang=r, aire_dite=a, nombre=nombres[r], aire=aires[r],
                                  brute=brutes[r], ecart=ecart, sous=sous, sur=sur, issue=issue,
                                  brut_ok=brut_ok, loi=loi))
    tous = all(d["issue"] in RECUS for d in decalages)
    if mutation == M1 and any(d["issue"] == A_BIS for d in decalages):
        tous = True
    raison = None
    if tous:
        famille = CONVERTIE
    elif all(d["brut_ok"] for d in decalages):
        famille = BRUTE
        for d in decalages:
            if d["issue"] not in RECUS:
                d["issue"] = NON_RECU
    else:
        famille = ILLISIBLE
        raisons = [d["issue"] for d in decalages if d["issue"] not in RECUS]
        if SANS_RAISON in raisons:
            raison = SANS_RAISON
        else:
            raison = next((x for x in (R1, R2, R3) if x in raisons), R3)
    return dict(decalages=decalages, famille=famille, raison=raison)


def ligne_du_decalage(d):
    txt = "    tranche %d, aire dite %s : nombre écrit %s ; aire réalisée %s (écart %s)" % (
        d["tranche"], fr(d["aire_dite"], 2), fr(d["nombre"]), fr(d["aire"]), fr(d["ecart"]))
    if d["sous"] is not None:
        (s, ns), (u, nu) = d["loi"].encadrantes_nommees(d["aire_dite"])
        txt += " ; aires encadrantes %s (%s) et %s (%s)" % (fr(s), ns, fr(u), nu)
    txt += " ; sous l'unité brute %s" % fr(d["brute"])
    return txt + " -> " + d["issue"]


def montrer(nom, nature, construction, prediction, tranches, nombres, attendu, note=True):
    res = controler(tranches, nombres, note=note)
    print("=== %s (%s)" % (nom, nature))
    print("  construction : " + construction)
    for t, loi in enumerate(tranches, start=1):
        print("  tranche %d : %s ; écart type %s" % (t, loi.nom, fr(loi.sigma)))
    print("  note d'écart scellée reçue par le contrôle : %s" % ("oui" if note else "non"))
    print("  prédit : " + prediction)
    for d in res["decalages"]:
        print(ligne_du_decalage(d))
    print("  rendu, famille : %s%s" % (res["famille"], (" ; raison : " + res["raison"]) if res["raison"] else ""))
    cas_reseau = sum(1 for d in res["decalages"] if d["issue"] == A_BIS)
    ecarts = sum(1 for d in res["decalages"] if d["issue"] == A and d["ecart"] > SEUIL_NOMME)
    print("  cas nommés « conforme au pas du réseau » : %d ; écarts de plus de 0,001 parmi les conformes à 0,005 : %d"
          % (cas_reseau, ecarts))
    rendu = [[d["issue"] for d in res["decalages"] if d["tranche"] == t] for t in (1, 2, 3)]
    tenue = (res["famille"] == attendu["famille"] and res["raison"] == attendu["raison"]
             and rendu == [list(x) for x in attendu["decalages"]]
             and cas_reseau == attendu["cas_reseau"]
             and (attendu.get("ecarts") is None or ecarts == attendu["ecarts"]))
    print("  PRÉDICTION %s" % ("TENUE" if tenue else "MANQUÉE"))
    if not tenue:
        print("    attendu, famille : %s ; raison : %s ; cas : %s ; écarts : %s" % (
            attendu["famille"], attendu["raison"], attendu["cas_reseau"], attendu.get("ecarts")))
        print("    attendu, décalages : %s" % attendu["decalages"])
    print()
    return tenue


def balayage(lois, loi_continue):
    """Tous les triplets de nombres d'une grille, dans une tranche : les raisons couvrent-elles tout ?"""
    print("=== Balayage : exhaustivité des raisons et garde d'ordre")
    total = sans_raison = ordre_seul = bis_sur_continue = 0
    comptes = {}
    for loi in lois:
        nombres = [i * 0.1 for i in range(0, 31)]
        k = 1
        while k * loi.pas / loi.sigma <= 3.0:
            nombres.append(k * loi.pas / loi.sigma)
            k += 1
        aires = [loi.aire(n * loi.sigma) for n in nombres]
        n = len(nombres)
        triplets = 0
        for i in range(n):
            for j in range(n):
                for l in range(n):
                    rendus = classer_tranche(loi, (aires[i], aires[j], aires[l]))
                    issues = [x[0] for x in rendus]
                    triplets += 1
                    for issue, applicables, _s, _u, _e in rendus:
                        comptes[issue] = comptes.get(issue, 0) + 1
                        if issue not in RECUS and not applicables:
                            sans_raison += 1
                    if R4 in issues and not any(x in (R1, R2, R3) for x in issues):
                        ordre_seul += 1
        total += triplets
        print("  %s : %d nombres, %d triplets" % (loi.nom, n, triplets))
    nombres = [i * 0.05 for i in range(0, 61)]
    aires = [loi_continue.aire(x * loi_continue.sigma) for x in nombres]
    continus = 0
    for i in range(len(nombres)):
        for j in range(len(nombres)):
            for l in range(0, len(nombres), 4):
                rendus = classer_tranche(loi_continue, (aires[i], aires[j], aires[l]))
                continus += 1
                if any(x[0] == A_BIS for x in rendus):
                    bis_sur_continue += 1
    print("  %s : %d triplets" % (loi_continue.nom, continus))
    print("  décalages classés sur les tranches arrondies, par issue :")
    for cle in (A, A_BIS, R1, R2, R3, R4, SANS_RAISON):
        print("    %s : %d" % (cle, comptes.get(cle, 0)))
    print("  prédit : aucun décalage non reçu sans raison ; la raison d'ordre jamais seule dans une tranche ;"
          " aucun « conforme au pas du réseau » sur la loi continue")
    print("  rendu : décalages non reçus sans raison : %d ; tranches où la raison d'ordre est seule : %d ;"
          " triplets de la loi continue avec un « conforme au pas du réseau » : %d"
          % (sans_raison, ordre_seul, bis_sur_continue))
    tenue = sans_raison == 0 and ordre_seul == 0 and bis_sur_continue == 0
    print("  PRÉDICTION %s (%d triplets sur réseau)" % ("TENUE" if tenue else "MANQUÉE", total))
    print()
    return tenue


def main():
    print("Épreuve sur réseau factice du projet de note d'écart v2 et de la règle v3 — illustration, non opposable")
    print("Aires dites %s ; tolérance %s ; seuil des écarts nommés %s ; plafond %s ; égalité à %s près"
          % (", ".join(fr(a, 2) for a in AIRES_DITES), fr(TOLERANCE, 3), fr(SEUIL_NOMME, 3), fr(PLAFOND, 2), "1e-9"))
    print()

    # Recoupement du réseau factice avec l'illustration du concepteur et l'épreuve du contre-lecteur.
    reference = {
        0.1: ((0.6895, 0.7020), (0.7919, 0.8017), (0.9479, 0.9517)),
        0.25: ((0.6705, 0.7011), (0.7865, 0.8104), (0.9433, 0.9532)),
        0.5: ((0.6355, 0.7011), (0.7557, 0.8104), (0.9433, 0.9584)),
        1.0: ((0.6355, 0.7430), (0.7430, 0.8506), (0.9045, 0.9584)),
        2.0: ((0.5000, 0.7578), (0.7578, 0.8654), (0.8654, 0.9730)),
    }
    print("Réseau factice : aires encadrantes de la normale réduite arrondie")
    lois = {}
    recoupe = True
    for pas in (0.1, 0.25, 0.5, 1.0, 2.0):
        loi = LoiNormaleArrondie(pas)
        lois[pas] = loi
        morceaux = []
        for a, (rs, ru) in zip(AIRES_DITES, reference[pas]):
            (s, ns), (u, nu) = loi.encadrantes_nommees(a)
            morceaux.append("%s : %s (%s) et %s (%s)" % (fr(a, 2), fr(s), ns, fr(u), nu))
            if abs(s - rs) > 0.00005 or abs(u - ru) > 0.00005:
                recoupe = False
        print("  pas %s, écart type %s — %s" % (fr(pas, 2), fr(loi.sigma), " ; ".join(morceaux)))
    print("  prédit : ces aires recoupent, à 0,00005 près, celles de l'illustration du concepteur et de l'épreuve"
          " du contre-lecteur")
    print("  PRÉDICTION %s" % ("TENUE" if recoupe else "MANQUÉE"))
    print()

    continue_1 = LoiNormale(1.0)
    l10, l25, l50, l100 = lois[0.1], lois[0.25], lois[0.5], lois[1.0]
    l2_50 = LoiNormaleArrondie(0.5, echelle=2.0)
    l2_fin = LoiNormaleArrondie(0.001, echelle=2.0)
    continus = [nombre_continu(a) for a in AIRES_DITES]

    objets = []

    objets.append(("SAIN 1", "vrai par construction",
                   "famille à trois tranches continues d'échelles différentes, décalages exacts",
                   "neuf décalages conformes à 0,005 près ; famille convertie ; la note ne joue pas",
                   [LoiNormale(1.0), LoiNormale(2.0), LoiNormale(0.5)], continus,
                   dict(famille=CONVERTIE, raison=None, decalages=[[A, A, A]] * 3, cas_reseau=0, ecarts=0), True))

    objets.append(("SAIN 2", "vrai par construction",
                   "trois tranches arrondies au pas 0,25 ; décalages qu'un auteur tire de la loi continue",
                   "dans chaque tranche, 0,69 et 0,80 au pas du réseau (0,6705 et 0,7865), 0,95 conforme ;"
                   " famille convertie ; six cas nommés",
                   [l25, l25, l25], [0.7012, 1.1902, 2.3262],
                   dict(famille=CONVERTIE, raison=None, decalages=[[A_BIS, A_BIS, A]] * 3, cas_reseau=6, ecarts=3), True))

    objets.append(("SAIN 3", "vrai par construction",
                   "famille à tranches mêlées : une continue, une arrondie au pas 0,25, une au pas 0,1 ; mêmes décalages",
                   "tranche continue conforme ; dans chaque tranche arrondie, 0,69 et 0,80 au pas du réseau ;"
                   " famille convertie ; quatre cas nommés",
                   [continue_1, l25, l10], [0.7012, 1.1902, 2.3262],
                   dict(famille=CONVERTIE, raison=None,
                        decalages=[[A, A, A], [A_BIS, A_BIS, A], [A_BIS, A_BIS, A]], cas_reseau=4, ecarts=2), True))

    objets.append(("ARTEFACT 1", "faux par construction ; objet FAUX 5 du contre-lecteur",
                   "pas 0,25 ; 0,69 reçu au pas du réseau, 0,80 un palier trop loin (0,8342)",
                   "0,80 non reçu, « aucune unité ne réalise les aires » ; famille non convertie, bien qu'un"
                   " décalage soit reçu au pas du réseau",
                   [l25, l25, l25], [0.7012, 1.3714, 2.3688],
                   dict(famille=ILLISIBLE, raison=R3, decalages=[[A_BIS, R3, A]] * 3, cas_reseau=3), True))

    objets.append(("ARTEFACT 2", "faux par construction ; objet FAUX 3 du contre-lecteur",
                   "pas 0,5 ; pour 0,69 l'aire encadrante du dessous (0,6355, à 0,0545), alors que celle du dessus"
                   " (0,7011) est à 0,0111",
                   "0,69 non reçu, « aire encadrante hors du plafond » ; famille non convertie",
                   [l50, l50, l50], [0.5 / l50.sigma, 1.2372, 2.2269],
                   dict(famille=ILLISIBLE, raison=R2, decalages=[[R2, A_BIS, A_BIS]] * 3, cas_reseau=6), True))

    objets.append(("ARTEFACT 3", "faux par construction ; objet FAUX 1 du contre-lecteur",
                   "pas 0,1 ; pour 0,69 le palier voisin (0,6771), à 0,0129 mais non encadrant",
                   "0,69 non reçu, « aucune unité ne réalise les aires » ; famille non convertie",
                   [l10, l10, l10], [0.6497, 1.1902, 2.3262],
                   dict(famille=ILLISIBLE, raison=R3, decalages=[[R3, A_BIS, A]] * 3, cas_reseau=3), True))

    objets.append(("ARTEFACT 4", "faux par construction",
                   "pas 1 : aucune aire atteignable à 0,02 de 0,69 ni de 0,80",
                   "0,69 et 0,80 non reçus, « réseau trop grossier pour l'aire dite » ; 0,95 au pas du réseau ;"
                   " famille non convertie",
                   [l100, l100, l100], [0.7012, 1.1902, 2.3262],
                   dict(famille=ILLISIBLE, raison=R1, decalages=[[R1, R1, A_BIS]] * 3, cas_reseau=3), True))

    objets.append(("ARTEFACT 5", "faux par construction ; unité brute, facteur d'écart type écrit",
                   "échelle 2 arrondie au pas 0,5 ; nombres écrits en unité brute (nombre en écarts types x écart type)",
                   "sous la lecture en écarts types, trois décalages non reçus ; sous l'unité brute, 0,69 et 0,80 hors de"
                   " 0,005 : pas d'« unité brute constatée » ; famille non lisible, non convertie",
                   [l2_50, l2_50, l2_50], [x * l2_50.sigma for x in continus],
                   dict(famille=ILLISIBLE, raison=R3, decalages=[[R3, R3, R3]] * 3, cas_reseau=0), True))

    objets.append(("ARTEFACT 6", "faux par construction ; unité brute sur réseau fin",
                   "échelle 2 arrondie au pas 0,001 ; nombres écrits en unité brute",
                   "sous l'unité brute, les trois aires à 0,005 près dans les trois tranches : « unité brute constatée »,"
                   " comme aujourd'hui ; non convertie ; aucune raison de la note ne s'y ajoute",
                   [l2_fin, l2_fin, l2_fin], [x * l2_fin.sigma for x in continus],
                   dict(famille=BRUTE, raison=None, decalages=[[NON_RECU] * 3] * 3, cas_reseau=0), True))

    objets.append(("ARTEFACT 7", "faux par construction ; tranches mêlées",
                   "une tranche continue où les décalages réalisent les aires dites plus 0,01 ; deux tranches arrondies"
                   " au pas 0,25 où les mêmes décalages sont reçus",
                   "tranche continue : trois décalages hors de 0,005, la tolérance du réseau n'y passe pas ;"
                   " famille non convertie",
                   [continue_1, l25, l25], [nombre_continu(a + 0.01) for a in AIRES_DITES],
                   dict(famille=ILLISIBLE, raison=R3,
                        decalages=[[HORS, HORS, HORS], [A_BIS, A_BIS, A], [A_BIS, A_BIS, A]], cas_reseau=4), True))

    objets.append(("ARTEFACT 8", "faux par construction ; garde d'ordre",
                   "pas 0,25 ; le décalage de 0,80 réalise la même aire que celui de 0,69 (0,6705)",
                   "0,80 non reçu, « aucune unité ne réalise les aires » ; 0,69 non reçu, « aires non croissantes dans"
                   " la tranche » ; la raison d'ordre n'est pas seule ; famille non convertie",
                   [l25, l25, l25], [0.7012, 0.6000, 2.3688],
                   dict(famille=ILLISIBLE, raison=R3, decalages=[[R4, R3, A]] * 3, cas_reseau=0), True))

    objets.append(("ARTEFACT 9", "faux par construction ; note non reçue",
                   "la famille du SAIN 2, le contrôle ne recevant pas l'empreinte de la note",
                   "0,005 partout : 0,69 et 0,80 non reçus, « réseau trop grossier pour l'aire dite » lu à 0,005 ;"
                   " aucun cas au pas du réseau ; famille non convertie",
                   [l25, l25, l25], [0.7012, 1.1902, 2.3262],
                   dict(famille=ILLISIBLE, raison=R1, decalages=[[R1, R1, A]] * 3, cas_reseau=0), False))

    objets.append(("ARTEFACT 10", "faux par construction ; palier au-delà de la mi-hauteur",
                   "pas 0,1 ; pour 0,80 le palier du dessus (0,8115, à 0,0115), que la valeur de saut 0,8017 sépare"
                   " de l'aire dite",
                   "0,80 non reçu, « aucune unité ne réalise les aires » ; famille non convertie",
                   [l10, l10, l10], [0.7497, 1.2495, 2.3490],
                   dict(famille=ILLISIBLE, raison=R3, decalages=[[A_BIS, R3, A]] * 3, cas_reseau=3), True))

    tenues = 0
    par_nom = {}
    for nom, nature, construction, prediction, tranches, nombres, attendu, note in objets:
        par_nom[nom] = (tranches, nombres, note)
        if montrer(nom, nature, construction, prediction, tranches, nombres, attendu, note):
            tenues += 1

    # Mutations : (mutation, objet qui doit la voir, issue de famille prédite sous mutation, raison prédite).
    mutations = [
        (M1, "ARTEFACT 1", CONVERTIE, None),
        (M2, "ARTEFACT 5", BRUTE, None),
        (M3, "ARTEFACT 3", CONVERTIE, None),
        (M4, "ARTEFACT 2", CONVERTIE, None),
        (M5, "ARTEFACT 2", ILLISIBLE, SANS_RAISON),
        (M6, "ARTEFACT 7", CONVERTIE, None),
        (M7, "ARTEFACT 10", CONVERTIE, None),
        (M8, "ARTEFACT 9", CONVERTIE, None),
    ]
    print("=== Mutations : chaque correction défaite doit être vue par un objet")
    vues = 0
    for mutation, nom, famille_predite, raison_predite in mutations:
        tranches, nombres, note = par_nom[nom]
        sans = controler(tranches, nombres, note=note)
        avec = controler(tranches, nombres, note=note, mutation=mutation)
        change = (avec["famille"], avec["raison"]) != (sans["famille"], sans["raison"])
        tenue = change and avec["famille"] == famille_predite and avec["raison"] == raison_predite
        if tenue:
            vues += 1
        print("  mutation : %s" % mutation)
        print("    objet : %s ; sans la mutation : %s%s ; avec : %s%s" % (
            nom, sans["famille"], (" (" + sans["raison"] + ")") if sans["raison"] else "",
            avec["famille"], (" (" + avec["raison"] + ")") if avec["raison"] else ""))
        print("    prédit avec la mutation : %s%s — %s" % (
            famille_predite, (" (" + raison_predite + ")") if raison_predite else "",
            "MUTATION VUE, PRÉDICTION TENUE" if tenue else "PRÉDICTION MANQUÉE"))
    print()

    balayage_tenu = balayage([l10, l25, l50, l100, lois[2.0], l2_50, LoiNormaleArrondie(1.0, echelle=2.0)],
                             continue_1)

    print("=== Bilan")
    print("  réseau factice recoupé : %s" % ("oui" if recoupe else "non"))
    print("  objets dont la prédiction est tenue : %d sur %d" % (tenues, len(objets)))
    print("  mutations vues comme prédit : %d sur %d" % (vues, len(mutations)))
    print("  balayage : %s" % ("prédiction tenue" if balayage_tenu else "prédiction manquée"))
    tout = recoupe and tenues == len(objets) and vues == len(mutations) and balayage_tenu
    print("  ensemble : %s" % ("toutes les prédictions tenues" if tout else "au moins une prédiction manquée"))
    return 0 if tout else 1


if __name__ == "__main__":
    sys.exit(main())
