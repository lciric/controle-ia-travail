"""Calcul exact, sans tirage, de ce que la théorie dit d'avance de la prédiction P3 de la ligne 3 — v1.

Objet : le bras « collège à cinq juges » du banc scripté de l'étage 1 (lois 1 et 4 du préenregistrement
`preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, 4e3680d9…, section « Plan d'analyse », lignes 203 à 220).
Ce programme n'ouvre aucun fichier en lecture, ne fait aucun tirage, ne lit aucune mesure de l'étage 1 et ne lance
pas le banc. Bibliothèque standard seule.

Ce qui est calculé, par cellule (loi, profil, ρ de la grille) :
  1. la loi exacte des 32 configurations de votes dans chaque classe (fractions exactes) ;
  2. l'erreur équilibrée exacte de chaque règle fixe : quotas 0 à 6 (dont l'unanimité, « au moins un » et la
     majorité stricte), et la règle de Bayes (la meilleure fonction des cinq votes, toutes règles confondues) ;
  3. la règle « en population » (étalonnage infini, classes égales) des bras « poids égaux », C et P, avec les
     égalités exactes au seuil signalées (là où un étalonnage fini bascule d'un côté ou de l'autre) ;
  4. pour le bras « poids égaux », l'espérance exacte à étalonnage fini (25, 50, 100, 200 témoins), par convolution
     (double précision, erreur de l'ordre de 1e-12), et l'écart type par réplique de son écart apparié à la
     majorité stricte, d'où une puissance d'équivalence.
Ce qui n'est pas calculé : la perte des bras C et P à étalonnage fini (la loi de leurs poids estimés porte sur des
tirages multinomiaux à 32 cases par classe, hors d'atteinte d'une énumération). Une borne tient pourtant pour toute
taille d'étalonnage : l'espérance de l'erreur équilibrée d'une règle gelée sur l'étalonnage, lue sur une moitié
indépendante, ne descend jamais sous celle de la règle de Bayes.

Usage : python3 calcul_exact_p3_ligne_3_v1.py SORTIE.json
"""
import itertools
import json
import math
import platform
import statistics
import sys
from fractions import Fraction

VERSION = "calcul-exact-p3-ligne-3-v1"
J = 5
RHOS = [Fraction(n, 100) for n in (0, 15, 30, 45, 60, 75, 90)]
ERREURS = list(itertools.product((0, 1), repeat=J))
REPLIQUES = 2000
# n de la grille → (bons d'étalonnage, mauvais d'étalonnage, bons de lecture, mauvais de lecture),
# selon le partage du texte (choix 1 de l'additif 1) : plafond(c/2) bons et plancher(c/2) mauvais à l'étalonnage.
PARTAGES = {50: (13, 12, 12, 13), 100: (25, 25, 25, 25), 200: (50, 50, 50, 50), 400: (100, 100, 100, 100)}


def fr(n, d=100):
    return Fraction(n, d)


def profils_de(loi):
    """(taux d'erreur sur les bons = vrais rejetés, taux d'erreur sur les mauvais = faux acceptés), par juge."""
    p = {
        "egal_0.05": ([fr(5)] * J, [fr(5)] * J),
        "egal_0.1": ([fr(10)] * J, [fr(10)] * J),
        "egal_0.2": ([fr(20)] * J, [fr(20)] * J),
        "egal_0.3": ([fr(30)] * J, [fr(30)] * J),
        "severe": ([fr(30)] * J, [fr(10)] * J),
        "indulgent": ([fr(10)] * J, [fr(30)] * J),
    }
    if loi == 1:
        inegal = [fr(10), fr(15), fr(20), fr(25), fr(30)]
        p["inegal"] = (list(inegal), list(inegal))
    return p


SYMETRIQUES = ("egal_0.05", "egal_0.1", "egal_0.2", "egal_0.3")
DISSYMETRIQUES = ("severe", "indulgent")


def produit(xs):
    r = Fraction(1)
    for x in xs:
        r *= x
    return r


def loi_erreurs(loi, p, rho):
    """Loi exacte des 32 configurations d'erreurs d'une classe, taux p (cinq fractions)."""
    P = {}
    if loi == 1:
        # Choc commun : avec probabilité ρ tous lisent le même tirage U (erreur du juge j si U < p(j)) ; sinon chacun le sien.
        for e in ERREURS:
            indep = produit(p[j] if e[j] else 1 - p[j] for j in range(J))
            bas = min([p[j] for j in range(J) if e[j]] + [Fraction(1)])
            haut = max([p[j] for j in range(J) if not e[j]] + [Fraction(0)])
            commun = max(Fraction(0), bas - haut)
            P[e] = rho * commun + (1 - rho) * indep
    elif loi == 4:
        # Blocs {1, 2}, {3, 4}, {5} ; taux égaux entre juges.
        if len(set(p)) != 1:
            raise ValueError("loi 4 : taux égaux entre juges")
        pp = p[0]
        q_tous = rho / 3
        q_bloc = (rho - rho / 3) / (1 - rho / 3)

        def paire(a, b):
            commun = pp if (a, b) == (1, 1) else (1 - pp if (a, b) == (0, 0) else Fraction(0))
            return q_bloc * commun + (1 - q_bloc) * (pp if a else 1 - pp) * (pp if b else 1 - pp)

        for e in ERREURS:
            tous = pp if sum(e) == J else (1 - pp if sum(e) == 0 else Fraction(0))
            P[e] = q_tous * tous + (1 - q_tous) * paire(e[0], e[1]) * paire(e[2], e[3]) * (pp if e[4] else 1 - pp)
    else:
        raise ValueError("loi inconnue")
    if sum(P.values()) != 1:
        raise AssertionError("la loi des erreurs ne somme pas à 1")
    return P


def cov_erreurs(E):
    m = [sum(P for e, P in E.items() if e[j]) for j in range(J)]
    C = [[sum(P for e, P in E.items() if e[j] and e[k]) - m[j] * m[k] for k in range(J)] for j in range(J)]
    return m, C


def rho_moyenne_plantee(Cg, Cb):
    """Formule poolée du texte : somme des covariances hors diagonale / ((J − 1) × somme des variances)."""
    tot = sum(Cg[j][k] + Cb[j][k] for j in range(J) for k in range(J))
    tr = sum(Cg[j][j] + Cb[j][j] for j in range(J))
    return (tot - tr) / ((J - 1) * tr)


def taux(acceptes, Pg, Pb):
    """(faux acceptés, vrais rejetés, erreur équilibrée) d'une règle donnée par l'ensemble des configurations acceptées."""
    acceptes = set(acceptes)
    fa = sum((Pb[v] for v in acceptes), Fraction(0))
    vr = sum((Pg[v] for v in ERREURS if v not in acceptes), Fraction(0))
    return fa, vr, (fa + vr) / 2


def quota(q):
    return [v for v in ERREURS if sum(v) >= q]


def resoudre(A, b):
    """Élimination de Gauss en fractions exactes ; None si la matrice ne s'inverse pas."""
    n = len(A)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if M[r][c] != 0), None)
        if pivot is None:
            return None
        M[c], M[pivot] = M[pivot], M[c]
        inv = 1 / M[c][c]
        M[c] = [x * inv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def poids_C_population(Cg, Cb, p_b, p_m):
    """Bras C, étalonnage infini, classes égales : w = (S + λ I)⁻¹ d, S covariance des votes ±1 à l'intérieur des classes."""
    S = [[2 * (Cg[j][k] + Cb[j][k]) for k in range(J)] for j in range(J)]
    d = [2 * (1 - p_b[j] - p_m[j]) for j in range(J)]
    tr = sum(S[j][j] for j in range(J))
    lam = Fraction(1, 10) * tr / J
    w = None
    if tr > 0:
        A = [[S[j][k] + (lam if j == k else 0) for k in range(J)] for j in range(J)]
        w = resoudre(A, d)
    if w is None or sum(w) / J <= 0:
        return [Fraction(1)] * J, True, False
    moyenne = sum(w) / J
    borne = [min(max(x, moyenne / 5), 5 * moyenne) for x in w]
    return borne, False, borne != w


def poids_P_population(Cg, Cb, p_b, p_m):
    """Bras P, étalonnage infini : exactitude équilibrée − 0,5, plancher 0,05 ; paire à ρ d'erreurs > 0,5 : poids divisés par 2."""
    w = [max(Fraction(1, 2) - (p_b[j] + p_m[j]) / 2, Fraction(1, 20)) for j in range(J)]
    S = [[Cg[j][k] + Cb[j][k] for k in range(J)] for j in range(J)]
    paires_au_fil = []
    for j in range(J):
        for k in range(j + 1, J):
            if S[j][k] > 0 and 4 * S[j][k] ** 2 > S[j][j] * S[k][k]:
                w[j] /= 2
                w[k] /= 2
            elif S[j][k] > 0 and 4 * S[j][k] ** 2 == S[j][j] * S[k][k]:
                paires_au_fil.append([j + 1, k + 1])
    return w, paires_au_fil


def regle_lineaire(w, p_b, p_m):
    """Seuil au milieu des deux moyennes de classe du score ; rend (acceptées, à égalité exacte au seuil)."""
    seuil = sum(w[j] * (p_m[j] - p_b[j]) for j in range(J))
    acceptes, egalites = [], []
    for v in ERREURS:
        s = sum(w[j] * (2 * v[j] - 1) for j in range(J))
        if s > seuil:
            acceptes.append(v)
        elif s == seuil:
            egalites.append(v)
    return acceptes, egalites, seuil


def nom_de_regle(acceptes):
    a = set(acceptes)
    for q in range(0, J + 2):
        if a == set(quota(q)):
            return {0: "constante_tout_notable", 1: "au_moins_un", 3: "majorite_stricte", 5: "unanimite",
                    6: "constante_rien"}.get(q, f"quota_{q}")
    return "autre_regle_ponderee"


def f(x):
    return float(x)


def fiche_regle(acceptes, Pg, Pb):
    fa, vr, ee = taux(acceptes, Pg, Pb)
    return {"regle": nom_de_regle(acceptes), "configurations_acceptees": len(set(acceptes)),
            "faux_acceptes": f(fa), "vrais_rejetes": f(vr), "erreur_equilibree": f(ee)}, ee


def convoluer(a, b):
    r = [0.0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0.0:
            continue
        for j2, y in enumerate(b):
            r[i + j2] += x * y
    return r


def puissances_de_convolution(base, tailles):
    """Loi de la somme de k copies indépendantes, pour chaque k demandé."""
    sortie = {}
    courant = [1.0]
    for k in range(1, max(tailles) + 1):
        courant = convoluer(courant, base)
        if k in tailles:
            sortie[k] = list(courant)
    return sortie


NORMALE = statistics.NormalDist()


def puissance_equivalence(delta_vrai, marge, erreur_type, alpha):
    """Deux tests unilatéraux au niveau alpha, approximation normale : P(intervalle tout entier dans ± marge)."""
    if erreur_type <= 0:
        return 1.0 if abs(delta_vrai) < marge else 0.0
    z = NORMALE.inv_cdf(1 - alpha)
    p = NORMALE.cdf((marge - delta_vrai) / erreur_type - z) - NORMALE.cdf((-marge - delta_vrai) / erreur_type + z)
    return max(0.0, p)


def poids_egaux_a_etalonnage_fini(Pg, Pb, ee_quota, ee_majorite):
    """Espérance exacte de l'erreur équilibrée du bras « poids égaux » (seuil au milieu, estimé), par taille d'étalonnage.

    Le bras accepte un témoin de c votes « notable » si c > (A / kb + B / km) / 2, où A et B sont les nombres de votes
    « notable » sur les kb bons et les km mauvais de l'étalonnage ; une égalité exacte rend « non notable ».
    Il joue donc le quota q = plancher(x) + 1, x = (A km + B kb) / (2 kb km)."""
    pg = [f(sum((P for v, P in Pg.items() if sum(v) == c), Fraction(0))) for c in range(J + 1)]
    pb = [f(sum((P for v, P in Pb.items() if sum(v) == c), Fraction(0))) for c in range(J + 1)]
    lois_A = puissances_de_convolution(pg, {kb for kb, _, _, _ in PARTAGES.values()})
    lois_B = puissances_de_convolution(pb, {km for _, km, _, _ in PARTAGES.values()})
    sortie = {}
    for n, (kb, km, lg, lb) in sorted(PARTAGES.items()):
        A, B = lois_A[kb], lois_B[km]
        cumul = [0.0]
        for y in B:
            cumul.append(cumul[-1] + y)  # cumul[i] = P(B < i)
        p_quota = [0.0] * (J + 2)
        p_egalite = 0.0
        for a, pa in enumerate(A):
            if pa == 0.0:
                continue
            for k in range(0, J + 1):
                # plancher(x) = k  ⇔  2 k kb km ≤ a km + B kb < 2 (k + 1) kb km
                bas = max(0, -((-(2 * k * kb * km - a * km)) // kb))
                haut = max(0, -((-(2 * (k + 1) * kb * km - a * km)) // kb))
                bas, haut = min(bas, len(B)), min(haut, len(B))
                if haut > bas:
                    p_quota[k + 1] += pa * (cumul[haut] - cumul[bas])
                # égalité exacte : a km + B kb = 2 k kb km
                reste = 2 * k * kb * km - a * km
                if reste >= 0 and reste % kb == 0 and reste // kb < len(B):
                    p_egalite += pa * B[reste // kb]
        esperance = math.fsum(p_quota[q] * f(ee_quota[q]) for q in range(1, J + 2))
        # Écart apparié par réplique, D = EE(poids égaux) − EE(majorité stricte), sur la moitié « lecture ».
        moments = []
        for q in range(1, J + 2):
            if q == 3:
                moments.append((p_quota[q], 0.0, 0.0))
                continue
            bande = range(q, 3) if q < 3 else range(3, q)
            pi_b = math.fsum(pb[c] for c in bande)
            pi_g = math.fsum(pg[c] for c in bande)
            signe = 1.0 if q < 3 else -1.0
            moyenne = 0.5 * signe * (pi_b - pi_g)
            variance = 0.25 * (pi_b * (1 - pi_b) / lb + pi_g * (1 - pi_g) / lg)
            moments.append((p_quota[q], moyenne, variance))
        d_moy = math.fsum(p * m for p, m, _ in moments)
        d_var = math.fsum(p * (v + m * m) for p, m, v in moments) - d_moy * d_moy
        ecart_type = math.sqrt(max(d_var, 0.0))
        erreur_type = ecart_type / math.sqrt(REPLIQUES)
        sortie[str(kb + km)] = {
            "n_de_la_grille": n, "bons_et_mauvais_d_etalonnage": [kb, km], "bons_et_mauvais_de_lecture": [lg, lb],
            "probabilite_de_chaque_quota_joue": {str(q): p_quota[q] for q in range(1, J + 2)},
            "probabilite_d_une_egalite_exacte_au_seuil": p_egalite,
            "erreur_equilibree_esperance": esperance,
            "ecart_a_la_majorite_stricte_esperance": esperance - f(ee_majorite),
            "controle_ecart_par_les_moments": d_moy,
            "ecart_type_par_replique_de_l_ecart_apparie": ecart_type,
            "erreur_type_de_la_moyenne_sur_2000_repliques": erreur_type,
            "demi_largeur_a_95_pour_cent_sur_2000_repliques": 1.959963984540054 * erreur_type,
            "puissance_d_equivalence_marge_0.01_alpha_0.05": puissance_equivalence(d_moy, 0.01, erreur_type, 0.05),
            "puissance_d_equivalence_marge_0.02_alpha_0.05": puissance_equivalence(d_moy, 0.02, erreur_type, 0.05),
            "puissance_d_equivalence_marge_0.01_alpha_0.05_sur_84": puissance_equivalence(d_moy, 0.01, erreur_type, 0.05 / 84),
        }
    return sortie


def etalon_bras_fixes(regles_fixes, Pg, Pb):
    """Espérance exacte et erreur type sur 2 000 répliques de l'erreur équilibrée des bras sans étalonnage, par n."""
    sortie = {}
    for nom, acceptes in regles_fixes.items():
        fa, vr, ee = taux(acceptes, Pg, Pb)
        par_n = {}
        for n, (_, _, lg, lb) in sorted(PARTAGES.items()):
            var = 0.25 * (f(fa) * (1 - f(fa)) / lb + f(vr) * (1 - f(vr)) / lg)
            par_n[str(n)] = math.sqrt(var / REPLIQUES)
        sortie[nom] = {"faux_acceptes": f(fa), "vrais_rejetes": f(vr), "erreur_equilibree": f(ee),
                       "erreur_type_de_la_moyenne_sur_2000_repliques_par_n": par_n}
    return sortie


def cellule(loi, nom, p_b, p_m, rho):
    Eb = loi_erreurs(loi, p_b, rho)
    Em = loi_erreurs(loi, p_m, rho)
    Pg = {v: Eb[tuple(1 - x for x in v)] for v in ERREURS}  # bon : « notable » = sans erreur
    Pb = dict(Em)                                            # mauvais : « notable » = erreur
    mg, Cg = cov_erreurs(Eb)
    mb, Cb = cov_erreurs(Em)
    if mg != list(p_b) or mb != list(p_m):
        raise AssertionError("taux marginaux différents des taux plantés")
    plantee = rho_moyenne_plantee(Cg, Cb)

    ee_quota = {}
    fiches = {}
    for q in range(0, J + 2):
        fiche, ee = fiche_regle(quota(q), Pg, Pb)
        ee_quota[q] = ee
        fiches[f"quota_{q}"] = fiche
    ee_maj = ee_quota[3]
    meilleur_q = min(range(0, J + 2), key=lambda q: (ee_quota[q], q))

    bayes = [v for v in ERREURS if Pg[v] > Pb[v]]
    egalites_bayes = [v for v in ERREURS if Pg[v] == Pb[v] and Pg[v] > 0]
    fiche_bayes, ee_bayes = fiche_regle(bayes, Pg, Pb)
    if ee_bayes != sum((min(Pg[v], Pb[v]) for v in ERREURS), Fraction(0)) / 2:
        raise AssertionError("erreur de Bayes incohérente")

    # « Poids égaux » en population : accepte c > x, x = (moyenne des votes « notable » chez les bons + chez les mauvais) / 2.
    x = (sum(1 - p for p in p_b) + sum(p_m)) / 2
    q_lettre = math.floor(x) + 1
    egalite_pe = (x == math.floor(x))
    fiche_pe, ee_pe = fiche_regle(quota(q_lettre), Pg, Pb)
    fiche_pe_autre, ee_pe_autre = (fiche_regle(quota(q_lettre - 1), Pg, Pb) if egalite_pe else (None, None))

    w_c, repli_c, coupe_c = poids_C_population(Cg, Cb, p_b, p_m)
    acc_c, eg_c, seuil_c = regle_lineaire(w_c, p_b, p_m)
    fiche_c, ee_c = fiche_regle(acc_c, Pg, Pb)
    fiche_c_autre, ee_c_autre = (fiche_regle(acc_c + eg_c, Pg, Pb) if eg_c else (None, None))

    w_p, au_fil_p = poids_P_population(Cg, Cb, p_b, p_m)
    acc_p, eg_p, seuil_p = regle_lineaire(w_p, p_b, p_m)
    fiche_p, ee_p = fiche_regle(acc_p, Pg, Pb)
    fiche_p_autre, ee_p_autre = (fiche_regle(acc_p + eg_p, Pg, Pb) if eg_p else (None, None))

    def gain(ee):
        return None if ee is None else f(ee_maj - ee)

    moyenne_w_c = sum(w_c) / J
    moyenne_w_p = sum(w_p) / J
    regles_fixes = {"F_majorite_stricte": quota(3), "U_unanimite": quota(5), "F_au_moins_un": quota(1),
                    "S_1_juge_seul": [v for v in ERREURS if v[0]], "S_5_juge_seul": [v for v in ERREURS if v[4]]}
    sortie = {
        "loi": loi, "profil": nom, "rho_grille": f(rho),
        "valeur_plantee_rho_moyenne": f(plantee),
        "regles_fixes_par_quota": fiches,
        "meilleur_quota": meilleur_q,
        "regle_de_bayes": dict(fiche_bayes, configurations_a_vraisemblances_egales=len(egalites_bayes)),
        "majorite_stricte_est_la_regle_de_bayes_exactement": bool(ee_maj == ee_bayes),
        "gain_maximal_de_toute_regle_sur_la_majorite_stricte": gain(ee_bayes),
        "gain_du_meilleur_quota_sur_la_majorite_stricte": gain(ee_quota[meilleur_q]),
        "poids_egaux_en_population": {
            "seuil_en_nombre_de_votes": f(x), "egalite_exacte_au_seuil": bool(egalite_pe),
            "lettre_du_code_egalite_non_notable": fiche_pe, "si_l_egalite_bascule_notable": fiche_pe_autre,
            "gain_sur_la_majorite_stricte_lettre": gain(ee_pe), "gain_sur_la_majorite_stricte_si_bascule": gain(ee_pe_autre)},
        "bras_C_en_population": {
            "poids_rapportes_a_leur_moyenne": [f(w / moyenne_w_c) for w in w_c], "repli_poids_egaux": repli_c,
            "poids_bornes": coupe_c, "seuil": f(seuil_c), "configurations_a_egalite_exacte_au_seuil": len(eg_c),
            "lettre_du_code_egalite_non_notable": fiche_c, "si_l_egalite_bascule_notable": fiche_c_autre,
            "gain_sur_la_majorite_stricte_lettre": gain(ee_c), "gain_sur_la_majorite_stricte_si_bascule": gain(ee_c_autre),
            "gain_sur_poids_egaux_en_population_lettre": f(ee_pe - ee_c)},
        "bras_P_en_population": {
            "poids_rapportes_a_leur_moyenne": [f(w / moyenne_w_p) for w in w_p],
            "paires_a_correlation_exactement_0.5": au_fil_p, "seuil": f(seuil_p),
            "configurations_a_egalite_exacte_au_seuil": len(eg_p),
            "lettre_du_code_egalite_non_notable": fiche_p, "si_l_egalite_bascule_notable": fiche_p_autre,
            "gain_sur_la_majorite_stricte_lettre": gain(ee_p), "gain_sur_la_majorite_stricte_si_bascule": gain(ee_p_autre)},
        "poids_egaux_a_etalonnage_fini_par_taille": poids_egaux_a_etalonnage_fini(Pg, Pb, ee_quota, ee_maj),
        "etalon_des_bras_sans_etalonnage": etalon_bras_fixes(regles_fixes, Pg, Pb),
    }
    exacts = {"ee_maj": ee_maj, "ee_bayes": ee_bayes, "ee_c": ee_c, "ee_c_autre": ee_c_autre, "ee_p": ee_p,
              "ee_p_autre": ee_p_autre, "ee_pe": ee_pe, "ee_pe_autre": ee_pe_autre, "plantee": plantee}
    return sortie, exacts


def gardes():
    """Contrôles sur cas connus (formules du texte) ; une valeur fausse arrête le programme."""
    rapport = {}
    # Majorité de cinq juges indépendants au taux 0,2 : P(au moins trois erreurs) = 0,05792.
    s, e = cellule(1, "egal_0.2", [fr(20)] * J, [fr(20)] * J, Fraction(0))
    attendu = Fraction(5792, 100000)
    if e["ee_maj"] != attendu:
        raise AssertionError("garde : majorité de cinq indépendants")
    rapport["majorite_de_cinq_independants_au_taux_0.2"] = f(e["ee_maj"])
    # Loi 1 à taux égaux : ρ moyenne plantée = ρ. Loi 4 : 7 ρ / 15 (texte, « Métrique »).
    for rho in RHOS:
        _, e1 = cellule(1, "egal_0.2", [fr(20)] * J, [fr(20)] * J, rho)
        _, e4 = cellule(4, "egal_0.2", [fr(20)] * J, [fr(20)] * J, rho)
        _, e4s = cellule(4, "severe", [fr(30)] * J, [fr(10)] * J, rho)
        if e1["plantee"] != rho or e4["plantee"] != 7 * rho / 15 or e4s["plantee"] != 7 * rho / 15:
            raise AssertionError("garde : valeur plantée")
    rapport["valeur_plantee_loi_1_egale_rho_et_loi_4_egale_7_rho_sur_15"] = True
    # Loi 4 : corrélation ρ dans un bloc, ρ / 3 entre blocs.
    E = loi_erreurs(4, [fr(20)] * J, fr(60))
    m, C = cov_erreurs(E)
    v = m[0] * (1 - m[0])
    if C[0][1] / v != fr(60) or C[2][3] / v != fr(60) or C[0][2] / v != fr(20) or C[0][4] / v != fr(20):
        raise AssertionError("garde : corrélations de la loi 4")
    rapport["loi_4_correlation_de_bloc_et_entre_blocs"] = True
    # À ρ = 0 les lois 1 et 4 sont la même loi.
    if loi_erreurs(1, [fr(30)] * J, Fraction(0)) != loi_erreurs(4, [fr(30)] * J, Fraction(0)):
        raise AssertionError("garde : lois 1 et 4 à ρ = 0")
    rapport["lois_1_et_4_identiques_a_rho_nul"] = True
    # Artefact : une règle codée à l'envers (accepter la minorité) doit s'écarter de la majorité.
    Pg = {vv: E[tuple(1 - x for x in vv)] for vv in ERREURS}
    envers = [vv for vv in ERREURS if sum(vv) <= 2]
    if taux(envers, Pg, E)[2] <= taux(quota(3), Pg, E)[2]:
        raise AssertionError("garde : la règle à l'envers n'est pas détectée")
    rapport["artefact_regle_a_l_envers_detecte"] = True
    # Convolution : la somme de 13 lois reste une loi.
    lois = puissances_de_convolution([0.1, 0.2, 0.3, 0.2, 0.1, 0.1], {13})
    if abs(math.fsum(lois[13]) - 1.0) > 1e-12:
        raise AssertionError("garde : convolution")
    rapport["convolution_somme_a_un"] = True
    return rapport


def syntheses(cellules, exacts):
    def choisir(loi, profils, rhos=None):
        return [(c, e) for c, e in zip(cellules, exacts)
                if c["loi"] == loi and c["profil"] in profils and (rhos is None or c["rho_grille"] in rhos)]

    def maxi(valeurs):
        valeurs = [v for v in valeurs if v is not None]
        return max(valeurs) if valeurs else None

    def mini(valeurs):
        valeurs = [v for v in valeurs if v is not None]
        return min(valeurs) if valeurs else None

    def resume(selection):
        tailles = ("25", "50", "100", "200")
        r = {
            "cellules": len(selection),
            "majorite_stricte_est_la_regle_de_bayes_dans_toutes": all(e["ee_maj"] == e["ee_bayes"] for _, e in selection),
            "gain_maximal_de_toute_regle_sur_la_majorite_stricte_max": maxi(
                c["gain_maximal_de_toute_regle_sur_la_majorite_stricte"] for c, _ in selection),
            "gain_maximal_de_toute_regle_sur_la_majorite_stricte_min": mini(
                c["gain_maximal_de_toute_regle_sur_la_majorite_stricte"] for c, _ in selection),
            "bras_C_population_gain_sur_majorite_lettre_min_max": [
                mini(c["bras_C_en_population"]["gain_sur_la_majorite_stricte_lettre"] for c, _ in selection),
                maxi(c["bras_C_en_population"]["gain_sur_la_majorite_stricte_lettre"] for c, _ in selection)],
            "bras_C_population_gain_sur_majorite_si_bascule_min_max": [
                mini(c["bras_C_en_population"]["gain_sur_la_majorite_stricte_si_bascule"] for c, _ in selection),
                maxi(c["bras_C_en_population"]["gain_sur_la_majorite_stricte_si_bascule"] for c, _ in selection)],
            "bras_P_population_gain_sur_majorite_lettre_min_max": [
                mini(c["bras_P_en_population"]["gain_sur_la_majorite_stricte_lettre"] for c, _ in selection),
                maxi(c["bras_P_en_population"]["gain_sur_la_majorite_stricte_lettre"] for c, _ in selection)],
            "bras_P_population_gain_sur_majorite_si_bascule_min_max": [
                mini(c["bras_P_en_population"]["gain_sur_la_majorite_stricte_si_bascule"] for c, _ in selection),
                maxi(c["bras_P_en_population"]["gain_sur_la_majorite_stricte_si_bascule"] for c, _ in selection)],
            "cellules_ou_le_seuil_de_poids_egaux_tombe_sur_une_egalite_exacte": sum(
                1 for c, _ in selection if c["poids_egaux_en_population"]["egalite_exacte_au_seuil"]),
        }
        par_taille = {}
        for t in tailles:
            ecarts = [c["poids_egaux_a_etalonnage_fini_par_taille"][t]["ecart_a_la_majorite_stricte_esperance"] for c, _ in selection]
            # Borne : gain maximal de toute règle étalonnée sur « poids égaux » à cette taille = EE(poids égaux) − EE(Bayes).
            bornes = [c["poids_egaux_a_etalonnage_fini_par_taille"][t]["erreur_equilibree_esperance"]
                      - c["regle_de_bayes"]["erreur_equilibree"] for c, _ in selection]
            demi = [c["poids_egaux_a_etalonnage_fini_par_taille"][t]["demi_largeur_a_95_pour_cent_sur_2000_repliques"] for c, _ in selection]
            puiss = [c["poids_egaux_a_etalonnage_fini_par_taille"][t]["puissance_d_equivalence_marge_0.01_alpha_0.05_sur_84"] for c, _ in selection]
            par_taille[t] = {
                "poids_egaux_moins_majorite_stricte_min_max": [min(ecarts), max(ecarts)],
                "gain_maximal_de_toute_regle_sur_poids_egaux_max": max(bornes),
                "demi_largeur_a_95_pour_cent_de_l_ecart_apparie_max": max(demi),
                "puissance_d_equivalence_marge_0.01_holm_84_min": min(puiss),
            }
        r["poids_egaux_a_etalonnage_fini"] = par_taille
        return r

    blocs_hauts = (0.6, 0.75, 0.9)
    ensembles = {
        "echangeables_lecture_etroite_loi_1_quatre_profils_egaux": choisir(1, SYMETRIQUES),
        "echangeables_ajout_de_la_lecture_large_loi_1_severe_et_indulgent": choisir(1, DISSYMETRIQUES),
        "blocs_loi_4_rho_0.6_ou_plus_quatre_profils_egaux": choisir(4, SYMETRIQUES, blocs_hauts),
        "blocs_loi_4_rho_0.6_ou_plus_severe_et_indulgent": choisir(4, DISSYMETRIQUES, blocs_hauts),
        "blocs_loi_4_toutes_valeurs_de_rho_quatre_profils_egaux": choisir(4, SYMETRIQUES),
        "inegaux_loi_1_profil_inegal_hors_P3": choisir(1, ("inegal",)),
    }
    return {nom: resume(sel) for nom, sel in ensembles.items()}


def main(argv):
    if len(argv) != 2:
        raise SystemExit("usage : python3 calcul_exact_p3_ligne_3_v1.py SORTIE.json")
    rapport_gardes = gardes()
    cellules, exacts = [], []
    for loi in (1, 4):
        for nom, (p_b, p_m) in profils_de(loi).items():
            for rho in RHOS:
                c, e = cellule(loi, nom, p_b, p_m, rho)
                cellules.append(c)
                exacts.append(e)
    resultat = {
        "version": VERSION,
        "nature": ("calcul exact sur les lois du banc à cinq juges (lois 1 et 4) ; aucun tirage, aucune graine, aucun "
                   "fichier lu, aucune mesure de l'étage 1 ; fractions exactes pour les règles fixes et les règles en "
                   "population, double précision pour les convolutions de l'étalonnage fini"),
        "python": platform.python_version(),
        "texte_qui_fait_foi": "preenregistrement-ligne-3-votes-effectifs-juges-v7.md, "
                              "4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0",
        "gardes": rapport_gardes,
        "syntheses": syntheses(cellules, exacts),
        "cellules": cellules,
    }
    with open(argv[1], "x", encoding="utf-8") as fichier:
        json.dump(resultat, fichier, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False)
        fichier.write("\n")
    print(json.dumps({"gardes": rapport_gardes, "syntheses": resultat["syntheses"]}, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main(sys.argv)
