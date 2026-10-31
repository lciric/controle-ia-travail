"""Caractéristiques opératoires des règles de lecture du brouillon 5 du préenregistrement
« identification semi-réelle » (loi binomiale exacte, intervalles de Wilson à 95 %),
arithmétique de budget, de condition de rang (théorème 1 de Khemakhem et collègues 2020),
de l'échelle de définitions de la variable auxiliaire u, et simulations de conception.
Copie du script du brouillon 4 : les paragraphes 1 à 25 sont repris sans aucun changement
(sortie identique au bit près à celle du brouillon 4 pour ces paragraphes, vérifiable par diff) ;
les paragraphes 26 à 35 sont nouveaux (traitement de la contre-lecture finale CS4).
Aucune donnée lue. Tirages aléatoires : paragraphe 25 (repris), paragraphes 26 à 30 (simulations de
conception sur des mondes jouets entièrement synthétiques) ; graines par numpy.random.SeedSequence
(numpy >= 1.25), racine RACINE_SCRIPT = 20261031, une clé par paragraphe ; le paragraphe 28 rejoue
à l'identique l'annexe A de la contre-lecture CS4 (sa racine et sa clé, SeedSequence(20261031,
spawn_key=(901,)), sont celles de la contre-lecture) : sortie reproductible au bit près pour une même
version de numpy et de scipy.
Les temps unitaires des paragraphes 12, 18, 21 et 35 sont des hypothèses de l'auteur (SUPPOSÉ), non des
mesures ; les approximations des paragraphes 23, 25, 31 et les modèles jouets des paragraphes 26 à 30
sont nommés comme tels (SUPPOSÉ : ils montrent un mécanisme, ils ne prédisent pas la base réelle).
Usage : python3 -I calcul-regles-identification-semi-reel-v1-brouillon5.py
Mode de contrôle (n'écrit rien, ne fait pas partie de la sortie empreintée) :
  python3 -I calcul-regles-identification-semi-reel-v1-brouillon5.py problemes CHEMIN_DU_BROUILLON
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

# ---------------------------------------------------------------- paragraphes nouveaux du brouillon 4
print("§ 21 — budget du brouillon 4 (temps unitaires SUPPOSÉS comme au § 12) : ajouts D5 (rétroaction), rétrodiction inversée, variantes « graphe amputé des ponts » et « disjonction par niche », préconditions du volet B ; options de DL-10")
T_RETRO = T_ECH                                   # une variante de rétrodiction d'un monde coûte comme une variante d'échelle (SUPPOSÉ)
N_DESC = 5                                        # D1 à D5


def budget4(desc=50, bh_par_cond=30, ech=30, amp=30, niche=30, retro=30, graines_bh=5, sous_etude_mondes=2,
            graines_bt=5, bt_conf=0):
    mA = mondes_decision_A + N_DESC * desc
    e = 13 * ech * 2                              # variantes d'échelle (2 en plus de la brute), 13 conditions
    r = 7 * retro                                 # rétrodiction : R2, R3, O2, O3, H2, H3, R2- (une variante)
    a = 2 * amp + 2 * niche                       # graphe amputé des ponts et disjonction par niche (volet A) : O2, O3 (une variante chacune)
    entr = (mondes_bt + bt_conf) * 2 * graines_bt + (4 * bh_par_cond) * 2 * graines_bh
    se = sous_etude_mondes * 50 * 2
    return (mA * T_A + (e + a) * T_ECH + r * T_RETRO + (entr + se) * T_ENTR) / 60


validation4 = validation + 0.25                   # + préconditions du volet B (classifieur X -> U, rang, dérive), forfait SUPPOSÉ
gardes4 = 2.5                                     # forfait SUPPOSÉ (gardes nouvelles : rétrodiction, disjonction, effets fixes de u, D5, graphe amputé)
for nom, bt_conf in (("DL-10 option 1 (aucune condition nouvelle en B-thêta)", 0),
                     ("DL-10 option 2 (Bthêta-v0-u, 50 mondes, décision)", 50),
                     ("DL-10 option 3 (Bthêta-v0-u, 30 mondes, descriptive)", 30)):
    b = budget4(bt_conf=bt_conf)
    mondes = mondes_decision_A + N_DESC * 50 + mondes_bt + mondes_bh + bt_conf
    tot = b + validation4 + gardes4
    print(f"  {nom} : mondes {mondes} ; calcul {b:.1f} h ; validation {validation4:.2f} h ; gardes {gardes4:.1f} h ; total {tot:.1f} h ;"
          f" multiplicateur toléré à 140 h {140 / tot:.2f}, à 150 h {150 / tot:.2f}, à 160 h {160 / tot:.2f}")
print(f"  détail des ajouts (option 1) : D5 {50 * T_A / 60:.2f} h ; rétrodiction {7 * 30 * T_RETRO / 60:.2f} h ; graphe amputé {2 * 30 * T_ECH / 60:.2f} h ; disjonction par niche {2 * 30 * T_ECH / 60:.2f} h")
for nom_opt, bt_conf in (("option 1", 0), ("option 2", 50)):
    etapes4 = (("(0) aucun", {}),
               ("(1) D1 à D5 à 30 mondes", {"desc": 30}),
               ("(2) + B-hors à 20 mondes par condition", {"desc": 30, "bh_par_cond": 20}),
               ("(3) + variantes d'échelle, graphe amputé et disjonction par niche à 15 mondes", {"desc": 30, "bh_par_cond": 20, "ech": 15, "amp": 15, "niche": 15}),
               ("(4) + graines de B-hors à 3", {"desc": 30, "bh_par_cond": 20, "ech": 15, "amp": 15, "niche": 15, "graines_bh": 3}),
               ("(5) + sous-étude à 1 monde", {"desc": 30, "bh_par_cond": 20, "ech": 15, "amp": 15, "niche": 15, "graines_bh": 3, "sous_etude_mondes": 1}))
    for nom, kw in etapes4:
        b = budget4(bt_conf=bt_conf, **kw)
        print(f"  DL-10 {nom_opt}, réduction cumulée {nom} : calcul {b:.1f} h ; avec validation et gardes {b + validation4 + gardes4:.1f} h")
    b_min4 = budget4(bt_conf=bt_conf, desc=30, bh_par_cond=20, ech=15, amp=15, niche=15, graines_bh=3, sous_etude_mondes=1)
    print(f"  DL-10 {nom_opt}, multiplicateur toléré après réduction complète : à 140 h {140 / (b_min4 + validation4 + gardes4):.2f} ;"
          f" à 150 h {150 / (b_min4 + validation4 + gardes4):.2f} ; à 160 h {160 / (b_min4 + validation4 + gardes4):.2f}")
print(f"  150 h de temps mural = {150 / 24:.2f} jours continus ; 160 h = {160 / 24:.2f} jours")
print(f"  options non recommandées, pour mémoire : DL-11 option 2 (affectation F de décision, 4 tailles x 100 mondes) = {400 * T_A / 60:.1f} h ;"
      f" mondes compagnons B-thêta à une violation (4 conditions x 30 mondes x 2 méthodes x 5 graines) = {4 * 30 * 2 * 5 * T_ENTR / 60:.1f} h")

print("§ 22 — rétrodiction inversée (garde-fou 2 de R-878, S23) : règle « recouvrement rétrodit (30 mondes) >= recouvrement prospectif (100 mondes) - 0,05 », dans X2 et dans X3 (deux conditions indépendantes)")


def p_retro_rule(p_pro, p_ret, n_pro=100, n_ret=30, marge=0.05):
    tot = 0.0
    for x in range(n_pro + 1):
        px = pmf(x, n_pro, p_pro)
        seuil = x / n_pro - marge
        tot += px * sum(pmf(y, n_ret, p_ret) for y in range(n_ret + 1) if y / n_ret >= seuil - 1e-12)
    return tot


for p_pro in (0.85, 0.95):
    for p_ret in (0.05, 0.30, 0.60, 0.75, 0.85, 0.95):
        q = p_retro_rule(p_pro, p_ret)
        print(f"  prospectif vrai {p_pro:.2f}, rétrodit vrai {p_ret:.2f} : règle déclenchée dans une condition = {q:.3f} ; dans X2 et X3 = {q * q:.3f}")
n_m = 60
print(f"  déclencheur S14 (m) : rétrodiction sous affectation au hasard, R2 et R3 regroupés ({n_m} mondes), estimation >= 0,20 (au moins 12 mondes)")
for p in (0.02, 0.05, 0.10, 0.20, 0.30):
    print(f"  part rétrodite vraie {p:.2f} : déclencheur = {proba(n_m, p, lambda x: x >= 12):.3f}")

print("§ 23 — garde-fou 5 de R-878 (jeux disjoints par niche et par période) : taille de E2 dans l'étape d'effet du volet B et statistique de test approchée (approximation normale, SUPPOSÉ)")
print("  hypothèses SUPPOSÉES : 3 environnements x 1 000 paires (plafond S8 atteint) ; années utilisables = P - tau_max ; échelle des comptes (log ignoré) ;"
      " années indépendantes de même écart-type sigma_e ; beta_Z = 0,4 ; effet de z1 = beta_Z * sigma_e * 2*Phi(z1), d'écart-type beta_Z * sigma_e / racine(3)")
PAIRES = 3000
s_eff = 0.4 / sqrt(3)                             # écart-type de l'effet de z1, en sigma_e
V_bruit = 3 + 2 * s_eff ** 2                      # Y+ = somme de 3 années ; deux autres latentes tirées indépendamment y contribuent
r_part = s_eff / sqrt(s_eff ** 2 + V_bruit)
print(f"  corrélation partielle approchée de g(Y+) avec z1 : {r_part:.3f}")


def q_interne(N, grande=True):
    a, b = N // 2, N - N // 2
    k = b if grande else a
    return comb(k, 2) / comb(N, 2)


for P in (12, 20):
    Yu = P - 3
    n_b3 = 0.10 * PAIRES * Yu
    print(f"  P = {P} (années utilisables {Yu}) ; brouillon 3 (E = 20 % des paires, E2 = moitié de E par paire, toutes années) : n(E2) = {n_b3:.0f} paires-années")
    for deff in (1.0, 2.0):
        zb = r_part * sqrt(n_b3 / deff)
        print(f"    effet de plan {deff:.0f} : statistique approchée {zb:.1f} ; puissance au seuil bilatéral 0,01 = {phi(zb - 2.5758293035489) :.3f}")
    for N in (15, 45):
        for f in (0.20, 0.30, 0.40):
            q2 = q_interne(N, grande=True)
            q1 = q_interne(N, grande=False)
            n_b4 = f * q2 * PAIRES * (-(-Yu // 2))
            n_e1 = f * q1 * PAIRES * (Yu // 2)
            n_train = (1 - f) * PAIRES * P
            z1_ = r_part * sqrt(n_b4)
            z2_ = r_part * sqrt(n_b4 / 2)
            print(f"    N = {N} niches par environnement, E = {f:.0%} : part de E interne à la moitié B = {q2:.3f} (moitié A {q1:.3f}) ; n(E1) = {n_e1:.0f} ; n(E2) = {n_b4:.0f}"
                  f" ({n_b4 / n_b3:.2f} fois le brouillon 3) ; entraînement {n_train:.0f} paires-années ; statistique {z1_:.1f} (effet de plan 1), {z2_:.1f} (effet de plan 2) ;"
                  f" puissance {phi(z1_ - 2.5758293035489):.3f} / {phi(z2_ - 2.5758293035489):.3f}")

print("§ 24 — préconditions de jugeabilité du volet B (S22, synthèse v2 de la question 6, section (b)) : niveau du hasard du classifieur X -> u et seuil « hasard + 0,05 »")
for U in (21, 22, 24, 33, 36, 48, 72):
    print(f"  {U} valeurs de u : hasard = {1 / U:.4f} ; seuil d'exactitude = {1 / U + 0.05:.4f}")
print("  rang exigé de la matrice L (théorème 1, n = 5, k = 2) : n*k = 10, matrice 10 x 10, au moins n*k + 1 = 11 valeurs de u")

print("§ 25 — loi nulle de r_g (maximum sur m = 5 dimensions de la corrélation de rangs absolue avec une latente indépendante) : approximation normale et contrôle par simulation")
from statistics import NormalDist
ND = NormalDist()
for n_pts in (1000, 2700, 10200):
    x95 = ND.inv_cdf((1 + 0.95 ** (1 / 5)) / 2) / sqrt(n_pts - 1)
    print(f"  n = {n_pts} points de E : quantile 0,95 approché du maximum de 5 corrélations absolues = {x95:.4f}")
import numpy as np
RACINE_SCRIPT = 20261031
ss = np.random.SeedSequence(entropy=RACINE_SCRIPT, spawn_key=(25,))
rng = np.random.default_rng(ss)


def rangs(a):
    o = np.argsort(a, axis=0, kind="stable")
    r = np.empty_like(o, dtype=float)
    idx = np.arange(a.shape[0], dtype=float)
    for j in range(a.shape[1]):
        r[o[:, j], j] = idx
    return r


for n_pts, reps in ((1000, 2000), (2700, 1000)):
    maxima = np.empty(reps)
    for i in range(reps):
        z = rng.standard_normal((n_pts, 6))       # colonne 0 = latente vraie ; 1 à 5 = dimensions apprises indépendantes
        rz = rangs(z)
        rz -= rz.mean(axis=0)
        rz /= np.sqrt((rz ** 2).sum(axis=0))
        rho = rz[:, 1:].T @ rz[:, 0]
        maxima[i] = np.abs(rho).max()
    print(f"  simulation (numpy {np.__version__}, SeedSequence({RACINE_SCRIPT}, spawn_key=(25,)), {reps} répétitions), n = {n_pts} :"
          f" quantile 0,95 empirique = {np.quantile(maxima, 0.95):.4f} ; maximum observé = {maxima.max():.4f}")
print("  le seuil r_tilde >= 0,70 est au moins huit fois au-dessus de ces quantiles nuls (n >= 1 000)")

# ---------------------------------------------------------------- paragraphes nouveaux du brouillon 5 (contre-lecture CS4)
import time as _time  # (aucune mesure de temps n'est imprimée : la sortie reste déterministe)
Z01 = 2.5758293035489                              # quantile bilatéral 0,01


def _gen(cle):
    return np.random.default_rng(np.random.SeedSequence(entropy=RACINE_SCRIPT, spawn_key=(cle,)))


def _ols_cluster(y, X, groupes):
    """Moindres carrés avec constante ; erreurs types robustes groupées (CR1) par `groupes`."""
    n = len(y)
    Xc = np.column_stack([np.ones(n), X])
    XtX_inv = np.linalg.inv(Xc.T @ Xc)
    b = XtX_inv @ (Xc.T @ y)
    e = y - Xc @ b
    s = Xc * e[:, None]
    ug, inv = np.unique(groupes, return_inverse=True)
    S = np.zeros((len(ug), Xc.shape[1]))
    np.add.at(S, inv, s)
    G, k = len(ug), Xc.shape[1]
    V = XtX_inv @ (S.T @ S) @ XtX_inv * (G / (G - 1)) * ((n - 1) / (n - k))
    return b[1:], np.sqrt(np.diag(V))[1:]


def _centrer(x, strate):
    ug, inv = np.unique(strate, return_inverse=True)
    return x - (np.bincount(inv, weights=x) / np.bincount(inv))[inv]


def monde_jouet(rng, part_strate, beta, eta, kappa=True, fond_negatif=False, n_env=3, n_paires=1000, T=20):
    """Monde jouet du volet A (SUPPOSÉ, échelle continue g) : sortie y = niveau de strate a(e, t) + popularité
    persistante b + eta*H + bruit AR(1) + effet de C au retard 2 ; affectation au hasard avec kappa cyclique
    par (environnement, bloc de cinq ans) comme S4 du brouillon 4 ; leurre L et jumeau C0 comme S4, S5."""
    Np = n_env * n_paires
    env = np.repeat(np.arange(n_env), n_paires)
    t = np.arange(T)
    a = 0.6 * ((t - t.mean()) / t.std())[None, :] + rng.normal(0, 0.6, (n_env, 1)) + rng.normal(0, 0.5, (n_env, T))
    a = (a - a.mean()) / a.std()
    v_autre = 0.3 + 0.7 + eta ** 2
    a = a * (np.sqrt(part_strate / (1 - part_strate) * v_autre) if part_strate > 0 else 0.0)
    b = rng.normal(0, np.sqrt(0.3), Np)
    H = rng.normal(0, 1, Np)
    eps = np.empty((Np, T)); eps[:, 0] = rng.normal(0, np.sqrt(0.7), Np)
    for j in range(1, T):
        eps[:, j] = 0.5 * eps[:, j - 1] + rng.normal(0, np.sqrt(0.7 * 0.75), Np)
    nb = -(-T // 5)
    if kappa:
        kap = np.array([[[0.5, 1.0, 1.5][(e * nb + bl) % 3] for bl in range(nb)] for e in range(n_env)])
        pi = 0.10 * kap[env][:, t // 5]
    else:
        pi = np.full((Np, T), 0.10)
    C = (rng.random((Np, T)) < pi).astype(float)
    C0 = (rng.random((Np, T)) < pi).astype(float)
    L = (rng.random((Np, T)) < 1 / (1 + np.exp(-(-3 + 2.5 * C + 1.0 * H[:, None])))).astype(float)
    y = a[env] + b[:, None] + eta * H[:, None] + eps
    Cl = np.zeros_like(C); Cl[:, 2:] = C[:, :-2]
    if fond_negatif:
        y = y + abs(beta) * (1 - Cl)                # fond planté sur les non-traitées ; C le retire (effet -|beta|)
        y[:, :2] -= abs(beta)                       # pas de fond avant la première année d'affectation
    else:
        y = y + beta * Cl
    S = b[:, None] + rng.normal(0, 0.3, (Np, T))
    return dict(env=env, C=C, C0=C0, L=L, y=y, S=S, Np=Np)


def _lignes(m, t0=8, t1=16):
    Np = m["Np"]; tt = np.arange(t0, t1)
    I = np.repeat(np.arange(Np), len(tt)); Tt = np.tile(tt, Np)
    return I, Tt, m["env"][I] * 1000 + Tt


def _taux(liste):
    return float(np.mean(liste)) if liste else float("nan")


def p_s14m(p):                                   # déclencheur S14 (m) : au moins 12 sur 60 mondes
    return proba(60, min(max(p, 0.0), 1.0), lambda x: x >= 12)


print("§ 26 — CS4-01 : kappa (S4) confond C avec le niveau de la sortie par (environnement x bloc), même sous affectation au hasard ;"
      " fermeture par centrage des variables continues dans chaque strate (environnement x année) (simulation, monde jouet SUPPOSÉ)")
print("  monde jouet : 3 environnements x 1 000 paires, fenêtre de 8 années (24 000 paires-années), beta = 0, eta = 0 (pas de facteur caché :"
      " isole le chemin par kappa) ; méthode témoin = régression linéaire de Y+ sur C, L, C0, S, y_t, erreurs groupées par paire, seuil 0,01 ;"
      " « erreur » = coefficient significatif, quel que soit le signe ; 300 mondes par ligne ; part_strate = part de la variance annuelle de y due à la strate")
g26 = _gen(26)
res26 = {}
for part in (0.0, 0.05, 0.10, 0.30):
    for kap in (True, False):
        if not kap and part not in (0.10,):
            continue
        err = {(c, v): [] for c in (False, True) for v in ("C", "L", "C0")}
        for _ in range(300):
            m = monde_jouet(g26, part, 0.0, 0.0, kappa=kap)
            I, Tt, st = _lignes(m)
            Yp = m["y"][I, Tt + 1] + m["y"][I, Tt + 2] + m["y"][I, Tt + 3]
            S_, y_ = m["S"][I, Tt], m["y"][I, Tt]
            for c in (False, True):
                Yv, Sv, yv = (_centrer(Yp, st), _centrer(S_, st), _centrer(y_, st)) if c else (Yp, S_, y_)
                X = np.column_stack([m["C"][I, Tt], m["L"][I, Tt], m["C0"][I, Tt], Sv, yv])
                bb, se = _ols_cluster(Yv, X, I)
                for k, v in enumerate(("C", "L", "C0")):
                    err[(c, v)].append(abs(bb[k] / se[k]) > Z01)
        for c in (False, True):
            r = {v: _taux(err[(c, v)]) for v in ("C", "L", "C0")}
            res26[(part, kap, c)] = r
            print(f"  part_strate {part:.2f}, kappa {'cyclique' if kap else 'absent (= 1)'}, {'centrage intra-strate' if c else 'sans centrage'} :"
                  f" erreur C (ligne 4) {r['C']:.3f} ; erreur L (ligne 5) {r['L']:.3f} ; erreur C0 (ligne 6) {r['C0']:.3f}")
print("  lecture : la taille nominale est celle du monde sans niveau de strate (part 0,00) ; écart-type de Monte-Carlo d'un taux de 0,01 sur 300 mondes : 0,006")
for part in (0.05, 0.10, 0.30):
    for c in (False, True):
        r = res26[(part, True, c)]
        q4 = proba(100, min(r["C"], 1.0), lambda x: x <= 8)
        q6 = proba(400, min(r["C0"], 1.0), lambda x: x <= 28)
        print(f"  part_strate {part:.2f}, {'centrage' if c else 'sans centrage'} : règle d'erreur C de S9 en R0 (au plus 8 sur 100) tenue avec {q4:.3f} ;"
              f" règle d'erreur C0 sous R (au plus 28 sur 400) tenue avec {q6:.3f} (taux simulés pris comme vrais)")

print("§ 27 — CS4-02 : rétrodiction inversée ; définitions du brouillon 4 et du brouillon 5, cas sain et artefact de fuite (simulation, monde jouet SUPPOSÉ)")
print("  monde jouet du § 26 avec part_strate 0,10, kappa cyclique, facteur caché eta = 0,3 (agit sur toutes les années, donc sur le passé), leurre L collisionneur ;"
      " R2 : beta = 0,2 ; R3 : beta = 0,4 ; R2- : fond 0,2 retiré par C ; 300 mondes par condition ; « trouve » = coefficient de C significatif au seuil 0,01 avec le signe planté")
print("  variantes : P = prospective (Y+ sur C, L, C0, S, y_t, centrée) ; R-b4 = rétrodite du brouillon 4 (Y- = y(t-3)+y(t-2)+y(t-1), mêmes candidates, sans centrage) ;"
      " R-b4c = R-b4 centrée (L gardée) ; R-b5 = définition du brouillon 5 (centrée, L retirée) ; R-fuite = R-b5 dont la fenêtre passée reçoit y(t+2) à la place de y(t-3) (artefact) ;"
      " M2-b4 = série renversée (y(s) sur C(s+1..s+3), conditionné sur y(s+1..s+3), L(s+1..s+3), sans centrage) ; M2-b4c = idem centrée ;"
      " M2-b5 = série décalée (y(t-4) sur C(t-1..t-3), conditionné sur y(t-5..t-7), S(t-4), C0(t-1..t-3), L retirée, centrée) ; M2-fuite = M2-b5 avec y(t+2) à la place de y(t-4)")
g27 = _gen(27)
VAR27 = ("P", "R-b4", "R-b4c", "R-b5", "R-fuite", "M2-b4", "M2-b4c", "M2-b5", "M2-fuite")


def _trouve(bb, se, idx, signe):
    return any((abs(bb[k] / se[k]) > Z01) and (np.sign(bb[k]) == signe) for k in idx)


def _cause(bb, se, idx):
    return any(abs(bb[k] / se[k]) > Z01 for k in idx)


res27 = {}
for cond, beta, fond in (("R2", 0.2, False), ("R3", 0.4, False), ("R2-", 0.2, True)):
    signe = -1 if fond else 1
    acc = {v: [] for v in VAR27}; acc_any = {v: [] for v in VAR27}
    for _ in range(300):
        m = monde_jouet(g27, 0.10, beta, 0.3, fond_negatif=fond)
        I, Tt, st = _lignes(m)
        y = m["y"]; Cm, Lm, C0m, Sm = m["C"], m["L"], m["C0"], m["S"]
        Yp = y[I, Tt + 1] + y[I, Tt + 2] + y[I, Tt + 3]
        Ym = y[I, Tt - 3] + y[I, Tt - 2] + y[I, Tt - 1]
        Yf = y[I, Tt + 2] + y[I, Tt - 2] + y[I, Tt - 1]
        c_, l_, c0_, s_, yt = Cm[I, Tt], Lm[I, Tt], C0m[I, Tt], Sm[I, Tt], y[I, Tt]
        sc, ytc = _centrer(s_, st), _centrer(yt, st)
        def coupe(Yv, avecL, centre):
            Yv2 = _centrer(Yv, st) if centre else Yv
            cols = [c_] + ([l_] if avecL else []) + [c0_, sc if centre else s_, ytc if centre else yt]
            bb, se = _ols_cluster(Yv2, np.column_stack(cols), I)
            return bb, se
        out = {}
        out["P"] = coupe(Yp, True, True); out["R-b4"] = coupe(Ym, True, False); out["R-b4c"] = coupe(Ym, True, True)
        out["R-b5"] = coupe(Ym, False, True); out["R-fuite"] = coupe(Yf, False, True)
        for v in ("P", "R-b4", "R-b4c", "R-b5", "R-fuite"):
            bb, se = out[v]
            acc[v].append(_trouve(bb, se, [0], signe)); acc_any[v].append(_cause(bb, se, [0]))
        # M2 (série renversée du brouillon 4) : lignes s = Tt
        for v, centre in (("M2-b4", False), ("M2-b4c", True)):
            ys = y[I, Tt]
            cols = [Cm[I, Tt + 1], Cm[I, Tt + 2], Cm[I, Tt + 3], y[I, Tt + 1], y[I, Tt + 2], y[I, Tt + 3],
                    Lm[I, Tt + 1], Lm[I, Tt + 2], Lm[I, Tt + 3]]
            if centre:
                ys = _centrer(ys, st)
                cols = cols[:3] + [_centrer(y[I, Tt + k], m["env"][I] * 1000 + Tt + k) for k in (1, 2, 3)] + cols[6:]
            bb, se = _ols_cluster(ys, np.column_stack(cols), I)
            acc[v].append(_trouve(bb, se, [0, 1, 2], signe)); acc_any[v].append(_cause(bb, se, [0, 1, 2]))
        # M2 (série décalée du brouillon 5) et sa fuite
        def cy(k):
            return _centrer(y[I, Tt + k], m["env"][I] * 1000 + Tt + k)
        for v, cible in (("M2-b5", cy(-4)), ("M2-fuite", cy(2))):
            cols = [Cm[I, Tt - 1], Cm[I, Tt - 2], Cm[I, Tt - 3], cy(-5), cy(-6), cy(-7),
                    _centrer(Sm[I, Tt - 4], m["env"][I] * 1000 + Tt - 4), C0m[I, Tt - 1], C0m[I, Tt - 2], C0m[I, Tt - 3]]
            if v == "M2-fuite":                      # la fuite : la cible est postérieure à C(t-1..t-3) ; on garde les mêmes conditions
                cols[0:3] = [Cm[I, Tt - 1], Cm[I, Tt], Cm[I, Tt - 3]]
            bb, se = _ols_cluster(cible, np.column_stack(cols), I)
            acc[v].append(_trouve(bb, se, [0, 1, 2], signe)); acc_any[v].append(_cause(bb, se, [0, 1, 2]))
    res27[cond] = ({v: _taux(acc[v]) for v in VAR27}, {v: _taux(acc_any[v]) for v in VAR27})
    print(f"  {cond} : " + " ; ".join(f"{v} {res27[cond][0][v]:.3f} (tout signe {res27[cond][1][v]:.3f})" for v in VAR27))
print("  déclencheur S14 (m) (au moins 12 « trouve » sur 60 mondes de R2 et R3 regroupés), probabilité pour chaque variante, taux simulés pris comme vrais :")
for v in VAR27[1:]:
    p = (res27["R2"][0][v] + res27["R3"][0][v]) / 2
    print(f"  {v} : part rétrodite regroupée {p:.3f} ; S14 (m) sonne avec {p_s14m(p):.3f}")
print("  S14 (m) du brouillon 5 : R2, R3 et R2- regroupés (90 mondes), au moins 18 (part >= 0,20) ; caractéristique opératoire :")
for p in (0.01, 0.02, 0.05, 0.10, 0.20, 0.30):
    print(f"  part rétrodite vraie {p:.2f} : déclencheur = {proba(90, p, lambda x: x >= 18):.3f}")
for v in ("R-b5", "M2-b5", "R-fuite", "M2-fuite", "R-b4", "M2-b4"):
    p = (res27["R2"][0][v] + res27["R3"][0][v] + res27["R2-"][0][v]) / 3
    print(f"  {v} : part rétrodite regroupée (R2, R3, R2-) {p:.3f} ; S14 (m) du brouillon 5 sonne avec {proba(90, min(p, 1.0), lambda x: x >= 18):.3f}")
print("  même déclencheur appliqué à R2- seul (30 mondes, au moins 6) pour mémoire :")
for v in ("R-b4", "R-b4c", "R-b5", "R-fuite", "M2-b4", "M2-b4c", "M2-b5"):
    p = res27["R2-"][0][v]
    print(f"  {v} : part rétrodite R2- {p:.3f} ; au moins 6 sur 30 avec {proba(30, min(p, 1.0), lambda x: x >= 6):.3f}")

print("§ 28 — CS4-03 : rejeu exact de l'annexe A de la contre-lecture CS4 (sim_estim2.py, empreinte f6bbfad7…, 250 mondes par ligne)")
print("  copie du code de la contre-lecture ; seuls changent le nom du générateur (rng_cl) et le préfixe des lignes imprimées ; même racine et même clé")
from scipy.stats import norm as _norm
rng_cl = np.random.default_rng(np.random.SeedSequence(20261031, spawn_key=(901,)))


def demean_by(g, X):
    out = X.astype(float).copy()
    ug, inv = np.unique(g, return_inverse=True)
    cnt = np.bincount(inv)
    for j in range(X.shape[1]):
        s = np.bincount(inv, weights=X[:, j])
        out[:, j] -= (s/cnt)[inv]
    return out


def ols_t(y, Z, g, deff=1.0):
    Yd = demean_by(g, y[:, None]); Zd = demean_by(g, Z)
    XtX = Zd.T @ Zd
    beta = np.linalg.solve(XtX, Zd.T @ Yd[:, 0])
    res = Yd[:, 0] - Zd @ beta
    dof = len(y) - len(np.unique(g)) - Z.shape[1]
    s2 = (res @ res)/dof
    se = np.sqrt(np.diag(np.linalg.inv(XtX))*s2*deff)
    return beta, beta/se


def one_world(N, P, firstyear, lastyear, beta_z=0.4, fe=True, deffs=(1.0,2.0), nsel_dims=5, eff=True):
    E = 3
    npair = min(N*(N-1)//2, 1000)
    allpairs = [(i,j) for i in range(N) for j in range(i+1,N)]
    sel = rng_cl.choice(len(allpairs), size=npair, replace=False)
    pairs = np.array([allpairs[s] for s in sel])
    years = np.arange(firstyear, lastyear+1)
    res = {d: dict(trouve=0, k_ok=0, sig=0, fd=0) for d in deffs}
    rows = []
    env = np.repeat(np.arange(E), npair)
    halfA = {e: set(rng_cl.permutation(N)[:N//2]) for e in range(E)}
    inE = rng_cl.random(E*npair) < 0.40
    pi = np.tile(pairs, (E,1))
    pa = np.array([ (pi[k,0] in halfA[env[k]]) and (pi[k,1] in halfA[env[k]]) for k in range(E*npair)])
    pb = np.array([ (pi[k,0] not in halfA[env[k]]) and (pi[k,1] not in halfA[env[k]]) for k in range(E*npair)])
    nY = len(years); h1 = years[:nY//2]; h2 = years[nY//2:]
    U = E*(lastyear+1)
    mu = rng_cl.uniform(-2,2,size=(5,E,lastyear+2)); sg = rng_cl.uniform(0.5,2,size=(5,E,lastyear+2))
    out = {}
    idxE = np.where(inE & (pa|pb))[0]
    yrs_all = np.arange(firstyear-1, lastyear+2)
    z = np.empty((len(idxE), len(yrs_all), 5))
    for a,k in enumerate(idxE):
        e = env[k]
        for b,yv in enumerate(yrs_all):
            z[a,b,:] = rng_cl.normal(mu[:,e,yv], sg[:,e,yv])
    z1 = z[:,:,0]; z1t = (z1 - z1.mean())/z1.std()
    e1 = beta_z*2*_norm.cdf(z1t) if eff else np.zeros_like(z1t)
    pos = {yv:i for i,yv in enumerate(yrs_all)}
    def build(maskpairs, yrs):
        Zs=[]; ys=[]; gs=[]
        for a,k in enumerate(idxE):
            if not maskpairs[k]: continue
            for yv in yrs:
                b = pos[yv]
                y = rng_cl.normal(0, np.sqrt(3.0)) + e1[a,b-1]+e1[a,b]+e1[a,b+1]
                Zs.append(z[a,b,:]); ys.append(y); gs.append(env[k]*1000+yv)
        return np.array(ys), np.array(Zs), np.array(gs)
    y1,Z1,g1 = build(pa, h1); y2,Z2,g2 = build(pb, h2)
    out['n1']=len(y1); out['n2']=len(y2)
    if len(y1)<200 or len(y2)<200: return out
    for d in deffs:
        if fe:
            b1,t1 = ols_t(y1, Z1, g1, d)
            kh = int(np.argmax(np.abs(b1*Z1.std(axis=0))))
            b2,t2 = ols_t(y2, Z2[:,[kh]], g2, d)
        else:
            gz1=np.zeros_like(g1); gz2=np.zeros_like(g2)
            b1,t1 = ols_t(y1, Z1, gz1, d); kh=int(np.argmax(np.abs(b1*Z1.std(axis=0))))
            b2,t2 = ols_t(y2, Z2[:,[kh]], gz2, d)
        out[('k_ok',d)] = (kh==0)
        out[('sig',d)] = (abs(t2[0])>2.5758293)
        out[('trouve',d)] = (kh==0) and abs(t2[0])>2.5758293 and b2[0]>0
        out[('t2',d)] = t2[0] if kh==0 else np.nan
    return out


def run(label, N, P, first, last, reps, fe=True, eff=True):
    acc = {}; n1=[]; n2=[]; t2=[]
    for r in range(reps):
        o = one_world(N,P,first,last,fe=fe,eff=eff)
        if ('trouve',1.0) not in o: continue
        n1.append(o['n1']); n2.append(o['n2'])
        for d in (1.0,2.0):
            acc.setdefault(('trouve',d),[]).append(o[('trouve',d)])
            acc.setdefault(('k_ok',d),[]).append(o[('k_ok',d)])
            acc.setdefault(('sig',d),[]).append(o[('sig',d)])
    if not n1:
        print(f"  {label} fe={fe} eff={eff}: aucun monde utilisable (E1 ou E2 < 200 paires-annees) ; n moyen non calcule"); return
    print(f"  {label} fe={fe} eff={eff}: reps={len(n1)} n(E1)={np.mean(n1):.0f} n(E2)={np.mean(n2):.0f} | "
          + " | ".join(f"deff {int(d)}: k_ok {np.mean(acc[('k_ok',d)]):.2f} sig {np.mean(acc[('sig',d)]):.2f} trouve {np.mean(acc[('trouve',d)]):.2f}" for d in (1.0,2.0)))


run("A: P=12, u2, annees 1..9 (hyp. du brouillon 4, N=45)", 45, 12, 1, 9, 250)
run("B: P=16, u1, annees 6..13", 45, 16, 6, 13, 250)
run("C: P=20, u1, annees 6..17", 45, 20, 6, 17, 250)
run("D: P=13, u1, annees 6..10", 45, 13, 6, 10, 250)
run("E (appel ajouté par la contre-lecture, CS4-04) : N = 15 niches", 15, 12, 1, 9, 50)

print("§ 29 — CS4-03 : puissance de l'étape d'estimation avec le modèle complet de la contre-lecture (même modèle que le § 28, code vectorisé),"
      " étendu : taille de E, définition de u (u1 = années après la référence, u2 = panel entier), nombre d'environnements, qualité de la représentation r")
print("  r = corrélation entre chaque dimension apprise et sa latente (r = 1 : représentation parfaite, borne haute de la contre-lecture ; r = 0,85 : représentation"
      " réaliste, SUPPOSÉ) ; « trouve » = k_hat = k* et coefficient significatif au seuil 0,01 et signe positif ; effet de plan 1 (justifié au § 30) et 2 (sensibilité) ;"
      " 45 niches et 1 000 paires par environnement ; 500 mondes par ligne")


def monde_estimation(rng, N, first, last, Efrac=0.40, rs=(1.0,), deffs=(1.0, 2.0), beta=0.4, eff=True, nenv=3):
    npair = min(N * (N - 1) // 2, 1000)
    iu, ju = np.triu_indices(N, 1)
    sel = rng.choice(len(iu), size=npair, replace=False)
    pi_, pj_ = iu[sel], ju[sel]
    years = np.arange(first, last + 1); nY = len(years)
    h1, h2 = years[: nY // 2], years[nY // 2:]
    yall = np.arange(first - 1, last + 2)
    mu = rng.uniform(-2, 2, size=(5, nenv, last + 2)); sg = rng.uniform(0.5, 2, size=(5, nenv, last + 2))
    blocs = []
    for e in range(nenv):
        A = np.zeros(N, bool); A[rng.permutation(N)[: N // 2]] = True
        inE = rng.random(npair) < Efrac
        blocs.append((e, inE & A[pi_] & A[pj_], inE & ~A[pi_] & ~A[pj_]))
    data = {1: [], 2: []}
    for e, pa, pb in blocs:
        for lab, msk, yrs in ((1, pa, h1), (2, pb, h2)):
            k = int(msk.sum())
            if k == 0:
                continue
            z = rng.normal(mu[:, e, yall].T[None, :, :], sg[:, e, yall].T[None, :, :], size=(k, len(yall), 5))
            data[lab].append((e, z, yrs))
    out = {}
    if not data[1] or not data[2]:
        out["n1"] = out["n2"] = 0
        return out
    allz1 = np.concatenate([z[:, :, 0].ravel() for lab in (1, 2) for (_, z, _) in data[lab]])
    m1, s1 = allz1.mean(), allz1.std()
    built = {}
    for lab in (1, 2):
        Zs, ys, gs = [], [], []
        for e, z, yrs in data[lab]:
            e1 = beta * 2 * _norm.cdf((z[:, :, 0] - m1) / s1) if eff else np.zeros(z.shape[:2])
            bb = yrs - (first - 1)
            yv = rng.normal(0, np.sqrt(3.0), size=(z.shape[0], len(yrs))) + e1[:, bb - 1] + e1[:, bb] + e1[:, bb + 1]
            Zs.append(z[:, bb, :].reshape(-1, 5)); ys.append(yv.ravel()); gs.append(np.tile(e * 1000 + yrs, z.shape[0]))
        built[lab] = (np.concatenate(ys), np.concatenate(Zs), np.concatenate(gs))
    y1, Z1, g1 = built[1]; y2, Z2, g2 = built[2]
    out["n1"], out["n2"] = len(y1), len(y2)
    if len(y1) < 200 or len(y2) < 200:
        return out
    for r in rs:
        if r < 1:
            Z1r = r * Z1 + np.sqrt(1 - r * r) * Z1.std(axis=0) * rng.standard_normal(Z1.shape)
            Z2r = r * Z2 + np.sqrt(1 - r * r) * Z2.std(axis=0) * rng.standard_normal(Z2.shape)
        else:
            Z1r, Z2r = Z1, Z2
        b1, _ = ols_t(y1, Z1r, g1)
        kh = int(np.argmax(np.abs(b1 * Z1r.std(axis=0))))
        b2, t2 = ols_t(y2, Z2r[:, [kh]], g2)
        for d in deffs:
            tt = t2[0] / np.sqrt(d)
            out[(r, d)] = bool((kh == 0) and abs(tt) > Z01 and b2[0] > 0)
            out[("fd", r, d)] = bool(abs(tt) > Z01)
    return out


g29 = _gen(29)
res29 = {}
grille = [(3, P, "u2", Ef) for P in (12, 14, 15, 16, 20) for Ef in (0.4, 0.5, 0.6)] + \
         [(3, P, "u1", 0.5) for P in (16, 20)] + [(5, 12, "u2", 0.5), (5, 14, "u2", 0.5)]
for nenv, P, ud, Ef in grille:
    first = 1 if ud == "u2" else 6
    res = [monde_estimation(g29, 45, first, P - 3, Efrac=Ef, rs=(1.0, 0.85), nenv=nenv) for _ in range(500)]
    ok = [o for o in res if (1.0, 1.0) in o]
    v = {k: _taux([o[k] for o in ok]) for k in ((1.0, 1.0), (1.0, 2.0), (0.85, 1.0), (0.85, 2.0))}
    n1m, n2m = np.mean([o["n1"] for o in ok]), np.mean([o["n2"] for o in ok])
    res29[(nenv, P, ud, Ef)] = (n1m, n2m, v)
    print(f"  {nenv} env., P = {P}, {ud} (années {first} à {P - 3}), E = {Ef:.0%} : n(E1) {n1m:.0f} ; n(E2) {n2m:.0f} ;"
          f" r = 1 : {v[(1.0, 1.0)]:.2f} (plan 1) / {v[(1.0, 2.0)]:.2f} (plan 2) ; r = 0,85 : {v[(0.85, 1.0)]:.2f} / {v[(0.85, 2.0)]:.2f}")
print("  fausse détection sans effet (beta_Z = 0), mêmes réglages, 1 000 mondes, au seuil 0,01, effet de plan 1 :")
for nenv, P, Ef in ((3, 16, 0.5), (3, 12, 0.4)):
    res = [monde_estimation(g29, 45, 1, P - 3, Efrac=Ef, rs=(1.0,), deffs=(1.0,), eff=False, nenv=nenv) for _ in range(1000)]
    ok = [o for o in res if ("fd", 1.0, 1.0) in o]
    print(f"  {nenv} env., P = {P}, u2, E = {Ef:.0%} : fausse détection {_taux([o[('fd', 1.0, 1.0)] for o in ok]):.3f} ({len(ok)} mondes)")
print("  règle d'estimation de S11 (au moins 37 sur 50), probabilité de la tenir quand la part vraie est celle de la ligne (r = 0,85, plan 1) :")
for key in ((3, 12, "u2", 0.4), (3, 14, "u2", 0.5), (3, 15, "u2", 0.5), (3, 16, "u2", 0.5), (3, 16, "u2", 0.6), (3, 20, "u2", 0.5), (3, 16, "u1", 0.5), (5, 12, "u2", 0.5)):
    p = res29[key][2][(0.85, 1.0)]
    print(f"  {key[0]} env., P = {key[1]}, {key[2]}, E = {key[3]:.0%} : part vraie {p:.2f} ; règle tenue {proba(50, p, lambda x: x >= 37):.3f}")

print("§ 30 — CS4-05 et effet de plan : estimateur dyadique de la variance (toutes les paires d'observations qui partagent une niche) contre estimateur naïf,"
      " estimateur groupé par paire et estimateur « à deux voies » (première niche, seconde niche, intersection = paire) ; monde jouet SUPPOSÉ")
print("  E2 jouet : 3 environnements x 45 niches, moitié B des niches (22 ou 23), paires internes, 7 années ; sortie = composantes persistantes de niche (variance 0,3 chacune)"
      " + de paire (0,3) + strate + somme glissante de trois bruits annuels (fenêtres de Y+ chevauchantes) ; effets fixes de u = (environnement x année) ;"
      " régresseur z tiré par paire-année (cas B-thêta) ou x = v_i + v_j persistant par niche (cas artefact de la garde) ; aucun effet (beta = 0) ; 1 000 répétitions")
g30 = _gen(30)


def _var_dyad(sc, ni, nj, paire, Gn):
    Sn = np.bincount(ni, weights=sc, minlength=Gn) + np.bincount(nj, weights=sc, minlength=Gn)
    Sp = np.bincount(paire, weights=sc)
    return (Sn @ Sn - Sp @ Sp)


def _var_groupe(sc, g):
    S = np.bincount(np.unique(g, return_inverse=True)[1], weights=sc)
    return S @ S


fd30 = {(cas, est): [] for cas in ("z", "x") for est in ("naif", "paire", "deux_voies", "dyadique")}
fd_perm = {"sain": [], "artefact": []}
B_PERM = 400
ratio30 = {cas: [] for cas in ("z", "x")}
for _ in range(1000):
    ni_l, nj_l, pa_l, st_l, Ycol, zc, xc = [], [], [], [], [], [], []
    pid = 0
    for e in range(3):
        B = g30.permutation(45)[:23]
        iu, ju = np.triu_indices(len(B), 1)
        ii, jj = B[iu] + 45 * e, B[ju] + 45 * e
        npair = len(ii)
        cn = g30.normal(0, np.sqrt(0.3), 45 * 3)
        vn = g30.normal(0, 1, 45 * 3)
        bp = g30.normal(0, np.sqrt(0.3), npair)
        T = 7
        w = g30.normal(0, 0.5, T)
        bruit = g30.normal(0, 1, (npair, T + 3))
        Yp = (bruit[:, 1:T + 1] + bruit[:, 2:T + 2] + bruit[:, 3:T + 3]) + (cn[ii] + cn[jj] + bp)[:, None] + w[None, :]
        mu_u = g30.uniform(-2, 2, T); sg_u = g30.uniform(0.5, 2, T)
        z = g30.normal(mu_u[None, :], sg_u[None, :], (npair, T))
        x = (vn[ii] + vn[jj])[:, None] + 0.2 * g30.normal(0, 1, (npair, T))
        for t in range(T):
            ni_l.append(ii); nj_l.append(jj); pa_l.append(np.arange(npair) + pid); st_l.append(np.full(npair, e * 100 + t))
            Ycol.append(Yp[:, t]); zc.append(z[:, t]); xc.append(x[:, t])
        pid += npair
    ni, nj, paire, st = map(np.concatenate, (ni_l, nj_l, pa_l, st_l))
    Yraw = np.concatenate(Ycol)
    Yv = _centrer(Yraw, st)
    zraw = np.concatenate(zc)
    n_ = len(Yraw)
    ordre = np.argsort(st, kind="stable")
    rang_st = np.unique(st, return_inverse=True)[1].astype(float)
    perm_idx = np.argsort(rang_st[None, :] + g30.random((B_PERM, n_)), axis=1)
    zc_ = _centrer(zraw, st)
    stat0 = abs(zc_ @ Yv)
    statp = np.abs(zc_[perm_idx] @ Yv[ordre])
    fd_perm["sain"].append((1 + np.sum(statp >= stat0)) / (1 + B_PERM) <= 0.01)
    za, Ya = zraw - zraw.mean(), Yraw - Yraw.mean()
    stat0a = abs(za @ Ya)
    perm_all = np.argsort(g30.random((B_PERM, n_)), axis=1)
    statpa = np.abs(za[perm_all] @ Ya)
    fd_perm["artefact"].append((1 + np.sum(statpa >= stat0a)) / (1 + B_PERM) <= 0.01)
    for cas, reg in (("z", np.concatenate(zc)), ("x", np.concatenate(xc))):
        xr = _centrer(reg, st)
        bh = (xr @ Yv) / (xr @ xr)
        e_ = Yv - bh * xr
        sc = xr * e_
        n = len(Yv); dof = n - len(np.unique(st)) - 1
        v_naif = (e_ @ e_ / dof) / (xr @ xr)
        Gn = 45 * 3
        v_dy = _var_dyad(sc, ni, nj, paire, Gn) / (xr @ xr) ** 2 * (Gn / (Gn - 1))
        v_pa = _var_groupe(sc, paire) / (xr @ xr) ** 2
        v_dv = (_var_groupe(sc, ni) + _var_groupe(sc, nj) - _var_groupe(sc, paire)) / (xr @ xr) ** 2
        for est, v in (("naif", v_naif), ("paire", v_pa), ("deux_voies", v_dv), ("dyadique", v_dy)):
            fd30[(cas, est)].append(abs(bh) / np.sqrt(max(v, 1e-300)) > Z01)
        ratio30[cas].append(v_dy / v_naif)
print("  test par permutation (décision du brouillon 5) : statistique |somme de x_tilde * Y_tilde| après effets fixes de u ; 400 permutations de z dans chaque"
      " strate de u (cas sain) ; artefact de code : permutation entre strates de u, sans effets fixes, alors que mu(u) et la sortie varient avec u ; fausse détection au seuil 0,01 :")
print(f"  permutation dans les strates de u (sain) : {_taux(fd_perm['sain']):.3f} ; permutation entre strates sans effets fixes (artefact) : {_taux(fd_perm['artefact']):.3f}"
      f" ; caractéristique de la garde (1 000 répétitions, refus au-delà de 18) : niveau 0,01 -> fausse alarme 0,0069 (§ 17)")
for cas, nom in (("z", "régresseur tiré par paire-année (B-thêta)"), ("x", "régresseur persistant par niche (artefact)")):
    print(f"  {nom} : effet de plan mesuré (variance dyadique / variance naïve) médiane {np.median(ratio30[cas]):.2f}"
          f" (quantiles 0,1 et 0,9 : {np.quantile(ratio30[cas], 0.1):.2f}, {np.quantile(ratio30[cas], 0.9):.2f}) ; fausse détection au seuil 0,01 :"
          + " ; ".join(f" {est} {_taux(fd30[(cas, est)]):.3f}" for est in ("naif", "paire", "deux_voies", "dyadique")))

print("§ 31 — CS4-04 : plancher de puissance du volet A (M § 8 corrigé : dépendance au nombre de paires-années de la fenêtre de plantation)")
print("  même approximation normale SUPPOSÉE qu'au § 8 : 10 % de paires-années traitées, statistique = (beta / racine(3)) / racine(1/n_T + 1/n_C) = 0,0346 x beta/0,2 x racine(n)")
for npa in (1200, 6000, 12000, 16000, 20000, 24000, 30000, 36000):
    zz = {b_: (b_ / sqrt(3)) / sqrt(1 / (0.1 * npa) + 1 / (0.9 * npa)) for b_ in (0.1, 0.2, 0.4)}
    print(f"  {npa:>6} paires-années : statistique {zz[0.1]:.1f} (beta 0,1) ; {zz[0.2]:.1f} (0,2) ; {zz[0.4]:.1f} (0,4) ;"
          f" puissance d'un test efficace au seuil 0,01 pour beta = 0,2 : {phi(zz[0.2] - Z01):.3f}")
print("  paires-années de la fenêtre (de la 6e année à P - 3, soit P - 8 années) selon la base, et booléen du plancher (>= 20 000) :")
for (E_, paires_env, P) in ((3, 105, 12), (3, 1000, 12), (3, 1000, 14), (3, 1000, 15), (3, 1000, 16), (3, 1000, 20), (4, 1000, 13), (5, 1000, 12), (6, 1000, 12)):
    npa = E_ * paires_env * (P - 8)
    print(f"  {E_} env. x {paires_env} paires, P = {P} : {npa} paires-années ; plancher {'tenu' if npa >= 20000 else 'non tenu'}")
print("  booléen PUIS-thêta de l'étape d'estimation (comptes seulement) : n(E1) = E x q_A x paires x floor(Y/2), n(E2) = E x q_B x paires x ceil(Y/2),"
      " Y = P - 3 années utilisables (u2), q = part des paires internes à une moitié de niches ; seuils n(E1) >= 2 000 et n(E2) >= 2 600 (§ 29 : part vraie >= 0,80 à r = 0,85)")
for (E_, N_, P, Ef) in ((3, 45, 12, 0.5), (3, 45, 15, 0.5), (3, 45, 16, 0.5), (3, 45, 16, 0.4), (3, 45, 20, 0.5), (3, 45, 14, 0.6), (5, 45, 12, 0.5), (4, 45, 14, 0.5)):
    qa, qb = q_interne(N_, grande=False), q_interne(N_, grande=True)
    pa_ = min(N_ * (N_ - 1) // 2, 1000) * E_
    Yu = P - 3
    n1_, n2_ = Ef * qa * pa_ * (Yu // 2), Ef * qb * pa_ * (-(-Yu // 2))
    print(f"  {E_} env. x {N_} niches, P = {P}, E = {Ef:.0%} : n(E1) = {n1_:.0f} ; n(E2) = {n2_:.0f} ; PUIS-thêta {'vrai' if (n1_ >= 2000 and n2_ >= 2600) else 'faux'}")

print("§ 32 — CS4-07 : chaîne de la Table A (lignes 3 à 10, hors règles non chiffrées) pour des méthodes de référence nommées ; S12 réduite")


def p_s12(q, n=30, net=4, ncomp=8, chute=0.0):
    pD = sum(pmf(x, n, q + chute) * pmf(yv, n, q) for x in range(n + 1) for yv in range(n + 1) if abs(x - yv) >= net)
    return pD, 1 - (1 - pD) ** ncomp


for q in (0.02, 0.03, 0.05):
    for net, tol in ((4, "0,10"), (5, "0,15")):
        pD, _ = p_s12(q, net=net)
        print(f"  S12, bascule {q:.2f} par monde et par sens, tolérance {tol} (au moins {net} mondes nets sur 30) : par comparaison {pD:.4f} ;"
              f" 8 comparaisons (R2, R3, O2, O3 ; standardisé et redimensionné) {1 - (1 - pD) ** 8:.3f} ; 14 : {1 - (1 - pD) ** 14:.3f} ; 26 : {1 - (1 - pD) ** 26:.3f}")
for chute in (0.20, 0.30):
    pD, _ = p_s12(0.02, net=5, chute=chute)
    print(f"  S12 tolérance 0,15 : artefact réel (chute de {chute:.2f} des mondes réussis en une échelle, bascule 0,02) détecté sur une comparaison avec {pD:.3f}")
for nom, rec, err, bas, ret in (("référence A (recouvrement 0,90, erreurs 0,03, bascule 0,02, rétrodit 0,05)", 0.90, 0.03, 0.02, 0.05),
                                ("référence B (recouvrement 0,85, erreurs 0,05, bascule 0,03, rétrodit 0,10)", 0.85, 0.05, 0.03, 0.10)):
    p_art = 1 - p_s12(bas, net=5)[1]
    p_c = proba(100, err, lambda x: x <= 8)
    p_lc = proba(400, err, lambda x: x <= 28)
    p_rec = proba(100, rec, lambda x: x >= 79)
    p_ret = 1 - p_retro_rule(rec, ret) ** 2
    l3_7bis = p_art * p_c * p_lc ** 2 * p_rec ** 3
    l3_10 = l3_7bis * p_c * p_lc ** 2 * p_rec ** 2 * p_ret ** 3
    print(f"  {nom} : S12 franchie {p_art:.3f} ; ligne 4 {p_c:.3f} ; lignes 5 et 6 {p_lc ** 2:.3f} ; lignes 7 et 7bis (R2, R3, R2-) {p_rec ** 3:.3f} ;"
          f" lignes 3 à 7bis ensemble {l3_7bis:.3f} ; avec ERR_O et REC_O (O0, O2, O3, 400 mondes de O) et S23 non déclenchée (R, R-, O) : {l3_10:.3f}"
          f" (non comptés : intervention, jugeabilités, S17, S10)")

print("§ 33 — CS4-06 : niveau du hasard du classifieur indicateurs -> u = fréquence de la plus grande classe de u (comptes seulement)")
for tailles, P in (((1000, 1000, 1000), 16), ((1000, 200, 100), 13), ((1000, 200, 100), 16), ((1000, 500, 300, 200), 14)):
    tot = sum(tailles)
    pmax = max(tailles) / tot / P
    U = len(tailles) * P
    print(f"  environnements de {tailles} paires, u2 sur P = {P} ans (U = {U}) : 1/U = {1 / U:.4f} ; plus grande classe = {pmax:.4f} ;"
          f" seuil du brouillon 4 = {1 / U + 0.05:.4f} ; seuil du brouillon 5 = {pmax + 0.05:.4f}")

print("§ 34 — S11 et table Estimation-thêta du brouillon 5 : ligne « puissance réalisée » (oracle z1 vrai) et déclencheur S14 (o)")
for p_or in (0.80, 0.90, 0.95):
    print(f"  oracle z1 vrai (k_hat choisi sur les vraies latentes) de part vraie {p_or:.2f} : tient la règle (au moins 37 sur 50) avec {proba(50, p_or, lambda x: x >= 37):.3f}")
print("  S14 (o) « trop propre » : M4 trouve dans au moins 5 mondes de plus que l'oracle z1 vrai sur les 50 mondes appariés (seuil de l'auteur, non calibré : une"
      " représentation apprise ne peut pas, sauf fuite, battre la latente vraie au-delà du hasard de sélection)")

print("§ 35 — CS4-12 : budget par combinaison des décisions DL-1, DL-3, DL-10, DL-11 (temps unitaires SUPPOSÉS comme au § 12 ; même compte que le § 21)")


def budget5(dl1=2, dl3=1, dl10=1, dl11=1):
    bt = {1: 0, 2: 200, 3: 200}[dl1]
    bh_cond = {1: 50, 2: 30, 3: 0}[dl1]
    r2m = {1: 100, 2: 50, 3: 0}[dl3]
    conf = {1: 0, 2: 50, 3: 30}[dl10] if dl1 != 1 else 0
    d5 = {1: 50, 2: 400, 3: 0}[dl11]
    ncond_ech = 12 + (1 if dl3 != 3 else 0)
    nret = 6 + (1 if dl3 != 3 else 0)
    mA = 12 * 100 + r2m + 4 * 50 + d5
    e = ncond_ech * 30 * 2
    r = nret * 30
    a = 2 * 30 + 2 * 30
    entr = (bt + conf) * 2 * 5 + (4 * bh_cond) * 2 * 5
    se = (2 if dl1 != 1 else 0) * 50 * 2
    calc = (mA * T_A + (e + a) * T_ECH + r * T_RETRO + (entr + se) * T_ENTR) / 60
    mondes = mA + bt + 4 * bh_cond + conf
    return mondes, calc, calc + validation4 + gardes4


base5 = budget5()
print(f"  recommandations (DL-1 = 2, DL-3 = 1, DL-10 = 1, DL-11 = 1) : {base5[0]} mondes ; calcul {base5[1]:.1f} h ; total {base5[2]:.1f} h (égal au § 21)")
for nom, kw in (("DL-1 = 1 (B-hors seul, 50 mondes par condition)", dict(dl1=1)), ("DL-1 = 3 (B-thêta seul)", dict(dl1=3)),
                ("DL-3 = 2 (R2- descriptive, 50 mondes)", dict(dl3=2)), ("DL-3 = 3 (pas de R2-)", dict(dl3=3)),
                ("DL-10 = 2 (Bthêta-v0-u décisive, 50)", dict(dl10=2)), ("DL-10 = 3 (Bthêta-v0-u descriptive, 30)", dict(dl10=3)),
                ("DL-11 = 2 (affectation F de décision, 400)", dict(dl11=2)), ("DL-11 = 3 (pas de D5)", dict(dl11=3)),
                ("minimum (DL-1 = 3, DL-3 = 3, DL-10 = 1, DL-11 = 3)", dict(dl1=3, dl3=3, dl10=1, dl11=3)),
                ("maximum (DL-1 = 2, DL-3 = 1, DL-10 = 2, DL-11 = 2)", dict(dl1=2, dl3=1, dl10=2, dl11=2))):
    mo, ca, to = budget5(**kw)
    print(f"  {nom} : {mo} mondes ; calcul {ca:.1f} h ; total {to:.1f} h ; multiplicateur toléré à 150 h {150 / to:.2f}, à 160 h {160 / to:.2f}")
