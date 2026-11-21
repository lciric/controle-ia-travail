"""Calculs d'illustration pour la note « reponse-opus-max-banc-lois-plantees-v1.md » (v1).

Auteur : Claude Opus 5.5 (claude-opus-5-5), effort maximal, 21 novembre 2026. Pièce de travail (classe C), non contre-lue.
Aucune donnée du programme : toutes les grandeurs sont des SUPPOSITIONS D'ILLUSTRATION, déclarées dans chaque bloc.
Lois exactes quand elles existent ; Monte-Carlo seulement pour les contrôles (graines par numpy.random.SeedSequence,
dérivées par bloc). Lancer : python calculs-opus-max-banc-lois-plantees-v1.py > calculs-opus-max-banc-lois-plantees-v1-sortie.txt

Blocs :
  A  Nul par acte exact (rang de l'acte suspect parmi K continuations du jumeau au même préfixe) contre une référence
     fixe de m actes honnêtes : validité sous hétérogénéité des mondes, puissance en fonction de l'horizon n.
  B  Appariement au niveau de l'épisode (même monde, même bruit) : variance, nombre de mondes, limite de détection.
  C  Flou mesuré dans un monde jouet à lois plantées : coût de vérification par composante du dommage (lois fausses
     promues, lois vraies perdues) rapporté au coût de production ; honnête handicapé à dommage égal.
  D  Coût en heures de carte et en dollars, pilote et banc complet, sous suppositions déclarées.
  E  Taille du sous-échantillon d'un rejeu par un tiers.
  F  Témoin « juge faible qui voit tout » : effectif pour borner son aire sous la courbe.
"""

import math

import numpy as np
from scipy import stats

RACINE = 20261121  # entropie racine déclarée ; les blocs dérivent leurs graines par spawn_key
VERSION = "calculs-opus-max-banc-lois-plantees-v1"


def generateur(bloc: int) -> np.random.Generator:
    return np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=RACINE, spawn_key=(bloc,))))


def z(p: float) -> float:
    return float(stats.norm.ppf(p))


def titre(t: str) -> None:
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


# ---------------------------------------------------------------------------------------------------------------------
# Bloc A
# ---------------------------------------------------------------------------------------------------------------------
def bloc_a() -> None:
    titre("Bloc A — nul par acte exact contre référence fixe (suppositions d'illustration)")
    print("Modèle de score par acte (supposé) : s = a_monde + b_prefixe + e, e ~ N(0, 1) ; Var(a) = tau2, Var(b) = kappa2.")
    print("Les K jumeaux tirés au MÊME préfixe partagent a + b et ont leur propre e. Saboteur diffus (supposé) :")
    print("décalage mu sur une part f des actes. Seuil : alpha = 0,01 unilatéral.")
    alpha = 0.01
    za = z(1 - alpha)

    # A.1 — validité : l'acte suspect est honnête (contrôle A/A), tous ses n actes viennent d'UN SEUL monde (un déploiement)
    rng = generateur(1)
    tau2, kappa2 = 0.25, 0.25
    m, n, K, reps = 400, 200, 8, 4000
    rejets_ref = 0
    rejets_rang = 0
    nul_rang_moy, nul_rang_var = (K + 2) / 2.0, K * (K + 2) / 12.0
    for _ in range(reps):
        # référence fixe : m actes honnêtes de m mondes et préfixes distincts
        ref = rng.normal(0, math.sqrt(tau2), m) + rng.normal(0, math.sqrt(kappa2), m) + rng.normal(0, 1, m)
        a = rng.normal(0, math.sqrt(tau2))  # un seul monde pour le suspect
        b = rng.normal(0, math.sqrt(kappa2), n)
        s = a + b + rng.normal(0, 1, n)
        # test de la référence fixe : moyenne du suspect contre moyenne de la référence, variance estimée sur la référence
        v = ref.var(ddof=1)
        t_ref = (s.mean() - ref.mean()) / math.sqrt(v / n + v / m)
        rejets_ref += t_ref > za
        # rang parmi K jumeaux au même préfixe (égalités impossibles en continu)
        jumeaux = (a + b)[:, None] + rng.normal(0, 1, (n, K))
        rangs = 1 + (s[:, None] > jumeaux).sum(axis=1)
        u = (rangs.sum() - n * nul_rang_moy) / math.sqrt(n * nul_rang_var)
        rejets_rang += u > za
    fpr_ref, fpr_rang = rejets_ref / reps, rejets_rang / reps
    se = math.sqrt(alpha * (1 - alpha) / reps)
    print(f"\nA.1  Contrôle A/A, n = {n} actes d'un seul monde, tau2 = {tau2}, kappa2 = {kappa2}, m = {m}, K = {K}, "
          f"{reps} répétitions :")
    print(f"     taux de fausses alertes, référence fixe : {fpr_ref:.4f} ; rang contre le jumeau : {fpr_rang:.4f} "
          f"(nominal {alpha} ; écart type Monte-Carlo {se:.4f})")
    print("     Lecture : la référence fixe absorbe mal l'effet du monde du déploiement (écart systématique) ; le rang au")
    print("     même préfixe est exact par construction (test de Monte-Carlo de Barnard), à l'approximation normale près.")

    # A.1 bis — même contrôle, n actes tirés de n mondes distincts (nul homogène) : la référence fixe redevient valide
    rng = generateur(2)
    rejets_ref = 0
    for _ in range(reps):
        ref = rng.normal(0, math.sqrt(tau2 + kappa2 + 1), m)
        s = rng.normal(0, math.sqrt(tau2 + kappa2 + 1), n)
        v = ref.var(ddof=1)
        rejets_ref += (s.mean() - ref.mean()) / math.sqrt(v / n + v / m) > za
    print(f"A.1b Même contrôle, n actes de n mondes distincts : fausses alertes de la référence fixe {rejets_ref / reps:.4f}.")

    # A.2 — puissance (lois exactes à l'approximation normale) en fonction de l'horizon n
    print("\nA.2  Puissance à alpha = 0,01 en fonction de l'horizon n (approximation normale ; actes de mondes distincts) :")
    print("     z connu = nul connu exactement (aucune référence) ; réf. m = 400 = référence fixe de 400 actes honnêtes,")
    print("     qui doit absorber Var totale = tau2 + kappa2 + 1 ; rang K = rang contre K jumeaux au même préfixe,")
    print("     dont le bruit n'est que e (le préfixe est conditionné).")
    sig_tot = math.sqrt(tau2 + kappa2 + 1)
    for f, mu in ((0.2, 0.5), (0.1, 0.5), (0.3, 0.3)):
        print(f"\n     part f = {f}, décalage mu = {mu} (en unités de e) :")
        print("       n       z connu   réf. m=400   rang K=4   rang K=8   rang K=32")
        for n_ in (50, 100, 200, 400, 800, 1600, 3200, 6400, 25600):
            p_z = stats.norm.cdf(f * mu * math.sqrt(n_) / sig_tot - za)  # nul connu, bruit total (actes de mondes distincts)
            p_ref = stats.norm.cdf(f * mu / (sig_tot * math.sqrt(1 / n_ + 1 / 400)) - za)
            ligne = f"       {n_:<7d} {p_z:8.3f}   {p_ref:9.3f}"
            for K_ in (4, 8, 32):
                # E[R - (K+2)/2] par acte décalé = K (Phi(mu/sqrt2) - 1/2) ; Var nulle du rang = K (K+2) / 12
                gain = K_ * (stats.norm.cdf(mu / math.sqrt(2)) - 0.5)
                p_r = stats.norm.cdf(f * gain * math.sqrt(n_) / math.sqrt(K_ * (K_ + 2) / 12.0) - za)
                ligne += f"   {p_r:8.3f}"
            print(ligne)
        plafond = stats.norm.cdf(f * mu * math.sqrt(400) / sig_tot - za)
        print(f"       plafond de la référence fixe quand n -> infini : {plafond:.3f}")

    # A.3 — contrôle Monte-Carlo de la puissance du rang (objet vrai par construction)
    rng = generateur(3)
    f, mu, K, n_, reps = 0.2, 0.5, 8, 800, 3000
    rej = 0
    for _ in range(reps):
        dec = (rng.random(n_) < f) * mu
        e = rng.normal(0, 1, n_) + dec
        jum = rng.normal(0, 1, (n_, K))
        rangs = 1 + (e[:, None] > jum).sum(axis=1)
        u = (rangs.sum() - n_ * (K + 2) / 2) / math.sqrt(n_ * K * (K + 2) / 12)
        rej += u > za
    gain = K * (stats.norm.cdf(mu / math.sqrt(2)) - 0.5)
    p_th = stats.norm.cdf(f * gain * math.sqrt(n_) / math.sqrt(K * (K + 2) / 12.0) - za)
    print(f"\nA.3  Contrôle : puissance du rang simulée (f = {f}, mu = {mu}, K = {K}, n = {n_}, {reps} rép.) = "
          f"{rej / reps:.3f} ; loi approchée = {p_th:.3f}.")
    print("     Efficacité relative asymptotique du rang contre le z à nul connu (bruit e seul) : 3/pi x K/(K+2) =",
          ", ".join(f"K={k}: {3 / math.pi * k / (k + 2):.3f}" for k in (4, 8, 16, 32)))

    # A.4 — contrôle plus dur : le préfixe dépend des actes passés du suspect (contexte qui se construit)
    rng = generateur(6)
    T, ep, K, reps = 20, 10, 8, 4000
    rej_rang, rej_ref, corr = 0, 0, []
    ref_pool = []
    for _ in range(2000):  # référence fixe : actes honnêtes d'épisodes indépendants, même dynamique
        a = rng.normal(0, 0.5)
        b, prec = 0.0, 0.0
        for t in range(T):
            b = 0.7 * b + 0.5 * prec
            e = rng.normal(0, 1)
            ref_pool.append(a + b + e)
            prec = e
    ref_pool = np.array(ref_pool)
    m_ref = 400
    for _ in range(reps):
        a = rng.normal(0, 0.5)  # un seul monde, ep épisodes
        rangs, scores = [], []
        for _e in range(ep):
            b, prec = 0.0, 0.0
            for t in range(T):
                b = 0.7 * b + 0.5 * prec  # le préfixe hérite de l'acte précédent DU SUSPECT
                e = rng.normal(0, 1)
                s = a + b + e
                jum = a + b + rng.normal(0, 1, K)
                rangs.append(1 + int((s > jum).sum()))
                scores.append(s)
                prec = e
        rangs = np.array(rangs)
        n_ = len(rangs)
        u = (rangs.sum() - n_ * (K + 2) / 2) / math.sqrt(n_ * K * (K + 2) / 12)
        rej_rang += u > za
        corr.append(np.corrcoef(rangs[:-1], rangs[1:])[0, 1])
        ref = rng.choice(ref_pool, m_ref, replace=False)
        v = ref.var(ddof=1)
        rej_ref += (np.mean(scores) - ref.mean()) / math.sqrt(v / n_ + v / m_ref) > za
    print(f"\nA.4  Préfixe qui hérite des actes passés du suspect (b_t = 0,7 b_t-1 + 0,5 e_t-1), un seul monde, {ep} épisodes")
    print(f"     de {T} actes, K = {K}, {reps} répétitions : fausses alertes du rang {rej_rang / reps:.4f} (nominal {alpha}) ;")
    print(f"     corrélation moyenne des rangs successifs {np.mean(corr):+.4f} (attendu 0 : rangs indépendants sous le nul) ;")
    print(f"     fausses alertes de la référence fixe (m = {m_ref}, actes d'autres mondes) {rej_ref / reps:.4f}.")


# ---------------------------------------------------------------------------------------------------------------------
# Bloc B
# ---------------------------------------------------------------------------------------------------------------------
def bloc_b() -> None:
    titre("Bloc B — appariement par monde et par bruit (suppositions d'illustration)")
    print("Dommage D = effet du monde w (Var tau2) + reste e (Var sigma2) ; ICC = tau2 / (tau2 + sigma2) ; sigma_tot = 1.")
    print("Apparié : suspect et K jumeaux sur le même monde ; Var(écart) = sigma2 (1 + 1/K) par monde.")
    print("Non apparié : jumeaux sur un autre monde ; Var(écart) = 2 tau2 + sigma2 (1 + 1/K).")
    print("Nombre de mondes J pour voir un excès de dommage delta = 0,3 sigma_tot (bilatéral 5 %, puissance 0,8) :")
    zz = (z(0.975) + z(0.8)) ** 2
    print("     ICC     K=1 app/non   K=4 app/non   K=8 app/non   K=16 app/non")
    for icc in (0.0, 0.3, 0.6, 0.9):
        tau2, sig2 = icc, 1 - icc
        ligne = f"     {icc:<6.1f}"
        for K in (1, 4, 8, 16):
            va = sig2 * (1 + 1 / K)
            vn = 2 * tau2 + sig2 * (1 + 1 / K)
            ligne += f"   {math.ceil(zz * va / 0.09):4d}/{math.ceil(zz * vn / 0.09):4d}"
        print(ligne)
    print("\nLimite de détection de l'excès de dommage, en unités de sigma (écart type intra-monde du jumeau),")
    print("à 5 % de fausses alertes unilatérales et 95 % de détection : (z_0,95 + z_0,95) x sqrt((1 + 1/K) / J) :")
    for J in (30, 100, 300, 1000):
        print(f"     J = {J:<5d}" + "".join(f"   K={K}: {2 * z(0.95) * math.sqrt((1 + 1 / K) / J):.3f}" for K in (4, 8, 16)))


# ---------------------------------------------------------------------------------------------------------------------
# Bloc C
# ---------------------------------------------------------------------------------------------------------------------
def n_par_bras(d: float, a: float, puissance: float) -> float:
    """Effectif par bras d'un test z unilatéral à deux bras (variance 1 par observation), effet d."""
    return 2.0 * (z(1 - a) + z(puissance)) ** 2 / d ** 2


def puissance_z(n_bras: float, d: float, a: float) -> float:
    return float(stats.norm.cdf(d * math.sqrt(n_bras / 2.0) - z(1 - a)))


def bloc_c() -> None:
    titre("Bloc C — flou mesuré dans un monde jouet à lois plantées (suppositions d'illustration)")
    print("Monde jouet (supposé) : M lois candidates ; M1 vraies d'effet d (en écarts types du bruit), les autres d'effet 0.")
    print("Honnête (supposé) : budget B réparti également, deux bras par candidate, test z unilatéral au seuil alpha/M ;")
    print("le registre affirme les candidates significatives. Coûts comptés en échantillons du monde.")
    print("Vérifier une affirmation (commission) : la rejouer à puissance 0,9 contre son effet affirmé, seuil 0,05/|affirmées|.")
    print("Vérifier une omission : re-tester chaque candidate non affirmée à puissance 0,9, seuil 0,05/|non affirmées|.")
    alpha = 0.05
    print("\n     M    M1   d     B (prod.)   perdues  fausses   coût commission  rho_c   coût omission  rho_o")
    for M, M1, d in ((20, 4, 0.5), (50, 5, 0.5), (100, 10, 0.4), (20, 4, 0.3)):
        a_test = alpha / M
        nb = n_par_bras(d, a_test, 0.8)  # budget de l'honnête : puissance 0,8 par loi vraie
        B = M * 2 * nb
        pw = puissance_z(nb, d, a_test)
        perdues = M1 * (1 - pw)
        fausses = (M - M1) * a_test
        affirmees = M1 * pw + fausses
        non_aff = M - affirmees
        c_com = affirmees * 2 * n_par_bras(d, alpha / max(affirmees, 1.0), 0.9)
        c_om = non_aff * 2 * n_par_bras(d, alpha / non_aff, 0.9)
        print(f"     {M:<4d} {M1:<4d} {d:<5.2f} {B:10.0f}   {perdues:6.2f}   {fausses:6.3f}   {c_com:14.0f}   "
              f"{c_com / B:5.2f}   {c_om:12.0f}   {c_om / B:5.2f}")
    print("     Lecture : rejouer ce qui est affirmé coûte une fraction de la production ; prouver qu'une loi vraie manque")
    print("     coûte autant que refaire la recherche. Le flou du banc est donc PAR COMPOSANTE du dommage.")

    # Honnête handicapé à dommage égal (budget réduit), et ce que l'égalité ne donne pas
    print("\nC.2  Honnête handicapé par réduction du budget (fraction h), monde M = 20, M1 = 4, d = 0,5 :")
    M, M1, d = 20, 4, 0.5
    a_test = alpha / M
    nb = n_par_bras(d, a_test, 0.8)
    perdues_h = lambda h: M1 * (1 - puissance_z(h * nb, d, a_test))
    print("     h      lois vraies perdues   lois fausses promues")
    for h in (1.0, 0.8, 0.6, 0.5, 0.4, 0.3):
        print(f"     {h:<5.2f}  {perdues_h(h):10.3f}            {(M - M1) * a_test:8.3f}")
    for cible in (1.5, 2.0, 2.5):
        lo, hi = 0.01, 1.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if perdues_h(mid) > cible:
                lo = mid
            else:
                hi = mid
        print(f"     pertes cibles {cible} (honnête plein : {perdues_h(1.0):.2f}) -> h* = {hi:.3f} ; fausses promues inchangées "
              f"({(M - M1) * a_test:.3f}) : l'égalité sur une composante ne donne pas l'égalité sur l'autre.")

    # Contrôles Monte-Carlo : l'oracle lit exactement une dose plantée ; A/A
    rng = generateur(4)
    reps = 4000
    n_bras = int(round(nb))
    def episode(rng_, retire=0):
        eff = np.array([d] * M1 + [0.0] * (M - M1))
        diff = rng_.normal(eff, math.sqrt(2.0 / n_bras))
        affirme = diff / math.sqrt(2.0 / n_bras) > z(1 - a_test)
        if retire:  # dose plantée par programme : retirer du registre « retire » lois vraies affirmées
            idx = np.flatnonzero(affirme[:M1])[:retire]
            affirme[idx] = False
        return (~affirme[:M1]).sum(), affirme[M1:].sum()
    honn = np.array([episode(rng) for _ in range(reps)])
    plant = []
    rng2 = generateur(5)
    rng3 = generateur(5)  # même graine : même monde et même bruit que l'épisode apparié
    for _ in range(reps):
        h_ = episode(rng2)
        p_ = episode(rng3, retire=1)
        plant.append((p_[0] - h_[0], p_[1] - h_[1]))
    plant = np.array(plant)
    print(f"\nC.3  Contrôles ({reps} mondes) : pertes moyennes de l'honnête {honn[:, 0].mean():.3f} (loi : {perdues_h(1.0):.3f}) ;")
    print(f"     fausses promues moyennes {honn[:, 1].mean():.4f} (loi : {(M - M1) * a_test:.4f}).")
    print(f"     Dose plantée « une loi vraie retirée », lue en apparié (même monde, même bruit) : excès de pertes moyen "
          f"{plant[:, 0].mean():.3f}, excès de fausses {plant[:, 1].mean():.3f} ;")
    print(f"     l'excès est exactement 1 quand l'honnête avait au moins une loi vraie affirmée : part de ces mondes "
          f"{(plant[:, 0] == 1).mean():.3f} (sinon 0 : la dose ne peut pas s'exercer).")


# ---------------------------------------------------------------------------------------------------------------------
# Bloc D
# ---------------------------------------------------------------------------------------------------------------------
def bloc_d() -> None:
    titre("Bloc D — coût en heures de carte, modèle de 8 milliards de paramètres (suppositions déclarées)")
    prix_h = 1.22  # USD par heure, A100 80 Go, carte + stockage, relevé du registre des dépenses (19 novembre)
    print(f"Prix : {prix_h} USD/h (A100 80 Go, relevé du registre des dépenses, 19 novembre). Débits [de mémoire, à mesurer] :")
    print("sortie 2 000 à 6 000 jetons/s en lot ; préremplissage 10 000 à 40 000 jetons/s ; passe avant des activations au")
    print("débit du préremplissage divisé par 2 (crochets). Épisode : T actes ; 1 500 jetons d'en-tête ; 200 d'observation")
    print("et 250 de sortie par acte ; registre 300. Sans cache de préfixe (pessimiste) puis avec (optimiste).")

    def couts(J, doses, K, niveaux_h, aa, T, frac_branche, K_acte, juge_faible=True, frac_attr=0.25, R_attr=4):
        ep_par_monde = doses + K + niveaux_h + aa
        sortie_ep = T * 250 + 300
        ctx = [1500 + t * 450 for t in range(T)]
        pre_sans = sum(ctx)
        pre_avec = 1500 + T * 450
        acts_branches = doses * T * frac_branche
        sortie_br = acts_branches * K_acte * 250
        pre_br_sans = acts_branches * K_acte * (1500 + T * 450 / 2)
        pre_br_avec = acts_branches * (1500 + T * 450 / 2)
        act_pass = ep_par_monde * (1500 + T * 450) + acts_branches * K_acte * (1500 + T * 450 / 2)
        juge = ep_par_monde * (1500 + T * 450 + 500) if juge_faible else 0
        # attribution du dommage par acte : depuis le préfixe du suspect, R_attr déroulés honnêtes jusqu'au registre, avec
        # l'acte du suspect et avec un acte du jumeau (2 x R_attr), sur une part frac_attr des actes, tirée par le défenseur
        acts_attr = doses * T * frac_attr
        sortie_attr = acts_attr * 2 * R_attr * ((T / 2) * 250 + 300)
        pre_attr_sans = acts_attr * 2 * R_attr * (T / 2) * (1500 + 0.75 * T * 450)
        pre_attr_avec = acts_attr * 2 * R_attr * (1500 + T * 450)
        res = {}
        for nom, deb_s, deb_p, pre_ep, pre_b, pre_a in (("pessimiste", 2000, 10000, pre_sans, pre_br_sans, pre_attr_sans),
                                                         ("optimiste", 6000, 40000, pre_avec, pre_br_avec, pre_attr_avec)):
            sec = J * (ep_par_monde * (sortie_ep / deb_s + pre_ep / deb_p) + sortie_br / deb_s + pre_b / deb_p
                       + act_pass / (deb_p / 2) + juge / deb_p)
            sec_attr = J * (sortie_attr / deb_s + pre_a / deb_p)
            res[nom] = sec / 3600
            res[nom + "_attr"] = sec_attr / 3600
        return ep_par_monde * J, res

    cas = (
        ("Prototype sur processeur (agents scriptés)", None),
        ("Pilote : 30 mondes, 2 doses, K = 8, 4 niveaux de handicap, 1 A/A, T = 12, 25 % d'actes bifurqués x 16",
         dict(J=30, doses=2, K=8, niveaux_h=4, aa=1, T=12, frac_branche=0.25, K_acte=16)),
        ("Banc : 300 mondes, 3 doses, K = 16, 6 niveaux, 1 A/A, T = 16, 25 % d'actes bifurqués x 32",
         dict(J=300, doses=3, K=16, niveaux_h=6, aa=1, T=16, frac_branche=0.25, K_acte=32)),
        ("Banc x 2 grammaires x 2 familles d'organismes (i, ii) avec jumeau à traitement égal",
         dict(J=1200, doses=3, K=16, niveaux_h=6, aa=1, T=16, frac_branche=0.25, K_acte=32)),
    )
    for nom, p in cas:
        if p is None:
            print(f"\n  {nom} : 0 USD (processeur local) ; aucun modèle.")
            continue
        n_ep, r = couts(**p)
        lo, hi = r["optimiste"], r["pessimiste"]
        print(f"\n  {nom}")
        print(f"     épisodes complets : {n_ep} ; heures de carte : {lo:.1f} à {hi:.1f} ; "
              f"coût de carte : {lo * prix_h:.1f} à {hi * prix_h:.1f} USD")
        print(f"     avec frais fixes (montage, téléchargement du modèle, essais à blanc : +3 h) et facteur 2 de marge :"
              f" {(lo + 3) * prix_h * 2:.0f} à {(hi + 3) * prix_h * 2:.0f} USD")
        la, ha = r["optimiste_attr"], r["pessimiste_attr"]
        print(f"     en plus, attribution du dommage par acte (25 % des actes suspects, 2 x 4 déroulés) : {la:.1f} à "
              f"{ha:.1f} h de carte, soit {la * prix_h:.1f} à {ha * prix_h:.1f} USD avant marge")
    # Juges boîte noire par fournisseur : prix relevés sur la page de prix versée le 21 novembre (USD par million de jetons)
    print("\n  Juges boîte noire lus par fournisseur payant (prix relevés le 21 novembre : modèle léger 0,30 en entrée et")
    print("  2,50 en sortie ; modèle de pointe 3,00 et 15,00 USD par million de jetons) ; entrée = trace entière + 500 jetons")
    print("  de consigne ; sortie supposée 1 000 jetons, réflexion comprise :")
    for nom, J, ep_monde, T in (("pilote", 30, 15, 12), ("banc", 300, 26, 16), ("banc x 4", 1200, 26, 16)):
        n_ep = J * ep_monde
        ent = n_ep * (1500 + T * 450 + 500) / 1e6
        sor = n_ep * 1000 / 1e6
        print(f"     {nom:9s} : {n_ep:6d} épisodes ; {ent:7.1f} M jetons lus ; léger {ent * 0.30 + sor * 2.50:7.1f} USD ; "
              f"pointe {ent * 3.00 + sor * 15.00:8.1f} USD (par juge et par passage)")
    print("\n  Hors carte : réglage fin des organismes (ii) et de leurs jumeaux à traitement égal, plusieurs graines ;")
    print("  juges boîte noire forts par fournisseur payant ; rejeu par un tiers (bloc E) ; ces lignes vont au devis.")
    print("  Stockage : une activation de 4 096 coordonnées en demi-précision = 8 Ko par jeton et par couche ; un épisode")
    print("  de 8 000 jetons sur 3 couches = 8 000 x 3 x 8 Ko = 196 Mo : on garde les jetons et les scores par acte, et l'on")
    print("  régénère les activations à la demande (passe avant unique sur les jetons enregistrés).")


# ---------------------------------------------------------------------------------------------------------------------
# Bloc E
# ---------------------------------------------------------------------------------------------------------------------
def bloc_e() -> None:
    titre("Bloc E — rejeu par un tiers : taille du sous-échantillon tiré par une balise publique")
    print("Si une part eps des épisodes ne se reproduit pas (monde, oracle, activations hors tolérance), le tiers en voit au")
    print("moins un avec probabilité 0,95 dès n = ceil(ln 0,05 / ln(1 - eps)) épisodes tirés au hasard :")
    for eps in (0.01, 0.02, 0.05, 0.10, 0.20):
        print(f"     eps = {eps:<5.2f} -> n = {math.ceil(math.log(0.05) / math.log(1 - eps))}")


# ---------------------------------------------------------------------------------------------------------------------
# Bloc F
# ---------------------------------------------------------------------------------------------------------------------
def hanley_mcneil(A: float, n1: int, n0: int) -> float:
    q1, q2 = A / (2 - A), 2 * A * A / (1 + A)
    return math.sqrt((A * (1 - A) + (n1 - 1) * (q1 - A * A) + (n0 - 1) * (q2 - A * A)) / (n1 * n0))


def bloc_f() -> None:
    titre("Bloc F — témoin « juge faible qui voit tout » : effectif pour que la borne haute à 95 % reste sous le seuil de mort")
    print("n épisodes suspects et n jumeaux ; aire vraie du juge faible A_w ; seuil de mort A_mort (le banc meurt si le juge")
    print("faible l'atteint) ; erreur type de Hanley et McNeil ; effectif minimal pour que A_w + 1,645 x ET < A_mort :")
    print("     A_w    A_mort=0,70  A_mort=0,75  A_mort=0,80")
    for A in (0.55, 0.60, 0.65):
        ligne = f"     {A:<5.2f}"
        for Am in (0.70, 0.75, 0.80):
            n = 5
            while A + z(0.95) * hanley_mcneil(A, n, n) >= Am and n < 100000:
                n += 1
            ligne += f"   {n:10d}"
        print(ligne)


if __name__ == "__main__":
    print(f"{VERSION} — entropie racine {RACINE} ; numpy {np.__version__}")
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    bloc_e()
    bloc_f()
