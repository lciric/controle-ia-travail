"""Caractéristiques opératoires des règles de lecture du brouillon 3 du préenregistrement
« identification semi-réelle » (loi binomiale exacte, intervalles de Wilson à 95 %),
arithmétique de budget, de condition de rang (théorème 1 de Khemakhem et collègues 2020)
et de l'échelle de définitions de la variable auxiliaire u.
Copie adaptée du script du brouillon 2 : les paragraphes 1 à 14 sont repris sans changement
de calcul (sortie identique au bit près à celle du brouillon 2 pour ces paragraphes) ;
les paragraphes 15 à 20 sont nouveaux (traitement de la contre-lecture CS2).
Aucun tirage aléatoire, aucune donnée lue : calcul déterministe, reproductible au bit près.
Les temps unitaires des paragraphes 12 et 18 sont des hypothèses de l'auteur (SUPPOSÉ), non des mesures.
Usage : python3 -I calcul-regles-identification-semi-reel-v1-brouillon3.py
Mode de contrôle (n'écrit rien, ne fait pas partie de la sortie empreintée) :
  python3 -I calcul-regles-identification-semi-reel-v1-brouillon3.py problemes CHEMIN_DU_BROUILLON
  appelle `controle_ia.prereg.problemes` du dépôt (lecture seule du brouillon) et imprime la liste.
"""
import sys
from math import comb, sqrt, erf, exp
from pathlib import Path

if len(sys.argv) >= 3 and sys.argv[1] == "problemes":
    racine = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes
    liste = problemes(sys.argv[2])
    print(f"problemes({sys.argv[2]}) : {len(liste)} problème(s)")
    for p in liste:
        print(f"  - {p}")
    sys.exit(0)

Z = 1.959963984540054  # quantile 0,975 de la loi normale


def wilson(x, n, z=Z):
    p = x / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    demi = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return centre - demi, centre + demi


def pmf(x, n, p):
    return comb(n, x) * p ** x * (1 - p) ** (n - x)


def proba(n, p, garde):
    return sum(pmf(x, n, p) for x in range(n + 1) if garde(x))


def phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


# ---------------------------------------------------------------- paragraphes repris du brouillon 1
print("§ 1 — règle de recouvrement : borne basse de Wilson à 95 % >= 0,70 (n = 100 mondes)")
n = 100
xmin = min(x for x in range(n + 1) if wilson(x, n)[0] >= 0.70)
print(f"  plus petit nombre de mondes réussis : {xmin} sur {n} (part {xmin / n:.2f})")
for p in (0.60, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95):
    print(f"  recouvrement vrai {p:.2f} : probabilité que la règle tienne = {proba(n, p, lambda x: x >= xmin):.3f}")
for p in (0.85, 0.90, 0.95):
    q = proba(n, p, lambda x: x >= xmin)
    print(f"  conjonction de 4 règles (R et O, beta moyen et fort), recouvrement vrai {p:.2f} partout : {q ** 4:.3f}")

print("§ 2 — règle d'erreur par affectation, beta = 0 (n = 100) : borne haute de Wilson <= 0,15")
xmax = max(x for x in range(n + 1) if wilson(x, n)[1] <= 0.15)
print(f"  plus grand nombre de mondes en erreur : {xmax} sur {n}")
for p in (0.01, 0.05, 0.08, 0.10, 0.15, 0.20):
    q = proba(n, p, lambda x: x <= xmax)
    print(f"  erreur vraie {p:.2f} : règle tenue = {q:.3f} ; sur les 3 affectations (indépendantes) = {q ** 3:.3f}")

print("§ 3 — règle d'erreur sur leurre et jumeau, regroupée par affectation (n = 400 : 4 tailles d'effet) : borne haute <= 0,10")
n4 = 400
xmax4 = max(x for x in range(n4 + 1) if wilson(x, n4)[1] <= 0.10)
print(f"  plus grand nombre de mondes en erreur : {xmax4} sur {n4} (part {xmax4 / n4:.4f})")
for p in (0.01, 0.03, 0.05, 0.07, 0.08, 0.10, 0.12):
    q = proba(n4, p, lambda x: x <= xmax4)
    print(f"  erreur vraie {p:.2f} : règle tenue = {q:.3f} ; leurre et jumeau sur 3 affectations (6 règles indépendantes) = {q ** 6:.3f}")

print("§ 4 — volet B : écart apparié iVAE - réseau libre sur 50 mondes ; règle : estimation >= 0,15 et borne basse > 0")
for sd in (0.10, 0.15, 0.25):
    se = sd / sqrt(50)
    for vrai in (0.05, 0.10, 0.15, 0.20, 0.30):
        p_est = 1 - phi((0.15 - vrai) / se)
        p_lb = 1 - phi((Z * se - vrai) / se)
        print(f"  écart-type des écarts {sd:.2f} (erreur type {se:.4f}) ; écart vrai {vrai:.2f} : P(estimation >= 0,15) = {p_est:.3f} ; P(borne basse > 0) = {p_lb:.3f}")

print("§ 5 — volet B : part de mondes avec corrélation au facteur vrai >= 0,70, règle borne basse de Wilson >= 0,60 (n = 50)")
n5 = 50
xmin5 = min(x for x in range(n5 + 1) if wilson(x, n5)[0] >= 0.60)
print(f"  plus petit nombre de mondes réussis : {xmin5} sur {n5} (part {xmin5 / n5:.2f})")
for p in (0.50, 0.60, 0.70, 0.75, 0.80, 0.90):
    print(f"  part vraie {p:.2f} : règle tenue = {proba(n5, p, lambda x: x >= xmin5):.3f}")

print("§ 6 — volet B regroupé (Bv0 + Bv1 : n = 100) : part de mondes avec corrélation au facteur vrai >= 0,70, règle borne basse de Wilson >= 0,60")
n6 = 100
xmin6 = min(x for x in range(n6 + 1) if wilson(x, n6)[0] >= 0.60)
print(f"  plus petit nombre de mondes réussis : {xmin6} sur {n6} (part {xmin6 / n6:.2f})")
for p in (0.60, 0.65, 0.70, 0.75, 0.80, 0.90):
    print(f"  part vraie {p:.2f} : règle tenue = {proba(n6, p, lambda x: x >= xmin6):.3f}")

print("§ 7 — jugeabilité du leurre : part d'erreur du prédicteur associatif sur le leurre, regroupée sous R (n = 400) ; règle estimation >= 0,20")
for p in (0.10, 0.15, 0.18, 0.20, 0.25, 0.30):
    print(f"  part vraie {p:.2f} : règle tenue = {proba(n4, p, lambda x: x >= 80):.3f}")

print("§ 8 — ordre de grandeur de la détection (approximation normale, SUPPOSÉ) : 30 000 paires-années, 10 % traitées, effet beta en écarts-types de la sortie annuelle, sortie cumulée sur 3 ans (écart-type multiplié par racine de 3)")
for beta in (0.1, 0.2, 0.4):
    se = sqrt(1 / 3000 + 1 / 27000)
    z = (beta / sqrt(3)) / se
    print(f"  beta = {beta:.1f} : statistique de test attendue {z:.1f}")

# ---------------------------------------------------------------- paragraphes nouveaux du brouillon 2
print("§ 9 — condition à effet négatif R2- (S20) : la règle de recouvrement de S9 s'y applique avec le signe négatif ; conjonction de 5 règles (R2, R3, O2, O3, R2-)")
for p in (0.80, 0.85, 0.90, 0.95):
    q = proba(n, p, lambda x: x >= xmin)
    print(f"  recouvrement vrai {p:.2f} partout : 4 règles = {q ** 4:.3f} ; 5 règles = {q ** 5:.3f}")
for p_moins in (0.70, 0.75, 0.80):
    q85 = proba(n, 0.85, lambda x: x >= xmin)
    qm = proba(n, p_moins, lambda x: x >= xmin)
    print(f"  recouvrement vrai 0.85 en R2, R3, O2, O3 et {p_moins:.2f} en R2- (détection asymétrique) : 5 règles = {q85 ** 4 * qm:.3f}")

print("§ 10 — condition de rang du théorème 1 (Khemakhem et collègues 2020, p. 5) : au moins n*k + 1 valeurs distinctes de la variable auxiliaire")
for (nn, kk) in ((5, 2), (5, 1), (6, 2)):
    print(f"  n = {nn} sources, k = {kk} statistiques suffisantes par source : n*k + 1 = {nn * kk + 1} ; marge recommandée 2*(n*k + 1) = {2 * (nn * kk + 1)}")
print("  valeurs distinctes de u selon sa définition (E environnements, P années de panel, référence 5 ans, tau_max = 3) :")
for (E, P) in ((3, 12), (3, 16), (3, 20), (4, 12), (5, 20), (6, 12)):
    fenetre = P - 5 - 3
    post_ref = P - 5
    blocs5 = -(-fenetre // 5)  # blocs de cinq ans entamés dans la fenêtre
    print(f"  E = {E}, P = {P} : fenêtre {fenetre} ans ; u = E x bloc de 5 ans (fenêtre) : {E * blocs5} ; u = E x année (fenêtre) : {E * fenetre} ; u = E x année (après la référence) : {E * post_ref}")

print("§ 11 — volet B regroupé à 30 mondes par condition (Bv0 + Bv1 : n = 60) : règle borne basse de Wilson >= 0,60")
n11 = 60
xmin11 = min(x for x in range(n11 + 1) if wilson(x, n11)[0] >= 0.60)
print(f"  plus petit nombre de mondes réussis : {xmin11} sur {n11} (part {xmin11 / n11:.3f})")
for p in (0.60, 0.65, 0.70, 0.75, 0.80, 0.90):
    print(f"  part vraie {p:.2f} : règle tenue = {proba(n11, p, lambda x: x >= xmin11):.3f}")

print("§ 12 — budget de processeur (temps unitaires SUPPOSÉS : 1,5 min par monde du volet A, 1,0 min par variante d'échelle d'un monde, 1,0 min par entraînement d'autoencodeur)")
T_A, T_ECH, T_ENTR = 1.5, 1.0, 1.0
mondes_A = 12 * 100 + 100 + 4 * 50          # 12 conditions de décision, R2-, D1 à D4
echelles = 13 * 30 * 2                        # 13 conditions du volet A (R2- compris), 30 mondes, 2 variantes en plus de la brute
for (nom, b_theta, b_hors) in (("option 1 (B hors théorème seul, 50 mondes par condition)", 0, 200),
                               ("option 2 (B-thêta 50 par condition + B hors théorème 30 par condition)", 200, 120),
                               ("option 2 réduite (B-thêta 50 + B hors théorème 20)", 200, 80)):
    for s in (2, 3, 5, 10):
        entr = (b_theta + b_hors) * 2 * s     # M4 et M5, s graines chacune
        sous_etude = 2 * 50 * 2               # 2 mondes, 50 graines, M4 et M5
        total = mondes_A * T_A + echelles * T_ECH + (entr + sous_etude) * T_ENTR
        print(f"  {nom}, {s} graines : volet A {mondes_A * T_A / 60:.1f} h ; échelles {echelles * T_ECH / 60:.1f} h ; volet B {entr * T_ENTR / 60:.1f} h ; sous-étude 50 graines {sous_etude * T_ENTR / 60:.1f} h ; total {total / 60:.1f} h")

print("§ 13 — stabilité entre graines : nombre de paires de graines comparées par monde")
for s in (2, 3, 5, 10, 50):
    print(f"  {s} graines : {s * (s - 1) // 2} paires")

print("§ 14 — Campos et collègues 2018 (fiche p. 17, art. 1011, note 21) : taux de base dyadique 3 828 / 86 068 533")
print(f"  taux = {3828 / 86068533:.6%} (la fiche arrondit à 0,004 %)")
print("  nombre de dyades nécessaires pour attendre k collaborations au taux de base :")
for k in (10, 100, 1000):
    print(f"  k = {k} : {k / (3828 / 86068533):,.0f} dyades".replace(",", " "))

# ---------------------------------------------------------------- paragraphes nouveaux du brouillon 3
print("§ 15 — échelle de définitions de u pour B-thêta (CS2-07, CS2-08, DL-8) : première définition qui atteint le seuil de S19 (22 valeurs)")
print("  u1 = environnement x année après la référence ; u2 = environnement x année du panel entier ; u3 = u2 x moitié de paires (parité du rang de la paire)")
SEUIL_U = 22
for (E, P) in ((3, 12), (3, 13), (3, 16), (3, 20), (4, 12), (5, 20), (6, 12), (2, 12)):
    u1, u2, u3 = E * (P - 5), E * P, 2 * E * P
    choix = next((nom for nom, v in (("u1", u1), ("u2", u2), ("u3", u3)) if v >= SEUIL_U), "aucune : B-thêta non exécutée")
    print(f"  E = {E}, P = {P} : u1 = {u1} ; u2 = {u2} ; u3 = {u3} ; définition retenue : {choix}")

print("§ 16 — étape d'effet du volet B-thêta (CS2-13) : règle de Wilson sur 50 mondes Bthêta-v1 et 50 mondes Bthêta-v0")
n16 = 50
xmin16 = min(x for x in range(n16 + 1) if wilson(x, n16)[0] >= 0.60)
print(f"  « trouve l'effet » : borne basse >= 0,60 exige au moins {xmin16} mondes sur {n16}")
for p in (0.50, 0.60, 0.70, 0.75, 0.80, 0.90):
    print(f"  part vraie {p:.2f} : règle tenue = {proba(n16, p, lambda x: x >= xmin16):.3f}")
xmax16 = max(x for x in range(n16 + 1) if wilson(x, n16)[1] <= 0.15)
print(f"  fausse détection : borne haute <= 0,15 permet au plus {xmax16} mondes sur {n16}")
for p in (0.01, 0.02, 0.05, 0.10, 0.15):
    print(f"  fausse détection vraie {p:.2f} : règle tenue = {proba(n16, p, lambda x: x <= xmax16):.3f}")
for borne in (0.10,):
    xb = [x for x in range(n16 + 1) if wilson(x, n16)[1] <= borne]
    print(f"  pour mémoire, borne haute <= {borne:.2f} sur {n16} mondes : " + (f"au plus {max(xb)} monde(s)" if xb else "aucun compte ne la tient (même 0 sur 50)"))

print("§ 17 — garde R5 de la sélection supervisée (CS2-15) : fausse détection sur base jouet, niveau nominal 0,01")
n17a, x17a = 200, 4
print(f"  ancienne garde ({n17a} répétitions, au plus {x17a} détections, soit 0,02) : fausse alarme au niveau nominal = P(X >= {x17a + 1} | 0,01) = {proba(n17a, 0.01, lambda x: x > x17a):.3f}")
n17 = 1000
xmax17 = min(x for x in range(n17 + 1) if proba(n17, 0.01, lambda y: y > x) <= 0.01)
print(f"  nouvelle garde ({n17} répétitions sur dimensions apprises synthétiques, sans entraînement) : refus si plus de {xmax17} détections")
print(f"  fausse alarme au niveau nominal 0,01 : P(X > {xmax17}) = {proba(n17, 0.01, lambda x: x > xmax17):.4f}")
for p in (0.02, 0.025, 0.03, 0.05):
    print(f"  fausse détection vraie {p:.3f} (artefact) : probabilité de détection = {proba(n17, p, lambda x: x > xmax17):.3f}")

print("§ 18 — budget (CS2-16) : décompte des mondes, validation, marge, réduction chiffrée pas à pas (temps unitaires SUPPOSÉS, comme au § 12)")
mondes_decision_A = 12 * 100 + 100
mondes_desc = 4 * 50
mondes_bt, mondes_bh = 200, 120
print(f"  mondes : volet A {mondes_decision_A} (dont R2- 100) + descriptifs D1 à D4 {mondes_desc} + B-thêta {mondes_bt} + B-hors {mondes_bh} = {mondes_decision_A + mondes_desc + mondes_bt + mondes_bh} ; plus 2 mondes rejoués de la sous-étude et 20 mondes de validation")


def budget(desc=50, bh_par_cond=30, ech=30, graines_bh=5, sous_etude_mondes=2, graines_bt=5):
    mA = mondes_decision_A + 4 * desc
    e = 13 * ech * 2
    entr = mondes_bt * 2 * graines_bt + (4 * bh_par_cond) * 2 * graines_bh
    se = sous_etude_mondes * 50 * 2
    return (mA * T_A + e * T_ECH + (entr + se) * T_ENTR) / 60


base = budget()
validation = (10 * T_A + 10 * 2 * 5 * T_ENTR) / 60     # 10 mondes du volet A, 10 mondes du volet B (2 méthodes, 5 graines)
gardes = 2.0                                           # forfait SUPPOSÉ pour les gardes sur base jouet (heures)
print(f"  option 2, 5 graines : {base:.1f} h ; validation (10 mondes A + 10 mondes B) {validation:.1f} h ; gardes (forfait SUPPOSÉ) {gardes:.1f} h ; total {base + validation + gardes:.1f} h")
for marge in (1.00, 1.25, 1.50):
    print(f"  total avec marge de relance x{marge:.2f} : {(base + validation + gardes) * marge:.1f} h")
print(f"  marge laissée par S15 = 110 h sur le seul calcul de base : {(110 / base - 1):.1%}")
etapes = (("(0) aucun", {}),
          ("(1) D1 à D4 à 30 mondes", {"desc": 30}),
          ("(2) + B-hors à 20 mondes par condition", {"desc": 30, "bh_par_cond": 20}),
          ("(3) + variantes d'échelle à 15 mondes", {"desc": 30, "bh_par_cond": 20, "ech": 15}),
          ("(4) + graines de B-hors à 3", {"desc": 30, "bh_par_cond": 20, "ech": 15, "graines_bh": 3}),
          ("(5) + sous-étude à 1 monde", {"desc": 30, "bh_par_cond": 20, "ech": 15, "graines_bh": 3, "sous_etude_mondes": 1}))
for nom, kw in etapes:
    b = budget(**kw)
    print(f"  réduction cumulée {nom} : calcul {b:.1f} h ; avec validation et gardes {b + validation + gardes:.1f} h")
b_min = budget(desc=30, bh_par_cond=20, ech=15, graines_bh=3, sous_etude_mondes=1)
print(f"  temps unitaires tolérés après réduction complète, à S15 = 110 h : multiplicateur {110 / (b_min + validation + gardes):.2f} ; à S15 = 140 h : {140 / (b_min + validation + gardes):.2f}")
print(f"  temps unitaires tolérés sans réduction : à 110 h {110 / (base + validation + gardes):.2f} ; à 140 h {140 / (base + validation + gardes):.2f}")
for h in (110, 140):
    print(f"  {h} h de temps mural = {h / 24:.1f} jours continus")

print("§ 19 — condition R2- (CS2-09) : écart R2 - R2- sous symétrie parfaite (approximation normale, 100 mondes de chaque côté)")
for p in (0.85, 0.90):
    se = sqrt(2 * p * (1 - p) / 100)
    un = 2 * (1 - phi(0.10 / se))
    print(f"  recouvrement vrai {p:.2f} des deux côtés : erreur type de l'écart {se:.4f} ; P(|écart| > 0,10) = {un:.3f} par méthode ; au moins une sur 4 méthodes = {1 - (1 - un) ** 4:.3f}")
    un30 = 2 * (1 - phi(0.30 / se))
    print(f"  même cas, déclencheur S14 (i) |écart| > 0,30 : {un30:.2e} par méthode")

print("§ 20 — arithmétique sur chiffres publiés (vérifiés à la page, voir le brouillon)")
print(f"  Campos et collègues 2018 : 0,0241 / 0,1563 = {0.0241 / 0.1563:.1%} (le papier écrit « around 16 % », p. 11)")
print(f"  Azoulay et collègues : 1 - exp(-0,092) = {1 - exp(-0.092):.2%} (note du tableau III, colonne 1a) ; 1 - exp(-0,086) = {1 - exp(-0.086):.2%} (le texte écrit 8,2 %, p. 17)")
