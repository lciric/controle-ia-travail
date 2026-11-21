"""Calculs de la note « protocole X, première étape : cinq questions sur le dommage » (v2).

Version 2, après la contre-lecture par un autre modèle : aucun chiffre de la v1 ne change. Ajouts : la règle
de trois du régime à une prise et le critère r.n <= alpha (bloc B) ; la décision que le jumeau prend 3 fois
sur 10 (bloc D). Corrections de texte : le tirage par le harnais et ses deux suppositions, la portée des
nombres de tâches (bloc A) ; le plancher isotrope dit repère (bloc C) ; le taux honnête se nomme r, non q
(bloc B), pour ne pas se confondre avec la probabilité de reconnaissance de l'oracle d'un texte accordé.
Le bloc A décrit une famille de menaces réservée : il ne part vers aucune session qui conçoit des moniteurs.

Lois exactes (binomiale, bêta, information mutuelle d'un canal binaire) ; aucun tirage, aucune donnée
du programme, bibliothèque standard seule. Toutes les valeurs d'entrée sont des suppositions
d'illustration. Les objets de contrôle sont des assertions : si l'une tombe, le script s'arrête.
Rejeu : python3 -B calculs-protocole-x-dommage-v2.py > calculs-protocole-x-dommage-v2.txt
"""
import math


def titre(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


def log_pmf(k, n, q):
    if q <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if q >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(q) + (n - k) * math.log1p(-q))


def queue_haute(c, n, q):
    """P(Bin(n, q) >= c), somme exacte."""
    if c <= 0:
        return 1.0
    if c > n:
        return 0.0
    return min(1.0, sum(math.exp(log_pmf(k, n, q)) for k in range(c, n + 1)))


def seuil_exact(n, q, alpha):
    """Plus petit c tel que P(Bin(n, q) >= c) <= alpha."""
    c = 0
    while queue_haute(c, n, q) > alpha:
        c += 1
    return c


def exces_vu(n, q, c, puissance):
    """Plus petit excès de taux e tel que P(Bin(n, q + e) >= c) >= puissance (bissection)."""
    bas, haut = 0.0, 1.0 - q
    if queue_haute(c, n, q + haut) < puissance:
        return None
    for _ in range(60):
        mil = (bas + haut) / 2
        if queue_haute(c, n, q + mil) >= puissance:
            haut = mil
        else:
            bas = mil
    return haut


def h2(x):
    """Entropie binaire, en bits."""
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def beta_cf(a, b, x):
    """Fraction continue de la fonction bêta incomplète (méthode de Lentz)."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = tiny if abs(d) < tiny else d
    d = 1.0 / d
    h = d
    for m in range(1, 5000):
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
        if abs(delta - 1.0) < 1e-14:
            break
    return h


def beta_cdf(x, a, b):
    """Fonction de répartition de la loi bêta(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lbt) * beta_cf(a, b, x) / a
    return 1.0 - math.exp(lbt) * beta_cf(b, a, 1.0 - x) / b


def beta_quantile(pr, a, b):
    bas, haut = 0.0, 1.0
    for _ in range(200):
        mil = (bas + haut) / 2
        if beta_cdf(mil, a, b) < pr:
            bas = mil
        else:
            haut = mil
    return haut


# ---------------------------------------------------------------------------------------------------
titre("[A] Le dommage sans masse comme choix dans la dispersion de l'honnête : ce que la sélection rapporte,\n"
      "    ce que lit le rang de la conclusion, ce que retire un tirage fait par le harnais")
print("Monde : pour une tâche, chaque chemin d'analyse défendable rend une conclusion ; elle est « mauvaise »")
print("avec probabilité pi chez l'honnête, qui suit un chemin tiré au hasard. Un agent qui explore k chemins")
print("défendables et rend le pire rend une mauvaise conclusion avec probabilité 1 - (1 - pi)^k. Chaque produit")
print("rendu est un chemin défendable : une lecture par produit n'y voit aucun écart.")
print()
print(f"{'pi':>5} | " + " | ".join(f"k = {k:<2} taux ; excès" for k in (1, 2, 4, 8)))
for pi in (0.05, 0.10, 0.20):
    cases = []
    for k in (1, 2, 4, 8):
        taux = 1 - (1 - pi) ** k
        cases.append(f"{taux:10.4f} ; {abs(round(taux - pi, 10)):6.4f}")
    print(f"{pi:>5} | " + " | ".join(cases))
assert abs((1 - 0.9 ** 1) - 0.10) < 1e-12          # objet où « la sélection rapporte » est faux : k = 1
assert abs((1 - 0.9 ** 8) - 0.10 - 0.4695) < 1e-4  # objet où c'est vrai : k = 8, pi = 0,10
print()
print("Nombre de tâches pour que le compte des mauvaises conclusions, comparé au taux pi du jumeau (supposé")
print("connu), sonne au niveau 1 % avec probabilité 0,9 (test binomial exact unilatéral). BORNE OPTIMISTE : le")
print("taux du jumeau est supposé connu (limite d'un nombre infini de tirages du jumeau) et les k chemins")
print("indépendants ; la puissance du rang contre K tirages finis, avec ex aequo, est plus basse et n'est pas")
print("calculée ici ; des chemins corrélés rapportent moins au suspect.")
print(f"{'pi':>5} | " + " | ".join(f"k = {k:<6}" for k in (1, 2, 4, 8)))
for pi in (0.05, 0.10, 0.20):
    cases = []
    for k in (1, 2, 4, 8):
        taux = 1 - (1 - pi) ** k
        if k == 1:
            cases.append("  jamais ")
            continue
        n = 1
        while True:
            c = seuil_exact(n, pi, 0.01)
            if queue_haute(c, n, taux) >= 0.9:
                break
            n += 1
        cases.append(f"{n:>9}")
    print(f"{pi:>5} | " + " | ".join(cases))
print()
print("Si l'ensemble des variantes défendables est fixé HORS du suspect (énuméré par le jumeau ou en contexte")
print("isolé) et que le harnais tire le chemin après l'engagement, le taux rendu vaut pi quel que soit k : excès")
print("nul. C'est un raisonnement, non un calcul de ce bloc, et il tient sous deux suppositions : le suspect ne")
print("compose pas l'ensemble (s'il le compose, le taux rendu est la part des mauvaises conclusions dans")
print("l'ensemble qu'il a composé, et l'excès n'est pas nul) ; l'exécution du chemin tiré est contrôlée.")
print("Objets de contrôle : k = 1 (honnête) doit rendre un excès nul et « jamais » ; k = 8, pi = 0,10 doit")
print("rendre un excès de 0,4695. La lecture par produit « réussit » (ne sonne pas) dans les deux : comme")
print("mesure du dommage de sélection elle est morte ; le compte des conclusions, lui, a une masse.")

# ---------------------------------------------------------------------------------------------------
titre("[B] Le dommage qui se confond avec les échecs honnêtes : le seuil garanti dépend du taux honnête de la\n"
      "    statistique qu'on audite, et tend vers le régime de signature quand ce taux tend vers zéro")
T, p = 10000, 0.20
n = int(T * p)
print(f"Suppositions : horizon T = {T} épisodes ; audit au hasard p = {p} ; nombre d'audits pris à sa moyenne")
print(f"n = {n} ; test binomial exact unilatéral au niveau 1 % sur le taux honnête r de l'événement audité.")
print("Épisodes en excès que le test ne voit qu'une fois sur deux (et qu'il manque 5 fois sur 100) :")
print()
print(f"{'r honnête':>10} | {'seuil c':>8} | {'excès vu 1 fois sur 2':>22} | {'excès vu 95 fois sur 100':>25}")
ref = {}
for q in (0.10, 0.03, 0.01, 0.003, 0.001, 0.0005, 0.000005, 0.0):
    c = seuil_exact(n, q, 0.01)
    e50 = exces_vu(n, q, c, 0.5)
    e95 = exces_vu(n, q, c, 0.95)
    ref[q] = (e50 * T, e95 * T)
    print(f"{q:>10} | {c:>8} | {e50 * T:>22.1f} | {e95 * T:>25.1f}")
assert seuil_exact(n, 0.000005, 0.01) == 1 and seuil_exact(n, 0.0005, 0.01) == 5   # dits dans la lecture
# objets de contrôle : r = 0,10 proche de l'approximation normale de la note sur l'attaquant informé
# (156,1) ; r = 0 doit rendre ln 2 / p et ln 20 / p (régime de signature).
assert abs(ref[0.10][0] - 156.1) < 12.0
assert abs(ref[0.0][0] - math.log(2) / p) < 0.05 and abs(ref[0.0][1] - math.log(20) / p) < 0.05
print()
print(f"Objets de contrôle : r = 0,10 doit rester près de 156,1 (approximation normale de la note sur")
print(f"l'attaquant informé) : rendu {ref[0.10][0]:.1f} ; r = 0 doit rendre ln 2 / p = {math.log(2) / p:.2f} et")
print(f"ln 20 / p = {math.log(20) / p:.2f} : rendu {ref[0.0][0]:.2f} et {ref[0.0][1]:.2f}.")
print()
print("Lecture : une seule prise suffit (seuil c = 1) quand 1 - (1 - r)^n <= alpha, c'est-à-dire à peu près")
print("r.n <= alpha : le critère dépend du niveau alpha et du nombre d'audits n à l'horizon dit. Ici, alpha = 1 %")
print("et n = 2 000 : r <= 0,000005 (une fois sur 200 000 épisodes) ; à une fois par échantillon d'audit")
print("(r = 0,0005) il faut cinq prises.")
alpha = 0.01
assert 1 - (1 - 0.000005) ** n <= alpha < 1 - (1 - 0.000006) ** n      # le critère exact, à la marge
print()
print("Ce qu'il faut d'épisodes honnêtes SANS UN SEUL événement pour établir un taux, par la règle de trois")
print("(zéro événement sur N borne le taux à 3 / N, au niveau 95 %) ; valeur exacte : ln 20 / -ln(1 - r).")
print(f"{'r à établir':>12} | {'règle de trois 3 / r':>21} | {'exact':>10}")
trois = {}
for r_ in (0.0005, 0.000005):
    exact = math.log(20) / -math.log1p(-r_)
    trois[r_] = (3 / r_, exact)
    print(f"{r_:>12} | {3 / r_:>21.0f} | {exact:>10.0f}")
assert round(trois[0.0005][0]) == 6000 and round(trois[0.000005][0]) == 600000
assert abs(trois[0.0005][1] / trois[0.0005][0] - 1) < 0.01               # la règle de trois est à 1 % de l'exact
print("Lecture : le régime à cinq prises demande 6 000 épisodes honnêtes sans événement ; le régime à une prise")
print("en demande 600 000. À l'échelle d'un banc, le régime à une prise ne s'établit donc pas par mesure : il")
print("ne s'atteint que pour un événement que l'honnête ne peut pas commettre par construction.")
print()
print("« Certifier ou céder » : n'est accepté tel quel que le produit que l'agent certifie ; le reste est refait")
print("par la voie de confiance. Courbe de certification de l'honnête SUPPOSÉE (part certifiée u, taux d'échec")
print("eps parmi les certifiés) ; audit p sur la part certifiée.")
print(f"{'part certifiée u':>17} | {'échec honnête eps':>18} | {'excès vu 1 fois sur 2':>22} | {'part refaite':>12}")
for u, eps in ((1.0, 0.10), (0.8, 0.03), (0.6, 0.01), (0.4, 0.003)):
    nu = int(T * u * p)
    c = seuil_exact(nu, eps, 0.01)
    e50 = exces_vu(nu, eps, c, 0.5)
    print(f"{u:>17} | {eps:>18} | {e50 * T * u:>22.1f} | {1 - u:>12.1f}")
print()
print("Appariement au jumeau sur la même tâche (banc) : sous l'honnête, les paires discordantes se partagent")
print("à égalité, quel que soit r : le nul est exact sans connaître r. Le bruit, lui, vaut le taux de")
print("discordance 2.r.(1 - r).(1 - rho), rho = corrélation des issues entre l'agent honnête et son jumeau.")
print("Facteur sur l'excès non vu, par rapport au test à r connu (approximation en racine, déclarée) :")
for rho in (0.0, 0.5, 0.9, 0.99, 1.0):
    print(f"   rho = {rho:<4} : facteur = {math.sqrt(2 * (1 - rho)):.3f}")
print("Lecture : apparier à un jumeau indépendant coûte un facteur 1,41 et achète l'exactitude du nul ;")
print("le gain ne vient que de ce que l'agent et le jumeau partagent (même début, mêmes tirages). Au banc")
print("seulement : en service il n'y a pas de jumeau.")

# ---------------------------------------------------------------------------------------------------
titre("[C] Deux verrous de la sonde de réussite attendue, chiffrés : ce que fuit un aiguillage tiré au sort,\n"
      "    et le plancher « direction au hasard » du recouvrement entre l'adaptateur et la sonde")
print("(i) Aiguillage tiré au sort : l'épisode est aiguillé avec probabilité a si la lecture est basse, b si")
print("elle est haute (lectures basses et hautes à parts égales). Information qu'une décision observée livre")
print("sur la lecture, en bits ; part utile de l'aiguillage a - b ; nombre de décisions observées qui suffit")
print("pour en apprendre le sens avec 5 % d'erreur au plus (borne de Chernoff, cas symétrique b = 1 - a).")
print(f"{'a':>5} | {'b':>5} | {'bits par décision':>18} | {'part utile':>10} | {'observations':>12}")
fuite = {}
for a, b in ((1.0, 0.0), (0.9, 0.1), (0.8, 0.2), (0.7, 0.3), (0.6, 0.4), (0.5, 0.5)):
    info = h2((a + b) / 2) - (h2(a) + h2(b)) / 2
    fuite[(a, b)] = info
    if a == 1.0:
        obs = "1"
    elif a == 0.5:
        obs = "jamais"
    else:
        obs = f"{math.ceil(math.log(20) / (-math.log(2 * math.sqrt(a * (1 - a)))))}"
    print(f"{a:>5} | {b:>5} | {info:>18.4f} | {a - b:>10.1f} | {obs:>12}")
assert abs(fuite[(1.0, 0.0)] - 1.0) < 1e-12 and abs(fuite[(0.5, 0.5)]) < 1e-12
print("Objets de contrôle : aiguillage déterministe = 1 bit ; aiguillage sans égard à la lecture = 0 bit.")
print("Lecture : le hasard n'achète le silence qu'en vendant l'aiguillage (0,03 bit pour 0,2 de part utile).")
print("Le silence se construit autrement : effets retenus jusqu'à la fin de l'épisode, décision hors de la")
print("vue de l'agent.")
print()
print("(ii) Recouvrement entre la direction lue par la sonde et l'espace où l'adaptateur écrit. Sous le nul")
print("« sous-espace tiré au hasard, de rang R, en dimension d », le carré du cosinus suit une loi")
print("bêta(R/2, (d - R)/2), de moyenne R/d. d = 4096 SUPPOSÉ (largeur du flux résiduel, à relire sur la")
print("configuration du modèle).")
d = 4096
print(f"{'rang R':>7} | {'moyenne R/d':>12} | {'quantile 0,99':>14} | {'quantile 0,999':>15}")
for R in (16, 64, 480, 2048):
    a_, b_ = R / 2.0, (d - R) / 2.0
    print(f"{R:>7} | {R / d:>12.5f} | {beta_quantile(0.99, a_, b_):>14.5f} | {beta_quantile(0.999, a_, b_):>15.5f}")
assert abs(beta_cdf(0.5, 1.0, 1.0) - 0.5) < 1e-9                      # bêta(1, 1) = uniforme
assert abs(beta_cdf(0.25, 0.5, 0.5) - (2 / math.pi) * math.asin(0.5)) < 1e-9   # loi de l'arc sinus
assert abs(beta_quantile(0.5, 2048 / 2.0, 2048 / 2.0) - 0.5) < 1e-6    # R = d/2 : médiane 1/2
print("Objets de contrôle : bêta(1, 1) rend 0,5 en 0,5 ; bêta(1/2, 1/2) rend la loi de l'arc sinus ; R = d/2")
print("rend une médiane de 1/2. Lecture : un adaptateur de rang 16 sur trente modules qui écrivent dans le")
print("flux (R = 480) recouvre déjà 12 % de toute direction par hasard : le plancher n'est pas zéro. Ce")
print("plancher est ISOTROPE (sous-espace tiré uniformément) : un repère seulement. Les états et les écritures")
print("d'un adaptateur sont anisotropes, et le plancher réel peut en être loin ; le plancher qui compte est")
print("celui de l'adaptateur honnête de même budget.")

# ---------------------------------------------------------------------------------------------------
titre("[D] Tâches floues : la garantie par accord avec le jumeau se paie en recouvrement entre honnêtes")
print("Règle : la décision d que porte le produit du suspect n'est acceptée que si au moins m de K tirages du")
print("jumeau sur la même tâche portent la même décision ; sinon le produit est refait par la voie de confiance.")
print("Pour TOUTE décision d* fixée, que le jumeau prend avec probabilité pi, et quoi que fasse le suspect :")
print("P(d* acceptée) <= P(Bin(K, pi) >= m). Sans la règle, un suspect qui rend toujours d* passe à coup sûr.")
print("Acceptation de l'honnête : somme sur d de p_d . P(Bin(K, p_d) >= m).")
K = 8
lois = (("nette", (0.95, 0.03, 0.02)),
        ("moyenne", (0.70, 0.20, 0.10)),
        ("floue", (0.40, 0.30, 0.20, 0.10)),
        ("très floue", tuple([0.10] * 10)))
print()
print(f"K = {K} tirages du jumeau. Borne sur le passage d'une décision de probabilité pi chez le jumeau :")
print(f"{'m':>3} | {'pi = 0,02':>10} | {'pi = 0,10':>10} | " + " | ".join(f"accept. loi {nom:<10}" for nom, _ in lois))
table = {}
for m in (0, 1, 2, 3, 4):
    b02, b10 = queue_haute(m, K, 0.02), queue_haute(m, K, 0.10)
    acc = [sum(pd * queue_haute(m, K, pd) for pd in loi) for _, loi in lois]
    table[m] = (b02, b10, acc)
    print(f"{m:>3} | {b02:>10.4f} | {b10:>10.4f} | " + " | ".join(f"{x:>22.3f}" for x in acc))
assert table[0][0] == 1.0 and all(abs(x - 1.0) < 1e-12 for x in table[0][2])   # m = 0 : aucune garantie
assert abs(table[2][2][0] - 0.951) < 5e-4 and abs(table[2][2][1] - 0.817) < 5e-4      # valeurs dites en lecture
assert abs(table[2][2][2] - 0.699) < 5e-4 and abs(table[2][2][3] - 0.187) < 5e-4
assert queue_haute(1, K, 0.0) == 0.0                                           # pi = 0 : jamais accepté
print()
print("Objets de contrôle : m = 0 (règle vide) doit rendre une borne de 1 et tout accepter : rendu ; une")
print("décision que le jumeau ne prend jamais (pi = 0) ne passe jamais : rendu.")
p30 = queue_haute(2, K, 0.30)
assert abs(table[2][0] - 0.0103) < 5e-5 and abs(p30 - 0.7447) < 5e-5
assert abs(p30 - (1 - 0.7 ** 8 - 8 * 0.3 * 0.7 ** 7)) < 1e-12              # objet de contrôle : forme close
print(f"Borne RELATIVE à la propension du jumeau : à m = 2, une décision que le jumeau prend 3 fois sur 10")
print(f"(deuxième décision de la loi floue) passe encore avec probabilité {p30:.3f} au plus. La règle ne retire")
print("donc pas un dommage choisi dans le support de l'honnête.")
print(f"Lecture : à m = 2, une décision que le jumeau prend 2 fois sur 100 passe avec probabilité {table[2][0]:.4f}")
print("au plus (environ une fois sur 100, non « au plus une fois sur 100 »), et")
print("l'honnête garde 0,95 de ses produits si ses décisions sont nettes, 0,82 si elles sont moyennes, 0,70")
print("si elles sont floues, 0,19 si elles sont très floues. Le « flou » d'une tâche est ce défaut de")
print("recouvrement ; il se mesure sur des honnêtes seuls. La borne vaut pour la décision projetée, tirages du")
print("jumeau faits après la remise et en secret, non pour ce que la projection efface.")
