"""Calculs de la note « couverture de l'oracle » (v1).

Lois exactes et formules fermées ; une approximation normale, déclarée au bloc C.
Aucun tirage, aucune donnée du programme, bibliothèque standard seule.
Toutes les valeurs d'entrée sont des suppositions d'illustration.
Rejeu : python -B calculs-couverture-oracle-v1.py > calculs-couverture-oracle-v1.txt
"""
import math


def phi(z):
    """Fonction de répartition de la loi normale centrée réduite."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def binom_cdf(m, n, q):
    """P(Bin(n, q) <= m), somme exacte."""
    return sum(math.comb(n, k) * q ** k * (1 - q) ** (n - k) for k in range(m + 1))


def borne_haute_manque(m, n, a):
    """Borne haute exacte (Clopper-Pearson) du taux de manque : q tel que P(Bin(n, q) <= m) = a."""
    if m >= n:
        return 1.0
    bas, haut = 0.0, 1.0
    for _ in range(200):
        mil = (bas + haut) / 2
        if binom_cdf(m, n, mil) > a:
            bas = mil
        else:
            haut = mil
    return haut


def titre(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


# ---------------------------------------------------------------------------------------------------
titre("[A] Détection = sélection x identification : le plancher d'audit corrigé de la couverture de l'oracle")
print("Rang du premier épisode endommagé pris avec probabilité 0,95 : plus petit K tel que 1 - (1 - p.r)^K >= 0,95,")
print("p = taux d'audit au hasard, r = probabilité que l'oracle reconnaisse ce dommage quand il le regarde.")
print()
print(f"{'p':>6} | " + " | ".join(f"r = {r:<4}" for r in (1.0, 0.5, 0.2, 0.05, 0.0)))
for p in (0.01, 0.05, 0.20):
    cases = []
    for r in (1.0, 0.5, 0.2, 0.05, 0.0):
        if p * r == 0:
            cases.append("  jamais")
        else:
            cases.append(f"{math.ceil(math.log(0.05) / math.log(1 - p * r)):>8}")
    print(f"{p:>6} | " + " | ".join(cases))
print()
print("Objets de contrôle : r = 1 doit rendre 299 (p = 0,01) et 14 (p = 0,20), valeurs des notes précédentes ;")
print("r = 0 doit rendre « jamais ». C'est l'attaquant qui choisit le genre et la dose, donc r est le minimum sur")
print("ce qu'il peut choisir, pas une moyenne.")

# ---------------------------------------------------------------------------------------------------
titre("[B] Ce que des dommages plantés disent de r : borne exacte, et prix du « pire des strates »")
print("Borne haute à 95 % du taux de manque de l'oracle dans une strate, après n plants dont m manqués (exacte).")
print()
print(f"{'n':>5} | {'m = 0':>8} | {'m = 1':>8} | {'m = 2':>8}")
for n in (10, 20, 30, 59, 100, 299):
    print(f"{n:>5} | " + " | ".join(f"{borne_haute_manque(m, n, 0.05):>8.4f}" for m in (0, 1, 2)))
print()
print("Nombre de plants par strate, tous retrouvés, pour certifier « r >= 1 - e dans CHAQUE strate »,")
print("à 95 % simultanément sur K strates (correction de Bonferroni) : n >= ln(0,05/K) / ln(1 - e).")
print()
print(f"{'K strates':>10} | {'e = 0,10':>9} | {'e = 0,20':>9} | {'total (e = 0,10)':>17}")
for K in (1, 5, 10, 20):
    n10 = math.ceil(math.log(0.05 / K) / math.log(0.9))
    n20 = math.ceil(math.log(0.05 / K) / math.log(0.8))
    print(f"{K:>10} | {n10:>9} | {n20:>9} | {K * n10:>17}")
print()
print("Objet de contrôle : m = 0, n = 59 doit rendre une borne juste sous 0,05, car 0,95^59 = "
      f"{0.95 ** 59:.4f} < 0,05 ; n = 299 juste sous 0,01, car 0,99^299 = {0.99 ** 299:.4f} < 0,05.")
print("Ce que la borne certifie : le taux de manque pour des dommages tirés comme ceux du planteur, dans cette strate.")

# ---------------------------------------------------------------------------------------------------
titre("[C] L'angle mort de taille : verdict binaire à limite de détection contre mesure graduée appariée")
M_LISTE = (30.0, 100.0, 200.0)
T = 10000          # horizon, en épisodes
P_AUDIT = 0.20     # taux d'audit au hasard
A50 = 0.30         # dose par épisode que le verdict binaire voit une fois sur deux
PENTE = 0.50       # écart type de la courbe dose-détection, en logarithme de la dose
SIGMA = 0.25       # écart type honnête de l'écart au jumeau, par épisode, en unités de dommage
print(f"Suppositions : horizon T = {T} épisodes ; audit p = {P_AUDIT} ; dommage plafonné à 1 par épisode ;")
print(f"verdict binaire : probabilité d'identifier une dose x = Phi((ln x - ln {A50}) / {PENTE}) ;")
print(f"mesure graduée : écart au jumeau par épisode audité, bruit honnête d'écart type {SIGMA}, test unilatéral à 5 %")
print("sur la somme des écarts de tous les épisodes audités (approximation normale, nombre d'audits pris à sa moyenne).")
print()
print("(i) Verdict binaire seul : probabilité de NON-détection d'un total M réparti en doses x sur M/x épisodes.")
print(f"{'dose x':>8} | {'identif.':>9} | " + " | ".join(f"M = {int(M):<4}" for M in M_LISTE))
for x in (1.0, 0.5, 0.3, 0.1, 0.05, 0.02):
    pod = phi((math.log(x) - math.log(A50)) / PENTE)
    ligne = []
    for M in M_LISTE:
        D = M / x
        if D > T:
            ligne.append("hors horizon")
        else:
            ligne.append(f"{(1 - P_AUDIT * pod) ** D:>8.4f}")
    print(f"{x:>8} | {pod:>9.5f} | " + " | ".join(ligne))
print()
print("(ii) Mesure graduée seule : la somme attendue des écarts audités vaut p.M quelle que soit la répartition ;")
print("     son écart type honnête vaut sigma.racine(p.T). Non-détection = 1 - Phi(M.racine(p/T)/sigma - 1,645).")
for M in M_LISTE:
    z = M * math.sqrt(P_AUDIT / T) / SIGMA
    print(f"     M = {int(M):>4} : z = {z:.3f} ; non-détection = {1 - phi(z - 1.645):.4f}")
m50 = 1.645 * SIGMA * math.sqrt(T / P_AUDIT)
m95 = (1.645 + 1.645) * SIGMA * math.sqrt(T / P_AUDIT)
print(f"     Total vu une fois sur deux : {m50:.1f} ; vu 95 fois sur 100 : {m95:.1f} (unités de dommage, sur {T} épisodes).")
print("     Même loi en racine que la règle « moniteur invalide » ; elle est proportionnelle à sigma :")
for s in (0.5, 0.25, 0.125):
    print(f"       sigma = {s:<6} -> total vu 95 fois sur 100 : {3.29 * s * math.sqrt(T / P_AUDIT):>7.1f}")
print()
print("(iii) Pire répartition pour le défenseur, à M donné :")
for M in M_LISTE:
    pire_bin = 0.0
    x = 1.0
    while x >= M / T:
        pod = phi((math.log(x) - math.log(A50)) / PENTE)
        pire_bin = max(pire_bin, (1 - P_AUDIT * pod) ** (M / x))
        x *= 0.95
    z = M * math.sqrt(P_AUDIT / T) / SIGMA
    nd_grad = 1 - phi(z - 1.645)
    print(f"     M = {int(M):>4} : binaire seul {pire_bin:.4f} ; gradué seul {nd_grad:.4f} ; "
          f"les deux (produit, au pire) {pire_bin * nd_grad:.4f}")
print()
print("Objets de contrôle : (faux) un verdict binaire devant un dommage dilué sous sa limite : la conclusion")
print("« le total M est vu » y est fausse, attendu non-détection proche de 1 ; (vrai) dose pleine x = 1 : attendu")
print("non-détection proche de 0. Lecture : le verdict binaire ne borne rien du dommage dilué ; seule la mesure")
print("graduée le borne, et sa borne vaut ce que vaut l'appariement au jumeau (sigma).")

# ---------------------------------------------------------------------------------------------------
titre("[D] Masse manquante des genres de dommage : Good-Turing, son biais exact, sa marge sans hypothèse")


def gt_exact(probs, n):
    """Espérances exactes : masse manquante E[U_n] et estimateur de Good-Turing E[N1/n], tirages indépendants."""
    e_u = sum(p * (1 - p) ** n for p in probs)
    e_gt = sum(p * (1 - p) ** (n - 1) for p in probs)
    return e_u, e_gt


def zipf(k):
    h = sum(1 / j for j in range(1, k + 1))
    return [1 / (j * h) for j in range(1, k + 1)]


cas = (
    ("objet vrai : 5 genres équiprobables", [0.2] * 5),
    ("genres en loi de Zipf, 200 genres", zipf(200)),
    ("objet faux : 1 000 000 de genres équiprobables", None),
)
print(f"{'loi des genres chez le planteur':<48} | {'n':>5} | {'E[masse manquante]':>18} | {'E[N1/n]':>9} | {'biais':>8} | {'1/n':>7}")
for nom, probs in cas:
    for n in (100, 500):
        if probs is None:
            k = 10 ** 6
            e_u = (1 - 1 / k) ** n
            e_gt = (1 - 1 / k) ** (n - 1)
        else:
            e_u, e_gt = gt_exact(probs, n)
        print(f"{nom:<48} | {n:>5} | {e_u:>18.6f} | {e_gt:>9.6f} | {e_gt - e_u:>8.6f} | {1 / n:>7.4f}")
print()
print("Le biais de N1/n (part des genres vus une seule fois) est toujours entre 0 et 1/n : somme des p^2.(1-p)^(n-1).")
print("Marge sans hypothèse sur la loi, tirages indépendants : avec probabilité >= 1 - d,")
print("  masse manquante <= N1/n + (1 + racine(2)).racine(ln(2/d)/n)")
print("  (inégalité des différences bornées sur N1, qu'un tirage change d'au plus 2, et théorème 1 de Berend et")
print("   Kontorovich sur la queue haute de la masse manquante ; assemblage de moi, non contre-lu).")
print()
print(f"{'n plants classés':>17} | {'marge à d = 0,05':>17}")
for n in (50, 100, 200, 500, 1000, 2000, 5000):
    print(f"{n:>17} | {(1 + math.sqrt(2)) * math.sqrt(math.log(2 / 0.05) / n):>17.3f}")
n_01 = math.ceil((1 + math.sqrt(2)) ** 2 * math.log(40) / 0.01)
print(f"Plants nécessaires pour une marge de 0,10 : {n_01}.")
print()
print("Objets de contrôle : sur l'objet faux (presque tout genre est neuf) l'estimateur doit rendre environ 1, il")
print("rend 0,9999 ; sur l'objet vrai (5 genres) environ 0, il rend 0,000000. La borne ne vaut que pour des tirages")
print("indépendants d'une loi fixe : celle du planteur, jamais celle d'un attaquant qui choisit.")

# ---------------------------------------------------------------------------------------------------
titre("[E] L'accord entre oracles comme mesure de l'angle mort commun : juste si les dommages se valent, faux sinon")


def deux_oracles(classes):
    """classes : liste (part, probabilité d'être vu par un oracle). Oracles indépendants sachant la classe."""
    n1 = sum(w * q for w, q in classes)
    les_deux = sum(w * q * q for w, q in classes)
    aucun = sum(w * (1 - q) ** 2 for w, q in classes)
    estime_total = n1 * n1 / les_deux          # Lincoln-Petersen, en part de la population vraie
    vu = 1 - aucun
    return aucun, estime_total - vu


def trois_oracles(classes):
    """Borne basse de Chao à k = 3 occasions : ((k - 1)/k).f1^2/(2.f2), f1 et f2 = vus par un seul, par deux."""
    f1 = sum(w * 3 * q * (1 - q) ** 2 for w, q in classes)
    f2 = sum(w * 3 * q * q * (1 - q) for w, q in classes)
    aucun = sum(w * (1 - q) ** 3 for w, q in classes)
    return aucun, (2 / 3) * f1 * f1 / (2 * f2)


homogene = [(1.0, 0.5)]
heterogene = [(0.5, 0.9), (0.5, 0.1)]
for nom, cl in (("objet vrai : tous les dommages vus avec probabilité 0,5 par chaque oracle", homogene),
                ("objet faux : moitié faciles (0,9), moitié durs pour tous (0,1)", heterogene)):
    vrai2, est2 = deux_oracles(cl)
    vrai3, chao = trois_oracles(cl)
    print(nom)
    print(f"   deux oracles   : part vraie vue par aucun = {vrai2:.4f} ; part estimée (capture et recapture) = {est2:.4f}")
    print(f"   trois oracles  : part vraie vue par aucun = {vrai3:.4f} ; borne basse de Chao à trois occasions = {chao:.4f}")
print()
print("Sur l'objet vrai, les deux méthodes rendent la vérité. Sur l'objet faux, elles « réussissent » (2 % et 4,5 %")
print("d'angle mort annoncés) là où la conclusion est fausse (41 % et 36,5 %) :")
print("comme garanties elles sont mortes ; elles restent des bornes basses. Un genre dur pour tous les oracles est")
print("ce que cherche un attaquant.")

# ---------------------------------------------------------------------------------------------------
titre("[F] La chaîne de raccordement : oracle bon marché sur tout, oracle cher sur un sous-échantillon tiré au hasard")
N_TOUT, N_CHER, THETA = 4000, 200, 0.15
print(f"Suppositions : {N_TOUT} épisodes lus par l'oracle bon marché, {N_CHER} tirés au hasard pour l'oracle cher ;")
print(f"taux de dommage vrai (au sens de l'oracle cher) = {THETA} ; l'oracle bon marché voit une part c des dommages,")
print("sans fausse alerte. Estimateur : moyenne(bon marché, tout) + moyenne(cher - bon marché, sous-échantillon).")
print("Variance calculée comme pour deux échantillons indépendants (approximation déclarée).")
print()
print(f"{'part vue c':>10} | {'bon marché seul : biais':>23} | {'raccordé : biais':>16} | {'écart type raccordé':>19} | {'vaut n étiquettes chères':>24}")
var_classique = THETA * (1 - THETA) / N_CHER
for c in (0.0, 0.3, 0.6, 0.9, 1.0):
    moy_b = c * THETA
    var_b = moy_b * (1 - moy_b)
    d = (1 - c) * THETA
    var_d = d * (1 - d)
    var = var_b / N_TOUT + var_d / N_CHER
    print(f"{c:>10.1f} | {moy_b - THETA:>23.3f} | {0.0:>16.3f} | {math.sqrt(var):>19.4f} | {N_CHER * var_classique / var:>24.0f}")
print()
print("Objets de contrôle : c = 1 doit valoir N/n fois le sous-échantillon (4000 étiquettes), c = 0 doit valoir le")
print("sous-échantillon seul (200). Un attaquant qui place son dommage hors de la vue de l'oracle bon marché ramène")
print("le gain à 1 ; il ne peut pas biaiser l'estimation. Reste l'angle mort de l'oracle cher lui-même.")

# ---------------------------------------------------------------------------------------------------
titre("[G] La formule de taille d'échantillon des garanties nucléaires est le plancher d'audit lu à l'envers")
N_ITEMS, D_DEF, BETA = 1000, 30, 0.10
n_formule = math.ceil(N_ITEMS * (1 - BETA ** (1 / D_DEF)))
nd_exact = math.comb(N_ITEMS - D_DEF, n_formule) / math.comb(N_ITEMS, n_formule)
print(f"n = N.(1 - beta^(1/D)) avec N = {N_ITEMS}, D = {D_DEF} objets en défaut, beta = {BETA} : n = {n_formule}.")
print(f"Probabilité exacte (hypergéométrique) de ne tirer aucun défaut avec n = {n_formule} : {nd_exact:.4f} (visé : {BETA}).")
for r in (1.0, 0.8, 0.5, 0.2):
    # chaque défaut tiré est identifié avec probabilité r, indépendamment : mélange hypergéométrique exact
    nd = 0.0
    for k in range(0, min(D_DEF, n_formule) + 1):
        pk = math.comb(D_DEF, k) * math.comb(N_ITEMS - D_DEF, n_formule - k) / math.comb(N_ITEMS, n_formule)
        nd += pk * (1 - r) ** k
    print(f"   identification r = {r:<4} : non-détection réalisée = {nd:.4f}")
print("Objet de contrôle : r = 1 doit rendre la valeur exacte ci-dessus. La probabilité de détection réalisée n'atteint")
print("le niveau visé que si l'identification vaut 1 : c'est la phrase du glossaire, entrée 9.32, et c'est la question.")
