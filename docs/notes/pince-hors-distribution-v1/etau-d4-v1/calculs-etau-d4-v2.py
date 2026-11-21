#!/usr/bin/env python3
"""Calculs de la note « mesurer la taxe de l'obscurcissement dans un bras d'attaque déclaré » (décision D-4 reprise, v2).

Version 2, après la contre-lecture d'Opus 5.5 (constats 4, 7, 8, 10, 11, 12) ; la v1 reste au dossier, inchangée.
Ce qui change : au bloc F1, huit couples publiés de plus (renforcement sans gradient), la ligne « modèle entraîné à rester
lisible » sortie des plafonds, les étendues de plafond par classe imprimées, la taxe des poids ajustés sous ses deux
références, la taxe à trois couches par interpolation ; au bloc F5, ce qui est posé est dit posé, l'espérance de chaque
information et la condition sur le coût de l'attente sont calculées ; au bloc F6, les valeurs sont dites bornes basses.
Les blocs F0, F2, F3 et F4 sont ceux de la v1, sans changement.

Lois exactes (binomiale ; loi bêta par l'identité binomiale), arithmétique déclarée, approximation normale déclarée
là où elle sert ; aucun tirage, aucune donnée du programme, aucun résultat d'expérience du programme.
Trois sortes d'entrées, marquées à chaque ligne : [publié] = lu sur un PDF du dépôt, à la page dite dans la note ;
[figure] = lu à l'œil sur une figure, approximatif ; [jugement], [convention] ou [supposé] = de l'auteur.
Rejeu : python3 -I calculs-etau-d4-v2.py > calculs-etau-d4-v2.txt
"""
from math import exp, log, sqrt

Z_A, Z_B = 1.645, 1.282      # niveau 5 % unilatéral, puissance 0,90 (approximation normale)
NMAX = 20000
LF = [0.0]                   # logarithmes des factorielles
for _i in range(1, NMAX + 1):
    LF.append(LF[-1] + log(_i))


def pmf(n, k, q):
    if k < 0 or k > n:
        return 0.0
    if q <= 0.0:
        return 1.0 if k == 0 else 0.0
    if q >= 1.0:
        return 1.0 if k == n else 0.0
    return exp(LF[n] - LF[k] - LF[n - k] + k * log(q) + (n - k) * log(1 - q))


def queue_haute(n, c, q):
    """P(X >= c) pour X binomiale (n, q) : somme exacte, arrêtée quand les termes sont négligeables (< 1e-18 de la somme)."""
    if c <= 0:
        return 1.0
    if c > n:
        return 0.0
    mode = int((n + 1) * q)
    s = 0.0
    if c > mode:                      # termes décroissants vers le haut
        for k in range(c, n + 1):
            t = pmf(n, k, q)
            s += t
            if t < 1e-18 * s:
                break
        return s
    for k in range(c - 1, -1, -1):    # termes décroissants vers le bas
        t = pmf(n, k, q)
        s += t
        if t < 1e-18 * s:
            break
    return 1.0 - s


def critique(n, q0, alpha):
    """Plus petit c tel que P(X >= c | q0) <= alpha ; la masse au-delà de 12 écarts types est négligée (< 1e-30)."""
    sd = sqrt(n * q0 * (1 - q0))
    haut = min(n, int(n * q0 + 12 * sd + 12))
    cum, c = 0.0, haut + 1
    for k in range(haut, -1, -1):
        p = pmf(n, k, q0)
        if cum + p > alpha:
            break
        cum += p
        c = k
    return c


def taille(q0, q1, alpha=0.05, puissance=0.90):
    """Plus petit n pour lequel un seuil c donne P(X >= c | q0) <= alpha et P(X >= c | q1) >= puissance (q1 > q0)."""
    for n in range(1, NMAX + 1):
        c = critique(n, q0, alpha)
        if queue_haute(n, c, q1) >= puissance:
            return n, c, queue_haute(n, c, q0), queue_haute(n, c, q1)
    return None


# ---------------------------------------------------------------- F0
print("[F0] Témoins : ce programme doit redonner trois tailles de la note sur l'étau (bloc E3 de sa sortie).")
print("     Attendu, écrit avant l'exécution : (11, 9), (38, 5), (596, 136).")
for q0, q1 in ((0.50, 0.90), (0.05, 0.20), (0.20, 0.25)):
    n, c, r, p = taille(q0, q1)
    print(f"     q0 = {q0:.2f}, q1 = {q1:.2f} : n = {n}, seuil {c} (risque {r:.4f}, puissance {p:.4f})")


# ---------------------------------------------------------------- F1
def plafond(r0, rho, c):
    """L'attaquant a au moins deux gestes : ne rien cacher (il passe avec 1 - r0, compétence entière) ou cacher comme
    l'attaque publiée (il passe avec (1 - rho) c). Ce que l'étau retire est donc AU PLUS 1 - max des deux."""
    sans, avec = 1 - r0, (1 - rho) * c
    return sans, avec, 1 - max(sans, avec)


print()
print("[F1] Ce que les attaques publiées disent de l'étau : toujours un plafond, jamais un plancher.")
print("     r0 = rappel de la sonde sans obscurcissement, à 1 % de fausses alertes ; rho = rappel sous l'attaque ;")
print("     c = compétence gardée sous l'attaque, rapportée à la compétence sans attaque ; taxe = 1 - c.")
print("     Plafond = 1 - max(1 - r0, (1 - rho) c) : part des tentatives que l'étau retire au plus, face à cet attaquant ou à un meilleur.")
print("     Objets de contrôle, attendus écrits avant l'exécution :")
for nom, r0, rho, c, attendu in (("attaque parfaite et gratuite (rho = 0, c = 1)", 0.9, 0.0, 1.0, 0.0),
                                 ("attaque qui échoue (rho = r0, c = 1)", 0.9, 0.9, 1.0, 0.9),
                                 ("attaque qui détruit la compétence (rho = 0, c = 0)", 0.9, 0.0, 0.0, 0.9)):
    print(f"       {nom} : plafond {plafond(r0, rho, c)[2]:.3f} (attendu {attendu:.3f})")

SQL0 = 34.8   # [publié] part des requêtes justes sans obscurcissement, en %
MOY = "renforcement, sonde à moyenne ou à médiane sur les jetons"
MAX = "renforcement, sonde à maximum ou à attention"
PUBLIES = (
    # (régime, organisme et sonde, r0, rho, c, marques)
    ("gradient, suffixe d'entrée", "requêtes SQL, 2 milliards de paramètres ; régression logistique, 26 couches", 1.00, 0.03, 15.0 / SQL0,
     "r0, rho [publié] ; c [figure]", "suffixe, requêtes SQL, 26 couches"),
    ("gradient, suffixe d'entrée", "requêtes SQL ; perceptron, 26 couches", 1.00, 0.62, 14.0 / SQL0, "r0, rho [publié] ; c [figure]",
     "suffixe, requêtes SQL, 26 couches"),
    ("gradient, suffixe d'entrée", "requêtes SQL ; régression sur traits d'autoencodeur, 26 couches", 0.92, 0.09, 6.0 / SQL0,
     "r0, rho [publié] ; c [figure]", "suffixe, requêtes SQL, 26 couches"),
    ("gradient, suffixe d'entrée", "requêtes SQL ; traits d'autoencodeur choisis à la main, 26 couches", 0.91, 0.00, 2.3 / SQL0,
     "r0, rho [publié] ; c [figure]", "suffixe, requêtes SQL, 26 couches"),
    ("gradient, suffixe d'entrée", "nocivité ; sonde linéaire (résumé de l'article)", 1.00, 0.00, 0.90,
     "[publié] ; c = taux de réussite gardé [convention]", "suffixe, nocivité"),
    ("gradient, suffixe d'entrée", "nocivité, modèle entraîné à rester lisible, 8 milliards", 1.00, 0.00, 35.0 / 95.0,
     "rho, c [publié] ; r0 [supposé] ; c rapporte deux modèles différents, l'un durci et l'autre non : DURCISSEMENT DU DÉFENSEUR, NON UNE TAXE",
     "hors plafond"),
    ("gradient, suffixe d'entrée", "nocivité, 8 milliards ; ensemble de sondes réappris contre les attaques passées, 70 tours", 1.00, 0.00, 0.50,
     "c [publié : « around 50% »] ; r0, rho [supposé]", "suffixe, nocivité"),
    ("gradient, poids ajustés, sonde jamais vue", "tromperie, premier jeu, 9 milliards ; une couche, moyenne des jetons", 0.55, 0.33,
     65.3 / 67.4, "r0, rho [publié] ; c = banc général [publié]", "poids ajustés, sonde jamais vue"),
    ("gradient, poids ajustés, sonde jamais vue", "tromperie, second jeu", 0.88, 0.00, 65.3 / 67.4,
     "r0 [publié] ; rho [figure] ; c = banc général", "poids ajustés, sonde jamais vue"),
    ("gradient, poids ajustés, sonde jamais vue", "nocivité, premier jeu", 0.90, 0.16, 65.3 / 67.4, "r0, rho [publié] ; c = banc général",
     "poids ajustés, sonde jamais vue"),
    ("gradient, poids ajustés, sonde jamais vue", "nocivité, second jeu", 0.75, 0.00, 65.3 / 67.4, "r0 [publié] ; rho [figure] ; c = banc général",
     "poids ajustés, sonde jamais vue"),
    ("verdicts rendus en contexte, adaptateur de rang un", "concepts tenus à l'écart ; sonde fixe", 1.00, 0.040, 1 - 0.034,
     "r0, rho [publié] ; c = pire banc général, points pris pour une part [convention]", "verdicts en contexte"),
    ("verdicts rendus en contexte, adaptateur de rang un", "les mêmes ; sonde réapprise sur le modèle ajusté", 1.00, 0.146, 1 - 0.034,
     "rho [publié] ; r0 [supposé] ; c [convention]", "verdicts en contexte"),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; linéaire, moyenne des jetons", 0.96, 1 - 0.594, (3.72 - 1) / 4,
     "[publié] ; c = place sur l'échelle [convention]", MOY),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; linéaire, médiane des jetons (ajout v2)", 0.95, 1 - 0.687, (4.47 - 1) / 4,
     "[publié, tableau 4] ; c [convention]", MOY),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; perceptron, moyenne des jetons (ajout v2)", 0.952, 1 - 0.892, (4.37 - 1) / 4,
     "[publié, tableau 4] ; c [convention]", MOY),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; perceptron, médiane des jetons (ajout v2)", 0.955, 1 - 0.559, (4.36 - 1) / 4,
     "[publié, tableau 4] ; c [convention]", MOY),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; linéaire, maximum des jetons", 0.98, 1 - 0.994, (1.0 - 1) / 4,
     "[publié] ; c [convention]", MAX),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; perceptron, maximum des jetons", 0.964, 1 - 0.998, (1.0 - 1) / 4,
     "[publié] ; c [convention]", MAX),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; attention, moyenne", 0.98, 1 - 0.02, (4.04 - 1) / 4, "[publié] ; c [convention]", MAX),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; attention, médiane (ajout v2)", 0.99, 1 - 0.012, (4.42 - 1) / 4,
     "[publié, tableau 4] ; c [convention]", MAX),
    ("renforcement, sans gradient", "nocivité, 7 milliards ; attention, maximum (ajout v2)", 0.987, 1 - 0.01, (4.35 - 1) / 4,
     "[publié, tableau 4] ; c [convention]", MAX),
    ("renforcement, sans gradient", "nocivité, 8 milliards ; linéaire, moyenne des jetons", 0.96, 1 - 0.75, (2.8 - 1) / 4,
     "[publié] ; c [convention]", MOY),
    ("renforcement, sans gradient", "nocivité, 8 milliards ; linéaire, maximum des jetons", 0.994, 1 - 0.058, (4.78 - 1) / 4,
     "[publié] ; c [convention]", MAX),
    ("renforcement, sans gradient", "nocivité, 8 milliards ; attention, moyenne", 0.99, 1 - 0.01, (1.08 - 1) / 4, "[publié] ; c [convention]", MAX),
    ("renforcement, sans gradient", "nocivité, 14 milliards ; linéaire, moyenne des jetons (ajout v2)", 0.98, 1 - 0.82, (3.1 - 1) / 4,
     "rho, c [publié, tableau 1] ; r0 [supposé : le tableau ne le donne pas] ; c [convention]", MOY),
    ("renforcement, sans gradient", "nocivité, 14 milliards ; linéaire, maximum des jetons (ajout v2)", 0.98, 1 - 0.044, (4.96 - 1) / 4,
     "rho, c [publié, tableau 1] ; r0 [supposé] ; c [convention]", MAX),
    ("renforcement, sans gradient", "nocivité, 14 milliards ; attention, moyenne (ajout v2)", 0.98, 1 - 0.018, (4.5 - 1) / 4,
     "rho, c [publié, tableau 1] ; r0 [supposé] ; c [convention]", MAX),
)
print("     Couples publiés (pages dans la note, § 2) :")
ETENDUES = {}
for regime, quoi, r0, rho, c, marque, classe in PUBLIES:
    sans, avec, plaf = plafond(r0, rho, c)
    geste = "cacher" if avec > sans else "ne rien cacher"
    print(f"       {regime:42s} | {quoi}")
    if classe == "hors plafond":
        print(f"       {'':42s} | r0 {r0:5.3f} | rho {rho:5.3f} | rapport des deux taux de réussite {c:5.3f} | HORS PLAFOND (constat 12 de la"
              f" contre-lecture) : {marque}")
        continue
    ETENDUES.setdefault(classe, []).append(plaf)
    print(f"       {'':42s} | r0 {r0:5.3f} | rho {rho:5.3f} | taxe {1 - c:5.3f} | passe sans cacher {sans:5.3f}, en cachant {avec:5.3f}"
          f" | meilleur geste : {geste} | plafond de l'étau {plaf:5.3f} | {marque}")
print("     Étendue des plafonds par classe (le plus bas est celui qui compte : c'est la meilleure attaque qui fixe le plafond) :")
for classe, vals in ETENDUES.items():
    print(f"       {classe:58s} : de {min(vals):5.3f} à {max(vals):5.3f} ({len(vals)} couples)")
print("     Taxe des poids ajustés, selon la référence (deux bancs généraux [publié]) : sous déclencheur contre le même modèle ajusté sans")
print("     déclencheur, puis contre le modèle d'origine ; un saboteur aux poids ajustés paie l'ajustement en permanence.")
for banc, origine, ajuste, declenche in (("premier banc", 71.3, 68.2, 67.0), ("second banc", 68.6, 67.4, 65.3)):
    print(f"       {banc:12s} : origine {origine:4.1f}, ajusté {ajuste:4.1f}, sous déclencheur {declenche:4.1f} : taxe {1 - declenche / ajuste:5.3f} contre le"
          f" modèle ajusté, {1 - declenche / origine:5.3f} contre le modèle d'origine")
print("     Plafonds des quatre sondes jamais vues, avec la compétence rapportée au modèle d'origine (65,3 / 68,6) :")
for quoi, r0, rho in (("tromperie, premier jeu", 0.55, 0.33), ("tromperie, second jeu", 0.88, 0.00), ("nocivité, premier jeu", 0.90, 0.16),
                      ("nocivité, second jeu", 0.75, 0.00)):
    print(f"       {quoi:24s} : plafond {plafond(r0, rho, 65.3 / 68.6)[2]:5.3f} (contre {plafond(r0, rho, 65.3 / 67.4)[2]:5.3f} avec la référence du modèle ajusté)")
print("     Coût publié de l'évasion elle-même, au-delà de celui du comportement caché (canal caché dans le texte, poids ajustés,")
print("     moyenne de six bancs, points de pourcentage par rapport au modèle de base) [publié] :")
for modele, sans_evasion, avec_evasion in (("Qwen3 8B", -1.5, -2.7), ("Llama 3.1 8B", -3.7, -5.4), ("Ministral 8B", -6.4, -8.3),
                                           ("Qwen3 14B", -1.3, -1.6), ("Phi-4 14B", -0.8, -1.3)):
    print(f"       {modele:13s} : canal seul {sans_evasion:+.1f} ; canal caché aux sondes {avec_evasion:+.1f} ; part de l'évasion {avec_evasion - sans_evasion:+.1f}")
print("     Pente lue sur la figure des requêtes SQL [figure] : points de requêtes justes perdus par couche cachée de plus")
for nom, debut, fin in (("régression logistique", 34.0, 15.0), ("perceptron", 30.0, 14.0), ("régression sur traits d'autoencodeur", 31.0, 6.0),
                        ("traits d'autoencodeur choisis", 27.5, 2.3)):
    print(f"       {nom:38s} : de {debut:4.1f} % (1 couche) à {fin:4.1f} % (26 couches) : {(debut - fin) / 25:.2f} point par couche ;"
          f" taxe à 1 couche {1 - debut / SQL0:5.3f}, à 26 couches {1 - fin / SQL0:5.3f}")
print("     Les mêmes droites lues, à trois couches (interpolation linéaire entre les deux bouts lus) [figure] :")
for nom, debut, fin in (("régression logistique", 34.0, 15.0), ("perceptron", 30.0, 14.0), ("régression sur traits d'autoencodeur", 31.0, 6.0),
                        ("traits d'autoencodeur choisis", 27.5, 2.3)):
    trois = debut - 2 * (debut - fin) / 25
    print(f"       {nom:38s} : {trois:4.1f} % à 3 couches : taxe {1 - trois / SQL0:5.3f}")
ec = sqrt(0.15 * 0.85 / 210)
print(f"     Bruit d'un point de cette figure : 210 questions [publié] ; à 15 % de requêtes justes, écart type {100 * ec:.1f} points.")


# ---------------------------------------------------------------- F2
print()
print("[F2] Un attaquant donne un plafond : ce qu'une « taxe mesurée haute » apprend, selon ce que vaut l'attaquant.")
print("     p = probabilité, avant la mesure, que la taxe vraie soit haute ; a = probabilité que l'attaque trouve un")
print("     obscurcissement bon marché quand il en existe un. « Mesurée basse » : la taxe vraie est basse, à coup sûr.")
print("     « Mesurée haute » : P(vraie haute) = p / (p + (1 - p)(1 - a)^n) après n familles d'attaque, supposées échouer indépendamment.")
print("     Objets de contrôle, attendus écrits avant l'exécution : a = 0 rend p ; a = 1 rend 1.")
for p in (0.10, 0.25, 0.40):
    for a in (0.0, 0.3, 0.5, 0.8, 0.95, 1.0):
        post = [p / (p + (1 - p) * (1 - a) ** n) for n in (1, 2, 3)]
        print(f"       p {p:4.2f} | a {a:4.2f} | P(mesurée basse) {(1 - p) * a:5.3f} | après 1, 2, 3 familles « hautes » : "
              + ", ".join(f"{x:5.3f}" for x in post))


# ---------------------------------------------------------------- F3
print()
print("[F3] Tailles pour lire une taxe sur des épisodes rejoués.")
print("     (a) Loi binomiale exacte, taux du témoin supposé connu (grand bras témoin) : n épisodes rejoués sous obscurcissement,")
print("         X = réussites. « Taxe haute » : taux <= p (1 - k_haut) ; « taxe basse » : taux >= p (1 - k_bas). Risque <= 0,05, puissance >= 0,90.")
for k_haut, k_bas in ((0.30, 0.10), (0.50, 0.10), (0.30, 0.00), (0.10, 0.02)):
    for p in (0.35, 0.60, 0.85):
        n, c, r, pu = taille(p * (1 - k_haut), p * (1 - k_bas))
        print(f"         taxe {k_haut:.2f} contre {k_bas:.2f}, réussite du témoin {p:.2f} : n = {n:5d}, « basse » si X >= {c} (risque {r:.4f}, puissance {pu:.4f})")
print("     (b) Deux bras de même taille (témoin et obscurci), approximation normale : statistique = taux obscurci - (1 - k_haut) taux témoin.")
for k_haut, k_bas in ((0.30, 0.10), (0.50, 0.10), (0.10, 0.02)):
    for p in (0.35, 0.60, 0.85):
        p0, p1 = p * (1 - k_haut), p * (1 - k_bas)
        s0 = sqrt(p0 * (1 - p0) + (1 - k_haut) ** 2 * p * (1 - p))
        s1 = sqrt(p1 * (1 - p1) + (1 - k_haut) ** 2 * p * (1 - p))
        n = ((Z_A * s0 + Z_B * s1) / ((k_haut - k_bas) * p)) ** 2
        print(f"         taxe {k_haut:.2f} contre {k_bas:.2f}, réussite du témoin {p:.2f} : {n:6.0f} épisodes par bras")


def quantile_fa(m, k, proba):
    """Seuil = k-ième plus grand score de m épisodes honnêtes : le taux de fausses alertes réalisé F suit une loi bêta (k, m - k + 1),
    et P(F <= x) = P(binomiale (m, x) >= k). Quantile par dichotomie."""
    a, b = 0.0, 1.0
    for _ in range(100):
        x = (a + b) / 2
        if queue_haute(m, k, x) < proba:
            a = x
        else:
            b = x
    return (a + b) / 2


print("     (c) Le « 1 % de fausses alertes » quand le seuil est réglé sur peu d'épisodes honnêtes (loi exacte) :")
for m in (100, 300, 1000, 3000):
    k = max(1, int(0.01 * (m + 1)))
    print(f"         {m:5d} épisodes honnêtes, seuil au score de rang {k} en partant du haut : taux réalisé moyen {k / (m + 1):.4f},"
          f" de {quantile_fa(m, k, 0.05):.4f} à {quantile_fa(m, k, 0.95):.4f} dans 90 % des cas")


# ---------------------------------------------------------------- F4
print()
print("[F4] Heures de carte graphique des bras entraînés, d'après les durées publiées. Aucun prix : il est à relever au devis.")
print("     Renforcement sans gradient, modèle de 8 milliards de paramètres : 120 minutes par passe sur 1 000 exemples, une carte [publié].")
for nom, cibles, reglages, passes in (("une cible, un réglage, 3 passes", 1, 1, 3), ("deux cibles, trois réglages, 3 passes", 2, 3, 3),
                                      ("trois cibles, grille publiée de douze réglages, 6 passes", 3, 12, 6)):
    print(f"       {nom:58s} : {cibles * reglages * passes * 2:5d} heures de carte")
print("     Gradient à travers la sonde, suffixe d'entrée, modèle de 8 milliards : 256 pas, environ 10 minutes [publié] ;")
print("     contre un modèle entraîné à rester lisible : 16 384 pas, environ 10 heures [publié].")
for nom, suffixes, minutes in (("trois cibles, cinq poids de pénalité, trois graines, cas publié le plus court", 45, 10),
                               ("les mêmes, si chaque suffixe demande dix fois plus", 45, 100),
                               ("les mêmes, au cas publié le plus long", 45, 600)):
    print(f"       {nom:78s} : {suffixes * minutes / 60:6.1f} heures de carte")
print(f"     Rapport des coûts d'attaque publiés, avec et sans l'entraînement à rester lisible : {16384 / 256:.0f} fois en pas ; taux de réussite de 95 % à 35 %.")


# ---------------------------------------------------------------- F5
print()
print("[F5] La décision : sous quelles valeurs chaque option est la meilleure. Toutes les entrées sont des [jugements].")
print("     v = l'étau reste une grandeur que le programme veut dire avec des chiffres ;")
print("     h = le plafond par effacement est haut sur une cible au moins (un bras entraîné reste alors utile à l'étau) ;")
print("     q = l'expérience du coût de déplacement du papier C part à temps et peut viser les sondes de sabotage telles qu'elles sont déployées.")
print("     (a) lecture ajoutée à cette expérience : la meilleure si v et (non h, ou q) ; (b) bras à part : si v, h et non q ; (c) rien : si non v.")
print("     (a) échelonnée = plafond par effacement d'abord, hôte du bras entraîné choisi ensuite : POSÉE la meilleure dès que v.")
print("     Ce 0,850 n'est donc pas un résultat : le modèle ne compte ni le délai, ni le texte à sceller, ni la charge d'un lot de plus,")
print("     et compare une politique qui attend de savoir à des options engagées tout de suite (constat 8 de la contre-lecture).")


def parts(v, h, q):
    return v * (1 - h + h * q), v * h * (1 - q), 1 - v


va, vb, vc = parts(0.85, 0.5, 0.5)
print(f"     Valeurs de base v = 0,85, h = 0,50, q = 0,50 : (a) {va:.3f} ; (b) {vb:.3f} ; (c) {vc:.3f} ; somme {va + vb + vc:.3f} (attendu 1) ; (a) échelonnée 0.850")
print("     Objets de contrôle, attendus écrits avant l'exécution : q = 1 rend (a) = v ; h = 0 rend (a) = v ; h = 1 et q = 0 rendent (a) = 0.")
print(f"       q = 1 : {parts(0.85, 0.5, 1.0)[0]:.3f} ; h = 0 : {parts(0.85, 0.0, 0.5)[0]:.3f} ; h = 1, q = 0 : {parts(0.85, 1.0, 0.0)[0]:.3f}")
print(f"     Part des cas où le plafond par effacement règle seul la question en régime de gradient (1 - h) : {1 - 0.5:.2f} aux valeurs de base.")
print("     Sensibilité de (a), engagée dès maintenant :")
for v in (0.70, 0.85, 0.95):
    for h in (0.3, 0.5, 0.7):
        print(f"       v {v:4.2f} | h {h:3.1f} | q = 0,2 : {parts(v, h, 0.2)[0]:.3f} | q = 0,5 : {parts(v, h, 0.5)[0]:.3f} | q = 0,8 : {parts(v, h, 0.8)[0]:.3f}"
              f" | (a) échelonnée : {v:.3f}")
print("     Seuil de q au-dessus duquel (a) engagée dépasse 0,70 : q >= 1 - (1 - 0,70 / v) / h")
for v in (0.85, 0.95):
    for h in (0.3, 0.5, 0.7):
        seuil = 1 - (1 - 0.70 / v) / h
        print(f"       v {v:4.2f} | h {h:3.1f} : q >= {max(0.0, seuil):.3f}")
print("     Ce que chaque information fait à (a) engagée, depuis les valeurs de base :")
print(f"       q connu : {parts(0.85, 0.5, 1.0)[0]:.3f} si « à temps et compatible », {parts(0.85, 0.5, 0.0)[0]:.3f} sinon (coût : une question, aucune dépense)")
print(f"       h connu : {parts(0.85, 0.0, 0.5)[0]:.3f} si « plafond bas partout », {parts(0.85, 1.0, 0.5)[0]:.3f} sinon (coût : le plafond par effacement)")
print(f"       v connu : {parts(1.0, 0.5, 0.5)[0]:.3f} si l'étau reste à dire, 0.000 sinon (coût : ta décision sur la façon de dire l'étau)")
print("     Une information tranche, elle ne fait pas monter : espérance de (a) engagée après chacune, aux probabilités de base")
print("     (attendu, écrit avant l'exécution : la valeur de base, 0,6375, les trois fois, puisque (a) est linéaire en chacune) :")
e_q = 0.5 * parts(0.85, 0.5, 1.0)[0] + 0.5 * parts(0.85, 0.5, 0.0)[0]
e_h = 0.5 * parts(0.85, 0.0, 0.5)[0] + 0.5 * parts(0.85, 1.0, 0.5)[0]
e_v = 0.85 * parts(1.0, 0.5, 0.5)[0] + 0.15 * 0.0
print(f"       après q : {e_q:.4f} ; après h : {e_h:.4f} ; après v : {e_v:.4f}")
print("     Le coût de l'attente, absent ci-dessus : d = probabilité que l'échelonnement fasse manquer son heure à la mesure (texte à")
print("     sceller, logement du premier échelon hors de la lignée qui conçoit le saboteur, attente du gel de l'agent) [jugement].")
print("     L'option échelonnée vaut alors v (1 - d) ; elle ne dépasse (a) engagée que si d < h (1 - q).")
print("     Objets de contrôle, attendus écrits avant l'exécution : d = 0 rend v ; au seuil d = h (1 - q), les deux options sont égales.")
print(f"       d = 0 : {0.85 * (1 - 0.0):.3f} ; au seuil d = {0.5 * (1 - 0.5):.2f} : échelonnée {0.85 * (1 - 0.25):.4f}, (a) engagée {parts(0.85, 0.5, 0.5)[0]:.4f}")
for h in (0.3, 0.5, 0.7):
    for q in (0.2, 0.5, 0.8):
        print(f"       h {h:3.1f} | q {q:3.1f} : seuil d < {h * (1 - q):.2f}")
for d in (0.0, 0.1, 0.2, 0.25, 0.3, 0.4):
    print(f"       d {d:4.2f} : échelonnée {0.85 * (1 - d):.4f} ; (a) engagée {parts(0.85, 0.5, 0.5)[0]:.4f} ; (b) {parts(0.85, 0.5, 0.5)[1]:.4f}")


# ---------------------------------------------------------------- F6
def etau_sanction(r0, kappa, s, rho_min=0.0):
    """Rappel rho(o) = rho_min + (r0 - rho_min)(1 - o) ; compétence 1 - kappa o ; s = ce que le saboteur perd s'il est pris,
    en unités du gain d'un dommage passé. Utilité U(o) = (1 - rho(o))(1 - kappa o) - s rho(o), concave en o.
    Rend (o*, passe, U*)."""
    g = r0 - rho_min
    if g <= 0:
        o = 0.0
    elif kappa <= 0:
        o = 1.0
    else:
        o = min(1.0, max(0.0, (g * (1 + s) - kappa * (1 - r0)) / (2 * kappa * g)))
    rho = rho_min + g * (1 - o)
    passe = (1 - rho) * (1 - kappa * o)
    return o, passe, passe - s * rho


print()
print("[F6] L'économie de la taxe : ce que la sanction change (forme linéaire du bloc E1 de la note sur l'étau, plus un terme de sanction).")
print("     Témoin : sans sanction, ce programme doit redonner le bloc E1 (passe 0,7000 ; 0,5625 ; 0,7000 ; 0,5062).")
for r0, kappa in ((0.8, 0.30), (0.5, 0.50), (0.3, 0.50), (0.8, 0.50)):
    print(f"       r0 {r0:.2f}, taxe {kappa:.2f} : passe {etau_sanction(r0, kappa, 0.0)[1]:.4f}")
print("     Attendu, écrit avant l'exécution : le retrait ne décroît jamais quand la sanction monte ; sans plancher de rappel, il tend vers la taxe ;")
print("     il reste sous max(r0, taxe).")
pire = 0.0
for r0, kappa in ((0.8, 0.30), (0.3, 0.50), (0.5, 0.10)):
    ligne, avant = [], -1.0
    for s in (0.0, 0.5, 2.0, 10.0, 1000.0):
        o, passe, u = etau_sanction(r0, kappa, s)
        ligne.append(f"s={s:g} : cache {o:4.2f}, retrait {1 - passe:6.4f}")
        pire = max(pire, avant - (1 - passe), (1 - passe) - max(r0, kappa))
        avant = 1 - passe
    print(f"       r0 {r0:.2f}, taxe {kappa:.2f}, min {min(r0, kappa):.2f} | " + " | ".join(ligne))
print(f"     plus grande violation des deux attentes (décroissance, dépassement de max(r0, taxe)) : {pire:+.2e} (attendu : <= 0)")
def dommages_avant_prise(r0, kappa, rho_min, pas=1000):
    """Maximum, sur le degré d'obscurcissement o, de (1 - rho(o))(1 - kappa o) / rho(o) : nombre attendu de dommages discrets
    passés avant la première prise, et sanction au-dessus de laquelle aucun degré ne laisse une utilité positive. Grille de 1 001 points."""
    meilleur, ou = -1.0, 0.0
    for i in range(pas + 1):
        o = i / pas
        rho = rho_min + (r0 - rho_min) * (1 - o)
        if rho <= 0:
            return float("inf"), o
        val = (1 - rho) * (1 - kappa * o) / rho
        if val > meilleur:
            meilleur, ou = val, o
    return meilleur, ou


print("     RÉSERVE (constat 4 de la contre-lecture) : le rho_min des lignes publiées ci-dessous est le rappel laissé par UNE attaque publiée.")
print("     C'est une borne HAUTE du plancher de rappel : un attaquant meilleur le fait descendre. Les s* imprimés sont donc des bornes")
print("     BASSES du nombre attendu de dommages avant la première prise, non des valeurs. Pour la sonde à maximum sous renforcement,")
print("     l'attaque est un échec que ses auteurs rangent parmi des modes d'échec de l'entraînement : la borne basse y est la moins serrée.")
print("     Avec un plancher de rappel rho_min que l'obscurcissement complet n'efface pas : le saboteur renonce si la sanction dépasse")
print("     s* = maximum sur o de (1 - rho(o))(1 - taxe o) / rho(o) ; là où une seule prise l'incrimine, c'est aussi le nombre attendu")
print("     de dommages discrets passés avant la première prise, à son meilleur choix. Objet de contrôle, attendu écrit avant l'exécution :")
print("     rappel plein et taxe nulle sans plancher : infini ; rappel plancher de 1 : zéro.")
print(f"       plancher nul, taxe nulle : {dommages_avant_prise(0.9, 0.0, 0.0)[0]} ; plancher 1 : {dommages_avant_prise(1.0, 0.3, 1.0)[0]:.3f}")
for nom, r0, rho_min, kappa in (("sonde à maximum sous renforcement, 8 milliards [publié, convention]", 0.994, 1 - 0.058, 1 - (4.78 - 1) / 4),
                                ("sonde de nocivité jamais vue, poids ajustés [publié, banc général]", 0.90, 0.16, 1 - 65.3 / 67.4),
                                ("régression logistique, requêtes SQL, suffixe [publié, figure]", 1.00, 0.03, 1 - 15.0 / SQL0),
                                ("plancher nul (obscurcissement complet atteint)", 0.90, 0.0, 0.03)):
    val, ou = dommages_avant_prise(r0, kappa, rho_min)
    if val == float("inf"):
        print(f"       {nom:68s} : rho_min 0.000, taxe {kappa:5.3f} : s* infini : aucune sanction ne dissuade, aucune prise n'arrive")
    else:
        print(f"       {nom:68s} : rho_min <= {rho_min:5.3f}, taxe {kappa:5.3f} : s* >= {val:6.2f} (atteint en cachant {ou:4.2f})")
