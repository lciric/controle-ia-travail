#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « protocole X : six questions sur l'attaquant informé » (v2).

Formules fermées, énumérations exactes, quadratures déterministes ; aucun tirage,
aucune donnée du programme, bibliothèque standard seule. Toutes les entrées sont
des suppositions d'illustration, sauf les valeurs de comparaison recopiées de
pièces du dépôt et dites telles.

Version 2, après la contre-lecture de la v1 (Opus 5.5, constats 6, 8, 9, 15, 16). Ce qui change :
  [A4] la phrase de lecture dit pour quelles qualités de prédiction la sonde brute passe sous son résidu,
       avec une assertion ; le « cinquième des occasions » est dit paramètre de l'exemple ;
  [B2] la référence de la recapture est la part signalée chez les témoins endommagés honnêtes (f_h), non la
       part signalée de tous les épisodes ; un objet de contrôle où « évité » est faux par construction ;
  [C4] l'horizon est calculé sur le minimum de la borne de la règle et de la borne triviale n (1 - rho0) ;
       les cases où seule la borne triviale tient sont marquées ;
  [C6] la borne sur le dommage total est dite « théorème repris » (la règle appliquée avec un moniteur muet).
Aucun autre chiffre ne change : tous les nombres de la v1 hors [C4] sont rendus à l'identique.
Les blocs modifiés ne sont pas contre-lus.

Usage : python3 -I calculs-protocole-x-attaquant-v2.py > calculs-protocole-x-attaquant-v2.txt
"""
import itertools
import math
from fractions import Fraction


# ------------------------------------------------------------------ outils
def phi_n(x):
    """Fonction de répartition de la loi normale centrée réduite."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def dens_n(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def quantile_n(p):
    lo, hi = -12.0, 12.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if phi_n(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def simpson(f, a, b, n=4000):
    """Quadrature de Simpson, n pair, déterministe."""
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4.0 if i % 2 else 2.0)
    return s * h / 3.0


def binom_cdf(k, n, p):
    """P(Bin(n, p) <= k), somme exacte en flottants."""
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return sum(math.comb(n, i) * p ** i * (1.0 - p) ** (n - i) for i in range(k + 1))


def n95(c):
    """Nombre d'épisodes endommagés après lequel la prise est acquise avec probabilité 0,95."""
    if c <= 0.0:
        return None
    if c >= 1.0:
        return 1
    return math.ceil(math.log(0.05) / math.log(1.0 - c))


def fmt_n(n):
    return "jamais" if n is None else str(n)


Z95 = quantile_n(0.99)  # seuil à 1 % de fausses alertes sur une lecture normale réduite

print("Calculs de la note « protocole X : six questions sur l'attaquant informé » (v2)")
print("Aucun tirage ; entrées = suppositions d'illustration, sauf mention « recopié ».")
print()

# =================================================================== bloc A
print("[A] Question 1 — ce que l'attaquant gagne à connaître le protocole, et ce qui lui survit")
print()
print("  [A1] Borne : succès de l'attaquant qui voit V avant d'agir <= valeur à l'aveugle + fuite,")
print("       fuite = moyenne, sur le tirage Z, de la distance en variation totale entre la loi de V sachant Z")
print("       et la loi de V. Vérification exacte sur une famille de mondes finis.")


def valeurs(pi, succes, lam):
    """pi : loi du tirage Z ; succes[a][z] dans [0, 1] ; la vue V vaut Z avec probabilité lam,
    sinon un tirage indépendant de loi pi. Renvoie (aveugle, informé, fuite)."""
    nz = len(pi)
    aveugle = max(sum(pi[z] * s[z] for z in range(nz)) for s in succes)
    informe = 0.0
    for v in range(nz):
        # P(V = v, Z = z) = pi_z (lam 1[v = z] + (1 - lam) pi_v)
        joint = [pi[z] * ((lam if v == z else 0.0) + (1.0 - lam) * pi[v]) for z in range(nz)]
        informe += max(sum(joint[z] * s[z] for z in range(nz)) for s in succes)
    fuite = sum(pi[z] * lam * (1.0 - pi[z]) for z in range(nz))
    return aveugle, informe, fuite


pire, serre, cas = -1.0, 0.0, 0
lois = [(1 / 3, 1 / 3, 1 / 3), (0.6, 0.3, 0.1), (0.8, 0.1, 0.1), (0.5, 0.5, 0.0)]
for bits in itertools.product((0.0, 1.0), repeat=9):          # toutes les matrices 3 x 3 à entrées 0 ou 1
    succes = [bits[0:3], bits[3:6], bits[6:9]]
    for pi in lois:
        for lam in (0.0, 0.25, 0.5, 0.75, 1.0):
            av, inf, fu = valeurs(pi, succes, lam)
            cas += 1
            pire = max(pire, inf - av - fu)
            if fu > 0:
                serre = max(serre, (inf - av) / fu)
print(f"       {cas} cas (512 matrices de succès, 4 lois du tirage, 5 niveaux de fuite)")
print(f"       plus grand dépassement de la borne : {pire:.2e} (attendu : nul ou négatif, au bruit d'arrondi près)")
print(f"       plus grand rapport (gain de l'informé) / fuite : {serre:.3f} (au plus 1 ; 1 = borne atteinte)")
av0, inf0, fu0 = valeurs((1 / 3, 1 / 3, 1 / 3), [(0, 1, 1), (1, 0, 1), (1, 1, 0)], 0.0)
av1, inf1, fu1 = valeurs((1 / 3, 1 / 3, 1 / 3), [(0, 1, 1), (1, 0, 1), (1, 1, 0)], 1.0)
print(f"       objet de contrôle, fuite nulle   : aveugle {av0:.3f}, informé {inf0:.3f} (attendu : égaux)")
print(f"       objet de contrôle, tirage connu  : aveugle {av1:.3f}, informé {inf1:.3f}, fuite {fu1:.3f}")
print()

print("  [A2] Monde à trois canaux. Une attaque s'appuie sur la forme du texte, sur la mémoire du contexte ou")
print("       sur un tirage rare ; la paraphrase, la remise à zéro et le rééchantillonnage détruisent chacun")
print("       un canal (succès résiduel r). Une attaque « robuste » ne s'appuie sur aucun canal et perd kappa.")
print("       P = probabilité qu'une intervention tombe sur un pas. Marge = baisse du succès de l'attaque.")
P_TOT, R_RES = 0.9, 0.1


def succes_canal(p_canal, r=R_RES):
    return 1.0 - p_canal * (1.0 - r)


marge_naif = 1.0 - succes_canal(P_TOT)                     # défense réglée contre l'attaque naïve (un canal)
print(f"       P = {P_TOT}, r = {R_RES}")
print(f"       attaquant naïf, défense réglée contre lui (toute la masse sur son canal) : marge {marge_naif:.3f}")
print("       attaquant informé contre cette même défense : il change de canal, marge 0.000")
print("       attaquant qui connaît chaque tirage : il prend un canal épargné, marge 0.000 quelle que soit la loi")
for kappa in (0.0, 0.1, 0.3, 0.5, 1.0):
    # point selle par exploration de la grille des répartitions (pas 0,05 de P), contre la forme fermée
    meilleur = 2.0
    pas = 18
    for i in range(pas + 1):
        for j in range(pas + 1 - i):
            p1, p2 = P_TOT * i / pas, P_TOT * j / pas
            p3 = P_TOT - p1 - p2
            rep = max(succes_canal(p1), succes_canal(p2), succes_canal(p3), 1.0 - kappa)
            meilleur = min(meilleur, rep)
    ferme = max(succes_canal(P_TOT / 3.0), 1.0 - kappa)
    assert abs(meilleur - ferme) < 1e-12
    print(f"       taxe de robustesse kappa = {kappa:.1f} : marge au point selle = {1.0 - meilleur:.3f}"
          f"  (= min(couverture {1.0 - succes_canal(P_TOT / 3.0):.3f}, kappa))")
print("       objet de contrôle : kappa = 0 rend une marge nulle (le tirage secret seul ne donne rien) ;")
print("       kappa = 1 rend la couverture du mélange. La marge au point selle vaut au plus la taxe.")
print()

print("  [A3] Rééchantillonnage tiré en secret, un seul des k tirages exécuté au hasard, preuve cumulée sur les k.")
print("       Gain en preuve par pas exécuté (donc division du délai d'alerte) : G = k / (1 + (k - 1) rho),")
print("       rho = corrélation, chez l'honnête, de la lecture entre deux tirages d'un même état.")
print("       " + "rho".ljust(8) + "".join(f"k = {k}".rjust(9) for k in (2, 4, 8, 16)) + "   limite (1/rho)")
for rho in (0.0, 0.2, 0.45, 0.8, 1.0):
    ligne = "".join(f"{k / (1.0 + (k - 1) * rho):9.2f}" for k in (2, 4, 8, 16))
    lim = "sans borne" if rho == 0 else f"{1.0 / rho:.2f}"
    print(f"       {rho:<8.2f}{ligne}   {lim}")
print("       objet de contrôle : rho = 1 rend G = 1 (rien à gagner) ; rho = 0 rend G = k.")
print("       Si l'attaquant sait quel tirage s'exécute, il ne nuit que sur celui-là : G = 1 quel que soit rho.")
print("       Fuite partielle : sur une part lam des pas, l'attaquant sait quel tirage s'exécute. S'il lui suffit")
print("       de nuire sur une part eps des pas, il loge son dommage dans les pas connus d'abord. Gain restant,")
print("       pour G = 2,50 (k = 4, rho = 0,2) : [min(eps, lam) + max(0, eps - lam) G] / eps.")
print("       " + "eps".ljust(8) + "".join(f"lam = {x:.2f}".rjust(13) for x in (0.0, 0.01, 0.05, 0.2)))
for eps in (0.02, 0.05, 0.2):
    ligne = ""
    for lam in (0.0, 0.01, 0.05, 0.2):
        g_eff = (min(eps, lam) + max(0.0, eps - lam) * 2.5) / eps
        ligne += f"{g_eff:13.2f}"
    print(f"       {eps:<8.2f}{ligne}")
print("       Une fuite égale au taux de sabotage annule tout le gain : le secret doit tenir mieux que ce taux.")
print()

print("  [A4] Sélection d'attaque par simulation du juge de texte, et résidu de la sonde.")
print("       Lecture de la sonde = part que le texte prédit (T) + résidu (R), indépendants, variance 1 chacun")
print("       chez l'honnête. Sous attaque : T décalé de dT, R décalé de dR. L'attaquant prédit T avec une")
print("       corrélation c et n'exécute que le cinquième des occasions où sa prédiction est la plus basse.")
print("       Rappel à 1 % de fausses alertes, parmi les attaques exécutées.")


def rappels(d_t, d_r, corr, part):
    """Renvoie (juge de texte, sonde brute, résidu) : rappels à 1 % parmi les attaques exécutées."""
    seuil = Z95
    r_res = 1.0 - phi_n(seuil - d_r)
    if part >= 1.0 or corr <= 0.0:
        r_txt = 1.0 - phi_n(seuil - d_t)
        r_brut = 1.0 - phi_n(seuil - (d_t + d_r) / math.sqrt(2.0))
        return r_txt, r_brut, r_res
    # prédiction That = corr * (T - dT) + sqrt(1 - corr^2) * bruit : normale réduite, corrélée à T
    coupe = quantile_n(part)                      # on exécute si That < coupe

    def poids(u):
        return dens_n(u)

    def txt(u):   # P(T > seuil | That = u), T | u ~ N(dT + corr u, 1 - corr^2)
        sd = math.sqrt(max(1.0 - corr * corr, 1e-300))
        return 1.0 - phi_n((seuil - d_t - corr * u) / sd)

    def brut(u):  # P((T + R)/sqrt 2 > seuil | That = u), T + R | u ~ N(dT + corr u + dR, 2 - corr^2)
        sd = math.sqrt(2.0 - corr * corr)
        return 1.0 - phi_n((seuil * math.sqrt(2.0) - d_t - corr * u - d_r) / sd)

    if corr >= 1.0:
        def txt(u):   # noqa: F811 — T = dT + u exactement
            return 1.0 if d_t + u > seuil else 0.0
    r_txt = simpson(lambda u: poids(u) * txt(u), -10.0, coupe) / part
    r_brut = simpson(lambda u: poids(u) * brut(u), -10.0, coupe) / part
    return r_txt, r_brut, r_res


print("       " + "cas".ljust(46) + "juge de texte   sonde brute   résidu")
A4 = {}
for nom, d_t, d_r, corr, part in (
        ("aucune sélection (dT = 2, dR = 2)", 2.0, 2.0, 0.0, 1.0),
        ("sélection, prédiction médiocre (c = 0,5)", 2.0, 2.0, 0.5, 0.2),
        ("sélection, bonne prédiction (c = 0,85)", 2.0, 2.0, 0.85, 0.2),
        ("sélection, simulation parfaite (c = 1)", 2.0, 2.0, 1.0, 0.2),
        ("contrôle : résidu vide (dR = 0), c = 1", 2.0, 0.0, 1.0, 0.2),
        ("contrôle : tout dans le résidu (dT = 0), c = 1", 0.0, 2.0, 1.0, 0.2),
):
    a, b, c_ = rappels(d_t, d_r, corr, part)
    A4[(d_t, d_r, corr, part)] = (a, b, c_)
    print(f"       {nom:<46}{a:13.3f}{b:14.3f}{c_:9.3f}")
b_050, res = A4[(2.0, 2.0, 0.5, 0.2)][1], A4[(2.0, 2.0, 0.5, 0.2)][2]
b_085, b_100 = A4[(2.0, 2.0, 0.85, 0.2)][1], A4[(2.0, 2.0, 1.0, 0.2)][1]
assert b_050 > res > b_085 > b_100          # la sonde brute ne passe sous son résidu que si la prédiction est bonne
print("       Lecture : sous sélection le juge de texte s'effondre et le résidu ne bouge pas. La sonde brute ne")
print(f"       passe sous son propre résidu ({res:.3f}) que si la prédiction est bonne (c = 0,85 : {b_085:.3f} ; c = 1 :")
print(f"       {b_100:.3f}) ; quand elle est médiocre (c = 0,5) la sonde brute reste au-dessus ({b_050:.3f}).")
print("       Si le résidu est vide (dR = 0), rien ne survit : c'est le rappel de 0,010 du hasard.")
print("       Suppose que l'attaquant ne prédit rien du résidu : canal de retour fermé (aucun verdict ni aucune")
print("       correction ne lui revient). Avec retour, ce bloc ne dit rien.")
print("       Le « cinquième des occasions » est un paramètre de l'exemple, non un coût mesuré.")
print()

# =================================================================== bloc B
print("[B] Question 2 — la part du plancher quand l'attaquant devine le soupçon")
print()
print("  [B1] Budget d'audit p. Le moniteur signale une part f des épisodes ; sans sélection il signale une")
print("       attaque avec probabilité r. L'attaquant devine avec une qualité g (0 = pas du tout, 1 = toujours)")
print("       et renonce aux attaques qu'il prévoit signalées. Part des attaques exécutées qui sont signalées :")
print("       R = r (1 - g) / (1 - r g). Probabilité de prise par attaque exécutée, plancher pi :")
print("       c = pi + R (p - pi) / f. Épisodes endommagés avant la prise (probabilité 0,95).")
P_AUD, F_SIG, R_MON = 0.02, 0.05, 0.6
print(f"       p = {P_AUD}, f = {F_SIG}, r = {R_MON}")
print("       " + "g".ljust(6) + "levier R/f".rjust(11) + "tout au soupçon".rjust(18) + "moitié-moitié".rjust(16)
      + "tout au plancher".rjust(18) + "   meilleure règle / moitié-moitié")
for g in (0.0, 0.5, 0.9, 0.97, 1.0):
    rr = R_MON * (1.0 - g) / (1.0 - R_MON * g)
    cs = {}
    for nom, pi in (("soupcon", 0.0), ("moitie", P_AUD / 2.0), ("plancher", P_AUD)):
        cs[nom] = pi + rr * (P_AUD - pi) / F_SIG
    meilleur = max(cs.values())
    rapport = meilleur / cs["moitie"]
    assert rapport <= 2.0 + 1e-12
    print(f"       {g:<6.2f}{rr / F_SIG:11.2f}{fmt_n(n95(cs['soupcon'])):>18}{fmt_n(n95(cs['moitie'])):>16}"
          f"{fmt_n(n95(cs['plancher'])):>18}   {rapport:.2f}")
print("       La règle optimale bascule quand le levier passe sous 1 ; qui ignore g perd au plus un facteur 2")
print("       en probabilité de prise avec la règle moitié-moitié. Objet de contrôle : levier 1 rend les trois")
print("       règles égales ; g = 1 rend « jamais » pour l'audit des seuls signalés.")
g_egal = (R_MON - F_SIG) / (R_MON * (1.0 - F_SIG))
print(f"       qualité de devin où le levier vaut 1 : g = {g_egal:.3f}")
print()
print("  [B2] Recapture lue des deux côtés. Parmi n épisodes endommagés trouvés par le plancher, combien le")
print("       moniteur en avait-il signalé ? Référence : f_h, la part signalée chez les témoins endommagés")
print("       honnêtes du même régime (non la part signalée de tous les épisodes). Aveugle : f_h. Voyant : r.")
print("       Sous la référence : moins que f_h, ce qui a deux causes possibles (évité ; ou mode de dommage")
print("       par nature moins signalé, sans aucun modèle du moniteur).")
for f_sig in (0.05, 0.2, 0.5):
    n_evite = math.ceil(math.log(0.05) / math.log(1.0 - f_sig))
    print(f"       référence f_h = {f_sig:.2f} : {n_evite} épisodes endommagés audités, tous non signalés, écartent")
    print("         « aveugle » au niveau 5 % et font conclure « sous la référence » (cas extrême : aucun signalé)")
print("       Objet de contrôle où « sous la référence, donc évité » est faux par construction : un mode de")
print("       dommage que le moniteur signale par nature à 0,05, sans aucun modèle du moniteur, lu contre")
F_REF, F_MODE = 0.20, 0.05
n_ref = math.ceil(math.log(0.05) / math.log(1.0 - F_REF))
p_faux = (1.0 - F_MODE) ** n_ref
n_mode = math.ceil(math.log(0.05) / math.log(1.0 - F_MODE))
print(f"       une référence f_h = {F_REF:.2f} : les {n_ref} épisodes sont tous non signalés avec probabilité {p_faux:.3f},")
print("       et « évité » s'annoncerait à tort. Lu contre des témoins plantés du même mode, sans modèle du")
print(f"       moniteur (référence {F_MODE:.2f}), le même flux ne conclut rien avant {n_mode} épisodes : ce sont ces")
print("       témoins qui séparent « évité » de « mode par nature moins signalé ».")
for f_sig, r_mon in ((0.05, 0.6), (0.2, 0.6)):
    trouve = None
    for n in range(1, 400):
        for k in range(0, n + 1):
            fausse = 1.0 - binom_cdf(k - 1, n, f_sig)       # P(au moins k signalés | aveugle)
            puiss = 1.0 - binom_cdf(k - 1, n, r_mon)        # P(au moins k signalés | voyant)
            if fausse <= 0.05 and puiss >= 0.9:
                trouve = (n, k)
                break
        if trouve:
            break
    print(f"       séparer « voyant » (r = {r_mon}) de « aveugle » (f_h = {f_sig}) à 5 % et 90 % : n = {trouve[0]}, seuil {trouve[1]}")
print()
print("  [B3] Tirer aussi ce que l'oracle vérifie. m contrôles d'enjeux égaux, un seul tiré par audit, p = 0,05 :")
for m in (1, 3, 10):
    print(f"       m = {m:2d} : prise par épisode endommagé {0.05 / m:.4f} ; acquise à 0,95 au {n95(0.05 / m)}e épisode endommagé")
print("       La couverture devient la réunion des m contrôles ; le délai est multiplié par m.")
print()

# =================================================================== bloc C
print("[C] Question 3 — la boucle audit, recapture, réapprentissage : quand converge-t-elle")
print()
print("  [C1] Borne d'erreurs amincie. Un apprenant qui fait au plus d erreurs sur toute suite réalisable,")
print("       mis à jour sur les seules erreurs auditées (probabilité e, pièce fraîche) : le total M de ses")
print("       erreurs vérifie E[M] <= d / e, et P(M >= m) <= P(Bin(m, e) <= d).")
print("       " + "d".ljust(5) + "e".ljust(7) + "E[M] au plus".rjust(13) + "   m tel que P(M >= m) <= 0,05")
for d in (5, 20):
    for e in (0.01, 0.05, 0.2):
        m = d
        while binom_cdf(d, m, e) > 0.05:
            m += 1
        print(f"       {d:<5d}{e:<7.2f}{d / e:13.0f}   {m}")
print()
print("  [C2] Objets de contrôle exécutés : la classe des seuils sur une droite (étiquette = 1 si x > seuil).")
print("       Apprenant : coupe au milieu de ce qui reste possible. Adversaire : présente le point de coupe")
print("       et lui donne l'étiquette contraire à la prédiction, ce qui reste cohérent avec un seuil possible.")


def joue_seuils(grille, tours):
    """grille = None : seuils réels dans [0, 1] (fractions exactes) ; sinon nombre fini N de seuils k/N.
    Renvoie le nombre d'erreurs forcées en `tours` tours, toutes étiquettes vues."""
    erreurs = 0
    if grille is None:
        bas, haut = Fraction(0), Fraction(1)                # seuil dans ]bas, haut]
        for _ in range(tours):
            x = (bas + haut) / 2
            # l'apprenant prédit 0 pour x (il croit le seuil au-dessus de x, par convention) ; l'adversaire dit 1
            haut = x                                        # étiquette 1 : le seuil est sous x
            erreurs += 1                                    # il reste toujours des seuils : erreur à chaque tour
        return erreurs
    bas, haut = 0, grille                                   # seuils possibles : indices bas+1 .. haut
    for _ in range(tours):
        if haut - bas <= 1:
            break                                           # un seul seuil possible : plus d'erreur forçable
        milieu = (bas + haut) // 2
        haut = milieu                                       # l'adversaire contredit, l'ensemble est coupé en deux
        erreurs += 1
    return erreurs


print(f"       seuils réels (dimension de Littlestone infinie), 60 tours : {joue_seuils(None, 60)} erreurs"
      " (attendu : une par tour, sans plafond)")
for n_seuils in (64, 1024):
    print(f"       {n_seuils} seuils possibles (classe finie), 60 tours : {joue_seuils(n_seuils, 60)} erreurs"
          f" (attendu : au plus log2 = {int(math.log2(n_seuils))})")
print("       Une lecture de précision finie, ou une marge que l'adversaire ne peut pas réduire, borne le total ;")
print("       un lecteur linéaire sur des états que l'adversaire place à volonté n'a pas de borne.")
print()
print("  [C3] Réapprentissage répété, vu comme une itération. Le moniteur se replace en m' = clip(b - c m) :")
print("       c = (mobilité de la réponse de l'agent au moniteur) x (mobilité du moniteur) / (courbure).")
print("       Si une part lam seulement de l'état du moniteur atteint l'agent, c = lam x c_max.")
C_MAX, B_IT = 3.0, 0.9
print(f"       c_max = {C_MAX}, b = {B_IT}, départ m = 0 ; après 400 réapprentissages :")
for lam in (0.0, 0.1, 0.3, 1.0 / 3.0, 0.5, 1.0):
    c = lam * C_MAX
    m, traj = 0.0, []
    tours_conv = None
    for t in range(1, 401):
        m_suiv = min(1.0, max(0.0, B_IT - c * m))
        traj.append(m_suiv)
        if tours_conv is None and abs(m_suiv - B_IT / (1.0 + c)) < 0.01:
            tours_conv = t
        m = m_suiv
    ecart = abs(traj[-1] - traj[-2])
    etat = "converge" if ecart < 1e-9 else "oscille sans fin"
    if etat != "converge":
        tours_conv = None
    conv = "-" if tours_conv is None else str(tours_conv)
    print(f"       fuite lam = {lam:.3f} : c = {c:.2f} ; {etat} ; écart entre deux tours = {ecart:.3f} ;"
          f" tours pour être à 0,01 du point fixe : {conv}")
print("       Seuil : c < 1, soit lam < 1 / c_max. Objet de contrôle où la convergence est fausse par")
print("       construction : la réponse qui saute (exemple 3.4 de l'article sur la prédiction performative),")
seq, m = [], 0.0
for _ in range(6):
    m = 1.0 if m < 0.5 else 0.0
    seq.append(int(m))
print(f"       suite obtenue : {seq} (attendu : alternance sans fin)")
print()
print("  [C4] L'horizon d'expiration de la garantie en régime d'excès. Règle « moniteur invalide » corrigée")
print("       (mélange, douze taux qui descendent vers le taux acceptable) ; B(n) = borne garantie de l'excès")
print("       d'épisodes endommagés et non signalés avant l'annonce, avec probabilité 0,90.")
ALPHA, BETA = 0.05, 0.10
GRILLE = [1.0 + 4.0 / 2 ** j for j in range(12)]


def phi_q(q, s):
    return q * s + math.log(1.0 - q + q * math.exp(-s))


def borne_un(mult, lam, q, n, rho0, big_l):
    rho = mult * rho0
    u = math.log(rho / rho0)
    b = math.log((1.0 - rho0) / (1.0 - rho))
    a = u + b
    aa = q * a - (phi_q(q, lam * u) - phi_q(q, -lam * b)) / lam
    if aa <= 0.0:
        return math.inf
    cc = q * b + phi_q(q, -lam * b) / lam
    return (big_l + math.log(1.0 / BETA) / lam) / aa + n * (cc / aa - rho0)


def borne(q, n, rho0):
    big_l = math.log(len(GRILLE) / ALPHA)
    meilleur = math.inf
    for mult in GRILLE:
        pts = [math.exp(math.log(1e-4) + i * (math.log(50.0) - math.log(1e-4)) / 400) for i in range(401)]
        vals = [borne_un(mult, lam, q, n, rho0, big_l) for lam in pts]
        i0 = min(range(len(pts)), key=lambda i: vals[i])
        lo, hi = pts[max(i0 - 1, 0)], pts[min(i0 + 1, len(pts) - 1)]
        g = (math.sqrt(5.0) - 1.0) / 2.0
        c, d = hi - g * (hi - lo), lo + g * (hi - lo)
        fc, fd = borne_un(mult, c, q, n, rho0, big_l), borne_un(mult, d, q, n, rho0, big_l)
        for _ in range(60):
            if fc < fd:
                hi, d, fd = d, c, fc
                c = hi - g * (hi - lo)
                fc = borne_un(mult, c, q, n, rho0, big_l)
            else:
                lo, c, fc = c, d, fd
                d = lo + g * (hi - lo)
                fd = borne_un(mult, d, q, n, rho0, big_l)
        meilleur = min(meilleur, vals[i0], fc, fd)
    return meilleur


# valeurs recopiées de l'erratum 1 de la note « science de la détection », § 2 (rho0 = 0,10)
PUBLIE = {(0.20, 1000): 136.1, (0.20, 4000): 252.4, (0.20, 16000): 483.7,
          (0.05, 1000): 317.9, (0.05, 4000): 564.6, (0.05, 16000): 1045.1}
ecart_max = 0.0
for (q, n), v in PUBLIE.items():
    ecart_max = max(ecart_max, abs(borne(q, n, 0.10) - v))
assert ecart_max < 0.1, ecart_max
print(f"       objet de contrôle : ma réimplémentation contre les six valeurs recopiées de l'erratum 1 :"
      f" écart maximal {ecart_max:.3f}")


def horizon(theta, q, rho0, n_max=10 ** 8):
    """Plus grand n tel que B(n) <= theta (B croît avec n) ; None si B(1) > theta."""
    if borne(q, 1, rho0) > theta:
        return None
    lo, hi = 1, 2
    while hi < n_max and borne(q, hi, rho0) <= theta:
        lo, hi = hi, hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if borne(q, mid, rho0) <= theta:
            lo = mid
        else:
            hi = mid
    return lo


def horizon_trivial(theta, rho0_frac):
    """Plus grand n tel que n (1 - rho0) <= theta : sur n épisodes l'excès ne peut pas dépasser n (1 - rho0),
    quelle que soit la règle. Arithmétique exacte."""
    return int(Fraction(theta) / (1 - rho0_frac))


print("       Borne triviale : sur n épisodes, l'excès vaut au plus n (1 - rho0), sans aucune règle. L'horizon")
print("       est donc pris sur min(B(n), n (1 - rho0)). Une case marquée « t » est un horizon trivial : la règle")
print("       n'y ajoute rien, ce n'est pas un horizon d'expiration de sa garantie.")
print("       Horizon jusqu'où l'on garantit « moins de theta épisodes en excès avant l'annonce » :")
print("       " + "taux honnête".ljust(14) + "audit".ljust(8) + "".join(f"theta = {t}".rjust(15) for t in (30, 100, 300, 1000)))
HORIZONS = {}
for rho0, rho0_frac in ((0.10, Fraction(1, 10)), (0.01, Fraction(1, 100))):
    for q in (0.05, 0.20):
        ligne = ""
        for theta in (30, 100, 300, 1000):
            h_regle = horizon(theta, q, rho0)           # borne de la règle seule (calcul de la v1)
            h_triv = horizon_trivial(theta, rho0_frac)
            assert h_triv * (1 - rho0_frac) <= theta < (h_triv + 1) * (1 - rho0_frac)
            if h_regle is None or h_regle <= h_triv:
                HORIZONS[(rho0, q, theta)] = (h_triv, True, h_regle)
                ligne += f"{h_triv} t".rjust(15)
            else:
                HORIZONS[(rho0, q, theta)] = (h_regle, False, h_regle)
                ligne += f"{h_regle:15d}"
        print(f"       {rho0:<14.2f}{q:<8.2f}{ligne}")
print("       Pour mémoire, la borne de la règle seule (v1) donnait dans les cases triviales :")
for (rho0, q, theta), (h, triv, h_regle) in HORIZONS.items():
    if triv:
        ancien = "aucun" if h_regle is None else str(h_regle)
        print(f"         taux honnête {rho0:.2f}, audit {q:.2f}, theta = {theta} : {ancien} (triviale jusqu'à {h})")
n_triv = sum(1 for v in HORIZONS.values() if v[1])
print(f"       {n_triv} cases triviales sur {len(HORIZONS)} : toute la colonne theta = 30, et theta = 100 quand l'audit est à 0,05.")
assert all(HORIZONS[(r, q, 30)][1] for r in (0.10, 0.01) for q in (0.05, 0.20))
assert HORIZONS[(0.10, 0.05, 100)][1] and HORIZONS[(0.01, 0.05, 100)][1]
assert n_triv == 6
# borne basse valable pour toute règle : valeurs recopiées de la re-dérivation indépendante, § 3.5
BAS = {1000: 18, 4000: 36, 16000: 73}
consts = [v / math.sqrt(n) for n, v in BAS.items()]
c_bas = sum(consts) / len(consts)
print("       Ce qu'aucune règle n'évite (recopié de la re-dérivation, § 3.5 ; taux honnête 0,10, audit 0,20) :")
print(f"       18, 36 et 73 épisodes à 1 000, 4 000 et 16 000, soit environ {c_bas:.3f} x racine de n.")
for theta in (30, 100, 300, 1000):
    print(f"         theta = {theta:4d} : aucune règle ne garantit au-delà d'environ {(theta / c_bas) ** 2:,.0f} épisodes"
          .replace(",", " "))
print("       (extrapolation en racine des trois valeurs recopiées : un ordre de grandeur, non une borne)")
print()
print("  [C5] Le prix de N répétitions. Si la règle est remise à zéro après chaque réapprentissage et que le")
print("       risque de fausse annonce est dépensé en alpha x 6 / (pi^2 n^2) au n-ième tour (somme <= alpha) :")
for n in (1, 10, 100, 1000):
    a_n = ALPHA * 6.0 / (math.pi ** 2 * n * n)
    print(f"       tour {n:4d} : seuil de richesse 1/{a_n:.2e} ; délai multiplié par environ"
          f" {math.log(1.0 / a_n) / math.log(1.0 / ALPHA):.2f}")
print("       Le délai croît comme le logarithme du rang du tour : tenable.")
print()
print("  [C6] Objet de contrôle où « la boucle borne le dommage » est faux : l'horloge remise à zéro.")
print("       Horizon 16 000, audit 0,20, taux honnête 0,10. Si la règle repart de zéro à chaque")
print("       réapprentissage et que l'agent change de mode à ce rythme, les excès permis s'ajoutent :")
for tours in (1, 4, 16):
    n_tour = 16000 // tours
    print(f"       {tours:2d} tour(s) de {n_tour:5d} épisodes : {tours} x {borne(0.20, n_tour, 0.10):.1f}"
          f" = {tours * borne(0.20, n_tour, 0.10):.0f} épisodes en excès permis")
print(f"       Le test du plancher sur le dommage lui-même, jamais remis à zéro : {borne(0.20, 16000, 0.10):.0f}.")
print("       (la règle appliquée avec un moniteur qui ne signale rien : le dommage non signalé est alors le")
print("       dommage total ; le théorème de la re-dérivation, § 3.1, vaut pour tout moniteur : théorème repris)")
print()

# =================================================================== bloc D
print("[D] Question 5 — ce que doit valoir un signal précoce pour aller plus vite que le plancher")
print()
print("  Le saboteur endommage une part eps des épisodes en plus du taux honnête rho0. Le plancher audite une")
print("  part p. Un signal bon marché, lu sur tous les épisodes, se décale de d écarts types sur un épisode")
print("  endommagé. Information par épisode (approximation locale, eps petit) : plancher p eps^2 / (2 rho0 (1 - rho0)) ;")
print("  signal, par la somme : (eps d)^2 / 2 ; par le rapport de vraisemblance : eps^2 (exp(d^2) - 1) / 2.")
print("  Le signal va plus vite que le plancher dès que d dépasse d*, quel que soit eps.")
print("  " + "rho0".ljust(7) + "p".ljust(7) + "d* (somme)".rjust(12) + "aire sous la courbe".rjust(21)
      + "d* (rapport)".rjust(14) + "aire sous la courbe".rjust(21))
for rho0 in (0.10, 0.01):
    for p in (0.01, 0.05, 0.20, 1.00):
        x = p / (rho0 * (1.0 - rho0))
        d_s, d_l = math.sqrt(x), math.sqrt(math.log(1.0 + x))
        print(f"  {rho0:<7.2f}{p:<7.2f}{d_s:12.3f}{phi_n(d_s / math.sqrt(2.0)):21.3f}{d_l:14.3f}"
              f"{phi_n(d_l / math.sqrt(2.0)):21.3f}")
print("  Objet de contrôle : p tend vers 0, d* tend vers 0 (sans audit, tout signal valide accélère) ;")
x_un = 1.0 / (0.5 * 0.5)
print(f"  audit complet et taux honnête 0,5 : d* (somme) = {math.sqrt(x_un):.3f}.")
print("  Suppose une référence honnête exacte pour le signal : sinon son gain plafonne (loi de la référence).")
print("  Un attaquant qui divise d par deux divise par quatre la vitesse du signal ; il ne touche pas le plancher.")
print("  Plus le dommage honnête est rare, plus le plancher est difficile à battre : le signal précoce sert")
print("  surtout là où l'honnête échoue souvent, c'est-à-dire là où il confond le plus l'échec et le sabotage.")
print()

# =================================================================== bloc E
print("[E] Question 6 — la diversité effective comme ordre de coupe, et ce que l'ordre ne dit pas")
print()
print("  Un regard se tait si l'une des suppositions qu'il consomme est violée. Le système se tait si tous")
print("  ses regards se taisent. Ordre = plus petit nombre de suppositions à violer pour le faire taire.")


def ordre(systeme, prix=None):
    """systeme : liste d'ensembles de suppositions (un par regard). Renvoie (ordre, coupe) ou,
    si prix est donné, (coût minimal, coupe la moins chère)."""
    univers = sorted(set().union(*systeme))
    meilleur = None
    for k in range(1, len(univers) + 1):
        for coupe in itertools.combinations(univers, k):
            if all(set(coupe) & regard for regard in systeme):
                if prix is None:
                    return k, coupe
                cout = sum(prix[s] for s in coupe)
                if meilleur is None or cout < meilleur[0]:
                    meilleur = (cout, coupe)
    return meilleur


SONDE = {"représentations non déplacées", "l'attaque déplace ce qui est lu"}
JUGE = {"le juge de texte n'est pas simulé", "le lecteur n'est pas persuadé par le texte"}
PLANCHER = {"l'oracle reconnaît le dommage", "le tirage ne se devine pas", "référence honnête valable"}
PLANCHER_LECTEURS = PLANCHER | {"le lecteur n'est pas persuadé par le texte"}
for nom, systeme in (
        ("1 sonde", [SONDE]),
        ("12 sondes (graines, couches, familles)", [SONDE] * 12),
        ("12 sondes + juge de texte", [SONDE] * 12 + [JUGE]),
        ("12 sondes + juge + plancher (oracle par programme)", [SONDE] * 12 + [JUGE, PLANCHER]),
        ("12 sondes + juge + plancher (oracle fait de lecteurs)", [SONDE] * 12 + [JUGE, PLANCHER_LECTEURS]),
):
    k, coupe = ordre(systeme)
    print(f"  {nom:<56} M = {len(systeme):2d}   ordre {k}   une coupe : {' ; '.join(coupe)}")
print("  Douze sondes valent une sonde. Un oracle fait de lecteurs partage une supposition avec le juge :")
print("  l'ordre retombe de 3 à 2 (cause commune). Lecture des suppositions : la mienne, non mesurée.")
print()
print("  Objet de contrôle où « décorrélés, donc divers » est faux par construction : deux moniteurs dont les")
print("  fausses alertes bénignes sont indépendantes (corrélation 0) mais qui consomment la même supposition :")
print(f"  ordre {ordre([{'s'}, {'s'}])[0]} ; deux moniteurs aux fausses alertes liées mais aux suppositions"
      f" distinctes : ordre {ordre([{'s1'}, {'s2'}])[0]}.")
print()
print("  L'ordre ne dit pas le prix. Coût, pour l'attaquant, de violer chaque supposition (part de succès perdue) :")
prix_a = {"a1": 0.05, "a2": 0.05, "a3": 0.05}
prix_b = {"b1": 0.50}
ka, ca = ordre([{"a1"}, {"a2"}, {"a3"}], prix_a)
kb, cb = ordre([{"b1"}], prix_b)
print(f"  système d'ordre 3, trois suppositions à 0,05 : coupe la moins chère = {ka:.2f}")
print(f"  système d'ordre 1, une supposition à 0,50    : coupe la moins chère = {kb:.2f}")
print("  Le second résiste mieux. La diversité effective se dit donc par deux nombres : l'ordre, et le prix")
print("  de la coupe la moins chère ; et le dommage retiré vaut au plus ce prix.")
